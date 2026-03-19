"""
Soul Document Architecture Spec → PDF Generator
NC — NeuroAI Cognitive Companion
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    HRFlowable, KeepTogether, PageBreak
)
from reportlab.platypus.flowables import Flowable
from reportlab.lib.colors import HexColor
from datetime import datetime

# ── Colour Palette ────────────────────────────────────────────────────────────
NC_DARK        = HexColor("#0F1F2E")   # deep navy
NC_ACCENT      = HexColor("#1E6FFF")   # electric blue
NC_TEAL        = HexColor("#00B4A6")   # teal
NC_LIGHT_BG    = HexColor("#F0F4FF")   # very light blue-white
NC_CODE_BG     = HexColor("#1A1A2E")   # dark code background
NC_CODE_FG     = HexColor("#E8EAF6")   # code text
NC_BORDER      = HexColor("#CBD5E1")   # subtle border
NC_SECTION_BG  = HexColor("#E8F0FE")   # section header background
NC_WARN        = HexColor("#F59E0B")   # amber for open questions
WHITE          = colors.white
TEXT_DARK      = HexColor("#1E293B")   # near-black text
TEXT_MID       = HexColor("#475569")   # mid-grey

PAGE_W, PAGE_H = A4
L_MARGIN = 20*mm
R_MARGIN = 20*mm
T_MARGIN = 22*mm
B_MARGIN = 22*mm

# ── Styles ────────────────────────────────────────────────────────────────────
styles = getSampleStyleSheet()

def make_style(name, parent='Normal', **kwargs):
    return ParagraphStyle(name, parent=styles[parent], **kwargs)

S_COVER_TITLE = make_style('CoverTitle',
    fontSize=28, textColor=WHITE, leading=36, alignment=TA_LEFT,
    fontName='Helvetica-Bold')

S_COVER_SUB = make_style('CoverSub',
    fontSize=13, textColor=HexColor("#A5C8FF"), leading=18, alignment=TA_LEFT)

S_COVER_META = make_style('CoverMeta',
    fontSize=10, textColor=HexColor("#7B9FC4"), leading=14, alignment=TA_LEFT)

S_H1 = make_style('H1',
    fontSize=17, textColor=NC_DARK, leading=22, spaceBefore=16, spaceAfter=6,
    fontName='Helvetica-Bold', borderPadding=(0,0,4,0))

S_H2 = make_style('H2',
    fontSize=13, textColor=NC_ACCENT, leading=18, spaceBefore=12, spaceAfter=4,
    fontName='Helvetica-Bold')

S_H3 = make_style('H3',
    fontSize=11, textColor=NC_TEAL, leading=15, spaceBefore=8, spaceAfter=3,
    fontName='Helvetica-Bold')

S_BODY = make_style('Body',
    fontSize=10, textColor=TEXT_DARK, leading=15, alignment=TA_JUSTIFY,
    spaceAfter=6)

S_BODY_SMALL = make_style('BodySmall',
    fontSize=9, textColor=TEXT_MID, leading=13, spaceAfter=4)

S_BULLET = make_style('Bullet',
    fontSize=10, textColor=TEXT_DARK, leading=14, leftIndent=12,
    bulletIndent=0, spaceAfter=3)

S_CODE = make_style('Code',
    fontSize=8, textColor=NC_CODE_FG, leading=11, fontName='Courier',
    leftIndent=0, spaceAfter=0, backColor=NC_CODE_BG)

S_CAPTION = make_style('Caption',
    fontSize=8.5, textColor=TEXT_MID, leading=12, alignment=TA_CENTER,
    spaceAfter=8)

S_LABEL = make_style('Label',
    fontSize=9, textColor=NC_ACCENT, leading=12, fontName='Helvetica-Bold')

S_CALLOUT = make_style('Callout',
    fontSize=9.5, textColor=TEXT_DARK, leading=14, leftIndent=10, rightIndent=10,
    spaceAfter=6)

S_ITALIC = make_style('Italic',
    fontSize=9.5, textColor=TEXT_MID, leading=13, fontName='Helvetica-Oblique',
    spaceAfter=4)

# ── Custom Flowables ──────────────────────────────────────────────────────────

class ColorRect(Flowable):
    """A filled colour rectangle used for decorative blocks."""
    def __init__(self, width, height, color, radius=3):
        super().__init__()
        self.width = width
        self.height = height
        self.color = color
        self.radius = radius

    def draw(self):
        self.canv.setFillColor(self.color)
        self.canv.roundRect(0, 0, self.width, self.height,
                            self.radius, fill=1, stroke=0)


class CodeBlock(Flowable):
    """Dark-background monospace code block."""
    def __init__(self, text, available_width):
        super().__init__()
        self.text = text
        self.available_width = available_width
        self.padding = 8
        self.line_height = 11
        self.font_size = 7.5

    def wrap(self, aW, aH):
        lines = self.text.split('\n')
        self.lines = lines
        self.height = (len(lines) * self.line_height) + (self.padding * 2)
        self.width = self.available_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(NC_CODE_BG)
        c.roundRect(0, 0, self.width, self.height, 4, fill=1, stroke=0)
        # Left accent bar
        c.setFillColor(NC_ACCENT)
        c.rect(0, 0, 3, self.height, fill=1, stroke=0)
        # Text
        c.setFillColor(NC_CODE_FG)
        c.setFont('Courier', self.font_size)
        y = self.height - self.padding - self.font_size
        for line in self.lines:
            c.drawString(self.padding + 4, y, line[:120])  # truncate very long lines
            y -= self.line_height


class SectionHeader(Flowable):
    """Full-width section header with number badge."""
    def __init__(self, number, title, available_width):
        super().__init__()
        self.number = number
        self.title = title
        self.available_width = available_width
        self.height = 26

    def wrap(self, aW, aH):
        self.width = self.available_width
        return self.width, self.height

    def draw(self):
        c = self.canv
        w, h = self.width, self.height
        # Background bar
        c.setFillColor(NC_SECTION_BG)
        c.roundRect(0, 0, w, h, 4, fill=1, stroke=0)
        # Left accent
        c.setFillColor(NC_ACCENT)
        c.roundRect(0, 0, 4, h, 2, fill=1, stroke=0)
        # Number badge
        badge_w = 24
        c.setFillColor(NC_ACCENT)
        c.roundRect(10, 4, badge_w, h-8, 3, fill=1, stroke=0)
        c.setFillColor(WHITE)
        c.setFont('Helvetica-Bold', 10)
        c.drawCentredString(10 + badge_w/2, 8, str(self.number))
        # Title
        c.setFillColor(NC_DARK)
        c.setFont('Helvetica-Bold', 12)
        c.drawString(42, 8, self.title)


class HorizontalRule(Flowable):
    def __init__(self, width, color=NC_BORDER, thickness=0.5):
        super().__init__()
        self.hr_width = width
        self.color = color
        self.thickness = thickness
        self.height = 6

    def wrap(self, aW, aH):
        return self.hr_width, self.height

    def draw(self):
        self.canv.setStrokeColor(self.color)
        self.canv.setLineWidth(self.thickness)
        self.canv.line(0, 3, self.hr_width, 3)


class CalloutBox(Flowable):
    """Highlighted callout box with icon-style label."""
    def __init__(self, label, text, available_width, color=NC_LIGHT_BG,
                 accent=NC_ACCENT):
        super().__init__()
        self.label = label
        self.text = text
        self.available_width = available_width
        self.color = color
        self.accent = accent
        self.padding = 10

    def wrap(self, aW, aH):
        from reportlab.pdfbase.pdfmetrics import stringWidth
        self.width = self.available_width
        # Estimate height: wrap text at ~width - 2*padding
        usable = self.width - 2 * self.padding - 4
        chars_per_line = int(usable / 5.5)
        words = self.text.split()
        lines, line = [], []
        for w in words:
            if sum(len(x)+1 for x in line) + len(w) < chars_per_line:
                line.append(w)
            else:
                lines.append(' '.join(line))
                line = [w]
        if line:
            lines.append(' '.join(line))
        self.wrapped_lines = lines
        self.height = max(40, (len(lines) * 13) + 28)
        return self.width, self.height

    def draw(self):
        c = self.canv
        # Background
        c.setFillColor(self.color)
        c.roundRect(0, 0, self.width, self.height, 4, fill=1, stroke=0)
        # Left accent
        c.setFillColor(self.accent)
        c.roundRect(0, 0, 4, self.height, 2, fill=1, stroke=0)
        # Label
        c.setFillColor(self.accent)
        c.setFont('Helvetica-Bold', 8)
        c.drawString(12, self.height - 14, self.label.upper())
        # Text
        c.setFillColor(TEXT_DARK)
        c.setFont('Helvetica', 9)
        y = self.height - 27
        for ln in self.wrapped_lines:
            c.drawString(12, y, ln)
            y -= 13


# ── Page Templates ────────────────────────────────────────────────────────────

def on_first_page(canvas, doc):
    """Cover page background."""
    canvas.saveState()
    # Full-page gradient-style background
    canvas.setFillColor(NC_DARK)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    # Decorative top strip
    canvas.setFillColor(NC_ACCENT)
    canvas.rect(0, PAGE_H - 6*mm, PAGE_W, 6*mm, fill=1, stroke=0)
    # Bottom strip
    canvas.setFillColor(NC_TEAL)
    canvas.rect(0, 0, PAGE_W, 3*mm, fill=1, stroke=0)
    # Large decorative circle
    canvas.setFillColor(HexColor("#162335"))
    canvas.circle(PAGE_W - 30*mm, PAGE_H - 60*mm, 80*mm, fill=1, stroke=0)
    # Smaller accent circle
    canvas.setFillColor(HexColor("#1A3050"))
    canvas.circle(10*mm, 40*mm, 50*mm, fill=1, stroke=0)
    canvas.restoreState()


def on_later_pages(canvas, doc):
    """Header and footer for content pages."""
    canvas.saveState()
    # Header bar
    canvas.setFillColor(NC_DARK)
    canvas.rect(0, PAGE_H - 12*mm, PAGE_W, 12*mm, fill=1, stroke=0)
    canvas.setFillColor(NC_ACCENT)
    canvas.rect(0, PAGE_H - 12*mm, 3, 12*mm, fill=1, stroke=0)
    # Header text
    canvas.setFont('Helvetica-Bold', 8)
    canvas.setFillColor(WHITE)
    canvas.drawString(L_MARGIN, PAGE_H - 8*mm, "Soul Document Architecture Specification")
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(HexColor("#7B9FC4"))
    canvas.drawRightString(PAGE_W - R_MARGIN, PAGE_H - 8*mm,
                           "NC — NeuroAI Cognitive Companion  |  v0.1 Draft")
    # Footer
    canvas.setFillColor(NC_BORDER)
    canvas.rect(L_MARGIN, 10*mm, PAGE_W - L_MARGIN - R_MARGIN, 0.5, fill=1, stroke=0)
    canvas.setFont('Helvetica', 7.5)
    canvas.setFillColor(TEXT_MID)
    canvas.drawString(L_MARGIN, 6*mm, "CONFIDENTIAL — Pre-PRD Concept Specification")
    canvas.drawRightString(PAGE_W - R_MARGIN, 6*mm, f"Page {doc.page - 1}")
    canvas.restoreState()


# ── Build Content ─────────────────────────────────────────────────────────────

def build_pdf():
    output_path = "/Users/snnair/Documents/NC/_bmad-output/planning-artifacts/soul-document-architecture-spec-2026-03-16.pdf"

    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=L_MARGIN,
        rightMargin=R_MARGIN,
        topMargin=T_MARGIN + 12*mm,
        bottomMargin=B_MARGIN + 5*mm,
        title="Soul Document Architecture Specification",
        author="Snnair",
        subject="NC — NeuroAI Cognitive Companion",
    )

    available_w = PAGE_W - L_MARGIN - R_MARGIN
    story = []

    # ── COVER PAGE ──────────────────────────────────────────────────────────
    # Spacer to push content down on the dark page
    story.append(Spacer(1, 55*mm))
    story.append(Paragraph("Soul Document", S_COVER_TITLE))
    story.append(Paragraph("Architecture Specification", S_COVER_TITLE))
    story.append(Spacer(1, 5*mm))
    story.append(Paragraph("NC — NeuroAI Cognitive Companion", S_COVER_SUB))
    story.append(Paragraph("Digital Twin / Personality Fingerprint Layer", S_COVER_SUB))
    story.append(Spacer(1, 12*mm))

    meta_data = [
        ["Version", "0.1 Draft"],
        ["Date", "2026-03-16"],
        ["Author", "Snnair"],
        ["Status", "Pre-PRD Concept Specification"],
        ["Classification", "Confidential"],
    ]
    for label, value in meta_data:
        story.append(Paragraph(
            f'<font color="#7B9FC4"><b>{label}:</b></font>'
            f'  <font color="#A5C8FF">{value}</font>',
            S_COVER_META))
    story.append(PageBreak())

    # ── TOC-STYLE OVERVIEW ──────────────────────────────────────────────────
    story.append(Paragraph("Document Contents", S_H1))
    story.append(HorizontalRule(available_w, NC_ACCENT, 1.5))
    story.append(Spacer(1, 4*mm))

    toc_items = [
        ("1", "Executive Summary", "What the Soul Document is and why it exists"),
        ("2", "The Problem This Solves", "NC's current gap and what the Soul Document addresses"),
        ("3", "Soul Document Schema — 6 Layers", "Identity Core · Decision Architecture · Emotional Signature · Narrative Library · Communication Style · Temporal Index"),
        ("4", "The Intake Pipeline", "Biographical Interview · Passive Digital Harvest · Adversarial Correction Loop"),
        ("5", "Inference-Time Injection", "Semantic Layer Router · Token Budget Management"),
        ("6", "Versioning and Temporal Snapshots", "Snapshot creation, querying past selves"),
        ("7", "Integration with NC's Architecture", "Fitting into NC's 3-layer model"),
        ("8", "Governance, Consent, and Ownership", "Personality Sovereignty model"),
        ("9", "Research Validation Plan", "Studies 1, 2, 3 — Cold Start, Amygdala Race, Adversarial Refinement"),
        ("10", "Implementation Roadmap", "4-phase 12-month plan"),
        ("11", "Open Design Questions", "6 unresolved design decisions"),
        ("12", "Glossary", "Key terms and definitions"),
    ]

    for num, title, desc in toc_items:
        toc_table = Table(
            [[
                Paragraph(f'<font color="{NC_ACCENT.hexval()}">'
                          f'<b>{num}</b></font>', S_BODY),
                Paragraph(f'<b>{title}</b>', S_BODY),
                Paragraph(desc, S_BODY_SMALL),
            ]],
            colWidths=[12*mm, 58*mm, available_w - 70*mm]
        )
        toc_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('TOPPADDING', (0,0), (-1,-1), 3),
            ('BOTTOMPADDING', (0,0), (-1,-1), 3),
            ('LINEBELOW', (0,0), (-1,-1), 0.3, NC_BORDER),
        ]))
        story.append(toc_table)

    story.append(PageBreak())

    # ── SECTION 1: EXECUTIVE SUMMARY ────────────────────────────────────────
    story.append(SectionHeader("1", "Executive Summary", available_w))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph(
        "The Soul Document is NC's <b>portable, structured, model-agnostic personality representation</b> — "
        "a layered document that encodes an individual's identity, decision architecture, emotional signature, "
        "and narrative history. It is injected at inference time into NC's foundation model to condition "
        "intent prediction on <i>who the person actually is</i>, not just what they wrote.",
        S_BODY))

    story.append(CalloutBox(
        "Core Principle",
        "The Soul Document is NOT a fine-tuned model. It is a living structured corpus that travels with "
        "the user, upgrades as base models improve, and gets richer with every correction. Fine-tuning "
        "tattoos personality onto a model. The Soul Document hands any model a richly annotated biography.",
        available_w, NC_LIGHT_BG, NC_ACCENT))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("This document specifies:", S_BODY))
    for item in [
        "The full Soul Document schema (6 layers)",
        "How each layer is populated (3 intake modes)",
        "Inference-time injection architecture (Semantic Layer Router)",
        "Versioning and temporal snapshot protocol",
        "Governance, consent, and ownership model",
        "Integration with NC's existing foundation model architecture",
    ]:
        story.append(Paragraph(f"&#8226;  {item}", S_BULLET))

    story.append(Spacer(1, 4*mm))

    # ── SECTION 2: THE PROBLEM ───────────────────────────────────────────────
    story.append(SectionHeader("2", "The Problem This Solves Within NC", available_w))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph(
        "NC's current architecture conditions intent prediction on "
        "<b>P(intent | message, relational_history, context)</b>. This is powerful — but it models "
        "<i>communication patterns</i>, not <i>the person behind them</i>.",
        S_BODY))

    story.append(Paragraph(
        "Two people can have identical message histories and entirely different intent architectures:",
        S_BODY))

    contrast_data = [
        ["Same Signal", "Different Meaning"],
        ["Same words", "Different risk tolerance"],
        ["Same silence", "Different attachment style"],
        ['Same "I\'m fine"', "Different conflict suppression pattern"],
    ]
    contrast_table = Table(contrast_data,
                           colWidths=[available_w/2, available_w/2])
    contrast_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('BACKGROUND', (0,1), (-1,-1), NC_LIGHT_BG),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [NC_LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(contrast_table)
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph(
        "Without a personality layer, NC is doing <b>relational pattern matching</b>. With a Soul Document, "
        "NC does <b>person-aware intent modelling</b> — the same distinction as knowing someone's message "
        "history vs. genuinely knowing them.",
        S_BODY))

    story.append(CalloutBox(
        "The Cold Start Case",
        "New users have no message history. A Soul Document built from a 30-minute biographical intake "
        "gives NC immediate, rich grounding — Day 1 accuracy that would otherwise take 3 months of "
        "usage data to achieve.",
        available_w, HexColor("#FFF8E1"), NC_WARN))

    story.append(PageBreak())

    # ── SECTION 3: SCHEMA ────────────────────────────────────────────────────
    story.append(SectionHeader("3", "Soul Document Schema — The 6 Layers", available_w))
    story.append(Spacer(1, 2*mm))
    story.append(Paragraph(
        "Each layer serves a distinct function in intent modelling. Together they approximate "
        "how a person actually thinks, feels, and communicates.",
        S_BODY))
    story.append(Spacer(1, 3*mm))

    # Layer overview table
    layer_data = [
        ["#", "Layer", "Changes When", "Primary Use"],
        ["1", "Identity Core", "Decade-scale events", "Value ranking, non-negotiables"],
        ["2", "Decision Architecture", "Major life shifts", "Novel situation prediction"],
        ["3", "Emotional Signature", "Ongoing (passive)", "Threat modulation, state detection"],
        ["4", "Narrative Library", "New stories added", "RAG grounding at inference"],
        ["5", "Communication Style", "Continuous drift", "Formality and tone detection"],
        ["6", "Temporal Snapshot Index", "Per snapshot", "Historical self comparison"],
    ]
    layer_table = Table(layer_data,
                        colWidths=[8*mm, 45*mm, 45*mm, available_w - 98*mm])
    layer_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [NC_LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('TEXTCOLOR', (0,1), (0,-1), NC_ACCENT),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
    ]))
    story.append(layer_table)
    story.append(Spacer(1, 5*mm))

    # Individual layers
    layers = [
        {
            "num": "Layer 1",
            "name": "Identity Core",
            "sub": "Static anchor — changes only at decade-scale life events",
            "desc": "The bedrock of the Soul Document. Encodes ranked values (not listed — ranked with evidence), "
                    "non-negotiables, self-concept statements, and identity paradoxes. When a message could be "
                    "read as a challenge or an inquiry, the Identity Core tells NC: does this person default to "
                    "defence or curiosity?",
            "code": """identity_core:
  values_ranked:
    - rank: 1
      value: "intellectual honesty"
      over: "social harmony"
      evidence: "will correct factual errors in public even at social cost"

  non_negotiables:
    - "Will not take credit for others' work"
    - "Will not stay silent when witnessing injustice in their presence"

  paradoxes:
    - "Craves deep connection but retreats when it gets too close"
    - "Believes in fairness but is highly competitive in practice"
""",
        },
        {
            "num": "Layer 2",
            "name": "Decision Architecture",
            "sub": "The algorithm behind preferences — highest value for novel situation prediction",
            "desc": "This is the most powerful layer for replication. It encodes risk tolerance by domain, "
                    "dominant reasoning style, tradeoff patterns, living heuristics, known cognitive biases, "
                    "and conflict response patterns. This layer lets NC predict novel decisions — situations "
                    "the person has never faced.",
            "code": """decision_architecture:
  risk_profile:
    financial: 0.3    # cautious, researches thoroughly
    social: 0.7       # will say the uncomfortable thing
    creative: 0.8     # tries ideas before validating
    professional: 0.6 # calculated risks, not impulsive

  conflict_response:
    default: "withdraws, processes alone, re-engages with reasoned position"
    under_threat: "becomes precise and formal, removes emotional language"
    when_values_violated: "direct and firm, will not defer regardless of social cost"
""",
        },
        {
            "num": "Layer 3",
            "name": "Emotional Signature",
            "sub": "How they feel — captured partly from passive multimodal signals",
            "desc": "Captures emotional triggers, suppression patterns, attachment style, humor architecture, "
                    "energy rhythms, and resilience patterns. Crucially, passive signal sources (music, "
                    "communication timing, response latency) are encoded here — giving NC behavioral data "
                    "that text alone cannot provide.",
            "code": """emotional_signature:
  suppression_patterns:
    - pattern: "intellectualises under emotional overwhelm"
      signal: "message length increases, vocabulary formalises"
    - pattern: "silence as signal of serious upset (not indifference)"
      signal: "response latency increases dramatically"

  passive_signals:
    communication_timing:
      latency_when_upset: "12+ hours or no response"
      latency_when_excited: "< 5 minutes"
""",
        },
        {
            "num": "Layer 4",
            "name": "Narrative Library",
            "sub": "The story bank — grounding for RAG-based retrieval at inference time",
            "desc": "20-30 defining stories from across the person's life, each tagged with themes, "
                    "emotions, extracted lessons, reference frequency, and decision patterns revealed. "
                    "At inference time, semantically similar stories are retrieved and used as grounding — "
                    "the twin responds from actual lived experience, not generalised traits.",
            "code": """narrative_library:
  stories:
    - id: "story_001"
      era: "adolescence"
      title: "The Science Fair Exclusion"
      themes: ["injustice", "institutional_authority", "silence_as_strategy"]
      lesson_extracted: "Institutions protect themselves, not merit."
      decision_pattern_revealed: "Avoids systems he can't control; builds independent paths"

  retrieval_tags:
    authority_conflict: ["story_001"]
    truth_telling: ["story_001", "story_003"]
""",
        },
        {
            "num": "Layer 5",
            "name": "Communication Style Map",
            "sub": "How they express — the surface signature NC reads and generates in",
            "desc": "Writing fingerprint, formality drift as emotional signal, family-of-origin "
                    "communication patterns, and neurodivergent calibration. NC uses this layer to "
                    "detect when the way someone is writing has drifted from baseline — a signal of "
                    "emotional state change that may not be explicit in the content.",
            "code": """communication_style:
  formality_drift:
    baseline: "professional-warm"
    when_upset: "formality increases markedly — shorter sentences, precise word choice"
    when_excited: "sentence length shortens, more fragments, fewer hedges"
    when_vulnerable: "passive voice increases — creates distance from the statement"

  family_patterns:
    learned_patterns:
      - "Indirect expression of emotional need — states facts, expects inference"
      - "Apology through action, not words"
""",
        },
        {
            "num": "Layer 6",
            "name": "Temporal Snapshot Index",
            "sub": "The 'how they've changed' layer — enables the temporal stack",
            "desc": "Versioned history of all Soul Document snapshots, divergence scores between "
                    "eras, and a belief evolution log. Enables NC to query past versions of the "
                    "self, compute cross-snapshot deltas, and detect personality drift over time.",
            "code": """temporal_index:
  snapshots:
    - snapshot_id: "snap_002"
      timestamp: "2025-03-01"
      trigger: "User-initiated — significant life event: relationship ended"
      changes_from_previous:
        - layer: "decision_architecture"
          change: "social risk increased 0.7 -> 0.8"
        - layer: "emotional_signature"
          change: "repair_pattern: now initiates repair when trust established"
      divergence_score: 0.18   # 18% shift from previous — moderate change
""",
        },
    ]

    for layer in layers:
        story.append(KeepTogether([
            Paragraph(f'<b>{layer["num"]}: {layer["name"]}</b>', S_H2),
            Paragraph(layer["sub"], S_ITALIC),
            Paragraph(layer["desc"], S_BODY),
        ]))
        story.append(CodeBlock(layer["code"], available_w))
        story.append(Spacer(1, 5*mm))
        story.append(HorizontalRule(available_w))
        story.append(Spacer(1, 3*mm))

    story.append(PageBreak())

    # ── SECTION 4: INTAKE PIPELINE ───────────────────────────────────────────
    story.append(SectionHeader("4", "The Intake Pipeline", available_w))
    story.append(Spacer(1, 3*mm))

    intake_modes = [
        {
            "title": "Mode 1: Biographical Interview (Foundation Layer)",
            "sub": "30-60 minutes at onboarding — populates Layers 1, 2, 4",
            "desc": "A structured conversation — not a survey. Questions are narrative probes designed "
                    "to extract stories, not opinions. Conducted in four phases.",
            "code": """Phase 1: Formation (15 min)
  "What's the earliest memory where you made a decision you're still proud of?"
  "Who had the most influence on how you handle conflict — and what did they teach you?"

Phase 2: Decision Architecture (15 min)
  "Tell me about the last time you chose the harder path when the easy one was right there."
  "What's a rule you live by that most people would find surprising?"

Phase 3: Relational Patterns (15 min)
  "How do you know when someone has really earned your trust?"
  "What do you do when you're upset with someone close — what does your pattern look like?"

Phase 4: Temporal Anchor (15 min)
  "What did you believe at 20 that you now think was naive?"
  "If your 25-year-old self met you today — what would surprise them most?"
""",
        },
        {
            "title": "Mode 2: Passive Digital Harvest",
            "sub": "Continuous — populates Layers 3, 5. All processing is local-first.",
            "desc": "Raw behavioral data never leaves the device. Structured signal extraction "
                    "happens on-device; only the extracted YAML fields are stored in the Soul Document.",
            "code": """Signal Source          Layer Target               Specific Signal
──────────────────────────────────────────────────────────────────
Music streaming        Emotional Signature        Genre, tempo, lyrical themes
                                                  Late-night vs. daytime listening

Communication timing   Emotional Signature        Response latency patterns
                       Communication Style        Latency drift by emotional state

Writing samples        Communication Style        Sentence structure, vocabulary
(emails, messages)                                Formality drift detection

Calendar patterns      Decision Architecture      What gets protected vs. cancelled
                       Emotional Signature        Energy rhythms, social scheduling
""",
        },
        {
            "title": "Mode 3: Adversarial Correction Loop",
            "sub": "Ongoing — refines all layers through structured disagreement",
            "desc": "The key insight: disagreement is a higher-value training signal than agreement. "
                    "When a person says 'I'd never do that,' the specificity of that rejection reveals "
                    "the edges of their identity more precisely than any affirmation can.",
            "code": """"Yes, exactly"         -> Confidence score +1 on relevant fields
"Close but off-tone"   -> Soft update: tone/style fields flagged for refinement
"Completely wrong"     -> High-signal correction event:
                          - User prompted: "What would you have said instead?"
                          - Correction tagged to specific layer + field
                          - Conflicting field weight reduced
                          - New evidence integrated
""",
        },
    ]

    for mode in intake_modes:
        story.append(Paragraph(mode["title"], S_H2))
        story.append(Paragraph(mode["sub"], S_ITALIC))
        story.append(Paragraph(mode["desc"], S_BODY))
        story.append(CodeBlock(mode["code"], available_w))
        story.append(Spacer(1, 5*mm))

    story.append(PageBreak())

    # ── SECTION 5: INFERENCE ARCHITECTURE ───────────────────────────────────
    story.append(SectionHeader("5", "Inference-Time Injection Architecture", available_w))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("The Semantic Layer Router", S_H2))
    story.append(Paragraph(
        "When a query arrives, the router decides which layers to inject — keeping context lean "
        "while maximising relevance. Not all queries need all layers.",
        S_BODY))

    router_code = """QUERY ARRIVES: "Why did she go silent after I said that?"
         |
         v
SEMANTIC QUERY CLASSIFIER
  Query type: [relational_intent / emotional]
         |
    ┌────┴─────────────────┐
    v                      v                      v
[ALWAYS LOAD]         [RETRIEVE]            [CONDITIONALLY]
Identity Core         3-5 Stories           Decision Architecture
(500 tokens)          by semantic           if query involves
                      similarity            choice / action
                      (800 tokens)          (400 tokens)
    |                      |                      |
    └──────────────────────┴──────────────────────┘
                           |
                           v
         STRUCTURED SYSTEM PROMPT ASSEMBLY
  "You are reasoning as [person]. Here is who they
   are: [Identity Core]. Here are relevant experiences:
   [Story 001, Story 003]. Their response pattern in
   relational conflict is: [Emotional Signature]"
                           |
                           v
         BASE LLM (Claude / GPT / Llama)
         Produces person-aware intent prediction
"""
    story.append(CodeBlock(router_code, available_w))
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("Token Budget Management", S_H2))
    token_data = [
        ["Layer", "Tokens", "Loaded When"],
        ["Identity Core", "500", "Always"],
        ["Active Conversation", "2,000", "Always"],
        ["Narrative Retrieval (3-5 stories)", "800", "Always"],
        ["Decision Architecture", "400", "Query involves choice/action"],
        ["Emotional Signature", "400", "Relational/emotional query"],
        ["Communication Style", "300", "Style/tone query"],
        ["Temporal Context", "200", "Historical query"],
        ["Response Reserve", "1,592", "Output generation"],
        ["TOTAL", "8,192", "Context window"],
    ]
    token_table = Table(token_data, colWidths=[75*mm, 25*mm, available_w - 100*mm])
    token_table.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [NC_LIGHT_BG, WHITE]),
        ('BACKGROUND', (0,-1), (-1,-1), NC_DARK),
        ('TEXTCOLOR', (0,-1), (-1,-1), WHITE),
        ('FONTNAME', (0,-1), (-1,-1), 'Helvetica-Bold'),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('ALIGN', (1,0), (1,-1), 'CENTER'),
    ]))
    story.append(token_table)
    story.append(PageBreak())

    # ── SECTION 6: VERSIONING ────────────────────────────────────────────────
    story.append(SectionHeader("6", "Versioning and Temporal Snapshot Protocol", available_w))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph("When Snapshots Are Created", S_H2))
    triggers_data = [
        ["Trigger Type", "Description"],
        ["User life event tag", '"I got married", "we broke up", "I changed jobs"'],
        ["Divergence threshold", "Score crosses >0.25 from previous snapshot"],
        ["Scheduled review", "Every 6 months by default"],
        ["Correction volume", ">10 high-signal corrections in 30 days"],
    ]
    t = Table(triggers_data, colWidths=[50*mm, available_w - 50*mm])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [NC_LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t)
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("Querying Past Snapshots", S_H2))
    story.append(CodeBlock(
        '# Implicit temporal query\n'
        '"What would 2024-me have done in this situation?"\n'
        '-> Router loads snap_001 context instead of active snapshot\n\n'
        '# Cross-snapshot dialogue\n'
        '"What changed between how I thought about conflict then vs. now?"\n'
        '-> Router loads snap_001 and snap_002, computes narrative diff, surfaces delta',
        available_w))
    story.append(PageBreak())

    # ── SECTION 7: NC INTEGRATION ────────────────────────────────────────────
    story.append(SectionHeader("7", "Integration With NC's Foundation Model", available_w))
    story.append(Spacer(1, 3*mm))

    integration_data = [
        ["NC Layer", "Existing Capability", "Soul Document Addition"],
        ["Layer 1\nFoundation Model",
         "TPJ-inspired mentalising head\nAmygdala-analogue threat detector",
         "Soul Document injection conditions intent prediction on sender/receiver personality. "
         "Reduces ambiguity in threat-tagging for known individuals."],
        ["Layer 2\nRelationship Twin",
         "Dyadic communication pattern model\nIntent gap visualiser",
         "Soul Document comparison surfaces structural incompatibilities "
         "(attachment mismatch, risk tolerance gap). Generates translation layer between styles."],
        ["Layer 3\nCognitive Companion",
         "Real-time browser extension\nIntent reframing interface",
         "Soul Document personalises reframing suggestions to match receiver's emotional signature. "
         '"She would hear this better framed as X, given her pattern of Y."'],
    ]
    it = Table(integration_data, colWidths=[28*mm, 50*mm, available_w - 78*mm])
    it.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [NC_LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (0,1), (0,-1), NC_ACCENT),
    ]))
    story.append(it)
    story.append(Spacer(1, 4*mm))

    story.append(Paragraph("The Cold Start Advantage", S_H2))
    cold_data = [
        ["Timepoint", "Without Soul Document", "With Soul Document (30-min intake)"],
        ["Day 1", "40% intent prediction accuracy", "74% intent prediction accuracy"],
        ["Week 4", "65%", "81%"],
        ["Month 3", "82%", "89%"],
    ]
    ct = Table(cold_data, colWidths=[28*mm, 70*mm, available_w - 98*mm])
    ct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 9),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [NC_LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('TEXTCOLOR', (2,1), (2,-1), NC_TEAL),
        ('FONTNAME', (2,1), (2,-1), 'Helvetica-Bold'),
    ]))
    story.append(ct)
    story.append(Paragraph(
        "* Figures are hypothetical projections for Study 1 validation — not observed data.",
        S_BODY_SMALL))
    story.append(PageBreak())

    # ── SECTION 8: GOVERNANCE ────────────────────────────────────────────────
    story.append(SectionHeader("8", "Governance, Consent, and Ownership", available_w))
    story.append(Spacer(1, 3*mm))

    story.append(Paragraph(
        "The Soul Document represents a new category of personal data — identity data at "
        "fine-grained fidelity. It requires a governance model designed from day one, not "
        "retrofitted after deployment.",
        S_BODY))

    story.append(CalloutBox(
        "Personality Sovereignty Principle",
        "The user owns the Soul Document absolutely. Storage is local-first, "
        "encrypted at rest (AES-256, device keychain). Cloud sync is opt-in only, "
        "end-to-end encrypted if enabled. The user retains the right to full export, "
        "per-layer consent revocation, and complete deletion at any time.",
        available_w, HexColor("#E8F5E9"), NC_TEAL))
    story.append(Spacer(1, 3*mm))

    gov_data = [
        ["Access Level", "Rights", "Constraints"],
        ["Owner", "Full read/write all layers", "—"],
        ["Partner (mutual consent)", "Read only — specified layers", "Mutual consent required; revocable"],
        ["Therapist (explicit grant)", "Read only — specified layers", "Explicit grant per session"],
        ["NC Foundation Model", "Read — inference only", "No retention; no training"],
        ["Third Parties", "PROHIBITED", "No sale or licensing without opt-in"],
    ]
    gt = Table(gov_data, colWidths=[40*mm, 55*mm, available_w - 95*mm])
    gt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8.5),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [NC_LIGHT_BG, WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 7),
        ('TEXTCOLOR', (0,5), (-1,5), HexColor("#C0392B")),
        ('FONTNAME', (0,5), (1,5), 'Helvetica-Bold'),
    ]))
    story.append(gt)
    story.append(Spacer(1, 4*mm))

    story.append(CalloutBox(
        "Domestic Safety Design Constraint",
        "The Soul Document must not become a surveillance instrument. Shared device scenarios "
        "require biometric-gated access. The tool is explicitly designed so that an abusive "
        "partner cannot use it to model, predict, or manipulate the other party. "
        "IRB review is required before any research use of Soul Document data.",
        available_w, HexColor("#FFF3E0"), HexColor("#E65100")))
    story.append(PageBreak())

    # ── SECTION 9: RESEARCH ──────────────────────────────────────────────────
    story.append(SectionHeader("9", "Research Validation Plan", available_w))
    story.append(Spacer(1, 3*mm))

    studies = [
        {
            "num": "Study 1",
            "title": "Cold Start Validation",
            "q": "Does a Soul Document replace 3 months of message history?",
            "rows": [
                ["Design", "RCT, N=100 new NC users, 12-week study"],
                ["Group A", "Standard NC onboarding (message history builds over time)"],
                ["Group B", "30-minute biographical intake → Soul Document at Day 1"],
                ["Measure", "Intent prediction F1 score at Week 1, 4, 12"],
                ["Hypothesis", "Group B matches Group A's Week 12 F1 from Week 1"],
                ["Timeline", "Month 1-3 of research programme"],
                ["Est. Cost", "~$15,000 (recruitment + annotation validation)"],
            ]
        },
        {
            "num": "Study 2",
            "title": "Amygdala Race Modulation",
            "q": "Does Soul Document context reduce threat-tagging of ambiguous messages?",
            "rows": [
                ["Design", "EEG/fNIRS within-subjects, N=24 (12 dyads)"],
                ["Condition A", "Read ambiguous message with no context"],
                ["Condition B", "Read ambiguous message after viewing sender's Soul Document summary"],
                ["Measure", "Amygdala activation magnitude, P300 latency, self-reported intent"],
                ["Hypothesis", "Condition B shows reduced threat activation + faster accurate classification"],
                ["Timeline", "Month 4-8 (concurrent with existing EEG pilot)"],
            ]
        },
        {
            "num": "Study 3",
            "title": "Adversarial Refinement Convergence",
            "q": "Does disagreement with your twin accelerate accuracy faster than agreement?",
            "rows": [
                ["Design", "8-week longitudinal, N=60 NC users"],
                ["Group A", "Passive use — read twin responses, no correction"],
                ["Group B", "Active correction — rate responses, flag errors, explain why"],
                ["Measure", "Soul Document accuracy vs. third-party observer ratings"],
                ["Hypothesis", "Group B converges 3x faster than Group A"],
                ["Timeline", "Month 6-12"],
            ]
        },
    ]

    for study in studies:
        story.append(Paragraph(f'{study["num"]}: {study["title"]}', S_H2))
        story.append(Paragraph(study["q"], S_ITALIC))
        st = Table(study["rows"], colWidths=[28*mm, available_w - 28*mm])
        st.setStyle(TableStyle([
            ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'),
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('TEXTCOLOR', (0,0), (0,-1), NC_ACCENT),
            ('ROWBACKGROUNDS', (0,0), (-1,-1), [NC_LIGHT_BG, WHITE]),
            ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 7),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(st)
        story.append(Spacer(1, 5*mm))

    story.append(PageBreak())

    # ── SECTION 10: ROADMAP ──────────────────────────────────────────────────
    story.append(SectionHeader("10", "Implementation Roadmap", available_w))
    story.append(Spacer(1, 3*mm))

    phases = [
        {
            "phase": "Phase 1",
            "title": "Foundation",
            "months": "Months 1-3",
            "goal": "Build and validate the Soul Document schema",
            "items": [
                ("Week 1-2", "Finalise schema (all 6 layers); engineer YAML validation"),
                ("Week 3-4", "Build biographical interview protocol; pilot with 5 users"),
                ("Week 5-8", "Build Semantic Layer Router; integrate with NC inference pipeline"),
                ("Week 9-12", "Launch Study 1 (cold start validation); begin passive signal harvest"),
            ]
        },
        {
            "phase": "Phase 2",
            "title": "Multimodal Enrichment",
            "months": "Months 4-6",
            "goal": "Add passive behavioral signal pipeline",
            "items": [
                ("Month 4", "Communication timing signal extractor (on-device)"),
                ("Month 5", "Writing style fingerprint extractor (on-device NLP)"),
                ("Month 6", "Music/media consumption connector (Spotify API + on-device processing)"),
            ]
        },
        {
            "phase": "Phase 3",
            "title": "Temporal Stack",
            "months": "Months 7-9",
            "goal": "Versioning, snapshot creation, temporal queries",
            "items": [
                ("Month 7", "Snapshot creation protocol and trigger system"),
                ("Month 8", "Cross-snapshot divergence scoring"),
                ("Month 9", 'Temporal query routing ("what would 2024-me have said?")'),
            ]
        },
        {
            "phase": "Phase 4",
            "title": "Clinical Integration",
            "months": "Months 10-12",
            "goal": "Connect Soul Document to NC's therapeutic positioning",
            "items": [
                ("Month 10", "Relationship Mirror feature (compare partner Soul Documents)"),
                ("Month 11", "Longitudinal mental health baseline detection"),
                ("Month 12", "IRB submission for Study 2 (Amygdala Race test)"),
            ]
        },
    ]

    for ph in phases:
        phase_header = Table([[
            Paragraph(f'<b>{ph["phase"]}</b>', make_style(
                f'ph_{ph["phase"]}', fontSize=10, textColor=WHITE,
                fontName='Helvetica-Bold')),
            Paragraph(f'<b>{ph["title"]}</b>  '
                      f'<font color="#A5C8FF">{ph["months"]}</font>', make_style(
                f'pht_{ph["phase"]}', fontSize=10, textColor=WHITE)),
            Paragraph(ph["goal"], make_style(
                f'phg_{ph["phase"]}', fontSize=9, textColor=HexColor("#A5C8FF"))),
        ]], colWidths=[22*mm, 55*mm, available_w - 77*mm])
        phase_header.setStyle(TableStyle([
            ('BACKGROUND', (0,0), (-1,-1), NC_DARK),
            ('TOPPADDING', (0,0), (-1,-1), 6),
            ('BOTTOMPADDING', (0,0), (-1,-1), 6),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(phase_header)

        items_data = [[Paragraph(t, S_LABEL), Paragraph(d, S_BODY)]
                      for t, d in ph["items"]]
        items_table = Table(items_data, colWidths=[25*mm, available_w - 25*mm])
        items_table.setStyle(TableStyle([
            ('FONTSIZE', (0,0), (-1,-1), 9),
            ('ROWBACKGROUNDS', (0,0), (-1,-1), [NC_LIGHT_BG, WHITE]),
            ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 8),
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ]))
        story.append(items_table)
        story.append(Spacer(1, 4*mm))

    story.append(PageBreak())

    # ── SECTION 11: OPEN QUESTIONS ───────────────────────────────────────────
    story.append(SectionHeader("11", "Open Design Questions", available_w))
    story.append(Spacer(1, 3*mm))

    oq_data = [
        ["#", "Question", "Options", "Recommendation"],
        ["1", "Should Soul Document require onboarding interview, or be optional?",
         "Required / Optional / Progressive",
         "Progressive — basic doc from sign-up; interview unlocks full precision"],
        ["2", "How many stories minimum for RAG to be effective?",
         "5 / 10 / 20",
         "10 minimum; 20 for high-confidence retrieval"],
        ["3", "Should partners see each other's Soul Documents?",
         "No / Mutual consent / Therapist-mediated",
         "Mutual consent with layer-level granularity"],
        ["4", "Should the twin correct itself in real time or in batches?",
         "Real-time / Weekly / User-triggered",
         "User-triggered with weekly prompt — avoids destabilising mid-conversation"],
        ["5", "What happens to Soul Document on account deletion?",
         "Archive / Full delete / Transfer",
         "Full delete by default; optional export before deletion"],
        ["6", "Can a Soul Document be built from public data (social posts)?",
         "Yes / No / Consent-gated",
         "Consent-gated only; never without explicit opt-in"],
    ]
    oqt = Table(oq_data, colWidths=[8*mm, 45*mm, 38*mm, available_w - 91*mm])
    oqt.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), NC_DARK),
        ('TEXTCOLOR', (0,0), (-1,0), WHITE),
        ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
        ('FONTSIZE', (0,0), (-1,-1), 8),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [HexColor("#FFF8E1"), WHITE]),
        ('GRID', (0,0), (-1,-1), 0.5, NC_BORDER),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TEXTCOLOR', (0,1), (0,-1), NC_WARN),
        ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'),
        ('TEXTCOLOR', (3,1), (3,-1), NC_TEAL),
    ]))
    story.append(oqt)
    story.append(PageBreak())

    # ── SECTION 12: GLOSSARY ─────────────────────────────────────────────────
    story.append(SectionHeader("12", "Glossary", available_w))
    story.append(Spacer(1, 3*mm))

    glossary = [
        ("Soul Document",
         "Structured YAML personality representation injected at inference time into NC's LLM."),
        ("Temporal Snapshot",
         "A frozen, versioned copy of the Soul Document at a specific life moment."),
        ("Divergence Score",
         "Quantified delta between two Soul Document snapshots, expressed as 0.0–1.0."),
        ("Semantic Layer Router",
         "System that selects which Soul Document layers to inject per incoming query."),
        ("Adversarial Correction",
         "User disagreement with twin output — the highest-value training signal in the system."),
        ("Cold Start",
         "The early period before message history is rich enough to ground intent prediction."),
        ("Personality Sovereignty",
         "Principle that the user owns, controls, and can delete their Soul Document absolutely."),
        ("Intent Gap",
         "Delta between a sender's intended meaning and a receiver's interpreted meaning."),
        ("Passive Digital Harvest",
         "On-device extraction of behavioral signals from music, timing, writing, and calendar data."),
        ("Biographical Interview",
         "Structured 4-phase narrative conversation that populates Layers 1, 2, and 4 of the Soul Document."),
    ]

    for term, definition in glossary:
        g_table = Table([[
            Paragraph(f'<b>{term}</b>', make_style(
                f'GT_{term[:8]}', fontSize=9.5, textColor=NC_DARK,
                fontName='Helvetica-Bold')),
            Paragraph(definition, S_BODY_SMALL),
        ]], colWidths=[48*mm, available_w - 48*mm])
        g_table.setStyle(TableStyle([
            ('VALIGN', (0,0), (-1,-1), 'TOP'),
            ('LINEBELOW', (0,0), (-1,-1), 0.3, NC_BORDER),
            ('TOPPADDING', (0,0), (-1,-1), 5),
            ('BOTTOMPADDING', (0,0), (-1,-1), 5),
            ('LEFTPADDING', (0,0), (-1,-1), 4),
        ]))
        story.append(g_table)

    story.append(Spacer(1, 8*mm))
    story.append(HorizontalRule(available_w, NC_ACCENT, 1))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph(
        "This document is a pre-PRD concept specification. It requires ethics review, IRB consultation, "
        "and technical feasibility validation before implementation begins.",
        S_ITALIC))
    story.append(Paragraph(
        "Next step: Present to NC research team for feedback; initiate ethics board review of "
        "data governance model.",
        S_ITALIC))

    # ── BUILD ────────────────────────────────────────────────────────────────
    doc.build(
        story,
        onFirstPage=on_first_page,
        onLaterPages=on_later_pages,
    )
    print(f"PDF generated: {output_path}")


if __name__ == "__main__":
    build_pdf()
