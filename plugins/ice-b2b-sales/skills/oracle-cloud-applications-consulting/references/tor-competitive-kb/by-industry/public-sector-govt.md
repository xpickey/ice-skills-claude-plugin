# TOR Competitive KB — public-sector-govt — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "แต่ละ record ระบุ Confidence (high/medium/low) ตามว่ามี KB/official citation รองรับหรือไม่ — high = มีเอกสารทางการ Oracle/NetSuite Help หรือ KB ยืนยัน; medium = ผสม KB + secondary/partner source หรือมี flag [ต้อง verify]. ข้อมูลตั้งต้นเป็นชุดร่าง TOR เชิงแข่งขันที่เอียงเข้าหา Oracle Fusion — จึงถ่วงด้วย iCE second-opinion (over-spec / procurement fairness / สตง.) ทุก record เพื่อความสมดุลและลดความเสี่ยงถูกท้วงติงเชิงจัดซื้อ."
ams_review: "yearly — re-verify product positions"
industry_scope: "healthcare / blood-bank / non-profit foundation / public-sector / semi-governmental (generalized industry pattern — ไม่ระบุชื่อหน่วยงานเฉพาะ)"
product_angle: "Oracle Fusion — SELL side (Standout + Weaponize)"
---

## วิธีใช้เอกสารนี้ / How to use

เอกสารนี้ใช้ตอน iCE **ขาย Oracle Fusion** ให้กลุ่มลูกค้าภาครัฐ/กึ่งราชการ/องค์กรสาธารณกุศล (healthcare, blood-bank, non-profit foundation, public-sector) โดยสรุปไว้ 3 ชั้นต่อหนึ่งความสามารถ (capability):

1. **Oracle Fusion advantage (Standout)** — จุดที่ Fusion ชนะจริง เพื่อใช้วาง value narrative
2. **TOR wording to weaponize (TH + EN)** — ถ้อยคำสเปกที่แนะนำ ซึ่งออกแบบให้คู่แข่ง NetSuite ตอบได้เพียง Partial/No
3. **iCE caveat** — คำเตือน over-spec / ความเป็นธรรมเชิงจัดซื้อ (สตง. / ผู้ยื่นรายอื่น) ที่ทีมขายต้องรู้ก่อนดันสเปกจริง

> **หลักการกำกับ (จาก second_opinion.txt):** การล็อกสเปกให้ผูกกับฟีเจอร์เฉพาะผลิตภัณฑ์หนึ่งในงานจัดซื้อภาครัฐมีความเสี่ยงถูกท้วงติง (สตง. / ผู้ยื่นรายอื่น) — เมื่อดัน TOR ให้เขียนแบบ **อิงผลลัพธ์ (outcome-based)** ตามภารกิจจริงของหน่วยงาน และเลือกเน้นเฉพาะ record ที่มี business rationale หนักแน่นจริง (สูง/กลาง) ไม่ใช่เหมารวมทุกข้อ. record ที่ iCE ตีว่า "แทบไม่มีผล/over-spec" ให้ใช้เป็น talk-track เชิงคุณค่า ไม่แนะนำให้ใส่เป็น Mandatory เพราะเป็น over-spec ที่เห็นชัด.

**สรุประดับความรุนแรง (iCE severity) ของ 16 record ในเวอร์ทิคัลนี้:** สูง 11 · กลาง 3 · ต่ำ 1 · แทบไม่มีผล 1 — สัดส่วน "สูง" ที่มากสะท้อนว่าเวอร์ทิคัลภาครัฐโหลดหนักไปทางธีมการกำกับตรวจสอบ (data residency/sovereignty, SoD/GRC, e-Tax Invoice) ซึ่งเป็นแกน weaponize ที่ปลอดภัยและมี business rationale จริงที่สุด ส่วน record ต่ำ/แทบไม่มีผล (F-PRC-01, NF-SEC-02) ใช้เป็น value story เท่านั้น. ข้อควรระวัง: record "สูง" หลายตัวเป็นธีมเดียวกันที่ทับซ้อน (sovereignty 4 ตัว, SoD/GRC 4 ตัว) — ให้ยุบเป็น outcome เดียวต่อธีมเมื่อประกอบ TOR จริง เพื่อเลี่ยงภาพล็อกสเปก.

---

## F-PRC-01 — Strategic Sourcing (RFx / e-Auction)

- **Capability (TH):** การจัดหาเชิงกลยุทธ์ (RFx / e-Auction)
- **Capability (EN):** Strategic sourcing (RFx / e-auction)
- **Domain:** Procurement · **iCE severity:** ต่ำ

**Oracle Fusion advantage (Standout):** Oracle Procurement Cloud (Sourcing) มี sourcing engine ครบวงจรในตัว ทั้งการออกเอกสารสอบราคา (RFx) และการประมูลย้อนกลับแบบสด (live reverse e-auction) บนแพลตฟอร์มเดียวกับ Procure-to-Pay และ Supplier Management โดยไม่ต้องผูก network ภายนอก — จุดที่ NetSuite ไม่มีในตัวคือ live reverse e-auction (NetSuite มี RFQ + auto Purchase Contract แบบ native แต่ไม่มีการประมูลสดในตัว ERP).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการจัดหาเชิงกลยุทธ์ (strategic sourcing) ในตัว: การออกเอกสารสอบราคา (RFx) และการประมูลอิเล็กทรอนิกส์ (e-auction)

**TOR wording (English):** The solution must provide native strategic sourcing: RFx and e-auction.

**iCE caveat:** เป็น over-spec ที่ควรระวังในบริบทภาครัฐไทย — การจัดซื้อใช้เงินรัฐมักดำเนินการผ่านระบบ e-GP กลางของกรมบัญชีกลาง ไม่ใช่ e-auction ในตัว ERP; RFx เอง NetSuite รองรับ native และ auto-สร้าง Purchase Contract ต่อผู้ขายที่ได้รับรางวัลได้ ช่องว่างจริงจึงแคบเหลือเพียง live e-auction ซึ่งหน่วยงานแทบไม่ใช้ในตัว ERP. หากดันข้อนี้เป็น Mandatory เสี่ยงถูกมองว่าล็อกสเปกโดยไม่มี use case จริง — แนะนำใช้เป็น value story ไม่ใช่เกณฑ์ตัดสิทธิ์. [ต้อง verify ระเบียบพัสดุเฉพาะของหน่วยงาน]

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Purchasing and Receiving (0.66) — Request for Quotes feature / Vendor RFQ / Awarding a Request for Quote / Purchase Contracts
- [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (Award column; auto-creates Purchase Contract per awarded vendor; ไม่มี e-auction)
- [ต้อง verify] จัดซื้อใช้เงินรัฐในไทยมักผ่าน e-GP กลาง ไม่ใช่ e-auction ในตัว ERP; หน่วยงานมีระเบียบพัสดุของตนเอง

---

## F-PRJ-01 — Capital Project Costing / Grants

- **Capability (TH):** การคิดต้นทุนโครงการลงทุน / ทุนสนับสนุน (grants)
- **Capability (EN):** Capital project costing / grants
- **Domain:** Project · **iCE severity:** กลาง

**Oracle Fusion advantage (Standout):** Oracle Project Costing Cloud รองรับ capital/EPC project, การบริหารทุนสนับสนุน (grants), งานระหว่างก่อสร้าง (CWIP) และโครงสร้างงานหลายระดับ (deep multi-level WBS) แบบ native ในชั้นเดียว — ต่างจาก NetSuite ที่ฟังก์ชันเหล่านี้กระจายอยู่บน SuiteApp/โมดูลเสริมหลายชั้น (Job Costing ต้องให้ account rep เปิด; CWIP/CIP ตั้งสินทรัพย์ผ่าน Fixed Assets Management SuiteApp แบบ manual; grants/fund ใช้ NFP Financials SuiteApp โดยรายงานสำเร็จรูปอิง US-FASB ต้องปรับเข้ามาตรฐานไทย).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับการคิดต้นทุนโครงการลงทุน (capital project costing): การบริหารทุนสนับสนุน (grants), งานระหว่างก่อสร้าง (CWIP) และโครงสร้างงานหลายระดับ (deep WBS)

**TOR wording (English):** The solution must support capital project costing: grants, capital work-in-progress (CWIP) and deep multi-level WBS.

**iCE caveat:** แกนที่หน่วยงานภาครัฐ/สาธารณกุศลใช้จริง (grants/fund + capitalization ครุภัณฑ์/สิ่งก่อสร้าง) NetSuite ทำได้ผ่าน SuiteApp — จุดที่ Fusion เหนือกว่าจริงคือ deep multi-level WBS/EPC ซึ่งหน่วยงานแทบไม่ใช้ จึงเป็น over-spec มากกว่าช่องว่างที่กระทบงานจริง. หากดัน "deep WBS/EPC" เป็น Mandatory เสี่ยงถูกมองว่าล็อกสเปก — แนะนำเน้นถ้อยคำ grants/fund/capitalization (มี business rationale จริง) และวาง WBS เป็นเกณฑ์ให้คะแนน ไม่ใช่ตัดสิทธิ์.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Projects (0.61) — Job Costing/Project Budgeting โพสต์เข้า GL (ต้องให้ account rep เปิด)
- [KB] Netsuite-Non-Profit SuiteApps (0.66) — NFP Financials: Grant/Fund/Revenue Restriction
- [KB] Netsuite-Fixed Assets Management (0.53) — asset type 'project' (CIP) ตั้งสินทรัพย์เมื่อปิดโครงการ
- [WEB:netsuite.com] NetSuite Nonprofit — Fund Accounting & Grant Management (NFP Financials SuiteApp)
- [WEB:community.oracle.com] FAM — Tracking Construction in Progress (CIP) in Fixed Asset Management
- [WEB:netgain.tech] NetSuite Fixed Asset Roll Forward & CIP (NetAsset = third-party add-on)

---

## NF-ARC-02 — Deployment Options & Data Residency / Sovereignty

- **Capability (TH):** ทางเลือกการติดตั้ง / ถิ่นที่อยู่ของข้อมูล (data residency)
- **Capability (EN):** Deployment & data residency options
- **Domain:** Technical · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle มีเส้นทางการติดตั้งที่ยืดหยุ่นและครอบคลุมถิ่นที่อยู่ของข้อมูล — Cloud@Customer, regional data center, private options และเส้นทาง in-country/sovereign (AIS Cloud / Oracle Alloy ในไทย, EU Sovereign Cloud) — ในขณะที่ NetSuite เป็น pure multi-tenant SaaS ล้วน ไม่มี on-prem/private/Cloud@Customer และไม่มี data center ในไทย อีกทั้งยังไม่รองรับ Oracle EU Sovereign Cloud (สถานะ Q1/2026). นี่เป็นช่องว่างเชิงสถาปัตยกรรมที่ NetSuite ปิดด้วย SuiteApp/custom ไม่ได้เลย.

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีทางเลือกการติดตั้งที่ยืดหยุ่น รวมถึงตัวเลือกเก็บข้อมูลภายในประเทศ (data residency) หรือแบบ dedicated / Cloud@Customer

**TOR wording (English):** The solution must offer flexible deployment options including in-country data residency or a dedicated / Cloud@Customer option.

**iCE caveat:** นี่คือ record ที่ **weaponize ได้อย่างชอบธรรมที่สุด** สำหรับลูกค้าภาครัฐ/สาธารณสุขที่ถือข้อมูลอ่อนไหว (ข้อมูลสุขภาพผู้ป่วย/ผู้บริจาค) เพราะเป็นช่องว่างจริงที่ปิดไม่ได้ และแนบภารกิจ/การกำกับตรวจสอบภาครัฐโดยตรง. แต่ต้องเขียนอย่างระวัง — PDPA ไทย **ไม่บังคับ** เก็บข้อมูลในประเทศ; on-prem/private เป็น over-spec เมื่อหน่วยงานเลือกแนวทาง SaaS อยู่แล้ว. วางกรอบให้เป็น **การตัดสินใจ/ยอมรับความเสี่ยงระดับบอร์ดเรื่อง sovereignty** (นโยบาย ไม่ใช่ข้อบังคับกฎหมาย) แล้วให้ TOR ขอ "ทางเลือก in-country/sovereign residency" เป็นเกณฑ์คุณค่า — ปลอดภัยกว่าการเขียนบังคับ on-prem ตรง ๆ. [ต้อง verify สถานะ Oracle EU Sovereign Cloud + in-country roadmap ของทั้งสองค่าย]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] What is NetSuite ERP (multi-tenant SaaS, no on-prem)
- [WEB:sota.io] NetSuite NOT available on Oracle EU Sovereign Cloud as of Q1 2026 [ต้อง verify]
- [WEB:oracle.com] AIS Cloud / Oracle Alloy — in-country Thai cloud (2024)
- [KB] NSTWP — multi-tenant shared service (0.541)

---

## NF-SEC-01 — Automated Segregation of Duties (SoD) & Access Governance

- **Capability (TH):** การแบ่งแยกหน้าที่ (SoD) แบบอัตโนมัติ + การกำกับดูแลสิทธิ์เข้าถึง
- **Capability (EN):** Automated SoD & access governance
- **Domain:** Technical · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle Risk Management Cloud (Advanced Access Controls) มี automated Segregation of Duties + access governance + continuous controls monitoring พร้อม ruleset สำเร็จรูปจำนวนมากในตัว — ในขณะที่ NetSuite มี role-based security ละเอียดและเครื่องมือตรวจสิทธิ์ (Use Searches to Audit Roles, Show Role Permission Differences, Login Audit Trail) แต่ **ไม่มี engine SoD อัตโนมัติ/continuous controls monitoring สำเร็จรูปแบบ native** ต้องเสริม SuiteApp certified (Fastpath Assure, Netwrix Strongpoint, SafePaaS).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการแบ่งแยกหน้าที่ (segregation of duties) แบบอัตโนมัติ พร้อมการกำกับดูแลสิทธิ์เข้าถึง (access governance) และการบริหารความเสี่ยง (risk management) ในตัว

**TOR wording (English):** The solution must provide automated segregation of duties (SoD) with access governance and risk management natively.

**iCE caveat:** ช่องว่าง "engine SoD อัตโนมัติ native" มีจริงและ Oracle เหนือกว่าชัดเจน — และ SoD แนบการกำกับภาครัฐโดยตรง (การรับบริจาค/จัดซื้อจัดจ้างอยู่ภายใต้การตรวจของ สตง.) จึงเป็น weaponize ที่มี business rationale หนักแน่น. แต่พึงระวัง 2 จุด: (1) ถ้อยคำ "ในตัว (native)" คือส่วนที่เป็น over-spec — SoD ที่หน่วยงานต้องการจริงปิดได้ด้วย NetSuite native (detective) + SuiteApp certified ที่ต้นทุนไม่สูง; (2) GRC engine อัตโนมัติระดับ enterprise เต็มรูปเกินความจำเป็นขององค์กรประเทศเดียว. แนะนำเน้น outcome ("ต้องแสดง automated SoD + access governance ที่ตรวจสอบได้") มากกว่าบังคับคำว่า native เพื่อลดความเสี่ยงถูกท้วงเชิงจัดซื้อ.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
- [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review/terminated-user revocation
- [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + ruleset สำเร็จรูปจำนวนมาก
- [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
- [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## NF-SEC-02 — Industry / Government Accreditations

- **Capability (TH):** การรับรองด้านอุตสาหกรรม / ภาครัฐ
- **Capability (EN):** Industry / government accreditations
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**Oracle Fusion advantage (Standout):** Oracle (OCI/Fusion) มี industry solutions + การรับรองภาครัฐกว้างกว่า เช่น FedRAMP / government-cloud / sovereign region — ในขณะที่ NetSuite เป็น pure multi-tenant SaaS จึงไม่มี accreditation ภาครัฐกลุ่มนี้ (แต่ถือใบรับรองสากลครบ: SOC 1/SOC 2 Type II, ISO 27001/27018/42001, PCI DSS Level 1 Service Provider + PCI SSF).

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องแสดงรายการการรับรอง (accreditation) ด้านอุตสาหกรรมและภาครัฐ/หน่วยงานกำกับ ที่เกี่ยวข้องกับธุรกิจของหน่วยงาน

**TOR wording (English):** The bidder must provide a list of relevant industry and government/regulatory accreditations applicable to the organization's business.

**iCE caveat:** **over-spec ที่เอียงเข้าหา Oracle อย่างชัดเจน — ใช้ด้วยความระมัดระวังสูง.** การรับรองภาครัฐที่ Oracle เหนือกว่า (FedRAMP/IL/sovereign) เป็นการรับรองของรัฐบาล/กลาโหมสหรัฐฯ **ไม่ใช่ข้อกำหนดของหน่วยงานไทย**; ใบรับรองที่เกี่ยวข้องจริง (ISO 27001, SOC, PCI สำหรับช่องทางรับบริจาคบัตรเครดิต) NetSuite มีครบ. การเขียน TOR ให้ต้องมี "accreditation ภาครัฐกว้าง" จึงเสี่ยงถูกท้วงติงเรื่องความเป็นธรรม. ถ้อยคำที่แนะนำข้างต้นตั้งใจเขียนแบบเปิด (ให้ระบุ accreditation ที่ "เกี่ยวข้องกับธุรกิจของหน่วยงาน") ซึ่งเป็นกลางและปลอดภัยกว่าการล็อกชื่อ certification เฉพาะของสหรัฐฯ.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Application and Operational Security — SOC 1/2, ISO 27001/27018/42001, PCI DSS, PCI SSF
- [WEB:houseblend.io] NetSuite Audit Readiness: SOC 1, SOC 2 & ISO 27001 Guide
- [WEB:stratusgreen.com] NetSuite PCI Compliance — Level 1 Service Provider

---

## GP-FUNC-11 — Contract Lifecycle Management (CLM)

- **Capability (TH):** การบริหารสัญญาแบบครบวงจร (CLM)
- **Capability (EN):** Contract Lifecycle Management (CLM)
- **Domain:** Procurement · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle Fusion มี CLM ในตัว (clause library, authoring, obligation management) — ในขณะที่ NetSuite **ไม่มีโมดูล CLM เฉพาะในตัวเลย**: 'Managing Contracts' native เป็นสัญญาฝั่งขาย/ต่ออายุเท่านั้น ไม่มี clause library, authoring, redline หรือ obligation management; ฝั่งจัดซื้อมีเพียง Purchase Contract + เก็บไฟล์ใน File Cabinet. CLM เต็มรูปของ NetSuite ต้องพึ่ง SuiteApp พาร์ทเนอร์ (Gatekeeper, Conga/Malbek) ทั้งหมด. (เปรียบเทียบ 3 ค่าย: NetSuite 1★ / Oracle Fusion 4★ / SAP S/4HANA 4★ — Gap Severity: Med)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการบริหารสัญญาแบบครบวงจร (contract lifecycle management) ในตัว รองรับคลังข้อสัญญา (clause library), การร่างและปรับแก้ (authoring/redline), การติดตามภาระผูกพัน (obligation management) และการแจ้งเตือนต่ออายุ พร้อม audit trail

**TOR wording (English):** The solution must provide native contract lifecycle management (CLM) with a clause library, authoring/redline, obligation management, renewal alerts and an audit trail.

**iCE caveat:** ความต้องการจริงของหน่วยงานภาครัฐ/สาธารณกุศล (คลังสัญญา + แจ้งเตือนต่ออายุ + audit trail — เพราะงานจัดซื้อ/สัญญาทุนสนับสนุนอยู่ใต้การตรวจ สตง.) ทำได้ด้วย NetSuite native + SuiteApp ราคาประหยัด ไม่ใช่ blocker. ส่วน CLM ระดับ enterprise (AI redline / clause library เต็มรูป) เป็น over-spec — iCE ตี gap_severity = "Med" ไม่ใช่ Critical. แนะนำ weaponize เฉพาะแกน "คลังสัญญา + obligation + audit trail" (มี rationale จริง) และวาง AI-redline/clause-library เต็มรูปเป็นเกณฑ์ให้คะแนน ไม่ใช่ Mandatory ตัดสิทธิ์.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Software Vertical Contract Renewals (0.66) + Netsuite-Sales Orders and Cash Sales (0.63) — เป็น contract ฝั่งขาย/ต่ออายุเท่านั้น
- [WEB:docs.oracle.com] NetSuite Applications Suite — Managing Contracts (จำกัดที่ sales renewal lifecycle; ไม่มี clause library/authoring/obligation)
- [WEB:suiteapp.com] Gatekeeper Contract Management & Vendor Portal — CLM สำหรับ NetSuite เป็น SuiteApp พาร์ทเนอร์ (ยืนยันมีจริง)

---

## GP-FUNC-16 — Statutory Localization, Tax Engine & e-Invoicing (e-Tax Invoice TH)

- **Capability (TH):** Tax engine & localization ตามกฎหมายแต่ละประเทศ (รวม e-Tax Invoice ไทย)
- **Capability (EN):** Statutory localization, tax engine & e-invoicing
- **Domain:** Finance · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle Fusion มี global tax engine + localization/e-invoice ที่ครอบคลุมกว้างสุด และรองรับมาตรฐาน e-invoicing ตามข้อกำหนดของแต่ละประเทศ — ในขณะที่ NetSuite SuiteTax + SEA Localization รองรับ VAT/ภ.พ.30/ใบกำกับภาษี-เครดิตโน้ตตามรูปแบบกรมสรรพากรครบสำหรับไทย แต่ **ไม่มีมาตรฐาน e-Tax Invoice ไทยแบบ native** — Electronic Invoicing SuiteApp เป็นเพียงกรอบออก XML/JSON ต้องทำ template เอง/ใช้พาร์ทเนอร์เพื่อส่งกรมสรรพากร. (เปรียบเทียบ 3 ค่าย: NetSuite 2★ / Oracle Fusion 4★ / SAP S/4HANA 5★ — Gap Severity: Critical)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี localization และ statutory/tax compliance ในตัวสำหรับทุกประเทศที่องค์กรดำเนินงาน รวมถึง e-invoicing/e-tax ตามข้อกำหนดของแต่ละประเทศ (เช่น e-Tax Invoice & e-Receipt ตามกรมสรรพากรไทย) โดยไม่ต้องพึ่ง third-party add-on

**TOR wording (English):** The solution must provide built-in localization and statutory/tax compliance for every country of operation, including country-specific e-invoicing/e-tax (e.g. Thai e-Tax Invoice & e-Receipt), without reliance on third-party add-ons.

**iCE caveat:** ช่องว่างจริงและ weaponize ได้คือ **e-Tax Invoice/e-Receipt XML ส่งกรมสรรพากร** ซึ่งเป็นข้อบังคับตามกฎหมายไทยและ NetSuite ยังไม่มี native (ต้อง custom/partner) — มี business rationale หนักแน่นสำหรับทุกหน่วยที่ออกเอกสารภาษี. แต่พึงระวัง 2 จุด over-spec: (1) เงื่อนไข "ทุกประเทศ" ไม่เกี่ยวเพราะหน่วยงานอยู่ไทยประเทศเดียว — statutory ไทยพื้นฐาน NetSuite รองรับครบ; (2) วลี "โดยไม่พึ่ง third-party add-on" คลาดเคลื่อน เพราะ SEA Localization + International Tax Reports เป็น free managed bundle **ของ NetSuite เอง ไม่ใช่ third-party**. แนะนำ weaponize เฉพาะ "e-Tax Invoice ไทย native" (จุดจริง) และตัดเงื่อนไข "ทุกประเทศ" ออกเพื่อลดภาพล็อกสเปก.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Country Specific Features (0.7242, SuiteTax Reports/VAT)
- [WEB:docs.oracle.com] Thailand Tax Invoice & Credit Memo Templates (SEA Localization, P.P.30)
- [WEB:docs.oracle.com] Electronic Invoicing Overview (กรอบ XML/JSON ไม่มี native มาตรฐานไทย)

---

## GP-FUNC-21 — Enterprise PPM, Project Costing & Grants

- **Capability (TH):** PPM ระดับองค์กร / ต้นทุนโครงการ / ทุนวิจัย
- **Capability (EN):** Enterprise PPM, project costing & grants
- **Domain:** Project · **iCE severity:** กลาง

**Oracle Fusion advantage (Standout):** Oracle PPM Cloud นำหน้าเรื่อง enterprise project costing/grants ระดับองค์กร รวมถึงตารางงานระดับ Primavera สำหรับโครงการสเกลใหญ่ — ในขณะที่ NetSuite Project Management โพสต์ต้นทุนเข้า GL พร้อม budget vs actual ได้ และทำทุนวิจัย/grants ผ่าน NFP Financials (SuiteApp) แต่ด้อยกว่าใน enterprise PPM/project costing สเกลใหญ่และ deep WBS. (เปรียบเทียบ 3 ค่าย: NetSuite 3★ / Oracle Fusion 5★ / SAP S/4HANA 4★ — Gap Severity: High)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการบริหารโครงการระดับองค์กร (Enterprise PPM) รองรับ project costing, budget vs actual, capitalization, grants และการเชื่อมโยงต้นทุนโครงการเข้ากับบัญชีแยกประเภทอัตโนมัติ พร้อมโครงสร้างงานหลายระดับ (multi-level WBS)

**TOR wording (English):** The solution must provide Enterprise PPM with project costing, budget vs actual, capitalization, grants, automatic posting of project costs to the general ledger, and multi-level WBS.

**iCE caveat:** ความต้องการจริงของหน่วยงานภาครัฐ/สาธารณกุศลอยู่ในระดับที่ NetSuite + Nonprofit edition รองรับครบ (project costing / grants / fund accounting) — ส่วนที่ NetSuite แพ้คือ enterprise PPM/Primavera tier-1 ซึ่งหน่วยงานแทบไม่ใช้ จึงเป็น over-spec/ล็อกสเปก ไม่ใช่ช่องว่างที่กระทบงานจริง. พึงรู้ต้นทุนฝั่ง NetSuite: NFP Financials SuiteApp (add-on) + งานปรับรายงานสำเร็จรูป US-FASB เข้ามาตรฐานไทย. แนะนำเน้น grants/fund/capitalization (rationale จริง) และวาง PPM tier-1/Primavera เป็นเกณฑ์คะแนน ไม่ใช่ Mandatory.

**Confidence:** medium

**หลักฐาน / Citation:**
- [KB] Netsuite-Projects (0.61) — native project costing/job costing/budgeting
- [KB] Netsuite-Non-Profit SuiteApps (0.66) — Grant Management & Fund Accounting
- [WEB:netsuite.com] NetSuite Nonprofit ERP — Grant Management & Fund Accounting
- [WEB:docs.oracle.com/netsuite] Non-Profit Financial Management (NetSuite Help)

---

## GP-FUNC-27 — Governance, Risk & Compliance (GRC) / SoD

- **Capability (TH):** กำกับ ความเสี่ยง การควบคุม / SoD
- **Capability (EN):** Governance, Risk & Compliance (GRC) / SoD
- **Domain:** GRC · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle Risk Management Cloud มี automated SoD + continuous controls monitoring แบบ native — ในขณะที่ GRC ในตัวของ NetSuite เป็น umbrella ของ native controls (role/permission + audit trail + approval workflow + saved search/role audit) + partner SuiteApp ไม่ใช่ engine automated SoD/continuous controls monitoring แบบ native. NetSuite ปิด gap นี้ด้วย SuiteApp (Fastpath Assure, Netwrix Strongpoint, SafePaaS). (เปรียบเทียบ 3 ค่าย: NetSuite 2★ / Oracle Fusion 5★ / SAP S/4HANA 5★ — Gap Severity: High)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการกำกับ ความเสี่ยง และการควบคุม (GRC) ในตัว รองรับการแบ่งแยกหน้าที่ (SoD) แบบอัตโนมัติและ continuous controls monitoring

**TOR wording (English):** The solution must provide native Governance, Risk & Compliance (GRC) with automated Segregation of Duties (SoD) and continuous controls monitoring.

**iCE caveat:** gap automated SoD/CCM เทียบ Oracle/SAP มีจริง และแนบการกำกับภาครัฐ (องค์กรอยู่ใต้การตรวจของ สตง.) จึงมี rationale — แต่ iCE ตีเรตติ้ง NetSuite ที่ 2★ (Partial) ว่า "สมเหตุผล" เพราะ NetSuite มีเครื่องมือ audit role + audit trail native และ ecosystem SoD ที่ certified. ส่วน continuous controls monitoring ระดับ enterprise เต็มรูปไม่ใช่ความจำเป็นพื้นฐานขององค์กรประเทศเดียว = over-spec. **หมายเหตุ:** record นี้ทับซ้อนกับ NF-SEC-01 และ TOR-TECH-05 — เมื่อประกอบ TOR ให้รวมเป็นข้อเดียวเชิง outcome เพื่อเลี่ยงการดันสเปก SoD ซ้ำหลายข้อ (จะยิ่งดูล็อกสเปก).

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.695/0.6678) — role permissions + audit role searches
- [WEB:netsuite.com] What is NetSuite Governance, Risk & Compliance? — GRC = native controls + partner SuiteApp (ไม่ใช่ SoD engine native)
- [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring
- [WEB:netwrix.com] NetSuite Segregation of Duties (Strongpoint) — alert on SoD conflicts
- [WEB:suiteapp.com] Fastpath Assure for NetSuite

---

## GP-TECH-08 — Data Residency, Sovereignty & Region Count

- **Capability (TH):** ถิ่นที่อยู่ข้อมูล / sovereign / จำนวน region
- **Capability (EN):** Data residency, sovereignty & region count
- **Domain:** Technical · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle มี public + government + sovereign regions มากสุด เหมาะกับ TOR ภาครัฐ/ข้อมูลในประเทศ และมีเส้นทาง sovereign/in-country (EU Sovereign Cloud, AIS Cloud/Oracle Alloy ไทย) — ในขณะที่ NetSuite ให้ data residency ผ่าน data center หลายภูมิภาค (EU/NA/APAC) แต่ **ไม่มี DC ในประเทศไทยและไม่รองรับ EU Sovereign Cloud** จุดต่างนี้ไม่สมมาตร. (เปรียบเทียบ 3 ค่าย: NetSuite 2★ / Oracle Fusion 5★ / SAP S/4HANA 4★ — Gap Severity: High)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องรองรับข้อกำหนดถิ่นที่อยู่ของข้อมูล (data residency) และ data sovereignty โดยผู้เสนอราคาต้องระบุจำนวนและตำแหน่ง region (public / government / sovereign / in-country) ที่รองรับ

**TOR wording (English):** The solution must meet data residency and data-sovereignty requirements; the bidder must state the number and location of supported regions (public / government / sovereign / in-country).

**iCE caveat:** เป็นแกน weaponize ที่ชอบธรรมสำหรับข้อมูลสุขภาพ/ผู้บริจาคภายใต้การกำกับภาครัฐ — แต่ต้องรู้ 2 ข้อถ่วงดุล: (1) PDPA ไทย **ไม่บังคับ** data localization และ Oracle Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน — ข้อได้เปรียบจริงอยู่ที่เส้นทาง sovereign/in-country ของ Oracle (Alloy/AIS) ไม่ใช่ public region; (2) record นี้ทับซ้อนกับ NF-ARC-02 และ TOR-TECH-04 — รวมเป็นข้อเดียว. วางกรอบเป็นประเด็นนโยบาย sovereignty ระดับบอร์ด แล้วขอให้ "ระบุทางเลือก" (outcome-based) ปลอดภัยกว่าบังคับ in-country ตรง ๆ. [ต้อง verify สถานะ sovereign roadmap ทั้งสองค่าย]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — EU DCs (Amsterdam/Frankfurt/London/Newport), no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:bakermckenzie.com] Thailand cross-border data transfer — no localization mandate
- [WEB:oracle.com] AIS Cloud / Oracle Alloy Thailand (2024)

---

## GP-TECH-11 — Fine-grained Access & Automated SoD Controls

- **Capability (TH):** ควบคุมสิทธิ์ละเอียด / SoD อัตโนมัติ
- **Capability (EN):** Fine-grained access & automated SoD controls
- **Domain:** Technical · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** Oracle Risk Management Cloud มี automated SoD + continuous controls monitoring ในตัว — ในขณะที่ NetSuite มี fine-grained access (permission view/create/edit/full ต่อ record/feature, 636+ permissions) + Login Audit Trail + role-diff/audit search + 2FA/TBA แต่ **"automated SoD controls" ระดับ ruleset อัตโนมัติ + continuous monitoring ต้องใช้ SuiteApp** (Fastpath Assure, Netwrix Strongpoint, SafePaaS). (เปรียบเทียบ 3 ค่าย: NetSuite 2★ / Oracle Fusion 5★ / SAP S/4HANA 5★ — Gap Severity: High)

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการควบคุมสิทธิ์การเข้าถึงแบบละเอียด (fine-grained access control) พร้อมการตรวจสอบการแบ่งแยกหน้าที่ (SoD) แบบอัตโนมัติ (ruleset) และ continuous controls monitoring ในตัว

**TOR wording (English):** The solution must provide fine-grained access control with automated (ruleset-based) Segregation of Duties checks and built-in continuous controls monitoring.

**iCE caveat:** Oracle Risk Mgmt/SAP GRC มี automated SoD/CCM ที่ NetSuite ไม่มี native — จุดนี้จริง. แต่ถ้อยคำ "NetSuite role-based พื้นฐาน" มองข้ามว่าการคุมสิทธิ์ของ NetSuite ละเอียด (636+ permission) และ audit ได้ และ gap ปิดได้ด้วย add-on. fine-grained access เป็นความจำเป็นจริง (weaponize ได้) แต่ automated continuous SoD เป็นส่วนเสริมที่เกินความจำเป็นสำหรับสเกลองค์กรประเทศเดียว. **หมายเหตุ:** ทับซ้อนกับ NF-SEC-01 / GP-FUNC-27 / TOR-TECH-05 — อย่าดันซ้ำหลายข้อใน TOR เดียว.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Managing Users & Roles (0.6691) — granular permission structure (636+ permissions)
- [KB] Netsuite-Authentication Guide — 2FA / token-based auth; Netsuite-Administrator Guide (0.6642) — password policy + SoD monitoring example (PO created by AP)
- [WEB:oracle.com] Oracle Advanced Access Controls — continuous SoD monitoring
- [WEB:mysuite.tech] NetSuite SoD native vs add-on boundary (detective not preventive)

---

## GP-STANDOUT-09 — Fusion Standout: Broad Public + Sovereign Cloud Regions

- **Capability (TH):** region / sovereign cloud หลากหลาย
- **Capability (EN):** Broad public + sovereign cloud regions
- **Domain:** Technical (Non-Functional standout) · **iCE severity:** สูง

**Oracle Fusion advantage (Standout):** OCI มี public + government + sovereign regions มากสุด เหมาะกับ TOR ภาครัฐ/ข้อมูลในประเทศ — เป็นข้อได้เปรียบ Fusion/OCI ที่ **legitimate** (iCE ระบุเองว่า "อาจสำคัญจริง"). ตัวเลือก data center ของ NetSuite จำกัดและไม่มี government/sovereign region ในไทย.

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องแสดงความครอบคลุมของ cloud region (public / government / sovereign) และตัวเลือก in-country region ที่รองรับข้อกำหนด data sovereignty ของหน่วยงานภาครัฐ

**TOR wording (English):** The bidder must demonstrate cloud region coverage (public / government / sovereign) and in-country region options meeting the public-sector organization's data-sovereignty requirements.

**iCE caveat:** iCE จัดข้อนี้เป็นข้อได้เปรียบ Fusion ที่ **ควร verify ไม่ใช่ปัดทิ้ง** — หากหน่วยงานมีข้อกำหนด data residency ในไทย (ข้อมูลสุขภาพ/ผู้บริจาคภายใต้ PDPA) เรื่อง region/sovereign cloud อาจเป็น blocker จริงต่อ NetSuite. แต่ต้องยืนยันตัวเลือก data center ในประเทศของทั้งสองค่ายก่อนตัดสิน (PDPA ไม่บังคับ localization; public region มาตรฐานไม่มีในไทยทั้งคู่). record นี้ทับซ้อนกับ NF-ARC-02 / GP-TECH-08 / TOR-TECH-04 — ใช้ร่วมกันเป็นแกน sovereignty เดียว. [ต้อง verify]

**Confidence:** medium

**หลักฐาน / Citation:**
- vs NetSuite: NetSuite data center จำกัด — [อ้างอิงร่วม GP-TECH-08: WEB:netsuite.com NetSuite Data Center datasheet, no Thai DC]
- vs SAP: SAP มี region แต่ตัวเลือก sovereign น้อยกว่า
- Why Fusion wins: OCI มี public+government+sovereign regions มากสุด เหมาะ TOR ภาครัฐ/ข้อมูลในประเทศ
- [ต้อง verify] ตัวเลือก data center ในประเทศ/sovereign ของทั้งสองค่ายก่อนตัดสิน (record นี้เป็น STANDOUT-level ในแหล่งข้อมูล ไม่มี citation แยกเฉพาะ — confidence จึงเป็น medium และผูกหลักฐานร่วมกับ GP-TECH-08)

---

## TOR-FIN-03 — TOR Spec: Statutory Tax / e-Invoicing (e-Tax Invoice TH)

- **Capability (TH):** localization + statutory/tax compliance + e-invoicing/e-tax ตามข้อกำหนดแต่ละประเทศ
- **Capability (EN):** Statutory tax / e-invoicing (Thai e-Tax Invoice)
- **Domain:** Finance · **iCE severity:** สูง · **NetSuite ตอบได้?:** No (ตามร่างเดิม) · **Priority:** Mandatory

**Oracle Fusion advantage (Standout):** SuiteTax ครอบคลุมประเทศน้อยกว่า; SAP/Oracle ครอบคลุม localization/e-invoice กว้างสุด. Oracle Fusion จึงชนะเรื่องความกว้างของประเทศและมาตรฐาน e-invoicing — โดยจุดที่ NetSuite ขาดจริงคือ e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากรที่ยังไม่มี native (Electronic Invoicing เป็นกรอบเปล่า ต้อง custom/partner).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมี localization และ statutory/tax compliance ในตัวสำหรับทุกประเทศที่องค์กรดำเนินงาน รวมถึง e-invoicing/e-tax ตามข้อกำหนดของแต่ละประเทศ โดยไม่ต้องพึ่ง third-party add-on

**TOR wording (English):** The solution shall provide built-in localization and statutory/tax compliance for every country of operation, including country-specific e-invoicing/e-tax, without reliance on third-party add-ons.

**iCE caveat:** ร่างเดิมให้ "No" ซึ่ง iCE ชี้ว่า **เกินจริงสำหรับ scope ไทย** — NetSuite รองรับ statutory ไทย (VAT/ภ.พ.30/ใบกำกับภาษี) ผ่าน SEA Localization + International Tax Reports ซึ่งเป็น **free managed bundle ของ NetSuite เอง ไม่ใช่ third-party**; ความจริงคือ Partial ไม่ใช่ No. ช่องว่างจริงที่ weaponize ได้เหลือเฉพาะ **e-Tax Invoice XML** (custom/partner). เงื่อนไข "ทุกประเทศ + ไม่พึ่ง add-on" เป็นการล็อกสเปก (หน่วยงานอยู่ไทยประเทศเดียว) — แนะนำเขียนเจาะจงที่ e-Tax Invoice ไทย native และตัดเงื่อนไข "ทุกประเทศ"/"ไม่พึ่ง third-party" ออกเพื่อเลี่ยงข้อครหาเชิงจัดซื้อ.

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:docs.oracle.com] Southeast Asia Localization (free managed first-party bundle)
- [WEB:docs.oracle.com] Thailand Invoicing Features / Electronic Invoicing Overview (กรอบ ไม่มี native ไทย)
- [KB] Netsuite-Country Specific Features (0.7209)

---

## TOR-PPM-01 — TOR Spec: Enterprise PPM, Project Costing & Grants

- **Capability (TH):** การบริหารโครงการระดับองค์กร (Enterprise PPM) + project costing/grants
- **Capability (EN):** Enterprise PPM, project costing & grants
- **Domain:** Project · **iCE severity:** กลาง · **NetSuite ตอบได้?:** Partial · **Priority:** Important

**Oracle Fusion advantage (Standout):** NetSuite SuiteProjects ดีสำหรับงาน services; Oracle PPM Cloud เหนือกว่าใน project costing/grants ระดับองค์กรและ deep WBS/EPC-grade — จุดที่ NetSuite ไม่มี native คือ Enterprise PPM ระดับ deep WBS/EPC (งานหลักอย่าง project costing / budget vs actual / auto-post GL ทำได้ แต่ Job Costing ต้องให้ account rep เปิด, capitalization CIP มักพึ่ง third-party NetAsset, grants/fund ต้องซื้อ NFP Financials SuiteApp).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการบริหารโครงการระดับองค์กร (Enterprise PPM) รองรับ project costing, budget vs actual, capitalization, grants และการเชื่อมโยงต้นทุนโครงการเข้ากับบัญชีแยกประเภทอัตโนมัติ

**TOR wording (English):** The solution shall provide Enterprise PPM with project costing, budget vs actual, capitalization, grants, and automatic posting of project costs to the general ledger.

**iCE caveat:** ติด Partial เพราะ deep WBS/EPC-grade เท่านั้น — ฟังก์ชันหลักของ TOR (costing, budget vs actual, capitalization, grants) NetSuite ทำได้จริงผ่าน SuiteApp; grants/fund + capitalization มี rationale จริงต่อภารกิจรับบริจาค/กองทุน ส่วน enterprise PPM tier-1/Primavera เป็น over-spec. แนะนำ weaponize เฉพาะ grants/fund + capitalization และวาง deep WBS/PPM tier-1 เป็นเกณฑ์คะแนน ไม่ใช่ Mandatory ตัดสิทธิ์.

**Confidence:** high

**หลักฐาน / Citation:**
- [KB] Netsuite-Projects (0.61) — native project costing/job costing/budgeting
- [KB] Netsuite-Non-Profit SuiteApps (0.66) — NFP Financials Grant/Fund
- [WEB:netsuite.com] NetSuite Nonprofit — Fund Accounting & Grant Management (NFP Financials)
- [WEB:community.oracle.com] FAM CIP — capitalize project costs to fixed asset
- [WEB:netgain.tech] CIP buildup via NetAsset (third-party add-on)

---

## TOR-TECH-04 — TOR Spec: Deployment / Data Residency Options

- **Capability (TH):** ทางเลือกการติดตั้ง (public / private / sovereign / in-country) + data residency
- **Capability (EN):** Deployment / data residency options
- **Domain:** Technical · **iCE severity:** สูง · **NetSuite ตอบได้?:** Partial · **Priority:** Mandatory

**Oracle Fusion advantage (Standout):** NetSuite = public multi-tenant, region จำกัด; Oracle OCI มี sovereign/gov regions เด่น (SAP private ผ่าน RISE). Oracle มีเส้นทาง in-country (AIS Cloud/Oracle Alloy ไทย) ที่ NetSuite **ยังไม่มี** — NetSuite เป็น public multi-tenant SaaS เท่านั้น ไม่มี DC ในไทย, ไม่มี private/sovereign region และไม่อยู่บน EU Sovereign Cloud; เป็นช่องว่างที่เพิ่ม in-country/sovereign region ให้ NetSuite ไม่ได้เชิงสถาปัตยกรรม.

**TOR wording to weaponize (ภาษาไทย):** ผู้เสนอราคาต้องระบุทางเลือกการติดตั้ง (public cloud, private cloud, sovereign/in-country region) และตำแหน่ง data center ที่รองรับข้อกำหนดถิ่นที่อยู่ของข้อมูล (data residency) ของหน่วยงาน

**TOR wording (English):** The bidder shall state available deployment options (public, private, sovereign/in-country region) and data-center locations meeting the organization's data-residency requirements.

**iCE caveat:** ข้อกำหนดในร่างเป็นเพียง "ระบุทางเลือก" ซึ่ง NetSuite ทำได้ (จึงเป็น Partial ไม่ใช่ตก) และ in-country ไทยไม่ใช่ข้อบังคับ PDPA — การตี "region จำกัด → Partial" ต่ำกว่าจริงเล็กน้อย. แต่ข้อนี้แตะข้อมูลสุขภาพผู้ป่วย/ผู้บริจาคซึ่งเป็น data class อ่อนไหวสูงและอยู่ใต้การกำกับภาครัฐ — หากหน่วยงานกำหนด in-country/sovereign residency เป็นเงื่อนไข NetSuite เสียเปรียบและปิด gap ไม่ได้. **นี่คือถ้อยคำ weaponize ที่ปลอดภัยที่สุดในกลุ่ม sovereignty** เพราะขอเพียง "ระบุทางเลือก" (outcome-based) ไม่บังคับ on-prem ตรง ๆ จึงถูกท้วงติงยาก. [ต้อง verify in-country/sovereign roadmap]

**Confidence:** medium

**หลักฐาน / Citation:**
- [WEB:netsuite.com] NetSuite Data Center datasheet — multi-region, no Thai DC
- [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
- [WEB:oracle.com] Public Cloud Regions; AIS Cloud/Oracle Alloy Thailand
- [WEB:securiti.ai] Thailand PDPA — no localization mandate

---

## TOR-TECH-05 — TOR Spec: GRC / Automated SoD Controls

- **Capability (TH):** ควบคุมสิทธิ์ละเอียด + SoD อัตโนมัติ + continuous controls monitoring
- **Capability (EN):** GRC / automated SoD controls
- **Domain:** Technical · **iCE severity:** สูง · **NetSuite ตอบได้?:** Partial · **Priority:** Important

**Oracle Fusion advantage (Standout):** NetSuite SoD พื้นฐาน → Partial; Oracle Risk Management Cloud & SAP GRC มี automated SoD + continuous controls monitoring ในตัว. NetSuite ทำ fine-grained access control ได้ และทำ SoD แบบ **detective** ได้ (saved search/role audit เช่นค้นรายการที่ creator=approver) แต่ **"built-in continuous controls monitoring" + automated SoD เชิง preventive (block self-approval แบบ ruleset) ไม่มี native** ต้องใช้ SuiteApp (Fastpath Assure, Netwrix Strongpoint, Greenlight Approvals).

**TOR wording to weaponize (ภาษาไทย):** ระบบต้องมีการควบคุมสิทธิ์การเข้าถึงแบบละเอียด พร้อมการตรวจสอบการแบ่งแยกหน้าที่ (Segregation of Duties) อัตโนมัติ และ continuous controls monitoring ในตัว

**TOR wording (English):** The solution shall provide fine-grained access control with automated Segregation of Duties (SoD) checks and built-in continuous controls monitoring.

**iCE caveat:** ช่องว่าง "continuous controls monitoring ในตัว" เป็น gap native ที่มีจริง (Oracle/SAP เหนือกว่า) และแนบการกำกับภาครัฐโดยตรง (SoD อยู่ใต้การตรวจของ สตง.) — แต่การบังคับให้มี "ในตัว (native)" คือ over-spec; SoD ที่หน่วยงานต้องการจริงทำได้ด้วย NetSuite native (detective) + SuiteApp certified ซึ่งเป็น market-standard. CCM แบบ native เต็มรูปเป็นฟีเจอร์ระดับองค์กรข้ามชาติ. **record นี้ทับซ้อนกับ NF-SEC-01 / GP-FUNC-27 / GP-TECH-11 — เมื่อประกอบ TOR ให้ยุบเป็นข้อเดียวเชิง outcome (automated + auditable SoD) เพื่อเลี่ยงภาพดันสเปก SoD ซ้ำ ๆ ที่ทำให้ดูล็อกสเปก.**

**Confidence:** high

**หลักฐาน / Citation:**
- [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native ไม่ block self-approval แบบ ruleset)
- [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
- [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
- [KB] Netsuite-Managing Users & Roles (0.6544) — access review/audit guidance (manual)

---

## ภาคผนวก — สรุปเชิงยุทธศาสตร์สำหรับทีมขาย Oracle Fusion (public-sector-govt)

**แกน weaponize ที่ปลอดภัยและมี business rationale จริง (แนะนำ Mandatory ได้):**
1. **Data residency / sovereignty** (NF-ARC-02, GP-TECH-08, GP-STANDOUT-09, TOR-TECH-04) — ยุบเป็นข้อเดียวเชิง outcome "ต้องระบุทางเลือก in-country/sovereign region" · เขียนแบบ outcome-based ไม่บังคับ on-prem
2. **SoD / GRC / access governance** (NF-SEC-01, GP-FUNC-27, GP-TECH-11, TOR-TECH-05) — ยุบเป็นข้อเดียว "automated + auditable SoD" · แนบเหตุผลการตรวจของ สตง.
3. **e-Tax Invoice ไทย native** (GP-FUNC-16, TOR-FIN-03) — เจาะจงที่ e-Tax Invoice XML ส่งกรมสรรพากร · ตัดเงื่อนไข "ทุกประเทศ/ไม่พึ่ง add-on"

**แกนใช้เป็น value story เท่านั้น (ไม่แนะนำ Mandatory — เสี่ยง over-spec/ล็อกสเปก):**
- CLM เต็มรูป (GP-FUNC-11) — ปิดได้ด้วย SuiteApp ราคาประหยัด
- Enterprise PPM/Primavera tier-1 (F-PRJ-01, GP-FUNC-21, TOR-PPM-01) — grants/fund ใช้ได้จริง; PPM tier-1 over-spec
- Strategic sourcing / e-auction (F-PRC-01) — จัดซื้อภาครัฐผ่าน e-GP; e-auction ในตัว ERP แทบไม่ใช้
- Government accreditations (NF-SEC-02) — over-spec เอียงเข้า Oracle ชัด (FedRAMP = สหรัฐฯ ไม่ใช่เกณฑ์ไทย)

**กฎกำกับความเป็นธรรม (สตง. / ผู้ยื่นรายอื่น):** ไม่ดันสเปกที่ทับซ้อนกันหลายข้อเพื่อบีบ NetSuite ให้ตกซ้ำ ๆ (โดยเฉพาะกลุ่ม SoD และ sovereignty ที่มี 3-4 record ทับซ้อน) — ยุบเป็น outcome เดียวต่อธีม, เขียน requirement อิงผลลัพธ์ตามภารกิจจริง, และเก็บ record ที่ iCE ตี "แทบไม่มีผล/over-spec" ไว้เป็น talk-track ไม่ใช่เกณฑ์ตัดสิทธิ์.
