---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `leatherworking/04-CUTTING-SKIVING.md`
- `leatherworking/05-TOOLING-CARVING.md`
- `leatherworking/06-DYEING-FINISHING.md`
- `leatherworking/07-STITCHING-SEWING.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
selector tables. Current Certified Gold requires diagnostic reader-task support
with caveats.

## Changes

| Guide | Repair |
|---|---|
| `leatherworking/04-CUTTING-SKIVING.md` | Rebuilt the cutting/skiving table around cutting surfaces, knives, skiving, bevelers, pricking irons, belt holes, and buckle slots. |
| `leatherworking/05-TOOLING-CARVING.md` | Rebuilt the tooling table around veg-tan, casing, beveling, Sheridan style, swivel-knife depth, shaders, antique finish, flesh-side moisture, and sharpening. |
| `leatherworking/06-DYEING-FINISHING.md` | Rebuilt the dyeing/finishing table around dye penetration, antique contrast, edge compounds, Resolene, darkening, oiling, edge sequence, and cleaning. |
| `leatherworking/07-STITCHING-SEWING.md` | Rebuilt the stitching table around saddle stitch, thread length, wax, machine needles, walking feet, thread choice, needle path, spacing, pre-punching, and grooving. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- leatherworking\04-CUTTING-SKIVING.md leatherworking\05-TOOLING-CARVING.md leatherworking\06-DYEING-FINISHING.md leatherworking\07-STITCHING-SEWING.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml leatherworking\04-CUTTING-SKIVING.md leatherworking\05-TOOLING-CARVING.md leatherworking\06-DYEING-FINISHING.md leatherworking\07-STITCHING-SEWING.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

