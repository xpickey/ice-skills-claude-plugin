# GFMIS Procedures — ขั้นตอนปฏิบัติงานฉบับสมบูรณ์ (Consulting Grade)
## อ้างอิง: กรมบัญชีกลาง + ระเบียบ 2562 + หนังสือเวียนที่เกี่ยวข้อง

---

## ภาพรวม End-to-End Business Process

```
Budget → Procurement → Payment → Accounting → Reporting
FM       PO             AP         GL            MIS

1. FM  — จัดสรรงบประมาณ (Budget Allocation)
2. PO  — สร้าง PO + ผูกพันงบประมาณ (Commitment)
3. PO  — รับสินค้า/บริการ (Goods Receipt / Service Acceptance)
4. AP  — บันทึกใบแจ้งหนี้ + เบิกจ่ายเงิน (Invoice + Payment)
5. GL  — บันทึกบัญชีอัตโนมัติ (Auto Posting)
6. FA  — บันทึกสินทรัพย์ (ถ้าเป็นครุภัณฑ์ ≥ 10,000 บาท)
7. MIS — รายงานสำหรับผู้บริหาร (Dashboard + Analytics)
```

---

## Module 1: FM — Fund Management (Budget Control)

### 1.1 โครงสร้างงบประมาณ (Budget Structure)

```
6 มิติ (Multi-Dimensional Budget Classification):
1. Agency Code        — รหัสหน่วยงาน (5 หลัก: MMNNN)
2. Budget Unit Code   — รหัสหน่วยรับงบประมาณ (10 หลัก)
3. Fund Source Code   — รหัสแหล่งของเงิน (7 หลัก: YY BB XXX)
4. Budget Type        — รหัสงบประมาณ (20 หลัก)
5. Commitment Item    — รหัสรายการผูกพันงบประมาณ
6. Area Code          — รหัสพื้นที่
```

### 1.2 ประเภทงบรายจ่าย

| รหัส | หมวดงบ | IT ที่เกี่ยวข้อง | รหัสผูกพัน |
|------|--------|----------------|-----------|
| 1XX | งบบุคลากร | เงินเดือน IT Staff | 5000 |
| 2XX | งบดำเนินงาน | Cloud SaaS, License รายปี, Maintenance | 5000 |
| 310/311/312 | งบลงทุนครุภัณฑ์ | Hardware, Server, Network | 1206XX |
| 320/321/322 | งบลงทุนที่ดิน/สิ่งปลูกสร้าง | Data Center | 1204/1208 |
| 410/420 | เงินอุดหนุน | IT อุดหนุนแก่หน่วยงานอื่น | 5000 |
| 500 | งบรายจ่ายอื่น | ค่าใช้จ่ายพิเศษ | 5000 |

### 1.3 เอกสาร FM สำคัญ

| เอกสาร | หน้าที่ | ขั้นตอน |
|--------|---------|---------|
| ขงป.01 | สร้าง/ค้นหา/แก้ไขข้อมูลหลักรหัสงบประมาณ | CGD สร้างให้ |
| อง.03 | โอน/เปลี่ยนแปลงงบประมาณโดยหน่วยเบิกจ่าย | สร้าง → ค้นหา → ยกเลิก |
| สง.01 | สำรองเงิน — เงินปัจจุบัน (กันเงินเหลื่อมปี) | สร้าง/แก้ไข/ยกเลิก |
| สง.02 | รายการเอกสารสำรองเงิน (List) | ขยายเวลาเบิกจ่าย |
| สง.03 | ยกเลิกเอกสารสำรองเงิน (List Cancel) | ยกเลิกทั้งหมด |
| อพ.01 | ยืนยันเอกสารสำรองเงิน (Confirm) | CGD/คลัง ยืนยัน |
| บท.01 | จัดทำข้อมูลเบิกแทนกัน (Request) | สร้าง/แสดง/แก้ไข/ยกเลิก |
| อบ.01 | ยืนยันรายการเบิกแทน (Confirm Request) | หน่วยงานที่เบิกแทน |
| อบ.02 | รับรายการเบิกแทน (Accept Request) | หน่วยงานที่รับเบิกแทน |
| บท.04 | คืนงบประมาณเบิกแทน (Return Request) | |
| อบ.03/04 | ยืนยัน/รับการคืนเบิกแทน | |

### 1.4 Key Features — Budget Control

- **Real-time Hard Stop**: ระบบปฏิเสธอัตโนมัติถ้างบประมาณไม่พอ (ก่อนสร้าง PO/AP)
- **Budget Reservation**: ผูกพันงบ (Commitment) ตั้งแต่สร้าง PO
- **Multi-dimensional**: รายงาน Budget vs. Actual ได้หลายมิติ
- **Carry-forward**: กันเงินเหลื่อมปี 6+6 เดือน (ม.43 พรบ.วิธีการงบ 2561)

### 1.5 รายงาน FM

| รายงาน | ความหมาย |
|--------|----------|
| NFMA55 | แสดงยอดงบประมาณตามหน่วยรับงบประมาณ |
| NFMBB_TRN_RT01 | รายงานการโอน/เปลี่ยนแปลงงบประมาณ |
| NFMA60 | เอกสารสำรองเงินสำหรับส่วนราชการ |
| NFMA60CX | เอกสารสำรองเงิน — มีข้อมูลสัญญา |
| NFMSUB_AG_RPT_0001 | ข้อมูลหลักรายการเบิกแทน |

---

## Module 2: PO — Procurement (Purchasing Order)

### 2.1 End-to-End PO Process

```
1. Vendor Master Setup (สร้าง/ค้นหา Vendor)
2. รับข้อมูลจาก e-GP (เลขสัญญา/โครงการ/ตรวจรับ)
3. สร้าง PO (บส.01) → ระบบ FM ตรวจสอบ/จองงบประมาณ
4. ตรวจรับสินค้า/งาน (K=ตรวจในระบบ GF / S,I=ไม่ต้องตรวจในระบบ)
5. กันเงินและขยายเวลาเบิกจ่าย (ถ้าข้ามปีงบประมาณ)
6. บันทึกบัญชีอัตโนมัติ → GL / FA (ถ้าครุภัณฑ์) / AP (เบิกจ่าย)
```

### 2.2 Integration Flow

```
e-GP
├── Tax ID ผู้ขาย
├── เลขที่คุมสัญญา
├── เลขที่โครงการ
└── เลขที่คุมตรวจรับ
    ↓ (ดึงข้อมูลอัตโนมัติ)
PO System (GFMIS)
├── Vendor Master Sync
├── Budget Check → FM
├── PO Creation (บส.01)
├── Goods Receipt (GR)
└── Auto-post → GL / FA / AP
```

### 2.3 Vendor Master — 8 กลุ่ม (ฉบับครบถ้วน)

| กลุ่ม | ประเภทผู้ขาย | คำค้นหา | รหัส |
|-------|------------|---------|------|
| 1000 | นิติบุคคล (บริษัท/ห้าง/สหกรณ์) | TIN 13 หลัก | 1XXXXXXXXX |
| 2000 | บุคคลธรรมดา (มีรหัสประชาชน) | เลขประชาชน 13 หลัก | 9XXXXXXXXX |
| 3000 | สรก. (เบิกผ่านสรก.แล้วจ่ายต่อ) | รหัสหน่วยเบิกจ่าย 10 หลัก | VYYYYZZZZZ |
| 4000 | สรก. (เบิกเข้าสรก.แล้วจ่ายภายใน) | รหัสหน่วยเบิกจ่าย 10 หลัก | AYYYYZZZZZ |
| 5000 | CGD สร้างให้ (รัฐวิสาหกิจ/สาธารณูปโภค) | รหัสที่ CGD กำหนด | 8XXXXXXXXX |
| 6000 | ผู้ขายต่างประเทศ (นิติบุคคล/บุคคลธรรมดา) | เลขหนังสือเดินทาง | 7XXXXXXXXX |
| 7000 | — | — | — |
| 8000 | อปท. (ไม่รวม กทม./พัทยา) | รหัสที่ CGD กำหนด | C1588XXXXX |

> YYYY = รหัสหน่วยงาน 4 หลัก | ZZZZZ = 5 หลักสุดท้ายหน่วยเบิกจ่าย

**กระบวนการสร้าง/จัดการ Vendor**:
- ค้นหาก่อนเสมอ → หากไม่พบ → สร้างใหม่
- สร้างจาก e-GP: ดึงข้อมูลอัตโนมัติผ่าน Web Online
- หลักฐานที่ต้องส่ง CGD: สำเนาสัญญา + หนังสือรับรองบริษัท + สำเนาบัญชีธนาคาร
- Operations: อนุมัติ / ยืนยัน / แก้ไข / บล็อค / ปลดบล็อค / ลบ

### 2.4 ประเภท PO ตามการส่งมอบ

| ประเภท | ลักษณะ | ตรวจรับในระบบ |
|--------|--------|-------------|
| K (Standard) | ส่งมอบแน่นอน ต้องตรวจรับ | ต้องตรวจรับใน GFMIS |
| S (Blanket) | ส่งมอบแน่นอน ไม่ต้องตรวจ | ไม่ต้องตรวจรับใน GFMIS |
| I (Framework) | ส่งมอบไม่แน่นอน | ไม่ต้องตรวจรับใน GFMIS |

### 2.5 Asset Capitalization Threshold

- **≥ 10,000 บาท**: บันทึกเป็นสินทรัพย์ถาวร (FA Module) → ระบบสร้าง FA Master อัตโนมัติจาก PO
- **< 10,000 บาท**: บันทึกเป็นวัสดุ (Operating Expense)

---

## Module 3: AP — Accounts Payable (Disbursement)

### 3.1 Payment Types

| ประเภทการจ่าย | รหัส/เอกสาร | ลักษณะ |
|-------------|-----------|--------|
| เบิกจ่ายตรงผู้ขาย (PO-based) | ขบ.01 | อ้างอิง PO ในระบบ |
| เบิกจ่ายตรงผู้ขาย (Non-PO) | ขบ.02 | ไม่อ้างอิง PO |
| เงินเดือน/ค่าจ้าง (Payroll) | K0 | Payroll interface |
| เงินยืม (Advance) | K2 | ยืมทดรองราชการ |
| เงินอุดหนุน (Subsidy) | K8 | จ่ายแก่หน่วยงานอื่น |
| เงินประกัน/มัดจำ (Deposit) | K9 | หลักประกันสัญญา |
| เบิกแทนกัน | บท.01 | ผ่านหน่วยงานอื่น |

### 3.2 กระบวนการเบิกจ่ายตรงผู้ขาย (ผ่าน PO — ขบ.01)

```
สร้าง PO → ตรวจรับ PO (GR)
    → บันทึกขอเบิก (ขบ.01) — อ้างอิงเลขที่ PO + เลขที่ใบแจ้งหนี้
    → เลือกงวดเงินที่ต้องการเบิก
    → ระบุประเภทภาษี (กรณีมีภาษีหัก ณ ที่จ่าย)
    → อนุมัติขั้นที่ 1 (อม.01: รหัส xxxxxx01)
    → อนุมัติขั้นที่ 2 (อม.02: รหัส xxxxxx02)
    → CGD/สนง.คลังจังหวัด ตรวจสอบและอนุมัติ
    → Run Payment (15:00 น.)
    → โอนเงิน D+2 (BAHTNET ≥ 2M) หรือ D+3 (SMART < 2M)
```

### 3.3 Document Status Control

```
Draft → Pending Approval → Approved → In Payment → Paid
                         ↓
                      Rejected → Revised → Re-approve
```

**Special Functions**:
- **เบิกเกินส่งคืน**: เงินที่เบิกแล้วแต่ไม่ได้จ่าย → นำส่งคลัง
- **Advance Clearing**: ล้างเงินยืมเมื่อกลับจากราชการ
- **Payment Reversal**: ยกเลิกรายการจ่ายที่ผิดพลาด

### 3.4 Run Payment Process

| วันทำการ | เวลา | ระบบ | มูลค่า |
|---------|------|------|-------|
| D+1 | 15:00 | อนุมัติ → Run Payment | ทุกมูลค่า |
| D+2 | 10:00 | **BAHTNET** (ธปท.) | ≥ 2,000,000 บาท |
| D+3 | 10:00 | **SMART** (ธปท.) | < 2,000,000 บาท |

```
CGD Approve → Run Payment
    → ส่งไฟล์ให้ ธปท. (15:00)
    → บัญชีเงินคงคลัง ธปท.
    → BAHTNET / SMART
    → โอนเข้าบัญชีผู้มีสิทธิรับเงิน
```

---

## Module 4: RP — Revenue & Remittance (Receipt Process)

### 4.1 ประเภทรายรับ

| ประเภท | รหัส | ลักษณะ |
|--------|------|--------|
| รายได้แผ่นดิน | RA | รายได้ทั่วไปของรัฐ |
| รายได้ท้องถิ่น | RB | รายได้ขององค์กรปกครองส่วนท้องถิ่น |
| เงินนอกงบประมาณ | RC | เงินที่ไม่ต้องนำส่งคลัง |
| เงินฝากคลัง | RD | เงินมัดจำ/ประกัน |

### 4.2 กระบวนการนำส่งเงินคลัง

```
รับเงิน (Bill Payment/EDC/QR Code/เงินสด/เช็ค)
    → บันทึกจัดเก็บในระบบ (นส.01: รหัส RYYXXXXXXX)
    → นำส่งด้วยใบ Pay-in (GFMIS) → บัญชีเงินฝากคลัง กทม./คลังจังหวัด
    → นำส่งผ่าน KTB Corporate Online
    → KTB ส่ง Statement → GFMIS กระทบยอด (Bank Reconciliation)
```

### 4.3 เอกสาร RP

| เอกสาร | หน้าที่ |
|--------|---------|
| นส.01 | รับเงินของหน่วยงาน (รหัสเอกสาร: RYYXXXXXXX) |
| นส.02-1 | นำส่งเงินแบบผ่านรายการ |
| R1-R4 | Remittance to Treasury (นำส่งคลังแต่ละประเภท) |

### 4.4 Bank Reconciliation

```
GFMIS Statement ↔ KTB Bank Statement
    → ระบบกระทบยอดอัตโนมัติ
    → รายการที่ไม่ตรง → ตรวจสอบและปรับปรุง
    → รายงานการกระทบยอดประจำวัน/เดือน
```

---

## Module 5: FA — Fixed Assets Management

### 5.1 Asset Lifecycle

```
1. ข้อมูลหลักสินทรัพย์ — กำหนดรหัส (12 หลัก)
2. การได้มา — Auto-create จาก PO/AP (≥ 10,000 บาท)
3. Asset Capitalization — โอนจาก CWIP เป็น Fixed Asset
4. Depreciation — คำนวณสิ้นงวด/สิ้นปีบัญชี
5. Asset Transfer — โอนสินทรัพย์ระหว่างหน่วยงาน
6. Asset Disposal — ตัดจำหน่าย/ขาย/ทำลาย
7. Reporting — รายงานสินทรัพย์คงเหลือ
```

### 5.2 Asset Categories

| ประเภท | เกณฑ์ทุน | อายุการใช้งาน (โดยทั่วไป) |
|--------|---------|--------------------------|
| ที่ดิน | ไม่มีเกณฑ์ | ไม่คิดค่าเสื่อม |
| อาคาร/สิ่งปลูกสร้าง | ≥ 10,000 บาท | 20-50 ปี |
| ครุภัณฑ์คอมพิวเตอร์/IT | ≥ 10,000 บาท | 5-7 ปี |
| ครุภัณฑ์สำนักงาน | ≥ 10,000 บาท | 5-10 ปี |
| ยานพาหนะ | ≥ 10,000 บาท | 10 ปี |
| โครงสร้างพื้นฐาน | ≥ 10,000 บาท | 10-30 ปี |

### 5.3 IT Asset Classification

| รายการ | การจัดประเภท | GL Posting |
|--------|-----------|-----------|
| Server / Hardware | สินทรัพย์ถาวร (FA) | ครุภัณฑ์คอมพิวเตอร์ |
| Software License (Perpetual) | สินทรัพย์ไม่มีตัวตน (Intangible) | งบลงทุน |
| Software License (Subscription) | ค่าใช้จ่ายล่วงหน้า | งบดำเนินงาน |
| Cloud SaaS | Operating Expense | งบดำเนินงาน 2XX |
| Custom Development | สินทรัพย์ไม่มีตัวตน | งบลงทุน |
| Annual Maintenance | Operating Expense | งบดำเนินงาน 2XX |

---

## Module 6: GL — General Ledger

### 6.1 Document Types

| ประเภท | ความหมาย | แหล่งที่มา |
|--------|---------|----------|
| JV | Journal Voucher — การปรับปรุงบัญชีที่ไม่ใช่เงินสด | Manual Entry (บช.01) |
| JR | Journal Revenue — รายการที่เกี่ยวกับเงินสด | Manual Entry (บช.02) |
| PP | Payment Posting — บันทึกการจ่ายเงิน | Auto จาก AP |
| RE | Revenue Entry — บันทึกรายรับ | Auto จาก RP |
| GR | Goods Receipt — บันทึกรับสินค้า | Auto จาก PO |
| FA | Fixed Asset — บันทึกสินทรัพย์ + ค่าเสื่อม | Auto จาก FA |

### 6.2 Auto Posting Flow

```
FM (Budget Commitment) → ผูกพันงบเมื่อสร้าง PO
PO (Goods Receipt)     → Dr. Expense/Asset, Cr. GR/IR
AP (Invoice)           → Dr. GR/IR, Cr. AP Payable
AP (Payment)           → Dr. AP Payable, Cr. Cash/Bank
RP (Revenue)           → Dr. Cash, Cr. Revenue
FA (Depreciation)      → Dr. Depreciation Expense, Cr. Accum. Depreciation
```

### 6.3 Accrual Accounting (เกณฑ์คงค้าง)

| รายการ | หลักการ |
|--------|---------|
| รับรู้รายได้ | เมื่อเกิดสิทธิ์ (ไม่ใช่เมื่อรับเงิน) |
| รับรู้ค่าใช้จ่าย | เมื่อใช้ประโยชน์ (ไม่ใช่เมื่อจ่ายเงิน) |
| สินทรัพย์ถาวร | บันทึกต้นทุน + คำนวณค่าเสื่อม |
| หนี้สิน | บันทึกเมื่อเกิดพันธะผูกพัน |

### 6.4 COA (Chart of Accounts) — Government Standard

```
Dimension Structure:
1. Fund (แหล่งของเงิน)      — YY BB XXX
2. Department (หน่วยงาน)   — MMNNN
3. Program (แผนงาน)         — BP
4. Project (โครงการ/ผลผลิต) — PPPP
5. Account (รายการบัญชี)    — GL Account
6. Activity (กิจกรรม)       — ย่อยของโครงการ
7. Source of Fund           — แหล่งเงิน

Fiscal Calendar: 1 ต.ค. – 30 ก.ย.
```

---

## Module 7: MIS — Financial Analytics & Reporting

### 7.1 ประเภทรายงาน

| ระดับ | รายงาน | ผู้ใช้ |
|------|--------|--------|
| Strategic | งบการเงินรวม (Financial Statements) | ผู้บริหารระดับสูง, CGD |
| Managerial | Budget vs. Actual Dashboard | ผู้บริหาร, CFO |
| Operational | รายงานประจำวัน/สัปดาห์ | เจ้าหน้าที่การเงิน |
| Compliance | รายงานสำหรับ สตง./ผู้ตรวจสอบ | Internal/External Audit |

### 7.2 Financial Statements (IPSAS/Thai Government Standard)

- **Statement of Financial Position** (งบแสดงฐานะทางการเงิน)
- **Statement of Operations** (งบแสดงผลการดำเนินงาน)
- **Cash Flow Statement** (งบกระแสเงินสด)
- **Budget Execution Report** (รายงานการใช้จ่ายงบประมาณ)
- **Cost per Output Report** (ต้นทุนต่อหน่วยผลผลิต)

### 7.3 Key Reports ในระบบ GFMIS

| รหัสรายงาน | ความหมาย | ระดับ |
|-----------|---------|------|
| NFMA55 | ยอดงบประมาณตามหน่วยรับงบ | Agency |
| NFMA60 | เอกสารสำรองเงิน | Agency |
| NFMBB_TRN_RT01 | การโอนงบประมาณ | Agency/Central |
| ZMIRO Report | สรุปรายการขอเบิกเงิน | Agency |
| Web Report (Budget/Cash) | Daily Reconciliation | Agency |
| MIS Dashboard | Executive View | Management |

---

## User Access Management (UAM)

### รหัสผู้ใช้งาน GFMIS (User ID Structure)

```
Format: [หน่วยงาน][หน้าที่][Running]
หลักที่ 10:
  10 = ผู้บันทึกข้อมูล (Data Entry)
  01 = ผู้อนุมัติขั้นที่ 1 (อม.01)
  02 = ผู้อนุมัติขั้นที่ 2 (อม.02)
```

### Segregation of Duties (บังคับ)

```
ผู้บันทึกข้อมูล (xxxxxx10)   ≠   ผู้อนุมัติ (xxxxxx01/02)
ห้ามบุคคลเดียวกันบันทึกและอนุมัติรายการเดียวกัน
```

### Security Requirements

| ข้อกำหนด | รายละเอียด |
|---------|----------|
| Password Policy | เปลี่ยนทุก **3 เดือน** (ไม่เปลี่ยน = ล็อค) |
| Token Renewal | GFMIS Token Key อายุ ~3 ปี |
| Authentication | Soft Token (New GFMIS) / Token Key (เดิม) |
| ThaID | พิสูจน์ตัวตนดิจิทัลในการลงทะเบียน UAM |

---

## การกันเงินเบิกเหลื่อมปี — รายละเอียด

### เงื่อนไข

- มีการก่อหนี้ผูกพันก่อนสิ้นปีงบประมาณ (ก่อน 30 ก.ย.)
- ไม่สามารถเบิกได้ทันสิ้นปีงบประมาณ
- วงเงิน ≥ 100,000 บาท (กรณีทั่วไป)

### Timeline

```
ก่อน 30 ก.ย.  → ก่อหนี้ผูกพัน + ยื่น สง.01 (กันเงิน)
1 ต.ค. – 31 มี.ค. → ระยะเวลาเบิกปกติ (6 เดือน)
31 มี.ค.       → ครบกำหนดปกติ
1 เม.ย. – 30 ก.ย. → ขยายครั้งที่ 2 (ทำความตกลง กค. อีก 6 เดือน)
หลัง 30 ก.ย.  → เงิน Lapse (หมดอายุ ต้องขอ ครม. กรณีพิเศษ)
```

### อ้างอิง: มาตรา 43 พรบ.วิธีการงบประมาณ 2561
- ขยายได้ **ไม่เกิน 6 เดือน** ของปีงบประมาณถัดไป
- ทำความตกลงกับ กค. ขยายได้อีก **ไม่เกิน 6 เดือน**
- โครงการ ≥ 1,000 ล้านบาท → ต้องขอ ครม. อนุมัติล่วงหน้า (ม.26)

---

## IT Project Budget & GFMIS Coding Best Practices

### การจำแนกประเภทงบ IT

| รายการ IT | งบประมาณ | รหัส | ผูกพัน |
|-----------|---------|------|--------|
| Hardware/Server | งบลงทุนครุภัณฑ์ | 310 | 1206XX |
| Cloud SaaS (รายปี) | งบดำเนินงาน | 2XX | 5000 |
| On-Premise License (Perpetual) | งบลงทุนครุภัณฑ์ | 310 | 1206XX |
| Software Subscription (รายปี) | งบดำเนินงาน | 2XX | 5000 |
| Custom Development | งบลงทุน | 310/2XX | 1206XX/5000 |
| Annual Maintenance | งบดำเนินงาน | 2XX | 5000 |
| Data Center/อาคาร | งบลงทุนที่ดิน/สิ่ง | 320 | 1208 |
| Training | งบดำเนินงาน | 2XX | 5000 |
| Consulting/TOR | งบดำเนินงาน | 2XX | 5000 |

### โครงการ IT ข้ามปีงบประมาณ

```
Prerequisite: ก่อหนี้ผูกพัน + กันเงิน (สง.01) ก่อน 30 ก.ย.
โครงการ ≥ 1,000 ล้าน: ขอ ครม. อนุมัติก่อนตั้งงบ (ม.26)
GF-eGP Integration: PO ↔ e-GP Auto-sync (ปีงบ 2569-70)
GFMIS Enhancement: Central Asset Master (ปีงบ 2570-71)
```

---

## การตรวจสอบภายใน (Internal Audit) — Checklist

### Daily Controls

- [ ] ตรวจรายงาน ZMIRO: สรุปรายการขอเบิก vs. ข้อมูลขอเบิก
- [ ] ตรวจรายงาน Web Report: เงินสดคงเหลือ GFMIS vs. รายงานนอกระบบ
- [ ] กรณีพบข้อคลาดเคลื่อน: พิสูจน์ยอด → เสนอหัวหน้าลงนาม → เก็บรักษา

### Monthly Controls

- [ ] Bank Reconciliation: RP Statement vs. KTB Statement
- [ ] Budget Utilization Report: Budget vs. Actual by Program
- [ ] Vendor Master Review: TIN ถูกต้อง + บัญชีธนาคารเป็นปัจจุบัน
- [ ] Open PO Review: PO ค้างนานเกิน 6 เดือน → พิจารณาสลาย/ยกเลิก

### Annual Controls

- [ ] FA Physical Count vs. FA Register ในระบบ
- [ ] Year-end Carry-forward: ทุก PO/สัญญาที่ข้ามปี → สร้าง สง.01 ก่อน 30 ก.ย.
- [ ] Password Reset Cycle: ทุกผู้ใช้งานเปลี่ยน Password ครบทุก 3 เดือน
- [ ] Token Key Renewal: ตรวจสอบอายุ Token ทุกรายก่อนหมดอายุ
