# Anti-Patterns — Reference

This file consolidates the failure modes that recur across B2B relationship management. Each anti-pattern is named, described, diagnosed, and given a corrective action. Use this as a self-check before delivering any artifact produced by this skill.

The anti-patterns are organized by where they typically appear in the lifecycle. Many are referenced from other files in this skill — this is the canonical source.

## Account Planning Anti-Patterns

### A1. The Shelf-Ware SAP
**Description**: Strategic Account Plan written once at the start of the year and never opened again.
**Diagnosis**: Look for last-modified dates older than 60 days on Tier-1 accounts. Ask the KAM to recall the top 3 plays from memory — if they can't, the plan is dead.
**Fix**: Move SAP to a living document with a monthly update ritual; tie account-team comp to evidence of plan execution (named plays delivered, not just SAP refresh).

### A2. The Wishlist Plan
**Description**: Plan reads as a sequence of aspirations ("become trusted advisor", "expand to all business units") with no mechanism, owner, or date.
**Diagnosis**: Search the document for "we will" — if it appears more than 5 times without a name + date attached, it's aspirational rather than operational.
**Fix**: Replace every "we will X" with "[Name] will X by [Date], measured by [signal]".

### A3. The Year-Over-Year Refresh
**Description**: This year's plan is last year's plan with the year changed and a few cosmetic edits.
**Diagnosis**: Compare current SAP to prior-year SAP — if >70% identical, the relationship hasn't actually evolved or we're not paying attention.
**Fix**: Force a "what changed" section at the front of every annual refresh; require 3 named changes in the customer's situation that drive plan adjustments.

### A4. Activity as Strategy
**Description**: Plan substitutes activity ("hold 4 QBRs, 1 EBR, 12 working sessions") for strategy (what we're trying to achieve and why).
**Diagnosis**: Calendar the planned activities against measurable outcomes — if there are 20+ activities and 0–2 outcomes, activity has eaten the strategy.
**Fix**: Force outcomes-first formulation. Activities are how we deliver outcomes, not the outcomes themselves.

## Stakeholder Mapping Anti-Patterns

### S1. Roles Without Names
**Description**: Power map lists "CFO", "CIO", "Head of Procurement" without actual names.
**Diagnosis**: Generic role names with no attached person.
**Fix**: Every role must have a named person. If unknown, the next action is "find out who" — that's a play in the plan.

### S2. Sentiment Inflation
**Description**: Half the buying committee marked as "Champion" or "Supporter" with no behavioral evidence.
**Diagnosis**: Champion count > 1 in the same account; "Supporter" applied to people we've met once.
**Fix**: Apply the Champion 5-criteria test (`champion-development.md`); demote anyone failing more than one. Most "Champions" are actually Supporters or Coaches.

### S3. Phantom Coverage
**Description**: Power map shows "Strong" coverage for relationships we have not contacted in 90+ days.
**Diagnosis**: Compare coverage rating to last-contact date.
**Fix**: Add a last-contact date column; downgrade coverage automatically when contact date exceeds threshold (60 days for Strong, 90 days for Developing).

### S4. The Single-Threaded Account
**Description**: Whole account managed through one relationship.
**Diagnosis**: Power map has 1–2 named relationships; if that one person leaves, we lose the account.
**Fix**: Multi-threading is the next play. Minimum 3 named relationships on any active enterprise opportunity.

### S5. Missing the Gatekeepers
**Description**: Map covers business stakeholders but ignores procurement, legal, IT, security — the people who can stop a deal cold.
**Diagnosis**: Power map has all "yes" people, no "no" people identified.
**Fix**: Force a gatekeeper section in every map. For each: who, when do they enter, what could they kill, how do we engage them early.

### S6. (Thai-Specific) Missing the Family / Network
**Description**: For Thai family conglomerates and networked accounts, the power map shows the org chart but misses the family principal, school network, military connections, or chairman's chief of staff.
**Diagnosis**: For known Thai family businesses, the family principal is not on the map.
**Fix**: Apply `thai-cultural-overlay.md` checks; consult a trusted local advisor for power-network insight.

## Engagement Cadence Anti-Patterns

### C1. The Sales-Pitch QBR
**Description**: QBR turns into a 60-minute pitch for the next module / expansion.
**Diagnosis**: Customer talks <20% of meeting time; agenda has more "what we're selling" than "what value you got".
**Fix**: Hard rule — customer talks ≥40%; expansion conversations belong in separate dedicated sessions, not in QBRs.

### C2. The Status-Report QBR
**Description**: QBR is a one-way recital of what happened last quarter.
**Diagnosis**: No customer voice; no joint-plan; no decisions made.
**Fix**: Reformat with mandatory customer-voice and joint-90-day-plan sections.

### C3. Cancelled EBR
**Description**: Executive Business Review repeatedly cancelled or rescheduled by the customer.
**Diagnosis**: EBR pushed >30 days from original date with vague reason.
**Fix**: Yellow flag on relationship health. Diagnose: are we asking too much of the executive's time, are we delivering low-quality content, is the relationship deteriorating? Different fixes for each.

### C4. Substitute Senior
**Description**: Our executive sponsor sends a delegate to the EBR.
**Diagnosis**: Our exec on calendar but not in seat.
**Fix**: Reschedule the EBR rather than send a substitute. Our executive's commitment is the signal that matters.

### C5. Generic Roadmap Slide
**Description**: Same 10-slide product roadmap deck shown to every customer in QBRs / EBRs.
**Diagnosis**: Roadmap slide is identical across accounts; nothing about the customer's specific context.
**Fix**: Filter every roadmap slide for relevance to *this* customer; remove what doesn't apply; annotate what does.

## Health Score Anti-Patterns

### H1. Optimism Bias
**Description**: KAM rates their own accounts higher than independent assessment would.
**Diagnosis**: All accounts in a KAM's portfolio score Green; never any Yellow; KAM's emotional attachment to the account is high.
**Fix**: Sales Leader spot-check on a sample of accounts every quarter; calibration meetings with peer KAMs.

### H2. Score Without Action
**Description**: Health score produced and reported but no playbook triggered.
**Diagnosis**: Yellow / Orange / Red accounts with no associated action plan within the required window (30 / 60 / 14 days).
**Fix**: Score is incomplete without action. No score is delivered until the playbook is named.

### H3. Operational Ticket Domination
**Description**: Score driven entirely by support ticket volume; misses Executive Sentiment as the actual problem.
**Diagnosis**: Score green on tickets, but executive sponsor has not engaged in 60+ days.
**Fix**: Ensure all six components contribute; weight tuning when one dominates inappropriately.

### H4. Quarterly Refresh on Deteriorating Account
**Description**: An account deteriorating month-over-month is only re-scored at quarter-end, missing the recovery window.
**Diagnosis**: Critical signals fired between scheduled refreshes were not acted on.
**Fix**: Trigger-event refresh discipline; any Critical Single Signal forces immediate re-score.

## Champion Development Anti-Patterns

### CH1. End-User as Champion
**Description**: Treating an enthusiastic end-user (who has no decision power) as the champion.
**Diagnosis**: Apply the 5-criteria test — they fail "Power" criterion.
**Fix**: Distinguish Champion from Coach / Supporter; develop a real champion in parallel.

### CH2. The Burnt Champion
**Description**: Champion is asked too often, with too much, and stops responding.
**Diagnosis**: Diminishing response rate; champion stops volunteering information.
**Fix**: Frequency discipline; reciprocate explicitly; protect the champion's calendar; develop succession.

### CH3. Champion Silence at Renewal
**Description**: Champion goes quiet during renewal cycle.
**Diagnosis**: T-90 to T-60 contact frequency drops despite our outreach.
**Fix**: Diagnose — has their authority changed, has competition reached them, is value realization weak? Different recoveries for each.

### CH4. Going Around the Champion
**Description**: Reaching out to the champion's boss without telling the champion.
**Diagnosis**: Champion learns of our exec's contact with their exec from their exec, not from us.
**Fix**: Always brief the champion before going up; in Thai context, this is relationship-ending if violated.

## Value Realization Anti-Patterns

### V1. Sold and Forgotten
**Description**: Pre-sale business case agreed, never re-opened.
**Diagnosis**: No baseline captured at go-live; no value scorecard in QBRs.
**Fix**: Mandatory baseline at go-live; mandatory value scorecard segment in every QBR; refresh business case annually.

### V2. Numbers Without Mechanism
**Description**: Value reported without explaining how our solution caused it.
**Diagnosis**: "DSO down 15 days" without "because of [specific feature / workflow / process change]".
**Fix**: Force the causal chain in every reported metric.

### V3. Optimism Inflation
**Description**: Reported value exceeds what the customer would attest to.
**Diagnosis**: Our scorecard claims X, customer says X/2; first dispute kills credibility.
**Fix**: Co-validate every reported number with the customer's data team or finance before reporting; use the customer's own systems where possible.

### V4. Hiding the Misses
**Description**: Reporting only green metrics; suppressing yellows and reds.
**Diagnosis**: Three quarters of all-green; first surfaced miss reads as cover-up.
**Fix**: Transparency builds trust; surface misses with root-cause and recovery action.

## Renewal & Expansion Anti-Patterns

### R1. First Contact at T-60
**Description**: First renewal-focused conversation at month T-60 of a 12-month contract.
**Diagnosis**: T-180 readiness assessment not done.
**Fix**: T-180 framework discipline (`renewal-expansion-motion.md`).

### R2. Bundling Expansion into Renewal
**Description**: Pushing an expansion module into the renewal package to boost ARR.
**Diagnosis**: Renewal proposal includes new modules; customer pushes back on whole package.
**Fix**: Decouple — expansion runs its own motion; customer earns the right to say yes / no on each independently.

### R3. Reflexive Discount
**Description**: Customer pushes back on renewal price; we discount without diagnosis.
**Diagnosis**: Discount applied with no recorded justification or trade.
**Fix**: Push back politely first; diagnose the source of pressure; trade discount for term, scope, expansion attach, or reference rights.

### R4. Assumed Continuity
**Description**: Assuming the same stakeholders, criteria, and dynamics from the previous renewal.
**Diagnosis**: No re-discovery between renewals; surprised by new evaluator or new requirements.
**Fix**: Re-discover at T-180 as if it were a new opportunity, even when the relationship is healthy.

## Escalation & Recovery Anti-Patterns

### E1. Slow First Response
**Description**: First acknowledgment beyond 24 hours of escalation.
**Diagnosis**: Time-stamp from escalation to first acknowledgment.
**Fix**: 4-hour acknowledgment SLA on any executive-level escalation; voice contact, not email.

### E2. Defensive Posture
**Description**: Explaining why we're not at fault before acknowledging the customer's experience.
**Diagnosis**: First two minutes of recovery call dedicated to context-setting / explanation.
**Fix**: Acknowledge first; understand second; explain only when asked.

### E3. Committee-Owned Recovery
**Description**: Recovery owned by a committee with no single accountable person.
**Diagnosis**: Multiple email threads, multiple "owners", customer unsure who to contact.
**Fix**: Single named Recovery Owner; everyone else is supporting.

### E4. Premature Victory
**Description**: Declaring recovery complete at day 30 because operational metrics improved while relationship remains fragile.
**Diagnosis**: De-escalation announced before customer has independently signaled relief.
**Fix**: Recovery complete only when both signals align: operational metrics + customer acknowledgment.

### E5. Recovery as Sales Motion
**Description**: Using the war-room to position expansion or renewal upside.
**Diagnosis**: Recovery meetings include forward sell.
**Fix**: Hard separation. Recovery first; commercial conversations resume only after Green re-established and customer acknowledges.

## Cultural Anti-Patterns (Thai)

### T1. Pushing for Decision in Meeting
**Description**: Asking a senior Thai stakeholder to commit in front of others.
**Diagnosis**: Direct yes/no questions in group settings.
**Fix**: Pre-wire 1:1; meetings are for alignment ritual, not negotiation.

### T2. Ignoring "Maybe Difficult"
**Description**: Treating "it might be difficult" or "we will consider" as openness.
**Diagnosis**: We move forward as if green-lighted; customer is mystified by our enthusiasm.
**Fix**: Apply high-context translation: "difficult" usually means "no"; verify in 1:1 with champion before committing.

### T3. Bypassing the Deputy
**Description**: Going to the Director-General without briefing the Deputy.
**Diagnosis**: Senior is briefed; deputy learns from senior.
**Fix**: Always brief the deputy first; never bypass without explicit blessing of the deputy.

### T4. Quarterly KAM Rotation
**Description**: Rotating KAMs every 12 months for "career development".
**Diagnosis**: Account-team turnover above 30% annually.
**Fix**: For Thai accounts, multi-year continuity is required; rotate roles around the relationship, not the relationship around the roles.

### T5. Aggressive Challenger Selling
**Description**: Direct provocation, "tell-them-what-they-don't-know" tactics applied without cultural calibration.
**Diagnosis**: Customer becomes polite, distant, and unresponsive after a "challenger" meeting.
**Fix**: Adapt the substance (insight, fresh perspective, frame-breaking question) but soften the form (consultative, indirect, given as a gift not a confrontation).

### T6. (Government-Specific) Late Entry
**Description**: Engaging only when the RFP is published.
**Diagnosis**: First customer contact appears in our CRM after TOR publication date.
**Fix**: Government engagement is a multi-year pre-RFP relationship; if you didn't shape the TOR through legitimate education, you're competing on price alone.

### T7. (Government-Specific) Compliance Theatre
**Description**: Claiming local-presence, technology-transfer, or PDPA compliance without real capability.
**Diagnosis**: Audits, post-implementation reviews, or first incident reveal the gap.
**Fix**: Build real capability before claiming it; partner with a credible local entity if needed.

## How to Use This File

Before delivering any artifact produced by this skill:

1. Identify which anti-patterns apply to the artifact type (account plan → A1–A4; QBR deck → C1–C5; etc.)
2. Walk through each one as a self-check
3. For any anti-pattern that may apply, either fix the artifact or explicitly note the deviation and why

This file is also useful as a coaching tool with KAMs and account teams — many of these failure modes are familiar to practitioners and naming them creates shared language for improvement.
