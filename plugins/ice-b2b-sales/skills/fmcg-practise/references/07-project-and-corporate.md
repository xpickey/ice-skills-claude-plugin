# 07 — Project and Corporate (ลูกค้าองค์กร / โครงการ)

> **Load this when:** the buyer is an organisation purchasing for its own use rather than for
> resale — a government agency, a state enterprise, a private company, a school, a club · you hear
> "โครงการ", "จัดซื้อจัดจ้าง", "TOR", "สัญญาสิทธิประโยชน์", "สโมสร", "ชุดพนักงาน" or "VIP" · the goods
> are usually made or decorated against a named requirement rather than picked from stock.
> **Do not load this for:** a dealer or shop reselling the goods → **01** · organised retail →
> **02** · an overseas organisation → **08** · the decoration and make-to-order mechanics
> themselves → **12** · staff purchases and giveaways, which look corporate but are not sales →
> **09**.
> **Source basis:** the apparel reference implementation documents this channel with the **same
> process spine as traditional trade** — identical requirement rows, identical integrations,
> step-for-step identical flows. Several things a project business expects — milestone billing, a
> project master, pipeline structure — are **absent from that source**, and section 5 says so rather
> than inventing them.

## 1. Use cases — what this channel actually is

The distinguishing fact is not the size of the order. It is that **the buyer consumes the goods
instead of reselling them**, and that the sale usually starts as an opportunity against a stated
requirement — a tender, a uniform specification, a sponsorship agreement, an event — long before
anything exists that an ERP would recognise as an order.

The recognisable situations: a ministry or state enterprise buying staff uniforms through a
procurement process with its own documentation rules; a private company ordering branded kit for a
campaign; a sports club whose sponsorship contract entitles it to draw down team kit over a season;
an internal VIP or brand project where the goods are made for a purpose rather than for a market.

| Sub-variant | Thai | What behaves differently |
|---|---|---|
| **Government and state enterprise** | ภาครัฐ / รัฐวิสาหกิจ | procurement rules, tender documentation, bid bonds and portal obligations sit outside the ERP but constrain the paperwork it must produce |
| **Private enterprise** | ลูกค้าองค์กรเอกชน | closest to ordinary wholesale; a purchase order and a credit term, with made-to-order as the norm |
| **Club or sponsorship rights contract** | สัญญาสิทธิประโยชน์ (สโมสร) | the contract, not the order, is the commercial object; entitlement is drawn down over time and some of what is owed is not a goods delivery at all |
| **Internal or VIP project** | โครงการ / Project VIP | no external procurement process; the constraint is a delivery date tied to an event |

**The three defining facts.** The **debtor is the organisation** — a single, usually
well-capitalised counterparty rather than a spread of small shops. **Unsold stock is a near-moot
question**, because the goods are made against a named requirement and there is rarely a residual
the brand carries. The **tax point** is the one to handle carefully: the channel map (**00**) records
this channel as invoicing *per milestone or on shipment*, and both do occur in the market — but **in
the reference implementation the invoice was always raised on shipment**, with a single deposit
netted against one final invoice. Staged billing is therefore the general shape of the channel, not
documented practice from the source. Treat it as scope to be confirmed, not as capability to be
assumed.

### Why this is not a separate process

The reference implementation's design documents for traditional trade and project sales are, at
process level, identical — the same requirements, the same integration list, the same step
sequences. Channel identity is carried in a **customer-master segment**, and process variation comes
from **payment term and sourcing model**, not from the channel. The full statement of that finding,
the credit chain, the deposit chain and the pricing write-back all live in file **01** and are not
repeated here. What follows is only what is genuinely different.

## 2. Process — the flow

### What the reference actually ran

```
front office: opportunity created against a requirement or tender
  → quotation prepared and accepted             (opportunity status fed back to the front office)
  → stock check · credit-limit check · overdue check
  → sales order created + reservation           status = APPROVED (credit) | PENDING (cash)
  → [deposit branch] deposit receipted, VAT charged, tax invoice issued on the deposit
  → [cash branch] payment evidence uploaded → finance approves release → status APPROVED
  → sourcing tail:  stocked  |  made to order (requisition → purchase order → supplier location)
                    |  transformation (own stock transferred out, production request raised)
  → production status maintained on the sales order, BY HAND
  → order fulfilment                            status = PICKED → PACKED → SHIPPED
  → STOCK RELIEVED, cost of sales posted
  → invoice / tax invoice raised, net of any deposit — only from a fulfilment in shipped status
  → billing note on the agreed term → receipt → cash applied
```

The garment tail is the visible difference from file **01**: on a made-to-order project the sales
order carries a **production status list** through the making stages — greige preparation, dyeing,
cutting, printing or embossing, embroidery, sewing, quality control — before it reaches picking and
packing. In the reference these statuses were **updated manually by the merchandising team**, with no
automated feed from the maker, and the order line carried a **dummy item** until the real item
existed. Both are stated limitations of that design, not recommendations.

### What a project business commonly expects, and the source does not show

Mark these as **design intent to be confirmed, not verified practice**:

| Expectation | Status in the source |
|---|---|
| Contract or project as a header above the orders | **absent** — no project code, project master, work-breakdown or contract reference field exists; orders are referenced only by sales order and customer |
| Billing in progress stages (งวดการวางบิล) | **absent** — the only staged mechanism is one deposit netted off one final invoice |
| Delivery in tranches against one commitment | **absent as a structure**; achievable by raising several orders, which loses the commitment view |
| Pipeline stages, forecast category, win or loss handling | **absent** — the only opportunity-level artefact is a status update passed back to the front office |
| Entitlement drawdown under a sponsorship or club contract | **absent** — the customer code distinguishes club accounts, and one code marks a contract with drawdown over time, but no drawdown ledger is designed |
| Retention, performance bond, tender deposit | **absent** — no equivalent of a deposit that is held rather than earned |

The honest reading: this reference implemented **project selling as wholesale with made-to-order
sourcing**. That is enough for corporate uniform and event business. It is **not** enough for a
prospect who bills in stages, tracks commitment against a contract, or reports a pipeline — and each
of those is a distinct scope item with its own build, not a configuration switch.

### Transformation and made-to-order work

Most project business runs on it, which puts file **12** on the critical path of the estimate.
Nothing about decoration, item-code creation, subcontracting or work orders is repeated here. The
requisition-to-payment chain that made-to-order triggers belongs to procurement.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **Opportunity against a requirement**, with its status visible to the ERP side | the commercial life of a project starts long before an order | standard in a front office; the feedback link is an interface |
| 2 | **Quotation converted to a sales order** without rekeying | the quoted specification is the contract | standard |
| 3 | **Contract or project reference on the order**, and reporting grouped by it | otherwise several deliveries against one commitment cannot be seen together | **not present in the reference** — assume custom |
| 4 | **Commitment versus drawn-down view** for club and sponsorship contracts | the obligation is an entitlement, not an order | not present in the reference — custom |
| 5 | **Staged or milestone billing** against a schedule | if the prospect bills in progress stages, nothing in a deposit mechanism substitutes | not present in the reference — scope it explicitly |
| 6 | **Deposit handling** — receipt, VAT on the deposit, its own tax invoice, netting on the final invoice | deposits are the norm here, not the exception | standard receipt; VAT and netting usually custom |
| 7 | **Automatic requisition from the sales order** for made-to-order lines | the alternative is rekeying every project order into purchasing | custom in most products |
| 8 | **Production status on the sales order**, through the making stages | the question the customer asks weekly is "where is my order" | field is standard; an automated feed behind it is the hard part |
| 9 | **Transformation sourcing** — own stock out to a subcontractor, decorated goods back | see file **12** | largely custom |
| 10 | Credit-limit and overdue check at order creation | a large single order concentrates exposure that many small ones spread | standard, plus front-end integration |
| 11 | **Cash-sale release gate** — payment evidence, finance approval, then release | common where the buyer is new or the order is large | standard approval plus custom evidence capture |
| 12 | **Invoice only from a fulfilment in shipped status** | stops billing goods that never left | standard control |
| 13 | Statutory Thai preprinted document formats | government buyers are unforgiving about document form | custom report development |
| 14 | **Tender and procurement document output** — the formats the buyer's process demands | sits outside the ERP but constrains what it must be able to print or export | usually manual or custom |
| 15 | Returns in two forms — with goods return, and credit note only | specification disputes on made-to-order goods land here | standard, needs deliberate design |
| 16 | **Discount and promotion write-back** onto the sales line | project pricing is negotiated in the front office; the ERP must still record what was granted | integration design — detail in file **01** |

Rows 3, 4 and 5 are the ones to price honestly. They are absent from the reference implementation, so
a proposal that implies they come as standard is making a promise the evidence does not support.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Customer creation and amendment | front office → ERP, result back | asynchronous | organisation, addresses, contacts, credit terms |
| Opportunity status update | front office ↔ ERP | synchronous | opportunity and order status tracking |
| Stock availability check | front office → ERP | synchronous | on-hand and available |
| Credit and overdue check | front office → ERP | **synchronous** — a human is waiting | credit remaining, overdue flag |
| Sales order creation and reservation | front office → ERP | **synchronous** | order header and lines, **with price detail and discount breakdown** |
| Requisition raised from the sales order | ERP internal | event-driven | made-to-order lines into purchasing |
| Production or subcontract status | maker → ERP | **manual in the reference** | making-stage status on the sales order |
| Picking instruction and warehouse confirmation | ERP ↔ warehouse operator | asynchronous | fulfilment instruction, packed confirmation |
| Invoice document to the warehouse operator | ERP → warehouse operator | file transfer | tax invoice travelling with the goods |
| Electronic tax document | ERP → tax service | batch | signed invoice and credit note — see file **17** |

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Project sold as a separate process** | recognised it as the same process family as traditional trade, differing by payment term and sourcing model | resist a per-channel process; put the difference in customer coding, contract reference and tax point |
| **Milestone billing assumed to exist** | **not designed** — one deposit netted against one final invoice was the only staged mechanism | ask the billing question in the first workshop; a progress-billing schedule is a build, and it changes revenue recognition as well as invoicing |
| **No project or contract header** | **not designed** — orders reference only the sales order and the customer | if several deliveries belong to one commitment, add the header early; retrofitting it means restating history |
| **Sponsorship and club obligations treated as ordinary orders** | the customer code marks club accounts, one value covering a contract drawn down over time; no drawdown ledger exists | model entitlement and drawdown explicitly, including obligations that are not goods |
| **Production visibility promised, then hand-maintained** | manual status updates on the sales order, plus a dummy item until the real item exists | agree what the maker can actually feed back before promising order tracking to the sales team |
| **Made-to-order requisition rekeyed** | automatic requisition creation from the sales order, recorded as a customisation | design it in, and price it; it is not standard in most products |
| **Tender obligations discovered late** | outside the documented ERP scope | list the buyer's document formats, bonds and portal duties during discovery — they are effort even when they are not system scope |
| **Retention and bonds** | **no mechanism designed** — genuinely unknown territory in this source | if the prospect's contracts hold money back, treat it as unresearched and ask; do not assume the deposit mechanism covers it |

## 6. Discovery questions

1. Who is the buyer — do they consume the goods themselves, or do they resell? *(this is the
   question that separates this file from **01**)*
2. **Do you bill a project in stages, or once on delivery?** If in stages, what triggers each
   stage — a date, a delivery, an acceptance? ⚑ *changes the estimate materially*
3. Is there a contract or project that several orders belong to, and do you need to see them
   together? ⚑
4. For club or sponsorship agreements — what is the customer entitled to, over what period, and who
   tracks what has been drawn down? ⚑
5. Do your contracts hold money back — retention, performance bond, tender deposit? ⚑
6. Do you take deposits, and how is the tax invoice on the deposit handled?
7. Of your project orders, what proportion is made to order or decorated to order rather than
   supplied from stock? ⚑ *this puts file 12 on the critical path*
8. Once production starts, how does the customer find out where their order is — and who updates
   that today?
9. For government buyers, what documents and formats does their procurement process demand from
   you?
10. Where is project pricing decided and approved, and does the ERP receive the discount breakdown
    or only the net amount? ⚑
11. When a project delivery is rejected on specification, what happens — goods back, or a credit
    note only?

## Related files

- **00** channel map and the classification method
- **01** traditional trade — the shared process spine, credit management, deposits, returns and the
  pricing write-back, none of which are repeated here
- **08** export — the same spine again, for organisations outside the country
- **09** event, employee and complimentary — staff and giveaway movements that look corporate but
  are not sales
- **11** inventory, locations and costing — including the supplier-linked locations this channel
  uses
- **12** make to order and transformation — on the critical path of almost every project estimate
- **17** Thailand compliance — electronic tax documents. **The VAT treatment of deposits is not
  covered there** and is an open question for the client's adviser
- **19** the full discovery bank and what typically delays these programmes
