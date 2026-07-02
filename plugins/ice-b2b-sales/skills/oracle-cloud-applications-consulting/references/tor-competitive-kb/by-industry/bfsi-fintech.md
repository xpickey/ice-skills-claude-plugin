# TOR Competitive KB — bfsi-fintech — Oracle Fusion Standout & TOR Weaponization

---
last_verified: "2026-06-29"
source: "TOR Requirement Bank + Gap Pack v2"
confidence_note: >
  บันทึกนี้สกัดจากชุดร่าง TOR เชิงแข่งขัน (competitive TOR draft) ที่ออกแบบมาเพื่อให้ Oracle Fusion ตอบ Fully
  ในขณะที่คู่แข่ง NetSuite ตอบได้เพียง Partial/No ตามที่ระบุไว้ใน README ต้นทางเอง จึงมิใช่การวิเคราะห์ความต้องการที่เป็นกลาง.
  ทุกระเบียนคงมุมมองถ่วงดุลของ iCE (Second Opinion) ไว้ครบ — ทั้งจุดที่ Oracle Fusion ชนะจริง และข้อเตือนเรื่อง
  การตั้งสเปกเกินจำเป็น (over-spec) หรือความเสี่ยงด้านการจัดซื้อจัดจ้าง (สตง./ผู้ยื่นรายอื่นท้วงติงการล็อกสเปก).
  ระดับ Confidence ของแต่ละระเบียนอิงจากการมีอยู่ของหลักฐาน KB/เอกสารทางการ มิใช่การคาดเดา. ห้ามนำไปใช้เป็น
  ข้อความ TOR จริงโดยไม่ผ่านการปรับให้อิงผลลัพธ์ (outcome-based) ตามภารกิจของหน่วยงานปลายทาง.
  This KB is derived from a competitive TOR draft biased toward Oracle Fusion. It is a SELL-Fusion aid, not a neutral requirements analysis.
ams_review: "yearly — re-verify product positions"
---

> **วิธีใช้ (How to use):** ระเบียนด้านล่างจัดเรียงเพื่อการขาย Oracle Fusion ในกลุ่มอุตสาหกรรม **bfsi-fintech**
> (ธนาคาร ประกันภัย หลักทรัพย์ FinTech สินเชื่อ และองค์กรที่อยู่ภายใต้การตรวจสอบเข้มด้านธรรมาภิบาลการเงิน).
> แต่ละระเบียนให้ (ก) จุดที่ Oracle Fusion โดดเด่นจริง (Standout) (ข) ถ้อยคำ TOR ที่ใช้ตั้งสเปกให้ข้อเสนอที่ยึด
> NetSuite ได้คะแนน Partial/No (TH+EN) และ (ค) ข้อเตือนถ่วงดุลของ iCE เพื่อไม่ให้ตั้งสเปกเกินจำเป็นจนเสี่ยงถูกท้วงติง.
> **หลักสำคัญ:** จุดอ่อน NetSuite หลายข้อปิดได้ด้วย add-on first-party ที่ใช้เอนจิน Oracle เดียวกัน (NSPB=Oracle PBCS,
> NetSuite Account Reconciliation=Oracle Fusion EPM, NSAW=Oracle ADW) — การตัดสิทธิ์ด้วยเกณฑ์ที่ Oracle Fusion เองก็ต้อง
> ซื้อโมดูลแยก จึงต้องเขียนอย่างระมัดระวัง.

---

## NF-SEC-01 — การแบ่งแยกหน้าที่อัตโนมัติ & Access Governance / Automated SoD & access governance

- **Capability (TH):** การแบ่งแยกหน้าที่แบบอัตโนมัติ (Automated Segregation of Duties) พร้อมการกำกับดูแลสิทธิ์เข้าถึงและการบริหารความเสี่ยงในตัว
- **Capability (EN):** Automated SoD, access governance & risk management
- **Domain:** Technical (Security / GRC) · **iCE severity:** สูง (High)

**Oracle Fusion advantage (Standout):**
Oracle Risk Management Cloud โดยเฉพาะ Oracle Advanced Access Controls ให้ engine การแบ่งแยกหน้าที่ (SoD) แบบอัตโนมัติในตัว มาพร้อม ruleset สำเร็จรูปจำนวนมาก (out-of-the-box conflict library) และ continuous controls monitoring ระดับ preventive ที่ตรวจจับและปิดกั้นความขัดแย้งของสิทธิ์แบบต่อเนื่อง โดยไม่ต้องพึ่ง add-on ภายนอก. สำหรับสถาบันการเงิน ประกันภัย และ FinTech ที่อยู่ภายใต้การกำกับของ ธปท./คปภ./ก.ล.ต. และการตรวจสอบภายในที่เข้มงวด นี่คือจุดที่ Oracle Fusion เหนือกว่า NetSuite อย่างชัดเจนเชิงโครงสร้าง เพราะ NetSuite ทำ SoD ได้เพียงแบบ detective (ตรวจย้อนหลังผ่าน saved search/role audit) และต้องเสริมด้วย SuiteApp certified เพื่อให้ได้ automated/continuous controls.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีการแบ่งแยกหน้าที่ (segregation of duties) แบบอัตโนมัติ พร้อมการกำกับดูแลสิทธิ์เข้าถึง (access governance) และการบริหารความเสี่ยง (risk management) ในตัว

**TOR wording (English):**
The solution must provide automated segregation of duties (SoD) with access governance and risk management natively.

**iCE caveat:**
ช่องว่าง "engine SoD อัตโนมัติแบบ native" มีจริงและ Oracle Advanced Access Controls เหนือกว่าชัดเจน — แต่ถ้อยคำเดิมที่ว่า NetSuite "ไม่มี access governance ระดับ audit" นั้นลดทอนความจริง เพราะ NetSuite มี role-based security ละเอียด (permission ต่อ record/feature), เครื่องมือตรวจสิทธิ์ในตัว (Use Searches to Audit Roles, Show Role Permission Differences), Login Audit Trail, 2FA/SSO และผ่าน SOC 1/SOC 2 Type II + ISO 27001 จริง อีกทั้งปิด gap ได้ด้วย SuiteApp certified (Fastpath Assure, Netwrix Strongpoint, SafePaaS) ที่ต้นทุนบริหารจัดการได้. สำหรับ NGO/หน่วยงานประเทศเดียว engine GRC อัตโนมัติระดับ enterprise ถือเป็นส่วนเกิน — ควรเขียนข้อกำหนดแบบอิงผลลัพธ์ (บังคับให้แสดง "การควบคุมความขัดแย้งของสิทธิ์ที่ตรวจสอบได้และรายงานต่อผู้ตรวจสอบ") มากกว่าบังคับคำว่า "native automated engine" ซึ่งเอียงเข้าหา Oracle และเสี่ยงถูก สตง./ผู้ยื่นรายอื่นท้วงว่าล็อกสเปก.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Managing Users & Roles (0.6678) — Use Searches to Audit Roles + Login Audit Trail
  - [KB] Netsuite-Managing Users & Roles (0.6544) — periodic access review/terminated-user revocation
  - [WEB:oracle.com] Oracle Advanced Access Controls Cloud Service datasheet — automated SoD + continuous monitoring + ruleset สำเร็จรูปจำนวนมาก
  - [WEB:suiteapp.com] Fastpath Assure for NetSuite — SoD analysis by user/role/permission (ruleset 125+ conflicts)
  - [WEB:mysuite.tech] Segregation of Duties in NetSuite: where native tools stop

---

## GP-TECH-11 — ควบคุมสิทธิ์ละเอียด & SoD อัตโนมัติ / Fine-grained access & automated SoD controls

- **Capability (TH):** การควบคุมสิทธิ์แบบละเอียด (fine-grained access) พร้อม SoD ควบคุมอัตโนมัติ
- **Capability (EN):** Fine-grained access & automated SoD controls
- **Domain:** Technical (Security / GRC) · **iCE severity:** สูง (High)

**Oracle Fusion advantage (Standout):**
Oracle Risk Management Cloud (Advanced Access Controls) ทำ automated SoD และ continuous controls monitoring (CCM) ได้ในตัว — ตรวจจับความขัดแย้งของสิทธิ์แบบอัตโนมัติต่อเนื่อง ควบคู่กับ fine-grained access ระดับ enterprise. เทียบกับ NetSuite ที่มี fine-grained access จริง (permission view/create/edit/full ต่อ record/feature กว่า 636 รายการ) และ audit ได้ แต่ automated SoD ระดับ ruleset + CCM ต้องเสริม SuiteApp. ในบริบทสถาบันการเงินและ FinTech ที่ต้องพิสูจน์การควบคุมภายในต่อผู้กำกับและผู้สอบบัญชี ความสามารถ CCM แบบ native ของ Oracle Fusion เป็นจุดขายเชิงธรรมาภิบาลที่หนักแน่น.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีการควบคุมสิทธิ์การเข้าถึงแบบละเอียด (fine-grained access control) พร้อมการควบคุมการแบ่งแยกหน้าที่ (Segregation of Duties) แบบอัตโนมัติ และการเฝ้าระวังการควบคุมอย่างต่อเนื่อง (continuous controls monitoring) ในตัว

**TOR wording (English):**
The solution must provide fine-grained access control with automated Segregation of Duties (SoD) controls and built-in continuous controls monitoring.

**iCE caveat:**
Oracle Risk Mgmt และ SAP GRC มี automated SoD/CCM ที่ NetSuite ไม่มี native — จุดนี้จริง แต่คำว่า "NetSuite role-based พื้นฐาน" มองข้ามว่าการคุมสิทธิ์ของ NetSuite ละเอียด (636+ permission) audit ได้ และมี 2FA/TBA/นโยบายรหัสผ่าน อีกทั้ง gap ปิดได้ด้วย add-on (Fastpath Assure, Netwrix Strongpoint, SafePaaS). สำหรับองค์กรที่ไม่ใช่ข้ามชาติขนาดใหญ่ automated continuous SoD เป็นส่วนเสริมที่เกินความจำเป็น — การบังคับ "ในตัว/native" เสี่ยงเป็นการล็อกสเปก ควรตั้งเกณฑ์เป็น "ต้องปิดความขัดแย้งของสิทธิ์ที่พิสูจน์ได้ต่อการตรวจสอบ" และเปิดให้ปิด gap ด้วย certified add-on ได้.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Managing Users & Roles (0.6691) — granular permission structure (636+ permissions)
  - [KB] Netsuite-Authentication Guide — 2FA / token-based auth; Netsuite-Administrator Guide (0.6642) — password policy + SoD monitoring example (PO created by AP)
  - [WEB:oracle.com] Oracle Advanced Access Controls — continuous SoD monitoring
  - [WEB:mysuite.tech] NetSuite SoD native vs add-on boundary (detective not preventive)

---

## TOR-TECH-05 — GRC / การควบคุมสิทธิ์และ SoD อัตโนมัติ (TOR spec) / GRC / automated SoD controls

- **Capability (TH):** การควบคุมสิทธิ์การเข้าถึงแบบละเอียด + SoD อัตโนมัติ + continuous controls monitoring (TOR spec)
- **Capability (EN):** Fine-grained access control with automated SoD checks + built-in continuous controls monitoring (TOR spec)
- **Domain:** Technical (GRC) · **iCE severity:** สูง (High)

**Oracle Fusion advantage (Standout):**
Oracle Risk Management Cloud มี built-in continuous controls monitoring และ automated SoD เชิง preventive (บล็อกการอนุมัติที่ขัดแย้ง เช่น self-approval แบบ ruleset) ในตัว ซึ่งเป็นข้อกำหนดที่ NetSuite ตอบได้เพียง Partial เพราะ native ทำ SoD ได้แค่ detective (saved search/role audit ตรวจ creator=approver) และไม่มี CCM ในตัว. สำหรับสถาบันการเงินและ FinTech ที่ต้องยื่นหลักฐานการควบคุมเชิงป้องกัน (preventive controls) ต่อผู้กำกับ ความสามารถ preventive + CCM แบบ native ทำให้ Oracle Fusion ได้เปรียบเชิง compliance โดยตรง.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีการควบคุมสิทธิ์การเข้าถึงแบบละเอียด พร้อมการตรวจสอบการแบ่งแยกหน้าที่ (Segregation of Duties) อัตโนมัติ และ continuous controls monitoring ในตัว

**TOR wording (English):**
The solution shall provide fine-grained access control with automated Segregation of Duties (SoD) checks and built-in continuous controls monitoring.

**iCE caveat:**
ข้อกำหนด "continuous controls monitoring ในตัว" เป็นช่องว่าง native ที่มีจริง (Oracle/SAP เหนือกว่า) — แต่การบังคับให้มี "ในตัว" คือ over-spec; SoD ที่องค์กรส่วนใหญ่ต้องการจริงทำได้ด้วย NetSuite native (detective) + SuiteApp certified (Fastpath Assure, Netwrix Strongpoint, Greenlight Approvals) ซึ่งเป็น market-standard. fine-grained access เกี่ยวข้องสูง แต่ CCM แบบ native เป็นฟีเจอร์ระดับองค์กรข้ามชาติ มิใช่ความต้องการหลักของหน่วยงานประเทศเดียว — การบังคับคำว่า "built-in/native" เสี่ยงถูกตีความว่าเอียงเข้าหา Oracle. แนะนำเขียนแบบอิงผลลัพธ์ (บังคับให้แสดง preventive SoD ที่ผ่านการตรวจสอบ) และยอมรับการปิด gap ด้วย certified add-on.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:mysuite.tech] NetSuite SoD: detective vs preventive (native ไม่ block self-approval แบบ ruleset)
  - [WEB:oracle.com] Oracle Risk Management Cloud — built-in continuous controls monitoring
  - [WEB:suiteapp.com] Greenlight Approvals / Fastpath Assure — preventive self-approval blocking + automated SoD
  - [KB] Netsuite-Managing Users & Roles (0.6544) — access review/audit guidance (manual)

---

## GP-FUNC-27 — ธรรมาภิบาล ความเสี่ยง และการควบคุม (GRC) / Governance, Risk & Compliance (GRC) / SoD

- **Capability (TH):** การกำกับดูแล ความเสี่ยง และการควบคุม (GRC) / การแบ่งแยกหน้าที่ (SoD)
- **Capability (EN):** Governance, Risk & Compliance (GRC) / SoD
- **Domain:** GRC · **iCE severity:** สูง (High)

**Oracle Fusion advantage (Standout):**
Oracle Fusion (Risk Management Cloud) ได้คะแนนเต็มในการเปรียบเทียบ 3 ทาง (Oracle 5★ · SAP S/4HANA 5★ · NetSuite 2★) โดยมี automated SoD และ controls monitoring ในตัวเป็นแกน — ครอบคลุมการออกแบบ control matrix, การตรวจจับความขัดแย้งของสิทธิ์ และการเฝ้าระวังต่อเนื่องภายในแพลตฟอร์มเดียว. สำหรับกลุ่ม BFSI ที่ต้องยกระดับ GRC ให้ผ่านการตรวจของผู้กำกับและ สตง. ความครบของ Oracle Fusion เป็นข้อได้เปรียบเทียบกับ NetSuite ที่ GRC เป็น umbrella ของ native controls + partner SuiteApp มากกว่าจะเป็น engine ในตัว.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีความสามารถด้านการกำกับดูแล ความเสี่ยง และการควบคุม (Governance, Risk & Compliance) ในตัว รวมถึงการแบ่งแยกหน้าที่ (Segregation of Duties) แบบอัตโนมัติและการเฝ้าระวังการควบคุมอย่างต่อเนื่อง โดยไม่ต้องพึ่งเครื่องมือภายนอก

**TOR wording (English):**
The solution must provide native Governance, Risk & Compliance (GRC) capabilities, including automated Segregation of Duties (SoD) and continuous controls monitoring, without reliance on external tools.

**iCE caveat:**
เรตติ้ง 2★ (Partial) ของ NetSuite สมเหตุผล และ gap automated SoD/CCM เทียบ Oracle/SAP มีจริง — แต่ถ้อยคำ "SoD/role review พื้นฐาน" ลดทอน เพราะ NetSuite มีเครื่องมือ audit role + audit trail native และ ecosystem SoD ที่ certified เต็มที่. continuous controls monitoring ระดับ enterprise ไม่ใช่ความจำเป็นพื้นฐานของหน่วยงานประเทศเดียว. เนื่องจากองค์กรอยู่ใต้การตรวจของ สตง. SoD เป็นข้อกำหนดจริง แต่ควรปิดด้วย SuiteApp certified + control design ได้ — การบังคับ "ในตัว/native โดยไม่พึ่งเครื่องมือภายนอก" เป็น over-spec ที่เอียงเข้าหา Oracle และเสี่ยงถูกท้วงติงเรื่องความเป็นธรรม.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Managing Users & Roles (0.695/0.6678) — role permissions + audit role searches
  - [WEB:oracle.com] Oracle Risk Management Cloud — automated SoD + continuous monitoring

---

## TOR-FIN-02 — การจัดทำงบการเงินรวมหลายระดับ multi-GAAP & ปิดงบตรวจสอบได้ (TOR spec) / Multi-level group consolidation, multi-GAAP, auditable close

- **Capability (TH):** งบการเงินรวมหลายระดับ หลายมาตรฐานบัญชี (multi-GAAP/IFRS) + intercompany elimination + currency translation + การปิดงบอัตโนมัติที่ตรวจสอบได้ (TOR spec)
- **Capability (EN):** Multi-level group consolidation, multi-GAAP/IFRS, intercompany elimination, currency translation & auditable automated close (TOR spec)
- **Domain:** Finance · **iCE severity:** กลาง (Medium)

**Oracle Fusion advantage (Standout):**
Oracle FCCS (Financial Consolidation and Close Cloud) เหนือกว่าในงาน consolidation ซับซ้อน — โครงสร้างการถือหุ้นหลายชั้น, equity pickup/equity method, NCI (ส่วนได้เสียที่ไม่มีอำนาจควบคุม) และงบรวมหลายมาตรฐานพร้อมมุมมอง statutory + management ในระดับ enterprise. สำหรับกลุ่มสถาบันการเงิน/ประกันภัยที่มีบริษัทลูก บริษัทร่วม และ JV จำนวนมากข้ามประเทศ FCCS ให้การปิดงบอัตโนมัติที่ตรวจสอบได้ (auditable close) และ audit trail ในตัว — จุดที่ NetSuite OneWorld ทำได้เพียงระดับ mid-market และต้องซื้อโมดูล NetSuite Account Reconciliation (NSAR) เสริมเพื่อให้ได้ auditable automated close.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องรองรับการจัดทำงบการเงินรวม (group consolidation) หลายระดับ หลายมาตรฐานบัญชี (multi-GAAP/IFRS) พร้อม intercompany elimination, currency translation และ audit trail ของการปิดงบอัตโนมัติ

**TOR wording (English):**
The solution shall support multi-level group consolidation across multiple accounting standards (multi-GAAP/IFRS), including intercompany elimination, currency translation, and an auditable automated financial close.

**iCE caveat:**
ตามตัวอักษรของข้อกำหนด NetSuite ครอบคลุมเกือบครบ: OneWorld (multi-tier consolidation + auto elimination + CTA) และ Multi-Book (multi-GAAP) ทำได้ในตัว — จึงเข้าข่ายใกล้ Fully มากกว่าจะเป็นแค่ Partial. ส่วน "auditable automated close" ต้องเสริม NSAR (ซื้อเพิ่ม) และ NCI/equity method เคสซับซ้อนต้อง SuiteApp/ปรับมือ. หากตีความ "หลายระดับ/หลายมาตรฐาน" เป็น enterprise ซับซ้อนมาก (equity method, NCI, สเกลใหญ่) Oracle FCCS ยังเหนือกว่า — การให้ Partial จึงพอเถียงได้บนขอบ complexity เท่านั้น. สำหรับหน่วยงานที่มีงบรวมหลายกองทุน/หน่วยงาน + IFRS แต่ไม่มีโครงสร้าง FCCS/NCI ซับซ้อน การตั้งบาร์ให้ NetSuite = Partial มีลักษณะล็อกสเปก และต้องนับต้นทุน NSAR add-on ของทั้งสองฝั่งอย่างเป็นธรรม (Oracle เองก็คิดค่าโมดูลนี้แยก).

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates (currency translation)
  - [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — multi-GAAP secondary books
  - [WEB:prnewswire.com] NetSuite Account Reconciliation 2023-06-14 — auditable automated close (add-on)
  - [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier consolidation, auto elimination, CTA + ข้อจำกัด NCI/equity method

---

## GP-FUNC-12 — งบรวมกลุ่มหลายมาตรฐานบัญชี ขนาดใหญ่ / Group consolidation & multi-GAAP at scale

- **Capability (TH):** งบการเงินรวมกลุ่มหลายมาตรฐานบัญชี ระดับขนาดใหญ่ (at scale)
- **Capability (EN):** Group consolidation & multi-GAAP at scale
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล (Negligible)

**Oracle Fusion advantage (Standout):**
ในการเปรียบเทียบ 3 ทาง (Oracle Fusion 5★ · SAP S/4HANA 4★ · NetSuite 3★) Oracle FCCS (สาย Hyperion) นำหน้าทั้งคู่เรื่อง consolidation ซับซ้อน "ขนาดใหญ่/หลาย GAAP/NCI-equity method". สำหรับกลุ่มบริษัทการเงินใหญ่หลายสิบนิติบุคคลข้ามประเทศที่ถือหุ้นบางส่วน ข้อได้เปรียบของ FCCS เรื่อง NCI/equity method และ consolidation ซับซ้อนมีจริงและสำคัญ — NetSuite OneWorld + Multi-Book เพียงพอระดับ mid-market เท่านั้น.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องรองรับการจัดทำงบการเงินรวมกลุ่มขนาดใหญ่ (group consolidation at scale) ที่มีหลายมาตรฐานบัญชี (multi-GAAP) โครงสร้างการถือหุ้นซับซ้อน equity method และการปรับปรุงส่วนได้เสียที่ไม่มีอำนาจควบคุม (NCI) แบบอัตโนมัติในตัว

**TOR wording (English):**
The solution must support group consolidation at scale with multi-GAAP, complex ownership structures, equity-method accounting, and automated non-controlling-interest (NCI) adjustments natively.

**iCE caveat:**
ข้อเปรียบเทียบนี้ค่อนข้างสมดุล (ให้ NetSuite 3/5) — จริงที่ Oracle FCCS นำหน้าเรื่อง consolidation ซับซ้อนขนาดใหญ่ ส่วน OneWorld + Multi-Book เพียงพอระดับ mid-market และทำ consolidation พื้นฐาน + multi-GAAP ได้ในตัว. "group consolidation & multi-GAAP at scale" เกินความจำเป็นของนิติบุคคลเดียว/องค์กรที่ไม่มีกลุ่มบริษัทข้ามประเทศ = over-spec ในบริบท TOR — ควรบังคับก็ต่อเมื่อองค์กรมีโครงสร้างกลุ่มหลายนิติบุคคลข้ามชาติจริง มิฉะนั้นเสี่ยงถูกท้วงเรื่องล็อกสเปก.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — secondary books multi-GAAP
  - [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
  - [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — OneWorld เพียงพอ mid-market แต่จำกัดในเคสซับซ้อน (equity method, complex NCI)

---

## F-EPM-02 — การรวมงบการเงินขั้นสูง / Advanced financial consolidation

- **Capability (TH):** การรวมงบการเงินขั้นสูง (multi-tier ownership %, equity method, matrix consolidation)
- **Capability (EN):** Advanced financial consolidation
- **Domain:** EPM · **iCE severity:** แทบไม่มีผล (Negligible)

**Oracle Fusion advantage (Standout):**
Oracle FCCS รองรับโครงสร้างถือหุ้นหลายชั้น (multi-tier ownership %), equity pickup, matrix consolidation และมุมมอง statutory + management ในตัว — และลงบัญชี/ปรับ NCI อัตโนมัติ ซึ่ง NetSuite OneWorld ไม่ทำให้ (มีเพียงฟิลด์ Ownership% และ minority interest เบื้องต้น แต่ไม่ลงบัญชี NCI/equity method อัตโนมัติ). ในกลุ่มการเงินข้ามชาติที่มี JV/บริษัทร่วมและถือหุ้นบางส่วนจำนวนมาก Oracle FCCS เหนือกว่าชัดเจน เพราะ NetSuite ต้องพึ่ง SuiteApp (เช่น Eide Bailly NCI Module) หรือปรับมือสำหรับ equity method, step acquisition และ fair-value NCI.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องรองรับการรวมงบการเงินที่มีโครงสร้างการถือหุ้นหลายชั้น (multi-tier ownership %), การบันทึกแบบ equity method, การตัดรายการระหว่างกัน (intercompany elimination) อัตโนมัติ และให้รายงานได้ทั้งมุมมอง statutory และ management

**TOR wording (English):**
The solution must support financial consolidation with multi-tier ownership %, equity-method accounting, automated intercompany eliminations, and both statutory and management reporting views.

**iCE caveat:**
NetSuite OneWorld ทำ consolidation หลายชั้น + ตัดรายการระหว่างกันอัตโนมัติ + แปลงค่าเงิน/CTA ได้ และมีฟิลด์ Ownership% — จึงไม่ใช่ทั้ง "ไม่มี ownership%" (ผิด) และไม่ใช่ "ครบในตัว" (เกิน). จุดที่ FCCS เหนือกว่าคือการลงบัญชี NCI/equity method อัตโนมัติ ซึ่งเกี่ยวข้องเฉพาะกลุ่มที่มีโครงสร้างถือหุ้นบางส่วน/JV ซับซ้อนจริง. หน่วยงานที่เป็นนิติบุคคลเดียวไม่มีโครงสร้างถือหุ้นหลายชั้น → ความสามารถระดับ FCCS แทบไม่ได้ใช้ = over-spec; การใส่ใน TOR โดยไม่มี use case เสี่ยงถูกท้วงเรื่องล็อกสเปก.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-General Accounting (consolidation, 0.59) — Intercompany Auto Elimination + consolidated exchange rates
  - [KB] Netsuite-NetSuite OneWorld Guide (consolidation, 0.60) — subsidiary เป็นนิติบุคคล/nexus/base currency
  - [WEB:timdietrich.me] NetSuite Intercompany Transactions & Eliminations — multi-tier hierarchy, auto elimination, CTA, Ownership% พร้อมข้อจำกัด equity method/complex NCI
  - [WEB:suiteapp.com] Eide Bailly NCI Module for Partially-Owned Subsidiaries — ยืนยันว่า NetSuite ไม่ลงบัญชี NCI ถือหุ้นบางส่วนอัตโนมัติ ต้องใช้ SuiteApp

---

## F-EPM-03 — การกระทบยอดบัญชีอัตโนมัติ & Close Orchestration / Automated reconciliation & close

- **Capability (TH):** การกระทบยอดบัญชีอัตโนมัติ (account reconciliation) + transaction matching + การบริหารงานปิดบัญชี (close orchestration)
- **Capability (EN):** Automated reconciliation & close orchestration
- **Domain:** EPM · **iCE severity:** กลาง (Medium)

**Oracle Fusion advantage (Standout):**
Oracle ARCS (Account Reconciliation Cloud) ทำ account reconciliation + transaction matching + close-task orchestration ในตัวบนแพลตฟอร์ม Oracle Fusion EPM — จับคู่รายการปริมาณมาก (ระดับล้านรายการ), เทมเพลตกระทบยอดหลายประเภท (AP/AR/bank/prepaid/accrual/FA/intercompany), audit trail และ close management ครบวงจร. สำหรับสถาบันการเงินและ FinTech ที่มีปริมาณธุรกรรมสูงและต้องปิดงบเร็วภายใต้การกำกับ ความสามารถ transaction matching + close orchestration แบบอัตโนมัติของ Oracle เป็นจุดขายเชิงประสิทธิภาพและ auditability ที่แข็ง — ในขณะที่ฐาน ERP ของ NetSuite มีเพียง period-close checklist + bank reconciliation ต้องซื้อ NetSuite Account Reconciliation (NSAR) เสริม.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีความสามารถกระทบยอดบัญชี (account reconciliation) แบบอัตโนมัติ พร้อมการจับคู่รายการ (transaction matching) และการบริหารงานปิดบัญชี (financial close orchestration) ในตัว

**TOR wording (English):**
The solution must provide automated account reconciliation with transaction matching and financial close-task orchestration natively.

**iCE caveat:**
ตั้งแต่ มิ.ย. 2023 NetSuite ออก NetSuite Account Reconciliation (NSAR) สร้างบน Oracle Fusion EPM (เอนจินเดียวกับ ARCS) — มี transaction matching engine จับคู่ได้ระดับล้านรายการ (สูงสุด ~5 ล้านแถว CSV), เทมเพลตหลายประเภท, audit trail และ close management; ส่วน period close checklist + bank reconciliation มีในฐาน ERP อยู่แล้ว. ช่องว่างเดิมจึงถูกปิด แต่ NSAR เป็นโมดูล add-on ที่ต้องซื้อ/ลิขสิทธิ์เพิ่ม (เช่นเดียวกับ Oracle ARCS ที่คิดค่าโมดูลแยก). สำหรับนิติบุคคลเดียว transaction matching อัตโนมัติระดับล้านรายการเป็น nice-to-have — ควรพิจารณางบ NSAR แต่ไม่ควรตั้งเป็นเงื่อนไขตัดสิทธิ์โดยไม่นับต้นทุน add-on ของทั้งสองฝั่ง.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:prnewswire.com] NetSuite Account Reconciliation announced 2023-06-14 — built on Oracle Fusion EPM, transaction matching engine + reconciliation/close management
  - [WEB:oracle.com] NSAR What's New 2023 — transaction matching export สูงสุด 5,000,000 แถว CSV
  - [KB] Netsuite-General Accounting (reconciliation_close, 0.62) — Period Close Checklist
  - [KB] NETSUITE_FOR_CONSULTANTS (reconciliation_close, 0.63) — Period Close / period lockdown

---

## F-FIN-01 — Multi-GAAP / บัญชีแยกประเภทรอง / Multi-GAAP / secondary ledgers

- **Capability (TH):** Multi-GAAP ด้วยบัญชีแยกประเภทหลัก (primary) + บัญชีแยกประเภทรอง/เพื่อการรายงาน (secondary/reporting ledgers)
- **Capability (EN):** Multi-GAAP / secondary ledgers
- **Domain:** Finance · **iCE severity:** ต่ำ (Low)

**Oracle Fusion advantage (Standout):**
Oracle รองรับ primary ledger + multiple secondary/reporting ledgers พร้อม mapping อัตโนมัติ โดยไม่มีเพดานจำนวนสมุดที่แคบ — ยืดหยุ่นกว่า NetSuite Multi-Book ที่จำกัดสมุดหลัก 1 + สมุดรองสูงสุด 4 (รวม 5 สมุด active) และต้องเปิดผ่าน OneWorld + NetSuite Professional Services เท่านั้น. สำหรับสถาบันการเงินที่ต้องรายงานหลายมาตรฐาน (statutory ไทย + IFRS + management + regulatory/ธปท./คปภ.) พร้อมกันหลายชุด ความยืดหยุ่นของ reporting ledgers ของ Oracle เป็นจุดได้เปรียบเมื่อจำนวนสมุดเกินเพดาน 4 ของ NetSuite.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องรองรับ multi-GAAP ด้วยบัญชีแยกประเภทหลัก (primary) และบัญชีแยกประเภทรอง/เพื่อการรายงาน (secondary/reporting ledgers) หลายชุด พร้อมการ mapping อัตโนมัติ

**TOR wording (English):**
The solution must support multi-GAAP via a primary ledger and multiple secondary/reporting ledgers with automated mapping.

**iCE caveat:**
NetSuite Full Multi-Book Accounting รองรับสมุดหลัก 1 + สมุดรองสูงสุด 4 (รวม 5 สมุด active) แต่ละชุดต่างมาตรฐานได้ (US GAAP/IFRS/tax/management) พร้อมกฎ mapping ผังบัญชีและปรับค่าเงินรายสมุด → ตรงกับ "primary + secondary ledgers + auto mapping" จริง แต่ยืดหยุ่นน้อยกว่าเมื่อจำเป็นต้องมีสมุดจำนวนมาก. หน่วยงานส่วนใหญ่ต้องการสมุดหลัก (statutory ไทย) + อาจ 1 สมุด IFRS/บริหาร ซึ่งอยู่ในเพดาน 4 สมุดสบาย — การตั้งสเปกเน้น "หลายชุดไม่จำกัด" เกินความจำเป็นสำหรับองค์กรที่ไม่ต้องการสมุดจำนวนมาก และเสี่ยงเอียงเข้าหา Oracle.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Multi-Book Accounting (multibook_secondary, 0.71) — Full/Adjustment-Only secondary books, OneWorld only, multiple sets of records จาก transaction เดียว
  - [WEB:docs.oracle.com] Planning for Multi-Book Accounting — สูงสุด 4 secondary books (รวม 5 active books), ต่าง COA/currency/accounting rules
  - [WEB:netsuite.com] Multi-Book Accounting — COA mapping rules ต่อมาตรฐาน

---

## GP-FUNC-17 — บัญชีสัญญาเช่า IFRS16/ASC842 ในตัว / Lease accounting (IFRS16 / ASC842)

- **Capability (TH):** บัญชีสัญญาเช่า (IFRS 16 / ASC 842) แบบ native
- **Capability (EN):** Lease accounting (IFRS16 / ASC842) native
- **Domain:** Finance · **iCE severity:** กลาง (Medium)

**Oracle Fusion advantage (Standout):**
Oracle Fusion มี native lease accounting รองรับ IFRS 16 / ASC 842 ในตัว (operating/finance lease, right-of-use asset, amortization schedule, journal อัตโนมัติ) โดยไม่ต้องติดตั้งโมดูลเสริมแยก. เทียบกับ NetSuite ที่ต้องใช้ Fixed Assets Management (FAM) SuiteApp ซึ่งเป็น add-on ต้องติดตั้ง/ตั้งค่าและโดยทั่วไปมีค่า license แยก. สำหรับสถาบันการเงิน/ประกันภัยที่มีพอร์ตสัญญาเช่าอาคารสาขาและอุปกรณ์จำนวนมากภายใต้ TFRS 16 การมี lease accounting ในตัวลดความซับซ้อนของ close และ audit.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีการบัญชีสัญญาเช่า (lease accounting) ตามมาตรฐาน IFRS 16 / ASC 842 แบบ native ในตัว รองรับ operating/finance lease, right-of-use asset, ตารางค่าตัดจำหน่าย และการลงบัญชีอัตโนมัติ โดยไม่ต้องใช้โมดูลเสริมหรือ third-party add-on

**TOR wording (English):**
The solution must provide native lease accounting compliant with IFRS 16 / ASC 842 (operating/finance lease, right-of-use asset, amortization schedules, automated journals) without any add-on module or third-party tool.

**iCE caveat:**
Lease Accounting อยู่ในโมดูล Fixed Assets Management (FAM) SuiteApp ของ NetSuite เอง (first-party) รองรับ IFRS 16/ASC 842 ครบ (operating/finance lease, amortization, journal อัตโนมัติ) และใช้ Multi-Book ทำ ASC 842 + IFRS 16 พร้อมกันได้ — จึงไม่ใช่ "ทำแทบไม่ได้" ตามที่คะแนน 1★ สื่อ. แต่ต้องยอมรับตรง ๆ ว่า FAM เป็น add-on มีต้นทุน license + งาน implement ไม่ใช่ของฟรีติดมาใน core. การบังคับคำว่า "native โดยไม่ใช้โมดูลเสริม" เป็นการตั้งบาร์ที่ตัด NetSuite ด้วยเส้นแบ่ง "add-on vs native" ทั้งที่ FAM เป็น first-party ของ NetSuite เอง — ควรเขียนอิงผลลัพธ์ (บังคับการปฏิบัติตาม TFRS 16 ที่ตรวจสอบได้) แทน.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Fixed Assets Management (0.551, Lease Accounting)
  - [WEB:docs.oracle.com] Fixed Assets Lease Accounting (IFRS 16/ASC 842)
  - [WEB:netsuite.com] Lease Accounting Changes: ASC 842 & IFRS 16; NetLease by Netgain = third-party add-on สำหรับพอร์ตซับซ้อน

---

## TOR-FIN-04 — โมดูลบริหารเงินสดและเงินทุน Treasury (TOR spec) / Treasury & cash / bank-risk management

- **Capability (TH):** โมดูลบริหารเงินสดและเงินทุน (Treasury & Cash Management) ในตัว — cash position, bank reconciliation อัตโนมัติ, in-house bank, FX risk management (TOR spec)
- **Capability (EN):** Native Treasury & Cash Management — cash positioning, automated bank reconciliation, in-house banking, FX risk management (TOR spec)
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล (Negligible)

**Oracle Fusion advantage (Standout):**
Oracle Fusion มีความสามารถด้าน treasury/cash management ครบกว่า NetSuite — ครอบคลุม cash positioning, bank reconciliation, และเชื่อมกับ treasury workflows ในตัว ในขณะที่ NetSuite ไม่มี full Treasury Management System (ไม่มี in-house banking, FX/interest hedging, portfolio management แบบ native) และต้องต่อ TMS ภายนอกเช่น Kyriba. สำหรับสถาบันการเงินหรือกลุ่มที่มีการบริหารสภาพคล่องและความเสี่ยงอัตราแลกเปลี่ยนเชิงรุก ความครบของ Oracle/SAP TRM เป็นจุดขายจริง.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีโมดูลบริหารเงินสดและเงินทุน (Treasury & Cash Management) ในตัว รองรับ cash position, bank reconciliation อัตโนมัติ, in-house bank และการบริหารความเสี่ยงอัตราแลกเปลี่ยน (FX risk management)

**TOR wording (English):**
The solution shall include a native Treasury & Cash Management module supporting cash positioning, automated bank reconciliation, in-house banking, and FX risk management.

**iCE caveat:**
การให้ NetSuite ตอบ "No" ผิด — 2 ใน 4 ข้อย่อย (cash position แบบ real-time, automated bank reconciliation ผ่าน Bank Feeds/intelligent matching ซึ่งเป็น first-party ของ NetSuite) ทำได้ในตัว. ที่ขาดจริงคือ in-house banking + FX risk management/hedging ซึ่งเป็น treasury ระดับองค์กรข้ามชาติ. องค์กรที่บริหารเงินสกุลเดียว (เช่น THB) และไม่มี hedging portfolio แทบไม่มี use case → in-house bank/FX hedge เป็น over-spec. การมัดรวม 4 ข้อย่อยแล้วบังคับ "ในตัว" ตัด NetSuite ด้วยส่วนที่องค์กรไม่ได้ใช้ ควรแยกข้อกำหนดที่จำเป็นจริง (cash + bank rec) ออกจากส่วน enterprise treasury.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [WEB:netsuite.com] NetSuite Cash Management Software (automated bank reconciliation)
  - [WEB:houseblend.io] NetSuite Treasury — no native FX hedging/in-house banking (secondary)
  - [KB] Netsuite-Financial Statements Guide (0.5453, Cash Flow Statement)

---

## GP-FUNC-14 — บริหารเงินสด/เงินทุน Treasury / Treasury & cash / bank-risk management

- **Capability (TH):** บริหารเงินสด/เงินทุน (Treasury) และ bank-risk management
- **Capability (EN):** Treasury & cash / bank-risk management
- **Domain:** Finance · **iCE severity:** แทบไม่มีผล (Negligible)

**Oracle Fusion advantage (Standout):**
ในการเปรียบเทียบ 3 ทาง (SAP S/4HANA 5★ · Oracle Fusion 4★ · NetSuite 1★) Oracle Fusion มี treasury/cash management ในตัวเหนือกว่า NetSuite ที่ไม่มี treasury module เต็มรูป (ไม่มี FX/interest hedging, in-house banking, portfolio management). SAP TRM ลึกที่สุด แต่ Oracle Fusion ยังเหนือ NetSuite ชัดเจนในงานบริหารสภาพคล่องและความเสี่ยงทางการเงินระดับองค์กร — เป็นจุดขายสำหรับกลุ่ม BFSI ที่ต้องการ treasury เชิงลึก.

**TOR wording to weaponize (ภาษาไทย):**
ระบบต้องมีความสามารถบริหารเงินสดและเงินทุน (Treasury) ในตัว ครอบคลุม cash positioning แบบ real-time, การบริหารความเสี่ยงอัตราแลกเปลี่ยน/อัตราดอกเบี้ย (FX/interest hedging), in-house banking และการบริหารพอร์ตการลงทุน

**TOR wording (English):**
The solution must provide native treasury capabilities including real-time cash positioning, FX/interest-rate hedging, in-house banking, and investment portfolio management.

**iCE caveat:**
การให้ 1★ พร้อมระบุ "ไม่มี treasury module" เกินจริง — งาน cash positioning + bank reconciliation ที่ใช้จริง NetSuite ทำได้ในตัว (Cash Management: cash position real-time, intelligent matching + Bank Feeds SuiteApp ฟรี, payment/bank account management). ที่ขาดคือ treasury ระดับองค์กรข้ามชาติ (hedging/in-house bank/portfolio) ที่องค์กรสกุลเงินเดียวแทบไม่ใช้. cash/bank rec เกี่ยวข้องและ NetSuite มีแล้ว; hedging/in-house bank เป็น over-spec — การบังคับทั้งชุดตัด NetSuite ด้วยส่วนที่ไม่มี use case จริง.

- **Confidence:** high
- **หลักฐาน / Citation:**
  - [KB] Netsuite-Financial Statements Guide (0.5694, Cash Statement)
  - [WEB:netsuite.com] What is NetSuite Cash Management Software
  - [WEB:houseblend.io] Kyriba vs NetSuite Treasury — no native FX hedging/in-house bank (secondary)

---

## สรุปเชิงกลยุทธ์ (Positioning Summary) — bfsi-fintech

จาก 12 ระเบียนในกลุ่ม bfsi-fintech จุดที่ Oracle Fusion **ได้เปรียบแท้จริง (severity สูง)** และควรใช้เป็นแกน TOR คือ **ธรรมาภิบาลการเงิน/GRC/SoD** (NF-SEC-01, GP-TECH-11, TOR-TECH-05, GP-FUNC-27) — Oracle Risk Management Cloud มี automated preventive SoD + continuous controls monitoring ในตัว ซึ่ง NetSuite ทำได้เพียง detective + certified SuiteApp. สี่ระเบียนนี้เป็น "ประเด็นควรพิจารณาจริง" ตามความเห็นถ่วงดุลของ iCE เพราะองค์กรที่อยู่ใต้การตรวจของ สตง./ผู้กำกับต้องพิสูจน์การควบคุมภายในได้.

ระเบียนกลุ่ม **consolidation, treasury, lease, multi-GAAP** (F-EPM-02, F-EPM-03, F-FIN-01, GP-FUNC-12, GP-FUNC-14, GP-FUNC-17, TOR-FIN-02, TOR-FIN-04) ส่วนใหญ่มี severity **กลาง/ต่ำ/แทบไม่มีผล** เพราะ NetSuite ปิด gap ได้ด้วย first-party add-on ที่ใช้เอนจิน Oracle เดียวกัน (NSPB, NSAR บน Oracle Fusion EPM, FAM SuiteApp) — การตั้งสเปกบังคับ "native โดยไม่ใช้ add-on" จึงตัด NetSuite ด้วยมาตรฐานที่ Oracle Fusion เองก็คิดค่าโมดูลแยก (FCCS/ARCS) และเสี่ยงถูกท้วงเรื่องล็อกสเปก. ใช้เมื่อองค์กรมีโครงสร้างกลุ่มบริษัทข้ามชาติ/JV/treasury เชิงรุกจริงเท่านั้น.

**หลักการจัดซื้อจัดจ้าง (procurement fairness):** เพื่อลดความเสี่ยงถูกท้วงติงจาก สตง. หรือผู้ยื่นรายอื่น ให้เขียน requirement แบบอิงผลลัพธ์ (outcome-based) ตามภารกิจจริง มิใช่ผูกกับฟีเจอร์เฉพาะผลิตภัณฑ์ — และเมื่อเทียบต้นทุน (TCO) ต้องนับค่าโมดูล add-on ของทั้งสองฝั่งอย่างเป็นธรรม.
