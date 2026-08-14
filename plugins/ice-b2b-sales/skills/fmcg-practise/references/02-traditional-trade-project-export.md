# 02 — Wholesale channels: dealer, project and export

> Load this when dealers, distributors, corporate or government projects, sponsorship
> contracts, or export sales are in scope. These three share one process spine, so they
> are documented together and their differences called out explicitly.

## A finding worth stating up front

In the reference implementation, the design documents for **Traditional Trade** and **Project
Sales** are, at process level, **identical** — the same requirements, the same integrations, the
same step sequences. Every requirement that names a channel names them together.

That is not sloppiness. It is the correct answer, and it generalises:

> **In a B2B2C consumer-goods design, channel differentiation belongs in customer coding and
> tax-point rules. Process differentiation belongs in payment terms and sourcing model.**

Writing a separate process per channel would have produced a dozen near-identical designs that all
have to be maintained. Recognising this early is a genuine saving in both build and support, and
it is a useful thing to say in a solution workshop when a customer insists each channel is unique.

## What actually differs — the three real axes

| Axis | Variants | What changes in the system |
|---|---|---|
| **Payment terms** | cash (ขายสด) vs credit (เครดิต) | Cash inserts four extra steps: proof-of-payment upload by sales, notification to Finance, Finance approval of goods release, and the order opening **pending** instead of approved. Credit relies on the automated credit-limit and overdue check instead of a human release gate. |
| **Sourcing model** | stocked collection · made to order · transformation with item change · transformation without item change | Stocked goods flow straight to fulfilment. Made to order raises a requisition and purchase order, receiving into a supplier-linked location. Transformation transfers own stock out to a subcontractor and raises a production request (see file 08). |
| **Deposit present or not** | with / without เงินมัดจำ | With a deposit: automatic receipt to an undeposited-funds account, VAT charged and a tax invoice issued on the deposit, and the final invoice netted against it. Without: a single invoice at fulfilment. |

Channel identity itself — dealer, project, export, sponsorship — is carried in a **customer-master
segment**, driving reporting and tax-point treatment rather than changing the transaction path.

## The shared order-to-cash chain

```
CRM: sales rep confirms the sale
  → stock check · credit-limit check · overdue-invoice check
  → CRM creates the Sales Order + reserves stock in the ERP
     status = Pending (cash)  |  Approved (credit)
  → [cash] deposit or full payment: proof uploaded, Finance verifies,
     deposit receipt posted, tax invoice issued on the deposit
  → Finance approves release → order status Approved
  → automatic release to the warehouse
  → 3PL picks and packs → confirms back → status Packed / Shipped
  → STOCK RELIEVED, cost of sales posted
  → Accounting raises Invoice / Tax Invoice, net of any deposit
  → delivery → billing → cash application
```

**Two control points to name in any design review:**
- **Stock is relieved on the warehouse's confirmation**, not on the ERP's instruction — the physical
  event drives the accounting event.
- **The invoice may only be raised from a fulfilment in shipped status.** This single rule stops
  every wholesale channel from billing goods that never left.

## Credit management

| Element | How it works in the reference implementation |
|---|---|
| Where the limit lives | the **ERP** holds the credit limit; the CRM calls it synchronously at order creation |
| What is checked | credit remaining **and** whether the customer has overdue invoices — both gate the sales order |
| What the rep sees | a credit-remaining view: customer, name, credit remaining, overdue yes/no |
| Overdue visibility in CRM | surfaced from the ERP so the rep sees it before promising |
| Who maintains the limit | changed through the customer-amendment flow — a finance-controlled field with accounting plus authorised-approver sign-off |
| **Who can override a block** | **not documented in the reference design** |

That last row is a genuine gap and a good discovery probe. Every wholesale business has exceptions —
a strategic dealer at limit on the last day of quarter, a project customer whose payment is
confirmed but not cleared. If there is no designed override path with an approval trail, staff
invent one outside the system, and the control stops meaning anything. **Ask who can release a
credit hold, up to what value, and where that decision is recorded.**

### The pattern to propose where none exists

A credit-hold release should be **a recorded transaction, not a changed master record.** The
failure mode to design against is the one that always happens otherwise: someone raises the credit
limit to let one order through, and nobody lowers it again.

| Element | What good looks like |
|---|---|
| **Mechanism** | a hold-release action against **the specific order**, leaving the customer's credit limit untouched |
| **Authority** | tiered by exposure value, with the tiers set by Finance rather than by Sales |
| **Reason** | a mandatory reason code from a maintained list — payment in transit, strategic account, order under negotiation — not free text |
| **Expiry** | the release applies to that order only and lapses when it ships |
| **Visibility** | a released-on-override report that Finance reviews on a cycle, showing who released what and why |
| **Master-data change** | a genuine limit increase remains a separate, finance-controlled amendment with its own approval — never the answer to a single blocked order |

Proposing this in a fit-gap workshop costs nothing and lands well, because the finance director has
almost always seen the alternative.

## Pricing and discount

| Element | Finding from the reference implementation |
|---|---|
| Price list | mastered in the **ERP**, pushed to the CRM as a batch feed carrying item, unit of measure and price |
| Product master | mastered in the ERP, pushed to the CRM as a scheduled file |
| Stock availability | queried live from the ERP by the CRM |
| **Tiered or volume discount** | **not present in the source design** |
| **Discount approval authority** | **not present in the source design** |
| Promotion | the ERP holds a **base price only**; discount and promotion logic sits in the **channel front-end systems** |

### The architecture is fine. The write-back is the requirement.

**The ERP holding a base price while each channel decides its own discount is a sound design, and
should be defended rather than apologised for.** The front end is where the deal context lives —
the retailer's trade agreement, the marketplace campaign, the sales rep's negotiation, the store's
member price. Forcing all of that into the ERP produces a promotion engine nobody can maintain.

**What is not optional is that the promotion comes back.** Whatever channel decided the discount,
the ERP transaction must carry what was actually granted — otherwise the business has revenue it
cannot explain and margin it cannot analyse.

> **The rule: the front end owns the decision; the ERP owns the record.**
> Every channel, without exception, writes its realised pricing back onto the ERP sales
> transaction. A channel that cannot write back is a channel you cannot analyse.

### What must land on the ERP transaction line

| Field | Why it is needed |
|---|---|
| **Gross price** (list / base) | the baseline the discount is measured against |
| **Discount amount** and **discount percentage** | the value actually given away |
| **Discount or promotion type** | trade discount · campaign · member price · staff price · platform-funded · brand-funded — these are different economics and must not be one bucket |
| **Promotion or campaign code** | so a campaign can be evaluated across every channel that ran it |
| **Net price** and **net line value** | what was actually invoiced |
| **Who funded it** — brand, retailer or platform | a platform-funded discount is not a cost to the brand; a brand-funded one is. Netting them together destroys the margin number |

With those on the line, sales analysis works the same way in every channel: **gross sales less
discount equals net sales**, and both discount and campaign become reportable dimensions rather
than a difference nobody can name.

### What this changes in the integration design

- Order-creation interfaces carry **price detail, not just a final amount**. An interface that
  sends only the net value is cheaper to build and permanently blinds the analysis.
- The **promotion or campaign code becomes reference data shared across systems**, with one owner —
  the same governance problem as the channel dimension in file **10**, and the same answer.
- Where a channel front end genuinely cannot send the breakdown, the honest fallback is to derive
  it: the ERP holds the base price, so **discount = base price × quantity − net line value**. That
  recovers the amount but not the *type* or the *funder*, which is the part that matters most.
  Treat derivation as a stopgap, not a design.

### The two consequences that remain, stated honestly

1. **Discount governance sits outside the ERP's approval framework**, so the authority matrix has to
   be built where the discounting happens — in each front end — and it will not look the same in all
   of them.
2. **Agreed commercial terms and billed amounts still live in two places.** The write-back makes them
   *comparable*; it does not make them *one record*. A periodic report comparing the trade agreement
   to what was actually granted is still worth building.

If a prospect expects tiered pricing, deal-based discount approval and margin control **inside** the
ERP, that is a scope item — not an assumption. But if they expect **channel and campaign margin
analysis** from an ERP fed by front-end discounting, that is entirely achievable, and the write-back
above is how.

## Project and corporate sales — what is genuinely different

Project business (corporate, government, sponsorship, club rights) shares the process spine but
carries extra characteristics worth probing:

- **Opportunity-driven front end.** The pipeline stage matters commercially long before an order
  exists. The reference implementation carries an opportunity-status integration back to the CRM,
  but no deeper project structure.
- **Made to order is the norm rather than the exception.** Corporate uniform and team kit are
  ordered, not stocked — so the transformation module (file 08) is on the critical path.
- **Deposits are common**, which is why the deposit chain is designed in rather than bolted on.
- **Milestone or staged billing** — **not present in the reference design.** The only staged
  mechanism is a single deposit netted against a final invoice. If a prospect bills projects in
  progress stages, that is additional scope.
- **Tender and procurement compliance** for government buyers — documentation formats, bid bonds
  and procurement-portal obligations sit outside the ERP but constrain the paperwork it must
  produce.

## Export and international sales

Export runs the same eight sourcing-and-payment variants as the domestic wholesale channels. The
additional design concerns:

- **Currency** — the order, the invoice and the settlement may each sit in a different currency;
  revaluation and realised gain or loss must have a home.
- **Export documentation** — invoice, packing list, certificate of origin and shipping documents
  drive both customs clearance and the buyer's payment release.
- **Landed cost and the export cost sheet** — the reference architecture shows an **export order
  cost sheet** as a front-end capability, sitting outside the core ERP. Freight, insurance, duty and
  handling have to be assembled somewhere before a price can be quoted.
- **Tax treatment** — export sales are treated differently from domestic sales; confirm the position
  with the customer's tax adviser rather than assuming.
- **Payment instruments** — letters of credit and documentary collections change when the receivable
  is recognised and when it can be collected.

## Returns and credit notes

The wholesale channels use the two return paths shared across the whole design:

- **Credit note with goods return** — the return is recorded against the original sales document,
  approved by authority level, sent to the warehouse, physically received, and a credit memo raised;
  a refund follows if money must go back.
- **Credit note only** — a price or allowance correction with no goods movement.

Note that in the reference implementation's earliest channel documents, the credit-note *process*
was not designed at the channel level at all — only the requirement to *see* credit-note data and to
print the statutory credit-note form. The full return flow came later, as a separate process area.
That sequencing is itself a lesson: **returns get designed late and then rushed.** Put them in the
first design pass.

## Scoping signals

Raise the estimate when you see:
- Tiered pricing or discount-approval workflow expected inside the ERP
- A credit-override or credit-hold-release process with an audit trail
- Milestone or progress billing on projects
- Export with letters of credit, landed cost, or multi-currency settlement
- Sponsorship or rights contracts with obligations that are not simple goods delivery
- Made-to-order volume expecting automatic requisition creation from the sales order

## Discovery questions

1. Do you sell on credit, cash, or both — and who releases goods when payment is not yet cleared?
2. Where are your prices held today, and where are discounts decided and approved?
3. What happens when a dealer is at their credit limit and wants to order?
4. For project business, do you bill in stages or on delivery?
5. For export, in what currency do you invoice, and when do you recognise the sale?
6. When goods come back from a dealer, what happens today?

## Related files

- **01** the full channel map and the product-type dimension
- **03** modern trade — the organised-retail sibling
- **08** made to order and transformation, which most project business depends on
- **09** the procurement side that made-to-order triggers
- **12** gaps versus common practice
