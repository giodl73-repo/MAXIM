# Functional Analysis — Complete Reference

## The Big Picture

Functional analysis is linear algebra in infinite dimensions. The jump from ℝⁿ to infinite-dimensional spaces introduces genuinely new phenomena: non-equivalent norms, unbounded operators, non-closed subspaces, the distinction between strong and weak convergence. This guide covers Banach and Hilbert spaces, the bounded operator theory, spectral theory in infinite dimensions, and the connections to PDEs, quantum mechanics, and machine learning.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  FUNCTIONAL ANALYSIS LANDSCAPE                                              │
│                                                                             │
│  Normed Spaces                        Dual Spaces & Weak Topology           │
│  ──────────────────────────────        ──────────────────────────────────   │
│  Normed, Banach, Hilbert spaces       Dual space X* = B(X, 𝕂)               │
│  Completeness, Schauder bases         Hahn-Banach theorem                   │
│  Examples: Lᵖ, C[a,b], ℓᵖ, H^k      Weak topology σ(X, X*)                  │
│                                        Weak* topology σ(X*, X)              │
│                                        Reflexive spaces                     │
│                                                                             │
│  Bounded Operators                    Spectral Theory                       │
│  ──────────────────────────────        ──────────────────────────────────   │
│  B(X,Y): bounded linear maps          Eigenvalues vs spectrum               │
│  Operator norm, compactness           Compact operators                     │
│  Open mapping, closed graph theorem   Spectral theorem (compact, SA)        │
│  Adjoints (Banach/Hilbert)            Functional calculus                   │
│                                                                             │
│  Applications                                                               │
│  ────────────────────────────────────────────────────────────────────────── │
│  PDEs (Sobolev spaces, weak solutions)   QM (observables, C*-algebras)      │
│  ML (RKHS, kernel methods, SVMs)         Signal processing (Fourier in L²)  │
│  Numerical methods (Krylov, FEM)         Neural operators (attention as op) │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Normed Spaces and Banach Spaces

### Normed Space

A **normed space** is a vector space X over 𝕂 (ℝ or ℂ) with a norm ||·||: X → ℝ≥0:
```
(N1) ||x|| = 0 iff x = 0                    [non-degeneracy]
(N2) ||αx|| = |α| ||x||  for α ∈ 𝕂         [homogeneity]
(N3) ||x+y|| ≤ ||x|| + ||y||               [triangle inequality]
```

A norm induces a metric: d(x,y) = ||x-y||.

**Banach space**: A normed space that is complete (every Cauchy sequence converges).

### Key Examples

```
ℓᵖ (p ∈ [1,∞]): sequences x = (x₁, x₂, ...) with
  ||x||_p = (Σ|xₙ|ᵖ)^{1/p}  for p < ∞
  ||x||_∞ = sup|xₙ|          for p = ∞

  All Banach. ℓ² is Hilbert.
  ℓ¹ ⊂ ℓ² ⊂ ... ⊂ ℓ∞  (as sets, for p < q: ℓᵖ ⊂ ℓᵍ)

Lᵖ(μ): measurable functions on (Ω,ℱ,μ) with finite p-norm.
  Banach by Riesz-Fischer. L² is Hilbert.

C[a,b]: continuous functions on [a,b] with sup norm ||f||_∞ = max|f(x)|.
  Banach. Not reflexive. Not separable with ℓ¹ norm.

C^k[a,b]: k-times continuously differentiable functions.
  ||f||_{C^k} = Σ_{j=0}^k ||f^(j)||_∞.  Banach.

H^k(Ω) (Sobolev spaces): L² functions with weak derivatives up to order k in L².
  ||f||_{H^k}² = Σ_{|α|≤k} ||D^α f||_{L²}².
  Hilbert. Critical for PDE theory.
```

### Equivalent Norms

```
Two norms ||·||₁, ||·||₂ on X are equivalent if:
  c||x||₁ ≤ ||x||₂ ≤ C||x||₁  for some 0 < c ≤ C < ∞.

Key theorem: On a finite-dimensional space, ALL norms are equivalent.
  Proof: The unit ball is compact in finite dimensions; continuous functions
  on compact sets achieve their extrema.

In infinite dimensions: norms can be inequivalent.
  Example: C[0,1] with ||·||_∞ vs ||·||_2.
  ||f||_2 ≤ ||f||_∞ but no C with ||f||_∞ ≤ C||f||_2 for all f.
  They generate different topologies, different notions of convergence.
```

### Separability

X is **separable** if it has a countable dense subset.

```
Separable: ℓᵖ (p < ∞), Lᵖ(ℝ) (p < ∞), L²(ℝ), C[a,b].
Not separable: ℓ∞, L∞(ℝ).

Separability important for: Schauder bases (countable basis), second-countability,
  compactness arguments (sequential compactness in reflexive spaces).
```

---

## 2. Hilbert Spaces

### Inner Product Spaces

A **Hilbert space** H is a complete inner product space. Inner product ⟨·,·⟩: H×H → 𝕂:
```
(I1) ⟨x,x⟩ ≥ 0; ⟨x,x⟩ = 0 iff x = 0
(I2) ⟨x,y⟩ = ⟨y,x⟩̄  (conjugate symmetric; symmetric over ℝ)
(I3) ⟨αx+βy, z⟩ = α⟨x,z⟩ + β⟨y,z⟩  (linear in first argument)

Induced norm: ||x|| = √⟨x,x⟩

Cauchy-Schwarz: |⟨x,y⟩| ≤ ||x|| ||y||
  Equality iff x and y are linearly dependent.

Parallelogram law: ||x+y||² + ||x-y||² = 2||x||² + 2||y||²
  A normed space is Hilbert iff the parallelogram law holds.
```

### Orthogonality and Projections

```
x ⊥ y: ⟨x,y⟩ = 0.
M⊥ = {x ∈ H : ⟨x,m⟩=0 for all m ∈ M} (orthogonal complement).

Projection theorem: If M ⊆ H is a closed subspace, then:
  H = M ⊕ M⊥   (every x = m + m⊥ uniquely, m ∈ M, m⊥ ∈ M⊥)

Orthogonal projection P_M: H → M:
  P_M(x) = argmin_{m∈M} ||x-m||  (nearest point in M)
  P_M is linear, idempotent (P²=P), self-adjoint (⟨Px,y⟩=⟨x,Py⟩), ||P||=1.
  Bessel's inequality: ||P_M x||² ≤ ||x||²
```

**Riesz representation theorem** (Hilbert case):
```
For any bounded linear functional f: H → 𝕂, ∃! y ∈ H:
  f(x) = ⟨x,y⟩ for all x ∈ H, and ||f|| = ||y||.

H ≅ H* (dual space isomorphism, conjugate-linear in complex case).
```

### Orthonormal Bases

A sequence {eₙ} is **orthonormal** if ⟨eₘ,eₙ⟩ = δₘₙ. It's an **orthonormal basis** (ONB) if span is dense.

```
For x ∈ H with ONB {eₙ}:
  x = Σₙ ⟨x,eₙ⟩ eₙ  (Fourier series in H)
  ||x||² = Σₙ |⟨x,eₙ⟩|²  (Parseval's identity)
  Bessel's inequality: Σ_{n≤N} |⟨x,eₙ⟩|² ≤ ||x||²  (partial sums bounded)
```

**Gram-Schmidt**: Given linearly independent {vₙ}, produce ONB by subtracting projections onto previous basis vectors. Generalizes finite-dimensional version to countably many vectors.

**Separable Hilbert spaces**: All infinite-dimensional separable Hilbert spaces are isometrically isomorphic to ℓ². This is why L²[0,1] ≅ ℓ² — they're "the same" Hilbert space.

---

## 3. Bounded Linear Operators

### Bounded Operators

A linear map T: X → Y between normed spaces is **bounded** if:
```
||T|| := sup_{x≠0} ||Tx||/||x|| = sup_{||x||=1} ||Tx|| < ∞

Equivalently: T is continuous (linear + continuous = linear + bounded).
Proof: ||Tx - Ty|| = ||T(x-y)|| ≤ ||T|| ||x-y|| → continuity.
       If continuous at 0: ||Tx|| = ||T(x-0)|| → 0 as x→0 → bounded.
```

Bounded linear operators X → Y form a Banach space B(X,Y) with operator norm.

**B(X) = B(X,X)**: bounded operators from X to itself, forming a Banach algebra.

### The Four Fundamental Theorems

**Hahn-Banach** (extension theorem):
```
Let M ⊆ X subspace, f: M → 𝕂 linear with |f(x)| ≤ p(x) (p sublinear).
Then ∃ F: X → 𝕂 linear with F|_M = f and |F(x)| ≤ p(x) on all of X.

For normed spaces: Every bounded functional on a subspace extends to all of X
with the same norm.

Corollaries:
  For x≠0, ∃ F ∈ X* with F(x)=||x|| and ||F||=1.
  X* separates points: F(x)=F(y) ∀F ∈ X* → x=y.
  For closed subspace M ≄ X, ∃ F ∈ X* with F|_M = 0, F(x)≠0 for x∉M.
```

**Baire Category Theorem**: A complete metric space (Banach space) is not a countable union of nowhere dense sets. The Baire category theorem is the key input for the next three results.

**Uniform Boundedness Principle** (Banach-Steinhaus):
```
Let X be Banach, Y normed, {T_α} ⊆ B(X,Y).
If sup_α ||T_α x|| < ∞ for each x ∈ X (pointwise bounded),
then sup_α ||T_α|| < ∞ (uniformly bounded).

Proof: Baire category → ∃ ball on which all T_α uniformly bounded → bounded everywhere.

Corollary: If T_n → T weakly (T_n x → Tx for all x), then sup||T_n|| < ∞ and ||T|| ≤ liminf ||T_n||.
```

**Open Mapping Theorem**:
```
If T ∈ B(X,Y) is surjective (X,Y Banach), then T is an open map:
  T maps open sets to open sets.

Equivalently: ∃δ>0 such that T(B_X(0,1)) ⊇ B_Y(0,δ).

Corollary (Bounded Inverse Theorem / Banach isomorphism theorem):
  If T is bijective, then T⁻¹ is also bounded.
  A bijective bounded operator between Banach spaces is an isomorphism.
```

**Closed Graph Theorem**:
```
Graph of T: Γ(T) = {(x,Tx) : x ∈ X} ⊆ X×Y.
If X,Y Banach and T is linear, then:
  T is bounded iff Γ(T) is closed in X×Y.

Why useful: Often easier to show closedness than direct boundedness.
  Closed graph: xₙ→x and Txₙ→y imply Tx=y.
```

---

## 4. Dual Spaces and Weak Topologies

### Dual Space

The **dual** of a normed space X is X* = B(X, 𝕂) (bounded linear functionals).

```
Important dual pairs:
  (Lᵖ)* ≅ Lᵍ for 1 < p < ∞, 1/p+1/q=1.  [Riesz representation]
  (L¹)* ≅ L∞.
  (L∞)* ⊃ L¹ (strictly; includes finitely additive measures).
  (ℓᵖ)* ≅ ℓᵍ for 1≤p<∞.
  (C[a,b])* ≅ M[a,b] (Borel measures; Riesz-Markov-Kakutani).
  (ℓ¹)* ≅ ℓ∞.
  (H)* ≅ H for Hilbert H (Riesz representation).
```

### Reflexive Spaces

```
Second dual X** = (X*)*.
Canonical embedding J: X → X** by J(x)(f) = f(x).
J is always isometric (||J(x)|| = ||x||).

X is reflexive if J is surjective (X ≅ X**).

Reflexive: ℓᵖ (1<p<∞), Lᵖ(μ) (1<p<∞), all Hilbert spaces, finite-dimensional spaces.
Not reflexive: ℓ¹, ℓ∞, L¹, L∞, C[a,b].

Reflexivity matters because: bounded sequences in reflexive Banach spaces have
  weakly convergent subsequences (Banach-Alaoglu + reflexive).
  → PDE: minimize energy over weakly compact set → extract weakly convergent subsequence.
```

### Weak Topologies

**Weak topology** σ(X, X*): coarsest topology making all f ∈ X* continuous.
```
xₙ → x weakly: f(xₙ) → f(x) for all f ∈ X*.
Notation: xₙ ⇀ x.

In infinite dimensions: weak convergence ≠ norm convergence.
  Example: eₙ ⇀ 0 in L² (sin(nπx) → 0 weakly by Riemann-Lebesgue).
  But ||eₙ||_2 = 1 ≠ 0.
  (eₙ is ONB; weak convergence = Fourier coefficients → 0.)
```

**Weak* topology** σ(X*, X): coarsest topology making evaluation at x continuous.
```
f_n →^{w*} f: f_n(x) → f(x) for all x ∈ X.
```

**Banach-Alaoglu theorem**: The unit ball in X* is compact in the weak* topology.
```
{f ∈ X* : ||f|| ≤ 1} is weak*-compact.

In reflexive spaces (X = X**): unit ball in X is weakly compact.
  Key for: variational problems in PDEs, convex optimization.
```

---

## 5. Compact Operators

### Definition

T: X → Y is **compact** if T maps bounded sets to relatively compact sets (sets with compact closure). Equivalently: every bounded sequence {xₙ} has a subsequence {xₙₖ} with {Txₙₖ} convergent.

```
Compact operators form a closed two-sided ideal in B(X) (when X = Y).
  T compact, S bounded → TS and ST compact.

Finite-rank operators (range is finite-dimensional) are compact.
Compact operators are limits of finite-rank operators (in separable Hilbert space).
```

### Spectral Theory for Compact Operators

**Spectrum** of T ∈ B(X):
```
σ(T) = {λ ∈ ℂ : T - λI is not invertible}
  = eigenvalues ∪ "rest of spectrum"

For T ∈ B(X) (general): σ(T) ⊆ {|λ| ≤ ||T||}. Compact set.
Spectral radius: r(T) = sup{|λ| : λ ∈ σ(T)} = lim ||Tⁿ||^{1/n}.
```

**Fredholm alternative**: For compact T ∈ B(X):
```
Either:
  (a) (T - λI) is bijective (invertible), OR
  (b) ker(T - λI) is finite-dimensional and non-trivial (λ is an eigenvalue).

The equation (T - λI)x = y has a solution iff y ⊥ ker(T* - λ̄I).
```

**Spectral theorem for compact self-adjoint operators** (Hilbert space):
```
Let T: H → H be compact and self-adjoint (T = T*).

Then:
  1. All eigenvalues λₙ are real.
  2. Eigenvalues accumulate only at 0 (only finitely many with |λ| ≥ ε).
  3. Eigenvectors for distinct eigenvalues are orthogonal.
  4. Eigenspaces are finite-dimensional (except possibly for λ=0).
  5. H has an ONB of eigenvectors {eₙ}:
       Tx = Σₙ λₙ ⟨x, eₙ⟩ eₙ

This is the infinite-dimensional analogue of diagonalization.
Applications: PCA (covariance operators), kernel methods, Sturm-Liouville problems.
```

---

## 6. Spectral Theory — Bounded Self-Adjoint Operators

### Adjoint Operators

For T ∈ B(H), the **adjoint** T* ∈ B(H) satisfies:
```
⟨Tx, y⟩ = ⟨x, T*y⟩  for all x, y ∈ H.

Exists uniquely by Riesz representation.
||T*|| = ||T||, ||T*T|| = ||T||².

T is self-adjoint if T* = T.
T is normal if T*T = TT*.
T is unitary if T*T = TT* = I.
T is positive if ⟨Tx,x⟩ ≥ 0 for all x.
```

### Spectral Theorem for Bounded Self-Adjoint Operators

For bounded self-adjoint T ∈ B(H) (H separable):
```
Spectral theorem: ∃ projection-valued measure E on (ℝ, Borel):
  T = ∫ λ dE(λ)

E(B) = orthogonal projection onto "part of H corresponding to spectrum in B."
Supported on σ(T) ⊆ [m, M] where m = inf⟨Tx,x⟩/||x||², M = sup.

Functional calculus: for any bounded Borel f: ℝ→ℂ:
  f(T) = ∫ f(λ) dE(λ)   (well-defined bounded operator)

Special cases:
  T = ∫ λ dE(λ)        [definition]
  T² = ∫ λ² dE(λ)
  e^{iT} = ∫ e^{iλ} dE(λ)  [unitary operator, Stone's theorem]
  (T - λI)⁻¹ = ∫ 1/(μ-λ) dE(μ) for λ ∉ σ(T)
```

**For compact self-adjoint T**: E is discrete (concentrated on eigenvalues). The spectral theorem reduces to the diagonalization in the previous section.

**Continuous spectrum**: For non-compact self-adjoint operators, the spectrum may have a continuous part (no eigenvectors, but "approximate eigenvectors" xₙ with ||xₙ||=1 and ||(T-λI)xₙ||→0).

Example: Multiplication operator (Mf)(x) = x·f(x) on L²[0,1]. σ(M) = [0,1]. No eigenvalues. Every λ ∈ [0,1] is in continuous spectrum.

---

## 7. Quantum Mechanics Dictionary

Functional analysis is the mathematical foundation of quantum mechanics. The connection is exact, not metaphorical.

### The QM–Functional Analysis Dictionary

```
QM concept                      Functional analysis object
────────────────────────────    ──────────────────────────────────────────────
Pure quantum state |ψ⟩         Unit vector ψ ∈ L²(ℝ³) (or H, any Hilbert space)
Observable A (e.g., energy)    Self-adjoint operator A on H
Expectation value ⟨A⟩_ψ       ⟨ψ, Aψ⟩ = ∫ ψ̄(x) (Aψ)(x) dx
Eigenvalue equation Aψ = λψ    Spectral eigenvalue; λ is a possible measurement outcome
Spectral theorem for A          Decomposes H into eigenspaces (discrete) + continuous spectrum
Measurement outcome             λ ∈ σ(A) with probability ||E_A({λ})ψ||²
Time evolution |ψ(t)⟩           U(t)|ψ(0)⟩ where U(t) = e^{-iHt/ℏ} is unitary
Schrödinger equation            iℏ d/dt ψ = Hψ  [H = Hamiltonian operator]
Commutator [A,B]                AB - BA on H; zero iff A, B simultaneously measurable
Uncertainty principle           σ_A · σ_B ≥ ½|⟨[A,B]⟩|  [Robertson inequality]
Position operator Q             (Qψ)(x) = xψ(x) [multiplication operator]
Momentum operator P             (Pψ)(x) = -iℏ ∂ψ/∂x [differentiation operator]
[Q, P] = iℏI                   Heisenberg canonical commutation relation
```

**Why self-adjoint, not just symmetric**: The spectral theorem requires genuine self-adjointness (Dom(A) = Dom(A*)), not just symmetry. Self-adjoint operators generate one-parameter unitary groups (Stone's theorem below). Only self-adjoint observables have real spectra and complete sets of "eigenstates" (via the PVM). A symmetric operator that fails to be self-adjoint does not have a spectral theorem and cannot correspond to a physical observable.

### Stone's Theorem

**Stone's theorem** is the mathematical engine connecting self-adjoint operators to unitary time evolution:

```
Stone's Theorem:
  Let A be self-adjoint (possibly unbounded) on H.
  Then U(t) = e^{itA} defines a strongly continuous one-parameter unitary group:
    U(t): H → H is unitary for each t ∈ ℝ
    U(0) = I
    U(s+t) = U(s)U(t)  [group property]
    U(t)ψ → ψ in H as t → 0  [strong continuity]
    d/dt U(t)ψ|_{t=0} = iAψ  for ψ ∈ Dom(A)

  Converse: Every strongly continuous one-parameter unitary group U(t) arises
  this way from a unique self-adjoint generator A = (1/i) d/dt U(t)|_{t=0}.
```

**QM application**: The Schrödinger equation iℏ ∂_t ψ = Hψ has solution ψ(t) = e^{-iHt/ℏ}ψ(0). Stone's theorem guarantees this U(t) = e^{-iHt/ℏ} is unitary (norm-preserving = probability-preserving) if and only if H is self-adjoint. Self-adjointness of the Hamiltonian is not a physics assumption — it is a mathematical condition equivalent to having well-defined unitary time evolution.

**Functional calculus connection**: The spectral theorem for A gives
```
U(t) = e^{itA} = ∫_ℝ e^{itλ} dE(λ)

where E is the projection-valued measure of A. The integral over the spectrum
replaces the matrix exponential of the finite-dimensional case. For the free
particle (H = -ℏ²/(2m) Δ), σ(H) = [0,∞), and e^{-iHt/ℏ} acts as a Fourier
multiplier: multiplication by e^{-iℏk²t/(2m)} in momentum space.
```

### C*-Algebras (Algebraic Abstraction of QM)

The **C*-algebra** framework abstracts QM observables away from any particular Hilbert space representation:

```
C*-algebra: a Banach algebra A over ℂ with an involution * satisfying:
  ||a*a|| = ||a||²   [C*-identity — the key axiom]

Examples:
  B(H): bounded operators on H. The paradigm C*-algebra.
  C(X): continuous functions on compact X, with * = complex conjugate.
    This is commutative. Every commutative C*-algebra ≅ C(X) for some compact X
    (Gelfand representation theorem).
  Calkin algebra B(H)/K(H): quotient of bounded by compact operators.
    Relevant for Fredholm theory and index theory.

States and observables in the algebraic framework:
  Observable: self-adjoint element a = a* ∈ A.
  State:       positive linear functional ω: A → ℂ with ω(1) = 1.
  Expectation: ω(a) = expected value of observable a in state ω.

GNS construction (Gelfand-Naimark-Segal):
  Every state ω on a C*-algebra A gives a Hilbert space H_ω and representation
  π_ω: A → B(H_ω) with a cyclic vector Ω ∈ H_ω:
    ω(a) = ⟨Ω, π_ω(a) Ω⟩.
  This reconstructs the Hilbert space from the algebra and the state.
  Different states give inequivalent representations — relevant for QFT
  (vacuum state vs. thermal state give unitarily inequivalent Hilbert spaces).
```

**Why C*-algebras matter for QM**: Classical observables form a commutative algebra (C(X)). Quantum observables form a non-commutative C*-algebra. The non-commutativity of [Q,P] = iℏI is exactly the content of Heisenberg's uncertainty principle — Q and P are non-commuting elements of the Weyl algebra (a specific C*-algebra).

---

## 8. Unbounded Operators

### Why Unbounded Operators Matter

In quantum mechanics, observables (position, momentum, Hamiltonian) are unbounded self-adjoint operators on L².

```
Differentiation operator D = d/dx: L²(ℝ) → L²(ℝ).
  D is NOT bounded: ||Df||/||f|| is unbounded (sin(nx) has ||·||=1, D gives n·cos(nx)).

  Need: domain Dom(D) = {f ∈ L² : f absolutely continuous, f' ∈ L²}
        (not all of L²).
```

### Closed and Self-Adjoint Unbounded Operators

```
Densely defined operator T: Dom(T) ⊆ H → H (Dom(T) dense in H).

Adjoint T*: f ∈ Dom(T*) iff ⟨Tx,y⟩ = ⟨x,z⟩ for all x ∈ Dom(T).
  Then T*y = z.  Dom(T*) = {y : x ↦ ⟨Tx,y⟩ is bounded}.

T is symmetric: ⟨Tx,y⟩ = ⟨x,Ty⟩ for all x,y ∈ Dom(T).
  Symmetric ≠ self-adjoint in general (need Dom(T) = Dom(T*)).

T is self-adjoint: T = T* (including domains).

T is essentially self-adjoint: T̄ (closure) is self-adjoint.
```

**Schrödinger operator**: H = -ℏ²/(2m)Δ + V(x) on L²(ℝ³).
- Δ = Laplacian (unbounded).
- V(x) = potential (multiplication operator).
- For "nice" V: H is essentially self-adjoint. Self-adjointness = physical observability.
- Spectrum: discrete eigenvalues (bound states) + continuous spectrum (scattering states).

### Stone's Theorem for Unbounded Operators

(See Section 7 for the full statement.) For unbounded self-adjoint A, Stone's theorem still holds:
```
U(t) = e^{itA} = ∫_ℝ e^{itλ} dE_A(λ)

where E_A is defined via the spectral theorem for unbounded self-adjoint operators.
The domain condition: U(t)ψ is differentiable at t=0 iff ψ ∈ Dom(A).
```

**Kato-Rellich theorem**: If A is self-adjoint and B is A-bounded with relative bound < 1
(meaning ||Bψ|| ≤ a||Aψ|| + b||ψ|| for some a < 1), then A + B is self-adjoint on Dom(A).
This is the main tool for establishing self-adjointness of Schrödinger operators: H = -Δ + V where V is Kato-bounded relative to the Laplacian.

---

## 9. Sobolev Spaces and PDEs

### Weak Derivatives

For f ∈ L¹_loc(Ω), the **weak derivative** D^α f is the function g satisfying:
```
∫_Ω f · D^α φ dx = (-1)^|α| ∫_Ω g · φ dx   for all φ ∈ C_c^∞(Ω).

If f is classically differentiable: classical = weak derivative.
But weak derivatives exist for much more irregular functions.
```

### Sobolev Space H^k(Ω)

```
H^k(Ω) = W^{k,2}(Ω) = {f ∈ L²(Ω) : D^α f ∈ L²(Ω) for all |α| ≤ k}

Inner product: ⟨f,g⟩_{H^k} = Σ_{|α|≤k} ⟨D^α f, D^α g⟩_{L²}

H⁰(Ω) = L²(Ω).
H¹(Ω): functions in L² with L² weak first derivatives.
H₀^k(Ω): closure of C_c^∞(Ω) in H^k norm. Functions that "vanish" at boundary.

Sobolev embedding theorem: (Ω ⊆ ℝⁿ bounded, smooth boundary)
  If k > n/2 + m: H^k(Ω) ⊆ C^m(Ω)  [Sobolev embeds into classical C^m]
  In 1D (n=1): H¹(Ω) ⊆ C(Ω). L²-functions with L² derivative are continuous.
```

### Weak Formulation of PDEs

Classical approach: find u satisfying PDE pointwise. Requires u to be classically differentiable.

Weak approach: find u ∈ H¹(Ω) satisfying integral identity.

```
Poisson equation: -Δu = f on Ω,  u = 0 on ∂Ω.

Multiply by test function v ∈ H₀¹(Ω), integrate:
  ∫ ∇u · ∇v dx = ∫ f v dx   (after integration by parts)

Define: a(u,v) = ∫ ∇u·∇v dx   [bilinear form]
        F(v) = ∫ f v dx        [linear functional]

Weak problem: find u ∈ H₀¹(Ω) s.t. a(u,v) = F(v) for all v ∈ H₀¹(Ω).

Lax-Milgram theorem: If a is bounded and coercive (a(u,u) ≥ α||u||²),
  then ∃! weak solution u.

Coercivity for Poisson: a(u,u) = ∫|∇u|² dx = ||∇u||²_{L²}.
Poincaré inequality: ||u||_{L²} ≤ C||∇u||_{L²} for u ∈ H₀¹.
→ a(u,u) ≥ (1/C)||u||²_{H¹}. Coercive!
```

**FEM (Finite Element Method)**: Discretize H₀¹(Ω) by piecewise polynomial finite-dimensional subspace V_h. Solve Galerkin approximation: find u_h ∈ V_h s.t. a(u_h, v_h) = F(v_h) for all v_h ∈ V_h. Leads to sparse linear system.

### Numerical Analysis: Krylov Methods and Operator Theory

Functional analysis is the theoretical backbone for convergence analysis of iterative solvers. The connection is not incidental — these methods are projections in Hilbert space.

**Krylov subspace methods**: Given linear system Ax = b (A self-adjoint positive definite on ℝⁿ, or abstractly on H):
```
Krylov subspace: K_k(A, r₀) = span{r₀, Ar₀, A²r₀, ..., A^{k-1}r₀}
  where r₀ = b - Ax₀ is the initial residual.

Conjugate Gradient (CG): find xₖ ∈ x₀ + K_k(A,r₀) minimizing ||x - x*||_A
  where ||v||_A = √(v, Av)  [the energy norm, = ||A^{1/2}v||₂].

This is orthogonal projection onto K_k(A,r₀) in the A-inner product.

Convergence bound (spectral condition number κ = λ_max/λ_min):
  ||xₖ - x*||_A ≤ 2 (√κ - 1)ᵏ / (√κ + 1)ᵏ · ||x₀ - x*||_A

The key quantity is the spectral distribution of A (distribution of eigenvalues
under the spectral measure E_A). If eigenvalues cluster, convergence is fast
even if κ is large.
```

**Why spectral theory drives convergence**: CG minimizes a polynomial p(A)r₀ where p ranges over degree-k polynomials with p(0)=1. By the spectral theorem:
```
||p(A)r₀||² = ∫ |p(λ)|² d||E(λ)r₀||²

Convergence = minimize a polynomial over the spectrum of A weighted by the
spectral measure of the initial residual. Clustered eigenvalues → low-degree
polynomial approximates zero on the cluster → fast convergence.

This connects:
  - Abstract spectral theory (projection-valued measure E)
  - Chebyshev polynomial approximation (optimal polynomial for [a,b])
  - Preconditioners (shift/cluster the spectrum)
```

**Operator splitting**: Time-integration of ∂_t u = (A + B)u (stiff PDEs):
```
Lie-Trotter splitting: e^{t(A+B)} ≈ (e^{tA/n} e^{tB/n})ⁿ  → exact as n→∞
Strang splitting:      e^{t(A+B)} ≈ e^{tA/2} e^{tB} e^{tA/2}  [2nd order]

Error via BCH formula: e^X e^Y = e^{X+Y+½[X,Y]+O(||...||³)}
  First-order error = [A,B] (commutator of operators).
  If [A,B] = 0 (operators commute): splitting is exact.
  If [A,B] ≠ 0: error proportional to t²||[A,B]|| per step.

For Schrödinger: e^{-iHt/ℏ} = e^{-iT t/ℏ} e^{-iVt/ℏ} + O(t²)
  T = kinetic (diagonal in Fourier space), V = potential (diagonal in position space).
  Split-step Fourier: alternating FFT and pointwise multiplication → spectral method.
```

---

## 10. Fredholm Theory

### Fredholm Operators

T: X → Y is **Fredholm** if:
```
dim ker(T) < ∞     [finite-dimensional kernel]
dim coker(T) < ∞   [coker = Y/Im(T), finite-dimensional cokernel]
Im(T) closed       [range is closed]

Fredholm index: ind(T) = dim ker(T) - dim coker(T)
```

**Compact perturbation**: If T Fredholm and K compact, then T+K is Fredholm with same index.

**Atiyah-Singer Index Theorem** (1963): For elliptic differential operators on compact manifolds, the analytic index (Fredholm index) equals a topological invariant (K-theory class / characteristic classes). One of the most celebrated results in 20th-century mathematics.

```
Simplest case: for a Fredholm operator T,
  ind(T) = dim ker(T) - dim ker(T*)
  This is a stable quantity: ind(T+K) = ind(T) for K compact.
```

---

## 11. RKHS and Kernel Methods (ML Bridge)

### From Operators to Attention: The Integral Operator Perspective

Before the RKHS definition, a concrete bridge connecting the spectral theory above to modern neural networks:

The **attention mechanism** in transformers is a discretized integral operator. For queries Q, keys K, values V (each n×d matrices, n = sequence length):
```
Attention(Q,K,V) = softmax(QKᵀ/√d) · V

This is a discretization of the integral operator:
  (Tf)(x) = ∫ K(x,y) f(y) dμ(y)

where the kernel K(x,y) = softmax_y(qₓᵀk_y / √d) is the attention weight.

Connection to functional analysis:
  - T is an integral operator on a function space (L² or RKHS)
  - The attention matrix softmax(QKᵀ/√d) is the matrix representation of T
    with respect to the n basis points {x₁,...,xₙ}
  - The operator is low-rank (each head computes rank at most d attention)
  - PCA / SVD of the attention matrix = spectral decomposition of T

Self-attention is positive semi-definite when K(x,y) = K(y,x) (symmetric kernel).
In that case: attention = orthogonal projection in RKHS defined by K.
```

**Neural operators** (FNO, DeepONet): these learn operators F: function → function. The Fourier Neural Operator (FNO) parameterizes integral operators directly:
```
(K_θ u)(x) = ∫ κ_θ(x,y) u(y) dy  [integral kernel layer]

In Fourier space: multiplication by learnable weight R_θ(ω).
Convergence analysis uses exactly the spectral theory of Section 6:
  approximate the target operator by its projection onto low-frequency modes.
```

### Reproducing Kernel Hilbert Spaces (RKHS)

An **RKHS** is a Hilbert space H of functions f: X → ℝ such that point evaluations are bounded linear functionals:
```
For each x ∈ X, ∃ Kₓ ∈ H such that f(x) = ⟨f, Kₓ⟩_H   [reproducing property]

The kernel: K(x,y) = ⟨K_y, K_x⟩_H = Kₓ(y).
```

**Mercer's theorem**: K: X×X → ℝ is the kernel of an RKHS iff K is:
- Symmetric: K(x,y) = K(y,x)
- Positive definite: Σᵢⱼ cᵢcⱼ K(xᵢ,xⱼ) ≥ 0 for all {cᵢ}, {xᵢ}

```
Common kernels:
  Linear:     K(x,y) = x'y
  Polynomial: K(x,y) = (x'y + c)^d
  RBF/Gaussian: K(x,y) = exp(-||x-y||²/(2σ²))  ← infinite-dimensional feature map
  Matérn:     fractional smoothness parameter ν → control regularity of GP
```

### Representer Theorem

For regularized regression in RKHS:
```
min_{f ∈ H} Σᵢ L(yᵢ, f(xᵢ)) + λ||f||²_H

Solution has the form: f*(x) = Σᵢ αᵢ K(xᵢ, x)

Only n-dimensional optimization needed despite infinite-dimensional search space.
This is the mathematical foundation of SVMs, Gaussian process regression, spline regression.
```

**Kernel trick**: Replace inner products ⟨φ(x),φ(y)⟩ in feature space by kernel evaluations K(x,y). Never need to compute infinite-dimensional feature maps φ(x) explicitly.

---

## Decision Cheat Sheet

```
Space type:                                 Structure:
────────────────────────────────────────    ──────────────────────────────────────────
Metric + complete                           Banach (if vector space)
Banach + inner product                      Hilbert
Separable Hilbert (infinite-dim)            ≅ ℓ² (up to isometric isomorphism)
Non-reflexive                               ℓ¹, ℓ∞, L¹, L∞, C[a,b]

Operator type:                              What it gives you:
Bounded self-adjoint                        Spectral theorem via PVM
Compact self-adjoint                        ONB of eigenvectors, discrete spectrum
Compact + Fredholm                          Well-posedness, index theory
Unbounded self-adjoint                      QM observable; use Stone's theorem for e^{itA}
Symmetric but not self-adjoint              No spectral theorem; not a valid QM observable

PDE question:                               Tool:
"Does solution exist/unique?"               Lax-Milgram (coercive bilinear form on H¹)
"Can I extract converging subsequence?"     Banach-Alaoglu (weak* compact unit ball)
"How smooth is the solution?"              Sobolev embedding theorem
"PDE on curved manifold?"                   Atiyah-Singer (topology of operator)

QM question:                                Tool:
Observable has real spectrum?               Self-adjoint (not just symmetric)
Unitary time evolution?                     Stone's theorem: A self-adjoint → e^{itA} unitary
Algebraic QM without Hilbert space?         C*-algebra + GNS construction
Position/momentum uncertainty?             [Q,P] = iℏI → Robertson inequality

Numerical question:                         Tool:
Iterative solver convergence rate?         Spectral distribution of A; condition number
Preconditioner design?                      Cluster eigenvalues to improve polynomial approx
Time-splitting error?                       BCH formula; error = t²||[A,B]||

ML question:                                Tool:
Kernel regression                           RKHS + Representer theorem
Infinite-dimensional features implicitly    Mercer kernel trick
Function space smoothness priors            Sobolev space regularization
Gaussian process covariance                 Mercer decomposition of kernel
Attention as operator                       Integral operator with softmax kernel
Neural operator convergence                 Spectral approximation theory
```

---

## Common Confusion Points

**Bounded ≠ finite-valued**: A bounded operator maps bounded sets to bounded sets. The operator itself can map to very large values — just not unboundedly so. Bounded = continuous for linear maps.

**Self-adjoint ≠ symmetric for unbounded operators**: A symmetric operator satisfies ⟨Tx,y⟩=⟨x,Ty⟩ on its domain. Self-adjoint requires additionally that Dom(T) = Dom(T*). This distinction matters for QM: only self-adjoint operators have a spectral theorem and generate unitary groups (Stone's theorem).

**Weak convergence ≠ strong convergence**: The orthonormal sequence eₙ satisfies eₙ ⇀ 0 weakly in any Hilbert space (Fourier coefficients → 0) but ||eₙ|| = 1 ≠ 0. In infinite dimensions, weak convergence is strictly weaker.

**Compact operators are "almost finite-rank"**: A compact operator on a separable Hilbert space is the limit of finite-rank operators. It cannot be invertible (its image is not closed unless finite-dimensional). The Fredholm alternative applies precisely because compact operators are "small" perturbations.

**Sobolev spaces are not classical function spaces**: H¹[0,1] contains functions with L² (not pointwise) derivatives. The Sobolev embedding theorem tells you when H^k functions have classical regularity. Without the embedding condition k > n/2 + m, functions in H^k may be discontinuous.

**RKHS norm ≠ L² norm**: The RKHS norm ||f||_H measures smoothness (controls function oscillation), not just L² size. For Gaussian RBF kernel, high ||f||_H means highly oscillatory function. Regularization ||f||²_H penalizes complex functions, implementing Occam's razor.

**Dual of L∞ is bigger than L¹**: (L∞)* ≅ the space of finitely additive signed measures (ba[0,1]), which strictly contains L¹. This is why L∞ is not reflexive. For 1 < p < ∞, the duality (Lᵖ)* = Lᵍ is clean; at the endpoints it breaks.

**Stone's theorem requires self-adjoint, not just symmetric**: There exist symmetric operators that are not essentially self-adjoint and do not generate unitary groups. The self-adjointness condition (or essential self-adjointness) is the precise mathematical requirement for well-posed quantum dynamics.

**C*-identity is the key axiom**: The condition ||a*a|| = ||a||² is what makes C*-algebras special among Banach *-algebras. It forces the norm to be determined by the algebraic structure and gives the Gelfand-Naimark theorem (every C*-algebra embeds isometrically into B(H)).
