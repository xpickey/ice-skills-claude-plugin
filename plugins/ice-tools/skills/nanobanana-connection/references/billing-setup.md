# Billing Setup Guide — เปิดสิทธิ์ Image Generation

**ข้อเท็จจริง:** Gemini Image Generation Models (NB2, Pro, Flash 2.5) ทั้งหมดมี **Free Tier Quota = 0** ต้องเปิด Billing ก่อนใช้งาน

## Option 1: Google AI Studio (Pay-as-you-go) — แนะนำสำหรับเริ่มต้น

### ขั้นตอน (3 นาที)

1. **ไปที่:** https://aistudio.google.com/app/billing
2. **Sign in** ด้วย Google Account เดียวกับที่สร้าง API Key
3. **กด "Set up Billing"** หรือ **"Upgrade to Tier 1"**
4. **เลือก/สร้าง GCP Project** (Recommend: สร้าง Project แยกสำหรับ AI เช่น `my-ai-projects`)
5. **ใส่ข้อมูลบัตรเครดิต** (Visa / Mastercard / Amex รองรับ)
6. **ยืนยัน** — Activate ทันที

### ราคา (Pay-as-you-go, USD)

| Model | ราคาต่อภาพ (ประมาณ) | 100 ภาพ |
|---|---|---|
| Flash 2.5 (Legacy) | $0.039 | $3.90 |
| Nano Banana 2 (`nb2`) | $0.039 (1K) - $0.04 (4K) | $4.00 |
| Nano Banana Pro (`pro`) | $0.12 | $12.00 |

**Per Megapixel Pricing:**
- Flash 2.5: $0.039/MP (output)
- NB2: $0.039/MP (output)
- Pro: $0.12/MP (output)

ดู Pricing ล่าสุดที่ https://ai.google.dev/pricing

### ตั้ง Budget Alert (สำคัญมาก)

ป้องกันบิลพุ่ง:
1. ไปที่ https://console.cloud.google.com/billing
2. เลือก Billing Account → **Budgets & alerts** → **Create budget**
3. ตั้งงบ:
   - Conservative: $5 / month
   - Moderate: $25 / month
   - Aggressive (Business): $100 / month
4. ตั้ง Alert threshold: 50%, 80%, 100% — ส่งเข้า Email/Slack

### ตั้ง Quota Cap (ป้องกัน Spike)

1. Cloud Console → **APIs & Services** → **Quotas**
2. Filter: `generativelanguage.googleapis.com`
3. เลือก Quota ที่ต้องการ Cap:
   - `Generate Content Requests Per Day` — กำหนดสูงสุดต่อวัน
   - `Generate Content Input Token Count Per Day`
4. กด **Edit Quotas** → ใส่ Limit ที่รับได้

---

## Option 2: Vertex AI (Production-grade)

### เมื่อใช้

- งานที่ต้อง SLA / Audit Log
- ลูกค้าธุรกิจ (PDPA, ISO 27001)
- ต้องการ Region Control (Data Residency)
- ใช้ใน CI/CD หรือ Server-side Application

### ขั้นตอน (15-30 นาที)

**Step 1: สร้าง/เลือก GCP Project**
```bash
# สร้าง Project ใหม่
gcloud projects create my-nanobanana-prod --name="Nano Banana Production"

# หรือเลือก Project ที่มีอยู่
gcloud config set project <PROJECT_ID>
```

**Step 2: Link Billing Account**
```bash
# ดู Billing Accounts ที่มี
gcloud billing accounts list

# Link Billing Account กับ Project
gcloud billing projects link <PROJECT_ID> \
  --billing-account=<BILLING_ACCOUNT_ID>
```

**Step 3: Enable Vertex AI API**
```bash
gcloud services enable aiplatform.googleapis.com \
  --project=<PROJECT_ID>
```

**Step 4: Grant IAM Role**
```bash
# สำหรับ User Account
gcloud projects add-iam-policy-binding <PROJECT_ID> \
  --member=user:<your-email> \
  --role=roles/aiplatform.user

# สำหรับ Service Account (สำหรับ Production Server)
gcloud iam service-accounts create nanobanana-sa \
  --display-name="Nano Banana Service Account" \
  --project=<PROJECT_ID>

gcloud projects add-iam-policy-binding <PROJECT_ID> \
  --member=serviceAccount:nanobanana-sa@<PROJECT_ID>.iam.gserviceaccount.com \
  --role=roles/aiplatform.user
```

**Step 5: Setup Application Default Credentials**
```bash
# สำหรับ Local Dev
gcloud auth application-default login

# สำหรับ Production Server (ใช้ Service Account Key)
gcloud iam service-accounts keys create ~/sa-key.json \
  --iam-account=nanobanana-sa@<PROJECT_ID>.iam.gserviceaccount.com

export GOOGLE_APPLICATION_CREDENTIALS=~/sa-key.json
```

**Step 6: Update MCP Config**
```json
{
  "mcpServers": {
    "nanobanana": {
      "command": "/path/to/uv",
      "args": ["run", "--directory", "/path/to/project",
               "python", "-m", "nanobanana_mcp_server.server"],
      "env": {
        "NANOBANANA_AUTH_METHOD": "vertex_ai",
        "GCP_PROJECT_ID": "<PROJECT_ID>",
        "GCP_REGION": "global",
        "GOOGLE_APPLICATION_CREDENTIALS": "/path/to/sa-key.json"
      }
    }
  }
}
```

### Region Selection

| Region | Models | Use Case |
|---|---|---|
| `global` | NB2, Pro | Default — Global low latency |
| `us-central1` | Flash 2.5, NB2, Pro | US-based, lower cost |
| `europe-west4` | NB2, Pro | EU compliance |
| `asia-southeast1` | NB2, Pro | APAC compliance, Thailand data residency |

**สำหรับลูกค้าไทย/APAC:** ใช้ `asia-southeast1` (Singapore) เพื่อ Data Residency

---

## Option 3: Custom API Endpoint (Proxy/Gateway)

ถ้าองค์กรมี API Gateway (เช่น Cloudflare Workers, Kong, AWS API Gateway) ห่อ Gemini API:

```json
"env": {
  "GEMINI_API_KEY": "your-key",
  "GEMINI_BASE_URL": "https://your-proxy.example.com/v1beta"
}
```

ประโยชน์:
- เพิ่ม Logging / Audit Layer
- Rate Limit ตามนโยบาย Org
- Cache บางส่วน

---

## ตรวจสถานะ Billing

### AI Studio Way
1. https://aistudio.google.com/app/billing
2. ดู "Current Tier" — ต้องเป็น "Tier 1" หรือสูงกว่า (ไม่ใช่ "Free")
3. ดู "Usage" — เห็น MP ที่ใช้ + Estimated Cost

### Cloud Console Way
1. https://console.cloud.google.com/billing
2. เลือก Billing Account
3. **Reports** — ดูรายเดือน/วัน + Filter by Service "Generative Language API" หรือ "Vertex AI API"

### CLI Way
```bash
gcloud billing accounts list
gcloud billing projects describe <PROJECT_ID>
```

---

## ค่าใช้จ่ายโดยประมาณตาม Use Case

| Use Case | ภาพ/เดือน | Model | Cost/เดือน |
|---|---|---|---|
| Personal Demo | 10-50 | NB2 | $1-2 |
| Side Project | 100-300 | NB2 | $4-12 |
| Small Business Marketing | 500-1000 | NB2 | $20-40 |
| Agency / Heavy Use | 2000-5000 | NB2 + Pro | $80-300 |
| Enterprise / API Server | 10,000+ | Pro | $1,200+ |

---

## หลังเปิด Billing — ทำต่อทันที

1. **ทดสอบ Generate** — รัน `generate_image` ภาพเล็กๆ ตรวจว่าผ่าน
2. **ตรวจ Console** หลัง Generate 5-10 ภาพ ดูว่า Cost ตรงคาดหวัง
3. **บันทึก Config** ของ MCP ไว้ (เผื่อย้าย Machine)
4. **Setup Backup Key** (ถ้าใช้ API Key Method) เก็บไว้ที่ปลอดภัย
5. **Document ขั้นตอน** สำหรับทีม (ถ้ามีหลายคนใช้)

---

## Security Best Practices

1. **อย่า Commit API Key เข้า Git** — ใช้ `.env` + `.gitignore`
2. **Rotate API Key ทุก 90 วัน** — แม้ไม่มีเหตุการณ์
3. **ใช้ Vertex AI สำหรับ Production** — มี IAM Audit ดีกว่า
4. **ตั้ง Quota Cap** — ป้องกัน Spike จาก Key Compromise
5. **Monitor Billing Daily** — ตั้ง Alert + ดูทุกเช้า 1 อาทิตย์แรก
6. **แยก Project Dev/Prod** — Quota และ Billing คนละ Project
