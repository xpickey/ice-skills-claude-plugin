# Layout Templates — B2B Presentation Creator

## Overview

This folder contains **12 canonical slide layouts** and **4 deck-type templates** that map each slide of a standard B2B presentation to its layout pattern.

---

## The 12 Canonical Layouts

These layout patterns are the building blocks of all B2B decks. Each layout defines:
- **Slide structure** (how content is arranged)
- **Content zones** (where text, images, icons, and charts go)
- **Grid patterns** (1-column, 2-column, 3-column, grid)
- **Visual hierarchy** (headers, body, callouts)

| # | Layout Name | Pattern | Best For |
|---|---|---|---|
| 1 | **hero** | Full-bleed image + large text overlay | Title slides, impact statements |
| 2 | **title-hero** | Centered title + subtitle + date | Deck opening, section breaks |
| 3 | **two-column** | Left column (text/logo) + right column (image/stat) | About us, before/after, comparisons |
| 4 | **icon-text-rows** | 3–5 rows: icon + title + description | Agendas, features, capabilities, next steps |
| 5 | **question-led** | 3–5 open questions, formatted for discussion | Discovery slide 4, ideation prompts |
| 6 | **half-bleed-image** | Large image left + 3–5 stat callouts right | Context slides, industry trends |
| 7 | **2x2-grid** | Four quadrants: icon/image + title + text | Pain points, features, options |
| 8 | **2x3-grid** | Six boxes: icon/image + title + text | Pain points, capabilities, outcomes |
| 9 | **process-flow** | 3–5 numbered boxes connected by arrows | Engagement model, methodology, workflow |
| 10 | **phased-timeline** | Timeline with phases, durations, milestones | Implementation, roadmap, project plan |
| 11 | **stat-callout** | Large number + label + supporting text | Key findings, metrics, single-stat slides |
| 12 | **stat-callout-grid** | 3–4 stat callouts in a grid | Customer references, multiple KPIs, outcomes |

---

## Deck-Type Templates

Each JSON file defines a complete deck structure. Use these to build consistent, proven slide sequences.

### File Structure

```json
{
  "name": "Deck Type Display Name",
  "description": "When to use this deck",
  "length": "8-12 slides",
  "slides": [
    {
      "slide": 1,
      "layout": "hero",
      "purpose": "Title",
      "speaker_notes": "Open with customer name and meeting context"
    }
  ]
}
```

---

## Included Templates

### 1. Discovery & Qualification Deck
**File:** `discovery-deck.json`  
**When:** First or second meeting. Goal: surface pain, qualify fit.  
**Length:** 8–12 slides

| Slide | Layout | Purpose |
|-------|--------|---------|
| 1 | title-hero | Title |
| 2 | icon-text-rows | Agenda (3–5 items) |
| 3 | two-column | About Us — short version |
| 4 | question-led | What We Want to Understand |
| 5 | half-bleed-image | Industry Context |
| 6 | 2x3-grid | Where Companies Get Stuck |
| 7 | two-column | What Good Looks Like |
| 8 | process-flow | How We Typically Help |
| 9 | icon-text-rows | What We'd Need from You |
| 10 | phased-timeline | Next Steps |
| 11 (opt) | stat-callout-grid | Case Studies (appendix) |
| 12 (opt) | title-hero | Q&A (appendix) |

---

### 2. Solution & Demo Deck
**File:** `solution-demo-deck.json`  
**When:** Solutioning stage. Champion + senior stakeholders.  
**Length:** 12–18 slides

| Slide | Layout | Purpose |
|-------|--------|---------|
| 1 | title-hero | Title |
| 2 | stat-callout | Why We're Here |
| 3 | 2x3-grid | What We Heard |
| 4 | two-column | What Success Means to You |
| 5 | process-flow | Our Approach |
| 6 | half-bleed-image | Solution Architecture |
| 7 | 2x3-grid | Module / Capability Map |
| 8 | half-bleed-image | Walkthrough — Day in the Life |
| 9 | icon-text-rows | Where the Magic Happens |
| 10 | half-bleed-image | Integration & Data |
| 11 | icon-text-rows | Security & Compliance |
| 12 | phased-timeline | Implementation Approach |
| 13 | stat-callout-grid | Customer References |
| 14 | icon-text-rows | What We Need from You |
| 15 | phased-timeline | Suggested Next Steps |
| 16–18 | various | Appendix |

---

### 3. Proposal & Business Case Deck
**File:** `proposal-deck.json`  
**When:** Late-stage sale. Board/C-suite approval.  
**Length:** 18–25 slides

| Slide | Layout | Purpose |
|-------|--------|---------|
| 1 | title-hero | Title (with version, date) |
| 2 | two-column | Executive Summary |
| 3 | stat-callout | Situation Today |
| 4 | two-column | Why This Matters Now |
| 5–7 | stat-callout (×3) | What We Heard (pain themes) |
| 8 | two-column | What Success Looks Like |
| 9 | half-bleed-image | Solution Overview |
| 10 | 2x3-grid | Solution — How It Solves Each Pain |
| 11 | icon-text-rows | Differentiators — Why Us |
| 12 | phased-timeline | Implementation Approach |
| 13 | half-bleed-image | Team and Roles |
| 14 | icon-text-rows | Investment Summary (table) |
| 15 | 2x3-grid | Total Cost of Ownership (TCO) |
| 16 | 2x3-grid | Return on Investment (ROI) |
| 17 | 2x3-grid | Risk and Mitigation |
| 18 | stat-callout-grid | Customer References |
| 19 | stat-callout | Why Us — Closing |
| 20 | icon-text-rows | What We Need to Move Forward |
| 21–25 | various | Appendix |

---

### 4. Customer Success & QBR Deck
**File:** `qbr-deck.json`  
**When:** Quarterly / annual review with existing customer.  
**Length:** 10–15 slides

| Slide | Layout | Purpose |
|-------|--------|---------|
| 1 | title-hero | Title (Q/Year) |
| 2 | two-column | Executive Summary |
| 3 | stat-callout | Where We Started |
| 4 | stat-callout-grid | What We've Delivered |
| 5 | 2x3-grid | Health Score Scorecard |
| 6 | icon-text-rows | Wins This Quarter |
| 7 | icon-text-rows | What Didn't Land |
| 8 | 2x3-grid | Adoption Metrics (charts) |
| 9 | phased-timeline | Roadmap — What's Next from Us |
| 10 | icon-text-rows | What We're Asking from You |
| 11 | two-column | Renewal / Expansion Conversation |
| 12 | two-column | Risks We're Watching |
| 13 | phased-timeline | Mutual Action Plan |
| 14–15 | various | Appendix |

---

## How to Use These Templates

1. **Choose a deck type** based on the meeting stage and audience.
2. **Load the corresponding JSON file** → it lists all slides and their layouts.
3. **Use layout patterns** as a content template → each layout defines what goes where.
4. **Follow the speaker notes** to understand intent and content rules.

Example: Building Slide 8 of a Solution Demo Deck
- **Layout:** `half-bleed-image`
- **Purpose:** "Walkthrough — Day in the Life"
- **Content rule:** Persona-led scenario, 5–7 frames showing how a key user gets work done.

---

## Layout Design Principles

- **Structure, not design:** Each layout defines content zones, not colors or fonts.
- **Consistent hierarchy:** All layouts use similar visual weighting for titles, body, callouts.
- **Flexible content:** Same layout works for text, images, charts, or mixed content.
- **Readable at any size:** Works on 16:9 (standard), 4:3 (older rooms), and mobile.

---

## Next Steps

- Open a deck-type JSON file and map its slides.
- Use the layout reference to fill each slide with content.
- Refer to `/references/06-layouts.md` for detailed layout specs and examples.
- See `/references/07-infographics.md` for diagram and chart patterns.

---

**End of layouts/README.md.** Refer to individual JSON files for specific deck structures.
