# Floating-Point Arithmetic

## The Big Picture

Floating-point is a hardware-level approximation to real arithmetic. Every calculation introduces small errors; how those errors compound determines whether you get a useful result or garbage.

```
+------------------------------------------------------------------+
|                   IEEE 754 FLOATING-POINT                        |
+------------------------------------------------------------------+
|                                                                  |
|  A floating-point number x:                                      |
|  x = (-1)^sign * mantissa * 2^exponent                         |
|                                                                  |
|  DOUBLE PRECISION (float64):                                     |
|  +--------+--------------------+------------------------------+  |
|  | 1 bit  | 11 bits            | 52 bits                      |  |
|  | sign   | biased exponent    | fraction (significand)       |  |
|  +--------+--------------------+------------------------------+  |
|                                                                  |
|  Range: ~5e-324 to ~1.8e308                                     |
|  Machine epsilon: eps_mach = 2^{-52} = 2.22e-16                |
|  (~16 significant decimal digits)                               |
|                                                                  |
|  SINGLE PRECISION (float32): eps_mach = 2^{-23} = 1.19e-7     |
|  (~7 significant decimal digits)                                |
|  Common in GPU ML (TPU uses bfloat16: exp=8 bits, frac=7 bits) |
|                                                                  |
+------------------------------------------------------------------+
```

---

## The IEEE 754 Standard

IEEE 754 (1985, revised 2008) defines floating-point arithmetic for all modern hardware. The learner's background with .NET and CLR puts them in regular contact with this standard — every float and double in C# obeys it.

**Number representation**:

```
  Normalized number: x = +/- 1.f * 2^e
  where f is the 52-bit fraction and e = exponent - 1023 (bias)

  Subnormal numbers: gradual underflow near 0
  x = +/- 0.f * 2^{-1022}  (no leading 1)
  Allow gradual loss of precision near 0; avoid hard underflow to 0.

  Special values:
  +inf, -inf: overflow or division by nonzero / 0
  NaN (Not a Number): 0/0, inf - inf, sqrt(-1), etc.
  +0 and -0: same value, different bit pattern. (+0 == -0 is true)

  IEEE GUARANTEES:
  Each basic operation (+, -, *, /, sqrt) is "correctly rounded":
  fl(x op y) = round(x op y)  where round rounds to nearest representable float.
  This is the EXACT rounding guarantee — critical for reproducibility.
```

**Machine epsilon**:

```
  eps_mach = 2^{-p+1}  where p = bits in significand
  = smallest eps such that fl(1 + eps) > 1

  Interpretation: fl(x) = x(1 + delta)  where |delta| <= eps_mach/2
  Every representable number has relative error at most eps_mach/2.

  float16:  eps_mach = 2^{-10}  = 9.77e-4   (~3 decimal digits)
  bfloat16: eps_mach = 2^{-7}   = 7.81e-3   (~2 decimal digits)
  float32:  eps_mach = 2^{-23}  = 1.19e-7   (~7 decimal digits)
  float64:  eps_mach = 2^{-52}  = 2.22e-16  (~16 decimal digits)
  float128: eps_mach = 2^{-112} = 1.93e-34  (~34 decimal digits)
```

---

## Rounding Modes

IEEE 754 specifies five rounding modes:

```
  ROUND TO NEAREST EVEN (default):
  Round to the nearest representable number.
  If equidistant: round to the one with even last bit.
  This is the most common mode; minimizes average rounding error.

  ROUND TOWARD +INF (ceiling):
  Always round up. Used in interval arithmetic upper bounds.

  ROUND TOWARD -INF (floor):
  Always round down. Used in interval arithmetic lower bounds.

  ROUND TOWARD ZERO (truncation):
  Chop off the fractional part.

  ROUND AWAY FROM ZERO:
  Less common; maximizes magnitude.

  For .NET/C# context:
  System.Math.Round(x) uses banker's rounding (round half to even) by default.
  Math.Round(x, MidpointRounding.AwayFromZero) uses round-half-up.
  This difference breaks naive financial rounding if not handled carefully.
```

---

## Catastrophic Cancellation

The most important source of catastrophic accuracy loss:

```
  CATASTROPHIC CANCELLATION:
  When two nearly-equal numbers are subtracted, significant bits cancel.

  Example: a = 1.234567890123456, b = 1.234567890123455
  a - b should = 1e-15
  In float64: fl(a) = fl(b) (identical bit patterns if they differ by less than eps_mach * a)

  THE MECHANISM:
  fl(a) = a (1 + alpha), |alpha| <= eps_mach
  fl(b) = b (1 + beta),  |beta|  <= eps_mach
  fl(a) - fl(b) ≈ (a - b) + a*alpha - b*beta

  Relative error of (a - b):
  |fl(a) - fl(b) - (a-b)| / |a-b| ≈ a/(a-b) * eps_mach

  If a ≈ b (a/(a-b) >> 1): CATASTROPHIC amplification of eps_mach.
```

**Examples of catastrophic cancellation**:

```
  QUADRATIC FORMULA: roots of ax^2 + bx + c = 0
  x = (-b +/- sqrt(b^2 - 4ac)) / (2a)

  When b >> sqrt(4ac): sqrt(b^2 - 4ac) ≈ |b|
  For x_small = (-b + sqrt(b^2-4ac)) / (2a) with b > 0:
  -b + sqrt(b^2-4ac) = very small difference of large numbers. CANCELLATION.

  FIX: use the numerically stable form
  x_small = c / (a * x_large)   (from Vieta's formulas: x_small * x_large = c/a)

  SAMPLE VARIANCE: (1/n) Sum (x_i - x_bar)^2
  Naive computation: (1/n) Sum x_i^2 - x_bar^2
  = (large) - (large) if x_i >> variation.
  FIX: compute x_bar first, then Sum (x_i - x_bar)^2.
  Or use Welford's online algorithm for numerically stable one-pass variance.

  exp(x) - 1 near x = 0:
  Direct: exp(x) = 1 + x + x^2/2 + ...  -> fl(exp(x)) - 1 = CANCELLATION.
  FIX: use expm1(x) = x + x^2/2 + ... (standard library function, no cancellation).
```

---

## Conditioning and Condition Numbers

**Condition number of a problem**: measures sensitivity of the output to perturbations in the input.

```
  For a function f: R^n -> R^m, at input x:
  kappa = ||J_f(x)|| * ||x|| / ||f(x)||   (relative condition number)

  where J_f = Jacobian of f.

  Large kappa: ill-conditioned. Small input perturbation -> large output change.
  kappa ≈ 1: well-conditioned.

  RULE OF THUMB:
  If kappa = 10^k, expect to lose k significant digits of accuracy.
  For float64 (16 digits): problems with kappa > 10^{16} are numerically meaningless.
```

**Condition number of a linear system Ax = b**:

```
  kappa(A) = ||A|| * ||A^{-1}||  (using any consistent matrix norm)
  For 2-norm: kappa_2(A) = sigma_max(A) / sigma_min(A)   (largest / smallest singular value)

  Sensitivity:
  ||delta x|| / ||x|| <= kappa(A) * ||delta b|| / ||b||

  Meaning: a small relative change in b causes at most kappa(A) times larger
  relative change in x.

  ILL-CONDITIONED EXAMPLES:
  Hilbert matrix H_{ij} = 1/(i+j-1): kappa = 10^13 for n=8.
  Vandermonde matrices for high-degree polynomial interpolation.
  Near-singular covariance matrices in statistics.
```

**Conditioning vs. stability (the key distinction)**:

```
  Computing x = b/a:
  Conditioning: if a ≈ 0, the problem is ill-conditioned. No algorithm can fix this.
  Stability: if you compute x = (b + eps_1) / (a + eps_2), the error propagation
  depends on how eps_1 and eps_2 are introduced.

  Computing sqrt(x^2 + y^2) ("hypot"):
  Naive: risk of overflow (x^2 or y^2 may overflow float64 even if result is fine).
  Stable: let m = max(|x|, |y|); return m * sqrt(1 + (min/max)^2).
  Same problem (perfectly conditioned), different stability.
```

---

## Backward Error Analysis

Backward error analysis (Wilkinson 1960s) is the standard framework for analyzing numerical algorithms:

```
  An algorithm A computes fl(f(x)). The backward error is:
  Find x_tilde such that A(x) = f(x_tilde) EXACTLY.

  The backward error is ||x_tilde - x||.

  A BACKWARD STABLE ALGORITHM has backward error of size O(eps_mach).
  It computes the EXACT result for a SLIGHTLY PERTURBED input.

  COMPOSING:
  Forward error <= backward error * condition number
  (for well-conditioned problems, backward stable = accurate)

  WHY BACKWARD STABILITY?
  Because the exact answer to a slightly different problem IS the answer
  if the input data itself has measurement uncertainty of that size.
  Backward stable = "as good as the data warrants."
```

**Examples**:

```
  GAUSSIAN ELIMINATION with partial pivoting: backward stable (Wilkinson 1963).
  Computes exact solution to (A + E)x = b where ||E|| <= const * eps_mach * ||A||.
  Well-conditioned -> accurate. Ill-conditioned -> as good as possible.

  WITHOUT PIVOTING: NOT backward stable in general.
  The 2x2 example: [[1e-20, 1]; [1, 1]]. Without pivoting: catastrophic loss.
  With partial pivoting: swap rows -> stable.
```

---

## Floating-Point Pitfalls in Practice

```
  ASSOCIATIVITY FAILS:
  In math: (a + b) + c = a + (b + c).
  In float: NOT always equal.
  Impact: parallel reductions (Sum x_i) give different results with different ordering.
  Pairwise summation (tree reduction) reduces error from O(n eps) to O(log(n) eps).

  COMPARISON WITH TOLERANCE:
  NEVER: if (a == b) for floats.
  USE: if (abs(a - b) < tol * max(abs(a), abs(b), 1.0))
  (relative tolerance, with fallback to absolute for near-zero values)

  DIVISION NEAR ZERO:
  if x is very small, 1/x overflows to Inf.
  Check for underflow: if |x| < eps_mach * |y|, the ratio y/x is unreliable.

  INTEGER EXACT REPRESENTATION:
  Integers up to 2^53 are exactly representable in float64.
  Beyond 2^53: consecutive integers are no longer representable.
  Long values beyond 9e15: float64 truncates. Always use long for large counts.
```

---

## Interval Arithmetic

Interval arithmetic replaces real numbers with intervals [a, b] that are guaranteed to contain the true value:

```
  [a,b] + [c,d] = [a+c, b+d]
  [a,b] * [c,d] = [min(ac,ad,bc,bd), max(ac,ad,bc,bd)]
  [a,b] / [c,d] = [a,b] * [1/d, 1/c]  (if 0 not in [c,d])

  Using directed rounding:
  Lower bound operations use ROUND TOWARD -INF.
  Upper bound operations use ROUND TOWARD +INF.

  RESULT: The computed interval is guaranteed to contain the true mathematical result.
  No rounding error can violate the bounds.

  DEPENDENCY PROBLEM: If x appears multiple times in an expression,
  the same interval is used independently, which may overestimate:
  x * (1 - x) for x in [0,1]: interval arithmetic gives [-1, 1],
  but true range is [0, 0.25].
  Fix: use "affine arithmetic" or tighter inclusion functions.

  USE CASES:
  - Verified/certified numerical computation
  - Constraint propagation in optimization
  - Rigorous numerical proofs (e.g., Kepler conjecture, Poincaré conjecture verification)
```

---

## Mixed Precision Computing

Modern ML drives a new era of deliberate precision reduction:

```
  TRAINING MODERN ML MODELS:
  float32: standard training. 32-bit, ~12 GB for GPT-3 weights.
  float16: halves memory, 2x matrix throughput on tensor cores.
           But: exponent range only 10^{-4} to 10^4. Gradient underflow common.
  bfloat16 (Brain Float 16): same exponent range as float32, less mantissa.
           Preferred for training (no gradient underflow). Google's choice.
  TF32 (TensorFloat-32): 10-bit mantissa, float32 exponent. A100/H100 default.
  float8: emerging standard for inference. Even less mantissa.

  MIXED PRECISION TRAINING (NVIDIA Apex, PyTorch AMP):
  Store weights in float32 (master copy).
  Compute forward/backward in float16.
  Loss scaling: multiply loss by large constant before backward pass to avoid underflow,
  then divide gradients before weight update.

  Effective result: 2x memory savings, 3-8x training speedup on tensor cores,
  with accuracy maintained by the float32 master copy.
```

---

## Decision Cheat Sheet

| Situation | Solution |
|---|---|
| Subtraction of nearby numbers | Reformulate to avoid cancellation (expm1, log1p, hypot) |
| Ill-conditioned linear system | Cannot fix; report condition number, use regularization |
| Sum of many numbers with varying signs | Compensated summation (Kahan) or pairwise summation |
| Equality comparison of floats | Use tolerance-based comparison; never use == |
| Need guaranteed bounds on error | Interval arithmetic |
| Overflow/underflow concerns | Scale inputs; use log-space computation; check exponent range |
| Scientific computing speed | Use float32 or mixed precision deliberately |
| Need reproducible results | Fix rounding mode; use deterministic algorithms; avoid parallelism |

---

## Common Confusion Points

**"Using double precision (float64) means I have 16 significant digits of accuracy."**
You have 16 digits of input representation accuracy. But if the problem has condition number kappa, you lose log10(kappa) digits. For kappa = 10^8 (common in ill-conditioned linear systems), you only have 8 accurate digits even with float64.

**"Floating-point errors are tiny and can be ignored."**
For a single operation: yes (relative error = eps_mach ≈ 2.2e-16). For an algorithm with n operations, the errors compound. In pathological cases (catastrophic cancellation, ill-conditioned problems), they can render results completely meaningless.

**"NaN propagates, so I'll catch errors."**
NaN only arises from operations like 0/0, inf-inf, sqrt(-1). Finite-but-wrong results (from cancellation or ill-conditioning) do NOT become NaN. They silently propagate through your computation, producing confident-looking but wrong answers. NaN detection is not a substitute for error analysis.

**"Parallel sum gives the same result as sequential sum."**
Not with floating-point. Different orderings of the sum give different results due to non-associativity. For reproducible distributed computing, you need either deterministic ordering or compensated summation. This is a real issue in distributed ML training where gradient aggregation order varies run to run.
