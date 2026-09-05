# Compass.Next — Anti-Loop Contract Reference (§15)

> **Loaded by:** iCE-Compass.Next + ทุก in-path agent (เป็น contract ร่วม)
> **Design ref:** iCE-B2B-Compass.Next_V01R02 §11

> **นิยามศัพท์และรหัสที่ไฟล์นี้ใช้** (มาตรฐานการเขียนไฟล์ระบบ: `~/.claude/agents/reference/fleet-writing-standard.md`)
>
> · **L0 / L1 / L2** ชั้นการทำงาน: L0 = main loop ของ session ที่คุยกับผู้ใช้โดยตรง · L1 = agent ระดับบนที่เป็นเจ้าของงาน (กัปตัน / คิม / สมนึก) · L2 = specialist ที่ L1 เรียกใช้

---

## Why fleet ใหม่ loop ยากเกิด
```
43 agents: 5 layers · 33+ nodes · call graph ลึก → loop เสี่ยงสูง
6 agents:  2 layers · 6 nodes (NO leaf) · depth ~2 → loop เสี่ยงต่ำมาก + 5 กลไก
```

## กลไก 1 — Tree-Enforcing Call Graph
```
1. CALL-CHAIN BREADCRUMB: Pack มี call_chain · agent append ตัวเองก่อนเรียก child
   → id ตัวเองอยู่ใน chain แล้ว? → REFUSE (return status→blocked, reason "cycle")
2. NO-BACK-CALL: child ห้ามเรียก ancestor ใน chain
3. SIBLING-THROUGH-PARENT: ②③④⑤ ต้องการ sibling → ผ่าน L1 (Compass/Kim) → serialise
   → ไม่มี peer cycle (②→③→② เป็นไปไม่ได้)
4. DEPTH CAP ≤ 3: L1→L2 = depth 2 ปกติ · cap=3 เผื่อ ③ retrieve sub-call · เกิน → refuse
→ tree ไม่มี cycle ตามนิยาม → infinite loop เป็นไปไม่ได้เชิงโครงสร้าง
```

## กลไก 2 — Two-Tier Briefing Pack (กัน context decay)
```
CORE PACK (immutable verbatim): customer/product/primary_product/primary_industry/phase/
  language_directive/wording_discipline/brand_locks/core_pack_locked/call_chain/call_depth
  → child ห้ามแก้/ลบ (additive-only)
SECTION PACK (prunable+checksum): key_facts/build_safe_rules/section_spec/comparison_scope/requirement_source
  → parent prune ได้ แต่บันทึก facts_forwarded
REFERENCE PATHS: escape hatch (อ่านเฉพาะถ้า embedded ไม่พอ)
```

## กลไก 3 — Unified Return Envelope (กัน guess-instead-of-ask)
```
status (native→loop state) · work · questions · self_assessment{confidence,gaps} · sub_results · needs_followup
FALLBACK: no recognizable status ⇒ ready
CONFIDENCE GATE: ready BUT confidence:low → Compass ไม่ accept (re-command/ask)
NEVER-GUESS: brand/number/date/regulatory ไม่มีใน Pack → needs_input (H1-H4)
```

## กลไก 4 — Loop Guards
```
max_clarify_rounds=3 · max_review_rounds=2 · max_qa_rebuilds=2 ·
inline_build_tripwire (Compass เขียน build > couple steps → STOP dispatch④) ·
call_depth cap=3 · cycle guard · build-vs-edit guard
```

## กลไก 5 — Hard Delegation Rule
```
COMPASS=COMMANDER: NEW deliverable/>5 slides → MUST dispatch④ (ห้าม build inline)
INLINE only: ≤5 slides edit บน valid base ผ่าน python-pptx API
EXIT RAMP: Compass เริ่ม build + bug > couple steps → STOP, hand④
```

## Multi-Agent Discuss (star = tree, ไม่ loop)
```
R1 parallel-only · R2 independent (call_chain แยก) · R3 Compass-only synthesis · R4 max_discuss_rounds=2
3-Lens: Product→③ · Commercial→② · Risk→⑤ → Compass สังเคราะห์คนเดียว
```

## 2 L1 (Compass + Kim) — ยังเป็น tree
```
2 roots peer — ไม่ recursion (Kim ขอ Compass = provide ครั้งเดียว)
Kim→Compass→Kim → cycle guard บล็อก (ปกติไม่เกิด: Compass ไม่ขอ Kim)
```

## 3 Structural Failures ที่แก้
```
A. Context decay → กลไก 2 (Core Pack immutable + checksum)
B. Guess-instead-of-ask → กลไก 3 (confidence gate + never-guess)
C. Agents looping A→B→A → กลไก 1 (tree-enforcing) + กลไก 4 (depth/cycle guard)
```

---

*reference/anti-loop.md | Compass.Next §15 | honored by all in-path agents*

---

# ส่วนที่ 2 — Loop Engineering Layer L1-L8 (รวมเข้ามาจากไฟล์ loop-engineering.md เมื่อ 2026.09.05 เพื่อให้กติกากันวนทั้งหมดอยู่ไฟล์เดียว)

> คำเตือนเรื่องรหัส: L1 ถึง L8 ในส่วนที่ 2 นี้คือชื่อกลไกกันวน 8 ตัว ไม่ใช่ชั้นการทำงาน L0/L1/L2 ที่ใช้ในส่วนที่ 1

> **Version:** V01R01 | **Date:** 2026.07.10 | **ใช้กับ:** iCE-Compass-Next V03R01+ (§3 MAIN LOOP อ้างไฟล์นี้)
> **ที่มา:** สกัดจาก repo `cobusgreyling/loop-engineering` (แนวคิด Loop Engineering — "อย่า prompt agent ทีละครั้ง จง design ระบบที่ prompt agent แทนคุณ") — คัดเฉพาะหลักการที่เข้ากับงาน Business Consult / Advisor / Enterprise Application Sales / PhD-depth advisory · **ไม่เอาส่วน coding-specific** (ดูตาราง Not-Adopted ท้ายไฟล์)

> **นิยามศัพท์และรหัสที่ไฟล์นี้ใช้** (มาตรฐานการเขียนไฟล์ระบบ: `~/.claude/agents/reference/fleet-writing-standard.md`)
>
> · 🔴 **L1 ถึง L8 ในไฟล์นี้คือชื่อกลไกกันวน ไม่ใช่ชั้นของ agent** — เช่น L1 = TRIAGE, L7 = KILL SWITCH (ดูหัวข้อทั้งแปดด้านล่าง) · ส่วนคำว่า "ชั้น agent" ที่ไฟล์อื่นเขียนว่า L0/L1/L2 ไม่ใช้ในไฟล์นี้ ยกเว้นจุดที่เขียนคำว่า "agent" กำกับไว้ตรง ๆ
> · **② ก้อง · ③ เทพ · ④ เจนนี่ · ⑤ อริส** = specialist ที่ไฟล์นี้อ้าง: ② `sales-process-agent` เนื้อหางานขาย · ③ `solution-knowledge-agent` ความรู้ product · ④ `deliverable-gen-agent` ผู้สร้างไฟล์ (ทำงานเฉพาะเมื่อผู้ใช้เรียกชื่อตรง) · ⑤ `qa-master-agent` ผู้ตรวจคุณภาพ
> · **S0 · S4 · S6 · §9 (ที่เขียนว่า "บ้านกฎ")** = หมายเลขขั้นตอนใน MAIN LOOP ของไฟล์ persona ที่ใช้กลไกนั้น — กัปตันใช้รหัส S, คิมใช้ K, สมนึกใช้ T · ไฟล์นี้เป็นคลังกลไก ไม่ใช่ MAIN LOOP จึงชี้กลับไปที่ไฟล์เจ้าของขั้นตอน
> · **Fast / Full / Submit** = ระดับความกว้างของงาน (Orchestration Mode) ที่กำหนดโควตาในตารางลิมิต — คนละแกนกับระดับความลึกการตรวจของผู้ตรวจคุณภาพ
> · **`V##R##`** รหัสรุ่นเอกสาร เช่น `V02R05` — V คือรุ่นหลัก R คือการแก้ย่อย ต้องมีทั้งในชื่อไฟล์และในตัวเอกสาร

---

## หลักคิดแม่ของ repo (5 Primitives + Memory → แปลงเป็นภาษา Compass)

| Primitive (repo) | ความหมายเดิม (coding) | เทียบใน Compass |
|---|---|---|
| Automations/Scheduling | cron/loop รันตามรอบ | Scheduled Refresh (§9) + session-start triage |
| Worktrees | git isolation ต่อ attempt | ❌ ไม่ adopt — งานเอกสารใช้ V##R## versioning แทน |
| Skills | ความรู้ถาวรของ intent (จ่าย intent debt ครั้งเดียว) | skill ecosystem + Job 7 Learn เขียน lesson ลง reference |
| Plugins/Connectors (MCP) | ต่อ tool จริง | gdrive/gmail/notebooklm/web (A1-gated) |
| Sub-agents (Maker/Checker) | คนทำ ≠ คนตรวจ | Producer≠Checker (มีอยู่แล้ว — ยืนยันด้วย L4) |
| + Memory/State | STATE.md durable นอก conversation | _opportunity-context + _status-ledger + QA log |

---

## L1 — TRIAGE-FIRST + EARLY EXIT (บ้านกฎ: MAIN LOOP S0)

- **ที่มา:** `docs/operating-loops.md` — "Triage pass is cheap; spawn sub-agents only when state says actionable. Empty watchlist → exit in <5k tokens."
- **กติกา:** ก่อน dispatch ทุกครั้ง อ่าน state (ถูก) ก่อน spawn agent (แพง) · งานที่ state ตอบได้ (status/lookup/คำถามที่ ledger มีคำตอบ) → ตอบเลยพร้อมระบุ "ข้อมูล ณ [last_updated]" · actionable จริงค่อยเดิน S1
- **ตัวอย่างธุรกิจ:** User ถาม "proposal ลูกค้ารายนี้ถึงไหน" → อ่าน ledger เจอ artifacts_done + next_actions → ตอบทันที 0 spawn (เดิม: อาจ dispatch ② โดยไม่จำเป็น)

## L2 — STATE HYGIENE R-W-P + HUMAN INBOX (บ้านกฎ: S0 + S6 + §9)

- **ที่มา:** `templates/STATE.md.template` + failure mode "State Rot" (state อ้างของที่จบไปแล้ว → agent ทำงานกับผี)
- **กติกา:** **R**ead ก่อนเริ่มทุก task · **W**rite ผลลัพธ์+timestamp เมื่อจบ · **P**rune รายการที่จบ/ยกเลิกออกทุกครั้งที่เขียน — state ที่ไม่ prune = state ที่โกหก
- **Human Inbox:** ทุก escalation ต้องลงหมวด `Human Inbox` ใน _opportunity-context (format → §9) — แก้ปัญหา "escalation หายไปกับ context ยาว" · User ตัดสินแล้ว → prune + ย้ายผลลง decisions
- **ตัวอย่างธุรกิจ:** รอ User เลือก SLA option (ก) 99.7% (ข) custom → ลง INB-03 · สองสัปดาห์ต่อมาเปิด session ใหม่ Compass อ่าน inbox เจอเรื่องค้าง → ทวงได้เอง

## L3 — STAGNATION CIRCUIT BREAKER (บ้านกฎ: S4 + §6)

- **ที่มา:** `templates/SKILL.md.loop-guard` (circuit breaker + ledger: same error N× = trip) + failure mode "Infinite Fix Loop"
- **กติกา:** issue ID เดิมโผล่ 2 รอบติด (QA round / review round) โดยไม่คืบ → **trip ทันที ไม่รอครบ cap** → STOP → escalate พร้อมสรุปสะอาด: ติดอะไร ลองอะไรแล้ว (จาก QA log) เสนอทางเลือก (ก/ข/ค)
- **ต่างจาก cap อย่างไร:** cap = ปริมาณ (นับรอบ) · breaker = คุณภาพ (จับอาการซ้ำ) — deck แก้ 3 จุด แต่ ISS-07 โผล่ทั้ง round 1 และ 2 → breaker trip แม้ QA-REBUILD ยังไม่ครบ 2
- **หลักการสำคัญ:** "Never widen thresholds just to keep looping — **escalation is a feature, not a failure**" · ห้ามแก้ log เพื่อซ่อนอาการซ้ำ
- **ตัวอย่างธุรกิจ:** font overflow slide 39 แก้แล้วโผล่อีกใน re-QA → ไม่สั่งแก้รอบ 3 → escalate: "โครง slide นี้ content เกิน layout — เลือก (ก) ตัด content (ข) เปลี่ยน layout (ค) แตก 2 slides"

## L4 — EVIDENCE-BASED VERDICT (บ้านกฎ: S4 + §8 COMPONENT SCHEMA)

- **ที่มา:** `skills/loop-verifier/SKILL.md` — "Default stance: REJECT until proven otherwise. Do not trust implementer's claim that tests passed — run them." + failure mode "Verifier Theater" (ตรวจผ่านแต่ไม่ได้ดูจริง)
- **กติกา:** verdict ทุกตัว (verify_verdict ของ ③ / QA ของ ⑤ / review ใด ๆ) ต้องแนบ `evidence:` = สิ่งที่**เปิดดู/นับ/เทียบจริง** (เช่น "เปิด slide 12 นับ ODI = 10 ตรง key_facts") · ไม่มี evidence = ไม่นับเป็น verdict — Compass ตีกลับ · ผู้ตรวจ default REJECT จนหลักฐานพอ
- **ตัวอย่างธุรกิจ:** ③ ตอบ "NetSuite รองรับ multi-book ✓ PASS" เฉย ๆ → ตีกลับ · ต้องเป็น "PASS — evidence: SuiteAnswers doc id NNN ระบุ Multi-Book Accounting ใน version ที่เสนอ + เทียบ scope ลูกค้า 3 books < limit"

## L5 — SPAWN BUDGET (บ้านกฎ: S2 + §6)

- **ที่มา:** `skills/loop-budget/SKILL.md` (max sub-agent spawns/run · 80% → report-only · exceed → หยุดแจ้ง human)
- **กติกา:** งบเรียก sub-agent ต่อ task (รวม retry): **Fast=2 · Full=4 · Submit=6** · แตะเพดาน → หยุด รายงาน "ใช้ไปเท่าไรกับอะไร" → ถามก่อน spawn เพิ่ม · **ยกเว้น CB** (id15) ใช้ Granularity Ladder เป็น budget ของตัวเองอยู่แล้ว (ladder ออกแบบมา cap จำนวน preview/review ตาม N)
- **เหตุผลตัวเลข:** Full chain หนักสุดนอก CB = ②③⑤ + ⑤QA = 4 · Submit + ④ build + re-QA = 6 — พอดีงานจริง ไม่รัดจน routine สะดุด

## L6 — PHASED TRUST / REPORT-FIRST (บ้านกฎ: S2)

- **ที่มา:** upgrade path "L1 report-only → L2 assisted → L3 unattended · Never skip L1 for a new pattern" (`docs/operating-loops.md`, `docs/loop-design-checklist.md`)
- **กติกา:** activity type ที่**ไม่เคยทำใน opportunity นี้** (เช็คจาก ledger/Run Line) **และ** เข้า HIGH-STAKES signal → เสนอ PLAN-CARD ให้ User เห็นก่อน execute (report-first เฉพาะครั้งแรก) · User สั่ง "ทำเลย" = ข้าม · เคยทำผ่านแล้ว → execute ตรง
- **ตัวอย่างธุรกิจ:** ครั้งแรกที่ทำ concession matrix ให้ deal นี้ (id6 — ผูก commitment การเงิน) → โชว์แผน: จะให้ ② ร่าง 3 scenario, ③ refute ตัวเลข, ⑤ ตรวจ liability — User เห็นทิศก่อนเปลือง 4 spawns

## L7 — KILL SWITCH (บ้านกฎ: S0 + §6)

- **ที่มา:** `docs/safety.md` + `loop-budget.md` (kill switch `loop-pause-all` + resume เมื่อเคลียร์)
- **กติกา:** User สั่ง "หยุด/พอก่อน/stop" กลางงาน → (1) ไม่ dispatch เพิ่ม (2) งานที่เสร็จแล้วเก็บ (3) เขียน state ค้าง: ถึงไหน/อะไรค้าง/resume ยังไง (4) ยืนยันกับ User ว่าหยุดแล้ว + จุด resume — **หยุดสะอาด ไม่ใช่หยุดทิ้ง**
- **ตัวอย่างธุรกิจ:** กลาง CB Phase 2 (7/12 หน่วย accept แล้ว) User สั่งหยุดไปประชุม → เขียน: units 1-7 accepted, 8 อยู่ระหว่าง review, 9-12 ยังไม่เริ่ม → กลับมาต่อที่หน่วย 8 ไม่เริ่มใหม่

## L8 — RUN LINE (บ้านกฎ: S6 + §9)

- **ที่มา:** `loop-run-log.md` (append JSON 1 entry/run — "no run log = cannot debug why did it do that Tuesday")
- **กติกา:** จบทุก task ต่อ 1 บรรทัดลง `_activity.log`: `{ts, activity, mode, tier, spawns, rounds, breaker_trips, escalations, outcome}` · เขียน**หลัง**ส่งงาน User (Deferred Log — ไม่กั้น critical path)
- **ใช้ทำอะไร:** Job 7 Learn มีข้อมูลจริง — activity ไหนวนบ่อย (breaker_trips สูง) / แพง (spawns ชนเพดาน) / escalate บ่อย → ปรับ skill/threshold ด้วยหลักฐาน · L6 Phased Trust เช็คจากนี่ว่า activity เคยทำหรือยัง · ตัวเลข [ASSUMED] ใน design ทั้งหมด validate จากข้อมูลนี้หลังใช้จริง 3-5 งาน

---

## แนวคิดเสริมที่ฝังในเนื้อ Compass (ไม่เป็นข้อแยก)

| แนวคิด (repo: `docs/concepts.md`) | ความหมาย | ฝังที่ |
|---|---|---|
| **Intent Debt** | agent เริ่ม session เย็นทุกครั้ง — ความตั้งใจที่ไม่เขียนไว้ถูกเติมด้วยการเดา | Job 7 Learn เขียน lesson/convention ลง skill+reference ทันทีที่จบ deal (จ่ายครั้งเดียว อ่านทุก run) |
| **Comprehension Debt** | ช่องว่างระหว่างของที่ผลิต กับที่เราเข้าใจจริง | S6 Verify-by-Observation — Compass ต้องอ่านของที่ ④ ผลิตจริง ไม่ rubber-stamp |
| **Cognitive Surrender** | ปล่อย loop ทำแล้วเลิกมีความเห็น | Compass ต้องมี verdict + เหตุผลเสมอ (§5 Synthesis = Compass คนเดียว) — orchestrate เพื่อคิดให้คมขึ้น ไม่ใช่เลิกคิด |
| **Orchestration Tax** | ต้นทุนมนุษย์ในการ coordinate หลาย agent | Human Inbox + Run Line + PLAN-CARD = ลดภาระ User ตาม ไม่ใช่เพิ่ม |

## Fable 5 ↔ Loop Engineering (ทำไมเข้ากันเป็นเนื้อเดียว)

F2 Scout-then-Commit = ราก L1 · F3 Verify-by-Observation = ราก L4 · F6 Two-Strike Rethink = ราก L3 — Fable 5 Protocol คือ**วิธีคิดของ Commander** ส่วน L1-L8 คือ**กลไกเชิงระบบ**ที่ทำให้วิธีคิดนั้นถูกบังคับใช้แม้ context ยาว/งานหนัก

---

## ตาราง NOT-ADOPTED (coding-only — ตัดสินใจแล้ว ไม่ต้องคิดใหม่)

| ของใน repo | ทำไมไม่เอา |
|---|---|
| Git worktrees / loop-worktree CLI | งานเอกสารธุรกิจไม่มี merge conflict แบบ code — V##R## versioning + backup convention ทำหน้าที่นี้อยู่แล้ว |
| CI Sweeper / PR Babysitter / Dependency Sweeper / Post-Merge / Changelog Drafter patterns | ผูกกับ CI/PR/package ecosystem — ไม่มี analog ที่คุ้มในงาน sales/advisory |
| Auto-merge policy + path allowlist | ไม่มี auto-merge ในงานเอกสาร — RATCHET + Hard QA Gate คุม external delivery อยู่แล้ว |
| npm CLIs (loop-audit/loop-init/loop-cost/loop-context/loop-sync/loop-mcp-server) | tooling ของ dev workflow — กลไกที่ต้องการ (breaker/budget/log) แปลงเป็นกติกาใน agent แทน |
| GitHub Actions cron | Compass เป็น interactive agent — scheduling ที่มีคือ Scheduled Refresh ผ่าน User/Kim |
| MCP GitHub scopes / bot identity | ไม่ relevant กับ gdrive/gmail scope ปัจจุบัน |

---

*Reference: loop-engineering.md V01R01 | 2026.07.10 | คู่กับ iCE-Compass-Next V03R01 §3/§6/§9*

