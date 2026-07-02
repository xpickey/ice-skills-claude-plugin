# TOR Competitive KB — education — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "Records carry per-item confidence (high/medium/low) mapped from the source's [ความเชื่อมั่น] tag. 'high' = at least one official Oracle/NetSuite Help or vendor citation on file; 'medium' = mixed/partner-blog or verify-flagged sources; 'low' = no citation on file. No record here is invented. This KB is a COMPETITIVE Oracle Fusion selling aid — it deliberately foregrounds where Fusion wins. The iCE balanced second-opinion (many gaps are coverable by NetSuite first-party add-ons or native SuitePeople, or are over-spec / procurement-fairness risks) is preserved under each record's 'iCE caveat'. Do NOT strip the caveat when reusing wording in a live bid. Only two records in the master mapping carry the 'education' vertical — both are HCM/Talent, both rated iCE severity ต่ำ (Low) — so this file is deliberately short and both entries lean 'differentiate, do not over-spec'."
ams_review: "yearly — re-verify product positions"
---

> **How to use this file (Oracle Fusion sell-side).** Each section states where Oracle Fusion genuinely out-classes NetSuite for an **education** buyer (university, college, institute, training/e-learning body, or the education arm of a public-sector / non-profit foundation), then gives ready-to-paste TOR wording (TH + EN) engineered so a NetSuite-based bid scores **Partial** or **No**. Because iCE also resells NetSuite and answers to สตง.-style procurement scrutiny, every entry keeps the honest counter-view: locking a TOR to a single product's feature is a fairness risk, and the "gaps" here are talent-suite (ATS / LMS / succession) depth — an area where an education body typically bolts on a specialist system rather than mandating it inside the ERP. Both education records are rated **ต่ำ (Low)** severity by iCE, so weaponize them as **credibility differentiators** (unified single-model HCM, native performance) rather than as knock-out clauses; a "must be native, no third-party" mandate on LMS/ATS for a charitable or public education body reads as over-spec.

---

## GP-FUNC-19 — Talent: Performance / Learning / Recruiting [3-way: NS 1★ / Fusion 5★ / SAP 5★]

- **Capability (TH):** ชุดบริหารบุคลากร (Talent) — บริหารผลงาน (performance), การเรียนรู้ (learning/LMS), การสรรหา (recruiting/ATS)
- **Capability (EN):** Talent: performance, learning, recruiting (with succession as the implied fourth pillar)
- **Domain:** HCM · **iCE severity:** ต่ำ (Low) · **Gap Severity (source): Critical**
- **Oracle Fusion advantage (Standout):** The three-way benchmark scores NetSuite **1★** against Oracle Fusion **5★** and SAP S/4HANA (SuccessFactors) **5★**. Oracle Fusion HCM carries a complete, market-leading talent suite — recruiting (ATS), performance, learning (LMS) and succession — as first-party modules on a single HCM data model. For an education institution that runs large academic + administrative headcounts, recurring faculty/staff appraisal cycles, mandatory continuing-education and certification tracking, and structured recruitment intakes, Fusion delivers this end-to-end **without** stitching in external systems. NetSuite has no native LMS and no native succession planning, and its recruiting is only a basic Job Requisition record plus a Recruiting Reports bundle — not a full applicant-tracking system — so the learning and talent-pipeline pillars that an education buyer cares about are the ones where Fusion's edge is real.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีชุดบริหารบุคลากร (Talent) ครบวงจร ได้แก่ การสรรหาบุคลากรแบบ applicant tracking (ATS), การบริหารผลงาน (performance), ระบบการเรียนรู้/พัฒนาบุคลากร (learning management / LMS) และการวางแผนสืบทอดตำแหน่ง (succession) โดยเป็นโมดูลในตัว (native) บน data model เดียวกับ Core HR ไม่พึ่งพาระบบภายนอก"
- **TOR wording (English):** "The solution must provide a complete native Talent suite — applicant-tracking recruiting (ATS), performance management, learning management (LMS), and succession planning — as first-party modules on the same data model as Core HR, without reliance on external systems."
- **iCE caveat:** Over-stated as written and fairness-exposed. The "แทบไม่มี talent suite" claim behind the 1★ is not accurate: **SuitePeople Performance Management is native** (goals, reviews, check-in, Kudos) on the same data model as Core HR, and basic performance/learning tracking of academic and administrative staff runs fine on NetSuite native. The **genuine** gaps are full ATS, native LMS, and succession — but a university or training body almost always prefers a **specialist** best-of-breed LMS/ATS (e.g. Moodle/Canvas-class LMS, Greenhouse/Lever-class ATS) integrated via API, rather than a talent suite fused into the ERP. So mandating "native, no third-party" LMS/ATS/succession is **over-spec** for an education entity — and for a charitable / public-education foundation it invites a สตง. single-vendor-lock challenge. Weaponize instead on the **unified single data-model** angle (see TOR-HCM-02) where the story is honest, and let the buyer scope only the talent modules it truly needs.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] SuitePeople Performance Management (product page)
  - [KB] Netsuite-Administrator Guide — Performance Management (SuitePeople HR), Kudos (0.5788)
  - [KB] Netsuite-Employee Management — Recruiting Reports bundle/Job Requisition (0.4987; recruiting พื้นฐาน ไม่ใช่ ATS)

---

## TOR-HCM-02 — Talent Management (performance / learning / recruiting / succession)

- **Capability (TH):** ชุดบริหารบุคลากร (Talent) ครบวงจร — สรรหา (recruiting), บริหารผลงาน (performance), การเรียนรู้ (learning), การวางแผนสืบทอดตำแหน่ง (succession) บน data model เดียวกับ Core HR
- **Capability (EN):** End-to-end Talent suite — recruiting, performance, learning, and succession — on the same data model as Core HR
- **Domain:** HCM · **iCE severity:** ต่ำ (Low) · **Type: Functional · Priority: Important**
- **Oracle Fusion advantage (Standout):** This is the TOR-spec form of the talent gap, and the differentiator note is precise: **Oracle HCM centralizes the entire talent lifecycle on one data model** (a single record of the person flows through recruiting → performance → learning → succession), whereas SAP SuccessFactors stitches several clouds together and NetSuite simply does not offer the full suite. For an education body — where the same individual is a candidate, then a faculty/staff member on an appraisal cycle, then a learner completing mandatory development, then a succession candidate for a department head or programme-lead role — the "one unified person model" is a substantive Fusion advantage: no cross-system identity reconciliation, one analytics surface across the whole employee journey.
- **TOR wording to weaponize (ภาษาไทย):** "ระบบต้องมีชุดบริหารบุคลากร (Talent) ครบวงจร: สรรหา (recruiting), บริหารผลงาน (performance), การเรียนรู้ (learning) และการวางแผนสืบทอดตำแหน่ง (succession) บน data model เดียวกับ Core HR"
- **TOR wording (English):** "The solution shall provide an end-to-end Talent suite — recruiting, performance, learning, and succession — on the same data model as Core HR."
- **iCE caveat:** The source's "NetSuite = No" scoring is over-stated. **NetSuite passes the "single data model" test for Performance Management outright** — SuitePeople Performance runs natively on the same model as Core HR — so a blanket "No" is wrong; this criterion was really engineered to hit SuccessFactors' multi-cloud architecture, and NetSuite arguably meets it for the performance pillar. The parts NetSuite genuinely lacks natively are ATS, LMS and succession, which are connected via third-party. For a charitable / public education organisation, a fully-integrated ATS + LMS + succession suite is largely **over-spec**: the pragmatic path is to keep Core HR + performance native and connect only the specific talent modules actually required. Use the **unified data-model** clause as an honest differentiator, but avoid a "native + no third-party across all four pillars" lock, which is the fairness-exposed, single-vendor-tilted phrasing a สตง. reviewer or a rival bidder can challenge.
- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] SuitePeople Performance Management (product page)
  - [KB] Netsuite-Administrator Guide — Performance Management (SuitePeople HR), Kudos (0.5788)

---

## Sell-side summary (education)

- **Both education records are HCM/Talent and both rated iCE severity ต่ำ (Low).** There is no "สูง (High)" education-specific gap in the source mapping — the sharp, mission-critical Oracle Fusion wins (process/GMP manufacturing, quality/CAPA, data residency, GRC/SoD) live in other verticals, not here.
- **Weaponize honestly on the unified single data-model story** (recruiting → performance → learning → succession on one person record). This is Fusion's real, defensible edge for an education buyer and survives a fairness review.
- **Do not weaponize "native LMS/ATS/succession, no third-party."** Education institutions normally run best-of-breed LMS/ATS by choice; a native-only mandate is over-spec and, for a public / charitable education body, a สตง. single-vendor-lock risk.
- **Anti-hallucination note:** the source contains no education-only KB citations beyond the SuitePeople Performance and Recruiting Reports/Job Requisition references reproduced above; nothing here has been invented. Any position flagged for real-environment verification should be confirmed with the vendor before use in a live bid.
