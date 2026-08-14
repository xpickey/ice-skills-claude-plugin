# 00 — Channel Map: how to classify what you are looking at

> **Load this first**, before any individual channel file, whenever you are working out what a
> prospect actually has. Every other channel file assumes you have already classified correctly.
> **Source basis:** two completed implementations — an apparel and sportswear brand, and a food and
> beverage manufacturer — both selling through Thai organised retail and direct channels.

## The classification method

Do not classify a prospect's business by what their sales team calls things. Sales teams name
channels after **where the goods go**; systems have to be built around **how the money and the stock
behave**. Those are different, and the gap between them is where scoping errors live.

Three questions classify any customer group. Ask all three, every time:

| # | Question | Why it decides the design |
|---|---|---|
| **1** | **When must the tax invoice be issued?** — on delivery, on sale to the end shopper, or on receipt of payment | sets the revenue and tax point, which is the hardest thing to change later |
| **2** | **Who actually owes you the money?** — the shop, the retailer's head office, the courier, the platform, the consumer, the employer | determines the receivable sub-ledger and the reconciliation problem |
| **3** | **After delivery, whose balance sheet carries unsold stock?** | determines whether you need a consignment location, a shadow book, or neither |

**Two customer groups that differ on any one of these need separate treatment**, however similar the
commercial relationship looks. Two that agree on all three can usually share a design even if the
sales team insists they are different.

### The question to ask *per category, not per account*

A single retailer group commonly buys some categories outright, takes others on consignment, and
runs a department-store counter on a third arrangement. **Classify at the level where the answers
actually change** — which is usually the category, the counter or the agreement line, not the
customer record.

## Why channel count always exceeds the estimate

The apparel implementation's tender assumed roughly six channels. The finished design carried
**fifteen customer-group channels**. That expansion was not scope creep — it was finance
discovering, group by group, that the three questions above had different answers.

Say this at scoping time. A proposal built on the channel count in the tender document will be
wrong, and it is better to be the vendor who predicted that than the one who discovers it in build.

## The channel set

Nine channel files, each with its own use cases, process, functions, integrations and gaps.

| File | Channel | Thai | Defining characteristic |
|---|---|---|---|
| **01** | Traditional trade | ขายขาดผ่านร้านค้า | outright sale to dealers and independent shops |
| **02** | Modern trade | โมเดิร์นเทรด | organised retail — carries **three commercial models at once** |
| **03** | Consignment | ฝากขาย | brand owns the stock until it sells; **two tax-point models** |
| **04** | Van sales | ขายบนรถ / รถเร่ | stock and cash travel on the vehicle; settled daily |
| **05** | Owned store and point of sale | ร้านของแบรนด์เอง | brand's own retail; posted by the day, not the transaction |
| **06** | Online and marketplace | ออนไลน์ | at least four sub-models with different debtors |
| **07** | Project and corporate | ลูกค้าองค์กร / โครงการ | opportunity-driven, often made to order |
| **08** | Export | ส่งออก | currency, documentation, landed cost |
| **09** | Event, employee, complimentary and other | อีเว้นท์ · พนักงาน · อภินันทนาการ | short-lived or non-commercial groups that still need a home |

Cross-channel capabilities — trade spend, inventory, planning, the application estate — are **not**
repeated inside channel files. They live in files 10 to 16.

## Comparison at a glance

Read this as *where the accounting events happen*, not as a summary of the process.

| Channel | Tax invoice issued | Debtor | Unsold stock owned by | Stock relief triggered by |
|---|---|---|---|---|
| Traditional trade | on shipment | the dealer | the dealer | warehouse fulfilment confirmation |
| Modern trade — outright | on shipment, net of deposit | retailer head office | the retailer | warehouse fulfilment confirmation |
| Modern trade — true consignment | **on sale-out** | the retailer | **the brand** | the sale-out feed |
| Modern trade — pseudo consignment | **on delivery** | the retailer | the brand, commercially | fulfilment; the shadow book relieves at sale-out |
| Van sales | at the point of sale on the vehicle | the shop, or cash | the brand, while on the van | the van settlement |
| Owned store | on request, else aggregated daily | the consumer | the brand | the daily revenue posting |
| Online — prepaid | on request | the consumer | the brand | release after payment verified |
| Online — cash on delivery | on invoice | **the courier**, in transit | the brand | release |
| Online — marketplace | on delivery confirmation | **the platform** | the brand | release |
| Project and corporate | on shipment · **milestone billing occurs in the market but was not present in either reference implementation — see 07** | the organisation | the customer | fulfilment |
| Export | per shipping documents | the overseas buyer | the buyer, per incoterm | fulfilment |
| Event | follows the true or pseudo split | varies | the brand | sale-out or settlement |

**Stock relief is one rule everywhere:** the ERP issues a release instruction, but stock is relieved
and cost of sales posted **when the movement is confirmed** — by the warehouse, by the van
settlement, or by the daily store posting. Two rows do not follow the plain warehouse pattern and
are marked above: owned store (goods are already in the shop) and true consignment (delivery is
confirmed normally, but relief waits for the sale-out feed).

## The dimension that cuts across every wholesale channel

Traditional trade, project, corporate and export all repeat the same matrix — **four sourcing models
× two payment terms**:

| Sourcing model | Thai | What happens |
|---|---|---|
| Stocked collection product | สินค้าใน Collection | sold from existing inventory |
| Made to order | สั่งผลิต | the order triggers a purchase requisition or production order |
| Transformation, item code changes | แปรสภาพ – เปลี่ยน Item# | decoration creates a **different sellable item** |
| Transformation, item code unchanged | แปรสภาพ – ไม่เปลี่ยน Item# | value added, same item |

× **cash sale (ขายสด)** and **credit sale (เครดิต)**.

**What the payment term changes:** cash inserts a human release gate — the order opens pending, the
sales team uploads proof of payment, finance verifies and only then releases to the warehouse.
Credit relies on the automated credit-limit and overdue check instead, and the order opens approved.
Same documents, different control.

**What transformation changes** is more fundamental, and it is what separates apparel, promotional
goods, uniforms and personalised consumer products from generic fast-moving goods. The same blank
becomes a different sellable thing depending on what is printed on it. Whether that creates a new
item code decides how costing, stock visibility and planning all behave. Full treatment in file
**12**.

## One term that means two different things — read this before using it

**"Sale-out" (ยอดขายออก) is used in two distinct senses in this practice, and conflating them
produces wrong answers.**

| Sense | Meaning | Where it matters | File |
|---|---|---|---|
| **Accounting sense** | the event at which revenue is recognised | consignment — sale-out **is** the revenue event; in outright modern trade it is not | 02, 03 |
| **Demand-signal sense** | what the shopper actually bought, as distinct from what the retailer ordered | planning — sell-in is the order signal, sell-through is the true consumption signal | 13 |

The same data feed often serves both purposes. **Say which sense you mean.** When a client asks "do
you handle sale-out?", the useful reply is a question: *"for revenue recognition, or for
forecasting?"* — because the answer determines whether this is an accounting design problem or a
planning data problem, and they are scoped very differently.

## Related files

- **10** trade spend and Net GP — what the retailer takes back, across all retail channels
- **11** inventory, locations and costing — the backbone every channel draws on
- **16** the application estate and its integration catalogue
- **19** discovery question bank and what typically goes wrong
