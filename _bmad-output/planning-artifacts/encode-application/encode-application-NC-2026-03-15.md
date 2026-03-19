---
title: "NeuroAI Cognitive Companion: An Intent-Conditioned Language Model Grounded in Dyadic Relational History"
subtitle: "Encode x Pillar VC AI for Science Fellowship Application"
author: Snnair
date: 2026-03-15
status: draft
sourceDocument: _bmad-output/planning-artifacts/product-brief-NC-2026-03-14.md
---

# NeuroAI Cognitive Companion
## An Intent-Conditioned Language Model Grounded in Dyadic Relational History

**Encode x Pillar VC AI for Science Fellowship, Application**
**Applicant:** Snnair
**Date:** March 2026
**ARIA Spaces:** Scalable Neural Interfaces · Collective Flourishing

---

## Section 1: Overview

**Scientific question:** Can a language model conditioned on dyadic relational history, combined with a closed-loop intent feedback intervention, measurably reduce miscommunication and produce detectable changes in neural markers of mentalising versus threat processing over 60 days?

The most powerful capability a human being can have in the AI era is not a technical skill or an information advantage — it is trust. As artificial intelligence absorbs more of the cognitive and informational labour of human interaction, what remains distinctly, irreducibly human is the quality of connection between people: the degree to which we understand each other's intentions, and are understood in return. Yet as AI mediates more of that connection — drafting our messages, summarising our conversations, predicting our responses — the risk is not that humans become less intelligent. It is that humans become less legible to each other. The intent gap is the measurable form of that illegibility: the distance between what one person means and what another person receives. This project builds the first scientific instrument to measure it, the first intervention designed to test whether it can be closed at the neural level, and a candidate infrastructure for scaling that understanding across populations. That is the foundation of a trust-based society — and it is what AI for Science is built for.

Human miscommunication is not primarily a social or technological failure. It has a biological substrate. The amygdala's subcortical threat-processing pathway (LeDoux, 1996) responds to emotionally ambiguous stimuli ahead of prefrontal cortical semantic resolution. In digital text communication, where prosody, expression, and physical context are absent, this timing asymmetry means that emotionally ambiguous messages are systematically threat-tagged before their communicative intent is understood. The result is a measurable divergence between what a sender intends and what a receiver parses: an *intent gap*.

No existing NLP system models this gap directly. Sentiment classifiers measure surface tone. Emotion recognition systems measure affective expression. Neither asks the question that matters: *what did this person most likely mean, given who they are and who they are talking to?* Crucially, the same message, "Can we talk tonight?", carries a fundamentally different intent distribution when sent by a new colleague versus a partner of three years after a difficult week. Relational history is not context noise. It is the primary signal.

This project addresses three concrete scientific gaps:

1. **No neural-pragmatic dataset** conditions intent annotation on dyadic relational history with dual sender/receiver labelling and inter-rater reliability validation.
2. **No language model** has been trained to predict the *receiver's parsed intent* conditioned on dyadic relational context and evaluated against a human-parity baseline.
3. **No empirical study** has tested whether closed-loop intent feedback, showing users the gap between their expressed tone and likely received intent, produces measurable shifts in neural markers of mentalising circuitry over a sustained intervention period.

The dataset produced by this project is structurally novel: no existing NLP corpus provides dual sender-intent and perceived-intent labels on the same message, conditioned on dyadic relational context metadata, with validated inter-rater reliability on both label types simultaneously — the combination required to measure the intent gap as a computable scalar rather than an impressionistic claim.

The scientific model must account for the full relational distribution: not only pathological divergence, but complementary difference and the developmental arc toward greater relational depth. Reducing the intent gap is not the only goal — understanding the structure of a healthy, thriving dyad, and showing people the path to one, is equally part of the science.

Crucially, the biological substrate of the intent gap is not fixed. The amygdala–TPJ balance is plastic: socio-cognitive training produces measurable increases in TPJ cortical thickness (Singer, 2025); closed-loop neurofeedback produces lasting functional change via Hebbian co-activation of target circuits (Sitaram et al., 2017); post-interaction inter-brain coupling persists beyond the interaction that created it and predicts future social motivation (Finn et al., 2024). The mechanism for changing the trust deficit is established in the literature. This project tests whether it can be applied at scale, in naturalistic digital communication.

**Why intent classification — not sentiment, not coaching, not therapy?** Sentiment analysis measures surface tone; it does not ask what the sender meant. Relationship coaching changes habits over months; it does not make the biological gap visible in real time. Therapy addresses downstream symptoms; it does not produce a per-message, per-dyad scalar that can be tracked, intervened on, and tested for neural change. Intent classification is the minimal sufficient primitive: the one signal whose failure causes trust breakdown at the belief layer, and the one signal that can be measured continuously, fed back in the cognitive reappraisal window, and used as a training input to the brain's own mentalising circuitry. Everything else follows from getting this signal right.

**This is AI for Science, not science-flavoured product.**

The intent-conditioned language model, fine-tuned from RoBERTa-large with a novel 16-dimensional relational context layer, is the scientific instrument. The cognitive companion is the delivery mechanism for the intervention. The 60-day pilot is the empirical study. There is, to our knowledge, no dataset of this form in the literature; we will construct and release one openly. The validation chain runs across three levels: computational (does relational context improve intent prediction? — H₁), behavioural (does the feedback intervention reduce the gap over 60 days? — H₂), and neural (does sustained feedback produce measurable reorganisation of mentalising circuitry? — H₃). Each level is independently publishable; together they form a coherent scientific programme rather than three disconnected studies.

**12-month deliverables (primary commitment):**
- A 2,000-message annotated neural-pragmatic dataset (dual sender-intent / perceived-intent labels, relational context metadata, κ-validated, 5 relationship types), published on HuggingFace and OpenNeuro
- A trained intent-conditioned language model, RoBERTa-large fine-tuned with a novel 16-dimensional dyadic relational context layer, with H₁ confirmed or falsified
- A paper submitted to a peer-reviewed venue reporting dataset, model, and primary results
- *(SHOULD, pending lab partner confirmation)* A 60-day EEG pilot (N = 20–24) testing inter-brain synchrony shift as a neural correlate of the intervention

**ARIA alignment:** The intent-conditioned model and dataset directly advance *Scalable Neural Interfaces*, computational tools that interact with and model human neural processes at scale. The longer-term vision, a consent-based network where intent representations are shared between dyads, maps to *Collective Flourishing*: infrastructure for human understanding at population scale, built on science, not attention extraction. As AI systems absorb more cognitive labour, the quality of human-to-human communication, the trust layer between people, becomes the critical bottleneck for productivity and coordination. The intent gap is its most measurable failure mode. This work builds the scientific foundation for upgrading that layer: not by coaching humans to communicate better, but by proving the biological bottleneck can be changed.

**Why this fellow, now:** I am an AI engineer with production systems experience in NLP and applied ML. The dataset pipeline, annotation tooling, model training infrastructure, and browser extension delivery mechanism are not research risks for me, they are solved engineering problems. I build the science infrastructure while embedded in a neuroscience lab that provides EEG equipment, ethics coverage, and experimental paradigm expertise. The combination of builder velocity and neuroscience rigour is precisely what makes this programme executable in 12 months by one fellow.

**The product is already in development.** The Cognitive Companion is not a hypothetical delivery mechanism — it is a parallel product development track with an existing technical specification (v3.0), a Node.js/OpenClaw gateway architecture, and on-device privacy-by-design infrastructure. The fellowship funds the science layer — the dataset, the fine-tuned RoBERTa-large model, and the EEG validation — that makes the product scientifically defensible; the product is the real-world deployment environment that makes the science ecologically valid. The product's intent classification layer is architected behind an interface from Day 1, designed to swap from a bridge classifier (GPT-4o-mini with SI/PI prompting) to the fine-tuned RoBERTa-large model once H₁ validation is complete. EEG pilot participants in Study 4 are recruited from the beta cohort — the same individuals whose neural change is measured in the lab also generate continuous real-world intent gap data in naturalistic WhatsApp usage, enabling a two-environment validation: controlled lab (EEG) and naturalistic deployment (product) measuring the same intervention simultaneously. Research track obligations and lab commitments are the primary time allocation; the product development track runs in parallel during remaining time and draws on no Encode fellowship funds.

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

### 2.5 Formal Hypotheses

**H₁, Behavioural / Computational (Primary):**
A RoBERTa-large model fine-tuned on perceived-intent prediction, with a 16-dimensional dyadic relational context vector concatenated to the [CLS] token representation, will achieve significantly higher macro-averaged F1 on perceived-intent (PI) prediction for emotionally ambiguous messages than an ablated message-only baseline, on a held-out 400-message test set (paired t-test, α = 0.05, minimum effect size Cohen's d ≥ 0.3).

*Failure condition:* If H₁ is not confirmed, dyadic relational history does not significantly improve intent prediction at this scale and label granularity. This is a publishable null result with clear theoretical implications, and the project pivots to characterising *where* and *why* relational context fails to add signal.

**H₂, Behavioural (Secondary):**
Participants using the Cognitive Companion browser extension for 60 days will show a significant reduction in intent gap score compared to their own Day 0 baseline, indicating that closed-loop intent feedback changes how people compose emotionally ambiguous messages (within-subjects, paired Wilcoxon signed-rank test, α = 0.05). *Operationalisation note:* In real-world usage, ground-truth sender intent labels are unavailable for natural messages. The gap score is therefore computed as JS-divergence(SI_model, PI_model), where SI_model (the model's sender-intent head output) serves as a proxy for the sender's communicative intent. The 60-day trajectory measures whether users compose messages whose model-estimated SI and PI distributions converge over time. This proxy assumption is explicit and defensible: the SI head is trained on annotator-labelled sender perspectives and captures the pragmatically intended meaning, even absent direct sender confirmation.

**H₃, Neural (Exploratory, EEG pilot):**
H₃ is the most exploratory hypothesis in this programme: that 60 days of closed-loop intent feedback is sufficient to produce measurable reorganisation of the neural balance between threat and mentalising circuitry. If confirmed, this would suggest that a digital intervention may contribute to lasting reorganisation of how the brain processes communicative intent — a neuroplastic change, not merely a behavioural one. That is the scientific claim this project is designed to test.

The proposed mechanism is a four-step cascade, each step grounded in established neuroscience. *Step 1:* the intent distribution display occupies the cognitive reappraisal window (Gross, 1998), activating lateral PFC and suppressing the amygdala threat cascade before a response is composed. *Step 2:* when the model's displayed intent matches the sender's actual intent — the experience of "being understood" — the nucleus accumbens releases oxytocin and dopamine, reinforcing the trust-confirming neural state (Zak et al., 2017). *Step 3:* repeated correct intent scaffolding strengthens TPJ activation via Hebbian co-activation — the same closed-loop mechanism demonstrated in neurofeedback paradigms to produce lasting functional change in target circuits (Sitaram et al., 2017). *Step 4:* across 60 days, sustained high-synchrony inter-dyadic states produce persistent inter-brain coupling in the right IFG and dorsomedial PFC — coupling that outlasts the individual interactions and raises the dyad's baseline mentalising capacity (Finn et al., 2024). The delivery vehicle is novel. The neuroscience is not.

Operationally: participants who complete the 60-day intervention will show measurably increased theta-band inter-brain phase synchrony (IBS) during a standardised dyadic ambiguous-message reading task at Day 60 compared to Day 0 baseline, indicating that the intervention shifts neural coupling toward the pattern associated with successful mentalising-mediated communication (Hasson et al., 2012). Pre-registered analysis for IBS only; ERP analysis is exploratory and reported as preliminary findings.

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
- Two separate fine-tuning runs: one for SI prediction, one for PI prediction
- Classification head: 7-way softmax over I1–I7 (I8 excluded from single-message classification, detected at pattern level only)

**Experimental conditions:**
- **Condition A (full model):** RoBERTa-large + relational context vector
- **Condition B (ablation / baseline):** RoBERTa-large without context vector (message content only)
- **Condition C (surface baseline):** RoBERTa-base fine-tuned for sentiment classification (represents existing tool capability)

**Training:** 3 runs per condition × 5 epochs; AdamW optimiser; learning rate sweep (1e-5, 2e-5, 3e-5); early stopping on validation loss. A100 GPU on Lambda Labs.

**Evaluation:**
- Macro-averaged F1 on 400-message held-out test set (ambiguous-valence subset prioritised for primary analysis)
- Human majority-vote baseline: plurality vote of 5 annotators as ground truth; human-parity gap reported
- **Primary metric (H₁):** ΔF1 (Condition A − Condition B) on PI prediction for ambiguous-valence messages; paired t-test, α = 0.05, minimum d ≥ 0.3
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
| **Month 1** | κ pilot (20 msgs, 5 annotators); annotation tooling build; ethics application submitted with lab partner; taxonomy unification with product classifier schema | Annotation protocol validated; ethics in review; unified SI/PI/intent schema | MUST |
| **Month 1–3** | Full 2,000-message annotation; dataset QA; small online behavioural validation study (H₂ probe, N=50, online, no EEG) | Annotated dataset v1.0; early H₁ signal | MUST |
| **Month 3–6** | RoBERTa-large fine-tuning; ablation studies; evaluation vs. baselines; demo Streamlit app | H₁ confirmed/falsified; model released on HuggingFace | MUST |
| **Month 5** | Paper draft #1: dataset + model + H₁ | Submitted to arXiv; circulated to lab partner | MUST |
| **Month 6–8** | Brain-Score submission; EEG pilot design finalised; IRB approval; participant recruitment from beta cohort | Brain-Score result; pilot protocol approved | SHOULD |
| **Month 7–11** | 60-day EEG pilot; continuous intent gap data from product cohort; Day 0 and Day 60 EEG sessions | H₂/H₃ data collected; product behavioural data as wild-environment H₂ measure | SHOULD |
| **Month 11–12** | Data analysis; paper draft #2 (full study: dataset + model + pilot + EEG + product behavioural cohort); submission | Paper submitted to peer-reviewed venue | MUST |

**Parallel product track:**

| Period | Product Activity | Key Output |
|--------|-----------------|------------|
| **Month 1** | Taxonomy unification; OpenClaw/Node.js gateway scaffold; Baileys WhatsApp integration; bridge classifier (GPT-4o-mini, SI/PI schema) behind abstracted `ClassifierInterface`; bilateral consent flow | Infrastructure complete; bridge classifier live behind interface |
| **Month 1–3** | Internal alpha; basic intent gap feature on bridge classifier; data schema compatible with RoBERTa-large output from Day 1; privacy gateway (on-device, AES-256) | Internal alpha working; 0 external users |
| **Month 3–6** | Closed alpha: 10–20 couples; core intent gap feature; privacy gateway; web dashboard V1; Coach agent (rule-based V1) | Alpha validated: does bridge classifier produce coherent gap scores on real messages? |
| **Month 6–7** | RoBERTa-large deployed in shadow mode behind `ClassifierInterface`; 2-week shadow validation; model cutover; beta launch to 30–50 couples | First product in the world running a scientifically validated intent gap model |
| **Month 7–9** | Twin agent activated (4+ weeks data accumulated); Weekly Reflection feature; EEG pilot participants recruited from beta cohort; beta expanded to 250 couples | Two-environment H₂ validation: product (wild) + EEG (lab) |
| **Month 9–12** | Scale and stabilise; product in maintenance mode during paper writing; population-scale intent gap dataset accumulating from consented beta users | Real-world deployment evidence for paper; commercial proof-of-concept |

**The parallel tracks are one programme, not two.** The critical design decision that makes this feasible: the product's intent classification layer is abstracted behind a `ClassifierInterface` from Day 1. In Months 1–3, this interface is backed by a GPT-4o-mini bridge classifier using the same SI/PI label schema as the fellowship annotation protocol. At Month 6–7, the same interface is re-backed by the fine-tuned RoBERTa-large model — zero upstream product code changes, no migration crisis. Taxonomy unification in Month 1 (a joint task counted for both tracks) ensures the product output schema is identical to the fellowship annotation schema throughout. The product build requires approximately 30% of weekly time in Months 1–3 (infrastructure, no ML), 35% in Months 3–6 (alpha, lean feature set), and 45% in Months 6–8 (beta launch, model integration). Research track takes the remainder. The EEG pilot (Months 7–11) is the most time-constrained research phase; product work is intentionally minimal during this window, limited to scaling and maintenance.

**Month 1–3 online behavioural study (pre-EEG signal):** 50 participants recruited online (Prolific); read 40 ambiguous messages with and without model-provided intent distributions; rate perceived intent before/after; 2-week follow-up. This provides an early, low-cost test of H₂'s behavioural component before the full 60-day pilot begins, de-risking the timeline and providing pilot data for effect size estimation.

**Gantt stretch goals:** Full 60-day longitudinal behavioural data from 20+ pairs; ERP N2/P3 analysis; Relationship Digital Twin visualisation.

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
- Browser extension (Cognitive Companion delivery mechanism), production-grade Chrome MV3 engineering
- Streamlit demo application, visual hypothesis display for fellowship review and lab presentations
- Analysis code for intent gap metrics, JS-divergence computation, and model evaluation
- Full documentation and reproducibility infrastructure (DVC, HuggingFace Hub, OpenNeuro upload)

**Division of labour:**
- Behavioural and ML work (Studies 1–3): primarily fellow-led, with PI scientific oversight
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
The Relationship Digital Twin stored on-device could become a surveillance instrument if a controlling partner accesses the device.
*Mitigation:* Digital Twin data encrypted at rest (AES-256, device keychain). No cloud sync in MVP. Biometric/PIN gate on Companion data access. Critically: **the Relationship Digital Twin visualisation is opt-in and hidden by default**, it is not visible unless the user explicitly activates it. The MVP explicitly does not include any "partner monitoring" features; all analysis is strictly first-person (your own sent messages, your own gap scores). The domestic abuse scenario is reviewed explicitly with the lab ethics board in Month 1 as a named design constraint.

**5. Participant data in EEG pilot**
EEG and behavioural data from 20–24 participants requires secure handling, appropriate consent, and clear data retention policies.
*Mitigation:* Full ethics application submitted Month 1 with lab partner. Informed consent covers EEG recording, 60-day message metadata collection (no message content, intent gap scores only), and data retention period. Participants can withdraw at any time with data deletion.

---

## Section 6: Bibliography

1. Adolphs, R. (2002). Recognizing emotion from facial expressions: Psychological and neurological mechanisms. *Behavioural and Cognitive Neuroscience Reviews*, 1(1), 21–62.
2. Blank, I., Kanwisher, N., & Fedorenko, E. (2014). A functional dissociation between language and multiple-demand systems revealed in patterns of BOLD signal fluctuations. *Journal of Neurophysiology*, 112(5), 1105–1118.
3. Brady, W. J., Wills, J. A., Jost, J. T., Tucker, J. A., & Van Bavel, J. J. (2017). Emotion shapes the diffusion of moralized content in social networks. *PNAS*, 114(28), 7313–7318.
4. Davidson, R. J., & Lutz, A. (2008). Buddha's brain: Neuroplasticity and meditation. *IEEE Signal Processing Magazine*, 25(1), 176–174.
5. Dikker, S., Wan, L., Davidesco, I., Kaggen, L., Oostrik, M., McClintock, J., ... & Poeppel, D. (2017). Brain-to-brain synchrony tracks real-world dynamic group interactions outside the laboratory. *Current Biology*, 27(9), 1375–1380.
6. Fedorenko, E., Behr, M. K., & Kanwisher, N. (2011). Functional specificity for high-level linguistic processing in the human brain. *PNAS*, 108(39), 16428–16433.
7. Fletcher, G. J., Simpson, J. A., & Thomas, G. (2000). The measurement of perceived relationship quality components: A confirmatory factor analytic approach. *Personality and Social Psychology Bulletin*, 26(3), 340–354.
8. Frith, C. D., & Frith, U. (2006). The neural basis of mentalizing. *Neuron*, 50(4), 531–534.
9. Haidt, J., & Rose-Stockwell, T. (2019). The dark psychology of social networks. *The Atlantic*, December 2019.
10. Hasson, U., Ghazanfar, A. A., Galantucci, B., Garrod, S., & Keysers, C. (2012). Brain-to-brain coupling: A mechanism for creating and sharing a social world. *Trends in Cognitive Sciences*, 16(2), 114–121.
11. LeDoux, J. E. (1996). *The Emotional Brain: The Mysterious Underpinnings of Emotional Life*. Simon & Schuster.
12. Liu, Y., Ott, M., Goyal, N., Du, J., Joshi, M., Chen, D., ... & Stoyanov, V. (2019). RoBERTa: A robustly optimized BERT pretraining approach. *arXiv:1907.11692*.
13. Öhman, A., & Mineka, S. (2001). Fears, phobias, and preparedness: Toward an evolved module of fear and fear learning. *Psychological Review*, 108(3), 483–522.
14. Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017). Brain-to-brain entrainment: EEG interbrain synchronization while speaking and listening. *Scientific Reports*, 7(1), 4190.
15. Saxe, R., & Kanwisher, N. (2003). People thinking about thinking people: The role of the temporo-parietal junction in "theory of mind." *NeuroImage*, 19(4), 1835–1842.
16. Schrimpf, M., Blank, I., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., ... & Fedorenko, E. (2021). The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*, 118(45), e2105646118.
17. Askenasy, J. J. M., & Lehmann, D. (2013). Consciousness, brain, neuroplasticity. *Frontiers in Psychology*, 4, 412.
18. Grice, H. P. (1975). Logic and conversation. In P. Cole & J. Morgan (Eds.), *Syntax and Semantics, Vol. 3: Speech Acts* (pp. 41–58). Academic Press.
19. Sperber, D., & Wilson, D. (1986). *Relevance: Communication and Cognition*. Harvard University Press.
20. Wang, A., Singh, A., Michael, J., Hill, F., Levy, O., & Bowman, S. R. (2018). GLUE: A multi-task benchmark and analysis platform for natural language understanding. *arXiv:1804.07461*.
21. Lombardo, M. V., Chakrabarti, B., Bullmore, E. T., Wheelwright, S. J., Sadek, S. A., Suckling, J., ... & Baron-Cohen, S. (2011). Specialization of right temporo-parietal junction for mentalizing and its relation to social impairments in autism. *NeuroImage*, 56(3), 1832–1838.
22. Gottman, J. M. (1994). *What Predicts Divorce? The Relationship Between Marital Processes and Marital Outcomes*. Lawrence Erlbaum Associates.
23. Gross, J. J. (1998). Antecedent- and response-focused emotion regulation: Divergent consequences for experience, expression, and physiology. *Journal of Personality and Social Psychology*, 74(1), 224–237.
24. Ochsner, K. N., & Gross, J. J. (2005). The cognitive control of emotion. *Trends in Cognitive Sciences*, 9(5), 242–249.
25. Searle, J. R. (1976). A classification of illocutionary acts. *Language in Society*, 5(1), 1–23.
26. Li, Y., Su, H., Shen, X., Li, W., Cao, Z., & Niu, S. (2017). DailyDialog: A manually labelled multi-turn dialogue dataset. *Proceedings of IJCNLP 2017*, 986–995.
27. Welivita, A., & Pu, P. (2020). A taxonomy of empathetic response intents in human social conversations. *Proceedings of COLING 2020*, 4444–4453.
28. Brown, P., & Levinson, S. C. (1987). *Politeness: Some Universals in Language Usage*. Cambridge University Press.
29. Goffman, E. (1967). *Interaction Ritual: Essays on Face-to-Face Behaviour*. Anchor Books.
30. Xu, H., Zhao, H., Gu, W., Xu, L., Zhu, L., Liu, T., & Zhao, Z. (2023). MIntRec2.0: A large-scale benchmark dataset for multimodal intent recognition and out-of-scope detection in conversations. *arXiv:2309.04421*.
31. Finn, E. S., Huber, L., Jangraw, D. C., Molfese, P. J., & Bandettini, P. A. (2024). Post-interaction neuroplasticity of inter-brain networks predicts social motivation. *PNAS*, 121(5), e2311771121.
32. Sitaram, R., Ros, T., Stoeckel, L., Haller, S., Scharnowski, F., Lewis-Peacock, J., ... & Sulzer, J. (2017). Closed-loop brain training: The science of neurofeedback. *Nature Reviews Neuroscience*, 18(2), 86–100.
33. Singer, T. (2025). A neuroscience perspective on the plasticity of the social and relational brain. *Annals of the New York Academy of Sciences*, 1544, 15–34.
34. Ickes, W. (1993). Empathic accuracy. *Journal of Personality*, 61(4), 587–610.
35. Pavlacic, J. M., Buchanan, E. M., Maxwell, N. P., Hopke, T. G., & Schulenberg, S. E. (2019). A meta-analysis of expressive writing on posttraumatic stress, posttraumatic growth, and quality of life. *Review of General Psychology*, 23(2), 230–250.
36. Fritz, J., de Graaff, A. M., Caisley, H., van Harmelen, A. L., & Wilkinson, P. O. (2024). A systematic review of amenable resilience factors that moderate and/or mediate the relationship between childhood adversity and mental health in young people. *Advances in Methods and Practices in Psychological Science*, 7(1), 25152459241267912.
37. McGaugh, J. L. (2000). Memory — a century of consolidation. *Science*, 287(5451), 248–251.
38. Gilardi, F., Alizadeh, M., & Kubli, M. (2023). ChatGPT outperforms crowd workers for text-annotation tasks. *PNAS*, 120(30), e2305016120.
39. Møller, A. G., Dalsgaard, J., Pera, A., & Aiello, L. M. (2023). Is a prompt and a few samples all you need? Using GPT-4 for data augmentation in low-resource classification tasks. *arXiv:2304.13861*.
40. Rashkin, H., Smith, E. M., Li, M., & Boureau, Y. L. (2019). Towards empathetic open-domain conversation models: A new benchmark and dataset. *Proceedings of ACL 2019*, 5370–5381.

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

*The reflection journal is the mechanism by which the Mirror's self-model gets populated.* The classifier infers what the user does; the journal captures what the user believes and intends. Together they form a triangulated individual consciousness model: inferred behaviour + stated intent + stated aspiration. The improvement signal is convergence across all three — the point at which who you are as a communicator, what you mean to say, and who you want to be begin to align.*

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

**Horizon 3, The Map (Long-run vision):**
Thousands of consented pairs. An empirical atlas of communicative intent at population scale, where misunderstanding concentrates, where understanding spontaneously forms, what closing the gap actually looks like across cultures, relationship types, and demographics. The data that founds the field of population-level neural pragmatics. *"And together, humanity begins to understand itself."*

**ARIA alignment:**
- *Scalable Neural Interfaces:* The intent-conditioned model and dataset are computational tools that interface with human neural language processing, validated against neural data via Brain-Score, designed to scaffold mentalising circuitry.
- *Collective Flourishing:* The Map is the long-term vision, intent infrastructure that reduces the structural cost of human miscommunication at population scale, built on consent architecture rather than attention extraction.

---

## Appendix B: Technical Specification

### B.1 Intent-Conditioned Model Architecture

```
Input: [message_text] + [relational_context_vector]

Tokenisation:  RoBERTa tokeniser (BPE, 50k vocab)
Encoder:       RoBERTa-large (24 layers, 1024 hidden, 16 heads, 355M params)

Context vector (16-dim):
  - relationship_type:     5-dim one-hot (couple/parent-child/friend/community/colleague)
  - duration_log:          1-dim continuous (log months)
  - recent_valence:        1-dim continuous [-1, +1]
  - message_frequency:     1-dim continuous (log msgs/week)
  - rolling_gap_score:     1-dim continuous (14-day mean JS-divergence)
  - [7 reserved dims for future relational features]

Integration:   Context vector concatenated to [CLS] hidden state before classification head
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

### B.3 EEG Analysis Plan

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

*"We are not building a chatbot. We are building the instrument that measures and closes the biological gap between human minds, and proves, for the first time, that it can be changed."*
