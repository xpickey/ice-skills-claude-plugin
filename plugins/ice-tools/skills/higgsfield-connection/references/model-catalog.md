# Higgsfield Model Catalog — 30+ models แยกตาม output type

> **เช็คจริงเสมอ:** model list เปลี่ยนได้ — ใช้ `models_explore(action='list'|'search', type='image'|'video'|'audio')` ดู catalog ปัจจุบัน + `action='get', model_id='...'` ดู constraint (aspect_ratio, duration, medias roles). ตารางด้านล่างเป็น default-pick guide ไม่ใช่รายการตายตัว.

> **Version-Agnostic Policy:** อย่า hardcode version number ใน logic — ค้นจาก family แล้ว pick latest ที่ MCP คืนมา. ตารางนี้บันทึก model_id ที่ verified ณ 2026-06 ไว้เป็น reference เท่านั้น. เมื่อ Higgsfield upgrade (เช่น veo3 → veo4) ให้ใช้ family search ไม่ต้อง update skill.

---

## Verified Models (2026-06) + Version-Agnostic Guide

### IMAGE models (verified via models_explore — 2026-06)

| Family | model_id ที่ verified | Use-case | หมายเหตุ |
|---|---|---|---|
| **GPT Image** | `gpt_image`, `gpt_image_2` | org/infographic/text/diagram | `gpt_image` = 1.5; `gpt_image_2` = higher res 1k/2k/4k |
| **Nano Banana** | `nano_banana_pro` | 4K, text, diagram, product, photoreal | text fidelity สูงสุด |
| **Recraft** | `recraft-v4-1` | logo, icon, vector graphic | model_type: standard/vector/utility — เลือก vector |
| **FLUX** | `flux_2` (variants: pro/flex/max) | concept art, illustration, high-detail | ใช้ `flux_2` + variant |
| **Flux Kontext** | `flux_kontext` | context-aware edit, style transfer, retouch | **substitute สำหรับ "Reve" ที่ไม่มีใน MCP** |
| **Auto** | `image_auto` | ให้ Higgsfield เลือก model ที่เหมาะจาก prompt | verified EXISTS — ใช้ได้เลย |
| Soul | `soul_2`, `soul_cinematic` | portrait/fashion/UGC, cinematic stills | stable — ไม่เปลี่ยนบ่อย |
| Marketing | `marketing_studio_image` | ad/product commercial | stable |
| MS Image (DTC) | `ms_image` | DTC ads | ต้องมี `style_id` |
| Soul Cast | `soul_cast` | character/avatar จาก text ล้วน | ไม่ต้อง ref image |

> ⚠️ **"Reve" ไม่มีใน MCP** (ณ 2026-06) — substitute = `flux_kontext` (context-aware edit ใกล้เคียงที่สุด). เมื่อผู้ใช้ขอ Reve → fuzzy suggest flux_kontext + ถามยืนยัน

### VIDEO models (verified via models_explore — 2026-06)

| Family | model_id ที่ verified | Use-case | หมายเหตุ |
|---|---|---|---|
| **Veo** | `veo3`, `veo3_1`, `veo3_1_lite` | storytelling, long-form, complex scenes | `veo3_1` = newer; pick latest via search |
| **Kling 2.x** | `kling2_6` | character consistency, cinematic motion | search `kling2` → pick latest 2.x |
| **Kling 3** | `kling3_0` | multi-shot, audio sync | search `kling3` → pick latest |
| Higgsfield cinematic | `cinematic_studio_video_v2`, `cinematic_studio_3_0` | cinematic quality | |
| Marketing Studio Video | `marketing_studio_video` | TikTok/Reels/DTC | stable |
| Seedance | `seedance_2_0` | identity/face-consistency | stable |
| Higgsfield preset | `higgsfield_preset` | ใช้ preset | ต้องมี `preset_id` จาก `presets_show` |
| Grok Video | `grok_video` | text+image-to-video | |

---

## IMAGE models

| Model | เหมาะกับ | หมายเหตุ |
|---|---|---|
| `marketing_studio_image` | commercial / product / ad / DTC | optimized ad — default งานขาย |
| `soul_2` | portrait / fashion / UGC / editorial / photoreal | default character/people |
| `soul_2` + `soul_id` | **character คงหน้า reusable** | ต้อง train Soul ID ก่อน (5-20 รูป, ~10 นาที) |
| `soul_cast` | character/avatar จาก text ล้วน | ไม่ต้อง ref image |
| `nano_banana_pro` | 4K / text ในภาพ / diagram / one-off char ref | text fidelity สูงสุด |

## VIDEO models

| Model | เหมาะกับ |
|---|---|
| `marketing_studio_video` | ads / product video — default งานขาย |
| `seedance_2_0` | identity (คงหน้าในวิดีโอ) · audio ผ่าน medias |
| `kling3_0` | multi-shot / audio / motion transfer |
| `veo` (3.1) / อื่น ๆ | ดู `models_explore(type='video')` |
| `higgsfield_preset` | ใช้ preset (ต้องมี `preset_id` จาก `presets_show`) |

roles ของ video medias: `start_image` / `end_image` / `image` (ตาม model)

## AUDIO models

| Model | เหมาะกับ | param พิเศษ |
|---|---|---|
| `sonilo_music` | เพลง/ดนตรี | ต้องมี `duration` |
| `mirelo_text_to_audio` | sound effect | ต้องมี `duration` |
| `inworld_text_to_speech` | voiceover / พูด | ต้องมี `voice` · **ไม่ต้อง** duration |

audio = single-sample (`count: 1`)

## เลือก model — decision flow

```
ภาพ?
  ├─ ad/product/ขาย → marketing_studio_image
  ├─ คน/portrait → soul_2 (คงหน้า reusable? → +soul_id, train ก่อน)
  ├─ text-only char → soul_cast
  └─ 4K/text/diagram → nano_banana_pro
วิดีโอ?
  ├─ ad/product → marketing_studio_video
  ├─ คงหน้า → seedance_2_0
  └─ multi-shot/motion/audio → kling3_0
เสียง?
  ├─ เพลง → sonilo_music (+duration)
  ├─ SFX → mirelo_text_to_audio (+duration)
  └─ พูด → inworld_text_to_speech (+voice)
ไม่ชัด → models_explore(action='recommend', query='<งาน>', type='<image|video|audio>')
```

## Constraint checklist (ก่อนสั่ง)
- aspect_ratio — เช็ค model รองรับค่าไหน (`models_explore get`)
- duration (video/audio) — เช็ค range; ไม่ใส่ = default
- medias roles — แต่ละ model ต้องการ role ต่างกัน
- count — image/video 1-4 · audio = 1
- ราคาต่าง model ต่างมาก — video/marketing แพงสุด → `get_cost: true` ก่อน
