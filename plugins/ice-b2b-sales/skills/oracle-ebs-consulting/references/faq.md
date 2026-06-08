## PART 13: Frequently Asked Questions (FAQ)

### General Implementation

**Q: How long does a typical EBS implementation take?**
A: Varies widely based on scope. Single-module (e.g., GL only): 3-6 months. Full Financials (GL, AP, AR, FA, CM): 6-9 months. Financials + Procurement + SCM: 12-18 months. Financials + Procurement + SCM + Manufacturing + HRMS: 18-24 months. Add 20-30% for global rollouts and 50%+ for heavily customized implementations.

**Q: Cloud vs. On-Premise EBS?**
A: Oracle EBS is primarily on-premise, though it can be hosted on cloud infrastructure (IaaS). Oracle Fusion Cloud Applications is the cloud-native SaaS offering. EBS offers deeper functionality, more customization, and is proven in complex environments. Fusion offers modern UX, automatic updates, and lower IT overhead. Many customers maintain EBS for core operations while adopting Fusion for newer business units or regions.

**Q: Upgrade vs. Reimplementation?**
A: If current implementation is relatively clean with moderate customizations, upgrade is typically faster and less risky. If legacy implementation has significant technical debt, heavy customizations, or poor data quality, consider reimplementation to start fresh with best practices. Hybrid approach: Upgrade technical platform but reimplementl key modules.

### Technical Questions

**Q: How to handle customizations during upgrade?**
A: Document all customizations (Forms, Reports, Workflows, APIs, OAF). Assess if still needed or if standard R12 functionality can replace them. For retained customizations: Recompile forms, regenerate reports, retest OAF extensions, migrate workflow definitions. Use ADOP for online patching in R12.2 to minimize downtime.

**Q: Best practice for concurrent manager configuration?**
A: Start with Standard Manager (all-purpose). Add specialized managers for high-volume processes (Inventory Manager for lot of item imports, Receiving Manager for high receipt volume). Configure Work Shifts to ensure 24x7 processing. Set up conflict domains to prevent incompatible programs from running concurrently. Monitor queue depth and processing times, add managers/processes as needed.

**Q: How to optimize EBS performance?**
A: Database level: Gather stats regularly, partition large tables (GL_BALANCES, GL_JE_LINES), index optimization, SQL tuning. Application level: Concurrent manager tuning, forms cache settings, workflow purge, archive old data. Infrastructure: Load balancing, network optimization, adequate hardware (CPU, RAM, disk I/O).

### Functional Questions

**Q: How to handle inter-company transactions?**
A: Set up Intercompany segment in Chart of Accounts. Configure intercompany rules in GL (auto-generate balancing entries). In AP: Intercompany invoices post to intercompany AP. In AR: Intercompany invoices post to intercompany AR. At consolidation: Eliminate intercompany balances (IC AP vs. IC AR, IC Revenue vs. IC Expense, IC Profit in Inventory).

**Q: Multi-currency best practices?**
A: Use consistent functional currency across related entities (e.g., all Thailand OUs use THB). Define reporting currency at ledger level (typically group currency like USD). Set up daily rates for common currency pairs (USD/THB, EUR/THB). Use Corporate rate type for standard transactions, Historical for equity translations. Run revaluation monthly to capture unrealized FX gains/losses.

**Q: How to achieve fast period close?**
A: Pre-close activities: Reconcile subledgers to GL before period-end. Automate recurring entries. Use close checklist with dependencies. Day 1: Run depreciation, process payroll, accrue revenue. Day 2: Subledger transfers (AP, AR, FA), post to GL. Day 3: Review variances, make adjustments, final review. Day 4: Management reports, board pack. Day 5: Lock period. Target 5 business days for soft close, 10 days for hard close.

### Integration Questions

**Q: How to integrate EBS with non-Oracle systems?**
A: Options: (1) File-based: Export from source system, import to EBS via open interface. (2) API-based: Call EBS APIs (PL/SQL packages) from external system. (3) Web Services: Expose EBS as web service, external system calls via SOAP/REST. (4) Middleware: Use Oracle SOA Suite or OIC to orchestrate complex integrations with transformations, error handling, monitoring.

**Q: Real-time vs. batch integration?**
A: Real-time: For critical, time-sensitive data (customer orders, inventory availability, pricing). Use web services or API calls. Batch: For high-volume, less time-sensitive data (GL journals, invoice imports, daily sales). Run during off-peak hours (nights, weekends). Hybrid: Real-time for user-facing, batch for back-office.

---
