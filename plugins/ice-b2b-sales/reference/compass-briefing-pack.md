# Compass.Next — ซองคำสั่งและซองผลงาน: โครงเต็มของ Two-Tier Briefing Pack และ DISK-IS-TRUTH Brief (ย้ายมาจากไฟล์กัปตัน §8 เมื่อ 2026.09.05)

> **Version:** V01R01 | **Date:** 2026.09.05 | **ใช้โดย:** กัปตัน (`iCE-Compass-Next`) ทุกครั้งที่ส่งงานให้ specialist (ขั้น S3 DISPATCH) และ specialist ทุกตัวที่ต้องคืนงาน
> **ไฟล์นี้ใช้ทำอะไร:** เก็บโครงช่องครบทุกช่องของซองที่ใช้สื่อสารระหว่างกัปตันกับ specialist · ไฟล์กัปตัน §8 เหลือรายชื่อช่องบังคับและกติกาสั้น ส่วนโครงเต็มอยู่ที่นี่ · หลักการเบื้องหลัง (Core Pack ห้ามตัด · envelope กันการเดา) อยู่ที่ `reference/anti-loop.md` กลไก 2 และ 3
> **นิยามที่ไฟล์นี้ใช้:** ② `sales-process-agent` · ③ `solution-knowledge-agent` · ④ `deliverable-gen-agent` (เจนนี่ ทำงานเฉพาะเมื่อ user เรียกชื่อตรง) · ⑤ `qa-master-agent` · ⑥ `retrieval-scout-agent` (เสี่ยวป้อ เก็บวัตถุดิบ) · ⑦ `demo-builder-agent` (โมโม่ สร้าง demo app) · **Core Pack** = ส่วนแกนที่ส่งครบทุกครั้งห้ามตัด · **Section Pack** = ส่วนราย section ที่ตัดทอนได้ · **envelope** = โครงคำตอบที่ specialist คืน · **DISK-IS-TRUTH** = ผลงานจริงอยู่บนดิสก์ ซองเป็นเพียงใบแจ้ง · **A1 / H2** = ด่านขออนุญาต user ก่อนออก internet ตามกฎเหล็ก H2 ของ `~/.claude/CLAUDE.md` · **codex_scope** = ขอบเขตที่ user เปิดให้ใช้ Codex หรือ OpenRouter (โหมด A-E อยู่ที่ skill `claude-codex-bridge`) · **K1** = กติกา brief 4 ช่อง objective / cannot_change / can_change / process (ไฟล์กัปตัน §2)

## Two-Tier Briefing Pack — ฝังในทุก dispatch

```yaml
# ── CORE PACK ── ส่งครบทุก agent ทุกครั้ง (ห้ามตัด ~150 token)
core_pack:
  customer: "<ชื่อ | (internal)>"
  product: "<product>" · primary_product: "<1 ตัว — ③ ล็อก product หลักกันปน>" · primary_industry: "<1 ตัว>"
  phase: "<Pre-Sale|Deal|Customer>" · language_directive: "<TH|EN|TH+EN-tech|Bilingual>"
  wording_discipline: { mode: "<Neutral|Positive-Dominant|Honest-Reframe>" }
  objective: "<นิยามเสร็จที่วัดได้>"          # K1 4 ช่อง
  cannot_change: [ "<ห้ามแตะ — รวม brand_locks และตัวเลขทางการ>" ]
  can_change: [ "<เขตอิสระของ specialist>" ] · process: [ "<optional>" ] · brand_locks: [ "<คัดลอกตามตัวอักษร>" ]
  codex_scope: "none | available | instructed" · codex_mode: "<A-E เมื่อ instructed>"
  memory_paths: { team_memory: "<path โปรเจกต์ปัจจุบันเท่านั้น>", opportunity_context: "<เดียวกัน>" }
  # ISOLATION: แนบได้เฉพาะ path ใต้โปรเจกต์ปัจจุบัน · specialist ห้ามอ่าน memory โปรเจกต์อื่น ·
  # การเรียนรู้ข้ามโปรเจกต์ทำผ่าน Portfolio Mode แบบถอดชื่อลูกค้าเท่านั้น (กติกาเต็ม reference/team-memory.md)
  core_pack_locked: true · call_chain: ["iCE-Compass-Next"] · call_depth: 1

# ── SECTION PACK ── เฉพาะ agent ที่ทำ section นั้น (ตัดทอนได้ ~400 token)
section_pack:
  key_facts: [ "<ตรวจแล้ว — คัดลอก ไม่แต่งเพิ่ม>" ] · build_safe_rules: [ "<บทเรียน PPTX ใน ice-doc-builder §2>" ]
  term_policy: { register: Professional-B2B, rule: "ice-writing-register ข้อ 3 (ลำดับเลือกศัพท์)", keep_english: [...],
                 verify_feature_names: true, audit_all_sources: true }   # บังคับเมื่อไทยหรือสองภาษา + เนื้อหาเทคนิค
  section_spec: { id, title, key_message, slides: [...] }
  cb_unit_spec: { unit_id, unit_type, position, frame_ref, build_scope, content, reviewer_verdict }  # Composed Build เท่านั้น
  comparison_scope: [...] · comparison_dimensions: [...] · requirement_source: "<path TOR — qa_mode=compliance>"

# ── REFERENCE PATHS ── ทางออกสำรองเมื่อสิ่งที่ฝังไม่พอ
reference_paths: [ "<memory/playbook path>" ]
```

**Output Schema ที่ห่อ Pack ตอนส่ง:** `caller / target_agent / task / core_pack / section_pack / qa_mode: <quality|compliance|both|skip> / orchestration_mode / expected_output_type`

**กติกาการฝัง:** brand_locks · key_facts · section_spec ฝังในซองโดยตรง ไม่ให้ specialist ไปหาเอง · เมื่อกติกาขัดกัน Anti-Hallucination (H3) ชนะทุกข้อ · ถ้อยคำงานขาย B2B ตรวจโดยกัปตัน (fix-in-place) + skill ice-writing-register + อริส D5 — ไม่ส่งเข้าเส้นทางตรวจภาษาวิชาการ

## DISK-IS-TRUTH Brief — สำหรับ ④ / ⑥ / ⑦ และ specialist ที่คืนงานหนัก

ทำไมต้องมี: งานที่ stream ยาวหลุดง่าย เกิดกรณี "ไฟล์รอดแต่ซองหาย" · จึงส่ง brief เล็กที่สุด (paths-only ไม่เกิน 20 บรรทัด ห้ามแนบเนื้อหาก้อนใหญ่) และให้ผลลัพธ์จริงอยู่บนดิสก์ ซองเป็นเพียงใบแจ้ง

```yaml
disk_brief:
  role: "builder(④) | scout(⑥) | demo(⑦)"
  spec_paths: [ "<content-spec หรือ DEMO-SPEC>", "<design-spec>" ]
  query_or_targets: [ "<url|folder|topic>" ]      # ⑥
  deal_type: "<ชนิดดีล เช่น FMCG/แฟชั่น ขายหลายช่องทาง>"   # ⑥ — ด่านตรวจความครบของวัตถุดิบฝั่ง ⑥ ทำงานเมื่อบอกเท่านั้น
  chunk_id: "<ชิ้นไหนใน DEMO-SPEC>"                # ⑦
  data_set: "<ชุดข้อมูล>" · consent_status: "<จริง-ยินยอมแล้ว | แปลงสมจริง>"   # ⑦ — Demo Data Policy
  output_dir: "<path>" · version: "V##R##"        # ④
  result_md: "<_build-result.md | _gather-result.md>"
  core_pack: { ... — codex_scope ของ ④ และ ⑦ = none เสมอ }
  internet_permission: "granted-by-user | none"   # ⑥ — A1/H2
return: { status, artifact_paths: [...], result_md_path, counts, note }   # 5 บรรทัด
# ซองไม่กลับ → STALL WATCHDOG (ไฟล์กัปตัน §6): อ่าน result_md และ ls เอง
```

*Reference: compass-briefing-pack.md V01R01 | ที่มา: ไฟล์กัปตัน V05R16 §8 บรรทัด 481-534 (ช่อง deal_type เพิ่มจาก S0 บรรทัด 140 ซึ่งเป็นกติกาเดิม)*
