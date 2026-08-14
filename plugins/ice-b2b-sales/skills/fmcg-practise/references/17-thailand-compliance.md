# 17 — Thailand: tax, trade law and payments

> **Load this when:** the prospect is Thai and the conversation touches electronic tax invoicing,
> the tax treatment of rebates and retailer fees, what a retailer may lawfully charge a supplier,
> marketplace tax reporting, cash on delivery, or automated cash application.
> **Do not load this for:** investment-promotion privileges → **18 BOI** · the trade-spend process
> itself → **10**.
> **Source basis:** two research rounds against primary sources — the Revenue Department, the Trade
> Competition Commission, the Federation of Accounting Professions — plus a Thai electronic-data
> service provider. Confidence is stated per topic below.

> ### ⚠ Standing rule for this file
> **It gives you the structure of each problem, never a rate, a threshold or a filing date.** Those
> change, and a wrong one in a client document is a real liability. Every one is listed at the end
> as something to confirm with a tax or legal adviser. What earns the meeting is knowing *which
> questions exist* — most competitors do not.

---

## 1. What a retailer may lawfully charge — the finding most consultants do not know

**Thailand has a published Trade Competition Commission guideline on unfair trade practices between
wholesale and retail businesses and their manufacturers or distributors**, issued under the Trade
Competition Act and published in the Royal Gazette in 2019. It is a guideline on how the unfair-
practice provision of the Act will be applied.

**It names the fees directly.** Its clause on unfair charges covers entry or listing fees, shelf and
special-display fees, new-store-opening fees — **and it uses the term "ส่วนลดเมื่อซื้อสินค้าได้ตามเป้า
(Rebate)" explicitly.** These are not abstract categories; they are the same line items in file
**10**.

**Three consequences that change the design conversation:**

| Provision | What it means for the system |
|---|---|
| **A written agreement, made in advance, is required** | the trade agreement stops being good practice and becomes a **compliance artefact**. Versioning and amendment history are no longer only for audit — they are how the supplier evidences that a charge was agreed beforehand |
| An entry fee is treated as unfair **when it is charged beyond what the contract states** | the system must be able to show what the contract said **at the time the charge arose** — the same versioning requirement that file **10** derives from dispute defence, arriving here from a second direction |
| Provisions on forcing price reductions on goods already delivered and accepted, read together with the charging provisions | **retrospective charging is constrained in practice**, even though no single sentence bans it |

> **How to use this in a meeting, carefully.** Say that Thai competition guidance addresses retailer
> charges to suppliers and requires prior written agreement, and that this raises the bar on
> contract record-keeping. **Do not advise on whether a specific charge is lawful** — that is the
> client's legal counsel's call. Positioning the system as *the evidence layer* is both accurate and
> commercially strong.

## 2. Value added tax on rebates — the assumption that is probably wrong

Most system designs assume a volume rebate is settled by issuing a **tax credit note (ใบลดหนี้)**.
Thai guidance points the other way.

A Revenue Department ruling establishes that a **conditional discount is not a discount given at the
time of sale**. It therefore forms part of the VAT base at the time of sale, and **a tax credit note
under the credit-note provision cannot be issued for it** — only a **commercial credit note carrying
no VAT**. Read alongside the closed list of events that do permit a tax credit note, the conclusion
is that **a rebate earned on cumulative volume is not a credit-note event at all**.

**Design consequences:**

- The system needs **two distinct documents**: a tax credit note for the events that qualify, and a
  **commercial credit note without VAT** for conditional rebates. They are not the same object and
  must not share a numbering series.
- **Discount at the moment of sale behaves completely differently from a rebate settled later.**
  This is exactly the on-invoice versus off-invoice distinction in file **10**, and in Thailand the
  gap between them is a tax-character gap, not merely a timing one.
- Any design that routes all trade spend through tax credit notes will produce VAT that does not
  reconcile.

> Confidence: the ruling and the credit-note event list were retrieved from primary sources. **The
> application to a specific rebate structure still needs the client's tax adviser** — rulings answer
> the facts put to them.

## 3. Withholding tax on promotional payments and retailer fees

Promotional payments to a retailer attract **withholding at source**, and there is a Revenue
Department instruction dealing specifically with promotional-incentive payments. Two things follow.

**The base is the amount excluding value added tax.** Not the amount after withholding, and not the
VAT-inclusive figure. Name the field carefully in the design — the two readings sound identical in
conversation and produce different money.

**The open question worth raising with the client's adviser**, because no source settles it: are
**entry, shelf-space and new-store-opening fees** *promotional payments* (outside the VAT base) or
*a service the retailer supplies* (inside the retailer's VAT base)? Research indicates the
withholding treatment is the same either way, **but the VAT consequence differs**. A design that
assumes one answer for all fee types will be wrong for some of them.

**Design consequence:** the fee type must be a **configurable attribute driving tax determination**,
not a hard-coded rule — because the answer may differ per fee and may change with a future ruling.

## 4. Which financial reporting framework the client uses changes the scope

**The Thai standard equivalent to the international revenue standard is a direct translation** — no
local modification on consideration payable to a customer.

**But entities without public accountability apply a different framework**, and its revenue chapter
measures revenue net of trade discounts and volume discounts **only**. It carries **no variable
consideration concept**, and the professional body itself identifies consideration payable to a
customer as a point of difference.

**This is a scoping question, not an accounting footnote.** A client on the full standard needs
estimation method, constraint and reassessment each reporting date (file **10**, stage 2). A client
on the simplified framework does not. **Ask which framework applies before sizing the trade-spend
accrual work** — it can move the estimate materially in either direction.

## 5. Electronic tax invoice and receipt

### Elective in law, expected in practice — say both, and keep them apart

Two things are true at once here, and conflating them is what makes a consultant look either
uninformed or alarmist.

**In law it is an election.** The Revenue Department's own material describes entering the scheme as
an election made by application; no commencement date for a general obligation was found, and a
legal-tracking source likewise reported no business-to-business mandate in force. *(An internal
reference in this firm's toolkit describes the scheme as mandatory and phased — that description
could not be substantiated. Do not repeat it.)*

**In business-to-business practice it is close to unavoidable, for two reasons:**

| Pressure | Why it bites |
|---|---|
| **Counterparty pull** | once a customer or supplier is issuing and receiving electronically, the other side is expected to match. A brand selling to large organised-retail or corporate buyers does not get to decide this alone — the buyer's accounts-payable process does |
| **Fiscal encouragement** | the state actively promotes adoption through tax relief on the investment in issuing electronically. Where such relief is available, staying on paper is a decision with a measurable cost, not a neutral one |

**So the wrong advice is "you can defer this", and the wrong advice is also "the law compels you".**

> **What to say:** *"Legally it is elective today — do not let anyone tell you otherwise, because you
> can check that. In practice your B2B counterparties will pull you in, and there is tax relief for
> moving. So we would not build it as a later project. We design the document layer so that adopting
> it is a switch you turn on when you choose, not a rebuild."*

That position is defensible on both halves, and it converts a compliance argument — which clients
resist — into a design argument they can act on.

**Confirm with the client's tax adviser, and do not state from this file:** whether relief is
currently available, what form it takes, its rate, and whether it has an expiry. Incentives of this
kind are commonly time-limited, and the value of the advice collapses if the figure is stale.

### Mechanics that shape the architecture

Two schemes exist at different levels of sophistication, and **an entity elects one — it cannot run
both**. The election is **entity-wide, not per channel**, so a brand cannot put its high-volume
retail channel on the lighter route and corporate invoicing on the fuller one. Total volume across
all channels decides.

| Element | Design consequence |
|---|---|
| Documents exchanged as **structured, digitally signed XML** | the ERP produces and signs a defined structure, not a printed document |
| Transmission on a **monthly cycle with a deadline early in the following month** | a batch process with a hard cut-off, plus a failure and resubmission path |
| The **signing certificate sits on hardware** — a token or security module | an infrastructure and access question. Ask who holds it and what happens when they are away |
| **Credit notes are in scope** | every channel issuing credit notes is inside the scheme, not only sales invoices |

**Unresolved:** how each consignment model (file **03**) interacts with electronic issuance, and how
a later credit note behaves when the original was issued electronically. Flag it; do not assume
symmetry.

## 6. Marketplace platforms report seller data to the tax authority

An instrument requires electronic platforms above a defined size to maintain and file a special
account of seller activity. **The obligation sits with the platform, not the seller** — but the
consequence for the brand is that **a third party reports its revenue independently of its own
return**.

That turns marketplace settlement reconciliation (file **06**) from a finance convenience into an
**audit-defence artefact**. Hold, per platform and per period, three separately addressable figures:
the **gross** the platform recorded, the **deductions** it applied, and the **net** it remitted. A
design storing only the net receipt cannot answer why the authority's figure differs from the
client's.

> The detailed field list could not be retrieved, so whether reporting reaches individual seller
> level or platform totals is unknown — and that decides how closely a brand can tie to it.

## 7. Withholding and VAT on platform and service fees

**Withholding behaviour is per-platform configuration, not company policy.** Whether the brand
withholds on a commission depends on **which legal entity it contracts with** — a locally
incorporated entity or an offshore one. The same marketplace can present differently in different
arrangements.

**Design consequence:** the platform master must carry the **contracting entity and its tax status**
as a field driving tax determination on every fee posting.

**The question no public source answers:** does withholding appear as a **separate line** on the
platform's settlement report, or embedded in a net figure? It changes how deduction-by-type must be
built. **Ask for a real settlement report in discovery** — one file answers it in a minute.

Thailand also operates a regime for VAT on **electronic services supplied by non-resident
providers**, relevant to advertising, marketplace services and software bought from offshore. No
primary source was retrieved; included so it is not forgotten, and marked for the adviser.

## 8. Cash on delivery and carrier remittance

The evidence base for how large cash on delivery is in Thai e-commerce proved **weaker than
expected** — no source of adequate quality was found. **Do not quote a share figure.**

The design constraint holds regardless: **the carrier is the debtor while goods are in transit, not
the consumer.** That requires a **clearing account per carrier**, remittance recorded **gross with
fees posted separately**, and the ability to **clear a shipment that was returned rather than
collected, with no cash receipt ever occurring** — the case most often missed, and not rare in
fashion or consumer goods.

## 9. Payments — the detail that enables automated cash application

Thailand's standardised QR payment scheme carries, in its bill-payment structure, a **biller
identifier**, a **mandatory first reference limited in length**, and an **optional second
reference**.

**That mandatory reference is the mechanism that makes automatic cash matching possible — and its
length limit is the trap.** Check the client's document-numbering scheme against it **during design,
not during testing**. A document number longer than the limit cannot be carried as the matching
reference, and the automated-matching benefit quietly disappears — usually discovered in user
acceptance testing, after the efficiency has been promised.

Where automatic matching is wanted, use a **dynamic code generated per transaction** carrying the
document reference, rather than a static payee code that identifies only who paid.

Card acquiring and gateway settlement cycles were **not sourced**. The clearing-account pattern
above applies to them equally.

## 10. Modern trade electronic data exchange

The three-architecture model — portal-only, bureau-integrated, direct-per-retailer — lives in file
**02**. Two refinements from research:

**Confirmed:** the service-bureau model **does offer system-level integration to a supplier's ERP**
over standard business-to-business transport protocols. It is genuinely not portal-only.

**Not published:** the message standard. **Ask the client for a sample file**; specify the interface
by capability in a proposal and assume per-partner mapping effort.

**Absent from the document set: sales and stock-on-hand reporting.** Sale-out capture must be
designed as its own path — which matters most for consignment, where sale-out *is* the revenue
event.

---

## Must be confirmed with a tax or legal adviser — hand this list to the client

Listing these in a proposal is itself a credibility signal; most competitors simply assume.

1. **What tax relief is currently available for adopting electronic tax invoicing, in what form, and when it expires** — the legal position is elective, so the live question is the incentive and the counterparty pressure, not the obligation
2. Which electronic scheme fits the volume, and the consequences of the entity-wide election
3. **Whether entry, shelf-space and new-store fees are promotional payments or a retailer service** — the withholding treatment appears the same, the VAT consequence differs
4. Withholding categories and rates by spend type — not one blanket rate
5. Whether a specific rebate structure can be settled by tax credit note, or only by commercial credit note
6. **The tax and accounting classification of delivery-performance and compliance penalties** — two research rounds failed to source this
7. Which financial reporting framework the entity applies, and its treatment of consideration payable to a customer
8. Whether the client's retailer charges comply with the competition guideline, and what contract evidence is expected
9. The tax point for each consignment model, and how a later credit note interacts with an electronically issued invoice
10. Validity periods and content requirements for tax debit and credit notes
11. Record-retention periods for electronic documents and evidence
12. Whether VAT on foreign electronic services applies to the client's purchases

## What could not be established, and must not be invented

- The platform special-account field list — so how closely a brand can tie to it is unknown
- Whether withholding appears as a separate settlement line
- The classification of delivery-performance penalties — **unfound in two attempts**
- Any Thai figure for cash-on-delivery share, carrier remittance cycles, listing fees, rebate levels
  or deduction rates — **ask the client; no defensible market figure exists to quote**
- Card and gateway settlement cycles
- Published Thai multi-channel case studies of adequate source quality

## Related files

- **02** modern trade, and the three electronic-exchange architectures
- **03** consignment and its two tax points
- **06** online, marketplace settlement and cash on delivery
- **10** trade spend — the process this file taxes
- **18** BOI and investment-promotion privileges
- **19** the discovery bank
