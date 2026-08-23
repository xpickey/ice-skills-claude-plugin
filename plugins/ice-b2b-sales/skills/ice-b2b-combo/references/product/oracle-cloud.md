# Product — Oracle Fusion Cloud Applications (ERP / EPM / OCI)

> ความรู้ผลิตภัณฑ์ Oracle Fusion Cloud สำหรับ fit-gap, scoping, business case. ใช้ทุก stage ที่ผูก product นี้.
> ทุกข้ออ้าง version/feature/man-day → tag FACT/PATTERN/ASSUMPTION (ดู `_capabilities/know.md`) · release เปลี่ยน quarterly → ตรวจสด.

---

## 1. ERP Cloud — Financials

| โมดูล | ครอบคลุม |
|---|---|
| **GL** | Chart of Accounts (segment design), multi-ledger, period close, allocations, FX translation/revaluation, consolidation, account hierarchies, journal workflow |
| **AP** | vendor master, invoice matching (2/3-way), payment processing, approval workflow |
| **AR** | customer master, billing, receipts, collections, revenue |
| **FA** | asset lifecycle, depreciation, retirement |
| **Cash Mgmt** | bank reconciliation, cash positioning |
| **Tax** | tax determination engine (ผูก `domain/th-etax.md` สำหรับ VAT/WHT ไทย) |

## 2. ERP Cloud — Procurement / SCM

- **Procurement:** self-service procurement, supplier portal, sourcing, purchasing, supplier qualification.
- **SCM:** inventory, order management, manufacturing, planning, cost management.

## 3. EPM Cloud (Planning + Close)

- **Planning (PBCS/EPBCS):** budgeting, forecasting, workforce/capex planning, scenario.
- **Financial Consolidation (FCCS):** consolidation, eliminations, ownership.
- **Account Reconciliation (ARCS):** recon automation, transaction matching.
- **Narrative Reporting / Tax Reporting** — disclosure management, Pillar Two.

## 4. OCI (Infrastructure)

- compute, storage, networking, autonomous database, security · region/availability domain · landing zone.
- จุดขาย: integrated stack (apps + DB + infra เจ้าเดียว) · security.

---

## Fit-Gap (เทียบกับทางเลือก — Primary-Lock)

ตอบเรื่อง Oracle Cloud = ล็อกที่ Oracle (ดู `_capabilities/know.md` Primary-Lock). เทียบคู่แข่งในตารางแยก:

| มิติ | จุดแข็ง Oracle Cloud |
|---|---|
| Financials depth | แข็งมากสำหรับองค์กรใหญ่ · multi-entity/currency/GAAP |
| EPM | ครบที่สุดในตลาด (planning+close+recon ในชุดเดียว) |
| Integrated stack | apps+DB+infra เจ้าเดียว (vs best-of-breed ที่ต้อง integrate) |
| quarterly update | feature ใหม่ทุกไตรมาส (ต้องตามทัน — ดู staleness) |

> เทียบ vs SAP/Dynamics/Workday → ทำตารางแยก label ชัด ไม่ปนในย่อหน้า (ดู `_capabilities/know.md`).

---

## Fit-gap ลึก + man-day (เมื่อถูกถาม)

- fit-gap Level 0-0.5 (business) = ตอบได้เลย · Level 1+ (version/integration/customization) = ต้องลงรายละเอียด architecture.
- **man-day estimate** = tag PATTERN ถ้าอิง benchmark · ถ้าลูกค้าจะตัดสินใจจากตัวเลขนี้ = ต้องยืนยัน (FACT) ไม่เดา.
- Thai localization: ผูก `domain/th-etax.md` (VAT/WHT/e-Tax) + `product/...` localization features.

---

## ข้อควรระวัง

- **อย่า over-commit version capability** — feature ที่ไม่แน่ใจว่ามีใน release ปัจจุบัน → flag ตรวจสอบ (ดู `_capabilities/know.md`).
- quarterly release = ข้อมูลเก่าเร็ว → เรื่อง feature ใหม่/limit ตรวจสด ก่อนใส่ในข้อเสนอ.

> งานภาครัฐไทยที่ใช้ Oracle → ผูก `domain/govt-gfmis.md` (GFMIS integration) + `domain/govt-egp.md` (TOR).
> งานตั้งสเปก/ตอบ TOR ที่แข่งกับ NetSuite → เปิด `product/tor-competitive.md` (dual-angle playbook).
