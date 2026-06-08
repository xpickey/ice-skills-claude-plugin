# Reference 08 — Color System & Accessibility

This reference defines the color discipline that makes every industry theme (02), vendor overlay (03), and custom variant (04) function cohesively. A theme is not just a palette — it is a system of roles, contrast rules, and cycling logic that ensures readability, professionalism, and visual hierarchy across 20+ slides.

---

## The 60-30-10 Rule

Every theme assigns visual weight through the 60-30-10 principle:

| Weight | Role | Example Usage |
|---|---|---|
| **60%** | Primary | Title bars, hero blocks, dominant chart series, key visual masses |
| **30%** | Secondary | Soft background tints, section dividers, supporting fills, secondary data |
| **10%** | Accent | CTA buttons, highlighted stats, single callout, urgent visual anchor |

**Visual manifestation on a real slide:**

- **Title bar:** Primary color (`#1E2761` in Trust Navy) fills the full width top.
- **Body background:** White canvas with subtle secondary tint fills (5–8% opacity) for soft section boxes.
- **Data highlight:** Accent color (`#D97757` in Trust Navy) labels a single key metric or points to one critical message.

Do not exceed 10% accent — multiple competing accent colors create chaos and reduce impact of each.

---

## Color Roles & One-to-One Mapping

Each color in a theme JSON has a single, specific role. Mixing roles is forbidden.

| Role | Token | Example Hex (Trust Navy) | Strict Usage |
|---|---|---|---|
| **Primary** | `primary` | `#1E2761` | Title bars, hero blocks, first/dominant chart series, key backgrounds (60% of slide) |
| **Secondary** | `secondary` | `#CADCFC` | Supporting fills, section backgrounds, soft dividers, secondary chart series (30%) |
| **Accent** | `accent` | `#D97757` | CTA buttons, highlighted KPI, one callout per slide, heatmap extremes (10%) |
| **Background** | `background` | `#FFFFFF` | Slide canvas — never overlaid with other colors without transparency |
| **Text** | `text` | `#141413` | All body copy, paragraph text, standard labels — must pass WCAG AA contrast on background |
| **Muted** | `muted` | `#6E6B66` | Captions, footnotes, secondary labels, legend text — lower contrast acceptable |

**Golden rule:** If a slide uses `primary` for the title, it must use `secondary` for supporting elements and `accent` for the single highlight. Never put `accent` on top of `primary` without contrast testing.

---

## Contrast & Accessibility

### WCAG AA Standards (Mandatory)

All readable text must pass the Web Content Accessibility Guidelines (WCAG) Level AA contrast ratio:

- **Body text & small text** (<18pt): **4.5:1 minimum**
- **Large text** (≥18pt, bold, or ≥14pt bold): **3:1 minimum**

### The Contrast Ratio Formula

Contrast Ratio = (L1 + 0.05) / (L2 + 0.05)

Where L is the relative luminance:
- L = 0.2126 × R + 0.7152 × G + 0.0722 × B
- R, G, B are sRGB values normalized to 0–1 (divide hex component by 255)

**Example:** White text (`#FFFFFF`) on Trust Navy primary (`#1E2761`)

- L(white) = 0.2126(1) + 0.7152(1) + 0.0722(1) = 1.0
- L(navy) = 0.2126(0.118) + 0.7152(0.149) + 0.0722(0.380) = 0.0605
- Ratio = (1.0 + 0.05) / (0.0605 + 0.05) = 1.05 / 0.1105 = **9.5:1** ✓ PASS

**Example:** Black text (`#141413`) on Trust Navy primary (`#1E2761`)

- L(black) ≈ 0.006
- Ratio ≈ 0.006 / 0.111 = **0.054:1** ✗ FAIL — unreadable

### Quick Contrast Lookup (Industry Primaries)

| Theme | Primary Hex | White Text | Black Text | Recommendation |
|---|---|---|---|---|
| Trust Navy | `#1E2761` | 9.5:1 ✓ | 0.05:1 ✗ | Use white text only |
| Civic Indigo | `#1A3D8F` | 8.8:1 ✓ | 0.06:1 ✗ | Use white text only |
| Steel Forge | `#36454F` | 8.2:1 ✓ | 0.08:1 ✗ | Use white text only |
| Calm Teal | `#028090` | 7.6:1 ✓ | 0.10:1 ✗ | Use white text only |
| Vibrant Coral | `#F96167` | 3.2:1 ✓ | 5.8:1 ✓ | Use black text (better) |
| Future Slate | `#0F172A` | 13.1:1 ✓ | 0.04:1 ✗ | Use white text only |
| Signal Magenta | `#C026D3` | 4.1:1 ✓ | 3.8:1 ✓ | Use white text (lighter) |
| Scholar Olive | `#5C6E2E` | 5.9:1 ✓ | 1.2:1 ✗ | Use white text only |
| Heritage Burgundy | `#6D2E46` | 6.4:1 ✓ | 0.9:1 ✗ | Use white text only |

**Practical test command (macOS / Linux):**

```bash
# Use an online WCAG contrast checker (WebAIM, TPGi) or this Node script:
# Save as contrast.js
const luminance = (hex) => {
  const rgb = parseInt(hex.slice(1), 16);
  const r = ((rgb >> 16) & 0xff) / 255;
  const g = ((rgb >> 8) & 0xff) / 255;
  const b = (rgb & 0xff) / 255;
  const l = 0.2126*r + 0.7152*g + 0.0722*b;
  return l <= 0.03928 ? l/12.92 : Math.pow((l+0.055)/1.055, 2.4);
};
const contrast = (hex1, hex2) => {
  const l1 = luminance(hex1), l2 = luminance(hex2);
  const lighter = Math.max(l1, l2), darker = Math.min(l1, l2);
  return ((lighter + 0.05) / (darker + 0.05)).toFixed(2);
};
console.log(contrast("#FFFFFF", "#1E2761")); // 9.5:1
```

Always test text color on the actual background of a slide before publishing.

---

## Color Cycling (Chart Palettes)

When a chart requires more than three data series, derive a cycle from the theme:

| Cycle Position | Logic | Example (Trust Navy) |
|---|---|---|
| 1 | Primary | `#1E2761` |
| 2 | Primary darkened 20% | `#141B3F` |
| 3 | Secondary | `#CADCFC` |
| 4 | Secondary darkened 15% | `#A7C7EB` |
| 5 | Accent | `#D97757` |
| 6 | Muted (safe fallback) | `#6E6B66` |

**Derivation formula:**
- Darken primary: Reduce L by 0.2 in HSL, or subtract 20% from each RGB component.
- Darken secondary: Reduce L by 0.15 in HSL.
- Never cycle the same color twice; never place adjacent colors that differ by <2:1 in luminance (they blend).

**Example 6-color chart cycle per theme:**

**Trust Navy:**
1. `#1E2761` (primary)
2. `#141B3F` (primary dark)
3. `#CADCFC` (secondary)
4. `#A7C7EB` (secondary dark)
5. `#D97757` (accent)
6. `#6E6B66` (muted)

**Vibrant Coral:**
1. `#F96167` (primary)
2. `#DC4F56` (primary dark)
3. `#F9E795` (secondary)
4. `#E8D67F` (secondary dark)
5. `#2F3C7E` (accent)
6. `#5C5C5C` (muted)

---

## Forbidden Color Combinations

Do not use these combinations — each violates accessibility, perceptual clarity, or professionalism:

| Combination | Why Forbidden |
|---|---|
| Red + Green side-by-side in a chart | 8% of males have red-green color blindness; the colors become indistinguishable to them |
| Pure black `#000000` + Pure white `#FFFFFF` | Extreme contrast causes eye strain; use `#141413` + `#FAF9F5` instead |
| Saturated yellow on white (`#FFFF00` on `#FFFFFF`) | Luminance difference is <2:1; unreadable |
| >4 saturated colors on a single slide | Overwhelms the viewer; dilutes any single message |
| Gradient background behind body text | Text becomes illegible; gradients create uneven contrast zones |
| Both primary and secondary at full saturation touching each other | Vibrational artifact (especially blues + oranges); reduce one to a tint |
| Accent color used for multiple elements | Defeats visual hierarchy; only one thing per slide should call for attention |
| Light text (`#FAF9F5`) on secondary tint (`#CADCFC`) | Contrast ratio fails; secondary must stay in the background |

---

## Dark Mode Considerations

Not every industry theme supports dark mode. When a theme does, the role mapping inverts:

| Role (Light Mode) | Light Mode Hex (Trust Navy) | Dark Mode Hex | Mapping Rule |
|---|---|---|---|
| background | `#FFFFFF` | `#0A0A0A` or primary | Background and primary swap |
| primary | `#1E2761` | `#F8FAFC` or near-white | Becomes light text |
| text | `#141413` | `#FFFFFF` or light | Becomes white/light |
| secondary | `#CADCFC` | `#1E2761` or dark primary | Becomes dark supporting fill |
| accent | `#D97757` | `#FF9B8F` or lighter accent | Stays warm, reduced saturation slightly |
| muted | `#6E6B66` | `#A0A0A0` or lighter grey | Becomes lighter for visibility on dark |

**Dark-mode-compatible themes:** Future Slate, Signal Magenta
**Dark-mode incompatible:** Civic Indigo, Heritage Burgundy (gold accents + dark bg fail WCAG)

Do not force a theme into dark mode if it is not listed as compatible.

---

## Customer Brand Color Overrides

When a customer's brand primary color becomes the deck's primary, all derived colors must follow HSL math to maintain harmony:

**Worked example:** Customer primary is `#0066CC` (electric blue)

1. **Primary:** Use customer color as-is = `#0066CC`
2. **Secondary:** Tint by 70% (lighten to 80% L in HSL)
   - HSL: `H=210°, S=100%, L=40%` → lighten to L=80% → `#99CCFF`
3. **Accent:** Derive from complementary hue (rotate H by +180°) and reduce saturation
   - Complement of 210° = 30° (orange-gold)
   - HSL: `H=30°, S=100%, L=50%` → reduce saturation to 60% → `#FF9900` (warm gold)
4. **Muted:** Desaturate primary by 40%, lower L to 60%
   - HSL: `H=210°, S=30%, L=60%` → `#7FA6CC` (grey-blue)
5. **Text:** Black `#141413` on light secondary passes WCAG; test on the specific tint.

**HSL adjustment steps:**
- Tint (lighten): increase L by 20–30%
- Shade (darken): decrease L by 15–25%
- Desaturate: reduce S by 30–50%
- Derive complement: add 180° to H, wrap to 360°

Always test the derived secondary against white body text for contrast.

---

## Color in Tables & Charts

### Tables

- **Header row:** Solid primary color, white text (per contrast lookup table above)
- **Alternating rows:** 5% tint of primary (e.g., `#1E2761` at 5% opacity on white = `#F5F7FB`)
- **Borders:** Primary color, 1pt weight
- **Text:** Standard body text color (`#141413` in Trust Navy)

Never use multiple competing row colors; never use secondary or accent in table rows.

### Charts (Bar, Line, Scatter)

- **Series 1:** Primary
- **Series 2:** Secondary
- **Series 3+:** Follow the 6-color cycle (above)
- **Positive/Negative bars:** Accent for positive, muted for negative (not red/green)
- **Legend:** Muted text on white background

### Heatmaps

Use a single-hue gradient (light to dark of one color), never a rainbow:

**Example:** Teal heatmap (Calm Teal theme)
- Light: `#E8F1F2` (10% intensity)
- Medium: `#71C4CE` (50% intensity)
- Dark: `#028090` (100% intensity, primary)

---

## Print vs. Screen

### Screen (PowerPoint, PDF on monitor)

- RGB hex colors (`#RRGGBB`)
- Saturation can be high (100% is acceptable)
- No adjustments needed

### Print (RFP / TOR submissions, hard-copy PDF)

- Convert hex RGB to CMYK-friendly equivalents
- Reduce saturation by 10–15% (S: 85–90% instead of 100%)
- Black solid text: **C=0 M=0 Y=0 K=100** (pure black ink, not RGB black)
- Use PDF export with "Print Optimized" color profile

**Example CMYK conversion (Trust Navy `#1E2761`):**

| Format | Value |
|---|---|
| RGB (screen) | R=30, G=39, B=97 |
| HSL (screen) | H=233°, S=52%, L=25% |
| CMYK (print) | C=72, M=65, Y=0, K=65 |
| HSL (print, reduced S) | H=233°, S=45%, L=25% |

Most modern presentation software (PowerPoint, Keynote) handles this automatically with "Print" export profiles. Always preview the printed PDF against a color swatch.

---

## Quick Contrast Reference Table

Use this table to rapidly verify text color choices on any primary:

| Primary (Theme) | White Text Passes AA? | Black Text Passes AA? | Recommended Text |
|---|---|---|---|
| `#1E2761` (Trust Navy) | Yes (9.5:1) | No (0.05:1) | White (`#FFFFFF`) |
| `#1A3D8F` (Civic Indigo) | Yes (8.8:1) | No (0.06:1) | White (`#FFFFFF`) |
| `#36454F` (Steel Forge) | Yes (8.2:1) | No (0.08:1) | White (`#FFFFFF`) |
| `#028090` (Calm Teal) | Yes (7.6:1) | No (0.10:1) | White (`#FFFFFF`) |
| `#F96167` (Vibrant Coral) | Yes (3.2:1) | Yes (5.8:1) | Black (`#141413`) ← better |
| `#0F172A` (Future Slate) | Yes (13.1:1) | No (0.04:1) | White (`#FFFFFF`) |
| `#C026D3` (Signal Magenta) | Yes (4.1:1) | Yes (3.8:1) | White (`#FFFFFF`) ← lighter |
| `#5C6E2E` (Scholar Olive) | Yes (5.9:1) | No (1.2:1) | White (`#FFFFFF`) |
| `#6D2E46` (Heritage Burgundy) | Yes (6.4:1) | No (0.9:1) | White (`#FFFFFF`) |

If a primary is new (custom override), run the contrast formula above before approving any text color.

---

**End of 08-color-system.md.** See `02-themes-industry.md` for palette definitions, `03-themes-vendor.md` for accent overrides, and `05-typography.md` for font pairing with color roles.
