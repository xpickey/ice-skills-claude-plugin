# Glossary — FMCG / fashion multi-channel terms

Thai term in brackets where the Thai is what you will actually hear in a Bangkok meeting room.
Reference file numbers point to **where the term is explained in context** — not to where it is
merely mentioned. Terms with no number are conventions of this practice rather than file content.

**Accrual (trade spend)** — the trade obligation recognised as contra-revenue at the point of the sales invoice, once probable and estimable, then reviewed and trued up. The single source of truth for the accrued trade liability. (10)

**Allocation** — setting aside stock for a specific channel or order so another channel cannot take it. Alternative to a single live pool. (11)

**API gateway** — a brand-owned service sitting between marketplaces and the ERP so the ERP integrates once instead of once per platform. (06, 16)

**Assembly item** — a master record for a product built from components, used where transformation produces a distinct sellable item. (12)

**Back margin** — see *rebate*. (10)

**Banner** — an individual retail chain, as distinct from the group that owns it. One of the two axes of rebate scope, and the dimension every trade-spend transaction must carry. (10)

**Base price** — the list price held in the ERP before channel discounts. In both reference implementations the ERP holds only this; discounting happens in front-end systems, which is why the write-back matters. (01)

**Bill of materials** — the component list behind an assembled or transformed item. (12)

**Bill-payment reference (Thai QR)** — the matching key carried in a standardised QR payment: a mandatory reference of limited length plus an optional second. Check document-numbering length against it at design time. (17)

**Bin** — a subdivision of a location. In this practice bins separate stock **by material status** (good, damaged, customer claim) inside one location, and hold stock at bin-and-lot grain. (11)

**BOI / investment promotion (การส่งเสริมการลงทุน)** — privileges granted to a legal entity through one or more promotion certificates, each with its own promoted activity, exemption ceiling and period. "The company is BOI-promoted" is never a complete answer; ask how many certificates and where each is in its life. (18)

**Cannibalisation (ผลกระทบข้ามสินค้า)** — the demand a promoted item takes from other items in its set, held as a cross-elasticity relationship on the promotion record. The model behind the values is a customer decision, not something this practice supplies. (13)

**Cash on delivery** — the courier collects payment on handover and remits to the brand. Makes the **courier** the debtor, not the consumer. (06)

**Chargeback / deduction** — a retailer paying less than the invoice for short delivery, damage, lateness, a compliance penalty or a claimed entitlement. (10)

**Collection product (สินค้าใน Collection)** — a finished stocked item sold from inventory, as opposed to made to order or transformed. (01)

**Commercial credit note (ใบลดหนี้ทางการค้า)** — a credit document carrying **no VAT**, used in Thailand where a conditional rebate does not qualify as a tax credit note event. A distinct object from the tax credit note, with its own numbering series. Whether a specific rebate structure falls here is a question for the client's tax adviser. (10, 17)

**Complimentary (อภินันทนาการ)** — goods given away. Stock and expense move; no revenue. Its own customer group in the reference model. (09)

**Consignment (ฝากขาย)** — goods placed with a counterparty who sells them; ownership stays with the brand until sale. Two tax-point models — see *true* and *pseudo consignment*. (03)

**Consignment-in (รับฝากขาย)** — goods the brand holds and sells on someone else's behalf. The mirror of consignment-out; needs its own location group. (03, 11)

**Contribution-margin waterfall** — gross revenue → cost of sales → CM1 → trade deductions → CM2 → fulfilment cost → CM3 (Net GP). The reporting structure that answers which retailer is actually profitable. (10)

**Cost of inaction** — the section of a proposal quantifying what standing still costs. The only place loss-framed language is permitted.

**Credit note (ใบลดหนี้) / credit memo** — a document reducing a receivable. Two process paths — **with goods return**, and **credit note only** for price or allowance corrections with no goods movement — and, in Thailand, two distinct document types that must not share a numbering series. See *tax credit note* and *commercial credit note*. (11, 17)

**Customer hierarchy scope** — the customer axis of a rebate agreement (group, banner, store cluster), which cascades downward and must combine with the product axis without double-counting. The axis most home-grown designs omit. (10)

**Dead stock** — inventory with no movement over a defined period. Reported alongside fast- and slow-moving classification; custom in the reference implementations. (11)

**Deduct-first** — the retailer behaviour of short-paying an invoice and explaining afterwards, or not at all. The defining problem trade-spend management exists to solve. (10)

**Deduction intake** — the single front door that normalises every short-payment, whatever route it arrived by, into one claim structure. (10)

**Deposit (เงินมัดจำ)** — advance payment. Receipted separately, carries VAT and its own tax invoice, and must be netted off the final invoice. Note that a deposit is **not** a milestone-billing mechanism. (01, 07)

**Distribution-centre allowance** — a retailer charge for its own logistics, usually settled as a deduction. Market vocabulary rather than a named line in the reference material; treat it as a member of the **unconditional-fee family**, charged regardless of performance. (10)

**Double-dip** — the same entitlement settled twice, typically once by credit note and once by deduction. A recurring real loss; the matching engine must block it. (10)

**Electronic data interchange** — structured document exchange with a retailer. In the Thai market it is commercially available through service-bureau Web EDI covering the major chains and six document types; coverage is **per retailer and per document**, not one yes or no. Do not assume purchase-order-only. (02)

**Electronic tax invoice and receipt** — Thailand's structured, digitally signed tax-document scheme. Two mutually exclusive routes; the election is entity-wide, not per channel. **Elective in law but close to unavoidable in business-to-business practice** — counterparties pull you in and the state offers tax relief for adopting. Design so that adoption is a switch, not a rebuild. (17)

**Estimation method (expected value / most likely amount)** — the required per-contract choice of how an uncertain rebate outcome is estimated, together with constraining the estimate and reassessing it at each reporting date. Accruing at the current rate and truing up periodically satisfies the arithmetic but not the requirement. Confirm any standard citation with the client's auditor. (10)

**Export cost sheet** — the outbound quoting build-up assembled before an export price is given, in the reference implementation held **outside** the core ERP. Not to be confused with inbound landed cost — different direction, different build. (08)

**Fast/slow-moving report** — SKU movement classification driving markdown and buying decisions. (11)

**FEFO — first-expired-first-out (เบิกจ่ายตามวันหมดอายุ)** — the rule that the earliest-expiring lot leaves first, enforced at receipt, put-away, pick and van load-out, and return restock — four separate points, not one. It outranks fair-share allocation. (11, 13)

**Forecast accuracy (ความแม่นยำของการพยากรณ์)** — the measurement layer over a forecast, held at item × banner × period grain and separated between promoted and non-promoted periods so a promotional miss is investigated as an uplift assumption rather than as a baseline error. Tolerances are the customer's to set. (13)

**Fulfilment (Order Fulfilment)** — the warehouse instruction and its confirmation. Serves both sales orders and transfer orders. **Stock is relieved on confirmation, not on instruction** — and confirmation takes three forms across the channels: the warehouse's confirmation, the van settlement, and the daily store posting. (11)

**Goods return** — the physical return path, distinct from a credit-note-only adjustment. Returns are classified twice, by reason and by condition, and the disposition decides whether stock re-enters under FEFO. (11)

**Gross-profit guarantee** — the brand underwrites the retailer's margin; any shortfall is clawed back. (10)

**Growth rebate** — a rebate earned only on achieving growth against a base period. Reversed when the target will not be met. (10)

**In-transit location (คลังระหว่างทาง / ระหว่างทำ)** — where stock sits between despatch and receipt on an inter-site transfer, so it is never invisible and never double-counted. (05, 11)

**Inventory adjustment** — increase or decrease of stock outside a purchase or sale. Used in this practice for point-of-sale corrections, consignment relief, van recalibration and transformation cost setting. (11)

**Inventory ageing report** — stock by age band. Where seasonal margin is protected or lost. (11)

**Landed cost** — the full delivered cost of **inbound** purchased goods including freight, insurance, duty and handling, estimated at receipt and trued up when the supplier invoice arrives. An import mechanism — see *export cost sheet* for the outbound side. (11, 14)

**Listing fee / entry fee** — paid to a retailer to have a SKU carried. One of the unconditional-fee family, and named directly in Thai competition guidance on retailer charges. (10, 17)

**Loaned goods (คลังยืมสินค้า)** — samples, sponsorship stock and event loans. Owned, not sellable, and needing its own location group. (09, 11)

**Made to order (สั่งผลิต)** — produced or purchased against a specific customer order rather than sold from stock. (07, 12)

**Marketplace** — a third-party selling platform. Makes the **platform** the debtor and introduces net settlement. (06)

**Merchandiser / product consultant** — the brand's staff member working on a retailer's floor, who records sale-out and scans consignment receipts. (03)

**Modern trade (ห้างสรรพสินค้า / โมเดิร์นเทรด)** — organised retail: department stores, specialty chains, convenience chains, hypermarkets, cash-and-carry. **The channel, not the commercial model** — the same account can carry outright sale, true consignment and pseudo consignment at once, and what the retailer takes back is a domain of its own. (02)

**Moving average costing** — inventory valued at a rolling average cost. The reference implementation's method, with an open decision on whether the average is held per entity or per location. (11)

**Net GP** — margin after everything the retailer takes back. Distinct from gross margin, and the number the board is actually asking for. (10)

**Other charge for purchasing** — an orderable non-inventory charge line, used for the transformation service fee. (12)

**Outside processing (แปรสภาพ / งาน Outside)** — subcontracted transformation: blanks go to a supplier, come back decorated. Has its own location, master data and cost event. (12)

**Overselling** — the same physical unit sold twice across channels. Managed by live availability or by allocation. (06, 11)

**Platform special account** — the record electronic platforms above a defined size must maintain and file on seller activity. The obligation sits with the platform; the consequence for the seller is that its revenue is reported independently. (17)

**Platform-funded versus brand-funded discount** — who paid for a promotion. A platform-funded discount is not a cost to the brand; netting the two together understates online margin. Must be distinguishable on the ERP transaction line. (06)

**Portal registry** — the record of each retailer's dispute portal: submission window, accepted codes, required document formats, escalation contact. Missing the window is a permanent, avoidable loss. (10)

**Promoted versus non-promoted activity (กิจการที่ได้รับ / ไม่ได้รับการส่งเสริม)** — the split of revenue, cost and assets between business covered by a promotion certificate and business that is not. It has to be proven on the source document at posting, not reconstructed in the ledger at year end. (18)

**Promotion uplift** — the demand-side object of a campaign: an uplift factor and curve, a pull-forward assumption, a post-promotion dip window, and a cannibalisation set. The same promotion record that drives a trade-spend accrual drives this. (13)

**Promotion write-back** — the realised discount and campaign data returned from the channel front end onto the ERP sales line — gross price, discount amount and type, campaign code, net price and **who funded it** — so margin can be analysed by channel and campaign. The front end owns the decision; the ERP owns the record. (01, 02)

**Proof of performance** — evidence that a promotion ran as agreed, reconciled against the retailer's point-of-sale scan report before the claim is settled. (10)

**Prospective rebate** — a rebate mechanic where the benefit earned now applies to **future** purchases. Published guidance treats this as a customer option that may be deferred rather than accrued — a different accounting model, not a different rate. (10)

**Pseudo consignment (ฝากขายเทียม)** — consignment where the **tax invoice is issued on delivery**. Stock is relieved and revenue booked at delivery; a **shadow book** holds the position still at the retailer. Requires custom synchronisation. (03)

**Rebate / back margin** — volume- or period-based retailer compensation, decomposed into components each carrying basis, two-axis scope, mechanic and settlement. (10)

**Reservation (การจองสินค้า)** — holding stock against a sales order at the moment of order creation; all-or-nothing where availability is insufficient. (11)

**Responsibility categorisation** — classifying a deduction as caused by the supplier, the retailer, the carrier, or a genuine promotional entitlement, before deciding to accept or dispute. (10)

**Retail event (อีเว้นท์)** — a temporary selling point. Carries the same true/pseudo tax-point split as consignment, whose mechanics it reuses wholesale. (09)

**Retroactive tier** — a tier whose rate, once crossed, re-rates all prior volume in the period. Creates a catch-up charge at the moment of crossing; the most common trade-spend modelling error. (10)

**Route selling (การขายตามสายวิ่ง)** — selling along a published sequence of outlet stops, with the route calendar and stop sequence as master data and geofenced check-in proving the visit happened. (04)

**Safety stock (สต๊อกสำรอง)** — buffer inventory held as a **governed policy** per item by location or channel and differentiated by service level, not as one assumed buffer. The formula and the service-level table are customer decisions this practice does not supply. (13)

**Sale channel (ช่องทางการขาย)** — the customer-group classification carried on the customer master. Drives reporting and, on inbound integrations, derives the accounting dimensions. Its ledger counterpart is one designated reporting dimension, derived through a single governed mapping. (00, 16)

**Sale-in (ยอดขายเข้า)** — *in the accounting sense* — the brand selling to the retailer. **The revenue event where the arrangement is outright sale** — not wherever the goods went to a modern-trade retailer. For the planning sense see *sell-in*. (02, 03)

**Sale-out (ยอดขายออก)** — *in the accounting sense* — the retailer selling to the shopper. Management information in outright modern trade; **the revenue event in consignment**. For the planning sense see *sell-through*. (02, 03)

**Scanback / scan-down** — a promotion paid per unit actually scanned at the till, settled from the retailer's point-of-sale report. Distinct from an up-front billback. (10)

**Sell-in (ยอดขายเข้า) — as a demand signal** — the order or withdrawal signal: the distributor's order to the factory, or the retailer's order to the distributor. Inflated when the channel builds its own stock, so a spike may be replenishment rather than demand. Do not plan primary demand from it. (13)

**Sell-through (ยอดขายออก) — as a demand signal** — actual consumption at the retailer's till. The true signal, but it arrives late and incomplete. High sell-in against low sell-through is the divergence flag worth designing for. (13)

**Sell-through rate** — proportion of received stock sold within a period. Core seasonal-apparel measure, and an inventory metric rather than a planning feed. (11)

**Settlement (marketplace)** — the platform's periodic net remittance after fees, commission and subsidies. Reconciled many-to-one against orders. (06)

**Settlement three-way match** — ERP revenue against the platform's settlement report against the bank receipt. The design that answers whether the platform paid for everything shipped, whether its deductions were correct, and whether the net arrived. (06)

**Shadow book / second book** — the parallel inventory position used in the pseudo-consignment model to keep sight of goods already sold in the accounts. (03)

**Shelf life and lot aging (อายุสินค้า)** — remaining life measured against the consumption or delivery date rather than against today, driving near-expiry alerting, a mandatory action set and disposition routes. A planning dimension as much as a warehouse one, and the minimum remaining life a retailer will accept at receipt is a discovery question, never an assumption. (11, 13)

**Shrinkage** — unexplained stock loss, most visible at consignment counters and store floors. (03, 05)

**Stock request / stock response** — the store's replenishment request and the ERP's answer; the request creates a transfer order for Supply Chain approval. (05)

**Subsidiary → Location → Bin** — the three-level inventory structure in this practice, with lot beneath it wherever expiry matters. (11)

**Suspense (deduction)** — the visible, aged holding position for a deduction that cannot yet be applied to an open receivable. Never a general adjustment. (10)

**Tax credit note (ใบลดหนี้ภาษี)** — the statutory Thai VAT credit document, available only for a closed list of qualifying events and carrying its own content, timing and validity requirements. Whether a given rebate qualifies is a question for the client's tax adviser, not an assumption for the design. (17)

**Tax invoice (ใบกำกับภาษี)** — the statutory Thai document. Its timing defines the channel design; its format is frequently a preprinted-form customisation. (00, 03)

**Tax invoice on request** — the decision node in every consumer-facing flow. Determines whether a named invoice or an aggregated one is raised. (05, 06)

**Three-way matching** — matching invoice to purchase order to goods receipt before paying. (14)

**Trade agreement** — the annual commercial contract with a retailer, versioned and amendment-tracked, from which rebate components are decomposed. In Thailand it is also the evidence that a charge was agreed in advance. (10, 17)

**Trade-spend ratio** — trade spend as a proportion of revenue, shown alongside Net GP margin. Either figure alone misleads. (10)

**Traditional trade (ร้านค้าทั่วไป / เทรดดิชันแนลเทรด)** — dealers, wholesalers and independent shops. Outright sale. (01)

**Transfer order / transfer request (ใบขอโอน)** — the document moving stock between locations. The **document choice distinguishes true consignment (transfer request) from pseudo consignment (sales order)**. (03, 05)

**Transformation (แปรสภาพ)** — decorating or modifying goods. Two variants: **item code changes** and **item code unchanged**. (12)

**True consignment (ฝากขายแท้)** — consignment where the **tax invoice is issued on sale-out**. Stock stays in a consignment location until sold; invoicing is grouped on a cycle. (03)

**True-up** — the periodic adjustment bringing an accrual to actual, with the variance classified as one-time, structural or controllable. (10)

**Unconditional fee** — money the retailer charges regardless of performance — listing and slotting, new-store opening, shelf and display space, marketing development funds, free fill. A different family from rebates, treated by substance rather than accrued like one. (10)

**Undeposited funds** — the holding account for receipts not yet confirmed against the bank; where deposits land before Finance verifies. (01)

**Van inventory (สต๊อกบนรถ)** — stock loaded on a vehicle, keyed by vehicle, item and lot, carrying loaded, sold and returned quantities. Brand-owned stock in one person's custody overnight, outside the distribution centre, and audited on its own regime. (04)

**Van sales (ขายบนรถ / รถเร่)** — direct store delivery where the rep sells from what is on the vehicle, hands over the goods, takes the money or extends credit, and settles both stock and cash at the end of the shift. A delivery-and-settlement model layered on the traditional-trade customer base, not a different customer base. **How the document is issued on the vehicle is an open question to ask, not to assume.** (04)

**Van settlement (เคลียร์รถ / เคลียร์ของเคลียร์เงิน)** — the end-of-shift close on one record set: money reconciled on an explicit equation including change given, and stock reconciled per item **and per lot**. Maker, checker and poster are different people, and the posted reconciliation is immutable — a correction is a new adjustment, never an edit. This, not the moment of sale, is when van stock is relieved. (04)

**Web EDI / EDI service bureau** — a shared service that exchanges trade documents with many retailers on a supplier's behalf, accessed through a web portal or integrated to the supplier's ERP. The pattern mirrors an API gateway for marketplaces: one connection for the ERP, many dialects absorbed by the provider. (02, 16)

**Weeks of supply** — stock on hand expressed as weeks of forward demand. (11)

**Work in process** — goods under transformation or production, owned and not sellable. (11, 12)
