# Gold Factory Wave 3

## Mission

Continue scaled Gold promotion with exact-file scouting and a math-heavy cohort.
Avoid directory fallback noise, promote only proof-clean topology and number
theory guides, and leave information-theory/signal-processing repairs for a
separate diagram/table wave.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `topology/01-METRIC-SPACES.md` | metric-space foundation exemplar | `metric-spaces-concrete-foundation` |
| `topology/02-TOPOLOGICAL-SPACES.md` | open-set framework exemplar | `topological-spaces-framework` |
| `topology/03-CONTINUITY-HOMEOMORPHISM.md` | topological map hierarchy exemplar | `topological-maps-hierarchy` |
| `topology/04-COMPACTNESS.md` | compactness exemplar | `compactness-finite-cover` |
| `topology/05-CONNECTEDNESS.md` | connectedness hierarchy exemplar | `connectedness-hierarchy` |
| `topology/06-FUNDAMENTAL-GROUP.md` | loop invariant exemplar | `fundamental-group-loops` |
| `topology/08-COHOMOLOGY.md` | cohomology ring-structure exemplar | `cohomology-dual-ring-structure` |
| `topology/09-MANIFOLDS.md` | locally Euclidean space exemplar | `manifolds-locally-euclidean` |
| `topology/10-APPLICATIONS.md` | applied topology exemplar | `topology-applications-domains` |
| `number-theory/01-DIVISIBILITY-PRIMES.md` | divisibility and prime foundation exemplar | `divisibility-lattice-primes` |
| `number-theory/04-QUADRATIC-RECIPROCITY.md` | quadratic reciprocity exemplar | `quadratic-reciprocity-map` |
| `number-theory/05-DIOPHANTINE-EQUATIONS.md` | Diophantine methods exemplar | `diophantine-equations-classes-methods` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| Exact topology/number-theory scout found 15 proof-clean candidates | Selected 12 for a coherent topology-first math cohort |
| Information Theory 01, 03, and 05 had table/ASCII defects | Deferred to information-theory repair lane |
| Signal-processing candidates were not needed after the topology/number lane was clean | Left for a later cohort |
| Earlier number-theory command noise came from a wrong/nonexistent path falling back to directory proof | Used exact existing filenames only in this wave |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `topology/01-METRIC-SPACES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/02-TOPOLOGICAL-SPACES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/03-CONTINUITY-HOMEOMORPHISM.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/04-COMPACTNESS.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `topology/05-CONNECTEDNESS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/06-FUNDAMENTAL-GROUP.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/08-COHOMOLOGY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/09-MANIFOLDS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `topology/10-APPLICATIONS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `number-theory/01-DIVISIBILITY-PRIMES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `number-theory/04-QUADRATIC-RECIPROCITY.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `number-theory/05-DIOPHANTINE-EQUATIONS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| Point-set topology ladder | Metric spaces, topological spaces, maps, compactness, and connectedness form the foundation sequence |
| Algebraic topology bridge | Fundamental group, cohomology, manifolds, and applications connect spaces to algebraic invariants |
| Number-theory bridge | Divisibility, quadratic reciprocity, and Diophantine equations provide arithmetic foundations adjacent to algebra |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml topology\01-METRIC-SPACES.md topology\02-TOPOLOGICAL-SPACES.md topology\03-CONTINUITY-HOMEOMORPHISM.md topology\04-COMPACTNESS.md topology\05-CONNECTEDNESS.md topology\06-FUNDAMENTAL-GROUP.md topology\08-COHOMOLOGY.md topology\09-MANIFOLDS.md topology\10-APPLICATIONS.md number-theory\01-DIVISIBILITY-PRIMES.md number-theory\04-QUADRATIC-RECIPROCITY.md number-theory\05-DIOPHANTINE-EQUATIONS.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-gold-factory-wave-3\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve selected guides to Certified Gold. Defer Information Theory
and Signal Processing to a later proof-repair or clean-candidate wave.
