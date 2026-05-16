---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `natural-sciences/11-EVOLUTION-GENETICS.md`
- `natural-sciences/12-SYSTEMS-SYNTHETIC.md`
- `natural-sciences/13-GEOPHYSICS.md`
- `natural-sciences/14-ATMOSPHERE-CLIMATE.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/concept/answer selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `natural-sciences/11-EVOLUTION-GENETICS.md` | Rebuilt the evolution/genetics table around carrier frequency, selection, overdominance, drift, hybrid sterility, phylogeny uncertainty, Hox modularity, bottlenecks, and synonymous variation. |
| `natural-sciences/12-SYSTEMS-SYNTHETIC.md` | Rebuilt the systems/synthetic biology table around bistability, oscillation, feed-forward filtering, FBA, expression noise, optogenetics, CRISPRi, CRISPRa, and essentiality testing. |
| `natural-sciences/13-GEOPHYSICS.md` | Rebuilt the geophysics table around core state, plate forcing, mantle tomography, arc volcanism, isostasy, seafloor age, glacial rebound, fault regime, and magnetic reversals. |
| `natural-sciences/14-ATMOSPHERE-CLIMATE.md` | Rebuilt the atmosphere/climate table around greenhouse baseline, stratospheric stability, trade winds, logarithmic CO2 forcing, ECS, AMOC, ozone-hole timing, El Nino teleconnections, and cloud-feedback uncertainty. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- natural-sciences\11-EVOLUTION-GENETICS.md natural-sciences\12-SYSTEMS-SYNTHETIC.md natural-sciences\13-GEOPHYSICS.md natural-sciences\14-ATMOSPHERE-CLIMATE.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml natural-sciences\11-EVOLUTION-GENETICS.md natural-sciences\12-SYSTEMS-SYNTHETIC.md natural-sciences\13-GEOPHYSICS.md natural-sciences\14-ATMOSPHERE-CLIMATE.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

