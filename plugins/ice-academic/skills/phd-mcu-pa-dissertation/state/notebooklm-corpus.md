# NotebookLM Corpus
## ดุษฎีนิพนธ์ ปร.ด. รปศ. มจร — [Researcher Name]

**Last Updated:** 2026-05-03
**Notebook:** phd-mcu-pa-dissertation-corpus
**Total Searches:** 0
**Total Sources Cited:** 0

> **Schema Version:** V01R01
> **Reference:** `01-notebooklm-protocol.md` §6 — Corpus Format Specification
> **Purpose:** Cross-session record ของทุก MCP query + Manual paste ที่ใช้ในเล่ม

---

## Index by Chapter Section

| Chapter Section | Search IDs | Verify IDs |
|-----------------|------------|------------|
| 1.1 ความเป็นมา | — | — |
| 2.1 หลักธรรม | — | — |
| 2.3 IV1 | — | — |
| 2.4 IV2 | — | — |
| 2.5 DV | — | — |
| 2.6 งานวิจัย | — | — |
| 2.6/2.7 กรอบแนวคิด | — | — |
| 5.2 อภิปราย | — | — |

---

## Search Entries (UC-2 Extract Specific Points)

> Pattern แต่ละ entry — Skill จะ append entry ใหม่ตามนี้

### S001 — [YYYY-MM-DD HH:mm] — "[Query Topic]"

**Type:** UC-2 Extract Specific Points
**MCP Call:**
```
notebook_query(
  notebook_id="phd-mcu-pa-dissertation-corpus",
  query="[query string]",
  filter={tags:["mcu-thesis","external-thesis"]}
)
```
**Sources Returned:** 0 / 0 ที่ใช้ในเล่ม
**Linked Section:** [บท X.Y]
**Status:** ⏳ Pending

#### Result 1
**Source ID (in notebook):** [src_id]
**Citation (มาตรฐาน มจร):** [Citation in MCU footnote format]
**Quote (ภาษาต้นฉบับ):**
> [Exact quote]
**คำแปล/สรุปโดย Claude:**
[Synthesized summary by Claude]
**Use Plan:**
- [บท X.Y — purpose]
**Cited in Footnote:** [เชิงอรรถที่ N บทที่ M] — กรอกหลังเขียน

---

## Verify Citation Log (UC-3)

### V001 — [YYYY-MM-DD HH:mm]

**Context:** [What Claude was about to write]
**MCP Call:**
```
source_get_content(
  source_id="[src_id]",
  section="[page or section]"
)
```
**Quote ที่ดึงมา:**
> [Exact quote from source]
**ผลการเปรียบเทียบ:**
- ✅ ตรง — เขียนต่อได้
- 🟡 ไม่ตรงเล็กน้อย — ปรับ paraphrase
- ❌ ไม่ตรง — ต้องเขียนใหม่
**Action Taken:**
[What Claude did after verification]

---

## Manual Path Entries

### M001 — [YYYY-MM-DD HH:mm] — [Manual]

**Method:** Manual paste from NotebookLM Web
**Original Query:** "[query]"
**User-pasted Output:**
> [exact paste]
**Status:** ⏳ Pending Verify
**Note:** Manual entry — ผู้ใช้รับรองความถูกต้องของ paste

---

## Statistics

| Metric | Value |
|--------|-------|
| Total Searches (S###) | 0 |
| Total Verifications (V###) | 0 |
| Total Manual Entries (M###) | 0 |
| Verified Status | 0 |
| Pending Status | 0 |
| Sources by Tag |  |
| - mcu-thesis | 0 |
| - external-thesis | 0 |
| - journal-article | 0 |
| - target-org | 0 |
| - tipitaka-mcu | 0 |
| - payutto | 0 |
| - pa-theory | 0 |
| **MCU Citation %** | 0% |
| **Target MCU Citation %** | ≥ 60% |

---

## Usage Instructions

1. **Skill อ่านไฟล์นี้** เมื่อ
   - ก่อนเขียน chapter (ใช้ Source ที่มี)
   - ก่อน Fact Audit (cross-check citation)
   - ก่อน AI Detection (ตรวจ source-trace)

2. **Skill เขียน entry ใหม่** เมื่อ
   - หลัง MCP `notebook_query` สำเร็จ
   - หลัง MCP `source_get_content` Verify
   - หลัง User paste Manual

3. **Skill อัปเดต Status** เมื่อ
   - Citation ถูกใช้ใน text แล้ว → Verified
   - Citation ผ่าน Verify → Verified
   - Citation อ้างซ้ำ → Cited in Footnote (เพิ่มเลข)

---

**Schema Version:** V01R01
**Last Updated:** 2026-05-03
