# Typography & Bilingual QA Gate
**Version:** V02R01 | **Date:** 2026.05.14 | **Companion to:** `../SKILL.md`

# Section 0 — Why This Gate Exists

Customer-facing decks and documents in Thailand are bilingual by default. Mixing a
Latin font and a Thai font badly produces an immediate signal of carelessness — the
reader sees uneven baselines, mismatched x-heights, and "two different documents stuck
together." The QA gate exists to keep that from leaving iCE.

The gate runs once, just before save. It takes 2–3 minutes. It catches roughly five
specific defects that recur in 90% of bilingual decks: dated Thai default fonts (Angsana
New, Cordia New) on modern proposals; Latin sans paired with a Thai serif by accident;
x-height mismatch making Thai look 20% smaller than the surrounding Latin; inconsistent
heading-vs-body font assignment; and government-formal documents using a corporate-
modern pair where TH SarabunPSK is mandatory by convention.

# Section A — When to Run This Gate

Run before saving any .docx, .pptx, or .pdf that will leave iCE. Specifically:

| Artifact | QA required? | Notes |
|---|---|---|
| Customer-facing proposal (.docx) | Yes | Always |
| Customer-facing pitch deck (.pptx) | Yes | Always |
| RFI/RFP/TOR response (any format) | Yes | Government-Formal pair often mandated |
| Board paper for external board | Yes | Same as customer-facing |
| Board paper for iCE internal use | Optional | Catch the worst defects only |
| Internal sitrep / working doc | Skip | Time cost > benefit |
| Email draft | Skip | Mail client governs font |
| Excel-only deliverable | Skip the deck checks | Run only Section D row 7 (table fonts) |
| PDF generated from an already-QA'd source | Skip | The source QA flows to the PDF |

If unsure, run the gate. Two minutes to be safe beats a customer seeing the wrong
font hierarchy.

# Section B — Approved Font Pairs

iCE deliverables observed in 2026.05 cluster into three calibration zones. Each zone
has an Approved Pair, a Backup Pair, and rules for when to apply.

## B.1 Corporate-Modern Pair

**Use when:** Customer is Public Listed, Mid-market, Trading, FMCG, Manufacturing,
Healthcare-private. Pitch decks, investment proposals, demo decks, board papers.

| Role | Latin | Thai |
|---|---|---|
| Headings (Major) | Raleway, weights 600–800 | Sukhumvit Set (Thick), weights 600–700 |
| Headings (Backup) | Aptos Display | IBM Plex Sans Thai |
| Body (Minor) | Open Sans, weight 400–500 | Sarabun (NOT TH SarabunPSK), weight 400 |
| Body (Backup) | Arial | Noto Sans Thai |
| Numbers / Data | Open Sans Tabular, weight 500 | Sarabun Tabular, weight 500 |

**Rationale:** Raleway / Sukhumvit Set carry similar geometric weight at heading sizes,
keeping bilingual headers visually equal. Open Sans / Sarabun pair at body size with
matched x-heights when Sarabun is set 2pt larger than Open Sans (see Section C).

**Source patterns observed:**
- `[CUSTOMER: Large Travel-Retail Group]` iCE EPM Presentation V02R01, 2026.05 —
  slide-level: Arial + Raleway; theme fallback: Calibri + Angsana New (slide-level
  override applied throughout).
- `[CUSTOMER: Integrated Poultry Group]` NetSuite Proposal V01R05, 2026.01 —
  slide-level: Arial + Century Gothic; theme fallback: Arial + Angsana New / Cordia
  New. NetSuite proposals trend toward this corporate-modern register, with Century
  Gothic surfacing as the heading-display face on title slides.
- `[CUSTOMER: Health Foods Corporation]` Propose Solution rev0.2, 2025.02 —
  slide-level: Arial + Raleway. Same register as Travel-Retail.
- `[CUSTOMER: Sports Apparel Group]` C-Suite Proposal DEMO v2.0, 2024.06 —
  slide-level: Arial + Raleway. Same register.
- `[BANK: Agricultural Cooperatives Bank]` ERP Roadmap, 2026.04 — slide-level:
  Montserrat + Poppins (Latin-only); theme fallback: Aptos Display / Aptos +
  Angsana / Cordia. SOE-Bank Roadmap drifted to a marketing-style Latin pair —
  notable because the parent organisation is SOE; this is the Roadmap-deck deviation,
  not the Comply-document register.

**Watch-out:** the Roadmap-deck variant (Montserrat + Poppins) is decorative and
appropriate for the CIO-Office audience, but a TOR Compliance Matrix derived from
the same project must NOT inherit it. Comply documents always reset to
Government-Formal pair (Section B.2) regardless of what the Roadmap deck looked
like.

## B.2 Government-Formal Pair

**Use when:** Customer is ราชการ, รัฐวิสาหกิจ, ราชการในกำกับของรัฐ, อปท., or any
e-Bidding / TOR Response under พรบ. 2560. RFI Response slide decks, TOR Comply
documents, Compliance Matrix workbooks.

| Role | Latin | Thai |
|---|---|---|
| Headings (Major) | Century Gothic, weight 700 | TH SarabunPSK, weight 700 |
| Headings (Backup) | Aptos Display | Sarabun (regular), weight 700 |
| Body (Minor) | Century Gothic, weight 400 | TH SarabunPSK, weight 400 |
| Body (Backup) | Arial, weight 400 | Sarabun (regular), weight 400 |
| Compliance Matrix | Arial, weight 400 (tabular) | TH SarabunPSK, weight 400 (tabular) |

**Rationale:** TH SarabunPSK is the de-facto Thai government typeface (specified in
government document standards). Century Gothic harmonises with TH SarabunPSK because
both share a geometric construction and similar x-height behaviour. Where Century
Gothic is not available on the customer's machine, Arial is the backup — never
Calibri (Calibri's humanist rounding clashes with TH SarabunPSK's geometric form).

**Source pattern observed:** `[QUASI-GOVT: Pharmaceutical Manufacturing Institute]`
RFI Response V01R04, 2026.05 — slide-level fonts: Century Gothic + Sarabun + TH
SarabunPSK.

## B.3 Corporate-Clean Pair

**Use when:** Customer is internal-facing, mid-market with no strong brand, or the
deliverable is a working document that doesn't need brand expression. NetSuite-track
proposals at mid-market often default here.

| Role | Latin | Thai |
|---|---|---|
| Headings (Major) | Calibri, weight 700 | Calibri (CSS fallback uses Sarabun for Thai glyphs) |
| Headings (Backup) | Arial, weight 700 | Sarabun, weight 700 |
| Body (Minor) | Calibri, weight 400 | Calibri / Sarabun (renderer-dependent) |
| Body (Backup) | Arial, weight 400 | Sarabun, weight 400 |

**Rationale:** Office 365 default in Thai locale renders Calibri Latin and falls back
to the OS Thai font. This is "neutral" — readable but unmemorable. Acceptable for
working documents, weaker for hero proposals.

**Source pattern observed:** `[CUSTOMER: Telecom-Services Group]` NetSuite EPM Budget
Investment V02R01, 2026.05 — slide-level fonts: Calibri only, falling back to theme
default Angsana New / Cordia New for Thai.

# Section C — X-Height Compensation Rules

Thai and Latin scripts have different baseline behaviour. Setting them at the same
point size produces a Thai script that looks roughly 15–20% smaller than the Latin
script around it. The fix is to set Thai 1–3 points larger.

## C.1 Default Compensation Table

| Latin Size (pt) | Thai Size (pt) | Use Case |
|---|---|---|
| 8 | 10 | Captions, footnotes (tight tables) |
| 9 | 11 | Compliance Matrix cells |
| 10 | 12 | Body in proposal .docx |
| 11 | 13 | Body in pitch deck (large room) |
| 12 | 14 | Sub-headings |
| 14 | 16 | Section headings |
| 16 | 18 | Slide headers |
| 18 | 20 | Cover page sub-titles |
| 24 | 28 | Slide section dividers |
| 32 | 36 | Cover page main title |

## C.2 Exceptions

- **TH SarabunPSK** rides closer to Latin x-height than Sarabun; reduce the
  compensation by 1pt when using TH SarabunPSK.
- **Angsana New / Cordia New** are old-style Thai fonts that need +2–3pt compensation
  even against the same Latin size. If forced to use them, compensate aggressively.
- **All-caps Latin headings** look visually larger than mixed-case at the same point
  size; reduce Thai compensation by 1pt when the Latin heading is set in all caps.
- **Tabular numbers** in financial tables — keep Latin and Thai the same point size to
  preserve column alignment. The visual size difference is acceptable in numeric
  context.

## C.3 Line-Height Rules

- Thai requires more vertical breathing room than Latin because of the upper and
  lower diacritics (vowels, tone marks).
- Default line-height: 1.4× for Latin, 1.6× for Thai when mixed; 1.5× when separated.
- Headings: tighten to 1.2× (Latin) and 1.3× (Thai) — denser headings read more
  professional.

# Section D — Pre-Save Checklist

Run these eight checks in order. Stop and fix on the first failure; do not save until
all pass.

| # | Check | Pass Condition |
|---|---|---|
| 1 | **Font pair zone identified** | Pair belongs to Corporate-Modern, Government-Formal, or Corporate-Clean per Section B |
| 2 | **Theme defaults overridden where used** | If theme says "Calibri / Angsana New" but slide uses different fonts, ensure the slide-level override is consistent across all slides |
| 3 | **No forbidden pair in body** | Section E forbidden combinations not present |
| 4 | **X-height compensation applied** | Section C table followed; Thai sized 1–3pt larger than Latin per row |
| 5 | **Heading vs body assignment consistent** | Major font is heading-only; Minor font is body-only; no swap on later slides |
| 6 | **All-caps and small-caps usage controlled** | All-caps used only for section dividers / cover; not for body Latin |
| 7 | **Table fonts match document body** | Tables don't drift to a third font (most common drift: pasted-in tables retaining Calibri 11pt) |
| 8 | **Bilingual line pairing tested visually** | Open one body slide / one body page, eyeball Thai vs Latin at body size — if Thai looks smaller, recompensate |

# Section E — Forbidden Pairs

Some combinations are visually broken even when individually approved. Never ship
with these.

| Forbidden Pair (Latin + Thai) | Why |
|---|---|
| Calibri + Angsana New | Calibri's humanist warmth clashes with Angsana New's serif formality; reads as "two unrelated documents" |
| Arial + Angsana New | Same clash, sharper because of Arial's stark grotesque vs. Angsana's old-style |
| Times New Roman + any Thai sans (Sarabun, Noto, TH SarabunPSK) | Serif Latin with sans Thai breaks the visual register entirely |
| Comic Sans + anything | Always |
| Cordia New + any modern Latin (Raleway, Aptos, Open Sans) | Cordia is geometrically old; modern Latin makes it look mis-aligned |
| Multiple sans-serif Latin fonts within one document | Pick one Latin font for body and stay |
| Multiple Thai fonts within one section | Same rule for Thai |
| TH SarabunPSK + Latin condensed/expanded (e.g. Arial Narrow, Bahnschrift) | Width mismatch; the Thai will look stretched or compressed |

# Section F — Fix Recipes

When the gate flags a defect, apply the matching recipe.

## F.1 Recipe: Theme defaults to Angsana / Cordia in slides

**Symptom:** Theme file says Calibri + Angsana New + Cordia New, but slide-level
overrides use a different pair (Raleway + Sarabun). The theme defaults leak through
on any newly-added slide.

**Fix:**
1. Open the deck's master / theme settings.
2. Replace the theme's major-font and minor-font for the Thai script row.
3. Save the theme; verify by inserting a new blank slide.
4. Existing slides with explicit overrides remain unchanged.

## F.2 Recipe: Thai looks 20% smaller than Latin in body

**Symptom:** A bilingual paragraph has Latin and Thai at the same point size; Thai
visually shrinks.

**Fix:**
1. Identify Latin body size (e.g. 10pt in a .docx).
2. Find Section C row matching that Latin size.
3. Apply Thai = Latin + 2pt (e.g. Thai 12pt).
4. Re-test by reading the paragraph from arm's length — Thai and Latin should now
   share visual weight.

## F.3 Recipe: Pasted-in table uses different font

**Symptom:** A table copied from another file shows Calibri 11pt when the host
document is Open Sans 10pt.

**Fix:**
1. Select the entire table.
2. Reset font to the document's body font.
3. Reset point size per Section C.
4. Re-test for x-height after the table re-flows.

## F.4 Recipe: Government deck uses Corporate-Modern pair

**Symptom:** A TOR Response or RFI deck is set in Raleway + Sarabun (Corporate-Modern)
instead of Century Gothic + TH SarabunPSK (Government-Formal).

**Fix:**
1. Confirm the document IS bound for a government / รัฐวิสาหกิจ audience.
2. If yes, swap the deck-wide font pair to Government-Formal per Section B.2.
3. Re-apply Section C compensation (TH SarabunPSK uses 1pt-less compensation).
4. Re-run Check 1–8 in Section D.

## F.5 Recipe: Latin headings in all-caps clash with Thai mixed-case

**Symptom:** Slide header "FINANCIAL CONSOLIDATION" in all-caps Latin sits next to
"การจัดทำงบการเงินรวม" in normal Thai; the all-caps Latin overpowers.

**Fix:**
1. Either: drop the all-caps and use mixed-case Latin matching Thai (preferred).
2. Or: reduce Thai compensation by 1pt to balance visual weight (acceptable for
   section-divider slides).
3. Do not bold the Thai to compensate — bolding changes glyph weight, not size.

## F.6 Recipe: Compliance Matrix cells overflow

**Symptom:** TOR Compliance Matrix table cells with Thai content overflow vertically;
the table doesn't fit a page.

**Fix:**
1. Confirm Thai is at the correct compensation size (Section C row 2 — Latin 9pt,
   Thai 11pt for Compliance Matrix cells).
2. If still overflowing, do NOT shrink Thai below 10pt. Instead:
   - Switch table orientation to landscape, or
   - Split the Compliance Matrix into multiple tables by TOR section, or
   - Use TH SarabunPSK (slightly narrower than Sarabun) to recover space.

# Section G — User Communication Templates

When the QA gate finds a defect that needs the user's decision, use these one-line
prompts to keep the loop tight.

| Defect | Prompt |
|---|---|
| Forbidden pair detected | "ผมตรวจพบ font pair ที่ห้ามใช้ (X + Y) ในเอกสารชุดนี้ ขออนุญาตเปลี่ยนเป็น Pair ที่อนุมัติ (Corporate-Modern / Government-Formal / Corporate-Clean) — ท่านต้องการให้ใช้ Pair ใดครับ?" |
| Wrong pair for audience | "เอกสารนี้เป็น TOR Response สำหรับ [SOE] แต่ใช้ Corporate-Modern pair ผมแนะนำให้สลับเป็น Government-Formal (Century Gothic + TH SarabunPSK) — ยืนยันหรือไม่?" |
| X-height compensation missing | "ผมพบว่า Thai script ใช้ point size เดียวกับ Latin (เช่น 10pt/10pt) ขออนุญาตปรับ Thai เป็น 12pt ตาม X-Height Compensation Rule — ยืนยันหรือไม่?" |
| Theme-default leak | "Theme ของไฟล์ตั้ง Calibri + Angsana New แต่ slide จริงใช้ Raleway + Sarabun ผมจะแก้ Theme ให้สอดคล้องเพื่อกันการ regress ใน slide ที่เพิ่มใหม่ — ยืนยันหรือไม่?" |
| Compliance Matrix overflow | "Compliance Matrix overflow แนวตั้ง ขอเสนอ 3 ทางเลือก: (a) Landscape, (b) Split per TOR section, (c) ใช้ TH SarabunPSK แทน Sarabun (แคบกว่า ~5%) — ท่านเลือกข้อใด?" |

# Section H — Maintenance Notes

- **Calibration drift.** When a new Microsoft Office version changes default fonts
  (e.g. Aptos became 365 default in 2023), re-verify Section B.3 fallback chain.
- **Theme template library.** If iCE maintains shared deck templates with embedded
  themes, audit the themes quarterly using Section D checklist.
- **Customer-mandated brand.** When a customer specifies their own font set (Marriott,
  Banpu, IIG family), that mandate overrides Section B. Capture the mandated pair as
  a one-off note in the customer folder; do NOT add it to Section B unless the customer
  recurs.
- **Government typeface updates.** TH SarabunPSK is the current default but Sarabun
  (without "PSK") is acceptable in newer government documents. Verify with the
  procurement reference before locking the pair for a TOR Response.

End of Typography & Bilingual QA Gate.
