# Example — Oracle Cloud Fusion Envisioning Workshop

A worked example showing how this skill wraps around a typical Oracle Cloud ERP / EPM / SCM opportunity. Discipline sequence: **ST gate → DT envisioning → ST fit check → Why-Invest/Now/Us → Proposal**.

## The Situation

**Client:** Thai mid-market manufacturing conglomerate (฿8B revenue, 4 subsidiaries, listed on SET)
**Context:** Running Oracle EBS R12.2 for 11 years. CFO has raised concerns about close time (14 days), audit findings on manual reconciliations, and IFRS 9 / BOI compliance exposure. CEO has signaled "cloud-first" for FY28 budget.
**Ask:** Our firm is shortlisted to propose the migration path. The first touchpoint is a half-day envisioning workshop with CFO, CIO, and 5 business leaders.

## Step 1 — Strategic Fit Gate (ST)

Before scheduling the workshop, we run a 60-minute internal check:
- **Where-to-Play fit:** yes — Thai mid-market manufacturing is ICP.
- **How-to-Win fit:** yes — fixed-price, BOI-defensible methodology is our differentiator.
- **Pricing envelope:** ฿30–60M for full-scope Fusion migration.
- **Non-goals:** do not propose RISE with SAP; do not compete on price alone.
- **Horizon tag:** H2 (building) — this account could be a flagship reference.

Decision: proceed with the workshop; expected deal value supports full engagement.

## Step 2 — Pre-Workshop Prep

- 1-on-1 pre-interviews with CFO (45 min) and CIO (45 min)
- Pre-read (2 pages): market context, ECC-vs-Oracle comparison, Thai references
- Pre-work: each attendee sends top 2 pain points and 1 aspiration
- Stakeholder intelligence: recent annual report, CEO letter on digital priorities
- Delegate to `oracle-cloud-applications-consulting` skill for Fusion configuration depth as needed

## Step 3 — Half-Day Envisioning Workshop

Using the `workshops/halfday-envisioning.md` kit.

### Discovery block
- AS-IS journey map for **monthly close**: 14-day cycle, 3 subsidiaries on 3 ledgers, 40% of time on manual reconciliations, 20% on currency remeasurement
- Moments of truth: day 10 when subsidiaries submit, day 13 when auditors ask for supporting schedules
- Pain voted highest: "the week before close, everyone is yelling at everyone else"

### Problem framing
- POV: *"The CFO of a Thai listed manufacturer needs to close in 5 days and pass IFRS 9 audit without adding headcount, because a late close or audit finding can delay the FY28 BOI certification renewal."*
- Top 3 HMWs:
  - HMW reduce close from 14 days to 5 days?
  - HMW pre-empt auditor questions at the point of entry?
  - HMW unify 3 subsidiary ledgers without forcing each BU onto the same processes?

### Ideation
- Crazy 8s per HMW → 40+ ideas
- Analogous: "how does a bank close overnight?" → surfaced continuous accounting
- Tech-forward: "what would AI exception handling do?" → Oracle AI Agents for auto-reconciliation

### Convergence
- Impact-effort matrix → top 3 concepts:
  1. **Fusion Cloud ERP multi-book consolidation** (Big Bet, 18-month program)
  2. **Continuous accounting + AI exception handler** (Quick Win on Fusion, unlocks the big bet)
  3. **BOI / IFRS 9 automated disclosure pack** (Accelerator, reusable)

### Value case draft
- Why Invest: 14-day → 5-day close saves ~2,000 person-hours / month; audit risk reduction; BOI-defensible
- Why Now: EBS 12.2 extended support sunset; IFRS 9 mandate; FY28 budget window
- Why Us: Oracle Cloud Elite partner, 4 comparable Thai references, fixed-price commitment, Thai senior team

## Step 4 — Strategic Fit Re-check (ST)

After the workshop, before proposal drafting:
- Does the concept still fit Where / How? YES — this is our sweet spot.
- Commercial envelope fits: estimated ฿40–45M for the full program.
- Capability check: Thai Oracle Fusion consultants sufficient; IFRS 9 / BOI accelerator exists.
- Go to proposal.

## Step 5 — Why-Invest / Why-Now / Why-Us

Using `templates/why-invest-why-now-why-us.md`.

### Narrative version (proposal body)

**Why Invest** — The monthly close today runs 14 days, consumes 2,000 person-hours, and still produces audit findings. In 12 months, without change, the IFRS 9 adoption will add 3–5 additional days to close, pushing year-end reporting past SET listing deadlines. In 24 months, a missed BOI renewal would cost the Group ฿80M in corporate tax relief. A 5-day close, clean audit, and BOI-defensible process is worth ฿120M over three years — before counting strategic option value from unified analytics.

**Why Now** — Three windows are closing in FY27. (1) Oracle EBS 12.2 extended support sunset — after that, upgrades and patches become premium-priced and limited. (2) IFRS 9 expected credit loss mandates for Thai listed companies — your auditors will want evidence in the FY28 audit. (3) The FY28 BOI privilege renewal — late or qualified audits jeopardize the renewal. Delaying six months means missing the migration window against FY28 fiscal year close.

**Why Us** — We are Oracle Cloud Elite certified with four comparable Thai listed manufacturing migrations delivered on time and within budget. Our Thai team is led by a partner who served as CFO at a comparable SET-listed company before joining our practice. Our fixed-price commitment of ฿42M includes the IFRS 9 accelerator and BOI disclosure templates that we have pre-built for Thai regulation. We commit to a 5-day close by month 9 post-go-live, backed by outcome-linked fees.

### Next action
*"We propose a Solution Design Confirmation session with your CFO and CIO within 3 weeks to pressure-test the program structure and confirm the investment envelope for FY28 capex approval."*

## Step 6 — Orchestration Delegations

For detailed configuration, we delegate:
- Fusion Cloud module design, close automation setup → `oracle-cloud-applications-consulting`
- EBS-to-Fusion migration path specifics → `oracle-ebs-consulting`
- Legal / data residency / PDPA for cloud migration → `legal-it-thailand-cloud`
- Sales strategy, deal pursuit, account plan → `b2b-enterprise-sale-strategy`
- Pipeline reporting → `sales-pipeline-report`

This skill (`b2b-design-thinking-skill`) owns the DT envisioning, the ST fit gates, and the Why-Invest/Now/Us narrative.

## Key Lessons

- **Strategic fit gate before AND after** discovery prevents pulling into an unprofitable deal.
- **AS-IS journey is the unlock** — the client's own story of their process is more persuasive than any slide we bring.
- **Why-Now grounded in regulation and fiscal windows** is far more potent than "digital transformation is happening".
- **Delegate vendor-specific detail** to the Oracle skill; this skill stays in the DT/ST/value-case lane.
