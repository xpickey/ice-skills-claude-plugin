# Reference: NPL/NPA Asset Management

## NPL/NPA Fundamentals

### Definitions

| Term | Definition | Typical Trigger |
|------|------------|-----------------|
| **NPL** (Non-Performing Loan) | Loan with payments overdue >90 days | DPD 90+ |
| **NPA** (Non-Performing Asset) | Broader term including NPLs + other assets | Varies by regulation |
| **DPD** (Days Past Due) | Days since missed payment | Payment date |
| **Write-Off** | Accounting removal from books | After exhausting recovery |
| **Technical Write-Off** | Accounting treatment, recovery continues | Policy-driven |

### NPL Lifecycle

```
PERFORMING → WATCHLIST → SUBSTANDARD → DOUBTFUL → LOSS
    │            │            │            │         │
    │         30 DPD       90 DPD      180 DPD   Write-off
    │            │            │            │         │
    ▼            ▼            ▼            ▼         ▼
 Standard    Enhanced     Active       Legal     Recovery/
Collection  Monitoring   Collection   Process    Write-off
```

---

## AMC Operating Model

### Organizational Structure

```
┌─────────────────────────────────────────────────────────────────────┐
│                    AMC ORGANIZATION                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│                        ┌─────────────┐                              │
│                        │     CEO     │                              │
│                        └──────┬──────┘                              │
│                               │                                      │
│    ┌──────────────┬──────────┼──────────┬──────────────┐           │
│    │              │          │          │              │           │
│    ▼              ▼          ▼          ▼              ▼           │
│ ┌──────┐    ┌──────────┐ ┌──────┐ ┌──────────┐  ┌──────────┐      │
│ │ Acq. │    │Collection│ │Legal │ │ Finance  │  │ Tech/Ops │      │
│ │ Team │    │  Team    │ │ Team │ │  Team    │  │  Team    │      │
│ └──────┘    └──────────┘ └──────┘ └──────────┘  └──────────┘      │
│                                                                      │
│  Portfolio    Soft/Hard    Litigation  Accounting   Systems         │
│  Valuation    Collection   Recovery    Reporting    Data Mgmt       │
│  Due Dilig.   Field Ops    Auction     Investor     Analytics       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### Core Processes

#### 1. Portfolio Acquisition
- **Sourcing**: Bank relationships, auctions, broker networks
- **Due Diligence**: Data room review, sampling, legal assessment
- **Valuation**: DCF modeling, comparable transactions, recovery curves
- **Bidding**: Pricing strategy, bid-ask negotiation
- **Transfer**: Legal documentation, data migration, customer notification

#### 2. Portfolio Segmentation

| Segment | Criteria | Strategy |
|---------|----------|----------|
| **Self-Cure** | Recent delinquency, good prior history | Light touch, reminder |
| **Promise to Pay** | Willing but unable, temporary hardship | Restructuring, forbearance |
| **Can Pay Won't Pay** | Capacity exists, avoiding payment | Escalated collection |
| **Cannot Pay** | No capacity, severe hardship | Settlement, write-off |
| **Skip/Fraud** | Untraceable, suspected fraud | Skip tracing, legal |
| **Deceased/Bankrupt** | Legal status change | Estate claim, legal process |

#### 3. Collection Strategies

**Soft Collection (0-90 DPD)**
- Automated reminders (SMS, Email, IVR)
- Call center outreach
- Payment plan offers
- Digital self-service

**Hard Collection (90-180 DPD)**
- Field visits
- Demand letters
- Negotiated settlements
- Skip tracing

**Legal Collection (180+ DPD)**
- Legal notice issuance
- Court proceedings
- Asset seizure/auction
- Bankruptcy claims

---

## Valuation Methodologies

### Gross Book Value (GBV) vs. Expected Recovery

```
Portfolio Valuation Components:

GBV (Gross Book Value)
├── Principal Outstanding
├── Accrued Interest
├── Fees and Charges
└── Legal Costs

Expected Recovery Value (ERV) = GBV × Recovery Rate

Recovery Rate = f(Collateral, Vintage, DPD, Segment, Jurisdiction)

Purchase Price = ERV × Discount Factor

Typical Pricing (% of GBV):
├── Secured (Property): 30-60%
├── Secured (Auto): 20-40%
├── Unsecured Consumer: 5-15%
├── Unsecured SME: 3-10%
└── Credit Card: 2-8%
```

### Recovery Curve Modeling

```python
# Illustrative Recovery Curve Model

def recovery_curve(months, segment):
    """
    Monthly cumulative recovery projection
    
    Parameters:
    - months: projection period
    - segment: loan segment
    
    Returns:
    - cumulative recovery %
    """
    
    # Segment-specific parameters
    params = {
        'secured_property': {'ultimate': 0.55, 'speed': 0.03},
        'secured_auto': {'ultimate': 0.35, 'speed': 0.08},
        'unsecured_consumer': {'ultimate': 0.12, 'speed': 0.15},
        'unsecured_sme': {'ultimate': 0.08, 'speed': 0.10}
    }
    
    p = params[segment]
    # Asymptotic recovery curve
    recovery = p['ultimate'] * (1 - np.exp(-p['speed'] * months))
    
    return recovery
```

---

## Technology Stack

### Collection Management System Components

| Module | Function |
|--------|----------|
| **Case Management** | Account allocation, workflow, task management |
| **Contact Management** | Multi-channel communication, history tracking |
| **Strategy Engine** | Segmentation, treatment path assignment |
| **Payment Processing** | Collection, settlement, allocation |
| **Field Operations** | Mobile app, GPS tracking, visit scheduling |
| **Legal Management** | Case tracking, document generation, hearing dates |
| **Analytics & Reporting** | Performance dashboards, collector scorecards |

### Key Integrations

```
┌─────────────────────────────────────────────────────────────────────┐
│               COLLECTION SYSTEM INTEGRATIONS                         │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  INBOUND                              OUTBOUND                       │
│  ────────                             ────────                       │
│  • Core Banking (Account Data)        • Payment Gateway              │
│  • Bureau (Credit Updates)            • SMS/Email Gateway            │
│  • KYC Systems (Customer Info)        • Dialer Integration           │
│  • Document Repository                • Legal Case Systems           │
│  • Valuation Systems                  • Accounting System            │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Performance Metrics

### Operational KPIs

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| **Collection Rate** | Collections / Target | >85% |
| **Recovery Rate** | Recovered / GBV | Segment-specific |
| **Roll Rate** | Accounts moving to worse bucket | <20% |
| **Promise to Pay Kept** | PTP Kept / PTP Made | >60% |
| **Right Party Contact** | RPC / Total Calls | >40% |
| **Cost per Dollar Collected** | Opex / Collections | <$0.10 |

### Portfolio Health Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Resolution Rate** | Resolved Accounts / Total | >30% annually |
| **Average Days to Resolution** | Avg time to close | <18 months |
| **Settlement Rate** | Settlements / Resolutions | 40-60% |
| **Legal Recovery Rate** | Legal Recovery / Legal Cases | >25% |
