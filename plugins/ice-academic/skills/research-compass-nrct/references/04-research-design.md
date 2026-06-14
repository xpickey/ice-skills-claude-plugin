# 04 — การออกแบบการวิจัย (หมวด ๔)

ELO ที่เกี่ยวข้อง: ELO 2 (ออกแบบให้สอดคล้องคำถาม/วัตถุประสงค์/ผลผลิต) ผ่าน K2-1, K2-2, S2-1, A2-1
หลักสูตรแบ่งเป็น ๗ สาขา OECD: (๔.๑) วิศวกรรมศาสตร์ (๔.๒) วิทยาศาสตร์ธรรมชาติ (๔.๓) วิทยาศาสตร์การแพทย์/สุขภาพ
(๔.๔) เกษตร (๔.๕) สังคมศาสตร์ (๔.๖) มนุษยศาสตร์ (๔.๗) บูรณาการ หลักการในไฟล์นี้ใช้ข้ามสาขา ส่วนรายละเอียดเฉพาะ
สาขาอยู่ท้ายไฟล์

หลักแกน: **method follows question** — เลือกวิธีให้ตอบคำถามวิจัยได้ตรง ไม่ใช่เลือกวิธีที่ถนัดก่อน

---

## 1. ความรู้: เลือกแนวทางให้ตรงคำถาม

| คำถามแบบ | แนวทาง | ตัวอย่างแบบแผน |
|----------|--------|----------------|
| มากแค่ไหน / สัมพันธ์กันไหม / ต่างกันไหม / เป็นเหตุไหม | เชิงปริมาณ | survey, correlational, quasi-experiment, experiment (RCT) |
| ทำไม / อย่างไร / มีความหมายอย่างไร | เชิงคุณภาพ | phenomenology, grounded theory, case study, ethnography, content/thematic analysis |
| ทั้งวัดและเข้าใจ | ผสม (mixed methods) | explanatory sequential, exploratory sequential, convergent, embedded |

หลักสูตรยังระบุชนิดเชิงคุณภาพ/บูรณาการที่ลึกขึ้น เช่น การวิจัยเชิงปรัชญา เชิงสร้างสรรค์ เชิงวิพากษ์ เชิงชาติพันธุ์วรรณา
เชิงปฏิบัติการ การวิจัยเชิงระบบ (systems-based) และการวิจัยเชิงบูรณาการเชิงปรัชญา (philosophical integrative)

## 2. ความรู้: การออกแบบเชิงปริมาณ

- **กรอบแนวคิดและตัวแปร** — ระบุตัวแปรต้น/ตาม/ควบคุม/แทรกซ้อน และนิยามเชิงปฏิบัติการ (operational definition)
- **การสุ่มตัวอย่าง (sampling)** —
  - แบบความน่าจะเป็น: simple random, systematic, stratified, cluster, **multi-stage random sampling**
  - แบบไม่ใช่ความน่าจะเป็น: **purposive**, quota, convenience, snowball
  - คำนวณขนาดตัวอย่าง: power analysis (G*Power) หรือสูตร เช่น Taro Yamane, Cochran ระบุเหตุผลของขนาดที่เลือก
- **เครื่องมือและคุณภาพ** —
  - **ความตรง (validity)**: content (IOC จากผู้เชี่ยวชาญ ≥ 0.5), construct, criterion
  - **ความเที่ยง (reliability)**: Cronbach's alpha (≥ 0.7), test-retest, inter-rater (Kappa) จาก pilot test
- **เลือกสถิติให้ตรงสมมติฐานและระดับการวัด**

| เป้าหมาย | สถิติ |
|----------|-------|
| บรรยาย | mean, SD, ความถี่, ร้อยละ |
| เปรียบเทียบ ๒ กลุ่ม | t-test (independent/paired) |
| เปรียบเทียบ > ๒ กลุ่ม | ANOVA / ANCOVA |
| ความสัมพันธ์ | Pearson / Spearman correlation |
| ทำนาย | regression (simple/multiple/logistic) |
| ตัวแปรแฝง/โมเดลเชิงสาเหตุ | SEM / PLS-SEM (ดู `11-advanced-toolkit.md`) |
| ข้อมูลจัดประเภท | Chi-square |

ตรวจข้อตกลงเบื้องต้น (assumptions เช่น normality, homogeneity) ก่อนใช้สถิติพาราเมตริก

## 3. ความรู้: การออกแบบเชิงคุณภาพ

- **การเลือกผู้ให้ข้อมูล** — purposive/theoretical sampling จนถึงจุดอิ่มตัว (saturation)
- **เครื่องมือ** — แนวคำถามสัมภาษณ์กึ่งโครงสร้าง (interview guide), การสังเกต (participant/non-participant), focus group
- **ความน่าเชื่อถือ (trustworthiness)** — credibility, transferability, dependability, confirmability ด้วย
  triangulation, member checking, audit trail, thick description
- **การวิเคราะห์** — thematic/content analysis เข้ารหัส (coding: open→axial→selective ใน grounded theory)
  อย่างเป็นระบบ เก็บร่องรอยการตัดสินใจ

## 4. ความรู้: การออกแบบแบบผสม (mixed methods)

ระบุให้ชัดว่า ส่วนปริมาณกับคุณภาพ **ต่อกันตรงไหน (point of integration)** และ **ฝั่งไหนนำ (priority)**

- explanatory sequential (QUAN → qual อธิบายผล) · exploratory sequential (qual → QUAN สร้างเครื่องมือ/ทฤษฎี)
- convergent (เก็บคู่ขนานแล้วเทียบ) · embedded (ฝังชุดเล็กในชุดใหญ่)

## 5. ความรู้: การจัดการข้อมูล (Data Management — เชื่อม RCR บท ๔)

- ออกแบบ **case record form / data sheet** ให้ตอบคำถามวิจัยและได้ข้อมูลที่วิเคราะห์ได้จริง
- นิยาม data dictionary, ทำ data cleaning, ควบคุมคุณภาพ (data quality)
- จัดเก็บปลอดภัย สำรองข้อมูล แยกข้อมูลระบุตัวตน กำหนดสิทธิ์เข้าถึง (เชื่อม PDPA)
- เก็บข้อมูลดิบและสคริปต์วิเคราะห์ให้ตรวจย้อนได้ เพื่อ reproducibility (RCR บท ๘)

## 6. ทักษะ: ซอฟต์แวร์ตามสาขา (S2-1)

- เชิงปริมาณ/วิศวะ-วิทย์: SPSS, R, Python, MATLAB, Minitab, SAS, JASP, SmartPLS, AMOS
- เชิงคุณภาพ/สังคม-มนุษย์: NVivo, ATLAS.ti, **Dedoose, MAXQDA** (วิเคราะห์ข้อมูลเชิงผสม)
- จัดการอ้างอิง: Zotero, EndNote, Mendeley

ระบุเวอร์ชันและขั้นตอนเพื่อให้ทำซ้ำได้

## 7. จริยธรรมฝังในการออกแบบ (ethics by design — A3-1)

ตั้งแต่ขั้นออกแบบให้ระบุ: ต้องขอรับรองมาตรฐานใด (มนุษย์/สัตว์/ชีวภาพ/ห้องปฏิบัติการ), แผน consent,
การลดความเสี่ยงต่อผู้เข้าร่วม และแผนปกป้องข้อมูล อย่าทิ้งจริยธรรมไว้ท้ายสุด

## 8. ชั้นขั้นสูง (Beyond)

- การออกแบบทดลอง/กึ่งทดลองที่ควบคุมตัวแปรกวน, factorial/repeated-measures, randomization & blinding
- SEM/PLS-SEM, multilevel modeling, mediation/moderation, time-series, Bayesian analysis (ดู `11-advanced-toolkit.md`)
- การออกแบบเชิงคุณภาพที่เข้มงวด: เกณฑ์ COREQ/SRQR สำหรับรายงาน, intercoder reliability
- pre-registration ของแบบแผนและสถิติเพื่อกัน p-hacking

## 9. รายละเอียดเฉพาะสาขา (๔.๑-๔.๗) — โดยย่อ

- **วิศวกรรม** — เชิงทดลอง, R&D, เชิงจำลอง, สร้าง-ทดสอบต้นแบบ; เครื่องมือ MATLAB/Python/R
- **วิทยาศาสตร์ธรรมชาติ** — เชิงทดลองในห้องปฏิบัติการ, การควบคุมตัวแปร, ความปลอดภัยชีวภาพ/ห้องปฏิบัติการ
- **การแพทย์/สุขภาพ** — RCT, cohort, case-control, cross-sectional; จริยธรรมในมนุษย์เข้มข้น (IRB)
- **เกษตร** — แปลงทดลอง (RCBD, Latin square), การวิเคราะห์ผลผลิต
- **สังคมศาสตร์** — survey, correlational, mixed; SEM; เครื่องมือ SPSS/AMOS/SmartPLS
- **มนุษยศาสตร์** — เชิงคุณภาพ/ปรัชญา/วิพากษ์/สร้างสรรค์; การตีความและการวิเคราะห์เอกสาร
- **บูรณาการ** — systems-based, transdisciplinary, philosophical integrative (เชื่อม `06-research-network.md`)

## 10. เกณฑ์ตรวจการออกแบบ

- วิธีที่เลือก ตอบคำถามวิจัยได้ตรงหรือไม่
- ตัวอย่าง/ผู้ให้ข้อมูล เป็นตัวแทนหรือเข้าถึงปรากฏการณ์ได้จริงหรือไม่
- เครื่องมือผ่านการทดสอบคุณภาพ (validity/reliability หรือ trustworthiness) แล้วหรือยัง
- แผนวิเคราะห์และสถิติสอดคล้องกับสมมติฐานและระดับการวัดหรือไม่
- จริยธรรมและการจัดการข้อมูลถูกฝังไว้ครบหรือยัง
