---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `masonry/03-BRICKLAYING.md`
- `masonry/04-STONEWORK.md`
- `masonry/05-STRUCTURAL-MASONRY.md`
- `masonry/06-ARCHES-VAULTS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
situation selector tables. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `masonry/03-BRICKLAYING.md` | Rebuilt the bricklaying table around CMU, English/Flemish/running/stack bonds, repairs, leads, and course control. |
| `masonry/04-STONEWORK.md` | Rebuilt the stonework table around ashlar, rubble, dry-stone, retaining walls, historic seismic work, flooring, paving, and restoration. |
| `masonry/05-STRUCTURAL-MASONRY.md` | Rebuilt the structural table around empirical design, engineered design, seismic masonry, slenderness, shear walls, URM upgrades, retaining walls, and net/gross area. |
| `masonry/06-ARCHES-VAULTS.md` | Rebuilt the arch/vault table around small and medium openings, pointed arches, groin/rib/fan vaults, domes, cracked arches, and catenary limits. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- masonry\03-BRICKLAYING.md masonry\04-STONEWORK.md masonry\05-STRUCTURAL-MASONRY.md masonry\06-ARCHES-VAULTS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml masonry\03-BRICKLAYING.md masonry\04-STONEWORK.md masonry\05-STRUCTURAL-MASONRY.md masonry\06-ARCHES-VAULTS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

