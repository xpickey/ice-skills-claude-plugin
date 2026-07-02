# TOR Competitive KB — public-sector-govt — NetSuite Weakness & Counter

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: "แต่ละ record ให้ระดับ confidence (high/medium/low) ตามว่ามี KB/official citation รองรับหรือไม่ — high = มี KB Qdrant + official Oracle/NetSuite Help/web ยืนยันตรง; medium = มีบางส่วนหรือมี [ต้อง verify]; low = ไม่มี citation ในแหล่ง. รายการที่ติดป้าย [ต้อง verify] ต้องยืนยันกับ environment จริง/ผู้ขายก่อนตัดสินใจ. เอกสารต้นทางเป็น 'ชุดร่าง TOR เชิงแข่งขัน' ที่ออกแบบให้ NetSuite ตอบได้แค่ Partial/No — จึงถือ balanced counter-view ของ iCE เป็นแกนคู่กับ gap ทุกข้อ (ห้ามใช้ gap ลอย ๆ โดยไม่มี counter)."
ams_review: "yearly — re-verify product positions"
---

> **บริบทการใช้งาน (public-sector-govt):** ไฟล์นี้ใช้เมื่อ iCE ขายหรือปกป้อง NetSuite ในบริบทหน่วยงานภาครัฐ/กึ่งราชการ/องค์กรสาธารณกุศลที่อยู่ใต้การกำกับและการตรวจของสำนักงานการตรวจเงินแผ่นดิน (สตง.) และใช้ระบบจัดซื้อจัดจ้างภาครัฐ (e-GP กลาง กรมบัญชีกลาง). ทุกข้ออ้างอิงรูปแบบภารกิจภาครัฐ/สาธารณกุศล/สุขภาพ-ธนาคารเลือด แบบทั่วไป (industry pattern) — ไม่มีชื่อหน่วยงานเฉพาะราย.
>
> **มุมมองเชิงจัดซื้อ (สำคัญที่สุดสำหรับ public-sector):** การเขียน TOR ล็อกสเปกไปที่ฟีเจอร์เฉพาะผลิตภัณฑ์ใดผลิตภัณฑ์หนึ่งมีความเสี่ยงถูกท้วงติงจาก สตง. และผู้ยื่นข้อเสนอรายอื่น. iCE แนะนำให้เขียน requirement แบบ **อิงผลลัพธ์ (outcome-based)** ตามภารกิจจริง ไม่ผูกกับฟีเจอร์ผลิตภัณฑ์เดียว. ประเด็นนี้ถูกอ้างอิงซ้ำในหลาย record ด้านล่างเป็น **Procurement caveat**.

---

## F-PRC-01 — Strategic Sourcing (RFx / e-Auction)

- **Capability (TH):** การจัดหาเชิงกลยุทธ์ (RFx / e-Auction) · **(EN):** Strategic sourcing
- **Domain:** Procurement · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ข้อความ TOR อ้างว่า NetSuite "ไม่มี sourcing engine (RFx/e-auction) ในตัว" และให้คะแนน 0 (ทำไม่ได้เลย) เทียบกับ Oracle Procurement Cloud (Sourcing) ที่มี RFx + e-auction. จุดอ่อน native ที่แท้จริงเหลือเพียง **การประมูลย้อนกลับสด (live reverse e-auction)** ซึ่ง NetSuite ไม่มีในตัว.

**Counter / Mitigation:** คะแนน 0 ไม่ถูกต้อง — NetSuite มี **Request for Quote (RFQ) เป็น native** (ต้องเปิด feature ก่อนใช้): ตั้งช่วงเสนอราคา, ผู้ขายยื่นราคาหลาย tier/price break ผ่าน Vendor Center, มี Award column เปรียบเทียบ/มอบรางวัล และเมื่อบันทึกระบบ **auto-สร้าง Purchase Contract หนึ่งใบต่อผู้ขายที่ได้รับรางวัล** (ยืนยันจาก docs.oracle.com). ช่องว่างจริงจึงแคบเหลือเพียง e-auction เรียลไทม์เท่านั้น ไม่ใช่ "ไม่มี sourcing".

**Procurement caveat:** สำหรับหน่วยงานภาครัฐ/กึ่งราชการในไทย การจัดซื้อใช้เงินรัฐมักผ่าน **ระบบ e-GP กลางของกรมบัญชีกลาง** ไม่ใช่ e-auction ในตัว ERP — การบังคับ "e-auction ในตัว" ลง TOR จึงเป็น over-spec ที่ไม่สะท้อนกระบวนการจริง และเสี่ยงถูกมองว่าล็อกสเปก [ต้อง verify ระเบียบพัสดุเฉพาะของหน่วยงาน].

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Purchasing and Receiving (0.66) — Request for Quotes feature / Vendor RFQ / Awarding a Request for Quote / Purchase Contracts
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (Award column; auto-creates Purchase Contract per awarded vendor; ไม่มี e-auction)
  - [ต้อง verify] จัดซื้อใช้เงินรัฐในไทยมักผ่าน e-GP กลาง ไม่ใช่ e-auction ในตัว ERP; หน่วยงานอาจมีระเบียบพัสดุของตนเอง

---

## F-PRJ-01 — Capital Project Costing / Grants

- **Capability (TH):** การคิดต้นทุนโครงการลงทุน / ทุนสนับสนุน · **(EN):** Capital project costing
- **Domain:** Project · **iCE severity:** กลาง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ข้อความ TOR ระบุ NetSuite PSA เน้นงานบริการ ส่วน capital project (grants, CWIP, deep multi-level WBS) อ่อนกว่า Oracle Project Costing Cloud ซึ่งรองรับ capital/EPC, grants, CWIP และ deep WBS ในตัว. จุดที่อ่อนกว่าจริงคือ **deep multi-level WBS/EPC**.

**Counter / Mitigation:** ฟังก์ชันที่หน่วยงานภาครัฐ/สาธารณกุศลใช้จริงทำได้ แต่กระจายอยู่บน SuiteApp/โมดูลเสริมหลายชั้น: **Job Costing/Project Budgeting** โพสต์ต้นทุนเข้า GL อัตโนมัติ (ต้องให้ account rep เปิดให้); **CWIP/CIP** พักต้นทุนใน GL แล้วตั้งเป็นสินทรัพย์เสื่อมราคาผ่าน **Fixed Assets Management (FAM = SuiteApp)** ได้ (base FAM แบบ manual; workflow CIP buildup คล่องตัวมักพึ่ง third-party Netgain NetAsset); **grants/fund** ใช้ **NFP Financials (managed SuiteApp)** ครอบคลุม Grant/Fund/Revenue Restriction — แต่รายงานสำเร็จรูปอิง US-FASB ต้องปรับให้เข้ามาตรฐานไทย. deep WBS/EPC เป็น over-spec สำหรับภารกิจสร้างสถานพยาบาล/ครุภัณฑ์.

**Procurement caveat:** grants/fund + capital project เกี่ยวข้องสูงและอยู่ใต้การตรวจ สตง. — ต้องวางแผนติดตั้ง SuiteApp (FAM + NFP Financials) และปรับรายงานให้เข้ามาตรฐานไทยตั้งแต่แผน implementation; ส่วน deep WBS/EPC ที่ TOR อาจบรรจุเป็นการล็อกสเปกที่หน่วยงานแทบไม่ใช้.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Projects (0.61) — Job Costing/Project Budgeting โพสต์เข้า GL (ต้องให้ account rep เปิด)
  - [KB] Netsuite-Non-Profit SuiteApps (0.66) — NFP Financials: Grant/Fund/Revenue Restriction
  - [KB] Netsuite-Fixed Assets Management (0.53) — asset type 'project' (CIP) ตั้งสินทรัพย์เมื่อปิดโครงการ
  - [WEB:netsuite.com] NetSuite Nonprofit — Fund Accounting & Grant Management (NFP Financials SuiteApp)
  - [WEB:community.oracle.com] FAM — Tracking Construction in Progress (CIP) in Fixed Asset Management
  - [WEB:netgain.tech] NetSuite Fixed Asset Roll Forward & CIP (NetAsset = third-party add-on)

---

## NF-ARC-02 — Deployment Options & Data Residency / Sovereignty

- **Capability (TH):** ทางเลือกการติดตั้ง / data residency · **(EN):** Deployment & data residency options
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite เป็น **multi-tenant SaaS ล้วน** — ไม่มีทางเลือก on-prem / private / Cloud@Customer และ **ไม่มี data center ในไทย** อีกทั้งยังไม่รองรับ Oracle EU Sovereign Cloud (เลือกได้เพียง data center ภูมิภาค เช่น EU: Amsterdam/Frankfurt/London). Oracle มีเส้นทาง in-country/sovereign (AIS Cloud/Oracle Alloy ในไทย, EU Sovereign Cloud) ที่ NetSuite ยังไม่มี. **นี่เป็นข้อจำกัดเชิงสถาปัตยกรรมที่ปิดด้วย SuiteApp/custom ไม่ได้เลย.**

**Counter / Mitigation:** ข้อจำกัดนี้ถูกต้อง ไม่ใช่การกล่าวเกิน — แต่เป็น **over-spec เมื่อองค์กรเลือกแนวทาง SaaS** และ **PDPA ไทยไม่บังคับเก็บข้อมูลในประเทศ** (เป็นประเด็นนโยบายบอร์ด ไม่ใช่ข้อบังคับกฎหมาย). NetSuite มี data residency เชิงภูมิภาค (EU/NA/APAC) และ Oracle Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน. หากบอร์ดให้น้ำหนัก sovereignty ของข้อมูลผู้ป่วย/ผู้บริจาค ควรเป็นการตัดสินใจ/ยอมรับความเสี่ยงระดับบอร์ดก่อน go-live.

**Procurement caveat:** สำหรับหน่วยงานภาครัฐที่ถือข้อมูลสุขภาพ/ผู้บริจาค (data class อ่อนไหวสูง อยู่ใต้การกำกับภาครัฐ) หากกำหนด in-country/sovereign residency เป็น "ข้อบังคับ" ใน TOR → NetSuite จะเสียเปรียบและปิด gap ไม่ได้. ควรเขียนเป็น "ระบุทางเลือก data center + แผนจัดการข้อมูล" (outcome-based) มากกว่าล็อก sovereign region ในไทย เพื่อไม่ให้เป็นเงื่อนไขกันผู้เสนอ SaaS-only. [ต้อง verify สถานะ Oracle EU Sovereign Cloud].

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] What is NetSuite ERP (multi-tenant SaaS, no on-prem)
  - [WEB:sota.io] NetSuite NOT available on Oracle EU Sovereign Cloud as of Q1 2026 [ต้อง verify]
  - [WEB:oracle.com] AIS Cloud / Oracle Alloy — in-country Thai cloud (2024)
  - [KB] NSTWP — multi-tenant shared service (0.541)

---

## NF-SEC-01 — Automated Segregation of Duties (SoD)

- **Capability (TH):** การแบ่งแยกหน้าที่อัตโนมัติ (SoD) · **(EN):** Automated SoD & access governance
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite มี role-based security แต่ **ไม่มี engine SoD อัตโนมัติ / continuous controls monitoring สำเร็จรูปแบบ native** ต่างจาก Oracle Risk Management Cloud (Advanced Access Controls) ที่ทำ automated SoD + access governance + risk management ในตัวพร้อม ruleset สำเร็จรูปจำนวนมาก.

**Counter / Mitigation:** ข้อความ "ไม่มี access governance ระดับ audit" ลดทอนของจริง — NetSuite มี role-based security ละเอียด + approval routing (SuiteFlow / SuiteApprovals) + **เครื่องมือตรวจสิทธิ์ในตัว** (Use Searches to Audit Roles, Show Role Permission Differences), **Login Audit Trail**, 2FA/SSO และผ่าน audit SOC 1/2, ISO 27001 จริง. ปิด gap SoD engine ด้วย **certified SuiteApp** (Fastpath Assure ruleset 125+ conflicts, Netwrix Strongpoint, SafePaaS) ที่ต้นทุนบริหารจัดการได้.

**Procurement caveat:** SoD/access governance ครอบการรับบริจาคและการจัดซื้อจัดจ้างที่อยู่ **ภายใต้การตรวจของ สตง.** โดยตรง จึงควรวางแผนจัดหา SuiteApp certified ปิด gap ก่อน go-live เป็นความจำเป็นจริง (ไม่ใช่ over-spec). ส่วน GRC engine อัตโนมัติเทียบ Oracle Advanced Access Controls ที่เหนือกว่าเป็นส่วนเกินของ NGO/หน่วยงานประเทศเดียว — ไม่ควรล็อกเป็น "native ในตัว".

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
  - [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review/terminated-user revocation
  - [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + ruleset สำเร็จรูปจำนวนมาก
  - [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
  - [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## NF-SEC-02 — Industry / Government Accreditations

- **Capability (TH):** การรับรองด้านอุตสาหกรรม/ภาครัฐ · **(EN):** Industry/government accreditations
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite **ไม่มี accreditation ภาครัฐแบบ FedRAMP / government-cloud / sovereign region** เหมือน Oracle OCI เพราะเป็น multi-tenant SaaS ล้วน. Oracle มี industry solutions + gov/regulated accreditation กว้างกว่า.

**Counter / Mitigation:** NetSuite ถือ **ใบรับรองสากลครบ**: SOC 1/SOC 2 Type II, ISO 27001/27018/42001 และ **PCI DSS Level 1 Service Provider + PCI SSF** (verified จากหน้า NetSuite Operational Security). accreditation ภาครัฐที่ Oracle เหนือกว่า (FedRAMP/IL/sovereign) เป็นการรับรองของ **รัฐบาล/กลาโหมสหรัฐฯ** ไม่ใช่ข้อกำหนดของหน่วยงานไทย.

**Procurement caveat:** การเขียน TOR ให้ต้องมี "accreditation ภาครัฐกว้าง" เป็น over-spec ที่เอียงเข้าหา Oracle — ใบรับรองที่เกี่ยวข้องจริงกับหน่วยงานไทย (ISO 27001, SOC, PCI สำหรับช่องทางรับบริจาคบัตรเครดิต) NetSuite มีครบ. ควรระบุเฉพาะ accreditation ที่ผูกกับภารกิจจริง ไม่อ้าง FedRAMP/US-gov cloud.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] NetSuite Application and Operational Security — SOC 1/2, ISO 27001/27018/42001, PCI DSS, PCI SSF
  - [WEB:houseblend.io] NetSuite Audit Readiness: SOC 1, SOC 2 & ISO 27001 Guide
  - [WEB:stratusgreen.com] NetSuite PCI Compliance — Level 1 Service Provider

---

## GP-FUNC-09 — Strategic Sourcing / e-Sourcing / RFx & Auctions

- **Capability (TH):** จัดหาเชิงกลยุทธ์ / e-Sourcing / ประมูล · **(EN):** Strategic sourcing / e-Sourcing / RFx & auctions
- **Domain:** Procurement · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** Gap Pack ให้ NetSuite 1★ ระบุ "จัดซื้อพื้นฐาน" เทียบ Oracle Fusion 4★ / SAP S/4HANA 5★ (SAP Ariba & Oracle Sourcing Cloud ครบกว่ามาก). จุดอ่อนจริงคือ **ไม่มี e-auction (ประมูลออนไลน์ย้อนกลับ)** และ **ไม่มีเครือข่ายจัดหาแบบ SAP Ariba Network/Oracle Sourcing Cloud**.

**Counter / Mitigation:** เรตติ้ง 1★ ต่ำเกินไป — NetSuite จัดซื้อมากกว่า "พื้นฐาน": **RFQ native + Purchase Contracts/Blanket Orders (auto จาก RFQ)** + vendor performance (on-time delivery native, scorecard ผ่าน KPI Scorecard/custom KPI, predictive ผ่าน Supply Chain Control Tower เสริม). งาน RFx/เปรียบเทียบราคา/ออก Purchase Contract ทำได้ในตัว. ที่เกินคือ e-auction และ sourcing network ระดับองค์กรข้ามชาติ.

**Procurement caveat:** e-Sourcing network/e-auction เกี่ยวข้องต่ำกับหน่วยงานภาครัฐ/สาธารณกุศลในไทยที่จัดซื้อผ่าน e-GP กลาง — การบังคับ e-auction "ในตัว" เป็น over-spec/ล็อกสเปก. RFx/contract เกี่ยวข้องและ NetSuite รองรับ native.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Purchasing and Receiving (0.66–0.67) — RFQ / Award / Purchase Contracts & Blanket Orders
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (auto Purchase Contract; ไม่มี e-auction)
  - [ต้อง verify][WEB:erpresearch.com] ความเห็นว่า Oracle ERP Cloud เหนือกว่าด้าน procurement แต่ NetSuite ครอบ mid-market — เป็นแหล่งความเห็น/บล็อก ยังไม่ยืนยันแน่ชัด

---

## GP-FUNC-11 — Contract Lifecycle Management (CLM)

- **Capability (TH):** บริหารสัญญา (CLM) · **(EN):** Contract Lifecycle Management (CLM)
- **Domain:** Procurement · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite **ไม่มีโมดูล CLM ในตัวเลย** — native "Managing Contracts" เป็นสัญญาฝั่งขาย/ต่ออายุเท่านั้น (Software Vertical Contract Renewals) ไม่มี **clause library (คลังข้อสัญญา), authoring, redline หรือ obligation management**; ฝั่งจัดซื้อมีเพียง Purchase Contract + เก็บไฟล์ใน File Cabinet. CLM เต็มรูปต้องพึ่ง SuiteApp พาร์ทเนอร์ (Gatekeeper, Azdan, Conga/Malbek) ทั้งหมด. Gap Severity = Med (ในเอกสาร).

**Counter / Mitigation:** ข้อกล่าวอ้าง "ไม่มี CLM ในตัว" ถูกต้องในแง่โมดูลเฉพาะ — แต่ความต้องการจริงของหน่วยงานภาครัฐ (**คลังสัญญา + แจ้งเตือนต่ออายุ + audit trail**) ทำได้ด้วย native + **SuiteApp ราคาประหยัด (Gatekeeper ฯลฯ) ต้นทุนไม่สูง** ไม่ใช่ blocker. CLM ระดับ enterprise (AI redline/clause library เต็มรูป) เป็น over-spec — จึงสอดคล้องกับ gap severity "Med" ในระดับผลิตภัณฑ์.

**Procurement caveat:** งานจัดซื้อ/สัญญาทุนสนับสนุนของหน่วยงานอยู่ **ใต้การตรวจ สตง.** ต้องมีคลังสัญญา + แจ้งเตือนต่ออายุ + audit trail พร้อมใช้ตั้งแต่ go-live — ต้องวางแผน/จัดงบเปิดใช้ SuiteApp ล่วงหน้า (จึงจัด iCE severity = สูง แม้ gap ระดับผลิตภัณฑ์เป็น Med). ไม่ควรล็อก TOR ไปที่ AI redline/clause library ระดับ enterprise.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Software Vertical Contract Renewals (0.66) + Netsuite-Sales Orders and Cash Sales (0.63) — เป็น contract ฝั่งขาย/ต่ออายุเท่านั้น
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Managing Contracts (จำกัดที่ sales renewal lifecycle; ไม่มี clause library/authoring/obligation)
  - [WEB:suiteapp.com] Gatekeeper Contract Management & Vendor Portal — CLM สำหรับ NetSuite เป็น SuiteApp พาร์ทเนอร์ (ยืนยันมีจริง)

---

## GP-FUNC-16 — Statutory Localization, Tax Engine & e-Invoicing (e-Tax Invoice TH)

- **Capability (TH):** Tax engine & localization ตามกฎหมายแต่ละประเทศ · **(EN):** Statutory localization, tax engine & e-invoicing
- **Domain:** Finance · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** Gap Pack ให้ 2★ ระบุ SuiteTax ครอบคลุมประเทศน้อยกว่า SAP/Oracle. จุดอ่อนจริงเชิงไทยคือ **e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากรยังไม่มี native** — Electronic Invoicing SuiteApp เป็นเพียง "กรอบ" ออก XML/JSON ต้องทำ template เอง/ใช้ partner.

**Counter / Mitigation:** การให้ 2★ ประเมินต่ำไปสำหรับ scope ไทย — **SuiteTax เป็น tax engine จริง + localization ไทยครบ** (SEA Localization + International Tax Reports → VAT/ภ.พ.30, ใบกำกับภาษี/เครดิตโน้ตตามรูปแบบกรมสรรพากร) ซึ่ง SuiteApp ที่ใช้เป็น **free managed first-party bundle ของ NetSuite เอง (ไม่ใช่ third-party)**. ช่องว่างจริงจึงเหลือเฉพาะ e-Tax Invoice XML (custom/partner) ไม่ใช่ "ทำภาษีไม่ได้" และไม่ใช่เรื่องจำนวนประเทศ.

**Procurement caveat:** e-Tax Invoice & e-Receipt เป็น **ข้อบังคับตามกฎหมายไทย** ทุกหน่วยที่ออกเอกสารภาษี (สถานพยาบาล/จัดซื้อ/รับบริจาคที่มีภาษี) จึงต้องวางแผนทำ custom/partner เพื่อปิด gap นี้ก่อน go-live (จริงจัง, ไม่ใช่ over-spec). ส่วนเงื่อนไข "ทุกประเทศ native โดยไม่พึ่ง add-on" ไม่เกี่ยวเพราะหน่วยงานอยู่ไทยประเทศเดียว.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Country Specific Features (0.7242, SuiteTax Reports/VAT)
  - [WEB:docs.oracle.com] Thailand Tax Invoice & Credit Memo Templates (SEA Localization, P.P.30)
  - [WEB:docs.oracle.com] Electronic Invoicing Overview (กรอบ XML/JSON ไม่มี native มาตรฐานไทย)

---

## GP-FUNC-27 — Governance, Risk & Compliance (GRC) / SoD

- **Capability (TH):** กำกับ ความเสี่ยง การควบคุม / SoD · **(EN):** Governance, Risk & Compliance (GRC) / SoD
- **Domain:** GRC · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** Gap Pack ให้ 2★ (Partial). GRC ในตัวของ NetSuite เป็นเพียงบริหาร role/permission + audit trail + approval workflow + เครื่องมือตรวจสิทธิ์ (saved search/role audit) — **ไม่มี engine automated SoD / continuous controls monitoring แบบ native** เหมือน Oracle Risk Mgmt Cloud หรือ SAP GRC Access Control.

**Counter / Mitigation:** เรตติ้ง 2★ (Partial) สมเหตุผล และ gap automated SoD/CCM มีจริง — แต่ถ้อยคำ "SoD/role review พื้นฐาน" ลดทอน: NetSuite มี **เครื่องมือ audit role + audit trail native และ ecosystem SoD ที่ certified เต็มที่** (Fastpath Assure, Netwrix Strongpoint, SafePaaS) ปิด gap ได้.

**Procurement caveat:** องค์กรอยู่ **ใต้การตรวจของ สตง.** การควบคุมการแบ่งแยกหน้าที่ (SoD) เป็นข้อกำหนดด้านธรรมาภิบาล/ตรวจสอบ — ต้องวางแผนติดตั้ง SuiteApp SoD ที่ certified และออกแบบ controls ก่อน go-live (ความจำเป็นจริง). ส่วน continuous controls monitoring ระดับ enterprise เต็มรูปเป็นส่วนเสริมที่เลือกได้ ไม่ควรบังคับเป็น "native ในตัว".

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Managing Users & Roles (0.695/0.6678) — role permissions + audit role searches
  - [WEB:netsuite.com] What is NetSuite Governance, Risk & Compliance? — GRC = native controls + partner SuiteApp (ไม่ใช่ SoD engine native)
  - [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring
  - [WEB:netwrix.com] NetSuite Segregation of Duties (Strongpoint) — alert on SoD conflicts
  - [WEB:suiteapp.com] Fastpath Assure for NetSuite

---

## GP-TECH-07 — Deployment Options (Public / Private / On-Prem)

- **Capability (TH):** ทางเลือกติดตั้ง (cloud/private/on-prem) · **(EN):** Deployment options (public/private/on-prem)
- **Domain:** Technical · **iCE severity:** แทบไม่มีผล

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite เป็น **public multi-tenant cloud อย่างเดียว** ไม่มีทางเลือก private cloud หรือ on-premise แบบ SAP RISE/S/4HANA on-prem (ทุกอย่างเป็น fully-managed บน OCI/Oracle Autonomous Database). Gap Pack ให้ 1★ เทียบ Oracle 4★ / SAP 5★. ข้อจำกัดนี้เป็นจริงตามสเปก.

**Counter / Mitigation:** เมื่อองค์กรตัดสินใจมุ่งใช้ SaaS แล้ว **ความยืดหยุ่นเรื่อง private/on-prem จะไม่ถูกนำมาใช้จริง** — Oracle ก็ให้บริการ NetSuite แบบ fully-managed อยู่แล้ว (ลดภาระ infra/DBA).

**Procurement caveat:** การบังคับ on-prem/private ใน RFP ระบบคลาวด์เป็น **การล็อกสเปกเพื่อกัน vendor ที่เป็น SaaS-only** มากกว่าจะเป็นความต้องการใช้งานจริง — สำหรับ public-sector ที่เลือกแนวทาง SaaS นี่คือ over-spec ที่เสี่ยงถูกท้วง. (แยกออกจากประเด็น data residency ที่เป็นเรื่องคนละมิติ — ดู NF-ARC-02 / GP-TECH-08).

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] Why Multi-tenancy in the Cloud Matters (cloud-only, no on-prem)
  - [WEB:netsuite.com] What is NetSuite ERP

---

## GP-TECH-08 — Data Residency, Sovereignty & Region Count

- **Capability (TH):** ถิ่นที่อยู่ข้อมูล / sovereign / จำนวน region · **(EN):** Data residency, sovereignty & region count
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite **ไม่มี DC ในประเทศไทยและไม่รองรับ EU Sovereign Cloud** ขณะที่ Oracle มีเส้นทาง sovereign/in-country (EU Sovereign Cloud, AIS Cloud/Oracle Alloy ไทย) ที่ NetSuite ยังไม่มี — จุดต่างนี้ **ไม่สมมาตร**. Gap Pack ให้ NetSuite 2★ เทียบ Oracle 5★ (OCI public+gov+sovereign regions มากสุด เหมาะ TOR ภาครัฐ).

**Counter / Mitigation:** ข้อความ "ไม่มี residency" ไม่ถูกต้อง — NetSuite ให้ **data residency ผ่าน data center หลายภูมิภาค (EU/NA/APAC)**. จุดต่างจริงคือไม่มี DC ในไทย/EU Sovereign Cloud เท่านั้น. **PDPA ไม่บังคับ data localization** และ **Oracle Fusion SaaS แบบ public มาตรฐานก็ไม่มี region ในไทยเช่นกัน** — จึงไม่ใช่ข้อได้เปรียบ Fusion แบบเบ็ดเสร็จ ยกเว้นบอร์ดเลือกเส้นทาง sovereign in-country ของ Oracle.

**Procurement caveat:** ข้อมูลสุขภาพ/ผู้บริจาคทำให้ data sovereignty มีน้ำหนักเชิงนโยบาย/การตรวจสอบสำหรับ public-sector — ควร **เคลียร์ทางเลือก data center ในประเทศ/sovereign ก่อน go-live** และตรวจตัวเลือกของทั้งสองค่าย (ไม่ปัดทิ้ง แต่ก็ไม่ควรล็อก sovereign region ในไทยเป็นข้อบังคับ เพราะไม่มีเจ้าใดมี public region มาตรฐานในไทย). [ต้อง verify].

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] NetSuite Data Center datasheet — EU DCs (Amsterdam/Frankfurt/London/Newport), no Thai DC
  - [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
  - [WEB:bakermckenzie.com] Thailand cross-border data transfer — no localization mandate
  - [WEB:oracle.com] AIS Cloud / Oracle Alloy Thailand (2024)

---

## GP-TECH-11 — Fine-Grained Access & Automated SoD Controls

- **Capability (TH):** ควบคุมสิทธิ์ละเอียด / SoD อัตโนมัติ · **(EN):** Fine-grained access & automated SoD controls
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite **ไม่มี "การแยกหน้าที่อัตโนมัติ" (SoD) ระดับ ruleset และ continuous control monitoring แบบ preventive ในตัว** — ทำได้เพียง detective (เช่น Login Audit Trail) ต้องเสริมด้วย SuiteApp พาร์ทเนอร์ (Fastpath Assure, Netwrix Strongpoint, SafePaaS) ขณะที่ Oracle Risk Mgmt/SAP GRC มีในตัว. Gap Pack ให้ 2★.

**Counter / Mitigation:** ถ่วงดุล: **การคุมสิทธิ์พื้นฐานของ NetSuite ละเอียดและ audit ได้** — fine-grained permission **636+ ต่อ record/feature** + Login Audit Trail + 2FA/TBA + role-diff/audit search จึงไม่ใช่แค่ "role-based พื้นฐาน" อย่างที่ร่างกล่าวอ้าง และ gap ปิดได้ด้วย add-on certified.

**Procurement caveat:** กระทบงานควบคุมภายในที่อยู่ **ใต้การตรวจของ สตง.** โดยตรง — ต้องวางแผนจัดซื้อ add-on SoD/GRC และตั้งงบบริหารจัดการก่อน go-live. automated continuous SoD ระดับ enterprise เป็นส่วนเสริมที่เกินจำเป็นสำหรับสเกลหน่วยงานประเทศเดียว — ควรกำหนดเป็นผลลัพธ์ (มี SoD control ที่ตรวจสอบได้) ไม่ใช่บังคับ "native CCM".

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Managing Users & Roles (0.6691) — granular permission structure (636+ permissions)
  - [KB] Netsuite-Authentication Guide — 2FA / token-based auth; Netsuite-Administrator Guide (0.6642) — password policy + SoD monitoring example (PO created by AP)
  - [WEB:oracle.com] Oracle Advanced Access Controls — continuous SoD monitoring
  - [WEB:mysuite.tech] NetSuite SoD native vs add-on boundary (detective not preventive)

---

## GP-STANDOUT-07 — Fusion Standout: End-to-End Procurement Cloud

- **Capability (TH):** Procurement Cloud ครบวงจร · **(EN):** End-to-end Procurement Cloud
- **Domain:** Procurement · **iCE severity:** ต่ำ

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** Oracle Fusion ยก Procure-to-Pay + Sourcing + Supplier Mgmt อยู่ในชุดเดียว ไม่ต้องผูก network แยกแบบ Ariba. NetSuite ให้งานจัดซื้อระดับพื้นฐาน (P2P) — **ขาดความครบของ strategic sourcing/e-auction และ supplier management เชิงลึก** ที่ Oracle Fusion มีในตัว และต้องต่อ e-GP ตามระเบียบพัสดุไทยผ่าน integration เอง.

**Counter / Mitigation:** งานจัดซื้อสาธารณกุศล/กึ่งราชการเน้น **procure-to-pay + เส้นทางอนุมัติ + เชื่อม e-GP** ซึ่ง NetSuite Procurement + integration ทำได้. ส่วน strategic sourcing/e-auction เต็มรูปเป็น **nice-to-have ไม่ใช่ตัวตัดสิน**.

**Procurement caveat:** สำหรับ public-sector ไทย เส้นทางจัดซื้อจริงคือ P2P + e-GP กลาง — จึงควรกำหนด TOR รอบ "เชื่อม e-GP + approval workflow ตามระเบียบพัสดุ" (outcome-based) มากกว่าล็อก "Procurement Cloud ครบวงจรในชุดเดียว" ที่เอียงเข้า Fusion.

- **Confidence:** low
- **หลักฐาน / Citation:**
  - (ไม่มี KB/official citation เฉพาะใน record มาตรฐานนี้ — ข้อสรุปอิงตำแหน่งผลิตภัณฑ์ Fusion vs NetSuite; cross-reference หลักฐาน RFQ/Purchase Contract native ที่ GP-FUNC-09 / F-PRC-01)

---

## GP-STANDOUT-09 — Fusion Standout: Broad Public + Sovereign Cloud Regions

- **Capability (TH):** region/sovereign cloud หลากหลาย · **(EN):** Broad public + sovereign cloud regions
- **Domain:** Technical · **iCE severity:** สูง

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ตัวเลือก data center ของ NetSuite จำกัดและ **ไม่มี government/sovereign region ในไทย** ต่างจาก OCI ที่มี public + government + sovereign regions มากกว่า — **ข้อนี้เป็นข้อได้เปรียบ Fusion/OCI ที่ legitimate** (ไม่ใช่ over-spec เสมอไป).

**Counter / Mitigation:** เป็นข้อได้เปรียบ Oracle จริง — iCE แนะนำ **verify ตัวเลือก data center ในประเทศของทั้งสองค่ายก่อนตัดสิน (ไม่ปัดทิ้ง)**. หากมีข้อกำหนด data residency ในไทยสำหรับข้อมูลสุขภาพ/ผู้บริจาคโลหิตภายใต้ PDPA เรื่อง region/sovereign cloud อาจเป็น blocker.

**Procurement caveat:** สำหรับ public-sector/ธนาคารเลือด หากกำหนด in-country/sovereign residency เป็นเงื่อนไข → ต้องตรวจตัวเลือก data center ในประเทศของทั้งสองค่ายและวางแผนปิด gap ก่อน go-live. นี่เป็นหนึ่งในไม่กี่ข้อที่ iCE ยอมรับว่าเป็น "ประเด็นควรพิจารณาจริง" (ไม่ใช่ over-spec) — แต่พึงระวังว่า Oracle Fusion SaaS public มาตรฐานก็ไม่มี region ในไทยเช่นกัน จึงต้องเป็นเส้นทาง sovereign เฉพาะ. [ต้อง verify].

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - (Record standout อ้างตำแหน่งผลิตภัณฑ์; หลักฐานเชิงเทคนิครองรับดูที่ GP-TECH-08 / NF-ARC-02 — NetSuite EU DCs no Thai DC; Oracle AIS Cloud/Alloy Thailand 2024; NetSuite not on EU Sovereign Cloud Q1 2026 [ต้อง verify])

---

## TOR-FIN-03 — TOR: Statutory Tax / e-Invoicing (e-Tax Invoice TH)

- **Capability (TH):** localization + statutory/tax + e-invoicing/e-tax ในตัวทุกประเทศ · **(EN):** Built-in localization & statutory/tax compliance incl. e-invoicing
- **Domain:** Finance · **iCE severity:** สูง · **Priority:** Mandatory · **NetSuite ตอบได้?:** No (ในร่าง TOR)

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ร่าง TOR กำหนด "ต้องมี localization และ statutory/tax compliance ในตัวสำหรับทุกประเทศ รวมถึง e-invoicing/e-tax โดยไม่ต้องพึ่ง third-party add-on" และให้ NetSuite = **No**. จุดอ่อนจริงคือ **e-Tax Invoice/e-Receipt แบบ XML ส่งกรมสรรพากรยังไม่มี native** (Electronic Invoicing เป็นกรอบเปล่า).

**Counter / Mitigation:** การตอบ "No" เกินจริงสำหรับ scope ไทย — NetSuite รองรับ statutory/localization ไทยผ่าน **SuiteApp ที่ NetSuite เผยแพร่เอง (SEA Localization + International Tax Reports = free managed bundle ไม่ใช่ third-party)** ครอบคลุม VAT/ภ.พ.30 + ใบกำกับภาษี/เครดิตโน้ตตามกรมสรรพากร. ความจริงคือ **Partial ไม่ใช่ No** — จุดอ่อนเหลือเฉพาะ e-Tax Invoice XML (custom/partner).

**Procurement caveat:** เงื่อนไข "ทุกประเทศ + e-tax native โดยไม่พึ่ง add-on" คือ **การล็อกสเปก** — หน่วยงานอยู่ไทยประเทศเดียว และ SuiteApp ที่ใช้เป็นของ NetSuite เอง (ไม่ใช่ third-party ตามที่อ้าง). e-Tax Invoice XML เป็นข้อกำหนดไทยที่ต้องส่งกรมสรรพากร จึงต้องวางแผนปิด gap นี้ (custom/partner) ก่อนใช้งานจริง — แต่ควรเขียน TOR อิงผลลัพธ์ "รองรับ e-Tax Invoice ตามมาตรฐานกรมสรรพากร" ไม่ใช่ "native ทุกประเทศ".

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:docs.oracle.com] Southeast Asia Localization (free managed first-party bundle)
  - [WEB:docs.oracle.com] Thailand Invoicing Features / Electronic Invoicing Overview (กรอบ ไม่มี native ไทย)
  - [KB] Netsuite-Country Specific Features (0.7209)

---

## TOR-PRC-01 — TOR: Strategic Sourcing (RFx / e-Auction)

- **Capability (TH):** strategic sourcing (RFx, e-auction, supplier scorecard, supplier lifecycle) · **(EN):** Strategic sourcing with RFx, e-auctions, scorecards, SLM
- **Domain:** Procurement · **iCE severity:** ต่ำ · **Priority:** Important · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ร่าง TOR รวม RFx + e-auction + supplier scorecard + supplier lifecycle ในข้อเดียว. NetSuite **ขาด e-auction (การประมูลออนไลน์) ในตัว** และ **supplier lifecycle/qualification ครบวงจรยังอ่อน** (ทำได้บางส่วน). Differentiator ในร่างระบุ "NetSuite จัดซื้อพื้นฐาน".

**Counter / Mitigation:** NetSuite ทำได้ ~3/4 ของข้อกำหนด: **RFQ + auto Purchase Contract เป็น native (แข็ง)**, vendor scorecard ผ่าน on-time delivery native + KPI Scorecard/custom KPI + Supply Chain Control Tower เสริม (กลาง), vendor lifecycle/qualification บางส่วน (อ่อน). ns_can='Partial' ตรงข้อเท็จจริง แต่ฉลาก "จัดซื้อพื้นฐาน" ลดทอนเกินไป.

**Procurement caveat:** RFx + supplier scorecard เกี่ยวข้องและ NetSuite รองรับ native/คอนฟิก — การบังคับ e-auction "ในตัว" เข้า TOR คือ **over-spec ที่หน่วยงานภาครัฐไทยไม่ได้ใช้จริง** (จัดซื้อผ่าน e-GP กลาง). [ต้อง verify use case จริงของหน่วยงาน].

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Purchasing and Receiving (0.66) — RFQ/Award/Purchase Contracts
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Analyzing and Awarding a Request for Quote (RFx native, auto Purchase Contract, ไม่มี e-auction)
  - [WEB:docs.oracle.com] NetSuite Applications Suite — Vendor Delivery Performance Scores (scorecard ผ่าน Supply Chain Control Tower + custom KPI)

---

## TOR-PPM-01 — TOR: Enterprise PPM, Project Costing & Grants

- **Capability (TH):** Enterprise PPM (project costing, budget vs actual, capitalization, grants, auto-post GL) · **(EN):** Enterprise PPM with project costing, grants, auto GL posting
- **Domain:** Project · **iCE severity:** กลาง · **Priority:** Important · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** ร่าง TOR ให้ Partial โดย differentiator ระบุ "NetSuite SuiteProjects ดีงาน services; Oracle PPM Cloud เหนือกว่าใน project costing/grants". ที่ติด Partial คือ **deep WBS/EPC-grade** เท่านั้น.

**Counter / Mitigation:** องค์ประกอบหลักของ TOR ทำได้จริงผ่าน native + SuiteApp: **project costing, budget vs actual, auto-post เข้า GL** (Job Costing/Project Budgeting — ต้องให้ account rep เปิด), **capitalization ผ่าน FAM** (CIP→สินทรัพย์เสื่อมราคา; workflow CIP คล่องตัวมักพึ่ง third-party NetAsset, base FAM แบบ manual) และ **grants/fund ผ่าน NFP Financials (SuiteApp**; รายงานสำเร็จรูปอิง US-FASB ต้องปรับเป็นไทย). Partial จึงต่ำกว่าความจริงในบริบทหน่วยงานสาธารณกุศล.

**Procurement caveat:** สูงสำหรับ grants/fund + capitalization (ภารกิจรับบริจาค/ทุนสนับสนุน อยู่ใต้การตรวจ สตง.) — ต้องตั้งงบ NFP Financials + FAM และปรับรายงานเข้ามาตรฐานไทยตั้งแต่แผน. enterprise PPM tier-1/Primavera เป็น over-spec — ไม่ควรล็อก deep WBS/EPC.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Projects (0.61) — native project costing/job costing/budgeting
  - [KB] Netsuite-Non-Profit SuiteApps (0.66) — NFP Financials Grant/Fund
  - [WEB:netsuite.com] NetSuite Nonprofit — Fund Accounting & Grant Management (NFP Financials)
  - [WEB:community.oracle.com] FAM CIP — capitalize project costs to fixed asset

---

## TOR-TECH-04 — TOR: Deployment / Data Residency Options

- **Capability (TH):** ระบุทางเลือกการติดตั้ง (public/private/sovereign) + data center รองรับ data residency · **(EN):** State deployment options & data-center locations meeting data-residency
- **Domain:** Technical · **iCE severity:** สูง · **Priority:** Mandatory · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** จุดอ่อนจริงและ **ปิดไม่ได้เชิงสถาปัตยกรรม**: NetSuite เป็น public multi-tenant SaaS เท่านั้น — **ไม่มี data center ในไทย ไม่มี private/sovereign region และไม่อยู่บน EU Sovereign Cloud**; ต่างจาก gap อื่นในชุดนี้ที่ปิดได้ด้วย SuiteApp ข้อนี้เพิ่ม in-country/sovereign region ให้ NetSuite ไม่ได้. Oracle มีเส้นทาง in-country (AIS Cloud/Oracle Alloy ไทย) ที่ NetSuite ยังไม่มี.

**Counter / Mitigation:** การตี "region จำกัด → Partial" ประเมินต่ำกว่าจริง เพราะ **ข้อกำหนดเพียง "ระบุทางเลือก"** ซึ่ง NetSuite ทำได้ (public multi-tenant บน data center EU/NA/APAC มี data residency เชิงภูมิภาค). in-country ไทยไม่ใช่ข้อบังคับ PDPA และ **Fusion SaaS public มาตรฐานก็ไม่มี region ในไทยเช่นกัน**.

**Procurement caveat:** แตะข้อมูลสุขภาพผู้ป่วย/ผู้บริจาคโลหิตของศูนย์บริการโลหิตและโรงพยาบาลโดยตรง (data class อ่อนไหวสูง อยู่ใต้การกำกับภาครัฐ) — หากองค์กรกำหนด in-country/sovereign residency เป็นเงื่อนไข NetSuite จะเสียเปรียบและต้องเคลียร์ก่อน go-live. แต่เนื่องจาก TOR ขอเพียง "ระบุทางเลือก" ควรคง requirement ไว้ระดับนี้ (NetSuite ตอบได้) ไม่ยกเป็น sovereign-in-country mandatory. [ต้อง verify in-country/sovereign roadmap].

- **Confidence:** medium
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] NetSuite Data Center datasheet — multi-region, no Thai DC
  - [WEB:sota.io] NetSuite not on Oracle EU Sovereign Cloud (Q1 2026) [ต้อง verify]
  - [WEB:oracle.com] Public Cloud Regions; AIS Cloud/Oracle Alloy Thailand
  - [WEB:securiti.ai] Thailand PDPA — no localization mandate

---

## TOR-TECH-05 — TOR: GRC / Automated SoD Controls

- **Capability (TH):** fine-grained access + automated SoD + continuous controls monitoring ในตัว · **(EN):** Fine-grained access with automated SoD & built-in CCM
- **Domain:** Technical · **iCE severity:** สูง · **Priority:** Important · **NetSuite ตอบได้?:** Partial

**จุดที่ NetSuite สู้ไม่ได้ (Gap):** NetSuite ทำ fine-grained access control ได้ในตัว และทำ SoD แบบ **detective** ได้ (saved search/role audit เช่นค้นรายการที่ creator=approver) — แต่ **"built-in continuous controls monitoring" + automated SoD เชิง preventive (block self-approval แบบ ruleset) ไม่มี native** ต้องใช้ SuiteApp (Fastpath Assure, Netwrix Strongpoint, Greenlight Approvals) ซึ่งเป็น market-standard.

**Counter / Mitigation:** จุดอ่อน native มีจริง (Oracle Risk Mgmt Cloud/SAP GRC เหนือกว่า) — แต่ปิดได้ด้วย **certified SuiteApp** สำหรับส่วน preventive/CCM. fine-grained access + detective SoD ที่หน่วยงานต้องการจริงทำได้ด้วย NetSuite native.

**Procurement caveat:** เกี่ยวข้องสูงเพราะการแบ่งแยกหน้าที่ (SoD) อยู่ **ใต้การตรวจของ สตง.** โดยตรง — ต้องวางแผนจัดหา SuiteApp ปิด preventive SoD และออกแบบ control matrix ให้พร้อมก่อน go-live เพื่อผ่านการตรวจ. ส่วน CCM แบบ native เต็มรูปเป็นฟีเจอร์ระดับองค์กรข้ามชาติที่เป็น over-spec — บังคับให้ "มีในตัว" คือการล็อกสเปก ควรกำหนดเป็นผลลัพธ์ "มี SoD/CCM ที่ตรวจสอบได้" แทน.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native ไม่ block self-approval แบบ ruleset)
  - [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
  - [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
  - [KB] Netsuite-Managing Users & Roles (0.6544) — access review/audit guidance (manual)

---

## สรุปเชิงกลยุทธ์สำหรับ public-sector-govt (iCE view)

- **จุดที่ต้องปิด gap จริงก่อน go-live (สูง — วางแผน/จัดงบ):** SoD/GRC ผ่าน certified SuiteApp (NF-SEC-01, GP-FUNC-27, GP-TECH-11, TOR-TECH-05 — ทั้งหมดอยู่ใต้การตรวจ สตง.); CLM ผ่าน SuiteApp (GP-FUNC-11); e-Tax Invoice XML ผ่าน custom/partner (GP-FUNC-16, TOR-FIN-03); grants/fund + capitalization ผ่าน NFP Financials + FAM (F-PRJ-01, TOR-PPM-01).
- **ประเด็น sovereignty ที่ "ควรพิจารณาจริง" (ไม่ใช่ over-spec เสมอ):** data residency/in-country region (NF-ARC-02, GP-TECH-08, GP-STANDOUT-09, TOR-TECH-04) — เป็นข้อได้เปรียบ Oracle ที่ legitimate ถ้าบอร์ดให้น้ำหนัก sovereignty; ต้อง verify ตัวเลือก data center ในประเทศของทั้งสองค่าย (NetSuite ปิด gap นี้ด้วย SuiteApp ไม่ได้). PDPA ไทยไม่บังคับ localization.
- **จุดที่เป็น over-spec / เสี่ยงล็อกสเปก (ป้องกัน NetSuite ได้):** e-auction ในตัว ERP (F-PRC-01, GP-FUNC-09, TOR-PRC-01, GP-STANDOUT-07 — จัดซื้อภาครัฐใช้ e-GP กลาง); on-prem/private deployment (GP-TECH-07); accreditation ภาครัฐสหรัฐฯ FedRAMP (NF-SEC-02).
- **แนวทางจัดซื้อ (procurement):** เขียน requirement แบบ outcome-based ตามภารกิจจริง ไม่ผูกฟีเจอร์เฉพาะผลิตภัณฑ์ — ลดความเสี่ยงถูกท้วงจาก สตง./ผู้ยื่นรายอื่น.
