---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `freshwater-biology/08-CONSERVATION.md`
- `freshwater-biology/09-WATER-QUALITY.md`
- `coral-reefs/01-REEF-FORMATION.md`
- `coral-reefs/02-CORAL-BIOLOGY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era Q&A
tables. Current Certified Gold requires diagnostic reader-task support with
caveats.

## Changes

| Guide | Repair |
|---|---|
| `freshwater-biology/08-CONSERVATION.md` | Rebuilt the conservation table around zebra mussels, Nile perch, downstream dam temperature, delta sediment starvation, environmental flows, dam removal, mussel threats, and fish ladders. |
| `freshwater-biology/09-WATER-QUALITY.md` | Rebuilt the water-quality table around BOD, DO stress, nitrate units, EPT richness, IBI, oxygen sag, EU WFD status, and conductivity. |
| `coral-reefs/01-REEF-FORMATION.md` | Rebuilt the reef-formation table around aragonite, atolls, CCA, branching and massive coral growth, accretion, sea-level tracking, drowned reefs, ahermatypic corals, and Porites proxies. |
| `coral-reefs/02-CORAL-BIOLOGY.md` | Rebuilt the coral-biology table around cnidarian identity, Anthozoa, corallites, septa, nematocysts, mesenterial filaments, spawning, brooding, annual bands, and massive-coral age. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- freshwater-biology\08-CONSERVATION.md freshwater-biology\09-WATER-QUALITY.md coral-reefs\01-REEF-FORMATION.md coral-reefs\02-CORAL-BIOLOGY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml freshwater-biology\08-CONSERVATION.md freshwater-biology\09-WATER-QUALITY.md coral-reefs\01-REEF-FORMATION.md coral-reefs\02-CORAL-BIOLOGY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

