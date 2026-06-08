# iCE Skills Marketplace

Complete skill marketplace for the iCE workflow — **40 skills in 3 plugins**, synced across Claude Code CLI / Web / Desktop / Cowork via Git.

## Plugins

| Plugin | Skills | Scope |
|---|---|---|
| **ice-academic** | 6 | Thai academic writing — PhD/MA dissertation (MCU), TCI/AGJ/JPSPA journal articles, social-science articles, AI-detection & humanization |
| **ice-b2b-sales** | 29 | iCE B2B enterprise software sales — Oracle/SAP/NetSuite/MS Dynamics, B2B methodology, Thai GFMIS/e-GP/tax, pricing, presentation |
| **ice-tools** | 5 | Productivity tools — graphify, nanobanana, notebooklm, cua-driver, automation-workflow |

## Install (any client)

```
/plugin marketplace add xpickey/ice-skills-marketplace
/plugin install ice-academic@ice-skills
/plugin install ice-b2b-sales@ice-skills
/plugin install ice-tools@ice-skills
```

## Update (after editing a skill)

Edit in `~/.claude/skills/<skill>/`, re-sync into this repo, then:
```
git add -A && git commit -m "update <skill>" && git push
```
Every client: `/plugin marketplace update ice-skills`

## Notes
- Runtime artifacts (`.venv/`, browser cache, `.tflite`, `__pycache__`) are gitignored — clients rebuild them on use.
- Version: 1.0.0 | 2026.06.08
