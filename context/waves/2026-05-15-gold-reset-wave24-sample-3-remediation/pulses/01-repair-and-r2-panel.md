---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `animal-phylogeny/10-AMPHIBIA.md`
- `animal-phylogeny/11-REPTILIA-BIRDS.md`
- `animal-phylogeny/12-MAMMALIA.md`
- `archaeology/02-DATING-METHODS.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
identification keys and method-selector tables. Current Certified Gold requires
diagnostic reader-task support with caveats.

## Changes

| Guide | Repair |
|---|---|
| `animal-phylogeny/10-AMPHIBIA.md` | Rebuilt the amphibian identification key around anuran, salamander, neoteny, lungless, caecilian, and tetrapod-transition caveats. |
| `animal-phylogeny/11-REPTILIA-BIRDS.md` | Rebuilt the reptile/bird key around avian dinosaurs, turtles, crocodilians, squamates, snakes, venom, and tuatara caveats. |
| `animal-phylogeny/12-MAMMALIA.md` | Rebuilt the mammal order key around monotreme, marsupial, placental, whale, primate, and cognition caveats. |
| `archaeology/02-DATING-METHODS.md` | Rebuilt the dating-method selector around radiocarbon, dendrochronology, OSL, TL, volcanic, U-series, archaeomagnetic, Bayesian, and typological caveats. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- animal-phylogeny\10-AMPHIBIA.md animal-phylogeny\11-REPTILIA-BIRDS.md animal-phylogeny\12-MAMMALIA.md archaeology\02-DATING-METHODS.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml animal-phylogeny\10-AMPHIBIA.md animal-phylogeny\11-REPTILIA-BIRDS.md animal-phylogeny\12-MAMMALIA.md archaeology\02-DATING-METHODS.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

