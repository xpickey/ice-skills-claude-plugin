# Domain — GFMIS (ระบบบริหารการเงินการคลังภาครัฐไทย)

> overlay สำหรับงานขายภาครัฐไทยที่เกี่ยว GFMIS. ใช้เมื่อลูกค้าเป็นส่วนราชการ/รัฐวิสาหกิจที่ผูกระบบการเงินภาครัฐ.
> ใช้ช่วง Qualify → Solution. ทุกข้ออ้างกฎหมาย/ระเบียบ → ตรวจแหล่งทางการ (ดู `_capabilities/know.md`).

---

## 1. GFMIS คืออะไร

**GFMIS** = Government Fiscal Management Information System — ระบบบริหารการเงินการคลังภาครัฐอิเล็กทรอนิกส์ บริหารโดย **กรมบัญชีกลาง (CGD)**.

**วัตถุประสงค์หลัก:**
- ควบคุมงบประมาณแบบรวมศูนย์ (centralized budget control).
- มาตรฐานบัญชีภาครัฐ — **Accrual-based IPSAS**.
- รายงาน online real-time.
- จ่ายตรงเจ้าหนี้/ผู้รับประโยชน์ (direct payment).
- โปร่งใส ตรวจสอบได้ (สตง.).

---

## 2. GFMIS vs ERP (จุดสำคัญงานขาย)

| มิติ | GFMIS | ERP เอกชน |
|---|---|---|
| เจ้าของ | กรมบัญชีกลาง (ส่วนกลาง) | องค์กรเอง |
| ขอบเขต | budget/payment/accounting ภาครัฐ | ครบ business process |
| มาตรฐาน | IPSAS / ระเบียบราชการ | TFRS/IFRS |
| integration | หน่วยงานต้องเชื่อม GFMIS | — |

**ประเด็นขาย:** หน่วยงานที่มี ERP เอง ต้อง **integrate กับ GFMIS** (ไม่ใช่แทน) — positioning คือ ERP เสริม GFMIS ไม่ใช่แข่ง.

> ⚠️ **อย่า hallucinate ว่า "ERP แทน GFMIS" หรือ "รวมรายงานเป็นหนึ่งเดียว":** GFMIS ใช้ **IPSAS (บัญชีภาครัฐ)** · ERP ของหน่วยงาน/SOE ใช้ **TFRS (บัญชีพาณิชย์)** — **คนละมาตรฐาน รันคู่ขนาน** ไม่ใช่ระบบเดียว. ERP feed ข้อมูล GL เข้า interface GFMIS — ไม่ได้แทนที่. ตอบผิดเรื่องนี้ = เสียเครดิตทันทีกับลูกค้าภาครัฐ.

---

## 3. กรอบกฎหมายที่เกี่ยว

```
พรบ.วินัยการเงินการคลัง 2561
  └─ พรบ.วิธีการงบประมาณ 2561
      └─ พรบ.การจัดซื้อจัดจ้างฯ 2560  → ดู domain/govt-egp.md
```

- การจัดซื้อระบบ IT ภาครัฐ = ตามระเบียบจัดซื้อ (e-GP) — ดู `domain/govt-egp.md`.
- IT Service Provider ต้องเข้าใจ TOR/contract ภาครัฐ.

---

## Why Now (ภาครัฐ triggers)

- **GFMIS rollout/upgrade** — รอบปรับปรุงระบบกลาง.
- **พรบ.งบประมาณ / นโยบายรัฐ** — บังคับมาตรฐานใหม่.
- **audit (สตง.)** — ความโปร่งใส/ตรวจสอบได้.
- **digital government** — นโยบายรัฐบาลดิจิทัล.

---

## Pre-sales (ภาครัฐ)

- **วงจรยาว 12-18 เดือน** ผูกปีงบประมาณ (ต.ค.-ก.ย.).
- **TOR เป็นหัวใจ** — comply ทุกข้อ + honest (ดู `_capabilities/check.md` D9) · ดู `domain/govt-egp.md`.
- **สตง. sensitivity** — ข้อเสนอต้อง defensible, ตรวจสอบได้.
- relationship + hierarchy (ดู `_shared/thai-calibration.md`).

> ระบบ ERP ที่ integrate GFMIS → `product/oracle-cloud.md` / `product/oracle-ebs.md` · จัดซื้อ → `domain/govt-egp.md`.
