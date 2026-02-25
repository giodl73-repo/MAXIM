# Scientific Computing Ecosystem

## The Big Picture

Scientific computing is the software layer that makes the algorithms from modules 01-08 run efficiently on real hardware. The central insight: raw Python/MATLAB code hits a performance wall; the ecosystem routes compute to hand-tuned FORTRAN/C kernels from the 1970s that are still unbeaten on modern CPUs.

```
+------------------------------------------------------------------+
|              SCIENTIFIC COMPUTING STACK                          |
+------------------------------------------------------------------+
|                                                                  |
|  HIGH-LEVEL APIs            (NumPy / SciPy / Julia / MATLAB)   |
|  +-------------------------------------------------------------+ |
|  | Array notation, broadcasting, high-level routines           | |
|  | Python: numpy.linalg.solve() -> calls LAPACK dgesv          | |
|  | Julia:  A \ b             -> calls LAPACK dgesv              | |
|  +-------------------------------------------------------------+ |
|                          |                                       |
|  LAPACK                  | (Linear Algebra PACKage)             |
|  +-------------------------------------------------------------+ |
|  | Dense: LU/QR/Cholesky/SVD/eigenvalue — module 02/03        | |
|  | Drivers (simple/expert), computational routines, auxiliary  | |
|  +-------------------------------------------------------------+ |
|                          |                                       |
|  BLAS                    | (Basic Linear Algebra Subprograms)   |
|  +-------------------------------------------------------------+ |
|  | Level 1: vector ops  (O(n))    dot, axpy, nrm2, scal        | |
|  | Level 2: matrix-vec  (O(n^2))  gemv, trmv, ger              | |
|  | Level 3: matrix-mat  (O(n^3))  gemm, trsm, syrk             | |
|  +-------------------------------------------------------------+ |
|                          |                                       |
|  VENDOR BLAS             | (architecture-specific tuning)       |
|  +---------------------+ | +----------------------------------+  |
|  | Intel MKL            | | | OpenBLAS (open-source)          |  |
|  | (AVX-512, cache opt) | | | (multi-platform, near-MKL)      |  |
|  +---------------------+ | +----------------------------------+  |
|                          |                                       |
|  HARDWARE                                                        |
|  CPU (SIMD) ---- GPU (cuBLAS/cuSPARSE/cuSOLVER) ---- TPU       |
+------------------------------------------------------------------+

SPARSE LAYER (runs alongside dense):
  SciPy sparse / Eigen / CHOLMOD / SuperLU / UMFPACK / PARDISO
  Format: CSR / CSC / COO / BSR / DIA / LIL
  For large FEM/graph systems: millions of unknowns, 99.9% zeros

DISTRIBUTED LAYER (multiple nodes):
  ScaLAPACK -> PBLAS -> MPI
  PETSc / Trilinos / Elemental -> Azure HPC / Slurm clusters
```

---

## BLAS: Levels 1, 2, 3

BLAS is the bedrock. Everything else calls BLAS. The level taxonomy maps to computation-to-memory ratios:

```
  LEVEL 1 — O(n) flops, O(n) memory:
  DDOT:  dot(x, y) = Sum x_i y_i           (inner product)
  DAXPY: y = alpha*x + y                   (a*x + y, the workhorse)
  DNRM2: ||x||_2                           (Euclidean norm)
  DSCAL: x = alpha*x                       (scale a vector)
  DSWAP: swap vectors                      (in-place)
  DCOPY: y = x                             (vector copy)

  Arithmetic intensity: 2 flops / 2 reads (or similar).
  MEMORY-BANDWIDTH BOUND on modern hardware (CPU spends time
  waiting for data from DRAM, not on arithmetic).

  LEVEL 2 — O(n^2) flops, O(n^2) memory:
  DGEMV: y = alpha*A*x + beta*y            (matrix-vector product)
  DSYMV: symmetric matrix-vector
  DTRMV: triangular matrix-vector
  DGER:  A = alpha*x*y^T + A               (rank-1 update)
  DTRSV: solve triangular system           (back-sub kernel)

  Arithmetic intensity: O(n^2 flops) / O(n^2 reads) = O(1).
  ALSO memory-bandwidth bound. Hard to speed up significantly.

  LEVEL 3 — O(n^3) flops, O(n^2) memory:
  DGEMM: C = alpha*A*B + beta*C            (THE critical operation)
  DSYRK: C = alpha*A*A^T + beta*C          (symmetric rank-k update)
  DTRSM: solve A*X = B with triangular A   (batch triangular solve)
  DSYMM: C = alpha*A*B for symmetric A

  Arithmetic intensity: O(n^3 flops) / O(n^2 reads) = O(n).
  COMPUTE-BOUND. Vendor BLAS achieves >90% of peak FLOPS via:
  - Loop blocking (tiling) to fit cache
  - SIMD vectorization (AVX-512: 8 doubles/cycle)
  - Pipelining and instruction reordering

WHY DGEMM IS SPECIAL:
  A 1000x1000 DGEMM:
  - 2 * 10^9 FLOPs
  - 2 * 8 * 10^6 bytes memory (A, B, C each 8MB)
  - Arithmetic intensity = 125 flops/byte -> compute-limited
  - Intel MKL achieves ~90% of theoretical peak (~1 TFLOP on single core * 8 AVX-512)

  This is why numpy.dot(A, B) for large matrices is fast even in Python:
  Python overhead is negligible; the work is 100% in DGEMM.

TYPE VARIANTS (BLAS naming: type prefix + name):
  D = double (float64)   S = single (float32)
  Z = complex128         C = complex64
  DGEMM vs. SGEMM: single-precision 2x throughput + half memory bandwidth.
  ML uses SGEMM/half-precision GEMM for training (module 01 mixed precision).
```

---

## LAPACK: Dense Linear Algebra

LAPACK sits above BLAS. Factorizations, eigenvalue problems, least squares — all from modules 02 and 03.

```
NAMING CONVENTION:
  xYYZZZ where:
  x    = type (S/D/C/Z)
  YY   = matrix type (GE=general, SY=symmetric, PO=SPD, HE=Hermitian,
                      TR=triangular, OR=orthogonal, UN=unitary, BN=banded,
                      GB=general banded, TB=triangular banded, ...)
  ZZZ  = operation

DRIVER ROUTINES (simple, one-stop):
  DGESV:  general linear solve   A x = b  (LU with pivoting)
  DGELS:  least squares          min ||Ax-b||_2  (QR)
  DSYSV:  symmetric indefinite   Ax = b  (LDLT)
  DPOSV:  symmetric pos def      Ax = b  (Cholesky)
  DGESVD: full SVD               A = U Sigma V^T
  DSYEV:  symmetric eigenproblem Ax = lambda x
  DGEEV:  non-symmetric eigenval Ax = lambda x
  DGELS + DGGLSE: constrained least squares

COMPUTATIONAL ROUTINES (building blocks):
  DGETRF: LU factorization  (Gaussian elimination + partial pivoting)
  DGETRS: triangular solve  (forward/back substitution using LU)
  DGEQRF: QR factorization  (Householder reflections)
  DORMQR: apply Q from QR   (apply Householder reflections to B)
  DPOTRF: Cholesky           (for SPD matrices)
  DGEHRD: reduce to Hessenberg  (for eigenvalue computation)
  DHSEQR: Schur decomposition from Hessenberg

WORKSPACE PATTERN:
  LAPACK routines require a workspace array WORK.
  Two-phase call:
  1. Query: call with LWORK=-1, WORK(1) returns optimal size.
  2. Allocate: allocate WORK(LWORK).
  3. Compute: call with actual LWORK.
  Modern wrappers (NumPy/SciPy) handle this automatically.

LAPACK ERROR HANDLING:
  INFO parameter: 0 = success, < 0 = bad argument, > 0 = algorithm failure.
  DGESV: INFO = k > 0 means U(k,k) = 0 -> singular matrix.
  NumPy: raises LinAlgError("Singular matrix") if INFO != 0.

SCIPY INTERFACE:
  scipy.linalg.solve(A, b)          -> DGESV
  scipy.linalg.lstsq(A, b)          -> DGELSD (divide-and-conquer SVD)
  scipy.linalg.lu(A)                 -> DGETRF
  scipy.linalg.cholesky(A)           -> DPOTRF
  scipy.linalg.svd(A)               -> DGESVD or DGESDD
  scipy.linalg.eigh(A)               -> DSYEVD (symmetric, divide-and-conquer)
  scipy.linalg.eig(A)               -> DGEEV (non-symmetric, Schur)

  scipy.linalg vs. numpy.linalg:
  scipy.linalg: more options, can access LAPACK routines directly.
  numpy.linalg: cleaner interface, slightly less feature-complete.
  For performance-critical code: scipy.linalg.get_lapack_funcs() -> direct LAPACK call.
```

---

## ScaLAPACK: Distributed Dense Linear Algebra

When the matrix doesn't fit on one node — HPC clusters, Azure HPC:

```
+----------------------------------------------+
|         SCALAPACK ARCHITECTURE               |
+----------------------------------------------+
|                                              |
|  ScaLAPACK  (distributed dense linear alg)  |
|       |                                      |
|  PBLAS  (parallel BLAS — collective ops)     |
|       |                                      |
|  BLACS  (Basic Linear Algebra Comm. Subprog) |
|  (message-passing layer — wraps MPI)         |
|       |                                      |
|  MPI   (Message Passing Interface)           |
|  (typically OpenMPI or IntelMPI)             |
|       |                                      |
|  Network: InfiniBand / Azure RDMA            |
+----------------------------------------------+

BLOCK-CYCLIC DISTRIBUTION:
  Matrix distributed across P x Q process grid.
  Rows partitioned into blocks of size MB, distributed cyclically.
  Columns partitioned into blocks of size NB, distributed cyclically.

  WHY CYCLIC? Load balance: if row 1 is dense (expensive), row 2 is cheap,
  cyclic ensures each process gets both expensive and cheap rows.
  Block structure: large blocks = better DGEMM efficiency.

  Example: 1000x1000 matrix, 2x2 process grid, MB=NB=64:
  Process (0,0): rows {1-64, 129-192, ...} x cols {1-64, 129-192, ...}
  Process (0,1): rows {1-64, 129-192, ...} x cols {65-128, 193-256, ...}
  etc.

SCALAPACK ROUTINES:
  PDGESV:  distributed LU solve
  PDGELS:  distributed least squares
  PDSYEV:  distributed symmetric eigenproblem
  PDGESVD: distributed SVD (less common in practice — communication-heavy)

COMMUNICATION COSTS:
  LU factorization O(n^3/P) computation, O(n^2) communication.
  Scalability: near-linear in P for large n; communication dominates for small n.

ALTERNATIVES TO ScaLAPACK:
  Elemental (better algorithm choices), SLATE (GPU-aware, replaces ScaLAPACK),
  PETSc (sparse+iterative, much more used than ScaLAPACK in practice).

AZURE HPC CONNECTION:
  Azure HBv3/HC VMs with InfiniBand + MPI for PBLAS communication.
  Azure Batch + MPI job submission = your VSTS/ADF pipeline equivalent.
  HPC Pack (familiar name if you know Azure services) -> Azure CycleCloud now.
```

---

## Sparse Matrix Formats

Most large-scale scientific problems (FEM, graph problems, PDEs) have sparse matrices: N = 10^6 unknowns but only O(N) nonzeros.

```
DENSE vs. SPARSE:
  1000x1000 Laplacian (FEM, ~5 nonzeros/row):
  Dense storage:  8 MB, O(N^3) solve.
  Sparse storage: 40 KB, O(N) solve (multigrid) or O(N^1.5) (sparse Cholesky).

STORAGE FORMATS:

COO (Coordinate / Triplet) — easiest to build:
  Store list of (row, col, value) triples.
  row_idx = [0, 0, 1, 1, 2]
  col_idx = [0, 1, 0, 1, 2]
  values  = [2,-1,-1, 2, 1]

  Simple construction (just append triples).
  Inefficient for matrix-vector product.
  Use: initial construction, format conversion.
  scipy.sparse: coo_matrix((data, (row, col)), shape=(m,n))

CSR (Compressed Sparse Row) — standard for computation:
  indptr:  length n+1, indptr[i] = start of row i in data array
  indices: column indices of nonzeros (sorted within each row)
  data:    nonzero values

  Example above as CSR:
  indptr  = [0, 2, 4, 5]    (row 0: entries 0-1, row 1: entries 2-3, row 2: entry 4)
  indices = [0, 1, 0, 1, 2]
  data    = [2,-1,-1, 2, 1]

  SPMV (sparse matrix-vector multiply):
  for i in range(n):
    for j in indptr[i]:indptr[i+1]:
      y[i] += data[j] * x[indices[j]]

  O(nnz) time, cache-friendly (sequential access to data[]).
  Standard for iterative solvers (CG uses SPMV at each step).
  scipy.sparse: csr_matrix

CSC (Compressed Sparse Column) — transpose of CSR:
  Same structure but column-compressed.
  Efficient for column slicing, least squares via column operations.
  scipy.sparse: csc_matrix
  SuiteSparse (CHOLMOD, UMFPACK): prefer CSC.

BSR (Block Sparse Row) — for block-structured systems:
  Blocks of size (r x c) treated as atomic units.
  For FEM with DOF per node: blocks = local stiffness contributions.
  Better DGEMM efficiency per block (use BLAS Level 3).
  scipy.sparse: bsr_matrix

DIA (Diagonal) — for banded/stencil matrices:
  Stores diagonals explicitly.
  Tridiagonal: 3 diagonals.
  5-point Laplacian: 5 diagonals.
  Very fast SPMV when matrix is banded.
  scipy.sparse: dia_matrix

LIL (List of Lists) — for incremental construction:
  Row-wise linked list of (col, value) pairs.
  Efficient random insertion: A[i,j] = val is O(1) amortized.
  Slow SPMV.
  Pattern: build in LIL, convert to CSR for computation.
  scipy.sparse: lil_matrix

CONVERSION COSTS (important for workflow):
  LIL -> CSR: O(nnz log nnz) — sort within rows.
  COO -> CSR: O(nnz + n) — count sort.
  CSR -> CSC: O(nnz + n) — transpose.

SPARSE DIRECT SOLVERS (for moderate n, say n < 10^6):
  CHOLMOD: Cholesky for SPD (fill-reducing reordering + supernodal Cholesky).
  UMFPACK: LU for non-symmetric.
  SuperLU: LU for general (multifrontal algorithm).
  PARDISO: Intel's direct solver (often fastest on Intel hardware).

  Key concept: FILL-IN — LU of sparse matrix is denser than the matrix.
  Reordering (AMD, METIS, SCOTCH) permutes rows/cols to minimize fill-in.
  Without reordering: O(n^2) fill-in for 2D FEM, O(n^3) work.
  With nested dissection (METIS): O(n^{3/2}) fill-in for 2D FEM, O(n^{3/2}) work.

scipy.sparse.linalg:
  spsolve(A, b)       -> UMFPACK or SuperLU (direct)
  splu(A)             -> LU factorization (use for multiple RHS)
  cg(A, b)            -> Conjugate Gradient (for SPD, module 02)
  gmres(A, b)         -> GMRES (module 02)
  eigsh(A, k)         -> ARPACK (Lanczos, module 03)
  LinearOperator      -> matrix-free interface (only need A*x)
```

---

## GPU Computing for Linear Algebra

GPUs have 10-100x the peak FLOP rate of CPUs for matrix operations, but with different programming constraints:

```
+--------------------------------------------------+
|         GPU MEMORY HIERARCHY                     |
+--------------------------------------------------+
| Host (CPU) RAM    <--- PCIe ----> Device (GPU) RAM|
|    DDR5: ~80 GB/s              HBM3: ~3,000 GB/s |
|    ~1 TB capacity              ~80 GB capacity   |
+--------------------------------------------------+

KEY INSIGHT: PCIe transfer (12-64 GB/s) is the bottleneck.
  - Small matrix: CPU wins (data transfer dominates)
  - Large matrix: GPU wins (arithmetic dominates, HBM bandwidth huge)

CROSSOVER POINT (approximate, RTX 4090):
  Dense GEMM:    n > 1000 -> GPU wins
  Batch GEMM:    many small (~32x32) GEMMs -> GPU wins (high parallelism)
  SpMV:          GPU often wins even at moderate size (HBM bandwidth)

NVIDIA COMPUTE LIBRARIES:
  cuBLAS:    GPU BLAS (DGEMM/SGEMM/etc. on GPU)
  cuSPARSE:  Sparse matrix operations (SpMV, SpMM, SpSV)
  cuSOLVER:  LAPACK equivalent (LU/QR/Cholesky/SVD/eigenvalues)
  cuFFT:     FFT (used by spectral methods and signal processing)
  CUTLASS:   Templates for custom GEMM kernels (fine-grained control)

HALF-PRECISION TENSOR CORES (Ampere/Hopper):
  A100 Tensor Cores: 312 TFLOPS FP16 vs 19.5 TFLOPS FP64.
  16x speedup for FP16 vs FP64!
  Used for ML training (module 01 mixed precision / module 08 Adam).
  CUBLAS_COMPUTE_16F: use Tensor Cores.
  BFLOAT16: 8-bit exponent (same range as FP32), 7-bit mantissa (same as FP16).
    Preferred over FP16 for ML (better dynamic range, same throughput).

PYTHON-GPU WORKFLOW:
  CuPy:    NumPy-compatible API running on GPU.
           import cupy as cp; A = cp.array(A_np); cp.linalg.solve(A, b)
           -> calls cuSOLVER internally.
  PyTorch: Primary ML library, also usable for general GPU linear algebra.
           torch.linalg.solve(A, b)  -> cuSOLVER
  JAX:     NumPy-compatible, supports CPU/GPU/TPU with same code.
           jnp.linalg.solve(A, b)  -> XLA-compiled (GPU or TPU)
  RAPIDS cuML: SciPy equivalent for GPU (scikit-learn API, GPU backend).

MEMORY MANAGEMENT:
  Transfer bottleneck: always minimize CPU-GPU transfers.
  Fused kernels: do multiple operations in one GPU pass.
    Example: instead of (1) compute A*b, (2) compute norm:
    Fuse into one kernel that computes and reduces in shared memory.
  Pinned memory: locks CPU RAM page, enables async DMA transfers.
    torch.Tensor.pin_memory() / cudaMallocHost.
  Streams: multiple GPU operations in parallel (if independent).

ROOFLINE MODEL:
  Peak performance = min(Peak FLOP/s, BW * Arithmetic intensity)

  DGEMM (arithmetic intensity O(n)): compute-bound -> scales with FLOP/s.
  SpMV  (arithmetic intensity ~1):  memory-bound -> scales with HBM BW.

  GPU wins because:
  - Higher FLOP/s (for compute-bound)
  - Higher memory bandwidth (for bandwidth-bound), especially HBM vs. DDR5.
```

---

## NumPy: The Foundation

NumPy is the universal data container and array computation layer for scientific Python:

```
CORE CONCEPT: NDARRAY
  n-dimensional array with:
  - dtype: element type (float64, float32, int32, bool, complex128, ...)
  - shape: tuple of dimensions (e.g., (100, 200, 3))
  - strides: bytes between successive elements in each dimension
    Strides are the key to zero-copy views.

STRIDES AND VIEWS (critical for performance):
  A = np.array([[1,2,3],[4,5,6]])   # shape (2,3), strides (24, 8) bytes (C order)
  B = A.T                            # shape (3,2), strides (8, 24) — NO COPY!
  C = A[0, :]                        # shape (3,), strides (8,) — NO COPY!
  D = A[::2, :]                      # strided view — NO COPY!
  E = np.ascontiguousarray(D)       # force copy if non-contiguous needed

  Non-contiguous arrays: some LAPACK/BLAS calls require contiguous.
  np.ascontiguousarray() / np.copy() force a contiguous copy.

BROADCASTING RULES:
  NumPy aligns shapes from the right:
  (3, 4) + (4,)   -> OK: (4,) broadcast to (3, 4)
  (3, 1) + (1, 4) -> OK: result is (3, 4)
  (3, 4) + (3,)   -> FAILS: (3,) would need to broadcast along axis 1, not aligned

  Broadcasting avoids Python loops; the loop runs in C.
  Rule: size 1 dimensions can be broadcast to match any size.

VECTORIZATION PRINCIPLE:
  Slow: for i in range(n): c[i] = a[i] + b[i]   (Python loop, ~50ns/iteration)
  Fast: c = a + b                                  (NumPy ufunc, ~0.5ns/element)

  100x speedup just from eliminating the Python loop overhead.
  Further speedup from SIMD (ufuncs use AVX-512 when available).

KEY NUMPY FUNCTIONS:
  np.dot(A, B)         -> BLAS DGEMM or DDOT
  np.linalg.solve(A,b) -> LAPACK DGESV
  np.linalg.svd(A)     -> LAPACK DGESDD (divide-and-conquer)
  np.linalg.eigh(A)    -> LAPACK DSYEVD (symmetric)
  np.fft.fft(x)        -> FFTPACK or FFTW
  np.random.randn(n,n) -> PRNG (Mersenne Twister by default)

  np.einsum('ij,jk->ik', A, B) -> GEMM (with contraction specification)
  np.einsum is powerful for batched operations:
  np.einsum('bij,bjk->bik', A, B)  # batched GEMM: shape (batch, m, n) x (batch, n, k)

MEMORY LAYOUT (C vs. Fortran order):
  C order (row-major, default): A[i,j] = A.flat[i*n + j]
    Row-by-row in memory. Cache-friendly for row operations.
  F order (column-major): A[i,j] = A.flat[j*m + i]
    Column-by-column. LAPACK expects Fortran order!

  NumPy passes arrays to LAPACK by silently transposing if needed.
  For performance-critical code: use np.asfortranarray() for matrices
  that will be passed to LAPACK many times.
```

---

## SciPy: The Algorithm Library

SciPy provides high-level wrappers around BLAS/LAPACK/FFTW, plus implementations of the algorithms in modules 04-08:

```
scipy.linalg       — Dense linear algebra (LAPACK wrappers)
scipy.sparse       — Sparse matrices (CSR/CSC/COO/etc.)
scipy.sparse.linalg — Sparse solvers (CG/GMRES/ARPACK/direct)
scipy.optimize     — Optimization (module 08: L-BFGS-B, trust-constr, etc.)
scipy.integrate    — Numerical integration (module 05: quad, solve_ivp, etc.)
scipy.interpolate  — Interpolation (module 04: splines, RBF)
scipy.fft          — FFT (FFTW-backed, faster than numpy.fft)
scipy.stats        — Statistical distributions and tests (probability-statistics/)
scipy.signal       — Signal processing (filter design, convolution, spectrograms)
scipy.spatial      — KD-trees, Delaunay, Voronoi, distance metrics

KEY SCIPY INTEGRATION PATTERNS:

solve_ivp (module 06):
  result = solve_ivp(fun, t_span, y0, method='RK45', rtol=1e-6, atol=1e-9)
  method options: 'RK45' (default), 'RK23', 'DOP853', 'Radau', 'BDF', 'LSODA'
  dense_output=True: get a callable interpolant (not just grid values)
  events: stop when f(t, y) = 0 (zero-crossing detection)

minimize (module 08):
  result = minimize(fun, x0, jac=grad, method='L-BFGS-B', bounds=bounds)
  methods: 'L-BFGS-B', 'SLSQP', 'trust-constr', 'Nelder-Mead', 'BFGS'
  scipy.optimize.minimize_scalar: 1D minimization (Brent's method)
  scipy.optimize.linprog: LP solver (HiGHS backend since 1.6)

quad (module 05):
  result, error = quad(f, a, b)              # adaptive Gauss-Kronrod
  result = dblquad(f, a, b, gfun, hfun)      # 2D integration
  result = nquad(f, ranges)                   # n-D integration (slow for high-d)

FFTW BACKEND:
  scipy.fft uses FFTW (Fastest Fourier Transform in the West) when available.
  scipy.fft.set_backend('pyfftw') -> enables multi-threaded FFTW.
  pyfftw.interfaces.numpy_fft as np_fft: drop-in fast FFT.
  FFTW is ~2-4x faster than NumPy's default FFT for large transforms.

PERFORMANCE TIPS:
  Use scipy.linalg.solve(A, b, assume_a='pos') for SPD: calls DPOSV (Cholesky).
  Use scipy.linalg.solve_triangular() for triangular: calls DTRTRS directly.
  For repeated solves with same A: lu = scipy.linalg.lu_factor(A); solve = scipy.linalg.lu_solve(lu, b)
  Use scipy.linalg.get_lapack_funcs(['gesv'], (A, b)) to get direct LAPACK function pointer.
```

---

## Julia: The Performance Alternative

Julia was designed from scratch to close the "two-language problem" (prototype in Python, rewrite in C for performance):

```
TWO-LANGUAGE PROBLEM:
  Python: fast to write, slow to run (interpreted loop bottleneck).
  C/Fortran: fast to run, slow to write.
  Old solution: prototype in Python, rewrite hot loops in C extensions.
  Julia's solution: JIT-compile Julia code to native LLVM IR -> near-C speed.

JULIA TYPE SYSTEM AND MULTIPLE DISPATCH:
  Julia's performance secret: functions specialize on argument types.
  When f(x::Float64) is first called: LLVM compiles a specialized version.
  Next call with same type: runs compiled version.
  This is "type inference + specialization" — automatic, not manual like C++ templates.

  Multiple dispatch: method chosen based on ALL argument types (vs. single dispatch in Python/C++).
  norm(x::Vector{Float64}) dispatches differently from norm(x::SparseVector{Float64}).
  Library authors define specialized methods for each type combination.

ARRAY PERFORMANCE:
  a = [1.0, 2.0, 3.0]          # Vector{Float64}, stack/heap allocated
  for i in 1:length(a)          # Julia loop: ~same speed as C loop after JIT
    a[i] = a[i] * 2
  end

  @simd for i in ...: hint SIMD vectorization.
  @inbounds for i in ...: skip bounds checks (dangerous but fast).
  @turbo (LoopVectorization.jl): auto-vectorize with SLEEF intrinsics.

KEY JULIA PACKAGES:
  LinearAlgebra (stdlib) — wraps BLAS/LAPACK (same backends as SciPy)
    A \ b:          dispatches to appropriate LAPACK solver based on A's type
    Symmetric(A):   hints that A is symmetric -> uses DSYSV
    Cholesky(A):    explicit Cholesky
    svd(A):         DGESVD/DGESDD

  SparseArrays (stdlib) — CSC-format sparse matrices
    sparse(I, J, V, m, n)
    A \ b: calls CHOLMOD (SPD) or UMFPACK (general)

  DifferentialEquations.jl — best ODE/PDE ecosystem available
    solve(prob, Tsit5())    # 4th/5th order Runge-Kutta (better than RK45)
    solve(prob, Rodas5())   # 5th order Rosenbrock (stiff)
    solve(prob, KenCarp4()) # IMEX for PDE method-of-lines
    Event handling, delay DEs, SDEs, DDEs all unified.

  Flux.jl / Lux.jl — ML in Julia (uses Zygote.jl for AD)
  Turing.jl — probabilistic programming (NUTS/HMC, equivalent to Stan/PyMC)
  Optim.jl — optimization (L-BFGS, Nelder-Mead, CG, trust region)
  Makie.jl — high-performance plotting (GPU-accelerated)

  Automatic Differentiation ecosystem:
  Zygote.jl: source-to-source AD (reverse mode) — for ML
  ForwardDiff.jl: forward-mode AD via dual numbers — for small gradients
  Enzyme.jl: LLVM-level AD — fastest, but harder to use

JULIA vs. PYTHON:
  First run: slow (JIT compilation). Subsequent runs: near-C speed.
  Time-to-first-plot (TTFP) problem: historically bad, improving with precompilation.
  Ecosystem: smaller than Python's but often higher quality in numerical domains.
  Interop: PyCall.jl (call Python from Julia), PythonCall.jl (better).
```

---

## MATLAB: The Legacy Standard

MATLAB remains dominant in control theory, signal processing, and many engineering domains. Understanding its model is important for bridging to Python/Julia:

```
MATLAB ARCHITECTURE:
  Interpreted JIT-compiled language + extensive toolbox ecosystem.
  MathWorks maintains tight control: proprietary, license-based.

  The matrix is the native type (hence MATLAB = MATrix LABoratory).
  A = [1 2; 3 4]  creates a 2x2 matrix — no explicit types needed.
  Division A/b calls backslash operator -> LAPACK solver selection.

MATLAB vs. PYTHON EQUIVALENTS:
  MATLAB                    NumPy/SciPy equivalent
  -------                   -----------------------
  A \ b                     scipy.linalg.solve(A, b)
  [U,S,V] = svd(A)          U, s, Vt = scipy.linalg.svd(A)
  eig(A)                    scipy.linalg.eig(A)
  fft(x)                    scipy.fft.fft(x)
  ode45(f, tspan, y0)       solve_ivp(f, tspan, y0, method='RK45')
  ode15s(f, tspan, y0)      solve_ivp(f, tspan, y0, method='BDF')
  fminunc(f, x0)            scipy.optimize.minimize(f, x0, method='BFGS')
  linprog(c, A, b)          scipy.optimize.linprog(c, A_ub=A, b_ub=b)
  bvp4c(f, bc, solinit)     scipy.integrate.solve_bvp(f, bc, x, y)
  sparse(I, J, V, m, n)     scipy.sparse.coo_matrix((V,(I,J)),shape=(m,n))

MATLAB TOOLBOXES (key ones):
  Optimization Toolbox       — fmincon, quadprog, intlinprog
  Statistics & ML Toolbox    — equivalent to scikit-learn/statsmodels
  Signal Processing Toolbox  — filter design, spectral analysis
  Control System Toolbox     — Bode plots, LQR, Nyquist
  Simulink                   — block diagram simulation (DAE solver backbone)
  Parallel Computing Toolbox — parfor, GPU arrays (gpuArray)
  Communications Toolbox     — modulation, error correction

  Most have direct Python equivalents now; MATLAB's advantage is integration
  and the Simulink ecosystem (which has no real peer for control/systems work).

MATLAB vs. PYTHON/JULIA PERFORMANCE:
  MATLAB: Fast matrix ops (BLAS/MKL), but slow loops (JIT somewhat helps).
  Python+NumPy: Similar matrix op performance, same BLAS backend.
  Julia: Faster than both for loop-heavy code; similar for BLAS-heavy.

  MATLAB's JIT (MATLAB 2015b+): loops are much faster now, but still ~2-5x
  slower than Julia/C for non-vectorizable code.

OCTAVE:
  Open-source MATLAB clone. Most MATLAB syntax compatible.
  ~50% speed of MATLAB (no equivalent JIT/code generation).
  Sufficient for most algorithm prototyping.
```

---

## Automatic Differentiation

AD is essential for all gradient-based methods in module 08. It's not numerical differentiation:

```
COMPARISON:
  Numerical diff:  (f(x+h) - f(x)) / h   -- O(epsilon^{1/2}) accuracy, O(n) cost for gradient
  Symbolic diff:   expression manipulation -- exact but exponential blowup
  Automatic diff:  exact derivatives, O(cost of f) -- the right approach

FORWARD MODE AD (dual numbers):
  Represent (value, derivative) pairs.
  For scalar input: propagate (f(x), f'(x)) through the computation graph.
  COST: one forward pass per input dimension.
  OPTIMAL WHEN: few inputs, many outputs. df/dx for scalar x.

  Dual number: x = (a, b) means a + b*epsilon, epsilon^2 = 0.
  (a,b) * (c,d) = (ac, ad + bc)   [product rule encoded in multiplication]
  sin((a,b)) = (sin(a), b*cos(a)) [chain rule encoded]

REVERSE MODE AD (backpropagation):
  Forward pass: record computation graph (tape).
  Backward pass: propagate adjoint (sensitivity) from output to inputs.
  COST: O(cost of f) regardless of input dimension.
  OPTIMAL WHEN: many inputs, scalar/few outputs. Gradient of f: R^n -> R.

  This is why backpropagation in neural networks uses reverse mode:
  Loss is scalar, parameters are millions -> reverse mode essential.

PYTHON AD LIBRARIES:
  PyTorch (torch.autograd): reverse mode, dynamic computation graph.
    loss.backward() -> accumulates gradients in .grad attributes.
  JAX (jax.grad): functional AD, supports forward+reverse+higher-order.
    jax.grad(f)(x) -> gradient of f at x (reverse mode by default).
    jax.jvp(f, (x,), (v,)) -> (f(x), Jf(x)@v) (forward mode JVP).
    jax.vmap(jax.grad(f))(X) -> batched gradient (vectorized over batch).
  Zygote.jl (Julia): source-to-source, very fast for Julia code.
  Enzyme.jl (Julia): LLVM-level, fastest available.

HIGHER-ORDER DERIVATIVES:
  JAX: jax.hessian(f)(x) = jax.jacfwd(jax.jacrev(f))(x)
    O(n^2) output but computable via forward-over-reverse.
  Practical Hessian-vector products: O(cost of f) via forward-over-reverse.
    jax.jvp(jax.grad(f), (x,), (v,)) -> (grad f(x), H(x)@v)
  Used in: Newton's method (module 08), Gauss-Newton, natural gradient.

JAX TRANSFORMS COMPOSABILITY:
  jax.jit: JIT-compile Python+NumPy code to XLA (CPU/GPU/TPU).
  jax.grad: differentiation.
  jax.vmap: vectorize (auto-batch).
  jax.pmap: parallelize across devices (multi-GPU).
  These COMPOSE: jax.jit(jax.vmap(jax.grad(f))) works correctly.
```

---

## Performance Profiling and Benchmarking

Numerical code performance requires measurement, not intuition:

```
PYTHON PROFILING:
  %timeit np.linalg.solve(A, b)        # IPython/Jupyter: repeat timing
  cProfile.run("func()")               # function-level profiling
  line_profiler (@profile decorator)   # line-level timing
  memory_profiler (@profile, memory)   # memory usage per line

  NUMPY PERFORMANCE DIAGNOSTICS:
  np.__config__.show()   # which BLAS/LAPACK is linked
  import numpy as np; np.show_config()
  # Look for: "openblas_info", "blas_mkl_info"
  # MKL is fastest on Intel CPUs.

JULIA PROFILING:
  @time f(x)              # wall time + allocations
  @btime f($x)            # BenchmarkTools: stable timing, eliminates JIT noise
  @profile f(x)           # statistical profiler
  Profile.print()         # show results
  Cthulhu.jl: annotate types in compiled code (find type instabilities)
  @code_warntype f(x)     # show type inference result (red = bad)

BOTTLENECK IDENTIFICATION:
  Amdahl's Law: if 10% of runtime is not parallelizable,
  max speedup = 1 / (1 - 0.9) = 10x regardless of parallelism.
  Find the serial bottleneck first.

  Rule of thumb for numerical code:
  1. Is it memory-bandwidth bound? (SpMV, streaming ops)
     -> Try cache blocking, compressed storage, different format.
  2. Is it compute bound? (GEMM, FFT)
     -> Already close to peak; use vendor library, mixed precision.
  3. Is it latency bound? (many small operations)
     -> Batch/fuse operations, reduce Python overhead, use numba/Cython.

NUMBA — JIT for Python loops:
  from numba import njit
  @njit
  def myloop(x, y):
    s = 0.0
    for i in range(len(x)):
      s += x[i] * y[i]
    return s

  First call: compiles to LLVM native code.
  Subsequent calls: runs compiled code — near-Fortran speed.
  Supports @njit(parallel=True) with prange for OpenMP-style loops.
  Supports @cuda.jit for GPU kernels (CUDA Python).

  NUMBA vs. NUMPY:
  Vectorizable ops (dot, sum): NumPy wins (hand-tuned BLAS/ufuncs).
  Non-vectorizable loops, custom logic: Numba wins.
  Pattern: replace pure Python loops with @njit, use NumPy for everything else.
```

---

## Putting It Together: A Scientific Computing Workflow

```
PROBLEM: Solve 2D Poisson equation on irregular domain (FEM, module 07)
         with 10^5 degrees of freedom, need solution and sensitivity.

STEP 1 — MESH GENERATION:
  Python: meshio (read Gmsh .msh files), pygmsh (script Gmsh from Python).
  MATLAB: PDE Toolbox (generateMesh), or Gmsh interface.
  Output: nodes (N x 2 float64), connectivity (E x 3 int32).

STEP 2 — ASSEMBLE STIFFNESS MATRIX:
  Tight loop over elements -> use Numba @njit.
  Assemble in COO format (append (i,j,val) triples per element).
  Convert to CSC: K = scipy.sparse.csc_matrix((data,(row,col)), shape=(N,N))
  Load vector f: straightforward NumPy.

STEP 3 — APPLY BOUNDARY CONDITIONS:
  Dirichlet: zero rows/columns (modify CSC in-place or rebuild COO).

STEP 4 — SOLVE:
  K is SPD (for Poisson): use scipy.sparse.linalg.cholesky (CHOLMOD).
  factor = cholesky(K); u = factor(f)
  OR: if iterative OK: scipy.sparse.linalg.cg(K, f, M=AMG_preconditioner)
  AMG preconditioner: pyamg library (Algebraic MultiGrid, module 02).

STEP 5 — POST-PROCESS:
  u is a NumPy array; evaluate at points, interpolate (module 04).
  scipy.interpolate.LinearNDInterpolator for scattered-to-regular grid.

STEP 6 — SENSITIVITY ANALYSIS:
  If need du/dp where p is a parameter: adjoint method.
  Solve K^T lambda = dJ/du; dJ/dp = -lambda^T (dK/dp u - df/dp).
  Same K factorization reused for adjoint solve.

STEP 7 — VISUALIZATION:
  Python: matplotlib (2D), PyVista (3D mesh visualization via VTK).
  Julia: Makie.jl (high performance, GPU-accelerated).
  MATLAB: built-in pdeplot, pdemesh.

AZURE HPC SCALE-OUT:
  If N > 10^7 (e.g., full 3D FEM model):
  - Distribute K across nodes via PETSc (Python interface: petsc4py).
  - Use MUMPS or SuperLU_DIST for distributed-memory sparse direct solve.
  - Azure HBv3 VM: 120 cores + InfiniBand -> MPI for PBLAS/ScaLAPACK.
  - Azure Batch: submit MPI job via BatchClient (same pattern as ADF pipeline).
  - Monitoring: Azure Monitor -> equivalent to your SCOM background.
```

---

## Decision Cheat Sheet

| Need | Tool | Notes |
|---|---|---|
| Dense matrix ops in Python | NumPy + SciPy | BLAS/LAPACK backend, near-C speed |
| Sparse linear solve, SPD | scipy.sparse.linalg + CHOLMOD | Reordering essential for large problems |
| Sparse linear solve, general | UMFPACK via scipy.sparse.linalg.spsolve | Or iterative (CG/GMRES + precond) |
| ODE/PDE in Python | scipy.integrate.solve_ivp | RK45 default; Radau/BDF for stiff |
| ODE/PDE with max performance | DifferentialEquations.jl (Julia) | Best ecosystem for diffeq anywhere |
| GPU-accelerated dense linalg | CuPy or PyTorch | cuBLAS/cuSOLVER backend |
| GPU-accelerated ML training | PyTorch or JAX | Half-precision Tensor Cores |
| Auto-differentiation, ML | PyTorch (dynamic) or JAX (functional) | Both call cuBLAS for ops |
| Performance-critical Python loops | Numba @njit | JIT to native, near-Fortran |
| Large-scale distributed | PETSc (petsc4py) or ScaLAPACK | MPI-based, Azure HPC ready |
| FFT (large, performance) | scipy.fft + pyfftw | FFTW backend ~2-4x faster |
| Control systems / Simulink work | MATLAB | Still dominant for control eng |
| Eigenvalue, sparse, large | scipy.sparse.linalg.eigsh (ARPACK) | Lanczos, module 03 |
| Optimization, general | scipy.optimize.minimize (L-BFGS-B) | Module 08 |
| Sparse format conversion path | COO -> CSR/CSC -> solve | Build in COO, compute in CSR/CSC |

---

## Common Confusion Points

**"Python is slow for numerical computing."**
Python the interpreter is slow (50-100ns per iteration). But numpy.dot(A, B) for large A, B runs at near-peak FLOP/s because it calls DGEMM — zero Python overhead during the actual computation. The key insight: move work below the Python interpreter layer. Vectorized NumPy, Numba JIT, and CuPy all do this. The "slow Python" problem only bites when you write explicit Python loops over array elements.

**"MATLAB is obsolete."**
MATLAB is still dominant in control systems, signal processing, and anything using Simulink. The Simulink ecosystem (model-based design, code generation for embedded) has no real Python equivalent. For pure numerical algorithm work, Python/Julia have largely caught up. For academic/research work: Python has won (scikit-learn, PyTorch, etc.). For industrial control/embedded: MATLAB/Simulink is still the standard.

**"Julia will replace Python."**
Julia solves the two-language problem for code where you need to write custom loops. For NumPy/SciPy workloads (calling into BLAS/LAPACK), Python and Julia have identical performance because they call the same BLAS routines. Julia's advantage is code where Python needs Numba or C extensions. Python's advantage is ecosystem size (ML, web, data engineering). Most practitioners use Python for the ecosystem and add Julia/Numba for hot loops.

**"GPU always beats CPU."**
PCIe transfer speed (16 GB/s typical) is the ceiling. For operations that require moving data CPU<->GPU, you need O(time to compute) >> O(time to transfer) to break even. A 1000x1000 DGEMM: 8 MB data, 2 ms transfer at 4 GB/s vs. 1 ms compute on modern GPU — marginal. A 10000x10000 DGEMM: 800 MB data but 2000x more compute: GPU wins by 1000x. Keep data on GPU across multiple operations; never ping-pong between CPU and GPU.

**"scipy.linalg and numpy.linalg are the same."**
Both call LAPACK, but scipy.linalg exposes more control. scipy.linalg.solve() has assume_a parameter (sym/pos/gen) that selects the appropriate LAPACK driver. scipy.linalg.lu_factor() / lu_solve() allow factoring once and solving many times. scipy.linalg.get_lapack_funcs() gives raw LAPACK function handles. Use scipy.linalg for performance-critical code where you know the matrix structure.

**"Automatic differentiation is just numerical differentiation."**
Numerical differentiation: (f(x+h) - f(x))/h. Only O(epsilon^{1/2}) accurate (FP cancellation), and O(n) cost for gradient. Automatic differentiation: chain rule applied exactly through the computation graph. Machine-precision accurate, O(cost of f) for gradient in reverse mode — independent of parameter count. This is why backpropagation works for training billion-parameter neural networks: exact gradients at O(1 forward pass) cost.
