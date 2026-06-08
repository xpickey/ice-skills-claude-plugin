# API Key Rotation Reference

วิธีเปลี่ยน Gemini API Key สำหรับ Nano Banana MCP — ครอบคลุม Claude Desktop, Cowork, และ Code CLI

## When to Rotate Key

| Trigger | Action | Urgency |
|---|---|---|
| Key รั่วในแชท / อีเมล / Git Commit | Rotate + **ลบ Key เก่าทันที** | 🔴 ทันที |
| สงสัย Anomaly Usage ใน Billing Dashboard | Rotate + ตรวจ Logs | 🔴 ทันที |
| Compromise สงสัยจาก Phishing / Malware | Rotate + Audit ทุก Key อื่นใน Project | 🔴 ทันที |
| ครบกำหนด 90 วัน (Best Practice Rotation) | Rotate ตามรอบ | 🟡 ตามตาราง |
| เปลี่ยน Owner / Admin ของ GCP Project | Rotate + Re-grant IAM | 🟡 ภายใน 7 วัน |
| Migrate จาก API Key → Vertex AI ADC | Rotate ทั้งหมด + ลบ Old Keys | 🟢 ตาม Roadmap |
| Setup Environment ใหม่ (Dev → Prod) | สร้าง Key แยกตาม Env | 🟢 ตามแผน |

---

## Configuration File Locations

| Client | File | Mechanism |
|---|---|---|
| Claude Desktop | `~/Library/Application Support/Claude/claude_desktop_config.json` | Edit JSON ด้วยมือ หรือ UI |
| Claude Cowork | `~/Library/Application Support/Claude/claude_desktop_config.json` | **เดียวกับ Desktop** |
| Claude Code CLI | `~/.claude.json` | จัดการผ่าน `claude mcp` command |

**ข้อสำคัญ:** Desktop + Cowork ใช้ Config ไฟล์เดียวกัน — แก้ทีเดียว Effect ทั้งสอง

---

## Method 1: One-Script (แนะนำ — ทำทั้งสองพร้อมกัน)

Skill นี้มี Script Bundle อยู่ที่ `scripts/rotate_api_key.sh`

```bash
# ถ้า Skill ติดตั้งใน Claude Code CLI ($HOME/.claude/skills/)
bash ~/.claude/skills/nanobanana-connection/scripts/rotate_api_key.sh

# หรือถ้ามีไฟล์อยู่ที่อื่น
bash /path/to/nanobanana-connection/scripts/rotate_api_key.sh
```

Script จะ:
1. เตือนให้ลบ Key เก่าที่ AI Studio ก่อน
2. ขอ Key ใหม่ (Hidden Input ปลอดภัย)
3. **ทดสอบ Key ก่อนใช้งานจริง** (curl test ที่ Gemini API)
4. หา `uv` Full Path อัตโนมัติ
5. **[1/2]** Backup + Update Desktop / Cowork Config (JSON merge)
6. **[2/2]** Remove + Re-add ใน Claude Code CLI
7. แสดง Next Step

**Override Defaults (ถ้าจำเป็น):**
```bash
TARGET_DIR=/custom/path \
IMAGE_OUTPUT_DIR=/custom/images \
bash scripts/rotate_api_key.sh
```

---

## Method 2: Manual — Claude Desktop / Cowork

### ทาง A: ผ่าน Settings UI

1. Settings (Cmd+,) → Developer / MCP Servers
2. หา `nanobanana` → กด **Edit**
3. เปลี่ยน Value ของ `GEMINI_API_KEY`
4. Save → **Cmd+Q ปิดสนิท → เปิดใหม่**

### ทาง B: แก้ JSON ด้วยมือ

```bash
open -e "$HOME/Library/Application Support/Claude/claude_desktop_config.json"
```

หา section `mcpServers.nanobanana.env.GEMINI_API_KEY` แก้ Value → Save → Restart

### ทาง C: Python One-liner

```bash
NEW_KEY="AIza..." python3 -c "
import json, os
p = os.path.expanduser('~/Library/Application Support/Claude/claude_desktop_config.json')
with open(p) as f: cfg = json.load(f)
cfg['mcpServers']['nanobanana']['env']['GEMINI_API_KEY'] = os.environ['NEW_KEY']
with open(p, 'w') as f: json.dump(cfg, f, indent=2)
print('✓ Updated')
"
```

---

## Method 3: Manual — Claude Code CLI

CLI ไม่ Support `mcp edit` — ต้อง Remove + Re-add

```bash
# 1. ลบ Server เดิม
claude mcp remove nanobanana --scope user

# 2. Add ใหม่พร้อม Key ใหม่
claude mcp add nanobanana --scope user \
  --env GEMINI_API_KEY=AIza_NEW_KEY \
  --env IMAGE_OUTPUT_DIR="/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp/images" \
  --env NANOBANANA_MODEL=auto \
  -- /Users/xpickey/.local/bin/uv run \
     --directory "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp" \
     python -m nanobanana_mcp_server.server

# 3. ตรวจสอบ
claude mcp list
claude mcp get nanobanana

# 4. ออกจาก Session เดิม (Ctrl+D) → เปิดใหม่
claude
# พิมพ์ /mcp ใน Session ใหม่ ตรวจสถานะ
```

---

## Pre-Rotation Checklist

ก่อนรัน Script หรือทำมือ:

- [ ] มี Key ใหม่จาก https://aistudio.google.com/apikey พร้อมแล้ว
- [ ] ลบ Key เก่าที่ AI Studio (ถ้ารั่ว/Compromise)
- [ ] ปิด Claude Desktop / Cowork ไม่จำเป็นต้องปิดตอน Script รัน แต่ต้องปิดหลังจาก Update Config เสร็จ
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

- **Desktop / Cowork:** Settings → Developer → ดู `nanobanana` ต้องเป็น Connected (สีเขียว)
- **Code CLI:** พิมพ์ `/mcp` ใน Session → ดู `nanobanana` ต้องเป็น Connected

### Step 3: Functional Test

ใช้ Prompt ทดสอบ (ภาพเล็กๆ ประหยัด Credit):

```
ใช้ nanobanana สร้าง icon รูปแมวการ์ตูนเรียบๆ
ขนาด 1:1 resolution 1k save ที่ images folder
```

ถ้าได้ภาพ = Rotation สำเร็จ ถ้าได้ Error 401/403 = Key ใหม่อาจไม่เปิด Billing หรือ Key ผิด

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
| Dev | `nanobanana-dev` | Low ($5/mo cap) | Local Dev, Testing |
| Staging | `nanobanana-staging` | Mid ($25/mo) | Pre-prod Validation |
| Prod | `nanobanana-prod` | High ($500+/mo) | Production Server |

ในแต่ละ Key:
- ตั้ง **API Restrictions** ใน Cloud Console — Limit เฉพาะ Generative Language API
- ตั้ง **Application Restrictions** ถ้าใช้จาก Server → Bind ตาม IP / Service Account

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
2. รัน `rotate_api_key.sh` → Time การทำงาน
3. ตรวจ Verification
4. ลบ Key ทดสอบ

เป้าหมาย: Rotate ได้ภายใน **<5 นาที** ตั้งแต่ Detect Compromise → Fully Verified

---

## Troubleshooting

### Issue 1: "Server disconnected" หลัง Rotate
**สาเหตุ:** PATH env หาย / uv path เปลี่ยน
**แก้:** รัน Script `fix_config_V01R02_2026.05.25.sh` (จาก Project Folder) ใหม่อีกครั้ง

### Issue 2: "401 Unauthorized" หลังใส่ Key ใหม่
**สาเหตุ:** Key ผิด หรือ Billing ไม่เปิด
**แก้:**
1. ตรวจ Copy Key ครบหรือไม่ (ห้ามมี Space ต้น/ท้าย)
2. ทดสอบด้วย curl ก่อน:
   ```bash
   curl "https://generativelanguage.googleapis.com/v1beta/models?key=<NEW_KEY>"
   ```
3. ถ้าได้ 403 = Billing ไม่เปิด → `references/billing-setup.md`

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

```bash
# 1. กลับไปใช้ Backup ล่าสุด
DESKTOP_CONFIG="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
LATEST_BACKUP=$(ls -t "${DESKTOP_CONFIG}.backup."* 2>/dev/null | head -1)

if [[ -n "$LATEST_BACKUP" ]]; then
  cp "$LATEST_BACKUP" "$DESKTOP_CONFIG"
  echo "✓ Rollback แล้ว — Restart Claude Desktop / Cowork"
else
  echo "❌ ไม่พบ Backup"
fi

# 2. สำหรับ Code CLI ใส่ Key เก่ากลับ (ถ้ายังไม่ลบที่ AI Studio):
claude mcp remove nanobanana --scope user
claude mcp add nanobanana --scope user \
  --env GEMINI_API_KEY=<OLD_KEY> \
  -- /path/to/uv run --directory "/path" python -m nanobanana_mcp_server.server
```

**คำเตือน:** Rollback ใช้เฉพาะกรณี Key ใหม่มีปัญหา + Key เก่ายังไม่ได้ลบที่ AI Studio
หาก Key เก่าลบไปแล้ว → ต้องสร้าง Key ใหม่อีกตัว แล้ว Rotate ใหม่
