# Reference 02 — Thai OneWorld Topology Patterns

Version: V01R01 | Date: 2026.05.23

## When OneWorld is the right answer

NetSuite OneWorld is justified when at least one of these conditions holds:

1. Multiple legal entities in scope, regardless of geography.
2. Single entity today but expansion plan to multi-entity within 24-36 months.
3. Multi-currency reporting requirements (THB primary + USD or other parent currency for consolidation).
4. Inter-company elimination is non-trivial.

For single-entity Thai SMEs with no expansion plan and no multi-currency need, standard NetSuite (non-OneWorld) is the right answer. Recommending OneWorld in that scenario inflates cost without adding value, and erodes trust.

## Topology patterns

### Pattern A — Single Thai entity (non-OneWorld)

```
[Thai BizCo Ltd]
   Currency: THB
   COA: TFRS-aligned
   Tax: VAT registered, WHT compliant
```

Use when: One Thai legal entity, no plans for multi-entity, no consolidation need beyond Thai statutory.

### Pattern B — Thai parent with Thai subsidiary (OneWorld)

```
[Thai HoldCo]
   ├── [Thai OpCo 1]  (BOI-promoted, separate subsidiary per Section 1.5 choice 1)
   └── [Thai OpCo 2]  (non-promoted)
```

Use when: Holding company structure for legal or tax efficiency reasons, with BOI separation strategy choosing dedicated subsidiaries.

### Pattern C — Regional parent with Thai subsidiary (OneWorld)

```
[APAC RegionalCo]   (consolidation, regional reporting in USD)
   ├── [Thai SubCo]      (THB primary)
   ├── [SG SubCo]        (SGD primary)
   └── [VN SubCo]        (VND primary)
```

Use when: Multinational with regional consolidation. Thai entity is one of several APAC subsidiaries.

### Pattern D — Global parent through regional shell

```
[Global ParentCo]              (USD or home currency)
   └── [APAC ShellCo]          (USD)
         ├── [Thai SubCo]      (THB)
         ├── [Mfg SubCo Thai]  (THB, BOI-promoted)
         └── [Other APAC subs]
```

Use when: Listed parent or PE-backed group with regional treasury, multiple Thai entities including BOI-promoted manufacturing.

## Configuration template per Thai subsidiary

For every Thai subsidiary in OneWorld, lock these at setup:

```
Subsidiary Name:           [Thai legal name + English transliteration]
Country:                   Thailand
Currency:                  THB
Tax Nexus:                 Thailand
Tax Registration Number:   [เลขประจำตัวผู้เสียภาษี — 13 digits]
Branch Code:               [if multiple branches for VAT filing]
Fiscal Year:               [most common: Jan-Dec; confirm with customer]
Reporting Currency:        [matches parent for consolidation]
Address Format:            Thai
Language:                  Thai + English (if bilingual outputs required)
```

## Chart of Accounts approach

Two common patterns:

### Pattern 1 — Customer's existing COA migrated

Most Thai customers have a numeric-coded COA inherited from their previous system (often something like 1XXXX for assets, 2XXXX for liabilities, 4XXXX for revenue, 5XXXX for COGS, 6XXXX for opex). They will resist forcing onto NetSuite's default segment structure.

Recommended approach:

- Migrate their existing account numbers as the primary identifier.
- Map to NetSuite's standard account types (Bank, AR, AP, etc.) for system behavior.
- Add account hierarchy that matches TFRS disclosure groups for statutory reporting.

### Pattern 2 — Greenfield TFRS-aligned COA

For new entities or customers willing to redesign, use a TFRS-aligned hierarchical structure. Cleaner, but requires more change management.

## Multi-book accounting decision

Multi-book is worth turning on for Thai entities if any of these apply:

- BOI separation strategy is "multi-book" (Section 1.5 choice 3).
- Group consolidation under IFRS while Thai statutory uses TFRS for NPAEs.
- US-listed parent requiring US GAAP secondary book alongside Thai statutory.

Multi-book adds licensing cost. Confirm the business case justifies it before turning it on.

## Inter-company

For Thai customers with regional or global structures, inter-company is rarely just a transfer pricing matter — it has VAT and WHT implications.

Design rules:

1. Inter-company services between Thai entities are subject to VAT and WHT.
2. Inter-company services from Thai entity to overseas entity may be VAT zero-rated under specific conditions — confirm with customer's tax advisor.
3. Transfer pricing documentation is a separate exercise; NetSuite holds the data but does not generate the TP file.

Configure inter-company workflows with explicit tax-code mapping per scenario. Do not assume.

## Common topology mistakes

Three mistakes that show up repeatedly on Thai engagements:

1. **Setting Thai subsidiary in USD because the regional team wanted "consistent reporting"** — breaks Thai statutory accounting. Always THB primary for any Thai-incorporated subsidiary.
2. **Skipping BOI separation strategy at design time** — discovered during UAT, when re-architecture is painful. Section 1.5 must be confirmed before SuiteSuccess kickoff.
3. **Underestimating Thai-language form requirements** — assuming English-language documents are acceptable. Suppliers, customers, and auditors will request Thai versions; budget the PDF template work upfront.
