# B2B Deck Quality Charter

**Version:** V01R02
**Date:** 2026.05.19
**Origin:** Lesson-learned from prior session (deck functional but visually unimpressive)
**Authoritative Source:** `b2b-presentation-creator.skill` (V01R02 ZIP) — `references/12-quality-charter.md`

---

## Purpose

Mandatory pre-build checklist that EVERY deck build must satisfy before producing the .pptx artifact. This Charter prevents the "functional but not delightful" failure mode where content is correct but visual treatment is monotonous, executive readers disengage in 10 seconds, and the deck fails to land its key message.

**Charter Compliance is enforced by**
- `presentation-generator-agent` V01R03 — Phase A.5 Charter Compliance Gate (pre-build)
- `qa-master-agent` V01R02 — Dimension 6 Brand Compliance extension (post-build)

---

## Why This Charter Exists

A prior session produced a deck that was technically correct (English content, accurate facts, valid PPTX) but visually unimpressive. The reference deck (V02R02) showed what executive-grade design looks like. The gap was traced to four root causes

1. Reading only SKILL.md without the full references folder
2. Defaulting to one design pattern (4-card layouts) repeatedly
3. Skipping icon library, color semantics, and big-number callouts
4. Using placeholder data instead of realistic illustrative examples

This Charter codifies the lessons learned so they apply across all future sessions.

---

## Core Principle

A deck is not "done" when content is correct.
A deck is "done" when content is correct **AND** visually compelling **AND** varied **AND** readable in 10 seconds per slide by a busy executive.

**Bilingual statement (TH):** สไลด์ไม่ใช่ว่า "เสร็จ" เมื่อเนื้อหาถูกต้อง — สไลด์ "เสร็จ" เมื่อเนื้อหาถูกต้อง **และ** ดูดี **และ** หลากหลาย **และ** ผู้บริหารอ่านจบใน 10 วินาทีต่อสไลด์

---

## 9 Mandatory Visual Elements Checklist

Before declaring any B2B deck complete, verify ALL of the following. If any item is missing, the deck is **not ready**. Pass threshold = ≥8/9 (see Metrics section).

### 1. Brand Chrome (Best Effort)

- Customer logo present on every content slide (top-left or top-right)
- Consultant/iCE logo present on every content slide (opposite corner)
- Cover slide carries both logos prominently
- Footer contains version (V##R##), date (YYYY.MM.DD), and confidentiality marker

If logos are not available, ASK before building. **Do not invent logos.** If no logo can be obtained, document this in the QA report and continue (best-effort item).

### 2. Icon Library (Mandatory)

- At least one contextual icon per content slide
- Icons match a single family (no mixing Lucide + Material + clip-art)
- Icon stroke weight matches theme personality
- **Plain rectangles ARE NOT a substitute for icons**
- Icons sized appropriately (24px inline, 48px row, 64px hero)

**Source:** Skill ships 12 Lucide SVG icons in `assets/icons/` (bar-chart, check-circle, clock, cloud, database, handshake, lightbulb, shield, target, trending-up, users, alert-triangle). Use these as the canonical icon library for iCE decks.

### 3. Color Semantics (Mandatory for Multi-State Slides)

When a slide depicts multiple states, scenarios, or comparisons (routine vs breach, healthy vs overdue, baseline vs target), apply this semantic color code

| Color | Semantic Meaning |
|---|---|
| **Green** | Routine, healthy, on-track, succeeded |
| **Red** | Breach, alert, blocked, failed |
| **Slate Gray** | Neutral, reversal, audit, post-event |
| **Navy (Primary)** | Standard content, primary brand color |
| **Accent (Orange / Coral / Teal)** | Highlights, callouts (use sparingly, ≈10%) |

A slide that shows "before vs after", "good vs bad", or "by status" without color coding loses its semantic edge. Apply this consistently across the deck.

### 4. Big Number Callouts — Hero Numbers (Mandatory)

Every outcome or capability slide should have at least ONE large number callout. Pattern

- **60-80pt bold** for the number
- **9-11pt regular** for the label below
- Examples
  - "**40%** LESS MANUAL WORK"
  - "**7 Days** FASTER MONTH-END"
  - "**Zero** RECONCILIATION GAPS"
  - "**100%** OIC VISIBILITY"

**Avoid:** "We will reduce manual work by approximately forty percent." (boring, no anchor)
**Prefer:** "**40%** LESS MANUAL WORK" (executive eye-catcher)

### 5. Layout Variation (Mandatory)

- **No layout pattern repeated more than 3 times consecutively**
- Mix of layouts across the deck
  - 4-card grid
  - 2-column "DRIVES" layout
  - Full-bleed hero
  - Numbered process flow
  - 5-tile timeline
  - T-account boxes
  - Capability map
  - KPI tiles
- Section dividers between major acts (Cover → Stage → Anchor → Detail → Trust → Decision → Reference)

A 12-slide deck with the same 4-card layout 12 times reads as monotonous regardless of content quality.

### 6. Realistic Example Data with Disclaimer (Mandatory — Anti-Hallucination)

When showing T-accounts, transaction traces, or data examples

- Use plausible, round numbers ("USD 1,200,000" annual premium, "100k DR / 90k CR / 10k brokerage")
- Use fictional but realistic identifiers ("Policy ABC-2026-001", "Tx #BXC-2025-001")
- Add small italic disclaimer somewhere on the slide: *Illustrative example*

**Do not fabricate REAL customer data.** **Do not use placeholder text** like "XX,XXX THB" or "[Insert Number Here]" — those signal an unfinished deck.

Per CLAUDE.md V07R01 H1-H4 — real customer facts must trace to source documents; speculative figures must carry PLACEHOLDER tag.

### 7. Business Benefit / Outcome Closing Card per Section (Mandatory)

Every functional or technical slide should close with a small call-out card

- Icon (chart / check / lightbulb / shield from skill icon library)
- Title: "Business Benefit" / "Outcome" / "Why This Matters"
- 1-2 sentences of plain English benefit
- Optional: quantified outcome

This anchors business value at every step. Do not assume the audience will infer benefits from technical detail.

### 8. Section Labels Single-Line (Cosmetic)

- Section labels (e.g., "SLIDE 5 - CESSION-LEVEL DATA MODEL") render on a single line
- Text-box widths set to at least 9 inches (deck width minus 1.5 inch margin)
- **No mid-word line breaks anywhere**

### 9. Font Discipline (Cosmetic)

- Single font family across the deck (typically Sarabun + Inter for Bilingual TH/EN, or template-specified font pair)
- **No more than 6 distinct font sizes** used
- Defaults: Title 28pt / Subtitle 13pt / Body 10-11pt / Footer 9pt
- Apply size compensation for mismatched Thai+English x-height pairs (per Step 6.5 in sales-pipeline-report skill, same logic)

---

## Pre-Build Workflow (8-Step — Mandatory)

Before generating ANY .pptx file, complete this sequence

1. **Read Charter** — this file (12-quality-charter.md)
2. **Read full skill references** — for b2b-presentation-creator, read all 12 reference files (01-deck-types through 12-quality-charter)
3. **Confirm assets** — verify icons, logos, fonts available at expected paths; ask user if missing
4. **Define slide-by-slide visual approach** — write outline that states, for each slide, WHICH visual method (Method 1 native shapes, Method 2 SVG, Method 3 AI imagery, Method 4 icons) and WHICH layout pattern
5. **Get user sign-off on outline** — present the outline before any .pptx generation
6. **Build** — only after sign-off
7. **Visual QA** — render to PDF, view JPGs, fix issues before declaring done
8. **Final Charter check** — re-read this Charter, score the deck against each item, document gaps

---

## Anti-Patterns to Reject

These outputs are unacceptable; if produced, refactor before delivering

| Anti-Pattern | Why Reject |
|---|---|
| All slides use the same 4-card layout | Boring, monotonous (violates §5) |
| No icons anywhere | Looks like Word doc converted to slides (violates §2) |
| All boxes one color | No semantic hierarchy (violates §3) |
| Hero numbers absent | No executive eye-catcher (violates §4) |
| Text-only slides | Forgettable |
| Placeholder text "XXX" or "Lorem ipsum" | Signals unfinished (violates §6) |
| Section label wraps to two lines | Looks broken (violates §8) |
| Mixed fonts (Arial + Calibri) | Looks unprofessional (violates §9) |
| Footer says "Slide 2 of 10" but deck has 12 slides | Signals copy-paste error |
| Diagrams generated as raster images that render blurry | Switch to SVG or native shapes |

---

## When to Override This Charter

The Charter applies to executive-facing decks (CEO / CFO / Board level). It can be relaxed for

- Internal working drafts marked "DRAFT — DO NOT DISTRIBUTE"
- Highly technical documents for IT review (where dense tables are appropriate)
- One-off ad-hoc requests where speed beats polish (and user confirms the trade-off)

In every case, **document the override decision explicitly in the QA report** so the next reader knows why standards were relaxed.

---

## Metrics — Pass Threshold

A deck passes Charter compliance if it scores **at least 8 out of 9** mandatory checklist items.

| Score | Verdict |
|---|---|
| 9/9 | PASS — Exemplary |
| 8/9 | PASS — Acceptable |
| 7/9 | CONDITIONAL — Fix gap before customer delivery |
| <7 | FAIL — Redo |

---

## Integration with iCE Cognitive Compass V02R01

| Touchpoint | Agent / Skill | Responsibility |
|---|---|---|
| **Skill** (rules home) | `b2b-presentation-creator` V01R02 | Charter resides here as `references/12-quality-charter.md` |
| **Pre-Build Gate** | `presentation-generator-agent` V01R03 — Phase A.5 | Charter Compliance Gate before slide build |
| **Post-Build Gate** | `qa-master-agent` V01R02 — Dimension 6 | Validate Charter 9-item checklist + score ≥8/9 |
| **Backward Compat** | `/Users/xpickey/Documents/Claude/B2B_DECK_QUALITY_CHARTER.md` | Standalone reference, note authoritative source = this file |

---

## Bilingual Note

Charter rules apply equally to Thai and English language decks. Specific calibration

- Thai customer C-suite decks: TH primary copy + EN technical terms parenthetical
- Hero numbers: Thai uses Arabic numerals (no Thai numerals) per business convention
- Color semantics: identical (Green/Red/Slate/Navy/Accent)
- Section labels: Thai labels also require single-line rendering — text-box width is the constraint

---

*Charter Version V01R02 | Date 2026.05.19*
*Authoritative source in `b2b-presentation-creator.skill` V01R02 ZIP*
*Re-read at the start of every B2B deck task*
