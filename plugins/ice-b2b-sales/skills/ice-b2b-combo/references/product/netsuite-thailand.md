# Product — NetSuite Thailand / APAC Localization

> ความรู้เฉพาะการ implement NetSuite ให้องค์กรไทย/APAC. ใช้ pre-sales advisory + scoping + business case ลูกค้าไทย.
> **NetSuite core อยู่ที่ `product/netsuite.md`** — ที่นี่เน้นเฉพาะ Thai context. ทุกข้ออ้างกฎ/อัตรา → ตรวจกับแหล่งทางการ (ดู `_capabilities/know.md`).
> ใช้เป็น design input — **ไม่ใช่คำแนะนำภาษี/กฎหมายขั้นสุดท้าย** (ยืนยันกับที่ปรึกษาภาษีลูกค้า + ประกาศกรมสรรพากรล่าสุด).

---

## 1. Currency + Reporting (ไทย)

- **THB** = primary currency ของ Thai subsidiary ใน OneWorld.
- Group reporting มัก USD/parent currency → ตั้ง consolidated currency ที่ parent + FX revaluation รายเดือน.
- **TFRS** converge กับ IFRS เป็นส่วนใหญ่ — แต่ disclosure timing + lease carve-out ต่างสำหรับ SME ภายใต้ **TFRS for NPAEs**. ยืนยันก่อน map CoA ว่าลูกค้ารายงานแบบไหน.

## 2. VAT (ภาษีมูลค่าเพิ่ม)

- อัตรา **7%** (เป็น parameter — อ่าน tax setup ลูกค้า ไม่ hardcode · ดู `domain/th-etax.md`).
- input/output VAT แยกกัน → ตั้ง tax code แยก (input/output/zero-rated).
- รายละเอียดเต็ม VAT/WHT/e-Tax → `domain/th-etax.md`.

## 3. WHT (หัก ณ ที่จ่าย)

- NetSuite จัดการ WHT ผ่าน tax code/custom — ต้องตั้งตามอัตรา ภงด. (ดู `domain/th-etax.md`).
- หนังสือรับรองหัก ณ ที่จ่าย — ออกตามรูปแบบไทย.

## 4. OneWorld topology (ไทย)

- โครงสร้าง subsidiary: parent + Thai entity + entity อื่นใน region.
- พิจารณา: **BOI separation** (กิจการ BOI ต้องแยกบัญชี) · จุดตัด tax/legal entity.
- **Pillar Two readiness** (global minimum tax) สำหรับกลุ่มข้ามชาติ.

## 5. e-Tax Invoice / e-Receipt + localization gaps

- กรมสรรพากร push e-Tax invoice — NetSuite ต้องรองรับการออก/ส่ง (ดู `domain/th-etax.md` รายละเอียด).
- ⚠️ **NetSuite Thai localization ไม่ครบในตัว** — หลายส่วนต้อง **SuiteApp/partner/custom**: e-Tax invoice (XML), หนังสือรับรองหัก ณ ที่จ่าย (WHT cert printing). มีต้นทุนเพิ่ม. **อย่า quote ลูกค้าว่า "รวมในตัวแล้ว"** โดยไม่ยืนยัน availability + cost ก่อน. ส่วนที่มักได้ standard: Buddhist Era dating.

---

## Pre-sales framing (ไทย)

- **business case ใส่ THB** + อิงประโยชน์จริง (compliance + multi-entity + scale).
- **Why Now ไทย:** e-Tax mandate · TFRS · BOI expiry · การขยาย subsidiary · succession (ดู `_shared/why-stack.md`).
- **bilingual artifact** — ระวังฟอนต์ไทย (ดู `_capabilities/build-spec.md` D1-D4).
- ภาครัฐ/SOE → ผูก `domain/govt-egp.md` (จัดซื้อ) · `domain/govt-gfmis.md`.

---

## ข้อควรระวัง

- **อัตราภาษี/กฎหมาย = parameter ไม่ hardcode** — ตรวจกับประกาศล่าสุด (ดู `_capabilities/know.md` staleness).
- localization บางอย่างต้อง SuiteApp/partner solution — ยืนยัน availability ก่อน commit.
- TFRS vs TFRS-NPAEs — ถามก่อน design CoA (กระทบ structure).

> รายละเอียดภาษีไทยเต็ม → `domain/th-etax.md` · NetSuite core → `product/netsuite.md`.
