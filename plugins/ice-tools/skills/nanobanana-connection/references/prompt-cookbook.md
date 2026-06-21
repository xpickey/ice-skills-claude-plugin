# Prompt Cookbook — 30+ Production-grade Patterns

> **Engine:** rlabs/gemini-mcp (`@rlabs-inc/gemini-mcp`) · server `gemini` · default model Nano Banana Pro (`gemini-3-pro-image-preview`).
> **Tools:** `mcp__gemini__gemini-generate-image` (one-shot) · `gemini-start/continue/end-image-edit` (session-based edit) · `gemini-analyze-image` (Claude เห็นภาพ → iterate) · `gemini-image-prompt` (ช่วยร่าง prompt).

แต่ละ Pattern มี: **Use Case** + **Recommended Specs** + **Prompt Template** (ทั้งไทย+อังกฤษ พร้อม Variables) + **Variations**

## Parameter Model (rlabs — อ่านก่อนใช้ทุก Pattern)

`gemini-generate-image` รับ param ดังนี้ (ต่างจาก nanobanana เดิมที่ใช้ `model_tier`/`resolution`/`negative_prompt`/`output_path`):

| Param | ค่าที่ใช้ได้ | หมายเหตุ |
|---|---|---|
| `prompt` *(required)* | ข้อความบรรยายภาพ | ใส่ subject + composition + lighting + mood + technical ในนี้ |
| `style` | เช่น `photorealistic`, `cinematic`, `watercolor`, `oil painting`, `anime`, `3D render`, `isometric`, `flat design`, `pixel art` | **param แยก** — ไม่ฝัง style ใน prompt อีกต่อไป |
| `aspectRatio` | `1:1`, `16:9`, `9:16`, `21:9`, `4:3`, `3:4`, `4:5`, `5:4`, `2:3`, `3:2` | แทนที่ `aspect_ratio` เดิม |
| `imageSize` | `1K`, `2K` (default), `4K` | แทนที่ `resolution` (high/4k/2k/1k) และไม่มี `model_tier` (nb2/pro/flash) อีกแล้ว |
| `useGoogleSearch` | `true`/`false` | ให้ภาพอ้างอิงข้อมูลจริงจาก search เมื่อจำเป็น |

**สิ่งที่หายไปจาก nanobanana (อย่าใช้):** `model_tier`, `resolution` (high/4k…), `negative_prompt` (image), `output_path`, `n` (batch), `mode=edit`, `input_image_path_*`, built-in template (`logo_text`/`sticker_flat`). ภาพ save อัตโนมัติลง `GEMINI_OUTPUT_DIR` (`~/.local/share/gemini-mcp-images`) — ไม่ต้องระบุ path.

**Negative prompt (image) ไม่มีแล้ว** — สิ่งที่ "ไม่อยากได้" ให้เขียนเป็นประโยคในตัว `prompt` (เช่น "clean background with no text or logo, no harsh shadows"). ดู Negative-as-clause Library ด้านล่าง.

## Universal Prompt Anatomy (ใช้ทุกครั้ง)

```
[Subject] + [Composition/Camera] + [Action/State] + [Setting/Location] +
[Lighting] + [Mood/Atmosphere] + [Technical Specs] + [clauses to avoid]
```
- **Style** ไม่ต้องอยู่ใน anatomy ของ prompt อีกแล้ว — ย้ายไปใส่ param `style` แยก.
- **Specs ในแต่ละ Pattern** เขียนรูปแบบ `style=... · aspectRatio=... · imageSize=...` เพื่อ map ตรงเข้า param.

**English Bridge Words (ใช้บ่อย):**
- Style (→ param `style`): photorealistic, cinematic, illustration, watercolor, oil painting, anime, 3D render, isometric, flat design, pixel art
- Lighting (→ ใน `prompt`): golden hour, blue hour, soft diffused, dramatic side-lit, rim light, studio softbox, neon, candlelight
- Composition (→ ใน `prompt`): close-up, medium shot, wide shot, overhead, low angle, eye level, three-quarter view, rule of thirds, centered
- Mood (→ ใน `prompt`): serene, energetic, melancholic, mysterious, joyful, professional, intimate, epic

---

## Category 1: PHOTOGRAPHY (10 Patterns)

### P-01: Portrait — Professional Headshot
**Use:** LinkedIn, About Page, Speaker Bio
**Specs:** `style=photorealistic` · `aspectRatio=4:5` · `imageSize=4K`

```
A professional headshot of [GENDER] [AGE] [PROFESSION] wearing [ATTIRE],
warm friendly smile, looking directly at camera. Soft studio lighting
with subtle rim light. Neutral gradient background ([COLOR1] to [COLOR2]).
Shallow depth of field, 85mm lens, magazine quality. Clean background with
no text or logo, no harsh shadows.
```
- Variables: GENDER, AGE, PROFESSION (e.g., "Asian male 40s executive"), ATTIRE ("navy business suit"), COLOR1/2 ("gray", "charcoal")

### P-02: Product Photography — White Background
**Use:** E-commerce, Catalog, Spec Sheet
**Specs:** `style=photorealistic` · `aspectRatio=1:1` หรือ `3:4` · `imageSize=4K`

```
Product photography of [PRODUCT], centered composition, clean pure white
background (#FFFFFF), soft three-point lighting, subtle ground shadow.
Sharp focus throughout, color accurate, commercial style. No reflections,
no hand model, no busy background.
```
- Variables: PRODUCT ("ceramic coffee mug, beige color, matte finish")

### P-03: Product Photography — Lifestyle
**Use:** Marketing, Social Media, Hero Image
**Specs:** `style=photorealistic` · `aspectRatio=16:9` หรือ `4:5` · `imageSize=4K`

```
Lifestyle product shot of [PRODUCT] in [SETTING], natural [TIME] lighting,
[MOOD] atmosphere. [HUMAN ELEMENT optional]. Authentic candid feel,
shallow depth of field, color-graded with [COLOR PALETTE].
```
- Variables: PRODUCT, SETTING ("scandinavian kitchen counter"), TIME ("morning golden hour"), MOOD ("calm, inviting"), COLOR PALETTE ("warm earth tones")

### P-04: Food Photography — Hero Dish
**Use:** Menu, Recipe, Restaurant Marketing
**Specs:** `style=photorealistic` · `aspectRatio=1:1` หรือ `4:5` · `imageSize=4K`

```
Overhead food photography of [DISH] on [PLATE], styled with [GARNISH],
natural window light from the left, soft shadows, vibrant colors,
high-end restaurant aesthetic. Marble surface, minimal props.
```
- Variables: DISH ("seared salmon with asparagus"), PLATE ("matte black ceramic"), GARNISH ("lemon wedge, fresh dill")

### P-05: Architecture — Building Exterior
**Use:** Real Estate, Architecture Portfolio, Brand HQ
**Specs:** `style=photorealistic` · `aspectRatio=16:9` หรือ `21:9` · `imageSize=4K`

```
Architectural photography of [BUILDING TYPE] in [LOCATION/STYLE],
[TIME] light, dramatic perspective from [ANGLE]. Clean lines emphasized,
sky [SKY CONDITION], minimal people. Wide-angle lens, color-corrected.
```
- Variables: BUILDING TYPE ("modern office tower"), LOCATION/STYLE ("Bangkok CBD glass curtain wall"), TIME ("blue hour"), ANGLE ("low angle hero shot"), SKY ("deep blue with thin clouds")

### P-06: Landscape — Cinematic
**Use:** Hero Banner, Inspiration Image, Slide Cover
**Specs:** `style=cinematic` · `aspectRatio=21:9` · `imageSize=4K`

```
Cinematic landscape of [LOCATION] during [TIME OF DAY], featuring
[FOREGROUND], [MIDGROUND], [BACKGROUND]. [WEATHER] adds atmosphere.
Composition follows rule of thirds, dramatic [COLOR PALETTE]
color grading, anamorphic lens flare. Inspiring, vast scale.
```
- Variables: LOCATION ("Northern Thailand mountain range"), TIME ("sunrise"), FOREGROUND ("morning mist over rice terraces"), WEATHER ("low fog"), COLOR ("warm amber and teal")

### P-07: Street Photography — Urban Story
**Use:** Editorial, Storytelling, Cultural Asset
**Specs:** `style=photorealistic` · `aspectRatio=3:2` · `imageSize=2K` หรือ `4K`

```
Candid street photography in [CITY/DISTRICT], [SUBJECT] caught in [ACTION],
authentic moment. [LIGHTING] adds depth. 35mm lens, slight grain,
documentary style, Magnum Photos aesthetic.
```

### P-08: Macro — Texture/Detail
**Use:** Brand Storytelling, Product Detail, Texture Reference
**Specs:** `style=photorealistic` · `aspectRatio=1:1` · `imageSize=4K`

```
Macro photography of [SUBJECT], extreme close-up showing [TEXTURE DETAIL],
soft directional light revealing surface character. Shallow depth of field
with bokeh background, color-accurate, museum quality.
```

### P-09: Event Photography — Conference/Workshop
**Use:** Case Study, Marketing, Internal Comms
**Specs:** `style=photorealistic` · `aspectRatio=3:2` · `imageSize=2K`

```
Photojournalistic shot of [EVENT TYPE], [SCENE], natural mixed lighting
(ambient + warm spots), authentic engagement, no posed feeling.
Tasteful focus on [FOCAL ELEMENT], background context softly visible.
```

### P-10: Drone/Aerial
**Use:** Project Overview, Site Photo, Hero Banner
**Specs:** `style=photorealistic` · `aspectRatio=21:9` · `imageSize=4K`

```
Aerial drone photography of [LOCATION], overhead perspective at [ALTITUDE],
[TIME] light casting long shadows. [PATTERN/COMPOSITION FEATURE] creates
visual interest. Color-graded, sharp detail throughout.
```

---

## Category 2: DESIGN/BRAND (8 Patterns)

### D-01: Logo — Minimal Type
**Use:** Quick Logo Concept, Brand Variant
**Specs:** `style=flat design` · `aspectRatio=1:1` · `imageSize=2K`

```
Minimalist logo design with the text "[BRAND NAME]", clean geometric
sans-serif typography, [COLOR] color, centered composition, pure white
background. Professional, modern, scalable, vector-style flat design.
No 3D effects, no gradients, no decorative elements, single typeface only.
```

### D-02: Logo — Icon + Wordmark
**Specs:** `style=flat design` · `aspectRatio=1:1` · `imageSize=2K`

```
Logo combining a simple geometric icon ([ICON DESCRIPTION]) with the
wordmark "[BRAND NAME]" set in [TYPOGRAPHY STYLE]. [COLOR PALETTE].
Icon left of text, balanced spacing, pure white background. Flat vector
style, no drop shadow, no gradients.
```

### D-03: Icon Set — Consistent Style
**Use:** UI/UX, App Icons, Documentation
**Specs:** `style=flat design` · `aspectRatio=1:1` · `imageSize=2K`

```
Set of [N] icons in consistent [STYLE] style: [ICON1], [ICON2], [ICON3].
[COLOR] color on white background. Grid layout, uniform stroke width
([WEIGHT]), rounded corners, modern flat design.
```

### D-04: Pattern — Brand Background
**Specs:** `style=flat design` · `aspectRatio=1:1` · `imageSize=2K`

```
Seamless tileable pattern featuring [MOTIFS] in [STYLE], [COLOR PALETTE],
geometric/organic [GEOMETRY], suitable for brand backgrounds. Subtle,
not distracting. Vector style.
```

### D-05: Mockup — Device/Print
**Use:** Pitch Deck, Portfolio, Concept Validation
**Specs:** `style=photorealistic` · `aspectRatio=varies` · `imageSize=4K`

```
Realistic mockup of [DEVICE/MEDIUM] displaying [SCREEN/DESIGN CONTENT],
[ENVIRONMENT SETTING], soft studio lighting with subtle shadow.
Photorealistic, high-fidelity, no UI overlays beyond the design itself.
```
- Variables: DEVICE ("MacBook Pro 16-inch open at 45-degree angle"), CONTENT ("dashboard with charts")

### D-06: Concept Sketch — Workshop/Whiteboard
**Use:** Design Sprint, Ideation, Workshop Output
**Specs:** `style=illustration` · `aspectRatio=4:3` · `imageSize=1K` (เร็ว/ประหยัด)

```
Hand-drawn concept sketch on white paper of [CONCEPT], pencil and marker
style, casual ideation feel, annotation notes in handwriting, brainstorm
energy. Workshop board aesthetic.
```

### D-07: Sticker — Flat Design
**Use:** Marketing Asset, Social Sticker, Internal Fun
**Specs:** `style=flat design` · `aspectRatio=1:1` · `imageSize=1K`

```
Flat design sticker of [SUBJECT], bold outlines, [COLOR PALETTE],
playful style, transparent or pure white background, slight 3D shadow.
Vector aesthetic, suitable for product packaging or app stickers.
```

### D-08: Infographic Element
**Use:** Slide, Report, Social Post
**Specs:** `style=flat design` · `aspectRatio=1:1` หรือ `16:9` · `imageSize=2K`

```
Infographic illustration of [CONCEPT], minimalist flat design, [COLOR
PALETTE matching brand], clean composition with [NUMBER] elements:
[ELEMENT1], [ELEMENT2], [ELEMENT3]. Clear visual hierarchy, no text
labels (will be added in post-production).
```

---

## Category 3: MARKETING/SOCIAL (6 Patterns)

### M-01: Hero Banner — Web Landing
**Specs:** `style=cinematic` · `aspectRatio=21:9` หรือ `16:9` · `imageSize=4K`

```
Hero banner image for [WEBSITE TOPIC], featuring [MAIN VISUAL ELEMENT],
[COLOR PALETTE matching brand]. Cinematic composition with visual breathing
room for headline text on the [LEFT/RIGHT/CENTER]. Engaging, professional,
conversion-optimized aesthetic.
```

### M-02: Social Square — Instagram
**Specs:** `style=photorealistic` (หรือ `flat design`) · `aspectRatio=1:1` · `imageSize=2K`

```
Instagram-style square post about [TOPIC], vibrant [COLOR], attention-grabbing
first second, central focal point. Suitable for adding text overlay.
Mobile-feed optimized.
```

### M-03: Story/Reel — Vertical
**Specs:** `style=cinematic` · `aspectRatio=9:16` · `imageSize=2K`

```
Vertical 9:16 image for Instagram Story/Reel cover about [TOPIC],
[VISUAL ELEMENT], [MOOD], thumb-stopping aesthetic. Lower third reserved
for text overlay. Bold composition.
```

### M-04: YouTube Thumbnail
**Specs:** `style=photorealistic` · `aspectRatio=16:9` · `imageSize=2K`

```
YouTube thumbnail for "[VIDEO TITLE]" featuring [CENTRAL VISUAL] with
exaggerated [EMOTION/REACTION], bold contrasting colors ([COLOR1] vs
[COLOR2]), high visual impact, click-bait friendly composition. Space
for 3-5 word headline text overlay.
```

### M-05: Campaign Banner Series — Consistent
**Specs:** `style=` (ล็อกค่าเดียวทุกใบเพื่อ consistency) · `aspectRatio=` (ล็อกค่าเดียว) · `imageSize=2K`

```
Series of [N] campaign banners, all featuring [CONSISTENT ELEMENT],
[COLOR PALETTE], same composition framework but different
[VARIATION DIMENSION e.g., season/product/audience]. Banner [N] focus:
[SPECIFIC FEATURE].
```
- **Consistency tip (rlabs ไม่มี `n` batch):** generate ทีละใบโดยล็อก `style`, `aspectRatio`, `imageSize` ให้เหมือนกันทุกครั้ง แล้วเปลี่ยนเฉพาะ [SPECIFIC FEATURE] ใน `prompt`. ถ้าต้องการให้ใบหลัง "ต่อยอด" จากใบแรกจริง ๆ ใช้ session-based edit (ดูหัวข้อ Iterative Edit) แทนการ generate ใหม่.

### M-06: Event/Webinar Promo
**Specs:** `style=flat design` หรือ `cinematic` · `aspectRatio=16:9` · `imageSize=2K`

```
Event promotional image for "[EVENT TITLE]" on [DATE], professional
conference aesthetic, [VISUAL THEME relating to topic]. Composition
allows speaker names + venue + CTA to be overlaid. [COLOR matching brand].
```

---

## Category 4: B2B / PROPOSAL (6 Patterns)

### B-01: Slide Hero — Section Cover
**Use:** Proposal Section, Chapter Opener
**Specs:** `style=isometric` หรือ `flat design` · `aspectRatio=16:9` · `imageSize=4K`

```
Slide section cover image about [SECTION TOPIC e.g., "Digital
Transformation"], abstract conceptual visualization combining [ELEMENT1]
+ [ELEMENT2], [BRAND COLOR PALETTE], generous negative space for slide title.
Professional, enterprise-grade.
```

### B-02: Concept Mockup — Customer Workshop
**Specs:** `style=illustration` · `aspectRatio=16:9` · `imageSize=2K`

```
Concept visualization for client workshop on [TOPIC], illustrated style
showing [SCENARIO], collaborative annotations style, ideation board feel.
Casual but informed, suitable for design sprint or strategy session.
```

### B-03: Process Diagram Style — Conceptual
**Specs:** `style=isometric` · `aspectRatio=16:9` · `imageSize=2K`

```
Conceptual illustration of [PROCESS/JOURNEY], isometric perspective showing
[STAGE1] -> [STAGE2] -> [STAGE3], connected by flow elements. Clean modern
style, [BRAND COLORS], suitable as Slide background to overlay specifics.
```

### B-04: Industry-themed Hero
**Variables for major industries (ใส่ใน `prompt`):**
- Financial Services: `secure vault aesthetic, blue palette, data visualization`
- Healthcare: `clinical clean, soft greens, human warmth`
- Manufacturing: `precision engineering, industrial metallic, blueprint blue`
- Public Sector: `dignified formal, civic colors, institutional aesthetic`
- Retail: `vibrant consumer, lifestyle warmth, brand-energetic`
- FinTech: `digital innovation, gradient purples/cyans, futuristic`

**Specs:** `style=cinematic` หรือ `flat design` · `aspectRatio=16:9` · `imageSize=4K`

```
B2B hero image for [INDUSTRY] proposal about [TOPIC], [INDUSTRY VARIABLES
ABOVE], professional gravitas. Room for headline text.
```

### B-05: Technology Conceptual
**Specs:** `style=3D render` หรือ `isometric` · `aspectRatio=16:9` · `imageSize=4K`

```
Conceptual visualization of [TECH e.g., "AI Agents", "Cloud Architecture",
"Data Pipeline"], abstract but recognizable, cool color palette, flowing
connections suggesting interoperability. Modern enterprise tech aesthetic,
not literal screenshots.
```

### B-06: Workshop Mood Board Item
**Specs:** `style=` (ตาม aesthetic ที่ต้องการ) · `aspectRatio=` (ตามการใช้งาน) · `imageSize=2K`

```
Mood board reference image for [WORKSHOP TOPIC], evocative not literal,
conveys [EMOTION/CONCEPT]. Used for kickstarting ideation, not final
deliverable.
```

---

## Pattern: Iterative Edit (สำคัญที่สุดเรื่อง Edit) — Session-based

> rlabs ใช้ **multi-turn session** ต่างจาก nanobanana เดิม (one-shot `mode=edit`).
> Workflow: `gemini-start-image-edit(prompt, aspectRatio, imageSize)` → ได้ภาพ base + `sessionId` → `gemini-continue-image-edit(sessionId, prompt)` ซ้ำได้กี่รอบก็ได้ → `gemini-end-image-edit(sessionId)` ปิดเมื่อพอใจ. ดู session ที่ค้างด้วย `gemini-list-image-sessions()`.

**ลำดับใช้งานจริง:**
1. `gemini-start-image-edit` ด้วย prompt ตั้งต้น (หรือ prompt ที่บรรยายภาพที่ต้องการเป็นจุดเริ่ม) → จด `sessionId`.
2. แต่ละ `gemini-continue-image-edit` ส่งเฉพาะ "การเปลี่ยนแปลงรอบนี้" — โมเดลจำ context ของ session ไว้แล้ว ไม่ต้องบรรยายทั้งภาพซ้ำ.
3. (เสริม) ระหว่างทางใช้ `gemini-analyze-image(imagePath, query)` ให้ Claude "เห็น" ภาพล่าสุดแล้วบอกว่ายังขาดอะไร → ป้อนคำสั่งแก้ที่แม่นขึ้นใน continue รอบถัดไป (loop iterate ที่ nanobanana ทำไม่ได้).
4. `gemini-end-image-edit(sessionId)` เมื่อจบงาน.

### Single-change Edit (ใช้ใน `continue-image-edit`)
```
Keep the [PRESERVE ELEMENTS] exactly as-is. Change only [SPECIFIC CHANGE].
Preserve composition, color temperature, and overall mood.
```

### Background Replacement
```
Replace the background with [NEW BACKGROUND DESCRIPTION]. Keep the subject
exactly as before, including pose, lighting on subject, and color. Blend
edges naturally with [LIGHTING DIRECTION matching new bg].
```

### Style Transfer
```
Apply the visual style of [STYLE DESCRIPTION] to this image. Preserve all
subject identities, poses, and composition. Only change rendering style:
color palette, brushwork, texture treatment.
```

### Add Element
```
Add [NEW ELEMENT] to the [LOCATION in image, e.g., "lower right"]. Match
lighting direction ([from where]), color temperature, and scale with the
existing scene. Cast natural shadow on [SURFACE].
```

### Remove Element
```
Remove [ELEMENT TO REMOVE]. Fill the area with [WHAT SHOULD BE THERE,
e.g., "continuation of the background pattern"]. Preserve everything else
exactly.
```

---

## Multi-element / Composition (Session-based)

> rlabs ไม่มี `input_image_path_1/2` multi-image แบบ nanobanana — ทำ composition ผ่าน **session edit ทีละชั้น** แทน: start จากฉาก/setting ก่อน แล้ว `continue` เพื่อ "เพิ่ม" subject/องค์ประกอบลงไป รอบต่อรอบ พร้อมสั่งให้ match lighting/scale.

```
Start: [DESCRIBE BASE SCENE/SETTING], [STYLE via param], [ASPECT RATIO].
Continue 1: Add [SUBJECT/ELEMENT] into the [LOCATION], matching the scene's
            lighting direction, color temperature, and scale. Natural shadow.
Continue 2: [FURTHER REFINEMENT / blend / color-grade to unify].
```
- ตรวจระหว่างชั้นด้วย `gemini-analyze-image` (query เช่น "does the added subject's lighting match the background?") เพื่อ iterate ก่อนปิด session.

---

## Negative-as-clause Library (image — เขียนใน `prompt`)

rlabs **ไม่มี** `negative_prompt` param สำหรับภาพ — แปลงเป็น "positive clause สั่งให้หลีกเลี่ยง" ต่อท้าย prompt:

| Use Case | Clause ต่อท้าย prompt |
|---|---|
| Photo | `clean image with no text, no watermark, no signature, no logo; sharp and high quality` |
| Logo | `flat vector only, no gradient, no 3D, no drop shadow, single subject, no text artifacts` |
| Product | `no human hand, no model, clean uncluttered background, no props, no reflections, no dust` |
| Portrait | `no text overlay, no watermark, single person only, natural symmetric features, well-formed hands` |
| Brand | `no competitor logos, no copyrighted characters, no recognizable real people` |
| Marketing | `safe-for-work, no politically sensitive or controversial imagery` |

> หมายเหตุ: `gemini-generate-video` (Veo) **ยังมี** `negativePrompt` param แยกของมันเอง — ใช้ได้เฉพาะกับ video tool ไม่ใช่ image.

---

## Thai-to-English Bridge Vocabulary

| ไทย | English | ใช้กับ Prompt / param |
|---|---|---|
| สวยหรู | luxurious, premium, high-end | "luxurious leather texture" |
| มินิมอล | minimalist, clean, simple | "minimalist composition" |
| อบอุ่น | warm, cozy, inviting | "warm cozy atmosphere" |
| น่าเชื่อถือ | trustworthy, professional, authoritative | "professional executive feel" |
| ทันสมัย | modern, contemporary, current | "contemporary design" |
| ดูแพง | premium-looking, upscale, refined | "upscale aesthetic" |
| สดใส | vibrant, bright, lively | "vibrant colors" |
| สงบ | serene, peaceful, tranquil | "serene atmosphere" |
| มีพลัง | energetic, dynamic, powerful | "dynamic composition" |
| ดิบ | raw, authentic, gritty | "raw authentic feel" |
| คมชัด | sharp, crisp, defined | "sharp focus, crisp details" |
| นุ่มนวล | soft, gentle, smooth | "soft diffused lighting" |
| ภาพถ่ายจริง | photorealistic | `style=photorealistic` |
| สีน้ำ | watercolor | `style=watercolor` |
| การ์ตูนญี่ปุ่น | anime | `style=anime` |
| ไอโซเมตริก | isometric | `style=isometric` |

---

*Cookbook นี้ map ตรงเข้า rlabs/gemini-mcp (`gemini-generate-image` + session edit + `gemini-analyze-image`). Style ทุก Pattern ส่งผ่าน param `style` แยก, ขนาดใช้ `imageSize` (1K/2K/4K), สัดส่วนใช้ `aspectRatio`. ไม่มี model_tier / negative_prompt (image) / output_path อีกต่อไป.*
