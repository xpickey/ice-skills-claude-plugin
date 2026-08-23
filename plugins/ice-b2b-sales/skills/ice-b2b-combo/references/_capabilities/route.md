# Capability — ROUTE (จัดเส้นทางงาน + คุมวินัย)

> ความสามารถ "ตัวคุมงาน" — ตัดสินว่างานนี้คืออะไร, ใช้ความรู้/วิธีไหน, ลึกแค่ไหน, และกันงานวนหรือพัง.
> โหลดไฟล์นี้เมื่ออยู่ STEP 0-1. หัวใจคือ 5 กลไก: Context-Lock · Mode · 4Q-Routing · Validation-Gates · Anti-Loop.

---

## 1. Context-Lock — ตรึงข้อเท็จจริงไว้ชุดเดียว

**ปัญหาที่แก้:** ทำงานหลายขั้น/หลายเอกสาร แล้วตัวเลขหรือชื่อขัดกัน (deck บอกงบ 12 ล้าน, proposal บอก 15 ล้าน).

**กลไก:**
1. เมื่อรู้บริบทแล้ว (STEP 0) จด *canonical facts* ไว้ชุดเดียว:
   ```
   customer        : <ชื่อ — ตามที่ผู้ใช้ให้ ไม่กุ>
   primary_product : <Oracle Cloud | EBS | NetSuite | FinTech>
   scope           : <โมดูล/ขอบเขตที่ตกลง>
   key_numbers     : <งบ · #user · timeline — เท่าที่ผู้ใช้ให้จริง>
   language        : <ภาษา output ที่ยืนยันแล้ว>
   stage           : <sale stage>
   decisions       : <สิ่งที่ตัดสินไปแล้วในงานนี้>
   ```
2. **ทุกขั้นถัดไปอ้างชุดนี้ชุดเดียว** — ห้ามมีตัวเลข/ชื่อจากที่อื่นมาแทรกโดยไม่ผ่านชุดนี้.
3. ผู้ใช้ให้ข้อมูลใหม่ → อัปเดต **ที่ชุดนี้ที่เดียว** แล้วงานอื่นอ้างตาม.

**กฎทอง:** ตัวเลขสำคัญ = มี source เดียว. ถ้าเอกสาร 2 ฉบับต้องใช้ตัวเลขเดียวกัน ให้ดึงจากชุดนี้ทั้งคู่.

---

## 2. Mode Selection — เลือกงบความพยายาม

2 มิติอิสระ (อย่าปนกัน):

**Orchestration Mode** (จะคิดกี่มุม):
| Mode | ใช้เมื่อ | ทำอะไร |
|---|---|---|
| **Fast** (default) | งานเดี่ยว ชัดเจน | ตอบตรง 1 มุม |
| **Full** | high-stakes / หลายทางเลือก | ชั่งน้ำหนัก 3 มุม ก่อนสรุป |
| **Submit** | มี deliverable ส่งลูกค้าจริง | ครบ build-spec + QA |

**ตัดสินใจ:** เริ่ม Fast เสมอ. เห็นสัญญาณ (คำว่า "เสนอลูกค้า"/"ผู้บริหาร"/"เลือกระหว่าง"/งบสูง) → ยกเป็น Full/Submit.
ไม่แน่ใจ → **ถามครั้งเดียวต่อ session** ("งานนี้ส่งลูกค้าเลยไหม / อยากให้ลงลึกแค่ไหน") ไม่ถามซ้ำ.

**RATCHET:** artifact ที่จะเป็น final ส่งจริง — ต้องผ่าน Submit + FULL QA เสมอ แม้ก่อนหน้าจะทำแบบ Fast.

---

## 3. Routing 4 คำถาม (first-hit-wins)

ตอบตามลำดับ ห้ามข้าม — คำตอบแรกที่ "ใช่" ตั้งโครงงาน:

1. **Q1 — Deliverable คืออะไร?** (proposal / RFP-TOR / business-case / account-plan / discovery-guide /
   demo-script / QBR / pricing / email-สรุป) → กำหนดโครงและ method หลัก.
2. **Q2 — ผูก product ไหน?** → กำหนด `product/<x>.md`.
3. **Q3 — มี domain overlay ไหม?** ภาครัฐไทย / ภาษีไทย / FinTech-IFRS9 → เพิ่ม `domain/<y>.md`.
4. **Q4 — industry ลูกค้า?** → ไม่เพิ่มไฟล์เสมอ แต่ปรับภาษา/ตัวอย่าง/KPI ให้ตรง vertical.

### Default chains (โหลดชุดไหนตามงาน — ไม่เกิน 5 ไฟล์)

**Pre-sales (hot path)** — Proposal / RFP-TOR / Business-case / Demo / Board paper:
```
strategic-thinking → solution-selling → product/<x> → domain/<y> (ถ้ามี) → [BUILD-SPEC]
```

**Strategic (standard)** — Account plan / Win plan / Competitive / QBR / Win-loss:
```
strategic-thinking → why-thinking → relationship-management → product/<x> (ถ้าเจาะ product)
```

**Communication (fast)** — Discovery prep / Sales email / Meeting summary:
```
questioning  OR  relationship-management   (ไฟล์เดียว artifact เดียว)
```

> ถ้า deliverable กำกวมว่าตรงกับ chain ไหน → `decision-matrix.md`

### Risk-Overlay Routing (route จาก deal-risk ไม่ใช่แค่ deliverable)

หลังเลือก chain จาก deliverable — เช็คว่ามี **deal-risk** ที่ต้องโหลด reference เพิ่มไหม (enterprise sales มัก route จาก risk):

| risk สัญญาณ | โหลดเพิ่ม / โฟกัส |
|---|---|
| **incumbent lock-in** (มีเจ้าเดิมอยู่) | solution-selling (reframe/displacement) + product/<x> (wedge strategy) |
| **budget owner ไม่ชัด** | `_shared/meddpicc.md` (Economic Buyer) — qualify ก่อนทุ่ม |
| **procurement trap** (ภาครัฐ/e-bidding) | `domain/govt-egp.md` + meddpicc Paper Process |
| **security/legal objection** | flag — ต้องข้อมูล security/compliance จริง (ไม่เดา) |
| **competitor นำ** | strategic-thinking (Why-Us) + product Primary-Lock เทียบ |

> deal-risk มักกำหนด move จริงมากกว่าชนิดเอกสาร — ถ้าเห็น risk ชัด ให้ route ตาม risk ก่อน.

### Fallback เมื่อ reference โหลดไม่ได้ (ตัวไหน fatal / ตัวไหนข้ามได้)

| reference | ถ้าหาย/โหลดไม่ได้ | ทำอะไร |
|---|---|---|
| `method/<x>.md` | **ข้ามได้** | สังเคราะห์จาก `_capabilities/` (route+know) + หลักทั่วไป + flag "ใช้กรอบทั่วไป ไม่ได้โหลด method เฉพาะ" |
| `product/<y>.md` | **กึ่ง fatal** | อย่าเดา product knowledge — ยืนยัน product/scope กับผู้ใช้ก่อน + flag ว่าตอบจากความรู้ทั่วไป ลด confidence |
| `domain/<z>.md` ทั่วไป (industry) | **ข้ามได้** (optional) | ทำงานต่อ แต่ note ว่าขาด overlay เฉพาะ |
| `domain/<z>.md` **regulated** (govt-egp, govt-gfmis, th-etax, fintech) | **fatal สำหรับ customer-facing** | กฎหมาย/ภาษี/จัดซื้อภาครัฐ/การเงิน — **ห้ามเดา** ในเอกสารลูกค้า → validate กับแหล่งทางการ หรือถามก่อน |
| `_shared/<c>.md` | **ข้ามได้** | concept พื้นฐาน — สังเคราะห์ได้ แต่ flag |

> หลัก: **product + regulated-domain (ภาษี/กฎหมาย/ภาครัฐ/การเงิน) = ห้ามเดาใน customer-facing** (กระทบความถูกต้อง + ความน่าเชื่อถือ) · method/industry-domain/shared = สังเคราะห์+flag ได้.

---

## 4. Validation Gates — ตรวจอะไรก่อนส่ง (ความเป็นเจ้าของ)

ก่อนส่ง deliverable เดินผ่านประตูเหล่านี้ (ข้ามได้ถ้าไม่เกี่ยว):

| Gate | ตรวจอะไร | ใครตรวจ (ในสกิลเดียว = ทำเองคนละขั้น) |
|---|---|---|
| G1 Numbers Foot | บวกลบถูก + ตัวเลขตรงกันข้ามเอกสาร (จาก Context-Lock) | ROUTE ขั้นนี้ |
| G2 Anti-Hallucination | ชื่อ/เลข/วันที่/version มี source | → CHECK (STEP 5 D3) |
| G3 Brand/Legal scrub | ไม่อ้างชื่อบริษัทที่ปรึกษา/methodology ที่ห้าม | ROUTE ขั้นนี้ |
| G5 Compliance/TOR | comply % ตรงจริง ไม่ปิดบัง | → CHECK (STEP 5 D9) |
| G7 Wording | positive 70/25/5 · เหมาะ stage | → CHECK (STEP 5 D8) |
| G8 Font/Visual | tri-slot + ไทย optical + ไม่ทับ | → CHECK (STEP 5 D7) |

**Closed-loop:** ทุก issue ที่เจอ ติดป้าย — แก้แล้ว / ผู้ใช้ตัดสิน / ไม่แก้+เหตุผล — ไม่ปล่อยลอย.

---

## 5. Anti-Loop — กันงานวนไม่จบ

**Cap ตาม mode:** Fast = วนแก้ 1 รอบ · Full = 2 · Submit = 3.

**เมื่อครบ cap แล้วยังไม่ลงตัว → STOP** แล้วเสนอ trade-off ให้ผู้ใช้เลือก เช่น:
> "ปรับมา 2 รอบแล้วยังชน 2 ข้อกำหนดที่ขัดกัน (timeline สั้น vs scope กว้าง) — เลือก (a) ลด scope ให้ทันเวลา
> หรือ (b) ขยาย timeline. บอกผมแล้วทำต่อให้เลย."

**ห้ามวนเองเกิน cap** — การวนต่อเงียบ ๆ = เปลือง token และมักได้ผลแย่ลง.

---

## 6. Positive Wording (Business-First) — เขียนสะอาดตั้งแต่แรก

- **ลดคำลบ → ทางบวก/ทางเลือก** โดยเฉพาะงานที่ลูกค้าอ่าน (แต่ไม่บิดความจริง — escalation ต้องตรงไปตรงมา).
- **Executive-grade prose:** ประโยคสมบูรณ์ ไม่ใช้ bullet ห้วน ๆ แทนการอธิบาย · ทุกคำแนะนำมี เหตุผล + trade-off + ทางเลือก.
- **เขียนสะอาดตั้งแต่ร่างแรก** (prevention) — ไม่ใช่เขียนมั่วแล้วค่อยตรวจ AI ปลายน้ำ.
- **Fix-in-place** — ปรับภาษาตรงนั้นเลย ไม่ส่งกลับไปกลับมาหลายรอบ.
