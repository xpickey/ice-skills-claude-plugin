# Install & Authentication Reference

ครอบคลุม 3 Auth Methods + 4 Client Configurations + Fixed Configs ที่ทำให้ทำงานได้จริง

## Authentication Methods (3 วิธี)

### Method 1: API Key (ง่ายที่สุด — แนะนำสำหรับ Personal Use)

**ขั้นตอน:**
1. ไปที่ https://aistudio.google.com/apikey
2. Sign in ด้วย Google Account
3. กด "Create API Key" → เลือก Project
4. **เปิด Billing** ที่ https://aistudio.google.com/app/billing (Image Generation ต้องมี Billing)
5. Copy Key (ขึ้นต้น `AIza...`) เก็บไว้

**ใส่ใน Config:**
```bash
GEMINI_API_KEY=AIzaSyXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**Pros:** Setup เร็ว, Per-user accountability
**Cons:** ถ้าเปิด Billing แล้ว Key รั่ว ใครได้ไปก็เรียกได้ — ต้อง Rotate ทันที

---

### Method 2: Vertex AI ADC (Production-grade)

**ขั้นตอน:**
1. สร้าง GCP Project — https://console.cloud.google.com
2. Enable Vertex AI API:
   ```bash
   gcloud services enable aiplatform.googleapis.com --project=<PROJECT_ID>
   ```
3. Grant IAM Role:
   ```bash
   gcloud projects add-iam-policy-binding <PROJECT_ID> \
     --member=user:<your-email> \
     --role=roles/aiplatform.user
   ```
4. Login ADC:
   ```bash
   gcloud auth application-default login
   ```

**ใส่ใน Config:**
```bash
NANOBANANA_AUTH_METHOD=vertex_ai
GCP_PROJECT_ID=your-project-id
GCP_REGION=global             # สำหรับ NB2/Pro
# GCP_REGION=us-central1      # สำหรับ Flash 2.5 Legacy
```

**Pros:** IAM Control, Audit Log, Region Control, ปลอดภัยกว่า
**Cons:** Setup ซับซ้อน, ต้องมี GCP Knowledge

---

### Method 3: Auto (Mixed)

ใส่ทั้งคู่ในใน Config — Server เลือก API Key ถ้ามี ไม่งั้นใช้ ADC

```bash
NANOBANANA_AUTH_METHOD=auto
GEMINI_API_KEY=AIza...
GCP_PROJECT_ID=...
```

**Pros:** Flexible, Dev/Prod ใช้ Config เดียวกัน
**Cons:** Debug ยาก ไม่รู้ใช้วิธีไหน

---

## Client Configurations (4 Clients)

### Client 1: Claude Desktop / Cowork (Same Config)

**Config File:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

**Recommended Config (Local Source + Full Path):**
```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "/Users/xpickey/.local/bin/uv",
      "args": [
        "run",
        "--directory",
        "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp",
        "python",
        "-m",
        "nanobanana_mcp_server.server"
      ],
      "env": {
        "GEMINI_API_KEY": "AIza...",
        "IMAGE_OUTPUT_DIR": "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp/images",
        "NANOBANANA_MODEL": "auto",
        "LOG_LEVEL": "INFO",
        "PATH": "/Users/xpickey/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
```

**Alternative (uvx Published — ง่ายกว่า):**
```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "/Users/xpickey/.local/bin/uvx",
      "args": ["nanobanana-mcp-server@latest"],
      "env": {
        "GEMINI_API_KEY": "AIza...",
        "PATH": "/Users/xpickey/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
      }
    }
  }
}
```

**Restart:** Cmd+Q ปิดสนิท → เปิดใหม่

---

### Client 2: Claude Code CLI

**Add via Command (User Scope — แนะนำ):**
```bash
claude mcp add nanobanana --scope user \
  --env GEMINI_API_KEY=AIza... \
  --env IMAGE_OUTPUT_DIR=/path/to/images \
  --env NANOBANANA_MODEL=auto \
  -- /Users/xpickey/.local/bin/uv run \
     --directory "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp" \
     python -m nanobanana_mcp_server.server
```

**Verify:**
```bash
claude mcp list                # ดูรายการ
claude mcp get nanobanana      # ดู Detail
```

**Project Scope (.mcp.json ที่ Project Root):**
```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "uvx",
      "args": ["nanobanana-mcp-server@latest"],
      "env": {
        "GEMINI_API_KEY": "${GEMINI_API_KEY}"
      }
    }
  }
}
```
(Export `GEMINI_API_KEY` จาก Shell ก่อนรัน Claude Code)

**Remove:**
```bash
claude mcp remove nanobanana --scope user
```

---

### Client 3: Cursor / Continue.dev / Codex

**Cursor `~/.cursor/mcp.json`:**
```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "uvx",
      "args": ["nanobanana-mcp-server@latest"],
      "env": { "GEMINI_API_KEY": "AIza..." }
    }
  }
}
```

(Continue.dev / Codex Config คล้ายกัน — ดู Docs ของแต่ละ Client)

---

### Client 4: Open WebUI

`config.json` ของ Open WebUI:
```json
{
  "mcp_servers": {
    "nanobanana": {
      "command": ["uvx", "nanobanana-mcp-server@latest"],
      "env": { "GEMINI_API_KEY": "AIza..." }
    }
  }
}
```

---

## Fixed Config After Common Errors

### Error: "Server disconnected" — แก้ด้วย Full Path + PATH env
```json
{
  "command": "/Users/xpickey/.local/bin/uv",   ← Full Path ไม่ใช่แค่ "uv"
  "env": {
    "PATH": "/Users/xpickey/.local/bin:/opt/homebrew/bin:/usr/local/bin:/usr/bin:/bin"
  }
}
```

### Error: "uv run could not find pyproject.toml" — แก้ด้วย --directory หรือ cwd
```json
{
  "args": ["run", "--directory", "/full/path/to/project", "python", "-m", "..."]
}
```
หรือ:
```json
{
  "cwd": "/full/path/to/project"
}
```

### Error: "permission denied" บน images folder — แก้ด้วย mkdir + chmod
```bash
mkdir -p "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp/images"
chmod 755 "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp/images"
```

---

## Prerequisites Cheatsheet

```bash
# 1. ติดตั้ง uv
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. ติดตั้ง Claude Code CLI (ถ้ายังไม่มี)
# ดูที่ https://docs.claude.com/en/docs/claude-code

# 3. Clone repo (Option B Local Source)
cd ~/Documents/Claude/Custom\ Skill
git clone https://github.com/zhongweili/nanobanana-mcp-server.git nanobanana-mcp
cd nanobanana-mcp
uv sync

# 4. ทดสอบ Manual ก่อนใส่ใน Client Config
export GEMINI_API_KEY=AIza...
~/.local/bin/uv run python -m nanobanana_mcp_server.server
# (ออกด้วย Ctrl+C)
```

---

## Switch Auth Method ภายหลัง

จาก API Key → Vertex AI:
1. ตั้ง GCP Project + Enable API + Grant IAM (ดู Method 2)
2. `gcloud auth application-default login`
3. แก้ Config:
   ```json
   "env": {
     "NANOBANANA_AUTH_METHOD": "vertex_ai",
     "GCP_PROJECT_ID": "...",
     "GCP_REGION": "global"
   }
   ```
4. ลบ `GEMINI_API_KEY` ออก (หรือเก็บไว้ใช้ Auto)
5. Restart Client
