# MCP Function Reference — Gemini (rlabs/gemini-mcp)

Complete catalog ของ Tools และ Resources สำหรับ MCP server `gemini` (`@rlabs-inc/gemini-mcp` v0.8.1).

> **Migration note (2026-06-21):** Skill นี้ย้ายจาก Nano Banana MCP เดิม มาใช้ **rlabs/gemini-mcp** แทนทั้งหมด. ทุก tool ใช้ prefix `mcp__gemini__` และพึ่ง `GEMINI_API_KEY` อย่างเดียว (ไม่มี Vertex AI / ADC). Default image model คือ **Nano Banana Pro** (`gemini-3-pro-image-preview`).

## Tools (8)

ภาพรวม: 6 tools สำหรับ image (generate / prompt-assist / 3 tools สำหรับ session edit / list session), 1 tool สำหรับ image analysis, 1 tool สำหรับ video.

| # | Tool | บทบาท |
|---|---|---|
| 1 | `gemini-generate-image` | สร้างภาพใหม่ (one-shot) |
| 2 | `gemini-image-prompt` | ช่วยร่าง prompt ก่อน generate |
| 3 | `gemini-start-image-edit` | เปิด session แก้ภาพ → คืน `sessionId` + ภาพ base |
| 4 | `gemini-continue-image-edit` | แก้ภาพต่อใน session (multi-turn) |
| 5 | `gemini-end-image-edit` | ปิด session |
| 6 | `gemini-list-image-sessions` | ดู session ที่เปิดอยู่ |
| 7 | `gemini-analyze-image` | ให้ Claude วิเคราะห์/มองเห็นภาพ |
| 8 | `gemini-generate-video` | สร้างวิดีโอ (Veo) |

---

### 1. `gemini-generate-image`

สร้างภาพใหม่แบบ one-shot. ภาพจะถูก save ลง `GEMINI_OUTPUT_DIR` โดยอัตโนมัติ (default `~/.local/share/gemini-mcp-images`) — ไม่มี output path parameter ให้ระบุปลายทางเอง.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `prompt` | string | (required) | Image prompt — ดู Prompt Anatomy 6 ส่วน |
| `style` | string | null | Style แยกออกจาก prompt เช่น `photorealistic`, `watercolor`, `anime`, `oil painting`, `3d render` |
| `aspectRatio` | string | null | `1:1`, `16:9`, `9:16`, `21:9`, `4:3`, `3:4`, `4:5`, `5:4`, `2:3`, `3:2` |
| `imageSize` | string | `2K` | `1K` / `2K` / `4K` (ไม่ใช่ model tier — เป็นความละเอียดล้วน) |
| `useGoogleSearch` | bool | false | เปิด Google Search grounding เพื่อให้ภาพอ้างข้อเท็จจริงปัจจุบันได้ |

**ข้อสังเกตสำคัญ:**
- **ไม่มี** `output_path` — ภาพไป `GEMINI_OUTPUT_DIR` เสมอ. ถ้าต้องการเก็บที่อื่น ให้ copy/move ไฟล์หลัง generate ด้วยเครื่องมือ filesystem ปกติ.
- **ไม่มี** `model_tier`, `negative_prompt`, `n` (batch), `mode` — feature เหล่านี้ของ Nano Banana เดิมไม่มีใน rlabs.
- `style` เป็น parameter แยก ไม่ต้องฝัง style ลงใน prompt (แม้ใส่ใน prompt ก็ทำงานได้ แต่ใช้ `style` ชัดเจนกว่า).
- ความละเอียดสูงขึ้น (`4K`) = ราคาต่อภาพสูงขึ้น (~$0.12/ภาพ ที่ 4K บน Nano Banana Pro).

**Examples:**
```text
# Basic Generate (default 2K)
gemini-generate-image(
    prompt="A red apple on white background, studio product photo",
    aspectRatio="1:1"
)

# Photorealistic, style แยก
gemini-generate-image(
    prompt="Bowl of ramen with soft-boiled egg, steam rising, dark wooden table",
    style="photorealistic",
    aspectRatio="3:2"
)

# 4K Cinematic + grounding (อ้างข้อเท็จจริงปัจจุบัน)
gemini-generate-image(
    prompt="Cinematic wide shot of a modern Bangkok skyline at golden hour",
    style="photorealistic",
    aspectRatio="21:9",
    imageSize="4K",
    useGoogleSearch=true
)
```

---

### 2. `gemini-image-prompt`

ช่วยร่าง/ขัดเกลา image prompt ก่อนส่งเข้า `gemini-generate-image`. ใช้เมื่อ user ให้ idea หลวมๆ แล้วต้องการ prompt ที่โครงสร้างครบ.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `description` | string | (required) | คำอธิบายภาพที่อยากได้ (หยาบๆ ได้) |
| `style` | string | null | Style ที่ต้องการ เช่น `cinematic`, `flat illustration` |
| `mood` | string | null | อารมณ์/บรรยากาศ เช่น `warm`, `dramatic`, `minimal` |
| `details` | string | null | รายละเอียดเสริม (lighting, composition, props) |

**Returns:** prompt ที่ขัดเกลาแล้ว — นำไปวางต่อใน `gemini-generate-image(prompt=...)`.

**ใช้เมื่อ:** brief ยังไม่ชัด, ต้องการ prompt คุณภาพสูงโดยไม่ต้องเขียน 6 ส่วนเองทั้งหมด, หรืออยากให้ Claude เสนอ prompt หลายแนวให้เลือก.

---

### 3. `gemini-start-image-edit`

เปิด **session การแก้ภาพแบบ multi-turn**. คืน `sessionId` พร้อมภาพ base ตัวแรก. เป็นจุดเริ่มของ workflow แก้ภาพแบบต่อเนื่อง — แทนที่ Nano Banana mode=edit แบบ one-shot เดิม.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `prompt` | string | (required) | Prompt ภาพตั้งต้นของ session |
| `aspectRatio` | string | null | สัดส่วนภาพ (ค่าเดียวกับ generate-image) |
| `imageSize` | string | `2K` | `1K` / `2K` / `4K` |
| `useGoogleSearch` | bool | false | Google Search grounding |

**Returns:** `sessionId` (ใช้ส่งต่อให้ `gemini-continue-image-edit` และ `gemini-end-image-edit`) + ภาพ base.

---

### 4. `gemini-continue-image-edit`

แก้ภาพต่อภายใน session เดิม. เรียกซ้ำได้หลายรอบเพื่อ iterate ทีละขั้น (เช่น ปรับแสง → เปลี่ยน background → เพิ่ม element). แต่ละครั้งภาพใหม่ save ลง `GEMINI_OUTPUT_DIR`.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `sessionId` | string | (required) | ID จาก `gemini-start-image-edit` |
| `prompt` | string | (required) | คำสั่งแก้ไขรอบนี้ เช่น `make the lighting warmer`, `change background to ocean sunset` |

---

### 5. `gemini-end-image-edit`

ปิด session การแก้ภาพ. ควรเรียกเมื่อแก้เสร็จ เพื่อปล่อย resource ของ session.

**Parameters:**
| Parameter | Type | Description |
|---|---|---|
| `sessionId` | string | (required) ID ของ session ที่จะปิด |

---

### 6. `gemini-list-image-sessions`

แสดงรายการ session แก้ภาพที่ยังเปิดอยู่. ใช้เป็น **Pre-flight / housekeeping probe** — เช็คได้ว่ามี session ค้างอยู่หรือไม่ และ MCP server ตอบสนองปกติ (แทน `show_output_stats` เดิมของ Nano Banana ที่ไม่มีใน rlabs).

**No Parameters**

**ใช้เมื่อ:**
- ตรวจว่า MCP `gemini` ทำงาน/ตอบสนองอยู่ (lightweight probe)
- หา `sessionId` ที่ลืม end ไว้ → เรียก `gemini-end-image-edit` เก็บกวาด
- ก่อนเริ่ม edit ใหม่ เพื่อไม่ให้ session ค้างสะสม

> **หมายเหตุ Pre-flight:** rlabs ไม่มี `show_output_stats` แบบ Nano Banana เดิม. ถ้าต้องการยืนยันว่า generation ใช้งานได้จริง (เช่น billing เปิดแล้ว) ให้ลองเรียก `gemini-generate-image` ภาพเล็ก (`imageSize="1K"`) หนึ่งครั้ง หรือใช้ `gemini-list-image-sessions` เป็น health-check เบาๆ.

---

### 7. `gemini-analyze-image`

ให้ Claude **วิเคราะห์/มองเห็นภาพ** ที่มีอยู่ — feature ใหม่ที่ Nano Banana เดิมไม่มี. ใช้ปิด loop "สร้าง → ดู → ปรับ": generate ภาพ → analyze ว่าตรงโจทย์ไหม → continue-edit แก้จุดที่ยังไม่ใช่.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `imagePath` | string | (required) | Path ของไฟล์ภาพที่จะวิเคราะห์ (เช่น ภาพใน `GEMINI_OUTPUT_DIR`) |
| `query` | string | null | คำถามเฉพาะ เช่น `Does this match a corporate, minimal style?` |
| `detectObjects` | bool | false | ตรวจจับ/แจกแจง object ในภาพ |
| `model` | string | null | ระบุ model ที่ใช้วิเคราะห์ (ถ้าต้องการ override default) |
| `thinkingLevel` | string | null | ระดับการคิด เช่น `low` / `high` สำหรับการวิเคราะห์ที่ละเอียดขึ้น |

**ใช้เมื่อ:**
- ตรวจว่าภาพที่ generate ตรงกับ brief หรือไม่ ก่อนส่งต่อ
- อ่าน/สรุปเนื้อหาภาพที่ user ส่งมา (เช่น ภาพ reference, screenshot)
- ป้อนผลวิเคราะห์กลับเข้า `gemini-continue-image-edit` เพื่อ iterate อย่างมีทิศทาง

---

### 8. `gemini-generate-video`

สร้างวิดีโอด้วย Veo. วิดีโอ save ลง `GEMINI_OUTPUT_DIR` เช่นเดียวกับภาพ.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `prompt` | string | (required) | คำอธิบายวิดีโอที่ต้องการ |
| `aspectRatio` | string | null | สัดส่วนวิดีโอ เช่น `16:9`, `9:16` |
| `negativePrompt` | string | null | สิ่งที่ห้ามให้ปรากฏในวิดีโอ |

> **หมายเหตุ:** `negativePrompt` มีเฉพาะใน video tool — image generation ของ rlabs ไม่มี negative prompt.

---

## Edit Workflow — Session-based (ต่างจาก Nano Banana เดิม)

Nano Banana เดิม: `generate_image(mode=edit, input_image_path_1=...)` — แก้แบบ one-shot ครั้งเดียว.

rlabs ใหม่ใช้ session แบบ multi-turn:

```text
# 1) เปิด session — ได้ภาพ base + sessionId
gemini-start-image-edit(
    prompt="Corporate headshot of a Thai businesswoman, neutral grey background",
    aspectRatio="4:5",
    imageSize="2K"
)
# → sessionId = "sess_abc123"

# 2) แก้ต่อทีละขั้น (เรียกซ้ำได้)
gemini-continue-image-edit(sessionId="sess_abc123", prompt="make the lighting warmer")
gemini-continue-image-edit(sessionId="sess_abc123", prompt="change background to soft office bokeh")

# 3) (ทางเลือก) ตรวจผลก่อนปิด
gemini-analyze-image(
    imagePath="~/.local/share/gemini-mcp-images/<latest>.png",
    query="Is this warm, professional, and corporate-appropriate?"
)

# 4) ปิด session
gemini-end-image-edit(sessionId="sess_abc123")
```

**Iterate loop ที่แนะนำ:** `start-image-edit` → `continue-image-edit` → `analyze-image` (ตรวจ) → `continue-image-edit` (แก้ตามผลตรวจ) → `end-image-edit`.

---

## Resources

| URI | Returns |
|---|---|
| `file://images` | รายการภาพที่ generate ไว้ใน `GEMINI_OUTPUT_DIR` |
| `file://images/{id}` | Full image |

> ภาพและวิดีโอทั้งหมด save อัตโนมัติลง `GEMINI_OUTPUT_DIR` (default `~/.local/share/gemini-mcp-images`). ไม่มี Files API / upload resource แยกแบบ Nano Banana เดิม.

---

## Prompt Patterns (ยังใช้ได้ — ปรับ syntax เป็น rlabs)

แนวทางการเขียน prompt ที่ดียังเหมือนเดิม. ความแตกต่างคือ **ย้าย style ออกมาเป็น parameter** และไม่มี template registry ฝั่ง server — Claude ประกอบ prompt + เลือก `style`/`aspectRatio` ให้เอง.

### Photography
- **Subject + Lighting + Composition** ใน `prompt`, ตั้ง `style="photorealistic"`.
  เช่น: `prompt="A single ceramic coffee cup on marble counter, soft window light from left, shallow depth of field"`, `style="photorealistic"`, `aspectRatio="3:2"`.

### Logo / Text rendering
- ระบุ Brand Name + คำสั่ง rendering ข้อความใน `prompt`, ตั้ง `style="minimal"` / `bold` / `playful`.
  เช่น: `prompt="Logo with the text 'iCE' in clean geometric sans-serif, navy on white"`, `style="minimal"`, `aspectRatio="1:1"`.

### Product shot (e-commerce)
- Product + Background + Lighting + Angle ใน `prompt`.
  เช่น: `prompt="White wireless earbuds case, seamless light-grey backdrop, top-down 45-degree angle, soft studio lighting"`, `style="photorealistic"`, `aspectRatio="1:1"`, `imageSize="4K"`.

### Flat sticker / illustration
- Subject + Color palette ใน `prompt`, ตั้ง `style="flat illustration"` หรือ `sticker`.

### Iterative edit / style transfer
- ใช้ session: `start-image-edit` ตั้งภาพ base → `continue-image-edit` ป้อนคำสั่งแก้ทีละ change request (เช่น "apply a watercolor style", "swap subject background"). เป็น flow เทียบเท่า iterative edit / composition transfer เดิม แต่ทำต่อเนื่องและตรวจด้วย `analyze-image` ได้.

---

## MCP Server Config (ใน `~/.claude.json`)

```json
{
  "mcpServers": {
    "gemini": {
      "command": "/Users/xpickey/.hermes/node/bin/gemini-mcp",
      "env": {
        "GEMINI_API_KEY": "<your-key-from-aistudio>",
        "GEMINI_IMAGE_MODEL": "gemini-3-pro-image-preview",
        "GEMINI_OUTPUT_DIR": "~/.local/share/gemini-mcp-images"
      }
    }
  }
}
```

**ข้อเท็จจริง config:**
- ชื่อ server = `gemini` (ทุก tool prefix `mcp__gemini__`).
- `command` ชี้ไป binary local ที่ `/Users/xpickey/.hermes/node/bin/gemini-mcp` — **ไม่ใช่** `uv` / `uvx` / `npx`, และไม่อยู่บน iCloud.
- ติดตั้งด้วย `npm install -g @rlabs-inc/gemini-mcp` (ได้ binary `gemini-mcp`).
- เป็น **MCP stdio เสมอ** ทุก environment (Claude Desktop / Claude Code / Cowork) — ไม่มี CLI แยก.
- Auth ใช้ `GEMINI_API_KEY` อย่างเดียว — **ไม่มี** Vertex AI / ADC / `GCP_PROJECT_ID` / `NANOBANANA_AUTH_METHOD`.

---

## Billing / Auth

- ต้องมี `GEMINI_API_KEY` จาก https://aistudio.google.com/apikey และ **เปิด billing** (image/video generation ไม่อยู่ใน free tier).
- ราคา default (Nano Banana Pro `gemini-3-pro-image-preview`): ~$0.12/ภาพ ที่ 4K. `imageSize` ต่ำลง = ถูกลง.
- `429` / `RESOURCE_EXHAUSTED` มักแปลว่า **billing ยังไม่เปิด** → ไปเปิด billing ที่ aistudio.

---

## Error Handling Quick Reference

| Error Pattern | Likely Scenario | Action |
|---|---|---|
| `RESOURCE_EXHAUSTED` / `429` | Billing ยังไม่เปิด / quota | เปิด billing ที่ aistudio.google.com |
| `unauthorized` / `401` | `GEMINI_API_KEY` ผิด | อัปเดต key ใน env ของ server `gemini` |
| `GEMINI_API_KEY not set` | ไม่มี key ใน env | ใส่ `GEMINI_API_KEY` ใน config |
| `Server failed to start` | binary path ผิด | ตรวจ `/Users/xpickey/.hermes/node/bin/gemini-mcp` มีจริง / `npm install -g @rlabs-inc/gemini-mcp` |
| `Tool not found` | MCP `gemini` ยังไม่ถูก setup/restart | เพิ่ม config + restart client |
| `sessionId not found` | session ปิดไปแล้ว / ผิด ID | `gemini-list-image-sessions` เพื่อหา session ที่ยังเปิด |
| ภาพไม่ปรากฏ แต่ไม่มี error | save ไป `GEMINI_OUTPUT_DIR` แล้ว | เช็คโฟลเดอร์ output / `file://images` |
