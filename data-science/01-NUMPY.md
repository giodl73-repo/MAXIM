# 01 — NumPy

> NumPy is not a math library. It is a memory layout manager with a C execution engine
> that happens to speak linear algebra. Understanding the memory model explains everything.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         NUMPY IN THE STACK                                  │
│                                                                             │
│  Your Python code                                                           │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  NumPy API  (ndarray methods, ufuncs, linalg, fft, random, ...)    │   │
│  └────┬────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  C extension layer  (type-specialized loops, BLAS/LAPACK calls)    │   │
│  └────┬────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  Contiguous memory block  (dtype-homogeneous, row-major by default) │   │
│  └────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  Everything above NumPy — Pandas, scikit-learn, PyTorch CPU, SciPy —      │
│  ultimately operates on or converts to ndarray memory.                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## The ndarray Memory Model

This is the thing that actually matters. Once you understand the memory layout,
broadcasting, views, copies, and performance characteristics all follow.

```
ndarray metadata:
  data      → pointer to start of memory block
  dtype     → element type (float64, int32, complex128, ...)
  shape     → tuple of dimension sizes: (rows, cols, ...)
  strides   → bytes to step in each dimension
  flags     → C_CONTIGUOUS, F_CONTIGUOUS, WRITEABLE, OWNDATA
```

### Strides Are the Key

```python
import numpy as np

a = np.array([[1, 2, 3],
              [4, 5, 6]], dtype=np.float64)

print(a.shape)    # (2, 3)
print(a.strides)  # (24, 8)  — 24 bytes to next row, 8 bytes to next col
                  # float64 = 8 bytes; row-major → col stride = 8, row stride = 3*8 = 24
```

Memory layout (row-major / C order):
```
[1.0][2.0][3.0][4.0][5.0][6.0]
 ←── 8 bytes ──→
 ←────────── 24 bytes (one row) ──────────→
```

### Views vs Copies

Most NumPy operations return **views** — a new ndarray metadata struct pointing
into the same memory block with different shape/strides. No data is copied.

```python
a = np.arange(12, dtype=np.float64)  # [0,1,2,...,11]

# View: same memory, different shape
b = a.reshape(3, 4)
b[0, 0] = 99
print(a[0])        # 99 — b and a share memory

# View: transpose — just swaps strides
c = b.T
print(c.strides)   # (8, 32) — was (32, 8) — transposing swaps strides, no copy

# Copy: when you actually need independent data
d = b.copy()
d[0, 0] = 0
print(b[0, 0])     # still 99

# Fancy indexing always copies
e = a[[0, 2, 5]]   # e is a copy, not a view
```

**Rule of thumb**: slicing with `[start:stop:step]` → view. Integer array indexing → copy.

### Contiguity and BLAS

BLAS (Basic Linear Algebra Subprograms) — what makes `np.dot` fast — requires
C-contiguous or F-contiguous memory. When you pass a non-contiguous array (e.g.,
a transposed matrix) to a BLAS routine, NumPy silently copies it first.

```python
a = np.random.rand(1000, 1000)
b = np.random.rand(1000, 1000)

# Fast: both C-contiguous, BLAS call direct
%timeit np.dot(a, b)          # ~2ms on modern CPU

# Slower: a.T is not C-contiguous, NumPy copies before BLAS
%timeit np.dot(a.T, b)        # ~3ms — extra copy

# F-order matrix is C-contiguous when transposed
a_f = np.asfortranarray(a)
%timeit np.dot(a_f.T, b)      # ~2ms — a_f.T is C-contiguous
```

---

## dtypes

```
┌──────────────┬──────────┬─────────────────────────────────────────────┐
│  dtype       │  bytes   │  notes                                      │
├──────────────┼──────────┼─────────────────────────────────────────────┤
│  float64     │  8       │  default float; C double                    │
│  float32     │  4       │  half memory; GPU-native; less precision    │
│  float16     │  2       │  ML inference; 5-bit exponent               │
│  int64       │  8       │  default integer on 64-bit                  │
│  int32       │  4       │  common in indices, counters                │
│  int8        │  1       │  quantized ML weights                       │
│  bool_       │  1       │  masks; packed in memory                    │
│  complex128  │  16      │  two float64; FFT output                    │
│  object_     │  varies  │  Python objects; kills vectorization        │
└──────────────┴──────────┴─────────────────────────────────────────────┘

object_ dtype is the performance trap. A Pandas column of mixed types
or Python strings ends up as object_ — no vectorized C path available.
```

```python
# dtype promotion rules
a = np.array([1, 2, 3])          # int64 (platform default)
b = np.array([1.0, 2.0, 3.0])   # float64

c = a + b                         # float64 — int promotes to float
d = a + np.int8(1)                # int64 — int8 promotes to int64

# Explicit dtype
e = np.zeros((100, 100), dtype=np.float32)  # half memory of float64
```

---

## Array Creation

```python
import numpy as np

# From data
a = np.array([1, 2, 3])                     # 1-D, int64
b = np.array([[1, 2], [3, 4]], dtype=float) # 2-D, float64

# Ranges
np.arange(0, 10, 2)          # [0, 2, 4, 6, 8]  — like range(), returns ndarray
np.linspace(0, 1, 5)         # [0.0, 0.25, 0.5, 0.75, 1.0]  — n evenly spaced
np.logspace(0, 3, 4)         # [1, 10, 100, 1000]  — log-spaced

# Filled
np.zeros((3, 4))             # 3×4 of 0.0 float64
np.ones((3, 4), dtype=int)   # 3×4 of 1 int64
np.full((3, 4), 7.0)         # 3×4 of 7.0
np.eye(4)                    # 4×4 identity
np.diag([1, 2, 3])           # diagonal matrix

# Random (new API — use default_rng, not np.random directly)
rng = np.random.default_rng(seed=42)
rng.random((3, 3))           # uniform [0, 1)
rng.standard_normal((3, 3))  # N(0,1)
rng.integers(0, 10, size=5)  # random ints in [0, 10)

# From existing — reshape/views
np.arange(12).reshape(3, 4)  # shape (3,4)
a.flatten()                  # always a copy, 1-D
a.ravel()                    # view if possible, 1-D
```

---

## Indexing and Slicing

```python
a = np.arange(24).reshape(4, 6)  # shape (4, 6)

# Basic slicing — views
a[0]          # first row: shape (6,)
a[:, 0]       # first column: shape (4,)
a[1:3, 2:5]   # submatrix rows 1-2, cols 2-4: shape (2, 3)
a[::2, ::2]   # every other row and col

# Ellipsis — fills in missing dimensions
b = np.zeros((2, 3, 4, 5))
b[0, ..., 2]  # equivalent to b[0, :, :, 2], shape (3, 4)

# Integer indexing — copies, advanced indexing
a[[0, 2]]         # rows 0 and 2: shape (2, 6)
a[[0, 1], [0, 2]] # elements (0,0) and (1,2): shape (2,)  NOT a 2×2 block

# Boolean masking — copies
mask = a > 10
a[mask]           # 1-D array of elements > 10
a[a % 2 == 0]     # elements divisible by 2

# np.ix_ for Cartesian product indexing (the thing you probably want)
rows = np.array([0, 2])
cols = np.array([1, 3, 5])
a[np.ix_(rows, cols)]  # 2×3 submatrix — this is a copy
```

The `[rows, cols]` vs `[np.ix_(rows, cols)]` distinction is the #1 NumPy
indexing confusion. The former zips the indices; the latter takes the outer product.

---

## Broadcasting

Broadcasting is NumPy's most powerful (and most confusing) feature. It allows
operations between arrays of different shapes by implicitly expanding dimensions.

### Rules

```
1. Align shapes right-to-left.
2. For each dimension:
   - If sizes match → fine
   - If one size is 1 → broadcast (stretch) that dimension
   - Otherwise → shape error
```

```
Example:
  a shape: (4, 3)
  b shape:    (3,)    →  right-aligned: (1, 3)  →  broadcast to (4, 3)
  a + b:   (4, 3)

  c shape: (4, 1)
  d shape: (1, 3)
  c + d:   (4, 3)   — outer product pattern

  e shape: (4, 3)
  f shape: (4,)     →  right-aligned: (1, 4)?  → NO — (4,) aligns as (4,) not (4,1)
  e + f:   ERROR    — dimensions don't broadcast
  fix:   e + f[:, np.newaxis]  or  e + f.reshape(4, 1)
```

```python
# Row-wise normalization without a loop
X = rng.random((100, 10))
row_means = X.mean(axis=1)        # shape (100,)
row_stds = X.std(axis=1)          # shape (100,)

# Need (100, 1) to broadcast against (100, 10)
X_normalized = (X - row_means[:, np.newaxis]) / row_stds[:, np.newaxis]

# Equivalently with keepdims=True
row_means2 = X.mean(axis=1, keepdims=True)  # shape (100, 1)
X_normalized2 = (X - row_means2) / X.std(axis=1, keepdims=True)
```

### Broadcasting Performance

Broadcasting does **not** allocate the expanded intermediate array — it is a
virtual expansion, stepping through memory with zero-sized strides on broadcast
dimensions. This is why `X - row_means[:, np.newaxis]` is fast: it computes each
element directly from the original memory layout.

---

## Universal Functions (ufuncs)

Ufuncs are element-wise operations implemented in C with type dispatch and
loop fusion. They support broadcasting, output arrays, accumulation, and reduction.

```python
a = np.array([1.0, 4.0, 9.0])

np.sqrt(a)          # [1.0, 2.0, 3.0]  — much faster than [math.sqrt(x) for x in a]
np.log(a)           # natural log element-wise
np.exp(a)           # e^x element-wise
np.add(a, a)        # same as a + a
np.maximum(a, 3.0)  # element-wise max with scalar

# Output buffer — avoid allocating a new array
out = np.empty_like(a)
np.sqrt(a, out=out)

# Reduce and accumulate
np.add.reduce(a)         # sum: 14.0
np.add.accumulate(a)     # cumulative sum: [1.0, 5.0, 14.0]
np.multiply.reduce(a)    # product: 36.0

# Outer product
np.multiply.outer([1, 2, 3], [10, 20])
# [[10, 20], [20, 40], [30, 60]]
```

---

## Axis Operations

The `axis` parameter is how NumPy knows which dimension to collapse/operate along:

```
axis=0 → operate along rows (collapse rows → result has shape of one row)
axis=1 → operate along cols (collapse cols → result has shape of one col)
axis=-1 → last axis
```

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])  # shape (2, 3)

a.sum(axis=0)    # [5, 7, 9]   — sum down the rows: shape (3,)
a.sum(axis=1)    # [6, 15]     — sum across the cols: shape (2,)
a.sum()          # 21          — sum everything

a.max(axis=0)    # [4, 5, 6]
a.argmax(axis=1) # [2, 2]      — index of max in each row
```

---

## Linear Algebra — `np.linalg`

You know the math. Here is the API surface you will use:

```python
A = np.array([[2., 1.], [1., 3.]])
b = np.array([8., 13.])

# Solve Ax = b
x = np.linalg.solve(A, b)          # [3., 2.] — uses LAPACK gesv (LU factorization)

# Eigendecomposition
eigenvalues, eigenvectors = np.linalg.eig(A)    # general (possibly complex)
eigenvalues, eigenvectors = np.linalg.eigh(A)   # symmetric/Hermitian → real eigenvalues

# SVD
U, s, Vt = np.linalg.svd(A)                    # full SVD
U, s, Vt = np.linalg.svd(A, full_matrices=False) # economy SVD

# Matrix properties
np.linalg.det(A)        # determinant
np.linalg.matrix_rank(A)# rank
np.linalg.cond(A)       # condition number
np.linalg.norm(A)       # Frobenius norm by default
np.linalg.norm(A, ord=2)# spectral norm (largest singular value)

# Matrix operations
np.linalg.inv(A)        # inverse — don't use this to solve Ax=b (use solve)
np.linalg.pinv(A)       # Moore-Penrose pseudoinverse
A @ b                   # matrix multiply (@ operator, Python 3.5+)
np.dot(A, b)            # same; @ is preferred for clarity

# Cholesky (A must be positive definite)
L = np.linalg.cholesky(A)   # A = L @ L.T

# QR decomposition
Q, R = np.linalg.qr(A)
```

`np.linalg.solve` is always preferable to `np.linalg.inv(A) @ b` — it is faster
and more numerically stable (avoids computing the inverse explicitly).

### Batch Linear Algebra

All `np.linalg` functions support batched inputs since NumPy 1.8:

```python
# Solve 100 systems simultaneously
A_batch = rng.random((100, 3, 3))
b_batch = rng.random((100, 3))
x_batch = np.linalg.solve(A_batch, b_batch)  # shape (100, 3)

# 100 eigendecompositions
vals, vecs = np.linalg.eigh(A_batch)  # vals: (100,3), vecs: (100,3,3)
```

---

## FFT — `np.fft`

```python
# 1-D DFT
signal = np.sin(2 * np.pi * 5 * np.linspace(0, 1, 1000))  # 5 Hz sine
spectrum = np.fft.fft(signal)               # complex output, length 1000
freqs = np.fft.fftfreq(1000, d=1/1000)     # frequency axis (Hz)
magnitude = np.abs(spectrum)

# Shift to center DC component
spectrum_centered = np.fft.fftshift(spectrum)
freqs_centered = np.fft.fftshift(freqs)

# Real FFT (input is real → output is Hermitian symmetric, half the size)
spectrum_r = np.fft.rfft(signal)            # length 501 (N//2 + 1)
freqs_r = np.fft.rfftfreq(1000, d=1/1000)  # positive freqs only

# 2-D DFT (image processing)
image = rng.random((256, 256))
spectrum_2d = np.fft.fft2(image)
spectrum_2d_shifted = np.fft.fftshift(spectrum_2d)
```

The 2-D DFT is the same algorithm you covered in MIT 2-D DSP, just wrapped.

---

## Performance Patterns

### Vectorize, Never Loop

```python
# Slow: Python loop
result = np.empty(1_000_000)
for i in range(1_000_000):
    result[i] = np.sqrt(arr[i])        # 1M Python dispatch overhead calls

# Fast: vectorized ufunc
result = np.sqrt(arr)                  # single C loop, ~100× faster

# Slow: list comprehension over array rows
norms = [np.linalg.norm(row) for row in X]  # N Python function calls

# Fast: vectorized along axis
norms = np.linalg.norm(X, axis=1)
```

### Memory-Efficient Patterns

```python
# In-place operations avoid allocation
a += b          # modifies a in place; no new array
np.add(a, b, out=a)  # same, explicit

# Views avoid copies — use when possible
sub = a[10:20]        # view into a; no copy

# Specify dtype upfront
X = np.zeros((N, D), dtype=np.float32)  # half the memory of float64
```

### When Vectorization Isn't Enough

```
NumPy → Numba (JIT-compile Python loops with @njit)
NumPy → CuPy (same API, GPU execution)
NumPy → JAX  (NumPy-compatible, XLA compilation, autograd)
NumPy → Cython (typed Cython → C extension)
```

Numba is the easiest path: `@numba.njit` on a pure Python function that iterates
over NumPy arrays compiles it to native machine code at first call.

---

## Common Confusion Points

**`a * b` vs `a @ b`**: `*` is element-wise multiplication (Hadamard product).
`@` is matrix multiplication. `np.dot` with 2-D arrays is also matrix multiply.
They are different operations. `a * b` on two `(3,3)` matrices is NOT matrix
multiply — it is element-wise.

**Slicing returns views; fancy indexing returns copies**: `a[0:3]` is a view.
`a[[0, 1, 2]]` is a copy. Mutating a sliced subarray modifies the original.
Mutating a fancy-indexed array does not.

**`axis=0` collapses rows, not "operates on rows"**: `a.mean(axis=0)` gives the
column means (one value per column) by collapsing across rows. The wording "along
axis 0" means the axis is consumed, not preserved.

**Shape `(N,)` vs `(N,1)` vs `(1,N)`**: These broadcast differently.
`(N,)` and `(N,1)` are not the same. Transposing a `(N,)` array has no effect —
`a.T` where `a.shape == (5,)` still has shape `(5,)`. Use `a[:, np.newaxis]`
or `a.reshape(-1, 1)` to get `(N, 1)`.

**`np.random.seed` is deprecated**: Use `np.random.default_rng(seed)` and keep
the Generator object. The legacy `np.random.seed` / `np.random.rand` API is
not thread-safe and will eventually be removed.

**Integer overflow is silent**: NumPy integer arithmetic wraps on overflow.
`np.int8(127) + np.int8(1)` is `-128`, not an error. Use `int64` or check
values if this matters.

---

## Decision Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│  TASK                           │  APPROACH                        │
├─────────────────────────────────┼──────────────────────────────────┤
│  Create array from list         │  np.array([...])                 │
│  Create range array             │  np.arange / np.linspace         │
│  Solve linear system Ax=b       │  np.linalg.solve(A, b)           │
│  Eigendecomposition (symmetric) │  np.linalg.eigh(A)               │
│  SVD                            │  np.linalg.svd(A, full_matrices=F│
│  Matrix multiply                │  A @ B  (not A * B)              │
│  Row/col statistics             │  .mean(axis=0) / .mean(axis=1)   │
│  Normalize rows                 │  X / X.sum(axis=1, keepdims=True)│
│  Boolean mask                   │  a[a > threshold]                │
│  Non-contiguous submatrix       │  a[np.ix_(rows, cols)]           │
│  FFT of real signal             │  np.fft.rfft(x)                  │
│  Check if view or copy          │  a.base is not None → view       │
│  Force C-contiguous copy        │  np.ascontiguousarray(a)         │
├─────────────────────────────────┼──────────────────────────────────┤
│  PERFORMANCE                    │                                  │
│  Loop is slow                   │  Vectorize or np.vectorize       │
│  Need faster loops              │  numba.njit                      │
│  Need GPU                       │  CuPy (same NumPy API)           │
│  Need autograd + GPU + JIT      │  JAX                             │
│  Memory is tight                │  float32 instead of float64      │
└─────────────────────────────────┴──────────────────────────────────┘
```
