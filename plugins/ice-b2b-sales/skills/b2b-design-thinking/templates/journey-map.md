# Journey Map Template

A time-sequenced view of how a user (persona or named individual) moves through a process or experience, capturing actions, thoughts, feelings, pain points, and moments of truth. Used for AS-IS and TO-BE analysis.

## When to Use
- Discovery: document the current experience (AS-IS)
- Envisioning: design the aspirational experience (TO-BE)
- Opportunity identification: find high-pain / high-value moments
- Change management: show stakeholders the transformation

## Canvas Structure

Rows (top to bottom):
1. **Stages** — the sequential phases of the journey
2. **Actions** — what the user does at each stage
3. **Touchpoints** — systems, documents, people interacted with
4. **Thoughts** — what they are thinking
5. **Feelings** — emotional arc (plot as curve from frustrated → neutral → delighted)
6. **Pain points** — specific frustrations, delays, rework
7. **Opportunities** — where we can intervene with a better experience
8. **Metrics** — time, cost, quality, satisfaction at each stage

Columns are the sequential stages.

## Stage Framework by Process

### Procure-to-Pay (P2P)
Requisition → Approval → PO Issue → Goods Receipt → Invoice Match → Payment → Reconciliation

### Order-to-Cash (O2C)
Lead → Quote → Order → Fulfillment → Invoice → Collection → Dispute → Revenue Recognition

### Record-to-Report (R2R)
Transaction → Subledger → General Ledger → Close → Consolidation → Reporting → Disclosure

### Hire-to-Retire (H2R)
Requisition → Recruit → Hire → Onboard → Develop → Perform → Compensate → Separate

### Customer Service
Issue Occurs → Search Self-Service → Contact Channel → Authenticate → Diagnose → Resolve → Follow-up → Feedback

### Enterprise Software Sale
Awareness → Consideration → Evaluation → Shortlist → Proposal → Negotiation → Signature → Kickoff → Value Realization → Renewal / Expansion

## Example — Thai SME Invoice Processing AS-IS

| Stage | Receive | Match | Approve | Post | Pay |
|---|---|---|---|---|---|
| Actions | Open email, save PDF | Manually compare to PO | Route to 3 approvers | Key into ERP | Prepare payment file |
| Touchpoints | Gmail, Drive | Excel, PDFs | Line, Email | SAP B1 | Bank portal |
| Thoughts | "Another one?" | "Did we actually order this?" | "Who is OOO?" | "My fingers ache" | "Did I upload the right file?" |
| Feelings | Flat | Frustrated | Anxious | Bored | Nervous |
| Pain | Unstructured data | No 3-way match | Approval lag | Keying errors | Compliance risk |
| Opportunities | OCR | Auto 3-way match | Mobile approval | Direct ERP API | BAHTNET integration |
| Metrics | 5 min/invoice | 15 min/invoice | 3 days avg | 10 min/invoice | 1 day cycle |

Journey total: 5+ days per invoice; error rate 4%; cost per invoice ~฿120.

## TO-BE Overlay Technique

Draw the TO-BE on the same canvas in a different color. For each stage:
- Keep the stage if it is value-adding
- Collapse / eliminate if it is waste
- Automate if it is rules-based
- Delight if it is a moment of truth

## Moments of Truth

Mark stages where the user's emotion swings sharply. These are the highest-leverage moments for investment. Every journey has 2–4 moments of truth — finding them is the main point of this exercise.

## Quality Bar

- Stages are MECE (no gaps, no overlaps)
- Grounded in real observation or interview data
- Emotional curve is plotted, not just described
- Pain points have metrics (time, cost, error rate)
- Opportunities tie to specific solution concepts
- TO-BE is concrete enough to storyboard
