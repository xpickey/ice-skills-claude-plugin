# Customer CI Finder — Extract Customer Brand → Custom CI Pattern

> **Reference for:** b2b-slide-designer V03R01 (used by deliverable-gen-agent)
> **Purpose:** ค้นหา CI ลูกค้า → สร้าง Custom CI Pattern สำหรับ co-brand (iCE + customer) ใน PPTX/Word/Excel
> **⚠️ ANTI-HALLUCINATION:** ห้าม invent hex/font — ต้องสกัดจาก logo/brand จริงเท่านั้น

---

## PROCESS

```
INPUT: ชื่อลูกค้า + website / annual report / logo file

STEP 1 — FETCH brand asset:
  • logo ลูกค้า: จาก website, annual report PDF, หรือ /iCE-Brand/Customer-logo/ (ถ้ามี)
  • (มีตัวอย่าง: /iCE-Brand/Customer logo FG2026.pptx)

STEP 2 — EXTRACT brand color:
  • สกัด dominant hex 2-3 สีจาก logo (ใช้ imagecolorpicker.com หรือ image color extraction)
  • ระบุ primary brand color + secondary

STEP 3 — IDENTIFY brand font (ถ้าระบุได้):
  • จาก brand guideline ลูกค้า (ถ้ามี) — ไม่มี → ใช้ paired font ของ iCE (Raleway↔Kanit / Open Sans↔Sarabun)

STEP 4 — BUILD Custom CI spec:
  {
    customer: "<name>",
    primary: "<hex จาก logo>",      # สกัดจริง ไม่ invent
    secondary: "<hex>",
    accent: "<hex>",
    font_pair: { en: "...", th: "..." },
    logo_path: "<path>",
    co_brand_rule: "iCE logo + customer logo (positioning per deck type)"
  }

OUTPUT: CI spec JSON → deliverable-gen-agent ใช้ build (co-brand iCE + customer)
```

---

## CO-BRAND RULES (iCE + Customer)

```
• Cover/Title: customer logo เด่น + iCE logo (vendor) มุม
• Content slides: iCE logo มุม (เป็น vendor proposing) + customer brand color accent
• ใช้ customer primary color เป็น accent ใน deck (แสดงความใส่ใจ brand ลูกค้า)
• ห้ามทับ/แก้ logo ลูกค้า — ใช้ตามที่ได้มา (legal)
```

---

## ⚠️ ANTI-HALLUCINATION (บังคับ)

```
✗ ห้าม invent hex ("น่าจะเป็นสีน้ำเงิน #003366")
✓ สกัดจาก logo จริง (imagecolorpicker จาก logo file)
✗ ห้าม invent brand font
✓ จาก brand guideline จริง หรือ fallback iCE paired font
หาก fetch logo ไม่ได้ → needs_input: "ขอ logo/brand guideline ลูกค้า"
```

---

## 🚧 BUILD NOTE
customer logo = fetch ตอนใช้งานจริง (per customer) — ไม่ pre-store · image color extraction tool ตอน build

---

*Reference: customer-ci-finder.md | b2b-slide-designer V03R01 | 2026.06.01*
