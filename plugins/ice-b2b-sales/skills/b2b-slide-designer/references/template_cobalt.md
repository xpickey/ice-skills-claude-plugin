# Cobalt Template — Designer Brief (iCE-CI Integrated)

> **Version:** V01R01 | **Date:** 2026-04-28
> **Concept:** "น้ำเงิน iCE เข้มข้น สง่างาม" — Bold Corporate, Authoritative, Trustworthy

---

## 1. Theme Concept

Cobalt ออกแบบมาเพื่อสื่อสาร "ความเป็นมืออาชีพระดับองค์กร ความน่าเชื่อถือ และความเชี่ยวชาญ"
เหมาะอย่างยิ่งสำหรับ Executive Briefing, Board Meeting, Annual Report, Financial Review,
Earnings Call, Investor Update, และเอกสารทางการระดับ C-Suite โดยใช้ iCE Main Blue เข้ม
เป็นพื้นหลังหลักหรือเป็นแถบเด่น ตัดด้วยสีขาวเพื่อสร้างความสง่างามและภูมิฐาน

อารมณ์ของ Template: หนักแน่น น่าเชื่อถือ ภูมิฐาน เป็นทางการ มั่นคง ผู้นำองค์กร

---

## 2. Color System

### 2.1 Primary Palette

| Role | Hex | Sample Use |
| :--- | :--- | :--- |
| Background Primary | `#1E66A4` (iCE Main Blue) | พื้นหลัง Hero Section |
| Background Light | `#FFFFFF` (Pure White) | พื้นหลังหน้าเนื้อหา |
| Background Slate | `#F4F6F8` (Cool Gray Light) | พื้นรอง |
| Accent | `#41A8B5` (iCE Secondary Blue) | Highlight, Link, Pop Color |
| Text on Dark | `#FFFFFF` | Body Text บนพื้นน้ำเงิน |
| Text on Light | `#1A1A1A` (Near Black) | Body Text บนพื้นขาว |
| Text Secondary | `#6B7280` (Slate Gray) | Caption, Footer |

### 2.2 Tints & Shades

| Token | Hex |
| :--- | :--- |
| iCE Blue 95 | `#194F7A` |
| iCE Blue 80 | `#2B7AC0` |
| iCE Blue 30 | `#A8C7E0` |
| iCE Blue 10 | `#E5EEF5` |
| Gold Accent | `#C9A961` (Optional Pop) |

### 2.3 Semantic Colors

| สถานะ | Hex |
| :--- | :--- |
| Success | `#16A34A` |
| Warning | `#D97706` |
| Error | `#DC2626` |
| Info | `#41A8B5` |

---

## 3. Typography Hierarchy

### 3.1 Font Stack
| Language | Primary | Secondary |
| :--- | :--- | :--- |
| Thai | Kanit | Sarabun |
| English | Raleway | Open Sans |

### 3.2 Type Scale (PPTX 16:9)
| Role | Weight | Size |
| :--- | :--- | :--- |
| Display | ExtraBold 800 | 60 pt |
| H1 | Bold 700 | 36 pt |
| H2 | SemiBold 600 | 26 pt |
| H3 | Medium 500 | 20 pt |
| Body | Regular 400 | 18 pt |
| Caption | Regular 400 | 14 pt |
| Quote | Regular 400 Italic | 24 pt |

### 3.3 Type Scale (Word A4)
| Role | Size |
| :--- | :--- |
| Cover Title | 32 pt |
| Heading 1 | 18 pt |
| Heading 2 | 14 pt |
| Body | 11 pt |
| Caption | 9 pt |

---

## 4. Grid System

### 4.1 PPTX 16:9
- Margin: 48 px
- Column: 12
- Gutter: 24 px
- Header Height: 80 px (มี Logo + Page Indicator)
- Footer Height: 32 px (สี Cool Gray + Confidentiality Note)

### 4.2 Word A4 Portrait
- Margin: 2.5 cm
- Column: 1
- Header: 1.5 cm (Logo + ชื่อเอกสาร)
- Footer: 1.5 cm (Page Number + Document Code)

---

## 5. Spacing / Padding Scale

| Token | Value |
| :--- | :--- |
| xxs | 4 px |
| xs | 8 px |
| sm | 16 px |
| md | 24 px |
| lg | 32 px |
| xl | 48 px |
| 2xl | 72 px |

---

## 6. Image Treatment

- โทนภาพ: Neutral หรือ Cool ตัดด้วย Layer สีน้ำเงิน iCE Opacity 30%
- รูปทรง: สี่เหลี่ยมขอบมน 4 px (ขอบเฉียบ ภูมิฐาน)
- Style: Corporate Photography, Boardroom, Cityscape
- Treatment: Duotone (ดำ-น้ำเงิน) สำหรับ Hero Image

---

## 7. Iconography Style

- สไตล์: Solid Filled (หนักแน่น) หรือ Outline เส้น 2 px
- ขนาด: 24 / 32 / 48 px
- สีหลัก: ขาว (บนพื้นน้ำเงิน) / iCE Blue (บนพื้นขาว)
- Recommend: Material Icons Filled

---

## 8. Animation & Transition

- Slide Transition: Fade Through Black 0.5s (เป็นทางการ)
- Object Animation: Fade-In 0.3s
- หลีกเลี่ยง: Bounce, Spin, Zoom-In ขนาดใหญ่
- Timing: ช้าและสง่างาม (Ease-In-Out)

---

## 9. Accessibility Notes

| ประเด็น | มาตรฐาน |
| :--- | :--- |
| Contrast Ratio | ขาวบน iCE Main Blue = 7.2:1 (AAA) |
| Body Font Size | ≥ 18 pt (PPTX), ≥ 11 pt (Word) |
| Print Test | ผ่าน Print Preview ขาว-ดำ ไม่สูญเสียความหมาย |

---

## 10. 15 Layout Patterns

### Layout 01 — Title / Cover
- **Header:** ไม่มี
- **Background:** iCE Main Blue เต็มหน้า
- **Text:** Headline 60 pt ExtraBold สีขาว ซ้ายล่าง
- **Subtitle:** 24 pt Regular สี iCE Secondary Blue
- **Logo:** ขวาบน สีขาว 100 px
- **Footer Bar:** เส้น Gold Accent 4 px ใต้ Headline

### Layout 02 — Section Divider
- **Background:** iCE Blue 95 (เข้มกว่า Main)
- **Text:** "PART 01" 14 pt Letter-Spacing 4px สี iCE Secondary
- **Section Title:** Display 60 pt สีขาว
- **Accent:** เส้นแนวนอนยาว Gold Accent 80 px

### Layout 03 — Two-Column Text
- **Header:** Title Bar 80 px พื้น iCE Main Blue ตัวขาว
- **Body:** สองคอลัมน์ พื้นขาว Text Near Black
- **Divider:** เส้นแนวตั้งสี Cool Gray Light

### Layout 04 — Text Left + Image Right
- **Header:** Title Bar iCE Main Blue
- **Image:** ขวา 50% Duotone ดำ-น้ำเงิน
- **Text:** ซ้าย 50%, Body 18 pt
- **Pull Quote:** ก่อน Body วาง Quote 22 pt iCE Secondary

### Layout 05 — Image Left + Text Right
- **Image:** ซ้าย 60% เต็มความสูง
- **Text:** ขวา 40% พื้น Cool Gray Light Padding 32 px

### Layout 06 — Full-Bleed Image with Brand Bar
- **Image:** เต็มหน้า + Overlay iCE Blue Opacity 50% ฝั่งซ้าย
- **Brand Bar:** แถบแนวตั้งซ้าย 8 px สี Gold Accent
- **Text:** Headline สีขาวซ้ายบน

### Layout 07 — Three-Column Cards
- **Header:** Title Bar 80 px
- **Cards:** 3 การ์ด พื้นขาวขอบมน 4 px Border 1 px Cool Gray
- **Card Header:** แถบบน 4 px iCE Main Blue
- **Card Icon:** 40 px iCE Main Blue
- **Card Title:** H3 Bold

### Layout 08 — Quote / Testimonial
- **Background:** iCE Blue 95
- **Quote Mark:** Gold Accent 240 pt มุมซ้ายบน
- **Quote Body:** สีขาว 32 pt Italic
- **Attribution:** Avatar 80 px + ชื่อ Bold + ตำแหน่ง iCE Secondary

### Layout 09 — Big Number / Stat Highlight
- **Background:** ครึ่งบน iCE Main Blue / ครึ่งล่างขาว
- **Stat:** ตัวเลข 220 pt ExtraBold สีขาว วางคร่อมเส้นแบ่ง
- **Unit:** Gold Accent 48 pt
- **Body Below:** บนพื้นขาว 18 pt

### Layout 10 — Timeline / Roadmap
- **Timeline Bar:** 6 px iCE Main Blue
- **Milestone:** สี่เหลี่ยมจัตุรัส 24 px iCE Secondary หรือ Gold Accent
- **Labels:** H3 ทุก Milestone, Caption ปี

### Layout 11 — Comparison Table
- **Header Row:** iCE Main Blue + ตัวขาว Bold
- **Stripe:** สลับขาว/Cool Gray Light
- **Total Row:** สี Gold Accent
- **Highlight Column:** Border 3 px Gold Accent

### Layout 12 — Process Flow / Diagram
- **Step Box:** สี่เหลี่ยมขอบมน 4 px iCE Main Blue ตัวขาว
- **Connector:** ลูกศร Solid iCE Secondary
- **Step Number:** วงกลม 36 px Gold Accent ตัวดำ

### Layout 13 — Bullet List / Key Points
- **Bullet:** สี่เหลี่ยมเล็ก 8 px iCE Secondary
- **Indent:** 24 px
- **Highlight Word:** Bold + สี iCE Main Blue

### Layout 14 — Q&A / Discussion
- **Background:** Half iCE Main Blue / Half White
- **Headline:** "QUESTIONS" สีขาวฝั่ง Blue
- **Subhead:** "Discussion" iCE Main Blue ฝั่ง White
- **Logo:** กึ่งกลางเส้นแบ่ง

### Layout 15 — Closing / Thank You
- **Background:** iCE Main Blue เต็มหน้า
- **Headline:** "THANK YOU" 96 pt ExtraBold สีขาว
- **Contact Block:** ใต้ Headline พื้น Pure White ขนาด 50% สี iCE Main Blue
- **Logo:** ขวาบน สีขาว
- **Brand Bar:** Gold Accent ล่างสุด

---

## 11. Application Notes

### 11.1 PowerPoint
- ใช้ Theme "Office Theme" ปรับสีให้ตรง
- เปิดใช้ "Slide Master" กำหนด Header/Footer Block
- บันทึก `.potx` พร้อม Theme Color และ Theme Font

### 11.2 Word
- ตั้ง Heading 1 เป็น iCE Main Blue Bold
- ใช้ Style "Intense Quote" สำหรับ Pull Quote
- เปิด Heading Numbering สำหรับเอกสารทางการ

### 11.3 ห้ามทำ
- ห้ามใช้สีหวาน (Pastel) เป็นหลัก
- ห้ามใช้ฟอนต์ Script หรือ Handwritten
- ห้ามใช้รูป Cartoon

---

**End of Cobalt Designer Brief**
