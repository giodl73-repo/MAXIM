---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `animal-phylogeny/06-ARTHROPODA.md`
- `animal-phylogeny/07-DEUTEROSTOMES-ECHINODERMS.md`
- `animal-phylogeny/08-CHORDATA-ORIGINS.md`
- `animal-phylogeny/09-FISH.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
identification-key cheat sheets. Current Certified Gold requires diagnostic
reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `animal-phylogeny/06-ARTHROPODA.md` | Rebuilt the arthropod identification key around arachnid, myriapod, crustacean, insect, and insect-order diagnostic caveats. |
| `animal-phylogeny/07-DEUTEROSTOMES-ECHINODERMS.md` | Rebuilt the echinoderm/hemichordate key around radial symmetry, class-level anatomy, larval bilaterality, and gill-slit homology caveats. |
| `animal-phylogeny/08-CHORDATA-ORIGINS.md` | Rebuilt the chordate lookup key around life-stage traits, tunicate derivation, amphioxus limits, vertebral-column diagnosis, and embryonic pharyngeal caveats. |
| `animal-phylogeny/09-FISH.md` | Rebuilt the fish identification key around fish-as-grade, jawless vertebrates, chondrichthyans, ray-finned fish, lobe-finned fish, and lung/swim-bladder caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- animal-phylogeny\06-ARTHROPODA.md animal-phylogeny\07-DEUTEROSTOMES-ECHINODERMS.md animal-phylogeny\08-CHORDATA-ORIGINS.md animal-phylogeny\09-FISH.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml animal-phylogeny\06-ARTHROPODA.md animal-phylogeny\07-DEUTEROSTOMES-ECHINODERMS.md animal-phylogeny\08-CHORDATA-ORIGINS.md animal-phylogeny\09-FISH.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

