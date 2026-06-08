## PART 12: Common Implementation Scenarios

### Scenario 1: Multi-Org with Shared Services

**Business Context**:
- Multiple operating units (OUs) across different countries
- Centralized shared services center in Thailand
- Shared AP, AR, Treasury, Payroll
- Local procurement and order management
- Consolidated reporting at group level

**Solution Design**:
- Set up multiple OUs under single ledger
- Multi-Org Access Control (MOAC) for cross-OU visibility
- Centralized supplier master, customer master, item master
- Inter-OU transfers for goods movement between OUs
- Intercompany invoicing for services (management fee, royalty)
- Security profiles to restrict users to their OU
- Global lookups for consistency (payment terms, freight terms)

### Scenario 2: Manufacturing with By-Products & Co-Products

**Business Context**:
- Process manufacturing (food, chemical, pharmaceutical)
- Multiple products from single production run
- Co-products (main products of similar value)
- By-products (minor products, lower value)
- Quality testing and lot tracking required

**Solution Design**:
- Process Manufacturing (OPM) module, not Discrete
- Formula with multiple products, co-products, by-products
- Cost allocation across products (market value, volume, weight)
- Quality specifications and test methods per product
- Lot and expiration date control
- Certificate of Analysis (COA) generation
- Waste and yield tracking

### Scenario 3: Project-Based Accounting

**Business Context**:
- Engineering & construction company
- Project-based revenue and cost tracking
- Progress billing and retention
- Multi-currency projects
- Project-specific chart of accounts segment

**Solution Design**:
- Project Accounting (PA) module or Project segment in COA
- Project-based purchasing (charge to project on PO/requisition)
- Project-based time entry (timecards charged to project)
- Project WIP (Work in Process) tracking
- Project revenue recognition (% completion, milestone-based)
- Project invoicing (progress billing, retention, final billing)
- Project costing (actual cost, committed cost, forecast)
- Project reporting (budget vs. actual, variance analysis, profitability)

### Scenario 4: Consignment & VMI (Vendor Managed Inventory)

**Business Context**:
- High-value components held on consignment
- Supplier owns inventory until consumption
- Automatic replenishment by supplier (VMI)
- Consumption-based invoicing

**Solution Design**:
- Consignment agreement with supplier
- Consigned subinventory setup
- No PO required for consigned items (blanket agreement)
- Consumption transaction triggers AP invoice creation
- Supplier visibility to on-hand levels (supplier portal)
- Automatic replenishment based on min-max levels
- Monthly reconciliation of consumed vs. invoiced qty

### Scenario 5: Drop Ship & Back-to-Back

**Business Context**:
- Distributor model, no physical inventory
- Customer order triggers supplier purchase
- Supplier ships directly to customer
- Revenue recognition without possession

**Solution Design**:
- Drop ship order type in Order Management
- Link sales order line to purchase order line
- PO created automatically from sales order (AutoCreate)
- Supplier ships to customer, sends ASN
- Receipt in OM (not in Inventory)
- Customer invoice created automatically
- Supplier invoice matched to PO (2-way match, no receipt)
- No inventory on-hand, no cost of goods sold until supplier invoice

---
