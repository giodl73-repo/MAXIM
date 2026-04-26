# Metric Spaces

## The Big Picture

```
+====================================================================+
|              METRIC SPACES — THE CONCRETE FOUNDATION               |
+====================================================================+
|                                                                    |
|  METRIC d: X × X → R satisfying:                                 |
|  1. d(x,y) = 0 iff x = y  (identity of indiscernibles)           |
|  2. d(x,y) = d(y,x)        (symmetry)                            |
|  3. d(x,z) ≤ d(x,y)+d(y,z) (triangle inequality)                 |
|                                                                    |
|  Open ball: B(x,r) = {y ∈ X : d(x,y) < r}                       |
|  Defines topology: U open iff ∀x∈U ∃r>0: B(x,r) ⊆ U             |
|                                                                    |
|  CONVERGENCE: xₙ → x iff d(xₙ,x) → 0                             |
|  COMPLETENESS: every Cauchy sequence converges in X               |
|  COMPACTNESS: every sequence has a convergent subsequence          |
|                (for metric spaces = sequential compactness)        |
|                                                                    |
|  BAIRE CATEGORY THEOREM:                                          |
|  Complete metric space is NOT a countable union of nowhere-dense  |
|  closed sets. ← Fundamental to functional analysis                |
+====================================================================+
```

---

## Metric Axioms and Examples

```
STANDARD METRICS:
  Euclidean: d(x,y) = √(Σ(xᵢ-yᵢ)²) on Rⁿ.
  Manhattan (L¹): d(x,y) = Σ|xᵢ-yᵢ|.
  Chebyshev (L∞): d(x,y) = max|xᵢ-yᵢ|.
  Discrete: d(x,y) = 0 if x=y, else 1.
  p-adic: dₚ(m,n) = p^{-v_p(m-n)} where v_p = p-adic valuation.
  Hamming: d(x,y) = |{i : xᵢ ≠ yᵢ}| on strings of length n.
  Hausdorff: on compact subsets of a metric space.

ULTRAMETRIC SPACES:
  d(x,z) ≤ max(d(x,y), d(y,z))  (strong triangle inequality)
  p-adic metric dₚ is an ultrametric: every triangle is isosceles.
  Ultrametric spaces are always totally disconnected.
  Bridge to TDA: hierarchical clustering produces an ultrametric
    (distance between clusters = the scale at which they merge).
  The H₀ persistence diagram of a point cloud IS the ultrametric
    structure of single-linkage clustering.

GROMOV-HAUSDORFF DISTANCE:
  d_GH(X,Y) = inf{d_H^Z(f(X),g(Y))} over all metric spaces Z
    and isometric embeddings f: X→Z, g: Y→Z.
  This is a metric on the space of compact metric spaces (up to isometry).
  TDA stability theorem: if d_GH(X,Y) ≤ ε, then the persistence
    diagrams of X and Y differ by at most ε in bottleneck distance.
  This is why TDA is robust to noise: small perturbations of data
    (bounded in Hausdorff/GH distance) produce small changes in topology.

Lᵖ SPACES:
  Lᵖ([0,1]) = {measurable f : ∫|f|ᵖ < ∞}, d(f,g) = (∫|f-g|ᵖ)^{1/p}.
  L²: the Hilbert space of square-integrable functions. Inner product ⟨f,g⟩=∫f·ḡ.
  L∞: essentially bounded functions. d(f,g) = ess sup |f-g|.
  Lᵖ for 1≤p<∞: Banach spaces (complete normed spaces).

EQUIVALENT METRICS (give same open sets):
  Euclidean, L¹, L∞ on Rⁿ are all equivalent.
  (Equivalent: ∃c,C: c·d₁(x,y) ≤ d₂(x,y) ≤ C·d₁(x,y).)
  Equivalent metrics give the same topological space (same open sets).
  "Metric" structure (actual distances) differs; "topological" structure is the same.
```

---

## Open and Closed Sets

```
OPEN BALL: B(x,r) = {y : d(x,y) < r}.  (Open — strict inequality)
CLOSED BALL: B̄(x,r) = {y : d(x,y) ≤ r}.  (Closed — not always closed!)

Wait — closed ball IS closed in metric spaces:
  B̄(x,r) = {y : d(x,y) ≤ r} is closed because its complement {y : d(x,y)>r}
  is open: for any z with d(x,z) = s > r, B(z, s-r) ⊆ complement.

OPEN SET: U such that every point has an open ball inside U.
  ∀x ∈ U ∃ε > 0: B(x,ε) ⊆ U.

CLOSED SET: complement of an open set.
  Equivalently: contains all its limit points.

EXAMPLES:
  R: (a,b) open, [a,b] closed, [a,b) neither.
  R: {x} closed (single point), (R,discrete): every subset is open AND closed.
  R^n: same as R using Euclidean metric.
  Q ⊆ R: closed? No — {rationals} has limit points (irrationals) not in it.
         open? No — every open interval contains irrationals.
         Q is neither open nor closed in R.

INTERIOR int(S) = largest open set ⊆ S = {x : ∃ε>0, B(x,ε)⊆S}.
CLOSURE cl(S) = smallest closed set ⊇ S = S ∪ {limit points of S}.
BOUNDARY ∂S = cl(S) \ int(S).
```

---

## Convergence and Continuity

```
SEQUENCE CONVERGENCE: xₙ → x iff d(xₙ,x) → 0.
  ∀ε>0 ∃N: n>N → d(xₙ,x) < ε.

CAUCHY SEQUENCE: d(xₘ,xₙ) → 0 as m,n → ∞.
  ∀ε>0 ∃N: m,n>N → d(xₘ,xₙ) < ε.
  Every convergent sequence is Cauchy.
  Cauchy does NOT imply convergent in general:
    Q with Euclidean metric: xₙ = rational approximations to √2.
    xₙ is Cauchy but √2 ∉ Q → sequence doesn't converge in Q.

CONTINUITY at x: f is continuous at x iff
  ∀ε>0 ∃δ>0: d(x,y)<δ → d(f(x),f(y))<ε.
  Equivalently: f(xₙ) → f(x) whenever xₙ → x.

UNIFORM CONTINUITY: ∃δ works for ALL x simultaneously.
  f: [a,b] → R continuous on compact set → uniformly continuous.
  f(x) = 1/x on (0,1]: continuous but NOT uniformly continuous.

LIPSCHITZ: ∃K: d(f(x),f(y)) ≤ K·d(x,y).
  Lipschitz → uniformly continuous → continuous.
  Converse fails: |x|^{1/2} is uniformly continuous but not Lipschitz at 0.
```

---

## Completeness

```
COMPLETE METRIC SPACE: every Cauchy sequence converges.

EXAMPLES:
  Complete: R, Rⁿ, C, Lᵖ spaces, L²([0,1]), all Banach spaces.
  NOT complete: Q, (0,1), any open subset of R^n.
  C([0,1]) with sup metric: complete (uniform limit of continuous functions is continuous).
  C([0,1]) with L¹ metric: not complete (can Cauchy-converge to discontinuous function).

COMPLETION: Every metric space X has a unique (up to isometry) complete metric space
  X̄ (its completion) with X dense in X̄.
  Q completes to R.  Cauchy sequences over Q modulo eventual equality.

IMPORTANT COMPLETE METRIC SPACES:
  Hilbert spaces: L²(μ), ℓ², Sobolev spaces.
  Banach spaces: Lᵖ(μ) for p≥1, C(K) with sup norm, bounded operators.
  Polish spaces: separable complete metric spaces.
    Used in: descriptive set theory, probability (Borel σ-algebra on Polish = standard).
```

---

## Baire Category Theorem

```
BAIRE CATEGORY THEOREM:
  A complete metric space is NOT a countable union of nowhere-dense closed sets.

NOWHERE DENSE: E is nowhere dense if int(cl(E)) = ∅.
  ("E has no open part after closing.")
  Examples: Z in R (nowhere dense), Q in R (NOT nowhere dense: cl(Q) = R).

MEAGER (FIRST CATEGORY): countable union of nowhere-dense sets.
  Q has measure zero but is NOT meager (Q = ∪{q} where {q} is nowhere dense... wait:
  Q = ∪_{q ∈ Q} {q}: each {q} is nowhere dense. Q has cardinality ℵ₀.
  So Q IS meager in R! R = (R\Q) ∪ Q; R\Q is dense and co-meager.)

BAIRE: In a complete metric space X, if X = ∪Aₙ (countable union), then
  at least one Aₙ has nonempty interior.
  Equivalently: intersection of countably many dense open sets is dense.

TCS CONNECTION — DESCRIPTIVE SET THEORY:
  Baire category connects directly to the Borel hierarchy:
  Open sets = Σ₁⁰, closed = Π₁⁰, Fσ = Σ₂⁰, Gδ = Π₂⁰, ...
  In computability: decidable sets = clopen (Δ₁⁰),
    semidecidable = open (Σ₁⁰), co-semidecidable = closed (Π₁⁰).
  Baire category theorem → "generic" computations exist:
    the meager/comeager distinction parallels "measure zero" in
    algorithmic randomness. A comeager set of reals is "generic"
    (contains a dense Gδ), just as a measure-1 set is "random."
  Wadge hierarchy (refinement of Borel hierarchy) classifies
    sets in Polish spaces by continuous reducibility — directly
    analogous to many-one reducibility in computability theory.

APPLICATIONS:
  Open mapping theorem: Continuous surjective linear map between Banach spaces is open.
    (Proof uses Baire → one term of the preimage has nonempty interior → expand.)
  Closed graph theorem: Linear map T: X → Y (Banach) has closed graph → T is continuous.
  Uniform boundedness (Banach-Steinhaus): pointwise bounded family of operators is
    uniformly bounded.
    (If Tₙ is a sequence of bounded operators with sup_n |Tₙ(x)| < ∞ for each x,
     then sup_n ‖Tₙ‖ < ∞.)
  Principle of condensation of singularities.
  Non-constructive existence proofs: "the set of functions where something fails is meager."
```

---

## Completeness vs Compactness

```
COMPLETE: every Cauchy sequence converges. (Sequences "don't escape to infinity.")
COMPACT: every sequence has a convergent subsequence. (Space is "bounded and complete.")

In metric spaces:
  Compact ⟹ complete and totally bounded.
  Complete + totally bounded ⟹ compact.
  (Totally bounded = ∀ε>0, X covered by finitely many ε-balls.)

In Rⁿ:
  Compact ↔ closed and bounded  (Heine-Borel).

In infinite-dimensional spaces (Banach/Hilbert):
  Closed unit ball is complete but NOT compact!
  (The sequence e₁, e₂, e₃, ... (standard basis vectors) has d(eᵢ,eⱼ) = √2 → no convergent subseq.)
  Compact sets in Banach spaces must be "tight": no escaping to infinity in any direction.
```

---

## Contraction Mapping (Banach Fixed Point Theorem)

```
CONTRACTION: f: X → X with d(f(x),f(y)) ≤ c·d(x,y) for some c < 1.

BANACH FIXED POINT THEOREM:
  If (X,d) is a complete metric space and f is a contraction, then:
  1. f has a unique fixed point x* (f(x*) = x*).
  2. For any starting x₀, the iteration xₙ₊₁ = f(xₙ) converges to x*.
  3. Rate: d(xₙ, x*) ≤ cⁿ/(1-c) · d(x₁, x₀).

APPLICATIONS:
  Existence of ODEs (Picard-Lindelöf): f(t,x) Lipschitz → unique solution.
  Newton's method: near a simple root, the iteration is a contraction → quadratic convergence.
  Iterated function systems: fractals as fixed points of contractions on compact subsets.
  Implicit function theorem: local inversion via contraction.
  Hash tables: consistent hashing (not quite BCT but similar flavour).
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Define continuity precisely | ε-δ definition using metric |
| Show sequence converges | Show d(xₙ,x) → 0 |
| Show space is incomplete | Find non-convergent Cauchy sequence |
| Show space is complete | Complete the Cauchy completeness proof |
| Apply BCT consequences | Need complete metric space (e.g., Banach space) |
| Show function has fixed point | Find contraction on complete metric space |
| Show two metrics are equivalent | Find c,C: c·d₁ ≤ d₂ ≤ C·d₁ |
| Understand compactness in Rⁿ | Heine-Borel: closed + bounded |
| Understand compactness in ∞-dim | Sequential: compact = complete + totally bounded |

---

## Common Confusion Points

**"Closed and bounded implies compact."**
Only in Rⁿ (Heine-Borel theorem). In infinite-dimensional Banach spaces, the closed
unit ball is closed and bounded but NOT compact. Compactness requires total boundedness
(can be covered by finitely many ε-balls for every ε > 0).

**"Q is dense in R, so Q can't be meager."**
Wrong. Dense ≠ non-meager. Q = ∪_{q∈Q} {q} is a countable union of nowhere-dense sets
(each singleton {q} in R has empty interior). By definition, Q is meager.
But R\Q (irrationals) is dense AND co-meager. Measure and category are different:
Q has measure zero; irrationals have full measure.

**"Complete = no 'holes' like R."**
Informal intuition is correct for metric spaces: complete means limits of Cauchy sequences
exist. But this is not the same as "connected" or "no gaps." The Cantor set is complete
(it's closed in R) but highly disconnected. A single point {p} is trivially complete.

**"Uniform continuity and continuity are the same on compact sets."**
Correct! A continuous function on a compact metric space is automatically uniformly
continuous. This is a key theorem with many applications (integration, approximation).
On non-compact sets: 1/x is continuous but not uniformly continuous on (0,1].
