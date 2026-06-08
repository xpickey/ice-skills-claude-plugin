# Linen Template — Designer Brief (iCE-CI Integrated)

> **Version:** V01R01 | **Date:** 2026-04-28
> **Concept:** "ผ้าลินินสีครีม ผสานน้ำเงิน iCE" — Natural Texture, Elegant, Trustworthy

---

## 1. Theme Concept (แนวคิดของ Template)

Linen ออกแบบมาเพื่อสื่อสาร "ความเป็นธรรมชาติ ความนุ่มนวล และความน่าไว้วางใจระยะยาว"
เหมาะอย่างยิ่งสำหรับงานที่ต้องการลดความแข็งกระด้างของ Corporate Tone เช่น Soft Proposal,
HR Communication, Sustainability Report, ESG Disclosure, Brand Story, และ Wellness/CSR
Campaign โดยใช้พื้นผิวสีครีมอุ่น (Linen White) เป็นพื้นหลังหลัก ตัดด้วย iCE Main Blue
สำหรับหัวข้อสำคัญ และ iCE Secondary Blue สำหรับองค์ประกอบรอง

อารมณ์ของ Template: เรียบหรู ผ่อนคลาย เปิดกว้าง น่าไว้วางใจ มืออาชีพแต่ไม่เย็นชา

---

## 2. Color System (ระบบสี)

### 2.1 Primary Palette

| Role | Hex | Sample Use |
| :--- | :--- | :--- |
| Background Primary | `#FAF0E6` (Linen White) | พื้นหลังหลักของทุกสไลด์ |
| Background Soft | `#F5E6D3` (Cream Mist) | กล่องเน้นข้อความ Section พื้นรอง |
| Accent Brand 1 | `#1E66A4` (iCE Main Blue) | หัวข้อหลัก (H1), ปุ่ม CTA, ตัวเลขสถิติ |
| Accent Brand 2 | `#41A8B5` (iCE Secondary Blue) | กราฟ, เส้นแบ่ง, ไอคอน, ลิงก์ |
| Text Primary | `#333333` (Charcoal) | Body Text บนพื้นอ่อน |
| Text Secondary | `#6E6E6E` (Warm Gray) | Caption, Metadata, Footer |

### 2.2 Tints & Shades (เฉดเสริม)

| Token | Hex | การใช้งาน |
| :--- | :--- | :--- |
| iCE Blue 90 | `#205F94` | Hover State, Active Link |
| iCE Blue 50 | `#7AA8CC` | Background Card หัวข้อรอง |
| iCE Blue 10 | `#E5EEF5` | Background Highlight อ่อน |
| Linen 90 | `#E8DAC4` | Section Divider, Border |
| Linen 50 | `#F2E4D2` | Hover Background |

### 2.3 Semantic Colors

| สถานะ | Hex | การใช้งาน |
| :--- | :--- | :--- |
| Success | `#3B8A5A` (Sage Green) | ผลลัพธ์ดี, Achievement |
| Warning | `#C99738` (Amber Soft) | คำเตือน, ข้อควรระวัง |
| Error | `#B0454A` (Muted Brick) | ข้อผิดพลาด, Risk |
| Info | `#41A8B5` (iCE Secondary) | ข้อมูลอ้างอิง, Note |

---

## 3. Typography Hierarchy (ระบบตัวอักษร)

### 3.1 Font Stack

| Language | Primary | Secondary |
| :--- | :--- | :--- |
| Thai | Kanit | Sarabun |
| English | Raleway | Open Sans |

### 3.2 Type Scale (PPTX 16:9)

| Role | Font | Weight | Size | Line Height | Letter Spacing |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Display | Kanit / Raleway | Light 300 | 60 pt | 1.1 | -1% |
| H1 | Kanit / Raleway | Bold 700 | 36 pt | 1.2 | 0 |
| H2 | Kanit / Raleway | SemiBold 600 | 28 pt | 1.3 | 0 |
| H3 | Kanit / Raleway | Medium 500 | 22 pt | 1.3 | 0 |
| Body Large | Sarabun / Open Sans | Regular 400 | 20 pt | 1.5 | 0 |
| Body | Sarabun / Open Sans | Regular 400 | 18 pt | 1.5 | 0 |
| Caption | Sarabun / Open Sans | Light 300 | 14 pt | 1.4 | 0 |

### 3.3 Type Scale (Word A4)

| Role | Size | Use |
| :--- | :--- | :--- |
| Cover Title | 32 pt | หน้าปกเอกสาร |
| Heading 1 | 18 pt | บทใหญ่ |
| Heading 2 | 14 pt | หัวข้อย่อย |
| Body | 11 pt | เนื้อความปกติ |
| Caption | 9 pt | Footnote, รูปประกอบ |

---

## 4. Grid System (ระบบกริด)

### 4.1 PPTX 16:9 (1280 × 720 px)

- Margin: 48 px ทุกด้าน
- Column: 12 คอลัมน์
- Gutter: 24 px
- Header Height: 80 px (Logo + Page Number Zone)
- Footer Height: 40 px (CI Footer Line)

### 4.2 Word A4 Portrait

- Margin: 2.54 cm (top/bottom), 2.0 cm (left/right)
- Column: 1 หรือ 2 (สำหรับ Newsletter Style)
- Gutter (2-col): 0.8 cm
- Header: 1.27 cm (Logo + Title)
- Footer: 1.27 cm (Page Number + Document Code)

---

## 5. Spacing / Padding Scale

ใช้ระบบ 8-point grid ทั่วทั้ง Template

| Token | Value | Use |
| :--- | :--- | :--- |
| xxs | 4 px | Inline Padding ในไอคอน |
| xs | 8 px | ช่องไฟภายใน Tag/Chip |
| sm | 16 px | ช่องไฟ Card Padding |
| md | 24 px | ระยะระหว่างคอลัมน์ |
| lg | 32 px | ระยะระหว่าง Section ภายในสไลด์ |
| xl | 48 px | Margin หลักของสไลด์ |
| 2xl | 64 px | ระยะ Hero Padding |

---

## 6. Image Treatment (สไตล์การใช้รูปภาพ)

- โทนภาพ: อบอุ่น (Warm Tone) อุณหภูมิสี 5500–6000K
- Filter: ลด Saturation 10–15% เพื่อให้กลมกลืนกับพื้นลินิน
- รูปทรง: สี่เหลี่ยมขอบมน 12 px หรือวงกลม
- Border: เส้นบาง 2 px สี iCE Secondary Blue (Optional)
- Caption: วางใต้รูป ใช้ Caption Style สี Warm Gray

---

## 7. Iconography Style

- สไตล์: Outline (เส้นบาง 1.5–2 px) ขอบมน
- ขนาดมาตรฐาน: 24 / 32 / 48 px
- สีหลัก: `#1E66A4` (iCE Main Blue)
- สีรอง: `#41A8B5` (iCE Secondary Blue)
- ห้ามใช้ Icon แบบ Solid Fill หรือ Multi-color

---

## 8. Animation & Transition

- Slide Transition: Fade 0.4s
- Object Animation: Fade-In Up 0.3s ระยะ 24 px
- หลีกเลี่ยง: Bounce, Spin, Zoom-Out, Curtain
- ลำดับ: เน้นองค์ประกอบสำคัญก่อน (Headline → Body → Detail)

---

## 9. Accessibility Notes

| ประเด็น | มาตรฐาน |
| :--- | :--- |
| Contrast Ratio | Charcoal บน Linen White = 11.5:1 (AAA) |
| Body Font Size | ≥ 18 pt (PPTX), ≥ 11 pt (Word) |
| Color-only Information | ห้ามใช้สีเพียงอย่างเดียวสื่อความหมาย |
| Alt Text | ทุกภาพต้องมีคำอธิบายภาษาไทย |

---

## 10. 15 Layout Patterns (รูปแบบการวาง 15 หน้า)

> หมายเหตุ: 15 หน้านี้คือ "Layout Patterns" ที่หมุนเวียนใช้ตามความต้องการเนื้อหา
> ไม่ใช่ลำดับ Cover → Agenda → Closing แบบตายตัว

### Layout 01 — Title / Cover (หน้าปก)
- **Header:** ไม่มี (Full Bleed)
- **Image:** พื้นผิวลายลินินจางๆ เต็มหน้า (Opacity 30%)
- **Text:** Headline กึ่งกลางซ้าย ขนาด Display, สี iCE Main Blue
- **Logo:** มุมขวาบน 80 px
- **Accent:** เส้นบาง 4 px สี iCE Secondary Blue ใต้ Headline

### Layout 02 — Section Divider (หน้าคั่นหัวข้อ)
- **Header:** ไม่มี
- **Image:** พื้นหลังครีม Solid
- **Text:** หมายเลข Section ขนาด Display 120 pt สี iCE Blue 50, ชื่อ Section H1 ใต้หมายเลข
- **Accent:** เส้น Hairline แนวตั้งซ้ายมือสูง 60% ของความสูงสไลด์

### Layout 03 — Two-Column Text (สองคอลัมน์ข้อความ)
- **Header:** Title Bar 80 px พร้อม H2 ซ้าย, Logo ขวา
- **Image:** ไม่มี
- **Text:** สองคอลัมน์เท่ากัน ระยะ Gutter 24 px, Body 18 pt
- **Accent:** เส้นแบ่งแนวตั้งสี Linen 90 ตรงกลาง

### Layout 04 — Text Left + Image Right (ข้อความซ้าย รูปขวา)
- **Header:** Title Bar 80 px, H2 ซ้าย
- **Image:** ขวา 50% ของความกว้าง ขอบมน 12 px
- **Text:** ซ้าย 50%, H3 + Body 18 pt, Bullet จุดสี iCE Secondary
- **Caption:** ใต้ภาพ 14 pt Warm Gray

### Layout 05 — Image Left + Text Right (รูปซ้าย ข้อความขวา)
- **Header:** Title Bar 80 px, H2 ขวา
- **Image:** ซ้าย 50%, ขอบมน 12 px พร้อม Border 2 px iCE Secondary Blue
- **Text:** ขวา 50%, H3 + Body 18 pt
- **Variation:** ใช้เมื่อต้องการให้สายตาเริ่มจากภาพก่อน

### Layout 06 — Full-Bleed Image (รูปเต็มหน้า)
- **Header:** Logo สีขาวมุมขวาบน
- **Image:** เต็มหน้า ใส่ Overlay สี iCE Blue Opacity 30% ที่ฝั่ง Text
- **Text:** Headline ฝั่งซ้ายล่าง สีขาว ขนาด Display
- **Use Case:** Brand Story, Customer Testimonial Hero

### Layout 07 — Three-Column Cards (สามการ์ดเรียง)
- **Header:** Title Bar 80 px H2 ซ้าย, Subtitle ใต้ H2
- **Cards:** 3 การ์ดขนาดเท่ากัน พื้นหลัง Cream Mist, ขอบมน 12 px, Padding 24 px
- **Card Header:** Icon 32 px iCE Blue + H3 ใต้ Icon
- **Card Body:** Body 16 pt 3–4 บรรทัด

### Layout 08 — Quote / Testimonial (คำพูดอ้างอิง)
- **Header:** ไม่มี (เพื่อความสง่า)
- **Background:** Linen White Solid
- **Text:** Quote Mark ขนาด 200 pt สี iCE Blue 50 มุมซ้ายบน
- **Quote Body:** กึ่งกลางสไลด์ ขนาด 32 pt Italic
- **Attribution:** ใต้ Quote ขนาด 16 pt Warm Gray พร้อมรูป Avatar วงกลม 64 px

### Layout 09 — Big Number / Stat Highlight (ตัวเลขเด่น)
- **Header:** Title Bar 80 px H2 บอกบริบท
- **Stat:** ตัวเลขขนาด 180 pt สี iCE Main Blue กึ่งกลางสไลด์
- **Unit/Label:** ใต้ตัวเลข ขนาด H3 สี Charcoal
- **Supporting Text:** Body 16 pt อธิบายแหล่งที่มา

### Layout 10 — Timeline / Roadmap (เส้นเวลา)
- **Header:** Title Bar 80 px
- **Timeline Bar:** เส้นแนวนอนสี iCE Secondary Blue หนา 4 px กึ่งกลางสไลด์
- **Milestones:** จุดวงกลม 16 px สี iCE Main Blue ระยะเท่ากัน
- **Labels:** สลับบน-ล่าง H3 + Caption เดือน/ปี

### Layout 11 — Comparison Table (ตารางเปรียบเทียบ)
- **Header:** Title Bar 80 px
- **Table Header:** สี iCE Main Blue ตัวอักษรขาว Padding 16 px
- **Row Stripe:** สลับ Linen White / Cream Mist
- **Highlight Column:** สี iCE Blue 10 พร้อม Border iCE Secondary

### Layout 12 — Process Flow / Diagram (ขั้นตอน)
- **Header:** Title Bar 80 px
- **Step Boxes:** 3–5 กล่องเรียงแนวนอน พื้น Cream Mist, ขอบมน 12 px
- **Connectors:** ลูกศรหัวมน สี iCE Secondary Blue
- **Step Number:** วงกลม 32 px สี iCE Main Blue ตัวเลขขาว
- **Label:** H3 สี iCE Main Blue, Body 14 pt อธิบาย

### Layout 13 — Bullet List / Key Points (จุดสำคัญ)
- **Header:** Title Bar 80 px
- **Bullet Style:** จุดวงกลม 8 px สี iCE Secondary Blue
- **Indent:** 24 px จาก Margin ซ้าย
- **Line Spacing:** 1.6 ระหว่าง Bullet
- **Sub-Bullet:** เส้นขีด 8 px สี Warm Gray

### Layout 14 — Q&A / Discussion (คำถาม)
- **Header:** ไม่มี
- **Background:** iCE Blue 10
- **Text:** "Q&A" ขนาด Display สี iCE Main Blue กึ่งกลาง
- **Subtitle:** "ขอบคุณสำหรับความสนใจ — เปิดให้ซักถาม" สี Warm Gray
- **Logo:** มุมขวาล่าง

### Layout 15 — Closing / Thank You (หน้าจบ)
- **Header:** ไม่มี
- **Background:** Gradient Diagonal iCE Main Blue → iCE Secondary Blue
- **Text:** "ขอบคุณ — Thank You" สีขาว ขนาด Display กึ่งกลาง
- **Contact:** อีเมล / โทรศัพท์ / เว็บไซต์ Caption สีขาว Opacity 80% ใต้ Headline
- **Logo:** สีขาว มุมขวาบน

---

## 11. Application Notes

### 11.1 PowerPoint (.pptx)
- ใช้ Slide Master เพื่อกำหนด Color Theme และ Font Theme
- บันทึกเป็น `.potx` (Template) สำหรับใช้ซ้ำ
- ตั้ง Default Slide Size: Widescreen 16:9

### 11.2 Word (.docx)
- ใช้ Style System (Heading 1/2/3, Normal, Caption) แทนการ Format ตัวอักษรโดยตรง
- ตั้ง Theme Color ใน Design Tab ให้ตรงกับ Color System
- ใช้ Section Break เพื่อสลับ Layout 1-Column / 2-Column

### 11.3 ห้ามทำ (Don'ts)
- ห้ามใช้ Drop Shadow แบบหนักบนตัวอักษร
- ห้ามใช้ Gradient Background ที่ไม่ใช่ iCE Blue Family
- ห้ามใช้ Comic Sans, Cordia New, หรือฟอนต์มีหัวแบบไทยดั้งเดิม
- ห้ามใช้รูป Stock Photo ที่มี Watermark หรือคุณภาพต่ำกว่า 1500 px

---

**End of Linen Designer Brief**
