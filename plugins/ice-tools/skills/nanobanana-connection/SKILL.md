---
name: nanobanana-connection
description: เชื่อมต่อและสั่งงาน Gemini Image MCP Server (rlabs/gemini-mcp — Google Nano Banana Pro / gemini-3-pro-image-preview) จาก Claude Desktop, Cowork และ Code CLI. ใช้ทุกครั้งที่ผู้ใช้ต้องการ สร้างภาพ AI, แก้ภาพ, ทำ Logo, Hero Image, Product Shot, Thumbnail, Banner, Mockup, Sticker, Illustration, วิเคราะห์/อ่านภาพ (Vision), สร้างวิดีโอ (Veo), Setup/Troubleshoot Gemini MCP, หรือ เปลี่ยน/Rotate API Key. ครอบคลุม Pre-flight Connection Test (MCP+Auth+Billing), Prompt Cookbook ไทย-อังกฤษ 30+ Pattern, Aspect Ratio/Image Size, Session-based Multi-turn Editing, Image Analysis (Claude เห็นภาพ), Billing/Quota Recovery, และ API Key Rotation. Triggers ภาษาไทย — ทำภาพให้หน่อย, สร้างภาพ AI, วาด AI, ทำ hero/thumbnail/logo/product shot/banner/illustration, แก้ภาพนี้, สร้าง mockup, วิเคราะห์ภาพ, อ่านภาพนี้, ทำวิดีโอ, Nano Banana, Gemini image, เปลี่ยน API Key, rotate key, Key รั่ว. English — generate/edit/analyze image, create illustration/banner, AI image, nano banana, generate video, rotate API key, change Gemini key, leaked key. คู่กับ b2b-presentation-creator, canvas-design, brand-guidelines.
metadata:
  version: V03R01
  date: 2026-06-21
  author: Trusted Transformation Strategist
---

# Gemini Image Connection Skill — บูรณาการ Image Generation MCP (rlabs/gemini-mcp) กับ Claude

## Purpose | วัตถุประสงค์

ทำให้ผู้ใช้สั่งสร้างภาพ AI ผ่าน **rlabs/gemini-mcp** (`@rlabs-inc/gemini-mcp`, Server name = `gemini`, Default Model = Google Nano Banana Pro / `gemini-3-pro-image-preview`) จาก **Claude Desktop, Claude Cowork และ Claude Code CLI** ได้อย่างเป็นระบบ ครอบคลุมตั้งแต่การติดตั้ง การตรวจ Connection ก่อนใช้งาน การตั้งค่า Image Size/Aspect Ratio/Style การออกแบบ Prompt ที่ใช้งานได้จริง การแก้ภาพแบบ Session Multi-turn การให้ Claude วิเคราะห์ภาพ (Vision) ไปจนถึงการ Recovery เมื่อเจอ Billing/Auth Error

**Skill นี้แก้ปัญหา 6 ข้อ:**
1. ผู้ใช้ไม่รู้ว่า Gemini MCP มี Tool อะไรบ้าง สั่งงานอะไรได้แค่ไหน (Generate / Edit / Analyze / Video)
2. Auth Setup — rlabs ใช้ `GEMINI_API_KEY` อย่างเดียว แต่ผู้ใช้สับสนกับ Vertex AI ADC (rlabs **ไม่ใช้** Vertex)
3. **Free Tier ของ Gemini Image Generation = 0** (กับดักที่ผู้ใช้ใหม่เกือบทุกคนเจอ) — Skill นี้บังคับตรวจ Billing ใน Pre-flight
4. Token หาย/หมดอายุระหว่างทำงาน — Skill นี้บังคับ Pre-flight Test ก่อนทุกครั้ง
5. ไม่มี Convention การตั้ง Image Size (1K/2K/4K) และ Aspect Ratio ที่เหมาะกับงาน ทำให้สิ้นเปลือง Credit หรือคุณภาพไม่พอ
6. Prompt สั้นเกินไปได้ภาพ Generic — Skill นี้มี Prompt Cookbook 30+ Pattern พร้อม Variable

## When to Invoke | เมื่อใดควรใช้

ใช้ Skill นี้เมื่อผู้ใช้ต้องการ:
- สร้างภาพประกอบ: Hero Image, Section Cover, Thumbnail, Banner, Illustration
- ทำ Logo, Product Shot, Sticker, Mockup, Icon
- แก้ไขภาพเดิม: Iterative Edit, Composition Transfer, Style Transfer, Background Change (ผ่าน Session Multi-turn)
- **วิเคราะห์/อ่านภาพ** (Vision): ให้ Claude เห็นภาพ → อธิบาย / ตรวจ / Detect Object → Iterate Prompt ต่อ
- **สร้างวิดีโอสั้น** (Veo) จาก Prompt
- สร้าง Mood Board สำหรับ Workshop หรือ Design Sprint
- ทำภาพประกอบใน Proposal, Slide Deck, Marketing Campaign, Brand Asset
- Setup, Troubleshoot Gemini MCP
- **เปลี่ยน / Rotate Gemini API Key** (กรณี Key รั่ว, ครบกำหนด, หรือเปลี่ยน Environment) — ใช้ Bundle Script `scripts/rotate_api_key.sh` ทำพร้อมกันทุก Client

ห้ามใช้ Skill นี้ทำ:
- Algorithmic Art ที่ใช้ Code (ใช้ `algorithmic-art` แทน)
- Poster/Print Material ที่ต้องการ Vector Layout (ใช้ `canvas-design`)
- Diagram/Flowchart (ใช้ Mermaid หรือ `visualize`)
- OCR เฉพาะทาง / Document Parsing เชิงโครงสร้าง (ใช้ Tool เฉพาะทาง — `gemini-analyze-image` ทำ Vision ทั่วไปได้ แต่ไม่ใช่ OCR Engine)

---

## STEP 0 — Pre-flight Connection Test (บังคับทุกครั้ง)

**ห้ามข้าม. ทำก่อนเรียก `gemini-generate-image` ทุกครั้ง.**

เหตุผล: Gemini MCP ใช้ `GEMINI_API_KEY` ที่อยู่ใน MCP Config (env) หาก Skill ไม่ตรวจก่อน จะเกิด Failure Pattern: สั่งสร้างภาพ → Server ไม่ตอบ / 401 / 429 → ผู้ใช้รอเปล่า → เสียเวลา/Credit Pre-flight ใช้เวลาไม่กี่วินาที ป้องกันได้ทั้งหมด

> หมายเหตุ: rlabs/gemini-mcp **ไม่มี** Tool Local-only แบบ `show_output_stats` เดิม จึงใช้ Probe แบบ Lightweight แทน

### Pre-flight Sequence — 3 ขั้น

**ขั้นที่ 1 — Lightweight Probe**

เลือกหนึ่งวิธี (เรียงจากเบาไปหนัก):

1. **`gemini-list-image-sessions`** (เบาที่สุด, Local-ish) — ถ้า Tool ตอบกลับ (แม้ List ว่าง) = MCP Server `gemini` ขึ้นและ Config โหลดสำเร็จ
2. ถ้าต้องยืนยัน Auth/Billing จริง ให้สั่ง **Smoke Test** ด้วย `gemini-generate-image` แบบเล็กที่สุด — `imageSize: "1K"`, `aspectRatio: "1:1"`, Prompt สั้น (เช่น "a single grey circle on white") — ผ่าน = พร้อมใช้งานจริง

**ขั้นที่ 2 — ตีความผลลัพธ์**

| Result | สาเหตุ | ไปที่ Scenario |
|---|---|---|
| Session list ตอบ / Smoke image สำเร็จ | Server พร้อม + Config ถูก + Billing เปิด | ดำเนินงานต่อ (ข้ามไป Step 1) |
| `Tool not found` / MCP Server `gemini` หาไม่เจอ | MCP ยังไม่ Setup / ยังไม่ Restart Client | **Scenario A** |
| `GEMINI_API_KEY not set` / env ว่าง | ไม่มี API Key ใน Config | **Scenario B** |
| `auth` / `API key not valid` / `unauthorized` / `401` / `403` | Key หมดอายุ / ผิด / ถูก Revoke | **Scenario C** |
| `gemini-mcp: command not found` / Server failed to start / spawn ENOENT | Binary Path ผิด / ยังไม่ได้ Install | **Scenario D** |
| `429` / `RESOURCE_EXHAUSTED` / `quota` / `billing` | Billing ไม่เปิด (Image Gen ไม่อยู่ Free Tier) | **Scenario G** |
| Other unknown error | ไม่รู้ที่มา | **Scenario F** (Diagnostic) |

**ขั้นที่ 3 — Mid-task Auth/Quota Probe**

ถ้า Operation ใดตอบกลับด้วย Error ที่มีคำว่า `RESOURCE_EXHAUSTED`, `429`, `quota`, `billing` → กลับไป **Scenario G — Billing/Quota** ทันที (ดู `references/troubleshooting-quota.md`)

---

## STEP 1 — Recovery Scenarios

### Scenario A — MCP ยังไม่ Setup / ยังไม่ Restart Client
แสดงคำตอบนี้กับผู้ใช้:
```
ตรวจไม่พบ Gemini MCP (server: gemini) ในเครื่องของท่านครับ
อาจเป็นเพราะ (1) ยังไม่ติดตั้ง MCP Server หรือ (2) ติดตั้งแล้วแต่ยังไม่ Restart Client

หากยังไม่ติดตั้ง ดูคู่มือเต็ม: references/install-and-auth.md
หากติดตั้งแล้ว: ปิด Client สนิท (Cmd+Q) → เปิดใหม่ → ลองอีกครั้ง

ติดตั้งสั้นๆ:
  1. ขอ Gemini API Key ที่ https://aistudio.google.com/apikey
  2. เปิด Billing (Free Tier ไม่ครอบคลุม Image Generation)
  3. ติดตั้ง MCP: npm install -g @rlabs-inc/gemini-mcp
     (Binary จะอยู่ที่ /Users/xpickey/.hermes/node/bin/gemini-mcp)
  4. เพิ่ม Server ชื่อ "gemini" ใน Config ตาม Client ของท่าน (ดู references/install-and-auth.md)
```

### Scenario B — ไม่มี API Key
```
Config มี Server "gemini" แล้วแต่ไม่มี GEMINI_API_KEY ครับ

แก้ไข:
  1. ขอ Key ที่ https://aistudio.google.com/apikey
  2. ใส่ใน env ของ Server "gemini":
     - Claude Desktop/Cowork: ~/Library/Application Support/Claude/claude_desktop_config.json
     - Claude Code CLI: claude mcp remove gemini && claude mcp add gemini ...
     env ที่ต้องมี: GEMINI_API_KEY, GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview, GEMINI_OUTPUT_DIR=~/.local/share/gemini-mcp-images
  3. Restart Client (Cmd+Q แล้วเปิดใหม่)
```

### Scenario C — API Key หมดอายุ / ผิด
```
API Key มีอยู่ แต่ Gemini ปฏิเสธครับ (อาจหมดอายุ ถูก Revoke หรือพิมพ์ผิด)

แก้ไข:
  1. เปิด https://aistudio.google.com/apikey
  2. ตรวจ Key ที่ใช้ — ถ้า Revoke แล้ว → ลบทิ้ง + สร้างใหม่
  3. Update env GEMINI_API_KEY ใน Config ของ Server "gemini"
  4. Restart Client
```

### Scenario D — Binary/Path ผิด (Server Disconnected) ⭐ พบบ่อย
```
Server "gemini" Start ไม่ได้ครับ — ส่วนใหญ่เพราะ:

สาเหตุ 1: ยังไม่ได้ติดตั้ง Binary หรือ Path ใน command ผิด
  rlabs ใช้ Binary local ตรง ไม่ใช่ uv/npx:
    command: /Users/xpickey/.hermes/node/bin/gemini-mcp
  แก้: ติดตั้ง npm install -g @rlabs-inc/gemini-mcp แล้วชี้ command ไปที่ Binary path เต็ม

สาเหตุ 2: Claude Desktop (GUI App บน macOS) ไม่อ่าน ~/.zshrc
  แก้: ใช้ Full Path ของ Binary เสมอ (อย่าใช้ชื่อสั้น "gemini-mcp" ลอยๆ)
  ตรวจว่า Binary ไม่อยู่บน iCloud Drive (ต้องอยู่ Local เช่น ~/.hermes/...)

สาเหตุ 3: env ไม่ครบ
  แก้: ใส่ env ครบ — GEMINI_API_KEY, GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview,
       GEMINI_OUTPUT_DIR=~/.local/share/gemini-mcp-images

Config Template ที่ถูกต้องอยู่ที่ references/install-and-auth.md
```

### Scenario F — Unknown Error (Diagnostic Mode)
```
พบ Error ที่ไม่รู้ที่มาแน่ชัดครับ

Diagnostic 5 ขั้น:
  1. รัน Binary มือจาก Terminal เพื่อดู Error ตรงๆ:
     export GEMINI_API_KEY=<key>
     export GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview
     /Users/xpickey/.hermes/node/bin/gemini-mcp
     → ควรขึ้นเป็น MCP stdio server (รอ input) ถ้า Error จะแสดงทันที

  2. ตรวจ Log ของ Client:
     macOS: ~/Library/Logs/Claude/
     Look for: mcp-server-gemini.log

  3. ทดสอบด้วย MCP Inspector:
     npx @modelcontextprotocol/inspector /Users/xpickey/.hermes/node/bin/gemini-mcp

  4. ตรวจ Version: npm ls -g @rlabs-inc/gemini-mcp (ควร >= 0.8.1) / อัปเดต Client

  5. ส่ง Error เต็มให้ผม + ระบุขั้นที่ลองแล้ว
```

### Scenario G — Quota Exhausted / Billing ไม่เปิด ⭐ สำคัญที่สุด

**ข้อเท็จจริง: Gemini Image Models มี Free Tier Quota = 0**
ผู้ใช้ใหม่เกือบทุกคนเจอข้อนี้ครั้งแรก

```
ครับ Error 429 RESOURCE_EXHAUSTED — สาเหตุ: Image Generation ไม่อยู่ใน Free Tier ของ Gemini API

ทางเลือก:
  Option 1 (เร็วที่สุด): เปิด Billing ที่ AI Studio
    → https://aistudio.google.com/app/billing
    → Set up Billing → ใส่บัตรเครดิต
    → Key เดิมใช้ต่อได้ ไม่ต้องเปลี่ยน
    → ตั้ง Budget Alert ที่ $5-$10 ป้องกันใช้เกิน

  Option 2 (รอ Reset): Free Tier ของ Text Models Reset ทุกวัน
    แต่ Image Models = 0 ตลอด ถ้าไม่เปิด Billing

ค่าใช้จ่ายโดยประมาณ (Pay-as-you-go, Default = Nano Banana Pro):
  - gemini-3-pro-image-preview (Nano Banana Pro): ~$0.12/ภาพ ที่ 4K

ลูกค้าธุรกิจ: เปิด Billing 1 ครั้งใช้ทั่วทุก Surface (Desktop, Cowork, Code CLI)
```

ดูรายละเอียดเต็มที่ `references/billing-setup.md` และ `references/troubleshooting-quota.md`

---

## STEP 2 — Image Generation Workflow (หลังผ่าน Pre-flight)

### Core Principle — Right Specs, Right Style, Right Output

ทุก `gemini-generate-image` ต้องคิด 3 มิติพร้อมกัน:

**1. Image Size** (param `imageSize`)
| imageSize | เมื่อใช้ | หมายเหตุ |
|---|---|---|
| `1K` | Thumbnail, Icon, Draft รัวๆ, Smoke Test | เบา/ถูกที่สุด |
| `2K` (Default) | งาน 80% — Web, Social, Hero ทั่วไป | สมดุลคุณภาพ/ราคา |
| `4K` | Print, Hero Ultra-detail, งานคุณภาพสูง | ราคาสูงสุด (~$0.12/ภาพ) |

> rlabs **ไม่มี** `model_tier` (nb2/pro/flash) แล้ว — Model ถูก Fix ที่ `gemini-3-pro-image-preview` (Nano Banana Pro) ผ่าน env. ควบคุมคุณภาพ/ราคาด้วย `imageSize` แทน

**2. Aspect Ratio** (param `aspectRatio`)
| Ratio | Use Case |
|---|---|
| `1:1` | Social Post, Profile, Icon, Logo |
| `16:9` | Slide Hero, YouTube Thumbnail, Web Banner |
| `9:16` | Mobile Story, Reel, Phone Wallpaper |
| `21:9` | Cinematic Banner, Website Hero (Ultra-wide) |
| `4:3` / `3:4` | Photo Print, Product Page |
| `4:5` / `5:4` | Instagram Portrait / Square+ |
| `2:3` / `3:2` | Editorial, Poster, Classic Photo |

**3. Style** (param `style` — เป็น Param แยก ไม่ฝังใน Prompt)
- ตัวอย่าง: `"photorealistic"`, `"watercolor"`, `"anime"`, `"3d render"`, `"line art"`, `"oil painting"`
- ใส่ Style ทาง Param ทำให้ Prompt สะอาด โฟกัสที่เนื้อหา

> **Output:** ภาพ Save ลง `GEMINI_OUTPUT_DIR` (`~/.local/share/gemini-mcp-images`) **อัตโนมัติ** — rlabs **ไม่มี** `output_path` param. ถ้าผู้ใช้ต้องการไฟล์ในโฟลเดอร์เฉพาะ ให้ Generate ก่อนแล้วใช้ Bash `cp`/`mv` ย้ายไป Path ที่ต้องการ (แจ้ง Path ปลายทางให้ผู้ใช้)

### 6-Step Workflow

เมื่อผู้ใช้ขอ "ทำภาพให้หน่อย":

0. **Pre-flight** — Probe `gemini-list-image-sessions` (Step 0 ข้างบน)
1. **Clarify Intent** — ใช้ที่ไหน? (Slide / Social / Print / Web)
2. **Set Specs** — `imageSize` (2K default) + `aspectRatio` + `style`
3. **Compose Prompt** — ใช้ Pattern จาก `references/prompt-cookbook.md` (อ่านก่อนเขียน Prompt เอง). ถ้าผู้ใช้ให้ Brief สั้น ใช้ `gemini-image-prompt` ช่วยร่าง Prompt ก่อน
4. **Generate** — เรียก `gemini-generate-image` → ภาพ Save ลง `GEMINI_OUTPUT_DIR`
5. **Verify (Optional but recommended)** — เรียก `gemini-analyze-image` บนไฟล์ที่เพิ่งสร้าง เพื่อให้ Claude "เห็น" ว่าภาพตรง Brief ไหม → ถ้าไม่ตรง Iterate ผ่าน Edit Session
6. **Return** — แจ้ง Path ไฟล์ + สรุป Specs + Next Step ให้ผู้ใช้

---

## MCP Tool Catalog | สรุปย่อ (server: `gemini`, prefix `mcp__gemini__`)

รายละเอียดเต็มอยู่ที่ `references/mcp-functions.md`

**Image Generation & Prompt:**
- `gemini-generate-image(prompt*, style, aspectRatio, imageSize, useGoogleSearch)` — สร้างภาพใหม่ (Save ลง GEMINI_OUTPUT_DIR อัตโนมัติ). `imageSize` = `1K`/`2K`/`4K`. `useGoogleSearch` = ดึงข้อมูลจริงมาประกอบภาพ (เช่น Landmark/Brand ที่มีอยู่จริง)
- `gemini-image-prompt(description*, style, mood, details)` — ช่วยร่าง Prompt คุณภาพสูงจาก Brief สั้น ก่อนส่งเข้า generate

**Session-based Editing (Multi-turn):**
- `gemini-start-image-edit(prompt*, aspectRatio, imageSize, useGoogleSearch)` → คืน **`sessionId`** + ภาพ Base
- `gemini-continue-image-edit(sessionId*, prompt*)` — แก้ภาพต่อใน Session เดิม (เช่น "make it warmer", "remove the cup") เรียกซ้ำได้หลายรอบ
- `gemini-end-image-edit(sessionId*)` — ปิด Session เมื่อพอใจ
- `gemini-list-image-sessions()` — ดู Session ที่เปิดอยู่ (ใช้เป็น Pre-flight Probe ด้วย)

**Vision & Video:**
- `gemini-analyze-image(imagePath*, query, detectObjects, model, thinkingLevel)` — Claude วิเคราะห์/อ่าน/อธิบายภาพ + Detect Object (Feature ใหม่ที่ของเดิมไม่มี — ใช้ Verify ผลงานหรืออ่านภาพอ้างอิง)
- `gemini-generate-video(prompt*, aspectRatio, negativePrompt)` — สร้างวิดีโอสั้นด้วย Veo (`negativePrompt` เฉพาะ Video เท่านั้น)

> **ของเดิมที่ไม่มีแล้วใน rlabs (อย่าเรียก):** `show_output_stats`, `maintenance`, `upload_file`, และ Param `model_tier` / `output_path` / `negative_prompt` (สำหรับภาพ) / `n` / `mode=edit` / `input_image_path`. การแก้ภาพทำผ่าน **Session** เท่านั้น (ไม่ใช่ one-shot mode=edit)

---

## Prompt Composition Standard

### Prompt Anatomy 5 ส่วน + Style Param (ทำให้ภาพ Production-grade)

ทุก Prompt ที่ส่งให้ `gemini-generate-image` ควรมี (Style แยกไปไว้ใน Param `style`):

| ส่วน | คำอธิบาย | ตัวอย่าง | ไปไว้ที่ |
|---|---|---|---|
| **Subject** | สิ่งหลักในภาพ | "A long-haired Persian cat with white-silver fur" | prompt |
| **Composition** | จัดวาง/มุมกล้อง | "sitting on a wooden windowsill, three-quarter view" | prompt |
| **Action/State** | กำลังทำอะไร | "gazing peacefully outside" | prompt |
| **Location/Setting** | ฉาก/พื้นหลัง | "warm cozy living room interior at sunset" | prompt |
| **Lighting/Detail** | แสง + รายละเอียด | "cinematic golden-hour lighting, shallow DOF" | prompt |
| **Style** | สไตล์โดยรวม | `"photorealistic"` | **param `style`** |

> rlabs ภาพ **ไม่มี** `negative_prompt` — สิ่งที่ไม่ต้องการให้เขียนเป็น Positive Constraint ใน prompt แทน (เช่น "clean plain background, no other objects") หรือถ้าต้อง Remove จริงให้ใช้ Edit Session ("remove the watermark"). `negativePrompt` มีเฉพาะใน `gemini-generate-video`

**Anti-pattern (อย่าทำ):**
- ❌ "วาดแมว" — Generic เกินไป
- ❌ "ภาพแมวสวยๆ" — ไม่มี Composition/Lighting

**Production-grade (ทำแบบนี้):**
- ✅ prompt: "A majestic long-haired Persian cat with luxurious white-silver fur, sitting on a wooden windowsill, three-quarter pose, gazing through a slightly open window at a golden sunset. Warm amber light streams through, illuminating the fur. Cozy interior with soft bokeh background, shallow depth of field, professional photography." + `style: "photorealistic"` + `aspectRatio: "16:9"` + `imageSize: "2K"`

ดู Pattern เต็ม 30+ ใน `references/prompt-cookbook.md`

---

## Pre-flight Checklist for Image Request

ก่อนเรียก `gemini-generate-image` ตรวจ:
- [ ] Pre-flight Connection Test ผ่านแล้ว (Step 0)
- [ ] Billing เปิดแล้ว (ถ้าใช้ครั้งแรก) — ดู Scenario G
- [ ] `imageSize` เลือกถูก (2K default พอสำหรับ 80% ของงาน, 4K สำหรับ Print/Hero, 1K สำหรับ Thumbnail/Draft)
- [ ] `aspectRatio` ตรงกับ Use Case
- [ ] `style` ระบุชัด (param แยก) ตรงกับ Mood ที่ต้องการ
- [ ] Prompt ครบ 5 ส่วน (Subject + Composition + Action + Setting + Lighting)
- [ ] (Edit) ใช้ Session Flow: start → continue → end (ไม่มี one-shot mode=edit)
- [ ] (Brand) ระบุ Brand Color/Style ใน prompt + อาจ Verify ด้วย `gemini-analyze-image`
- [ ] (ต้องการไฟล์ในโฟลเดอร์เฉพาะ) วางแผน cp/mv จาก GEMINI_OUTPUT_DIR ไป Path ปลายทาง

---

## Anti-patterns | สิ่งที่ห้ามทำ

1. **เรียก `gemini-generate-image` ก่อน Pre-flight** — เสียเวลา/Credit ฟรีๆ
2. **เรียก Tool เก่าที่ไม่มีแล้ว** — `show_output_stats` / `maintenance` / `upload_file` / `generate_image` (ของ nanobanana เดิม) จะ Error เสมอ ใช้ชื่อ rlabs (`gemini-*`)
3. **ส่ง `model_tier` / `output_path` / `negative_prompt` ให้ภาพ** — Param เหล่านี้ไม่มีใน rlabs schema จะ Error
4. **ใช้ 4K กับทุกงาน** — เปลือง $ มาก ใช้ 2K ก่อน (Default)
5. **Prompt สั้น** — "ภาพแมว" ได้ผลแย่ ใช้ Prompt Anatomy 5 ส่วน + `style` param
6. **Aspect Ratio ผิด Use Case** — Thumbnail YouTube ด้วย 1:1 = ไม่ Fit
7. **แก้ภาพแบบ one-shot** — rlabs ใช้ Session: start → continue (ซ้ำได้) → end. ลืม `gemini-end-image-edit` = Session ค้าง (ตรวจด้วย `gemini-list-image-sessions`)
8. **บอกผู้ใช้ว่า "Free Tier ใช้ได้"** — Image Models = 0 ใน Free Tier ต้องเปิด Billing
9. **บอกว่าตั้ง `output_path` ได้** — ภาพไปที่ GEMINI_OUTPUT_DIR เสมอ ต้อง cp/mv เองถ้าต้องการที่อื่น

---

## Sensitive Content Guardrail

Gemini มี Built-in Safety Filter — ห้ามสร้าง:
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
  Model:        gemini-3-pro-image-preview (Nano Banana Pro)
  Image Size:   [1K / 2K / 4K]
  Aspect Ratio: [1:1 / 16:9 / 9:16 / 21:9 / 4:3 ...]
  Style:        [photorealistic / watercolor / ...]
  Saved to:     ~/.local/share/gemini-mcp-images/<filename>.png
  Next Step:    [Verify ด้วย analyze-image / Edit Session / ย้ายไฟล์ไปโฟลเดอร์งาน]
```

**แก้ภาพ (Session) เสร็จ:**
```
✓ แก้ภาพเรียบร้อย
  Session:   <sessionId>
  Edit:      [สรุปสิ่งที่เปลี่ยนในรอบนี้]
  Saved to:  ~/.local/share/gemini-mcp-images/<filename>.png
  Status:    [Session ยังเปิด — continue ได้ / ปิดแล้วด้วย end-image-edit]
  Next Step: [Continue edit / End session / Verify]
```

**วิเคราะห์ภาพเสร็จ (Vision):**
```
✓ วิเคราะห์ภาพเรียบร้อย
  Source:   <imagePath>
  Findings: [สรุปสิ่งที่ Claude เห็น / Object ที่ Detect]
  Next Step: [Iterate prompt / ใช้ภาพต่อ]
```

**Pre-flight Fail:**
```
⚠ Gemini MCP ยังไม่พร้อม
  Scenario:   [A / B / C / D / F / G]
  Diagnosis:  [สาเหตุที่ตรวจพบ]
  Recovery:   [Template ที่ตรง]
  Next Step:  [ขั้นแรกที่ผู้ใช้ต้องทำ]
```

---

## Reference Files

อ่านไฟล์เหล่านี้เมื่อต้องลงรายละเอียด — อย่าใช้ความจำลอยๆ:

| ไฟล์ | อ่านเมื่อ |
|---|---|
| `references/install-and-auth.md` | Setup ใหม่ (npm install -g + Binary path) / Troubleshoot Connection |
| `references/mcp-functions.md` | ก่อนเรียก Tool จริง / ต้องการ Parameter Spec ของ rlabs |
| `references/prompt-cookbook.md` | ก่อนเขียน Prompt — มี 30+ Pattern พร้อม Variable |
| `references/command-templates.md` | แปลคำสั่งภาษาไทยเป็น MCP Call (rlabs syntax) |
| `references/use-cases.md` | แนะนำ Use Case + imageSize + aspectRatio + style |
| `references/billing-setup.md` | เปิด Billing ที่ AI Studio |
| `references/troubleshooting-quota.md` | เจอ 429 / Quota Exhausted |
| `references/api-key-rotation.md` | เปลี่ยน Key (Manual หรือ Bundled Script) — พร้อม Verification |

## Bundled Scripts

| Script | Purpose |
|---|---|
| `scripts/rotate_api_key.sh` | One-script API Key Rotation อัปเดต env `GEMINI_API_KEY` ของ Server `gemini` พร้อมกัน Desktop+Cowork+Code CLI (มี Key Test + Backup + Verification Hints) |

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
Pre-flight → Clarify → Set Specs (imageSize/aspectRatio/style) → Compose Prompt → `gemini-generate-image` → (Optional) Verify ด้วย `gemini-analyze-image` → Return

**Mode B — Edit (Session Multi-turn)** (แก้ภาพเดิม):
Pre-flight → `gemini-start-image-edit(prompt)` → ได้ sessionId + Base → `gemini-continue-image-edit(sessionId, "...")` ซ้ำจนพอใจ → `gemini-end-image-edit(sessionId)` → Return
(ตรวจ Session ค้างด้วย `gemini-list-image-sessions`)

**Mode C — Analyze / Vision** (อ่าน/ตรวจภาพ):
Pre-flight → `gemini-analyze-image(imagePath, query, detectObjects)` → สรุปสิ่งที่เห็น → (ถ้าต่อยอด) เข้า Mode A/B เพื่อ Iterate

**Mode D — Video** (สร้างวิดีโอ Veo):
Pre-flight → Clarify → `gemini-generate-video(prompt, aspectRatio, negativePrompt)` → Return

**Mode E — Troubleshoot** (แก้ปัญหา Connection):
Pre-flight → Diagnose Scenario A/B/C/D/F/G → แสดง Recovery → Re-test → กลับไปทำงาน

**Mode F — Key Rotation** (เปลี่ยน Gemini API Key):
ตรวจสาเหตุ (รั่ว/ครบกำหนด/Compromise) → เตือนลบ Key เก่า → รัน `scripts/rotate_api_key.sh` →
อัปเดต env `GEMINI_API_KEY` ของ Server `gemini` ทั้ง Desktop+Cowork+Code CLI พร้อมกัน → Verify ที่ทุก Client → Functional Test

**เมื่อ Trigger Mode F:**
- ผู้ใช้พิมพ์ "เปลี่ยน API Key", "rotate key", "Key รั่ว", "change Gemini key"
- ตรวจพบ Scenario C (Auth Misconfigured) ระหว่าง Pre-flight แล้วผู้ใช้ยืนยันว่ามี Key ใหม่
- ผู้ใช้แชร์ Key เก่ามาในแชท (Auto-trigger Security Warning + แนะนำ Rotation ทันที)

**Workflow Mode F:**
1. ถาม: Key รั่วในที่ไหน? (เพื่อประเมินความเร่งด่วน + Audit Logs)
2. แนะนำให้ลบ Key เก่าที่ https://aistudio.google.com/apikey ก่อน
3. แนะนำให้สร้าง Key ใหม่ → Copy ไว้
4. รัน Script:
   ```bash
   bash ~/.claude/plugins/marketplaces/ice-skills/plugins/ice-tools/skills/nanobanana-connection/scripts/rotate_api_key.sh
   ```
   (หรือ Manual แก้ env `GEMINI_API_KEY` ใน Config แต่ละ Client ตาม `references/api-key-rotation.md`)
5. หลัง Script เสร็จ — ย้ำให้ Restart Desktop/Cowork (Cmd+Q) + Code CLI Session
6. Functional Test ด้วย Smoke Image (1K, 1:1, Prompt สั้น) ก่อนใช้งานจริง

ดูรายละเอียดเต็มที่ `references/api-key-rotation.md` (Methods + Pre-checklist + Verification + Security Best Practices + Rollback)

ทุกโหมดต้องคืนผลลัพธ์ใช้งานต่อได้ทันที (Saved Path + Specs + Status + Next Step)

---

**Version:** V03R01 | **Date:** 2026-06-21 | **Author:** Trusted Transformation Strategist

**Change Log V02R02 → V03R01 — Migration to rlabs/gemini-mcp (`@rlabs-inc/gemini-mcp` v0.8.1):**
- **เปลี่ยน MCP Backend ทั้งหมด** จาก nanobanana MCP → rlabs/gemini-mcp. Server name `nanobanana` → `gemini`. Tool prefix → `mcp__gemini__`
- **Tool ใหม่:** `gemini-generate-image` (param: prompt/style/aspectRatio/imageSize/useGoogleSearch), `gemini-image-prompt`, Session-based edit (`gemini-start-image-edit` / `gemini-continue-image-edit` / `gemini-end-image-edit` / `gemini-list-image-sessions`), และ Feature ใหม่ **`gemini-analyze-image`** (Vision — Claude เห็นภาพ) + `gemini-generate-video` (Veo)
- **ลบ:** `show_output_stats`, `maintenance`, `upload_file`, และ Param `model_tier` (nb2/pro/flash) / `output_path` / `negative_prompt` (image) / `n` / `mode=edit` / `input_image_path`
- **ลบ Vertex AI / uv / uvx config** (Scenario E เดิม) — rlabs ใช้ `GEMINI_API_KEY` อย่างเดียว, ติดตั้งด้วย `npm install -g` + Binary path `/Users/xpickey/.hermes/node/bin/gemini-mcp`
- **เปลี่ยน Quality Control:** จาก `model_tier` → `imageSize` (1K/2K/4K). Default Model Fix ที่ `gemini-3-pro-image-preview` (Nano Banana Pro, ~$0.12/ภาพ ที่ 4K) ผ่าน env
- **Pre-flight ใหม่:** ใช้ `gemini-list-image-sessions` + Smoke Image แทน `show_output_stats`
- **Edit Workflow ใหม่:** one-shot mode=edit → Session Multi-turn (start → continue ซ้ำได้ → end)
- คงไว้: ชื่อ Skill (`nanobanana-connection`), โครงสร้าง Heading, Prompt Cookbook, Use Cases, Thai/English Triggers, Billing Recovery, API Key Rotation

**Change Log V02R01 → V02R02 (Legacy):**
- เพิ่ม Operating Mode — Key Rotation + Bundled Script `scripts/rotate_api_key.sh` + Reference `references/api-key-rotation.md`
- Auto-trigger Key Rotation เมื่อตรวจพบผู้ใช้แชร์ Key ในแชท (Security Defense)
