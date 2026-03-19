# NC — Builder's Quick Reference

**Companion to:** Product Requirements Document - NC (prd.md)
**Date:** 2026-03-19
**Purpose:** Answer "What am I building this week?" without reading 50+ pages.

---

## What NC Is (One Sentence)

NC is a personal AI companion that helps you understand what people actually mean in their messages — through both a conversational interface (paste and ask) and a real-time overlay on incoming messages.

---

## What We're Shipping (Phase 0)

| Surface | What It Does | Tech |
|---|---|---|
| **Mobile App** | Conversational companion (paste message → interpretation + reply suggestions) + Soul Document management + daily reflection | React Native, AES-256 encrypted local storage |
| **Web App** | Same conversational companion for desktop | React |
| **Chrome Extension** | Real-time intent prediction overlay on WhatsApp Web incoming messages | Chrome MV3, content scripts, service worker |
| **Inference API** | Receives message + Soul Document + Relationship Context, returns streaming interpretation/prediction | Llama 3.1 70B on own infra (RunPod/Modal), vLLM, zero-retention |

---

## Two Core Loops

### Conversational Mode (Mobile + Web)
```
User pastes a message from someone
  → NC receives message + Soul Document + Relationship Context for sender
  → Llama 3.1 70B inference (streaming, first token < 2s)
  → Returns: intent interpretation, contextual explanation, reply suggestions
  → User reads, reflects, decides how to respond
```

### Overlay Mode (Extension)
```
Message arrives on WhatsApp Web
  → Content script detects DOM mutation, extracts text + sender ID
  → Service worker retrieves Soul Document from chrome.storage.local
  → POST to NC inference API (streaming)
  → Intent label + confidence + contextual note stream into overlay
  → User reads prediction → modifies (or doesn't modify) their reply
```

**Both modes use the same model, same Soul Document, same Relationship Context.** User corrections in either mode feed the annotation dataset for Phase 1.

---

## 8 Intent Categories

The model classifies into 8 categories. These are not arbitrary — they map to the highest-frequency sources of the intent gap in intimate communication. The label space was validated in the annotation study.

---

## Key Numbers

| What | Phase 0 Target |
|---|---|
| Conversational response (P95) | First token < 2s, full response < 5s |
| Overlay response (P95, streaming) | First token < 2s |
| Intent accuracy (no Soul Doc) | >= 75% |
| Intent accuracy (with Soul Doc) | >= 85% (Phase 1 target after fine-tuning) |
| High-ambiguity flag threshold | Max confidence <= 55% |
| Low-confidence suppression | Max confidence < 40% → no overlay / no prediction shown |
| Overlay suppression (rapid-fire) | >= 5 messages in 60s → suppress after 3rd |
| Emotional dependency threshold | > 10 consultations/day for 7 days → self-check prompt |
| Soul Document encryption | AES-256, keychain-gated |
| Data deletion | <= 3 taps, < 10 seconds, confirmed with timestamp |
| Infra cost (alpha, 50 users) | ~£25–40/month |
| Infra cost (beta, 500 users) | ~£300–500/month |

---

## What's In / Out for Phase 0

### In (Must Ship)

**Conversational Companion:**
- Paste message → interpretation + reply suggestions
- Relationship Context per-sender injection
- Abuse disclosure safeguarding (FR57)
- Emotional dependency detection (FR58)
- Manipulation request refusal (FR59)
- Cooling-off prompt for repeated emotional queries (FR60)

**Real-Time Overlay:**
- WhatsApp Web real-time interception
- Intent prediction overlay (non-intrusive, dismissible, streaming)
- 8-category intent + confidence display
- High-ambiguity flag
- "NC got this wrong" correction flow
- I8 safeguarding signpost (client-side only)
- Rapid-fire message suppression
- Cooling-off mode (per-conversation)
- Over-reliance self-check prompt

**Shared:**
- Soul Document v1 guided intake (conversational, 3 questions, <= 10 min)
- Soul Document summary view + edit
- AES-256 encrypted local storage (Keychain/Keystore)
- Biometric/PIN gate on Soul Document
- Full data deletion (all surfaces)
- Daily reflection prompt (local notification)
- QR-code device pairing (extension <-> mobile)
- Shareable institutional referral card
- PII-redacted correction logs
- GDPR consent gate (separate from ToS)
- Per-session Soul Document transmission consent
- Soul Document declined/empty fallback (message-only mode)

**Infrastructure:**
- Llama 3.1 70B quantised on own GPU (RunPod/Modal)
- Llama 3.1 8B as fast fallback
- vLLM serving, open-source code
- Zero server-side data persistence

### Out (Do Not Build in Phase 0)

- Gmail, Slack, iMessage Web interception (Phase 1 / Growth)
- Firefox / Safari extensions (Growth)
- Mobile real-time message interception (Growth)
- Admin UI / report queue dashboard (Growth)
- Cloud sync / multi-device Soul Document (Growth)
- Soul Document v2 layers 4-6 (Growth)
- Fine-tuned intent model (Phase 1)
- Partner consent network (Vision)
- Clinician dashboard (Growth)
- Voice channel support (Vision)
- Cross-language support (Growth)

---

## Hard Gates (Cannot Launch Phase 0 Without These)

1. Llama 3.1 70B serving: stable on own infra with < 5s P95 response time
2. Soul Document + Relationship Context injection producing coherent interpretations
3. WCAG 2.1 AA audit pass on all surfaces
4. IRB approval for RCT (no study recruitment before this)
5. GDPR consent flow + data deletion verified (legal sign-off)
6. EU AI Act legal opinion received
7. I8 safeguarding signpost reviewed by domestic abuse specialist
8. Conversational safeguarding guardrails (FR57–60) tested and validated
9. Chrome Web Store pre-review submitted and accepted
10. App Store + Play Store legal review + submission accepted
11. Open-source serving code published and auditable

---

## Team

| Role | Scope | FTE |
|---|---|---|
| ML / AI engineer | Llama 3.1 serving, Soul Document + Relationship Context injection, prompt engineering, inference API | 1 |
| Full-stack / Extension engineer | Chrome MV3 extension, overlay UI, web app conversational interface | 1 |
| React Native engineer | Mobile app (conversational companion, Soul Document intake, reflection layer) | 1 |
| Product / Researcher (founder) | Soul Document design, annotation pipeline, RCT protocol, safeguarding review | 1 |
| Legal / compliance | GDPR, EU AI Act review, store submission copy | 0.25 (retained) |

---

## Privacy Rules (Non-Negotiable)

- Soul Document: local-first, encrypted, keychain-gated, fully deletable
- Message content: processed transiently, never stored server-side
- No Soul Document transmitted without per-session user consent
- Partner access to Soul Document: architecturally prohibited
- I8 safeguarding signpost + conversational safeguarding: client-side only, never logged to servers
- **Own infrastructure:** NC runs its own inference servers — no third-party LLM provider touching user data
- **Open-source serving code:** Users can audit — verifiable privacy, not just contractual
- Zero server-side persistence: nothing to steal, nothing to subpoena

---

## When Something Fails

| Failure | System Behaviour |
|---|---|
| Inference API timeout | Overlay suppressed. Companion shows "NC is thinking..." then graceful error after 10s. User reads messages normally. |
| GPU instance unavailable | Request queued; if > 5s queue wait, show fallback message. Serverless auto-scales. |
| Service worker inactive (extension) | Content script retries (max 2, exponential backoff). Then silent degradation. |
| Soul Document not created | Message-only predictions at baseline accuracy. Weekly soft prompt (max 4). |
| Soul Document consent declined (this session) | Lightweight predictions only. No degradation messaging. |
| Confidence < 40% | Overlay suppressed entirely. Companion adds uncertainty caveat. |
| Rapid-fire messages (>= 5 in 60s) | Overlay suppressed after 3rd. "NC is here when you're ready to pause." |
| Emotional dependency pattern detected | Self-check prompt surfaced (FR58). Does not block use. |
| Manipulation request detected | NC declines and explains (FR59). |
| Network offline (mobile) | All Soul Document operations work normally (offline-first). Companion unavailable. |

---

*Full details: prd.md | Phase 0 architecture: phase-0-technical-architecture.md | Soul Document spec: soul-document-architecture-spec-2026-03-16.md*
