---
name: ice-demo-builder
description: iCE Demo/Prototype Build Craft — ความรู้สร้าง application สำหรับ demo และ prototype ในงานขาย B2B (ERP/EPM/CRM) ระดับ specialist. ถือ DEMO-PIPELINE 6 ด่าน (QUALIFY → SPEC → DESIGN → BUILD → VERIFY → REHEARSE), ตาราง Tier เลือกความลึกของ demo, Demo Data Policy 3 ระดับ (POC ใช้ข้อมูลจริงที่ลูกค้ายินยอม · demo ทั่วไปใช้ข้อมูลแปลงสมจริง · ห้ามประดิษฐ์), stack recipes (NetSuite SuiteScript/UIF SPA, Oracle APEX, เว็บทั่วไป), tool map (frontend-design, ui-ux-pro-max, Figma MCP, Browser ในแอป, iOS Simulator) และ guardrails (เพดานรอบแก้ ≤3, ผู้ตรวจต้องรันแอปจริง). ใช้โดยกัปตัน (L0-adopted, build เอง) และ demo-builder-agent (โมโม่ ⑦, build เป็นชิ้น). Triggers (TH): ทำ demo แอป, สร้าง prototype, เตรียมแอปสาธิต, mockup หน้าจอ, แอปกดได้จริง, POC, โมโม่ build. Triggers (EN): build demo app, prototype application, clickable mockup, demo preparation, POC build, app for customer demo.
---

# iCE DEMO BUILDER — Demo/Prototype Application Craft

> **Skill:** ice-demo-builder | **Version:** V01R01 | **Date:** 2026.08.07
> **กำเนิด:** คำสั่ง user 2026.08.07 — เพิ่มความสามารถทำ Prototype/Demo app ให้ fleet โดยกัปตันออกแบบและสั่งโมโม่ ⑦ เป็นชิ้น ๆ ได้ · best practice สกัดจาก 3 repo (shanraisshan RPI · addyosmani agent-skills · cobusgreyling loop-engineering — หลักการมาเขียนเอง ไม่ clone, MIT ทั้งหมด) ผสานเข้ากติกา fleet เดิม (DOC-PIPELINE V3 · H3/H4 · file hygiene · font governance)
> **หลักออกแบบ:** craft อยู่ที่ skill นี้ — ผู้ใช้ skill คือกัปตัน (build เอง) หรือโมโม่ (build เป็นชิ้นตาม brief) · ผู้ตรวจแยก context เสมอ (Producer ≠ Checker)

---

## §0 เข้าเงื่อนไขไหน — ROUTING GATE (อ่านก่อนทุกครั้ง)

| deliverable ที่ user ต้องการ | เส้นทาง |
|---|---|
| ไฟล์เอกสาร office (.pptx/.docx/.xlsx/PDF) — รวม "deck สำหรับเดโม" | **DOC-PIPELINE** (skill ice-doc-builder) — ไม่ใช่ skill นี้ |
| แอป/หน้าจอที่**รันได้จริง กดได้จริง** (เว็บ, NetSuite, APEX, mobile) | **DEMO-PIPELINE** (skill นี้) |
| **กำกวม** — เช่น "ทำ demo" ที่อาจหมายถึง deck ก็ได้ แอปก็ได้ | 🔴 **ถาม user ก่อน ห้ามเดา** (คำสั่ง user 2026.08.07) — คำถามเดียวสั้น ๆ: "ชิ้นงานที่ต้องการคือเอกสารนำเสนอ หรือแอปที่กดได้จริงครับ" |

**ที่เก็บงาน (file hygiene):** งานจริงทั้งหมด → `<opportunity>/50 - Demo/` (โฟลเดอร์มาตรฐานใหม่ ตัดสินโดย user 2026.08.07) · ไฟล์ temp/ทดลอง → `<opportunity>/20-Output/_temp/` ตามกติกาเดิม · 🔴 ห้ามสร้างไฟล์นอกโปรเจกต์

---

## §1 DEMO-PIPELINE — 6 ด่าน (เดินตามลำดับ ผ่านแล้วค่อยไปต่อ)

### DM-0 QUALIFY — คุ้มไหม ระดับไหน (ที่มา: RPI research gate — GO/NO-GO ก่อนลงแรง)
ตอบ 4 ข้อก่อนเริ่ม (ตอบไม่ได้ = ยังไม่พร้อม กลับไปคุยกับ user):
1. **เป้าหมายการขาย** — demo นี้ต้องทำให้อะไรเกิดขึ้นในดีล (ผ่าน gate ไหนของ MEDDPICC / โน้มน้าวใครให้ตัดสินใจอะไร)
2. **ผู้ชม** — CFO (ดูตัวเลข/ผลลัพธ์) · CIO/IT (ดูสถาปัตยกรรม/ความปลอดภัย) · ผู้ใช้งานจริง (ดูขั้นตอนงานประจำวัน) — ผู้ชมกำหนดว่าโชว์หน้าไหน ลึกแค่ไหน
3. **Pain ที่จะโชว์** — เลือก ≤3 pain ที่ demo ต้องตอบ (มากกว่านั้น = demo ยาว หลุดโฟกัส)
4. **GO/NO-GO + Tier** — เทียบตาราง §2 · ถ้า effort เกินมูลค่าดีล/เวลาที่มี = NO-GO แจ้ง user พร้อมทางเลือก (เช่น ใช้ deck + วิดีโอ screen-record แทน)

บทบาทร่วม (เมื่อเดินเป็น pipeline เต็ม): ② ยอดนักขาย = demo storyline ตามหลักการขาย · ③ เทพ = ยืนยันว่า product ทำได้จริงตามที่จะโชว์ (กัน overpromise — FACT gate)

### DM-1 SPEC — เก็บความต้องการแล้วเขียนลงดิสก์ (ที่มา: interview-me + idea-refine + spec-on-disk เดิม)
- **เก็บ requirement แบบถามทีละคำถาม** (H4) จนมั่นใจ แล้ว**รวบคำถามทั้งหมดถามชุดเดียวก่อนเริ่ม build** (ASK-FIRST — กำกวมกลางทาง = หยุดถาม ห้ามเดา)
- เขียน **`DEMO-SPEC.md` ลงดิสก์ก่อน build เสมอ** ที่ `50 - Demo/_build/DEMO-SPEC.md` — 3 ส่วน:
  1. **เรื่องเล่าการขาย** — ลำดับฉากของ demo (เปิดด้วย pain → โชว์ทางแก้ → ปิดด้วยผลลัพธ์ธุรกิจ) ผูกกับ pain ที่เลือกใน DM-0
  2. **หน้าจอ + สถานะ** — รายการหน้าจอ (screen inventory) · ต่อหน้าจอระบุ: ข้อมูลที่แสดง, ปุ่ม/การกระทำที่ต้องกดได้จริง, ปุ่มที่เป็นแค่ภาพ (ระบุชัดว่าอันไหนกดไม่ได้ — กันหน้าแตกกลางเดโม)
  3. **เทคนิค** — stack ที่เลือก (§3), ชุดข้อมูล+สถานะความยินยอม (§4), วิธีรัน
- **MVP scope + Not-Doing list** — เขียน "สิ่งที่ demo นี้**ไม่ทำ** เพราะอะไร" อย่างน้อย 3 ข้อ (กัน scope บานปลาย — demo ที่ดีคือ demo ที่ตัดเก่ง)

### DM-2 DESIGN — ระบบดีไซน์ก่อนโค้ด
- **Theme:** ค่าเริ่มต้น = iCE CI (`#1E66A4` primary · `#41A8B5` secondary · `#595959` text) · ถ้าโจทย์คือ "ให้เหมือนระบบของลูกค้า" → เก็บ design จริงด้วยเสี่ยวป้อ (skill copy-design → DESIGN.md) ห้ามเดา brand เอง
- **Font:** ตาม `_lib/font_policy.py` RAILS — เว็บใช้ IBM Plex Sans Thai Looped ได้ตรงจาก Google Fonts (ไทย=อังกฤษ ตระกูลเดียว) · ห้าม hard-code ชื่อฟอนต์อื่น
- **โหลด skill ประกอบ:** `frontend-design` (พื้นฐาน UI จริงจัง) · `ui-ux-pro-max` (งานที่ต้อง polish สูง) · Figma MCP เมื่อมีไฟล์ดีไซน์อยู่แล้ว (figma-design-to-code)
- **กติกาจาก frontend-ui-engineering (สกัด):** ทุกหน้าจอออกแบบครบ 4 สถานะ — loading / empty / error / success (demo ที่โชว์แต่ happy path จะแตกทันทีที่ลูกค้าขอกดเอง) · ใช้ component ซ้ำ ไม่สร้างใหม่ทุกหน้า · **ต้องไม่ดูเป็น "AI สร้าง"** — ห้าม purple gradient, ห้าม emoji เป็น icon, ห้าม metric ประดิษฐ์ (สอดคล้องด่าน visual anti-slop D7.S ของอริส)

### DM-3 BUILD — สร้างทีละชิ้นแนวตั้ง (ที่มา: incremental-implementation)
- **หั่นงานเป็น vertical slice** — 1 ชิ้น = 1 หน้าจอ/ฟีเจอร์ที่จบในตัว รันได้ ดูได้ (ไม่ใช่ "layer ทั้งระบบ") · เรียงชิ้นตามเรื่องเล่าการขาย: หน้าที่เปิดฉาก demo สร้างก่อน
- **ใครสร้าง:** งานเล็ก (≤2 หน้าจอ) → กัปตัน/L0 build เอง inline · งานหลายหน้าจอ/ขนานได้/context หนัก → **สั่งโมโม่ ⑦ เป็นชิ้น** — 1 brief = 1 ชิ้น พร้อม path DEMO-SPEC + ชิ้นที่รับผิดชอบ + output dir + budget
- **เพดานรอบแก้ ≤3 ต่อชิ้น** (ที่มา: loop-engineering Infinite Fix Loop) — แก้เกิน 3 รอบแล้วยังไม่ผ่าน = หยุด รายงานอาการ+สิ่งที่ลองแล้ว ให้ระดับบนตัดสิน (ห้าม debug วนเงียบ ๆ — บทเรียน TQR 155 รอบ)
- โค้ด/สคริปต์ build อยู่ `50 - Demo/_build/` ข้าง artifact (เอกสารประกอบงาน ไม่ใช่ temp)

### DM-4 VERIFY — ตรวจด้วยการรันจริงเท่านั้น (ที่มา: browser-testing + loop-engineering Verifier Theater)
- 🔴 **กติกาเหล็ก: ผู้ตรวจต้องรันแอปจริง ห้ามตรวจด้วยการอ่านโค้ดอย่างเดียว** — "Verifier Theater" (ตรวจแบบละคร) คือความล้มเหลวชนิดเดียวกับ validator ที่ขึ้น PASS ทั้งที่ฟอนต์ผิดทั้งไฟล์
- เว็บ → เปิดใน **Browser ในแอป** กดตามเรื่องเล่าการขายทีละฉาก + เก็บ **screenshot เป็นหลักฐาน** ลง `20-Output/_temp/qa/` · อ่าน console ต้องไม่มี error ค้าง
- Mobile → **iOS Simulator** แตะ/ปัด/พิมพ์ตามบท + screenshot
- ตรวจข้ามสถานะ: ลอง empty state (ข้อมูลว่าง) และ error state อย่างน้อย 1 จุด — ลูกค้าชอบกดของที่เราไม่ได้เตรียม
- **customer-facing → อริส ⑤ ตรวจใน context แยก** (visual anti-slop D7.S + ความถูกต้องข้อมูลเทียบ DEMO-SPEC) · ไฟล์โค้ดที่จะส่งมอบให้ลูกค้า → ผ่าน code-review/security-review ก่อน

### DM-5 REHEARSE — ซ้อมและเตรียมวันจริง
เขียน `50 - Demo/README.md` ให้คนที่ไม่ได้ build เปิด demo ได้เองใน 5 นาที:
1. **วิธีเปิด** — คำสั่ง start ครบทุกขั้น (server, URL, login ถ้ามี) ทดสอบจากเครื่องสะอาดในหัว: ถ้าพรุ่งนี้เช้าเปิดใหม่ ต้องกดอะไรบ้าง
2. **บทเดโม** — run-through script ตามเรื่องเล่าการขาย: ฉากไหนกดอะไร พูดประเด็นไหน + จุดที่**ห้ามกด** (ปุ่มที่เป็นภาพ)
3. **แผนสำรอง** — ถ้าแอปพัง/เน็ตล่มกลางเดโม ใช้อะไรแทน (ชุด screenshot ทุกหน้าจอที่เก็บจาก DM-4 = แผนสำรองฟรี เตรียมเป็น PDF ไว้เสมอ)
4. **ซ้อมจริง 1 รอบเต็ม** จับเวลา — demo ควรจบใน 15-20 นาที เกินนั้นตัดฉาก

---

## §2 ตาราง TIER — เลือกความลึกให้ตรง stage ของดีล

| Tier | คืออะไร | effort | เหมาะกับ stage | ข้อมูล (§4) |
|---|---|---|---|---|
| **T1 Mockup** | หน้า HTML นิ่ง/คลิกเบา 1-3 หน้า โชว์ concept | ชั่วโมง | First call / Discovery — ให้ลูกค้า "เห็นภาพ" | แปลงสมจริง |
| **T2 Prototype** | เว็บแอปกดได้จริง หลายหน้าจอ + ข้อมูลแปลง เดินเรื่องได้ครบ | วัน | Solution / Demo stage — พิสูจน์ workflow | แปลงสมจริง |
| **T3 Real-stack** | ระบบจริง: NetSuite sandbox (SuiteScript/SPA/SDF) หรือ APEX workspace | สัปดาห์ | POC / Validation — พิสูจน์ของจริง | จริงที่ลูกค้ายินยอม |

หลักเลือก: **เอา Tier ต่ำสุดที่ตอบเป้าหมายการขายได้** — T3 ที่ไม่จำเป็นคือการเผา effort ของทีมและเวลาของลูกค้า · ยกระดับ Tier เมื่อดีลลึกขึ้นเท่านั้น

---

## §3 STACK RECIPES

### NetSuite (skill ครบในเครื่อง)
- **หน้าจอ custom ใน NetSuite:** `netsuite-uif-spa-reference` (SPA) — demo ที่ดูเนียนเป็นส่วนหนึ่งของ product จริง
- **logic/ข้อมูล:** `netsuite-suitescript-records-reference` + `netsuite-suitescript-upgrade` · deploy ผ่าน `netsuite-sdf-project-documentation` / `netsuite-sdf-roles-and-permissions`
- **ความปลอดภัยก่อนส่งมอบ:** `netsuite-owasp-secure-coding`
- ใช้ **sandbox account เท่านั้น** — ห้ามแตะ production ของลูกค้าในงาน demo ทุกกรณี

### Oracle APEX
- Reference ในเครื่อง: `LLM-Memory/30-Product/Oracle-APEX/` (เอกสารทางการที่เสี่ยวป้อเก็บ พร้อม provenance) — อ่านก่อนเริ่มงาน APEX ทุกครั้ง
- จุดแข็งเชิง demo: low-code สร้างหน้า CRUD/dashboard จากตารางได้เร็วมาก — เหมาะ T3 ที่ต้องขึ้นของจริงไว
- ยังไม่มี skill development เฉพาะทาง — งานลึกเกิน reference ให้แจ้ง user ตรง ๆ ว่าส่วนไหนอิงเอกสาร ส่วนไหนอิงความรู้ทั่วไปของโมเดล (H3 — ติดป้ายให้เห็น)

### เว็บทั่วไป (T1/T2)
- **T1:** ไฟล์ HTML เดี่ยว + CSS ฝังใน (ไม่มี dependency — เปิดได้ทุกเครื่อง ส่งลูกค้าได้เป็นไฟล์เดียว)
- **T2:** Vite + React หรือ plain HTML+JS หลายหน้า · mock API ด้วย JSON ในเครื่อง — **ไม่ต่อ internet ระหว่างเดโม** (เน็ตห้องประชุมลูกค้า = ความเสี่ยงอันดับหนึ่ง ออกแบบให้ demo วิ่งได้ offline เสมอ)
- รันดู: `preview_start` → Browser ในแอป (dev server อยู่ในเครื่อง)

---

## §4 DEMO DATA POLICY — 3 ระดับ (คำสั่ง user 2026.08.07 — ไม่ใช่ mock ลอย ๆ)

| ระดับ | ใช้เมื่อ | กติกา |
|---|---|---|
| **ข้อมูลจริงของลูกค้า** | **POC (T3)** | ใช้ได้เฉพาะชุดที่ลูกค้า**ส่งมอบมาเพื่อการนี้และยินยอมให้แสดงแล้ว** · บันทึกใน DEMO-SPEC: ชุดไหน ได้รับความยินยอมเมื่อไร จากใคร · อยู่ในเครื่อง/ระบบที่ตกลงกันเท่านั้น |
| **ข้อมูลแปลงสมจริง** | **Demo ทั่วไป (T1/T2)** | แปลงจากข้อมูล/บริบทลูกค้าให้ใกล้เคียงของจริง — **ประเภทรายการเดียวกัน โครงธุรกิจ/อุตสาหกรรมเดียวกัน** ชื่อ-ตัวเลขถูก mask/scale · เป้าหมาย: ลูกค้าดูแล้ว "นี่มันงานของเรา" ไม่ใช่ตัวอย่างลอย ๆ · ระบุใน DEMO-SPEC ว่าแปลงจากชุดไหน วิธีอะไร (ตามรอยได้ — H3) |
| **ห้ามเสมอ** | ทุกกรณี | ❌ ประดิษฐ์ตัวเลข/ชื่อขึ้นเองแล้วอ้างว่าเป็นของจริง (H3) · ❌ เอาข้อมูลจริงที่ลูกค้า**ยังไม่ยินยอม**ขึ้นจอ · ❌ ส่งข้อมูลลูกค้าออกนอกเครื่อง — รวมการ publish Artifact — โดยไม่ขออนุญาต user รายครั้ง |

ข้อมูลแปลงที่ดี: ยอดขายจริง 4,213,567 บาท → 4.2 ล้าน "บริษัท สยามเทรดดิ้ง จำกัด (ตัวอย่าง)" · โครงสร้าง GL/BU/สาขา คงรูปเดิม · สัดส่วนตัวเลขสมเหตุผลทางบัญชี (เดบิต=เครดิต, AR aging รวมตรง) — ตัวเลขที่บวกไม่ลงตัวคือจุดที่ CFO จับได้ก่อนใคร

---

## §5 TOOL MAP — เครื่องมือในเครื่อง ใช้ตรงไหน

| ขั้น | เครื่องมือ |
|---|---|
| DESIGN (DM-2) | skill `frontend-design` · `ui-ux-pro-max` · `design:design-system` · Figma MCP (`figma-design-to-code`, `figma-generate-design`) · เสี่ยวป้อ `copy-design` (brand ลูกค้า) |
| BUILD (DM-3) | โค้ดตรง + skill stack ตาม §3 · Artifact เฉพาะข้อมูลแปลง/สมมติล้วน + แจ้ง user ก่อน (ออกนอกเครื่อง) |
| VERIFY (DM-4) | **Browser ในแอป** (`preview_start` → navigate → screenshot → read_console) · **iOS Simulator** (attach → tap/swipe → screenshot) · `code-review` / `security-review` ก่อนส่งมอบโค้ด |
| REHEARSE (DM-5) | screenshot ชุดจาก DM-4 → PDF แผนสำรอง (ผ่าน DOC-PIPELINE ถ้าจะทำเป็นเอกสารสวย) |

---

## §6 GUARDRAILS (สกัดจาก loop-engineering failure modes + กติกา fleet)

1. **เพดานรอบแก้ ≤3 ต่อชิ้น** — เกินแล้วหยุดรายงาน (กัน Infinite Fix Loop / token burn)
2. **ผู้ตรวจต้องรันจริง** — screenshot + console log คือหลักฐาน ไม่ใช่คำว่า "ตรวจแล้ว" (กัน Verifier Theater)
3. **ครบ = หยุด** — build ตาม DEMO-SPEC เท่านั้น ไอเดียเพิ่มระหว่างทาง → จดเสนอ user ไม่ทำเอง (กัน scope creep)
4. **ออกนอกเครื่อง = ขออนุญาตรายครั้ง** — Artifact, ส่ง repo, deploy ขึ้น cloud ใด ๆ · อนุมัติครั้งเดียว ≠ อนุมัติถาวร
5. **Human gate ก่อนวันจริง** — user ต้องเห็นและ walk through demo ก่อนใช้กับลูกค้าเสมอ (demo ที่ user ไม่เคยเห็น = ห้ามขึ้นจอลูกค้า)
6. **File hygiene** — จริง `50 - Demo/` · temp `20-Output/_temp/` · จบงาน `ls` ยืนยันไม่มีไฟล์หลง
7. **ห้าม build ไฟล์ office ด้วย skill นี้** — เอกสารเดิน DOC-PIPELINE ตามเดิม (hook ice-prebuild-guard คุมอยู่ — งานโค้ด html/js/ts ไม่ถูก block)

---

*Skill: ice-demo-builder **V01R01** | 2026.08.07 | ผู้ใช้: กัปตัน (inline) + demo-builder-agent โมโม่ ⑦ (เป็นชิ้น) | ตรวจ: อริส ⑤ (customer-facing) | ที่มา best practice: RPI gate + agent-skills craft + loop-engineering guardrails — เขียนเอง ไม่ clone*
