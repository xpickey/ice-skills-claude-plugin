# Prompt Cookbook — 30+ Production-grade Patterns

แต่ละ Pattern มี: **Use Case** + **Recommended Specs** + **Prompt Template** (ทั้งไทย+อังกฤษ พร้อม Variables) + **Variations**

## Universal Prompt Anatomy (ใช้ทุกครั้ง)

```
[Subject] + [Composition/Camera] + [Action/State] + [Setting/Location] +
[Lighting/Style] + [Mood/Atmosphere] + [Technical Specs]
+ negative_prompt: [Things to avoid]
```

**English Bridge Words (ใช้บ่อย):**
- Style: photorealistic, cinematic, illustration, watercolor, oil painting, anime, 3D render, isometric, flat design, pixel art
- Lighting: golden hour, blue hour, soft diffused, dramatic side-lit, rim light, studio softbox, neon, candlelight
- Composition: close-up, medium shot, wide shot, overhead, low angle, eye level, three-quarter view, rule of thirds, centered
- Mood: serene, energetic, melancholic, mysterious, joyful, professional, intimate, epic

---

## Category 1: PHOTOGRAPHY (10 Patterns)

### P-01: Portrait — Professional Headshot
**Use:** LinkedIn, About Page, Speaker Bio
**Specs:** `nb2`, `4:5`, `4k`

```
A professional headshot of [GENDER] [AGE] [PROFESSION] wearing [ATTIRE],
warm friendly smile, looking directly at camera. Soft studio lighting
with subtle rim light. Neutral gradient background ([COLOR1] to [COLOR2]).
Shallow depth of field, 85mm lens, photorealistic, magazine quality.
```
- Variables: GENDER, AGE, PROFESSION (e.g., "Asian male 40s executive"), ATTIRE ("navy business suit"), COLOR1/2 ("gray", "charcoal")
- Negative: `cluttered background, harsh shadows, no text, no logo`

### P-02: Product Photography — White Background
**Use:** E-commerce, Catalog, Spec Sheet
**Specs:** `nb2`, `1:1` or `3:4`, `4k`

```
Product photography of [PRODUCT], centered composition, clean pure white
background (#FFFFFF), soft three-point lighting, subtle ground shadow.
Sharp focus throughout, color accurate, commercial style, no reflections.
```
- Variables: PRODUCT ("ceramic coffee mug, beige color, matte finish")
- Negative: `cluttered scene, hand model, busy background`

### P-03: Product Photography — Lifestyle
**Use:** Marketing, Social Media, Hero Image
**Specs:** `nb2`, `16:9` or `4:5`, `4k`

```
Lifestyle product shot of [PRODUCT] in [SETTING], natural [TIME] lighting,
[MOOD] atmosphere. [HUMAN ELEMENT optional]. Authentic candid feel,
shallow depth of field, color-graded with [COLOR PALETTE].
```
- Variables: PRODUCT, SETTING ("scandinavian kitchen counter"), TIME ("morning golden hour"), MOOD ("calm, inviting"), COLOR PALETTE ("warm earth tones")

### P-04: Food Photography — Hero Dish
**Use:** Menu, Recipe, Restaurant Marketing
**Specs:** `nb2`, `1:1` or `4:5`, `4k`

```
Overhead food photography of [DISH] on [PLATE], styled with [GARNISH],
natural window light from the left, soft shadows, vibrant colors,
high-end restaurant aesthetic. Marble surface, minimal props.
```
- Variables: DISH ("seared salmon with asparagus"), PLATE ("matte black ceramic"), GARNISH ("lemon wedge, fresh dill")

### P-05: Architecture — Building Exterior
**Use:** Real Estate, Architecture Portfolio, Brand HQ
**Specs:** `nb2`, `16:9` or `21:9`, `4k`

```
Architectural photography of [BUILDING TYPE] in [LOCATION/STYLE],
[TIME] light, dramatic perspective from [ANGLE]. Clean lines emphasized,
sky [SKY CONDITION], minimal people. Wide-angle lens, color-corrected.
```
- Variables: BUILDING TYPE ("modern office tower"), LOCATION/STYLE ("Bangkok CBD glass curtain wall"), TIME ("blue hour"), ANGLE ("low angle hero shot"), SKY ("deep blue with thin clouds")

### P-06: Landscape — Cinematic
**Use:** Hero Banner, Inspiration Image, Slide Cover
**Specs:** `nb2` or `pro`, `21:9`, `4k`

```
Cinematic landscape of [LOCATION] during [TIME OF DAY], featuring
[FOREGROUND], [MIDGROUND], [BACKGROUND]. [WEATHER] adds atmosphere.
Composition follows rule of thirds, dramatic [COLOR PALETTE]
color grading, anamorphic lens flare. Inspiring, vast scale.
```
- Variables: LOCATION ("Northern Thailand mountain range"), TIME ("sunrise"), FOREGROUND ("morning mist over rice terraces"), WEATHER ("low fog"), COLOR ("warm amber and teal")

### P-07: Street Photography — Urban Story
**Use:** Editorial, Storytelling, Cultural Asset
**Specs:** `nb2`, `3:2`, `2k` or `4k`

```
Candid street photography in [CITY/DISTRICT], [SUBJECT] caught in [ACTION],
authentic moment. [LIGHTING] adds depth. 35mm lens, slight grain,
documentary style, Magnum Photos aesthetic.
```

### P-08: Macro — Texture/Detail
**Use:** Brand Storytelling, Product Detail, Texture Reference
**Specs:** `nb2`, `1:1`, `4k`

```
Macro photography of [SUBJECT], extreme close-up showing [TEXTURE DETAIL],
soft directional light revealing surface character. Shallow depth of field
with bokeh background, color-accurate, museum quality.
```

### P-09: Event Photography — Conference/Workshop
**Use:** Case Study, Marketing, Internal Comms
**Specs:** `nb2`, `3:2`, `2k`

```
Photojournalistic shot of [EVENT TYPE], [SCENE], natural mixed lighting
(ambient + warm spots), authentic engagement, no posed feeling.
Tasteful focus on [FOCAL ELEMENT], background context softly visible.
```

### P-10: Drone/Aerial
**Use:** Project Overview, Site Photo, Hero Banner
**Specs:** `nb2`, `21:9`, `4k`

```
Aerial drone photography of [LOCATION], overhead perspective at [ALTITUDE],
[TIME] light casting long shadows. [PATTERN/COMPOSITION FEATURE] creates
visual interest. Color-graded, sharp detail throughout.
```

---

## Category 2: DESIGN/BRAND (8 Patterns)

### D-01: Logo — Minimal Type
**Use:** Quick Logo Concept, Brand Variant
**Specs:** `nb2` or use Built-in `logo_text` template, `1:1`, `2k`

```
Minimalist logo design with the text "[BRAND NAME]", clean geometric
sans-serif typography, [COLOR] color, centered composition, pure white
background. Professional, modern, scalable. Vector-style flat design.
```
- Negative: `3D effects, gradients, decorative elements, multiple fonts`

### D-02: Logo — Icon + Wordmark
```
Logo combining a simple geometric icon ([ICON DESCRIPTION]) with the
wordmark "[BRAND NAME]" set in [TYPOGRAPHY STYLE]. [COLOR PALETTE].
Icon left of text, balanced spacing. White background.
```

### D-03: Icon Set — Consistent Style
**Use:** UI/UX, App Icons, Documentation
**Specs:** `nb2`, `1:1`, `2k`

```
Set of [N] icons in consistent [STYLE] style: [ICON1], [ICON2], [ICON3].
[COLOR] color on white background. Grid layout, uniform stroke width
([WEIGHT]), rounded corners, modern flat design.
```

### D-04: Pattern — Brand Background
```
Seamless tileable pattern featuring [MOTIFS] in [STYLE], [COLOR PALETTE],
geometric/organic [GEOMETRY], suitable for brand backgrounds. Subtle,
not distracting. Vector style.
```

### D-05: Mockup — Device/Print
**Use:** Pitch Deck, Portfolio, Concept Validation
**Specs:** `nb2`, varies, `4k`

```
Realistic mockup of [DEVICE/MEDIUM] displaying [SCREEN/DESIGN CONTENT],
[ENVIRONMENT SETTING], soft studio lighting with subtle shadow.
Photorealistic, high-fidelity, no UI overlays beyond the design itself.
```
- Variables: DEVICE ("MacBook Pro 16-inch open at 45-degree angle"), CONTENT ("dashboard with charts")

### D-06: Concept Sketch — Workshop/Whiteboard
**Use:** Design Sprint, Ideation, Workshop Output
**Specs:** `flash` (เร็ว), `4:3`, `1k`

```
Hand-drawn concept sketch on white paper of [CONCEPT], pencil and marker
style, casual ideation feel, annotation notes in handwriting, brainstorm
energy. Workshop board aesthetic.
```

### D-07: Sticker — Flat Design
**Use:** Marketing Asset, Social Sticker, Internal Fun
**Specs:** `nb2` or use Built-in `sticker_flat`, `1:1`, `1k`

```
Flat design sticker of [SUBJECT], bold outlines, [COLOR PALETTE],
playful style, transparent background, slight 3D shadow. Vector aesthetic,
suitable for product packaging or app stickers.
```

### D-08: Infographic Element
**Use:** Slide, Report, Social Post
**Specs:** `nb2`, `1:1` or `16:9`, `2k`

```
Infographic illustration of [CONCEPT], minimalist flat design, [COLOR
PALETTE matching brand], clean composition with [NUMBER] elements:
[ELEMENT1], [ELEMENT2], [ELEMENT3]. Clear visual hierarchy, no text
labels (will be added in post-production).
```

---

## Category 3: MARKETING/SOCIAL (6 Patterns)

### M-01: Hero Banner — Web Landing
**Specs:** `nb2`, `21:9` or `16:9`, `4k`

```
Hero banner image for [WEBSITE TOPIC], featuring [MAIN VISUAL ELEMENT],
[STYLE], [COLOR PALETTE matching brand]. Cinematic composition with
visual breathing room for headline text on the [LEFT/RIGHT/CENTER].
Engaging, professional, conversion-optimized aesthetic.
```

### M-02: Social Square — Instagram
**Specs:** `nb2`, `1:1`, `2k`

```
Instagram-style square post about [TOPIC], [STYLE], vibrant [COLOR],
attention-grabbing first second, central focal point. Suitable for
adding text overlay. Mobile-feed optimized.
```

### M-03: Story/Reel — Vertical
**Specs:** `nb2`, `9:16`, `2k`

```
Vertical 9:16 image for Instagram Story/Reel cover about [TOPIC],
[VISUAL ELEMENT], [MOOD], thumb-stopping aesthetic. Lower third reserved
for text overlay. Bold composition.
```

### M-04: YouTube Thumbnail
**Specs:** `nb2`, `16:9`, `2k`

```
YouTube thumbnail for "[VIDEO TITLE]" featuring [CENTRAL VISUAL] with
exaggerated [EMOTION/REACTION], bold contrasting colors ([COLOR1] vs
[COLOR2]), high visual impact, click-bait friendly composition. Space
for 3-5 word headline text overlay.
```

### M-05: Campaign Banner Series — Consistent
```
Series of [N] campaign banners, all featuring [CONSISTENT ELEMENT],
[COLOR PALETTE], same composition framework but different
[VARIATION DIMENSION e.g., season/product/audience]. Banner [N] focus:
[SPECIFIC FEATURE]. [ASPECT RATIO] format.
```

### M-06: Event/Webinar Promo
```
Event promotional image for "[EVENT TITLE]" on [DATE], professional
conference aesthetic, [VISUAL THEME relating to topic]. Composition
allows speaker names + venue + CTA to be overlaid. [COLOR matching brand].
```

---

## Category 4: B2B / PROPOSAL (6 Patterns)

### B-01: Slide Hero — Section Cover
**Use:** Proposal Section, Chapter Opener
**Specs:** `nb2`, `16:9`, `4k`

```
Slide section cover image about [SECTION TOPIC e.g., "Digital
Transformation"], abstract conceptual visualization combining [ELEMENT1]
+ [ELEMENT2], [STYLE e.g., "isometric", "minimal line art", "geometric
abstract"], [BRAND COLOR PALETTE], generous negative space for slide title.
Professional, enterprise-grade.
```

### B-02: Concept Mockup — Customer Workshop
```
Concept visualization for client workshop on [TOPIC], illustrated style
showing [SCENARIO], collaborative annotations style, ideation board feel.
Casual but informed, suitable for design sprint or strategy session.
```

### B-03: Process Diagram Style — Conceptual
```
Conceptual illustration of [PROCESS/JOURNEY], isometric perspective showing
[STAGE1] → [STAGE2] → [STAGE3], connected by flow elements. Clean modern
style, [BRAND COLORS], suitable as Slide background to overlay specifics.
```

### B-04: Industry-themed Hero
**Variables for major industries:**
- Financial Services: `secure vault aesthetic, blue palette, data visualization`
- Healthcare: `clinical clean, soft greens, human warmth`
- Manufacturing: `precision engineering, industrial metallic, blueprint blue`
- Public Sector: `dignified formal, civic colors, institutional aesthetic`
- Retail: `vibrant consumer, lifestyle warmth, brand-energetic`
- FinTech: `digital innovation, gradient purples/cyans, futuristic`

```
B2B hero image for [INDUSTRY] proposal about [TOPIC], [INDUSTRY VARIABLES
ABOVE], professional gravitas. 16:9, room for headline.
```

### B-05: Technology Conceptual
```
Conceptual visualization of [TECH e.g., "AI Agents", "Cloud Architecture",
"Data Pipeline"], abstract but recognizable, [STYLE], cool color palette,
flowing connections suggesting interoperability. Modern enterprise tech
aesthetic, not literal screenshots.
```

### B-06: Workshop Mood Board Item
```
Mood board reference image for [WORKSHOP TOPIC], evocative not literal,
[STYLE/AESTHETIC keyword], conveys [EMOTION/CONCEPT]. Used for kickstarting
ideation, not final deliverable. [ASPECT RATIO].
```

---

## Pattern: Iterative Edit (สำคัญที่สุดเรื่อง Edit)

ใช้กับ mode=edit + input_image_path_1

### Single-change Edit
```
Keep the [PRESERVE ELEMENTS] exactly as-is. Change only [SPECIFIC CHANGE].
Preserve composition, color temperature, and overall mood.
```

### Background Replacement
```
Replace the background with [NEW BACKGROUND DESCRIPTION]. Keep the subject
exactly as in the original, including pose, lighting on subject, and
color. Blend edges naturally with [LIGHTING DIRECTION matching new bg].
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

## Multi-image Composition (Pro Model)

ใช้ input_image_path_1 + input_image_path_2 (+ 3)

```
Combine image 1 (which shows [DESCRIBE IMG1]) with image 2 (which shows
[DESCRIBE IMG2]) such that [COMBINATION RULE, e.g., "the subject from
image 2 is placed in the setting of image 1 with matching lighting"].
Preserve [IMPORTANT PRESERVATION POINTS]. Final output: [ASPECT RATIO,
STYLE].
```

---

## Negative Prompt Library

ใช้ใน parameter `negative_prompt`:

| Use Case | Negative Prompt |
|---|---|
| Photo | `text, watermark, signature, logo, ugly, deformed, low quality, blurry` |
| Logo | `gradient, 3D, drop shadow, complex details, multiple subjects, text artifacts` |
| Product | `human hand, model, cluttered background, props, reflections, dust` |
| Portrait | `text overlay, watermark, multiple people, deformed hands, asymmetric eyes` |
| Brand | `competitor logos, copyrighted characters, recognizable real people without consent` |
| Marketing | `politically sensitive imagery, controversial elements, NSFW` |

---

## Thai-to-English Bridge Vocabulary

| ไทย | English | ใช้กับ Prompt |
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
