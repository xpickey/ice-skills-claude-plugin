# 19 — Discovery and Scoping

> **Load this when:** preparing for a first meeting, building a discovery agenda, sizing an
> opportunity, or explaining to a client why a comparable programme ran long.
> **Do not load this for:** per-channel questions — **every channel file carries its own section 6**,
> and they are not repeated here. This file holds what cuts *across* channels.
> **Source basis:** both reference implementations, their recorded gaps and open decisions, plus
> published practice sources. Where a benchmark could not be sourced, this file says so rather than
> quoting one.

## How this file relates to the rest

Each channel file (00–09) and each capability file (10–18) ends with **its own discovery questions**
and its own challenges. This file does three things those cannot:

1. **The opening sequence** — what to ask before you know which channels are in play.
2. **The cross-cutting risks** — what delays these programmes regardless of channel.
3. **Migration and cutover** — the two areas most consistently under-specified.

If you already know the channel, go to that file. Come here first, or when the estimate feels wrong
and you cannot say why.

---

## 1. The opening sequence

### Three questions, asked of every customer group

These are the classification questions from file **00**, and they are the whole opening:

1. **When must the tax invoice be issued?** — on delivery, on sale to the shopper, on payment
2. **Who actually owes you the money?** — the shop, head office, the courier, the platform, the consumer
3. **After delivery, whose balance sheet carries unsold stock?**

Ask them **per category or per counter, not per account**. A retailer group commonly gives different
answers for different parts of its business, and that is precisely what a single answer hides.

### The operating-model test

Four questions that reveal how the business actually runs, independent of channel:

| Question | What a revealing answer sounds like |
|---|---|
| *"Walk me through what happens between a customer deciding to buy and you having the money."* | the number of systems named, and the number of times a person re-keys |
| *"Where do you keep the number you would defend in front of the board?"* | if it is a spreadsheet, that spreadsheet is the real system and the ERP is a ledger |
| *"What did you stop measuring because it got too hard?"* | the abandoned metric is usually the one the project should restore |
| *"Who in this business would notice first if the stock figure were wrong?"* | if nobody, stock accuracy is not yet a felt problem and a business case built on it will not land |

### The channel-count warning, delivered early

The apparel implementation's tender assumed roughly six channels; the finished design carried
fifteen. **Say so at scoping.** A proposal built on the tender's channel count will be wrong, and it
is far better to be the vendor who predicted the expansion than the one who discovers it in build.

---

## 2. What actually delays these programmes

Ordered by how often they bite, from the recorded experience of both implementations.

| # | Area | Why it runs long |
|---|---|---|
| 1 | **Trade spend and deductions** | scoped as "a report", delivered as a domain. File **10** lists twenty functions |
| 2 | **Consignment, where the pseudo model applies** | dual-book mechanics, a synchronisation program, a reconciliation report and a support runbook — none of it configuration |
| 3 | **The integration estate** | counted by system rather than by touchpoint. File **16** counts by group and lands much higher |
| 4 | **Statutory document formats** | one per retailer, each custom, each discovered late |
| 5 | **Channel dimension governance** | never written down, so channel identity ends up in several places and per-channel margin cannot be trusted. File **15** |
| 6 | **Costing grain** | the decision to hold valuation at entity or site level is taken by default and surfaces in user acceptance testing. File **11** |
| 7 | **Promotion and discount visibility** | the ERP receives a net price, so campaign and channel margin can never be analysed. Files **10** and **01** |
| 8 | **Open positions at cutover** | see section 3 |

### The pattern behind the pattern

In both implementations the standard product absorbed the **process** — the order-to-cash spine was
a fit almost everywhere. The gaps clustered in three places, every time:

- **statutory document and tax formats**
- **channel-specific data entry ergonomics** — the screen a sales or store user actually needs
- **mechanics where accounting and physical reality diverge** — dual-book consignment, transformation
  costing, deduction matching

**Use this as a scoping heuristic.** When a requirement falls into one of those three, price it as
custom regardless of what a product datasheet claims. When it does not, expect a fit.

### On benchmark statistics

Published figures on programme overrun and on trade-spend levels exist, but the ranges **disagree
with each other** because the definitions differ, and the accessible ones are vendor-published.
**This skill therefore quotes none.**

When a client asks for benchmarks, the better answer is: *"I would rather show you your own numbers
than someone else's — and in two meetings we can."* It is more useful and more credible than a
statistic they can find themselves and discount.

---

## 3. Migration and cutover — the two under-specified areas

### Migration has three layers, and only two get planned

| Layer | Usually planned? | The risk |
|---|---|---|
| **Master data** — customers, items, prices, locations | yes | cleansing effort underestimated, but visible |
| **Opening balances** — receivables, payables, stock, ledger | yes | reconciliation effort underestimated, but visible |
| **Open positions** — half-finished process instances | **rarely** | the one that breaks go-live |

**The governing question, applied to every process in scope:** *"What does a half-finished instance
of this look like, and where does it go on day one?"*

Worked examples, all real in a multi-channel consumer business: a sales order picked but not
shipped · goods in transit between sites · stock sitting at a consignment counter · a promotion
running across the cutover date · a deduction raised but not yet matched · a dispute filed and
awaiting the retailer's answer · a purchase order partly received · a return authorised but not yet
back.

Each needs a decision **before** the cutover plan is credible.

### Cutover in a multi-channel business

The specific difficulties, which do not arise in a single-channel migration:

- **Channels cannot all pause.** A wholesale order book can be held for a weekend; a marketplace
  cannot. Marketplace orders will not respect a switchover, so the online channels need either a
  parallel period or a defined replay.
- **Order cut-off differs per channel**, because order origin differs. There is no single moment when
  "orders stop".
- **Counting stock requires people who do not work for the client** — consignment counters and
  third-party warehouses. Agree who counts, when, and who arbitrates a difference, well in advance.
- **Trade-spend accruals span the cutover.** An accrual raised in the old system and settled by a
  deduction in the new one needs a route, or it will be settled twice or not at all.

### Phasing

A shape that has worked, **to be validated against the client's own risk appetite rather than
applied as a template**: prove the spine on the least time-critical channel first, then add the
channels whose failure is most visible to consumers, and leave the analytical layer — channel
margin, Net GP, planning accuracy — until the transactional data feeding it is trustworthy.
Delivering the analytics first produces confident reporting of unreliable numbers, which costs more
credibility than delivering them late.

---

## 4. Where the two reference implementations differ — and what that tells you

Reading the two cases against each other is itself a scoping tool, because the differences are the
things a prospect may have that your last project did not.

| Area | Apparel and sportswear | Food and beverage |
|---|---|---|
| Channel breadth | **fifteen customer groups** | organised retail centred |
| Consignment | **both models, fully designed** | not the focus |
| Transformation | **central** — decoration, item-code decisions | absent |
| Trade spend and deductions | **absent** | **fifteen screens, the deepest area** |
| Demand planning | thin | **substantial** — uplift, cannibalisation, accuracy measurement |
| Shelf life and lot control | absent | **central** — first-expired-first-out throughout |
| Van sales | absent | **present**, though not second-pass reviewed |
| Investment-promotion privileges | absent | **present** |

**How to use this table:** it names the eight things most likely to be missing from an estimate
built on a single prior project. Ask about each one. A prospect with shelf-life goods and a
deduction problem is not the same shape as a prospect with decoration and consignment, even though
both are "FMCG multi-channel".

---

## 5. The questions that change an estimate materially

Every channel file marks its own with ⚑. These are the cross-cutting ones:

1. How many distinct customer groups will need different tax-point or debtor treatment?
2. Is any stock held by someone else that you still own — and who counts it?
3. Where are discounts and promotions decided, and does the ERP receive the breakdown or only the net?
4. When a retailer or platform pays you less than the invoice, how do you find out why?
5. Do you decorate, personalise or subcontract any part of the product?
6. Do you have goods with a shelf life or lot traceability requirement?
7. Which financial reporting framework do you apply? *(changes the accrual scope — file 17)*
8. How many statutory document formats do your counterparties require?
9. What must keep running through the cutover, and what can pause?
10. Where is the number the board sees produced today?

---

## 6. Open topics this skill does not yet cover

Stated so nobody assumes coverage that is not there.

- **Demand planning — order-item management only.** Source pages for that topic were image-only and
  unreadable *(the forecast review loop and accuracy reporting are covered in file **13**)*
- **Delivery-performance penalty classification** for tax and accounting — unfound in two research
  rounds
- **Thai market figures** of any kind — retailer trade terms, deduction rates, e-commerce return
  rates, cash-on-delivery share
- **Retailer-by-retailer electronic exchange capability** — must be verified per account
- **Published Thai case studies** of adequate source quality
- **Manufacturing** — file **12** covers transformation and made-to-order work that hangs off a sales
  order, and explicitly excludes multi-level bills of material, routings, capacity and material
  requirements planning, shop-floor scheduling and production variance. **A prospect that runs a
  factory needs that scoped separately, and this skill cannot size it**
- **Food regulatory** — labelling, registration, good-manufacturing-practice evidence and mock-recall
  traceability. Only lot traceability and recall blocking appear, in file **11**
- **Excise and product-specific indirect tax** — file **17** covers income, value-added and
  competition law only
- **Adjacent systems** not examined: product lifecycle, partner platforms and franchise
  *(warehouse management is covered in file **11**; consolidation in file **15**)*

## Related files

- **00** the channel map and the classification method — start here
- **10** trade spend, the largest under-scoped area
- **16** the application estate and how to count integrations honestly
- **17** Thailand — the compliance questions to hand to the client's adviser
