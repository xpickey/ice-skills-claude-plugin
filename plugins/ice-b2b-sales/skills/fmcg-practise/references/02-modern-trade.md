# 02 — Modern Trade (โมเดิร์นเทรด)

> **Load this when:** the prospect sells into department stores, hypermarkets, supermarkets,
> convenience chains, specialty chains or cash-and-carry · the words "key account", "sale-in",
> "sale-out", "EDI" or "the buyer" appear · they have a trading agreement with a retail group.
> **Do not load this for:** the money the retailer takes back — listing fees, rebates, promotions,
> deductions, disputes, Net GP → go to **10 Trade Spend and Net GP**, which is a domain in its own
> right and is where most of the scope actually is.
> **Source basis:** both reference implementations. The apparel case supplies the order-to-cash
> chain and the consignment mechanics; the food and beverage case supplies the trade-agreement and
> deduction depth. Thai EDI market position is from a public service-provider source.

## 1. Use cases — what this channel actually is

Modern trade is **the channel, not the commercial arrangement**. Organised retail is where the goods
go. How the brand gets paid for them varies *within* that same channel, and frequently within the
same retailer group.

Three arrangements run through modern trade, and a real account often carries more than one:

| Arrangement | Thai | Tax invoice at | Debtor | Unsold stock owned by |
|---|---|---|---|---|
| **Outright sale** | ขายขาด | shipment, net of any deposit | retailer head office | the retailer |
| **True consignment** | ฝากขายแท้ | **sale-out** | the retailer | **the brand** |
| **Pseudo consignment** | ฝากขายเทียม | **delivery** | the retailer | the brand commercially, though invoiced |

**The recognisable situations:**

A brand supplying a hypermarket group buys its way onto the shelf with a listing fee, ships against
purchase orders, and is paid on terms less whatever the retailer decides to deduct. A department
store operates the same brand as a **counter** — the brand's own merchandiser stands on the floor,
the stock is still the brand's, and revenue only exists when a shopper buys. A convenience chain
takes small, frequent deliveries against a central distribution centre. All three are "modern trade"
to the sales director, and all three need different accounting.

Two structural facts about retail markets shape the master data before any transaction exists.
First, **a small number of groups own many banners** — so the master needs a parent group above the
banner, or the brand cannot see its true exposure or its real negotiating position. Second,
**groups merge, split and re-brand banners**, so the re-map must be effective-dated and must not
restate prior-period reporting.

### How to classify a specific account

Ask **per category or per counter**, never per retailer:

1. *"After delivery, if the goods do not sell, who carries them on their balance sheet?"*
   → the retailer means outright · the brand means consignment.
2. *"When do you have to issue the tax invoice — when you deliver, or when it sells?"*
   → delivery means outright or pseudo consignment · on sale means true consignment.

The **consignment mechanics themselves — transfer versus sales order, the shadow book, the sale-out
feed, reconciliation — live in file 03.** What this file adds is that they sit in the *same customer
account* as the outright business and must reconcile together at period end.

### Sale-in and sale-out in this channel

| Term | Thai | Meaning |
|---|---|---|
| **Sale-in** | ยอดขายเข้า | the brand sells to the retailer — **the revenue event where the arrangement is outright** |
| **Sale-out** | ยอดขายออก | the retailer sells to the shopper — **the revenue event where the arrangement is consignment**; management information where it is outright |

In the outright portion, sale-out is still worth capturing: it drives replenishment, promotion
effectiveness and forecasting. But it is **not an accounting event there**, and a design that treats
it as one will double-count. See the two-senses warning in file **00**.

## 2. Process — the flow

### Outright sale

```
Trade agreement in force (annual, versioned)
  → order arrives: retailer portal · file import · EDI · brand's own order screen
  → credit-limit and overdue check · stock check
  → sales order + reservation created
  → [deposit branch] deposit receipted separately, its own tax invoice, VAT on the deposit
  → release to warehouse → fulfilment → confirmation back
  → STOCK RELIEVED, cost of sales posted
  → invoice / tax invoice raised, net of deposit — only from a fulfilment in shipped status
  → invoice travels with the goods where the retailer requires it
  → billing on the agreed credit term
  → payment arrives SHORT  →  hand off to file 10
```

The last line is the one that matters. In this channel the payment almost never matches the invoice,
and everything downstream of it is a separate domain.

### Consignment portion

Runs the flow in file **03** — transfer or sales order out, then a periodic sale-out feed that
creates revenue (true model) or relieves the shadow book (pseudo model) — but **against the same
customer account** as the outright business.

### Where orders actually come from

| Route | What it is | Reality |
|---|---|---|
| **Retailer portal** | the retailer's own supplier website | common; often means someone re-keys into the ERP |
| **File or template import** | agreed spreadsheet or flat file | what shipped in the apparel case when EDI proved unavailable for that counterparty |
| **EDI via a service bureau** | one provider exchanges with many retailers | available in Thailand, covering the major chains and six document types |
| **Direct EDI to the retailer** | point-to-point per chain | heaviest option; one interface per retailer, forever |
| **Brand's own order screen** | staff enter on behalf of the account | delivered as a customisation in the apparel case, to let staff pick items, check stock and create an order quickly |

### EDI in the Thai market — what is actually available

EDI **is** commercially available through a **service-bureau model** covering the large chains, and
it supports six document types: purchase order · invoice · advance ship notice · credit note
request · remittance advice · return to vendor. It is positioned at suppliers with no EDI
infrastructure of their own.

**The trap:** it is accessed through a web portal. A supplier saying "we already have EDI" may be
describing a person reading that portal and typing into the ERP — which is exactly the manual step
the project exists to remove. **The bureau does also offer system-level integration to a supplier's
ERP over standard business-to-business transport protocols**, so bureau-integrated is achievable;
it is not portal-only.

**The message standard is not published.** Do not design a mapping against an assumed standard — ask
the client for a sample file, and specify the interface by capability in a proposal.

**Sales reporting and stock-on-hand reporting are absent from the six document types.** Sale-out
capture must therefore be designed as its own path — portal download, merchandiser application, or a
negotiated feed. It does not arrive through EDI. That matters most for the consignment portion,
where sale-out *is* the revenue event.

One recorded outcome worth carrying, with the right lesson attached: in the apparel implementation
the tender asked for sale-in capture through an EDI provider and the outcome was recorded as a gap —
that counterparty could use EDI for purchase orders only. **Read that as a limitation of one
counterparty, not of the Thai market.** Verify per retailer and per document type.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | Retailer and banner master with a **parent group** above the banner | groups own several banners; consolidated exposure and negotiating position are per group | standard master data, custom hierarchy field |
| 2 | **Effective-dated banner re-mapping** that preserves reporting history | retail groups merge and re-brand; a simple overwrite silently restates prior periods | usually custom |
| 3 | Order intake from **multiple routes** into one order structure | portal, file, EDI, internal screen must converge | integration build per route |
| 4 | Credit-limit and overdue check **at order creation**, surfaced to the person entering the order | prevents shipping into a blocked account | standard, plus integration to surface it in the front end |
| 5 | Reservation of stock at order creation | prevents another channel taking the same units | standard |
| 6 | **Deposit handling** — separate receipt, its own tax invoice, VAT on the deposit, netted off the final invoice | common in this channel and mishandled often | standard receipt, custom netting and forms |
| 7 | **Invoice only from a fulfilment in shipped status** | stops billing goods that never left | standard control, worth stating explicitly |
| 8 | Statutory invoice and credit-note **print formats** to each retailer's requirement | Thai preprinted forms differ; recorded as a gap requiring customisation in the apparel case | custom |
| 9 | **Both consignment models** on the same customer account | a real account carries more than one arrangement | see file 03 — largely custom |
| 10 | **Sale-out capture** independent of the EDI channel | EDI does not carry it, and consignment revenue depends on it | custom or third-party |
| 11 | **Sale-out to invoice reconciliation** with variance reporting | catches missing and duplicated sale-in; delivered via saved searches in the apparel case | standard reporting |
| 12 | Returns in two forms — **with goods return**, and **credit note only** | trade allowances and price corrections must not be forced through a goods-receipt path | standard, needs deliberate design |
| 13 | Channel and banner **reporting dimension** on every transaction | per-retailer margin is impossible without it | standard, governance-dependent |
| 14 | **Discount and promotion write-back** onto the sales line — amount, type, campaign code, funder | the front end decides the discount; the ERP must record it or no margin analysis is possible | integration design |

Functions 1, 2, 9, 10 and 14 are where the effort concentrates. Everything else is broadly
mainstream.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Customer creation and amendment | CRM → ERP, result back | asynchronous | account, addresses, contacts, credit terms |
| Credit and overdue check | front end → ERP | **synchronous** — a human is waiting | limit remaining, overdue flag |
| Stock availability check | front end → ERP | synchronous | on-hand and available |
| Order creation and reservation | front end or portal → ERP | synchronous | order header and lines, **with price detail and discount breakdown** |
| Order status back | ERP → front end | asynchronous | fulfilment and invoice status |
| Product and price list master | ERP → front end | batch | item, unit of measure, base price |
| Order import from file or bureau | file or EDI → ERP | asynchronous | order lines mapped to internal items |
| Warehouse release and confirmation | ERP ↔ warehouse | asynchronous | fulfilment instruction, picked and packed confirmation |
| Sale-out feed | retailer or merchandiser system → ERP | asynchronous, usually daily | sale-out lines by store and item |
| Electronic tax document | ERP → tax service | batch | signed invoice and credit note documents |

**Rule of thumb:** synchronous only where a human is waiting for the answer — credit, stock, order
creation. Everything else asynchronous, with a visible status so users are not left guessing.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementations did | What a better design looks like |
|---|---|---|
| **Modern trade designed as one commercial model** | the apparel design initially separated consignment into its own channel, leaving a real account split across two designs | classify per category or counter; keep all arrangements on one account and reconcile together at period end |
| **EDI capability assumed rather than verified** | recorded as a gap after the tender had already promised it; fell back to file import plus a custom order screen | verify per retailer **and per document type** before fixing the estimate; propose bureau-integrated as the default architecture |
| **Sale-out capture forgotten because EDI was assumed to carry it** | delivered through the merchandiser device path | design sale-out capture as its own path from the start; it feeds both consignment revenue and forecasting |
| **Statutory print formats underestimated** | four Thai preprinted invoice and credit-note forms, all custom | count the formats per retailer during discovery and price them as line items |
| **Deposit VAT and netting handled manually** | custom programs for deposit receipt, VAT on deposit, and netting | make it part of the standard order-to-cash configuration, not an afterthought |
| **Discount and promotion invisible in the ERP** | the ERP held only a base price; discounting lived in front-end systems | keep that architecture — it is correct — but require the **write-back** of amount, type, campaign code and funder onto the sales line |
| **Deductions treated as "a report"** | the food and beverage design treats it as fifteen screens across intake, matching, dispute, accrual, tax and reporting | scope it as its own domain — file **10** |
| **Trade terms benchmarking** | — | **no defensible Thai market figure exists** for listing fees, rebate levels or deduction rates. Ask the client; never quote a number |

## 6. Discovery questions

1. Which retail groups do you supply, and which banners sit under each? *(shapes the master data)*
2. For each category or counter — **if the goods do not sell, who owns them?** ⚑ *changes the estimate materially*
3. For each — **when must the tax invoice be issued: on delivery or on sale?** ⚑
4. How do orders reach you today from each retailer — portal, file, EDI, phone? Does any of it touch your ERP, or is it re-keyed? ⚑
5. Which document types do you exchange electronically with each retailer? *(coverage is per retailer and per document, not one answer)*
6. How do you receive sale-out data today, and from which retailers?
7. How many different statutory invoice and credit-note formats do your retailers require?
8. Do you take deposits in this channel? How is the tax invoice on the deposit handled?
9. Where are discounts and promotions decided — in your sales system, on the retailer's terms, or in the ERP? Does the ERP see the breakdown? ⚑
10. When a retailer short-pays, how do you find out why — and what proportion is never explained? ⚑ *(this opens file 10)*
11. Do you know your margin **after** everything the retailer takes back, by retailer and by item?

## Related files

- **00** channel map and the classification method
- **03** consignment — the mechanics of both models
- **10** trade spend and Net GP — deductions, rebates, disputes, the real margin
- **13** demand planning — where sell-through becomes a forecasting signal
- **17** Thailand compliance — electronic tax documents and their effect on this channel
- **19** the full discovery bank and what typically delays these programmes
