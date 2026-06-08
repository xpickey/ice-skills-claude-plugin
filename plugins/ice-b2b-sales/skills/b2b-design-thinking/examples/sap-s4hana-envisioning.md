# Example — SAP S/4HANA RISE Envisioning with AppHaus Style

A worked example of using this skill for a SAP-stack opportunity. Discipline sequence: **ST gate → DT (AppHaus-styled) envisioning → ST fit → Proposal**.

## The Situation

**Client:** Thai food & beverage group (฿15B revenue, 6 business units, export-heavy)
**Context:** Running SAP ECC 6.0 since 2014 with extensive customizations in MM, FI, and CO. ECC support ends 2027. The CIO wants to evaluate RISE with SAP vs. S/4HANA on-prem vs. staying on ECC with extended support.
**Ask:** Our firm is one of three SAP Platinum partners invited to run a 1-day envisioning workshop to shape the client's RFP.

## Step 1 — Strategic Fit Gate (ST)

- **Where-to-Play fit:** yes — Thai large enterprise manufacturing / F&B is ICP.
- **How-to-Win fit:** yes — we have a "Clean Core" migration methodology and 3 Thai F&B references.
- **Pricing envelope:** ฿80–150M for RISE migration + BTP extensions.
- **Non-goals:** do not propose re-implementation on ECC; do not compete primarily on price.
- **Horizon tag:** H2 (anchor account for S/4HANA practice).

Decision: proceed; this is a lighthouse opportunity.

## Step 2 — AppHaus Workshop Structure

SAP pre-sales typically uses the **AppHaus method** — DT-informed envisioning with SAP-specific framing. We adopt its structure:

- **Explore** — stakeholder landscape, current state, pain
- **Discover** — personas, journeys, HMWs
- **Design** — ideate, storyboard, prioritize
- **Deliver** — value case, roadmap, commitments

## Step 3 — 1-Day Ideation Workshop

Using `workshops/1day-ideation.md` adapted with AppHaus language.

### Discovery block
- AS-IS journey for **order-to-cash (export channel)**: 9 days from PO receipt to invoice clearance, 3% error rate on customs documentation, 2-week currency remeasurement cycle
- AS-IS journey for **procure-to-pay (local + import)**: 21-day cycle, 15% of invoices in exception, manual 3-way match
- Moments of truth: export customs clearance (revenue recognition risk), vendor payment week (cash-flow risk)

### Problem framing
- POV: *"The Group CFO of a Thai F&B exporter needs a closed, audit-ready book by day 7 and visibility of working capital in near real time, because exchange-rate swings and export customs delays can move quarterly EPS by ±8%."*
- Top HMWs:
  - HMW close books by day 7 with multi-BU, multi-currency complexity?
  - HMW automate export customs documentation integration with SAP GTS / customs portal?
  - HMW use Joule / BTP agentic workflows to resolve invoice exceptions automatically?

### Ideation
- Crazy 8s produced 45 ideas
- Tech-forward HMW tied to SAP Joule and Build Process Automation
- Analogous: Vietnamese and Malaysian F&B exporter patterns shared

### Convergence (impact-effort)
- **Quick Wins:** BTP Build Apps for customs tracking; pre-built localization accelerators; consolidated close templates
- **Big Bets:** RISE with SAP migration with Clean Core; Joule-powered intelligent close; export GTS integration
- **Fill-ins:** Fiori UX tweaks, mobile approvals
- **Killed:** custom ABAP enhancements in ECC to "bridge" (Money Pit)

### Storyboards (3 concepts)
1. RISE with SAP + Clean Core — 18-month program
2. BTP-layered AI intelligent close — phased extension on top of core
3. Joule agentic invoice exception handler — pilot in 90 days on top of BTP

### Value case
- Close: 13 days → 7 days
- Export O2C: 9 days → 5 days
- Exception auto-resolution: 40% of invoices
- Currency remeasurement: 2 weeks → 2 days
- Aggregate value: ~฿180M over 3 years (working capital release + labor efficiency + risk reduction)

## Step 4 — Strategic Fit Re-check (ST)

- Still fits Where / How — large Thai F&B is our sweet spot.
- Commercial envelope: ฿110–130M for RISE + BTP + Joule phase 1.
- Capability: Thai SAP S/4HANA team of 8 consultants + BTP specialists in Bangkok. Gap: Joule hands-on experience — fill with a Singapore partner.
- Go to proposal.

## Step 5 — Why-Invest / Why-Now / Why-Us

### Narrative version

**Why Invest** — Today, close runs 13 days across 6 BUs; customs exceptions on export orders cost 3% in rework; currency remeasurement swings EPS by ±8%. In 12 months, without action, ECC 6 will be on extended support at premium cost and Joule / AI advantages will be unavailable on the legacy core. In 24 months, a RISE migration under pressure — forced by the 2027 sunset — will cost 1.5–2x of a planned migration. The modernized environment unlocks ~฿180M of value over 3 years through faster close, release of working capital, and intelligent exception handling.

**Why Now** — Three forces align to FY27 H2. First, SAP ECC mainstream support ends December 2027; every quarter of delay narrows the migration window. Second, SAP's RISE commercial construct is most favorable under current promotion terms ending at the FY26 year-end SAP fiscal. Third, your FY28 strategic plan commits to regional export expansion — the new core must be in place before that volume hits. A planned migration starting FY27 Q2 completes safely ahead of the sunset; later, and it becomes a fire drill.

**Why Us** — We are a SAP Platinum partner with S/4HANA RISE certified consultants in Bangkok. We have delivered three comparable Thai F&B migrations, two with export complexity similar to yours. Our "Clean Core" methodology has been published in SAP's Thai reference materials. We commit to a fixed-scope, fixed-price anchor of ฿110M for the RISE migration, with the BTP Joule intelligent-close pilot delivered in months 6–9 at risk-share pricing tied to 30% exception auto-resolution. Our Thai senior partner previously led SAP practice for a SET-listed F&B group — we speak your operational language.

### Next action
*"We propose a Solution Design Confirmation session within 2 weeks to pressure-test the program shape and align the RFP so it cleanly maps to the architecture we have envisioned together."*

## Step 6 — Orchestration Delegations

- SAP S/4HANA configuration depth, BTP architecture → external SAP practice skill (not in installed set; engage SAP partner directly)
- Legal / data residency → `legal-it-thailand-cloud`
- Sales strategy → `b2b-enterprise-sale-strategy`
- Account plan, pipeline → `sales-pipeline-report`, `sales:*`

## Key Lessons

- **AppHaus structure** gives SAP customers a familiar vocabulary and increases proposal-to-win rate.
- **Clean Core** is the defining theme — most customers have extensive customizations that block upgrade.
- **BTP + Joule as extension story** makes the value case punchier than core migration alone.
- **Why-Now tied to support sunset + commercial window + internal expansion plan** makes the timing case irrefutable.
