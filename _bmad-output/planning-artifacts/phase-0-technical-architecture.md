# Phase 0 Technical Architecture — NC

**Author:** Snnair
**Date:** 2026-03-19
**Version:** 0.3
**Companion to:** PRD (prd.md), Soul Document Architecture Spec (soul-document-architecture-spec-2026-03-16.md)

---

## 1. Overview

Phase 0 is NC's first deployable product — a **privacy-first personal AI companion** that ships multiple interaction surfaces designed to meet the user where they already are:

1. **NC Keyboard** (iOS + Android): Custom keyboard that lives inside every messaging app. NC sees conversation context and delivers intent interpretation + reply suggestions inline — zero app-switching, zero copy-paste.
2. **Conversational companion** (mobile app + web): User shares or pastes a message, asks NC for interpretation, contextual explanation, and reply suggestions. Streaming responses. The deliberate-reflection mode.
3. **Real-time overlay** (Chrome extension): Intent prediction on incoming WhatsApp Web messages, displayed as a non-intrusive overlay before the user replies.
4. **Share Sheet** (iOS + Android): User long-presses a message in any app → shares to NC → gets instant interpretation. Two taps.
5. **Notification Listener + Floating Bubble** (Android only): NC reads incoming message notifications and proactively shows intent interpretation as a floating bubble — fully passive, zero user action.

All surfaces are powered by the same inference pipeline: Soul Document + Relationship Context injected into Llama 3.1 70B at inference time, served on NC's own GPU infrastructure.

**Positioning:** Personal AI, not enterprise AI. *Your AI. Not your company's.*

**Key architectural principle:** Privacy is **architectural** (verifiable via open-source serving code), not just **contractual** (a DPA you have to trust). Users can inspect the inference server code to verify no data is retained.

---

## 2. Model Selection

| Role | Model | Rationale |
|---|---|---|
| **Primary** | Llama 3.1 70B quantised (AWQ/GPTQ 4-bit) | Best open-source quality for relational reasoning. 70B parameter count provides the nuance needed for intent interpretation grounded in personality context. Quantisation reduces GPU memory to ~35GB, enabling single-GPU serving. |
| **Fast fallback** | Llama 3.1 8B quantised | For simpler queries (e.g., clarification questions, short messages with clear intent) where 70B quality is unnecessary. Reduces cost and latency on straightforward requests. |

**Why open-source, not API providers (OpenAI/Anthropic)?**

| Factor | Open-source (Llama) | API provider |
|---|---|---|
| Privacy verification | Users can inspect serving code — verifiable zero-retention | Trust-based — DPA is a legal document, not a technical guarantee |
| Data residency | NC controls server location (UK/EU) | Provider decides; SCCs required for non-EU processing |
| Cost at scale | Predictable GPU cost; no per-token markup | Per-token pricing; costs scale linearly with usage |
| Vendor lock-in | None — model weights are portable | High — prompt engineering, fine-tuning, API integration all provider-specific |
| Model quality | Competitive at 70B for structured reasoning tasks | Marginally better on some benchmarks; gap narrowing |
| Fine-tuning | Full control — LoRA on own data, own schedule | Limited — provider-specific fine-tuning APIs, restrictions on data |

**Recommendation:** Start with Llama 3.1 70B. If a newer open-source model (e.g., Llama 4, Mistral Large) demonstrates meaningfully better relational reasoning performance before Phase 0 launch, swap in — the architecture is model-agnostic. The serving infrastructure doesn't change.

---

## 3. Infrastructure

### Serving Architecture

```
Client (NC Keyboard / Mobile App / Web / Extension / Notification Listener)
  │
  ├── HTTPS/TLS 1.3
  │
  ▼
NC Inference API (stateless, zero-persistence)
  │
  ├── Request: message + Soul Document excerpt + Relationship Context
  │
  ▼
Serverless GPU (RunPod / Modal)
  │
  ├── Llama 3.1 70B (primary) or 8B (fallback)
  ├── vLLM serving engine (open-source)
  ├── Streaming response via SSE
  │
  ▼
Response streamed back to client
  │
  └── All request data discarded after response complete
```

### Infrastructure Decisions

| Decision | Choice | Rationale |
|---|---|---|
| **Compute** | Serverless GPU (RunPod / Modal) with warm pool | Pay-per-use with a **minimum 1 warm instance** to eliminate cold starts. Scale up automatically under load. Scale to warm-pool minimum (not zero) when idle. See Section 13A for cold start mitigation. |
| **Serving engine** | vLLM | Open-source, high-throughput, KV cache optimisation. Supports streaming, quantised models, and continuous batching. |
| **API layer** | Lightweight Python API (FastAPI) | Stateless request handler. Receives request, forwards to vLLM, streams response, discards all data. |
| **Persistence** | None on server | Zero server-side storage. No database, no logs containing user data, no message content retention. |
| **Code** | Open-source serving code | Published on GitHub. Users can audit: no data retention, no telemetry on message content, no side-channel exfiltration. |

**Recommendation:** Start with RunPod for alpha (simpler setup, GPU availability). Evaluate Modal for beta if auto-scaling behaviour is better. Both support vLLM containers.

**Warm Pool Strategy (cold start mitigation):**
- **Alpha (50 users):** 1 always-on reserved GPU instance (~£150–200/month). This eliminates cold starts entirely. Serverless burst instances handle overflow only.
- **Beta (500 users):** 1–2 reserved base-load instances + serverless burst. Reserved instances handle P95 traffic; serverless absorbs spikes.
- **Trade-off:** Warm pool increases base cost from £25–40/month to ~£150–200/month at alpha. But a 30–120 second cold start on first request of the day would destroy keyboard UX and first impressions. The warm pool cost is justified.
- **Health ping:** Cron job pings the warm instance every 5 minutes with a lightweight health check to prevent provider-side idle shutdown.

### Stateless Design

Every inference request is **self-contained**:
- Client sends: message text + **pruned** Soul Document excerpt + Relationship Context for the sender + system prompt
- Server processes: inference only — no state lookup, no session tracking, no user identification
- Server returns: streaming response (interpretation, confidence, reply suggestions)
- Server discards: everything — no logs, no cache, no residual data

This means:
- Server restart loses nothing (there was nothing to lose)
- No user data exists on any NC server at any time except during the ~2–5 seconds of active inference
- Horizontal scaling is trivial — any server instance can handle any request

### Context Pruning Strategy

**Problem:** Injecting a full Soul Document + full Relationship Context + conversation history into every request causes prompt bloat — high token costs, risk of hitting context limits, and "lost in the middle" degradation where the model ignores earlier context.

**Solution: Client-side semantic retrieval** — only send the 3–5 most relevant Soul Document traits and relationship patterns for the current conversation.

| Component | Pruning Method | Target Token Budget |
|---|---|---|
| **Soul Document** | On-device semantic similarity (lightweight embedding model or keyword matching) selects top-k traits relevant to the message | ~300–500 tokens (not full document) |
| **Relationship Context** | Only the sender's context is included. Recent interaction patterns weighted higher than historical. | ~200–400 tokens |
| **Conversation history** | Sliding window: last 3–5 exchanges. Older context summarised into a single paragraph by a previous inference call (or dropped). | ~300–500 tokens |
| **System prompt** | Static, pre-optimised | ~200–300 tokens |
| **User message** | Verbatim | Variable |
| **Total budget** | — | **~1,500–2,000 tokens in** (well within 70B context window) |

**Implementation options for on-device semantic retrieval:**
- **Phase 0 (simple):** Keyword/tag matching — Soul Document traits are tagged with relationship categories (e.g., `conflict`, `affection`, `stress`). Client matches message keywords to tags and selects top-k.
- **Phase 0+ (better):** Lightweight local embedding model (e.g., `all-MiniLM-L6-v2` at 23MB) running on-device. Embeds the incoming message and retrieves nearest Soul Document chunks via cosine similarity. Libraries: `sqlite-vss` (mobile), `transformers.js` (web/extension).
- **Phase 1:** Server-side RAG if Soul Documents grow beyond what client-side retrieval can handle efficiently.

---

## 4. Cost Projections

### Per-Query Cost Model

| Component | Cost per query (est.) |
|---|---|
| Llama 3.1 70B inference (RunPod A100 80GB, ~500 tokens in + ~300 tokens out) | £0.003–0.005 |
| Llama 3.1 8B inference (fallback) | £0.0005–0.001 |
| API compute overhead | negligible |
| **Blended average** (80% 70B / 20% 8B) | **~£0.004** |

### Monthly Cost by Scale

| Stage | Users | Queries/user/day | Monthly queries | Inference cost | Warm pool cost | **Total monthly** |
|---|---|---|---|---|---|---|
| **Alpha** | 50 | 5 | 7,500 | £25–40 | £150–200 | **£175–240** |
| **Beta** | 500 | 8 | 120,000 | £300–500 | £200–300 (1–2 reserved) | **£500–800** |
| **Growth** (1,000 users) | 1,000 | 10 | 300,000 | £800–1,200 | £300–400 (2 reserved) | **£1,100–1,600** |

**Recommendation:** The warm pool adds ~£150–200/month at alpha — a significant increase from the original £25–40 estimate, but essential for keyboard UX. A 30–120 second cold start on first request would kill adoption. The cost inflection point is now ~1,500 active users at ~10 queries/day, where monthly cost reaches £1,500+. This is the point where freemium conversion revenue must begin covering infrastructure.

**Cost reduction levers:**
- **Hybrid inference (beta):** Local on-device model handles 40–60% of simple intents at zero cloud cost, reducing per-query spend significantly.
- **Context pruning:** Sending ~1,500 tokens instead of ~4,000+ per request reduces inference time and cost by ~50%.
- **8B aggressive routing:** Route more queries to 8B (£0.001/query vs £0.004/query for 70B) once quality thresholds are validated.
- **Spot/preemptible GPUs:** RunPod spot instances are 30–50% cheaper. Acceptable for burst capacity (not warm pool).

---

## 5. Latency

| Mode | Target | Rationale |
|---|---|---|
| **NC Keyboard** (reply suggestions) | First token: **< 1.5 seconds**. Full suggestion: **< 3 seconds** at P95 | Keyboard is the highest-latency-sensitivity surface. User is mid-conversation, expecting near-instant help. Must feel comparable to Apple QuickType. Warm pool + 8B routing for simple intents makes this achievable. |
| **Conversational companion** | First token: **< 2 seconds**. Full response: **< 5 seconds** at P95 | User-initiated, not real-time. Users expect "thinking" time when asking a question. Streaming makes 2–5s feel responsive. |
| **Real-time overlay** | First token: **< 2 seconds**. Streaming overlay render as tokens arrive | Relaxed from original 800ms target. 70B model on serverless GPU cannot hit 800ms. Users see streaming prediction appearing progressively — perceived latency is first-token, not total. |
| **Fallback (8B)** | First token: **< 500ms**. Full response: **< 2 seconds** | For simpler queries routed to the 8B model. |

**Phase 0 vs. Phase 1 latency:**

The original PRD specifies < 800ms end-to-end for the overlay. This target was designed for a fine-tuned model with optimised inference (Phase 1). Phase 0's Llama 3.1 70B on serverless GPU will not hit 800ms — streaming mitigates the perceived latency. Phase 1 re-targets < 800ms with a fine-tuned, smaller model.

**Recommendation:** Accept 2–5s streaming for Phase 0. The conversational companion is user-initiated (latency tolerance is higher). The overlay uses streaming render — first intent label appears quickly, confidence and contextual note fill in progressively. Track P95 latency to ensure Phase 0 is usable, but do not gate launch on 800ms.

### Hybrid Inference Strategy (Local + Cloud)

**Problem:** Even with a warm pool, cloud inference adds network latency. For the keyboard surface, users expect near-instant response — 2–5 seconds feels slow when you're mid-conversation.

**Solution:** Route simple intents to a **local on-device model** and reserve cloud 70B for complex relational analysis.

| Intent Complexity | Model | Where | Latency |
|---|---|---|---|
| **Simple** — clear intent, short message, low ambiguity (e.g., "ok", "thanks", "see you at 7") | Llama 3.2 1B/3B or similar small model | **On-device** (iOS Core ML / Android NNAPI) | **< 200ms** |
| **Medium** — some ambiguity, needs basic relationship context | Llama 3.1 8B | **Cloud** (fallback model) | **< 1s** |
| **Complex** — high ambiguity, emotional subtext, needs full Soul Document context | Llama 3.1 70B | **Cloud** (primary model) | **< 3s** |

**Complexity routing logic (client-side):**
1. Message length < 10 words AND no question marks AND sender has low-ambiguity history → route to local model
2. Message contains emotional language, questions, or sender has high-ambiguity history → route to cloud 8B or 70B
3. User explicitly asks for "deep analysis" or companion mode → always 70B

**Phase 0 implementation:**
- **Alpha:** Cloud-only (8B + 70B). Local model is a beta feature — requires on-device model optimisation and platform-specific NPU integration.
- **Beta:** Ship local 1B/3B model for simple intent classification. Cloud 70B for everything else.
- **Benefit:** Keyboard feels instant for 40–60% of messages (simple intents). Complex messages still get full 70B analysis.

**On-device model options:**
| Model | Size | Platform support | Quality |
|---|---|---|---|
| Llama 3.2 1B (quantised) | ~500MB | iOS Core ML, Android NNAPI | Sufficient for simple intent classification |
| Llama 3.2 3B (quantised) | ~1.5GB | iOS Core ML, Android NNAPI | Better for medium-complexity messages |
| Phi-3 Mini (3.8B, quantised) | ~1.8GB | iOS Core ML, Android NNAPI | Strong reasoning for size; alternative to Llama 3.2 |
| Custom distilled model (Phase 1) | ~200–500MB | Both platforms | Fine-tuned on NC's own data — best quality/size ratio, but requires Phase 0 dataset first |

---

## 6. Privacy Architecture

### Zero-Persistence Model

| Layer | Data | Retention |
|---|---|---|
| **Client (mobile/web/extension)** | Soul Document, Relationship Context, reflection journal, correction history | Persistent, AES-256 encrypted, device-only |
| **In-flight (HTTPS)** | Message + Soul Document excerpt + Relationship Context | TLS 1.3 encrypted in transit; exists only during transmission |
| **Server (inference)** | Full request payload during inference | **Exists only during the ~2–5 second inference window. Discarded immediately after response stream completes.** |
| **Server (at rest)** | Nothing | No database, no log files containing user data, no message cache |

### Verification

- **Open-source serving code:** The NC inference server code is published on GitHub. Anyone can audit the code to verify:
  - No data is written to disk
  - No data is sent to third parties
  - No telemetry contains message content or Soul Document fields
  - Request payloads are discarded after response
- **No DPA required:** Because NC controls the servers and the code is auditable, there is no third-party data processor. GDPR compliance is architectural, not contractual.
- **Server monitoring:** NC monitors server health (uptime, latency, error rate) but **not** request content. Monitoring telemetry contains only: timestamp, response time, token count, model used, error code (if any). No user identity, no message content, no Soul Document content.

### Privacy Dashboard (Auditability as Product)

Beyond open-source code, NC provides a **user-facing Privacy Dashboard** that makes zero-retention tangible:

| Feature | What it shows | Why it matters |
|---|---|---|
| **Request Inspector** | The exact JSON payload sent to the server for the last N requests (stored client-side only) | User can see exactly what NC sent — no hidden data |
| **Deletion Receipt** | Timestamp + cryptographic hash confirming server-side payload discard | Proof, not promise |
| **Data Map** | Visual diagram: "Your data lives HERE (your device) and NOWHERE else" | Non-technical users understand the architecture at a glance |
| **Open Source Link** | Direct link to the NC inference server GitHub repo with the relevant code highlighted | One tap to verify |

**Positioning:** This turns privacy from a trust exercise into a **product feature**. Competitors say "we don't store your data." NC says "here's the proof — inspect it yourself."

### Soul Document Privacy

| Property | Implementation |
|---|---|
| Storage | Client-only, AES-256 encrypted at rest |
| Transmission | Only with per-session user consent (FR54–56) |
| Server retention | Zero — discarded after inference response |
| Partner access | Architecturally prohibited (FR46) |
| Deletion | User-initiated, ≤ 3 taps, confirmed with timestamp (FR24) |

---

## 7. Fine-Tuning Strategy

### Three-Stage Progression

| Stage | Timing | Method | Data Source | Goal |
|---|---|---|---|---|
| **Stage 1** | Phase 0 launch | Base Llama 3.1 70B + prompt engineering | Soul Document + Relationship Context as prompt context | Baseline intent interpretation quality. No fine-tuning. System prompt defines NC's role, intent categories, output format. |
| **Stage 2** | Month 3–6 | LoRA fine-tune on relationship/communication data | Publicly available relationship communication datasets, curated by NC team | Improved relational reasoning. Model better understands relationship dynamics, stress patterns, conflict archetypes. |
| **Stage 3** | Month 6+ | LoRA fine-tune on NC's own annotated dataset | User corrections from Phase 0 (both companion and overlay). PII-redacted, consent-gated. | NC-specific intent prediction accuracy. This dataset feeds Phase 1's dedicated model. |

**Recommendation:** Stage 1 (prompt engineering only) is the right launch approach. Prompt engineering on 70B is surprisingly effective for structured reasoning tasks — especially with the Soul Document providing rich context. Don't fine-tune until you have enough NC-specific data (target: 5,000+ correction pairs) to meaningfully improve on the base model. Premature fine-tuning on generic data may not help and could introduce bias.

### LoRA Configuration (Stages 2–3)

| Parameter | Value | Rationale |
|---|---|---|
| Rank | 16–32 | Balance between adaptation capacity and training cost |
| Alpha | 32–64 | Standard scaling factor |
| Target modules | q_proj, v_proj, k_proj, o_proj | Attention layers — where relational reasoning happens |
| Training data size | Stage 2: ~10K examples. Stage 3: 5K+ NC corrections | Minimum viable fine-tuning sets |
| Evaluation | Held-out test set of annotated intent pairs | Accuracy on ambiguous-valence messages |

---

## 8. Client Architecture

### Surfaces

| Surface | Technology | Primary Function | Friction Level |
|---|---|---|---|
| **NC Keyboard** | Custom keyboard (iOS: Swift, Android: Kotlin) | Inline intent interpretation + reply suggestions inside any messaging app | **Zero** — always present when typing |
| **Mobile app** | React Native (latest stable LTS) | Conversational companion + Soul Document management + reflection + Share Sheet host | **Low** — 2 taps via Share Sheet; or open app directly |
| **Web app** | React | Conversational companion (desktop) | **Low** — paste or type directly |
| **Chrome extension** | Chrome MV3 | Real-time overlay on WhatsApp Web | **Zero** — passive overlay on incoming messages |
| **Notification Listener + Bubble** | Android service (Kotlin) | Passive intent prediction on incoming message notifications, shown as floating bubble | **Zero** — fully automatic (Android only) |

### Interaction Surface Priority

| Priority | Surface | Ship phase | Rationale |
|---|---|---|---|
| **P0 — Ship first** | NC Keyboard (iOS + Android) | Alpha | Highest impact. Turns NC from "a separate app" into "embedded in every conversation." Works across all messaging apps. This is the mobile overlay equivalent. |
| **P0 — Ship first** | Chrome extension overlay | Alpha | Already designed. Desktop real-time overlay on WhatsApp Web. |
| **P1 — Ship with keyboard** | Share Sheet extension (iOS + Android) | Alpha | Trivial to build alongside the mobile app. Fallback for users who don't want a custom keyboard. |
| **P1 — Ship with keyboard** | Mobile app (companion + Soul Doc management) | Alpha | Core Soul Document CRUD, reflection journal, and conversational companion mode. |
| **P2 — Ship at beta** | Web app (companion) | Beta | Desktop companion for deliberate reflection. Lower priority than keyboard + extension. |
| **P3 — Android beta** | Notification Listener + Floating Bubble | Beta | True passive mobile overlay — but Android only, and requires careful Play Store policy navigation. Build after keyboard is stable. |

**Surface fragmentation risk & mitigation:** Five surfaces across four tech stacks (Swift, Kotlin, React Native, Chrome MV3) is significant engineering overhead for alpha. Mitigation:
- **Alpha ships 3 surfaces only:** NC Keyboard (iOS + Android), Chrome extension, mobile app (with Share Sheet). Web app and Notification Listener are beta.
- **Shared inference client:** The API client, streaming parser, Soul Document manager, and correction flow are shared TypeScript/Kotlin modules — not rewritten per surface.
- **Keyboard is the bet:** If keyboard UX is excellent, Share Sheet and Notification Listener become nice-to-haves. If keyboard UX fails, the entire mobile strategy needs rethinking. Don't spread thin — get the keyboard right first.

### Platform Constraints — Why Real-Time Overlay Differs by Surface

The "real-time overlay" concept requires NC to (a) read incoming messages from another app and (b) inject a visual interpretation layer. This is only possible where the operating system permits cross-app access:

| Surface | Can NC read messages? | Can NC inject overlay UI? | Constraint |
|---|---|---|---|
| **Chrome extension** | Yes — DOM access on WhatsApp Web | Yes — content script injects overlay | Chrome MV3 allows extensions to read and modify web page content |
| **NC Keyboard (iOS + Android)** | Partial — sees text field content and conversation context visible while keyboard is active | Yes — keyboard tray UI is NC's own surface | Custom keyboards are a standard, approved app category on both platforms. "Full Access" permission required — NC's open-source code + zero-persistence model makes this trustworthy. |
| **Android Notification Listener** | Yes — reads notification content (sender, message preview) | Yes — floating bubble overlay (like Messenger chat heads) | NotificationListenerService is a standard Android API. Play Store scrutinises misuse but allows legitimate use cases. NC's transparent privacy model should pass review. |
| **iOS (native apps)** | No — Apple's app sandboxing is absolute | No — iOS does not allow floating overlays from third-party apps | No technical path to passive overlay on iOS. Share Sheet is the closest alternative. |
| **Standalone web app** | No — same-origin policy prevents cross-tab DOM access | No — separate browser tab | Fundamental browser security constraint. Web app serves companion/reflection only. |

**Key insight:** The NC Keyboard is the **mobile equivalent of the Chrome extension overlay** — it lives inside the messaging app and has access to conversation context while the user is composing a reply. It doesn't require the user to switch apps or copy-paste anything.

### Shared Components

- **Soul Document manager:** Shared logic for YAML parsing, encryption/decryption, and validation. Used by all surfaces (mobile app, web, extension, keyboard).
- **Relationship Context manager:** Per-sender data structure (Soul Doc Architecture Spec v0.3, Section 5b). Shared between all surfaces.
- **Inference client:** Shared API client for communicating with NC inference API. Handles streaming response parsing, error handling, and retry logic. Used by keyboard, companion, extension, and notification listener.
- **Correction flow:** Shared correction submission logic. User flags a wrong prediction → structured correction event → stored client-side + submitted to PII-redacted correction log.
- **Keyboard inference bridge:** Lightweight bridge between the custom keyboard context (visible text, app identifier) and the inference client. Determines which Relationship Context to inject based on the detected sender/conversation.

### Data Bridge

- **QR-code pairing:** Extension ↔ mobile Soul Document sync via QR code. No cloud infrastructure required.
- **Local storage:** Each surface maintains its own encrypted copy. Sync is explicit (user-initiated via QR pairing), not automatic.
- **Sync friction mitigation:** QR pairing is high-friction for non-technical users. Planned improvements:
  - **Alpha:** QR code only (simplest to build, most private).
  - **Beta:** Add **Bluetooth LE pairing** as alternative — phone and laptop pair directly without internet.
  - **Future:** Optional **end-to-end encrypted cloud sync** via user-held key (like Signal's encrypted backup). NC server never holds the decryption key. This is the convenience path for users who want seamless multi-device, with privacy preserved through client-side encryption.
- **Keyboard ↔ App data sharing:** On iOS, the keyboard extension and host app share data via App Groups (shared container). On Android, the keyboard service accesses the app's encrypted storage directly. Soul Document and Relationship Context are available to the keyboard without duplication.

### Offline Behaviour

| Surface | Offline Capability |
|---|---|
| Mobile app | Soul Document CRUD, reflection journal, correction history — all work offline. Conversational companion requires network (inference). |
| Web | Same as mobile. Conversational companion requires network. |
| Extension | Overlay requires network (inference). Extension gracefully degrades to invisible when offline. |
| NC Keyboard | Keyboard functions normally for typing. Intent interpretation requires network (inference). Gracefully degrades to standard keyboard when offline. |
| Notification Listener | Notifications still arrive. Intent interpretation requires network. Bubble does not appear when offline. |

---

## 9. Phase 0 → Phase 1 Bridge

Phase 0 generates the annotation dataset that enables Phase 1:

```
Phase 0 User Corrections
  │
  ├── Overlay: "NC got this wrong" → user selects correct intent
  ├── Companion: user asks follow-up or rephrases → implicit correction
  │
  ▼
PII-Redacted Correction Log (FR48)
  │
  ├── Message pattern (redacted), predicted intent, corrected intent, Soul Document context hash
  │
  ▼
Annotation Dataset
  │
  ├── Target: 5,000+ correction pairs before Phase 1 fine-tuning
  │
  ▼
Phase 1: LoRA fine-tuned model with NC-specific intent prediction
```

**Both products coexist after Phase 1 launches:**
- Conversational companion continues on the same (or updated) model — serves reflection use case
- Overlay uses the fine-tuned model — serves real-time use case with higher accuracy and lower latency targets

---

## 10. Deployment & Operations

### Deployment Pipeline

| Step | Tool | Description |
|---|---|---|
| Model serving | vLLM on RunPod/Modal | Docker container with quantised model weights + vLLM |
| API layer | FastAPI on same container or lightweight proxy | Stateless request handler |
| Mobile app | React Native → App Store + Play Store | Standard mobile CI/CD. Includes Share Sheet extension. |
| NC Keyboard (iOS) | Swift → App Store (bundled with mobile app) | Custom keyboard extension distributed as part of the NC app bundle |
| NC Keyboard (Android) | Kotlin → Play Store (bundled with mobile app) | Custom keyboard / input method service distributed with the NC app |
| Web | React → static hosting (Vercel/Cloudflare Pages) | Standard web deployment |
| Chrome extension | Chrome MV3 → Chrome Web Store | Store submission + review |
| Notification Listener (Android) | Kotlin → Play Store (bundled with mobile app) | Android service, requires NotificationListenerService permission |

### Monitoring

| Metric | How | What NC monitors | What NC does NOT monitor |
|---|---|---|---|
| Uptime | Health check endpoint | Server responding, model loaded | — |
| Latency | Per-request timing | First-token latency, total latency, timeout rate | — |
| Error rate | HTTP status codes | 4xx/5xx rate, inference failures | — |
| Cost | Provider billing API | GPU-hours consumed, queries served | — |
| **User content** | **Not monitored** | — | Message content, Soul Document content, user identity |

### Scaling Triggers

| Threshold | Action |
|---|---|
| Warm instance health check fails | Alert + auto-restart warm instance immediately |
| P95 latency > 3s on keyboard surface | Investigate — keyboard latency is the most critical metric |
| P95 latency > 5s sustained 15 min (all surfaces) | Add GPU instance |
| Concurrent requests > 10 | Add burst GPU instance |
| GPU utilisation < 20% sustained 30 min (burst instances only) | Scale down burst instances. Warm pool **never** scales to zero. |
| Monthly cost > £800 at < 500 users | Investigate query volume anomalies |

---

## 11. Security Considerations

| Threat | Mitigation |
|---|---|
| Man-in-the-middle on inference requests | TLS 1.3 minimum; certificate pinning on extension and keyboard |
| Server compromise exposes user data | Zero-persistence architecture — nothing to steal. Even if an attacker gains server access, there is no stored data. |
| Model extraction via inference API | Rate limiting; API key per user; query pattern monitoring |
| Prompt injection via pasted messages | System prompt hardening; output validation; model-level guardrails (FR59) |
| Soul Document exfiltration from device | AES-256 encryption; biometric/PIN gate; platform keychain for key storage |
| Keyboard "full access" trust concern | NC keyboard's open-source code is auditable. Zero-persistence inference means keystrokes are not stored server-side. Privacy policy explicitly states: keyboard data is used only for real-time inference and immediately discarded. No keystroke logging, no analytics on typed content. |
| Notification Listener misuse perception | Permission requested with clear explanation of purpose. NC only reads notifications from user-selected messaging apps (configurable). Open-source code verifiable. Play Store data safety section documents exact data usage. |
| Keyboard data leakage via OS | iOS: keyboard network access requires "Allow Full Access" — clearly explained during onboarding with link to audit source code. Android: input method permissions are standard. Both platforms: NC keyboard sends data only to NC inference API (no third-party endpoints). |

---

## 12. Open Questions for Phase 0

| Question | Impact | Decision needed by |
|---|---|---|
| RunPod vs. Modal for alpha? | Operational complexity, auto-scaling behaviour | Before alpha deployment |
| 4-bit vs. 8-bit quantisation for 70B? | Quality vs. cost tradeoff. 8-bit is ~2x cost but measurably better on complex reasoning. | Before alpha deployment |
| Should 8B fallback routing be automatic or user-configurable? | UX complexity vs. cost optimisation | Before beta |
| Web app framework: React SPA or Next.js SSR? | SEO (irrelevant for private app), developer velocity, deployment complexity | Before development starts |
| How to handle correction consent for annotation dataset? | GDPR — corrections used for model training need separate consent | Before alpha deployment |
| NC Keyboard: native (Swift/Kotlin) or React Native bridge? | Native gives best performance and deepest OS integration. React Native keyboard extensions are possible but less mature. Native recommended for alpha — keyboard latency and responsiveness are critical to user trust. | Before development starts |
| NC Keyboard: how much conversation context is accessible? | iOS custom keyboards have limited context access (text field only). Android IME has broader access. This affects how much Relationship Context the keyboard can infer without user action. | Before keyboard development |
| Android Notification Listener: which messaging apps to support at launch? | WhatsApp is primary. Slack, Telegram, SMS are candidates. Each app's notification format differs — extraction logic must be app-specific. | Before beta |
| Play Store policy risk for Notification Listener? | Google scrutinises apps requesting NotificationListenerService. NC's legitimate, transparent use case should pass, but rejection risk exists. Mitigation: submit early for policy pre-review. | Before beta |
| Mobile overlay feasibility beyond keyboard? | Android Accessibility Service could enable deeper screen-reading overlay (reading messages in-app, not just in text field). But Google restricts Accessibility API usage to genuine accessibility tools — Play Store rejection risk is high. Not recommended for Phase 0. | Phase 1 evaluation |

---

## 13. Critical Risks & Mitigations Summary

| Risk | Severity | Mitigation | Section |
|---|---|---|---|
| **A. Cold starts (30–120s)** kill keyboard UX | **Critical** | Warm pool strategy: 1 always-on reserved instance (~£150–200/month at alpha). Health ping every 5 min. Never scale to zero. | §3 Infrastructure |
| **B. Prompt bloat** — full Soul Doc + context burns tokens, hits "lost in the middle" | **High** | Client-side semantic retrieval: send only top 3–5 relevant traits. Token budget capped at ~1,500–2,000 tokens in. Keyword matching at alpha, lightweight embedding model at beta. | §3 Context Pruning |
| **C. Surface fragmentation** — 5 surfaces, 4 tech stacks, alpha team | **High** | Alpha ships 3 surfaces only (keyboard + extension + mobile app). Shared inference client across all surfaces. Keyboard is the make-or-break bet — don't spread thin. | §8 Surface Priority |
| **D. Keyboard latency** — 2–5s feels slow mid-conversation | **High** | Hybrid inference: local 1B/3B model for simple intents (< 200ms), cloud 70B for complex. Ships at beta. Alpha uses warm pool + 8B routing to hit < 1.5s first token. | §5 Hybrid Inference |
| **E. Data sync friction** — QR pairing is high-friction for non-technical users | **Medium** | Alpha: QR only. Beta: Bluetooth LE. Future: optional E2E encrypted cloud sync with user-held key. Progressive convenience without sacrificing privacy. | §8 Data Bridge |
| **F. iOS keyboard context limits** — Apple restricts what custom keyboards can see | **Medium** | iOS keyboard sees text field content only (not full conversation). Mitigation: user taps a "context" button in keyboard tray to manually select sender → NC loads that sender's Relationship Context. Android IME has broader access. | §12 Open Questions |
| **G. Play Store rejection** for Notification Listener | **Medium** | Submit for early policy pre-review. NC's transparent, open-source, no-data-retention model is a strong case. Notification Listener is P3 (beta) — not blocking alpha. | §12 Open Questions |

### Architecture Quality Gate

Before alpha launch, the following must be validated:

| Gate | Pass criteria |
|---|---|
| Warm pool latency | P95 first-token < 1.5s on keyboard surface with warm instance |
| Context pruning accuracy | Pruned context (top-5 traits) produces equivalent interpretation quality to full Soul Document on 50-message test set |
| Keyboard UX | 3/5 test users rate keyboard experience as "natural" or better in blind comparison with standard keyboard + manual NC app query |
| Privacy audit | Independent review of open-source serving code confirms zero-retention claim |
| Surface stability | NC Keyboard, Chrome extension, and mobile app all pass 48-hour soak test without crashes |

---

*Full product requirements: prd.md | Soul Document spec: soul-document-architecture-spec-2026-03-16.md*
