---
stepsCompleted: [step-01-init, step-01b-continue, step-02-discovery, step-02b-vision, step-02c-executive-summary, step-03-success, step-04-journeys, step-05-domain, step-06-innovation, step-07-project-type, step-08-scoping, step-09-functional, step-10-nonfunctional, step-11-polish]
classification:
  projectType: multi-surface (conversational-app + browser-extension + mobile-app)
  domain: neuroai-scientific-consumer
  complexity: high
  projectContext: greenfield
inputDocuments:
  - _bmad-output/planning-artifacts/product-brief-NC-2026-03-14.md
  - _bmad-output/planning-artifacts/soul-document-architecture-spec-2026-03-16.md
  - _bmad-output/planning-artifacts/research/technical-neuroai-cognitive-companion-research-2026-03-13.md
  - _bmad-output/planning-artifacts/research/domain-neuroplasticity-trust-research-2026-03-16.md
  - _bmad-output/planning-artifacts/research/domain-reflection-journal-consciousness-research-2026-03-16.md
  - _bmad-output/brainstorming/brainstorming-session-2026-03-13-1500.md
  - _bmad-output/brainstorming/brainstorming-session-2026-03-16-1600.md
  - _bmad-output/planning-artifacts/encode-application/encode-application-NC-2026-03-17-v2.3.md
  - _bmad-output/planning-artifacts/implementation-readiness-report-2026-03-18.md
workflowType: 'prd'
prdScope: 'product-development-track'
briefCount: 1
researchCount: 3
brainstormingCount: 2
projectDocsCount: 0
---

# Product Requirements Document - NC

**Author:** Snnair
**Date:** 2026-03-16

---

## Executive Summary

Human relationships are breaking at the speed of biology — not at the speed of intention. A 40–80 millisecond amygdala threat-tagging gap causes the brain to classify the *tone* of an incoming message as a threat signal before the prefrontal cortex can process *communicative intent*. This is not a social media problem; it is a neuroscience problem. Social media spent 15 years amplifying that gap — training billions of people to scan for threat compulsively, at scale. The damage lands across every relationship that matters: couples, co-parents, colleagues, and friends.

**NC (NeuroAI Cognitive Companion)** is the counter-intervention. It is a multi-surface AI companion — browser extension and mobile app — that predicts what a person *actually means* and presents it to the receiver *before* the amygdala response can embed a false interpretation. NC is grounded in the neuroscience of mentalising (temporoparietal junction) and threat response (amygdala), deployed across digital text channels where ambiguity does its greatest relational damage.

**Target users:** Individuals experiencing relational friction in text-based digital communication — adults in intimate relationships, co-parenting arrangements, high-stakes professional relationships, and deep friendships — who are motivated to reduce misreading and restore signal fidelity in their most important conversations. **Neurodivergent users** (ADHD, ASD) are a named secondary segment: their intent-expression gap is wider than the neurotypical baseline and NC's person-aware model is particularly well-suited to bridging it. ND users are expected to be early adopters disproportionately represented in the initial cohort.

**The problem NC solves:** The intent gap — the systematic delta between what a sender means and what a receiver interprets — is invisible, pervasive, and cumulative. Each misread builds on the last. NC makes the gap visible and intervenes at the point of reception, before the narrative solidifies.

### What Makes This Special

NC is not a communication coach, a sentiment analyser, or a conflict-resolution chatbot. It is a **foundation model of communicative intent** — the first product to combine three capabilities simultaneously:

1. **Person-aware intent modelling via the Soul Document.** NC conditions every intent prediction on *who the person actually is* — their ranked values, decision architecture, and narrative history — not just what they wrote. The Soul Document is a portable, structured, model-agnostic personality representation (3-layer YAML schema) injected at inference time. This solves the cold-start problem from Day 1: new users receive accurate intent predictions without months of message history accumulation.

2. **Neuroscience-grounded inference, not pattern matching.** The core architecture models `P(intent | message, relational_history, soul_document, context)` — a probabilistic framework that explicitly separates the TPJ mentalising pathway from the amygdala threat pathway. No competitor has built intent prediction at this level of neurobiological precision.

3. **Personality sovereignty as a design constraint.** The Soul Document is local-first, AES-256 encrypted, not accessible to partners or third parties, and fully deletable. NC's differentiator is not data capture — it is data trust. Users who understand the alternative choose NC specifically because it doesn't monetise their personality.

**Why users will choose NC over alternatives:** Every other tool either analyses communication patterns without personal context (generic) or requires clinical intervention (inaccessible). NC is the only product that operates at consumer scale, in real time, across the channels where the intent gap actually lives — the text thread, the Slack message, the WhatsApp chain — with a personality layer that knows the person behind the words.

**Core insight:** Intent prediction accuracy is not a language problem. It is a person-knowledge problem. The same words, sent by different people in different relational contexts, mean entirely different things. NC is the first product built on this insight at production scale.

### Phased Delivery Strategy

NC ships in two phases, both of which coexist permanently once launched:

**Phase 0 — Personal AI Companion (first to ship).** NC launches with two modes from Day 1: (1) a **conversational companion** where users paste messages and ask NC for interpretation, contextual explanation, and reply suggestions; and (2) a **real-time intent prediction overlay** on incoming messages via Chrome extension. Phase 0 is built on open-source infrastructure — Llama 3.1 70B quantised, served on NC's own GPU infrastructure (RunPod/Modal) with open-source serving code, delivering **architectural privacy** (verifiable, not just contractual). Phase 0 surfaces include mobile app (React Native), web app, and Chrome extension. Revenue model: freemium — Phase 0 free, users pay for enhanced usage.

**Phase 1 — Fine-Tuned Intent Prediction (builds on Phase 0 data).** Phase 0 user corrections generate an annotated dataset of real-world intent interpretations. Phase 1 uses this dataset to fine-tune a dedicated intent prediction model with higher accuracy targets (≥ 85% with Soul Document) and lower latency targets. Phase 1 enhances the overlay; the conversational companion continues alongside it.

**Both modes persist:** The conversational companion serves reflection and deliberate interpretation; the overlay serves real-time reception. Users use both depending on context — overlay for incoming messages in flow, companion for messages they want to think about more carefully.

**The flywheel:** Science → Product → Data → Better Science. Every user interaction is a scientific data point. Every paper strengthens the product's credibility. Every credibility gain brings higher-quality users whose corrections improve the model. NC does not compete on data volume — it competes on data quality and scientific legitimacy. Where social media captured the amygdala, NC trains the prefrontal cortex — using the same neuroplasticity mechanisms, deliberately, for relational repair.

## Project Classification

- **Project Type:** Multi-surface — conversational companion (mobile + web) + browser extension (real-time overlay) + mobile app (Soul Document management, reflection layer)
- **Domain:** NeuroAI / Scientific Consumer — grounded in peer-reviewed neuroscience (amygdala threat response, TPJ mentalising, neuroplasticity), designed for everyday consumer deployment without clinical mediation
- **Complexity:** High — novel AI architecture (Soul Document + intent prediction model), dual-surface delivery, IRB-required research study embedded in Year 1, regulatory sensitivity around personal/relational data, and a scientific validity bar that most consumer products do not carry
- **Project Context:** Greenfield — no existing codebase, no legacy architecture, no inherited technical debt; all infrastructure, data pipelines, ML systems, and product surfaces built from first principles

---

## Success Criteria

> **Note on dual-track success:** NC operates across two parallel tracks — a commercial product track and an embedded research track. This section defines **commercial product success only**. Research success (H1/H2/H3 experimental outcomes, annotation reliability, Brain-Score validation) is governed by the Soul Document Architecture Specification and the Experimental Plan in the product brief. These tracks are complementary but independently evaluated.

---

### User Success

NC succeeds for a user when it intervenes in the intent gap *before* a false interpretation becomes a relational narrative.

**The success moment:** A user reads an ambiguous message, sees NC's intent prediction, and modifies their response — editing, delaying, or discarding a reply that would have compounded misunderstanding. This is the primary behavioural signal of NC working. It does not require the user to report anything; it is measurable in-product.

**The felt experience of success:**
- *"I almost replied defensively — NC showed me he was actually nervous, not attacking."* (de-escalation before the reactive message sends)
- *"I didn't have to decode what she meant. NC told me, and she confirmed I got it right."* (accuracy + validation loop)
- *"We haven't had that kind of spiral in three weeks."* (downstream relational outcome — word-of-mouth signal, not primary metric)

**User success is NOT:**
- A user reading NC's prediction and ignoring it
- A user using NC on low-stakes, unambiguous messages
- A user who churns after the novelty wears off without behaviour change

**Measurable user success criteria:**

| Metric | MVP Bar | Growth Bar |
|--------|---------|------------|
| Reply modification rate (edit, delay, or discard after intent prediction surfaced) | ≥ 20% of intent-prediction exposures | ≥ 35% |
| Week-8 retention (user still active at 8 weeks — the neuroplasticity window) | ≥ 50% | ≥ 60% |
| Soul Document completion rate (users who complete intake and activate) | ≥ 70% of signups | ≥ 80% |
| User-reported accuracy ("NC got what they meant right") — in-app prompt, 5-point scale | ≥ 3.5 / 5.0 | ≥ 4.0 / 5.0 |

---

### Phase 0 Success Milestones

| Metric | Alpha (Month 3) | Beta (Month 6) |
|--------|-----------------|----------------|
| Active users (conversational + overlay combined) | 50 | 500 |
| Soul Document completion rate | ≥ 70% of signups | ≥ 75% |
| Conversational mode sessions per active user per week | ≥ 3 | ≥ 5 |
| Overlay adoption rate (among Phase 0 users) | ≥ 40% install extension | ≥ 50% |
| User corrections submitted (annotation dataset) | 500 total | 5,000 total |
| Phase 0 → Phase 1 readiness | — | Annotation dataset sufficient for LoRA fine-tuning |

**Recommendation:** Track conversational mode and overlay mode engagement separately — they serve different use cases (reflection vs. real-time) and will have different retention curves. The annotation dataset size from user corrections is the key Phase 0 → Phase 1 gate.

---

### Business Success

**12-month commercial success (end of fellowship year):**

NC has commercial legs if — independent of the research study — a cohort of real users is staying, engaging, and telling others. The following three signals together constitute a go/no-go signal for commercial investment:

| Signal | Target | Why It Matters |
|--------|--------|----------------|
| Active non-study users (all surfaces) | 300–500 by Month 12 | Proves demand outside research recruitment |
| Week-8 retention | ≥ 60% | Proves the neuroplasticity use-case — users come back because it's changing something |
| Institutional letter of intent | ≥ 1 (couples therapist / HR platform / mediation service) | Proves professional market sees clinical/institutional value |

**Revenue model:** Freemium. Phase 0 is free — users pay for usage beyond a free tier (premium features, higher query limits). Phase 1+ introduces paid subscription for enhanced overlay capabilities.

**What business success is NOT at 12 months:**
- 10,000 downloads with 10% retention
- Viral growth (NC is intimate-use product; growth is trust-gated, not share-able)

**18–24 month commercial horizon (post-fellowship):**

| Metric | Target |
|--------|--------|
| Paid subscriber conversion | ≥ 15% of active free users |
| Monthly recurring revenue | £10K MRR as seed-round signal |
| Platform partnerships (therapy, HR, co-parenting apps) | 2–3 signed integrations |
| Waitlist for mobile app (iOS) | 2,000+ at launch |

---

### Technical Success

**Intent prediction accuracy — the core technical bar:**

NC must be *right often enough to be trusted*. Below the MVP floor, users experience NC as noise — it creates doubt without confidence and churns within days. Above the growth target, NC earns habitual use.

| Threshold | Accuracy | Condition |
|-----------|----------|-----------|
| MVP floor | **≥ 75%** on ambiguous-valence messages | Message + relational history, no Soul Document |
| Growth target | **≥ 85%** | Message + relational history + Soul Document active |
| Vision ceiling | **≥ 90%** | 90+ days of relational history + full Soul Document |

**Rationale for 75% floor:** Unaided human interpretation of emotionally ambiguous digital text is accurate approximately 50–60% of the time (informed by intent-gap annotation study baseline). NC at 75% is meaningfully better than unaided reading — sufficient for users to trust it. NC below 75% is not better enough to change behaviour.

**Latency — the neuroscience constraint:**

NC must surface the intent prediction *before* the amygdala response embeds a false interpretation. The relevant biological window is 40–800ms from stimulus receipt to cortical processing completion. For a browser extension intercepting an incoming message:

| Target | Threshold |
|--------|-----------|
| Intent prediction surface time | **< 800ms** from message receipt to UI display |
| Soul Document injection overhead | **< 200ms** additional (included in 800ms total) |
| Extension load time | **< 1s** on cold start |

**Privacy and security — hard constraints (not aspirational):**

These are not technical stretch goals. They are product-defining constraints. Failure on any of these is product failure:

- Soul Document: local-first storage, AES-256 encryption at rest, device keychain gating
- No Soul Document content transmitted to server without explicit per-session user consent
- Full data deletion executable by user in ≤ 3 taps, with confirmation of deletion
- Partner access to another user's Soul Document: **architecturally prohibited in v1**
- GDPR Article 25 (privacy by design) compliance from Day 1 — not retrofitted

**Cross-surface reliability (Phase 0):**

| Surface | Function |
|---------|----------|
| Browser extension | WhatsApp Web real-time overlay (Phase 0); Gmail, Slack, iMessage web (Growth) |
| Mobile app | Conversational companion + Soul Document management + async reflection |
| Web app | Conversational companion (desktop) |

---

### Measurable Outcomes Summary

| Category | Metric | MVP Target | Growth Target |
|----------|--------|------------|---------------|
| User | Reply modification rate | 20% | 35% |
| User | W8 retention | 50% | 60% |
| User | Soul Document activation | 70% | 80% |
| User | User-reported accuracy | 3.5 / 5.0 | 4.0 / 5.0 |
| Business | Active non-study users (Month 12) | 300 | 500 |
| Business | Institutional LOI | 1 | 3 |
| Technical | Intent accuracy (no Soul Doc) | 75% | — |
| Technical | Intent accuracy (Soul Doc active) | — | 85% |
| Technical | End-to-end latency | < 800ms | < 500ms |
| Technical | Privacy constraints | All met | All met |

---

### Instrumentation Plan

Every metric in the Measurable Outcomes Summary requires specific telemetry events to be computable. This section defines the events, their capture points, and the privacy constraints on each.

**User Metrics Instrumentation:**

| Metric | Event Name | Trigger | Data Captured | Privacy Constraint |
|---|---|---|---|---|
| Reply modification rate | `reply_modified` | User edits, delays (≥ 10s after overlay display), or discards a draft after intent prediction was rendered | Overlay session ID, modification type (edit/delay/discard), time-to-action (ms) | No message content. No draft content. Session ID is ephemeral, not linked to user identity on server |
| Reply modification rate (denominator) | `overlay_rendered` | Intent prediction overlay is displayed to user | Overlay session ID, channel (WhatsApp/Gmail/Slack/iMessage), confidence score, ambiguity flag | No message content. No sender identity transmitted |
| W8 retention | `session_active` | User has at least one `overlay_rendered` event in a calendar day | User pseudonym ID, date | Pseudonym ID generated client-side; not reversible to user identity without client-side key |
| Soul Document completion | `soul_doc_activated` | User taps "Activate" after reviewing Soul Document summary | User pseudonym ID, intake surface (mobile/extension), intake duration (seconds) | No Soul Document content transmitted in this event |
| Soul Document completion (denominator) | `signup_completed` | User completes GDPR consent gate | User pseudonym ID, signup surface | — |
| User-reported accuracy | `accuracy_rating_submitted` | User responds to in-app accuracy prompt | Rating (1–5), overlay session ID, channel | No message content. Prompt shown after every 10th overlay; frequency configurable |

**Business Metrics Instrumentation:**

| Metric | Measurement Method | Source |
|---|---|---|
| Active non-study users | Count of distinct pseudonym IDs with ≥ 1 `session_active` event in trailing 7 days, excluding IDs flagged as study participants | Server-side aggregation on pseudonymised event stream |
| Institutional LOI | Manual tracking — signed document count | CRM / founder records |

**Technical Metrics Instrumentation:**

| Metric | Event Name | Trigger | Data Captured |
|---|---|---|---|
| Intent accuracy | `prediction_accuracy_check` | Offline evaluation against held-out annotated test set | Prediction vs. ground truth on test set; not from production traffic |
| End-to-end latency | `inference_latency` | Every inference request completes (success or timeout) | Total latency (ms), lightweight-phase latency (ms), enrichment-phase latency (ms), timeout flag |
| Privacy constraints | Automated audit | CI pipeline and pre-launch security review | Pass/fail per constraint; logged in compliance register |

**Instrumentation Principles:**
- All telemetry events are opt-in via GDPR consent gate (FR32). Users who consent to product analytics receive telemetry; users who decline receive NC with no telemetry — product functions identically
- No message content, draft content, sender identity, or Soul Document content appears in any telemetry event
- Pseudonym IDs are generated client-side using a one-way hash; server cannot reverse to user identity
- All events transmitted over the same HTTPS/TLS 1.3 channel as inference payloads (NFR-S3)
- Telemetry retention: 12 months rolling, then aggregated and individual events purged

**Decision Thresholds:**

| Signal | Threshold | Decision |
|---|---|---|
| Reply modification rate < 10% at Week 4 | Below floor | Investigate overlay UX — prediction may be accurate but not actionable |
| W8 retention < 40% | Below floor | Investigate churn drivers; survey churned users on trust/accuracy |
| Soul Document completion < 50% | Below floor | Simplify intake or extend inline fallback capability |
| User-reported accuracy < 3.0 / 5.0 | Below floor | Model quality gate — halt user acquisition until accuracy improves |
| Reply modification rate ≥ 20% AND W8 retention ≥ 50% AND accuracy ≥ 3.5 | MVP bar met | Proceed to general availability; begin Growth feature development |

---

## Product Scope

### Phase 0 — Personal AI Companion (First Ship)

*What must work for NC to be useful at all.*

Phase 0 is the first deployable version of NC. It ships two interaction modes from Day 1 — a **conversational companion** and a **real-time overlay** — both powered by Llama 3.1 70B on NC's own GPU infrastructure with architectural (verifiable) privacy.

**Phase 0 includes:**

- **Conversational companion (mobile + web):** User pastes a message from someone, asks NC for interpretation, contextual explanation grounded in Soul Document + Relationship Context, and reply suggestions. Streaming responses, 2–5 second target latency.
- **Browser extension (Chrome MV3) — real-time overlay:** Intent prediction on incoming messages on WhatsApp Web (primary channel). Displays intent prediction as a non-intrusive overlay before the user replies. Same Llama 3.1 70B model; streaming overlay render.
- **Soul Document v1 intake:** Guided 3-question self-report (≤ 10 minutes). NC extracts and structures 3-layer YAML automatically. User reviews and activates before first use.
- **Relationship Context injection:** Per-person data structure (schema defined in Soul Document Architecture Spec v0.3, Section 5b) — communication patterns, correction history, and contextual notes per sender, injected alongside Soul Document at inference time.
- **Intent gap visualiser:** Shows the predicted intent distribution (8-category label space) with confidence levels. High-entropy predictions display "high ambiguity" flag — no false confidence.
- **Reply modification UX:** Passive instrumentation of reply editing behaviour. No prompts or nudges — the prediction itself is the intervention.
- **Local-first data model:** Soul Document stored on-device, AES-256 encrypted, no cloud sync.
- **Full data deletion:** User can delete all NC data in ≤ 3 taps.
- **Mobile app (iOS + Android):** Conversational companion + Soul Document management, intake, and async reflection prompts. Built in React Native. Android minimum supported version: API 26 (Android 8.0). Soul Document encrypted at rest using Android Keystore (Android) and iOS Keychain (iOS); biometric/PIN gate on both platforms.
- **Web app:** Conversational companion interface for desktop users who prefer not to install the extension, or for deeper reflection sessions.
- **Infrastructure:** Llama 3.1 70B quantised on own GPU infrastructure (RunPod/Modal). Llama 3.1 8B as fast fallback. Open-source serving code for verifiable privacy. Stateless inference, zero persistence.
- **Revenue:** Freemium — Phase 0 free, users pay for usage beyond free tier.

**Phase 0 explicitly excludes:**

- Multi-user / partner consent networking (Vision)
- Voice channel support
- Real-time message interception on mobile (iOS or Android) — Growth feature for both platforms
- Fine-tuned model (Phase 1 — requires annotation dataset from Phase 0 corrections)
- Gmail, Slack, iMessage Web interception (Growth — WhatsApp Web only in Phase 0)

---

### Phase 1 — Fine-Tuned Intent Prediction (Post-Phase 0 Data)

*What makes the overlay substantially more accurate.*

Phase 1 builds on the annotation dataset generated by Phase 0 user corrections. It fine-tunes a dedicated intent prediction model via LoRA, targeting higher accuracy and lower latency than the base Llama 3.1 70B.

**Phase 1 adds:**

- Fine-tuned intent prediction model (LoRA on NC's own annotated dataset)
- Higher accuracy targets: ≥ 85% with Soul Document (up from Phase 0 baseline)
- Lower latency targets for overlay mode
- Extended channel support: Gmail, Slack web, iMessage web
- Both modes (conversational companion + overlay) continue; Phase 1 enhances the overlay model

---

### Growth Features (Post-MVP)

*What makes NC competitive and retentive.*

- **Relational history deepening:** Progressive improvement in intent accuracy as message history accumulates. Accuracy trajectory surfaced to user ("NC knows you better now").
- **Pattern-level insights:** Weekly reflection on recurring intent gap patterns — "This phrasing is consistently misread between you and [X]."
- **Mobile real-time interception (iOS + Android):** Extend intent prediction to native mobile messaging — iOS (iMessage, WhatsApp iOS via share extension) and Android (WhatsApp, SMS via Accessibility Services or notification listener, pending platform policy review). iOS first given permissions complexity; Android to follow. Both require independent platform compliance review before shipping.
- **Soul Document v2:** Layers 4–6 (Narrative History, Relational Maps, Temporal Patterns). Richer cold-start accuracy. Automated story tagging replaces manual RA tagging.
- **Institutional integration API:** Headless NC engine consumable by couples therapy platforms, HR tools, and co-parenting apps.
- **Precision accuracy tooling:** In-app accuracy feedback loop — user can flag wrong predictions. Feeds anonymised improvement signal (with consent).

---

### Vision (Future)

*What NC becomes if the science holds and the product earns trust.*

- **Consent network (Horizon 2):** Two users in a relationship can opt into mutual intent sharing — both see each other's intent predictions with explicit, revocable bilateral consent. Ethics review required; coercive control design constraint governs architecture.
- **Voice channel:** Real-time intent prediction on voice messages and calls. Requires new model architecture (prosodic + semantic fusion).
- **Neuroplasticity programme:** Structured 60-day programme grounded in H3 mechanism — designed to shift users from threat-first to intent-first interpretation as a lasting cognitive change, not just an in-the-moment tool.
- **Clinician dashboard:** Read-only, consent-gated view for therapists and mediators working with NC users — aggregate pattern trends, not message content.
- **Cross-language support:** Intent prediction beyond English, beginning with languages with the highest dyadic digital communication volume (Spanish, Mandarin, Hindi).
- **Foundation model open release:** The NC intent prediction model and annotated dataset released as open-source scientific infrastructure — the "ImageNet for communicative intent."

---

## User Journeys

---

### Journey 1: Core Receiver — Success Path
**Persona: Maya, 34 — Partner in a 6-year relationship**

> *"He's always so short with me when he's stressed. I never know if he's angry at me or just overwhelmed."*

**Opening Scene**

It's 6:43pm on a Wednesday. Maya is finishing a difficult day at work when a message arrives from her partner Daniel: *"Fine. I'll sort it."* Four words. No punctuation relief. No warmth. Maya has seen this pattern before — and she knows exactly what her gut says it means: dismissal. Irritation. She starts typing a response that begins *"You don't have to be like that—"*

She's used NC for three weeks. The extension intercepts the message before she finishes her reply.

**Rising Action**

NC surfaces a prediction overlay on WhatsApp Web: **I3 — Setting a boundary (72% confidence) / I5 — Expressing frustration (21%)** with a note: *"Daniel's messages shorten and tone formalises when he's processing stress — this pattern appears in 8 of the last 12 similar exchanges. He is most likely signalling overwhelm, not displeasure with you."*

Maya stops. She reads it twice. The drafted *"You don't have to be like that"* sits in the text box.

**Climax**

She deletes her draft. She types instead: *"Sounds like a rough one — I'll handle dinner. Come home when you're ready."* She sends it. Daniel replies within two minutes: *"Thank you. Really needed that."*

**Resolution**

The spiral didn't happen. Maya didn't need to suppress anything — she just had better information before she reacted. The conversation that would have run through the evening as a low-grade argument simply didn't start. She doesn't think of it as NC working. She thinks of it as understanding him better.

**Requirements this journey reveals:**
- Real-time message interception on WhatsApp Web
- Intent prediction overlay UI (non-intrusive, dismissible)
- Soul Document stress response layer driving the contextual note
- Confidence display with secondary intent visible
- Reply modification instrumentation (draft deleted = NC influenced)

---

### Journey 2: Core Receiver — Edge Case
**Persona: Priya, 41 — Co-parent, 2 years post-separation**

> *"We're civil. But every message from him feels like a test I might fail."*

**Opening Scene**

Priya receives a message from her ex-husband Ravi about their daughter's school pickup: *"I assume you've already sorted Friday."* NC predicts: **I7 — Giving information (68% confidence)**. Priya reads it and feels immediately that this is wrong. To her, that message has never been neutral — *"I assume"* from Ravi always carries an edge of accusation. She taps the "NC got this wrong" flag.

**Rising Action**

NC registers the correction signal. It surfaces a follow-up prompt: *"Thanks for the correction. How would you describe what this message meant to you?"* Priya selects from a short list: **I5 — Expressing frustration.** NC notes the divergence — her Soul Document doesn't yet have enough relational history with Ravi to calibrate his patterns accurately. It displays: *"High ambiguity — NC has limited history with this sender. Treat this prediction with caution."*

**Climax**

Priya doesn't feel misled — she feels *seen*. NC told her it wasn't sure. It didn't pretend confidence it didn't have. She replies to Ravi factually, without escalation, and makes a mental note to trust her own read for Ravi-messages until NC has more data.

**Resolution**

Three weeks later, after 14 more corrected predictions on Ravi's messages, NC's accuracy on his messages reaches 81%. Priya notices she's been flagging corrections less. The calibration happened quietly, incrementally — and she was part of it.

**Requirements this journey reveals:**
- "NC got this wrong" in-product correction flow
- High-ambiguity / low-confidence display state (not false confidence)
- Per-sender calibration tracking (separate from global Soul Document)
- Accuracy improvement feedback loop (correction → model signal)
- Trust recovery UX — NC acknowledging uncertainty earns more trust than masking it

---

### Journey 3: New User Onboarding
**Persona: James, 29 — First-time user, referred by a friend**

> *"My friend said it changed how he reads his girlfriend's messages. I don't really get what it does yet."*

**Opening Scene**

James installs the Chrome extension on a Sunday afternoon. He's mildly curious, mildly sceptical. The onboarding screen says: *"Before NC can help, it needs to know you — not your messages, just you."* It explains the Soul Document in one sentence: *"A private personality layer, stored on your device, that helps NC understand the person behind the words."*

**Rising Action**

Three questions. Ten minutes.

*"What matters most to you — ranked, not listed?"* James thinks longer than he expected to. He types: directness, then loyalty, then not wasting time. NC reflects them back as structured values and asks him to confirm or edit.

*"When you're stressed or overwhelmed, how do you usually communicate?"* James types: *"I go quiet. I stop texting back as fast. People think I'm angry."* NC extracts: stress response pattern — withdrawal, response latency increase, perceived as disengagement.

*"Tell me about a recent conversation that was harder than it should have been."* James describes a misread with his sister. NC structures a narrative entry into the Soul Document stories layer and flags it as a calibration reference.

**Climax**

James reviews the Soul Document summary NC has assembled. He edits one value ranking. He reads the stress response entry and thinks: *"That's exactly right."* He activates it. NC says: *"Ready. I'll start helping when messages arrive."*

**Resolution**

James's first interception happens three hours later — a message from his flatmate. NC's prediction feels accurate. He doesn't think about the Soul Document again. It's just working.

**Requirements this journey reveals:**
- 3-question guided intake UI (conversational, not form-based)
- NC-automated YAML extraction from natural language responses
- User review + edit before activation (trust gate)
- Soul Document summary view (readable, not raw YAML)
- Activation confirmation state
- Cold-start accuracy from Day 1 (no message history needed)

---

### Journey 4: Institutional Referral
**Persona: Dr. Sarah Chen, 47 — Couples therapist, private practice**

> *"Half of what I do in sessions is help people decode what their partner actually meant. I'm doing it manually, one hour at a time."*

**Opening Scene**

Sarah hears about NC from a colleague at a conference. She's professionally cautious — she's seen apps that claim to help couples and damage them instead. She googles NC and finds the research paper. She reads the H1 validation results. She downloads the Soul Document architecture spec. She spends 40 minutes reading it.

**Rising Action**

What stops her from dismissing it: the privacy architecture. Local-first. No partner access. No data monetisation. She's seen enough coercive control situations to know that a relationship intelligence tool in the wrong hands is a surveillance weapon. NC has explicitly designed against this — she can see it in the spec. That earns her attention.

She clicks "Recommend to a client" — a flow that generates a shareable explainer card: what NC is, what it does, what it doesn't do, who owns the data, and a direct install link. She sends it to one couple she's been working with for six months who consistently misread each other's stress responses.

**Climax**

Four weeks later, the couple reports in session that they've had fewer escalation cycles. One partner says: *"I stopped assuming he was dismissing me. I started asking instead."* Sarah didn't prescribe NC — she introduced it. The couple adopted it themselves.

**Resolution**

Sarah recommends NC to two more clients. She emails the NC team asking about a clinical integration pathway — a read-only aggregate view for therapists, with client consent. She's not a user in the product sense. She's a referral channel and a credibility signal.

**Requirements this journey reveals:**
- Public-facing privacy + research summary (clinician-readable, not marketing copy)
- "Recommend to a client" referral flow with shareable explainer card
- Install link with therapist attribution (for referral tracking)
- Clinician inquiry / partnership contact path
- No requirement for therapist account or dashboard in MVP — that is Growth

---

### Journey 5: NC Ops / Admin
**Persona: Internal NC team member — handling a quality flag**

**Opening Scene**

A user submits a report: NC predicted I1 (Seeking Connection) on a message their partner sent during an argument. The user states the prediction was not just wrong — it felt dismissive of a genuinely threatening message pattern they had been experiencing.

**Rising Action**

The ops team member opens the report queue. The report includes: the message content (redacted to remove PII), the prediction made, the user's correction flag, and a free-text note. The team member reviews the pattern: this is the third report in two weeks where NC has under-predicted I5 (Expressing Frustration) in high-conflict message contexts.

This is not a one-off error — it is a systematic calibration gap in high-conflict relational contexts. The team member tags it as a model quality issue and routes it to the ML team with a priority flag.

**Climax**

The ML team reviews the flagged message cluster. They identify that the training data underrepresents high-conflict dyadic exchanges — the annotation dataset skewed toward moderate-valence messages. They add a targeted fine-tuning batch and flag the affected accuracy bucket in the model changelog.

**Resolution**

The fix ships in the next model update. The user who reported it receives a message: *"Thank you for your correction — it helped us improve NC for situations like yours."* The systematic gap is logged in the product's known-limitations register and added to the pre-launch accuracy disclosure.

**Requirements this journey reveals:**
- Admin report queue with PII-redacted message + prediction log
- Correction pattern aggregation (identify systematic vs. one-off errors)
- Model quality flag + ML team routing workflow
- Model changelog and accuracy bucket tracking
- User-facing acknowledgement of correction contribution
- Known-limitations register (transparency infrastructure)

---

### Journey Requirements Summary

| Journey | Core Capabilities Revealed |
|---|---|
| 1 — Receiver success | Real-time interception, intent overlay UI, Soul Document stress-pattern injection, reply modification instrumentation |
| 2 — Receiver edge case | Correction flow, high-ambiguity display state, per-sender calibration, trust recovery UX |
| 3 — Onboarding | Conversational intake UI, YAML extraction, user review/edit gate, Soul Document summary view, cold-start Day-1 accuracy |
| 4 — Institutional referral | Privacy/research summary, shareable referral card, clinician inquiry path |
| 5 — Ops/admin | Report queue, PII redaction, correction pattern aggregation, model quality routing, accuracy transparency infrastructure |


---

## Domain-Specific Requirements

---

### Compliance & Regulatory

**GDPR — Soul Document as Special Category Data**

The Soul Document encodes an individual's ranked values, decision architecture, stress responses, conflict patterns, and narrative history. This constitutes psychological profiling and maps onto GDPR Article 9 Special Category Data ("data concerning health" and data revealing personal characteristics used to profile natural persons).

Mandatory requirements from Day 1:
- Explicit, informed consent collected before Soul Document creation begins — separate from general terms of service
- Purpose limitation: Soul Document data used solely for intent prediction for the data subject; not used for model training, third-party profiling, or commercial inference without separate explicit consent
- Data minimisation: Soul Document fields limited to those with demonstrated intent prediction contribution (ablation-first principle)
- Right to erasure: Full Soul Document deletion executable by user in ≤ 3 taps; deletion confirmed to user with timestamp; no residual copy retained on NC servers
- Data Processing Agreement (DPA) required for any third-party processor that touches Soul Document data (e.g., LLM inference providers)
- GDPR Article 25 (privacy by design): local-first architecture is the compliance implementation — not a product differentiator bolted on

**Sensitive communications data:**

Message content intercepted by the browser extension is processed transiently and must not be stored, logged, or retained beyond the inference call:
- No message content persisted to NC servers
- No message content included in correction feedback signals without explicit per-instance user consent
- Inference pipeline ephemeral: input → prediction → output → discard

**EU AI Act — Provisional Classification**

NC performs automated inference on personal communications to assess communicative intent, influencing user behaviour in interpersonal relationships. This intersects with EU AI Act provisions on AI systems that make inferences about natural persons' emotional or psychological states in sensitive contexts (Article 6 + Annex III) and transparency obligations for AI systems interacting with natural persons (Article 50).

**Provisional classification: Likely Limited Risk (Article 50 transparency obligations) with potential reclassification to High Risk pending regulatory guidance on emotional inference systems.**

Pre-launch requirements:
- Legal opinion on EU AI Act classification obtained before any public release in EU/UK — **hard gate, not optional**
- If classified as High Risk: technical documentation (Article 11), human oversight measures (Article 14), transparency to users (Article 13), and conformity assessment required
- If classified as Limited Risk: transparency disclosure to users that intent predictions are probabilistic — not definitive
- NC's existing design (confidence display, high-ambiguity flag, correction flow) satisfies Article 50 transparency obligations in the Limited Risk scenario — document this alignment explicitly

**Research Ethics — IRB Scope Boundary**

- Non-study user data cannot be retroactively reclassified as research data without separate IRB amendment and individual consent
- Study participants and commercial users must be in separate data environments — no commingling of correction signals, message patterns, or behavioural telemetry
- IRB approval obtained before any study participant is recruited — **hard gate for the research track**, independent of commercial product launch timeline
- Ethics board review of safeguarding signpost design required before MVP launch

---

### Safeguarding Requirements

**I8 Pattern Detection — Safeguarding Signpost**

NC's intent label space includes I8 (Chronic self-interest): pattern-level detection of sustained disregard for the receiver's perspective across message history. This pattern is associated with coercive communication dynamics.

**Signpost trigger:** Automatic soft signpost when I8 pattern detected across ≥ 7 consecutive messages from a single sender with confidence ≥ 70%.

**Signpost design constraints:**
- Soft, non-alarming copy: "If conversations feel consistently one-sided, support is available." — not diagnostic, not alarmist
- National/regional helpline links included (UK: Refuge, Men's Advice Line; adaptable by locale)
- User can dismiss; signpost does not reappear for 30 days from dismissal
- No logging of which users triggered the signpost — signpost display is client-side only, not reported to NC servers
- Signpost copy reviewed by domestic abuse / coercive control specialist before launch — **hard gate**

**Domestic abuse scenario — architectural prohibitions (v1 and permanent):**
- Partner access to another user's Soul Document by any mechanism — prohibited
- Shared device detection that would expose Soul Document to a co-user — prohibited
- Any feature usable as a surveillance instrument by an abusive partner — prohibited
- These prohibitions must be included in the engineering threat model and reviewed at every major feature addition

---

**Phase 0 Conversational Safeguarding**

The conversational companion introduces new safeguarding requirements beyond the overlay's I8 signpost. In conversational mode, users may disclose abuse, develop emotional dependency on NC, or request help crafting manipulative messages. These scenarios do not exist in the overlay (which is passive and display-only).

- **FR57:** If the user shares content in the conversational companion indicating they are experiencing abuse, coercive control, or domestic violence, NC must surface safeguarding resources (same regional crisis links as the I8 signpost — Refuge, Men's Advice Line, etc.) without logging the disclosure to NC servers. **Recommendation:** Use the same client-side-only detection approach as the I8 signpost — pattern detected locally, resource displayed locally, no server event. This maintains the privacy guarantee that NC never knows who triggered a safeguarding response.
- **FR58:** If NC detects a pattern of the user relying on NC for interpersonal decisions at a rate exceeding **10 consultations per day sustained over 7 consecutive days**, NC must surface a self-check prompt: "NC is a tool to help you understand — not a replacement for your own judgement. Consider whether you're comfortable making this decision on your own." Prompt is dismissible and does not reappear for 7 days after dismissal. **Recommendation:** Track consultation count client-side only (same privacy model as I8). The threshold of 10/day for 7 days is deliberately high — most engaged users will not trigger this. The goal is to catch compulsive reliance, not regular use.
- **FR59:** If the user asks NC to help craft a manipulative, deceptive, or coercive message — including requests to help "make them feel guilty," "get them to do what I want," or similar intent — NC must decline and explain: "NC helps you understand what someone means, not control how they respond. I can help you express what you actually feel instead." The refusal must not log the request to NC servers. **Recommendation:** This is a model-level guardrail (system prompt constraint on Llama 3.1 70B), not a pattern detection rule. It triggers on the intent of the user's request, not a keyword match. False positives (declining a legitimate request) are less harmful than false negatives (helping craft manipulation).
- **FR60:** If the user submits **> 5 emotionally charged messages about the same person in a single session** (detected by emotional intensity and same-sender reference), NC must surface a cooling-off suggestion: "You've been thinking about this conversation a lot. It might help to step away before deciding what to do." Prompt is dismissible and does not block further use. **Recommendation:** Define "session" as a continuous period of activity with no gap > 30 minutes. "Emotionally charged" is assessed by the model at inference time (not keyword matching). This mirrors the rapid-fire suppression logic (FR52) but for the conversational companion.

---

### Technical Constraints

**Browser extension — Chrome MV3 host permissions:**
- Request only minimum host permissions required for supported channels (Gmail, WhatsApp Web, Slack web, iMessage web)
- Plain-language explanation of what is accessed and why, at permission request time
- No speculative permissions for unsupported channels
- Comply with Chrome Web Store single-purpose policy
- Chrome Web Store pre-review submission required before launch — **hard gate**

**Mobile app — platform permissions:**
- iOS: Soul Document encrypted at rest via iOS Keychain; biometric/PIN gate via LocalAuthentication framework
- Android: Soul Document encrypted at rest via Android Keystore; biometric/PIN gate on API 26+ (Android 8.0+); minimum supported version API 26, covering ~95% of active Android devices
- Neither platform: real-time message interception in MVP — Growth feature requiring independent platform compliance review before shipping

**Apple App Store — iOS mental health guidelines (Guideline 1.4.2):**
- App must not claim diagnostic or therapeutic capabilities
- Wellbeing claims must be accurate and not misleading
- Crisis resource (safeguarding signpost) required
- Legal review of App Store submission copy before submission — **hard gate**

**Google Play Store — mental health / wellness app policy:**
- Equivalent requirements to Apple: no diagnostic claims, accurate wellbeing claims, crisis resource included
- Sensitive permissions (notification access, Accessibility Services) not required in MVP — deferred to Growth mobile interception feature
- Legal review of Play Store submission copy before submission — **hard gate**

---

### Integration Requirements

**LLM inference providers:**

Any LLM provider processing Soul Document content at inference time is a GDPR data processor and requires:
- Signed Data Processing Agreement (DPA) with zero data retention clause
- Confirmation that inference inputs are not retained for model training
- EU/UK data residency or Standard Contractual Clauses (SCCs) if processing occurs outside UK/EEA
- Preferred providers: those with explicit zero-retention inference modes (e.g., OpenAI Enterprise, Anthropic API with DPA)

**Annotation pipeline separation:**

The 2,000-message annotated dataset used for model training is governed by separate consent from message contributors and must not be linked to any commercial product user profile. Separate data environments enforced architecturally.

---

### Risk Register — Domain-Specific

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| EU AI Act reclassified as High Risk post-launch | Medium | High — conformity assessment required, potential launch pause | Legal opinion pre-launch; architecture built to High Risk standard where feasible |
| Chrome Web Store rejects extension for host permissions | Medium | High — blocks primary distribution channel | Pre-review submission; single-purpose justification; legal review of privacy policy |
| Google Play rejects app for sensitive permission claims | Low | Medium — blocks Android distribution | MVP avoids sensitive permissions entirely; legal review of submission copy |
| Soul Document accessed by abusive partner via shared device | Low | Critical — user safety | Biometric/PIN gate; domestic abuse scenario in engineering threat model |
| IRB data and commercial data commingled | Low | High — ethics violation, research invalidation | Separate data environments; architectural enforcement |
| I8 signpost triggers false positive — user distressed | Medium | Medium — user harm, trust damage | Specialist copy review; high confidence threshold (≥70%); 30-day suppression after dismiss |
| LLM provider retains Soul Document for model training | Low | High — GDPR breach | DPA with zero-retention clause; audit rights; preferred zero-retention providers |

### Risk Productisation — User Harm Prevention Features

The following risks are identified in the Risk Register above but require translation into concrete product features, not just process mitigations. Each risk below maps to a specific UI state or behavioural constraint.

**1. Over-reliance risk — user stops thinking for themselves**

NC's intervention could replace the user's own interpretive judgment rather than augmenting it. A user who blindly follows NC's predictions without engaging their own reading is not experiencing the neuroplasticity benefit and is vulnerable to NC errors.

| Product Response | Implementation | FR/NFR |
|---|---|---|
| **Confidence-first display** | Every prediction shows confidence score prominently — never hidden behind a tap. Users always see that NC is probabilistic, not definitive | FR09, FR10 |
| **Periodic self-check prompt** | After every 20th prediction, overlay includes: "What did you think they meant before NC weighed in?" — a 1-tap optional reflection that re-engages the user's own interpretive process | New: FR51 |
| **Accuracy trajectory visibility** | Users can see NC's accuracy on a per-sender basis over time. This surfaces that NC is a learning system, not an oracle | Growth feature — accuracy dashboard |
| **No auto-action** | NC never modifies, delays, or discards a reply automatically. The prediction is information; the decision is always the user's | Architectural constraint (enforced by FR12 — dismiss without action) |

**2. Emotional sensitivity risk — prediction surfaces during acute distress**

NC predictions on high-conflict messages could amplify distress if the timing or framing is wrong — e.g., telling a user their partner "is likely expressing frustration" during an active argument they're emotionally dysregulated about.

| Product Response | Implementation | FR/NFR |
|---|---|---|
| **High-ambiguity first** | When prediction entropy is high, NC leads with uncertainty ("NC isn't sure — here are possibilities") rather than a single label. This prevents false certainty in emotionally charged moments | FR04, FR14, NFR-M4 |
| **Rapid-fire suppression** | When ≥ 5 messages arrive from the same sender within 60 seconds (active argument pattern), NC suppresses overlay after the 3rd message and shows: "Conversation moving fast — NC is here when you're ready to pause." Overlay resumes after 2-minute gap | New: FR52 |
| **Cooling-off mode** | User can tap a single button to disable NC predictions for a specific conversation for 1 hour / 24 hours / indefinitely. Re-enables automatically or via settings | New: FR53 |
| **Emotional framing constraint** | Contextual notes (FR11) must never use accusatory language about the sender. Copy constraint: notes describe *patterns*, not *character* ("Messages often shorten when stressed" not "He's being dismissive") | UX copy guideline — binding on all contextual note templates |

**3. Misinterpretation compounding risk — NC is wrong and user acts on it**

If NC predicts the wrong intent and the user modifies their reply based on that wrong prediction, the misunderstanding could be worse than if NC hadn't intervened.

| Product Response | Implementation | FR/NFR |
|---|---|---|
| **One-tap correction** | Correction flow is accessible directly from the overlay — no navigation required. Reducing friction on "NC got this wrong" is a safety feature, not just a feedback mechanism | FR13, FR25, FR26 |
| **Low-confidence suppression** | When max-category confidence is below 40%, NC suppresses the overlay entirely rather than showing a likely-wrong prediction. The harm of a wrong prediction exceeds the value of a low-confidence one | New: NFR-M7 |
| **Wrong-prediction acknowledgement** | When a user flags a prediction as wrong, NC immediately displays: "Thanks — NC will weight your read more heavily for messages from [sender] going forward." This rebuilds trust in the moment of failure | FR28 (extended) |

**New Functional Requirements from Risk Productisation:**

- **FR51:** The system can display an optional self-check reflection prompt ("What did you think before NC weighed in?") at a configurable interval (default: every 20th prediction) to counter over-reliance
- **FR52:** The system can detect rapid-fire messaging patterns (≥ 5 messages from one sender in 60 seconds) and suppress overlay predictions after the 3rd message, resuming after a 2-minute conversation gap
- **FR53:** A user can temporarily disable NC predictions for a specific conversation for a selectable duration (1 hour, 24 hours, or indefinitely) via a single tap from the overlay

**New Non-Functional Requirement:**

- **NFR-M7:** When max-category confidence is below 40%, the intent prediction overlay must not be displayed. Suppression rate tracked via `overlay_suppressed` telemetry event to monitor model quality

---

## Innovation & Novel Patterns

---

### Detected Innovation Areas

**1. Person-Aware Intent Modelling via Soul Document**

Every existing NLP-based communication tool — Grammarly, Crystal Knows, Replika, tone analysers — operates on the message in isolation. NC is the first consumer product to condition intent prediction on a structured model of *who the person is*: their ranked values, stress response patterns, conflict archetypes, and relational narrative history.

The formal model: **P(intent | message, soul_document, relational_context)** — where the Soul Document is a persistent, user-owned personality layer injected at inference time. This is architecturally distinct from:
- Fine-tuning (Soul Document is not trained into the model — it is a prompt-layer injection, preserving updateability and user control)
- RAG from interaction history (Soul Document captures *who the person is*, not what they said last week)
- Persona APIs (Crystal Knows infers personality from public data; NC captures self-reported, private, nuanced personality at much higher resolution)

The commercial differentiator: NC knows who they are, not just what they said. This makes every prediction contextually grounded in the sender's actual psychology — not a generic interpretation of the words.

---

**2. Intent Gap as a Formal Metric**

NC introduces a novel measurable quantity to consumer communication: the **intent gap** — the divergence between what was meant (sender intent, SI) and what was received (perceived intent, PI), formalised as:

**Intent Gap = JS-divergence(P(SI), P(PI))**

Where SI is captured via sender self-annotation (gold standard) and PI is NC's real-time prediction of how the receiver will interpret the message. This is not a metaphor — it is a computable, trackable quantity that has never been operationalised at consumer scale.

The scientific significance: this makes relational misalignment *measurable* — allowing NC to track whether intent gaps narrow over time for users who train with the Soul Document, providing the mechanistic evidence for H1 (intent prediction accuracy), H2 (conflict de-escalation), and H3 (relational satisfaction).

The product significance: users can see, concretely, that NC improved their understanding of a specific sender. Improvement is not a feeling — it is a tracked delta.

---

**3. Receiver-Side Biological Window Targeting**

The intervention timing in NC is grounded in a specific neurobiological mechanism: the 40–800ms window between message receipt and amygdala threat-tagging. Within this window, the brain is still in interpretive mode — threat has not yet been embedded. NC's interception goal is to surface the intent prediction *before* the amygdala fires, inserting a re-appraisal signal into the cognitive pathway before the emotional response is complete.

This is categorically different from post-hoc communication coaching (Reflectly, therapy apps) or pre-send nudges (Grammarly tone detection). NC intervenes at the *moment of reception*, in the *biological window where intervention has maximum effect*. The < 800ms latency target is not a UX performance target — it is a neuroscience-derived constraint.

No competitor has articulated, let alone designed to, this specific intervention window.

---

**4. Cold-Start Accuracy via Personality Injection**

The standard cold-start problem in AI personalisation: the system is useless until it has accumulated enough interaction history to calibrate. NC solves cold-start differently — the Soul Document provides a rich personality layer from Day 1, before any message history exists. A user who completes the Soul Document intake on onboarding has a higher-accuracy prediction engine from their *first* message than any interaction-history-based system achieves after months of use.

This creates a compounding advantage: the Soul Document gets richer over time, meaning NC's accuracy trajectory is fundamentally different from competitor approaches (steep initial improvement vs. NC's high baseline with continued refinement).

---

**5. Hypothesis-Driven Product Development — The Product Is the Experiment**

NC is being built as a scientific instrument that happens to be a consumer product. The three core hypotheses (H1: intent prediction accuracy, H2: conflict reduction, H3: relational satisfaction) are pre-registered, falsifiable, and designed to produce a publishable result regardless of outcome. If NC fails to improve relational outcomes, that is a contribution to the literature.

NC's RCT design means the product team will have causal evidence — not correlational — for NC's effect on communication outcomes within the fellowship year. This evidence is the foundation for institutional credibility, clinical adoption, and research partnership that no competitor can acquire through product iteration alone.

---

### Market Context & Competitive Landscape

**The white space NC occupies:**

| Category | Example products | What they do | What they miss |
|---|---|---|---|
| Pre-send tone detection | Grammarly, Hemingway | Analyse your draft before you send | Do not address received message interpretation; no soul model; no relational history |
| Personality profiling | Crystal Knows, DISC tools | Infer personality from public data | No real-time message interception; no intent prediction; professional context only |
| Post-hoc relationship coaching | Gottman apps, Lasting | Reflect on past interactions | No real-time intervention; no message-level analysis; therapeutic framing |
| General AI assistants | ChatGPT, Claude | Answer questions including "what did they mean?" | No soul document; no persistent relational context; user-initiated only; no scientific validation |
| Mindfulness / emotional regulation | Headspace, Calm | Regulate your own state | Do not address the source of the trigger; no message analysis |

**NC's unoccupied position:** Real-time, receiver-side, person-aware intent prediction grounded in neuroscience and validated by a pre-registered RCT. No product in any of these categories is building toward this position.

**Closest emerging threat:** Large AI platforms adding relationship/communication intelligence to general assistants. NC's moat: the Soul Document architecture (depth of person-model), the relational dataset (annotated intent-gap pairs), and the scientific credibility (RCT results). These are not replicable by prompt engineering.

---

### Validation Approach

| Innovation | Validation Method |
|---|---|
| Person-aware modelling | Ablation study within RCT — accuracy with Soul Document active vs. disabled on matched message sets |
| Intent gap metric | Pre/post JS-divergence measurement in RCT — reduction in intent gap for NC users vs. control group |
| Biological window targeting | Instrumented latency measurement — sub-800ms confirmed at 95th percentile of production traffic before launch |
| Cold-start via personality injection | Day 1 accuracy (Soul Document only) vs. interaction-history-based system at Day 30 — target: NC Day 1 ≥ competitor Day 30 |
| Hypothesis-driven development | RCT pre-registered before recruitment; results published regardless of direction |

---

### Risk Mitigation

| Innovation Risk | Likelihood | Mitigation |
|---|---|---|
| Soul Document accuracy contribution smaller than expected | Medium | Modular architecture — additional intake dimensions added iteratively without model retraining |
| Intent gap metric too noisy to be meaningful | Medium | Pre-launch calibration on annotation dataset; JS-divergence threshold tuned before RCT |
| < 800ms latency not achievable with full Soul Document injection | Medium | Tiered inference: lightweight prediction first (< 200ms), Soul Document enrichment layer second (< 600ms additional) |
| Large platform replicates person-aware intent prediction | Low (12-month horizon) | Moat is relational dataset + Soul Document depth + RCT credibility; file provisional patents on Soul Document architecture + intent gap metric before launch |
| RCT results null or negative | Low-Medium | Pre-registered null result is publishable; NC pivots on evidence; Soul Document architecture retains independent value regardless of RCT outcome |
| Soul Document becomes a coercive control tool | Low | Architectural prohibition on partner access; domestic abuse threat model reviewed at every feature addition |

---

## Multi-Surface Specific Requirements

---

### Project-Type Overview

NC is a **dual-surface product** with asymmetric responsibilities across surfaces:

| Surface | Primary Role | Runtime Context |
|---|---|---|
| **Chrome Extension (MV3)** | Real-time intent prediction — the core value delivery layer | Desktop browser, persistent content script, < 800ms inference loop |
| **Mobile App (React Native)** | Soul Document management + async reflection — the depth and trust layer | iOS + Android, offline-first, notification-driven |

The surfaces are architecturally coupled at the Soul Document layer (shared encrypted data model) but independently deployable. The extension can function without the mobile app; the mobile app without the extension provides Soul Document management only. Desktop is the primary interception channel in MVP; mobile is the onboarding and retention layer.

---

### Platform Requirements

**Chrome Extension — MV3**

| Requirement | Specification |
|---|---|
| Manifest version | MV3 — no legacy MV2 fallback |
| Background execution | Service worker (not persistent background page) — all persistent state managed via `chrome.storage` |
| Content script injection | Declarative injection via `content_scripts` manifest key; dynamic injection via `chrome.scripting.executeScript` for late-loading SPAs |
| Host permissions | Declared in manifest: `mail.google.com`, `web.whatsapp.com`, `app.slack.com`, `messages.google.com` — no wildcard permissions |
| Storage | `chrome.storage.local` for extension state; Soul Document cloud sync deferred to Growth |
| Minimum Chrome version | Chrome 102+ (MV3 stable) |
| Cross-browser | Chrome only in MVP; Firefox and Safari Web Extensions as Growth — separate compliance review per browser |

**Mobile App — React Native**

| Requirement | Specification |
|---|---|
| Framework | React Native (latest stable LTS at build time) |
| iOS minimum | iOS 15.0+ (~95% of active iOS devices) |
| Android minimum | API 26 / Android 8.0 (~95% of active Android devices) |
| Navigation | React Navigation v6 (stack + tab navigator) |
| State management | Zustand (lightweight; no Redux overhead for MVP scope) |
| Offline-first | Full offline capability required — all Soul Document read/write operations must function without network |
| Build tooling | Expo managed workflow for MVP; eject to bare workflow if native modules require it at Growth |

---

### Device Permissions

**Chrome Extension permissions matrix:**

| Permission | Purpose | MVP | Store Justification |
|---|---|---|---|
| `host_permissions` (4 domains) | Content script injection for message interception | Yes | Single-purpose: intent prediction on declared messaging platforms |
| `storage` | Extension state persistence | Yes | Standard — no user data stored server-side |
| `scripting` | Dynamic content script execution | Yes | Required for SPA platforms (Slack, WhatsApp Web) that load asynchronously |
| `activeTab` | Overlay injection into active tab | Yes | Scoped to active tab only — not persistent access |
| `notifications` | System notification for high-ambiguity alert | No | Deferred — overlay-based MVP does not require |

**Mobile App permissions matrix:**

| Permission | Platform | Purpose | MVP |
|---|---|---|---|
| `FaceID` / `TouchID` | iOS | Biometric gate on Soul Document | Yes |
| `USE_BIOMETRIC` / `USE_FINGERPRINT` | Android | Biometric gate on Soul Document | Yes |
| `POST_NOTIFICATIONS` (Android 13+) | Android | Async reflection push prompts | Yes |
| `UserNotifications` | iOS | Async reflection push prompts | Yes |
| Camera / Location / Microphone | Both | Not required | No — never in MVP |
| `RECEIVE_SMS` / Accessibility Services | Android | Mobile real-time interception | No — Growth only |

---

### Offline Mode

**Extension:** Not applicable — inherently online. If inference API unreachable: overlay suppressed, no error state shown, message reading unblocked. NC never delays the user.

**Mobile App — fully offline for all MVP features:**

| Feature | Offline behaviour |
|---|---|
| Soul Document read / view | Fully offline — local storage only |
| Soul Document edit | Fully offline — writes to encrypted local store; sync queued when online |
| Onboarding intake | Fully offline — YAML extraction runs locally; falls back to manual intake if LLM inference unavailable |
| Async reflection prompts | Scheduled locally — local notification delivery; no push server dependency in MVP |
| Reflection journal entries | Fully offline — stored locally; no server upload without explicit user action |

**Data layer:** `expo-sqlite` for structured Soul Document storage + `react-native-keychain` for AES-256 encryption key management. SQLite database file encrypted at rest on both platforms via Android Keystore (Android) and iOS Keychain (iOS).

---

### Push Notification Strategy

**MVP: Local notifications only** — no push server infrastructure required.

| Notification type | Trigger | Delivery | Phase |
|---|---|---|---|
| Daily reflection prompt | User-configured time (default: 8pm) | Local | MVP |
| Weekly pattern summary | Sunday 10am | Local | MVP |
| High-ambiguity alert (I8 threshold) | Client-side pattern detection | Local | MVP |
| Accuracy improvement confirmation | Post-correction feedback | Local | MVP |
| Consent network request | Partner requests mutual intent sharing | Push (APNs / FCM) | Growth |

**Push infrastructure (Growth):** APNs + FCM. Zero PII in push payload — notification body assembled client-side from payload token.

---

### Technical Architecture Considerations

**Content script ↔ Service worker communication:**

MV3 service workers are ephemeral (spin down after ~30s inactivity). All persistent state must be in `chrome.storage.local`. Content scripts communicate via `chrome.runtime.sendMessage` / `chrome.runtime.onMessage`. If the service worker is inactive at message receipt, Chrome restarts it — content script handles startup latency with retry (max 2 retries, exponential backoff) before silent degradation.

**Inference pipeline:**

```
Content script (message receipt)
  → extract message text + sender ID
  → chrome.runtime.sendMessage → service worker
    → retrieve Soul Document context (chrome.storage.local)
    → construct inference payload
    → POST to NC inference API (target: < 600ms)
    → receive intent prediction
  → chrome.runtime.sendMessage → content script
    → render intent overlay UI (target: < 200ms)
Total end-to-end: < 800ms
```

**Tiered inference fallback** (if Soul Document injection exceeds latency budget):
1. Lightweight prediction (message only) — < 200ms — display immediately
2. Soul Document enrichment pass — < 600ms additional — update overlay if enriched prediction differs significantly

**Per-Session Consent UX — Soul Document Transmission:**

The privacy constraint "No Soul Document content transmitted to server without explicit per-session user consent" requires a specific consent flow. This is the UX specification:

**Context:** When the extension performs tiered inference, the enrichment pass transmits a Soul Document excerpt (relevant fields only, not the full document) to the NC inference API as part of the request payload. This transmission occurs every time a message is processed with Soul Document enrichment. The per-session consent gate governs *whether* the enrichment pass runs at all during a browser session.

**Session consent flow:**

1. **First overlay of a new browser session:** Before the enrichment pass runs, the extension displays a one-time session consent banner in the overlay area: *"NC would like to use your Soul Document to improve predictions this session. Your personality data is sent encrypted and never stored on our servers."*
2. **User options:**
   - **"Allow this session"** — Soul Document enrichment enabled for the remainder of the browser session. Consent expires when the browser closes or after 24 hours, whichever is first
   - **"Always allow"** — Persistent consent stored in `chrome.storage.local`. No further session prompts. User can revoke in extension settings at any time
   - **"Not now"** — Enrichment pass skipped for this session. Lightweight predictions only. No further prompts until next session
3. **Consent state transitions:**
   - Browser session ends → consent reverts to default (unless "Always allow" was selected)
   - User revokes "Always allow" in settings → next session prompts again
   - User deletes Soul Document → consent state cleared automatically
4. **No-consent behaviour:** NC operates in message-only inference mode (lightweight predictions). The overlay does not indicate that enrichment was declined — it simply shows baseline predictions. No degradation messaging, no guilt prompting.

**Design constraints:**
- The consent banner must not block message reading — it appears *alongside* the first lightweight prediction, not *instead of* it
- The consent banner must be dismissible in one action (tapping outside the banner = "Not now")
- Consent state is never transmitted to NC servers — it is a client-side gate only
- The "Always allow" option must be discoverable in extension settings with a clear explanation of what is transmitted

**New Functional Requirements:**

- **FR54:** The system can prompt for per-session Soul Document transmission consent on first overlay display of each browser session, without blocking message reading or the lightweight prediction
- **FR55:** A user can grant persistent Soul Document transmission consent ("Always allow") and revoke it at any time via extension settings
- **FR56:** The system can operate in message-only inference mode when Soul Document transmission consent has not been granted, with no UX degradation beyond reduced prediction accuracy

**React Native ↔ Extension data bridge (MVP):**

No live data bridge in MVP. Soul Document authored on mobile; extension reads a cached copy synced via QR-code-based device pairing or manual export (iCloud / Google Drive). Cloud sync with E2E encryption is a Growth feature.

---

### Accessibility — WCAG 2.1 AA

The intent prediction overlay is NC's primary UI element. Non-negotiable accessibility requirements:

- All intent labels have accessible text alternatives — no icon-only display
- Overlay is keyboard navigable (Tab / Enter / Escape)
- Confidence display does not rely solely on colour (colour-blind users)
- Overlay respects `prefers-reduced-motion` — no animation if reduced motion set
- React Native: all interactive elements have `accessibilityLabel` props; screen reader tested on VoiceOver (iOS) and TalkBack (Android)

---

### Store Compliance Checklist

*(Full requirements in Domain-Specific Requirements — this is the implementation checklist)*

| Check | Chrome Web Store | App Store | Play Store |
|---|---|---|---|
| Single-purpose declaration | ✓ Required | N/A | N/A |
| Privacy policy URL | ✓ Required | ✓ Required | ✓ Required |
| Host permissions justification | ✓ Each domain justified | N/A | N/A |
| No diagnostic / therapeutic claims | N/A | ✓ Guideline 1.4.2 | ✓ Wellness policy |
| Crisis resource present | N/A | ✓ Required | ✓ Required |
| Legal review of submission copy | ✓ Hard gate | ✓ Hard gate | ✓ Hard gate |
| Pre-review submission | ✓ Hard gate | N/A | N/A |
| Data safety / privacy nutrition label | N/A | ✓ Required | ✓ Required |

**Data safety declaration (both mobile stores):** No user data transmitted to NC servers in MVP. LLM inference payload (message text + Soul Document excerpt) declared as "App functionality — encrypted in transit — not sold." Full data deletion supported (≤ 3 taps, timestamp confirmation).

---

### Implementation Sequencing

**Extension first, mobile second.** The extension is the value-delivery surface. Ship extension in working state before mobile app is available. The extension must include a fallback inline onboarding flow (simplified Soul Document intake) for the pre-mobile-app period — users cannot be blocked from using NC because the mobile app is not yet released.

---

## Project Scoping & Phased Development

---

### Phase 0 Strategy & Philosophy

**Phase 0 Approach: Platform MVP + Conversational Surface**

NC's Phase 0 is a **platform MVP** — the goal is to ship the infrastructure that makes all future NC applications possible: the Soul Document layer, the Relationship Context layer, the intent prediction engine, and both interaction surfaces (conversational companion + real-time overlay). Phase 0 also generates the annotation dataset (via user corrections) that enables Phase 1's fine-tuned model. Every scoping decision protects this platform layer and defers application-layer features.

The test of a valid Phase 0 feature: *"Does this teach us something we cannot learn any other way, does it generate training data, or does it protect a user from harm?"* If none, it is Growth.

**Phase 0 Philosophy: Two modes, one model, done properly.**

Ship both the conversational companion (mobile + web) and WhatsApp Web overlay with Soul Document v1 + Relationship Context, powered by Llama 3.1 70B on own infrastructure. Prove two core loops: (1) user pastes message → NC interprets → user reflects → better response; (2) message arrives → NC intercepts → intent predicted → user modifies response. Both modes generate corrections that build the annotation dataset for Phase 1.

**MVP Team Requirements:**

| Role | Responsibility | FTE |
|---|---|---|
| ML / AI engineer | Intent prediction model, Soul Document injection pipeline, inference API | 1 |
| Frontend / Extension engineer | Chrome MV3 extension, content script, overlay UI | 1 |
| React Native engineer | Mobile app (Soul Document intake, reflection layer, cross-platform) | 1 |
| Product / Researcher | Soul Document design, annotation pipeline, RCT protocol, IRB liaison | 1 (founder) |
| Legal / compliance | GDPR DPA, EU AI Act review, store submission copy | 0.25 (retained advisor) |

**Minimum viable team: 3 engineers + 1 founder-researcher.**

---

### Phase 0 Feature Set

**Core journeys supported in Phase 0:**
- ✅ Journey 1: Core Receiver — Success Path (overlay + conversational)
- ✅ Journey 2: Core Receiver — Edge Case (trust recovery)
- ✅ Journey 3: New User Onboarding (conversational intake on mobile/web)
- ✅ Journey 4: Institutional Referral (lightweight — referral card only, no therapist account)
- ⚠️ Journey 5: Ops / Admin (manual process — no admin UI)

**Phase 0 Capabilities:**

| Capability | Surface | Rationale |
|---|---|---|
| **Conversational companion** — paste message, ask for interpretation + reply suggestions | Mobile + Web | Core Phase 0 value: deliberate reflection on received messages |
| **Reply suggestion generation** — NC suggests contextually grounded responses | Mobile + Web | Extends companion from interpretation to actionable output |
| WhatsApp Web real-time message interception | Extension | Primary overlay channel; highest intimate-relationship traffic |
| Intent prediction overlay UI (non-intrusive, dismissible) | Extension | Real-time value delivery alongside conversational mode |
| 8-category intent label space with confidence display | Extension + Companion | Validated in annotation study; satisfies EU AI Act Article 50 |
| High-ambiguity / low-confidence flag | Extension + Companion | Trust recovery UX |
| "NC got this wrong" correction flow | Extension + Companion | Per-sender calibration; accuracy feedback loop; annotation dataset generation |
| Soul Document v1 — full guided intake (conversational, 3 questions, ≤ 10 min) | Mobile + Web | Rich cold-start accuracy; biometric-gated trust |
| **Relationship Context per-person injection** | All surfaces | Per-sender data structure (Soul Doc Arch Spec v0.3 §5b) injected at inference time |
| Soul Document summary view + edit | Mobile + Web | User review and control of personality layer |
| Soul Document YAML extraction from natural language | Mobile + Web | NC-automated extraction; user answers in prose |
| AES-256 encrypted local storage (Keychain / Keystore) | All | Privacy-by-design hard constraint |
| Biometric / PIN gate on Soul Document | Mobile | Domestic abuse scenario protection — hard constraint |
| Full data deletion (≤ 3 taps + timestamp confirmation) | All | GDPR right to erasure — hard constraint |
| Daily reflection prompt (local notification) | Mobile | Retention mechanism; neuroplasticity window engagement |
| Reply modification instrumentation (passive) | Extension | Core success metric — no prompts, passive tracking only |
| I8 safeguarding signpost (client-side, no server logging) | Extension | User safety — hard constraint |
| **Conversational safeguarding** (FR57–FR60) | Companion | Abuse disclosure handling, emotional dependency detection, manipulation refusal, cooling-off |
| QR-code device pairing (extension ↔ mobile Soul Document sync) | Extension + Mobile | Phase 0 data bridge — no cloud infrastructure required |
| Shareable institutional referral card | Extension / Web | Journey 4 — therapist attribution link |
| PII-redacted correction logs (structured for manual review) | API | Ops / admin captured correctly even if surfaced manually |
| GDPR consent gate (pre-Soul Document creation) | All | Hard gate — explicit consent separate from ToS |
| Per-session Soul Document transmission consent | All | Privacy control per-session |
| **Llama 3.1 70B inference on own infrastructure** | API | Architectural privacy — open-source, verifiable, zero-retention |

**Phase 0 explicitly excludes:**

| Feature | Phase |
|---|---|
| Gmail, Slack, iMessage Web interception | Growth |
| Firefox / Safari extensions | Growth |
| Mobile real-time message interception (iOS or Android) | Growth |
| Admin UI / report queue dashboard | Growth |
| Cloud sync / multi-device Soul Document | Growth |
| Soul Document v2 (Layers 4–6) | Growth |
| Partner consent network | Vision |
| Clinician dashboard | Growth |
| Voice channel support | Vision |
| Cross-language support | Growth |
| Fine-tuned intent prediction model | Phase 1 |

---

### Phase 1 Feature Set — Fine-Tuned Model

*Built after Phase 0 annotation dataset is sufficient for LoRA fine-tuning.*

Phase 1 enhances the overlay with a fine-tuned model trained on Phase 0 user corrections. The conversational companion continues unchanged. Both modes coexist.

**Phase 1 adds:**

| Capability | Surface | Rationale |
|---|---|---|
| LoRA fine-tuned intent prediction model | API | Higher accuracy from NC-specific training data |
| Gmail, Slack, iMessage Web interception | Extension | Channel expansion post WhatsApp Web validation |
| Tiered inference (lightweight first, Soul Document enrichment second) | Extension + API | Latency budget compliance with fine-tuned model |
| Simplified 3-question inline onboarding (extension fallback) | Extension | Unblocks extension-first users |
| Revenue / payment infrastructure | All | Freemium conversion: Phase 0 free → paid premium features |

**Phase 1 targets:**

| Metric | Target |
|---|---|
| Intent accuracy (with Soul Document) | ≥ 85% |
| End-to-end overlay latency (P95) | < 800ms |
| Phase 0 → Phase 1 adoption | ≥ 30% of Phase 0 users |

---

### Post-MVP Features — Phase 2 (Growth)

*Target: Months 7–18 post-MVP launch*

**Channel expansion:** Gmail, Slack web, iMessage web (Safari Web Extension, separate review pathway)

**Mobile interception:** iOS Share Extension (WhatsApp); Android notification listener (WhatsApp + SMS, pending Play Store policy review). Both require independent compliance review and domestic abuse threat model re-review before shipping.

**Soul Document deepening:** v2 intake (Layers 4–6: Narrative History, Relational Maps, Temporal Patterns); automated story tagging; per-sender calibration history surfaced to user

**Platform enhancements:** Cloud sync with E2E encryption; multi-device access; in-app accuracy trajectory view; weekly pattern insight notifications

**Ops tooling:** Admin report queue; correction pattern aggregation; model quality routing; known-limitations register (public)

**Institutional pathway:** Therapist account (read-only, consent-gated); clinician privacy + research summary; partnership inquiry → LOI workflow

---

### Post-MVP Features — Phase 3 (Vision)

*Target: 18–36 months, post-RCT results*

- **Consent network:** Bilateral opt-in intent sharing; ethics review + coercive control architecture review required before build
- **Neuroplasticity programme:** Structured 60-day programme grounded in H3 mechanism
- **Voice channel:** Real-time intent prediction on voice messages and calls; new model architecture required
- **Clinician dashboard:** Aggregate pattern trends (not message content); consent-gated
- **Cross-language support:** Spanish, Mandarin, Hindi
- **Foundation model open release:** Intent prediction model + annotated dataset as open-source scientific infrastructure
- **Institutional integration API:** Headless NC engine for therapy platforms, HR tools, co-parenting apps
- **Temporal drift detection:** NC detects divergence between a user's Soul Document and a sender's evolving communication patterns — a leading indicator of relational deterioration before either party is consciously aware of it
- **Neurodivergent calibration programme:** ND-specific Soul Document intake and intent model calibration, validated by a three-group RCT (ND vs. neurotypical receiver; ND vs. NT sender); addresses the intent-expression gap unique to ADHD and ASD communicators

---

### Risk Mitigation Strategy

**Technical risks:**

| Risk | Mitigation |
|---|---|
| WhatsApp Web DOM changes break content script | Versioned content script adapters; automated DOM regression tests on CI |
| < 800ms latency not achievable at launch | Tiered inference architecture — acceptable degradation path defined |
| Soul Document YAML extraction insufficient for cold-start accuracy | Pre-launch calibration on extraction prompts; user review/edit gate catches errors |
| MV3 service worker drops messages | Stateless inference pipeline — each message a self-contained request; no in-memory state required |

**Market risks:**

| Risk | Mitigation |
|---|---|
| WhatsApp Web blocks extension | Modular channel adapter architecture — Gmail is backup primary channel |
| User adoption slower than expected | Waitlist pre-launch; therapist referral channel seeded before general availability; RCT participants as early adopter cohort |
| Trust barrier to Soul Document completion | Inline 3-question fallback means users experience NC value before committing to full Soul Document intake |
| Large platform copies core mechanic | Patent filing on Soul Document architecture + intent gap metric before launch |

**Resource risks:**

| Risk | Mitigation |
|---|---|
| ML engineer unavailable at launch | Pre-trained base model via API (Anthropic / OpenAI); NC adds Soul Document injection — not training from scratch in MVP |
| React Native scope creeps | Mobile MVP strictly Soul Document management + reflection — no feature additions without explicit scope decision |
| Legal / compliance delays store submission | Store review initiated 6 weeks before target launch; legal review begins at feature-freeze, not at submission |
| Fellowship year ends before 300-user target | Month 9 checkpoint: if active users < 150, trigger therapist referral acceleration and institutional partnership push |

---

### MVP Launch Gate Sequence

| Milestone | Gate | Timing |
|---|---|---|
| Inference API live — 75% accuracy on held-out test set | Accuracy validation | Pre-alpha |
| Extension inline onboarding + overlay UI complete | WCAG 2.1 AA audit; < 800ms at P95 | Pre-alpha |
| Mobile Soul Document intake + QR sync complete | Biometric gate tested on iOS + Android | Alpha |
| IRB approval for RCT | Hard gate — no study recruitment before this | Alpha |
| GDPR consent flow + data deletion verified | Legal sign-off | Beta |
| EU AI Act legal opinion received | Hard gate — no public launch before this | Beta |
| I8 safeguarding signpost reviewed by specialist | Hard gate | Beta |
| Chrome Web Store pre-review submitted and accepted | Hard gate | Beta |
| App Store + Play Store legal review + submission accepted | Hard gate | Launch |

---

## Functional Requirements

---

### 1. Message Interception & Intent Prediction

- **FR01:** The system can detect when a new message arrives on a supported messaging platform in an active browser tab
- **FR02:** The system can extract message text and sender identity from a supported messaging platform without storing message content beyond the inference call
- **FR03:** The system can classify a received message into one of eight intent categories with an associated confidence score. The intent label space must cover social nuance categories including irony and sarcasm, passive aggression, and deference and politeness — these are not edge cases but high-frequency sources of the intent gap in intimate communication
- **FR04:** The system can identify when a message has high entropy across intent categories and flag it as high-ambiguity
- **FR05:** The system can apply Soul Document context to enrich a base intent prediction with person-specific calibration
- **FR06:** The system can detect when the inference API is unreachable and degrade gracefully without blocking or delaying message reading
- **FR07:** The system can perform tiered inference — producing a lightweight prediction first, then an enriched prediction when Soul Document context is available

---

### 2. Intent Prediction Overlay UI

- **FR08:** A receiver can view an intent prediction overlay when a new message arrives, before composing a reply
- **FR09:** A receiver can view the primary predicted intent label and confidence score in the overlay
- **FR10:** A receiver can view a secondary intent label and confidence score when the prediction distribution is non-uniform
- **FR11:** A receiver can view a contextual note explaining why NC predicts this intent based on sender patterns from the Soul Document
- **FR12:** A receiver can dismiss the intent prediction overlay without taking any action
- **FR13:** A receiver can flag a prediction as incorrect directly from the overlay
- **FR14:** A receiver can view a high-ambiguity indicator when NC cannot predict intent with sufficient confidence
- **FR15:** A receiver can view the I8 safeguarding signpost when a sustained coercive communication pattern is detected from a sender

---

### 3. Soul Document Management

- **FR16:** A user can create a Soul Document by completing a guided conversational intake
- **FR17:** The system can extract structured personality data (values, stress responses, narrative story) from a user's natural language intake responses
- **FR18:** A user can review the structured Soul Document summary before activating it
- **FR19:** A user can edit any field in their Soul Document summary before or after activation
- **FR20:** A user can activate their Soul Document to enable person-aware intent prediction
- **FR21:** A user can view their complete Soul Document in a readable summary format at any time
- **FR22:** A user can complete a simplified 3-question intake via the browser extension when the mobile app is not available
- **FR23:** A user can access their Soul Document only after passing biometric or PIN authentication
- **FR24:** A user can permanently delete all NC data including their Soul Document in three or fewer steps, with deletion confirmed by timestamp
- **FR24a:** The system can operate in message-only inference mode when no Soul Document exists — delivering lightweight intent predictions without person-aware enrichment
- **FR24b:** A user who declines or skips Soul Document creation can still receive intent predictions at baseline accuracy, with a non-intrusive periodic prompt (maximum once per week) to complete intake
- **FR24c:** The system can display a contextual indicator distinguishing baseline predictions (no Soul Document) from person-aware predictions (Soul Document active), so users understand the accuracy difference

**Soul Document — Empty / Declined Fallback Behaviour:**

NC must function without a Soul Document. The Soul Document improves accuracy but is not a prerequisite for value delivery. The following table defines system behaviour across Soul Document states:

| Soul Document State | Inference Behaviour | UI Indicator | Prompt Behaviour |
|---|---|---|---|
| Not yet created (new user) | Message-only inference (no enrichment pass) | Subtle badge: "Basic mode — NC works better when it knows you" | Inline onboarding prompt on first session; weekly soft prompt thereafter (max 4, then silent) |
| Created but not activated | Message-only inference | Badge: "Soul Document ready — activate to improve accuracy" | One-tap activation prompt in overlay footer |
| Activated | Full tiered inference (lightweight + enrichment) | No badge — this is the default state | — |
| Deleted by user | Message-only inference; all calibration data cleared | Badge returns to "Basic mode" state | No prompt for 30 days after deletion; then single re-engagement prompt; if dismissed, no further prompts |
| Partially completed (intake abandoned) | Message-only inference; partial data discarded (not used) | Badge: "Basic mode" | Resume prompt on next mobile app open; partial data auto-deleted after 7 days if not resumed |

**Design constraint:** NC must never block, gate, or degrade the core message-reading experience based on Soul Document state. A user who never creates a Soul Document still receives intent predictions — just at baseline accuracy (75% floor vs. 85% with Soul Document).

---

### 4. Correction & Calibration

- **FR25:** A receiver can submit a correction when NC's intent prediction does not match their interpretation
- **FR26:** A receiver can select the correct intent label from the 8-category label space when submitting a correction
- **FR27:** The system can record corrections as a per-sender calibration signal linked to the receiver's Soul Document context
- **FR28:** The system can surface an acknowledgement to a user when their correction has been included in the next model calibration update batch — within **72 hours** of submission or at the next model update, whichever comes first
- **FR29:** The system can track correction patterns across ≥ 5 messages from the same sender to detect systematic calibration gaps, and flag the pattern to the ML team when ≥ 3 of those corrections share the same direction (e.g., consistently under-predicting a specific intent category for that sender)

---

### 5. Onboarding & User Activation

- **FR30:** A new user can install the browser extension and reach a working intent prediction state without requiring the mobile app to be installed
- **FR31:** A new user can understand what NC does, what the Soul Document is, and what data NC accesses, before providing any personal information
- **FR32:** A new user can complete the GDPR consent process as a distinct step before Soul Document creation begins
- **FR33:** The system can present the Soul Document onboarding as a conversational flow — sequential questions with free-text responses, no form elements or multi-field screens — with a target completion time of **≤ 10 minutes** for the standard 3-question intake
- **FR34:** A user can pair their browser extension with their mobile app via QR code to sync their Soul Document across surfaces

---

### 6. Reflection & Retention

- **FR35:** A user can receive a daily async reflection prompt at a user-configured time via local notification
- **FR36:** A user can receive a weekly pattern summary notification highlighting communication themes that appeared in ≥ 3 messages from the same sender within the preceding 7 days — delivered at the user's configured reflection time (default: Sunday 10:00 local), suppressible, and limited to the **top 3 senders** by pattern frequency
- **FR37:** A user can write and save a reflection journal entry in response to a prompt
- **FR38:** A user can view their reflection journal history within the mobile app

---

### 7. Institutional Referral

- **FR39:** A clinician or institutional user can generate a shareable referral card for NC containing product description, privacy architecture summary, and a direct install link
- **FR40:** The system can attribute installs to a referring clinician via a unique referral link for tracking purposes
- **FR41:** A clinician or institutional user can submit an inquiry about partnership or clinical integration via a contact pathway

---

### 8. Privacy, Safety & Compliance

- **FR42:** The system can store the Soul Document on-device in encrypted form without transmitting it to NC servers except as part of a transient inference payload
- **FR43:** The system can process message content transiently — input to inference, prediction returned, message content discarded — with no server-side persistence of message text
- **FR44:** The system can display the I8 safeguarding signpost with regional crisis resource links when a coercive communication pattern threshold is met, without logging which users triggered it
- **FR45:** The system can suppress the I8 safeguarding signpost for 30 days after a user dismisses it
- **FR46:** The system can enforce architectural prohibition on any mechanism that allows one user to access another user's Soul Document
- **FR47:** A user can view a plain-language explanation of what data NC accesses, stores, and transmits at any point during onboarding or post-activation

---

### 9. Conversational Companion (Phase 0)

- **FR57:** If the user shares content in the conversational companion indicating they are experiencing abuse, coercive control, or domestic violence, NC must surface safeguarding resources (same regional crisis links as I8 signpost) without logging the disclosure to NC servers
- **FR58:** If NC detects a pattern of user relying on NC for interpersonal decisions at a rate exceeding 10 consultations per day sustained over 7 consecutive days, NC must surface a self-check prompt (dismissible, 7-day suppression after dismissal)
- **FR59:** If the user asks NC to help craft a manipulative, deceptive, or coercive message, NC must decline and explain why — implemented as a model-level guardrail (system prompt constraint), not keyword matching
- **FR60:** If the user submits > 5 emotionally charged messages about the same person in a single session (no gap > 30 minutes), NC must surface a cooling-off suggestion (dismissible, does not block use)
- **FR61:** A user can paste a message from any sender into the conversational companion and receive an intent interpretation grounded in their Soul Document and Relationship Context for that sender
- **FR62:** NC can generate contextually grounded reply suggestions in the conversational companion, informed by the user's Soul Document values and communication style
- **FR63:** The conversational companion must stream responses in real time, with first token visible within **2 seconds** and full response within **5 seconds** at P95

---

### 10. Ops & Quality (Internal)

- **FR48:** The system can capture correction events as PII-redacted structured logs accessible to the NC operations team
- **FR49:** An NC operations team member can review correction reports containing redacted message content, the prediction made, and the user's correction
- **FR50:** The system can route a quality flag to the ML team when a correction pattern indicates a systematic model calibration gap

---

### Capability Contract — Coverage Validation

| Capability | FR Coverage | Phase |
|---|---|---|
| **Conversational companion** — interpretation + reply suggestions | FR61, FR62, FR63 | Phase 0 |
| **Conversational safeguarding** — abuse, dependency, manipulation, cooling-off | FR57, FR58, FR59, FR60 | Phase 0 |
| WhatsApp Web interception | FR01, FR02, FR06 | Phase 0 |
| Intent prediction overlay | FR08–FR15 | Phase 0 |
| 8-category intent + confidence | FR03, FR09, FR10 | Phase 0 |
| High-ambiguity flag | FR04, FR14 | Phase 0 |
| Correction flow | FR25–FR29 | Phase 0 |
| Soul Document v1 intake (mobile + web) | FR16–FR21 | Phase 0 |
| Biometric / PIN gate | FR23 | Phase 0 |
| Full data deletion | FR24 | Phase 0 |
| Daily reflection prompt | FR35 | Phase 0 |
| I8 safeguarding signpost (overlay) | FR15, FR44, FR45 | Phase 0 |
| QR pairing | FR34 | Phase 0 |
| Institutional referral card | FR39, FR40 | Phase 0 |
| PII-redacted correction logs | FR48, FR49 | Phase 0 |
| GDPR consent gate | FR32 | Phase 0 |
| Architectural prohibition (partner access) | FR46 | Phase 0 |
| Soul Document fallback (no/declined/deleted) | FR24a, FR24b, FR24c | Phase 0 |
| Over-reliance self-check prompt | FR51 | Phase 0 |
| Rapid-fire suppression | FR52 | Phase 0 |
| Cooling-off mode | FR53 | Phase 0 |
| Per-session Soul Document consent | FR54, FR55, FR56 | Phase 0 |
| Tiered inference (fine-tuned model) | FR07 | Phase 1 |
| Inline onboarding (extension fallback) | FR22, FR30, FR31 | Phase 1 |

> ⚠️ **Capability Contract is now binding.** 63 FRs across 10 capability areas. Any feature not listed does not exist in the final product unless explicitly added via a scope change decision.

---

## Non-Functional Requirements

---

### Product Experience Philosophy

NC's interaction register is **warm, quiet, and non-intrusive**. Every design decision — overlay placement, copy tone, prediction confidence display, correction flow — must be consistent with the following principles, which UX designers must treat as binding:

- **NC is a knowing friend, not a clinical tool.** It surfaces insight without judgment. It never implies the user is wrong to feel what they feel — only that there may be more to the story.
- **NC earns trust by admitting uncertainty.** A high-ambiguity flag is not a failure state — it is the product behaving with integrity. Designs that hide uncertainty erode trust faster than designs that surface it.
- **NC never interrupts.** The overlay is available — never intrusive. It appears only on incoming messages, never during composition. It can be dismissed in one action. It never blocks.
- **NC is consent-first, transparency-by-design.** The user always knows what NC can see, what it stores, and how to remove it. Privacy is not fine print — it is the product's primary trust signal.
- **NC's language is human-scale, not algorithmic.** Prediction labels and contextual notes must be written in the language a thoughtful friend would use, not the language of a classification system.

These principles are not aspirational — they are testable. UX review at each sprint should include an explicit check: does this design feel like a knowing friend or a surveillance tool?

---

### Performance

- **NFR-P1:** The intent prediction overlay must be visible within **800ms** of message receipt at P95 of production traffic. Measured: message DOM mutation event → overlay render complete. This is a neuroscience-derived hard constraint — beyond 800ms the amygdala threat-tagging response is complete.
- **NFR-P2:** Lightweight prediction (message only): rendered within **200ms** at P95. Soul Document enrichment layer: delivered within **600ms** additional (total ≤ 800ms) at P95. If enrichment exceeds budget: lightweight prediction displayed; enriched update suppressed.
- **NFR-P3:** Browser extension must reach operational state within **1 second** of browser startup on Chrome 102+.
- **NFR-P4:** Mobile app must display first interactive screen within **2 seconds** of launch on minimum supported device (mid-range Android API 26; mid-range iPhone iOS 15).
- **NFR-P5:** All Soul Document read, write, and edit operations must complete within **500ms** including AES-256 encryption/decryption on the mobile app.
- **NFR-P6:** All mobile features designated as offline-capable (FR16–FR24, FR35–FR38) must maintain identical performance characteristics online and offline — no network round-trip introduced into offline flows.

---

### Security & Privacy

- **NFR-S1:** Soul Document database file encrypted at rest with AES-256. Encryption key stored exclusively in platform secure storage (iOS Keychain / Android Keystore). Key never written to disk unencrypted, logged, or transmitted to NC servers. Verified by security audit before launch.
- **NFR-S2:** Message text extracted by the content script must not persist beyond the inference call lifecycle. No message content written to extension local storage, logged server-side, or retained in any memory structure after prediction is returned.
- **NFR-S3:** All inference payloads transmitted over HTTPS with TLS 1.3 minimum. Certificate pinning applied to the NC inference API endpoint in the extension.
- **NFR-S4:** No API endpoint, data structure, or user flow may expose one user's Soul Document to another user's session. Verified by threat model review at each major feature addition. Architectural enforcement — not policy-only.
- **NFR-S5:** Biometric / PIN gate on Soul Document uses platform-native authentication APIs exclusively (iOS `LocalAuthentication`, Android `BiometricPrompt`). Gate re-challenges after app is backgrounded for > 60 seconds.
- **NFR-S6:** Soul Document fields limited to those with demonstrated intent prediction contribution via ablation study. Fields with no measurable accuracy contribution must be removed. New fields added only after ablation validation confirms prediction contribution.
- **NFR-S7:** User-initiated deletion removes all NC data (Soul Document, correction history, reflection journal, per-sender calibration, extension local storage) within **10 seconds**, confirmed to user with timestamp. No residual data retained on NC servers.
- **NFR-S8:** The I8 safeguarding signpost trigger event must not be logged to NC servers or linked to any user identifier. Detection is client-side only.
- **NFR-S9:** LLM inference provider must operate under a signed DPA with explicit zero data retention for inference inputs, including audit rights. Violation is a GDPR breach and a product launch blocker.

---

### Reliability & Resilience

- **NFR-R1:** NC must never prevent a user from reading or responding to messages. Any NC component failure (inference API timeout, service worker inactive, overlay render error) results in NC becoming invisible — not blocking.
- **NFR-R2:** NC inference API must maintain **99.5% uptime** during active hours (06:00–24:00 UK time) once the product reaches 100+ daily active users.
- **NFR-R3:** Each inference request must be stateless — fully self-contained with all required context in the request payload. Service worker restart mid-flow must not drop the prediction.
- **NFR-R4:** Complete network loss must not cause data loss for any Soul Document write operation. Writes committed to encrypted local database before any network sync attempt.
- **NFR-R5:** Chrome extension updates must not interrupt an active inference session. Content script must gracefully restart without displaying an error to the user.

---

### Accessibility

- **NFR-A1:** The intent prediction overlay (extension) and all mobile app screens must conform to **WCAG 2.1 Level AA**. Required under UK Equality Act 2010 for public-facing digital services.
- **NFR-A2:** Confidence display and intent label indicators must communicate meaning via at least two distinct visual channels (e.g., colour + icon, colour + text label). No information conveyed by colour alone.
- **NFR-A3:** Intent prediction overlay must be fully operable via keyboard. Tab order: overlay focus → primary intent label → secondary label → dismiss → flag incorrect. No pointer required.
- **NFR-A4:** All overlay elements must have accessible text alternatives compatible with NVDA/JAWS (Windows) and VoiceOver (macOS). Mobile app: all interactive elements must have programmatic accessible labels and roles. Screen reader compatibility tested on VoiceOver (iOS) and TalkBack (Android) before launch.
- **NFR-A5:** Overlay appearance and animated elements must respect `prefers-reduced-motion`. If set: overlays appear/disappear instantly — no animation or transition.
- **NFR-A6:** Mobile app must support OS-level text size scaling (Dynamic Type iOS / Font Size Android) at all system settings without text truncation or layout breakage.

---

### AI Model Quality

- **NFR-M1:** Intent prediction model must achieve ≥ **75% accuracy** on ambiguous-valence messages (message-only, no Soul Document) on the held-out annotated test set before launch. Launch is blocked below this threshold.
- **NFR-M2:** With Soul Document active, intent prediction accuracy must reach ≥ **85%** on the matched message set used for Soul Document ablation testing.
- **NFR-M3:** Model confidence scores must be calibrated — a prediction displayed at 70% confidence must be correct approximately 70% of the time (±5% tolerance). Expected Calibration Error (ECE) ≤ 0.05 before launch.
- **NFR-M4:** The high-ambiguity flag must trigger when max-category confidence is ≤ 55%. Threshold validated on the test set to confirm correct identification of messages human annotators rated as ambiguous (≥ 40% inter-annotator disagreement).
- **NFR-M5:** After 10 user-submitted corrections for a single sender, per-sender calibration must improve accuracy on that sender's messages by ≥ 5 percentage points relative to uncalibrated baseline.
- **NFR-M6:** The I8 pattern detector must achieve ≥ **70% precision** on the I8 test set before the safeguarding signpost is enabled in production. False positive rate ≤ 15% — a false positive signpost is a user harm event.

---

### Scalability

- **NFR-SC1:** The inference API must support **50 concurrent requests** without latency degradation beyond P95 800ms at MVP launch (~500 daily active users, 10% concurrent session assumption).
- **NFR-SC2:** Inference API infrastructure must be horizontally scalable to **500 concurrent requests** through provisioning changes only — no architectural changes required.
- **NFR-SC3:** Local Soul Document storage model must support Soul Document sizes up to **500KB** without performance degradation at NFR-P5 thresholds, accommodating Soul Document v2 (Growth) without a storage migration.
- **NFR-SC4:** PII-redacted correction log system must handle **10,000 correction events per month** without query degradation. Provides 10x headroom at MVP scale.

---

### Integration

- **NFR-I1:** Content script must function correctly across WhatsApp Web DOM versions released within the past **90 days** at any given point. Automated DOM regression tests run on CI against current WhatsApp Web DOM snapshot.
- **NFR-I2:** NC must pin to a specific LLM inference API version. Provider API version upgrades are explicit — no automatic upgrades. Breaking changes to the inference API must not affect production without a validated NC model update.
- **NFR-I3:** QR-code device pairing (FR34) must complete Soul Document transfer within **30 seconds** on a standard home WiFi connection. Transfer is atomic — either complete or rolled back. Partial transfers must not activate.
- **NFR-I4:** Extension must pass Chrome Web Store automated review checks on every release. Mobile app must pass App Store and Play Store automated validation checks on every release. CI pipeline includes store validation checks before release candidate tagging.

