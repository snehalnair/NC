---
stepsCompleted: [step-01-document-discovery, step-02-source-analysis, step-03-dual-track-assessment]
documentsInventoried:
  prd: null
  architecture: null
  epics: null
  ux: null
  primarySource: "_bmad-output/planning-artifacts/encode-application/encode-application-NC-2026-03-17-v2.3.md"
  supportingDocs:
    - "_bmad-output/planning-artifacts/product-brief-NC-2026-03-14.md"
    - "_bmad-output/planning-artifacts/soul-document-architecture-spec-2026-03-16.md"
    - "_bmad-output/planning-artifacts/research/technical-neuroai-cognitive-companion-research-2026-03-13.md"
    - "_bmad-output/planning-artifacts/research/domain-neuroplasticity-trust-research-2026-03-16.md"
    - "_bmad-output/planning-artifacts/research/domain-reflection-journal-consciousness-research-2026-03-16.md"
---

# Implementation Readiness Assessment Report

**Date:** 2026-03-18
**Project:** NC

---

## Step 1: Document Discovery — Inventory

### Document Status Summary

| Document Type | Status | File |
|---|---|---|
| PRD | ❌ Not created (stub only) | `prd.md` — frontmatter only, no content |
| Architecture | ❌ Not created | None found for application architecture |
| Epics & Stories | ❌ Not created | None found |
| UX Design | ❌ Not created | None found |

### Primary Source Document (for assessment)

- ✅ `encode-application/encode-application-NC-2026-03-17-v2.3.md` — Authoritative latest version (60,761 bytes, Mar 17)

### Supporting / Reference Documents

- `product-brief-NC-2026-03-14.md` — Product brief
- `soul-document-architecture-spec-2026-03-16.md` — Soul document architecture (domain concept, not app architecture)
- `research/technical-neuroai-cognitive-companion-research-2026-03-13.md`
- `research/domain-neuroplasticity-trust-research-2026-03-16.md`
- `research/domain-reflection-journal-consciousness-research-2026-03-16.md`

### Duplicate / Superseded Documents (encode-application folder)

The following are older/superseded versions and will NOT be used in assessment:
- `encode-application-NC-2026-03-15.md` (superseded)
- `encode-application-NC-2026-03-17.md` (superseded)
- `encode-application-NC-2026-03-17-compressed.md` (superseded)
- `encode-application-NC-2026-03-17-v2.2.md` (superseded)

---

## Step 2: Source Analysis — Requirements Extraction

> **Context note:** No traditional PRD, Architecture, Epics or UX documents exist. The primary source is the Encode x Pillar VC AI for Science Fellowship application (v2.3, final submission). This is a research application, not a product spec. Assessment adapted to dual-track approach: (A) Research Track readiness and (B) parallel Product Development track feasibility.

### Key Functional Requirements (from encode-application-v2.3)

**Research Track (FR-R)**

| ID | Requirement | Tier |
|----|------------|------|
| FR-R1 | 2,000-message annotated dataset with dual SI/PI labels, 5 relationship types, κ-validated (κ>0.70) | MUST |
| FR-R2 | Annotation tooling for Prolific-based annotation pipeline | MUST |
| FR-R3 | RoBERTa-large fine-tuned with 16-dim dyadic relational context vector (Conditions A, B, C, D) | MUST |
| FR-R4 | Biographical intake instrument v1 — 8 questions, 3 layers, story tagging | MUST |
| FR-R5 | Study 1b randomised controlled trial (N=100, 2 arms, 4 weeks) for H₄ cold-start ablation | MUST |
| FR-R6 | Intent gap score per message: Jensen-Shannon divergence with Laplace smoothing | MUST |
| FR-R7 | κ pilot (20 messages, 5 annotators) before full annotation | MUST |
| FR-R8 | Open-source release: dataset on HuggingFace + OpenNeuro, model weights + code on HuggingFace (Apache 2.0) | MUST |
| FR-R9 | Paper #1: dataset + model + H₁ result submitted to ACL/EMNLP/CHI | MUST |
| FR-R10 | Online behavioural H₂ probe (N=50, no EEG, Months 2–3) | MUST |
| FR-R11 | Brain-Score Language benchmark submission for neural plausibility | SHOULD |
| FR-R12 | Browser extension research prototype for 60-day EEG pilot (N=20–24 dyads) | SHOULD |
| FR-R13 | EEG hyperscanning protocol: Day 0 and Day 60 sessions, theta-band IBS measurement | SHOULD |

**Product Development Track (FR-P)**

| ID | Requirement | Surface | Status |
|----|------------|---------|--------|
| FR-P1 | Browser extension: inject signal bar into compose area of web messaging apps | Laptop | Implied by research prototype |
| FR-P2 | 5-state gap signal display: Crystal clear / Well understood / Getting lost / Significant misread / Crossed wires | All surfaces | Defined in live demo |
| FR-P3 | Mobile keyboard extension / chat overlay: single signal pill, one colour, plain English, 4s auto-dismiss | Mobile | Shown in live demo |
| FR-P4 | Audio ambient mode: on-device transcription → real-time classification → screen glow by gap state | Audio | Shown in live demo |
| FR-P5 | Biographical intake UI: 8-question structured form, AES-256 encrypted, local-first, biometric/PIN gate | All | Partially defined |
| FR-P6 | Rapid account deletion from first screen, no authentication required | All | Defined (ethics requirement) |
| FR-P7 | Session-disabling 3-tap gesture, clears session silently | All | Defined (ethics requirement) |
| FR-P8 | Domestic abuse safeguarding: signpost to National Domestic Abuse Helpline on sustained divergence + self-interest asymmetry | All | Defined (ethics requirement) |
| FR-P9 | Lock screen / app switcher anonymity: no identifying information visible | All | Defined (ethics requirement) |
| FR-P10 | Extension icon glow when gap detected (even without compose box open) | Laptop | Shown in live demo |
| FR-P11 | Therapist / mediator mode: third screen showing both parties' gap trajectories simultaneously | Audio | Shown in live demo |

### Non-Functional Requirements

| ID | Requirement | Category |
|----|------------|----------|
| NFR1 | All biographical intake data: AES-256 encrypted at rest, device keychain, no cloud sync in MVP | Security |
| NFR2 | Intent gap scores only stored (no raw message content) for logging | Privacy |
| NFR3 | No cross-partner data access permitted at any consent level | Privacy |
| NFR4 | On-device transcription for audio surface — no cloud | Privacy |
| NFR5 | Per-culture κ reported; high cross-cultural-variance categories flagged with wider confidence intervals | Fairness |
| NFR6 | Separate κ computed on neurodiverse annotator subset; model error rates on neurodiverse messages explicitly reported | Fairness |
| NFR7 | Model must be calibrated (ECE as secondary metric alongside macro F1) | Quality |
| NFR8 | Compute budget: covered by Encode fellowship allocation (minimum £100k); annotation budget ~£5,000–7,000 | Budget |
| NFR9 | Ethics/IRB approval required before Study 1b data collection; application Month 1 | Compliance |
| NFR10 | Research browser extension: HCI research prototype standard, researcher-supported, not publicly released | Scope |

### Constraints & Assumptions

- Lab partner not yet confirmed (outreach initiated March 15, 2026); EEG pilot (Study 4) is formally contingent on confirmation by Month 3
- MUST tier (dataset + model + Study 1b + papers) fully executable without lab partner
- Relational context in Study 1 operationalised as controlled metadata, not verbatim interaction history (Year 2 extension)
- RoBERTa-large chosen over GPT-style architectures because task is classification; encoder-only purpose-built and has established Brain-Score baseline
- Study 1 scale (2,000 messages) appropriate for relative ablation test; absolute scale question deferred to Year 2
- H₄ primary metric is researcher-labelled held-out set (not user self-annotations, which are tertiary engagement metric only)

---

## Step 3: Dual-Track Implementation Readiness Assessment

### TRACK A — Research Track Readiness

#### Overall Verdict: 🟡 CONDITIONALLY READY

The research plan is unusually well-specified for a pre-execution stage. Scientific hypotheses are formal, pre-registered, and falsifiable. Methods are appropriate. Risks are identified with mitigations. The MUST tier is executable independently of lab partner. Key gaps are operational, not conceptual.

---

#### A1. What is Ready ✅

| Area | Assessment |
|------|-----------|
| Scientific hypotheses (H₁–H₄) | Formal, pre-registered, falsifiable. Well-powered. Clear null-result protocol. |
| Dataset design | Sampling procedure, label space (I1–I7), annotation protocol, κ gate, inter-rater design — all specified at execution level |
| Model architecture | RoBERTa-large + 16-dim context vector + personality context block — architecture specified, training conditions A/B/C/D defined cleanly |
| Biographical intake instrument | 8 questions, 3 layers, story-tagging approach defined |
| Study 1b design | N=100, 2 arms, primary/secondary/tertiary metrics defined, ANCOVA covariate specified, null result planned for |
| Ethics architecture | Safeguarding features specified; ethics application timeline built into Month 1 |
| Publication targets | ACL, EMNLP, CHI named; arXiv pre-submission planned |
| Open-source release | HuggingFace + OpenNeuro + Apache 2.0 — format and timing specified |
| Reproducibility infrastructure | DVC, HuggingFace Hub, OpenNeuro named |
| Budget | Annotation (~£5–7k Prolific), compute (Encode fellowship allocation) — confirmed |

#### A2. Gaps Requiring Resolution Before Execution 🔴

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| **Lab partner not confirmed** | Study 4 (EEG pilot, H₃) cannot proceed without letter of intent | Continue outreach; confirm by Month 3 or formally defer Study 4 to Year 2 |
| **Annotation tooling not specified** | Month 1 start requires tooling ready on Day 1 | Decide: Prolific native interface vs. custom Label Studio/Argilla deployment. Document the choice. |
| **Recruitment plan for Study 1b (N=100) not specified** | 100 participants needed by Month 3 (post-ethics) | Define channels: Prolific? University participant pools? Community groups? Pre-screen criteria document needed. |
| **16-dim relational context vector schema not fully specified** | Model training (Months 3–6) blocked without complete feature schema | Define all 16 dimensions precisely (the 6 named in the document leave 10 undefined) — needed for dataset metadata schema and model architecture |
| **κ pilot logistics not specified** | First deliverable in Month 1 | Define: Which 20 messages? Which 5 annotators (Prolific screened)? Timeline within Month 1? |

#### A3. Gaps That Are Acceptable / Deferred ⚠️

| Gap | Why Acceptable |
|-----|---------------|
| Brain-Score submission detail | SHOULD tier; 2-week task post-training; does not need pre-specification |
| fMRI / amygdala-TPJ regional analysis | Explicitly Year 2; correctly out of scope |
| Verbatim interaction history as relational context | Explicitly Year 2; controlled metadata for Year 1 is correct scientific choice |
| H₅ (empathic accuracy via soul surface) | Beyond fellowship year; correctly stated as formal research question only |
| Horizon 2 and 3 product vision | Product vision appendix; clearly scoped out of 12-month commitment |

---

### TRACK B — Product Development Track Feasibility

#### Overall Verdict: 🟢 READY TO START (model-agnostic MVP)

There is enough UX definition (visible in the live demo) and enough product intent (in the research application's appendix and safeguarding specs) to begin building the product shell immediately, with a placeholder model that the research model drops into.

---

#### B1. The Model Interface Contract (Critical First Step)

The entire parallel-track strategy depends on defining this interface cleanly before any product code is written:

```typescript
interface IntentPredictor {
  // Core prediction
  predict(
    message: string,
    context: RelationalContext
  ): Promise<IntentDistribution>

  // Gap score between sender and receiver distributions
  getGapScore(
    senderDist: IntentDistribution,
    receiverDist: IntentDistribution
  ): number  // Jensen-Shannon divergence, 0–1
}

interface RelationalContext {
  relationshipType: 'romantic' | 'parent_child' | 'close_friend' | 'social_group' | 'professional'
  durationMonths: number
  recentValence: number  // -1 to +1
  messageFrequency?: number
  rollingGapHistory?: number  // 14-day mean gap score
  personalityContext?: PersonalityContextBlock  // from biographical intake
}

type IntentCategory = 'I1' | 'I2' | 'I3' | 'I4' | 'I5' | 'I6' | 'I7'

interface IntentDistribution {
  probabilities: Record<IntentCategory, number>  // sums to 1
  confidence: number  // 1 - normalised entropy
  gapState: 'crystal_clear' | 'well_understood' | 'getting_lost' | 'significant_misread' | 'crossed_wires'
}
```

**Placeholder implementation:** Map existing RoBERTa-base sentiment → I1–I7 heuristic mapping. Pre-computed distributions (as in the live demo) can serve as fallback. Full model drops in behind same interface.

#### B2. What Can Be Built Now (Model-Agnostic) ✅

**Priority 1 — Browser Extension (Laptop Surface)**

This is the highest-value starting point. It is:
- Required for the research prototype anyway
- Buildable in 2–3 weeks to research-prototype quality
- Tests the core UX hypothesis in real conditions

Scope:
- Detects active compose area in target apps (Slack, WhatsApp Web, Gmail, iMessage web)
- Captures text-in-progress (debounced, e.g. 800ms after typing stops)
- Calls placeholder `IntentPredictor` locally
- Injects signal bar between text field and send button
- Signal bar shows gap state colour + plain English label
- Extension icon glows when gap detected even without compose open
- All storage local, AES-256 encrypted
- Safeguarding features from Day 1 (ethics requirement, not optional)

**Priority 2 — Biographical Intake UI**

Completely model-independent. Pure UX/data capture:
- 8-question structured flow (identity values → decision architecture → narrative stories)
- Estimated 10–15 minute guided experience
- Local-first storage: AES-256, biometric/PIN gate
- Rapid deletion from first screen
- Export as structured JSON for model inference injection
- Can be built as a standalone web app (served locally) or native

**Priority 3 — Mobile Signal Overlay**

Two implementation options:
- **iOS Keyboard Extension:** Shows pill above keyboard in any app. Higher friction to build + distribute (requires App Store review or TestFlight). Best long-term.
- **iOS Share Extension / iMessage App Extension:** Lower friction to distribute. User manually invokes before sending. Less seamless but faster to ship.

Recommendation: **Start with iOS iMessage App Extension** for research prototype (faster), plan Keyboard Extension for public product.

**Priority 4 — Audio Ambient Mode**

Most technically novel surface. On-device transcription (Whisper.cpp or Apple Speech Recognition framework) feeding real-time classification. The ambient screen glow is achievable as:
- iOS app in foreground running Whisper locally
- Classification result drives screen colour overlay (full-screen or edge-glow)
- Haptic band: Apple Watch haptic feedback (WatchKit) as wearable signal

#### B3. Suggested Architecture for Parallel Tracks

```
┌─────────────────────────────────────────────────────────┐
│                    Shared Model Layer                    │
│                                                         │
│  IntentPredictor interface                              │
│  ├── PlaceholderPredictor (now)                        │
│  │   └── Sentiment → I1-I7 heuristic mapping           │
│  └── ResearchModelPredictor (Month 6+)                 │
│      └── RoBERTa-large fine-tuned v1                   │
└────────────────────┬────────────────────────────────────┘
                     │
        ┌────────────┼────────────┐
        ▼            ▼            ▼
  Browser Ext    Mobile App   Audio App
  (Laptop)       (iOS/Android) (Ambient)
```

All surfaces share:
- Same `IntentPredictor` interface
- Same gap state vocabulary (5 states, colours, plain English labels)
- Same biographical intake data schema
- Same local encrypted storage layer
- Same safeguarding feature set

#### B4. What's Missing for Product Development 🔴

| Gap | Impact | Recommendation |
|-----|--------|----------------|
| **No PRD for product** | No formal requirements document for product features, user journeys, or acceptance criteria | Create a lightweight product PRD (the research application appendix is a start — needs formalising) |
| **No UX design spec** | The live demo shows intent but no wireframes, user flows, edge case handling, or onboarding UX | Create UX spec covering: onboarding, intake flow, signal states, safeguarding flows, settings/deletion |
| **No architecture doc for product** | No decisions on tech stack, data model, extension architecture, or native vs. web approach | Create architecture doc before coding begins |
| **No epics / stories** | No breakdown of product work into implementable units | Create epics (at minimum) to organise parallel track work |
| **Mobile platform decision not made** | iOS first? Android? Both? PWA first? | Decide based on research cohort's device distribution |
| **Target messaging apps not prioritised** | Browser extension needs a target app list (can't inject into everything Day 1) | Define: Slack first? WhatsApp Web? Gmail? |
| **Relational context UI not designed** | How does user set relationship type, duration, valence for each contact? | This is a key UX challenge — the model needs context to work |

---

### TRACK B5 — UX Observations from Live Demo + Alternative Suggestions

**What the live demo gets right:**
- The 5-state vocabulary (Crystal clear → Crossed wires) with colour coding is elegant and immediately legible
- "No numbers. One colour. Plain English" — correct for non-clinical users
- The ambient audio surface (glowing orb) is genuinely novel and beautiful
- Therapist/mediator mode (both gap trajectories visible) is a strong differentiator
- Safety architecture built-in from the start is the right approach

**Suggestions and alternatives:**

1. **Smartwatch as primary audio signal surface (instead of phone face-up)**
   The current audio design has the phone lying face-up between two people, which creates a "there's a device in the room" social signal that may disrupt the very conversation it's meant to help. An Apple Watch subtle colour shift on the watch face (or gentle haptic pattern) is far less intrusive for face-to-face conversations. Keeps the signal private without the device presence.

2. **Consider a "Pre-send" model rather than "In-compose" model for mobile**
   Currently the pill appears as you type. An alternative: the signal only appears when you long-press the send button (or hover over it). This feels more intentional — you're explicitly checking before sending, rather than being monitored while composing. Less likely to cause anxiety or performance pressure during writing.

3. **Notification / Focus Mode integration for laptop**
   Rather than only injecting into compose areas, the browser extension could use the browser notification API to surface a gap score retrospectively — "The message you sent 2 minutes ago may have landed as frustration" — if the received reply shows a high gap. This turns the tool from pre-send only into a repair-moment instrument.

4. **Onboarding without biographical intake (cold start)**
   The current design implies biographical intake from Day 1. But user adoption requires a zero-friction path: let users start with zero context (relationship type only), accumulate value, then offer intake as an "upgrade." This also makes H₄ testing more ecologically valid — real cold-start conditions.

5. **Progressive disclosure of the signal vocabulary**
   Don't show all 5 states to a new user immediately. Start with binary: "Your message aligns / may not land as intended." Introduce the full 5-state vocabulary after 7 days. Reduces cognitive load during onboarding, surfaces complexity only when users have built intuition.

---

## Summary: Implementation Readiness Scorecard

### Research Track

| Dimension | Score | Notes |
|-----------|-------|-------|
| Scientific rigour | 🟢 High | Hypotheses formal, pre-registered, falsifiable |
| Dataset design | 🟢 Ready | Sampling, labels, annotation protocol all specified |
| Model architecture | 🟢 Ready | Architecture and ablation conditions fully defined |
| Execution planning | 🟡 Partial | Month-by-month plan exists; 3 operational gaps need closing |
| Risk management | 🟢 Strong | Risks identified with mitigations; null-result protocol planned |
| Lab partner | 🔴 Unconfirmed | Critical for SHOULD tier; outreach in progress |
| Ethics/IRB | 🟡 Pending | Application planned Month 1; approval timeline risk |

**Research Track Verdict:** Begin Month 1 immediately. Close the 5 operational gaps (tooling, recruitment plan, 16-dim schema, κ pilot logistics, lab partner confirmation) in parallel.

### Product Development Track

| Dimension | Score | Notes |
|-----------|-------|-------|
| UX intent | 🟢 Strong | Live demo shows clear, well-conceived UX across 3 surfaces |
| Safety architecture | 🟢 Defined | Safeguarding features specified in research doc + demo |
| Signal vocabulary | 🟢 Ready | 5-state system, colours, plain English — build to this spec |
| Model interface | 🟡 Needs formalising | Implicit in the research design; needs explicit contract |
| PRD | 🔴 Missing | No product requirements document |
| Architecture | 🔴 Missing | No tech stack decisions, data model, or extension architecture |
| Epics / Stories | 🔴 Missing | No breakdown of product work |
| UX design spec | 🔴 Missing | Live demo shows intent but no wireframes, flows, or edge cases |

**Product Track Verdict:** Create PRD and architecture doc before coding. Browser extension + biographical intake UI can start once those exist. The model interface contract should be the very first code written.

---

### Recommended Next Steps (Prioritised)

**Immediate (this week):**
1. Define the 16-dimensional relational context vector schema completely
2. Write the `IntentPredictor` model interface contract
3. Decide annotation tooling (Label Studio vs. Prolific native vs. Argilla)
4. Define Study 1b recruitment channels and pre-screening criteria

**Short-term (next 2 weeks):**
5. Create lightweight product PRD (can build on the appendix in encode-application v2.3)
6. Create product architecture decision record (tech stack, extension architecture, mobile approach)
7. Define target messaging app list for browser extension MVP
8. Begin browser extension scaffold — detection logic, local storage, placeholder model

**Before Month 3:**
9. Confirm lab partner (letter of intent)
10. Create UX design spec (onboarding, intake flow, signal states, safeguarding flows)
11. File ethics/IRB application jointly with lab partner
12. Pre-screen Study 1b cohort (100 participants, 2 arms)
