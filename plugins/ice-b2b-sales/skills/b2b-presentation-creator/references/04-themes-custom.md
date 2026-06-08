# Reference 04 — Custom Themes

When the customer's brand color is highly specific or their industry does not fit the nine pre-built themes (02-themes-industry.md), build a custom theme from scratch. This reference defines the workflow: color extraction → palette derivation → typography pairing → visual motif → JSON output.

Custom themes are stored at `assets/themes/custom/<customer-name>.json` and treated as one-off builds until reused.

---

## When to Build Custom

Build a custom theme when **any** of these conditions apply:

1. **Strong brand identity** — The customer has a distinctive logo color (e.g., a tech startup's proprietary teal, a beverage brand's signature red) that doesn't match any of the nine industry themes.

2. **Regulated industry not on the list** — The customer operates in a regulated sector (pharma compliance, financial audit, critical infrastructure) whose constraints require a specific color palette to signal authority or security.

3. **Logo color doesn't fit available themes** — The customer's primary brand color is neither navy, teal, coral, magenta, olive, burgundy, slate, indigo, nor charcoal. For example, a high-end fashion brand using rose gold, or a health-tech company using a specific shade of mint.

4. **Vendor color palette** — The customer is a vendor of another company (e.g., a MSP selling to enterprises) and needs their partner's accent integrated without losing their own brand. Custom themes can accommodate a secondary brand layer (see `03-themes-vendor.md`).

5. **No suitable industry match** — The customer is in entertainment, luxury, fintech sub-sectors (crypto, trading), or emerging industries (deeptech, climate) where tone-of-voice requires bespoke visual identity.

**When NOT to build custom:** If the customer fits one of the nine industries even loosely, prefer the stock theme and let the `03-themes-vendor.md` overlay layer customer accents on top. Custom themes add build complexity; stock themes are battle-tested.

---

## Inputs Required Before Starting

Gather the following from the customer or their collateral before Step 1:

- **Logo file** (SVG preferred, PNG acceptable, high resolution)
  OR **Hex color code** of the brand primary (e.g., `#008080`)
  OR **Website screenshot** showing the customer's dominant color

- **Brand guideline document** (if available) — PDF, Figma, or web link containing color rules, typeface choices, usage restrictions

- **Customer name and industry** — Used in file naming and as a reference in the SKILL.md decoder

- **Intended deck audience** — Investors, employees, customers, regulators, or board — affects whether to skew the secondary color toward reassurance (trust) or energy (confidence)

- **Specific constraints** — Any required color avoidances (e.g., "must not use red due to cultural sensitivity," "accent must pass WCAG AA contrast")

---

## The 5-Step Custom Theme Workflow

### Step 1: Extract Base Color

Extract one dominant color from the customer's environment. This becomes the theme's `primary` token.

**Method A: Logo PNG / SVG**
- Open the logo in an image editor or use a color-picker tool (e.g., ColorPick Eyedropper for Chrome).
- Sample the most prominent brand color. If the logo uses multiple colors, pick the one that appears in ≥30% of the logo area.
- Convert to hex. Aim for a color that is **saturated and distinct** — avoid pale or desaturated variants at this stage.

**Method B: Hex Code Provided**
- Use the customer-provided hex directly.
- If the customer gives a range ("somewhere between navy and teal"), ask them to pin it down to a specific hex or show you the logo in context.

**Method C: Website Screenshot**
- If the customer lacks a formal logo but has a website, take a screenshot of the hero section.
- Use an eyedropper to sample the dominant accent color (e.g., a CTA button, banner background, or header bar).

**Example:** A Thai retail bank's website prominently displays navy `#002B5C` in its header and hero button. This becomes the theme's primary.

---

### Step 2: Derive Complementary Palette

From the primary, calculate the secondary, accent, and neutral colors using the 60-30-10 rule. Reference `08-color-system.md` for the full logic; this section provides the working rules.

**The 60-30-10 Rule (from 08-color-system.md):**
- **60%:** Primary color — dominant fills, title bars, large visual blocks
- **30%:** Secondary color — backgrounds, soft fills, support areas
- **10%:** Accent color — CTAs, key statistics, visual highlights

**Derivation Rules:**

| Step | Token | Formula | Why |
|---|---|---|---|
| 1 | `primary` | Customer brand hex | Anchors the palette |
| 2 | `secondary` | Tint primary by +70% lightness | Provides soft background; maintains brand feeling |
| 3 | `accent` | Hue rotation 180° from primary, mid-saturation | Optical contrast for CTAs and stats |
| 4 | `background` | Always `#FFFFFF` | Professional default; keeps text contrast high |
| 5 | `text` | `#141413` or `#1A1A1A` | Matches industry theme standard |
| 6 | `muted` | Hue match primary, -40% saturation, +20% lightness | Softer than text; for captions, footnotes |

**Worked Example 1: Navy Primary `#002B5C` (Thai Retail Bank)**

```
Primary:     #002B5C (dark navy)
Secondary:   Lighten by +70% lightness
             → Sample tint: #CADCFC (pale blue, matches Trust Navy secondary)
Accent:      Rotate hue 180° from navy (hue ~220°)
             → Hue ~40° (warm yellow-orange territory)
             → Select mid-saturation warm tone: #D97757 (warm coral)
             Rationale: Navy + coral is a classic financial pairing; warm accent
             signals human approval in a conservative setting.
Background:  #FFFFFF (standard)
Text:        #141413 (standard)
Muted:       Hue match navy, desaturate & lighten: #6E6B66
```

**Worked Example 2: Teal Primary `#008080` (Health-Tech Startup)**

```
Primary:     #008080 (bright clinical teal)
Secondary:   Lighten by +70% lightness
             → #C8E5E5 (soft seafoam)
Accent:      Rotate hue 180° from teal (hue ~180°)
             → Hue ~0° (warm orange-red territory)
             → Select warm accent: #FF8C6B (warm coral-orange)
             Rationale: Teal + warm coral signals healthcare (clinical + human care).
Background:  #FFFFFF
Text:        #102F33 (darker teal-influenced text for healthcare)
Muted:       #5C7174
```

**Quick Lightness Check:**
- If `primary` is darker than `#4A4A4A`, aim for secondary lightness ≥ 85%.
- If `primary` is lighter than `#CCCCCC`, aim for secondary lightness ≥ 95% (avoid washing out).

---

### Step 3: Pick Typography

Reuse the typography stack from the closest industry theme in `02-themes-industry.md`. Do not invent new font combinations.

**Selection Logic:**
- If the customer's primary color is a shade of navy/indigo → Use **Trust Navy** or **Civic Indigo** typography
- If teal/green → Use **Calm Teal** or **Scholar Olive** typography
- If warm (red/coral/orange) → Use **Vibrant Coral** or **Heritage Burgundy** typography
- If cool (slate/grey/purple) → Use **Future Slate** or **Steel Forge** typography
- If pink/magenta → Use **Signal Magenta** typography

**Example:** A custom theme built on navy `#002B5C` borrows **Trust Navy** typography:
```
EN headers: Inter Tight (or Inter)
EN body:    Lora
TH headers: IBM Plex Sans Thai
TH body:    Sarabun
```

**No custom fonts.** The build system assumes fonts are available in the PDF generation pipeline. Introducing a new font requires changes to the asset library (a separate workflow). Stick to the nine sets in `02-themes-industry.md`.

---

### Step 4: Visual Motif

Translate the customer's brand personality into slide design rules: corner radius, line weight, shadow style, decorative elements, and icon treatment.

**Motif Selection Questions:**
1. Is the customer's brand **geometric or organic?** (Straight lines / curves?)
2. Is the customer's brand **minimalist or ornate?** (Whitespace / detail?)
3. Does the customer's logo use **rounded or sharp corners?**
4. Is the customer's audience **conservative or contemporary?**

**Motif Templates (inherit from closest industry theme):**

| Template | Corner Radius | Line Weight | Shadow | Icon Style | Decorative Elements |
|---|---|---|---|---|---|
| Trust Navy (conservative) | 0° (90°) | 1pt thin | Minimal | Outlined | Top-of-slide rule in accent |
| Civic Indigo (authoritative) | 0° | 1pt thin | Subtle | Outlined | Gold underline headers |
| Steel Forge (industrial) | 2–4pt | 1.5–2pt | Subtle | Outlined + filled | Horizontal rules, blueprint lines |
| Calm Teal (human-centered) | 4pt | 1pt | Soft (blur 2px) | Outlined | Soft shadows, rounded photo frames |
| Vibrant Coral (energetic) | 4–6pt | 1.5pt | Soft | Filled & colorful | Color-blocked sections, hero imagery |
| Future Slate (contemporary) | 0–2pt | 1pt | Minimal | Outlined | Generous whitespace, gradient overlays on hero slides only |
| Signal Magenta (bold) | 2–4pt | 1.5pt | Subtle | Filled | Layered text & image, full-bleed photography |
| Scholar Olive (editorial) | 0–2pt | 1–1.5pt | Minimal | Outlined | Two-column layouts, ornamental dividers |
| Heritage Burgundy (premium) | 0pt | 0.5–1pt | Minimal | Outlined | Monograms, small caps, classical proportions |

**Example:** A custom theme on health-tech teal `#008080` inherits **Calm Teal** visual motif:
- 4pt corner radius (approachable, modern)
- 1pt line weight (clinical precision)
- Soft shadows (human trust, not harsh)
- Rounded icon frames (friendly)
- Soft-shadow photo frames (healthcare imagery supported)

---

### Step 5: Output to JSON

Generate a theme JSON file at `assets/themes/custom/<customer-name>.json`. The JSON schema mirrors the industry theme structure.

**Naming rule:** Use the customer name in lowercase, hyphens instead of spaces:
- "Thai Retail Bank" → `thai-retail-bank.json`
- "Health Tech Startup" → `health-tech-startup.json`

**Schema (from SKILL.md section 4):**

```json
{
  "id": "custom_thai_retail_bank",
  "name": "Thai Retail Bank Custom",
  "category": "custom",
  "description": "Custom theme built on navy #002B5C, derived secondary #CADCFC, warm coral accent #D97757. Typography from Trust Navy. Motif: financial precision with human warmth.",
  "colors": {
    "primary": "#002B5C",
    "secondary": "#CADCFC",
    "accent": "#D97757",
    "background": "#FFFFFF",
    "text": "#141413",
    "muted": "#6E6B66",
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444"
  },
  "typography": {
    "headings": {
      "en": "Inter Tight, sans-serif",
      "th": "IBM Plex Sans Thai, sans-serif"
    },
    "body": {
      "en": "Lora, serif",
      "th": "Sarabun, sans-serif"
    }
  },
  "motif": {
    "cornerRadius": {
      "button": "0px",
      "card": "0px",
      "input": "0px"
    },
    "lineWeight": {
      "thin": "1pt",
      "medium": "1.5pt",
      "bold": "2pt"
    },
    "shadows": {
      "enabled": false,
      "style": "none"
    },
    "decorativeElements": [
      "thin_top_rule",
      "accent_color_stats"
    ],
    "iconStyle": "outlined"
  },
  "usage": {
    "primary_percentage": 60,
    "secondary_percentage": 30,
    "accent_percentage": 10,
    "recommended_audience": "Enterprise financial services, retail banking, wealth management"
  }
}
```

---

## Color Theory Cheat Sheet

Quick reference for deriving secondary and accent colors without a full design tool.

**Secondary (30% color):**
- Take the primary hex.
- Increase lightness (L in HSL) by 60–80%.
- Keep hue and saturation the same.
- If the result is too pale, reduce lightness increase to 50–60%.

**Accent (10% color):**
- Take the primary hue.
- Rotate the hue by 180° (opposite on the color wheel).
- Use 60–80% saturation (mid-range; not neon, not muddy).
- Keep lightness around 45–55% (mid-tone; visible on both light and dark backgrounds).

**Quick Hex Conversion Example (Navy `#002B5C`):**

```
Primary:     RGB(0, 43, 92)
             HSL(220°, 100%, 18%) ← dark blue

Secondary:   HSL(220°, 100%, 80%) ← same hue/sat, +62% lightness
             Approximate RGB(204, 220, 252) → #CADCFC

Accent:      Rotate hue 220° + 180° = 40°
             HSL(40°, 70%, 50%) ← warm orange-coral
             Approximate RGB(217, 119, 87) → #D97757
```

**Standard Neutral (Muted):**
Use the industry-standard text and muted from the closest theme template above. If you must derive it:
- Hue match the primary.
- Reduce saturation by 40–50%.
- Increase lightness by 20–30%.
- Result: a tone that feels related to primary but readable as a secondary text color.

---

## Logo Handling

When the customer logo appears in the deck, follow these rules:

**Placement:**
- **Title slide (slide 1):** Logo top-left corner, minimum 12mm (0.47") on the short edge
- **Content slides (2+):** Logo bottom-right corner, minimum 10mm on the short edge
- **Never center the logo** — it competes with content hierarchy

**Sizing:**
- Logo shall occupy **≤ 1/8 of the slide area** (e.g., 1" x 1" on a 10" wide slide)
- If the logo is text-based (no symbol), use 18–24pt font size equivalent
- If the logo is a symbol only, constrain the symbol to 0.75"–1" on the short edge

**Clearspace:**
- Maintain at least 0.25" of whitespace around all four edges of the logo
- Do not place text or other elements within the clearspace
- If the customer logo has a preferred clearspace specification, honor it

**Color Usage:**
- Prefer full-color logo if provided
- If full-color is not available, use the primary color (not black, not white)
- Never invert the logo color (e.g., white logo on dark slide) without customer approval

**Accessibility:**
- Ensure the logo is not the *only* identifier on a slide (e.g., a title or slide number must also be present)
- If the slide is a full-bleed image with an embedded logo, add a transparent text layer with the company name for screen readers

---

## Approval Gate — Preview Before Committing

Before applying the custom theme to a 25-slide deck, render a **1-slide preview** and show the user the theme in context.

**Preview Slide Checklist:**
1. Title slide with customer logo, primary color in background, secondary color in accent bar
2. Headline in typography pair (EN and TH if applicable)
3. A sample stat block using the accent color
4. A sample call-to-action button
5. Footer with muted text and line rule (if the motif includes one)

**Approval Questions for the User:**
- "Does the primary color feel right for your brand?" (Show primary in a large block)
- "Is the secondary color appropriate as a soft background?" (Show secondary tint)
- "Does the accent color work as a highlight?" (Show accent in a CTA or stat)
- "Are the fonts readable and professional?" (Show a headline and paragraph in each language)
- "Does the overall visual motif match your brand personality?" (Show geometric vs. organic, minimal vs. ornate)

**Iteration Loop:**
If the user wants changes, the steps are:
1. Identify which token (primary / secondary / accent / typography / motif) needs adjustment
2. Make the change in the theme JSON
3. Re-render the 1-slide preview
4. Confirm again with the user

**Do NOT apply the theme to the full 25-slide deck until the user approves the preview.**

---

## Failure Modes — When Custom Theme Underperforms

**Symptom: The custom palette looks washed out or unreadable**
- Cause: Secondary color is too light (lightness >95%) or too close to white.
- Fix: Reduce secondary lightness to 80–85%. Re-render the preview.

**Symptom: The accent color is too weak or blends into the primary**
- Cause: Accent hue is too close to primary (hue difference <60°) or saturation is too low.
- Fix: Increase hue rotation to 150–210° from primary. Increase saturation to 60–80%. Re-test.

**Symptom: The theme looks generic or doesn't feel like the customer's brand**
- Cause: The primary color was sampled incorrectly or the visual motif doesn't match the brand personality.
- Fix: Re-sample the logo or website. If a different hue would be stronger, ask the customer to confirm the "official" brand hex.

**Symptom: The theme passes the preview but looks jarring at full-deck scale (25+ slides)**
- Cause: The accent color (10% rule) is too saturated or too bright when used across many slides; it creates visual fatigue.
- Fix: Reduce accent saturation by 10–20%. Use the accent sparingly — only on CTAs, key stats, and section dividers.

**When to Give Up and Revert:**
If after two iteration cycles the custom theme still underperforms:
- Revert to the closest industry theme from `02-themes-industry.md` (e.g., **Civic Indigo** or **Trust Navy**).
- Use `03-themes-vendor.md` to layer the customer's accent color on top as a secondary brand.
- Explain to the user: "The industry theme + vendor accent approach will give you a more polished look while honoring your brand color. This is a battle-tested combination."

Most customers accept this trade-off because the resulting deck is more professional than a struggling custom theme.

---

## Sample JSON Theme Output

Below is a complete, production-ready custom theme JSON for a fictional health-tech startup.

```json
{
  "id": "custom_health_tech_startup",
  "name": "HealthTech Startup — Custom Teal",
  "category": "custom",
  "description": "Custom theme for health-tech B2B SaaS. Primary teal #008080 derived from logo. Secondary soft seafoam #C8E5E5. Accent warm coral #FF8C6B. Motif: rounded, approachable, clinical. Typography from Calm Teal. Audience: healthcare providers, hospital IT, wellness platforms.",
  "colors": {
    "primary": "#008080",
    "secondary": "#C8E5E5",
    "accent": "#FF8C6B",
    "background": "#FFFFFF",
    "text": "#102F33",
    "muted": "#5C7174",
    "success": "#10B981",
    "warning": "#F59E0B",
    "error": "#EF4444"
  },
  "typography": {
    "headings": {
      "en": "Inter, sans-serif",
      "th": "IBM Plex Sans Thai, sans-serif",
      "weight": "bold",
      "size": "32–48px"
    },
    "subheadings": {
      "en": "Inter, sans-serif",
      "th": "IBM Plex Sans Thai, sans-serif",
      "weight": "semibold",
      "size": "20–28px"
    },
    "body": {
      "en": "Lora, serif",
      "th": "Sarabun, sans-serif",
      "weight": "regular",
      "size": "14–16px",
      "lineHeight": "1.6"
    },
    "caption": {
      "weight": "regular",
      "size": "12px",
      "color": "$muted"
    }
  },
  "motif": {
    "cornerRadius": {
      "button": "4px",
      "card": "4px",
      "input": "4px",
      "image": "4px"
    },
    "lineWeight": {
      "thin": "0.5pt",
      "medium": "1pt",
      "bold": "1.5pt"
    },
    "shadows": {
      "enabled": true,
      "style": "soft",
      "blur": "2px",
      "offset": "0 2px",
      "color": "rgba(0, 0, 0, 0.1)"
    },
    "decorativeElements": [
      "soft_shadows_on_photo_frames",
      "rounded_icon_containers",
      "accent_color_in_stats_and_CTAs"
    ],
    "iconStyle": "outlined",
    "photo_style": "clinical + lifestyle mix (real people in healthcare settings preferred)"
  },
  "usage": {
    "primary_percentage": 60,
    "secondary_percentage": 30,
    "accent_percentage": 10,
    "recommended_audience": "Healthcare providers, hospital systems, health-tech platforms, wellness SaaS",
    "slide_count_tested": "20–30 slides",
    "build_date": "2026-04-26",
    "notes": "Teal primary signals clinical trust; warm coral accent humanizes healthcare messaging. Rounded motif appeals to healthcare professionals seeking modern, approachable vendors."
  }
}
```

---

**End of 04-themes-custom.md.** Continue to `05-typography.md` for detailed font loading, `08-color-system.md` for color-theory deep dive, or `03-themes-vendor.md` for layering customer accents on top of industry themes.
