# Design System — "iCE Midnight Executive"

## Color Palette

| Role | Name | Hex | Usage |
|---|---|---|---|
| Background Dark | Navy | `#1A2332` | Title slide, section headers |
| Background Light | Off-white | `#F8F9FA` | Content slide backgrounds |
| Header/Accent | Slate | `#2C3E50` | Table headers, slide title bars |
| Primary Action | Orange | `#E8913A` | KPI numbers, accents, CTAs |
| WIN | Green | `#27AE60` | WIN category color |
| FOCUS | Orange | `#E8913A` | FOCUS category color |
| ACTIVE | Blue | `#3498DB` | ACTIVE category color |
| EARLY | Gray | `#7F8C9B` | EARLY category color |
| NetNew | Purple | `#8E44AD` | NetNew revenue labels |
| Recurring | Teal | `#1ABC9C` | Recurring revenue labels |
| Danger/Risk | Red | `#E74C3C` | Risk indicators |
| Text Light | White | `#FFFFFF` | Text on dark backgrounds |
| Text Dark | Charcoal | `#2C3E50` | Body text on light backgrounds |
| Text Muted | Gray | `#95A5A6` | Secondary labels, footnotes |

---

## Typography

| Element | Font | Size | Weight | Color |
|---|---|---|---|---|
| Slide title | Trebuchet MS | 28–36pt | Bold | White (dark bg) / Slate (light bg) |
| Section header | Trebuchet MS | 20–24pt | Bold | Category color or white |
| KPI hero number | Trebuchet MS | 32–40pt | Bold | Orange or category color |
| KPI label | Calibri | 10pt | Regular | Gray |
| Table header | Calibri | 10pt | Bold | White |
| Table body | Calibri | 9pt | Regular | Charcoal |
| Amount values | Calibri | 9–10pt | Bold | Color-coded by type |
| Insight text | Calibri | 10–11pt | Regular | Charcoal |
| Footer/caption | Calibri | 8pt | Regular | Gray #95A5A6 |

---

## KPI Card Specification

```
┌──────────────────────────────────────┐
│ ▌ [ICON] CATEGORY NAME               │  ← Colored left border (4px) + icon
│                                      │
│   ฿XX.XM                             │  ← Hero number (40pt bold, category color)
│   XXX Deals                          │  ← Deal count (10pt gray)
│                                      │
│   NetNew ฿XX.XM  │  Recurring ฿XX.XM │  ← Split (9pt, purple / teal)
└──────────────────────────────────────┘
```

- Background: White with subtle shadow
- Border left: 4px solid, category color
- Padding: 0.15" all sides
- Corner radius: 3px

---

## Table Specification

```
┌────────────────────────────────────────────────────────┐
│ COMPANY        │ OPPORTUNITY   │ STAGE  │ Q1 │ TOTAL   │  ← Slate #2C3E50 header, white text, 10pt bold
├────────────────────────────────────────────────────────┤
│ Company A      │ Project X     │ Won    │    │ ฿12.5M  │  ← White row
├────────────────────────────────────────────────────────┤
│ Company B      │ Project Y     │ A+     │    │ ฿8.2M   │  ← #F8F9FA alternate row
└────────────────────────────────────────────────────────┘
```

- Amount values: right-aligned, bold, colored (purple = NetNew, teal = Recurring)
- Row height: 0.25" minimum
- Column widths: Company 1.5", Opportunity 2.0", Stage 1.0", Quarter cols 0.7" each, Total 0.9"

---

## Slide Layout Grid

- Slide dimensions: 13.33" × 7.5" (widescreen 16:9)
- Top margin: 0.5" (for title bar)
- Content area: 0.4" from edges
- Title bar height: 0.5"
- KPI card row height: 1.3"
- Gap between elements: 0.15–0.25"

---

## Insight Bar Specification

```
┌──────────────────────────────────────────────────────────────────┐
│  🔑 Key insight text here — specific, actionable, data-backed    │
└──────────────────────────────────────────────────────────────────┘
```

- Background: very light category color (10% opacity) or #EAF2FB for blue
- Left border: 3px solid category color
- Font: Calibri 10pt, charcoal
- Height: 0.3"
- Position: bottom of content area, full width
