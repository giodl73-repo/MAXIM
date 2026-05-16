---
wave: fourth-gold-promotion
date_open: 2026-05-14
date_close: 2026-05-14
status: complete
source_wave: third-gold-promotion
---

# Fourth Gold Promotion

## Mission

Add mathematics/physics, engineering/mechanics, and arts/culture exemplars to
Certified Gold while preserving the same proof-first, invariant-backed workflow.

## Candidate Set

| Candidate | Section Coverage | Why this one |
|---|---|---|
| `mathematics/06-LINEAR-ALGEBRA.md` | Mathematics & Physics | Core mathematical substrate for computation, physics, optimization, and data science |
| `mechanical/01-THERMODYNAMICS.md` | Mechanics | Engineering foundation for cycles, entropy, exergy, refrigeration, and useful work |
| `art-history/03-RENAISSANCE.md` | Arts & Culture | Canonical art-historical period with technical, geographic, and patronage structure |

## Mechanical Gate

```powershell
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail mathematics\06-LINEAR-ALGEBRA.md mechanical\01-THERMODYNAMICS.md art-history\03-RENAISSANCE.md proof.toml
```

Result: pass.

## Content Actions Completed

| Action | File |
|---|---|
| Added stable Big Picture heading | `mathematics/06-LINEAR-ALGEBRA.md` |
| Repaired refrigeration-cycle ASCII box | `mechanical/01-THERMODYNAMICS.md` |
| Repaired oil-technique ASCII width | `art-history/03-RENAISSANCE.md` |
| Added cross-reference table | `mathematics/06-LINEAR-ALGEBRA.md` |
| Added cross-reference table | `mechanical/01-THERMODYNAMICS.md` |
| Added cross-reference table | `art-history/03-RENAISSANCE.md` |
| Added Da Vinci invariant | `linear-algebra-landscape` |
| Added Da Vinci invariant | `thermodynamics-work-entropy` |
| Added Da Vinci invariant | `renaissance-geography-chronology` |

## Score Table

| Guide | Tier | Average | Decision |
|---|---:|---:|---|
| `mathematics/06-LINEAR-ALGEBRA.md` | Gold | 4.7 | Broad and deep map from vector spaces to SVD, numerical LA, QM, and spectral theory |
| `mechanical/01-THERMODYNAMICS.md` | Gold | 4.6 | Engineering-first framing around useful work, entropy, cycles, and exergy |
| `art-history/03-RENAISSANCE.md` | Gold | 4.6 | Strong geography/chronology map plus technical perspective and oil-glaze analysis |

## Dimension Scores

| Dimension | Linear Algebra | Thermodynamics | Renaissance |
|---|---:|---:|---:|
| Landscape power | 5 | 4 | 5 |
| Layering integrity | 5 | 5 | 5 |
| ASCII precision | 4 | 5 | 5 |
| Explanatory compression | 5 | 4 | 4 |
| Decision utility | 5 | 5 | 4 |
| Confusion handling | 5 | 5 | 5 |
| Bridge quality | 5 | 4 | 4 |
| Cross-reference value | 5 | 5 | 5 |
| Voice | 4 | 5 | 5 |
| Factual confidence | 4 | 4 | 4 |

## Reader Task Results

| Guide | Reader Tasks Pass? | Notes |
|---|---|---|
| Linear Algebra | yes | Answers map/map-geometry, decomposition choice, SVD vs eigendecomposition, numerical stability, and QM observable questions |
| Thermodynamics | yes | Answers maximum work, entropy destruction, Carnot bounds, refrigeration COP, and cycle choice |
| Renaissance | yes | Answers chronological geography, perspective mechanics, disegno/colorito, Northern oil technique, and common myths |

## Closeout

Certified Gold now spans fourteen guides and includes the core mathematical,
engineering, and art-historical exemplar surfaces.
