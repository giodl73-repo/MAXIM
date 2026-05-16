---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `ceramics/02-FORMING.md`
- `ceramics/03-DRYING-FIRING.md`
- `ceramics/04-GLAZES.md`
- `ceramics/05-DECORATION.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but their cheat sheets were
direct forming, firing, glaze, and decoration selectors. Current Certified Gold
requires diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `ceramics/02-FORMING.md` | Rebuilt forming selection around throwing, multi-part work, pressing/extrusion, slip casting, hand-building, tribal lineage, architectural profiles, molds, and 3D printing. |
| `ceramics/03-DRYING-FIRING.md` | Rebuilt firing selection around electric, reduction, wood, salt/soda, raku, low-fire color, high-fire strength, and porcelain. |
| `ceramics/04-GLAZES.md` | Rebuilt glaze selection around tin, cobalt, celadon, copper red, matte, crystalline, rutile, tenmoku, crawl, and commercial-stain caveats. |
| `ceramics/05-DECORATION.md` | Rebuilt decoration selection around cobalt, enamels, majolica, luster, raku, transfer/inkjet, slip techniques, carbon reduction, photo tiles, and istoriato. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- ceramics\02-FORMING.md ceramics\03-DRYING-FIRING.md ceramics\04-GLAZES.md ceramics\05-DECORATION.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ceramics\02-FORMING.md ceramics\03-DRYING-FIRING.md ceramics\04-GLAZES.md ceramics\05-DECORATION.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

