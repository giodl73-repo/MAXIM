# Sixth Gold Promotion

## Mission

Promote one guide each from People, Medicine, and Security Engineering into the
Certified Gold set, extending Gold coverage into biography/history, clinical
systems, and software risk control.

## Scope

| Guide | Section | Promotion Target |
|---|---|---|
| `computing-pioneers/01-MECHANICAL-ERA.md` | People | Mechanical computing lineage exemplar |
| `medicine/01-ANTIBIOTICS.md` | Life Sciences / Medicine | Antibiotic target and resistance exemplar |
| `security-engineering/01-THREAT-MODELING.md` | Computing / Security | Threat modeling workflow exemplar |

## Pulse Record

| Pulse | Work | Result |
|---|---|---|
| 01 | Candidate selection | Picked three mechanically clean guides from sections not yet represented in Gold |
| 02 | Gold polish | Normalized Mechanical Era to `The Big Picture`; added decision/cross-reference surfaces |
| 03 | Da Vinci coverage | Added protected opening-figure invariants for all three guides |
| 04 | Registry update | Added all three guides to `context/gold/REGISTRY.md` as Certified Gold |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `computing-pioneers/01-MECHANICAL-ERA.md` | 4.7 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `medicine/01-ANTIBIOTICS.md` | 4.6 | 4.6 | 4.6 | 4.6 | 4.6 | 5.0 | 4.6 |
| `security-engineering/01-THREAT-MODELING.md` | 4.7 | 4.6 | 4.7 | 4.7 | 4.6 | 5.0 | 4.7 |

## Reader-Task Checks

| Guide | Reader Task | Pass Evidence |
|---|---|---|
| Mechanical Era | Explain how Babbage, Lovelace, and Hollerith differ | Comparison table, Who to Cite table, and decision sheet separate architecture, programming concept, and data processing |
| Mechanical Era | Map 19th-century machines to modern computing concepts | Analytical Engine section maps store/mill/cards to RAM/ALU/instructions/data |
| Antibiotics | Choose a class from bacterial target and syndrome | Target map, class sections, and decision sheet connect mechanism, spectrum, and scenario |
| Antibiotics | Explain resistance as an adversarial evolutionary system | Systems Bridge and resistance section enumerate inactivation, target modification, permeability, efflux, and gene transfer |
| Threat Modeling | Run a design-time STRIDE pass from a DFD | Big Picture, STRIDE-per-element table, and Microsoft Tool workflow give the execution path |
| Threat Modeling | Decide between STRIDE, PASTA, attack trees, and pen testing | Decision sheet states when each method is appropriate |

## Da Vinci Invariants

| Invariant | Protects |
|---|---|
| `mechanical-computing-timeline` | Mechanical computing timeline from Babbage through Lovelace and Hollerith |
| `antibiotic-target-map` | Bacterial target map across cell wall, membrane, ribosome, DNA, and folate synthesis |
| `threat-modeling-process` | Threat modeling workflow from decomposition through mitigation |

## Findings

| Finding | Decision |
|---|---|
| No proof warnings in candidate baseline | Promote after Gold-surface polish and invariants |
| Mechanical Era lacked explicit Decision Cheat Sheet | Added decision table before promotion |
| Cross-reference surfaces were absent | Added in all three guides |
| Opening figures needed regression locks | Fixed with Da Vinci invariants in `proof.toml` |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml computing-pioneers\01-MECHANICAL-ERA.md medicine\01-ANTIBIOTICS.md security-engineering\01-THREAT-MODELING.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-sixth-gold-promotion\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all three guides to Certified Gold.
