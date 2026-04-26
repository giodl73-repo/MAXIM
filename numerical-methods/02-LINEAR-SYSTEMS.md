# Linear Systems

## The Big Picture

Solving Ax = b is the most common operation in scientific computing. Every PDE solver, least-squares regression, and iterative optimizer reduces to linear solves. The choice between direct and iterative methods depends on problem size and structure.

```
+------------------------------------------------------------------+
|                  LINEAR SYSTEM SOLVER TAXONOMY                   |
+------------------------------------------------------------------+
|                                                                  |
|  DIRECT METHODS                    ITERATIVE METHODS             |
|  (exact up to rounding)            (converge to solution)       |
|  +---------------------+           +-------------------+        |
|  | LU factorization    |           | CG (sym. PD)      |        |
|  | Ax=b, dense         |           | GMRES (general)   |        |
|  | O(n^3) work         |           | BiCGSTAB          |        |
|  | O(n^2) storage      |           | MINRES (sym.)     |        |
|  +---------------------+           | Multigrid         |        |
|  | QR factorization    |           +-------------------+        |
|  | Least squares min   |           | O(n) to O(n^{4/3})         |
|  | ||Ax-b||^2          |           | for sparse A      |        |
|  +---------------------+           +-------------------+        |
|  | Cholesky (sym.PD)   |           PRECONDITIONING:             |
|  | A = LL^T            |           Key to practical speed       |
|  | Half the work of LU |                                        |
|  +---------------------+                                        |
|                                                                 |
|  WHEN DIRECT:          n < 10^4, dense, need exact solution     |
|  WHEN ITERATIVE:       n > 10^4, sparse, structure exploitable  |
+------------------------------------------------------------------+
```

---

## Gaussian Elimination and LU Factorization

**Gaussian elimination** transforms Ax = b into Ux = c (upper triangular) by row operations:

```
  FORWARD ELIMINATION:
  For k = 1 to n-1:
    For i = k+1 to n:
      m_ik = A_{ik} / A_{kk}   (multiplier; A_{kk} = pivot)
      For j = k to n:
        A_{ij} = A_{ij} - m_ik * A_{kj}
      b_i = b_i - m_ik * b_k

  BACK SUBSTITUTION:
  x_n = b_n / A_{nn}
  x_i = (b_i - Sum_{j=i+1}^n A_{ij} x_j) / A_{ii}   for i = n-1 down to 1

  COST: O(n^3) flops (2n^3/3 for elimination + O(n^2) for back substitution)
  STORAGE: O(n^2)
```

**LU factorization** decomposes A = LU (L lower triangular, U upper triangular):

```
  L_{ik} = m_ik (multipliers stored below diagonal of "A")
  U_{kj} = A_{kj} after elimination (upper triangular result)

  SOLVE Ax = b using A = LU:
  Ly = b (forward substitution, O(n^2))
  Ux = y (back substitution, O(n^2))

  ADVANTAGE: Factorize ONCE (O(n^3)), solve MANY times (O(n^2) each).
  For solving with multiple right-hand sides b_1, b_2, ...: one factorization suffices.
```

**Partial pivoting** (essential for stability):

```
  PROBLEM: If A_{kk} is small, the multipliers m_ik = A_{ik}/A_{kk} are large.
  Large multipliers amplify rounding errors. UNSTABLE without pivoting.

  PARTIAL PIVOTING: before elimination step k, find row with largest |A_{ik}| for i >= k.
  Swap that row with row k. Record the permutation.

  PA = LU factorization with permutation matrix P.
  Solve Ax = b: Ly = Pb, then Ux = y.

  STABILITY: Backward stable with partial pivoting (Wilkinson's theorem).
  Grows: |U_{ij}| <= 2^{n-1} |A_{ij}| in worst case (practically never an issue).

  COMPLETE PIVOTING: also permute columns. More expensive, rarely needed.
```

---

## QR Factorization

**QR decomposition**: A = QR where Q is orthogonal (Q^T Q = I) and R is upper triangular.

```
  CONSTRUCTION:
  1. Gram-Schmidt (classical or modified):
     Compute orthonormal basis of col(A) column by column.
     Numerically unstable (classical) or stable (modified Gram-Schmidt).

  2. Householder reflections (preferred):
     Sequence of orthogonal reflections H_1, H_2, ..., H_n:
     H_n ... H_2 H_1 A = R
     Q = H_1 H_2 ... H_n
     Each H_k reflects to zero out below-diagonal entries in column k.
     COST: 2n^3/3 flops (same as LU, but ~2x the constant in practice).
     VERY STABLE: H_k are orthogonal (||H_k x|| = ||x||, no error amplification).

  3. Givens rotations:
     Zero out entries one at a time with 2x2 rotations.
     Useful for structured problems (banded matrices, updating an existing QR).

  APPLICATIONS OF QR:
  - Least squares: min ||Ax - b||^2 with A full column rank
    Qx = b in the subspace of col(Q). Normal equations: A^T A x = A^T b.
    Numerically: R x = Q^T b.  MORE STABLE than computing A^T A explicitly.
  - Eigenvalue computation (QR algorithm, see 03)
  - Rank-revealing factorization (with column pivoting)
```

---

## Cholesky Factorization

For **symmetric positive-definite (SPD)** matrices A, Cholesky is:

```
  A = L L^T   where L is lower triangular with positive diagonal

  COST: n^3/3 flops (half the work of LU)
  STORAGE: n(n+1)/2 (stores only lower triangle)
  STABILITY: Inherently stable for SPD A (no pivoting needed)

  Algorithm:
  For j = 1 to n:
    L_{jj} = sqrt(A_{jj} - Sum_{k=1}^{j-1} L_{jk}^2)
    For i = j+1 to n:
      L_{ij} = (A_{ij} - Sum_{k=1}^{j-1} L_{ik} L_{jk}) / L_{jj}

  BREAKDOWN: L_{jj} = sqrt(negative number) -> A is not positive definite.
  This is a useful test: Cholesky breakdown = matrix is NOT SPD.

  USE CASES:
  - Solving linear systems when A is covariance matrix, FEM stiffness matrix, etc.
  - Computing det(A) = prod(L_{ii})^2  (product of diagonal entries squared)
  - Sampling from multivariate Normal: x = L z where z ~ N(0,I)
  - Kalman filter: Cholesky to update covariance
```

---

## Special Structures

Exploit structure for significant speedups:

```
  BANDED MATRICES: A_{ij} = 0 for |i-j| > b (bandwidth b)
  LU with band structure: O(nb^2) instead of O(n^3).
  Example: FD discretization of 1D ODE is tridiagonal (b=1): O(n).

  SPARSE MATRICES: most entries zero.
  Fill-in during Gaussian elimination: zero entries can become nonzero.
  Reorder rows/columns to minimize fill-in (AMD, METIS, nested dissection).
  n x n sparse matrix from 2D PDE: O(n) nonzeros.
  LU with nested dissection: O(n^{3/2}) flops, O(n log n) storage.

  SYMMETRIC MATRICES: A = A^T.
  Can exploit symmetry in LU (Bunch-Kaufman for indefinite symmetric).
  Cholesky for SPD.

  TOEPLITZ MATRICES: A_{ij} = a_{i-j} (shift-invariant).
  Solve in O(n log^2 n) using FFT-based algorithms.
  Appears in convolution, time series, signal processing.
```

---

## Engineering Bridge: Iterative Solvers as Graph Propagation

```
GRAPH ALGORITHM                  ITERATIVE LINEAR SOLVER
──────────────────────────────────────────────────────────────────────
Adjacency matrix A               Sparse matrix A (same object!)
Node values x                    Solution vector x
Message passing: x ← A x         Matrix-vector product: y = A x
PageRank: x ← α A x + (1-α)e    Power iteration on stochastic A
Label propagation: x ← D⁻¹A x   Jacobi iteration: x ← D⁻¹(b - (A-D)x)
Laplacian flow: L x = b          CG on graph Laplacian (SPD!)
  L = D - A                        Solves network flow / equilibrium
```

For any MIT TCS reader, this is the structural identity: CG on a sparse SPD matrix *is* structured iterative refinement of a flow problem on the corresponding graph. The sparse matrix IS the adjacency/Laplacian matrix; SpMV IS one round of message passing. Multigrid coarsening IS graph coarsening — collapsing clusters of nodes into supernodes, solving the smaller graph, and interpolating back. The algorithms in this module and graph algorithms in TCS are the same algorithms viewed from different traditions.

---

## Iterative Methods for Large Sparse Systems

For n > 10^4 sparse systems, direct methods become impractical. Iterative methods generate a sequence x^{(0)}, x^{(1)}, ... converging to x*.

**Conjugate Gradient (CG)** — for symmetric positive definite A:

```
  ALGORITHM (for A SPD):
  r^{(0)} = b - A x^{(0)};  p^{(0)} = r^{(0)}
  For k = 0, 1, 2, ...:
    alpha_k = ||r^{(k)}||^2 / (p^{(k)^T} A p^{(k)})    (step size)
    x^{(k+1)} = x^{(k)} + alpha_k p^{(k)}               (update solution)
    r^{(k+1)} = r^{(k)} - alpha_k A p^{(k)}             (update residual)
    beta_k = ||r^{(k+1)}||^2 / ||r^{(k)}||^2
    p^{(k+1)} = r^{(k+1)} + beta_k p^{(k)}              (update search direction)

  KEY FACTS:
  - Each iteration requires ONE matrix-vector product Ap (O(nnz) for sparse A)
  - Exact convergence in at most n iterations (exact arithmetic)
  - In practice: convergence in <<n iterations depending on eigenvalue clustering
  - Error bound: ||e^{(k)}|| <= 2 * ((sqrt(kappa) - 1)/(sqrt(kappa) + 1))^k * ||e^{(0)}||
    (kappa = condition number of A)
  - Memory: O(n) (just store a few vectors)

  CONVERGENCE:
  Fast when eigenvalues cluster (small effective condition number).
  Slow when eigenvalues spread widely (large kappa).
  Fix: preconditioning.
```

**GMRES** — for general non-symmetric A:

```
  Generalized Minimum Residual. Minimizes ||r^{(k)}|| over a Krylov subspace.
  Krylov(A, b, k) = span{b, Ab, A^2 b, ..., A^{k-1} b}

  Each iteration: one mat-vec product, store k orthonormal basis vectors.
  Memory grows: O(k n) after k iterations.

  RESTART: GMRES(m) restarts every m iterations to limit memory.
  Breaks the guarantee of monotone decrease; choose m by experiment.

  CONVERGENCE: Depends on eigenvalue distribution of A.
  For normal matrices: reduces to CG in symmetric case.
  For highly non-normal A: convergence can be non-monotone or slow.
```

---

## Preconditioning

Preconditioning transforms the system to improve convergence:

```
  ORIGINAL: Ax = b
  PRECONDITIONED: M^{-1} Ax = M^{-1} b  (left preconditioning)
  Or: AM^{-1} (M x) = b  (right preconditioning)

  IDEAL: M = A  => M^{-1}A = I  (one iteration, but then M = A is the problem)
  PRACTICAL: Choose M that is:
  - A good approximation to A (eigenvalues of M^{-1}A cluster near 1)
  - Cheap to apply (solve My = c in O(n) or O(n log n))

  COMMON PRECONDITIONERS:
  DIAGONAL (Jacobi): M = diag(A). Trivial but often helps.
  SSOR: symmetric SOR. Slightly better.
  INCOMPLETE LU (ILU): LU factorization dropping fill-in beyond a threshold.
  AMG (Algebraic Multigrid): optimal for elliptic PDEs. O(n) per iteration.
  Sparse approximate inverse (SPAI): M^{-1} ≈ A^{-1} in sparse form.
```

**GPU acceleration of iterative solvers**: CG and GMRES are dominated by SpMV — one sparse matrix-vector product per iteration. On GPU, this maps directly:

```
  CG INNER LOOP ON GPU:
  ──────────────────────────────────────────────────────────
  SpMV:  w = A p          cuSPARSE::csrmv (CSR stays on device)
  dot:   r^T r            cuBLAS::ddot
  axpy:  x += α p         cuBLAS::daxpy
  axpy:  r -= α w         cuBLAS::daxpy
  dot:   r_new^T r_new    cuBLAS::ddot
  axpy:  p = r + β p      cuBLAS::daxpy + dscal
  ──────────────────────────────────────────────────────────
  Entire iteration: no CPU-GPU transfer (all vectors on device).
  Speedup: 10-50x for large sparse systems (HBM bandwidth >> DDR5).
  Libraries: NVIDIA AmgX (CG/GMRES + AMG preconditioner on GPU).
```

**Multigrid**: The optimal method for elliptic PDEs (e.g., -nabla^2 u = f):

```
  IDEA: Work with the problem at multiple "levels" (coarse to fine grid).
  Fine grid: resolves high-frequency errors quickly.
  Coarse grid: resolves low-frequency errors cheaply.

  V-CYCLE (two-level):
  1. Pre-smooth: a few iterations of Gauss-Seidel on fine grid (kills high-freq)
  2. Compute residual r = b - Ax
  3. Restrict r to coarse grid: r_H = R r
  4. Solve coarse-grid problem: A_H e_H = r_H  (cheap, 2x fewer unknowns per dimension)
  5. Prolongate correction: e = P e_H
  6. Correct: x <- x + e
  7. Post-smooth: a few iterations of Gauss-Seidel

  COMPLEXITY: O(n) per V-cycle, O(n) total. OPTIMAL.
  Works because: smooth errors look like coarse errors. High-frequency errors
  are killed by local smoothers. This is the "multigrid principle."
```

---

## Condition Number and Backward Stability

```
  CONDITION NUMBER OF A:
  kappa(A) = ||A|| * ||A^{-1}|| = sigma_max / sigma_min  (2-norm condition number)

  For solving Ax = b with LU + partial pivoting:
  Backward error: ||A x_computed - b|| <= eps_mach * ||A|| * ||x_computed||
  Forward error: ||x_computed - x|| / ||x|| <= kappa(A) * eps_mach

  ITERATIVE REFINEMENT:
  After computing x_computed = LU^{-1} b:
  r = b - A x_computed          (residual, computed in higher precision if possible)
  Solve A delta = r             (using stored LU factorization, O(n^2))
  x_better = x_computed + delta
  Repeat: convergence at rate eps_mach * kappa(A)

  Iterative refinement effectively makes LU backward stable even for slightly
  ill-conditioned A (kappa < 1/eps_mach).
```

---

## Decision Cheat Sheet

| Matrix Type | Preferred Method | Cost |
|---|---|---|
| Dense, general | LU with partial pivoting | O(n^3) |
| Dense, SPD | Cholesky | O(n^3/3) |
| Dense, symmetric indefinite | Bunch-Kaufman | O(n^3/3) |
| Dense, overdetermined Ax≈b (least sq.) | QR factorization | O(mn^2) |
| Sparse, SPD, structured (PDE) | Multigrid | O(n) |
| Sparse, SPD, unstructured | CG + AMG preconditioner | O(n log n) typical |
| Sparse, non-symmetric | GMRES + ILU preconditioner | Problem-dependent |
| Tridiagonal / banded | Banded LU | O(nb^2) |
| Toeplitz | FFT-based solver | O(n log^2 n) |

---

## Common Confusion Points

**"Gaussian elimination without pivoting is fine for most matrices."**
It is fine MOST of the time but can be catastrophically unstable for certain inputs. The whole point of partial pivoting is to guarantee backward stability. Always use LU with partial pivoting by default; this is what LAPACK's DGESV does.

**"CG works for any symmetric matrix."**
CG requires A to be symmetric POSITIVE DEFINITE. For symmetric indefinite matrices, use MINRES or GMRES. For non-symmetric, use GMRES or BiCGSTAB. Applying CG to a non-SPD matrix can fail (division by near-zero) or give wrong answers without warning.

**"The residual ||Ax - b|| being small means the solution is accurate."**
Only for well-conditioned A. For ill-conditioned A, you can have ||Ax - b|| = 0 (machine precision) while ||x - x*|| is huge. Always check the condition number and report it alongside the residual.

**"Preconditioning is an optional optimization."**
For poorly-conditioned or large systems, preconditioning is essential. Without a good preconditioner, CG/GMRES may take O(n) iterations (no better than direct methods) or even fail to converge. A good preconditioner can reduce iteration count from O(n) to O(1) (mesh-independent convergence for multigrid on elliptic PDEs).
