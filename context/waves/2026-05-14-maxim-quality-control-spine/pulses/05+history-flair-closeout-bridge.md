---
wave: maxim-quality-control-spine
pulse: 05
date: 2026-05-14
status: done
depends_on: [01]
governing_roles: [card-steward, reference-editor]
---

# Pulse 05 - History/Flair Closeout Bridge

## Mission

Meld wave closeouts with MAXIM's existing card/flair honor system so execution
history and poetic project memory reinforce each other instead of competing.

## Pre-implementation Scout

```powershell
rg "Phases Claimed|Image flair|roles remain|/honor" C:\src\maxim\HISTORY.md C:\src\maxim\.claude\skills\honor\SKILL.md C:\src\maxim\cards\ROLES.md
```

## Deliverables

- [x] Define when a wave close should recommend `/honor`.
- [x] Define a closeout section that records candidate card role, rationale, and
      flair seed without mutating `HISTORY.md`.
- [x] Define how backfilled waves cite existing phases and commits.
- [x] Decide whether wave closeouts should include "flair seed" text.

## Evidence

- `artifacts/HISTORY-FLAIR-CLOSEOUT-BRIDGE.md`

## Validation

```powershell
git diff --check
```

## Non-Goals

- Do not claim a role automatically.
- Do not edit `HISTORY.md` or `cards/CONCEPTS.md` in this pulse unless the user
  explicitly asks to run `/honor`.
