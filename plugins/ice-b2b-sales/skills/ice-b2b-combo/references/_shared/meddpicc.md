# Shared — Qualification Scorecard (MEDDPICC)

> กรอบ qualify ดีลที่ใช้ร่วมหลายงาน (solution-selling, why-thinking, questioning). เก็บที่เดียว — reference อื่นชี้มา.
> ใช้ช่วง Discovery → Qualify → ตลอดดีล (re-score เมื่อข้อมูลเปลี่ยน).

---

## 8 องค์ประกอบ

| ตัว | คำถามหลัก | สิ่งที่ต้องได้ |
|---|---|---|
| **M** — Metrics | ลูกค้าวัดความสำเร็จด้วยตัวเลขอะไร | KPI/ROI ที่ลูกค้ายอมรับ (ไม่ใช่ที่เรากุ) — ระวัง vanity vs purpose (ดูล่าง) |
| **E** — Economic Buyer | ใครเซ็นอนุมัติงบจริง | ชื่อ/ตำแหน่ง + เข้าถึงได้ไหม |
| **D** — Decision Criteria | เกณฑ์ตัดสินเลือก vendor | technical + business + ความสัมพันธ์ |
| **D** — Decision Process | ขั้นตอนอนุมัติ + timeline | ใครเกี่ยวบ้าง · ขั้นไหน · เมื่อไหร่ |
| **P** — Paper Process | ขั้นตอนจัดซื้อ/กฎหมาย/สัญญา | (ภาครัฐไทย = สำคัญมาก — ดู domain) |
| **I** — Identify Pain | ความเจ็บปวดที่ทำให้ต้องเปลี่ยน | pain ที่วัดเป็นเงิน/ความเสี่ยงได้ |
| **C** — Champion | คนในที่เชียร์เรา + มีอิทธิพล | มี power จริงไหม · ทดสอบแล้วหรือยัง |
| **C** — Competition | คู่แข่ง + สถานะเทียบเรา | ใครนำ · จุดแข็ง/อ่อนเทียบ |

---

## วิธี score

ให้แต่ละตัว: **🟢 รู้ชัด+แข็ง / 🟡 รู้บางส่วน / 🔴 ไม่รู้/อ่อน**

- 🔴 หลายตัว = ดีลยังไม่ qualified → กลับไป discovery (อย่าเพิ่งทุ่มทำ proposal).
- **M + E + Champion** = 3 ตัวที่ขาดไม่ได้ — ไม่มีคนเซ็นงบ (E) หรือคนเชียร์ (Champion) หรือตัวชี้วัด (M) = เสี่ยงสูง.
- re-score ทุกครั้งที่ได้ข้อมูลใหม่ — MEDDPICC เป็น living scorecard ไม่ใช่ทำครั้งเดียว.

---

## กับดักที่พบบ่อย

- **สับสน Champion กับ Coach** — Coach ให้ข้อมูลแต่ไม่มี power · Champion มี power + เชียร์ + พร้อมสู้แทนเรา.
  **ทดสอบ power จริง:** ขอให้ champion ทำอะไรที่ต้องใช้อิทธิพล (จัดประชุม EB, ดัน agenda) — ถ้าทำไม่ได้ = Coach.
- **เดา Economic Buyer** — คิดว่า IT manager เซ็น แต่จริง ๆ CFO เซ็น → ต้องยืนยัน ไม่เดา.
- **Metrics ที่เรากุเอง** — ROI ต้องมาจากตัวเลขลูกค้า ไม่ใช่ benchmark ที่เราใส่เอง (ดู know.md FACT-gate).

---

## Metrics: Vanity vs Purpose (สำคัญมากกับลูกค้าไทย)

ผู้บริหารไทยมักอ้าง **vanity KPI** ที่ดูดีในสไลด์แต่ไม่กระทบ bonus/การประเมินจริง:

| Vanity (ดูดี ไม่กระทบจริง) | Purpose (กระทบ KPI ผู้บริหารจริง) |
|---|---|
| "ปิดงบเร็วขึ้น 50% (7→3 วัน)" | "board ตัดสินจ่ายปันผลเร็วขึ้น 2 สัปดาห์ เพราะข้อมูลเชื่อถือได้" |
| "ลดเวลา manual entry" | "ผ่าน audit สตง./ผู้สอบบัญชี ไม่มีข้อสังเกต" |

**วิธีขุด purpose:** ถาม "ทำไม metric นั้นสำคัญกับ**คุณ**" ซ้ำ 3 รอบ จน link ไปถึง KPI ที่นายของ Economic Buyer ใช้ประเมินเขา.
**คำถามทอง:** "ผู้บริหาร/board ใช้ตัวเลขอะไรประเมินงานของคุณ?" — นั่นคือ M จริง.

---

## Readiness Gate (เช็คก่อนข้าม Discovery — ดีลล่มเพราะข้อนี้บ่อย)

นอกจาก 8 องค์ประกอบ — ก่อนทุ่มทำ proposal เช็ค **ความพร้อม 3 ด้าน**:

| ด้าน | เช็คอะไร | 🔴 = เสี่ยง |
|---|---|---|
| **Infrastructure** | DB/cloud readiness · integration · ระบบเดิมพร้อมเชื่อมไหม | infra ไม่พร้อม = go-live ล่ม |
| **People** | change management · org พร้อมเปลี่ยนไหม · มี sponsor จริง | คนต้าน = adoption ตก |
| **Process** | กระบวนการชัดไหม · maturity พอ implement ไหม | process มั่ว = scope creep |

🔴 ด้านใด → flag เป็นความเสี่ยง + คุยกับลูกค้าก่อน commit timeline. ดีลที่ซื้อแล้วแต่ infra/คน/process ไม่พร้อม = ล่มตอน delivery.

> ภาครัฐไทย: Paper Process + Decision Process ผูกกับระเบียบจัดซื้อ — ดู `references/domain/govt-egp.md`
