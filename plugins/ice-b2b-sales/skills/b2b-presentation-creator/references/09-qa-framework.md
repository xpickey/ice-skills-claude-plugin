# Reference 09 — QA Framework

This is the quality assurance framework for every deck this skill produces. The QA pass is mandatory; skipping it produces decks that look fine in code review but fail when displayed.

The framework has two halves:
1. **5-Dimensional Visual Review** — adapted from design critique practice. Catches design and usability issues.
2. **Content Integrity Review** — catches placeholders, fabricated facts, missing logos, bilingual rendering errors.

Both halves must pass before declaring the deck done.

---

## 1. The Five Dimensions

Every deck is reviewed across five dimensions. Each dimension has explicit checks and a severity level.

| Dimension | What it asks | Critical issues | Moderate issues | Minor issues |
|---|---|---|---|---|
| **First Impression** | Does the deck land in 2 seconds? | Title doesn't communicate purpose; theme fights the customer's brand; opening slide is a wall of text | Hero image is generic stock; subhead is missing | Title kerning slightly off |
| **Usability** | Can the audience follow the story? | Slide order doesn't make sense; key argument missing; CTA absent | Section dividers unclear; transitions abrupt | Some bullets phrased passively |
| **Visual Hierarchy** | Are the right elements emphasized? | Title same size as body; stat callouts not visually dominant | Some slides lack a focal point; mixed emphasis weights | One headline slightly smaller than its sibling |
| **Consistency** | Is the theme applied uniformly? | Multiple colors fighting each other; mixed icon families; mixed font families across slides | One slide uses different font; inconsistent corner radius | Slight spacing variance between slides |
| **Accessibility** | Does it work for all viewers? | Body text below 4.5:1 contrast; touch targets <44pt for interactive overlays | Caption text below 4.5:1; small font on busy background | Color-only signal (no shape backup) |

### How to Score

- **Critical (red)** — must fix before delivery. Will damage credibility.
- **Moderate (yellow)** — should fix in this iteration. Audience may not notice but a sharp reviewer will.
- **Minor (green)** — flag and fix if time allows.

---

## 2. The Visual QA Workflow

This is the operational sequence for running QA on a generated deck.

### Step 1 — Generate slide images

```bash
# Convert .pptx to PDF then to images at 150dpi
python scripts/office/soffice.py --headless --convert-to pdf "Deck.pptx"
pdftoppm -jpeg -r 150 "Deck.pdf" slide
ls slide-*.jpg
```

`pdftoppm` zero-pads filenames based on slide count. Decks under 10 slides become `slide-1.jpg`, 10–99 become `slide-01.jpg`, 100+ become `slide-001.jpg`. Use the names actually printed by `ls`.

### Step 2 — Dispatch the visual QA subagent (REQUIRED for ≥5 slides)

You are the deck author; you've been staring at the code and will see what you expected, not what's there. A subagent has fresh eyes.

Dispatch with this prompt template:

```
Visually inspect these B2B presentation slides as if you were a senior design reviewer.
Assume there are issues — find them. Report ALL issues, even minor.

Across each slide, evaluate:

1. FIRST IMPRESSION (2-second test)
   - What draws the eye first? Is it the right element?
   - Does the slide's purpose land instantly?

2. USABILITY
   - Can a viewer skim and grasp the key message?
   - Is the reading order obvious?
   - Are CTAs / next-action callouts unambiguous?

3. VISUAL HIERARCHY
   - Title 36pt+ vs body 14-16pt — clear?
   - Stat callouts visually dominant where used?
   - Is there a focal point per slide?

4. CONSISTENCY
   - Does the theme color stay primary on all slides?
   - Same font family (header / body) throughout?
   - Same icon family (e.g. all Lucide)?
   - Corner radius, line weights, shadow style uniform?
   - Margin discipline (0.5" minimum) honored on every slide?

5. ACCESSIBILITY
   - Body text passes 4.5:1 WCAG AA contrast?
   - Caption text legible (not gray-on-gray)?
   - Color is not the sole signal (e.g. green/red status backed by text or icon)?

Also check for these AI-generated tells:
- Decorative line under titles
- Generic stock-photo handshakes or businesspeople
- Cliché tech imagery (circuit boards, glowing brains)
- Three slides in a row with the same layout
- Centered body text
- Cartoon / clip-art style icons

For each slide, report:
- One-line summary
- Issues found (label each Critical / Moderate / Minor)
- If the slide passes, say "Pass" with one positive observation

The slide files are at:
[paste actual filenames from `ls slide-*.jpg`]

Expected purposes (from the outline):
1. <slide-1.jpg> — Title slide
2. <slide-2.jpg> — Agenda
3. ...
```

### Step 3 — Read the report and triage

Convert the subagent's findings into a triage table:

| Slide | Severity | Issue | Fix |
|---|---|---|---|
| 3 | Critical | Body text contrast 3.2:1 (gray on cream) | Change body color from `#9CA3AF` to `#374151` |
| 5 | Moderate | Two-column wraps text under chart | Move chart down 0.3" or shrink chart 5% |
| 12 | Minor | Footer page number off-baseline by 2pt | Lower footer text 2pt |

Address every Critical and Moderate. Minor issues — fix if cheap, defer if not.

### Step 4 — Fix and re-render

After fixes, re-render only the affected slides (don't regenerate the whole deck — slower and risks new issues):

```bash
pdftoppm -jpeg -r 150 -f 3 -l 3 "Deck.pdf" slide-fixed-3
pdftoppm -jpeg -r 150 -f 5 -l 5 "Deck.pdf" slide-fixed-5
```

Compare side-by-side to verify the fix landed without creating a new issue.

### Step 5 — One more pass

Run the visual subagent once more on the fixed slides. The first round of fixes commonly creates new issues (a moved chart now overlaps a footer; a font swap caused a wrap that now overflows). The second pass catches them. Two iterations is the practical floor; three is normal for high-stakes decks.

---

## 3. Content Integrity QA

The visual review covers visual issues. Content QA covers what the deck SAYS.

### Step 1 — Extract text and grep for placeholders

```bash
python -m markitdown "Deck.pptx" > deck-text.md

# Catch leftover placeholders
grep -iE "xxxx|lorem|ipsum|placeholder|tbd|todo|\\[customer\\]|\\[date\\]|\\[name\\]" deck-text.md

# Catch obvious LLM scaffolding
grep -iE "as an? (AI|advisor|consultant)|in this slide|the following bullet" deck-text.md
```

Any match is a Critical bug. Fix before delivery.

### Step 2 — Customer-specific facts audit

Read every slide and verify:

- [ ] Customer name spelled correctly and consistently (Thai + English variants, official spelling)
- [ ] Customer logo is real (not a placeholder shape) — and used with permission
- [ ] All financial figures cite the source (the user's brief, the customer's data, vendor docs)
- [ ] All dates are correct and in the right calendar (CE vs BE for Thai government)
- [ ] All quotes attributed to a real source; no fabricated testimonials
- [ ] All statistics from external sources cite the source (e.g. "Source: Bank of Thailand, 2025")
- [ ] All vendor product claims align with the vendor's official capability list
- [ ] All compliance claims (ISO 27001, PDPA, etc.) reflect what the firm actually has

If any of these is uncertain, mark the slide with `[NEED FROM USER: ...]` and stop. Do not deliver a deck with fabricated facts.

### Step 3 — Bilingual rendering audit (TH+EN decks only)

- [ ] Thai font glyphs render correctly (no `?` boxes, correct vowel/tone-mark stacking)
- [ ] English glyphs use the paired Latin font, not the Thai font's Latin fallback (which is usually ugly)
- [ ] Thai line breaks fall at word boundaries (Thai doesn't use spaces — verify visually)
- [ ] Currency, dates, and numbers are formatted consistently across slides
- [ ] No mixed numeral systems on the same slide (don't mix ๑๒๓ with 123)

### Step 4 — Theme integrity audit

- [ ] Primary color appears on every slide
- [ ] Accent color appears on no more than 2 elements per slide (it's the 10%, not the 60%)
- [ ] No off-theme colors (e.g. a screenshot pasted in with its own palette — should be cropped or recolored)
- [ ] Charts use the theme's chart palette (not the renderer's default)
- [ ] Footer / page number / divider lines all use the theme's muted color

### Step 5 — Source data integrity (when applicable)

- [ ] If the deck shows pipeline / forecast data, the underlying numbers reconcile to the source CSV
- [ ] If the deck shows ROI / TCO, the math checks (sum of line items = totals shown)
- [ ] If the deck cites benchmarks, the citation is real and current (not a 2018 stat used in a 2026 deck)

---

## 4. The QA Report

Every QA pass produces a markdown file alongside the deck:

```
samples/Deck_BangkokBank_V01R01_2026-04-26/
├── Deck_BangkokBank_V01R01_2026-04-26.pptx
├── outline_V01R01.md
├── qa_V01R01.md            ← THIS FILE
└── slide-images/
    ├── slide-01.jpg
    ├── slide-02.jpg
    └── ...
```

Template:

```markdown
# QA Report — V01R01 — Deck for Bangkok Bank — 2026-04-26

## Summary
- Slides: 18
- Critical issues: 0
- Moderate issues: 2 (both fixed in V01R02)
- Minor issues: 4 (3 fixed, 1 deferred)
- Iterations run: 2 (V01R01 → V01R02)

## 5-Dimensional Review

### First Impression
Pass — title slide reads "Proposal — Core Banking Modernization" in 2 seconds; theme matches Trust Navy.

### Usability
Pass — slide order follows Discovery → Solution → Business Case structure. Clear next steps on slide 17.

### Visual Hierarchy
Pass after fix — moderate issue on V01R01 slide 9 where stat callout was undersized; fixed by increasing to 72pt.

### Consistency
Pass — IBM Plex Sans Thai + Inter applied throughout; Lucide icons used consistently.

### Accessibility
Pass — all body text passes WCAG AA against the chosen background; checked with the contrast formula in 08-color-system.md.

## Content Integrity

- Customer name: "ธนาคารกรุงเทพ จำกัด (มหาชน) / Bangkok Bank PLC" — verified spelling and Thai/English forms
- Logo: real logo provided by user, placed per brand guidelines
- Financial figures: all sourced from user-provided RFP response brief
- Quotes: none used (intentional)
- Compliance claims: ISO 27001, PDPA — verified the firm is certified
- Bilingual rendering: verified Thai glyphs render correctly; line breaks audited slide by slide

## Open Issues
- Slide 13 (Team and Roles): photo of project manager not yet provided. Marked [NEED FROM USER]; placeholder shape in place.

## Theme Integrity
- Primary `#1E2761`, secondary `#CADCFC`, accent `#D97757` consistent across all slides
- Chart palette uses theme cycle
- Two screenshots on slide 11 cropped to remove off-theme red highlights

## Iteration Log
- V01R01 → V01R02: Fixed stat callout size on slide 9; tightened bilingual line breaks on slides 4 and 7.
```

The QA report is part of the deliverable. The user uses it to understand what was checked and what's still open.

---

## 5. When to Skip Visual QA Subagent

Visual QA via subagent is required for decks with **5 or more slides**. For shorter decks, do the visual QA yourself directly:

- 1–2 slides: visual QA inline (look at the rendered images, run through the 5 dimensions)
- 3–4 slides: visual QA inline + one peer prompt to a subagent if anything looks off
- 5+ slides: visual QA via subagent is mandatory

For high-stakes decks (TOR responses, board readouts, executive proposals), always use a subagent regardless of slide count. The cost is small; the cost of a missed issue is large.

---

## 6. Anti-Patterns the QA Pass Must Catch

These are the mistakes that consistently slip past the deck author and only get noticed in the customer meeting. The QA pass must specifically look for them:

- **AI-generated tells:** Decorative thin line under titles. Generic stock photography of handshakes. Cliché tech imagery. Centered body text. The same layout three slides in a row.
- **Lazy bilingual:** Word-for-word machine-translated headings. Thai numerals mixed with Western. Side-by-side body paragraphs that don't fit.
- **Theme drift:** A chart that uses the renderer's default palette instead of the deck theme. A screenshot with a UI accent color clashing with the theme.
- **Hidden bugs:** Footer text rendered in the same color as the background (invisible). Title that wraps under a hero image. A bilingual slide where one language is cut off the canvas.
- **Outdated facts:** A number from a previous customer or a previous version of the deck slipping into the new one.
- **Missing customer name:** The classic "I forgot to update slide 1" — the deck still says the previous customer's name.

A QA pass that doesn't find at least one issue on the first iteration was probably not run carefully enough. Look harder.

---

## 7. Self-Check Before Calling QA Done

- [ ] All slides converted to images and inspected
- [ ] Visual QA subagent dispatched for ≥5-slide decks
- [ ] Triage table produced with severity levels
- [ ] All Critical issues fixed
- [ ] All Moderate issues fixed
- [ ] At least one full re-render and re-QA cycle completed
- [ ] Markdown content extracted; placeholder grep returned no results
- [ ] Customer-specific facts audited (no fabrications)
- [ ] Bilingual rendering verified (if TH+EN deck)
- [ ] Theme integrity verified (60-30-10 honored)
- [ ] QA report written and saved alongside the .pptx

---

**End of 09-qa-framework.md.** When QA is complete, return to `SKILL.md` Section 7 (Output Contract) and prepare delivery to the user.
