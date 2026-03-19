---
stepsCompleted: [1, 2, 3, 4, 5, 6]
status: complete
inputDocuments:
  - _bmad-output/brainstorming/brainstorming-session-2026-03-13-1500.md
  - _bmad-output/planning-artifacts/research/technical-neuroai-cognitive-companion-research-2026-03-13.md
date: 2026-03-14
author: Snnair
---

# Product Brief: NC — NeuroAI Cognitive Companion

<!-- Content will be appended sequentially through collaborative workflow steps -->

---

## Executive Summary

Human relationships are breaking — not because people have bad intentions, but because of a 40–80 millisecond biological timing gap. The amygdala fires a threat response to ambiguous messages before the prefrontal cortex processes meaning. Surface tone gets threat-tagged before communicative intent is understood. This is not a social media problem. It is a biology problem — and it plays out across every relationship that matters: couples, parents and children, friends, communities, and colleagues.

Social media spent 15 years rewiring human brains toward threat-first communication — infinite scroll and variable reward trained us to scan for threat signals compulsively, at scale, without our consent. The **NeuroAI Cognitive Companion** is the counter-intervention: a foundation model of communicative intent, grounded in the neuroscience of mentalising (TPJ) and threat response (amygdala), deployed as an omnichannel cognitive companion across digital text, mobile, and voice.

It does not classify tone. It models the probability distribution of communicative intent — conditioned on relational history, current context, and the living semantic space between two specific people (the Relationship Digital Twin). It surfaces the gap between what was expressed and what was likely received. And through repeated conscious correction of that gap, it rewires users — using the same neuroplasticity mechanisms as Duolingo, directed toward intent-first connection instead of threat-first vigilance.

This is AI for Science: a testable neuroscience hypothesis, a novel foundation model, a Brain-Score validated architecture, and a 50-person behavioural pilot — all within 12 months. The cognitive companion is how that science reaches the world.

---

## Experimental Plan & Scientific Specification

*This section provides the precise experimental design, hypothesis specification, label schema, and 12-month scope tiers — the scientific programme underlying the product brief. Written for neuroscience PIs and ARIA-style reviewers.*

---

### The Central Scientific Hypothesis (Formally Stated)

**H₁ (Primary):** A language model conditioned on dyadic relational history will predict the *receiver's* parsed intent with significantly higher accuracy than a model conditioned on message content alone — on a held-out test set of emotionally ambiguous English dyadic messages (paired t-test, α = 0.05, minimum effect size Cohen's d ≥ 0.3).

**H₂ (Neural):** Participants who use the Cognitive Companion for 60 days will show measurably increased EEG theta-band inter-brain synchrony during a standardised dyadic communication task, compared to baseline — indicating that externally scaffolded intent awareness facilitates the neural coupling associated with successful communication (Hasson et al., 2012).

**H₃ (Neuroplasticity — exploratory):** Repeated conscious correction of intent gaps, prompted by the Companion over 60 days, will be associated with reduced amygdala-dominant response latency to emotionally ambiguous messages, as measured by ERP components (N2/P3 latency shift). *This is a target of the work, not an established mechanism. We hypothesise it; we do not assert it.*

**What failure looks like:** If H₁ is not confirmed (relational context does not significantly improve intent prediction accuracy), the foundation model's core premise is falsified. The project pivots to understanding *why* dyadic history is insufficient — itself a publishable null result with strong theoretical value.

---

### Intent Label Space (Formally Defined)

The model outputs a probability distribution over **8 mutually exclusive sender intent categories**, applied to emotionally ambiguous dyadic text messages in English:

| ID | Intent Category | Definition | Example signal phrase |
|----|----------------|------------|----------------------|
| I1 | **Seeking connection** | Primary goal is relational proximity; content is secondary | "Can we talk tonight?" |
| I2 | **Expressing concern** | Communicates worry about the receiver's state or situation | "You seem quiet lately" |
| I3 | **Setting a boundary** | Signals a limit on behaviour, time, or emotional availability | "I need some space this week" |
| I4 | **Seeking validation** | Requests acknowledgement or agreement, not action | "Does that make sense to you?" |
| I5 | **Expressing frustration** | Communicates emotional state as primary payload | "Fine, do whatever you want" |
| I6 | **Making a request** | Clear instrumental ask for action or change | "Can you let me know when you're home?" |
| I7 | **Giving information** | Neutral informational content with low emotional valence | "I'll be back at 7" |
| I8 | **Chronic self-interest** | Pattern-level: consistent disregard for receiver's perspective across message history | *(Detected at pattern level, not single-message level)* |

**Annotation constructs — two separate labels per message:**
- **Sender intent label (SI):** What did the writer most likely *intend* to communicate? (Annotator takes the sender's perspective)
- **Perceived intent label (PI):** What is a reasonable receiver most likely to *parse* from this message in the given relational context? (Annotator takes the receiver's perspective)

The *intent gap score* is the divergence between SI and PI distributions — formally: JS-divergence(P(SI), P(PI)). This is the core product metric and the scientific quantity of interest. It is not a sentiment score. It is not a tone score. It is the measurable distance between communicative intent and communicative reception.

**Inter-rater reliability target:** Cohen's κ > 0.70 on *both* SI and PI labels independently, measured on a 20-message pilot annotation set with 5 annotators, before any model training begins. If either κ falls below threshold, the annotation protocol is redesigned before proceeding.

---

### Experimental Design (12-Month Programme)

#### Study 1: Annotation Reliability & Dataset Construction (Month 1–3)

**Goal:** Establish a valid training signal for H₁.

**Method:**
- Curate 2,000 dyadic text messages across 5 relationship types (couples, parent-child, close friends, community groups, colleagues) and 4 emotional valence levels (high positive, high negative, ambiguous positive, ambiguous negative)
- 5 independent annotators per message; annotate SI and PI separately using the 8-category schema above
- Relational context provided as a brief description (relationship type, duration, recent interaction valence) — no identifying information
- Compute κ per category and overall; flag and adjudicate categories below threshold

**Primary output:** 2,000-message annotated dataset with SI/PI dual labels, relational context metadata, κ scores per category. Published on HuggingFace and OpenNeuro.

**Failure gate:** If overall κ < 0.70 after two rounds of adjudication → pause, publish methodology note, redesign label schema.

---

#### Study 2: Foundation Model Training & H₁ Validation (Month 3–6)

**Goal:** Test H₁ — does relational context improve intent prediction?

**Method:**
- Base model: RoBERTa-large (125M parameters) fine-tuned on SI and PI annotation tasks separately
- Relational context encoding: a 16-dimensional context vector (relationship type [5 categories], duration [continuous, log-scaled], recent valence [−1 to +1], message frequency [continuous]) concatenated to the [CLS] token representation
- Experimental condition: model with relational context vector vs. ablated model without (message-only baseline)
- Evaluation: macro-averaged F1 on held-out 400-message test set; paired t-test on per-message accuracy between conditions
- Human baseline: majority vote of 5 annotators as ground truth; human-parity gap reported

**Primary metric:** ΔF1 (model with context − model without context) on PI label prediction on ambiguous-valence messages (highest practical relevance)

**Secondary metric:** Calibration (ECE — expected calibration error) of the intent distribution output

**Compute budget:**
- Demo/prototype (DistilBERT, Colab): ~$20–50
- Full RoBERTa-large fine-tuning (3 runs × 5 epochs, A100): ~$150–300 on Lambda Labs
- Ablation studies + hyperparameter sweeps: ~$300–600
- **Total ML compute budget: ~$500–1,000** (to be confirmed with Encode funding allocation)

---

#### Study 3: Brain-Score Neural Plausibility Validation (Month 6–8)

**Goal:** Validate that the foundation model's internal representations are neurally plausible.

**Method:**
- Submit to **Brain-Score Language** benchmark (Martin et al., 2023; DiCarlo Lab, MIT)
- Specific benchmarks targeted: **Pereira2018** (fMRI, language comprehension), **Fedorenko2016** (fMRI, localiser paradigm), **Blank2014** (fMRI, naturalistic reading)
- Adaptation: extract hidden-state activations from the RoBERTa-large intent model at each transformer layer; fit linear regression probes to fMRI ROI activations in language-selective cortex (IFG, aMTG, pMTG, PostTemp, AnGyd)
- Comparison: report Brain-Score on each benchmark vs. published baseline (GPT-2, RoBERTa-base on standard language tasks)
- **What failure looks like:** If our intent model scores significantly *below* standard RoBERTa-base on neural plausibility benchmarks, this suggests the pragmatic fine-tuning has reduced rather than enhanced neural alignment — a publishable finding about the relationship between pragmatic training and neural plausibility

**Note on scope:** Brain-Score validation is a **Should** deliverable (see Scope Tiers below), not a Must. It does not gate the primary H₁ result. It provides a second, independent line of scientific evidence if H₁ is confirmed.

---

#### Study 4: Behavioural Pilot & H₂ EEG Validation (Month 7–11)

**Goal:** Test H₂ — does 60 days of Companion use shift EEG inter-brain synchrony during dyadic communication tasks?

**Scope (right-sized from original):**
- **N = 20–24 participants** (12 dyadic pairs) — powered for a medium effect size (d = 0.5) with 80% power at α = 0.05 for a within-subjects pre/post design
- **EEG only** (not fMRI) — 64-channel active EEG (lab partner equipment), standard 10-20 placement
- **Single primary endpoint:** theta-band (4–8 Hz) inter-brain phase synchrony (IBS) during a standardised dyadic task (simultaneous reading of ambiguous messages, rating of perceived intent)
- **Two timepoints:** Baseline (Day 0) and post-intervention (Day 60)
- **Intervention:** 60 days of Companion browser extension use in naturalistic messaging contexts
- **Control condition:** same dyads at baseline pre-Companion, serving as their own controls (within-subjects)

**Primary analysis:** Paired Wilcoxon signed-rank test on IBS values (pre vs. post); effect size r reported

**Secondary analysis:** Correlation between individual intent gap score decline (product metric) and IBS increase (neural metric) — tests whether the product intervention and the neural shift are causally related

**H₃ (exploratory):** ERP component analysis (N2/P3 latency) on single-message EEG trials — exploratory, not pre-registered, reported as preliminary findings

**Lab partner role:**
- Provides: EEG equipment, lab space, ethics umbrella, existing dyadic communication paradigm (to be adapted)
- Contributes: named PI co-authorship, IRB/ethics approval framework, EEG data preprocessing pipeline
- Our contribution: foundation model, browser extension, intent gap visualiser, annotated dataset, analysis code

**Recruitment:** 12 couples/close dyads recruited via lab partner's existing participant pool + university mailing lists. Inclusion criteria: English-speaking dyad, smartphone users, ≥6 months established relationship.

---

### 12-Month Scope Tiers (Must / Should / Could)

| Tier | Deliverable | Rationale |
|------|-------------|-----------|
| **MUST** | 2,000-message annotated dataset (SI + PI dual labels, κ validated) | The scientific contribution. Exists nowhere today. |
| **MUST** | Foundation model (RoBERTa-large, relational context conditioning) trained and H₁ tested | Core hypothesis. If this fails, everything else is moot. |
| **MUST** | Intent Gap Visualiser demo (Streamlit) with history slider | Fellowship submission asset. Shows hypothesis visually. |
| **MUST** | Paper submitted: dataset + model + H₁ results | Primary fellowship output. |
| **SHOULD** | 20-participant EEG pilot (H₂) — with confirmed lab partner | Adds neural evidence layer. Requires lab partner letter of intent. |
| **SHOULD** | Brain-Score submission (Pereira2018, Fedorenko2016) | Second scientific contribution. ~2 weeks work post-model-training. |
| **SHOULD** | Dataset published on OpenNeuro/HuggingFace | Open science. Community value. |
| **COULD** | Browser extension (Chrome MV3, local inference) | Product proof-of-concept. Depends on model size fitting on-device. |
| **COULD** | Relationship Digital Twin basic visualisation | Demonstrates Horizon 1 product direction. |
| **COULD** | 60-day longitudinal behavioural component of pilot | Richer neuroplasticity data. Depends on recruitment pace. |

**The 12-month primary commitment is the MUST tier.** Everything in SHOULD is high-confidence given a confirmed lab partner. COULD items are genuine stretch goals — valuable if reached, not promised.

---

### Bias, Fairness & Ethical Risk Analysis

**1. Cultural and linguistic label bias**
Intent categories and their surface linguistic signals vary across cultures. "Fine, do whatever you want" carries different pragmatic weight in British English, American English, and South Asian English. Annotators from a single cultural background will systematically mislabel messages from other communities.

*Mitigation:* Annotator pool deliberately diverse across UK cultural backgrounds (target: minimum 3 distinct cultural backgrounds among 5 annotators). Cultural background recorded as annotator metadata. Per-culture κ reported separately; categories with high cross-cultural variance flagged and handled with wider confidence intervals in the model output.

**2. Systematic mislabelling of marginalised communication styles**
Neurodiverse communicators (ADHD, autism spectrum) use pragmatic structures that diverge from neurotypical norms. A model trained predominantly on neurotypical annotations will systematically misclassify neurodiverse intent — potentially causing harm to the users who most need accurate intent support.

*Mitigation:* Neurodiverse-authored messages explicitly included in the dataset (recruited via autism/ADHD community groups). Separate κ computed on neurodiverse subset. Model error rates on neurodiverse messages reported explicitly in the paper. "I don't know / ambiguous" is a valid annotator response — not forced into the 8-category schema.

**3. Downstream harm in vulnerable relationships**
A false low gap score (model says "no misunderstanding risk" when there is one) in a high-stakes relationship context could cause real harm — e.g., in a relationship with a history of emotional abuse, a low risk score could discourage a user from seeking help.

*Mitigation:* The Companion explicitly surfaces uncertainty. Distributions with high entropy (model is uncertain) display a "high ambiguity" flag, not a false confidence score. The truth-telling feature (pattern asymmetry detection) is designed to surface risk, not suppress it. Safeguarding signpost integrated for users whose Digital Twin shows sustained divergence with high self-interest asymmetry.

**4. On-device security and GDPR Article 25 — threat model**
The Relationship Digital Twin is stored locally. The threat: device compromise (malware, shared device, domestic abuse scenario where a partner accesses the device).

*Mitigation:* Digital Twin data encrypted at rest (AES-256, device keychain). No cloud sync in MVP. Biometric/PIN gate on Companion data access. Explicit design review: the tool must not become a surveillance instrument for an abusive partner. Domestic abuse scenario is an explicit design constraint, reviewed with lab partner ethics board.

**5. Consent network (Horizon 2) — asymmetric power in consent**
In relationships with power imbalances, "mutual consent" may not be truly voluntary. A partner, manager, or parent may pressure the other party to activate intent sharing.

*Mitigation:* This is explicitly a Horizon 2 ethical design constraint, not an MVP concern. When Horizon 2 is designed, consent architecture will be reviewed with an ethics board and domestic abuse / coercive control specialists before any feature ships.

---

Every human relationship is mediated by language. And language, as processed by the human brain, is systematically distorted — not by malice, but by biology. The amygdala's threat response fires within tens to hundreds of milliseconds — ahead of the prefrontal cortex's completion of semantic processing (LeDoux, 1996; Öhman & Mineka, 2001; subcortical "low road" threat pathway). In that window, emotionally ambiguous messages get tagged as potential threats before their communicative intent is fully resolved. Intent is lost. Misunderstanding becomes the default.

*Note: The specific latency figures derive from threat-response research using visual and auditory stimuli in controlled lab settings. Extrapolation to digital text message reading is a core assumption of this project — one we intend to test directly in the EEG pilot.*

This timing gap does not discriminate between a Slack message from a colleague and a WhatsApp message from a partner. It fires in every relationship, across every communication channel, every day. The result is:

- Couples who argue about what was *meant*, not what was *said*
- Parents and children who feel chronically misunderstood by each other
- Friends whose relationships quietly erode over messages that were never meant the way they landed
- Communities fractured by the compounding weight of small misreadings
- Professionals who communicate with precision but still generate conflict

No tool today addresses this at the source. Grammarly corrects surface language. Hume AI measures emotional expression. Crystal Knows gives static personality profiles. None model the probability distribution of communicative intent — conditioned on who is speaking, who is listening, and the full history of their relationship.

### Problem Impact

The scale of this problem is civilisational:

- **Couples:** 40–50% of marriages end in divorce; communication breakdown is the most cited cause
- **Mental health:** Chronic miscommunication is a primary driver of loneliness, anxiety, and relationship-induced depression
- **Neurodiverse individuals:** Structural neurological differences in intent parsing create chronic isolation for millions — the gap between intended and received meaning is their daily reality
- **Communities:** Social media's variable-reward architecture has been associated with measurably increased polarisation, affective distrust, and conflict at population scale (Haidt & Rose-Stockwell, 2019; Brady et al., 2017 on moral-emotional language amplification) — consistent with threat-first attentional priming at scale, though direct causal neuroplasticity evidence remains an active research area

The deeper harm: most people experiencing this do not know the mechanism. They attribute miscommunication to character flaws — "she's too sensitive," "he never listens," "they're selfish" — when the actual cause is a 40ms biological timing gap they have no tool to see.

### Why Existing Solutions Fall Short

| Solution | What it does | What it misses |
|---|---|---|
| **Grammarly** | Corrects surface grammar and tone | Does not model intent; does not know relational history |
| **Hume AI** | Measures emotional expression in voice | Measures *how* you feel, not *what you meant* |
| **Crystal Knows** | Static personality profiles (OCEAN/MBTI) | No dynamic relational context; no intent modelling |
| **Therapy / coaching** | Human-guided reflection | Not scalable; not real-time; not in the moment of communication |
| **Social media** | Amplifies expression | Actively worsens threat-first parsing through variable reward loops |

The fundamental gap: **no existing tool conditions intent on relational history.** The same message — "fine, do whatever you want" — has a completely different intent distribution from a stranger versus a partner of ten years after three days of silence. A model that ignores history is not modelling intent. It is modelling surface patterns.

There is also the hardest unsolved problem: **some people genuinely have ill intentions or are chronically self-absorbed.** A tool that cannot distinguish genuine misunderstanding from consistent manipulation is not just incomplete — it is dangerous. It would gaslight users into tolerating toxic relationships. The Cognitive Companion is explicitly designed to surface this truth, not obscure it.

### Proposed Solution

The **NeuroAI Cognitive Companion** is a three-layer system:

**Layer 1: The Foundation Model (Science)**
A ~1B parameter transformer trained on communicative intent — not sentiment, not tone, not personality. The model outputs an *intent distribution*: P(intent | message, relational history, context). It is architecturally grounded in neuroscience:
- **TPJ-inspired mentalising head:** A dedicated module trained on Theory of Mind tasks, modelling what the *receiver* is likely to parse
- **Amygdala-analogue threat detector:** A fast, parallel classifier that flags when threat-first parsing is likely to activate in the receiver
- **Predictive coding layer:** Models communicative surprise — high surprise = miscommunication risk
- **Brain-Score validated:** Neural plausibility benchmarked against fMRI data (MIT DiCarlo Lab framework)

**Layer 2: The Relationship Digital Twin (Memory)**
A living computational model of the semantic space between two specific people — built from relational history, updated with every interaction, stored privately on-device. It:
- Conditions the intent distribution on *this specific relationship's* history
- Detects pattern asymmetries: is one person's intent consistently self-serving? Is the semantic gap widening or closing over time?
- Distinguishes chronic misunderstanding from genuine ill intent — surfacing the truth rather than manufacturing comfort
- Visualises relationship health as a dynamic 2D semantic map — convergence means growing shared meaning; divergence means growing distance

**Layer 3: The Cognitive Companion (Reach)**
The omnichannel surface layer that brings the science to every communication moment:
- **Browser extension:** Real-time intent analysis as you type (Chrome MV3, Offscreen Documents API, sub-500ms latency)
- **Mobile keyboard:** iOS/Android AI keyboard layer — intent distribution shown before you send
- **Earpiece:** Voice-based real-time analysis (BLE audio pipeline, Whisper Turbo ASR, on-device inference)
- **Federated personal model:** On-device LoRA adapter personalised to each user via FwdLLM — never leaves the device

**The Neuroplasticity Loop (Hypothesis):**
Every time the Companion shows the gap between expressed tone and likely received intent — and the user consciously corrects it — we hypothesise they are performing the class of deliberate mental training that Davidson & Lutz (2008) showed produces measurable plastic changes in neural circuits. The mechanism: repeated, conscious correction of a cognitive pattern is structurally analogous to the attentional training protocols that produce detectable changes in prefrontal and anterior cingulate activity. Whether the Companion's feedback loop constitutes equivalent mental training is a target of the 60-day pilot — not an established fact. The neuroplasticity loop is the hypothesis the pilot is designed to test. If confirmed, the Companion becomes a scalable neuroplasticity intervention. The same feedback architecture as Duolingo, directed toward intent-first communication. After 60 days, we predict:

> *"I stopped reacting to what I thought they meant, and started responding to what they actually meant."*

### Key Differentiators

**1. Intent distribution, not tone classification**
The model outputs P(intent | message, history, context) — a probability distribution over communicative intents. Not "this message is negative." Not "you sound frustrated." *"There is a 68% probability this message will be received as a threat, a 22% probability it will land as concern, and a 10% probability it will be read as neutral — based on your relational history."* No existing tool does this.

**2. Relational history as a first-class input**
The Relationship Digital Twin conditions every intent prediction on the full history of the specific relationship. The same message means different things in different relationships. This is the scientific novelty — and the product moat.

**3. Truth-telling, not comfort-manufacturing**
The tool surfaces pattern asymmetries — chronic self-interest, widening semantic gaps, manipulation patterns — rather than optimising for user comfort. It is not a tool for making bad relationships feel better. It is a tool for making the truth of a relationship visible.

**4. Neuroscience-grounded rewiring**
The neuroplasticity mechanism is not a metaphor. It is grounded in Davidson & Lutz (2008), Askenasy & Lehmann (2013), and the predictive coding literature. The tool is explicitly designed as a top-down intervention — using conscious awareness of intent gaps to induce measurable synaptic change in mentalising circuits.

**5. Privacy-first federated architecture**
The personal model and Relationship Digital Twin never leave the device. The foundation model is public and open-source. This is GDPR Article 25 (Privacy by Design) by architecture, not by policy.

---

## Encode Fellowship Demo Plan

### Goal
Demonstrate the core scientific hypothesis in under 3 minutes in a way that lands simultaneously with:
- **ARIA/Encode reviewers:** Rigorous neuroscience, testable hypothesis, credible architecture
- **Pillar VC partners:** Compelling hook, massive addressable problem, clear product vision

### The Demo: "Intent Gap Visualiser"

A Streamlit Python app demonstrating the full hypothesis stack in a single screen.

#### Screen 1: The Neuroscience Problem (0:00–0:30)
**Voiceover opens:**
> *"There is a 40–80 millisecond window between when your amygdala fires and when your prefrontal cortex processes meaning. In that window, every ambiguous message gets threat-tagged before it gets understood. That's not a communication problem. That's a biology problem."*

Show a simple animated diagram: amygdala fires (red) → 40ms gap → PFC processes (blue). The gap is labelled: *"Where miscommunication lives."*

#### Screen 2: The Demo — Intent Gap Made Visible (0:30–1:15)
Input a real message: *"Fine, do whatever you want."*

Show three panels side by side:
- **Left:** What tone classifiers see — "Neutral / Slightly negative" (what Grammarly/Hume see)
- **Centre:** Intent distribution — bar chart: Frustrated 71% / Resigned 19% / Genuinely permissive 10%
- **Right:** Relational history slider — "How well do you know this person?" Slide from Stranger → Close partner. Watch the distribution shift in real time as history is added.

The key moment: the distribution shifts dramatically with relational context. *This is the science.* Same message, completely different intent — depending on who is saying it and to whom.

#### Screen 3: The Science Underneath (1:15–1:45)
One clean slide:
> *"This is a foundation model of communicative intent — not sentiment. It is architecturally grounded in the TPJ (mentalising) and amygdala (threat detection). We validate against fMRI data using Brain-Score (MIT). The personal layer is federated — it never leaves your device."*

Show the TPJ/amygdala diagram with the model architecture overlaid. Name the ARIA spaces: *"Scalable Neural Interfaces + Collective Flourishing."*

#### Screen 4: The Neuroplasticity Loop (1:45–2:30)
Show the **7-day rewiring tracker** — a Duolingo-style streak with intent clarity score improving over time. Show the **Relationship Digital Twin** — a 2D semantic map of two people's communication space. Two clusters. Are they converging or diverging?

> *"Social media spent 15 years rewiring human brains toward threat-first communication. This is the counter-intervention — same neuroplasticity mechanisms, directed toward connection."*

Then show the **truth-telling feature**: a relationship where one person's intent consistently scores high on self-interest regardless of context. The Digital Twin shows divergence. The tool surfaces the pattern — honestly.

> *"This is not a tool for making bad relationships feel better. It is a tool for making the truth of a relationship visible."*

#### Screen 5: The Arc — Three Horizons (2:30–3:00)

Three frames. Fifteen seconds each. No explanation needed.

**Frame 1 — The Mirror:**
Maya alone. Her message. The gap score. The Digital Twin — one person's communicative patterns, mapped.
*"You see yourself as others receive you."*

**Frame 2 — The Bridge:**
Maya AND Dev. Two constellations. A consent toggle — one tap, symmetric. The gap score updating from both sides simultaneously, dropping in real time.
*"With mutual consent — you see each other as you mean to be seen."*

**Frame 3 — The Map:**
Thousands of constellations. Zooming out. A living atlas — anonymous, consensual, healing.
*"And together — humanity begins to understand itself."*

Fade to black. White text:

> *"We are building the foundation model that explains why humans misunderstand each other at the brain level — and the cognitive companion is how that science reaches the world."*

### Build Plan (1.5 Weeks)

| Days | Task | Output |
|------|------|--------|
| 1–2 | Curate 200 annotated ambiguous messages (GPT-4 assisted labelling across all relationship types) | Training dataset |
| 3–4 | Fine-tune DistilBERT/RoBERTa intent classifier; add relational history conditioning via context vector | Intent distribution model |
| 5–6 | Build Streamlit UI: message input, tone vs intent panels, history slider, distribution visualiser | Core demo screen |
| 7–8 | Add neuroplasticity streak tracker + Relationship Digital Twin 2D plot (plotly) + truth-telling asymmetry panel | Full demo |
| 9 | Add neuroscience panel: TPJ/amygdala timing diagram (matplotlib), ARIA alignment slide | Science credibility screen |
| 10 | Record 3-minute demo video; upload to YouTube/Drive | Encode submission asset |

**Compute cost:** ~$10–30 on Google Colab Pro or Lambda Labs A100

### The One Screen That Will Make Reviewers Stop

**The transformation moment — two worlds, one message.**

The demo message: *"Can we talk tonight?"* — sent at 2pm on a Tuesday by Maya to Dev.

**Split screen:**
- **Left — The Old World (Amygdala):** The raw message, stark. Dev's internal state: stomach drops. Threat response fires. *"Something is wrong. Are we in trouble?"* No tool intervenes. The damage begins before a word is spoken.
- **Right — The New World (TPJ):** Intent distribution visible — *Wants to connect: 84% / Something wrong: 12% / Practical logistics: 4%.* History slider: Partner of 2 years. Threat score: low. Dev responds from curiosity, not defence.

Between them: the **intent gap score** — one number. *"Gap: 74%."*

**The moment the history slider moves** — from Stranger to Partner of 2 years — and the distribution reshapes completely in real time — *that* is the science made visceral. Same message. Completely different intent. Depending on who is saying it and to whom.

**The moment of scientific honesty** (earns the ARIA reviewers):
> *"This model is wrong 26% of the time on ambiguous messages. That's not a limitation to hide — that's the research mission. Twelve months of neural validation, Brain-Score benchmarking, and a 50-person behavioural pilot exist to close that gap. The science is the point."*

That single screen IS the product, the pitch, and the proposal simultaneously. It makes the invisible visible — and it gives every reviewer, VC and scientist alike, the feeling of seeing something for the first time.

---

## Target Users

### Primary Users

**1. Maya & Dev — Couple Living Together (Primary Demo Persona)**
- **Who:** Partners sharing a home, communicating across digital channels throughout the day
- **Pain:** The same argument every two weeks — started by a message sent under stress, misread before Dev finished reading it. By the time they're face to face, the original intent is buried under three layers of defensive reaction. Proximity creates more communication surface area, not less friction.
- **What they'd say at 60 days:** *"We still disagree. But we stopped having the argument about the argument."*
- **Why primary:** Universal recognition — every reviewer has sent or received a message that landed wrong with someone they love. No setup required.

**2. Sarah — Mum Group / Community Friend Circle**
- **Who:** 38, mother of two, member of a WhatsApp group of 12 school mums — ostensibly supportive, actually a minefield
- **Pain:** A message about school pickup logistics last month was read as passive aggression by three people. She didn't notice she'd caused offence until someone went quiet. The relationships that hold her community together are the most fragile to a single misread message — and she has no real-time visibility.
- **What they'd say at 60 days:** *"I used to spend an hour after sending a message wondering if it landed wrong. I don't do that anymore. I just know before I send."*
- **Why important:** Community dimension — underrepresented in tech demos; represents the social fabric use case; enormous word-of-mouth network

**3. Priya — Neurodiverse Individual (ADHD / Autism Spectrum)**
- **Who:** 28, professional, structurally processes communicative intent differently from neurotypical people
- **Pain:** The gap between what she means and what people receive is a daily source of confusion and isolation. She's tried therapy, coaching, social cues guides. Nothing gives real-time feedback in the moment of communication.
- **What they'd say at 60 days:** *"I finally have a way to check what I think I'm saying against what people are likely to hear. It's like having a translator — but for intent, not words."*
- **Why important:** Strongest scientific and ethical framing for ARIA; measurable clinical outcome; underserved market with acute need

**4. Arun — Father of a Teenager**
- **Who:** 52, father of a 17-year-old son, relationship deteriorating through digital miscommunication
- **Pain:** He means care; his son hears control. He has no way of seeing how his messages land — and the distance is growing with every unanswered text.
- **What they'd say at 60 days:** *"My son told me something real for the first time in months. I think it's because I stopped sounding like I was criticising when I wasn't."*

**5. James — Remote Engineering Manager**
- **Who:** 41, engineering manager, sends 200+ Slack messages daily
- **Pain:** Three team members have flagged him as "intimidating" in anonymous feedback. His intent is directness. The received intent is threat. He genuinely doesn't know why.
- **What they'd say at 60 days:** *"My manager thinks I've become a better communicator. I haven't changed what I say — I've changed how I send it."*

### Secondary Users

| User | Role | Value |
|------|------|-------|
| **Therapists / Couples Counsellors** | Clinical tool — use the Relationship Digital Twin to surface patterns in sessions | Professionalises the insight; opens B2B clinical channel |
| **Neuroscientists / Lab Partners** | Use the open-source foundation model for their own research | Accelerates adoption; generates citations; builds scientific credibility |
| **Encode/ARIA Reviewers** | Researchers who have personally experienced lab collaboration miscommunication | The demo persona speaks directly to their lived experience |

### User Journey: Maya & Dev (Primary)

| Stage | Experience |
|-------|-----------|
| **Discovery** | Maya sees a post: *"I nearly ended a 3-year relationship over a misread message."* She downloads the app. |
| **Onboarding** | Pastes the last message that caused a fight. Sees the intent gap score for the first time. *"That's exactly what happened."* Aha moment in under 60 seconds. |
| **Core Usage** | Browser extension active while typing. Mobile keyboard layer for WhatsApp. Before sending anything difficult — checks the intent distribution. |
| **The Streak** | Day 7: intent clarity score up 18%. Dev notices something has shifted in their conversations. Doesn't know why yet. |
| **Success Moment** | Day 23: They have the conversation they've been avoiding for 6 months. It doesn't spiral. Maya knows why. |
| **Long-term** | The Companion becomes invisible — because the habit is now internal. Intent-first communication has been rewired. That's the product working perfectly. |

---

## Success Metrics

### The ONE Scientific Finding to Aim For

> *Neural convergence between sender and receiver intent representations — measurable via EEG/fMRI — after 60 days of Companion use, compared to baseline. That is the result that makes this a neuroscience paper, not just a product.*

### Layer 1: Scientific Metrics (ARIA/Encode reviewers)

| Metric | Target | How Measured |
|--------|--------|-------------|
| Inter-rater reliability (SI labels) | Cohen's κ > 0.70 | 20-message pilot, 5 annotators, before model training |
| Inter-rater reliability (PI labels) | Cohen's κ > 0.70 | Same pilot — separate construct, separate κ |
| H₁: ΔF1 (relational context model vs. message-only baseline) | Statistically significant positive delta (α = 0.05, d ≥ 0.3) | Paired t-test on 400-message held-out test set, ambiguous-valence subset |
| H₁: PI prediction macro-F1 | >65% vs. human majority-vote baseline | Held-out test set, human annotator baseline reported |
| Brain-Score (Pereira2018, Fedorenko2016) | Reported score vs. RoBERTa-base baseline | MIT Brain-Score Language benchmark — linear probe on hidden states |
| Novel neural-pragmatic dataset | 2,000 messages, dual SI/PI labels, κ-validated, 5 relationship types | HuggingFace + OpenNeuro publication |
| Lab partner confirmed (named PI, letter of intent) | Before application submission 28 March | UCL FIL / Cambridge CBU / Nottingham Psychology |

**Note on model error:** On emotionally ambiguous messages, human annotators themselves disagree ~30% of the time (expected given the κ target). A model matching human-level agreement on ambiguous messages is not underperforming — it is correctly representing the genuine uncertainty of communicative intent. The gap score's entropy communicates this uncertainty to users. Overconfident classification would be a worse failure than honest uncertainty.

### Layer 2: Neuroplasticity Metrics (Encode science panel)

| Metric | Target | Timeframe |
|--------|--------|-----------|
| Intent gap score decline per user | >20% reduction | 60 days |
| EEG theta-band synchrony shift | Measurable increase vs. baseline | Pilot month 8–11 |
| TPJ activation increase vs. amygdala dominance | Detectable via fMRI in 50-person pilot | Month 9–11 |
| Conscious correction rate | User corrects message after seeing intent distribution >3×/week | Day 14 onward |
| "Stopped having the argument about the argument" | >60% of couples pilot self-report | Day 60 |

### Layer 3: Product Metrics (Pillar VC)

| Metric | Target | Timeframe |
|--------|--------|-----------|
| 60-day pilot completion rate | >80% of 50 participants complete protocol | Month 11 |
| 7-day streak retention | >50% of users maintain streak | Day 30 |
| Relationship Digital Twin convergence score | Measurable convergence in 70% of active relationships | Day 90 |
| Daily active usage | >4× per week per user | Day 30 |
| NPS / would recommend | >70 | Day 60 |

### Layer 4: Fellowship Deliverables (Encode programme team)

| Milestone | Target Date |
|-----------|------------|
| Foundation model trained + open-sourced on HuggingFace | Month 5 |
| Novel neural-pragmatic dataset collected (50 participants EEG) | Month 8 |
| Dataset published on OpenNeuro | Month 9 |
| Brain-Score submission | Month 10 |
| 50-person behavioural pilot completed | Month 11 |
| Paper submitted (foundation model + Brain-Score + pilot results) | Month 12 |
| Lab partner co-authorship confirmed | Month 2 |

### Business Objectives (12-Month Horizon)

| Objective | Success Signal |
|-----------|---------------|
| Scientific credibility | Published paper, Brain-Score ranking, lab partner co-authorship |
| Open-source adoption | Foundation model downloaded >500× on HuggingFace within 3 months of release |
| Product-market signal | 50-person pilot with >80% completion, >70 NPS |
| Fellowship value | Encode network, ARIA visibility, Pillar VC relationship for Series A |
| Lab partner ecosystem | 2+ neuroscience labs actively using the foundation model for their own research |

---

## MVP Scope

### The Minimum That Proves The Science

The MVP is not a product launch. It is a scientific proof-of-concept with a working demonstration — designed to win the Encode x Pillar VC AI for Science Fellowship and validate the core hypothesis within 12 months. Everything in scope serves one mission: proving that relational context transforms intent prediction, and that conscious exposure to that prediction rewires communication habits.

### Core Features (IN for MVP)

**1. Intent Gap Visualiser — The Demo**
- Streamlit web app accepting a text message as input
- Outputs intent distribution: P(intent | message, context) as a labelled bar chart
- Three-panel split: tone classifier view (what Grammarly sees) vs. intent distribution vs. relational history effect
- **History slider:** Moves from Stranger → Acquaintance → Close Friend → Partner — distribution reshapes in real time
- **Gap score:** Single number showing the delta between what was expressed and what is likely received
- The demo message: *"Can we talk tonight?"* — Maya to Dev — split screen Old World / New World
- This screen IS the scientific hypothesis made visible. Nothing is more important to ship.

**2. Foundation Model (The Science Core)**
- ~200M–1B parameter transformer trained on communicative intent — not sentiment, not tone
- Outputs intent distribution with confidence scores across intent categories
- TPJ-inspired mentalising head: dedicated module trained on Theory of Mind tasks
- Amygdala-analogue threat detector: fast parallel classifier for threat-first parsing risk
- Relational history conditioning: context vector encoding relationship type, duration, recent interaction valence
- Trained on novel neural-pragmatic dataset (curated + annotated, see below)
- Open-sourced on HuggingFace at Month 5 milestone

**3. Novel Neural-Pragmatic Dataset**
- 200 seed messages (curated, GPT-4 assisted initial labelling, human-verified)
- 50-participant behavioural pilot — messages annotated with intent labels across relationship types
- 5 human annotators per message subset; inter-rater reliability threshold: Cohen's κ > 0.70
- EEG data collection paired with intent annotation tasks (UCL FIL / Cambridge CBU lab partner)
- Published on OpenNeuro at Month 9
- **This dataset is the scientific contribution.** It does not exist today. Creating it is a primary deliverable.

**4. Brain-Score Validation**
- Foundation model submitted to MIT Brain-Score Language benchmark (neural predictivity against fMRI data)
- Validates that the model's internal representations are neurally plausible — not just behaviourally useful
- Submitted at Month 10; result reported in fellowship paper
- Target: comparable to published NeuroAI baselines on language tasks

**5. Relationship Digital Twin (Basic — MVP Version)**
- Lightweight on-device relational history model
- Tracks: message valence history, intent gap scores over time, convergence/divergence trend
- Visualised as 2D semantic map — two clusters, distance indicates semantic convergence or divergence
- **Pattern asymmetry detection:** flags when one person's messages consistently score high on self-interest intents regardless of relational context — the truth-telling feature. Does not hide chronic manipulation.
- Stored locally; never transmitted. GDPR Article 25 by architecture.

**6. Browser Extension (Proof of Concept)**
- Chrome MV3 extension with Offscreen Documents API
- Reads message being typed; shows intent distribution in sidebar before send
- Sub-500ms latency on local inference (quantised model, INT8)
- Works on: Gmail, WhatsApp Web, Slack Web
- **This is the neuroplasticity delivery mechanism** — the conscious correction moment that rewires over 60 days

**7. Behavioural Pilot with EEG Component**
- **N = 20–24 participants (12 dyadic pairs)** — right-sized for within-subjects pre/post design powered at 80% (d = 0.5, α = 0.05); recruited via lab partner participant pool + university mailing lists
- Relationship types: couples and close friends (dyadic pairs with ≥6 months established relationship, English-speaking, smartphone users)
- **EEG only** (not fMRI) — 64-channel active EEG at lab partner facility; two timepoints: Day 0 (baseline) and Day 60 (post-intervention)
- **Primary EEG endpoint:** theta-band (4–8 Hz) inter-brain phase synchrony (IBS) during standardised dyadic message-reading task — pre vs. post Companion use
- **Behavioural measures:** intent gap score decline (product metric), 60-day streak data, self-reported relationship quality (validated RQ scale), NPS
- **Exploratory EEG:** ERP N2/P3 latency analysis (not pre-registered; reported as preliminary)
- **Minimum success gate:** κ > 0.70 on annotation pilot → model H₁ confirmed → EEG IBS shift detectable with r ≥ 0.3 effect size

---

### Out of Scope for MVP

These features are explicitly deferred — not because they lack value, but because including them in Month 1–12 would guarantee failure. Each deferral is a deliberate scope discipline decision, not a permanent no.

| Feature | Why Deferred |
|---------|-------------|
| **Mobile AI keyboard (iOS/Android)** | Requires App Store approval, platform-specific development, and live inference optimisation. Adds 3+ months of build time. The browser extension proves the same mechanism at 10% of the cost. |
| **Earpiece / BLE audio pipeline** | Voice inference pipeline (Whisper Turbo + BLE) requires hardware testing, latency optimisation, and separate user research. Post-MVP when product-market signal is confirmed. |
| **Full federated learning infrastructure** | FwdLLM on-device personalisation at scale requires significant MLOps infrastructure. MVP uses on-device storage only — no model updates. Full personalisation is a Year 2 capability. |
| **Multi-language support** | Pragmatic intent annotation in non-English languages requires separate datasets and annotators. English-only for MVP. Scientific validity is language-agnostic — the mechanism transfers. |
| **Group chat / multi-party intent analysis** | Three-or-more-party intent modelling is a materially harder problem. Dyadic (two-person) relationships are the MVP constraint. Group dynamics are a post-pilot product extension. |
| **B2B therapist platform** | Clinical-grade tools require IRB-approved protocols, HIPAA compliance (US), and professional liability framing. This is a Year 2 revenue stream — after scientific credibility is established. |
| **Manipulation detection at scale / population-level analysis** | Aggregating pattern data across users raises serious ethical and privacy questions. All analysis stays local to the individual relationship in MVP. Population-level insights require ethics board approval. |
| **Real-time voice in consumer app** | Live conversation coaching (not just text) is a fundamentally different UX and inference challenge. Text-first is the MVP constraint. Voice is Year 2. |

---

### MVP Success Criteria

The MVP is successful when ALL FOUR of the following gates are passed:

**Gate 1 — Scientific Validity**
- Foundation model achieves >65% intent accuracy on held-out ambiguous messages vs. human baseline
- Inter-rater reliability on intent annotation reaches Cohen's κ > 0.70 before model training begins
- Brain-Score submission accepted and result published

**Gate 2 — Neural Evidence (SHOULD tier — requires confirmed lab partner)**
- EEG data collected from ≥20 participants (12 dyadic pairs) shows measurable theta-band inter-brain synchrony shift (Day 60 vs. Day 0 baseline), effect size r ≥ 0.3
- ERP N2/P3 latency analysis completed as exploratory finding (not pre-registered)
- *fMRI is explicitly out of scope for Year 1. Subcortical/cortical activation analysis is a Year 2 extension.*

**Gate 3 — Product Signal**
- 50-person pilot: >80% completion rate, >70 NPS
- Day 60 intent gap score reduction: >20% per active user
- "Stopped having the argument about the argument": >60% self-report at Day 60

**Gate 4 — Fellowship Deliverables**
- Foundation model open-sourced on HuggingFace (Month 5)
- Dataset published on OpenNeuro (Month 9)
- Paper submitted to peer-reviewed venue (Month 12)
- Lab partner co-authorship confirmed (before application submission — not Month 2, this week)

---

### Risk Mitigation Constraints (Pre-Mortem Applied)

Five failure modes were identified through pre-mortem analysis. These are not risks to monitor — they are **scope constraints that must be built into the execution plan from Day 1.**

**Constraint 1 — Lab Partner Confirmation is Pre-Application, Not Month 2**
The single most catastrophic failure mode: reaching the EEG data collection phase (Month 8) without a confirmed lab partner and IRB approval. Prevention: email UCL FIL, Cambridge CBU, and Nottingham Psychology this week — before the application is submitted on 28 March. A letter of intent from a neuroscience lab is not a nice-to-have. It is an application differentiator and a 12-month critical path dependency.

**Constraint 2 — Ground Truth Problem is Solved Before Model Training Begins**
If the intent annotation process cannot achieve Cohen's κ > 0.70, the foundation model has no valid training signal. Prevention: run a small pilot annotation study (20 messages, 5 annotators) in Month 1 — before any model training begins. If κ < 0.70, pause and redesign the annotation protocol. This is not a technical problem — it is a scientific methodology problem. It must be validated first.

**Constraint 3 — Serial Sequencing is Non-Negotiable**
Running foundation model training, ethics approval, EEG study design, and pilot recruitment in parallel is the fastest path to doing all four badly. The sequence is locked: foundation model complete → ethics approved → EEG study designed → pilot recruited → data collected. No parallelisation of dependent steps.

**Constraint 4 — Onboarding Aha Moment in Under 60 Seconds**
If users do not experience the intent gap viscerally in their first 60 seconds, they will not return. Prevention: the first onboarding screen is a live gap score on the user's own last sent message — no tutorial, no setup, no explanation. The moment of *"that's exactly what happened"* must come before the user reads a single word of copy. This is a product discipline constraint, not a UX detail.

**Constraint 5 — The One Sentence Never Changes**
The greatest risk to a 12-month fellowship is story drift — the framing shifts as new ideas emerge, reviewers push back, or early results are ambiguous. Prevention: one sentence is fixed for the entire 12 months and appears in every communication, every update, every paper abstract:

> *"We are building the foundation model that explains why humans misunderstand each other at the brain level — and the cognitive companion is how that science reaches the world."*

This sentence does not change. Everything else is negotiable.

---

### Future Vision — Three Horizons

There is no fixed timeline. The Cognitive Companion exists on a single arc — accelerated by the pace of AI hardware and model compression, unlocked sequentially as the science earns each step forward. There are three horizons: what the MVP proves, what mutual consent makes possible, and where humanity goes when both are true.

Each horizon requires a human being to say yes. Not surveillance. Not extraction. The philosophical inversion of everything that broke the internet — *consent as architecture, not policy.*

---

#### Horizon 1 — The Mirror *(MVP)*

One person. One message. One Companion.

The gap made visible: P(intent | message, relational history, context) — the probability distribution of what was meant versus what will be received. The history slider shows how relational context reshapes meaning in real time. The Relationship Digital Twin maps the full semantic space of one relationship — convergence, divergence, pattern asymmetry, truth.

The user is alone with their mirror. But the mirror is already changing them.

**The science:** Individual mentalising — TPJ activation, amygdala threat suppression, predictive coding. Validated against fMRI via Brain-Score (MIT DiCarlo Lab). Rewired through the neuroplasticity loop: Davidson & Lutz (2008), repeated conscious correction becoming automatic correction over 60 days.

*"You see yourself as others receive you."*

---

#### Horizon 2 — The Bridge *(When the Science Is Ready)*

Two people. Mutual consent. Both Companions active.

With one symmetric, revocable tap — Maya and Dev each share their Companion's intent model with the other. Maya sees her gap as always. But now Dev's Companion is enriched by Maya's model: he sees his own reception patterns through her lens. The gap score updates from both sides simultaneously. The distance closes from both ends at once.

This is not thought-reading. It is not surveillance. It is the externalisation of what the TPJ already does in every successful act of human understanding — modelling what the other person's mind is processing — made mutual, computational, and conscious.

**What is shared (precisely):**
- **YES** — Intent representation vectors: the mathematical output of each person's foundation model after processing a message
- **YES** — Reception model parameters: how this person's Companion has learned they tend to receive certain intent categories
- **YES** — Convergence/divergence trend: whether this relationship's semantic space is growing or shrinking
- **NOT** raw messages, personal data, inner thoughts, or emotional states

All of it anonymisable. All of it reversible. All of it meaningless without the explicit consent relationship that activates it.

**The science:** Inter-brain neural synchrony — Hasson et al. (2012) showed that neural coupling between speaker and listener predicts communication success; brains literally synchronise during genuine understanding. The Bridge scaffolds that synchrony *before* the conversation, not after. Testable via dual-EEG paradigms. First study of its kind with this architecture.

**The product:** Mobile-first ambient companion — on every device, in every messaging surface, invisible until needed. Full federated personalisation via on-device LoRA adapter. B2B clinical channel: the Relationship Digital Twin as a tool for couples therapists, ADHD coaches, and neurodiverse support practitioners. Multi-language intent modelling beginning with Mandarin and Spanish.

*"With mutual consent — you see each other as you mean to be seen."*

---

#### Horizon 3 — The Map *(Beyond)*

Thousands of pairs. Anonymised. Consented. A living atlas.

When enough Bridges exist — when enough people have chosen, pair by pair, to share their intent models with each other — something emerges that has never existed before: an empirical map of human communicative intent at population scale. Where misunderstanding concentrates — geographically, demographically, relationally. Where understanding spontaneously forms. Where the gap is widest and where it closes fastest.

This is not a product dataset. It is the foundation of a new scientific field: **collective neuroplasticity** — the study of how meaning is made and lost at the level of populations, not just individuals. The Companion creates the data that founds it.

The aggregate pattern, anonymised and consented, becomes a mirror for humanity itself — revealing the structural fault lines of miscommunication that thread through every culture, every relationship type, every language. And for the first time, giving the world the tool to close them.

**The science:** Population-level neural pragmatics — a field that does not yet exist. The dataset that makes it possible does not yet exist. The Cognitive Companion creates both.

> *"Every message sent by a human being is understood as it was intended — not as the amygdala threat-tagged it."*

This is not a productivity tool. It is not a wellness app. It is **intent infrastructure** — the cognitive layer beneath all human interaction, making meaning legible where biology makes it opaque. Three scientific frontiers. One product. One arc.

The Cognitive Companion is how that science reaches every person.
The Map is how it reaches the world.
