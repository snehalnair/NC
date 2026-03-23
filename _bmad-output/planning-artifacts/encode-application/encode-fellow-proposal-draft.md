# Encode: AI for Science Fellowship — Fellow Proposal

**Name:** Snehal Nair
**Current Institution:** University of Edinburgh

---

## 1) Problem

Human miscommunication has a biological substrate. The amygdala processes emotional salience via a subcortical pathway (LeDoux, 1996) that threat-tags emotionally ambiguous stimuli before the prefrontal cortex and temporoparietal junction (TPJ) complete semantic interpretation. In digital text — where prosody, expression, and physical context are absent — this timing asymmetry means ambiguous messages are systematically misread before their intent is understood.

No existing NLP system addresses this directly. Sentiment classifiers measure surface tone. Emotion recognition systems measure affective expression. Neither asks: *what did this person most likely mean, given who they are and who they are talking to?* The same message — "Can we talk tonight?" — carries a fundamentally different intent distribution when sent by a new colleague versus a partner after a difficult week. Relational history is not context noise; it is the primary signal.

**Four concrete scientific gaps this project addresses:**

1. No neural-pragmatic dataset conditions intent annotation on dyadic relational history with dual sender/receiver labelling and inter-rater reliability validation.
2. No language model has been trained to predict receiver-parsed intent conditioned on dyadic relational context.
3. No empirical study has tested whether closed-loop intent feedback produces measurable shifts in neural markers of mentalising circuitry.
4. No structured personality characterisation instrument has been tested as an independent conditioning signal for intent prediction, or evaluated for cold-start inference.

These claims rest on our review of the pragmatics, social NLP, and affective computing literature as of March 2026.

---

## 2) Solution

**Scientific instrument:** A RoBERTa-large language model (355M parameters; Liu et al., 2019) fine-tuned for intent classification with a novel architecture modification:

- **16-dimensional dyadic relational context vector** — encoding relationship type (5 categories), duration, recent valence, message frequency, and rolling intent gap history — concatenated to the [CLS] token before the classification head
- **Personality context block** — a 600–900 token structured representation derived from a biographical intake instrument (8 guided questions across identity values, decision architecture, and narrative stories) — prepended to the message at inference time
- **Output:** Probability distribution over 7 intent categories (seeking connection, expressing concern, setting boundary, seeking validation, expressing frustration, making request, giving information), predicted from both sender and receiver perspectives

**Training data:** A purpose-built 2,000-message annotated dataset with dual sender-intent (SI) and perceived-intent (PI) labels, 5 annotators per message, across 5 relationship types. Sources: relabelled public datasets (~700), researcher-constructed stimuli (~600), and LLM-generated with human review (~700). The intent gap is quantified as Jensen-Shannon divergence between P(SI) and P(PI).

**Intervention instrument:** A browser extension that surfaces the model's intent prediction — what the sender most likely meant — in the cognitive reappraisal window between reading a message and replying. This fills the pause with an alternative interpretation before the receiver commits to a threat-based reading.

**Validation chain across four levels:**

| Level | Hypothesis | Test |
|-------|-----------|------|
| Computational (H₁) | Relational context improves intent prediction over message-only baseline | Ablation: model with context vs. without (paired t-test, d ≥ 0.3) |
| Cold-start ablation (H₄) | Personality context improves Day 1 accuracy before dyadic history accumulates | 100 users randomised 1:1, personality context vs. none |
| Behavioural (H₂) | 60-day intent feedback reduces intent gap scores | Within-subjects pre/post (Wilcoxon signed-rank) |
| Neural (H₃, stretch) | 60-day feedback increases theta-band inter-brain synchrony | EEG hyperscanning, N=20–24, pre/post (Wilcoxon signed-rank) |

Each level is independently publishable; null results are pre-registered and publishable.

---

## 3) Translation Opportunity

The scientific instrument validates a new measurement construct (the intent gap) and a new conditioning signal (dyadic relational context). If H₁ confirms that relational context measurably improves intent prediction:

- **Product:** The browser extension becomes a consumer cognitive companion — an intent prediction overlay for digital messaging. The biographical intake instrument becomes a structured onboarding flow. Revenue model: freemium with premium features (personality context, relationship-specific tuning).
- **Open-source research tool:** The annotated dataset and trained model are released on HuggingFace under Apache 2.0, enabling other researchers to build on dyadic intent prediction.
- **Institutional partnerships:** Clinical applications in couples therapy, family mediation, and workplace communication training. Letter of intent from at least one therapy/mediation service is a 12-month business target.
- **Neurodivergent applications:** The model predicts systematically wider intent gaps in neurodivergent dyads (testable secondary prediction). If confirmed, the tool is most scientifically relevant to populations where miscommunication has the sharpest biological basis — a pathway to specialist partnerships with autism/ADHD support organisations.
- **Longer-term vision (Year 2+):** Consent-gated mutual personality sharing between relationship partners — a computational implementation of Gottman's "love map" concept — enabling indirect, safe probing of a partner's inner world without the face-threat cost of direct questioning.

**ARIA alignment:** The intent-conditioned model and dataset advance *Scalable Neural Interfaces* (computational tools modelling human neural processes at scale). The longer-term vision maps to *Collective Flourishing*: infrastructure for human understanding at population scale, built on consent rather than attention-extraction.

---

## 4) Goals / Milestones / Resources

| Goals (What success is) | Milestones (3 mo, 6 mo, 1 yr) | Resources Needed |
|-------------------------|-------------------------------|-----------------|
| **MUST:** Validated annotated dataset with dual SI/PI labels and κ > 0.70 | **3 mo:** 2,000-message dataset annotated, κ validated, published on HuggingFace | Compute (fellowship allocation); Prolific Academic annotator budget (~£5–7K); annotation tooling (built by fellow) |
| **MUST:** Intent-conditioned model with H₁ confirmed or falsified | **6 mo:** RoBERTa-large fine-tuned across 4 ablation conditions; H₁ result; model released on HuggingFace; Paper #1 submitted (dataset + model) | Compute for training (3 runs × 4 conditions × 5 epochs); HuggingFace hosting |
| **MUST:** Cold-start ablation (H₄) confirmed or falsified | **6 mo:** Study 1b data collection complete (N=100); **8 mo:** H₄ analysis complete | Ethics approval (Month 1–3); participant recruitment |
| **MUST:** Peer-reviewed paper submitted | **12 mo:** Full paper (dataset + model + pilot results) submitted to ACL/EMNLP/CHI | — |
| **SHOULD:** 60-day EEG pilot (H₂/H₃) | **8 mo:** EEG pilot begins; **11 mo:** Day 60 sessions complete; **12 mo:** analysis | Lab partner with 64-channel EEG, hyperscanning paradigm, ethics umbrella |
| **SHOULD:** Brain-Score neural plausibility validation | **8 mo:** Model submitted to MIT Brain-Score Language benchmark | ~2 weeks engineering post-training |

---

## People Involved

| Name | Institution | Involvement |
|------|------------|-------------|
| **Snehal Nair** | University of Edinburgh (Independent AI Researcher) | Fellow — dataset pipeline, model training, annotation tooling, biographical intake instrument, browser extension, analysis code, full reproducibility infrastructure |
| **Lab Partner (TBC)** | Outreach active: UCL FIL, MRC CBU Cambridge, U. of Nottingham | EEG equipment & lab space, existing hyperscanning paradigm, ethics/IRB umbrella, PI co-authorship on neural study. Core MUST deliverables do not depend on lab partner confirmation |

---

## 5) Data Landscape

**In-house (built by fellow):** The 2,000-message annotated dataset is purpose-built for this project. No equivalent dataset exists — dual SI/PI labels conditioned on dyadic relational history is the scientific novelty. Message sources include relabelled public datasets (DailyDialog, EmpatheticDialogues — both publicly available), researcher-constructed stimuli, and LLM-generated synthetic examples with human review gates. All annotation is conducted via Prolific Academic.

**Study 1b data:** 100 new users' messages collected with informed consent under ethics approval. Messages are annotated by independent raters (not participants). Personality context data from biographical intake is local-first, AES-256 encrypted.

**EEG data (if lab partner confirmed):** Collected under joint ethics application at lab partner facility. Standard 64-channel EEG, stored per institutional data governance.

---

## 6) Data Characterisation

- **Fidelity:** 5 independent annotators per message; Cohen's κ > 0.70 gate before full annotation; separate κ for SI and PI labels; per-culture and neurodiverse-subset κ reported
- **Modality:** Text (messages) + structured metadata (relationship type, duration, valence) + EEG time-series (if Study 4 proceeds)
- **Volume:** 2,000 annotated messages (Study 1); ~2,800 messages from 100 users over 4 weeks (Study 1b); 40-message controlled stimulus set per EEG session × 24 participants × 2 sessions (Study 4)
- **Scalability:** The annotation protocol, intent label schema, and model architecture are designed for extension: Year 2 targets 10,000+ messages with naturalistic dyadic history and multilingual expansion

---

## 7) Anticipated Failure Modes

The most likely reason for failure is **κ < 0.70 on the annotation pilot** — if human annotators cannot reliably agree on sender and perceived intent using the 7-category schema, the training signal is invalid and no model can be meaningfully trained. This is mitigated by running the κ pilot in Month 1 before any full annotation, with two adjudication rounds and schema redesign if needed.

Secondary failure mode: **H₁ null result** — relational context may not improve intent prediction at this model scale. This is explicitly a publishable outcome (the first rigorous test of the dyadic conditioning hypothesis) and does not invalidate the dataset or the annotation methodology contribution.

---

## 8) Three Context Papers

1. **LeDoux, J. E. (1996).** *The Emotional Brain.* Simon & Schuster. — Establishes the subcortical thalamo-amygdala pathway: the biological mechanism underlying threat-tagging of ambiguous stimuli before cortical semantic processing, the core neurological basis for the intent gap.

2. **Pérez, A., Carreiras, M., & Duñabeitia, J. A. (2017).** Brain-to-brain entrainment: EEG interbrain synchronization while speaking and listening. *Scientific Reports*, 7(1), 4190. — Demonstrates theta-band inter-brain synchrony as a measurable correlate of communication quality, the neural outcome measure for H₃.

3. **Schrimpf, M., et al. (2021).** The neural architecture of language: Integrative modeling converges on predictive processing. *PNAS*, 118(45). — Establishes the Brain-Score Language benchmark used in Study 3 to test whether pragmatic fine-tuning enhances or degrades neural plausibility of the intent model.

---

## 9) ARIA Alignment

The intent-conditioned model and dataset advance **Scalable Neural Interfaces** by building computational tools that model human mentalising processes. The longer-term vision — consent-based infrastructure for understanding at population scale — maps to **Collective Flourishing**.

---

## 10) Additional Information

**Skills and collaborator needs:** I bring production AI engineering (NLP, ML systems at scale, KDD '24/'25), dataset pipeline design, and rapid prototyping (working demo at dyadicmentalising.streamlit.app). I need a neuroscience lab partner for the EEG component: someone with an existing hyperscanning paradigm, ethics infrastructure, and theta-band IBS analysis pipeline. The MUST-tier deliverables (dataset, model, H₁/H₄ papers) are executable independently; the SHOULD tier (EEG pilot) is explicitly contingent on this partnership.

**Resource challenges:** No proprietary datasets are required — all data is purpose-built or drawn from public sources. The primary resource dependency is lab partner confirmation for the EEG study. Outreach is active (UCL FIL, MRC CBU Cambridge, Nottingham). If not confirmed by Month 3, EEG defers to Year 2 with no impact on core deliverables.

---

## Open-source Opt-in

Yes — I would like the research opportunity included in the R&D Gap Map and to be listed as a point of contact for AI researchers interested in collaborating on computational models of communicative intent and dyadic mentalising.
