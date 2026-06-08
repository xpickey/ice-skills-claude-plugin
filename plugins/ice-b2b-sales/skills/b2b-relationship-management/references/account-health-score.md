# Account Health Score & Risk Assessment — Reference

The account health score is the early-warning system that prevents Red surprises. It is a composite indicator that combines hard data (product usage, support volume, financial signals, contract status) with soft signals (executive sentiment, stakeholder turnover, NPS).

The point of the score is not the number — it is the **playbook the number triggers**.

## Composite Score Components

Six components, each scored 0–100, weighted to produce an overall score.

| Component | Weight | What it measures | Source signals |
|---|---|---|---|
| **Product Adoption** | 20% | Are they actually using what they bought? | Active users vs. licensed; module utilization; feature depth; key workflow execution rate |
| **Value Realization** | 25% | Are the promised business outcomes happening? | Pre-sale business case actuals; ROI tracking; documented quantified value (see `value-realization-tracking.md`) |
| **Executive Sentiment** | 15% | Does the senior sponsor still care? | EBR attendance; executive call frequency; named-sponsor stability; sponsor-initiated outreach |
| **Operational Health** | 15% | Are day-to-day operations smooth? | Support ticket volume / severity / age; SLA compliance; escalation frequency; CSAT / NPS |
| **Commercial Health** | 15% | Is the contractual / financial relationship healthy? | Days-to-pay; AMS renewal track record; contract concentration; expansion booked vs. plan |
| **Relationship Coverage** | 10% | Do we have multi-threaded, current relationships? | Number of active relationships; coverage of buying committee; days since last meaningful touch on each |

Weights are starting defaults. Tune for the customer (e.g., for a Thai government SOE in year 1 of an implementation, increase Operational Health to 25% and decrease Value Realization to 15%).

## Four-State Classification

| State | Score range | Meaning | Required action |
|---|---|---|---|
| **Green** | 80–100 | Healthy. Relationship is durable and growing. | Continue normal cadence. Look for advocacy / expansion plays. |
| **Yellow** | 65–79 | One or two components are weak. Watching. | KAM-led action plan within 30 days. No leadership escalation yet. |
| **Orange** | 50–64 | Material risk. Multiple components weak or one critical component (Exec Sentiment / Value Realization) at <40. | Sales-Leader involvement. 60-day formal recovery plan. Internal monthly review. |
| **Red** | <50 | At-risk of churn, escalation, or loss of strategic status. | Executive war-room governance. Recovery plan within 14 days (see `escalation-recovery.md`). Weekly review. |

Movement between states is itself a signal. An account dropping from Green to Yellow with no clear cause is a stronger early-warning than a Yellow that has been stable for two quarters.

## Critical Single Signals (Override the Composite)

Some signals are severe enough to override the weighted score and trigger immediate Orange or Red regardless of other components:

- **Executive sponsor exits** the customer org → Orange minimum until replacement sponsor confirmed
- **Champion exits** → Yellow minimum, Orange if account is single-threaded
- **Executive escalation** lodged formally → Orange minimum until resolution
- **Reference rescinded** or refusal to take a reference call → Orange
- **RFP issued for a category we already serve** → Red (we are being put on notice)
- **Late payment >60 days with no explanation** → Orange
- **AMS / subscription renewal notice not signed within 60 days of expiry** → Orange
- **Public statement** of dissatisfaction (analyst quote, conference comment, peer reference) → Red
- **Competitor announced as displacing us** in any module → Red

## Refresh Cadence

| Account tier | Refresh frequency | Reviewer |
|---|---|---|
| Tier-1 Strategic | Monthly | KAM + Sales Leader |
| Tier-2 Key | Quarterly | KAM |
| Tier-3 Growth | Quarterly | KAM |
| Any account in Yellow / Orange / Red | Weekly until back in Green for 2 consecutive cycles | KAM + Sales Leader (Orange/Red) |

Trigger-event refresh (regardless of cadence): leadership change, support escalation, contract event, public news, sponsor change.

## Health Score → Playbook

The score's value is the action it triggers.

### Green Playbook
- Confirm advocacy posture: reference-readiness, case-study willingness, advisory board interest
- Identify expansion white-space using `renewal-expansion-motion.md`
- Schedule next QBR / EBR per `engagement-cadence-qbr-ebr.md`
- Test the relationship: ask for a small favor (intro, panel speaker, beta participation) — healthy accounts say yes

### Yellow Playbook
- KAM diagnosis: which component(s) drove the drop? What specific event(s)?
- 30-day action plan: 3–5 specific actions with named owners and dates
- Notify Sales Leader (informational, no escalation)
- Adjust cadence: extra working-level touches between scheduled QBRs
- Re-score in 30 days

### Orange Playbook
- Sales-Leader-led 60-day recovery plan
- Direct outreach to Executive Sponsor (ours → theirs)
- Root-cause documentation: what specifically broke and what we are doing about it
- Formal communication to customer: "we hear you, here is what we are doing, here is the timeline"
- Internal monthly review with delivery, CS, finance
- Re-score weekly

### Red Playbook
- Executive war-room governance — see `escalation-recovery.md`
- 14-day recovery plan with executive sponsorship on both sides
- Daily standup internally for the first 2 weeks
- Customer-facing weekly status with named owners and concrete progress
- Consider: dedicated resources, fee adjustments, executive site visit, board-level acknowledgment
- Decision point at day 60: meaningful recovery? If not, plan a graceful exit that preserves the option to return

## Cultural Calibration (Thai)

- Yellow / Orange / Red status is **never** communicated to the customer in those terms — it is internal language
- Hard truths to the customer go in private 1:1 with the senior sponsor, not in a multi-stakeholder meeting (see `thai-cultural-overlay.md`)
- "We have a problem" framing is fine; "you have a problem" framing is not
- For Thai government / SOE: a Red status often has political dimensions on the customer side that we do not fully see — over-index on listening, under-index on prescribing

## Common Failure Modes

- Scoring the customer's *behavior* instead of the *relationship's health* (the customer can be busy, distracted, or reorganizing without us being in trouble)
- Optimism bias — KAMs over-rate relationships they own; Sales Leader spot-check is essential
- Treating the score as a report instead of a trigger — score with no action plan is theater
- Refreshing too rarely — a quarterly score on a deteriorating account misses the window to recover
- Letting Operational Health (support tickets) dominate when Executive Sentiment is the actual problem

## Output Format

Use `assets/account-health-scorecard.md` as the starting template. Render as a one-pager that fits on a single screen for monthly review.
