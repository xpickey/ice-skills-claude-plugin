## PART 2: Oracle EBS Procurement

### Core Modules Coverage

#### iProcurement (Self-Service Procurement)

**Requisition Processing**:
- **Requisition Creation**: Shop for items, non-catalog requests, services procurement
- **Shopping Lists**: Saved favorites, shopping cart, requisition templates
- **Catalog Management**: Internal catalog, punchout catalog, supplier catalog
- **Punchout Integration**: OCI, cXML, supplier website integration, roundtrip procurement
- **Requisition Preferences**: Default ship-to, deliver-to, charge account, requestor defaults
- **Multi-Line Requisitions**: Multiple lines, multiple suppliers, different charge accounts
- **Item Descriptions**: Free-text description, item attributes, attachments (specs, images)

**Approval Workflows**:
- **AME Integration**: Amount-based approval, position-based approval, exception approval
- **Approval Hierarchy**: Manager approval, budget owner approval, procurement approval
- **Delegation**: Vacation rules, temporary delegation, permanent delegation
- **Notification**: Email notifications, worklist, approval status tracking
- **Escalation**: Auto-escalation on timeout, reminder notifications

**Requisition Management**:
- **Requisition Status**: Draft, pending approval, approved, ordered, received, cancelled
- **Requisition Change**: Modify requisition, cancel lines, change quantity/date
- **Requisition Inquiry**: Search requisitions, view history, track delivery
- **Requisition Reports**: Requisition register, pending approval list, procurement backlog

#### Purchasing

**Purchase Order Types**:
- **Standard PO**: One-time purchase, full PO lifecycle (create, approve, receive, invoice)
- **Blanket Purchase Agreement (BPA)**: Long-term contract, release against BPA, price list
- **Contract Purchase Agreement (CPA)**: Master agreement, terms and conditions, no pricing
- **Planned PO**: Schedule of deliveries, blanket release, committed quantities
- **RFQ (Request for Quote)**: Supplier bidding, quote analysis, award to supplier

**PO Creation & Processing**:
- **Manual PO Creation**: Item-based, amount-based, services-based PO
- **AutoCreate**: Create PO from approved requisitions, source rules, auto-numbering
- **PO Templates**: Pre-filled PO, standard terms, approval routing
- **PO Approval**: Approval hierarchy, approval limits, position-based approval
- **PO Matching**: 2-way, 3-way, 4-way matching, tolerance setup
- **Change Order**: PO amendment, quantity change, price change, re-approval if needed
- **PO Cancellation**: Cancel PO, cancel line, cancel shipment, close for receiving/invoicing

**Supplier Management**:
- **Supplier Setup**: Supplier name, tax ID, payment terms, purchasing site, pay site
- **Supplier Qualification**: Supplier assessment, ISO certification, insurance, financial health
- **Supplier Performance**: On-time delivery, quality metrics, lead time analysis
- **Supplier Portal**: Supplier login, PO acknowledgment, ASN submission, invoice submission
- **Supplier Communication**: PO transmission (email, fax, EDI), acknowledgment tracking

**Receiving & Inspection**:
- **Receipt Entry**: Direct receipt, express receipt, cascade receipt
- **Receipt Matching**: Match to PO, auto-receive, over-receipt tolerance
- **Inspection**: Inspection required, inspection results, accept/reject/return
- **Receipt Correction**: Correct quantity, correct date, return to supplier
- **Receipt Traveler**: Print traveler, barcode scanning, RFID tracking
- **Receiving Reports**: Open receipts, received not invoiced, receipt history

#### Sourcing & Supplier Qualification

**Strategic Sourcing**:
- **Negotiation Types**: RFI, RFQ, Auction (forward, reverse, sealed bid)
- **Multi-Round Negotiation**: Supplier response, evaluation, counter-offer, final award
- **Evaluation Criteria**: Price, quality score, delivery performance, technical capability
- **Weighted Scoring**: Assign weights to criteria, calculate total score, ranking
- **Award Scenario**: Award to single supplier, split award, no award

**Supplier Qualification Management**:
- **Qualification Areas**: ISO 9001, ISO 14001, financial stability, insurance coverage
- **Questionnaires**: Create questionnaires, supplier responses, evaluation scoring
- **Document Requirements**: Upload certificates, insurance policies, financial statements
- **Qualification Status**: Qualified, disqualified, pending, expired
- **Re-Qualification**: Periodic re-qualification, expiration alerts, renewal process

---
