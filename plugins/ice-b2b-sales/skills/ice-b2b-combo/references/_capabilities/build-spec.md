# Capability — BUILD-SPEC (ออกข้อกำหนดเอกสาร ไม่สร้างเอง)

> ความสามารถ "วินัยการสร้างเอกสาร" — เมื่อมี deliverable (.pptx/.docx/.xlsx) สกิลนี้ **ออก spec ละเอียดให้
> เครื่องมือสร้างเอกสารใด ๆ ทำตาม** (portable — ไม่ผูก builder ตัวใดตัวหนึ่ง · ไม่รัน build ในสกิลนี้).
> โหลดเมื่ออยู่ STEP 4. หัวใจ: Font D1-D4 · 18 build-lessons · Build-vs-Edit · Preview-First.

---

## 1. Font Discipline D1-D4 (แก้ปัญหาฟอนต์ไทย+อังกฤษที่ยากสุด)

ปัญหาคลาสสิก: ฟอนต์ไทยตกเป็น default, ไทยกับอังกฤษไม่เข้ากัน, ไฟล์เปิดไม่ขึ้น. spec ต้องสั่ง:

**D1 — Tri-slot binding:** ทุก text run ต้อง set 3 slot:
```
<a:latin>  → ฟอนต์อังกฤษ
<a:ea>     → East-Asian
<a:cs>     → Complex-Script (ไทยใช้ slot นี้)
```
ถ้าไทยไม่มี `<a:cs>` → ตกเป็น Calibri = ผิด.

**D2 — Normalization:** รวม variant ฟอนต์ให้เหลือ **≤12 ตระกูล** ที่อนุมัติ. map ชื่อ variant เข้าตัวหลัก
(THSarabunPSK → **TH Sarabun New** — ตัว maintained; ไม่ใช้ PSK).

**D3 — Optical size (นโยบาย 2026.07.31 — พิสูจน์ด้วย PDF จริง 45 ฉบับ + วัด metric 9 ตระกูล):**
- **ค่าเริ่มต้น = SINGLE-FAMILY:** ฟอนต์ตระกูลเดียวคุมทั้งไทย+อังกฤษ ขนาด**เท่ากัน ห้ามบวก** —
  ตำนาน "ไทยต้อง +2pt" วัดจริงต่างแค่ ~2% (cap height 0.700 vs 0.714 em) บวกแล้วไทย**ใหญ่เกิน**.
- **ฟอนต์มาตรฐาน:** งานเอกชน = **IBM Plex Sans Thai Looped** (ต้อง Looped — cut ไม่มีหัวเป็นโทน display
  ผิด register เอกสารทางการ) · งานราชการ = **TH Sarabun New 16pt** (มติ ครม. 2553 ผูกพันส่วนราชการ
  ไม่ผูกพันผู้ขาย — ใช้เพื่อเข้ากับ register ผู้อ่าน).
- **จับคู่ 2 ตระกูลเฉพาะเมื่อลูกค้าบังคับ Latin brand font** → ชดเชยขนาดด้วยสูตร cap-ratio ไม่ใช่บวกตายตัว.
- ไทย body **≥18pt** (deck), heading **≥24pt** · line-height ไทย ≥1.8 (สระบน-ล่างต้องการที่หายใจ).

**D4 — No-overlap + Embed:** object ไม่ทับกัน (เช็ค bbox) · เนื้อหาไม่ล้นกรอบ 16:9 · **ฝังฟอนต์ในไฟล์**
(embeddedFontLst หลัง notesSz, content-type ถูก, fontTools normalize) — ไม่งั้นเครื่องปลายทางไม่มีฟอนต์ = เพี้ยน.

**เลือกฟอนต์ตามภาษา ไม่ตาม template:**
- ไทยล้วน / ไทย+อังกฤษปน → **ตระกูลเดียวคุมทั้ง deck** (IBM Plex Sans Thai Looped หรือ TH Sarabun New ตาม register) —
  ใส่ชื่อเดียวกันทั้ง slot latin และ cs, ขนาดเท่ากัน.
- อังกฤษล้วน → ฟอนต์ latin ได้อิสระกว่า.
- ลูกค้าบังคับ Latin brand font → ค่อยจับคู่ latin + cs แล้วชดเชย cap-ratio.
- สี → ปรับตาม CI/color pattern ของลูกค้าได้ (font เลือกตามภาษา, สีเลือกตาม brand).

---

## 2. Build-Lessons สำคัญ (กันไฟล์พัง — ใส่ใน spec ให้ tool ทำตาม)

| # | ปัญหา | spec ที่สั่ง |
|---|---|---|
| L1 | `→` (U+2192) ทำ PowerPoint-Mac reject ทั้งไฟล์ | แทนด้วย `▸` (U+25B8) ทุกที่ · scan ก่อนส่ง |
| L2 | เปลี่ยน preset shape แล้ว avLst เก่าค้าง → Repair | ล้าง `<a:avLst>` ทุกครั้งที่เปลี่ยน prstGeom |
| L3 | ย่อหน้าไม่มี endParaRPr → text run ว่าง corrupt | ทุก `<a:p>` ต้องมี endParaRPr |
| L4 | sldSz มี type attribute → 16:9 เพี้ยน | strip type, ใช้ 12192000×6858000 EMU |
| L5 | qlmanage/LibreOffice ขึ้นเขียวลวง | ยืนยันด้วยการเปิดใน PowerPoint จริงเท่านั้น |

> รายการเต็ม 18 บทเรียน — ใส่เป็น checklist ให้ builder validate ก่อนคืนไฟล์.

---

## 3. Build-vs-Edit Guard (เลือกวิธีให้ถูก)

- **เอกสารใหม่ หรือแก้ > 5 สไลด์/หน้า** → **สร้างใหม่ทั้งชุด** จาก spec (full pipeline).
- **แก้ ≤ 5 สไลด์** (typo/ตัวเลข/คำ) บนไฟล์ที่ valid อยู่แล้ว → **แก้ในไฟล์เดิม** (ไม่ rebuild —
  การ rebuild เสี่ยง re-introduce ปัญหา text-run ว่าง).

เหตุผล: rebuild ทั้งไฟล์เพื่อแก้คำเดียว = เสี่ยงพังเปล่า ๆ.

---

## 4. Preview-First (กันสร้างผิดแนว เสียเวลา)

เมื่อ infographic/layout มีได้หลายแนว (decision-tree vs matrix vs funnel vs timeline):
1. **เสนอ 2-3 แนว** พร้อมอธิบายสั้น ๆ ว่าแต่ละแนวเหมาะกับอะไร (preview ก่อน — ไม่สร้างเต็ม).
2. ผู้ใช้เลือก 1.
3. สร้างเต็มเฉพาะแนวที่เลือก.

**Adaptive Mix:** ถ้าอิง template — เอา *แนว/ลักษณะ* ของ template มา แต่สร้าง object **เท่าจำนวนเนื้อจริง**
(ข้อมูล 3 ข้อ = 3 กล่อง ไม่ใช่ยัดให้ครบ 5 ช่องตาม template หรือเหลือช่องว่าง). ลด/เพิ่ม object ให้พอดีเนื้อ.

---

## 5. รูปแบบ spec ที่ส่งให้ builder

```yaml
deliverable_spec:
  type: pptx | docx | xlsx
  language: TH | EN | bilingual
  theme: <ชื่อ theme / CI colors>
  fonts:
    latin: <ตระกูลเดียวกับ cs เว้นแต่ลูกค้าบังคับ brand font>
    cs: <IBM Plex Sans Thai Looped | TH Sarabun New>
    sizes: { body_th: 18, heading_th: 24, th_vs_en: "equal — single-family, no +pt" }
  structure:
    - slide/section: <หัวข้อ + เนื้อ (จาก Context-Lock — ตัวเลขชุดเดียว)>
  guards: [ tri-slot, normalize≤12, no-overlap, embed-fonts, arrow→▸, clear-avLst, endParaRPr ]
  build_mode: build-full | edit-in-place
  validation_required: [ open-in-real-PowerPoint, char-scan, bbox-check, font-embed-check ]
```

> สกิลนี้ออก spec นี้ → ส่งให้เครื่องมือสร้างเอกสารที่มีในสภาพแวดล้อมทำตาม. ไม่ build เอง = portable.
