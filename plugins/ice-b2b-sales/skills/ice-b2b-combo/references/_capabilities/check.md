# Capability — CHECK (QA ก่อนส่ง · ชี้ปัญหา ไม่แก้เงียบ)

> ความสามารถ "ด่านคุณภาพ" — ตรวจ deliverable ก่อนถึงมือลูกค้า/ผู้บริหาร. บทบาทคือ **detector** —
> ชี้ปัญหา + หลักฐาน ไม่ตัดสินใจแก้แทน (ให้ผู้ใช้/ขั้นถัดไปตัดสิน). โหลดเมื่ออยู่ STEP 5.
> หัวใจ: 9-dimension · Speed-Tier · Producer≠Checker · Delta-ReQA · RATCHET.

---

## 1. Producer ≠ Checker (กฎพื้นฐาน)

คนที่สร้าง ≠ คนที่ตรวจ — ในอุดมคติให้ **ตรวจในมุมมอง/รอบที่แยกจากตอนสร้าง** เพื่อเลี่ยง confirmation bias
(คนเขียนมักมองข้ามที่ผิดของตัวเอง). ถ้าทำในสกิลเดียว → เข้าโหมด CHECK แบบ "อ่านงานคนอื่น" จริง ๆ ไม่เข้าข้างงานที่เพิ่งสร้าง.

---

## 2. Speed-Tier (เลือกความเข้มตามความเสี่ยง)

| Tier | ใช้เมื่อ | ตรวจอะไร |
|---|---|---|
| **DRAFT** | ร่างภายใน ดูเล่น ๆ | ข้าม QA |
| **FAST** | งานเร็ว ความเสี่ยงต่ำ | 3 มิติที่พังเห็นทันที: Completeness · Anti-Hallucination · Font/Layout |
| **FULL** | ส่งลูกค้า/ผู้บริหาร | ครบ 9 มิติ |

**RATCHET:** ถ้าเป็น **final ส่งจริง** → บังคับ **FULL เสมอ** ไม่ว่าก่อนหน้าจะทำ tier ไหน (กันร่างหลุดเป็นของจริง).
- **เมื่อเลื่อน FAST → Submit:** ต้อง **ตรวจ D5 (Anti-AI) เพิ่ม** เพราะ FAST ไม่ได้ตรวจ D5 (กันข้อความ AI หลุดถึงลูกค้าผ่านทาง ratchet). ตรวจ D5 ไม่ได้ = ลด confidence + flag.

---

## 3. 9 Dimensions (FULL)

| D | มิติ | ตรวจอะไร · เกณฑ์ตก |
|---|---|---|
| **D1** | Requirement Alignment | ตอบโจทย์/TOR ที่ขอจริงไหม |
| **D2** | Completeness | ครบทุกหัวข้อที่ควรมี · ไม่มีช่องว่าง/placeholder ค้าง |
| **D3** | Consistency + Anti-Hallucination | ตัวเลข/ชื่อ/วันที่ตรงกันทั้งเอกสาร + มี source (เทียบ Context-Lock) · กุข้อมูล = ตก |
| **D4** | Logical Flow | เรียงเหตุผลต่อเนื่อง · MECE · ไม่ขัดแย้งในตัว |
| **D5** | **Anti-AI** | ภาษาไม่เป็น AI-cadence (ดู §4) — customer-facing ที่หลุดเยอะ = ตก |
| **D6** | Brand Compliance | ไม่อ้างชื่อบริษัทที่ปรึกษา/methodology ที่ห้าม · ตรง CI |
| **D7** | **Font/Layout** | tri-slot ไทยครบ · ไม่ทับ · ไม่ล้น · ฝังฟอนต์ — **hard-block ถ้า customer-facing** |
| **D8** | Wording Discipline | positive 70/25/5 (ดูนิยามล่าง) · เหมาะ stage (discovery=neutral, proposal=positive) |
| **D9** | Compliance / TOR | เทียบ TOR ทีละข้อ: COMPLY/PARTIAL/MISSING/EXTRA/DEVIATION · comply% ตรงจริง |
| **D10** | **Deal-Quality** | (สำหรับงานขาย — ไม่ใช่แค่เอกสารสวย) ดีลจะปิดได้ไหม (ดูล่าง) |

**D10 — Deal-Quality (ตรวจความแข็งของดีล ไม่ใช่แค่เอกสาร):**
QA ที่ดีต้องถามว่า "ดีลนี้จะปิดได้จริงไหม" ไม่ใช่แค่ "เอกสารตรง TOR ไหม". เช็ค:
- **Buyer clarity** — รู้ Economic Buyer จริงไหม (ไม่ใช่เดา)? (ดู `_shared/meddpicc.md`)
- **Compelling event** — มี Why Now จริงไหม หรือแค่ nice-to-have? (ดู `_shared/why-stack.md`)
- **Value proof** — ตัวเลข value มีที่มาไหม หรือกุ? (ดู `know.md` FACT-gate)
- **Differentiation** — ผ่าน remove-name test ไหม (เอาชื่อเราออก คู่แข่งใส่แทนได้ = ไม่ต่าง)?
- **Risk-to-close** — readiness (infra/people/process) พร้อมไหม? competitive trap? proof gap?
- **Next-step ownership** — มี next step ชัด + ใครรับผิดชอบ?
🔴 หลายข้อ = ดีลอ่อน → flag ให้ผู้ใช้รู้ก่อนทุ่มทำ proposal (ไม่ใช่ปล่อยให้เอกสารสวยแต่ดีลตาย).

**ผลตรวจ = ชี้เป้า + หลักฐาน + before/after** ไม่แก้เงียบ ๆ:
```
[D7 · slide 4] ฟอนต์ไทยหัวข้อตกเป็น Calibri (ไม่มี <a:cs>) — customer-facing → BLOCK
   หลักฐาน: run "ระบบบริหารงบประมาณ" ใช้ latin-only
   แนะนำ: set cs = Sarabun, size 24pt
```

### D8 — นิยาม positive 70/25/5 (wording balance)

สัดส่วนภาษาในเอกสารลูกค้า (โดยเฉพาะ proposal):
- **70% positive** — ประโยชน์, ผลลัพธ์, ความสามารถที่ได้.
- **25% neutral / trade-off** — ต้นทุน, timeline, effort ตามจริง (honest ไม่ปิดบัง).
- **5% honest risk** — ความเสี่ยง/ข้อจำกัด/dependency ที่ต้องรู้.

> ตัวอย่าง: "NetSuite OneWorld รองรับโครงสร้าง multi-subsidiary (70%) ใช้เวลา implement ~6 เดือน (25%)
> และต้อง redesign chart-of-accounts ก่อน (5%)". — บวกเป็นหลัก แต่ไม่ขายฝัน (discovery=neutral มากขึ้น · escalation=honest นำ).

---

## 4. D5 Anti-AI — ชี้ไปแหล่งเดียว (ไม่ทำซ้ำในสกิลนี้)

การตรวจภาษา AI (สำนวนซ้ำ ๆ ที่ฟ้องว่า AI เขียน) ให้ **ใช้สกิลตรวจ-AI ที่มีในสภาพแวดล้อม** (เช่น สกิลตระกูล
AI-detection สำหรับ TH+EN) — **ไม่คัดลอก pattern มาไว้ที่นี่** เพื่อให้มี source of truth ที่เดียว ไม่ขัดกันเวลาแก้.

สัญญาณคร่าว ๆ ที่ต้องเอะใจ (แล้วไปตรวจเต็มที่แหล่งนั้น):
- ไทย: "เป็นที่ทราบกันดี", "ปฏิเสธไม่ได้ว่า", "เป็นเรื่องธรรมชาติที่…", ประโยคยาวสม่ำเสมอเกินไป.
- อังกฤษ: delve, leverage, robust, seamless, "It's worth noting that…".
- สถิติ: ความยาวประโยคสม่ำเสมอ (burstiness ต่ำ) = ฟ้อง AI.

**Fallback เมื่อไม่มีสกิลตรวจ-AI ในสภาพแวดล้อม (portable):** ไม่ block — ทำ manual self-check แทน:
1. สุ่ม 3 ย่อหน้า → ดู burstiness (ประโยคสั้น-ยาวสลับไหม หรือยาวเท่ากันหมด) + สำนวนซ้ำข้างบน.
2. customer-facing → ถ้าตรวจเต็มไม่ได้ = **ลด confidence + flag "ควรให้คนตรวจภาษา"** (ไม่อ้างว่าผ่าน D5).
3. ระวัง false-positive: ภาษาราชการ/ทางการไทยที่สุภาพ ≠ AI เสมอ — ดู pattern ซ้ำ ไม่ใช่แค่ความเป็นทางการ.

---

## 5. Delta Re-QA (รอบที่ 2+ ไม่ต้องตรวจซ้ำหมด)

ถ้าตรวจรอบแรกแล้วแก้ตามแล้วส่งกลับมา:
- ตรวจ **เฉพาะจุดที่แก้** (delta) + spot-check ข้างเคียงว่าการแก้ไม่ทำพังที่อื่น.
- **ไม่ re-scan ทั้งเอกสาร** ทุกรอบ (เปลือง) — **ยกเว้น** is_final=true → FULL re-scan ครั้งสุดท้าย.

---

## 6. หลัก DETECTOR not DECIDER

- CHECK **ชี้** ว่าอะไรผิด + ทำไม + แนะแนวแก้ — แต่ **ไม่ตัดสินใจแก้แทน** ในเรื่องที่เป็น business judgment
  (เช่น "ราคานี้ต่ำไป" = ชี้ได้ว่าต่ำกว่า benchmark แต่ผู้ใช้ตัดสินว่าจะปรับไหม).
- เรื่อง technical พังชัด (ฟอนต์ตก/ไฟล์ corrupt/ตัวเลขไม่ลงตัว) → **recommend แก้แน่นอน** + customer-facing = block.
- เรื่องก้ำกึ่ง → flag + ให้ผู้ใช้ revalidate (ไม่บังคับ).
