# Phase 0 Technical Architecture — NC

**Author:** Snnair
**Date:** 2026-03-19
**Version:** 0.1
**Companion to:** PRD (prd.md), Soul Document Architecture Spec (soul-document-architecture-spec-2026-03-16.md)

---

## 1. Overview

Phase 0 is NC's first deployable product — a **privacy-first personal AI companion** that ships two interaction modes from Day 1:

1. **Conversational companion** (mobile + web): User pastes a message, asks NC for interpretation, contextual explanation, and reply suggestions. Streaming responses.
2. **Real-time overlay** (Chrome extension): Intent prediction on incoming WhatsApp Web messages, displayed as a non-intrusive overlay before the user replies.

Both modes are powered by the same inference pipeline: Soul Document + Relationship Context injected into Llama 3.1 70B at inference time, served on NC's own GPU infrastructure.

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
Client (Mobile / Web / Extension)
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
| **Compute** | Serverless GPU (RunPod / Modal) | Pay-per-use; no idle cost at alpha scale. Scale to zero when no requests. Scale up automatically under load. |
| **Serving engine** | vLLM | Open-source, high-throughput, KV cache optimisation. Supports streaming, quantised models, and continuous batching. |
| **API layer** | Lightweight Python API (FastAPI) | Stateless request handler. Receives request, forwards to vLLM, streams response, discards all data. |
| **Persistence** | None on server | Zero server-side storage. No database, no logs containing user data, no message content retention. |
| **Code** | Open-source serving code | Published on GitHub. Users can audit: no data retention, no telemetry on message content, no side-channel exfiltration. |

**Recommendation:** Start with RunPod for alpha (simpler setup, GPU availability). Evaluate Modal for beta if auto-scaling behaviour is better. Both support vLLM containers.

### Stateless Design

Every inference request is **self-contained**:
- Client sends: message text + Soul Document excerpt + Relationship Context for the sender + system prompt
- Server processes: inference only — no state lookup, no session tracking, no user identification
- Server returns: streaming response (interpretation, confidence, reply suggestions)
- Server discards: everything — no logs, no cache, no residual data

This means:
- Server restart loses nothing (there was nothing to lose)
- No user data exists on any NC server at any time except during the ~2–5 seconds of active inference
- Horizontal scaling is trivial — any server instance can handle any request

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

| Stage | Users | Queries/user/day | Monthly queries | Monthly cost |
|---|---|---|---|---|
| **Alpha** | 50 | 5 | 7,500 | **£25–40** |
| **Beta** | 500 | 8 | 120,000 | **£300–500** |
| **Growth** (1,000 users) | 1,000 | 10 | 300,000 | **£800–1,200** |

**Recommendation:** At alpha scale (£25–40/month), infrastructure cost is negligible. The cost inflection point is ~2,000 active users at ~10 queries/day, where monthly cost reaches £1,500–2,000. This is the point where freemium conversion revenue must begin covering infrastructure.

---

## 5. Latency

| Mode | Target | Rationale |
|---|---|---|
| **Conversational companion** | First token: **< 2 seconds**. Full response: **< 5 seconds** at P95 | User-initiated, not real-time. Users expect "thinking" time when asking a question. Streaming makes 2–5s feel responsive. |
| **Real-time overlay** | First token: **< 2 seconds**. Streaming overlay render as tokens arrive | Relaxed from original 800ms target. 70B model on serverless GPU cannot hit 800ms. Users see streaming prediction appearing progressively — perceived latency is first-token, not total. |
| **Fallback (8B)** | First token: **< 500ms**. Full response: **< 2 seconds** | For simpler queries routed to the 8B model. |

**Phase 0 vs. Phase 1 latency:**

The original PRD specifies < 800ms end-to-end for the overlay. This target was designed for a fine-tuned model with optimised inference (Phase 1). Phase 0's Llama 3.1 70B on serverless GPU will not hit 800ms — streaming mitigates the perceived latency. Phase 1 re-targets < 800ms with a fine-tuned, smaller model.

**Recommendation:** Accept 2–5s streaming for Phase 0. The conversational companion is user-initiated (latency tolerance is higher). The overlay uses streaming render — first intent label appears quickly, confidence and contextual note fill in progressively. Track P95 latency to ensure Phase 0 is usable, but do not gate launch on 800ms.

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

| Surface | Technology | Primary Function |
|---|---|---|
| **Mobile app** | React Native (latest stable LTS) | Conversational companion + Soul Document management + reflection |
| **Web app** | React | Conversational companion (desktop) |
| **Chrome extension** | Chrome MV3 | Real-time overlay on WhatsApp Web |

### Shared Components

- **Soul Document manager:** Shared logic for YAML parsing, encryption/decryption, and validation. Used by mobile, web, and extension.
- **Relationship Context manager:** Per-sender data structure (Soul Doc Architecture Spec v0.3, Section 5b). Shared between all surfaces.
- **Inference client:** Shared API client for communicating with NC inference API. Handles streaming response parsing, error handling, and retry logic.
- **Correction flow:** Shared correction submission logic. User flags a wrong prediction → structured correction event → stored client-side + submitted to PII-redacted correction log.

### Data Bridge

- **QR-code pairing:** Extension ↔ mobile Soul Document sync via QR code. No cloud infrastructure required.
- **Local storage:** Each surface maintains its own encrypted copy. Sync is explicit (user-initiated via QR pairing), not automatic.

### Offline Behaviour

| Surface | Offline Capability |
|---|---|
| Mobile | Soul Document CRUD, reflection journal, correction history — all work offline. Conversational companion requires network (inference). |
| Web | Same as mobile. Conversational companion requires network. |
| Extension | Overlay requires network (inference). Extension gracefully degrades to invisible when offline. |

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
| Mobile | React Native → App Store + Play Store | Standard mobile CI/CD |
| Web | React → static hosting (Vercel/Cloudflare Pages) | Standard web deployment |
| Extension | Chrome MV3 → Chrome Web Store | Store submission + review |

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
| P95 latency > 5s sustained 15 min | Add GPU instance |
| Concurrent requests > 10 | Add GPU instance |
| GPU utilisation < 20% sustained 30 min | Scale down (serverless handles automatically) |
| Monthly cost > £500 at < 500 users | Investigate query volume anomalies |

---

## 11. Security Considerations

| Threat | Mitigation |
|---|---|
| Man-in-the-middle on inference requests | TLS 1.3 minimum; certificate pinning on extension |
| Server compromise exposes user data | Zero-persistence architecture — nothing to steal. Even if an attacker gains server access, there is no stored data. |
| Model extraction via inference API | Rate limiting; API key per user; query pattern monitoring |
| Prompt injection via pasted messages | System prompt hardening; output validation; model-level guardrails (FR59) |
| Soul Document exfiltration from device | AES-256 encryption; biometric/PIN gate; platform keychain for key storage |

---

## 12. Open Questions for Phase 0

| Question | Impact | Decision needed by |
|---|---|---|
| RunPod vs. Modal for alpha? | Operational complexity, auto-scaling behaviour | Before alpha deployment |
| 4-bit vs. 8-bit quantisation for 70B? | Quality vs. cost tradeoff. 8-bit is ~2x cost but measurably better on complex reasoning. | Before alpha deployment |
| Should 8B fallback routing be automatic or user-configurable? | UX complexity vs. cost optimisation | Before beta |
| Web app framework: React SPA or Next.js SSR? | SEO (irrelevant for private app), developer velocity, deployment complexity | Before development starts |
| How to handle correction consent for annotation dataset? | GDPR — corrections used for model training need separate consent | Before alpha deployment |

---

*Full product requirements: prd.md | Soul Document spec: soul-document-architecture-spec-2026-03-16.md*
