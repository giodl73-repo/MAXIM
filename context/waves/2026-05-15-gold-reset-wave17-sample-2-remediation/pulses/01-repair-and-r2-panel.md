---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `woodworking/05-SURFACE-PREPARATION.md`
- `woodworking/06-FINISHING.md`
- `woodworking/07-FURNITURE-CONSTRUCTION.md`
- `woodworking/08-TURNING-CARVING.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
selector tables. Current Certified Gold requires diagnostic reader-task support
with caveats.

## Changes

| Guide | Repair |
|---|---|
| `woodworking/05-SURFACE-PREPARATION.md` | Rebuilt the preparation table around twist, planing sequence, scrapers, sanding, grain raising, scratch detection, sanding endpoint, and blotching. |
| `woodworking/06-FINISHING.md` | Rebuilt the finishing table around shellac, yellowing, light woods, wipe-on film, crosslinking, food contact, water-based tradeoffs, compatibility, and sheen. |
| `woodworking/07-FURNITURE-CONSTRUCTION.md` | Rebuilt the furniture table around cabinet systems, panels, haunches, tabletops, chair joints, repair glue, 32 mm layout, drawer bottoms, and breadboards. |
| `woodworking/08-TURNING-CARVING.md` | Rebuilt the turning/carving table around lathe speed, spindle and bowl geometry, gouge choice, green wood, chip carving, sweep numbers, and sharpening. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- woodworking\05-SURFACE-PREPARATION.md woodworking\06-FINISHING.md woodworking\07-FURNITURE-CONSTRUCTION.md woodworking\08-TURNING-CARVING.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml woodworking\05-SURFACE-PREPARATION.md woodworking\06-FINISHING.md woodworking\07-FURNITURE-CONSTRUCTION.md woodworking\08-TURNING-CARVING.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

