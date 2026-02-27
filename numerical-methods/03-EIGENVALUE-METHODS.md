# Eigenvalue Methods

## The Big Picture

Computing eigenvalues and singular values is central to data analysis, stability analysis, and scientific computing. The algorithms are more subtle than linear system solvers because the eigenvalue problem is inherently nonlinear.

```
+------------------------------------------------------------------+
|                   EIGENVALUE ALGORITHM TAXONOMY                  |
+------------------------------------------------------------------+
|                                                                  |
|  FIND ALL EIGENVALUES           FIND FEW EIGENVALUES/VECTORS    |
|  +---------------------+        +------------------------+      |
|  | QR ALGORITHM        |        | POWER ITERATION        |      |
|  | Dense matrices      |        | Largest eigenvalue     |      |
|  | O(n^3) work         |        | O(n k) per iteration   |      |
|  | Industry standard   |        +------------------------+      |
|  | (LAPACK DSYEV/DGEEV)|        | INVERSE ITERATION      |      |
|  +---------------------+        | Smallest eigenvalue    |      |
|                                  +------------------------+      |
|  SVD                            | RAYLEIGH QUOTIENT ITER |      |
|  +---------------------+        | Cubic convergence      |      |
|  | A = U Sigma V^T     |        +------------------------+      |
|  | Generalizes EVD     |        | LANCZOS / ARNOLDI      |      |
|  | Rank, null space,   |        | Sparse large matrices  |      |
|  | pseudoinverse       |        | Basis for ARPACK       |      |
|  +---------------------+        +------------------------+      |
|                                  | RANDOMIZED SVD         |      |
|                                  | Approximate, very fast |      |
|                                  | Foundation of many ML  |      |
|                                  +------------------------+      |
+------------------------------------------------------------------+
```

---

## Power Iteration

**The simplest eigenvalue algorithm**: repeated matrix-vector products.

```
  Given A (n x n), find the dominant eigenvalue (largest |lambda|):

  v^{(0)} = random unit vector
  For k = 0, 1, 2, ...:
    w = A v^{(k)}
    v^{(k+1)} = w / ||w||           (normalize)
    lambda^{(k)} = (v^{(k)})^T A v^{(k)}   (Rayleigh quotient)

  CONVERGENCE: v^{(k)} -> v_1 (dominant eigenvector)
  Rate: |lambda_2 / lambda_1|^k   (ratio of 1st and 2nd largest eigenvalue)

  SLOW if |lambda_2| / |lambda_1| close to 1 (eigenvalues close together).

  INVERSE ITERATION: Apply power iteration to A^{-1} -> finds smallest eigenvalue.
  Solve (A - mu I) v^{(k+1)} = v^{(k)} at each step.
  For mu near lambda_i: converges extremely fast to lambda_i.

  SHIFTED INVERSE ITERATION:
  Apply to (A - mu I)^{-1} with shift mu near target eigenvalue.
  Convergence rate: |(lambda_i - mu)/(lambda_j - mu)| for nearest competitor lambda_j.
  For mu close to lambda_i: this ratio is tiny -> superlinear convergence.
```

**Rayleigh quotient iteration**:

```
  Update shift mu = Rayleigh quotient at each step:
  mu^{(k)} = (v^{(k)})^T A v^{(k)} / (v^{(k)})^T v^{(k)}

  Solve (A - mu^{(k)} I) v^{(k+1)} = v^{(k)}  (shifted system)
  Normalize v^{(k+1)}.

  CONVERGENCE: CUBICALLY convergent once near the eigenvalue.
  (Most algorithms have linear or quadratic convergence. Cubic is rare.)
  Risk: may converge to wrong eigenvalue depending on starting vector.
```

---

## The QR Algorithm (LAPACK Standard)

The **QR iteration** is the standard algorithm for computing all eigenvalues of a dense matrix.

**Basic QR iteration** (conceptual):

```
  A_0 = A
  For k = 0, 1, 2, ...:
    A_k = Q_k R_k    (QR factorization)
    A_{k+1} = R_k Q_k   (reverse order)

  Remarkable fact: A_k -> upper triangular (Schur form) for generic A.
  Eigenvalues appear on the diagonal of the limiting triangular matrix.
  Converges at rate |lambda_{i+1}/lambda_i|^k (slow without shifts).
```

**Practical QR algorithm with shifts**:

```
  1. REDUCTION TO HESSENBERG:
     H = Q^T A Q  (Q orthogonal, H upper Hessenberg: zero below first subdiagonal)
     Cost: O(n^3) one-time cost. Subsequent QR steps cost O(n^2) each.

  2. SHIFTED QR ON HESSENBERG:
     mu = estimated eigenvalue (Wilkinson shift: eigenvalue of bottom-right 2x2)
     H_k - mu I = Q_k R_k
     H_{k+1} = R_k Q_k + mu I

     Convergence: essentially cubic near eigenvalues.

  3. DEFLATION:
     Once a subdiagonal entry of H becomes small (< eps_mach * ||H||):
     the problem deflates into independent sub-problems.
     Repeat on each sub-problem.

  TOTAL COST: O(n^3) for all n eigenvalues.
  LAPACK: DGEEV (general), DSYEV (symmetric), DSYEVD (divide-and-conquer, faster).
```

---

## SVD: The Most Useful Matrix Decomposition

**Singular Value Decomposition**: Every m x n matrix A can be written as:

```
  A = U Sigma V^T

  U: m x m orthogonal (left singular vectors, columns = u_i)
  V: n x n orthogonal (right singular vectors, columns = v_i)
  Sigma: m x n diagonal (singular values sigma_1 >= sigma_2 >= ... >= 0)

  ECONOMY SVD (thin SVD): if m > n, keep only first n columns of U:
  A = U_n Sigma_n V^T  (U_n: m x n, Sigma_n: n x n, V: n x n)

  KEY FACTS:
  sigma_i = sqrt(eigenvalues of A^T A) = sqrt(eigenvalues of AA^T)
  u_i = eigenvectors of AA^T
  v_i = eigenvectors of A^T A
  rank(A) = number of nonzero singular values

  APPLICATIONS:
  Pseudoinverse: A^+ = V Sigma^+ U^T  (Sigma^+: invert nonzero sigmas)
  Best rank-k approximation: A_k = Sum_{i=1}^k sigma_i u_i v_i^T  (Eckart-Young theorem)
  Principal directions: v_1, ..., v_k (= PCA directions)
  Null space of A: span of v_{r+1}, ..., v_n  (r = rank(A))
  Range of A: span of u_1, ..., u_r
```

**Computing the SVD**:

```
  DENSE MATRICES (LAPACK DGESVD):
  1. Bidiagonalize A: A = U_1 B V_1^T  (B bidiagonal, O(mn^2) work)
  2. Apply QR algorithm to B -> singular values
  3. Total: O(mn^2) for m >= n.

  DIVIDE-AND-CONQUER (DGESDD): faster in practice, O(mn^2) but smaller constant.
```

---

## Lanczos Algorithm (Sparse, Large Matrices)

For a large sparse symmetric matrix A (n x n, n >> 10^3), computing ALL eigenvalues is infeasible. Lanczos finds the k largest (or smallest) eigenvalues and eigenvectors.

```
  LANCZOS ITERATION:
  Start with random unit vector v_1.
  For j = 1, 2, ..., k:
    w = A v_j
    alpha_j = v_j^T w
    w = w - alpha_j v_j - beta_{j-1} v_{j-1}   (orthogonalize)
    beta_j = ||w||
    v_{j+1} = w / beta_j

  After k steps: have tridiagonal matrix T_k = V_k^T A V_k
  where V_k = [v_1, ..., v_k] (nearly orthonormal, ~O(k n) storage).

  EIGENVALUES: compute eigenvalues of T_k (trivial, T_k is k x k tridiagonal).
  These are the "Ritz values" -- approximations to extreme eigenvalues of A.

  CONVERGENCE: Extreme eigenvalues converge first, fastest.
  After ~10 iterations: good approximations to a few extreme eigenvalues.
  Basis for ARPACK (which is what scipy.sparse.linalg.eigsh calls).

  GHOSTING: Finite precision causes loss of orthogonality.
  Spurious eigenvalues ("ghosts") appear.
  Fix: Full reorthogonalization (expensive) or partial reorthogonalization.
```

**Arnoldi iteration** extends Lanczos to non-symmetric matrices. Arnoldi = Lanczos for general A. GMRES (from 02) is derived from Arnoldi.

---

## Randomized SVD

For very large matrices (n, m > 10^5) where even O(mn) work is expensive:

```
  RANDOMIZED RANGE FINDER:
  1. Draw Omega: n x k random Gaussian matrix (k << n)
  2. Compute Y = A Omega  (m x k matrix)
  3. Y approximately spans the range of A (for rank-k approximation)

  RANDOMIZED SVD (Halko-Martinsson-Tropp 2011):
  1. Omega = randn(n, k+p)  (k = target rank, p = oversampling, typically p=5-10)
  2. Y = A Omega
  3. [Q, ~] = qr(Y)  (Q: m x (k+p) orthonormal)
  4. B = Q^T A  ((k+p) x n)
  5. [U_B, Sigma, V] = svd(B)  (small SVD: (k+p) x n)
  6. U = Q U_B

  TOTAL COST: O(mn k) instead of O(mn min(m,n)).
  For k << min(m,n): MASSIVE speedup.

  ACCURACY: With high probability:
  ||A - U Sigma V^T|| <= (1 + eps) * sigma_{k+1}
  (near-optimal for the target rank; oversampling p handles the probability guarantee)

  POWER ITERATION VARIANT: Use Y = (AA^T)^q A Omega to improve accuracy for slowly
  decaying singular values. q=2 usually sufficient.

  In scikit-learn: TruncatedSVD uses randomized SVD.
  PCA of large matrices: LinearSVC, text TF-IDF matrices, etc.
```

---

<!-- @editor[content/P2]: Randomized SVD section mentions power iteration variant but does not cover the sketching framework (Johnson-Lindenstrauss, CountSketch, leverage score sampling) that underlies randomized linear algebra more broadly. The learner calibration explicitly calls out "sketching" as a needed topic. A paragraph connecting RandSVD's random projection Omega to the JL lemma and to streaming/one-pass sketching algorithms would fill this gap. -->

## Generalized Eigenvalue Problems

Many physical problems lead to generalized eigenvalue problems:

```
  Av = lambda Bv   (standard: Av = lambda v is B = I case)

  Where A and B are symmetric, B is positive definite.

  Reduction to standard: B = L L^T (Cholesky), then
  L^{-1} A L^{-T} y = lambda y  where v = L^{-T} y

  APPLICATIONS:
  Structural vibration: K u = omega^2 M u (stiffness, mass matrices)
  Fisher's linear discriminant: S_W^{-1} S_B v = lambda v
  Graph Laplacian eigenvectors: L v = lambda D v
  PCA with non-standard metric
```

---

## Symmetric vs. Non-Symmetric Eigenvalue Problems

```
  SYMMETRIC MATRIX (A = A^T):
  All eigenvalues REAL.
  Eigenvectors orthogonal.
  Numerically well-conditioned (eigenvalues are normal; no ill-conditioning
  from clustering that doesn't physically cross).
  Algorithm: QR with Wilkinson shifts on tridiagonalized A. Very stable.

  NON-SYMMETRIC MATRIX:
  Complex eigenvalues possible (appear in conjugate pairs for real A).
  Schur decomposition: A = Q T Q^T where T is quasi-upper-triangular
  (2x2 diagonal blocks for complex conjugate pairs).
  Eigenvectors can be nearly parallel -> ill-conditioned.
  Eigenvalue sensitivity: kappa_i = 1/|l_i^T r_i| where l_i, r_i are
  left/right eigenvectors. Can be huge for near-defective matrices.
  Algorithm: QR with Francis double-shift (handles complex pairs on real arithmetic).
```

---

<!-- @editor[bridge/P2]: No GPU-accelerated eigenvalue/SVD callout. cuSOLVER has cusolverDn*gesvd for dense SVD and cusolverSp* for sparse eigenvalue problems. For the randomized SVD, the random projection Y = A*Omega is a dense matrix multiply — pure cuBLAS DGEMM — making it naturally GPU-accelerated. A table showing "Algorithm → GPU library → when GPU wins" would be the practical bridge the learner needs. -->

## Singular Value Decomposition in ML Context

SVD is central to both the theory and practice of ML:

```
  PCA: principal components = right singular vectors v_i of centered data matrix X.
  principal values = sigma_i^2 / (n-1) = variances.

  LATENT SEMANTIC ANALYSIS: SVD of term-document matrix. Left/right singular vectors
  = semantic dimensions.

  MATRIX COMPLETION (Netflix problem): observed entries of A ≈ low-rank U Sigma V^T.
  ALS (Alternating Least Squares): alternately fix U, solve for V, fix V, solve for U.
  Nuclear norm minimization: convex relaxation of rank, uses SVD in each step.

  ATTENTION IN TRANSFORMERS: Attention(Q,K,V) = softmax(QK^T/sqrt(d)) V.
  The QK^T matrix has effective rank << d for trained models.
  Low-rank approximation of attention matrices (LoRA) for efficient fine-tuning.

  CONDITION NUMBER AND NEURAL NETWORKS:
  Singular values of weight matrices determine gradient flow.
  Near-zero singular values: vanishing gradients.
  Very large singular values: exploding gradients.
  Spectral normalization: normalize W by sigma_max(W) to control Lipschitz constant.
```

---

## Decision Cheat Sheet

| Problem | Algorithm | Complexity | Notes |
|---|---|---|---|
| All eigenvalues, dense symmetric | QR algorithm (DSYEV) | O(n^3) | Stable, complete |
| All eigenvalues, dense general | QR algorithm (DGEEV) | O(n^3) | Complex eigenvalues |
| Full SVD, dense | DGESVD / DGESDD | O(mn^2) | m >= n |
| k largest eigenvalues, sparse | Lanczos (ARPACK) | O(k * nnz) | Reorthogonalize |
| k largest singular values, large A | Randomized SVD | O(mnk) | Near-optimal |
| Single largest eigenvalue | Power iteration | O(nnz) per iter | Simple, slow convergence |
| Eigenvalue near target mu | Shifted inverse iteration | O(n^2-3) per iter | Cubic convergence |
| Generalized A v = lambda B v | Cholesky reduce + QR | O(n^3) | B must be SPD |

---

## Common Confusion Points

**"The eigenvalues of A are the eigenvalues of A^T A."**
The SQUARED SINGULAR VALUES of A are the eigenvalues of A^T A (which are non-negative). The eigenvalues of A are different things for non-symmetric A. For symmetric A = A^T: singular values = |eigenvalues| and left singular vectors = right singular vectors = eigenvectors.

**"SVD and eigendecomposition are the same thing."**
For symmetric A: eigendecomposition A = Q Lambda Q^T is a special case of SVD with U = V = Q and sigma_i = |lambda_i|. For non-symmetric A: SVD always exists with real non-negative sigma_i; eigendecomposition may not exist (defective matrices) or requires complex arithmetic.

**"Power iteration is too slow for practical use."**
Correct for finding all eigenvalues. But for the dominant eigenvector of a large sparse matrix (e.g., PageRank computation), power iteration is the right tool — it costs O(nnz) per iteration and Google's original PageRank was essentially power iteration on the web graph adjacency matrix.

**"Randomized SVD gives an approximate answer — is it trustworthy?"**
Yes, with quantifiable error bounds. The error is at most (1 + eps) * sigma_{k+1} with high probability — the smallest retained singular value times a small constant. For matrices with rapidly decaying singular values (low-rank structure), the approximation is essentially exact. The oversampling parameter p=10 makes failure probability negligible.
