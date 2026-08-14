# 18 — Investment Promotion Privileges (BOI)

> **Load this when:** the prospect manufactures in Thailand and mentions a promotion certificate
> (บัตรส่งเสริม), tax privileges, duty-free imported raw material, or promoted versus non-promoted
> business · or when a manufacturing client's finance team talks about exempt profit.
> **Do not load this for:** ordinary Thai tax on sales and trade spend → **17** · the ledger
> dimension design this depends on → **15** · inventory valuation → **11**.
> **Source basis:** the food and beverage implementation's investment-promotion specification, nine
> screens. **Its authors marked every certificate number, amount, rate, ceiling, period and date in
> it as illustrative and requiring verification.** This file therefore carries no figures at all.

## 1. What it is, and why it changes the system

Thailand's Board of Investment grants privileges to a **legal entity** through a **promotion
certificate**. One entity may hold **several certificates**, each covering a different promoted
activity — so "the company is BOI-promoted" is never a complete answer. The right question is *how
many certificates, covering what, and where is each one in its life*.

Each certificate carries an **activity class**, a corporate income tax exemption or reduction, an
exemption **ceiling**, an exemption **period**, a **first-revenue date**, the promoted products and
an approved capacity, and a status.

**Why this is an ERP problem and not an accounting one:** the privilege has to be *proven at the
transaction*, not reconstructed at year end. What an auditor or the promotion office asks to see is
the **source document** — the invoice, the goods receipt, the asset record. A design that tags
everything correctly in the ledger but leaves the originating documents untagged will fail the
inspection it was built to pass.

### The four statutory mechanics that drive the design

The source names them by section of the Investment Promotion Act. **Treat the section references as
the source's own citation and confirm them with the promotion office or the client's adviser before
using them in a document.**

| Mechanic | What it grants | What constrains it |
|---|---|---|
| **Corporate income tax exemption** on promoted-activity profit | exempt profit while promoted | bounded by **both a monetary ceiling and a time period — it ends on whichever arrives first** |
| **Dividend relief** | dividends paid out of exempt retained earnings are tax-free to the shareholder | only if declared **during the privilege period or within a defined window after it ends** |
| **Import-duty exemption on raw material** for export production | duty-free raw material | administered through a raw-material tracking scheme with an **approved maximum stock holding** and an **approved formula converting finished goods into raw-material coefficients** |
| **Machinery import-duty exemption** | duty-free machinery | carries a **no-disposal and no-transfer condition** for a defined period |

**The dual-ceiling rule is the one most often missed in scoping.** A privilege can expire because the
money ran out or because the clock ran out, and a system that tracks only one of them will report an
entitlement the business no longer has. The period is counted from the **first revenue** — the first
invoice — not from the certificate's issue date.

## 2. The nine control areas

| Area | What it does |
|---|---|
| **Certificate master** | the declared single source of truth every other area reads. **Effective-dated and version-controlled**, so a back-dated transaction resolves the certificate terms that were in force *on the transaction date*. Active versions are immutable; a change creates a new version with an amendment reference. Whether a ceiling applies at all derives from the activity class |
| **Cost-centre and project segregation** | the operational engine — revenue tagged per certificate, direct costs tagged, and **common costs allocated** across certificates and non-promoted business on a chosen basis. Notably, **profit above the ceiling is not blocked from being booked — it is reclassified as taxable** when the statement is generated |
| **Asset-to-certificate tracking** | decides where each asset's depreciation lands. Dual-use assets split by basis. Promoted-side depreciation **may not start before the first-revenue date**, and depreciation after the exemption period ends is non-promoted. Carries the machinery duty reference and **blocks a disposal, transfer, write-off or relocation that would breach the no-disposal condition**, with the duty-exempt amount held as the contingent exposure |
| **Statement generation and the tax return** | assembles a **per-certificate statement plus a consolidated entity statement**, splits exempt from taxable, tracks cumulative ceiling usage, and produces the return dataset and the annual report to the promotion office. Blocks finalisation when the ceiling is exceeded, when a certificate with revenue has no allocation, when asset coverage is incomplete, or when **intercompany sales have not been eliminated before promoted revenue is computed** — otherwise exempt revenue is overstated |
| **Incentive utilisation ledger** | the running control over the life of the privilege, holding both dimensions that end it: cumulative exempt profit against ceiling, and elapsed time against period. **A loss year consumes no ceiling but the clock keeps running** |
| **Duty-exempt raw material control** | an entitlement master holding the approved maximum stock and the approved formula · a balance ledger running import lot to consumption to disposal · and an **inventory segregation gate keeping duty-exempt stock apart from domestic and duty-paid stock in the valuation layer, not merely by report filter**. Commingling in one valuation layer is blocked outright |
| **Exempt-profit and dividend pool** | splits retained earnings into exempt and normally taxed pools per certificate per year, so a dividend can be traced to its source and tested against the relief window. Paying from the exempt pool after the window closes reclassifies the dividend as taxable |
| **Document-level sales and procurement segregation** | tags and validates **each sales or tax invoice and each purchase order or goods receipt** to a certificate or to non-promoted business **before posting**. The rationale: the accounting layer segregates the *destination*, but the source documents are what gets inspected. Issuing an exempt invoice for a product outside the certificate's scope is a **hard block no role may override**, because on audit it can mean retrospective loss of the privilege plus penalty |
| **Compliance calendar and evidence repository** | obligation control across certificates — filing deadlines, certificate expiry, the dividend window, machinery condition dates, scheme approval expiry — each with an owner, lead time and evidence requirement. The repository holds certificates, amendment letters, **the first tax invoice that starts the entitlement clock**, and filing receipts. Committed evidence is immutable; replacement creates a version |

## 3. Where it touches the rest of the design

| Area | What BOI adds | Home file |
|---|---|---|
| **Inventory** | duty status originates on the source document, is enforced **in the valuation layer**, and is controlled quantitatively against an approved maximum holding. Two breach paths create exposure — balance above the maximum, and consumption outside the promoted scope — and both raise a **back-duty (จ่ายอากรย้อนหลัง)** provision before filing | **11** |
| **Procurement** | the **purchase order and goods receipt are where duty status originates**, and they are what an audit inspects. Two controls belong upstream rather than in the ledger: a certificate tag validated **before posting**, and a block on tagging a purchase to a certificate carrying no raw-material entitlement. Exempted duty is also **not a landed-cost component** and must not be absorbed into item cost | **14** |
| **Costing** | direct costs tag to a certificate; common costs run through a governed chain — an **approved basis master** with versioning and an append-only recalculation log, an **effective-dated matrix** that must total exactly one hundred per cent with no overlap and no gap, and a **mandatory transaction tag** where an empty tag blocks posting | **11**, **15** |
| **General ledger** | a mandatory certificate tag on the relevant transaction natures · **separate accounts for promoted and non-promoted depreciation** with a tie-out to the asset register · and an allocation reconciliation requiring direct plus allocated to equal the pool's ledger total. At statement level the sum across certificates and non-promoted business must tie to the trial balance or finalisation is blocked | **15** |
| **Reporting** | per-certificate and consolidated statements · the exempt-versus-taxable reconciliation · the annual return dataset · the operating-results report per certificate · the duty-exempt material reconciliation | **15** |
| **Period close** | the fiscal year cannot close until the statement is finalised | **15** |

## 4. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **Certificate master, effective-dated and versioned** | a back-dated transaction must resolve the terms in force on its own date | custom |
| 2 | **Dual tracking of ceiling and period**, ending the privilege on whichever comes first | tracking one alone reports an entitlement that no longer exists | custom |
| 3 | Period counted from the **first revenue event**, captured and evidenced | the clock does not start at certificate issue | custom |
| 4 | **Certificate tag mandatory on the relevant transaction natures**, blocking posting when empty | the ledger cannot be split after the fact | configuration plus validation |
| 5 | **Governed common-cost allocation** — versioned basis, effective-dated matrix totalling exactly one hundred per cent, append-only recalculation log | a free-text percentage cannot be defended on audit | custom |
| 6 | Allocation reconciliation — direct plus allocated equals the ledger pool | otherwise the statement does not tie | custom |
| 7 | **Asset-to-certificate mapping** with dual-use splitting, and depreciation start and end bound to the privilege dates | wrong mapping produces a wrong statement, wrong ceiling and a wrong return | custom |
| 8 | **No-disposal condition enforcement** on duty-exempt machinery, with the exposure carried | a breach is a real financial liability | custom |
| 9 | **Duty-exempt raw material segregated in the valuation layer** | a report filter is not segregation; commingling must be impossible | custom, and hard in most products |
| 10 | Entitlement balance ledger against an approved maximum holding, with **approval before use** | drawing on an unapproved formula or over the maximum creates back-duty | custom |
| 11 | Consumption tested against production quantity times the approved coefficient, with a tolerance and a justification route | over-consumption is a duty event, not a variance | custom |
| 12 | **Back-duty exposure surfaced before filing**, not discovered afterwards | the provision belongs in the statement | custom |
| 13 | **Exempt versus normally taxed retained-earnings pools**, with dividends traced to source and tested against the relief window | paying from the wrong pool or after the window reclassifies the dividend | custom |
| 14 | **Document-level eligibility validation** against a certificate-to-activity-to-product matrix, effective-dated | the source documents are what is inspected | custom |
| 15 | **Hard block on an exempt invoice for an out-of-scope product**, overridable by no role | the downside is retrospective loss of the privilege plus penalty | custom |
| 16 | Mixed exempt and taxable lines on one invoice, split by tag for the return | real invoices are mixed | custom |
| 17 | **Intercompany elimination before promoted revenue is computed** | otherwise exempt revenue is overstated | custom |
| 18 | Per-certificate and consolidated statements with a **finalisation gate** and a **period-close gate** | prevents closing on an unfinished position | custom |
| 19 | **Compliance calendar** with owners, lead times and evidence requirements per obligation | multi-certificate obligations are not trackable by memory | custom |
| 20 | **Immutable evidence repository** with versioned replacement, linked by certificate and transaction | the audit asks for the document, not the report | custom |

**Almost everything here is custom.** That is the honest headline for a proposal: investment-promotion
compliance is not a module you switch on, and a prospect holding several certificates should expect
it to be a named workstream.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **"We are BOI-promoted" taken as one fact** | modelled multiple certificates per entity from the start | ask how many certificates, covering what, and where each is in its life — the answer changes the scope |
| **Only the ceiling tracked, or only the period** | both, ending on whichever comes first | build the dual test; a loss year consumes no ceiling but the clock keeps running |
| **Segregation done in reporting rather than in the data** | valuation-layer segregation for duty-exempt stock; mandatory tags at posting | a report filter can be changed by anyone; a blocked posting cannot |
| **Source documents left untagged** | document-level validation before posting, with a non-overridable block on out-of-scope exempt invoices | the accounting layer segregates the destination; only the document layer segregates the origin, and the origin is what is inspected |
| **Common-cost allocation as a typed percentage** | versioned basis master, effective-dated matrix, append-only log | an allocation you cannot reproduce is an allocation you cannot defend |
| **Back-dated transactions resolved against today's certificate terms** | effective-dated, version-controlled certificate master | this is the single most valuable structural decision in the module |
| **Intercompany sales left in promoted revenue** | elimination enforced before computation | otherwise exempt revenue — and the privilege consumed — are both overstated |
| **Where revenue is recognised in a group** | **left open** — see below | resolve in discovery with the promotion office; it is not a system preference |

### The open decision the source deliberately did not settle

**In a group where the certificate holder manufactures and another entity sells onward, where is
promoted revenue recognised** — at the certificate-holding manufacturer on a transfer price, or at
the point of sale outside the group?

The specification left this open for resolution with the promotion office. **Do not answer it in a
proposal.** It changes the transfer-pricing design, the elimination logic and the ceiling
consumption rate, and it is a decision for the client's advisers. Raising it as a known open point
is a credibility signal; guessing at it is a liability.

## 6. Discovery questions

1. How many promotion certificates does the entity hold, and what activity does each cover? ⚑
2. For each — when did revenue first arise, and where is it against its ceiling and its period? ⚑
3. Do any assets serve both promoted and non-promoted production, and how is depreciation split today? ⚑
4. Do you import raw material under duty exemption? Is the formula and maximum holding approved, and who watches the balance? ⚑
5. How are common costs allocated across certificates today, and can you reproduce last year's allocation?
6. Does the group sell through more than one entity, and where do you recognise promoted revenue? ⚑ *(the open decision above)*
7. Have you ever had to pay back duty, and what triggered it?
8. Who currently tracks the filing dates, the certificate expiry and the dividend window?
9. Have you declared dividends from exempt retained earnings, and how do you evidence the source pool?
10. Is your fiscal year the same across all entities in the group?

## Related files

- **11** inventory and costing — the valuation-layer segregation and the costing chain this depends on
- **14** procure to pay — where duty status originates, on the purchase order and the goods receipt
- **15** finance, ledger and assets — the dimensions, the tie-out and the close gate
- **17** Thailand tax — the ordinary tax layer this sits alongside
- **19** the full discovery bank
