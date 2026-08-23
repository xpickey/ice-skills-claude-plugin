# Product — Oracle NetSuite (ERP / EPM / SuiteCloud)

> ความรู้ผลิตภัณฑ์ NetSuite core สำหรับ fit-gap, scoping, business case. ใช้ทุก stage ที่ผูก NetSuite.
> **Thailand localization อยู่แยกที่ `product/netsuite-thailand.md`** — ที่นี่เน้น core ไม่เขียนซ้ำเรื่องไทย.
> ทุกข้ออ้าง version/feature → tag FACT/PATTERN/ASSUMPTION (ดู `_capabilities/know.md`) · release 2 ครั้ง/ปี → ตรวจสด.

---

## 1. ERP Core — Financials

| โมดูล | ครอบคลุม |
|---|---|
| **GL** | CoA with segments (subsidiary/department/class/location/project/custom), multi-subsidiary/currency (OneWorld), period close, consolidation+elimination |
| **AP/AR** | vendor/customer master, billing, payment, collections |
| **FA** | fixed assets, depreciation |
| **Cash/Bank** | reconciliation, cash management |
| **Revenue** | revenue recognition (ASC 606/IFRS 15) |

## 2. OneWorld (multi-entity)

- จุดขายหลัก NetSuite — **multi-subsidiary, multi-currency, multi-tax** ในระบบเดียว.
- consolidation across subsidiaries + intercompany + elimination.
- เหมาะองค์กรหลายบริษัท/หลายประเทศ (Thailand entity → ดู `product/netsuite-thailand.md`).

## 3. SuiteCloud (extend platform)

- **SuiteScript** — server/client script customization.
- **SuiteFlow** — workflow automation (no-code).
- **SuiteBuilder** — custom record/field/form.
- **SuiteAnalytics** — reporting/dashboard.
- **SDF** — SuiteCloud Development Framework (version-controlled deployment).

## 4. EPM (NetSuite Planning & Budgeting)

- planning, budgeting, forecasting · reconciliation (account recon) · narrative reporting.

## 5. Beyond ERP

- **SuiteCommerce** (e-commerce) · **CRM** (lead-to-cash) · **SuiteSuccess** (industry pre-config bundle — เร่ง implementation).

---

## Fit-Gap vs ทางเลือก (Primary-Lock)

ตอบ NetSuite = ล็อก NetSuite. เทียบในตารางแยก:

| มิติ | จุดแข็ง NetSuite |
|---|---|
| Multi-entity | OneWorld แข็งมาก (vs ระบบที่ต้อง bolt-on) |
| Cloud-native | SaaS แท้ตั้งแต่ออกแบบ |
| Mid-market fit | เหมาะ growth company / หลาย subsidiary |
| Time-to-value | SuiteSuccess เร่ง go-live |

> เทียบ vs Business Central / Fusion / SAP → ตารางแยก label ชัด (ดู `_capabilities/know.md`).

---

## สถานการณ์ขาย

- **new deployment** (growth company) = sweet spot.
- **wedge into legacy ERP shops** (EBS/SAP): เริ่ม subsidiary ใหม่ / commerce-first / multi-entity rollup → ขยายทีหลัง.
- **SuiteSuccess** = ลด implementation risk + time (industry pre-config).

---

## Fit-gap ลึก + man-day

- SuiteScript/SDF customization = ประเมิน effort ตาม complexity (tag PATTERN/ASSUMPTION).
- **อย่า over-commit** feature/customization ที่ไม่แน่ใจ → flag (ดู `_capabilities/know.md`).

> ลูกค้าไทย/APAC → **ต้องผูก `product/netsuite-thailand.md`** (THB/TFRS/VAT/WHT/e-Tax/BOI/OneWorld ไทย).
> เจอ TOR ที่ถูกตั้งสเปกเข้าทาง Fusion / ต้อง rebut gap → เปิด `product/tor-competitive.md` (มุม NetSuite defense).
