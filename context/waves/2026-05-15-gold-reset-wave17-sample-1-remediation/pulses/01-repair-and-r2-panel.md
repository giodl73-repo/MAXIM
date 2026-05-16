---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `woodworking/01-WOOD-SELECTION.md`
- `woodworking/02-HAND-TOOLS.md`
- `woodworking/03-POWER-TOOLS.md`
- `woodworking/04-JOINERY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
selector tables. Current Certified Gold requires diagnostic reader-task support
with caveats.

## Changes

| Guide | Repair |
|---|---|
| `woodworking/01-WOOD-SELECTION.md` | Rebuilt the selection table around stability, joinery, bending, movement, moisture, grading, figure, twist, and reaction-wood diagnostics. |
| `woodworking/02-HAND-TOOLS.md` | Rebuilt the hand-tool table around planes, chip-breakers, chisel geometry, saw choice, layout, paring, and sharpness diagnostics. |
| `woodworking/03-POWER-TOOLS.md` | Rebuilt the power-tool table around table-saw safety, bandsaw setup, router work, lathe speed, dust exposure, and warped-stock diagnostics. |
| `woodworking/04-JOINERY.md` | Rebuilt the joinery table around tenons, dovetails, haunches, draw-boring, loose tenons, box joints, glue joints, bridles, and knife-line accuracy. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- woodworking\01-WOOD-SELECTION.md woodworking\02-HAND-TOOLS.md woodworking\03-POWER-TOOLS.md woodworking\04-JOINERY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml woodworking\01-WOOD-SELECTION.md woodworking\02-HAND-TOOLS.md woodworking\03-POWER-TOOLS.md woodworking\04-JOINERY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

