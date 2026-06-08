# GFMIS vs ERP — Consulting Comparison Guide
## อ้างอิง: Practical Implementation Experience in Thai Government Financial Environments

---

## 1. Core Concept: "Control System" vs "Management System"

### GFMIS = Fiscal Control System
- **Primary Objective**: Control budget usage, Enforce compliance, Ensure transparency
- **Design Philosophy**: Every transaction must comply with budget + regulation FIRST
- **Driver**: Law/Regulation-driven
- **Examples of Control**: Hard Stop if no budget, Mandatory segregation, Fixed workflow

### ERP (SAP / Oracle / Dynamics) = Business Management System
- **Primary Objective**: Improve operational efficiency, Support decision-making, Optimize resources
- **Design Philosophy**: Transactions driven by business operations
- **Driver**: Efficiency-driven
- **Examples of Flexibility**: Configurable workflow, Optional budget control, Custom approval rules

```
GFMIS: LAW → BUDGET → TRANSACTION → REPORTING
ERP:   OPERATION → TRANSACTION → CONTROL (optional) → REPORTING
```

---

## 2. Budget Control — Most Critical Difference

### GFMIS Budget Control
| Feature | Detail |
|---------|--------|
| Role | Legal Mandatory Control |
| Hard Stop | YES — cannot proceed if budget insufficient |
| Commitment | Automatic at PO creation |
| Structure | Multi-dimensional: Fund Source + Budget Type + Activity + Commitment Item |
| Transfer | Requires formal approval process (อง.03) |
| Carry-forward | Regulated (6+6 months, ม.43 พรบ.วิธีการงบ 2561) |

### ERP Budget Control
| Feature | Detail |
|---------|--------|
| Role | Management Tool (optional) |
| Hard Stop | Configurable — can be Warning only or fully disabled |
| Commitment | Optional (can skip) |
| Structure | Flexible by company policy |
| Transfer | Internal process, no regulation |

### Practical Implication
```
GFMIS: สร้าง PO → ระบบตรวจงบทันที → ถ้าไม่พอ = ไม่สามารถสร้างได้ (Hard Stop)
ERP:   สร้าง PO → ระบบแจ้งเตือน (Warning) → ยังสร้างได้ต่อไป (Soft Control)
```

---

## 3. Payment Process — Centralized vs Decentralized

### GFMIS Payment
```
หน่วยราชการ → บันทึกขอเบิก → อนุมัติ 2 ระดับ
    → กรมบัญชีกลาง/คลังจังหวัด ตรวจสอบ
    → Run Payment (15:00)
    → BOT / BAHTNET / SMART
    → โอนเงินตรง Vendor / ผู้มีสิทธิ
```
- **Control Point**: CGD เป็น Central Treasury
- **Agency Role**: บันทึกและอนุมัติ แต่ไม่ได้จ่ายเงินเอง
- **Security**: ลดความเสี่ยงทุจริตเพราะ agency ไม่มีเงินสดในมือ

### ERP Payment
```
AP Invoice → Approval → Payment Run
    → จ่ายจากบัญชีธนาคารขององค์กร
    → โอนตามกำหนดการขององค์กร
```
- **Control Point**: Organization treasury / CFO
- **Flexibility**: สามารถเลือกเวลาจ่าย วิธีจ่าย ธนาคารที่ใช้

---

## 4. Procurement — Legal vs Operational

### GFMIS Procurement (PO Module + e-GP)
| Aspect | Detail |
|--------|--------|
| Regulation | พรบ.จัดซื้อจัดจ้าง 2560 + ระเบียบกระทรวงการคลัง 2560 |
| System | ผ่านระบบ e-GP บังคับ |
| PO Nature | Legal Commitment Document |
| Budget Effect | ผูกพันงบประมาณทันที (Commitment) |
| Audit | สตง. มีสิทธิตรวจสอบทุกขั้นตอน |

### ERP Procurement
| Aspect | Detail |
|--------|--------|
| Regulation | ไม่มี External Legal Enforcement |
| System | Internal system ขององค์กร |
| PO Nature | Operational Document |
| Budget Effect | Optional commitment |
| Audit | Internal audit only |

---

## 5. Accounting Standards

### GFMIS — Government Accounting
```
Standard:  Thai Government Accounting Standard (IPSAS-based)
Objective: Budget Control + Fund Accountability + Transparency
Type:      Accrual + Fund Accounting Hybrid
Dimensions (7):
  1. Fund (แหล่งของเงิน)
  2. Department (หน่วยงาน)
  3. Program (แผนงาน)
  4. Project (โครงการ/ผลผลิต)
  5. Account (รายการบัญชี)
  6. Activity (กิจกรรม)
  7. Source of Fund

Reporting: Financial Position, Operations, Cash Flow, Budget Execution
```

### ERP — Commercial Accounting
```
Standard:  IFRS / GAAP / Thai GAAP
Objective: Profitability, Performance, Tax optimization
Type:      Accrual
Dimensions (flexible):
  - Company / Business Unit
  - Cost Center / Profit Center
  - Segment / Region

Reporting: P&L, Balance Sheet, Cash Flow Statement
```

---

## 6. Revenue — Treasury Control vs Business Revenue

### GFMIS Revenue (RP Module)
```
รับเงิน (Bill Payment/EDC/QR/Cash)
    → บันทึกในระบบ (นส.01)
    → นำส่งคลัง (Pay-in GFMIS / KTB Corp.)
    → GL บันทึกอัตโนมัติ

Rule: รายได้แผ่นดิน = ของรัฐ ต้องนำส่งคลัง
Revenue Types: RA (รายได้แผ่นดิน), RB (รายได้ท้องถิ่น), RC (นอกงบ), RD (เงินฝาก)
```

### ERP Revenue
```
Invoice → Payment → Deposit to Company Bank
    → AR Module → GL Posting

Rule: Revenue belongs to the company
No mandatory remittance to external treasury
```

---

## 7. Fixed Assets

### GFMIS FA
| Feature | Detail |
|---------|--------|
| Threshold | ≥ 10,000 บาท (รัฐบาลกำหนด) |
| Classification | Government Standard (Mandatory) |
| Auto-creation | จาก PO/AP (ครุภัณฑ์) |
| Focus | Compliance + Audit + Central Reporting |
| Depreciation | ตาม CGD Standard |

### ERP FA
| Feature | Detail |
|---------|--------|
| Threshold | ตามนโยบายองค์กร (ยืดหยุ่น) |
| Classification | Configurable by company |
| Focus | Depreciation Optimization + Tax Strategy |
| Depreciation | Multiple methods (SL, DB, MACRS) |

---

## 8. User Access & Control

### GFMIS
```
Strict 3-level Segregation:
  Requestor (บันทึก: xxxxxx10)
  ≠ Approver Level 1 (อม.01: xxxxxx01)
  ≠ Approver Level 2 (อม.02: xxxxxx02)

Central UAM (User Access Management)
Mandatory Authentication: Soft Token / ThaID
Password: Change every 3 months (System Lock if not)
Audit Log: All access tracked
```

### ERP
```
Flexible Role Design (configured by organization)
Internal IT manages access
Authentication: varies by implementation
Segregation: depends on organization policy
```

---

## 9. Reporting & Analytics

### GFMIS MIS
| Feature | Detail |
|---------|--------|
| Purpose | Government Reporting + Audit/Transparency |
| Format | Predefined Government Standards |
| Customization | Limited |
| Users | Agency / Central / Committee levels |
| Examples | Budget Execution Report, Cost per Output |

### ERP Analytics
| Feature | Detail |
|---------|--------|
| Purpose | Business Insight + Strategy |
| Format | Fully customizable |
| Tools | SAP BW, Oracle OTBI, Power BI |
| Customization | High |
| Examples | P&L Dashboard, Sales Analytics |

---

## 10. System Architecture

### GFMIS
```
One National System:
- All government agencies use same platform
- Managed by CGD (กรมบัญชีกลาง)
- Centralized data repository

External Integrations (National):
- e-GP (government procurement)
- KTB Corporate Online (banking)
- BOT BAHTNET/SMART (payment clearing)
- PromptBiz / e-Tax (tax receipts)
- ThaID / Paotang (authentication)
```

### ERP
```
Per-Organization System:
- Each company/agency has own instance
- Managed by internal IT
- Organization-specific data

External Integrations (as needed):
- Banking: depends on bank
- Tax: depends on configuration
- Procurement: depends on industry
```

---

## 11. Process Rigidity

### GFMIS = Rigid but Controlled
```
Cannot skip steps → Every step has legal basis
Cannot customize easily → National standard
Cannot pay outside system → CGD controls
All transactions logged → Full audit trail
Every deviation requires → Formal approval/waiver
```

### ERP = Flexible but Requires Governance
```
Configurable workflow → Risk: inconsistency if misconfigured
Custom approval rules → Risk: control gaps without proper design
Multiple payment methods → Risk: requires strong policies
Highly customizable → Risk: over-customization = hard to maintain
```

---

## Integration Strategy: ERP + GFMIS

### Architecture Pattern
```
┌──────────────────────────────────────┐
│  ERP (Oracle Cloud / SAP S/4 HANA)  │
│  Front-end Operational System        │
│  • Procurement (PR → PO → GR)       │
│  • Project Management                │
│  • Asset Management (draft)          │
│  • AP Invoice (draft)                │
└───────────────┬──────────────────────┘
                │
        IEG (Information Exchange Gateway)
        CGD Standard: XML/JSON API
                │
        Integration Layer:
        • Budget Sync (Real-time Check)
        • Document Reference Mapping
        • Vendor Master Sync
        • Payment Confirmation
                │
┌───────────────▼──────────────────────┐
│  GFMIS (New GFMIS Thai)             │
│  Back-end Financial Control          │
│  • FM Budget Hard Stop               │
│  • PO Legal Commitment               │
│  • AP Direct Payment → CGD → BOT   │
│  • GL Accrual Posting (Auto)         │
│  • FA Government Standard            │
│  • MIS Government Reporting          │
└──────────────────────────────────────┘
```

### Integration Focus Points (5 Critical)

1. **Budget Synchronization**
   - ERP Commitment Must = GFMIS FM Reservation
   - Real-time check BEFORE posting in ERP
   - Budget coding: 7-dimension must match exactly

2. **Document Reference Mapping**
   - ERP PO Number ↔ GFMIS PO (เลขที่ใบสั่งซื้อ)
   - ERP Invoice ↔ GFMIS เอกสารขอเบิก
   - e-GP Contract No. ↔ GFMIS สัญญา
   - Avoid duplicate reference numbers

3. **Vendor Master Synchronization**
   - ERP Supplier Master ↔ GFMIS Vendor Groups 1000-8000
   - TIN (เลขผู้เสียภาษี) = Primary Key
   - Bank account must be same in both systems
   - GFMIS Vendor ID ≠ ERP Vendor ID → need mapping table

4. **Payment Confirmation**
   - ERP cannot pay independently (must go through GFMIS)
   - After GFMIS Run Payment → BOT → Bank → ERP Clearing
   - BAHTNET (≥2M, D+2) vs SMART (<2M, D+3)

5. **Real-time Budget Validation**
   - ERP calls GFMIS API before creating PO
   - Response: Approved / Rejected (with reason)
   - Timeout handling: if GFMIS unavailable → ERP holds

### Common Integration Pitfalls
```
❌ ERP pays vendor directly (bypassing GFMIS) → Not allowed
❌ Budget coded differently in ERP vs GFMIS → Mismatch = Failed
❌ Vendor TIN not matched → Payment rejected
❌ PO Reference duplicated → GL posting error
❌ No carry-forward in GFMIS before year-end → Budget lapsed
❌ Customizing GFMIS workflow → Not possible (National Standard)
```

---

## Summary Quick Reference Card

```
┌─────────────────┬──────────────────┬──────────────────┐
│ Topic           │ GFMIS            │ ERP              │
├─────────────────┼──────────────────┼──────────────────┤
│ Purpose         │ Control          │ Efficiency       │
│ Budget          │ Hard Stop/Legal  │ Optional/Config  │
│ Payment         │ CGD Centralized  │ Org Decentralized│
│ Procurement     │ e-GP/Law-driven  │ Business-driven  │
│ Accounting      │ IPSAS/Fund       │ IFRS/Commercial  │
│ Assets          │ ≥10K/Gov Std     │ Flexible         │
│ Users           │ National System  │ Per-Organization │
│ Revenue         │ Must Remit       │ Org Keeps        │
│ Flexibility     │ Low              │ High             │
│ Audit Trail     │ Mandatory/Full   │ Depends on Setup │
└─────────────────┴──────────────────┴──────────────────┘

Golden Rule for Integration:
ERP = Operational Front-end
GFMIS = Financial Control Back-end
NEVER bypass GFMIS for government payment
```
