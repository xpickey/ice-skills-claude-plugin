# MCP Function Reference — Nano Banana

Complete catalog of Tools, Resources, and Prompt Templates.

## Tools (4)

### 1. `generate_image`

Generate new images or edit existing images. Auto-detects mode based on parameters.

**Parameters:**
| Parameter | Type | Default | Description |
|---|---|---|---|
| `prompt` | string | (required) | Image prompt — see Prompt Anatomy 6 ส่วน |
| `model_tier` | string | `auto` | `flash` / `nb2` / `pro` / `auto` |
| `aspect_ratio` | string | null | `1:1`, `4:3`, `3:4`, `16:9`, `9:16`, `21:9`, etc. |
| `resolution` | string | `high` | `high` / `4k` / `2k` / `1k` |
| `n` | int | 1 | จำนวนภาพที่ขอ (1-4) |
| `negative_prompt` | string | null | สิ่งที่ห้าม |
| `output_path` | string | null | Path ปลายทาง (ดู Output Path Rules) |
| `mode` | string | `auto` | `generate` / `edit` / `auto` |
| `input_image_path_1/2/3` | string | null | Path ภาพ Input สำหรับ Edit/Conditioning |
| `file_id` | string | null | Files API ID (จาก upload_file) |
| `enable_grounding` | bool | true | Google Search Grounding (NB2/Pro) |
| `thinking_level` | string | null | `low` / `high` (NB2/Pro) |
| `system_instruction` | string | null | Tone/Style guidance |
| `return_full_image` | bool | null | Return Full vs Thumbnail |

**Output Path Rules:**
- `output_path="/path/img.png"` → Save ตรง path
- `output_path="/path/folder/"` → Auto-name ในโฟลเดอร์
- `output_path=null` → ใช้ `IMAGE_OUTPUT_DIR` env
- **Multi-image (n>1):** เพิ่ม suffix `_2`, `_3` อัตโนมัติ

**Mode Auto-detection:**
- มี `input_image_path_*` หรือ `file_id` → mode=edit
- ไม่มี → mode=generate

**Examples:**
```python
# Basic Generate
generate_image(
    prompt="A red apple on white background, product photo",
    aspect_ratio="1:1",
    output_path="/path/apple.png"
)

# 4K Production
generate_image(
    prompt="Cinematic landscape...",
    model_tier="nb2",
    aspect_ratio="21:9",
    resolution="4k",
    enable_grounding=True
)

# Edit Mode
generate_image(
    prompt="Change background to ocean sunset",
    mode="edit",
    input_image_path_1="/path/original.png",
    output_path="/path/edited.png"
)

# Multi-image Conditioning (Pro)
generate_image(
    prompt="Combine the style of image 1 with the subject of image 2",
    model_tier="pro",
    input_image_path_1="/path/style.png",
    input_image_path_2="/path/subject.png"
)
```

---

### 2. `upload_file`

Upload large images (>20MB) or images for reuse via Gemini Files API.

**Parameters:**
| Parameter | Type | Description |
|---|---|---|
| `file_path` | string | Local path ของไฟล์ |
| `mime_type` | string | (optional) auto-detect ถ้าไม่ระบุ |
| `display_name` | string | (optional) ชื่อแสดงผล |

**Returns:** `file_id` (e.g., `files/abc123`) สำหรับใช้ใน `generate_image(file_id=...)`

**เมื่อใช้:**
- ภาพ Input > 20MB
- ต้อง Edit ภาพเดียวกันหลายรอบ (Cache ไว้)
- Multi-image Conditioning ที่ภาพใหญ่

---

### 3. `maintenance`

Cleanup operations for output directory and Files API.

**Operations:**
| Operation | Description |
|---|---|
| `cleanup_expired` | ลบ Files API entries ที่หมดอายุ |
| `cleanup_local` | ลบไฟล์เก่าใน Output Dir (LRU/age-based) |
| `check_quota` | ดู Files API Storage Usage (Budget ~20GB) |
| `database_hygiene` | แก้ DB Inconsistency |
| `full_cleanup` | รันทุก Operation ตามลำดับ |

**Parameters:**
- `dry_run` (default: true) — รายงานอย่างเดียวไม่ลบจริง
- `max_age_hours` — สำหรับ cleanup_local (default 168 = 1 week)
- `keep_count` — จำนวน Recent Files ที่จะเก็บ

**ความถี่แนะนำ:**
- ราย Week: `cleanup_local` + `cleanup_expired`
- ราย Month: `full_cleanup`
- เมื่อ Disk ใกล้เต็ม: `cleanup_local` + `keep_count=20`

---

### 4. `show_output_stats`

แสดงสถิติ Output Directory — ใช้เป็น **Pre-flight Probe**

**No Parameters**

**Returns:**
```json
{
  "output_directory": "/path/to/images",
  "total_images": 42,
  "total_size_bytes": 123456789,
  "total_size_mb": 117.7,
  "recent_images": [...]
}
```

**ใช้เมื่อ:**
- Pre-flight Check (ก่อน generate_image ทุกครั้ง)
- ตรวจ Disk Usage
- ดูภาพล่าสุดที่สร้างไว้

---

## Resources (7)

| URI | Returns |
|---|---|
| `gemini://files/{name}` | File metadata จาก Gemini Files API |
| `file://images` | รายการภาพทั้งหมด |
| `file://images/{id}` | Full image |
| `file://images/{id}/thumbnail` | Thumbnail |
| `nano-banana://prompt-templates` | Built-in templates catalog |
| `progress://operations/{id}` | Long-running operation status |
| `progress://operations/list` | All active operations |

---

## Built-in Prompt Templates (6)

ใช้ผ่าน Server's prompt registry (อาจไม่ต้องเรียกตรงๆ — Claude เลือกให้)

### Photography
**`photorealistic_shot`** — Subject + Lighting + Composition + Style → Photorealistic image

### Design
**`logo_text`** — Brand Name + Style (minimal/bold/playful) + Color → Logo with text rendering

**`product_shot`** — Product Name + Background + Lighting + Angle → E-commerce ready

**`sticker_flat`** — Subject + Color Palette + Style → Flat sticker with transparent background

### Editing
**`iterative_edit_instruction`** — Original Description + Change Request → Refined edit prompt

**`composition_and_style_transfer`** — Composition Source + Style Source + Target Description → Multi-image conditioning prompt

---

## Error Handling Quick Reference

| Error Pattern | Likely Scenario | Action |
|---|---|---|
| `RESOURCE_EXHAUSTED` / `429` | Quota / Billing | Scenario G — เปิด Billing |
| `unauthorized` / `401` | API Key ผิด | Scenario C — Update Key |
| `GEMINI_API_KEY not set` | ไม่มี Key | Scenario B |
| `Server failed to start` | uv/Path ผิด | Scenario D |
| `Tool not found` | MCP ไม่ Setup | Scenario A |
| Vertex AI / aiplatform error | ADC ผิด | Scenario E |
| `returned: 0` (no error) | Silent quota fail | ถือเป็น G |
