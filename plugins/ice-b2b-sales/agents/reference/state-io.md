# Compass.Next — State & IO Reference (Job 6)

> **Loaded by:** iCE-Compass.Next (progressive disclosure — โหลดตอนทำ State+IO task)
> **Absorbs:** sales-admin-agent capabilities (ยุบเข้า Compass)

---

## 3-Zone Storage Policy

```
ZONE 1 — /Customer/{Code}/                        entity profile (permanent, cross-opp)
   customer-profile_V##R##.md (9 sections: Identity/Financial/Pain/PowerMap/TechStack/DesignPref/PastOpp)
ZONE 2 — /Projects/{Code}/{YY-Opp}/{NN-Stage}/    active working (00→99 stages)
   00-Customer-Profile · 10-RFP-Requirement · 20-Discovery · 30-Solution · 40-Estimation ·
   50-Proposal · 60-Negotiation · 70-Contract · 80-Handover · 90-PostSale · 99-Archive
ZONE 3 — /Customer/{Code}/{YY-Opp}/               closed snapshot (read-only, copy FINAL only)

Zone Transition: opp ปิด (Win/Loss/Q-Out) → copy FINAL ของแต่ละประเภท Zone2→Zone3 (latest-only, ไม่ copy ทุก version)
```

## Metadata Files (Compass เขียน/อ่าน)

```
_opportunity.json    — customer/opp/phase/stage/phase_history/stage_history
_active-session.json — active_customer/opportunity/folder/phase/process — + language_directive
_activity.log        — ทุก action (mode/dispatch/transition) full + เก็บตลอด
_registry.json       — customer + opportunity catalog
_status-ledger.json  — ⭐ ดู _infra/status-ledger-schema.json (ให้ Kim เห็นภาพรวม)
```

## Path Enforcement (Q25 — Block + Alert + Log)
```
ห้าม write นอก scope ของ active opportunity · violation → block + alert User + log
Zone 3 write-protected หลัง archive
```

## Document Save (Q11 — Confirm ทุกครั้ง)
```
Pre-Save Confirmation: ชื่อ [DocumentName]_V##R##_YYYY.MM.DD.ext → ที่ Zone 2 stage folder
V##R##: first=V01R01 · minor=R+1 · major=V+1 reset R · uncertain→ask User
หลัง save → update _status-ledger.json (artifacts_done) + _activity.log
```

## Win/Loss/Q-Out Auto-Actions
```
Win:  copy FINAL Zone2→Zone3 · update customer-profile (past opp) · trigger Portfolio learning (pattern)
Loss: copy Zone2→Zone3 · trigger Portfolio learning (anti-pattern)
Q-Out: archive · log reason
```

## Drive Dual-Write (ผ่าน gdrive MCP)
```
Local Zone 2 ↔ Drive /iCE-Sales/Project/{Code}/{YY-Opp}/ (mirror)
Customer profile → Drive /iCE-Sales/Customer/{Code}/
escalate_to_user เมื่อ MCP ทำไม่ได้ (delete/move/share) — never silent fallback
```

---

*reference/state-io.md | Compass.Next Job 6 | absorbs sales-admin*
