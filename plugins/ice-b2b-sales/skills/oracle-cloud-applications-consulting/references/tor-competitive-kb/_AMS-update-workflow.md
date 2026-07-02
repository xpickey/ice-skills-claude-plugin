# AMS Yearly Update Workflow — TOR Competitive KB

**Owner:** iCE AMS / Pre-sales knowledge team · **Cadence:** yearly (or on a major Oracle Fusion / NetSuite release wave) · **Scope:** `references/tor-competitive-kb/by-industry/*.md`

> **เจตนา / Purpose:** ตำแหน่งผลิตภัณฑ์เปลี่ยนทุกปี — NetSuite ปิด gap ด้วยฟีเจอร์/SuiteApp ใหม่ และ Oracle Fusion ออกความสามารถใหม่ทุกไตรมาส. คลังนี้จะ "เชื่อถือได้" ก็ต่อเมื่อมีการทบทวนประจำปี. This workflow keeps every record current: re-verify product positions, refresh `last_verified` + `confidence`, append new gaps, and retire gaps the competitor has closed.

---

## 0. Before you start / เตรียมตัว

- **Source-of-truth for the year:** latest **Oracle Fusion Cloud release readiness / What's New** notes, latest **NetSuite release notes** (two waves/yr) + **suiteapp.com** for certified SuiteApps, and the internal NetSuite KB (Qdrant). Cross-check analyst notes only as secondary.
- **Do not invent.** If a claim has no citation after review, it stays `low` confidence and gets a `[ต้อง verify / verify]` flag — never upgrade confidence on a hunch (ANTI-HALLUCINATION).
- **Keep the anonymization.** Never write the source client's real name. Generalize to *healthcare / blood-bank / non-profit foundation / public-sector*.
- **Keep the balance.** Every record must retain its **iCE caveat** (first-party add-on cover / over-spec / procurement-fairness). A record with only the Fusion win and no caveat is incomplete.

---

## 1. Re-verify each record's product position / ทบทวนตำแหน่งผลิตภัณฑ์

For every record in a vertical file, walk the four checks:

| # | Check / ตรวจ | Action |
|---|---|---|
| a | **Fusion side still true?** | Confirm the Oracle Fusion "Standout" still holds in the current release. If Fusion moved it into a different module or renamed it, update the wording. |
| b | **NetSuite closed it?** | Check NetSuite release notes + suiteapp.com. If NetSuite added a native feature or a certified SuiteApp now covers the gap, this record may need the **"gap closed"** flag (§4). |
| c | **Add-on cover changed?** | Re-check the first-party add-on mapping (NSPB / NetSuite Account Reconciliation / NSAW / NSPCM). If the add-on parity changed, update the iCE caveat. |
| d | **Still relevant to the vertical?** | If the capability became over-spec (or newly relevant) for that industry, adjust `iCE severity` and note why. |

---

## 2. Update `last_verified`, `confidence`, and severity / อัปเดตวันที่และความเชื่อมั่น

- **`last_verified`** (file front matter): set to the review date, `YYYY-MM-DD`.
- **Per-record `Confidence`:** re-map from evidence on file this year — `high` (≥1 official Oracle/NetSuite Help or vendor citation), `medium` (mixed / partner-blog / verify-flagged), `low` (no citation). Confidence may go **down** as well as up.
- **`iCE severity`:** keep to the four-value scale — **สูง / กลาง / ต่ำ / แทบไม่มีผล**. Change only with a one-line reason in the caveat.
- **Front matter `ams_review`:** keep the `"yearly — re-verify product positions"` marker.

---

## 3. Append new records / เพิ่มระเบียนใหม่

1. Pick the **correct vertical file** (or `cross-cutting.md` for a platform/technical gap). Healthcare / blood-bank / non-profit gaps go into the existing **`by-industry/healthcare-public-sector.md`** — an industry-vertical file, which is allowed and already anonymized — plus **`cross-cutting.md`** for any platform-level gap. (An industry-vertical-named file is correct; only a *client*-named file is forbidden.)
2. Assign a **new ID** following the existing prefix scheme: `F-*` (TOR bank functional), `NF-*` (TOR bank non-functional), `GP-FUNC-*` / `GP-TECH-*` / `GP-STANDOUT-*` (gap pack), `TOR-*` (TOR spec). Use the next free number in that family; never reuse an ID.
3. Fill the record using the **template in §6**.
4. Update this KB's **README index table** (`README.md` §3): bump the record count and re-tally the severity mix for that file.

---

## 4. Flag closed gaps / ระบุ gap ที่ถูกปิดแล้ว

When a competitor closes a gap, **do not delete the record** — mark it, so we never re-weaponize a stale claim in a live bid.

- Prepend the record title with **`[GAP CLOSED YYYY]`** and set `iCE severity` toward **แทบไม่มีผล** if the gap is no longer usable.
- Add a `Gap-closed note:` line stating what closed it (NetSuite release / SuiteApp name) and the evidence.
- Keep the original text below it for audit history.

Example header after closure:
```
## GP-FUNC-17 — [GAP CLOSED 2027] Lease accounting (IFRS16 / ASC842)
- Gap-closed note (2027-03): NetSuite native Lease Accounting GA'd in 2026.2; certified for IFRS16/ASC842. Was iCE severity กลาง → now แทบไม่มีผล. Do not use as a TOR gate.
```

---

## 5. Finish the review / ปิดงานทบทวน

- Update every touched file's `last_verified`.
- Re-tally and update the **README §3 index** (record counts + severity columns) so it matches disk.
- Log a one-line changelog entry (date, files touched, records added / closed / re-graded).
- If any record moved to `[GAP CLOSED]`, note it so sales stop pitching it.

---

## 6. Template for a NEW record / แม่แบบระเบียนใหม่

Copy this block into the correct `by-industry/*.md` file. Keep both languages. **The `iCE caveat` and `Confidence` lines are mandatory — a record without them is not review-complete.**

```markdown
## <NEW-ID> — <Capability title EN> / <หัวข้อภาษาไทย>

- **Capability (TH):** <ความสามารถโดยย่อ ภาษาไทย>
- **Capability (EN):** <capability in one line>
- **Domain:** <Finance | SCM | Manufacturing | Procurement | Project | HCM | Quality | GRC | Technical | ...> · **iCE severity:** <สูง | กลาง | ต่ำ | แทบไม่มีผล> (<High|Medium|Low|Negligible>)

**Oracle Fusion advantage (Standout):**
<Where Oracle Fusion genuinely out-classes NetSuite (and, if from the gap pack, the 3-way vs SAP S/4HANA). State the module/product name and the concrete capability. TH or EN as source dictates.>

**TOR wording to weaponize (ภาษาไทย):**
<ถ้อยคำ TOR ภาษาไทย — พร้อมวาง>

**TOR wording (English):**
<paste-ready English TOR clause>

**iCE caveat:**
<MANDATORY balanced counter. State which of the three patterns applies: (a) first-party add-on cover — name the module (NSPB / NetSuite Account Reconciliation / NSAW / NSPCM / certified SuiteApp); (b) over-spec / not-applicable for a single-entity Thai non-profit or public body; (c) procurement-fairness / spec-lock risk under สตง. audit. Recommend the outcome-based rewrite where relevant.>

- **Confidence:** <high | medium | low>   <!-- high = ≥1 official Oracle/NetSuite Help or vendor citation on file; low = no citation, treat as claim + [ต้อง verify] -->
- **last_verified (record):** <YYYY-MM-DD>
- **Source:** <TOR Requirement Bank | Gap Pack — functional/technical/standout/torspec | new-<year> intake>
```

---

*Run yearly. When done, `last_verified` on every touched file and the README §3 index must agree with what is on disk. Do not strip caveats. Do not name the client.*

---

## Backlog — improvements deferred from 2026-06-29 team review / รายการปรับปรุงที่เลื่อนไว้

รายการเหล่านี้ผ่าน review แล้วว่า **ไม่ block การใช้งาน** (should/nice-to-have) — ทำในรอบ AMS ถัดไป:

- **[SHOULD] SoD/duplicate-record canonical pointer** — `cross-cutting.md` เก็บ SoD เป็น 3 เรคคอร์ดใกล้เคียง (NF-SEC-01 / GP-FUNC-27 / GP-TECH-11). เพิ่มบรรทัด "CANONICAL: weaponize จาก GP-FUNC-27; NF-SEC-01/GP-TECH-11 = cross-cut view" กัน paste ซ้ำ 2 เวอร์ชัน.
- **[SHOULD] manufacturing.md process-mfg prose** — ปรับถ้อยคำ STANDOUT ให้ตรง rating gap_pack (Fusion 4★ vs SAP 5★): Fusion นำ NetSuite ด้าน native process/mixed-mode + batch genealogy จริง แต่ GMP electronic batch record + potency ระดับลึกสุด SAP PP-PI ยังเหนือกว่า (caveat + confidence medium ในเรคคอร์ดถูกต้องแล้ว — แค่ prose-tightening).
- **[NICE] per-record "safe-to-lift" flag** — เพิ่มป้าย HONEST-KNOCKOUT vs CREDIBILITY-DIFFERENTIATOR-DO-NOT-LOCK ต่อเรคคอร์ด กัน junior rep lock spec ผิดจาก severity ต่ำ.
