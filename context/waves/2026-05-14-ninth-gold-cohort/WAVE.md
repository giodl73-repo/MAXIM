# Ninth Gold Cohort

## Mission

Continue scaled Gold promotion with a twelve-guide cohort focused on computing,
engineering systems, and human/social systems.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `ai-engineering/01-LLM-CONCEPTS.md` | LLM conceptual stack exemplar | `llm-concepts-stack` |
| `data-science/01-NUMPY.md` | ndarray memory-model exemplar | `numpy-stack-memory` |
| `os/01-CHEATSHEET.md` | operating-system vocabulary exemplar | `os-kernel-architecture` |
| `formal-methods/01-LOGIC-FOUNDATIONS.md` | logic-layer formal-methods exemplar | `formal-methods-logic-stack` |
| `robotics/01-KINEMATICS.md` | kinematics landscape exemplar | `robotics-kinematics-landscape` |
| `biomedical-engineering/01-BIOMECHANICS.md` | biomechanics force/motion exemplar | `biomechanics-force-motion` |
| `environmental-engineering/01-WATER-TREATMENT.md` | water-treatment process exemplar | `water-treatment-train` |
| `urban-planning/01-LAND-USE.md` | zoning/land-use control exemplar | `land-use-control-system` |
| `sociology/01-SOCIAL-STRUCTURE.md` | social-structure exemplar | `social-structure-landscape` |
| `psychology/01-SOCIAL-PSYCHOLOGY.md` | social-influence exemplar | `social-influence-landscape` |
| `education/01-LEARNING-THEORY.md` | learning-theory exemplar | `learning-theory-landscape` |
| `organizational-behavior/01-MOTIVATION.md` | motivation-theory exemplar | `motivation-theory-landscape` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| `query-languages/01-SQL-CORE.md` had too many diagram issues for this cohort | Deferred; replaced with `organizational-behavior/01-MOTIVATION.md` |
| `formal-methods/01-LOGIC-FOUNDATIONS.md` had two narrow ASCII drifts | Repaired table/header and DPLL(T) line |
| `psychology/01-SOCIAL-PSYCHOLOGY.md` had two ASCII drifts | Repaired social influence and authority boxes |
| `os/01-CHEATSHEET.md` lacked a stable Big Picture heading | Added `## The Big Picture` above the kernel architecture diagram |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `ai-engineering/01-LLM-CONCEPTS.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.7 |
| `data-science/01-NUMPY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `os/01-CHEATSHEET.md` | 4.6 | 4.6 | 4.7 | 4.8 | 4.6 | 5.0 | 4.6 |
| `formal-methods/01-LOGIC-FOUNDATIONS.md` | 4.8 | 4.6 | 4.7 | 4.8 | 4.6 | 5.0 | 4.7 |
| `robotics/01-KINEMATICS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `biomedical-engineering/01-BIOMECHANICS.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `environmental-engineering/01-WATER-TREATMENT.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `urban-planning/01-LAND-USE.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `sociology/01-SOCIAL-STRUCTURE.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `psychology/01-SOCIAL-PSYCHOLOGY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `education/01-LEARNING-THEORY.md` | 4.6 | 4.5 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `organizational-behavior/01-MOTIVATION.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Computing systems | LLM Concepts, NumPy, OS, and Formal Methods let a reader move from runtime substrate to model behavior to proof obligations |
| Engineering systems | Robotics, Biomechanics, Water Treatment, and Land Use connect physical constraints to design/control decisions |
| Human systems | Sociology, Psychology, Education, and Motivation separate individual influence, institutional structure, learning, and incentives |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml ai-engineering\01-LLM-CONCEPTS.md data-science\01-NUMPY.md os\01-CHEATSHEET.md formal-methods\01-LOGIC-FOUNDATIONS.md robotics\01-KINEMATICS.md biomedical-engineering\01-BIOMECHANICS.md environmental-engineering\01-WATER-TREATMENT.md urban-planning\01-LAND-USE.md sociology\01-SOCIAL-STRUCTURE.md psychology\01-SOCIAL-PSYCHOLOGY.md education\01-LEARNING-THEORY.md organizational-behavior\01-MOTIVATION.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-ninth-gold-cohort\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve guides to Certified Gold. SQL Core is explicitly deferred
for a future diagram-healing pass rather than forcing a noisy candidate through
the cohort.
