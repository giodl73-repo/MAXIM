# Eleventh Gold Cohort

## Mission

Continue scaled Gold promotion with an engineering-infrastructure cohort:
classical mechanics, aerospace, process thermodynamics, nuclear physics,
power systems, materials, semiconductor manufacturing, nanotechnology,
storage, infrastructure classification, and rail transportation.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `structural/01-STATICS.md` | statics workflow exemplar | `statics-workflow` |
| `aeronautics/01-AERODYNAMICS.md` | aerodynamic regime hierarchy exemplar | `aerodynamic-flow-hierarchy` |
| `chemical-eng/01-THERMO.md` | chemical thermodynamics toolkit exemplar | `chemical-thermodynamics-toolkit` |
| `nuclear/01-NUCLEAR-PHYSICS.md` | nuclear scale and notation exemplar | `nuclear-key-scales` |
| `electrical-grid/01-GENERATION.md` | generation conversion-chain exemplar | `generation-technology-chain` |
| `energy-systems/01-SOLAR-PV.md` | photon-to-grid PV stack exemplar | `solar-pv-stack` |
| `materials/01-CRYSTAL-STRUCTURE.md` | crystal-structure landscape exemplar | `crystal-structure-landscape` |
| `semiconductor-manufacturing/01-SILICON-SUBSTRATE.md` | sand-to-wafer chain exemplar | `sand-to-wafer` |
| `nanotechnology/01-NANOSCALE-PHYSICS.md` | nanoscale regime-shift exemplar | `nanoscale-physical-regimes` |
| `energy-storage/01-ELECTROCHEMICAL.md` | electrochemical cell exemplar | `electrochemical-cell-overview` |
| `infrastructure-systems/01-CLASSIFICATION.md` | critical-infrastructure taxonomy exemplar | `critical-infrastructure-classification` |
| `transportation/01-RAIL.md` | rail system-layer exemplar | `rail-system-layers` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| `materials/01-CRYSTAL-STRUCTURE.md` had two ASCII box drift errors | Shortened the Hume-Rothery valence line and normalized two arrow rows in the crystalline-vs-amorphous comparison |
| Several early engineering guides used descriptive opening H2s instead of stable `The Big Picture` anchors | Normalized Structural, Aeronautics, Chemical Engineering, Nuclear, and Electrical Grid headings while preserving their subject subtitles |
| Cohort lacked explicit cross-reference surfaces | Added Cross-References sections across all twelve guides |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `structural/01-STATICS.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `aeronautics/01-AERODYNAMICS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `chemical-eng/01-THERMO.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `nuclear/01-NUCLEAR-PHYSICS.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `electrical-grid/01-GENERATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `energy-systems/01-SOLAR-PV.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `materials/01-CRYSTAL-STRUCTURE.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `semiconductor-manufacturing/01-SILICON-SUBSTRATE.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `nanotechnology/01-NANOSCALE-PHYSICS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `energy-storage/01-ELECTROCHEMICAL.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `infrastructure-systems/01-CLASSIFICATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `transportation/01-RAIL.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Mechanics to flight | Statics and Aerodynamics connect equilibrium, continuum flow, and design regimes |
| Energy conversion | Chemical Thermodynamics, Nuclear, Grid Generation, Solar PV, and Storage connect thermodynamic potentials to electrons and dispatch |
| Matter to devices | Materials, Semiconductor Manufacturing, and Nanotechnology connect lattice structure to industrial nanoscale control |
| Networked systems | Infrastructure Classification and Rail connect sector taxonomy, dependencies, corridors, and operations |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml structural\01-STATICS.md aeronautics\01-AERODYNAMICS.md chemical-eng\01-THERMO.md nuclear\01-NUCLEAR-PHYSICS.md electrical-grid\01-GENERATION.md energy-systems\01-SOLAR-PV.md materials\01-CRYSTAL-STRUCTURE.md semiconductor-manufacturing\01-SILICON-SUBSTRATE.md nanotechnology\01-NANOSCALE-PHYSICS.md energy-storage\01-ELECTROCHEMICAL.md infrastructure-systems\01-CLASSIFICATION.md transportation\01-RAIL.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-eleventh-gold-cohort\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve guides to Certified Gold.
