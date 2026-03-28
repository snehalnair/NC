---
title: "Encode Fellowship — 3-Minute Demo Plan v2"
status: draft
date: 2026-03-28
format: Loom screen recording (screen + face cam bottom-left)
total-duration: "2:28 (32s buffer, pauses included)"
---

# Encode Fellowship — 3-Minute Demo Plan v2

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

## The Narrative Thread

The demo tells one story in three acts:

> **I built AI systems at production scale → one failure taught me that the hardest problems aren't language problems, they're people problems → so I built a scientific instrument to measure that, and here's what it shows.**

Every sentence must pull the viewer forward to the next. No dead ends. No section should feel like it starts from scratch.

---

## Full Script (continuous)

### 🎬 0:00–0:18 — OPEN (16s spoken + 2s tab switch)

**[Face to camera, no screen share]**

> "I'm Snehal. I've spent a decade building AI systems at production scale — most recently at Viator, a Tripadvisor company. I want to show you what I learned there, and what it led me to build."

**[Cmd+Tab → Architecture diagram in Preview (2s)]**

**Voice:** Warm, direct. You're inviting them into a story, not delivering a pitch.

---

### 🎬 0:18–0:48 — PRODUCTION: THE LESSON (28s spoken + 2s tab switch)

**[Full-screen: architecture diagram — let the visual carry the detail]**

> "This is an agentic customer service platform I designed and shipped. First version failed in two weeks — told customers their tour included hotel pickup. It didn't. The fix was a five-subsystem architecture you see here. Result: 43% deflection across 10,000 conversations.
>
> But the interesting thing wasn't the success — it was the 57% that still failed. The hardest conversations weren't language problems. They were problems where two people meant different things by the same words. That question stuck with me."

**[Cmd+Tab → Streamlit Tab A (2s)]**

**Voice:** Confident, storytelling pace. The architecture is on screen — don't narrate what they can see. Narrate the *journey*.

**Transition thread:** "That question stuck with me" → bridges directly to the prototype.

---

### 🎬 0:48–1:18 — CORE DEMO: THE INTENT GAP (24s spoken + 4s pause + 2s tab switch)

**[Streamlit Tab A is showing: "Can we talk tonight?" — Close friend, neutral history]**

> "So I built this. 'Can we talk tonight?' — from a close friend, neutral history. The model predicts the intent: seeking connection. Gap score: near zero. Sender and receiver agree on what it means."

**[Click to Tab B — 4 seconds of silence. Let the visual land.]**

> "Same four words. Ex-partner, high conflict. Now the model predicts frustration and boundary-setting. Gap score: 0.35. The words didn't change — the relationship did. That divergence is measurable: Jensen-Shannon divergence between sender intent and perceived intent. And no published system models it."

**Voice:** Slow down for the gap score reveal. The 4-second silence after the tab switch is the most important moment in the demo — let the visual contrast do the work.

**Transition thread:** "No published system models it" → sets up the science.

---

### 🎬 1:18–1:50 — THE SCIENCE: WHY IT VARIES (30s spoken + 2s scroll)

**[Still on Streamlit — then quick scroll through The Science tab]**

> "The question this fellowship answers: why does the gap vary between people? Computational psychiatry research predicts it should. Weaker relational priors in autistic traits — harder to infer intent from context. Stronger threat priors in anxiety — ambiguous messages read as danger. Negative biases in depression.
>
> My lab advisor Peggy Seriès at Edinburgh works on exactly this — Bayesian models of how these traits shape perception. Together we've designed four hypotheses, a 2,000-message dataset with dual-perspective annotation, and a 12-month plan to test them."

**[Quick scroll through The Science tab during the second paragraph — don't read, let the viewer see the structure]**

**Voice:** Shift to curious researcher tone — slower, more deliberate. You're sharing what fascinates you, not selling.

**Transition thread:** "test them" → leads to "and here's what the test looks like over time."

---

### 🎬 1:50–2:06 — THE TRAJECTORY (14s spoken + 2s transition)

**[Show 60-day trajectory visualisation]**

> "And this is the intervention question: if you feed back the model's prediction to the receiver, does the gap close over time? This visualisation shows what convergence looks like. The real test is a within-subjects pre/post design — 100 participants over 60 days."

**Voice:** Let the visual breathe. Point at the convergence curve if using face cam.

**Transition thread:** "100 participants over 60 days" → grounds the close in what the fellowship enables.

---

### 🎬 2:06–2:28 — CLOSE (18s spoken + 2s camera transition + 2s hold)

**[Look at camera — transition away from screen share (2s)]**

> "That's how I work: build, measure, learn — and when the measurement reveals a deeper question, follow it. Encode gives me twelve months with Peggy Seriès to answer this one: does relational context close the intent gap, and does the answer depend on how each person is wired?"

**[Hold eye contact for 2 seconds. Let the question land. End.]**

**Voice:** Earnest, unhurried. This is a researcher telling you what they need to find out — not a founder making a pitch. End on the question.

---

## Timing Budget

| Section | Spoken | Pauses/Transitions | Total | Cumulative |
|---|---|---|---|---|
| Open (intro + hook) | 16s | 2s (tab switch) | 18s | 0:18 |
| Production system | 28s | 2s (tab switch) | 30s | 0:48 |
| Core demo (gap score) | 24s | 6s (pause + tab switch) | 30s | 1:18 |
| Science + Peggy | 30s | 2s (scroll) | 32s | 1:50 |
| 60-day trajectory | 14s | 2s (transition) | 16s | 2:06 |
| Close | 18s | 4s (camera + hold) | 22s | 2:28 |
| **Total** | **2:10** | **18s** | **2:28** | |
| **Buffer** | | | **32s** | **3:00** |

**The 32-second buffer absorbs:** speaking at 85% speed, an extra beat after the gap score, a hesitation, or a slower tab switch.

---

## The Narrative Thread (summary)

| Section | Last line | → | Next section opens with |
|---|---|---|---|
| Open | "what it led me to build" | → | Architecture diagram appears |
| Production | "That question stuck with me" | → | "So I built this" |
| Core demo | "no published system models it" | → | "The question this fellowship answers" |
| Science | "a 12-month plan to test them" | → | "And this is the intervention question" |
| Trajectory | "100 participants over 60 days" | → | "That's how I work" |
| Close | "how each person is wired?" | → | [silence — end] |

Every exit line is the entrance to the next section. No dead ends.

---

## Live Links to Share

- **Q22 (live project links):** https://dyadicmentalising.streamlit.app/
- **Portfolio:** https://snehalnair.github.io/portfolio/portfolio-2/

---

## What NOT to Do

- Don't describe the architecture diagram — narrate the story (fail → fix → lesson)
- Don't show all Streamlit tabs — the two-tab contrast is the demo
- Don't read text off the screen — narrate what the viewer sees
- Don't mention "product" or "startup" — this is a science demo
- Don't demo the browser extension — it doesn't exist yet
- Don't show the JS-divergence formula — say the name, let the visual carry meaning
- Don't rush the gap score moment — the 4-second silence is the most powerful beat
- Don't say "neurodivergent dyads" — say "interindividual differences" or "trait profiles"
- Don't say "clinical populations" — it's general population via Prolific
- Don't say "Sériès" with wrong accent — it's "Seriès" (accent on second e only)
- Don't say "theta-band" alone — say "predictive coding markers" if EEG comes up
- Don't end with a feature list — end with the question

---

## Practice Protocol

1. Read the full script aloud once — should land around 2:20–2:30
2. Check every transition: does the last sentence of each section pull you into the next?
3. Record a test take — play back, check audio, tab switches, and pacing
4. The gap score silence: click Tab B, count "one-Mississippi, two-Mississippi, three-Mississippi, four-Mississippi" before speaking
5. The close: practise holding eye contact for 2 full seconds after the final question
6. Record final take at 85% speed — the 32s buffer absorbs nerves
7. Watch playback — verify total is under 2:50
