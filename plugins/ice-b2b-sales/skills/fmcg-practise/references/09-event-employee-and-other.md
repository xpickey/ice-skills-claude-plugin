# 09 — Event, employee, complimentary and other (อีเว้นท์ · พนักงาน · อภินันทนาการ · อื่น ๆ)

> **Load this when:** the client's channel list has groups that do not fit anywhere else — roadshows,
> pop-ups, fairs, staff sales, giveaways, sponsorship goods, sample loans, a service line with no
> inventory behind it · the words "อีเว้นท์", "ออกบูธ", "ขายพนักงาน", "อภินันทนาการ", "ของแถม",
> "ยืมสินค้า" or "รายได้ค่าบริการ" appear · the channel count keeps growing during design and these are
> what is growing it.
> **Do not load this for:** the mechanics of true and pseudo consignment, which the event group reuses
> wholesale → **03 Consignment**. Nor for the permanent owned-store estate and its daily posting → **05
> Owned store and point of sale**, whose route several of these groups ride on.
> **Source basis:** one reference implementation — a Thai apparel and sportswear brand — whose
> finished channel model carried fifteen customer groups, of which five are collected here because
> each is too small to justify its own chapter and too different to be folded into another. The detail
> is thinner than in the major channel files, and deliberately so: these groups are usually a few days
> of design each, but they are also where a channel count quietly doubles.

## 1. Use cases — what this channel actually is

This file is the home for the customer groups that a sales director would not call channels and that
a controller cannot avoid treating as channels. They share one property: **each fails at least one of
the three classification questions in a way that stops it being folded into a neighbouring group.**

| Group | Thai | Tax point | Debtor | Unsold stock owned by |
|---|---|---|---|---|
| **Event and temporary retail** | ลูกค้าขายปลีกและอีเว้นท์ | follows the true or pseudo split, exactly as consignment does | varies with the split — the host, or the consumer | **the brand**, while the event runs |
| **Employee sales** | กลุ่มพนักงาน | at the sale, on the same point-of-sale route as a shop | the employee, or payroll where it is deducted | the brand, until sold |
| **Complimentary and giveaway** | กลุ่มลูกค้าอภินันทนาการ | **none — there is no sale** | **none** | the brand, until the goods leave as an expense |
| **Sample and sponsorship loan** | ยืมสินค้า | none while on loan | none | **the brand, at someone else's site** |
| **Other sales, and service revenue** | กลุ่มขายอื่น ๆ · กลุ่มงานบริการ | on invoice | the customer | **not applicable — service carries no inventory** |

Read the blanks in that table rather than skipping them. **A group with no tax point and no debtor is
not an incomplete row; it is the finding.** Complimentary goods move stock and create an expense
without ever creating revenue, and a design that forces them through the order-to-cash chain in order
to make the table look complete will produce revenue that does not exist and a receivable nobody will
ever collect. The same applies to service revenue in the opposite direction: it invoices without
touching inventory, so every stock-driven control in the order-to-cash spine has to be bypassed rather
than satisfied.

**The recognisable situations.** A brand takes a stand at a trade fair and moves stock to the venue
beforehand. It opens a staff sale at a discount, sometimes deducted from payroll. It gives product to a
sponsored team, to media, and to a customer as a goodwill gesture after a complaint. It lends samples
to a photo shoot and expects most of them back. It bills a fitting service that consumes no sellable
item. None of these is large, and together they routinely add four or five channels to a count that was
quoted as six. That is why this file exists: the reference implementation's tender assumed roughly six
channels and the finished design carried fifteen, with a meaningful share of the expansion sitting
here — groups finance insisted on separating because tax point, debtor or stock ownership genuinely
differed. Say so at scoping time, and price the long tail rather than discovering it.

### Event stock repeats the consignment split — and that is the whole point

The reference model applies the same **true and pseudo (แท้ / เทียม)** distinction to event and
temporary retail that it applies to consignment, which confirms the split is a reusable pattern rather
than a retailer-specific quirk. The trigger is the same in both cases: **goods are sitting somewhere
the brand does not permanently control, and the question is whether the tax invoice is due when they
got there or when they sell.** Where an event is hosted by a retailer or a venue that takes the money,
that is a consignment in substance no matter what the events team calls it.

The mechanics — transfer versus sales order, the shadow book, the sale-out feed, the reconciliation —
are **not repeated here**. They live in file **03** and are identical.

## 2. Process — the flow

```
EVENT AND TEMPORARY RETAIL
  event approved → stock moved to the venue
    · TRUE model  → transfer to an event location the brand still owns; no revenue yet
    · PSEUDO model→ moved as a sales order; stock relieved and the document raised on delivery,
                    with a shadow-book receipt for the same quantity
  → selling runs for the event window, sale-out captured
  → TRUE: sale-out creates the revenue · PSEUDO: sale-out relieves the shadow book
  → EVENT CLOSES → unsold stock returns → count against the sale-out → settle → close the location

EMPLOYEE SALES
  sale rung on the point-of-sale route, at the employee price basis
  → [branch] deducted from payroll? → passes to payroll rather than to a receipt
  → posted with the daily summary, but under its own customer group so it stays separable

COMPLIMENTARY AND GIVEAWAY
  internal request, approved to an authority level
  → stock issued from inventory → NO SALES ORDER, NO INVOICE, NO REVENUE
  → Dr expense (marketing, sponsorship, goodwill) / Cr Inventory
  → the reason and the recipient are the record; without them the entry cannot be defended

SAMPLE AND SPONSORSHIP LOAN
  goods issued to a loan location that the brand still owns
  → expected back → returned and inspected, or converted to a giveaway, or written off
  → an ageing report on the loan location is what stops the balance becoming permanent

OTHER SALES AND SERVICE
  invoice raised directly, with its own approval, carrying no inventory movement
  → the stock-driven controls of the order-to-cash spine are bypassed, not satisfied
```

**The complimentary flow is the one most often built wrong.** Because every other channel starts with
a sales order, the temptation is to raise a zero-value order and net it off. That produces a customer
who buys nothing repeatedly, a receivable that closes itself, and revenue reporting that has to be
explained every month. Issue the stock as a stock movement to an expense account and keep the sales
documents out of it entirely.

**The sample loan is the one most often forgotten.** It is stock the brand owns, sitting at a location
it does not control, with nobody chasing it — and it does not appear in any receivable ageing because
there is no receivable. A dedicated loan location with its own ageing view is the whole of the fix.

## 3. Functions the system must provide

| # | Function | Why it is needed | Typically standard or custom |
|---|---|---|---|
| 1 | **A separate customer group per behaviour**, not per sales-team label | these groups exist precisely because tax point, debtor or stock ownership differ | standard master data, deliberate governance |
| 2 | **A temporary location** for event stock, opened and closed with the event | stock at a venue is neither warehouse nor shop | standard, if location design allows short-lived locations |
| 3 | **Both consignment models available to the event group** — see file **03** | the event split is the consignment split | largely custom |
| 4 | **Event close-out**: unsold stock returned, counted against sale-out, location closed | an event that never closes leaves a permanent phantom location | custom, and usually a manual procedure |
| 5 | **Employee price basis** distinct from any customer price list | the discount must not leak into a commercial list | standard pricing |
| 6 | **Payroll-deduction branch** on the employee sale | the money never passes through a till | integration to payroll, usually custom |
| 7 | **Employee sales separable in reporting** for tax and benefit purposes | a staff benefit may be reportable; it is certainly auditable | standard, dimension-driven |
| 8 | **Complimentary issue with no sales document** — stock movement to an expense account | prevents fabricated revenue and a self-clearing receivable | standard inventory adjustment, with a deliberate account map |
| 9 | **Reason and recipient mandatory on every complimentary issue**, with an approval authority | an unexplained free issue is indistinguishable from shrinkage | standard workflow, must be configured |
| 10 | **A loan location for samples and sponsorship goods**, with an ageing view | owned stock at someone else's site with no receivable behind it is invisible otherwise | standard location plus a custom report |
| 11 | **Direct invoice with its own approval**, carrying no inventory | service revenue and one-off other sales have no fulfilment to bill from | standard, but the approval must be deliberate |
| 12 | **The shipped-status control relaxed only where there is genuinely nothing to ship** | the rule that an invoice may only be raised from a shipped fulfilment is a good rule; the exception must be narrow and named | configuration, governance-dependent |
| 13 | **Channel dimension carried on every one of these transactions** | otherwise the long tail disappears into "other" and nobody can size it next year | standard, governance-dependent |

The judgements in the last column describe mainstream capability in this category rather than any one
product's behaviour. Rows 3, 4, 6 and 10 are where the effort sits; the rest is configuration and
discipline.

## 4. Integration touchpoints

| Touchpoint | Direction | Mode | What it carries |
|---|---|---|---|
| Event stock movement | ERP → warehouse or third party | asynchronous | transfer or fulfilment to the event location |
| Event sale-out | temporary point of sale or merchandiser device → ERP | asynchronous, daily during the event | sale-out lines by item |
| Employee sale | point of sale → ERP | asynchronous, in the daily summary | revenue under the employee customer group |
| Payroll deduction | ERP → payroll | batch | employee, amount, period |
| Complimentary issue | internal request → ERP | none — internal | stock movement and expense account |
| Loan issue and return | ERP internal | none — internal | loan location movements |

Almost nothing here is a new interface. These groups mostly reuse the point-of-sale route of file
**05** and the consignment feed of file **03**; the payroll link is the only genuinely additional
connection, and it exists only where staff purchases are deducted rather than paid. The full estate
view lives in file **16**.

## 5. Challenges, gaps and improvement areas

| What commonly goes wrong | What the reference implementation did | What a better design looks like |
|---|---|---|
| **The long tail is left out of the channel count** | the tender assumed roughly six channels; the finished design carried fifteen, and several of the extra ones are in this file | enumerate customer groups by tax point, debtor and stock ownership during discovery, and price the tail explicitly |
| **Complimentary goods forced through the order-to-cash chain** | kept as a separate customer group with no revenue — stock and expense only | issue as a stock movement to an expense account; never raise a zero-value sales order to make the process look uniform |
| **A free issue with no reason and no named recipient** | approval to an authority level was part of the design | make reason, recipient and approver mandatory — otherwise the entry is indistinguishable from shrinkage and cannot be defended in an audit |
| **Event stock that never closes out** | the true and pseudo split was applied to events as it was to consignment | make the close-out — return, count, reconcile, close the location — an explicit step with an owner, because an event has no natural month-end |
| **An event treated as owned retail when the venue takes the money** | — | classify it exactly as a counter would be classified: who takes the money, and when is the tax invoice due — file **03** |
| **Sample and sponsorship loans invisible** | a dedicated loan location group existed in the location design | add the ageing view; the location alone tells nobody the goods have been out for a year |
| **Staff discount leaking into a commercial price list** | employee sales ran on the point-of-sale route under their own group and price basis | keep the price basis separate from any customer price list, and keep the group separable in reporting |
| **Service revenue fighting the inventory controls** | carried as its own group with no inventory behind it | name the exception narrowly and keep the shipped-status rule intact for everything else |
| **These groups quietly absorbed into "other"** | — | give each a channel dimension value of its own; a group that cannot be measured cannot be argued about next year |

## 6. Discovery questions

1. Beyond your main channels, which customer groups do you sell to that your sales team would not call
   a channel? ⚑ *this question, asked plainly, is what moves a channel count from six to fifteen*
2. Do you sell at events, fairs or pop-ups? Who takes the money at the stand — you, or the venue? ⚑
   *the answer decides whether this is a consignment*
3. Where does event stock come from, and what happens to what does not sell?
4. Do you sell to your own staff? Is it discounted, and is it ever deducted from payroll? ⚑
5. Does staff purchasing need to be reported separately for tax or benefit purposes?
6. Do you give product away — to sponsored teams, to media, as goodwill after a complaint? Who
   approves that today, and is the recipient recorded? ⚑
7. Do you lend product out — samples, shoots, sponsorship — and does it come back? How would you know
   if it had not?
8. Do you invoice anything that has no goods behind it at all — a service, a fee, a fitting?
9. Which of these groups do you need to see separately in your margin reporting, and which are content
   to sit in one bucket?

## Related files

- **00** channel map and the classification method — the three questions this file is built on
- **03** consignment — the true and pseudo mechanics that the event group reuses unchanged
- **05** owned store and point of sale — the route that employee and event sales ride on
- **11** inventory, locations and costing — location groups, including consignment-out, loan and scrap
- **16** the application estate and its integration catalogue
- **17** Thailand compliance — tax documents. **Note:** the tax treatment of goods given without
  consideration is **not covered there and was not researched** — treat it as an open question for
  the client's tax adviser rather than an answer this skill holds
- **19** the full discovery bank and what typically delays these programmes
