# Command Templates — Thai → MCP Call Mapping

แปลคำสั่งภาษาไทย/อังกฤษที่ผู้ใช้พิมพ์ → MCP Call จริง พร้อม Edge Case

## Pattern Recognition

| ผู้ใช้พิมพ์ | Recognize as | Suggested Spec |
|---|---|---|
| "ทำภาพ hero สำหรับ slide" | Slide Hero Image | nb2 + 16:9 + 4k |
| "ทำ logo บริษัท..." | Logo Design | flash/nb2 + 1:1 + 2k + logo_text template |
| "ทำ product shot..." | Product Photography | nb2 + 1:1 or 3:4 + 4k |
| "ทำ thumbnail YouTube..." | YouTube Thumbnail | nb2 + 16:9 + 2k |
| "ทำ banner Facebook/IG" | Social Banner | nb2 + 16:9 or 1:1 + 2k |
| "ทำ wallpaper มือถือ" | Mobile Wallpaper | nb2 + 9:16 + 4k |
| "แก้ภาพนี้..." | Edit Mode | mode=edit + input_image_path_1 |
| "เปลี่ยน background เป็น..." | Background Replace | edit + Background Replacement template |
| "ทำ mockup..." | Device/Print Mockup | nb2 + varies + 4k |
| "ทำ icon set..." | Icon Set | nb2 + 1:1 + 2k |
| "วาดการ์ตูน..." | Illustration | nb2 + varies + 2k |
| "ทำ mood board..." | Mood Board | flash + 1:1 + 1k (multiple) |
| "ทำภาพประกอบบทความ" | Article Illustration | nb2 + 16:9 + 2k |

## Full Mapping Examples

### Example 1: "ทำภาพ hero สำหรับ slide proposal Oracle Cloud ERP"
```python
generate_image(
    prompt="""B2B hero image for Oracle Cloud ERP proposal, abstract
    conceptual visualization combining cloud architecture with enterprise
    data flow, isometric style with clean geometric lines, blue and teal
    palette with subtle orange accent, generous negative space for slide
    title on the left side. Professional, enterprise-grade aesthetic.""",
    model_tier="nb2",
    aspect_ratio="16:9",
    resolution="4k",
    output_path="/Users/.../slides/section-1-hero_V01R01.png",
    enable_grounding=True
)
```

### Example 2: "ทำ logo บริษัท ABC Consulting แบบ minimal สีน้ำเงิน"
```python
generate_image(
    prompt="""Minimalist logo design with the text "ABC Consulting",
    clean geometric sans-serif typography, deep navy blue (#1E3A8A) color,
    centered composition, pure white background. Professional, modern,
    scalable. Vector-style flat design.""",
    model_tier="flash",  # Logo ไม่ต้อง 4K
    aspect_ratio="1:1",
    resolution="2k",
    negative_prompt="gradient, 3D effects, drop shadow, decorative elements",
    output_path="/Users/.../brand/logo_minimal_V01R01.png"
)
```

### Example 3: "วาด product shot กาแฟแก้วเดียวบนพื้นขาว"
```python
generate_image(
    prompt="""Product photography of a single ceramic coffee mug
    (matte beige, minimalist design) filled with espresso. Centered
    composition, clean pure white background (#FFFFFF), soft three-point
    lighting from upper-left, subtle ground shadow. Sharp focus throughout,
    color-accurate, commercial e-commerce style.""",
    model_tier="nb2",
    aspect_ratio="3:4",
    resolution="4k",
    negative_prompt="cluttered, hand model, busy background, reflections",
    output_path="/Users/.../products/coffee_mug_white_bg_V01R01.png"
)
```

### Example 4: "ทำ thumbnail youtube หัวข้อ AI Transformation"
```python
generate_image(
    prompt="""YouTube thumbnail for "AI Transformation Explained" video,
    featuring a glowing brain-circuit hybrid icon as central visual,
    bold contrasting colors (electric blue vs vibrant orange), dramatic
    light rays radiating outward, dark gradient background. High visual
    impact, click-bait friendly. Space on the lower-third for 3-5 word
    headline text overlay.""",
    model_tier="nb2",
    aspect_ratio="16:9",
    resolution="2k",
    output_path="/Users/.../youtube/ai-transform_thumb_V01R01.png"
)
```

### Example 5: "แก้ภาพนี้เปลี่ยน background เป็นทะเล"
```python
generate_image(
    prompt="""Replace the background with a serene tropical ocean view
    at sunset — calm turquoise water, soft pink-orange sky, distant
    horizon line, subtle wave details. Keep the subject (person in white
    shirt) exactly as in the original, preserve pose, facial expression,
    and lighting on subject. Blend edges naturally with warm sunset
    lighting matching the new background.""",
    mode="edit",
    input_image_path_1="/Users/.../originals/portrait_studio.jpg",
    model_tier="nb2",
    output_path="/Users/.../edited/portrait_beach_V01R01.png"
)
```

### Example 6: "สร้าง 4 variation banner สำหรับ Facebook Ad"
```python
generate_image(
    prompt="""Facebook Ad banner for [PRODUCT/CAMPAIGN], vibrant attention-
    grabbing composition, [BRAND COLORS], lifestyle setting, focal point
    on the right two-thirds (left third reserved for text overlay).
    Professional ad aesthetic, mobile-first design.""",
    model_tier="nb2",
    aspect_ratio="16:9",
    resolution="2k",
    n=4,
    output_path="/Users/.../ads/facebook_variation_/"  # trailing slash
    # → จะได้ facebook_variation.png, _2.png, _3.png, _4.png
)
```

### Example 7: "ทำ Persian cat ริมหน้าต่าง 16:9 4K (ที่ลองในแชท)"
```python
generate_image(
    prompt="""A majestic long-haired Persian cat with luxurious white and
    silver fur sitting peacefully on a wooden windowsill, gazing out
    through a slightly open window at a breathtaking sunset. Warm golden
    and amber light streams through the window, illuminating the cat's
    fluffy fur and making its bright emerald-green eyes glow. The sky
    outside displays brilliant orange, pink, and purple hues with soft
    clouds catching the last rays of sunlight. Cozy interior with warm
    bokeh light. Photorealistic, cinematic lighting, shallow depth of
    field, hyper-detailed fur texture, professional photography style.""",
    model_tier="nb2",
    aspect_ratio="16:9",
    resolution="4k",
    output_path="/Users/.../images/persian_cat_sunset_V01R01.png"
)
```

---

## Edge Cases

### EC-1: ผู้ใช้บอก "Logo" แต่ต้องการ Icon
**Clarify:** ขนาดเล็กที่จะเอาไปใช้ใน App/Web หรือ Branding หลัก?
- ถ้า Branding หลัก → ใช้ Logo template
- ถ้า App Icon → ใช้ Icon Set template (D-03)

### EC-2: ผู้ใช้บอก "ทำหลายภาพ" แต่ไม่ระบุจำนวน
**Default:** n=4 + output_path เป็น directory (trailing slash)
**Clarify:** หาก > 4 ต้องเรียกหลายครั้ง (max=4 per call)

### EC-3: ผู้ใช้ส่งภาพมาแก้ แต่ไม่บอกว่าเปลี่ยนอะไร
**Don't guess.** ถาม:
- เปลี่ยนเฉพาะส่วนไหน? (Background / Subject / Color / Style)
- รักษาส่วนไหนไว้?

### EC-4: ผู้ใช้บอก "ทำให้ดูแพง / Premium / High-end"
**Translate:**
- ภาพ: เพิ่ม "luxurious", "premium materials", "high-end retail aesthetic", "soft studio lighting"
- Logo: "refined typography", "sophisticated minimalism", "elegant"
- ใช้ Pro model สำหรับ Premium/High-end

### EC-5: ผู้ใช้บอก "เร็วๆ ก่อน" / "Draft"
**Use:** model_tier="flash" + resolution="1k" — เร็วและถูก สำหรับ Iteration

### EC-6: ผู้ใช้บอก "4K Print Quality"
**Use:** model_tier="nb2" or "pro" + resolution="4k" + aspect_ratio ที่ตรง Print Format (เช่น 4:3, 3:2)

### EC-7: ผู้ใช้บอก "ภาพแมว" สั้นๆ
**Don't generate.** ขยาย Prompt ก่อนด้วย 6 ส่วน หรือ ขอข้อมูลเพิ่ม:
- พันธุ์อะไร? สี? ขนาด?
- กำลังทำอะไร?
- ที่ไหน?
- สไตล์/มู้ดยังไง?

### EC-8: ผู้ใช้ขอภาพคน/บุคคลที่มีชื่อจริง
**Refuse politely.** Nano Banana ห้ามสร้าง Deepfake/Impersonation
**Alternative:** "สร้างภาพ Generic ของบุคคลในวิชาชีพ/ลักษณะที่ระบุ"

### EC-9: ผู้ใช้ขอภาพที่มี Brand Logo บริษัทอื่น
**Refuse politely.** Trademark Issue
**Alternative:** "Generic representation of [industry]" หรือใส่ Logo Post-production

### EC-10: ผู้ใช้บอกว่า "ภาพที่ทำมาแย่ แก้ใหม่"
**Don't blindly retry.** ถาม:
- แย่ตรงไหน? (Composition / Color / Style / Subject)
- สิ่งที่ Like จากภาพเดิม คืออะไร? (จะรักษาไว้)
- ตัวอย่าง Reference Image ที่ชอบมีไหม?
- ลอง mode=edit + Iterative Edit Pattern แทน Generate ใหม่

---

## Universal Response Template (หลัง Generate)

```
✓ สร้างภาพเรียบร้อยครับ

Image:        [computer:///absolute/path/to/image.png]
Model:        [nb2 / pro / flash]
Aspect Ratio: [16:9 etc.]
Resolution:   [4k etc.]
Generation:   [N seconds]

Prompt ที่ใช้:
> [first 1-2 lines of prompt]

Next Steps (เลือกได้):
1. ใช้เลย — อัปโหลดเข้า [slide/social/site]
2. แก้เพิ่มเติม — ผมแก้ให้ (บอกว่าเปลี่ยนอะไร)
3. สร้าง Variations — ผมทำเพิ่มอีก 3 แบบให้เลือก
4. ขนาดอื่น — บอกว่าจะเอาไปใช้ที่ไหน ผมปรับ Aspect Ratio
```
