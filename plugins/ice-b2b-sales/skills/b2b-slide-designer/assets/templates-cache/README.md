# Template Cache (local-only)

ไฟล์ .pptx ที่ทยอย copy มาเก็บตอนเรียกใช้ (cache-on-demand). **ไม่เข้า git** (.gitignore).

- **Portable metadata** = `../references/templates-cache-meta.json` (เข้า git — ย้ายเครื่องได้)
- **Resolution:** cache → src_path (ต้นทาง 800-Infographic) → fallback inspiration
- **เติม cache:** `python ../scripts/template_cache.py get "<framework>"`
- **health-check:** `python ../scripts/template_cache.py check`
