# 02a — Literature Search Strategy (PICO → คำค้น → Boolean)

> **Authority Source:** ดัดแปลงวิธีการจาก Prompt อบรมนักวิจัยรุ่นใหม่ (สำนักงานการวิจัยแห่งชาติ วช./NRCT) — "Prompt for Literature Review (Search Strategy)" ปรับให้เข้ากับมาตรฐาน JPSPA TCI Tier 1
>
> **ใช้เมื่อ:** **Stage 2 (Literature Review)** — *ก่อน* ส่งงานให้ `notebooklm-connection` ค้น/filing เพื่อเตรียมคำค้นให้ครบและคม
>
> **ขอบเขต:** เป็น *ขั้นตอนคิดเพื่อสร้างคำค้น* ไม่ใช่เนื้อหาที่เขียนลงบทความ — ผลลัพธ์คือชุดคำค้นที่ป้อนเข้า Stage 2 และเอกสารที่ค้นพบต้องผ่าน 4-Pillar Citation Audit (RULE 13) ก่อนนำไปอ้าง

---

## สารบัญ

- [PART A — PICO/PICo Interpretation](#part-a)
- [PART B — คำค้น 2 ภาษา (กว้าง/แคบ/คำพ้อง)](#part-b)
- [PART C — Boolean String](#part-c)
- [PART D — Bridge เข้า Lifecycle + Guard](#part-d)

---

<a id="part-a"></a>

## PART A — ตีความ PICO/PICo จากหัวข้อ

แตกหัวข้อบทความเป็นองค์ประกอบ (เชิงเปรียบเทียบใช้ PICO · เชิงปรากฏการณ์/คุณภาพใช้ PICo):

| องค์ประกอบ | ความหมาย | หมายเหตุ |
|---|---|---|
| **P** (Population) | ประชากร/หน่วยศึกษา เช่น อปท., รัฐวิสาหกิจ, ข้าราชการ | — |
| **I** (Intervention / Phenomenon of Interest) | สิ่งที่ศึกษา/ปรากฏการณ์ เช่น e-GP, ธรรมาภิบาล, ภาวะผู้นำ | — |
| **C** (Comparator) | กลุ่ม/แนวทางเปรียบเทียบ | *ถ้าไม่มี ปล่อยว่าง — อย่าแต่งให้มี* |
| **O** (Outcome) | ผลลัพธ์ที่สนใจ เช่น ประสิทธิผล ความโปร่งใส | — |
| **Context** | บริบทไทย / รปศ.-รัฐศาสตร์ / มิติพุทธ | ใช้ผูก Buddhist Integration (Stage 3) ภายหลัง |

---

<a id="part-b"></a>

## PART B — สร้างชุดคำค้น 2 ภาษา (กว้าง / แคบ / คำพ้อง)

1. **EN keyword 20–30 คำ** จัดกลุ่มตาม PICO (population / intervention-phenomenon / comparator-ถ้ามี / outcome / context)
2. **TH keyword เทียบเคียง** + **คำพ้อง / การสะกดหลายแบบ** (เช่น "ธรรมาภิบาล / good governance"; "ดิจิทัล / ดิจิตอล / digital")
3. เสนอ **ศัพท์กว้าง ↔ ศัพท์แคบ** ต่อกลุ่ม (กว้างไว้ค้นรอบแรก · แคบไว้คัดกรอง)

| กลุ่ม PICO | EN keywords | TH เทียบเคียง + คำพ้อง | กว้าง / แคบ |
|---|---|---|---|
| Population | | | |
| Intervention/Phenomenon | | | |
| Comparator (ถ้ามี) | | | |
| Outcome | | | |
| Context (ไทย/พุทธ/รปศ.) | | | |

---

<a id="part-c"></a>

## PART C — ประกอบ Boolean String (ต่อฐานข้อมูล)

- รูปแบบ: `(synonym1 OR synonym2 OR ...) AND (synonym1 OR ...) AND ...` ต่อกลุ่ม PICO
- เสนอ **คำตัดออก (NOT / exclusion)** ที่อาจทำให้เกิด false positives
- ปรับ syntax ตามฐาน: **ThaiJO** (so08.tci-thaijo.org — รองรับไทย) · **Google Scholar** (วลีในเครื่องหมายคำพูด, `intitle:`) · **TCI/TDC** — *ผู้เขียนปรับตามหน้าจริงของแต่ละฐาน*

---

<a id="part-d"></a>

## PART D — Bridge เข้า Lifecycle + Guard

**Bridge → Lifecycle JPSPA (บังคับ — ห้ามข้าม):**

| ผลจาก Search Strategy | ป้อนเข้าตรงไหน |
|---|---|
| ชุด keyword + Boolean | **Stage 2 Literature Review** — ส่งให้ `notebooklm-connection` ค้น/filing/tagging |
| เอกสารที่ค้นพบจริง | ต้องผ่าน **4-Pillar Citation Audit** (RULE 13) + เกณฑ์ TCI Tier 1 ก่อนนำไปอ้าง |
| Context (พุทธ/รปศ.) | input ของ **Stage 3** Theoretical Framework & Buddhist Mapping |

**Guard (Anti-Hallucination — ผูกกับ governance jpspa):**
- **คำค้น = สมมติฐานการสืบค้น** — เอกสารจริงต้องมาจากการค้น Stage 2; **ห้าม hallucinate** ผู้แต่ง/ปี/ชื่อบทความ (RULE 2 Source Integrity)
- เอกสารที่นำมาอ้างต้องสอดคล้องเกณฑ์ TCI Tier 1: **Recency ≥ 50% (5 ปีล่าสุด) + International 30–50%** (RULE 10/13)
- ไม่แน่ใจคำเทียบเคียง/ศัพท์เทคนิค → ระบุ **"ต้องตรวจโดยผู้วิจัย"**
- แยกชัด: **คำค้นที่เสนอ** (ของ Claude) ≠ **เอกสารที่พบจริง** (ผ่าน Stage 2 + Citation Audit)
