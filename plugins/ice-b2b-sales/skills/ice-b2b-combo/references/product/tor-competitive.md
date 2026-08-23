# TOR Competitive Playbook — Oracle Fusion ⇄ NetSuite (dual-angle)

> กลั่นจาก TOR Competitive KB ภายในของ iCE (171 record-views · verified 2026-06-29) — ใช้เมื่องานเป็น
> **ตั้งสเปก TOR / ตอบ TOR / เทียบ Fusion vs NetSuite (vs SAP)**. ไฟล์นี้เป็นฉบับ portable:
> ถือ **วิธีคิด + ธีมอาวุธหลัก** — ถ้อยคำ TOR รายข้อฉบับเต็มอยู่ในคลังภายใน (เครื่อง iCE:
> `oracle-cloud-applications-consulting` และ `oracle-netsuite-consulting` → `references/tor-competitive-kb/`).
> **INTERNAL** — สิ่งที่ถึงลูกค้าได้มีเพียงถ้อยคำ TOR แบบ outcome-based ที่ derive แล้วเท่านั้น.

---

## 1. หลักคิด dual-angle (ใช้ requirement ID ชุดเดียวกัน 2 มุม)

- **มุม Fusion (ขาย Fusion):** ชี้จุดที่ Fusion เหนือจริง → แปลงเป็นถ้อยคำ TOR ที่ข้อเสนอฐาน NetSuite ตอบได้แค่ Partial/No.
- **มุม NetSuite (ขาย NetSuite):** requirement ID เดียวกัน → วิธี **rebut/ปิด gap** (add-on cover, over-spec argument, fairness challenge).
- เลือกมุมตาม product ที่กำลังขาย (Context Gate Q2) — ห้ามใช้สองมุมพร้อมกันในเอกสารเดียว.

## 2. กติกาถ่วงดุล (ห้ามละเมิด — ติดทุก record ของ KB ต้นทาง)

1. **Add-on cover:** "gap" จำนวนมากปิดได้ด้วย first-party module ของ NetSuite ที่ใช้ engine Oracle เดียวกัน
   (NSPB=EPBCS · NS Account Reconciliation=Fusion EPM · NSAW=ADW+Analytics · NSPCM=costing) —
   ตัดสิทธิ์ NetSuite ด้วยเกณฑ์ที่ Fusion เองก็คิดเงินแยก module = ไม่แฟร์ เป็นคำถาม TCO ไม่ใช่ capability gap.
2. **Over-spec:** ความสามารถระดับ plant-grade/multi-country (APS, S&OP/IBP, global payroll, TMS, MDM, EAM)
   มักไม่เกี่ยวกับผู้ซื้อ single-entity ไทย — บังคับใน TOR = อ่านออกว่า spec-lock.
3. **Procurement fairness:** ล็อก TOR ด้วยชื่อ feature เฉพาะผลิตภัณฑ์ เสี่ยงถูกท้วง (แนว สตง.) และถูกคู่แข่ง
   challenge — เขียนเป็น **outcome-based** ผูก mission จริงของผู้ซื้อเสมอ.
4. **Anonymization:** ห้ามอ้างชื่อลูกค้าต้นเรื่อง — ใช้ industry pattern เท่านั้น.

## 3. ธีมอาวุธหลัก (สูง/High — ยิงได้จริง มี citation ฝั่ง KB)

| ธีม | Fusion ชนะตรงไหน | มุม NetSuite rebut |
|---|---|---|
| **SoD / GRC อัตโนมัติ** (NF-SEC-01 · GP-FUNC-27 · GP-TECH-11) | Risk Management Cloud: SoD rule engine + access certification ในตัว | กำหนด role design + compensating control · ถาม: ผู้ซื้อมี GRC maturity ถึงระดับใช้จริงไหม (over-spec สำหรับองค์กรเล็ก) |
| **Data residency / sovereign cloud** (NF-ARC-02 · GP-TECH-08 · GP-STANDOUT-09) | region เยอะ + sovereign/dedicated option | งาน SaaS ทั่วไป residency ไทยยังไม่ใช่ข้อบังคับตามกฎหมายส่วนใหญ่ — ตรวจ requirement จริงก่อน ไม่ใช่ยอมตาม spec-lock |
| **Process/GMP manufacturing + QMS/CAPA** (F-MFG-01 · GP-FUNC-01 · F-QM-01 · GP-FUNC-26) | recipe/batch genealogy/GMP + inspection/NCR/CAPA ลึกกว่า | ผู้ซื้อทำ discrete/เบา → over-spec · หรือปิดด้วย partner solution/SuiteApp — ประกาศ scope ตรงไปตรงมา |
| **Statutory tax / e-Tax Invoice TH** (GP-FUNC-16 · TOR-FIN-03) | tax engine + localization กว้าง | NetSuite ปิดด้วย TH localization SuiteApp ที่พิสูจน์แล้ว — แสดง reference ไทยจริง |
| **CLM (Contract Lifecycle)** (GP-FUNC-11) | Sourcing/CLM ครบวงจร | ถามว่า CLM เป็น mission-critical ของผู้ซื้อจริงไหม หรือใช้ระบบเฉพาะทางแยกก็ได้ |
| **Industry cloud depth** (GP-TECH-12) | industry solution เฉพาะทางลึกกว่า | vertical ไหนไม่มี record ใน KB — อย่า invent gap (กติกา H3) |

**Severity discipline:** ยิงเฉพาะ **สูง (High)** เป็น mandatory gate · ระดับ **แทบไม่มีผล** ใช้เป็นสีสัน/credibility
เท่านั้น — KB ต้นทางมี records ~1 ใน 3 ที่ caveat บอกเองว่า "อย่า spec-lock".

## 4. Workflow ตอนใช้ในงาน TOR/proposal

1. รู้ product ที่ขาย (Q2) + industry (Q4) → เลือกมุม + vertical.
2. เอาเฉพาะธีม High → เขียนเป็น **outcome-based requirement** (ผลลัพธ์ที่ผู้ซื้อต้องได้ ไม่ใช่ชื่อ feature).
3. ทุก claim ที่จะลง bid จริง → ตรวจกับ release ปัจจุบันก่อน (confidence ของ KB มีทั้ง high/medium/low —
   ต้อง verify ตัว low/medium เสมอ; portable context ที่ไม่มี KB เต็ม = flag `[to confirm]` ห้ามเดา).
4. อย่าลืมมุมกลับ: ทุกอาวุธที่เรายิงได้ คู่แข่งก็ยิงเรากลับด้วย ID เดียวกัน — เตรียม rebuttal ล่วงหน้า
   (ดู skill competitor-objection-bank ในเครื่อง iCE).

> เชื่อมโยง: `product/oracle-cloud.md` · `product/netsuite.md` · `domain/govt-egp.md` (fairness ภาครัฐ) ·
> `_capabilities/know.md` (FACT-gate ก่อนยืนยัน capability ใด ๆ).
