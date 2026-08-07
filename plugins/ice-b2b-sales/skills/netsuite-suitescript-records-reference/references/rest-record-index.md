# NetSuite REST Record API — Record Type Index (v1 / 2024.2)

> **Provenance:** extracted live from the NetSuite REST API Browser
> (`.../REST_API_Browser/record/v1/2024.2/index.html`) on **2026-08-07**.
> Source is the rendered Spectacle doc (17 chunks, ~16.8 MB HTML).
> **Total REST record types: 151** (NetSuite 2024 Release 2).
>
> This index lists *which* record types the REST Record API exposes. For each
> record's exact fields/operations, open that record in the Browser or pull the
> per-account metadata-catalog — see `rest-record-api.md`. REST naming (camelCase)
> differs from SuiteScript internal IDs; do not equate this list 1:1 with `records.json`.

## Standard operations per record type

Most record types expose: `GET /{recordType}` (list), `GET /{recordType}/{id}`,
`POST /{recordType}`, `PATCH /{recordType}/{id}`, `PUT /{recordType}/eid:{externalId}`
(upsert), `DELETE /{recordType}/{id}`, plus sublist sub-resources and, where applicable,
`POST /{recordType}/{id}/!transform/{target}`. Exact per-record operation availability
must be confirmed in the Browser / metadata-catalog (some records are read-only or
transform-only).

## All 151 record types (alphabetical)

**A** — account, accountingPeriod, advIntercompanyJournalEntry, assemblyBuild, assemblyItem, assemblyUnbuild

**B** — billingAccount, billingRevenueEvent, billingSchedule, bin, binTransfer, blanketPurchaseOrder, bom, bomRevision

**C** — calendarEvent, campaign, campaignResponse, cashRefund, cashSale, charge, check, classification, commerceCategory, competitor, consolidatedExchangeRate, contact, contactCategory, contactRole, costCategory, couponCode, creditCardCharge, creditCardRefund, creditMemo, currency, currencyRate, customer, customerCategory, customerDeposit, customerMessage, customerPayment, customerRefund, customerStatus, customerSubsidiaryRelationship

**D** — department, deposit, depositApplication, descriptionItem, discountItem, downloadItem

**E** — emailTemplate, employee, estimate, expenseCategory, expenseReport

**F** — fairValuePrice, fulfillmentRequest

**G** — giftCertificateItem

**I** — inboundShipment, intercompanyJournalEntry, intercompanyTransferOrder, inventoryAdjustment, inventoryCostRevaluation, inventoryCount, inventoryItem, inventoryNumber, inventoryTransfer, invoice, issue, itemFulfillment, itemGroup, itemReceipt, itemRevision

**J** — job, jobStatus, jobType, journalEntry

**K** — kitItem

**L** — location

**M** — manufacturingCostTemplate, manufacturingOperationTask, manufacturingRouting, markupItem, message

**N** — nexus, nonInventoryPurchaseItem, nonInventoryResaleItem, nonInventorySaleItem, noteType

**O** — opportunity, otherChargePurchaseItem, otherChargeResaleItem, otherChargeSaleItem, otherName, otherNameCategory

**P** — partner, paycheck, paymentItem, paymentMethod, phoneCall, priceBook, priceLevel, pricePlan, pricingGroup, projectTask, promotionCode, purchaseContract, purchaseOrder, purchaseRequisition

**R** — resourceGroup, returnAuthorization, revRecSchedule, revRecTemplate

**S** — salesOrder, salesRole, salesTaxItem, servicePurchaseItem, serviceResaleItem, serviceSaleItem, shipItem, statisticalJournalEntry, subscription, subscriptionChangeOrder, subscriptionLine, subscriptionPlan, subscriptionTerm, subsidiary, subtotalItem, supportCase

**T** — task, taxType, term, timeBill, timeSheet, topic, transferOrder

**U** — unitsType, usage

**V** — vendor, vendorBill, vendorCategory, vendorCredit, vendorPayment, vendorPrepayment, vendorPrepaymentApplication, vendorReturnAuthorization, vendorSubsidiaryRelationship

**W** — webSite, workOrder, workOrderClose, workOrderCompletion, workOrderIssue

## Notes

- **151** is the REST standard-record count for 2024.2 — smaller than SuiteScript's
  272 (`records.json`), because REST exposes a curated subset (plus custom record types,
  which appear per-account and are not in this static list).
- Custom record types are reachable via `GET /record/v1/customrecord_<id>` when enabled,
  but are account-specific and not part of this standard index.
- Newer releases (2025.1+) add/adjust record types — re-extract from the matching Browser
  release or the account metadata-catalog to stay current.
