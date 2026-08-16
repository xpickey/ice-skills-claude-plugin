# iCE SUPER TEMPLATE — "Gold Line" (แม่แบบ deck มาตรฐาน iCE สำหรับ Proposal / Presentation)

> **Version:** V01R01 | 2026.08.07 | ส่วนหนึ่งของ skill `ice-doc-builder` (โหลดเมื่อ build deck iCE)
> **กำเนิด:** user พิมพ์ชุดคำสั่งเดียวกันซ้ำ ≥5 session (Viriyah ×4 · Akara · Minor) — รวบเป็นแม่แบบเดียว สั่งครั้งเดียวจบ
> **การใช้ (แก้ตามคำสั่ง user 2026.08.07 — เรียกโดยชื่อเท่านั้น):** template นี้ทำงานเมื่อ **user เอ่ยชื่อ "iCE Super Template"** (หรือสั่งชัดว่าใช้แม่แบบ iCE ลายทอง) → ดึงทั้งชุดขึ้นมาใช้ทันที ถามแค่ 4 ข้อ (§1) · **สั่ง deck ทั่วไปโดยไม่เอ่ยชื่อ = ห้ามเหมาใช้แม่แบบนี้เอง** — เดิน ASK-FIRST ปกติ (ถาม CI ไหน/รายละเอียดแบบใด/template อะไร)
> **ONE-HOME:** สี/type scale/grid/pattern A-D/anti-pattern = `b2b-slide-designer/references/template_ice_propose.md` (authority เดิม — ห้าม fork ตัวเลข) · ไฟล์นี้เพิ่ม **ชั้นลายเส้นทอง + สูตร background + archetype รายหน้า + คำถามก่อน build** เท่านั้น

---

## §1 ถามก่อน build (ASK-FIRST ชุดสั้น — รวบครั้งเดียว · รู้แล้วข้าม)

1. **อุตสาหกรรมลูกค้า** (กำหนดลายเส้น — ดู §3) 2. **ภาษาเอกสาร** thai / mix / english (กำหนดฟอนต์ §5) 3. **ผู้ชม** (ผู้บริหาร/IT/จัดซื้อ — กำหนดความลึกเนื้อหา) 4. **โครงหัวข้อ** มีแล้วหรือให้ร่าง — แค่ 4 ข้อนี้ นอกนั้นแม่แบบตัดสินให้หมด

## §2 ARCHETYPE รายหน้า (6 แบบ — ทุก deck iCE ประกอบจากชุดนี้)

| หน้า | พื้นหลัง | องค์ประกอบบังคับ |
|---|---|---|
| **① COVER ปก** | **สีเข้มไล่เฉด** (gradient 135° ฐาน #1E66A4→#41A8B5 โทนเข้ม) + **ลายเส้นทองคล้ำบาง**ตามอุตสาหกรรม (§3) — สร้างด้วย Higgsfield (§4) | ชื่อ Topic วางตำแหน่งเด่น อ่านง่าย (EN-first bilingual) · โลโก้ iCE **ขาว** มุมบนซ้าย + โลโก้ลูกค้าขาว/สว่างมุมบนขวา (กติกา CI: โลโก้ขาวบนพื้นเข้ม ห้ามใส่กล่อง) · ผู้เสนอ/วันที่ล่าง |
| **② TOC สารบัญ** | **เข้ม-อ่อนไล่เฉด** + ลายเส้นทองคล้ำบาง (motif เดียวกับปก จางกว่า) | **Level 1 + Level 2 จบใน 1 หน้า** · เลขหัวข้อสี teal · ชื่อหัวข้อขาว/เทาอ่อนตามพื้น |
| **③ DIVIDER หน้าคั่นหัวข้อ** | เข้ม-อ่อนไล่เฉด + ลายเส้นทอง (ชุดเดียวกับ TOC) | เลข section ตัวใหญ่ ghost + ชื่อหัวข้อ bilingual + โลโก้ตามกติกาพื้นเข้ม |
| **④ DETAIL เนื้อหา** (หัวข้อละหน้า) | **พื้นขาว** + **ลายทองรางเส้นบาง ๆ ไม่บังสายตา** (มุม/ขอบ ไม่ทับพื้นที่ข้อความ) | header/footer + type scale + grid ตาม iCE-Propose · โลโก้ iCE สีมุมบนขวา · การ์ด Pattern C เมื่อเป็นรายการ |
| **⑤ PROCESS / SOLUTION / FLOW** | พื้นขาวเหมือน ④ | ทำเป็น **infographic + icon** ไม่ใช่ bullet ยาว · **Color telling + Block Pattern + Shading ไล่สี**แยกประเภท/เฟส — palette ไม่ต้องตรง iCE CI แต่**โทนต้องไม่โดด** (ตระกูลเดียวกับ blue-teal-gold หรือโทนกลาง) · ซับซ้อน/หลายทางเลือก → **ถาม user ใน session ว่าต้องการแบบไหน + เสนอแบบที่เหมาะจากข้อมูล** ก่อนลงมือ |
| **⑥ CLOSING ปิดท้าย** | gradient เดียวกับปก | ข้อความปิด + ช่องทางติดต่อ + โลโก้ขาว |

**⭐ กฎกลางทุกหน้าอธิบาย (user เน้นย้ำ 2026.08.07 — ไม่ใช่แค่หน้า process):** การอธิบาย/แยกประเภท/แยกเฟส/แยกกลุ่มในทุกสไลด์ ให้ใช้ **Color telling + Block Pattern ลวดลาย + Shading ไล่สี** เป็นเครื่องมือหลักแทนการใช้ตัวหนังสือแยก — palette **ไม่จำเป็นต้องเป็น iCE CI** เลือกชุดสีที่เล่าเรื่องได้ดีที่สุดสำหรับเนื้อหานั้น แต่**โทนต้องไม่โดดจากทั้งเล่มจนเกินไป** (อยู่ตระกูลเดียวกับ blue-teal-gold หรือโทนกลางที่กลมกลืน) · ประเภทเดียวกัน = สีเดียวกันทุกหน้าทั้งเล่ม (consistency ของ color telling)

## §3 ลายเส้นทองตามอุตสาหกรรม (motif table — เลือกจากอุตสาหกรรมลูกค้า)

**สเปกทองเดียวกันทุกงาน:** ทองคล้ำ (muted gold ~#C9A86A → เข้มสุด #8F7B4F) · เส้นบาง · โปร่ง (บนพื้นเข้ม alpha ต่ำ · บนพื้นขาว จางมากจนไม่แย่งสายตา) · **ห้ามทองสด/ทองมัน** (ดูเป็นการ์ดอวยพร)

| อุตสาหกรรม | motif ลายเส้น |
|---|---|
| InsurTech / ประกัน | โล่ ร่ม เส้นใยเครือข่ายคุ้มครอง คลื่นข้อมูล |
| Food production | รวงข้าว ใบไม้ เส้นสายการผลิต ภาชนะ |
| Banking / FinTech | เสาอาคาร เส้นกราฟ ลายผลึก เส้นทางธุรกรรม |
| Manufacturing | เฟือง เส้น isometric โครงเครื่องจักร |
| Retail / Trading | เส้นทางสินค้า ชั้นวาง โหนดเชื่อม |
| Logistics / W&D | เส้นทางเดินรถ คลัง โครงข่ายจุดต่อ |
| Healthcare | เส้นชีพจร โมเลกุล ใบไม้การดูแล |
| Energy / Utilities | เส้นคลื่นพลังงาน สายส่ง กังหัน |
| ราชการ / SOE | ลายไทยประยุกต์เส้นบาง เรขาคณิตสมมาตร |
| อื่น ๆ / ไม่ระบุ | เรขาคณิตนามธรรมเส้นโค้งบาง (กลางที่สุด) |

## §4 สูตรสร้าง background (Higgsfield MCP · model openai — ทำครั้งเดียวต่อ deck)

1. **GENERATE ONCE, REUSE ALL:** สร้าง **ชุดละ 4 ภาพ** (ปกเข้ม · TOC/divider เข้ม-อ่อน · detail ขาวลายจาง · closing) motif เดียวกันทั้งชุด → save `<opp>/<งาน>/_build/assets/bg/` → **ใช้ซ้ำทุกหน้า archetype เดียวกัน — ห้าม generate รายหน้า** (คุมต้นทุน + ภาพนิ่งสม่ำเสมอทั้งเล่ม) · ลูกค้าเดิม deck ใหม่ = reuse ชุดเดิมได้ถ้า motif ยังตรง
2. **PROMPT แม่แบบ (เปลี่ยนเฉพาะ {motif} + {โทนพื้น}):** `elegant minimal {โทนพื้น} background, thin muted dark-gold line art of {motif}, subtle, luxurious consulting style, lines occupy edges/corner only, large clear empty area for text, no text, no logo, 16:9` · **preflight cost ก่อนยิงเสมอ** (กติกา Higgsfield เดิม)
3. **ตรวจก่อนใช้:** ลายไม่ทับพื้นที่ข้อความ · contrast ตัวอักษรบนพื้นผ่าน (ขาวบนเข้ม / เทาเข้มบนขาว — เกณฑ์ WCAG ของ D7.H3) · ภาพเดียวกันทุกหน้า archetype เดียวกัน
4. **FALLBACK ไม่มี Higgsfield/ยิงไม่ผ่าน:** วาดเองด้วย python-pptx (เส้นโค้ง/เรขาคณิตทอง freeform บาง ๆ ตาม motif) — **ไม่ block งาน ไม่วนรอ** แจ้ง user ว่าใช้ลายวาดแทนภาพ generate

**§4b INFOGRAPHIC + ICON (หน้า process/solution — user กำหนด 2026.08.07): สร้างได้ 2 ทาง เลือกตามความเหมาะสม**
- **⭐ ก่อนเลือกทางใด ต้องผ่านการตั้งโจทย์ตาม `b2b-slide-designer §4.11` ก่อนเสมอ** (คำถาม 5 ข้อ · ตัด→จัด→วาด · เสนอโครง 2 ทางพร้อมข้อเสียให้ user เลือก · ตรวจตัวเลขย้อนกลับหลังวาด) — หัวข้อนั้นเป็นบ้านเดียวของหลักการ ที่นี่ถือเฉพาะสูตรการผลิต
- **ทาง ① Higgsfield MCP (model openai):** เหมาะกับภาพประกอบเชิงบรรยากาศ/isometric/ภาพ concept — ดูความเหมาะสมก่อนยิง + preflight cost · 🔴 **ห้ามให้ AI generate ตัวหนังสือ/ตัวเลขฝังในภาพ** (สะกดเพี้ยนโดยเฉพาะไทย) — ภาพ = ฉาก/องค์ประกอบเท่านั้น ตัวหนังสือทั้งหมดวางเป็น text layer จริงใน PPTX ทับบนภาพ (แก้ไข/ค้นหา/แปลได้)
- **ทาง ② agent วาดเอง (python-pptx shapes + icon):** เหมาะกับ diagram/flow/chevron/matrix ที่ต้องแม่นตำแหน่งและแก้ไขได้ — **แต่ให้ระวัง (คำสั่ง user):** ① icon ทั้งเล่มชุดเดียว stroke เดียว สไตล์เดียว (flat หรือ line เลือกอย่างเดียว) — ห้าม emoji แทน icon ② ตัวเลข/ข้อมูลใน infographic ทุกตัวมาจาก spec เท่านั้น ห้ามประดิษฐ์ metric ประกอบภาพ (H3 — invented metric คือ visual AI tell อันดับต้น) ③ ผ่านด่าน D7.S visual anti-slop ของอริสเสมอ ④ ซับซ้อน/ไม่แน่ใจแบบ → ถาม user ใน session + เสนอแบบที่เหมาะจากข้อมูล ก่อนลงมือ
- เลือกทางไหนประกาศใน design spec ต่อหน้า (ผสมได้ในเล่มเดียว — ภาพบรรยากาศ=① · diagram แม่นยำ=②)

## §5 ฟอนต์ตามภาษาเอกสาร (ผูก `font_policy.RAILS` — ห้าม hard-code)

| โหมด | หัวเรื่อง | เนื้อความ |
|---|---|---|
| **thai** | ฟอนต์รางเอกชน (RAILS) น้ำหนัก Bold | ฟอนต์ราง Regular |
| **mix thai+EN** | EN = Raleway ExtraBold (คู่ละตินตาม CI) · TH = ฟอนต์ราง Bold — **bilingual EN-first: EN บน-เข้ม-ใหญ่ · TH ล่าง-เทา-เล็กกว่า** (กติกา iCE-Propose เดิม) | EN = Open Sans · TH = ฟอนต์ราง |
| **english** | Raleway ExtraBold | Open Sans Light |

จบ build รัน `_lib/audit_fonts.py` เสมอ (V4 rail conformance) · งานราชการ/TOR → รางราชการชนะ (§3.0 ของ SKILL.md)

## §6 ภาษาเขียน (pointer — บังคับทุก deck)

Write-Clean Card core A1-A5 + B-Business (ไม่ใช่สำนวน AI) · professional ละเอียดกระชับ ไม่ย่อความ ไม่ใช้คำย่อ · ศัพท์เฉพาะ: **ใช้ศัพท์จากเอกสารต้นฉบับลูกค้าก่อน** → ไม่มี = ทับศัพท์ EN → จะแปลไทยต้องค้นคำที่วงการใช้จริง (ขอ H2 ก่อนค้น) ห้ามประดิษฐ์เอง — SSOT: `reference/language-register.md` + `12_write_clean_card.md`

## §8 ⭐ CONSULTING-GRADE LAYOUT — เลือกแบบสวยระดับที่ปรึกษาให้อัตโนมัติ (คำสั่ง user 2026.08.07)

หน้าเนื้อหา (archetype ④/⑤) ไม่ต้องออกแบบจากศูนย์และไม่ต้องรอ user สั่ง — **template นี้มีหน้าที่เลือก layout ที่สวยและเหมาะกับเนื้อหาให้เอง** จากคลังใน `b2b-slide-designer/references/`:
- **`consulting-template-library.md`** — DNA 3 ค่าย: **M-style** (text-structured, hypothesis-driven — action title + โครงเหตุผล) · **B-style** (framework/matrix, action-oriented — 2×2, การเปรียบเทียบ) · **Bn-style** (results/financial-impact — ตัวเลขนำ)
- **`catalog-by-firm.md`** — ตัวอย่างจริง 480+ deck (รวม Deloitte/KPMG/EY/PwC/Accenture) + timeline examples · **`catalog-templates-ready.md`** ของพร้อมใช้

**ตารางตัดสิน — ชนิดสไลด์ → layout ที่เลือกให้ (default · เสนอทางเลือกเมื่อก้ำกึ่ง):**

| ชนิดสไลด์ | layout default | เหตุผล |
|---|---|---|
| **Executive Summary** | M-style: action title 1 ประโยคตอบคำถามผู้บริหาร + 3 แถวสรุป (สถานการณ์/ข้อเสนอ/ผลลัพธ์) | ผู้บริหารอ่าน 10 วินาทีจบ |
| **Approach / วิธีทำงาน** | M-style horizontal phase flow (chevron 3-5 เฟส + กิจกรรมใต้เฟส) | เล่าลำดับชัด |
| **Project Plan / Timeline** | Timeline+Swimlane (Pattern D ของ iCE-Propose) + ตัวอย่างจาก catalog timeline section | ผูกกับ RACI/milestone ได้ |
| **Proposed Solution / Architecture** | B-style framework block (ชั้น layer + module card) หรือ Pattern B Horizontal Tech Flow | เห็นภาพรวมระบบใน 1 หน้า |
| **ทางเลือก / เปรียบเทียบ (options)** | B-style 2×2 matrix หรือ comparison column + คะแนน | ตัดสินใจง่าย |
| **Business Case / ROI** | Bn-style ตัวเลขนำ (ตัวเลขใหญ่ 3 ช่อง + waterfall/bar ที่มาของค่า) | ผลลัพธ์การเงินเด่น |
| **Governance / ทีม** | org block + RACI mini (Pattern D ย่อ) | บทบาทชัด |
| **Fit-Gap / Compliance** | ตาราง status สี (Comply/Partial/Gap — Color telling) | scan เร็ว |

**กติกาการเลือก:** ① เลือก default ตามตารางแล้ว**ประกาศใน design spec** ว่าหน้าไหนใช้แบบไหนเพราะอะไร (user veto ได้ตอน PLAN-CARD) ② เนื้อหาก้ำกึ่ง 2 แบบ → เสนอ 2 ทางพร้อมความเห็นว่าแบบไหนเหมาะกว่าเพราะอะไร ให้ user เลือกใน session ③ ทั้งเล่มคุมโทนเดียว — DNA หลัก 1 ค่าย/เล่ม ผสมได้เฉพาะหน้าที่เนื้อหาต่างชนิดจริง ④ ทุก layout สวมสี/ฟอนต์/grid ของ iCE Super Template (ยืมโครง ไม่ยืมสี) ⑤ **H8 NAME-DROP SCRUB บังคับ:** ชื่อค่าย (McKinsey/BCG/Bain/Deloitte ฯลฯ) ใช้ได้เฉพาะไฟล์ภายใน — **ห้ามโผล่ในเนื้อ deck/notes/ชื่อไฟล์ที่ลูกค้าเห็นเด็ดขาด** (ด่านตรวจ = scrub section ของ consulting-template-library + อริส D6)

## §7 ลำดับ build (เข้ากับ DOC-PIPELINE ปกติ — ไม่มีขั้นพิเศษ)

D-P2: spec ระบุ `template: ice-super` + คำตอบ §1 + **layout ต่อหน้า (จากตาราง §8)** → D-P3: gen background ชุดเดียว (§4) → build ตาม archetype §2 + iCE-Propose spec → audit_fonts → D-P4: อริสตรวจ (D6.lib เทียบแม่แบบนี้ · D7.S กันลายเกิน · H8 scrub) · แก้ archetype/motif กลางทาง = แก้ที่ spec แล้ว rebuild หน้า archetype นั้น ไม่รื้อทั้งเล่ม
