# 09 — Procure to pay and budget control

> Load this when sourcing, purchasing, goods receipt, payables, treasury, or budget control
> are in scope for a consumer-goods or apparel brand.
> The transformation-specific purchasing chain lives in **08**; this file covers the whole module.

## The framing: procurement here is three processes sharing one screen

A branded apparel or fast-moving consumer-goods business buys three fundamentally different
things, and they behave differently in lead time, quality risk and accounting:

1. **Finished goods bought for resale**
2. **Materials and services sent out for conversion** — printing, embroidery, screen printing,
   cut-make-trim (see file 08)
3. **General spend, services and assets**

The reference implementation carries this classification through the whole document-numbering
spine and **splits goods receipt into three distinct flows: converted goods (สินค้าแปรสภาพ),
stock items, and services/subcontract/assets.** That is above-average practice and worth carrying
into a new design.

**The refinement worth proposing:** in the reference implementation the class is a naming
convention. Naming conventions drift. Make it a **validated attribute captured at requisition
entry**, driving the receipt route, the account and the approval path.

## Function inventory — what the module must be able to do

### Supplier master
Create a vendor from a request package with system-assigned code · search-before-create to prevent
duplicates · assign to one or more operating companies from day one · hold tax registration,
addresses, contacts, bank details and legal name · **set and amend a credit limit per vendor** ·
activate and deactivate rather than delete · **attach statutory documents and track their expiry** ·
classify vendors into groups that drive the payables ledger split, and **grade and tag them by
process type and product group**.

### Agreements
Contract agreement per vendor with item list, price and validity dates · **blanket agreement** with
total committed quantity plus a delivery schedule per release round · multi-level approval · issue
to the vendor by email with a print fallback · reference the agreement from a purchase order so
contract pricing applies · **warn on expiry and show consumption to date** · a contract register for
management review.

### Requisition
Raise for five object types — inventory item, import item, service, fixed asset (with the related
asset number), and project — each with its own required fields · capture company, department,
location, project, vendor, estimated price and expected receipt date · type-bearing automatic
numbering · **accept a system-generated requisition raised by the sales side**, so a project sale
creates its expense requisition through an interface with no re-keying · investment-approval form
for new projects · sequential multi-level approval with reject-and-return.

### Sourcing and quotation
Raise a request for quotation and select the vendors to invite · issue by email or print · **let
vendors enter prices online**, or key in returned quotations · on-screen price comparison submitted
for approval · force attachment of the quotation document when received manually · keep bid history
for audit.

### Purchase order
**Create only by pulling an approved requisition — direct purchase-order entry is deliberately
disabled** · optionally link to a contract so agreed pricing carries · amend location, lines,
quantity, price and delivery date while open · type-bearing numbering · multi-level approval that
stamps the approver's electronic signature on the printed form · **email the approved order to the
vendor automatically**, with print as the fallback · open and close a purchase-order period to cut
off stale commitments · report open orders, history, received quantity by date, outstanding
quantity, and **on-time versus late delivery**.

### Receipt
Receive in **three flows** — converted goods, stock items, services and assets · accept a goods
receipt **posted by the third-party warehouse through an interface**, with automatic numbering ·
receive manually at a company warehouse when goods bypass the 3PL · **enter estimated landed cost
at receipt for imports and true it up at invoice** · print the goods-received note, and an asset
receipt note that feeds fixed assets · raise a **vendor return authorisation** with return request
and return note, and receive the vendor's credit note · **return stock physically at the 3PL by
transferring it back into a company warehouse first** · run a **claim and warranty replacement
cycle** on dedicated holding bins — awaiting claim (company) → awaiting claim (supplier) →
replacement into quality-control hold → release to sellable only after inspection passes · capture
a **maintained reason code** on receipt and return so returns can be analysed.

### Payable and treasury
Record a **vendor prepayment or deposit against a purchase order as a percentage of its value**,
separately for goods and expenses · **net the prepayment automatically when the bill is raised** ·
create the bill from the purchase order with the receipt upstream, covering imported goods,
imported goods **recognised before the invoice arrives**, domestic goods and general expenses ·
post actual landed cost onto the import bill and adjust the earlier estimate · amend an open bill ·
raise a bill credit from the original bill · route bills through approval with **a checker step and
a hard edit-lock once the checker approves** · create a payment across selected open bills and print
the billing document · pay by cheque or by **bank payment file** · deduct **withholding tax with more
than one service type on a single payment** and produce the electronic certificate · handle
foreign-currency payment with rate editing at bill or payment · **void a payment and instruct the
bank to stop it** · run **petty cash** two ways — float established and replenished by journal, and
requester drawdowns consolidated and uploaded · run **employee advances end to end** with all three
settlement cases (spend equals, exceeds, or falls short of the advance) · payables ageing summary
and detail, voucher and vendor bill reporting · multi-currency with a daily automatic rate update.

## The control points that matter

| Control | How it works | Why it earns its place |
|---|---|---|
| **No purchase order without an approved requisition** | direct order entry disabled | makes requisition approval binding rather than advisory |
| Sequential multi-level approval on requisition, order, agreement, bill and payment | reject-and-return at each level | the standard segregation-of-duties spine |
| **Checker step with edit-lock after approval** | the bill cannot be changed once the checker signs | closes the classic payables fraud path |
| Purchase-order period open/close | stale commitments cut off | keeps committed spend honest |
| Quality-control hold on claim replacements | release only after inspection | keeps unsellable stock out of available-to-promise |
| Statutory document expiry tracking on vendors | alert on expiry | a compliance control that is cheap to build and expensive to omit |

**Three controls that were still open in the reference design — probe for each of these in a new
engagement:**

- **Matching tolerance is undefined.** The bill is built from the purchase order with the receipt
  upstream, but no price or quantity tolerance and no exception route for a partial or over-receipt
  is written down. In a business that routinely receives short shipments, this surfaces first in
  user acceptance testing — the worst possible moment.
- **The requisition-to-order price ceiling was pending.** If a buyer can exceed the approved
  requisition price at order entry, requisition approval means nothing. For seasonal buying against
  a plan, close this before go-live.
- **Payables cannot be split by purchase type natively.** Separating trade, other and asset payables
  by vendor grouping alone is fragile, because the same legal vendor sells you fabric and a machine.
  This deserves a recorded decision rather than a workaround.

## Master data and structure

- **Vendor grouping drives the payables ledger split** — trade, other, asset. Fragile if a vendor
  spans categories.
- **Vendor grading and capability tagging by process type and product group** — this is what makes
  sourcing repeatable across seasonal drops. Most implementations bolt it on late; designing it in
  is cheap.
- **Type-bearing document numbering** across requisition, order, receipt and bill, carrying the
  purchase class.
- **Quarantine and claim bin topology** — awaiting claim (company), awaiting claim (supplier),
  quality-control hold — sitting inside the location structure from file 07.

## Six things a consumer-goods brand needs here

Worth naming explicitly in any pursuit, because they separate a category-aware proposal from a
generic one:

1. **Outside processing as a first-class purchase type.** A brand that owns design but not its
   factories lives on subcontracting. Conversion needs its own receipt flow and document class.
2. **Vendor capability tagging.** Sourcing has to be repeatable season after season.
3. **Landed cost estimated at receipt, trued up at invoice.** For imported apparel, duty and freight
   often exceed the margin difference between channels — and the freight invoice arrives weeks after
   the goods.
4. **A quarantine topology for claims.** Claimed, supplier-returned and replacement stock in separate
   non-sellable bins with inspection as the release gate keeps unsellable inventory out of the
   availability number every channel reads.
5. **Deposits with automatic netting.** Overseas suppliers demand deposits; manual netting means
   deposits get paid twice.
6. **Purchasing joined to the third-party warehouse by interface, not email.** On-hand is right on
   the day of receipt, which is what any multi-channel allocation depends on.

## Weak spots to price explicitly

- **Treasury is usually the thinnest area.** Bank reconciliation, cheque clearing, the cheque
  register and payment splitting by withholding-tax treatment sat at "pending solution" in the
  reference implementation. In Thailand these are month-end blockers. Scope treasury as its own
  workstream rather than assuming it lands with payables.
- **Vendor performance was a custom report, not a designed capability.** On-time delivery and
  postponement counts drive sourcing in fashion, where a two-week slip kills a drop. Designing it
  in — with a delay-cause code — is worth more than the report.
- **The accounting design may be absent from the process documents.** In the reference
  implementation no journal postings appeared in any procurement flow. **Treat a process flow with
  no journal entries as an incomplete blueprint** and price the accounting mapping as its own
  workshop. A controller cannot review a flow they cannot see the postings for.

---

## Budget control

### The one decision that matters

> **Where in the purchase chain is the budget consumed?**

The reference implementation checks at **requisition, purchase order, receipt, invoice, credit note
and journal** — which means the budget is committed **when the buyer commits**, not when the invoice
lands two months later. For a brand that buys seasonally, that is the difference between a budget
that prevents overspend and a budget that reports it after the season is over.

**Any competing design that checks only at invoice should be challenged on exactly this point.**

### Function inventory

Maintain a budget by period and dimension · create and amend a budget through an approval route ·
run a fund check at each controlled document type · report budget versus actual · handle the
approval and rejection cycle on budget amendment.

### Three things to insist on as standard

1. **A three-state view: commitment, obligation, actual.** A seasonal buyer needs *promised*,
   *delivered-but-unbilled* and *paid* as three separate numbers. This was requested and recorded as
   a **gap** in the reference implementation. It is the most-requested budget report in any
   product-buying business — assume it in scope rather than discover it.
2. **Multi-year carry-forward.** Store fit-outs, campaigns and product development straddle
   year-end. Carrying the unspent balance forward with opening and remaining both visible was also a
   **gap**. Flag it early: it touches the fiscal calendar and the project dimension, not only the
   report.
3. **A defined over-budget behaviour, by document type.** Best practice is not "block everything" —
   it is **warn at requisition, block at purchase order, allow at invoice with a recorded override**.

### What was left open — and is therefore a discovery question

The reference documents state that the system shows an error and returns the user to amend the
budget, but **do not say whether the check is a hard stop or whether it can be overridden**, do not
finalise the **control level** (department, project, account), and contain **no budget transfer
between units or projects at all** — only amendment.

Ask all three directly. "Does the system stop them, or warn them?" is a question that changes the
design and that customers frequently have not decided.

## Scoping signals

Raise the estimate when you see:
- Imports at volume — landed cost, multi-currency, and goods recognised before the invoice arrives
- A claim or warranty cycle with quality-control release
- Withholding tax with multiple service types on one payment
- Employee advances and petty cash expected in the system rather than in spreadsheets
- Bank payment files and cheque management
- Budget with commitment/obligation/actual reporting, or multi-year carry-forward
- Vendor performance measurement as a decision input rather than a report
- Any process documentation that arrives without journal postings

## Discovery questions

1. What are the three or four different things you buy, and do they follow the same approval path today?
2. Can a buyer raise a purchase order without an approved requisition?
3. When you receive short, what happens to the invoice match?
4. For imports, when do you know the true landed cost, and what do you do until then?
5. When goods are defective, where do they sit while the claim runs?
6. At what point does your budget get used up — when you ask, when you order, or when you pay?
7. If someone is over budget, does the system stop them or warn them, and who can override?
8. Does unspent budget carry into next year?

## Related files

- **08** the subcontract purchasing chain for transformation
- **07** the quarantine, claim and supplier-return locations
- **10** where procurement postings land in the ledger
- **12** procurement gaps versus common practice
