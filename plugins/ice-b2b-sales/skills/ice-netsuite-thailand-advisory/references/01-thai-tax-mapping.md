# Reference 01 — Thai Tax Mapping to NetSuite

Version: V01R01 | Date: 2026.05.23

> Disclaimer: This is a design-input reference, not tax advice. Verify all rates, filings, and procedural rules against the latest Revenue Department announcements and the customer's tax advisor before commitment.

## VAT (ภาษีมูลค่าเพิ่ม)

| Item | Thai term | Notes |
|---|---|---|
| Standard rate | อัตรามาตรฐาน | 7 percent at time of writing — read from customer's tax setup, do not hardcode |
| Zero-rate | อัตรา 0% | Exports, certain international services |
| Exempt | ยกเว้น | Specific exempt activities — confirm scope with customer |
| Registration threshold | เกณฑ์การจดทะเบียน | Confirm current threshold with customer's tax advisor |
| Tax point | จุดความรับผิด | Generally at invoice issue or payment, whichever earlier |
| Branch reporting | สาขา | Thai law requires VAT filing per branch; configure branch codes accordingly |

### NetSuite configuration pointers

- Set up separate tax codes per category — input VAT, output VAT, zero-rate, exempt.
- Branch code is captured via a custom field on subsidiary or location, then surfaced on the tax filing report.
- VAT return ภพ.30 is the monthly filing; design a saved search or custom report early. Standard NetSuite tax reports do not match the Thai filing format.

## Withholding Tax (ภาษีหัก ณ ที่จ่าย)

| Transaction type | Common rate | PND form | Notes |
|---|---|---|---|
| Service to corporation | 3% | PND 53 | Confirm against specific service category |
| Rent to corporation | 5% | PND 53 | |
| Transportation | 1% | PND 53 | |
| Service to individual | 3% (subject to progressive bands) | PND 3 | Individual rates more complex |
| Employment income | Progressive | PND 1 | Out of typical NetSuite scope — payroll system |
| Dividend | 10% | PND 2 | |
| Interest | 1% / 15% (varies) | PND 2 | |

### NetSuite configuration pointers

- WHT is recorded at payment time in Thai practice — design payment flow accordingly.
- Vendor master must carry WHT type and tax ID for the หนังสือรับรองการหักภาษี (WHT certificate) generation.
- PND extract: build a saved search keyed on payment date, grouped by vendor, summing WHT amount by category. Automate the export to the format the customer's tax filing system expects.

## e-Tax Invoice and e-Receipt

The Revenue Department's e-Tax framework requires:

- XML format per RD specification.
- Digital signature (CA-issued certificate).
- Submission to the RD within timing rules.

### NetSuite options

| Option | Approach | Trade-off |
|---|---|---|
| Localization SuiteApp | Use a Thai partner's SuiteApp that adds e-Tax XML generation and submission inside NetSuite | Lowest integration risk; vendor lock-in; ongoing fee |
| Middleware integration | NetSuite → middleware (Boomi, MuleSoft, native HTTPS) → RD-certified service provider | Most flexibility; more design and maintenance effort |
| Manual export | Generate invoice PDF + XML, submit manually via RD portal | Acceptable only for very low volume |

Flag the choice in the proposal; do not defer it to UAT.

## Pillar Two (GloBE)

Applicable when consolidated group revenue exceeds EUR 750 million in two of the last four fiscal years.

Data requirements per jurisdiction:

- Financial accounting net income or loss (FANIL)
- Covered taxes
- Substance-based income exclusion (payroll + tangible assets)
- Top-up tax computation

### NetSuite contribution

NetSuite is a source system, not the calculation engine. Source data to extract per jurisdiction:

- GL data with country/entity tagging
- Payroll cost (from HR system, mapped to NetSuite)
- Tangible asset NBV (from Fixed Asset module)
- Tax expense by jurisdiction

Hand the calculation to Oracle EPM TRCS or equivalent. NetSuite Analytics Warehouse (NSAW) can stage the data.

## BOI (Board of Investment)

BOI privileges affect:

- Corporate income tax exemption / reduction for promoted activities
- Import duty exemption on specific machinery / raw materials
- Separate cost and revenue tracking for promoted vs non-promoted business

### NetSuite design choices

See main SKILL.md Section 1.5. Three approaches; pick based on volume and audit complexity:

1. **Separate subsidiary per BOI promotion** — cleanest segregation, doubles master-data effort.
2. **Single subsidiary with classification dimension** — efficient master data, requires discipline in posting.
3. **Multi-book accounting** — primary book = legal, secondary book = BOI reporting view.

Document the choice and rationale in the business case.

## Thai-language statutory documents

Customers and auditors frequently expect these in Thai:

- Tax invoice (ใบกำกับภาษี)
- Credit memo (ใบลดหนี้)
- Debit memo (ใบเพิ่มหนี้)
- Receipt (ใบเสร็จรับเงิน)
- Withholding tax certificate (หนังสือรับรองการหักภาษี ณ ที่จ่าย)

### Font and PDF handling

- Use TH Sarabun New or Sarabun for body text — these are the de facto standards for Thai government and corporate documents.
- Embed the font in the PDF; do not rely on system default.
- Test rendering at 12pt and 14pt; some custom PDF templates have Thai diacritic alignment issues that only surface in print.

## Other Thai-specific items to flag during scoping

- Social Security Fund (กองทุนประกันสังคม) reporting — usually payroll system, not NetSuite, but the integration must carry the data.
- Provident Fund (กองทุนสำรองเลี้ยงชีพ) — same as above.
- Stamp Duty (อากรแสตมป์) — for specific contract types, may require accrual or expense recognition in NetSuite if material.
- Specific Business Tax (ภาษีธุรกิจเฉพาะ) — applies to certain financial services; rare in scope but flag it.
