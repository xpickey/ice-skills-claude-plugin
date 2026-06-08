# Theme: iCE Zen Sales Pipeline — Clear, Strategic, Insight-Driven

## Concept

A presentation and dashboard theme blending **Japanese minimalist visual clarity** with
**CRM pipeline insight principles**. Emphasizes simplicity, data focus, and role-specific
communication. Use this theme as an alternative to "iCE Midnight Executive" when the audience
or brand calls for a calmer, more elegant aesthetic.

---

## When to Use This Theme

| Use Case | Recommended Theme |
|---|---|
| Internal executive reporting, board decks, dark-mode | iCE Midnight Executive |
| Client-facing proposals, clean brand environments, Japanese/APAC clients | **iCE Zen Sales Pipeline** ← this file |
| Both needed | Generate two versions; Zen for external, Midnight for internal |

---

## 1. Color Palette — "iCE Zen"

| Role | Name | Hex | Usage |
|---|---|---|---|
| Background | Pure White | `#FFFFFF` | All slide backgrounds |
| Surface | Warm Off-White | `#F7F6F3` | Card backgrounds, alternating rows |
| Primary Text | Ink | `#1C1C1E` | Headlines, body |
| Secondary Text | Stone | `#6B7280` | Labels, captions, metadata |
| Accent — Primary | Indigo | `#4F46E5` | Key KPIs, active highlights, CTA |
| Accent — Secondary | Teal | `#0D9488` | Recurring revenue, secondary metrics |
| WIN | Moss Green | `#15803D` | WIN category |
| FOCUS | Amber | `#D97706` | FOCUS category |
| ACTIVE | Slate Blue | `#3B82F6` | ACTIVE category |
| EARLY | Warm Gray | `#9CA3AF` | EARLY category |
| Risk/Alert | Soft Red | `#DC2626` | Warnings, risk cards |
| NetNew | Indigo | `#4F46E5` | NetNew revenue |
| Border | Light Gray | `#E5E7EB` | Card borders, dividers, table lines |

**Rule:** Maximum 2 accent colors visible per slide. Let white space and typography do the work.

---

## 2. Typography — iCE Zen

| Element | Font | Size | Weight | Notes |
|---|---|---|---|---|
| Report title | Georgia or Cambria | 36–40pt | Bold | Elegant serif for gravitas |
| Slide title | Calibri | 24–28pt | Regular | Clean, not heavy |
| Section label | Calibri | 11pt | Bold | Uppercase, wide letter-spacing |
| KPI hero number | Calibri Light or Trebuchet | 36–44pt | Light/Regular | Let the number breathe |
| Body / table | Calibri | 10–11pt | Regular | |
| Caption / footnote | Calibri | 8–9pt | Regular | Stone color |

**Rule:** Never use more than 2 font weights on a single slide.

---

## 3. Layout Principles

### Generous White Space
- Minimum 0.6" margins on all sides
- 0.3"–0.4" gap between every content block
- Never fill more than 65% of a slide with content

### One Major Insight Per Slide
- Each slide communicates ONE clear takeaway
- State it explicitly in a subtitle or insight caption below the title

### Visual Hierarchy — iCE Zen Grid
```
┌─────────────────────────────────────────────────────────┐
│  [Section label — uppercase 11pt stone]                 │  ← 0.4" top
│                                                         │
│  Slide Title — Calibri 26pt                             │
│  One-line insight caption — 11pt stone italic           │
│                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Content   │  │   Content   │  │   Content   │     │  ← Main area
│  │   Block 1   │  │   Block 2   │  │   Block 3   │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│                                                         │
│  ─────────────────────────────────────────────────      │  ← Thin divider line
│  Footnote / data source — 8pt stone                     │  ← 0.3" bottom
└─────────────────────────────────────────────────────────┘
```

---

## 4. Component Specifications — iCE Zen

### KPI Card (Zen Style)
```
┌──────────────────────────────────┐
│                                  │
│   ฿XX.XM                         │  ← 40pt light/regular, Indigo
│   Total NetNew Pipeline          │  ← 10pt stone
│                                  │
│   ↑ +12% vs last quarter         │  ← 9pt, moss green (positive) or red (negative)
│                                  │
└──────────────────────────────────┘
```
- No colored left border (unlike iCE Midnight Executive)
- Subtle bottom border only: 1px `#E5E7EB`
- Background: `#F7F6F3`
- Corner radius: 6px

### Table (Zen Style)
```
┌────────────────────────────────────────────┐
│ COMPANY        OPPORTUNITY    TOTAL         │  ← No background; bold uppercase, stone color, small letter-spacing
├────────────────────────────────────────────┤  ← 1px indigo divider under header
│ Company A      Project X      ฿12.5M        │  ← White row
│ Company B      Project Y      ฿ 8.2M        │  ← `#F7F6F3` alternate row
└────────────────────────────────────────────┘
```
- No heavy slate header bar — use a thin indigo line separator instead
- Amount values: right-aligned, bold, ink color (not color-coded unless critical)

### Stage Funnel (Zen Style)
- Horizontal flow: WIN → FOCUS → ACTIVE → EARLY (right to left = future to present)
- Each stage: a rounded pill shape with amount below
- Connector: thin gray arrow between stages
- Color: light tint of category color as pill background; category color as text

### Insight Caption Bar (Zen Style)
```
  ─────────────────────────────────────────────────────
  💡  XX% of pipeline value sits in EARLY stage — acceleration needed for Q3 target.
  ─────────────────────────────────────────────────────
```
- No background fill — just a thin top border line
- Font: Calibri 10pt italic, stone color
- Position: bottom of content area

---

## 5. Slide Structure — iCE Zen Theme

Apply this structure in place of the iCE Midnight Executive structure when this theme is selected:

| Slide | Zen Adaptation |
|---|---|
| 1 — Title | White background, large ink title, indigo accent line (top only), no dark bg |
| 2 — Exec Overview | 4 KPI cards in a clean row, no colored header bar, horizontal funnel below |
| 3–6 — Stage Detail | Minimal header with stage name + thin color underline; table without heavy header |
| 7 — NetNew Overview | Same clean layout; chart uses indigo/teal palette |
| 8 — NetNew Detail | Matrix with thin borders only; top deals in clean table |
| 9 — Risks & Actions | Two-column layout; risks in soft red cards, actions in soft green — no heavy card borders |
| 10–11 — BU / Recurring | Full-width matrix with zen table style |

---

## 6. Chart Colors — iCE Zen

### Stacked Bar (Quarterly)
```javascript
chartColors: ['#15803D', '#D97706', '#3B82F6', '#9CA3AF']  // WIN/FOCUS/ACTIVE/EARLY
```

### Doughnut / Pie
```javascript
chartColors: ['#4F46E5', '#0D9488', '#D97706']  // NetNew / Recurring / Other
```

### Line / Trend
```javascript
chartColors: ['#4F46E5']  // Single indigo line on white background
```

---

## 7. Role-Specific View Notes

When generating slides for specific audiences, adjust the information density:

| Audience | Focus | Density |
|---|---|---|
| Executive / Board | Total committed, WIN+FOCUS only, trend vs target | Low — 3 KPIs max per slide |
| Sales Manager | All 4 categories, team deal breakdown, bottleneck indicators | Medium |
| Sales Rep | Own deals only, next actions, days in stage | High — detail tables OK |

The iCE Zen theme is especially effective for **Executive and Board** audiences.

---

## 8. Theme Toggle in SKILL.md

When user specifies theme, apply the following override:

```
User says: "use zen theme" / "Japanese style" / "minimalist" / "clean white" / "client-facing"
→ Load this file (theme-zen.md) and override design-system.md
→ Replace color palette, card spec, table spec, and chart colors
→ Keep all data structure, slide sequence, and computation logic unchanged
```

Default (no theme specified): use **iCE Midnight Executive** (`design-system.md`)
