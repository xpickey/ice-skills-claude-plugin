# Team Memory — `_team-memory.md` Schema & Rules (ONE-HOME)

> **Version: V01R01 | 2026.07.10** — หน่วยความจำร่วมของทีม agent ระดับ opportunity/project
> **เป้าหมาย (คำสั่ง user):** ทุก agent ในงานเดียวกัน **เห็น goal เดียวกัน** · แชร์ปัญหา/bug/บทเรียนถึงกัน · ทำงานต่อเนื่องข้าม session
> **ที่มา:** business-adapted จาก `thedotmack/claude-mem` (typed observations + session digest + inject-at-start + dedup + never-block) — เอา **data model** ไม่เอา infra (daemon/SQLite/Chroma) · ออกแบบตาม memory best practice ของ Claude: 1 รายการ = 1 ข้อเท็จจริง · pointers ไม่ใช่ payloads · อัปเดตแทนสร้างซ้ำ · ลบของผิด/จบแล้ว

## LOCATION + TEMPLATE

```
LOCATION: Projects/{Account}/{Opp}/00 - Context/_team-memory.md   (1 ไฟล์/opportunity)
CREATE:   lazy — L1 สร้างจาก template นี้ครั้งแรกที่แตะงานนั้น (ดึง Goal จาก ledger/context เดิม)

# Team Memory — {Account}/{Opp}
> updated: YYYY.MM.DD โดย {agent} · cap 120 บรรทัด — ชนแล้ว prune ก่อนเขียนเพิ่ม

## Goal & Plan (canonical — ≤10 บรรทัด · L1 ดูแล)
- GOAL: <เป้าหมายหลักของงานนี้ 1-2 ประโยค>
- PLAN: <แผน/phase ปัจจุบัน + นิยามเสร็จ>
- NOW: <กำลังทำอะไร · next action>

## Known Issues & Bugs (เปิดอยู่ — ปิดแล้วลบออก · ถ้าเป็นบทเรียนย้ายลง Observations)
- [ ] KI-01 <ปัญหาที่ทีมต้องรู้ · ใครเจอ · วันที่>

## Observations (1 บรรทัด = 1 ข้อเท็จจริง · เนื้อยาวชี้ path ไม่ copy มาแปะ)
- [bug|decision|lesson|watch-out|fact] <ข้อเท็จจริง> (ใคร · YYYY.MM.DD)

## Session Digests (ล่าสุดบนสุด · เก็บ ~10 — เกินลบเก่าสุด)
- YYYY.MM.DD {agent}: ทำ<อะไร> · เรียนรู้<อะไร> · เสร็จ<อะไร>
```

## กติกาอ่าน-เขียน (งบความเร็ว — บังคับ ไม่ใช่แนะนำ)

| ฝั่ง | กติกา |
|---|---|
| **อ่าน** | ทุก agent อ่านที่ step แรกของ loop (S0/K0/T0/E1) · **L2 อ่านเฉพาะ 2 หมวดบน** (Goal & Plan + Known Issues — รวม ≤40 บรรทัด) · L1 อ่านทั้งไฟล์ได้ |
| **เขียน** | **L1 เท่านั้น** (กัปตัน/คิม/สมนึก — single-writer ต่องาน กันเขียนชน = one-owner-per-state) · L2 ส่ง observations ใน envelope `run_data.observations[]` → L1 คัด+**dedup** (มีแล้ว→อัปเดตของเดิม)+เขียน · **รวบ 1 ครั้ง/งาน หลังส่งมอบงานให้ user แล้วเสมอ** (Deferred — ห้ามเขียนกลางงาน) · งานจิ๋ว/ไม่มีอะไรใหม่ → no-op |
| **เพดาน** | ทั้งไฟล์ ~**120 บรรทัด** — จะเขียนแล้วเกิน → prune ก่อน (บังคับ): ลบ digest เก่าสุด → ลบ KI ที่ปิดแล้ว → ยังเกิน → ย้ายส่วนเก่าไป `_team-memory-archive.md` |
| **พัง** | อ่านไม่ได้/ไฟล์หาย → **ทำงานต่อทันที ไม่หยุดรอ** · แจ้ง user 1 บรรทัด · L1 สร้างใหม่จาก template ตอนจบงาน (memory ห้าม block งาน) |

## ความสัมพันธ์กับ state files อื่น (ไม่ซ้ำหน้าที่)

| ไฟล์ | บทบาท | เมื่อขัดกัน |
|---|---|---|
| `_opportunity-context.md` | ข้อเท็จจริง deal (key_facts/decisions/brand locks) — **canonical** | **context ชนะเสมอ** → จดความขัดแย้งเป็น observation ให้ user เห็น |
| `_team-memory.md` | ความรู้ร่วมอายุยาว (goal กลาง/bug/lesson/digest) | — |
| `_status-ledger.json` | สถานะ machine-readable ให้ Kim อ่าน | ledger = status · memory = ความรู้ |
| Two-Tier Pack | push คำสั่งเฉพาะ task | pack = คำสั่งครั้งเดียว · memory = ยืนข้าม session |
| QA log ต่อ artifact | ประวัติ issue ราย artifact | QA log ละเอียดราย artifact · memory = ภาพรวมที่ทีมต้องรู้ |

## ⭐ MEMORY ISOLATION by Project (V01R02 — Hard Rule · คำสั่ง user 2026.07.13)

- **ระดับการแชร์ = PROJECT:** ทุก agent ที่ทำงานในโปรเจกต์เดียวกันอ่าน `_team-memory.md` ชุดเดียวกัน — **ข้ามโปรเจกต์ห้ามมองเห็นกัน**
- **ฝั่ง dispatch (L0/L1):** `memory_paths` ใน Pack แนบได้เฉพาะ path ใต้โปรเจกต์ปัจจุบัน (path-prefix check แบบเดียวกับ PATH ENFORCEMENT ใน state-io) — path นอกโปรเจกต์ = violation แจ้ง user
- **ฝั่ง L2:** ห้ามเปิดอ่าน team-memory ของโปรเจกต์อื่นแม้รู้ path · ได้ path นอกโปรเจกต์มา → รายงานเป็น blocker ไม่อ่าน
- **Cross-project learning:** ทางเดียวที่อนุญาต = Portfolio Mode (กัปตัน Job 7) เป็น **pattern ถอดชื่อลูกค้าแล้วเท่านั้น** (สอดคล้อง Conditional Customer Naming anti-leak)

## Prevention & Remediation (ตาม D4 ของแผน)

- **ป้องกัน:** cap 120 + L2 อ่าน 2 หมวดบน + เขียน 1 ครั้ง/งาน + single-writer + dedup + prune บังคับ + Goal ≤10 บรรทัด + ISOLATION by project
- **แก้ไข:** ไฟล์หาย → สร้างใหม่จาก template+ledger (ไม่หยุดงาน) · บวม → prune procedure → archive · ข้อมูลขัด context → context ชนะ + จด observation · เนื้อหาผิด → ลบ/แก้ทันทีที่พิสูจน์ (ไม่เก็บของผิดไว้หลอกตัวเอง)

*Version V01R02 (2026.07.13 — +ISOLATION) · ใช้โดย: กัปตัน V03R03 (S0/S6 + §8 memory_paths) · คิม V02R02 (K0/K6) · สมนึก V02R02 (T0/T6) · L2 ทั้ง 4 V02R02 (E1 อ่าน · E5 ส่ง observations)*
