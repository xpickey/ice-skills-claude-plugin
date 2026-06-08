# Oracle Cloud Architecture สำหรับภาครัฐไทย

## Oracle OCI Government Cloud Design Principles

### 1. Data Residency & Sovereignty
```
สำหรับหน่วยงานรัฐไทย:
├── Primary Region: ap-singapore-1 (หรือ Thailand Region เมื่อพร้อม)
├── DR Region: ap-sydney-1 หรือ ap-tokyo-1
└── Data Classification:
    ├── ข้อมูลสาธารณะ → Standard OCI
    ├── ข้อมูลราชการลับ → Dedicated Region / Government Cloud
    └── ข้อมูล CII → Sovereign Cloud (On-premise OCI หรือ Dedicated)
```

### 2. Security Architecture (ISO 27001/กมช. Cloud Standard 2567)
```
Internet
    │
    ▼
[WAF / DDoS Protection]
    │
    ▼
[OCI Load Balancer (Public)]
    │
    ▼
[DMZ Subnet]
├── Web Application Tier
│
[Private Subnet - Application]
├── Oracle ERP Cloud (HTTPS)
├── Oracle EPM Cloud
└── Integration Layer (API Gateway)
    │
[Private Subnet - Database]
├── Oracle Autonomous Database
├── Oracle DB System (BYOL)
└── Oracle Data Guard (Standby)
    │
[OCI Vault] ← Key Management (TDE Keys)
```

### 3. Identity & Access Management (IAM)
- **Oracle Identity Cloud Service (IDCS)** → SSO สำหรับ Oracle Cloud Applications
- **OCI IAM** → สิทธิ์การเข้าถึง Infrastructure
- **Integration กับ AD/LDAP** → ใช้ SAML 2.0 Federation
- **MFA Requirement** → บังคับสำหรับ privileged accounts
- **เชื่อมกับ GFMIS Access Control** → ตาม Policy หนังสือ กค.

## Oracle ERP Cloud – Government-Specific Configuration

### Chart of Accounts (COA) สำหรับภาครัฐไทย
```
Segment 1: Company (หน่วยงาน) - 5 digits
Segment 2: Department (กอง/ฝ่าย) - 4 digits  
Segment 3: Fund (แหล่งเงิน) - 3 digits
           100 = งบประมาณรายจ่าย
           200 = เงินนอกงบประมาณ
           300 = เงินกู้
Segment 4: Program (แผนงาน) - 6 digits (ตาม GFMIS)
Segment 5: Account (บัญชี) - 6 digits (ตามผังบัญชีภาครัฐ)
Segment 6: Intercompany (0000 = ไม่ใช่รายการระหว่างหน่วยงาน)
```

### Fiscal Calendar Setup
```sql
-- Oracle ERP: Thai Government Fiscal Year
Period Name: FY2568
Start Date: 01-OCT-2024  
End Date: 30-SEP-2025
Period Type: Month (12 periods)
```

### Budgetary Control Configuration
```
Enable Budgetary Control: Yes
Budget Level: Project/Task (ระดับแผนงาน/โครงการ)
Funds Check Level: Advisory (แจ้งเตือน) หรือ Absolute (บังคับ)
Budget Calendar: Thai Fiscal Year
```

## Oracle EPM Cloud – MTEF Implementation

### Medium-Term Expenditure Framework (3 Years)
ตาม มาตรา 24(3) พรบ.วิธีการงบประมาณ + พรบ.วินัยการเงินการคลัง มาตรา 13

```
EPM Planning Hierarchy:
├── Country Level (กรอบวงเงินงบประมาณรวม)
│   ├── Ministry Level (กระทรวง)
│   │   ├── Department Level (กรม)
│   │   │   ├── Program (แผนงาน)
│   │   │   └── Budget Item (รายการงบประมาณ)
│   │   └── Budget Category
│   │       ├── Personnel (งบบุคลากร)
│   │       ├── Operating (งบดำเนินงาน)
│   │       └── Capital (งบลงทุน)
└── Scenario
    ├── Current Year Budget
    ├── Year 1 Projection
    ├── Year 2 Projection
    └── Year 3 Projection
```

## Oracle Database Configuration สำหรับ GFMIS Integration

### Data Integration Patterns
```
GFMIS → Oracle ERP Cloud
├── Method 1: File-based (CSV/XML) via SFTP
├── Method 2: REST API (New GFMIS Thai)
└── Method 3: Oracle Integration Cloud (OIC)

Key Interfaces:
1. GL Journal Import (จาก GFMIS → ERP GL)
2. Supplier (Vendor Master) Sync
3. Payment Reconciliation
4. Budget Consumption Update
```

### DBA Security Requirements (ภาครัฐ)
```sql
-- Audit Configuration (พรบ.คอมพิวเตอร์ 2560)
AUDIT SELECT, INSERT, UPDATE, DELETE 
ON financial_transactions BY ACCESS;

-- TDE Wallet (ข้อมูลทางการเงิน)
ADMINISTER KEY MANAGEMENT SET KEYSTORE OPEN
IDENTIFIED BY "wallet_password";

-- Data Masking (สำหรับ Non-Prod environments)
-- ห้ามใช้ข้อมูลจริงใน Dev/Test ตาม PDPA
BEGIN
  DBMS_DATA_MASKING.MASK_DATA(
    table_name => 'CITIZEN_DATA',
    policy_name => 'PDPA_MASK_POLICY'
  );
END;
```

### Backup & Recovery Standards (กมช. Cloud Standard 2567)
| ระดับระบบ | RPO | RTO | วิธีการ |
|-----------|-----|-----|---------|
| CII (ระบบวิกฤต) | ≤ 1 ชม. | ≤ 4 ชม. | Oracle Data Guard + RMAN |
| ระบบสำคัญ | ≤ 4 ชม. | ≤ 8 ชม. | RMAN + Oracle Backup Cloud Service |
| ระบบทั่วไป | ≤ 24 ชม. | ≤ 24 ชม. | Daily Backup + Object Storage |
