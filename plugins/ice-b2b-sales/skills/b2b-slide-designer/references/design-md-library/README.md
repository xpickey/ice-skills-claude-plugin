# DESIGN.md Library — Brand Design-Language Tokens (curated 12/73)

> **V01R01 | 2026.07.10** · ที่มา: [VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (MIT © 2026 VoltAgent) — DESIGN.md = design system เป็น plain-markdown ที่ agent อ่านแล้วสร้าง UI ตาม design language ได้ (แนวคิดจาก Google Stitch) · แต่ละไฟล์มี: color tokens (hex ครบ) · typography ราย level · spacing · component rules · voice

## ใช้เมื่อไร (Router §4.5 เรียกมาที่นี่)

1. **HTML deck / dashboard / microsite** — token → CSS vars ตรง ๆ (ต่อกับ §5.6 html-styling-export)
2. **Customer-CI co-brand** — ลูกค้ามี design language ใกล้แบรนด์ไหน → ใช้ token เป็นจุดตั้งต้น แล้ว override ด้วย CI จริงจาก customer-ci-finder
3. **Internal mockup / demo UI** (Lovable/Stitch-style) — วางไฟล์เป็น DESIGN.md ใน project แล้วให้ agent สร้างตาม

## ⚠️ BRAND GUARD (บังคับ — อ่านก่อนใช้ทุกครั้ง)

- นี่คือ design language ของ**แบรนด์จริง** — ใช้เป็น (ก) reference โครง token/ระดับคุณภาพ (ข) internal mockup (ค) จุดตั้งต้นเมื่อ CI ลูกค้าใกล้เคียง
- **ห้ามส่งงาน customer-facing ที่เป็นหน้าตาแบรนด์คนอื่นตรง ๆ** (สี+font+voice ครบชุด = เลียนแบรนด์) — งานส่งลูกค้า = iCE CI หรือ CI ลูกค้าเสมอ · token ที่หยิบมาต้องถูก override จนเป็นของเรา/ของลูกค้า
- อริส D6.lib (template/brand fidelity) จะ FLAG deviation ให้ตรวจ — ตามระบบเดิม
- ห้ามอ้างชื่อแบรนด์ต้นทางใน deliverable (No Name-Dropping — ใช้ token ได้ ไม่ต้องบอกที่มา)

## Curated 12 (เลือกตามงาน B2B/enterprise/fintech/AI ของ iCE)

| ไฟล์ | โทน/เหมาะกับ |
|---|---|
| `claude.md` | warm cream + serif editorial — AI demo, งานที่อยากอบอุ่นไม่ cold-tech |
| `apple.md` | premium minimal — executive/board deck |
| `stripe.md` | fintech/SaaS มาตรฐานทอง — product page, developer-facing |
| `linear.app.md` | SaaS คมกริบ dark-friendly — modern dashboard |
| `airtable.md` | data/SaaS สีสดเป็นระบบ — data product |
| `clickhouse.md` | enterprise data/tech — technical deck |
| `cohere.md` | enterprise AI — AI solution สาย corporate |
| `coinbase.md` | fintech regulated — BFSI/สถาบันการเงิน |
| `wise.md` | fintech cross-border สดใส — payment/remittance |
| `ibm.md` | enterprise classic (Carbon) — องค์กรใหญ่/ราชการ modern |
| `mastercard.md` | payments/BFSI brand system |
| `vercel.md` | dev-tool dark modern — demo/microsite เท่ ๆ |

## ต้องการแบรนด์นอก 12 ตัวนี้ (มีทั้งหมด 73)

รายชื่อเต็ม: airbnb airtable apple binance bmw-m bmw bugatti cal claude clay clickhouse cohere coinbase composio cursor dell-1996 elevenlabs expo ferrari figma framer hashicorp hp ibm intercom kraken lamborghini linear.app lovable mastercard meta minimax mintlify miro mistral.ai mongodb nike nintendo-2001 notion nvidia ollama opencode.ai pinterest playstation posthog raycast renault replicate resend revolut runwayml sanity sentry shopify slack spacex spotify starbucks stripe supabase superhuman tesla theverge together.ai uber vercel vodafone voltagent warp webflow wired wise x.ai zapier

ดึงเพิ่ม (ครั้งละไฟล์ที่ต้องใช้ — อย่า copy ทั้งหมด กัน bloat):
```bash
gh api -H "Accept: application/vnd.github.raw" \
  "repos/VoltAgent/awesome-design-md/contents/design-md/<brand>/DESIGN.md" \
  > ~/.claude/skills/b2b-slide-designer/references/design-md-library/<brand>.md
```
ดึงแล้วเพิ่มแถวในตารางข้างบน + sync plugin ตอน deploy รอบถัดไป
