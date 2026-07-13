# iCE-Compass-Next — Changelog & Lessons Archive

> **Version:** V01R01 | **Date:** 2026.07.10 | ไฟล์นี้เก็บ **ประวัติ version + บทเรียนเต็ม** ที่ย้ายออกจาก body ของ agent (ตั้งแต่ V03R01) — เพื่อให้ main prompt เหลือเฉพาะกฎที่ใช้ตอนนี้ · อ่านไฟล์นี้เมื่อต้องการเหตุผลเบื้องหลังกฎ หรือทำ version ถัดไป

---

## Version History

### V03R03 (2026.07.13) — DOC-PIPELINE + 2-Tier Invocation (8 จุด)
**Root cause:** Viriyah RFP session `0d9285cb` (12-13 ก.ค.) — L0 สวมบทกัปตันโดยไม่ได้อ่านไฟล์ + ultracode ดันไปใช้ Workflow generic (5 workflows ไม่มี agentType) + build Excel inline 400+ จุด → **เจนนี่ถูกเรียก 0 ครั้ง** · pattern ซ้ำที่ EuroFood/Akara · content เชิง solution ไม่มีเจ้าของ (③ ถูกห้าม author) · "Failed to extract RFP ref" ไม่หยุดสายพาน
**แก้ 8 จุด:** (0) description encode 2-Tier — spawn เฉพาะ Tier 1 (1) header ประกาศ OPERATING MANUAL ของ L0 (2) S2 +TASK DECOMPOSITION mapping ตายตัว + PLAN-CARD-FIRST (3) S3 +Q-CONTENT-A/B ยิงก่อน Q1 (4) PRE-BUILD STOP ครอบ Workflow script/heredoc (5) §4 ③=CO-AUTHOR · ④ needs_input เมื่อ content ไม่ครบ · +แถว content design (6) §5 +DOC-PIPELINE id16 (CONTENT-READY GATE + SAVE + DELIVERY REPORT) (7) §10 +WORKFLOW GUARD (agentType ทุก stage) (8) §8 +memory_paths + ISOLATION by project
**คู่กัน:** CLAUDE.md V09R04 (ชั้น A) + folder CLAUDE.md ×4 (ชั้น B) + fleet V02R02 (คิม/สมนึก/เจนนี่/เทพ/ก้อง/bridges — ดู fleet-changelog "DOC-PIPELINE Wave")

### V03R01 — 2026.07.10 (MAJOR REWRITE — current)
- **โครงใหม่ทั้งไฟล์:** §1 Identity → §2 Principles (+Fable 5 Protocol F1-F7) → **§3 MAIN LOOP S0→S6** (เส้นทางเดียวทุก task) → §4 Routing & Ownership (รวม Dispatch Table + OWNERSHIP LOCK ที่เคยแยก 2 ที่) → §5 Master Matrix (+Panel+CB) → **§6 Control Limits** (ทุก cap/breaker/budget ตารางเดียว — แทน GLOSSARY 4-CAP) → §7 Stop & Escalate (dedup) → §8 Schemas → §9 State & IO → §10 Integrations → §11 Reference Index
- **หลักที่ใช้ rewrite:** ONE-HOME (กฎนิยามที่เดียว ที่อื่นอ้างชื่อ — แก้อาการ model อ่านเจอกฎเดิม 3-4 เวอร์ชันแล้ววนคิด) · จัดชั้น context (always-on ต้น / lookup กลาง / rare → reference)
- **ของใหม่:** ⭐ Loop Engineering Layer **L1-L8** (business-adapted จาก `cobusgreyling/loop-engineering` — Triage-First / State-Hygiene+Human-Inbox / Circuit-Breaker / Evidence-Verdict / Spawn-Budget / Phased-Trust / Kill-Switch / Run-Line — เต็ม → `reference/loop-engineering.md`) + ⭐ **Fable 5 Thinking Protocol F1-F7** (Understand→Plan→Act→Verify→Report · Scout-then-Commit · Verify-by-Observation · Calibration Tags · Fail-Loud · Two-Strike Rethink · Parallel-when-Independent)
- **คงครบจาก V02R06:** 7 Jobs · Self-Audit 3Q · Pre-Build Stop · Smart Fix · Hard QA Gate + Speed Tier + RATCHET · 8 Gates · Two-Tier Pack (term_policy/cb_unit_spec) · Orchestration Mode + TRIPWIRE · Master Matrix 14 + OFF-RAMP · 3-Lens Panel R1-R4 · CB 5-phase + Ladder + ALWAYS-DRILL + Reviewer Router · Anti-Loop Contract · 3-Zone State + ledger + γ3 + QA log closed-loop · Scheduled Refresh · Kim protocol · Entry Routing + SELF-INTRODUCE · Output/Component/Envelope schemas (+`evidence` field ใหม่) · Deferred/Forensic Log · Layer-0 awareness · Second-Opinion Codex/OpenRouter
- ขนาด: 675 → ~460 บรรทัด (−32%) · Conforms to: CLAUDE.md V09R03 (เดิมอ้าง V07R02)

### V02R06 — 2026.06.25
+ OpenRouter second-opinion option (openrouter-bridge — เลือก model ได้ทุกตัว) ข้าง Codex + CB Per-Unit Reviewer Router (Codex XOR OpenRouter by content/persona — เด่น persona review CFO/CIO) · คู่กับ openrouter-agent V01R01

### V02R05 — 2026.06
+ **Composed Build (CB)** orchestration (Master Matrix #15, Pattern #4 Generate-And-Filter w/ capped per-unit filter loop) สำหรับ deck >10 slides / proposal ≥2 บท — Track A unit=หน้า · Track B unit=บท · 5-phase: Frame → Overall-outline+③ (ไม่ batch) → per-unit draft+review (③ XOR Codex) → per-unit preview-inspect (④ build → กัปตันคุมกรอบ) → build-once → inspect-same-artifact present-on-PASS · PUL CAP Fast1/Full2/Submit3 · Granularity Ladder (≤12 per-unit / 13-30 section-batch / >30 sample-frame → 77 slides ≈ 8 preview) · always-drill ≤8 · small-deck escape · คู่กับ ④ V01R15

### V02R04 — 2026.06
+ P7 Card B6 Term-Localization pointer + section_pack `term_policy` (register Professional-B2B · TL-A/B/C + MG1 misname guard · seeds verified keep_english จาก source · verify_feature_names · audit_all_sources) + wording-ownership note (เคส VFIN — B2B wording ไม่ route ไป academic pass)

### V02R03 — 2026.06
+ AI imagery routing — dispatch ④ (gemini-rlabs/higgsfield), Compass ไม่ build inline (routing-only ใน Dispatch Table + engine guideline · ไม่เพิ่ม mcp_tools เพราะ producer≠orchestrator)

### V02R02 — 2026.06
+ L1 Write-Clean Card pointer (prevention layer — เขียนสะอาดตั้งแต่แรก · P7 Human Voice → core A1-A5 + register B-Business · source of truth = skill thesis-ai-det-col)

### V02R01 — 2026.06
+ Orchestration Mode (Fast/Full/Submit) + Master Matrix 14 activity (Pattern ID traceable) + Mid-stream Verify + clarify-gate + TOR-veto + verify-verdict schema + Chain-Round Loop Cap + Glossary 3-CAP

### V01 (design lineage)
- Design ref: iCE-B2B-Compass.Next_V01R02_2026.06.01.MD §5 · V01R04 orchestration design (return envelope + Two-Tier Pack + §15 anti-loop → implement 2026.06.01 ครอบ 19 agents)
- Replaces: iCE-b2b-Compass + sales-admin + gdrive + gmail + portfolio-intelligence (5→1 · initiative 43→6 consolidation)

---

## Lessons Archive (บทเรียนจริงที่รองรับกฎ — ย้ายจาก body V02R06)

### บทเรียน TQR (Reinsurance Broker — ERP proposal deck)
**อาการ:** Compass เวอร์ชันก่อน build deck 84 slides เองแบบ inline → เจอ XML corruption (endParaRPr/empty-run) → วน debug ด้วย Bash **155 รอบ** โดยไม่ hand off · custom agents (④②③) ไม่ถูกเรียกเลยทั้งโปรเจกต์
**Root cause 3 จุด:** (1) ไม่มีกลไก**บังคับ** delegate — มีแค่คำแนะนำ (2) ไม่มี exit ramp จาก inline debug spiral (3) build capability อยู่ผิดที่ (ใน playbook ของโปรเจกต์ ไม่ใช่ใน specialist agent)
**กฎที่เกิดจากบทเรียนนี้:** Hard Delegation + PRE-BUILD STOP (ดักก่อนพิมพ์ build code — ไม่ใช่ดักหลังเจอ bug) + Exit Ramp (bug เกิน couple steps → hand off) + Commander-not-Builder เป็นปรัชญาหลัก · V03R01 เสริม L3 Circuit Breaker (จับอาการซ้ำตั้งแต่รอบ 2 — ถ้ามีตอนนั้น 155 รอบจะจบที่ 2)

### บทเรียน Ascend (EPM opportunity)
**อาการชุดที่ 1 (God-Object):** Compass build .pptx/.xlsx เอง + เขียน content เอง + ไม่ verify fact · 3 custom agents ไม่ถูกเรียก → เกิด **DISPATCH SELF-AUDIT 3Q** + Routing Table (ตัด judgment ออกจากการเลือก owner)
**อาการชุดที่ 2 (RW-4 — ข้าม QA):** present deck โดยไม่ผ่าน QA — User ต้องทัก · หลังแก้ก็ไม่ re-QA → เกิด **Hard QA Gate + re-QA หลังแก้บังคับ**
**อาการชุดที่ 3 (Round 3 forensics — QA ช้า):** QA = fixed cost ~7.2 นาที/รอบ · บังคับ FULL ทุกครั้ง = ช้าตอนอยากได้ draft → เกิด **SPEED TIER (DRAFT/FAST/FULL) + RATCHET** (เลือกความลึกตาม urgency แต่ final ลูกค้า = FULL เสมอ)
**อาการชุดที่ 4 (RW-9 — ตัวเลขขัดกัน):** ตัวเลข ODI ขัดกันระหว่าง slide กับ commercial table → เกิด **γ3 CANONICAL-COUNT** (key_facts = source เดียว ทุก derived slide reconcile ก่อน)
**อาการชุดที่ 5 (briefing pack ภาระ):** Compass ประกอบ pack ใหญ่ทุก dispatch = ภาระสูงจนเลือกทำเองแทน → เกิด **Pull model** (context กลาง sub-agent อ่านเอง — dispatch ส่ง path + section spec)
**อาการชุดที่ 6 (log กั้นงาน):** เขียน log ก่อนส่งงาน = User รอโดยไม่จำเป็น → เกิด **Deferred Log** (ส่งงานก่อน log ตาม · forensic = on-demand)

### บทเรียน VFIN (wording ownership)
B2B deliverable ถูกส่งไป academic humanize pass ผิด register → เกิด **wording-ownership note**: wording/anti-AI/term-localization บน B2B artifact = Compass Language-Authority + ④ write-clean (Card B6) + ⑤ D5/D5.TL — register ตาม artifact ไม่ใช่ keyword

### บทเรียน 2026.07.10 (ที่มาของ V03R01)
ไฟล์ V02R06 โต 675 บรรทัดจากการเติมสะสม 6 รอบ R — กฎเดิมถูกเขียนซ้ำหลายที่ (Pre-Build ×3 · QA ×3) + ต้องมี GLOSSARY "อย่าสับสน" 3 จุด = โครงสร้างเริ่มสร้างภาระการอ่านเอง → rewrite เป็น MAIN LOOP + ONE-HOME · **หลักสำหรับ R ถัดไป: เพิ่มกฎใหม่ = หาบ้านใน S0-S6/§4-10 ให้ก่อน ห้ามแปะท้ายไฟล์**

---

*Reference: compass-changelog.md V01R01 | 2026.07.10 | คู่กับ iCE-Compass-Next V03R01*
