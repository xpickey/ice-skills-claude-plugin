# Linkage — How b2b-presentation-creator Composes with Other Skills

This document records the linkage between `b2b-presentation-creator` and the `ice-b2b-enterprise-sale` orchestrator skill, plus the broader composition pattern for use with other B2B skills.

**Version:** V01R01
**Date:** 2026-04-26

---

## 1. Linkage with `ice-b2b-enterprise-sale`

### Discovery mechanism

`ice-b2b-enterprise-sale` (the iCE orchestrator) discovers `b2b-presentation-creator` through the following chain:

```
1. iCE receives a B2B sales/presales/CS request
2. iCE checks the user's Custom Skill folder:
   /Users/xpickey/Documents/Claude/Custom Skill/SKILL_INDEX.md
3. SKILL_INDEX.md catalogs b2b-presentation-creator
4. When the request matches a deck-creation trigger,
   iCE references b2b-presentation-creator as the
   materialization step (Tier E in the iCE sub-skill index)
```

This is the supported, out-of-the-box pattern; no plugin modification required. It is documented in `ice-b2b-enterprise-sale/references/sub-skill-index.md` Section "Tier E — Custom Skill folder overlay".

### Roles in the chain

| Stage | Skill | Output |
|---|---|---|
| Strategic thinking | `b2b-strategic-thinking` (Tier A) | Why Change / Why Now / Why Us narrative |
| Sales mechanics | `b2b-solution-selling` (Tier A) | Pain sheet, MEDDPICC, business case math |
| Product depth | `oracle-cloud-applications-consulting` / `oracle-ebs-consulting` / `oracle-netsuite-consulting` (Tier B) | Product capability claims, fit-gap mapping |
| Domain compliance | `govt-egp-gfmis` / `advisor-govt-gfmis` / `fin-tech-consulting` (Tier C) | Regulatory citations, TOR clauses, IFRS9 logic |
| Relationship calibration | `b2b-relationship-management` (Tier A) | Stakeholder map, kreng jai/bunkhun/face overlay |
| **Deck materialization** | **`b2b-presentation-creator` (Tier E)** | **The .pptx artifact + outline + QA report** |

`b2b-presentation-creator` is always the **last** step in the chain. It does not strategize; it materializes.

### Handoff contract

When `ice-b2b-enterprise-sale` hands work to `b2b-presentation-creator`, the handoff package must include:

1. **Deck type** — one of: discovery / solution-demo / proposal / qbr / hybrid
2. **Sales stage** — one of the 10 lifecycle stages
3. **Customer context** — name (TH + EN if applicable), industry, audience
4. **Slide story** — slide-by-slide content as a markdown outline (matching the schema in `SKILL.md` Section 2 Step 4)
5. **Open issues** — anything still missing that the user must close (logos, financial figures, quotes)

`b2b-presentation-creator` then:

1. Asks the user for the theme (industry × vendor × custom) and language (TH / EN / Bilingual)
2. Validates the outline against the deck-type blueprint
3. Confirms the outline with the user (no .pptx generated until sign-off)
4. Builds the `.pptx`
5. Runs the 5-dimensional QA pass
6. Returns the deliverable bundle

---

## 2. Composition with other skills

`b2b-presentation-creator` composes naturally with several other skills in the user's library:

### `pptx`

**Relationship:** Engine dependency. `b2b-presentation-creator` uses the `pptx` skill's tooling guidance for low-level rendering, image conversion, and visual QA. Read `pptx` skill's SKILL.md before generating final files.

### `theme-factory`

**Relationship:** Pattern source. `b2b-presentation-creator` uses the same theme-selection pattern as `theme-factory` (showcase → user picks → apply). The two skills can be used together when the user wants a stock theme rather than an industry-specific one.

### `sales-pipeline-report`

**Relationship:** Upstream feeder. When the user wants a deck that shows pipeline analysis, run `sales-pipeline-report` first to compute the data, then hand the output to `b2b-presentation-creator` to wrap in an executive narrative deck.

### `brand-guidelines`

**Relationship:** Style overlay. When the customer is Anthropic itself or another brand with documented guidelines, layer the brand-guidelines skill on top of the chosen industry theme.

### `brand-voice:guideline-generation` / `brand-voice:enforce-voice`

**Relationship:** Voice overlay. When the user has brand voice guidelines saved at `.claude/brand-voice-guidelines.md`, `b2b-presentation-creator` applies them silently when writing slide copy.

### `canvas-design`

**Relationship:** Visual asset source. For hero slides or section dividers that need a custom visual, `canvas-design` can produce a PNG/PDF that `b2b-presentation-creator` then embeds.

### `legal-it-thailand-cloud`

**Relationship:** Compliance overlay. When the deck contains security/compliance claims (ISO 27001, PDPA, Cloud Security Standard 2567), pull citations from `legal-it-thailand-cloud` BEFORE writing those slides. Never invent compliance language.

### `phd-buddhist-public-admin` / `agj-academic-article` / `soc-sci-academic-article`

**Relationship:** Out-of-scope. These academic skills produce papers and dissertations; `b2b-presentation-creator` produces enterprise sales decks. They do not compose directly. If the user wants slides FROM an academic paper, use the slide blueprints in `01-deck-types.md` adapted to academic-conference format manually.

---

## 3. Invocation patterns

### Pattern A — Strategy-first, deck-second (preferred)

```
User: "ช่วยทำ deck เสนอ Oracle Fusion ให้ลูกค้า ABC Manufacturing"
↓
ice-b2b-enterprise-sale activates
↓
Tier-A chain (questioning → strategic-thinking → solution-selling) produces:
  - Why Change / Why Now / Why Us narrative
  - MEDDPICC score
  - Pain sheet (5 pain themes)
  - Business case (ROI / TCO / Risk)
  - Slide-by-slide outline
↓
ice-b2b-enterprise-sale hands the outline to b2b-presentation-creator
↓
b2b-presentation-creator asks:
  - Industry: Manufacturing → Steel Forge theme
  - Vendor: Oracle Fusion → Oracle red accent (10%)
  - Language: Bilingual TH+EN
  - Confirm outline
↓
Builds Solution_ABCManufacturing_V01R01_2026-04-26.pptx
↓
Runs 5-dim QA + visual subagent inspection
↓
Returns .pptx + outline.md + qa.md + open questions
```

### Pattern B — Direct invocation (when story is already known)

```
User: "I have an outline already, just turn it into a deck"
↓
b2b-presentation-creator activates standalone
↓
Validates outline schema, asks for theme + language
↓
Builds + QA + returns
```

### Pattern C — Government / TOR response

```
User: "ทำ TOR Response Deck สำหรับโครงการ XYZ ของกรม ABC"
↓
ice-b2b-enterprise-sale activates
↓
govt-egp-gfmis (Tier C) loads first — must verify TOR compliance
↓
b2b-solution-selling drafts the response narrative
↓
Outline produced with TOR-mandatory sections + paragraph-level compliance map
↓
b2b-presentation-creator activates with Civic Indigo theme + TH-only mode
↓
Builds with TH Sarabun PSK font (Thai government standard)
↓
QA includes a TOR compliance grid in the appendix
↓
Returns deliverable bundle
```

---

## 4. Quality contract across the chain

Regardless of which orchestrator invokes `b2b-presentation-creator`, the following are guaranteed:

- **No fabricated facts.** Customer names, financials, dates, quotes, logos, compliance claims must come from the chain's upstream skills or the user's brief. Missing items become open questions.
- **Outline confirmation gate.** No `.pptx` is generated until the user signs off on the outline.
- **Theme + language confirmation.** Both are explicitly confirmed before building.
- **Visual QA pass.** Mandatory for ≥5-slide decks via subagent.
- **Bilingual rendering verification.** When bilingual, line breaks, glyph stacking, and currency formatting are audited slide by slide.
- **Versioning.** Every deliverable carries `V##R##` in filename and footer.

---

## 5. Stronger linkage (optional, requires plugin write access)

If the user wants linkage at the plugin level (i.e. `ice-b2b-enterprise-sale`'s installed SKILL.md and sub-skill-index.md explicitly mention `b2b-presentation-creator`), the modifications are:

### Edit 1 — `ice-b2b-enterprise-sale/SKILL.md`

In Section 4.x (the role chain section), add a final step to each chain:

```
Step N+1: b2b-presentation-creator — materialize the deck
- When the artifact requested is a slide deck (.pptx)
- Hand the confirmed outline to b2b-presentation-creator
- The skill returns .pptx + outline + QA report
```

### Edit 2 — `ice-b2b-enterprise-sale/references/sub-skill-index.md`

Replace the "Tier E — Custom Skill folder overlay" section with the entry described in the user's `SKILL_INDEX.md`. The full text is in the `SKILL_INDEX.md` at `/Users/xpickey/Documents/Claude/Custom Skill/SKILL_INDEX.md`.

These edits require write access to the plugin's installation folder. Most Cowork users keep the plugin folder read-only and rely on the SKILL_INDEX.md discovery mechanism — which is already in place after this linkage step.

---

## 6. Verification

To verify the linkage is working:

1. Open a new conversation where `ice-b2b-enterprise-sale` is enabled
2. Ask: "ช่วยทำ deck เสนอ Solution Pitch สำหรับลูกค้า Manufacturing"
3. iCE should:
   - Run its standard Role × Stage × Product × Domain analysis
   - Reference `b2b-presentation-creator` for materialization
   - Hand off the outline
4. `b2b-presentation-creator` should activate, ask for theme/language, and proceed to build

If iCE does not reference `b2b-presentation-creator`, check that:

- `/Users/xpickey/Documents/Claude/Custom Skill/SKILL_INDEX.md` exists (created by this linkage step)
- The user's request matches one of the deck-creation triggers listed in this skill's SKILL.md
- The b2b-presentation-creator folder is at the path documented in SKILL_INDEX.md

---

**End of LINKAGE.md.**
