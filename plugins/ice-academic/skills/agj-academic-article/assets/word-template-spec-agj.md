# Word Template Specification — บทความวิชาการ วารสาร AGJ

ข้อกำหนดสำหรับการสร้างไฟล์ .docx ตามรูปแบบวารสารบัณฑิตศึกษาวิชาการ
สกัดจาก: บทความวิชาการ 2569.docx (template ต้นฉบับ)

---

## Page Setup

```python
from docx.shared import Inches, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

section = document.sections[0]
section.page_width = Cm(21.0)       # A4
section.page_height = Cm(29.7)      # A4
section.top_margin = Inches(1.0)    # 1 นิ้ว
section.bottom_margin = Inches(1.0) # 1 นิ้ว
section.left_margin = Inches(1.0)   # 1 นิ้ว
section.right_margin = Inches(1.0)  # 1 นิ้ว
```

---

## Font & Paragraph Styles

| Style Name | Font | Size | Bold | Alignment | Indent |
|---|---|---|---|---|---|
| ArticleType | TH SarabunPSK | 12pt | No | Center | — |
| TitleTH | TH SarabunPSK | 20pt | Yes | Center | — |
| TitleEN | TH SarabunPSK | 18pt | Yes (CAPS) | Center | — |
| Author | TH SarabunPSK | 14pt | No | Center | — |
| HeadingMain | TH SarabunPSK | 18pt | Yes | Left | — |
| Body | TH SarabunPSK | 16pt | No | Justify | First line ~1.25cm (5 chars) |
| Keyword | TH SarabunPSK | 16pt | No | Left | — |
| Reference | TH SarabunPSK | 16pt | No | Left | Hanging 1.27cm |
| FigureCaption | TH SarabunPSK | 16pt | No | Center | — |
| TableCaption | TH SarabunPSK | 16pt | No | Left | — |

---

## Line Spacing

- ทั้งเอกสาร: **Single (1.0)**
- Space Before: 0pt
- Space After: 0pt

---

## Page Numbers

- **ไม่ใส่เลขหน้า**

---

## Document Structure (ลำดับการพิมพ์)

```
1.  "บทความวิชาการ" (12pt, กลาง)
2.  [บรรทัดว่าง]
3.  ชื่อเรื่องไทย (20pt, หนา, กลาง)
4.  ชื่อเรื่องอังกฤษ (18pt, หนา, CAPS, กลาง)
5.  ชื่อผู้เขียนหลัก (ไทย)¹*, ชื่อผู้เขียนร่วม (ไทย)² (14pt, กลาง)
6.  ชื่อผู้เขียนหลัก (อังกฤษ)¹*, ชื่อผู้เขียนร่วม (อังกฤษ)² (14pt, กลาง)
7.  ¹สังกัดผู้เขียนหลัก (ไทย) (14pt, กลาง)
8.  ¹สังกัดผู้เขียนหลัก (อังกฤษ) (14pt, กลาง)
9.  ²สังกัดผู้เขียนร่วม (ไทย) (14pt, กลาง)
10. ²สังกัดผู้เขียนร่วม (อังกฤษ) (14pt, กลาง)
11. *Corresponding Author E-mail: xxx@xxx (14pt, กลาง)
12. Received…; Revised…; Accepted…
13. [บรรทัดว่าง]
14. "บทคัดย่อ" (18pt, หนา)
15. เนื้อบทคัดย่อ (16pt, justify, ย่อหน้า)
16. [บรรทัดว่าง]
17. "คำสำคัญ:" คำ1, คำ2, คำ3 (16pt)
18. [บรรทัดว่าง]
19. "Abstract" (18pt, หนา)
20. เนื้อ Abstract (16pt, justify, ย่อหน้า)
21. "Keywords:" word1, word2, word3 (16pt)
22. "บทนำ" (18pt, หนา)
23. เนื้อบทนำ (16pt, justify, ย่อหน้า)
24. [บรรทัดว่าง]
25. "เนื้อหา" หรือหัวข้อเนื้อหา (18pt, หนา)
26. เนื้อหา (16pt, justify, ย่อหน้า)
    - หัวข้อย่อย (16pt, หนา)
    - ภาพ: "ภาพที่ X ชื่อภาพ" (16pt, กลาง) + "ที่มา:" (16pt)
    - ตาราง: "ตารางที่ X ชื่อตาราง" (16pt) + คำอธิบาย
27. "องค์ความรู้ใหม่" (18pt, หนา)
28. เนื้อองค์ความรู้ + โมเดล/แผนภาพ (16pt)
29. "สรุป" (18pt, หนา)
30. เนื้อสรุป (16pt, justify, ย่อหน้า)
31. "เอกสารอ้างอิง" (18pt, หนา)
32. รายการอ้างอิง (16pt, hanging indent)
```

---

## ภาพ

```
[ภาพ - จัดกลาง]

ภาพที่ 1 ชื่อภาพ (16pt, กลาง)
ที่มา: ระบุแหล่งที่มา (ถ้ามี) (16pt)

คำอธิบายภาพ (ถ้ามี) (16pt)
```

## ตาราง

```
ตารางที่ 1 ชื่อตาราง (16pt)
[ตาราง]
คำอธิบายตาราง (16pt)
```
- ตารางข้ามหน้า: `ตารางที่ 1 ชื่อตาราง (ต่อ) (16pt)`

---

## python-docx Quick Reference

```python
from docx import Document
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# Page setup
section = doc.sections[0]
section.top_margin = Inches(1.0)
section.bottom_margin = Inches(1.0)
section.left_margin = Inches(1.0)
section.right_margin = Inches(1.0)

# Helper function
def add_paragraph(doc, text, size=16, bold=False, align='justify', indent_first=False):
    p = doc.add_paragraph()
    run = p.add_run(text)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(size)
    run.bold = bold
    if align == 'center':
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    elif align == 'justify':
        p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    elif align == 'left':
        p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    if indent_first:
        p.paragraph_format.first_line_indent = Cm(1.25)
    # Single spacing
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(0)
    return p

# Article type label
add_paragraph(doc, 'บทความวิชาการ', size=12, align='center')

# Title
add_paragraph(doc, 'ชื่อเรื่องภาษาไทย', size=20, bold=True, align='center')
add_paragraph(doc, 'TITLE IN ENGLISH', size=18, bold=True, align='center')

# ... continue for each section
```

---

## สำคัญ: ใช้ SKILL docx ด้วย

เมื่อต้องสร้างไฟล์ .docx จริง ให้อ่าน `/mnt/skills/public/docx/SKILL.md` ร่วมด้วยสำหรับ best practices การสร้างเอกสาร Word
