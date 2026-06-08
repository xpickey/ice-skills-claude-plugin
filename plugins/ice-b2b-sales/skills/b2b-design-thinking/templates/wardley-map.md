# Wardley Map Template

Simon Wardley's mapping technique: a value chain plotted against component evolution (Genesis → Custom → Product → Commodity). Unique among strategy tools in that it is literally a map — it shows *where* you are and *where to move*.

## The Two Axes

### Vertical axis — Value Chain (visibility to the user)
- Top: user need
- Next: user-facing activities
- Middle: supporting systems
- Bottom: commodities / infrastructure

### Horizontal axis — Evolution
- **Genesis** — novel, uncertain, high cost, rare
- **Custom-built** — bespoke, some understanding, still uncertain
- **Product / rental** — well-defined, buyable, feature competition
- **Commodity / utility** — standardized, cheap, widespread

```
     User need
       |
  visible         [user activity]
       |
       |              [app layer]
       |
       |                   [platform]
       |
       |                       [infra / commodity]
  invisible  ────────────────────────────────────→
           Genesis  Custom  Product  Commodity
```

## Why This Matters for Enterprise Software

Wardley mapping forces a sharp question most strategy tools avoid: **which of our components are stuck in the wrong evolutionary stage?**

- A custom-built ERP in a world of Cloud ERP commodity is a Money Pit
- A commodity integration where a product exists is a waste
- A Genesis AI use case running on commodity infra may be under-invested

## Step-by-Step

### 1. Anchor the map on user need
What does the customer actually care about? Examples:
- "Close the books by day 5"
- "Match invoices without manual effort"
- "Serve citizens faster without queuing"

### 2. Chain the components
Decompose the value chain from user need downward to commodity infrastructure.

### 3. Plot evolution
Place each component on the evolution axis. Use characteristics (uncertainty, repeatability, availability) to score.

### 4. Look for movement
Components evolve left-to-right over time. Ask:
- What is moving right (becoming commoditized)?
- What is stuck too far left (still custom when it should be product)?
- Where is the next pool of value? (Often one stage right of today's commodity)

### 5. Pick moves
Three classic moves:
- **Invest in Genesis** — capture new capability early
- **Build a product** in a Custom stage component to create a new market
- **Consume commodity** — stop building what is now buyable

## Example — Thai Mid-Market ERP Value Chain (2026)

```
     Close books by day 5                      (user need)
            |
     Journal entry, recon     [Custom → Product]
            |
     Subledger, AP / AR       [Product]
            |
     ERP core (Fusion / S/4)  [Product → becoming Commodity for cloud]
            |
     Database                 [Commodity (Autonomous DB / HANA Cloud)]
            |
     Compute / storage        [Commodity]
```

Moves implied:
- **Stop custom-coding** in core ERP — adopt clean-core principle
- **Invest Genesis** in AI exception handling and agentic workflows
- **Buy commodity** for infra; not a differentiator anymore

## Common Pitfalls

- **Misplacing evolution** — most under-estimate how far right cloud / commodity has moved
- **No movement arrows** — a static map is less useful than one showing direction
- **Confusing innovation with Genesis** — many "AI" ideas are actually Custom or Product
- **Ignoring inertia** — customers have organizational inertia that slows the right-ward pull

## Workshop Run (2 hours)

1. Define user need (15 min)
2. Chain components (30 min)
3. Plot evolution (30 min)
4. Identify misplacements and movements (30 min)
5. Name strategic moves (15 min)

## Quality Bar

- Map anchored on a specific user need
- Chain is complete (nothing missing that the user needs)
- Each component is placed deliberately, not guessed
- At least one misplacement identified
- At least 2–3 strategic moves named with rationale
