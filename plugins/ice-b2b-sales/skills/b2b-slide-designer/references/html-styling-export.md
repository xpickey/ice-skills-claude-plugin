<!-- ============================================================
     html-styling-export.md — HTML Output Styling reference for b2b-slide-designer
     Companion to §5.6 (HTML Output Styling) in SKILL.md.

     Fixed-stage CSS model adapted from frontend-slides (MIT © 2025 Zara Zhang).
     Design thresholds follow design-principles.md (power-design, MIT © 2026 Jack Roberts).
     See NOTICE-html-slides.md for full license.
     ============================================================ -->

# HTML Output Styling — CSS Variable Export (Companion to §5.6)

> **บทบาท:** เมื่อ output เป็น **HTML deck** (ไม่ใช่ .pptx) — ไฟล์นี้คือสะพานจาก
> "Designer-Brief (theme/CI/font)" → "CSS variable spec" ที่ `b2b-presentation-creator`
> `scripts/build_html.py` รับไปใช้. slide-designer **ป้อน spec** — ไม่ build.
>
> **คงไว้:** §5.5.1 ยังเป็น SINGLE SOURCE ของ **font selection** (ไฟล์นี้ไม่ทับ — แค่ map
> ฟอนต์ที่ §5.5.1 เลือกแล้ว → web-safe CSS stack).

---

## 1. Theme → CSS Variable Map (ป้อนเข้า build_html.py `--css-vars`)

แต่ละ template/CI ของ slide-designer export เป็น `:root` token. build_html.py มี
DEFAULT_VARS (iCE Blue) อยู่แล้ว — ป้อนเฉพาะตัวที่ override:

```json
{
  "--accent":        "#1E66A4",
  "--accent-2":      "#41A8B5",
  "--stage-bg":      "#0d1117",
  "--slide-bg":      "#ffffff",
  "--text-primary":  "#141413",
  "--text-muted":    "#6e6b66",
  "--font-display":  "'Kanit','Raleway',system-ui,sans-serif",
  "--font-body":     "'Sarabun','Open Sans',system-ui,sans-serif",
  "--title-size":    "112px",
  "--subtitle-size": "40px",
  "--body-size":     "30px",
  "--slide-padding": "112px"
}
```

### Template → accent mapping (ผูกกับ 8 template เดิม)

| Template | `--accent` | `--stage-bg` | scheme |
|---|---|---|---|
| **iCE-CI / iCE-Propose** | `#1E66A4` (iCE Blue) | `#0d1117` | light slide / dark stage |
| **Cobalt** | `#1E40AF` | `#0a1128` | dark |
| **Onyx** | `#41A8B5` | `#000000` | premium dark |
| **Linen** | `#8a7a5c` | `#f5f3ee` | light |
| **Arctic** | `#0066ff` | `#0a0a0a` | clean |
| **Amber** | `#e8731c` | `#1a1a1a` | warm |
| **Whiteboard** | `#39d353` | `#fafafa` | light/internal |

> ค่า hex อ้างจาก template reference เดิม — ป้อนเป็น `--css-vars` ไม่แก้ build_html.py.

---

## 2. Web-Safe Font Fallback (จาก §5.5.1 → HTML stack)

HTML deck ใช้ฟอนต์จาก **Google Fonts CDN** (`display=swap`) — ฟอนต์ tier ของ §5.5.1
บางตัวเป็น macOS-only (Sukhumvit Set) → ต้องมี web fallback. ตารางนี้ map **ฟอนต์ที่
§5.5.1 เลือกแล้ว** → web-safe stack (ไม่เปลี่ยนการเลือก — แค่เพิ่ม fallback):

| §5.5.1 เลือก (TH+EN) | Web CDN | HTML fallback stack |
|---|---|---|
| **Sukhumvit Set** (T1, macOS-only) | ไม่มีบน CDN → ใช้ **Kanit** แทนบนเว็บ | `'Kanit','Sukhumvit Set',system-ui,sans-serif` |
| **IBM Plex Sans Thai** (T1 Alt) | ✅ Google Fonts | `'IBM Plex Sans Thai','IBM Plex Sans',system-ui,sans-serif` |
| **Sarabun** (T2) | ✅ Google Fonts | `'Sarabun','Open Sans',system-ui,sans-serif` |
| **Noto Sans Thai** (T2 Alt) | ✅ Google Fonts | `'Noto Sans Thai','Noto Sans',system-ui,sans-serif` |
| **Kanit** (display) | ✅ Google Fonts | `'Kanit','Raleway',system-ui,sans-serif` |
| **TH SarabunPSK** (T3 ราชการ) | ไม่มีบน CDN → ใช้ **Sarabun** แทนบนเว็บ | `'Sarabun','TH Sarabun New',serif` |

> **Bilingual rule (เหมือน PPTX latin+cs):** HTML ไม่มี `cs` slot แยก — แต่ต้องวาง
> **ฟอนต์ไทยก่อน Latin** ใน stack เสมอ (`'Sarabun','Open Sans'`) เพื่อให้ตัวไทย render
> ด้วยฟอนต์ที่ตั้งใจ ไม่ fallback ไป Latin-only ที่อักษรไทยแตก.

> **Sukhumvit/TH SarabunPSK บนเว็บ:** ถ้า audience เปิดบน Mac จะได้ฟอนต์จริง (อยู่ใน
> stack); เครื่องอื่นได้ web-equivalent (Kanit/Sarabun) ที่ใกล้เคียง — acceptable เพราะ
> HTML embed ฟอนต์ไม่ได้แบบ PPTX (ใช้ CDN + fallback แทน).

---

## 3. Fixed 16:9 Stage Rule (อ้าง viewport-base.css)

ทุก HTML deck **ต้อง** ฝัง `assets/html/viewport-base.css` (build_html.py ทำให้อัตโนมัติ):
- slide authored ที่ **1920×1080** เสมอ — scale ทั้ง stage ด้วย JS (ไม่ reflow ต่อ device)
- `.slide` ใช้ `visibility:hidden`+`opacity:0` สลับ (ไม่ใช่ `display:none` — กัน layout class override)
- letterbox/pillarbox ทุกจอ · `@media print` = 1 slide/page · `prefers-reduced-motion` รองรับ

---

## 4. WCAG Contrast (ตรงกับ §5 Quality Standards เดิม + design-principles rule 11)

- Body text contrast **≥4.5:1** (AA) — **aim 7:1 (AAA)** สำหรับ projector resilience
  (projector ลด contrast 30-50% — ดู design-principles.md §5)
- accent บน background ต้องผ่าน ≥3:1 (large text/UI)
- ตรวจจริงตอน QA (qa-master D7 HTML track) — ไม่ใช่แค่ตอน design

---

## 5. Handoff Checklist (slide-designer → build_html.py)

ก่อนส่ง spec ให้ presentation-creator build:
- [ ] เลือก template → ได้ `--accent` / `--stage-bg` / scheme
- [ ] เลือกฟอนต์จาก §5.5.1 → map เป็น web-safe stack (§2 ข้างบน) → `--font-display` / `--font-body`
- [ ] ฟอนต์ไทยอยู่หน้า Latin ใน stack (bilingual rule)
- [ ] ยืนยัน contrast ≥4.5:1 (accent vs slide-bg, text vs slide-bg)
- [ ] เลือก mode (presenter ≤25 คำ/slide · document ≤75) ตาม design-principles rule 20
