# Reference 01 — Deck Type Blueprints

This reference defines the four standard B2B deck types. Each blueprint specifies the slide-by-slide structure, the recommended layout for each slide, and the content patterns proven to land with enterprise audiences.

Use this file once Step 1 of the workflow has classified the deck.

---

## Table of Contents

1. [Discovery & Qualification Deck](#1-discovery--qualification-deck)
2. [Solution & Demo Deck](#2-solution--demo-deck)
3. [Proposal & Business Case Deck](#3-proposal--business-case-deck)
4. [Customer Success & QBR Deck](#4-customer-success--qbr-deck)
5. [Hybrid Decks and Variations](#5-hybrid-decks-and-variations)

---

## 1. Discovery & Qualification Deck

**When to use:** First or second meeting. Champion or working team. Goal is to surface pain, qualify fit, and earn the right to a solution conversation.

**Audience:** Champion, mid-level operators, occasionally a senior sponsor for the close.

**Length:** 8–12 slides.

**Tone:** Question-led, curious, low-pressure. The deck is a conversation prompt, not a pitch.

### Slide Blueprint

| # | Slide | Layout (from `06-layouts.md`) | What goes on it |
|---|---|---|---|
| 1 | Title | Hero / Half-bleed | Customer name + meeting purpose ("Discovery Conversation") + date |
| 2 | Agenda | Icon + text rows (3–5 items) | What we'll cover, with timestamps if helpful |
| 3 | About Us — short | Two-column (logo + 3 stats) | One-paragraph who-we-are, NO product features |
| 4 | What We Want to Understand | Question-led | 3–5 open questions framed for discussion |
| 5 | Industry Context | Half-bleed image + 3 stats | Macro trends in customer's industry |
| 6 | Where Companies Like Yours Get Stuck | 2x2 or 2x3 grid | 4–6 pain themes, each with a 1-line description |
| 7 | What Good Looks Like | Two-column | Outcome states for the same pain themes |
| 8 | How We Typically Help | Process flow (numbered steps) | 3-step or 5-step engagement model — high level |
| 9 | What We'd Need from You | Icon + text rows | Information / access / sponsor commitments |
| 10 | Next Steps | Numbered timeline | Concrete actions with owners and dates |
| 11 (optional) | Appendix — Case studies | Stat callout grid | 1–3 anonymized references, only if customer asks |
| 12 (optional) | Appendix — Q&A | Title only | Holding slide for live discussion |

### Content Pattern Rules

- **Slide 4** should have between 3 and 5 questions, each phrased as an open question (no yes/no). Format: "What does success look like for [team] over the next 12 months?" not "Are you happy with the current system?"
- **Slide 6** uses pain language pulled from the customer's industry — avoid generic "lack of visibility" boilerplate. If you don't know specific pains, ask the user to fill them in before building.
- **Slide 8** must be vendor-neutral and product-neutral. Discovery is too early for product names.
- **Slide 10** always has owners and dates. If they're unknown, mark as `[NEED FROM USER]`.

---

## 2. Solution & Demo Deck

**When to use:** Solutioning stage. Champion has been qualified; senior stakeholders are joining. Goal is to show how the proposed solution maps to the customer's pain, and to set up a credible technical conversation.

**Audience:** Champion + Economic Buyer + technical evaluators (CIO / CTO / Head of Operations).

**Length:** 12–18 slides.

**Tone:** Confident, evidence-led. The deck mixes narrative with visual storytelling.

### Slide Blueprint

| # | Slide | Layout | What goes on it |
|---|---|---|---|
| 1 | Title | Hero / Half-bleed | Customer name + "Proposed Solution" + date |
| 2 | Why We're Here | Stat callout (large) | One-sentence framing of the customer's central challenge |
| 3 | What We Heard | 2x3 grid | 4–6 pain points captured during discovery, each in customer language |
| 4 | What Success Means to You | Two-column | Outcome statements, ideally quoted from the discovery transcript |
| 5 | Our Approach | Process flow (3–5 phases) | The engagement / methodology at a glance |
| 6 | Solution Architecture | Workflow diagram | High-level diagram — components, integrations, key data flows |
| 7 | Module / Capability Map | 2x2 or 2x3 grid | Modules or capabilities, each tied to one pain point from slide 3 |
| 8 | Walkthrough — Day in the Life | Workflow / storyboard | Persona-led scenario. 5–7 frames showing how a key user gets work done |
| 9 | Where the Magic Happens | Icon + text rows | 3–5 differentiators, each a sentence + one supporting fact |
| 10 | Integration & Data | Workflow diagram | Existing systems + planned integrations + data flow direction |
| 11 | Security & Compliance | Icon + text rows | 3–5 standards/controls (ISO 27001, PDPA, etc.) — see `legal-it-thailand-cloud` skill |
| 12 | Implementation Approach | Phased timeline | Phases with weeks/months, not specific dates |
| 13 | Customer References | Stat callout grid | 1–3 references from same industry or similar size |
| 14 | What We Need from You | Icon + text rows | Decisions, access, sponsorship commitments |
| 15 | Suggested Next Steps | Numbered timeline | 3–5 actions with owners and dates |
| 16–18 | Appendix | Various | Detail slides held in reserve (data model, deeper architecture, screenshots) |

### Content Pattern Rules

- **Slide 6 (Solution Architecture)** must be a real diagram, not a list of components. Use the workflow infographic patterns in `references/07-infographics.md`. If the architecture is technical, prepare an executive version (slide 6) AND a technical version (appendix).
- **Slide 8 (Day in the Life)** is the highest-leverage slide in this deck. Spend disproportionate effort here. Persona must be specific (e.g. "Khun Somchai, AP Specialist"), not a generic "user".
- **Slide 11 (Security)** — never name-drop standards you can't actually deliver against. If the deal is for Thai government, pull the right standards from `legal-it-thailand-cloud` and `advisor-govt-gfmis` references.

---

## 3. Proposal & Business Case Deck

**When to use:** Late-stage sale. Proposal submission, executive readout, or board approval support. Goal is to win the commercial decision.

**Audience:** Economic Buyer + C-suite + procurement + sometimes board members.

**Length:** 18–25 slides (often paired with a separate detailed proposal document).

**Tone:** Executive, evidence-rich, financially literate. Every claim is supported by a number or a citation.

### Slide Blueprint — the "Why Invest / Why Now / Why Us" structure

| # | Slide | Layout | What goes on it |
|---|---|---|---|
| 1 | Title | Hero | Customer + Proposal Title + Version + Date |
| 2 | Executive Summary | Two-column | Recommendation in one sentence + 3 key reasons in supporting bullets |
| 3 | Situation Today | Stat callout | The customer's current state, in their own numbers |
| 4 | Why This Matters Now | Two-column with icons | Macro pressure / regulatory / competitive trigger |
| 5–7 | What We Heard (×3 themes) | Stat callout per theme | Each pain theme as a separate slide with supporting numbers |
| 8 | What Success Looks Like | Two-column (before / after) | Quantified target state |
| 9 | Our Solution — Overview | Workflow diagram | Solution architecture at a high level |
| 10 | Solution — How It Solves Each Pain | 2x3 grid | Pain → Solution mapping, one row per pain |
| 11 | Differentiators — Why Us | Icon + text rows | 3–5 specific differentiators, each with proof |
| 12 | Implementation Approach | Phased timeline | Phases, durations, key milestones |
| 13 | Team and Roles | Photo grid + responsibilities | Named team + experience + RACI |
| 14 | Investment Summary | Table | Pricing breakdown — software / services / support — with currency clearly stated |
| 15 | Total Cost of Ownership (TCO) | Stacked bar chart | 3-year or 5-year TCO with line items |
| 16 | Return on Investment (ROI) | Waterfall + key stats | Quantified benefits, payback period, NPV/IRR if relevant |
| 17 | Risk and Mitigation | Two-column or 2x3 grid | Top 5 risks + mitigation for each |
| 18 | Customer References | Logo grid + stats | Logos with one-line outcomes |
| 19 | Why Us — Closing | Stat callout | One number that proves the firm can deliver |
| 20 | What We Need to Move Forward | Icon + text rows | Decision needed + by when |
| 21–25 | Appendix | Various | Methodology / org chart / detailed pricing / security / SLAs |

### Content Pattern Rules

- **Slides 5–7** — pull the pain themes from the discovery deck (slide 6 of Discovery deck). Same language.
- **Slide 14 (Investment Summary)** — currency must be explicit (THB / USD / EUR). Show net + VAT separately for Thai customers.
- **Slide 16 (ROI)** — never invent benefits. Every benefit line item must come from a real customer statement, an industry benchmark with citation, or a vendor-published case study (cited).
- **Slide 17 (Risks)** — list real risks honestly. Vague "low risk" claims signal that the seller hasn't thought about it.

### Specific Guidance for Thai Government / e-GP Bids

When this is a TOR/RFP response for Thai government:
- Slide 1 must show the TOR reference number and submission date prominently.
- The cover language should match the TOR (Thai-led).
- Slides 14–16 must follow Thai government cost categories from the relevant พรบ. and ระเบียบ (see `govt-egp-gfmis` skill).
- Add an appendix slide listing compliance with each TOR section by paragraph number.

---

## 4. Customer Success & QBR Deck

**When to use:** Quarterly or annual review with an existing customer. Goal is to demonstrate value delivered, surface risks, and tee up renewal or expansion.

**Audience:** Champion + executive sponsor; sometimes the original Economic Buyer.

**Length:** 10–15 slides.

**Tone:** Outcome-focused, candid. Acknowledge what didn't work alongside what did.

### Slide Blueprint

| # | Slide | Layout | What goes on it |
|---|---|---|---|
| 1 | Title | Hero | Customer + "Quarterly Business Review — Q[N] [YYYY]" + date |
| 2 | Executive Summary | Two-column | Health score + headline outcomes + headline asks |
| 3 | Where We Started | Stat callout (before) | Original objectives and starting state |
| 4 | What We've Delivered | Stat callout grid | 3–5 outcomes with numbers |
| 5 | Health Score | Dashboard layout | Scorecard across adoption / value / advocacy / risk |
| 6 | Wins This Quarter | Icon + text rows | 3–5 specific wins with named teams or users |
| 7 | What Didn't Land | Icon + text rows | Honest list of missed targets, with diagnosis |
| 8 | Adoption Metrics | Charts grid | Logins / active users / module adoption / data quality — with trend lines |
| 9 | Roadmap — What's Next from Us | Phased timeline | Upcoming features, releases, services |
| 10 | What We're Asking from You | Icon + text rows | Customer commitments / data / sponsor time |
| 11 | Renewal / Expansion Conversation | Two-column | If renewal in <6 months: terms, timing, value justification |
| 12 | Risks We're Watching | Two-column or 2x3 grid | Top 3 risks with action plans |
| 13 | Mutual Action Plan | Numbered timeline | Joint actions with owners and dates |
| 14–15 | Appendix | Various | Detailed metrics, support ticket summary, escalation log |

### Content Pattern Rules

- **Slide 5 (Health Score)** — use a clear visual scorecard. Avoid traffic-light only; show the underlying metric.
- **Slide 7 (What Didn't Land)** — this slide builds trust. Skip it and the deck reads as marketing.
- **Slide 11 (Renewal)** — only include if renewal is within 6 months. Otherwise hold for the next QBR.

---

## 5. Hybrid Decks and Variations

Sometimes a single deck needs to span stages. Common hybrids:

| Hybrid | Combine slides from… | Length |
|---|---|---|
| **Discovery → Solution Pitch** (one-shot meetings) | Discovery #1–7 + Solution #6–10, #14, #15 | 14–16 |
| **Solution Workshop** (full-day envisioning) | Discovery #4 + Solution #1–12 + ideation breakout slides | 18–22 |
| **Executive Briefing** (30-min C-suite touch) | Proposal #1, #2, #11, #16, #19, #20 | 6–8 |
| **Account Plan Internal Readout** | Discovery #6 + Proposal #11, #18 + custom internal slides | 10–12 |

For hybrids, always confirm the time slot first — that determines slide count more than anything else.

**Time-to-slide guideline:**
- 15-minute slot: 4–6 slides
- 30-minute slot: 8–10 slides
- 60-minute slot: 12–18 slides
- Half-day workshop: 18–25 slides + breakout artifacts

---

## When in doubt

Ask the user:

> "ขอเรียนสอบถามเพิ่มเติมเพื่อให้ Deck ตรงสถานการณ์ครับ:
> 1. **เวทีนี้ใช้เวลาเท่าใด** ครับ? (15 นาที / 30 นาที / 60 นาที / Workshop)
> 2. **ผู้ฟังหลัก** เป็นใครครับ? (Champion / Economic Buyer / C-suite / ทีมงาน)
> 3. **ผลลัพธ์ที่ต้องการ** จากเวทีนี้คืออะไรครับ? (เปิดประตู / Qualifying / Solution buy-in / Commercial close / Renew)"

The answers map directly to deck type and length.

---

**End of 01-deck-types.md.** Continue to `02-themes-industry.md` for theme selection, or `06-layouts.md` for layout patterns.
