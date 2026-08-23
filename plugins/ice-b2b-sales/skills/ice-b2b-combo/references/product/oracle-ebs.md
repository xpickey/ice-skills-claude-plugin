# Product — Oracle E-Business Suite (EBS R12.2 / 11i)

> ความรู้ผลิตภัณฑ์ Oracle EBS (on-premise legacy) สำหรับ fit-gap, upgrade, migration, business case. ใช้ทุก stage ที่ผูก EBS.
> ทุกข้ออ้าง version/feature → tag FACT/PATTERN/ASSUMPTION (ดู `_capabilities/know.md`). EBS ยังอยู่ใน ~40% องค์กรใหญ่ไทย.

---

## 1. โมดูลหลัก

| กลุ่ม | โมดูล |
|---|---|
| **Financials** | GL · AP · AR · FA · Cash Management · E-Business Tax |
| **Procurement** | Purchasing · iProcurement · Sourcing · Supplier Lifecycle |
| **SCM** | Inventory · Order Management · WMS · Manufacturing (Discrete/Process) |
| **Projects** | Project Costing · Billing · Management |
| **HRMS** | Core HR · Payroll · Self-Service |

## 2. Technical architecture

- **3-tier:** database · application · client.
- **customization:** forms/reports, workflow, OAF, concurrent programs, APIs.
- **version:** R12.2 (online patching/ADOP) · 11i (legacy, ใกล้ end of support).

---

## 3. สถานการณ์งานขายหลัก

### A) Upgrade / stay on EBS
- 11i → R12.2 upgrade · หรือ stay + extended support.
- จุดพิจารณา: customization เยอะ = migration cost สูง · business continuity.

### B) Migration EBS → Cloud (displacement)
- EBS → Oracle Fusion Cloud (ดู `product/oracle-cloud.md`).
- **wedge strategy:** เริ่ม EPM/specific module ก่อน full swap (ลดความเสี่ยง + แสดง value เร็ว).
- **อย่า oversell "lift and shift ง่าย"** — re-implementation จริง ๆ มี business process redesign.

---

## Fit-Gap + man-day

- EBS customization เยอะ = ต้องประเมิน migration effort ละเอียด (tag PATTERN/ASSUMPTION ถ้าไม่มีข้อมูลจริง).
- **MD050 (config) / MD070 (technical)** — เอกสาร implementation มาตรฐาน.
- Thai localization: VAT/WHT/e-Tax (ดู `domain/th-etax.md`).

---

## Fit-Gap vs Cloud (Primary-Lock)

ตอบ EBS = ล็อก EBS. เทียบ Cloud ในตารางแยก:

| มิติ | EBS | → Cloud (เทียบ) |
|---|---|---|
| Deployment | on-premise (คุมเอง) | SaaS (Oracle host) |
| Update | manual patch | quarterly auto |
| Customization | ลึก (forms/OAF) | จำกัดกว่า (extensions/PaaS) |
| TCO ระยะยาว | infra + maintenance สูง | subscription |

> เทียบต้อง label ชัด ไม่ปนในย่อหน้า (ดู `_capabilities/know.md`).

---

## ข้อควรระวัง

- 11i ใกล้ end of support → Why Now ชัด (ดู `_shared/why-stack.md`) แต่อย่าขู่เกินจริง.
- migration ไม่ใช่ lift-and-shift — honest เรื่อง effort/risk (ดู `_capabilities/route.md` positive wording — honest).

> ภาครัฐ EBS → `domain/govt-gfmis.md` · งานไทย → `domain/th-etax.md`.
