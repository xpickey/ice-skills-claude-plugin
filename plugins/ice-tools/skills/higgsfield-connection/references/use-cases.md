# Higgsfield — End-to-End Use Cases (iCE / Business)

> recipe ครบขั้นสำหรับงานจริง iCE/business — แต่ละ recipe = **เป้าหมาย → model → ขั้นตอน (pre-flight → cost → generate → poll → deliver) → insert เข้า deck/deliverable**.
> เชื่อมกับ skill `b2b-presentation-creator` (hero/AI imagery ในสไลด์) + agent `deliverable-gen-agent` (เจนนี่ build .pptx/.docx).
>
> **กฎร่วมทุก recipe:**
> - tool prefix เป็น **UUID** (เช่น `mcp__6473a427-...__`) — ตรวจ session จริงว่า prefix ปัจจุบันคืออะไร แล้วเรียก tool ตามชื่อหลัง prefix. ด้านล่างเขียนชื่อ tool ไม่รวม prefix.
> - **credit-based** — ตั้ง `get_cost: true` preflight ทุกงานแพง (video/marketing/upscale). credit ไม่พอ → `show_plans_and_credits(intent='topup')`. ดู balance → `balance`.
> - async (video/upscale/virality/video_analysis) คืน **job** → ต้อง poll status จน completed — อย่ารอ block, แจ้งผู้ใช้ว่ากำลังประมวลผล.
> - `medias[].value` = **media_id / job_id เท่านั้น** — ห้าม URL ดิบ. local → `media_upload_widget`; URL → `media_import_url`.
> - model/constraint ไม่แน่ใจ → **เช็คด้วย `models_explore(action='get', model_id=...)` / `balance` / `get_cost`** ก่อนสั่ง.

## สารบัญ
1. [Hero image สำหรับสไลด์ proposal](#1-hero-image-สำหรับสไลด์-proposal)
2. [Brand / Product video สั้นสำหรับ pitch](#2-brand--product-video-สั้นสำหรับ-pitch)
3. [Consistent character / avatar ข้ามหลายภาพ (Soul ID)](#3-consistent-character--avatar-ข้ามหลายภาพ-soul-id)
4. [DTC product ad จากเว็บลูกค้า](#4-dtc-product-ad-จากเว็บลูกค้า)
5. [Upscale ภาพเก่าใน deck](#5-upscale-ภาพเก่าใน-deck)
6. [Virality check ก่อนโพสต์วิดีโอ](#6-virality-check-ก่อนโพสต์วิดีโอ)
- [ตารางสรุป: Recipe → Model → Insert target](#ตารางสรุป-recipe--model--insert-target)
- [Insert เข้า deck/deliverable — pattern กลาง](#insert-เข้า-deckdeliverable--pattern-กลาง)

---

## 1. Hero image สำหรับสไลด์ proposal

**เป้าหมาย:** ภาพหน้าปก/หัวข้อ (title slide, section divider, banner) คุณภาพสูง สำหรับ deck เสนอลูกค้า.

**Model:** `nano_banana_pro` (4K + text ในภาพคมที่สุด — เหมาะถ้าต้องมีคำบนภาพ) หรือ `marketing_studio_image` (วาง concept commercial/clean). ภาพไม่มีคน sync, one-off → 2 ตัวนี้พอ.

**ขั้นตอน:**
1. **Pre-flight** — เช็ค MCP เชื่อม (`generate_image` ปรากฏ) + `balance` (credit พอ). กำหนด aspect_ratio ตาม layout สไลด์ (16:9 full-bleed / 4:3 / 1:1 spot).
2. **Cost** — `generate_image(model='nano_banana_pro', prompt='...', aspect_ratio='16:9', get_cost: true)` → ดูราคา.
3. **Generate** —
   ```text
   generate_image(
     model     = 'nano_banana_pro',
     prompt    = '<theme ภาพ: เช่น abstract enterprise data-flow, blue/teal corporate palette, clean negative space ด้านขวาไว้วางหัวข้อ>',
     aspect_ratio = '16:9',
     count     = 2          # ทำ 2 variant ให้เลือก
   )
   ```
   image gen เร็ว (sync) — ได้ผลทันที. หลีกเลี่ยงข้อความไทยยาวในภาพ (เสี่ยง render เพี้ยน) — ใส่หัวข้อจริงทับใน PowerPoint แทน.
4. **Poll** — image sync, ไม่ต้อง poll. ดูผล `show_generations` ถ้าต้องเรียกย้อน.
5. **Deliver** — เลือก variant ที่ดี → ถ้าความละเอียดไม่พอ full-bleed → `upscale_image` (ดู Recipe 5).

**Insert เข้า deck:** ดาวน์โหลดไฟล์ → วางเป็น background/spot image ของ title หรือ section slide. ผ่าน `deliverable-gen-agent` (เจนนี่) ใช้ `insert_image` ของ PowerPoint MCP. เว้น negative space ใน prompt เพื่อให้มีที่วาง headline + โลโก้ลูกค้า.

---

## 2. Brand / Product video สั้นสำหรับ pitch

**เป้าหมาย:** วิดีโอสั้น 5–10 วินาที (intro deck, product teaser, opening loop ใน pitch) — เปิดประชุม/ฝังในสไลด์.

**Model:** `marketing_studio_video` (default งานขาย/ads) · `kling3_0` (multi-shot / motion / audio) · `seedance_2_0` (ถ้าต้องคงหน้าคน/แบรนด์ในวิดีโอ). ไม่ชัด → `models_explore(action='recommend', query='short brand teaser', type='video')`.

**ขั้นตอน:**
1. **Pre-flight** — เช็ค MCP + `balance`. video แพงกว่าภาพมาก — ยืนยัน budget ก่อน. ถ้าจะ animate จากภาพนิ่ง (เช่น hero จาก Recipe 1) → upload ภาพ start ก่อน: `media_import_url` (URL) หรือ `media_upload_widget` (local) → ได้ `media_id`.
2. **Cost** — `generate_video(..., get_cost: true)` **เสมอ** (video = ของแพงสุด).
3. **Generate** —
   ```text
   generate_video(
     model     = 'marketing_studio_video',
     prompt    = '<การเคลื่อนไหว: เช่น slow cinematic push-in, product rotating, light sweep, corporate>',
     aspect_ratio = '16:9',
     duration  = 5,                       # ไม่ระบุ → model default
     medias    = [{ value: '<media_id ภาพ start>', role: 'start_image' }]   # ถ้า animate จากภาพ
   )
   ```
   roles ต่างตาม model (`start_image` / `end_image` / `image`) — เช็ค `models_explore(action='get', model_id='...')`.
4. **Poll** — **async**: คืน job. video ใช้เวลา ~3–5 นาที. poll status จน `completed`. ระหว่างรอแจ้งผู้ใช้ว่ากำลัง render. ดูผล `job_display(<job_id>)`.
5. **Deliver** — ได้ video media. ถ้าต้องการคมขึ้น → `upscale_video` (bytedance ต้อง width/height + fps 24/30/60 · topaz aspect-ratio). ก่อนโพสต์ social → ส่งต่อ Recipe 6 (virality check).

**Insert เข้า deck:** ดาวน์โหลด .mp4 → ฝังเป็น media ในสไลด์เปิด pitch (PowerPoint insert video) หรือใช้เป็น loop หน้าปก. แนบลิงก์/ไฟล์ใน deliverable. PowerPoint MCP ปัจจุบันเน้นภาพ — สำหรับ video ส่งไฟล์ให้ผู้ใช้วางเองในสไลด์ + ระบุ slide ที่ตั้งใจวาง.

---

## 3. Consistent character / avatar ข้ามหลายภาพ (Soul ID)

**เป้าหมาย:** ตัวละคร/พรีเซนเตอร์/avatar หน้าตา **คงเส้นคงวา** ใช้ซ้ำหลายสไลด์/หลาย scene (เช่น persona ใน customer-journey, mascot แบรนด์, presenter เดียวทั้ง deck).

**Model:** `soul_2` + `soul_id` (ต้อง train Soul ID ก่อน) · ถ้าไม่ต้อง train และยอมรับหน้าใกล้เคียง one-off → `soul_cast` (text-only character) หรือ `nano_banana_pro` (one-off char ref).

**ขั้นตอน:**
1. **Pre-flight + ถามผู้ใช้ก่อน** — Soul ID train ใช้ **5–20 รูป** ของ subject เดียวกัน + เวลา **~10 นาที** + **เสียเครดิต** → **ต้องถามผู้ใช้ยืนยันก่อนเริ่ม train** (มีรูปครบไหม / ยอม cost ไหม). เช็ค `balance`.
2. **Train** — `show_characters(action='train')` + รูป (upload ผ่าน `media_upload_widget` / `media_import_url` ก่อน → media_id). รอ ~10 นาที → ได้ `soul_id`.
3. **Cost** — `generate_image(model='soul_2', soul_id='<id>', ..., get_cost: true)`.
4. **Generate (ซ้ำได้หลายภาพ)** —
   ```text
   generate_image(
     model    = 'soul_2',
     soul_id  = '<soul_id ที่ train>',
     prompt   = '<scene/ท่าทาง/ฉาก ที่ 1: เช่น presenter ชี้กราฟบนจอ, สำนักงานโมเดิร์น>',
     aspect_ratio = '16:9'
   )
   # เปลี่ยน prompt scene 2, 3, ... โดยใช้ soul_id เดิม → หน้าคงเดิม
   ```
5. **Poll** — image sync. ทำหลาย scene = หลาย call (หรือ `count` หลาย variant ต่อ scene).
6. **Deliver** — ชุดภาพหน้าเดียวกันข้าม scene → ใช้เป็น persona/presenter ต่อเนื่องทั้ง deck.

**Insert เข้า deck:** วางภาพ persona เดียวกันใน customer-journey / before-after / testimonial mockup เพื่อความต่อเนื่องเชิงเล่าเรื่อง. ผ่าน `b2b-presentation-creator` (AI imagery) + เจนนี่ build.

> **Note:** Soul ID = สินทรัพย์ reusable — train ครั้งเดียว ใช้ได้หลายงาน. บันทึก `soul_id` ไว้ใน project note.

---

## 4. DTC product ad จากเว็บลูกค้า

**เป้าหมาย:** โฆษณา product/brand (UGC, Unboxing, Product-Review, Tutorial) สร้างจาก **เว็บไซต์ลูกค้า** โดยตรง — สำหรับ pitch งาน marketing/DTC หรือ mockup แคมเปญ.

**Model / Tool:** `show_marketing_studio` (ตัวหลัก) → ออก image/video ผ่าน `marketing_studio_image` / `marketing_studio_video`.

**ขั้นตอน:**
1. **Pre-flight** — เช็ค MCP + `balance`. เลือก `type`:
   - `product` = **สินค้าชิ้นเดียว** (ad โชว์สินค้า)
   - `webproduct` = **เว็บ/แอป** (ad โปรโมตเว็บ/บริการ; App-Store link → webproduct)
   - ไม่ชัด → default `product`.
2. **Fetch จากเว็บ** —
   ```text
   show_marketing_studio(action='fetch', type='product', url='<URL เว็บสินค้าลูกค้า>')
   # เว็บแบรนด์ทั้งก้อน (โลโก้/สี/ฟอนต์) → brand_kit ด้วย scrap_url
   show_marketing_studio(action='fetch', type='brand_kit', scrap_url='<URL หน้าแบรนด์>')
   ```
   เป็น async (มี progress pill) — รอ fetch เสร็จได้ product/brand_kit object.
3. **เลือก preset + settings** — `show_marketing_studio(action='presets', type='product')` → เลือก hook/preset (UGC / Tutorial / Unboxing / Product-Review) + settings.
4. **Cost** — preflight ราคา (`get_cost: true` ตอน generate).
5. **Create / Generate** — `show_marketing_studio(action='create', type='product', ...)` ตาม preset → ออกเป็น image หรือ video ad. video → **async, poll** ตาม Recipe 2.
6. **Deliver** — ได้ ad image/video. รวมหลาย hook เป็น mockup ทางเลือกแคมเปญ.

**Insert เข้า deck:** ใช้เป็น slide "ตัวอย่างแคมเปญ/ม็อกอัพโฆษณา" ใน proposal งาน marketing — โชว์ผลลัพธ์ที่ลูกค้าจะได้จริงจากเว็บ/สินค้าของเขาเอง (มีพลัง pitch สูง). ส่งต่อ Recipe 6 ก่อนโพสต์จริง.

> รายละเอียด Marketing Studio เต็ม (brand_kit, avatar, ad_format) → `references/marketing-studio.md`.

---

## 5. Upscale ภาพเก่าใน deck

**เป้าหมาย:** ภาพ resolution ต่ำ/เบลอใน deck เก่า (โลโก้, screenshot, ภาพ stock เดิม) → คมพอสำหรับฉาย projector / full-bleed / print proposal.

**Model / Tool:** `upscale_image` (ภาพ) · `upscale_video` (วิดีโอ — bytedance ต้อง width/height + fps · topaz ใช้ aspect-ratio).

**ขั้นตอน:**
1. **Pre-flight** — เช็ค MCP + `balance`. เตรียมภาพต้นทาง → upload เป็น media_id ก่อน: `media_upload_widget` (ไฟล์ local จาก deck) หรือ `media_import_url` (URL).
2. **Cost** — preflight ราคาก่อน batch (ถ้าหลายรูป — รวมเร็ว).
3. **Generate** —
   ```text
   upscale_image(value='<media_id ภาพต้นทาง>')      # ดู param จริงด้วย models_explore/tool schema
   ```
   (ถ้าเป็นวิดีโอ deck เก่า → `upscale_video` + provider: `bytedance` [width/height + fps 24/30/60] หรือ `topaz` [aspect-ratio] → 1080p/2K/4K.)
4. **Poll** — image upscale อาจ sync; **video upscale = async → poll** จน completed.
5. **Deliver** — ได้ภาพคมขึ้น → แทนภาพเดิมในสไลด์ตำแหน่งเดิม.

**Insert เข้า deck:** swap ภาพเดิมด้วยตัว upscale (ขนาดเฟรมเดิม) — เจนนี่ใช้ `insert_image` แทนที่. คู่กับ `remove_background` ถ้าต้องแยก subject ออกจากพื้นเก่า, หรือ `reframe`/`outpaint_image` ถ้าต้องเปลี่ยน aspect ratio ให้พอดี layout ใหม่.

> ไม่แน่ใจ param/ค่าที่รองรับ → **เช็คด้วย `models_explore` / tool schema** ก่อนสั่ง.

---

## 6. Virality check ก่อนโพสต์วิดีโอ

**เป้าหมาย:** ประเมินโอกาสไวรัล + hook/retention ของวิดีโอ (brand video Recipe 2 หรือ DTC ad Recipe 4) **ก่อนตัดสินใจโพสต์ social** — ลด risk โพสต์คอนเทนต์ที่ engagement ต่ำ.

**Model / Tool:** `virality_predictor` (model fixed = `'virality_predictor'`). เสริม: `video_analysis_create` (scene-by-scene) ถ้าต้องวิเคราะห์ละเอียด.

**ขั้นตอน:**
1. **Pre-flight** — เตรียม video เป็น media_id / job_id (จาก generate_video หรือ upload). เช็ค `balance`.
2. **Create** —
   ```text
   virality_predictor(action='create', model='virality_predictor', value='<video media_id / job_id>')
   ```
3. **Poll** — **async** → poll จน completed. (เปิด dashboard เดิมซ้ำ → `virality_predictor(action='preview', value='<job_id>')`.)
4. **อ่านผล** — คืน dashboard: virality / engagement / hook / retention. ใช้ตัดสิน go/no-go + จุดที่ต้องแก้ (เช่น hook 3 วิแรกอ่อน → กลับไป re-generate Recipe 2).
5. **(option) Scene analysis** — `video_analysis_create(video_input_id='<id>'` **หรือ** `youtube_url='...')` → poll `video_analysis_status(video_analyze_id)` (3–5 นาที). วิดีโอยิ่งยาว แม่นน้อยลง — เตือนผู้ใช้.
6. **Deliver** — สรุปคะแนน + คำแนะนำเป็น 1 สไลด์ "Pre-launch readiness" ใน deck หรือ note ส่งทีม marketing.

**Insert เข้า deck:** capture สรุปผล (score + recommendation) เป็น bullet/ตารางในสไลด์ "Content readiness / Why this will perform" — ใช้ประกอบ pitch ความมั่นใจในแคมเปญ.

---

## ตารางสรุป: Recipe → Model → Insert target

| # | Use case | Model หลัก | Async? | Insert เข้า |
|---|---|---|---|---|
| 1 | Hero image (title/divider) | `nano_banana_pro` / `marketing_studio_image` | ไม่ (sync) | title / section slide (background/spot) |
| 2 | Brand/Product video สั้น | `marketing_studio_video` / `kling3_0` / `seedance_2_0` | ใช่ (~3–5 นาที) | opening loop / teaser slide |
| 3 | Consistent character (Soul ID) | `soul_2` + `soul_id` (train ก่อน) | train ~10 นาที | persona / journey / presenter ทั้ง deck |
| 4 | DTC product ad จากเว็บ | `show_marketing_studio` → marketing_studio_* | video = ใช่ | slide ตัวอย่างแคมเปญ/ม็อกอัพ |
| 5 | Upscale ภาพเก่า | `upscale_image` / `upscale_video` | video = ใช่ | swap ภาพเดิมในตำแหน่งเดิม |
| 6 | Virality check | `virality_predictor` | ใช่ | slide content-readiness / note |

> ราคาต่าง model ต่างมาก (video/marketing/upscale แพงสุด) — **`get_cost: true` ก่อนเสมอ**. ไม่แน่ใจ model/ค่าที่รองรับ → `models_explore` / `balance`.

---

## Insert เข้า deck/deliverable — pattern กลาง

ทุก recipe จบที่ "เอา output ไปใช้ในงานจริง" — flow มาตรฐาน:

1. **เลือก output** ที่ดีที่สุด (จาก `count` หลาย variant หรือ `show_generations`).
2. **ดาวน์โหลด** ไฟล์ลงเครื่อง (ภาพ → .png/.jpg · วิดีโอ → .mp4).
3. **ส่งต่อ pipeline สไลด์:**
   - **skill `b2b-presentation-creator`** — เมื่อออกแบบสไลด์/เลือกตำแหน่ง hero/AI imagery (ref 07 Method 3) → ระบุ slide + role ของภาพ.
   - **agent `deliverable-gen-agent` (เจนนี่)** — เป็นคน build .pptx/.docx จริง: วางภาพด้วย `insert_image`, swap ภาพเดิม, จัด layout, Font Discipline. ส่ง path ไฟล์ + slide เป้าหมายให้เจนนี่.
4. **ปฏิบัติตาม Hard Rules:** ก่อน save deliverable ต้องมี pre-save confirmation + version `V##R##` (CLAUDE.md H9). ถามภาษาไฟล์ (TH/EN/Bilingual) ถ้ายังไม่ระบุ (H6).
5. **Next step** — เสนอ upscale / variation / virality check ตามบริบทงานถัดไป.

> Higgsfield = **source ของ asset** (ภาพ/วิดีโอ); `b2b-presentation-creator` + เจนนี่ = **คนประกอบเข้า deliverable**. แยกบทบาทให้ชัด — skill นี้ generate, agent build.
