---
name: fmcg-practise
description: >-
  Multi-channel solution practice for FMCG, fashion, sportswear, food and consumable-product brands
  selling B2B2C. Use for pre-sales discovery, fit-gap, solution design, demo design, proposal and
  scoping — and reach for it whenever a prospect sells the same product through more than one route
  to the shopper, even if they never say "multi-channel". Nine sales channels, each with its own use
  cases, process, function checklist, integrations and gaps: traditional trade, modern trade,
  consignment in both tax-point models, van sales, owned-store point of sale, e-commerce and
  marketplace, project and corporate, export, and event/employee groups. Plus trade spend and Net GP
  (trade agreements, rebate structures, listing fees, promotions and scanbacks, deduction intake,
  matching, disputes, accruals, gross-to-net), inventory location topology and costing, transformation
  and made-to-order, demand planning with promotion uplift and sell-through, procure-to-pay and budget
  control, ledger dimensions for channel profitability, the application footprint and its integration
  catalogue, Thai tax and trade-competition compliance, investment-promotion privileges, and a
  discovery and scoping bank. Triggers on FMCG solution, fashion ERP, apparel ERP, food and beverage
  ERP, consumer goods ERP, multi-channel sales, omni-channel, consignment, sale-in sale-out, modern
  trade, trade spend, rebate, listing fee, deduction, chargeback, Net GP, gross-to-net, EDI,
  marketplace integration, Shopee Lazada TikTok, POS integration, van sales, 3PL, FEFO, shelf life,
  dead stock, channel profitability, BOI, ขายหลายช่องทาง, ฝากขาย, โมเดิร์นเทรด, ขายออนไลน์, ขายบนรถ,
  ระบบ POS, คลังสินค้า, ต้นทุนสินค้า, แปรสภาพสินค้า, ส่วนลดการค้า, ค่าแรกเข้า, กระทบยอด, fit-gap FMCG,
  วางโซลูชัน FMCG.
license: Proprietary
metadata:
  version: V02R07
  date: 2026.08.14
  origin: >-
    Distilled from two completed implementations — an apparel and sportswear brand, and a food and
    beverage manufacturer, both selling through Thai organised retail and direct channels — plus
    research against primary tax, competition-law and accounting sources. All content is generalised:
    no customer name, figures, prices, rates or contract terms are carried. Referred to throughout as
    "the reference implementations".
  changelog: >-
    V02R07 — file 06 gains the three-integration-class table (full marketplace /
    platform-storefront-seller-collects / chat commerce): TikTok Shop reconciles like
    Shopee plus creator-affiliate commission into trade spend; LINE SHOPPING uses the
    order API without escrow design; Facebook-Instagram Thailand is chat commerce
    needing the manual-verify sub-model and an order-capture decision. Five platforms
    equal two connector designs plus one capture decision.
    V02R06 — file 06 gains verified API mechanics: Shopee escrow formula and
    pull-after-completion rule, Lazada finance endpoints and token-refresh design,
    and the five recurring spreadsheet-import transforms (VAT extraction, pack-SKU
    explosion, per-platform one-time customer, line-level dedupe key, tax-invoice
    request fields). Distilled from a live pursuit; generalised.
    V02R00 — full restructure. Reorganised into nine channel files sharing one fixed six-part template
    (use cases, process, function checklist, integrations, gaps, discovery questions) plus capability,
    context and discovery layers. Second reference case added, bringing trade spend, demand planning,
    van sales, shelf-life control and investment promotion. Trade spend rebuilt against published
    practice: three-value mechanic, two-axis scope, estimation method, unconditional-fee family. Thai
    layer rebuilt against primary sources including the trade-competition guideline on retailer charges.
    V02R01 — cold-reader audit fixes: patterns.md taught a superseded rebate model (four attributes,
    one scope axis, two mechanics) and now matches file 10; file 19 no longer disclaims warehouse
    management and consolidation, which files 11 and 15 cover; five cross-references corrected,
    including investment-promotion questions routed to 18 rather than 17, which disclaims them; files
    11 and 14 now carry the duty-exempt content 18 pointed at; the sale-out two-senses trap is
    reachable from the routing table; the delivery-penalty invariant separates the reporting judgement
    from the unsettled tax classification; and the skill now states plainly that it cannot scope a
    factory.
    V02R02 — delta-audit fixes: three Related-files pointers broken by the previous round's insertion
    script were repaired and re-ordered (a scripted edit that passed its own assertion but produced
    unreadable output — the lesson being that an edit must be read, not only asserted); file 18 gained
    the procurement row and back-link the changelog had claimed; the delivery-penalty hedge propagated
    to patterns and cheatsheet; a mechanic value mislabelled as an attribute corrected; file 19's
    demand-planning disclaimer narrowed to what is genuinely absent; and files 11 and 14 gained the
    discovery questions that make their new duty-exempt content reachable.
    V02R03 — third audit round: five files pointed at file 17 for topics it does not contain (export
    tax, VAT on deposits, tax depreciation) and one pointed at file 11 for landed cost, which is file
    14. All now name the gap honestly rather than mis-routing the reader, following the pattern file
    09 already used. The two duty-exempt trigger questions moved into the numbered discovery lists
    where the workflow actually reaches them.
    V02R04 — final sweep: the cheatsheet still carried a superseded EDI block asserting "purchase
    order and little else" alongside the corrected three-architecture block, and gained the
    versioned-agreement decision rule where dispute defence and Thai competition compliance meet.
    V02R05 — electronic tax invoicing restated on the user's correction. The previous wording was
    right in law and misleading in practice: it is elective, but business-to-business counterparties
    pull a supplier in and the state offers tax relief for adopting, so "you can defer it" is as wrong
    as "the law compels you". New invariant 13a, a cheatsheet decision block, a corrected glossary
    entry, and the adviser question reframed from the obligation to the incentive and its expiry.
  composes_with:
    - ice-netsuite-thailand-advisory
    - oracle-netsuite-consulting
    - b2b-solution-selling
    - ice-b2b-enterprise-sale
---

# FMCG / multi-channel consumer goods — solution practice

## What this is for

A brand that makes or sources consumer goods and reaches shoppers through retailers, its own shops,
vehicles and online **does not have one sales process with a few variations**. It has a channel model,
an inventory backbone every channel draws on, a layer of money the retailers take back, and an
application estate where each channel keeps its own way of working while stock and money converge on
one place.

This skill carries that practice — **what the channels are, how each runs, what functions the system
must provide, what connects to what, and where these designs typically go wrong**.

## What it is not

- **Not a product feature list.** Capability questions for a specific product go to that product's skill.
- **Not tax or legal advice.** File **17** gives you the questions; the client's adviser gives the
  answers. Never quote a rate or a rule from here into a client document.
- **Not a manufacturing scope.** File **12** covers transformation and made-to-order work that hangs
  off a sales order. It does **not** cover a factory — multi-level bills of material, routings and
  work centres, capacity and material requirements planning, shop-floor scheduling or production
  variance. **A prospect that runs its own factory needs that scoped separately, and this skill
  cannot size it.** Say so rather than letting the channel coverage imply the rest.
- **Not deal strategy.** That is `b2b-solution-selling` and `ice-b2b-enterprise-sale`.
- **Not a customer reference.** The origin implementations are never named. Describe them as
  "a comparable multi-channel brand" and carry no figures from them.

## Reach for it when

Consumer goods, apparel, footwear, cosmetics, food or beverage · more than one route to the shopper ·
the words consignment, ฝากขาย, modern trade, marketplace, van sales, "our own shops" · goods that get
printed, embroidered, personalised or subcontracted · goods with a shelf life · a stock-accuracy,
dead-stock, deduction or channel-margin problem.

---

## How the files are organised

Every **channel file** uses the same six sections, so you can jump to what you need without reading
prose: **1 use cases · 2 process · 3 function checklist · 4 integration touchpoints · 5 challenges and
gaps · 6 discovery questions.** Section 3 is written to be lifted straight into a fit-gap document.

| Group | Files |
|---|---|
| **Map** | **00** how to classify any customer group |
| **Channels** | **01** traditional trade · **02** modern trade · **03** consignment · **04** van sales · **05** owned store and POS · **06** online and marketplace · **07** project and corporate · **08** export · **09** event, employee and other |
| **Capabilities** | **10** trade spend and Net GP · **11** inventory and costing · **12** make and transform · **13** demand planning · **14** procure to pay and budget · **15** finance, ledger and assets · **16** application footprint |
| **Context** | **17** Thailand compliance · **18** BOI and incentives · **19** discovery and scoping |
| **Layers** | `glossary.md` terms · `patterns.md` reusable mechanisms · `cheatsheet.md` decision rules for a live meeting |

---

## Routing

| The question sounds like | Load |
|---|---|
| "What channels does a brand like this sell through?" · "How do I tell which one this is?" · ขายผ่านช่องทางไหนบ้าง | **00** |
| **"Do you handle sale-out?"** · sale-out vs sell-through · "is that revenue or is that demand" | **00**, the two-senses table — **ask back which sense they mean before answering** |
| Dealers, distributors, wholesale credit terms, deposits | **01** |
| Department stores, hypermarkets, key accounts, sale-in vs sale-out, "is it outright or consignment" | **02** |
| EDI · "the client says they already have EDI" · portal vs bureau vs direct | **02**, EDI section |
| ฝากขาย, consignment, counters, sale-out recognition, stock at the retailer, reconciliation | **03** |
| Van sales, รถเร่, route selling, load and settle, cash on the vehicle | **04** |
| Own shops, POS, daily revenue posting, store replenishment, staff sales | **05** |
| Website, Shopee/Lazada/TikTok, API gateway, cash on delivery, online returns, chat selling | **06** |
| Platform settlement · "did the platform pay us for everything we shipped" · fees and subsidies | **06**, settlement section |
| Corporate, government, project, VIP, sponsorship contracts | **07** |
| Export, incoterms, landed cost, foreign currency | **08** |
| Events, pop-ups, employee purchase, giveaways, service revenue | **09** |
| **Listing fee, rebate, promotion, scanback, deduction, chargeback, dispute, accrual, Net GP, gross-to-net** · "which retailer is actually profitable" | **10** |
| Trade agreement structure, rebate tiers, retroactive vs prospective, hierarchy cascade | **10**, stage 2 |
| Warehouse structure, locations, 3PL, costing method, stock valuation, FEFO, shelf life, ageing, dead stock, overselling | **11** |
| Printing, embroidery, personalisation, subcontracting, made to order, item-code decisions | **12** |
| Forecasting, promotion uplift, cannibalisation, sell-through, safety stock, forecast accuracy | **13** |
| Purchasing, vendors, goods receipt, imports, payables, budget control | **14** |
| General ledger, channel profitability, dimensions, period close, fixed assets | **15** |
| "Draw me the architecture" · which system owns what · how many integrations · middleware | **16** |
| **Sketch the footprint for a prospect who sells through X, Y and Z** · sizing a live opportunity | **16**, worked example |
| Thai e-Tax Invoice · "do we have to move to e-Tax?" · VAT on rebates, withholding on retailer fees, **what a retailer may lawfully charge**, platform reporting, Thai QR | **17** |
| BOI, investment promotion, promoted vs non-promoted, imported raw-material control | **18** |
| Discovery agenda, what delays these programmes, migration, cutover, phasing | **19** |
| A term I do not recognise | `glossary.md` |
| A mechanism I want to reuse | `patterns.md` |
| I am in the meeting now and need the decision rules | `cheatsheet.md` |

---

## Cross-channel invariants — answer directly, load a file for depth

**1. Three questions classify any customer group.** When must the tax invoice be issued · who actually
owes the money · after delivery, whose balance sheet carries unsold stock. Two groups differing on any
one need separate treatment. **Ask per category or counter, not per account.**

**2. Channel count always exceeds the estimate.** One reference tender assumed roughly six channels;
the finished design carried fifteen. Say so at scoping rather than discovering it in build.

**3. Modern trade is a channel, not a commercial model.** The same retailer account can carry outright
sale, true consignment and pseudo consignment at once.

**4. Consignment is two designs.** True consignment invoices **on sale-out**; pseudo consignment
invoices **on delivery** and needs a shadow book plus a synchronisation program. Never quote the second
as configuration.

**5. "Sale-out" means two different things.** In accounting it is a revenue-recognition event; in
planning it is a demand signal. When a client asks "do you handle sale-out?", ask back: *for revenue
recognition, or for forecasting?* — different designs, different scope.

**6. Stock is relieved on confirmation, not on instruction.** The ERP issues the release; stock is
relieved and cost posted when the movement is confirmed — by the warehouse, the van settlement, or the
daily store posting.

**7. Invoice only from a fulfilment in shipped status.** One rule that stops every channel billing
goods that never left.

**8. Channel identity has two homes and they must not be confused.** The **customer master** carries
the channel *classification*, which drives commercial and tax treatment. The **ledger** needs one
designated *reporting dimension* that owns channel, derived from it through a single governed mapping.
Leave this unwritten and channel identity ends up in three places, as it did in one reference case —
which is why per-channel margin could not be trusted.

**9. The front end owns the discount decision; the ERP owns the discount record.** Holding only a base
price in the ERP while each channel decides its own promotion is sound architecture. What is not
optional is the **write-back**: gross price, discount amount and type, campaign code, net price and
**who funded it**. A channel that cannot write back is a channel you cannot analyse.

**10. Trade spend is the largest under-scoped area of any retail deal.** Retailers **deduct first and
explain later, or never** — money arrives via remittance advice, retailer portal and bank statement,
with no single place to collect it. Twenty functions, not a report. File **10**.

**11. Gross margin does not answer the board's question.** A brand can win the listing, hit the volume
target and still lose money on that retailer. Report a contribution-margin waterfall, show margin
percentage **beside** trade-spend ratio, and keep delivery-performance penalties **out** of the trade
bucket. That placement is a **management-reporting judgement** — sound, and to be settled with the
accounting-policy owner before build. Their **tax and accounting classification is a separate
question that two research rounds could not settle** (file **17**). Do not present the two as one.

**12. Marketplace settlement is a designed three-way match** — ERP revenue against the platform's
settlement report against the money received — with deductions posted by type and **brand-funded
separated from platform-funded**. Book a platform-funded discount as brand cost and online margin is
understated.

**13. One promotion master, consumed twice.** The promotion that drives a trade-spend accrual is the
same one that drives a forecast uplift. Two records means the sell-through settling the scanback
differs from the one forecasting demand, and both become unreliable.

**13a. Thai electronic tax invoicing is elective in law and close to unavoidable in practice.** Never
tell a client it is compulsory — they can check. Never tell them it can wait either: counterparties
pull them in and the state offers relief for adopting. **Design the document layer so that adoption
is a switch, not a rebuild.** File **17**.

**14. Where the gaps cluster, every time:** statutory document and tax formats · channel-specific
data-entry ergonomics · mechanics where accounting and physical reality diverge. Price those as custom
regardless of the datasheet; expect a fit elsewhere.

**15. Costing grain is a decision, not a default.** Moving-average valuation held at entity level makes
**per-site inventory valuation reporting wrong** while entity-level reporting stays right. If the
controller wants stock value per shop, that is a design decision with a reporting consequence.

---

## Using this in a live pursuit

**Discovery:** open with the three questions in invariant 1, asked per category. Then take the
operating-model test in **19**. Each channel file's section 6 gives you the rest, with ⚑ marking the
questions that move the estimate.

**Fit-gap:** section 3 of each channel file is a function checklist written to be lifted directly.

**Sizing:** the scoping and gap sections tell you **what to price as its own line item** — not how
much. This skill carries **no verified effort data**; rates come from your own delivery estimating
model. `cheatsheet.md` ranks the heavy areas by design complexity and custom content.

**Architecture:** **16** has a five-step worked example from channel enumeration to an integration
count.

**Thailand:** **17** gives you questions to hand to the client's adviser. Listing them in a proposal is
itself a credibility signal — most competitors assume instead.

---

## What may be named in output

The test: **could a knowledgeable reader work out which company this was?**

| Never name | Safe to name |
|---|---|
| The origin customers, in any form | Product and stack names (the ERP, the CRM) |
| Any specific retailer or retail group | Regional marketplaces as market categories |
| The logistics provider, payment gateway, e-tax provider, EDI provider or middleware vendor | Generic descriptors — "a national modern-trade retailer", "the 3PL provider" |
| Any individual | Standard industry terms |

**Never carry into client output:** money figures, rates, percentages, thresholds or benchmark
statistics from this skill. Every number in both source implementations is marked illustrative by its
own authors, and published trade-spend ranges disagree with each other because the definitions differ.
When a client asks for benchmarks, offer to show them their own numbers instead.

## Composition

Thai tax and localisation depth → `ice-netsuite-thailand-advisory` · product capability →
`oracle-netsuite-consulting` · deal strategy and proposal structure → `b2b-solution-selling` and
`ice-b2b-enterprise-sale` · document production → `ice-doc-builder`.
