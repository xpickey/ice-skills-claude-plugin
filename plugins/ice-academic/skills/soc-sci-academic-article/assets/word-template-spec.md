# Word Template Specification — บทความวิชาการ วารสาร มจร สังคมศาสตร์ปริทรรศน์

ข้อกำหนดสำหรับการสร้างไฟล์ .docx ตามรูปแบบวารสาร

---

## Page Setup

```python
# python-docx page setup
from docx.shared import Cm, Pt

section = document.sections[0]
section.page_width = Cm(21.0)       # A4
section.page_height = Cm(29.7)      # A4
section.top_margin = Cm(3.0)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3.5)
section.right_margin = Cm(2.5)
```

---

## Font & Paragraph Styles

| Style Name | Font | Size | Bold | Alignment | Space After | Indent |
|---|---|---|---|---|---|---|
| Title-TH | TH SarabunPSK | 18pt | Yes | Center | 6pt | — |
| Title-EN | TH SarabunPSK | 16pt | Yes | Center | 6pt | — |
| Author | TH SarabunPSK | 14pt | No | Center | 6pt | — |
| Heading | TH SarabunPSK | 16pt | Yes | Left | 6pt | — |
| Body | TH SarabunPSK | 16pt | No | Justify | 0pt | First line 1.25cm |
| Footnote | TH SarabunPSK | 14pt | No | Left | 0pt | — |
| Reference | TH SarabunPSK | 16pt | No | Left | 6pt | Hanging 1.27cm |
| Keyword | TH SarabunPSK | 16pt | No | Left | 6pt | — |

---

## Line Spacing

- ทั้งเอกสาร: **Single (1.0)**
- Space Before: 0pt
- Space After: 0pt (ยกเว้น Heading = 6pt)

---

## Page Numbers

- ตำแหน่ง: กลางล่าง (Center Bottom)
- เริ่มจากหน้าแรก
- Font: TH SarabunPSK 16pt

---

## Document Structure Order

```
1. ชื่อเรื่อง (ภาษาไทย)          → Title-TH style
2. ชื่อเรื่อง (ภาษาอังกฤษ)        → Title-EN style
3. ชื่อผู้เขียน + เชิงอรรถ*         → Author style
   * เชิงอรรถ: สังกัด + Email
4. [เว้น 1 บรรทัด]
5. "บทคัดย่อ"                     → Heading style
6. เนื้อหาบทคัดย่อไทย             → Body style (ไม่ indent)
7. "คำสำคัญ:" + คำ                → Keyword style
8. [เว้น 1 บรรทัด]
9. "Abstract"                      → Heading style
10. English abstract                → Body style (ไม่ indent)
11. "Keywords:" + words             → Keyword style
12. [เว้น 1 บรรทัด]
13. "บทนำ"                         → Heading style
14. เนื้อหาบทนำ                    → Body style
15. [หัวข้อแนวคิดและทฤษฎี]         → Heading style
16. เนื้อหาทฤษฎี                   → Body style
17. [หัวข้อเนื้อหาวิเคราะห์]        → Heading style
18. เนื้อหาวิเคราะห์               → Body style
    (แบ่ง sub-heading ได้)
19. "สรุป" / "บทสรุปและข้อเสนอแนะ" → Heading style
20. เนื้อหาสรุป                    → Body style
21. [เว้น 1 บรรทัด]
22. "เอกสารอ้างอิง"               → Heading style
23. รายการอ้างอิง                  → Reference style (Hanging indent)
```

---

## python-docx Code Snippet

```python
from docx import Document
from docx.shared import Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# --- Page Setup ---
section = doc.sections[0]
section.top_margin = Cm(3.0)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3.5)
section.right_margin = Cm(2.5)

def add_title_th(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(18)
    run.bold = True
    return p

def add_title_en(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(text)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(16)
    run.bold = True
    return p

def add_heading_custom(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    run = p.add_run(text)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(16)
    run.bold = True
    p.paragraph_format.space_after = Pt(6)
    return p

def add_body(doc, text, indent=True):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    if indent:
        p.paragraph_format.first_line_indent = Cm(1.25)
    run = p.add_run(text)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(16)
    p.paragraph_format.line_spacing = 1.0
    p.paragraph_format.space_after = Pt(0)
    return p

def add_reference(doc, text):
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.LEFT
    p.paragraph_format.left_indent = Cm(1.27)
    p.paragraph_format.first_line_indent = Cm(-1.27)
    run = p.add_run(text)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(16)
    p.paragraph_format.space_after = Pt(6)
    return p

# --- Page Numbers ---
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

def add_page_number(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    p = footer.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run()
    fld = OxmlElement('w:fldSimple')
    fld.set(qn('w:instr'), 'PAGE')
    run._element.append(fld)
    run.font.name = 'TH SarabunPSK'
    run.font.size = Pt(16)
```

---

## Blind Review Checklist

เมื่อสร้างไฟล์ .docx ต้องตรวจสอบ:

1. ไม่มีชื่อผู้เขียนในเนื้อหา (ยกเว้นหน้าแรกที่มีเชิงอรรถ — แยกไฟล์สำหรับ submission)
2. File Properties ลบข้อมูลผู้เขียน:
   ```python
   doc.core_properties.author = ''
   doc.core_properties.last_modified_by = ''
   ```
3. ไม่มี Track Changes / Comments ที่แสดงชื่อ
