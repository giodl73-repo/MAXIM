---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `dyeing-fiber/02-MORDANTING.md`
- `dyeing-fiber/03-DYE-CHEMISTRY.md`
- `dyeing-fiber/04-FIBER-PREPARATION.md`
- `dyeing-fiber/05-SPINNING.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
color-shift, fiber/dye, end-use, and goal selector tables. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `dyeing-fiber/02-MORDANTING.md` | Rebuilt the mordant table around alum, iron, copper, tin, chrome, indigo, cellulose tannin, and one-bath shortcuts. |
| `dyeing-fiber/03-DYE-CHEMISTRY.md` | Rebuilt the dye-chemistry table around wool, cotton, indigo, silk, polyester, and durability diagnostics. |
| `dyeing-fiber/04-FIBER-PREPARATION.md` | Rebuilt the preparation table around knitting, suiting, linen, cotton, silk, and blended performance uses. |
| `dyeing-fiber/05-SPINNING.md` | Rebuilt the spinning table around knitting, warp, lace, beginner practice, fine Merino, rustic yarn, plying, and twist-bias diagnostics. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- dyeing-fiber\02-MORDANTING.md dyeing-fiber\03-DYE-CHEMISTRY.md dyeing-fiber\04-FIBER-PREPARATION.md dyeing-fiber\05-SPINNING.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml dyeing-fiber\02-MORDANTING.md dyeing-fiber\03-DYE-CHEMISTRY.md dyeing-fiber\04-FIBER-PREPARATION.md dyeing-fiber\05-SPINNING.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

