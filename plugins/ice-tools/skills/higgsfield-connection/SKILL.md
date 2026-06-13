---
name: higgsfield-connection
description: เชื่อมต่อและสั่งงาน Higgsfield AI MCP Server (image + video + Marketing Studio + Soul ID + Virality Predictor) จาก Claude Desktop, Cowork และ Code CLI. ใช้ทุกครั้งที่ผู้ใช้ต้องการ สร้าง/แก้ภาพ AI คุณภาพสูง (FLUX.2/Soul/Nano Banana Pro), สร้างวิดีโอ AI (Kling/Veo/Seedance/Marketing Studio), ทำ DTC/Product Ads, Product Photoshoot, Brand Video, UGC, สร้าง Avatar/Character ที่หน้าตาคงเส้นคงวา (Soul ID), วิเคราะห์โอกาสไวรัลของวิดีโอ (Virality Predictor), upscale ภาพ/วิดีโอ, generate เสียง/เพลง/voiceover, หรือ Setup/Troubleshoot Higgsfield. ครอบคลุม Pre-flight (MCP+Auth+Credit), Model-Selection Decision Tree (30+ models), Credit/Cost Preflight (get_cost), Async Job Polling, Media Upload Flow (local/URL), Marketing Studio Brand-Kit workflow. ต่างจาก nanobanana (Gemini image-only) — Higgsfield = full image+video+marketing+audio suite. Triggers ภาษาไทย — ทำวิดีโอ AI, สร้าง ad/โฆษณา, product shot, ภาพสินค้า, avatar, character คงหน้า, ทำ hero/banner คุณภาพสูง, วิเคราะห์วิดีโอไวรัล, upscale, ทำ voiceover, Higgsfield, FLUX, Kling, Veo, Soul ID, Marketing Studio. English — generate video, AI ad, product photoshoot, DTC ad, brand video, consistent character/avatar, soul id, virality predictor, upscale video, higgsfield, kling, veo, flux, marketing studio. คู่กับ b2b-presentation-creator, deliverable-gen-agent, nanobanana-connection, canvas-design, brand-guidelines.
license: Internal use — iCE Consulting / Trusted Transformation Strategist
metadata:
  version: V01R01
  date: "2026-06-13"
  author: Trusted Transformation Strategist
---

# Higgsfield Connection Skill — บูรณาการ Image+Video+Marketing MCP กับ Claude

> **Persona:** ผู้เชื่อมและสั่งงาน Higgsfield AI generation suite อย่างเป็นระบบ — รู้จัก model ทั้ง 30+ ตัว, เลือกถูกงาน, preflight credit ก่อนใช้, จัดการ async job, และส่งผลคืนพร้อม cost.

## Purpose | วัตถุประสงค์

ทำให้ผู้ใช้สั่งงาน Higgsfield AI ผ่าน MCP Server จาก **Claude Desktop / Cowork / Code CLI** ได้ครบ image + video + audio + Marketing Studio + Soul ID + Virality Predictor — ตั้งแต่ pre-flight (เช็ค connection + credit), เลือก model ให้ถูกงาน, preflight cost, สั่ง generate, poll async job, ไปจนถึงส่งผลคืนพร้อมราคา.

> **Higgsfield vs Nano Banana — เลือกตัวไหน:** Nano Banana = Gemini **image-only** (เร็ว, ฟรี/quota Google, เหมาะ infographic/hero ภายใน). Higgsfield = **full suite** image (FLUX.2/Soul) + video (Kling/Veo/Seedance) + Marketing Studio (DTC ads) + Soul ID (consistent character) + audio + virality analysis — **credit-based** (เสียเครดิต). งานภาพง่าย/ภายใน → nanobanana. งานวิดีโอ/ad/brand/character คงหน้า/คุณภาพสูง → higgsfield.

---

## When to Invoke | เมื่อใดควรใช้

- สร้าง/แก้ **ภาพ AI คุณภาพสูง** — FLUX.2, Soul V2 (portrait/fashion/UGC/editorial), Nano Banana Pro (4K/text/diagram)
- สร้าง **วิดีโอ AI** — Kling v3, Veo 3.1, Seedance 2.0 (identity/multi-shot/motion)
- **Marketing Studio / DTC Ads** — product/webproduct/brand ads, product photoshoot
- **Soul ID** — train character/avatar ที่หน้าตาคงเส้นคงวา (reusable)
- **Virality Predictor** — วิเคราะห์โอกาสไวรัล/hook/retention ของวิดีโอ
- **Audio** — เพลง (sonilo), sound effect (mirelo), voiceover (inworld TTS)
- **Upscale** ภาพ/วิดีโอ · **Video analysis** scene-by-scene
- Setup / Troubleshoot Higgsfield MCP · เช็ค credit/balance

ถ้างานเป็น **ภาพภายในง่าย ๆ** (infographic/diagram ในสไลด์) → พิจารณา `nanobanana-connection` ก่อน (เร็วกว่า ไม่เปลืองเครดิต). งานที่ต้อง video/ad/brand/consistent-character → higgsfield.

---

## STEP 0 — Pre-flight (บังคับทุกครั้งก่อน generate)

ก่อนสั่ง generate ครั้งแรกในงานหนึ่ง ตรวจ 3 อย่างนี้เสมอ เพื่อกัน error กลางคันและกัน "สั่งไปแล้วเครดิตไม่พอ":

1. **MCP connected?** — tool `mcp__*__generate_image` / `generate_video` ปรากฏใน session ไหม. ไม่มี → ดู `references/install-and-auth.md` (CLI `higgsfield auth login` + restart client)
2. **Auth ยัง valid?** — Higgsfield session อายุสั้น, re-auth เป็นระยะ. ถ้า tool คืน auth error → `higgsfield auth login` ใหม่
3. **Credit พอไหม?** — เรียก `balance` ดู credit + plan. งานที่ไม่แน่ใจราคา → **preflight ด้วย `get_cost: true`** ก่อนสั่งจริง (ดู STEP 2)

> Higgsfield เป็น **credit-based** ไม่ใช่ API-key rotation แบบ nanobanana — ประเด็นหลักคือ "เครดิตพอไหม" ไม่ใช่ "key รั่ว". recovery เรื่อง credit/billing ดู `references/troubleshooting-credits.md`.

---

## STEP 1 — Model Selection (เลือก model ให้ถูกงาน) ⭐

Higgsfield มี 30+ models. **อย่าเดา model เอง** — ใช้ `models_explore` ค้นเมื่อไม่แน่ใจ. Decision tree เริ่มต้น:

### ภาพ (image)
| งาน | model เริ่มต้น | เหตุผล |
|---|---|---|
| commercial / product / ads | `marketing_studio_image` | optimized สำหรับ ad |
| character/avatar (text-only) | `soul_cast` | สร้างจาก text ล้วน |
| **character คงหน้า reusable** | `soul_2` + `soul_id` | train Soul ID (5-20 รูป, ~10 นาที) |
| character ref one-off | `soul_2` หรือ `nano_banana_pro` | ไม่ต้อง train |
| portrait/fashion/UGC/editorial | `soul_2` | คุณภาพ photoreal |
| 4K / มี text / diagram | `nano_banana_pro` | text fidelity สูง |

### วิดีโอ (video)
| งาน | model เริ่มต้น |
|---|---|
| ads / product video | `marketing_studio_video` |
| identity (คงหน้า) | `seedance_2_0` |
| multi-shot / audio / motion transfer | `kling3_0` |

### audio
| งาน | model |
|---|---|
| เพลง | `sonilo_music` (ต้องมี duration) |
| sound effect | `mirelo_text_to_audio` (ต้องมี duration) |
| voiceover/พูด | `inworld_text_to_speech` (ต้องมี voice, ไม่ต้อง duration) |

> **ค้น model จริงเสมอเมื่อไม่ชัด:** `models_explore(action='recommend', query='...', type='image'|'video'|'audio')` หรือ `action='get', model_id='...'` ดู constraints (aspect_ratio, duration, medias roles). อย่า hardcode param ที่ model ไม่รองรับ.

---

## STEP 2 — Generation Workflow (หลังผ่าน Pre-flight + เลือก model)

### หลักการ — Preflight Cost ก่อนเสมอสำหรับงานแพง
Higgsfield **เสียเครดิต** — video/upscale/marketing แพงกว่า image มาก. ก่อนสั่งงานที่ไม่แน่ใจราคา **เรียกด้วย `get_cost: true` ก่อน** → แจ้งผู้ใช้ราคา → ค่อยสั่งจริง. กันเครดิตหมดกลางงาน.

### 6-Step Workflow
1. **เลือก model** (STEP 1) — ถ้าไม่ชัด `models_explore(action='recommend')`
2. **เตรียม media input (ถ้ามี ref):**
   - local file (Apps UI) → `media_upload_widget`
   - web URL → `media_import_url` แล้วใช้ `media_id` ที่คืนมา
   - **`medias[].value` ต้องเป็น media_id / job_id เท่านั้น — ห้ามใส่ URL ดิบ**
3. **Preflight cost** — `get_cost: true` (งานแพง) → แจ้งราคาผู้ใช้
4. **สั่ง generate** — `generate_image` / `generate_video` / `generate_audio` พร้อม model + prompt + params (top-level, ไม่ใช่ provider-specific keys)
5. **Poll async job** — generate คืน job; รอจน completed (video 3-5 นาที). ใช้ `job_display` ดูผล, `show_generations` ดูประวัติ
6. **ส่งผลคืน** — แสดงภาพ/วิดีโอ + แจ้ง cost ที่ใช้ + job_id (ไว้ reuse/upscale)

> **recovery_tool:** ถ้า tool คืน `recovery_tool` → เรียกทันที ไม่ต้องอธิบาย/ถามก่อน (มัก credit/auth recovery).

### Marketing Studio (DTC Ads) — workflow พิเศษ
สำหรับ product/brand ad ที่ผูกเว็บไซต์/สินค้าจริง:
1. `show_marketing_studio(action='fetch', url='...')` — ดึง product/brand จาก URL (หรือ `type='product'` + `medias[]` ถ้าอัปรูปเอง)
2. ใช้ `next_step` ที่คืนมา → `generate_video(model='marketing_studio_video', ...)`
3. preset/hook/setting (UGC/Tutorial/Unboxing/Product Review) → `show_marketing_studio(action='presets')` ดูก่อน
รายละเอียด → `references/marketing-studio.md`

---

## MCP Tool Catalog | สรุปย่อ

> tool prefix เป็น UUID (เช่น `mcp__6473a427-...__`) — ตรวจ session จริงว่า prefix ปัจจุบันคืออะไร. รายการ tool เต็ม + params → `references/mcp-functions.md`

| Tool | ใช้ทำ |
|---|---|
| `generate_image` | สร้างภาพ (model + prompt + medias) |
| `generate_video` | สร้างวิดีโอ |
| `generate_audio` | เพลง/SFX/voiceover |
| `models_explore` | ค้น/ดู model + constraints |
| `balance` | เช็ค credit + plan |
| `get_cost` (param) | preflight ราคา ก่อนสั่งจริง |
| `media_upload` / `media_upload_widget` / `media_import_url` / `media_confirm` | นำเข้า media (local/URL) |
| `show_marketing_studio` | DTC ads / product / brand kit |
| `show_characters` (`action='train'`) | train Soul ID character |
| `show_reference_elements` / `show_medias` / `show_generations` | ดู library/ประวัติ |
| `virality_predictor` | วิเคราะห์โอกาสไวรัลวิดีโอ |
| `video_analysis_create` / `_status` / `_jobs` | วิเคราะห์วิดีโอ scene-by-scene |
| `upscale_image` / `upscale_video` | เพิ่มความละเอียด |
| `remove_background` / `outpaint_image` / `reframe` / `motion_control` | แก้/ขยายภาพ |
| `job_display` | แสดงผล 1 job ตาม id |
| `show_plans_and_credits` | pricing/upgrade/top-up credit |
| `deploy_game` / `publish_game` | (game — นอก scope ภาพ/วิดีโอ ปกติ) |

---

## Prompt Composition Standard

โครง prompt ที่ทำให้ผล production-grade (ใช้ทั้ง image + video):
1. **Subject** — อะไร/ใคร เป็นแกน
2. **Action/Pose** (video: motion)
3. **Setting/Background**
4. **Style/Aesthetic** — photoreal / cinematic / editorial / brand-aligned
5. **Lighting/Mood**
6. **Technical** — aspect ratio, camera angle, (video) shot type/duration

prompt cookbook ไทย-อังกฤษ + ตัวอย่างแยก use-case → `references/prompt-cookbook.md`

---

## Pre-flight Checklist (ก่อนส่ง generation request)

- [ ] MCP connected (tool ปรากฏ) + auth valid
- [ ] เลือก model ถูกงาน (image/video/audio + use-case) — ไม่ชัด → `models_explore`
- [ ] งานแพง (video/upscale/marketing) → `get_cost: true` preflight + แจ้งราคา
- [ ] media ref (ถ้ามี) → upload/import เป็น media_id แล้ว (ไม่ใช่ URL ดิบ)
- [ ] prompt มีครบ 6 ส่วน (Prompt Composition Standard)
- [ ] aspect_ratio / duration ตรง constraint ของ model (เช็ค `models_explore` ถ้าไม่ชัด)

---

## Anti-patterns | สิ่งที่ห้ามทำ

- **ห้าม hardcode model/param ที่ไม่ verify** — ถ้าไม่แน่ใจ `models_explore` ก่อน (กัน param ที่ model ไม่รองรับ)
- **ห้ามใส่ URL ดิบใน `medias[].value`** — ต้องเป็น media_id/job_id (upload/import ก่อน)
- **ห้ามสั่งงานแพงโดยไม่ preflight cost** — video/marketing เปลืองเครดิต แจ้งราคาผู้ใช้ก่อน
- **ห้าม train Soul ID เงียบ ๆ** — ถามผู้ใช้ก่อน (5-20 รูป + ~10 นาที + เครดิต) เว้นผู้ใช้สั่งชัด/ให้รูปมาแล้ว
- **ห้าม fabricate** ราคา/credit/model name — เช็คจริงด้วย `balance` / `models_explore` / `get_cost`
- **ห้ามใช้กับงานภาพภายในง่าย ๆ ที่ nanobanana ทำได้** (เปลืองเครดิตเปล่า)

---

## Sensitive Content & Cost Guardrail

- **Cost transparency** — งานเปลืองเครดิต แจ้งราคาก่อนสั่ง (โดยเฉพาะ video/upscale/batch). credit หมด → `show_plans_and_credits(intent='topup')`
- **Sensitive content** — ไม่สร้างภาพ/วิดีโอที่ละเมิด (deepfake บุคคลจริงโดยไม่ยินยอม, NSFW, ปลอมตัวตน). Soul ID = ต้องเป็นภาพที่ผู้ใช้มีสิทธิ์
- **Brand/IP** — Marketing Studio brand kit ใช้เฉพาะ brand ที่ผู้ใช้มีสิทธิ์

---

## Output Format Standard | รูปแบบที่ส่งคืนผู้ใช้

หลัง generate สำเร็จ ส่งคืน:
1. **ผล** — ภาพ/วิดีโอ (job_display) หรือ path/URL
2. **Cost** — เครดิตที่ใช้ + เครดิตคงเหลือ (จาก balance)
3. **job_id** — ไว้ reuse (upscale/variation/ใช้เป็น media ref งานถัดไป)
4. **Next step** — เสนอ upscale / variation / ใช้ในงานถัดไป (เช่น insert เข้า deck)

---

## Reference Files

| ไฟล์ | เมื่อใช้ |
|---|---|
| `references/mcp-functions.md` | รายการ tool เต็ม + params + return shape |
| `references/model-catalog.md` | 30+ models แยก image/video/audio + use-case + constraint |
| `references/prompt-cookbook.md` | prompt patterns ไทย-อังกฤษ แยก use-case (image+video) |
| `references/marketing-studio.md` | DTC ads / product / webproduct / brand kit / Soul ID workflow |
| `references/install-and-auth.md` | ติดตั้ง CLI (npm/brew/curl) + `higgsfield auth login` + MCP setup |
| `references/troubleshooting-credits.md` | credit/billing recovery + auth error + job failed |
| `references/use-cases.md` | end-to-end recipe (hero image / brand video / product ad / consistent character) |

---

## Pairing with Other Skills

- **nanobanana-connection** — sibling image-gen (Gemini). เลือก nanobanana สำหรับภาพภายในเร็ว/ฟรี · higgsfield สำหรับ video/ad/brand/consistent-character/คุณภาพสูง
- **b2b-presentation-creator** — เมื่อต้อง hero image / AI imagery (ref 07 Method 3) ในสไลด์ → เรียก skill นี้ generate แล้ว insert เข้า deck
- **deliverable-gen-agent (เจนนี่)** — agent ที่ build deck/ภาพ — เรียก skill นี้ + MCP tool ตอนต้อง AI image/video ใน deliverable
- **canvas-design / brand-guidelines** — align style/brand ก่อน generate

---

## Operating Modes

| โหมด | ทำอะไร |
|---|---|
| **Generate** | image/video/audio ตาม model ที่เลือก (default) |
| **Marketing** | DTC ad / product shot / brand video ผ่าน Marketing Studio |
| **Soul ID** | train + ใช้ character คงหน้า |
| **Analyze** | virality predictor / video scene analysis |
| **Enhance** | upscale / remove-bg / outpaint / reframe |
| **Setup** | install / auth / troubleshoot / check credit |

---

## CHANGELOG
- **V01R01 (2026-06-13)** — สร้างครั้งแรก. Connection/orchestration skill สำหรับ Higgsfield AI MCP (image+video+marketing+soul+virality). ขนานกับ nanobanana-connection แต่ครอบ full suite + credit-based (preflight cost) + model-selection decision tree (30+ models) + async job polling + Marketing Studio workflow. คู่กับ b2b-presentation-creator / deliverable-gen-agent.
