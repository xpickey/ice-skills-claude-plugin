---
name: fmcg-practise
description: >-
  Multi-channel solution practice for FMCG, fashion, sportswear and consumable-product brands
  selling B2B2C on a NetSuite-centric estate. Use for pre-sales discovery, fit-gap, solution
  design, demo design, proposal and scoping. Covers the fifteen-channel customer-group model,
  traditional trade, modern trade with sale-in versus sale-out, consignment in both tax-point
  models, e-commerce storefront and marketplace, owned-store point of sale, project and export,
  made-to-order and transformation work, inventory location topology, costing and its
  per-location valuation trap, third-party warehouse, the ~25-touchpoint integration catalogue,
  procure-to-pay, budget control, ledger dimensions for channel profitability, retail-estate
  fixed assets, and seasonal demand planning. Triggers on FMCG solution, fashion ERP, apparel
  ERP, sportswear, consumer goods ERP, multi-channel sales, omni-channel inventory, consignment,
  sale-in sale-out, modern trade, EDI, marketplace integration, Shopee Lazada TikTok, POS
  integration, 3PL, B2B2C footprint, channel profitability, dead stock, inventory ageing,
  ขายหลายช่องทาง, ฝากขาย, โมเดิร์นเทรด, ขายออนไลน์, ระบบ POS, คลังสินค้า, ต้นทุนสินค้า,
  แปรสภาพสินค้า, fit-gap FMCG, วางโซลูชัน FMCG, เสื้อผ้ากีฬา ERP.
license: Proprietary
metadata:
  version: V01R01
  date: 2026.08.14
  changelog: >-
    V01R01 — pricing and promotion reframed on the user's direction: base price in the ERP with
    front-end discounting is a sound architecture, and the requirement is the promotion write-back
    onto the ERP sales line (amount, type, campaign code, funder) so channel and campaign margin
    analysis works. Marketplace settlement reconciliation upgraded from a caution to a designed
    three-way-match solution. New invariants 3b and 3c, two new patterns, two routing rows.
  origin: >-
    Distilled from a completed multi-channel NetSuite implementation for a Thai sportswear and
    apparel brand, plus the firm's FMCG application-landscape approach. All content is
    generalised — no customer name, figures, prices, rates or contract terms are carried.
    Referred to throughout as "the reference implementation".
  composes_with:
    - ice-netsuite-thailand-advisory
    - oracle-netsuite-consulting
    - b2b-solution-selling
    - ice-b2b-enterprise-sale
---

# FMCG / fashion multi-channel solution practice

## What this skill is for

A consumer-goods brand that manufactures or sources product and reaches shoppers through
retailers, its own shops and online **does not have one sales process with a few variations**. It
has a channel model, an inventory backbone that every channel draws on, and an application estate
where each channel keeps its own way of working while money and stock converge on one place.

This skill carries that practice: what the channels are, how each one actually runs, what the
back-office modules must do to support them, what the integration estate looks like, and — most
usefully in a sales conversation — **where these designs typically go wrong and what to ask before
quoting**.

## What it is not

- Not a NetSuite feature list. Product capability questions go to `oracle-netsuite-consulting`.
- Not Thai tax or localisation depth. That is `ice-netsuite-thailand-advisory`.
- Not deal strategy or proposal structure. That is `b2b-solution-selling` and `ice-b2b-enterprise-sale`.
- Not a customer reference. The origin implementation is never named in output; describe it as
  "a comparable multi-channel apparel brand" or "the reference implementation" and carry no figures
  from it.

## When to reach for it

Any of these in a prospect conversation:
- consumer goods, apparel, sportswear, footwear, cosmetics, food and beverage brands
- more than one route to the shopper
- the words consignment, ฝากขาย, modern trade, marketplace, or "our own shops"
- goods that get printed, embroidered, personalised or subcontracted
- a stock accuracy, dead-stock or channel-margin problem

---

## Routing — which file answers which question

| The question sounds like | Load |
|---|---|
| "What channels does a brand like this sell through?" · "How do they differ?" · ขายผ่านช่องทางไหนบ้าง | **01** channel landscape |
| Dealers, distributors, credit terms, project sales, sponsorship, export, deposits | **02** wholesale channels |
| Department stores, key accounts, EDI, sale-in vs sale-out, rebates, chargebacks, deductions | **03** modern trade |
| Consignment, ฝากขาย, sale-out recognition, stock at the retailer, reconciliation, event stock | **04** consignment |
| Website, Shopee/Lazada/TikTok, API gateway, cash on delivery, online returns, chat selling | **05** online |
| **Platform settlement reconciliation** · "did the platform pay us for everything we shipped" · fees, commission, subsidy · กระทบยอดกับเงินรับจาก platform | **05**, "Platform settlement reconciliation" section |
| **Pricing, discount and promotion write-back** · "where do promotions live" · channel and campaign margin analysis | **02**, "The architecture is fine. The write-back is the requirement." |
| Own shops, POS, daily revenue posting, store replenishment, store returns, staff sales | **06** owned store and POS |
| Warehouse structure, locations, 3PL, fulfilment, costing method, stock valuation, ageing, dead stock, overselling | **07** inventory, fulfilment, costing |
| Printing, embroidery, personalisation, subcontracting, made to order, item-code decisions, transformation cost | **08** make and transform |
| Purchasing, vendors, goods receipt, imports, landed cost, payables, treasury, budget control | **09** procure to pay and budget |
| General ledger, channel profitability, dimensions, period close, fixed assets, store assets, demand planning | **10** finance and planning |
| "Draw me the architecture" · which system owns what · how many integrations · middleware | **11** application footprint |
| **"Sketch the footprint for a prospect who sells through X, Y and Z"** · sizing the shape of a live opportunity | **11**, "Worked example" section — a full channel-enumeration-to-integration-count walkthrough |
| What goes wrong · challenges · gaps · improvement areas · discovery questions · what to ask before quoting | **12** practice, gaps and discovery |
| A term I do not recognise | `glossary.md` |
| A mechanism I want to reuse | `patterns.md` |
| I am in the meeting now and need the decision rules | `cheatsheet.md` |

---

## Cross-channel invariants — safe to answer without loading anything

These hold across the whole practice. Use them directly; load a reference file for depth.

**1. Three questions define a channel.** When must the tax invoice be issued · who actually owes
the money · after delivery, whose balance sheet carries the stock. Two customer groups that differ
on any one of those need separate treatment, however similar the commercial deal looks.

**2. Channel count is larger than anyone expects.** The reference implementation's tender assumed
roughly six channels; the finished design carried **fifteen customer-group channels**. Expect
expansion during design and say so at scoping time.

**3. Channel identity belongs in master data, not in the process.** One order-to-cash spine serves
every wholesale channel; the differences live in **payment terms** (cash inserts a human release
gate; credit relies on the automated credit and overdue check) and **sourcing model** (stocked, made
to order, transformed with or without an item-code change).

**3a. Two different things are both called "the channel" — keep them apart.** The **customer master**
carries the channel *classification*, which is what decides commercial and tax treatment for that
customer. The **ledger** needs one designated *reporting dimension* that owns channel, from which
every other dimension derives. In a clean design the ledger dimension is populated from the customer
master's classification through a single governed mapping table. **In the reference implementation
this rule was never written down**, and channel identity ended up living in three places at once —
see file **10**. That gap is the reason channel-profitability reporting could not be trusted.

**3b. The front end owns the discount decision; the ERP owns the discount record.** Holding only a
base price in the ERP while each channel decides its own promotion is a sound architecture and should
be defended. What is not optional is the **write-back**: every channel writes the realised pricing
onto the ERP sales line — gross price, discount amount and type, campaign code, net price, and **who
funded it**. A channel that cannot write back is a channel you cannot analyse. File **02** carries the
field set.

**3c. Marketplace settlement reconciliation is a designed solution, not a later report.** It is a
three-way match — ERP revenue against the platform's settlement report against the money received —
with deductions posted by type and brand-funded separated from platform-funded. Book a
platform-funded discount as brand cost and online margin is understated, which distorts every channel
investment decision that follows. File **05** carries the design.

**4. Consignment is two designs, not one.** True consignment (ฝากขายแท้) issues the tax invoice
**on sale-out**; pseudo consignment (ฝากขายเทียม) issues it **on delivery** and needs a shadow
book plus a custom synchronisation program. Never quote the second as configuration.

**5. Sale-in is the revenue event in outright modern trade; sale-out is the revenue event in
consignment.** Confusing them is the most common scoping error on a consumer-goods deal.

**6. Online is at least four sub-models** with four different debtors — consumer (prepaid website),
courier (cash on delivery), platform (marketplace), consumer again but manually verified (chat
commerce).

**7. Stock is relieved on the warehouse's confirmation; the invoice may only be raised from a
fulfilment in shipped status.** The physical event drives the accounting event, and nothing gets
billed that never left.

**8. Locations are grouped by function, not geography.** For every place a unit can be, ask *do I
own it* and *can I sell it this month*. That test produces eight groups: trading, transformation,
consignment-out, consignment-in, returns, work-in-process/in-transit, loaned, damaged. Bins within
a location separate by material status.

**9. Moving-average costing held at company level makes per-location stock valuation inaccurate.**
If the controller wants stock value per shop, that is a design decision with a reporting
consequence, not a configuration checkbox.

**10. The estate runs on roughly twenty-five integrations, not five** — and the register grows
during build as channels are discovered.

**11. The ERP owns money, stock and master data; the front ends own engagement and
channel-specific data entry.** The test for any contested capability: does it change a balance or
a stock position?

**12. Ageing and fast/slow/dead-stock reporting are in scope, not standard.** For a seasonal brand
this is where the margin goes.

---

## How to use this in a live pursuit

- **First meeting** — open `cheatsheet.md`, ask the three channel questions and two or three of the
  credibility questions at the end of it. Do not present; diagnose.
- **Fit-gap** — load the channel files in scope plus **07**. Each file's **"scoping signals"** section
  tells you **what must be priced as its own line item** and why. It deliberately gives **no effort
  figures**: this skill carries no verified man-day data, and inventing ranges would be worse than
  omitting them. Take the line items from here and the rates and durations from your own delivery
  estimating model. The relative-weight ranking in `cheatsheet.md` tells you which lines are the
  large ones.
- **Solution design** — load **11** for the architecture, then the relevant channel files, then
  `patterns.md` for the mechanisms to reuse.
- **Proposal or deck** — take the structure and the gaps from **12**, and route document production
  and language discipline to `ice-b2b-enterprise-sale`.

## Origin and how to speak about it

The practice is distilled from one completed implementation and the firm's FMCG approach material.
It is generalised on purpose: **mechanisms are described, never the customer's numbers, rates,
partners or terms.** In customer-facing output refer to "a comparable multi-channel apparel brand"
or "the reference implementation".

### What may and may not be named — the rule, applied

| Never name | Safe to name |
|---|---|
| the origin customer, in any form | **market-category names**: the regional marketplaces (Shopee, Lazada, TikTok), because every consumer brand in the region sells on them and naming them identifies nobody |
| its retailers and department-store partners | **product and stack names** (the ERP, the CRM), where the conversation is about the stack |
| its logistics provider, payment gateway, e-tax service provider or middleware vendor | generic role descriptions — "the 3PL provider", "the payment gateway", "a commercial multi-channel order platform" |
| any individual — project staff, approvers, contacts | job roles — merchandiser, cost accountant, supply-chain approver |
| its figures, rates, credit limits, fees or contract terms | the **mechanism** those figures sat inside |

The test: **would a knowledgeable reader be able to work out which company this was?** Naming a
marketplace that thousands of brands use fails that test harmlessly. Naming a retailer, a logistics
provider and a product category together does not.

Where this skill records something as a **gap** or an **open decision**, that is a factual record of
what the reference design left unresolved — useful as an honest improvement story, and not to be
presented as a shipped capability.
