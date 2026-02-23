# 06 — Linear Algebra: Vectors, Matrices, Eigenstructure, and SVD

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  VECTOR SPACES          MATRICES               EIGENSTRUCTURE
  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
  │ abstract spaces │    │ linear maps      │    │ Av = λv         │
  │ span, basis     │ →  │ rank, null space │ →  │ diagonalization │
  │ dimension       │    │ row reduction    │    │ spectral theorem │
  └────────┬────────┘    └────────┬────────┘    └────────┬────────┘
           │                     │                       │
           ▼                     ▼                       ▼
  INNER PRODUCTS         DECOMPOSITIONS          APPLICATIONS
  ┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
  │ dot product     │    │ LU, QR, Cholesky│    │ QM: Hermitian   │
  │ orthogonality   │    │ SVD — the king  │    │ PCA, least sq.  │
  │ Gram-Schmidt    │    │ eigendecomp     │    │ DFT as matrix   │
  └─────────────────┘    └─────────────────┘    └─────────────────┘

  CENTRAL THESIS:
  A matrix is a linear map between vector spaces.
  Eigenvalues reveal the intrinsic geometry of that map.
  SVD reveals the geometry of ANY linear map, even non-square.
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. Vector Spaces

### 1.1 The Abstract Definition

A **vector space** V over field F satisfies:

```
  (V, +) is an abelian group
  Scalar multiplication: F × V → V
  ├── α(u + v) = αu + αv    (distributive over vector addition)
  ├── (α + β)v = αv + βv    (distributive over scalar addition)
  ├── (αβ)v = α(βv)          (associative)
  └── 1·v = v                (identity)

  EXAMPLES:
  ℝⁿ — standard n-dimensional real space
  ℂⁿ — complex n-space (QM lives here)
  Polynomials of degree ≤ n — infinite-dim function spaces
  Continuous functions C([a,b]) — infinite-dimensional
  Solutions to a linear ODE — finite-dimensional (!)
  L²(ℝ) — square-integrable functions (QM Hilbert space)
```

### 1.2 Span, Linear Independence, Basis, Dimension

```
  Span{v₁,...,vₖ} = {α₁v₁ + ... + αₖvₖ | αᵢ ∈ F}
  = all linear combinations

  LINEARLY INDEPENDENT: α₁v₁ + ... + αₖvₖ = 0 ⟹ all αᵢ = 0

  BASIS: linearly independent set that spans V

  DIMENSION dim(V): number of vectors in any basis
  (all bases of a finite-dimensional space have the same size)

  Standard basis of ℝⁿ: e₁=(1,0,...,0), e₂=(0,1,...,0), ..., eₙ=(0,...,0,1)

  Key theorem: if dim(V) = n, any n linearly independent vectors form a basis.
```

### 1.3 Subspaces

```
  W ⊆ V is a subspace if:
  ├── 0 ∈ W
  ├── u, v ∈ W ⟹ u + v ∈ W
  └── v ∈ W, α ∈ F ⟹ αv ∈ W

  Sum: W₁ + W₂ = {w₁ + w₂ | wᵢ ∈ Wᵢ}
  Direct sum: V = W₁ ⊕ W₂ means W₁ ∩ W₂ = {0} and W₁ + W₂ = V

  Dimension formula: dim(W₁ + W₂) = dim(W₁) + dim(W₂) - dim(W₁ ∩ W₂)
```

---

## 2. Matrices as Linear Maps

### 2.1 The Fundamental View

```
  Matrix A ∈ M_{m×n}(F) defines a linear map T: Fⁿ → Fᵐ by T(x) = Ax

  FOUR FUNDAMENTAL SUBSPACES of A ∈ M_{m×n}:
  ┌────────────────────────────────────────────────────────────────────┐
  │                                                                    │
  │  Column space (range):   C(A) = {Ax | x ∈ Fⁿ}    ⊆ Fᵐ           │
  │  Null space (kernel):    N(A) = {x | Ax = 0}       ⊆ Fⁿ          │
  │  Row space:              C(Aᵀ)                     ⊆ Fⁿ          │
  │  Left null space:        N(Aᵀ)                     ⊆ Fᵐ          │
  │                                                                    │
  │  RANK-NULLITY THEOREM:                                             │
  │  rank(A) + nullity(A) = n                                         │
  │  dim C(A) + dim N(A) = number of columns                          │
  │                                                                    │
  │  ORTHOGONALITY:                                                    │
  │  C(A) ⊥ N(Aᵀ)    (column space ⊥ left null space, both in Fᵐ)   │
  │  C(Aᵀ) ⊥ N(A)    (row space ⊥ null space, both in Fⁿ)           │
  └────────────────────────────────────────────────────────────────────┘

  RANK = dim C(A) = dim C(Aᵀ) = number of pivots after row reduction
```

### 2.2 Row Reduction — Gaussian Elimination

```
  Three elementary row operations (each = multiplication by an elementary matrix):
  1. Swap rows i and j
  2. Scale row i by nonzero scalar
  3. Add multiple of row i to row j

  REDUCED ROW ECHELON FORM (RREF):
  ┌                      ┐         Pivots (leading 1s): mark rank
  │ 1  0  2  0  3  │ 5  │    ←    columns are pivot columns
  │ 0  1 -1  0  2  │ 3  │    ←    free variables: non-pivot columns
  │ 0  0  0  1  4  │ -1 │
  │ 0  0  0  0  0  │ 0  │    ←    consistent (no 0=nonzero rows)
  └                      ┘

  From RREF you read off:
  ├── rank (number of pivots = 3 here)
  ├── null space basis (one free variable vector per free column)
  ├── particular solution to Ax = b (if consistent)
  └── whether system is consistent (0 row with nonzero RHS = inconsistent)
```

### 2.3 Matrix Operations

```
  Addition:         (A + B)ᵢⱼ = Aᵢⱼ + Bᵢⱼ    (same dimensions)
  Scalar mult:      (αA)ᵢⱼ = αAᵢⱼ
  Multiplication:   (AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ       (m×n)(n×p) → m×p
  Transpose:        (Aᵀ)ᵢⱼ = Aⱼᵢ
  Conjugate trans:  A† = (A*)ᵀ  (Hermitian conjugate — used in QM)

  Properties:
  (AB)ᵀ = BᵀAᵀ           (AB)† = B†A†
  (AB)⁻¹ = B⁻¹A⁻¹         (reverse order for both!)
  tr(AB) = tr(BA)          (trace is cyclic, even for non-square)
  det(AB) = det(A)det(B)
```

### 2.4 Determinant

```
  det: M_{n×n} → F

  Geometric meaning: signed volume scaling factor of the linear map.
  If det(A) = 0: map is singular, collapses dimension, not invertible.
  If det(A) ≠ 0: invertible.

  2×2: det([a b; c d]) = ad - bc
  3×3: cofactor expansion along any row or column

  Key properties:
  det(Aᵀ) = det(A)
  det(A⁻¹) = 1/det(A)
  det(αA) = αⁿ det(A)   for n×n matrix
  Row swap: flips sign
  Row scale by c: multiplies det by c
  det of triangular matrix: product of diagonal entries
```

### 2.5 Inverse

```
  A⁻¹ exists ↔ det(A) ≠ 0 ↔ rank(A) = n ↔ N(A) = {0}

  2×2 inverse:
  [a b]⁻¹    1   [ d -b]
  [c d]   = ─── [-c  a]
             ad-bc

  Numerical: don't compute A⁻¹ to solve Ax = b.
  Use LU decomposition: LUx = b → Ly = b (forward sub) → Ux = y (back sub)
  Computing A⁻¹ explicitly is ~3× more work and numerically worse.
```

---

## 3. Inner Products and Orthogonality

### 3.1 Inner Product

```
  Inner product ⟨·,·⟩: V × V → F  satisfying:
  ├── Linearity in first argument:  ⟨αu+βv, w⟩ = α⟨u,w⟩ + β⟨v,w⟩
  ├── Conjugate symmetry:           ⟨u,v⟩ = ⟨v,u⟩*  (= ⟨v,u⟩ over ℝ)
  └── Positive definite:            ⟨v,v⟩ ≥ 0, = 0 iff v = 0

  Standard inner products:
  ℝⁿ: ⟨x,y⟩ = xᵀy = Σᵢ xᵢyᵢ               (dot product)
  ℂⁿ: ⟨x,y⟩ = x†y = Σᵢ xᵢ*yᵢ              (QM inner product)
  L²: ⟨f,g⟩ = ∫ f*(x)g(x) dx               (function space — QM)

  Norm:  ‖v‖ = √⟨v,v⟩
  Cauchy-Schwarz: |⟨u,v⟩| ≤ ‖u‖·‖v‖
  Angle: cos θ = ⟨u,v⟩/(‖u‖‖v‖)
```

### 3.2 Orthogonality

```
  u ⊥ v  iff  ⟨u,v⟩ = 0

  ORTHONORMAL BASIS: {e₁,...,eₙ} with ⟨eᵢ,eⱼ⟩ = δᵢⱼ  (Kronecker delta)

  Orthonormal expansion: v = Σᵢ ⟨eᵢ,v⟩ eᵢ
  (coordinates = projections onto basis vectors)

  ORTHOGONAL PROJECTION onto subspace W:
  Pᵥᵥ = projection of v onto W
  v = Pᵥ + (v - Pᵥ)   where  Pᵥ ∈ W  and  (v - Pᵥ) ⊥ W

  This is the geometry behind least squares:
  Ax = b has no solution → find x minimizing ‖Ax - b‖²
  → Ax* = projection of b onto C(A) → normal equations AᵀAx = Aᵀb
```

### 3.3 Gram-Schmidt Orthogonalization

```
  Given basis {v₁, v₂, ..., vₙ}, produce orthonormal basis {u₁, ..., uₙ}:

  u₁ = v₁/‖v₁‖

  v₂' = v₂ - ⟨u₁,v₂⟩u₁        (subtract projection onto u₁)
  u₂ = v₂'/‖v₂'‖

  v₃' = v₃ - ⟨u₁,v₃⟩u₁ - ⟨u₂,v₃⟩u₂
  u₃ = v₃'/‖v₃'‖

  ...and so on.

  This produces the QR decomposition: A = QR
  Q = orthonormal columns, R = upper triangular
  Used in: least squares, eigenvalue algorithms, Fourier series
  (orthonormal basis of sin/cos is Gram-Schmidt on {1, x, x², ...} in L²)
```

---

## 4. Eigenvalues and Eigenvectors

### 4.1 The Definition

```
  Av = λv   where v ≠ 0

  λ = eigenvalue (scalar), v = eigenvector (direction preserved by A)

  Rewrite: (A - λI)v = 0
  Non-trivial solution exists ↔ det(A - λI) = 0

  CHARACTERISTIC POLYNOMIAL:
  p(λ) = det(A - λI)  = (-1)ⁿ(λⁿ - tr(A)λⁿ⁻¹ + ... + (-1)ⁿdet(A))

  Roots of p(λ) = eigenvalues (counted with algebraic multiplicity)
  Over ℂ: n×n matrix always has exactly n eigenvalues (fundamental theorem)
  Over ℝ: may have complex conjugate pairs
```

### 4.2 Computing Eigenvalues and Eigenvectors

```
  STEP 1: Solve det(A - λI) = 0 → get eigenvalues λ₁, λ₂, ...

  STEP 2: For each λᵢ, solve (A - λᵢI)v = 0 → get eigenvectors
          Eigenspace E(λᵢ) = N(A - λᵢI)

  EXAMPLE: A = [3 1; 0 2]
  det(A - λI) = (3-λ)(2-λ) - 0 = (3-λ)(2-λ) = 0
  λ₁ = 3, λ₂ = 2

  For λ₁=3: (A-3I)v = [0 1; 0 -1]v = 0 → v₁ = (1,0)
  For λ₂=2: (A-2I)v = [1 1; 0 0]v = 0 → v₂ = (-1,1)

  GEOMETRIC vs ALGEBRAIC MULTIPLICITY:
  Algebraic multiplicity: multiplicity as root of characteristic polynomial
  Geometric multiplicity: dim(eigenspace) = dim N(A - λI)
  Geometric ≤ Algebraic always
  A is diagonalizable ↔ Geometric = Algebraic for all eigenvalues
```

### 4.3 Diagonalization

```
  If A has n linearly independent eigenvectors v₁,...,vₙ with eigenvalues λ₁,...,λₙ:

  A = PDP⁻¹

  where P = [v₁ | v₂ | ... | vₙ]  (eigenvectors as columns)
        D = diag(λ₁, λ₂, ..., λₙ)  (eigenvalues on diagonal)

  Powers: Aᵏ = PDᵏP⁻¹ = P·diag(λ₁ᵏ,...,λₙᵏ)·P⁻¹
  Functions: f(A) = Pf(D)P⁻¹ = P·diag(f(λ₁),...,f(λₙ))·P⁻¹

  Applications:
  ├── Solving linear ODEs: x' = Ax → x(t) = e^(At) x(0) = Pe^(Dt)P⁻¹x(0)
  ├── Markov chains: Aᵏ → dominant eigenvector (PageRank)
  └── Principal Component Analysis: covariance matrix diagonalization
```

### 4.4 Special Matrix Classes

```
  SYMMETRIC (real): A = Aᵀ
  ├── All eigenvalues are real
  ├── Eigenvectors for distinct eigenvalues are orthogonal
  └── Always diagonalizable: A = QΛQᵀ  (Q orthogonal)

  HERMITIAN (complex): A = A†  (A† = conjugate transpose)
  ├── All eigenvalues are real    ← CRITICAL FOR QM
  ├── Eigenvectors form orthonormal basis
  └── A = UΛU†  (U unitary)
  This is why QM observables are Hermitian: eigenvalues = measurement results = real

  SKEW-SYMMETRIC: A = -Aᵀ → purely imaginary eigenvalues
  UNITARY: U†U = I → eigenvalues on unit circle |λ| = 1
  NORMAL: A†A = AA† → unitarily diagonalizable (includes Hermitian, unitary, skew-Hermitian)

  POSITIVE DEFINITE: ⟨v, Av⟩ > 0 for all v ≠ 0
  ↔ all eigenvalues > 0
  ↔ A = BᵀB for some invertible B  (Cholesky: A = LLᵀ)
  ├── Covariance matrices are positive semidefinite
  └── Used in optimization (Hessian positive definite → local minimum)
```

---

## 5. The Spectral Theorem

```
  SPECTRAL THEOREM (real symmetric):
  Every real symmetric matrix A = QΛQᵀ where:
  Q is orthogonal (Qᵀ = Q⁻¹), Λ = diag(λ₁,...,λₙ) real

  Equivalently: A = Σᵢ λᵢ qᵢqᵢᵀ    (spectral decomposition)
  Each qᵢqᵢᵀ is a rank-1 projection onto the i-th eigenvector.
  A is a weighted sum of orthogonal projections.

  SPECTRAL THEOREM (complex Hermitian / normal):
  A = UΛU†  where U is unitary

  PHYSICS: In QM, every observable A is Hermitian.
  Measurement of A:
  ├── Possible outcomes = eigenvalues λᵢ (must be real → Hermitian)
  ├── Probability of λᵢ = |⟨ψᵢ, ψ⟩|²  (Born rule = projection squared)
  └── After measurement: state collapses to eigenvector ψᵢ

  The spectral theorem IS quantum mechanics, mathematically.
```

---

## 6. Singular Value Decomposition (SVD)

### 6.1 The Theorem

```
  Every matrix A ∈ M_{m×n} (real or complex) has:

  A = UΣVᵀ    (real case)    or    A = UΣV†  (complex case)

  U ∈ M_{m×m}: orthogonal (unitary)  — left singular vectors
  Σ ∈ M_{m×n}: "diagonal" with σ₁ ≥ σ₂ ≥ ... ≥ σᵣ ≥ 0 on diagonal
  V ∈ M_{n×n}: orthogonal (unitary)  — right singular vectors

  σᵢ = singular values = √(eigenvalues of AᵀA) = √(eigenvalues of AAᵀ)
  r = rank(A)
  u columns of U = left singular vectors (eigenvectors of AAᵀ)
  v columns of V = right singular vectors (eigenvectors of AᵀA)
```

### 6.2 Geometric Interpretation

```
  WHAT SVD SAYS ABOUT THE LINEAR MAP T: Rⁿ → Rᵐ

  Every linear map is:
  1. ROTATION/REFLECTION in Rⁿ        (multiplication by Vᵀ)
  2. SCALING along coordinate axes    (multiplication by Σ)
  3. ROTATION/REFLECTION in Rᵐ        (multiplication by U)

  ┌─────┐  Vᵀ  ┌─────┐  Σ   ┌─────┐  U   ┌─────┐
  │ Rⁿ  │ ──→  │ Rⁿ  │ ──→  │ Rᵐ  │ ──→  │ Rᵐ  │
  └─────┘      └─────┘      └─────┘      └─────┘
  original     rotated      scaled       final
  space        to align     + embedded   rotated

  σ₁ = largest singular value = operator norm ‖A‖₂ = max stretch factor
  σᵣ = smallest nonzero singular value = "how close to singular"
  Condition number κ(A) = σ₁/σᵣ — measures numerical sensitivity
```

### 6.3 Low-Rank Approximation — The Killer Application

```
  ECKART-YOUNG THEOREM:
  Best rank-k approximation to A (in both Frobenius and operator norm):

  Aₖ = Σᵢ₌₁ᵏ σᵢ uᵢ vᵢᵀ    (keep top k singular value/vector triples)

  This is optimal — no rank-k matrix is closer to A.

  APPLICATIONS:
  ┌────────────────────────────────────────────────────────────────────┐
  │  Image compression: A = image matrix, Aₖ = compressed version    │
  │  k=10 terms: ~90% quality, 10× compression                       │
  │                                                                    │
  │  PCA (Principal Component Analysis):                              │
  │  Center data, compute SVD of data matrix X                        │
  │  Principal components = right singular vectors (rows of Vᵀ)      │
  │  Variance captured = σᵢ²/Σσᵢ²                                    │
  │                                                                    │
  │  Latent Semantic Analysis (pre-deep learning NLP):                │
  │  Term-document matrix → SVD → semantic "topics"                  │
  │                                                                    │
  │  Recommender systems (Netflix Prize era): matrix factorization    │
  │  Ratings matrix ≈ UΣVᵀ, fill in missing entries from low-rank   │
  └────────────────────────────────────────────────────────────────────┘
```

### 6.4 Pseudoinverse

```
  For non-square or singular A, the Moore-Penrose pseudoinverse A⁺:

  A = UΣVᵀ  →  A⁺ = VΣ⁺Uᵀ
  where Σ⁺ = diag(1/σ₁, ..., 1/σᵣ, 0, ..., 0)

  Least-squares solution to Ax ≈ b: x* = A⁺b
  x* is the minimum-norm solution when multiple solutions exist.
  This is what `numpy.linalg.lstsq` computes.
```

---

## 7. Key Decompositions

```
  DECOMPOSITION  FORM        WHEN TO USE
  ──────────────────────────────────────────────────────────────────────
  LU             A = LU      Solving Ax = b (Gaussian elimination)
                             Works for any square invertible A
                             (with partial pivoting: PA = LU)

  Cholesky       A = LLᵀ     A symmetric positive definite
                             2× faster than LU, numerically stable
                             Covariance matrices, optimization

  QR             A = QR      Least squares (overdetermined Ax ≈ b)
                             Eigenvalue algorithms (QR iteration)
                             Always exists, even for m×n matrices

  Eigendecomp    A = PDP⁻¹  A diagonalizable square matrix
                             Matrix functions, ODEs, Markov chains

  Schur          A = QTQ*    Any square matrix (T upper triangular)
                             Numerically stable eigenvalue computation

  SVD            A = UΣVᵀ   Any matrix, any shape
                             PCA, low-rank approx, pseudoinverse
                             The universal tool

  ──────────────────────────────────────────────────────────────────────
  RULE: For solving Ax = b → LU. For least squares → QR. For everything else → SVD.
```

---

## 8. Change of Basis

```
  Suppose V has two bases: B = {b₁,...,bₙ} and C = {c₁,...,cₙ}

  Change-of-basis matrix P: [v]_B = P·[v]_C
  (P's columns are the C-coordinates of the B-basis vectors)

  Linear map A in basis B:  [T]_B = P⁻¹[T]_C P   (similarity transform)

  SIMILARITY TRANSFORMS don't change:
  ├── Eigenvalues
  ├── Determinant
  ├── Trace
  └── Rank

  DIAGONALIZATION is just change of basis to the eigenbasis:
  In eigenbasis, A acts as pure scaling. Off-diagonal = coupling.
  Decoupling: if A is diagonal, coordinates evolve independently.
```

---

## 9. The DFT as a Matrix

The Discrete Fourier Transform is exactly a change of basis:

```
  DFT of x ∈ ℂⁿ:  X = Fₙ x

  where Fₙ is the DFT matrix:
  (Fₙ)ₖₗ = (1/√n) ω^(kl)    ω = e^(-2πi/n)  (primitive n-th root of unity)

  F is UNITARY: Fₙ†Fₙ = I  (orthonormal basis of complex exponentials)

  Columns of Fₙ = Fourier basis vectors = eigenvectors of cyclic shift matrix!

  The DFT diagonalizes the circular convolution operator.
  Convolution in time domain = pointwise multiplication in frequency domain.
  This is Fₙ's eigendecomposition.

  FFT: computes Fₙx in O(n log n) instead of O(n²) via Cooley-Tukey recursion.
```

---

## 10. Linear Algebra in Quantum Mechanics

The full dictionary (building on module 08-QUANTUM-BRIDGE):

```
  MATH OBJECT              QM OBJECT
  ───────────────────────────────────────────────────────────────────
  Complex vector space      Hilbert space ℋ
  Vector v ∈ ℋ              State |ψ⟩ (ket)
  Dual vector vᵀ            Bra ⟨ψ|
  Inner product ⟨v,u⟩       Amplitude ⟨φ|ψ⟩  (prob amplitude)
  |⟨v,u⟩|²                  Transition probability
  Orthonormal basis         Complete set of orthonormal states
  Hermitian operator A      Observable (position, momentum, energy)
  Eigenvalue λ              Measurement outcome
  Eigenvector               Definite-value state
  A = Σ λᵢ|ψᵢ⟩⟨ψᵢ|          Spectral decomposition of observable
  Projection |ψᵢ⟩⟨ψᵢ|       Measurement operator
  Unitary operator U        Time evolution e^(-iHt/ℏ), quantum gates
  Tensor product ⊗          Multi-particle state space
  Partial trace             Tracing out environment (open systems)
  Density matrix ρ          Mixed state (statistical ensemble)
  ───────────────────────────────────────────────────────────────────

  COMMUTATOR [A,B] = AB - BA:
  [x̂, p̂] = iℏ               canonical commutation relation
  [Jᵢ, Jⱼ] = iℏ εᵢⱼₖ Jₖ    angular momentum algebra (= SU(2) algebra!)
  [H, A] = 0 ↔ A conserved  (A commutes with Hamiltonian ↔ A is conserved)
```

---

## Decision Cheat Sheet

| Need to... | Use... |
|-----------|--------|
| Solve square Ax = b | LU decomposition |
| Solve overdetermined Ax ≈ b | QR or SVD pseudoinverse |
| Find eigenvalues/vectors | Characteristic polynomial → eigenspaces |
| Diagonalize A | Check geometric = algebraic multiplicity |
| Compress a matrix / find structure | SVD |
| Check if positive definite | All eigenvalues > 0 (or Cholesky succeeds) |
| Change basis | Similarity transform P⁻¹AP |
| Find orthonormal basis | Gram-Schmidt |
| Project v onto subspace W | Normal equations, QR |
| Understand a QM observable | Spectral theorem for Hermitian operators |

---

## Common Confusion Points

**"Eigenvectors are only defined up to scaling — which one is 'correct'?"**
Any nonzero scalar multiple of an eigenvector is also an eigenvector. The eigenspace (all scalar multiples) is what's intrinsic. In practice, normalize to unit length for numerical work. For degenerate eigenspaces (dim > 1), any basis of that subspace works — you choose the most convenient one.

**"What's the difference between diagonalization and SVD?"**
Eigendecomposition A = PDP⁻¹ requires a square matrix with n independent eigenvectors; P is not generally orthogonal. SVD A = UΣVᵀ works for *any* matrix (any shape); U and V are *both orthogonal*; Σ is real and non-negative on the diagonal. SVD always exists; eigendecomposition doesn't. For symmetric positive definite A, they coincide: P = U = V, D = Σ.

**"Why is rank-nullity n and not m?"**
T: Fⁿ → Fᵐ has domain of dimension n. The domain splits: rank(A) dimensions go somewhere (column space), nullity(A) dimensions collapse to zero. Together they account for all n input dimensions. The output space Fᵐ is separate — its dimension m doesn't appear in rank-nullity.

**"Hermitian means A = A†. Why does that force real eigenvalues?"**
If Av = λv, take inner product: ⟨v, Av⟩ = λ⟨v,v⟩. Also ⟨v, Av⟩ = ⟨A†v, v⟩ = ⟨Av, v⟩* = (λ⟨v,v⟩)*. So λ‖v‖² = λ*‖v‖², which gives λ = λ* → λ is real. This is why QM observables must be Hermitian: you need real measurement outcomes.

**"Condition number κ(A) = σ₁/σᵣ — what does it mean practically?"**
The condition number measures how much the output can amplify input perturbations. κ = 10⁶ means a 1-part-per-million error in b could become a 100% error in the solution x of Ax = b. "Ill-conditioned" means κ is large. This is why you never invert a matrix numerically if you can avoid it — instead use LU/QR which are backward stable.

---

*Next: `mathematics/07-DIFFEQ.md` — ODEs, PDEs, phase planes, Fourier solutions, and the equations that appear throughout physics.*
