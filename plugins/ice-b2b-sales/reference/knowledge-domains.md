# KNOWLEDGE DOMAINS — แผนที่ความรู้ 4 ด้านของ solution-knowledge-agent (เทพ)

> **Version:** V01R01 | **Date:** 2026.09.05 | ย้ายมาจาก `solution-knowledge-agent.md` §4 (V03R08) ในงาน Pass 3 ของแผนแก้ทีม agent
> **ไฟล์นี้ใช้ทำอะไร:** เป็นแผนที่ว่าความรู้แต่ละด้านของเทพอยู่ที่ skill หรือโฟลเดอร์ใด และคลังใดมีเงื่อนไขการใช้พิเศษ — เทพเปิดไฟล์นี้ในขั้น E2 (เลือกความรู้) เมื่อตารางเส้นทาง skill ยังไม่ชี้ skill ให้ หรือเมื่องานแตะคลังที่มีเงื่อนไขพิเศษ (คลัง TOR เชิงแข่งขัน · fmcg-practise · ความรู้รายอุตสาหกรรม)
> **ความสัมพันธ์กับตารางเส้นทาง:** "งานแบบไหนต้องโหลด skill อะไร" มีบ้านเดียวคือ `~/.claude/hooks/skill-routing.yaml` — ไฟล์นี้ไม่ซ้ำหน้าที่นั้น แต่บอกว่าในแต่ละ skill มีความรู้อะไร และคลังใดมีกติกาการใช้ที่ต้องอ่านก่อน

## ด้านที่ 1 — product (โหลดตาม primary_product ที่ Pack ล็อก)

| product | ที่อยู่ของความรู้ | หมายเหตุ |
|---|---|---|
| Oracle Fusion Cloud ERP/EPM | skill `oracle-cloud-applications-consulting` | ตารางเส้นทางแถว `product-oracle-cloud` |
| Oracle E-Business Suite | skill `oracle-ebs-consulting` | ตารางเส้นทางแถว `product-ebs` |
| Oracle NetSuite | skill `oracle-netsuite-consulting` (product) + `ice-netsuite-thailand-advisory` (ภาษีและกฎเกณฑ์ไทยบน NetSuite) | ตารางเส้นทางแถว `product-netsuite` · งาน SuiteScript/SDF ลึกมี skill ตระกูล `netsuite-*` (suitescript-records-reference · sdf-project-documentation · sdf-roles-and-permissions · uif-spa-reference · suitescript-upgrade · owasp-secure-coding · ai-connector-instructions) |
| SAP · Microsoft Dynamics · Anaplan · Coupa | ไม่มี skill เฉพาะ — ใช้ความรู้จากการฝึกของ model | เพราะไม่มีแหล่งในเครื่องให้เทียบ ป้ายความเชื่อถือจึงติดได้อย่างมากแค่ PATTERN จนกว่าจะค้นแหล่งจริงได้ ห้ามติด FACT จากความจำ |

ความรู้ที่ด้านนี้ครอบคลุม: แผนที่ module · ความสามารถราย version · fit-gap ระดับ 1 ขึ้นไป · SuiteScript/SDF/API · การประเมิน man-day · architecture

**คลังความรู้ TOR เชิงแข่งขัน (Competitive TOR KB)** — โหลดเฉพาะงาน TOR เชิงแข่งขัน (งานฝัง spec หรืองานแก้ TOR ที่เอียงเข้าคู่แข่ง) ไม่โหลดในงานทั่วไป
- มุม NetSuite: `~/.claude/skills/oracle-netsuite-consulting/references/tor-competitive-kb/` · มุม Fusion: `~/.claude/skills/oracle-cloud-applications-consulting/references/tor-competitive-kb/`
- โครงสร้างในคลัง: `README.md` เป็นดัชนี · `by-industry/<อุตสาหกรรม>.md` ตาม 11 อุตสาหกรรม · `cross-cutting.md` เปิดคู่กับไฟล์อุตสาหกรรมเสมอ · `_AMS-update-workflow.md` คือขั้นตอนเติมข้อมูลรายปี
- **กติกาการใช้คลังนี้อยู่ที่ `_ACCESS.md` และหัวข้อ "หลักการสมดุล" ใน `README.md` ของคลัง — ต้องอ่านก่อนใช้ทุกครั้ง** สาระที่จะพบ: คลังเป็นข้อมูลภายในของ iCE ห้ามคัดลอกเนื้อดิบเข้าเอกสารถึงลูกค้า (ใช้ได้เฉพาะถ้อยคำที่แปลงเป็นเชิงผลลัพธ์แล้ว) · ข้อมูลในคลังคือ TOR เชิงแข่งขันซึ่งมีอคติ จึงต้องดึงคำโต้แย้งและข้อจำกัดมาพร้อมจุดอ่อนเสมอ · การล็อก spec ให้ product เดียวเป็นความเสี่ยงด้านจัดซื้อของลูกค้า (ประเด็นสำนักงานการตรวจเงินแผ่นดิน) เทพต้องเตือนผู้เรียกเมื่อเห็น · ทุก record มี confidence และ citation ของตัวเอง ให้ติดป้าย FACT/PATTERN/ASSUMPTION ตามนั้น

## ด้านที่ 2 — อุตสาหกรรม (vertical)

11 อุตสาหกรรมที่เทพถือความรู้แกนในตัว: BFSI (ธนาคาร ประกัน สถาบันการเงิน) · Manufacturing · Public Sector ไทย · Energy · Retail · Healthcare · Hospitality · Logistics · Telco · Education · Reinsurance — ความรู้ราย deal ที่ทีมสะสมไว้อ่านจาก `/Users/xpickey/Documents/Claude/Portfolio-Insights/vertical-reference-knowledge/`

skill `fmcg-practise` — practice หลายช่องทางของแบรนด์สินค้าอุปโภคบริโภค แฟชั่น ชุดกีฬา อาหาร บนฐาน NetSuite · โหลดเมื่อลูกค้าขายถึงผู้ซื้อมากกว่าหนึ่งเส้นทาง หรือโจทย์เอ่ยคำว่า ฝากขาย (consignment) โมเดิร์นเทรด marketplace ร้านของตัวเอง POS 3PL trade spend หรือปัญหาสต็อกไม่ตรงและกำไรรายช่องทาง · **กติกาการใช้ทั้งหมดอยู่ใน `~/.claude/skills/fmcg-practise/SKILL.md`** — หัวข้อ "Cross-channel invariants" (ข้อที่ตอบได้ทันทีโดยไม่ต้องเปิดไฟล์ย่อย เช่น sale-out มีสองความหมายต้องถามกลับก่อนตอบ · trade spend เป็นส่วนที่ประเมินต่ำที่สุดในดีลค้าปลีก · e-Tax Invoice ไทยไม่บังคับตามกฎหมายแต่ในทางปฏิบัติเลี่ยงแทบไม่ได้) · ตาราง routing ในตัว skill ชี้ไฟล์ย่อย 00–19 · หัวข้อ "Not a customer reference" (ห้ามเอ่ยชื่อลูกค้าต้นทางหรือคู่ค้าของเขา ให้เรียกว่า "แบรนด์แฟชั่นหลายช่องทางที่เทียบเคียงได้" และ skill นี้ไม่มีตัวเลข man-day) · ความสามารถของ product ไปที่ `oracle-netsuite-consulting` ภาษีไทยไปที่ `ice-netsuite-thailand-advisory`

## ด้านที่ 3 — กฎเกณฑ์และกฎหมาย (regulated — โหลดตาม domain ของงาน)

| domain | skill | ตารางเส้นทาง |
|---|---|---|
| สถาบันการเงิน สินเชื่อ ประกัน (IFRS 9 · Basel · NPL) | `fin-tech-consulting` | แถว `product-fintech` |
| ภาครัฐไทย (GFMIS · e-GP · รัฐวิสาหกิจ · ระเบียบพัสดุ) | `govt-egp-gfmis` · `advisor-govt-gfmis` | แถว `govt-thailand` |
| ภาษีไทยและเอกสารตามกฎหมาย (e-Tax Invoice · กรมสรรพากร · ภ.ง.ด. · ภ.พ.) — เฉพาะ "กฎที่กรมสรรพากรกำหนด" · ส่วน "NetSuite รองรับกฎนั้นในไทยอย่างไร" อยู่ `ice-netsuite-thailand-advisory` (ด้านที่ 1) คำถาม e-Tax บน NetSuite เปิดทั้งสองตัว | `th-rd-etax-compliance` | ตารางยังไม่มีแถว — เทพเปิดเองเมื่อโจทย์แตะภาษีไทย |
| ราคาอ้างอิงและ man-day ในตลาดไทย | `th-pricing-reference` | ตารางยังไม่มีในแถว `sales-thinking` — เทพเปิดเองเมื่อต้องประเมิน man-day หรือราคา |

## ด้านที่ 4 — ที่ปรึกษาธุรกิจ (business consulting)

Finance · Procurement · Supply Chain · Manufacturing · As-Is/To-Be · แผนที่จาก pain สู่ product · ROI/NPV/IRR · KPI baseline · PMO (แผนงาน M01–M05 · RACI) — skill: `b2b-strategic-thinking` · `b2b-design-thinking` · `competitor-objection-bank` (ตารางเส้นทางแถว `sales-thinking` ครอบสองตัวแรกและตัวสุดท้ายบางส่วน — `b2b-design-thinking` เทพเปิดเองเมื่อทำ As-Is/To-Be)

## ความรู้ภาษาที่ไม่ใช่ product — skill `pali-language`

ภาษาบาลี (ไวยากรณ์ · paradigm ผันนามและกิริยา · ความหมายศัพท์ · โครงพระไตรปิฎก) — โหลดอัตโนมัติเมื่อพบสัญญาณบาลีตามข้อ 7 ของ `invocation_pattern` ในส่วนหัวไฟล์ agent (บ้านเดียวของกติกานี้) · ไม่อยู่ใต้ Primary Lock เพราะเป็นความรู้ภาษา ไม่ใช่ product · ไม่มีอายุความสด · ตารางเส้นทางยังไม่มีแถว

*reference/knowledge-domains.md | เปิดโดย solution-knowledge-agent ขั้น E2 | ผู้ดูแล: user*
