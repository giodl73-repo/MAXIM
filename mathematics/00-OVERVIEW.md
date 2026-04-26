# 00-OVERVIEW — Mathematics: The Dependency Map

> 24 modules, ~1,600 pages. Every branch of mathematics in this library connects
> to every other through a web of prerequisites, shared structures, and recurring
> ideas. This file is the map of that web — the dependency DAG, the groupings,
> the bridge points to computation and physics, and the decision tree for
> "where do I start?"

---

## The Mathematical Landscape

```
THE MATHEMATICAL LANDSCAPE — DEPENDENCY ARCHITECTURE
═══════════════════════════════════════════════════════════════════════════════════

  FOUNDATIONS                          ANALYSIS                  TRANSFORMS
  ┌──────────────────────┐             ┌────────────────────┐    ┌──────────────┐
  │ 03 Trigonometry      │             │ 01 Vector Calculus  │    │ 12 Fourier   │
  │ 04 Power Series      │             │ 02 Integral Thms    │    │ 13 Laplace   │
  │ 05 Groups/Sets/Alg.  │             │ 07 DiffEq           │    └──────┬───────┘
  │ 06 Linear Algebra    │             │ 14 Complex Analysis │           │
  └──────────┬───────────┘             │ 21 Measure Theory   │           │
             │                         │ 23 Functional Anal. │           │
             │                         └────────┬───────────┘           │
             │                                  │                       │
             │          GEOMETRY / TOPOLOGY      │        APPLIED       │
             │          ┌────────────────────┐   │    ┌────────────────┐│
             ├────────→ │ 08 Topology        │   │    │ 11 Probability ││
             │          │ 09 Manifolds       │   ├──→ │ 15 Optimization││
             │          │ 10 Diff. Geometry  │   │    │ 17 Combinatorics│
             │          └────────────────────┘   │    │ 19 Numerical   ││
             │                                   │    │ 20 Statistics  ││
             │          ALGEBRA (ADVANCED)        │    └────────────────┘│
             │          ┌────────────────────┐   │                      │
             └────────→ │ 18 Number Theory   │   │    STRUCTURE         │
                        │ 22 Category Theory │   │    ┌────────────────┐│
                        │ 24 Representation  │   └──→ │ 16 Info Theory ││
                        └────────────────────┘        └────────────────┘│
                                                                        │
═══════════════════════════════════════════════════════════════════════════════════
```

**What the diagram encodes.** The arrows are not just "A comes before B" — they are
logical dependencies. You can read Topology (08) without Measure Theory (21), but
you cannot read Functional Analysis (23) without both. Linear Algebra (06) feeds
into nearly everything. Category Theory (22) sits above, providing a language that
unifies the structures in every other module — but you can ignore it entirely and
still do all the mathematics in the other 23.

---

## The Dependency DAG

This is the full prerequisite graph. An arrow A --> B means "material in A is
assumed by B." Transitive dependencies are omitted (if A-->B-->C, the arrow A-->C
is not drawn).

```
PREREQUISITE DAG — READ BOTTOM TO TOP
═══════════════════════════════════════════════════════════════════════════════════

                        ┌──────────────────┐
                        │  22 CATEGORY     │  (reads all other modules as examples)
                        │     THEORY       │
                        └──────────────────┘

        ┌──────────────────┐          ┌──────────────────┐
        │  24 REPRESENTATION│          │  23 FUNCTIONAL   │
        │     THEORY        │          │     ANALYSIS     │
        └────────┬─────────┘          └────┬─────┬───────┘
                 │                         │     │
    ┌────────────┤              ┌──────────┘     │
    │            │              │                 │
    │   ┌────────┴────────┐    │    ┌────────────┴──────────┐
    │   │ 05 GROUPS/SETS  │    │    │   21 MEASURE THEORY   │
    │   │    ALGEBRA       │    │    └────────────┬──────────┘
    │   └────────┬────────┘    │                 │
    │            │              │                 │
    │            │    ┌────────┴────────┐        │
    │            │    │ 10 DIFF. GEOM. │         │
    │            │    └────┬───────────┘         │
    │            │         │                    │
    │            │    ┌────┴───────────┐        │
    │            │    │  09 MANIFOLDS  │        │
    │            │    └────┬───────────┘        │
    │            │         │                    │
    │   ┌────────┴────┐   │    ┌───────────────┴─────┐
    │   │ 08 TOPOLOGY │   │    │ 14 COMPLEX ANALYSIS │
    │   └─────────────┘   │    └──────────┬──────────┘
    │                      │               │
    │   ┌─────────────┐   │    ┌──────────┴──────────┐
    │   │ 18 NUMBER   │   │    │  04 POWER SERIES    │
    │   │    THEORY    │   │    └──────────┬──────────┘
    │   └──────┬──────┘   │               │
    │          │          │               │
    │   ┌──────┴─────────┐│    ┌──────────┴──────────┐
    │   │ 17 COMBIN. /   ││    │  07 DIFFEQ          │
    │   │    GRAPHS       ││    └──────────┬──────────┘
    │   └──────┬─────────┘│               │
    │          │           │    ┌──────────┴──────────┐
    │          │           │    │ 02 INTEGRAL THMS    │
    │          │           │    └──────────┬──────────┘
    │          │           │               │
    │          │           │    ┌──────────┴──────────┐
    │          │           │    │ 01 VECTOR CALC      │
    │          │           │    └──────────┬──────────┘
    │          │           │               │
    ├──────────┴───────────┴───────────────┤
    │                                      │
    │        ┌──────────────────────┐      │
    │        │  06 LINEAR ALGEBRA   │       │
    │        └──────────┬──────────┘       │
    │                   │                   │
    │        ┌──────────┴──────────┐       │
    │        │  03 TRIGONOMETRY     │       │
    │        └─────────────────────┘       │
    │                                       │
    ═════════════════════════════════════════

  PARALLEL TRACKS (each depends on subsets above):

  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐
  │11 PROB.   │  │12 FOURIER │  │13 LAPLACE │  │15 OPTIM.  │  │16 INFO    │
  │ ← 21,06  │  │ ← 14,06  │  │ ← 14,07  │  │ ← 06,01  │  │ ← 11,21  │
  │           │  │           │  │           │  │           │  │           │
  │20 STATS   │  │           │  │           │  │19 NUMER.  │  │           │
  │ ← 11,06  │  │           │  │           │  │ ← 06,07  │  │           │
  └───────────┘  └───────────┘  └───────────┘  └───────────┘  └───────────┘
```

### Deepest Dependency Chains

The longest paths through the DAG, showing which topics require the most accumulated
machinery:

```
Chain 1 — Representation Theory (8 deep):
  Trig → LinAlg → Groups → Topology → Manifolds → DiffGeom → RepTheory
  (03)    (06)     (05)     (08)       (09)        (10)       (24)

Chain 2 — Functional Analysis (7 deep):
  Trig → LinAlg → VectorCalc → IntegralThms → DiffEq → PowerSeries → ComplexAnal → MeasureTheory → FunctionalAnal
  (03)    (06)     (01)         (02)           (07)     (04)          (14)          (21)            (23)

Chain 3 — Information Theory via Probability (5 deep):
  LinAlg → MeasureTheory → Probability → Statistics → InfoTheory
  (06)     (21)            (11)          (20)          (16)
```

These chains explain why certain subjects feel hard — it is not that the ideas are
intrinsically difficult, it is that six layers of prerequisite structure must be
loaded first. Representation theory is not harder than trigonometry. It just sits
higher in the dependency tree.

---

## Groupings

The 24 modules cluster into five natural groups. Within each group, the ordering
is by dependency depth (read top to bottom within a group).

### Group 1: Foundations (the load-bearing layer)

Everything else sits on these. Linear algebra in particular is the most-depended-on
module in the entire library.

| # | Module | Core Ideas |
|---|--------|------------|
| 03 | Trigonometry | Identities, polar coordinates, the unit circle as the simplest Lie group |
| 04 | Power Series | Taylor/Maclaurin, convergence radii, generating functions |
| 05 | Groups / Sets / Algebra | Groups, rings, fields, ideals, quotient structures — the algebraic toolkit |
| 06 | Linear Algebra | Eigenvalues, SVD, spectral theorem, tensor products — the universal workhorse |

### Group 2: Analysis (the continuous world)

The study of limits, continuity, and integration — the mathematics of physics.

| # | Module | Core Ideas |
|---|--------|------------|
| 01 | Vector Calculus | Gradient, divergence, curl — Maxwell's equations decoded |
| 02 | Integral Theorems | Green's, Stokes', Divergence theorem — the d-squared-is-zero hierarchy |
| 07 | Differential Equations | ODEs, PDEs, separation of variables, Sturm-Liouville |
| 14 | Complex Analysis | Holomorphic functions, Cauchy integral formula, residues, conformal maps |
| 21 | Measure Theory | sigma-algebras, Lebesgue integration, L^p spaces, Radon-Nikodym |
| 23 | Functional Analysis | Banach/Hilbert spaces, spectral theorem for operators, Fredholm theory |

### Group 3: Geometry and Topology (shape and structure)

What persists under deformation (topology) and what depends on measurement (geometry).

| # | Module | Core Ideas |
|---|--------|------------|
| 08 | Topology | Metric spaces, compactness, connectedness, homotopy, homology, TDA |
| 09 | Manifolds | Smooth manifolds, tangent bundles, differential forms, Stokes on manifolds |
| 10 | Differential Geometry | Curvature, connections, Riemannian geometry, Gauss-Bonnet |

### Group 4: Algebra (advanced structures)

Building on Group 1's foundations to study symmetry, structure, and classification.

| # | Module | Core Ideas |
|---|--------|------------|
| 18 | Number Theory | Primes, modular arithmetic, quadratic reciprocity, Dirichlet, RSA |
| 22 | Category Theory | Categories, functors, natural transformations, adjunctions, monads |
| 24 | Representation Theory | Lie groups/algebras, Schur's lemma, characters, SU(2)/SU(3) |

### Group 5: Applied Mathematics (tools that touch the world)

Each of these applies the pure machinery to solve problems in engineering, science,
data analysis, and computation.

| # | Module | Core Ideas |
|---|--------|------------|
| 11 | Probability | Measure-theoretic probability, CLT, large deviations, stochastic processes |
| 12 | Fourier Analysis | Series, transform, DFT/FFT, Parseval, convolution theorem |
| 13 | Laplace Transform | Circuit analysis, transfer functions, z-transform |
| 15 | Optimization | Convex/non-convex, KKT conditions, duality, LP/QP/SDP, gradient descent |
| 16 | Information Theory | Entropy axioms, channel capacity, rate-distortion, Kullback-Leibler |
| 17 | Combinatorics & Graphs | Generating functions, Ramsey theory, network flows, matching |
| 19 | Numerical Methods | Floating point, root finding, quadrature, interpolation, FEM |
| 20 | Statistics | MLE/MAP, hypothesis testing, confidence intervals, regression, bootstrap |

---

## Mathematics as Experimental Discovery

A word on how to read these modules.

Mathematics is often presented as a deductive chain: axioms first, then theorems,
then applications. That is how it is *verified*, not how it is *discovered*. The
actual history runs backwards. Euler computed specific sums and noticed patterns.
Riemann explored a particular function and conjectured. Galois solved a concrete
problem (which polynomials can be solved by radicals?) and the entire theory of
groups fell out as a byproduct.

The Experimenter's frame: every theorem in this library was once a *conjecture
someone tested*. The integral theorems (02) started as observations about fluid
flow and heat — Gauss and Stokes noticed that certain volume integrals always
equaled certain surface integrals, tried enough cases to be sure, then found the
proof. Category theory (22) did not emerge from abstract contemplation — it was
forced into existence because the same structural patterns kept appearing in
topology, algebra, and geometry, and Eilenberg-Mac Lane finally said: "These
patterns are the mathematics, not the specific objects."

Three investigative stances recur throughout:

**1. The right abstraction reveals hidden unity.**
Linear algebra (06) is a single subject, but it shows up as matrix mechanics in
quantum physics, as the spectral theorem in functional analysis, as SVD in data
science, as tensor products in representation theory. The abstraction is not a
flight from reality — it is the discovery that apparently different phenomena
share the same structural skeleton.

**2. The obstruction is the invariant.**
Topology (08) and number theory (18) both work the same way: you want to prove
something is impossible (these two spaces are not homeomorphic; this equation has
no solution), so you construct an *invariant* — a quantity that does not change
under the allowed transformations — and show it differs. The fundamental group,
the Euler characteristic, quadratic residues — all are obstructions. The theorem
was not inevitable; someone had to invent the right invariant.

**3. Duality doubles your theorems for free.**
A theorem about compact spaces gives you a theorem about discrete spaces by
duality. A theorem about convex optimization gives you a theorem about the dual
problem. Pontryagin duality connects the Fourier transform on groups to the
structure of their character groups. Poincare duality connects homology and
cohomology. Once you see the duality, you get two theorems for the price of one.
This is not a trick — it is a structural feature of mathematics that category
theory (22) makes precise.

---

## Bridge: Mathematics and Computation

You know Godel, Church, Turing from the TCS side. Here is where those ideas
surface across the library, and where modern computation returns the favor.

### Curry-Howard-Lambek: Proofs Are Programs Are Morphisms

The three-way correspondence (detailed in 22-CATEGORY-THEORY) maps:

```
LOGIC                    TYPE THEORY              CATEGORY THEORY
─────────────────────    ─────────────────────    ─────────────────────
Proposition              Type                     Object
Proof                    Program / Term           Morphism
Conjunction A ^ B        Product type A x B       Categorical product
Disjunction A v B        Sum type A + B           Coproduct
Implication A -> B       Function type A -> B     Exponential object
True                     Unit type                Terminal object
False                    Empty type               Initial object
Universal quantifier     Polymorphic type         End
```

This is not analogy. A proof in intuitionistic logic *is* a lambda term *is* a
morphism in a Cartesian closed category. Lean 4, Coq, and Agda all rest on this
correspondence — their proof kernels are typed lambda calculi.

### Automated Theorem Proving: Lean, Coq, and the Formalization Project

| System | Foundation | Notable Achievements |
|--------|-----------|---------------------|
| Lean 4 + Mathlib | Dependent type theory (CIC variant) | 150,000+ theorems, formalizing undergrad math |
| Coq | Calculus of Inductive Constructions | CompCert (verified C compiler), Feit-Thompson |
| Agda | Martin-Lof type theory | HoTT library, cubical type theory |
| Isabelle/HOL | Higher-order logic | Kepler conjecture (Flyspeck project) |

The workflow: state a theorem as a type, construct a proof as a term of that type,
let the kernel verify. Where it intersects this library:

- **Measure theory (21)**: Mathlib has Lebesgue measure, L^p spaces, Radon-Nikodym.
- **Topology (08)**: Lean has metric spaces, compactness, connectedness formalized.
- **Category theory (22)**: Mathlib's category theory library is one of its largest.
- **Number theory (18)**: Formalization of quadratic reciprocity, class field theory in progress.

### Computational Complexity as Mathematical Structure

The P vs NP question is not just a question about algorithms — it is a question
about the structure of mathematics itself:

```
COMPLEXITY CLASS    MATHEMATICAL ANALOG              MODULE CONNECTION
──────────────────────────────────────────────────────────────────────
P                   problems solvable in poly-time    19 (numerical methods)
NP                  problems verifiable in poly-time  17 (combinatorics)
#P                  counting problems                 11 (probability via counting)
BPP                 randomized poly-time              11 (probabilistic methods)
PSPACE              polynomial space                  (game-theoretic connections)
IP = PSPACE         interactive proofs                18 (number theory — primality)
```

The complexity of optimization problems (15) depends on convexity: convex problems
are in P, general nonlinear programming is NP-hard. The complexity of linear
algebra (06) operations determines the practical limits of numerical methods (19).

### The Unreasonable Effectiveness

Wigner's 1960 observation keeps getting confirmed. The mathematics in this library
was not developed *for* physics and engineering — but it turns out to be exactly
what they need:

```
MATHEMATICS DEVELOPED FOR...        LATER ESSENTIAL IN...
──────────────────────────────────────────────────────────────────────
Riemannian geometry (pure math)     General relativity (1915)
Group theory (abstract algebra)     Particle physics (Standard Model)
Hilbert spaces (functional anal.)   Quantum mechanics
Random matrices (prob/stats)        Nuclear energy levels, wireless comms
Topology (pure math)                Topological insulators, condensed matter
Category theory (pure math)         Programming language semantics, databases
Information theory (comm. eng.)     Statistical mechanics, ML, neuroscience
Fourier analysis (heat equation)    Signal processing, MRI, JPEG
Number theory (pure math)           Cryptography (RSA, elliptic curves)
```

This is not a coincidence to be explained away — it is evidence that mathematical
structure is *discovered*, not invented. The modules are empirical reports.

---

## Module Map

Complete cross-reference: every module, its prerequisites, and where else in the
library it is used.

| # | File | Topic | Prerequisites | You Will Use This In... |
|---|------|-------|---------------|------------------------|
| 01 | `VECTOR-CALC` | Gradient, divergence, curl, Laplacian | 03, 06 | physics/, electronics/, fluid-dynamics/, meteorology/ |
| 02 | `INTEGRAL-THEOREMS` | Green's, Stokes', Divergence theorem | 01 | physics/, aeronautics/, electrical-grid/ |
| 03 | `TRIG` | Identities, inverse trig, polar coords | -- | signal-processing/, acoustics/, astronomy/ |
| 04 | `POWER-SERIES` | Taylor/Maclaurin, convergence, generating fns | 03 | 14, 17, numerical-methods/, physics/ |
| 05 | `GROUPS-SETS-ALGEBRA` | Groups, rings, fields, ideals, quotients | 06 | 08, 18, 22, 24, cryptography/, coding-theory |
| 06 | `LINEAR-ALGEBRA` | Eigenvalues, SVD, spectral thm, tensors | 03 | *nearly everything* — physics/, data-science/, ai-engineering/, quantum-computing/ |
| 07 | `DIFFEQ` | ODEs, PDEs, Laplacian, separation of variables | 01, 02, 06 | physics/, control-theory/, electronics/, chemical-eng/ |
| 08 | `TOPOLOGY` | Metric spaces, compactness, homotopy, homology, TDA | 05, 06 | physics/ (gauge theory), data-science/ (TDA), robotics/ |
| 09 | `MANIFOLDS` | Smooth manifolds, tangent bundles, forms, Stokes on manifolds | 06, 08 | 10, 24, differential-geometry/, physics/ (GR) |
| 10 | `DIFF-GEOMETRY` | Curvature, connections, Riemannian/pseudo-Riemannian | 06, 09 | physics/ (GR), 24, robotics/, computer-graphics |
| 11 | `PROBABILITY` | Measure-theoretic prob, CLT, large deviations, stochastic processes | 06, 21 | 16, 20, ai-engineering/, finance/, game-theory/ |
| 12 | `FOURIER` | Series, transform, DFT/FFT, Parseval, convolution | 06, 14 | signal-processing/, acoustics/, data-science/, physics/ |
| 13 | `LAPLACE` | Transfer functions, z-transform, circuit analysis | 07, 14 | control-theory/, electronics/, signal-processing/ |
| 14 | `COMPLEX-ANALYSIS` | Holomorphic fns, Cauchy, residues, conformal maps | 04, 06 | 12, 13, 21, 23, physics/ (QFT), aeronautics/ |
| 15 | `OPTIMIZATION` | Convex/non-convex, KKT, duality, LP/QP/SDP | 01, 06 | ai-engineering/, finance/, operations-research, control-theory/ |
| 16 | `INFORMATION-THEORY` | Entropy, channel capacity, rate-distortion, KL divergence | 11, 21 | ai-engineering/, cryptography/, data-science/, neuroscience/ |
| 17 | `COMBINATORICS-GRAPHS` | Generating fns, Ramsey, network flows, matching | 04, 05 | computing/ (algorithms), game-theory/, logistics |
| 18 | `NUMBER-THEORY` | Primes, modular arith, quadratic reciprocity, RSA | 05 | cryptography/, computing/ (hashing), coding-theory |
| 19 | `NUMERICAL-METHODS` | Floating point, root finding, quadrature, FEM | 06, 07 | computing/, physics/ (simulations), data-science/ |
| 20 | `STATISTICS` | MLE/MAP, hypothesis testing, CI, regression, GLMs, bootstrap | 06, 11 | data-science/, medicine/, psychology/, economics/ |
| 21 | `MEASURE-THEORY` | sigma-algebras, Lebesgue integral, L^p spaces, Radon-Nikodym | 06, 14 | 11, 16, 23, probability-statistics/ |
| 22 | `CATEGORY-THEORY` | Categories, functors, natural transforms, adjunctions, monads | 05, 06 (+ examples from all) | computing/ (PL theory), formal-methods/, languages/ (Haskell) |
| 23 | `FUNCTIONAL-ANALYSIS` | Banach/Hilbert spaces, spectral theorem, distributions, Fredholm | 06, 14, 21 | physics/ (QM), signal-processing/, PDEs |
| 24 | `REPRESENTATION-THEORY` | Lie groups/algebras, Schur's lemma, characters, SU(2)/SU(3) | 05, 06, 09, 10 | physics/ (Standard Model), crystallography/, chemistry/ |

### Key Numbers

```
Total modules:                 24
Total estimated pages:         ~1,600
Deepest dependency chain:      8 modules (03 → 06 → 05 → 08 → 09 → 10 → 24)
Most-depended-on module:       06 Linear Algebra (prerequisite for 19 of 24)
Most cross-references:         06 Linear Algebra → used in 12+ other library dirs
Modules with no prerequisites: 03 Trigonometry (the root)
Terminal modules (nothing depends on them):
    12 Fourier, 13 Laplace, 15 Optimization, 16 Info Theory,
    19 Numerical Methods, 20 Statistics, 22 Category Theory
```

---

## Decision Cheat Sheet

| I need to understand... | Start with module... | Then... |
|-------------------------|---------------------|---------|
| Maxwell's equations | 01 Vector Calc → 02 Integral Theorems | physics/ |
| Quantum mechanics | 06 Linear Algebra → 23 Functional Analysis | physics/ |
| Machine learning math | 06 Linear Algebra → 15 Optimization → 11 Probability | ai-engineering/ |
| Cryptography (RSA, ECC) | 05 Groups/Sets → 18 Number Theory | cryptography/ |
| Signal processing | 06 Linear Algebra → 14 Complex Analysis → 12 Fourier | signal-processing/ |
| Control systems | 07 DiffEq → 13 Laplace | control-theory/ |
| General relativity | 06 LinAlg → 08 Topology → 09 Manifolds → 10 Diff Geom | physics/ |
| Particle physics (Standard Model) | 05 Groups → 24 Representation Theory | physics/ |
| Data science / statistics | 06 LinAlg → 11 Probability → 20 Statistics | data-science/ |
| Topological data analysis | 06 LinAlg → 08 Topology (Section 10) | data-science/ |
| Numerical simulation (FEM/CFD) | 06 LinAlg → 07 DiffEq → 19 Numerical Methods | computing/ |
| Information theory / coding | 11 Probability → 16 Information Theory | cryptography/, data-science/ |
| Functional programming theory | 05 Groups/Sets → 22 Category Theory | computing/, languages/ |
| Convex optimization for ML | 06 LinAlg → 15 Optimization | ai-engineering/ |
| Combinatorial algorithms | 04 Power Series → 17 Combinatorics & Graphs | computing/ |
| Financial modeling | 11 Probability → 20 Statistics | finance/ |
| Type theory / proof assistants | 05 Groups/Sets → 22 Category Theory | formal-methods/ |

### Reading Order by Goal

**Path A: The Physicist's Track**
```
03 Trig → 06 LinAlg → 01 VecCalc → 02 IntThms → 07 DiffEq → 14 Complex
    → 12 Fourier → 13 Laplace → 23 Functional Analysis
Side quest: 08 Topology → 09 Manifolds → 10 DiffGeom (for GR/gauge theory)
```

**Path B: The Data Scientist's Track**
```
06 LinAlg → 11 Probability → 20 Statistics → 15 Optimization
    → 16 Information Theory
Side quest: 08 Topology Section 10 (TDA), 19 Numerical Methods
```

**Path C: The Pure Mathematician's Track**
```
05 Groups/Sets → 06 LinAlg → 08 Topology → 09 Manifolds → 10 DiffGeom
    → 14 Complex Analysis → 21 Measure Theory → 23 Functional Analysis
Side quest: 18 Number Theory, 22 Category Theory, 24 Representation Theory
```

**Path D: The Computer Scientist's Track**
```
06 LinAlg → 05 Groups/Sets → 17 Combinatorics → 11 Probability
    → 15 Optimization → 22 Category Theory
Side quest: 18 Number Theory (for crypto), 16 Info Theory
```

---

## The Recurring Structures

Five structural patterns recur across the entire library. Recognizing them is
the difference between learning 24 separate subjects and learning one subject
with 24 expressions.

### 1. Linearity

A map T is linear if T(ax + by) = aT(x) + bT(y). That is the definition, and it
shows up in:

```
MODULE                WHERE LINEARITY APPEARS
──────────────────────────────────────────────────────────────────────
06 Linear Algebra     The entire subject
01 Vector Calculus    Gradient, divergence, curl are linear operators
07 DiffEq            Linear ODEs/PDEs → superposition principle
12 Fourier           Fourier transform is a linear map L^2 → L^2
23 Functional Anal.  Bounded linear operators on Banach/Hilbert spaces
15 Optimization      Linear programming: linear objective + linear constraints
```

When a problem is linear, you can decompose it, solve the pieces, and add the
solutions. This is why linear algebra (06) is the most universal module.

### 2. The Exact Sequence / d-squared-is-zero

The identity d^2 = 0 appears in at least four disguises:

```
CONTEXT              INCARNATION
──────────────────────────────────────────────────────────
01 Vector Calculus   curl(grad f) = 0,  div(curl F) = 0
02 Integral Thms     boundary of a boundary is empty
08 Topology          chain complex: boundary operator partial^2 = 0
09 Manifolds         exterior derivative: d^2 omega = 0
22 Category Theory   chain complexes as functors, derived categories
```

This is *one mathematical fact* wearing different costumes. The exterior derivative
d generalizes all the vector calculus operators, and its nilpotency d^2 = 0 is what
makes cohomology work. Modules 01, 02, 08, and 09 are all telling the same story.

### 3. Duality

For almost every construction in mathematics, there is a dual construction obtained
by "reversing arrows" or "swapping roles."

```
PRIMAL                      DUAL                           MODULE
──────────────────────────────────────────────────────────────────────
Vector space V              Dual space V*                   06
Homology H_n                Cohomology H^n                  08, 09
Optimization primal         Lagrangian dual                 15
Group G                     Character group G^              24
Locally compact abelian G   Pontryagin dual G^              12 (Fourier)
Category C                  Opposite category C^op          22
Measure mu                  Radon-Nikodym derivative        21
Direct limit                Inverse limit                   22
```

### 4. The Universal Property Pattern

Rather than defining an object by its internal construction, define it by its
*relationship to all other objects* — the universal property. This is the central
idea of category theory (22), but it pervades the library:

```
OBJECT                  UNIVERSAL PROPERTY SAYS...                     MODULE
──────────────────────────────────────────────────────────────────────────────
Tensor product V tensor W  Universal bilinear map                       06
Free group on S           Universal group with generators S              05
Quotient ring R/I         Universal ring killing I                       05
Completion of metric space Universal complete metric space containing X  08
Stone-Cech compactification Universal compact space containing X         08
Adjoint pair F -| G       Universal relation: Hom(FA,B) ~ Hom(A,GB)     22
```

### 5. Spectral Methods

Decompose a problem into its "frequency components," solve each independently,
then recombine. The Fourier transform (12) is the archetype, but the pattern is
everywhere:

```
CONTEXT                    "FREQUENCIES"                    MODULE
──────────────────────────────────────────────────────────────────────
Fourier analysis           Sines/cosines (eigenfns of d/dx) 12
Linear algebra             Eigenvalues/eigenvectors          06
Functional analysis        Spectrum of an operator           23
Representation theory      Irreducible representations       24
Number theory              Characters mod n                  18
Quantum mechanics          Energy eigenstates                physics/
```

The spectral theorem (06, 23) is the rigorous version: a self-adjoint operator on a
Hilbert space can be decomposed into its spectral projections. Every application of
"expand in a basis and solve term-by-term" is this theorem in action.

---

## Connections Across the Library

The mathematics modules are not self-contained — they provide the language and tools
used throughout every other directory.

```
LIBRARY DIRECTORY           PRIMARY MATH MODULES USED
══════════════════════════════════════════════════════════════════════════════
physics/                    01, 02, 06, 07, 08, 09, 10, 14, 23, 24
electronics/                01, 07, 12, 13, 06
ai-engineering/             06, 11, 15, 16, 20
data-science/               06, 11, 15, 16, 19, 20
cryptography/               05, 18, 16
signal-processing/          06, 12, 13, 14
control-theory/             06, 07, 13, 15
quantum-computing/          06, 08, 23, 24
information-theory/         11, 16, 21
numerical-methods/          06, 07, 14, 19
probability-statistics/     06, 11, 20, 21
differential-geometry/      06, 09, 10
topology (standalone dir)   08, 09
complex-analysis (dir)      14
game-theory/                06, 11, 15, 17
finance/                    11, 15, 20
computer-architecture/      17 (Boolean algebra, combinatorial logic)
machine-learning-theory/    06, 11, 15, 16, 20
```

---

## Common Confusion Points

**"Linear algebra is easy — I took it as a freshman."**
The freshman course covers matrix multiplication and Gaussian elimination. The
real linear algebra — spectral theory, tensor products, dual spaces, multilinear
maps — is the foundation of quantum mechanics, data science, and half of applied
mathematics. Module 06 goes past the freshman version. If you have not seen the
singular value decomposition derived from the spectral theorem, or tensor products
defined by a universal property, there is material here.

**"Topology and analysis look like separate subjects."**
They are the same subject viewed from different distances. Analysis asks "what
is the limit of this sequence?" Topology asks "in what structure does that
question even make sense?" Measure theory (21) connects them: the Lebesgue
integral is the completion of the Riemann integral in a topological sense
(L^p spaces are complete, the space of Riemann-integrable functions is not).
Functional analysis (23) is the synthesis: topology + algebra + analysis on
infinite-dimensional spaces.

**"Category theory is too abstract to be useful."**
Category theory is the study of the *structural patterns* that recur across
every other branch. Adjunctions, limits, and natural transformations are not
abstractions for their own sake — they are the reason that free groups, tensor
products, and completions all behave similarly. If you find yourself saying
"this proof looks like a proof I saw in a different subject," category theory
(22) is the explanation. It also directly grounds the semantics of typed
programming languages (Curry-Howard-Lambek), Haskell's type class hierarchy,
and the algebraic theory of databases.

**"I can never remember which integral theorem to use."**
They are all one theorem: Stokes' theorem on manifolds, which says the
integral of d(omega) over a region M equals the integral of omega over the
boundary of M. Green's theorem, the divergence theorem, and the classical
Stokes' theorem are special cases for different dimensions and different
types of forms. Module 02 makes this explicit; module 09 gives the general
version.

**"Measure theory exists only to torture analysis students."**
No. Measure theory exists because Riemann integration breaks on limits.
There exist sequences of Riemann-integrable functions whose pointwise limit
is not Riemann-integrable. Lebesgue integration fixes this: the dominated
convergence theorem and the monotone convergence theorem give you clean
conditions under which limits and integrals commute. Without measure theory,
probability theory cannot be made rigorous (what is P(X in A) if A is not
measurable?), and functional analysis cannot define L^2 as a Hilbert space.

**"Why are there both Fourier and Laplace transforms?"**
Fourier (12) decomposes functions into sinusoidal frequencies — it works on
L^2 functions and is an isometry (Parseval/Plancherel). Laplace (13) introduces
exponential damping (the real part of s), which lets it handle growing functions
and transient behavior that Fourier cannot. The Laplace transform evaluated on
the imaginary axis *is* the Fourier transform: F(omega) = L{f}(s=i*omega).
Fourier is for steady-state and spectral analysis; Laplace is for initial-value
problems and transfer functions.

**"Representation theory and linear algebra are the same thing."**
Not quite. Linear algebra studies vector spaces and linear maps.
Representation theory studies how *groups* (or algebras) *act* on vector spaces
via linear maps. The distinction: in linear algebra, the map is the object of
study; in representation theory, the *group element* is the object of study, and
the linear map is how it acts. The payoff is that group-theoretic questions
(which are hard) become linear-algebraic questions (which are tractable). Module
24 makes this conversion explicit for Lie groups and their algebras.

---

*The landscape. The dependency DAG. The recurring structures. Now pick a path
and start reading — the modules are ordered so that every prerequisite comes
before the module that needs it.*
