# Reference 05 — Typography System

This reference defines the font pairing strategy, sizing discipline, and language-specific typographic rules for B2B decks in Thai, English, or Bilingual (TH+EN).

**Critical principle:** A bilingual deck fails visually when the Thai font and Latin font have mismatched visual weight. This guide prevents that failure by enforcing paired font sets where glyph height and stroke weight are balanced across scripts.

---

## 1. Why Font Pairing Matters

When a Thai title (e.g., "ความสำเร็จด้านการขาย") sits next to its English equivalent ("Sales Achievement"), the Thai glyphs may appear heavier, lighter, or misaligned if the fonts are not chosen as a pair.

**Common failures:**
- IBM Plex Sans Thai paired with Calibri → Thai looks 20% heavier
- Sarabun paired with Arial → glyph height mismatch, especially on ascenders
- Using a single "universal" font (e.g., Tahoma) across both scripts → dated appearance, poor modern kerning

**The solution:** Each personality (Modern, Trust, Tech, Premium, Government) is assigned a canonical Thai font and a canonical English font *designed to pair together*.

---

## 2. The Five Canonical Font Pairs

| Personality | Thai Font | EN Font | Download | When to Use | When NOT to Use |
|---|---|---|---|---|---|
| **Modern Executive** | IBM Plex Sans Thai | Inter | [IBM Plex](https://www.ibm.com/plex/), [Inter](https://fonts.google.com/specimen/Inter) | Default for bilingual corporate, fintech, SaaS. Clean, balanced cap heights. | Avoid for government TOR, luxury, or heavily design-driven decks. |
| **Trust / Banking** | Sarabun | Lora | [Google Fonts](https://fonts.google.com/specimen/Sarabun), [Lora](https://fonts.google.com/specimen/Lora) | Financial services, insurance, official corporate. Serif/sans balance signals authority. | Not for tech, retail, media. |
| **Tech-Forward** | Prompt | Manrope | [Google Fonts](https://fonts.google.com/specimen/Prompt), [Manrope](https://fonts.google.com/specimen/Manrope) | SaaS, tech startups, cloud services, industrial. High x-height, contemporary. | Avoid premium or government contexts. |
| **Premium / Luxury** | Noto Serif Thai | Playfair Display | [Google Fonts](https://fonts.google.com/specimen/Noto+Serif+Thai), [Playfair Display](https://fonts.google.com/specimen/Playfair+Display) | Legal, real estate, luxury goods, heritage brands. Editorial elegance. | Not for tech-forward, high-energy retail. |
| **Government / Restrained** | TH Sarabun New (or Sarabun) | Source Sans 3 | [TH Sarabun New](https://github.com/Cadiak/ThaiFont), [Google Fonts](https://fonts.google.com/specimen/Source+Sans+3) | RFP/TOR responses, government briefings, formal submissions. Neutral, proven. | Avoid retail, media, premium luxury. |

---

## 3. Language Modes

### English Only
Pick **one** from the following. Order by preference:
1. **Inter** — most versatile, excellent at small sizes, corporate neutral
2. **Manrope** — heavier weight, tech-friendly
3. **Lora** — serif, formal/editorial
4. **Source Sans 3** — government/legal clarity
5. **Playfair Display** — headers only, heritage contexts
6. **JetBrains Mono** — code, data, technical content (monospace)

**Rule:** Do not mix serif and sans in body text on the same slide. Serif headers + sans body, or vice versa, is acceptable; sans + sans throughout is default.

### Thai Only
Pick **one** from the following:
1. **IBM Plex Sans Thai** — modern, clean, tech-friendly, excellent hinting
2. **Sarabun** — familiar to all Thai government and corporate audiences; widely installed
3. **Prompt** — contemporary, higher x-height, tech-forward
4. **Noto Serif Thai** — editorial, premium
5. **Anuphan** — geometric, design-forward (less common; check client installation)
6. **TH Sarabun New** — official Thai government alternative; required for some RFPs

**Rule:** Thai body text must never be smaller than 14pt without line-height compensation (see Section 5).

### Bilingual TH+EN
**Mandatory rule:** Always use a paired font set from Section 2, above. Never mix unpaired fonts.

When both scripts appear on the same slide:
- Use the canonical Thai font from the pair in Column 2
- Use the canonical EN font from the pair in Column 3
- Do not deviate to a "better" EN font unless the customer explicitly requests it (and be prepared to re-pair)

---

## 4. Sizing System (Slide-Relative)

This sizing system assumes a 1920×1080 pixel slide (16:9 aspect ratio). Adjust proportionally for 4:3 or ultrawide formats.

| Element | Size (EN) | Size (TH) | Weight | Notes |
|---|---|---|---|---|
| **Slide Title** | 36–44pt | 40–48pt | Bold | Main headline; all-caps or title-case. Thai +5pt due to descender/ascender ratio. |
| **Section Header** | 24–28pt | 28–32pt | Bold | Divider slide or major topic break. |
| **Subhead** | 18–22pt | 22–26pt | SemiBold | Slide content header (e.g., "Market Analysis"). |
| **Body Text** | 14–16pt | 14–16pt | Regular | Paragraph copy. Do not go below 14pt without explicit line-height increase. |
| **Caption / Footnote** | 10–12pt | 10–12pt | Regular | Source attribution, slide number, metadata. Use `muted` color from theme. |
| **Stat Hero (numbers)** | 60–96pt | 72–96pt | Bold | Large data visualizations (e.g., "340%" revenue growth). Thai +10% to account for tone-mark clearance. |

**Key compensation rule for Thai:** Thai vowels and tone marks sit *above* the baseline and extend above cap height. When mixing Thai and English:
- Thai subheadings are typically 4–6 points larger than EN equivalents to maintain visual balance
- Thai stat heroes are 10–15% larger
- Body text can remain equal size *if* you increase line-height (see Section 5)

---

## 5. Line Height & Spacing

Line height is measured as a multiplier (e.g., 1.5 = 150% of font size). Spacing is measured in points from the typography baseline.

### English Body Text
- **Line height:** 1.4–1.5x (40–45% of font size for 14–16pt)
- **Paragraph spacing:** 12pt after (before next paragraph)
- **Margin around text blocks:** 24–36pt (min 20pt)

### Thai Body Text
- **Line height:** 1.6–1.8x (56–72% of font size for 14–16pt)
- **Paragraph spacing:** 14pt after
- **Margin around text blocks:** 36–48pt (min 28pt)
- **Rationale:** Thai tone marks, vowel marks, and long vowels (ำ, ี, ู, etc.) require extra vertical space. Without it, lines jam together and become unreadable.

### Bilingual (Mixed TH+EN Body)
- **Use Thai spacing rules** (1.6–1.8x line height) for the entire text block, even if EN is present
- When Thai and EN are in the same paragraph, EN may appear loose; this is correct and preferable to cramped Thai

### Headers (All Languages)
- **Line height:** 1.1–1.3x (typically solid or tight)
- **Tracking (letter-spacing):** -0.02em for bold headers, 0em for regular
- **All-caps headers:** increase tracking to -0.01em (compressed all-caps look too tight otherwise)

---

## 6. Bilingual Layout Patterns (Preview)

These three patterns are the most common. Full implementation detail lives in `10-bilingual-handling.md`.

### Pattern A: Side-by-Side Title (TH | EN)
```
ความสำเร็จด้านการขาย  |  Sales Achievement
```
- Thai on left, EN on right, separated by a thin vertical rule (1–2pt)
- Both at the same font size
- Use when the slide is content-heavy and vertical space is constrained

### Pattern B: Stacked Title (EN Headline / TH Subhead)
```
Sales Achievement
ความสำเร็จด้านการขาย
```
- EN headline at 40–44pt, SemiBold
- TH subtitle at 22–26pt, Regular
- Use when the deck is primarily for EN audience with TH translation below

### Pattern C: Bilingual Body (TH First / EN Underneath)
```
ความสำเร็จด้านการขาย
(Sales Achievement)
```
- Thai at normal weight, EN in lighter weight (e.g., Regular vs. Normal, or lighter color `muted`)
- EN slightly smaller (1–2pt smaller) and indented 8–12pt
- Use for bullet points, annotations, and mixed-language lists

---

## 7. Font Installation Guidance

### macOS
1. **Via Homebrew (fastest for developers):**
   ```bash
   brew install font-inter font-lora font-ibm-plex-sans-thai
   ```

2. **Via Font Book:**
   - Download .ttf or .otf from Google Fonts or vendor site
   - Double-click the file → "Install Font" button
   - Verify in any application: Format → Font → [search font name]

3. **Google Fonts direct:**
   - Visit [fonts.google.com](https://fonts.google.com)
   - Click "Download" → Unzip → Drag to `/Library/Fonts/`

### Linux (Sandboxed Environment)
If running in a containerized or VM-sandboxed environment (CI/CD, build server, etc.):
1. Check if fonts are pre-installed: `fc-list | grep -i "Inter"`
2. If missing, use the helper script at `scripts/install_fonts.sh`
3. Script installs fonts to `~/.local/share/fonts/` and rebuilds font cache

### Fallback Chain (When Font Missing)
If a custom font is unavailable at render time, the application must follow this fallback chain:

#### For Thai
```
IBM Plex Sans Thai → Sarabun → TH Sarabun New → Anuphan → [System Thai Sans-Serif]
```

#### For English
```
Inter → Manrope → Source Sans 3 → Lora → [System Sans-Serif] (e.g., Helvetica, Arial)
```

#### For Serif (Fallback Only)
```
Playfair Display → Lora → Noto Serif Thai → [System Serif] (e.g., Times New Roman)
```

---

## 8. Common Typography Mistakes to Avoid

| Mistake | Why It Fails | Correct Approach |
|---|---|---|
| Using **Tahoma** for both Thai and EN | Dated appearance, weak kern pairs, Thai looks heavier | Use IBM Plex Sans Thai + Inter (or paired set from Section 2) |
| Using **Cordia New** | Deprecated, no longer maintained; poor Thai glyph support | Use Prompt or Sarabun instead |
| Mixing serif Thai (Noto Serif Thai) with sans EN (Inter) | Glyph weight mismatch; serif Thai is heavier, looks unbalanced | Keep both serif or both sans; use paired set |
| Thai body at 14pt without line-height compensation | Tone marks and vowels jam together; unreadable | Use 1.6–1.8x line-height for Thai at any size |
| Forgetting **TH Sarabun PSK** vs. **TH Sarabun New** | Government RFPs often specify one; using the wrong one fails technical review | Check customer requirement; if Thai government entity, default to TH Sarabun New |
| All-caps Thai with default letter-spacing | Looks cramped and amateurish | Use tracking (letter-spacing) +0.02em for Thai all-caps |
| Centering bilingual body text | EN text appears loose; Thai appears cramped; mixed centering looks chaotic | Use left-align or justified for bilingual blocks |

---

## 9. Font Weight Conventions

Most paired fonts come in multiple weights. Use these conventions:

| Context | Weight |
|---|---|
| **Slide title** | Bold (700) or ExtraBold (800) |
| **Section header** | Bold (700) |
| **Subhead** | SemiBold (600) |
| **Body text** | Regular (400) |
| **Emphasis within body** | SemiBold (600) or Bold (700) — sparingly |
| **Caption / footnote** | Regular (400), color `muted` |
| **Call-to-action (CTA button text)** | SemiBold (600) or Bold (700) |

---

## 10. Inter Font Variants (Special Note)

Google Fonts offers **Inter** and **Inter Tight**. Both are excellent; the difference:
- **Inter:** Standard width; slightly wider character spacing; better for accessibility and body text
- **Inter Tight:** Condensed width; better for headlines where space is constrained

Default is **Inter** for body; use **Inter Tight** only for headlines on ultra-dense slides. Never mix Inter and Inter Tight in the same body paragraph.

---

## 11. Quick Reference: By Personality

| Personality | TH Font | EN Font | TH Size Bump | Line-Height | Use Case |
|---|---|---|---|---|---|
| Modern Executive | IBM Plex Sans Thai | Inter | +5pt (subhead) | 1.6x (TH body), 1.4x (EN body) | Corporate, fintech, SaaS |
| Trust / Banking | Sarabun | Lora | +4pt (subhead) | 1.7x (TH), 1.5x (EN) | Banks, insurance, official |
| Tech-Forward | Prompt | Manrope | +5pt (subhead) | 1.6x (TH), 1.4x (EN) | Tech, startup, cloud |
| Premium / Luxury | Noto Serif Thai | Playfair Display | +6pt (subhead) | 1.8x (TH), 1.5x (EN) | Legal, real estate, heritage |
| Government / Restrained | TH Sarabun New | Source Sans 3 | +4pt (subhead) | 1.7x (TH), 1.4x (EN) | Government, RFP, formal |

---

## 12. Testing Your Pair

Before finalizing a deck, test every font pair at the actual intended sizes:

1. **Create a test slide** with the Thai title + EN title, bilingual body paragraph, and a data hero (e.g., "250% ROI")
2. **Project or share the PDF** on the actual display device (not just screen preview)
3. **Check for:**
   - Thai and EN glyphs aligned on the same baseline
   - No tone-mark crowding on Thai text
   - EN spacing not visually "lighter" than Thai
   - Readability at the back of the room (for in-person pitches)
4. **If misalignment appears,** adjust sizes (Thai +1–2pt) or swap to a different paired set

---

**End of 05-typography.md.** Continue to `06-imagery-and-data.md` for photography and chart guidelines, or `10-bilingual-handling.md` for detailed bilingual layout patterns.
