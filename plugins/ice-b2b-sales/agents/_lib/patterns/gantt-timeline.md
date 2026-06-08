# Gantt / Project Timeline — Design Spec (Reusable Pattern)

> **Owner:** deliverable-gen-agent | **Version:** V01R01 | **Date:** 2026.06.03
> **Source:** สกัดจาก Ascend EPM Phase II deck V5 (slide 33-36) — Gantt ที่ผ่านงานจริง + User อนุมัติ
> **Purpose:** ให้ deliverable-gen สร้าง Project Timeline / Gantt แบบ detailed schedule ได้ในรูปแบบเดิม
>             โดย "ไม่ต้องให้ผู้ใช้ส่งภาพตัวอย่างทุกครั้ง" — ใช้ spec นี้เป็น reference

---

## เมื่อไหร่ใช้ pattern นี้

เมื่อผู้ใช้ขอ: Project Timeline · Project Plan · Gantt · implementation schedule · roadmap
รายโครงการ (1 หน้า/โครงการ) ที่มี activity rows + แกนเวลาเดือน + ownership (ใครรับผิดชอบ)

---

## โครงสร้าง Layout (1 slide ต่อ 1 โครงการ — 16:9)

```
┌────────────────────────────────────────────────────────────────────┐
│ PROJECT 0N — PROJECT TIMELINE & MILESTONES            [navy header]  │
│ [ชื่อโครงการ] · [module] · [N] months                                │
├────────────────────────────────────────────────────────────────────┤
│ Phase header (chevron, 4 ช่วง):                                      │
│   1 Analysis & Design · 2 Build & Configure · 3 Test & Deploy ·      │
│   4 Go-Live                                                          │
├──────────────────────────────┬─────────────────────────────────────┤
│ PROJECT ACTIVITIES (ซ้าย)     │ Timeline (months) M0 M1 M2 ... MN    │
│  1  Project planning...       │ ▓▓▓ (bar สี ownership)                │
│  2  Kick-off meeting          │   ▓                                  │
│  3  Requirement workshops     │   ▓▓▓                                │
│  ...(≤12 rows)                │      ▓▓▓▓                            │
│  N  Warranty & support        │              ▓▓                      │
│  ★  Joint working & Steering   │ ──────────── (band ตลอดแนว)          │
├──────────────────────────────┴─────────────────────────────────────┤
│ LEGEND: ◼ Joint—iCE+Ascend  ◼ iCE  ◼ Ascend(Customer)               │
│ Indicative RACI & durations — fine-tuned in Discovery  [footer flag] │
│ [ชื่อลูกค้า] [โครงการ] | Confidential                                │
└────────────────────────────────────────────────────────────────────┘
```

---

## องค์ประกอบบังคับ (จาก Ascend จริง — 126 shapes/slide)

### 1. Activity rows (≤12 แถว — ถ้าเกินให้ compress)
ชุดมาตรฐาน 12 activity (EPM/ERP implementation):
```
1  Project planning, team & deliverable templates
2  Kick-off meeting
3  Requirement gathering workshops
4  Solution design & fit-gap; data-migration plan
5  Design sign-off                          [milestone]
6  Build & configure (module, ODI, unit test)
7  Source data preparation (initial load)
8  UAT data & environment; key-user training
9  UAT execution & sign-off                 [milestone]
10 Cutover & PROD environment setup
11 Go-Live                                   [milestone]
12 Warranty & post-Go-Live support (1 mo)
★  Joint working & Steering Committee (throughout)
```
> ปรับ activity ตามโครงการจริงได้ แต่คงโครง 4 phase (Plan→Build→Test→Go-Live)

### 2. แกนเวลา (month axis)
- M0 ถึง MN (N = duration เดือนของโครงการ — เช่น 6 months → M0-M6)
- ปรับความกว้างคอลัมน์ให้พอดี 16:9 (ดู Y-budget ด้านล่าง)

### 3. Ownership color (สกัดจริง — ใช้ชุดนี้)
```
iCE                = teal   #0891B2
Ascend (Customer)  = gold   #C99700
Joint (iCE+Ascend) = light  #BFD9E6  + ★ marker
```
> ถ้าลูกค้าอื่น: เปลี่ยน "Ascend" เป็นชื่อลูกค้า + ปรับสี gold เป็นสี CI ลูกค้า (customer-ci-finder)

### 4. Theme color (navy base — สกัดจริง)
```
navy bg        #1E293B / #0D2137 / #122840
panel light    #F4F8FB
text on navy   #FFFFFF
risk/alert     #C0392B  (ถ้ามี)
```

### 5. Footer flag (anti-hallucination — บังคับ)
```
"Indicative RACI & durations — fine-tuned in Discovery"
```
> ⭐ สำคัญ: timeline/RACI/duration เป็นค่าประมาณเสมอ (ถ้าไม่มีใน SOW) — ต้อง flag ชัดว่า indicative
>          ห้ามนำเสนอเป็นตัวเลขยืนยันถ้ายังไม่ได้ confirm กับลูกค้า (anti-hallucination)

---

## ก่อนสร้าง — ต้องถาม/ยืนยันอะไร (อิง Ascend RW-6/RW-7)

```
1. ownership mapping (RACI): activity ไหนใครทำ (iCE/Ascend/Joint) — ถ้าไม่มี → เสนอ RACI มาตรฐานให้ดูก่อน
2. duration ต่อ phase: ถ้าไม่มีใน SOW → เสนอสัดส่วน (เช่น Plan 0.25 เดือน, Build หนักสุด) ให้ดูก่อน — ห้ามเดาเงียบ
3. row density: ถ้า activity > 12 → ขอลด/รวม (กัน overflow)
4. warranty/support: อยู่ใน duration หรือแยก — เช็ก SOW จริง
```

---

## Y-budget (กัน overflow — แก้ Ascend RW-7)

```
16:9 slide = 12.19m (W) × 6.858m (H) [EMU: 12192000 × 6858000]
จองพื้นที่: header ~1.2m · phase chevron ~0.5m · footer/legend ~1.0m
เหลือสำหรับ grid: ~4.0m → 12 rows = ~0.33m/row (พอดี)
⚠️ ถ้า rows > 12 หรือ activity name ยาว → ลด row หรือย่อข้อความ ก่อน render (ไม่ใช่ render แล้วค่อยเจอ)
เช็ก collision: legend ไม่ตกขอบ · chevron ไม่ wrap (ใช้เลขล้วนถ้าแคบ)
```

---

## Build Discipline (ใช้ร่วม D1-D4 เสมอ)

- Tri-slot font (latin+ea+cs) ทุก text run — TH ใน activity names ต้องมี `<a:cs>` Sarabun
- ไม่มี object ทับซ้อน (Strict Validator)
- เปิด PowerPoint จริงก่อน return (qlmanage false-green)

---

*Gantt Timeline Design Spec V01R01 | source: Ascend EPM deck V5 slide 33-36 | for deliverable-gen reuse*
