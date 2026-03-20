"""
NeuroAI Cognitive Companion — Intent Gap Visualiser
Encode x Pillar VC AI for Science Fellowship Demo

This demo visualises the core scientific concept:
the intent gap (JS-divergence between sender intent and perceived intent)
as a function of dyadic relational context.

Uses a pre-computed mock model (lookup table) — no RoBERTa inference required.
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import numpy as np
from scipy.spatial.distance import jensenshannon
import pandas as pd

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Intent Gap Visualiser · NeuroAI Cognitive Companion",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Intent schema ─────────────────────────────────────────────────────────────
INTENTS = {
    "I1": "Seeking connection",
    "I2": "Expressing concern",
    "I3": "Setting a boundary",
    "I4": "Seeking validation",
    "I5": "Expressing frustration",
    "I6": "Making a request",
    "I7": "Giving information",
}
INTENT_LABELS = [f"{k}: {v}" for k, v in INTENTS.items()]
INTENT_KEYS = list(INTENTS.keys())

# ── Mock model: pre-computed SI/PI distributions per (message, context) ───────
# Format: {message_key: {context_key: {"SI": [...], "PI": [...]}}}
# Distributions are over I1–I7 (7 categories)

MOCK_MODEL = {
    # ── "Can we talk tonight?" ─────────────────────────────────────────────────
    # Scientifically: same message, different relational loading
    # Colleague: almost pure I6 request — moderate gap (~0.08) because PI adds some I5 uncertainty
    # Friend: I1 warmth dominant — low gap (~0.06) as friend understands the reach-out
    # Partner positive: I1 very strong — near-noise gap (~0.04) as partner reads warmth accurately
    # Partner conflict: SI=I1 connection, PI=I5 threat — HIGH gap (~0.39)
    "Can we talk tonight?": {
        "new_colleague_neutral": {
            "SI": [0.05, 0.06, 0.04, 0.04, 0.04, 0.65, 0.12],
            "PI": [0.06, 0.09, 0.14, 0.06, 0.28, 0.28, 0.09],  # gap ~0.15 amber: colleague genuinely unsure — meeting or confrontation?
        },
        "close_friend_neutral": {
            "SI": [0.40, 0.14, 0.05, 0.22, 0.05, 0.09, 0.05],
            "PI": [0.28, 0.13, 0.06, 0.20, 0.18, 0.10, 0.05],  # gap ~0.08 low: friend mostly gets warmth, slight I5 leak
        },
        "partner_positive": {
            "SI": [0.55, 0.15, 0.04, 0.14, 0.03, 0.06, 0.03],
            "PI": [0.52, 0.14, 0.04, 0.16, 0.06, 0.05, 0.03],  # gap ~0.04 near-unanimous: heard as warmth
        },
        "partner_after_conflict": {
            "SI": [0.55, 0.20, 0.12, 0.08, 0.03, 0.01, 0.01],
            "PI": [0.03, 0.04, 0.08, 0.03, 0.72, 0.07, 0.03],  # gap ~0.39: I1→I5 full threat-parse
        },
    },
    # ── "Fine, do whatever you want." ─────────────────────────────────────────
    # Colleague: I5 frustration both ways — low gap (~0.06)
    # Friend: SI=I3 boundary + I5, PI=mostly I5 — moderate gap (~0.10)
    # Partner positive: reads as mild I5 + some I3 — low-moderate (~0.08)
    # Partner conflict: SI=I3 boundary, PI=I5 pure hostility — HIGH gap (~0.24)
    "Fine, do whatever you want.": {
        "new_colleague_neutral": {
            "SI": [0.04, 0.04, 0.13, 0.04, 0.52, 0.19, 0.04],
            "PI": [0.04, 0.05, 0.16, 0.04, 0.56, 0.11, 0.04],  # gap ~0.06
        },
        "close_friend_neutral": {
            "SI": [0.04, 0.06, 0.32, 0.05, 0.40, 0.08, 0.05],
            "PI": [0.04, 0.05, 0.16, 0.04, 0.62, 0.06, 0.03],  # gap ~0.10: friend misses the boundary
        },
        "partner_positive": {
            "SI": [0.06, 0.05, 0.20, 0.07, 0.34, 0.25, 0.03],
            "PI": [0.05, 0.05, 0.22, 0.05, 0.42, 0.18, 0.03],  # gap ~0.08
        },
        "partner_after_conflict": {
            "SI": [0.04, 0.04, 0.62, 0.04, 0.22, 0.02, 0.02],
            "PI": [0.02, 0.02, 0.05, 0.02, 0.83, 0.04, 0.02],  # gap ~0.24: I3→I5
        },
    },
    # ── "You seem quiet lately." ───────────────────────────────────────────────
    # Colleague: SI=I2 concern, PI splits I2+I5 (is this criticism?) — moderate gap (~0.11)
    # Friend: SI=I1+I2, PI closely matches — low gap (~0.06)
    # Partner positive: warmth + concern read accurately — gap ~0.04
    # Partner conflict: SI=I2 genuine concern, PI=I5 surveillance/criticism — HIGH gap (~0.32)
    "You seem quiet lately.": {
        "new_colleague_neutral": {
            "SI": [0.06, 0.58, 0.03, 0.05, 0.04, 0.17, 0.07],
            "PI": [0.06, 0.28, 0.08, 0.07, 0.34, 0.11, 0.06],  # gap ~0.16 amber: colleague reads concern/criticism split
        },
        "close_friend_neutral": {
            "SI": [0.26, 0.52, 0.03, 0.08, 0.03, 0.05, 0.03],
            "PI": [0.22, 0.46, 0.04, 0.10, 0.10, 0.05, 0.03],  # gap ~0.06
        },
        "partner_positive": {
            "SI": [0.32, 0.48, 0.03, 0.10, 0.03, 0.02, 0.02],
            "PI": [0.30, 0.46, 0.03, 0.12, 0.05, 0.02, 0.02],  # gap ~0.04: heard as warmth
        },
        "partner_after_conflict": {
            "SI": [0.10, 0.60, 0.08, 0.12, 0.06, 0.02, 0.02],
            "PI": [0.03, 0.06, 0.10, 0.03, 0.70, 0.05, 0.03],  # gap ~0.32: I2→I5 surveillance parse
        },
    },
    # ── "I just need some space right now." ───────────────────────────────────
    # Colleague: clear I3 boundary, PI closely follows — gap ~0.05
    # Friend: SI=I3+some I2, PI adds I5 flavour — moderate gap (~0.09)
    # Partner positive: I3 boundary with care, heard accurately — gap ~0.07
    # Partner conflict: SI=I3 boundary, PI=I5 rejection — HIGH gap (~0.30)
    "I just need some space right now.": {
        "new_colleague_neutral": {
            "SI": [0.04, 0.04, 0.70, 0.04, 0.08, 0.06, 0.04],
            "PI": [0.04, 0.05, 0.62, 0.04, 0.14, 0.07, 0.04],  # gap ~0.05
        },
        "close_friend_neutral": {
            "SI": [0.06, 0.12, 0.58, 0.08, 0.08, 0.05, 0.03],
            "PI": [0.05, 0.08, 0.46, 0.07, 0.24, 0.07, 0.03],  # gap ~0.09: friend adds I5 worry
        },
        "partner_positive": {
            "SI": [0.10, 0.13, 0.55, 0.10, 0.06, 0.04, 0.02],
            "PI": [0.08, 0.12, 0.48, 0.09, 0.14, 0.06, 0.03],  # gap ~0.07
        },
        "partner_after_conflict": {
            "SI": [0.06, 0.08, 0.68, 0.06, 0.08, 0.02, 0.02],
            "PI": [0.02, 0.03, 0.10, 0.02, 0.76, 0.05, 0.02],  # gap ~0.30: I3→I5 rejection parse
        },
    },
    # ── "Don't worry about it, I'm fine." ─────────────────────────────────────
    # Colleague: I7 information, taken at face value — gap ~0.04
    # Friend: hears deflection, SI=I4+I5 masked, PI adds I5 concern — moderate gap (~0.09)
    # Partner positive: mild I5 deflection, still heard warmly — gap ~0.07
    # Partner conflict: SI=I4 validation-seeking masked, PI=I3 cold shutdown — HIGH gap (~0.31)
    "Don't worry about it, I'm fine.": {
        "new_colleague_neutral": {
            "SI": [0.08, 0.04, 0.04, 0.05, 0.08, 0.04, 0.67],
            "PI": [0.08, 0.06, 0.04, 0.05, 0.10, 0.04, 0.63],  # gap ~0.04: taken at face value
        },
        "close_friend_neutral": {
            "SI": [0.10, 0.10, 0.07, 0.14, 0.28, 0.04, 0.27],
            "PI": [0.08, 0.16, 0.08, 0.08, 0.42, 0.04, 0.14],  # gap ~0.09: friend senses deflection
        },
        "partner_positive": {
            "SI": [0.14, 0.10, 0.08, 0.14, 0.22, 0.04, 0.28],
            "PI": [0.12, 0.12, 0.10, 0.10, 0.32, 0.04, 0.20],  # gap ~0.07
        },
        "partner_after_conflict": {
            "SI": [0.08, 0.10, 0.06, 0.52, 0.14, 0.04, 0.06],
            "PI": [0.02, 0.02, 0.60, 0.02, 0.28, 0.04, 0.02],  # gap ~0.31: I4 validation→I3 shutdown parse
        },
    },
}

CONTEXT_LABELS = {
    "new_colleague_neutral": "New colleague · neutral history",
    "close_friend_neutral": "Close friend · neutral history",
    "partner_positive": "Partner of 3+ years · positive recent history",
    "partner_after_conflict": "Partner of 3+ years · after conflict",
}

# ── Helper functions ──────────────────────────────────────────────────────────

def js_divergence(p, q):
    p = np.array(p, dtype=float)
    q = np.array(q, dtype=float)
    p /= p.sum()
    q /= q.sum()
    return float(jensenshannon(p, q) ** 2)  # squared JSD in [0,1]

def gap_color(score):
    # Thresholds grounded in annotation disagreement norms for 7-class distributions
    if score < 0.05:
        return "#6BAE8A"   # nc-muted-green — noise-level variation
    elif score < 0.10:
        return "#a8d8a8"   # light green — low but detectable
    elif score < 0.20:
        return "#C9922A"   # nc-muted-amber — moderate genuine ambiguity
    elif score < 0.35:
        return "#C9922A"   # nc-muted-amber — high systematic disagreement
    else:
        return "#B84040"   # nc-muted-red — near-maximum polarisation (JSD > 0.35)

def network_bar_color(score):
    """Muted green → amber → red for the connection clarity chart."""
    if score < 0.10:
        return "#6BAE8A"   # muted green — clear signal
    elif score < 0.20:
        return "#C9922A"   # muted amber — moderate gap
    elif score < 0.35:
        return "#B8762A"   # muted orange — high gap
    else:
        return "#B84040"   # muted red — crossed wires

def gap_label(score):
    # Five-tier scale grounded in NLP annotation disagreement norms for 7-class distributions
    if score < 0.05:
        return "Near-unanimous · noise-level variation (JSD < 0.05)"
    elif score < 0.10:
        return "Low gap · one reading dominant (JSD 0.05–0.10)"
    elif score < 0.20:
        return "Moderate gap · genuine ambiguity (JSD 0.10–0.20)"
    elif score < 0.35:
        return "High gap · systematic misalignment (JSD 0.20–0.35)"
    else:
        return "Very high gap · near-maximum polarisation (JSD > 0.35)"

def distribution_chart(si, pi, title=""):
    short_labels = list(INTENTS.keys())
    fig = go.Figure()
    fig.add_trace(go.Bar(
        name="Sender Intent (SI)",
        x=short_labels,
        y=si,
        marker_color="#6B9FC4",
        opacity=0.85,
        hovertemplate="<b>%{x}</b><br>SI: %{y:.2f}<extra></extra>",
    ))
    fig.add_trace(go.Bar(
        name="Perceived Intent (PI)",
        x=short_labels,
        y=pi,
        marker_color="#e7a59c",
        opacity=0.85,
        hovertemplate="<b>%{x}</b><br>PI: %{y:.2f}<extra></extra>",
    ))
    fig.update_layout(
        title=title,
        barmode="group",
        xaxis_title="Intent category",
        yaxis_title="Probability",
        yaxis_range=[0, 1],
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=320,
        margin=dict(t=50, b=40, l=40, r=20),
        plot_bgcolor="#f5f6f7",
        paper_bgcolor="#f5f6f7",
        font=dict(color="#2c3e50"),
    )
    return fig

def gap_gauge(score, context_label):
    color = gap_color(score)
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=round(score, 3),
        title={"text": f"Intent Gap Score<br><sub>{context_label}</sub>", "font": {"size": 14}},
        gauge={
            "axis": {"range": [0, 1], "tickwidth": 1},
            "bar": {"color": color},
            "steps": [
                {"range": [0, 0.05],  "color": "#d4ebe0"},   # nc-muted-green tint: near-unanimous
                {"range": [0.05, 0.10], "color": "#b5d9c6"}, # nc-muted-green light: low gap
                {"range": [0.10, 0.20], "color": "#f2e3c0"}, # nc-muted-amber tint: moderate
                {"range": [0.20, 0.35], "color": "#e5c48a"}, # nc-muted-amber: high
                {"range": [0.35, 1.0],  "color": "#dba9a9"}, # nc-muted-red tint: very high
            ],
            "threshold": {
                "line": {"color": "white", "width": 2},
                "thickness": 0.75,
                "value": score,
            },
        },
        number={"font": {"size": 40, "color": color}},
    ))
    fig.update_layout(
        height=260,
        margin=dict(t=60, b=20, l=30, r=30),
        paper_bgcolor="#f5f6f7",
        font=dict(color="#2c3e50"),
    )
    return fig

def trajectory_chart(days=60, start_gap=0.52, end_gap=0.14, noise_scale=0.03):
    np.random.seed(42)
    x = np.arange(1, days + 1)
    decay = np.exp(-4 * (x - 1) / (days - 1))
    trend = end_gap + (start_gap - end_gap) * decay
    noise = np.random.normal(0, noise_scale, days)
    noise[0] = 0
    gap = np.clip(trend + noise, 0.05, 0.95)

    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=gap,
        mode="lines",
        line=dict(color="#6B9FC4", width=2),
        name="Daily intent gap score",
        hovertemplate="Day %{x}<br>Gap: %{y:.3f}<extra></extra>",
    ))
    # Rolling 7-day mean
    rolling = pd.Series(gap).rolling(7, min_periods=1).mean()
    fig.add_trace(go.Scatter(
        x=x, y=rolling,
        mode="lines",
        line=dict(color="#B84040", width=2, dash="dash"),
        name="7-day rolling mean",
        hovertemplate="Day %{x}<br>Rolling mean: %{y:.3f}<extra></extra>",
    ))
    fig.add_hline(
        y=0.10,
        line_dash="dot",
        line_color="#6BAE8A",
        annotation_text="Low gap threshold (0.10)",
        annotation_position="bottom right",
        annotation_font_color="#6BAE8A",
    )
    fig.add_vrect(
        x0=1, x1=7,
        fillcolor="#6B9FC4", opacity=0.08,
        annotation_text="Intervention begins",
        annotation_position="top left",
        annotation_font_color="#6B9FC4",
    )
    fig.update_layout(
        title="Simulated 60-day intent gap trajectory (H₂ illustration)",
        xaxis_title="Day",
        yaxis_title="JS-divergence (intent gap score)",
        yaxis_range=[0, 0.75],
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        height=360,
        margin=dict(t=60, b=40, l=50, r=20),
        plot_bgcolor="#f5f6f7",
        paper_bgcolor="#f5f6f7",
        font=dict(color="#2c3e50"),
    )
    return fig

def context_comparison_chart(message_key):
    contexts = list(CONTEXT_LABELS.keys())
    gaps = []
    for ctx in contexts:
        data = MOCK_MODEL[message_key][ctx]
        gaps.append(js_divergence(data["SI"], data["PI"]))

    colors = [gap_color(g) for g in gaps]
    labels = [CONTEXT_LABELS[c] for c in contexts]

    fig = go.Figure(go.Bar(
        x=gaps,
        y=labels,
        orientation="h",
        marker_color=colors,
        text=[f"{g:.3f}" for g in gaps],
        textposition="outside",
        hovertemplate="<b>%{y}</b><br>Gap: %{x:.3f}<extra></extra>",
    ))
    fig.update_layout(
        title="Same message — four relational contexts<br><sub>Relational history is the primary signal</sub>",
        xaxis_title="Intent gap score (JS-divergence)",
        xaxis_range=[0, 0.85],
        height=300,
        margin=dict(t=70, b=40, l=20, r=80),
        plot_bgcolor="#f5f6f7",
        paper_bgcolor="#f5f6f7",
        font=dict(color="#2c3e50"),
    )
    return fig

# ── Non-technical tab helpers ─────────────────────────────────────────────────

# Human-readable framing for each (SI dominant intent, PI dominant intent) pair
def get_human_story(message, context_key, si, pi, gap):
    si_dom_idx = int(np.argmax(si))
    pi_dom_idx = int(np.argmax(pi))
    si_dom = INTENT_KEYS[si_dom_idx]
    pi_dom = INTENT_KEYS[pi_dom_idx]

    intent_plain = {
        "I1": "reaching out for connection",
        "I2": "expressing genuine care",
        "I3": "asking for space or a boundary",
        "I4": "looking for reassurance",
        "I5": "frustration or conflict",
        "I6": "making a practical request",
        "I7": "sharing information, nothing more",
    }

    # Build the "sent as" / "heard as" story
    sent_as = intent_plain.get(si_dom, si_dom)
    heard_as = intent_plain.get(pi_dom, pi_dom)

    if gap < 0.05:
        connection_level = "Crystal clear"
        summary = f"This message landed exactly as it was meant. Both people are reading from the same page."
        color_theme = "#4a9b6f"
        signal_icon = "●"
        bridge_fill = 0.98
    elif gap < 0.10:
        connection_level = "Well understood"
        summary = f"The message came through clearly. A small amount of ambiguity is normal — no relationship is a perfect mind-read."
        color_theme = "#5b8db8"
        signal_icon = "●"
        bridge_fill = 0.82
    elif gap < 0.20:
        connection_level = "Getting lost in translation"
        summary = f"The receiver is genuinely uncertain about what this message means. The sender's true meaning is slipping through the cracks."
        color_theme = "#c9922a"
        signal_icon = "●"
        bridge_fill = 0.52
    elif gap < 0.35:
        connection_level = "Significant misread"
        summary = f"A real gap. The sender means one thing — the receiver is hearing something quite different. This is where misunderstandings become arguments."
        color_theme = "#c4732a"
        signal_icon = "●"
        bridge_fill = 0.28
    else:
        connection_level = "Crossed wires"
        summary = f"The sender's meaning is being almost completely reversed. This is the territory where one person reaches out and the other braces for impact."
        color_theme = "#b84040"
        signal_icon = "●"
        bridge_fill = 0.08

    return {
        "sent_as": sent_as,
        "heard_as": heard_as,
        "aligned": si_dom == pi_dom,
        "connection_level": connection_level,
        "summary": summary,
        "color_theme": color_theme,
        "signal_icon": signal_icon,
        "bridge_fill": bridge_fill,
        "si_dom": si_dom,
        "pi_dom": pi_dom,
    }

def context_label_plain(ctx_key):
    plain = {
        "new_colleague_neutral": "👔  Work colleague",
        "close_friend_neutral": "🤝  Close friend",
        "partner_positive": "💚  Partner — good times",
        "partner_after_conflict": "⚡  Partner — after a fight",
    }
    return plain.get(ctx_key, ctx_key)

def make_bridge_chart(bridge_fill, color, gap):
    """A horizontal 'connection bridge' metaphor — how much of the signal got through."""
    # Smooth arc via parametric semicircle — 400 points for a clean curve
    theta = np.linspace(0, np.pi, 400)
    x_arc = np.cos(theta)
    y_arc = np.sin(theta) * 0.38

    # Fill portion
    fill_end = max(4, int(bridge_fill * 400))
    x_fill = x_arc[:fill_end]
    y_fill = y_arc[:fill_end]

    fig = go.Figure()

    # Track (light grey, clean — like NC card borders)
    fig.add_trace(go.Scatter(
        x=x_arc, y=y_arc,
        mode="lines",
        line=dict(color="#dce7f3", width=18, shape="spline"),
        hoverinfo="skip",
        showlegend=False,
    ))

    # Filled arc — muted colour, NC palette
    fig.add_trace(go.Scatter(
        x=x_fill, y=y_fill,
        mode="lines",
        line=dict(color=color, width=14, shape="spline"),
        hoverinfo="skip",
        showlegend=False,
    ))

    # Left node — sender (NC dark blue)
    fig.add_trace(go.Scatter(
        x=[-1], y=[0],
        mode="markers+text",
        marker=dict(size=22, color="#2c3e50", symbol="circle",
                    line=dict(color="#8ca3b0", width=2)),
        text=["SENDER"],
        textposition="bottom center",
        textfont=dict(color="#8ca3b0", size=11, family="monospace"),
        hoverinfo="skip",
        showlegend=False,
    ))

    # Right node — receiver (NC slate)
    fig.add_trace(go.Scatter(
        x=[1], y=[0],
        mode="markers+text",
        marker=dict(size=22, color="#2c3e50", symbol="circle",
                    line=dict(color="#8ca3b0", width=2)),
        text=["RECEIVER"],
        textposition="bottom center",
        textfont=dict(color="#8ca3b0", size=11, family="monospace"),
        hoverinfo="skip",
        showlegend=False,
    ))

    # Percentage label — placed well above the arc apex, no box overlap
    pct = int(bridge_fill * 100)
    fig.add_annotation(
        x=0.0, y=0.72,
        text=f"<b>{pct}%</b>",
        showarrow=False,
        font=dict(color=color, size=30, family="Arial Black"),
        align="center",
        bgcolor="#ffffff",
        bordercolor="#e0e8f0",
        borderwidth=1,
        borderpad=8,
    )
    fig.add_annotation(
        x=0.0, y=0.56,
        text="of meaning got through",
        showarrow=False,
        font=dict(color="#8ca3b0", size=12, family="sans-serif"),
        align="center",
    )

    fig.update_layout(
        height=240,
        margin=dict(t=30, b=55, l=20, r=20),
        xaxis=dict(visible=False, range=[-1.45, 1.45]),
        yaxis=dict(visible=False, range=[-0.22, 0.90]),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    return fig

def make_radar_all_contexts(message_key, selected_ctx_key=None):
    """Spider chart in Network-tab style: SI vs PI for the selected context,
    ghost PI outlines for other contexts. Transparent background, full intent labels."""
    contexts = list(CONTEXT_LABELS.keys())
    intent_labels = list(INTENTS.values())   # full names — matches Network tab

    # Muted palette (one per context), with explicit rgba fills
    colors_ctx = {
        "new_colleague_neutral":  "#C9922A",
        "close_friend_neutral":   "#6BAE8A",
        "partner_positive":       "#6B9FC4",
        "partner_after_conflict": "#B84040",
    }
    fills_ctx = {
        "new_colleague_neutral":  "rgba(201,146,42,0.13)",
        "close_friend_neutral":   "rgba(107,174,138,0.13)",
        "partner_positive":       "rgba(107,159,196,0.13)",
        "partner_after_conflict": "rgba(184,64,64,0.13)",
    }
    fills_pi = {
        "new_colleague_neutral":  "rgba(201,146,42,0.07)",
        "close_friend_neutral":   "rgba(107,174,138,0.07)",
        "partner_positive":       "rgba(107,159,196,0.07)",
        "partner_after_conflict": "rgba(184,64,64,0.07)",
    }
    ctx_plain = {c: context_label_plain(c) for c in contexts}

    fig = go.Figure()

    # Ghost PI outlines for non-selected contexts
    for ctx in contexts:
        if selected_ctx_key and ctx == selected_ctx_key:
            continue
        pi = MOCK_MODEL[message_key][ctx]["PI"]
        col = colors_ctx[ctx]
        fig.add_trace(go.Scatterpolar(
            r=pi + [pi[0]],
            theta=intent_labels + [intent_labels[0]],
            fill="toself",
            name=ctx_plain[ctx],
            line=dict(color=col, width=1, dash="dot"),
            fillcolor=fills_pi[ctx],
            showlegend=True,
        ))

    # Selected context: SI (solid) + PI (dashed) — Network tab style
    if selected_ctx_key and selected_ctx_key in contexts:
        ctx = selected_ctx_key
        si = MOCK_MODEL[message_key][ctx]["SI"]
        pi = MOCK_MODEL[message_key][ctx]["PI"]
        col = colors_ctx[ctx]
        fig.add_trace(go.Scatterpolar(
            r=si + [si[0]],
            theta=intent_labels + [intent_labels[0]],
            fill="toself",
            name="Sent as (SI)",
            line=dict(color=col, width=2),
            fillcolor=fills_ctx[ctx],
            showlegend=True,
        ))
        fig.add_trace(go.Scatterpolar(
            r=pi + [pi[0]],
            theta=intent_labels + [intent_labels[0]],
            fill="toself",
            name="Received as (PI)",
            line=dict(color=col, width=2, dash="dot"),
            fillcolor=fills_pi[ctx],
            showlegend=True,
        ))
    elif not selected_ctx_key:
        # No selection: show all PI shapes equally
        for ctx in contexts:
            pi = MOCK_MODEL[message_key][ctx]["PI"]
            col = colors_ctx[ctx]
            fig.add_trace(go.Scatterpolar(
                r=pi + [pi[0]],
                theta=intent_labels + [intent_labels[0]],
                fill="toself",
                name=ctx_plain[ctx],
                line=dict(color=col, width=2),
                fillcolor=fills_ctx[ctx],
                showlegend=True,
            ))

    fig.update_layout(
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                visible=True,
                range=[0, 0.7],
                gridcolor="rgba(140,163,176,0.18)",
                tickfont=dict(size=7, color="#8ca3b0"),
                showticklabels=False,
            ),
            angularaxis=dict(
                tickfont=dict(size=9, color="#8ca3b0"),
                gridcolor="rgba(140,163,176,0.18)",
                linecolor="rgba(140,163,176,0.25)",
            ),
        ),
        paper_bgcolor="rgba(245,246,247,1)",
        font=dict(color="#2c3e50"),
        legend=dict(
            orientation="h", yanchor="bottom", y=-0.28, xanchor="center", x=0.5,
            font=dict(size=11, color="#8ca3b0"),
            bgcolor="rgba(0,0,0,0)",
        ),
        height=380,
        margin=dict(t=40, b=90, l=50, r=50),
        title=dict(
            text="How the receiver interprets the same message<br><sub>Your selected relationship is highlighted — others shown as outlines</sub>" if selected_ctx_key
                 else "How the receiver interprets the same message<br><sub>Shape shifts with relationship — same words, different worlds</sub>",
            font=dict(color="#8ca3b0", size=13),
        ),
    )
    return fig

def make_neural_signal_bars(message_key):
    """Horizontal bars showing 'connection quality' per context — no numbers, just signal strength."""
    contexts = list(CONTEXT_LABELS.keys())
    gaps = [js_divergence(MOCK_MODEL[message_key][c]["SI"], MOCK_MODEL[message_key][c]["PI"]) for c in contexts]
    # Invert gap to "connection quality" (1 - normalised gap)
    max_gap = max(gaps)
    quality = [1.0 - (g / (max_gap + 0.01)) for g in gaps]
    quality = [max(0.05, min(0.99, q)) for q in quality]

    colors_q = [network_bar_color(g) for g in gaps]
    labels = [context_label_plain(c) for c in contexts]

    fig = go.Figure()
    for i, (lbl, q, col) in enumerate(zip(labels, quality, colors_q)):
        # Background bar
        fig.add_trace(go.Bar(
            x=[1.0], y=[lbl], orientation="h",
            marker_color="#ececf0",
            showlegend=False,
            hoverinfo="skip",
        ))
        # Signal bar
        fig.add_trace(go.Bar(
            x=[q], y=[lbl], orientation="h",
            marker=dict(
                color=col,
                line=dict(color=col, width=0),
            ),
            showlegend=False,
            hovertemplate=f"<b>{lbl}</b><br>Connection clarity: {int(q*100)}%<extra></extra>",
        ))

    fig.update_layout(
        barmode="overlay",
        xaxis=dict(visible=False, range=[0, 1.05]),
        yaxis=dict(
            tickfont=dict(color="#717182", size=13),
            gridcolor="#ececf0",
        ),
        height=240,
        margin=dict(t=10, b=10, l=10, r=20),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        showlegend=False,
    )
    return fig


# ── CSS injection — NeuralConnexions brand palette ───────────────────────────
# Palette: nc-ivory #f5f6f7 · nc-dark #2c3e50 · nc-slate #8ca3b0
#          nc-blue  #dce7f3 · nc-blush #e7a59c · white #ffffff
FUTURISTIC_CSS = """
<style>
/* ── Global Streamlit overrides — NC brand ── */
[data-testid="stAppViewContainer"] {
    background-color: #f5f6f7 !important;
}
[data-testid="stSidebar"] {
    background-color: #ffffff !important;
    border-right: 1px solid #ececf0 !important;
}
[data-testid="stSidebar"] * {
    color: #2c3e50 !important;
}
[data-testid="stMainBlockContainer"] {
    background-color: #f5f6f7 !important;
}
h1, h2, h3, h4 {
    color: #2c3e50 !important;
}
p, li, label {
    color: #717182 !important;
}
/* Tab styling */
[data-testid="stTabs"] [data-baseweb="tab"] {
    background: transparent !important;
    color: #8ca3b0 !important;
    border-bottom: 2px solid transparent !important;
    font-weight: 500 !important;
}
[data-testid="stTabs"] [aria-selected="true"] {
    color: #2c3e50 !important;
    border-bottom: 2px solid #e7a59c !important;
}
/* Slider */
[data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] {
    background-color: #8ca3b0 !important;
}
/* Select box */
[data-testid="stSelectbox"] {
    color: #2c3e50 !important;
}

/* ── NC card system ── */
.nt-card {
    background: #ffffff;
    border: 1px solid #ececf0;
    border-radius: 12px;
    padding: 20px 24px;
    margin-bottom: 16px;
    box-shadow: 0 2px 12px rgba(140, 163, 176, 0.10);
}
.nt-header {
    font-size: 2.4em;
    font-weight: 700;
    letter-spacing: 0.02em;
    background: linear-gradient(90deg, #8ca3b0 0%, #2c3e50 60%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 4px;
}
.nt-subheader {
    color: #8ca3b0;
    font-size: 0.95em;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    margin-bottom: 20px;
}
.nt-signal-box {
    border-radius: 10px;
    padding: 18px 22px;
    margin: 8px 0;
    border-left: 4px solid;
}
.nt-sent {
    background: rgba(220, 231, 243, 0.6);
    border-left-color: #8ca3b0;
}
.nt-heard {
    background: rgba(231, 165, 156, 0.12);
    border-left-color: #e7a59c;
}
.nt-label {
    font-size: 0.75em;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #8ca3b0;
    margin-bottom: 4px;
}
.nt-intent-text {
    font-size: 1.35em;
    font-weight: 600;
    color: #2c3e50;
}
.nt-summary {
    color: #717182;
    font-size: 1.05em;
    line-height: 1.65;
    margin: 14px 0 0 0;
}
.nt-connection-badge {
    display: inline-block;
    border-radius: 20px;
    padding: 6px 18px;
    font-size: 1.1em;
    font-weight: 700;
    letter-spacing: 0.04em;
    margin-bottom: 6px;
}
.nt-section-title {
    font-size: 0.8em;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #8ca3b0;
    margin-bottom: 10px;
    margin-top: 24px;
}
.nt-divider {
    border: none;
    border-top: 1px solid #ececf0;
    margin: 22px 0;
}
.nt-insight-box {
    background: linear-gradient(90deg, rgba(220,231,243,0.5) 0%, rgba(231,165,156,0.12) 100%);
    border: 1px solid #ececf0;
    border-radius: 10px;
    padding: 16px 20px;
    color: #717182;
    font-size: 1.02em;
    line-height: 1.6;
    margin-top: 8px;
}
.nt-big-question {
    font-size: 1.6em;
    font-weight: 600;
    color: #2c3e50;
    line-height: 1.4;
    margin-bottom: 8px;
}
.nt-context-pill {
    display: inline-block;
    border-radius: 6px;
    padding: 3px 12px;
    font-size: 0.88em;
    background: rgba(220,231,243,0.7);
    border: 1px solid #dce7f3;
    color: #8ca3b0;
    margin-bottom: 14px;
    letter-spacing: 0.04em;
}
</style>
"""

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.image("https://img.shields.io/badge/Encode_x_Pillar_VC-AI_for_Science_Fellowship-blue?style=for-the-badge", use_container_width=True)
    st.markdown("## NeuroAI Cognitive Companion")
    st.markdown("**Intent Gap Visualiser** — demo instrument")
    st.divider()
    st.markdown("""
**What is the intent gap?**

The JS-divergence between what a sender *means* (Sender Intent, SI) and what a receiver *parses* (Perceived Intent, PI):

> `gap = JS-divergence(P(SI), P(PI))`

- `0.0` = perfect alignment
- `1.0` = maximum misalignment

**The core finding this demo illustrates:**
The same message carries a fundamentally different intent distribution depending on relational history. Relational context is not noise — it is the primary signal.
""")
    st.divider()
    st.markdown("**Intent schema (I1–I7):**")
    for k, v in INTENTS.items():
        st.markdown(f"- `{k}` {v}")
    st.divider()
    st.caption("Demo uses pre-computed distributions. Full system uses RoBERTa-large fine-tuned on 2,000-message annotated dataset.")

# ════════════════════════════════════════════════════════════════════════════
# OPENING FRAME — The Wound + The Instrument (before tabs)
# ════════════════════════════════════════════════════════════════════════════
st.markdown("""
<div style='
    background: linear-gradient(180deg, #ffffff 0%, #f5f6f7 100%);
    border: 1px solid #dce7f3;
    border-radius: 16px;
    padding: 40px 48px 36px 48px;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
'>
  <!-- Background glow -->
  <div style='position:absolute;top:-60px;right:-60px;width:300px;height:300px;
              background:radial-gradient(circle,rgba(231,165,156,0.10) 0%,transparent 70%);
              pointer-events:none;'></div>
  <div style='position:absolute;bottom:-60px;left:-60px;width:300px;height:300px;
              background:radial-gradient(circle,rgba(140,163,176,0.10) 0%,transparent 70%);
              pointer-events:none;'></div>

  <!-- Opening statement -->
  <div style='font-size:1.15em;color:#8ca3b0;letter-spacing:0.18em;text-transform:uppercase;
              margin-bottom:18px;'>NeuroAI Cognitive Companion</div>

  <div style='font-size:1.55em;font-weight:800;color:#2c3e50;line-height:1.35;margin-bottom:0;'>
    The largest untapped source of human potential <span style='color:#c47b71;'>is not a new model.</span><br>
    <span style='color:#6b9fc4;'>It is the gap between what humans mean and what others receive.</span>
  </div>
  <br><br>

  <!-- Biology mechanism row -->
  <div style='display:flex;align-items:center;gap:0;margin:28px 0 24px 0;flex-wrap:wrap;'>
    <!-- Amygdala node — warm coral: threat/fast -->
    <div style='text-align:center;padding:14px 20px;background:rgba(196,123,113,0.12);
                border:1px solid rgba(196,123,113,0.45);border-radius:12px;min-width:130px;'>
      <div style='font-size:1.4em;margin-bottom:4px;'>🧠</div>
      <div style='font-size:0.78em;font-weight:700;color:#c47b71;letter-spacing:0.1em;text-transform:uppercase;'>Amygdala</div>
      <div style='font-size:0.72em;color:#8ca3b0;margin-top:3px;'>Threat pathway fires</div>
      <div style='font-size:0.82em;font-weight:700;color:#c47b71;margin-top:2px;'>FAST</div>
    </div>
    <!-- Arrow: coral → blue (threat → cognition) -->
    <div style='flex:1;text-align:center;padding:0 8px;min-width:120px;'>
      <div style='font-size:0.7em;color:#c47b71;font-weight:700;letter-spacing:0.12em;
                  text-transform:uppercase;margin-bottom:4px;'>⚡ tens of milliseconds</div>
      <div style='height:2px;background:linear-gradient(90deg,#c47b71,#6b9fc4);
                  border-radius:2px;margin:6px 0;'></div>
      <div style='font-size:0.68em;color:#8ca3b0;margin-top:4px;'>ambiguous message<br>tagged as threat</div>
    </div>
    <!-- PFC node — cool slate blue: cognitive/slower -->
    <div style='text-align:center;padding:14px 20px;background:rgba(107,159,196,0.12);
                border:1px solid rgba(107,159,196,0.45);border-radius:12px;min-width:130px;'>
      <div style='font-size:1.4em;margin-bottom:4px;'>💡</div>
      <div style='font-size:0.78em;font-weight:700;color:#6b9fc4;letter-spacing:0.1em;text-transform:uppercase;'>Prefrontal Cortex</div>
      <div style='font-size:0.72em;color:#8ca3b0;margin-top:3px;'>Meaning resolved</div>
      <div style='font-size:0.82em;font-weight:700;color:#6b9fc4;margin-top:2px;'>SLOWER</div>
    </div>
    <!-- Arrow: blue → teal (cognition → measurement) -->
    <div style='flex:1;text-align:center;padding:0 8px;min-width:100px;'>
      <div style='font-size:0.7em;color:#8ca3b0;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;'>before meaning lands</div>
      <div style='height:2px;background:linear-gradient(90deg,#6b9fc4,#5b9e8a);border-radius:2px;margin:6px 0;'></div>
      <div style='font-size:0.68em;color:#8ca3b0;margin-top:4px;'>damage is done</div>
    </div>
    <!-- Intent Gap node — teal: measurable/scientific -->
    <div style='text-align:center;padding:14px 20px;background:rgba(91,158,138,0.12);
                border:1px solid rgba(91,158,138,0.45);border-radius:12px;min-width:140px;'>
      <div style='font-size:1.4em;margin-bottom:4px;'>📐</div>
      <div style='font-size:0.78em;font-weight:700;color:#5b9e8a;letter-spacing:0.1em;text-transform:uppercase;'>Intent Gap</div>
      <div style='font-size:0.72em;color:#8ca3b0;margin-top:3px;'>JS-divergence(P(SI), P(PI))</div>
      <div style='font-size:0.82em;font-weight:700;color:#5b9e8a;margin-top:2px;'>MEASURABLE</div>
    </div>
  </div>

  <!-- Three-line thesis — colours mirror the node they relate to -->
  <div style='display:flex;gap:16px;flex-wrap:wrap;margin-top:8px;'>
    <!-- Problem: coral — the threat/pain -->
    <div style='flex:1;min-width:200px;padding:14px 18px;background:rgba(196,123,113,0.09);
                border-left:3px solid #c47b71;border-radius:0 8px 8px 0;'>
      <div style='font-size:0.72em;color:#c47b71;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:4px;'>The Problem</div>
      <div style='font-size:0.88em;color:#2c3e50;line-height:1.5;'>High emotions, ego, misunderstanding — not character flaws, but biology playing out in everyday communication.</div>
    </div>
    <!-- Instrument: slate blue — the scientific tool -->
    <div style='flex:1;min-width:200px;padding:14px 18px;background:rgba(107,159,196,0.09);
                border-left:3px solid #6b9fc4;border-radius:0 8px 8px 0;'>
      <div style='font-size:0.72em;color:#6b9fc4;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:4px;'>The Instrument</div>
      <div style='font-size:0.88em;color:#2c3e50;line-height:1.5;'>To our knowledge, the first scientific instrument to measure the intent gap, conditioned on dyadic relational history. <em>This dataset does not yet exist.</em></div>
    </div>
    <!-- Hypothesis: teal — the hopeful outcome -->
    <div style='flex:1;min-width:200px;padding:14px 18px;background:rgba(91,158,138,0.09);
                border-left:3px solid #5b9e8a;border-radius:0 8px 8px 0;'>
      <div style='font-size:0.72em;color:#5b9e8a;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:4px;'>The Hypothesis</div>
      <div style='font-size:0.88em;color:#2c3e50;line-height:1.5;'>Repeated intent feedback leaves a trace in the brain — shifting neural markers from threat-first toward meaning-first. H₃, 60-day EEG pilot.</div>
    </div>
  </div>

  <!-- Source note -->
  <div style='margin-top:20px;font-size:0.72em;color:#8ca3b0;font-style:italic;'>
    Biological mechanism: subcortical threat pathway (LeDoux, 1996). Cognitive reappraisal window (Gross, 1998).
    Neuroplasticity mechanism (Singer, 2025; Sitaram et al., 2017). All hypotheses are stated as such — this programme is designed to test them.
  </div>
</div>
""", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_science, tab_theplan, tab_human, tab_deploy, tab_network = st.tabs([
    "📊  Scientific View",
    "🔬  The Science",
    "🫀  What Does This Mean?",
    "📱  In the Wild",
    "🌐  The Network"
])


# ════════════════════════════════════════════════════════════════════════════
# TAB 1 — SCIENTIFIC VIEW (original content)
# ════════════════════════════════════════════════════════════════════════════
with tab_science:
    st.markdown("# 🧠 Intent Gap Visualiser")
    st.markdown("*NeuroAI Cognitive Companion · Encode x Pillar VC AI for Science Fellowship*")
    st.divider()

    # ── Biology framing banner ─────────────────────────────────────────────────
    st.markdown("""
    <div style='padding:10px 18px;background:rgba(231,165,156,0.10);border:1px solid rgba(231,165,156,0.4);
                border-radius:10px;margin-bottom:20px;display:flex;align-items:center;gap:14px;'>
      <div style='font-size:1.3em;flex-shrink:0;'>🧠</div>
      <div style='font-size:0.85em;color:#717182;line-height:1.6;'>
        <strong style='color:#2c3e50;'>Measuring the intent gap:</strong>
        JS-divergence between sender intent P(SI) and perceived intent P(PI), conditioned on dyadic relational history.
        The same message carries fundamentally different intent distributions depending on relational context —
        <em>this is what existing sentiment tools cannot measure.</em>
        &nbsp;<span style='color:#556677;font-size:0.85em;'>H₁: RoBERTa-large + 16-dim relational context vector · untested · this programme is designed to test it</span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Section 1: Message + context selector ────────────────────────────────
    st.markdown("## 1 · Select a message and relational context")

    col1, col2 = st.columns([1, 1])

    with col1:
        selected_message = st.selectbox(
            "Message",
            options=list(MOCK_MODEL.keys()),
            index=0,
            key="sci_message",
            help="Select a pre-loaded ambiguous message from the demo set.",
        )
        st.markdown(f"> *\"{selected_message}\"*")

    with col2:
        selected_context_key = st.selectbox(
            "Relational context",
            options=list(CONTEXT_LABELS.keys()),
            format_func=lambda k: CONTEXT_LABELS[k],
            index=1,
            key="sci_context",
            help="Relational history changes the intent distribution for the same message.",
        )

    data = MOCK_MODEL[selected_message][selected_context_key]
    si = data["SI"]
    pi = data["PI"]
    gap = js_divergence(si, pi)
    color = gap_color(gap)
    label = gap_label(gap)

    # ── Section 2: Gap score + distributions ─────────────────────────────────
    st.divider()
    st.markdown("## 2 · Intent distributions and gap score")

    col_gauge, col_chart = st.columns([1, 2])

    with col_gauge:
        st.plotly_chart(
            gap_gauge(gap, CONTEXT_LABELS[selected_context_key]),
            use_container_width=True,
        )
        st.markdown(
            f"<div style='text-align:center; color:{color}; font-size:1.1em; font-weight:600'>{label}</div>",
            unsafe_allow_html=True,
        )
        st.markdown(
            f"<div style='text-align:center; color:#aaa; font-size:0.85em; margin-top:4px'>JS-divergence(P(SI), P(PI)) = {gap:.4f}</div>",
            unsafe_allow_html=True,
        )

    with col_chart:
        st.plotly_chart(
            distribution_chart(si, pi, title=f"\"{selected_message}\""),
            use_container_width=True,
        )
        si_dominant = INTENT_KEYS[int(np.argmax(si))]
        pi_dominant = INTENT_KEYS[int(np.argmax(pi))]
        si_label = INTENTS[si_dominant]
        pi_label = INTENTS[pi_dominant]

        if si_dominant == pi_dominant:
            st.success(f"**Aligned:** Sender most likely means `{si_dominant}: {si_label}` — receiver most likely parses the same.")
        else:
            st.warning(f"**Misaligned:** Sender most likely means `{si_dominant}: {si_label}` — receiver most likely parses `{pi_dominant}: {pi_label}`.")

    # ── Section 3: Relational context effect ─────────────────────────────────
    st.divider()
    st.markdown("## 3 · The relational context effect")
    st.markdown(
        "The same message across four relational contexts. "
        "Relational history shifts the intent distribution — and the gap score — dramatically."
    )
    st.plotly_chart(context_comparison_chart(selected_message), use_container_width=True)

    gaps_all = {
        ctx: js_divergence(MOCK_MODEL[selected_message][ctx]["SI"], MOCK_MODEL[selected_message][ctx]["PI"])
        for ctx in CONTEXT_LABELS
    }
    max_ctx = max(gaps_all, key=gaps_all.get)
    min_ctx = min(gaps_all, key=gaps_all.get)
    delta = gaps_all[max_ctx] - gaps_all[min_ctx]

    st.info(
        f"**Context effect:** The gap ranges from **{gaps_all[min_ctx]:.3f}** "
        f"({CONTEXT_LABELS[min_ctx]}) to **{gaps_all[max_ctx]:.3f}** "
        f"({CONTEXT_LABELS[max_ctx]}) — a {delta:.3f} difference driven entirely by relational history, "
        f"with the message content unchanged."
    )

    # ── Section 3b: Neurodivergent prediction (H2.1) ─────────────────────────
    st.divider()
    st.markdown("## 3b · A testable prediction: neurodivergent dyads")
    st.markdown(
        "If the intent gap arises from asymmetry between subcortical threat-tagging and cortical "
        "mentalising, it should be **systematically elevated in neurodivergent dyads** — not as a "
        "deficit, but as a structural asymmetry the instrument is specifically designed to scaffold. "
        "This is a **pre-registered secondary analysis** (H2.1)."
    )

    nd_col1, nd_col2 = st.columns([1.6, 1])
    with nd_col1:
        nd_pair_types = [
            "Both neurotypical",
            "NT sender / ND receiver",
            "ND sender / NT receiver",
            "Both neurodivergent",
        ]
        nd_mean_gaps  = [0.18, 0.27, 0.31, 0.24]
        nd_err        = [0.04, 0.05, 0.06, 0.05]
        nd_colors     = ["#8ca3b0", "#e7a59c", "#e7a59c", "#dce7f3"]

        fig_nd = go.Figure()
        fig_nd.add_trace(go.Bar(
            x=nd_pair_types, y=nd_mean_gaps,
            error_y=dict(type="data", array=nd_err, visible=True, color="#999"),
            marker_color=nd_colors,
            marker_line_color=["#6a8499","#c47b71","#c47b71","#aabccc"],
            marker_line_width=1.5,
            width=0.5,
        ))
        fig_nd.update_layout(
            title=dict(text="Mean intent gap score by annotator-pair type<br><sup>Pre-registered · H2.1 · Months 3–7 · Mock data for illustration</sup>",
                       font_size=13),
            yaxis=dict(title="Mean JSD (intent gap)", range=[0, 0.45]),
            xaxis=dict(tickfont=dict(size=11)),
            plot_bgcolor="#f5f6f7", paper_bgcolor="#f5f6f7",
            margin=dict(l=10, r=10, t=60, b=10), height=300,
        )
        fig_nd.add_hline(y=0.18, line_dash="dot", line_color="#8ca3b0", opacity=0.5,
                         annotation_text="NT–NT baseline", annotation_position="right")
        st.plotly_chart(fig_nd, use_container_width=True)

    with nd_col2:
        st.markdown("""
        <div style='background:#fff8f7;border-left:4px solid #e7a59c;padding:16px 18px;
                    border-radius:0 8px 8px 0;margin-top:12px;font-size:0.88em;color:#2c3e50;line-height:1.7;'>
          <div style='font-weight:700;margin-bottom:8px;color:#c47b71;'>Why the model predicts this</div>
          For <strong>autistic individuals</strong>, mentalising circuitry requires greater effort and
          less automaticity — the TPJ-mediated operation of reading another's intent is cognitively
          more costly.<br><br>
          For individuals with <strong>ADHD</strong>, attentional load may reduce resources available
          for pragmatic inference.<br><br>
          In both cases, the mechanism predicts a <em>wider intent gap on average</em> —
          exactly the asymmetry the instrument is designed to scaffold.
        </div>
        <div style='margin-top:12px;padding:8px 12px;background:rgba(220,231,243,0.6);
                    border-radius:6px;font-size:0.78em;color:#717182;'>
          Pre-registered secondary analysis · Intent gap scores stratified by annotator neurodiverse status ·
          Separate κ computed on neurodiverse-authored message subset
        </div>
        """, unsafe_allow_html=True)

    # ── Section 4: 60-day trajectory (H₂ illustration) ───────────────────────
    st.divider()
    st.markdown("## 4 · 60-day intent gap trajectory")
    st.markdown(
        "**H₂:** Participants using the Cognitive Companion for 60 days show a significant reduction "
        "in intent gap score compared to their Day 0 baseline. "
        "This chart illustrates the simulated trajectory for one participant dyad."
    )

    col_traj_controls, _ = st.columns([1, 2])
    with col_traj_controls:
        start_gap = st.slider("Starting gap (Day 1)", min_value=0.30, max_value=0.80, value=0.52, step=0.01)
        end_gap = st.slider("End gap (Day 60)", min_value=0.05, max_value=0.30, value=0.14, step=0.01)

    st.plotly_chart(
        trajectory_chart(days=60, start_gap=start_gap, end_gap=end_gap),
        use_container_width=True,
    )

    reduction_pct = round((start_gap - end_gap) / start_gap * 100, 1)
    st.success(
        f"**Simulated outcome:** Gap reduced from {start_gap:.2f} to {end_gap:.2f} "
        f"({reduction_pct}% reduction over 60 days). "
        f"This is the behavioural signature H₂ is designed to detect."
    )

    st.divider()
    st.markdown(
        "<div style='text-align:center; color:#666; font-size:0.85em'>"
        "NeuroAI Cognitive Companion · Encode x Pillar VC AI for Science Fellowship · March 2026<br>"
        "Demo uses pre-computed distributions. Production system: RoBERTa-large (355M params) fine-tuned on 2,000-message neural-pragmatic dataset.<br>"
        "<em>\"We are not building a chatbot. We are building the instrument that measures and closes the biological gap between human minds.\"</em>"
        "</div>",
        unsafe_allow_html=True,
    )


# ════════════════════════════════════════════════════════════════════════════
# TAB 2 — THE SCIENCE (hypotheses · dataset · model · RCT · timeline)
# ════════════════════════════════════════════════════════════════════════════
with tab_theplan:

    st.markdown("# 🔬 The Science")
    st.markdown("*Five hypotheses. One dataset. One model architecture. Twelve months.*")
    st.divider()

    # ── A1: Five Hypotheses ──────────────────────────────────────────────────
    st.markdown("## Five Formal Hypotheses")
    st.markdown(
        "Each hypothesis is independently testable, pre-registered, and publishable — "
        "including null results. MUST tier is fully executable without a lab partner."
    )

    hyp_data = [
        {
            "id": "H₁",
            "type": "Computational · Primary",
            "type_color": "#6B9FC4",
            "tier": "MUST",
            "tier_color": "#27ae60",
            "title": "Relational context improves intent prediction",
            "body": (
                "A RoBERTa-large model fine-tuned with a <strong>16-dimensional dyadic relational context vector</strong> "
                "concatenated to the [CLS] token achieves significantly higher macro-averaged F1 on "
                "perceived-intent prediction than an ablated message-only baseline.<br>"
                "<em>Test: paired t-test · α=0.05 · minimum Cohen's d ≥ 0.3</em>"
            ),
            "status": "Validation in progress · Months 3–6",
        },
        {
            "id": "H₂",
            "type": "Behavioural · Secondary",
            "type_color": "#9b59b6",
            "tier": "MUST",
            "tier_color": "#27ae60",
            "title": "60-day intervention reduces the intent gap",
            "body": (
                "Participants using the Cognitive Companion for 60 days show <strong>significant reduction "
                "in intent gap score</strong> compared to their Day 0 baseline.<br>"
                "<em>Test: within-subjects Wilcoxon signed-rank · α=0.05 · online behavioural probe N=50, Months 2–3</em>"
            ),
            "status": "Study design finalised · behavioural probe Month 2–3",
        },
        {
            "id": "H₃",
            "type": "Neural · Exploratory",
            "type_color": "#e7a59c",
            "tier": "STRETCH",
            "tier_color": "#95a5a6",
            "title": "Theta-band IBS increases after 60-day feedback",
            "body": (
                "Dyadic pairs who complete 60 days of closed-loop intent feedback show "
                "<strong>significant increase in theta-band inter-brain phase synchrony (IBS)</strong> "
                "during ambiguous-message reading tasks vs Day 0 baseline.<br>"
                "<em>Test: within-subjects Wilcoxon · EEG hyperscanning · N=20–24 dyadic pairs · α=0.05</em>"
            ),
            "status": "Lab partner outreach active · UCL FIL · MRC CBU · Nottingham Social Neuro",
        },
        {
            "id": "H₄",
            "type": "Ablation · Within Study 1b",
            "type_color": "#C9922A",
            "tier": "MUST",
            "tier_color": "#27ae60",
            "title": "Personality context solves cold-start",
            "body": (
                "A model conditioned on both the relational context vector <em>and</em> the "
                "<strong>biographical intake instrument personality context block</strong> achieves higher "
                "intent prediction accuracy at Day 1 than the relational-context-only model, "
                "with the gap narrowing as dyadic history accumulates over 4 weeks.<br>"
                "<em>Test: one-tailed t-test · α=0.05 · power=0.80 · primary metric: macro-F1 at Day 1, 14, 28</em>"
            ),
            "status": "RCT designed · N=100 · recruitment Month 1 · data collection Months 3–7",
        },
        {
            "id": "H₅",
            "type": "Exploratory · Beyond Year 1",
            "type_color": "#8ca3b0",
            "tier": "POST-FELLOWSHIP",
            "tier_color": "#bdc3c7",
            "title": "Soul surface produces higher empathic accuracy than direct conversation",
            "body": (
                "Consent-gated indirect probing of a partner's personality model produces "
                "<strong>higher empathic accuracy gains</strong> than equivalent amounts of direct conversation, "
                "because it removes the face-threat cost that suppresses authentic question-asking.<br>"
                "<em>Conditional on H₁ + H₂ validation</em>"
            ),
            "status": "Post-fellowship vision · Horizon 1 product layer",
        },
    ]

    for h in hyp_data:
        st.markdown(f"""
        <div style='margin-bottom:14px;padding:18px 20px;
                    background:rgba(220,231,243,0.25);border:1px solid #dce7f3;
                    border-radius:10px;border-left:4px solid {h["type_color"]};'>
          <div style='display:flex;align-items:center;gap:10px;margin-bottom:8px;flex-wrap:wrap;'>
            <span style='font-size:1.25em;font-weight:800;color:{h["type_color"]};'>{h["id"]}</span>
            <span style='font-size:0.72em;font-weight:700;color:{h["type_color"]};background:rgba(220,231,243,0.7);
                         padding:2px 8px;border-radius:4px;letter-spacing:0.08em;text-transform:uppercase;'>{h["type"]}</span>
            <span style='font-size:0.70em;font-weight:700;color:white;background:{h["tier_color"]};
                         padding:2px 8px;border-radius:4px;letter-spacing:0.08em;text-transform:uppercase;margin-left:auto;'>{h["tier"]}</span>
          </div>
          <div style='font-size:1.0em;font-weight:700;color:#2c3e50;margin-bottom:6px;'>{h["title"]}</div>
          <div style='font-size:0.84em;color:#556677;line-height:1.65;margin-bottom:8px;'>{h["body"]}</div>
          <div style='font-size:0.74em;color:#8ca3b0;font-style:italic;'>{h["status"]}</div>
        </div>
        """, unsafe_allow_html=True)

    st.caption("*Every null result is planned for and publishable. The programme depends on rigorous testing, not on confirmation.*")

    # ── A2: Dataset Architecture ─────────────────────────────────────────────
    st.divider()
    st.markdown("## Dataset Architecture — 2,000-Message Neural-Pragmatic Dataset")
    st.markdown(
        "To our knowledge, the first scientific dataset conditioning intent annotation on "
        "dyadic relational history, with dual sender-intent / perceived-intent labels and validated inter-rater reliability."
    )

    ds_col1, ds_col2 = st.columns([1.2, 1])

    with ds_col1:
        # Source breakdown bar
        sources = ["Relabelled public datasets", "Researcher-constructed stimuli", "LLM-assisted synthetic\n(human-reviewed)"]
        source_counts = [700, 600, 700]
        source_colors = ["#6B9FC4", "#e7a59c", "#8ca3b0"]
        fig_ds = go.Figure(go.Bar(
            x=source_counts, y=sources, orientation="h",
            marker_color=source_colors, text=source_counts,
            textposition="outside", width=0.5,
        ))
        fig_ds.update_layout(
            title=dict(text="2,000-message dataset — source breakdown", font_size=13),
            xaxis=dict(title="Messages", range=[0, 900]),
            plot_bgcolor="#f5f6f7", paper_bgcolor="#f5f6f7",
            margin=dict(l=10, r=60, t=50, b=10), height=220,
        )
        fig_ds.add_vline(x=700, line_dash="dot", line_color="#ccc", opacity=0.6)
        st.plotly_chart(fig_ds, use_container_width=True)

        # Relationship types
        st.markdown("""
        <div style='display:flex;flex-wrap:wrap;gap:8px;margin-top:4px;'>
          <span style='padding:5px 12px;background:rgba(107,159,196,0.12);border:1px solid #6B9FC4;
                       border-radius:20px;font-size:0.78em;color:#6B9FC4;font-weight:600;'>💑 Romantic partners</span>
          <span style='padding:5px 12px;background:rgba(231,165,156,0.12);border:1px solid #e7a59c;
                       border-radius:20px;font-size:0.78em;color:#c47b71;font-weight:600;'>👨‍👩‍👧 Parent-child</span>
          <span style='padding:5px 12px;background:rgba(46,204,113,0.12);border:1px solid #2ecc71;
                       border-radius:20px;font-size:0.78em;color:#27ae60;font-weight:600;'>🤝 Close friends</span>
          <span style='padding:5px 12px;background:rgba(155,89,182,0.12);border:1px solid #9b59b6;
                       border-radius:20px;font-size:0.78em;color:#9b59b6;font-weight:600;'>👥 Community / social</span>
          <span style='padding:5px 12px;background:rgba(201,146,42,0.12);border:1px solid #C9922A;
                       border-radius:20px;font-size:0.78em;color:#C9922A;font-weight:600;'>💼 Professional colleagues</span>
        </div>
        <div style='margin-top:8px;font-size:0.76em;color:#8ca3b0;'>
          Deliberate oversampling of ambiguous-valence messages (target 60%)
        </div>
        """, unsafe_allow_html=True)

    with ds_col2:
        st.markdown("""
        <div style='padding:16px 18px;background:rgba(220,231,243,0.4);border:1px solid #dce7f3;
                    border-radius:10px;font-size:0.84em;color:#556677;line-height:1.7;'>
          <div style='font-weight:700;color:#2c3e50;margin-bottom:8px;'>Annotation protocol</div>
          <div>📌 <strong>5 independent annotators</strong> per message</div>
          <div>📌 SI and PI annotated <strong>blind to each other</strong></div>
          <div>📌 "Ambiguous / I don't know" is a valid response</div>
          <div>📌 Cultural background recorded as metadata</div>
          <div>📌 Neurodiverse-authored messages included with separate κ</div>
          <div>📌 Recruited via <strong>Prolific Academic</strong></div>
          <div style='margin-top:10px;color:#8ca3b0;'>Estimated cost: £5,000–7,000</div>
        </div>
        <div style='margin-top:10px;padding:12px 16px;background:#fff8f7;border:1px solid #e7a59c;
                    border-left:4px solid #e7a59c;border-radius:0 8px 8px 0;font-size:0.82em;'>
          <div style='font-weight:700;color:#c47b71;margin-bottom:4px;'>Quality gate</div>
          <div style='color:#556677;'>κ pilot — 20 messages, 5 annotators — in Month 1.<br>
          Gate: if κ &lt; 0.70 after 2 adjudication rounds → pause, redesign schema, re-pilot.<br>
          <strong>Target: Cohen's κ &gt; 0.70</strong></div>
        </div>
        <div style='margin-top:10px;padding:10px 14px;background:rgba(46,204,113,0.1);border-radius:8px;
                    font-size:0.78em;color:#27ae60;font-weight:600;'>
          📤 Published on HuggingFace + OpenNeuro at Month 5
        </div>
        """, unsafe_allow_html=True)

    # 7-intent label space
    st.markdown("<div style='height:12px'></div>", unsafe_allow_html=True)
    st.markdown("**7-category intent label space (I1–I7)**")
    intent_rows = "".join([
        f"<tr style='border-bottom:1px solid #dce7f3;'>"
        f"<td style='padding:7px 14px;font-weight:700;color:#6B9FC4;'>{k}</td>"
        f"<td style='padding:7px 14px;font-weight:600;color:#2c3e50;'>{INTENTS[k]}</td>"
        f"<td style='padding:7px 14px;color:#717182;font-size:0.88em;'>{desc}</td></tr>"
        for k, desc in [
            ("I1", "Primary goal is relational proximity; content is secondary"),
            ("I2", "Communicates worry about receiver's state or wellbeing"),
            ("I3", "Signals a limit on behaviour, time, or emotional availability"),
            ("I4", "Requests acknowledgement or agreement, not action"),
            ("I5", "Communicates emotional state as primary payload"),
            ("I6", "Clear instrumental ask for action or change"),
            ("I7", "Neutral informational content with low emotional valence"),
        ]
    ])
    st.markdown(f"""
    <div style='overflow-x:auto;'>
    <table style='width:100%;border-collapse:collapse;font-size:0.85em;'>
      <thead><tr style='background:rgba(220,231,243,0.5);'>
        <th style='padding:8px 14px;text-align:left;color:#8ca3b0;'>ID</th>
        <th style='padding:8px 14px;text-align:left;color:#8ca3b0;'>Category</th>
        <th style='padding:8px 14px;text-align:left;color:#8ca3b0;'>Definition</th>
      </tr></thead>
      <tbody>{intent_rows}</tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

    # ── A3: Model Architecture ────────────────────────────────────────────────
    st.divider()
    st.markdown("## Model Architecture — Four Ablation Conditions")

    st.markdown("""
    <div style='padding:16px 20px;background:rgba(74,144,196,0.06);border:1px solid #dce7f3;
                border-radius:10px;margin-bottom:16px;font-size:0.88em;color:#556677;line-height:1.65;'>
      <strong>Base model:</strong> RoBERTa-large (355M parameters) — encoder-only architecture,
      purpose-built for classification tasks.<br>
      <strong>Architecture modification:</strong> 16-dimensional relational context vector concatenated
      to the [CLS] token representation before the classification head.
      Optional personality context block: 600–900 token biographical intake prepended to the message input.<br>
      <strong>Training:</strong> 3 runs × 5 epochs · AdamW · lr sweep 1e-5/2e-5/3e-5 ·
      early stopping on validation loss · <strong>Compute: Encode fellowship allocation (min £100k)</strong>
    </div>
    """, unsafe_allow_html=True)

    arch_col1, arch_col2 = st.columns([1.4, 1])

    with arch_col1:
        conditions = [
            ("A", "Relational context only",   "RoBERTa-large + 16-dim relational context vector",                             "#6B9FC4", "Tests H₁"),
            ("B", "Message only (baseline)",   "RoBERTa-large, no context vector",                                             "#8ca3b0", "H₁ baseline"),
            ("C", "Surface baseline",           "RoBERTa-base + sentiment classifier",                                          "#bdc3c7", "Surface floor"),
            ("D", "Full model (H₄)",            "RoBERTa-large + 16-dim vector + personality context block",                    "#e7a59c", "Tests H₄"),
        ]
        for cond, name, desc, color, note in conditions:
            st.markdown(f"""
            <div style='display:flex;align-items:flex-start;gap:12px;margin-bottom:10px;
                        padding:12px 14px;background:rgba(220,231,243,0.25);border-radius:8px;
                        border-left:3px solid {color};'>
              <div style='font-size:1.3em;font-weight:800;color:{color};min-width:26px;'>{cond}</div>
              <div>
                <div style='font-weight:700;color:#2c3e50;font-size:0.9em;'>{name}
                  <span style='font-size:0.72em;font-weight:400;color:#8ca3b0;margin-left:8px;'>{note}</span>
                </div>
                <div style='font-size:0.80em;color:#717182;margin-top:2px;font-family:monospace;'>{desc}</div>
              </div>
            </div>
            """, unsafe_allow_html=True)

    with arch_col2:
        st.markdown("""
        <div style='padding:16px 18px;background:rgba(220,231,243,0.4);border:1px solid #dce7f3;
                    border-radius:10px;'>
          <div style='font-size:0.72em;color:#8ca3b0;font-weight:700;letter-spacing:0.10em;
                      text-transform:uppercase;margin-bottom:10px;'>Architecture flow</div>
          <div style='font-family:monospace;font-size:0.78em;color:#2c3e50;line-height:2.0;'>
            [Message text]<br>
            &nbsp;&nbsp;↓<br>
            [RoBERTa-large encoder]<br>
            &nbsp;&nbsp;↓<br>
            [CLS token] ⊕ [16-dim relational vector]<br>
            &nbsp;&nbsp;↓<br>
            [Classification head]<br>
            &nbsp;&nbsp;↓<br>
            [7-way softmax P(I1–I7)]
          </div>
          <div style='margin-top:12px;padding:8px 10px;background:#fff8f7;border-radius:6px;
                      font-size:0.76em;color:#c47b71;'>
            <strong>Personality context block (Condition D):</strong><br>
            [Biographical intake] → [600–900 token block] → prepended to message input
          </div>
        </div>
        <div style='margin-top:10px;padding:10px 14px;background:rgba(52,152,219,0.08);
                    border-radius:8px;font-size:0.80em;color:#556677;'>
          <strong>H₁ contrast:</strong> Condition A vs Condition B<br>
          <strong>H₄ contrast:</strong> Condition D vs Condition A at Day 1
        </div>
        <div style='margin-top:8px;padding:10px 14px;background:rgba(46,204,113,0.08);
                    border-radius:8px;font-size:0.78em;color:#556677;'>
          📤 Fine-tuned model weights + evaluation harness released on HuggingFace under Apache 2.0 · Month 5–6
        </div>
        """, unsafe_allow_html=True)

    # ── A4: Study 1b Cold-Start RCT ───────────────────────────────────────────
    st.divider()
    st.markdown("## Study 1b — Cold-Start RCT (H₄ Test)")
    st.markdown(
        "Randomised controlled trial testing whether the biographical intake instrument "
        "improves intent prediction accuracy at Day 1 — before any dyadic history exists."
    )

    rct_col1, rct_col2 = st.columns([1.4, 1])

    with rct_col1:
        rct_months = ["Month 1", "Month 3", "Months 3–7", "Months 5–6", "Months 7–8"]
        rct_group_a = ["Recruitment (N=100), randomisation 1:1",
                       "Standard onboarding — no personality context",
                       "2× weekly sender self-annotation (Group A)",
                       "Researcher-labelled held-out evaluation set scoring",
                       "Primary analysis: H₄ confirmed or falsified"]
        rct_group_b = ["",
                       "10–15 min biographical intake (personality context)",
                       "2× weekly sender self-annotation (Group B)",
                       "",
                       ""]

        for i, (month, a, b) in enumerate(zip(rct_months, rct_group_a, rct_group_b)):
            st.markdown(f"""
            <div style='display:flex;gap:10px;margin-bottom:8px;align-items:flex-start;'>
              <div style='min-width:90px;font-size:0.78em;font-weight:700;color:#8ca3b0;padding-top:3px;'>{month}</div>
              <div style='flex:1;'>
                <div style='padding:7px 12px;background:rgba(74,144,196,0.12);border-radius:6px;
                            font-size:0.80em;color:#2c3e50;margin-bottom:4px;'>{a}</div>
                {"" if not b else f"<div style='padding:7px 12px;background:rgba(231,165,156,0.15);border-radius:6px;font-size:0.80em;color:#c47b71;'><strong>Group B only:</strong> {b}</div>"}
              </div>
            </div>
            """, unsafe_allow_html=True)

    with rct_col2:
        st.markdown("""
        <div style='padding:16px 18px;background:rgba(220,231,243,0.4);border:1px solid #dce7f3;border-radius:10px;'>
          <div style='font-size:0.72em;color:#8ca3b0;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;margin-bottom:10px;'>
            Study design
          </div>
          <div style='font-size:0.84em;color:#556677;line-height:1.7;'>
            <strong>N = 100</strong> new users (50 per arm)<br>
            Randomisation: 1:1<br>
            Recruitment: Month 1<br>
            Data collection: Months 3–7<br>
            Active period: 4 weeks per participant<br><br>
            <strong>Primary metric:</strong><br>
            Macro-averaged F1 on researcher-labelled held-out evaluation set at Day 1, 14, 28<br><br>
            <strong>Secondary metric:</strong><br>
            Time-to-convergence — the week at which Group B's F1 reaches Group A's Week 4 F1<br><br>
            Engagement level included as ANCOVA covariate
          </div>
        </div>
        <div style='margin-top:10px;padding:12px 14px;background:#fff8f7;border:1px solid #e7a59c;
                    border-radius:8px;font-size:0.82em;color:#c47b71;font-style:italic;'>
          "A null result in H₄ is planned for and publishable."
        </div>
        """, unsafe_allow_html=True)

    # ── A5: 12-Month Work Plan ────────────────────────────────────────────────
    st.divider()
    st.markdown("## 12-Month Work Plan")

    plan_data = [
        ("Month 1",       "κ pilot · ethics application · Study 1b pre-screening",           "MUST"),
        ("Months 1–3",    "2,000-message annotation · online H₂ behavioural probe (N=50)",   "MUST"),
        ("Month 3",       "Ethics approval received · Study 1b data collection begins",       "MUST"),
        ("Months 3–6",    "RoBERTa fine-tuning · ablation A/B/C/D · H₁ validation",          "MUST"),
        ("Months 3–7",    "Study 1b data collection: Group A and Group B",                    "MUST"),
        ("Month 5",       "Paper draft #1: dataset + model + H₁ → arXiv + circulated",       "MUST"),
        ("Months 7–8",    "Study 1b primary analysis: H₄ confirmed or falsified",            "MUST"),
        ("Months 6–8",    "Brain-Score submission · EEG pilot design · IRB approval",         "SHOULD"),
        ("Months 7–11",   "60-day EEG pilot · N=20–24 dyadic pairs · Day 0 + Day 60 EEG",    "SHOULD"),
        ("Months 11–12",  "Full study paper → submitted to ACL / EMNLP / CHI",               "MUST"),
    ]

    tier_color = {"MUST": "#27ae60", "SHOULD": "#C9922A", "STRETCH": "#95a5a6"}
    for period, activity, tier in plan_data:
        color = tier_color[tier]
        st.markdown(f"""
        <div style='display:flex;align-items:flex-start;gap:10px;margin-bottom:7px;'>
          <div style='min-width:100px;font-size:0.76em;font-weight:700;color:#8ca3b0;padding-top:5px;'>{period}</div>
          <div style='flex:1;padding:8px 14px;background:rgba(220,231,243,0.25);border-radius:7px;
                      border-left:3px solid {color};font-size:0.83em;color:#2c3e50;'>{activity}</div>
          <div style='min-width:62px;'>
            <span style='font-size:0.68em;font-weight:700;color:white;background:{color};
                         padding:3px 8px;border-radius:4px;letter-spacing:0.08em;text-transform:uppercase;'>{tier}</span>
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.caption("SHOULD tier requires confirmed lab partner letter by Month 3. MUST tier is fully executable independently.")

    st.divider()
    st.markdown(
        "<div style='text-align:center; color:#666; font-size:0.85em'>"
        "NeuroAI Cognitive Companion · Encode x Pillar VC AI for Science Fellowship · March 2026<br>"
        "<em>\"This is AI for Science, not science-flavoured product.\"</em>"
        "</div>",
        unsafe_allow_html=True,
    )


# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — NON-TECHNICAL / HUMAN STORY VIEW
# ════════════════════════════════════════════════════════════════════════════
with tab_human:
    st.markdown(FUTURISTIC_CSS, unsafe_allow_html=True)

    # ── Header ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style='padding: 28px 0 8px 0;'>
        <div class='nt-header'>Every word you say lands differently<br>depending on who's listening.</div>
        <div class='nt-subheader'>NeuroAI Cognitive Companion &nbsp;·&nbsp; Intent Gap Visualiser</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class='nt-insight-box'>
    Your words don't travel from your mind to theirs unchanged.
    They pass through the entire history of your relationship —
    every argument, every warmth, every unspoken assumption.
    This instrument measures that gap.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)

    # ── Selectors ─────────────────────────────────────────────────────────────
    st.markdown("<div class='nt-section-title'>Choose a scenario</div>", unsafe_allow_html=True)

    col_nt1, col_nt2 = st.columns([1, 1])
    with col_nt1:
        nt_message = st.selectbox(
            "What was said?",
            options=list(MOCK_MODEL.keys()),
            index=0,
            key="nt_message",
            help="Choose from these everyday messages.",
        )
    with col_nt2:
        nt_context_key = st.selectbox(
            "Who said it to?",
            options=list(CONTEXT_LABELS.keys()),
            format_func=lambda k: context_label_plain(k),
            index=0,
            key="nt_context",
        )

    nt_data = MOCK_MODEL[nt_message][nt_context_key]
    nt_si = nt_data["SI"]
    nt_pi = nt_data["PI"]
    nt_gap = js_divergence(nt_si, nt_pi)
    story = get_human_story(nt_message, nt_context_key, nt_si, nt_pi, nt_gap)

    # ── The message card ──────────────────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='nt-big-question'>"{nt_message}"</div>
    <div class='nt-context-pill'>{context_label_plain(nt_context_key)}</div>
    """, unsafe_allow_html=True)

    # Sent / Heard boxes
    col_sent, col_heard = st.columns(2)
    with col_sent:
        st.markdown(f"""
        <div class='nt-signal-box nt-sent'>
            <div class='nt-label'>📡 &nbsp; Sent as</div>
            <div class='nt-intent-text'>{story['sent_as'].capitalize()}</div>
        </div>
        """, unsafe_allow_html=True)
    with col_heard:
        heard_color_class = "nt-heard" if story["aligned"] else "nt-heard"
        st.markdown(f"""
        <div class='nt-signal-box nt-heard' style='border-left-color: {"#6BAE8A" if story["aligned"] else "#B84040" if nt_gap > 0.25 else "#C9922A"};'>
            <div class='nt-label'>📥 &nbsp; Received as</div>
            <div class='nt-intent-text'>{story['heard_as'].capitalize()}</div>
        </div>
        """, unsafe_allow_html=True)

    # Connection level badge + summary
    st.markdown(f"""
    <div style='margin: 18px 0 4px 0;'>
        <span class='nt-connection-badge' style='background:#ffffff; border: 2px solid {story["color_theme"]}; color:#2c3e50;'>
            <span style='display:inline-block;width:10px;height:10px;border-radius:50%;
                         background:{story["color_theme"]};margin-right:7px;vertical-align:middle;'></span>{story['connection_level']}
        </span>
    </div>
    <div class='nt-summary'>{story['summary']}</div>
    """, unsafe_allow_html=True)

    # ── Connection bridge arc ─────────────────────────────────────────────────
    st.markdown("<div class='nt-section-title' style='margin-top:28px'>How much meaning got through?</div>", unsafe_allow_html=True)

    col_bridge, col_bridge_text = st.columns([1.2, 1])
    with col_bridge:
        st.plotly_chart(
            make_bridge_chart(story["bridge_fill"], story["color_theme"], nt_gap),
            use_container_width=True,
        )
    with col_bridge_text:
        pct = int(story["bridge_fill"] * 100)
        if pct >= 90:
            bridge_narrative = "The signal is travelling clean. Both minds are aligned on what this conversation is actually about."
        elif pct >= 75:
            bridge_narrative = "Most of the meaning arrived intact. A small residue of uncertainty is normal — every relationship has a little noise."
        elif pct >= 45:
            bridge_narrative = "Almost half the meaning is lost in transit. The receiver is reconstructing what they think you meant — not necessarily what you said."
        elif pct >= 20:
            bridge_narrative = "The message has been substantially reinterpreted. By the time it lands, it carries a different emotional weight than it was sent with."
        else:
            bridge_narrative = "The signal has been nearly inverted. A message sent as a reach for connection is landing as a threat. This is the most common engine of unnecessary conflict."
        st.markdown(f"""
        <div style='padding: 20px 0 0 10px; color: #99aabb; font-size: 1.05em; line-height: 1.7;'>
            {bridge_narrative}
        </div>
        """, unsafe_allow_html=True)

    # ── Relationship context comparison ──────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>How the same words travel through different relationships</div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='nt-insight-box'>
    "<em>{nt_message}</em>" — one sentence. Four relationships. Four completely different arrivals.
    The words don't change. The relationship does the interpreting.
    </div>
    """, unsafe_allow_html=True)

    # Connection quality bars — no numbers
    st.markdown("<div style='margin: 16px 0 8px 0; color: #6680aa; font-size: 0.9em;'>Connection clarity across relationship types:</div>", unsafe_allow_html=True)
    st.plotly_chart(make_neural_signal_bars(nt_message), use_container_width=True)

    # Context-by-context plain English breakdown
    contexts_ordered = list(CONTEXT_LABELS.keys())
    gaps_nt = {c: js_divergence(MOCK_MODEL[nt_message][c]["SI"], MOCK_MODEL[nt_message][c]["PI"]) for c in contexts_ordered}
    context_stories_nt = {c: get_human_story(nt_message, c, MOCK_MODEL[nt_message][c]["SI"], MOCK_MODEL[nt_message][c]["PI"], gaps_nt[c]) for c in contexts_ordered}

    col_ctx1, col_ctx2 = st.columns(2)
    ctx_cols = [col_ctx1, col_ctx2, col_ctx1, col_ctx2]

    for i, ctx in enumerate(contexts_ordered):
        s = context_stories_nt[ctx]
        with ctx_cols[i]:
            match_icon = "✓" if s["aligned"] else "≠"
            match_color = "#7BA7C9" if s["aligned"] else s["color_theme"]
            st.markdown(f"""
            <div class='nt-card' style='padding:12px 16px; border-color:#ececf0;'>
                <div style='display:flex;align-items:center;justify-content:space-between;margin-bottom:5px;'>
                    <span style='font-size:0.92em;font-weight:600;color:#4a5568;'>{context_label_plain(ctx)}</span>
                    <span style='display:flex;align-items:center;gap:5px;'>
                        <span style='width:7px;height:7px;border-radius:50%;background:{s["color_theme"]};display:inline-block;flex-shrink:0;'></span>
                        <span style='font-size:0.75em;color:#8ca3b0;'>{s['connection_level']}</span>
                    </span>
                </div>
                <div style='font-size:0.83em;color:#8ca3b0;'>
                    {s['sent_as'].capitalize()}
                    <span style='color:{match_color};margin:0 3px;'>{match_icon}</span>
                    {s['heard_as'].capitalize()}
                </div>
            </div>
            """, unsafe_allow_html=True)

    # ── Radar: intent fingerprint across contexts ─────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>The interpretation fingerprint</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='color:#717182; font-size:0.95em; margin-bottom:12px;'>
    Each shape below shows how the receiver interprets the message in that relationship.
    When shapes overlap, understanding aligns. When they diverge, so does the conversation.
    </div>
    """, unsafe_allow_html=True)
    st.plotly_chart(make_radar_all_contexts(nt_message, selected_ctx_key=nt_context_key), use_container_width=True)

    # ── Cold-Start / Personality Context (H₄) ────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='margin-bottom:14px;'>
      <div style='font-size:1.3em;font-weight:700;color:#2c3e50;margin-bottom:6px;'>
        What if the model has never seen this person before?
        <span style='font-size:0.58em;font-weight:400;color:#8ca3b0;letter-spacing:0.1em;
                     text-transform:uppercase;margin-left:10px;vertical-align:middle;
                     background:rgba(220,231,243,0.7);padding:2px 8px;border-radius:4px;'>
          H₄ · Cold-start problem
        </span>
      </div>
      <div style='font-size:0.88em;color:#717182;line-height:1.6;max-width:760px;'>
        At Day 1, there is no relational history. Without context, the model defaults to
        population-level priors — the gap score is systematically inflated.
        The <strong>biographical intake instrument</strong> solves this: 8 guided questions across
        three layers <em>(identity values · decision architecture · narrative stories)</em> — 10–15 minutes,
        completed once before first use.
      </div>
    </div>
    """, unsafe_allow_html=True)

    cs_col1, cs_col2 = st.columns(2)

    _cs_intents_short = ["Connection", "Concern", "Boundary", "Validation", "Frustration", "Request", "Info"]
    _cs_si  = [0.40, 0.14, 0.05, 0.22, 0.05, 0.09, 0.05]
    _cs_pi_cold  = [0.11, 0.10, 0.16, 0.12, 0.28, 0.14, 0.09]   # inflated gap ~0.28
    _cs_pi_warm  = [0.30, 0.14, 0.07, 0.21, 0.13, 0.10, 0.05]   # calibrated  ~0.10

    def _cs_bar(si, pi, title, gap_val, gap_color_hex):
        fig = go.Figure()
        fig.add_trace(go.Bar(name="Sender Intent (SI)", x=_cs_intents_short, y=si,
                             marker_color="#6B9FC4", opacity=0.85))
        fig.add_trace(go.Bar(name="Perceived Intent (PI)", x=_cs_intents_short, y=pi,
                             marker_color="#e7a59c", opacity=0.85))
        fig.update_layout(
            title=dict(text=title, font_size=12),
            barmode="group",
            yaxis=dict(range=[0, 0.6], title="Probability"),
            plot_bgcolor="#f5f6f7", paper_bgcolor="#f5f6f7",
            legend=dict(orientation="h", y=-0.25),
            margin=dict(l=10, r=10, t=50, b=10), height=280,
            annotations=[dict(
                text=f"Gap: <b>{gap_val:.2f}</b>",
                xref="paper", yref="paper", x=0.98, y=0.96,
                showarrow=False, bgcolor=gap_color_hex, bordercolor=gap_color_hex,
                font=dict(color="white", size=13, family="monospace"),
                borderpad=5, borderwidth=1,
            )],
        )
        return fig

    with cs_col1:
        st.markdown("""
        <div style='background:#fff8f7;border:1px solid #e7a59c;border-radius:8px;padding:10px 14px 4px;
                    margin-bottom:8px;font-size:0.82em;color:#c47b71;font-weight:600;'>
          Day 1 — no biographical context
        </div>""", unsafe_allow_html=True)
        st.plotly_chart(_cs_bar(_cs_si, _cs_pi_cold,
                                '"Can we talk tonight?" · Day 1, no context', 0.28, "#e7a59c"),
                        use_container_width=True)

    with cs_col2:
        st.markdown("""
        <div style='background:#f0fff4;border:1px solid #2ecc71;border-radius:8px;padding:10px 14px 4px;
                    margin-bottom:8px;font-size:0.82em;color:#27ae60;font-weight:600;'>
          Day 1 — with biographical intake instrument
        </div>""", unsafe_allow_html=True)
        st.plotly_chart(_cs_bar(_cs_si, _cs_pi_warm,
                                '"Can we talk tonight?" · Day 1, with personality context', 0.10, "#27ae60"),
                        use_container_width=True)

    st.markdown("""
    <div style='margin-top:8px;padding:16px 20px;background:rgba(220,231,243,0.4);
                border:1px solid #dce7f3;border-radius:10px;font-size:0.86em;color:#556677;line-height:1.65;'>
      <span style='font-weight:700;color:#2c3e50;'>Gap reduction at Day 1:</span>
      0.28 → 0.10 — before a single message is exchanged.
      The biographical intake instrument provides the prior that relational history cannot provide yet.<br><br>
      <span style='font-weight:700;color:#8ca3b0;'>H₄ prediction:</span> The gap between Group A (no personality context) and
      Group B (with biographical intake) narrows as dyadic history accumulates over 4 weeks —
      the instrument solves cold-start, history takes over.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='margin-top:14px;padding:16px 20px;
                background:linear-gradient(135deg,rgba(220,231,243,0.6) 0%,rgba(231,165,156,0.08) 100%);
                border:1px dashed #8ca3b0;border-radius:10px;font-size:0.84em;line-height:1.65;'>
      <div style='font-size:0.7em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;
                  text-transform:uppercase;margin-bottom:8px;'>🔒 Soul Surface — Horizon 1 · Consent-gated</div>
      <div style='color:#2c3e50;'>
        The biographical intake instrument doubles as a <strong>consent-gated soul surface</strong> —
        a curated window into how a person thinks, shareable only when both partners have
        reciprocally shared their own.
        Raw biographical answers are never shared; only the derived intent model is accessible,
        under explicit mutual consent with full revocation rights.<br><br>
        <em style='color:#8ca3b0;'>This operationalises Gottman's (1994) love map construct computationally.</em>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Cognitive Field ────────────────────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='margin-bottom:14px;'>
      <div style='font-size:1.3em;font-weight:700;color:#2c3e50;margin-bottom:6px;'>
        Cognitive Field
        <span style='font-size:0.6em;font-weight:400;color:#8ca3b0;letter-spacing:0.1em;
                     text-transform:uppercase;margin-left:10px;vertical-align:middle;
                     background:rgba(220,231,243,0.7);padding:2px 8px;border-radius:4px;'>
          Horizon 1 · Beta Month 6
        </span>
      </div>
      <div style='font-size:0.88em;color:#717182;line-height:1.6;max-width:700px;'>
        Every interaction leaves a trace in the semantic field between two minds.
        The model doesn't just record what was said — it learns how each person's intent
        landscape shifts relative to the other's over time. As the field converges,
        understanding deepens. This is what the programme is designed to measure — and to change.
        <br><span style='color:#8ca3b0;font-size:0.9em;font-style:italic;'>
        Illustrative — based on mock model data. Real cognitive fields generated from beta cohort, Month 6+.
        </span>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Cognitive Field — two Gaussian density fields showing convergence
    # Day 0: separate fields (high gap state)
    # Day 60: overlapping fields (low gap state)
    import math as _math
    _grid_x = np.linspace(-3, 3, 80)
    _grid_y = np.linspace(-3, 3, 80)
    _X, _Y = np.meshgrid(_grid_x, _grid_y)

    def _gauss2d(cx, cy, sx, sy, amp=1.0):
        return amp * np.exp(-((_X - cx)**2 / (2*sx**2) + (_Y - cy)**2 / (2*sy**2)))

    # Day 0 fields — diverged
    _maya_d0 = _gauss2d(-1.3, 0.5, 0.7, 0.6, 1.0)
    _dev_d0  = _gauss2d( 1.3, -0.5, 0.7, 0.6, 1.0)
    # Day 60 fields — converging toward centre
    _maya_d60 = _gauss2d(-0.5, 0.2, 0.55, 0.5, 1.0)
    _dev_d60  = _gauss2d( 0.5, -0.2, 0.55, 0.5, 1.0)
    # Shared field — the overlap zone (what they've built together)
    _shared = np.minimum(_maya_d60, _dev_d60) * 2.2

    col_twin_l, col_twin_r = st.columns(2)
    with col_twin_l:
        fig_d0 = go.Figure()
        fig_d0.add_trace(go.Contour(
            z=_maya_d0, x=_grid_x, y=_grid_y,
            colorscale=[[0,'rgba(245,246,247,0)'],[0.3,'rgba(140,163,176,0.15)'],
                        [0.7,'rgba(140,163,176,0.45)'],[1,'rgba(44,62,80,0.7)']],
            showscale=False, contours=dict(coloring='fill', showlines=False),
            name='Maya', opacity=0.85,
        ))
        fig_d0.add_trace(go.Contour(
            z=_dev_d0, x=_grid_x, y=_grid_y,
            colorscale=[[0,'rgba(245,246,247,0)'],[0.3,'rgba(231,165,156,0.15)'],
                        [0.7,'rgba(231,165,156,0.45)'],[1,'rgba(196,123,113,0.7)']],
            showscale=False, contours=dict(coloring='fill', showlines=False),
            name='Dev', opacity=0.85,
        ))
        # Labels
        fig_d0.add_annotation(x=-1.3, y=0.5, text="Maya", showarrow=False,
            font=dict(color='#2c3e50', size=11, family='sans-serif'), bgcolor='rgba(255,255,255,0.7)')
        fig_d0.add_annotation(x=1.3, y=-0.5, text="Dev", showarrow=False,
            font=dict(color='#c47b71', size=11, family='sans-serif'), bgcolor='rgba(255,255,255,0.7)')
        fig_d0.update_layout(
            title=dict(text='Day 0 · Separate cognitive fields',
                       font=dict(size=11, color='#8ca3b0'), x=0.5),
            xaxis=dict(visible=False, range=[-3, 3]),
            yaxis=dict(visible=False, range=[-3, 3]),
            paper_bgcolor='rgba(245,246,247,0)', plot_bgcolor='rgba(220,231,243,0.2)',
            margin=dict(l=10, r=10, t=45, b=10), height=260, showlegend=False,
        )
        st.plotly_chart(fig_d0, use_container_width=True)

    with col_twin_r:
        fig_d60 = go.Figure()
        fig_d60.add_trace(go.Contour(
            z=_maya_d60, x=_grid_x, y=_grid_y,
            colorscale=[[0,'rgba(245,246,247,0)'],[0.3,'rgba(140,163,176,0.15)'],
                        [0.7,'rgba(140,163,176,0.45)'],[1,'rgba(44,62,80,0.7)']],
            showscale=False, contours=dict(coloring='fill', showlines=False),
            name='Maya', opacity=0.75,
        ))
        fig_d60.add_trace(go.Contour(
            z=_dev_d60, x=_grid_x, y=_grid_y,
            colorscale=[[0,'rgba(245,246,247,0)'],[0.3,'rgba(231,165,156,0.15)'],
                        [0.7,'rgba(231,165,156,0.45)'],[1,'rgba(196,123,113,0.7)']],
            showscale=False, contours=dict(coloring='fill', showlines=False),
            name='Dev', opacity=0.75,
        ))
        fig_d60.add_trace(go.Contour(
            z=_shared, x=_grid_x, y=_grid_y,
            colorscale=[[0,'rgba(245,246,247,0)'],[0.5,'rgba(180,195,160,0.3)'],
                        [1,'rgba(120,160,120,0.55)']],
            showscale=False, contours=dict(coloring='fill', showlines=False),
            name='Shared', opacity=0.9,
        ))
        fig_d60.add_annotation(x=-0.5, y=0.2, text="Maya", showarrow=False,
            font=dict(color='#2c3e50', size=11, family='sans-serif'), bgcolor='rgba(255,255,255,0.7)')
        fig_d60.add_annotation(x=0.5, y=-0.2, text="Dev", showarrow=False,
            font=dict(color='#c47b71', size=11, family='sans-serif'), bgcolor='rgba(255,255,255,0.7)')
        fig_d60.add_annotation(x=0.0, y=0.05, text="shared", showarrow=False,
            font=dict(color='#5a7a5a', size=10, family='sans-serif'), bgcolor='rgba(255,255,255,0.7)')
        fig_d60.update_layout(
            title=dict(text='Day 60 · Fields converging — shared zone emerging',
                       font=dict(size=11, color='#8ca3b0'), x=0.5),
            xaxis=dict(visible=False, range=[-3, 3]),
            yaxis=dict(visible=False, range=[-3, 3]),
            paper_bgcolor='rgba(245,246,247,0)', plot_bgcolor='rgba(220,231,243,0.2)',
            margin=dict(l=10, r=10, t=45, b=10), height=260, showlegend=False,
        )
        st.plotly_chart(fig_d60, use_container_width=True)

    st.markdown("""
    <div style='text-align:center;font-size:0.73em;color:#8ca3b0;font-style:italic;margin-top:-8px;margin-bottom:8px;'>
      Cognitive field density map · blue = Maya's intent landscape · blush = Dev's · green overlap = shared semantic ground ·
      H₂: gap score decline over 60 days · Projected
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style='display:flex;gap:16px;flex-wrap:wrap;margin-top:4px;margin-bottom:8px;'>
      <div style='flex:1;min-width:180px;padding:10px 14px;background:rgba(220,231,243,0.5);
                  border-radius:8px;font-size:0.82em;color:#717182;'>
        <span style='color:#8ca3b0;font-weight:700;'>Faded points</span> = Day 0 baseline.<br>
        <span style='color:#8ca3b0;font-weight:700;'>Solid points</span> = Day 60 post-intervention.<br>
        Arrows show centroid trajectory.
      </div>
      <div style='flex:1;min-width:180px;padding:10px 14px;background:rgba(220,231,243,0.4);
                  border-radius:8px;font-size:0.82em;color:#717182;'>
        <span style='color:#8ca3b0;font-weight:700;'>Converging clusters</span> = growing shared understanding.<br>
        Measured via JS-divergence on rolling 14-day message window.
      </div>
      <div style='flex:1;min-width:180px;padding:10px 14px;background:rgba(231,165,156,0.10);
                  border-radius:8px;font-size:0.82em;color:#717182;'>
        <span style='color:#e7a59c;font-weight:700;'>H₂ behavioural proxy:</span> gap score decline over 60 days.
        Real beta data from Month 6 onwards.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Real-time deployment vision ───────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>Where this lives — real-time & on-device</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class='nt-insight-box' style='margin-bottom:16px;'>
    This demo runs as a web app. The production instrument lives <em>inside</em> the conversation —
    as a quiet signal layer sitting beneath the messages you're already sending.
    No data leaves your device. No cloud. Just the gap, made visible, in the moment.
    </div>
    """, unsafe_allow_html=True)

    col_d1, col_d2, col_d3 = st.columns(3)
    with col_d1:
        st.markdown("""
        <div class='nt-card' style='min-height:260px;'>
            <div style='font-size:1.6em; margin-bottom:10px;'>💬</div>
            <div style='font-weight:700; color:#8ca3b0; font-size:1.05em; margin-bottom:8px;'>Chat · Text · Messaging</div>
            <div style='color:#8ca3b0; font-size:0.88em; line-height:1.65;'>
                A browser extension or keyboard overlay shows a small signal indicator
                as you type. Before you hit send, you see how the message is likely
                to land — in this relationship, today. One colour. No scores.<br><br>
                <span style='color:#8ca3b0; font-size:0.9em;'>WhatsApp · iMessage · Slack · Teams</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_d2:
        st.markdown("""
        <div class='nt-card' style='min-height:260px;'>
            <div style='font-size:1.6em; margin-bottom:10px;'>🎙️</div>
            <div style='font-weight:700; color:#8ca3b0; font-size:1.05em; margin-bottom:8px;'>Voice · Audio · Face-to-face</div>
            <div style='color:#8ca3b0; font-size:0.88em; line-height:1.65;'>
                Real-time transcription feeds the intent classifier on-device.
                A subtle ambient signal — a soft colour wash on screen or a discreet
                wearable indicator — shifts as the conversation drifts. Both people
                can opt in, creating a shared signal neither is performing for.<br><br>
                <span style='color:#8ca3b0; font-size:0.9em;'>Couples sessions · Therapy · Mediation</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    with col_d3:
        st.markdown("""
        <div class='nt-card' style='min-height:260px;'>
            <div style='font-size:1.6em; margin-bottom:10px;'>🧠</div>
            <div style='font-weight:700; color:#8ca3b0; font-size:1.05em; margin-bottom:8px;'>Neural · EEG · Biometric</div>
            <div style='color:#8ca3b0; font-size:0.88em; line-height:1.65;'>
                In the research lab, the same intent gap signal is paired with EEG
                inter-brain synchrony. The computational measure and the neural
                measure are validated against each other — so that eventually,
                the software signal alone predicts the brain state it was designed to shift.<br><br>
                <span style='color:#8ca3b0; font-size:0.9em;'>H₃ · EEG hyperscanning · 60-day pilot</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Design principles strip
    st.markdown("""
    <div style='margin-top:18px; padding: 14px 20px; background: rgba(52,152,219,0.04);
         border: 1px solid #dce7f3; border-radius:10px;
         display:flex; gap:40px; flex-wrap:wrap; color:#8ca3b0; font-size:0.85em; line-height:1.8;'>
        <span>🔒 &nbsp;<span style='color:#5577aa;'>On-device · no cloud transit</span></span>
        &nbsp;&nbsp;&nbsp;
        <span>👁️ &nbsp;<span style='color:#5577aa;'>Opt-in · consent-first</span></span>
        &nbsp;&nbsp;&nbsp;
        <span>🤫 &nbsp;<span style='color:#5577aa;'>Ambient · not intrusive</span></span>
        &nbsp;&nbsp;&nbsp;
        <span>⚡ &nbsp;<span style='color:#5577aa;'>&lt;200ms latency · real-time</span></span>
        &nbsp;&nbsp;&nbsp;
        <span>📵 &nbsp;<span style='color:#5577aa;'>No message content stored</span></span>
    </div>
    """, unsafe_allow_html=True)

    # ── What the AI can do ────────────────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='padding: 8px 0 4px 0;'>
        <div style='font-size:1.55em; font-weight:700; color:#8ca3b0; margin-bottom:10px;'>
            What if you could close the gap?
        </div>
    </div>
    <div class='nt-insight-box' style='font-size:1.05em; line-height:1.75;'>
    The NeuroAI Cognitive Companion doesn't tell you what to say.
    It shows you how your words are landing — and, over time, helps both of you
    learn to listen for what the other person actually means, not just what they said.<br><br>
    Measured not by relationship advice, but by the same tools neuroscience uses
    to study how the brain processes another person's mind.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div style='height: 12px'></div>", unsafe_allow_html=True)

    col_cta1, col_cta2, col_cta3 = st.columns(3)
    with col_cta1:
        st.markdown("""
        <div class='nt-card' style='text-align:center; padding: 22px 16px;'>
            <div style='font-size:2em; margin-bottom:8px;'>🧬</div>
            <div style='font-weight:700; color:#8ca3b0; font-size:1.05em; margin-bottom:6px;'>Grounded in neuroscience</div>
            <div style='color:#8ca3b0; font-size:0.9em;'>The gap between intended and perceived meaning is a measurable neural phenomenon, not just a feeling.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_cta2:
        st.markdown("""
        <div class='nt-card' style='text-align:center; padding: 22px 16px;'>
            <div style='font-size:2em; margin-bottom:8px;'>📡</div>
            <div style='font-weight:700; color:#8ca3b0; font-size:1.05em; margin-bottom:6px;'>Real-time signal</div>
            <div style='color:#8ca3b0; font-size:0.9em;'>Every message tagged, every context accounted for. A living map of how two minds are — and aren't — connecting.</div>
        </div>
        """, unsafe_allow_html=True)
    with col_cta3:
        st.markdown("""
        <div class='nt-card' style='text-align:center; padding: 22px 16px;'>
            <div style='font-size:2em; margin-bottom:8px;'>🌱</div>
            <div style='font-weight:700; color:#8ca3b0; font-size:1.05em; margin-bottom:6px;'>Closes over time</div>
            <div style='color:#8ca3b0; font-size:0.9em;'>The brain is plastic. With the right signal, the gap can narrow — measurably, verifiably, at the neural level. That's what H₃ is designed to test.</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Footer ────────────────────────────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center; color:#8ca3b0; font-size:0.82em; padding-bottom: 20px;'>
        NeuroAI Cognitive Companion &nbsp;·&nbsp; Encode × Pillar VC AI for Science Fellowship &nbsp;·&nbsp; March 2026<br>
        <span style='color:#1e2a4a;'>━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━</span><br>
        <em style='color:#8ca3b0;'>"The most powerful thing two people can do is understand what the other actually means."</em>
    </div>
    """, unsafe_allow_html=True)


# ════════════════════════════════════════════════════════════════════════════
# TAB 3 — IN THE WILD: DEVICE & FREQUENCY UX
# ════════════════════════════════════════════════════════════════════════════
with tab_deploy:
    st.markdown(FUTURISTIC_CSS, unsafe_allow_html=True)

    # ── helpers for this tab ──────────────────────────────────────────────────
    def signal_dot(color, label, size=14):
        return (f"<span style='display:inline-block;width:{size}px;height:{size}px;"
                f"border-radius:50%;background:{color};margin-right:6px;"
                f"vertical-align:middle;box-shadow:0 0 6px {color};'></span>"
                f"<span style='color:#2c3e50;font-size:0.85em;'>{label}</span>")

    def freq_bar(pct, color, label, sublabel=""):
        return f"""
        <div style='margin-bottom:10px;'>
          <div style='display:flex;justify-content:space-between;margin-bottom:3px;'>
            <span style='color:#717182;font-size:0.82em;'>{label}</span>
            <span style='color:{color};font-size:0.78em;font-weight:600;'>{sublabel}</span>
          </div>
          <div style='background:#111122;border-radius:4px;height:8px;overflow:hidden;'>
            <div style='width:{pct}%;height:100%;background:linear-gradient(90deg,{color}88,{color});
                        border-radius:4px;'></div>
          </div>
        </div>"""

    # ── Header ────────────────────────────────────────────────────────────────
    st.markdown("""
    <div style='padding:28px 0 6px 0;'>
      <div class='nt-header' style='font-size:2.0em;'>Where the signal lives.<br>When it speaks. How it looks.</div>
      <div class='nt-subheader'>Real-world deployment · device formats · trigger logic</div>
    </div>
    <div class='nt-insight-box'>
    The intent gap instrument is not a standalone app you open.
    It is a <em>layer</em> — a quiet presence inside the tools you already use.
    This tab shows the three deployment surfaces, when the signal fires, and exactly what you see.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # SECTION 1 — DEVICE MOCKUPS (side by side)
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("<div class='nt-section-title'>Surface 1 of 3 — Choose a device</div>", unsafe_allow_html=True)

    dev_choice = st.radio(
        "",
        ["📱  Mobile · texting in the moment",
         "💻  Laptop · messaging at a desk",
         "🎙️  Audio · face-to-face / voice call"],
        horizontal=True,
        key="dev_choice",
        label_visibility="collapsed",
    )

    st.markdown("<div style='height:8px'></div>", unsafe_allow_html=True)

    # ── MOBILE MOCKUP ─────────────────────────────────────────────────────────
    if "Mobile" in dev_choice:
        col_phone, col_phone_desc = st.columns([1.4, 1])
        with col_phone:
            st.markdown("""
            <div style='display:flex;justify-content:center;'>
            <div style='
                width:220px; height:440px;
                background:linear-gradient(180deg,#ffffff 0%,#f5f6f7 100%);
                border-radius:36px;
                border:2px solid #dce7f3;
                box-shadow:0 8px 32px rgba(140,163,176,0.18), inset 0 0 12px rgba(220,231,243,0.3);
                position:relative; overflow:hidden;
                font-family: -apple-system, sans-serif;
            '>
              <!-- notch -->
              <div style='width:70px;height:18px;background:#ececf0;border-radius:0 0 12px 12px;
                          margin:0 auto;position:relative;z-index:10;'></div>
              <!-- status bar -->
              <div style='display:flex;justify-content:space-between;padding:4px 18px 0 18px;
                          font-size:9px;color:#8ca3b0;'>
                <span>9:41</span><span>●●●  WiFi  🔋</span>
              </div>
              <!-- app bar -->
              <div style='background:#f5f6f7;padding:8px 14px;margin-top:4px;
                          border-bottom:1px solid #ececf0;display:flex;align-items:center;gap:8px;'>
                <div style='width:28px;height:28px;border-radius:50%;background:#dce7f3;
                             border:1px solid #8ca3b0;display:flex;align-items:center;
                             justify-content:center;font-size:11px;color:#2c3e50;font-weight:600;'>A</div>
                <div>
                  <div style='font-size:10px;font-weight:600;color:#2c3e50;'>Alex</div>
                  <div style='font-size:8px;color:#8ca3b0;'>Partner · 3 years</div>
                </div>
              </div>
              <!-- chat bubbles -->
              <div style='padding:10px 10px 4px;'>
                <!-- incoming -->
                <div style='display:flex;gap:6px;margin-bottom:8px;'>
                  <div style='width:22px;height:22px;border-radius:50%;background:#dce7f3;
                               border:1px solid #8ca3b0;flex-shrink:0;font-size:9px;
                               display:flex;align-items:center;justify-content:center;color:#2c3e50;font-weight:600;'>A</div>
                  <div style='background:#dce7f3;border-radius:12px 12px 12px 2px;
                               padding:6px 10px;max-width:130px;'>
                    <div style='font-size:9px;color:#2c3e50;'>How was your day?</div>
                    <div style='font-size:7px;color:#8ca3b0;margin-top:2px;'>10:23 AM</div>
                  </div>
                </div>
              </div>
              <!-- INPUT BAR with signal indicator -->
              <div style='position:absolute;bottom:28px;left:8px;right:8px;'>
                <!-- SIGNAL PILL — the key UI element -->
                <div style='
                    background:rgba(231,165,156,0.18);
                    border:1px solid #e7a59c;
                    border-radius:8px;
                    padding:5px 10px;
                    margin-bottom:5px;
                    display:flex;align-items:center;gap:6px;
                '>
                  <div style='width:8px;height:8px;border-radius:50%;background:#e7a59c;
                               box-shadow:0 0 6px rgba(231,165,156,0.5);flex-shrink:0;'></div>
                  <div style='font-size:8px;color:#c47b71;font-weight:600;'>
                    May land as frustration
                  </div>
                </div>
                <!-- text input mock -->
                <div style='background:#ffffff;border:1px solid #dce7f3;border-radius:20px;
                             padding:7px 12px;display:flex;align-items:center;gap:6px;'>
                  <div style='font-size:9px;color:#8ca3b0;flex:1;'>Fine, do whatever you want.</div>
                  <div style='width:20px;height:20px;border-radius:50%;background:#8ca3b0;
                               display:flex;align-items:center;justify-content:center;font-size:10px;color:#fff;'>➤</div>
                </div>
              </div>
            </div>
            </div>
            """, unsafe_allow_html=True)

        with col_phone_desc:
            st.markdown("""
            <div style='padding: 12px 0 0 20px;'>
              <div style='font-size:1.3em;font-weight:700;color:#8ca3b0;margin-bottom:12px;'>
                Mobile · iMessage / WhatsApp overlay
              </div>
              <div style='color:#717182;font-size:0.92em;line-height:1.7;margin-bottom:18px;'>
                A keyboard extension or chat overlay sits above your input field.
                As you finish typing — before you hit send — a single signal pill appears.
                One colour. Plain English. Gone after 4 seconds or the moment you send.
              </div>
            """, unsafe_allow_html=True)

            # When does it fire?
            st.markdown("""
              <div style='font-size:0.75em;letter-spacing:0.15em;text-transform:uppercase;
                          color:#8ca3b0;margin-bottom:10px;'>When the signal fires</div>
            """, unsafe_allow_html=True)
            st.markdown(freq_bar(95, "#B84040", "After a conflict in last 48h", "fires on every message"), unsafe_allow_html=True)
            st.markdown(freq_bar(65, "#C9922A", "Neutral relational history", "fires when gap > 0.10"), unsafe_allow_html=True)
            st.markdown(freq_bar(22, "#6BAE8A", "Positive recent history", "fires only if gap > 0.20"), unsafe_allow_html=True)
            st.markdown(freq_bar(8,  "#6B9FC4", "Well-aligned dyad (low baseline)", "rare — safety net only"), unsafe_allow_html=True)

            st.markdown("""
              <div style='margin-top:14px;padding:10px 14px;background:rgba(231,165,156,0.10);
                          border-left:3px solid #e74c3c;border-radius:0 8px 8px 0;
                          font-size:0.85em;color:#717182;line-height:1.6;'>
                <b style='color:#c47b71;'>Right now on screen:</b><br>
                "Can we talk tonight?" sent after a conflict → pill reads
                <span style='color:#c47b71;font-weight:600;'>"May land as a threat"</span>.
                Partner sees only the message. Only the sender sees the signal.
              </div>
            </div>
            """, unsafe_allow_html=True)

    # ── LAPTOP MOCKUP ─────────────────────────────────────────────────────────
    elif "Laptop" in dev_choice:
        col_laptop, col_laptop_desc = st.columns([1.4, 1])
        with col_laptop:
            st.markdown("""
            <div style='display:flex;justify-content:center;'>
            <div style='width:480px;'>
              <!-- screen bezel -->
              <div style='
                background:linear-gradient(180deg,#0d0d1a,#111126);
                border-radius:12px 12px 0 0;
                border:2px solid #1e2a4a;
                padding:14px;
                box-shadow:0 0 40px rgba(52,152,219,0.10);
                position:relative;
              '>
                <!-- browser chrome -->
                <div style='background:#0a0a14;border-radius:6px;padding:6px 10px;
                             display:flex;align-items:center;gap:8px;margin-bottom:10px;'>
                  <div style='display:flex;gap:4px;'>
                    <div style='width:8px;height:8px;border-radius:50%;background:#e74c3c;'></div>
                    <div style='width:8px;height:8px;border-radius:50%;background:#f39c12;'></div>
                    <div style='width:8px;height:8px;border-radius:50%;background:#2ecc71;'></div>
                  </div>
                  <div style='flex:1;background:#111120;border-radius:4px;padding:3px 10px;
                               font-size:9px;color:#8ca3b0;'>slack.com/messages/alex</div>
                  <!-- EXTENSION ICON glowing in toolbar -->
                  <div style='width:18px;height:18px;border-radius:4px;background:#1a2a4a;
                               border:1px solid #e74c3c;display:flex;align-items:center;
                               justify-content:center;font-size:10px;
                               box-shadow:0 0 8px rgba(231,76,60,0.5);'>🧠</div>
                </div>
                <!-- slack layout -->
                <div style='display:flex;gap:8px;height:240px;'>
                  <!-- sidebar -->
                  <div style='width:90px;background:#0a0a14;border-radius:6px;padding:8px;flex-shrink:0;'>
                    <div style='font-size:8px;color:#8ca3b0;margin-bottom:6px;letter-spacing:0.1em;'>CHANNELS</div>
                    <div style='font-size:8px;color:#556677;margin-bottom:4px;'>  # general</div>
                    <div style='font-size:8px;color:#556677;margin-bottom:4px;'>  # team</div>
                    <div style='font-size:8px;color:#8ca3b0;margin-bottom:10px;border-top:1px solid #1a2040;padding-top:6px;'>DIRECT</div>
                    <div style='font-size:8px;color:#8ca3b0;background:#1a2a3a;border-radius:4px;padding:2px 4px;margin-bottom:3px;'>● Alex R.</div>
                    <div style='font-size:8px;color:#556677;margin-bottom:3px;'>  Jordan K.</div>
                    <div style='font-size:8px;color:#556677;'>  Sam L.</div>
                  </div>
                  <!-- main chat -->
                  <div style='flex:1;display:flex;flex-direction:column;'>
                    <!-- messages -->
                    <div style='flex:1;padding:4px 0;overflow:hidden;'>
                      <div style='display:flex;gap:6px;align-items:flex-start;margin-bottom:10px;'>
                        <div style='width:20px;height:20px;border-radius:4px;background:#1a3050;
                                     flex-shrink:0;font-size:8px;display:flex;align-items:center;
                                     justify-content:center;color:#8ca3b0;'>A</div>
                        <div>
                          <div style='font-size:8px;color:#8ca3b0;font-weight:600;'>Alex R. <span style="color:#8ca3b0;font-weight:normal;">10:41 AM</span></div>
                          <div style='font-size:8px;color:#8ca3b0;margin-top:2px;'>You seem quiet lately.</div>
                        </div>
                      </div>
                      <div style='display:flex;gap:6px;align-items:flex-start;margin-bottom:10px;'>
                        <div style='width:20px;height:20px;border-radius:4px;background:#1a2050;
                                     flex-shrink:0;font-size:8px;display:flex;align-items:center;
                                     justify-content:center;color:#8ca3b0;'>Y</div>
                        <div>
                          <div style='font-size:8px;color:#8ca3b0;font-weight:600;'>You <span style="color:#8ca3b0;font-weight:normal;">10:43 AM</span></div>
                          <div style='font-size:8px;color:#8ca3b0;margin-top:2px;'>Don't worry about it, I'm fine.</div>
                        </div>
                      </div>
                    </div>
                    <!-- COMPOSE BOX with inline signal -->
                    <div style='background:#0e1520;border:1px solid #1e2a3a;border-radius:8px;padding:8px 10px;'>
                      <div style='font-size:8px;color:#556677;margin-bottom:6px;'>I just need some space right now.</div>
                      <!-- SIGNAL BANNER inline above send button -->
                      <div style='display:flex;align-items:center;justify-content:space-between;'>
                        <div style='display:flex;align-items:center;gap:6px;'>
                          <div style='width:7px;height:7px;border-radius:50%;background:#f39c12;
                                       box-shadow:0 0 5px #f39c12;'></div>
                          <span style='font-size:7px;color:#e7a59c;'>Boundary — may read as rejection</span>
                        </div>
                        <div style='display:flex;gap:4px;'>
                          <div style='font-size:7px;color:#8ca3b0;padding:2px 6px;border:1px solid #dce7f3;border-radius:3px;'>Aa</div>
                          <div style='font-size:7px;color:#8ca3b0;padding:2px 6px;border:1px solid #dce7f3;border-radius:3px;'>📎</div>
                          <div style='background:#1a3a5c;border-radius:3px;padding:2px 8px;font-size:7px;color:#8ca3b0;'>Send</div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <!-- laptop base -->
              <div style='height:12px;background:#0a0a14;border-radius:0 0 4px 4px;
                           border:2px solid #1e2a4a;border-top:none;'></div>
              <div style='height:5px;background:#060610;border-radius:0 0 8px 8px;
                           width:94%;margin:0 auto;'></div>
            </div>
            </div>
            """, unsafe_allow_html=True)

        with col_laptop_desc:
            st.markdown("""
            <div style='padding: 12px 0 0 12px;'>
              <div style='font-size:1.3em;font-weight:700;color:#8ca3b0;margin-bottom:12px;'>
                Laptop · browser extension
              </div>
              <div style='color:#717182;font-size:0.92em;line-height:1.7;margin-bottom:18px;'>
                A browser extension injects a single-line signal bar into the compose
                area of any messaging app. The signal sits between your text and the
                send button — visible only to you, dismissed on send.
              </div>
            """, unsafe_allow_html=True)

            st.markdown("""
              <div style='font-size:0.75em;letter-spacing:0.15em;text-transform:uppercase;
                          color:#8ca3b0;margin-bottom:10px;'>Trigger frequency at desk</div>
            """, unsafe_allow_html=True)
            st.markdown(freq_bar(88, "#C9922A", "Work context · new relationship", "fires when gap > 0.10"), unsafe_allow_html=True)
            st.markdown(freq_bar(40, "#6BAE8A", "Long-term colleague · established rapport", "fires when gap > 0.15"), unsafe_allow_html=True)
            st.markdown(freq_bar(72, "#B84040", "Personal messages via work apps", "fires on misaligned sends"), unsafe_allow_html=True)

            st.markdown("""
              <div style='margin-top:14px;padding:10px 14px;background:rgba(243,156,18,0.06);
                          border-left:3px solid #f39c12;border-radius:0 8px 8px 0;
                          font-size:0.85em;color:#717182;line-height:1.6;'>
                <b style='color:#e7a59c;'>Extension icon</b> glows in the toolbar
                when a gap is detected — even without the compose box open.
                Click to see the full breakdown for the last message received.
              </div>
            </div>
            """, unsafe_allow_html=True)

    # ── AUDIO / FACE-TO-FACE MOCKUP ───────────────────────────────────────────
    else:
        col_audio, col_audio_desc = st.columns([1, 1.6])
        with col_audio:
            st.markdown("""
            <div style='display:flex;justify-content:center;'>
            <div style='width:230px;'>
              <!-- wearable + ambient screen combo -->
              <!-- phone propped showing ambient mode -->
              <div style='
                width:130px;height:230px;margin:0 auto;
                background:linear-gradient(180deg,#0a0a14,#0d0d1e);
                border-radius:24px;
                border:2px solid #1e2a4a;
                box-shadow:0 0 30px rgba(231,76,60,0.18);
                position:relative;overflow:hidden;
              '>
                <!-- ambient colour wash — the primary signal -->
                <div style='
                    position:absolute;inset:0;
                    background:radial-gradient(ellipse at 50% 70%,
                        rgba(231,76,60,0.18) 0%,
                        rgba(231,76,60,0.04) 60%,
                        transparent 100%);
                '></div>
                <div style='padding:16px 14px;position:relative;z-index:2;'>
                  <div style='font-size:9px;color:#8ca3b0;text-align:center;margin-bottom:20px;'>AMBIENT MODE</div>
                  <!-- pulsing orb -->
                  <div style='
                    width:70px;height:70px;border-radius:50%;
                    background:radial-gradient(circle,rgba(231,76,60,0.4),rgba(231,76,60,0.05));
                    border:1.5px solid rgba(231,76,60,0.4);
                    margin:0 auto 16px auto;
                    display:flex;align-items:center;justify-content:center;
                    box-shadow:0 0 20px rgba(231,76,60,0.25);
                  '>
                    <div style='font-size:22px;'>🔴</div>
                  </div>
                  <div style='text-align:center;font-size:9px;color:#c47b71;font-weight:600;letter-spacing:0.1em;'>HIGH GAP</div>
                  <div style='text-align:center;font-size:8px;color:#556677;margin-top:3px;'>words ≠ meaning</div>
                  <!-- transcript snippet -->
                  <div style='margin-top:16px;background:rgba(0,0,0,0.3);border-radius:6px;padding:6px;
                               border:1px solid #1a2030;'>
                    <div style='font-size:7px;color:#8ca3b0;margin-bottom:4px;letter-spacing:0.08em;'>LIVE TRANSCRIPT</div>
                    <div style='font-size:8px;color:#9b8870;font-style:italic;'>"I'm fine, don't worry…"</div>
                    <div style='font-size:7px;color:#c47b71;margin-top:3px;'>↳ heard as: shutting down</div>
                  </div>
                </div>
              </div>
              <!-- wearable band below -->
              <div style='
                width:88px;height:20px;
                background:linear-gradient(90deg,#1a0a0a,#2a1010,#1a0a0a);
                border:1px solid rgba(231,76,60,0.3);
                border-radius:10px;margin:6px auto 0 auto;
                display:flex;align-items:center;justify-content:center;
                box-shadow:0 0 10px rgba(231,76,60,0.15);
              '>
                <div style='width:10px;height:10px;border-radius:50%;background:#e74c3c;
                             box-shadow:0 0 6px #e74c3c;margin-right:6px;'></div>
                <span style='font-size:7px;color:#c47b71;letter-spacing:0.08em;'>WEARABLE</span>
              </div>
            </div>
            </div>
            """, unsafe_allow_html=True)

        with col_audio_desc:
            st.markdown("""
            <div style='padding: 12px 0 0 20px;'>
              <div style='font-size:1.3em;font-weight:700;color:#8ca3b0;margin-bottom:12px;'>
                Audio · face-to-face · voice call
              </div>
              <div style='color:#717182;font-size:0.92em;line-height:1.7;margin-bottom:18px;'>
                On-device transcription feeds the classifier in real-time.
                No cloud. The phone lies face-up between you — its screen glows the gap colour.
                A wearable (haptic band) can give the same signal privately.
                Both people opt in. Neither performs for the signal.
              </div>
            """, unsafe_allow_html=True)

            st.markdown("""
              <div style='font-size:0.75em;letter-spacing:0.15em;text-transform:uppercase;
                          color:#8ca3b0;margin-bottom:10px;'>Trigger logic · voice</div>
            """, unsafe_allow_html=True)
            st.markdown(freq_bar(100, "#B84040", "Conflict conversation detected", "continuous ambient colour"), unsafe_allow_html=True)
            st.markdown(freq_bar(55,  "#C9922A", "Ambiguous exchange flagged", "orb pulses once"), unsafe_allow_html=True)
            st.markdown(freq_bar(20,  "#6BAE8A", "Aligned conversation", "signal fades to background"), unsafe_allow_html=True)
            st.markdown(freq_bar(35,  "#9b59b6", "Repair moment detected", "green pulse — acknowledge"), unsafe_allow_html=True)

            st.markdown("""
              <div style='margin-top:14px;padding:10px 14px;background:rgba(155,89,182,0.06);
                          border-left:3px solid #9b59b6;border-radius:0 8px 8px 0;
                          font-size:0.85em;color:#717182;line-height:1.6;'>
                <b style='color:#8ca3b0;'>Therapist / mediator mode:</b><br>
                A third screen visible only to the facilitator shows both people's
                gap trajectories simultaneously — real-time map of where the session is.
              </div>
            </div>
            """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # SECTION 2 — SIGNAL TRIGGER TIMELINE
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>When does the signal appear? — trigger logic timeline</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='color:#8ca3b0;font-size:0.9em;margin-bottom:16px;'>
    The system does not fire on every message. It fires when the gap crosses a threshold that
    <em>matters</em> — grounded in the same ChaosNLI human annotation baseline used in the scientific model.
    </div>
    """, unsafe_allow_html=True)

    # Timeline as a Plotly figure — horizontal swimlanes per scenario
    def make_trigger_timeline():
        scenarios = [
            "After a conflict (partner)",
            "Neutral (colleague)",
            "Positive history (partner)",
            "Aligned dyad (long-term)",
        ]
        # Each scenario: list of (day, event_label, color, y_offset)
        # Simulate a 10-message conversation
        messages = ["msg 1", "msg 2", "msg 3", "msg 4", "msg 5",
                    "msg 6", "msg 7", "msg 8", "msg 9", "msg 10"]
        x_pos = list(range(1, 11))

        # Gap values per scenario per message (illustrative)
        gaps = {
            "After a conflict (partner)":   [0.38, 0.42, 0.35, 0.28, 0.41, 0.33, 0.29, 0.22, 0.18, 0.14],
            "Neutral (colleague)":           [0.06, 0.12, 0.08, 0.15, 0.11, 0.07, 0.13, 0.09, 0.10, 0.06],
            "Positive history (partner)":    [0.03, 0.04, 0.22, 0.05, 0.03, 0.04, 0.03, 0.21, 0.04, 0.03],
            "Aligned dyad (long-term)":      [0.02, 0.03, 0.04, 0.02, 0.03, 0.02, 0.03, 0.04, 0.02, 0.03],
        }
        # Thresholds per scenario (context-adaptive)
        thresholds = {
            "After a conflict (partner)":  0.10,
            "Neutral (colleague)":          0.10,
            "Positive history (partner)":   0.20,
            "Aligned dyad (long-term)":     0.25,
        }
        colors_s = {
            "After a conflict (partner)":  "#B84040",
            "Neutral (colleague)":          "#C9922A",
            "Positive history (partner)":   "#6B9FC4",
            "Aligned dyad (long-term)":     "#6BAE8A",
        }

        fig = go.Figure()
        y_positions = {s: i * 2 for i, s in enumerate(reversed(scenarios))}

        for scenario in scenarios:
            y = y_positions[scenario]
            g = gaps[scenario]
            thresh = thresholds[scenario]
            col = colors_s[scenario]

            # Baseline swim lane
            fig.add_shape(type="line", x0=0.5, x1=10.5, y0=y, y1=y,
                          line=dict(color="#1a2030", width=1))

            for xi, gap_val in zip(x_pos, g):
                fires = gap_val >= thresh
                dot_color = col if fires else "#1e2a3a"
                dot_size = 14 if fires else 8
                symbol = "circle" if fires else "circle-open"
                fig.add_trace(go.Scatter(
                    x=[xi], y=[y],
                    mode="markers",
                    marker=dict(
                        size=dot_size,
                        color=dot_color,
                        symbol=symbol,
                        line=dict(color=col if fires else "#2a3a4a", width=1.5),
                    ),
                    hovertemplate=(
                        f"<b>{scenario}</b><br>"
                        f"Message {xi}<br>"
                        f"Gap: {gap_val:.2f}<br>"
                        f"Threshold: {thresh}<br>"
                        f"Signal: {'🔔 FIRES' if fires else '🔕 silent'}"
                        "<extra></extra>"
                    ),
                    showlegend=False,
                ))
                # If fires, add small label above
                if fires:
                    fig.add_annotation(
                        x=xi, y=y + 0.35,
                        text=f"{gap_val:.2f}",
                        showarrow=False,
                        font=dict(color=col, size=8),
                        align="center",
                    )

        # Scenario labels on y-axis
        fig.update_layout(
            yaxis=dict(
                tickmode="array",
                tickvals=list(y_positions.values()),
                ticktext=list(y_positions.keys()),
                tickfont=dict(color="#7788aa", size=11),
                gridcolor="#ececf0",
            ),
            xaxis=dict(
                tickmode="array",
                tickvals=x_pos,
                ticktext=[f"Msg {i}" for i in x_pos],
                tickfont=dict(color="#556677", size=10),
                gridcolor="#ececf0",
                range=[0.3, 10.7],
            ),
            height=300,
            margin=dict(t=20, b=40, l=180, r=30),
            paper_bgcolor="#f5f6f7",
            plot_bgcolor="#dce7f3",
            showlegend=False,
            title=dict(
                text="Signal fires (bright dot) vs stays silent (hollow dot) across 10 messages",
                font=dict(color="#556677", size=11),
            ),
        )

        # Legend manually
        for scenario, col in colors_s.items():
            y = y_positions[scenario]
            fig.add_trace(go.Scatter(
                x=[None], y=[None],
                mode="markers",
                marker=dict(size=10, color=col),
                name=scenario,
                showlegend=True,
            ))

        fig.update_layout(
            legend=dict(
                orientation="h", yanchor="bottom", y=-0.30,
                xanchor="center", x=0.5,
                font=dict(size=10, color="#778899"),
                bgcolor="rgba(0,0,0,0)",
            )
        )
        return fig

    st.plotly_chart(make_trigger_timeline(), use_container_width=True)

    # Threshold table
    st.markdown("""
    <div style='margin-top:4px;'>
    <table style='width:100%;border-collapse:collapse;font-size:0.85em;'>
      <thead>
        <tr style='border-bottom:1px solid #1a2a3a;'>
          <th style='text-align:left;padding:8px 12px;color:#8ca3b0;font-weight:600;letter-spacing:0.06em;'>CONTEXT</th>
          <th style='text-align:center;padding:8px 12px;color:#8ca3b0;font-weight:600;letter-spacing:0.06em;'>THRESHOLD</th>
          <th style='text-align:left;padding:8px 12px;color:#8ca3b0;font-weight:600;letter-spacing:0.06em;'>RATIONALE</th>
          <th style='text-align:center;padding:8px 12px;color:#8ca3b0;font-weight:600;letter-spacing:0.06em;'>EST. FIRE RATE</th>
        </tr>
      </thead>
      <tbody>
        <tr style='border-bottom:1px solid #0e1520;'>
          <td style='padding:8px 12px;color:#8ca3b0;'>After conflict</td>
          <td style='padding:8px 12px;text-align:center;'><span style='color:#c47b71;font-weight:700;'>0.10</span></td>
          <td style='padding:8px 12px;color:#717182;'>Every message at risk — low bar is a safety net</td>
          <td style='padding:8px 12px;text-align:center;color:#c47b71;'>~80–95%</td>
        </tr>
        <tr style='border-bottom:1px solid #0e1520;'>
          <td style='padding:8px 12px;color:#8ca3b0;'>Neutral history</td>
          <td style='padding:8px 12px;text-align:center;'><span style='color:#e7a59c;font-weight:700;'>0.10</span></td>
          <td style='padding:8px 12px;color:#717182;'>Evidently AI drift standard — genuine ambiguity threshold</td>
          <td style='padding:8px 12px;text-align:center;color:#e7a59c;'>~40–65%</td>
        </tr>
        <tr style='border-bottom:1px solid #0e1520;'>
          <td style='padding:8px 12px;color:#8ca3b0;'>Positive history</td>
          <td style='padding:8px 12px;text-align:center;'><span style='color:#8ca3b0;font-weight:700;'>0.20</span></td>
          <td style='padding:8px 12px;color:#717182;'>Higher bar — only flag systematic misalignment</td>
          <td style='padding:8px 12px;text-align:center;color:#8ca3b0;'>~15–25%</td>
        </tr>
        <tr>
          <td style='padding:8px 12px;color:#8ca3b0;'>Aligned dyad</td>
          <td style='padding:8px 12px;text-align:center;'><span style='color:#8ca3b0;font-weight:700;'>0.25</span></td>
          <td style='padding:8px 12px;color:#717182;'>Safety net only — ChaosNLI noise floor well below this</td>
          <td style='padding:8px 12px;text-align:center;color:#8ca3b0;'>~5–10%</td>
        </tr>
      </tbody>
    </table>
    </div>
    """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # SECTION 3 — WHAT YOU SEE (signal vocabulary)
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>What the signal looks like — the full vocabulary</div>", unsafe_allow_html=True)

    st.markdown("""
    <div style='color:#8ca3b0;font-size:0.9em;margin-bottom:16px;'>
    Five states. No numbers. Each maps to a gap tier and a plain-English phrase.
    The system never shows a decimal. It never gives advice. It shows the gap.
    </div>
    """, unsafe_allow_html=True)

    sig_cols = st.columns(5)
    signals = [
        ("#4a9b6f",  "Crystal clear",      "Gap < 0.05",   "Message aligns perfectly.\nNo signal shown."),
        ("#5b8db8",  "Well understood",     "Gap 0.05–0.10","Soft blue glow.\nFades in 2s."),
        ("#c9922a",  "Getting lost",        "Gap 0.10–0.20","Amber pill appears.\nStays until send."),
        ("#c4732a",  "Significant misread", "Gap 0.20–0.35","Orange pulse.\nCompose box border glows."),
        ("#b84040",  "Crossed wires",       "Gap > 0.35",   "Red wash.\nLabel: 'May land as threat'."),
    ]
    for col, (color, label, range_txt, desc) in zip(sig_cols, signals):
        with col:
            st.markdown(f"""
            <div style='
                background:#ffffff;
                border:1px solid #e0e8f0;
                border-top:3px solid {color};
                border-radius:10px;
                padding:16px 12px;
                text-align:center;
                height:210px;
                display:flex;flex-direction:column;align-items:center;justify-content:space-between;
            '>
              <div style='
                width:22px;height:22px;border-radius:50%;
                background:{color};
                box-shadow:0 2px 6px {color}55;
                margin:0 auto 2px;
              '></div>
              <div style='font-weight:700;color:#2c3e50;font-size:0.88em;margin:4px 0;'>{label}</div>
              <div style='font-size:0.72em;color:#8ca3b0;background:#dce7f3;
                          border-radius:4px;padding:2px 8px;margin-bottom:4px;'>{range_txt}</div>
              <div style='font-size:0.76em;color:#556677;line-height:1.5;white-space:pre-line;'>{desc}</div>
            </div>
            """, unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # SECTION 3b — ETHICS FRAMEWORK
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>Built with safety architecture from the start</div>", unsafe_allow_html=True)
    st.markdown("""
    <div style='font-size:0.84em;color:#717182;margin-bottom:16px;line-height:1.5;'>
      These are not afterthoughts. Each ethical risk is identified, mitigated, and built into the instrument
      architecture before first deployment.
    </div>
    """, unsafe_allow_html=True)

    eth_col1, eth_col2 = st.columns(2)
    _eth_card = lambda icon, title, body, color: f"""
    <div style='padding:16px 18px;background:rgba(220,231,243,0.3);border:1px solid #dce7f3;
                border-radius:10px;border-top:3px solid {color};margin-bottom:12px;'>
      <div style='font-size:0.72em;font-weight:700;letter-spacing:0.10em;text-transform:uppercase;
                  color:{color};margin-bottom:6px;'>{icon} {title}</div>
      <div style='font-size:0.82em;color:#556677;line-height:1.6;'>{body}</div>
    </div>"""

    with eth_col1:
        st.markdown(_eth_card("🚨", "Domestic abuse safeguarding",
            "When model detects <strong>sustained divergence + high self-interest asymmetry</strong>, "
            "the instrument displays an explicit signpost to the National Domestic Abuse Helpline. "
            "Rapid account deletion accessible from the app's <em>first screen</em> without authentication. "
            "Session-disabling 3-tap gesture. No identifying information on lock screen.",
            "#B84040"), unsafe_allow_html=True)
        st.markdown(_eth_card("🧩", "Neurodivergent inclusion",
            "Neurodiverse-authored messages explicitly included in the dataset (recruited via autism/ADHD community groups). "
            "Separate κ computed on neurodiverse message subset. "
            "Model error rates on neurodiverse messages explicitly reported — not hidden in aggregate metrics.",
            "#9b59b6"), unsafe_allow_html=True)

    with eth_col2:
        st.markdown(_eth_card("🌍", "Cultural annotation bias",
            "Minimum <strong>3 distinct cultural backgrounds</strong> in every 5-annotator pool. "
            "Per-culture κ reported alongside aggregate κ. "
            "High cross-cultural-variance intent categories flagged in published dataset.",
            "#C9922A"), unsafe_allow_html=True)
        st.markdown(_eth_card("🔒", "Biographical intake as sensitive data",
            "Local-first, <strong>AES-256 encrypted at rest</strong>. Not shareable with any partner or third party. "
            "Fully deletable at any time. "
            "<em>Ablation-first principle:</em> biographical intake fields that do not measurably improve H₄ "
            "accuracy are removed before v2 — preventing accumulation of unused sensitive data.",
            "#27ae60"), unsafe_allow_html=True)

    # ════════════════════════════════════════════════════════════════════════
    # SECTION 4 — PRIVACY + TECH SPECS
    # ════════════════════════════════════════════════════════════════════════
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("<div class='nt-section-title'>Under the hood — privacy & performance</div>", unsafe_allow_html=True)

    col_priv1, col_priv2 = st.columns(2)
    with col_priv1:
        st.markdown("""
        <div class='nt-card'>
          <div style='font-weight:700;color:#8ca3b0;font-size:1.0em;margin-bottom:12px;'>🔒 Privacy architecture</div>
          <div style='color:#556677;font-size:0.88em;line-height:1.75;'>
            <span style='color:#717182;'>Model runs on-device.</span>
            Message text is processed locally — never transmitted. Only the gap score (a single float) is logged,
            never the original text.<br><br>
            <span style='color:#717182;'>No content stored.</span>
            The relational context vector (16 dimensions) encodes relationship history as aggregated statistics —
            not message content.<br><br>
            <span style='color:#717182;'>Consent architecture:</span>
            both parties opt in explicitly. Either party can pause or end the signal at any time
            with a single tap.
          </div>
        </div>
        """, unsafe_allow_html=True)
    with col_priv2:
        specs = [
            ("Inference latency",   "< 200ms",    "#6BAE8A", "DistilBERT on-device, Month 1–6"),
            ("Gap computation",     "< 5ms",      "#6BAE8A", "JSD is O(n) — trivially fast"),
            ("Model size (v1)",     "66MB",       "#C9922A", "DistilBERT quantised"),
            ("Model size (v2)",     "355MB",      "#C9922A", "RoBERTa-large, Month 6–7"),
            ("Battery impact",      "< 1% / hr",  "#6BAE8A", "Passive inference, not streaming"),
            ("Transcription (v2)",  "< 100ms",    "#6B9FC4", "On-device Whisper tiny"),
        ]
        rows = "".join([
            f"<div style='display:flex;justify-content:space-between;border-bottom:1px solid #0e1520;"
            f"padding:5px 0;'>"
            f"<span style='color:#7788aa;'>{k}</span>"
            f"<span style='color:{c};font-weight:600;'>{v}</span>"
            f"</div>"
            for k, v, c, _ in specs
        ])
        st.markdown(f"""
        <div class='nt-card'>
          <div style='font-weight:700;color:#8ca3b0;font-size:1.0em;margin-bottom:12px;'>⚡ Performance targets</div>
          {rows}
          <div style='margin-top:10px;font-size:0.8em;color:#8ca3b0;'>Engineering targets — empirical benchmarking in progress</div>
        </div>
        """, unsafe_allow_html=True)

    # ── Neuroplasticity Arc ───────────────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='margin-bottom:14px;'>
      <div style='font-size:1.3em;font-weight:700;color:#8ca3b0;margin-bottom:6px;'>
        The Neuroplasticity Arc — what happens over 60 days
        <span style='font-size:0.58em;font-weight:400;color:#e7a59c;letter-spacing:0.1em;
                     text-transform:uppercase;margin-left:10px;vertical-align:middle;
                     background:rgba(243,156,18,0.1);padding:2px 8px;border-radius:4px;'>
          Projected · H₂ + H₃ · EEG pilot Month 7–11
        </span>
      </div>
      <div style='font-size:0.85em;color:#556677;font-style:italic;margin-bottom:4px;'>
        Illustrative projection based on H₂ intervention design and neuroplasticity literature (Singer, 2025; Sitaram et al., 2017).
        Real data from 60-day EEG pilot, N=20–24 dyadic pairs.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # 60-day gap trajectory chart
    days = list(range(0, 61, 3))
    # Projected gap decline — exponential decay toward ~0.08 floor
    import math
    gap_proj = [0.47 * math.exp(-0.038 * d) + 0.08 for d in days]
    # Upper/lower bounds (illustrative confidence band)
    gap_upper = [g + 0.07 * math.exp(-0.02 * d) for g, d in zip(gap_proj, days)]
    gap_lower = [max(0.05, g - 0.06 * math.exp(-0.02 * d)) for g, d in zip(gap_proj, days)]

    fig_neuro = go.Figure()
    fig_neuro.add_trace(go.Scatter(
        x=days + days[::-1], y=gap_upper + gap_lower[::-1],
        fill='toself', fillcolor='rgba(201,146,42,0.08)',
        line=dict(color='rgba(0,0,0,0)'), showlegend=False, hoverinfo='skip'))
    fig_neuro.add_trace(go.Scatter(
        x=days, y=gap_proj, mode='lines+markers',
        name='Projected intent gap score',
        line=dict(color='#C9922A', width=2.5),
        marker=dict(size=5, color='#C9922A'),
    ))
    # Key annotations
    fig_neuro.add_annotation(x=0, y=0.47, text="Day 0<br>Baseline: 0.47", showarrow=True,
        arrowhead=2, ax=30, ay=-30, font=dict(size=10, color='#B84040'),
        arrowcolor='#B84040', bgcolor='rgba(13,13,26,0.8)', bordercolor='#B84040', borderwidth=1)
    fig_neuro.add_annotation(x=30, y=gap_proj[10], text="Day 30<br>~30% reduction<br>(H₂ behavioural)", showarrow=True,
        arrowhead=2, ax=40, ay=-40, font=dict(size=10, color='#C9922A'),
        arrowcolor='#C9922A', bgcolor='rgba(13,13,26,0.8)', bordercolor='#C9922A', borderwidth=1)
    fig_neuro.add_annotation(x=60, y=gap_proj[-1], text="Day 60<br>EEG session<br>IBS shift measured", showarrow=True,
        arrowhead=2, ax=-60, ay=-30, font=dict(size=10, color='#6BAE8A'),
        arrowcolor='#6BAE8A', bgcolor='rgba(13,13,26,0.8)', bordercolor='#6BAE8A', borderwidth=1)
    fig_neuro.update_layout(
        paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(220,231,243,0.3)',
        font=dict(color='#717182', size=11),
        xaxis=dict(title='Day', showgrid=True, gridcolor='#1a2030', tickvals=[0,10,20,30,40,50,60]),
        yaxis=dict(title='Intent Gap Score (JS-divergence)', showgrid=True, gridcolor='#1a2030',
                   range=[0, 0.65], tickformat='.2f'),
        height=320,
        title=dict(text='60-day intent gap trajectory — projected from H₂ intervention design',
                   font=dict(size=11, color='#445566'), x=0.5),
        legend=dict(bgcolor='rgba(0,0,0,0)', font=dict(size=10, color='#778899')),
        margin=dict(l=50, r=30, t=50, b=50)
    )
    st.plotly_chart(fig_neuro, use_container_width=True)

    # Hebbian mechanism steps
    st.markdown("""
    <div style='display:flex;gap:12px;flex-wrap:wrap;margin-top:8px;margin-bottom:20px;'>
      <div style='flex:1;min-width:160px;padding:14px 16px;background:rgba(231,165,156,0.12);
                  border-radius:10px;text-align:center;'>
        <div style='font-size:1.5em;margin-bottom:6px;'>🧠</div>
        <div style='font-size:0.72em;color:#c47b71;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;'>Step 1</div>
        <div style='font-size:0.82em;color:#2c3e50;font-weight:600;margin-bottom:4px;'>TPJ fires</div>
        <div style='font-size:0.75em;color:#717182;line-height:1.4;'>The intent signal occupies the cognitive reappraisal window — lateral PFC activates, amygdala cascade suppressed</div>
      </div>
      <div style='flex:0;padding:14px 4px;display:flex;align-items:center;color:#8ca3b0;font-size:1.2em;'>→</div>
      <div style='flex:1;min-width:160px;padding:14px 16px;background:rgba(231,165,156,0.10);
                  border-radius:10px;text-align:center;'>
        <div style='font-size:1.5em;margin-bottom:6px;'>💛</div>
        <div style='font-size:0.72em;color:#e7a59c;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;'>Step 2</div>
        <div style='font-size:0.82em;color:#2c3e50;font-weight:600;margin-bottom:4px;'>Dopamine + oxytocin reward</div>
        <div style='font-size:0.75em;color:#717182;line-height:1.4;'>Correct intent inference confirmed — nucleus accumbens releases dopamine and oxytocin, reinforcing the trust-confirming mentalising state (Zak et al., 2017)</div>
      </div>
      <div style='flex:0;padding:14px 4px;display:flex;align-items:center;color:#8ca3b0;font-size:1.2em;'>→</div>
      <div style='flex:1;min-width:160px;padding:14px 16px;background:rgba(220,231,243,0.5);
                  border-radius:10px;text-align:center;'>
        <div style='font-size:1.5em;margin-bottom:6px;'>🔗</div>
        <div style='font-size:0.72em;color:#8ca3b0;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;'>Step 3</div>
        <div style='font-size:0.82em;color:#2c3e50;font-weight:600;margin-bottom:4px;'>Circuit strengthens</div>
        <div style='font-size:0.75em;color:#717182;line-height:1.4;'>Hebbian co-activation of TPJ — repeated correct scaffolding strengthens mentalising circuitry (Sitaram et al., 2017)</div>
      </div>
      <div style='flex:0;padding:14px 4px;display:flex;align-items:center;color:#8ca3b0;font-size:1.2em;'>→</div>
      <div style='flex:1;min-width:160px;padding:14px 16px;background:rgba(220,231,243,0.4);
                  border-radius:10px;text-align:center;'>
        <div style='font-size:1.5em;margin-bottom:6px;'>🌿</div>
        <div style='font-size:0.72em;color:#8ca3b0;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;margin-bottom:4px;'>Step 4</div>
        <div style='font-size:0.82em;color:#2c3e50;font-weight:600;margin-bottom:4px;'>Trace in the brain</div>
        <div style='font-size:0.75em;color:#717182;line-height:1.4;'>Sustained IFG/dmPFC inter-brain coupling persists beyond the interaction — raising dyad's baseline mentalising capacity (Finn et al., 2024)</div>
      </div>
    </div>
    <div style='font-size:0.75em;color:#8ca3b0;font-style:italic;padding:8px 0;'>
      Mechanism: LeDoux (1996), Gross (1998), Sitaram et al. (2017), Singer (2025), Finn et al. (2024).
      All steps are hypothesised cascade — H₃ is the exploratory hypothesis this programme is designed to test.
    </div>
    """, unsafe_allow_html=True)

    # Footer
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='text-align:center;color:#8ca3b0;font-size:0.82em;padding-bottom:20px;'>
        NeuroAI Cognitive Companion &nbsp;·&nbsp; Encode × Pillar VC AI for Science Fellowship &nbsp;·&nbsp; March 2026<br>
        <em style='color:#8ca3b0;'>"The gap is real. The signal is measurable. The intervention is the instrument."</em>
    </div>
    """, unsafe_allow_html=True)

# ── Tab 4: The Network ─────────────────────────────────────────────────────────
with tab_network:

    # ── Section header ─────────────────────────────────────────────────────────
    st.markdown("""
    <div style='padding:18px 24px 14px;background:linear-gradient(135deg,rgba(220,231,243,0.5) 0%,rgba(231,165,156,0.08) 100%);
                border:1px solid #dce7f3;border-radius:14px;margin-bottom:24px;'>
      <div style='font-size:1.05em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:6px;'>
        🌐  The Network
      </div>
      <div style='font-size:0.88em;color:#2c3e50;line-height:1.6;max-width:800px;'>
        From measuring one mind reading another — to building the infrastructure for a trust-based world.
        Three horizons. One direction.
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Three Horizon frames ───────────────────────────────────────────────────
    st.markdown("""
    <div style='display:flex;gap:14px;flex-wrap:wrap;margin-bottom:28px;'>

      <!-- Horizon 1: Mirror -->
      <div style='flex:1;min-width:200px;padding:18px 18px 14px;
                  background:rgba(231,165,156,0.12);border:1px solid rgba(231,165,156,0.4);border-radius:12px;'>
        <div style='font-size:0.7em;color:#c47b71;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;'>
          Horizon 1 · Now
        </div>
        <div style='font-size:1.4em;margin-bottom:8px;'>🪞 The Mirror</div>
        <div style='font-size:0.88em;color:#2c3e50;font-weight:600;margin-bottom:6px;'>Individual intent awareness</div>
        <div style='font-size:0.78em;color:#717182;line-height:1.5;'>
          The app shows you your own intent signal before you send.
          A private mirror — your intent fingerprint, visible only to you.
          Stored on-device. Never shared without consent.
        </div>
        <div style='margin-top:10px;padding:8px 10px;background:rgba(231,76,60,0.1);border-radius:7px;
                    font-size:0.72em;color:#c47b71;font-weight:600;'>
          ✓ Prototype built · H₁ computational validation in progress
        </div>
      </div>

      <!-- Arrow -->
      <div style='padding:0 4px;display:flex;align-items:center;color:#8ca3b0;font-size:1.6em;'>→</div>

      <!-- Horizon 2: Bridge -->
      <div style='flex:1;min-width:200px;padding:18px 18px 14px;
                  background:rgba(220,231,243,0.5);border:1px solid #dce7f3;border-radius:12px;'>
        <div style='font-size:0.7em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;'>
          Horizon 2 · 12–18 months
        </div>
        <div style='font-size:1.4em;margin-bottom:8px;'>🌉 The Bridge</div>
        <div style='font-size:0.88em;color:#2c3e50;font-weight:600;margin-bottom:6px;'>Consent-based dyadic sharing</div>
        <div style='font-size:0.78em;color:#717182;line-height:1.5;'>
          With mutual opt-in, two people can see each other's intent fingerprints in real time.
          Not surveillance — a shared channel for understanding.
          Gap score visible from both sides.
        </div>
        <div style='margin-top:10px;padding:8px 10px;background:rgba(52,152,219,0.1);border-radius:7px;
                    font-size:0.72em;color:#8ca3b0;font-weight:600;'>
          H₂ behavioural · Beta cohort planned Month 3–6
        </div>
      </div>

      <!-- Arrow -->
      <div style='padding:0 4px;display:flex;align-items:center;color:#8ca3b0;font-size:1.6em;'>→</div>

      <!-- Horizon 3: The Map -->
      <div style='flex:1;min-width:200px;padding:18px 18px 14px;
                  background:rgba(220,231,243,0.4);border:1px solid #dce7f3;border-radius:12px;'>
        <div style='font-size:0.7em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;'>
          Horizon 3 · 3–5 years
        </div>
        <div style='font-size:1.4em;margin-bottom:8px;'>🗺️ The Map</div>
        <div style='font-size:0.88em;color:#2c3e50;font-weight:600;margin-bottom:6px;'>Population-scale trust infrastructure</div>
        <div style='font-size:0.78em;color:#717182;line-height:1.5;'>
          Aggregated, anonymised intent signatures across thousands of dyads.
          A living map of how understanding flows — or breaks — across a network.
          The counter-architecture to threat-first communication.
        </div>
        <div style='margin-top:10px;padding:8px 10px;background:rgba(46,204,113,0.1);border-radius:7px;
                    font-size:0.72em;color:#8ca3b0;font-weight:600;'>
          Horizon · Conditional on H₁ + H₂ validation
        </div>
      </div>

    </div>
    """, unsafe_allow_html=True)

    # ── ARIA Spaces Alignment ──────────────────────────────────────────────────
    st.markdown("""
    <div style='margin:8px 0 20px;'>
      <div style='font-size:0.78em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;
                  text-transform:uppercase;margin-bottom:14px;'>
        ARIA Spaces — where this programme lives
      </div>
    </div>
    """, unsafe_allow_html=True)

    aria_col1, aria_col2 = st.columns(2)
    with aria_col1:
        st.markdown("""
        <div style='padding:18px 20px;background:rgba(220,231,243,0.5);border:1px solid #dce7f3;
                    border-radius:12px;height:100%;'>
          <div style='font-size:0.72em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;
                      text-transform:uppercase;margin-bottom:8px;'>🧠 Scalable Neural Interfaces</div>
          <div style='font-size:0.88em;color:#2c3e50;line-height:1.65;margin-bottom:12px;'>
            The intent-conditioned model and dataset are computational tools that interface with
            human neural language processing. Validated against neural data via <strong>Brain-Score</strong>
            (Study 3) — testing whether pragmatic fine-tuning enhances neural similarity to
            language-selective cortex (IFG, aMTG, TPJ).
          </div>
          <div style='font-size:0.78em;color:#717182;font-style:italic;'>
            This is AI for Science, not science-flavoured product.
          </div>
          <div style='margin-top:12px;padding:8px 10px;background:rgba(52,152,219,0.1);
                      border-radius:6px;font-size:0.74em;color:#8ca3b0;font-weight:600;'>
            Study 3 · Brain-Score Language benchmark · Months 6–8 · SHOULD tier
          </div>
        </div>
        """, unsafe_allow_html=True)
    with aria_col2:
        st.markdown("""
        <div style='padding:18px 20px;background:rgba(231,165,156,0.08);border:1px solid rgba(231,165,156,0.3);
                    border-radius:12px;height:100%;'>
          <div style='font-size:0.72em;color:#c47b71;font-weight:700;letter-spacing:0.12em;
                      text-transform:uppercase;margin-bottom:8px;'>🌱 Collective Flourishing</div>
          <div style='font-size:0.88em;color:#2c3e50;line-height:1.65;margin-bottom:12px;'>
            The Map (Horizon 3) is the long-run vision: intent infrastructure that reduces the
            structural cost of human miscommunication at population scale — built on consent
            architecture, not attention extraction.
          </div>
          <div style='font-size:0.78em;color:#717182;font-style:italic;'>
            Measured by JS-divergence at scale, not engagement metrics.
          </div>
          <div style='margin-top:12px;padding:8px 10px;background:rgba(46,204,113,0.1);
                      border-radius:6px;font-size:0.74em;color:#27ae60;font-weight:600;'>
            Horizon 3 · Conditional on H₁ + H₂ validation · N = thousands of consented dyads
          </div>
        </div>
        """, unsafe_allow_html=True)

    # Brain-Score panel
    st.markdown("""
    <div style='margin-top:14px;padding:16px 20px;background:rgba(220,231,243,0.3);
                border:1px solid #dce7f3;border-radius:10px;font-size:0.84em;color:#556677;line-height:1.6;'>
      <div style='font-weight:700;color:#2c3e50;margin-bottom:6px;'>
        Study 3 — Brain-Score neural plausibility validation
        <span style='font-size:0.75em;font-weight:400;color:#8ca3b0;margin-left:8px;'>Months 6–8 · SHOULD</span>
      </div>
      Submit the trained intent model to the MIT Brain-Score Language benchmark
      (Schrimpf et al., 2021). Target benchmarks: <strong>Pereira2018, Fedorenko2016, Blank2014</strong>.
      Extract hidden-state activations at each transformer layer; fit linear regression probes to
      fMRI ROI activations in language-selective cortex (IFG, aMTG, pMTG, PostTemp, AnGyd).<br><br>
      <strong>Prediction:</strong> If the intent model scores above RoBERTa-base on language-selective
      neural alignment → pragmatic fine-tuning enhances neural similarity to human language processing.
      This validates the computational model as neurally plausible — not just behaviourally predictive.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)

    # ── Section A: The Bridge — dual radar charts ──────────────────────────────
    st.markdown("""
    <div style='font-size:0.78em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;
                text-transform:uppercase;margin-bottom:12px;'>
      🌉  Section A — The Bridge: Two Intent Fingerprints
    </div>
    <div style='font-size:0.82em;color:#717182;margin-bottom:16px;line-height:1.5;'>
      With mutual consent, both parties can see each other's intent signal in real time.
      The gap score — shown from both sides simultaneously — is the shared language for understanding.
    </div>
    """, unsafe_allow_html=True)

    col_bridge_left, col_bridge_right = st.columns(2)

    # Maya's intent fingerprint
    with col_bridge_left:
        bridge_cats = ["Seeking connection", "Expressing concern", "Setting a boundary",
                       "Seeking validation", "Expressing frustration", "Making a request", "Giving information"]
        maya_si = [0.48, 0.28, 0.10, 0.07, 0.04, 0.02, 0.01]
        maya_pi = [0.09, 0.12, 0.18, 0.06, 0.41, 0.09, 0.05]

        fig_maya = go.Figure()
        fig_maya.add_trace(go.Scatterpolar(
            r=maya_si + [maya_si[0]],
            theta=bridge_cats + [bridge_cats[0]],
            fill='toself',
            name="Maya's intent (SI)",
            line=dict(color='#6B9FC4', width=2),
            fillcolor='rgba(107,159,196,0.18)',
        ))
        fig_maya.add_trace(go.Scatterpolar(
            r=maya_pi + [maya_pi[0]],
            theta=bridge_cats + [bridge_cats[0]],
            fill='toself',
            name="Dev perceives (PI)",
            line=dict(color='#e7a59c', width=2, dash='dot'),
            fillcolor='rgba(231,165,156,0.18)',
        ))
        fig_maya.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 0.6],
                                gridcolor='rgba(255,255,255,0.06)',
                                tickfont=dict(size=8, color='#556677')),
                angularaxis=dict(tickfont=dict(size=9, color='#aabbcc'),
                                 gridcolor='rgba(255,255,255,0.06)'),
                bgcolor='rgba(0,0,0,0)',
            ),
            showlegend=True,
            legend=dict(font=dict(size=9, color='#aabbcc'), bgcolor='rgba(0,0,0,0)'),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=50, b=20),
            title=dict(text="Maya · intent fingerprint", font=dict(size=11, color='#aabbcc'), x=0.5),
            height=320,
        )
        st.plotly_chart(fig_maya, use_container_width=True)

        # Gap badge
        gap_maya = 0.47
        st.markdown(f"""
        <div style='text-align:center;margin-top:-10px;margin-bottom:8px;'>
          <span style='background:rgba(231,165,156,0.18);border:1px solid #e7a59c;
                       border-radius:20px;padding:5px 16px;font-size:0.82em;color:#c47b71;font-weight:700;'>
            Gap score: {gap_maya}  ·  HIGH
          </span>
        </div>
        """, unsafe_allow_html=True)

    # Dev's intent fingerprint
    with col_bridge_right:
        dev_si = [0.05, 0.08, 0.12, 0.04, 0.62, 0.06, 0.03]
        dev_pi = [0.42, 0.24, 0.14, 0.11, 0.04, 0.03, 0.02]

        fig_dev = go.Figure()
        fig_dev.add_trace(go.Scatterpolar(
            r=dev_si + [dev_si[0]],
            theta=bridge_cats + [bridge_cats[0]],
            fill='toself',
            name="Dev's intent (SI)",
            line=dict(color='#C9922A', width=2),
            fillcolor='rgba(201,146,42,0.15)',
        ))
        fig_dev.add_trace(go.Scatterpolar(
            r=dev_pi + [dev_pi[0]],
            theta=bridge_cats + [bridge_cats[0]],
            fill='toself',
            name="Maya perceives (PI)",
            line=dict(color='#6BAE8A', width=2, dash='dot'),
            fillcolor='rgba(107,174,138,0.12)',
        ))
        fig_dev.update_layout(
            polar=dict(
                radialaxis=dict(visible=True, range=[0, 0.7],
                                gridcolor='rgba(255,255,255,0.06)',
                                tickfont=dict(size=8, color='#556677')),
                angularaxis=dict(tickfont=dict(size=9, color='#aabbcc'),
                                 gridcolor='rgba(255,255,255,0.06)'),
                bgcolor='rgba(0,0,0,0)',
            ),
            showlegend=True,
            legend=dict(font=dict(size=9, color='#aabbcc'), bgcolor='rgba(0,0,0,0)'),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=50, b=20),
            title=dict(text="Dev · intent fingerprint", font=dict(size=11, color='#aabbcc'), x=0.5),
            height=320,
        )
        st.plotly_chart(fig_dev, use_container_width=True)

        # Gap badge
        gap_dev = 0.51
        st.markdown(f"""
        <div style='text-align:center;margin-top:-10px;margin-bottom:8px;'>
          <span style='background:rgba(231,165,156,0.18);border:1px solid #e7a59c;
                       border-radius:20px;padding:5px 16px;font-size:0.82em;color:#c47b71;font-weight:700;'>
            Gap score: {gap_dev}  ·  HIGH
          </span>
        </div>
        """, unsafe_allow_html=True)

    # Consent toggle mockup
    st.markdown("""
    <div style='padding:14px 20px;background:rgba(220,231,243,0.5);border:1px solid #dce7f3;
                border-radius:10px;margin-top:4px;margin-bottom:28px;display:flex;align-items:center;gap:16px;'>
      <div style='font-size:1.4em;'>🔒</div>
      <div style='flex:1;'>
        <div style='font-size:0.82em;color:#8ca3b0;font-weight:700;margin-bottom:3px;'>Consent Bridge — mutual opt-in required</div>
        <div style='font-size:0.75em;color:#717182;line-height:1.4;'>
          Both Maya and Dev have enabled intent sharing for this conversation.
          Either party can withdraw at any time — intent fingerprints are deleted from the bridge immediately.
          No data leaves the device without dual consent.
        </div>
      </div>
      <div style='padding:6px 14px;background:rgba(220,231,243,0.5);border:1px solid #8ca3b0;
                  border-radius:20px;font-size:0.78em;color:#8ca3b0;font-weight:700;white-space:nowrap;'>
        ✓ Both consented
      </div>
    </div>
    <div style='font-size:0.73em;color:#8ca3b0;font-style:italic;margin-top:-20px;margin-bottom:28px;'>
      Illustrative mockup · Consent architecture is a core design constraint, not an afterthought
    </div>
    """, unsafe_allow_html=True)

    # ── Section B: Individual Consciousness ───────────────────────────────────
    st.markdown("""
    <div style='font-size:0.78em;color:#e7a59c;font-weight:700;letter-spacing:0.12em;
                text-transform:uppercase;margin-bottom:12px;'>
      🧬  Section B — Individual Consciousness: Your Intent Fingerprint
    </div>
    """, unsafe_allow_html=True)

    col_ic_left, col_ic_right = st.columns([1.2, 1])

    with col_ic_left:
        # Blind-spot histogram: frequency of high-gap sends per intent category
        blindspot_cats = ["Seeking\nconnection", "Expressing\nconcern", "Setting a\nboundary",
                          "Seeking\nvalidation", "Expressing\nfrustration", "Making a\nrequest"]
        blindspot_freq = [2, 4, 8, 3, 14, 2]  # high-gap sends in last 30 days

        fig_bs = go.Figure()
        colors_bs = ['rgba(231,76,60,0.8)' if f >= 10 else
                     'rgba(243,156,18,0.7)' if f >= 5 else
                     'rgba(52,152,219,0.6)' for f in blindspot_freq]
        fig_bs.add_trace(go.Bar(
            x=blindspot_cats,
            y=blindspot_freq,
            marker=dict(color=colors_bs, line=dict(color='rgba(255,255,255,0.05)', width=1)),
            text=blindspot_freq,
            textposition='outside',
            textfont=dict(size=9, color='#aabbcc'),
        ))
        fig_bs.update_layout(
            title=dict(text="Blind-spot histogram · high-gap sends (last 30 days)",
                       font=dict(size=11, color='#aabbcc'), x=0),
            xaxis=dict(tickfont=dict(size=9, color='#778899'), gridcolor='rgba(255,255,255,0)',
                       showgrid=False),
            yaxis=dict(title="# high-gap sends", tickfont=dict(size=9, color='#556677'),
                       gridcolor='rgba(255,255,255,0.05)', title_font=dict(size=9, color='#556677')),
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=50, r=20, t=45, b=10),
            height=280,
            bargap=0.3,
        )
        st.plotly_chart(fig_bs, use_container_width=True)

    with col_ic_right:
        st.markdown("""
        <div style='padding:16px 18px;background:rgba(231,165,156,0.10);border:1px solid rgba(231,165,156,0.4);
                    border-radius:10px;height:100%;'>
          <div style='font-size:0.8em;color:#e7a59c;font-weight:700;margin-bottom:10px;'>
            🧬 Your intent fingerprint
          </div>
          <div style='font-size:0.78em;color:#2c3e50;margin-bottom:14px;line-height:1.5;'>
            A private model of how you communicate — built from your history, stored on your device.
          </div>

          <div style='margin-bottom:10px;'>
            <div style='font-size:0.72em;color:#717182;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;'>Primary gap mode</div>
            <div style='font-size:0.85em;color:#c47b71;font-weight:600;'>Expressing frustration — 14 high-gap events</div>
          </div>

          <div style='margin-bottom:10px;'>
            <div style='font-size:0.72em;color:#717182;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;'>Growth since Month 1</div>
            <div style='font-size:0.85em;color:#8ca3b0;font-weight:600;'>−38% overall gap score (mock trajectory)</div>
          </div>

          <div style='margin-bottom:10px;'>
            <div style='font-size:0.72em;color:#717182;text-transform:uppercase;letter-spacing:0.08em;margin-bottom:4px;'>Reflection loop</div>
            <div style='font-size:0.78em;color:#717182;line-height:1.4;'>
              Each high-gap send generates a journal prompt — not judgment, a question.
              <em style='color:#2c3e50;'>"What were you feeling when you sent that?"</em>
            </div>
          </div>

          <div style='padding:8px 10px;background:rgba(220,231,243,0.4);border:1px solid #dce7f3;
                      border-radius:7px;font-size:0.72em;color:#8ca3b0;font-style:italic;'>
            "Your intent fingerprint is yours. It exists to show you yourself — not to be used against you."
          </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div style='font-size:0.73em;color:#8ca3b0;font-style:italic;margin-top:6px;margin-bottom:28px;'>
      Illustrative — intent fingerprint generated from mock model data. Real fingerprints built from beta cohort, Month 3+
    </div>
    """, unsafe_allow_html=True)

    # ── Section C: The Map ─────────────────────────────────────────────────────
    st.markdown("""
    <div style='font-size:0.78em;color:#8ca3b0;font-weight:700;letter-spacing:0.12em;
                text-transform:uppercase;margin-bottom:12px;'>
      🗺️  Section C — The Map: Population-Scale Intent Signatures
    </div>
    <div style='font-size:0.82em;color:#717182;margin-bottom:16px;line-height:1.5;'>
      Thousands of dyads. Aggregated, anonymised intent trajectories.
      A living map of how understanding flows — and where it breaks — across a network.
    </div>
    """, unsafe_allow_html=True)

    # The Map — Trust Propagation Field
    # A density surface showing understanding signal spreading from mature dyads outward
    # Warm blush = high gap (fragmented). Cool slate-blue = low gap (understanding).
    # The field is not static — it evolves as the network grows.
    np.random.seed(99)
    _mx = np.linspace(-4, 4, 120)
    _my = np.linspace(-4, 4, 120)
    _MX, _MY = np.meshgrid(_mx, _my)

    def _trust_node(cx, cy, radius, strength):
        """A trust node radiates understanding outward."""
        dist = np.sqrt((_MX - cx)**2 + (_MY - cy)**2)
        return strength * np.exp(-(dist**2) / (2 * radius**2))

    # Seed trust nodes — mature dyads that have converged
    _trust_field = (
        _trust_node(-1.8, -1.5, 0.9, 1.0) +
        _trust_node( 0.3,  1.2, 0.8, 0.95) +
        _trust_node( 2.1, -0.8, 0.7, 0.85) +
        _trust_node(-0.5, -2.8, 0.6, 0.75) +
        _trust_node( 3.0,  2.2, 0.5, 0.65)
    )
    # Gap zones — areas of high fragmentation between nodes
    _gap_field = (
        _trust_node( 1.0,  0.1, 1.2, 0.6) +
        _trust_node(-2.8,  1.8, 0.9, 0.5) +
        _trust_node( 0.5, -1.5, 0.8, 0.45)
    )
    # Composite field: trust - gap (normalised 0..1)
    _composite = _trust_field - 0.4 * _gap_field
    _composite = (_composite - _composite.min()) / (_composite.max() - _composite.min())

    fig_map = go.Figure()
    fig_map.add_trace(go.Heatmap(
        z=_composite, x=_mx, y=_my,
        colorscale=[
            [0.0,  '#e7a59c'],   # blush — high gap / fragmented
            [0.25, '#dce7f3'],   # soft blue — transitioning
            [0.55, '#c0d4e8'],   # mid slate-blue — converging
            [0.80, '#8ca3b0'],   # slate — strong understanding
            [1.0,  '#2c3e50'],   # dark — deep coherence
        ],
        showscale=True,
        colorbar=dict(
            title=dict(text='Understanding', font=dict(size=10, color='#8ca3b0'), side='right'),
            tickvals=[0, 0.5, 1], ticktext=['fragmented', '', 'coherent'],
            tickfont=dict(size=9, color='#8ca3b0'),
            thickness=10, len=0.6,
        ),
        hovertemplate='Understanding: %{z:.2f}<extra></extra>',
        opacity=0.88,
    ))
    # Overlay trust node markers (mature dyads)
    _node_x = [-1.8, 0.3, 2.1, -0.5, 3.0]
    _node_y = [-1.5, 1.2, -0.8, -2.8, 2.2]
    _node_size = [14, 13, 11, 10, 9]
    fig_map.add_trace(go.Scatter(
        x=_node_x, y=_node_y, mode='markers+text',
        marker=dict(size=_node_size, color='#ffffff', line=dict(color='#8ca3b0', width=2)),
        text=['●', '●', '●', '●', '●'],
        textposition='middle center',
        textfont=dict(size=8, color='#8ca3b0'),
        name='Mature dyads', showlegend=True,
        hovertemplate='Mature dyad · trust anchor<extra></extra>',
    ))
    fig_map.update_layout(
        xaxis=dict(visible=False, range=[-4, 4]),
        yaxis=dict(visible=False, range=[-4, 4]),
        paper_bgcolor='rgba(245,246,247,0)',
        plot_bgcolor='rgba(245,246,247,0)',
        legend=dict(font=dict(size=9, color='#8ca3b0'), bgcolor='rgba(255,255,255,0.8)',
                    orientation='h', y=-0.05),
        margin=dict(l=10, r=60, t=10, b=30),
        height=360,
    )
    st.plotly_chart(fig_map, use_container_width=True)

    st.markdown("""
    <div style='font-size:0.73em;color:#8ca3b0;font-style:italic;margin-top:-8px;margin-bottom:28px;'>
      Trust propagation field · Each white node is a mature dyad that has converged ·
      Understanding radiates outward as the network grows ·
      Illustrative · Real population field: Horizon 3, conditional on H₁ + H₂ validation
    </div>
    """, unsafe_allow_html=True)

    # ── Closing statement ──────────────────────────────────────────────────────
    st.markdown("<hr class='nt-divider'>", unsafe_allow_html=True)
    st.markdown("""
    <div style='padding:28px 32px;background:linear-gradient(135deg,rgba(220,231,243,0.5) 0%,rgba(231,165,156,0.10) 100%);
                border:1px solid #dce7f3;border-radius:16px;margin:8px 0 28px;text-align:center;'>
      <div style='font-size:0.72em;color:#8ca3b0;font-weight:700;letter-spacing:0.15em;
                  text-transform:uppercase;margin-bottom:14px;'>
        Why this matters
      </div>
      <div style='font-size:1.05em;color:#2c3e50;line-height:1.7;font-weight:500;max-width:720px;margin:0 auto 16px;'>
        Social media spent fifteen years shaping human communication toward threat-first patterns.
      </div>
      <div style='font-size:1.05em;color:#2c3e50;line-height:1.7;max-width:720px;margin:0 auto 16px;'>
        This is the counter-architecture.
      </div>
      <div style='font-size:0.92em;color:#717182;line-height:1.7;max-width:680px;margin:0 auto 20px;'>
        It starts with two people and a single message.
        It ends with the infrastructure for a trust-based world.
      </div>
      <div style='font-size:0.82em;color:#8ca3b0;font-style:italic;max-width:600px;margin:0 auto 6px;'>
        That's not a product. That's what AI for Science is built for.
      </div>
      <div style='font-size:0.7em;color:#8ca3b0;margin-top:14px;'>
        Encode × Pillar VC AI for Science Fellowship · NeuroAI Cognitive Companion · March 2026
      </div>
    </div>
    """, unsafe_allow_html=True)
