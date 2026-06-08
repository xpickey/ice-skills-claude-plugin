# Reference: Lending & Loan Origination

## Lending Product Taxonomy

### Consumer Lending (B2C)

#### Secured Products
| Product | Typical Tenure | Collateral | Risk Profile |
|---------|---------------|------------|--------------|
| Mortgage/Home Loan | 15-30 years | Property | Low |
| Auto Loan | 3-7 years | Vehicle | Low-Medium |
| Loan Against Property | 10-20 years | Property | Low |
| Gold Loan | 3-12 months | Gold | Very Low |

#### Unsecured Products
| Product | Typical Tenure | Credit Basis | Risk Profile |
|---------|---------------|--------------|--------------|
| Personal Loan | 1-5 years | Income/Score | Medium-High |
| Credit Card | Revolving | Income/Score | High |
| BNPL | 3-12 months | Limited | High |
| Overdraft | Revolving | Relationship | Medium |

### Commercial Lending (B2B)

#### Working Capital Finance
- **Cash Credit/Overdraft**: Revolving facility against current assets
- **Trade Finance**: LC, BG, export/import financing
- **Invoice Financing**: Factoring, reverse factoring, dynamic discounting
- **Supply Chain Finance**: Payables/receivables financing

#### Term Lending
- **Term Loans**: Capex financing, expansion funding
- **Project Finance**: Infrastructure, real estate development
- **Acquisition Finance**: M&A financing, LBO structures
- **Equipment Finance**: Asset-backed lending, leasing

---

## Loan Origination System (LOS) Architecture

### Functional Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                    LOAN ORIGINATION SYSTEM                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │ Customer │  │  Credit  │  │ Decision │  │ Document │            │
│  │ Onboard  │→ │  Check   │→ │  Engine  │→ │ Mgmt     │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│       │             │             │             │                   │
│       ▼             ▼             ▼             ▼                   │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐            │
│  │   KYC    │  │  Bureau  │  │   Risk   │  │ e-Sign/  │            │
│  │   AML    │  │  Integr. │  │  Scoring │  │ e-Stamp  │            │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘            │
│                                                                      │
│  ┌──────────────────────────────────────────────────────┐          │
│  │              WORKFLOW ENGINE                          │          │
│  │  (Application Routing, SLA Management, Escalations)   │          │
│  └──────────────────────────────────────────────────────┘          │
│                                                                      │
│  ┌──────────────────────────────────────────────────────┐          │
│  │              INTEGRATION LAYER                        │          │
│  │  (Core Banking, Payment, External APIs, Data Lake)    │          │
│  └──────────────────────────────────────────────────────┘          │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Data Requirements

#### Customer Data
- Demographics (Name, DOB, Address, Contact)
- Identity Documents (Government ID, Tax ID)
- Employment/Business Details
- Financial Statements (for business loans)

#### Credit Data
- Bureau Reports (Experian, Equifax, TransUnion, local bureaus)
- Bank Statements (transaction analysis)
- Existing Exposures
- Historical Repayment Behavior

#### Collateral Data
- Property Valuation Reports
- Vehicle Registration/Valuation
- Inventory/Receivables Aging

---

## Credit Decisioning Framework

### Scorecard Components

```
CREDIT SCORE = f(Application Score, Bureau Score, Behavioral Score)

Application Score:
├── Demographics (Age, Education, Marital Status)
├── Employment (Tenure, Industry, Designation)
├── Financial (Income, Assets, Liabilities)
└── Product-Specific (LTV, Tenure, Purpose)

Bureau Score:
├── Payment History (Delinquencies, Defaults)
├── Credit Utilization (Revolving, Term)
├── Credit Mix (Secured, Unsecured)
├── Credit Age (Average, Oldest Account)
└── Recent Inquiries

Behavioral Score (Existing Customers):
├── Account Conduct (Overdrafts, Bounces)
├── Relationship Depth (Products, Tenure)
├── Transaction Patterns (Cash Flow, Trends)
└── Previous Loan Performance
```

### Decision Matrix Example

| Score Range | Risk Grade | Decision | Pricing Tier |
|-------------|-----------|----------|--------------|
| 750+ | A | Auto-Approve | Tier 1 (Base Rate + 0-1%) |
| 700-749 | B | Auto-Approve | Tier 2 (Base Rate + 1-2%) |
| 650-699 | C | Refer to Underwriter | Tier 3 (Base Rate + 2-4%) |
| 600-649 | D | Enhanced Due Diligence | Tier 4 (Base Rate + 4-6%) |
| <600 | E | Decline | N/A |

---

## Vendor Landscape

### Enterprise LOS Platforms

| Vendor | Strengths | Best Fit |
|--------|-----------|----------|
| **nCino** | Salesforce-native, cloud-first | Banks on Salesforce ecosystem |
| **Finastra Fusion** | Comprehensive, global footprint | Large banks, multi-product |
| **Temenos Infinity** | Strong in consumer lending | Retail-focused banks |
| **Newgen** | BPM strength, cost-effective | Emerging markets |
| **Blend** | Digital mortgage excellence | US mortgage lenders |

### Point Solutions

| Category | Notable Vendors |
|----------|-----------------|
| Credit Decisioning | FICO, Experian PowerCurve, Zest AI |
| Document Management | DocuSign, Adobe Sign, Laserfiche |
| KYC/AML | Jumio, Onfido, LexisNexis |
| Bank Statement Analysis | Yodlee, Plaid, Perfios |

---

## Implementation Best Practices

### Phased Approach

**Phase 1: Foundation (3-4 months)**
- Core application capture
- Basic credit check integration
- Simple approval workflow
- Document upload capability

**Phase 2: Enhancement (3-4 months)**
- Advanced credit decisioning
- Automated document processing
- Complex workflow routing
- Customer portal

**Phase 3: Optimization (2-3 months)**
- Analytics and reporting
- Performance optimization
- Advanced integrations
- Self-service capabilities

### Common Pitfalls to Avoid

1. **Underestimating Data Migration**: Legacy data quality issues
2. **Scope Creep**: Too many customizations in Phase 1
3. **Integration Complexity**: Underestimating middleware needs
4. **Change Management**: Insufficient user training and adoption
5. **Testing Shortcuts**: Inadequate UAT and performance testing
