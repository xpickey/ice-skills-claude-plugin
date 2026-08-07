# NetSuite REST Web Services — Record API Reference (Pointer + Mapping)

> Companion to `records.json` (SuiteScript). This file covers the **REST Record
> Service (SuiteTalk REST Web Services)** — a *different API surface* from
> SuiteScript. It is a **pointer + mapping reference**, not a frozen field dump:
> for exact, current field-level schema always consult the authoritative
> REST API Browser or the account's live metadata-catalog (see below).
>
> Added locally to extend the Oracle-authored skill · scope: pointer/mapping only.

---

## Authoritative Source (version-aware)

The canonical human-readable reference is the **NetSuite REST API Browser**:

```
https://system.netsuite.com/help/helpcenter/en_US/APIs/REST_API_Browser/record/v1/<RELEASE>/index.html
```

- Captured target: **`record/v1/2024.2`** (NetSuite 2024 Release 2).
- To view a different release, swap the `<RELEASE>` segment (e.g. `2025.1`, `2025.2`).
- The Browser is a single-page app that renders an OpenAPI 3.0 spec — it must be
  opened in a browser; a plain HTTP fetch returns only the shell.

**Machine-readable equivalent (per account, always current):** the metadata-catalog
endpoint returns the same schema as OpenAPI 3.0 / JSON Schema — see *Metadata Catalog* below.

---

## Endpoint Pattern

Base host (per account):

```
https://<ACCOUNT_ID>.suitetalk.api.netsuite.com/services/rest/record/v1/
```

- `<ACCOUNT_ID>` is the lowercased account id; sandbox uses a suffix, e.g.
  `1234567-sb1.suitetalk.api.netsuite.com`. Confirm the exact host in
  **Setup > Company > Company Information > Company URLs** (do not guess it).

| Operation | Method & Path |
|-----------|---------------|
| List / search a record type | `GET  /record/v1/{recordType}` |
| Get one record | `GET  /record/v1/{recordType}/{id}` |
| Create | `POST /record/v1/{recordType}` |
| Update (partial) | `PATCH /record/v1/{recordType}/{id}` |
| Upsert by external id | `PUT  /record/v1/{recordType}/eid:{externalId}` |
| Delete | `DELETE /record/v1/{recordType}/{id}` |
| Get a sublist / sub-resource | `GET  /record/v1/{recordType}/{id}/{sublist}` |
| Transform (e.g. SO → Invoice) | `POST /record/v1/{recordType}/{id}/!transform/{targetType}` |

`{recordType}` uses the REST resource name (usually the same lowercase id as the
SuiteScript record, e.g. `salesOrder` / `salesorder`, `customer`, `invoice`) — but
**verify against the Browser**, as REST naming is not guaranteed identical to SuiteScript.

### Common Query Parameters (collections)

| Param | Purpose |
|-------|---------|
| `q` | Filter expression on the collection (field operators, e.g. `q=email START_WITH "a"`) |
| `limit` / `offset` | Pagination (limit default & max **1000**) |
| `fields` | Sparse fieldset — return only listed fields |
| `expandSubResources=true` | Inline sub-resources instead of HATEOAS links |
| `simpleEnumFormat=true` | Return enum values as plain strings |

Responses are JSON with **HATEOAS `links`**; collections return id + link stubs
(fetch each id for the full body unless `expandSubResources` is set).

---

## Authentication

- **OAuth 2.0** (authorization code or client credentials) — recommended.
- **OAuth 1.0 / TBA** (Token-Based Authentication) — still supported.
- Requires the **SuiteTalk (REST Web Services)** feature enabled
  (*Setup > Company > Enable Features > SuiteCloud*), plus a role with
  **REST Web Services** and **Log in using OAuth 2.0 / Access Tokens** permissions.
- `Content-Type: application/json`; `Accept: application/json`.
- See SafeWords in `../SKILL.md` — never store or echo tokens/secrets.

---

## Metadata Catalog (OpenAPI 3.0 — the real schema)

Per-account, always current, machine-readable — the source the Browser renders:

```
GET /services/rest/record/v1/metadata-catalog                 # index of all record types
GET /services/rest/record/v1/metadata-catalog/{recordType}    # schema for one record type
```

Accept headers:
- `application/schema+json` → JSON Schema
- `application/swagger+json` → OpenAPI/Swagger

> This endpoint (not `records.json`) is the correct place to pull **exact REST field
> names, types, and required flags**. Use it if you later want a full `rest-records.json`.

---

## REST ↔ SuiteScript Field Mapping (why the two are not interchangeable)

`records.json` in this skill describes **SuiteScript** internals. REST uses its own
schema. Do **not** assume a SuiteScript internal id is the valid REST field name —
map with the table below and confirm exact names in the Browser / metadata-catalog.

| Aspect | SuiteScript (`records.json`) | REST Record API |
|--------|------------------------------|-----------------|
| CRUD verb | `N/record.create/load/save/delete` | HTTP `POST/GET/PATCH/DELETE` |
| Body field naming | internal id, lowercase (`trandate`, `entity`) | JSON key, often camelCase (`tranDate`) — **verify per record** |
| Select / reference field | scalar internal id | object `{ "id": "...", "refName": "..." }` |
| Sublist / line items | `getSublistValue()` / line index | sub-resource collection `{ "items": [ ... ] }` |
| Custom field | `custbody_x`, `custentity_x`, `custrecord_x` | same custom id, exposed directly in the JSON body |
| Boolean | `true`/`false` (or `"T"/"F"` legacy) | JSON `true` / `false` |
| Date | string per user format | ISO `YYYY-MM-DD` (datetime ISO-8601) |
| Query | `N/search` / `N/query` (SuiteQL) | collection `q`, or the SuiteQL endpoint `/services/rest/query/v1/suiteql` |
| Enum / list value | internal id | `id` + `refName` (or plain string with `simpleEnumFormat`) |

---

## Related NetSuite APIs (not this file)

| API | Where |
|-----|-------|
| SuiteScript records/fields (272 types) | `records.json` + `record-index.md` (this skill) |
| SuiteQL over REST | `/services/rest/query/v1/suiteql` (REST, but query not record CRUD) |
| SOAP Web Services (legacy) | separate WSDL browser — not covered here |
| SuiteTalk REST **record** metadata | *this file* + metadata-catalog |

---

## Caveats (anti-staleness / anti-hallucination)

1. **Version-bound.** `2024.2` is a snapshot; a NetSuite account may run a newer
   release. The account's `metadata-catalog` is the only always-correct source for
   that account.
2. **Field-level data lives in `rest-records.json`** (all 151 records, 2024.2 snapshot,
   extracted 2026-08-07). This file (`rest-record-api.md`) stays pointer + mapping.
   For a newer release or exact per-account fields, use the metadata-catalog — do not
   fabricate field names from the SuiteScript `records.json`.
3. **Naming is not 1:1.** REST and SuiteScript share record concepts but differ in
   field representation (see mapping table). Always confirm before writing integration code.
