# Soul Document Architecture Specification
**NC — NeuroAI Cognitive Companion**
*Digital Twin / Personality Fingerprint Layer*
**Version:** 0.3 — Relationship Context Addition
**Date:** 2026-03-19
**Author:** Snnair
**Status:** Updated — Adds per-person Relationship Context (1-to-many mapping)

---

## Change Log: v0.1 → v0.2 → v0.3

| Version | Fix | Change Made |
|---------|-----|-------------|
| v0.2 | Scope | Primary scope is now Soul v1 (3 layers, fellowship year). Full 6-layer schema moved to Appendix A as north-star vision. |
| v0.2 | Mode B | Reframed as channel pilot contingent on professional partner — not a Year-1 dependency. |
| v0.2 | Story tagging | Explicit note added: v1 stories are manually tagged by researcher/RA. Automated tagging is a v2 problem. |
| v0.2 | Router spec | Rule-based query classification specified for v1 — no classifier required. |
| v0.2 | Study precision | Intent prediction accuracy defined precisely. Engagement covariate noted. |
| v0.2 | Governance | New standalone section: Soul v1 Data Governance Constraints. Partner access explicitly prohibited in v1. |
| v0.2 | Study framing | "Foundation for everything" reframed as first empirical test — honest about null results. |
| v0.2 | Ablation-first | Explicit principle added: features not improving H1/H2 get removed. |
| **v0.3** | **Relationship Context** | **New Section 5b: Per-person Relationship Context data structure. Soul Document is base layer (who you are); Relationship Contexts are companion structures (how you communicate with each specific person). Schema, lifecycle, injection architecture, and governance specified.** |

---

## 1. Executive Summary

The Soul Document is NC's **portable, structured, model-agnostic personality representation** — a layered document that encodes an individual's identity, decision architecture, and narrative history. It is injected at inference time into NC's foundation model to condition intent prediction on *who the person actually is*, not just what they wrote.

It is **not** a fine-tuned model. It is a **structured retrieval corpus** injected at inference time into any capable base LLM — model-agnostic, forward-compatible, and richer with every correction. Think of it as the difference between tattooing personality onto a model (fine-tuning) versus handing any model a richly annotated biography (Soul Document + RAG).

**Soul v1 Design Principle:**
> *Prove that any structured personal context beats no context for cold-start intent prediction. Nothing more. Nothing less.*

**This document specifies:**
- Soul v1 schema (3 layers — fellowship year scope)
- Soul v1 intake pipeline (two modes, one contingent)
- Soul v1 inference-time injection (rule-based router + prompt adapter)
- **Relationship Context: per-person communication modelling (1-to-many mapping)**
- Soul v1 study design (one Cold Start A/B test)
- Soul v1 data governance constraints (local-first, no partner access)
- Soul vFull north-star architecture (Appendix A — 3-5 year vision)

---

## 2. The Problem This Solves Within NC

NC's current architecture conditions intent prediction on `P(intent | message, relational_history, context)`. This is powerful — but it models *communication patterns*, not *the person behind them*.

Two people can have identical message histories and entirely different intent architectures:
- Same words, different risk tolerance
- Same silence, different conflict response pattern
- Same "I'm fine", different suppression style

Without a personality layer, NC is doing **relational pattern matching**. With a Soul Document, NC does **person-aware intent modelling** — the same distinction as knowing someone's message history vs. genuinely knowing them.

**The cold start problem alone justifies this:** new users have no message history. A Soul Document built from a structured biographical intake gives NC immediate, rich grounding — Day 1 accuracy that would otherwise take months of usage data to achieve.

---

## 3. Soul v1 — Fellowship Year Scope

### 3.1 The 3-Layer Schema

**Ablation-First Principle:**
Every field in the Soul v1 schema must earn its place. The v1 study (Section 6) is explicitly designed to measure which subsets of the Soul Document improve intent prediction accuracy. Any layer or field that does not measurably contribute to H1 or H2 will be removed before v2. The default position is *less is more* — we add complexity only when evidence demands it.

---

#### Layer 1: Identity Core
*Static anchor — always injected. Changes only at decade-scale life events.*

```yaml
identity_core:
  version: "1.0"
  last_updated: "2026-03-17"

  # Core values — ranked, not listed
  # Rank order matters: tells NC how this person resolves value conflicts
  values_ranked:
    - rank: 1
      value: "intellectual honesty"
      over: "social harmony"
      evidence: "will correct factual errors in public even at social cost"
    - rank: 2
      value: "long-term relationship depth"
      over: "social breadth"
      evidence: "maintains 3-5 close relationships over decades, not wide network"

  # Non-negotiables — max 3, things they will not compromise on
  non_negotiables:
    - "Will not take credit for others' work"
    - "Will not stay silent when witnessing injustice in their presence"

  # Self-concept — how they describe themselves unprompted
  self_concept:
    - "Someone who finishes what they start, even when it gets hard"
    - "Deeply introverted who performs extroversion well — and pays a cost for it"

  # Known paradoxes — where self-concept is internally contradictory
  paradoxes:
    - "Craves deep connection but retreats when it gets too close"
    - "Believes in fairness as a principle but is highly competitive in practice"
```

**Intent modelling use:** When a message could be read as a challenge or an inquiry, the Identity Core tells NC: does this person default to defence or curiosity? The ranked values answer that immediately, without requiring message history.

**Population method:** Self-report via guided interview. Consumer Mode A: 3 questions (10 min). Mode B: full Phase 1 interview (15 min). NC extracts and structures YAML automatically from conversational responses; user reviews and edits before activation.

---

#### Layer 2: Decision Architecture (Lite)
*Injected conditionally — when conflict, choice, or ambiguity markers detected in query.*

```yaml
decision_architecture_lite:
  version: "1.0"

  # Risk profile — by domain (conservative / moderate / high)
  risk_profile:
    social: high          # Will say the uncomfortable thing in the room
    professional: moderate  # Takes calculated career risks, not impulsive ones
    emotional: conservative # Cautious with vulnerability

  # Dominant heuristic — one primary decision rule
  dominant_heuristic: "Would I be proud to tell someone I respect about this decision?"

  # Stress response pattern — most important signal for intent prediction
  stress_response:
    pattern: "withdraws and processes alone before re-engaging"
    communication_signal: "response latency increases, messages shorten, tone formalises"
    misread_risk: "withdrawal often interpreted as disengagement or coldness — it is neither"

  # Conflict response
  conflict_response:
    default: "withdraws initially, processes alone, re-engages with reasoned position"
    when_values_violated: "direct and firm, will not defer regardless of social cost"
```

**Intent modelling use:** Shorter messages + delayed replies become interpretable as stress response, not disengagement. NC stops misreading withdrawal as rejection. Conflict queries route to this layer automatically.

**Population method:** Self-report via 3 guided interview questions (Phase 2 protocol). No clinical inference — these are self-reported patterns, not diagnostic classifications.

---

#### Layer 3: Narrative Library
*RAG-retrieved on demand — 5-7 stories minimum for v1 study cohort.*

```yaml
narrative_library:
  version: "1.0"

  # v1 note: Story themes and retrieval tags are MANUALLY ANNOTATED
  # by the researcher/RA in the study cohort. Automated NLP tagging
  # is a v2 problem. v1 intentionally tests whether manually-tagged
  # stories improve intent prediction — automated extraction is
  # a separate, later hypothesis.

  stories:

    - id: "story_001"
      era: "adolescence"
      age_approximate: 16
      title: "The Science Fair Exclusion"
      raw_narrative: >
        "I worked for three months on a project that I knew was better
        than anything else submitted. I was excluded from the final
        presentation because the teacher thought I was 'too difficult to
        manage in public.' I said nothing. I went home and never entered
        another school competition."
      themes: ["injustice", "institutional_authority", "silence_as_strategy"]
      emotion_at_time: ["humiliation", "rage", "determination"]
      lesson_extracted: "Institutions protect themselves, not merit. Work around them."
      decision_pattern_revealed: "Avoids systems he can't control; builds independent paths"

    - id: "story_002"
      era: "early_adult"
      age_approximate: 24
      title: "The Partnership That Didn't"
      raw_narrative: >
        "My co-founder and I had different risk tolerances. I wanted to
        move faster; he needed more certainty. We let the decision sit
        for eight months until the window closed. Neither of us was wrong.
        We were just incompatible at a fundamental level we'd never named."
      themes: ["collaboration", "risk", "timing", "compatibility", "unsaid_things"]
      emotion_at_time: ["frustration", "loss", "eventual_acceptance"]
      lesson_extracted: "Name the incompatibility early or pay for it with time."
      decision_pattern_revealed: "Names incompatibilities quickly now, even at social cost"

    - id: "story_003"
      era: "mid_adult"
      age_approximate: 35
      title: "The Conversation That Changed Everything"
      raw_narrative: >
        "My father called me unexpectedly and said, 'I don't think I was
        a good enough father to you.' That was all. I didn't know what
        to do with it for two years. Then I realised he gave me the only
        gift that mattered — he told the truth."
      themes: ["parental_relationship", "truth", "repair", "time"]
      emotion_at_time: ["shock", "grief", "eventually_gratitude"]
      lesson_extracted: "Truth arrives on its own timeline. Receive it when it comes."
      decision_pattern_revealed: "Values truth-telling over comfort; gives others time to arrive at truth"

  # Story retrieval index — manually annotated in v1
  retrieval_tags:
    authority_conflict: ["story_001"]
    partnership_risk: ["story_002"]
    trust_repair: ["story_003"]
    truth_telling: ["story_001", "story_003"]
    timing_decisions: ["story_002"]
    injustice: ["story_001"]
```

**Intent modelling use:** When a query involves conflict with authority, `story_001` is retrieved and used as grounding. NC doesn't just know this person avoids institutions — it knows *the specific experience that made that true*.

**Population method:** 15-minute guided narrative interview (Phase 3 protocol). Themes and retrieval tags are manually assigned by researcher/RA in the v1 study cohort. Users in consumer Mode A receive a guided prompting UI that extracts stories conversationally.

**v1 study note:** The v1 evaluation explicitly tests whether manually-tagged story retrieval improves intent prediction accuracy over Layer 1+2 alone. This is an ablation question — not an assumption.

---

### 3.2 What Soul v1 Deliberately Excludes

| Excluded Feature | Why Excluded | When Reconsidered |
|-----------------|-------------|------------------|
| Emotional Signature Layer (Layer 3 of vFull) | Requires clinical framing to interpret safely; pseudo-diagnostic without clinician | Soul v2 — after v1 ablation results |
| Communication Style Map (Layer 4 of vFull) | Useful but not essential for H1/H2; adds intake burden | Soul v2 |
| Temporal Snapshot Stack (Layer 5 of vFull) | Non-trivial infrastructure; unproven incremental value | Soul v3 |
| Passive digital harvest (music, calendar, search) | Consent/trust risk too high for consumer context | Ethics-gated; never without explicit opt-in |
| Attachment style classification | Pseudo-diagnostic without clinical training; cannot be reliably inferred from 30-min interview | Never without clinical channel |
| Partner read access to Soul Document | Safety risk; power dynamics make "mutual consent" unreliable | Requires ethics board approval; out of scope for fellowship year |
| Adversarial correction loop | Valuable but not core to cold-start validation | Soul v2 |
| Humour architecture | Interesting signal; not essential for v1 hypothesis | Soul v2+ |
| Relationship Mirror / dyadic comparison | High safety risk; requires clinical mediation | Ethics-gated; never without IRB approval |

**All Soul v1 data is local-first, encrypted at rest (AES-256), not shareable with partners or third parties, and fully deletable. Clinical and partner-facing features are explicitly out of scope for the fellowship year.**

---

## 4. Soul v1 Intake Pipeline

### Mode A: Consumer Intake (10-15 minutes)
*Standard onboarding for all NC users*

A guided conversational UI — not a form, not a clinical survey. NC asks 8 questions across the 3 layers and extracts YAML automatically. The user reviews and edits the structured output before activation.

**8 Core Questions:**

```
Layer 1 — Identity Core (3 questions, ~5 min)
Q1: "What's something you believe that most people you know disagree with?"
    → Extracts: values, paradoxes, self-concept

Q2: "What's a line you've never crossed, even when it would have made things easier?"
    → Extracts: non_negotiables

Q3: "How would someone who knows you very well describe you — including the parts
    you find hard to admit?"
    → Extracts: self_concept, paradoxes

Layer 2 — Decision Architecture Lite (2 questions, ~5 min)
Q4: "When you're genuinely upset with someone close to you, what does your
    behaviour look like from the outside?"
    → Extracts: stress_response, conflict_response

Q5: "What's a rule you apply to almost every difficult decision you make?"
    → Extracts: dominant_heuristic, risk_profile

Layer 3 — Narrative Library (3 questions, ~5 min)
Q6: "Tell me about a time you made a decision that still feels right, even though
    it cost you something."
    → Extracts: story (themes: values_over_comfort, decision_pattern)

Q7: "Describe a relationship — work, personal, or family — that taught you something
    fundamental about how you operate."
    → Extracts: story (themes: relational_pattern, lesson_extracted)

Q8: "What's an experience that changed how you think about conflict or repair?"
    → Extracts: story (themes: conflict_response, repair_pattern)
```

**Output:** 3-layer Soul Document with confidence flags per field. Low-confidence fields are surfaced to the user for manual correction before activation. Minimum viable document: Layer 1 + Layer 2 populated; Layer 3 requires at least 2 usable stories.

---

### Mode B: Therapist/Coach Channel (30 minutes)
*Optional deep-intake mode — contingent on professional partner*

**⚠️ Fellowship Year Constraint:** Mode B is a channel pilot, not a Year-1 dependency. It will be developed only if a professional partner (therapist practice, coaching platform, or clinical pilot site) is secured during the fellowship year. Mode B is not on the critical path for Study 1.

If a partner is secured, Mode B uses the full 4-phase biographical interview protocol:

```
Phase 1: Formation (5 min)       → Layer 1: Identity Core (rich version)
Phase 2: Decision Architecture   → Layer 2: Decision Architecture Lite
         (10 min)
Phase 3: Relational Patterns     → Layer 3: Narrative Library (5-10 stories)
         (10 min)
Phase 4: Temporal Anchor (5 min) → Future: Layer 6 seed (north-star only)
```

The clinician helps the user articulate stories they may not have surfaced on their own — particularly for conflict, trust repair, and relational patterns that Mode A's conversational UI may not reach.

**Mode B advantage:** Richer narrative library (5-10 stories vs. 2-3 from Mode A). Higher confidence scores on all layers. Reduced risk of idealised self-report through clinician probing.

---

## 5. Inference-Time Injection Architecture

### 5.1 The Soul-to-Prompt Adapter

Before any query is processed, the Soul Document must be translated into a compact, robust system prompt. This is the **Soul-to-Prompt Adapter** — a lightweight formatting layer that takes structured YAML and produces a grounded context block.

**v1 Adapter Output Format:**

```
PERSON CONTEXT — [User Name]

IDENTITY:
You are reasoning about someone who holds these values in this order:
1. [value_1] over [value_1_over] — [value_1_evidence]
2. [value_2] over [value_2_over] — [value_2_evidence]
They will not: [non_negotiables, comma-separated]
They see themselves as: [self_concept]
Note paradox: [paradox_1]

DECISION PATTERN:
Under stress, this person: [stress_response.pattern]
Communication signal: [stress_response.communication_signal]
IMPORTANT: [stress_response.misread_risk]
When values are violated: [conflict_response.when_values_violated]

RELEVANT EXPERIENCE:
[Retrieved story raw_narrative]
What this revealed: [decision_pattern_revealed]
```

The adapter produces a context block of approximately 600-900 tokens — compact enough for any 8K+ context window alongside the active conversation.

---

### 5.2 The Query Router (Rule-Based, v1)

For v1, query classification is **rule-based** — no classifier required. The router uses a keyword heuristic list to decide which layers to inject:

```
ALWAYS INJECT:
└── Identity Core (via Soul-to-Prompt Adapter)
    Tokens: ~300 | Trigger: every query

INJECT WHEN conflict/decision markers detected:
└── Decision Architecture Lite
    Trigger keywords: "why did", "what should", "I don't understand why",
                      "upset", "angry", "silent", "pulling away", "conflict",
                      "decide", "choose", "should I", "what do you think"
    Tokens: ~250

RETRIEVE AND INJECT (semantic similarity, top 2 stories):
└── Narrative Library (RAG retrieval)
    Trigger: any query involving a theme present in retrieval_tags
    Retrieval method: keyword overlap with retrieval_tags in v1
                      (embedding-based retrieval considered for v2)
    Tokens: ~400-600 per story, max 2 stories injected
```

**v1 router note:** Keyword heuristics are a deliberate simplicity choice for the fellowship year. They are fast, auditable, and sufficient to test the core hypothesis. A lightweight classifier (e.g., fine-tuned BERT for intent query type) is a v2 upgrade, pending evidence that the heuristic approach is the bottleneck.

---

### 5.3 Token Budget (v1)

```yaml
token_budget_v1:
  total_context_window: 8192    # conservative baseline
  allocation:
    identity_core_prompt: 300   # always
    active_conversation: 2000   # always
    narrative_retrieval: 1000   # top 2 stories (conditional)
    decision_architecture: 250  # conditional
    response_reserve: 1500      # output generation
    buffer: 3142                # remaining headroom
```

---

## 5b. Relationship Context — Per-Person Communication Modelling

### The Problem: People Communicate Differently With Different People

The Soul Document captures WHO the user is — their stable identity, values, stress patterns. But communication is relational: the same person may be direct with their best friend, careful with their partner, formal with their manager, and guarded with their co-parent. A single personality model cannot capture these relationship-specific patterns.

**Architectural principle:** The Soul Document is a base layer (stable identity). Relationship Contexts are companion data structures (dyad-specific communication patterns) that accumulate per person the user communicates with.

### 5b.1 Relationship Context Schema

```yaml
relationship_contexts:
  - person_label: "Dev"               # User-assigned label (not real name required)
    relationship_type: "partner"       # partner | family | friend | colleague | co-parent
    created: "2026-04-01"

    # Seeded from initial 3-question intake on first mention
    communication_dynamic: "Direct but emotionally avoidant under stress"

    # Learned progressively from conversations with NC about this person
    learned_patterns:
      - pattern: "Short replies usually = tiredness, not anger"
        confidence: 0.8
        source: "user_correction"      # user_correction | inferred | intake
        first_observed: "2026-04-03"
      - pattern: "Uses sarcasm when feeling unheard"
        confidence: 0.6
        source: "inferred"
        first_observed: "2026-04-10"

    # User-reported or NC-inferred triggers for this specific relationship
    known_triggers:
      - "Feeling controlled about schedule"
      - "Being compared to ex-partner"

    # Misread correction history — NC tracks what the user initially thought
    # vs what was actually meant, building a per-person calibration signal
    misread_history:
      - user_interpretation: "angry"
        actual: "tired"
        count: 3
      - user_interpretation: "dismissive"
        actual: "overwhelmed"
        count: 2

    last_updated: "2026-04-15"
```

### 5b.2 Lifecycle

| State | Trigger | Behaviour |
|---|---|---|
| **Not yet created** | User first asks NC about a message from a new person | NC asks 3 seed questions: (1) Who is this person to you? (2) What's the communication dynamic? (3) Any recurring misread patterns? |
| **Seeded** | User answers seed questions | Relationship Context created with `communication_dynamic` and initial `known_triggers` |
| **Accumulating** | Each subsequent conversation about this person | NC infers patterns from corrections and queries; adds to `learned_patterns` and `misread_history` |
| **Reviewable** | User asks "What do you know about my relationship with [person]?" | NC shows full Relationship Context summary; user can edit or delete any entry |
| **Deleted** | User deletes a specific Relationship Context | All data for that person removed; Soul Document unaffected |

### 5b.3 Inference-Time Injection

When the user queries NC about a message from a specific person, the Soul-to-Prompt Adapter injects BOTH the Soul Document context AND the active Relationship Context:

```
PERSON CONTEXT — [User Name]
[... Soul Document context as per Section 5.1 ...]

RELATIONSHIP CONTEXT — [Person Label]
Relationship type: [type]
Communication dynamic: [dynamic]
Known patterns:
- [pattern_1]
- [pattern_2]
Known triggers: [triggers]
Previous misreads with this person:
- You thought [interpretation_1] but it was actually [actual_1] (happened [count] times)
```

**Token budget impact:** Each Relationship Context adds ~150-300 tokens. With the v1 token budget (Section 5.3), 1-2 Relationship Contexts can be injected alongside the Soul Document without exceeding the 8K context window. For users with many relationships modelled, only the active person's context is injected.

### 5b.4 Data Governance

Relationship Contexts inherit ALL data governance constraints from Section 7:
- Stored locally, AES-256 encrypted, same keychain gating as Soul Document
- No partner access — the user's Relationship Context about their partner is never visible to the partner
- Fully deletable per-person or in bulk
- Transmitted to server only under the same per-session consent gate as the Soul Document
- Not used for model training

**Additional constraint:** Relationship Context labels are user-assigned and may not correspond to real names. NC never attempts to verify, cross-reference, or de-anonymise person labels.

---

## 6. Study 1: Cold Start Validation (Fellowship Year)

*Is this the first empirical test of whether structured personal context improves NC's cold-start intent prediction, and it will inform whether and how we invest in deeper Soul layers.*

### Design

```
Study type:  Randomised controlled trial
N:           100 new NC users (50 per arm)
Duration:    4 weeks
Assignment:  Random allocation at sign-up
             (1:1, stratified by age and relationship status)

Group A:     Standard NC onboarding
             No Soul Document. Intent prediction builds from message history only.

Group B:     NC + Soul v1
             10-15 min Mode A intake at Day 1. Soul Document active from first session.
```

### Primary Metric: Intent Prediction Accuracy

**Precise definition:**

Intent prediction accuracy is measured against **sender self-annotation** — the gold standard for what the sender intended. Protocol:

```
1. Users in both groups are prompted (2x per week) to review 3 of their
   recent outgoing messages that NC flagged as "potentially ambiguous"
2. For each message, the sender answers:
   "What did you actually mean when you sent this?" (free text)
   "On a 1-5 scale, how well did NC's interpretation match your intent?"
3. NC's interpretation is extracted from the conversation log
4. Accuracy = mean rating across all annotated messages, per user, per week
```

This approach uses the sender as ground truth — the person who sent the message is the only reliable arbiter of what they intended. It is more feasible than third-party raters and more valid than receiver-report for measuring *sender intent accuracy*.

### Secondary Metric

```
"Feels understood" score: Weekly single-item self-report
"How well does NC understand you on a scale of 1-10?"
Treated as secondary — self-report of relationship quality,
not direct accuracy measurement.
```

### Engagement Covariate

Soul v1 users spend 10-15 minutes on intake — they are already more invested in NC than Group A users at Day 1. This engagement differential may independently improve outcomes, confounding the Soul Document effect.

**Control approach:**
- Track total messages sent, sessions per week, and days active for all users
- Include engagement level as a covariate in the primary analysis (ANCOVA)
- Report both unadjusted and engagement-adjusted accuracy differences
- Conduct a sensitivity analysis: if the Soul Document effect disappears after controlling for engagement, this is a finding, not a failure — it informs the v2 design

### Hypotheses

```
H1 (Primary):   Group B intent prediction accuracy at Week 1 significantly
                exceeds Group A accuracy at Week 1
                (one-tailed t-test, α=0.05, power=0.80)

H2 (Secondary): Group B "feels understood" score at Week 4 significantly
                exceeds Group A score at Week 4

H3 (Ablation):  Within Group B, accuracy improvement is significantly
                correlated with Soul Document layer completeness score
                (tests whether more complete = more accurate)
```

### What We Learn From a Null Result

If H1 is not confirmed, Soul v1 still produces actionable findings:
- If engagement-adjusted effect is null → Soul Document content doesn't improve accuracy; engagement effect is what matters → redesign around engagement
- If Group B improves accuracy but not "feels understood" → accuracy ≠ perceived understanding → reframe the product claim
- If H3 is null → layer completeness doesn't drive accuracy → Layer 2 or Layer 3 may not be needed → Soul v1.1 becomes Layer 1 only

**Timeline and cost:**

```
Recruitment:    Month 1 (100 users via NC waitlist + partner referrals)
Data collection: Month 1-4 (4-week study + 2-week annotation follow-up)
Analysis:       Month 4-5
Publication prep: Month 5-6
Estimated cost: ~£12,000 (recruitment incentives + RA annotation time)
```

---

## 7. Soul v1 Data Governance Constraints

The following constraints apply to Soul v1 and cannot be overridden by user preference or partner request. These are not configuration options — they are design constraints.

**Storage and encryption:**
- All Soul Document data is stored locally on the user's device
- Encrypted at rest using AES-256 with device keychain key management
- Cloud sync is opt-in only and end-to-end encrypted if enabled
- Raw behavioral data (if any) is never retained — only extracted YAML fields

**Access control:**
- Only the owner can read or write their Soul Document
- No partner access — not with mutual consent, not with any consent
- No therapist access — this constraint is lifted only when Mode B is deployed with a formally onboarded clinical partner and ethics board approval
- NC foundation model reads at inference time only — no persistent retention of Soul Document content in model state

**Prohibited uses (v1 — non-negotiable):**
- Third-party sale or licensing
- Training of any external model
- Access by any party other than the owner
- Use without biometric or PIN authentication

**User rights:**
- Full export as YAML at any time
- Full deletion including all snapshots — immediate and irreversible
- Right to review all stored fields and edit any self-reported entry

**Domestic abuse constraint:**
The Soul Document must not become a surveillance instrument. Shared device scenarios require biometric-gated access. This is a safety requirement, not a UX feature.

**IRB classification:**
Soul Document data is classified as sensitive personal data requiring explicit informed consent, purpose limitation, and enhanced security controls. IRB review is required before any research use of Soul Document data from real users.

---

## 8. Soul v1 → v2 → vFull Roadmap

```
SOUL v1 (Fellowship Year — this document)
├── Layer 1: Identity Core
├── Layer 2: Decision Architecture Lite
├── Layer 3: Narrative Library (manually tagged)
├── Intake: Mode A consumer (10-15 min) + Mode B pilot (conditional)
├── Router: Rule-based keyword heuristics
├── Adapter: Soul-to-Prompt (static YAML → context block)
├── Study: Cold Start A/B (H1, H2, H3)
└── Governance: Local-first, no partner access, IRB-gated

SOUL v2 (Post-Fellowship — contingent on v1 evidence)
├── + Layer 4: Emotional Signature (if ablation shows value)
├── + Layer 5: Communication Style Map
├── + Automated NLP story tagging (replaces manual RA annotation)
├── + Adversarial correction loop
├── + Embedding-based story retrieval (replaces keyword heuristics)
├── + Lightweight query classifier
└── Study: Adversarial Refinement Convergence

SOUL vFull (3-5 Year North Star — see Appendix A)
├── All 6 layers
├── Multimodal passive harvest (with explicit opt-in)
├── Temporal snapshot stack
├── Clinical integration (Mode B at scale)
├── Partner features (ethics board required)
└── Full research programme (Studies 2-6)
```

---

## 9. Open Questions (v1 Scope)

| # | Question | Options | Recommendation |
|---|----------|---------|----------------|
| 1 | Minimum stories for RAG effectiveness? | 2 / 5 / 7 | 5 minimum; v1 study will test whether more stories = better accuracy |
| 2 | Should keyword router be expanded or kept minimal? | Minimal list / Expanded list | Minimal for v1; expand based on false-negative analysis in study |
| 3 | How do we handle users who can't recall meaningful stories? | Prompt harder / Accept thin Layer 3 / Offer alternatives | Accept thin Layer 3; flag low-confidence; test whether Layer 1+2 alone is sufficient |
| 4 | What happens to Soul Document on account deletion? | Archive / Full delete / Transfer | Full delete by default; export available before deletion |
| 5 | Should the consumer UI show the generated YAML or abstract it? | Show YAML / Show plain language / Show nothing | Show plain language summary; YAML export available on demand |

---

## 10. Glossary

| Term | Definition |
|------|-----------|
| **Soul Document** | Structured YAML personality representation injected at inference time |
| **Soul v1** | Fellowship-year scope: 3 layers, rule-based router, one study |
| **Soul vFull** | North-star architecture: 6 layers, multimodal, temporal stack, clinical integration |
| **Soul-to-Prompt Adapter** | Formatting layer that converts YAML layers into a structured system prompt |
| **Semantic Layer Router** | System that selects which Soul Document layers to inject per query |
| **Ablation-First Principle** | Only features measurably improving H1/H2 are retained in the schema |
| **Cold Start** | The period before message history is rich enough to ground intent prediction |
| **Personality Sovereignty** | Principle that the user owns, controls, and can delete their Soul Document |
| **Intent Gap** | Delta between sender's intended meaning and receiver's interpreted meaning |
| **Manual Tagging (v1)** | Story themes and retrieval tags assigned by researcher/RA in v1 study cohort |

---

## Appendix A: Soul vFull — North Star Architecture

*This section documents the full 6-layer vision for Soul vFull. It is not in scope for the fellowship year. It is preserved here to inform investors, advisors, and ethics board reviewers of the long-term direction, while making clear that v1 is a disciplined, scoped starting point.*

The full 6-layer schema, intake pipeline (including passive digital harvest), inference architecture, temporal snapshot protocol, and governance model are documented in the v0.1 spec (archived). The key additions beyond Soul v1 are:

**Layer 4: Emotional Signature**
Captures emotional triggers, suppression patterns, energy rhythms, and grief/resilience patterns. Requires clinical framing to interpret safely. Passive signal sources (music, communication timing) feed this layer after consent architecture is established.

**Layer 5: Communication Style Map**
Writing fingerprint, formality drift as emotional signal, family-of-origin communication patterns. Neurodivergent calibration profile.

**Layer 6: Temporal Snapshot Index**
Versioned stack of Soul Document states across time. Divergence scoring between snapshots. Temporal query routing ("what would 2024-me have said?").

**Soul vFull Research Programme (Studies 2-6)**
- Study 2: Amygdala Race Modulation (EEG/fNIRS, N=24)
- Study 3: Relationship Drift Detection (longitudinal, N=200 couples, 18 months)
- Study 4: Neurodivergent Calibration (NT/ND dyads, N=90)
- Study 5: Adversarial Refinement Convergence (N=60, 8 weeks)
- Study 6: Twin-Mediated Repair Protocol (clinical RCT)

*These studies require separate funding, ethics board approval, and clinical infrastructure. They are not bundled with the fellowship year scope.*

---

*This document is version 0.2 of the Soul Document Architecture Specification.*
*It incorporates peer review feedback received 2026-03-17.*
*Next step: Use this spec as input to PRD Step 2 — Project Discovery.*
*Ethics review and IRB consultation required before any study recruitment begins.*
