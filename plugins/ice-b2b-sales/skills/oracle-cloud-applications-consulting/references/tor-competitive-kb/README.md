# TOR Competitive KB — Oracle Fusion Standout & TOR Weaponization

**Internal competitive-intelligence knowledge base for iCE Consulting** · Effective 2026-06-29 · Review cadence: yearly (AMS)

> **หนึ่งบรรทัดสรุป / One-line summary:** คลังความรู้เชิงแข่งขันที่ชี้ว่า **Oracle Fusion Cloud** เหนือกว่า **NetSuite** ตรงไหน แปลงเป็น **ถ้อยคำ TOR (TH+EN)** ที่ตั้งสเปกได้ พร้อม **ข้อเตือนถ่วงดุลของ iCE** ทุกระเบียน — a sell-side competitive KB that maps where Oracle Fusion out-classes NetSuite, converts each gap into paste-ready TOR wording (TH+EN), and preserves iCE's balanced counter-view on every record.

---

## 1. What this KB is / คลังนี้คืออะไร

**TH —** คลังนี้สกัดจากสองแหล่ง: (1) **TOR Requirement Bank** (จุดอ่อน NetSuite เทียบ Oracle Fusion พร้อมถ้อยคำ TOR ที่ใช้ตั้งสเปก) และ (2) **Gap Pack** (การเทียบ 3 ทาง NetSuite vs Oracle Fusion vs SAP S/4HANA — เชิงฟังก์ชัน เชิงเทคนิค จุดเด่น Fusion และ TOR spec). เจตนาคือช่วยทีมขาย/พรีเซล **ตั้งสเปก TOR ให้ Oracle Fusion ตอบ Fully ในขณะที่ข้อเสนอที่ยึด NetSuite ตอบได้เพียง Partial/No**.

**EN —** This is a **sell-Fusion aid**, not a neutral requirements analysis. The source is a **competitive TOR draft deliberately biased toward Oracle Fusion**. Use it to shape TOR wording that a NetSuite-based bid scores Partial/No against — while staying inside the fairness guardrails below.

### The non-negotiable balance rule (from `second_opinion.txt`)

Every record keeps **both** the Fusion gap **and** the iCE counter-view. Do not strip the caveat. The three counter-patterns iCE has verified are:

1. **First-party add-on cover / มี add-on ปิดได้** — many "gaps" close with NetSuite first-party modules running the **same Oracle engine**: **NSPB** = Oracle PBCS/EPBCS, **NetSuite Account Reconciliation** = Oracle Fusion EPM, **NSAW** = Oracle ADW + Analytics Cloud, **NSPCM** = profitability/costing. Disqualifying NetSuite on a criterion that Oracle Fusion itself charges as a separate module is not a fair comparison — it is a TCO question, not a capability gap.
2. **Over-spec / not-applicable / ตั้งสเปกเกิน** — "plant-grade / multi-country" capabilities (full process manufacturing, APS, S&OP/IBP, multi-country global payroll, TMS, global trade, MDM, EAM) are usually irrelevant to a single-entity Thai non-profit / public-sector body. Mandating them in a TOR reads as spec-locking.
3. **Procurement-fairness risk / เสี่ยงถูกท้วงติง** — locking a TOR to one product's feature name is legally risky under **สตง.**-style audit and open to challenge by other bidders. Write **outcome-based** requirements tied to the buyer's real mission, not to a product-specific feature.

### Client-anonymization rule (enforced)

The raw source referenced a specific healthcare / blood-bank / non-profit foundation and a serum-and-vaccine production unit. **These names never appear in this KB.** They are generalized to industry patterns: *healthcare / blood-bank / non-profit foundation / public-sector*. Keep it that way in every reuse.

---

## 2. How this KB is organized / โครงสร้าง

```
tor-competitive-kb/
├── README.md                 ← this file (what/how/index/query)
├── _AMS-update-workflow.md    ← yearly re-verify + append workflow (AMS team)
├── _ACCESS.md                 ← internal-only handling + procurement-fairness note
└── by-industry/               ← records grouped by iCE industry vertical
    ├── bfsi-fintech.md
    ├── cross-cutting.md        ← platform/technical gaps that span all verticals
    ├── education.md
    ├── energy-utilities.md
    ├── healthcare-public-sector.md
    ├── logistics.md
    ├── manufacturing.md
    ├── public-sector-govt.md
    └── trading-services.md
```

**Taxonomy = the 11 iCE industry verticals** (`bfsi-fintech`, `telco`, `manufacturing`, `retail-distribution`, `healthcare-public-sector`, `energy-utilities`, `public-sector-govt`, `logistics`, `hospitality`, `education`, `trading-services`) **plus `cross-cutting`** for platform/technical gaps that apply everywhere.

> **สำคัญ / Important — the `healthcare-public-sector` file.** The original source is a healthcare / blood-bank / non-profit case. Its records live in a dedicated industry-vertical file, **`by-industry/healthcare-public-sector.md`** — an *industry-pattern* file, **not** a client-shaped one, so it honors the anonymization rule (no client name appears anywhere in it). **When you serve a healthcare / blood-bank / non-profit / public-body buyer, read `by-industry/healthcare-public-sector.md` + `cross-cutting.md` together** — the vertical file is PRIMARY, and `public-sector-govt.md` adds government-procurement / e-GP / สตง. / statutory-tax specifics on top when the buyer is also a public body. No `telco`, `retail-distribution`, or `hospitality` file was written — the source mapping produced no records anchored to those verticals.

### Record anatomy (every entry in a by-industry file)

Each record is a `## <ID> — <title>` section carrying:
- **Capability (TH / EN)** — what the capability is, both languages.
- **Domain · iCE severity** — one of **สูง / กลาง / ต่ำ / แทบไม่มีผล** (High / Medium / Low / Negligible).
- **Oracle Fusion advantage (Standout)** — where Fusion genuinely wins.
- **TOR wording to weaponize (TH + EN)** — paste-ready spec language.
- **iCE caveat** — the balanced counter (add-on cover / over-spec / fairness risk). **Never delete.**
- **Confidence** — `high` (≥1 official Oracle/NetSuite Help or vendor citation on file) / `medium` (mixed / partner-blog / verify-flagged) / `low` (no citation on file — treat as claim, verify before bid).

Per-file YAML front matter carries `last_verified`, `source`, `confidence_note`, and `ams_review`.

---

## 3. Index / สารบัญไฟล์ที่มีจริง

Only files that were actually written are listed. Record counts and severity mix are read directly from the files (as of `last_verified: 2026-06-29`).

| Vertical file | Records | สูง (High) | กลาง (Med) | ต่ำ (Low) | แทบไม่มีผล (Negl.) | Top-severity focus |
|---|---:|---:|---:|---:|---:|---|
| `by-industry/healthcare-public-sector.md` | **44** | **16** | 14 | 12 | 1 | ไฟล์แกนกลางของ dataset — severity เข้มข้น (process/GMP mfg, QMS, data residency, SoD, EAM, PPM/grants) |
| `by-industry/public-sector-govt.md` | 16 | **11** | 3 | 1 | 1 | Data residency/sovereignty, GRC/SoD, process/GMP mfg, quality/CAPA — the sharpest public-body wins |
| `by-industry/cross-cutting.md` | 51 | **11** | 1 | 20 | 19 | Platform/technical gaps spanning all verticals (residency, SoD, iPaaS, analytics, AI, MDM) |
| `by-industry/manufacturing.md` | 19 | **5** | 2 | 6 | 6 | Process / mixed-mode mfg (recipe, batch, GMP), quality management (QMS/CAPA) |
| `by-industry/bfsi-fintech.md` | 12 | **4** | 3 | 1 | 4 | Automated SoD/GRC, consolidation, close orchestration, multi-GAAP |
| `by-industry/trading-services.md` | 13 | 1 | 2 | 4 | 6 | Sourcing/CLM, supplier lifecycle, statutory localization |
| `by-industry/logistics.md` | 8 | 0 | 3 | 3 | 2 | WMS directed operations, demand planning |
| `by-industry/energy-utilities.md` | 3 | 0 | 2 | 1 | — | Enterprise asset management (EAM) & maintenance |
| `by-industry/education.md` | 2 | 0 | 0 | 2 | 0 | HCM/Talent (recruiting→performance→learning→succession) — differentiate, do not over-spec |

**Totals: 9 files · 171 record-views** (underlying unique ~101 ids — many requirements appear in more than one vertical). No file was written for `telco`, `retail-distribution`, or `hospitality` (see §2 note).

**Reading the severity mix:** a file heavy in **สูง (High)** carries genuine knock-out clauses; a file heavy in **แทบไม่มีผล (Negligible)** is mostly over-spec you should *not* weaponize as a mandatory gate — use those as credibility color, and expect the iCE caveat to say "do not spec-lock."

---

## 4. How to query / วิธีเรียกใช้ในงานจริง

**Rule of thumb — always open the vertical file _plus_ `cross-cutting.md`.** Vertical files hold industry-specific functional gaps; `cross-cutting.md` holds the platform/technical gaps (residency, SoD, iPaaS, analytics, AI) that apply to every deal.

| ผู้ใช้ขอ / User asks for | เปิดไฟล์ / Open |
|---|---|
| **Healthcare / blood-bank / non-profit / hospital / foundation TOR** | `by-industry/healthcare-public-sector.md` **+** `by-industry/cross-cutting.md` (the vertical file is the anonymized home of the source case; add `public-sector-govt.md` if the buyer is also a public body) |
| Government / SOE / รัฐวิสาหกิจ TOR | `by-industry/public-sector-govt.md` + `cross-cutting.md` |
| Bank / insurance / securities / FinTech / lending | `by-industry/bfsi-fintech.md` + `cross-cutting.md` |
| Manufacturer (process, GMP, batch, quality) | `by-industry/manufacturing.md` + `cross-cutting.md` |
| Trading / distribution / services (sourcing, CLM, supplier) | `by-industry/trading-services.md` + `cross-cutting.md` |
| Logistics / 3PL / warehouse | `by-industry/logistics.md` + `cross-cutting.md` |
| Energy / utilities (asset-heavy, EAM) | `by-industry/energy-utilities.md` + `cross-cutting.md` |
| University / college / institute / training body | `by-industry/education.md` + `cross-cutting.md` |
| Pure platform / technical differentiators (any deal) | `by-industry/cross-cutting.md` |
| `telco` / `retail-distribution` / `hospitality` | No dedicated file — use `cross-cutting.md` and the nearest functional analog; do not invent records |

### Workflow inside a TOR / proposal task

1. **Filter by severity first.** Lead with **สูง (High)** records — those are the real, defensible Fusion wins. Treat **แทบไม่มีผล (Negligible)** as color, not as mandatory gates.
2. **Check Confidence.** For any record you will put in a live bid, prefer `high`. Flag `low`/`medium` and verify against the latest release notes before committing (see `_AMS-update-workflow.md`).
3. **Read the iCE caveat before you paste.** If the caveat says "over-spec" or "spec-lock risk," rewrite the TOR line as **outcome-based** — describe the *result the buyer needs*, not a product-specific feature name.
4. **Anonymize.** Never reintroduce the source client's real name. Keep the industry-pattern phrasing.
5. **Customer-facing = derived wording only.** Only the neutral, outcome-based TOR wording may reach the customer. The competitor-weakness analysis and iCE caveats are **internal** (see `_ACCESS.md`).

### Related iCE assets

- Objection handling → skill `competitor-objection-bank`
- NetSuite counter-positioning / TH advisory → skill `ice-netsuite-thailand-advisory`, `oracle-netsuite-consulting`
- Fusion delivery methodology → this skill (`oracle-cloud-applications-consulting`)
- Live TOR/proposal build → route via `iCE-Compass-Next` (กัปตัน)

**🔗 Paired KB (opposite angle — same requirement IDs).** This KB is the **Oracle Fusion angle (standout + weaponize)**.
For the **NetSuite angle (weakness + counter/defense)** of the *same* requirement IDs (F-EPM-01, GP-FUNC-27, etc. — IDs are
shared across both KBs) → open `oracle-netsuite-consulting/references/tor-competitive-kb/by-industry/<vertical>.md`.
Pull **attack + defense for one ID in a single move**: Fusion-side (this file) = how to spec so NetSuite fails ·
NetSuite-side = how to rebut / close the gap. Use whichever matches the product you are selling.

---

*Maintained under the yearly AMS review cadence — see `_AMS-update-workflow.md`. Internal handling rules — see `_ACCESS.md`.*
