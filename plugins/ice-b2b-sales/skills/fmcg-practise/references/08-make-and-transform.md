# 08 — Make to order and transformation (แปรสภาพ): the apparel differentiator

> Load this when the brand personalises, decorates, prints, embroiders, assembles or
> subcontracts finishing — team kit, corporate uniform, licensed product, promotional goods,
> or anything made against a customer order rather than sold from the shelf.
> This is the module that separates an apparel or promotional-goods brand from a plain distributor.

## Why this exists as its own module

A distributor buys finished goods and sells them. An apparel or sportswear brand often sells a
**blank that becomes a specific product only after decoration** — a club name, a sponsor logo, a
player's number, a corporate identity. The same physical garment can become dozens of different
sellable products.

The reference implementation treats this as a distinct process area — **Outside Process
(สินค้าแปรสภาพ)** — sitting alongside procure-to-pay, order-to-cash and inventory. That structural
choice is itself the lesson: transformation is not a variation of purchasing and not a variation of
selling. It touches both, and it has its own master data, its own stock location, and its own cost
event.

## The four sourcing models, restated

Every wholesale channel in the reference model offers these four:

| Model | Thai | What the ERP has to do |
|---|---|---|
| Collection product | สินค้าใน Collection | sell from stock — the simple case |
| Made to order | สั่งผลิต | order triggers procurement or production; goods received, then shipped |
| Transformation, **item code changes** | แปรสภาพ – เปลี่ยน Item# | consume a blank, produce a **different sellable item** |
| Transformation, **item code unchanged** | แปรสภาพ – ไม่เปลี่ยน Item# | add value; the item stays the same, its cost rises |

### The change-item decision, and how to advise on it

**Change the item code when** the output is independently sellable and needs its own demand
history, its own price, and its own stock position — a licensed club jersey, a catalogue-listed
customised line. The cost of this choice is item-master proliferation, and someone must own the
creation and retirement of those codes.

**Keep the item code when** the decoration is customer-specific, one-off, and will never be sold to
anyone else — a corporate uniform for one company, a one-season event batch. The cost of this
choice is that the added value has to be carried some other way, and stock visibility no longer
distinguishes a decorated unit from a plain one.

Get this wrong in either direction and it is painful: proliferate codes for one-off jobs and the
item master becomes unusable; keep one code for genuinely different products and you cannot plan
demand or report margin.

## The outside-processing chain (made to order)

The subcontracted flow in the reference implementation, end to end:

1. Sales confirms the order; it interfaces into the ERP as a sales order.
2. Merchandising **links a purchase order to the transformation-service charge line on the sales
   order** — the ERP creates the purchase order automatically. The service fee (ค่าจ้างแปรสภาพ) is
   an orderable charge item, not a free-text cost.
3. Purchasing reviews and approves the subcontract purchase order.
4. Merchandising creates and approves a **Transfer Order** moving the blanks to the **outside
   (subcontractor) location**; the warehouse is notified.
5. The warehouse ships the blanks and confirms fulfilment; stock moves to the outside location, and
   the receipt at the subcontractor is confirmed back.
6. The subcontractor decorates the goods and notifies Merchandising, who inspects.
7. Goods return to the brand's warehouse with the subcontractor's invoice; the warehouse books the
   physical receipt and notifies Accounts Payable and Merchandising.
8. Merchandising passes the original transfer documents to **Cost Accounting**.
9. Cost Accounting **adjusts the raw material and finished goods out** of the outside location.
10. Cost Accounting **receives the finished goods back in at the cost it determines**.
11. The warehouse fulfils the original sales order and confirms shipment.
12. Accounting raises the AR invoice to the customer.
13. Accounts Payable books the subcontractor's bill for the service fee.

**Drop-ship variant:** if the subcontractor ships directly to the end customer, Merchandising
prepares the customer invoice and sends it to the subcontractor to travel with the goods; the
subcontractor returns its own invoice plus the signed customer delivery note, and the payable is
booked from there.

There is also a **made-to-stock** variant of the same chain, where the transformation is done
against a forecast rather than a specific order.

## The costing mechanic — and its honest weakness

Look closely at steps 9 and 10. The cost of a transformed unit is set by **two inventory
adjustments**: one issuing the raw material and finished goods out of the outside location, and one
receiving the finished goods back **at a cost Cost Accounting determines**.

**That means the transformed cost is entered by a person, not calculated by the system.**

There is no work-order backflush computing material plus subcontract labour plus overhead into a
finished cost automatically. The bill of materials exists in the master data (manage assembly,
manage bill of materials, manage item component) but the routine transformation flow settles cost
through manual adjustment.

**Consequences to raise with any prospect doing this:**
- Transformed-goods margin is only as accurate as the cost accountant's discipline and timing.
- There is no automatic variance between expected and actual transformation cost, so drift is
  invisible until someone looks.
- The process does not scale linearly — twice the jobs is roughly twice the manual cost work.
- Month-end close depends on Cost Accounting having caught up with the physical flow.

**The improvement area:** move the routine cases onto a work order with a bill of materials and a
subcontract operation, so material and service cost roll into the finished item automatically, and
keep manual adjustment for exceptions. That is a credible phase-two story and a legitimate
differentiator in a proposal — provided it is offered as an improvement, not implied as already
present.

## Master data the module requires

| Master | Why it exists |
|---|---|
| Outside supplier | the subcontractor, with the terms of the service |
| Outside location | where the goods sit while they are with the subcontractor — still owned, not sellable |
| Item component | the blanks and materials consumed |
| Other charge for purchasing | the transformation service fee as an orderable line |
| Assembly item | the transformed output where it is a distinct product |
| Bill of materials | what goes into the transformed item |

**The outside location is the piece most often forgotten.** Goods at a subcontractor are still the
brand's asset and still need to be counted, valued and insured — but they are not sellable and must
not appear in availability. This is the same "own it but cannot sell it" logic that drives the
eight location groups in file 07.

## Control and verification processes

The module carries its own verification set, which is a good sign of a design that has met reality:

- **Verify stock (outside process)** — what is actually with subcontractors right now
- **Verify purchase orders outstanding (outside process)** — which subcontract orders are open
- **Verify work orders outstanding (made to stock)** — which transformation jobs are running
- **Verify cost** — whether the cost adjustments have been done

That last one exists precisely because the costing is manual. If you adopt the same manual approach
for a client, adopt the verification report with it, and put it in the month-end checklist.

## Made-to-order procurement linkage

For made-to-order goods that are bought rather than transformed, the chain runs sales order →
purchase requisition → purchase order → receipt into a supplier-linked location → fulfilment to the
customer. The reference implementation recorded **auto-creating the purchase requisition from the
sales order as a GAP requiring a custom interface** — worth knowing, because prospects routinely
assume this link is standard.

## Scoping signals

Raise the estimate when you see:
- Decoration or personalisation as a routine part of the order book, not an occasional favour
- Both change-item and keep-item transformation in scope
- Subcontractors who ship directly to end customers
- A requirement for accurate margin per transformed job
- Made-to-order volume that expects automatic requisition creation
- Multiple subcontractors with different lead times feeding one order

## Discovery questions

1. What proportion of your orders involve decoration, printing, embroidery or personalisation?
2. When you decorate a blank, does it become a new product code in your current system, or stay the same one?
3. Who does the decoration — your own operation, subcontractors, or both?
4. While goods are with a subcontractor, how do you know what is there and what it is worth?
5. How is the cost of a decorated item determined today — calculated, or set by an accountant?
6. Do any subcontractors ship directly to your customers?
7. For made-to-order goods, how does the purchase order get raised from the customer order today?

## Related files

- **02** the wholesale channels where transformation is sold
- **07** the outside location inside the wider inventory topology, and the costing method it inherits
- **09** the procurement chain that raises the subcontract order
- **10** how transformation cost lands in the general ledger
- **12** the costing gap and its improvement path
