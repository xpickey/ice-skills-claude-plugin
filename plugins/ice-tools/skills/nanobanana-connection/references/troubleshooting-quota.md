# Troubleshooting Quota & Rate Limits

## Error Patterns ที่ต้องรู้

### Pattern 1: Hard 429 — Free Tier Quota = 0
```
429 RESOURCE_EXHAUSTED
* Quota exceeded for metric:
  generativelanguage.googleapis.com/generate_content_free_tier_requests
  limit: 0
  model: gemini-3.1-flash-image
```

**สาเหตุ:** Image Generation ไม่อยู่ใน Free Tier (limit: 0)
**แก้:** เปิด Billing — ดู `billing-setup.md` Option 1

### Pattern 2: Silent Fail — `returned: 0`
```json
{"requested": 1, "returned": 0, "images": []}
```
ไม่มี Error Message ชัด แต่ไม่ได้ภาพ

**สาเหตุที่เป็นได้:**
- Quota Exhausted (Server กลืน Error)
- Safety Filter Block
- Prompt ไม่ผ่าน Content Policy

**Debug:**
1. ตรวจ Billing เปิดหรือไม่ (Most likely)
2. ลอง Prompt อื่นที่ง่ายกว่า
3. ตรวจ Log ที่ `~/Library/Logs/Claude/mcp-server-nanobanana.log`

### Pattern 3: Soft 429 — Rate Limit ชั่วคราว
```
429 Too Many Requests
Please retry in 4.712999624s
```

**สาเหตุ:** เรียกเร็วเกิน RPM (Requests Per Minute)
**แก้:** รอตามจำนวนวินาทีที่บอก แล้วลองใหม่

### Pattern 4: 403 Permission Denied
```
403 PERMISSION_DENIED
The caller does not have permission
```

**สาเหตุ:**
- ใช้ Vertex AI แต่ไม่ Grant IAM `aiplatform.user`
- Project ไม่ Enable Vertex AI API
- API Key restricted ใน Cloud Console

**แก้:** ดู `billing-setup.md` Option 2 Step 4

### Pattern 5: 400 Invalid Argument
```
400 INVALID_ARGUMENT
* Model "..." not available in region "us-central1"
```

**สาเหตุ:** เลือก Region ที่ไม่ Support Model นั้น
**แก้:** เปลี่ยน `GCP_REGION=global` สำหรับ NB2/Pro

---

## Rate Limit Tier Reference

หลังเปิด Billing → จะอยู่ใน Tier ตามการใช้งาน:

| Tier | RPM (NB2) | RPM (Pro) | RPD | เงื่อนไข |
|---|---|---|---|---|
| Free | 0 | 0 | 0 | Default — Image Gen ไม่ใช้ได้ |
| Tier 1 | 60 | 30 | 1,000 | เปิด Billing แล้ว |
| Tier 2 | 1,000 | 100 | 10,000 | ใช้งาน + ค่าใช้จ่าย > $250 + เวลา 30 วัน |
| Tier 3 | 2,000 | 500 | unlimited | ใช้งาน + ค่าใช้จ่าย > $1,000 |

**RPM** = Requests Per Minute | **RPD** = Requests Per Day

ตรวจ Tier ปัจจุบันที่ https://aistudio.google.com/app/billing/tier

---

## Common Diagnostic Flow

### Flowchart: ลำดับตรวจเมื่อ Generate Fail

```
1. Generate Failed
   ↓
2. ดู Error Message
   ↓
   ┌─ มี "429" / "RESOURCE_EXHAUSTED" / "quota" / "billing" / "free_tier"
   │  → ไป Scenario G (Billing/Quota)
   │  → ตรวจ Billing เปิดหรือไม่ → ถ้าไม่ เปิดเลย
   │
   ├─ มี "401" / "403" / "unauthorized" / "credential"
   │  → ไป Scenario C (Auth) หรือ E (Vertex AI ADC)
   │
   ├─ "returned: 0" ไม่มี Error
   │  → ลอง Manual Run จาก Terminal ดู Error จริง
   │  → ส่วนใหญ่คือ Quota เงียบ — ตรวจ Billing
   │
   └─ Server ไม่ตอบเลย / Connection Reset
      → ไป Scenario D (uv/Path)
      → Restart Client
```

---

## Manual Diagnostic Commands

### A. ตรวจว่า Server Start ได้
```bash
cd "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp"
export GEMINI_API_KEY=<your-key>
~/.local/bin/uv run python -m nanobanana_mcp_server.server
```
**ผลที่ควรเห็น:**
```
INFO: Server starting on stdio transport...
INFO: Listening for MCP requests...
```
**ถ้าเห็น Error:** อ่าน Error Output ตรงนั้น

### B. ตรวจว่า API Key ใช้ได้
```bash
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" | head -50
```
**ผลที่ควรเห็น:** JSON List ของ Models
**ถ้าเห็น Error:** Key ไม่ Valid

### C. ตรวจว่า Quota เป็น 0 จริงไหม
```bash
curl -X POST \
  "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-image:generateContent?key=$GEMINI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"contents":[{"parts":[{"text":"test"}]}]}'
```
**ถ้าได้ 429 RESOURCE_EXHAUSTED limit:0** → ยืนยัน ต้องเปิด Billing

### D. ตรวจ Vertex AI ADC ใช้ได้
```bash
gcloud auth application-default print-access-token | head -1
# ต้องได้ Token (ขึ้นต้น ya29.)

gcloud projects describe <PROJECT_ID>
# ดู Project Status: ACTIVE
```

### E. ตรวจ MCP Inspector
```bash
npx @modelcontextprotocol/inspector \
  /Users/xpickey/.local/bin/uv \
  run --directory "/Users/xpickey/Documents/Claude/Custom Skill/nanobanana-mcp" \
  python -m nanobanana_mcp_server.server
```
จะเปิด Web UI ที่ http://localhost:6274 ลอง Call Tool โดยตรง

---

## Quota Recovery Strategy

### When Quota เต็มแล้ว — Options:

**Option 1: รอ Reset**
- Per-minute quota: Reset อัตโนมัติทุก 60 วินาที
- Per-day quota: Reset เที่ยงคืน Pacific Time (PT)

**Option 2: Upgrade Tier**
- ใช้งานต่อ + จ่าย $ จนถึง Threshold (Tier 2 = $250, Tier 3 = $1,000)
- Auto-upgrade หลัง 30 วัน

**Option 3: ขอเพิ่ม Quota Manually**
- Cloud Console → APIs & Services → Quotas
- เลือก Quota → กด "Request quota increase"
- กรอก Use Case + จำนวนที่ต้องการ
- รอ Approval (1-3 วันทำการ)

**Option 4: ใช้หลาย Project**
- สร้าง GCP Project หลายตัว แต่ละ Project มี Quota แยก
- หา Load Balance ผ่าน Multiple Keys
- **ระวัง:** ผิด Google Acceptable Use Policy ถ้าทำเพื่อ Bypass Quota

**Option 5: Migrate ไป Vertex AI**
- Vertex AI มี Quota แยก + ขอเพิ่มง่ายกว่า
- รองรับ Production Workload ได้ดีกว่า

---

## Monitor Usage Real-time

### AI Studio Dashboard
https://aistudio.google.com/app/usage
- ดู Real-time MP Usage
- Filter by Model

### Cloud Console
https://console.cloud.google.com/apis/api/generativelanguage.googleapis.com/metrics
- Real-time RPM, RPD
- Latency, Error Rate

### Programmatic
```bash
gcloud logging read 'resource.type="aiplatform.googleapis.com/Endpoint"' \
  --limit=10 --format=json
```

---

## Cost Optimization Tips

1. **ใช้ Flash 2.5 (Legacy) สำหรับ Draft** — ถูกกว่า + 1024px พอใช้ Iterate
2. **ใช้ NB2 Default** — Quality/Cost Balance ดีสุด
3. **ใช้ Pro เฉพาะเมื่อจำเป็น** — ต้อง Reasoning ลึก, Multi-image
4. **ขอ Resolution ตามจริง** — `1k` สำหรับ Web Thumbnail พอ ไม่ต้อง `4k`
5. **อย่าใส่ `enable_grounding=true` ทุกครั้ง** — ใช้เมื่อจำเป็นจริงๆ
6. **Cache ภาพที่ Generate แล้ว** — ใช้ Files API + file_id แทน Re-generate
7. **Batch Edit แทน Re-generate** — แก้บางส่วนใช้ mode=edit + iterative
