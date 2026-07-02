# TOR Competitive KB — manufacturing — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Records carry per-item confidence (high/medium/low) mapped from the source's [ความเชื่อมั่น] tag. 'high' = at least one official Oracle/NetSuite Help or vendor citation on file; 'medium' = mixed/partner-blog or verify-flagged sources; no record here is invented. This KB is a COMPETITIVE Oracle Fusion selling aid — it deliberately foregrounds where Fusion wins. The iCE balanced second-opinion (many gaps are coverable by NetSuite first-party add-ons, or are over-spec / procurement-fairness risks) is preserved under each record's 'iCE caveat'. Do NOT strip the caveat when reusing wording in a live bid."
ams_review: "yearly — re-verify product positions"
---

> **How to use this file (Oracle Fusion sell-side).** Each section states where Oracle Fusion genuinely out-classes NetSuite for a **manufacturing** buyer, then gives ready-to-paste TOR wording (TH + EN) engineered so a NetSuite-based bid scores **Partial** or **No**. Because iCE also resells NetSuite and answers to สตง.-style procurement scrutiny, every entry keeps the honest counter-view: locking a TOR to a single product's feature is a fairness risk, and several "gaps" are coverable by NetSuite first-party add-ons (Advanced Manufacturing, NSPB, NSAR, NSAW, WMS SuiteApp, FSM, Quality Management SuiteApp). Weaponize on the items where Fusion's edge is **real and material** (process/GMP manufacturing, quality/CAPA depth, EAM breadth); treat the "แทบไม่มีผล / over-spec" items as differentiators to raise only when the buyer's own use case truly needs them.

---

## F-MFG-01 — Process / Mixed-mode Manufacturing

- **Capability (TH):** การผลิตแบบ mixed-mode (discrete + process) รวมสูตรการผลิต (recipe/formula) และการสืบย้อนกลับล็อต (batch genealogy)
- **Capability (EN):** Process / mixed-mode manufacturing (recipe/formula, batch genealogy, potency)
- **Domain:** Manufacturing · **iCE severity:** สูง (High)
- **Oracle Fusion advantage (Standout):** Oracle Manufacturing Cloud natively supports discrete **plus** process **plus** mixed-mode manufacturing on one model. For a regulated biologics / light-pharma line (serum, vaccine, blood-component separation), Fusion carries recipe/formula, batch genealogy and the deeper regulatory batch-record/potency handling that NetSuite's standard ERP does not. NetSuite reaches recipe/formula and co-/by-product only through the paid **Advanced Manufacturing** add-on, and GMP-grade electronic batch record + potency requires custom SuiteScript or an external SuiteApp (blendAPPS / BatchMaster) — a genuine, hard-to-close gap for a GMP producer.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับการผลิตแบบ mixed-mode (ทั้ง discrete และ process manufacturing) รวมถึงสูตรการผลิต (recipe/formula) และการสืบย้อนกลับล็อต (batch genealogy) ในตัว"
- **TOR wording (English):** "The solution must support mixed-mode manufacturing (both discrete and process) including recipe/formula and batch genealogy natively."
- **iCE caveat:** Partially legitimate to spec, but honest. NetSuite Advanced Manufacturing *does* deliver recipe/formula (workbench level) and co-/by-product, and lot/expiry/traceability is native (FEFO via NetSuite's own SuiteApp) — so a blanket "no process manufacturing" claim is over-stated and would draw a fair Partial, not a No. The **material** gap is only GMP/regulated electronic batch record + potency (relevant to a biologics/vaccine unit, not to every plant). Frame the requirement around the regulatory batch-record outcome the buyer actually needs; a "native mixed-mode + full batch genealogy" mandate on a low-volume line risks over-spec and a สตง. challenge.
- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Advanced Manufacturing User Guide (Setting up an Assembly CoProduct 0.62)
  - [KB] NSIMG/Inventory Management (FEFO Lot Allocations SuiteApp 0.69)
  - [WEB:docs.oracle.com] Lot Numbered Items / Lot and Serial Number Trace
  - [WEB:suiteapp.com] blendAPPS Formula & Recipe Management (deep process/recipe usually needs external SuiteApp)

---

## GP-FUNC-01 — Process manufacturing (formula, batch, co/by-products) [3-way: NS 1★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** การผลิตแบบกระบวนการ (สูตร/ล็อต/co-by product)
- **Capability (EN):** Process manufacturing (formula, batch, co/by-products)
- **Domain:** Manufacturing · **iCE severity:** สูง (High) · **Gap Severity (source): Critical**
- **Oracle Fusion advantage (Standout):** Three-way benchmark scores NetSuite 1★ against Oracle Fusion 4★ and SAP S/4HANA 5★. For biologics that must control potency and genealogy tightly, the depth of Oracle (and SAP PP-PI) is real. Fusion wins on native formula/batch depth without bolting on a third-party SuiteApp.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับการผลิตแบบกระบวนการ (process/formula manufacturing) ในตัว: สูตรการผลิต (formula/recipe), การจัดการล็อต/แบทช์, ผลิตภัณฑ์ร่วมและผลพลอยได้ (co-/by-products) พร้อมการสืบย้อนกลับ genealogy ระดับ GMP โดยไม่พึ่ง third-party add-on"
- **TOR wording (English):** "The solution must provide native process/formula manufacturing: formula/recipe, lot/batch management, co-/by-products, and GMP-grade batch genealogy traceability without third-party add-ons."
- **iCE caveat:** This record duplicates F-MFG-01. Same balance applies: NetSuite native has recipe/formula (workbench) + co-/by-product and native lot/batch (FEFO SuiteApp), so 1★ under-states reality. The genuine, close-before-go-live gap is GMP potency/genealogy for a biologics unit — SAP PP-PI is deepest there. Adding a "without third-party add-on" clause is the sharpest lock but also the most fairness-exposed line: use only where a regulated batch record is a true mission requirement.
- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Advanced Manufacturing User Guide (Assembly CoProduct 0.62)
  - [KB] Netsuite-Manufacturing (BOM/routing/Advanced Manufacturing 0.60)
  - [WEB:netsuite.com] Lot Tracking native (FEFO via SuiteApp)
  - [WEB:suiteapp.com] blendAPPS Formula & Recipe Management

---

## TOR-MFG-01 — Process / mixed-mode manufacturing (ready TOR spec)

- **Capability (TH):** ระบบต้องรองรับการผลิตแบบกระบวนการ (process/formula) — recipe/BOM, ล็อต, co-/by-products และ finite scheduling/APS
- **Capability (EN):** Process/formula manufacturing including recipes/BOM, lot/batch, co-/by-products, and finite-capacity scheduling (APS)
- **Domain:** Manufacturing · **iCE severity:** สูง (High) · **Priority (source): Mandatory · NetSuite: No**
- **Oracle Fusion advantage (Standout):** This is the packaged TOR line that bundles process/formula + lot/batch + co-/by-product + finite scheduling (APS) into a single Mandatory requirement. Oracle Manufacturing is strong across all four; SAP PP-PI leads on the regulated end. Bundling tier-1 capabilities into one Mandatory line is the mechanism that forces a NetSuite bid to "No".
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับการผลิตแบบกระบวนการ (process/formula manufacturing) ได้แก่ สูตรการผลิต (recipe/BOM), การจัดการล็อต, ผลิตภัณฑ์ร่วม/ผลพลอยได้ (co-/by-products) และการวางแผนการผลิตแบบจำกัดกำลังการผลิต (finite scheduling/APS)"
- **TOR wording (English):** "The solution shall support process/formula manufacturing including recipes/BOM, lot/batch management, co-/by-products, and finite-capacity production scheduling (APS)."
- **iCE caveat:** The bundling itself is the pressure technique that pushes NetSuite to "No". Honestly, NetSuite Advanced Manufacturing covers recipe/formula (workbench), co-/by-product and finite scheduling, with native lot/batch (FEFO SuiteApp) — so the truthful score is at least **Partial**, not No. Only the GMP/regulated batch-record + potency piece is a real must-add gap. A single Mandatory line stacking multiple tier-1 features is a classic lock-in pattern and the highest procurement-fairness risk in this file; split it into outcome-based sub-criteria if audit exposure matters.
- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Advanced Manufacturing User Guide (CoProduct 0.62 + Finite Scheduling 0.70)
  - [KB] NSIMG/Inventory Management (Lot Numbered / FEFO SuiteApp 0.69)
  - [WEB:docs.oracle.com] Lot Numbered Items / Finite Scheduling
  - [WEB:suiteapp.com] blendAPPS Formula & Recipe Management (deep process mfg uses external SuiteApp)

---

## F-MFG-02 — Advanced Planning & Scheduling (APS / finite scheduling)

- **Capability (TH):** การวางแผนและจัดตารางการผลิตแบบ finite/constraint-based (advanced planning & scheduling)
- **Capability (EN):** Finite scheduling / APS
- **Domain:** Manufacturing · **iCE severity:** แทบไม่มีผล (negligible)
- **Oracle Fusion advantage (Standout):** Oracle Production Scheduling performs full constraint-based, multi-constraint finite-capacity scheduling that optimizes across complex real plant constraints — deeper than NetSuite's work-center-level heuristic. Genuine Fusion edge for large, complex discrete plants.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีการวางแผนและจัดตารางการผลิตแบบ finite/constraint-based (advanced planning & scheduling) โดยคำนึงถึงกำลังการผลิตจริง"
- **TOR wording (English):** "The solution must provide finite/constraint-based advanced planning & scheduling (APS) that accounts for real production capacity."
- **iCE caveat:** Weak weaponization target — the "no finite scheduling" claim is factually wrong. NetSuite Advanced Manufacturing has native finite/capacity scheduling (confirmed in KB and official Help), releasing work orders against machine/labor capacity. Its limit is that it is a work-center heuristic, not a full multi-constraint solver. For a small/mid production line this is over-spec; forcing a constraint-solver-grade APS mandate has no real use case there and reads as a lock-in.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Advanced Manufacturing User Guide (Finite Scheduling 0.70; Scheduling Production 0.67)
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Finite Scheduling (ns-online-help/bridgehead_1508338278)

---

## GP-FUNC-02 — Advanced production scheduling (finite capacity, APS) [3-way: NS 1★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** วางแผนการผลิตแบบจำกัดกำลัง (APS/finite scheduling)
- **Capability (EN):** Advanced production scheduling (finite capacity, APS)
- **Domain:** Manufacturing · **iCE severity:** แทบไม่มีผล (negligible) · **Gap Severity (source): Critical**
- **Oracle Fusion advantage (Standout):** Benchmark scores NetSuite 1★ vs Fusion 4★ / SAP 5★. Measured against full constraint-based APS, NetSuite cannot match Oracle Production Scheduling / SAP — Fusion's optimization depth is the differentiator for complex plants.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมี Advanced Planning & Scheduling (APS) แบบ constraint-based เต็มรูปแบบ ที่ optimize ตารางการผลิตข้ามหลายข้อจำกัด (เครื่องจักร/แรงงาน/วัตถุดิบ) แบบ real-time"
- **TOR wording (English):** "The solution must provide full constraint-based Advanced Planning & Scheduling (APS) that optimizes production schedules across multiple constraints (machine/labor/material) in real time."
- **iCE caveat:** The "only basic work order, no finite scheduling" note is over-stated — finite/capacity scheduling is native in Advanced Manufacturing (KB + official Help, high confidence). What NetSuite lacks is full constraint-solver optimization, which is over-spec for a small-scale production unit with no real APS use case. Raise this only for a genuinely large, constraint-heavy plant.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Advanced Manufacturing User Guide (Finite Scheduling 0.70; Scheduling Production 0.67)
  - [WEB:docs.oracle.com] NetSuite — Finite Scheduling (Help page)

---

## GP-FUNC-03 — Discrete MRP II & shop-floor execution [3-way: NS 2★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** MRP II / shop-floor control เชิงลึก
- **Capability (EN):** Discrete MRP II & shop-floor execution
- **Domain:** Manufacturing · **iCE severity:** ต่ำ (Low) · **Gap Severity (source): High**
- **Oracle Fusion advantage (Standout):** Fusion (4★) and SAP (5★) both out-depth NetSuite's Advanced Manufacturing (2★) on MRP II and shop-floor execution. SAP PP/MES is deepest for large complex discrete shop floors; Oracle Manufacturing Cloud is materially stronger than NetSuite on operation-level MES.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมี MRP II และการควบคุมชั้นการผลิต (shop-floor execution) เชิงลึก: operation-level dispatching, WIP/routing, scrap/rework tracking และ MES integration ในตัว"
- **TOR wording (English):** "The solution must provide deep MRP II and shop-floor execution: operation-level dispatching, WIP/routing, scrap/rework tracking, and native MES integration."
- **iCE caveat:** Fair on depth, but honest. NetSuite (via Advanced Manufacturing) does have MRP/supply planning, routing/WIP and shop-floor control (operation-level reporting, scrap/rework, mobile/tablet) — it is just shallower than SAP PP/MES for large complex discrete floors. For a buyer not running a large discrete line, the excess MES depth does not affect real work. Weaponize only for a heavy discrete manufacturer.
- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [KB] NSIMG/Inventory Management (supply planning / regenerate supply plan 0.57)
  - [KB] Netsuite-Advanced Manufacturing User Guide (Shop Floor: Scanner/Tablet data)
  - [WEB:netsuite.com] Advanced Manufacturing datasheet (finite capacity scheduling, batch management, MES)

---

## F-MFG-03 — Project / Engineer-to-Order Manufacturing

- **Capability (TH):** การผลิตแบบ engineer-to-order (ETO) / project manufacturing ผูกต้นทุนกับโครงสร้างโครงการ (project/WBS)
- **Capability (EN):** Project / ETO manufacturing
- **Domain:** Manufacturing · **iCE severity:** แทบไม่มีผล (negligible)
- **Oracle Fusion advantage (Standout):** Oracle supports project/ETO manufacturing natively, tying production cost to project/WBS structures. NetSuite can link a work order to a project but has no deep engineer-to-order / EPC project-manufacturing costing like Oracle Project Manufacturing or SAP PS+PP — this gap is factually correct.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับการผลิตแบบ engineer-to-order (ETO) / project manufacturing โดยผูกต้นทุนการผลิตกับโครงสร้างโครงการ (project/WBS) ในตัว"
- **TOR wording (English):** "The solution must support engineer-to-order (ETO) / project manufacturing with production cost tied to project/WBS structures natively."
- **iCE caveat:** The technical weakness is real, but ETO/EPC is build-to-order-by-design work (shipbuilding, aerospace, construction contracting). A public-sector / healthcare / non-profit buyer typically has no such business model, so putting this in a TOR is locking a spec that will never be used. Include only if the buyer genuinely runs project/ETO production.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Manufacturing (work order types / project link ~0.60)
  - [KB] Netsuite-Projects (create order/link to project 0.61)

---

## GP-FUNC-22 — Project manufacturing / Engineer-to-Order [3-way: NS 1★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** Project Manufacturing / Engineer-to-Order
- **Capability (EN):** Project manufacturing / ETO
- **Domain:** Project · **iCE severity:** แทบไม่มีผล (negligible) · **Gap Severity (source): High**
- **Oracle Fusion advantage (Standout):** Fusion 4★ / SAP 5★ vs NetSuite 1★. NetSuite does not link project↔manufacturing deeply the way SAP PS+PP does for EPC/ETO — SAP is the standard, Oracle is strong. Duplicates F-MFG-03.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับ project manufacturing / engineer-to-order (ETO) โดยเชื่อมโครงสร้างโครงการ (WBS) เข้ากับใบสั่งผลิตและต้นทุนการผลิตแบบสองทิศทาง (bi-directional) ในตัว"
- **TOR wording (English):** "The solution must support project manufacturing / engineer-to-order (ETO) with bi-directional linkage between the project WBS and production work orders/costs, natively."
- **iCE caveat:** Factually accurate as an SAP/Oracle strength, but no real use case for a healthcare/public-sector/non-profit buyer — build-to-order contracting is outside that mission. Specifying it in a TOR is over-spec / lock-in with no benefit to real work.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Manufacturing (work order/project link ~0.60)
  - [KB] Netsuite-Projects (project→order 0.61)

---

## F-QM-01 — Quality Management (QM / CAPA)

- **Capability (TH):** การบริหารคุณภาพในตัว: แผนการตรวจสอบ (inspection plans), non-conformance (NCR) และ CAPA
- **Capability (EN):** Quality management (inspection / NCR / CAPA)
- **Domain:** Quality · **iCE severity:** สูง (High)
- **Oracle Fusion advantage (Standout):** Oracle Quality Cloud carries inspection, non-conformance and CAPA as depth capabilities. For regulated production (serum/vaccine, blood-component work) NetSuite's free Quality Management SuiteApp covers inspection plans, inspection queue and NCR via SuiteFlow with lot/serial traceability, but **full CAPA** (root-cause 5-Why/Fishbone/8D → corrective action → effectiveness verification) and **pharma GxP validation / electronic batch record** are not out-of-the-box — they need SuiteFlow config or a dedicated QMS SuiteApp (Intellect QMS, QT9). That regulated-quality depth is a real Fusion edge.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีการบริหารคุณภาพ (quality management) ในตัว: แผนการตรวจสอบ (inspection plans), การจัดการของไม่เป็นไปตามข้อกำหนด (non-conformance) และการแก้ไข/ป้องกัน (CAPA)"
- **TOR wording (English):** "The solution must provide native quality management: inspection plans, non-conformance handling and corrective/preventive actions (CAPA)."
- **iCE caveat:** The "no QM at all" framing is over-stated — NetSuite's native Quality Management SuiteApp genuinely handles inspection/NCR + traceability at current scale for a serum/blood-centre unit. Do not over-claim the reverse either: full CAPA and drug validation are real gaps requiring config or a purchased QMS. Weaponize on the **CAPA + GxP validation** wording specifically (where Fusion is strong and NetSuite thin), not on a blanket "no quality management" line, which is inaccurate and challengeable.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Quality User Guide (0.56)
  - [KB] NSIMG (0.57) — non-conformance via SuiteFlow
  - [WEB:brokenrubik.com] NetSuite Quality Management Guide (partner blog) — explicitly not a drug-validation QMS
  - [WEB:docs.oracle.com] NetSuite Quality Inspection Queue

---

## GP-FUNC-26 — Quality Management (QMS), inspection plans [3-way: NS 1★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** ระบบคุณภาพ (QMS) / แผนตรวจสอบ
- **Capability (EN):** Quality Management (QMS), inspection plans
- **Domain:** Quality · **iCE severity:** สูง (High) · **Gap Severity (source): High**
- **Oracle Fusion advantage (Standout):** Fusion 4★ / SAP 5★ vs NetSuite 1★. SAP QM is deepest for regulated industry; Oracle Quality Cloud is strong. Depth to full validated-GxP quality is the real gap NetSuite cannot close natively.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมี Quality Management System (QMS) ในตัวที่รองรับ inspection plans หลายระดับ, non-conformance/CAPA เต็มวงจร และการทำ validation ตามมาตรฐาน GxP/ISO 13485 โดยไม่พึ่ง SuiteApp/third-party"
- **TOR wording (English):** "The solution must provide a native QMS supporting multi-level inspection plans, full-cycle non-conformance/CAPA, and GxP/ISO 13485 validation without reliance on SuiteApp/third-party."
- **iCE caveat:** 1★ misleads — NetSuite's native Quality Management SuiteApp (inspection plan + NCR via SuiteFlow + lot/serial traceability) is genuinely usable (realistically ~3★) and partly supports an ISO 13485 approach. But full CAPA needs SuiteFlow config or a QMS SuiteApp, and it is not a fully validated GxP system like SAP QM — that regulated-pharma depth is the real gap. The "without SuiteApp/third-party" clause is the strongest lock but also the most fairness-exposed; use it only where validated GxP quality is a true mission need.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Quality User Guide (0.56)
  - [KB] NSIMG (0.57) — non-conformance via SuiteFlow
  - [WEB:brokenrubik.com] NetSuite Quality Management Guide (partner blog)
  - [WEB:docs.oracle.com] NetSuite Quality Inspection Queue

---

## F-EPM-04 — Multidimensional profitability & activity-based costing

- **Capability (TH):** การวิเคราะห์กำไรและต้นทุนแบบหลายมิติ (multidimensional profitability & cost allocation) สำหรับ activity-based costing
- **Capability (EN):** Multidimensional profitability & activity-based costing
- **Domain:** EPM · **iCE severity:** ต่ำ (Low)
- **Oracle Fusion advantage (Standout):** Oracle PCMCS (Profitability & Cost Management) provides a full multidimensional profitability and activity-based-costing engine. NetSuite's core has weighted/driver allocation but no full ABC engine — that requires the paid NetSuite Profitability & Cost Management (NSPCM) add-on (same Hyperion/EPM lineage as PCMCS), separately licensed and implemented.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับการวิเคราะห์กำไรและต้นทุนแบบหลายมิติ (multidimensional profitability & cost allocation) สำหรับ activity-based costing ในตัว (native) โดยไม่ต้องซื้อโมดูล EPM แยก"
- **TOR wording (English):** "The solution must support native multidimensional profitability and cost-allocation modelling for activity-based costing, without a separately licensed EPM module."
- **iCE caveat:** "No profitability/allocation engine" is over-stated. NetSuite native allocation (Fixed/Dynamic Allocation Schedules weighted by Statistical Accounts) + Custom Segments allocate indirect cost into program/fund/cost-centre — and NetSuite Help itself states these are "useful in advanced costing such as Activity Based Costing." Mandating a native PCMCS-grade ABC engine is over-spec; if truly needed, NSPCM can be bought (so the honest outcome is Partial, not "cannot do"). The "without a separately licensed EPM module" clause is the effective lock — but note Oracle's own PCMCS is also a separate module, so this wording cuts NetSuite by a standard Fusion itself does not meet natively.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-General Accounting (0.59) — Allocation Schedules across account/department/class/location/custom segment
  - [KB] Netsuite-Statistical Accounting (0.60) — Dynamic Allocation weighted by Statistical Account
  - [KB] Netsuite-Projects (0.50) — Project Profitability / Job Costing
  - [WEB:docs.oracle.com] NetSuite Help — Working with Allocation Schedules Weighted by the Balance of a Statistical Account (chapter_3866895958): "useful in advanced costing such as Activity Based Costing and Usage Based Costing" — verified
  - [WEB:netsuite.com] NetSuite Profitability and Cost Management (EPM add-on)
  - [WEB:oracle.com] Oracle PCMCS — Profitability & Cost Management (same EPM/Hyperion lineage as NSPCM)

---

## GP-FUNC-15 — Advanced cost accounting (multi-method costing) [3-way: NS 2★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** ต้นทุนขั้นสูง (actual/standard หลายวิธี)
- **Capability (EN):** Advanced cost accounting (multi-method costing)
- **Domain:** Finance · **iCE severity:** ต่ำ (Low) · **Gap Severity (source): High**
- **Oracle Fusion advantage (Standout):** Fusion 4★ / SAP 5★ (SAP Material Ledger deepest) vs NetSuite 2★. The genuine gap is deep actual costing across multiple valuations/currencies (SAP CO/ML) — Oracle out-depths NetSuite here, and NetSuite's costing method is set once on the item record and cannot change after posting.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องรองรับ actual costing หลาย valuation/หลายสกุลเงิน (material-ledger-grade) และการเปลี่ยน/กำหนดวิธีต้นทุนได้อย่างยืดหยุ่นรายบัญชี (per-book costing method) ในตัว"
- **TOR wording (English):** "The solution must support multi-valuation / multi-currency actual costing (material-ledger-grade) and flexible per-book costing methods natively."
- **iCE caveat:** "Limited costing methods" under-rates NetSuite — it has **7 native methods** (Average/FIFO/LIFO/Standard/Group Average/Lot-Numbered/Specific) + Landed Cost, and Lot-Numbered costing maps directly to per-lot costing of serum/vaccine/blood products. Structural limits are real (method fixed at item record; Multi-Book sets a per-book *standard cost* but not a per-book *method*). SAP-Material-Ledger depth is over-spec for a non-manufacturing-heavy buyer. The "per-book costing method" clause is the precise lock, because that is exactly the structural line NetSuite cannot cross.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] NSIRM (0.657) — Costing Methods: Average/FIFO/LIFO/Standard/Group Average/Lot/Specific
  - [KB] Netsuite-Item Record Management (0.62) — Group Average, Standard Costing, Cost Category, Landed Cost
  - [KB] Netsuite-Multi-Book Accounting + Item Record Mgmt (0.55) — per-book standard cost (per-book amount)
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Costing Methods (section_N2191818) — verified all 7 methods
  - [WEB:docs.oracle.com] NetSuite Help — Revaluation and Multi-Book Accounting: per-book standard cost (per-book cost, not per-book method) — verified
  - [WEB:netsuite.com] Beyond FIFO & LIFO: Inventory Costing Methods — verified

---

## F-SCM-01 — Demand/supply planning & S&OP

- **Capability (TH):** แพลตฟอร์มวางแผนความต้องการและอุปทาน (demand & supply planning) พร้อม statistical forecasting และ S&OP
- **Capability (EN):** Demand/supply planning & S&OP
- **Domain:** SCM · **iCE severity:** ต่ำ (Low)
- **Oracle Fusion advantage (Standout):** Oracle SCM Planning Cloud is a tier-1 planning platform with demand sensing/ML and enterprise S&OP. NetSuite has native Demand/Supply Planning + DRP (under Advanced Inventory) with 4 basic statistical methods, but no demand sensing/ML and no enterprise S&OP — the enterprise-S&OP half is a real gap.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีแพลตฟอร์มวางแผนความต้องการและอุปทาน (demand & supply planning) พร้อมการพยากรณ์เชิงสถิติ (statistical forecasting) และกระบวนการ S&OP ในตัว"
- **TOR wording (English):** "The solution must provide a native demand & supply planning platform with statistical forecasting and S&OP."
- **iCE caveat:** A flat "score 1 / needs add-on" over-generalizes — basic demand/supply planning is native (Linear Regression / Moving Average / Seasonal Average / Sales Forecast). The real gap is only enterprise S&OP, which is half the requirement, not all of it. For blood/serum demand forecasting, native planning is adequate at scale (short-shelf-life blood may need custom forecast tuning); full S&OP is over-spec. Weaponize on the S&OP clause specifically.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Inventory Management (0.69) — Demand Planning native + Distribution Resource Planning + projection methods
  - [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method, multi-location Supply Allocation
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (4 native statistical methods, /ns-online-help/section_N2290234.html)

---

## GP-FUNC-04 — Demand planning & statistical forecasting [3-way: NS 1★ / Fusion 5★ / SAP 4★]

- **Capability (TH):** วางแผนอุปสงค์ / พยากรณ์
- **Capability (EN):** Demand planning & statistical forecasting
- **Domain:** SCM · **iCE severity:** ต่ำ (Low) · **Gap Severity (source): Critical · Fusion เด่นสุด ✔✔**
- **Oracle Fusion advantage (Standout):** Rare double-check-mark Fusion standout: Oracle SCM Demand Management (5★) leads both NetSuite (1★) and SAP (4★). Demand sensing/ML and collaborative forecasting are the differentiators NetSuite's 4 basic methods do not reach.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีการวางแผนอุปสงค์ขั้นสูง รองรับ demand sensing/ML, การพยากรณ์เชิงสถิติหลายแบบจำลอง และการวางแผนร่วม (collaborative planning) ในตัว"
- **TOR wording (English):** "The solution must provide advanced demand planning with demand sensing/ML, multi-model statistical forecasting, and collaborative planning natively."
- **iCE caveat:** 1★ "very limited" under-states — NetSuite Demand Planning is native with 4 statistical methods, adequate for a charity/public-sector scale; the 1★ reflects a tier-1 benchmark, not real need. Blood/vaccine/serum demand forecasting is covered by native methods without tier-1 demand forecasting. The demand-sensing/ML clause is the lock — genuine Fusion strength, but over-spec unless the buyer truly needs ML forecasting.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Inventory Management (0.69) — Demand Planning analyzes stock demand from historical
  - [KB] NSIMG (0.66) — Demand Plans/Supply Plans, Seasonal Average method
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Calculating Item Demand (Linear Regression/Moving Average/Seasonal Average/Sales Forecast)

---

## GP-FUNC-05 — Sales & Operations Planning (S&OP / IBP) [3-way: NS 0 / Fusion 5★ / SAP 5★]

- **Capability (TH):** S&OP / Integrated Business Planning
- **Capability (EN):** Sales & Operations Planning (S&OP / IBP)
- **Domain:** SCM · **iCE severity:** แทบไม่มีผล (negligible) · **Gap Severity (source): Critical**
- **Oracle Fusion advantage (Standout):** NetSuite scores 0 — it has **no native S&OP/IBP module**; its KB "forecasting" is Sales Force Automation (probability-weighted pipeline), not an operational S&OP process. True S&OP/IBP is Oracle SCP Cloud and SAP IBP (separate license). This is a factually clean gap.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีกระบวนการ S&OP / Integrated Business Planning ในตัว ที่เชื่อมโยงแผนการขาย-การผลิต-การเงินเข้าด้วยกันเป็น consensus plan เดียว"
- **TOR wording (English):** "The solution must provide a native S&OP / Integrated Business Planning process that links sales, production, and financial plans into a single consensus plan."
- **iCE caveat:** The claim is factually correct, but S&OP/IBP is a consensus planning process for large commercial manufacturers/distributors. Mandating it for a public-sector / non-profit buyer is over-spec / lock-in toward Oracle — even a serum/vaccine unit does not run commercial-scale S&OP. Include only where consensus sales-production-finance planning is a real operating process.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Sales Force Automation (0.62) — "forecasting" = sales pipeline / probability-weighted, not S&OP
  - [KB] netsuite_kb — search "S&OP/IBP" finds no real module (top hit 0.50 off-topic) = evidence of no native module
  - [WEB:sap.com] SAP Integrated Business Planning — separate product
  - [WEB:netsuite.com] What Is Integrated Business Planning — educational article, not an in-product module

---

## GP-STANDOUT-06 — Fusion standout: Demand planning & SCM Cloud breadth

- **Capability (TH):** วางแผนอุปสงค์ / SCM Cloud
- **Capability (EN):** Demand planning & SCM Cloud breadth
- **Domain:** SCM · **iCE severity:** ต่ำ (Low) · **Fusion standout Rank 6**
- **Oracle Fusion advantage (Standout):** Oracle SCM Cloud (Demand/Supply/Inventory) is broad and unified inside one suite with ERP — more complete than NetSuite's shallower Demand Planning and cleanly integrated with Finance. SAP IBP is good but sits on a separate license/landscape.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีชุด SCM แบบครบวงจร (demand/supply/inventory planning) บน data model เดียวกับ ERP/Finance โดยไม่ต้องเชื่อมต่อ landscape แยก และรองรับการพยากรณ์เชิงสถิติขั้นสูง"
- **TOR wording (English):** "The solution must provide an end-to-end SCM suite (demand/supply/inventory planning) on the same data model as ERP/Finance, without a separate landscape, and support advanced statistical forecasting."
- **iCE caveat:** Low relevance for a non-commercial buyer. A healthcare/public-sector/non-profit organization is not a large commercial manufacturer/distributor; blood/medical-supply warehousing is covered by NetSuite inventory + reorder point + lot/expiry. Full demand/supply planning (demand sensing/ML/S&OP) is over-spec. Note the "same data model / no separate landscape" phrasing is also a native NetSuite strength (born-in-cloud unified suite), so it does not cleanly separate the two on that axis.
- **Confidence:** low
- **หลักฐาน / Citation:**
  - (Standout record — no per-item KB citation in source; positioning claim only. Confidence set low per anti-hallucination rule.)
  - Corroborated by GP-FUNC-04 evidence: [WEB:docs.oracle.com] NetSuite — Calculating Item Demand (native statistical methods)

---

## GP-FUNC-23 — Enterprise Asset Management & maintenance (EAM) [3-way: NS 1★ / Fusion 4★ / SAP 5★]

- **Capability (TH):** บริหารสินทรัพย์/ซ่อมบำรุงองค์กร (EAM)
- **Capability (EN):** Enterprise Asset Management & maintenance (EAM)
- **Domain:** Asset · **iCE severity:** กลาง (Medium) · **Gap Severity (source): High**
- **Oracle Fusion advantage (Standout):** Fusion 4★ / SAP 5★ vs NetSuite 1★. NetSuite's base FAM (SuiteApp) does only depreciation/revaluation/disposal + maintenance schedule/insurance — **no work order**. Work-order-based maintenance requires the separate NetSuite Field Service Management module. Heavy-plant EAM (linear asset / reliability) is a genuine SAP PM / Oracle Maintenance Cloud strength.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีการบริหารสินทรัพย์และซ่อมบำรุงระดับองค์กร (EAM) ในตัว: work order, preventive/predictive maintenance, meter reading, asset hierarchy และ reliability/linear-asset management โดยไม่พึ่งโมดูล field service แยก"
- **TOR wording (English):** "The solution must provide native enterprise asset management (EAM): work orders, preventive/predictive maintenance, meter readings, asset hierarchy, and reliability/linear-asset management, without a separate field-service module."
- **iCE caveat:** 1★ under-states — NetSuite Field Service Management (first-party after Oracle acquired Next Technik, Oct 2023) delivers work order, preventive maintenance (time/usage/meter-based auto-generation), asset hierarchy and maintenance history; it is a separate purchase and leans toward field service, and is **not** full predictive/condition-based EAM. PM of medical/lab/cold-chain equipment is genuinely relevant (though hospitals often use a specialist biomedical CMMS); heavy-plant EAM is over-spec. The "reliability/linear-asset + no separate field-service module" clause is the effective lock.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Fixed Assets Management (0.60) — depreciation + maintenance schedule/insurance, no work order
  - [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
  - [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance (hours/mileage/cycles) auto-generates jobs
  - [WEB:oracle.com] Oracle acquires Next Technik — FSM becomes first-party (2023)

---

## TOR-EAM-01 — Enterprise Asset Management & maintenance (ready TOR spec)

- **Capability (TH):** ระบบต้องมี EAM รองรับ work order, preventive/predictive maintenance, meter reading และประวัติการบำรุงรักษา
- **Capability (EN):** EAM with work orders, preventive/predictive maintenance, meter readings, and maintenance history
- **Domain:** Asset / EAM · **iCE severity:** กลาง (Medium) · **Priority (source): Important · NetSuite: No**
- **Oracle Fusion advantage (Standout):** Oracle Maintenance Cloud is strong and SAP PM/EAM leads for heavy plant. NetSuite base FAM is depreciation-only. Predictive / condition-based EAM is the axis NetSuite (via FSM) cannot fully reach.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีการบริหารสินทรัพย์และซ่อมบำรุง (Enterprise Asset Management) รองรับ work order, preventive/predictive maintenance, meter reading และประวัติการบำรุงรักษา"
- **TOR wording (English):** "The solution shall provide Enterprise Asset Management (EAM) with work orders, preventive/predictive maintenance, meter readings, and maintenance history."
- **iCE caveat:** "No" over-states — NetSuite FSM (first-party) delivers work order, preventive maintenance (time/usage-based), asset hierarchy and maintenance history; meter/usage-based auto-generates work orders. The source explicitly cuts the word "predictive" from what can be confirmed — FSM verifies only **preventive + usage-based**, not full predictive/condition-based EAM. So the honest rating is **Partial**, not No. The **"predictive"** qualifier is therefore the sharp weaponization lever (Fusion/SAP have it; NetSuite does not) — but keep it honest: PM of cold-chain/medical equipment is a real need coverable by FSM, while full-plant predictive EAM is over-spec.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Fixed Assets Management (0.60) — base FAM = depreciation + maintenance schedule, no work order
  - [WEB:netsuite.com] NetSuite Field Service Management — work orders, automated preventive maintenance, asset hierarchy
  - [WEB:netsuite.com] FSM datasheet — usage/meter-based maintenance auto-generates work orders
  - [WEB:oracle.com] Oracle acquires Next Technik — FSM becomes first-party (2023)

---

## GP-FUNC-24 — Configure-Price-Quote (CPQ) & complex pricing [3-way: NS 2★ / Fusion 4★ / SAP 4★]

- **Capability (TH):** CPQ / กำหนดราคาซับซ้อน
- **Capability (EN):** Configure-Price-Quote (CPQ) & complex pricing
- **Domain:** Order Mgmt · **iCE severity:** แทบไม่มีผล (negligible) · **Gap Severity (source): Med**
- **Oracle Fusion advantage (Standout):** Fusion 4★ / SAP 4★ vs NetSuite 2★. Oracle CPQ and SAP have a stronger configurator for highly complex product configuration than NetSuite CPQ.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมี Configure-Price-Quote (CPQ) ในตัวที่รองรับ configurator กฎซับซ้อนหลายชั้น, guided selling และการกำหนดราคาแบบหลายเงื่อนไข (complex/tiered pricing) ระดับองค์กร"
- **TOR wording (English):** "The solution must provide native CPQ with a multi-layer rules configurator, guided selling, and enterprise complex/tiered pricing."
- **iCE caveat:** Weak weaponization target and low relevance. NetSuite CPQ is a native product (from the Verenia acquisition) with Configurator, Guided Selling, Proposal Generator and Manufacturing Integration; it trails Oracle/SAP only on very-high-complexity configuration. For a healthcare/public-sector/non-profit buyer (blood/serum/hospital/relief/donations) there is essentially no CPQ use case — so specifying it is over-spec / lock-in with no impact on real work.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-SuiteCommerce Store Front (0.56) — only quote/pricing, no configurator engine
  - [WEB:netsuite.com] NetSuite CPQ product page
  - [WEB:docs.oracle.com] NetSuite CPQ Overview

---

### Coverage note
19 manufacturing-tagged records included: F-MFG-01, F-MFG-02, F-MFG-03, F-QM-01, F-EPM-04, F-SCM-01 (TOR Requirement Bank); GP-FUNC-01, GP-FUNC-02, GP-FUNC-03, GP-FUNC-04, GP-FUNC-05, GP-FUNC-15, GP-FUNC-22, GP-FUNC-23, GP-FUNC-24, GP-FUNC-26, GP-STANDOUT-06 (Gap Pack); TOR-MFG-01, TOR-EAM-01 (Gap Pack TOR spec). Records whose source `verticals` array did not include "manufacturing" (e.g. F-WMS-01, F-PRC-02, F-PRJ-01, GP-FUNC-06/07, TOR-SCM-02) are intentionally excluded from this industry file.
