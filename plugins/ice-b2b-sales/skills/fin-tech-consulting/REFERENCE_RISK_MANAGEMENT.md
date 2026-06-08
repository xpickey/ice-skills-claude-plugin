# Reference: Enterprise Risk Management

## Risk Taxonomy

### Credit Risk

```
CREDIT RISK
├── Default Risk
│   ├── Probability of Default (PD)
│   └── Loss Given Default (LGD)
├── Concentration Risk
│   ├── Single Name
│   ├── Sector/Industry
│   ├── Geographic
│   └── Product
├── Counterparty Risk
│   ├── Pre-settlement Risk
│   └── Settlement Risk
└── Country Risk
    ├── Transfer Risk
    └── Sovereign Risk
```

### Market Risk

| Risk Type | Description | Measurement |
|-----------|-------------|-------------|
| **Interest Rate Risk** | Sensitivity to rate changes | Duration, DV01, VaR |
| **FX Risk** | Currency exposure | Position limits, VaR |
| **Equity Risk** | Stock price movements | Beta, VaR |
| **Commodity Risk** | Commodity price exposure | VaR, stress tests |

### Operational Risk

```
OPERATIONAL RISK (Basel Categories)
├── Internal Fraud
├── External Fraud
├── Employment Practices & Workplace Safety
├── Clients, Products & Business Practices
├── Damage to Physical Assets
├── Business Disruption & System Failures
└── Execution, Delivery & Process Management
```

### Liquidity Risk

| Type | Description | Metrics |
|------|-------------|---------|
| **Funding Liquidity** | Ability to meet obligations | LCR, NSFR |
| **Market Liquidity** | Ability to liquidate assets | Bid-ask spread, market depth |
| **Contingent Liquidity** | Stress scenario funding | Stress test survival period |

---

## Risk Governance Framework

### Three Lines of Defense

```
┌─────────────────────────────────────────────────────────────────────┐
│                THREE LINES OF DEFENSE MODEL                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                           BOARD / AUDIT COMMITTEE                    │
│                                    │                                 │
│  ┌──────────────────┬──────────────┴──────────────┬───────────────┐ │
│  │                  │                              │               │ │
│  │   1ST LINE       │        2ND LINE             │   3RD LINE    │ │
│  │                  │                              │               │ │
│  │   Business       │        Risk Management      │   Internal    │ │
│  │   Operations     │        Compliance           │   Audit       │ │
│  │                  │                              │               │ │
│  │   • Own Risk     │   • Oversight & Challenge   │  • Independent│ │
│  │   • Execute      │   • Framework & Policy      │    Assurance  │ │
│  │     Controls     │   • Monitoring & Reporting  │  • Testing    │ │
│  │   • Report       │   • Guidance & Support      │  • Validation │ │
│  │                  │                              │               │ │
│  └──────────────────┴──────────────────────────────┴───────────────┘ │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Risk Appetite Framework

```
RISK APPETITE HIERARCHY

Board Risk Appetite Statement
    │
    ├── Quantitative Metrics
    │   ├── Capital: CET1 > 12%, Total CAR > 15%
    │   ├── Liquidity: LCR > 120%, NSFR > 110%
    │   ├── Credit: NPL < 3%, Concentration < 15%
    │   └── Operational: Op Risk Loss < 0.5% Revenue
    │
    ├── Qualitative Statements
    │   ├── Risk culture expectations
    │   ├── Strategic risk tolerance
    │   └── Conduct and compliance standards
    │
    └── Cascaded Limits
        ├── Business Unit Limits
        ├── Product Limits
        ├── Counterparty Limits
        └── Trader/Desk Limits
```

---

## Credit Risk Management

### Credit Risk Rating System

| Rating | PD Range | Description | Facilities |
|--------|----------|-------------|------------|
| 1 | 0.00-0.05% | Exceptional | Unsecured, high limits |
| 2 | 0.05-0.10% | Excellent | Unsecured, standard limits |
| 3 | 0.10-0.25% | Very Good | Unsecured/Secured |
| 4 | 0.25-0.50% | Good | Secured preferred |
| 5 | 0.50-1.00% | Satisfactory | Secured, enhanced monitoring |
| 6 | 1.00-2.50% | Adequate | Secured, covenants |
| 7 | 2.50-5.00% | Watch | Watchlist, remediation |
| 8 | 5.00-10.00% | Substandard | Active management |
| 9 | 10.00-25.00% | Doubtful | Workout, provision |
| 10 | >25.00% | Loss | Write-off candidate |

### Portfolio Risk Metrics

```python
# Key Portfolio Risk Calculations

# Expected Loss (EL)
EL = PD × LGD × EAD

# Unexpected Loss (UL) - simplified
UL = sqrt(PD × (1-PD)) × LGD × EAD × Correlation_Factor

# Economic Capital
EC = UL × Confidence_Factor  # e.g., 99.9% = 3.09 sigma

# Risk-Adjusted Return
RAROC = (Revenue - Costs - EL) / EC

# Portfolio Concentration (HHI)
HHI = Σ(Exposure_i / Total_Exposure)^2
```

---

## Stress Testing Framework

### Scenario Design

| Scenario Type | Purpose | Typical Shocks |
|---------------|---------|----------------|
| **Historical** | Replicate past crisis | 2008 GFC, 1997 Asian Crisis |
| **Hypothetical** | Explore potential events | Pandemic, cyberattack |
| **Sensitivity** | Single factor shock | +200bps rates, -20% property |
| **Reverse** | Find breaking point | What causes capital breach |

### Stress Test Process

```
┌─────────────────────────────────────────────────────────────────────┐
│                  STRESS TESTING WORKFLOW                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   1. SCENARIO        2. TRANSLATION      3. IMPACT         4. MGMT  │
│      DESIGN              ENGINE          ASSESSMENT        ACTION   │
│                                                                      │
│   ┌─────────┐       ┌─────────────┐     ┌──────────┐    ┌────────┐ │
│   │ Macro   │       │ Satellite   │     │ Capital  │    │ Capital│ │
│   │ Scenario│──────▶│ Models      │────▶│ Impact   │───▶│ Actions│ │
│   └─────────┘       └─────────────┘     └──────────┘    └────────┘ │
│                                                                      │
│   GDP: -5%          PD ↑ 2x             CET1: 12%→9%    Dividend   │
│   Unemp: +4%        LGD ↑ 1.3x          RWA: ↑15%       cut,       │
│   Rates: +200bps    Collateral ↓20%     P&L: -$500M     Asset      │
│   Property: -25%                                         sales      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Model Risk Management

### Model Lifecycle

```
MODEL LIFECYCLE MANAGEMENT

1. DEVELOPMENT
   ├── Business requirement
   ├── Data exploration
   ├── Model design
   ├── Build & calibration
   └── Documentation

2. VALIDATION
   ├── Conceptual soundness
   ├── Data quality review
   ├── Quantitative testing
   ├── Outcomes analysis
   └── Validation report

3. IMPLEMENTATION
   ├── Approval (Model Committee)
   ├── Production deployment
   ├── User training
   └── Controls implementation

4. MONITORING
   ├── Performance tracking
   ├── Stability monitoring
   ├── Back-testing
   └── Periodic review

5. RETIREMENT
   ├── Trigger assessment
   ├── Replacement planning
   ├── Decommissioning
   └── Documentation archival
```

### Model Tiering

| Tier | Criteria | Validation Frequency | Governance |
|------|----------|---------------------|------------|
| **Tier 1** | Regulatory capital, pricing, IFRS9 | Annual + event-driven | Board approval |
| **Tier 2** | Management reporting, limits | 18-24 months | CRO approval |
| **Tier 3** | Operational, low materiality | 24-36 months | Business approval |

---

## Regulatory Capital (Basel III/IV)

### Capital Components

```
CAPITAL STRUCTURE

Total Capital = Tier 1 + Tier 2

Tier 1 Capital (Going Concern)
├── CET1 (Common Equity Tier 1)
│   ├── Common shares
│   ├── Retained earnings
│   ├── AOCI (adjusted)
│   └── Regulatory deductions
└── AT1 (Additional Tier 1)
    └── Perpetual instruments

Tier 2 Capital (Gone Concern)
├── Subordinated debt (>5 years)
├── General provisions (up to 1.25% RWA)
└── Hybrid instruments

Minimum Requirements:
├── CET1: 4.5%
├── Tier 1: 6.0%
├── Total Capital: 8.0%
└── Buffers: Conservation (2.5%), Countercyclical (0-2.5%), G-SIB (1-3.5%)
```

### Risk-Weighted Assets

| Approach | Credit Risk | Market Risk | Operational Risk |
|----------|-------------|-------------|------------------|
| **Standardized** | Regulatory risk weights | Standardized tables | Basic Indicator / Standardized |
| **Advanced** | IRB (Foundation/Advanced) | Internal Models | Advanced Measurement |
