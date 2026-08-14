# 01 — Channel Landscape: how a consumer-goods brand actually sells

> Load this when the question is "what channels exist / how do they differ / where do I start".
> Per-channel depth lives in files 02-06. This file is the map and the comparison.

## Why channel count is the first thing to get right

A brand that manufactures consumer goods and reaches shoppers both through retailers and
directly does **not** have one sales process with a few variations. In the reference
implementation — a Thai sportswear and apparel brand selling wholesale, retail, online and
export — the finance and sales teams landed on **fifteen distinct customer-group channels**
after a full design cycle. The initial tender document had assumed roughly six.

That expansion is the most transferable lesson in this skill. Channels multiplied not because
anyone wanted complexity, but because three things differ per customer group and each one
forces a separate configuration:

1. **The tax point** — when the tax invoice must legally be issued (on delivery, on sale-out, on receipt of payment).
2. **The debtor** — who actually owes the money (the shop, the retailer's head office, the courier, the marketplace platform, the consumer).
3. **Stock ownership** — whether goods sitting at the counterparty are still on the brand's balance sheet.

Two customer groups that look commercially identical will still need separate treatment if any
one of those three differs. Ask about all three in discovery.

## The fifteen-channel reference model

| # | Channel | Thai term | Order origin | Debtor | Stock at counterparty owned by brand? |
|---|---|---|---|---|---|
| 1 | Traditional Trade — outright | ขายขาดผ่านร้านค้า | CRM / sales rep | the dealer | no |
| 2 | Modern Trade — outright | ขายขาดห้างสรรพสินค้า | CRM, portal, or file import | retailer head office | no |
| 3 | Project VIP | โครงการลูกค้า VIP | CRM opportunity | the project customer | no |
| 4 | Sponsorship / club rights | กลุ่มสัญญาสิทธิประโยชน์ (สโมสร) | contract-driven | the club or sponsor | no |
| 5 | Consignment | กลุ่มลูกค้าฝากขาย | transfer, then sale-out feed | the retailer, on sale-out | **yes** (until sold) |
| 6 | Owned store | ร้านของแบรนด์เอง | point of sale | the consumer | yes (own site) |
| 7 | Online | กลุ่มลูกค้า Online | storefront, marketplace, chat | varies — see file 05 | yes (own or 3PL site) |
| 8 | Corporate & government project | ลูกค้าองค์กรภาครัฐและเอกชน | CRM opportunity, tender | the organisation | no |
| 9 | Export / international | กลุ่มลูกค้าต่างประเทศ (Inter Sale) | CRM, export desk | the overseas buyer | no |
| 10 | Retail event / pop-up | กลุ่มลูกค้าขายปลีกและอีเว้นท์ | event stock transfer + sale-out | varies by model | **yes** (event stock) |
| 11 | Employee sales | กลุ่มพนักงาน | point of sale | the employee | yes |
| 12 | Complimentary / giveaway | กลุ่มลูกค้าอภินันทนาการ | internal request | none — no revenue | n/a |
| 13 | Other sales | กลุ่มขายอื่นๆ | manual | varies | varies |
| 14 | Adjacent product line | e.g. health products & services | varies | varies | varies |
| 15 | Service revenue | กลุ่มงานบริการ | manual / contract | the customer | n/a — non-inventory |

Not every prospect needs all fifteen. The point is the **method**: enumerate customer groups by
tax point, debtor and stock ownership rather than by sales-team org chart.

## The product-type dimension — cuts across channels

Every wholesale-type channel in the reference model repeats the same matrix:

**Four sourcing models × two payment terms = eight process variants per channel.**

| Sourcing model | Thai | What happens |
|---|---|---|
| Stocked collection product | สินค้าใน Collection | sold from existing inventory |
| Made to order | สั่งผลิต | order triggers a purchase requisition or production order; goods received then shipped |
| Transformation, item code changes | แปรสภาพ – เปลี่ยน Item# | a blank is decorated (printed, embroidered, personalised) and becomes a **different sellable SKU** |
| Transformation, item code unchanged | แปรสภาพ – ไม่เปลี่ยน Item# | value is added but the SKU stays the same |

× **cash sale (ขายสด)** and **credit sale (เครดิต)**.

**Why the transformation dimension matters.** This is the axis that separates apparel, sportswear,
promotional goods and personalised consumer products from generic fast-moving goods. The same
physical blank garment becomes a club kit, a corporate uniform or a named jersey depending on
what is printed on it. The design question — does decoration create a new item code or stay on
the original — decides how costing, stock visibility and demand planning all behave. Any prospect
doing team kit, corporate uniform, licensing or personalisation hits this on day one.

**What the payment term actually changes.** Cash sale inserts a human release gate: the order
opens in a pending status, the sales team uploads proof of payment, finance verifies it and only
then approves release to the warehouse. Credit sale relies on the automated credit-limit and
overdue-invoice check instead, and the order opens approved. The steps differ; the documents do
not.

## What is genuinely shared across all channels

Despite fifteen channels, one order-to-cash spine serves them all:

```
credit + stock check → sales order + reservation → release to warehouse
  → fulfilment → stock relieved → invoice → billing → receipt
```

Three shared controls are worth naming in any solution design:

- **Invoice may only be raised from a fulfilment in shipped status.** This single rule stops
  every channel from billing goods that never left the building.
- **Stock is relieved at fulfilment, not at invoice.** Cost of goods sold posts with the physical
  movement; revenue posts with the document. Keeping them separate is what makes cross-channel
  margin reporting possible.
- **Channel identity lives on the customer master, not in the process.** In the reference model
  the channel code sits in a customer-master segment and **drives the tax-point and commercial
  treatment for that customer; the ledger's channel reporting dimension is then derived from it.**
  Those are two separate things and must not be maintained twice — file **10** carries the rule and
  what went wrong when it was left unwritten. Writing a separate process per channel would have
  produced a dozen near-identical designs.

## Comparison at a glance — where revenue and stock actually move

**Read the middle column carefully.** In every channel that ships from a warehouse, stock is
relieved and cost of sales posted **when the warehouse confirms fulfilment** — never when the ERP
issues the release instruction. The column below names the *business event* that triggers that
chain, not a different accounting rule. Two rows are annotated because they do not follow the plain
pattern: the **owned store**, where no warehouse confirmation exists because the goods are already in
the shop, and **true consignment**, where the delivery does go through warehouse fulfilment but stock
relief happens later, at the sale-out feed.

| Channel | What triggers stock relief | Tax invoice issued when | Reconciliation burden |
|---|---|---|---|
| Traditional Trade | order released → warehouse confirms fulfilment | on invoice after shipment | low — order-to-invoice matching |
| Modern Trade outright | order released → warehouse confirms fulfilment | on invoice, net of any deposit | medium — deductions and chargebacks |
| Consignment "true" | **the sale-out feed**, not the delivery — the delivery only moved the goods to a consignment location the brand still owns | **on sale-out** | **high** — periodic stock count vs sale-out feed |
| Consignment "pseudo" | delivery — warehouse confirms fulfilment, and a shadow-book receipt is booked for the same quantity | **at delivery** | **high** — shadow book must be kept in step |
| Owned store | **the daily revenue summary posting** (no warehouse confirmation exists — the goods are already in the shop) | on request, else aggregated daily | medium — cash and payment-type reconciliation |
| Website prepaid | payment verified → release → warehouse confirms fulfilment | on request | low |
| Website cash on delivery | order released immediately → warehouse confirms fulfilment | on invoice; collected from the courier | medium — courier settlement |
| Marketplace | order released → warehouse confirms fulfilment | on the platform's delivery confirmation | **high** — platform settlement and fee matching |
| Export | order released → warehouse confirms fulfilment | per shipping documents | medium — currency and documentation |
| Retail event | depends on model — same true/pseudo split as consignment | same split | high while the event runs |

## Discovery questions this file supports

1. Which customer groups do you sell to, and for each — who pays you, and when must the tax invoice be issued?
2. Is any stock sitting at someone else's site that you still own? How do you count it, and how often?
3. Do you customise or decorate goods to order? Does that create a new item code in your current system?
4. Which channels sell the same SKU, and how do you stop two channels selling the same unit?
5. When a customer returns goods, does the stock always come back, or do you sometimes issue credit with no return?

## Related files

- **02** dealer, project and export channels — the wholesale spine
- **03** modern trade — sale-in versus sale-out, trade terms, deductions
- **04** consignment — the two tax-point models and their reconciliation
- **05** online — website, marketplace and chat commerce
- **06** owned store and point of sale
- **07** the inventory backbone all channels share
- **12** what typically goes wrong, and what to ask before quoting
