---
name: nanobanana-connection
description: เชื่อมต่อและสั่งงาน Nano Banana MCP Server (Google Gemini Image Generation) จาก Claude Desktop, Cowork และ Code CLI. ใช้ทุกครั้งที่ผู้ใช้ต้องการ สร้างภาพ AI, แก้ภาพ, ทำ Logo, Hero Image, Product Shot, Thumbnail, Banner, Mockup, Sticker, Illustration, Setup/Troubleshoot Nano Banana MCP, หรือ เปลี่ยน/Rotate API Key. ครอบคลุม Pre-flight Connection Test (MCP+Auth+Quota), Prompt Cookbook ไทย-อังกฤษ 30+ Pattern, Aspect Ratio/Resolution, Multi-image Editing, Billing/Quota Recovery 7 Scenario, และ API Key Rotation One-script (Desktop+Cowork+Code CLI พร้อมกัน). Triggers ภาษาไทย — ทำภาพให้หน่อย, สร้างภาพ AI, วาด AI, ทำ hero/thumbnail/logo/product shot/banner/illustration, แก้ภาพนี้, สร้าง mockup, Nano Banana, Gemini image, เปลี่ยน API Key, rotate key, Key รั่ว. English — generate/edit image, create illustration/banner, AI image, nano banana, rotate API key, change Gemini key, leaked key. คู่กับ b2b-presentation-creator, canvas-design, brand-guidelines.
license: Internal use — iCE Consulting / Trusted Transformation Strategist
metadata:
  version: V02R02
  date: 2026-05-25
  author: Trusted Transformation Strategist
---

# Nano Banana Connection Skill — บูรณาการ Image Generation MCP กับ Claude

## Purpose | วัตถุประสงค์

ทำให้ผู้ใช้สั่งสร้างภาพ AI ผ่าน Nano Banana MCP Server (Google Gemini Image Models) จาก **Claude Desktop, Claude Cowork และ Claude Code CLI** ได้อย่างเป็นระบบ ครอบคลุมตั้งแต่การติดตั้ง การตรวจ Connection ก่อนใช้งาน การเลือก Model Tier การออกแบบ Prompt ที่ใช้งานได้จริง ไปจนถึงการ Recovery เมื่อเจอ Quota/Billing/Auth Error

**Skill นี้แก้ปัญหา 6 ข้อ:**
1. ผู้ใช้ไม่รู้ว่า Nano Banana MCP มี Tool/Resource อะไรบ้าง สั่งงานอะไรได้แค่ไหน
2. Auth Setup ซับซ้อน (3 วิธี: API Key / Vertex AI ADC / Auto) และ Config File ต่างกันใน Cowork/Desktop กับ Code CLI
3. **Free Tier ของ Gemini Image Generation = 0** (กับดักที่ผู้ใช้ใหม่เกือบทุกคนเจอ) — Skill นี้บังคับตรวจ Billing ใน Pre-flight
4. Token หาย/หมดอายุระหว่างทำงาน — Skill นี้บังคับ Pre-flight Test ก่อนทุกครั้ง
5. ไม่มี Convention การเลือก Model Tier ที่เหมาะกับงาน (Flash vs NB2 vs Pro) ทำให้สิ้นเปลือง Credit หรือคุณภาพไม่พอ
6. Prompt สั้นเกินไปได้ภาพ Generic — Skill นี้มี Prompt Cookbook 30+ Pattern พร้อม Variable

## When to Invoke | เมื่อใดควรใช้

ใช้ Skill นี้เมื่อผู้ใช้ต้องการ:
- สร้างภาพประกอบ: Hero Image, Section Cover, Thumbnail, Banner, Illustration
- ทำ Logo, Product Shot, Sticker, Mockup, Icon
- แก้ไขภาพเดิม: Iterative Edit, Composition Transfer, Style Transfer, Background Change
- สร้าง Mood Board สำหรับ Workshop หรือ Design Sprint
- ทำภาพประกอบใน Proposal, Slide Deck, Marketing Campaign, Brand Asset
- Setup, Troubleshoot, หรือเปลี่ยน Auth Method ของ Nano Banana MCP
- **เปลี่ยน / Rotate Gemini API Key** (กรณี Key รั่ว, ครบกำหนด, หรือเปลี่ยน Environment) — ใช้ Bundle Script `scripts/rotate_api_key.sh` ทำพร้อมกันทุก Client

ห้ามใช้ Skill นี้ทำ:
- Algorithmic Art ที่ใช้ Code (ใช้ `algorithmic-art` แทน)
- Poster/Print Material ที่ต้องการ Vector Layout (ใช้ `canvas-design`)
- Diagram/Flowchart (ใช้ Mermaid หรือ `visualize`)
- Image Recognition/OCR (Nano Banana ทำ Generation/Edit ไม่ใช่ Recognition)

---

## STEP 0 — Pre-flight Connection Test (บังคับทุกครั้ง)

**ห้ามข้าม. ทำก่อนเรียก generate_image ทุกครั้ง.**

เหตุผล: Nano Banana ใช้ API Key/ADC Token ที่อยู่ใน MCP Config File หาก Skill ไม่ตรวจก่อน จะเกิด Failure Pattern: สั่งสร้างภาพ → Server ไม่ตอบ → ผู้ใช้รอเปล่า → เสียเวลา/Credit Pre-flight Call ใช้เวลา <2 วินาที ป้องกันได้ทั้งหมด

### Pre-flight Sequence — 3 ขั้น

**ขั้นที่ 1 — Health Check ด้วย `show_output_stats`**

เรียก `show_output_stats` เพราะเป็น Tool Local-only ไม่กิน Gemini API Credit ตอบเร็ว และ Fail Fast ถ้า Server/Config ผิด

**ขั้นที่ 2 — ตีความผลลัพธ์**

| Result | สาเหตุ | ไปที่ Scenario |
|---|---|---|
| Stats returned ปกติ | Server พร้อม + Config ถูก | ดำเนินงานต่อ (ข้ามไป Step 1) |
| `Tool not found` / MCP Server หาไม่เจอ | MCP ยังไม่ Setup / ยังไม่ Restart Client | **Scenario A** |
| `GEMINI_API_KEY not set` | ไม่มี API Key | **Scenario B** |
| `auth` / `credential` / `unauthorized` / `401` / `403` | Key หมดอายุ / ผิด | **Scenario C** |
| `Server failed to start` / `uv: command not found` | uv ไม่เจอ / Path ผิด / cwd ผิด | **Scenario D** |
| `Vertex AI` / `GCP` / `aiplatform` Error | Vertex AI ADC ผิด | **Scenario E** |
| Other unknown error | ไม่รู้ที่มา | **Scenario F** (Diagnostic) |

**ขั้นที่ 3 — Mid-task Auth/Quota Probe**

ถ้า Operation ใดตอบกลับด้วย Error ที่มีคำว่า `RESOURCE_EXHAUSTED`, `429`, `quota`, `billing`, `free_tier` → กลับไป **Scenario G — Billing/Quota** ทันที (ดู `references/troubleshooting-quota.md`)

---

## STEP 1 — Recovery Scenarios

### Scenario A — MCP ยังไม่ Setup / ยังไม่ Restart Client
แสดงคำตอบนี้กับผู้ใช้:
```
ตรวจไม่พบ Nano Banana MCP ในเครื่องของท่านครับ
อาจเป็นเพราะ (1) ยังไม่ติดตั้ง MCP Server หรือ (2) ติดตั้งแล้วแต่ยังไม่ Restart Client

หากยังไม่ติดตั้ง ดูคู่มือเต็ม: references/install-and-auth.md
หากติดตั้งแล้ว: ปิด Client สนิท (Cmd+Q) → เปิดใหม่ → ลองอีกครั้ง

ติดตั้งสั้นๆ:
  1. ขอ Gemini API Key ที่ https://aistudio.google.com/apikey
  2. เปิด Billing (Free Tier ไม่ครอบคลุม Image Generation)
  3. ติดตั้ง uv: curl -LsSf https://astral.sh/uv/install.sh | sh
  4. แก้ Config ตาม Client ของท่าน (ดู references/install-and-auth.md)
```

### Scenario B — ไม่มี API Key
```
Config มี Server แล้วแต่ไม่มี GEMINI_API_KEY ครับ

แก้ไข:
  1. ขอ Key ที่ https://aistudio.google.com/apikey
  2. แก้ Config:
     - Claude Desktop/Cowork: ~/Library/Application Support/Claude/claude_desktop_config.json
     - Claude Code CLI: claude mcp remove nanobanana && claude mcp add ...
  3. Restart Client (Cmd+Q แล้วเปิดใหม่)
```

### Scenario C — API Key หมดอายุ / ผิด
```
API Key มีอยู่ แต่ Gemini ปฏิเสธครับ (อาจหมดอายุ ถูก Revoke หรือพิมพ์ผิด)

แก้ไข:
  1. เปิด https://aistudio.google.com/apikey
  2. ตรวจ Key ที่ใช้ — ถ้า Revoke แล้ว → ลบทิ้ง + สร้างใหม่
  3. Update Config (เปลี่ยน GEMINI_API_KEY)
  4. Restart Client
```

### Scenario D — uv/Path ผิด (Server Disconnected) ⭐ พบบ่อย
```
Server Start ไม่ได้ครับ — ส่วนใหญ่เพราะ:

สาเหตุ 1: Claude Desktop เรียก uv ไม่เจอ (GUI Apps บน macOS ไม่อ่าน ~/.zshrc)
  แก้: ใช้ Full Path ของ uv ใน command (เช่น /Users/<user>/.local/bin/uv)

สาเหตุ 2: ไม่ระบุ cwd ทำให้ uv run หา pyproject.toml ไม่เจอ
  แก้: เพิ่ม "cwd": "/path/to/nanobanana-mcp" หรือใช้ args ["run", "--directory", "/path", ...]

สาเหตุ 3: PATH env ใน Config ไม่มี
  แก้: ใส่ "env": {..., "PATH": "/Users/<user>/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"}

Config Template ที่ถูกต้องอยู่ที่ references/install-and-auth.md (section "Fixed Config After Common Errors")
```

### Scenario E — Vertex AI ADC ผิด
```
ท่านใช้ Vertex AI Mode และ ADC มีปัญหาครับ

แก้ไข 5 ขั้น:
  1. Re-authenticate: gcloud auth application-default login
  2. ตรวจ GCP_PROJECT_ID ตรงกับ Project ที่ Enable Vertex AI แล้ว
  3. ตรวจ GCP_REGION = "global" (สำหรับ NB2/Pro), us-central1 สำหรับ Flash 2.5 เท่านั้น
  4. Enable API: gcloud services enable aiplatform.googleapis.com --project=<id>
  5. Grant IAM: roles/aiplatform.user
```

### Scenario F — Unknown Error (Diagnostic Mode)
```
พบ Error ที่ไม่รู้ที่มาแน่ชัดครับ

Diagnostic 5 ขั้น:
  1. รัน Server มือจาก Terminal:
     cd "/path/to/nanobanana-mcp"
     export GEMINI_API_KEY=<key>
     ~/.local/bin/uv run python -m nanobanana_mcp_server.server
     → ดู Error Output ตรงๆ

  2. ตรวจ Log ของ Client:
     macOS: ~/Library/Logs/Claude/
     Look for: mcp-server-nanobanana.log

  3. ทดสอบด้วย MCP Inspector:
     npx @modelcontextprotocol/inspector uvx nanobanana-mcp-server@latest

  4. อัปเดต Client เป็น Version ล่าสุด

  5. ส่ง Error เต็มให้ผม + ระบุขั้นที่ลองแล้ว
```

### Scenario G — Quota Exhausted / Billing ไม่เปิด ⭐ สำคัญที่สุด

**ข้อเท็จจริง: Gemini Image Models ทั้งหมด (NB2, Pro, Flash 2.5) มี Free Tier Quota = 0**
ผู้ใช้ใหม่เกือบทุกคนเจอข้อนี้ครั้งแรก

```
ครับ Error 429 RESOURCE_EXHAUSTED — สาเหตุ: Image Generation ไม่อยู่ใน Free Tier ของ Gemini API

ทางเลือก:
  Option 1 (เร็วที่สุด): เปิด Billing ที่ AI Studio
    → https://aistudio.google.com/app/billing
    → Set up Billing → ใส่บัตรเครดิต
    → Key เดิมใช้ต่อได้ ไม่ต้องเปลี่ยน
    → ตั้ง Budget Alert ที่ $5-$10 ป้องกันใช้เกิน

  Option 2 (Production): ใช้ Vertex AI พร้อม Billing
    → ดู references/billing-setup.md section "Vertex AI Setup"

  Option 3 (รอ Reset): Free Tier ของ Text Models Reset ทุกวัน
    แต่ Image Models = 0 ตลอด ถ้าไม่เปิด Billing

ค่าใช้จ่ายโดยประมาณ (Pay-as-you-go):
  - NB2 (Gemini 3.1 Flash Image): ~$0.04/ภาพ
  - Pro (Gemini 3 Pro Image):      ~$0.12/ภาพ
  - Flash 2.5 (Legacy):            ~$0.039/ภาพ

ลูกค้าธุรกิจ: เปิด Billing 1 ครั้งใช้ทั่วทุก Surface (Desktop, Cowork, Code CLI)
```

ดูรายละเอียดเต็มที่ `references/billing-setup.md` และ `references/troubleshooting-quota.md`

---

## STEP 2 — Image Generation Workflow (หลังผ่าน Pre-flight)

### Core Principle — Right Model, Right Specs, Right Output

ทุก `generate_image` ต้องคิด 3 มิติพร้อมกัน:

**1. Model Tier**
| Tier | model_tier | เมื่อใช้ | คุณภาพ | ความเร็ว | ราคา |
|---|---|---|---|---|---|
| Nano Banana 2 (Default) | `nb2` | งาน 80% — Marketing, Hero, Production | 4K | 2-4 วินาที | $$ |
| Nano Banana Pro | `pro` | งานซับซ้อน Multi-character, Cinematic | 4K Max | 5-8 วินาที | $$$ |
| Flash 2.5 (Legacy) | `flash` | Draft รัวๆ, Volume Generation | 1024px | 2-3 วินาที | $ |
| Auto | `auto` | ให้ Server เลือก (Default = NB2) | — | — | — |

**2. Aspect Ratio**
| Ratio | Use Case |
|---|---|
| `1:1` | Social Post, Profile, Icon, Logo |
| `16:9` | Slide Hero, YouTube Thumbnail, Web Banner |
| `9:16` | Mobile Story, Reel, Phone Wallpaper |
| `21:9` | Cinematic Banner, Website Hero (Ultra-wide) |
| `4:3` / `3:4` | Photo Print, Product Page |
| `4:5` / `5:4` | Instagram Portrait/Square+ |

**3. Output Path**
- File path เต็ม: `/Users/.../images/hero_V01R01.png` → Save ตามนั้น
- Directory (มี trailing slash): `/path/folder/` → Auto-naming ในโฟลเดอร์
- ละไว้: ใช้ `IMAGE_OUTPUT_DIR` env หรือ `~/nanobanana-images`

### 7-Step Workflow

เมื่อผู้ใช้ขอ "ทำภาพให้หน่อย":

0. **Pre-flight** — `show_output_stats` (Step 0 ข้างบน)
1. **Clarify Intent** — ใช้ที่ไหน? (Slide / Social / Print / Web)
2. **Select Model Tier** — nb2 Default, ใช้ Pro เฉพาะเมื่อต้อง Reasoning ลึก
3. **Set Specs** — Aspect Ratio + Resolution + Negative Prompt
4. **Compose Prompt** — ใช้ Pattern จาก `references/prompt-cookbook.md` (อ่านก่อนเขียน Prompt เอง)
5. **Specify Output Path** — ระบุชัดเพื่อให้ผู้ใช้หาเจอ
6. **Generate + Verify** — เรียก `generate_image` → ส่งคืน computer:// link

---

## MCP Tool Catalog | สรุปย่อ

รายละเอียดเต็มอยู่ที่ `references/mcp-functions.md`

**4 Tools:**
- `generate_image` — สร้างภาพใหม่ (mode=generate) หรือแก้ภาพ (mode=edit) — รองรับ Multi-image Conditioning (up to 3 input images)
- `upload_file` — Upload ภาพใหญ่ (>20MB) หรือใช้ซ้ำ เข้า Gemini Files API
- `maintenance` — cleanup_expired / cleanup_local / check_quota / database_hygiene / full_cleanup
- `show_output_stats` — สถิติโฟลเดอร์ Output (ใช้เป็น Pre-flight Probe)

**7 Resources:**
- `gemini://files/{name}` — File metadata
- `file://images` — รายการภาพทั้งหมด
- `file://images/{id}` — Full image
- `file://images/{id}/thumbnail` — Thumbnail
- `nano-banana://prompt-templates` — Template catalog
- `progress://operations/{id}` — Long-running status
- `progress://operations/list` — All operations

**6 Built-in Prompt Templates** (Server-side):
- Photography: `photorealistic_shot`
- Design: `logo_text`, `product_shot`, `sticker_flat`
- Editing: `iterative_edit_instruction`, `composition_and_style_transfer`

---

## Prompt Composition Standard

### Prompt Anatomy 6 ส่วน (ทำให้ภาพ Production-grade)

ทุก Prompt ที่ส่งให้ NB2/Pro ควรมี:

| ส่วน | คำอธิบาย | ตัวอย่าง |
|---|---|---|
| **Subject** | สิ่งหลักในภาพ | "A long-haired Persian cat with white-silver fur" |
| **Composition** | จัดวาง/มุมกล้อง | "sitting on a wooden windowsill, three-quarter view" |
| **Action/State** | กำลังทำอะไร | "gazing peacefully outside" |
| **Location/Setting** | ฉาก/พื้นหลัง | "warm cozy living room interior at sunset" |
| **Style/Lighting** | สไตล์ + แสง | "cinematic golden-hour lighting, shallow DOF, photorealistic" |
| **Negative/Constraints** | สิ่งที่ห้าม | (field `negative_prompt`) "no text, no watermark, no other animals" |

**Anti-pattern (อย่าทำ):**
- ❌ "วาดแมว" — Generic เกินไป
- ❌ "ภาพแมวสวยๆ" — ไม่มี Composition/Style

**Production-grade (ทำแบบนี้):**
- ✅ "A majestic long-haired Persian cat with luxurious white-silver fur, sitting on a wooden windowsill, three-quarter pose, gazing through a slightly open window at a golden sunset. Warm amber light streams through, illuminating the fur. Cozy interior with bokeh background. Photorealistic, cinematic, shallow depth of field, professional photography."

ดู Pattern เต็ม 30+ ใน `references/prompt-cookbook.md`

---

## Pre-flight Checklist for Image Request

ก่อนเรียก `generate_image` ตรวจ:
- [ ] Pre-flight Connection Test ผ่านแล้ว (Step 0)
- [ ] Billing เปิดแล้ว (ถ้าใช้ครั้งแรก) — ดู Scenario G
- [ ] Model Tier เลือกถูก (nb2 default พอสำหรับ 80% ของงาน)
- [ ] Aspect Ratio ตรงกับ Use Case
- [ ] Resolution พอเหมาะ (4K สำหรับ Print/Hero, 2K สำหรับ Web, 1K สำหรับ Thumbnail)
- [ ] Output Path ระบุชัด
- [ ] Prompt ครบ 6 ส่วน (Subject + Composition + Action + Setting + Style + Negative)
- [ ] (Edit) input_image_path_1 ชี้ไฟล์ที่มีอยู่จริง
- [ ] (Brand) System Instruction ระบุ Brand Color/Style

---

## Anti-patterns | สิ่งที่ห้ามทำ

1. **เรียก generate_image ก่อน Pre-flight** — เสียเวลา/Credit ฟรีๆ
2. **Default Output Path ตลอด** — ภาพกองที่ `~/nanobanana-images` ผู้ใช้หาไม่เจอ
3. **ใช้ Pro กับทุกงาน** — เปลือง $ มาก ใช้ nb2 ก่อน
4. **Prompt สั้น** — "ภาพแมว" ได้ผลแย่ ใช้ Prompt Anatomy 6 ส่วน
5. **Aspect Ratio ผิด Use Case** — Thumbnail YouTube ด้วย 1:1 = ไม่ Fit
6. **ไม่ใช้ built-in templates** — สำหรับ logo/product/sticker มี Server-side Template ใช้ก่อน
7. **Edit ภาพ >20MB โดยไม่ Upload** — Timeout
8. **ลืม cleanup** — รัน `maintenance cleanup_local` เป็นระยะ
9. **บอกผู้ใช้ว่า "Free Tier ใช้ได้"** — Image Models = 0 ใน Free Tier ต้องเปิด Billing

---

## Sensitive Content Guardrail

Nano Banana ใช้ Gemini ที่มี Built-in Safety Filter — ห้ามสร้าง:
- ภาพบุคคลจริงที่ไม่ยินยอม (Deepfake, Impersonation)
- Brand/Logo บริษัทอื่นที่อาจละเมิดเครื่องหมายการค้า
- NSFW, ความรุนแรง, สิ่งผิดกฎหมาย
- ภาพเด็กในบริบทไม่เหมาะสม

ถ้า Gemini Block ให้ปรับ Prompt ให้ Safe ขึ้น ไม่หาทาง Bypass

สำหรับงานลูกค้า:
- ตรวจ Brand Guidelines ก่อนใช้สี/Logo
- Output ใช้ตาม Google Gemini API Terms

---

## Output Format Standard | รูปแบบที่ส่งคืนผู้ใช้

**สร้างเสร็จ:**
```
✓ สร้างภาพเรียบร้อย
  Model:        [nb2 / pro / flash]
  Aspect Ratio: [1:1 / 16:9 / 9:16 / 21:9 / 4:3]
  Resolution:   [4k / 2k / 1k]
  Output:       computer:///absolute/path/to/image.png
  Generation:   N seconds
  Next Step:    [Iterate / Add to slide / Generate variations]
```

**แก้ภาพเสร็จ:**
```
✓ แก้ภาพเรียบร้อย
  Source:    computer:///original/path
  Output:    computer:///path/to/edited.png
  Edit:      [สรุปสิ่งที่เปลี่ยน]
  Model:     [model]
  Next Step: [Iterate / Final / Save]
```

**Pre-flight Fail:**
```
⚠ Nano Banana ยังไม่พร้อม
  Scenario:   [A / B / C / D / E / F / G]
  Diagnosis:  [สาเหตุที่ตรวจพบ]
  Recovery:   [Template ที่ตรง]
  Next Step:  [ขั้นแรกที่ผู้ใช้ต้องทำ]
```

---

## Reference Files

อ่านไฟล์เหล่านี้เมื่อต้องลงรายละเอียด — อย่าใช้ความจำลอยๆ:

| ไฟล์ | อ่านเมื่อ |
|---|---|
| `references/install-and-auth.md` | Setup ใหม่ / Troubleshoot Connection / Switch Auth Method |
| `references/mcp-functions.md` | ก่อนเรียก Tool จริง / ต้องการ Parameter Spec |
| `references/prompt-cookbook.md` | ก่อนเขียน Prompt — มี 30+ Pattern พร้อม Variable |
| `references/command-templates.md` | แปลคำสั่งภาษาไทยเป็น MCP Call |
| `references/use-cases.md` | แนะนำ Use Case + Model + Specs |
| `references/billing-setup.md` | เปิด Billing AI Studio หรือ Vertex AI |
| `references/troubleshooting-quota.md` | เจอ 429 / Quota Exhausted |
| `references/api-key-rotation.md` | เปลี่ยน Key (Manual หรือ Bundled Script) — 3 Methods พร้อม Verification |

## Bundled Scripts

| Script | Purpose |
|---|---|
| `scripts/rotate_api_key.sh` | One-script API Key Rotation ทำพร้อมกัน Desktop+Cowork+Code CLI (มี Key Test + Backup + Verification Hints) |

---

## Pairing with Other Skills

| สถานการณ์ | Skill ร่วม |
|---|---|
| Hero/Section Image ใน Slide Deck | + `b2b-presentation-creator` |
| Poster / Print Design | + `canvas-design` |
| Brand-aligned Visual | + `brand-guidelines` |
| Campaign Asset Series | + `marketing:content-creation` |
| Product Page / Spec Sheet | + `b2b-presentation-creator` |
| Workshop Mood Board | + `b2b-design-thinking` |

---

## Operating Modes

**Mode A — Generate** (สร้างภาพใหม่):
Pre-flight → Clarify → Select Specs → Compose Prompt → Generate → Return

**Mode B — Edit** (แก้ภาพเดิม):
Pre-flight → Identify Source → Plan Edit → Use `iterative_edit_instruction` → Edit → Iterate

**Mode C — Troubleshoot** (แก้ปัญหา Connection):
Pre-flight → Diagnose Scenario A-G → แสดง Recovery → Re-test → กลับไปทำงาน

**Mode D — Key Rotation** (เปลี่ยน Gemini API Key):
ตรวจสาเหตุ (รั่ว/ครบกำหนด/Compromise) → เตือนลบ Key เก่า → รัน `scripts/rotate_api_key.sh` →
อัปเดต Desktop+Cowork+Code CLI พร้อมกัน → Verify ที่ทุก Client → Functional Test

**เมื่อ Trigger Mode D:**
- ผู้ใช้พิมพ์ "เปลี่ยน API Key", "rotate key", "Key รั่ว", "change Gemini key"
- ตรวจพบ Scenario C (Auth Misconfigured) ระหว่าง Pre-flight แล้วผู้ใช้ยืนยันว่ามี Key ใหม่
- ผู้ใช้แชร์ Key เก่ามาในแชท (Auto-trigger Security Warning + แนะนำ Rotation ทันที)

**Workflow Mode D:**
1. ถาม: Key รั่วในที่ไหน? (เพื่อประเมินความเร่งด่วน + Audit Logs)
2. แนะนำให้ลบ Key เก่าที่ https://aistudio.google.com/apikey ก่อน
3. แนะนำให้สร้าง Key ใหม่ → Copy ไว้
4. รัน Script:
   ```bash
   bash ~/.claude/skills/nanobanana-connection/scripts/rotate_api_key.sh
   ```
   (หรือ Manual ตาม `references/api-key-rotation.md` Method 2/3 ถ้าต้องการแยก Client)
5. หลัง Script เสร็จ — ย้ำให้ Restart Desktop/Cowork (Cmd+Q) + Code CLI Session
6. Functional Test ด้วย Prompt เล็กๆ (ภาพ Icon 1k 1:1) ก่อนใช้งานจริง

ดูรายละเอียดเต็มที่ `references/api-key-rotation.md` (3 Methods + Pre-checklist + Verification + Security Best Practices + Rollback)

ทุกโหมดต้องคืนผลลัพธ์ใช้งานต่อได้ทันที (computer:// link + Path + Status)

---

**Version:** V02R02 | **Date:** 2026-05-25 | **Author:** Trusted Transformation Strategist

**Change Log V02R01 → V02R02:**
- เพิ่ม **Operating Mode D — Key Rotation** (Workflow ครบจาก Trigger ถึง Verification)
- เพิ่ม **Bundled Script** `scripts/rotate_api_key.sh` (One-script ทำ Desktop+Cowork+Code CLI พร้อมกัน + Key Test + Backup)
- เพิ่ม **Reference File** `references/api-key-rotation.md` (3 Methods + Lifecycle + Security + Rollback)
- เพิ่ม **Trigger Phrases** สำหรับ Key Rotation: "เปลี่ยน API Key", "rotate key", "Key รั่ว"
- Auto-trigger Mode D เมื่อตรวจพบผู้ใช้แชร์ Key ในแชท (Security Defense)

**Change Log V01R01 → V02R01:**
- เพิ่ม **Scenario G — Quota/Billing** (ปัญหาจริงที่เจอ: Free Tier = 0)
- เพิ่ม **Scenario D — uv/Path Fix** (Real Issue: Server Disconnected)
- เพิ่ม **Prompt Anatomy 6 ส่วน** + Pointer ไป `prompt-cookbook.md`
- เพิ่ม Client target: **Claude Desktop** (เดิมมีแค่ Cowork + Code CLI)
- ลด SKILL.md ขนาดลง ส่ง Detail ไป Reference Files (Progressive Disclosure)
