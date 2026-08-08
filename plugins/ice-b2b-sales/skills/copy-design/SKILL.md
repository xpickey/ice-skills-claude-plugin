---
name: copy-design
description: "Copy Design — สกัด design language ของเว็บไซต์ (สีจริง typography spacing component patterns) ออกมาเป็นไฟล์ DESIGN.md มาตรฐาน (แนวคิด Google Stitch / VoltAgent awesome-design-md) เพื่อใช้ co-brand ลูกค้าใน deck/HTML demo/proposal — ต่อยอด customer-ci-finder จาก 'logo+hex' เป็น design system เต็มใบ. เก็บจากของจริงเท่านั้น ไม่ invent สี/ฟอนต์. Triggers (TH): เก็บ design เว็บ, สกัดสี CI ลูกค้า, ทำ DESIGN.md, copy design, ดึง design language, สี brand ลูกค้า. Triggers (EN): copy design, extract design system, DESIGN.md, brand extraction, design tokens from site."
---

> **Skill:** copy-design | **Version:** V01R02 | **Date:** 2026.08.08
> **V01R02 (2026.08.08 · FLEET READABILITY V3 Phase 2):** +ตารางนิยาม (design language · DESIGN.md · design token · computed style · CSS variables · hex · A1/H2 · H3 · provenance · L1) + กติกาเหล็กเป็นประโยคเต็มพร้อมตัวอย่าง ❌/✅ — วิธีสกัดเดิมครบทุกข้อ
> **ที่มา:** vet จาก `VoltAgent/awesome-design-md` (MIT) 2026.07.18 — ยืมโครง DESIGN.md (73+ ตัวอย่างจริง: Apple/Figma/Airbnb) มาเป็น template · เขียน extractor เองด้วยเครื่องมือในระบบ

# ตารางนิยาม — ศัพท์และรหัสทุกตัวที่ไฟล์นี้ใช้

> วิธีเขียนไฟล์ระบบที่ skill นี้ยึด: `~/.claude/agents/reference/fleet-writing-standard.md`

| ศัพท์ / รหัส | ความหมาย |
|---|---|
| **design language (ภาษาการออกแบบ)** | ชุดกติกาที่ทำให้เว็บหนึ่งดูเป็นแบรนด์นั้น — สี ตัวอักษร ระยะห่าง ความมนของมุม และรูปทรงของ component ที่ใช้ซ้ำ |
| **DESIGN.md** | ไฟล์ผลลัพธ์ของ skill นี้ที่บันทึก design language ที่สกัดมาได้ ตามโครงในหัวข้อ template |
| **design token** | ค่าตั้งต้นที่นำไปใช้ซ้ำได้ เช่น สี primary หนึ่งค่า ขนาดตัวอักษรหนึ่งชุด — เก็บเป็นค่า ไม่ใช่คำบรรยาย |
| **computed style** | ค่าจริงที่เบราว์เซอร์คำนวณและใช้แสดงผลจริง (ต่างจากค่าที่เขียนใน CSS ซึ่งอาจถูกทับ) — เป็นแหล่งค่าที่เชื่อถือได้ที่สุด |
| **CSS variables (`:root`)** | ตัวแปรสีและขนาดที่เว็บประกาศไว้ใช้ทั้งไซต์ — ถ้าเว็บมี ให้เก็บชุดนี้ก่อนเพราะเป็น token ตัวจริงของแบรนด์ |
| **hex** | รหัสสีหกหลักแบบ `#1E66A4` |
| **A1 gate / H2** | ด่านขออนุญาต user ก่อนออก internet · H2 = กฎเหล็ก CLAUDE.md เครื่อง PART 3 ข้อ 2 |
| **H3** | กฎเหล็ก PART 3 ข้อ 3: ห้ามกุข้อมูล — ในงานนี้แปลว่า ห้ามเดาค่าสี/ฟอนต์ที่อ่านไม่ได้ |
| **provenance (ที่มา)** | ข้อมูลกำกับใน frontmatter: URL ต้นทาง วันที่เก็บ วิธีที่ใช้ — ไม่มี = ใช้อ้างอิงไม่ได้ |
| **L1 / b2b-slide-designer** | L1 = agent ระดับบนที่เป็นเจ้าของงาน (กัปตัน/คิม/สมนึก) · `b2b-slide-designer` = skill ออกแบบสไลด์ — ทั้งสองคือผู้ตัดสินว่าจะเอา design ที่เก็บมาใช้อย่างไร ส่วน skill นี้เก็บอย่างเดียว |
| **เลขวงกลม ① ② ③ ④** | ลำดับวิธีใน Method Ladder ไม่ใช่รหัสทีม |

# กติกาเหล็ก
1. **A1/H2 GATE — เข้า internet เฉพาะเมื่อ user อนุญาตในงานนั้น:** ซองคำสั่งต้องมีสิทธิ์ระบุไว้ · ไม่มี = แจ้งผู้มอบงานว่าติดด่าน ห้ามเปิดเว็บเอง
2. **ของจริงเท่านั้น (H3):** ค่าสี ฟอนต์ ระยะห่าง ทุกค่าต้องอ่านจากหน้าเว็บหรือ CSS จริง (computed style · stylesheet · ไฟล์ asset) เพราะค่าที่เดาไว้จะกลายเป็นแบรนด์ปลอมบนเอกสารที่ส่งลูกค้า · ค่าที่หาไม่ได้ให้เว้นว่างแล้วใส่ไว้ในรายการ `not_found`
   ❌ `primary: "#1E66A4"  # เดาจากภาพหน้าจอ` · ✅ `primary: "#1E66A4"  # getComputedStyle ปุ่ม CTA` หรือ `not_found: [primary]`
3. **PROVENANCE frontmatter บังคับ** — ต้องมี `source_url` + `fetched` + `method` เหมือน skill `copy-page-md` เพราะ design ของแบรนด์เปลี่ยนได้ ผู้ใช้ผลต้องรู้ว่าเก็บมาวันไหน
4. **เก็บ ไม่ตัดสิน:** สกัด design ที่เห็นตามจริง ห้ามวิจารณ์ว่าสวยหรือไม่สวย และห้ามเลือกให้ว่าควรใช้ค่าไหน เพราะการตัดสินใจใช้เป็นของ L1 และ skill ออกแบบสไลด์ที่เห็นบริบทงานทั้งหมด
   ❌ "สีนี้เข้มไป แนะนำใช้โทนอ่อนกว่า" · ✅ บันทึกค่าที่พบครบแล้วปล่อยให้ผู้ออกแบบเลือก

# วิธีสกัด (Method Ladder)
```
① Browser pane: เปิดหน้า → javascript_tool อ่าน getComputedStyle ของ element ตัวแทน
   (headings h1-h3 · body · buttons · links · cards) + ดึง CSS variables (:root)
   → ได้ hex/font/size/weight/line-height/radius จริง
② WebFetch หน้า + stylesheet หลัก → parse ค่าจาก CSS (fallback เมื่อไม่มี browser)
③ Screenshot (computer screenshot/zoom) → ยืนยันภาพรวม (สีที่ render จริง ≠ CSS เสมอ)
④ อ้างอิงโครงจากคลัง awesome-design-md (MIT) เมื่อเว็บดังมีอยู่แล้ว — cite repo
```

# DESIGN.md TEMPLATE (โครงตาม awesome-design-md — เติมเฉพาะที่เจอจริง)

> **รูปแบบไฟล์:** เขียนเป็นไฟล์ Markdown ที่มี frontmatter คั่นด้วย `---` ด้านบน (แต่ละคีย์อยู่บรรทัดของตัวเอง)
> ส่วนเนื้อด้านล่างเขียนเป็นบล็อก YAML ก้อนเดียว เพื่อให้เครื่องอ่านค่าไปใช้ต่อได้โดยไม่ต้องแกะจากข้อความ

```markdown
---
version: alpha          # คงค่า "alpha" ไว้เสมอจนกว่าผู้ใช้จะรับรอง design ชุดนี้ว่าใช้ได้จริง
name: "<Brand>-design-analysis"
source_url: "<url>"
fetched: "YYYY.MM.DD HH:MM"
fetched_by: "retrieval-scout (เสี่ยวป้อ) | <persona>"
method: "browser | webfetch"
title: "<ชื่อหน้าตามจริง>"
status: "complete | partial(<เหตุผล>)"
description: "<1 ย่อหน้า: บุคลิก design ที่เห็นจริง — โทน สี จังหวะ ความรู้สึก>"
---
logo:              # ที่อยู่ไฟล์โลโก้ที่ดาวน์โหลดเก็บไว้ + รูปแบบไฟล์ + พื้นหลังที่ใช้ได้ (สว่าง/มืด)
colors:            # hex จริงจากหน้า — primary/on-primary/ink/canvas/surface/accent/semantic
typography:        # ต่อ role (display/heading/body/caption): fontFamily/fontSize/fontWeight/lineHeight/letterSpacing
spacing_radius:    # grid unit · border-radius ที่ใช้ซ้ำ · shadow
components:        # ปุ่ม/card/nav ที่เป็นเอกลักษณ์ (รูปทรง+พฤติกรรม)
rules:             # กติกาที่สังเกตได้ (เช่น "CTA = pill เสมอ" "ไม่ใช้เงา")
not_found: [ ... ] # ค่าที่หาไม่ได้ — ห้ามเดา
```

**สองกติกาที่ต้องรู้ตอนเก็บจริง:**
- **ค่า CSS ไม่ตรงกับสีที่เห็นบนจอ → ยึด computed style เป็นค่าหลัก** แล้วบันทึกสีที่เห็นจาก screenshot ไว้ใน `rules` ว่าต่างกันอย่างไร (มักเกิดจากความโปร่งใสหรือ blend mode ซ้อนกัน) — ห้ามเลือกค่าใดค่าหนึ่งเงียบ ๆ
- **ขั้น ④ ที่อ้างอิงคลัง awesome-design-md ใช้เป็นตัวเทียบเท่านั้น ไม่ใช่แหล่งค่า** — ค่าที่บันทึกลง DESIGN.md ต้องมาจากหน้าเว็บจริงของลูกค้าเสมอตามกติกาข้อ 2 · เว็บองค์กรของลูกค้าส่วนใหญ่ไม่อยู่ในคลังนั้นอยู่แล้ว
- ปลายทาง: `[project]/00 - Context/_retrieved/DESIGN_<brand>_<YYYY.MM.DD>.md`
- ผู้ใช้ผล: กัปตัน/คิม (design spec ขั้น D-P2) + b2b-slide-designer (co-brand) + HTML demo (CSS vars)

*Skill: copy-design **V01R02** | 2026.08.08 | ใช้โดย: retrieval-scout-agent (หลัก) + ผู้ build ใน pipeline · แรงบันดาลใจ: VoltAgent/awesome-design-md (MIT) + Google Stitch DESIGN.md*
