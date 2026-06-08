# iCE-CI Template — Designer Brief (Official Corporate Identity)

> **Version:** V01R01 | **Date:** 2026-04-28
> **Concept:** "Standard iCE Corporate Identity" — Official, On-Brand, Default Choice
> **Source of Truth:** Corporate Identity Guideline — iCE Consulting Co., Ltd. (Dec 2021)

---

## 1. Theme Concept

iCE-CI คือ Template มาตรฐานที่สะท้อน Corporate Identity อย่างเป็นทางการของ
iCE Consulting Co., Ltd. โดยตรง ใช้สีและฟอนต์ตามคู่มือ CI ฉบับ Dec 2021 อย่างเคร่งครัด
เหมาะสำหรับงานที่ต้องการ "ความถูกต้องของแบรนด์" ทุกประเภท เช่น Proposal ทางการ,
RFP/TOR Response, Customer-facing Document, Public-facing Presentation, Press Release,
Annual Report, Brochure, Letter Head, และเอกสารทุกชนิดที่ต้องส่งให้ลูกค้าหรือผู้มี
ส่วนได้ส่วนเสียภายนอก

อารมณ์ของ Template: เป็นทางการ น่าเชื่อถือ ทันสมัย เป็นระเบียบ มืออาชีพ Trustworthy

> **Brand Promise:** "พันธมิตรทางเทคโนโลยี ที่ช่วยให้ลูกค้าองค์กรธุรกิจมีการจัดการระบบ
> การดำเนินธุรกิจอย่างมีประสิทธิภาพ และได้รับประโยชน์สูงสุดจากการนำเทคโนโลยีมาใช้"

---

## 2. Color System (ตามคู่มือ CI ฉบับทางการ)

### 2.1 Primary Palette (อ้างอิงจากคู่มือ)

| Role | Hex | ชื่อทางการ |
| :--- | :--- | :--- |
| Main Color | `#1E66A4` | น้ำเงิน iCE |
| Secondary Color | `#41A8B5` | ฟ้า iCE |
| Pure White | `#FFFFFF` | ขาว |
| Dark Gray (แทนสีดำ) | `#595959` | เทาเข้ม |

### 2.2 Suggested Background Gradient

| Direction | Stops |
| :--- | :--- |
| Diagonal (default) | `#1E66A4` → `#41A8B5` |
| Linear Horizontal | `#1E66A4` → `#41A8B5` |

### 2.3 Tints & Shades (ขยายเพิ่มเพื่อใช้งานจริง — ยังคงใน Brand Family)

| Token | Hex | การใช้งาน |
| :--- | :--- | :--- |
| iCE Blue 95 | `#194F7A` | Hover State, Heading เน้น |
| iCE Blue 80 | `#2B7AC0` | Body Heading รอง |
| iCE Blue 50 | `#7AA8CC` | Background Card |
| iCE Blue 30 | `#A8C7E0` | Border, Divider |
| iCE Blue 10 | `#E5EEF5` | Background Highlight อ่อน |
| iCE Cyan 50 | `#7BC9D2` | Tint รองสำหรับ Chart |
| iCE Cyan 10 | `#DAEEF1` | Background รอง |
| Cool Gray Light | `#F4F6F8` | Section Background |
| Mid Gray | `#9CA3AF` | Caption Secondary |

### 2.4 Semantic Colors (ใช้เฉพาะกรณีจำเป็น)

| สถานะ | Hex |
| :--- | :--- |
| Success | `#16A34A` |
| Warning | `#D97706` |
| Error | `#DC2626` |
| Info | `#41A8B5` (iCE Secondary) |

---

## 3. Typography Hierarchy (ตามคู่มือ CI)

### 3.1 Font Stack

| Language | Headline | Body A | Body B |
| :--- | :--- | :--- | :--- |
| English | Raleway ExtraBold | Raleway | Open Sans Light |
| Thai | Kanit Bold | Kanit Light | Sarabun Regular |

> **หมายเหตุ:** ตามคู่มือ Logo + ชื่อบริษัทใช้ Open Sans เป็นฟอนต์ประกอบ

### 3.2 Type Scale (PPTX 16:9)

| Role | Font | Weight | Size |
| :--- | :--- | :--- | :--- |
| Display | Kanit / Raleway | ExtraBold 800 | 60 pt |
| H1 | Kanit / Raleway | Bold 700 | 36 pt |
| H2 | Kanit / Raleway | SemiBold 600 | 28 pt |
| H3 | Kanit / Raleway | Medium 500 | 22 pt |
| Body | Sarabun / Open Sans | Regular 400 | 18 pt |
| Body Light | Kanit / Raleway | Light 300 | 18 pt |
| Caption | Sarabun / Open Sans Light | 300 | 14 pt |

### 3.3 Type Scale (Word A4)

| Role | Size |
| :--- | :--- |
| Cover Title | 32 pt Bold |
| Heading 1 | 18 pt Bold |
| Heading 2 | 14 pt SemiBold |
| Body | 11 pt Regular |
| Caption | 9 pt Light |

---

## 4. Grid System

### 4.1 PPTX 16:9 (1280 × 720 px)
- Margin: 48 px ทุกด้าน
- Column: 12
- Gutter: 24 px
- Header Height: 80 px (Logo 64 px + Page Indicator)
- Footer Height: 32 px (CI Footer Line สี iCE Secondary)

### 4.2 Word A4 Portrait
- Margin: 2.54 cm
- Column: 1
- Header: 1.27 cm (Logo iCE + ชื่อเอกสาร)
- Footer: 1.27 cm (Page Number + "Corporate Identity Guideline : iCE Consulting Co., Ltd")

### 4.3 Logo Placement (ตามคู่มือ CI)
- ตำแหน่ง: มุมขวาบน หรือ มุมซ้ายบน
- Safety Zone: เว้นพื้นที่รอบโลโก้อย่างน้อย 16 px ทุกด้าน
- ขนาดต่ำสุด: ความสูง 32 px (ไม่เล็กไปกว่านี้เพื่อความชัดเจน)
- บนพื้นขาว/อ่อน → ใช้ Logo สี
- บนพื้นเข้ม (ค่าน้ำหนักสีเกิน 50%) → ใช้ Logo ขาว

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
| 2xl | 64 px |

---

## 6. Image Treatment

- โทนภาพ: Professional, Clean, Modern
- รูปทรง: สี่เหลี่ยมขอบมน 8 px
- Style: Business Setting, Technology, Digital Transformation
- Filter: ปรับ Blue Cast เล็กน้อยเพื่อความเข้ากับ Brand
- Overlay: iCE Main Blue Opacity 30% สำหรับ Hero Image

---

## 7. Iconography Style

- สไตล์: Outline เส้น 2 px ขอบมน
- ขนาด: 24 / 32 / 48 px
- สีหลัก: `#1E66A4` (iCE Main Blue)
- สีรอง: `#41A8B5` (iCE Secondary Blue)
- Recommend: Material Symbols Outlined, Lucide Icons

### 7.1 Brand-Specific Visual Elements (ตามคู่มือ CI)
- ใช้องค์ประกอบ Dot Grid และ Pattern จุด-เส้น เป็นองค์ประกอบตกแต่ง
- Gradient Diagonal iCE Main → iCE Secondary สำหรับ Accent Bar

---

## 8. Animation & Transition

- Slide Transition: Fade 0.4s
- Object Animation: Fade-In 0.3s
- หลีกเลี่ยง: Bounce, Spin, Comic Animation

---

## 9. Accessibility Notes

| ประเด็น | มาตรฐาน |
| :--- | :--- |
| Contrast (Charcoal บนขาว) | 12.6:1 (AAA) |
| Contrast (ขาวบน iCE Main Blue) | 7.2:1 (AAA) |
| Body Font Size | ≥ 18 pt (PPTX), ≥ 11 pt (Word) |
| Print Test | ผ่านการพิมพ์ขาว-ดำ ไม่สูญเสียความหมาย |

---

## 10. 15 Layout Patterns

### Layout 01 — Title / Cover (Official Hero)
- **Background:** ขาว Pure White
- **Header Bar:** แถบบนหนา 8 px Gradient Diagonal iCE Main → iCE Secondary
- **Text:** Headline 60 pt ExtraBold สี iCE Main Blue กึ่งกลางซ้าย
- **Subtitle:** 22 pt Light สี Dark Gray
- **Logo:** ขวาบน Logo สี 100 px พร้อมชื่อบริษัท Open Sans ใต้โลโก้
- **Footer:** วันที่ + ชื่อเอกสาร 12 pt Caption

### Layout 02 — Section Divider
- **Background:** Gradient Diagonal iCE Main → iCE Secondary เต็มหน้า
- **Text:** หมายเลข Section "01" Display 200 pt Outline สีขาว
- **Section Title:** Display 60 pt ExtraBold สีขาว
- **Logo:** ขวาบน Logo ขาว

### Layout 03 — Two-Column Text
- **Header:** Title Bar 80 px H2 iCE Main Blue + Logo ขวา
- **Body:** สองคอลัมน์ Body 18 pt Dark Gray
- **Divider:** เส้นแนวตั้งสี iCE Blue 30 ตรงกลาง
- **Footer:** "Corporate Identity Guideline : iCE Consulting Co., Ltd"

### Layout 04 — Text Left + Image Right
- **Header:** Title Bar 80 px
- **Image:** ขวา 50% ขอบมน 8 px พร้อม Border iCE Secondary
- **Text:** ซ้าย 50% H3 + Body
- **Caption:** ใต้ภาพ Caption Light 14 pt

### Layout 05 — Image Left + Text Right
- (กลับด้าน Layout 04)
- **Use Case:** Customer Profile, Service Highlight

### Layout 06 — Full-Bleed Image with Brand Overlay
- **Image:** เต็มหน้า + Overlay iCE Main Blue Opacity 40% ฝั่งซ้าย
- **Text:** Headline ซ้ายบน 56 pt ExtraBold สีขาว
- **Logo:** ขวาบน สีขาว
- **Brand Bar:** แถบล่างหนา 8 px Gradient iCE

### Layout 07 — Three-Column Cards
- **Header:** Title Bar 80 px
- **Cards:** 3 การ์ดพื้น Cool Gray Light ขอบมน 8 px Padding 24 px
- **Card Header:** แถบบน 4 px iCE Main Blue
- **Card Icon:** 32 px iCE Secondary Blue Outline
- **Card Title:** H3 iCE Main Blue Bold
- **Card Body:** Body Dark Gray

### Layout 08 — Quote / Testimonial
- **Background:** Cool Gray Light
- **Quote Mark:** "" สี iCE Secondary Blue 240 pt มุมซ้ายบน Opacity 60%
- **Quote Body:** 32 pt Italic iCE Main Blue
- **Attribution:** Avatar 80 px ขอบมน + ชื่อ Bold + ตำแหน่ง Caption

### Layout 09 — Big Number / Stat Highlight
- **Header:** Title Bar 80 px H2 บอกบริบท
- **Stat:** ตัวเลข 200 pt ExtraBold สี iCE Main Blue กึ่งกลาง
- **Unit:** "%" หรือ "x" สี iCE Secondary Blue 56 pt
- **Body:** อธิบายแหล่งที่มา 16 pt Caption

### Layout 10 — Timeline / Roadmap
- **Header:** Title Bar 80 px
- **Timeline Bar:** Gradient iCE Main → iCE Secondary หนา 4 px
- **Milestone:** วงกลม 16 px iCE Main Blue + ขอบขาว 2 px
- **Labels:** H3 + Caption สลับบน-ล่าง

### Layout 11 — Comparison Table
- **Header:** Title Bar 80 px
- **Table Header:** สี iCE Main Blue ตัวอักษรขาว Padding 16 px
- **Stripe:** สลับขาว / Cool Gray Light
- **Highlight Column:** สี iCE Blue 10 + Border iCE Secondary
- **Footer Row:** Total เน้นด้วย iCE Main Blue 80%

### Layout 12 — Process Flow / Diagram
- **Header:** Title Bar 80 px
- **Step Box:** 3-5 กล่องเรียงแนวนอน พื้น Cool Gray Light ขอบมน 8 px
- **Connector:** ลูกศรหัวมน iCE Secondary Blue
- **Step Number:** วงกลม 32 px Gradient iCE ตัวเลขขาว
- **Label:** H3 iCE Main Blue + Body 14 pt

### Layout 13 — Bullet List / Key Points
- **Header:** Title Bar 80 px
- **Bullet:** ● จุดวงกลม 8 px สี iCE Secondary
- **Indent:** 24 px
- **Line Spacing:** 1.6
- **Highlight Word:** Bold + iCE Main Blue

### Layout 14 — Q&A / Discussion
- **Background:** iCE Blue 10
- **Headline:** "Q&A — คำถามและคำตอบ" 64 pt ExtraBold iCE Main Blue
- **Subtitle:** "เปิดให้ซักถาม / Open Discussion" Caption Dark Gray
- **Logo:** ขวาบน

### Layout 15 — Closing / Thank You
- **Background:** Gradient Diagonal iCE Main → iCE Secondary เต็มหน้า
- **Headline:** "ขอบคุณ — Thank You" 80 pt ExtraBold สีขาว กึ่งกลาง
- **Contact Block:** ใต้ Headline
  - อีเมล / โทรศัพท์ / เว็บไซต์ Caption Light สีขาว
  - Icon Outline ขาว 24 px
- **Logo:** มุมขวาบน Logo สีขาว
- **Brand Promise:** Footer "พันธมิตรทางเทคโนโลยี" ตัวเล็ก Caption

---

## 11. Application Notes

### 11.1 PowerPoint
- เริ่มจาก Master Slide ที่กำหนด:
  - Theme Color: iCE Main / iCE Secondary / Cool Gray / White
  - Theme Font: Heading = Kanit Bold, Body = Sarabun
- ตั้ง Logo ในตำแหน่งคงที่ทุก Layout
- บันทึก `.potx` เป็น Template มาตรฐาน

### 11.2 Word
- ใช้ Theme Built-in: ปรับ Color ตรงกับ Section 2.1
- ตั้ง Heading 1 = Kanit Bold 18 pt iCE Main Blue
- ตั้ง Heading 2 = Kanit SemiBold 14 pt iCE Main Blue
- ตั้ง Body = Sarabun Regular 11 pt Dark Gray
- Header: ใส่ Logo + ชื่อเอกสาร
- Footer: ใส่ "Corporate Identity Guideline : iCE Consulting Co., Ltd"

### 11.3 Logo Usage Rules (ตามคู่มือ CI)
- ✅ ใช้ Logo สี บนพื้นขาว (JPEG, PNG)
- ✅ ใช้ Logo ขาว บนพื้นสี (PNG)
- ❌ ห้ามเพิ่มรายละเอียดใน Logo
- ❌ ห้ามบิดสัดส่วน — ต้องใช้ Shift/Ctrl ขณะย่อ-ขยาย
- ❌ ห้ามวางบนพื้นที่มีลวดลายเยอะ — เลือกพื้นเรียบ

### 11.4 ห้ามทำ
- ห้ามใช้ฟอนต์มีหัว (Cordia, Browallia, Angsana) ในงานทางการ
- ห้ามใช้สี iCE ปลอม (เช่น น้ำเงิน Microsoft, น้ำเงิน Facebook)
- ห้ามใช้ Logo คู่กับ Logo Partner โดยไม่เว้น Safety Zone
- ห้ามใช้ Logo เก่า / รุ่นก่อน Dec 2021

---

## 12. Cross-Reference: Templates Other Than iCE-CI

iCE-CI Template เป็น **ค่าเริ่มต้น** ของ Skill นี้
หากผู้ใช้งานต้องการ Mood ที่ต่างออกไป ให้พิจารณา Template อื่นในตระกูลเดียวกัน:

| Mood | Recommend Template |
| :--- | :--- |
| Soft / Sustainability | Linen |
| Tech / Innovation | Arctic |
| Executive / Investor | Cobalt |
| Premium / Luxury | Onyx |
| Marketing / Energy | Amber |
| Internal / Workshop | Whiteboard |

ทุก Template อ้างอิง iCE Main Blue และ iCE Secondary Blue เป็น Anchor ดังนั้นแม้เปลี่ยน
Template สีก็ยังคงสอดคล้องกับ Brand

---

**End of iCE-CI Designer Brief**
