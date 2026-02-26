# 19th-Century Analysis — Cauchy, Riemann, Weierstrass, Cantor, Dedekind

## The Problem They Were Solving

By 1800, calculus was a century old and extraordinarily powerful. But it rested on
shaky foundations. Newton's "fluxions" and Leibniz's "infinitesimals" were criticized
by Berkeley as "ghosts of departed quantities" — you use them in calculations but
then discard them. Nobody had a precise definition of what a limit, a derivative,
or an integral actually *was*.

```
THE FOUNDATION CRISIS OF EARLY 19TH CENTURY
=============================================

What Cauchy found wrong:
  Fourier (1822): The heat equation's solution requires
  "any function" to have a Fourier series.
  But what IS a function? Can any arbitrary rule be a function?

  Early calculus: Differentiation was applied freely.
  Cauchy's question: When is it valid?

  Early series: Power series, Fourier series used freely.
  Cauchy's question: When do they converge?

What they built in response:
  Cauchy → rigorous limits, continuity, convergence tests
  Riemann → rigorous integral, complex analysis (Riemann surfaces)
  Weierstrass → epsilon-delta, pathological counterexamples
  Dedekind → real numbers from rationals (Dedekind cuts)
  Cantor → set theory, transfinite numbers, cardinality
```

---

## Augustin-Louis Cauchy (1789–1857)

### Who He Was

French mathematician. Prolific — published ~800 papers (second most ever, after Euler).
Worked as an engineer briefly, then became a professor. Royalist and devout Catholic;
exiled briefly after the 1830 revolution. His mathematics and his politics were both
uncompromising.

### The Contribution: Making Calculus Rigorous

**The Limit Definition of Derivative**

```
CAUCHY'S FORMALIZATION
=======================

Before Cauchy: "The derivative is the infinitely small change."
  Berkeley's objection: You compute dy/dx as if dx ≠ 0, then set dx = 0.
  This is inconsistent.

Cauchy's approach (Cours d'analyse, 1821):
  The derivative of f at x is:
    f'(x) = lim_{h→0} [f(x+h) - f(x)] / h

  "Limit" means: for any desired precision ε > 0, there exists δ > 0
  such that whenever |h| < δ, the ratio is within ε of the limit.

  No infinitesimals. No "ghosts." Just inequalities.

This made the derivative a DEFINED OBJECT, not a vague intuition.
The epsilon-delta machinery was refined by Weierstrass (see below).
```

**Continuity**

Cauchy defined continuity precisely: f is continuous at x if f(x+h) → f(x)
as h → 0. He introduced the intermediate value theorem proof: if f is
continuous on [a,b] with f(a) < 0 < f(b), then there exists c in (a,b)
with f(c) = 0. The proof uses the completeness of the real numbers.

**Complex Analysis — Cauchy's Theorem**

```
CAUCHY'S INTEGRAL THEOREM
==========================

If f(z) is analytic (complex-differentiable) in a region D,
then for any closed curve C in D:

  ∮_C f(z) dz = 0

Cauchy's Integral Formula: for z₀ inside C:
  f(z₀) = (1/2πi) ∮_C f(z)/(z-z₀) dz

Corollary: An analytic function is infinitely differentiable.
  (Compare: a real differentiable function need not be twice differentiable.)

Why this matters:
  - Computing real integrals via complex contours (residue theorem)
  - Signal processing: the z-transform residues
  - Control theory: poles of transfer functions
  - Fluid dynamics: complex potential for 2D flow
  - Quantum mechanics: propagators as contour integrals
```

**Convergence Tests**

Cauchy gave the first rigorous convergence tests for series:
- Cauchy root test: lim sup |aₙ|^(1/n) < 1 implies convergence
- Cauchy condensation test
- The Cauchy criterion: a sequence converges iff it is Cauchy
  (|aₘ - aₙ| → 0 as m,n → ∞)

---

## Bernhard Riemann (1826–1866)

### Who He Was

German mathematician. Student of Gauss. Died at 39 of tuberculosis.
In fewer than 40 years, he founded: Riemann surfaces, Riemannian geometry,
the Riemann integral, the Riemann zeta function (and the hypothesis),
and made fundamental contributions to complex analysis and trigonometric series.
He had one of the highest idea-per-year rates in mathematical history.

### The Contribution: Geometry, Integration, and the Zeta Function

**The Riemann Integral**

```
RIEMANN'S DEFINITION OF THE INTEGRAL
======================================

To define ∫_a^b f(x) dx rigorously:
  Partition [a,b] into n subintervals: a = x₀ < x₁ < ... < xₙ = b
  Pick any sample point cᵢ in each [xᵢ₋₁, xᵢ]
  Form the Riemann sum: Σᵢ f(cᵢ)(xᵢ - xᵢ₋₁)

  The integral is the limit of these sums as max(xᵢ - xᵢ₋₁) → 0,
  IF this limit is the same for all partitions and sample points.

What functions are Riemann integrable?
  - All continuous functions on [a,b]
  - Functions with finitely many discontinuities
  NOT: functions with "too many" discontinuities

Riemann gave a necessary and sufficient condition:
  f is Riemann integrable iff its set of discontinuities has
  measure zero. (This was later formalized by Lebesgue.)
```

**Riemannian Geometry**

Riemann's 1854 Habilitation lecture "On the Hypotheses that Lie at the
Foundations of Geometry" (published 1868) created differential geometry.

```
RIEMANNIAN GEOMETRY IN ONE DIAGRAM
=====================================

Euclidean space: flat, metric ds² = dx² + dy² + dz²

Riemann's generalization: The metric can vary from point to point.
  ds² = Σᵢⱼ gᵢⱼ dxⁱ dxʲ     (the metric tensor)

  gᵢⱼ encodes distances, angles, and curvature at every point.

Special cases:
  gᵢⱼ = δᵢⱼ (identity):    Euclidean space (flat)
  On a sphere of radius R:  ds² = R²(dθ² + sin²θ dφ²)
  Gauss curvature K = 1/R² > 0: positive curvature

Einstein (1915): Spacetime is a 4D Riemannian manifold (pseudo-Riemannian).
  The metric gᵢⱼ is determined by the distribution of mass-energy.
  General relativity is entirely written in Riemann's language.

Without Riemann's 1854 lecture, general relativity as Einstein wrote it
would be impossible — the mathematical language didn't exist before Riemann.
```

**The Riemann Hypothesis**

```
THE RIEMANN HYPOTHESIS
=======================

Euler's zeta function: ζ(s) = Σ₁^∞ 1/nˢ converges for Re(s) > 1.

Riemann (1859) extended ζ to all complex s ≠ 1 using analytic continuation.

The Riemann Hypothesis: All non-trivial zeros of ζ(s) lie on
  the "critical line" Re(s) = 1/2.

Why it matters:
  The distribution of primes is controlled by the zeros of ζ(s).
  The prime counting function π(x) ~ Li(x) + error.
  If RH is true, the error is O(√x log x) — the "best possible."
  If RH is false, primes are distributed more erratically.

Current status: Verified for the first 10¹³ zeros.
  Still unproved (or disproved) in general.
  One of the Millennium Prize Problems: $1,000,000 prize.

The statement seems simple. The implications reach throughout
number theory, cryptography, and the distribution of primes.
```

**Riemann Surfaces**

A Riemann surface is a 1D complex manifold — a way of making multi-valued
complex functions (like √z or log z) single-valued by "unfolding" the domain.
The function w = √z has two "sheets"; its Riemann surface is topologically
a sphere with a handle (genus 1). Riemann surfaces connect complex analysis
to topology to algebraic geometry. Grothendieck's program built on this.

---

## Karl Weierstrass (1815–1897)

### Who He Was

German mathematician. "Father of modern analysis." Worked as a high school teacher
for 14 years before his mathematical work was recognized — published major results
in an obscure school journal. At 40, appointed to the University of Berlin.
Built the rigorous epsilon-delta foundations through his lectures, which were
written up by students and circulated widely.

### The Contribution: Epsilon-Delta and Pathological Functions

**Epsilon-Delta Formalism**

```
THE EPSILON-DELTA DEFINITION
==============================

Cauchy had the right ideas; Weierstrass made them completely rigorous.

"f is continuous at a" means:
  ∀ε > 0, ∃δ > 0 such that |x - a| < δ → |f(x) - f(a)| < ε

"lim_{x→a} f(x) = L" means:
  ∀ε > 0, ∃δ > 0 such that 0 < |x - a| < δ → |f(x) - L| < ε

These definitions:
  1. Eliminate infinitesimals entirely — pure finite inequalities
  2. Are logically precise — can be verified or refuted
  3. Distinguish "continuous at a point" from "uniformly continuous"
     (whether δ can be chosen independently of where you are)
  4. Make pathological cases visible (see below)

The universal quantifier + existential quantifier structure (∀ε ∃δ) is
exactly the structure you saw in formal logic and type theory at MIT.
Weierstrass essentially wrote formal logic into analysis.
```

**Pathological Functions — The Monsters**

Weierstrass constructed functions that violate "obvious" intuitions:

```
WEIERSTRASS'S CONTINUOUS NOWHERE-DIFFERENTIABLE FUNCTION
=========================================================

W(x) = Σₙ₌₀^∞ aⁿ cos(bⁿ π x)
  where 0 < a < 1, b is a positive odd integer, and ab > 1 + 3π/2

This function is:
  - Continuous everywhere (converges uniformly, limits of continuous functions)
  - Differentiable NOWHERE (infinitely jagged at every scale)

Before Weierstrass, mathematicians assumed continuous = "almost everywhere
differentiable." Riemann had an example; Weierstrass made it rigorous
and shocking.

Modern interpretation: Weierstrass functions are fractals before fractals
were named. They have non-integer (fractal) dimension. They are "typical"
in the function space C[0,1] — most continuous functions are nowhere
differentiable. The "nice" functions are the exceptional ones.
```

**Uniform Convergence**

The distinction Weierstrass made rigorous: pointwise convergence vs. uniform
convergence of a sequence of functions.

```
POINTWISE VS UNIFORM CONVERGENCE
==================================

Pointwise: fₙ(x) → f(x) for each fixed x, but δ may depend on x.
Uniform: ∀ε, ∃N such that for all n ≥ N and ALL x: |fₙ(x) - f(x)| < ε
  N is independent of x.

Why it matters:
  Cauchy "proved" that a convergent series of continuous functions is
  continuous — but his proof was wrong! He assumed uniform convergence
  without recognizing it was a special condition.

  Weierstrass fixed this: the sum of uniformly convergent continuous
  functions is continuous.

  This distinction matters everywhere in analysis, PDEs, Fourier theory.
```

**Weierstrass Approximation Theorem**

Every continuous function on [a,b] can be uniformly approximated by polynomials.
This is the foundation for numerical approximation theory — splines, Bernstein
polynomials, and the theoretical basis for why polynomial interpolation works.

---

## Georg Cantor (1845–1918)

### Who He Was

German mathematician. Created set theory and the theory of infinite cardinals.
Faced intense opposition from Kronecker ("God made the integers; all else is
the work of man"), whose attacks may have contributed to Cantor's mental illness.
Spent time in psychiatric institutions. His work was not widely accepted in his
lifetime; Hilbert later said "No one shall expel us from the paradise that
Cantor has created."

### The Contribution: Transfinite Mathematics

**Diagonal Argument — Uncountability of the Reals**

```
CANTOR'S DIAGONAL ARGUMENT (1891)
===================================

Claim: The real numbers in [0,1] cannot be listed in a sequence.
  (They are "uncountably infinite" — more numerous than the integers.)

Proof by contradiction:
  Suppose they can be listed: r₁, r₂, r₃, ...

  Write each in decimal:
    r₁ = 0.d₁₁ d₁₂ d₁₃ d₁₄ ...
    r₂ = 0.d₂₁ d₂₂ d₂₃ d₂₄ ...
    r₃ = 0.d₃₁ d₃₂ d₃₃ d₃₄ ...
    ...
  (The diagonal digits are d₁₁, d₂₂, d₃₃, ...)

  Construct d: define d = 0.e₁ e₂ e₃ ...
  where eₙ = 5 if dₙₙ ≠ 5, else eₙ = 6
  (Just pick anything different from the diagonal digit.)

  Then d differs from r₁ in digit 1, from r₂ in digit 2,
  from r₃ in digit 3, and so on.
  So d is NOT in the list — contradiction.

This same structure (the diagonal argument) reappears in:
  - Russell's paradox (the set of all sets that don't contain themselves)
  - Godel's incompleteness theorem
  - Turing's halting problem undecidability
  - Rice's theorem
  - Tarski's undefinability theorem

The diagonal argument is one of the great proof techniques.
You know it from your TCS background — Turing's proof is exactly this.
```

**Cardinality — Infinite Sets Have Different Sizes**

```
CANTOR'S HIERARCHY OF INFINITIES
==================================

ℵ₀ (aleph-null): the cardinality of the natural numbers N
  Sets of cardinality ℵ₀: N, Z (integers), Q (rationals)
  These can all be put in 1-1 correspondence with N (they are "countable")

  Example: Rationals are countable. Arrange as:
    1/1, 1/2, 2/1, 1/3, 2/2, 3/1, 1/4, 2/3, 3/2, 4/1, ...
  (diagonal traversal of the grid of fractions — a bijection with N)

𝔠 (cardinality of the continuum): cardinality of R
  𝔠 = 2^ℵ₀ > ℵ₀
  R is strictly larger than N (proved by the diagonal argument)

  Also: 𝔠 = cardinality of [0,1] = R = R² = Rⁿ for any finite n
  (There's a bijection between [0,1] and the entire plane — surprising!)

ℵ₁, ℵ₂, ...: larger infinite cardinals
  Cantor's theorem: |P(S)| > |S| for any set S
  (The power set is strictly larger than the original set.)
  This gives an infinite tower of infinities.

The Continuum Hypothesis: Is 2^ℵ₀ = ℵ₁?
  (Is the cardinality of the reals the "next" infinity after ℵ₀?)
  Godel (1940): CH cannot be disproved from ZFC
  Cohen (1963): CH cannot be proved from ZFC
  CH is independent of ZFC — you can assume it or its negation.
```

**The Impact on Mathematics' Self-Understanding**

Set theory became the **foundation** of mathematics — the language in which
all other mathematics is expressed. ZFC (Zermelo-Fraenkel with Choice) axioms
are the standard foundation. Every mathematical object (number, function,
relation, structure) is defined as a set. This is Cantor's legacy.

---

## Richard Dedekind (1831–1916)

### Who He Was

German mathematician. Student of Gauss and Riemann. Friend of Cantor. Made
algebraic number theory rigorous. Also defined the real numbers via "Dedekind cuts."

### The Contribution: Real Numbers and Algebraic Structures

**Dedekind Cuts — Constructing the Reals**

```
DEDEKIND CUTS
==============

Problem: What IS √2? Or π? These are not fractions.
  We use them in calculations but haven't defined them rigorously.

Dedekind's solution (1872): Define a real number AS a "cut" in the rationals.

A Dedekind cut (A, B) is a partition of Q into two sets such that:
  - A ∪ B = Q, A ∩ B = ∅
  - A is non-empty and B is non-empty
  - Every a ∈ A is less than every b ∈ B
  - A has no greatest element

The cut "is" the real number at the dividing point.

Example: √2 is the cut:
  A = {r ∈ Q : r < 0 or r² < 2}
  B = {r ∈ Q : r ≥ 0 and r² ≥ 2}

This defines √2 WITHOUT assuming it exists first.
You can then define addition/multiplication of cuts, prove the axioms,
and show the resulting system is complete (no gaps).

This construction:
  - Makes real numbers rigorous from rational numbers
  - Proves the least upper bound property (every bounded set has a sup)
  - Establishes that the reals are the unique complete ordered field
```

**Algebraic Number Theory — Ideals**

Working with algebraic integers (roots of monic polynomials with integer
coefficients), unique factorization can fail:
In Z[√-5]: 6 = 2 × 3 = (1 + √-5)(1 - √-5)
These are two genuinely different factorizations — unique factorization fails.

Dedekind's solution: factor not into **elements** but into **ideals** —
the right notion for "virtual factors." Unique factorization into prime ideals
always holds. This is the foundation of algebraic number theory and is why
the concept of "ideal" is called an ideal.

Modern algebra: rings, ideals, quotient rings — the entire structure comes
from Dedekind's work, later systematized by Noether.

---

## Comparison Table

| Figure | Dates | Blocked Problem | Key Tool Invented | Legacy |
|--------|-------|-----------------|-------------------|--------|
| **Cauchy** | 1789–1857 | Rigor for limits/derivatives | Limit definition, complex integral | All of analysis on solid footing |
| **Riemann** | 1826–1866 | What IS an integral? What IS geometry? | Riemann integral, metric tensor, ζ(s) | General relativity, complex analysis, RH |
| **Weierstrass** | 1815–1897 | When can you interchange limits? | Epsilon-delta, uniform convergence | Modern analysis, approximation theory |
| **Cantor** | 1845–1918 | Are all infinities equal? | Set theory, diagonal argument, cardinality | All of modern mathematics (foundational language) |
| **Dedekind** | 1831–1916 | What ARE real numbers? | Dedekind cuts, ideals | Foundations, algebraic number theory |

---

## Who to Cite for What

| Concept | Cite | Notes |
|---------|------|-------|
| Rigorous limits and derivatives | Cauchy (then Weierstrass) | Cauchy started, Weierstrass completed |
| Cauchy's integral theorem / formula | Cauchy | Complex analysis foundation |
| Riemann integral definition | Riemann | The standard integral in intro calculus |
| Riemannian geometry / metric tensor | Riemann | *Über die Hypothesen* 1854 |
| Riemann hypothesis | Riemann | *Über die Anzahl der Primzahlen* 1859 |
| Riemann surfaces | Riemann | Complex analysis, algebraic geometry |
| Epsilon-delta definition (complete) | Weierstrass | After Cauchy's sketches |
| Uniform convergence (as distinct concept) | Weierstrass | Critical for Fourier series |
| Nowhere-differentiable continuous function | Weierstrass | Broke "obvious" intuition |
| Uncountability of the reals | Cantor | Diagonal argument (1891) |
| Cardinality / aleph numbers | Cantor | Set theory |
| Set theory (Naive) | Cantor | Paradoxes led to ZFC |
| Diagonal argument (general technique) | Cantor | Used by Godel, Turing, Russell |
| Dedekind cuts (real number construction) | Dedekind | 1872 |
| Ideals in rings | Dedekind | Algebraic number theory |

---

## Common Confusion Points

**"Weierstrass invented epsilon-delta"** — Cauchy introduced the framework; Weierstrass
systematized it into the form we use. The key Weierstrass contributions: distinguishing
pointwise from uniform convergence, recognizing Cauchy's errors, constructing
counterexamples. Attribution: Cauchy-Weierstrass for the whole edifice.

**"The diagonal argument is Turing's"** — Cantor's diagonal argument predates
Turing by ~50 years (1891 vs 1936). Turing's halting problem proof uses the
same structure but in a different setting (programs instead of decimal expansions).
The technique is Cantor's. The credit for applying it to computation is Turing's.

**"Cantor's set theory caused the foundations crisis"** — Cantor's set theory was
one trigger. Russell's paradox (1901 — the set of all sets that don't contain
themselves) showed that *naive* set theory was inconsistent. This led to ZFC
axiomatization (Zermelo 1908, Fraenkel 1922). The crisis was productive —
it forced mathematics to confront its foundations.

**"Real numbers are 'obvious'"** — Before Dedekind and Cantor, nobody had
rigorously defined them. Dedekind cuts, Cauchy sequences, and the axiom of
completeness (every Cauchy sequence converges) are all 19th-century inventions.
The "obvious" real number line is actually a 19th-century construction.

**"The Riemann Hypothesis is about random primes"** — The primes have a definite
pattern; the hypothesis is about the precision of our best approximation formula.
The zeros of the zeta function encode deviations from the asymptotic prime-counting
formula. If RH is true, these deviations are "small" in a precise sense.
