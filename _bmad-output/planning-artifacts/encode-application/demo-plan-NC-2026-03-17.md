---
title: "NeuroAI Cognitive Companion — Streamlit Demo Plan"
subtitle: "Missing insights & additions for Encode x Pillar VC video submission"
author: Snnair
date: 2026-03-17
status: ready-to-implement
---

# Streamlit Demo Plan — Encode x Pillar VC Video Submission

**Source of truth:** `encode-application-NC-2026-03-17-v2.3.md`
**Current demo:** `http://localhost:8502/` (app.py, 2,820 lines)
**Goal:** Add all missing insights from the application, then record a 3–5 min video walkthrough.

---

## 1 · Gap Analysis — What's Missing

### Current Streamlit (4 tabs)
| Tab | What's there |
|-----|-------------|
| Scientific View | Message selector · gap gauge · relational context bar chart · 60-day H₂ trajectory |
| What Does This Mean? | Human story cards · bridge arc · cognitive field density · "where this lives" deployment vision |
| In the Wild | Mobile/laptop/audio mockups · trigger timeline · threshold table · neuroplasticity arc |
| The Network | 3-horizon frames (Mirror → Bridge → Map) · dual radar · Individual Consciousness · The Map |

### What the application contains that the demo does not show

| Application section | Missing from demo | Priority |
|---------------------|------------------|---------|
| **All 5 formal hypotheses (H1–H5)** with type, test design, ablation plan | Nowhere — H₂/H₃ mentioned in passing only | 🔴 CRITICAL |
| **Dataset architecture** — 2,000 messages, 5 relationship types, 3-source sampling, annotation protocol, κ ≥ 0.70 gate | Nowhere | 🔴 CRITICAL |
| **Model architecture** — RoBERTa-large + 16-dim relational context vector + personality context block + 4 ablation conditions (A/B/C/D) | Nowhere — model just implied | 🔴 CRITICAL |
| **Personality context / biographical intake instrument** (H4 cold-start problem) | Nowhere — Mirror concept referenced but not shown | 🔴 CRITICAL |
| **Study 1b cold-start RCT** — N=100, Group A vs B, 4 weeks, time-to-convergence metric | Nowhere | 🟠 HIGH |
| **12-month MUST/SHOULD/STRETCH work plan** | Nowhere | 🟠 HIGH |
| **ARIA Spaces alignment** — Scalable Neural Interfaces + Collective Flourishing | Nowhere | 🟠 HIGH |
| **Neurodivergent prediction H2.1** — intent gap elevated in neurodivergent dyads, pre-registered secondary analysis | Nowhere | 🟠 HIGH |
| **Brain-Score Study 3** — neural plausibility validation, TPJ/IFG alignment | Nowhere | 🟡 MEDIUM |
| **Lab partner outreach** — UCL FIL, MRC CBU, Nottingham Social Neuro; what each party brings | Nowhere | 🟡 MEDIUM |
| **Ethics framework** — domestic abuse safeguarding, cultural annotation bias, consent architecture | Nowhere | 🟡 MEDIUM |
| **12-month deliverables** — dataset on HuggingFace/OpenNeuro, paper submitted to ACL/EMNLP/CHI | Nowhere | 🟡 MEDIUM |

---

## 2 · Additions Plan — What to Build

### Addition A — "The Science" tab (NEW 5th tab)

A new tab, **"🔬 The Science"**, placed second in the tab order (between Scientific View and What Does This Mean?).

Contains 4 sections:

#### A1 — Five Hypotheses Panel
Visual card grid: one card per hypothesis, colour-coded by type.

| Card | Content |
|------|---------|
| **H₁** (Computational · Primary) | RoBERTa-large + 16-dim relational context vector achieves higher macro-F1 on perceived-intent than message-only baseline. Paired t-test, α=0.05, d≥0.3. **STATUS: Validation in progress.** |
| **H₂** (Behavioural · Secondary) | 60-day users show significant intent gap reduction vs Day 0 baseline. Within-subjects Wilcoxon, α=0.05. **STATUS: Study design finalised.** |
| **H₃** (Neural · Exploratory) | 60-day closed-loop feedback → significant increase in theta-band IBS. Pre/post EEG hyperscanning, N=20–24. **STATUS: Lab partner outreach active.** |
| **H₄** (Ablation · Within Study 1b) | Model with personality context block achieves higher cold-start F1 than relational-context-only model; gap narrows over 4 weeks. One-tailed t-test. **STATUS: RCT designed, recruitment Month 1.** |
| **H₅** (Exploratory · Beyond Year 1) | Consent-gated soul surface produces higher empathic accuracy gains than direct conversation. **STATUS: Post-fellowship — conditional on H₁+H₂.** |

Each card: hypothesis type chip (Computational / Behavioural / Neural / Ablation) · status badge (MUST / SHOULD / STRETCH) · test design one-liner · key metric.

#### A2 — Dataset Architecture
Three-column layout showing the 2,000-message annotation pipeline:

- **Source breakdown** (horizontal bar chart): Relabelled public datasets ~700 · Researcher-constructed stimuli ~600 · LLM-assisted synthetic (human-reviewed) ~700
- **5 relationship types** with oversampling target: Romantic partners · Parent-child · Close friends · Community/social groups · Professional colleagues
- **7 intent label space (I1–I7)** table with definitions (already in app data, needs surface)
- **Annotation protocol panel**: 5 annotators per message · SI and PI annotated blind · κ ≥ 0.70 gate · Prolific Academic · £5,000–7,000 estimated cost
- **Quality gate callout**: κ pilot Month 1 → if κ < 0.70 after 2 adjudication rounds → pause and redesign

Interactive element: **κ slider** — show what κ=0.40 vs κ=0.70 vs κ=0.85 looks like on a simulated annotation agreement heatmap.

#### A3 — Model Architecture
Side-by-side visual of the 4 ablation conditions:

```
Condition A: RoBERTa-large + 16-dim relational context vector  ← tests H₁
Condition B: RoBERTa-large (message content only, no context)   ← baseline
Condition C: RoBERTa-base + sentiment classifier               ← surface baseline
Condition D: RoBERTa-large + 16-dim vector + personality block ← tests H₄
```

Architecture flow diagram (HTML/CSS):
`[Message text] → [RoBERTa-large encoder] → [CLS token] + [16-dim relational vector] → [Classification head] → [7-way softmax P(I1-I7)]`

Personality context block annotation:
`[Biographical intake (8 questions)] → [600–900 token context block] → prepended to message → same encoder`

H₁ contrast label: `Condition A vs Condition B`
H₄ contrast label: `Condition D vs Condition A at Day 1`

Tech specs row: RoBERTa-large 355M params · AdamW · lr sweep 1e-5/2e-5/3e-5 · 3 runs × 5 epochs · Encode compute allocation (min £100k)

#### A4 — Study 1b Cold-Start RCT
Timeline visual for the 4-month RCT:

```
Month 1    → Recruitment (N=100), randomisation 1:1
Month 3    → Group B: 10–15 min biographical intake (personality context)
             Group A: standard onboarding (no personality context)
Months 3–7 → Active data collection: 2× weekly sender self-annotation
Month 5–6  → Held-out evaluation set scoring (researcher-labelled)
Months 7–8 → Primary analysis: H₄ confirmed or falsified
```

Metric panel: Primary = macro-averaged F1 at Day 1, 14, 28 · Secondary = time-to-convergence (week at which Group B F1 reaches Group A Week 4 F1)

Quote callout: *"A null result in H₄ is planned for and publishable."*

---

### Addition B — Personality Context / Cold-Start Demo (in "What Does This Mean?" tab)

Insert a new section after the "Interpretation Fingerprint" radar, before "Cognitive Field".

**Title:** *"What if the model has never seen this person before?"*

Content:
- The cold-start problem: at Day 1, there is no relational history. The model defaults to population-level priors — the gap score is systematically inflated.
- The biographical intake instrument solves this: 8 guided questions across 3 layers (identity values · decision architecture · narrative stories) administered in 10–15 minutes before first use.
- Interactive mockup: show 2 intent distributions for the same message — one with no context (cold start, high gap) and one conditioned on biographical intake (lower gap, more calibrated).

**Visual:** Two-panel side-by-side bar chart:
- Left: `"Can we talk tonight?" — Day 1, no context` → high-entropy PI distribution, gap ~0.28
- Right: `"Can we talk tonight?" — Day 1, with biographical intake` → PI distribution narrows toward SI, gap ~0.14

**Soul surface callout** (below the chart):
> The biographical intake instrument doubles as a consent-gated *soul surface* — a curated window into how a person thinks, shareable only when both partners have reciprocally shared their own. Raw answers never shared; only the derived intent model. Full revocation rights.

Styled as a "locked" card with a consent icon, making clear this is a future Horizon 1 feature.

---

### Addition C — Neurodivergent Prediction (in "Scientific View" tab)

Insert after Section 3 (Relational Context Effect) and before Section 4 (60-day trajectory).

**Title:** *"A testable prediction: neurodivergent dyads"*

One callout box:
> If the intent gap arises from asymmetry between subcortical threat-tagging and cortical mentalising, it should be **systematically elevated** in neurodivergent dyads. For autistic individuals, mentalising circuitry requires greater effort. For ADHD, attentional load reduces resources available for pragmatic inference. This is not a deficit — it is a structural asymmetry the instrument is specifically designed to scaffold.
>
> **Pre-registered secondary analysis:** Intent gap scores stratified by neurodivergent/neurotypical annotator pairing. Test: is JSD significantly larger when annotator pairs include a neurodiverse rater?

Bar chart (mock data): 4 annotator-pair types × mean intent gap score:
- Both neurotypical: ~0.18
- NT sender / ND receiver: ~0.27
- ND sender / NT receiver: ~0.31
- Both neurodivergent: ~0.24

With error bars and a "Pre-registered · H2.1 · Months 3–7" badge.

---

### Addition D — ARIA Spaces Alignment (in "The Network" tab)

Insert between the 3-horizon frames and the Bridge dual-radar section.

**Title:** *"ARIA Spaces: where this programme lives"*

Two-column layout:

| 🧠 Scalable Neural Interfaces | 🌱 Collective Flourishing |
|---|---|
| The intent-conditioned model and dataset are computational tools that interface with human neural language processing. Validated against neural data via Brain-Score (Study 3) — testing whether pragmatic fine-tuning enhances neural similarity to language-selective cortex (IFG, aMTG, TPJ). | The Map (Horizon 3) is the long-term vision: intent infrastructure that reduces the structural cost of human miscommunication at population scale — built on consent architecture, not attention extraction. |
| *This is AI for Science, not science-flavoured product.* | *Measured by JSD at scale, not engagement metrics.* |

Brain-Score panel (below):
> **Study 3 — Brain-Score neural plausibility validation (Months 6–8, SHOULD)**
> Submit trained intent model to MIT Brain-Score Language benchmark. Target benchmarks: Pereira2018, Fedorenko2016, Blank2014. Extract hidden-state activations at each transformer layer; fit linear regression probes to fMRI ROI activations in language-selective cortex. If intent model scores above RoBERTa-base on neural alignment → pragmatic fine-tuning enhances neural similarity to human language processing.

---

### Addition E — 12-Month Work Plan (in "The Network" tab or new Science tab)

Place at the end of "The Science" tab (Addition A).

**Gantt-style visual** using Plotly horizontal bar chart:

| Tier | Period | Activity | Key Output |
|------|--------|----------|------------|
| MUST | Month 1 | κ pilot · ethics application · Study 1b pre-screening | Protocol validated |
| MUST | Months 1–3 | 2,000-message annotation · online H₂ probe N=50 | Dataset v1.0 |
| MUST | Month 3 | Ethics approval · Study 1b data collection begins | Data stream active |
| MUST | Months 3–6 | RoBERTa fine-tuning · ablation studies | H₁ confirmed/falsified · model on HuggingFace |
| MUST | Month 5 | Paper draft #1: dataset + model + H₁ | arXiv preprint |
| MUST | Months 7–8 | Study 1b primary analysis | H₄ confirmed/falsified |
| MUST | Months 11–12 | Full study paper | Submitted to ACL/EMNLP/CHI |
| SHOULD | Months 6–8 | Brain-Score · EEG pilot design · IRB approval | Brain-Score result |
| SHOULD | Months 7–11 | 60-day EEG pilot N=20–24 | H₂/H₃ data |
| STRETCH | Months 9–12 | H₃ neural analysis | IBS pre/post comparison |

Colour code: MUST = dark teal · SHOULD = amber · STRETCH = grey
Footnote: *"SHOULD tier requires confirmed lab partner by Month 3. MUST tier is fully executable independently."*

---

### Addition F — Ethics Signpost (in "In the Wild" tab)

Insert before the privacy & tech specs section.

**Title:** *"Built with safety architecture from the start"*

4-card grid:

| Card | Content |
|------|---------|
| 🚨 Domestic abuse safeguarding | When model shows sustained divergence + high self-interest asymmetry → explicit signpost to National Domestic Abuse Helpline. Rapid account deletion accessible from app's first screen. Session-disabling 3-tap gesture. No identifying information on lock screen. |
| 🌍 Cultural annotation bias | Minimum 3 distinct cultural backgrounds in 5-annotator pool. Per-culture κ reported. High cross-cultural-variance categories flagged in dataset. |
| 🧩 Neurodivergent inclusion | Neurodiverse-authored messages included (recruited via autism/ADHD community groups). Separate κ computed on neurodiverse subset. Model error rates on neurodiverse messages explicitly reported. |
| 🔒 Biographical intake data | Local-first, AES-256 encrypted at rest. Never shareable with any partner or third party. Fully deletable. Ablation-first principle: fields that don't improve H₄ removed before v2. |

---

## 3 · Video Script — 4-Minute Demo Walkthrough

### Pre-video prep
- Set browser window to 1280×800, zoom 100%
- Start on the opening hero frame (scroll to top before recording)
- Disable notifications, close other apps
- Use screen recording with microphone (e.g., Loom or QuickTime)

---

### Segment 1 · Hook (0:00–0:30)

**Show:** Opening hero frame
**Say:**
> "The largest untapped source of human potential is not a new model. It's the gap between what humans mean — and what others receive. This is the NeuroAI Cognitive Companion, a research instrument that makes that gap measurable for the first time."

**Action:** Scroll slowly through the opening frame — Amygdala → Prefrontal Cortex → Intent Gap flow diagram.

---

### Segment 2 · The Core Demo (0:30–1:30)

**Show:** Scientific View tab
**Say:**
> "Here's the core finding. Take the message 'Can we talk tonight?' and watch what happens when I change only the relational context."

**Actions:**
1. Select message: "Can we talk tonight?"
2. Select context: "Partner of 3+ years · positive recent history" → show gap 0.003, point to gauge "Near-unanimous"
3. Switch to: "Partner of 3+ years · after conflict" → show gap 0.391, point to gauge "Crossed wires"
4. Say: "Same message. Same words. The relational history is the primary signal — not the text."
5. Scroll to Section 3 (Relational Context Effect) bar chart — let it speak for itself.
6. Briefly show Section 4 (60-day trajectory): "This is what H₂ is designed to detect — a measurable decline in this number over 60 days."

---

### Segment 3 · The Five Hypotheses (1:30–2:15)

**Show:** "The Science" tab → A1 Five Hypotheses panel
**Say:**
> "This programme is structured around five formal hypotheses — each one independently publishable, each one building on the last."

**Actions:**
1. Point to H₁: "H₁ tests whether relational context improves intent prediction — computational, testable against a message-only baseline."
2. Point to H₂: "H₂ tests whether 60 days of the instrument reduces the gap — behavioural, within-subjects."
3. Point to H₃: "H₃ is the stretch goal — does it leave a trace in the brain? Theta-band IBS, EEG hyperscanning, N=20–24."
4. Point to H₄: "H₄ solves the cold-start problem — what if there's no history yet? That's the biographical intake instrument."
5. Say: "Every hypothesis is pre-registered, every null result is publishable."

---

### Segment 4 · The Model (2:15–2:45)

**Show:** "The Science" tab → A3 Model Architecture
**Say:**
> "The model is RoBERTa-large, fine-tuned with a 16-dimensional relational context vector appended to the CLS token. We test four ablation conditions — this is rigorous science, not a product demo."

**Actions:**
1. Point to the architecture flow diagram
2. Highlight Condition A vs B (H₁ test)
3. Highlight Condition D (adds personality block — H₄ test)
4. Show the compute spec: "RoBERTa-large, 355M parameters — compute via Encode fellowship allocation."

---

### Segment 5 · Cold Start & Personality Context (2:45–3:15)

**Show:** "What Does This Mean?" tab → Addition B (cold-start panel)
**Say:**
> "The cold-start problem: at Day 1, there's no relational history. The model defaults to population-level priors, inflating the gap. The biographical intake instrument — 8 questions, 10 minutes — solves this."

**Actions:**
1. Show the two-panel chart (Day 1 no context vs Day 1 with biographical intake)
2. Point to gap score drop: "From 0.28 to 0.14 — calibrated intent prediction before a single message is exchanged."
3. Show the soul surface callout card: "And over time, with mutual consent, this becomes the relational bridge — not surveillance, but shared understanding."

---

### Segment 6 · ARIA Alignment & Long-Run Vision (3:15–3:50)

**Show:** "The Network" tab → ARIA Spaces panel, then The Map section
**Say:**
> "This programme sits at the intersection of two ARIA Spaces: Scalable Neural Interfaces — validated against Brain-Score language benchmarks — and Collective Flourishing. The Map is the long-run vision: a population-scale atlas of communicative intent. Not built on engagement metrics — built on consent architecture and trust."

**Actions:**
1. Show ARIA panel
2. Scroll to The Map visualisation
3. Let the network graph animate briefly

---

### Segment 7 · Close (3:50–4:00)

**Show:** Return to opening hero frame (scroll to top)
**Say:**
> "We are not building a chatbot. We are building the instrument that measures — and closes — the biological gap between human minds. Twelve months. Five hypotheses. The dataset does not yet exist. That's the point."

---

## 4 · Implementation Order

| # | Addition | Tab | Complexity | Time estimate |
|---|----------|-----|------------|---------------|
| 1 | Five Hypotheses panel (A1) | New "The Science" tab | Medium | 2–3h |
| 2 | Dataset Architecture (A2) | New "The Science" tab | Medium | 2–3h |
| 3 | Model Architecture (A3) | New "The Science" tab | Low | 1–2h |
| 4 | Study 1b RCT (A4) | New "The Science" tab | Low | 1h |
| 5 | 12-Month Work Plan (Addition E) | New "The Science" tab | Medium | 2–3h |
| 6 | Personality Context / Cold-Start (Addition B) | What Does This Mean? | Medium | 2h |
| 7 | Neurodivergent Prediction (Addition C) | Scientific View | Low | 1h |
| 8 | ARIA Spaces Alignment (Addition D) | The Network | Low | 1h |
| 9 | Brain-Score callout (part of D) | The Network | Low | 30min |
| 10 | Ethics Signpost (Addition F) | In the Wild | Low | 1h |

**Total estimated implementation: ~14–16 hours**
**Minimum viable set for video (items 1–6): ~10–12 hours**

---

## 5 · Tab Order After Changes

```
Tab 1: 📊 Scientific View      (existing + Addition C neurodivergent)
Tab 2: 🔬 The Science          (NEW — A1 hypotheses + A2 dataset + A3 model + A4 RCT + E timeline)
Tab 3: 🫀 What Does This Mean? (existing + Addition B cold-start)
Tab 4: 📱 In the Wild          (existing + Addition F ethics)
Tab 5: 🌐 The Network          (existing + Addition D ARIA)
```

---

## 6 · Video Recording Checklist

- [ ] All 5 tabs load cleanly (no errors)
- [ ] Browser at 1280×800
- [ ] Demo server running: `streamlit run app.py --server.port 8502`
- [ ] Microphone tested
- [ ] Recording software ready (Loom / QuickTime / OBS)
- [ ] Encode x Pillar VC badges visible in top-left
- [ ] Walk through video script once before recording
- [ ] Record 1–2 takes; keep best
- [ ] Trim to ≤5 minutes
- [ ] Export as MP4, 1080p if possible

---

*Plan authored: 2026-03-17. Source application: v2.3 final submission. Implementation target: before Encode deadline.*
