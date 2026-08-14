# Glossary — FMCG / fashion multi-channel terms

Thai term in brackets where the Thai is what you will actually hear in a Bangkok meeting room.
Reference file numbers point to where the term is explained in context.

**Allocation** — setting aside stock for a specific channel or order so another channel cannot take it. Alternative to a single live pool. (07)

**API gateway** — a brand-owned service sitting between marketplaces and the ERP so the ERP integrates once instead of once per platform. (05, 11)

**Assembly item** — a master record for a product built from components, used where transformation produces a distinct sellable item. (08)

**Back margin** — see *rebate*. (03)

**Base price** — the list price held in the ERP before channel discounts. In the reference implementation the ERP holds only this; discounting happens in front-end systems. (02)

**Bill of materials** — the component list behind an assembled or transformed item. (08)

**Bin** — a subdivision of a location. In this practice bins separate stock **by material status** (good, damaged, customer claim) inside one location. (07)

**Cash on delivery** — the courier collects payment on handover and remits to the brand. Makes the **courier** the debtor, not the consumer. (05)

**Chargeback / deduction** — a retailer paying less than the invoice for short delivery, damage, lateness or a compliance penalty. (03)

**Collection product (สินค้าใน Collection)** — a finished stocked item sold from inventory, as opposed to made to order or transformed. (01, 02)

**Complimentary (อภินันทนาการ)** — goods given away. Stock and expense move; no revenue. Its own customer group in the reference model. (01)

**Consignment (ฝากขาย)** — goods placed with a counterparty who sells them; ownership stays with the brand until sale. Two tax-point models — see *true* and *pseudo consignment*. (04)

**Consignment-in (รับฝากขาย)** — goods the brand holds and sells on someone else's behalf. The mirror of consignment-out; needs its own location group. (04, 07)

**Cost of inaction** — the section of a proposal quantifying what standing still costs. The only place loss-framed language is permitted.

**Credit note (ใบลดหนี้) / credit memo** — a document reducing a receivable. Two kinds: **with goods return**, and **credit note only** for price or allowance corrections with no goods movement. (03, 05)

**Dead stock** — inventory with no movement over a defined period. Reported alongside fast- and slow-moving classification; custom in the reference implementation. (07)

**Deposit (เงินมัดจำ)** — advance payment. Receipted separately, carries VAT and its own tax invoice, and must be netted off the final invoice. (02, 03)

**Distribution-centre allowance** — a retailer charge for its own logistics, usually settled as a deduction. (03)

**Electronic data interchange** — structured document exchange with a retailer. In the Thai market it is commercially available through service-bureau Web EDI covering the major chains and six document types; coverage is **per retailer and per document**, not one yes or no. Do not assume purchase-order-only. (03)

**Fast/slow-moving report** — SKU movement classification driving markdown and buying decisions. (07)

**Fulfilment (Order Fulfilment)** — the warehouse instruction and its confirmation. Serves both sales orders and transfer orders. **Stock is relieved on the warehouse's confirmation.** (07)

**Goods return** — the physical return path, distinct from a credit-note-only adjustment. (03, 05)

**In-transit location (คลังระหว่างทาง / ระหว่างทำ)** — where stock sits between despatch and receipt on an inter-site transfer, so it is never invisible and never double-counted. (06, 07)

**Inventory adjustment** — increase or decrease of stock outside a purchase or sale. Used in this practice for point-of-sale corrections, consignment relief, and transformation cost setting. (07, 08)

**Inventory ageing report** — stock by age band. Where seasonal margin is protected or lost. (07)

**Landed cost** — the full delivered cost including freight, insurance, duty and handling. Assembled on an export cost sheet before quoting. (02)

**Listing fee / entry fee** — paid to a retailer to have a SKU carried. (03)

**Loaned goods (คลังยืมสินค้า)** — samples, sponsorship stock and event loans. Owned, not sellable, and needing its own location group. (07)

**Made to order (สั่งผลิต)** — produced or purchased against a specific customer order rather than sold from stock. (01, 02, 08)

**Marketplace** — a third-party selling platform. Makes the **platform** the debtor and introduces net settlement. (05)

**Merchandiser / product consultant** — the brand's staff member working on a retailer's floor, who records sale-out and scans consignment receipts. (03, 04)

**Modern trade (ห้างสรรพสินค้า / โมเดิร์นเทรด)** — organised retail: department stores, specialty chains, convenience chains. In this practice, **outright sale**. (03)

**Moving average costing** — inventory valued at a rolling average cost. The reference implementation's method, with an open decision on whether the average is held per subsidiary or per location. (07)

**Other charge for purchasing** — an orderable non-inventory charge line, used for the transformation service fee. (08)

**Outside processing (แปรสภาพ / งาน Outside)** — subcontracted transformation: blanks go to a supplier, come back decorated. Has its own location, master data and cost event. (08)

**Overselling** — the same physical unit sold twice across channels. Managed by live availability or by allocation. (05, 07)

**Platform-funded versus brand-funded discount** — who paid for a promotion. A platform-funded discount is not a cost to the brand; netting the two together understates online margin. Must be distinguishable on the ERP transaction line. (02, 05)

**Promotion write-back** — the realised discount and campaign data returned from the channel front end onto the ERP sales line, so margin can be analysed by channel and campaign. The front end owns the decision; the ERP owns the record. (02)

**Pseudo consignment (ฝากขายเทียม)** — consignment where the **tax invoice is issued on delivery**. Stock is relieved and revenue booked at delivery; a **shadow book** holds the position still at the retailer. Requires custom synchronisation. (04)

**Rebate / back margin** — volume- or period-based retailer compensation, usually settled by credit note at period end. (03)

**Reservation (การจองสินค้า)** — holding stock against a sales order at the moment of order creation. (02, 07)

**Retail event (อีเว้นท์)** — a temporary selling point. Carries the same true/pseudo tax-point split as consignment. (01, 04, 06)

**Sale-in (ยอดขายเข้า)** — the brand selling to the retailer. **The revenue event in outright modern trade.** (03)

**Sale-out (ยอดขายออก)** — the retailer selling to the shopper. Management information in outright modern trade; **the revenue event in consignment**. (03, 04)

**Sale channel (ช่องทางการขาย)** — the customer-group classification carried on the customer master. Drives reporting and, on inbound integrations, derives the accounting dimensions. (01, 11)

**Sell-through rate** — proportion of received stock sold within a period. Core seasonal-apparel measure. (07)

**Settlement (marketplace)** — the platform's periodic net remittance after fees, commission and subsidies. Reconciled many-to-one against orders. (05)

**Settlement three-way match** — ERP revenue against the platform's settlement report against the bank receipt. The design that answers whether the platform paid for everything shipped, whether its deductions were correct, and whether the net arrived. (05)

**Shadow book / second book** — the parallel inventory position used in the pseudo-consignment model to keep sight of goods already sold in the accounts. (04)

**Shrinkage** — unexplained stock loss, most visible at consignment counters and store floors. (04)

**Stock request / stock response** — the store's replenishment request and the ERP's answer; the request creates a transfer order for Supply Chain approval. (06)

**Subsidiary → Location → Bin** — the three-level inventory structure in this practice. (07)

**Tax invoice (ใบกำกับภาษี)** — the statutory Thai document. Its timing defines the channel design; its format is frequently a preprinted-form customisation. (01, 03, 04)

**Tax invoice on request** — the decision node in every consumer-facing flow. Determines whether a named invoice or an aggregated one is raised. (05, 06)

**Three-way matching** — matching invoice to purchase order to goods receipt before paying. (09)

**Traditional trade (ร้านค้าทั่วไป / เทรดดิชันแนลเทรด)** — dealers, wholesalers and independent shops. Outright sale. (02)

**Transfer order / transfer request (ใบขอโอน)** — the document moving stock between locations. The **document choice distinguishes true consignment (transfer request) from pseudo consignment (sales order)**. (04, 06)

**Transformation (แปรสภาพ)** — decorating or modifying goods. Two variants: **item code changes** and **item code unchanged**. (01, 08)

**True consignment (ฝากขายแท้)** — consignment where the **tax invoice is issued on sale-out**. Stock stays in a consignment location until sold; invoicing is grouped on a cycle. (04)

**Undeposited funds** — the holding account for receipts not yet confirmed against the bank; where deposits land before Finance verifies. (02)

**Weeks of supply** — stock on hand expressed as weeks of forward demand. (07)

**Work in process** — goods under transformation or production, owned and not sellable. (07, 08)

**Web EDI / EDI service bureau** — a shared service that exchanges trade documents with many retailers on a supplier's behalf, accessed through a web portal or integrated to the supplier's ERP. In the Thai market this covers the major chains and six document types. The pattern mirrors an API gateway for marketplaces: one connection for the ERP, many dialects absorbed by the provider. (03, 11)
