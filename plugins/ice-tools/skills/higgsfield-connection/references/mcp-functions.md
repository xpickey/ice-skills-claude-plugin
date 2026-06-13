# Higgsfield MCP — Tool Reference (functions + params)

> Tool prefix เป็น **UUID** (เช่น `mcp__6473a427-64e7-4c97-b980-658fc7de9360__`). prefix อาจต่างตาม session/install — ตรวจ session จริงว่า prefix ปัจจุบันคืออะไร แล้วใช้ tool ตามชื่อหลัง prefix. ด้านล่างใช้ชื่อ tool (ไม่รวม prefix).

## Generation

### `generate_image`
สร้างภาพ. params: `model` (required), `prompt`, `aspect_ratio`, `count` (1-4), `medias[]` ({value, role}), `get_cost` (bool — preflight ราคา).
- `medias[].value` = media_id (จาก media_upload/media_import_url) หรือ job_id — **ห้าม URL ดิบ**
- `medias[].role` ต่างตาม model — ดู `models_explore(action='get')`

### `generate_video`
สร้างวิดีโอ. params: `model` (required), `prompt`, `aspect_ratio`, `duration` (วินาที), `count` (1-4), `medias[]`, `preset_id` (ใช้กับ model `higgsfield_preset`), `get_cost`.
- duration ไม่ระบุ → model default; ไม่รองรับ → clamp/นearest
- roles: start_image / end_image / image (ตาม model)

### `generate_audio`
เพลง/SFX/voiceover. params: `model` (required), `prompt` (required), `voice` (inworld TTS เท่านั้น), `duration` (sonilo_music + mirelo ต้องมี; inworld ไม่ต้อง), `count: 1` (single-sample), `get_cost`.
- ห้ามใส่ provider-specific keys (text/seed/num_samples/ambience ฯลฯ)

## Discovery / Cost

### `models_explore`
ค้น/ดู model. params: `action` (list/search/get/recommend), `query`, `type` (image/video/audio/3d), `input` (text/image), `model_id` (get), `limit`, `after` (cursor).
- `recommend` + goal + input context → แนะ model
- `get` + `model_id` → constraints (aspect_ratio, duration, medias roles, params)

### `balance`
credit + plan ปัจจุบัน. ไม่มี params. (transaction history → `transactions`)

### `get_cost` (param ใน generate_*)
ตั้ง `get_cost: true` ใน generate_image/video/audio → คืน cost (credit) โดยไม่สั่งงานจริง. ใช้ preflight งานแพง.

## Media I/O

| tool | ใช้ |
|---|---|
| `media_upload_widget` | local file (Apps UI) — เปิด widget ให้ผู้ใช้เลือกไฟล์ |
| `media_upload` | upload media (คืน media_id) |
| `media_import_url` | web URL → media_id (ใช้ media_id ต่อ ไม่ใช่ URL) |
| `media_confirm` | ยืนยัน media ที่ upload |
| `upload_image` / `upload_file` | (ดู session — บาง deploy แยก tool) |

## Marketing Studio

### `show_marketing_studio`
DTC ads / product / webproduct / brand kit / avatar.
- `action`: list / presets / fetch / create / update / get / delete
- `type`: avatar / product / webproduct / hook / setting / ad_reference / brand_kit / ad_format
- `url` + `action='fetch'` → ดึง product/brand จากเว็บ (async, มี progress pill)
- `product` = สินค้าชิ้นเดียว (ad โชว์สินค้า) · `webproduct` = เว็บ/แอป (ad โปรโมตเว็บ) · ไม่ชัด → default product / App-Store → webproduct
- manual create: `action='create'` + `type` + `medias[]` (media_input ต้องมี url)
- brand_kit: `scrap_url` (fetch จากเว็บ brand) · create/update ต้องมี CDN url (upload ก่อน)

## Character / Soul ID

### `show_characters`
- `action='train'` → train Soul ID (5-20 รูป, ~10 นาที, เสียเครดิต) — **ถามผู้ใช้ก่อน**
- ใช้ใน generate: `model='soul_2'` + `soul_id`

### `show_reference_elements` / `show_medias` / `show_generations`
ดู library / media / ประวัติ generation

## Analysis

### `virality_predictor`
- `action='create'` (เริ่มจาก video media_id/job_id) / `'preview'` (เปิด dashboard เดิมด้วย job_id)
- `model: 'virality_predictor'` (fixed)
- คืน: virality/engagement/hook/retention dashboard

### `video_analysis_create` / `video_analysis_status` / `video_analysis_jobs`
scene-by-scene analysis.
- create: `video_input_id` (uploaded) **หรือ** `youtube_url` (อย่างใดอย่างหนึ่ง)
- คืน queued → poll `video_analysis_status(video_analyze_id)` จน completed (3-5 นาที)
- วิดีโอยิ่งยาว ยิ่งแม่นน้อย — เตือนผู้ใช้

## Enhance / Edit

| tool | ใช้ |
|---|---|
| `upscale_image` | เพิ่มความละเอียดภาพ |
| `upscale_video` | provider `bytedance` (preset + ต้องส่ง width/height + fps 24/30/60) หรือ `topaz` (aspect-ratio, ไม่ต้อง dimensions) → 1080p/2K/4K |
| `remove_background` | ลบพื้นหลัง |
| `outpaint_image` | ขยายภาพออกนอกกรอบ |
| `reframe` | เปลี่ยน aspect ratio |
| `motion_control` / `animation_actions` | คุม motion วิดีโอ |

## Display / Billing / Workspace

| tool | ใช้ |
|---|---|
| `job_display` | แสดงผล 1 job ตาม id (1 call/id) |
| `show_output_stats` | สถิติ output |
| `show_plans_and_credits` | pricing widget (intent: upgrade/topup/auto_refill/general) — credit หมดใช้ตัวนี้ |
| `transactions` | ประวัติเครดิต |
| `list_workspaces` / `select_workspace` | จัดการ workspace |
| `sync_agents` | sync agents |
| `presets_show` | ดู preset (ใช้กับ higgsfield_preset video) |
| `personal_clipper_create/_jobs/_status` | clip วิดีโอ |
| `generate_3d` | สร้าง 3D |
| `maintenance` | server maintenance |

## Async Pattern (สำคัญ)
generate_video / virality / video_analysis / upscale = **async** — คืน job/queued → ต้อง poll status จน completed. video gen 3-5 นาที. อย่ารอ block — แจ้งผู้ใช้ว่ากำลังประมวลผล + poll เป็นระยะ.

## recovery_tool
ถ้า tool คืน field `recovery_tool` → เรียก tool นั้นทันที ไม่ต้องอธิบาย/ถามก่อน (มัก credit/auth/billing recovery).
