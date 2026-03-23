# Encode: AI for Science Fellowship — Fellow Proposal

**Name:** Snehal Nair
**Current Institution:** University of Edinburgh

---

## 1) Problem

Human miscommunication has a biological substrate. Ambiguous emotional stimuli are threat-tagged via subcortical processing (LeDoux, 1996) before higher-order language and mentalising systems fully resolve intent. In digital text, where prosody, facial expression, and physical context are absent, this timing asymmetry makes misunderstanding especially likely.

To our knowledge, no published NLP system models intent as a dyadic phenomenon conditioned on relational history. Sentiment classifiers measure tone, and emotion recognition systems measure affective expression, but neither asks what a person most likely meant, given who they are and who they are talking to. The same message can carry a different intent distribution depending on relationship type, history, and context. The central question is whether conditioning on dyadic context and providing closed-loop feedback measurably improves intent prediction and reduces miscommunication.

This project addresses four scientific gaps (based on our review of the pragmatics, social NLP, and affective computing literature as of March 2026):

1. To our knowledge, no published dataset conditions intent annotation on dyadic relational history with dual sender/receiver labels and reliability validation.
2. To our knowledge, no language model has been trained to predict receiver-parsed intent conditioned on dyadic relational context.
3. To our knowledge, no empirical study has tested whether closed-loop intent feedback changes behavioural or neural markers of mentalising.
4. To our knowledge, no structured personality instrument has been tested as an independent conditioning signal for cold-start intent prediction.

---

## 2) Solution

The core scientific instrument is a RoBERTa-large model (355M parameters; Liu et al., 2019) fine-tuned for intent classification with two conditioning signals:

- A **16-dimensional dyadic relational context vector**, encoding relationship type, duration, recent valence, message frequency, and rolling divergence history, concatenated to the [CLS] token before the classification head.
- A **personality context block**, derived from an 8-question biographical intake instrument across identity values, decision architecture, and narrative stories, prepended at inference time.

The model outputs a probability distribution over seven intent categories (seeking connection, expressing concern, setting boundary, seeking validation, expressing frustration, making request, giving information), predicted from both sender and receiver perspectives. The project creates a purpose-built 2,000-message dataset with dual sender-intent (SI) and perceived-intent (PI) labels, five annotators per message, across five relationship types (romantic partners, parent-child, close friends, community/social, professional). The divergence between these distributions is quantified as Jensen-Shannon divergence (JSD) — chosen because it is symmetric, bounded [0, 1], and well-suited for comparing two probability distributions over the same label space.

The intervention instrument is a browser extension that surfaces the model's predicted intent in the pause between reading a message and replying, providing an alternative interpretation before the receiver forms a response.

Validation proceeds across four levels:

- **Computational (H₁):** Relational context improves intent prediction over a message-only baseline (ablation, paired t-test, d ≥ 0.3).
- **Cold-start ablation (H₄):** Personality context improves Day 1 accuracy before dyadic history accumulates (100 users randomised 1:1).
- **Behavioural (H₂):** 60-day intent feedback reduces divergence scores (within-subjects pre/post, Wilcoxon signed-rank).
- **Neural (H₃, stretch):** 60-day feedback increases theta-band inter-brain synchrony (EEG hyperscanning, N=20–24, pre/post).

Each level is independently publishable, and null results are pre-registered. A secondary prediction follows from the biological mechanism: if the divergence between sender and receiver intent arises from asymmetry between subcortical threat-tagging and cortical mentalising, it should be systematically elevated in neurodivergent dyads — a falsifiable prediction tested via stratified analysis.

---

## 3) Translation Opportunity

The scientific contribution is a new measurement construct — the divergence between sender-intent and perceived-intent distributions — and a new conditioning signal: dyadic relational context. If the model confirms that relational context improves prediction, the open-source dataset and trained model (released on HuggingFace under Apache 2.0) will support follow-on research in pragmatic inference, social cognition, and human-AI communication.

Longer-term translation may include consent-gated relational tools for communication support, but that is explicitly downstream of the scientific validation. The immediate outcome of the fellowship is a rigorous, reusable research instrument, not a consumer product.

ARIA alignment is direct: the project advances **Scalable Neural Interfaces** through computational tools that model human mentalising, and it points toward **Collective Flourishing** by making understanding measurable rather than extractive.

---

## 4) Goals / Milestones / Resources

| Goals | Milestones | Resources Needed |
|-------|-----------|-----------------|
| **MUST:** Validated annotated dataset with dual SI/PI labels and κ > 0.70 | **3 mo:** Validate κ pilot; annotate 2,000 messages; publish on HuggingFace | Fellowship compute allocation; Prolific Academic annotator budget (~£5–7K); annotation tooling (built by fellow) |
| **MUST:** Intent-conditioned model with H₁ confirmed or falsified | **6 mo:** Fine-tune RoBERTa-large across 4 ablation conditions; confirm or falsify H₁; release model on HuggingFace; submit Paper #1 | Compute for training (3 runs × 4 conditions × 5 epochs) |
| **MUST:** Cold-start ablation (H₄) confirmed or falsified | **6 mo:** Complete Study 1b data collection (N=100); **8 mo:** Complete H₄ analysis | Ethics approval (Month 1–3); participant recruitment via Prolific |
| **MUST:** Peer-reviewed paper submitted | **12 mo:** Submit full paper to ACL, EMNLP, or CHI | — |
| **SHOULD:** 60-day EEG pilot (H₂/H₃) | **8 mo:** Begin pilot; **11 mo:** Complete Day 60 sessions; **12 mo:** Analyse results | Lab partner: 64-channel EEG, hyperscanning paradigm, ethics umbrella |
| **SHOULD:** Brain-Score neural plausibility validation | **8 mo:** Submit model to MIT Brain-Score Language benchmark | ~2 weeks engineering post-training |

---

## People Involved

| Name | Institution | Involvement |
|------|------------|-------------|
| **Snehal Nair** | University of Edinburgh (Independent AI Researcher) | Fellow — dataset pipeline, model training, annotation tooling, biographical intake instrument, browser extension, analysis code, reproducibility infrastructure (DVC, HuggingFace Hub, OpenNeuro) |
| **Lab Partner (TBC)** | Outreach active: UCL FIL, MRC CBU Cambridge, University of Nottingham | EEG equipment and lab space, existing hyperscanning paradigm, ethics/IRB umbrella, PI co-authorship on neural study. Core MUST deliverables do not depend on lab partner confirmation |

---

## 5) Data Landscape

The dataset is purpose-built for this project. Message sources: relabelled public datasets (DailyDialog, Li et al. 2017; EmpatheticDialogues, Rashkin et al. 2019), researcher-constructed stimuli, and LLM-generated examples with human review gates. All annotation is conducted via Prolific Academic with a structured dual-pass protocol (SI and PI labelled separately, blind to each other).

Study 1b adds 100 new users under informed consent, with independent raters evaluating held-out messages. Personality context data from the biographical intake is local-first and encrypted (AES-256). If the EEG pilot proceeds, neural data is collected under joint ethics approval at the lab partner facility.

---

## 6) Data Characterisation

- **Fidelity:** 5 independent annotators per message; Cohen's κ > 0.70 quality gate before full annotation; separate κ for SI and PI labels; per-culture and neurodiverse-subset reliability reported.
- **Modality:** Text (messages) + structured metadata (relationship type, duration, valence) + EEG time-series (if Study 4 proceeds).
- **Volume:** 2,000 annotated messages (Study 1); ~2,800 messages from 100 users over 4 weeks (Study 1b); 40-message stimulus set × 24 participants × 2 sessions (Study 4).
- **Scalability:** Annotation protocol, label schema, and model architecture are designed for extension to 10,000+ messages with naturalistic history and multilingual expansion in Year 2.

---

## 7) Anticipated Failure Modes

The main risk is annotation failure: if annotators cannot reliably agree on sender and perceived intent (κ < 0.70), the training signal is invalid. This is mitigated through an early κ pilot in Month 1, two adjudication rounds, and schema redesign if needed.

A second risk is a null H₁ result. That outcome is still publishable — it provides, to our knowledge, the first rigorous test of whether dyadic relational context improves intent prediction at this scale. A null result does not invalidate the dataset or the annotation methodology.

---

## 8) Three Context Papers

1. **LeDoux, J. E. (1996).** *The Emotional Brain: The Mysterious Underpinnings of Emotional Life.* Simon & Schuster. — Establishes the subcortical thalamo-amygdala pathway underlying rapid threat-tagging of ambiguous stimuli before cortical semantic processing; the core neurological basis for the sender-receiver divergence this project measures.

2. **Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017).** Brain-to-brain entrainment: EEG interbrain synchronization while speaking and listening. *Scientific Reports*, 7(1), 4190. — Demonstrates theta-band inter-brain phase synchrony as a measurable, reproducible correlate of communication quality; the neural outcome measure for H₃.

3. **Schrimpf, M., Blank, I., Tuckute, G., Kauf, C., Hosseini, E. A., Kanwisher, N., ... & Fedorenko, E. (2021).** The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*, 118(45), e2105646118. — Establishes the Brain-Score Language benchmark used to assess whether pragmatic fine-tuning enhances or degrades neural plausibility of the intent model.

---

## 9) ARIA Alignment

The intent-conditioned model and dataset advance **Scalable Neural Interfaces** by building computational tools that model human mentalising at scale. The longer-term vision maps to **Collective Flourishing** through consent-based infrastructure for understanding rather than attention extraction.

---

## 10) Additional Information

**Skills and collaborator needs:** I have built and led AI teams at scale (KDD '24/'25), with a working prototype already deployed (dyadicmentalising.streamlit.app) and production experience in NLP, dataset pipeline design, and ML systems. The project needs a neuroscience lab partner for the EEG component — someone with an existing hyperscanning paradigm, ethics infrastructure, and theta-band IBS analysis pipeline. The MUST-tier deliverables (dataset, model, H₁/H₄ papers) are executable independently; the SHOULD tier (EEG pilot) is explicitly contingent on this partnership.

**Resource challenges:** No proprietary datasets are required — all data is purpose-built or drawn from public sources. The primary resource dependency is lab partner confirmation for the EEG study. Outreach is active (UCL FIL, MRC CBU Cambridge, Nottingham). If not confirmed by Month 3, EEG defers to Year 2 with no impact on core deliverables.

---

## Open-source Opt-in

Yes — I would like the research opportunity included in the R&D Gap Map and to be listed as a point of contact for AI researchers interested in collaborating on computational models of communicative intent and dyadic mentalising.
