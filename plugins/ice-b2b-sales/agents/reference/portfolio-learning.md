# Compass.Next — Portfolio Learning Reference (Job 7)

> **Loaded by:** iCE-Compass.Next (progressive disclosure — โหลดตอน Portfolio Mode)
> **Skill:** portfolio-intelligence | **Absorbs:** portfolio-intelligence-agent learning loop

---

## Portfolio Mode — Cross-Deal Learning

```
READ-scope: /Customer/** (all opp + profiles + activity)
WRITE-scope: /Portfolio-Insights/** only

/Portfolio-Insights/ structure:
  pattern-library/        — successful-proposals · effective-discovery-questions · winning-objection-responses
  anti-pattern-library/   — lost-deal-analysis
  benchmark/
  skill-tuning-suggestions/ — pending-reviews · approved · rejected
  vertical-reference-knowledge/ — BFSI/Manufacturing/Public-Sector-TH/Energy/Retail/... (×11)
```

## Learning Loop Triggers
```
Win event       → สกัด win pattern (3+ similar wins → pattern) → pattern-library
Loss event      → สกัด anti-pattern (2+ losses → anti-pattern) → anti-pattern-library
Phase transition → benchmark update
MEDDPICC drop   → flag + analysis
```

## Cross-Deal Intelligence (ตอบ Compass/Kim/③)
```
"deal นี้คล้าย deal ไหน" → search Customer/ profiles + pattern-library
"solution ที่เคยเสนอ BFSI" → vertical-reference-knowledge/BFSI + final proposals (latest-only)
"objection ที่เคยชนะ" → pattern-library/winning-objection-responses
```

## Skill-Tuning Feedback → Sub-agents
```
Portfolio mode พบ pattern ว่า skill ไหนควรปรับ → เขียน skill-tuning-suggestions/pending-reviews
→ User approve → feedback ไป sub-agent ปรับ skill (เช่น b2b-* skill, product skill)
```

## Scheduled Refresh (product knowledge staleness)
```
STALENESS: Oracle ERP Cloud=90d · NetSuite=180d · EBS=365d · SAP/MS=90d
Compass trigger Solution-Knowledge refresh: Quarterly / ก่อน opp ใหม่ / User สั่ง
→ ③ retrieve latest → diff → write skill → bump version
```

## Latest-Only KB Policy
```
WORKING AREA (Zone 2): ทุก version · old → 99-Archive
KNOWLEDGE AREA (Customer/ + Portfolio-Insights/): FINAL เท่านั้นต่อประเภท (cross-deal ค้นเจอ final ไม่ใช่ draft)
```

---

*reference/portfolio-learning.md | Compass.Next Job 7 | absorbs portfolio-intelligence*
