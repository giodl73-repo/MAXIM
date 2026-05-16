# Gold Factory Wave 6

## Mission

Continue scaled Gold promotion with a proof-clean PDE and variational-calculus
cohort. Preserve exact-file gating: noisy numerical, complex-analysis, and
statistical-mechanics files are deferred rather than repaired opportunistically
inside the promotion wave.

## Scope

| Guide | Promotion Target | Invariant |
|---|---|---|
| `partial-differential-equations/01-CLASSIFICATION.md` | PDE classification exemplar | `pde-classification-determines` |
| `partial-differential-equations/02-FIRST-ORDER.md` | first-order PDE exemplar | `first-order-pde-taxonomy` |
| `partial-differential-equations/03-WAVE-EQUATION.md` | hyperbolic wave exemplar | `wave-equation-landscape` |
| `partial-differential-equations/04-HEAT-EQUATION.md` | parabolic heat exemplar | `heat-equation-landscape` |
| `partial-differential-equations/05-LAPLACE-POISSON.md` | elliptic equilibrium exemplar | `laplace-poisson-landscape` |
| `partial-differential-equations/06-FOURIER-METHODS.md` | spectral PDE methods exemplar | `fourier-methods-pde-landscape` |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | operator-inverse exemplar | `greens-function-concept` |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | weak formulation exemplar | `weak-formulation-concept` |
| `partial-differential-equations/09-NUMERICAL-PDES.md` | numerical PDE methods exemplar | `numerical-pde-methods-landscape` |
| `variational-calculus/01-FUNCTIONALS.md` | functional calculus exemplar | `functionals-vs-functions` |
| `variational-calculus/02-EULER-LAGRANGE.md` | Euler-Lagrange exemplar | `euler-lagrange-equation` |
| `variational-calculus/03-CONSTRAINTS.md` | constrained variation exemplar | `constrained-variation` |

## Baseline Findings

| Finding | Resolution |
|---|---|
| Numerical methods and complex analysis candidates had many ASCII/table defects | Deferred to repair lanes |
| Statistical mechanics had several table and ASCII defects | Deferred noisy files while retaining clean candidates for later |
| All nine PDE exact files proofed clean | Selected the full PDE ladder |
| Variational calculus 01-03 proofed clean | Added as the natural PDE-adjacent variational foundation |
| PDE 01 and variational 01-02 did not expose the standard `## The Big Picture` anchor | Normalized headings before adding invariants |

## Gold Rubric v2 Scores

| Guide | Explanation | Diagrams | Tables | Bridges | Cross-links | Proof | Overall |
|---|---:|---:|---:|---:|---:|---:|---:|
| `partial-differential-equations/01-CLASSIFICATION.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/02-FIRST-ORDER.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/03-WAVE-EQUATION.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/04-HEAT-EQUATION.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/05-LAPLACE-POISSON.md` | 4.6 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/06-FOURIER-METHODS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/07-GREENS-FUNCTIONS.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/08-VARIATIONAL-WEAK.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `partial-differential-equations/09-NUMERICAL-PDES.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `variational-calculus/01-FUNCTIONALS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |
| `variational-calculus/02-EULER-LAGRANGE.md` | 4.7 | 4.6 | 4.6 | 4.8 | 4.6 | 5.0 | 4.6 |
| `variational-calculus/03-CONSTRAINTS.md` | 4.6 | 4.6 | 4.6 | 4.7 | 4.6 | 5.0 | 4.6 |

## Reader-Task Checks

| Task Family | Representative Pass |
|---|---|
| PDE type ladder | Classification, first-order PDEs, wave, heat, Laplace/Poisson, Fourier, Green's functions, weak forms, and numerics form a full PDE path |
| Variational bridge | Functionals, Euler-Lagrange equations, and constraints bridge optimization to PDE and mechanics |
| Numerical/physical bridge | Weak forms, spectral methods, and Green's functions connect analysis to computation and signal-processing analogies |

## Validation

```powershell
git -C C:\src\maxim diff --check
Set-Location -LiteralPath C:\src\maxim
C:\src\proof\target\debug\proof.exe check --daVinci -e --no-fail proof.toml partial-differential-equations\01-CLASSIFICATION.md partial-differential-equations\02-FIRST-ORDER.md partial-differential-equations\03-WAVE-EQUATION.md partial-differential-equations\04-HEAT-EQUATION.md partial-differential-equations\05-LAPLACE-POISSON.md partial-differential-equations\06-FOURIER-METHODS.md partial-differential-equations\07-GREENS-FUNCTIONS.md partial-differential-equations\08-VARIATIONAL-WEAK.md partial-differential-equations\09-NUMERICAL-PDES.md variational-calculus\01-FUNCTIONALS.md variational-calculus\02-EULER-LAGRANGE.md variational-calculus\03-CONSTRAINTS.md
C:\src\proof\target\debug\proof.exe check -e --no-fail context\gold\REGISTRY.md context\waves\2026-05-14-gold-factory-wave-6\WAVE.md context\waves\PHASES.md
```

## Decision

Promote all twelve selected guides to Certified Gold. Defer the repair-heavy
numerical-methods, complex-analysis, and statistical-mechanics candidates to
targeted proof-repair waves.
