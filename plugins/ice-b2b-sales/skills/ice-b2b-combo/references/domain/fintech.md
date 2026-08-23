# Domain — FinTech / Lending / IFRS9

> overlay ความรู้สำหรับงานขายภาคการเงิน: lending, NPL/NPA, IFRS9 ECL, risk. ใช้เมื่อลูกค้าเป็น bank/NBFI/lending/AMC.
> ใช้ช่วง Solution → Proposal (vertical ลึก). ทุกข้ออ้างกฎ/อัตรา → ตรวจแหล่งทางการ (ดู `_capabilities/know.md`).

---

## 1. Lending + Loan Origination (LOS)

- **B2C:** consumer/personal loan, credit card, mortgage, auto.
- **B2B:** commercial lending, trade finance, supply chain finance, working capital.
- **LOS:** digitize end-to-end · credit decisioning · workflow automation.
- **Credit scoring:** traditional scorecard · ML-based · alternative data.

## 2. NPL / NPA / Distressed Asset

- **NPL/NPA management:** portfolio acquisition, valuation, collection, workout.
- **AMC operations:** debt recovery, legal process, auction.
- **portfolio analytics:** segmentation, recovery forecasting, collection optimization.

## 3. IFRS9 + ECL Engine (หัวใจ regulatory)

- **ECL (Expected Credit Loss)** 3 stage: performing (12-month ECL) → underperforming (lifetime) → impaired (lifetime + credit-impaired).
- **PD/LGD/EAD** modeling · staging criteria · SICR (significant increase in credit risk).
- **forward-looking** macro overlay · scenario weighting.
- ERP/risk system ต้องรองรับ ECL calculation + provisioning + reporting.

## 4. Risk Management

- credit risk · market risk · operational risk · liquidity.
- regulatory reporting (BOT — Bank of Thailand) · stress testing.

---

## Why Now (FinTech triggers — Thailand)

> reviewer feedback: Why-Now ของ FinTech ต่างจาก generic. trigger จริง:

- **IFRS9 / TFRS 9 compliance** — provisioning ที่ถูกต้อง = regulatory deadline.
- **BOT regulation** — รายงาน, capital adequacy, stress test.
- **NPL surge** — เศรษฐกิจ → NPL เพิ่ม → ต้องระบบ collection/workout.
- **digital lending competition** — neo-bank/digital lender กดดัน traditional.
- **AML/KYC** — regulatory tightening.

---

## Business case (FinTech)

- value = provisioning accuracy + regulatory compliance + collection efficiency + risk reduction.
- ตัวเลข ECL/recovery rate = ต้องมาจากลูกค้า (ดู `_capabilities/know.md` FACT-gate) — **กุไม่ได้เด็ดขาด** (regulatory sensitive).
- positioning: ดู `method/solution-selling.md` + `_shared/why-stack.md`.

---

## ข้อควรระวัง

- regulatory เปลี่ยนบ่อย (BOT, สรรพากร) → ตรวจสด (ดู `_capabilities/know.md` staleness).
- ECL methodology = technical สูง → fit-gap ลึกต้องระวัง over-commit.
- ผูกภาษีไทย → `domain/th-etax.md` · ERP core → `product/*`.

> vertical นี้ลึก — ตัวเลข/regulatory ต้องแม่น ห้ามเดา.
