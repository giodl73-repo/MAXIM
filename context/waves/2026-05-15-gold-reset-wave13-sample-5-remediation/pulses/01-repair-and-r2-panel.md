---
pulse: 01
title: Repair and R2 Panel
status: complete
---

# Pulse 01 - Repair and R2 Panel

## Scope

- `natural-sciences/02-BONDING.md`
- `natural-sciences/03-THERMOCHEM.md`
- `natural-sciences/04-KINETICS.md`
- `natural-sciences/05-ELECTROCHEMISTRY.md`

## Pre-implementation Scout

The guides were proof-clean and invariant-covered, but retained factory-era
question/concept/equation selector tables. Current Certified Gold requires
diagnostic reader-task support with explicit caveats.

## Changes

| Guide | Repair |
|---|---|
| `natural-sciences/02-BONDING.md` | Rebuilt the bonding table around valence, VSEPR, MO magnetism, bond order, hydrogen bonding, polarity, isoelectronic comparison, radius trends, hypervalence, and hybridization limits. |
| `natural-sciences/03-THERMOCHEM.md` | Rebuilt the thermochemistry table around enthalpy, free energy, crossover temperature, equilibrium, Van't Hoff, colligative behavior, phase diagrams, pressure melting, Q/K response, and standard-state confusion. |
| `natural-sciences/04-KINETICS.md` | Rebuilt the kinetics table around rate-law measurement, Arrhenius sensitivity, enzyme acceleration, rate-determining steps, gas collision frequency, catalysis, integrated-rate plots, and radical inhibition. |
| `natural-sciences/05-ELECTROCHEMISTRY.md` | Rebuilt the electrochemistry table around redox spontaneity, free energy, equilibrium constants, Nernst shifts, galvanic corrosion, cathodic protection, passivation, plating mass, battery voltage, and fuel-cell overpotential. |

## Gates

| Gate | Status |
|---|---|
| Proof + Da Vinci | PASS |
| Targeted editorial repair | PASS |
| R2 reference-editor panel | PASS |
| Consolidated Gold decision | PASS |

## Validation

```powershell
git --no-pager diff --check -- natural-sciences\02-BONDING.md natural-sciences\03-THERMOCHEM.md natural-sciences\04-KINETICS.md natural-sciences\05-ELECTROCHEMISTRY.md
$proofOut = C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml natural-sciences\02-BONDING.md natural-sciences\03-THERMOCHEM.md natural-sciences\04-KINETICS.md natural-sciences\05-ELECTROCHEMISTRY.md 2>&1; $proofOut; if ($proofOut -match 'FAIL') { exit 1 }
```

Result: PASS.

