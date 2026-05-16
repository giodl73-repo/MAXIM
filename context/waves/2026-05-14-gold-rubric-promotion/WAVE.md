---
wave: gold-rubric-promotion
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: maxim-quality-control-spine
---

# Gold Rubric Promotion

## Mission

Move Gold Rubric v2 from a wave artifact into the operational review skill so
future `/reference-review` work can apply the higher bar consistently.

## Pulse Status

| Pulse | Status | Evidence |
|---|---|---|
| 01 - Promote tier model | DONE | `.claude/skills/reference-review/SKILL.md` now defines Gold/Silver/Bronze/Held |
| 02 - Promote ten dimensions | DONE | Review skill now includes the ten Gold scoring dimensions |
| 03 - Wire single-file review | DONE | `file <path>` mode now requires Gold scoring, reader tasks, and tier decision for Gold candidates |

## Validation

```powershell
git diff --check
```

## Closeout

The source artifact remains in the quality-control spine as historical design
record. The active operational copy now lives in the review skill.
