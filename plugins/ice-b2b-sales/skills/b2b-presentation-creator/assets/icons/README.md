# Icon Library — B2B Presentation Creator

## Overview

This icon library provides 12 essential SVG icons for B2B presentation decks. All icons follow the **Lucide design system** — a clean, minimal stroke-based icon set licensed under MIT.

- **Source:** https://lucide.dev (open source, MIT license)
- **Licensing:** MIT — free to use, modify, and distribute with attribution
- **Attribution:** Icons adapted from Lucide Icons (https://lucide.dev) under MIT License

---

## Icon Sizing Convention

All icons in this library follow these standards:

| Property | Value |
|----------|-------|
| **ViewBox** | `0 0 24 24` |
| **Stroke Width** | `1.5pt` |
| **Stroke Color** | `currentColor` (inherits from CSS/theme) |
| **Line Caps** | `round` |
| **Line Joins** | `round` |
| **Fill** | `none` (stroke only) |

### Why currentColor?

Using `currentColor` for stroke allows the presentation theme system to recolor icons at runtime without modifying SVG source files:

```css
/* Example: recolor all icons to brand blue in dark mode */
.dark-theme .icon {
  color: #0066ff;
}
```

This makes icons **themeable** across light, dark, and custom brand palettes.

---

## 12 Essential Icons

| # | Icon | Filename | Use Case | Semantic Meaning |
|---|------|----------|----------|-----------------|
| 1 | Shield | `shield.svg` | Security / Compliance | Trust, protection, standards |
| 2 | Trending Up | `trending-up.svg` | Growth / ROI / Results | Positive momentum, improvement |
| 3 | Users | `users.svg` | Team / People / Adoption | Collaboration, scale, team size |
| 4 | Target | `target.svg` | Goals / Objectives / Focus | Strategy alignment, precision |
| 5 | Clock | `clock.svg` | Time / Timeline / Urgency | Deadlines, implementation phases |
| 6 | Check Circle | `check-circle.svg` | Completion / Wins / Success | Delivery, achievement, done |
| 7 | Alert Triangle | `alert-triangle.svg` | Risks / Issues / Caution | Problems, risks, attention needed |
| 8 | Bar Chart | `bar-chart.svg` | Analytics / Metrics / Data | Measurement, performance, KPIs |
| 9 | Database | `database.svg` | Data / Storage / Backend | Infrastructure, persistence, scale |
| 10 | Cloud | `cloud.svg` | Cloud / SaaS / Integration | Modern infrastructure, accessibility |
| 11 | Handshake | `handshake.svg` | Partnership / Agreement / Mutual | Deal, collaboration, alignment |
| 12 | Lightbulb | `lightbulb.svg` | Ideas / Innovation / Features | Creativity, novelty, solution |

---

## Usage Examples

### In Presentation Markup

```html
<!-- Slide: "Where We Add Value" -->
<section class="slide">
  <div class="icon-row">
    <svg class="icon" data-src="assets/icons/shield.svg">
      <!-- Icon loaded here -->
    </svg>
    <h3>Enterprise Security</h3>
    <p>ISO 27001 and SOC 2 Type II certified...</p>
  </div>
  
  <div class="icon-row">
    <svg class="icon" data-src="assets/icons/trending-up.svg"></svg>
    <h3>Proven ROI</h3>
    <p>Average 3.2x ROI within 18 months...</p>
  </div>
</section>
```

### In CSS (Theming)

```css
/* Light theme: dark icons */
.light-theme .icon {
  color: #333333;
}

/* Dark theme: light icons */
.dark-theme .icon {
  color: #ffffff;
}

/* Brand color override */
.highlight .icon {
  color: #0066ff; /* Brand blue */
}

/* Sizes */
.icon-sm { width: 16px; height: 16px; }
.icon-md { width: 24px; height: 24px; }
.icon-lg { width: 32px; height: 32px; }
```

---

## How to Add More Icons

1. **Find icon at Lucide** → https://lucide.dev/icons/
2. **Copy SVG code** → Right-click icon > "Copy SVG"
3. **Save to file** → `assets/icons/[icon-name].svg`
4. **Verify format:**
   - ViewBox is `0 0 24 24`
   - Stroke uses `currentColor`
   - Stroke width is `1.5`
   - No fill attributes (stroke only)

**Example: Adding a "Dollar Sign" icon**

```bash
# Download from Lucide or copy SVG, then save:
cat > assets/icons/dollar-sign.svg << 'EOF'
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" 
     viewBox="0 0 24 24" fill="none" stroke="currentColor" 
     stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round">
  <line x1="12" y1="1" x2="12" y2="23"></line>
  <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path>
</svg>
EOF
```

Then update this README with the new icon in the table.

---

## Icon Design Principles

- **Minimal stroke:** No fills, no complex paths — 1.5pt stroke only
- **Clear at scale:** Visible at 16px (small) to 48px (large)
- **Single concept:** Each icon represents one idea
- **Consistent style:** All icons use the same weight and visual language
- **Accessible:** No reliance on color alone; shape conveys meaning

---

## License

All icons are derived from or compatible with **Lucide Icons**, licensed under MIT:

> MIT License
> 
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, and publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
> 
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.

**Attribution:** If you distribute presentations containing these icons, include:
> Icons from Lucide Icons (https://lucide.dev) — MIT License

---

## Questions?

Refer to the **B2B Presentation Creator** skill documentation for integration examples. For custom icons, extend this library by adding new SVG files and updating this README.
