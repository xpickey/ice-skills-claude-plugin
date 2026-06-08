# Reference 10 — Bilingual Handling (TH + EN)

This reference defines three distinct language modes for B2B decks and the layout patterns that make each one work without producing crowded, mechanically-translated slides.

---

## Why Bilingual Decks Fail

Most Thai+English bilingual decks fail because they treat both languages as equal text that must fit the same slide template:
- Thai and English have wildly different character densities (Thai has no space between words).
- Mechanical side-by-side layouts leave one language cramped while the other has breathing room.
- Single font choices (e.g. Sarabun for both) weaken the typographic hierarchy.
- Currency, date, and numeral formatting is inconsistent across slides.

This skill prevents that through explicit layout patterns: each language mode (TH-only, EN-only, or Bilingual) has dedicated layout rules that honor both languages' typographic needs.

---

## Mode 1 — TH-only (Domestic Audience)

**When to use:** Thai government TOR, อบจ./เทศบาล board presentations, Thai SME audiences, formal domestic procurement.

### Typography

From `05-typography.md`, use Thai-optimized stacks:
- **Headers:** Sarabun SemiBold / Prompt SemiBold / IBM Plex Sans Thai SemiBold
- **Body:** Sarabun / IBM Plex Sans Thai / Noto Sans Thai
- **Note:** For formal government TOR work, explicitly offer **TH Sarabun PSK** or **TH Sarabun New** as an alternative — many Thai government reviewers expect the official font on title slides.

### Sizing & Leading

- **Body text:** Add 5–10% size compensation vs. English (Thai characters are visually smaller at the same point size).
- **Line-height:** 1.6–1.8× (Thai benefits from more breathing room than English body text).
- **Example:** 14pt EN body = 14–16pt TH body with 1.7× line-height.

### Number Formatting

| Element | Format | Notes |
|---|---|---|
| **Numerals** | Western (1, 2, 3) | Thai numerals (๑, ๒, ๓) only for formal government or ceremonial docs; exception, not default |
| **Currency** | ฿ (Thai baht) | Always include symbol; e.g., ฿1,500,000 or ฿1.5M |
| **Thousands separator** | Comma (1,500) | Thai convention |
| **Date format** | `วันที่ DD เดือน BE-YYYY` | Formal: "วันที่ 26 เมษายน 2569" (BE year, +543 years); commercial: `DD/MM/YYYY` CE |
| **Decimals** | Period (1.5) | Not comma; Thai uses period as decimal |

### Special Considerations

- **Government TOR slides:** Title slide font should match the TOR template language preference (usually Sarabun PSK for formal government).
- **Large stat slides:** TH numerals work well for ceremonial budget presentations; ask user if unclear.
- **Date consistency:** If using BE (Buddhist Era), apply to all dates in the deck, not just one slide.

---

## Mode 2 — EN-only (International Audience)

**When to use:** International roundup, regional partnership pitch, vendor presentations to non-Thai stakeholders, cross-border investor decks.

### Typography

From `05-typography.md`, use EN-optimized stacks:
- **Headers:** Inter Tight / Manrope / Poppins / Playfair Display
- **Body:** Lora / Inter / Source Sans 3
- Defer to the industry theme's EN stack (from `02-themes-industry.md`).

### Sizing & Leading

- **Standard:** Follow the industry theme's typography settings.
- **No adjustment needed:** EN typography is the baseline.

### Number Formatting

| Element | Format | Notes |
|---|---|---|
| **Numerals** | Western (1, 2, 3) | Always — audience expects it |
| **Currency** | Varies by context | USD: $1,500,000; EUR: €1,500,000; THB: THB 1,500,000 or 1.5M THB; always state currency if regional mixed audience |
| **Thousands separator** | Comma (1,500,000) | EN convention |
| **Date format** | ISO (YYYY-MM-DD) or US (Month DD, YYYY) | ISO for tech/finance; US for general business; e.g., `2026-04-26` or `April 26, 2026` |
| **Decimals** | Period (1.5) | Standard |

### Special Considerations

- **Currency clarity:** If the audience is regional (APAC mix), always include the currency code (THB, SGD, etc.); do not assume.
- **Date ambiguity:** Avoid `DD/MM/YYYY` format — EN audiences read it as MM/DD/YYYY and misinterpret.

---

## Mode 3 — Bilingual TH + EN (Mixed Thai + International Audience)

**When to use:** Default for "bilingual deliverable." Thai C-suite + international stakeholders in the same room. Regional HQ with Thai local teams + parent-company observers.

### Font Pairing

ALWAYS use a paired set from `05-typography.md`:

| Pair | Headers | Body | Best for |
|---|---|---|---|
| **IBM Plex + Inter** | IBM Plex Sans Thai SemiBold (TH), Inter Bold (EN) | IBM Plex Sans Thai (TH), Inter (EN) | Tech, SaaS, modern enterprise |
| **Sarabun + Lora** | Sarabun SemiBold (TH), Lora Bold (EN) | Sarabun (TH), Lora (EN) | Finance, consulting, formal |
| **Prompt + Manrope** | Prompt SemiBold (TH), Manrope Bold (EN) | Prompt (TH), Manrope (EN) | Retail, consumer, energetic |
| **Noto Serif Thai + Playfair** | Noto Serif Thai SemiBold (TH), Playfair Bold (EN) | Noto Serif Thai (TH), Playfair (EN) | Premium, law, heritage |

**Rule:** Never mix unpaired fonts (e.g., Sarabun TH with Manrope EN). The visual weight must feel balanced or bilingual slides look incoherent.

### Three Sub-Patterns for Bilingual Layout

Choose **one sub-pattern per slide** based on content type and audience emphasis:

---

#### Sub-Pattern A: Side-by-Side (Left TH, Right EN)

**When:** Parallel headlines, labels, short bullet lists, agenda slides. Works best for slides that are ~40% content + ~60% visual.

**Layout specs:**
- **Column width:** 5.4" each on standard 13.33" slide (1920×1440px); gutter 0.5"
- **Vertical separator:** Thin 1pt rule (color: 40% of primary color) between columns
- **Text alignment:** TH left-aligned left column, EN left-aligned right column
- **Max content:** 5 short labels/bullets per column; beyond that, the slide becomes a wall of text

**Example slide types:**
- Agenda (TH labels in left column, EN labels in right)
- Feature comparison (TH feature name left, EN feature name right, shared visual middle/below)
- Timeline with bilingual labels

**Danger zone:** Do NOT use for body paragraphs or long explanations — the two-column layout forces narrower text width and makes reading harder for both languages.

---

#### Sub-Pattern B: Stacked Title (Primary Lang Large, Secondary Muted Below)

**When:** Title slides, section dividers, big-stat slides. Works best when one language is the primary communication vehicle and the other is a reference translation.

**Layout specs:**
- **Primary headline:** 36–44pt, full opacity, chosen based on audience emphasis (usually TH for Thai-dominant room, EN for international-dominant)
- **Secondary headline:** 14–18pt, 60% opacity, immediately below in the same font family
- **Single-language body:** Only the primary language; secondary language gets no body text
- **Vertical spacing:** 0.15"–0.2" between primary and secondary headlines

**Example:**
```
โปรแกรมคุณภาพผู้บริหาร
(Executive Steering Committee Program)

[Body in Thai only, describes the program]
```

**Decision rule:** Ask the user which language emphasizes their message (Thai for domestic board, EN for parent company observer).

---

#### Sub-Pattern C: Bilingual Body (Sequential Paragraphs)

**When:** Proposal narrative, detailed explanation, sections where both audiences need full context. Use sparingly — it risks overcrowding the slide.

**Layout specs:**
- **Primary paragraph:** 14–16pt, full opacity (100%)
- **Secondary paragraph:** 13–15pt, 70% opacity, immediately below in muted color (60% primary color + 20% text color)
- **Visual separator:** 0.2" gap between paragraphs; optional thin rule in muted color
- **Max length:** One short paragraph per language; anything longer should be split into two slides

**Example:**
```
ยุทธศาสตร์การลงทุนเน้นการสร้างมูลค่าระยะยาว ผ่านการพัฒนาบุคลากร
การปรับปรุงกระบวนการผลิต และการลดต้นทุน

[14pt TH, full opacity]

Our investment strategy focuses on long-term value creation through talent
development, manufacturing process improvements, and cost reduction.

[13–15pt EN, 70% opacity]
```

**Anti-pattern:** Do NOT use bilingual body for lists or data. Use side-by-side or pick one language for the data; the other gets a label translation (Stacked Title pattern).

---

## Decision Tree: Which Sub-Pattern?

```
START: Bilingual slide content

├─ Is this a HEADLINE + LABEL SLIDE (agenda, feature list, timeline)?
│  └─ YES → Side-by-Side (Pattern A)
│
├─ Is this a TITLE SLIDE or BIG STAT (one central message)?
│  └─ YES → Stacked Title (Pattern B)
│  └─ NO, continue below
│
├─ Is this a NARRATIVE PARAGRAPH (explanation, rationale, proposal)?
│  └─ YES → Bilingual Body (Pattern C)
│  └─ NO, continue below
│
└─ NO CLEAR FIT → Ask the user; default to Stacked Title (Pattern B)
   if uncertain.
```

---

## Detailed Layout Rules

### Side-by-Side (Pattern A)

**Specifications:**

| Spec | Value | Rationale |
|---|---|---|
| Column width | 5.4" each | 50% of 13.33" slide minus 0.5" gutter |
| Gutter | 0.5" | Visual breathing room; 1pt vertical rule in muted color |
| Text width | 5.0" per column | 0.2" margin inside each column |
| Vertical separator | 1pt, muted color | Subtle; 40% opacity of primary color |
| Max bullets per column | 5 | Beyond this, reading speed drops |
| Headline per column | 18–24pt | Smaller than single-language slide (60–70% of single-lang size) |
| Body text | 12–14pt | Reduced from single-language (constraint: narrow width) |

**Sizing example (Trust Navy theme, TH + EN agenda):**
- Slide title (full width): Inter Tight 32pt EN + Sarabun 32pt TH stacked
- Left column header "วาระประชุม": IBM Plex Sans Thai 20pt
- Right column header "Agenda": Inter 20pt
- Left column items: Sarabun 13pt, 1.5× line-height
- Right column items: Inter 13pt, 1.4× line-height

---

### Stacked Title (Pattern B)

**Specifications:**

| Spec | Value | Rationale |
|---|---|---|
| Primary headline size | 36–44pt | Dominant; room for 1–2 lines TH or EN |
| Secondary headline size | 14–18pt | Supportive; clearly subordinate |
| Secondary opacity | 60% | Visible but not competing |
| Vertical gap | 0.15"–0.2" | Tight coupling; single visual unit |
| Body text (single lang) | 14–16pt | Full slide width available |
| Body opacity | 100% | Primary language only |
| Line-height (body) | 1.6–1.8× (TH) / 1.4–1.5× (EN) | Match language needs |

**Sizing example (TH-primary audience, Finance proposal):**
- Primary headline (TH): Sarabun Bold 40pt, "ความเสี่ยงการดำเนินการ"
- Secondary headline (EN): Lora Italic 16pt at 60% opacity, "Operational Risk"
- Body (TH only): Sarabun 15pt, 1.7× line-height, full description

---

### Bilingual Body (Pattern C)

**Specifications:**

| Spec | Value | Rationale |
|---|---|---|
| Primary paragraph | 14–16pt, 100% opacity | Full readability |
| Secondary paragraph | 13–15pt, 70% opacity | Visible translation; not distraction |
| Secondary color | Muted (60% primary + 20% text) | Visually recessive |
| Vertical gap | 0.2" | Clear separation |
| Optional separator rule | 0.5pt, muted | Subtle; use for proposals, not casual slides |
| Max paragraphs | 1 per language | Prevents wall-of-text effect |
| Line-height | 1.6× (TH) / 1.4× (EN) | Balanced readability |

**Sizing example (SaaS proposal, mixed audience):**
- Primary paragraph (TH): IBM Plex Sans Thai 15pt, 1.6× line-height, 100% opacity
- Blank space: 0.2"
- Secondary paragraph (EN): Inter 14pt, 1.4× line-height, 70% opacity (text color)

---

## Translation Discipline (Anti-Hallucination)

### Rule 1: Never Machine-Translate Customer-Specific Content

Do NOT auto-translate:
- Customer names, project codes, contract values
- Stakeholder titles, department names
- Custom terminology (e.g., a client's proprietary process name)
- Technical specifications from their TOR

**Action:** Always ask the user: "ขอเรียนขอ official translation ของ [term/name] ครับ ผมจะใช้เวอร์ชันที่ท่านให้มา"

### Rule 2: Acceptable Generic Translations

Safe to translate standard business phrases without asking. Use the **Standard Rendering Glossary** below.

### Rule 3: Flag Ambiguous Terms

If a term has multiple valid translations depending on context (e.g., "Solution" = "วิธีการแก้ไข" vs. "บริการ"), ask the user which version fits.

---

## Standard Rendering Glossary (EN ↔ TH)

For generic, context-independent business terms, use this glossary without asking. If the term is not listed or context-specific, ask the user.

| English | Thai | Use Case |
|---|---|---|
| Executive Summary | สรุปผู้บริหาร | Proposal, business case |
| Agenda | วาระการประชุม | Meeting slides, agenda |
| Next Steps | ขั้นตอนต่อไป | Close slide, action items |
| Why Us | ทำไมต้องเรา | Sales pitch |
| Why Now | ทำไมต้องตอนนี้ | Urgency, business case |
| Investment | การลงทุน | Financial slides |
| Return on Investment (ROI) | ผลตอบแทนการลงทุน | Financial analysis |
| Risk | ความเสี่ยง | Risk assessment |
| Mitigation | การบรรเทาผล | Risk response |
| Timeline | ตารางเวลา | Project planning |
| Deliverables | ผลลัพธ์ที่ต้องสัง่ | Project scope |
| Success Criteria | เกณฑ์ความสำเร็จ | Project KPI |
| Key Performance Indicator (KPI) | ตัวชี้วัดผล | Metrics |
| Cost Savings | การประหยัดต้นทุน | Financial benefit |
| Revenue Growth | การเติบโตของรายได้ | Financial benefit |
| Market Share | สัดส่วนตลาด | Competitive position |
| Customer Retention | การรักษาลูกค้า | Business health |
| Quality Assurance | การรับประกันคุณภาพ | Operational discipline |
| Implementation | การดำเนินการ | Project phase |
| Go-Live | เปิดใช้งาน | Launch |
| Stakeholder | ผู้มีส่วนได้ส่วนเสีย | Governance |
| Governance | การกำหนดนโยบาย | Leadership structure |
| Compliance | การปฏิบัติตามกฎหมาย | Legal/regulatory |
| Sustainability | ความยั่งยืน | ESG/long-term |
| Digital Transformation | การปรับปรุงดิจิทัล | Technology change |
| Cloud Infrastructure | โครงสร้างพื้นฐานคลาวด์ | Technology |
| Data Security | ความปลอดภัยข้อมูล | IT/risk |
| Innovation | นวัตกรรม | Strategy |
| Partnership | ความเป็นหุ้นส่วน | Collaboration |

---

## Number, Date & Currency Formatting Rules

### Currency

**Bilingual slides (Stacked Title or Side-by-Side):**
- Always use symbol: `฿1,500,000` (Thai baht)
- For very large numbers, executive shorthand is acceptable: `฿1.5M`
- When ambiguity exists (regional audience), spell it: `THB 1.5M` or `1,500,000 Thai Baht`
- If mixed currencies in the same deck (e.g., HQ budget in USD, Thailand ops in THB), label all clearly: `Investment: USD 5M (HQ) + THB 50M (Local Ops)`

### Dates on Bilingual Slides

**Title slide (dual-format):** Show both, separated by slash
```
26 April 2026 / 26 เมษายน 2569
```

**Body slides (single-format):** Pick one per language
- TH: `วันที่ 26 เมษายน 2569` (formal) or `26/04/2569` (shorthand)
- EN: `April 26, 2026` (US) or `2026-04-26` (ISO)

**BE vs. CE:** Thai government often expects BE (Buddhist Era, +543 years). Commercial Thai typically uses CE. Bilingual decks default to CE with optional BE in parentheses for clarity:
```
วันที่ 26 เมษายน 2569 (CE 2026)
```

### Numerals

**Bilingual slides:** Use Western numerals (1, 2, 3) in body text. Thai numerals (๑, ๒, ๓) only for ceremonial government decks — ask the user if unsure.

**Stat callouts (bilingual):** Pick ONE numeral system per slide, not mixed. If a slide has a large stat in Thai numerals, all numbers on that slide should be Thai numerals.

---

## Common Layout Pitfalls & Fixes

### Pitfall 1: Uneven Title Wrapping

**Problem:** TH title wraps to 2 lines, EN title stays 1 line (or vice versa) when stacked.

**Fix:** Cap TH headlines at 60 characters, EN at 80 characters. If either exceeds, rewrite:
- Original (TH 72 chars): "ความสามารถในการดำเนินการและการบรรยายของระบบการจัดการคุณภาพ"
- Revised (TH 58 chars): "ความสามารถการบรรยายของระบบจัดการคุณภาพ"

### Pitfall 2: Mixed Numeral Systems in Stats

**Problem:** Side-by-side slide shows `฿1,500,000` (TH side) and `$1,500,000` (EN side) — the reader doesn't know which is which at a glance.

**Fix:** Add currency code; better yet, unify the stat in one position and translate the label:

```
LEFT COLUMN            RIGHT COLUMN
"ต้นทุนการลงทุน"        "Investment Cost"
฿1.5M                  ฿1.5M
(same stat, both languages)
```

### Pitfall 3: Side-by-Side Body Text

**Problem:** Long paragraphs in side-by-side columns become cramped and hard to read.

**Fix:** Convert to Stacked Title (single language body) or Bilingual Body (sequential paragraphs) if both languages are essential.

### Pitfall 4: Thai Text Overflow in Narrow Columns

**Problem:** Thai text in a 5.4" column forces tight wrapping; compound words don't break cleanly.

**Fix:** Reduce font size 1–2pt or increase column width. If neither is possible, move to a different pattern (Stacked Title or Bilingual Body).

---

## QA Checklist for Bilingual Slides

Before finalizing:

- [ ] **TH spell check:** Run Thai spell checker (e.g., Typo Assistant plugin)
- [ ] **EN spell check:** Run English spell checker
- [ ] **TH font rendering:** No `?` boxes; glyphs stack correctly (Thai tone marks align)
- [ ] **EN font rendering:** No missing glyphs; kerning is even
- [ ] **Line breaks (TH):** No orphaned particles at end of line (e.g., "ที่" alone)
- [ ] **Line breaks (EN):** No widows/orphans; no hyphens mid-word unless necessary
- [ ] **Date consistency:** All dates use the same format across the deck
- [ ] **Currency consistency:** All currency symbols and amounts are formatted identically
- [ ] **Numeral consistency:** Only one numeral system per slide (no mixing Thai + Western)
- [ ] **Font pairing:** TH and EN fonts come from the same paired set (from `05-typography.md`)
- [ ] **Pattern consistency:** Bilingual slides use the same sub-pattern (all Side-by-Side, not a mix of A + B + C)
- [ ] **Opacity hierarchy:** Secondary language is visibly subordinate (70% or 60% opacity where applicable)
- [ ] **Gutter/margin:** Vertical separator (if used) is subtle (1pt, muted color); columns have 0.2" inner margin minimum

---

**End of 10-bilingual-handling.md.** Continue to `05-typography.md` for paired font stacks, or `02-themes-industry.md` for industry color/font defaults.
