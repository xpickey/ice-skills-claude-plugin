# 03 — Modern Trade: outright sale to organised retail

> Load this when department stores, specialty chains, convenience chains, key accounts,
> sale-in versus sale-out, EDI, or retailer deductions are in scope.
> For goods that stay on the brand's books at the retailer, go to **04 Consignment** instead.

## What modern trade means here

Modern trade in this practice is **outright sale (ขายขาด)** to organised retail — department
stores, specialty stores and convenience chains. The retailer buys the goods, owns them, and
resells at its own risk. Commercially this is closer to a large dealer than to consignment,
even though both involve a shop floor.

Confusing the two is the single most common scoping error on a consumer-goods deal, because the
customer's own sales team often calls both "selling into the mall". Separate them in discovery
with the ownership question: **after delivery, if the goods do not sell, who carries them on
their balance sheet?**

## Sale-in versus sale-out — say what you mean

| Term | Thai | Meaning | Who records it |
|---|---|---|---|
| **Sale-in** | ยอดขายเข้า | the brand sells to the retailer | the brand — this is the revenue event in outright modern trade |
| **Sale-out** | ยอดขายออก | the retailer sells to the shopper | the retailer's point of sale, fed back to the brand |

In **outright** modern trade, revenue is recognised on sale-in. Sale-out data is still valuable —
it drives replenishment, promotion effectiveness and demand planning — but it is **management
information, not an accounting event**.

In **consignment**, sale-out *is* the accounting event. This is why the two channels cannot share
one design.

The reference implementation still built a **sale-out reconciliation capability for modern trade**:
comparing sale-out reported by the front-line merchandiser network against invoices raised in the
ERP, and reporting the variance. That reconciliation exists to catch missing or duplicated
sale-in, not to post revenue.

## The order-to-cash chain

```
retailer purchase order arrives (portal, file, email, or rep-entered)
  → credit-limit + overdue-invoice check + stock check
  → sales order created + stock reserved, status approved
  → [deposit branch] deposit invoiced and receipted separately, VAT charged on the deposit
  → automatic release to the warehouse
  → warehouse picks, packs, ships   → stock relieved, cost of sales posted
  → Accounting prepares the invoice and tax invoice, NET OF ANY DEPOSIT,
    and sends it to travel with the goods
  → billing on the retailer's credit terms → receipt
```

Two details that repeat across consumer-goods deals:

- **The invoice travels with the goods.** In Thai organised retail the delivery is commonly
  refused at the dock without the correct statutory tax-invoice paperwork. That makes the
  preprinted-form requirement a *delivery* dependency, not a finance nicety.
- **Deposits are their own document chain.** A deposit is receipted, VAT is charged on it, a tax
  invoice is issued for it, and the final invoice must net it off. Missing the netting step is a
  recurring defect.

## EDI — the expectation gap worth naming early

The reference implementation's tender asked for **sale-in capture through an EDI provider**. The
outcome was recorded as a **GAP**: the counterparty could not use EDI for replenishment and
sales — **only for purchase orders**.

What shipped instead:
- **CSV/template import** for modern-trade orders and online-platform orders
- A **purpose-built order-entry screen** so modern-trade sales staff could pick items, check stock
  and create the order quickly — delivered as a customisation

**Carry this into every FMCG conversation.** Assume the retailer's EDI covers the purchase order
and little else. Budget for a file-import path plus a sale-out reconciliation report, and treat
full end-to-end EDI as an upside to be proven, not a baseline to be promised. Promising EDI
parity in a proposal and discovering the retailer's limits in build is a schedule risk that lands
squarely on the implementer.

## Trade terms and deductions — where margin actually goes

Organised retail rarely pays the invoice face value. The mechanisms in common use:

| Mechanism | What it is | Where it usually lands |
|---|---|---|
| Listing / entry fee | paid to have the SKU carried | supplier invoice or deduction |
| Rebate / back-margin | volume- or period-based rebate | credit note at period end |
| Distribution-centre allowance | charge for the retailer's logistics | deduction on payment |
| Promotion support | funding a price event or display | credit note or separate billing |
| Chargeback / deduction | short delivery, damage, late arrival, compliance penalty | short payment against the invoice |
| Return of unsold goods | negotiated take-back | credit note, with or without goods return |

**The design consequence:** the receivable that gets paid is rarely the receivable that was
raised. A modern-trade design must plan for **partial settlement with documented deductions**, and
must be able to distinguish "the retailer disputes this" from "the retailer applied an agreed
trade term". Without that split, the AR ageing report becomes noise within two quarters.

A pricing point from the reference implementation shapes how this must be built: **the ERP held only
a base price; discounts and promotions were defined in the channel front-end systems.** That
architecture is sound — the trade agreement lives where the account is managed. What it makes
non-negotiable is the **write-back**: every discount and promotion granted to a retailer must land
on the ERP sales line with its amount, its type and its funder (see file **02** for the full field
set). Modern trade is where this matters most, because a retailer's price is built from several
layers — trade discount, campaign support, volume rebate — and a single net figure on the invoice
tells you nothing about which layer moved.

With the write-back in place, the remaining honest limitation is narrower: the **agreed** terms sit
in the front end and the **granted** terms sit in the ERP, so a periodic report comparing the two is
still worth building. That is a report, not a redesign.

## Returns and credit notes

Two distinct paths, and modern trade uses both heavily:

- **Credit note with goods return** — unsold or damaged stock physically comes back, is received
  into a returns location, and a credit memo follows.
- **Credit note only** — a price correction, agreed allowance, or settled deduction, with no goods
  movement at all.

Forcing an allowance through a goods-receipt path (because the system only knows one return type)
creates phantom stock. Separate them from the start.

## Reporting the channel needs

From the reference implementation's requirements, all satisfied by saved searches and standard
reporting once the data model was right:

- Sale-out detail by retailer and SKU
- **Reconciliation variance between sale-out and invoices**
- Orders by sales channel
- Full transaction view per retailer: orders, returns and credit-note status, invoices and
  payments, shipments

## Scoping signals

Raise the estimate when you see:
- More than two or three retailer groups, each with its own portal and file format
- A demand for genuine EDI rather than file import
- Trade terms settled by deduction rather than by credit note
- Sale-out required for replenishment as well as reporting
- Statutory preprinted invoice formats differing by retailer

## Discovery questions

1. After you deliver, who owns the stock — you or the retailer?
2. How does the purchase order reach you today, per retailer?
3. Which trade terms do you agree, and are they settled by credit note or by deduction on payment?
4. Do you get sale-out data? In what form, how often, and what do you use it for?
5. When a retailer short-pays, how do you decide today whether it is a valid deduction?
6. Does any retailer refuse delivery without a specific document format?

## Related files

- **01** where modern trade sits among the other channels
- **04** consignment — the model to use when the goods stay yours
- **07** returns locations and the inventory backbone
- **11** the file-import and order integration touchpoints
- **12** gaps and improvement areas versus common practice
