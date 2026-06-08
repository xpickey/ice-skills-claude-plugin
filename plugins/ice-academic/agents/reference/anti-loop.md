# Compass.Next — Anti-Loop Contract Reference (§15)

> **Loaded by:** iCE-Compass.Next + ทุก in-path agent (เป็น contract ร่วม)
> **Design ref:** iCE-B2B-Compass.Next_V01R02 §11

---

## Why fleet ใหม่ loop ยากเกิด
```
43 agents: 5 layers · 33+ nodes · call graph ลึก → loop เสี่ยงสูง
6 agents:  2 layers · 6 nodes (NO leaf) · depth ~2 → loop เสี่ยงต่ำมาก + 5 กลไก
```

## กลไก 1 — Tree-Enforcing Call Graph
```
1. CALL-CHAIN BREADCRUMB: Pack มี call_chain · agent append ตัวเองก่อนเรียก child
   → id ตัวเองอยู่ใน chain แล้ว? → REFUSE (return status→blocked, reason "cycle")
2. NO-BACK-CALL: child ห้ามเรียก ancestor ใน chain
3. SIBLING-THROUGH-PARENT: ②③④⑤ ต้องการ sibling → ผ่าน L1 (Compass/Kim) → serialise
   → ไม่มี peer cycle (②→③→② เป็นไปไม่ได้)
4. DEPTH CAP ≤ 3: L1→L2 = depth 2 ปกติ · cap=3 เผื่อ ③ retrieve sub-call · เกิน → refuse
→ tree ไม่มี cycle ตามนิยาม → infinite loop เป็นไปไม่ได้เชิงโครงสร้าง
```

## กลไก 2 — Two-Tier Briefing Pack (กัน context decay)
```
CORE PACK (immutable verbatim): customer/product/primary_product/primary_industry/phase/
  language_directive/wording_discipline/brand_locks/core_pack_locked/call_chain/call_depth
  → child ห้ามแก้/ลบ (additive-only)
SECTION PACK (prunable+checksum): key_facts/build_safe_rules/section_spec/comparison_scope/requirement_source
  → parent prune ได้ แต่บันทึก facts_forwarded
REFERENCE PATHS: escape hatch (อ่านเฉพาะถ้า embedded ไม่พอ)
```

## กลไก 3 — Unified Return Envelope (กัน guess-instead-of-ask)
```
status (native→loop state) · work · questions · self_assessment{confidence,gaps} · sub_results · needs_followup
FALLBACK: no recognizable status ⇒ ready
CONFIDENCE GATE: ready BUT confidence:low → Compass ไม่ accept (re-command/ask)
NEVER-GUESS: brand/number/date/regulatory ไม่มีใน Pack → needs_input (H1-H4)
```

## กลไก 4 — Loop Guards
```
max_clarify_rounds=3 · max_review_rounds=2 · max_qa_rebuilds=2 ·
inline_build_tripwire (Compass เขียน build > couple steps → STOP dispatch④) ·
call_depth cap=3 · cycle guard · build-vs-edit guard
```

## กลไก 5 — Hard Delegation Rule
```
COMPASS=COMMANDER: NEW deliverable/>5 slides → MUST dispatch④ (ห้าม build inline)
INLINE only: ≤5 slides edit บน valid base ผ่าน python-pptx API
EXIT RAMP: Compass เริ่ม build + bug > couple steps → STOP, hand④
```

## Multi-Agent Discuss (star = tree, ไม่ loop)
```
R1 parallel-only · R2 independent (call_chain แยก) · R3 Compass-only synthesis · R4 max_discuss_rounds=2
3-Lens: Product→③ · Commercial→② · Risk→⑤ → Compass สังเคราะห์คนเดียว
```

## 2 L1 (Compass + Kim) — ยังเป็น tree
```
2 roots peer — ไม่ recursion (Kim ขอ Compass = provide ครั้งเดียว)
Kim→Compass→Kim → cycle guard บล็อก (ปกติไม่เกิด: Compass ไม่ขอ Kim)
```

## 3 Structural Failures ที่แก้
```
A. Context decay → กลไก 2 (Core Pack immutable + checksum)
B. Guess-instead-of-ask → กลไก 3 (confidence gate + never-guess)
C. Agents looping A→B→A → กลไก 1 (tree-enforcing) + กลไก 4 (depth/cycle guard)
```

---

*reference/anti-loop.md | Compass.Next §15 | honored by all in-path agents*
