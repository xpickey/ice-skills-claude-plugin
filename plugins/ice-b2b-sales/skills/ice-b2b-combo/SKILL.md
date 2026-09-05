---
name: ice-b2b-combo
description: "ใช้เมื่อทำงานขายหรือก่อนการขายซอฟต์แวร์องค์กร Oracle Cloud, EBS, NetSuite หรือ FinTech ในไทย โดยต้องการ skill เดียวที่ครบทั้งวิธีขาย ความรู้ product spec เอกสาร และการตรวจก่อนส่ง — ยืนยัน product และขั้นการขายก่อนเสมอ · คำกระตุ้น: ทำข้อเสนอ, ตอบ TOR, เตรียม demo, qualify ดีล, เจรจาราคา"
license: MIT
---

# iCE B2B Sales — Combo Skill

ทักษะเดียวที่ทำงานขาย/พรีเซลล์ B2B Enterprise Software ครบวงจร — **route → know → build-spec → check** —
โดยโหลดรายละเอียดเฉพาะที่งานนั้นต้องการ (lazy-load) เพื่อให้เร็วและไม่เปลือง context.

สกิลนี้ทำงานเป็น **pipeline 6 ขั้น** ที่ต่อเนื่องกัน แต่ละขั้นมี: *เงื่อนไขเข้า → สิ่งที่ทำ → output ส่งต่อ*.
ขั้นต้นทางสุดคือ **Context Gate** — ต้องรู้ **product + sale stage** ก่อนเสมอ ถ้าไม่รู้ให้ถามก่อนทำสิ่งอื่น.

> **หลักการเขียนงาน (ทุก output):** ประโยคธุรกิจสมบูรณ์ระดับที่ปรึกษา-ผู้บริหาร · มีเหตุผล/trade-off เสมอ ·
> ไม่กุข้อมูล (ชื่อ/ตัวเลข/วันที่/เวอร์ชัน) — ไม่แน่ใจ = ถามหรือ flag · เขียนภาษาเดียวกับที่ผู้ใช้พิมพ์.

---

## ⏱️ Pipeline ภาพรวม

```
STEP 0  CONTEXT GATE     รู้ product + stage ก่อน (ไม่รู้ = ถาม)        [→ _capabilities/route.md]
STEP 1  ROUTE            เลือก mode + chain ของ reference ที่ต้องใช้     [→ _capabilities/route.md · decision-matrix.md]
STEP 2  LAZY-LOAD        เปิดเฉพาะ reference ใน chain (ไม่อ่านทั้งหมด)   [→ reference-index.md]
STEP 3  KNOW + VALIDATE  ตอบด้วยความรู้ + ตรวจข้อเท็จจริงก่อนยืนยัน      [→ _capabilities/know.md · web-validation.md]
STEP 4  BUILD-SPEC       ออก spec ของ deliverable (ไม่ build เอง)        [→ _capabilities/build-spec.md]
STEP 5  CHECK            QA ก่อนส่ง (detector ชี้ปัญหา ไม่แก้เงียบ)       [→ _capabilities/check.md · qa/pre-flight.md]

CONTEXT DISCIPLINE  — เช็คท้ายทุกขั้นเมื่องานยาว/หลายรอบ                  [→ context-discipline.md]
```

ไม่ใช่ทุกงานต้องครบ 6 ขั้น — งานตอบคำถาม (discovery/qualify) จบที่ STEP 3; งานมี deliverable (proposal/deck)
ไปถึง STEP 5. แต่ **STEP 0 ทำเสมอ**.

---

## STEP 0 — CONTEXT GATE (ทำก่อนเสมอ)

ก่อนตอบหรือลงมือใด ๆ ต้องตรึง 2 ค่านี้ให้ได้ก่อน:

1. **Product** — `Oracle Cloud (Fusion)` · `Oracle EBS` · `NetSuite` · `FinTech/Lending` · `ยังไม่เลือก/หลายตัว`
2. **Sale stage** — `Prospect` · `Discovery` · `Qualify` · `Solution` · `Proposal` · `Demo` · `Negotiate` · `Close` · `Onboard` · `QBR/Success` · `Renew/Expand`

**วิธีทำ:**
- **เดาจาก input ก่อน** — ถ้าผู้ใช้พิมพ์ "ทำ proposal NetSuite ช่วงยื่นข้อเสนอ" = รู้ครบ → ข้ามไป STEP 1 ทันที.
- **ไม่ชัด → ถามทีละ 1 ข้อ** (ไม่รวบหลายคำถาม): ถาม **product ก่อน** → ได้แล้วถาม **stage** → ถามเฉพาะตัวที่ขาด.
- **อย่าเดาเงียบ ๆ** ถ้าเดาผิดทั้ง pipeline จะเลือก reference ผิด.

**เมื่อ signal ขัดกัน/ไม่ครบ (ถามตัวที่กระทบมากที่สุดก่อน):**
- **product ขาด แต่ domain ชัด** (เช่น "ตอบ TOR e-GP" — รู้ว่าภาครัฐ แต่ไม่รู้ product) → ถาม **product ก่อน** (กระทบ chain มากสุด) — อย่าเดา product จาก domain.
- **stage ขัดกัน** (เช่น "ร่าง proposal ช่วง qualify" — proposal=stage หลัง, qualify=stage ต้น) → ถาม **stage** ให้ชัด (proposal คือ deliverable หรือกำลัง qualify อยู่?).
- **product หลายตัว** (เทียบ Oracle vs NetSuite) → ไม่ต้องล็อกตัวเดียว — ใช้ Primary-Lock ใน STEP 3 (ดู `_capabilities/know.md`).
- **กฎ:** ถามตัวที่ผิดแล้วเสียหายมากสุดก่อน (product กระทบ chain · stage กระทบ method) — ไม่ถามทุกอย่างรวด.

**EXPLORATION MODE (ยังไม่รู้ product — งาน early-advisory):** งานขายจริงหลายงานเริ่มจาก *pain / industry / TOR / incumbent / คู่แข่ง* โดยยังไม่รู้ product/stage. กรณีนี้ **ไม่ต้องบังคับถาม product ก่อนเสมอ** — เริ่มจาก business problem ได้เลย โดย:
- ตั้ง **`product = ยังไม่เลือก`** ใน Context-Lock อย่างชัดเจน.
- **ห้าม product-claim** (อ้าง feature/fit/ราคาของ product ใด) จนกว่าจะยืนยัน product — ตอบเชิง business/industry ก่อน.
- พอบทสนทนาแคบลงถึงจุดที่ต้องผูก product (fit-gap/pricing/proposal) → **ถาม product ตอนนั้น**.

**ask vs flag — กฎเด็ดขาด (อย่าให้ขัดกัน):**
- **customer-facing / contract / legal / pricing / product-feature / ตัวเลขในข้อเสนอ** → **ต้องถามหรือ validate** (ไม่ flag แล้วเดินต่อ).
- **internal draft / hypothesis / supporting detail** → **flag แล้วเดินต่อได้** (ระบุว่าเป็นสมมติฐาน).

**CONTEXT-LOCK:** เมื่อรู้แล้ว ให้จด *canonical facts* ของงานนี้ไว้เป็นชุดเดียว — customer, product, scope,
ตัวเลขสำคัญ (งบ/จำนวน user/timeline ถ้ามี), ภาษา output. ทุกขั้นถัดไป **อ้างชุดนี้ชุดเดียว** เพื่อกันตัวเลข/ชื่อ
ขัดกันข้ามเอกสาร. ถ้าผู้ใช้ให้ตัวเลขมาทีหลัง → อัปเดตที่ชุดนี้ที่เดียว.

> รายละเอียดเทคนิค Context-Lock + การจัดการเมื่อมีหลาย opportunity → `references/_capabilities/route.md`

---

## STEP 1 — ROUTE (เลือก mode + chain)

### 1.1 เลือก Mode (งบ orchestration)
ค่าเริ่มต้น = **Fast**. เลือกตามเกณฑ์ชัด (เรียงจากชัดสุด):

| ถ้า input มี… | → Mode | เพราะ |
|---|---|---|
| ชื่อ deliverable file ชัด: "proposal / deck / TOR / business case" | **Submit** | มีไฟล์ส่งจริง → ผ่าน STEP 4-5 ครบ |
| "เสนอผู้บริหาร/board รับรอง" หรือ "เลือกระหว่าง X กับ Y" | **Full** | high-stakes/multi-option → ดู 3 มุม |
| "ร่างภายใน / ดูคร่าว ๆ / discovery prep / email / คำถามเดียว" | **Fast** | งานเดี่ยว reversible |

- **"ร่าง proposal" (ไม่ระบุส่งใคร)** → เริ่ม **Fast** แต่ **เตือน**: "นี่เป็นร่าง — ถ้าจะส่งลูกค้าจริง ต้องผ่าน Submit + QA เต็มก่อน" (RATCHET — ดู STEP 5).
- ยังไม่ชัดหลังดูเกณฑ์ → **ถามครั้งเดียว** ("งานนี้ส่งลูกค้าเลยไหม / อยากให้ลึกแค่ไหน").

### 1.2 Routing 4 คำถาม (first-hit-wins — ตอบตามลำดับ ห้ามข้าม)
1. **Q1 Deliverable** — งานนี้ผลิตอะไร? (proposal/RFP-TOR/business-case/account-plan/discovery-guide/demo-script/QBR/email)
   → ตั้งโครงงานทั้งหมด. ดู `decision-matrix.md` ถ้า deliverable กำกวม.
2. **Q2 Product** — ผูกกับ product ไหน (จาก STEP 0)? → กำหนด `product/<x>.md` ที่ต้องโหลด.
3. **Q3 Domain overlay** — แตะภาครัฐไทย (GFMIS/e-GP) · ภาษีไทย (e-Tax/VAT/WHT) · FinTech/IFRS9 ไหม? → เพิ่ม `domain/<y>.md`.
4. **Q4 Industry context** — อุตสาหกรรมลูกค้า (manufacturing/retail/banking/SOE)? → ไม่เพิ่มไฟล์เสมอ แต่ใช้ปรับภาษา/KPI.

**ผลลัพธ์:** chain ของ reference ที่ต้อง lazy-load (STEP 2) — **ไม่เกิน 5 ไฟล์** ต่องาน. ถ้าเกิน = งานกว้างไป
ให้ถามผู้ใช้ว่าจะโฟกัสส่วนไหนก่อน.

### 1.3 Anti-Loop cap
ถ้างานวนแก้ไปมา: Fast = วนได้ 1 รอบ · Full = 2 · Submit = 3. ครบ cap แล้วยังไม่ลงตัว → **STOP แล้วเสนอ
trade-off ให้ผู้ใช้เลือก** (ไม่วนต่อเอง).

> default chains (Pre-sales / Strategic / Communication) + decision logic เต็ม → `references/_capabilities/route.md`

---

## STEP 2 — LAZY-LOAD (เปิดเฉพาะที่เกี่ยว)

เปิดอ่าน **เฉพาะ** reference ใน chain จาก STEP 1 — ไม่อ่านทั้ง library:
- `references/method/<x>.md` — วิธีขาย/วิธีคิด (ดูตารางด้านล่าง)
- `references/product/<y>.md` — ความรู้ product
- `references/domain/<z>.md` — overlay ไทย/vertical (ถ้ามี)
- `references/_shared/*.md` — เปิด **เมื่อ reference ข้างบนชี้มา** (เช่น method ชี้ไป `_shared/meddpicc.md`)

**ถ้า reference ที่ต้องการเปิดไม่ได้/ไม่มี** → อย่าหยุดงาน: สังเคราะห์จาก `_capabilities/` (route+know) + ความรู้ทั่วไป
แล้ว **flag ชัด** ว่า "อ้างอิงจากหลักการทั่วไป — ไม่ได้โหลด reference เฉพาะ [ชื่อ]" + ลด confidence (ดู `_capabilities/know.md`).

**Load-budget (ทำให้ lazy-load efficient จริง ไม่ใช่แค่ ≤5 ไฟล์):**
- จัดลำดับ reference เป็น **mandatory** (ต้องอ่าน) · **optional** (อ่านถ้าเหลือ budget) · **skip** (ไม่เกี่ยว).
- **อ่านเฉพาะ section ที่ตรง intent** — เริ่มจาก heading ที่ตรง ไม่อ่านทั้งไฟล์ (ทุก reference มีหัวข้อชัด).
- งานเดี่ยว/คำถามเดียว → 1-2 ไฟล์ mandatory พอ · งานใหญ่ (proposal) → ครบ chain แต่ section-level.

**Index ของ reference (โหลดตัวไหนเมื่อไหร่):**

| งาน/สัญญาณ | method ที่โหลด | product/domain เพิ่ม |
|---|---|---|
| Discovery / ตั้งคำถาม | `method/questioning.md` | — |
| Qualify / MEDDPICC | `method/solution-selling.md` → `_shared/meddpicc.md` | — |
| กลยุทธ์ดีล / account plan | `method/strategic-thinking.md` → `_shared/why-stack.md` | — |
| Business case / pain→value | `method/solution-selling.md` + `method/why-thinking.md` | product ที่เกี่ยว |
| Workshop / envisioning | `method/design-thinking.md` | — |
| ความสัมพันธ์ / QBR / renewal | `method/relationship-management.md` | — |
| segment playbook (gov/large/SME) | `method/enterprise-sale-strategy.md` | — |
| งานผูก Oracle Cloud | (ตาม deliverable) | `product/oracle-cloud.md` |
| งานผูก Oracle EBS | (ตาม deliverable) | `product/oracle-ebs.md` |
| งานผูก NetSuite | (ตาม deliverable) | `product/netsuite.md` (+ `product/netsuite-thailand.md` ถ้าลูกค้าไทย) |
| ภาครัฐไทย / TOR | strategic + solution-selling | `domain/govt-gfmis.md` + `domain/govt-egp.md` |
| ภาษีไทย / localization | (ตาม deliverable) | `domain/th-etax.md` |
| FinTech / lending / IFRS9 | solution-selling | `domain/fintech.md` |

> ดัชนีเต็ม + disambiguation → `references/reference-index.md`

---

## STEP 3 — KNOW + VALIDATE (ตอบด้วยความรู้ + ตรวจก่อนยืนยัน)

เมื่อตอบด้วยความรู้ product/domain/method — ใช้วินัยนี้ทุกข้อที่อ้าง:

### 3.1 FACT / PATTERN / ASSUMPTION gate
ทุกข้ออ้าง (ตัวเลข, เวอร์ชัน, feature, กฎหมาย, man-day) ติด tag ในใจ:
- **FACT** — มีในแหล่ง/reference จริง → ระบุได้ว่ามาจากไหน.
- **PATTERN** — อนุมานจากแบบทั่วไป → บอกผู้ใช้ว่า "โดยทั่วไป/benchmark" ไม่ใช่ตัวเลขจริงของลูกค้า.
- **ASSUMPTION** — เดา/ไม่มีแหล่ง → **flag ชัดว่า "ต้องยืนยัน"** ห้ามนำเสนอเป็นข้อเท็จจริง.

**Self-check ก่อนตอบ:** ถ้าเป็น ชื่อ/ตัวเลข/วันที่/เวอร์ชัน ที่ไม่มีแหล่ง → **ถามผู้ใช้ หรือ flag — ไม่เดา** (P5/H3).

### 3.2 Primary-Lock (กันความรู้ปนกัน)
ถ้าต้องเทียบหลาย product (Oracle vs SAP vs MS) → ล็อก **primary 1 ตัว** ตอบหลักจากตัวนั้น · เทียบตัวอื่นใน
**ตาราง/section แยกชัด** (ไม่ปนในย่อหน้าเดียว) · เทียบเสร็จกลับมาตอบ primary ต่อ.

### 3.3 Web research + Validation (tool-agnostic)
เมื่อข้อมูลเป็น ASSUMPTION หรือเป็นเรื่อง version-specific / กฎหมาย / ตัวเลขตลาด ที่ต้องแม่น:
- **ค้น web** (ใช้เครื่องมือค้นที่มีในสภาพแวดล้อมนั้น — ไม่ผูกตัวใดตัวหนึ่ง) → **cross-check ≥ 2 แหล่งอิสระ** → **cite**.
- ขัดกัน/ไม่เจอ → **flag ไม่เดา**. ออก confidence: high/medium/low.
- low + high-stakes → แนะนำให้ขอ second-opinion ก่อนใช้ (ผู้ใช้ตัดสิน).

> protocol เต็ม (เมื่อไหร่ต้องค้น, เกณฑ์ cross-check, รูปแบบ cite) → `references/web-validation.md`
> เทคนิค confidence/gap/needs-input → `references/_capabilities/know.md`

ถ้างานเป็นการตอบ/ให้คำแนะนำล้วน (ไม่มีไฟล์ส่งมอบ) — **จบที่ STEP 3** แล้วข้ามไป Context Discipline.

---

## STEP 4 — BUILD-SPEC (ออก spec ของ deliverable)

เมื่องานมีไฟล์ส่งมอบ (.pptx / .docx / .xlsx) — สกิลนี้ **ออก spec ให้เครื่องมือสร้างเอกสารใด ๆ ทำตาม
ไม่ build เอง** (portable — ไม่ผูก builder ตัวใดตัวหนึ่ง). spec ต้องระบุ:

- **Font discipline (D1-D4):** tri-slot ทุก text run (latin + ea + cs) · normalize ให้เหลือ ≤12 ฟอนต์ ·
  ไทย optical size ≥18pt และใหญ่กว่าอังกฤษ +1-2pt · ไม่มี object ทับกัน + ฝังฟอนต์.
- **Char/build guards (บทเรียนสำคัญ):** แทน `→` (U+2192) ด้วย `▸` · ล้าง avLst เมื่อเปลี่ยน preset shape ·
  ทุกย่อหน้ามี endParaRPr · 16:9 lock.
- **Build-vs-Edit:** เอกสารใหม่หรือแก้ >5 สไลด์ = สร้างใหม่ทั้งชุด · ≤5 สไลด์ = แก้ในไฟล์เดิม (ไม่ rebuild).
- **Preview-First:** ถ้า infographic มีได้หลายแนว → เสนอ 2-3 แนวให้ผู้ใช้เลือกก่อนสร้างเต็ม (ไม่เสียเวลาสร้างผิดแนว).

> spec template เต็ม + 18 บทเรียน build + font strategy TH/EN → `references/_capabilities/build-spec.md`

---

## STEP 5 — CHECK (QA ก่อนส่ง)

ตรวจ deliverable ก่อนส่ง — บทบาทคือ **detector ชี้ปัญหา + หลักฐาน ไม่แก้เงียบ ๆ** (ให้ผู้ใช้/ขั้นถัดไปตัดสินแก้).

**Speed-Tier (เลือกความเข้มตามความเร่ง/ความเสี่ยง):**
- **DRAFT** — ร่างภายใน ไม่ต้อง QA.
- **FAST** — ตรวจ 3 มิติที่พังเห็นทันที: Completeness · Anti-Hallucination · Font/Layout.
- **FULL** — ตรวจครบ 9 มิติ. **บังคับ FULL เสมอถ้าเป็น final ส่งลูกค้า** (RATCHET — ร่างห้ามหลุดเป็นจริง).

**9 มิติ (FULL):** Requirement · Completeness · Consistency+Anti-Hallucination · Logic · **Anti-AI** ·
Brand · **Font/Layout (hard-block ถ้า customer-facing)** · Wording (positive 70/25/5) · Compliance (เทียบ TOR ทีละข้อ).

- **Anti-AI** ใช้แนวทางจากสกิลตรวจภาษา AI ที่มีในสภาพแวดล้อม (ไม่คัดลอกมาซ้ำในสกิลนี้ — ชี้ไปแหล่งเดียว).
- **Font/Layout** customer-facing + ละเมิด = **hard-block** (ฟอนต์ไทยตก/ไฟล์เปิดไม่ได้ = ส่งไม่ได้).
- **Producer ≠ Checker:** ในอุดมคติให้คนละ context ตรวจ (ผู้สร้าง ≠ ผู้ตรวจ) เพื่อเลี่ยง bias.

> 9-dimension เต็ม + Delta Re-QA (ตรวจเฉพาะที่แก้) + pre-flight checklist → `references/_capabilities/check.md` · `references/qa/pre-flight.md`

---

## CONTEXT DISCIPLINE (จัดการ context เมื่องานยาว)

เช็ค **ท้ายทุกขั้น** เมื่องานยาว/หลายรอบ — เพื่อไม่ให้ context บวมจนช้า/แพง:

**Worth-It check** (compact เมื่อครบ 3 ข้อเท่านั้น):
- **SAFE** — งานสำคัญเซฟลงไฟล์แล้ว · ไม่มี gate/approval ค้าง · ไม่มีอะไรยังไม่บันทึก.
- **PAYOFF** — ยังเหลืองานเยอะ **และ** ขั้นถัดไปใช้ context น้อยกว่าที่แบกอยู่ตอนนี้มาก. *(ประเมิน PAYOFF ก่อน —
  ถ้าเป็นงานสุดท้ายไม่มีอะไรต่อ = ไม่ compact)*.
- **NO-THRASH** — ขั้นถัดไปจะไม่รีบอ่านสิ่งที่เพิ่ง drop กลับมาทันที.

**Keep set = pointers ไม่ใช่ payload:** เก็บแค่ *โฟกัสปัจจุบัน + next action เดียว + path ของไฟล์ state/หลักฐาน*.
เนื้อหาหนักอ่านกลับจาก path ทีหลัง (path กินไม่กี่ token · ไฟล์หลังมันกินเป็นพัน).

**จำแนกขอบเขตเมื่อ context สูง:**
- **TERMINUS** (งานจบ ไม่มีต่อ) → สรุปแล้วหยุด — **ไม่ compact**.
- **CONTINUATION** (มีงานต่อชัด หรือผู้ใช้บอกทำต่อ) → compact แล้วทำต่อ (confirm → compact → work).
- **GREY ZONE** (มีแค่งาน optional) → ถามผู้ใช้ก่อน compact เฉพาะเมื่อยืนยัน.

> เหตุผลเต็ม + วิธีเขียน keep-set → `references/context-discipline.md`

---

## หลักการประจำตัวสกิล (ยึดทุกงาน)

1. **Context ก่อน** — product + stage ต้องชัดก่อนทำ (STEP 0).
2. **ไม่กุข้อมูล** — ชื่อ/ตัวเลข/วันที่/เวอร์ชัน ไม่มีแหล่ง = ถามหรือ flag (STEP 3).
3. **โหลดเท่าที่ใช้** — lazy-load เฉพาะ chain (STEP 2) ไม่อ่านทั้ง library.
4. **ส่งมอบ= ออก spec** — ไม่ build เอง ให้ tool ใด ๆ ทำตาม (STEP 4) → portable.
5. **ตรวจก่อนส่ง** — detector ชี้ปัญหา ไม่แก้เงียบ · final = FULL QA (STEP 5).
6. **ภาษา mirror** — ตอบภาษาเดียวกับที่ผู้ใช้พิมพ์ · ถามภาษาไฟล์ก่อนถ้าไม่ชัด.
7. **จัดการ context** — งานยาว = ประเมิน Worth-It · keep pointers ไม่ใช่ payload.
