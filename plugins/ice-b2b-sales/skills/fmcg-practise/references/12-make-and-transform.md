# 12 — Make to Order and Transformation (สั่งผลิตและแปรสภาพ)

> **Load this when:** the brand decorates, prints, embroiders, personalises, assembles or subcontracts finishing ·
> the order book contains team kit, corporate uniform, licensed product or promotional goods · the words
> "สั่งผลิต", "แปรสภาพ", "ค่าจ้างแปรสภาพ", "subcontract", "made to order" or "outside process" appear · goods are
> physically sitting at a third party who is working on them.
> **Do not load this for:** warehouse topology, location groups and item costing method → **11 Inventory and Item
> Costing** · buying finished goods or raw material from suppliers → **14 Procurement** · forecasting and
> replenishment → **13 Demand Planning** · how the decorated product is sold to each type of buyer → **00-09 the
> channel files**.
> **Source basis:** one apparel and sportswear reference implementation that carried outside process
> (สินค้าแปรสภาพ) as a distinct process area with its own master data, its own stock location and its own cost
> event. No defensible market benchmark exists for transformation cost, subcontract lead time or decoration
> yield — ask the client, never quote a figure.

## 1. Why this is a module of its own

A distributor buys finished goods and sells them. An apparel or promotional-goods brand often sells a **blank that
becomes a specific product only after decoration** — a club name, a sponsor logo, a player number, a corporate
identity. The same physical garment can become many different sellable products. The reference design treats this
as a process area in its own right, sitting alongside procure-to-pay, order-to-cash and inventory, and that
structural choice is itself the lesson. Transformation is not a variation of purchasing and not a variation of
selling. It touches both, and it brings three things neither has: its own master data, its own stock location,
and its own cost event.

### Scope boundary — read this before estimating

This file covers **transformation and made-to-order work that hangs off a sales order**: a blank is consumed, a
service is bought from a subcontractor or performed in house, and a finished item comes back for a customer who is
already known. It does **not** cover a full manufacturing operation — multi-level bills of material, routings and
work centres, capacity and material requirements planning, shop-floor scheduling, production variance analysis. A
prospect that runs its own factory needs a separate manufacturing assessment and a separate estimate; the practice
knowledge in this skill will under-scope it.

**13 Demand Planning points here for anything that looks like material requirements planning.** The honest
answer that file expects to find is this: what is described below is order-driven transformation, not planned
production. If the requirement is genuinely "plan material and capacity ahead of demand across levels", say
so early and price it as manufacturing scope.

## 2. The four sourcing models

Every wholesale channel in the reference model offered these four, and a real order book carries more than one:

| Model | Thai | What the system has to do |
|---|---|---|
| Collection product | สินค้าใน Collection | sell from stock — the simple case |
| Made to order | สั่งผลิต | the order triggers procurement or production; goods received, then shipped |
| Transformation, **item code changes** | แปรสภาพ – เปลี่ยน Item# | consume a blank, produce a **different sellable item** |
| Transformation, **item code unchanged** | แปรสภาพ – ไม่เปลี่ยน Item# | add value; the item stays the same and its cost rises |

### The change-item decision, and how to advise on it

**Change the item code when** the output is independently sellable and needs its own demand history, its own
price and its own stock position — a licensed jersey, a catalogue-listed customised line. The price of that
choice is item-master proliferation, and somebody must own the creation and retirement of codes.

**Keep the item code when** the decoration is customer-specific, one-off, and will never be sold to anyone else —
a corporate uniform for a single company, a one-season event batch. The price of that choice is that the added
value has to be carried some other way, and stock visibility no longer distinguishes a decorated unit from a
plain one. Getting this wrong hurts in both directions: proliferate codes for one-off jobs and the item master
becomes unusable, keep one code for genuinely different products and demand cannot be planned or margin reported.

## 3. The outside-processing cycle

The subcontracted flow in the reference implementation, end to end:

1. Sales confirms the order and it lands in the system as a sales order.
2. Merchandising **links a purchase order to the transformation-service charge line on the sales order** and the
   purchase order is created from it. The service fee (ค่าจ้างแปรสภาพ) is an orderable charge item, not free text.
3. Purchasing reviews and approves the subcontract purchase order.
4. Merchandising creates and approves a **transfer order** moving the blanks to the **outside (subcontractor)
   location**, and the warehouse is notified.
5. The warehouse ships the blanks and confirms fulfilment; stock moves to the outside location and receipt at the
   subcontractor is confirmed back.
6. The subcontractor decorates the goods and notifies Merchandising, who inspects.
7. Goods return to the brand's warehouse with the subcontractor's invoice; the warehouse books the physical
   receipt and notifies Accounts Payable and Merchandising.
8. Merchandising passes the transfer documents to Cost Accounting.
9. Cost Accounting **adjusts the material and finished goods out** of the outside location.
10. Cost Accounting **receives the finished goods back in at the cost it determines**.
11. The warehouse fulfils the original sales order and confirms shipment.
12. Accounting raises the customer invoice, and Accounts Payable books the subcontractor's service bill.

**Drop-ship variant.** If the subcontractor ships straight to the end customer, Merchandising prepares the
customer invoice and sends it to the subcontractor to travel with the goods; the subcontractor returns its own
invoice plus the signed customer delivery note, and the payable is booked from there. Nobody in the brand's
warehouse ever sees the finished units, so the inspection step has to be replaced by something — a sample, a
photo, an acceptance note.

**Made-to-stock variant.** The same chain runs against a forecast rather than a specific order. Everything
below about cost applies unchanged; only the trigger differs.

## 4. How transformation cost is set — and the weakness accepted in the reference design

Look closely at steps 9 and 10. The cost of a transformed unit is set by **two inventory adjustments**: one
issuing material and finished goods out of the outside location, one receiving the finished goods back in at
a cost Cost Accounting determines.

**That means the transformed cost is entered by a person. It is not calculated by the system.**

There is no work order backflushing material plus subcontract service plus overhead into a finished cost
automatically. Bill-of-materials master data exists — assembly item, bill of materials, item component —
but the routine transformation flow settles cost through manual adjustment. Raise these consequences with
any prospect running this pattern:

- Transformed-goods margin is only as good as the cost accountant's discipline and timing.
- There is no automatic variance between expected and actual transformation cost, so drift stays invisible.
- The work does not scale — more jobs means proportionally more manual cost effort, with no relief.
- Month-end close depends on Cost Accounting having caught up with the physical flow.

**The improvement path** is to move the routine, repeatable cases onto a work order with a bill of materials and a
subcontract operation, so material and service cost roll into the finished item automatically, keeping manual
adjustment for exceptions only. That is a credible phase-two story and a genuine differentiator in a proposal —
**provided it is offered as an improvement, never implied as already present.**

## 5. Master data the module requires

| Master | Why it exists |
|---|---|
| Outside supplier | the subcontractor, with the terms of the service |
| **Outside location** | where goods sit while they are with the subcontractor — still owned, not sellable |
| Item component | the blanks and materials consumed |
| Other charge for purchasing | the transformation service fee as an orderable line |
| Assembly item | the transformed output where it is a distinct product |
| Bill of materials | what goes into the transformed item |

**The outside location is the piece most often forgotten.** Goods at a subcontractor remain the brand's asset and
still have to be counted, valued and insured, yet they must not appear in availability to sell. That is the same
"own it but cannot sell it" logic behind the location groups in **11** — go there for topology and costing method.

## 6. Control and verification

The module carries its own verification set, which is a good sign that the design has met reality: **verify
stock at outside process** (what is physically with subcontractors right now) · **verify outstanding
subcontract purchase orders** (which service orders are still open) · **verify outstanding work orders** for
the made-to-stock variant (which transformation jobs are running) · **verify cost** (whether the cost adjustments
have actually been done). The last one exists precisely because the costing is manual. If a client adopts the
manual approach, adopt this report with it and put it in the month-end checklist — otherwise §4 has no detector.

## 7. Made-to-order linkage to procurement

For made-to-order goods that are bought rather than transformed, the chain runs sales order → purchase
requisition → purchase order → receipt into a supplier-linked location → fulfilment to the customer. The
reference implementation recorded **automatic creation of the purchase requisition from the sales order as a gap
requiring a custom interface** — worth knowing, because prospects routinely assume that link is standard. Approval
routing, supplier terms and receipt handling belong to **14 Procurement**; only the sales-order trigger sits here.

## 8. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Transformation **service fee as an orderable charge item** on the sales order | the fee must be priced, taxed and billed like any other line, not typed as a cost note | standard master data, deliberate design |
| 2 | **Purchase order linked to the service charge line** of the sales order | ties subcontract spend to the job that caused it; without it, job margin is guesswork | standard link, usually needs configuration |
| 3 | **Outside location** excluded from available-to-promise but included in valuation | goods are owned, counted and insured, yet not sellable | standard, governance-dependent |
| 4 | Transfer order out to, and receipt back from, the outside location | the physical movement must be a stock transaction, not a note | standard |
| 5 | **Both transformation models** — item code changes and item code unchanged | a real order book carries both, and they cost differently | standard, needs a naming and ownership rule |
| 6 | Item-code creation and retirement **governance** for transformed outputs | the item master degrades fast without a named owner | process, not software |
| 7 | Cost adjustment in and out of the outside location, with the entered cost visible and auditable | this is where transformed cost is actually set | standard, manual by design |
| 8 | **Work order with bill of materials and subcontract operation** for repeatable jobs | removes the manual cost step for the routine cases | standard capability, phase-two scope |
| 9 | Verification reports — stock outside, open subcontract orders, open work orders, cost done | the only detector for uncosted or stranded jobs | saved searches or reports |
| 10 | **Drop-ship path** — customer invoice prepared before goods move, delivery note returned as proof | the subcontractor ships direct and the brand never touches the goods | custom document flow |
| 11 | Automatic purchase requisition from a made-to-order sales line | recorded as a gap in the reference implementation | custom interface |
| 12 | Job-level margin reporting — sale value against material plus service cost | the whole reason for linking the purchase order to the order line | reporting, depends on 2 and 7 |

Functions 2, 5, 7, 8, 10 and 11 are where the effort concentrates. The rest is broadly mainstream.

## 9. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Transformed cost set by hand** | two inventory adjustments, cost entered by Cost Accounting | work order with bill of materials and subcontract operation for repeatable jobs; manual adjustment kept for exceptions |
| **No expected-versus-actual variance on transformation** | none — drift is invisible until someone looks | carry a standard transformation cost per job type and report the variance |
| **Goods at the subcontractor invisible or wrongly sellable** | dedicated outside location plus a verification report | make the location non-available by design and count it in the stock-take cycle |
| **Item codes proliferate, or collapse into one** | both models supported, the decision left to the business | write the rule during design — independently sellable means a new code, one-off customer work does not |
| **Purchase requisition assumed to raise itself from the order** | recorded as a gap needing a custom interface | verify in discovery and price the interface as a line item |
| **Drop-ship treated as a normal shipment** | separate document flow, customer invoice travelling to the subcontractor | design inspection and proof of delivery explicitly, since nobody at the brand sees the goods |
| **Month-end closed before costing caught up** | the verification-of-cost report | put that report in the close checklist with a named owner |
| **Full manufacturing sold as transformation** | out of scope of the reference design | say so early; multi-level planning is a separate assessment and a separate estimate (see §1) |

### Scoping signals — raise the estimate when you see

Decoration or personalisation as a routine part of the order book rather than an occasional favour · both
transformation models in scope · subcontractors shipping direct to end customers · a requirement for accurate
margin per transformed job · made-to-order volume that expects automatic requisition creation · several subcontractors
with different lead times feeding one customer order · in-house decoration alongside subcontracted decoration.

## 10. Discovery questions

1. What share of your orders involves decoration, printing, embroidery or personalisation? ⚑ *(routine rather
   than occasional changes the estimate materially)*
2. When you decorate a blank, does it become a new product code today, or stay the same one? ⚑
3. Who does the decoration — your own operation, subcontractors, or both?
4. While goods are with a subcontractor, how do you know what is there and what it is worth?
5. How is the cost of a decorated item determined today — calculated by the system, or set by an accountant?
   ⚑ *(the question that exposes the weakness in §4)*
6. Do any subcontractors ship directly to your customers? ⚑
7. For made-to-order goods, how does the purchase order get raised from the customer order today? ⚑
8. Do you need margin per transformed job, or is margin at product level enough? ⚑
9. Do you plan material and capacity ahead of orders, across more than one level of bill of materials? ⚑ *(a
   yes moves the work outside the scope of this practice — see §1)*
10. How long does a decoration job take from blank issued to finished goods received, and what happens to the
    customer order while it is out?

## Related files

- **00-09** — the channels where transformed and made-to-order product is actually sold
- **11 Inventory and Item Costing** — location topology, the outside location, and the costing method inherited here
- **15 Finance, Ledger and Assets** — where the transformation cost finally lands in the ledger, and the dimensions it must carry
- **13 Demand Planning** — forecasting and replenishment; the planned-production boundary is set in §1
- **14 Procurement** — the subcontract purchase order, supplier terms, approval and receipt
- **19** — the full discovery bank
