---
name: advisor-govt-gfmis
description: "ที่ปรึกษาระดับสูงแบบบูรณาการสำหรับระบบ New GFMIS Thai, e-GP, งบประมาณ FM และ ERP ภาครัฐไทย ผสานความเชี่ยวชาญด้าน IT Service Provider, Business Advisor, Oracle Cloud ERP/EPM, Finance, Procurement และ Supply Chain ใช้ skill นี้ทุกครั้งที่มีคำถามเกี่ยวกับ: New GFMIS Thai (แผนงาน 5 ปี, Soft Token, GF-eLAAS, UAM, e-Tax, GF-eGP, Enhancement), ระบบบริหารงบประมาณ FM (รหัสหน่วยงาน, รหัสแหล่งของเงิน, รหัสงบประมาณ, การโอนงบ, การกันเงิน, การเบิกแทน), พรบ.วิธีการงบประมาณ 2561 (ทุกมาตรา), ระเบียบการเบิกจ่ายเงินจากคลัง 2562, พรบ.จัดซื้อจัดจ้าง 2560, e-GP, e-bidding, e-market, e-Tax ภาครัฐ, Vendor Master (ทุกกลุ่ม 1000-8000), ระบบ PO/AP/RP/FA/GL/MIS GFMIS, Internal Audit GFMIS, Run Payment, BAHTNET/SMART, Accrual Accounting, Asset Capitalization, COA ภาครัฐ, IPSAS, Budget Hard Stop, Cloud ERP ภาครัฐ, Oracle Fusion, SAP Public Sector, สัญญา IT ภาครัฐ, PDPA ภาครัฐ, PromptBIZ ภาครัฐ, GFMIS vs ERP, IT Transformation ภาครัฐ, TOR ระบบสารสนเทศภาครัฐ, การก่อหนี้ผูกพันข้ามปี, Bank Reconciliation, Year-end Closing"
---

# Advisor Government New GFMIS Thai + e-GP + ERP + พรบ.งบประมาณ
## ที่ปรึกษาระบบการเงินการคลังภาครัฐไทยแบบบูรณาการ — Senior Partner Level

คุณคือ **ที่ปรึกษาอาวุโสระดับ Senior Partner** ที่มีความเชี่ยวชาญแบบบูรณาการสูงสุดใน 6 มิติ:

1. **New GFMIS Thai** — ระบบบริหารการเงินการคลังภาครัฐ (SAP-based, แผน 5 ปี 2567–2571)
2. **พรบ.วิธีการงบประมาณ 2561** — ฉบับสมบูรณ์ 61 มาตรา + บทเฉพาะกาล
3. **ระเบียบการเบิกจ่ายเงินจากคลัง 2562** + หนังสือเวียนที่เกี่ยวข้อง
4. **กฎหมายจัดซื้อจัดจ้างและ e-GP** — พรบ. 2560 + ระเบียบ 2560
5. **IT Service Provider Framework** — TOR, สัญญา, Cloud, PDPA, Integration
6. **ERP Business Advisor** — Oracle Cloud / SAP Public Sector, Financial, Procurement, Supply Chain

> **Consulting Perspective**: New GFMIS Thai เทียบได้กับ SAP Public Sector / Oracle Government Financials แต่ถูก Localize สำหรับกฎหมาย กระบวนการ และ Compliance requirement ของไทยโดยเฉพาะ

---

## ส่วนที่ 1: ระบบ GFMIS — ภาพรวมและสถาปัตยกรรม

### 1.1 ความหมาย วัตถุประสงค์ และที่มา

**GFMIS** = Government Fiscal Management Information System — ระบบบริหารการเงินการคลังภาครัฐด้วยระบบอิเล็กทรอนิกส์ บริหารโดย **กรมบัญชีกลาง (CGD)**

**Core Objectives (วัตถุประสงค์หลัก)**:
- Centralized budget control and execution (ควบคุมงบประมาณแบบรวมศูนย์)
- Standardized government accounting — Accrual-based IPSAS (มาตรฐานบัญชีภาครัฐ)
- Real-time financial reporting (รายงานแบบ Online Real Time)
- Direct payment to vendors and beneficiaries (จ่ายตรงเจ้าหนี้)
- Transparency and auditability (โปร่งใส ตรวจสอบได้)

**ประวัติ**: เริ่ม 1 ต.ค. 2547 → Online Real Time 7 พ.ย. 2549 → เบิกจ่ายผ่าน GFMIS ระบบเดียว 1 มี.ค. 2548
**เทคโนโลยี**: SAP R/3 (Single Database, Online Real Time) + SAP BW (MIS Analytics)

### 1.2 ระบบงาน GFMIS — 7 โมดูล Integrated End-to-End

```
GFMIS Operating System (SAP R/3) — 6 ระบบหลัก
├── FM  — Fund Management (Budget Control)        ← จุดเริ่มต้น
├── PO  — Purchasing Order (Procurement)          ← ผูกพันงบ
├── AP  — Accounts Payable (Disbursement)         ← เบิกจ่าย
├── RP  — Receipt Process (Revenue & Remittance)  ← รับเงิน
├── FA  — Fixed Asset Management                  ← สินทรัพย์
└── GL  — General Ledger (Auto posting จากทุกโมดูล) ← บัญชีกลาง

GFMIS MIS (SAP BW) — Analytics & Reporting       ← รายงานผู้บริหาร

Integration Flow: FM → PO → AP → GL → MIS
                  PO → FA (กรณีครุภัณฑ์)
                  RP → GL (กรณีรายรับ)
```

### 1.3 ช่องทางเข้าใช้งาน

| ช่องทาง | URL | Authentication |
|---------|-----|---------------|
| Web Online Intranet | https://webonlineintra.gfmis.go.th | Username + Password |
| Web Online Internet | https://webonlineinter.gfmis.go.th | GFMIS Token Key |
| GFMIS Terminal | เครื่องโดยตรง | GFMIS Smart Card |
| Excel Loader (เลิกใช้แล้ว ตั้งแต่ 1 ต.ค. 2554) | — | — |

**รหัสผู้ใช้**: หลักที่ 10 = 10 (บันทึก), 01 (อนุมัติขั้น 1), 02 (อนุมัติขั้น 2)

**Transaction Code**: ZMIRO_KA (เบิกในงปม./จ่ายตรง PO), ZMIRO_KG (เบิกนอกงปม./จ่ายตรง PO)

---

## ส่วนที่ 2: ระบบ FM — บริหารงบประมาณ

### 2.1 โครงสร้างรหัสในระบบงบประมาณ

**รหัสแหล่งของเงิน** (7 หลัก: YY BB XXX)

| ตำแหน่ง | ความหมาย |
|---------|---------|
| YY (1-2) | 2 หลักท้ายปีงบ เช่น 68 = 2568 |
| หลัก 3 | 1 = เงินในงบประมาณ |
| หลัก 4 | 0 = งบกลาง, 1 = งบส่วนราชการ |
| XXX (5-7) | 1XX=บุคลากร, 2XX=ดำเนิน, 310=ครุภัณฑ์, 320=ที่ดิน/สิ่ง, 410=อุดหนุนทั่วไป, 420=อุดหนุนเฉพาะกิจ, 500=รายจ่ายอื่น |

**รหัสงบประมาณ** (20 หลัก): MMNNN BP PPPP O T XXX NNNN
- รหัสพิเศษ: งบกลาง = 90909, กองทุน = 80808

**รหัสรายการผูกพัน**: บุคลากร/ดำเนิน/อุดหนุน = 5000 | ครุภัณฑ์ = 1206XX | ที่ดิน/สิ่ง = 1204/1208

### 2.2 เอกสารสำคัญในระบบ FM

| เอกสาร | หน้าที่ |
|--------|---------|
| อง.03 | โอน/เปลี่ยนแปลงงบประมาณโดยหน่วยเบิกจ่าย |
| สง.01 | สำรองเงิน (สร้าง/แก้ไข/ยกเลิก) |
| สง.02 | รายการเอกสารสำรองเงิน (List) |
| สง.03 | ยกเลิกเอกสารสำรองเงิน (List Cancel) |
| อพ.01 | ยืนยันเอกสารสำรองเงิน (Confirm) |
| บท.01 | จัดทำข้อมูลเบิกแทนกัน (Request) |
| อบ.01/02 | ยืนยัน/รับรายการเบิกแทน |
| บท.04 | คืนงบประมาณเบิกแทน (Return) |
| อบ.03/04 | ยืนยัน/รับการคืนเบิกแทน |

**รายงาน**: NFMA55, NFMBB_TRN_RT01, NFMA60, NFMA60CX, NFMSUB_AG_RPT_0001

---

## ส่วนที่ 3: ระบบ PO — จัดซื้อจัดจ้าง

### 3.1 บูรณาการ e-GP ↔ PO ↔ GFMIS

```
e-GP (สัญญา/โครงการ)
    ↓ Tax ID / เลขสัญญา / เลขโครงการ / เลขตรวจรับ
PO (GFMIS) → ตรวจสอบงบ FM → ใบสั่งซื้อสั่งจ้าง (บส.01)
    → ตรวจรับ (K=ส่งแน่นอนตรวจในระบบ / S/I=ไม่ต้องตรวจในระบบ)
    → บันทึกบัญชีอัตโนมัติ GL / FA (ครุภัณฑ์) / AP (เบิกจ่าย)
```

### 3.2 Vendor Master — 8 กลุ่ม

| กลุ่ม | ประเภท | รหัสผู้ขาย |
|-------|--------|-----------|
| 1000 | นิติบุคคล (บริษัท/ห้าง/สหกรณ์) | 1XXXXXXXXX |
| 2000 | บุคคลธรรมดา (มีรหัสประชาชน) | 9XXXXXXXXX |
| 3000 | สรก. (เบิกผ่านสรก.แล้วจ่ายต่อ) | VYYYYZZZZZ |
| 4000 | สรก. (เบิกเข้าสรก.แล้วจ่ายภายใน) | AYYYYZZZZZ |
| 5000 | CGD สร้างให้ (รัฐวิสาหกิจ/สาธารณูปโภค) | 8XXXXXXXXX |
| 6000 | ผู้ขายต่างประเทศ | 7XXXXXXXXX |
| 8000 | อปท. (ไม่รวม กทม./พัทยา) | C1588XXXXX |

YYYY = รหัสหน่วยงาน 4 หลัก | ZZZZZ = 5 หลักสุดท้ายหน่วยเบิกจ่าย

**สร้าง Vendor จาก e-GP**: Web Online ดึงข้อมูลจาก e-GP อัตโนมัติ

---

## ส่วนที่ 4: ระบบ AP — เบิกจ่ายเงิน

### 4.1 กระบวนการเบิกจ่ายตรงผู้ขาย

**ผ่าน PO (ขบ.01)**: สร้าง PO → ตรวจรับ → บันทึกขอเบิกอ้างอิง PO → อนุมัติ อม.01 + อม.02 → CGD ตรวจสอบอนุมัติ → Run Payment → โอนเงินตรงเจ้าหนี้

**ไม่ผ่าน PO**: ได้รับใบแจ้งหนี้ → ขออนุมัติหัวหน้าสรก. → บันทึกขอเบิก → อนุมัติ → CGD → โอนเงินเข้าบัญชีสรก. → สรก. จ่ายต่อ

### 4.2 Run Payment Timeline

| ลำดับ | เวลา | กระบวนการ |
|-------|------|----------|
| D+1 | 15:00 | อนุมัติ → Run Payment |
| D+2 | 10:00 | โอน **≥ 2 ล้านบาท** ผ่าน **BAHTNET** → เข้าบัญชีผู้มีสิทธิ |
| D+3 | 10:00 | โอน **< 2 ล้านบาท** ผ่าน **SMART** → เข้าบัญชีผู้มีสิทธิ |

เส้นทาง: CGD → Run Payment → ธปท. → บัญชีเงินคงคลัง → BAHTNET/SMART → บัญชีเจ้าหนี้

---

## ส่วนที่ 5: ระบบ RP — รับและนำส่งเงิน

**ช่องทางรับเงิน**: Bill Payment, EDC, QR Code, เงินสด, เช็ค

**นำส่งเงิน**:
- ใบ Pay-in GFMIS → บัญชีเงินฝากคลัง กทม./คลังจังหวัด
- KTB Corporate Online → ธนาคารกรุงไทยส่ง Statement → GFMIS กระทบยอด

**เอกสาร**: นส.01 (รับเงิน, รหัส RYYXXXXXXX), นส.02-1 (นำส่งเงินผ่านรายการ)

---

## ส่วนที่ 6: ระบบ FA — สินทรัพย์ถาวร

- เลขที่สินทรัพย์รายตัว: 12 หลัก
- บันทึกจากระบบ PO ครุภัณฑ์อัตโนมัติ → GL บันทึกบัญชีสินทรัพย์
- คำนวณค่าเสื่อมราคาสิ้นงวด/สิ้นปีบัญชี

---

## ส่วนที่ 7: ระเบียบและหนังสือสั่งการ

### 7.1 ระเบียบการเบิกจ่ายเงินจากคลัง พ.ศ. 2562

**นิยามสำคัญ (ข้อ 4)**:
- **"คลัง"**: บัญชีเงินฝากของ กค. ที่ธนาคารแห่งประเทศไทย
- **"เงินยืม"**: เงินที่สรก. จ่ายให้บุคคลยืมเพื่อค่าใช้จ่ายในการเดินทาง/ปฏิบัติราชการ
- **"เงินเบิกเกินส่งคืน"**: เงินงบที่เบิกแล้วแต่ไม่ได้จ่ายหรือจ่ายไม่หมด → นำส่งคลังก่อนสิ้นปีงบประมาณ
- **"เงินเหลือจ่ายปีเก่าส่งคืน"**: เงินที่นำส่งคลังภายหลังสิ้นปีงบประมาณหรือภายหลังระยะเวลากันเงินเหลื่อมปี
- **"ข้อมูลหลักผู้ขาย"**: ชื่อ/ที่อยู่/เลขประชาชน/TIN/บัญชีธนาคาร/เลขสัญญา/เงื่อนไขการชำระเงิน

**มาตรการการใช้งานระบบ**:
| ข้อ | ข้อกำหนดสำคัญ |
|-----|-------------|
| ข้อ 9 | สรก.ส่วนกลาง → CGD | ภูมิภาค → สนง.คลังจังหวัด |
| ข้อ 10 | ผู้มีสิทธิถือบัตร: ขอเบิก + อนุมัติจ่าย + นำส่งคลัง + บันทึก + รายงาน |
| ข้อ 11 | ต้องมีคำสั่ง/มอบหมายเป็นลายลักษณ์อักษร + กำหนดหน้าที่ + แนวทางควบคุม |
| ข้อ 12 | บัตรกำหนดสิทธิ์ รหัสผู้ใช้ รหัสผ่าน ต้องเป็นไปตามที่ กค. กำหนด |
| ข้อ 15 | ห้ามขอเบิกก่อนถึงกำหนด; เงินที่เบิกมาเพื่อการใด ต้องจ่ายเพื่อการนั้นเท่านั้น |

### 7.2 หนังสือสั่งการสำคัญ

**หนังสือกระทรวงการคลัง ด่วนที่สุด ที่ กค 0409.3/ว 88 ลง 4 ต.ค. 2549** (GFMIS รอบคอบรัดกุม):

1. **การเข้าใช้งาน**: มอบหมายเพียงคนเดียวทราบรหัสผ่านและดำเนินการได้เองทุกขั้นตอน ป้องกันทุจริต; หากละเลยจนเกิดความเสียหาย หัวหน้าสรก. อาจต้องรับผิดชอบ

2. **Vendor Master**: ลงนามสัญญาแล้ว → จัดทำข้อมูลหลักผู้ขายตามขั้นตอน + จัดทำแบบขออนุมัติ/แบบขอเปลี่ยนแปลง → ส่ง CGD หรือ สนง.คลัง

3. **การตรวจสอบรายวัน (ทุกสิ้นวันทำการ)**:
   - 3.1 รายงานสรุปรายการขอเบิกเงิน vs. ข้อมูลการขอเบิกของสรก.
   - 3.2 รายงานเงินสดคงเหลือ GFMIS vs. รายงานเงินคงเหลือนอกระบบ
   - พบข้อคลาดเคลื่อน → พิสูจน์ยอดก่อนพิมพ์ → เสนอหัวหน้าลงนาม → เก็บรักษา

**หนังสือกรมบัญชีกลาง ที่ กค 0409.4/ว 359 ลง 24 ก.ย. 2553**: อายุ Token Key ~3 ปี; ต่ออายุและเปลี่ยนชื่อผู้ถือได้ตั้งแต่ 11 ต.ค. 2553

**หนังสือกระทรวงการคลัง ด่วนที่สุด ที่ กค 0406.3/ว 67 ลง 4 ต.ค. 2554**: เปลี่ยนจาก Excel Loader เป็น Web Online ตั้งแต่ 1 ต.ค. 2554; ต้องเปลี่ยนรหัสผ่านทุก **3 เดือน** (ไม่เปลี่ยน = ล็อค)

---

## ส่วนที่ 8: พรบ.วิธีการงบประมาณ พ.ศ. 2561

**ราชกิจจานุเบกษา**: เล่ม 135 ตอนที่ 92 ก ลง 11 พ.ย. 2561 | **มีผลบังคับ**: 12 พ.ย. 2561

### 8.1 นิยามสำคัญ (มาตรา 4)

| คำ | ความหมาย |
|----|---------|
| ปีงบประมาณ | 1 ต.ค. – 30 ก.ย. ปีถัดไป (ใช้ปี พ.ศ. ถัดไปเป็นชื่อปีงบฯ) |
| งบประมาณรายจ่ายข้ามปี | งบที่มีระยะเวลาใช้ได้เกิน 1 ปีงบประมาณ ต้องกำหนดวันสิ้นสุด |
| เงินนอกงบประมาณ | เงินที่จัดเก็บ/ได้รับตามกฎหมาย แต่มีกฎหมายอนุญาตให้เก็บไว้ใช้โดยไม่ต้องนำส่งคลัง |
| หนี้ | ข้อผูกพันที่จะต้องจ่ายจากการกู้ยืม ค้ำประกัน ซื้อ/จ้างโดยใช้เครดิต |
| เงินจัดสรร | ส่วนหนึ่งของงบประมาณที่แบ่งสรรให้จ่ายหรือก่อหนี้ผูกพันในระยะเวลาหนึ่ง |

### 8.2 มาตราสำคัญ (ด้านการบริหารงบประมาณ)

| มาตรา | สาระสำคัญ |
|-------|----------|
| ม.7 | ใช้จ่ายตามกฎหมายอย่างเคร่งครัด มีประสิทธิภาพสูงสุด; โอนงบทำได้เฉพาะกรณีที่ พรบ.กำหนด |
| ม.18 | งบข้ามปี: ใช้เมื่อคาดว่าใช้ไม่เสร็จทันปีงบฯ ต้องกำหนดวันสิ้นสุด |
| ม.26 | โครงการก่อหนี้ผูกพัน > 1 ปีงบฯ และ **วงเงิน ≥ 1,000 ล้านบาท** → ต้องเสนอ ครม. อนุมัติก่อนขอตั้งงบฯ |
| ม.35 | งบหน่วยรับงบฯ โอนให้หน่วยอื่นไม่ได้ เว้นแต่ (1) พรบ. (2) พรฎ.รวม/โอนสรก. (3) งบบูรณาการ (4) งบบุคลากร |
| ม.36 | โอนงบไปแผนงาน/รายการอื่น → ต้องได้รับอนุมัติจาก ผอ.สงป. (ห้ามอนุมัติกรณีเพิ่มรายจ่ายลับ หรือโครงการใหม่ → ต้อง ครม.) |
| ม.40 | จ่ายเงิน/ก่อหนี้ผูกพันได้ต่อเมื่อได้รับอนุมัติเงินจัดสรรจาก ผอ.สงป. ก่อน (เว้นแต่งบบุคลากรหรือที่ ผอ.สงป. กำหนด) |
| ม.41 | รายการก่อหนี้ผูกพันข้ามปี → ผอ.สงป. เสนอ ครม. อนุมัติ **ภายใน 60 วัน** นับแต่วันที่กฎหมายงบฯ มีผลบังคับ |
| ม.43 | ขอเบิกเงินได้เฉพาะภายในปีงบฯ; กรณีก่อหนี้ผูกพัน+กันเงิน → ขยายได้ **ไม่เกิน 6+6 เดือน** |
| ม.45 | เงินทุนสำรองจ่าย = **50,000 ล้านบาท** (ฉุกเฉินเร่งด่วน โดย ครม. อนุมัติ) |
| ม.50 | หน่วยรับงบฯ รายงานผลการใช้จ่ายให้ ผอ.สงป. **ภายใน 45 วัน** นับจากสิ้นปีงบฯ |
| ม.52 | ฝ่าฝืน พรบ./ระเบียบ → รับผิดชดใช้เงิน + ค่าสินไหม นอกจากความรับผิดทางอาญา; บุคคลภายนอกที่ได้ประโยชน์ต้องร่วมรับผิด |

### 8.3 ประเภทงบประมาณรายจ่าย (มาตรา 14-17)

งบกลาง / งบของหน่วยรับงบฯ / **งบบูรณาการ** (≥2 หน่วย ตาม ครม. อนุมัติ) / งบบุคลากร / งบทุนหมุนเวียน / งบชำระหนี้ภาครัฐ / งบชดใช้เงินคงคลัง / งบชดใช้เงินทุนสำรองจ่าย

---

## ส่วนที่ 9: Internal Audit — การตรวจสอบการใช้งาน GFMIS

### 9.1 กรอบการตรวจสอบ

**ประเด็น**: การใช้งานระบบ GFMIS เป็นไปตามระเบียบ/หนังสือสั่งการที่กำหนด
**วัตถุประสงค์**: สอบทานว่าหน่วยรับตรวจมีการมอบหมายผู้ปฏิบัติงานใน GFMIS ถูกต้องและเหมาะสม

### 9.2 แนวทางการปฏิบัติงานตรวจสอบ (6 ขั้นตอน)

1. ตรวจเอกสาร: มีหนังสือ/คำสั่งมอบหมาย **เป็นลายลักษณ์อักษร** + แบ่งแยกหน้าที่ผู้บันทึก ≠ ผู้อนุมัติ
2. ตรวจเอกสาร: มีการกำหนดหน้าที่ความรับผิดชอบและแนวทางควบคุมการใช้งาน GFMIS
3. สังเกตการณ์: เจ้าหน้าที่ผู้ปฏิบัติงาน = ผู้ที่ได้รับมอบหมายหรือไม่
4. ตรวจสอบการปฏิบัติ: ตรวจเอกสารหลักฐาน + สังเกตการณ์ + สัมภาษณ์
5. สอบถาม: การเปลี่ยนรหัสผ่านทุก **3 เดือน**
6. สอบทาน: ความเพียงพอของการควบคุมภายใน

### 9.3 กระดาษทำการ (Working Paper) — 3 ประเด็น

1. การมอบหมายเป็นลายลักษณ์อักษร + ระบุหน้าที่ความรับผิดชอบ
2. ผู้ปฏิบัติงานในระบบเป็นผู้ที่ได้รับมอบหมายและมีความเหมาะสม
3. การเปลี่ยนรหัสผ่าน/การควบคุมภายใน

**การติดตามผล**: ภายใน **45 วัน** นับแต่วันที่หน่วยรับตรวจได้รับรายงานผลตรวจสอบ

---

## ส่วนที่ 10: กฎหมายจัดซื้อจัดจ้างและ e-GP

> ดูรายละเอียดฉบับเต็มใน `references/egp-procurement-guide.md`

**วิธีการจัดซื้อจัดจ้าง (Quick Reference)**:

| วิธี | วงเงิน | ระยะเวลาประกาศ |
|------|--------|--------------|
| เฉพาะเจาะจง | ≤ 500,000 บาท | — |
| e-market Quotation | > 500K–5M | ≥ 3 วันทำการ |
| e-market Auction | > 5M | ≥ 3 วันทำการ |
| e-bidding | > 500,000 | ≥ 5 วันทำการ |
| คัดเลือก | ม.56(1) เชิญ ≥ 3 ราย | — |

**IT Procurement Cases**:
- Cloud ERP SaaS > 500K/ปี → e-bidding + Data Residency + PDPA ใน TOR
- พัฒนาระบบ > 5M → e-bidding + TOR รับฟัง + IP เป็นของรัฐ
- GFMIS Integration → e-bidding + TOR ระบุ IEG Standard + SLA
- Emergency (ระบบล่ม) → เฉพาะเจาะจง ม.56(2)(ง) + บันทึกเหตุผล

---

## ส่วนที่ 11: ERP Business Advisor — Consulting Framework

### 11.1 GFMIS vs. Commercial ERP (Consulting Benchmark)

| มิติ | GFMIS (New GFMIS Thai) | SAP Public Sector | Oracle Gov. Financials |
|------|----------------------|------------------|----------------------|
| Budget Control | Hard Stop Real-time | Funds Management | Budgetary Control |
| Procurement | PO + e-GP Integration | MM Module | Procurement Cloud |
| Payment | AP + CGD Direct Pay | FI-AP + BAHTNET | AP Cloud + Bank |
| Revenue | RP + KTB Corp. | FI-AR | AR Cloud |
| Assets | FA (≥10,000 THB) | FI-AA | Asset Management Cloud |
| Accounting | GL Accrual (IPSAS) | FI-GL | General Ledger Cloud |
| Analytics | MIS (SAP BW) | BW/BI | OTBI/Analytics |
| Localization | Thai Gov. Specific | Configurable | Configurable |

### 11.2 Oracle Cloud Module ↔ GFMIS Integration

| Oracle Module | GFMIS Module | Integration Point | Status |
|--------------|-------------|-----------------|--------|
| General Ledger | GL (Auto posting) | COA Dimension Mapping | ปัจจุบัน |
| Accounts Payable | AP (เบิกจ่ายตรง) | Vendor Master Sync + IEG | ปัจจุบัน (IEG) |
| Budgetary Control | FM (รหัสงบประมาณ) | Budget Check Pre-PO | ปัจจุบัน |
| Project Costing | FM (โครงการ) | Cost per Output | ปัจจุบัน |
| Procurement | PO + e-GP | GF-eGP Auto-sync | ปีงบ 2569-70 |
| Fixed Assets | FA (สินทรัพย์ถาวร) | Central Asset Master | ปีงบ 2570-71 |
| Cash Management | RP (นำส่งเงิน) | KTB Corp. + BAHTNET Recon | ปัจจุบัน |

### 11.3 Key Strengths — Consulting Perspective

**Governance & Compliance**:
- Fully aligned with Ministry of Finance regulations
- Strong audit and control framework (สตง. / Internal Audit)
- Transparent reporting to public

**Financial Control**:
- Budget Hard Stop before spending (Real-time FM check)
- Prevents over-expenditure (ป้องกันใช้เงินเกินงบ)
- Commitment tracking ตั้งแต่สร้าง PO

**Transparency**:
- Direct payment to vendor (ลดการทุจริต)
- Full audit trail ทุกรายการ
- Segregation of Duties บังคับโดยระบบ

**Integration**:
- End-to-end financial lifecycle (FM → PO → AP → GL → MIS)
- No data duplication (Single Database)
- e-GP / PromptBiz / KTB Corp. integration

### 11.4 Budget Coding — IT Projects

```
Cloud SaaS (รายปี)         → 2XX + 5000 (งบดำเนินงาน)
On-Premise License (ถาวร)  → 310 + 1206XX (งบลงทุนครุภัณฑ์)
Software Subscription      → 2XX + 5000 (งบดำเนินงาน)
Hardware / Server          → 310 + 1206XX (งบลงทุนครุภัณฑ์)
Custom Development         → 310 + 1206XX หรือ 2XX + 5000 (ตามประเภท)
Annual Maintenance         → 2XX + 5000 (งบดำเนินงาน)
Data Center / อาคาร        → 320 + 1208 (งบลงทุนที่ดิน/สิ่ง)
Consulting / TOR           → 2XX + 5000 (งบดำเนินงาน)
Training                   → 2XX + 5000 (งบดำเนินงาน)
โครงการข้ามปีงบประมาณ      → กันเงิน สง.01 + ม.26/41 พรบ.วิธีการงบ
```

**กฎ IT Asset Capitalization**:
- Hardware ≥ 10,000 บาท → บันทึก FA Module + Auto GL posting
- Software License (Perpetual) → Intangible Asset
- Custom Software → Intangible Asset (เมื่อรับงานแล้ว)
- Cloud SaaS / Subscription → Operating Expense (ไม่ใช่สินทรัพย์)

### 11.5 Financial Transformation Roadmap

**Phase 1 (ปีที่ 1-2): Foundation**
- Soft Token Migration ครบทุกผู้ใช้ (UAM + ThaID)
- COA ปรับ 7 Dimension ให้ตรง GFMIS
- Segregation of Duties — ผู้บันทึก ≠ ผู้อนุมัติ
- ฝึกอบรมตามหลักสูตร กรมบัญชีกลาง (ม.49 พรบ.จัดซื้อ)
- Daily Reconciliation Routine (ตาม ว.88)

**Phase 2 (ปีที่ 2-3): Integration**
- GF-eLAAS: IEG Connection + Full Go-Live (เม.ย.–ก.ค. 68)
- e-Tax: PromptBIZ + KTB Sponsor Bank Auto-send
- Oracle/ERP ↔ GFMIS via IEG (Web Service / REST API)
- Automated Budget Control (Hard Stop pre-integration)
- Bank Reconciliation Automation (KTB Corp.)

**Phase 3 (ปีที่ 3-5): Optimization**
- GF-eGP: PO ↔ e-GP Auto-sync (ปีงบ 2569-2570)
- Central Vendor Master Sync (ปีงบ 2570-71)
- FA Automation: Asset creation from PO อัตโนมัติ
- MIS Analytics Dashboard (SAP BW / OTBI)
- Cost per Output Reporting (ต้นทุนต่อหน่วยผลผลิต)

---

## ส่วนที่ 12: กรอบการให้คำปรึกษา — Consulting Advisory Framework

### 12.1 การวิเคราะห์คำถาม 6 มิติ (Six-Lens Analysis)

1. **Context**: สรก. / รัฐวิสาหกิจ / อปท. / มหาวิทยาลัย / IT Vendor / ที่ปรึกษา / ผู้ตรวจสอบ
2. **Module**: FM / PO / AP / RP / FA / GL / MIS / UAM
3. **Law/Regulation**: พรบ.วิธีการงบ 2561 ม.X / ระเบียบ 2562 ข้อ X / พรบ.จัดซื้อ 2560 ม.X
4. **Document Code**: อง.03 / สง.01 / บท.01 / ขบ.01 / นส.01 / JV / PP ฯลฯ
5. **Risk**: กฎหมาย (ม.52) / วินัย / IT Security / สตง. / PDPA
6. **Action**: ขั้นตอน + เอกสาร + Timeline + รหัสในระบบ + หนังสือเวียนอ้างอิง

### 12.2 GFMIS Internal Control Checklist

**Access Control**:
- [ ] คำสั่ง/มอบหมายเป็นลายลักษณ์อักษร + กำหนดบุคคล + หน้าที่
- [ ] Segregation of Duties: บันทึก (xxxxxx10) ≠ อนุมัติ (xxxxxx01/02)
- [ ] เปลี่ยนรหัสผ่านทุก **3 เดือน** (ไม่เปลี่ยน = ระบบล็อค)
- [ ] Token Key / Soft Token: ต่ออายุก่อนหมด + อัปเดตชื่อผู้ถือ

**Daily Controls (ทุกสิ้นวันทำการ)**:
- [ ] ตรวจรายงาน: สรุปขอเบิก vs. ข้อมูลขอเบิกของสรก. (ZMIRO Report)
- [ ] ตรวจรายงาน: เงินสดคงเหลือ GFMIS vs. รายงานนอกระบบ
- [ ] กรณีพบข้อคลาดเคลื่อน: พิสูจน์ยอด → เสนอหัวหน้าลงนาม → เก็บรักษา

**Vendor Master**:
- [ ] สร้างก่อนทุกครั้งที่จ่ายเงิน (TIN + ชื่อ + บัญชีธนาคาร)
- [ ] ใช้กลุ่ม Vendor ให้ถูกต้อง (1000/2000/3000/4000/5000/6000/8000)
- [ ] มีสัญญาใน e-GP: ดึงข้อมูล Vendor จาก e-GP อัตโนมัติ

**Year-end Controls**:
- [ ] ทุก PO/สัญญาข้ามปี: สร้าง สง.01 ก่อน 30 ก.ย.
- [ ] โครงการ ≥ 1,000 ล้านบาท: ขอ ครม. อนุมัติล่วงหน้า (ม.26)
- [ ] FA Physical Count vs. FA Register ในระบบ
- [ ] Bank Reconciliation: RP Statement vs. KTB Statement

### 12.3 Risk Matrix — GFMIS + IT + Compliance

| ความเสี่ยง | กฎหมาย/ข้อ | ระดับ | มาตรการ |
|-----------|-----------|------|---------|
| จ่ายเงิน/ก่อหนี้โดยฝ่าฝืน | ม.52 พรบ.งบ 2561 | สูงมาก | รับผิดชดใช้เงิน + ค่าสินไหม + อาญา |
| โครงการ ≥ 1 พันล้าน ไม่ขอ ครม. | ม.26 | สูงมาก | เสนอ ครม. ก่อนตั้งงบฯ |
| กันเงิน/ขยายเกิน 6+6 เดือน | ม.43 | สูง | ทำความตกลงกับ กค. |
| Budget Overrun (ใช้เกินงบ) | ม.40 | สูง | Hard Stop ในระบบ FM |
| ใช้ User คนเดียวบันทึก+อนุมัติ | ข้อ 11 ระเบียบ 2562 | สูง | Segregation of Duties |
| ไม่เปลี่ยน Password ทุก 3 เดือน | หนังสือเวียน ว.67 | กลาง | ระบบ Lock อัตโนมัติ |
| Cloud Data นอกประเทศ | PDPA + Cloud Std 2567 | สูง | Data Residency Clause ใน TOR |
| ไม่ตรวจสอบรายงานรายวัน | หนังสือเวียน ว.88 | กลาง | Daily Reconciliation ทุกสิ้นวัน |
| IT Asset Class ผิดประเภท | ระเบียบ CGD | กลาง | IT Asset Classification Matrix |
| Vendor Master ข้อมูลผิด | ระเบียบ 2562 ข้อ 4 | กลาง | TIN Verification ก่อนสร้าง PO |

### 12.4 IT Service Provider — TOR/Contract Best Practices

**TOR สำหรับระบบที่เชื่อมต่อ GFMIS**:
- ข้อกำหนด IEG Standard API (CGD Standard)
- SLA: Uptime ≥ 99.5%, RPO ≤ 4 ชม., RTO ≤ 8 ชม.
- Security: DevSecOps + Kubernetes + Penetration Test ทุกปี
- Data Format: XML/JSON ตาม CGD Standard
- Source Code: เป็นของส่วนราชการ (ระบุในสัญญา)
- PDPA: DPA Agreement + ระบุ Sub-processor
- Exit Clause: Data Return/Migration ภายใน X วัน

**IT Procurement Quick Reference**:

| โครงการ | วิธีจัดซื้อ | ข้อระวัง |
|---------|-----------|---------|
| Cloud ERP SaaS > 500K/ปี | e-bidding | Data Residency + Audit Rights ใน TOR |
| GFMIS Integration Project | e-bidding > 500K | TOR ระบุ IEG Standard + SLA |
| Software License รายปี | e-market / เฉพาะเจาะจง ม.56(2)(ค) | ห้ามต่อสัญญาอัตโนมัติ |
| พัฒนาระบบ > 5M | e-bidding + รับฟัง TOR | IP + Source Code เป็นของรัฐ |
| Emergency (ระบบล่ม) | เฉพาะเจาะจง ม.56(2)(ง) | บันทึกเหตุผล + รายงาน |
| Annual Maintenance | เฉพาะเจาะจง ม.56(2)(จ) | ห้ามเลี่ยงการแข่งขัน |

---

## ส่วนที่ 12B: GFMIS vs ERP — Consulting Comparison Framework

> อ่าน `references/gfmis-vs-erp.md` สำหรับรายละเอียดครบถ้วนและ Use Cases

### ความแตกต่างหลัก (Executive Summary)

| มิติ | GFMIS (New GFMIS Thai) | ERP (SAP / Oracle / Dynamics) |
|------|----------------------|------------------------------|
| **วัตถุประสงค์** | Control & Compliance | Efficiency & Performance |
| **แนวคิด** | Fiscal Control System | Business Management System |
| **งบประมาณ** | Mandatory Hard Stop | Optional / Soft Control |
| **การจ่ายเงิน** | Centralized (CGD) | Decentralized (องค์กรเอง) |
| **การจัดซื้อ** | Legal-driven (e-GP/พรบ.) | Business-driven |
| **บัญชี** | Government/Fund (IPSAS) | Commercial (IFRS/GAAP) |
| **ความยืดหยุ่น** | ต่ำ (Rigid แต่ควบคุมได้) | สูง (ต้องมี Governance เอง) |
| **ผู้ใช้** | ระบบระดับชาติ (ทุกสรก.) | ระบบระดับองค์กร |
| **รายรับ** | ต้องนำส่งคลัง | เก็บในบัญชีองค์กร |
| **สินทรัพย์** | มาตรฐานภาครัฐ ≥10,000 บาท | ยืดหยุ่นตามนโยบายองค์กร |

### ความแตกต่างเชิงลึก 10 มิติ

**1. Core Concept**
- GFMIS = **Control-driven**: ทุก transaction ต้องผ่านการตรวจสอบงบประมาณและระเบียบก่อน
- ERP = **Operation-driven**: Transaction ขับเคลื่อนโดย business operation ก่อน

**2. Budget Control (Critical Difference)**
- GFMIS: Budget เป็น **Legal Control** — Hard Stop ถ้างบไม่พอ; Commitment ทันทีที่สร้าง PO; Multi-dimensional mandatory (Fund Source + Activity + Commitment Item)
- ERP: Budget เป็น **Management Tool** — อาจเป็นแค่ Warning; ปรับ Soft/Hard Control ได้

**3. Payment Process**
- GFMIS: **Centralized** ผ่าน CGD → BOT/Bank → Vendor โดยตรง; หน่วยงานไม่ได้จ่ายเอง
- ERP: **Decentralized** — องค์กรจ่ายจากบัญชีตนเอง ควบคุมเวลาจ่ายได้

**4. Procurement**
- GFMIS: **Legally Enforced** — ต้องเป็นไปตาม พรบ.จัดซื้อจัดจ้าง 2560 + e-GP; PO = Legal Commitment Document
- ERP: **Operational Process** — PR → PO → GR → Invoice; ไม่มีระบบบังคับทางกฎหมายภายนอก

**5. Accounting Standard**
- GFMIS: **Government Accounting + IPSAS** — Fund Accounting, Multi-dimension mandatory, Budget/Accrual Hybrid
- ERP: **Commercial (IFRS/GAAP)** — P&L, Balance Sheet, Cost Center/Profit Center

**6. Revenue**
- GFMIS: รายรับต้องบันทึก + นำส่งคลัง (Pay-in slip + KTB Corp.)
- ERP: รายรับเข้าบัญชีองค์กรโดยตรง ไม่ต้องนำส่งคลัง

**7. Fixed Assets**
- GFMIS: มาตรฐานภาครัฐ เกณฑ์ **≥ 10,000 บาท**; เน้น Compliance + Audit + Central Reporting
- ERP: ยืดหยุ่นตามนโยบายองค์กร; เน้น Depreciation Optimization + Tax Strategy

**8. User Access**
- GFMIS: **Strict Segregation** — ผู้ขอ ≠ ผู้อนุมัติ ≠ ผู้จ่าย; Central UAM; Mandatory Soft Token
- ERP: Flexible Role Design ตามนโยบายองค์กร

**9. Reporting**
- GFMIS: Predefined Government Formats; เน้น Audit/Transparency; MIS รองรับหลายระดับ (Agency/Central/Committee)
- ERP: Highly Customizable (BI Tools, Dashboards); เน้น Business Insight + Strategy

**10. System Architecture**
- GFMIS: **Centralized National Platform** — ทุกสรก.ใช้ระบบเดียวกัน; Integration กับ e-GP, KTB, BOT, PromptBiz
- ERP: แต่ละองค์กรมี Instance ของตัวเอง; Integration ตามความต้องการ

### Final Consulting Insight — Integration Strategy

```
GFMIS ≠ ERP ทั่วไป
GFMIS ≈ "SAP Public Sector + Treasury Control System + Regulatory Platform"

การ Integrate ERP กับ GFMIS:
┌─────────────────────────────────────────┐
│  ERP (Oracle / SAP)                     │
│  = Operational System (Front-end)       │
│  PR → PO → GR → Invoice                │
│  Asset Management / Project Costing     │
└──────────────┬──────────────────────────┘
               │  IEG (Information Exchange Gateway)
               │  Budget Sync + Document Reference
               │  Real-time Validation
┌──────────────▼──────────────────────────┐
│  GFMIS (New GFMIS Thai)                 │
│  = Financial Control & Reporting (Back) │
│  FM Budget Control (Hard Stop)          │
│  AP Direct Payment → CGD → BOT         │
│  GL Accrual + MIS Reporting             │
└─────────────────────────────────────────┘

Integration Focus:
1. Budget Synchronization (ERP Commitment ↔ GFMIS FM)
2. Document Reference Mapping (PO/Invoice No. ↔ เลขที่ GFMIS)
3. Real-time Budget Validation (Hard Stop pre-posting)
4. Vendor Master Sync (ERP Supplier ↔ GFMIS Vendor 1000-8000)
5. Payment Confirmation (GFMIS Run Payment → ERP Clearing)
```

### Process Rigidity — Consulting Implication

**GFMIS = Rigid but Controlled**:
- Cannot skip steps (workflow บังคับ)
- Hard to customize (เป็น National Standard)
- Designed for compliance + full audit trail
- Every deviation requires formal waiver/approval

**ERP = Flexible but Requires Governance**:
- Configurable workflow + approval rules
- Requires strong internal controls (ออกแบบเอง)
- Risk of inconsistency without proper governance

**Implication for Thai Government IT Projects**:
- GFMIS เป็น backbone ที่เปลี่ยนไม่ได้ → ERP/Back-office ต้อง adapt ให้ตรงกับ GFMIS workflow
- Budget coding ใน ERP ต้องตรงกับโครงสร้าง GFMIS ครบ 7 มิติ
- Payment รอบสุดท้ายเสมอผ่าน GFMIS (ห้าม bypass)

---

## ส่วนที่ 13: Reference Files

- `references/gfmis-procedures.md` — **ขั้นตอนปฏิบัติงาน GFMIS ฉบับ Consulting Grade** ครบทุกโมดูล FM/PO/AP/RP/FA/GL/MIS + UAM + IT Classification + Controls
- `references/gfmis-vs-erp.md` — **GFMIS vs ERP Consulting Framework** ครบ 11 มิติ + Integration Architecture + Pitfalls
- `references/egp-procurement-guide.md` — คู่มือ e-GP ฉบับสมบูรณ์ (10 ขั้นตอน, วิธีต่างๆ, IT Cases, FAQ)
- `references/budget-law-details.md` — พรบ.วิธีการงบประมาณ 2561 + การก่อหนี้ผูกพัน
- `references/oracle-govt-architecture.md` — Oracle Cloud Architecture + COA ภาครัฐ + Integration Patterns
- `references/new-gfmis-thai-system.md` — แผนงาน 5 ปี New GFMIS Thai (Soft Token, GF-eLAAS, UAM, e-Tax, GF-eGP, Enhancement)

---

> **อ้างอิงหลัก**: พรบ.วิธีการงบประมาณ พ.ศ. 2561 | ระเบียบเบิกจ่ายเงิน 2562 | คู่มือตรวจสอบ GFMIS (สป.มท. ต.ค. 2561) | ระบบ GFMIS (กองระบบการคลังภาครัฐ กรมบัญชีกลาง) | GFMIS Consulting Experience (Practical Implementation Guide) | แผนงาน 5 ปี New GFMIS Thai (23 มิ.ย. 2568) | พรบ.จัดซื้อจัดจ้าง 2560 + ระเบียบกระทรวงการคลัง 2560
