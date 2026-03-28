---
title: "Encode Fellowship — 3-Minute Demo Plan"
status: final
date: 2026-03-27
format: Loom screen recording (screen + face cam bottom-left)
total-duration: "2:55 (5s buffer)"
---

# Encode Fellowship — 3-Minute Demo Plan

> **Prompt:** "Help us understand how you work — please demo a technical project you've worked on in less than 3 minutes."

## Pre-Recording Setup

| Item | Detail |
|---|---|
| **Architecture visual** | Screenshot of agentic platform architecture diagram → open full-screen in Preview (no scrolling) |
| **Streamlit Tab A** | `dyadicmentalising.streamlit.app` → "Can we talk tonight?" + "Close friend · neutral history" (pre-loaded) |
| **Streamlit Tab B** | `dyadicmentalising.streamlit.app` → "Can we talk tonight?" + "Ex-partner · high conflict" (pre-loaded) |
| **Browser** | Full-screen mode (Cmd+Shift+F) — no URL bar, no bookmarks |
| **Microphone** | Dedicated mic or AirPods Pro — test audio before recording |
| **Loom** | Face cam bottom-left (small, ~20% screen) |
| **Screen resolution** | 1920×1080 |
| **Browser zoom** | 125% |
| **Test recording** | Full 3-min playback before final take |
| **File size** | < 100MB for upload |

---

## 🎬 0:00–0:15 — Hook (15 sec)

**[Face to camera, no screen share yet]**

> "Encode asked me to show how I work. I'll show two things: a production AI system I shipped at Viator — and a research prototype I built in three months for this fellowship."

---

## 🎬 0:15–1:20 — Agentic Platform (65 sec)

**[Full-screen: architecture diagram screenshot]**

### Problem (10s)

> "Our first chatbot failed in two weeks — told a customer their Colosseum tour included hotel pickup. It didn't. Root cause: no unified data layer connecting policies, bookings, reviews, and supplier rules."

### Architecture (15s)

> "Five subsystems: DeBERTa intent router at 15 milliseconds, GraphRAG knowledge layer with 92% cache hit rate, three-tier memory capped at 4,000 tokens, LangGraph orchestration with parallel tool calls, and confidence-based escalation at 0.85."

### Rigour (15s)

> "Every response cites its source tier — Gold for policy, Silver for product data, Bronze for traveller tips. We A/B tested 10,000 conversations. We deliberately kept refund disputes human-only — customers needed empathy, not accuracy."

### Results (10s)

> "43% Tier-1 deflection — short of the 60% target. Knowledge gaps, not agent capability. That honesty about what failed is the same discipline I've built into the fellowship proposal."

### Bridge (15s)

> "This platform integrates five separate projects — FAQ extraction, review summarisation, tip extraction, prompt optimisation, governance. The pattern is always: decompose, measure each subsystem, compose. I'm now moving from optimising customer journeys to measuring human understanding."

**Voice cadence:** Confident, production-engineer tone.

---

## 🎬 1:20–2:35 — Streamlit Prototype (75 sec)

**[Switch to pre-loaded Streamlit Tab A]**

### Setup (10s)

> "'Can we talk tonight?' — close friend, neutral history. The intent distribution: dominated by seeking connection. Gap score near zero."

### The Switch (5s)

**[Click to Tab B]** — **3 seconds of silence. Let the visual land.**

### Narrate the shift (15s)

> "Same words. Ex-partner, high conflict. Expressing frustration and setting boundary spike. Gap score jumps to 0.35. That shift is the intent gap — Jensen-Shannon divergence between what was meant and what was received."

### Interindividual differences prediction (10s)

> "Bayesian prediction: higher autistic traits may mean weaker relational priors, higher anxiety stronger threat priors, higher depression negative intent biases — each predicting differently structured gaps. My lab advisor Peggy Seriès at Edinburgh specialises in exactly this."

### The Science tab (20s)

**[Quick scroll through The Science tab — don't read, let the viewer see structure]**

> "Behind the demo: four pre-registered hypotheses, 2,000-message dataset with dual-pass annotation — context-blind then context-aware — four ablation conditions on RoBERTa-large, 12-month plan with MUST and SHOULD tiers. General population scored on AQ-50, GAD-7, and PHQ-9. Core deliverables are executable with fellowship compute. The EEG pilot uses the PPLS Cognitive Neuroscience Suite at Edinburgh."

### 60-day trajectory (15s)

**[Show 60-day trajectory visualisation]**

> "The intervention question: does feeding back the prediction change behaviour over time? This shows what convergence looks like. The real test is a within-subjects pre/post study measuring whether the gap actually closes."

**Voice cadence:** Curious researcher tone — slower, more deliberate.

---

## 🎬 2:35–2:55 — Close (20 sec)

**[Face to camera]**

> "That's how I work: decompose, measure, ablate, publish — including when the result is null. I've done that at production scale for a decade. With Encode and Peggy Seriès at Edinburgh, I have 12 months to test whether relational context actually closes the intent gap — and whether the effect varies with how people are wired."

**Voice cadence:** Earnest, direct eye contact.

---

## Timing Budget

| Section | Duration | Cumulative |
|---|---|---|
| Hook | 15s | 0:15 |
| Agentic platform | 65s | 1:20 |
| Streamlit demo | 75s | 2:35 |
| Close | 20s | 2:55 |
| **Buffer** | **5s** | **3:00** |

---

## Live Links to Share

- **Q22 (live project links):** https://dyadicmentalising.streamlit.app/
- **Portfolio:** https://snehalnair.github.io/portfolio/portfolio-2/

---

## What NOT to Do

- Don't show all 5 Streamlit tabs — pick the 3 strongest moments
- Don't read text off the screen — narrate what the viewer sees
- Don't mention "product" or "startup" — this is a science demo
- Don't demo the browser extension — it doesn't exist yet
- Don't show the JS-divergence formula — say the name, let the visual carry meaning
- Don't rush — the 3-second silence after the gap score jump is the most powerful moment
- Don't say "neurodivergent dyads" — say "interindividual differences" or "psychological trait profiles"
- Don't say "clinical populations" or mention hospitals — it's general population via Prolific
- Don't say "Sériès" with wrong accent — it's "Seriès" (accent on second e only)
- Don't say "theta-band" alone — say "predictive coding markers" if EEG comes up

---

## Practice Protocol

1. Read through once at normal speed (target: 2:50)
2. Record a test take — play back, check audio and tab switches
3. Record final take at 80% speed — the buffer absorbs any nerves
