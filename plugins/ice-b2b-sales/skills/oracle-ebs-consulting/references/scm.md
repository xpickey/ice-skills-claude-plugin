## PART 3: Oracle EBS Supply Chain Management

### Inventory Management (INV)

**Organization & Setup**:
- **Organization Hierarchy**: Business group, legal entity, operating unit, inventory org
- **Organization Parameters**: Master org, child org, costing org, distribution network
- **Inventory Parameters**: Negative inventory, cost method (standard, average), cycle count
- **Locators**: Aisle, row, bin, sub-inventory, locator control (none, pre-specified, dynamic)
- **Sub-Inventories**: Asset sub-inventory, expense sub-inventory, locator control, picking order
- **Shipping Networks**: Define shipping relationships, transit times, shipping methods

**Item Master & Categories**:
- **Item Definition**: Item number, description, UOM, item type (purchased, manufactured, service)
- **Item Attributes**: Stockable, transactable, inventory item, purchasable, customer orderable
- **Item Status**: Active, inactive, obsolete, pending, discontinued
- **Item Templates**: Pre-defined item attributes, apply template to new items
- **Item Categories**: Purchasing category, planning category, costing category, sales category
- **Category Sets**: Define category sets, assign categories to items, category hierarchy
- **Item Revisions**: Engineering changes, revision control, effectivity dates
- **Item Cross-References**: Supplier item number, customer item number, manufacturer part number

**Inventory Transactions**:
- **Miscellaneous Issue**: Issue to expense, issue to scrap, issue to project
- **Miscellaneous Receipt**: Receipt from supplier, receipt from production, correction receipt
- **Subinventory Transfer**: Move between sub-inventories, locator transfer
- **Inter-Org Transfer**: Transfer between inventory orgs, in-transit tracking, receipt at destination
- **Direct Ship**: Ship from supplier to customer, drop ship, back-to-back order
- **Consigned Inventory**: Vendor-owned inventory, consume on usage, vendor replenishment

**Inventory Costing**:
- **Cost Elements**: Material, material overhead, outside processing, resource, overhead
- **Costing Method**: Standard costing, average costing, FIFO, LIFO (via customization)
- **Cost Updates**: Standard cost update, pending cost, cost rollup, cost history
- **Material Overhead**: Overhead rates, absorption accounts, overhead pool
- **Inventory Valuation**: Valuation report, inventory value by org, by sub-inventory
- **Cost Accounting**: Cost of goods sold, inventory adjustments, variance analysis

**Cycle Counting & Physical Inventory**:
- **Cycle Count**: ABC classification, count frequency, count schedules
- **Cycle Count Entry**: Count entry, adjustment approval, adjustment processing
- **Variance Tolerance**: Approval required if variance exceeds tolerance
- **Physical Inventory**: Freeze inventory, count tags, tag reconciliation, adjustments
- **Physical Inventory Reports**: Count sheets, variance reports, adjustment reports

**Inventory Reporting & Inquiry**:
- **On-Hand Inquiry**: Current on-hand by org, sub-inventory, locator, lot, serial
- **Transaction History**: Item transaction history, transaction types, transaction sources
- **Replenishment**: Min-max planning, reorder point, safety stock, lead time
- **Inventory Aging**: Aging buckets, slow-moving items, obsolete items
- **Lot/Serial Tracking**: Lot control, serial control, lot genealogy, serial genealogy

### Order Management (OM)

**Sales Order Processing**:
- **Order Entry**: Manual order entry, order import interface, EDI orders, web orders
- **Order Types**: Standard order, return order, internal order, drop ship, back-to-back
- **Order Lines**: Item, price, quantity, ship-to, schedule date, shipping method
- **Order Holds**: Credit hold, shipping hold, pricing hold, manual hold, release hold
- **Order Scheduling**: ATP (Available to Promise), CTP (Capable to Promise), reservation
- **Order Promising**: Promise date, delivery lead time, transportation lead time
- **Order Split**: Split lines, split shipments, partial shipment allowed
- **Order Changes**: Change quantity, change date, change price, change customer

**Pricing & Discounts**:
- **Price Lists**: Standard price list, promotional price list, customer-specific price list
- **Price Modifiers**: Discounts, surcharges, freight charges, promotional pricing
- **Pricing Rules**: Price precedence, price break, volume discount, customer agreements
- **Price Adjustments**: Price protection, retroactive pricing, manual price override
- **Discount Policies**: Early payment discount, volume discount, promotional discount

**Order Fulfillment**:
- **Pick Release**: Wave planning, pick wave execution, pick slip printing
- **Warehouse Operations**: Pick confirm, pack, weigh, ship confirm
- **Backorder Processing**: Backorder allocation, backorder fulfillment, partial shipment
- **Ship Confirm**: Generate packing slip, bill of lading, shipping labels
- **Shipping Integration**: Integration with carriers (FedEx, UPS, DHL), tracking numbers
- **Drop Ship**: Supplier ships to customer, PO-SO linkage, supplier ship notification

**Return Management (RMA)**:
- **Return Authorization**: RMA creation, return reason codes, return approval
- **Receiving Returns**: Receipt of returned goods, inspection, restocking
- **Credit Processing**: Issue credit memo to customer, restock or scrap decision
- **Return to Vendor (RTV)**: Return defective goods to supplier, supplier credit

### Shipping Execution (WSH)

**Delivery & Shipping**:
- **Delivery Creation**: Auto-create deliveries, manual grouping, delivery consolidation
- **Carrier Setup**: Carrier definition, freight terms, shipping methods, service levels
- **Freight Costing**: Freight rates, freight charges, freight billing
- **Ship Confirm**: Generate shipping documents, update inventory, create invoice interface
- **Manifesting**: Carrier manifest, shipment summary, close manifest

**Warehouse Management (WMS - Optional)**:

- **Inbound**: ASN processing, directed putaway, cross-docking, quality inspection
- **Outbound**: Wave planning, task management, directed picking, packing, staging
- **Mobile Devices**: RF devices, barcode scanning, RFID, voice picking
- **Labor Management**: Task assignment, productivity tracking, performance metrics

### Advanced Planning (ASCP)

**Demand & Supply Planning**:
- **Demand Sources**: Sales orders, forecasts, inter-org demands, planning bills
- **Supply Sources**: On-hand inventory, POs, WIP jobs, in-transit shipments
- **Planning Parameters**: Planning horizon, planning fence, demand time fence
- **Planning Constraints**: Capacity constraints, material constraints, lead time
- **Safety Stock**: Safety stock calculation, reorder point, min-max planning

**Master Production Schedule (MPS)**:
- **MPS Planning**: Plan at MPS level, firm planned orders, release to MRP/MPS
- **Planning Bills**: Super BOMs, option classes, planning percentages
- **Final Assembly Schedule (FAS)**: Configure-to-order, final assembly planning

**Material Requirements Planning (MRP)**:
- **Net Requirements**: Gross requirements, scheduled receipts, projected on-hand, net requirements
- **Planned Orders**: Planned purchase orders, planned WIP jobs, reschedule recommendations
- **Pegging**: Demand pegging, supply pegging, order traceability
- **MRP Action Messages**: Expedite, de-expedite, cancel, reschedule, release

---
