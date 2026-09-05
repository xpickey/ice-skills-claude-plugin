# ประวัติการเปลี่ยนแปลงของ skill `ice-b2b-enterprise-sale`

> **ไฟล์นี้ใช้ทำอะไร:** เก็บบันทึกการเปลี่ยนแปลงรายรุ่นของ `SKILL.md` ทั้งหมด เพื่อให้ตัว `SKILL.md` เหลือเฉพาะกติกาที่ใช้ทำงาน ผู้ที่ต้องการรู้ว่ารุ่นก่อนเปลี่ยนอะไรไปบ้างและด้วยเหตุผลใด ให้เปิดไฟล์นี้ — งานปกติไม่ต้องอ่าน
> **รหัสรุ่น `V##R##`:** V คือรุ่นหลัก R คือรุ่นย่อย เช่น `V02R07` คือรุ่นหลักที่ 2 รุ่นย่อยที่ 7

**V02R07 — 2026.09.05 — FLEET READABILITY V3 Pass 2.5 (ทำให้อ่านง่ายขึ้น ไม่เพิ่มกฎ).**
ยุบ Section 3 (Decision Logic) · Section 4 (Default Chains) · Section 5 (Mix & Match) ที่เขียนเป็น
ร้อยแก้วยาว ให้เหลือหัวข้อเดียวที่ชี้ไปตารางเส้นทาง `~/.claude/hooks/skill-routing.yaml` ซึ่งเป็น
ไฟล์ที่ระบบอ่านจริงและเป็นผู้บอก skill ให้เองอยู่แล้ว เหตุผล: บัญชี Pass 1 พบว่าประโยคสั่งให้โหลด
skill กระจายอยู่ 153 ประโยคใน 30 ไฟล์ และร้อยแก้วในไฟล์นี้เก่ากว่าตารางที่ระบบใช้จริง (ลำดับ Hot
Path ไม่เคยเอ่ยถึง `b2b-slide-designer` และ `ice-writing-register` ที่ตารางกำหนดเป็น skill บังคับ)
กติกาที่ตารางเก็บแทนไม่ได้ยังคงอยู่ครบในหัวข้อ "ข้อจำกัดการทำงานในหนึ่งงาน" (เพดาน 5 sub-skill ·
ลำดับชั้น Tier · ตารางแก้ความทับซ้อน · ดีลภาครัฐหยิบ domain skill เสมอ) และหัวข้อบริบทอุตสาหกรรม
กับภาพจาก AI ซึ่งตารางไม่มีแนวคิดรองรับ · ย้าย Section 12 Change Log ทั้งหมดมาไฟล์นี้ · ยุบนิยาม
รหัสกฎเหล็กจาก Section 11 เข้าตารางนิยาม Section 0A ให้รหัสมีบ้านเดียว · ยุบข้อความเรื่องแหล่งกติกา
ฟอนต์ที่เคยซ้ำ 3 แห่ง ให้เหลือบ้านเดียวที่ด่านก่อนบันทึกไฟล์ข้อ 6 · เขียน Hard Rules ของถ้อยคำเชิงบวก
ใหม่เป็นคู่ตัวอย่าง ❌ กับ ✅ ตาม `fleet-writing-standard` ข้อ 2 · แทนชื่อจริงของเจ้าของงานด้วยคำว่า
"ผู้ใช้ระบบ" · ย่อ `description` จาก 942 ตัวอักษรเหลือไม่เกิน 300 ตัวอักษร ขึ้นต้นด้วยกรณีใช้งาน ·
ไม่มีการเพิ่มกฎใหม่ และไม่มีการเปลี่ยนเส้นทางการทำงาน · บัญชีตรวจสาระครบรายข้ออยู่ที่ `SKILL.inventory.md`

**คำเตือนที่ยกมาจาก Section 11 ของรุ่น V02R06:** รหัสกฎเหล็กชุดเดิมของ Protocol รุ่น V6.0
(H7 · H8 · H9 · H10 · H14 · H15 · H16) เลิกใช้แล้วและไม่ตรงกับกฎใด ๆ ที่มีอยู่จริง — ให้อ้างรหัสตาม
`~/.claude/CLAUDE.md` ฉบับปัจจุบันเท่านั้น ซึ่งนิยามไว้ในตารางนิยาม Section 0A ของ `SKILL.md`

**V02R06 — 2026.08.08 — FLEET READABILITY V3 Phase 2.**
Added Section 0A (definition table: router/sub-skill/chain, Fast Path vs Default Chain,
Tier A-D, deliverable, TOR/e-GP/GFMIS, Compliance Matrix, Rapid Workflow, Positive Wording,
Loss-Frame, `[ASSUMED]`, `V##R##`, and the current CLAUDE.md hard-rule codes) so a reader who
opens only this file can follow it. Rewrote Section 11 against the **current** machine
CLAUDE.md V09R08 rule numbering — the old Protocol V6.0 codes (H7/H8/H9/H10/H14/H15/H16) no
longer matched any existing rule and pointed readers at the wrong obligations. Resolved the
contradiction where Section 9 told the reader to open `typography-bilingual-qa.md` for fonts
while Section 7 had already retired that table: the reference is now labelled process-checklist
only, with `ice-doc-builder` §3.0 named as the sole font authority. No routing changes — Hot,
Standard, and Fast Path are identical.

**V02R05 — 2026.06.14 — Sub-release. Negotiation playbook authored.**
The dedicated `b2b-solution-selling/references/10-negotiation-playbook.md` (V01R01) was
authored — extracted from the iCE Negotiation-for-Sales corpus (Win-Win + Position/Interest,
5-step process, Logos/Pathos, Give-Take/Logrolling/Packaging, Anchoring/Deadlock,
BATNA/walk-away, countering 4 dirty tactics, 4-step Price Defense, Closing & Binding
Commitment, iCE Competitor Battle Card + Solution Bundle, Scope-Creep workflow). This closes
the long-standing reference gap first flagged in V02R02 (file 10 was scoped but not yet
written). The V02R02 changelog note is updated in place from "does not exist" to "now exists."
No routing or SKILL.md structure changes — the orchestrator already routed negotiation work to
Component 10; the deep content now lives in a real file instead of distributed across 00-09.

**V02R04 — 2026.06.14 — Sub-release. AI Imagery awareness added.**
เพิ่ม Step 5b (AI imagery, optional) ใน Hot Path chain (Section 4.1) — ให้ skill นี้รู้จัก
`nanobanana-connection` (Gemini image, MCP เสมอ, hero/infographic ภายในเร็ว/quota) และ
`higgsfield-connection` (full suite image+video+marketing+Soul-ID, credit-based, 4K/ad/brand/
character คงหน้า) เผื่อกรณีเรียก skill นี้ตรง (ไม่ผ่าน deliverable-gen agent). ฝัง Execution
Path Rule: Claude Code (Bash) → higgsfield CLI `hf generate create` · Claude Desktop/Web/Cowork
→ MCP tool · nanobanana = MCP เสมอ. preflight cost ก่อนงาน higgsfield แพง. No routing changes —
Hot/Standard/Fast Path เหมือนเดิม; เพิ่มเฉพาะ optional step ใน Hot Path เมื่อ ref 07 Method 3
(AI imagery) ของ b2b-presentation-creator ถูกเรียก. ไม่แตะ reference files.

**V02R03 — 2026.05.27 — Sub-release. Positive Wording Discipline added.**
Added Section 6A "Positive Wording Discipline" as a Ground Rule for all Proposal,
Presentation Material และ Pre-sales/Sales deliverables. Discipline is operationalised
in three levels — Word Substitution (Level 1, applied to every Stage and every
Touchpoint), Frame Change (Level 2, applied heavily in Solution Design, Proposal,
Presentation, Negotiation, Closing), and Document Architecture (Level 3, applied to
every Deliverable the customer reads without the seller present, with a 70/25/5
Positive/Neutral/Negative ratio). Activation map calibrated per Stage: Discovery
stays neutral to prevent Spontaneous Trait Transference; Pain Validation allows
Loss-Frame only inside the Cost of Inaction Section; Solution Design through
Renewal/Expansion enforce full Positive Wording; Escalation/Recovery is the only
Stage where negative facts must be acknowledged directly and then reframed as a
Path to Resolution. Pre-Save Quality Gate in Section 7 gains check #5 (Positive
Wording scan) inserted before the Typography & Bilingual QA. No routing changes —
Hot Path, Standard Path, and Fast Path remain identical. No reference-file changes
required; the discipline lives inside SKILL.md so it activates the moment the router
is invoked, regardless of which sub-skill chain runs next.

**V02R02 — 2026.05.22 — Sub-release. Negotiation routing enabled.**
Lite-update to enable Component-10 negotiation routing from the orchestrator without
disturbing the Section-3 routing logic or Section-4 default chains. Three references
updated together so routing stays consistent: `decision-matrix.md` Section 2.1 gains
D-21 (Negotiation Brief / Price Defense Sheet) and D-22 (BAFO Strategy Sheet);
`sub-skill-index.md` Section 1.1.2 widens the b2b-solution-selling outputs paragraph
to name negotiation-playbook, BATNA/ZOPA, and the 4-step objection protocol, and
Section 4 Stage Lens points the Negotiate row at Component 10 + D-21; and
`orchestration-playbook.md` adds a cross-reference from QRC-04 to the deep playbook
plus a new bilingual QRC-11 (Negotiation In-Room Field Card) calibrated for use in
the lift on the way up to a final-pricing meeting. No SKILL.md routing changes — the
Hot Path, Standard Path, and Fast Path remain identical. Negotiation content currently
lives distributed across `b2b-solution-selling/references/` (00-blueprint, 03-meddpicc,
04-challenger, 07-handover, 09-seller-dna — BATNA/ZOPA/objection handling); a dedicated
`10-negotiation-playbook.md` was scoped here but not yet authored. Until it exists, route
negotiation work to the 00-09 references above. *(V02R05 note: superseded —
`b2b-solution-selling/references/10-negotiation-playbook.md` now exists, V01R01,
extracted from the iCE Negotiation-for-Sales corpus; route deep negotiation work there.)*

**V02R01 — 2026.05.14 — Major version threshold (work-in-progress).**
Reframe acknowledged: source artifacts represent current-state working patterns,
not target-state best practice. Foundation set for Elevation Spec layer (per-WE
"lift this above current" guidance) to be added in the next release. Replaced
`[ASSUMED]` flags in WE-05 (NetSuite FMCG), WE-07 (FinTech Bank), and WE-08
(Government bidding) with real source patterns extracted from eleven anchor
artifacts: Warrix C-Suite DEMO v2.0 (Sports apparel CRM+ERP, 85 slides); GFPT
NetSuite Proposal (Poultry integrated business, 146 slides with named industry
references); HFC Propose Solution rev0.2 (Health Foods multi-channel, 90 slides);
IIG HFC Propose Solution (CRM/PRM Engagement Platform, Design-Thinking-anchored
3-Release Crawl-Walk-Run, 25 slides); BAAC ERP Demo Applications (Government Bank
EBS, Finance Modernisation for Banking Reference Architecture, 137 slides); BAAC
ERP Roadmap (3-topic structure with DC+DR Network Diagrams, 32 slides); BAAC TOR
Planning & Budgeting; GSB Hyperion Draft TOR (Price-Performance scoring with 7
ภาคผนวก); GSB FIS Business Requirement (6-module workbook); GSB HRIS Business
Requirement (9-process workbook); GSB Non-Functional Requirement (third-party-
consultant-facilitated Comply Y/N format). YAML frontmatter normalised to spec
(name + description + metadata only).

**V01R02 — 2026.05.14 — Sub-release.**
Same source-pattern enrichment scope as V02R01 above. Structure unchanged from
V01R01: routing tables, tier map, decision-matrix sections, and Quick Reference
Cards remain identical.

**V01R01 — 2026.05.14 — Initial restructure.**
Refactored from monolithic SKILL.md (17.6 K chars) to 5-file package: Lean
Router (this file) plus four lazy-lookup references (decision-matrix,
sub-skill-index, orchestration-playbook, typography-bilingual-qa). Rapid
Workflow calibration locked at 30–60 minutes per deliverable. Eight Worked
Examples (WE-00 through WE-08) and ten Quick Reference Cards (QRC-01 through
QRC-10) seeded. Tier map A/B/C established; disambiguation table built for four
overlap pairs; Industry × Product routing table covers ten customer segments.
