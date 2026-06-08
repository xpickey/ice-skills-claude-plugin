## PART 9: Configuration Deliverables

### MD050 Configuration Workbooks

**General Ledger MD050**:
1. Chart of Accounts structure and segment definitions
2. Value sets and cross-validation rules
3. Ledger setup (primary, secondary, reporting currency)
4. Accounting calendar and periods
5. Journal sources and categories
6. AutoAccounting rules and SLA configuration
7. Allocation rules and statistical accounts
8. Currency rates and translation methods
9. Consolidation setup and elimination rules
10. FSG report definitions and account hierarchies

**Accounts Payable MD050**:
1. Supplier setup and classification
2. Supplier sites and payment terms
3. Payment methods and bank accounts
4. Invoice tolerances and matching rules
5. Approval workflows and hold reasons
6. Withholding tax setup and tax codes
7. Expense report policies and categories
8. Accrual accounting rules
9. Payment formats and positive pay
10. Period-end close checklist

**Accounts Receivable MD050**:
1. Customer setup and profile classes
2. Customer sites and payment terms
3. Transaction types and sources
4. AutoCash rules and receipt methods
5. Revenue recognition rules
6. Credit management and risk scoring
7. Collections setup and dunning
8. Lockbox configuration
9. AutoAccounting rules
10. Statement cycles and printing

**Fixed Assets MD050**:
1. Asset categories and hierarchies
2. Asset books and depreciation methods
3. Location setup and asset tagging
4. Mass addition sources (PO, AP)
5. Prorate and retirement conventions
6. Depreciation calendars and schedules
7. Asset key flexfield structure
8. Physical inventory procedures
9. Revaluation and impairment rules
10. Asset reports and inquiries

**Procurement MD050**:
1. Purchasing options and controls
2. Document types and numbering
3. Approval hierarchies and limits
4. Receiving controls and tolerances
5. Blanket agreements and contracts
6. Supplier catalog and punchout
7. Requisition templates and preferences
8. AutoCreate rules and sourcing
9. Drop ship and direct delivery
10. Procurement reports

### MD070 Test Scripts

**Test Script Structure**:
- **Test ID**: Unique identifier
- **Test Scenario**: Description of business scenario
- **Pre-Requisites**: Master data, setup, permissions required
- **Test Steps**: Step-by-step instructions
- **Expected Results**: What should happen
- **Actual Results**: What actually happened
- **Status**: Pass / Fail / Blocked
- **Defects**: Link to defect tracking system
- **Tester**: Who executed the test
- **Date**: When test was executed

**Sample End-to-End Test Scenarios**:

1. **Procure-to-Pay**:
   - Create requisition → Approve → AutoCreate PO → Approve PO → Receive goods → Match invoice → Approve invoice → Create payment → Post to GL

2. **Order-to-Cash**:
   - Enter sales order → Credit check → Schedule → Pick release → Ship confirm → Invoice → Receipt → Apply to invoice → Post to GL

3. **Hire-to-Retire**:
   - Hire employee → Assign to position → Enter time → Process payroll → Distribute cost → Post to GL → Terminate employee

4. **Procure-to-Manufacture**:
   - Create requisition → PO → Receipt → WIP job → Issue material → Complete assembly → Deliver to inventory → Cost WIP job → Close job

5. **Plan-to-Produce**:
   - Enter forecast → MRP planning → Planned orders → Release to WIP → Production execution → Completion → Costing → Closing

---
