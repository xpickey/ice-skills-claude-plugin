# Marketing Studio — DTC Ads Workflow

> Tool prefix เป็น **UUID** (เช่น `mcp__6473a427-...__show_marketing_studio`). prefix ต่างตาม session/install — เช็ค session จริง แล้วใช้ tool ตามชื่อหลัง prefix. ด้านล่างใช้ชื่อ tool (ไม่รวม prefix).

Marketing Studio คือ workflow สำหรับสร้าง **DTC / Product Ads** แบบ asset-driven: สร้าง "ad reference asset" (product / webproduct / brand_kit / avatar) ก่อน แล้วต่อด้วย preset + hook + setting ไปจบที่ `generate_video(model='marketing_studio_video')`. tool หลักคือ `show_marketing_studio`.

## Table of Contents
- [ภาพรวม show_marketing_studio](#ภาพรวม-show_marketing_studio)
- [1. Product vs Webproduct](#1-product-vs-webproduct)
- [2. Fetch flow (ดึงจาก URL)](#2-fetch-flow-ดึงจาก-url)
- [3. Manual create (จากรูป)](#3-manual-create-จากรูป)
- [4. Brand Kit (scrap_url)](#4-brand-kit-scrap_url)
- [5. Presets / Hooks / Settings](#5-presets--hooks--settings)
- [6. Soul ID character ใน ad](#6-soul-id-character-ใน-ad)
- [7. Full example — end-to-end product ad](#7-full-example--end-to-end-product-ad)

---

## ภาพรวม show_marketing_studio

`show_marketing_studio` รับ params หลัก:

| param | ค่า | ใช้ |
|---|---|---|
| `action` | `list` / `presets` / `fetch` / `create` / `update` / `get` / `delete` | กริยาหลัก |
| `type` | `product` / `webproduct` / `brand_kit` / `avatar` / `hook` / `setting` / `ad_reference` / `ad_format` | ประเภท asset |
| `url` | URL สินค้า/เว็บ | คู่กับ `action='fetch'` |
| `scrap_url` | URL หน้าแบรนด์ | คู่กับ brand_kit |
| `medias[]` | `{value, role}` (`value` = media_id) | คู่กับ manual create — **ห้าม URL ดิบใน value** |

**Flow มาตรฐาน 3 ขั้น:**
1. สร้าง ad asset → `fetch` (จาก URL) **หรือ** `create` (จากรูป)
2. เลือก `presets` + hook + setting ให้ตรง ad type
3. `next_step` → `generate_video(model='marketing_studio_video')` พร้อม asset + preset

> Marketing Studio asset สามารถดึงด้วย `action='fetch'`/`get`, ดูรายการด้วย `action='list'`. ราคาต่อ ad ต่างตาม model/duration — preflight ด้วย `get_cost: true` ใน `generate_video` และเช็คเครดิตด้วย `balance` ก่อนสั่งจริง.

---

## 1. Product vs Webproduct

ตัดสินใจประเภท asset ก่อนเสมอ — เลือกผิดแล้ว ad จะ frame ผิด:

| Type | คืออะไร | ใช้เมื่อ | ตัวอย่าง ad |
|---|---|---|---|
| `product` | **สินค้าชิ้นเดียวจับต้องได้** | โฆษณาเน้นตัวสินค้า (โชว์ของ, unboxing, รีวิว) | ครีม, รองเท้า, เครื่องดื่ม, gadget |
| `webproduct` | **เว็บไซต์ / แอป / SaaS** | โปรโมตบริการ/ดิจิทัล (โชว์หน้าจอ/feature) | แอปมือถือ, SaaS dashboard, e-commerce site |

**Decision rule:**
```
สิ่งที่โฆษณาเป็นของจับต้องได้ (physical) → product
เป็นเว็บ/แอป/บริการดิจิทัล → webproduct
ไม่ชัด → default product
URL เป็น App Store / Google Play / SaaS landing → webproduct
```

ถ้าผู้ใช้ไม่ระบุ ให้ถาม 1 คำถาม (H4): "โฆษณานี้เน้น (a) ตัวสินค้าจับต้องได้ หรือ (b) เว็บ/แอป?"

---

## 2. Fetch flow (ดึงจาก URL)

วิธีเร็วที่สุดเมื่อสินค้า/เว็บมี URL อยู่แล้ว — Higgsfield ดึงรูป + ข้อมูลให้อัตโนมัติ.

```
show_marketing_studio(action='fetch', type='product',    url='https://shop.example/product/xyz')
show_marketing_studio(action='fetch', type='webproduct', url='https://app.example.com')
```

- เป็น **async** — มี progress pill ระหว่างดึง → รอ asset พร้อมก่อนไปขั้นถัดไป
- คืน ad asset (asset_id/reference) ใช้ต่อใน preset + `generate_video`
- ดู asset ที่ดึงมาแล้วได้ด้วย `action='list'` / `action='get'`
- ดึงไม่สมบูรณ์ (รูปขาด/หน้า block) → fallback ไป Manual create (ข้อ 3)

---

## 3. Manual create (จากรูป)

เมื่อไม่มี URL หรือ fetch ไม่ครบ — สร้าง asset จากรูปที่ upload เอง.

**ขั้นตอน:**
1. นำรูปเข้าระบบก่อน → ได้ `media_id`:
   - local file → `media_upload_widget` (เปิด widget ให้ผู้ใช้เลือก) หรือ `media_upload`
   - web image → `media_import_url` (URL → media_id)
2. สร้าง asset โดยอ้าง media_id:
```
show_marketing_studio(
  action='create',
  type='product',
  medias=[{ value: '<media_id>', role: '<role>' }]
)
```

- `medias[].value` = **media_id เท่านั้น — ห้าม URL ดิบ**
- หลาย angle/มุมสินค้า → ใส่หลาย media ใน `medias[]`
- ดู role ที่ asset type ต้องการ → `show_marketing_studio(action='get', ...)` หรือ session

---

## 4. Brand Kit (scrap_url)

Brand Kit = ชุด identity (โลโก้/สี/ฟอนต์/โทน) ที่ฝังลง ad ให้ดู on-brand. สร้างได้ 2 ทาง:

**(a) จากเว็บแบรนด์ (เร็วสุด) — `scrap_url`:**
```
show_marketing_studio(action='create', type='brand_kit', scrap_url='https://brand.example.com')
```
- ดึง logo/palette/typography จากหน้าเว็บอัตโนมัติ (async)

**(b) Manual create/update:** ต้องมี **CDN url** ของ asset (logo ฯลฯ) → upload ก่อนด้วย `media_upload` ให้ได้ url บน CDN แล้วค่อย create/update.

- ดู brand kit ที่มี → `action='list', type='brand_kit'`
- นำ brand_kit ผูกตอนสร้าง ad เพื่อให้ฉาก/สี/โลโก้ตรงแบรนด์

---

## 5. Presets / Hooks / Settings

หลังมี ad asset แล้ว เลือก **preset + hook + setting** กำหนดสไตล์/รูปแบบโฆษณา.

**ดู preset ที่มี:**
```
show_marketing_studio(action='presets', type='product')      # หรือ webproduct
```

**Ad presets (รูปแบบโฆษณายอดนิยม):**

| Preset | รูปแบบ | เหมาะกับ |
|---|---|---|
| **UGC** | คลิปเหมือนผู้ใช้ถ่ายเอง (มือถือ, จริงใจ) | social/TikTok, สร้างความน่าเชื่อ |
| **Tutorial** | สอน/สาธิตวิธีใช้ทีละขั้น | สินค้าที่ต้องอธิบายวิธีใช้ |
| **Unboxing** | แกะกล่อง/เผยสินค้า | สร้างความตื่นเต้น, สินค้าใหม่ |
| **Product Review** | รีวิวพูดถึงจุดเด่น | สร้าง trust, เปรียบเทียบ |
| **Virtual Try-On** | สวม/ลองสินค้ากับตัวคน | แฟชั่น, เครื่องสำอาง, accessories |

- **Hooks** (`type='hook'`) = ประโยค/ฉากเปิด 3 วินาทีแรก ดึงความสนใจ — เลือกให้ตรง preset
- **Settings** (`type='setting'`) = ฉาก/บรรยากาศพื้นหลัง ad
- เลือก preset/hook/setting ไม่ชัด → `action='presets'` ดูตัวเลือกจริงต่อ ad type (อย่าเดาชื่อ preset)

---

## 6. Soul ID character ใน ad

ใส่ **คนที่หน้าตาคงเส้นคงวา** (presenter/ตัวแทนแบรนด์) ลง ad ได้ ผ่าน Soul ID — เหมาะมากกับ preset UGC / Product Review / Virtual Try-On.

**ขั้นตอน:**
1. Train Soul ID ก่อน (ครั้งเดียว ใช้ซ้ำได้) — **ถามผู้ใช้ก่อนเสมอ** เพราะเสียเครดิต + ใช้เวลา:
```
show_characters(action='train')   # 5-20 รูป, ~10 นาที
```
2. นำ `soul_id` ที่ได้ ผูกตอน generate ad video — presenter จะหน้าเดิมทุก ad
3. avatar asset (`type='avatar'`) ใช้คู่กับ ad reference เป็นตัวแสดงในฉากได้

> ก่อน train ถาม: "ต้องการ train Soul ID (presenter หน้าเดิมทุก ad) ไหม? ใช้รูป 5-20 รูป ~10 นาที และเสียเครดิต." ถ้าไม่ต้องการคงหน้า → ข้าม ใช้ generic avatar/preset ปกติ.

---

## 7. Full example — end-to-end product ad

ตัวอย่าง: สร้าง UGC ad สำหรับครีมบำรุง จากหน้าสินค้าใน shop.

```
# STEP 0 — Pre-flight (บังคับ)
balance                          # เช็คเครดิตพอไหม

# 1. สร้าง product asset จาก URL (async — รอ pill เสร็จ)
show_marketing_studio(
  action='fetch', type='product',
  url='https://shop.example/serum-x'
)

# (ทางเลือก) ถ้าจะมี presenter หน้าเดิม — ถามผู้ใช้ก่อน แล้วค่อย train
# show_characters(action='train')   # 5-20 รูป, ~10 นาที, เสียเครดิต

# 2. ผูก brand identity (optional)
show_marketing_studio(
  action='create', type='brand_kit',
  scrap_url='https://shop.example'
)

# 3. ดู preset + เลือก UGC + hook + setting
show_marketing_studio(action='presets', type='product')
#   → เลือก preset UGC, hook ที่ตรง, setting ฉาก

# 4. Preflight cost ก่อนสั่งจริง
generate_video(
  model='marketing_studio_video',
  prompt='UGC-style ad: presenter applies Serum X, glowing skin result, on-brand',
  medias=[{ value: '<product_asset_or_soul_id>', role: '<role>' }],
  aspect_ratio='9:16',
  get_cost=true                   # คืนราคา ไม่สั่งจริง
)

# 5. สั่งจริง (async 3-5 นาที) → poll job จน completed
generate_video(
  model='marketing_studio_video',
  prompt='...',
  medias=[{ value: '<product_asset_or_soul_id>', role: '<role>' }],
  aspect_ratio='9:16'
)
#   → คืน job → poll status → job_display(job_id) แสดงผล
```

**Recap flow:** `fetch`/`create` asset → (optional brand_kit + Soul ID) → `presets` (UGC/Tutorial/Unboxing/Product-Review/Virtual-Try-On) + hook + setting → `get_cost` preflight → `generate_video(marketing_studio_video)` → poll → `job_display`.

> เครดิตหมดกลางทาง → `show_plans_and_credits(intent='topup')`. ราคา/รายชื่อ preset/model ที่แน่นอน — เช็คด้วย `models_explore` / `balance` / `get_cost` เสมอ (อย่าเดา).
