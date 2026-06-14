# 11 — คลังเทคนิควิจัยขั้นสูง (Advanced Research Toolkit)

ไฟล์นี้รวมความรู้และเทคนิคระดับ "เหนือหลักสูตร" สำหรับนักวิจัยที่ต้องการทำงานระดับตีพิมพ์สากลและขอทุนแข่งขัน
ใช้เมื่อผู้ใช้พร้อมยกระดับ ไม่ใช่จุดเริ่มต้น ทุกเทคนิคยังต้องยืนบนบูรณภาพ (RCR) และจริยธรรม (มาตรฐาน วช.)

---

## 1. สถิติและการสร้างโมเดลขั้นสูง

| เทคนิค | ใช้เมื่อ | เครื่องมือ |
|--------|---------|------------|
| Multiple / logistic regression | ทำนายผลจากหลายตัวแปร | R, Python (statsmodels), SPSS |
| SEM (covariance-based) | ทดสอบโมเดลเชิงสาเหตุที่มีตัวแปรแฝง ทฤษฎีหนักแน่น | AMOS, Mplus, lavaan (R) |
| PLS-SEM | โมเดลซับซ้อน ตัวอย่างไม่มาก เน้นทำนาย | SmartPLS, seminR (R) |
| Multilevel / HLM | ข้อมูลซ้อนชั้น (นักเรียนในห้องในโรงเรียน) | R (lme4), HLM, Mplus |
| Mediation / moderation | ทดสอบตัวแปรส่งผ่าน/กำกับ | PROCESS macro, lavaan |
| Time-series / panel | ข้อมูลตามเวลา | R, Stata, EViews |
| Bayesian analysis | อนุมานแบบความน่าจะเป็น ใช้ prior | Stan, brms (R), JASP |
| Machine learning | ทำนาย/จัดกลุ่มจากข้อมูลใหญ่ | Python (scikit-learn), R |

หลักสำคัญ: เลือกเทคนิคจาก **คำถามและโครงสร้างข้อมูล** ไม่ใช่ความนิยม ตรวจ assumptions, รายงาน effect size และ
ช่วงความเชื่อมั่น (CI) ไม่ใช่แค่ p-value

## 2. Systematic Review และ Meta-analysis

- ทำตาม **PRISMA 2020** — มี flow diagram (identification → screening → included) และ checklist
- ลงทะเบียน protocol ที่ **PROSPERO** ก่อนเริ่ม
- ประเมินอคติ: Cochrane RoB 2, ROBINS-I; ประเมินคุณภาพหลักฐานด้วย **GRADE**
- Meta-analysis: คำนวณ pooled effect size (Cohen's d, OR, RR), ตรวจ heterogeneity (I²), forest/funnel plot,
  publication bias (Egger's test) ด้วย R (metafor), RevMan, CMA

## 3. Bibliometrics และ Science Mapping

- ดึงข้อมูลจาก Scopus/Web of Science แล้ววิเคราะห์ด้วย **VOSviewer, CiteSpace, Bibliometrix (R)**
- เทคนิค: co-authorship, co-citation, bibliographic coupling, co-word/keyword burst
- ใช้หา research front, ช่องว่าง, ผู้เล่นหลัก และแนวโน้ม เพื่อวางตำแหน่งงานวิจัย

## 4. การออกแบบเชิงทดลองขั้นสูง

- Randomization, blinding, control of confounders
- Factorial design, repeated-measures, crossover, RCBD/Latin square (เกษตร/วิศวะ)
- A/B testing และ quasi-experiment (difference-in-differences, regression discontinuity, propensity score matching)
- คำนวณ power และ sample size ล่วงหน้า (G*Power) เพื่อหลีกเลี่ยง underpowered study

## 5. ความเข้มงวดเชิงคุณภาพ

- เกณฑ์รายงาน: **COREQ** (สัมภาษณ์/focus group), **SRQR** (qualitative ทั่วไป)
- Intercoder reliability, reflexivity, negative case analysis, abductive analysis
- เครื่องมือ CAQDAS: NVivo, ATLAS.ti, MAXQDA, Dedoose

## 6. Open Science และการทำซ้ำได้ (Reproducibility)

- **Reproducible workflow** — สคริปต์วิเคราะห์ที่รันซ้ำได้ (R Markdown / Jupyter), version control (Git/GitHub)
- เก็บข้อมูลและโค้ดบนคลังเปิด (OSF, Zenodo, figshare) พร้อม DOI ภายใต้ข้อจำกัด PDPA
- หลัก **FAIR data** และ data management plan (DMP)
- Pre-registration / Registered Report เพื่อกัน HARKing และ p-hacking

## 7. Theory of Change และการประเมินผลกระทบ

- เขียนห่วงโซ่เหตุผล (if-then) จาก activity → output → outcome → impact พร้อมเงื่อนไขจำเป็นและสมมติฐาน
- ออกแบบ logic model และตัวชี้วัด (indicators) ที่วัดได้
- วิธีประเมินผลกระทบ: counterfactual, contribution analysis, RCT เชิงนโยบาย, SROI (social return on investment)

## 8. Research Foresight

- horizon scanning, scenario planning, Delphi เพื่อตั้งโจทย์ที่ยังสำคัญในอนาคต
- เชื่อมกับยุทธศาสตร์ชาติและแนวโน้มโลก (เช่น BCG economy, SDGs)

## 9. หลักการเลือกเทคนิคขั้นสูง (กันใช้ของแพงผิดที่)

1. คำถามวิจัยต้องการอะไร (บรรยาย / สัมพันธ์ / เหตุ-ผล / ทำนาย / เข้าใจความหมาย)
2. โครงสร้างและขนาดข้อมูลเอื้อต่อเทคนิคนั้นหรือไม่
3. มี assumptions อะไรที่ต้องผ่าน และข้อมูลผ่านหรือไม่
4. ผลลัพธ์ตีความและสื่อสารต่อกลุ่มเป้าหมายได้หรือไม่
5. ทำซ้ำได้และโปร่งใสตามหลัก open science หรือไม่

> เทคนิคขั้นสูงไม่ได้ทำให้งานดีโดยอัตโนมัติ — โจทย์ที่คมและการออกแบบที่ตรงคำถามยังสำคัญกว่าเสมอ
