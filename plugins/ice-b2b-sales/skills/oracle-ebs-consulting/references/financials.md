## PART 1: Oracle EBS Financials

### Core Modules Coverage

#### General Ledger (GL)

**Chart of Accounts & Ledger Setup**:
- **Flexfield Structure**: Up to 30 segments (Company, Cost Center, Account, Product, Project, Intercompany, Future, Spare)
- **Value Sets**: Independent, dependent, table-validated, special (date, time), validation types
- **Cross-Validation Rules**: Segment combination validation, error/warning messages, effective dating
- **Accounting Flexfield (COA)**: Structure definition, segment qualifiers, allow dynamic inserts
- **Key Flexfields**: GL_BALANCING, GL_ACCOUNT, GL_INTERCOMPANY qualifiers
- **Ledger Architecture**: Primary ledger, secondary ledgers, reporting currencies, adjustment-only ledgers
- **Chart of Accounts Assignment**: Assign COA to ledger, multi-org access control (MOAC)
- **Ledger Options**: Currency, calendar, accounting method (accrual/cash), retained earnings account
- **Multi-Org Setup**: Operating units, legal entities, business groups, MOAC configuration

**Accounting Calendar & Periods**:
- **Calendar Definition**: Period types (month, quarter, year), period naming conventions
- **Period Setup**: Start date, end date, year, quarter assignment, adjustment periods
- **Period Control**: Open, close, permanently close, future-dated entries, reopening closed periods
- **Multi-Period Accounting**: Allow GL posting in future periods while closing current period
- **Year-End Close**: Final close checklist, retained earnings sweep, opening next fiscal year

**Journal Processing**:
- **Manual Journals**: Online entry, journal import, recurring journals, AutoAllocate, MassAllocations
- **Journal Sources**: Define sources (Payables, Receivables, Subledger Accounting, manual)
- **Journal Categories**: Default categories per source, approval requirements, effective date rules
- **Journal Approval Workflows**: AME integration, position-based approval, amount limits, delegation
- **Recurring Journals**: Formula-based, skeleton journals, schedule-based posting
- **Reversing Journals**: Automatic reversal, reversal date, reversal period control
- **Statistical Journals**: Non-currency journals, headcount, square footage, units for allocations
- **Encumbrance Journals**: Budget control integration, commitment tracking, liquidation

**Subledger Accounting (SLA)**:
- **Accounting Setup Manager**: Transaction objects, event classes, event types, accounting attributes
- **Journal Line Definitions**: Account derivation rules, multi-currency, statistical amounts
- **Subledger Journal Entries**: Create Accounting program, post to GL, drill-down to source
- **Accounting Methods**: IFRS, GAAP, Tax, Statutory, secondary ledger accounting methods
- **SLA Diagnostics**: Accounting events, event statuses, accounting entries, error resolution
- **Reporting**: SLA balances, trial balance, detail trial balance, accounting journals report

**Allocations & MassAllocations**:
- **Allocation Rules**: Percentage-based, formula-based, statistical account-based
- **Allocation Steps**: Generate, post, review, reverse
- **Batch Allocations**: Multiple allocation rules in single batch, automated scheduling
- **AutoAllocate**: Automated allocation posting integrated with period close
- **Cost Center Allocations**: Overhead distribution, shared services allocation, activity-based costing

**Currency & Translation**:
- **Currency Definition**: Currency codes (USD, THB, EUR, GBP), precision, rounding rules
- **Conversion Rate Types**: Corporate, User, Spot, Historical, custom rate types
- **Daily Rates**: Rate entry, rate import, rate change history
- **Translation**: Foreign currency translation (FC to reporting currency), translation adjustments
- **Revaluation**: Balance revaluation, unrealized gains/losses, realized gains on settlement
- **Average Balance Processing**: Weighted average, simple average, actual balance

**Consolidations**:
- **Financial Consolidation Hub**: Inter-ledger transfers, elimination entries, consolidation workflows
- **Global Consolidation System (GCS)**: Pre-R12 consolidation tool, data collection, eliminations
- **Mapping Sets**: Account mapping, entity mapping, consolidation hierarchies
- **Elimination Sets**: Intra-company eliminations, equity eliminations, investment eliminations
- **Consolidation Reports**: Consolidated balance sheet, income statement, equity reconciliation

**Financial Reporting & Analysis**:
- **Financial Statement Generator (FSG)**: Row sets, column sets, report definitions, content sets
- **Account Inquiry**: Account drill-down, journal drill-down, subledger drill-down
- **Trial Balance**: Detail trial balance, summary trial balance, ledger comparison
- **Budget vs. Actuals**: Budget inquiry, variance analysis, budget journals
- **Oracle Discoverer**: Ad-hoc queries, custom reports, EUL administration
- **Oracle Business Intelligence Applications (OBIA)**: Pre-built dashboards, KPIs, analytics

#### Accounts Payable (AP)

**Supplier Management**:
- **Supplier Setup**: Supplier name, tax registration number, address, contacts, sites
- **Supplier Sites**: Pay site, procurement site, payment terms, payment methods, tax defaults
- **Supplier Contacts**: Contact roles (purchasing, payment, ordering), email, phone
- **Supplier Merge**: Duplicate supplier cleanup, merge supplier records, historical transactions
- **Supplier Hold**: Payment hold, invoice hold, purchasing hold, reason codes
- **Supplier Banking**: Bank accounts, IBAN, SWIFT, ACH details, payment instruments
- **Supplier Profile**: Payment priority, pay group, liability account, prepayment account

**Invoice Processing**:
- **Invoice Entry**: Standard invoice, credit memo, debit memo, prepayment, expense report
- **Invoice Import**: EDI, XML, third-party scanning (Kofax, Captiva), OCR processing
- **Invoice Matching**: 2-way (PO-Invoice), 3-way (PO-Receipt-Invoice), 4-way (+Inspection)
- **Match Tolerance**: Quantity tolerance, amount tolerance, ship-to tolerance, price tolerance
- **Invoice Approval Workflow**: AME rules, position hierarchy, invoice amount thresholds
- **Invoice Hold**: Quantity variance, price variance, tax variance, approval required, manual hold
- **Invoice Validation**: Account validation, tax validation, matching validation, approval status
- **Withholding Tax**: WHT calculation, WHT certificates, WHT types, supplier tax profiles

**Payment Processing**:
- **Payment Process Request (PPR)**: R12.2 payment architecture, payment document creation
- **Payment Methods**: Check, EFT, Wire Transfer, SWIFT, ACH, BACS, PromptPay (Thailand)
- **Payment Programs**: Build, format, print/transmit, confirm, accounting
- **Payment Formats**: Oracle Payments formats, custom formats via BIP templates
- **Positive Pay**: Check register, electronic check register, fraud prevention
- **Payment Cancellation**: Void check, stop payment, reverse payment, reissue payment
- **Payment History**: Payment inquiry, payment status, cleared payments, outstanding payments
- **Bank Reconciliation**: Auto-reconcile cleared payments, exception handling, cash application

**Expense Report Processing**:
- **iExpenses Self-Service**: Web-based expense entry, receipt attachment, policy compliance
- **Expense Templates**: Pre-filled expense reports, recurring expenses, project-charged expenses
- **Expense Types**: Mileage, per diem, out-of-pocket, credit card expenses
- **Expense Approval**: Manager approval, project manager approval, audit random sampling
- **Policy Violations**: Over-limit alerts, out-of-policy flags, justification required
- **Credit Card Integration**: Corporate card feeds, personal card reimbursement, reconciliation
- **Cash Advance**: Employee cash advance, advance clearing against expense report

**Accounting & Reporting**:
- **Accrual Accounting**: Period-end accruals, receipt accruals, expense accruals
- **Subledger Accounting**: Create accounting, transfer to GL, drill-back capability
- **Aging Reports**: Payables aging by supplier, due date, invoice date
- **Payment Forecast**: Cash forecast, payment due list, supplier payment schedule
- **Audit Reports**: Invoice register, payment register, withholding tax certificates
- **Vendor Analysis**: Top vendors by spend, payment performance, early payment discounts

#### Accounts Receivable (AR)

**Customer Management**:
- **Customer Setup**: Customer name, tax registration, profile class, payment terms, credit limit
- **Customer Sites**: Bill-to, ship-to, contact information, dunning site, statement site
- **Customer Contacts**: Billing contact, shipping contact, collections contact
- **Customer Merge**: Duplicate customer cleanup, merge customer accounts, transaction history
- **Customer Profile Classes**: Credit policies, payment terms, dunning procedures, statement cycles
- **Customer Banking**: Bank accounts, direct debit mandates, auto-payment methods
- **Credit Management**: Credit limits, credit holds, credit reviews, risk scoring

**Invoicing & Revenue**:
- **Invoice Creation**: Manual invoices, imported invoices, AutoInvoice interface
- **Invoice Types**: Standard invoice, credit memo, debit memo, deposit, guarantee
- **Transaction Sources**: Order Management, manual entry, external systems
- **Transaction Types**: Line, tax, freight, charges, discounts
- **Flexfield (RA_INTERFACE_LINES)**: Import invoices via interface tables, validation, processing
- **Accounting Rules**: Revenue recognition (immediate, fixed schedule, deferred), ASC 606 alignment
- **AutoAccounting**: Revenue account, receivable account, tax account, freight account derivation
- **Printing & Delivery**: Invoice print, email delivery, EDI transmission, customer portal

**Receipt Processing**:
- **Receipt Entry**: Manual receipts, automatic receipts, lockbox receipts, credit card receipts
- **Receipt Methods**: Check, EFT, credit card, on-account, cash
- **Receipt Application**: Apply to invoice, on-account, unapplied, prepayment
- **AutoCash Rules**: Automatic matching by invoice number, purchase order, sales order
- **Lockbox Processing**: Bank file import (MT940, BAI2, SWIFT), auto-application, exception handling
- **Chargebacks**: Deduction management, short payments, dispute resolution
- **Receipt Reversal**: NSF (non-sufficient funds), stop payment, incorrect application
- **Receipt Clearing**: Clear receipts to cash, bank reconciliation, remittance matching

**Collections Management**:
- **Collector Assignment**: Auto-assignment by customer, territory, aging bucket
- **Dunning Letters**: Automatic dunning, dunning levels, escalation rules
- **Collections Workbench**: Aging buckets, customer contact, promise to pay, dispute tracking
- **Aging Analysis**: 30-60-90-120 day buckets, customer aging, invoice aging
- **Collector Performance**: Collector metrics, DSO (Days Sales Outstanding), collection effectiveness
- **Dispute Management**: Dispute reason codes, dispute resolution workflow, adjustment processing
- **Customer Statements**: Monthly statements, open item statements, balance forward statements

**Revenue Recognition & Reporting**:
- **Deferred Revenue**: Revenue deferral rules, multi-period recognition, revenue allocation
- **Revenue Contingencies**: Collectability assessment, variable consideration, contract modifications
- **Sales Tax Processing**: Tax calculation, tax posting, tax reconciliation, e-Tax filing (Thailand)
- **Receivables Reporting**: Aging reports, revenue reports, receipt reports, collection reports
- **Cash Application**: Unapplied cash, on-account credits, prepayments, deposit application
- **Intercompany Receivables**: IC invoicing, IC receipts, IC elimination in consolidation

#### Fixed Assets (FA)

**Asset Setup & Categories**:
- **Asset Categories**: Category definition, default accounts, depreciation rules, asset lifecycle
- **Asset Books**: Corporate book, tax book, IFRS book, depreciation methods (SL, DB, SYD, custom)
- **Location Setup**: Office locations, building, floor, room, responsible employee
- **Depreciation Methods**: Straight-line, declining balance, sum-of-years digits, units of production
- **Prorate Conventions**: Calendar, period, mid-period, full-period, none
- **Retirement Conventions**: Gain/loss calculation, NBV retirement, sale proceeds

**Asset Transactions**:
- **Asset Additions**: Manual additions, PO mass additions, AP invoice integration
- **Mass Additions**: Create from PO receipts, create from AP invoices, review, post, split, merge
- **Asset Adjustments**: Cost adjustment, depreciation adjustment, life adjustment, salvage value
- **Asset Transfers**: Location transfer, employee transfer, category transfer, between-book transfer
- **Asset Revaluation**: Revaluation reserve, fair value adjustment, impairment
- **Asset Retirements**: Retire by sale, retire by disposal, retire by write-off, partial retirement
- **Asset Splits**: Split asset into multiple assets, split cost, split depreciation reserve

**Depreciation Processing**:
- **Depreciation Run**: Calculate depreciation, review, post to GL, period-end close
- **Catch-Up Depreciation**: Missed periods, retroactive adjustments, prior period catch-up
- **Depreciation Calendars**: Fiscal calendar, period setup, depreciation frequency (monthly, quarterly)
- **Bonus Depreciation**: Tax incentive depreciation (US), accelerated depreciation (Thailand BOI)
- **Impairment**: Impairment testing, recoverable amount, write-down to recoverable amount
- **Asset Projection**: Future depreciation projection, remaining life, projected retirement

**Physical Inventory & Reporting**:
- **Asset Tagging**: Barcode, RFID, QR code, physical tag assignment
- **Physical Inventory**: Physical count, asset verification, location confirmation, reconciliation
- **Asset Inquiry**: Asset details, transaction history, depreciation history, current NBV
- **Asset Reports**: Asset register, depreciation forecast, retirement report, tax reporting
- **Asset Intelligence**: Asset utilization, asset lifecycle analysis, asset replacement planning

#### Cash Management (CE)

**Bank Account Setup**:
- **Bank Definition**: Bank name, branch, address, SWIFT code, routing number
- **Bank Accounts**: Account number, currency, account type (checking, savings, payroll)
- **Bank Account Relationships**: Legal entity, operating unit, cash account, bank charges account
- **Multi-Currency Accounts**: Foreign currency accounts, exchange rate handling
- **Cash Pooling**: Notional pooling, physical pooling, zero-balance accounts, target balance

**Bank Statement Reconciliation**:
- **Bank Statement Import**: MT940, BAI2, SWIFT MT101, custom formats, manual entry
- **Auto-Reconciliation**: Match cleared receipts, cleared payments, adjustments, miscellaneous transactions
- **Manual Reconciliation**: Reconcile unmatched transactions, bank errors, timing differences
- **Bank Statement Lines**: Statement line details, transaction codes, reference numbers
- **Reconciliation Tolerance**: Amount tolerance, date tolerance, auto-create adjustments
- **Month-End Close**: Statement reconciliation close, outstanding items report, reconciliation differences

**Cash Forecasting & Positioning**:
- **Receivables Forecast**: Expected receipts by due date, collection assumptions, DSO
- **Payables Forecast**: Expected payments by due date, payment terms, early payment discounts
- **Cash Position**: Current cash position, projected inflows, projected outflows, net position
- **Cash Flow Report**: Operating activities, investing activities, financing activities
- **Funds Transfer**: Inter-bank transfers, petty cash replenishment, cash concentration

**Bank Charges & Interest**:
- **Bank Charges**: Bank fees, transaction charges, account maintenance fees
- **Interest Calculation**: Interest earned, interest paid, accrual calculation
- **Bank Reconciliation Items**: Outstanding checks, deposits in transit, bank errors

---
