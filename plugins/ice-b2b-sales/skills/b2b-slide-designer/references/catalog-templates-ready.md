# Templates-Ready Catalog (ไฟล์ .pptx จริง — iCE internal library)

ไฟล์ template framework พร้อมใช้ **73 หมวด** (จาก iCE/800-Infographic) — เปิดดึง layout จริงไป build ต่อ.
ต่างจาก `catalog-infographics.md` (ชี้ URL inspiration) — อันนี้ **มี .pptx จริง** ที่เปิด+ดึง layout ได้เลย.

> **dedup:** เฉพาะหมวด**ไม่ซ้ำ** `catalog-infographics.md` (68 types) — ซ้ำใช้ของเดิมแกน.
> **internal iCE only** — commercial template, ไม่ redistribute.

## ⭐ Cache-on-Demand + Portability (เผื่อย้ายเครื่อง)

> **ปัญหา:** path ด้านล่างเป็น absolute (ผูกเครื่องนี้) — ย้ายเครื่อง/ลบไฟล์ = ชี้ไม่เจอ.
> **แก้:** 2-layer cache — binary ทยอยเก็บ (local) + metadata (portable, in git).

**Resolution order (ใช้ `scripts/template_cache.py get "<framework>"`):**
```
1. assets/templates-cache/<name>.pptx   — cache hit (เคยใช้แล้ว) → ใช้เลย
2. src_path (absolute ด้านล่าง)          — ต้นทางบนเครื่องนี้ → COPY เข้า cache (ทยอยเก็บ) + ใช้
3. ไม่มีทั้งคู่ → fallback graceful       — metadata บอก slide-count/หน้าตา → build จาก
                                            catalog-infographics (inspiration) หรือ MCP + แจ้ง user (ไม่ crash)
```

**2-layer cache:**
| ชั้น | เก็บอะไร | ที่ไหน | git | portable? |
|---|---|---|---|---|
| **Binary** | .pptx จริง (ทยอย copy ตอนใช้) | `assets/templates-cache/` | ❌ `.gitignore` | local-only (ไม่โต repo) |
| **Metadata** | slide-count + shapes + size + src_path | `references/templates-cache-meta.json` | ✅ in git | ✅ ข้ามเครื่องได้ |

**Migration (ย้ายเครื่อง):**
1. metadata (`templates-cache-meta.json`) ตามไปกับ git → เครื่องใหม่รู้ว่า template มีกี่ slide/หน้าตา
2. ถ้าย้าย `iCE/800 - Infographic/` ไปด้วย → `template_cache.py` หาเจอ (src_path เดิม) → copy ได้
3. ถ้าไม่ย้าย src → binary หาย แต่ **metadata ยังบอกโครงสร้าง** → build จาก inspiration ได้ (ไม่ crash)
4. **health-check:** `python scripts/template_cache.py check` → เช็คทั้ง 73 ว่ายังอยู่ไหม (รายงานตัวหาย)
5. *(ถ้า src ย้ายที่)* แก้ base-path ใน `templates-cache-meta.json` ครั้งเดียว → regenerate ด้วย `build_template_meta.py`

> **base path ปัจจุบัน:** `/Users/xpickey/Documents/iCE/800 - Infographic/` — ถ้าย้าย แก้ที่ metadata + catalog.
> ทุกไฟล์ verify เปิดได้ (>0 slides) ณ วันสร้าง catalog.

| Framework / หมวด | slides | .pptx full path | preview .pdf |
|---|---|---|---|
| **30 60 90 Day Plan** | 25 | `/Users/xpickey/Documents/iCE/800 - Infographic/30-60-90-day-plan/01 - Powerpoint/30 60 90 Days Plan.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/30-60-90-day-plan/Read Me - Font Link.pdf` |
| **Arrow Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Arrow Slides/01 - Arrow PowerPoint Slides/Presentation file/Arrow Powerpoint Template.pptx` | — |
| **Calendar 2021** | 61 | `/Users/xpickey/Documents/iCE/800 - Infographic/Calendar 2021/Calendar 2021 Google Slides/Presentation Files/Calendar 2021 Google Slidespptx.pptx` | — |
| **Challenges Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Challenges-Templates/01-Powerpoint-Challenges/Challenges Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Challenges-Templates/02-Keynote-Challenges/Read Me - Fonts Links.pdf` |
| **Chart Slides Rev** | 39 | `/Users/xpickey/Documents/iCE/800 - Infographic/Chart Slides rev/01 Powerpoint Slides/Presentation Files/Chart Slides Powerpoint Template.pptx` | — |
| **Cloud Slides Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Cloud-Slides-Templates/01-Powerpoint-Cloud/Cloud Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Cloud-Slides-Templates/02-Keynote-Cloud/Read Me - Fonts Links.pdf` |
| **Company Profile Slides** | 76 | `/Users/xpickey/Documents/iCE/800 - Infographic/Company Profile Slides/Company Profile PowerPoint Slides/Company Profile Powerpoint Template.pptx` | — |
| **Decision Slides** | 26 | `/Users/xpickey/Documents/iCE/800 - Infographic/Decision Slides/03 - Decision Tree Google Slides/Presentation file/Decision Tree Google Slides Template.pptx` | — |
| **Decision Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Decision-Templates/01-Powerpoint-Decision/Decision Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Decision-Templates/01-Powerpoint-Decision/Read Me - Fonts Links.pdf` |
| **Gantt Slides** | 8 | `/Users/xpickey/Documents/iCE/800 - Infographic/Gantt Slides/01 - Gantt PowerPoint Slides/Gantt Slides V4 Powerpoint Template/Presentation file/Gantt Slides V4 Powerpoint Template.pptx` | — |
| **Gap Analysis Template** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Gap-Analysis-Template/01-Powerpoint-Gap-Analysis/Gap Analysis.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Gap-Analysis-Template/02-Keynote-Gap-Analysis/Read Me - Fonts Links.pdf` |
| **Goals Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Goals Slides/03 - Goals Google Slides/Presentation File/Goals Google Slides Template.pptx` | — |
| **Iceberg Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Iceberg Slides/03 - Iceberg Google Slides/Presentation file/Iceberg Diagram Google Slides Template.pptx` | — |
| **Item** | 32 | `/Users/xpickey/Documents/iCE/800 - Infographic/Item/Waterfal Chart Powerpoint Slides 2/Presentation Files/Waterfall Chart Slides PowerPoint Template.pptx` | — |
| **Meeting Slides Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Meeting-Slides-Templates/01-Powerpoint-Meeting/Meeting Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Meeting-Slides-Templates/02-Keynote-Meeting/Read Me - Fonts Links.pdf` |
| **Milestones Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Milestones Slides/03 - Milestones Google Slides/Presentation File/Milestones Google Slides Template.pptx` | — |
| **Mind Map Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Mind-Map-Templates/01-Powerpoint-Mind-Map/Mind Map Infographics.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Mind-Map-Templates/02-Keynote-Mind-Map/Read Me - Fonts Links DM SANS.pdf` |
| **Mindmap Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Mindmap Slides/03 - Mindmap Google Slides/Presentation File/Mindmap Google Slides Template.pptx` | — |
| **Mockup Devices Templates** | 42 | `/Users/xpickey/Documents/iCE/800 - Infographic/Mockup-Devices-Templates/01-Powerpoint-Mockup-Devices/Mockup Devices.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Mockup-Devices-Templates/04-Illustrator-Mockup-Devices/Read Me - Fonts Links.pdf` |
| **Objective Slides Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Objective-Slides-Infographics/01 - Powerpoint/Objective Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Objective-Slides-Infographics/Read Me - Font Link.pdf` |
| **Pie Chart Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Pie Chart Slides/01 - Pie Chart PowerPoint Slides/Presentation File/Pie Chart Slides Powerpoint Template.pptx` | — |
| **Profit And Loss Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Profit and Loss Infographics/01 Powerpoint Template 2/Presentation/Profit and Loss Slides Powerpoint Template.pptx` | — |
| **Project Management Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Project Management Slides/03 - Project Management Google Slides/Project Management Slides Google Slides Template.pptx` | — |
| **Project Status Slides Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Project-Status-Slides-Templates/01-Powerpoint-Project-Status/Project Status.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Project-Status-Slides-Templates/02-Keynote-Project-Status/Read Me - Fonts Links.pdf` |
| **Question Templates** | 41 | `/Users/xpickey/Documents/iCE/800 - Infographic/Question-Templates/01-Powerpoint-Question/Questions Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Question-Templates/03-Google-Slides-Question/Questions Slides - S1 - Google Slides Link.pdf` |
| **Responsibility Assignment Matrix Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Responsibility-Assignment-Matrix-Templates/01-Powerpoint-Responsibility-Assignment-Matrix/Responsibility Assignment Matrix.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Responsibility-Assignment-Matrix-Templates/03-Google-Slides-Responsibility-Assignment-Matrix/Responsibility Assignment Matrix S1 - Google Slides Link.pdf` |
| **Swot Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/SWOT Slides/01 - SWOT PowerPoint Slides/Presentation file/SWOT Analysis Slides Powerpoint Template.pptx` | — |
| **Square Smart Art Posts For Powerpoint** | 202 | `/Users/xpickey/Documents/iCE/800 - Infographic/Square-Smart-Art-Posts-for-PowerPoint/PPTX/Smart Art Posts.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Square-Smart-Art-Posts-for-PowerPoint/Read Me - Fonts Links.pdf` |
| **Supply Chain Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Supply Chain Slides/03 - Supply Chain Google Slides/Presentation/Supply Chain Google Slides Template.pptx` | — |
| **Technology Infographics** | 32 | `/Users/xpickey/Documents/iCE/800 - Infographic/Technology Infographics/01 Powerpoint Template/Presentation/Technology Infographics Powerpoint Template.pptx` | — |
| **Theo Powerpoint Template** | 14 | `/Users/xpickey/Documents/iCE/800 - Infographic/Theo-Powerpoint-Template/Theo PowerPoint Template.pptx` | — |
| **Time Management Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Time-Management-Templates/01-Powerpoint-Time-Management/Time Management.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/Time-Management-Templates/03-Google-Slides-Time-Management/Time Management - S1 - Google Slides Link.pdf` |
| **Us Maps Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/US-Maps-Templates/01-Powerpoint-US-Maps/United States Maps.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/US-Maps-Templates/02-Keynote-US-Maps/Read Me - Fonts Links.pdf` |
| **Value Chain Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/Value Chain Infographics/01 Powerpoint Template/Presentation/Value Chain Slides Powerpoint Template.pptx` | — |
| **Worldwide Map** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/Worldwide Map/03 - World Map Google Slides/Presentation File/Worldmap Google Slides Template.pptx` | — |
| **Agile Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/agile-slides/Agile Powerpoint Slides/Presentation File/Agile Slides PowerPoint Template.pptx` | — |
| **Aida Model Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/aida-model-infographics/PPTX/AIDA Model Infographics.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/aida-model-infographics/GS/AIDA Model Infographics S1 - Google Slides.pdf` |
| **Artificial Intelligence** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/artificial-intelligence/PPTX/Artificial Intelligence Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/artificial-intelligence/Read Me - Fonts Links.pdf` |
| **Blue Ocean Strategy Rev** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/blue-ocean-strategy-rev/PPTX/Blue Ocean Strategy.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/blue-ocean-strategy-rev/GS/Blue Ocean Strategy S1 - Google Slides Link.pdf` |
| **Brain Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/brain-infographics/01 - Powerpoint/Brain Infographics.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/brain-infographics/Read Me - Fonts Links.pdf` |
| **Brain Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/brain-slides/Brain Google Slides/Brain Google Slides.pptx` | — |
| **Budget Slides** | 23 | `/Users/xpickey/Documents/iCE/800 - Infographic/budget-slides/Budget Powerpoint Slides/Budget Powerpoint Slides.pptx` | — |
| **Business Model Canvas** | 26 | `/Users/xpickey/Documents/iCE/800 - Infographic/business-model-canvas/PPTX/Business Model Canvas.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/business-model-canvas/Read Me - Fonts Links.pdf` |
| **Buyer Persona Slides** | 42 | `/Users/xpickey/Documents/iCE/800 - Infographic/buyer-persona-slides/01 - Powerpoint/Buyer Persona Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/buyer-persona-slides/Read Me - Fonts Links.pdf` |
| **Calendar Slides** | 61 | `/Users/xpickey/Documents/iCE/800 - Infographic/calendar-slides/Calendar Google Slides/Presentation Files/Calendar Google Slides .pptx` | — |
| **Circle Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/circle-slides/Circle Google Slides/Circle Google Slides.pptx` | — |
| **Credit Card Slide Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/credit-card-slide-infographics/01 - Powerpoint/Credit Card Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/credit-card-slide-infographics/Read Me - Font Link.pdf` |
| **Customer Journey Map Slides** | 24 | `/Users/xpickey/Documents/iCE/800 - Infographic/customer-journey-map-slides/Customer Journey Map Powerpoint Slides/Presentation File/Customer Journey Map PowerPoint Template.pptx` | — |
| **Cyber Security Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/cyber-security-slides/01 - Powerpoint/Cyber Security Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/cyber-security-slides/Read Me - Fonts Links.pdf` |
| **Digital Marketing Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/digital-marketing-slides/Digital Marketing Google Slides/Presentation Files/Digital Marketing Google Slides.pptx` | — |
| **Ecology Slides New** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/ecology-slides-new/01 - Powerpoint/Ecology Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/ecology-slides-new/Read Me - Fonts Links.pdf` |
| **Fitness Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/fitness-slides/Fitness Google Slides/Presentation Files/Fitness Google Slides.pptx` | — |
| **Flow Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/flow-slides/Flow Powerpoint Slides/Flow Powerpoint Slides.pptx` | — |
| **Manufacturing Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/manufacturing-slides/Manufacturing Powerpoint Slides 2/Presentation Files/Manufacturing Slides Powerpoint Template.pptx` | — |
| **Marketing Slides** | 63 | `/Users/xpickey/Documents/iCE/800 - Infographic/marketing-slides/Marketing Powerpoint Slides/Marketing Powerpoint Slides.pptx` | — |
| **Mckinsey 7S Model** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/mckinsey-7s-model/PPTX/McKinsey 7S Model.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/mckinsey-7s-model/GS/McKinsey 75 Model S1 - Google Slides Link.pdf` |
| **Medical Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/medical-infographics/01 - Powerpoint/Medical Infographics.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/medical-infographics/Read Me - Fonts Links.pdf` |
| **Office Scenes Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/office-scenes-slides/01 - Powerpoint/Office Scenes Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/office-scenes-slides/Read Me - Fonts Links.pdf` |
| **Pestel Templates** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/pestel-templates/01 - Powerpoint/PESTEL Analysis Slides S1.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/pestel-templates/Read Me - Font Link.pdf` |
| **Porter Five Forces** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/porter-five-forces/PPTX/Porter's Five Forces.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/porter-five-forces/Read Me - Fonts Links.pdf` |
| **Pricing Table Slides** | 27 | `/Users/xpickey/Documents/iCE/800 - Infographic/pricing-table-slides/Pricing Table Google Slides/Pricing Table Google Slides .pptx` | — |
| **Process Infographics S1** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/process-infographics-s1/01 - Powerpoint/Process Infographics.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/process-infographics-s1/Read Me - Fonts Links.pdf` |
| **Process Slides** | 32 | `/Users/xpickey/Documents/iCE/800 - Infographic/process-slides/Process Google Slides/Presentation Files/Process Google Slides.pptx` | — |
| **Product Roadmap Slides** | 32 | `/Users/xpickey/Documents/iCE/800 - Infographic/product-roadmap-slides/Product Roadmap Google Slides/Product Roadmap Google Slides.pptx` | — |
| **Puzzle Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/puzzle-slides/Puzzle Powerpoint Slides/Presentation Files/Puzzle Slides Powerpoint Template.pptx` | — |
| **Responsibility Assignment Matrix Rev** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/responsibility-assignment-matrix-rev/PPTX/Responsibility Assignment Matrix.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/responsibility-assignment-matrix-rev/GS/Responsibility Assignment Matrix S1 - Google Slides Link.pdf` |
| **Scrum Slides All Files** | 21 | `/Users/xpickey/Documents/iCE/800 - Infographic/scrum-slides-all-files/scrum-powerpoint/Presentation/SCRUM Powerpoint Template.pptx` | — |
| **Six Sigma Methodology** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/six-sigma-methodology/PPTX/Six Sigma Methodology.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/six-sigma-methodology/GS/Six Sigma Methodology S1 - Google Slides Link.pdf` |
| **Smile Rating Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/smile-rating-infographics/PPTX/Smile Rating Infographics.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/smile-rating-infographics/GS/Smile Rating Infographics S1 - Google Slides Link.pdf` |
| **Tables Of Content Infographics** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/tables-of-content-infographics/01 - Powerpoint/Tables of Content.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/tables-of-content-infographics/Read Me - Fonts Links.pdf` |
| **Thank You Slides** | 41 | `/Users/xpickey/Documents/iCE/800 - Infographic/thank-you-slides/PPTX/Thank You Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/thank-you-slides/Read Me - Fonts Links.pdf` |
| **Training Slides Rev** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/training Slides Rev/01 Powerpoint Slides 2/Presentation File/Training Powerpoint Slides.pptx` | — |
| **Work From Home Slides** | 22 | `/Users/xpickey/Documents/iCE/800 - Infographic/work-from-home-slides/01 - Powerpoint/Work From Home Slides.pptx` | `/Users/xpickey/Documents/iCE/800 - Infographic/work-from-home-slides/Read Me - Font Link.pdf` |

*Total: 73 หมวด · base: `/Users/xpickey/Documents/iCE/800 - Infographic/`*