---
wave: maxim-quality-control-spine
pulse: 01
date: 2026-05-14
status: done
depends_on: []
governing_roles: [reference-editor, card-steward]
---

# Pulse 01 - Wave/Pulse Skill Import

## Mission

Port the useful wave/pulse execution discipline from ROUTE and apportionment
into MAXIM as native skills and an active quality-control wave.

## Scope Inventory

| Area | Files |
|---|---|
| Skills | `.claude/skills/maxim-wave/`, `.claude/skills/maxim-pulse/`, `.claude/skills/maxim-fork/`, `.claude/skills/maxim-review/`, `.claude/skills/maxim-plan/` |
| Wave config | `.claude/waves.json` |
| Wave rail | `context/waves/PHASES.md`, `context/waves/2026-05-14-maxim-quality-control-spine/WAVE.md` |

## Deliverables

- [x] Add MAXIM-native wave management skill.
- [x] Add MAXIM-native pulse execution skill.
- [x] Add MAXIM-native fork context skill.
- [x] Add MAXIM-native review panel skill.
- [x] Add MAXIM-native wave/pulse planning skill.
- [x] Add wave index and active quality-control wave.
- [x] Preserve `HISTORY.md` and `/honor` as the narrative/flair layer rather
      than duplicating them.

## Validation

```powershell
git diff --check
```

## Non-Goals

- Do not rewrite `HISTORY.md`.
- Do not copy ROUTE or apportionment domain-specific gates.
- Do not create a bulk content-editing script.
