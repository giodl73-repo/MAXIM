# Compactness

## The Big Picture

```
+====================================================================+
|             COMPACTNESS — THE FINITE-COVER CONDITION              |
+====================================================================+
|                                                                    |
|  COMPACT: Every open cover has a finite subcover.                 |
|                                                                    |
|  ∀{Uα} open with X = ∪Uα,  ∃ finite {Uα₁,...,Uαₙ}: X=∪Uαᵢ.    |
|                                                                    |
|  INTUITION: Compact = "behaves like a finite set" even if infinite.|
|  The finite-cover condition forces all "infinity" to be controlled.|
|                                                                    |
|  KEY THEOREMS:                                                     |
|  Heine-Borel: [a,b] ⊆ R is compact (closed + bounded in Rⁿ).     |
|  Continuous image: f(X) compact if X compact, f continuous.       |
|  Extreme value: f: compact X → R attains max and min.             |
|  Tychonoff: ∏{compact spaces} is compact (needs Axiom of Choice). |
|                                                                    |
|  IN METRIC SPACES:                                                |
|  Compact ↔ sequentially compact ↔ complete + totally bounded.     |
+====================================================================+
```

Compactness is the most important single concept in point-set topology.
It turns infinite arguments into finite ones. It's why continuous functions
on closed bounded intervals achieve their maximum — a fact that requires proof.

<!-- @editor[bridge/P2]: No bridge from topological compactness to the compactness theorem in logic (which is mentioned later, but the connection to TCS should come here). The learner's MIT TCS background means: first-order logic compactness ↔ Tychonoff for {0,1}^A is a landmark insight. Also missing: the algorithmic/complexity connection — compact = "finite in disguise," which is why compactness arguments in complexity theory (e.g., finite model theory, compactness of propositional proof systems) work. -->

---

## Definitions and Equivalences

```
OPEN COVER DEFINITION:
  An open cover of X is a collection {Uα} of open sets with X = ∪Uα.
  X is compact if every open cover has a finite subcover.

SEQUENTIAL COMPACTNESS (for metric spaces):
  Every sequence in X has a convergent subsequence (converging to a point in X).

TOTALLY BOUNDED:
  For every ε>0, X can be covered by finitely many ε-balls.

THEOREM (for metric spaces):
  Compact ↔ Sequentially compact ↔ Complete + Totally bounded.

In GENERAL topological spaces:
  Compact ≠ Sequentially compact in general.
  Sequential compactness → countably compact → compact (with mild extra conditions).
```

---

## Heine-Borel Theorem

```
THEOREM: A subset of Rⁿ is compact iff it is closed and bounded.

PROOF (for [a,b] ⊆ R):
  Closed + bounded → compact:
  Let {Uα} be an open cover of [a,b].
  Let A = {x ∈ [a,b] : [a,x] has a finite subcover}.
  A ≠ ∅ (a ∈ A) and A is bounded above (by b).
  Let c = sup A.
  Some Uα contains c: Uα ⊇ (c-δ, c+δ). [a,c-δ/2] has a finite subcover.
  Adding Uα gives a finite subcover of [a,c+δ/2].
  So c+δ/2 ∈ A (if c < b) → contradiction with c = sup A.
  Therefore c = b and [a,b] is compact. □

Compact → closed: if p is a limit point of X not in X, construct an open cover with no finite subcover.
Compact → bounded: open cover {B(0,n)} has finite subcover → X ⊆ B(0,N) for some N.

FAILURE IN INFINITE DIMENSIONS:
  In L²: the closed unit ball {f : ‖f‖ ≤ 1} is closed and bounded but NOT compact.
  Sequence eₙ (standard basis): ‖eₙ - eₘ‖ = √2 for n≠m → no convergent subsequence.
  The Arzelà-Ascoli theorem gives compactness in C([0,1]): need equicontinuity too.
```

---

## Properties of Compact Spaces

### Continuous Images

```
THEOREM: If f: X → Y is continuous and X is compact, then f(X) is compact.
  Proof: Let {Vα} cover f(X). Then {f^{-1}(Vα)} covers X.
  Finite subcover: f^{-1}(Vα₁),...,f^{-1}(Vαₙ). → Vα₁,...,Vαₙ cover f(X). □

COROLLARIES:
  Extreme Value Theorem: If f: X → R is continuous and X is compact,
    then f attains its maximum and minimum.
    (f(X) is compact → closed + bounded → has sup and inf, attained.)

  Uniform Continuity: If f: X → Y with X compact metric, then f is uniformly continuous.
    (Key in Riemann integration: any continuous function on [a,b] is integrable.)
```

### Compact + Hausdorff = Very Nice

```
In a compact Hausdorff space:
  Every closed subset is compact.
  Every compact subset is closed.
  Normal: disjoint closed sets have disjoint open neighborhoods. (T₄)
  Continuous bijection → homeomorphism.
    (Proof: closed → compact → image closed → f^{-1} continuous.)

  The category of compact Hausdorff spaces is particularly well-behaved:
  Stone-Čech compactification: every Tychonoff (T₃.₅) space X embeds in
    a compact Hausdorff space βX, the Stone-Čech compactification.
    βX is characterized by: every bounded continuous f: X→R extends to βX.
```

---

## Tychonoff's Theorem

```
TYCHONOFF'S THEOREM: The product ∏_{α∈A} Xα of compact spaces is compact
  (in the product topology), for ANY index set A.

PROOF (requires Axiom of Choice via Zorn's Lemma or ultrafilters):
  Ultrafilter proof: An ultrafilter U on ∏Xα determines a point x with xα = lim_U π_α.
  (Because Xα compact: every ultrafilter on Xα converges to some point in Xα.)
  Every open cover has a finite subcover → refine to a sub-base cover first (Alexander).

IMPORTANCE:
  The theorem holds for uncountable products. Critical for:
  Proofs in functional analysis (compactness in weak topologies).
  Stone-Čech compactification constructions.
  Model theory: compactness theorem for first-order logic is essentially Tychonoff.

  Tychonoff ↔ Axiom of Choice (Kelley, 1950): the theorem is actually equivalent
  to AC over ZF. This is why the proof is non-constructive.

PRODUCT OF COMPACT HAUSDORFF:
  ∏_{α} Xα (with each Xα compact Hausdorff) is compact Hausdorff.
  This gives the Stone-Čech compactification and profinite groups.

PROFINITE GROUPS (number theory connection):
  Gal(Q̄/Q) = profinite group = inverse limit of Gal(Kᵢ/Q) (finite Galois groups).
  As a topological group: compact Hausdorff + totally disconnected.
  The open normal subgroups correspond to finite Galois extensions.
```

---

## Compactness in Function Spaces

### Arzelà-Ascoli Theorem

```
THEOREM: A subset F ⊆ C([a,b]) is compact (in the sup metric) iff:
  (1) F is uniformly bounded: ∃M: |f(x)| ≤ M for all f ∈ F, x ∈ [a,b].
  (2) F is equicontinuous: ∀ε>0 ∃δ>0: |x-y|<δ → |f(x)-f(y)|<ε for all f ∈ F.

WHY EQUICONTINUITY?
  In infinite dimensions, closed + bounded ≠ compact.
  Equicontinuity replaces "bounded" as the key extra condition.
  Uniform bound gives pointwise compactness; equicontinuity gives no "wild oscillations."

APPLICATIONS:
  Existence proofs in ODEs and PDEs.
  Schauder fixed-point theorem (compact convex operator has fixed point).
  Compactness of solution sets.

DIAGONALIZATION ARGUMENT:
  Proof: Take a sequence (fₙ) in F. Choose a dense subset {rₖ} ⊆ [a,b].
  Since (fₙ(r₁)) is bounded: has convergent subsequence fₙ₁.
  From (fₙ₁(r₂)) bounded: extract fₙ₂.
  Diagonal: fₙₙ converges at every rₖ.
  Equicontinuity → uniformly Cauchy everywhere → uniform limit exists. □
```

### Compact Operators

```
COMPACT OPERATOR T: B(X, Y) (between Banach spaces):
  T is compact if T maps bounded sets to precompact sets.
  Equivalently: every bounded sequence (xₙ) has a subsequence with (Txₙ) convergent.

FINITE-RANK OPERATORS are compact.
LIMIT OF COMPACT OPERATORS is compact.

SPECTRAL THEORY:
  If T: H → H is a compact self-adjoint operator on Hilbert space:
  H has an orthonormal basis of eigenvectors.
  Eigenvalues accumulate only at 0.
  This is the Hilbert-Schmidt theorem — infinite-dimensional analogue of diagonalization.

FREDHOLM THEORY:
  If K is compact: I-K has finite-dimensional kernel and cokernel.
  "Fredholm alternative": either Kx = y has a unique solution, or Kx = 0 has nonzero solutions.
  Used in: integral equations, elliptic PDEs.
```

---

## Compactness and Logic

```
COMPACTNESS THEOREM OF LOGIC:
  A set of first-order sentences Γ has a model iff every finite subset has a model.
  ("If you can't detect an inconsistency with finitely many axioms: there's a model.")

CONNECTION TO TYCHONOFF:
  Stone space of a Boolean algebra is compact.
  The compactness theorem = Tychonoff for {0,1}^A (product of finite spaces).

STONE-ČECH COMPACTIFICATION βN:
  The "free compact Hausdorff space" on the natural numbers.
  βN contains N as a dense subspace.
  Points of βN\N = "ultrafilters on N" = "ideal points at infinity."
  Any function f: N → [0,1] extends to f̄: βN → [0,1].

ULTRAFILTERS AND NONSTANDARD ANALYSIS:
  Choose an ultrafilter U on N.
  *R = R^N/U (equivalence classes of sequences of reals modulo U).
  *R is a "nonstandard extension" of R with infinitesimals and infinities.
  ε-δ proofs can often be replaced by nonstandard proofs (compactness is built in).
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Show X compact (abstract) | Find finite subcover for every open cover |
| Show subset of Rⁿ compact | Check closed + bounded (Heine-Borel) |
| Show f attains max/min | X compact + f continuous → use extreme value theorem |
| Show f uniformly continuous | X compact metric + f continuous → uniform continuity |
| Show F ⊆ C([a,b]) compact | Arzelà-Ascoli: uniformly bounded + equicontinuous |
| Show operator compact | Bounded sequences → precompact images |
| Product of compacts | Tychonoff (requires AC for infinite products) |
| Compactness in ∞-dim Banach | Need equicontinuity or more (closed ball not compact) |

---

## Common Confusion Points

**"Compact = closed and bounded."**
Only in Rⁿ (Heine-Borel). In infinite-dimensional spaces: fails completely.
In abstract spaces: closed and bounded is not even well-defined (no notion of "bounded"
without extra structure). The correct definition is always: every open cover has a
finite subcover.

**"Sequential compactness = compactness."**
In metric spaces: yes, they're equivalent. In general topological spaces: no.
Sequential compactness → countably compact → compact with additional axioms.
Example of compact but not sequentially compact: {0,1}^{[0,1]} (uncountable product of
two-point spaces) is compact (Tychonoff) but not sequentially compact.

**"Compactness is closed under unions."**
Finite unions of compact sets: compact. Infinite unions: no.
Each [n, n+1] is compact; ∪_{n∈Z} [n,n+1] = R, which is not compact.

**"Tychonoff's theorem is trivial for finite products."**
For finite products: yes, the proof is easy (product of finitely many compact spaces
is compact). For infinite products: the proof requires the Axiom of Choice. The theorem
is equivalent to AC over ZF.
