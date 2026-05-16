---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `leatherworking/08-HARDWARE-ASSEMBLY.md`
- `leatherworking/09-CARE-MAINTENANCE.md`
- `masonry/01-MASONRY-UNITS.md`
- `masonry/02-MORTAR-GROUT.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
and situation selector tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `leatherworking/08-HARDWARE-ASSEMBLY.md` | Rebuilt the hardware table around Chicago screws, rivets, snaps, buckles, gussets, sequencing, magnetic snaps, and Sam Browne studs. |
| `leatherworking/09-CARE-MAINTENANCE.md` | Rebuilt the care table around conditioning timing, light leather, neatsfoot oil, product exclusions, mold, water stains, storage, patina, redyeing, and humidity. |
| `masonry/01-MASONRY-UNITS.md` | Rebuilt the unit table around load-bearing walls, partitions, restoration, seismic CMU, adobe, ashlar, fire ratings, and freeze-thaw paving. |
| `masonry/02-MORTAR-GROUT.md` | Rebuilt the mortar/grout table around Type M/N/S/O, historic mortars, repointing, freeze exposure, grout, thin joints, and absorption. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- leatherworking\08-HARDWARE-ASSEMBLY.md leatherworking\09-CARE-MAINTENANCE.md masonry\01-MASONRY-UNITS.md masonry\02-MORTAR-GROUT.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml leatherworking\08-HARDWARE-ASSEMBLY.md leatherworking\09-CARE-MAINTENANCE.md masonry\01-MASONRY-UNITS.md masonry\02-MORTAR-GROUT.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

