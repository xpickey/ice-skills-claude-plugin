# Install & Authentication Reference

ครอบคลุม Install (`@rlabs-inc/gemini-mcp`) + Authentication (GEMINI_API_KEY) + Client Configurations + Fixed Configs ที่ทำให้ทำงานได้จริง

> **Engine:** rlabs/gemini-mcp (`@rlabs-inc/gemini-mcp` v0.8.1) — MCP stdio server ชื่อ `gemini`. Default image model = Nano Banana Pro (`gemini-3-pro-image-preview`). ใช้ **GEMINI_API_KEY อย่างเดียว** (ไม่มี Vertex AI ADC). เป็น MCP stdio เสมอทุก env (Desktop / Code / Cowork) — ไม่มี CLI แยก.

---

## Step 1: Install (npm global)

ติดตั้ง server แบบ global ผ่าน npm — ได้ binary มาที่ path ที่คงที่ ไม่พึ่ง `uv`/`uvx`/`npx` runtime ตอนรัน:

```bash
npm install -g @rlabs-inc/gemini-mcp
```

**Binary path ที่ใช้ใน Config (เครื่องนี้):**
```
/Users/xpickey/.hermes/node/bin/gemini-mcp
```

> Binary อยู่ใน node bin local (ไม่อยู่บน iCloud) เพื่อให้ MCP host เรียกได้เสถียร. ถ้า node ติดตั้งคนละ prefix ให้หา path จริงด้วย `which gemini-mcp` แล้วใช้ค่านั้นแทน.

**Verify ว่า binary มีอยู่จริง:**
```bash
ls -l /Users/xpickey/.hermes/node/bin/gemini-mcp
which gemini-mcp
```

---

## Step 2: Authentication (API Key + Billing)

rlabs/gemini-mcp ใช้ **API Key อย่างเดียว** — Setup เร็ว, Per-user accountability.

**ขั้นตอน:**
1. ไปที่ https://aistudio.google.com/apikey
2. Sign in ด้วย Google Account
3. กด "Create API Key" → เลือก Project
4. **เปิด Billing** ที่ https://aistudio.google.com/app/billing — **จำเป็น** เพราะ Image Generation ไม่อยู่ใน Free Tier
5. Copy Key (ขึ้นต้น `AIza...`) เก็บไว้ใส่ใน Config

```bash
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Pros:** Setup เร็ว, Per-user accountability
**Cons:** ถ้าเปิด Billing แล้ว Key รั่ว ใครได้ไปก็เรียกได้ — Rotate ทันทีเมื่อสงสัยว่ารั่ว

---

## Step 3: Environment Variables (3 ตัวหลัก)

| Env Var | ค่าแนะนำ | หน้าที่ |
|---|---|---|
| `GEMINI_API_KEY` | `AIza...` | API Key จาก AI Studio (จำเป็น) |
| `GEMINI_IMAGE_MODEL` | `gemini-3-pro-image-preview` | Image model (default = Nano Banana Pro) |
| `GEMINI_OUTPUT_DIR` | `~/.local/share/gemini-mcp-images` | โฟลเดอร์ที่ภาพ generate ถูก save ลงอัตโนมัติ |

> ภาพทุกใบจาก `gemini-generate-image` / edit session ถูกเขียนลง `GEMINI_OUTPUT_DIR` ให้เอง — ไม่มี `output_path` param ต่อ call. ถ้าต้องการเปลี่ยนปลายทาง แก้ที่ env นี้ตัวเดียว.

---

## Client Configurations

### Client 1: Claude Code / Desktop / Cowork (`~/.claude.json`)

ทั้งสาม environment ใช้ entry เดียวกัน เพราะ rlabs เป็น MCP stdio เสมอ. เพิ่ม server ชื่อ `gemini` เข้า `mcpServers`:

```json
{
  "mcpServers": {
    "gemini": {
      "command": "/Users/xpickey/.hermes/node/bin/gemini-mcp",
      "env": {
        "GEMINI_API_KEY": "AIza...",
        "GEMINI_IMAGE_MODEL": "gemini-3-pro-image-preview",
        "GEMINI_OUTPUT_DIR": "/Users/xpickey/.local/share/gemini-mcp-images"
      }
    }
  }
}
```

**Restart:**
- Claude Desktop / Cowork: Cmd+Q ปิดสนิท → เปิดใหม่
- Claude Code: ปิด session แล้วเปิดใหม่ / รัน `claude mcp list` เพื่อยืนยันว่าเห็น `gemini`

---

### Client 2: Claude Code CLI (Add via Command)

```bash
claude mcp add gemini --scope user \
  --env GEMINI_API_KEY=AIza... \
  --env GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview \
  --env GEMINI_OUTPUT_DIR=/Users/xpickey/.local/share/gemini-mcp-images \
  -- /Users/xpickey/.hermes/node/bin/gemini-mcp
```

**Verify:**
```bash
claude mcp list            # ต้องเห็น gemini ในรายการ
claude mcp get gemini      # ดู Detail + env
```

**Remove:**
```bash
claude mcp remove gemini --scope user
```

---

### Client 3: Cursor / Continue.dev / Codex

**Cursor `~/.cursor/mcp.json`:**
```json
{
  "mcpServers": {
    "gemini": {
      "command": "/Users/xpickey/.hermes/node/bin/gemini-mcp",
      "env": {
        "GEMINI_API_KEY": "AIza...",
        "GEMINI_IMAGE_MODEL": "gemini-3-pro-image-preview",
        "GEMINI_OUTPUT_DIR": "/Users/xpickey/.local/share/gemini-mcp-images"
      }
    }
  }
}
```

(Continue.dev / Codex Config คล้ายกัน — ชี้ `command` ไปที่ binary เดียวกัน, ใส่ env 3 ตัวเหมือนกัน — ดู Docs ของแต่ละ Client)

---

## Verify Install (แทน Pre-flight แบบเดิม)

rlabs **ไม่มี** `show_output_stats` / `maintenance` ฉะนั้น Pre-flight ใช้วิธีตรงไปตรงมา 2 ทาง:

1. **เช็ก session ที่เปิดอยู่ (เบาที่สุด ไม่เสียค่าใช้จ่าย):**
   เรียก `gemini-list-image-sessions()` — ถ้าตอบกลับได้ (แม้ list ว่าง) แปลว่า server connect และ auth ผ่าน
2. **ลอง generate จริง 1 ใบ (ยืนยัน billing ด้วย):**
   เรียก `gemini-generate-image(prompt="a single red apple on white background", imageSize="1K", aspectRatio="1:1")` — ภาพจะถูก save ลง `GEMINI_OUTPUT_DIR`

ถ้าทั้งสองทางผ่าน = พร้อมใช้งานเต็มรูปแบบ.

---

## Troubleshooting (Common Errors)

### Error: "Server disconnected" / server ไม่ขึ้นใน `claude mcp list`
- เช็กว่า binary path ถูกต้อง: `ls -l /Users/xpickey/.hermes/node/bin/gemini-mcp`
- ถ้าไม่เจอ ติดตั้งซ้ำ: `npm install -g @rlabs-inc/gemini-mcp` แล้วยืนยันด้วย `which gemini-mcp`
- ใช้ **Full Path** ใน `command` เสมอ (อย่าใส่แค่ `"gemini-mcp"`) เพื่อตัดปัญหา PATH ของ MCP host

### Error: `429` / `RESOURCE_EXHAUSTED`
- เกือบทุกครั้งคือ **Billing ยังไม่เปิด** (Image Generation ไม่อยู่ Free Tier)
- เปิด Billing ที่ https://aistudio.google.com/app/billing แล้วลองใหม่
- ถ้าเปิด Billing แล้วยังเจอ = ชน rate limit ชั่วคราว → เว้นช่วงแล้ว retry

### Error: `401` / `PERMISSION_DENIED` / Invalid API Key
- Key ผิด / หมดอายุ / ถูก Rotate → สร้างใหม่ที่ https://aistudio.google.com/apikey แล้วอัปเดต `GEMINI_API_KEY`

### Error: ภาพ generate สำเร็จแต่หาไฟล์ไม่เจอ
- ดูที่ `GEMINI_OUTPUT_DIR` ที่ตั้งไว้ — ภาพ save ที่นั่นเสมอ (ไม่มี `output_path` ต่อ call)
- สร้างโฟลเดอร์ + ให้สิทธิ์ถ้าจำเป็น:
  ```bash
  mkdir -p ~/.local/share/gemini-mcp-images
  chmod 755 ~/.local/share/gemini-mcp-images
  ```

---

## Tool Inventory (rlabs/gemini-mcp — prefix `mcp__gemini__`)

ทุก tool call ในสกิลนี้อ้างอิงรายการนี้:

| Tool | Params (`*` = required) | หน้าที่ |
|---|---|---|
| `gemini-generate-image` | `prompt*`, `style`, `aspectRatio`, `imageSize`, `useGoogleSearch` | สร้างภาพ — save ลง `GEMINI_OUTPUT_DIR` อัตโนมัติ |
| `gemini-image-prompt` | `description*`, `style`, `mood`, `details` | ช่วยร่าง/ขัดเกลา prompt ก่อน generate |
| `gemini-start-image-edit` | `prompt*`, `aspectRatio`, `imageSize`, `useGoogleSearch` | เริ่ม edit session → คืน `sessionId` + ภาพ base |
| `gemini-continue-image-edit` | `sessionId*`, `prompt*` | แก้ภาพต่อใน session เดิม (multi-turn) |
| `gemini-end-image-edit` | `sessionId*` | ปิด edit session |
| `gemini-list-image-sessions` | — | ดู session ที่เปิดค้างอยู่ |
| `gemini-analyze-image` | `imagePath*`, `query`, `detectObjects`, `model`, `thinkingLevel` | ให้ Claude "เห็น"/วิเคราะห์ภาพ แล้ว iterate ต่อ |
| `gemini-generate-video` | `prompt*`, `aspectRatio`, `negativePrompt` | สร้างวิดีโอ (Veo) |

**ค่า param ที่ใช้ได้จริง:**
- `imageSize`: `1K` / `2K` (default) / `4K`
- `aspectRatio`: `1:1`, `16:9`, `9:16`, `21:9`, `4:3`, `3:4`, `4:5`, `5:4`, `2:3`, `3:2`
- `style`: เช่น `photorealistic`, `watercolor`, `anime` — เป็น **param แยก** ไม่ต้องฝังคำสั่ง style ลงใน `prompt`

**สิ่งที่ engine นี้ไม่มี (อย่าเรียก):** `show_output_stats`, `maintenance`, `upload_file`, `model_tier` (nb2/pro/flash), `negative_prompt` ของภาพ, `output_path`, `n` (batch หลายภาพ/ครั้ง), `mode=edit`, `input_image_path`. การ edit ใช้ session-based เท่านั้น.

---

## Edit Workflow (Session-based)

การแก้ภาพเป็น **multi-turn session** — เริ่ม → แก้ซ้ำได้ → ปิด:

```
gemini-start-image-edit(prompt="modern minimalist living room, soft daylight", imageSize="2K", aspectRatio="16:9")
  → ได้ภาพ base + sessionId

gemini-continue-image-edit(sessionId="...", prompt="make the lighting warmer, golden hour")
gemini-continue-image-edit(sessionId="...", prompt="add a large green plant in the left corner")
  → แก้ต่อในบริบทเดิมได้ไม่จำกัดรอบ

gemini-end-image-edit(sessionId="...")
  → ปิด session
```

ข้อดีเทียบกับ one-shot edit: รักษา context ของภาพข้ามรอบการแก้ จึงปรับทีละนิดแล้วคงองค์ประกอบเดิมไว้ได้.

---

## Feature ใหม่: Claude เห็นภาพแล้ว Iterate (Analyze → Refine Loop)

`gemini-analyze-image` ทำให้ Claude อ่านภาพที่ generate ออกมาได้จริง — ปิด loop "สร้าง → ตรวจ → แก้" ได้ในตัว:

```
1. gemini-generate-image(prompt="...", imageSize="2K")
     → ภาพ save ที่ GEMINI_OUTPUT_DIR/<file>.png

2. gemini-analyze-image(imagePath="<GEMINI_OUTPUT_DIR>/<file>.png",
                        query="Does the composition match the brief? List anything off.")
     → Claude ระบุจุดที่ต้องแก้ (เช่น สัดส่วน, สี, องค์ประกอบ)

3. gemini-start-image-edit(...) → gemini-continue-image-edit(...) ตามที่วิเคราะห์ได้
```

ใช้กับ asset ที่ต้องตรงตาม brief (ภาพ presentation, product shot, hero banner) เพื่อลดการเดา.

---

## Pricing (ย่อ)

Default model = **Nano Banana Pro** (`gemini-3-pro-image-preview`):
- ราว **~$0.12 / ภาพ** ที่ `imageSize=4K`
- ต้องเปิด Billing เสมอ (ไม่อยู่ Free Tier) — รายละเอียดเต็มดู `references/pricing-and-cost.md` ของสกิลถ้ามี

---

## Switch Output Folder / Model ภายหลัง

ทุกอย่างคุมผ่าน env — แก้ใน Config แล้ว Restart Client:
- เปลี่ยนปลายทางภาพ: แก้ `GEMINI_OUTPUT_DIR`
- เปลี่ยน image model: แก้ `GEMINI_IMAGE_MODEL` (default `gemini-3-pro-image-preview`)
- เปลี่ยน API Key: แก้ `GEMINI_API_KEY`

ไม่มี auth method อื่นให้สลับ (ไม่มี Vertex AI ADC) — Key เดียวจบ.

---

*V03R01 · 2026.06.21 · Migrated from nanobanana MCP → rlabs/gemini-mcp (`@rlabs-inc/gemini-mcp` v0.8.1). เปลี่ยนเป็น npm install -g + binary `/Users/xpickey/.hermes/node/bin/gemini-mcp`, server name `gemini`, GEMINI_API_KEY only. ลบ Vertex AI ADC / uv / uvx / NANOBANANA_* config + tool ที่ engine ใหม่ไม่มี (show_output_stats, maintenance, upload_file, model_tier). เพิ่ม session-based edit + gemini-analyze-image.*
