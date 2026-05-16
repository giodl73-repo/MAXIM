# Fifth Gold Promotion

## Mission

Promote one underrepresented guide each from Language & Communication,
Technology, and Earth & Space into the Certified Gold set.

## Scope

| Guide | Section | Promotion Target |
|---|---|---|
| `translation/01-EQUIVALENCE-PROBLEM.md` | Language & Communication | Translation theory exemplar |
| `telecommunications/01-ELECTROMAGNETIC-SPECTRUM.md` | Technology | RF/link-budget exemplar |
| `space-exploration/01-ORBITAL-MECHANICS.md` | Earth & Space | Mission-mechanics exemplar |

## Pulse Record

| Pulse | Work | Result |
|---|---|---|
| 01 | Candidate selection | Picked three mechanically clean guides from still-underrepresented sections |
| 02 | Gold polish | Added cross-reference surfaces tying each guide to adjacent MAXIM concepts |
| 03 | Da Vinci coverage | Added protected opening-figure invariants for all three guides |
| 04 | Registry update | Added all three guides to `context/gold/REGISTRY.md` as Certified Gold |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `translation/01-EQUIVALENCE-PROBLEM.md` | 4.7 | 4.5 | 4.5 | 4.6 | 4.6 | 5.0 | 4.6 |
| `telecommunications/01-ELECTROMAGNETIC-SPECTRUM.md` | 4.6 | 4.5 | 4.7 | 4.5 | 4.6 | 5.0 | 4.6 |
| `space-exploration/01-ORBITAL-MECHANICS.md` | 4.6 | 4.5 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Guide | Reader Task | Pass Evidence |
|---|---|---|
| Translation | Choose formal, dynamic, foreignizing, or domesticating strategy for a text | Decision sheet names the preservation target and best application for each theory |
| Translation | Explain why "faithful translation" is underspecified | Common Confusion Points separates faithfulness to words, meaning, effect, style, and culture |
| Telecom | Pick a frequency band for HF, cellular, satellite, 60 GHz, or submarine links | Big Picture and Decision Cheat Sheet connect band, propagation mechanism, and use |
| Telecom | Compute whether a link barely closes | Link Budget section carries received power, noise floor, SNR, and modulation threshold |
| Orbital | Explain why delta-v, not distance, dominates mission cost | Rocket Equation, Delta-V Budget, and Engineering Parallels frame the budget correctly |
| Orbital | Choose when a Hohmann transfer is valid | Hohmann section states circular/coplanar assumptions and limitations |

## Da Vinci Invariants

| Invariant | Protects |
|---|---|
| `translation-equivalence-map` | Equivalence-problem map across formal, dynamic, functional, aesthetic, and critical approaches |
| `telecom-spectrum-bands` | EM spectrum band table from ELF through THF |
| `orbital-mechanics-framework` | Governing physics -> equations -> mission applications framework |

## Findings

| Finding | Decision |
|---|---|
| No proof warnings in candidate baseline | Promote after cross-reference and invariant additions |
| Cross-reference surfaces were thin or absent | Fixed in all three guides before promotion |
| Opening figures needed regression locks | Fixed with Da Vinci invariants in `proof.toml` |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml translation\01-EQUIVALENCE-PROBLEM.md telecommunications\01-ELECTROMAGNETIC-SPECTRUM.md space-exploration\01-ORBITAL-MECHANICS.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-fifth-gold-promotion\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all three guides to Certified Gold.
