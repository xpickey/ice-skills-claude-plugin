# 09 — Fact Audit
## Citation Verification + Hallucination Check + Cross-Chapter Consistency

**Version:** V01R01 | **Date:** 2026-05-03

---

## 1. Mission

ไฟล์นี้คือ **Fact Audit Reference** — ตรวจสอบความถูกต้องของข้อเท็จจริงในดุษฎีนิพนธ์ก่อนยื่นสอบ/ส่งเล่ม เพื่อป้องกัน Hallucination และให้ตรงกับมาตรฐาน มจร ที่เคร่งครัดเรื่องแหล่งอ้างอิง

**Authority Hierarchy:**
- **Level 1:** คู่มือ มจร — กฎ "ห้ามดึงผลจากหนังสือ" + "ระดับ ป.เอก เท่านั้น"
- **Level 2:** NotebookLM Corpus (`state/notebooklm-corpus.md`) — Source-traceable record
- **Level 3:** Bibliography ของเล่ม — Cross-reference checkpoint

Skill จะอ่านไฟล์นี้เมื่อ
1. ผู้ใช้กล่าวถึง "ตรวจอ้างอิง", "verify citation", "hallucination", "fact audit"
2. ก่อน Gate 2 + Gate 3 — Final Audit ก่อนสอบ
3. ก่อนส่งเล่ม Final Submission

---

## 2. 3-Layer Detection Architecture

```
┌──────────────────────────────────────────────┐
│ Layer 1 — Pattern-based Hallucination Check  │
│ ตรวจ pattern ที่ AI สร้างชื่อปลอม              │
└──────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────┐
│ Layer 2 — Cross-reference Audit              │
│ in-text citation ↔ บรรณานุกรม ↔ คำย่อ        │
└──────────────────────────────────────────────┘
              ↓
┌──────────────────────────────────────────────┐
│ Layer 3 — Source-trace Verification          │
│ ทุก citation มี Search ID ใน corpus.md        │
│ + MCP source_get_content เพื่อ Verify Quote    │
└──────────────────────────────────────────────┘
              ↓
        Final: Pass / Issue List
```

---

## 3. Audit Coverage by Chapter

### 3.1 Critical Chapters (Strictest Audit)

**Chapter 2 — Literature Review**
- ทุก citation ต้องมี Source ใน corpus
- ระดับ ป.เอก เท่านั้น (ห้าม ป.โท)
- มจร อ้างอิง ≥ 60%
- พระไตรปิฎก เลขเล่ม/ข้อ/หน้า ถูกต้อง

**Chapter 4 — Results**
- ⚠️ **CRITICAL:** ผลทั้งหมดจากสัมภาษณ์/แบบสอบถามจริงเท่านั้น — ห้ามอ้างหนังสือ
- ตัวเลข/% ตรงกับ raw data
- ตารางแจกแจงความถี่ตรงกับจำนวนผู้ให้ข้อมูล
- ไม่มี citation ที่ไม่ใช่ผลตรง

**Chapter 5 — Discussion**
- ระดับ ป.เอก เท่านั้นใน Discussion
- ทุกประเด็นเชื่อมงานวิจัยในบทที่ 2
- ข้อเสนอแนะมาจากผลวิจัยจริง

### 3.2 Standard Chapters

**Chapter 1, 3** — ตรวจมาตรฐาน Citation + Numbers + Dates

---

## 4. Layer 1 — Pattern-based Hallucination Detection

### 4.1 AI Hallucination Signatures

**(H1) ชื่อผู้แต่งทั่วไปไม่มีจริง**
- ✗ "Smith (2023)", "Johnson (2022)" ที่ไม่มีในบรรณานุกรมและไม่มีใน corpus
- ✓ ตรวจชื่อผู้แต่งจริงผ่าน NotebookLM / Google Scholar

**(H2) ปีพิมพ์ไม่ตรงกับยุคของเนื้อหา**
- ✗ "Spencer (1850)" เรื่องสมรรถนะ (Spencer & Spencer ของจริงคือ 1993)
- ✓ ปีตรงกับ historical context

**(H3) Citation pattern สม่ำเสมอเกินไป**
- ✗ ทุกบรรทัดมีอ้างอิง 1 ตัว / ผู้แต่งหลายคนปีติดกันผิดธรรมชาติ
- ✓ Citation pattern จริงมีความผันผวน

**(H4) Quote ที่ "ดูดี" เกินจริง**
- ✗ Quote ที่ generic ไม่มี source identifier
- ✓ Verify quote ผ่าน MCP `source_get_content`

**(H5) เลขพระไตรปิฎกที่ไม่มีอยู่จริง**
- ✗ "ที.ม. (ไทย) ๑๕/๙๙๙/๙๙๙๙" (เกินช่วงเลขจริง)
- ✓ ตรวจกับฐานข้อมูล มจร / 84000.org

**(H6) Journal ไม่มีอยู่จริง**
- ✗ "วารสารวิจัยที่ไม่มี ISSN"
- ✓ ตรวจ ISSN + ใน TCI / Scopus

**(H7) วิทยานิพนธ์ที่ไม่มีใน TDC**
- ✗ ดุษฎีนิพนธ์ที่อ้างไม่มีใน TDC
- ✓ ตรวจ TDC + คลัง มจร

### 4.2 Pattern Scan Workflow

```
Step 1: Extract ทุก citation pattern
   - "ผู้แต่ง (ปี)" / "Author, Year"
   - "ผู้แต่ง, ชื่อเรื่อง, ปี"
   - เลขพระไตรปิฎก "X.X. (X) X/X/X"

Step 2: ตรวจ pattern กับ Hallucination Signatures (H1-H7)

Step 3: List potential hallucinations
   - Confidence: HIGH / MEDIUM / LOW
   - Reason: ระบุ signature ที่ trigger

Step 4: Verify ด้วย Layer 2 + Layer 3
```

---

## 5. Layer 2 — Cross-reference Audit

### 5.1 In-text ↔ Bibliography

**กฎ:** ทุก citation ในเชิงอรรถ ต้องมีในบรรณานุกรม + ไม่ส่วนเกินกัน

**Workflow:**
```
1. List ทุก citation ที่ปรากฏในเชิงอรรถ (ทุกบท)
2. List ทุก entry ในบรรณานุกรม
3. Cross-check
   - ✓ Citation มีในบรรณานุกรม?
   - ✓ บรรณานุกรม มี citation จริง?
   - ❌ ลำดับชื่อ-นามสกุล ตรงกัน
4. Report
   - Missing in Bibliography (ต้องเพิ่ม)
   - Unused in text (ต้องลบจากบรรณานุกรม)
```

### 5.2 Symbols ↔ Footnote

**กฎ:** ทุกคำย่อพระไตรปิฎกในเชิงอรรถ ต้องมีในคำอธิบายสัญลักษณ์

**Workflow:**
```
1. Extract คำย่อพระไตรปิฎกจากเชิงอรรถ
2. Cross-check กับคำอธิบายสัญลักษณ์
3. Report missing
```

### 5.3 TOC ↔ Content

**กฎ:** หัวข้อ + เลขหน้าใน TOC = หัวข้อ + เลขหน้าในเนื้อหา 100%

**Workflow:**
```
1. Extract ทุกหัวข้อใน TOC + เลขหน้า
2. Extract ทุกหัวข้อในเนื้อหา + เลขหน้าจริง
3. Cross-check
4. Report mismatch
```

---

## 6. Layer 3 — Source-trace Verification

### 6.1 NotebookLM MCP Workflow

ทุก citation ที่ใช้ในเล่ม → ต้องมี **Search ID** ใน `state/notebooklm-corpus.md`

**Verify Workflow:**
```
For each citation in dissertation:
  1. หา Search ID ใน corpus.md
  2. ถ้าไม่มี → MARK as "Pending Source-trace"
  3. ถ้ามี → MCP `source_get_content` เพื่อ Verify quote
  4. เปรียบเทียบ quote ในเล่ม vs source ต้นทาง
  5. ถ้าตรง → ✅ Verified
  6. ถ้าไม่ตรง → ❌ Issue + paraphrase แทน
```

### 6.2 MCP Tool Usage

**Bulk Verify:**
```
notebook_query(
  query="all sources used in chapter 2",
  filter={tags:["mcu-thesis", "external-thesis"]}
)
```

**Specific Quote Verify:**
```
source_get_content(
  source_id="spencer-1993",
  section="page 21"
)
```

### 6.3 Manual Verify (สำหรับ Source ไม่อยู่ใน Corpus)

```
1. ผู้ใช้เปิด original source (book/journal)
2. ตรวจ quote + page number
3. Mark verified ใน corpus.md (Manual entry)
4. หรือ paraphrase + new citation
```

---

## 7. Numbers / Statistics Audit

### 7.1 Audit Scope

**Numbers ที่ต้องตรวจ:**
- จำนวนผู้ให้ข้อมูล (ตรงกับที่ระบุในบทที่ 3?)
- ตัวเลขในตารางความถี่ (ผลรวม = N ทั้งหมด?)
- ค่าเฉลี่ย / SD / IOC / Cronbach (จากการคำนวณจริง?)
- ร้อยละ (sum = 100%?)
- จำนวนผู้เชี่ยวชาญ (= 5? ภายนอก ≥ 2?)

### 7.2 Internal Consistency Check

**Cross-check ตัวเลขข้ามจุด:**

| ตัวเลข | ที่ระบุใน | ต้องตรงกับใน |
|--------|----------|------------|
| ผู้ให้ข้อมูล Mixed Methods | 3.2.1 / 3.3.1 | 4.x ผลสัมภาษณ์ |
| Sample size | 3.2.1 + ตาราง | Response Rate ใน 3.2.3 |
| ผู้เชี่ยวชาญ | 3.2.2 | Appendix รายชื่อ |
| Try out | 3.2.2 | 30 ชุด + Cronbach |
| Sample IOC | 3.2.2 | Appendix ตาราง IOC |

### 7.3 Mathematical Audit

**ตรวจการคำนวณ:**
- Σ frequency = N total
- ร้อยละ sum = 100%
- ค่าเฉลี่ย correct?
- IOC = Σ score / N experts (ถูกต้อง?)
- Cronbach's Alpha (≥ 0.70 ผ่าน)

---

## 8. Dates Audit

### 8.1 Date Consistency

**ตรวจวันที่:**
- วันที่สัมภาษณ์ = วันที่ใน Appendix
- ปีที่ทำวิจัยใน 1.4.4 = ตรงกับ data collection actual
- ปี พ.ศ. ในบรรณานุกรม = ตรงกับ original publication year

### 8.2 Anachronism Check

✗ อ้างทฤษฎีที่ตีพิมพ์หลังจากวันสำเร็จดุษฎีนิพนธ์
✗ อ้างเหตุการณ์ในอนาคต
✗ ปี พ.ศ. ที่ผิดยุค

---

## 9. Quotes Audit (Verbatim Check)

### 9.1 กฎเหล็ก

**ทุก Quote ต้อง verbatim** — ตัวอักษรต้องตรงกับ source ต้นทาง

**Process:**
```
1. Extract ทุก quoted text (ใน "...")
2. หา source ผ่าน MCP `source_get_content`
3. เปรียบเทียบทีละตัวอักษร
4. ถ้าผิด → แก้ไข paraphrase แทน หรือใช้ exact quote
```

### 9.2 Quote Modification Rules

✓ **Allowed:**
- Use [...] for omission
- Use [insertion] for clarification (in brackets)
- Translation with note "(ผู้วิจัยแปล)"

✗ **Forbidden:**
- เปลี่ยนคำใน quote
- เพิ่ม/ลบโดยไม่มี [ ]
- รวม quote ที่ไม่ติดกันโดยไม่ระบุ

---

## 10. Names Audit

### 10.1 Name Consistency

**ตรวจชื่อบุคคล:**
- Author name spelled correctly + consistent throughout
- Thai name with title (ดร., รศ., พระ-) consistent
- English name (Last, First) format consistent

### 10.2 Stakeholder Names

**ผู้ให้ข้อมูล:**
- รหัสผู้ให้ข้อมูลใช้สม่ำเสมอ (เช่น KI-01, KI-02)
- Anonymization PII ครบ
- รายชื่อใน Appendix ตรงกับใน main text

### 10.3 Institutional Names

**ชื่อหน่วยงาน:**
- "มหาวิทยาลัยมหาจุฬาลงกรณราชวิทยาลัย" (ตัวเต็ม)
- "มจร" (อักษรย่อ — ใช้หลังจากระบุตัวเต็มแล้ว)
- ชื่อมหาวิทยาลัยอื่นในบรรณานุกรม — ตรง

---

## 11. Cross-Chapter Variable Consistency Audit

> Cross-reference ไปไฟล์ `06-writing-standard.md` §6 — ใช้ Variable Consistency Chain

### 11.1 Audit ตัวแปรทุกตัวใน 6 จุด

| Variable | บท 1 ขอบเขต | บท 1 นิยาม | บท 2 ทบทวน | บท 2 กรอบ | บท 3 เครื่องมือ | บท 4 ผล | บท 5 อภิปราย |
|---------|-----------|-----------|-----------|-----------|---------------|---------|--------------|
| IV1 | ? | ? | ? | ? | ? | ? | ? |
| IV2 | ? | ? | ? | ? | ? | ? | ? |
| DV | ? | ? | ? | ? | ? | ? | ? |

**Pass Criterion:** ทุก ✓ ในทุกแถว

---

## 12. Common Mistakes Library (10 Checkpoints)

**[CP-94] Citation มีในเชิงอรรถ ไม่มีในบรรณานุกรม** [CRITICAL]
- ✗ อ้าง "Smith (1993)" ในเชิงอรรถ แต่ไม่มีในบรรณานุกรม
- ✓ Cross-check ทุก citation
- *Source: Layer 2 + Cross-H6*

**[CP-95] บรรณานุกรมมี ไม่ใช้ใน text** [Medium]
- ✗ บรรณานุกรมมี 50 รายการ แต่อ้างจริง 35
- ✓ ลบรายการที่ไม่ใช้ออก
- *Source: Layer 2*

**[CP-96] Quote ไม่ verbatim** [CRITICAL]
- ✗ Quote ในเล่ม ≠ Source ต้นทาง
- ✓ ตรงตัวอักษร 100%
- *Source: §9*

**[CP-97] เลขพระไตรปิฎกไม่ถูก** [CRITICAL]
- ✗ "ที.ม. (ไทย) ๑๕/๙๙๙/๙๙๙๙" (เกินช่วงจริง)
- ✓ Verify กับ 84000.org / มจร
- *Source: H5 + คู่มือ มจร*

**[CP-98] อ้าง ป.โท ในระดับ ป.เอก** [CRITICAL]
- ✗ อ้างวิทยานิพนธ์ ป.โท ในบทที่ 2 หรือ 5
- ✓ เฉพาะ ป.เอก หรือบทความวิจัย
- *Source: คู่มือ มจร P2 + P5*

**[CP-99] ผลบทที่ 4 อ้างหนังสือ** [CRITICAL]
- ✗ พบเชิงอรรถหนังสือใน 4.x
- ✓ ผลทั้งหมดจากสัมภาษณ์/แบบสอบถามจริงเท่านั้น
- *Source: คู่มือ มจร P4*

**[CP-100] ตัวเลขใน Chapter 4 ไม่ตรง raw data** [CRITICAL]
- ✗ ตารางบอก N=120 แต่ Demographic บอก N=115
- ✓ Internal consistency check
- *Source: §7.2*

**[CP-101] ผู้เชี่ยวชาญ < 5 หรือไม่มีภายนอก ≥ 2** [CRITICAL]
- ✗ Appendix รายชื่อ 4 คน
- ✓ 5 รูป/คน + ภายนอก ≥ 2
- *Source: §7.2 + คู่มือ มจร*

**[CP-102] Hallucinated Author** [CRITICAL]
- ✗ "Smith (2023)" ไม่มีในใดเลย
- ✓ ทุก author ตรวจ NotebookLM + Google Scholar
- *Source: H1 + Layer 1*

**[CP-103] Variable Consistency Chain ขาด** [CRITICAL]
- ✗ บท 1 ใช้ "สมรรถนะ 5 ด้าน" / บท 2 ใช้ "4 ด้าน"
- ✓ ตรงทุก 6 จุด (บท 1 ขอบเขต → นิยาม → บท 2 ทบทวน → กรอบ → บท 3 เครื่องมือ → บท 4 ผล → บท 5 อภิปราย)
- *Source: §11 + Cross-H1, H2, H3*

---

## 13. Pre-Submission Audit Checklist

### Layer 1 — Hallucination

✅ ทุก author ตรวจมีจริง (NotebookLM/Google Scholar)
✅ ทุกปี publication ตรวจตรงกับ historical context
✅ ทุกเลขพระไตรปิฎกอยู่ในช่วงจริง (มจร/84000)
✅ ทุก journal มี ISSN จริง
✅ ทุกวิทยานิพนธ์มีใน TDC/คลัง มจร

### Layer 2 — Cross-reference

✅ ทุก citation ในเชิงอรรถ → มีในบรรณานุกรม
✅ บรรณานุกรม → ใช้ใน text ทุกรายการ
✅ คำย่อพระไตรปิฎก → มีในคำอธิบายสัญลักษณ์
✅ TOC ↔ Content ตรง 100%

### Layer 3 — Source-trace

✅ ทุก citation มี Search ID ใน corpus.md
✅ ทุก Quote verbatim ตรงกับ source
✅ Citation ที่ใช้ Manual paste — มี V### entry

### Numbers + Dates + Names

✅ ผู้ให้ข้อมูล Mixed ≥ 17 / Qual ≥ 25
✅ Sample size + Response Rate consistent
✅ ผู้เชี่ยวชาญ 5 + ภายนอก ≥ 2
✅ Try out 30 ชุด + Cronbach ≥ 0.70
✅ ตัวเลขในตาราง = sum to N total
✅ ร้อยละ sum = 100%
✅ ปีที่ทำวิจัย ตรงทุกจุด
✅ ชื่อสะกดถูก + ใช้สม่ำเสมอ

### Cross-Chapter Variable Consistency

✅ Variable Consistency Chain ✓ ทุก 6 จุด
✅ ทุกตัวแปรในกรอบ มาจาก 2.x
✅ Section Numbering กรอบ (2.6 หรือ 2.7) ถูก

### MCU-specific Critical Rules

✅ ระดับ ป.เอก เท่านั้นในบทที่ 2 + 5
✅ ผลบทที่ 4 จากสัมภาษณ์/แบบสอบถามจริงเท่านั้น
✅ มจร อ้างอิง ≥ 60% ในบทที่ 2
✅ Buddhist integration ไม่เป็นเปลือก

**รวม: 27 audit items** — ผ่าน 100% = Fact Audit Pass

---

## 14. Routing Map

| สถานการณ์ | Load Reference ถัดไป |
|-----------|---------------------|
| Verify ผ่าน NotebookLM MCP | `01-notebooklm-protocol.md` |
| Citation/Footnote format | `11-citation-footnote.md` |
| Format Audit | `08-template-audit.md` |
| AI Detection | `10-ai-detection.md` |
| Voice Profile | `07-academic-thai-voice.md` |
| Cross-chapter consistency | `06-writing-standard.md` §6 |
| Theory-Dhamma verify | `04-pa-dhamma-mapping.md` |

---

## 15. Versioning

**Version:** V01R01
**Date:** 2026-05-03
**Source:**
- คู่มือ มจร — กฎ "ห้ามดึงผลจากหนังสือ" + "ระดับ ป.เอก เท่านั้น"
- NotebookLM MCP Workflow (`01-notebooklm-protocol.md`)
- Variable Consistency Chain (`06-writing-standard.md`)
- 7 Hallucination Signatures (H1-H7)
- 3-Layer Detection Architecture
- Common Mistakes 10 ข้อ (CP-94 ถึง CP-103)
**Update Rule:** Minor edit → V01R02; Major rewrite → V02R01
