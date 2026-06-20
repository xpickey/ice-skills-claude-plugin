<!-- ============================================================
     13-html-deck-builder.md — HTML Presentation Slide blueprint
     Workflow + html-template structure adapted from frontend-slides
     (MIT © 2025 Zara Zhang) https://github.com/zarazhangrui/frontend-slides
     Design thresholds from design-principles (power-design, MIT © 2026 Jack Roberts).
     See references/NOTICE-html-slides.md for full license.
     ============================================================ -->

# Reference 13 — HTML Deck Builder (web-native presentation output)

> **เมื่อใช้:** Step 4.5 (Output Format Decision) เลือก `html` หรือ `both`. ไฟล์นี้คือ
> blueprint การสร้าง **HTML deck** (single-file, zero-dependency, fixed 16:9) — ทางเลือก
> output คู่กับ .pptx เดิม.
>
> **หลักสำคัญ:** build อยู่ที่ **skill นี้** (`scripts/build_html.py` + `scripts/extract-pptx.py`).
> เจนนี่ (deliverable-gen) **invoke skill** เพื่อรัน — ไม่เก็บ build logic เอง.

---

## ⚡ EXECUTION PATH — เลือกตาม Environment (อ่านก่อนทุกครั้ง)

> HTML deck สร้างได้ **2 ทาง** ขึ้นกับว่า env มี shell (Bash) ไหม — เหมือน pattern Higgsfield
> (CLI vs MCP). เลือกถูก path = capability ใช้ได้ครบทั้ง Claude Code / Cowork / Desktop / Web.

| Environment | มี Bash? | Path | วิธีสร้าง HTML |
|---|---|---|---|
| **Claude Code** (CLI/IDE) | ✅ มี | **PATH A — Script** | รัน `python scripts/build_html.py` (อัตโนมัติ, เร็ว, sanitize ในตัว) |
| **Claude Cowork / Desktop / Web** | ❌ ไม่มี | **PATH B — Inline** | model **ประกอบ HTML เอง** จาก template ในตัว skill (ไม่รัน python) |

### PATH A — Script (Claude Code, มี Bash)
```bash
python scripts/build_html.py --outline outline.json --css-vars theme-vars.json \
  --output "Deck_[Customer]_V01R01_[date].html"
# PPT→HTML: python scripts/extract-pptx.py input.pptx out/
```
build_html.py ฝัง viewport-base.css + JS controller + arrow-sanitize ให้อัตโนมัติ.

### PATH B — Inline (Cowork/Desktop/Web, ไม่มี shell)
สร้าง .html เองในcontext โดยอ่านไฟล์เหล่านี้จาก skill (ไม่ต้องรัน script):
1. **อ่าน `assets/html/html-template.md`** — skeleton HTML (มีจุด `<!-- PASTE viewport-base.css -->`)
2. **อ่าน `assets/html/viewport-base.css`** — วางแทนจุด PASTE (fixed-16:9 + JS scale logic)
3. **อ่าน `assets/html/animation-patterns.md`** — entrance/reveal CSS ตาม mood
4. **(optional) อ่าน `assets/html/templates/<slug>/design.md`** — palette/font ของ template ที่เลือก
5. **ประกอบเป็น .html เดียว** — ฝัง CSS+JS inline, แต่ละ slide = `<section class="slide">`, ใส่ css_vars จาก slide-designer §5.6
6. **Sanitize เอง (สำคัญ):** แทน `→` ด้วย `▸` ด้วยมือ (PATH B ไม่มี auto-sanitize ของ script)
7. **PPT→HTML ใน PATH B:** ถ้าไม่มี shell รัน extract-pptx.py ไม่ได้ → ขอให้ user ส่งเนื้อ .pptx เป็นข้อความ/รูป หรือทำใน Claude Code แทน

> **กฎเลือก path:** มี Bash → PATH A เสมอ (เร็ว+ปลอดภัยกว่า). ไม่มี → PATH B. เจนนี่
> (deliverable-gen) ตรวจ env ก่อน invoke: Claude Code = A · อื่น = B.
> **ผลลัพธ์เหมือนกัน:** single .html, 16:9, zero-dep — ต่างแค่วิธีประกอบ.

---

## 0. เทียบ HTML vs PPTX (เลือกถูกตั้งแต่ Step 4.5)

| | HTML deck | PPTX deck (Step 5 เดิม) |
|---|---|---|
| ส่ง/นำเสนอ | browser, แชร์ URL (Vercel), มือถือ | PowerPoint app, ไฟล์แนบ email |
| ฟอนต์ | Google Fonts CDN + fallback (embed ไม่ได้) | embed จริง (D1-D4, §5.1) |
| แก้โดยลูกค้า | inline edit (กด E) / แก้ HTML | PowerPoint |
| dependency | **zero** (1 ไฟล์ .html) | python-pptx + fonts |
| เหมาะกับ | demo เว็บ, microsite, แชร์ลิงก์, มือถือ | board paper, e-bidding, ส่งราชการ |

> **TH+EN/ราชการ/TOR** → มักต้อง .pptx (embed ฟอนต์, ส่งไฟล์). **demo/แชร์ลิงก์/มือถือ** → HTML.
> ไม่แน่ใจ → ถาม (Step 4.5) หรือทำ `both`.

---

## 1. Workflow (adapt จาก frontend-slides Phase model → B2B)

```
Mode A (new HTML deck):   Step 1-4 เดิม (theme/lang/outline) → Step 4.5=html → §2 build
Mode B (PPT→HTML):        §4 extract-pptx.py → outline.json → §2 build
Mode C (enhance HTML):    อ่าน .html เดิม → แก้ → re-verify 16:9/overflow (§5)
```

Step 1-4 ของ skill หลัก (Classify/Theme/Language/Outline) **ใช้ร่วมกัน** — HTML แตกต่างแค่
ตอน build (Step 4.5 เป็นต้นไป). outline.json ที่ approve แล้วใช้ได้ทั้ง 2 format.

---

## 2. Build HTML deck — invoke `scripts/build_html.py`

**ขั้นที่ 1 — เตรียม outline.json** (จาก Outline ที่ user approve ใน Step 4):

```json
{
  "title": "iCE Cloud ERP — Executive Briefing",
  "css_vars": { "--accent": "#1E66A4", "--accent-2": "#41A8B5" },
  "slides": [
    { "layout": "title",   "title": "...", "subtitle": "...", "notes": "..." },
    { "layout": "content", "title": "...", "bullets": ["...","...","..."] },
    { "layout": "section", "title": "..." },
    { "layout": "quote",   "body": "..." }
  ]
}
```
- `css_vars` มาจาก **b2b-slide-designer §5.6 / html-styling-export.md** (theme→CSS var + web-safe font)
- `layout` ∈ `title | content | section | quote` (build_html.py รองรับ)
- `notes` → ฝังเป็น HTML comment (speaker notes ไม่โชว์บน slide — Mayer redundancy)

**ขั้นที่ 2 — รัน build:**
```bash
python scripts/build_html.py \
  --outline outline.json \
  --css-vars theme-vars.json \
  --title "Deck Title" \
  --output "Deck_[Customer]_V01R01_[YYYY-MM-DD].html"
```
ได้ **single .html** ฝัง viewport-base.css + JS controller (scale/keyboard/touch) — เปิด browser ได้เลย.

**ขั้นที่ 3 — เลือก visual style (optional):** ดู `assets/html/bold-template-index.json`
(10 template B2B) → คัดด้วย metadata (mood/tone/formality/best_for) → อ่าน `templates/<slug>/design.md`
เฉพาะตัวที่เลือก → ดึง palette/font/layout ไปเป็น `css_vars` + custom CSS. **อย่าอ่านครบทุก template.**

---

## 3. Design Discipline (บังคับ — จาก design-principles.md ของ slide-designer)

ก่อน build ทุก HTML deck ผ่าน checklist (ดูเต็ม `b2b-slide-designer/references/design-principles.md`):
- **1 idea/slide** · headline ≤10 คำ · **glanceable ≤3 วินาที**
- **mode lock:** presenter ≤25 คำ/slide **หรือ** document ≤75 — ห้ามปน
- **60-30-10** color · **1 accent/slide** · WCAG **≥4.5:1** (aim 7:1 projector)
- **8-pt grid** spacing · ≤4 type sizes/slide · whitespace ≥40% (hero ≥60%, quote ≥70%)
- **≤3 bullets ≤8 คำ** หรือไม่มี bullet (ทิ้ง 6×6 rule)
- safe-zone ≥5% (96px บน 1920) · F/Z-pattern (headline top-left)

> เหล่านี้ **format-agnostic** — ใช้กับ .pptx ด้วย (Quality Charter §12 + design-principles เสริมกัน).

---

## 4. PPT → HTML conversion — invoke `scripts/extract-pptx.py`

แปลง .pptx เดิม → web (เนื้อหา + รูป + speaker notes; layout regenerate ตาม style ใหม่):

```bash
python scripts/extract-pptx.py input.pptx output_dir/
# → output_dir/extracted-slides.json + output_dir/assets/ (รูปที่ดึงออกมา)
```
**ผลลัพธ์ extracted-slides.json:** array ของ `{number,title,content[],images[],notes}`
→ แปลงเป็น outline.json (§2 schema) → ยืนยันเนื้อกับ user → build (§2).

**ดึงได้:** text (title+body) · images (ไฟล์แยก+ขนาด) · speaker notes · ลำดับ slide.
**ไม่ดึง:** shape/drawing, layout positioning, animation (regenerate ใหม่ตาม style ที่เลือก).
**dependency:** `python-pptx` (มีอยู่แล้วจาก PPTX flow — ไม่ต้องลงใหม่).

---

## 5. QA (Step 6 — HTML track; เจ้ระเบียบ D7 ตรวจซ้ำแยก context)

ก่อนส่งมอบ HTML deck — verify (build เองตรวจ + เจ้ระเบียบ adversarial):
- [ ] **16:9 lock** — เปิด browser, ลองย่อ/ขยาย → stage scale ทั้งก้อน ไม่ reflow
- [ ] **no overflow/overlap** — ทุก slide เนื้อไม่ล้นกรอบ 1920×1080, panel ไม่ทับ
- [ ] **keyboard/touch nav** — ←→ space, swipe ทำงาน
- [ ] **WCAG ≥4.5:1** — text vs bg, accent vs bg (วัด 9 จุดถ้า text บนรูป)
- [ ] **responsive** — เปิด 1280×720 + 1 phone viewport → letterbox ถูก ไม่แตก
- [ ] **prefers-reduced-motion** — animation ลดเมื่อ user ตั้งค่า
- [ ] **arrow sanitize** — ไม่มี `→` (build_html.py แทนเป็น `▸` ให้แล้ว — cross-format safe)

> LibreOffice/qlmanage ไม่เกี่ยวกับ HTML — ตรวจ HTML = เปิด **browser จริง** (Chrome/Safari)
> หรือ screenshot ผ่าน Playwright (`scripts/export-pdf.sh` ใช้ engine เดียวกัน).

---

## 6. Optional Phase 6 — Share & Export (on-demand เท่านั้น)

- **PDF export:** `scripts/export-pdf.sh <deck.html>` (Playwright screenshot 1920×1080 → PDF; `--compact` = 1280×720). ลง Playwright ครั้งแรก (~150MB Chromium).
- **Live URL:** `scripts/deploy.sh` (Vercel — ลูกค้าเปิดทุกอุปกรณ์ผ่านลิงก์). ต้องมี Vercel account (free).
- ทั้งคู่ **optional** — ลงเมื่อ user ขอ ไม่ใช่ของบังคับ.

---

## 7. Files (อยู่ใน skill นี้ — self-contained)

```
scripts/build_html.py            ← PATH A: HTML deck builder (Claude Code, มี Bash)
scripts/extract-pptx.py          ← PATH A: PPT→HTML (Mode B)
scripts/export-pdf.sh            ← optional PDF (Phase 6)
scripts/deploy.sh                ← optional Vercel (Phase 6)
assets/html/viewport-base.css    ← fixed-16:9 skeleton (PATH A ฝังอัตโนมัติ · PATH B วางเอง)
assets/html/html-template.md     ← PATH B: HTML skeleton สำหรับประกอบ inline (no-shell)
assets/html/animation-patterns.md← PATH B: entrance/reveal CSS ตาม mood
assets/html/bold-template-index.json   ← 10 B2B template metadata
assets/html/templates/<slug>/design.md ← อ่านเฉพาะตัวที่เลือก
references/design-principles.md  ← (อยู่ที่ slide-designer) 20 codified rules
references/html-styling-export.md← (อยู่ที่ slide-designer §5.6) CSS var + web-safe font
```
