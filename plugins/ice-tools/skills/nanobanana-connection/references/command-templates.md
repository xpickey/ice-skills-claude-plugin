# Command Templates — Thai → MCP Call Mapping

แปลคำสั่งภาษาไทย/อังกฤษที่ผู้ใช้พิมพ์ → MCP Call จริง (rlabs/gemini-mcp, server name `gemini`, tool prefix `mcp__gemini__`) พร้อม Edge Case

> Backend: rlabs/gemini-mcp (`@rlabs-inc/gemini-mcp`) — default model `gemini-3-pro-image-preview` (Nano Banana Pro).
> ภาพถูก save ลง `GEMINI_OUTPUT_DIR` (`~/.local/share/gemini-mcp-images`) อัตโนมัติ — ไม่มี `output_path` param ให้กำหนดเอง.

## Pattern Recognition

| ผู้ใช้พิมพ์ | Recognize as | Suggested Spec |
|---|---|---|
| "ทำภาพ hero สำหรับ slide" | Slide Hero Image | aspectRatio 16:9 + imageSize 4K |
| "ทำ logo บริษัท..." | Logo Design | aspectRatio 1:1 + imageSize 2K + style flat/vector |
| "ทำ product shot..." | Product Photography | aspectRatio 1:1 or 3:4 + imageSize 4K + style photorealistic |
| "ทำ thumbnail YouTube..." | YouTube Thumbnail | aspectRatio 16:9 + imageSize 2K |
| "ทำ banner Facebook/IG" | Social Banner | aspectRatio 16:9 or 1:1 + imageSize 2K |
| "ทำ wallpaper มือถือ" | Mobile Wallpaper | aspectRatio 9:16 + imageSize 4K |
| "แก้ภาพนี้..." | Edit Session | start-image-edit → continue-image-edit → end-image-edit |
| "เปลี่ยน background เป็น..." | Background Replace | edit session + Background Replacement prompt |
| "ทำ mockup..." | Device/Print Mockup | aspectRatio varies + imageSize 4K |
| "ทำ icon set..." | Icon Set | aspectRatio 1:1 + imageSize 2K |
| "วาดการ์ตูน..." | Illustration | aspectRatio varies + imageSize 2K + style anime/illustration |
| "ทำ mood board..." | Mood Board | aspectRatio 1:1 + imageSize 1K (เรียกหลายครั้ง) |
| "ทำภาพประกอบบทความ" | Article Illustration | aspectRatio 16:9 + imageSize 2K |
| "ดูภาพนี้ให้หน่อย / ภาพนี้มีอะไร" | Image Analysis | gemini-analyze-image |

## Full Mapping Examples

### Example 1: "ทำภาพ hero สำหรับ slide proposal Oracle Cloud ERP"
```python
gemini-generate-image(
    prompt="""B2B hero image for Oracle Cloud ERP proposal, abstract
    conceptual visualization combining cloud architecture with enterprise
    data flow, isometric style with clean geometric lines, blue and teal
    palette with subtle orange accent, generous negative space for slide
    title on the left side. Professional, enterprise-grade aesthetic.""",
    style="photorealistic",
    aspectRatio="16:9",
    imageSize="4K",
    useGoogleSearch=True   # ถ้าอยากให้อ้างอิงภาพจริงประกอบ concept
)
# ภาพ save อัตโนมัติลง GEMINI_OUTPUT_DIR — รับ path กลับจาก tool result
```

### Example 2: "ทำ logo บริษัท ABC Consulting แบบ minimal สีน้ำเงิน"
```python
gemini-generate-image(
    prompt="""Minimalist logo design with the text "ABC Consulting",
    clean geometric sans-serif typography, deep navy blue (#1E3A8A) color,
    centered composition, pure white background. Professional, modern,
    scalable. Vector-style flat design. No gradients, no 3D effects, no
    drop shadow, no decorative elements.""",
    style="flat vector",
    aspectRatio="1:1",
    imageSize="2K"   # Logo ไม่จำเป็นต้อง 4K
)
# Note: ไม่มี negative_prompt param — ฝังข้อห้าม ("No gradients...") ใน prompt แทน
```

### Example 3: "วาด product shot กาแฟแก้วเดียวบนพื้นขาว"
```python
gemini-generate-image(
    prompt="""Product photography of a single ceramic coffee mug
    (matte beige, minimalist design) filled with espresso. Centered
    composition, clean pure white background (#FFFFFF), soft three-point
    lighting from upper-left, subtle ground shadow. Sharp focus throughout,
    color-accurate, commercial e-commerce style. No clutter, no hand model,
    no busy background, no harsh reflections.""",
    style="photorealistic",
    aspectRatio="3:4",
    imageSize="4K"
)
```

### Example 4: "ทำ thumbnail youtube หัวข้อ AI Transformation"
```python
gemini-generate-image(
    prompt="""YouTube thumbnail for "AI Transformation Explained" video,
    featuring a glowing brain-circuit hybrid icon as central visual,
    bold contrasting colors (electric blue vs vibrant orange), dramatic
    light rays radiating outward, dark gradient background. High visual
    impact, click-bait friendly. Space on the lower-third for 3-5 word
    headline text overlay.""",
    style="photorealistic",
    aspectRatio="16:9",
    imageSize="2K"
)
```

### Example 5: "แก้ภาพนี้เปลี่ยน background เป็นทะเล" (session-based edit)
```python
# Step 1 — เปิด session แก้ภาพ → คืน sessionId + ภาพ base
session = gemini-start-image-edit(
    prompt="""Replace the background with a serene tropical ocean view
    at sunset — calm turquoise water, soft pink-orange sky, distant
    horizon line, subtle wave details. Keep the subject (person in white
    shirt) exactly as in the original, preserve pose, facial expression,
    and lighting on subject. Blend edges naturally with warm sunset
    lighting matching the new background.""",
    aspectRatio="3:4",
    imageSize="4K"
)
# → ได้ sessionId

# Step 2 — แก้ต่อใน session เดิมได้เรื่อย ๆ (multi-turn)
gemini-continue-image-edit(
    sessionId=session.sessionId,
    prompt="Make the sunset slightly warmer and add gentle lens flare on the right."
)

# Step 3 — พอใจแล้วปิด session
gemini-end-image-edit(sessionId=session.sessionId)
```

### Example 6: "สร้าง 4 variation banner สำหรับ Facebook Ad"
```python
# ไม่มี n param — เรียก gemini-generate-image ซ้ำ 4 ครั้ง (ปรับ seed ผ่านการ
# เปลี่ยน detail ใน prompt เล็กน้อย หรือเรียกซ้ำ prompt เดิมเพื่อได้ variation)
base_prompt = """Facebook Ad banner for [PRODUCT/CAMPAIGN], vibrant attention-
grabbing composition, [BRAND COLORS], lifestyle setting, focal point
on the right two-thirds (left third reserved for text overlay).
Professional ad aesthetic, mobile-first design."""

for variation_hint in [
    "warm daytime lighting",
    "cool evening tone",
    "bright studio backdrop",
    "outdoor lifestyle scene",
]:
    gemini-generate-image(
        prompt=f"{base_prompt} Variation accent: {variation_hint}.",
        style="photorealistic",
        aspectRatio="16:9",
        imageSize="2K"
    )
# แต่ละครั้ง save แยกไฟล์ใน GEMINI_OUTPUT_DIR อัตโนมัติ
```

### Example 7: "ทำ Persian cat ริมหน้าต่าง 16:9 4K (ที่ลองในแชท)"
```python
gemini-generate-image(
    prompt="""A majestic long-haired Persian cat with luxurious white and
    silver fur sitting peacefully on a wooden windowsill, gazing out
    through a slightly open window at a breathtaking sunset. Warm golden
    and amber light streams through the window, illuminating the cat's
    fluffy fur and making its bright emerald-green eyes glow. The sky
    outside displays brilliant orange, pink, and purple hues with soft
    clouds catching the last rays of sunlight. Cozy interior with warm
    bokeh light. Photorealistic, cinematic lighting, shallow depth of
    field, hyper-detailed fur texture, professional photography style.""",
    style="photorealistic",
    aspectRatio="16:9",
    imageSize="4K"
)
```

### Example 8: "ช่วยร่าง prompt ภาพ..." (prompt helper)
```python
# ให้ Gemini ช่วยขยาย idea สั้น ๆ → เป็น prompt เต็มก่อน generate
gemini-image-prompt(
    description="โลโก้ร้านกาแฟ specialty สไตล์ minimal",
    style="flat vector",
    mood="warm, premium, inviting",
    details="earthy brown palette, coffee bean motif, clean typography"
)
# → ได้ prompt ที่ขยายแล้ว → ส่งต่อเข้า gemini-generate-image
```

### Example 9: "ดูภาพที่เพิ่งทำให้หน่อย ว่าต้องแก้ตรงไหน" (Claude เห็นภาพ → iterate)
```python
# Feature ใหม่: Claude วิเคราะห์ภาพได้เอง → ใช้ผล feedback ไปแก้ต่อ
gemini-analyze-image(
    imagePath="/Users/xpickey/.local/share/gemini-mcp-images/<filename>.png",
    query="ประเมินองค์ประกอบภาพ แสง สี และจุดที่ควรปรับสำหรับใช้เป็น slide hero",
    detectObjects=True,
    thinkingLevel="high"
)
# → ใช้ผลวิเคราะห์ตัดสินใจ continue-image-edit หรือ generate ใหม่ ได้แม่นขึ้น
```

---

## Edge Cases

### EC-1: ผู้ใช้บอก "Logo" แต่ต้องการ Icon
**Clarify:** ขนาดเล็กที่จะเอาไปใช้ใน App/Web หรือ Branding หลัก?
- ถ้า Branding หลัก → ใช้ Logo template (aspectRatio 1:1 + imageSize 2K)
- ถ้า App Icon → ใช้ Icon Set template (D-03)

### EC-2: ผู้ใช้บอก "ทำหลายภาพ" แต่ไม่ระบุจำนวน
**Default:** เรียก `gemini-generate-image` ซ้ำ 4 ครั้ง (ไม่มี batch `n` param) — แต่ละครั้ง save แยกไฟล์ใน `GEMINI_OUTPUT_DIR` อัตโนมัติ
**Clarify:** หากต้องการ > 4 ก็เรียกเพิ่มได้ตามจำนวน ไม่มีเพดาน per-call

### EC-3: ผู้ใช้ส่งภาพมาแก้ แต่ไม่บอกว่าเปลี่ยนอะไร
**Don't guess.** ถาม:
- เปลี่ยนเฉพาะส่วนไหน? (Background / Subject / Color / Style)
- รักษาส่วนไหนไว้?

ทางเลือกเสริม: ใช้ `gemini-analyze-image` ดูภาพต้นทางก่อน เพื่อตั้งคำถามให้ตรงจุด

### EC-4: ผู้ใช้บอก "ทำให้ดูแพง / Premium / High-end"
**Translate:**
- ภาพ: เพิ่ม "luxurious", "premium materials", "high-end retail aesthetic", "soft studio lighting" ใน prompt + `style="photorealistic"`
- Logo: "refined typography", "sophisticated minimalism", "elegant"
- เพิ่ม `imageSize="4K"` สำหรับงาน Premium/High-end (default model gemini-3-pro-image-preview รองรับอยู่แล้ว)

### EC-5: ผู้ใช้บอก "เร็วๆ ก่อน" / "Draft"
**Use:** `imageSize="1K"` — เร็วและถูกที่สุด สำหรับ Iteration (ไม่มี model tier ให้สลับ — ปรับที่ขนาดภาพแทน)

### EC-6: ผู้ใช้บอก "4K Print Quality"
**Use:** `imageSize="4K"` + `aspectRatio` ที่ตรง Print Format (เช่น 4:3, 3:2) + `style="photorealistic"`

### EC-7: ผู้ใช้บอก "ภาพแมว" สั้นๆ
**Don't generate.** ขยาย Prompt ก่อนด้วย 6 ส่วน (หรือใช้ `gemini-image-prompt` ช่วยร่าง) หรือ ขอข้อมูลเพิ่ม:
- พันธุ์อะไร? สี? ขนาด?
- กำลังทำอะไร?
- ที่ไหน?
- สไตล์/มู้ดยังไง?

### EC-8: ผู้ใช้ขอภาพคน/บุคคลที่มีชื่อจริง
**Refuse politely.** ห้ามสร้าง Deepfake/Impersonation
**Alternative:** "สร้างภาพ Generic ของบุคคลในวิชาชีพ/ลักษณะที่ระบุ"

### EC-9: ผู้ใช้ขอภาพที่มี Brand Logo บริษัทอื่น
**Refuse politely.** Trademark Issue
**Alternative:** "Generic representation of [industry]" หรือใส่ Logo Post-production

### EC-10: ผู้ใช้บอกว่า "ภาพที่ทำมาแย่ แก้ใหม่"
**Don't blindly retry.** ถาม:
- แย่ตรงไหน? (Composition / Color / Style / Subject)
- สิ่งที่ Like จากภาพเดิม คืออะไร? (จะรักษาไว้)
- ตัวอย่าง Reference Image ที่ชอบมีไหม?
- ใช้ `gemini-analyze-image` ดูภาพเดิมก่อน เพื่อระบุจุดอ่อนอย่างเป็นรูปธรรม
- เปิด edit session (`gemini-start-image-edit`) แล้ว `gemini-continue-image-edit` ปรับทีละจุด แทน generate ใหม่ทั้งภาพ

### EC-11: 429 / RESOURCE_EXHAUSTED ตอนเรียก generate
**สาเหตุ:** billing ยังไม่เปิด (image generation ไม่อยู่ใน free tier)
**Fix:** เปิด billing ที่ https://aistudio.google.com/apikey แล้วลองใหม่ — ไม่ใช่ปัญหา prompt

### EC-12: อยากเช็คว่ามี edit session ค้างอยู่ไหม
**Use:** `gemini-list-image-sessions()` ดู session ที่เปิดอยู่ → ปิดด้วย `gemini-end-image-edit(sessionId=...)` ถ้าค้าง

---

## Universal Response Template (หลัง Generate)

```
✓ สร้างภาพเรียบร้อยครับ

Image:        [computer:///absolute/path/from/GEMINI_OUTPUT_DIR/image.png]
Model:        gemini-3-pro-image-preview (Nano Banana Pro)
Aspect Ratio: [16:9 etc.]
Image Size:   [4K / 2K / 1K]
Style:        [photorealistic / watercolor / anime / ...]

Prompt ที่ใช้:
> [first 1-2 lines of prompt]

Next Steps (เลือกได้):
1. ใช้เลย — อัปโหลดเข้า [slide/social/site]
2. แก้เพิ่มเติม — ผมเปิด edit session แก้ให้ทีละจุด (บอกว่าเปลี่ยนอะไร)
3. สร้าง Variations — ผมเรียกซ้ำทำเพิ่มอีก 3 แบบให้เลือก
4. ขนาดอื่น — บอกว่าจะเอาไปใช้ที่ไหน ผมปรับ aspectRatio / imageSize
5. ให้ผมตรวจภาพให้ — ผมใช้ gemini-analyze-image ดูแล้วเสนอจุดปรับ
```
