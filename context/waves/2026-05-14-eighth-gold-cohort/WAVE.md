# Eighth Gold Cohort

## Mission

Scale from a nine-guide cohort to a twelve-guide Gold cohort while preserving
the same mechanical, editorial, Da Vinci, registry, and reader-task gates.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `probability-statistics/01-PROBABILITY-FOUNDATIONS.md` | Probability foundation exemplar | `probability-space-foundation` |
| `physics/01-ELECTROSTATICS.md` | Electrostatics field/potential exemplar | `electrostatics-landscape` |
| `electronics/01-CIRCUITS.md` | Circuit-analysis exemplar | `circuit-analysis-landscape` |
| `cryptography/01-SYMMETRIC.md` | Symmetric-crypto primitive stack exemplar | `symmetric-crypto-stack` |
| `cloud-architecture/01-CLOUD-MODELS.md` | Cloud service-model exemplar | `cloud-service-model-spectrum` |
| `astronomy/01-EARTH-MOTIONS.md` | Earth-motion hierarchy exemplar | `earth-motions-hierarchy` |
| `climate-science/01-CARBON-CYCLE.md` | Carbon-cycle reservoir exemplar | `carbon-cycle-reservoirs` |
| `neuroscience/01-NEURONS-SIGNALS.md` | Neural-signal hierarchy exemplar | `neural-signaling-hierarchy` |
| `rhetoric/01-CLASSICAL-RHETORIC.md` | Classical rhetoric landscape exemplar | `classical-rhetoric-landscape` |
| `architecture/01-SPATIAL-DESIGN.md` | Spatial-design stack exemplar | `spatial-design-stack` |
| `manufacturing/01-GDT-TOLERANCING.md` | GD&T comparison exemplar | `gdt-coordinate-comparison` |
| `machine-learning-theory/01-PAC-LEARNING.md` | PAC-learning framework exemplar | `pac-learning-framework` |

## Scale-Up Findings

| Finding | Resolution |
|---|---|
| Baseline proof found Physics ASCII width drift | Repaired the electrostatics box before promotion |
| Baseline proof found PAC table pipe parsing errors | Escaped `log\|H\|` table cells |
| Several guides lacked explicit cross-reference surfaces | Added a Cross-References section to all twelve |
| Electronics lacked a `The Big Picture` H2 above its opening landscape | Added the heading so Da Vinci can target it consistently |
| Cloud lacked a Decision Cheat Sheet | Added a cloud-model decision table before promotion |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `probability-statistics/01-PROBABILITY-FOUNDATIONS.md` | 4.7 | 4.6 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `physics/01-ELECTROSTATICS.md` | 4.6 | 4.6 | 4.5 | 4.6 | 4.6 | 5.0 | 4.6 |
| `electronics/01-CIRCUITS.md` | 4.6 | 4.6 | 4.5 | 4.7 | 4.6 | 5.0 | 4.6 |
| `cryptography/01-SYMMETRIC.md` | 4.8 | 4.6 | 4.7 | 4.7 | 4.6 | 5.0 | 4.7 |
| `cloud-architecture/01-CLOUD-MODELS.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `astronomy/01-EARTH-MOTIONS.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `climate-science/01-CARBON-CYCLE.md` | 4.7 | 4.6 | 4.7 | 4.6 | 4.6 | 5.0 | 4.6 |
| `neuroscience/01-NEURONS-SIGNALS.md` | 4.7 | 4.6 | 4.5 | 4.7 | 4.6 | 5.0 | 4.6 |
| `rhetoric/01-CLASSICAL-RHETORIC.md` | 4.6 | 4.6 | 4.5 | 4.7 | 4.6 | 5.0 | 4.6 |
| `architecture/01-SPATIAL-DESIGN.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `manufacturing/01-GDT-TOLERANCING.md` | 4.6 | 4.6 | 4.7 | 4.7 | 4.6 | 5.0 | 4.6 |
| `machine-learning-theory/01-PAC-LEARNING.md` | 4.8 | 4.6 | 4.7 | 4.8 | 4.6 | 5.0 | 4.7 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Formal/math foundations | Probability and PAC guides let the reader distinguish sample space, sigma-algebra, random variable, sample complexity, and confidence |
| Physical/electrical systems | Electrostatics, circuits, and GD&T guides preserve the chain from field laws to engineered tolerances |
| Computing/security systems | Symmetric crypto and cloud models expose primitive choices, responsibility boundaries, and operational failure modes |
| Earth/life/culture systems | Astronomy, carbon cycle, neural signals, rhetoric, and architecture guides each connect a landscape diagram to decision surfaces |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml probability-statistics\01-PROBABILITY-FOUNDATIONS.md physics\01-ELECTROSTATICS.md electronics\01-CIRCUITS.md cryptography\01-SYMMETRIC.md cloud-architecture\01-CLOUD-MODELS.md astronomy\01-EARTH-MOTIONS.md climate-science\01-CARBON-CYCLE.md neuroscience\01-NEURONS-SIGNALS.md rhetoric\01-CLASSICAL-RHETORIC.md architecture\01-SPATIAL-DESIGN.md manufacturing\01-GDT-TOLERANCING.md machine-learning-theory\01-PAC-LEARNING.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-eighth-gold-cohort\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve guides to Certified Gold. The scaled cohort remains valid:
baseline proof first, repair before claim, then Da Vinci protection and registry
evidence.
