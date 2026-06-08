# Template Placement Matrix
## ตำแหน่งจัดเก็บ Template ทั้ง 12 ไฟล์ใน Skill Reference Structure

**Status:** Internal staging — Mapping ของไฟล์ Template ผู้ใช้แนบ → MD ที่จะอ้างอิง
**Last Updated:** 2026-05-03

---

## Authority Hierarchy (ตามหลักการของผู้ใช้)

```
LEVEL 1 (Authoritative Source) — มีอำนาจสูงสุด
  คู่มือการเขียนดุษฎีนิพนธ์ฯ มจร 2563 (ISBN 978-616-300-672-1)
              ↓
LEVEL 2 (Structural Frame) — โครงร่างที่ใช้กรอกได้
  Template Files 12 ไฟล์ที่ผู้ใช้แนบ (07-11 + ส่วนนำ)
              ↓
LEVEL 3 (Practical Detail) — รายละเอียดเชิงปฏิบัติ
  Note อาจารย์ที่ปรึกษา (Excel + docx)
              ↓
LEVEL 4 (Worked Example) — ตัวอย่างเสร็จแล้ว
  วิจัยบทที่ 1-5.pdf + ตัวอย่างของผู้ใช้
```

**กฎเหล็ก:** ถ้าระดับใดขัดกัน → ใช้ระดับสูงกว่า (Level 1 > 2 > 3 > 4)

---

## Template Placement Matrix

| # | Template File | ประเภท | วางใน MD หลัก | วางใน MD รอง |
|---|---------------|--------|--------------|--------------|
| 1 | `01 หน้าปก.docx` | Front Matter | `08-template-audit.md` (Cover Page Spec) | — |
| 2 | `05 สารบัญ.docx` | Front Matter | `08-template-audit.md` (TOC Spec) | — |
| 3 | `06 คำอธิบายสัญลักษณ์และคำย่อ.docx` | Front Matter | `08-template-audit.md` (Symbols Spec) | `11-citation-footnote.md` (พระไตรปิฎก abbrev) |
| 4 | `07 Template บทที่ 1.docx` | Chapter Template | `06-writing-standard.md` (Ch1 structure) | `templates/chapter-1.md` (จะสร้างขั้นที่ 13) |
| 5 | `08 Template บทที่ 2.docx` | Chapter Template | `06-writing-standard.md` (Ch2 structure) | `templates/chapter-2.md` (จะสร้างขั้นที่ 14) |
| 6 | `09 Template บทที่ 3.docx` | Chapter Template | `05-methodology-design.md` (Ch3 structure) ⭐ | `06-writing-standard.md` + `templates/chapter-3.md` (จะสร้างขั้นที่ 15) |
| 7 | `8. ภาคผนวก.docx` | Back Matter | `08-template-audit.md` (Appendix Spec) | — |
| 8 | `10 บรรณานุกรม.docx` | Back Matter | `11-citation-footnote.md` (Bibliography format) ⭐ | `08-template-audit.md` |
| 9 | `11 ตัวอย่าง แบบสอบถามเพื่อการวิจัยและแบบสัมภาษณ์.docx` | Instrument Example | `05-methodology-design.md` (Questionnaire + Interview Form) ⭐ | — |
| 10 | `11 แบบสอบถามเครื่องมือ IOC.docx` | Instrument Validation | `05-methodology-design.md` (IOC Tool) ⭐ | — |
| 11 | `11 ประวัติผู้วิจัย.docx` | Back Matter | `08-template-audit.md` (Bio Spec) | — |
| 12 | `วิจัยบทที่ 1-5.pdf` | Worked Example | All chapter MDs (cross-reference) | — |

⭐ = ใช้ในขั้นที่จะสร้างถัดไป (`05-methodology-design.md`)

---

## Templates ที่จะใช้ในแต่ละ MD ที่เหลือ

### `05-methodology-design.md` (ขั้นถัดไป — กำลังจะร่าง)
- ⭐ `09 Template บทที่ 3.docx` (Ch3 Methodology Structure)
- ⭐ `11 ตัวอย่าง แบบสอบถามเพื่อการวิจัยและแบบสัมภาษณ์.docx` (Instrument Example)
- ⭐ `11 แบบสอบถามเครื่องมือ IOC.docx` (IOC Tool)
- `การสร้างเครื่องมือการวิจัย.pdf` (Tool Design Knowledge)

### `06-writing-standard.md` (ขั้นที่ 8)
- `07 Template บทที่ 1.docx` (Ch1 structure)
- `08 Template บทที่ 2.docx` (Ch2 structure)
- `09 Template บทที่ 3.docx` (Ch3 structure — secondary)
- `วิจัยบทที่ 1-5.pdf` (Worked Example)

### `08-template-audit.md` (ขั้นที่ 10)
- `01 หน้าปก.docx` (Cover spec)
- `05 สารบัญ.docx` (TOC spec)
- `06 คำอธิบายสัญลักษณ์และคำย่อ.docx` (Symbols spec)
- `8. ภาคผนวก.docx` (Appendix spec)
- `11 ประวัติผู้วิจัย.docx` (Bio spec)

### `11-citation-footnote.md` (ขั้นที่ 13)
- `10 บรรณานุกรม.docx` (Bibliography format)
- `06 คำอธิบายสัญลักษณ์และคำย่อ.docx` (พระไตรปิฎก abbrev — secondary)

### `templates/chapter-1.md` ถึง `chapter-3.md` (ขั้นที่ 15-17)
- `07 Template บทที่ 1.docx` → `chapter-1.md`
- `08 Template บทที่ 2.docx` → `chapter-2.md`
- `09 Template บทที่ 3.docx` → `chapter-3.md`

(Chapter 4-5 templates ยังไม่ได้แนบ — Skill จะใช้คู่มือ มจร เป็น Default)

---

## Usage Instructions for Future MDs

เมื่อสร้าง MD แต่ละไฟล์
1. **เปิด Authority Hierarchy** — ตรวจคู่มือ มจร ก่อน
2. **เปิด Template ที่เกี่ยวข้อง** — ดูโครงสร้าง field/section
3. **เทียบ Note อาจารย์** — ปรับรายละเอียดตาม practical
4. **อ้างอิง Worked Example** — ใช้เป็น illustration

ถ้า Template บอกอย่างหนึ่ง แต่คู่มือบอกอีกอย่าง → **ตามคู่มือ** + เพิ่ม Note ใน MD ว่ามี discrepancy

---

**END OF PLACEMENT MATRIX**
