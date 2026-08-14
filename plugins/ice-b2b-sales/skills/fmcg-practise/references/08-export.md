# 08 — Export (ส่งออก / กลุ่มลูกค้าต่างประเทศ)

> **Load this when:** the buyer is outside the country — an overseas distributor, an overseas
> organisation, or an affiliate in another market · you hear "Inter Sale", "ขายต่างประเทศ",
> "cost sheet", "incoterm", "L/C", "ใบขนสินค้า" or "invoice เป็นดอลลาร์" · the sale needs shipping
> documents before anyone can be paid.
> **Do not load this for:** a domestic dealer → **01** · a domestic organisation → **07** ·
> cross-border consumer selling through a marketplace or the brand's own site, where the platform or
> the consumer is the debtor → **06** · **inbound** import costing on goods the company buys, which
> belongs to procurement and to file **11**.
> **Source basis:** **thin, and stated as such.** The apparel reference implementation carries export
> as a customer group running the **same wholesale spine as file 01** — four sourcing models across
> two payment terms — with geography and channel marked in the customer code, and an **export order
> cost sheet shown as a front-office capability outside the core ERP**. Currency and landed cost
> appear as named structures in its ledger design, and period-end revaluation of open
> foreign-currency balances as an optional step. Everything beyond that — incoterms, export
> documents, payment instruments, zero-rating — is **general practice knowledge, marked in place, and
> must be confirmed with the client and their tax adviser.**

## 1. Use cases — what this channel actually is

Export is the domestic wholesale process with three extra problems bolted to it: **the money is in a
different currency, the goods need papers to cross a border, and ownership may not change hands where
the goods leave the warehouse.** The commercial relationship is usually the same one file **01**
describes — an outright sale to a party who resells.

The recognisable situations: a brand appointing a distributor in a neighbouring market who buys in
bulk on its own account; an overseas organisation buying uniforms or kit directly; a group affiliate
in another country taking stock from the manufacturing entity; an overseas buyer whose bank, not the
buyer, is effectively the payer under a letter of credit.

| Sub-variant | What behaves differently |
|---|---|
| **Overseas distributor or dealer** | closest to file **01**; adds currency, documents and an incoterm |
| **Overseas organisation or project** | adds file **07**'s characteristics — made to order, deposits, tender paperwork — on top of the above |
| **Affiliate or intercompany sale** | the sale must be eliminated on consolidation, and it distorts promoted-revenue and incentive calculations if it is not — see files **15** and **18** |
| **Cross-border consumer sale** | not this file; the debtor is a platform or a consumer → **06** |

**The three defining facts.** The **tax invoice follows the shipping documents** rather than a
warehouse event. The **debtor is the overseas buyer** — or, under a documentary instrument, a bank
standing behind that buyer. And **who owns unsold stock depends on the incoterm**, which is the one
answer in this file that cannot be assumed from the channel: it is negotiated per contract and
sometimes per shipment.

In the reference implementation, export identity is carried in the **customer master** — a geography
segment separating local from overseas accounts, and a channel-group segment for the international
group — exactly as file **01** describes for domestic channels. The process itself was not
redesigned.

## 2. Process — the flow

### The spine — what the reference actually ran

```
front office: enquiry → export cost sheet assembled (OUTSIDE the core ERP)
  → quotation in the agreed currency and incoterm
  → stock check · credit check (or the terms of the payment instrument instead)
  → sales order + reservation        status = APPROVED (credit) | PENDING (cash / prepaid)
  → sourcing tail: stocked | made to order | transformation       (as files 01 and 12)
  → order fulfilment → warehouse confirms packed → STOCK RELIEVED, cost of sales posted
  → invoice / tax invoice — only from a fulfilment in shipped status
  → export documents assembled and released              [general practice — see below]
  → shipment → documents presented → collection in foreign currency
  → settlement, exchange difference recognised           [general practice — see below]
```

Only the unmarked steps are evidenced. Credit, deposit, cash gate, reservation, stock relief and
invoicing are file **01**'s mechanics and are not repeated here.

### The export cost sheet — where the price comes from

The reference architecture places **export order entry and the cost sheet in the front-office layer,
not in the core ERP** (file **16**). That is a defensible split: before a price can be quoted,
freight, insurance, duty, handling and inland transport have to be assembled for a specific
destination and incoterm, and that assembly is a quoting exercise, not an accounting one.

Two things follow. If the cost sheet lives outside the ERP, the **realised price and its build-up
must be written back** onto the ERP sales line, exactly as file **01** requires for discounts —
otherwise export margin cannot be analysed. And do not confuse it with **landed cost on inbound
goods**: the source's landed-cost mechanism is an *import* one, estimated at goods receipt and trued
up at the supplier invoice, belonging to procurement and file **11**. The two are called the same
thing in the same meeting and face in opposite directions.

### Incoterm, risk transfer and the stock cut-off — general practice, needs confirmation

Every channel in this practice relieves stock **when the physical movement is confirmed** — file
**00** records that as one rule everywhere, and lists export as relieving on fulfilment. An incoterm
can place the transfer of risk and title somewhere else: at the seller's dock, the port of loading,
on board, or the buyer's destination. **Where those two points differ, the goods are in transit and
belong to somebody on the balance sheet meanwhile.** The reference does not document how it handled
this, so treat it as an open design question rather than a solved one:

| Incoterm family | Where risk typically transfers | What the system has to answer |
|---|---|---|
| Seller's premises collection | at the seller's dock | nothing unusual — relief on fulfilment is right |
| Port or on-board terms | at the port of loading or on board the vessel | is the gap between warehouse departure and loading material enough to need a transit location? |
| Destination terms | at the buyer's named destination | the goods are the seller's for the whole voyage — a **goods-in-transit location** and a revenue point later than shipment |

Ask which incoterms the client uses, in what proportion, and whether their auditor has taken a
position. If destination terms are common, the revenue and stock cut-off is a real scope item.

### Currency — what is evidenced, and what is not

**Evidenced:** the ledger names **currency** as a structural element alongside the chart of accounts
and offers **period-end revaluation of open foreign-currency balances** as an optional close step;
purchasing supports multi-currency with an automatic daily rate update. **General practice, to
confirm:** order, invoice and settlement may each sit in a different currency; realised gain or loss
arises on settlement and unrealised on revaluation, and both need a home in the ledger; one agreed
rate source with a stated update rule stops three systems disagreeing about the same day.

### Documents, collection and tax — general practice, needs confirmation

Nothing in the source specifies these. They are named because a proposal that omits them is
incomplete, not because the reference proved them.

- **Documents** — commercial invoice, packing list, certificate of origin, shipping documents, plus
  whatever the destination market demands. They drive customs clearance **and** the buyer's payment
  release, so a document error is a cash-collection problem, not only a logistics one.
- **Payment instruments** — open account, advance payment, documentary collection and letter of
  credit each change *when* the receivable can be recognised and collected; a letter of credit also
  makes document accuracy a condition of payment.
- **Tax treatment** — Thai export sales are treated differently from domestic, and investment-promotion
  raw-material entitlement is tied to export production. The entitlement belongs to file **18**.
  **Export tax treatment is not covered anywhere in this skill and was not researched** — file **17**
  covers domestic value-added tax, withholding, electronic tax documents and competition law, not
  cross-border supply. Treat it as an open question for the client's tax adviser rather than an
  answer this skill holds.

## 3. Functions the system must provide

Several rows below are general practice rather than evidence from the reference implementation, and
the last column says so per row. A consultant lifting this table should carry that wording with it.

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **Overseas customer master** with geography and channel-group coding | separates export exposure, reporting and tax treatment from domestic | standard master data; the code structure is usually custom |
| 2 | Transact sales orders in a **currency other than the functional currency** | the whole channel depends on it | standard in mainstream ERP |
| 3 | **Exchange-rate source with a stated update rule** and rate held on the transaction | three systems must not disagree about one day's rate | standard; the governance is the work |
| 4 | **Realised and unrealised exchange difference** posted to designated accounts | otherwise margin moves for reasons nobody can name | standard |
| 5 | **Period-end revaluation of open foreign-currency receivables** | evidenced in the source as an optional close step | standard, configuration decision |
| 6 | **Export cost sheet** — freight, insurance, duty, handling assembled before quoting | a price cannot be committed without it | front-office capability in the reference; outside the core ERP |
| 7 | **Write-back of the quoted build-up and realised price** onto the ERP sales line | if the cost sheet is outside, this is the only way export margin exists | integration design — the file **01** rule applies unchanged |
| 8 | **Incoterm recorded on the order**, and driving the revenue and stock cut-off | risk may transfer where the goods are not | general practice — **not evidenced in the source**; confirm, and expect custom if destination terms are used |
| 9 | **Goods-in-transit location** for shipments the seller still owns | the balance sheet has to hold them somewhere | general practice — not evidenced; standard mechanism where the product supports it |
| 10 | **Export document set** produced or assembled from the order — commercial invoice, packing list, certificate of origin, shipping documents | customs clearance and payment release both depend on them | general practice — not evidenced; usually custom or handled outside the ERP |
| 11 | **Payment instrument recorded against the order** — open account, advance, documentary collection, letter of credit | it changes when the receivable can be collected | general practice — not evidenced; confirm before assuming a receivable behaves normally |
| 12 | **Export tax treatment and its evidence** | Thai export VAT treatment differs from domestic | see file **17**; confirm with the client's tax adviser |
| 13 | **Intercompany identification and elimination** on affiliate sales | unmatched intercompany revenue overstates group and promoted revenue | standard where a consolidation module exists — see files **15** and **18** |
| 14 | Credit assessment appropriate to a **cross-border counterparty** | recovery against an overseas debtor is not the same problem as against a domestic one | standard credit check; the policy behind it is the client's |
| 15 | **Invoice only from a fulfilment in shipped status** | the same control as every other channel | standard |
| 16 | Returns in two forms — with goods return, and credit note only | a cross-border physical return is expensive; credit-note-only matters more here | standard, needs deliberate design |

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Overseas customer creation and amendment | front office → ERP, result back | asynchronous | account, addresses, currency, terms |
| Stock availability, credit and overdue check | front office → ERP | synchronous | on-hand and available; credit remaining, overdue flag |
| Sales order creation and reservation | front office → ERP | **synchronous** | order header and lines, **currency, incoterm, price build-up** |
| Export cost sheet | front office, standalone | — | freight, insurance, duty, handling by destination |
| Exchange-rate feed | rate source → ERP | scheduled | daily rates per currency pair |
| Picking instruction and warehouse confirmation | ERP ↔ warehouse operator | asynchronous | fulfilment instruction, packed confirmation |
| Freight forwarder or customs broker | ERP ↔ external party | **general practice — not evidenced** | shipment booking, document set, clearance status |
| Bank — collection and settlement | bank → ERP | **general practice — not evidenced** | receipts in foreign currency, charges, exchange difference |

Only the rows without a marking are evidenced in the source. The last two are named because they are
where export programmes actually consume effort.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **Export treated as a separate process** | ran it as the same wholesale spine, differentiated by customer coding | keep the spine; add currency, incoterm and documents as attributes, not as a parallel design |
| **Incoterm ignored in the cut-off design** | **not documented** — stock relieves on fulfilment confirmation like every other channel | establish where risk transfers before fixing the revenue and stock cut-off; destination terms mean transit stock and a later revenue point |
| **Export cost sheet outside the ERP, and never written back** | the cost sheet is a front-office capability by design | keep it outside — but require the price build-up to land on the ERP line, or the channel cannot be analysed |
| **Inbound landed cost confused with the outbound cost sheet** | landed cost exists in the source as an **import** mechanism, estimated at receipt and trued up at invoice | say which direction is meant every time the phrase is used; they are different builds in different modules |
| **Currency treated as a display setting** | currency and revaluation exist as named structures; no sales-side design is documented | agree the rate source, the update rule, and where realised and unrealised differences post, in the first finance workshop |
| **Payment instrument assumed to be open account** | **not documented** | ask before assuming the receivable behaves normally; a documentary instrument changes collection and sometimes recognition |
| **Export documents assumed to come from the ERP** | **not documented; the front-office layer carries export order entry** | establish early what the ERP prints, what the forwarder produces and what is manual — this is usually where the estimate is wrong |
| **Tax position assumed** | not in scope of the source | confirm export VAT treatment (file **17**) and any investment-promotion entitlement (file **18**) with the client's advisers |
| **Intercompany sales left in group revenue** | flagged in the source's compliance design as a reason promoted revenue is overstated | identify affiliate sales at the point of order, not at consolidation |

## 6. Discovery questions

1. Which markets do you sell to, and is the buyer a distributor, an organisation, or your own
   affiliate? *(the third answer changes the accounting, not just the address)*
2. **In what currency do you quote, invoice and get paid — and are they the same one?** ⚑ *changes
   the estimate materially*
3. **Which incoterms do you sell on, and in what proportion?** Where do you consider the goods to
   stop being yours? ⚑
4. When do you recognise an export sale today — at shipment, at the shipping documents, or at
   arrival? ⚑
5. How is an export price built up today, and in what system does that cost sheet live? Does the ERP
   ever see the build-up, or only the final price? ⚑
6. Which documents must you produce per shipment, and who produces them — you or your forwarder?
7. How do overseas customers pay — open account, advance, documentary collection, letter of credit?
   ⚑ *this decides whether the receivable behaves normally*
8. Who bears the exchange risk between order and settlement, where does that difference show up
   today, and what rate do you use from what source?
9. What is your export tax position, and who has confirmed it? *(a question for their tax adviser,
   not for the vendor — file 17)*
10. Do you sell to your own overseas affiliates, and how are those sales identified and eliminated?
11. When an overseas customer rejects goods, do they physically come back?

## Related files

- **00** channel map and classification method, including the stock-relief rule this file qualifies
- **01** traditional trade — the shared process spine, credit, deposits, returns and the price
  write-back rule, none of which are repeated here
- **06** online and marketplace — cross-border selling where the debtor is a platform or a consumer ·
  **07** project and corporate — for overseas organisations buying against a requirement
- **11** inventory, locations and costing · **12** make to order and transformation · **14** procure to
  pay — where inbound landed cost lives, which is not this file
- **16** the application estate — where the export order and cost sheet sit in the front-office layer
- **17** Thailand compliance — electronic tax documents. **Export tax treatment is not covered there**
  and is an open question for the client's adviser
- **18** BOI and incentives — investment-promotion entitlement tied to export production
- **19** the full discovery bank
