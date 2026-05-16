# Seventh Gold Cohort

## Mission

Scale Gold promotion from three-guide waves to a nine-guide cohort while keeping
the gates intact: proof, Da Vinci invariants, cross-reference polish, rubric
scores, reader-task checks, registry evidence, and validation.

## Scope

| Guide | Section | Promotion Target |
|---|---|---|
| `law/01-CONTRACTS.md` | Social Systems / Law | Contract-law framework exemplar |
| `optics/01-GEOMETRIC-OPTICS.md` | Mechanics / Optics | Ray-optics and matrix-method exemplar |
| `ceramics/01-CLAY-TYPES.md` | Material Culture | Clay mineral and body-selection exemplar |
| `finance/01-PORTFOLIO-THEORY.md` | Social Sciences / Finance | Mean-variance and factor-model exemplar |
| `game-theory/01-NORMAL-FORM.md` | Social Sciences / Game Theory | Strategic-form equilibrium exemplar |
| `control-theory/01-PID-CLASSICAL.md` | Mathematics & Physics / Control | Classical feedback-control exemplar |
| `geography/01-PHYSICAL-GEOGRAPHY.md` | Earth & Space / Geography | Earth process-cycle exemplar |
| `typography/01-WRITING-SYSTEMS.md` | Language & Communication | Writing-system genealogy exemplar |
| `ecology/01-POPULATION-DYNAMICS.md` | Life Sciences / Ecology | Population-model dynamics exemplar |

## Scale-Up Rules Proven

| Rule | Result |
|---|---|
| Candidate baseline proof runs before promotion | Geography exposed ASCII drift; repaired before certification |
| One cohort patch may add cross-reference surfaces | All nine guides received or already had Gold-grade cross-reference surfaces |
| Da Vinci coverage scales linearly | Nine new invariants added to `proof.toml` |
| Registry remains the source of truth | All nine promotions recorded in `context/gold/REGISTRY.md` |
| Mechanical validation remains non-negotiable | Cohort validated with focused proof and `--daVinci` |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `law/01-CONTRACTS.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `optics/01-GEOMETRIC-OPTICS.md` | 4.7 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `ceramics/01-CLAY-TYPES.md` | 4.6 | 4.6 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `finance/01-PORTFOLIO-THEORY.md` | 4.7 | 4.5 | 4.7 | 4.7 | 4.6 | 5.0 | 4.7 |
| `game-theory/01-NORMAL-FORM.md` | 4.8 | 4.6 | 4.7 | 4.7 | 4.6 | 5.0 | 4.7 |
| `control-theory/01-PID-CLASSICAL.md` | 4.8 | 4.6 | 4.7 | 4.8 | 4.6 | 5.0 | 4.7 |
| `geography/01-PHYSICAL-GEOGRAPHY.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `typography/01-WRITING-SYSTEMS.md` | 4.7 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `ecology/01-POPULATION-DYNAMICS.md` | 4.7 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Guide | Reader Task | Pass Evidence |
|---|---|---|
| Contracts | Decide whether common law or UCC governs a dispute | Formation, UCC, software licensing, and decision sheet separate the regimes |
| Optics | Trace a ray system and choose the right formula | Fermat, thin-lens, ABCD, instruments, and decision sheet cover the workflow |
| Ceramics | Choose clay body for porcelain, stoneware, sculpture, or raku | Mineral taxonomy, clay-body sections, and decision sheet connect material to use |
| Finance | Explain why raw Markowitz is unstable | Model stack and practice sections identify estimation error and shrinkage remedies |
| Game Theory | Move from dominance to Nash to correlated equilibrium | Opening solution ladder and decision sheet order the solution concepts |
| Control | Tune or reason about a SISO feedback loop | PID, root locus, Bode, Nyquist, and decision sheet map goal to method |
| Geography | Explain landform, hazard, soil, or settlement from process | Process cycle, tectonics, rocks, soils, and cross-links connect causes to outcomes |
| Typography | Distinguish alphabet, abjad, abugida, syllabary, and logography | Genealogy, script typology, Unicode bridge, and confusion points cover distinctions |
| Ecology | Pick a model for growth, predation, metapopulation, or extinction | Decision sheet and model sections map population question to method |

## Da Vinci Invariants

| Invariant | Protects |
|---|---|
| `contract-law-framework` | Contract-law formation-to-remedies landscape |
| `geometric-optics-fermat` | Fermat-principle foundation diagram |
| `clay-mineral-taxonomy` | Clay mineral taxonomy and plasticity mechanism |
| `portfolio-theory-model-stack` | Markowitz/CAPM/factor/Black-Litterman model stack |
| `normal-form-game-structure` | Normal-form primitives and solution ladder |
| `closed-loop-control-system` | Controller/plant/error/feedback diagram |
| `physical-geography-process-cycle` | Internal/external engines and rock-cycle process map |
| `writing-system-genealogy` | Writing-system historical genealogy |
| `population-dynamics-framework` | Single- and multi-species model framework |

## Findings

| Finding | Decision |
|---|---|
| Geography had proof-detected ASCII drift | Repaired before promotion |
| Some guides lacked explicit cross-reference surfaces | Added Gold-grade cross-reference tables |
| Three-guide cadence was too small for broad coverage | Scaled to nine-guide cohort while retaining all gates |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml law\01-CONTRACTS.md optics\01-GEOMETRIC-OPTICS.md ceramics\01-CLAY-TYPES.md finance\01-PORTFOLIO-THEORY.md game-theory\01-NORMAL-FORM.md control-theory\01-PID-CLASSICAL.md geography\01-PHYSICAL-GEOGRAPHY.md typography\01-WRITING-SYSTEMS.md ecology\01-POPULATION-DYNAMICS.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-seventh-gold-cohort\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all nine guides to Certified Gold. This cohort proves the scaled model:
promotion can run at nine guides per wave when baseline proof is clean or defects
are surgical, but the gate remains evidence-based rather than volume-based.
