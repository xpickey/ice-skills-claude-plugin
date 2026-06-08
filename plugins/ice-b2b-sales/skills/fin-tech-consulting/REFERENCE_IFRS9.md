# Reference: IFRS9 & ECL Engine

## IFRS9 Overview

### Key Changes from IAS 39

| Aspect | IAS 39 (Old) | IFRS9 (New) |
|--------|--------------|-------------|
| **Impairment Model** | Incurred Loss | Expected Credit Loss |
| **Recognition Timing** | Loss event required | Forward-looking from Day 1 |
| **Staging** | Not applicable | 3-stage model |
| **Calculation** | Point-in-time | Lifetime expected loss |

### Three-Stage Model

```
┌─────────────────────────────────────────────────────────────────────┐
│                    IFRS9 STAGING MODEL                               │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   STAGE 1              STAGE 2              STAGE 3                 │
│   ════════             ════════             ════════                │
│   Performing           Underperforming      Non-Performing          │
│                                                                      │
│   • No SICR            • SICR occurred      • Credit-impaired       │
│   • 12-month ECL       • Lifetime ECL       • Lifetime ECL          │
│   • Interest on        • Interest on        • Interest on           │
│     gross amount         gross amount         net amount            │
│                                                                      │
│   ◄─────────────────────────────────────────────────────────────►   │
│                                                                      │
│   Triggers for Stage Movement:                                       │
│   Stage 1 → 2: SICR (30 DPD, rating downgrade, watchlist)          │
│   Stage 2 → 3: Default (90 DPD, unlikely to pay, distressed)       │
│   Stage 2/3 → 1: Cure period satisfied, performance restored       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Significant Increase in Credit Risk (SICR)

#### Quantitative Indicators
- **PD Threshold**: Relative increase (e.g., 2x origination PD) or absolute increase
- **DPD Trigger**: Typically 30 DPD (rebuttable presumption)
- **Rating Migration**: Downgrade beyond threshold

#### Qualitative Indicators
- Borrower placed on watchlist
- Covenant breach
- Adverse change in business/employment
- Industry/geographic stress

---

## ECL Calculation Framework

### Core Formula

```
ECL = PD × LGD × EAD × Discount Factor

Where:
├── PD  = Probability of Default (Point-in-Time, adjusted for macro)
├── LGD = Loss Given Default (Downturn-adjusted)
├── EAD = Exposure at Default (Including undrawn commitments)
└── DF  = Discount Factor (Effective Interest Rate)

For Stage 1: 12-month ECL = Σ(Monthly PD × LGD × EAD × DF) for months 1-12
For Stage 2/3: Lifetime ECL = Σ(Monthly PD × LGD × EAD × DF) for remaining life
```

### PD Model Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PD MODEL ARCHITECTURE                             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  THROUGH-THE-CYCLE (TTC) PD                                         │
│  ├── Long-run average default rate                                  │
│  ├── Segment-specific                                               │
│  └── Based on historical performance                                │
│           │                                                          │
│           ▼                                                          │
│  POINT-IN-TIME (PIT) ADJUSTMENT                                     │
│  ├── Business cycle adjustment                                      │
│  ├── Macroeconomic variables (GDP, unemployment, rates)            │
│  └── Z-score or similar transformation                             │
│           │                                                          │
│           ▼                                                          │
│  FORWARD-LOOKING ADJUSTMENT                                         │
│  ├── Probability-weighted scenarios (Base, Up, Down)               │
│  ├── Macroeconomic forecasts                                       │
│  └── Expert judgment overlay                                       │
│           │                                                          │
│           ▼                                                          │
│  LIFETIME PD CURVE                                                  │
│  ├── Term structure of default                                     │
│  ├── Marginal PD by period                                         │
│  └── Cumulative PD to maturity                                     │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### LGD Components

| Component | Description | Typical Range |
|-----------|-------------|---------------|
| **Cure Rate** | Probability of returning to performing | 10-40% |
| **Recovery Rate** | % recovered from defaulted exposure | Segment-specific |
| **Collateral Haircut** | Discount on collateral value | 20-40% |
| **Time to Recovery** | Months to realize recovery | 12-36 months |
| **Direct Costs** | Legal, collection, admin costs | 5-15% |
| **Discount Rate** | EIR for NPV calculation | Contract rate |

```
LGD = 1 - Cure Rate - (1 - Cure Rate) × Recovery Rate × PV Factor

Downturn LGD = LGD × Downturn Adjustment Factor (typically 1.2-1.5x)
```

### EAD for Off-Balance Sheet

```
EAD = Drawn Amount + CCF × Undrawn Amount

Credit Conversion Factor (CCF):
├── Committed Facilities: 75-100%
├── Uncommitted Facilities: 20-50%
├── Trade Finance: 20-50%
└── Guarantees/LCs: 50-100%
```

---

## Scenario Analysis

### Multiple Economic Scenarios

| Scenario | Probability Weight | GDP Growth | Unemployment | Property Prices |
|----------|-------------------|------------|--------------|-----------------|
| **Upside** | 20% | +3.5% | 4.0% | +8% |
| **Base** | 50% | +2.0% | 5.5% | +3% |
| **Downside** | 25% | -0.5% | 7.5% | -5% |
| **Severe** | 5% | -3.0% | 10.0% | -15% |

### Probability-Weighted ECL

```
Final ECL = Σ (Scenario Weight × Scenario ECL)

Example:
ECL_weighted = 0.20×ECL_up + 0.50×ECL_base + 0.25×ECL_down + 0.05×ECL_severe
```

---

## IFRS9 Engine Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────────────┐
│                    IFRS9 ECL ENGINE                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────┐     ┌─────────────────┐                        │
│  │   DATA LAYER    │     │  MODEL LAYER    │                        │
│  ├─────────────────┤     ├─────────────────┤                        │
│  │ • Account Data  │     │ • PD Models     │                        │
│  │ • Customer Data │────▶│ • LGD Models    │                        │
│  │ • Collateral    │     │ • EAD Models    │                        │
│  │ • Macro Data    │     │ • Staging Rules │                        │
│  └─────────────────┘     └────────┬────────┘                        │
│                                   │                                  │
│                                   ▼                                  │
│                    ┌─────────────────────────┐                       │
│                    │   CALCULATION ENGINE    │                       │
│                    ├─────────────────────────┤                       │
│                    │ • Stage Assignment      │                       │
│                    │ • ECL Calculation       │                       │
│                    │ • Scenario Weighting    │                       │
│                    │ • Aggregation           │                       │
│                    └────────────┬────────────┘                       │
│                                 │                                    │
│           ┌─────────────────────┼─────────────────────┐             │
│           ▼                     ▼                     ▼             │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐         │
│  │  REPORTING  │      │  GL POSTING │      │   AUDIT     │         │
│  │  Dashboards │      │  Journals   │      │   Trail     │         │
│  └─────────────┘      └─────────────┘      └─────────────┘         │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Data Requirements

| Data Category | Key Fields | Source |
|---------------|------------|--------|
| **Account** | Account ID, Product, Balance, Rate, Tenure | Core Banking |
| **Customer** | Customer ID, Segment, Rating, Industry | CRM/Core Banking |
| **Performance** | DPD, Payment History, Default Flag | Core Banking |
| **Collateral** | Type, Value, LTV, Valuation Date | Collateral System |
| **Macro** | GDP, Unemployment, Interest Rates, Property Index | External/Economics |

---

## Implementation Roadmap

### Typical Timeline (Large Bank)

| Phase | Duration | Key Activities |
|-------|----------|----------------|
| **Assessment** | 2-3 months | Gap analysis, requirements, vendor selection |
| **Design** | 3-4 months | Model specification, architecture design, data mapping |
| **Build** | 6-8 months | Model development, engine configuration, integration |
| **Test** | 2-3 months | Model validation, UAT, parallel run |
| **Deploy** | 1-2 months | Go-live, hypercare, knowledge transfer |

### Common Challenges

1. **Data Quality**: Historical default data, collateral values, macro linkages
2. **Model Complexity**: Lifetime PD curves, scenario calibration
3. **Performance**: Calculation speed for large portfolios
4. **Governance**: Model validation, audit trail, documentation
5. **Integration**: Core banking, GL, reporting systems
