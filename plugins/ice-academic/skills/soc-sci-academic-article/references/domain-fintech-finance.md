# Domain Knowledge: FinTech & Financial Transformation

ความรู้พื้นฐานสำหรับการเขียนบทความวิชาการที่เกี่ยวข้องกับ FinTech, IFRS9, NPL/NPA, Digital Lending
สำหรับรายละเอียดเชิงลึก ให้อ่าน dependent skill: `fin-tech-consulting`

---

## 1. IFRS9 Expected Credit Loss (ECL) Framework

### ภาพรวม
- มาตรฐาน IFRS 9 (Financial Instruments) มีผลบังคับตั้งแต่ 1 ม.ค. 2561
- เปลี่ยนจาก Incurred Loss Model → Expected Credit Loss Model
- บังคับสถาบันการเงินทุกแห่งในไทย (ตาม ธปท.)

### องค์ประกอบ ECL
- **PD** (Probability of Default) — ความน่าจะเป็นที่จะผิดนัดชำระ
- **LGD** (Loss Given Default) — ความสูญเสียเมื่อผิดนัดชำระ
- **EAD** (Exposure at Default) — ยอดคงค้างเมื่อผิดนัดชำระ
- **ECL = PD × LGD × EAD × Discount Factor**

### Stage Classification
| Stage | เกณฑ์ | การคำนวณ ECL |
|---|---|---|
| Stage 1 | ปกติ ไม่มี SICR | 12-month ECL |
| Stage 2 | มี SICR (Significant Increase in Credit Risk) | Lifetime ECL |
| Stage 3 | Credit-Impaired (NPL) | Lifetime ECL |

### SICR Triggers (ตัวอย่าง)
- ค้างชำระ >30 วัน (Rebuttable presumption)
- Credit score ลดลงมาก
- Forbearance / Restructuring
- สภาพเศรษฐกิจเปลี่ยนแปลงรุนแรง

---

## 2. NPL/NPA Asset Management

### นิยาม
- **NPL** (Non-Performing Loan) — สินเชื่อที่ค้างชำระ >90 วัน หรือมีสัญญาณผิดนัด
- **NPA** (Non-Performing Asset) — สินทรัพย์รอการขาย (จากการยึดหลักประกัน)
- **AMC** (Asset Management Company) — บริษัทบริหารสินทรัพย์

### กระบวนการบริหาร NPL
1. **Portfolio Acquisition** — ซื้อหนี้จากสถาบันการเงิน
2. **Due Diligence** — ตรวจสอบคุณภาพหนี้
3. **Segmentation** — แบ่งกลุ่มหนี้ตามความสามารถในการชำระ
4. **Workout Strategy** — เจรจา / ปรับโครงสร้าง / ฟ้อง / ขายทอดตลาด
5. **Recovery** — เก็บเงินคืน

---

## 3. Digital Lending & Loan Origination

### Loan Origination System (LOS)
- ระบบ End-to-End: Application → Credit Decisioning → Approval → Disbursement
- Digital Credit Decisioning: Alternative Data + ML-based Scoring
- Core Banking Landscape: Temenos / Finastra / Oracle FLEXCUBE

### Digital Lending Trends
- Credit-as-a-Service (Embedded Finance)
- Open Banking & API Economy
- AI/ML in Credit Risk Assessment
- Digital Onboarding (e-KYC)

---

## 4. Basel III/IV

### Capital Requirements
- Common Equity Tier 1 (CET1): ≥4.5%
- Tier 1 Capital: ≥6%
- Total Capital: ≥8%
- Conservation Buffer: 2.5%
- Thai Banks: Typically hold 15-18% (well above minimum)

### Credit Risk Approaches
- Standardized Approach (SA) — ใช้ Risk Weight ตาม Basel
- Internal Ratings-Based (IRB) — ใช้ PD/LGD/EAD ภายใน

---

## 5. FinTech Engines & Platforms

| ประเภท | ตัวอย่าง Platform |
|---|---|
| IFRS9 Engine | Moody's, SAS, Oracle, Wolters Kluwer |
| Core Banking | Temenos, Finastra, Oracle FLEXCUBE, Finacle |
| LOS | Blend, nCino, Finastra Fusion, Newgen |
| Collection | FICO Debt Manager, Experian PowerCurve |
| Credit Scoring | FICO, Experian, TransUnion, Alternative Data |

---

## 6. ทฤษฎีที่เกี่ยวข้องสำหรับบทความวิชาการ

- **Financial Innovation Theory** (Merton, 1992) — วิเคราะห์นวัตกรรม FinTech
- **Agency Theory** (Jensen & Meckling, 1976) — วิเคราะห์ความสัมพันธ์ผู้ให้กู้-ผู้กู้
- **Information Asymmetry** (Akerlof, 1970) — วิเคราะห์ปัญหาข้อมูลไม่สมมาตรในตลาดสินเชื่อ
- **TAM** (Davis, 1989) — วิเคราะห์การยอมรับ Digital Lending
- **Diffusion of Innovation** (Rogers, 2003) — วิเคราะห์การแพร่กระจาย FinTech

### ตัวอย่างหัวข้อบทความวิชาการ
1. "การวิเคราะห์ผลกระทบ IFRS9 ต่อการบริหารความเสี่ยงสินเชื่อของธนาคารพาณิชย์ไทย"
2. "Digital Lending: มุมมองเชิงทฤษฎีนวัตกรรมทางการเงินและการคุ้มครองผู้บริโภค"
3. "บทวิจารณ์กรอบ Basel III/IV กับความเพียงพอของเงินกองทุนธนาคารพาณิชย์ไทย"
