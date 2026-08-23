# Decision Matrix — เลือก chain เมื่อ deliverable กำกวม

> เปิดไฟล์นี้ **เฉพาะเมื่อ** 4 คำถามใน SKILL.md STEP 1 ตอบไม่ชัดใน 1 นาที. แต่ละ section จบด้วยการ assign chain.
> หลักการ: **Deliverable-First** — ถาม "ผลิตอะไร" ก่อน "product อะไร" (product เดียวกันต้องใช้ chain ต่างกัน
> สำหรับ TOR Response vs Board Paper vs Change Request).

---

## ลำดับอ่านเมื่อรีบ

1. ตัดสิน **deliverable type** (Section 1) — นี่คือ 80% ของการ route.
2. เพิ่ม **product** — narrow ไปไฟล์ product ที่ใช่.
3. เพิ่ม **domain** — GFMIS / e-GP / e-Tax / FinTech ถ้าเกี่ยว.
4. เช็ค **stop rule** — chain ไม่เกิน 5 ไฟล์.

---

## Section 1 — Deliverable → Chain

| Deliverable | Path | Chain (lazy-load) |
|---|---|---|
| **Proposal / ข้อเสนอ** | Pre-sales | strategic-thinking → solution-selling → product/<x> → domain/<y> → [BUILD-SPEC] |
| **RFP / TOR Response** | Pre-sales | solution-selling → product/<x> → domain/govt-egp (ถ้ารัฐ) → [BUILD-SPEC + CHECK D9] |
| **Business Case** | Pre-sales | solution-selling → why-thinking → product/<x> → [_shared/why-stack, frameworks] |
| **Demo Script / Design** | Pre-sales | design-thinking → product/<x> |
| **Board Paper / Exec Brief** | Strategic | strategic-thinking → why-thinking → [_shared/frameworks Pyramid] |
| **Account Plan / Win Plan** | Strategic | strategic-thinking → relationship-management → product/<x> (ถ้าเจาะ) |
| **Competitive Battle Card** | Strategic | strategic-thinking → product/<x> (Primary-Lock + เทียบ) |
| **QBR / EBR / Renewal** | Strategic | relationship-management → questioning |
| **Discovery Prep** | Fast | questioning |
| **Sales Email / Meeting Summary** | Fast | questioning OR relationship-management (ไฟล์เดียว) |
| **Pricing** | Pre-sales | solution-selling → product/<x> → domain/th-etax (ถ้าไทย) |
| **Deep Q&A / เทียบ product** (ไม่มีไฟล์ส่ง) | Strategic/Fast | strategic-thinking → product/<x> (Primary-Lock) — **จบที่ STEP 3 ไม่ผ่าน BUILD-SPEC/CHECK** |

### Commercial-Execution artifacts (งานขายจริง ไม่ใช่แค่เอกสาร — first-class route)

งานเหล่านี้เป็น **deal-execution** ไม่ใช่ document-generation — route ตรง ไม่รวมใน "strategic" รวม ๆ:

| งาน | chain |
|---|---|
| **Mutual Action Plan / Close Plan** | solution-selling → `_shared/meddpicc.md` (Decision Process) → relationship-management |
| **Stakeholder / Power Map** | relationship-management (power vs interest) → `_shared/meddpicc.md` |
| **Procurement / TOR strategy** | solution-selling → `domain/govt-egp.md` (ภาครัฐ) → `_shared/meddpicc.md` (Paper Process) |
| **Objection Handling** | solution-selling (reframe) → product/<x> (counter ด้วย fact) |
| **Negotiation give/get** | strategic-thinking → solution-selling → Anti-Loop (trade-off) |
| **Implementation Handover** | solution-selling §9 (win brief sell→deliver) |

> งานพวกนี้มัก **ไม่มีไฟล์ส่ง** (เป็น plan/strategy) → จบที่ STEP 3 หรือออกเป็น internal artifact. แต่คือหัวใจของ "ปิดดีลได้จริง".

---

## Section 2 — Product layer

| สัญญาณ | โหลด |
|---|---|
| Oracle Fusion / Cloud ERP/EPM/OCI | `product/oracle-cloud.md` |
| Oracle EBS R12/11i (legacy) | `product/oracle-ebs.md` |
| NetSuite (core) | `product/netsuite.md` |
| NetSuite + ลูกค้าไทย/APAC | `product/netsuite.md` + `product/netsuite-thailand.md` |

---

## Section 3 — Domain overlay

| สัญญาณ | โหลด |
|---|---|
| ภาครัฐไทย / GFMIS / งบประมาณ | `domain/govt-gfmis.md` |
| จัดซื้อจัดจ้างภาครัฐ / e-GP / TOR | `domain/govt-egp.md` |
| ภาษีไทย / e-Tax / VAT / WHT / localization | `domain/th-etax.md` |
| FinTech / lending / NPL / IFRS9 | `domain/fintech.md` |

---

## Section 4 — Stop Rules

- **chain ≤ 5 ไฟล์** — เกิน = งานกว้างไป → ถามผู้ใช้ว่าโฟกัสส่วนไหนก่อน.
- **ลงทาง ไม่ออกข้าง** — เลือก chain แล้วทำให้จบ อย่าสลับ skill กลางคัน (จบก่อน แล้วค่อย revise).
- **Pre-sales = default** — ไม่แน่ใจ ให้ถือเป็น Pre-sales (workload จริงส่วนใหญ่เป็น pre-sales).
- **มี deliverable file → ผ่าน BUILD-SPEC (STEP 4) + CHECK (STEP 5) เสมอ.**
