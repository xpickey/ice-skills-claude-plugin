# New GFMIS Thai — System Reference Guide
## กรมบัญชีกลาง — ระบบบริหารการเงินการคลังภาครัฐแบบอิเล็กทรอนิกส์ใหม่

### Access Points
- GFMIS Web Online (Intranet): https://webonlineintra.gfmis.go.th
- GFMIS Web Online (Internet + Token): https://webonlineinter.gfmis.go.th
- Portal New GFMIS Thai: ผ่าน Soft Token
- UAM Registration: Web Register Portal
- CGD Official: www.cgd.go.th

---

## หลักการควบคุมระบบ (Access Control)

| หลักการ | รายละเอียด |
|--------|-----------|
| Segregation of Duties | ผู้บันทึก ≠ ผู้อนุมัติ (ห้ามคนเดียวทำทั้งหมด) |
| 1 คน / 1 ชุดสิทธิ์ | ห้ามใช้ชื่อผู้ใช้ร่วมกัน |
| Password Policy | เปลี่ยนทุก 3 เดือน |
| Authentication | Soft Token (ทยอย Migrate แทน Hardware Token) |
| Identity | ThaID Integration (UAM Enhancement) |

---

## Soft Token Migration Timeline

```
ปีงบประมาณ 2567
├── Migrate #1: กระทรวง (บน.) + สำนักงานปลัดกระทรวง (สป.กค.)
│   → ผู้ใช้ ~10,000 ราย
│
├── Migrate #2: อบต. (องค์การบริหารส่วนตำบล)
│   → ผู้ใช้ ~20,000 ราย
│
ปีงบประมาณ 2568
├── เทศบาลตำบล (ยกฐานะ) — New
│   → ผู้ใช้ ~20,000+ ราย
│
└── Migrate #3: ทั้งหมด (All Users)
    → เป้าหมาย ~50,000+ ราย (100% Soft Token)
```

---

## GF-eLAAS — Architecture Detail

### ภาพรวมการเชื่อมโยง
```
New GFMIS Thai (CGD)
       ↕  IEG (Information Exchange Gateway)
ระบบบัญชี LAAS (Local Authorities Accounting System)
       ↕
อปท. แต่ละแห่ง (อบต. / เทศบาล / อบจ.)
```

### Timeline (ปีงบ 2568)
| เดือน | Milestone |
|-------|-----------|
| ก.ย. 67 | จัดทำระบบเสร็จ + DevSecOps & Kubernetes Migration |
| ธ.ค. 67 | DB Backup Non-PRD |
| ม.ค. 68 | DB Backup PRD |
| มี.ค. 68 | Central Ministry Conso. + CGD Costing |
| เม.ย. 68 | Soft Go-Live IEG + Central Budget + Agency Interface + Web Vendor |
| พ.ค. 68 | Agency Online (Full) |
| มิ.ย. 68 | Agency Online Report |
| ก.ค. 68 | Full Go-Live IEG |

### Infrastructure Migration
- **จาก**: DevOps & Docker
- **ไปสู่**: DevSecOps & Kubernetes
- **ประโยชน์**: Security-by-design + Scalability + Container orchestration

---

## UAM (User Access Management) — Enhanced Features

### Architecture
```
เจ้าหน้าที่ส่วนกลาง (ผู้ดูแล UAM)
       ↓
   UAM System
       ↑
ส่วนราชการ (ผู้ใช้งาน)
   ├── Web Register (ลงทะเบียน)
   └── Portal (เข้าใช้งาน)
```

### Features (ระบุสถานะ)

| Feature | สถานะ | รายละเอียด |
|---------|-------|-----------|
| User Self Service (รีเซ็ตรหัสผ่าน) | ✅ ใช้งานแล้ว | ขอรหัสผ่านใหม่กรณีลืม |
| ThaID Integration | 🟡 รอ Go Live | พิสูจน์ตัวตนดิจิทัลผ่านกรมการปกครอง |
| สิทธิ์สำรอง (Backup Rights) | 🟡 รอ Go Live | มอบหมายสิทธิ์สำรองได้ |
| รายงาน UAM | 🟡 รอ Go Live | รายงานผู้ใช้งานและสิทธิ์ครบถ้วน |

### UAM Registration Flow
```
ผู้ใช้ใหม่ → Web Register Portal
    → กรอกข้อมูล + ThaID Verification
    → ส่งคำขอ → ผู้ดูแล UAM อนุมัติ
    → ได้รับ Soft Token + สิทธิ์การใช้งาน
    → Login ผ่าน Portal
```

---

## e-Tax System — Technical Detail

### ข้อมูลที่ส่งไป PromptBIZ ทุกสิ้นวัน
- รายการที่ **ยืนยันจ่ายเงินสำเร็จแล้วเท่านั้น**
- ข้อมูลรายการหักภาษี ณ ที่จ่าย (Withholding Tax)
- เลขประจำตัวผู้เสียภาษีของคู่สัญญา

### Sponsor Bank
- **ธนาคารกรุงไทย (KTB)** เป็น Sponsor Bank หลัก
- ผู้ขายดู e-Receipt ได้ผ่าน PromptBIZ
- ผู้ซื้อ (ราชการ) ดูหลักฐานได้ผ่าน K-Corp หรือระบบ Sponsor Bank

### ขอบเขตที่ไม่รวม
- ไม่นำข้อมูล e-Receipt จาก PromptBIZ กลับเข้า GFMIS
- ระบบเป็น One-way: GFMIS → PromptBIZ เท่านั้น

---

## GFMIS Vendor Master — ข้อมูลที่ต้องมี

| Field | รายละเอียด | ข้อสำคัญ |
|-------|-----------|---------|
| ชื่อ-นามสกุล / ชื่อนิติบุคคล | ต้องตรงกับ TIN | ต้องตรง e-Tax |
| ที่อยู่ | ที่อยู่ทางกฎหมาย | ใช้ออก ใบกำกับภาษี |
| เลขประจำตัวผู้เสียภาษี (TIN) | 13 หลัก | บังคับ |
| เลขบัญชีธนาคาร | PromptPay / บัญชีธนาคาร | จ่ายตรง |
| ประเภทธุรกิจ | บุคคล/นิติบุคคล/ราชการ | กระทบ VAT/WHT |

---

## GF-eGP — Integration Benefits (ปีงบ 2569-2570)

### ปัญหาปัจจุบัน (ก่อน GF-eGP)
- ต้องกรอกข้อมูลใน e-GP แล้วกรอกซ้ำใน GFMIS
- มีโอกาสข้อมูลไม่ตรงกันระหว่าง 2 ระบบ
- ขั้นตอนมาก + ใช้เวลานาน

### หลัง GF-eGP Integration
```
e-GP (สร้าง PO/สัญญา)
    ↓  Auto-sync
New GFMIS Thai (ผูกพันงบประมาณ + AP)
    ↓
จ่ายตรงผ่าน PromptPay/PromptBIZ
```

### ข้อมูลที่ Sync อัตโนมัติ
- ข้อมูลคู่สัญญา (Vendor) จาก e-GP → GFMIS Vendor Master
- มูลค่าสัญญา → GFMIS Budget Commitment
- สถานะการตรวจรับ → GFMIS AP Invoice

---

## New GFMIS Thai Enhancement — External Integration

### ระบบภายนอกที่จะบูรณาการ (ปีงบ 2570-2571)

| ระบบ | การบูรณาการ | ประโยชน์ |
|------|-----------|---------|
| Central Vendor Master | Sync ข้อมูลผู้ขายทั่วประเทศ | ลด Duplicate |
| ระบบสินทรัพย์ถาวร | Asset-to-GFMIS Integration | บัญชีสินทรัพย์อัตโนมัติ |
| ระบบเบิกจ่าย | Enhanced AP Automation | ลดขั้นตอนมนุษย์ |
| External ERP/Back-office | API Integration | หน่วยงานรัฐที่มี ERP เอง |

---

## FAQ — คำถามที่พบบ่อย

**Q: ต่างจาก GFMIS เดิมอย่างไร?**
A: New GFMIS Thai รองรับ National e-Payment, PromptPay, e-Tax, Cloud Infrastructure, DevSecOps และเชื่อมโยงกับระบบอื่นผ่าน IEG ได้มีประสิทธิภาพกว่า

**Q: Soft Token ต่างจาก Hardware Token อย่างไร?**
A: Soft Token เป็น Digital Token บนมือถือ/แอพ ไม่ต้องพกอุปกรณ์แยก เพิ่ม ThaID Verification และลดต้นทุนการจัดการ

**Q: หน่วยงาน อปท. ต้องทำอะไรบ้างสำหรับ GF-eLAAS?**
A: ต้องเตรียม (1) ระบบบัญชี LAAS ที่รองรับ IEG Protocol, (2) UAM + Soft Token ครบทุกผู้ใช้, (3) ทดสอบการส่งข้อมูลผ่าน Agency Interface ก่อน Full Go-Live

**Q: Budget Code YY ในปีงบ 2568 คืออะไร?**
A: YY = 68 (2 หลักท้ายของ พ.ศ. 2568) ดังนั้นรหัสแหล่งของเงินจะขึ้นต้นด้วย 68

**Q: Cloud ERP ต้องผ่าน e-GP หรือไม่?**
A: ต้อง — Cloud SaaS > 500,000 บาท/ปี ต้องใช้ e-bidding ใน e-GP และระบุข้อกำหนด Data Residency, PDPA, Audit Rights ใน TOR
