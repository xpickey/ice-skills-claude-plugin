# Reference Index — แผนที่ reference ทั้งหมด (โหลดตัวไหนเมื่อไหร่)

> ดัชนีของทุก reference ในสกิลนี้ + เมื่อไหร่ควรเปิด. ใช้เป็น lookup ตอน STEP 2 (lazy-load).
> หลักการ: เปิดเฉพาะที่งานต้องการ — ไม่อ่านทั้งหมด.

---

## Capabilities (4 หมวก + วินัย context) — เปิดตามขั้นของ pipeline

| ไฟล์ | เปิดเมื่อ | ให้อะไร |
|---|---|---|
| `_capabilities/route.md` | STEP 0-1 | Context-Lock · Mode · 4Q routing · Validation Gates · Anti-Loop · Positive wording |
| `_capabilities/know.md` | STEP 3 | FACT/PATTERN/ASSUMPTION gate · Primary-Lock · Confidence · Retrieval discipline |
| `_capabilities/build-spec.md` | STEP 4 (มี deliverable) | Font D1-D4 · 18 build-lessons · Build-vs-Edit · Preview-First |
| `_capabilities/check.md` | STEP 5 (ก่อนส่ง) | 9-dim QA · Speed-Tier · DETECTOR-not-DECIDER · Delta Re-QA |
| `context-discipline.md` | งานยาว/หลายรอบ | Worth-It compact check · keep-pointers · TERMINUS/CONTINUATION/GREY |
| `web-validation.md` | STEP 3 (ต้องยืนยัน fact) | เมื่อไหร่ค้น · cross-check ≥2 · cite · จัดการข้อมูลขัดกัน |

## Method (วิธีขาย/วิธีคิด) — เปิดตาม deliverable

| ไฟล์ | เปิดเมื่องาน |
|---|---|
| `method/questioning.md` | discovery / ตั้งคำถาม |
| `method/solution-selling.md` | qualify / business case / pain→value / proposal |
| `method/strategic-thinking.md` | กลยุทธ์ดีล / account plan / board paper |
| `method/why-thinking.md` | narrative ซื้อ / business case |
| `method/design-thinking.md` | workshop / envisioning / demo design |
| `method/relationship-management.md` | ความสัมพันธ์ / QBR / renewal / expansion |
| `method/enterprise-sale-strategy.md` | segment playbook (gov / large / SME) |

## Product (ความรู้ผลิตภัณฑ์) — เปิดตาม Q2

| ไฟล์ | product |
|---|---|
| `product/oracle-cloud.md` | Oracle Fusion Cloud (ERP/EPM/OCI) |
| `product/oracle-ebs.md` | Oracle EBS R12/11i |
| `product/netsuite.md` | NetSuite core (ERP/EPM/SuiteCloud) |
| `product/netsuite-thailand.md` | NetSuite + localization ไทย/APAC |
| `product/tor-competitive.md` | ตั้งสเปก/ตอบ TOR แข่ง Fusion⇄NetSuite (dual-angle · เปิดคู่ product ที่ขาย) |

## Domain (overlay ไทย/vertical) — เปิดตาม Q3

| ไฟล์ | domain |
|---|---|
| `domain/govt-gfmis.md` | GFMIS / งบประมาณภาครัฐไทย |
| `domain/govt-egp.md` | จัดซื้อจัดจ้าง / e-GP / TOR ภาครัฐ |
| `domain/th-etax.md` | ภาษีไทย / e-Tax / VAT / WHT / localization |
| `domain/fintech.md` | FinTech / lending / NPL / IFRS9 |

## Shared (ใช้ร่วม — เปิดเมื่อ reference อื่นชี้มา)

| ไฟล์ | concept |
|---|---|
| `_shared/meddpicc.md` | qualification scorecard 8 องค์ประกอบ |
| `_shared/why-stack.md` | เหตุผลซื้อ 5 ชั้น (Why Change/Now/Us/Invest/Stay) |
| `_shared/frameworks.md` | กรอบคิด (MECE/Pyramid/Issue-tree/Value-chain/ROI) |
| `_shared/thai-calibration.md` | ปรับภาษา/มารยาท/บริบทไทย + bilingual |

## QA

| ไฟล์ | ใช้ |
|---|---|
| `qa/pre-flight.md` | checklist ก่อนสร้าง/ส่ง deliverable |

---

## กฎการโหลด

- **chain ≤ 5 ไฟล์/งาน** — เลือกเท่าที่จำเป็น.
- `_shared/` เปิด **เมื่อถูกชี้** จาก method/product/domain — ไม่เปิดเองตั้งแต่แรก.
- งานตอบคำถามล้วน → method + (product/domain) พอ ไม่ต้องแตะ build-spec/check.
