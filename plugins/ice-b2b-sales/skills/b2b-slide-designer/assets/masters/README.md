# แม่แบบ .pptx ของ iCE — iCE-Propose_Master.pptx

> **Version:** V01R01 | **Date:** 2026.09.05 | Wave B ของแผนแก้ทีม agent จาก log สิงหาคม–กันยายน 2026
> **ไฟล์นี้ใช้ทำอะไร:** อธิบายว่าแม่แบบคืออะไร layout แต่ละชื่อใช้กับหน้าแบบไหน placeholder ชื่ออะไร เรียกใช้อย่างไร และอะไรที่ยังไม่บังคับ — ย่อหน้าแรกของหัวข้อ "สรุปสำหรับ skill" นำไปวางใน SKILL.md ได้ทันทีเมื่อ user อนุมัติ
> **สถานะ:** รอ user อนุมัติแม่แบบจากภาพ render ใน `_review/` ก่อน ยังไม่เปิดด่านบังคับ

## สรุปสำหรับ skill (หนึ่งย่อหน้า)

แม่แบบ `iCE-Propose_Master.pptx` คือไฟล์ PowerPoint ขนาด 16:9 (13.333 × 7.5 นิ้ว) ที่ฝังฟอนต์ theme ทั้งสามช่อง (latin, ea, cs) เป็นฟอนต์รางเอกชนจาก `~/.claude/agents/_lib/font_policy.py` สี theme จาก `iCE-Design-System/tokens/tokens.json` โลโก้ เส้นทองบาง footer และเลขหน้าไว้ใน master แล้ว พร้อม layout 10 แบบที่มี placeholder จริง (`cover` `divider` `action-title-body` `two-column` `three-card` `table` `timeline` `closing` `appendix` และ `blank`) builder จึงไม่ต้องวาดพื้นหลัง หัวเรื่อง โลโก้ หรือ footer เองอีก แค่เลือก layout ตามชื่อแล้วเติมเนื้อหาลง placeholder วิธีเรียกคือตั้งตัวแปรแวดล้อม `ICE_TEMPLATE=<path ของแม่แบบ>` หน้าคำสั่ง build (`build_pptx.py` และ `build_deck.py` รองรับแล้ว ไม่ตั้งตัวแปร = พฤติกรรมเดิมทุกอย่าง) ผลที่วัดได้จาก deck ตัวอย่าง 9 หน้า: เฉลี่ย 7 shape ต่อหน้า (เดิม 47) ผ่านตัวตรวจเลย์เอาต์ ฟอนต์ โครงสร้างไฟล์ และ render เป็น PDF ด้วย LibreOffice ตัวจริงโดยฟอนต์ฝังครบ ปัจจุบันยังไม่บังคับใช้ผ่านด่านก่อนสร้าง (โค้ดของด่านเขียนไว้เป็นคอมเมนต์ใน `~/.claude/hooks/ice-prebuild-guard.sh` ด่าน E รอ user อนุมัติ)

## ไฟล์ในโฟลเดอร์นี้

| ไฟล์ | คืออะไร |
|---|---|
| `iCE-Propose_Master.pptx` | แม่แบบตัวจริง (ต้นทางเดียว — โฟลเดอร์ `iCE-Design-System/presentation/` มีแค่ไฟล์ชี้มาที่นี่ ไม่มีสำเนา) |
| `make_master.py` | สคริปต์สร้างแม่แบบจากศูนย์ แก้สี ตำแหน่ง หรือ layout ให้แก้ที่นี่แล้วรันใหม่ ไม่แก้ในไฟล์ .pptx ด้วยมือ (แก้มือแล้วครั้งถัดไปที่รันสคริปต์จะทับหาย) |
| `README.md` | ไฟล์นี้ |
| `_review/` | deck ตัวอย่าง 9 หน้า (`iCE-Propose_Sample-9-layouts.pptx` + `.pdf` + `layout-1.png` ถึง `layout-9.png` + `contact-sheet.png`) และ spec ที่ใช้สร้าง (`sample-spec.json`) สำหรับให้ user เปิดดูทุก layout ก่อนอนุมัติ — ไฟล์ทดสอบเก็บที่นี่เท่านั้น |

## Layout แต่ละชื่อใช้กับหน้าแบบไหน และ placeholder ชื่ออะไร

ตัวเลขในวงเล็บคือ `idx` ของ placeholder (ใช้กับ `slide.placeholders` ของ python-pptx) · หัวเรื่องของทุกหน้าคือ `slide.shapes.title` · ทุกหน้าเนื้อหามี **icon นำหน้าหัวเรื่อง (pic 10)** ขนาด 0.75 นิ้ว เพื่อให้ทุกหน้ามีภาพประกอบตามกฎข้อ 2 ของแนวทางการทำสไลด์ · footer (11) และเลขหน้า (12) อยู่ในทุก layout ยกเว้น `cover` และ `closing`

| layout | ใช้กับหน้า | พื้น | placeholder |
|---|---|---|---|
| `cover` | หน้าปกของชุดเอกสาร | เข้ม ไล่เฉดน้ำเงิน→ฟ้า เส้นทองเฉียง โลโก้ขาวมุมซ้ายล่าง | ชื่อชุดเอกสาร (1) · ชื่อเรื่องหลัก (title) · คำอธิบายหนึ่งประโยค (2) · จัดทำสำหรับ/โดย/วันที่ (3) |
| `divider` | หน้าคั่นหัวข้อ | เข้ม โลโก้ขาวมุมขวาบน | เลขหัวข้อ (1) · ชื่อหัวข้อ (title) · ประโยคบอกว่าช่วงนี้ตอบคำถามอะไร (2) |
| `action-title-body` | หน้าเนื้อหาทั่วไป: หัวเรื่องประโยค + bullet ด้านซ้าย + ภาพ/แผนภาพ/icon ด้านขวา | อ่อน | icon หัวเรื่อง (pic 10) · bullet (1) · พื้นที่ภาพขวา 4.7 × 4.55 นิ้ว (pic 2) |
| `two-column` | เปรียบเทียบสองด้าน (ปัจจุบัน/เป้าหมาย · ทางเลือก ก/ข) | อ่อน มีเส้นทองคั่นกลาง | icon หัวเรื่อง (pic 10) · icon ซ้าย (pic 5) · หัวข้อซ้าย (1) · เนื้อหาซ้าย (2) · icon ขวา (pic 6) · หัวข้อขวา (3) · เนื้อหาขวา (4) |
| `three-card` | สามประเด็นเท่ากัน (ประโยชน์สามข้อ · ตัวเลือกสามทาง · ตัวชี้วัดสามตัว) | อ่อน การ์ดสามใบ แถบบนไล่เฉดน้ำเงิน→ฟ้า | icon หัวเรื่อง (pic 10) · การ์ดที่ 1: icon (pic 1) หัวข้อ (2) เนื้อหา (3) · การ์ดที่ 2: (pic 4) (5) (6) · การ์ดที่ 3: (pic 7) (8) (9) |
| `table` | ตารางเปรียบเทียบ ตารางราคา ตารางความรับผิดชอบ | อ่อน | icon หัวเรื่อง (pic 10) · ตาราง (tbl 1 — ใช้ `insert_table(rows, cols)`) · หมายเหตุ/ที่มา (2) |
| `timeline` | แผนงานสี่ช่วง ลำดับขั้นตอน | อ่อน เส้นแกนเวลาไล่เฉด + หมุดเลข 1–4 | icon หัวเรื่อง (pic 10) · ป้ายช่วงที่ 1–4 (1–4) · รายละเอียดช่วงที่ 1–4 (5–8) |
| `closing` | หน้าปิด ขอบคุณ ขั้นถัดไป ผู้ติดต่อ | เข้ม โลโก้ขาวมุมซ้ายล่าง | ขอบคุณ (title) · ประโยคปิด (1) · ผู้ติดต่อ (2) |
| `appendix` | ภาคผนวก ข้อมูลประกอบ | อ่อน มีป้าย "ภาคผนวก" เหนือหัวเรื่อง | icon หัวเรื่อง (pic 10) · เนื้อหาเต็มความกว้าง (1) |
| `blank` | หน้าที่ต้องวาด infographic เองทั้งหน้า (ยังได้พื้น โลโก้ เส้นทอง footer เลขหน้าจาก master) | อ่อน | footer (11) · เลขหน้า (12) เท่านั้น |

ค่าคงที่ของกริด: ขอบทุกด้าน 0.6 นิ้ว (safe margin ≥ 0.4) · หัวเรื่อง 26pt ตัวหนา สี navy เข้ม กว้าง 10.2 นิ้ว สูง 1.05 นิ้ว (สองบรรทัด) · เส้นทองใต้หัวเรื่องที่ y = 1.65 · พื้นที่เนื้อหา y = 1.95 ถึง 6.5 · เนื้อหา 18pt (bullet สีฟ้า) ระดับสอง 16pt · การ์ดและคอลัมน์ 16pt · footer และเลขหน้า 10pt · ขนาดตัวไทย = ตัวอังกฤษ ไม่บวก pt ตามวินัย D3

## วิธีเรียกใช้

```bash
# builder ทั่วไป (spec.json → .pptx) — โหมดแม่แบบ
ICE_BUILD=pipeline ICE_DESIGN=briefed ICE_BASE=NEW \
ICE_TEMPLATE=~/.claude/skills/b2b-slide-designer/assets/masters/iCE-Propose_Master.pptx \
python3 ~/.claude/agents/_lib/build_pptx.py spec.json out.pptx

# builder ของ skill b2b-presentation-creator (outline + theme → .pptx) — โหมดแม่แบบ
ICE_TEMPLATE=~/.claude/skills/b2b-slide-designer/assets/masters/iCE-Propose_Master.pptx \
python3 ~/.claude/skills/b2b-presentation-creator/scripts/build_deck.py --outline outline.json --theme theme.json --language th --output out.pptx
```

สิ่งที่ builder ทำเมื่อมี `ICE_TEMPLATE`: เปิดแม่แบบ ลบสไลด์ตัวอย่างที่ติดมา (ถ้ามี) เลือก layout ตามชื่อ เติม placeholder ถอด placeholder ที่ไม่ได้ใช้ออก และยก footer กับเลขหน้าจาก layout ลงสไลด์ให้ (python-pptx ไม่ทำสองอย่างหลังให้เอง PowerPoint แสดง footer และเลขหน้าเฉพาะเมื่อสไลด์มี placeholder ของตัวเอง)

**spec ของ `build_pptx.py` ในโหมดแม่แบบ** — ชื่อ layout ใช้ได้ทั้งชื่อเดิมของ builder (`title` `section` `bullets` `two_column` `table` `kpi` `image` `thanks`) และชื่อของแม่แบบข้างบน · คีย์เพิ่ม: ระดับ deck `footer` `icon_color` · ทุกหน้าเนื้อหา `icon` (ชื่อไฟล์ในคลัง เช่น `mdi-finance` — ดู `../icons/INDEX.md`) · `cover`: `kicker` `subtitle` `meta` · `divider`: `number` `subtitle` · `action-title-body`: `bullets` + `image_path` หรือ `image_icon` · `two-column`: `left_title` `left` `left_icon` `right_title` `right` `right_icon` · `three-card`: `cards: [{icon, title, text|bullets}]` (หรือแปลงจาก `kpis` ให้) · `table`: `headers` `rows` `note` · `timeline`: `phases: [{label, text}]` ไม่เกินสี่ · `closing`: `subtitle` `contact` · `appendix`: `bullets` · bullet ระดับสองเขียนขึ้นต้นด้วยสองช่องว่างหรือ `{"text": "...", "level": 1}` — ตัวอย่างครบทุก layout อยู่ที่ `_review/sample-spec.json`

**`build_deck.py` ในโหมดแม่แบบ** ยังวาดเนื้อหาด้วยฟังก์ชันเดิมของมัน (textbox และรูปทรง) แต่วาดบนแม่แบบ: `title-hero` ใช้ layout `cover` (ไม่วาดพื้นหลังทับ ตัวอักษรขาว) หน้าอื่นใช้ `blank` หรือระบุรายหน้าด้วย `"template_layout": "<ชื่อ>"` ใน outline · footer และเลขหน้ามาจากแม่แบบ ไม่วาดซ้ำ

## การเปลี่ยนแม่แบบ

แก้ที่ `make_master.py` เท่านั้น (สี ตำแหน่ง ขนาดตัวอักษร layout ใหม่) แล้วรัน `python3 make_master.py` ตามด้วยสามคำสั่งตรวจ: `validate_pptx_structure.py` กับไฟล์แม่แบบ · build `_review/sample-spec.json` ใหม่ด้วยคำสั่งข้างบน · `render_pdf.sh` แล้ว `pdftoppm -png -r 110` ดูภาพทุกหน้า · ค่าออกแบบมาจากสามที่: สีและไล่เฉดจาก `tokens.json` · หน้าตาจาก `iCE-Design-System/presentation/presentation.html` (ปก คั่น ปิด = พื้นเข้ม) และ `presentation-light.html` (หน้าเนื้อหา = พื้นอ่อน) · ฟอนต์จาก `font_policy.py` (ไม่มีชื่อฟอนต์ในสคริปต์)

## สิ่งที่ยังไม่บังคับ และข้อจำกัดที่รู้แล้ว

- **ด่านก่อนสร้างยังไม่บังคับ `ICE_TEMPLATE`** — โค้ดของด่าน E เขียนไว้เป็นคอมเมนต์ใน `~/.claude/hooks/ice-prebuild-guard.sh` พร้อมวิธีเปิด (ลบ `#E` หน้าสามบรรทัด) รอ user อนุมัติแม่แบบก่อน · เมื่อเปิดแล้ว งานที่ใช้แม่แบบของลูกค้าประกาศ `ICE_TEMPLATE=<path แม่แบบลูกค้า>` และงานที่ตั้งใจไม่ใช้แม่แบบประกาศ `ICE_TEMPLATE=none` พร้อมเหตุผลใน spec
- **น้ำหนักตัวอักษร:** หัวเรื่องใช้ `b="1"` (น้ำหนัก Bold ของฟอนต์ราง) เพราะตัวตรวจฟอนต์เทียบชื่อตระกูลแบบตรงตัว การเรียกน้ำหนัก SemiBold ต้องใช้ชื่อตระกูล "IBM Plex Sans Thai Looped SemiBold" ซึ่งจะถูกนับเป็นฟอนต์นอกราง — ถ้า user ต้องการ SemiBold ตามคำแนะนำ D3 ต้องเพิ่มชื่อนั้นในรายการที่อนุมัติของ `font_policy.py` ก่อน
- **ฟอนต์ยังไม่ถูกฝังในไฟล์แม่แบบ** — การฝังทำที่ขั้นส่งมอบด้วย `embed_fonts_pptx.py` (วิธี B ของ D4) เหมือนเดิม แม่แบบเพียงประกาศชื่อฟอนต์ใน theme และทุก placeholder
- **ตัวตรวจเลย์เอาต์ `audit_layout.py` มองเห็นเฉพาะรูปทรงบนสไลด์ ไม่เห็นของ layout/master** — โลโก้และเส้นตกแต่งไม่ถูกนับเป็นภาพ หน้า `cover` `divider` `closing` จึงต้องมีข้อความไม่เกิน 12 คำ มิฉะนั้นจะถูกนับเป็นหน้าเนื้อหาที่ไม่มีภาพ (deck ตัวอย่างผ่านเพราะคุมคำไว้) — ควรปรับตัวตรวจให้ยกเว้น layout สามชื่อนี้ในรอบถัดไป
- **icon จาก SVG:** แปลงด้วย `qlmanage` ของ macOS แล้วทำพื้นโปร่งใสด้วย Pillow (เครื่องนี้ไม่มี `rsvg-convert` และ `cairosvg` ใช้ไม่ได้เพราะไม่มี libcairo — วิธีติดตั้งอยู่ใน `../icons/INDEX.md`) · ภาพที่ได้เป็นบิตแมป 512 px ขยายใหญ่มากอาจเห็นขอบหยาบ
- **การเปิดใน PowerPoint จริง** ยังไม่ได้ทำในรอบนี้ (ตรวจด้วย validator โครงสร้าง + LibreOffice ตัวจริงแปลง PDF ผ่าน) — ตามวินัย D4 ผู้ตรวจคุณภาพต้องเปิดใน PowerPoint จริงก่อนส่งลูกค้า
- ตาราง (`table`) ใช้รูปแบบตารางค่าเริ่มต้นของ PowerPoint ที่ผูกกับสี accent1 (navy) — ยังไม่มีรูปแบบตารางเฉพาะของ iCE ในแม่แบบ
