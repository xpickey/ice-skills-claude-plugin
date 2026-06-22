# Color Palette Selection — Professional Color/Pattern Reference

> **Reference for:** b2b-slide-designer V03R01 (used by deliverable-gen-agent)
> **Purpose:** เลือกสี/palette อย่างมืออาชีพ สำหรับ PPTX/Word/Excel
> **หลัก:** แยก RULES (hardcode — ไม่เปลี่ยน) จาก TOOLS (live — ดึงตอน build เพราะ trending เปลี่ยน)

---

## RULES (hardcode — knowledge ถาวร)

```
60/30/10 RULE: primary 60% · secondary 30% · accent 10%

COLOR HARMONY: complementary (ตรงข้าม) · analogous (ข้างเคียง) · triadic (สามเหลี่ยม)

ACCESSIBILITY (WCAG): contrast ratio text/bg ≥ 4.5:1 (normal text) · ≥ 3:1 (large text)
  → ตรวจทุก text-on-color combination ก่อนใช้

INDUSTRY TONE (เลือกโทนตาม vertical):
  BFSI/Banking    → conservative: blue / navy (น่าเชื่อถือ มั่นคง)
  Energy/Utilities → green / earth tone (sustainability)
  Healthcare      → clean: teal / white (สะอาด ปลอดภัย)
  Hospitality     → warm tone (อบอุ่น ต้อนรับ)
  Public-Sector-TH → formal blue (ทางการ)
  Manufacturing   → industrial: steel / blue-gray
  Retail          → vibrant (สดใส ดึงดูด)
```

---

## INSTANCES (hex จริง — Design Library)

> 📌 **catalog-gradients.md = instance library** (29 gradient + hex + 5-stop ramp + use-case) —
> color-palette นี้มี RULES (60/30/10, harmony, WCAG) · catalog-gradients มี **ตัวอย่างจริงพร้อม hex**.
> เลือก gradient → `references/catalog-gradients.md` (by mood: cool/warm/dark/brand/green/pastel).

## TOOLS (live — ดึงตอน build, ไม่ hardcode)

```
imagecolorpicker.com              → ดึงสีจากภาพ/logo (สกัด dominant hex)
imagecolorpicker.com/color-code/{hex}  → color detail + variations + shades
coolors.co                        → palette generator (สร้าง harmony palette)
coolors.co/palettes/trending      → trending palettes (เปลี่ยนตลอด → ดู live)

🚧 BUILD NOTE: coolors hex อยู่หลัง JS — ถ้าต้อง trending จริง ใช้ browser/MCP fetch ตอน build (ไม่ใช่ตอนสร้าง skill)
```

---

## Workflow (เลือกสีสำหรับ deck)

```
1. ดู primary_industry → เลือก industry tone (RULES)
2. ถ้ามี customer CI → ใช้ customer-ci-finder ดึง brand color (co-brand)
3. ถ้าต้อง palette ใหม่ → coolors generate harmony (60/30/10)
4. ตรวจ WCAG contrast ทุก text-on-color
5. ออกมาเป็น palette spec: { primary, secondary, accent, bg, text, muted } + contrast verified
```

---

## iCE Default Palette (ฐาน — จาก iCE-Propose)
```
PRIMARY blue  #1E66A4 · SECONDARY teal #41A8B5 · body gray #595959 · H1 near-black #1E2937
SEMANTIC: success #16A34A · warning #D97706 · error #DC2626
(customize ต่อ customer ผ่าน customer-ci-finder ถ้าต้อง co-brand)
```

---

## Off-Catalog Palette → Custom-Theme Generation (§4.9)

เมื่อ brief ขอสีที่ไม่อยู่ใน catalog/CI (เช่น "moss/lichen/herbal", "neon cyber", "warm terracotta") → **อย่า outsource หรือ recolor มั่ว** ใช้ **§4.9 Custom-Theme Generation** ใน SKILL.md (สร้าง palette ใหม่: accent→paper→ink→greys, vibe-to-hue, WCAG check).

**Tint-neutral rule (anti-slop §4.8):** greys/neutrals **ห้ามใช้ pure `#000` / `#FFF`** — ต้อง tint เข้าหา accent hue เล็กน้อย (accent ฟ้า → ink `#1E2937` ไม่ใช่ `#000000`, paper `#FAFBFC` ไม่ใช่ `#FFFFFF`). pure black/white = AI default tell.

---

*Reference: color-palette-selection.md | b2b-slide-designer V03R01 | 2026.06.01*
