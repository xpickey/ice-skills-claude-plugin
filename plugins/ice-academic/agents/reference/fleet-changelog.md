# Fleet Changelog — ประวัติเวอร์ชันของ agent ทั้ง fleet (ยกเว้นกัปตันที่มี compass-changelog.md)

> **Version: V01R02 | 2026.07.13** — history ที่ย้ายออกจาก body ของแต่ละ agent ตอน Fleet Rewrite V2 (2026.07.10) เพื่อให้ main prompt เหลือเฉพาะกฎที่ใช้ตอนนี้ · อ่านเมื่อต้องการเหตุผลเบื้องหลัง/ทำ version ถัดไป

---

## ⭐ DOC-PIPELINE Wave (2026.07.13 — ทุกตัวพร้อมกัน · กัปตัน V03R03 + fleet V02R02 + CLAUDE.md V09R04)

**Root cause (หลักฐานจาก transcript Viriyah `0d9285cb` + EuroFood `7b2c7bd2` + Akara `0477f9ca`):** ผู้เล่นบทกัปตันตัวจริงคือ L0 ที่เปิด ultracode → content+build หลุดไป **Workflow generic subagent** (ไม่มี agentType สักตัว) + **build Excel inline 400+ จุด** — **เจนนี่ถูกเรียก 0 ครั้ง** ใน session ที่มีการ build · เทพถูกห้าม author content → content เชิง solution เป็นเด็กกำพร้าใน Routing

**สิ่งที่ทุกตัวได้ (2026.07.13):**
- **2-Tier Invocation** — Tier 1 spawn L1 ได้เฉพาะงานเดี่ยว · Tier 2 orchestration = L0 Read ไฟล์ L1 adopt เป็น **Operating Manual** (encode ใน description ทั้ง 3 L1 กัน harness auto-spawn ผิด tier)
- **Persona Loading 3 ชั้น** — ชั้น A: CLAUDE.md V09R04 PART 4 · ชั้น B: folder CLAUDE.md ×4 ใหม่ (Projects→กัปตัน · Academic→สมนึก · Customer+Working Email→คิม) · ชั้น C: ไฟล์ L1
- **DOC-PIPELINE (id16 ในกัปตัน §5)** — default ทุก file deliverable: D-P1 content (กัปตัน+③ CO-AUTHOR +② เมื่อ sales-process · CONTENT-READY GATE) → D-P2 visual (กัปตัน+④) → D-P3 ④ build+SAVE → D-P4 ⑤+Codex review บนไฟล์ที่ save → D-P5 fix ฉบับเดียว+SAVE · PLAN-CARD-FIRST + DELIVERY REPORT
- **WORKFLOW GUARD** — ทุก stage ต้องระบุ agentType (②③④⑤/Explore · ชื่อ user-level) · generic ห้าม content/build/QA
- **MEMORY ISOLATION by project** — memory_paths ใน Pack แนบได้เฉพาะโปรเจกต์ปัจจุบัน (team-memory ref V01R02)

**รายตัว:** กัปตัน V03R03 (8 จุด — ดู compass-changelog) · คิม V02R02 (OPERATING MANUAL + K3 DOC-PIPELINE + GUARD) · สมนึก V02R02 (OPERATING MANUAL + GUARD) · เจนนี่ V02R02 (⭐ CONTENT-DESIGN REJECT ใน E0 + D-P2/D-P3 roles + SAVE ทันที) · เทพ V02R02 (⭐ CO-AUTHOR MODE ใน E3 — FACT Gate + handoff-ready) · ก้อง V02R02 (D-P1 author ตาม Q-CONTENT-B) · bridges×2 V02R02 (D-P4 reviewer + counts→fix list เดียว) · อริส = ไม่แก้ (detector เดิมถูกอยู่แล้ว)

---

## Fleet Rewrite V2 (2026.07.10 — ทุกตัวพร้อมกัน)

**สิ่งที่ทุกตัวได้เหมือนกัน:** โครง clean (L1 = MAIN LOOP เต็ม · L2 = E0-E5) · ONE-HOME · F1-F7 (+B1-B4/K1/K3 ตามชั้น) · Envelope V2 (**evidence บังคับเมื่อ ready** + run_data{codex_turns, observations}) · team-memory (อ่านที่ step แรก · L2 ส่ง observations) · codex_scope Authorization (Matrix = skill claude-codex-bridge) · อ้าง CLAUDE.md V09R03 · แก้ version stale ในไฟล์เดิม (เทพ header≠footer · ยอดนักขาย footer เก่า · เจนนี่ footer V01R01 ทั้งที่จริง V01R17)
**Model (D1):** L1 = inherit (กัปตัน/คิม/สมนึก/สะพาน/openrouter) · L2 = opus (อริส/เทพ/ยอดนักขาย/เจนนี่)
**Design doc:** `Documents/Claude/Custom Agents/Fleet-Design_V01R01_2026.07.10.md` · แผน: `~/.claude/plans/agent-cheerful-river.md`

---

## kim-assistant (เลขาคิม)
- **V02R01 (2026.07.10)** — Major Rewrite: K0-K6 + L1-L8 + F/B/K + evidence + team-memory + ⭐ Gatekeeper Codex/OpenRouter Card (ปิด gap "ยามไม่มีกุญแจ" — เดิมถูกตั้งเป็น gatekeeper ในไฟล์อื่นแต่ตัวเองไม่มีเนื้อหา Codex เลย) · FRESHNESS CHECK ยกเป็นขั้นทางการใน K0
- V01R03 (2026.06.14) — AI imagery pointer (nanobanana/higgsfield — build ผ่านเจนนี่) 3 จุด · ไม่ bind mcp ตรง
- V01R02 (2026.06.13) — +[P6] Write-Clean Card pointer (B-General)
- V01R01 (2026.06.01) — NEW agent (Personal Assistant peer ของ Compass)

## thesis-ai-det-col-agent (ผู้ทรง/สมนึก/หลวงพี่)
- **V02R01 (2026.07.10)** — Major Rewrite: T0-T6 + ⭐ K2 AutoResearch (humanize วัดคะแนนก่อน-หลัง แก้ทีละมิติ ห้ามบอกเสร็จไม่มีตัวเลข) + ⭐ Breaker (คะแนนไม่ลด 2 รอบ = STOP) + evidence + Codex Card (**เปิดใช้เมื่อ user ระบุเท่านั้น** · division: Claude=calque/particle · Codex=surface/burstiness) · Worked Example ย่อ
- V01R07 (2026.06.25) — +OpenRouter option ข้าง Codex
- V01R06 (2026.06.14) — ผูก skill research-compass-nrct (นักวิจัยวช) + ชื่อเล่น "หลวงพี่"
- V01R05 (2026.06.14) — AI imagery awareness pointer (ไม่ใส่ mcp_tools)
- V01R04 (2026.06.13) — +Write-Clean Card pointer (Companion หลัง Step 0)
- V01R03 (2026.06.09) — ปิด drift Five→Six Modes (+Mode 6 ADD SOUL) · +Orchestration Mode + 3-Namespace + Matrix 12 + LOOP CAP
- V01R02 (2026.06.07) — ผูก TAAE 7-Phase engine + Step 0 Resolve Standard + Phase ownership
- V01R01 — initial

## qa-master-agent (เจ้ระเบียบ/อริส)
- **V02R01 (2026.07.10)** — Major Rewrite: E0-E5 + ⭐ evidence บังคับทุก dimension_result + team-memory read (ไม่ตรวจซ้ำ FIXED + รู้ bug ทีม) + Codex Card (codex_scope-gated · **ผลตรวจภายนอก map เข้า detected_issues[] + counts format เดียว**) · engines ครบเดิม (D5/D5.TL · D7×3 · D6.lib/D7.S · D9 · TAAE)
- V01R08 (2026.06.25) — +OpenRouter option · V01R07 (2026.06.24) — +D5.TL Term-Localization scan (เคส VFIN) +2 categories
- V01R06 (2026.06.22) — +D7.S Visual Anti-Slop (FLAG ไม่ block) · V01R05 (2026.06.20) — +Design-Library REVALIDATE (detector not decider)
- V01R04 (2026.06.20) — +D7-HTML track · V01R03 (2026.06.13) — +Write-Clean Card pointer
- V01R02 (2026.06.07) — Academic QA Mode + TAAE Phase 0,1,3,4,5,7 ownership · V01R01 — initial

## solution-knowledge-agent (เทพ/อาจารย์โป้ง)
- **V02R01 (2026.07.10)** — Major Rewrite: E0-E5 + ⭐ evidence บังคับใน verify_verdict ทุกชิ้น (ปิด "PASS ลอย ๆ") + team-memory + Codex Card (**refuter ไม่ใช่แหล่งข้อเท็จจริง — ทุก claim ผ่าน FACT Gate ก่อนติด tag**) · แก้ version ขัด (header V01R03 ≠ footer V01R04 → ยึด V01R04 เป็นฐาน)
- V01R04 (2026.07.02) — +Competitive TOR KB pointer (NetSuite vs Fusion vs SAP · BALANCED FACT-gate · 11 industries)
- V01R02 (2026.06.13) — +[P4] Write-Clean Card pointer · V01R01 (2026.06.01) — initial (Router-Shell รวม 21 agents)

## sales-process-agent (ยอดนักขาย/เฮียก้อง)
- **V02R01 (2026.07.10)** — Major Rewrite: E0-E5 + evidence (ทุกตัวเลขชี้แหล่ง) + team-memory + รับ 3 L1 · **ไม่มี Codex card โดยตั้งใจ** (② = author — ตรวจงานตัวเองขัด Producer≠Checker) · แก้ footer stale (V01R02 → จริง V01R03)
- V01R03 (2026.07.04) — +§Pitch Philosophy (SELLING STANCE: belief→proof) → pointer Pitch-Belief Card SSOT
- V01R02 (2026.06.13) — +Write-Clean Card pointer (B-Business) · V01R01 (2026.06.01) — initial (3→1)

## deliverable-gen-agent (เจนนี่/แจน)
- **V02R01 (2026.07.10)** — Major Rewrite เข้มข้น 4 ชั้น: E0-E5 + Build Knowledge Base §4 (**D1-D4 + 18 lessons + Method B 5 เงื่อนไข + Validator = คงคำต่อคำทุกบรรทัด — sweep รายข้อ ~140 anchors ผ่าน missing 0**) + evidence ใน validator_report (ตัวเลขจริง) + team-memory + Codex Card (codex_scope-gated · Preset 3 review build script · **ไม่แทน γ1/Validator**) · แก้ footer stale หนัก (V01R01 → จริง V01R17) · changelog 16 รายการย้ายมาที่นี่
- V01R17 (2026.07.04) — +Credibility Lens (VISUAL CREDIBILITY ของ Pitch-Belief Card) · V01R16 (2026.06.25) — +OpenRouter option
- V01R15 (2026.06.24) — +Progressive Per-Unit Build (CB · Validator-LITE/FULL) · V01R14 (2026.06.24) — +[P6] Card B6 Term-Localization (VFIN)
- V01R13 (2026.06.22) — +Design Discipline pointer (Anti-Slop + 6-Axis) · V01R12 (2026.06.20) — +Preview-First · V01R11 (2026.06.20) — +Design Library Router + FONT/ICON RULE
- V01R10 (2026.06.20) — +Document-Type Routing Matrix 12 · V01R09 (2026.06.20) — +Dual Execution Path HTML · V01R08 (2026.06.20) — +HTML deck output (skill-owned build)
- V01R07 (2026.06.17) — +Higgsfield official task skills ×4 · V01R06 (2026.06.14) — +Execution Path Rule (CLI/MCP) · V01R05 (2026.06.13) — +AI Imagery binding (gemini+higgsfield)
- V01R04 (2026.06.13) — +[P6] Write-Clean pointer · V01R03 (2026.06.13) — +Lesson #18 U+2192 · V01R02 (2026.06.09) — +Lesson #17 avLst · V01R01 (2026.06.01) — initial (7→1 + 16 lessons จาก TQR)

## codex-bridge-agent (สะพานโคเด็กซ์)
- **V02R01 (2026.07.10)** — +Modes A-E + Review Contract (counts/stagnation ผ่าน skill ref 05 + verdict.schema.json) + Shard orchestration + Degradation Ladder + codex_turns report + model: inherit
- V01R01 (2026.06.22) — initial thin wrapper (PROPOSE→CRITIQUE→REFINE + LOOP CAP + read-only default)

## openrouter-agent (ที่ปรึกษาหลายโมเดล)
- **V02R01 (2026.07.10)** — +Modes A-E (contract ชี้ claude-codex-bridge ONE-HOME) + counts/stagnation (fallback ชั้น 2-3 — ไม่มี output-schema) + persona=Mode D + model: inherit · ของเฉพาะตัวคงครบ (picker/persona/cost/key guard)
- V01R01 (2026.06.25) — initial. พี่น้อง codex-bridge (curl helper + history-resend + alias picker + persona preset)

## skill: claude-codex-bridge
- **V02R02 (2026.07.10 บ่าย)** — +helper `--model` passthrough (terra/luna/5.5 ต่อ call · feature-detected) · config default → gpt-5.6-terra · CLI 0.137→0.144.1 re-probed · ทดสอบจริง 4 ข้อผ่าน
- **V02R01 (2026.07.10)** — +Modes A-E · +ref 05 Review Contract + verdict.schema.json · +helper V02 (--session/--list-sessions/--schema + feature-detection + overwrite guard) · +Authorization Matrix + codex_scope (ONE-HOME) · +Degradation Ladder · ref 01 +Probe 2026.07.10 (--output-schema/resume-positional) · ref 02 +REVIEW shape + Shard
- V01R02 (2026.06.22) — +4 presets + fleet binding · V01R01 (2026.06.22) — initial

*Fleet Changelog V01R01 | 2026.07.10 | คู่กับ: compass-changelog.md (กัปตัน) · Fleet-Design_V01R01 (design doc)*

## QA Record — Codex Dogfood Review (2026.07.10 · Mode B + verdict.schema.json)
- **helper ask-codex.sh:** R1 พบ 0C/3H/4M (H1 dot-session ทะลุทับ default thread · H2 dash-prompt กินเป็น flag · H3 UUID fallback เสี่ยงผิด thread · M1-M4) → แก้ครบ + ทดสอบจริง 5 ข้อ → **R2: 0/0/0 · fixed_verified ทั้ง 7 — CONVERGE**
- **deliverable-gen (เจนนี่) knowledge-loss audit:** R1 พบ 0C/1H (xlsx formula-integrity หลุดจาก E4 บังคับ) + context_repair (E4 แยกตาม format) → แก้ทั้งคู่ → **R2: 0/0/0 · H1 fixed_verified — CONVERGE**
- บทเรียนใหม่: (1) OpenAI --output-schema = strict mode (ทุก object ต้อง required ครบทุก property — verdict.schema.json V01R02 แก้แล้ว) (2) error "models cache: unknown variant max" ของ codex = noise ไม่ fatal (3) network DNS หลุดชั่วคราว → retry 1 ครั้งพอ

## 2026.07.13 (บ่าย) — DOC-PIPELINE V2 + FAILURE PROTOCOL (root cause: MEA/Akara/Viriyah audit)
- **กัปตัน V03R04**: DOC-PIPELINE V2 (D-P1 READ-FIRST กัปตันอ่าน source เองเป็นหลัก + ผู้อ่าน ≤3 · D-P2 +Codex option · D-P4 อริส+Codex → กัปตัน FINAL รายข้อ · D-P5 ④ fix-only) + FAILURE PROTOCOL §6 (retry 1 → หยุดถาม user · ห้าม silent fallback · [EXCEPTION] ลง team-memory) + EVIDENCE FRESHNESS (S5) + Process Compliance ใน DELIVERY REPORT + QA-log บังคับ (§9 → reference/doc-qa-log.md)
- **คิม V02R03 / สมนึก V02R03**: DOC-PIPELINE V2 ฉบับตัวเอง (ผู้อ่านหลัก + FINAL = ตนเอง) + FAILURE PROTOCOL ย่อ + Process Compliance · สมนึก: Codex option ทุกจุด = user ระบุเท่านั้น (Matrix เดิม)
- **เจนนี่ V02R03**: BUILD MARKER `ICE_BUILDER=jenny` ทุกคำสั่ง build (ผูก PreToolUse hook) + D-P5 fix-executor (รับเฉพาะ fix list ที่ L1 FINAL แล้ว)
- **อริส V02R02**: EVIDENCE FRESHNESS Hard Rule ใน E4 (render สดเท่านั้น + บันทึกคำสั่ง/dpi/เวลา — บทเรียน Akara PNG เก่า → regression) + บท D-P4 detector→L1 FINAL
- **refs**: team-memory V01R03 (+[EXCEPTION] entry) · doc-qa-log V01R01 (ใหม่ — template จาก EuroFood) · folder CLAUDE.md ×4 V01R02 · hook ice-prebuild-guard.sh V01R01 (ทดสอบ live: block ✓ / marker pass ✓)
- Evidence audit: EuroFood = reference implementation (pipeline ถูกครบ) · Akara = กัปตัน build+QA inline เมื่อ subagent+classifier ล่ม · MEA = ไม่มี spec/QA-log · Viriyah = เจนนี่ถูกสั่ง content + workflow generic

## 2026.07.14 — READ-SELF FIRST + hook V01R02 read-safe (root cause: Viriyah RFP analysis)
- **Hook ice-prebuild-guard.sh V01R02**: เดิม block ทุกคำสั่ง python ที่เอ่ยถึงไฟล์ office → การอ่าน read-only โดน block จน L0 ต้องอ้อม agent/เลี่ยง guard (เคสจริง Viriyah) · แก้: block เฉพาะการเขียน (การเรียก save บนไฟล์ office / รัน build script ตามชื่อ) — อ่าน/inspect ผ่านเสมอ + ข้อความ deny ระบุห้ามเลี่ยง guard · pipe-test 10/10 + live proof · ข้อจำกัดที่รู้: meta-text ที่พูดถึง pattern ของ guard ใน heredoc อาจโดน block เอง (พังดัง ไม่พังเงียบ — ยอมรับ)
- **กัปตัน V03R05 / คิม V02R04 / สมนึก V02R04**: READ-SELF FIRST — รู้ path = อ่านเองทันที ห้ามส่ง Explore อ่านแทน (Explore เฉพาะกวาดกว้าง/หาไฟล์) · ฝั่ง L2 ย้ำ Pull model: อ่านเองจาก path ใน Pack ไม่ถามกลับ L0 (ถามเฉพาะ decision/ของที่ไม่มีในไฟล์)

## 2026.07.14 (2) — L2 STALL WATCHDOG + VALIDATION BUDGET (root cause: Viriyah — เจนนี่วน validate หลัง build เสร็จ)
- **เจนนี่ V02R04**: VALIDATION BUDGET ใน E4 — validator single-pass (PASS = return ทันที ห้ามวนเพื่อความชัวร์) · fail → delta re-check cap 2 · scale-to-size (งานเล็กไม่ต้อง render ทุกหน้า) · token discipline (คืน counts ไม่ dump raw) — เคสจริง: ไฟล์เสร็จ 08:01 แต่ agent วนต่อจน transcript 1.48MB
- **กัปตัน V03R06 / คิม V02R05 / สมนึก V02R05**: L2 STALL WATCHDOG — artifact SAVE แล้วแต่ envelope ไม่กลับ ~3 นาที → L1 verify ไฟล์เอง (read-only) → ครบ spec = หยุด agent + จด [watch-out] · ค้างซ้ำ 2 งานติด → แจ้ง user · แยกชัดจาก FAILURE PROTOCOL (นั่นคือ dispatch ไม่ติด — นี่คือติดแต่ไม่จบ)
- **(ขยายครบทุก L2 ตามคำสั่ง user):** อริส V02R03 = QA BUDGET (1 pass ครบมิติ/รอบ · render สดครั้งเดียว/รอบ · counts ไม่ dump raw) · เทพ V02R03 = RETRIEVAL BUDGET (≤2 pass/claim · ไม่เจอ = ASSUMPTION+gap หยุดหา · ไม่ re-verify ซ้ำ) · ก้อง V02R03 = DRAFT BUDGET (self-revise ≤1 รอบ → return) · กัปตัน watchdog ขยายจาก ④/⑤ → ทุก L2 (②③④⑤)

## 2026.07.14 (3) — SPEED & ECONOMY WAVE: MODE GATE + PANEL + PIPELINE-LITE (root cause: audit 1 สัปดาห์ — over-dispatch + Run Line ไม่เคยถูกเขียน)
- **กัปตัน V03R07**: ⭐ MODE GATE (S2) = 3 โหมด **SOLO** (ตอบในแชทเท่านั้น) / **PANEL** (งานคิด-วิเคราะห์-สรุป-เทียบ-.md ภายใน) / **PIPELINE** (office file เส้นทางลูกค้าทุกตัวแม้ draft → LITE|FULL) + burden-of-proof (ไม่แน่ใจ=เข้มกว่า) + **3 รั้วกัน L0 take-over** (ประกาศโหมดก่อนทำ · PROVENANCE LOCK · L0 ห้ามสร้าง office file) · PANEL DISCIPLINE (§5): ONE-WAVE ห้าม round 2 + L0-WRITES-FIRST (กัน anchoring) + lens brief แคบ ≤3 · **PIPELINE-LITE** (§5): งานลูกค้าเล็ก ตัดรอบ ไม่ตัดบทบาท (④⑤ ครบ · ⑤ FAST 1 รอบ · fix 1 รอบ · RATCHET FULL ก่อนส่งจริงเสมอ) · BRIEF ECONOMY (S3 ชี้ section) · **Run Line บังคับ 100% ทุกงานรวม SOLO/PANEL + field `work_mode`** (ไฟล์ไม่มี=สร้างใหม่)
- **คิม V02R06 / สมนึก V02R06**: MODE GATE + PANEL discipline + LITE + Run Line work_mode (ฉบับตัวเอง · lens ของคิม=③⑤(②) · ของสมนึก=③⑤ + Codex เมื่อ user ระบุ)
- **เจนนี่ V02R05**: LITE role (รับ spec รวบขั้นเดียว · build+Validator เหมือนเดิม · fix 1 รอบ · spec ต่ำกว่า handoff-ready ยัง needs_input) — บทบาทไม่เคยถูกข้าม
- **อริส V02R04**: LITE tier mapping (work_mode:lite → FAST D2+D3+D7 1 รอบ · **RATCHET ไม่แตะ: is_final → FULL 9 มิติเสมอ**)
- **hook V01R03**: + marker `ICE_SMARTFIX=1` (Smart Fix ≤5 slides ที่ user อนุมัติใน rules §1.6) · pipe-test 13/13 + live 2/2 (SMARTFIX ผ่าน · build ไม่มี marker ยัง block)
- **refs**: doc-qa-log V01R02 (+`mode` ใน Process Compliance = หลักฐาน PROVENANCE LOCK) · rules/deliverable.md §1.6 (+ICE_SMARTFIX) · folder CLAUDE.md ×4 V01R03 (ตาราง 3 โหมด + Run Line บังคับ)
- **หลักการที่ล็อก:** ความเร็วมาจาก **ตัดรอบใน pipeline** ไม่ใช่ข้าม pipeline · งานลูกค้า (= งานส่วนใหญ่ของ user) ห้าม L0 take-over เด็ดขาด

## 2026.07.17 — MANDATORY LENS ใน PANEL (root cause: Viriyah TOC — กัปตันเขียน demo story เดี่ยว → ภาษาละคร "องก์/ฉาก")
- **กัปตัน V03R08**: §5 PANEL DISCIPLINE กติกาข้อ 4 — content ธรรมชาติ sales (demo/POC/narrative/pitch/win-theme) → ② ก้องต้องเป็น 1 lens เสมอ (+Write-Clean B-Business) · content ธรรมชาติ solution/knowledge (product/fit-gap/architecture/fact) → ③ เทพต้องเป็น 1 lens เสมอ · มีทั้งสอง → ②+③ · **L1 ห้ามเขียน content เฉพาะทางเดี่ยว** (skill ไม่ได้หาย — คนถือ skill ไม่ได้ถูกเรียกมาทำงาน)
- **คิม V02R07**: K2 PANEL DISCIPLINE ข้อ ④ ฉบับย่อเดียวกัน · (สมนึกไม่แตะ — ตามคำสั่ง user)
- หมายเหตุเคสเจนนี่ Viriyah build ไม่จบ: วินิจฉัยแล้ว = 400 xhigh+thinking (ตาย 9 ครั้ง — แก้ด้วย alwaysThinkingEnabled:true) + guard block ก่อนใช้ marker (10 ครั้ง) + คำสั่งแก้แทรกกลาง build (2 ครั้ง) — ไม่ต้องแก้ไฟล์เจนนี่ · operational: เปิด session ใหม่ + รวบ fix เป็นชุดเดียวหลัง SAVE
