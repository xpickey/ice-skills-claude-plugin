# Fleet Changelog — ประวัติเวอร์ชันของ agent ทั้ง fleet (ยกเว้นกัปตันที่มี compass-changelog.md)

> **Version: V01R01 | 2026.07.10** — history ที่ย้ายออกจาก body ของแต่ละ agent ตอน Fleet Rewrite V2 (2026.07.10) เพื่อให้ main prompt เหลือเฉพาะกฎที่ใช้ตอนนี้ · อ่านเมื่อต้องการเหตุผลเบื้องหลัง/ทำ version ถัดไป

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
- **V02R01 (2026.07.10)** — +Modes A-E · +ref 05 Review Contract + verdict.schema.json · +helper V02 (--session/--list-sessions/--schema + feature-detection + overwrite guard) · +Authorization Matrix + codex_scope (ONE-HOME) · +Degradation Ladder · ref 01 +Probe 2026.07.10 (--output-schema/resume-positional) · ref 02 +REVIEW shape + Shard
- V01R02 (2026.06.22) — +4 presets + fleet binding · V01R01 (2026.06.22) — initial

*Fleet Changelog V01R01 | 2026.07.10 | คู่กับ: compass-changelog.md (กัปตัน) · Fleet-Design_V01R01 (design doc)*

## QA Record — Codex Dogfood Review (2026.07.10 · Mode B + verdict.schema.json)
- **helper ask-codex.sh:** R1 พบ 0C/3H/4M (H1 dot-session ทะลุทับ default thread · H2 dash-prompt กินเป็น flag · H3 UUID fallback เสี่ยงผิด thread · M1-M4) → แก้ครบ + ทดสอบจริง 5 ข้อ → **R2: 0/0/0 · fixed_verified ทั้ง 7 — CONVERGE**
- **deliverable-gen (เจนนี่) knowledge-loss audit:** R1 พบ 0C/1H (xlsx formula-integrity หลุดจาก E4 บังคับ) + context_repair (E4 แยกตาม format) → แก้ทั้งคู่ → **R2: 0/0/0 · H1 fixed_verified — CONVERGE**
- บทเรียนใหม่: (1) OpenAI --output-schema = strict mode (ทุก object ต้อง required ครบทุก property — verdict.schema.json V01R02 แก้แล้ว) (2) error "models cache: unknown variant max" ของ codex = noise ไม่ fatal (3) network DNS หลุดชั่วคราว → retry 1 ครั้งพอ
