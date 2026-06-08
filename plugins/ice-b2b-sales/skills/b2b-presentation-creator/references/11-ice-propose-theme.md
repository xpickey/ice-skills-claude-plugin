# 11. iCE Propose Theme — Reference Guide

> **Theme key:** `ice-propose`
> **Category:** Custom (iCE proprietary)
> **File:** `assets/themes/custom/ice-propose.json`
> **When to use:** iCE Consulting branded decks, methodology slides, solution architecture, project roadmaps, TOR-compliance documents, government and enterprise proposals where iCE is the issuer.

---

## 11.1 Brand DNA

iCE Consulting positions as **"Premium Enterprise Advisor with a Soft Edge"** — internationally credible, but not cold. The theme reflects this tension: cool palette for trust, glass/metallic 3D infographics for technical authority, generous whitespace for executive readability.

The theme places credibility first, decoration second. Visual elements help the data read faster — they do not compete with it.

---

## 11.2 Visual Mood Profile

| Dimension | Value | Avoid |
|-----------|-------|-------|
| Mood | Confident, Calm, Technical-Premium | Aggressive, Playful, Flat-Bold |
| Energy | Medium | High-saturation, Neon |
| Temperature | Cool (blue-cyan dominant) | Warm tones (use only for semantic warning) |
| Texture | Glass / Metallic / Soft Shadow | Matte flat, Heavy gradients |
| Whitespace | 35-45% of page | Cramped layout |

---

## 11.3 Color System

### Primary Palette (from iCE CI Guideline)

| Token | Hex | Role |
|-------|-----|------|
| iCE Blue (Main) | `#1E66A4` | Headlines, primary heading, iCE bar in Gantt |
| iCE Cyan (Secondary) | `#41A8B5` | Accent, top banner, Joint/Collaborative element |
| Pure White | `#FFFFFF` | Background, card surface |
| Dark Gray | `#595959` | Body text |

### Extended Tints & Shades

| Token | Hex | Use |
|-------|-----|-----|
| iCE Blue 95 | `#194F7A` | Hover, emphasis heading |
| iCE Blue 80 | `#2B7AC0` | Secondary heading, iCE Gantt bar |
| iCE Blue 50 | `#7AA8CC` | Soft card background |
| iCE Blue 30 | `#A8C7E0` | Borders, dividers |
| iCE Blue 10 | `#E5EEF5` | Light highlight background |
| iCE Cyan 50 | `#7BC9D2` | Chart tint, pyramid top |
| iCE Cyan 10 | `#DAEEF1` | Secondary background |
| Cool Gray Light | `#F4F6F8` | Section background |
| Mid Gray | `#9CA3AF` | Captions, Customer bar in Gantt |

### Semantic Colors (use sparingly)

| Status | Hex |
|--------|-----|
| Success | `#16A34A` |
| Warning | `#D97706` |
| Error | `#DC2626` |
| Info | `#41A8B5` (iCE Cyan) |

### Verified Color Pairings (from real iCE deliverables)

| Pair | Combination | Example |
|------|-------------|---------|
| Header Gradient | `#1E66A4` → `#41A8B5` | Top banner of roadmap slides |
| 3D Block Tri-tone | Top `#7BC9D2` + Mid `#41A8B5` + Base `#1E66A4` | Pyramid hierarchy, diamond milestones |
| Card on Light BG | White card + `#F4F6F8` BG + `#A8C7E0` border | Phase cards |
| Gantt Bar Coding | iCE `#1E66A4` / Customer `#9CA3AF` / Joint `#41A8B5` | RACI swimlane bars |
| Tech Diagram Frame | `#E5EEF5` panel + `#1E66A4` outline | Solution architecture panels |

---

## 11.4 Typography

### Font Stack (from iCE CI)

| Language | Headline | Body Heading | Body Paragraph |
|----------|----------|--------------|----------------|
| English | Raleway ExtraBold | Raleway | Open Sans Light |
| Thai | Kanit Bold | Kanit Light | Sarabun Regular |

### Type Scale

| Level | EN (pt) | TH (pt) | Color | Weight |
|-------|---------|---------|-------|--------|
| H1 Title | 36-44 | 32-40 | `#1E2937` | ExtraBold/Bold |
| H1 Sub (TH) | 22-26 | 22-26 | `#595959` | Regular |
| H2 Section | 22-26 | 20-24 | `#1E66A4` | Bold |
| H3 Item | 18-20 | 16-18 | `#1E2937` | Bold |
| Body | 12-14 | 12-14 | `#595959` | Regular |
| Caption | 9-10 | 9-10 | `#9CA3AF` | Regular |

### Bilingual Layering Rule

English is always the primary headline. Thai is always the secondary sub-headline — smaller, lighter color, never larger or bolder than English. This rule is non-negotiable for iCE-branded output.

```
[ENGLISH HEADLINE — Bold, Dark, Large]
[Thai sub-headline — Regular, Gray, Smaller]
```

---

## 11.5 Layout Patterns

iCE deliverables consistently use four layout patterns. Pick the one that matches the slide's job.

### Pattern A — Two-Column Split

Used for **principle + structure** slides, methodology, governance frameworks.

```
+--------------------------------+--------------------------------+
| Core Principles (45%)          | Visualization (55%)            |
| - 3D icon + bullet item 1      | [3D pyramid / diagram]         |
| - 3D icon + bullet item 2      | + tier labels right side       |
| - 3D icon + bullet item 3      |                                |
+--------------------------------+--------------------------------+
| Toolset gallery (4-5 cells, full width)                         |
+-----------------------------------------------------------------+
```

### Pattern B — Horizontal Tech Flow

Used for **Solution Architecture, Integration Diagram, Data Flow** slides.

```
+----------+    +----------+    +----------+    +----------+
| Source   | -> | Transport| -> | Dest.    | -> | Outputs  |
| Systems  |    | (VPN)    |    | Cloud    |    | (Reports)|
+----------+    +----------+    +----------+    +----------+
                                                ^
                                +----------+    |
                                | Identity |----+
                                | Provider |
                                +----------+
```

### Pattern C — Phase Grid (3×2)

Used for **Phase-based Roadmap, Process Stages, Method Steps**.

```
+----------+ +----------+ +----------+
| PHASE 1  | | PHASE 2  | | PHASE 3  |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
+----------+ +----------+ +----------+
+----------+ +----------+ +----------+
| PHASE 4  | | PHASE 5  | | PHASE 6  |
| ✓ Item   | | ✓ Item   | | ✓ Item   |
+----------+ +----------+ +----------+
```

- Card: White fill, 8px radius, `#A8C7E0` border, left accent bar `#41A8B5`
- Top banner: Solid `#41A8B5` with white title
- Bullets: Check icon in iCE Cyan, never plain dots

### Pattern D — Timeline + Swimlane (Gantt-style)

Used for **Master Schedule + Roles/Responsibilities + RACI** slides.

```
Milestones:   ◆ Charter   ◆ Design SO   ◆ SIT SO   ◆ Go-Live   ◆ Warranty End

Project Mgmt:  ████ iCE  ████████ Joint    ░░░░░░░░ Customer
Implementation:            ████ iCE  ░░░░░░░░ Customer  ████ Joint
Data Migration:            ████ iCE  ░░░░░░░░ Customer
Testing:                        ████ iCE  ████ Joint  ░░░░░░░░ Customer
Support & Training:                            ████ iCE  ████████ Joint

Timeline:     Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec
              Phase 1 | Phase 2 | Phase 3 | Phase 4 | Phase 5 | Phase 6
```

- iCE Consulting bar: `#1E66A4`
- Customer bar: `#9CA3AF`
- Joint bar: `#41A8B5`
- Milestone markers: 3D isometric diamond, `#1E66A4` to `#41A8B5` gradient by phase

---

## 11.6 Infographic Style

### 3D Icon System

| Attribute | Specification |
|-----------|---------------|
| Style | Isometric 3D, 15-25° tilt |
| Material | Glass + Metallic mix, soft reflection |
| Color range | Monochromatic blue-cyan (`#7AA8CC` to `#41A8B5`) |
| Highlight | Lighter tone, top-left light source |
| Shadow | Soft drop shadow, 15-25% opacity |
| Background | Often on a platform/base disc, same tone |
| Size consistency | Same size across an icon gallery — never mix big and small |

### 3D Pyramid / Tier Structure

For hierarchy (governance tiers, maturity levels, escalation paths):

```
Max 3 tiers — never more than 4.
Top:    Small cube, #41A8B5, glow effect on top
Middle: Mid slab, #7AA8CC, slightly transparent
Base:   Large slab, #1E66A4, foundation
Connect: Thin curve, #7AA8CC, to labels on the right
```

### Diamond Marker (Milestones)

```
Shape:     Isometric cube/diamond
Color:     Start #1E66A4 at first phase, fade to #41A8B5 at last
Size:      1.5-2× larger than regular icons
Position:  Floats above timeline or between phase brackets
Label:     Placed above (e.g., "Project Charter", "Go-Live")
```

### Card Styles

| Style | Spec | Use |
|-------|------|-----|
| Soft Card | White fill, 8px radius, `#A8C7E0` border 1px | Phase grid |
| Glass Panel | `#E5EEF5` fill, 12px radius, soft inner glow | Tech diagram panels |
| Toolset Tile | White top + colored bottom strip | Tool galleries |
| Legend Box | White fill, gray border, color chip per entry | Bottom of Gantt |

### Connector Lines

| Type | Spec | Use |
|------|------|-----|
| Solid arrow | 2px `#41A8B5` | Standard data flow |
| Glowing pipe | Gradient tube + animated arrow inside | Secure (VPN, MPLS) |
| Dotted line | 1.5px dashed `#A8C7E0` | Optional/conditional |
| Curve hint | Bezier curve, soft | Hierarchical (pyramid → label) |
| Bidirectional | Pair of arrows in tube | Two-way integration |

---

## 11.7 Composition Rules

### Grid & Spacing

| Element | Value |
|---------|-------|
| Page margin | 5-7% of width |
| Inter-section gap | 1.5× line-height |
| Card padding | 16-24px |
| Icon-to-text gap | 12-16px |
| Column gap | 24-32px |

### Reading Path (top to bottom)

1. Title block (EN bold → TH light)
2. Section headers (`#1E66A4`)
3. Focal visual (3D icon, diagram, chart)
4. Body content (`#595959`)
5. Caption/footnote (`#9CA3AF`)
6. Logo + page number (single corner, never both)

### Logo Placement

| Position | When |
|----------|------|
| Top-left | Cover slide, intro page |
| Top-right | Standard content slide |
| Bottom-left | Footer mode (page number bottom-right) |

One position per slide. Never duplicate.

---

## 11.8 Anti-Patterns (Never in iCE Decks)

| Forbidden | Why |
|-----------|-----|
| Colors outside palette in main content | Breaks brand recognition |
| Mixing flat icons with 3D icons | Inconsistent visual language |
| Heavy shadows or saturated gradients | Looks AI-generated stock |
| Thai title larger than English title | Wrong bilingual hierarchy |
| Plain black bullets | Use cyan check icon instead |
| Navy-full-page background in content | iCE uses white/light gray |
| Emojis in body content | Use 3D icon family |
| Fonts outside the stack | Breaks CI |
| Logo in both corners | Duplicate brand mark |
| Mixing big and small icons in gallery | Breaks rhythm |

---

## 11.9 Quick Layout Decision

| Slide job | Use pattern |
|-----------|-------------|
| Methodology + Governance | A (Two-Column) |
| Solution Architecture | B (Horizontal Tech Flow) |
| Phase-based Roadmap | C (3×2 Phase Grid) |
| Master Schedule + RACI | D (Timeline + Swimlane) |
| Comparison 2-3 items | A adapted, equal columns |
| Single concept + 3-5 items | A adapted |

---

## 11.10 Build Recipe

Each slide in iCE Propose theme follows this sequence:

1. Pick the layout pattern (A/B/C/D) based on slide job
2. Place bilingual title block at top (EN bold → TH light)
3. Set focal visual — one 3D element per slide
4. Apply type scale from §11.4
5. Use iCE Blue + iCE Cyan as the core — semantic colors only when needed
6. Run the Anti-Pattern check from §11.8
7. Place logo in single corner per §11.7
8. Add page number bottom-right, color `#9CA3AF`

---

## 11.11 Pairing with Vendor Themes

iCE Propose is cool-neutral by design — it pairs cleanly with vendor accents without clashing.

| Vendor Theme | How to combine |
|--------------|----------------|
| `oracle-accent` | Use iCE Propose as base, Oracle red as a 5-10% accent only |
| `netsuite-accent` | Use iCE Propose as base, NetSuite color in section dividers |
| `sap-accent` | Use iCE Propose as base, SAP blue as chart highlight |
| `microsoft-accent` | Use iCE Propose as base, MS color in icon highlights |

When pairing, iCE Propose remains the dominant palette. Vendor color stays under 10% to keep iCE branding primary.

---

## 11.12 JSON Reference

See `assets/themes/custom/ice-propose.json` for the machine-readable theme. Build with:

```bash
python scripts/build_deck.py \
  --outline outline.json \
  --theme assets/themes/custom/ice-propose.json \
  --language bilingual \
  --output "Proposal_[Customer]_V01R01_[YYYY-MM-DD].pptx"
```

---

**Source:** Distilled from 6 real iCE Consulting deliverables (Implementation Methodology, Solution Architecture, Project Roadmap, Master Schedule, TOR Compliance × 2) and the iCE Corporate Identity Guideline.

**Version:** V01R01 — 2026.05.15
