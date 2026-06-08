# Stakeholder & Power Mapping — Reference

Gartner's research now puts the average B2B buying committee at **6–10 decision-makers**. In enterprise software at Thai enterprise / government scale, the real number is often 12–20 once you include influencers, gatekeepers, and the regulatory-ecosystem actors. Mapping them is not optional.

A power map is the structured representation of who matters in this account, how much they matter, what they care about, and how well we cover them.

## Three Anchor Roles (Always Identify First)

Per Gartner / MEDDPICC / standard enterprise sales discipline, every active opportunity inside an account must surface these three:

| Role | Definition | What they care about | Risk if missing |
|---|---|---|---|
| **Champion** | Internal advocate who actively sells for us inside the org | Personal credibility, getting the problem solved, looking good to their boss | Single-threaded deal; one person leaves and the deal dies |
| **Economic Buyer** | Holds the budget; can say yes alone | ROI, total cost, alignment to corporate strategy, risk avoidance | Deal stalls in approval; price gets crushed because no one with budget authority defends the value |
| **Technical Evaluator** | Owns integration, security, architecture, compliance review | Technical fit, security posture, integration cost, vendor risk, ongoing support | Deal dies in technical or security review with no warning |

If any of these three is unknown after the second customer meeting, that is a Yellow flag. By the third meeting it is Orange.

## Full Stakeholder Taxonomy

Beyond the anchor three, the buying committee usually contains some combination of:

- **Executive Sponsor** — the most senior person who has personally endorsed the initiative
- **Project Owner** — operationally accountable for the outcome (often a VP / Director of Finance, IT, Ops)
- **End-user Lead** — represents the people who will actually use the system day-to-day
- **Procurement / Sourcing** — runs the commercial process; rarely the decision-maker but often the gatekeeper
- **Legal / Compliance** — contracts, data protection, regulatory; capable of stopping the deal cold
- **Finance** — budget mechanics distinct from the Economic Buyer (CFO often delegates here)
- **Internal Consultant / Architect** — sometimes carries veto-equivalent influence
- **External Consultant** — often Big Four; can be either friend or foe; for Thai accounts often an extended decision-maker
- **Board / Family Member** — for Thai family conglomerates, often the unseen real decision-maker
- **Coach** — gives us information without actively selling for us; valuable but not a champion

For Thai government / SOE accounts add:
- **ผู้บริหารระดับสูง / Senior bureaucrat** — formal authority, often hierarchical decision-making
- **คณะกรรมการ / Committee chair** — for procurement committees
- **ปลัด / Deputy** — operational authority, often the real signer
- **External oversight** — สตง., ป.ป.ช. context; not contacts but constraints

## Power Map Dimensions

For each named stakeholder, capture six dimensions:

1. **Role** — title and functional area
2. **Influence** — High / Medium / Low (capacity to move the decision)
3. **Sentiment toward us** — Champion / Supporter / Neutral / Skeptic / Blocker
4. **Sentiment toward incumbent / competitors** — same scale, applied to each major alternative
5. **Personal motivation** — what does *this person* personally care about (career, recognition, risk avoidance, relationship to a sponsor, technical curiosity, retirement-soon)
6. **Our coverage** — Named owner from our side / cadence of contact / quality of relationship (Strong / Developing / Cold / None)

## Multi-Threading Discipline

Single-threaded accounts (one relationship carrying the whole engagement) are the #1 cause of preventable losses. The discipline:

- **Minimum 3 named relationships** per active enterprise opportunity, ideally 5
- At least one relationship at each of: executive (C-1), management (Director / VP), and operational (manager / lead)
- At least one relationship in each of: business owner side, IT side, procurement / finance side
- For Thai government / SOE: add at least one relationship in the regulatory / oversight ecosystem (not necessarily a contact, but a known and tracked actor)

When a power map shows fewer than 3 relationships, the immediate next action is multi-threading expansion, not deal advance.

## RACI Overlay (For Active Workstreams)

When a workstream is in motion (an implementation, an evaluation, a renewal negotiation), overlay a RACI on the power map:

- **R**esponsible — does the work
- **A**ccountable — owns the outcome (one person)
- **C**onsulted — must give input before decision
- **I**nformed — must be told after decision

This catches the common failure where everyone consults the Champion but no one consults Legal, and the deal dies in contracts review.

## Champion Health Indicators

A champion is "healthy" when all five are true:

1. **Power** — can actually influence the decision (not just an enthusiastic end-user)
2. **Influence trajectory** — rising or stable, not declining
3. **Personal stake** — has visibly tied their own credibility to this initiative
4. **Access** — can get us in front of the Economic Buyer when needed
5. **Activity** — currently doing things on our behalf without being asked

Loss of any one moves the champion to Yellow. Loss of two moves the relationship to Orange. See `champion-development.md` for the full development and recovery playbook.

## Thai Cultural Calibration

When mapping Thai stakeholders:

- **Hierarchy is often invisible to outsiders** — the most powerful person in the room may not be the most senior title; ask trusted local advisors
- **Family / school / military networks** — frequently more decisive than org chart; track them where possible without being intrusive
- **บุญคุณ (bunkhun) chains** — who owes whom; affects how influence flows; treat as a balance sheet (see `thai-cultural-overlay.md`)
- **ผู้ใหญ่-ผู้น้อย dynamics** — never ask a senior to do something a junior could do; never bypass a senior without their blessing
- **External consultants** — often Big Four; if they are advising the customer, they are part of the buying committee even if no one says so

## Stakeholder Map Refresh Cadence

- **Active pursuit (in a deal)** — refresh after every customer meeting
- **Steady-state (no active deal)** — quarterly minimum
- **Trigger-event refresh** — leadership change, M&A, reorg, major contract event, public earnings event

## Output Format

Use `assets/stakeholder-power-map-template.md` as the starting structure. The template renders well as a table in a deck, a markdown file, or an Excel sheet.

## Anti-Patterns

See `anti-patterns.md`. Quick list:
- Listing roles without naming people
- Marking everyone as "Champion" or "Supporter" (sentiment inflation)
- Claiming "Strong" coverage on relationships we have not contacted in 90+ days
- Missing the procurement / legal / IT actors who can stop the deal
- For Thai accounts: missing the family / network / ผู้ใหญ่ behind the formal title
