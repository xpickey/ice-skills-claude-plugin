# Example — AI & Custom Extension Ideation on Top of Enterprise ERP

A worked example of running DT/ST for the AI & Custom Extension pillar — extending an existing ERP (Oracle Fusion) with AI agents and low-code apps. Discipline: **ST fit for H2/H3 portfolio positioning → DT ideation for AI use cases → prototype → Why-Invest/Now/Us**.

## The Situation

**Client:** Thai retailer (฿5B revenue, 40 stores, omni-channel e-commerce) already live on Oracle Fusion Cloud ERP for 18 months. Core is stable. The CDO wants to move beyond "system of record" to "system of intelligence" — specifically, use Oracle AI Agents + APEX / VBCS extensions to unlock the data sitting in Fusion.
**Ask:** A 2-week use-case ideation engagement to produce a prioritized backlog of 5–8 AI / extension concepts with quick-win prototypes.

## Step 1 — Strategic Fit Gate (ST)

- **Where-to-Play fit:** yes — Thai retailer with Fusion already live is a land-and-expand ICP.
- **How-to-Win fit:** yes — we own the client's Fusion deployment and have APEX + VBCS accelerators.
- **Pricing envelope:** ฿4–8M for ideation + 2 prototype builds.
- **Horizon classification:** H2 for the ideation engagement; some concepts may be H3 (exploratory AI); others H1 (immediate extensions).

## Step 2 — Use-Case Ideation (combined with `ai-use-case-finder` skill)

We engage the `ai-use-case-finder` skill for initial feasibility and ROI estimates, and use this skill for the envisioning wrap.

### Pillar-specific ideation prompts
Applying `references/enterprise-sw-context.md` Pillar 5:

**5a. GenAI copilots on top of Fusion**
- HMW: how might we enable the merchandising team to ask natural-language questions about stock and sell-through without writing a BI report?
- Idea: Oracle Analytics Copilot + Fusion Finance data + natural-language Q&A

**5b. Agentic AI workflows**
- HMW: how might we auto-resolve invoice exceptions (supplier mismatches, quantity variance) so the AP team only touches the 5% that need judgment?
- Idea: Oracle AI Agent chaining — 3-way match → exception classification → proposed resolution → AP officer approve

**5c. Predictive analytics**
- HMW: how might we forecast stock-out 14 days ahead by SKU × store to trigger automatic replenishment?
- Idea: demand-sensing model on Fusion inventory data + weather / holiday signals

**5d. Document intelligence**
- HMW: how might we automate supplier invoice extraction from PDF + Line / WeChat attachments into Fusion AP?
- Idea: OCR pipeline + agent classification + Fusion AP posting

**5e. Conversational interfaces**
- HMW: how might we let store managers self-serve HR / roster / inventory queries via Line chatbot in Thai?
- Idea: Thai NLU + VBCS-layered chatbot + Fusion HCM + Inventory API

**5f. Anomaly detection**
- HMW: how might we detect unusual journal entries or expense claims in real time?
- Idea: ML anomaly model on Fusion GL transactions + threshold-tuned alerts

### Custom Extensions on PaaS

For each AI concept, map to the extension platform:
- Oracle Analytics Copilot (for 5a)
- Oracle AI Agents + Integration Cloud (for 5b)
- Oracle Analytics + Autonomous DB (for 5c)
- VBCS + APEX for UI; Oracle Document Understanding for extraction (for 5d)
- VBCS (web) + Line channel adapter + Thai NLU (for 5e)
- Oracle ML in Autonomous DB (for 5f)

## Step 3 — Convergence

Impact-effort matrix across all 6 concepts:

| Concept | Impact (1–5) | Effort (1–5) | Quadrant |
|---|---|---|---|
| 1. NL Q&A copilot | 4 | 2 | Quick Win |
| 2. AP agent chain | 5 | 3 | Quick Win / Big Bet |
| 3. Stock-out forecast | 5 | 4 | Big Bet |
| 4. Invoice OCR pipeline | 4 | 3 | Quick Win |
| 5. Thai store chatbot | 4 | 3 | Quick Win |
| 6. Anomaly detection | 3 | 4 | Watch list |

### Top 3 prioritized for prototype:
- Concept 1 — NL Q&A copilot (2-week build)
- Concept 2 — AP agent chain (4-week prototype)
- Concept 4 — Invoice OCR pipeline (3-week prototype)

## Step 4 — Prototyping (2 concepts built in weeks 2–3 of engagement)

### Prototype A — NL Q&A copilot
- Oracle Analytics Cloud with copilot against 6 months of sales / inventory data
- 10 question patterns tested with Merchandising Director
- Result: 7 of 10 queries answered correctly without follow-up; 2 needed schema clarification; 1 failed on fuzzy query

### Prototype B — AP agent chain
- Oracle AI Agents orchestrating 3-way match + exception classification
- Ran against 500 sample invoices from prior month
- Result: 78% auto-resolved (well above 50% threshold); 15% flagged correctly for human review; 7% false positive — tunable

## Step 5 — Strategic Fit Re-check (ST)

- Concepts fit H2 (imminent build) and one H3 (anomaly detection stays in pilot)
- Commercial envelope: ฿6M for ideation + prototypes; subsequent productionization ฿12–18M
- Capability: in-house APEX / VBCS team + Oracle AI specialists sufficient
- Go to proposal for productionization phase

## Step 6 — Why-Invest / Why-Now / Why-Us

### Narrative version

**Why Invest** — Your Fusion deployment has captured the system of record; now the prize is to turn that record into intelligence. Each of the top 3 concepts has measurable payoff: NL Q&A saves ~3 hours / merchandiser / week (฿4.8M annual); AP agents process 78% of invoices without human touch (฿12M annual labor savings + 5-day cycle reduction); OCR ends supplier invoice keying (฿6M annual). Total value: ฿22M/year. Without action, the Fusion investment stays "nice to have" rather than transformative; competitors are already running agentic workflows.

**Why Now** — Oracle AI Agents entered general availability in the last 6 months with significantly improved Thai-language support. Your FY27 capex budget cycle is now; waiting a year means deferring value realization by 12–18 months. Your competitor Central Group has already announced AI agent deployments — parity risk is real. Thai retail labor market is tight; AI augmentation de-risks the FY28 hiring plan.

**Why Us** — We delivered your Fusion platform and know the data model intimately. Our APEX + VBCS team includes two Oracle AI specialists who piloted the prototypes you validated in weeks 2–3 of this engagement. We own the accelerators we built for the prototypes and will include them in the productionization contract. We commit to a fixed-price ฿14M Phase 1 with 30% outcome pricing tied to 70% AP auto-resolution.

### Next action
*"We propose a Solution Design Confirmation session within 7 business days to finalize the Phase 1 productionization scope and sequence Concepts 1, 2, and 4 for delivery in FY27 H1."*

## Step 7 — Orchestration Delegations

- Oracle Fusion configuration depth → `oracle-cloud-applications-consulting`
- AI use-case feasibility + ROI → `ai-use-case-finder`
- Legal / data governance for AI → `legal-it-thailand-cloud`
- Sales pursuit → `b2b-enterprise-sale-strategy`

## Key Lessons

- **The AI layer is where the next 2–3 years of value sits** for clients who already own the ERP core.
- **Anchor AI ideation in the 6 pattern categories** (copilot / agentic / predictive / document / conversational / anomaly) rather than chasing buzzwords.
- **Prototype in days, not months** — Oracle AI Agents + APEX + VBCS make it possible.
- **Combine with `ai-use-case-finder`** for ROI discipline; this skill provides the DT/ST envelope.
- **Thai-language support in AI models** is the differentiator — global vendors often lag Thai context.
