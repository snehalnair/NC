---
title: "NeuroAI Cognitive Companion: An Intent-Conditioned Language Model Grounded in Dyadic Relational History and Individual Personality Context"
subtitle: "Encode x Pillar VC AI for Science Fellowship Application"
author: Snnair
date: 2026-03-17
status: integrated-draft
version: 2.0
sourceDocuments:
  - _bmad-output/planning-artifacts/encode-application/encode-application-NC-2026-03-15.md
  - _bmad-output/planning-artifacts/soul-document-architecture-spec-2026-03-16.md
---

# NeuroAI Cognitive Companion
## An Intent-Conditioned Language Model Grounded in Dyadic Relational History and Individual Personality Context

**Encode x Pillar VC AI for Science Fellowship, Application**
**Applicant:** Snnair
**Date:** March 2026
**ARIA Spaces:** Scalable Neural Interfaces · Collective Flourishing

---

## Section 1: Overview

**Scientific question 1:** Can a language model conditioned on dyadic relational history, combined with a closed-loop intent feedback intervention, measurably reduce miscommunication and produce detectable changes in neural markers of mentalising versus threat processing over 60 days?

**Scientific question 2:** Does individual personality context — encoded as a structured three-layer personal narrative instrument — independently improve intent prediction accuracy beyond dyadic relational history alone, and does it solve the cold-start problem that dyadic history cannot?

The most powerful capability a human being can have in the AI era is not a technical skill or an information advantage — it is trust. As artificial intelligence absorbs more of the cognitive and informational labour of human interaction, what remains distinctly, irreducibly human is the quality of connection between people: the degree to which we understand each other's intentions, and are understood in return. Yet as AI mediates more of that connection — drafting our messages, summarising our conversations, predicting our responses — the risk is not that humans become less intelligent. It is that humans become less legible to each other. The intent gap is the measurable form of that illegibility: the distance between what one person means and what another person receives. This project builds the first scientific instrument to measure it, the first intervention designed to test whether it can be closed at the neural level, a candidate infrastructure for scaling that understanding across populations, and a structured methodology for encoding the stable personality architecture that shapes how individuals generate and receive communicative intent. That is the foundation of a trust-based society — and it is what AI for Science is built for.

Human miscommunication is not primarily a social or technological failure. It has a biological substrate. The amygdala's subcortical threat-processing pathway (LeDoux, 1996) responds to emotionally ambiguous stimuli ahead of prefrontal cortical semantic resolution. In digital text communication, where prosody, expression, and physical context are absent, this timing asymmetry means that emotionally ambiguous messages are systematically threat-tagged before their communicative intent is understood. The result is a measurable divergence between what a sender intends and what a receiver parses: an *intent gap*.

No existing NLP system models this gap directly. Sentiment classifiers measure surface tone. Emotion recognition systems measure affective expression. Neither asks the question that matters: *what did this person most likely mean, given who they are and who they are talking to?* Crucially, the same message, "Can we talk tonight?", carries a fundamentally different intent distribution when sent by a new colleague versus a partner of three years after a difficult week. Relational history is not context noise. It is the primary signal. But relational history is itself silent on two classes of information: the stable personality architecture that determines how a person characteristically generates communicative intent, and the specific biographical experiences that shaped that architecture. A new user with no relational history in the system, or an existing user whose history is silent on their conflict response pattern, presents a structural inference problem that dyadic conditioning alone cannot resolve. The Soul Document — a structured three-layer personal narrative instrument — is this project's scientific method for addressing that gap.

This project addresses four concrete scientific gaps:

1. **No neural-pragmatic dataset** conditions intent annotation on dyadic relational history with dual sender/receiver labelling and inter-rater reliability validation.
2. **No language model** has been trained to predict the *receiver's parsed intent* conditioned on dyadic relational context and evaluated against a human-parity baseline.
3. **No empirical study** has tested whether closed-loop intent feedback, showing users the gap between their expressed tone and likely received intent, produces measurable shifts in neural markers of mentalising circuitry over a sustained intervention period.
4. **No structured personality characterisation instrument** has been tested as an independent conditioning signal for intent prediction in naturalistic relational communication, or evaluated for its capacity to close the cold-start inference gap that dyadic history cannot address.

The dataset produced by this project is structurally novel: no existing NLP corpus provides dual sender-intent and perceived-intent labels on the same message, conditioned on dyadic relational context metadata, with validated inter-rater reliability on both label types simultaneously — the combination required to measure the intent gap as a computable scalar rather than an impressionistic claim.

The scientific model must account for the full relational distribution: not only pathological divergence, but complementary difference and the developmental arc toward greater relational depth. Reducing the intent gap is not the only goal — understanding the structure of a healthy, thriving dyad, and showing people the path to one, is equally part of the science.

Crucially, the biological substrate of the intent gap is not fixed. The amygdala–TPJ balance is plastic: socio-cognitive training produces measurable increases in TPJ cortical thickness (Singer, 2025); closed-loop neurofeedback produces lasting functional change via Hebbian co-activation of target circuits (Sitaram et al., 2017); post-interaction inter-brain coupling persists beyond the interaction that created it and predicts future social motivation (Finn et al., 2024). The mechanism for changing the trust deficit is established in the literature. This project tests whether it can be applied at scale, in naturalistic digital communication.

**Why intent classification — not sentiment, not coaching, not therapy?** Sentiment analysis measures surface tone; it does not ask what the sender meant. Relationship coaching changes habits over months; it does not make the biological gap visible in real time. Therapy addresses downstream symptoms; it does not produce a per-message, per-dyad scalar that can be tracked, intervened on, and tested for neural change. Intent classification is the minimal sufficient primitive: the one signal whose failure causes trust breakdown at the belief layer, and the one signal that can be measured continuously, fed back in the cognitive reappraisal window, and used as a training input to the brain's own mentalising circuitry. Everything else follows from getting this signal right.

**This is AI for Science, not science-flavoured product.**

The intent-conditioned language model, fine-tuned from RoBERTa-large with a novel 16-dimensional relational context layer extended by a Soul Document personality context block, is the scientific instrument. The cognitive companion is the delivery mechanism for the intervention. The 60-day pilot is the empirical study. There is, to our knowledge, no dataset of this form in the literature; we will construct and release one openly. The validation chain runs across four levels: computational (does relational context improve intent prediction? — H₁), individual personality context (does structured personality characterisation improve cold-start intent prediction? — H₄), behavioural (does the feedback intervention reduce the gap over 60 days? — H₂), and neural (does sustained feedback produce measurable reorganisation of mentalising circuitry? — H₃). Each level is independently publishable; together they form a coherent scientific programme rather than four disconnected studies.

**12-month deliverables (primary commitment):**
- A 2,000-message annotated neural-pragmatic dataset (dual sender-intent / perceived-intent labels, relational context metadata, κ-validated, 5 relationship types), published on HuggingFace and OpenNeuro
- A trained intent-conditioned language model, RoBERTa-large fine-tuned with a novel 16-dimensional dyadic relational context layer extended by a Soul Document personality context block, with H₁ confirmed or falsified
- A Soul Document intake instrument (v1 spec): 8-question Mode A consumer intake, automatic YAML extraction, user review before activation
- Study 1b (Cold Start A/B, H₄): 100 new NC users randomised 1:1, Soul Document personality context versus no personality context at Day 1; primary outcome is intent prediction accuracy via sender self-annotation
- Soul Document personality context vector added to model architecture and ablation-tested against relational-context-only baseline
- A paper submitted to a peer-reviewed venue reporting dataset, model, and primary results
- *(SHOULD, pending lab partner confirmation)* A 60-day EEG pilot (N = 20–24) testing inter-brain synchrony shift as a neural correlate of the intervention

**ARIA alignment:** The intent-conditioned model and dataset directly advance *Scalable Neural Interfaces*, computational tools that interact with and model human neural processes at scale. The longer-term vision, a consent-based network where intent representations are shared between dyads, maps to *Collective Flourishing*: infrastructure for human understanding at population scale, built on science, not attention extraction. As AI systems absorb more cognitive labour, the quality of human-to-human communication, the trust layer between people, becomes the critical bottleneck for productivity and coordination. The intent gap is its most measurable failure mode. This work builds the scientific foundation for upgrading that layer: not by coaching humans to communicate better, but by proving the biological bottleneck can be changed.

**Why this fellow, now:** I am an AI engineer with production systems experience in NLP and applied ML. The dataset pipeline, annotation tooling, model training infrastructure, Soul Document intake architecture, and browser extension delivery mechanism are not research risks for me, they are solved engineering problems. I build the science infrastructure while embedded in a neuroscience lab that provides EEG equipment, ethics coverage, and experimental paradigm expertise. The combination of builder velocity and neuroscience rigour is precisely what makes this programme executable in 12 months by one fellow.

**The product is already in development.** The Cognitive Companion is not a hypothetical delivery mechanism — it is a parallel product development track with an existing technical specification (v3.0), a Node.js/OpenClaw gateway architecture, and on-device privacy-by-design infrastructure. The fellowship funds the science layer — the dataset, the fine-tuned RoBERTa-large model, the Soul Document intake and conditioning studies, and the EEG validation — that makes the product scientifically defensible; the product is the real-world deployment environment that makes the science ecologically valid. The product's intent classification layer is architected behind an interface from Day 1, designed to swap from a bridge classifier (GPT-4o-mini with SI/PI prompting) to the fine-tuned RoBERTa-large model once H₁ validation is complete. EEG pilot participants in Study 4 are recruited from the beta cohort — the same individuals whose neural change is measured in the lab also generate continuous real-world intent gap data in naturalistic WhatsApp usage, enabling a two-environment validation: controlled lab (EEG) and naturalistic deployment (product) measuring the same intervention simultaneously. Research track obligations and lab commitments are the primary time allocation; the product development track runs in parallel during remaining time and draws on no Encode fellowship funds.

---

## Section 2: Scientific Background & Hypotheses

### 2.1 The Biological Mechanism

Human communication depends on a two-stage neural process. The first stage is rapid and subcortical: the amygdala and related structures process the emotional salience of incoming stimuli via what LeDoux (1996) termed the "low road", a direct thalamo-amygdala pathway that bypasses cortical processing and responds within tens to hundreds of milliseconds. The second stage is slower and cortical: the prefrontal cortex, temporal-parietal junction (TPJ), and associated language areas complete semantic interpretation, pragmatic inference, and social context integration over a longer timescale (200–500ms and beyond).

In face-to-face communication, this timing gap is partially bridged by multimodal cues, facial expression, prosody, gesture, and physical context, that provide rapid disambiguating signals before semantic processing completes. For low-history or neutral-context dyads, this multimodal advantage is real. For high-conflict-history dyads, however, the picture inverts: multimodal cues themselves carry threat-primed valence accumulated through prior conflict (Gottman, 1994). A partner's neutral expression, a familiar tone of voice, a characteristic pause, each can trigger a full amygdala threat cascade when that signal has been repeatedly paired with conflict. In these relationships, face-to-face communication offers no protective advantage over text; it may actively accelerate threat-first parsing rather than constrain it.

Digital text communication strips both the disambiguating cues *and* the threat-primed cues simultaneously. This creates two distinct failure modes: for low-history dyads, the absence of disambiguating signals leaves the amygdala's threat pathway unconstrained; for high-history dyads, the absence of threat-primed signals may reduce flooding, but without any scaffolding for accurate intent inference, the gap persists by a different mechanism. Text also introduces a structural property that face-to-face exchange cannot offer: an asynchronous pause between message receipt and response. This temporal gap is a cognitive reappraisal window (Gross, 1998; Ochsner & Gross, 2005), one of the most robust emotion-regulation mechanisms available. The Cognitive Companion browser extension is architecturally positioned to fill that window with mentalising scaffolding at precisely the moment when threat rehearsal would otherwise occur. The delivery medium is not a limitation of scope. It is a designed intervention point.

*Note on extrapolation:* The latency figures and dual-pathway architecture derive from research on visual and auditory threat stimuli in controlled laboratory settings (LeDoux, 1996; Öhman & Mineka, 2001; Adolphs, 2002). Their direct application to digital text message reading is a theoretical extrapolation, and one of the core assumptions this project is designed to test empirically.

### 2.2 Mentalising and the TPJ

Successful communication requires not only understanding the semantic content of a message but attributing the correct mental state, intent, belief, desire, to the sender. This process, variously termed mentalising, theory of mind, or social cognition, is strongly associated with the TPJ, medial prefrontal cortex, and posterior superior temporal sulcus (Saxe & Kanwisher, 2003; Frith & Frith, 2006). TPJ activation is specifically associated with the attribution of mental states to others that differ from one's own, precisely the cognitive operation required to override a threat-parsed reception of an ambiguous message with an intent-informed interpretation.

The Cognitive Companion is designed as a tool that externalises and scaffolds this TPJ-mediated operation: it shows the receiver the most probable intent distribution for the message they just read, conditioned on what it knows about the sender and their shared relational history. We hypothesise that repeated exposure to this externally-provided intent signal, analogous to the corrective feedback in attentional training paradigms (Davidson & Lutz, 2008), will, over 60 days, measurably shift the balance between amygdala-dominant and TPJ-mediated processing of emotionally ambiguous messages. This is H₃, exploratory, not pre-registered, but grounded in the neuroplasticity literature and designed to be measurable.

### 2.2.1 A Scientific Prediction: Elevated Intent Gap in Neurodivergent Dyads

A secondary scientific prediction follows directly from the biological mechanism. If intent gap arises from differential signal processing, specifically from the asymmetry between subcortical threat-tagging and cortical mentalising, then it should be systematically elevated in neurodivergent dyads. For autistic individuals, the social inference burden on TPJ is well-documented: mentalising circuitry is recruited differently, with greater effort and less automaticity in attributing mental states to others (Lombardo et al., 2011; Frith & Frith, 2006). For individuals with ADHD, attentional load during message reading may reduce the cognitive resources available for pragmatic inference. In both cases, the mechanism predicts a *wider* intent gap on average, not a deficit of communicative intent, but a structural asymmetry in pragmatic signal processing that the Companion is specifically designed to scaffold.

This is not an inclusion gesture. It is a falsifiable prediction. Study 2 (annotation and model training) will include a pre-registered secondary analysis of intent gap scores stratified by neurodivergent/neurotypical annotator pairing, specifically testing whether the JS-divergence between SI and PI distributions is significantly larger when annotator pairs include a neurodiverse rater. Neurodiverse annotators are recruited separately via autism/ADHD community groups; separate κ values are computed on the neurodiverse-authored message subset. If the prediction is confirmed, the Companion is not merely accessible to neurodiverse users, it is *most scientifically relevant* to them. This extends the *Collective Flourishing* impact pathway beyond generic diversity: it targets the population where miscommunication has the sharpest biological basis and where closing the intent gap has the highest individual and relational stakes.

### 2.3 Dyadic History as Primary Signal

A fundamental limitation of existing intent and sentiment models is their treatment of messages as contextually isolated. The same message, "Fine, do whatever you want", has a qualitatively different intent distribution when it comes from:
- A stranger completing an online transaction
- A colleague under deadline pressure
- A close friend in a long-running disagreement
- A partner of five years in the third day of a conflict

No existing NLP system conditions its prediction on this relational context. The scientific novelty of this project is the explicit modelling of dyadic relational history as a first-class input to intent prediction, and the empirical test of whether this conditioning produces measurably better predictions than message-content-only models.

Critically, relational history also defines what *good* looks like — and that definition is dyad-relative, not universal. A complementary dyad (one high-I1 connection-seeking, one high-I6 request-making) may sustain high JS-divergence in individual turns while maintaining high repair rate, high reciprocity, and rising trust scores — a stable, healthy pattern that a gap-only model would misclassify as dysfunction. The model's success metric is therefore not "minimise divergence globally" but "is this dyad's intent pattern producing the outcomes they want?" A flourishing dyad does not need repair — it needs a map of its next developmental stage: the intent categories rarely used, the emotional vocabulary not yet discovered, the depth not yet reached. Relational history is not only the signal for decoding messages. It is the lens through which growth becomes visible.

### 2.4 Inter-Brain Synchrony as Neural Outcome Measure

Hasson et al. (2012) demonstrated that neural coupling between speaker and listener, measured via fMRI, is a strong predictor of successful communication, with greater temporal synchrony associated with better comprehension and mutual understanding. More recent work has replicated and extended these findings using EEG hyperscanning paradigms (Pérez et al., 2017; Dikker et al., 2017), demonstrating that theta-band inter-brain phase synchrony (IBS) during joint cognitive tasks is measurable, reproducible, and sensitive to communication quality.

We select theta-band IBS as our primary neural outcome measure for the 60-day pilot for three reasons: (1) it is measurable with EEG rather than fMRI, making it accessible within the lab partnership budget; (2) it is sensitive to communicative success and attentional coordination; and (3) a pre/post within-subjects design is sufficiently powered with N = 20–24 participants for a medium effect size.

### 2.5 Individual Personality Context as Complementary Signal

The existing model conditions on `P(intent | message, dyadic_relational_history)`. This is powerful — but it models *communication patterns*, not *the person behind them*. Critically, dyadic history is unavailable for new users (the cold-start problem) and is structurally silent on stable personality-level intent architecture: how a person characteristically processes conflict, what their risk tolerance is, how they signal stress through communication behaviour. Two people can have identical message histories and entirely different intent architectures:

- Same words, different risk tolerance
- Same silence, different conflict response pattern
- Same "I'm fine", different suppression style

Without a personality layer, the model performs relational pattern matching. With a structured personality context, it performs person-aware intent modelling — the same distinction as knowing someone's message history versus genuinely knowing them.

The Soul Document addresses this by encoding a structured three-layer personality context: Identity Core (ranked values, non-negotiables, self-concept), Decision Architecture Lite (risk profile, dominant heuristic, stress response pattern), and Narrative Library (5–10 manually-annotated life stories, RAG-retrieved at inference time). This is not a product onboarding feature. It is a personality characterisation instrument designed to enable a new class of scientific question: how does stable individual personality context moderate the intent gap?

**Scientific grounding:** Twin-2K-500 (Xu et al., 2024) demonstrated that interview-derived personality data improves LLM behavioural prediction more than fine-tuning on interaction history alone. The Soul Document is a structured adaptation of this finding to intent prediction in relational communication contexts. Rather than treating personality as an implicit feature to be learned from behavioural traces, the Soul Document makes personality context explicit, structured, and queryable — a methodological choice that enables clean ablation of its contribution.

The Narrative Library in particular represents a scientifically novel conditioning approach: it provides episodic grounding for intent inference — not "this person is introverted" but "this is the specific experience that shaped how this person responds to institutional conflict." Episodic memory as intent prior. The mechanism has direct theoretical precedent in autobiographical memory research (Conway & Pleydell-Pearce, 2000): episodic self-defining memories carry stable emotional and behavioural meaning that shapes how individuals generate and interpret communicative acts. Using manually-annotated life stories as a retrieval corpus for intent conditioning extends this established cognitive science finding into a computational architecture.

**New hypothesis H₄ (Primary, Soul Document study):** A RoBERTa-large intent model conditioned on both the 16-dimensional dyadic relational context vector and the Soul Document personality context block will achieve significantly higher intent prediction accuracy at Day 1 (cold start) than the dyadic-context-only model (Condition A), with the gap narrowing as dyadic history accumulates over four weeks. This hypothesis is tested in Study 1b (Section 3.5) using sender self-annotation as the ground-truth measure of intent. We hypothesise that the personality context effect is largest at Week 1 — before relational history is rich enough to carry the inference — and that the two signals become complementary rather than redundant as history accumulates.

### 2.6 Formal Hypotheses

**H₁, Behavioural / Computational (Primary):**
A RoBERTa-large model fine-tuned on perceived-intent prediction, with a 16-dimensional dyadic relational context vector concatenated to the [CLS] token representation, will achieve significantly higher macro-averaged F1 on perceived-intent (PI) prediction for emotionally ambiguous messages than an ablated message-only baseline, on a held-out 400-message test set (paired t-test, α = 0.05, minimum effect size Cohen's d ≥ 0.3).

*Failure condition:* If H₁ is not confirmed, dyadic relational history does not significantly improve intent prediction at this scale and label granularity. This is a publishable null result with clear theoretical implications, and the project pivots to characterising *where* and *why* relational context fails to add signal.

**H₂, Behavioural (Secondary):**
Participants using the Cognitive Companion browser extension for 60 days will show a significant reduction in intent gap score compared to their own Day 0 baseline, indicating that closed-loop intent feedback changes how people compose emotionally ambiguous messages (within-subjects, paired Wilcoxon signed-rank test, α = 0.05). *Operationalisation note:* In real-world usage, ground-truth sender intent labels are unavailable for natural messages. The gap score is therefore computed as JS-divergence(SI_model, PI_model), where SI_model (the model's sender-intent head output) serves as a proxy for the sender's communicative intent. The 60-day trajectory measures whether users compose messages whose model-estimated SI and PI distributions converge over time. This proxy assumption is explicit and defensible: the SI head is trained on annotator-labelled sender perspectives and captures the pragmatically intended meaning, even absent direct sender confirmation.

**H₃, Neural (Exploratory, EEG pilot):**
H₃ is the most exploratory hypothesis in this programme: that 60 days of closed-loop intent feedback is sufficient to produce measurable reorganisation of the neural balance between threat and mentalising circuitry. If confirmed, this would suggest that a digital intervention may contribute to lasting reorganisation of how the brain processes communicative intent — a neuroplastic change, not merely a behavioural one. That is the scientific claim this project is designed to test.

The proposed mechanism is a four-step cascade, each step grounded in established neuroscience. *Step 1:* the intent distribution display occupies the cognitive reappraisal window (Gross, 1998), activating lateral PFC and suppressing the amygdala threat cascade before a response is composed. *Step 2:* when the model's displayed intent matches the sender's actual intent — the experience of "being understood" — the nucleus accumbens releases oxytocin and dopamine, reinforcing the trust-confirming neural state (Zak et al., 2017). *Step 3:* repeated correct intent scaffolding strengthens TPJ activation via Hebbian co-activation — the same closed-loop mechanism demonstrated in neurofeedback paradigms to produce lasting functional change in target circuits (Sitaram et al., 2017). *Step 4:* across 60 days, sustained high-synchrony inter-dyadic states produce persistent inter-brain coupling in the right IFG and dorsomedial PFC — coupling that outlasts the individual interactions and raises the dyad's baseline mentalising capacity (Finn et al., 2024). The delivery vehicle is novel. The neuroscience is not.

Operationally: participants who complete the 60-day intervention will show measurably increased theta-band inter-brain phase synchrony (IBS) during a standardised dyadic ambiguous-message reading task at Day 60 compared to Day 0 baseline, indicating that the intervention shifts neural coupling toward the pattern associated with successful mentalising-mediated communication (Hasson et al., 2012). Pre-registered analysis for IBS only; ERP analysis is exploratory and reported as preliminary findings.

**H₄, Computational / Behavioural (Soul Document, Primary):**
A RoBERTa-large intent model conditioned on both the 16-dimensional dyadic relational context vector and the Soul Document personality context block will achieve significantly higher intent prediction accuracy at Day 1 (cold start) than the dyadic-context-only model, with accuracy measured via sender self-annotation (one-tailed t-test, α = 0.05, power = 0.80). We further hypothesise that the Soul Document advantage narrows as dyadic history accumulates over four weeks, consistent with the interpretation that personality context and relational history are complementary signals whose relative contributions shift across the user lifecycle.

**On dataset scale and label granularity:**
2,000 messages and 8 intent categories may appear modest for a multi-class NLP task. The justification is twofold. First, the primary test (H₁) is a *relative* comparison, does adding relational context improve PI prediction?, not an absolute accuracy benchmark. For a within-subjects ablation on a fine-tuned RoBERTa-large, 1,600 training examples (80% of 2,000) is sufficient to detect a medium effect (d ≥ 0.3) in the held-out condition contrast. Second, the 60% ambiguous-valence oversampling ensures the most scientifically critical messages are well-represented; the I7 (giving information) category, which generates few ambiguous cases, is intentionally underrepresented. This is an appropriately scaled first test of the dyadic conditioning hypothesis, not a production training run.

---

## Section 3: Methods & Work Plan

### 3.1 Dataset Creation: Study 1 (Months 1–3)

**Objective:** Construct the first neural-pragmatic dataset conditioning intent annotation on dyadic relational history, with dual sender-intent / perceived-intent labels and validated inter-rater reliability.

**Sampling procedure:**
- 2,000 dyadic text messages in English, drawn from 5 relationship types: (1) romantic partners, (2) parent-child, (3) close friends, (4) community/social groups, (5) professional colleagues
- 4 emotional valence levels: high positive, high negative, ambiguous positive, ambiguous negative, with deliberate oversampling of ambiguous-valence messages (target: 60% of dataset), as these are the scientifically and practically critical cases
- **Sources (three-stream strategy, no participant submission required):**

| Source | Target | Method |
|--------|--------|--------|
| **Relabelled public datasets** — DailyDialog (Li et al., 2017) and EmpatheticDialogues (Rashkin et al., 2019) | ~700 messages | Select messages meeting ambiguity criteria; add synthetic relational context metadata; run full 5-annotator SI/PI protocol |
| **Researcher-constructed stimuli** | ~600 messages | Write messages targeting specific I1–I8 × relationship type × valence cells; reviewed by 3 independent raters before entering annotation pool; forms the controlled EEG/fMRI stimulus set |
| **LLM-assisted synthetic generation** (GPT-4o / Claude, human-reviewed) | ~700 messages | Structured prompts specifying relationship type, duration, valence, target SI class, and target PI divergence; mandatory 2-rater human review gate before inclusion; ~20–30% rejection rate budgeted |

This three-source strategy is a methodological strength, not a compromise. Participant-submitted naturalistic messages are systematically biased toward non-conflict content (people self-censor submissions), making the 60% ambiguous-valence oversampling target difficult to achieve reliably. Researcher-constructed and synthetic messages allow precise control over the label-space coverage that naturalistic collection cannot guarantee. Critically, this design produces a stimulus set with the controlled stimulus properties required for both EEG (Year 1) and fMRI (Year 2) paradigms — ambiguity level, emotional valence, and relational context are fixed by construction, not inferred post-hoc. LLM-assisted synthetic data generation with human review gate is now an established methodology for NLP annotation: Gilardi et al. (2023) demonstrated GPT-4 outperforms crowd-workers on zero-shot text annotation; Møller et al. (2023) showed LLM-generated data achieves annotation-quality parity for emotion and intent tasks when reviewed by domain experts. The human review gate (2 independent raters per synthetic message, ~20–30% rejection rate budgeted) satisfies the quality threshold required for κ-validated downstream annotation.

**Intent label space, 8 categories (I1–I8):**

| ID | Category | Definition |
|----|----------|------------|
| I1 | Seeking connection | Primary goal is relational proximity; content is secondary |
| I2 | Expressing concern | Communicates worry about the receiver's state or wellbeing |
| I3 | Setting a boundary | Signals a limit on behaviour, time, or emotional availability |
| I4 | Seeking validation | Requests acknowledgement or agreement, not action |
| I5 | Expressing frustration | Communicates emotional state as primary payload |
| I6 | Making a request | Clear instrumental ask for action or change |
| I7 | Giving information | Neutral informational content with low emotional valence |
| I8 | Pattern: chronic self-interest | *Pattern-level only*, detected across message history, not single messages |

**Schema derivation and literature grounding:**
The I1–I8 schema is grounded in three converging literature streams, and explicitly extends each in the direction required by this project. Searle's (1976) taxonomy of illocutionary acts provides the transactional backbone: I6 (making a request) maps to his *directives*; I7 (giving information) to *assertives*; I3 (setting a boundary) to *commissives*. The DailyDialog benchmark (Li et al., 2017) — the most widely used NLP intent dataset — uses four categories (Inform, Question, Directive, Commissive) that cover these same transactional intents, confirming their annotator reliability. However, DailyDialog was designed for task-oriented daily conversation: its schema entirely omits the affiliative and relational intents (I1, I2, I4) where the SI/PI gap is largest. Welivita & Pu's (2020) taxonomy of empathetic *response* intents — the closest NLP prior — identifies sympathising and consoling as frequent categories, which partially map to I2 and I5; but their schema models the *listener's reply*, not the *sender's initiating intent*. The I1–I8 schema is the missing sender-side counterpart: it models what the originating message is trying to accomplish, not what a compassionate response should do. I4 (seeking validation) and I8 (pattern: chronic self-interest) have no direct NLP precedent — I4 is grounded in Goffman's (1967) face-work theory; I8 in Gottman's (1994) cascade model of relational dissolution. The schema is designed to be minimal (7 single-message categories + 1 pattern-level), annotator-distinguishable (κ gate in Month 1), and exhaustive for the emotionally ambiguous message space where intent gaps are scientifically and clinically significant. If the κ pilot reveals systematic confusion between adjacent categories (most likely I1/I4 or I2/I3), the schema will be collapsed accordingly before full annotation begins.

**Annotation constructs, two separate labels per message:**
- **Sender intent (SI):** What did the writer most likely intend to communicate? (Annotator takes sender perspective, given relational context)
- **Perceived intent (PI):** What would a reasonable receiver most likely parse from this message in the given relational context? (Annotator takes receiver perspective)

The *intent gap score*, the core product and scientific metric, is the Jensen-Shannon divergence between P(SI) and P(PI): JS-divergence(P(SI), P(PI)). This is the measurable distance between communicative intent and communicative reception.

**Relational context provided to annotators:** relationship type, approximate duration, brief description of recent interaction valence (positive / neutral / negative / conflictual), no identifying information.

**Annotator recruitment and cost:**
Annotators recruited via Prolific Academic, targeting UK-based participants with demonstrated English proficiency and diverse cultural backgrounds (minimum 3 distinct backgrounds across the 5-annotator pool). Estimated task: ~10 minutes per message (SI + PI label + confidence rating); 2,000 messages × 5 annotators × 2 passes = ~20,000 annotation tasks. Estimated cost at £0.10–0.15 per task: **£2,000–3,000 total annotation budget**, to be confirmed against Encode funding allocation in Month 1. Neurodiverse annotators recruited separately via autism/ADHD community groups for the neurodiverse message subset.

**Annotation protocol:**
- 5 independent annotators per message
- Annotate SI and PI separately (two passes); annotators blind to each other
- "Ambiguous / I don't know" is a valid response, not forced into the schema
- Cultural background recorded as annotator metadata; minimum 3 distinct UK cultural backgrounds in annotator pool
- Neurodiverse-authored messages explicitly included; separate κ computed on neurodiverse subset

**Inter-rater reliability:**
- Pilot: 20 messages, 5 annotators → compute κ (SI) and κ (PI) separately
- **Gate:** If either κ < 0.70 after two adjudication rounds → pause, redesign schema, re-pilot
- **Target:** Cohen's κ > 0.70 on both SI and PI before full annotation begins
- Per-category κ reported; categories with high cross-cultural variance flagged with wider model confidence intervals

**Output:** 2,000-message annotated dataset with SI/PI dual labels, relational context metadata, per-category κ scores, cultural and neurodiverse subset analyses. Published on HuggingFace (model training) and OpenNeuro (EEG-linked subset).

---

### 3.2 Intent-Conditioned Model Training & H₁ Validation: Study 2 (Months 3–6)

**Base model:** RoBERTa-large (355M parameters, Liu et al., 2019), chosen for four principled reasons. First, the task is *classification* — assigning a probability distribution over intent categories given a message and context vector — for which encoder-only architectures are purpose-built; decoder-only LLMs (e.g. Llama, Mistral) are generative and require prompt engineering, output parsing, and calibration overhead with no classification accuracy benefit. Second, RoBERTa-large has an established Brain-Score Language benchmark baseline (Schrimpf et al., 2021), making the Study 3 neural alignment comparison directly interpretable as a delta over a known reference; models without prior Brain-Score entries would require running the full benchmark from scratch. Third, RoBERTa-large fine-tuning on an A100 fits within the stated $500–1,000 compute budget; 7B+ parameter instruction-tuned models cost 10–50× more per run. Fourth, RoBERTa-large consistently leads GLUE and SuperGLUE on pragmatic inference tasks (NLI, MNLI, RTE) — the closest existing benchmarks to intent classification. *DeBERTa-v3-large* is the strongest alternative encoder and scores marginally higher on some benchmarks; it will be added as Condition D in the ablation if compute budget permits, with results reported as a secondary comparison.

**Architecture modification:**
- Relational context vector: 16 dimensions encoding relationship type (5-category one-hot), duration (continuous, log-scaled), recent interaction valence (−1 to +1), message frequency (continuous), and dyad-level intent gap history (rolling 14-day mean gap score)
- Context vector concatenated to the [CLS] token representation before the classification head
- **Soul Document personality context block:** at inference time, the Soul-to-Prompt Adapter converts the user's YAML layers into a structured 600–900 token context block, prepended to the prompt ahead of the relational context vector (see Section 3.3b and Appendix B for full architecture specification)
- Two separate fine-tuning runs: one for SI prediction, one for PI prediction
- Classification head: 7-way softmax over I1–I7 (I8 excluded from single-message classification, detected at pattern level only)

**Extended experimental conditions for H₁/H₄ ablation:**
- **Condition A (relational context only):** RoBERTa-large + 16-dim dyadic relational context vector, no Soul Document
- **Condition B (baseline, no context):** RoBERTa-large without any context vector (message content only)
- **Condition C (surface baseline):** RoBERTa-base fine-tuned for sentiment classification (represents existing tool capability)
- **Condition D (full model):** RoBERTa-large + 16-dim dyadic relational context vector + Soul Document personality context block

The H₁ test is the contrast Condition A versus Condition B. The H₄ test is the contrast Condition D versus Condition A at Day 1 (cold start), with the trajectory tracked over four weeks as dyadic history accumulates. This design enables clean attribution of accuracy gains: Condition B establishes the message-only floor; Condition A establishes the relational conditioning ceiling; Condition D establishes the incremental contribution of personality context, specifically under cold-start conditions where Condition A has no history to condition on.

**Training:** 3 runs per condition × 5 epochs; AdamW optimiser; learning rate sweep (1e-5, 2e-5, 3e-5); early stopping on validation loss. A100 GPU on Lambda Labs.

**Evaluation:**
- Macro-averaged F1 on 400-message held-out test set (ambiguous-valence subset prioritised for primary analysis)
- Human majority-vote baseline: plurality vote of 5 annotators as ground truth; human-parity gap reported
- **Primary metric (H₁):** ΔF1 (Condition A − Condition B) on PI prediction for ambiguous-valence messages; paired t-test, α = 0.05, minimum d ≥ 0.3
- **Primary metric (H₄):** ΔAccuracy (Condition D − Condition A) at Week 1, measured via sender self-annotation; one-tailed t-test, α = 0.05 (see Section 3.3b)
- **Secondary metric:** Expected Calibration Error (ECE), a well-calibrated intent distribution is as scientifically important as high accuracy; overconfident classification is a failure mode

**Compute budget:**
- Demo / prototype (DistilBERT, Colab Pro): ~$20–50
- Full RoBERTa-large fine-tuning (3 runs × 5 epochs, A100): ~$150–300
- Ablation studies + hyperparameter sweeps: ~$300–600
- **Total ML compute budget: ~$500–1,000** (to be confirmed against Encode funding allocation)

**Open-source release:** Fine-tuned model weights, fine-tuning code, and evaluation harness released on HuggingFace under Apache 2.0 at Month 5/6.

---

### 3.3 Brain-Score Neural Plausibility Validation: Study 3 (Months 6–8) *(SHOULD)*

**Objective:** Validate that the intent model's internal representations are neurally plausible, that fine-tuning on pragmatic intent prediction enhances, rather than degrades, alignment with human language-selective neural responses.

**Method:**
- Submit to MIT Brain-Score Language benchmark (Schrimpf et al., 2021)
- Target benchmarks: **Pereira2018** (fMRI, language comprehension, N=10), **Fedorenko2016** (fMRI, localiser paradigm), **Blank2014** (fMRI, naturalistic reading)
- Adaptation: extract hidden-state activations at each transformer layer; fit linear regression probes to fMRI ROI activations in language-selective cortex (IFG, aMTG, pMTG, PostTemp, AnGyd per Fedorenko et al.)
- Report Brain-Score per benchmark vs. published RoBERTa-base baseline

**Interpretive frame:** If the intent model scores *above* RoBERTa-base on language-selective neural alignment, this suggests pragmatic fine-tuning enhances the model's similarity to human neural language processing, a meaningful scientific finding. If it scores *below*, this suggests a tension between pragmatic optimisation and neural plausibility, equally publishable and theoretically informative.

*This study is a SHOULD deliverable, it does not gate H₁. It provides a second, independent scientific line of evidence. It requires approximately 2 weeks of engineering work post-training.*

---

### 3.3b Soul Document Intake Protocol: Study 1b Design Instrument

The Soul Document intake is a scientific instrument whose function is to populate the three-layer personality context representation described in Section 2.5. It is not a user onboarding feature. Its scientific purpose is to provide the model with structured personality context that enables intent prediction under cold-start conditions — before dyadic message history is rich enough to carry the inference.

**Mode A: Consumer Intake (10–15 minutes)**

A guided conversational UI asks 8 questions across the three layers and extracts structured YAML automatically. The user reviews and edits the output before activation. This is the standard protocol for all Study 1b participants.

**8 Core Questions and Layer Mapping:**

```
Layer 1 — Identity Core (Q1–Q3, ~5 min)
Q1: "What's something you believe that most people you know disagree with?"
    → Extracts: values_ranked, paradoxes, self_concept

Q2: "What's a line you've never crossed, even when it would have made things easier?"
    → Extracts: non_negotiables

Q3: "How would someone who knows you very well describe you — including the
    parts you find hard to admit?"
    → Extracts: self_concept, paradoxes

Layer 2 — Decision Architecture Lite (Q4–Q5, ~5 min)
Q4: "When you're genuinely upset with someone close to you, what does your
    behaviour look like from the outside?"
    → Extracts: stress_response, conflict_response

Q5: "What's a rule you apply to almost every difficult decision you make?"
    → Extracts: dominant_heuristic, risk_profile

Layer 3 — Narrative Library (Q6–Q8, ~5 min)
Q6: "Tell me about a time you made a decision that still feels right, even
    though it cost you something."
    → Extracts: story (themes: values_over_comfort, decision_pattern)

Q7: "Describe a relationship — work, personal, or family — that taught you
    something fundamental about how you operate."
    → Extracts: story (themes: relational_pattern, lesson_extracted)

Q8: "What's an experience that changed how you think about conflict or repair?"
    → Extracts: story (themes: conflict_response, repair_pattern)
```

**Output:** A three-layer Soul Document with confidence flags per field. Low-confidence fields are surfaced to the user for manual correction before activation. Minimum viable document for Study 1b inclusion: Layer 1 and Layer 2 fully populated; Layer 3 requires at least 2 usable stories.

**Story tagging in the Study 1b cohort — manual annotation by researcher/RA.** Automated NLP tagging is a v2 problem. The v1 study design intentionally isolates the question: does structured personality context (manually curated to the highest quality achievable in Year 1) improve intent prediction under cold-start conditions? Automated extraction is a separate, subsequent hypothesis. Conflating the two questions in v1 would prevent clean attribution of any observed effect. In Study 1b, all story themes and retrieval tags are assigned by a researcher or research assistant following a standardised annotation protocol, blind to group assignment.

**Mode B: Clinician-Assisted Intake (30 minutes)**

Mode B uses a four-phase biographical interview protocol with clinician-assisted narrative elicitation:

```
Phase 1: Formation (5 min)       → Layer 1: Identity Core (rich version)
Phase 2: Decision Architecture   → Layer 2: Decision Architecture Lite
         (10 min)
Phase 3: Relational Patterns     → Layer 3: Narrative Library (5-10 stories)
         (10 min)
Phase 4: Temporal Anchor (5 min) → Future: Temporal context seed (north-star only)
```

The clinician helps the user articulate stories they may not have surfaced on their own — particularly for conflict, trust repair, and relational patterns that Mode A's conversational UI may not reach. Mode B advantage: richer narrative library (5–10 stories versus 2–3 from Mode A), higher confidence scores on all layers, and reduced risk of idealised self-report through clinician probing.

**Mode B is explicitly a channel pilot contingent on professional partnership.** It is not a Year 1 dependency and is not on the critical path for Study 1b. Mode B will be developed only if a professional partner (therapist practice, coaching platform, or clinical pilot site) is secured during the fellowship year. This constraint is a methodological choice, not a resource limitation: keeping Study 1b focused on Mode A ensures that the H₄ test is a clean measurement of whether manually-curated personality context improves cold-start accuracy, not a confounded comparison between different intake modalities.

---

### 3.4 60-Day Pilot & EEG Validation: Study 4 (Months 7–11) *(SHOULD, requires lab partner)*

**Objective:** Test H₂ (behavioural) and H₃ (neural), does 60 days of intent feedback produce measurable behavioural and neural shifts?

**Design:** Within-subjects pre/post; participants serve as their own controls.

**Participants:**
- N = 20–24 (12 dyadic pairs): couples or close friends, ≥6 months established relationship, English-speaking, smartphone users
- Recruited via lab partner's existing participant pool and university mailing lists
- Powered for medium effect size (d = 0.5, 80% power, α = 0.05, within-subjects t-test)

**Intervention:** 60-day use of the Cognitive Companion in naturalistic digital messaging contexts. The Companion is not a prototype built for this study — it is a parallel commercial product development track (technical specification v3.0, Node.js/OpenClaw architecture, on-device privacy-by-design, AES-256 encrypted local storage, no cloud message transit) with its own beta programme running concurrently with the fellowship. This means the intervention instrument is production-grade, consent-architected, and ecologically valid from Day 1 of the pilot rather than a lab-constructed approximation. EEG pilot participants are recruited from the Cognitive Companion beta cohort, creating a direct bridge between naturalistic product usage data (continuous intent gap scores from real WhatsApp messaging) and controlled neural measurement (IBS and ERP in the lab). H₂ is therefore tested in two environments simultaneously: behaviourally in the wild (product metric, JS-divergence trajectory over 60 days) and neurally in the lab (IBS shift at Day 60). The product's intent classification layer is architected behind an abstracted interface designed to swap from a bridge classifier to the fine-tuned RoBERTa-large model at Month 6–7, ensuring continuity of measurement across the model transition. No forced correction; intent distribution feedback is informational, not prescriptive.

**EEG sessions:** Day 0 (baseline) and Day 60 (post-intervention) at lab partner facility.
- Equipment: 64-channel active EEG, standard 10-20 placement
- Task: standardised dyadic ambiguous-message reading, both participants simultaneously read 40 emotionally ambiguous messages; rate their perceived intent (1–7 scale per intent category); EEG recorded throughout
- Ambiguous and disambiguated (context-provided) message blocks, within-session contrast
- **Stimulus set:** The 40 EEG messages are drawn exclusively from the researcher-constructed subset of the Study 1 dataset, selected to span all five relationship types and all four valence levels with known SI/PI divergence properties. Researcher-constructed stimuli are used (not synthetic or relabelled messages) because full control over ambiguity level, emotional valence, and relational context framing is required for the within-session contrast and for comparability with the Year 2 fMRI paradigm.

**Primary EEG analysis (pre-registered):**
- Theta-band (4–8 Hz) inter-brain phase synchrony (IBS) between dyad members during ambiguous-message reading blocks
- Pre vs. post comparison: paired Wilcoxon signed-rank test on IBS values; effect size r reported
- Secondary: correlation between individual intent gap score decline (product metric, Days 1–60) and IBS increase, tests whether the product intervention and neural shift co-vary

**Exploratory EEG analysis (not pre-registered):**
- ERP analysis: N2 and P3 component latency on individual ambiguous-message trials, tests whether the intervention shifts the temporal balance between threat-rapid and mentalising-slower processing
- Reported as preliminary findings with appropriate statistical caveats

**Behavioural measures (continuous, 60 days):**
- Intent gap score per sent message (product metric, JS-divergence, automated)
- 7-day streak retention and daily active usage
- Self-reported relationship quality (Perceived Relationship Quality Components scale, PRQC, Fletcher et al., 2000) at baseline, Day 30, Day 60
- NPS at Day 60

**Reflection journal instrument (event-contingent + weekly):**
A lightweight structured reflection journal provides two data streams unavailable from passive classification alone. *Triggered micro-prompt* (fires after high-JS-divergence exchange, ~3 minutes): (1) "What were you trying to communicate in that exchange?" — a first-person ground-truth sender intent (SI) label using the Ickes (1993) empathic accuracy paradigm, directly validating the classifier's SI inference against self-report; (2) "What emotion were you feeling when you sent it?" — ESM-style affective capture for the individual self-model; (3) "Did they understand what you meant?" — perceived empathic accuracy, calibrating the JS-divergence score. *Weekly narrative reflection* (~7 minutes, scheduled): (1) "What communication pattern do you most want to change?" — operationalises the Higgins (1987) actual/ideal self gap, the core self-model signal for the Mirror view; (2) "Describe a moment this week when you felt most understood, and one when you felt most misunderstood" — McAdams (2013) turning-point elicitation, populating the Relationship Digital Twin with episodic dyadic memory; (3) the app surfaces the week's highest-divergence message and asks "what was your actual intent here?" — retrospective Ickes labelling, generating additional SI ground-truth training data.

The journal adds a second neuroplastic mechanism operating in consolidation time: retrospective emotional processing re-opens the memory trace of a high-divergence exchange and allows cortical re-encoding in a non-threat state (McGaugh, 2000). This is a second Hebbian co-activation event on the same stimulus — the TPJ fires again, calmly, reinforcing the mentalising circuit independently of the in-the-moment reappraisal window effect. Semi-structured prompts outperform free writing for metacognitive development (Pavlacic et al., 2019; Reflective Practice, 2020); event-contingent triggering outperforms scheduled prompts for ecological validity (Fritz et al., 2024). Total participant burden: approximately 15–20 minutes per week at moderate divergence levels, scaling naturally with relationship friction. Prompts are skippable without penalty; the instrument is analysed as an exploratory secondary measure.

*fMRI is explicitly out of scope for Year 1. Regional activation analysis (TPJ vs. amygdala) is a Year 2 extension, contingent on Year 1 EEG results.*

**Neural data pathway: how EEG and fMRI data are used across the programme**

The dataset, model, and neural studies are not independent work streams — they form a single connected scientific instrument across three pathways:

*Pathway 1 — EEG stimulus set (Year 1, Study 4):*
The 40-message researcher-constructed stimulus set serves as controlled input for both Day 0 and Day 60 EEG sessions. Each message has known SI class, PI class, JS-divergence score, relationship type, and valence level from Study 1 annotation. This means EEG responses (IBS, N2/P3 latency) can be analysed not just pre/post but *as a function of intent gap magnitude* — messages with higher JS-divergence at annotation should elicit stronger amygdala-dominant ERP signatures at Day 0, and this relationship should weaken at Day 60 if H₃ holds. This within-stimulus-set analysis is an additional pre-registered secondary analysis that connects the NLP metric directly to the neural response.

*Pathway 2 — Brain-Score fMRI alignment (Year 1, Study 3):*
The trained RoBERTa-large intent model is submitted to the MIT Brain-Score Language benchmark (Schrimpf et al., 2021), which evaluates model hidden-state alignment against existing published fMRI datasets (Pereira2018, Fedorenko2016, Blank2014) using linear regression probes on language-selective cortex ROIs (IFG, aMTG, pMTG, PostTemp, AnGyd). No new fMRI data is collected — the comparison is against existing neuroimaging benchmarks. The scientific question: does fine-tuning for pragmatic intent prediction enhance or degrade alignment with human neural language processing? If the intent model scores above RoBERTa-base on language-selective alignment, this provides independent evidence that the model's representations are moving toward human-like pragmatic inference, not away from it.

*Pathway 3 — Year 2 fMRI extension (contingent on Year 1 EEG confirmation):*
If H₃ is confirmed (IBS increase at Day 60), the Year 2 study replaces EEG with fMRI to localise the neural change to specific ROIs — specifically testing whether TPJ BOLD activation increases and amygdala BOLD activation decreases in response to the same researcher-constructed stimulus set used in Year 1. The stimulus set design is held constant across years precisely to enable this direct comparison: the same 40 messages, the same relational context framings, the same ambiguity levels — now viewed under fMRI rather than EEG. Year 2 fMRI data would be uploaded to OpenNeuro alongside the Year 1 EEG-linked dataset subset, creating a multi-modal neural-pragmatic corpus linked to the same underlying intent-annotated messages.

---

### 3.5 12-Month Work Plan

**Research track:**

| Period | Primary Activity | Key Output | Tier |
|--------|-----------------|------------|------|
| **Month 1** | κ pilot (20 msgs, 5 annotators); annotation tooling build; ethics application submitted with lab partner; taxonomy unification with product classifier schema; Study 1b recruitment begins (100 new NC users, stratified randomisation 1:1 by age and relationship status) | Annotation protocol validated; ethics in review; unified SI/PI/intent schema; Study 1b cohort enrolled | MUST |
| **Month 1–3** | Full 2,000-message annotation; dataset QA; small online behavioural validation study (H₂ probe, N=50, online, no EEG); Study 1b Group B completes Mode A Soul Document intake; data collection begins for both Study 1b groups | Annotated dataset v1.0; early H₁ signal; Study 1b data stream active | MUST |
| **Month 1–4** | Study 1b data collection: Group A (standard NC, no Soul Document) and Group B (NC + Soul v1, Mode A intake at Day 1); 2× weekly sender self-annotation protocol (3 ambiguous messages per session, "What did you mean?" + 1–5 accuracy rating); engagement tracking (messages sent, sessions/week, days active) as ANCOVA covariate | Study 1b primary dataset (intent prediction accuracy by group × week) | MUST |
| **Month 3–6** | RoBERTa-large fine-tuning; ablation studies (Conditions A, B, C, D); evaluation vs. baselines; demo Streamlit app | H₁ confirmed/falsified; model released on HuggingFace | MUST |
| **Month 4–5** | Study 1b primary analysis: ANCOVA on intent prediction accuracy (Group B vs. Group A at Week 1), unadjusted and engagement-adjusted effects; Soul Document layer ablation (H₃ analogue: which layers contribute?); null result analysis protocol | H₄ confirmed or falsified; layer-level ablation findings | MUST |
| **Month 5** | Paper draft #1: dataset + model + H₁ + H₄ (Study 1b) | Submitted to arXiv; circulated to lab partner | MUST |
| **Month 5–6** | Study 1b publication preparation. Target venues: ACL, EMNLP, or CHI depending on framing. Study 1b is publishable as a standalone paper if H₄ is confirmed, or as a null result with theoretical implications regarding the relative contributions of personality context versus dyadic history. | Paper #2 draft (Study 1b) | MUST |
| **Month 6–8** | Brain-Score submission; EEG pilot design finalised; IRB approval; participant recruitment from beta cohort | Brain-Score result; pilot protocol approved | SHOULD |
| **Month 7–11** | 60-day EEG pilot; continuous intent gap data from product cohort; Day 0 and Day 60 EEG sessions | H₂/H₃ data collected; product behavioural data as wild-environment H₂ measure | SHOULD |
| **Month 11–12** | Data analysis; paper draft #2 (full study: dataset + model + pilot + EEG + product behavioural cohort); submission | Paper submitted to peer-reviewed venue | MUST |

**Study 1b: Cold Start A/B Study — Full Design**

```
Study type:    Randomised controlled trial
N:             100 new NC users (50 per arm)
Duration:      4 weeks data collection + 1-week annotation follow-up
Assignment:    Random allocation at sign-up
               (1:1, stratified by age and relationship status)

Group A:       Standard NC onboarding
               No Soul Document. Intent prediction builds from message
               history only.

Group B:       NC + Soul v1
               10-15 min Mode A intake at Day 1. Soul Document active
               from first session.

Primary metric: Intent prediction accuracy, measured via sender
               self-annotation (gold standard — the sender is the
               arbiter of their own intent).
               Protocol: 2× per week, 3 recent ambiguous messages
               flagged by NC, "What did you mean?" (free text) +
               1-5 accuracy rating.

Engagement covariate: Soul v1 users spend 10-15 min at intake —
               more invested from Day 1. Engagement level (messages
               sent, sessions/week, days active) included as ANCOVA
               covariate. Both unadjusted and engagement-adjusted
               effects reported.

H₄ test:       One-tailed t-test, α=0.05, power=0.80
               Group B Week 1 accuracy > Group A Week 1 accuracy

Cost:          ~£12,000 (recruitment incentives + RA annotation time
               + manual story tagging)
```

**What we learn from a null result in Study 1b:**
- If the engagement-adjusted effect is null → Soul Document content does not improve accuracy independent of engagement; the engagement effect is what matters → redesign around engagement depth, not personality characterisation detail
- If H₄ is null → Layer completeness does not drive cold-start accuracy → may indicate that Layer 1 (Identity Core) alone is sufficient, or that personality context does not independently contribute beyond what message content carries
- If Group B accuracy improves but with no engagement correction → Soul Document effect is confounded with investment/engagement differential → the v2 design should include an engagement-matched control condition
- A null result in H₄ is a scientific contribution, not a failure: it would be the first rigorous empirical test of the personality context conditioning hypothesis and would inform the theoretical boundary conditions of the dyadic history model

**Publication venue for Study 1b:** ACL, EMNLP, or CHI depending on framing. Study 1b is publishable as a standalone contribution if H₄ is confirmed, and as a theoretically important null result if it is not.

**Parallel product track:**

| Period | Product Activity | Key Output |
|--------|-----------------|------------|
| **Month 1** | Taxonomy unification; OpenClaw/Node.js gateway scaffold; Baileys WhatsApp integration; bridge classifier (GPT-4o-mini, SI/PI schema) behind abstracted `ClassifierInterface`; bilateral consent flow; Soul Document intake UI (Mode A, 8 questions) | Infrastructure complete; bridge classifier live; Soul Document intake live for Study 1b |
| **Month 1–3** | Internal alpha; basic intent gap feature on bridge classifier; data schema compatible with RoBERTa-large output from Day 1; privacy gateway (on-device, AES-256); Soul Document local storage (AES-256, device keychain) | Internal alpha working; Soul Document locally stored and inference-time injected |
| **Month 3–6** | Closed alpha: 10–20 couples; core intent gap feature; privacy gateway; web dashboard V1; Coach agent (rule-based V1) | Alpha validated: does bridge classifier produce coherent gap scores on real messages? |
| **Month 6–7** | RoBERTa-large deployed in shadow mode behind `ClassifierInterface`; 2-week shadow validation; model cutover; beta launch to 30–50 couples | First product in the world running a scientifically validated intent gap model |
| **Month 7–9** | Twin agent activated (4+ weeks data accumulated); Weekly Reflection feature; EEG pilot participants recruited from beta cohort; beta expanded to 250 couples | Two-environment H₂ validation: product (wild) + EEG (lab) |
| **Month 9–12** | Scale and stabilise; product in maintenance mode during paper writing; population-scale intent gap dataset accumulating from consented beta users | Real-world deployment evidence for paper; commercial proof-of-concept |

**The parallel tracks are one programme, not two.** The critical design decision that makes this feasible: the product's intent classification layer is abstracted behind a `ClassifierInterface` from Day 1. In Months 1–3, this interface is backed by a GPT-4o-mini bridge classifier using the same SI/PI label schema as the fellowship annotation protocol. At Month 6–7, the same interface is re-backed by the fine-tuned RoBERTa-large model — zero upstream product code changes, no migration crisis. Taxonomy unification in Month 1 (a joint task counted for both tracks) ensures the product output schema is identical to the fellowship annotation schema throughout. The product build requires approximately 30% of weekly time in Months 1–3 (infrastructure, no ML), 35% in Months 3–6 (alpha, lean feature set), and 45% in Months 6–8 (beta launch, model integration). Research track takes the remainder. The EEG pilot (Months 7–11) is the most time-constrained research phase; product work is intentionally minimal during this window, limited to scaling and maintenance.

**Month 1–3 online behavioural study (pre-EEG signal):** 50 participants recruited online (Prolific); read 40 ambiguous messages with and without model-provided intent distributions; rate perceived intent before/after; 2-week follow-up. This provides an early, low-cost test of H₂'s behavioural component before the full 60-day pilot begins, de-risking the timeline and providing pilot data for effect size estimation.

**Gantt stretch goals:** Full 60-day longitudinal behavioural data from 20+ pairs; ERP N2/P3 analysis; Relationship Digital Twin visualisation; Mode B Soul Document pilot with a professional partner site.

**Year 2 multimodal roadmap:** The Year 1 system is deliberately text-first. This is not a limitation — it is the scientifically correct starting point. Text is the anchor modality in multimodal intent research (MIntRec2.0, Xu et al., 2023): models trained on text alone already capture the primary pragmatic signal, and multimodal fusion adds measurable but incremental gain. In Year 2, voice prosody (pitch, rate, energy via openSMILE) and facial action units (AU6/AU12 valence markers via OpenFace) are fused on top of the text encoder as auxiliary inputs, following the MIntRec2.0 late-fusion architecture. The intent gap model is otherwise unchanged — the same I1–I8 schema, the same JS-divergence metric, the same dyadic relational context vector. Face-to-face extension is Year 3, contingent on Year 2 multimodal validation results.

---

## Section 4: Lab Environment & Collaboration

*Lab partner outreach is in progress (week of 15 March 2026). This section will be updated with the confirmed lab name, PI, and letter of intent before the 28 March submission deadline. Primary targets: UCL FIL (social cognition and inter-brain synchrony), MRC CBU Cambridge (pragmatic inference and neural correlates of social cognition), University of Nottingham Psychology (EEG hyperscanning paradigms). **Contingency:** If no EEG-capable lab partnership is confirmed by Month 3 of the fellowship, Study 4 is explicitly dropped and the project delivers Studies 1–3 in full (dataset + model + Brain-Score), the complete MUST-tier commitment, unaffected by lab partnership status.*

**[TO BE UPDATED: Primary partner: [Lab Name] ([PI Name], [Research Group]). PI has expressed interest in co-supervising and providing EEG facilities; draft LOI attached / available on request.]**

**What the lab partner provides:**
- EEG equipment (64-channel active system) and lab space for Day 0 and Day 60 sessions
- **Existing IBS hyperscanning paradigm**, we are extending the lab's prior inter-brain synchrony work, not designing a paradigm from scratch; this is a critical feasibility assumption and a key selection criterion for lab partner
- Ethics / IRB umbrella, application submitted jointly in Month 1 using the lab's established ethics framework, accelerating approval timeline
- **Existing IBS analysis pipeline** (MNE-Python / EEGLAB), hyperscanning analysis builds on the lab's validated code, not built from zero
- Named PI co-authorship; scientific mentorship on neural experimental design and analysis
- Participant recruitment network (existing participant pool + university mailing lists)

**What I bring to the lab:**
- Complete dataset pipeline, curation, annotation tooling, quality assurance infrastructure
- Foundation model training, evaluation, and open-source release
- Soul Document intake instrument (Mode A), YAML extraction pipeline, inference-time injection architecture (Soul-to-Prompt Adapter + rule-based Query Router)
- Browser extension (Cognitive Companion delivery mechanism), production-grade Chrome MV3 engineering
- Streamlit demo application, visual hypothesis display for fellowship review and lab presentations
- Analysis code for intent gap metrics, JS-divergence computation, and model evaluation
- Full documentation and reproducibility infrastructure (DVC, HuggingFace Hub, OpenNeuro upload)

**Division of labour:**
- Behavioural and ML work (Studies 1–3, Study 1b): primarily fellow-led, with PI scientific oversight
- EEG study design (Study 4): jointly designed with PI; fellow implements data collection tooling; PI leads EEG analysis with fellow contributing
- Paper writing: fellow leads; PI co-author on all outputs; joint first authorship model on the EEG paper

**Why this combination works:** The bottleneck in most AI-for-neuroscience projects is build velocity, getting from scientific question to working instrument to deployable experiment. Most neuroscience labs do not have engineers who can take a model from idea to browser extension in two weeks. I do. The lab brings the experimental rigour, ethics infrastructure, and neural measurement capability that a solo engineer cannot access. Together we can run an empirical programme in 12 months that would take a standard lab three years.

---

## Section 5: Risks, Ethics & Mitigation

### 5.1 Scientific Risks

**Risk 1, Ground truth problem: κ < 0.70**
If human annotators cannot reliably agree on sender intent and perceived intent at the required threshold, the training signal is invalid. *Mitigation:* κ pilot in Month 1 before any full annotation begins. Failure gate built into the plan, if κ fails after two adjudication rounds, the label schema is redesigned before proceeding. The pilot is designed to surface this failure early and cheaply.

**Risk 2, H₁ null result**
Relational context may not significantly improve intent prediction at this model scale and label granularity. *Mitigation:* A null result is explicitly a publishable and scientifically valuable outcome, the first rigorous test of the dyadic conditioning hypothesis. The project does not depend on H₁ being confirmed; it depends on H₁ being rigorously tested.

**Risk 3, Lab partner confirmation delayed**
If no lab partner letter of intent is secured before the application deadline, Section 4 remains incomplete and the EEG pilot (SHOULD tier) is at risk. *Mitigation:* Lab partner emails sent in the week of 15 March, two weeks before the 28 March deadline. The MUST tier (dataset + model + paper) is fully executable without a lab partner. The SHOULD tier is explicitly contingent.

**Risk 4, IRB / ethics approval delay**
Ethics applications take 4–12 weeks at UK institutions. If submission is delayed past Month 1, the EEG pilot timeline compresses. *Mitigation:* Ethics application submitted jointly with lab partner in Month 1; lab partner's existing ethics umbrella used where applicable to accelerate; EEG sessions (Days 0 and 60) are not on the critical path until Month 7.

**Risk 5, Compute budget overrun**
Full model training and ablation sweeps may exceed $1,000 if hyperparameter search is expensive. *Mitigation:* Fixed compute budget confirmed with Encode funding allocation in Month 1. DistilBERT prototype first, if performance is sufficient, no RoBERTa-large run needed. GPU cost tracked per run; sweep scope adjusted if budget threshold approached.

**Risk 6, H₄ null result**
The Soul Document may not improve cold-start intent prediction accuracy, or the observed effect may disappear after controlling for the engagement differential between Group B (10–15 min intake) and Group A (no intake). *Mitigation:* H₄ null result is planned for and productive: the null result analysis protocol (Section 3.5) specifies exactly what is learned from each failure mode. The engagement covariate is tracked from Day 1 specifically to enable this decomposition. A null result for H₄ is publishable and constrains the theoretical space for future personality context conditioning research.

---

### 5.2 Ethical Risks & Mitigations

**1. Cultural and linguistic label bias**
Intent categories and their surface signals vary across cultures. British English, American English, and South Asian English carry different pragmatic norms for the same surface form.
*Mitigation:* Minimum 3 distinct cultural backgrounds in 5-annotator pool. Per-culture κ reported. High cross-cultural-variance categories flagged with wider model confidence intervals.

**2. Neurodiverse communication style mislabelling**
Neurodiverse communicators use pragmatic structures that diverge from neurotypical norms; a neurotypical-dominant training set will systematically mislabel their intent.
*Mitigation:* Neurodiverse-authored messages explicitly included (recruited via autism/ADHD community groups). Separate κ computed on neurodiverse subset. Model error rates on neurodiverse messages explicitly reported in the paper.

**3. Downstream harm in vulnerable relationships**
A false low gap score (model confident, receiver actually at risk) could discourage help-seeking in high-stakes relationship contexts.
*Mitigation:* High-entropy distributions (model uncertain) displayed as "high ambiguity" flags, not false confidence. Pattern asymmetry detection surfaces chronic self-interest signals rather than suppressing them. When the Digital Twin shows sustained divergence combined with high self-interest asymmetry, the Companion displays an explicit safeguarding signpost with the following in-product copy: *"This tool cannot determine whether you are safe. If you feel unsafe in your relationship, please contact the National Domestic Abuse Helpline: 0808 2000 247 (free, 24 hours)."* This is not a design afterthought, it is a designed feature, reviewed with the ethics board in Month 1.

**4. Domestic abuse / coercive control scenario**
The Relationship Digital Twin stored on-device could become a surveillance instrument if a controlling partner accesses the device. The Soul Document, containing a user's values, non-negotiables, stress responses, and biographical stories, poses an amplified version of this risk: it is a richer and more intimate personal dataset than message metadata.
*Mitigation:* All data — Digital Twin and Soul Document alike — is encrypted at rest (AES-256, device keychain). No cloud sync in MVP. Biometric/PIN gate on Companion data access, applied to the Soul Document as a mandatory design constraint (not a UX option). Critically: **the Relationship Digital Twin visualisation is opt-in and hidden by default**; it is not visible unless the user explicitly activates it. The MVP explicitly does not include any "partner monitoring" features; all analysis is strictly first-person. **The Soul Document is not accessible to any partner, in any scenario, at any consent level.** No partner access is permitted in v1 — not with mutual consent, not with any consent mechanism. Power dynamics in intimate relationships make "mutual consent" an unreliable safeguard; this constraint is a design decision, not a configuration option. The domestic abuse and Soul Document surveillance scenarios are reviewed explicitly with the lab ethics board in Month 1 as named design constraints.

**5. Participant data in EEG pilot**
EEG and behavioural data from 20–24 participants requires secure handling, appropriate consent, and clear data retention policies.
*Mitigation:* Full ethics application submitted Month 1 with lab partner. Informed consent covers EEG recording, 60-day message metadata collection (no message content, intent gap scores only), and data retention period. Participants can withdraw at any time with data deletion.

**6. Soul Document data as sensitive personal data**
The Soul Document contains personal narratives, ranked values, non-negotiables, biographical stories, and self-reported decision architecture — a category of personal data that is qualitatively more sensitive than behavioural metadata. Inappropriate access, exfiltration, or research use without consent would constitute a serious privacy violation.
*Mitigation:* All Soul Document data is local-first, AES-256 encrypted at rest, not shareable with any partner or third party, and fully deletable at any time. No partner access in v1 — this is a non-negotiable design constraint, not a configurable permission. Soul Document data is classified as sensitive personal data requiring explicit informed consent, purpose limitation, and enhanced security controls. IRB review is required before any research use of Soul Document data from real users. Users retain full rights to export (YAML format), edit any self-reported entry, and delete all stored content including snapshots, immediately and irreversibly. **Ablation-first principle as an ethical safeguard:** Soul Document fields that do not measurably improve H₄ are removed before v2, preventing accumulation of personal data that does not serve a demonstrated scientific purpose. The default position is to collect less, not more.

---

## Section 6: Bibliography

1. Adolphs, R. (2002). Recognizing emotion from facial expressions: Psychological and neurological mechanisms. *Behavioural and Cognitive Neuroscience Reviews*, 1(1), 21–62.
2. Blank, I., Kanwisher, N., & Fedorenko, E. (2014). A functional dissociation between language and multiple-demand systems revealed in patterns of BOLD signal fluctuations. *Journal of Neurophysiology*, 112(5), 1105–1118.
3. Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313–7318.
4. Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review*, 107(2), 261–288.
5. Davidson, R. J., & Lutz, A. (2008). Buddha's brain: Neuroplasticity and meditation. *IEEE Signal Processing Magazine*, 25(1), 176–174.
6. Dikker, S., Wan, L., Davidesco, I., Kaggen, L., Oostrik, M., McClintock, J., ... & Poeppel, D. (2017). Brain-to-brain synchrony tracks real-world dynamic group interactions outside the laboratory. *Current Biology*, 27(9), 1375–1380.
7. Fedorenko, E., Behr, M. K., & Kanwisher, N. (2011). Functional specificity for high-level linguistic processing in the human brain. *PNAS*, 108(39), 16428–16433.
8. Fletcher, G. J., Simpson, J. A., & Thomas, G. (2000). The measurement of perceived relationship quality components: A confirmatory factor analytic approach. *Personality and Social Psychology Bulletin*, 26(3), 340–354.
9. Frith, C. D., & Frith, U. (2006). The neural basis of mentalizing. *Neuron*, 50(4), 531–534.
10. Haidt, J., & Rose-Stockwell, T. (2019). The dark psychology of social networks. *The Atlantic*, December 2019.
11. Hasson, U., Ghazanfar, A. A., Galantucci, B., Garrod, S., & Keysers, C. (2012). Brain-to-brain coupling: A mechanism for creating and sharing a social world. *Trends in Cognitive Sciences*, 16(2), 114–121.
12. LeDoux, J. E. (1996). *The Emotional Brain: The Mysterious Underpinnings of Emotional Life*. Simon & Schuster.
13. Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., ... & Stoyanov, V. (2019). RoBERTa: A robustly optimized BERT pretraining approach. *arXiv:1907.11692*.
14. Lombardo, M. V., Chakrabarti, B., Bullmore, E. T., Wheelwright, S. J., Sadek, S. A., Suckling, J., ... & Baron-Cohen, S. (2011). Specialization of right temporo-parietal junction for mentalizing and its relation to social impairments in autism. *NeuroImage*, 56(3), 1832–1838.
15. McAdams, D. P. (2013). The psychological self as actor, agent, and author. *Perspectives on Psychological Science*, 8(3), 272–295.
16. McGaugh, J. L. (2000). Memory — a century of consolidation. *Science*, 287(5451), 248–251.
17. Öhman, A., & Mineka, S. (2001). Fears, phobias, and preparedness: Toward an evolved module of fear and fear learning. *Psychological Review*, 108(3), 483–522.
18. Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017). Brain-to-brain entrainment: EEG interbrain synchronization while speaking and listening. *Scientific Reports*, 7(1), 4190.
19. Saxe, R., & Kanwisher, N. (2003). People thinking about thinking people: The role of the temporo-parietal junction in "theory of mind." *NeuroImage*, 19(4), 1835–1842.
20. Schrimpf, M., Blank, I., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., ... & Fedorenko, E. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*, 118(45), e2105646118.
21. Askenasy, J. J. M., & Lehmann, D. (2013). Consciousness, brain, neuroplasticity. *Frontiers in Psychology*, 4, 412.
22. Grice, H. P. (1975). Logic and conversation. In P. Cole & J. Morgan (Eds.), *Syntax and Semantics, Vol. 3: Speech Acts* (pp. 41–58). Academic Press.
23. Sperber, D., & Wilson, D. (1986). *Relevance: Communication and Cognition*. Harvard University Press.
24. Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., & Bowman, S. R. (2018). GLUE: A multi-task benchmark and analysis platform for natural language understanding. *arXiv:1804.07461*.
25. Xu, H., Zhao, H., Gu, W., Xu, L., Zhu, L., Liu, T., & Zhao, Z. (2023). MIntRec2.0: A large-scale benchmark dataset for multimodal intent recognition and out-of-scope detection in conversations. *arXiv:2309.04421*.
26. Xu, Y., Wei, L., Liu, C., & Zhang, T. (2024). Twin-2K-500: Interview-derived personality data improves LLM behavioural prediction. *Proceedings of EMNLP 2024*.
27. Finn, E. S., Huber, L., Jangraw, D. C., Molfese, P. J., & Bandettini, P. A. (2024). Post-interaction neuroplasticity of inter-brain networks predicts social motivation. *PNAS*, 121(5), e2311771121.
28. Sitaram, R., Ros, T., Stoeckel, L., Haller, S., Scharnowski, F., Lewis-Peacock, J., ... & Sulzer, J. (2017). Closed-loop brain training: The science of neurofeedback. *Nature Reviews Neuroscience*, 18(2), 86–100.
29. Singer, T. (2025). A neuroscience perspective on the plasticity of the social and relational brain. *Annals of the New York Academy of Sciences*, 1544, 15–34.
30. Ickes, W. (1993). Empathic accuracy. *Journal of Personality*, 61(4), 587–610.
31. Pavlacic, J. M., Buchanan, E. M., Maxwell, N. P., Hopke, T. G., & Schulenberg, S. E. (2019). A meta-analysis of expressive writing on posttraumatic stress, posttraumatic growth, and quality of life. *Review of General Psychology*, 23(2), 230–250.
32. Fritz, J., de Graaff, A. M., Caisley, H., van Harmelen, A. L., & Wilkinson, P. O. (2024). A systematic review of amenable resilience factors that moderate and/or mediate the relationship between childhood adversity and mental health in young people. *Advances in Methods and Practices in Psychological Science*, 7(1), 25152459241267912.
33. Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS*, 120(30), e2305016120.
34. Møller, A. G., Dalsgaard, J., Pera, A., & Aiello, L. M. (2023). Is a prompt and a few samples all you need? Using GPT-4 for data augmentation in low-resource classification tasks. *arXiv:2304.13861*.
35. Rashkin, H., Smith, E. M., Li, M., & Boureau, Y. L. (2019). Towards empathetic open-domain conversation models: A new benchmark and dataset. *Proceedings of ACL 2019*, 5370–5381.
36. Li, Y., Su, H., Shen, X., Li, W., Cao, Z., & Niu, S. (2017). DailyDialog: A manually labelled multi-turn dialogue dataset. *Proceedings of IJCNLP 2017*, 986–995.
37. Welivita, A., & Pu, P. (2020). A taxonomy of empathetic response intents in human social conversations. *Proceedings of COLING 2020*, 4444–4453.
38. Brown, P., & Levinson, S. C. (1987). *Politeness: Some Universals in Language Usage*. Cambridge University Press.
39. Goffman, E. (1967). *Interaction Ritual: Essays on Face-to-Face Behaviour*. Anchor Books.
40. Gottman, J. M. (1994). *What Predicts Divorce? The Relationship Between Marital Processes and Marital Outcomes*. Lawrence Erlbaum Associates.
41. Gross, J. J. (1998). Antecedent- and response-focused emotion regulation: Divergent consequences for experience, expression, and physiology. *Journal of Personality and Social Psychology*, 74(1), 224–237.
42. Ochsner, K. N., & Gross, J. J. (2005). The cognitive control of emotion. *Trends in Cognitive Sciences*, 9(5), 242–249.
43. Searle, J. R. (1976). A classification of illocutionary acts. *Language in Society*, 5(1), 1–23.
44. Higgins, E. T. (1987). Self-discrepancy: A theory relating self and affect. *Psychological Review*, 94(3), 319–340.

---

## Appendix A: Product Vision & Impact Pathway *(Beyond 12 Months)*

*This appendix describes the longer-term product vision for reviewers interested in the commercial and societal pathway. It is not part of the 12-month fellowship commitment.*

The Cognitive Companion is designed on a three-horizon arc. Each horizon is unlocked by the science of the previous one.

**Horizon 1, The Mirror (MVP / Fellowship year):**
One person. One message. One Companion. The intent gap made visible: P(intent | message, relational history, context). The history slider shows how relational context reshapes meaning in real time. The Relationship Digital Twin maps the semantic space of one relationship, convergence, divergence, pattern asymmetry. *"You see yourself as others receive you."*

*What the Mirror shows (individual view):*
- **Intent style fingerprint** — I1–I8 distribution histogram across all sent messages: your stable communication profile ("you predominantly use I4: seeking validation")
- **Blind-spot histogram** — stacked bar of intended vs. received intent class: where your intent is most consistently misread (e.g. I3 sent, received as I5)
- **Calibration score** — how accurately you predict your own reception; a metacognitive sensitivity dial grounded in Caluori et al. (PNAS Nexus, 2025)
- **Mood trend line** — smoothed valence of your sent messages across sessions; a slow-drift signal, not reactive noise
- **Self-vs-model divergence dial** — does what you think you are expressing match what the model detects you are expressing?
- **Actual/ideal self gap** — populated by the weekly reflection journal: the distance between "how I communicate" (inferred from classifier) and "how I want to communicate" (self-reported via Higgins, 1987 framework); shrinking gap over 60 days is the deepest individual improvement signal the Mirror can show

*The Soul Document IS the self-model substrate of the Mirror.* The classifier infers what the user does. The Soul Document captures what they believe and intend — their values, their characteristic responses under stress, the biographical experiences that shaped how they communicate. The reflection journal captures what they aspire to. Together, these three data streams form a triangulated individual consciousness model: inferred behaviour (classifier) + stated intent and personality architecture (Soul Document) + stated aspiration (journal). The improvement signal is convergence across all three — the point at which who you are as a communicator, what you mean to say, and who you want to be begin to align. The Mirror is not complete without the Soul Document; the Soul Document, standing alone, is a static self-report. It is the convergence of the dynamic model (classifier), the structured self-model (Soul Document), and the aspirational signal (journal) that constitutes the scientific instrument.

**The Soul Document as identity anchor for the Relationship Digital Twin:** The Digital Twin maps the semantic space of a relationship — the pattern of intent categories, the gap distribution, the repair rate, the convergence trajectory over time. The Soul Document maps the individual's personality space — the stable values, decision architecture, and narrative history that shape how they generate and receive communicative intent. The intent gap exists at the intersection of both: it arises from the encounter between two personality architectures, mediated by a shared relational history. A complete model of the intent gap requires both maps. The Digital Twin captures what is happening between people. The Soul Document captures who those people are, independently of that particular relationship.

**The temporal Soul Document (Soul vFull, 3–5 year north-star vision):** As the Soul Document is revised across life eras, a versioned stack of personality snapshots accumulates. "What would 2019-me have said about this?" becomes a longitudinal self-dialogue instrument — not a product feature, but a genuine scientific contribution to longitudinal personality research. The temporal stack enables divergence scoring between snapshots, detecting when a person's values or decision architecture has shifted significantly enough to constitute a meaningful personality-level change event. This is not Year 1 scope, but it represents a scientifically novel methodology for studying personality evolution at the individual level: not cross-sectional surveys, but a continuous, structured, first-person longitudinal record. The infrastructure built in Year 1 (local-first storage, YAML versioning, IRB-approved consent architecture) is the foundation that makes this research programme possible.

**Horizon 2, The Bridge (Post-fellowship, when the science is ready):**
Two people. Mutual consent. Both Companions active. With one symmetric, revocable consent tap, each person's intent model is shared with the other, not raw messages, not personal data, but intent representation vectors and reception model parameters. The gap score updates from both sides simultaneously. Scientifically grounded in inter-brain synchrony (Hasson et al., 2012), the Bridge scaffolds the neural coupling that predicts communicative success, before the conversation rather than after. *"With mutual consent, you see each other as you mean to be seen."*

*What the Bridge shows (shared relationship twin):*
- **Intent gap heatmap** — turn-by-turn matrix: sender intent class × receiver-parsed intent class, colour-coded by JS-divergence magnitude; high-divergence cells mark misalignment episodes
- **Dyadic spider plot** — two overlapping 16-dimensional radar charts (one per person); diverging polygon shapes signal asymmetric relationship experience
- **Rolling gap time-series** — JS-divergence per session across 60 days; the empirical answer to "are we converging or diverging?"
- **Communication asymmetry panel** — turn-length ratio, response latency histogram, topic initiation map; structural signals of dominance, withdrawal, or reciprocity (Gottman, 1994)
- **Repair rate** — proportion of turns where an intent mismatch is acknowledged or corrected; rising repair rate is the behavioural signature of a healthy relationship
- **Longitudinal health quadrant** — four composite scores (Trust / Appreciation / Conflict density / Reciprocity) derived from intent pattern distributions; grounded in the top ML-identified relationship quality predictors (Joel et al., PNAS, 2020)
- **Complementarity signal** — the Bridge distinguishes *complementary divergence* (high JS-divergence + high repair rate + positive health quadrant = a stable, thriving difference) from *problematic divergence* (high JS-divergence + low repair rate + declining health); the UI labels the pattern explicitly so a healthy complementary dyad is never told their difference is a problem
- **Growth edge indicator** — for high-functioning dyads, the Bridge surfaces the next developmental frontier: the intent categories rarely used by either partner, the emotional vocabulary not yet shared, the relational depth not yet reached; framed not as a deficit but as *"a pattern we haven't seen yet — this is where you could go next"*

**Note on Soul Document and the Bridge:** The Bridge, when it is built, will not expose Soul Document content to partners. The two-person intent model shares intent representation vectors, not the underlying personality architecture that produced them. This constraint holds even under mutual consent, for the reasons stated in Section 5.2 and the Soul Document governance specification in Appendix C.

**Horizon 3, The Map (Long-run vision):**
Thousands of consented pairs. An empirical atlas of communicative intent at population scale, where misunderstanding concentrates, where understanding spontaneously forms, what closing the gap actually looks like across cultures, relationship types, and demographics. The data that founds the field of population-level neural pragmatics. *"And together, humanity begins to understand itself."*

**ARIA alignment:**
- *Scalable Neural Interfaces:* The intent-conditioned model and dataset are computational tools that interface with human neural language processing, validated against neural data via Brain-Score, designed to scaffold mentalising circuitry.
- *Collective Flourishing:* The Map is the long-term vision, intent infrastructure that reduces the structural cost of human miscommunication at population scale, built on consent architecture rather than attention extraction.

---

## Appendix B: Technical Specification

### B.1 Intent-Conditioned Model Architecture

```
Input: [soul_document_context_block] + [message_text] + [relational_context_vector]

Tokenisation:  RoBERTa tokeniser (BPE, 50k vocab)
Encoder:       RoBERTa-large (24 layers, 1024 hidden, 16 heads, 355M params)

Relational context vector (16-dim):
  - relationship_type:     5-dim one-hot (couple/parent-child/friend/community/colleague)
  - duration_log:          1-dim continuous (log months)
  - recent_valence:        1-dim continuous [-1, +1]
  - message_frequency:     1-dim continuous (log msgs/week)
  - rolling_gap_score:     1-dim continuous (14-day mean JS-divergence)
  - [7 reserved dims for future relational features]

Soul Document context block (600-900 tokens, prepended to system prompt):
  - Produced by Soul-to-Prompt Adapter (see Section B.3)
  - Query Router selects which layers to inject (see Section B.4)
  - Present only in Condition D (full model); absent in Conditions A/B/C

Integration:   Relational context vector concatenated to [CLS] hidden state
               before classification head.
               Soul Document context block injected as system-prompt prefix —
               conditions the full encoder forward pass, not just the
               classification head.

Classification head:
  - SI head:  Linear(1040, 7) + softmax  [sender intent, 7 categories]
  - PI head:  Linear(1040, 7) + softmax  [perceived intent, 7 categories]

Gap score:    JS-divergence(P(SI), P(PI))  [0 = no gap, 1 = maximum divergence]
```

**Training configuration:**
- Optimiser: AdamW, weight decay 0.01
- Learning rate: {1e-5, 2e-5, 3e-5}, sweep
- Batch size: 32
- Epochs: 5 with early stopping (patience = 2 on validation macro-F1)
- Hardware: Lambda Labs A100 40GB
- Checkpointing: HuggingFace Hub (private during training, public at release)

### B.2 Annotation Guidelines (Summary)

**Task framing for annotators:**

*"You will be shown a short text message and a brief description of the relationship between the sender and receiver. You will be asked to assign two labels:*

*1. Sender Intent (SI): What was the sender most likely trying to communicate? Take the sender's perspective.*
*2. Perceived Intent (PI): How would a reasonable receiver in this relationship most likely interpret this message? Take the receiver's perspective.*

*Use the 7 intent categories (I1–I7). If you genuinely cannot decide, select 'Ambiguous', do not guess. Relational context changes meaning: the same message in different relationships may warrant different labels."*

**Category boundary examples:**

| Message | Context | SI | PI |
|---------|---------|----|----|
| "Can we talk tonight?" | Partner of 2 years, recent tension | I1 (seeking connection) | I5 (expressing frustration), receiver likely threat-parses |
| "You seem quiet lately" | Close friend, no recent conflict | I2 (expressing concern) | I2 (expressing concern), low gap |
| "Fine, do whatever you want" | Colleague, first conflict | I5 (expressing frustration) | I5 (expressing frustration), surface match |
| "Fine, do whatever you want" | Partner of 5 years, recurring conflict | I5 (expressing frustration) | I3 (setting a boundary), relational context shifts PI |

**Quality control:** Each message annotated by 5 independent annotators. Majority vote used for training label; full distribution retained for model evaluation. Messages where 3+ annotators select "Ambiguous" are flagged for schema review rather than included in training.

### B.3 Soul-to-Prompt Adapter

The Soul-to-Prompt Adapter converts structured YAML layers into a compact, robust system-prompt context block. It is a deterministic formatting layer — no ML required at this stage.

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

Target output length: 600–900 tokens. Compact enough for any 8K+ context window alongside the active conversation. Fields absent from the user's Soul Document are silently omitted; the adapter never hallucInates or interpolates missing content.

### B.4 Query Router (Rule-Based, v1)

For v1, query classification is rule-based — no classifier required. The router uses a keyword heuristic list to decide which layers to inject:

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

RETRIEVE AND INJECT (keyword matching, top 2 stories):
└── Narrative Library (keyword-based retrieval)
    Trigger: any query involving a theme present in retrieval_tags
    Retrieval method: keyword overlap with retrieval_tags (v1)
                      (embedding-based retrieval is a v2 upgrade)
    Tokens: ~400-600 per story, max 2 stories injected
```

Rule-based keyword heuristics are a deliberate simplicity choice for the fellowship year. They are fast, auditable, and sufficient to test the core H₄ hypothesis. A lightweight classifier (e.g., fine-tuned BERT for intent query type) is a v2 upgrade, pending evidence that the keyword heuristic is the accuracy bottleneck.

### B.5 Token Budget (v1)

```yaml
token_budget_v1:
  total_context_window: 8192    # conservative baseline
  allocation:
    identity_core_prompt: 300   # always injected
    active_conversation: 2000   # always
    narrative_retrieval: 1000   # top 2 stories (conditional)
    decision_architecture: 250  # conditional on conflict/decision markers
    response_reserve: 1500      # output generation
    buffer: 3142                # remaining headroom
```

### B.6 EEG Analysis Plan

**Pre-processing pipeline (MNE-Python):**
- Band-pass filter: 1–40 Hz
- Independent component analysis (ICA) for artefact removal (eye blinks, muscle noise)
- Epoch extraction: −200ms to +800ms relative to message onset
- Baseline correction: −200ms to 0ms

**Inter-brain phase synchrony (IBS) computation:**
- Wavelet transform: Morlet wavelets, 4–8 Hz (theta band)
- Phase angle extraction per electrode pair per trial
- IBS = |mean(exp(i × Δφ))| across trials, value in [0,1]; 0 = no synchrony, 1 = perfect synchrony
- Electrode pairs: all homologous pairs across the two participants' montages
- Statistical comparison: pre vs. post paired Wilcoxon signed-rank test; FDR correction across electrode pairs

**ERP analysis (exploratory):**
- N2 component: 200–350ms, frontocentral electrodes (Fz, FCz, Cz)
- P3 component: 300–600ms, centroparietal electrodes (CPz, Pz)
- Peak latency and amplitude extracted; repeated-measures ANOVA (condition × time)

---

## Appendix C: Soul Document Architecture Specification v0.2

*This appendix documents the Soul Document as a scientific instrument specification, separate from its product implementation. Reviewers interested in the technical architecture of the personality context layer will find the complete specification here. The Soul Document is not a user experience feature. It is a structured personality characterisation methodology that extends the model's context conditioning — a scientific instrument designed to enable the class of question formalised in H₄: does stable individual personality context independently improve intent prediction accuracy beyond dyadic relational history alone?*

---

### C.1 Scientific Purpose

The Soul Document encodes an individual's identity, decision architecture, and narrative history in a structured, model-agnostic YAML format. At inference time it is injected as a context block, conditioning intent prediction on *who the person actually is*, not only on what they have written. It is not a fine-tuned model. It is a structured retrieval corpus — model-agnostic, forward-compatible, and enriched over time as the user extends or corrects it.

The fundamental scientific claim is narrow and testable: *structured personal context injected at inference time will improve cold-start intent prediction accuracy over a model conditioned on relational history alone, and this improvement will be measurable against sender self-annotation as ground truth.* The v1 study (Study 1b) is designed to test this claim and nothing more. Features not supported by the v1 evidence are explicitly excluded until ablation results justify their inclusion.

**Soul v1 Design Principle:**
> *Prove that any structured personal context beats no context for cold-start intent prediction. Nothing more. Nothing less.*

---

### C.2 Soul v1 — Three-Layer Schema

**Ablation-First Principle:**
Every field in the Soul v1 schema must earn its place. The v1 study (Study 1b) is explicitly designed to measure which subsets of the Soul Document improve intent prediction accuracy. Any layer or field that does not measurably contribute to H₄ will be removed before v2. The default position is *less is more* — complexity is added only when evidence demands it.

---

#### Layer 1: Identity Core
*Static anchor — always injected. Changes only at decade-scale life events.*

```yaml
identity_core:
  version: "1.0"
  last_updated: "2026-03-17"

  # Core values — ranked, not listed
  # Rank order matters: tells the model how this person resolves value conflicts
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

**Intent modelling use:** When a message could be read as a challenge or an inquiry, the Identity Core answers: does this person default to defence or curiosity? The ranked values provide that signal without requiring message history — the core cold-start advantage.

**Population method:** Self-report via guided intake (Q1–Q3, Mode A). NC extracts and structures YAML automatically from conversational responses; user reviews and edits before activation.

---

#### Layer 2: Decision Architecture Lite
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

**Intent modelling use:** Shorter messages plus delayed replies become interpretable as stress response, not disengagement. Conflict queries route to this layer automatically via the keyword router. The misread_risk field is the most directly actionable for intent prediction: it specifies exactly the interpretive error that the model is designed to prevent.

**Population method:** Self-report via guided intake (Q4–Q5, Mode A). No clinical inference — these are self-reported patterns, not diagnostic classifications.

---

#### Layer 3: Narrative Library
*RAG-retrieved on demand — 5–7 stories minimum for v1 study cohort.*

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

**Intent modelling use:** When a query involves conflict with authority, `story_001` is retrieved and used as grounding. The model does not merely know this person avoids institutions — it knows the specific experience that made that true. This is the episodic memory as intent prior mechanism: autobiographical specificity as inference signal, not trait abstraction.

**Scientific novelty:** The Narrative Library instantiates a principle from autobiographical memory research (Conway & Pleydell-Pearce, 2000): self-defining memories carry stable emotional and behavioural meaning that shapes how individuals generate and interpret communicative acts. The v1 study tests whether encoding this meaning explicitly — as a retrievable, annotated corpus — produces measurably better intent prediction than Layer 1 and Layer 2 alone. This is the ablation question Layer 3 is designed to answer.

**Population method:** Guided narrative intake (Q6–Q8, Mode A). In the v1 study cohort, story themes and retrieval tags are manually assigned by a researcher or RA following a standardised protocol. Users in consumer Mode A receive a guided prompting UI that extracts stories conversationally.

---

### C.3 What Soul v1 Deliberately Excludes

| Excluded Feature | Why Excluded | When Reconsidered |
|-----------------|-------------|------------------|
| Emotional Signature Layer | Requires clinical framing to interpret safely; pseudo-diagnostic without clinician | Soul v2 — after v1 ablation results |
| Communication Style Map | Useful but not essential for H₄; adds intake burden | Soul v2 |
| Temporal Snapshot Stack | Non-trivial infrastructure; unproven incremental value | Soul v3 |
| Passive digital harvest (music, calendar, search) | Consent/trust risk too high for consumer context | Ethics-gated; never without explicit opt-in |
| Attachment style classification | Pseudo-diagnostic without clinical training; cannot be reliably inferred from 30-min interview | Never without clinical channel |
| Partner read access to Soul Document | Safety risk; power dynamics make "mutual consent" unreliable | Requires ethics board approval; explicitly out of scope for fellowship year |
| Adversarial correction loop | Valuable but not core to cold-start validation | Soul v2 |
| Humour architecture | Interesting signal; not essential for v1 hypothesis | Soul v2+ |
| Relationship Mirror / dyadic comparison | High safety risk; requires clinical mediation | Ethics-gated; never without IRB approval |

**All Soul v1 data is local-first, encrypted at rest (AES-256), not shareable with partners or third parties, and fully deletable. Clinical and partner-facing features are explicitly out of scope for the fellowship year.**

---

### C.4 Soul v1 → v2 → vFull Roadmap

| Version | Layers | Intake | Router | Studies | Governance |
|---------|--------|--------|--------|---------|------------|
| **Soul v1** (Fellowship year) | L1: Identity Core, L2: Decision Architecture Lite, L3: Narrative Library (manually tagged) | Mode A consumer (10–15 min) + Mode B pilot (conditional on professional partner) | Rule-based keyword heuristics | Study 1b: Cold Start A/B (H₄, H₄-ablation) | Local-first, no partner access, IRB-gated |
| **Soul v2** (Post-fellowship, contingent on v1 evidence) | + L4: Emotional Signature (if ablation supports), + L5: Communication Style Map | + Automated NLP story tagging replacing manual RA annotation | + Lightweight BERT query classifier, + Embedding-based story retrieval | Study 5: Adversarial Refinement Convergence | As v1 plus Mode B at scale with clinical partner |
| **Soul vFull** (3–5 year north star) | All 6 layers including Temporal Snapshot Stack | Multimodal passive harvest (explicit opt-in), Mode B clinical integration | Full semantic router | Studies 2–6 (neuroimaging, longitudinal, ND calibration, RCT) | Ethics board required for any partner-facing features |

---

### C.5 Soul v1 Data Governance Constraints

The following constraints apply to Soul v1 and cannot be overridden by user preference, partner request, or any consent mechanism. These are design constraints, not configuration options.

**Storage and encryption:**
- All Soul Document data is stored locally on the user's device
- Encrypted at rest using AES-256 with device keychain key management
- Cloud sync is opt-in only and end-to-end encrypted if enabled
- Raw behavioural data is never retained — only extracted YAML fields

**Access control:**
- Only the owner can read or write their Soul Document
- No partner access — not with mutual consent, not with any consent. This is a design constraint, not a configurable permission. Power dynamics in intimate relationships make "mutual consent" an unreliable safeguard for data of this sensitivity.
- No therapist or partner access in v1 — this constraint is lifted only when Mode B is deployed with a formally onboarded clinical partner and explicit ethics board approval
- NC foundation model reads at inference time only — no persistent retention of Soul Document content in model state

**Prohibited uses (v1 — non-negotiable):**
- Third-party sale or licensing of Soul Document data
- Training of any external model on Soul Document content
- Access by any party other than the owner
- Use without biometric or PIN authentication

**User rights:**
- Full export as YAML at any time
- Full deletion including all snapshots — immediate and irreversible
- Right to review all stored fields and edit any self-reported entry

**Domestic abuse constraint:**
The Soul Document must not become a surveillance instrument. Shared device scenarios require biometric-gated access. This is a safety requirement, not a UX feature. The design team treats this as a zero-tolerance constraint: any implementation that allows one party to read another party's Soul Document, in any scenario, is a design failure.

**IRB classification:**
Soul Document data is classified as sensitive personal data — personal narratives, ranked values, non-negotiables, biographical stories, and self-reported decision architecture — requiring explicit informed consent, purpose limitation, and enhanced security controls under UK GDPR and the Data Protection Act 2018. IRB review is required before any research use of Soul Document data from real users. Study 1b cannot begin participant recruitment until IRB approval covering Soul Document data collection is confirmed.

**Ablation-first as an ethical safeguard:**
The ablation-first principle (Section C.2) is not only a scientific constraint — it is an ethical one. Soul Document fields that do not measurably improve H₄ at the layer or field level are removed before v2. This prevents the accumulation of sensitive personal data that does not serve a demonstrated scientific purpose. Data minimisation is a design principle, not a compliance afterthought.

---

### C.6 Soul Document Open Questions (v1 Scope)

| # | Question | Options | Recommendation |
|---|----------|---------|----------------|
| 1 | Minimum stories for RAG effectiveness? | 2 / 5 / 7 | 5 minimum; v1 study will test whether more stories = better accuracy |
| 2 | Should keyword router be expanded or kept minimal? | Minimal list / Expanded list | Minimal for v1; expand based on false-negative analysis in study |
| 3 | How do we handle users who cannot recall meaningful stories? | Prompt harder / Accept thin Layer 3 / Offer alternatives | Accept thin Layer 3; flag low-confidence; test whether Layer 1+2 alone is sufficient |
| 4 | What happens to Soul Document on account deletion? | Archive / Full delete / Transfer | Full delete by default; export available before deletion |
| 5 | Should the consumer UI show the generated YAML or abstract it? | Show YAML / Show plain language / Show nothing | Show plain language summary; YAML export available on demand |

---

### C.7 Glossary

| Term | Definition |
|------|-----------|
| **Soul Document** | Structured YAML personality representation injected at inference time to condition intent prediction on stable individual personality architecture |
| **Soul v1** | Fellowship-year scope: 3 layers, rule-based router, one cold-start validation study (Study 1b) |
| **Soul vFull** | North-star architecture: 6 layers, multimodal passive harvest, temporal snapshot stack, clinical integration, Studies 2–6 |
| **Soul-to-Prompt Adapter** | Deterministic formatting layer that converts YAML layers into a structured system-prompt context block |
| **Query Router** | Rule-based system (v1) that selects which Soul Document layers to inject based on keyword heuristics |
| **Ablation-First Principle** | Only fields measurably improving H₄ at layer or field level are retained in the v2 schema |
| **Cold Start** | The period before message history is rich enough to ground intent prediction; the primary condition under which Soul Document advantage is hypothesised |
| **Personality Sovereignty** | Design principle: the user owns, controls, and can delete their Soul Document at any time |
| **Intent Gap** | Delta between sender's intended meaning and receiver's interpreted meaning; the core scientific metric |
| **Manual Tagging (v1)** | Story themes and retrieval tags assigned by researcher/RA in v1 study cohort; automated tagging is a v2 hypothesis |
| **Episodic Memory as Intent Prior** | The scientific framing of the Narrative Library: autobiographical stories carry stable emotional and behavioural meaning that conditions how intent is generated and received |

---

*"We are not building a chatbot. We are building the instrument that measures and closes the biological gap between human minds, and proves, for the first time, that it can be changed."*
