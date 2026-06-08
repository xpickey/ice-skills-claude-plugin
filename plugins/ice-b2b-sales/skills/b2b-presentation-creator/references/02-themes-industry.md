# Reference 02 — Industry Themes

This reference defines nine pre-built industry themes. The customer's industry sets the dominant color, typographic personality, and visual motif of the deck. This is the **base layer** of the theme stack (Industry → Vendor → Custom).

Each theme below has a corresponding JSON file at `assets/themes/industry/<theme-name>.json` that the build script consumes.

---

## How to Pick

Match the customer's industry to one of the nine. If the industry isn't listed, pick the closest neighbor and use the **Custom** workflow in `04-themes-custom.md` to fine-tune.

| Industry | Theme | When the customer is… |
|---|---|---|
| Banking, FinTech, Insurance | **Trust Navy** | A bank, securities firm, insurer, fintech, NPL/AMC operator |
| Government, SOE, Local Authority | **Civic Indigo** | A ministry, รัฐวิสาหกิจ, อบจ., เทศบาล, agency |
| Manufacturing, Industrial, Energy | **Steel Forge** | A factory, OEM, energy producer, refinery, utility |
| Healthcare, Pharma, Hospital | **Calm Teal** | A hospital, clinic, pharma, medical device, health insurer |
| Retail, Consumer, F&B | **Vibrant Coral** | A retailer, restaurant chain, FMCG, e-commerce |
| Tech, SaaS, Cloud | **Future Slate** | A tech company, SaaS, cloud-native, ISV |
| Telco, Media, Communications | **Signal Magenta** | A telco, broadcaster, media group, advertising platform |
| Education, Research, NGO | **Scholar Olive** | A university, school, foundation, research institute |
| Premium Services, Legal, Real Estate | **Heritage Burgundy** | A law firm, consultancy, premium real estate, private bank |

---

## 1. Trust Navy (Banking & FinTech)

**Personality:** Stable, precise, institutional. The colors of a bank's annual report combined with the typographic clarity of a modern financial brand.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#1E2761` | Dominant — title bars, key visual blocks (60%) |
| `secondary` | `#CADCFC` | Supporting — backgrounds, soft fills (30%) |
| `accent` | `#D97757` | Sparing — CTA, highlight stat (10%) |
| `background` | `#FFFFFF` | Slide background |
| `text` | `#141413` | Body text |
| `muted` | `#6E6B66` | Captions, footnotes |

**Typography:**
- EN headers: **Inter Tight** (or Inter)
- EN body: **Lora**
- TH headers: **IBM Plex Sans Thai**
- TH body: **Sarabun**

**Visual motif:** Sharp 90° corners, thin top-of-slide rule (1pt), no decorative gradients. Numerical stats use a contrasting accent color.

**Avoid:** Pastel pinks, bright greens, hand-drawn illustrations, casual icons.

---

## 2. Civic Indigo (Government & Public Sector)

**Personality:** Authoritative, restrained, accountable. Designed to read well in printed RFP responses and on government projection screens.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#1A3D8F` | Dominant (60%) |
| `secondary` | `#E5E8EE` | Supporting (30%) |
| `accent` | `#C8A951` | Sparing — gold accent for state symbolism (10%) |
| `background` | `#FFFFFF` | Background |
| `text` | `#1A1A1A` | Body |
| `muted` | `#5C5C5C` | Captions |

**Typography:**
- EN: **Source Sans 3** / **Source Serif 4**
- TH headers: **Sarabun** (or **TH Sarabun New** for legal documents)
- TH body: **Sarabun**

**Visual motif:** Classical proportions, generous margins, headers underlined in thin gold. Works well for TOR responses, e-bidding submissions, and ministerial briefings.

**Avoid:** Bright accents (e.g. coral, magenta), photographic backgrounds without authorization, casual typography.

**Special note for Thai government:** When the deck is a formal TOR response, use **TH Sarabun PSK / TH Sarabun New** instead of Sarabun on title slides — many government reviewers expect the official font.

---

## 3. Steel Forge (Manufacturing & Industrial)

**Personality:** Industrial confidence. Steel, blueprint, machinery aesthetic without becoming dystopian.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#36454F` | Dominant — charcoal grey (60%) |
| `secondary` | `#B0B7C0` | Supporting — steel grey (30%) |
| `accent` | `#FF6F3C` | Sparing — safety orange (10%) |
| `background` | `#F5F6F8` | Off-white background |
| `text` | `#1A1A1A` | Body |
| `muted` | `#5C5C5C` | Captions |

**Typography:**
- EN headers: **Manrope Bold** / **Inter Tight**
- EN body: **Inter**
- TH headers: **Prompt SemiBold** / **Anuphan SemiBold**
- TH body: **Sarabun**

**Visual motif:** Strong horizontal lines, sectioned blocks, occasional blueprint-line decoration (subtle). Numbers and OEE-style stats are dominant.

**Avoid:** Soft gradients, pastel anything, decorative serif fonts in body text.

---

## 4. Calm Teal (Healthcare & Pharma)

**Personality:** Clinical clarity, calm, trustworthy. Hospitals and pharma audiences read aggressive marketing as risky.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#028090` | Dominant — clinical teal (60%) |
| `secondary` | `#E8F1F2` | Supporting — soft sky (30%) |
| `accent` | `#F08C5E` | Sparing — warm coral for human moments (10%) |
| `background` | `#FFFFFF` | Background |
| `text` | `#102F33` | Body |
| `muted` | `#5C7174` | Captions |

**Typography:**
- EN: **Inter** / **Lora**
- TH: **IBM Plex Sans Thai** / **Sarabun**

**Visual motif:** Rounded corners (4pt radius), soft shadows allowed, human-centered photography in moderation. Avoid stock photos of doctors with stethoscopes.

**Avoid:** High-contrast red anywhere (signals emergency), bright yellow (unprofessional in this sector).

---

## 5. Vibrant Coral (Retail & Consumer)

**Personality:** Energetic, accessible, brand-confident. Retail decks compete with vendor marketing decks; this theme has more visual energy than the others.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#F96167` | Dominant — coral red (60%) |
| `secondary` | `#F9E795` | Supporting — soft gold (30%) |
| `accent` | `#2F3C7E` | Anchor — deep navy for credibility (10%) |
| `background` | `#FFFFFF` | Background |
| `text` | `#1A1A1A` | Body |
| `muted` | `#5C5C5C` | Captions |

**Typography:**
- EN headers: **Poppins ExtraBold**
- EN body: **Inter**
- TH headers: **Prompt Bold**
- TH body: **Sarabun**

**Visual motif:** Bold typography, large hero imagery, color-blocked sections. Numbers are the visual hook (e.g. "+18% basket size").

**Avoid:** Centered body text, cluttered slides — retail audiences expect breathing room.

---

## 6. Future Slate (Tech & SaaS)

**Personality:** Modern, technically credible, design-forward. Designed for audiences that have seen every SaaS pitch and notice when something looks "AI-generated."

| Token | Hex | Role |
|---|---|---|
| `primary` | `#0F172A` | Dominant — slate near-black (60%) |
| `secondary` | `#94A3B8` | Supporting — neutral slate (30%) |
| `accent` | `#22D3EE` | Sparing — electric cyan (10%) |
| `background` | `#FFFFFF` | Background (or `#0F172A` for dark mode) |
| `text` | `#0F172A` (light bg) / `#F8FAFC` (dark bg) | Body |
| `muted` | `#64748B` | Captions |

**Typography:**
- EN headers: **Inter Tight Bold** / **Manrope Bold**
- EN body: **Inter**
- EN code/data: **JetBrains Mono**
- TH headers: **IBM Plex Sans Thai SemiBold**
- TH body: **IBM Plex Sans Thai**

**Visual motif:** Generous whitespace, monospaced code blocks for any technical content, subtle gradient overlays only on hero slides. Dark-mode-friendly.

**Avoid:** Cliché tech imagery (circuit boards, glowing brains), Comic Sans (obviously), excessive gradients.

---

## 7. Signal Magenta (Telco & Media)

**Personality:** Bold, contemporary, signal-of-now. Media and telco audiences expect a higher visual production value than B2B average.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#C026D3` | Dominant — magenta (60%) |
| `secondary` | `#F5F3FF` | Supporting — soft violet (30%) |
| `accent` | `#FACC15` | Sparing — broadcast yellow (10%) |
| `background` | `#0F0F12` (dark) or `#FFFFFF` (light) | Background |
| `text` | `#F5F3FF` (dark bg) / `#1A1A1A` (light bg) | Body |
| `muted` | `#94A3B8` | Captions |

**Typography:**
- EN headers: **Bricolage Grotesque** / **Manrope Black**
- EN body: **Inter**
- TH headers: **Prompt Black** / **IBM Plex Sans Thai Bold**
- TH body: **IBM Plex Sans Thai**

**Visual motif:** Layered text and image, occasional photographic full-bleed slides, motion-friendly composition (this theme also exports cleanly to video).

**Avoid:** Conservative layouts, all-text slides, dated stock photography.

---

## 8. Scholar Olive (Education, Research, NGO)

**Personality:** Considered, evidence-led, mission-driven. Education and NGO audiences are sensitive to slick marketing and respond to substance.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#5C6E2E` | Dominant — olive (60%) |
| `secondary` | `#E8E6DC` | Supporting — parchment (30%) |
| `accent` | `#B85042` | Sparing — terracotta (10%) |
| `background` | `#FBFAF6` | Warm white background |
| `text` | `#1A1A1A` | Body |
| `muted` | `#5C5C5C` | Captions |

**Typography:**
- EN headers: **Cormorant Garamond Bold** / **Playfair Display**
- EN body: **Lora**
- TH headers: **Noto Serif Thai SemiBold**
- TH body: **Noto Serif Thai** or **Sarabun**

**Visual motif:** Editorial layouts, generous line-height, two-column text where appropriate. Charts use understated palettes.

**Avoid:** Aggressive sans-serifs, neon accents, high-energy hero imagery.

---

## 9. Heritage Burgundy (Premium Services, Legal, Real Estate)

**Personality:** Establishment, premium, considered. Audiences in this segment associate restraint with quality.

| Token | Hex | Role |
|---|---|---|
| `primary` | `#6D2E46` | Dominant — burgundy (60%) |
| `secondary` | `#ECE2D0` | Supporting — cream (30%) |
| `accent` | `#A26769` | Connector — dusty rose (10%) |
| `background` | `#FBFAF6` | Warm white |
| `text` | `#1A1A1A` | Body |
| `muted` | `#5C5C5C` | Captions |

**Typography:**
- EN headers: **Playfair Display Bold**
- EN body: **Lora**
- TH headers: **Noto Serif Thai SemiBold**
- TH body: **Noto Serif Thai**

**Visual motif:** Generous margins, classical proportions, monogram or initial-letter accents. Small typographic details (small caps, oldstyle figures) are appropriate.

**Avoid:** Casual typography, bright accents, infographics with cartoon-style icons.

---

## How the Industry Theme Affects the Build

When the build script reads the chosen theme JSON, the following are set automatically:

- All slide background colors, primary fills, text colors
- All font choices (per language mode in `05-typography.md`)
- The default chart palette (derived from primary + secondary)
- The icon set personality (rounded vs. sharp)
- Default corner radius, line weight, shadow style
- Header rule weight and accent line behavior

Anything the user later overrides at the deck level (e.g. a single hero slide using a vendor accent color) is layered on top — the industry theme is the base layer.

---

## Custom Industry — Build From Scratch

If none of the above fit, escalate to `04-themes-custom.md` and:

1. Pull 2 reference colors from the customer's environment (logo, website, signage)
2. Derive a primary / secondary / accent
3. Pair with the closest typography stack from this file
4. Save the result as a new theme at `assets/themes/industry/<custom-name>.json`
5. Treat it as a one-off until reused

---

**End of 02-themes-industry.md.** Continue to `03-themes-vendor.md` for vendor accents, `05-typography.md` for font detail, or `08-color-system.md` for the 60-30-10 rule.
