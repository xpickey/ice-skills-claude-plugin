# QA — Pre-Flight Checklist (ก่อนสร้าง/ส่ง deliverable)

> checklist บังคับก่อนสร้างหรือส่ง deck/เอกสาร — กันงาน "เนื้อถูกแต่ดีไซน์พัง/ซ้ำซาก". ใช้ STEP 4-5.
> คู่กับ `_capabilities/build-spec.md` (สร้าง) + `_capabilities/check.md` (ตรวจ 9-dim).

---

## ทำไมต้องมี (5 failure mode ที่กันได้)

deck มัก fail ฝั่ง visual แม้เนื้อถูก เพราะ:
1. อ่าน instruction แต่ข้าม reference design.
2. default "shape พื้นฐาน" ไม่พิจารณาวิธีอื่น.
3. ใช้ layout pattern เดียวซ้ำทั้ง deck.
4. ใช้ placeholder data แทนตัวอย่างจริง.
5. ข้าม icon/สี/big-number callout.

**วิธีกัน:** บังคับ "ประกาศแผนก่อนสร้าง".

---

## Pre-Build Declaration (ประกาศก่อนสร้าง)

ก่อนสร้าง deck — ระบุให้ครบ:
- [ ] **deck type** + ผู้ฟัง + objective (proposal/board/demo/training)
- [ ] **theme/CI** — สีตาม brand ลูกค้า (ดู `_capabilities/build-spec.md`)
- [ ] **font strategy** — TH-only / EN-only / TH+EN → เลือก font ตามภาษา (D1-D4)
- [ ] **layout variation** — ไม่ใช้ pattern เดียวซ้ำ · วาง ≥3 archetype
- [ ] **ข้อมูลจริง** — จาก Context-Lock (ดู `_capabilities/route.md`) ไม่ใช่ placeholder
- [ ] **icon/สี/callout** — มี visual hierarchy ไม่ใช่ text ล้วน

---

## Pre-Send Checklist (ก่อนส่ง)

เดินผ่าน 9-dimension (ดู `_capabilities/check.md`) — Speed-Tier ตามความเสี่ยง:
- [ ] **D2 Completeness** — ครบทุกหัวข้อ · ไม่มี placeholder ค้าง
- [ ] **D3 Anti-Hallucination** — ตัวเลข/ชื่อ/วันที่ตรงกัน + มีที่มา (เทียบ Context-Lock)
- [ ] **D5 Anti-AI** — ภาษาไม่เป็น AI-cadence (ดู `_capabilities/check.md` §4)
- [ ] **D7 Font/Layout** — tri-slot ไทยครบ · ไม่ทับ · ไม่ล้น · ฝังฟอนต์ → **customer-facing + พัง = BLOCK**
- [ ] **D8 Wording** — positive 70/25/5 · เหมาะ stage
- [ ] **D9 Compliance** — ถ้าตอบ TOR: เทียบทีละข้อ comply% จริง

---

## Font/Layout hard-block (เน้นย้ำ — ฟอนต์ไทยพังบ่อยสุด)

customer-facing + ละเมิดข้อใดข้อหนึ่ง = **ห้ามส่ง**:
- ฟอนต์ไทยตกเป็น Calibri (ไม่มี `<a:cs>`)
- ฟอนต์ไม่ฝัง (เครื่องปลายทางเพี้ยน)
- object ทับ / เนื้อล้นกรอบ
- `→` (U+2192) ในไฟล์ (PowerPoint-Mac reject) → แทน `▸`

> รายละเอียด → `_capabilities/build-spec.md` (D1-D4 + 18 lessons) · `_capabilities/check.md` (9-dim เต็ม).

---

## Producer ≠ Checker

ตรวจในมุม "อ่านงานคนอื่น" — ไม่เข้าข้างงานที่เพิ่งสร้าง (ดู `_capabilities/check.md`).
final ส่งจริง = ตรวจ FULL เสมอ (RATCHET).
