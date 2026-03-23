# Encode: AI for Science Fellowship — Fellow Proposal

**Name:** Snehal Nair
**Current Institution:** University of Edinburgh

---

## 1) Problem

Ambiguous emotional stimuli are threat-tagged via subcortical processing (LeDoux, 1996) before higher-order language and mentalising systems resolve intent. In digital text — where prosody, facial expression, and physical context are absent — this timing asymmetry makes misunderstanding especially likely.

Existing NLP systems do not model intent as a dyadic phenomenon. Sentiment classifiers measure tone; emotion recognition systems measure affective expression. Neither asks what a person most likely meant, given who they are and who they are talking to. The same message can carry a different intent distribution depending on relationship type, history, and context. The central question is whether conditioning on dyadic context and providing closed-loop feedback measurably improves intent prediction and reduces miscommunication.

To our knowledge, the following gaps remain open in the pragmatics, social NLP, and affective computing literature as of March 2026:

1. No published dataset conditions intent annotation on dyadic relational history with dual sender/receiver labels and reliability validation.
2. No language model has been trained to predict receiver-parsed intent conditioned on dyadic relational context.
3. No empirical study has tested whether closed-loop intent feedback changes behavioural or neural markers of mentalising.
4. No structured personality instrument has been tested as an independent conditioning signal for cold-start intent prediction.

---

## 2) Solution

The core instrument is a RoBERTa-large model (355M parameters; Liu et al., 2019) fine-tuned for intent classification with two conditioning signals:

- A **16-dimensional dyadic relational context vector**, encoding relationship type, duration, recent valence, message frequency, and rolling intent-gap history, concatenated to the [CLS] token before the classification head.
- A **personality context block**, derived from an 8-question biographical intake instrument across identity values, decision architecture, and narrative stories, prepended at inference time.

The model outputs a probability distribution over seven intent categories (seeking connection, expressing concern, setting boundary, seeking validation, expressing frustration, making request, giving information), predicted from both sender and receiver perspectives. The project creates a purpose-built 2,000-message dataset with dual sender-intent (SI) and perceived-intent (PI) labels, five annotators per message, across five relationship types (romantic partners, parent-child, close friends, community/social, professional). Divergence between these distributions is quantified as Jensen-Shannon divergence — symmetric, bounded [0, 1], and well-suited for comparing two probability distributions over the same label space.

A browser extension surfaces the model's predicted intent in the pause between reading a message and replying, providing an alternative interpretation before the receiver forms a response.

Validation proceeds across four levels:

- **Computational (H₁):** Relational context improves intent prediction over a message-only baseline (ablation, paired t-test, d ≥ 0.3).
- **Cold-start ablation (H₄):** Personality context improves Day 1 accuracy before dyadic history accumulates (100 users randomised 1:1).
- **Behavioural (H₂):** 60-day feedback reduces divergence scores (within-subjects pre/post, Wilcoxon signed-rank).
- **Neural (H₃, stretch):** 60-day feedback increases theta-band inter-brain synchrony (EEG hyperscanning, N=20–24, pre/post).

Each level is independently publishable; null results are pre-registered. A secondary prediction: if sender-receiver divergence arises from asymmetry between subcortical threat-tagging and cortical mentalising, it should be elevated in neurodivergent dyads — tested via stratified analysis.

---

## 3) Translation Opportunity

The scientific contribution is a new measurement construct — the divergence between sender-intent and perceived-intent distributions — and a new conditioning signal: dyadic relational context. The open-source dataset and trained model (HuggingFace, Apache 2.0) will support follow-on research in pragmatic inference, social cognition, and human-AI communication. Longer-term translation may include consent-gated relational tools, but that is explicitly downstream of the scientific validation.

ARIA alignment: the project advances **Scalable Neural Interfaces** through computational tools that model human mentalising, and points toward **Collective Flourishing** by making understanding measurable rather than extractive.

---

## 4) Goals / Milestones / Resources

| Goals | Milestones | Resources Needed |
|-------|-----------|-----------------|
| **MUST:** Validated dataset with dual SI/PI labels and κ > 0.70 | **3 mo:** Complete κ pilot validation; annotate 2,000 messages; publish on HuggingFace | Fellowship compute; Prolific annotator budget (~£5–7K); annotation tooling (built by fellow) |
| **MUST:** Intent-conditioned model with H₁ tested | **6 mo:** Fine-tune RoBERTa-large across 4 ablation conditions; test H₁; release model; submit Paper #1 | Training compute (3 runs × 4 conditions × 5 epochs) |
| **MUST:** Cold-start ablation H₄ tested | **6 mo:** Complete Study 1b data collection (N=100); **8 mo:** Complete H₄ analysis | Ethics approval (Month 1–3); Prolific recruitment |
| **MUST:** Peer-reviewed paper submitted | **12 mo:** Paper submitted to ACL, EMNLP, or CHI | — |
| **SHOULD:** 60-day EEG pilot (H₂/H₃) | **8 mo:** Begin pilot; **11 mo:** Complete Day 60 sessions; **12 mo:** Analyse | Lab partner: 64-channel EEG, hyperscanning paradigm, ethics umbrella |
| **SHOULD:** Brain-Score validation | **8 mo:** Submit model to MIT Brain-Score Language benchmark | ~2 weeks engineering post-training |

---

## People Involved

| Name | Institution | Involvement |
|------|------------|-------------|
| **Snehal Nair** | University of Edinburgh (Independent AI Researcher) | Fellow — dataset pipeline, model training, annotation tooling, biographical intake instrument, browser extension, analysis code, reproducibility infrastructure (DVC, HuggingFace Hub, OpenNeuro) |
| **Lab Partner (TBC)** | Outreach active: UCL FIL, MRC CBU Cambridge, University of Nottingham | EEG equipment and lab space, existing hyperscanning paradigm, ethics/IRB umbrella, PI co-authorship. MUST deliverables do not depend on lab partner confirmation |

---

## 5) Data Landscape

The dataset is purpose-built. Message sources: relabelled public datasets (DailyDialog, Li et al. 2017; EmpatheticDialogues, Rashkin et al. 2019), researcher-constructed stimuli, and LLM-generated examples with human review gates. Annotation is conducted via Prolific Academic with a structured dual-pass protocol (SI and PI labelled separately, blind to each other).

Study 1b adds 100 new users under informed consent, with independent raters evaluating held-out messages. Personality data is local-first and encrypted (AES-256). If the EEG pilot proceeds, neural data is collected under joint ethics approval at the lab partner facility.

---

## 6) Data Characterisation

- **Fidelity:** 5 independent annotators per message; κ > 0.70 quality gate; separate κ for SI and PI; per-culture and neurodiverse-subset reliability reported.
- **Modality:** Text + structured metadata (relationship type, duration, valence) + EEG time-series (if Study 4 proceeds).
- **Volume:** 2,000 messages (Study 1); ~2,800 from 100 users over 4 weeks (Study 1b); 40-message stimulus set × 24 participants × 2 sessions (Study 4).
- **Scalability:** Protocol and architecture designed for extension to 10,000+ messages with naturalistic history and multilingual expansion in Year 2.

---

## 7) Anticipated Failure Modes

The main risk is annotation failure: if annotators cannot reliably agree on sender and perceived intent (κ < 0.70), the training signal is invalid. Mitigated through an early κ pilot in Month 1, two adjudication rounds, and schema redesign if needed.

A second risk is a null H₁ result — still publishable as the first rigorous test of whether dyadic context improves intent prediction at this scale.

---

## 8) Three Context Papers

1. **LeDoux, J. E. (1996).** *The Emotional Brain.* Simon & Schuster. — Subcortical threat-tagging pathway; the neurological basis for sender-receiver divergence.

2. **Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017).** Brain-to-brain entrainment: EEG interbrain synchronization while speaking and listening. *Scientific Reports*, 7(1), 4190. — Theta-band inter-brain synchrony as a communication-quality correlate; the H₃ outcome measure.

3. **Schrimpf, M., et al. (2021).** The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*, 118(45), e2105646118. — Brain-Score Language benchmark for neural plausibility assessment.

---

## 9) ARIA Alignment

The project advances **Scalable Neural Interfaces** through computational tools that model human mentalising at scale, and points toward **Collective Flourishing** through consent-based infrastructure for understanding rather than attention extraction.

---

## 10) Additional Information

**Skills and collaborator needs:** I have built and led AI teams at scale (KDD '24/'25), with a working prototype deployed (dyadicmentalising.streamlit.app) and production experience in NLP and ML systems. The EEG component requires a neuroscience lab partner with an existing hyperscanning paradigm, ethics infrastructure, and theta-band IBS analysis pipeline. MUST-tier deliverables are executable independently; the SHOULD tier is contingent on this partnership.

**Resource challenges:** No proprietary datasets required. The primary dependency is lab partner confirmation. Outreach is active (UCL FIL, MRC CBU Cambridge, Nottingham). If not confirmed by Month 3, EEG defers to Year 2 with no impact on core deliverables.

---

## Open-source Opt-in

Yes — include in the R&D Gap Map and list as a point of contact for AI researchers interested in computational models of communicative intent.
