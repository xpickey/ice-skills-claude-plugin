---
name: th-rd-etax-compliance
description: Thailand Revenue Department (กรมสรรพากร / RD) tax compliance reference for enterprise software deployments — VAT (Por Por 30 / 36), Withholding Tax (PND 1 / 1ก / 2 / 3 / 53 / 54 / 50 ทวิ), e-Tax invoice / e-Receipt (CA-signed XML), bank file formats (BAHTNET / PromptPay / ITMX), Thai chart of accounts (TFRS-aligned), Buddhist Era (พ.ศ.) calendar handling, statutory year-end reports (ภงด.50/51, บอจ.5). Use whenever a deal touches Thai tax compliance, e-invoicing, payroll tax, statutory reporting, or RD-required document formats. Bilingual EN + TH formal register.
---

# Thai Revenue Department (RD) — Tax & Compliance Reference

## Mission of this skill
Be the authoritative reference for Thai tax / RD / statutory requirements that shape enterprise software fit-gap, especially **ERP localization** (Oracle Cloud / EBS / NetSuite, SAP RISE/B1, MS Dynamics F&O/BC).

If a customer asks "does your system handle Thai VAT?", this skill provides the answer at clause level — not generic.

---

## VAT (Value Added Tax / ภาษีมูลค่าเพิ่ม)

### Standard rate
- **7%** (statutory rate per RD Code Section 80; reduced from 10% by Royal Decree, currently extended)
- **0%** for export, international transport, BOI-promoted, etc.
- **Exempt:** specific goods/services (basic foodstuffs, education, healthcare per Section 81)

### Filing
- **Por Por 30 (ภ.พ.30)** — monthly VAT return, due **15th of the following month** (electronic filing extends to 23rd)
- **Por Por 36 (ภ.พ.36)** — VAT for non-resident services (reverse-charge), monthly
- **Por Por 09 / 09.2** — VAT registration

### Key ERP requirements
- Tax determination by transaction type, supplier/customer status, ship-to/from
- Multiple VAT codes per transaction (line-level)
- **VAT registration number (TIN — Tax ID 13-digit)** captured per supplier/customer
- Branch code (สาขา 5-digit) handling — head office "00000", branches "00001+"
- VAT report Por Por 30 by branch
- Tax point timing: cash-basis vs accrual-basis distinction
- Output VAT vs Input VAT segregation

---

## Withholding Tax (WHT / ภาษีหัก ณ ที่จ่าย)

### PND family — the forms ERP must produce
| Form | Purpose | Frequency |
|---|---|---|
| **PND 1 (ภงด.1)** | Salaries / wages — employees | Monthly |
| **PND 1ก (ภงด.1ก)** | Annual summary of PND 1 | Annual |
| **PND 2 (ภงด.2)** | Dividends, interest, royalties — individuals | Monthly |
| **PND 3 (ภงด.3)** | Service fees / rent / professional — individuals | Monthly |
| **PND 53 (ภงด.53)** | Service fees / rent / professional — juristic persons (Thai companies) | Monthly |
| **PND 54 (ภงด.54)** | Payments to non-residents (juristic) | Monthly |
| **50 ทวิ (ใบรับรองหัก ณ ที่จ่าย)** | Withholding tax certificate issued to payee | Per transaction |

### Common WHT rates (most-cited)
| Service | Resident company | Non-resident |
|---|---|---|
| Service fees / professional | 3% | 15% (or per DTA — Double Tax Agreement) |
| Rent | 5% | 15% |
| Royalties | 3% | 15% |
| Interest | 1% | 15% |
| Advertising | 2% | 15% |
| Transportation (domestic) | 1% | 15% |
| Construction services | 3% | 15% |
| Salaries | progressive (per PIT bracket) | progressive |

### Filing
- Submit by **7th of the following month** (paper) — electronic filing extends to **15th**
- E-filing via RD's portal (rd.go.th — แบบฟอร์มอิเล็กทรอนิกส์)

### Key ERP requirements
- WHT determination at invoice entry (or payment entry — depends on accounting treatment)
- 50 ทวิ certificate generation with sequential numbering
- PND form generation in RD's prescribed XML/CSV format
- Multi-year WHT certificate archive retention
- DTA-rate handling for non-resident vendors

---

## e-Tax Invoice / e-Receipt (ใบกำกับภาษีอิเล็กทรอนิกส์)

### What it is
RD-driven program (since 2018, mandatory phased) requiring electronic tax invoices and receipts in **CA-signed XML format**.

### Two RD methods
1. **e-Tax Invoice & e-Receipt (full)** — XML via RD-approved Service Provider (CA-signed by Thai Government CA), or
2. **e-Tax Invoice by Email** — for small business, signed PDF emailed to RD + customer (sunset path)

### Mandatory data fields (per RD spec)
- **Issuer:** Tax ID (13-digit), branch code, name, address
- **Buyer:** Tax ID, branch code, name, address
- **Document number / date / type code** (e.g. "388" = invoice, "381" = credit note, "383" = debit note)
- **Line items** with VAT determination
- **Total amount, VAT, grand total** (in Thai Baht THB)
- **Digital signature** from Thai Certificate Authority (CA)

### CA / Service Providers (RD-approved)
- **Inet (INT)**, **TOT**, **CAT**, **K-Bank Knet**, **RD-Cloud (free)**, **Thai Digital ID (TDID)**
- ERPs typically integrate via partner middleware (e.g. **Inspirage**, **Tris**, **Avalara**, **Thai-RD certified partners**)

### ERP implementation pattern
```
[ERP invoice generated]
   ↓ Outbound XML via OIC / Logic Apps / SuiteScript
[Service Provider Middleware]
   ↓ Validates + CA-signs
[XML to RD repository] + [Buyer email]
   ↓ Acknowledgement
[Status returned to ERP — "delivered" / "rejected"]
```

### Common gaps in vanilla ERP (always require partner / extension)
- Oracle Fusion Cloud ERP — needs partner content
- Oracle EBS — partner localization (Inspirage) standard
- NetSuite — SuiteApp from partner
- SAP S/4HANA — SAP Document and Reporting Compliance + partner
- D365 F&O — partner add-on
- D365 BC — partner ISV (CSP-supplied)

---

## Bank file formats (Thai banking interfaces)

### BAHTNET / SMART (BoT — Bank of Thailand)
- **BAHTNET** — Real-time gross settlement, high-value, ฿2M+ typical
- **SMART (Same Day)** — bulk same-day clearing
- **SMART (Next Day)** — overnight clearing
- File format: typically **ISO 20022 XML** (PAIN.001 for credit, CAMT.054 for confirmation) + bank-specific variants

### PromptPay / ITMX
- **PromptPay** — citizen ID / phone-number linked instant transfer
- **PromptBiz** — corporate variant (B2B), supports e-invoice settlement
- Used heavily in payroll, supplier payment, customer collections
- File format: ISO 20022 + Thai-specific extensions

### Bank-specific corporate cash-management files
| Bank | Format / portal |
|---|---|
| **K-Bank (KBank)** | K-Cash Connect Plus — proprietary format + ISO 20022 |
| **Bangkok Bank (BBL)** | iCash — proprietary + ISO 20022 |
| **SCB** | SCB Business Net — proprietary + ISO 20022 |
| **Krungthai (KTB)** | Krungthai Corporate — proprietary + ISO 20022 |
| **TMBThanachart (TTB)** | TTB Business Click |
| **Krungsri (BAY)** | Krungsri Business Online |

### ERP integration
- **Outgoing (payments):** ERP generates payment file → bank format → upload to bank portal or H2H
- **Incoming (statements):** Bank statement (BCA / MT940 / CAMT.053) → reconcile in ERP CM module
- **Host-to-Host (H2H):** SFTP / API-based for large customers
- **Real-time:** PromptPay / PromptBiz APIs

---

## Thai chart of accounts (TFRS-aligned)

### Accounting standard
- **TFRS (Thai Financial Reporting Standards)** — IFRS-aligned with TH-specific overlays
- **TFRS for NPAEs** — small/non-publicly-accountable entities
- **PSAS / IPSAS-based** — public sector (separate)

### Statutory accounts to support
- **บัญชีแยกประเภท (GL)** — standard structure
- **บัญชีลูกหนี้การค้า (AR)** — by customer
- **บัญชีเจ้าหนี้การค้า (AP)** — by supplier
- **บัญชีสินค้าคงเหลือ (Inventory)** — perpetual / periodic
- **บัญชีทรัพย์สิน (FA)** — depreciation methods (TFRS allows component depreciation)

### Key statutory chart-of-accounts elements
- VAT input/output accounts (separate ledger accounts)
- WHT receivable/payable accounts
- BOI tax-incentive accounting (separate cost centers / projects)
- IFRS 16 lease accounting (TFRS 16 equivalent)
- IFRS 9 financial instruments (TFRS 9 — for BFSI)

---

## Buddhist Era (พ.ศ.) calendar handling

- Thai Buddhist Era = Christian Era + 543 (e.g. CE 2026 = BE 2569 / พ.ศ. 2569)
- **Display layer** — most ERPs handle via locale config; underlying data stored in CE
- **Statutory documents** — must show พ.ศ. on tax forms, invoices, official documents
- **Fiscal year** — Thai government: 1 Oct – 30 Sep; private sector: usually 1 Jan – 31 Dec or per company decision
- **Date formats** — DD/MM/YYYY (พ.ศ.) common; ISO 8601 underneath

---

## Annual statutory year-end reports

### For juristic persons (Thai companies)
| Report | Purpose | Due |
|---|---|---|
| **ภงด.50** | Corporate income tax return (annual) | 150 days after fiscal year-end |
| **ภงด.51** | Half-year corporate tax estimate | 60 days after half-year |
| **บอจ.5** | List of shareholders | Annually with Department of Business Development (DBD) |
| **บัญชีงบดุล + งบกำไรขาดทุน + งบกระแสเงินสด** | Annual financial statements | Filed with DBD + RD |
| **ส.บ.ช. 3** | Auditor declaration (CPA-signed) | With financial statements |

### For BFSI / SET-listed
- **TFRS 9** quarterly reporting for credit risk
- **SET 56-1 / 56-2 forms** — annual / quarterly
- **Bank of Thailand (BoT)** reporting — DPS / DSI reports for banks
- **OIC** for insurance — actuarial reports

---

## PDPA (Personal Data Protection Act / พรบ.คุ้มครองข้อมูลส่วนบุคคล 2562)

- Thai equivalent of GDPR — **active since 1 June 2022**
- **Consent management** — customers must consent to data processing
- **Data subject rights** — access, rectification, erasure, portability
- **Data Protection Officer (DPO)** required for large data controllers
- **Data residency** — not strictly required but encouraged
- **Penalty:** up to ฿5M + criminal liability + 1% of revenue

### ERP / IT implications
- Customer / employee / vendor master must support consent flags
- Audit trail for personal data access
- Data subject request (DSR) workflow
- Data retention policy enforcement
- Encryption at rest + in transit (industry-standard but specifically called out for sensitive PII)

---

## Common Thai-localization gaps in vanilla ERP — and where they're closed

| Function | Oracle Fusion Cloud | Oracle EBS | NetSuite | SAP RISE | D365 F&O / BC |
|---|---|---|---|---|---|
| VAT 7% calc | ✅ standard | ✅ standard | ✅ standard | ✅ standard | ✅ standard |
| Por Por 30 form | ⚠️ partner pack | ⚠️ partner pack (Inspirage) | ⚠️ SuiteApp | ⚠️ partner / SAP Doc Comp | ⚠️ partner |
| WHT (PND family + 50 ทวิ) | ⚠️ partner | ⚠️ partner | ⚠️ SuiteApp | ⚠️ partner | ⚠️ partner |
| e-Tax invoice (CA-signed XML) | ⚠️ partner middleware | ⚠️ partner middleware | ⚠️ SuiteApp + middleware | ⚠️ Doc Comp + middleware | ⚠️ partner middleware |
| BAHTNET / SMART file format | ⚠️ partner / OIC | ⚠️ partner / config | ⚠️ Boomi / SuiteScript | ⚠️ BTP / partner | ⚠️ partner |
| Buddhist calendar display | ✅ locale | ⚠️ report mod | ⚠️ display script | ✅ locale | ✅ locale |
| Thai language UI | ✅ standard | ✅ standard | ✅ standard | ✅ standard | ✅ standard |

> **Rule of thumb:** Always assume Thai localization needs **partner content** (~$30K–80K USD line-item in the proposal) regardless of ERP. Don't sell vanilla.

---

## Output usage

When invoked by another agent, return:
- Specific RD requirements relevant to the deal (filing form, format, frequency)
- Localization gaps in the proposed ERP and the partner / pack to close them
- Estimated localization cost band ($30K–80K USD typical for full TH compliance pack)
- e-Tax CA / Service Provider recommendation
- Bank format requirements based on customer's bank list
- PDPA implications for personal data handling
- Sources: RD Code (ประมวลรัษฎากร), specific Por Por / PND / Section numbers
- Cross-reference to `vertical-knowledge-agent` for industry-specific Thai compliance (BFSI: BoT; Insurance: OIC; Public sector: GFMIS)
