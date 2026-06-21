# API Key Rotation Reference

วิธีเปลี่ยน Gemini API Key สำหรับ **rlabs/gemini-mcp** (`@rlabs-inc/gemini-mcp`) — ครอบคลุม Claude Desktop, Cowork, และ Code CLI

> Server นี้ใช้ `GEMINI_API_KEY` อย่างเดียว (ไม่มี Vertex AI ADC / Service Account) — Rotation จึงเหลือเพียงการสับ Key เดียวทุก Client ให้ตรงกัน

---

## When to Rotate Key

| Trigger | Action | Urgency |
|---|---|---|
| Key รั่วในแชท / อีเมล / Git Commit | Rotate + **ลบ Key เก่าทันที** | 🔴 ทันที |
| สงสัย Anomaly Usage ใน Billing Dashboard | Rotate + ตรวจ Logs | 🔴 ทันที |
| Compromise สงสัยจาก Phishing / Malware | Rotate + Audit ทุก Key อื่นใน Project | 🔴 ทันที |
| ครบกำหนด 90 วัน (Best Practice Rotation) | Rotate ตามรอบ | 🟡 ตามตาราง |
| เปลี่ยน Owner / Admin ของ GCP Project | Rotate + Re-grant Access | 🟡 ภายใน 7 วัน |
| Setup Environment ใหม่ (Dev → Prod) | สร้าง Key แยกตาม Env | 🟢 ตามแผน |

---

## Configuration File Locations

| Client | File | Mechanism |
|---|---|---|
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` | Edit JSON ด้วยมือ หรือ UI |
| Claude Cowork | `~/Library/Application Support/Claude/claude_desktop_config.json` | **เดียวกับ Desktop** |
| Claude Code CLI | `~/.claude.json` | จัดการผ่าน `claude mcp` command |

**ข้อสำคัญ:** Desktop + Cowork ใช้ Config ไฟล์เดียวกัน — แก้ทีเดียว Effect ทั้งสอง

**Server Entry ที่ต้องแก้:** ทุก Client ใช้ชื่อ server ว่า `gemini` ชี้ไปที่ binary local เดียวกันคือ
`/Users/xpickey/.hermes/node/bin/gemini-mcp` (ติดตั้งผ่าน `npm install -g @rlabs-inc/gemini-mcp` — ไม่ใช่ `uv`/`uvx`/`npx` runtime, และไม่อยู่บน iCloud) สิ่งที่ Rotation แตะมีเพียง `env.GEMINI_API_KEY` เท่านั้น ส่วน `GEMINI_IMAGE_MODEL` และ `GEMINI_OUTPUT_DIR` คงเดิม

---

## Method 1: Manual — Claude Desktop / Cowork

### ทาง A: ผ่าน Settings UI

1. Settings (Cmd+,) → Developer / MCP Servers
2. หา `gemini` → กด **Edit**
3. เปลี่ยน Value ของ `GEMINI_API_KEY`
4. Save → **Cmd+Q ปิดสนิท → เปิดใหม่**

### ทาง B: แก้ JSON ด้วยมือ

```bash
open -e "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

หา section `mcpServers.gemini.env.GEMINI_API_KEY` แก้ Value → Save → Restart

โครง Entry ที่ถูกต้องควรหน้าตาแบบนี้ (แก้เฉพาะบรรทัด Key):

```json
{
  "mcpServers": {
    "gemini": {
      "command": "/Users/xpickey/.hermes/node/bin/gemini-mcp",
      "env": {
        "GEMINI_API_KEY": "AIza_NEW_KEY",
        "GEMINI_IMAGE_MODEL": "gemini-3-pro-image-preview",
        "GEMINI_OUTPUT_DIR": "~/.local/share/gemini-mcp-images"
      }
    }
  }
}
```

### ทาง C: Python One-liner (แก้เฉพาะ Key)

```bash
NEW_KEY="AIza..." python3 -c "
import json, os
p = os.path.expanduser('~/Library/Application Support/Claude/claude_desktop_config.json')
with open(p) as f: cfg = json.load(f)
cfg['mcpServers']['gemini']['env']['GEMINI_API_KEY'] = os.environ['NEW_KEY']
with open(p, 'w') as f: json.dump(cfg, f, indent=2)
print('Updated gemini API key')
"
```

---

## Method 2: Manual — Claude Code CLI

CLI ไม่ Support `mcp edit` — ต้อง Remove + Re-add (ถ้าต้องการแก้แค่ Key อย่างเดียว ใช้ Python One-liner กับ `~/.claude.json` ก็ได้ — ดูท้ายหัวข้อ)

```bash
# 1. ลบ Server เดิม
claude mcp remove gemini --scope user

# 2. Add ใหม่พร้อม Key ใหม่ (ชี้ binary local ตรง — ไม่มี uv/npx runtime)
claude mcp add gemini --scope user \
  --env GEMINI_API_KEY=AIza_NEW_KEY \
  --env GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview \
  --env GEMINI_OUTPUT_DIR="$HOME/.local/share/gemini-mcp-images" \
  -- /Users/xpickey/.hermes/node/bin/gemini-mcp

# 3. ตรวจสอบ
claude mcp list
claude mcp get gemini

# 4. ออกจาก Session เดิม (Ctrl+D) → เปิดใหม่
claude
# พิมพ์ /mcp ใน Session ใหม่ ตรวจสถานะ
```

**ทางลัด — แก้เฉพาะ Key ใน `~/.claude.json` โดยไม่ Remove/Re-add:**

```bash
NEW_KEY="AIza..." python3 -c "
import json, os
p = os.path.expanduser('~/.claude.json')
with open(p) as f: cfg = json.load(f)
cfg['mcpServers']['gemini']['env']['GEMINI_API_KEY'] = os.environ['NEW_KEY']
with open(p, 'w') as f: json.dump(cfg, f, indent=2)
print('Updated gemini API key in CLI config')
"
# จากนั้น Ctrl+D → เปิด session ใหม่
```

---

## Pre-Rotation Checklist

ก่อนทำ:

- [ ] มี Key ใหม่จาก https://aistudio.google.com/apikey พร้อมแล้ว
- [ ] เปิด **Billing** ที่ AI Studio แล้ว (Image Generation ไม่อยู่ใน Free Tier — ดู `references/billing-setup.md`)
- [ ] ลบ Key เก่าที่ AI Studio (ถ้ารั่ว/Compromise)
- [ ] ปิด Claude Desktop / Cowork ไม่จำเป็นต้องปิดตอนแก้ Config แต่ต้องปิดหลังจาก Update เสร็จ
- [ ] (Optional) ทดสอบ Key ใหม่ใช้ได้จริง:
  ```bash
  curl -s "https://generativelanguage.googleapis.com/v1beta/models?key=AIza_NEW_KEY" | head -5
  ```

---

## Post-Rotation Verification

หลัง Rotate ต้องทำ 3 ขั้น:

### Step 1: Restart Clients

| Client | คำสั่ง |
|---|---|
| Desktop / Cowork | **Cmd+Q** ปิดสนิท → เปิดใหม่ |
| Code CLI | Ctrl+D ออกจาก Session → เปิดใหม่ |

### Step 2: ตรวจ Connection

- **Desktop / Cowork:** Settings → Developer → ดู `gemini` ต้องเป็น Connected (สีเขียว)
- **Code CLI:** พิมพ์ `/mcp` ใน Session → ดู `gemini` ต้องเป็น Connected

### Step 3: Functional Test

rlabs ไม่มี `show_output_stats` / health-check tool แยก — ยืนยันด้วยการเรียก image tool จริง (ภาพเล็ก 1K ประหยัด Credit) หรือเช็คเบาๆ ด้วย `gemini-list-image-sessions` (จะตอบกลับโดยไม่กิน Credit ถ้า Key + Server ทำงาน)

ทดสอบ Generate (Prompt สั้น):

```
ใช้ gemini สร้าง icon รูปแมวการ์ตูนเรียบๆ
style แบบ minimalist, aspectRatio 1:1, imageSize 1K
```

Tool ที่ถูกเรียกเบื้องหลังคือ `gemini-generate-image(prompt, style, aspectRatio, imageSize)` — ภาพจะถูก save ลง `GEMINI_OUTPUT_DIR` อัตโนมัติ (ไม่มี `output_path` param)

| ผลลัพธ์ | ความหมาย |
|---|---|
| ได้ภาพกลับมา | Rotation สำเร็จ |
| Error 401/403 | Key ผิด หรือ Copy ไม่ครบ (มี Space ต้น/ท้าย) |
| `429` / `RESOURCE_EXHAUSTED` | Billing ยังไม่เปิด → เปิดที่ AI Studio Billing (`references/billing-setup.md`) |

---

## Security Best Practices

### 1. Key Hygiene

- **อย่า Commit Key เข้า Git** — ใช้ `.env` + `.gitignore` หรือ Secret Manager
- **อย่าแชร์ Key ในแชท** — ส่ง Reference / Link to Vault แทน
- **อย่าใส่ Key ใน Screenshot** — Blur หรือ Redact ก่อนแชร์

### 2. Key Lifecycle

```
สร้าง Key → ใช้งาน <90 วัน → Rotate → ลบ Key เก่า
                                          ↓
                              เก็บ History ลบ Key เก่าทั้งหมด
```

### 3. Multi-Environment Strategy

แยก Key ตาม Environment เพื่อ Audit / Limit Blast Radius:

| Env | Key Name | Quota | Use |
|---|---|---|---|
| Dev | `gemini-dev` | Low ($5/mo cap) | Local Dev, Testing |
| Staging | `gemini-staging` | Mid ($25/mo) | Pre-prod Validation |
| Prod | `gemini-prod` | High ($500+/mo) | Production Server |

ในแต่ละ Key:
- ตั้ง **API Restrictions** ใน Cloud Console — Limit เฉพาะ Generative Language API
- ตั้ง **Application Restrictions** ถ้าใช้จาก Server → Bind ตาม IP / Service Account

> หมายเหตุต้นทุน: rlabs ตั้ง Default Model เป็น `gemini-3-pro-image-preview` (Nano Banana Pro) ราคา ~$0.12/ภาพ ที่ 4K — ตั้ง Quota Cap ให้สอดคล้องกับปริมาณการ Generate จริง

### 4. Monitor Key Usage

ตรวจทุกเช้า (สัปดาห์แรกหลังเปิด Billing) แล้วลดเป็นรายสัปดาห์:

- AI Studio Dashboard: https://aistudio.google.com/app/usage
- Cloud Console: https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/metrics

Anomaly ที่ต้องระวัง:
- Spike ผิดเวลา (เช่น 3am ตอนไม่ได้ทำงาน)
- RPM สูงผิดปกติ (อาจมีคน Brute force ผ่าน Key)
- เกิด 403 Spike (Key ถูก Restrict กระทันหัน)

### 5. Emergency Rotation Drill

ทำ Dry-run ทุก Quarter:
1. สร้าง Key ใหม่ทดสอบ
2. แก้ Config ทุก Client (Desktop/Cowork + CLI) → Time การทำงาน
3. ตรวจ Verification (Functional Test ด้านบน)
4. ลบ Key ทดสอบ

เป้าหมาย: Rotate ได้ภายใน **<5 นาที** ตั้งแต่ Detect Compromise → Fully Verified

---

## Troubleshooting

### Issue 1: "Server disconnected" หลัง Rotate
**สาเหตุ:** Binary path ผิด / `@rlabs-inc/gemini-mcp` ถูกถอนหรือย้ายที่
**แก้:**
1. ยืนยัน binary ยังอยู่: `ls -l /Users/xpickey/.hermes/node/bin/gemini-mcp`
2. ถ้าหาย → ติดตั้งใหม่: `npm install -g @rlabs-inc/gemini-mcp`
3. ตรวจ `command` ใน Config ชี้ไปที่ path เต็มของ binary (ไม่ใช่ `uv`/`npx`)

### Issue 2: "401 Unauthorized" หลังใส่ Key ใหม่
**สาเหตุ:** Key ผิด หรือ Billing ไม่เปิด
**แก้:**
1. ตรวจ Copy Key ครบหรือไม่ (ห้ามมี Space ต้น/ท้าย)
2. ทดสอบด้วย curl ก่อน:
   ```bash
   curl "https://generativelanguage.googleapis.com/v1beta/models?key=<NEW_KEY>"
   ```
3. ถ้าได้ 403 หรือ `429`/`RESOURCE_EXHAUSTED` = Billing ไม่เปิด → `references/billing-setup.md`

### Issue 3: Cowork ยังใช้ Key เก่า แม้แก้แล้ว
**สาเหตุ:** ไม่ได้ Restart สนิท
**แก้:**
```bash
# Force Quit + Verify
osascript -e 'quit app "Claude"'
sleep 2
ps aux | grep -i claude | grep -v grep
# ถ้ายังมี Process — kill ด้วย: kill -9 <PID>
open -a Claude
```

### Issue 4: Backup Config เก่าหายไม่อยากให้รก
หลัง Verify ใหม่ใช้งานได้:
```bash
ls -la "$HOME/Library/Application Support/Claude/" | grep backup
# ลบเก่า (เก็บล่าสุด 1 อันเผื่อ Rollback)
find "$HOME/Library/Application Support/Claude/" -name "*.backup.*" -mtime +7 -delete
```

---

## Rollback Procedure (ถ้า Key ใหม่ใช้งานไม่ได้)

ก่อนแก้ Config แนะนำ Backup ไฟล์เดิมไว้ก่อนทุกครั้ง:

```bash
DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
cp "$DESKTOP_CONFIG" "${DESKTOP_CONFIG}.backup.$(date +%Y%m%d_%H%M%S)"
```

เมื่อต้อง Rollback:

```bash
# 1. กลับไปใช้ Backup ล่าสุด
DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
LATEST_BACKUP=$(ls -t "${DESKTOP_CONFIG}.backup."* 2>/dev/null | head -1)

if [[ -n "$LATEST_BACKUP" ]]; then
  cp "$LATEST_BACKUP" "$DESKTOP_CONFIG"
  echo "Rollback แล้ว — Restart Claude Desktop / Cowork"
else
  echo "ไม่พบ Backup"
fi

# 2. สำหรับ Code CLI ใส่ Key เก่ากลับ (ถ้ายังไม่ลบที่ AI Studio):
claude mcp remove gemini --scope user
claude mcp add gemini --scope user \
  --env GEMINI_API_KEY=<OLD_KEY> \
  --env GEMINI_IMAGE_MODEL=gemini-3-pro-image-preview \
  --env GEMINI_OUTPUT_DIR="$HOME/.local/share/gemini-mcp-images" \
  -- /Users/xpickey/.hermes/node/bin/gemini-mcp
```

**คำเตือน:** Rollback ใช้เฉพาะกรณี Key ใหม่มีปัญหา + Key เก่ายังไม่ได้ลบที่ AI Studio
หาก Key เก่าลบไปแล้ว → ต้องสร้าง Key ใหม่อีกตัว แล้ว Rotate ใหม่

---

*V03R01 — Migrated to rlabs/gemini-mcp (`@rlabs-inc/gemini-mcp` v0.8.1) · 2026-06-21*
*การเปลี่ยนแปลงหลัก: server `nanobanana`→`gemini`, ลบ uv/uvx runtime + Vertex AI ADC (`NANOBANANA_AUTH_METHOD`/`GCP_PROJECT_ID`) + `NANOBANANA_MODEL`, command ชี้ binary local `/Users/xpickey/.hermes/node/bin/gemini-mcp`, ลบ rotate script bundle ที่อิง nanobanana path, Functional Test เปลี่ยนเป็น `gemini-generate-image` / `gemini-list-image-sessions` (ไม่มี `show_output_stats`), env ใหม่ `GEMINI_IMAGE_MODEL` + `GEMINI_OUTPUT_DIR`*
