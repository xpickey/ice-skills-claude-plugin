# Example — Thai Government GFMIS Design Sprint

A worked example of applying this skill to a Thai public sector opportunity around GFMIS / e-GP. Discipline: **ST fit (with heavy procurement constraints) → DT design sprint → Why-Now tied to fiscal + regulatory → TOR-aligned proposal**.

## The Situation

**Client:** Thai government ministry (agency of ~4,500 staff)
**Context:** Heavy GFMIS user for budget, procurement (e-GP), and accounting. Facing OAG audit findings related to reconciliation of GFMIS vs. in-agency subsystems, and a policy directive to adopt the Cloud Security Standard 2567. The Permanent Secretary wants a "next-generation" integrated platform on top of GFMIS, deliverable under FY28 budget.
**Ask:** A 3-day design sprint to shape the TOR (Terms of Reference) and produce a concept that will justify budget allocation.

## Step 1 — Strategic Fit Gate (ST)

- **Where-to-Play fit:** yes — Thai public sector with GFMIS integration is ICP.
- **How-to-Win fit:** yes — we have GFMIS integration experience and Cloud Standard 2567 expertise.
- **Pricing envelope:** ฿20–40M (matched to ministry FY28 budget line).
- **Non-goals:** do not compete on lowest-price e-bidding if technical bar drops below our quality floor; do not propose pure cloud infrastructure (DGA-controlled).
- **Regulatory envelope:** Public Procurement Act B.E. 2560, PDPA, Cloud Standard 2567 for CII.

Delegated to:
- `advisor-govt-gfmis` for GFMIS configuration depth
- `govt-egp-gfmis` for procurement law / e-GP technical detail
- `legal-it-thailand-cloud` for PDPA + Cloud Standard 2567

## Step 2 — 3-Day Design Sprint Adaptation

Using `workshops/3day-sprint.md` with public-sector adjustments:
- Decider: the Permanent Secretary (sponsor) — delegated to the Deputy for tactical breaks
- Test users: 5 officers from budget, procurement, accounting, audit liaison, and IT
- Observer: OAG audit representative invited for day 3 validation (critical for audit defensibility)

## Step 3 — Day 1 — Map & Target

### AS-IS journey — Reconciliation between GFMIS and in-agency subsystems
- 20+ manual reconciliation points each month
- Data flows via CSV export / re-keying for 3 subsystems (asset, inventory, personnel)
- Month-end close takes 9 days; OAG queries add 2–3 days
- Audit findings: 3 unresolved reconciliation exceptions from FY25

### Problem target (chosen by Decider end of day 1)
> *"How might we enable audit-defensible monthly reconciliation between GFMIS and agency subsystems within 3 business days, without forcing rework on the GFMIS side?"*

## Step 4 — Day 2 — Sketch & Decide

### Lightning demos
- Private-sector reconciliation platforms
- Other ministries' integration patterns
- DGA-endorsed API frameworks

### Sketches (top 3 after heat-map + supervote)
1. **Integration hub**: iPaaS layer between GFMIS and subsystems with pre-built connectors (on DGA-approved cloud)
2. **AI-assisted reconciliation agent**: agent proposes matches, officer approves (builds on hub)
3. **Audit-evidence automation**: every transaction carries audit metadata from the point of entry

### Supervote decision
Integrated concept combining all three — starting with hub (foundation), layering AI agent and audit automation in phase 2.

### Storyboard (detailed)
14-panel storyboard of officer's reconciliation experience from pain to payoff, ending with OAG audit walk-through showing defensible evidence.

## Step 5 — Day 3 — Prototype & Validate

### Prototype
- Clickable Figma mockup of the officer UI
- Simulated GFMIS data + subsystem data + reconciliation proposals
- Audit evidence pack generated per exception

### User interviews (5 × 45 min)
- Budget officer: "this is where we waste days — a match would save me a week"
- Procurement officer: positive, but asked about e-GP record integration
- Accounting officer: cautiously positive, worried about GFMIS change-management
- Audit liaison: very positive, asked about OAG audit trail retention
- OAG representative: supportive — asked about 7-year retention and tamper-proof logs

### Synthesis
- Strong validation on the hub + audit automation
- Concern: AI agent suggestions need clear override / traceability
- Add: e-GP integration explicitly

### Decision: invest

## Step 6 — Strategic Fit Re-check (ST)

- Fits Where / How.
- Commercial envelope: ฿28–32M for phase 1 (hub + audit automation), ฿10–12M for phase 2 (AI agent with e-GP).
- Capability: in-house GFMIS integration team + 2 Cloud Standard 2567 architects sufficient.
- Procurement path: e-bidding (given deal size); TOR must be crafted from sprint output.
- Go to proposal + TOR drafting.

## Step 7 — Why-Invest / Why-Now / Why-Us

### Narrative version

**Why Invest** — Today the agency spends ~9 days each month reconciling GFMIS vs. three subsystems, accumulating FY25 audit findings and consuming 200+ officer-hours per month. Without action, FY28 IFRS-adjacent requirements and the expanded OAG digital audit scope will increase findings, delay fiscal year closure, and risk administrative sanctions. A 3-day defensible reconciliation saves ~150 hours/month, eliminates material audit findings, and positions the agency as a digital government leader for the FY29 Permanent Secretary review.

**Why Now** — Three windows align. First, FY28 capital budget proposal window closes in Q1 FY27 — miss this and the budget line is forfeit. Second, Cloud Standard 2567 implementation deadlines require CII-grade architecture by end of FY27. Third, the OAG's announced FY28 digital audit methodology requires tamper-proof transaction evidence, which a FY28 H1 delivery can satisfy. Delaying six months means no budget, non-compliant architecture, and another audit cycle with findings.

**Why Us** — We deliver GFMIS integrations for three comparable ministries and hold Cloud Standard 2567 implementation experience. Our senior architect led the GFMIS integration at another agency. Our team is fully Thai, cleared for government work, and fluent in both PDPA and Public Procurement Act requirements. We commit to an e-bidding-aligned fixed-price of ฿28M for phase 1 with 5-year support, with clean TOR-ready documentation. Our governance includes direct OAG audit liaison and quarterly ministry steering reviews.

### Next action
*"We will deliver a draft TOR and budget justification for the FY28 capital budget window within 14 business days to support the ministry's submission to the Budget Bureau."*

## Step 8 — TOR Preparation

The sprint output feeds directly into TOR sections:
- Scope of work (functional requirements from storyboard)
- Technical architecture (integration hub + AI agent + audit module)
- Compliance requirements (Cloud Standard 2567, PDPA)
- Acceptance criteria (3-day reconciliation, tamper-proof audit evidence, OAG approval)
- Delivery timeline (aligned to fiscal year)
- Commercial construct (fixed-price with outcome milestones)

Delegated to `govt-egp-gfmis` for TOR drafting in statutory form.

## Key Lessons

- **Public sector sprints must honor procurement law** — TOR alignment is non-negotiable.
- **OAG observer participation** on validation day turned the concept into audit-defensible design.
- **Why-Now must stack fiscal + regulatory + audit timelines** — government timing is rigid.
- **Cloud Standard 2567 + PDPA as the "price of entry" differentiation** — we pre-solved the compliance problem competitors will stumble on.
- **Delegated deeply to vendor / gov skills** — this skill provides the wrapper, the installed skills provide the depth.
