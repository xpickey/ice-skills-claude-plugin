# Troubleshooting Quota & Rate Limits

> MCP server: **rlabs/gemini-mcp** (`@rlabs-inc/gemini-mcp`) — server name `gemini`, image tools prefix `mcp__gemini__`. Default model = **Nano Banana Pro** (`gemini-3-pro-image-preview`). Auth ใช้ `GEMINI_API_KEY` อย่างเดียว (ไม่มี Vertex AI ADC).

## Error Patterns ที่ต้องรู้

### Pattern 1: Hard 429 — Free Tier Quota = 0
```
429 RESOURCE_EXHAUSTED
* Quota exceeded for metric:
  generativelanguage.googleapis.com/generate_content_free_tier_requests
  limit: 0
  model: gemini-3-pro-image-preview
```

**สาเหตุ:** Image Generation ไม่อยู่ใน Free Tier (limit: 0) — Nano Banana Pro ต้องเปิด Billing ก่อนเสมอ
**แก้:** เปิด Billing ที่ https://aistudio.google.com/app/billing — ดู `billing-setup.md`

### Pattern 2: Silent Fail — ไม่ได้ภาพ ไม่มี Error ชัด
`gemini-generate-image` คืน Response แต่ไม่มีไฟล์ใน `GEMINI_OUTPUT_DIR` (default `~/.local/share/gemini-mcp-images`)

**สาเหตุที่เป็นได้:**
- Quota Exhausted (Server กลืน Error)
- Safety Filter Block
- Prompt ไม่ผ่าน Content Policy

**Debug:**
1. ตรวจ Billing เปิดหรือไม่ (Most likely)
2. ลอง Prompt อื่นที่ง่ายกว่า เช่น `gemini-generate-image(prompt="a red apple on a white table")`
3. ตรวจ Log ที่ `~/Library/Logs/Claude/mcp-server-gemini.log`
4. เช็คโฟลเดอร์ Output ว่ามีไฟล์ใหม่เกิดขึ้นจริงไหม: `ls -lt ~/.local/share/gemini-mcp-images | head`

### Pattern 3: Soft 429 — Rate Limit ชั่วคราว
```
429 Too Many Requests
Please retry in 4.712999624s
```

**สาเหตุ:** เรียกเร็วเกิน RPM (Requests Per Minute)
**แก้:** รอตามจำนวนวินาทีที่บอก แล้วลองใหม่. ถ้า Iterate ภาพหลายรอบ ให้ใช้ session-based edit (`gemini-continue-image-edit`) แทนการ `gemini-generate-image` ใหม่ทุกครั้ง — ลดจำนวน Request

### Pattern 4: 403 Permission Denied
```
403 PERMISSION_DENIED
The caller does not have permission
```

**สาเหตุ:**
- API Key ถูก restricted ใน Cloud Console (จำกัด API/Referrer/IP)
- Generative Language API ยังไม่ Enable ใน Project ของ Key
- Key ผูกกับ Project ที่ยังไม่เปิด Billing

**แก้:** ใช้ Key ที่สร้างจาก https://aistudio.google.com/apikey และตรวจ Restriction ใน Cloud Console — ดู `billing-setup.md`

### Pattern 5: 400 Invalid Argument
```
400 INVALID_ARGUMENT
* Invalid value for parameter ...
```

**สาเหตุ:** ส่ง param ที่ไม่รองรับ หรือค่าผิด format
**แก้:** ตรวจค่าให้ตรง schema ของ rlabs:
- `imageSize` รับเฉพาะ `1K` / `2K` (default) / `4K` — **ไม่ใช่** `high`/`4k`/`resolution` และ **ไม่มี** `model_tier` (nb2/pro/flash)
- `aspectRatio` รับเฉพาะ `1:1, 16:9, 9:16, 21:9, 4:3, 3:4, 4:5, 5:4, 2:3, 3:2`
- `style` เป็น param แยก (เช่น `"photorealistic"`, `"watercolor"`, `"anime"`) — ไม่ฝังใน prompt
- **ไม่มี** param เหล่านี้แล้ว: `output_path`, `negative_prompt` (สำหรับภาพ), `n`, `mode=edit`, `input_image_path`

---

## Rate Limit Tier Reference

หลังเปิด Billing → จะอยู่ใน Tier ตามการใช้งาน (Nano Banana Pro = `gemini-3-pro-image-preview`):

| Tier | RPM | RPD | เงื่อนไข |
|---|---|---|---|
| Free | 0 | 0 | Default — Image Gen ใช้ไม่ได้ |
| Tier 1 | ~30 | ~1,000 | เปิด Billing แล้ว |
| Tier 2 | ~100 | ~10,000 | ใช้งาน + ค่าใช้จ่าย > $250 + เวลา 30 วัน |
| Tier 3 | ~500 | unlimited | ใช้งาน + ค่าใช้จ่าย > $1,000 |

**RPM** = Requests Per Minute | **RPD** = Requests Per Day

ตรวจ Tier ปัจจุบันที่ https://aistudio.google.com/app/billing/tier

---

## Common Diagnostic Flow

### Flowchart: ลำดับตรวจเมื่อ Generate Fail

```
1. gemini-generate-image Failed / ไม่ได้ไฟล์
   ↓
2. ดู Error Message / เช็ค GEMINI_OUTPUT_DIR
   ↓
   ┌─ มี "429" / "RESOURCE_EXHAUSTED" / "quota" / "billing" / "free_tier"
   │  → Billing/Quota → ตรวจ Billing เปิดหรือไม่ → ถ้าไม่ เปิดเลย
   │
   ├─ มี "401" / "403" / "PERMISSION_DENIED" / "API key"
   │  → Auth → ตรวจ GEMINI_API_KEY + Restriction ใน Cloud Console
   │
   ├─ มี "400" / "INVALID_ARGUMENT"
   │  → ตรวจ param: imageSize (1K/2K/4K), aspectRatio, style
   │
   ├─ ไม่มี Error แต่ไม่มีไฟล์ใหม่ใน Output Dir
   │  → ส่วนใหญ่คือ Quota เงียบ หรือ Safety Filter — ตรวจ Billing + ลอง Prompt ง่ายกว่า
   │
   └─ Server ไม่ตอบเลย / Connection Reset
      → ตรวจ binary path /Users/xpickey/.hermes/node/bin/gemini-mcp มีจริงไหม
      → Restart Client
```

---

## Manual Diagnostic Commands

### A. ตรวจว่า binary/Server Start ได้
```bash
GEMINI_API_KEY=<your-key> /Users/xpickey/.hermes/node/bin/gemini-mcp
```
**ผลที่ควรเห็น:** Server เริ่มฟัง MCP request บน stdio (รอ input — กด Ctrl+C เพื่อออก)
**ถ้าเห็น "command not found":** ติดตั้งใหม่
```bash
npm install -g @rlabs-inc/gemini-mcp
which gemini-mcp
```

### B. ตรวจว่า API Key ใช้ได้
```bash
curl -s \
  "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" | head -50
```
**ผลที่ควรเห็น:** JSON List ของ Models
**ถ้าเห็น Error:** Key ไม่ Valid หรือ API ไม่ Enable

### C. ตรวจว่า Quota เป็น 0 จริงไหม (ยิงตรง Image Model)
```bash
curl -s -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3-pro-image-preview:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"a red apple"}]}]}'
```
**ถ้าได้ 429 RESOURCE_EXHAUSTED limit:0** → ยืนยัน ต้องเปิด Billing

### D. ตรวจ In-MCP — เรียก tool จริงผ่าน Claude
แทนการรัน Inspector แยก ให้ลองเรียก image tool จริงในเซสชัน แล้วดูผล:
```
gemini-generate-image(prompt="a simple red circle on white background", imageSize="1K")
```
- ถ้าได้ไฟล์ใน `~/.local/share/gemini-mcp-images` → Server + Billing OK
- ถ้าไม่ได้ → ดู Error ที่คืนมา แล้วเทียบกับ Pattern ด้านบน

ตรวจ Session ที่เปิดค้างอยู่ (กรณีใช้ edit workflow):
```
gemini-list-image-sessions()
```

### E. ตรวจ Output Directory
```bash
ls -lt ~/.local/share/gemini-mcp-images | head
# ดูว่ามีไฟล์ใหม่เกิดหลังเรียก generate ไหม + พื้นที่ดิสก์พอไหม
df -h ~
```

---

## Quota Recovery Strategy

### When Quota เต็มแล้ว — Options:

**Option 1: รอ Reset**
- Per-minute quota (RPM): Reset อัตโนมัติทุก 60 วินาที
- Per-day quota (RPD): Reset เที่ยงคืน Pacific Time (PT)

**Option 2: Upgrade Tier**
- ใช้งานต่อ + จ่าย $ จนถึง Threshold (Tier 2 = $250, Tier 3 = $1,000)
- Auto-upgrade หลัง 30 วัน

**Option 3: ขอเพิ่ม Quota Manually**
- Cloud Console → APIs & Services → Quotas
- เลือก Quota ของ Generative Language API → กด "Request quota increase"
- กรอก Use Case + จำนวนที่ต้องการ
- รอ Approval (1-3 วันทำการ)

**Option 4: ลดจำนวน Request ต่อชิ้นงาน**
- ใช้ session-based edit แทน re-generate: `gemini-start-image-edit` → `gemini-continue-image-edit` ซ้ำในภาพเดิม → ประหยัด Request เทียบกับ `gemini-generate-image` ใหม่ทุกครั้ง
- ใช้ `gemini-analyze-image(imagePath=...)` ให้ Claude "เห็น" ภาพที่มีอยู่แล้ว เพื่อตัดสินใจก่อนยิง generate รอบใหม่ — ลด Iteration ที่เสียเปล่า

---

## Monitor Usage Real-time

### AI Studio Dashboard
https://aistudio.google.com/app/usage
- ดู Real-time Usage
- Filter by Model

### Cloud Console
https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/metrics
- Real-time RPM, RPD
- Latency, Error Rate

### Local — นับภาพที่ Generate ในเครื่อง
```bash
ls -1 ~/.local/share/gemini-mcp-images | wc -l
# ดูจำนวนไฟล์ภาพที่สะสมไว้ใน Output Dir
```

---

## Cost Optimization Tips

ราคาอ้างอิง: Nano Banana Pro (`gemini-3-pro-image-preview`) ~$0.12/ภาพ ที่ 4K — ค่าใช้จ่ายแปรตาม `imageSize`

1. **ขอ `imageSize` ตามจริง** — `1K` พอสำหรับ Web Thumbnail / Draft, สงวน `2K`/`4K` ไว้สำหรับงานส่งจริง
2. **Iterate ด้วย session-based edit** — `gemini-start-image-edit` → `gemini-continue-image-edit` แก้ทีละจุด (เช่น `"make it warmer"`, `"remove the text"`) แทน `gemini-generate-image` ใหม่ทุกครั้ง — เร็วกว่า, ใช้ Request น้อยกว่า, รักษา composition เดิม
3. **ปิด session เมื่อเสร็จ** — เรียก `gemini-end-image-edit(sessionId)` เพื่อไม่ให้ session ค้าง (เช็คได้ด้วย `gemini-list-image-sessions`)
4. **ใช้ `gemini-analyze-image` ก่อนยิง generate ใหม่** — ให้ Claude วิเคราะห์ภาพที่มีอยู่ แล้วปรับ prompt ให้ตรงรอบเดียว แทนการลองผิดลองถูกหลายรอบ
5. **ร่าง prompt ด้วย `gemini-image-prompt` ก่อน** — `gemini-image-prompt(description=..., style=..., mood=...)` ช่วยให้ prompt แม่นตั้งแต่รอบแรก ลดจำนวนภาพที่ต้องทิ้ง
6. **อย่าเปิด `useGoogleSearch=true` ทุกครั้ง** — ใช้เฉพาะเมื่อต้องอ้างอิงข้อมูล/ภาพจริงจากเว็บ
