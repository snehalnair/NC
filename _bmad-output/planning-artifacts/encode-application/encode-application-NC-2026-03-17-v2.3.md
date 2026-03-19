---
title: "A Computational Model of Dyadic Mentalising: An Intent-Conditioned Language Model Grounded in Relational History and Personality Context"
subtitle: "Encode x Pillar VC AI for Science Fellowship Application"
author: Snnair
date: 2026-03-17
status: submission-ready-final
version: 2.4
note: "v2.4 — Reviewer comment fixes: jargon defined inline, acronyms introduced on first use, citations added, Soul Document 1-to-many relationship mapping clarified, language simplified where flagged."
---

# A Computational Model of Dyadic Mentalising
## An Intent-Conditioned Language Model Grounded in Relational History and Personality Context

**Encode x Pillar VC AI for Science Fellowship, Application**
**Applicant:** Snnair
**Date:** March 2026
**ARIA Spaces:** Scalable Neural Interfaces · Collective Flourishing

---

## Section 1: Overview

**Scientific question 1:** Can a language model conditioned on dyadic relational history, combined with a closed-loop intent feedback intervention, measurably reduce miscommunication and produce detectable changes in neural markers of mentalising versus threat processing over 60 days?

**Scientific question 2:** Does individual personality context, encoded as a structured biographical intake instrument, independently improve intent prediction accuracy beyond dyadic relational history alone, and does it solve the cold-start problem (the inability to make accurate predictions for new users who have no prior interaction history in the system) that dyadic history cannot?

The most powerful capability a human being can have in the AI era is not a technical skill or an information advantage — it is trust (Harari, 2018; O'Neil, 2016). As AI mediates more of human connection, drafting messages, summarising conversations, predicting responses, the risk is not that humans become less intelligent. It is that meaning gets lost in translation between sender and receiver. The *intent gap* is the measurable form of that loss: the distance between what one person means and what another person receives. This project builds a new computational instrument for measuring the intent gap directly, the first controlled test, to our knowledge, of whether closed-loop intent feedback produces measurable neural-level shifts in mentalising (the cognitive process of inferring another person's mental states — their beliefs, desires, and intentions) circuitry, and a structured methodology for encoding the stable personality architecture that shapes how individuals generate and receive communicative intent.

Human miscommunication has a biological substrate. The amygdala (the brain's rapid threat-detection centre) processes the emotional salience of incoming stimuli via a subcortical pathway (LeDoux, 1996) that responds to emotionally ambiguous stimuli ahead of prefrontal cortical semantic resolution. In digital text communication, where prosody, expression, and physical context are absent, this timing asymmetry means that emotionally ambiguous messages are systematically threat-tagged before their communicative intent is understood. To our knowledge, no existing NLP (Natural Language Processing) system models the sender/receiver intent divergence conditioned on dyadic (two-person) relational history directly. Sentiment classifiers measure surface tone. Emotion recognition systems measure affective expression. Neither asks what matters: *what did this person most likely mean, given who they are and who they are talking to?* The same message, "Can we talk tonight?", carries a fundamentally different intent distribution when sent by a new colleague versus a partner of three years after a difficult week. Relational history is not context noise. It is the primary signal.

**This project addresses four concrete scientific gaps:**

1. To our knowledge, **no neural-pragmatic dataset** conditions intent annotation on dyadic relational history with dual sender/receiver labelling and inter-rater reliability validation.
2. To our knowledge, **no language model** has been trained to predict the receiver's parsed intent conditioned on dyadic relational context and evaluated against a human-parity baseline.
3. To our knowledge, **no empirical study** has tested whether closed-loop intent feedback produces measurable shifts in neural markers of mentalising circuitry over a sustained intervention period.
4. To our knowledge, **no structured personality characterisation instrument** has been tested as an independent conditioning signal for intent prediction in naturalistic relational communication, or evaluated for its capacity to close the cold-start inference gap.

These claims rest on our review of the pragmatics, social NLP, and affective computing literature as of March 2026; we explicitly differentiate from adjacent work in Section 2.3.

**This is AI for Science, not science-flavoured product.**

The intent-conditioned language model, fine-tuned from RoBERTa-large with a novel 16-dimensional relational context layer extended by a personality context block, is the scientific instrument. The browser extension (intervention instrument) is the delivery mechanism for the intervention. The 60-day pilot is the empirical study. There is, to our knowledge, no dataset of this form in the literature; we will construct and release one openly. The validation chain runs across four levels: computational (H₁), personality context cold-start ablation (H₄, embedded within H₁ as a secondary test), behavioural (H₂), and neural (H₃). Each level is independently publishable; together they form a coherent scientific programme.

**12-month deliverables:**
- A 2,000-message annotated neural-pragmatic dataset (dual sender-intent / perceived-intent labels, relational context metadata, κ-validated, 5 relationship types), published on HuggingFace and OpenNeuro
- A trained intent-conditioned language model (RoBERTa-large fine-tuned with 16-dimensional dyadic relational context layer and personality context block), with H₁ confirmed or falsified
- A biographical intake instrument (v1): a 10–15 minute structured interview consisting of 8 guided questions across three layers (core values, decision-making patterns, and personal narrative stories). Participants' responses are tagged by researchers to extract personality themes relevant to communication style. The instrument is reviewed in the IRB (Institutional Review Board — the ethics committee that approves research involving human participants) application in Month 1
- Study 1b (Cold-Start A/B, H₄ ablation): 100 new users randomised 1:1, personality context versus no personality context at Day 1; primary outcome is intent prediction accuracy on a researcher-labelled held-out evaluation set
- A paper submitted to a peer-reviewed venue (ACL, EMNLP, or CHI) reporting dataset, model, and primary results
- *(STRETCH GOAL, contingent on (a) confirmed lab partner by Month 3 AND (b) H1/H4 analysis not slipping behind schedule) A 60-day EEG hyperscanning pilot (N=20–24 dyadic pairs): pre/post theta-band IBS measurement, testing H₃. An online-only behavioural H₂ probe (N=50, no EEG, Months 2–3) runs regardless of lab partnership, ensuring behavioural validation is not hostage to EEG availability.*

**ARIA alignment:** The intent-conditioned model and dataset directly advance *Scalable Neural Interfaces*, computational tools that model human neural processes at scale. The longer-term vision maps to *Collective Flourishing*: infrastructure for human understanding at population scale, built on a consent-based design (where users explicitly opt in to share data, and can revoke access at any time) rather than the attention-extraction model that drives social media platforms.

**Why this fellow, now:** I am an AI engineer with production systems experience in NLP and applied ML. The engineering components, dataset pipeline, annotation tooling, model training, biographical intake, and browser extension, are within my demonstrated capability. They represent significant parallel workload, managed via the MUST/SHOULD tiering above and the explicit contingency planning in Section 5. Embedded in a neuroscience lab that provides EEG equipment, ethics coverage, and experimental paradigm expertise, the combination of demonstrated capacity to build and ship research infrastructure rapidly and neuroscience rigour is what makes this programme executable in 12 months by one fellow.

---

## Section 2: Scientific Background

### 2.1 The Biological Mechanism

Human communication depends on a two-stage neural process. The first is rapid and subcortical: the amygdala processes the emotional salience of incoming stimuli via the direct thalamo-amygdala pathway (LeDoux, 1996), bypassing cortical processing within tens to hundreds of milliseconds. The second is slower and cortical: prefrontal cortex, the temporoparietal junction (TPJ — a brain region critical for understanding other people's mental states), and associated language areas complete semantic interpretation and pragmatic inference over 200–500ms and beyond.

In face-to-face communication, this timing gap is partially bridged by multimodal cues, facial expression, prosody, gesture, that provide rapid disambiguating signals before semantic processing completes. For low-conflict dyads this advantage is real. For high-conflict-history dyads, however, the picture inverts: multimodal cues themselves may carry threat-primed valence accumulated through prior conflict (Gottman, 1994). A partner's neutral expression or familiar tone can trigger a full amygdala threat cascade when that signal has been repeatedly paired with conflict. In these relationships, face-to-face communication may offer no protective advantage over text.

This timing asymmetry is modality-independent: the amygdala threat pathway fires on tonal shifts in voice calls, micro-expressions in face-to-face conversation, and silence latency in text, wherever emotional ambiguity is detectable, threat-tagging precedes semantic resolution. Digital text communication is a particularly high-risk context not because it creates this asymmetry, but because it removes the compensatory cues, prosody, facial expression, physical presence, that partially offset threat misattribution in richer modalities. In contexts of accumulated relational conflict, even these cues are insufficient: prior negative interaction history lowers the amygdala's threat threshold via predictive activation (Barrett, 2017), meaning the system arrives pre-primed before the first word is exchanged. It is in precisely this context, digitalised, history-laden, cue-stripped, that intent prediction conditioned on relational context offers the greatest marginal value.

Digital text also introduces a structural property that face-to-face exchange cannot offer: the pause between receiving a message and replying. During this pause, the receiver typically forms an interpretation of the sender's intent — often a threat-biased one, because the amygdala has already tagged the message before the slower cortical reasoning completes. This pause is a cognitive reappraisal window (Gross, 1998; Ochsner & Gross, 2005), one of the most robust emotion-regulation mechanisms available. The intervention instrument fills that window with an alternative interpretation — what the sender most likely meant, given the relationship context — before the receiver commits to a threat-based reading. In short: the tool shows the user what the sender probably meant, in the moment between reading a message and reacting to it, so the user can decide how to respond based on probable intent rather than initial gut reaction.

### 2.2 Mentalising and the TPJ

Successful communication requires attributing the correct mental state, intent, belief, desire, to the sender. This process, variously termed mentalising or theory of mind, is strongly associated with the TPJ, medial prefrontal cortex, and posterior superior temporal sulcus (Saxe & Kanwisher, 2003; Frith & Frith, 2006). TPJ activation is specifically associated with attributing mental states to others that differ from one's own, precisely the cognitive operation required to override a threat-parsed reception of an ambiguous message with an intent-informed interpretation.

The intervention instrument is designed to externalise and scaffold this TPJ-mediated operation: it shows the receiver the most probable intent distribution for the message they just read, conditioned on sender identity and shared relational history. We hypothesise that repeated exposure to this externally-provided intent signal, analogous to corrective feedback in attentional training paradigms (Davidson & Lutz, 2008), may, over 60 days, measurably shift the balance between amygdala-dominant and TPJ-mediated processing of emotionally ambiguous messages. This is H₃: exploratory, grounded in the neuroplasticity literature, and designed to be measurable.

### 2.2.1 A Scientific Prediction: Elevated Intent Gap in Neurodivergent Dyads

A secondary scientific prediction follows directly from the biological mechanism. If the intent gap arises from asymmetry between subcortical threat-tagging and cortical mentalising, it should be systematically elevated in neurodivergent dyads. For autistic individuals, mentalising circuitry is recruited with greater effort and less automaticity in attributing mental states to others (Lombardo et al., 2011; Frith & Frith, 2006). For individuals with ADHD, attentional load during message reading may reduce cognitive resources available for pragmatic inference. In both cases, the mechanism predicts a wider intent gap on average, not a deficit of communicative intent, but a structural asymmetry in pragmatic signal processing that the intervention is specifically designed to scaffold.

This is a falsifiable prediction. The model will include a pre-registered secondary analysis of intent gap scores stratified by neurodivergent/neurotypical annotator pairing, testing whether Jensen-Shannon divergence between SI and PI distributions is significantly larger when annotator pairs include a neurodiverse rater. If confirmed, the intervention is not merely accessible to neurodiverse users, it is *most scientifically relevant* to them. This extends the *Collective Flourishing* impact pathway to the population where miscommunication has the sharpest biological basis.

We acknowledge that wider JS-divergence in ND-annotated messages may reflect annotator-reliability differences (ND annotators disagreeing more with each other) rather than communicative intent gaps per se. To disentangle these, we will separately compute (a) intra-ND-annotator agreement (κ within the ND annotator pool) and (b) cross-NT/ND annotator agreement, and report both alongside the primary JS-divergence comparison.

### 2.3 Dyadic History as Primary Signal

A fundamental limitation of existing intent and sentiment models is their treatment of messages as contextually isolated. The same message, "Fine, do whatever you want", has a qualitatively different intent distribution when it comes from a stranger completing a transaction, a colleague under deadline pressure, or a partner of five years in the third day of a conflict. To our knowledge, no existing NLP system conditions its prediction on this relational context. The scientific novelty of this project is the explicit modelling of dyadic relational history as a first-class input to intent prediction, and the empirical test of whether this conditioning produces measurably better predictions than message-content-only models.

Critically, relational history also defines what *good* looks like — and that definition differs for each pair. Two people might regularly misread individual messages but quickly repair misunderstandings and maintain a strong, trusting relationship. A model that only minimises miscommunication per message would misclassify this as dysfunction. The model's success metric is therefore not "minimise miscommunication globally" but "is this pair's communication pattern producing the outcomes they want?" This is measured through the combination of automated intent gap scores (computed from every message) and self-reported relationship quality surveys (PRQC; Fletcher et al., 2000) administered at baseline, Day 30, and Day 60. Relational history is not only the signal for decoding messages — it is the lens through which improvement becomes measurable.

Several adjacent research traditions address related problems without converging on dyadic pragmatic intent. The Rational Speech Act (RSA) framework (Frank & Goodman, 2012) models pragmatic inference as recursive Bayesian reasoning but operates on single-utterance contexts without relational history. The ATOMIC commonsense knowledge graph (Sap et al., 2019) encodes if-then social reasoning at scale but does not condition on dyadic pair-level history or model the sender/receiver divergence specifically. Conversation emotion datasets (e.g., MELD, Poria et al., 2019; IEMOCAP) provide multi-turn dyadic annotations but label emotion or dialogue act rather than communicative intent from dual sender/receiver perspectives. Our contribution is differentiated by the combination: dual-perspective intent annotation conditioned on relationship-type metadata, in messages selected specifically for ambiguity, with JS-divergence as the gap metric.

### 2.4 Inter-Brain Synchrony as Neural Outcome Measure

Hasson et al. (2012) demonstrated that neural coupling between speaker and listener, measured via fMRI, is a strong predictor of successful communication, with greater temporal synchrony associated with better comprehension. Recent work has extended these findings using EEG hyperscanning paradigms (Pérez et al., 2017; Dikker et al., 2017), demonstrating that theta-band inter-brain phase synchrony (IBS) during joint cognitive tasks is measurable, reproducible, and sensitive to communication quality.

We select theta-band IBS as the primary neural outcome measure for the 60-day pilot for three reasons: (1) it is measurable with EEG rather than fMRI, making it accessible within the lab partnership budget; (2) it is sensitive to communicative success and attentional coordination; and (3) a pre/post within-subjects design is sufficiently powered with N = 20–24 participants for a medium effect size.

### 2.5 Individual Personality Context as Complementary Signal

A secondary scientific question asks whether stable individual personality context, encoded via a structured biographical intake instrument grounded in narrative identity methodology (McAdams, 2013) and empathic accuracy paradigms (Ickes, 1993), independently improves intent prediction accuracy before dyadic interaction history has accumulated (the cold-start problem). Unlike standard personality inventories that capture trait scores, the biographical intake instrument captures the episodic basis of communicative behaviour: the specific experiences that shaped a person's conflict response, risk tolerance, and stress signalling. We test this as an ablation condition (H₄, secondary) within the primary model study. The instrument uses 8 guided questions across three layers (identity values, decision architecture, narrative stories) administered in 10–15 minutes. Story-to-intent-theme tagging is manual in the v1 study cohort, isolating the question of whether structured personality context improves accuracy from the separate question of whether automated extraction can. If H₄ is not confirmed, the personality context adds no independent signal beyond dyadic history, a publishable null result with clear theoretical implications. The episodic grounding has direct precedent in autobiographical memory research (Conway & Pleydell-Pearce, 2000): episodic self-defining memories carry stable emotional and behavioural meaning that shapes how individuals generate and interpret communicative acts. Twin-2K-500 (Xu et al., 2024) demonstrated that interview-derived personality data improves LLM behavioural prediction more than fine-tuning on interaction history alone; the biographical intake instrument is a structured adaptation of that finding to intent prediction in relational communication.

The personality context instrument serves a dual function. As a research instrument, it conditions intent prediction at cold start (H4 ablation). As a product instrument, it captures the user's stable identity, but critically, people communicate differently with different people — a user may be direct with their best friend but guarded with their co-parent. The personality context therefore operates as a base layer (who you are) complemented by per-relationship context (how you communicate with this specific person), learned progressively through use. The base personality context is created once via the biographical intake; per-relationship context accumulates automatically as the user interacts with the system about messages from specific people, enabling the model to condition predictions on `P(intent | message, personality_context, relationship_context)` where relationship context is dyad-specific.

For the consent-gated mutual sharing pathway (Year 2): the raw biographical answers are never shared; only the derived identity model is accessible, and only under explicit mutual consent with full revocation rights. This operationalises Gottman's (1994) love map construct computationally — a structured, queryable representation of a partner's inner world that enables indirect probing of another's thinking without the face-threat cost of direct questioning (Brown & Levinson, 1987). Humans routinely avoid direct questions about a partner's inner world to avoid rejection or confrontation; the ability to probe indirectly, safely, and accurately addresses a gap that no existing relational tool resolves.

### 2.6 Formal Hypotheses

**H₁, Computational (Primary):** A RoBERTa-large model fine-tuned on perceived-intent prediction, with a 16-dimensional dyadic relational context vector concatenated to the [CLS] token representation, will achieve significantly higher macro-averaged F1 on perceived-intent prediction for emotionally ambiguous messages than an ablated message-only baseline (paired t-test, α = 0.05, minimum effect size Cohen's d ≥ 0.3). H₄ (below) is embedded as an ablation condition within this study, not as a co-equal fourth hypothesis.

Note: relational context in Study 1 is operationalised as controlled metadata (relationship type, duration, valence) rather than verbatim interaction history. H₁ therefore tests whether structured relational metadata shifts intent prediction, a necessary precondition for the richer naturalistic-history version of the hypothesis, which is a Year 2 target.

**H₂, Behavioural (Secondary):** Participants using the browser extension for 60 days will show a significant reduction in intent gap score compared to their own Day 0 baseline, indicating that closed-loop intent feedback changes how people compose emotionally ambiguous messages (within-subjects, paired Wilcoxon signed-rank test, α = 0.05). This computational measure is complemented by validated survey instruments: the Perceived Relationship Quality Components scale (PRQC; Fletcher et al., 2000) administered at baseline, Day 30, and Day 60, providing self-reported communication quality data that can be triangulated against the automated intent gap metric. The combination of automated measurement (intent gap scores from every message) and periodic surveys (self-reported relationship quality) provides both continuous granular data and the subjective experience measures that reviewers may find more immediately interpretable.

**H₃, Neural (Exploratory Stretch Goal — contingent on lab partner, see Section 4):** Dyadic pairs who complete 60 days of closed-loop intent feedback will show a significant increase in theta-band inter-brain phase synchrony (IBS — a measure of how synchronised two people's brain activity becomes during communication) during ambiguous-message reading tasks compared to Day 0 baseline (within-subjects, paired Wilcoxon signed-rank test, α = 0.05). We hypothesise that IBS increase reflects improved mentalising coordination between the pair, consistent with the inter-brain synchrony literature (Pérez et al., 2017; Dikker et al., 2017). **If the EEG pilot is deferred** (due to lab partner unavailability), H₃ is replaced by a survey-based behavioural proxy: the Perceived Relationship Quality Components scale (PRQC; Fletcher et al., 2000) and a custom communication satisfaction scale administered at baseline, Day 30, and Day 60, measuring whether participants self-report improved communication quality after 60 days of intent feedback. This survey-based approach is less scientifically ambitious but still provides publishable evidence of behavioural change.

**H₄, Computational Ablation (Secondary, within Study 1b):** A model conditioned on both the 16-dimensional dyadic relational context vector and the biographical intake instrument personality context block will achieve significantly higher intent prediction accuracy at Day 1 (cold start) than the dyadic-context-only model, with the gap narrowing as dyadic history accumulates over four weeks (one-tailed t-test, α = 0.05, power = 0.80). This is tested in Study 1b and reported as a secondary ablation within H₁.

H₄ primary metric: intent prediction accuracy on a researcher-labelled held-out evaluation set of 100 ambiguous messages (drawn from Study 1b participants' actual messages, with SI labels assigned by two independent raters blind to group assignment, κ computed). The model's predicted intent distribution is compared against the rater-consensus SI label using macro-averaged F1, separately for Group A and Group B at Day 1, Day 14, and Day 28. Secondary metric: time-to-convergence, the week at which Group B's F1 reaches Group A's Week 4 F1 (testing whether personality context accelerates accuracy accumulation). User self-annotation ratings (1–5) are retained as a tertiary engagement metric only, not as an accuracy measure.

**H5, Exploratory (Beyond Fellowship Year):** Consent-gated indirect probing of a partner's personality model will produce higher empathic accuracy gains than equivalent amounts of direct conversation, because it removes the face-threat cost (Brown & Levinson, 1987) that suppresses authentic question-asking in direct interaction (Ickes, 1993). This hypothesis is not tested within the fellowship year; it is stated here as a formal research question for Year 2, grounded in the empathic accuracy (Ickes, 1993) and intimacy process (Reis & Shaver, 1988) literatures.

---

## Section 3: Methods & Work Plan

### Overview of Studies

The research programme consists of four interconnected studies, each building on the previous:

```
Study 1 (Months 1-3): DATASET CREATION
  Build 2,000-message annotated dataset with dual SI/PI labels
  Output: Training data for the model
        │
        ▼
Study 1b (Months 3-7): PERSONALITY CONTEXT ABLATION (H₄)
  100 users, randomised: half get personality intake, half don't
  Test: Does knowing WHO the person is improve predictions?
  Output: H₄ confirmed or falsified
        │
        ▼
Study 2 (Months 3-6): MODEL TRAINING & H₁ VALIDATION
  Train intent prediction model on Study 1 dataset
  Test: Does relational context improve predictions?
  Output: H₁ confirmed or falsified; model released open-source
        │
        ▼
Study 3 (Months 6-8): BRAIN-SCORE VALIDATION [SHOULD]
  Submit model to MIT Brain-Score benchmark
  Test: Are the model's internal representations neurally plausible?
        │
        ▼
Study 4 (Months 7-11): 60-DAY PILOT & EEG [SHOULD, needs lab partner]
  20-24 participants use the tool for 60 days
  Test: Does intent feedback change behaviour (H₂) and brain activity (H₃)?
  Fallback: Survey-based measurement if EEG unavailable
```

*MUST = required fellowship deliverable; SHOULD = contingent on lab partner*

---

### 3.1 Dataset Creation: Study 1 (Months 1–3)

**Objective:** This is a controlled experimental stimulus set designed for pragmatic inference research, not a production dataset. The objective is to construct the first neural-pragmatic dataset, to our knowledge, conditioning intent annotation on dyadic relational history, with dual sender-intent / perceived-intent labels and validated inter-rater reliability.

**Sampling procedure:** 2,000 dyadic text messages in English, drawn from 5 relationship types (romantic partners, parent-child, close friends, community/social groups, professional colleagues), with deliberate oversampling of ambiguous-valence messages (target: 60%).

| Source | Target | Method |
|--------|--------|--------|
| Relabelled public datasets (DailyDialog, EmpatheticDialogues) | ~700 messages | Select messages meeting ambiguity criteria; add synthetic relational context metadata; run full SI/PI annotation protocol |
| Researcher-constructed stimuli | ~600 messages | Write messages targeting specific I1–I7 × relationship type × valence cells; 3-rater pre-review; forms the controlled EEG stimulus set |
| LLM-assisted synthetic generation (human-reviewed) | ~700 messages | Structured prompts specifying relationship type, valence, target SI class; mandatory 2-rater human review gate; ~20–30% rejection rate budgeted. This approach uses AI to generate realistic message scenarios that are then verified by human reviewers — combining the scalability of simulation with the validity of human judgment |

The controlled construction of 65% of stimuli is a methodological strength for this purpose: it allows precise control over ambiguity level, emotional valence, and relational context framing, the stimulus properties required for the within-session EEG contrast and for Year 2 fMRI comparability. LLM-assisted synthetic data generation with human review gates is an established methodology (Gilardi et al., 2023; Møller et al., 2023). Ecological validity is addressed by the concurrent naturalistic deployment study (Study 4), which measures the same participants in real-world messaging conditions over 60 days, two environments, same intervention, same participants.

Relational context is provided to annotators as experimentally controlled metadata (relationship type, duration, recent valence) rather than verbatim interaction history. This is a deliberate design choice: it allows systematic variation of the relational signal while controlling message content, the within-subjects contrast required to isolate H₁. Cognitive psychology routinely uses experimentally constructed social scenarios to test social cognition; the controlled framing is the experimental manipulation, not a limitation. Whether richer naturalistic dyadic history (full interaction logs) produces larger effects is an explicit follow-on question for Year 2, contingent on H₁ confirmation.

**Intent label space, 7 categories (I1–I7):**

| ID | Category | Definition |
|----|----------|------------|
| I1 | Seeking connection | Primary goal is relational proximity; content is secondary |
| I2 | Expressing concern | Communicates worry about the receiver's state or wellbeing |
| I3 | Setting a boundary | Signals a limit on behaviour, time, or emotional availability |
| I4 | Seeking validation | Requests acknowledgement or agreement, not action |
| I5 | Expressing frustration | Communicates emotional state as primary payload |
| I6 | Making a request | Clear instrumental ask for action or change |
| I7 | Giving information | Neutral informational content with low emotional valence |

The schema extends Searle's (1976) illocutionary taxonomy with the affiliative and relational intent categories (I1, I2, I4) where the SI/PI gap is largest, categories absent from DailyDialog and the closest NLP prior (Welivita & Pu, 2020), which models listener response rather than sender initiating intent. I4 is grounded in Goffman's (1967) face-work theory.

I8 (chronic self-interest pattern, Gottman 1994) is a relationship-level construct requiring message history; it is explicitly out of scope for single-message annotation in Study 1 and will be explored as a derived signal in Year 2 using the accumulated 60-day interaction logs.

**Annotation constructs — two separate labels per message:**

Each message receives two independent annotations, capturing both sides of the communication:

- **Sender Intent (SI):** What did the writer most likely *intend* to communicate? (The annotator takes the sender's perspective, using the provided relational context to infer the sender's probable goal)
- **Perceived Intent (PI):** What would a reasonable receiver most likely *interpret* from this message in the given relational context? (The annotator takes the receiver's perspective, inferring what a typical reader would understand)

The gap between SI and PI is the core quantity of interest: when what the sender meant and what the receiver understood diverge, miscommunication occurs. This dual-labelling approach — annotating the same message from both perspectives — is, to our knowledge, novel in the NLP literature.

The *intent gap score* is the Jensen-Shannon divergence (JS-divergence — a standard statistical measure of how different two probability distributions are, ranging from 0 for identical to 1 for completely different) between P(SI) and P(PI). This quantifies the measurable distance between communicative intent and communicative reception. To handle distributional sparsity from 5-annotator pools, we apply add-ε Laplace smoothing (ε = 0.01) before computing JS-divergence. JS-divergence scores will be calibrated against independent human ratings of perceived message ambiguity (1–5 Likert) collected from a held-out validation set of 50 messages, to confirm that high JS-divergence scores correspond to messages humans rate as ambiguous.

**Roles — who provides data vs. who annotates:**

- **Message sources:** The 2,000 messages come from public datasets (DailyDialog, EmpatheticDialogues), researcher-constructed stimuli, and LLM-generated synthetic examples — *not* from the annotators themselves. The people who annotate the messages are independent third parties, not the people who sent or received the original messages.
- **Annotators:** 5 independent annotators per message, recruited via Prolific Academic (a research participant platform). Annotators are trained on the 7-category schema and the dual SI/PI labelling task. They read each message with its relational context description and assign labels from both the sender's and receiver's perspective. Annotators are *not* the participants in the 60-day pilot (Study 4) — they are a separate pool of trained labellers.
- **Study 1b participants (separate):** 100 new users who use the tool in their own real messaging. Their messages are annotated by independent raters (not by the participants themselves) for the H₄ evaluation.

**Annotation protocol:** SI and PI annotated separately (two passes), blind to each other; "Ambiguous / I don't know" is a valid response; cultural background recorded as annotator metadata (minimum 3 distinct UK cultural backgrounds); neurodiverse-authored messages included with separate κ computation. Estimated cost: £5,000–7,000 (based on Prolific rate of £10–12/hr for screened annotators; approximately 650 annotator-hours across 2,000 messages × 5 annotators × 2 passes at ~2 min/message, plus κ pilot iterations, cultural background screening premium, and neurodiverse community recruitment via specialist panels).

**Inter-rater reliability:** Before full annotation begins, a 20-message pilot is conducted with 5 independent annotators. Each annotator reads each message (with its relational context description) and assigns both a Sender Intent (SI) label and a Perceived Intent (PI) label from the 7-category schema above. Cohen's κ (a statistical measure of agreement between annotators, where κ > 0.70 indicates substantial agreement) is computed separately for SI labels and PI labels. Gate: if either κ < 0.70 after two adjudication rounds → pause, redesign the label schema, and re-pilot. This ensures the training signal for the model is reliable before any full-scale annotation investment.

**Output:** 2,000-message annotated dataset with SI/PI dual labels, relational context metadata, per-category κ scores. Published on HuggingFace and OpenNeuro.

---

### 3.2 Intent-Conditioned Model Training & H₁ Validation: Study 2 (Months 3–6)

**Base model:** RoBERTa-large (a pre-trained language model with 355M parameters, developed by Facebook AI; Liu et al., 2019). RoBERTa is designed specifically for understanding text — it reads a message and produces a numerical representation that can be used for classification tasks. The task here is classification: assigning a probability distribution over intent categories (i.e., for each message, the model outputs the likelihood of each intent category). RoBERTa-large has an established Brain-Score Language benchmark baseline (Schrimpf et al., 2021), making the Study 3 neural alignment comparison directly interpretable.

**Architecture modification:**
- Relational context vector: a compact numerical summary of the relationship (not 16 messages, but 16 numerical features) encoding: relationship type (5 categories — romantic, parent-child, friends, community, professional — represented as a one-hot vector), relationship duration (continuous, log-scaled), recent interaction valence (a score from −1 to +1 indicating whether recent exchanges were positive or negative), message frequency (how often the pair communicates), and dyad-level intent gap history (rolling 14-day average of how often miscommunication has occurred between this pair)
- Context vector concatenated to the [CLS] token representation (a special summary vector that the model produces to represent the entire input — standard in transformer-based language models) before the classification head
- Personality context block: at inference time, the biographical intake instrument data is converted into a structured 600–900 token context block prepended to the message, conditioning the full encoder forward pass
- Two separate fine-tuning runs: one for SI prediction, one for PI prediction; 7-way softmax over I1–I7

**Experimental conditions for H₁/H₄ ablation:**

| Condition | Description |
|-----------|-------------|
| A (relational context only) | RoBERTa-large + 16-dim dyadic relational context vector; no personality context |
| B (baseline, no context) | RoBERTa-large without any context vector (message content only) |
| C (surface baseline) | RoBERTa-base fine-tuned for sentiment classification |
| D (full model) | RoBERTa-large + 16-dim dyadic relational context vector + personality context block |

H₁ is the contrast Condition A versus Condition B. H₄ is the contrast Condition D versus Condition A at Day 1 (cold start), tracked over four weeks as dyadic history accumulates. This enables clean attribution of accuracy gains: B establishes the message-only floor; A establishes the relational conditioning ceiling; D establishes the incremental contribution of personality context specifically under cold-start conditions.

**Training:** 3 runs per condition × 5 epochs; AdamW optimiser; learning rate sweep (1e-5, 2e-5, 3e-5); early stopping on validation loss. Compute is provided via the Encode fellowship individual compute allocation (minimum £100k). Full ablation sweeps across all four conditions (A–D), hyperparameter search, and multiple training runs are fully resourced. Compute is not a constraining factor for this project.

**Evaluation:** Macro-averaged F1 (a standard accuracy metric that balances precision and recall equally across all intent categories, ensuring the model performs well on rare categories, not just common ones) on a 400-message held-out test set (ambiguous-valence subset prioritised for primary analysis); human majority-vote baseline reported; Expected Calibration Error (ECE — a measure of whether the model's confidence scores are trustworthy: when the model says "70% confident," is it correct roughly 70% of the time?) as a secondary metric, a well-calibrated intent distribution is as scientifically important as high accuracy. Per-class F1 reported alongside macro-averaged F1; classes with fewer than 100 training examples are flagged with wider confidence intervals. The 2,000-sample scale is the appropriate starting point for a relative ablation test (does context improve prediction?), absolute scale is a Year 2 question, contingent on H₁ confirmation.

**Open-source release:** Fine-tuned model weights, fine-tuning code, and evaluation harness released on HuggingFace under Apache 2.0 at Month 5/6.

---

### 3.3 Brain-Score Neural Plausibility Validation: Study 3 (Months 6–8) *(SHOULD)*

**Objective:** Validate that the intent model's internal representations are neurally plausible, that fine-tuning on pragmatic intent prediction enhances, rather than degrades, alignment with human language-selective neural responses.

The trained model is submitted to the MIT Brain-Score Language benchmark (Schrimpf et al., 2021), targeting Pereira2018, Fedorenko2016, and Blank2014 benchmarks. Hidden-state activations are extracted at each transformer layer; linear regression probes are fit to fMRI ROI activations in language-selective cortex (IFG, aMTG, pMTG, PostTemp, AnGyd). If the intent model scores above RoBERTa-base on language-selective neural alignment, this suggests pragmatic fine-tuning enhances the model's similarity to human neural language processing. If it scores below, this suggests a productive tension between pragmatic optimisation and neural plausibility. Both outcomes are publishable. This study does not gate H₁ and requires approximately two weeks of engineering work post-training.

---

### 3.4 60-Day Pilot & EEG Validation: Study 4 (Months 7–11) *(SHOULD, requires lab partner)*

The browser extension is a first-party research prototype, a necessary component of the experimental design, not a commercial product. Its development follows HCI research prototype standards: sufficient for a controlled 60-day study with 20-24 participants, researcher-supported, not publicly released. The engineering scope is minimum-viable for valid data collection: intent prediction display, event-contingent reflection prompting, and encrypted local logging. This is consistent with how HCI and CSCW researchers routinely build and deploy research systems (Fogg et al., 2002; Consolvo et al., 2008). Building this instrument is not peripheral to the science, it is the delivery mechanism for H2 and H3, and its design and evaluation constitute a contribution to the HCI literature independent of the neural findings.

**Objective:** Test H₂ (behavioural) and H₃ (neural), does 60 days of intent feedback produce measurable behavioural and neural shifts?

**Design:** Within-subjects pre/post; N = 20–24 (12 dyadic pairs): couples or close friends, ≥6 months established relationship, English-speaking; powered for medium effect size (d = 0.5, 80% power, α = 0.05). The d = 0.5 assumption is imported from theta-band IBS studies in related contexts (Pérez et al., 2017; Dikker et al., 2017) and may not hold for a text-based intervention paradigm. We therefore treat the EEG pilot as hypothesis-generating: a confirmed effect at any size justifies a powered Year 2 study; a null result is informative about the neural pathway hypothesis independently of H₁ and H₂.

**Intervention:** 60-day use of the browser extension (intervention instrument) in naturalistic digital messaging contexts. EEG pilot participants are recruited from the pilot cohort, individuals whose neural change is measured in the lab also generate continuous real-world intent gap data in naturalistic messaging usage, enabling a two-environment validation: controlled lab (EEG) and naturalistic deployment (browser extension) measuring the same intervention simultaneously.

**EEG sessions:** Day 0 (baseline) and Day 60 (post-intervention) at lab partner facility.
- Equipment: 64-channel active EEG, standard 10-20 placement
- Task: standardised dyadic ambiguous-message reading (40 messages from the researcher-constructed Study 1 subset); both participants simultaneously read messages and rate perceived intent; EEG recorded throughout; within-session contrast between ambiguous and disambiguated (context-provided) blocks
- The stimulus set is drawn exclusively from researcher-constructed stimuli because full control over ambiguity level, valence, and relational context is required for the within-session contrast and for Year 2 fMRI comparability

**Primary EEG analysis (pre-registered):** Theta-band (4–8 Hz — a frequency range associated with attentional coordination and communication) inter-brain phase synchrony (IBS — a measure of how synchronised two people's brain activity is during a shared task) between dyad members during ambiguous-message reading blocks; pre vs. post comparison: paired Wilcoxon signed-rank test; secondary correlation between individual intent gap score decline (browser extension metric, Days 1–60) and IBS increase.

**Exploratory EEG analysis:** ERP (Event-Related Potential — brain voltage changes time-locked to specific events, in this case reading an ambiguous message) analysis, specifically the N2 and P3 components (brain responses occurring ~200ms and ~300ms after stimulus onset, respectively, associated with conflict detection and attentional allocation). Reported as preliminary findings with appropriate statistical caveats.

**Behavioural measures (continuous, 60 days):** Intent gap score per sent message (JS-divergence, automated); self-reported relationship quality (PRQC, Fletcher et al., 2000) at baseline, Day 30, Day 60; lightweight structured reflection journal providing event-contingent micro-prompts after high-divergence exchanges (~3 minutes) and weekly narrative reflections (~7 minutes). Semi-structured prompts outperform free writing for metacognitive development (Pavlacic et al., 2019); event-contingent triggering outperforms scheduled prompts for ecological validity (Shiffman, Stone, & Hufford, 2008). Journal data are analysed as an exploratory secondary measure; participant burden is approximately 15–20 minutes per week. fMRI is explicitly out of scope for Year 1; regional activation analysis (TPJ vs. amygdala) is a Year 2 extension contingent on Year 1 EEG results.

---

### 3.5 12-Month Work Plan

| Period | Primary Activity | Key Output | Tier |
|--------|-----------------|------------|------|
| Month 1 | κ pilot (20 messages, 5 annotators); annotation tooling; ethics application submitted with lab partner; Study 1b cohort pre-screened and waitlisted pending ethics approval | Annotation protocol validated; ethics in review; Study 1b cohort pre-screened | MUST |
| Months 1–3 | Full 2,000-message annotation; dataset QA; online behavioural H₂ probe (N=50, online, no EEG) | Annotated dataset v1.0; early H₁ signal | MUST |
| Month 3 | Ethics approval received; Study 1b Group B completes biographical intake; data collection begins | Study 1b data stream active | MUST |
| Months 3–7 | Study 1b data collection: Group A (relational-context-only model) and Group B (model + personality context, 10–15 min intake at Day 1); 2× weekly sender self-annotation protocol; engagement tracking as ANCOVA covariate | Study 1b primary dataset | MUST |
| Months 3–6 | RoBERTa-large fine-tuning; ablation studies (Conditions A, B, C, D); evaluation vs. baselines; demo Streamlit app | H₁ confirmed/falsified; model released on HuggingFace | MUST |
| Months 7–8 | Study 1b primary analysis: researcher-labelled held-out evaluation set scoring (macro-averaged F1, Group B vs. Group A at Day 1, Day 14, Day 28); personality context layer ablation; null result analysis protocol | H₄ ablation confirmed or falsified | MUST |
| Month 5 | Paper draft #1: dataset + model + H₁ | Submitted to arXiv; circulated to lab partner | MUST |
| Months 5–6 | Study 1b publication preparation; target venues: ACL, EMNLP, or CHI | Paper #2 draft (Study 1b) | MUST |
| Months 6–8 | Brain-Score submission; EEG pilot design finalised; IRB approval for EEG pilot; participant recruitment; Intervention instrument (browser extension) deployed to pilot cohort | Brain-Score result; pilot protocol approved | SHOULD |
| Months 7–11 | 60-day EEG pilot; continuous intent gap data from naturalistic deployment cohort; Day 0 and Day 60 EEG sessions | H₂/H₃ data collected | SHOULD |
| Months 11–12 | Data analysis; paper draft #2 (full study: dataset + model + pilot + EEG); submission | Paper submitted to peer-reviewed venue | MUST |

**Study 1b design summary:** Randomised controlled trial; N = 100 new users (50 per arm); recruitment and pre-screening in Month 1 (waitlisted pending ethics); data collection Months 3–7; 4 weeks active data collection per participant + 1-week annotation follow-up; Group A: standard onboarding with no personality context (relational history only); Group B: 10–15 min Mode A biographical intake at Day 1, personality context active from first session. Primary metric: intent prediction accuracy on a researcher-labelled held-out evaluation set of 100 ambiguous messages (drawn from Study 1b participants' actual messages, SI labels assigned by two independent raters blind to group assignment, κ computed); macro-averaged F1 compared across Group A and Group B at Day 1, Day 14, and Day 28. Secondary metric: time-to-convergence (week at which Group B's F1 reaches Group A's Week 4 F1). Engagement level (messages sent, sessions/week, days active) included as ANCOVA covariate; both unadjusted and engagement-adjusted effects reported. User self-annotation ratings (1–5) retained as a tertiary engagement metric only. A null result in H₄ is planned for: it constrains the theoretical space for personality context conditioning research and is publishable in its own right.

---

## Section 4: Lab Environment & Collaboration

*Lab partner outreach is active as of March 2026, with expressions of interest being sought from UCL Functional Imaging Laboratory (Prof. Karl Friston's group), MRC Cognition and Brain Sciences Unit Cambridge, and the University of Nottingham Social Neuroscience Group. A confirmed lab name, PI, and letter of intent will be inserted here before submission. If lab partnership is not confirmed by Month 3 of the fellowship, the EEG pilot (Study 4) is formally deferred to Year 2, and the fellowship deliverables revert to the MUST tier: dataset + H1 model + Study 1b (H4 ablation) + online behavioural H2 probe. The core scientific contribution does not depend on Study 4.*

**What the lab partner provides:**
- EEG equipment (64-channel active system) and lab space for Day 0 and Day 60 sessions
- Existing IBS hyperscanning paradigm and validated MNE-Python / EEGLAB analysis pipeline, extending prior inter-brain synchrony work, not designing from scratch
- Ethics / IRB umbrella applied for jointly in Month 1, accelerating approval timeline

**What I bring to the lab:**
- Complete dataset pipeline, annotation tooling, and quality assurance infrastructure
- Foundation model training, evaluation, and open-source release
- Biographical intake instrument (Mode A), story annotation protocol, inference-time injection architecture
- Browser extension (intervention instrument delivery mechanism), analysis code for intent gap metrics and JS-divergence, full reproducibility infrastructure (DVC, HuggingFace Hub, OpenNeuro)

The bottleneck in most AI-for-neuroscience projects is build velocity, getting from scientific question to working instrument to deployable experiment. Most neuroscience labs do not have engineers who can take a model from idea to browser extension in two weeks. The lab brings experimental rigour, ethics infrastructure, and neural measurement capability that a solo engineer cannot access. Together we can run an empirical programme in 12 months that would take a standard lab three years.

---

## Section 5: Risks, Ethics & Mitigation

### 5.1 Scientific Risks

**Risk 1, Ground truth problem (κ < 0.70):** If human annotators cannot reliably agree on sender and perceived intent, the training signal is invalid. *Mitigation:* κ pilot in Month 1 before any full annotation begins; if κ fails after two adjudication rounds, the schema is redesigned before proceeding.

**Risk 2, H₁ null result:** Relational context may not significantly improve intent prediction at this model scale and label granularity. *Mitigation:* A null result is explicitly a publishable outcome, the first rigorous test of the dyadic conditioning hypothesis. The project does not depend on H₁ being confirmed; it depends on H₁ being rigorously tested.

**Risk 3, Lab partner confirmation delayed:** If no lab partner letter of intent is secured before the submission deadline, the EEG pilot (SHOULD tier) is at risk. *Mitigation:* Lab partner outreach initiated the week of 15 March. The MUST tier (dataset + model + paper) is fully executable without a lab partner; SHOULD tier is explicitly contingent.

**Risk 4, IRB / ethics approval delay:** Ethics applications take 4–12 weeks at UK institutions. *Mitigation:* Ethics application submitted jointly with lab partner in Month 1 using the lab's existing ethics framework; Study 1b data collection does not begin until Month 3 (post-approval); EEG sessions are not on the critical path until Month 7.

### 5.2 Ethical Risks & Mitigations

**1. Cultural and linguistic label bias:** Intent categories and their surface signals vary across cultures. *Mitigation:* Minimum 3 distinct cultural backgrounds in the 5-annotator pool; per-culture κ reported; high cross-cultural-variance categories flagged with wider model confidence intervals.

**2. Neurodiverse communication style mislabelling:** Neurodiverse communicators use pragmatic structures that diverge from neurotypical norms. *Mitigation:* Neurodiverse-authored messages explicitly included (recruited via autism/ADHD community groups); separate κ computed on neurodiverse subset; model error rates on neurodiverse messages explicitly reported.

**3. Downstream harm in vulnerable relationships:** A false low gap score could discourage help-seeking in high-stakes contexts. *Mitigation:* High-entropy distributions displayed as "high ambiguity" flags, not false confidence. When the model shows sustained divergence combined with high self-interest asymmetry, the intervention instrument displays an explicit safeguarding signpost directing users to the National Domestic Abuse Helpline, a designed feature reviewed with the ethics board in Month 1.

**4. Domestic abuse / coercive control scenario:** The on-device relational data could become a surveillance instrument if a controlling partner accesses the device. *Mitigation:* All data encrypted at rest (AES-256, device keychain); no cloud sync in MVP; biometric/PIN gate on all data access; no partner access to any user's data is permitted at any consent level, this is a design constraint, not a configuration option. Device-level encryption (AES-256) and biometric gates address third-party access but not coercive unlocking. Additional mitigations: (1) a rapid account deletion feature accessible from the app's first screen without authentication, enabling users to erase all data in one tap; (2) a session-disabling gesture (configurable 3-tap sequence) that clears the session and returns to a neutral state; (3) the app displays no identifying information on the lock screen or in the app switcher. These features will be reviewed with the ethics board in Month 1 as part of the safeguarding protocol.

**5. Participant data in EEG pilot:** EEG and behavioural data from 20–24 participants requires secure handling. *Mitigation:* Full ethics application submitted Month 1 with lab partner; informed consent covers EEG recording, 60-day message metadata collection (no message content; intent gap scores only), and data retention; participants can withdraw at any time with data deletion.

**6. Biographical intake instrument as sensitive personal data:** The biographical intake instrument contains personal narratives, ranked values, biographical stories, and self-reported decision architecture, qualitatively more sensitive than behavioural metadata. *Mitigation:* All biographical intake data is local-first, AES-256 encrypted at rest, not shareable with any partner or third party, and fully deletable at any time. Explicit informed consent required; purpose limitation and enhanced security controls enforced. IRB review required before any research use. Ablation-first principle as ethical safeguard: biographical intake fields that do not measurably improve H₄ are removed before v2, preventing accumulation of personal data that does not serve a demonstrated scientific purpose. Reviewed with ethics board in Month 1.

---

## Section 6: Bibliography

1. Adolphs, R. (2002). Recognizing emotion from facial expressions: Psychological and neurological mechanisms. *Behavioural and Cognitive Neuroscience Reviews*, 1(1), 21–62.
2. Barrett, L. F. (2017). *How emotions are made: The secret life of the brain*. Houghton Mifflin Harcourt.
3. Blank, I., Kanwisher, N., & Fedorenko, E. (2014). A functional dissociation between language and multiple-demand systems revealed in patterns of BOLD signal fluctuations. *Journal of Neurophysiology*, 112(5), 1105–1118.
4. Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313–7318.
5. Brown, P., & Levinson, S. C. (1987). *Politeness: Some universals in language usage*. Cambridge University Press.
6. Collins, N. L., & Miller, L. C. (1994). Self-disclosure and liking: A meta-analytic review. *Psychological Bulletin*, 116(3), 457–475.
7. Consolvo, S., McDonald, D. W., & Landay, J. A. (2008). Theory-driven design strategies for technologies that support behaviour change in everyday life. *CHI 2008*, 405–414.
8. Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review*, 107(2), 261–288.
9. Davidson, R. J., & Lutz, A. (2008). Buddha's brain: Neuroplasticity and meditation. *IEEE Signal Processing Magazine*, 25(1), 176–174.
10. Dikker, S., Wan, L., Davidesco, I., Kaggen, L., Oostrik, M., McClintock, J., ... & Poeppel, D. (2017). Brain-to-brain synchrony tracks real-world dynamic group interactions outside the laboratory. *Current Biology*, 27(9), 1375–1380.
11. Fedorenko, E., Behr, M. K., & Kanwisher, N. (2011). Functional specificity for high-level linguistic processing in the human brain. *PNAS*, 108(39), 16428–16433.
12. Fletcher, G. J., Simpson, J. A., & Thomas, G. (2000). The measurement of perceived relationship quality components: A confirmatory factor analytic approach. *Personality and Social Psychology Bulletin*, 26(3), 340–354.
13. Finn, E. S., Huber, L., Jangraw, D. C., Molfese, P. J., & Bandettini, P. A. (2024). Post-interaction neuroplasticity of inter-brain networks predicts social motivation. *PNAS*, 121(5), e2311771121.
14. Fogg, B. J., Soohoo, C., Danielson, D., Marable, L., Stanford, J., & Tauber, E. R. (2002). How do people evaluate a web site's credibility? *Stanford Persuasive Technology Lab Technical Report*.
15. Frank, M. C., & Goodman, N. D. (2012). Predicting pragmatic reasoning in language games. *Science*, 336(6084), 998.
16. Frith, C. D., & Frith, U. (2006). The neural basis of mentalizing. *Neuron*, 50(4), 531–534.
17. Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS*, 120(30), e2305016120.
18. Goffman, E. (1967). *Interaction Ritual: Essays on Face-to-Face Behaviour*. Anchor Books.
19. Gottman, J. M. (1994). *What Predicts Divorce? The Relationship Between Marital Processes and Marital Outcomes*. Lawrence Erlbaum Associates.
20. Grice, H. P. (1975). Logic and conversation. In P. Cole & J. Morgan (Eds.), *Syntax and Semantics, Vol. 3: Speech Acts* (pp. 41–58). Academic Press.
21. Gross, J. J. (1998). Antecedent- and response-focused emotion regulation: Divergent consequences for experience, expression, and physiology. *Journal of Personality and Social Psychology*, 74(1), 224–237.
22. Haidt, J., & Rose-Stockwell, T. (2019). The dark psychology of social networks. *The Atlantic*, December 2019.
23. Hasson, U., Ghazanfar, A. A., Galantucci, B., Garrod, S., & Keysers, C. (2012). Brain-to-brain coupling: A mechanism for creating and sharing a social world. *Trends in Cognitive Sciences*, 16(2), 114–121.
24. Higgins, E. T. (1987). Self-discrepancy: A theory relating self and affect. *Psychological Review*, 94(3), 319–340.
25. Ickes, W. (1993). Empathic accuracy. *Journal of Personality*, 61(4), 587–610.
26. LeDoux, J. E. (1996). *The Emotional Brain: The Mysterious Underpinnings of Emotional Life*. Simon & Schuster.
27. Li, Y., Su, H., Shen, X., Li, W., Cao, Z., & Niu, S. (2017). DailyDialog: A manually labelled multi-turn dialogue dataset. *Proceedings of IJCNLP 2017*, 986–995.
28. Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., ... & Stoyanov, V. (2019). RoBERTa: A robustly optimized BERT pretraining approach. *arXiv:1907.11692*.
29. Lombardo, M. V., Chakrabarti, B., Bullmore, E. T., Wheelwright, S. J., Sadek, S. A., Suckling, J., ... & Baron-Cohen, S. (2011). Specialization of right temporo-parietal junction for mentalizing and its relation to social impairments in autism. *NeuroImage*, 56(3), 1832–1838.
30. McAdams, D. P. (2013). The psychological self as actor, agent, and author. *Perspectives on Psychological Science*, 8(3), 272–295.
31. McGaugh, J. L. (2000). Memory, a century of consolidation. *Science*, 287(5451), 248–251.
32. Mikulincer, M., & Shaver, P. R. (2003). The attachment behavioral system in adulthood. *Advances in Experimental Social Psychology*, 35, 53–152.
33. Møller, A. G., Dalsgaard, J., Pera, A., & Aiello, L. M. (2023). Is a prompt and a few samples all you need? Using GPT-4 for data augmentation in low-resource classification tasks. *arXiv:2304.13861*.
34. Ochsner, K. N., & Gross, J. J. (2005). The cognitive control of emotion. *Trends in Cognitive Sciences*, 9(5), 242–249.
35. Öhman, A., & Mineka, S. (2001). Fears, phobias, and preparedness: Toward an evolved module of fear and fear learning. *Psychological Review*, 108(3), 483–522.
36. Pavlacic, J. M., Buchanan, E. M., Maxwell, N. P., Hopke, T. G., & Schulenberg, S. E. (2019). A meta-analysis of expressive writing on posttraumatic stress, posttraumatic growth, and quality of life. *Review of General Psychology*, 23(2), 230–250.
37. Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017). Brain-to-brain entrainment: EEG interbrain synchronization while speaking and listening. *Scientific Reports*, 7(1), 4190.
38. Poria, S., Hazarika, D., Majumder, N., Naik, G., Cambria, E., & Mihalcea, R. (2019). MELD: A multimodal multi-party dataset for emotion recognition in conversations. *Proceedings of ACL 2019*.
39. Rashkin, H., Smith, E. M., Li, M., & Boureau, Y. L. (2019). Towards empathetic open-domain conversation models: A new benchmark and dataset. *Proceedings of ACL 2019*, 5370–5381.
40. Reis, H. T., & Shaver, P. (1988). Intimacy as an interpersonal process. In S. Duck (Ed.), *Handbook of Personal Relationships* (pp. 367–389). Wiley.
41. Sap, M., Le Bras, R., Allaway, E., Bhagavatula, C., Lourie, N., Rashkin, H., ... & Choi, Y. (2019). ATOMIC: An atlas of machine commonsense for if-then reasoning. *Proceedings of AAAI*, 33, 3027–3035.
42. Saxe, R., & Kanwisher, N. (2003). People thinking about thinking people: The role of the temporo-parietal junction in "theory of mind." *NeuroImage*, 19(4), 1835–1842.
43. Schrimpf, M., Blank, I., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., ... & Fedorenko, E. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*, 118(45), e2105646118.
44. Searle, J. R. (1976). A classification of illocutionary acts. *Language in Society*, 5(1), 1–23.
45. Shiffman, S., Stone, A. A., & Hufford, M. R. (2008). Ecological momentary assessment. *Annual Review of Clinical Psychology*, 4, 1–32.
46. Singer, T. (2025). A neuroscience perspective on the plasticity of the social and relational brain. *Annals of the New York Academy of Sciences*, 1544, 15–34.
47. Sitaram, R., Ros, T., Stoeckel, L., Haller, S., Scharnowski, F., Lewis-Peacock, J., ... & Sulzer, J. (2017). Closed-loop brain training: The science of neurofeedback. *Nature Reviews Neuroscience*, 18(2), 86–100.
48. Sperber, D., & Wilson, D. (1986). *Relevance: Communication and Cognition*. Harvard University Press.
49. Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., & Bowman, S. R. (2018). GLUE: A multi-task benchmark and analysis platform for natural language understanding. *arXiv:1804.07461*.
50. Welivita, A., & Pu, P. (2020). A taxonomy of empathetic response intents in human social conversations. *Proceedings of COLING 2020*, 4444–4453.
51. Xu, H., Zhao, H., Gu, W., Xu, L., Zhu, L., Liu, T., & Zhao, Z. (2023). MIntRec2.0: A large-scale benchmark dataset for multimodal intent recognition and out-of-scope detection in conversations. *arXiv:2309.04421*.
52. Xu, Y., Wei, L., Liu, C., & Zhang, T. (2024). Twin-2K-500: Interview-derived personality data improves LLM behavioural prediction. *Proceedings of EMNLP 2024*.
53. Harari, Y. N. (2018). *21 Lessons for the 21st Century*. Spiegel & Grau.
54. O'Neil, C. (2016). *Weapons of Math Destruction: How Big Data Increases Inequality and Threatens Democracy*. Crown.

---

## Appendix A: Product Vision & Impact Pathway *(Beyond 12 Months)*

*This appendix describes the longer-term vision for reviewers interested in the commercial and societal pathway. It is not part of the 12-month fellowship commitment.*

**What the intervention instrument does, in plain terms:** When a user receives an ambiguous text message (e.g., "Can we talk tonight?" from their partner), the browser extension shows them what the sender most likely *meant* — for example, "Most likely: seeking connection (72% confidence), possibly: expressing concern (18%)" — before the user writes their reply. The tool shows intent, not just tone. Over 60 days, we test whether repeatedly seeing this intent prediction changes how people interpret and respond to messages.

The intervention instrument is designed on a three-horizon arc. Each horizon is unlocked by the science of the previous one.

**Horizon 1, The Mirror (Fellowship year):** One person. One message. One instrument. The intent gap made visible: P(intent | message, relational history, personality context). The Relationship Digital Twin maps the semantic space of one relationship: convergence, divergence, pattern asymmetry. The Mirror's self-model is anchored by the biographical intake instrument, the classifier infers what the user does; the instrument captures what they intend; together they form a triangulated model of communicative identity. The improvement signal is convergence across all three streams, inferred behaviour (classifier), stated intent and personality architecture (biographical intake), and stated aspiration (reflection journal), the point at which who you are as a communicator, what you mean to say, and who you want to be begin to align. The individual personality context instrument doubles as a consent-gated relational bridge: each person gains a structured window into their own identity model, and when both partners are ready, a mutual soul surface, a curated, revocable view of how the other thinks, becomes available, making the Mirror simultaneously a self-understanding instrument and a foundation for deeper dyadic knowing. A downstream commercial application of the Mirror is private, context-aware response assistance: positioned in the same cognitive reappraisal window the instrument occupies, the on-device model can generate response options conditioned on the user's Soul Document and dyadic history — a privacy-preserving alternative to decontextualised AI advice for personal and relational situations, testable as a formal product hypothesis (H₅, AI-MC) beyond the fellowship year.

**Horizon 2, The Bridge (Post-fellowship, when the science is ready):** Two people. Mutual consent. Both instruments active. With one symmetric, revocable consent interaction, each person's intent model is shared with the other, not raw messages, not personal data, but intent representation vectors and reception model parameters. The gap score updates from both sides simultaneously. Grounded in inter-brain synchrony research (Hasson et al., 2012), the Bridge scaffolds the neural coupling that predicts communicative success. The Bridge, when built, will not expose biographical intake content to partners, the two-person intent model shares intent representation vectors, not the underlying personality architecture that produced them.

**Horizon 3, The Map (Long-run vision):** Thousands of consented pairs. An empirical atlas of communicative intent at population scale, where misunderstanding concentrates, where understanding spontaneously forms, what closing the gap looks like across cultures, relationship types, and demographics. Data enabling population-scale study of communicative intent and its neural correlates.

**ARIA alignment:** *Scalable Neural Interfaces*, the intent-conditioned model and dataset are computational tools that interface with human neural language processing, validated against neural data via Brain-Score, designed to scaffold mentalising circuitry. *Collective Flourishing*, the Map is the long-term vision: intent infrastructure that reduces the structural cost of human miscommunication at population scale, built on a consent-based design rather than attention extraction.

---

*Technical specifications for the intent-conditioned model architecture and the biographical intake instrument are available on request.*
