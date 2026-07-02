# TOR Competitive KB — bfsi-fintech — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: >
  Confidence is per-record and reflects whether an official KB / Oracle-NetSuite Help /
  suiteapp.com / analyst citation exists in the source record. "high" = corroborated by
  official documentation or KB with score; "medium" = partly documented or depends on
  product position that should be re-verified against a live environment; "low" = no hard
  citation in the source. The underlying dataset is a COMPETITIVE TOR draft deliberately
  biased toward Oracle Fusion (NetSuite scored Partial/No, Fusion scored Fully) — every
  record therefore carries the iCE balanced counter-view: many "gaps" are coverable by
  NetSuite first-party add-ons (NSPB = Oracle PBCS engine, NetSuite Account Reconciliation
  = Oracle Fusion EPM, NSAW = Oracle ADW + Analytics Cloud), or are over-spec for a single-
  entity Thai organization, or are procurement risks (locking a spec to one product invites
  a สตง. / competing-bidder challenge). Product positions are mid-2026; items tagged
  [ต้อง verify] must be confirmed with the live environment / vendor before decision.
ams_review: "yearly — re-verify product positions"
---

> **How to use this file (iCE internal).** This is the bfsi-fintech cut of the NetSuite
> weakness/counter knowledge base. Use it when iCE **sells NetSuite** into a bank / insurer /
> FinTech account, or when iCE must **defend NetSuite against a Fusion-biased TOR**. For every
> requirement you will find (a) the raw gap as the competitive TOR frames it, (b) the honest
> iCE counter / mitigation, and (c) — where relevant — the procurement caveat. Records here
> map to bfsi-fintech either directly (consolidation, treasury, GRC/SoD, multi-GAAP) or as
> cross-cutting controls that carry disproportionate weight in a regulated financial-services
> and public-audit (สตง.) context. Client identities in the source have been generalized to
> healthcare / blood-bank / non-profit-foundation / public-sector patterns.

---

## F-EPM-02 — การรวมงบการเงินขั้นสูง / Advanced financial consolidation

- **Capability (TH):** การรวมงบการเงิน (consolidation) ขั้นสูง — multi-tier ownership %, equity method, matrix consolidation
- **Capability (EN):** Advanced financial consolidation (multi-tier ownership, equity method, matrix consolidation)
- **Domain:** EPM · **iCE severity:** แทบไม่มีผล (negligible)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The competitive TOR frames NetSuite OneWorld as "mid-market only" — no multi-tier ownership %, no equity-method accounting, no matrix consolidation — against Oracle FCCS, which supports multi-tier ownership structures, equity pickup, and both statutory and management views. The genuine residual weakness is real but narrower than the TOR claims: NetSuite OneWorld does perform multi-tier subsidiary consolidation, automatic intercompany elimination, and currency translation/CTA natively, and it does carry an Ownership % field — but it does **not** post/adjust NCI (non-controlling interest) automatically, and it does not natively handle equity method, step acquisition, fair-value NCI, or elimination of intercompany profit in inventory. Those cases require a SuiteApp (e.g. Eide Bailly NCI Module) or manual adjustment. For a multinational group with many JVs/associates and partial ownership, Oracle FCCS is clearly ahead.

**Counter / Mitigation:**
- **Rebuttal to "ไม่มี ownership %":** false — OneWorld does multi-tier hierarchy + Intercompany Auto Elimination + consolidated exchange rates natively.
- **Rebuttal to "ครบในตัว" (the opposite over-claim):** also wrong — NCI/equity method is not automated.
- **First-party / SuiteApp path:** close the partial-ownership / NCI gap with a certified SuiteApp (Eide Bailly NCI Module) or scheduled manual NCI journals.
- **Over-spec rebuttal (bfsi-fintech context):** for a single legal entity with no multi-tier / JV / associate structure, FCCS-grade consolidation is essentially unused. Only invoke the full counter when the account genuinely has a complex holding structure — for a single-entity organization this requirement is over-spec.

**Procurement caveat:** Writing a TOR that mandates equity-method / matrix / multi-tier NCI consolidation for a single-entity buyer is a spec-lock toward FCCS; it should be justified by an actual group structure, otherwise it is challengeable by other bidders / สตง.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
- [KB] Netsuite-NetSuite OneWorld Guide (consolidation, 0.60) — subsidiary as legal entity / nexus / base currency
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier hierarchy, auto elimination, CTA, Ownership % with equity-method / complex-NCI limits
- [WEB:suiteapp.com] Eide Bailly NCI Module for Partially-Owned Subsidiaries — confirms NetSuite does not auto-post partial-ownership NCI

---

## F-EPM-03 — การกระทบยอดบัญชีอัตโนมัติ + close orchestration / Automated reconciliation & close

- **Capability (TH):** การกระทบยอดบัญชี (account reconciliation) อัตโนมัติ + transaction matching + close orchestration
- **Capability (EN):** Automated reconciliation & close orchestration
- **Domain:** EPM · **iCE severity:** กลาง (medium)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The TOR asserts that base NetSuite offers only a period-close checklist + bank reconciliation — no automated transaction matching and no financial-close orchestration — against Oracle ARCS. The genuine weakness: the **base ERP** does indeed ship only the period-close checklist + bank rec; the advanced matching/orchestration capability lives in a separately licensed add-on module. If the buyer does not license that add-on, the TOR's description holds.

**Counter / Mitigation:**
- **First-party add-on (this is the mitigation):** since June 2023, NetSuite ships **NetSuite Account Reconciliation (NSAR)**, built on the **Oracle Fusion EPM** platform — a transaction-matching engine that matches/exports at multi-million-row scale (up to ~5,000,000 CSV rows), reconciliation templates across many account types (AP/AR/bank/prepaid/accrual/FA/intercompany), audit trail, and close management. The historic gap is therefore closed by a NetSuite first-party module using the same Oracle engine Fusion itself uses.
- **TCO framing:** NSAR is a paid add-on, not bundled in base ERP — but Oracle Fusion also licenses ARCS separately, so this criterion cuts NetSuite by a standard Fusion itself must also buy.
- **Over-spec rebuttal (bfsi-fintech context):** for a single legal entity, million-row automated matching is nice-to-have; period close + bank rec cover the real workload. Genuine reconciliation volume for most single-entity finance shops does not reach that scale.

**Procurement caveat:** none material; note only that "native automated matching" in the TOR should acknowledge it is an add-on on both NetSuite and Fusion.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:prnewswire.com] NetSuite Account Reconciliation announced 2023-06-14 — built on Oracle Fusion EPM, transaction-matching engine + reconciliation/close management
- [WEB:oracle.com] NSAR What's New 2023 — transaction matching export up to 5,000,000 CSV rows
- [KB] Netsuite-General Accounting (reconciliation_close, 0.62) — Period Close Checklist
- [KB] NETSUITE_FOR_CONSULTANTS (reconciliation_close, 0.63) — Period Close / period lockdown

---

## F-FIN-01 — Multi-GAAP / secondary ledgers

- **Capability (TH):** Multi-GAAP / บัญชีแยกประเภทรอง (secondary/reporting ledgers)
- **Capability (EN):** Multi-GAAP / secondary ledgers
- **Domain:** Finance · **iCE severity:** ต่ำ (low)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The TOR positions NetSuite Multi-Book as narrower — limited parallel/secondary ledger support — against Oracle's primary + multiple secondary/reporting ledgers with automated mapping. The genuine weakness: NetSuite Full Multi-Book Accounting supports **1 primary + up to 4 secondary books (5 active books total)**, and it must be enabled via OneWorld + NetSuite Professional Services only. That is less flexible than Oracle's larger reporting/secondary-ledger count; an organization needing many books will hit the ceiling.

**Counter / Mitigation:**
- **First-party capability:** Full Multi-Book Accounting already delivers "primary + secondary ledgers + automated mapping" — each book can carry a different standard (US GAAP / IFRS / tax / management) with per-book COA mapping rules and per-book currency revaluation. This maps directly onto the TOR wording.
- **Over-spec rebuttal (bfsi-fintech context):** a single-jurisdiction entity typically needs primary (Thai statutory) + perhaps one IFRS / management book — comfortably inside the 4-secondary-book ceiling. The cap only bites for multi-book-heavy multinationals.

**Procurement caveat:** if the TOR demands an unbounded number of reporting ledgers, that is a spec-lock toward Oracle; state the actual number of books required and confirm it exceeds 4 before making it a differentiator.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — Full/Adjustment-Only secondary books, OneWorld only, multiple record sets from one transaction
- [WEB:docs.oracle.com] Planning for Multi-Book Accounting — up to 4 secondary books (5 active total), differing COA/currency/accounting rules
- [WEB:netsuite.com] Multi-Book Accounting — per-standard COA mapping rules

---

## GP-FUNC-12 — งบรวมกลุ่มหลายมาตรฐานบัญชี ขนาดใหญ่ / Group consolidation & multi-GAAP at scale

- **Capability (TH):** งบรวมกลุ่มหลายมาตรฐานบัญชี ขนาดใหญ่
- **Capability (EN):** Group consolidation & multi-GAAP at scale
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล (negligible)
- *3-way gap position: NetSuite ★★★ (3) · Oracle Fusion ★★★★★ (5) · SAP S/4HANA ★★★★ (4)*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
For large groups — dozens of cross-border entities with partial ownership — Oracle FCCS (Hyperion lineage) leads on complex consolidation (NCI / equity method, multi-GAAP at scale). NetSuite OneWorld + Multi-Book does basic consolidation + multi-GAAP natively but is constrained in the most complex cases.

**Counter / Mitigation:**
- **This gap-pack record is already balanced** (it scores NetSuite 3/5, not 1). The rebuttal is that OneWorld + Multi-Book covers mid-market consolidation and multi-GAAP in-product; the FCCS advantage is real only for large, complex, partial-ownership groups.
- **Over-spec rebuttal (bfsi-fintech context):** "group consolidation & multi-GAAP at scale" exceeds the need of a single Thai legal entity — in a single-entity TOR this is over-spec with no real use case.

**Procurement caveat:** "at scale" and "multi-GAAP" phrasing should be tied to the buyer's actual entity count; otherwise it tilts scoring toward FCCS.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — secondary books multi-GAAP
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — OneWorld sufficient for mid-market but limited in complex cases (equity method, complex NCI)

---

## GP-FUNC-14 — บริหารเงินสด/เงินทุน (Treasury) / Treasury & cash / bank-risk management

- **Capability (TH):** บริหารเงินสด/เงินทุน (Treasury) — cash position, bank rec, in-house bank, FX risk
- **Capability (EN):** Treasury & cash / bank-risk management
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล (negligible)
- *3-way gap position: NetSuite ★ (1) · Oracle Fusion ★★★★ (4) · SAP S/4HANA ★★★★★ (5)*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The gap pack says NetSuite has "no treasury module" (SAP TRM being deepest). The genuine weakness: NetSuite has **no full Treasury Management System** — no FX / interest-rate hedging, no in-house banking, no portfolio management à la SAP TRM.

**Counter / Mitigation:**
- **First-party capability:** NetSuite **Cash Management** works in-product: real-time cash position, automated bank reconciliation (intelligent matching + Bank Feeds, a free NetSuite SuiteApp), and payment/bank-account management. The "1★ / no treasury module" scoring is overstated — the everyday cash-positioning + bank-rec workload is native.
- **Third-party path for the true gap:** in-house banking + FX hedging require connecting a dedicated TMS (e.g. Kyriba).
- **Over-spec rebuttal (bfsi-fintech context):** hedging / in-house bank is multinational-group treasury; for a THB-denominated single entity there is essentially no use case — over-spec. (Note: for an actual FinTech/bank with genuine FX or interest-rate exposure this counter weakens; qualify the account's real treasury book before leaning on "over-spec.")

**Procurement caveat:** mandating a native in-house-bank / FX-hedging module is a spec-lock unless the buyer runs a real treasury desk.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Financial Statements Guide (0.5694, Cash Statement)
- [WEB:netsuite.com] What is NetSuite Cash Management Software
- [WEB:houseblend.io] Kyriba vs NetSuite Treasury — no native FX hedging / in-house bank (secondary)

---

## GP-FUNC-17 — บัญชีสัญญาเช่า (IFRS16 / ASC842) / Lease accounting

- **Capability (TH):** บัญชีสัญญาเช่า (IFRS16/ASC842) ในตัว
- **Capability (EN):** Lease accounting (IFRS16 / ASC842)
- **Domain:** Finance · **iCE severity:** กลาง (medium)
- *3-way gap position: NetSuite ★ (1) · Oracle Fusion ★★★★ (4) · SAP S/4HANA ★★★★ (4)*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The gap pack says NetSuite "must use a SuiteApp" for lease accounting while Fusion/SAP have it native. The genuine weakness: NetSuite has **no free native** lease-accounting engine in core — the capability lives in the **Fixed Assets Management (FAM)** module, a first-party SuiteApp add-on that must be installed/configured and generally carries a separate license + implementation effort.

**Counter / Mitigation:**
- **First-party add-on (the mitigation):** FAM is NetSuite's own module and covers **IFRS 16 / ASC 842** in full (operating/finance lease, amortization, automatic journals), and with Multi-Book can run ASC 842 + IFRS 16 in parallel. So "1★ / must use a SuiteApp" misleadingly implies it can barely be done — FAM does it, but honestly it is a paid add-on, not free-in-the-box.
- **Third-party path:** very complex lease portfolios sometimes choose a third-party (e.g. NetLease by Netgain).
- **Balanced view (bfsi-fintech context):** where TFRS 16 applies to material building/equipment leases (common for banks/insurers with branch estates), plan budget/resource to enable FAM. It is a manageable-cost add-on, **not a blocker**.

**Procurement caveat:** "native, no add-on" phrasing is a spec-lock; FAM is first-party and satisfies the standard, so the requirement should read "supports IFRS 16/ASC 842" not "in core without any module."

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Fixed Assets Management (0.551, Lease Accounting)
- [WEB:docs.oracle.com] Fixed Assets Lease Accounting (IFRS 16 / ASC 842)
- [WEB:netsuite.com] Lease Accounting Changes: ASC 842 & IFRS 16; NetLease by Netgain = third-party add-on for complex portfolios

---

## GP-FUNC-27 — กำกับ ความเสี่ยง การควบคุม / SoD / Governance, Risk & Compliance (GRC)

- **Capability (TH):** กำกับ ความเสี่ยง การควบคุม (GRC) / SoD
- **Capability (EN):** Governance, Risk & Compliance (GRC) / SoD
- **Domain:** GRC · **iCE severity:** สูง (high)
- *3-way gap position: NetSuite ★★ (2) · Oracle Fusion ★★★★★ (5) · SAP S/4HANA ★★★★★ (5)*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
NetSuite's native GRC = role/permission management + audit trail + approval workflow + access-audit tooling (saved-search / role audit). What NetSuite markets as "GRC" is an umbrella of native controls + partner SuiteApps — it is **not** a native automated-SoD / continuous-controls-monitoring engine like Oracle Risk Management Cloud or SAP GRC Access Control.

**Counter / Mitigation:**
- **First-party controls that are real:** role/permission audit, always-on audit trail, approval workflow, and access-review searches ship native — so "basic SoD/role review" understates the native audit tooling.
- **Certified SuiteApp path (the mitigation):** close the automated-SoD / CCM gap with a certified SuiteApp — **Fastpath Assure, Netwrix Strongpoint, or SafePaaS** — at a manageable cost.
- **bfsi-fintech / audit context:** this is a genuine and high-weight gap for a financial-services organization under สตง. audit — SoD over payments, procurement, and收 processing is a governance requirement. Plan the certified SoD SuiteApp and design the control matrix **before go-live**. Full enterprise-grade continuous-controls monitoring versus Oracle Advanced Access Controls is an optional extra beyond the baseline need.

**Procurement caveat:** "native automated SoD engine in-product" is where Oracle/SAP genuinely win — but requiring it *natively* is over-spec; the audit-satisfying SoD a regulated buyer actually needs is achievable with NetSuite native (detective) + certified SuiteApp (preventive). Do not let the TOR conflate "must have SoD controls" (legitimate) with "must have a native SoD engine" (spec-lock).

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.695 / 0.6678) — role permissions + audit role searches
- [WEB:netsuite.com] What is NetSuite Governance, Risk & Compliance? — GRC = native controls + partner SuiteApp (not a native SoD engine)
- [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring
- [WEB:netwrix.com] NetSuite Segregation of Duties (Strongpoint) — alert on SoD conflicts
- [WEB:suiteapp.com] Fastpath Assure for NetSuite

---

## GP-TECH-11 — ควบคุมสิทธิ์ละเอียด / SoD อัตโนมัติ / Fine-grained access & automated SoD controls

- **Capability (TH):** ควบคุมสิทธิ์ละเอียด / SoD อัตโนมัติ
- **Capability (EN):** Fine-grained access & automated SoD controls
- **Domain:** Technical · **iCE severity:** สูง (high)
- *3-way gap position: NetSuite ★★ (2) · Oracle Fusion ★★★★★ (5) · SAP S/4HANA ★★★★★ (5)*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The technical gap pack frames NetSuite as "role-based basic" against Oracle Risk Management / SAP GRC automated SoD + continuous controls. The genuine weakness: NetSuite has **no native ruleset-based automated SoD** and **no native preventive continuous-controls monitoring** — it does detective-only controls (e.g. Login Audit Trail, role-diff/audit searches).

**Counter / Mitigation:**
- **Rebuttal to "role-based basic":** understated — NetSuite has genuinely fine-grained access (view/create/edit/full permission per record/feature, **636+ permissions**), Login Audit Trail, role-diff/audit searches, plus 2FA / TBA / password policy. This is not merely "basic role-based."
- **Certified SuiteApp path (the mitigation):** close the automated/preventive SoD + continuous-monitoring gap with Fastpath Assure, Netwrix Strongpoint, or SafePaaS (market-standard).
- **bfsi-fintech / audit context:** fine-grained access is required and NetSuite does it well; automated continuous SoD is the genuine native gap and, for a financial-services buyer under สตง. audit, should be closed with an add-on and budgeted before go-live.

**Procurement caveat:** requiring automated SoD / CCM **natively in-product** is over-spec relative to the actual audit need; the requirement should permit a certified add-on to satisfy the control.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6691) — granular permission structure (636+ permissions)
- [KB] Netsuite-Authentication Guide — 2FA / token-based auth; Netsuite-Administrator Guide (0.6642) — password policy + SoD monitoring example (PO created by AP)
- [WEB:oracle.com] Oracle Advanced Access Controls — continuous SoD monitoring
- [WEB:mysuite.tech] NetSuite SoD native vs add-on boundary (detective not preventive)

---

## NF-SEC-01 — Automated Segregation of Duties (SoD) & access governance

- **Capability (TH):** การแบ่งแยกหน้าที่ (SoD) แบบอัตโนมัติ + access governance + risk management
- **Capability (EN):** Automated SoD & access governance
- **Domain:** Technical · **iCE severity:** สูง (high)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The TOR says NetSuite has role-based security but no SoD automation / audit-grade access governance, against Oracle Risk Management Cloud. The genuine weakness: NetSuite has **no out-of-the-box native automated-SoD engine / continuous-controls monitoring** — that must be added via SuiteApp (Fastpath Assure, Netwrix Strongpoint, SafePaaS).

**Counter / Mitigation:**
- **First-party controls that are real:** granular role-based access + approval routing (SuiteFlow / SuiteApprovals), built-in access-audit tools (Use Searches to Audit Roles, Show Role Permission Differences), Login Audit Trail, 2FA/SSO, and genuine SOC 1/2 + ISO 27001 audits. The original "no audit-grade access governance" claim understates this.
- **Certified SuiteApp path (the mitigation):** close the native automated-SoD engine gap with a certified SuiteApp at manageable cost. Oracle Advanced Access Controls (Risk Management Cloud) is genuinely stronger on automated ruleset SoD + continuous monitoring.
- **bfsi-fintech / audit context:** SoD spans donation-intake / payments / procurement that sit under สตง. audit, so this is high-weight for a regulated financial-services buyer — plan a certified SuiteApp to close the gap before go-live. Enterprise-grade automated GRC beyond that is over-spec for a single-jurisdiction organization.

**Procurement caveat:** same spec-lock pattern as GP-FUNC-27 / GP-TECH-11 / TOR-TECH-05 — "native automated SoD engine" favors Oracle; permit a certified add-on to satisfy the control.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
- [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review / terminated-user revocation
- [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + large prebuilt ruleset
- [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
- [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## TOR-FIN-02 — งบการเงินรวมหลายระดับ, multi-GAAP, auditable close / Multi-level group consolidation

- **Capability (TH):** งบการเงินรวมหลายระดับ หลายมาตรฐานบัญชี (multi-GAAP/IFRS) + intercompany elimination + currency translation + audit trail ปิดงบอัตโนมัติ
- **Capability (EN):** Multi-level group consolidation, multi-GAAP, auditable automated close
- **Domain:** Finance (Consolidation) · **iCE severity:** กลาง (medium)
- *TOR framing: NetSuite = Partial · Priority = Mandatory*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The TOR-spec requires multi-level group consolidation across multiple accounting standards (multi-GAAP/IFRS), intercompany elimination, currency translation, and an auditable automated close — and scores NetSuite "Partial" behind Oracle FCCS. The genuine residual weakness: **auditable automated close** is not native (needs the NSAR add-on), and complex NCI / equity-method cases need a SuiteApp or manual work.

**Counter / Mitigation:**
- **Reads closer to "Fully" than "Partial":** against the literal requirement, NetSuite covers most of it in-product — OneWorld (multi-tier + auto elimination + CTA) and Multi-Book (multi-GAAP) are native.
- **First-party add-on:** the "auditable automated close" leg is delivered by **NetSuite Account Reconciliation (NSAR)**, a paid add-on on the Oracle Fusion EPM platform; complex NCI/equity method needs a SuiteApp / manual adjustment.
- **bfsi-fintech context:** the real need (consolidating multiple funds/units + IFRS) is genuinely supported; impact is limited to the NSAR add-on cost and the small slice of close complexity beyond mid-market.

**Procurement caveat:** if "multi-level / multi-standard" is read as extreme-complexity enterprise (equity method, NCI, large scale), FCCS is ahead — so a "Partial" score is defensible **only at the complexity edge**, and the NSAR add-on cost must be counted. Setting the bar at "Partial" for a buyer whose actual need is multi-fund + IFRS has a spec-lock character; state the real complexity.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates (currency translation)
- [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — multi-GAAP secondary books
- [WEB:prnewswire.com] NetSuite Account Reconciliation 2023-06-14 — auditable automated close (add-on)
- [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier consolidation, auto elimination, CTA + NCI/equity-method limits

---

## TOR-FIN-04 — Treasury & Cash Management / โมดูลบริหารเงินสดและเงินทุน

- **Capability (TH):** โมดูลบริหารเงินสดและเงินทุน (Treasury & Cash Management) ในตัว — cash position, bank rec อัตโนมัติ, in-house bank, FX risk
- **Capability (EN):** Native Treasury & Cash Management (cash positioning, automated bank rec, in-house banking, FX risk management)
- **Domain:** Finance (Treasury) · **iCE severity:** แทบไม่มีผล (negligible)
- *TOR framing: NetSuite = No · Priority = Important*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The TOR scores NetSuite "No" — no treasury module — against Fusion/SAP. The genuine weakness: **in-house banking + FX risk management/hedging** are not native (require an external TMS such as Kyriba).

**Counter / Mitigation:**
- **"No" is wrong — it is Partial:** 2 of the 4 sub-requirements (cash positioning, automated bank reconciliation) are first-party in **NetSuite Cash Management** (Bank Feeds / intelligent matching). Only in-house banking + FX hedging are missing natively.
- **Third-party path for the true gap:** connect a TMS (e.g. Kyriba) for in-house banking / FX hedging.
- **Over-spec rebuttal (bfsi-fintech context):** in-house bank + FX hedge are multinational-group treasury functions with essentially no use case for a THB single entity; the cash-positioning + multi-account bank-rec the buyer actually uses are already native. (Qualify: for a genuine bank/FinTech with FX or an actual treasury book, the hedging leg becomes relevant — do not blanket-call it over-spec without checking the account.)

**Procurement caveat:** scoring NetSuite "No" when 2/4 sub-requirements are native is a mis-scoring that favors Fusion/SAP; correct it to "Partial" and separate the genuinely-missing hedging/in-house-bank legs.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Cash Management Software (automated bank reconciliation)
- [WEB:houseblend.io] NetSuite Treasury — no native FX hedging / in-house banking (secondary)
- [KB] Netsuite-Financial Statements Guide (0.5453, Cash Flow Statement)

---

## TOR-TECH-05 — GRC / automated SoD controls (TOR spec)

- **Capability (TH):** การควบคุมสิทธิ์การเข้าถึงแบบละเอียด + SoD อัตโนมัติ + continuous controls monitoring ในตัว
- **Capability (EN):** Fine-grained access control with automated SoD checks and built-in continuous controls monitoring
- **Domain:** Technical (GRC) · **iCE severity:** สูง (high)
- *TOR framing: NetSuite = Partial · Priority = Important*

**จุดที่ NetSuite สู้ไม่ได้ (Gap):**
The TOR-spec requires fine-grained access control + automated SoD + built-in continuous controls monitoring, scoring NetSuite "Partial." The genuine weakness: **built-in continuous controls monitoring** and **automated preventive SoD** (ruleset-based block of self-approval) are not native.

**Counter / Mitigation:**
- **First-party controls that are real:** NetSuite does fine-grained access control natively and does **detective** SoD (saved-search / role audit, e.g. finding records where creator = approver).
- **Certified SuiteApp path (the mitigation):** the preventive / continuous-monitoring leg is closed with a market-standard certified SuiteApp — **Fastpath Assure, Netwrix Strongpoint, or Greenlight Approvals** (preventive self-approval blocking + automated SoD).
- **bfsi-fintech / audit context:** highly relevant because SoD sits directly under สตง. audit — plan the SuiteApp to close preventive SoD and have the control matrix ready before go-live to pass audit. Native, full continuous-controls monitoring is a multinational-grade feature that is over-spec for a Thai single-jurisdiction NGO/entity.

**Procurement caveat:** "continuous controls monitoring built-in" is a genuine native gap (Oracle/SAP ahead), but mandating it *in-product* is over-spec; the SoD a regulated buyer truly needs is deliverable via NetSuite native (detective) + certified SuiteApp (preventive). Permit the add-on in the TOR wording.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native does not block self-approval by ruleset)
- [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
- [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
- [KB] Netsuite-Managing Users & Roles (0.6544) — access review / audit guidance (manual)

---

## Cross-record synthesis (bfsi-fintech quick read)

- **Recurring true gap (plan add-on before go-live):** automated / preventive **SoD + continuous controls monitoring** (GP-FUNC-27, GP-TECH-11, NF-SEC-01, TOR-TECH-05). All four are the *same* gap at different framings, all iCE severity **สูง**, all closable with a certified SuiteApp (Fastpath Assure / Netwrix Strongpoint / SafePaaS / Greenlight Approvals). In a สตง.-audited financial-services account this is the one cluster to budget and design early — not a blocker, but not to be waved away.
- **Add-on-covered, TCO-parity story:** advanced reconciliation/close (F-EPM-03 → NSAR), lease accounting (GP-FUNC-17 → FAM). Both are NetSuite first-party add-ons on Oracle engines; Fusion licenses the equivalents separately too, so the honest framing is TCO parity, not capability absence.
- **Over-spec / mis-scored for a single entity:** advanced consolidation & multi-GAAP-at-scale (F-EPM-02, GP-FUNC-12, TOR-FIN-02), multi-GAAP secondary ledgers (F-FIN-01), treasury (GP-FUNC-14, TOR-FIN-04). Genuine FCCS/TRM advantage exists only for complex multinational groups; for a single Thai entity these are over-spec, and several are actively **mis-scored** (treasury scored "No" when 2/4 legs are native).
- **Persistent procurement theme:** the source is a Fusion-biased competitive TOR. Wherever it demands a capability "natively / in core / without add-on," flag the spec-lock and, per the iCE second opinion, steer the buyer toward outcome-based requirements tied to real mission needs — locking a spec to one product invites a สตง. / competing-bidder challenge.
