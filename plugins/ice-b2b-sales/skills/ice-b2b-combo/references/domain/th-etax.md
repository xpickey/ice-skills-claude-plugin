# Domain — Thai Revenue Department / e-Tax Compliance

> overlay ภาษีไทยสำหรับ ERP localization + business case. ใช้เมื่องานแตะ VAT/WHT/e-Tax/บัญชีไทย.
> ใช้ช่วง Solution → Deploy (localization). **เป็น design input ไม่ใช่คำแนะนำภาษีขั้นสุดท้าย** — ยืนยันกับที่ปรึกษาภาษี + ประกาศสรรพากรล่าสุด (ดู `_capabilities/know.md`).

---

## 1. VAT (ภาษีมูลค่าเพิ่ม)

- อัตรา **7%** (ตามประมวลรัษฎากร ม.80 ลดจาก 10% โดยพระราชกฤษฎีกา ขยายเรื่อย ๆ — treat เป็น parameter).
- **0%** — ส่งออก, ขนส่งระหว่างประเทศ, BOI ฯลฯ.
- **ยกเว้น** — สินค้า/บริการเฉพาะ (อาหารพื้นฐาน, การศึกษา, สุขภาพ ม.81).

**แบบยื่น:**
- **ภ.พ.30** — VAT รายเดือน ครบกำหนด **วันที่ 15 ของเดือนถัดไป** (e-filing ขยายถึง 23).
- **ภ.พ.36** — VAT บริการจากต่างประเทศ (reverse-charge).
- **ภ.พ.09** — จดทะเบียน VAT.

## 2. WHT (ภาษีหัก ณ ที่จ่าย)

| แบบ | ใช้กับ |
|---|---|
| **ภงด.1** | เงินเดือน/ค่าจ้าง |
| **ภงด.3** | บุคคลธรรมดา (ค่าบริการ/วิชาชีพ) |
| **ภงด.53** | นิติบุคคล |
| **ภงด.54** | จ่ายต่างประเทศ |
| **ภงด.50/51** | ภาษีเงินได้นิติบุคคลประจำปี/ครึ่งปี |

- ERP ต้องออกหนังสือรับรองหัก ณ ที่จ่าย + ยื่นแบบตามรอบ.
- **อัตรา WHT ต่างกันตามประเภทเงินได้** (ค่าบริการ/วิชาชีพ/ค่าเช่า/ดอกเบี้ย ฯลฯ — มีหลายอัตรา) — **ห้ามตอบอัตราเดียวเหมารวม** (เช่น "WHT 5% ทุกบริการ" = ผิด). ต้องดูประเภทเงินได้ + ประกาศกรมสรรพากร แล้วตั้ง tax code แยกตามอัตรา. ถ้าไม่แน่ใจอัตรา = flag ให้ยืนยัน (ดู `_capabilities/know.md`).

## 3. e-Tax Invoice / e-Receipt

- กรมสรรพากร push e-Tax invoice & e-Receipt — ออก/ส่ง/เก็บแบบอิเล็กทรอนิกส์ + ลายเซ็นดิจิทัล.
- ERP ต้องรองรับ format (XML ตามประกาศกรมสรรพากร) + การส่ง/ลงทะเบียน.
- **ระวัง over-commit:** e-Tax/e-Receipt support บางระบบ (โดยเฉพาะ NetSuite) **ไม่ใช่ feature มาตรฐานครบ** — มักต้อง SuiteApp/partner solution/custom (มีต้นทุนเพิ่ม). **อย่าตอบว่า "รองรับครบในตัว" โดยไม่ยืนยัน** — flag ว่าต้องเช็ค availability + cost (ดู `product/netsuite-thailand.md`).

## 4. ERP requirements (Thai localization)

- **tax determination** ตาม transaction type, supplier/customer status, ship-to/from.
- **Thai CoA** + รายงานภาษี (ภพ.30, รายงานภาษีซื้อ/ขาย).
- **Buddhist Era (พ.ศ.)** — ปฏิทินไทย ในเอกสาร/รายงาน.
- **BAHTNET** — ระบบโอนเงินมูลค่าสูง.

---

## Business case angle

- value: compliance + ลดงานคำนวณภาษี manual + ลดความเสี่ยงปรับ.
- **Why Now ไทย:** e-Tax mandate · เปลี่ยนกฎภาษี · BOI · audit.
- ตัวเลขประหยัด = ต้องอิงจริง (ดู `_capabilities/know.md`) — ไม่กุ.

---

## ข้อควรระวัง

- **อัตรา/กฎ = parameter ไม่ hardcode** — สรรพากรเปลี่ยนได้ (VAT 7% เป็นการขยายชั่วคราว) → ตรวจประกาศล่าสุด (ดู `_capabilities/know.md` staleness).
- localization บางส่วนต้อง SuiteApp/add-on/partner — ยืนยัน availability.
- **ไม่ใช่คำแนะนำภาษี** — design input เท่านั้น ยืนยันกับที่ปรึกษาภาษีลูกค้า.

> ERP ที่ implement → `product/*` · NetSuite ไทย → `product/netsuite-thailand.md` · ภาครัฐ → `domain/govt-egp.md`.
