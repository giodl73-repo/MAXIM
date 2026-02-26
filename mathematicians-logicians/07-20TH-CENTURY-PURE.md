# 20th-Century Pure Mathematics — Hardy, Ramanujan, Von Neumann, Bourbaki, Weil, Grothendieck

## The 20th Century: Abstraction at Full Power

The 19th century built rigor. The 20th century used that rigor to build structures
of extraordinary abstraction — and then, astonishingly, found those structures
governing quantum mechanics, number theory, and everything else.

```
20TH CENTURY PURE MATHEMATICS — CONCEPTUAL MAP
================================================

ANALYSIS                 ALGEBRA / GEOMETRY        FOUNDATIONS
--------                 ------------------        -----------
Hardy (analytic NT,      Von Neumann (operator      Hilbert (1900–)
  G.H. Hardy)              algebras, QM, games)     Gödel (1930–)
Ramanujan (partitions,   Noether (abstract           ↓
  modular forms)           algebra — File 05)       Bourbaki group
Hardy-Ramanujan          Weil (arithmetic           (1935–)
  number theory           geometry, conjectures)    Axiomatics as a
  partnership            Grothendieck (categories,   cultural program
                           schemes, K-theory)
                         Atiyah (index theorem,
                           K-theory, topology)

KEY THEME: "Pure" math that physics needed
  Hilbert spaces → quantum mechanics
  Von Neumann algebras → quantum field theory
  Lie groups → gauge theory / Standard Model
  Differential geometry → general relativity
  K-theory → string theory, condensed matter
```

---

## G.H. Hardy (1877–1947)

### Who He Was

British mathematician, Cambridge and Oxford. Legendary figure in analytic number
theory and analysis. Author of *A Mathematician's Apology* (1940) — the most
celebrated account of what it feels like to be a mathematician.

Hardy is inseparable from Ramanujan: one of the most extraordinary intellectual
partnerships in history.

### The Contribution: Analytic Number Theory and Hardy-Weinberg

**The Hardy-Ramanujan Theorem**

```
PARTITION NUMBERS — THE PROBLEM
=================================

The partition function p(n) counts the number of ways to write n
as an unordered sum of positive integers.

p(1) = 1:  {1}
p(2) = 2:  {2}, {1+1}
p(3) = 3:  {3}, {2+1}, {1+1+1}
p(4) = 5:  {4}, {3+1}, {2+2}, {2+1+1}, {1+1+1+1}
p(5) = 7
p(10) = 42
p(50) = 204,226
p(100) = 190,569,292
p(200) = 3,972,999,029,388

The numbers grow FAST. Is there a formula?

Hardy and Ramanujan (1918): The asymptotic formula for p(n):

  p(n) ~ (1/(4n√3)) · exp(π√(2n/3))  as n → ∞

This is the Hardy-Ramanujan asymptotic formula.
Later, Rademacher found an exact series (not just asymptotic).

The method: "circle method" — use complex analysis (integrals around
a circle in the complex plane) to extract information about a power
series coefficient. This method is now a standard tool.
```

**Hardy-Weinberg Equilibrium (Genetics)**

Hardy's one contribution outside pure mathematics: he showed in a 1908 letter
that in a large random-mating population with no selection, the allele
frequencies remain constant from generation to generation. The Hardy-Weinberg
equilibrium is the null model of population genetics. Hardy himself considered
it trivial; Wilhelm Weinberg proved it independently.

**Hardy's Mathematical Values**

Hardy believed mathematics should be "useless" — pure curiosity, aesthetic,
not applied. Famously: "I have never done anything 'useful'. No discovery of mine
has made, or is likely to make, directly or indirectly, for good or ill, the least
difference to the amenity of the world."

Ironic postscript: The Hardy-Weinberg formula is used in genetic testing and
forensic genetics. The circle method is used in cryptography and coding theory.

**The Critical Line in the Zeta Function**

Hardy proved (1914) that infinitely many zeros of the Riemann zeta function lie
on the critical line Re(s) = 1/2. This does not prove the Riemann Hypothesis
(which requires ALL non-trivial zeros to lie there), but it was the first
concrete progress.

---

## Srinivasa Ramanujan (1887–1920)

### Who He Was

Indian mathematician from Madras. Largely self-taught from Carr's *Synopsis of
Pure Mathematics*. Wrote to Hardy in 1913 with a letter containing theorems —
Hardy immediately recognized extraordinary talent. Came to Cambridge 1914, died
of illness in 1920 at age 32.

Hardy said of their collaboration: "He could remember the idiosyncrasies of
numbers in an almost uncanny way." When Hardy visited Ramanujan in hospital
and mentioned arriving in taxi number 1729, Ramanujan immediately said:
"No, it is a very interesting number; it is the smallest number expressible
as the sum of two cubes in two different ways."

1729 = 1³ + 12³ = 9³ + 10³. The "taxicab number."

### The Contribution: Modular Forms and Infinite Series

**Mock Theta Functions and Modular Forms**

```
WHAT RAMANUJAN DISCOVERED
==========================

Ramanujan discovered, largely without proof, thousands of identities.
Many were not understood until decades later.

Examples of Ramanujan's identities:

1/1 + 1/(1+1) + 1/(1+2/1+2/...) = (√5 - 1)/2  [a continued fraction = φ⁻¹]

Σₙ₌₀^∞ (2n choose n)³ = π/(Γ(1/4))⁴ · 4/(2π)  [hypergeometric series for 1/π]

More famously:
  1 + 2 + 3 + 4 + ... = -1/12

This is NOT saying the series converges. It's the regularized value:
ζ(-1) = -1/12 (Riemann zeta function evaluated at -1).
This regularization is physically real in quantum field theory
(Casimir effect uses zeta regularization).

MODULAR FORMS:
  A modular form of weight k is a function f: H → C (H = upper half-plane)
  satisfying: f((az+b)/(cz+d)) = (cz+d)^k f(z) for (a b; c d) ∈ SL(2,Z)

  Ramanujan's tau function τ(n): coefficients of Δ(z) = q ∏(1-qⁿ)²⁴
  Ramanujan conjectured |τ(p)| ≤ 2p^(11/2) for prime p.
  Proved by Pierre Deligne (1974) using algebraic geometry Ramanujan couldn't access.
```

**The Ramanujan-Hardy Method (Circle Method)**

Together with Hardy, developed the powerful "circle method" for extracting
series coefficients via complex integration. Ramanujan identified which "major
arcs" contributed most to the integral. This method is foundational in
modern analytic number theory.

**Rogers-Ramanujan Identities**

1 + q/(1-q) + q⁴/((1-q)(1-q²)) + ... = ∏_{n≡±1 (mod 5)} 1/(1-qⁿ)

These appear in the theory of integer partitions, exactly solvable models in
statistical mechanics (Baxter's hard hexagon model), conformal field theory,
and string theory. Ramanujan discovered them; their significance unfolded over
a century.

**Mathematical Legacy**

Ramanujan's notebooks (published posthumously, fully analyzed by Bruce Berndt
1985–1998) contained thousands of results. The "lost notebook" (found by George
Andrews in 1976 in a storage box in Trinity College) contained mock theta functions
whose theory was only completed by Ken Ono and Kathrin Bringmann in 2002–2012.

---

## John von Neumann (1903–1957)

### Who He Was

Hungarian-American mathematician. Child prodigy who memorized telephone books.
PhD at 22 with a dissertation on set theory and logic (under Hilbert's influence),
having simultaneously received a diploma in chemical engineering in Zurich.
Worked on: quantum mechanics, game theory, set theory, logic, ergodic theory,
operator algebras, numerical analysis, the Manhattan Project, and the design
of modern computers.

### The Contribution: The Architecture of Modern Computation and Science

**Von Neumann Architecture**

```
VON NEUMANN ARCHITECTURE (1945 EDVAC Report)
=============================================

The architecture of essentially every computer built since 1945:

  ┌────────────────────────────────────────────────────┐
  │                    BUS                              │
  │  ┌──────────┐   ┌──────────┐   ┌──────────────┐   │
  │  │   CPU    │   │ Control  │   │    Memory    │   │
  │  │ (ALU +   │   │  Unit    │   │  (program +  │   │
  │  │ registers│   │          │   │   data       │   │
  │  └──────────┘   └──────────┘   │   unified)   │   │
  │                                └──────────────┘   │
  │  ┌──────────────────────────────────────────────┐  │
  │  │               I/O                            │  │
  │  └──────────────────────────────────────────────┘  │
  └────────────────────────────────────────────────────┘

Key innovations:
  1. STORED PROGRAM: Instructions stored in same memory as data.
     Program can modify itself (or read its own code).
  2. FETCH-DECODE-EXECUTE cycle: Uniform instruction processing.
  3. Random access to memory (vs. sequential tape).
  4. Binary arithmetic (influenced by his collaborations with logicians).

"Von Neumann bottleneck": CPU and memory connected by a single bus.
  Data must flow through this bottleneck.
  Modern solutions: cache hierarchy, DMA, SIMD, GPU parallelism.

You have built systems on this architecture for 30 years.
Every Azure VM, every .NET runtime, every SQL Server instance
runs on it.
```

**Quantum Mechanics Formalization**

Von Neumann's *Mathematische Grundlagen der Quantenmechanik* (1932)
put quantum mechanics on rigorous mathematical footing:

- Quantum states are **unit vectors** in a Hilbert space H
- Observables are **self-adjoint operators** on H
- Measurement collapses the state to an eigenstate (von Neumann measurement)
- Von Neumann entropy: S = -Tr(ρ log ρ) — the quantum analog of Shannon entropy

**Von Neumann Algebras**

A von Neumann algebra is a *-algebra of bounded operators on a Hilbert space,
closed in the weak operator topology. These are the natural algebraic structures
for quantum observables. Classification:
- Type I: matrix algebras, quantum mechanics of particles
- Type II: free probability, random matrices
- Type III: quantum field theory, black hole entropy

**Game Theory**

Von Neumann proved the **minimax theorem** (1928):
In a zero-sum two-player game, max_{x} min_{y} f(x,y) = min_{y} max_{x} f(x,y).
The minimax value exists. This is the mathematical foundation of game theory.
He and Morgenstern wrote *Theory of Games and Economic Behavior* (1944),
founding mathematical economics.

Nash (File 09) extended this to non-zero-sum games.

---

## Nicolas Bourbaki

### Who "He" Was

Bourbaki is not a person. It is a collective pseudonym for a group of
French mathematicians who began meeting in 1934–1935. Original members:
Henri Cartan, Claude Chevalley, Jean Dieudonné, Szolem Mandelbrojt,
René de Possel, Jean Delsarte, and André Weil. Later members included
Laurent Schwartz, Jean-Pierre Serre, Alexander Grothendieck.

Goal: Write mathematics entirely from scratch, rigorously, starting from
set theory and rebuilding all of it in modern axiomatic form.

### The Contribution: Mathematical Language and Culture

```
BOURBAKI'S "ÉLÉMENTS DE MATHÉMATIQUE"
=======================================

A multi-volume series beginning with set theory, then:
  - Algebra (groups, rings, modules, fields)
  - General topology
  - Functions of a real variable
  - Topological vector spaces
  - Integration
  - Lie groups and Lie algebras
  - Commutative algebra
  - Spectral theories
  - Differential and analytic manifolds
  - ...

STYLE: Ruthlessly abstract. No motivation. No examples until after the theory.
  Theorem-proof-theorem-proof. No diagrams.
  "Dangerous bend" symbol (☡) for especially subtle points.

IMPACT:
  1. Standardized notation and language across French (and then all)
     mathematics
  2. The "axiomatic style" — every concept rigorously defined
  3. Set the culture of pure mathematics for 40 years
  4. Influenced how mathematics is TAUGHT at universities worldwide
  5. The bourbakistes trained many students who dominated 20th-century math

CRITICISM:
  - No diagrams, no intuition, no motivation
  - Made mathematics inaccessible to outsiders
  - "Bourbakization" = abstraction for its own sake
  - Fields like combinatorics, computational math, probability that
    don't fit the clean Bourbaki framework were neglected by French math
```

---

## André Weil (1906–1998)

### Who He Was

French mathematician, founding member of Bourbaki, brother of philosopher
Simone Weil. Made fundamental contributions to algebraic geometry, number
theory, and the connections between them.

### The Contribution: Weil Conjectures and the Unity of Number Theory

**The Weil Conjectures (1949)**

```
WEIL CONJECTURES
=================

Context: Count solutions to polynomial equations mod p.
  If f(x,y) = 0 defines a curve over a finite field F_p,
  let Nₙ = number of solutions over F_{pⁿ} (field with pⁿ elements).

  Form the generating function: Z(T) = exp(Σ Nₙ Tⁿ/n)

WEIL CONJECTURED (1949):
  1. RATIONALITY: Z(T) is a rational function of T.
  2. FUNCTIONAL EQUATION: Z satisfies a symmetry relating T and 1/pⁿT.
  3. RIEMANN HYPOTHESIS ANALOG: The zeros of Z lie on the "critical arc"
     |T| = p^{-j/2} for appropriate j.
  4. CONNECTION TO TOPOLOGY: The degree of numerator/denominator equals
     the Betti numbers of the corresponding complex variety.

WHY SHOCKING:
  The conjectures connect:
    - Arithmetic (counting solutions over finite fields)
    - Topology (Betti numbers of manifolds)
  These were considered completely separate domains.

PROOFS:
  (1) Rationality: Dwork (1960) — using p-adic analysis
  (2) Functional equation: Grothendieck (1965) — étale cohomology
  (3) Riemann hypothesis: Deligne (1974) — Weil II, using Grothendieck's machinery
  (4) Connection to topology: Grothendieck's entire program

The Weil conjectures motivated Grothendieck to rebuild algebraic geometry
from scratch (see below). Deligne's proof of the Riemann analog won him
the Fields Medal.
```

---

## Alexander Grothendieck (1928–2014)

### Who He Was

Stateless German-born French mathematician. Father was a Russian anarchist,
killed in Auschwitz. Mother was German. Born in Berlin. Grew up in internment
camps in France. Completely self-taught in mathematics.

The most influential mathematician of the second half of the 20th century.
Rebuilt algebraic geometry from the ground up, creating the language
of schemes, categories, and cohomology that now pervades all of pure mathematics.

In 1970, abandoned mathematics and mainstream society, becoming a recluse.
In retirement, wrote *Récoltes et Semailles* (1986) — a 2000-page philosophical
meditation on mathematics and his estrangement from the mathematical community.

### The Contribution: The Language of Modern Mathematics

**The Key Conceptual Shifts**

```
GROTHENDIECK'S REBUILDING OF ALGEBRAIC GEOMETRY
=================================================

OLD APPROACH (classical): Study varieties as sets of solutions
  f(x,y) = 0 over the complex numbers — a geometric object in Cⁿ
  The geometry comes from the topology of Cⁿ.

GROTHENDIECK'S APPROACH: Schemes
  Don't just look at solutions over C.
  Look at solutions over ALL rings simultaneously.
  A "scheme" is a space that encodes a ring:
    Spec(R) = the set of prime ideals of R, with a topology and structure sheaf.

  This allows:
    - Geometry over finite fields (for number theory)
    - Geometry over Z (connecting number theory and geometry)
    - Infinitesimal deformations (formal schemes)
    - Everything at once

WHY POWERFUL:
  The SAME theorem about a variety applies simultaneously to:
    - Its solutions over Q (rational points — Fermat's Last Theorem territory)
    - Its solutions over Z/pZ (finite field counting — Weil conjectures)
    - Its solutions over C (complex topology)
  All these are "the same variety" in Grothendieck's scheme language.
```

**Topos Theory**

A topos is a generalization of a category of sheaves — it behaves like
a "universe of sets" but may be non-classical. Grothendieck toposes are
used in:
- Algebraic geometry: étale topos for proving Weil conjectures
- Logic: the internal logic of a topos is intuitionistic logic
- Computer science: categorical logic, type theory, realizability toposes

This is where Grothendieck's work meets the logic thread (Frege-Russell-Gödel):
the categorical foundations of logic.

**Categorical Thinking**

```
CATEGORIES AS THE LANGUAGE OF MATHEMATICS
==========================================

A category C consists of:
  - Objects: Ob(C)
  - Morphisms: for each pair (A,B) ∈ Ob(C)×Ob(C), a set Hom(A,B)
  - Composition: f: A→B, g: B→C gives g∘f: A→C
  - Identity: idₐ: A→A with identity laws

A functor F: C → D maps objects to objects and morphisms to morphisms,
preserving composition and identity.

A natural transformation η: F → G maps between functors.

WHAT THIS CAPTURES:
  - Structure-preserving maps between structures
  - "The same" structure in different settings
  - Adjunctions: the fundamental pattern in mathematics

  Left adjoint ⊣ Right adjoint:
    Free ⊣ Forgetful (free group is left adjoint to underlying set)
    Colimit ⊣ Diagonal ⊣ Limit
    Quantification ⊣ Substitution (in predicate logic)

Category theory has permeated:
  - Programming language theory (monads, functors in Haskell)
  - Proof theory (proof nets, categorical logic)
  - Topology (algebraic topology, homological algebra)
  - Physics (topological quantum field theory, string theory)
```

**The SGA, EGA, and Mathematical Hegemony**

Grothendieck and his collaborators (Serre, Deligne, Verdier, Giraud, Illusie...)
produced *Éléments de géométrie algébrique* (EGA) and *Séminaire de géométrie
algébrique du Bois Marie* (SGA) — thousands of pages of foundational material
rewriting algebraic geometry.

Deligne (his student) used this machinery to prove the Weil conjectures' Riemann
analog (1974). Wiles (in a different lineage) used descended techniques to prove
Fermat's Last Theorem (1995).

Grothendieck's impact: essentially all research-level algebraic geometry, algebraic
number theory, and much of algebraic topology is written in his language.

---

## Comparison Table

| Figure | Dates | Core Contribution | Abstraction Level | Modern Impact |
|--------|-------|-------------------|-------------------|---------------|
| **Hardy** | 1877–1947 | Analytic NT, rigorous analysis, Hardy-Ramanujan | High but concrete | Analytic number theory toolkit |
| **Ramanujan** | 1887–1920 | Modular forms, partition asymptotics, infinite series | High with mystical element | Mock theta → string theory, physics |
| **Von Neumann** | 1903–1957 | Operator algebras, QM formalization, game theory, computer architecture | Extremely high and broad | Everything — computers, physics, economics |
| **Bourbaki** | 1935– | Formal axiomatics, mathematical language | Maximally abstract | Mathematical culture, teaching, standardization |
| **Weil** | 1906–1998 | Arithmetic geometry, Weil conjectures | Extremely high | Number theory-geometry connection |
| **Grothendieck** | 1928–2014 | Schemes, topos theory, categorical foundations | Highest | All of modern pure mathematics |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Hardy-Ramanujan partition formula | Hardy + Ramanujan | 1918, circle method |
| Circle method in analytic NT | Hardy + Ramanujan | Standard now |
| Von Neumann architecture | Von Neumann | 1945 EDVAC report |
| Quantum mechanics formalization | Von Neumann | *Mathematische Grundlagen* 1932 |
| Minimax theorem | Von Neumann | Foundation of game theory |
| Von Neumann entropy | Von Neumann | -Tr(ρ log ρ) |
| Axiomatic style in mathematics | Bourbaki | *Éléments de Mathématique* |
| Weil conjectures (connection of arithmetic/topology) | Weil | 1949 |
| Étale cohomology (proof of Weil conjectures) | Grothendieck | SGA 4 |
| Schemes (algebraic geometry foundation) | Grothendieck | EGA |
| Topos theory | Grothendieck | Generalized set theory |
| Category theory as mathematical foundation | Grothendieck + Eilenberg + MacLane | |
| Adjoint functors | Kan (but developed in Grothendieck's framework) | "Kan extensions are everywhere" |

---

## Common Confusion Points

**"Ramanujan just guessed formulas"** — He derived them using methods he rarely
wrote down. When his notebooks were fully analyzed (Berndt, 1985–1998), essentially
every identity was correct. His methods were real — a combination of the *Synopsis*
he had studied, his own algebraic intuitions, and extraordinary facility with
modular forms and continued fractions. He was not guessing; he was working in
a private notation.

**"Von Neumann invented the computer"** — He formalized and systematized the
stored-program architecture, primarily in the 1945 EDVAC report. Zuse (Germany),
Atanasoff-Berry, Eckert-Mauchly (ENIAC) made earlier physical computing devices.
Alan Turing provided the theoretical foundation. Von Neumann's contribution was
the architectural synthesis that became standard.

**"Bourbaki was bad for mathematics"** — This is debated. Bourbaki provided
indispensable rigorous foundations and standardized language. The criticism
is the *style* — no motivation, no pictures, no applications — which they
took too far. In France, it led to a generation of students who could prove
theorems they didn't understand geometrically. But the *content* of Bourbaki
is still the standard algebraic and topological language.

**"Grothendieck's work is inaccessible to applied mathematics"** — Category theory
and topos theory are actively used in: type theory (Haskell monads are functors),
database theory (categorical query languages), program semantics (denotational
semantics), quantum computing (categorical quantum mechanics), and machine learning
theory (natural gradient via information geometry). Grothendieck's concepts percolate.
