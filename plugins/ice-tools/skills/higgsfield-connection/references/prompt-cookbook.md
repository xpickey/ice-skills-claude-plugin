# Prompt Cookbook (ไทย-อังกฤษ)

คู่มือ prompt patterns สำหรับ Higgsfield AI generation suite (ผ่าน MCP, tool prefix = UUID เช่น `mcp__6473a427-...`) แยกตาม use-case ครอบคลุม image + video. ทุก pattern ใช้โครง 6 ส่วน + ตัวอย่าง prompt ไทย/อังกฤษ + model แนะนำ + aspect ratio.

> หมายเหตุก่อนใช้งานจริง — model list / feature / cost ที่ไม่แน่ใจให้ **เช็คด้วย `models_explore` / `balance` / `get_cost:true` (preflight)** เสมอ. ห้ามสมมติราคาหรือ feature เกินที่ระบุในไฟล์นี้.

---

## Table of Contents

- [โครง 6 ส่วน (6-Part Prompt Skeleton)](#โครง-6-ส่วน-6-part-prompt-skeleton)
- [วิธีใช้ Cookbook นี้](#วิธีใช้-cookbook-นี้)
- [ตารางสรุป Pattern → Model → Aspect](#ตารางสรุป-pattern--model--aspect)
- **IMAGE patterns**
  - [P1 — Hero / Banner Image](#p1--hero--banner-image)
  - [P2 — Product Shot (สินค้าชิ้นเดียว)](#p2--product-shot-สินค้าชิ้นเดียว)
  - [P3 — Portrait / People (Soul ID)](#p3--portrait--people-soul-id)
  - [P4 — Diagram / 4K-Text Graphic](#p4--diagram--4k-text-graphic-nano_banana_pro)
  - [P5 — Lifestyle / Scene Composition](#p5--lifestyle--scene-composition)
- **VIDEO patterns**
  - [P6 — Brand Video (Marketing Studio)](#p6--brand-video-marketing-studio)
  - [P7 — UGC Ad (User-Generated-Style)](#p7--ugc-ad-user-generated-style)
  - [P8 — Product Demo Video](#p8--product-demo-video)
  - [P9 — Motion / Cinematic Video](#p9--motion--cinematic-video)
  - [P10 — Talking Avatar / Spokesperson](#p10--talking-avatar--spokesperson)
- [Negative Prompt & Modifier Bank](#negative-prompt--modifier-bank)
- [Post-Generation Workflow (enhance)](#post-generation-workflow-enhance)

---

## โครง 6 ส่วน (6-Part Prompt Skeleton)

ทุก prompt ที่ดีในคู่มือนี้ประกอบจาก 6 ส่วน เรียงตามลำดับนี้ (เรียงจากสำคัญ→รายละเอียด):

| # | ส่วน | ตอบคำถาม | ตัวอย่างคำ |
|---|------|----------|-----------|
| 1 | **Subject** | อะไร/ใครคือพระเอกของภาพ | "ขวดเซรั่มแก้วใส", "หญิงสาวไทยวัย 30" |
| 2 | **Action** | กำลังทำอะไร / ท่าทาง | "ถือสินค้ายิ้ม", "หยดน้ำกระเด็น", "หมุนช้า ๆ" |
| 3 | **Setting** | ฉาก/พื้นหลัง/บริบท | "โต๊ะหินอ่อน", "คาเฟ่มินิมอล", "พื้นหลังไล่เฉดสีพีช" |
| 4 | **Style** | สไตล์ภาพ/อารมณ์/genre | "minimalist luxury", "cinematic", "flat vector" |
| 5 | **Lighting** | แสง/โทน/เวลา | "soft diffused light", "golden hour", "studio softbox" |
| 6 | **Technical** | กล้อง/เลนส์/ความละเอียด/มุม | "85mm shallow DOF", "top-down", "4K, sharp" |

**สูตรกลาง:** `[Subject] + [Action] + [Setting], [Style], [Lighting], [Technical]`

> เคล็ดลับ: เขียน prompt ภาษาอังกฤษให้ engine (ผลลัพธ์มักนิ่งกว่า) แต่คุยกับผู้ใช้เป็นไทย. ถ้าผู้ใช้ให้ brief ไทยมา ให้แปล intent เป็นโครง 6 ส่วนก่อนยิง.

---

## วิธีใช้ Cookbook นี้

1. เลือก pattern ตาม use-case (ดูตารางสรุปด้านล่าง).
2. เติมโครง 6 ส่วนด้วยข้อมูลจริงของงาน.
3. **`get_cost:true` preflight** ก่อน generate จริงทุกครั้ง — ดู credit ที่ `balance`. ถ้าเครดิตหมด → `show_plans_and_credits(intent=topup/upgrade/auto_refill)`.
4. งาน video / upscale / virality / video_analysis เป็น **async** → ได้ `job_id` แล้ว poll สถานะ (video ~3-5 นาที).
5. media ที่อ้างใน prompt: ใช้ `media_upload_widget` (ไฟล์ local) หรือ `media_import_url` (URL → media_id) — ใน `medias[].value` ต้องเป็น `media_id`/`job_id` **ห้ามใส่ URL ดิบ**.
6. People/หน้าซ้ำคนเดิม → ฝึก Soul ID ก่อน (`show_characters(action=train)`, 5-20 รูป, ~10 นาที) — **ถามผู้ใช้ก่อนเสมอ**.

---

## ตารางสรุป Pattern → Model → Aspect

| Pattern | ประเภท | Model แนะนำ | Aspect ratio ที่นิยม |
|---------|--------|-------------|---------------------|
| P1 Hero / Banner | image | `marketing_studio_image` / `nano_banana_pro` | 16:9, 21:9 (เว็บ), 1:1 |
| P2 Product Shot | image | `marketing_studio_image` / `soul_2` | 1:1, 4:5 (IG), 3:4 |
| P3 Portrait / People | image | `soul_2` + Soul ID (`soul_cast`) | 4:5, 3:4, 1:1 |
| P4 Diagram / 4K-Text | image | `nano_banana_pro` | 16:9, 1:1, 4:3 |
| P5 Lifestyle / Scene | image | `marketing_studio_image` / `nano_banana_pro` | 4:5, 16:9 |
| P6 Brand Video | video | `marketing_studio_video` | 16:9, 9:16 |
| P7 UGC Ad | video | `marketing_studio_video` (+ preset) | 9:16 (Reels/TikTok) |
| P8 Product Demo | video | `seedance_2_0` / `kling3_0` | 9:16, 1:1, 16:9 |
| P9 Motion / Cinematic | video | `veo` / `kling3_0` / `seedance_2_0` | 16:9, 21:9, 9:16 |
| P10 Talking Avatar | video | `marketing_studio_video` (avatar) + `inworld_text_to_speech` | 9:16, 1:1 |

> model/aspect ที่ engine รองรับจริงในวันใช้งาน — **เช็คด้วย `models_explore`** (รายการอาจเปลี่ยน). audio ที่อ้างถึง: `sonilo_music` (เพลง), `mirelo_text_to_audio` (SFX/ambient), `inworld_text_to_speech` (เสียงพูด).

---

## IMAGE patterns

### P1 — Hero / Banner Image

ภาพหัวเว็บ/แบนเนอร์แคมเปญ พื้นที่กว้าง มีที่ว่างสำหรับวาง headline.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | สินค้า/คอนเซ็ปต์หลักวางเยื้องด้านหนึ่ง เว้น negative space อีกด้านไว้วางข้อความ |
| Action | นิ่ง สง่า หรือลอยเบา ๆ (floating) |
| Setting | พื้นหลังไล่เฉด/พื้นผิวเรียบ ไม่รก |
| Style | clean, premium, brand-aligned |
| Lighting | soft gradient light, rim light เน้นขอบ subject |
| Technical | wide composition, copy space, 4K |

**TH:**
```
ขวดน้ำหอมแก้วใสวางเยื้องขวา ลอยนิ่งเหนือพื้นผิวสะท้อนเงา พื้นหลังไล่เฉดสีพีชอบอุ่น เว้นพื้นที่ว่างด้านซ้ายสำหรับวางข้อความ สไตล์ luxury minimalist แสงนุ่มไล่เฉดมี rim light เน้นขอบขวด องค์ประกอบแนวนอนกว้าง คมชัด 4K
```
**EN:**
```
A clear glass perfume bottle positioned to the right, floating still above a reflective surface, warm peach gradient background, generous empty negative space on the left for headline text, luxury minimalist style, soft gradient lighting with subtle rim light on the bottle edges, wide horizontal composition, copy space, sharp 4K.
```
- **Model:** `marketing_studio_image` (brand-aligned) หรือ `nano_banana_pro` (ถ้าต้องการความคม/ข้อความในภาพ)
- **Aspect:** 16:9 หรือ 21:9 (hero เว็บ), 1:1 (social)

---

### P2 — Product Shot (สินค้าชิ้นเดียว)

ภาพสินค้าโฟกัสเดี่ยว สไตล์ e-commerce / catalog. ใช้คู่กับ Marketing Studio `type=product`.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | สินค้าชิ้นเดียว เต็มเฟรม รายละเอียดวัสดุชัด |
| Action | นิ่ง วางตั้ง/วางนอน หรือมี element เคลื่อนไหวรอบ (หยดน้ำ/ผง) |
| Setting | พื้นหลังเรียบ/พื้นผิวธรรมชาติ (หิน ไม้ ผ้า) |
| Style | studio product photography, hi-fidelity |
| Lighting | studio softbox, สะท้อนวัสดุสมจริง |
| Technical | 85mm macro feel, shallow DOF, top-down หรือ 45° |

**TH:**
```
กระปุกครีมบำรุงผิวสีขาวมุก ฝาทองเงา วางตั้งกลางเฟรมบนแผ่นหินอ่อนสีเทาอ่อน มีหยดน้ำเกาะผิวกระปุกเล็กน้อย สไตล์ถ่ายภาพสินค้าในสตูดิโอ ความสมจริงสูง แสง softbox นุ่มสะท้อนผิวกระปุกสวย มุมเฉียง 45 องศา ระยะชัดตื้น คมชัด 4K
```
**EN:**
```
A pearl-white skincare jar with a glossy gold lid, standing centered on a light grey marble slab, fine water droplets on the jar surface, studio product photography style, high fidelity, soft softbox lighting reflecting cleanly off the surface, 45-degree angle, shallow depth of field, sharp 4K.
```
- **Model:** `marketing_studio_image` (เข้ากับ brand kit) หรือ `soul_2`
- **Aspect:** 1:1, 4:5 (IG), 3:4
- **Tip:** สร้าง product asset ก่อนผ่าน `show_marketing_studio(action=create, type=product)` แล้วอ้างใน generation.

---

### P3 — Portrait / People (Soul ID)

ภาพคน/พรีเซนเตอร์ ต้องการความสม่ำเสมอของใบหน้าข้ามภาพ → ใช้ **Soul ID**.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | บุคคล (ระบุเพศ/อายุโดยประมาณ/ลุค) — ถ้ามี Soul ID ให้อ้าง character |
| Action | สีหน้า/ท่าทาง/การจัดมือ |
| Setting | ฉากหลังที่เข้ากับ brand/mood |
| Style | editorial / lifestyle / corporate headshot |
| Lighting | soft key light, catchlight ในตา |
| Technical | 85mm portrait, shallow DOF, eye-level |

**TH:**
```
หญิงสาวไทยวัยประมาณ 30 ปี ผมยาวสีน้ำตาลเข้ม ยิ้มอบอุ่นมองกล้อง สวมเสื้อเชิ้ตลินินสีครีม ยืนในคาเฟ่มินิมอลโทนอุ่น สไตล์ภาพ lifestyle editorial แสง key นุ่มจากหน้าต่างด้านข้าง มี catchlight ในดวงตา เลนส์พอร์เทรต 85mm ระยะชัดตื้น ระดับสายตา คมชัด
```
**EN:**
```
A Thai woman around 30, long dark-brown hair, warm genuine smile looking at camera, wearing a cream linen shirt, standing in a warm-toned minimalist cafe, lifestyle editorial style, soft side window key light with catchlight in the eyes, 85mm portrait lens, shallow depth of field, eye-level, sharp.
```
- **Model:** `soul_2` (general portrait) + Soul ID; `soul_cast` สำหรับงานที่ต้อง cast/หน้าซ้ำเดิม
- **Aspect:** 4:5, 3:4, 1:1
- **Soul ID:** `show_characters(action=train)` ใช้รูป 5-20 รูป ~10 นาที — **ถามผู้ใช้ก่อนเทรนเสมอ** (ใช้เครดิต + เวลา).

---

### P4 — Diagram / 4K-Text Graphic (`nano_banana_pro`)

ภาพที่มี **ข้อความ/ตัวเลข/ผังในภาพ** เช่น infographic, diagram, slide visual. `nano_banana_pro` เด่นเรื่อง text rendering คม + 4K.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | ผัง/แผนภาพ/การ์ดข้อมูล — ระบุข้อความที่ต้องการให้ปรากฏแบบ exact |
| Action | (มักนิ่ง) layout ของ element |
| Setting | พื้นหลังเรียบ/grid |
| Style | flat vector / clean infographic / isometric |
| Lighting | flat even (กราฟิก) |
| Technical | sharp typography, high contrast, 4K, legible text |

**TH:**
```
อินโฟกราฟิกแนวนอน flat vector แสดง 3 ขั้นตอน เรียงซ้ายไปขวา การ์ด 3 ใบมีไอคอนวงกลมด้านบน หัวข้อข้อความว่า "Discover", "Design", "Deliver" ชัดเจน พื้นหลังสีขาวมี grid จาง ๆ โทนสีน้ำเงิน-เขียวมินต์ สไตล์สะอาดทางธุรกิจ แสงเรียบสม่ำเสมอ ตัวอักษรคมอ่านง่าย ความละเอียดสูง 4K
```
**EN:**
```
A horizontal flat-vector infographic showing 3 steps left to right, three cards each with a circular icon on top, clear legible headings reading exactly "Discover", "Design", "Deliver", white background with a faint grid, blue and mint-green palette, clean business style, flat even lighting, crisp readable typography, high resolution 4K.
```
- **Model:** `nano_banana_pro` (เลือกตัวนี้เมื่อ "ต้องมีตัวอักษรในภาพ" หรืองาน slide/diagram)
- **Aspect:** 16:9 (slide), 1:1, 4:3
- **Tip:** ใส่ข้อความที่ต้องการในเครื่องหมายคำพูดและสั่ง "exact text" เพื่อให้ render ตรง. ถ้า text ยาว/ภาษาไทยซับซ้อน ตรวจผลลัพธ์ทุกครั้ง.

---

### P5 — Lifestyle / Scene Composition

สินค้า/บุคคลในบริบทการใช้งานจริง (in-context) สำหรับ social/campaign.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | สินค้า + บริบทคน/มือ/สภาพแวดล้อม |
| Action | กำลังใช้งาน/ถือ/วางในชีวิตประจำวัน |
| Setting | ฉากจริง (โต๊ะอาหารเช้า โต๊ะทำงาน สวน) |
| Style | natural lifestyle, authentic |
| Lighting | natural daylight, golden hour |
| Technical | 35-50mm, medium DOF, eye-level |

**TH:**
```
แก้วกาแฟลาเต้วางบนโต๊ะไม้ข้างโน้ตบุ๊ก มือคนถือกำลังจะหยิบแก้ว ฉากมุมทำงานที่บ้านโทนอุ่น มีต้นไม้เล็ก ๆ สไตล์ lifestyle เป็นธรรมชาติ แสงธรรมชาติช่วงเช้าจากหน้าต่าง เลนส์ 35mm ระยะชัดปานกลาง ระดับสายตา
```
**EN:**
```
A latte coffee cup on a wooden desk beside a laptop, a hand reaching to pick it up, cozy warm-toned home workspace with a small plant, natural lifestyle style, soft morning daylight from a window, 35mm lens, medium depth of field, eye-level.
```
- **Model:** `marketing_studio_image` หรือ `nano_banana_pro`
- **Aspect:** 4:5 (social), 16:9

---

## VIDEO patterns

> video เป็น **async**: ยิงแล้วได้ `job_id` → poll (ปกติ ~3-5 นาที). `get_cost:true` preflight ก่อนเสมอ.

### P6 — Brand Video (Marketing Studio)

วิดีโอแบรนด์สั้น เน้นความสอดคล้องกับ brand kit. ใช้ `show_marketing_studio` สร้าง brand_kit จาก `scrap_url` ก่อนได้.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | logo/สินค้า/คอนเซ็ปต์แบรนด์ |
| Action | การเคลื่อนกล้อง/transition ที่ smooth |
| Setting | ฉากที่ตรง brand mood |
| Style | premium brand film, ตาม brand palette |
| Lighting | cinematic soft, สอดคล้องโทนแบรนด์ |
| Technical | smooth camera move, stable, 16:9 หรือ 9:16 |

**TH:**
```
วิดีโอแบรนด์สั้น เปิดด้วยโลโก้แบรนด์ค่อย ๆ ปรากฏบนพื้นหลังไล่เฉดสีแบรนด์ กล้องเคลื่อนเข้าหา (slow push-in) ตัดสู่ภาพสินค้าหมุนช้า ๆ โทนภาพพรีเมียมตาม brand palette แสงนุ่มแบบภาพยนตร์ การเคลื่อนกล้องนุ่มนิ่ง อัตราส่วน 16:9
```
**EN:**
```
A short brand video opening with the brand logo gently fading in over a branded gradient background, slow camera push-in, cut to the product rotating slowly, premium look matching the brand palette, soft cinematic lighting, smooth stable camera movement, 16:9.
```
- **Model:** `marketing_studio_video`
- **Aspect:** 16:9 (YouTube/เว็บ), 9:16 (Stories)
- **Tip:** `show_marketing_studio(action=create, type=brand_kit)` จาก `scrap_url` เพื่อดึงสี/โลโก้แบรนด์อัตโนมัติก่อน.

---

### P7 — UGC Ad (User-Generated-Style)

โฆษณาสไตล์คนทั่วไปถ่ายเอง (authentic, ดูไม่เป็นโฆษณา) สำหรับ TikTok/Reels. ใช้ preset ของ Marketing Studio.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | คนถือ/รีวิวสินค้าแบบเป็นกันเอง |
| Action | พูดเข้ากล้อง/โชว์สินค้า/unboxing |
| Setting | ห้อง/บ้านจริง ดูไม่จัดฉาก |
| Style | UGC, handheld, authentic, casual |
| Lighting | natural indoor, ดูจริง |
| Technical | vertical 9:16, handheld feel, eye-level selfie |

**TH:**
```
วิดีโอสไตล์ UGC แนวตั้ง หญิงสาวถือสินค้าพูดเข้ากล้องแบบเป็นกันเองเหมือนถ่ายเซลฟี่รีวิว ฉากห้องนอนจริงดูไม่จัดฉาก กล้องสั่นมือเล็กน้อยให้ดูเป็นธรรมชาติ แสงในห้องตามจริง อัตราส่วน 9:16 ระดับสายตา
```
**EN:**
```
A vertical UGC-style video, a young woman holding the product talking to camera casually like a selfie review, real bedroom setting that looks unstaged, slight handheld camera shake for authenticity, natural indoor lighting, 9:16, eye-level selfie angle.
```
- **Model:** `marketing_studio_video` (+ preset)
- **Aspect:** 9:16
- **Preset:** ดูตัวเลือกผ่าน `presets_show` / `show_marketing_studio(action=presets)` — มี UGC / Tutorial / Unboxing / Product-Review (hooks + settings).

---

### P8 — Product Demo Video

โชว์สินค้าหมุน/ฟังก์ชัน/ก่อน-หลัง เน้นรายละเอียดสินค้า.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | สินค้า (อ้างจากภาพ product shot เป็น start frame ได้) |
| Action | หมุน 360°, ซูมรายละเอียด, เปิด/ปิดฝา |
| Setting | สตูดิโอเรียบ / พื้นผิวเด่นสินค้า |
| Style | clean product demo, hi-fidelity |
| Lighting | studio softbox สม่ำเสมอ |
| Technical | smooth orbit, stable, ตาม platform aspect |

**TH:**
```
วิดีโอเดโมสินค้า กระปุกครีมหมุนรอบตัวช้า ๆ 360 องศา บนแท่นหมุนพื้นหลังเรียบสีเทาอ่อน กล้องค่อย ๆ ซูมเข้าหารายละเอียดฝาทอง สไตล์เดโมสะอาดสมจริง แสง softbox สม่ำเสมอ การเคลื่อนนุ่มนิ่ง อัตราส่วน 1:1
```
**EN:**
```
A product demo video, the skincare jar rotating slowly 360 degrees on a turntable against a clean light-grey background, camera slowly zooming into the gold lid detail, clean high-fidelity demo style, even softbox lighting, smooth stable motion, 1:1.
```
- **Model:** `seedance_2_0` หรือ `kling3_0`
- **Aspect:** 9:16, 1:1, 16:9
- **Tip:** อัป product shot เป็น start image (`media_import_url`/`media_upload_widget` → ใส่ `media_id` ใน `medias[].value`) เพื่อให้สินค้าตรงของจริง.

---

### P9 — Motion / Cinematic Video

ช็อตภาพยนตร์ มีการเคลื่อนกล้อง/อารมณ์ เน้น mood + dynamic motion.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | ตัวละคร/ฉาก/วัตถุหลัก |
| Action | การเคลื่อนไหวเด่น (เดิน หันหน้า น้ำไหล) + camera move |
| Setting | สภาพแวดล้อม cinematic |
| Style | cinematic, film grain, color grade |
| Lighting | dramatic / golden hour / volumetric |
| Technical | dolly/crane/tracking shot, anamorphic feel, 24fps look |

**TH:**
```
ช็อตภาพยนตร์ หญิงสาวเดินช้า ๆ ผ่านถนนในเมืองยามค่ำ ไฟนีออนสะท้อนบนพื้นเปียกฝน กล้องแทร็กตามด้านข้าง (tracking shot) โทนภาพยนตร์มี color grade เย็น แสงดราม่าจากป้ายนีออน ฟิล์มเกรนบาง ๆ ฟีลเลนส์ anamorphic อัตราส่วน 21:9
```
**EN:**
```
A cinematic shot, a woman walking slowly through a city street at night, neon lights reflecting on wet pavement, side tracking shot, cinematic cool color grade, dramatic neon lighting, subtle film grain, anamorphic lens feel, 21:9.
```
- **Model:** `veo` / `kling3_0` / `seedance_2_0` (เลือกตาม motion ที่ต้องการ — **เช็คความสามารถจริงด้วย `models_explore`**)
- **Aspect:** 16:9, 21:9, 9:16
- **Tip:** เพิ่มเพลงด้วย `sonilo_music` หรือ ambient/SFX ด้วย `mirelo_text_to_audio` ในขั้น post.

---

### P10 — Talking Avatar / Spokesperson

อวตาร/พรีเซนเตอร์พูดสคริปต์ (lip-sync) สำหรับวิดีโอแนะนำ/ประกาศ.

| ส่วน | เนื้อหา |
|------|---------|
| Subject | avatar/พรีเซนเตอร์ (อ้าง avatar จาก Marketing Studio) |
| Action | พูดสคริปต์ ท่าทางสุภาพ มือประกอบเล็กน้อย |
| Setting | ฉากออฟฟิศ/สตูดิโอเรียบ |
| Style | corporate spokesperson, clean |
| Lighting | soft key + fill สม่ำเสมอ |
| Technical | medium close-up, eye-level, 9:16 หรือ 1:1 |

**TH:**
```
อวตารพรีเซนเตอร์ชายพูดเข้ากล้องตามสคริปต์ ท่าทางสุภาพมือประกอบเบา ๆ ฉากออฟฟิศมินิมอลเบลอด้านหลัง สไตล์พรีเซนเตอร์องค์กรสะอาด แสง key นุ่มมี fill สม่ำเสมอ ภาพระยะใกล้ปานกลาง ระดับสายตา อัตราส่วน 9:16
```
**EN:**
```
A male spokesperson avatar talking to camera following a script, polite posture with subtle hand gestures, minimalist office background blurred, clean corporate spokesperson style, soft key light with even fill, medium close-up, eye-level, 9:16.
```
- **Model:** `marketing_studio_video` (avatar) + เสียงพูดจาก `inworld_text_to_speech`
- **Aspect:** 9:16, 1:1
- **Tip:** สร้าง avatar ก่อนผ่าน `show_marketing_studio(action=create, type=avatar)` แล้วป้อนสคริปต์ + เสียง.

---

## Negative Prompt & Modifier Bank

ถ้า model รองรับ negative prompt (เช็คด้วย `models_explore`) ใช้คำเหล่านี้ตัดปัญหาที่พบบ่อย:

**Negative (สิ่งที่ไม่อยากได้):**
```
blurry, low resolution, distorted, deformed hands, extra fingers, text artifacts, watermark, logo overlay, oversaturated, plastic look, harsh shadows, cluttered background, duplicate object
```

**Quality modifiers (เติมท้ายเพื่อยกคุณภาพ):**

| เป้าหมาย | คำที่ใช้ |
|----------|---------|
| ความคม | `sharp focus, high detail, 4K, crisp` |
| ความสมจริง | `photorealistic, hyper-realistic, natural skin texture` |
| โทนพรีเมียม | `premium, luxury, editorial, high-end` |
| แสง | `soft diffused light, rim light, golden hour, studio softbox` |
| กล้อง | `85mm, shallow depth of field, bokeh, eye-level` / `top-down` / `45-degree angle` |
| กราฟิก | `flat vector, clean lines, high contrast, legible text` |

---

## Post-Generation Workflow (enhance)

หลังได้ผลลัพธ์แล้ว ปรับแต่งต่อด้วย tool เหล่านี้ (ทั้งหมด preflight `get_cost:true` ก่อน):

| ต้องการ | Tool | หมายเหตุ |
|---------|------|----------|
| ขยายความละเอียดวิดีโอ | `upscale_video` | **bytedance** ต้องระบุ `width`/`height`/`fps`; **topaz** ใช้ aspect-ratio |
| ขยายความละเอียดภาพ | `upscale_image` | — |
| ลบพื้นหลัง | `remove_background` | สำหรับ product cut-out |
| ขยายเฟรม (เติมขอบภาพ) | `outpaint_image` | เพิ่ม negative space ให้ banner |
| เปลี่ยน aspect ratio | `reframe` | แปลง 16:9 → 9:16 ฯลฯ |
| ทำนาย viral score | `virality_predictor` | async (job → poll) |
| วิเคราะห์วิดีโอ | `video_analysis` (`_create`/`_status`/`_jobs`) | async (job → poll) |

**ลำดับงานทั่วไป:**
1. preflight `get_cost:true` + เช็ค `balance`
2. (ถ้า people) เทรน Soul ID — ถามผู้ใช้ก่อน
3. generate image/video (video = async, poll `job_id`)
4. enhance: upscale / remove_background / outpaint / reframe ตามต้องการ
5. (video ad) `virality_predictor` / `video_analysis` เพื่อประเมินก่อนเผยแพร่

> เครดิตหมดระหว่างทาง → `show_plans_and_credits(intent=topup/upgrade/auto_refill)`. รายการ model/feature ที่ไม่แน่ใจ — **เช็คด้วย `models_explore` / `balance` / `get_cost`** เสมอ ห้าม fabricate.
