---
name: pre-flight-deck
description: |
  Mandatory gate-keeper that runs BEFORE any presentation deck (.pptx) creation or major edit. Forces comprehensive reading of skill references, asset verification, layout planning, and user sign-off before allowing build. Use this skill EVERY TIME the user asks for a deck, slides, presentation, pitch, proposal, demo deck, business case, QBR, or any .pptx output — including phrasings like "make a presentation", "build a deck", "create slides", "ทำ slide", "สร้าง deck", "เตรียม presentation". This skill prevents "functional but not delightful" output by enforcing the B2B Deck Quality Charter checklist BEFORE execution. It pairs with b2b-presentation-creator (which then does the actual build) and the project's B2B_DECK_QUALITY_CHARTER.md (which lists mandatory visual elements). Run this skill BEFORE invoking b2b-presentation-creator. Triggers especially on multi-slide decks (5+ slides), executive audiences (CEO/CFO/Board), and when the user's prior chat produced a deck that needed re-design.
---

# pre-flight-deck — Mandatory Pre-Build Gate-Keeper

> **Purpose:** Before any deck is built or significantly edited, this skill forces a structured pre-flight check. It is a gate, not a builder. The actual build is delegated to `b2b-presentation-creator` AFTER this skill completes.

---

## Why This Skill Exists

Deck creation tends to fail on the visual side — content is correct but design is monotonous. Root causes:

1. The model reads SKILL.md but skips the references/ folder
2. The model defaults to "Method 1 / native shapes" without considering Methods 2–4
3. The model uses one layout pattern repeatedly across the deck
4. The model uses placeholder data instead of realistic illustrative examples
5. The model skips icon library, color semantics, and big-number callouts

This skill exists to prevent all five failures by forcing the model to declare its plan BEFORE building.

---

## When to Use This Skill

Run this skill EVERY TIME a presentation deck is in scope. Specifically:

- New deck creation (any size)
- Major redesign of existing deck
- Adding 3+ new slides to existing deck
- Converting a markdown / Word document into slides
- Building a deck for executive audience (CEO / CFO / Board)
- After a previous chat produced an unsatisfactory deck

Do NOT skip this skill even if the request seems simple. The cost of running pre-flight is low; the cost of producing an underwhelming deck is high (rework, lost trust).

---

## The Five-Step Pre-Flight

Execute these five steps IN ORDER. Do not start the build until all five complete.

### Step 1 — List All References

For the skill that will build the deck (typically `b2b-presentation-creator`), enumerate ALL reference files. The b2b-presentation-creator skill points to:

```
references/01-deck-types.md
references/02-themes-industry.md
references/03-themes-vendor.md
references/04-themes-custom.md
references/05-typography.md
references/06-layouts.md       ← critical
references/07-infographics.md  ← critical
references/08-color-system.md  ← critical
references/09-qa-framework.md
references/10-bilingual-handling.md
```

State explicitly: "I will read X reference files before building."

### Step 2 — Read Each Reference and Confirm Understanding

Read each reference (no skipping). After each, write a one-line summary of what you learned. After all are read, declare understanding aloud:

- "I understand X layout patterns and will use Y, Z in this deck."
- "I understand the four infographic methods and will mix Methods 1, 2, and 4."
- "I understand color semantics: Green = routine, Red = alert, Gray = neutral, Navy = primary, Accent = highlight."
- "I understand the typography pair I will use: header X / body Y."

If any reference cannot be read (file missing, no permission), STOP and ask the user.

### Step 3 — Confirm Asset Availability

Verify or request the following:

- [ ] **Customer logo**: file path? If not provided, ask the user. If user has no logo, document the gap.
- [ ] **Consultant / firm logo**: file path? Same.
- [ ] **Icon library**: is Lucide (or equivalent) available locally at `/Users/xpickey/Documents/Claude/Assets/icons/lucide/`? If not, propose to download once.
- [ ] **Theme JSON**: industry × vendor × custom theme defined?
- [ ] **Realistic example data**: is there source material (numbers, IDs, scenarios) to draw from? If only placeholders are available, propose 2–3 plausible illustrative examples to user for sign-off.
- [ ] **Source content**: where is the content the deck will represent? Read it before outlining.

If any mandatory asset is missing, STOP and ask the user.

### Step 4 — Define Visual Quality Criteria for THIS Deck

For each slide planned, write a one-line declaration:

```
Slide N — [Title]
  Layout: [4-card grid / 2-col DRIVES / 5-tile process / T-account / hero number / quote / capability+icon row / matrix / timeline / etc.]
  Visual method: [Method 1 native shapes / Method 2 SVG / Method 3 AI / Method 4 icons / hybrid]
  Color semantics: [navy primary / green-red-gray for states / accent for highlights]
  Hero numbers: [yes — "40% less rework" / no]
  Brand chrome: [logo top corners / version footer]
```

This declaration enforces layout variation. If the same layout appears more than three times consecutively, revise the plan.

### Step 5 — Get User Sign-Off Before Build

Present:

- The slide-by-slide visual plan (from Step 4)
- The list of references read (from Step 2)
- The asset availability status (from Step 3)
- Open questions / decisions needed from the user

Wait for user confirmation. Do not proceed to `b2b-presentation-creator` until the user signs off.

---

## Block Condition

If any of the following are true, BLOCK the build:

- Step 1 not done (references not enumerated)
- Step 2 not done (references not read or understanding not declared)
- Step 3 has missing critical assets without user acknowledgment
- Step 4 shows the same layout used more than 3 times consecutively
- Step 5 has not received explicit user sign-off

Blocking is not failure — it is the skill working as designed. The downstream cost of skipping pre-flight is much higher than the upfront time cost.

---

## Handover to Builder Skill

Once all five steps pass and the user signs off, hand over to `b2b-presentation-creator` (or the appropriate builder skill) with the visual plan attached. The builder follows the plan; pre-flight does not generate slides itself.

---

## Output Contract

This skill does not produce a .pptx file. It produces:

1. A markdown document: `pre-flight-report-[deck-name]-[date].md` saved to the project's working folder
2. The visual plan (one entry per slide)
3. The list of asset gaps and user decisions needed
4. A "ready to build" or "blocked — reason X" status

Hand the report to the user and (if ready) to the builder skill.

---

## Anti-Patterns

Do NOT:

- Skip Step 2 because "I already read the SKILL.md" — that's not enough
- Default Method 1 (native shapes) for every slide just because it's editable — variety matters
- Allow the user to skip sign-off "to save time" — that converts pre-flight into theater
- Reuse the layout from the previous deck without re-evaluating fit
- Substitute icons with plain rectangles "to save asset acquisition time" — no
- Use placeholder text like "XXX" or "TBD" — propose real illustrative data to the user instead

---

## Composition

This skill chains with:

- **B2B_DECK_QUALITY_CHARTER.md** — read this charter as part of Step 2
- **b2b-presentation-creator** — the actual builder, invoked AFTER this skill completes
- **theme-factory** — for theme JSON if custom theme is needed
- **brand-guidelines** — for customer brand colors if available

---

**End of pre-flight-deck SKILL.md.** This skill is intentionally short — its job is to gate, not to teach.
