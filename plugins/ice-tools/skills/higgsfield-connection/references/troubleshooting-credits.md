# Higgsfield — Troubleshooting & Credits

> Recovery scenarios สำหรับงาน Higgsfield ผ่าน MCP. แต่ละ scenario มี **อาการ / สาเหตุ / แก้**. ภาษาไทยเป็นหลัก, tool name คงภาษาอังกฤษ.
>
> **กฎทอง 2 ข้อ:**
> 1. ถ้า tool คืน field `recovery_tool` → เรียก tool นั้น **ทันที** (ดู Scenario G) — ไม่ต้องถาม/อธิบายก่อน.
> 2. งานแพง (video/upscale/train Soul) → `get_cost: true` preflight ก่อนเสมอ. credit ปัจจุบันเช็คด้วย `balance`.
>
> ราคา/เครดิตจริงต่อ model ไม่ระบุตายตัวที่นี่ — **เช็คด้วย `get_cost` / `balance` / `models_explore`** ทุกครั้ง.

## Table of Contents
- [Quick Triage — เริ่มจากตรงนี้](#quick-triage--เริ่มจากตรงนี้)
- [Scenario A — MCP ไม่ connect / ยังไม่ restart](#scenario-a--mcp-ไม่-connect--ยังไม่-restart)
- [Scenario B — auth expired / session หมดอายุ](#scenario-b--auth-expired--session-หมดอายุ)
- [Scenario C — เครดิตหมด / ไม่พอ](#scenario-c--เครดิตหมด--ไม่พอ)
- [Scenario D — job failed / ค้างใน queue](#scenario-d--job-failed--ค้างใน-queue)
- [Scenario E — media upload error (media_id ไม่ใช่ URL)](#scenario-e--media-upload-error-media_id-ไม่ใช่-url)
- [Scenario F — model param ผิด](#scenario-f--model-param-ผิด)
- [Scenario G — recovery_tool returned](#scenario-g--recovery_tool-returned)
- [Diagnostic Tool Map](#diagnostic-tool-map)

---

## Quick Triage — เริ่มจากตรงนี้

ดู signal ที่ได้ก่อน แล้วเด้งไป scenario:

```
ผลลัพธ์/Error
   │
   ├─ tool คืน field "recovery_tool"
   │     → Scenario G (เรียกทันที — สำคัญสุด)
   │
   ├─ tool ทั้ง suite ไม่โผล่ / "no such tool" / prefix UUID หาย
   │     → Scenario A (MCP connect / restart)
   │
   ├─ "unauthorized" / "401" / "session expired" / "token invalid" / "login required"
   │     → Scenario B (auth login)
   │
   ├─ "insufficient credit" / "not enough credit" / balance ต่ำกว่า cost
   │     → Scenario C (credit topup/auto_refill)
   │
   ├─ job status = failed / error / ค้าง processing เกินเวลา
   │     → Scenario D (retry / recovery)
   │
   ├─ "invalid media" / ใส่ URL ดิบใน medias[].value / media_id ไม่เจอ
   │     → Scenario E (upload → media_id)
   │
   └─ "invalid param" / "model not found" / "aspect_ratio not supported" / "role mismatch"
         → Scenario F (models_explore get)
```

---

## Scenario A — MCP ไม่ connect / ยังไม่ restart

**อาการ**
- เรียก tool แล้วได้ "no such tool" / tool ไม่อยู่ในรายการ.
- prefix UUID (`mcp__6473a427-...__`) หายไป หรือไม่มี tool ตัวไหนของ Higgsfield ขึ้นเลย.
- เพิ่งติดตั้ง/แก้ config แต่ tool ยังไม่ปรากฏ.

**สาเหตุ**
- ติดตั้ง MCP server แล้วแต่ยัง **ไม่ restart client** → server ยังไม่ถูก register.
- prefix UUID เปลี่ยนตาม session/install — โค้ดที่ hardcode prefix เดิมจะหา tool ไม่เจอ.
- config MCP ไม่ถูกต้อง / server crash ตอน start.

**แก้**
1. **Restart client ก่อน** (Claude Code / Claude app) — เกือบทุกเคส "ติดตั้งแล้ว tool ไม่โผล่" คือยังไม่ restart.
2. หลัง restart → ตรวจว่า tool โผล่ครบ. **อย่า hardcode prefix** — ดู prefix UUID จริงใน session ปัจจุบัน แล้วใช้ tool ตามชื่อหลัง prefix (เช่น `balance`, `generate_image`).
3. ตรวจว่า CLI ติดตั้งจริง:
   ```bash
   npm i -g @higgsfield/cli
   # หรือ
   brew install higgsfield-ai/tap/higgsfield
   # หรือ
   curl https://raw.githubusercontent.com/higgsfield-ai/cli/main/install.sh | sh
   # repo: github.com/higgsfield-ai/cli
   ```
4. Smoke test เร็ว ๆ หลัง connect: เรียก `balance` (ไม่มี params, ไม่เสียเครดิต) — ถ้าได้ค่า credit กลับมา = MCP + auth พร้อมใช้.
5. ถ้ายังไม่ขึ้น → ดู log ของ client, ตรวจ config path ของ MCP server, แล้ว restart อีกครั้ง.

---

## Scenario B — auth expired / session หมดอายุ

**อาการ**
- tool คืน "unauthorized" / "401" / "session expired" / "token invalid" / "please login".
- เคยใช้งานได้ปกติ แต่จู่ ๆ ทุก tool เริ่ม fail พร้อมกัน.

**สาเหตุ**
- Higgsfield ใช้ **token-based session อายุสั้น** — ต้อง re-auth เป็นระยะ.
- session หมดอายุระหว่างใช้งาน → tool ที่ต้อง auth (generate / balance / media) เด้ง unauthorized.

**แก้**
1. Re-login ผ่าน CLI:
   ```bash
   higgsfield auth login
   ```
   ทำตาม flow (browser/token) จน login สำเร็จ.
2. กลับมาเรียก `balance` ยืนยันว่า auth กลับมาแล้ว (ได้ credit = ผ่าน).
3. ถ้า tool คืน `recovery_tool` ที่เกี่ยวกับ auth → เรียก recovery_tool นั้นทันที (Scenario G) ก่อนจะไปสั่ง CLI เอง.
4. **ป้องกัน:** session อายุสั้นเป็นเรื่องปกติ — ถ้างานยาว เจอ unauthorized กลางทาง อย่าตกใจ, แค่ `higgsfield auth login` ใหม่แล้วทำต่อ. งานที่ค้าง (job_id ที่ submit ไปแล้ว) ยังอยู่ — poll ต่อด้วย status tool ได้หลัง re-auth.

---

## Scenario C — เครดิตหมด / ไม่พอ

**อาการ**
- tool คืน "insufficient credit" / "not enough credit" / "credit balance too low".
- `get_cost` บอก cost สูงกว่าที่ `balance` มี.
- generate fail ทันทีโดยไม่เริ่มประมวลผล.

**สาเหตุ**
- Higgsfield เป็นระบบ **credit-based** (ไม่ใช่ API key / ไม่ใช่ quota รายนาที) — credit หมดก็สั่งงานไม่ได้.
- งานแพง (video / upscale / virality / train Soul) กิน credit เยอะ — สั่งโดยไม่ preflight แล้ว balance ไม่พอ.

**แก้**
1. **Preflight ก่อนสั่งจริง** — ใส่ `get_cost: true` ใน `generate_image` / `generate_video` / `generate_audio` → คืน cost (credit) โดยไม่สั่งงานจริง. เทียบกับ `balance`.
2. เช็ค balance ปัจจุบัน:
   - `balance` → credit + plan ปัจจุบัน.
   - `transactions` → ประวัติการใช้/เติม credit.
3. เมื่อ credit หมด/ไม่พอ → เปิด pricing widget ด้วย:
   ```
   show_plans_and_credits(intent='topup')        # เติม credit
   show_plans_and_credits(intent='auto_refill')  # ตั้ง auto-refill กัน credit หมดกลางงาน
   show_plans_and_credits(intent='upgrade')      # อัปเกรด plan
   ```
   ผู้ใช้ดำเนินการเติม/อัปเกรดใน widget เอง.
4. หลังเติม → เรียก `balance` ยืนยัน credit เพิ่มแล้ว ค่อยสั่งงานต่อ.

> ราคา/credit ต่อ model ไม่ fix ที่นี่ — **เช็คด้วย `get_cost` ทุกงานแพง** และดู `balance` ก่อนเริ่ม.

---

## Scenario D — job failed / ค้างใน queue

**อาการ**
- งาน async (video / upscale / virality / video_analysis) คืน job/queued แล้ว status = `failed` / `error`.
- poll แล้วค้าง `processing` นานเกินคาด (video ปกติ ~3-5 นาที).

**สาเหตุ**
- งาน async ฝั่ง server fail (prompt ติด policy, model error, resource ชั่วคราว).
- poll เร็ว/ถี่เกินไป หรือเข้าใจผิดว่ายังไม่เสร็จทั้งที่ยังอยู่ในช่วงเวลาปกติ.
- input ไม่ครบ (เช่น `upscale_video` provider `bytedance` ต้องมี width/height/fps).

**แก้**
1. ถ้า response มี field `recovery_tool` → **เรียกทันที** (Scenario G) — มักเป็น retry/recovery ที่ถูกต้องที่สุด.
2. ตรวจ status ด้วย tool ที่ตรงประเภทงาน แล้ว poll เป็นระยะ (อย่ารอ block):
   | งาน | poll ด้วย |
   |---|---|
   | video generation | ดู job ด้วย `job_display(job_id)` |
   | video_analysis | `video_analysis_status(video_analyze_id)` (เสร็จ ~3-5 นาที) |
   | virality | `virality_predictor(action='preview', job_id=...)` |
   | personal clipper | `personal_clipper_status(...)` / `personal_clipper_jobs` |
3. ถ้า failed จริง → อ่าน error message:
   - ติด content policy → ปรับ prompt แล้วสั่งใหม่.
   - input ไม่ครบ → ดู Scenario F (`models_explore action='get'`) เช็ค required params แล้ว resubmit.
   - resource ชั่วคราว → retry งานเดิม.
4. **อย่าสั่งซ้ำรัว ๆ** ระหว่างที่ job ยังอยู่ในเวลาปกติ — เปลือง credit. รอ poll ให้ครบช่วงก่อน (video ~3-5 นาที).
5. ระหว่างรอ → แจ้งผู้ใช้ว่ากำลังประมวลผล + poll ให้ ไม่ทิ้งให้ค้าง.

---

## Scenario E — media upload error (media_id ไม่ใช่ URL)

**อาการ**
- tool คืน "invalid media" / "media not found" / "expected media_id".
- ใส่ลิงก์รูป/วิดีโอตรง ๆ ใน `medias[].value` แล้ว fail.

**สาเหตุ**
- `medias[].value` ต้องเป็น **media_id หรือ job_id** เท่านั้น — **ห้ามใส่ URL ดิบ**.
- ยังไม่ได้ upload/import ไฟล์ให้กลายเป็น media_id ก่อนใช้.

**แก้**
1. แปลงไฟล์/URL → media_id ก่อนเสมอ:
   | input | ใช้ tool |
   |---|---|
   | ไฟล์ local | `media_upload_widget` (เปิด widget ให้ผู้ใช้เลือกไฟล์) → ได้ media_id |
   | upload โดยตรง | `media_upload` → คืน media_id |
   | web URL | `media_import_url` → URL กลายเป็น media_id |
   | ยืนยันหลัง upload | `media_confirm` (ถ้า flow ต้องการ) |
2. เอา **media_id** ที่ได้ไปใส่ใน `medias[].value` (ไม่ใช่ URL):
   ```json
   { "medias": [ { "value": "<media_id>", "role": "start_image" } ] }
   ```
3. `medias[].role` ต่างกันตาม model (เช่น start_image / end_image / image / reference) — เช็ค role ที่ model รับด้วย `models_explore(action='get', model_id='...')` (Scenario F).
4. ถ้าจะ chain งาน (เอา output ของ job หนึ่งไปเป็น input อีกงาน) → ใช้ **job_id** ใน `medias[].value` ได้เลย ไม่ต้อง download/re-upload.

---

## Scenario F — model param ผิด

**อาการ**
- "model not found" / "invalid model".
- "aspect_ratio not supported" / "duration out of range" / "role mismatch" / "missing required param".
- generate fail เพราะ param ไม่ตรงกับที่ model นั้นรับ.

**สาเหตุ**
- เดา model name / aspect_ratio / duration / medias role เอง โดยไม่เช็ค constraint จริง.
- model catalog เปลี่ยนได้ — ชื่อ/ข้อจำกัด model ไม่ใช่ค่าตายตัว.
- ใส่ provider-specific key ที่ model ไม่รับ (เช่น generate_audio ห้ามใส่ text/seed/num_samples/ambience).

**แก้**
1. ดู constraint จริงของ model ก่อนสั่ง:
   ```
   models_explore(action='get', model_id='<model>')
   ```
   → คืน aspect_ratio ที่รองรับ, duration range, medias roles, params ที่จำเป็น.
2. ไม่รู้จะใช้ model ไหน → ค้น/ให้แนะนำ:
   ```
   models_explore(action='list', type='image')       # ดู catalog
   models_explore(action='search', query='...', type='video')
   models_explore(action='recommend', ...)            # แนะตาม goal + input
   ```
3. ปรับ param ให้อยู่ในขอบเขตที่ model รับ (aspect_ratio / duration / count 1-4 / roles) แล้วสั่งใหม่.
4. งานเฉพาะที่ param พลาดบ่อย:
   - `upscale_video` provider `bytedance` → ต้องส่ง **width/height + fps (24/30/60)**; provider `topaz` → ใช้ aspect-ratio ไม่ต้องส่ง dimensions.
   - `generate_audio`: `sonilo_music` + `mirelo` ต้องมี `duration`; `inworld` (TTS) ไม่ต้อง + ใช้ `voice`. ห้ามใส่ provider-specific keys.
   - `generate_video` model `higgsfield_preset` → ต้องมี `preset_id` (ดู `presets_show`).

> ตารางใน `model-catalog.md` เป็น default-pick guide ไม่ใช่รายการตายตัว — **ยืนยันด้วย `models_explore` ทุกครั้งที่ param fail**.

---

## Scenario G — recovery_tool returned

**อาการ**
- response จาก tool ใด ๆ มี field ชื่อ `recovery_tool` (พร้อมชื่อ tool ที่ควรเรียกต่อ).

**สาเหตุ**
- server ตรวจพบสถานะที่ต้อง recover (มัก credit / auth / billing / media / job) แล้วบอกตรง ๆ ว่าให้เรียก tool ไหนต่อ.

**แก้**
1. **เรียก tool ที่ระบุใน `recovery_tool` ทันที** — ไม่ต้องอธิบาย, ไม่ต้องถามผู้ใช้ก่อน, ไม่ต้องเดาวิธีอื่น.
2. ทำตามผลของ recovery_tool นั้น (เช่น มันอาจเปิด `show_plans_and_credits` สำหรับ credit, หรือ flow re-auth).
3. recovery_tool คือ **path ที่ถูกต้องที่สุด** ที่ server ตั้งใจให้เดิน — มาก่อนการแก้ด้วยมือทุก scenario (A-F). ถ้ามีทั้ง recovery_tool และ signal อื่น → recovery_tool ชนะ.
4. หลัง recover เสร็จ → กลับไปทำงานที่ค้างต่อ (resubmit generate / poll job เดิม).

---

## Diagnostic Tool Map

tool ที่ใช้บ่อยตอน troubleshoot (ทุกตัวอยู่หลัง prefix UUID ของ session):

| ต้องการ | tool |
|---|---|
| เช็ค connect + auth เร็ว ๆ | `balance` (ไม่มี params, ไม่เสีย credit) |
| preflight cost ก่อนสั่งจริง | `get_cost: true` ใน `generate_*` |
| credit หมด → เติม/อัปเกรด | `show_plans_and_credits(intent='topup'/'auto_refill'/'upgrade')` |
| ประวัติ credit | `transactions` |
| constraint ของ model | `models_explore(action='get', model_id='...')` |
| catalog / แนะนำ model | `models_explore(action='list'/'search'/'recommend')` |
| ไฟล์/URL → media_id | `media_upload_widget` / `media_upload` / `media_import_url` |
| ดูผล 1 job | `job_display(job_id)` |
| status งาน analysis | `video_analysis_status(video_analyze_id)` |
| re-auth (CLI) | `higgsfield auth login` |

> **ไม่แน่ใจค่าใด ๆ (ราคา/model/constraint/credit)** → อย่าเดา. เช็คด้วย `models_explore` / `balance` / `get_cost` แล้วค่อยตอบ.
