# NeuralConnexions: The Science of What They Actually Meant

*Closing the intent gap between digital communication and human connection*

---

## The Problem

Miscommunication is among the primary drivers of relationship breakdown (Gottman, 1999), workplace conflict (CPP Inc., 2008), and therapeutic failure (Safran & Muran, 2000) — yet no scientific instrument exists to measure it. The biological basis is well-established: ambiguous emotional stimuli are threat-tagged via subcortical processing (LeDoux, 1996) before higher-order language and mentalising systems resolve intent. In digital text — where prosody, facial expression, and physical context are absent — this timing asymmetry makes misunderstanding especially likely.

The same message carries a different intent distribution depending on who sent it, who received it, and the history between them. No published NLP system models intent as a dyadic phenomenon conditioned on relational history. Sentiment classifiers measure tone; emotion recognition systems measure affective expression. Neither asks what a person most likely *meant*, given who they are and who they are talking to.

This is the **intent gap** — the measurable divergence between sender intent and perceived intent — and it is invisible, pervasive, and cumulative. Each misread builds on the last.

---

## The Vision

**NeuralConnexions (NC)** is a scientific instrument that measures the intent gap and tests whether surfacing it changes behaviour. The core hypothesis: repeated exposure to accurate intent predictions over a 60-day period will reduce sender-receiver divergence, with measurable changes in both behaviour and neural markers.

The intervention is embedded in existing digital text communication — a lightweight overlay that surfaces the model's predicted intent distribution during the natural pause between reading a message and composing a reply, offering an alternative interpretation before the receiver commits to a threat-based reading.

NC is not a communication coach, a sentiment analyser, or a conflict-resolution chatbot. It is a **computational model of communicative intent** — the first system to combine three capabilities simultaneously:

1. **Person-aware intent modelling.** NC conditions every intent prediction on *who the person is* — their identity values, decision architecture, and narrative history — via a structured personality context block derived from an 8-question biographical intake instrument. This solves the cold-start problem from Day 1: accurate predictions without months of message history accumulation.

2. **Dyadic relational context conditioning.** A 16-feature relational context vector — encoding relationship type, duration, recent valence, message frequency, and rolling intent-gap history — is concatenated with the message representation at classification. The same words, sent between different people, produce different intent distributions.

3. **Neuroscience-grounded intervention timing.** The overlay targets the biological window between message receipt and threat-tagging — surfacing a re-appraisal signal before the amygdala response embeds a false interpretation. The intervention operates at the *moment of reception*, where it has maximum cognitive effect.

---

## Scientific Foundation

NC is built as a testable scientific programme with four pre-registered, falsifiable hypotheses:

- **H1 (Computational):** A language model conditioned on dyadic relational history predicts receiver-parsed intent with significantly higher accuracy than a message-only baseline. Tested via ablation across 4 conditions on a 2,000-message annotated dataset. Success criterion: Cohen's d >= 0.3, paired t-test.

- **H2 (Behavioural):** 60-day intent feedback reduces sender-receiver divergence scores. 100 participants recruited via Prolific, randomised 1:1 (feedback vs. control), scored on AQ-50, GAD-7, PHQ-9. Within-subjects pre/post, Wilcoxon signed-rank.

- **H3 (Neural, time allowing):** 60-day feedback shifts predictive coding EEG markers — alpha/beta for predictions, gamma for feedforward signals. N=20-24 dyadic pairs, EEG hyperscanning via PPLS Cognitive Neuroscience Suite.

- **H4 (Cold-start):** Personality context from the biographical intake instrument improves Day 1 accuracy before any dyadic history exists. Tested within the validation study, randomised 1:1 (with/without personality context).

**Execution order:** H1 -> H4 -> H2 -> H3 — computational validation before behavioural and neural studies. Each level is independently publishable; null results are pre-registered.

The core model is **RoBERTa-large** (355M parameters), fine-tuned for intent classification with two conditioning signals over a **7-category intent label space** derived from speech act theory (Searle, 1969), attachment communication patterns (Mikulincer & Shaver, 2007), and pragmatic emotion expression. The performance metric — **Jensen-Shannon divergence** between sender-intent and perceived-intent distributions — is the first operationalisation of communicative misalignment at this scale.

---

## Who It Serves

NC examines five relationship types where the intent gap causes the most relational damage:

- **Romantic partners** — where recurring conflicts stem from misread intent rather than substantive disagreement
- **Parent-child** — particularly families navigating communication with neurodivergent children
- **Close friends** — where ambiguity accumulates silently and erodes trust
- **Community/social** — online communities where text-only communication amplifies intent ambiguity
- **Professional** — high-stakes communication in mediation, negotiation, and clinical settings

**Interindividual variation matters.** Computational psychiatry research suggests individuals with ASD may form weaker relational priors, those with anxiety may form stronger threat priors, and those with depression may show systematic negative biases in intent interpretation (Series, 2020). NC treats intent-gap variation as a function of broad interindividual differences rather than categorical diagnoses — testing predictions along continuous trait measures (AQ-50, GAD-7, PHQ-9) in a general population sample. This makes NC particularly relevant for neurodivergent users, whose intent-expression gap is wider than the neurotypical baseline.

---

## Translation Pathways

If the science holds, NC translates into a consumer product and an institutional platform across multiple domains:

**Consumer Product — Real-Time Intent Companion**

The scientific instrument becomes a multi-surface AI companion — browser extension and mobile app — that predicts what a person *actually means* and presents it to the receiver before the amygdala response can embed a false interpretation. The product operates across the digital text channels where ambiguity does its greatest relational damage: messaging apps, email, and workplace communication tools.

The product architecture preserves the scientific instrument's core properties: person-aware conditioning via the biographical intake instrument (productised as the "Soul Document" — a portable, structured, model-agnostic personality representation), dyadic context injection, and probabilistic intent display with confidence levels. Users see the intent distribution, not a single label — maintaining the instrument's epistemic honesty at consumer scale.

**Privacy as architectural constraint.** Personality data is local-first, AES-256 encrypted, not accessible to partners or third parties, and fully deletable. The differentiator is not data capture — it is data trust. This is particularly critical given the domestic abuse threat model: any relationship intelligence tool in the wrong hands is a surveillance weapon. NC is designed against this from the architecture up.

**Institutional Integration**

- **Couples therapy platforms** — a read-only, consent-gated view for therapists working with clients who use NC, showing aggregate pattern trends (not message content)
- **Workplace conflict reduction** — reducing the estimated 2.8 hours per employee per week spent managing miscommunication-driven conflict (CPP Inc., 2008)
- **Co-parenting applications** — tools for high-conflict separated families where every message carries relational weight
- **Mediation and negotiation services** — professional contexts where intent misalignment has material consequences
- **Clinical research** — in collaboration with Series (Computational Psychiatry, Edinburgh), the framework provides a controlled way to study how interindividual differences in psychological traits shape intent inference

**Revenue model:** Freemium — core intent predictions free, paid subscription for enhanced usage, institutional API licensing for platform partners.

**Research Network (Long-term)**

The long-term goal is to establish a research network for communication measurement — applying the intent-gap framework across languages, cultures, and populations. The annotated dataset and the biographical intake instrument are designed as independently publishable contributions. If the model achieves Brain-Score Language benchmark validation, it becomes open-source scientific infrastructure — an "ImageNet for communicative intent."

---

## The Flywheel

Science -> Product -> Data -> Better Science.

Every user interaction is a scientific data point. Every publication strengthens the product's credibility. Every credibility gain brings higher-quality users whose corrections improve the model. NC competes on data quality and scientific legitimacy — not data volume. The RCT results provide causal evidence (not correlational) for NC's effect on communication outcomes, creating a credibility moat that no competitor can acquire through product iteration alone.

---

## Competitive Position

| Category | What exists | What NC adds |
|---|---|---|
| Pre-send tone detection (Grammarly, Hemingway) | Analyse your draft before you send | No receiver-side interpretation; no person model; no relational history |
| Personality profiling (Crystal Knows, DISC) | Infer personality from public data | No real-time message interception; no intent prediction; professional context only |
| Post-hoc relationship coaching (Gottman apps, Lasting) | Reflect on past interactions | No real-time intervention; no message-level analysis |
| General AI assistants (ChatGPT, Claude) | Answer "what did they mean?" | No personality instrument; no persistent relational context; no scientific validation |
| Emotion regulation (Headspace, Calm) | Regulate your own state | Do not address the source of the trigger |

**NC's unoccupied position:** Real-time, receiver-side, person-aware intent prediction grounded in neuroscience and validated by a pre-registered RCT. No product in any adjacent category is building toward this position.

---

## ARIA Alignment

The project advances **Scalable Neural Interfaces** through computational tools that model human mentalising at scale, and points toward **Collective Flourishing** — characterising how psychological trait variation shapes miscommunication directly serves flourishing for underserved groups.

---

## 12-Month Delivery

| Milestone | Timeline |
|---|---|
| Validated dataset (2,000 messages, dual SI/PI labels, kappa > 0.70) | Month 3 |
| Intent-conditioned model trained, H1 tested, Paper #1 submitted | Month 6 |
| Cold-start ablation H4 tested | Month 6-8 |
| Validation study begins (N=100, Prolific) | Month 6 |
| EEG pilot begins (H2/H3, 12 dyadic pairs) | Month 8 |
| Brain-Score Language benchmark submission | Month 8 |
| Peer-reviewed paper submitted (ACL, EMNLP, or CHI) | Month 12 |
| Product prototype with real-time intent overlay | Month 12 |

---

## Team

- **Snehal Nair** — Fellow. Independent AI Researcher. Dataset pipeline, model training, annotation tooling, biographical intake instrument, intervention delivery, prototype development. Senior AI leader with production NLP/ML experience (KDD '24/'25 industrial track).
- **Prof Peggy Series** — Lab Advisor and co-PI. Chair in Computational Psychiatry, University of Edinburgh, School of Informatics. Bayesian inference framing, experimental design, interindividual differences in social cognition, co-authorship. Ethics approval via School of Informatics.
- **PhD Student (starting 2027)** — Potential collaborator (EEG/ML). Biomedical Innovations CDT, University of Edinburgh. Co-supervised by Lena Williams (Neuroscience) and Andrew Stanfield (Psychiatry). Available to support EEG pilot analysis.

---

*For full technical specification, success metrics, and implementation detail, see the attached Product Requirements Document.*
