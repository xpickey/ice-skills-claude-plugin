# Billing Setup Guide — เปิดสิทธิ์ Image Generation (rlabs/gemini-mcp)

**ข้อเท็จจริง:** Gemini Image Generation Models — รวมถึง `gemini-3-pro-image-preview` (Nano Banana Pro) ซึ่งเป็น default ของ rlabs/gemini-mcp — มี **Free Tier Quota = 0** ต้องเปิด Billing บน Google AI Studio ก่อนใช้งานเสมอ การออกแบบ key + billing ให้พร้อมตั้งแต่ต้น คือเงื่อนไขจำเป็นที่ทำให้ทุก tool ใน skill นี้เรียกใช้ได้จริง ไม่ติด error 429

---

## Google AI Studio (Pay-as-you-go) — เส้นทางเดียวที่ rlabs ใช้

rlabs/gemini-mcp ตรวจสิทธิ์ผ่าน **`GEMINI_API_KEY` อย่างเดียว** ไม่มี Application Default Credentials, ไม่มี Service Account, ไม่มี Vertex AI ADC ดังนั้นการเปิดสิทธิ์ทั้งหมดจบที่ AI Studio Billing ขั้นตอนสั้น ตรงไปตรงมา และเพียงพอสำหรับทั้งงานส่วนตัวและงานเสนอลูกค้า

### ขั้นตอน (3 นาที)

1. **ไปที่:** https://aistudio.google.com/app/billing
2. **Sign in** ด้วย Google Account เดียวกับที่สร้าง API Key
3. **กด "Set up Billing"** หรือ **"Upgrade to Tier 1"**
4. **เลือก/สร้าง GCP Project** (แนะนำให้แยก Project สำหรับงาน AI โดยเฉพาะ เช่น `my-ai-projects` เพื่อให้ Quota และ Billing ไม่ปนกับงานอื่น)
5. **ใส่ข้อมูลบัตรเครดิต** (Visa / Mastercard / Amex รองรับ)
6. **ยืนยัน** — Activate ทันที

### สร้าง API Key ให้ตรงกับ Project ที่เปิด Billing

1. ไปที่ https://aistudio.google.com/apikey
2. **Create API key** → เลือก GCP Project เดียวกับที่เพิ่งเปิด Billing ในข้อข้างบน (ถ้า key ผูกกับ Project ที่ยังไม่เปิด billing จะเจอ 429 ทันทีตอน generate)
3. คัดลอกค่า key ไปวางใน `env.GEMINI_API_KEY` ของ MCP server ชื่อ `gemini`

### ราคา (Pay-as-you-go, USD)

rlabs/gemini-mcp ใช้ `gemini-3-pro-image-preview` (Nano Banana Pro) เป็น model เริ่มต้น และไม่มีการสลับ model tier (ไม่มี nb2/pro/flash ให้เลือก) ราคาจึงคิดตาม Pro เป็นหลัก โดยปรับตามค่า `imageSize` ที่เลือก

| imageSize | ความละเอียด | ราคาต่อภาพ (ประมาณ) | 100 ภาพ |
|---|---|---|---|
| `1K` | ~1 MP | ต่ำสุดของช่วง | ต่ำสุดของช่วง |
| `2K` (default) | ~4 MP | กลาง | กลาง |
| `4K` | ~16 MP | ~$0.12 | ~$12.00 |

**หลักการคิดเงิน:** Nano Banana Pro คิดแบบ per-megapixel (output) ที่ ~$0.12/MP ดังนั้น `4K` แพงกว่า `1K` หลายเท่าตามจำนวน megapixel จริง สำหรับงาน draft/iterate ให้เริ่มที่ `1K` หรือ `2K` ก่อน แล้วค่อยยก `imageSize` เป็น `4K` เฉพาะภาพ final ที่ลูกค้าจะได้เห็นจริง

ดู Pricing ล่าสุดที่ https://ai.google.dev/pricing

### ตั้ง Budget Alert (สำคัญมาก)

ป้องกันบิลพุ่ง โดยเฉพาะเมื่อ default เป็น Pro ที่ราคาสูงกว่ารุ่นเก่า:
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

## MCP Config — server ชื่อ `gemini`

rlabs/gemini-mcp ติดตั้งเป็น binary local และรันเป็น MCP stdio เสมอในทุก environment (Claude Desktop / Claude Code / Cowork) ไม่มี uv/uvx และไม่มี CLI แยก การตั้งค่าใน `~/.claude.json` มีหน้าตาดังนี้

```json
{
  "mcpServers": {
    "gemini": {
      "command": "/Users/xpickey/.hermes/node/bin/gemini-mcp",
      "env": {
        "GEMINI_API_KEY": "<your-aistudio-key>",
        "GEMINI_IMAGE_MODEL": "gemini-3-pro-image-preview",
        "GEMINI_OUTPUT_DIR": "~/.local/share/gemini-mcp-images"
      }
    }
  }
}
```

ติดตั้ง/อัปเดต binary ผ่าน npm:

```bash
npm install -g @rlabs-inc/gemini-mcp
# binary จะอยู่ที่ /Users/xpickey/.hermes/node/bin/gemini-mcp
```

**หมายเหตุสำคัญเรื่อง path:** binary ต้องอยู่บน local disk (ตามตัวอย่าง `/Users/xpickey/.hermes/node/bin/gemini-mcp`) ไม่ควรวางบน iCloud Drive เพราะ MCP launch อาจล้มเหลวเมื่อไฟล์ถูก offload

---

## ตรวจสถานะ Billing

### AI Studio Way
1. https://aistudio.google.com/app/billing
2. ดู "Current Tier" — ต้องเป็น "Tier 1" หรือสูงกว่า (ไม่ใช่ "Free")
3. ดู "Usage" — เห็น MP ที่ใช้ + Estimated Cost

### Cloud Console Way
1. https://console.cloud.google.com/billing
2. เลือก Billing Account
3. **Reports** — ดูรายเดือน/วัน + Filter by Service "Generative Language API"

### CLI Way
```bash
gcloud billing accounts list
gcloud billing projects describe <PROJECT_ID>
```

---

## ตรวจว่า MCP + Billing ใช้ได้จริง (Pre-flight)

rlabs/gemini-mcp ไม่มี diagnostic tool แบบเก่า (ไม่มี `show_output_stats`, `maintenance`, `upload_file`) การ pre-flight จึงทำด้วยการเรียก tool จริงแบบเบาที่สุด แล้วดูผล

1. **ลอง generate ภาพเล็กที่สุด** — เรียก `gemini-generate-image` ด้วย `imageSize: "1K"` และ prompt สั้น ๆ เช่น `"a single red dot on white background"`
   - สำเร็จ → ภาพถูก save อัตโนมัติลง `GEMINI_OUTPUT_DIR` แปลว่า key + billing พร้อม
   - เจอ **429 / RESOURCE_EXHAUSTED** → billing ยังไม่เปิด หรือ key ผูกกับ Project ที่ไม่ได้เปิด billing → กลับไปที่ AI Studio Billing
2. **เช็ก session ที่ค้าง** — เรียก `gemini-list-image-sessions` เพื่อยืนยันว่า MCP server ติดต่อได้และไม่มี edit session ค้างจากรอบก่อน
3. **ยืนยันว่าเห็นภาพได้** — เรียก `gemini-analyze-image` กับไฟล์ที่เพิ่ง generate (ส่ง `imagePath` เป็น path เต็มใน `GEMINI_OUTPUT_DIR`) เพื่อยืนยันว่า round-trip generate → save → อ่านกลับ ทำงานครบวงจร

---

## ค่าใช้จ่ายโดยประมาณตาม Use Case

ตัวเลขอ้างอิงจาก default Pro และสมมติส่วนใหญ่ใช้ `2K`; เลื่อนขึ้นถ้าใช้ `4K` เป็นหลัก

| Use Case | ภาพ/เดือน | imageSize หลัก | Cost/เดือน (ประมาณ) |
|---|---|---|---|
| Personal Demo | 10-50 | 1K-2K | $1-5 |
| Side Project | 100-300 | 2K | $12-36 |
| Small Business Marketing | 500-1000 | 2K-4K | $60-120 |
| Agency / Heavy Use | 2000-5000 | 2K-4K | $240-600 |
| Enterprise / API Server | 10,000+ | 4K | $1,200+ |

---

## หลังเปิด Billing — ทำต่อทันที

1. **ทดสอบ Generate** — รัน `gemini-generate-image` ด้วย `imageSize: "1K"` ภาพเล็ก ๆ ตรวจว่าผ่านและไฟล์โผล่ใน `GEMINI_OUTPUT_DIR`
2. **ตรวจ Console** หลัง Generate 5-10 ภาพ ดูว่า Cost ตรงคาดหวัง (จำไว้ว่า default เป็น Pro ราคาสูงกว่ารุ่น flash)
3. **บันทึก Config** ของ MCP server `gemini` ไว้ (เผื่อย้าย Machine) — โดยเฉพาะ `command` path และ `GEMINI_OUTPUT_DIR`
4. **Setup Backup Key** เก็บ `GEMINI_API_KEY` สำรองไว้ที่ปลอดภัย เผื่อ key หลักโดน rotate/revoke
5. **Document ขั้นตอน** สำหรับทีม (ถ้ามีหลายคนใช้)

---

## Security Best Practices

1. **อย่า Commit API Key เข้า Git** — `GEMINI_API_KEY` อยู่ใน `~/.claude.json` ซึ่งไม่ควรเข้า repo; ถ้าจำเป็นต้องแชร์ config ให้ลบค่า key ออกก่อน
2. **Rotate API Key ทุก 90 วัน** — แม้ไม่มีเหตุการณ์ สร้าง key ใหม่ที่ https://aistudio.google.com/apikey แล้วอัปเดต `env.GEMINI_API_KEY`
3. **ตั้ง Quota Cap** — ป้องกัน Spike จาก Key Compromise โดยเฉพาะเพราะ default เป็น Pro ที่ราคาต่อภาพสูง
4. **Monitor Billing Daily** — ตั้ง Alert + ดูทุกเช้า 1 อาทิตย์แรกหลังเปิดใช้
5. **คุม imageSize ตามความจำเป็น** — ใช้ `1K`/`2K` สำหรับ draft, สงวน `4K` ไว้ภาพ final เพื่อกัน cost พุ่งโดยไม่ตั้งใจ
6. **เก็บ binary บน local disk** — อย่าวาง `gemini-mcp` บน iCloud/cloud sync เพื่อกัน MCP launch ล้มเหลว
