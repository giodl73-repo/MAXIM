---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `woodworking/09-SHOP-SETUP.md`
- `leatherworking/01-LEATHER-TYPES.md`
- `leatherworking/02-TANNING-PROCESSES.md`
- `leatherworking/03-PATTERN-MAKING.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
selector tables. Current Certified Gold requires diagnostic reader-task support
with caveats.

## Changes

| Guide | Repair |
|---|---|
| `woodworking/09-SHOP-SETUP.md` | Rebuilt the shop table around bench height, bench design, holdfasts, tool storage, silicone contamination, dust, blast gates, lumber storage, acclimation, and power. |
| `leatherworking/01-LEATHER-TYPES.md` | Rebuilt the leather-types table around full grain, marketing terms, suede/nubuck, bonded leather, pull-up, exotics, CITES, aniline, and vegan-label claims. |
| `leatherworking/02-TANNING-PROCESSES.md` | Rebuilt the tanning table around veg-tan, chrome, chromium states, wet blue, brain-tan, alum tawing, syntans, LWG, and waste risk. |
| `leatherworking/03-PATTERN-MAKING.md` | Rebuilt the pattern table around seam allowance, durable templates, hide regions, strap direction, yield, stitch lines, gussets, mockups, and marking. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- woodworking\09-SHOP-SETUP.md leatherworking\01-LEATHER-TYPES.md leatherworking\02-TANNING-PROCESSES.md leatherworking\03-PATTERN-MAKING.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml woodworking\09-SHOP-SETUP.md leatherworking\01-LEATHER-TYPES.md leatherworking\02-TANNING-PROCESSES.md leatherworking\03-PATTERN-MAKING.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

