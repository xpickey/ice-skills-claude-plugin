---
name: sales-pipeline-report
description: >
  Generate executive-grade Sales Pipeline reports from CRM Excel data — as a PowerPoint deck,
  Excel workbook, or structured markdown — using a clean visual design system with stage-based
  categorization (WIN / FOCUS / AT RISK / ACTIVE / EARLY), NetNew vs Recurring revenue split, and quarterly
  breakdowns. Use this skill whenever the user uploads or references a sales pipeline Excel file
  and wants any kind of report, deck, summary, or visualization — even if they just say "generate
  the pipeline report", "make slides from this data", "pipeline deck", or "pipeline summary".
  Also trigger when the user mentions CRM stage mapping, committed deals, or wants to analyze
  deal pipeline by quarter or product. Pairs with the pptx skill when output is a presentation.
---

# Sales Pipeline Report Skill

## Overview

This skill guides Claude through the full workflow of transforming CRM pipeline Excel data into
an executive-ready report. It handles common data quality issues, applies a configurable stage
mapping, and supports multiple output formats.

**Always read this file completely before starting.** Then check `references/` for output-specific guides.

---

## Step 1 — Understand the Source Data

### Expected Excel Structure

Pipeline exports typically arrive as multi-sheet Excel files. Common patterns:

| Sheet Name | Content | Watch For |
|---|---|---|
| Implementation / Imp-Service | Project/service deals | Usually NetNew |
| Software / Sale-SW | License + Maintenance + Subscription | Mix of NetNew + Recurring |
| AMS / Managed Services | Ongoing managed service deals | Often duplicated — see §Data Issues |
| Raw / All Deals | Full unfiltered export | May need pivot/filter |

**Standard columns to look for:**
```
Products/Services | Company Name | Opportunity Name | Stage | Q1 | Q2 | Q3 | Q4 | Grand Total
```

If column names differ, ask the user or infer from context. Fiscal year (e.g., 2026-Q1) may be embedded in column headers.

### Revenue Classification

| Type | Definition | Typical Sources |
|---|---|---|
| **NetNew** | One-time project/implementation revenue | Implementation, new license |
| **Recurring** | Annual/ongoing revenue | AMS, SW Subscription, SW Maintenance, Renewals |

Classify deals by product/service name when no explicit flag exists.

---

## Step 2 — Data Validation & Known Issues

### ⚠️ Run These Checks Before Computing Any Numbers

**Issue 1 — Duplicate Sheet (AMS = Copy of SW)**
- Symptom: Two sheets have identical Grand Total values
- Fix: Drop the duplicate. Source AMS figures from the previous file version, a separate sheet, or ask the user
- Flag clearly in the report as a data note

**Issue 2 — Decommitted Deals**
- Symptom: Rows where Grand Total = 0 (still appear in pivot)
- Fix: Exclude from all calculations; optionally count separately as "decommitted deals: N"

**Issue 3 — Missing Business Unit Column**
- Symptom: Pivot-only export lacks BU dimension
- Fix: Apply BU mapping if user provides one; otherwise group by Product/Service as proxy
- Note in report: "BU breakdown estimated from product category"

**Issue 4 — Stage Inconsistencies**
- Symptom: Typos, extra spaces, inconsistent capitalization in Stage column
- Fix: Normalize before mapping (strip, lowercase, fuzzy match to known stages)

---

## Step 3 — Stage → Category Mapping

Map CRM stages to 4 executive categories. This mapping is **configurable** — ask the user if their CRM uses different stage names.

### Default Mapping

| CRM Stage Pattern | Category | Icon | Meaning |
|---|---|---|---|
| `Won`, `Closed Won`, `Waiting Invoice`, `A++` | **WIN** | ✅ | Revenue secured |
| `Award`, `PO`, `Done Nego`, `On Purchasing`, `On Renewal`, `A+`, `A:` | **FOCUS** | 🔥 | High-probability, needs closing action |
| `May Loss`, `On Recover`, `B:` | **AT RISK** | ⚠️ | Deal in jeopardy — may-loss or in recovery; in pipeline but slipping |
| `Proposal`, `Decision Maker`, `Develop Sponsor`, `C:`, `D:` | **ACTIVE** | 🎯 | Active pursuit, outcome uncertain |
| `Opportunity Identified`, `Gathering Req`, `S:` | **EARLY** | 🌱 | Early stage, long-range pipeline |

**Mapping logic:**
```python
def map_stage(stage: str) -> str:
    # Match order: WIN → FOCUS → AT RISK → ACTIVE → EARLY. First match wins.
    s = stage.strip().lower()
    if any(x in s for x in ["won", "closed", "invoice", "a++"]):
        return "WIN"
    elif any(x in s for x in ["award", "po", "nego", "purchasing", "renewal", "a+", "a:"]):
        return "FOCUS"
    elif any(x in s for x in ["may loss", "recover", "b:"]):
        return "AT RISK"
    elif any(x in s for x in ["proposal", "decision", "develop", "c:", "d:"]):
        return "ACTIVE"
    else:
        return "EARLY"
```

---

## Step 4 — Compute the Numbers

After validation and mapping, compute these standard metrics:

```
TOTAL COMMITTED = Sum of all non-zero Grand Total values across all sheets (deduplicated)

Per Category (WIN / FOCUS / AT RISK / ACTIVE / EARLY):
  - Total amount
  - Deal count
  - NetNew subtotal
  - Recurring subtotal
  - Quarterly breakdown (Q1–Q4) for both NetNew and Recurring

Per Product/Service:
  - Total amount
  - Category breakdown

Per Quarter (Q1–Q4):
  - Total by category
  - NetNew vs Recurring split
```

Organize results in a clean data structure before building output.

---

## Step 5 — Choose Presentation Theme

Before building output, determine which visual theme to apply:

| Theme | File | When to Use |
|---|---|---|
| **Midnight Executive** | `references/design-system.md` | Internal decks, board/management reporting, dark-mode preference |
| **Zen Sales Pipeline** | `references/theme-zen.md` | Client-facing presentations, minimalist/APAC brand environments, Japanese-style |

**Selection logic:**
- User says "zen", "minimalist", "clean", "Japanese style", "client-facing", "white background" → use `theme-zen.md`
- User says "dark", "executive", "midnight", "navy" → use `design-system.md`
- No preference stated → default to **Midnight Executive** and note the alternative exists

Load only the selected theme file. The two theme files are **drop-in replacements** — all slide structure, data logic, and chart types remain the same; only colors, typography, card/table styling, and spacing change.

---

## Step 6 — Choose Output Format

Ask the user (or infer from context) which output they need:

| Format | When to Use | Guide |
|---|---|---|
| **PowerPoint (.pptx)** | Executive presentation, board/management reporting | See `references/pptx-structure.md` + use pptx skill |
| **Excel (.xlsx)** | Data-first summary, for further analysis | See `references/excel-structure.md` |
| **Markdown / Text** | Quick summary, email, or Slack update | Use standard markdown tables |
| **Multiple** | User wants both deck and data workbook | Generate sequentially |

---

## Step 6 — Build the Output

Go to the relevant reference file for detailed build instructions:

- **PowerPoint** → read `references/pptx-structure.md` (slide-by-slide blueprint) + selected theme file
- **Excel** → read `references/excel-structure.md` (sheet layout + formatting rules)
- **Markdown** → structure using standard markdown tables, apply theme colors as notes

Also read and follow the **pptx skill** (`/mnt/skills/public/pptx/SKILL.md`) when generating .pptx.

---

## Step 6.5 — Typography & Bilingual Font QA

**Mandatory gate before saving any .pptx, .xlsx, .docx, or .pdf output.**
Runs after Step 6 (Build) and before Step 7 (Quality Checks).

### When to Apply

| Trigger | Action |
|---|---|
| Output is .pptx / .xlsx / .docx / .pdf | **Mandatory** — run full QA |
| Output is Markdown / inline text | Skip — no font rendering |
| User explicitly says "skip QA" | Skip, but log warning in Pre-Save Confirmation |

### Approved Font Pairs (Thai + English)

Use font pairs designed for matching x-height. **Never mix mismatched pairs.**

| Use Case | Thai Font | English Font |
|---|---|---|
| **Business / Pipeline Deck** (default) | Sarabun | Inter |
| **Executive / Board** | IBM Plex Sans Thai | IBM Plex Sans |
| **Modern Sales Pitch** | Kanit (Display) + Sarabun (Body) | Montserrat (Display) + Inter (Body) |
| **Government / ราชการ** | TH Sarabun New 16pt | Times New Roman 14pt |
| **Academic** | TH Sarabun New 16pt | Times New Roman 12pt |

**Forbidden combinations** (x-height mismatch causes Thai to render visibly smaller):
- ❌ Cordia New + Arial
- ❌ Browallia New + Calibri
- ❌ Angsana New + Times
- ❌ TH Sarabun New + Helvetica
- ❌ Sarabun + Arial

### Consistency Rules

- **Max 2 font families** per document (Display + Body)
- **1 font family per object** (heading, paragraph, table cell)
- **Max 3 weights** in body text (Regular, SemiBold, Bold)
- **Font size scale** consistent (e.g., 10/12/14/18/24/32 — not 11.5/13.7)

### Bilingual Size Compensation

When Thai and English appear in the **same object** (slide title, chart label,
table header), apply size adjustment if the pair has unequal x-height:

| Font Pair | Thai Size Adjustment |
|---|---|
| Sarabun + Inter | +0% (matched) |
| Noto Sans Thai + Noto Sans | +0% (matched) |
| IBM Plex Thai + IBM Plex Sans | +0% (matched) |
| Kanit + Montserrat | +0% (matched) |
| TH Sarabun New + Times New Roman | **+25–33%** |
| TH Sarabun New + Arial | **+20–25%** |
| Sarabun + Arial | **+10–15%** |

**Example:** if English is 14pt Arial, Thai TH Sarabun New must be set
to 16–18pt to appear the same visual size.

### Pre-Save QA Checklist

Run these before Step 7. Report findings to the user:

- [ ] Font families ≤ 2 across the document
- [ ] Font pair is on the Approved list (or matches Document Type default)
- [ ] No font from Forbidden combinations
- [ ] Thai and English in the same object look the same visual size
- [ ] If using mismatched pair, size compensation applied per table above
- [ ] Heading hierarchy clear and consistent
- [ ] Line spacing ≥ 1.4 for Thai body text (room for tone marks)
- [ ] Government docs: TH Sarabun New 16pt body
- [ ] Numbers in tables use tabular-figure variant where available

### Defect Report Template

If defects found, report to user before saving:

```
TYPOGRAPHY QA REPORT — [Document Name]
─────────────────────────────────────
Font Families: [list]
Font Sizes:    [list]

Defects: [N]
[1] Slide X — Thai (14pt Sarabun) renders smaller than English (14pt Calibri)
    Fix: Replace Calibri → Inter (matched x-height with Sarabun)
[2] Slide Y — 3 font families used (Sarabun + Inter + Calibri)
    Fix: Standardize to Sarabun + Inter

Recommendation: [Apply fixes / Save with warning / User decides]
```

### Default Recommendation for This Skill

Sales Pipeline Reports default to **Sarabun + Inter** pairing because:
- Both fonts are weight-matched (Regular/Medium/SemiBold/Bold available)
- x-height is balanced — no compensation needed in mixed-language titles
- Both render well in PowerPoint, Excel, and PDF
- Open-source and freely available

If the user chose **Zen Sales Pipeline** theme (Step 5), confirm the theme
file's font specification overrides this default. If **Midnight Executive**
theme, this default applies unless theme file specifies otherwise.

---

## Step 7 — Quality Checks

Before presenting output to the user:

- [ ] Total committed matches sum of all sheets (minus duplicates)
- [ ] WIN + FOCUS + AT RISK + ACTIVE + EARLY = Grand Total
- [ ] NetNew + Recurring = Grand Total per category
- [ ] Q1 + Q2 + Q3 + Q4 = Annual total per category
- [ ] No decommitted deals (Grand Total = 0) included in figures
- [ ] AMS duplicate sheet issue documented if present
- [ ] All stage values successfully mapped (no "UNKNOWN" category)

---

## Communicating with the User

- **Always state data issues found** and how you resolved them (e.g., "AMS sheet was a duplicate — used prior file value of ฿46.1M")
- **Show a validation summary** before building output: key totals, deal counts, any anomalies
- **Ask before assuming** on BU mapping, fiscal year, or stage names that don't match defaults
- **Currency**: Use whatever currency appears in the data; default to showing values in millions (e.g., ฿312.8M) for executive summaries

---

## Reference Files

| File | Purpose |
|---|---|
| `references/pptx-structure.md` | Slide-by-slide blueprint for executive deck (11 slides) |
| `references/design-system.md` | **Theme: Midnight Executive** — navy/dark color palette, fonts, card/table specs |
| `references/theme-zen.md` | **Theme: Zen Sales Pipeline** — Japanese minimalist white palette, specs, role views |
| `references/excel-structure.md` | Excel output sheet layout and formatting |

---

**Version:** V01R05 | **Date:** 2026-06-14
**Change:** Added new **AT RISK** category (icon ⚠️). Stages `May Loss`,
`On Recover`/`recover`, and the `B:` prefix moved from ACTIVE → AT RISK;
ACTIVE narrows to `C:`, `D:`, `Proposal`, `Decision Maker`, `Develop Sponsor`.
AT RISK counts in the active pipeline total (WIN + FOCUS + AT RISK + ACTIVE +
EARLY = Grand Total). New match order: WIN → FOCUS → AT RISK → ACTIVE → EARLY.
Applied in trilogy lockstep with `ice-sale-pipeline-report` V04R01 and
`ice-sale-pipeline-dashboard` V04R01. **Note:** this skill's WIN/FOCUS still
maps `A+` to FOCUS (the A+→WIN promotion in `ice-sale-pipeline-report` V03R01
was NOT back-ported here — out of scope for the AT RISK change; flag if mixing
outputs).
**Prior versions:**
- V01R04 (2026-05-19) — Bundled 4 reference files into the .skill ZIP as a
  self-contained package. Skill logic unchanged from V01R03.
- V01R03 (2026-05-13) — Added Step 6.5 Typography & Bilingual Font QA
  (mandatory gate before saving .pptx / .xlsx / .docx / .pdf). Defaults
  to Sarabun + Inter for bilingual Thai-English consistency.
- V01R02 — Stage mapping change.
- V01R01 — Initial release.
