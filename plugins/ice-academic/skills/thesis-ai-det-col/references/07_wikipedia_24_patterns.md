# 24 AI Writing Patterns (Wikipedia "Signs of AI Writing")

## When to Read This

อ่านเมื่อทำ Mode 1 (DETECT) ในขั้น Layer 1 (Vocabulary Footprints) หรือ Mode 3 (CORRECT) Pass 2 — โดยเฉพาะเมื่อข้อความมีภาษาอังกฤษหรือต้องการตรวจ patterns ที่ครอบคลุมกว่า Verified AI Signature List ของไทย

**Source of Truth:** [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) maintained by WikiProject AI Cleanup — จากการสังเกตหลายพันกรณีของ AI-generated text บน Wikipedia ทั่วโลก

> **Key insight:** "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

---

## Index of 24 Patterns

| # | Pattern | Category | Severity |
|---|---|---|---|
| 1 | Inflated symbolism / Significance | Content | 🔴 High |
| 2 | Notability name-dropping | Content | 🟠 Medium |
| 3 | Superficial "-ing" analyses | Content | 🔴 High |
| 4 | Promotional language | Content | 🔴 High |
| 5 | Vague attributions / Weasel words | Content | 🔴 High |
| 6 | Formulaic "Challenges & Future Prospects" | Content | 🟠 Medium |
| 7 | Overused AI vocabulary | Language | 🔴 High |
| 8 | Copula avoidance (serves as / stands as) | Language | 🟠 Medium |
| 9 | Negative parallelisms ("It's not just X, it's Y") | Language | 🟠 Medium |
| 10 | Rule of three overuse | Language | 🟠 Medium |
| 11 | Elegant variation / Synonym cycling | Language | 🟢 Low |
| 12 | False ranges ("from X to Y") | Language | 🟢 Low |
| 13 | Em dash overuse | Style | 🟠 Medium |
| 14 | Boldface overuse | Style | 🟠 Medium |
| 15 | Inline-header vertical lists | Style | 🟠 Medium |
| 16 | Title Case headings | Style | 🟢 Low |
| 17 | Emoji decoration | Style | 🟢 Low |
| 18 | Curly quotation marks | Style | 🟢 Low |
| 19 | Chatbot artifacts ("I hope this helps") | Communication | 🔴 High |
| 20 | Knowledge-cutoff disclaimers | Communication | 🔴 High |
| 21 | Sycophantic tone ("Great question!") | Communication | 🔴 High |
| 22 | Filler phrases ("in order to") | Filler | 🟠 Medium |
| 23 | Excessive hedging | Filler | 🟠 Medium |
| 24 | Generic positive conclusions | Filler | 🟠 Medium |

---

## CONTENT PATTERNS (1-6)

### Pattern 1: Inflated Symbolism / Significance

**Words to watch:**
- *English:* stands/serves as, is a testament/reminder, a vital/significant/crucial/pivotal/key role/moment, underscores/highlights its importance/significance, reflects broader, symbolizing its ongoing/enduring/lasting, contributing to the, setting the stage for, marking/shaping the, represents/marks a shift, key turning point, evolving landscape, focal point, indelible mark, deeply rooted
- *ภาษาไทย:* "เป็นสัญลักษณ์ของ", "นับเป็นจุดเปลี่ยนสำคัญ", "สะท้อนถึงการเปลี่ยนแปลงครั้งใหญ่", "เป็นเครื่องหมายแห่ง", "ทิ้งรอยประทับอันลึกซึ้ง"

**Problem:** LLMs puff up importance by adding statements about how arbitrary aspects "represent" or "contribute to" a broader topic.

**Before:**
> The Statistical Institute of Catalonia was officially established in 1989, marking a pivotal moment in the evolution of regional statistics in Spain.

**After:**
> The Statistical Institute of Catalonia was established in 1989 to collect regional statistics independently from Spain's national statistics office.

### Pattern 2: Notability Name-Dropping

**Words to watch:** independent coverage, local/regional/national media outlets, written by a leading expert, active social media presence, cited in [list of outlets]

**Before:**
> Her views have been cited in The New York Times, BBC, Financial Times, and The Hindu. She maintains an active social media presence with over 500,000 followers.

**After:**
> In a 2024 New York Times interview, she argued that AI regulation should focus on outcomes rather than methods.

### Pattern 3: Superficial "-ing" Analyses

**Words to watch:**
- *English:* highlighting/underscoring/emphasizing, ensuring, reflecting/symbolizing, contributing to, cultivating/fostering, encompassing, showcasing
- *ภาษาไทย:* "ส่งเสริมให้", "สะท้อนถึง", "ก่อให้เกิด", "นำไปสู่การ", "เน้นย้ำถึง"

**Problem:** AI tacks present participle ("-ing") phrases onto sentences to add fake depth. The phrases sound deep but say little.

**Before:**
> The temple's color palette of blue, green, and gold resonates with the region's natural beauty, symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes, reflecting the community's deep connection to the land.

**After:**
> The temple uses blue, green, and gold colors. The architect said these were chosen to reference local bluebonnets and the Gulf coast.

### Pattern 4: Promotional / Advertisement Language

**Words to watch:** boasts a, vibrant, rich (figurative), profound, enhancing its, showcasing, exemplifies, commitment to, natural beauty, nestled, in the heart of, groundbreaking (figurative), renowned, breathtaking, must-visit, stunning

**ภาษาไทย:** "ตั้งอยู่ใจกลาง", "งดงามตระการตา", "เลื่องชื่อ", "ขึ้นชื่อในเรื่อง", "เพียบพร้อม", "อันทรงคุณค่า"

**Problem:** LLMs struggle to keep neutral tone, especially for "cultural heritage" topics — sounds like tourist brochure.

**Before:**
> Nestled within the breathtaking region of Gonder in Ethiopia, Alamata Raya Kobo stands as a vibrant town with a rich cultural heritage and stunning natural beauty.

**After:**
> Alamata Raya Kobo is a town in the Gonder region of Ethiopia, known for its weekly market and 18th-century church.

### Pattern 5: Vague Attributions / Weasel Words

**Already covered in `06_verified_ai_signatures.md`:**
- "Industry reports", "Observers have cited", "Experts argue", "Some critics argue"
- "งานวิจัยพบว่า" (without citation), "ผู้เชี่ยวชาญหลายท่านชี้ว่า"

### Pattern 6: Formulaic "Challenges and Future Prospects" Sections

**Words to watch:** Despite its... faces several challenges..., Despite these challenges, Challenges and Legacy, Future Outlook

**Problem:** Many LLM-generated articles include formulaic "Challenges" sections that follow a "Despite X, Y continues to thrive" template.

**Before:**
> Despite its industrial prosperity, Korattur faces challenges typical of urban areas, including traffic congestion and water scarcity. Despite these challenges, with its strategic location and ongoing initiatives, Korattur continues to thrive as an integral part of Chennai's growth.

**After:**
> Traffic congestion increased after 2015 when three new IT parks opened. The municipal corporation began a stormwater drainage project in 2022 to address recurring floods.

---

## LANGUAGE PATTERNS (7-12)

### Pattern 7: Overused AI Vocabulary (covered in `06_verified_ai_signatures.md`)

### Pattern 8: Copula Avoidance

**Problem:** LLMs substitute elaborate constructions for simple "is/are/has".

**Words to watch:**
- *English:* serves as / stands as / marks / represents [a], boasts / features / offers [a]
- *ภาษาไทย:* "เป็นเครื่องหมาย", "เป็นภาพแทน", "ทำหน้าที่เป็น", "นับเป็น"

**Before:**
> Gallery 825 serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces and boasts over 3,000 square feet.

**After:**
> Gallery 825 is LAAA's exhibition space for contemporary art. The gallery has four rooms totaling 3,000 square feet.

### Pattern 9: Negative Parallelisms

**Problem:** Constructions like "Not only X but Y" or "It's not just X, it's Y" overused for cheap dramatic effect.

**Words to watch:**
- *English:* "It's not just / merely / only X, it's Y", "Not only X but Y"
- *ภาษาไทย:* "ไม่เพียงแค่...แต่ยัง", "ไม่ใช่แค่...แต่เป็น", "มิเพียง...แต่ยัง"

**Before:**
> It's not just about the beat riding under the vocals; it's part of the aggression and atmosphere. It's not merely a song, it's a statement.

**After:**
> The heavy beat adds to the aggressive tone.

### Pattern 10: Rule of Three Overuse (covered in `01_three_layer_detection.md`)

### Pattern 11: Elegant Variation / Synonym Cycling

**Problem:** AI's repetition penalty causes excessive synonym substitution that reads as forced variety.

**Before:**
> The protagonist faces many challenges. The main character must overcome obstacles. The central figure eventually triumphs. The hero returns home.

**After:**
> The protagonist faces many challenges but eventually triumphs and returns home.

### Pattern 12: False Ranges

**Problem:** LLMs use "from X to Y" constructions where X and Y aren't on a meaningful scale.

**Before:**
> Our journey through the universe has taken us from the singularity of the Big Bang to the grand cosmic web, from the birth and death of stars to the enigmatic dance of dark matter.

**After:**
> The book covers the Big Bang, star formation, and current theories about dark matter.

---

## STYLE PATTERNS (13-18)

### Pattern 13: Em Dash Overuse (covered in Two-Pass Method)

### Pattern 14: Boldface Overuse

**Problem:** AI emphasizes phrases in boldface mechanically — every "key term" gets bolded, killing the visual hierarchy.

**Before:**
> It blends **OKRs (Objectives and Key Results)**, **KPIs (Key Performance Indicators)**, and visual strategy tools such as the **Business Model Canvas (BMC)** and **Balanced Scorecard (BSC)**.

**After:**
> It blends OKRs, KPIs, and visual strategy tools like the Business Model Canvas and Balanced Scorecard.

### Pattern 15: Inline-Header Vertical Lists

**Problem:** AI outputs lists where items start with bolded header followed by colon — looks structured but is bullet-point thinking in disguise.

**Before:**
> - **User Experience:** The user experience has been significantly improved with a new interface.
> - **Performance:** Performance has been enhanced through optimized algorithms.
> - **Security:** Security has been strengthened with end-to-end encryption.

**After:**
> The update improves the interface, speeds up load times through optimized algorithms, and adds end-to-end encryption.

### Pattern 16: Title Case in Headings

**Problem:** AI capitalizes all main words in headings, even in contexts where sentence case is conventional.

**Before:**
> ## Strategic Negotiations And Global Partnerships

**After:**
> ## Strategic negotiations and global partnerships

### Pattern 17: Emoji Decoration

**Problem:** AI decorates headings or bullet points with emojis mechanically.

**Before:**
> 🚀 **Launch Phase:** The product launches in Q3
> 💡 **Key Insight:** Users prefer simplicity
> ✅ **Next Steps:** Schedule follow-up meeting

**After:**
> The product launches in Q3. User research showed a preference for simplicity. Next step: schedule a follow-up meeting.

### Pattern 18: Curly Quotation Marks

**Problem:** ChatGPT uses curly quotes ("...") instead of straight quotes ("..."). In Thai academic writing, curly quotes are sometimes used but inconsistently — pure straight quotes is standard for technical documents.

**Before:** He said "the project is on track" but others disagreed.
**After:** He said "the project is on track" but others disagreed.

---

## COMMUNICATION PATTERNS (19-21)

### Pattern 19: Collaborative / Chatbot Artifacts

**Problem:** Text meant as chatbot correspondence gets pasted as content.

**Words to watch:** "I hope this helps", "Of course!", "Certainly!", "You're absolutely right!", "Would you like...", "let me know", "here is a..."

**Thai equivalent:** "หวังว่าคำตอบนี้จะเป็นประโยชน์", "แน่นอนครับ", "ตามที่ท่านสอบถาม", "ดังที่ท่านได้กล่าวมา"

**Before:**
> Here is an overview of the French Revolution. I hope this helps! Let me know if you'd like me to expand on any section.

**After:**
> The French Revolution began in 1789 when financial crisis and food shortages led to widespread unrest.

### Pattern 20: Knowledge-Cutoff Disclaimers

**Words to watch:** "as of [date]", "Up to my last training update", "While specific details are limited / scarce...", "based on available information..."

**Thai:** "เท่าที่ข้อมูลที่มีในปัจจุบัน", "ตามข้อมูลที่ทราบ", "หากข้อมูลเป็นปัจจุบัน"

**Before:**
> While specific details about the company's founding are not extensively documented in readily available sources, it appears to have been established sometime in the 1990s.

**After:**
> The company was founded in 1994, according to its registration documents.

### Pattern 21: Sycophantic / Servile Tone

**Problem:** Overly positive, people-pleasing language.

**Before:**
> Great question! You're absolutely right that this is a complex topic. That's an excellent point about the economic factors.

**After:**
> The economic factors you mentioned are relevant here.

---

## FILLER AND HEDGING PATTERNS (22-24)

### Pattern 22: Filler Phrases (ดูตารางใน `09_filler_replacement_table.md`)

### Pattern 23: Excessive Hedging

**Problem:** Over-qualifying statements with stacked hedges.

**Before:** "It could potentially possibly be argued that the policy might have some effect on outcomes."
**After:** "The policy may affect outcomes."

### Pattern 24: Generic Positive Conclusions

**Problem:** Vague upbeat endings that say nothing.

**Words to watch:** "the future looks bright", "exciting times lie ahead", "a major step in the right direction", "ก้าวสำคัญสู่อนาคต", "เปิดศักราชใหม่"

**Before:**
> The future looks bright for the company. Exciting times lie ahead as they continue their journey toward excellence. This represents a major step in the right direction.

**After:**
> The company plans to open two more locations next year.

---

## Severity Triage

When running detection:

🔴 **High severity (must fix):** Patterns 1, 3, 4, 5, 7, 19, 20, 21
🟠 **Medium severity (recommended fix):** Patterns 2, 6, 8, 9, 10, 13, 14, 15, 22, 23, 24
🟢 **Low severity (cosmetic):** Patterns 11, 12, 16, 17, 18

In Thai academic writing, prioritize 🔴 High severity patterns first — they signal AI most strongly to readers and detectors alike.

---

## Reference

This file integrates patterns from [Wikipedia:Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) (WikiProject AI Cleanup), adapted for Thai academic context where applicable. Patterns observed across thousands of AI-generated edits since GPT-3.5 release in late 2022.
