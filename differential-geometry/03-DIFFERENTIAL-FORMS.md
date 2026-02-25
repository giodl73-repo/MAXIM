# Differential Forms

## The Big Picture

Differential forms are the correct objects to integrate on manifolds. The exterior derivative d unifies gradient, curl, and divergence into a single coordinate-free operator. Stokes' theorem unifies all classical integral theorems.

```
+------------------------------------------------------------------+
|                   DIFFERENTIAL FORMS LANDSCAPE                   |
+------------------------------------------------------------------+
|                                                                  |
|  ALGEBRA                                                         |
|  Lambda^0(M) = C^inf(M)          (functions)                    |
|  Lambda^1(M) = sections of T*M   (1-forms)                      |
|  Lambda^k(M) = sections of Lambda^k T*M  (k-forms)             |
|  Lambda^n(M)                      (n-forms, top dimension)      |
|                                                                  |
|  WEDGE PRODUCT: Alpha^k x Lambda^l -> Lambda^{k+l}             |
|  EXTERIOR DERIVATIVE: d: Lambda^k -> Lambda^{k+1}              |
|  d^2 = 0                          (key property)               |
|                                                                  |
|  STOKES' THEOREM:                                               |
|  Integral_M d omega = Integral_{partial M} omega                |
|                                                                  |
|  DE RHAM COHOMOLOGY:                                            |
|  H^k_dR(M) = ker(d: Lambda^k -> Lambda^{k+1}) /                |
|              im(d: Lambda^{k-1} -> Lambda^k)                    |
|  = closed forms / exact forms                                   |
|  Topological invariant of M.                                    |
+------------------------------------------------------------------+
```

---

## k-Forms: Definition

A **k-form** omega at a point p is a totally antisymmetric multilinear map:

```
  omega_p: T_p M x T_p M x ... x T_p M -> R   (k copies)
           (v_1, v_2, ..., v_k) |-> omega_p(v_1,...,v_k)

  Antisymmetry: omega_p(..., v_i, ..., v_j, ...) = -omega_p(..., v_j, ..., v_i, ...)
  Swapping any two arguments negates the result.
```

**In local coordinates**: With chart (x^1, ..., x^n):

```
  A basis for k-forms at p:  dx^{i_1} wedge dx^{i_2} wedge ... wedge dx^{i_k}
  for i_1 < i_2 < ... < i_k  (there are C(n,k) basis elements)

  General k-form:
  omega = Sum_{I} omega_I dx^{I}
  = Sum_{i_1 < ... < i_k} omega_{i_1...i_k} dx^{i_1} wedge ... wedge dx^{i_k}

  Special cases:
  k=0: functions
  k=1: omega = Sum_i omega_i dx^i     (covector field)
  k=n: omega = f dx^1 wedge ... wedge dx^n   (volume form, if f > 0)
  k > n: automatically 0 (not enough antisymmetric slots)
```

---

## Wedge Product

The **wedge (exterior) product** alpha wedge beta for alpha in Lambda^k, beta in Lambda^l is the alternating product:

```
  (alpha wedge beta)(v_1,...,v_{k+l}) = (1/(k!l!)) Sum_{sigma in S_{k+l}} sgn(sigma) alpha(v_{sigma(1)},...,v_{sigma(k)}) * beta(v_{sigma(k+1)},...,v_{sigma(k+l)})

  KEY PROPERTIES:
  alpha wedge beta = (-1)^{kl} beta wedge alpha     (graded-commutativity)
  (alpha wedge beta) wedge gamma = alpha wedge (beta wedge gamma)  (associativity)
  Distributes over addition.

  For 1-forms dx^i, dx^j:
  dx^i wedge dx^j = -dx^j wedge dx^i    (antisymmetry)
  dx^i wedge dx^i = 0

  Example in R^3:
  dx^1 wedge dx^2 is the "signed area" element in the x^1-x^2 plane.
  dx^1 wedge dx^2 wedge dx^3 is the signed volume element.
```

---

## Exterior Derivative

The **exterior derivative** d: Lambda^k(M) -> Lambda^{k+1}(M) is the unique linear operator satisfying:

```
  1. d(f) = df for functions f in Lambda^0  (usual differential)
  2. d o d = 0  (d^2 = 0)
  3. d(alpha wedge beta) = (d alpha) wedge beta + (-1)^k alpha wedge (d beta)
     (graded Leibniz rule)

  In local coordinates for omega = Sum_I omega_I dx^I in Lambda^k:
  d omega = Sum_I d(omega_I) wedge dx^I
  = Sum_I Sum_j (partial omega_I / partial x^j) dx^j wedge dx^I

  Examples in R^3:
  f in Lambda^0:   df = (partial_1 f) dx + (partial_2 f) dy + (partial_3 f) dz
                   = gradient (as a 1-form)

  F = P dx + Q dy + R dz in Lambda^1:
  dF = (partial_y P - partial_x Q) dx wedge dy + (...)   cyclically
     = curl of the vector field (P,Q,R)  (as a 2-form)

  G = P dy wedge dz + Q dz wedge dx + R dx wedge dy in Lambda^2:
  dG = (partial_x P + partial_y Q + partial_z R) dx wedge dy wedge dz
     = divergence (as a 3-form / volume form)
```

**Unification**: The exterior derivative d unifies grad, curl, div. The classical theorems (Gradient theorem, Stokes, Gauss) all become one theorem: Integral_M d omega = Integral_{partial M} omega.

**d^2 = 0**: This is the algebraic engine behind de Rham cohomology and gauge theories. For vector calculus: curl(grad f) = 0 and div(curl F) = 0 are special cases.

---

## Interior Product and Cartan's Formula

The **interior product** i_X omega for a vector field X and k-form omega:

```
  (i_X omega)(v_2, ..., v_k) = omega(X, v_2, ..., v_k)
  (plug X into the first slot)

  i_X: Lambda^k -> Lambda^{k-1}  (decreases degree by 1)
  i_X o i_X = 0  (inserting same vector twice is antisymmetric = 0)
```

**Cartan's magic formula** (relating Lie derivative to d and i):

```
  L_X = d o i_X + i_X o d   (on differential forms)

  This is a "homotopy" relation: L_X is exact up to homotopy.
  Consequence: L_X preserves closed forms (if d omega = 0, then d(L_X omega) = 0).
```

---

## Integration of Differential Forms

The fundamental reason k-forms are the right things to integrate:

```
  A n-form on an oriented n-manifold M is integrable:
  Integral_M omega  (for omega in Lambda^n(M))

  LOCAL COMPUTATION in chart (U, phi = (x^1,...,x^n)):
  omega|_U = f(x) dx^1 wedge ... wedge dx^n
  Integral_U omega = Integral_{phi(U)} f(x) dx^1 ... dx^n  (Lebesgue integral in R^n)

  CHANGE OF VARIABLES: The antisymmetry of the wedge product encodes
  the Jacobian determinant in change of variables automatically:
  phi*(omega) = f(phi(x)) det(J_phi) dx^1 wedge ... wedge dx^n
  This is why forms are the natural objects to integrate — orientation and
  volume change are built in.
```

**Integration of k-forms on k-dimensional submanifolds**: If S is a k-dimensional oriented submanifold of M and omega in Lambda^k(M):

```
  Integral_S omega = Integral_S i* omega
  where i: S -> M is the inclusion map and i* is pullback.

  Work in coordinates on S and compute the pullback.
```

---

## Stokes' Theorem

The master theorem:

```
  For omega in Lambda^{n-1}(M) with compact support and M an oriented n-manifold with boundary:

  Integral_M d omega = Integral_{partial M} omega

  The boundary partial M inherits the induced orientation from M.
  If partial M = emptyset (closed manifold): Integral_M d omega = 0.
```

**Classical theorems as special cases**:

```
  FUNDAMENTAL THEOREM OF CALCULUS:
  M = [a,b], omega = f (0-form), d omega = f' dx.
  Integral_[a,b] f' dx = f(b) - f(a) = Integral_{partial [a,b]} f.  ✓

  GRADIENT THEOREM (line integral):
  M = curve C, omega = f (0-form), d omega = df.
  Integral_C grad f · dr = f(end) - f(start).  ✓

  CLASSICAL STOKES' THEOREM:
  M = surface S with boundary curve C in R^3.
  omega = F · dr (1-form from vector field F).
  d omega = curl(F) · dS (2-form).
  Integral_S curl(F) · dS = Integral_C F · dr.  ✓

  GAUSS' THEOREM (DIVERGENCE THEOREM):
  M = volume V in R^3, partial M = surface S.
  omega = F · dS (2-form).
  d omega = div(F) dx wedge dy wedge dz.
  Integral_V div(F) dV = Integral_S F · n dS.  ✓
```

---

## de Rham Cohomology

**Closed forms**: omega with d omega = 0.
**Exact forms**: omega with omega = d eta for some eta.

Every exact form is closed (d^2 = 0 implies d(d eta) = 0). The converse is Poincaré's lemma — it holds locally but not globally:

```
  Poincaré's lemma: On any contractible open set U:
  Every closed k-form on U is exact.

  GLOBAL OBSTRUCTION: A closed form may not be exact if M has topological holes.
  Classic example: 1/r^2 force in R^2 - {0}:
  omega = (-y dx + x dy) / (x^2 + y^2)  is closed but NOT exact.
  Integral around the origin = 2 pi  (non-zero integral -> not exact).
```

**de Rham cohomology groups**:

```
  H^k_dR(M) = Z^k(M) / B^k(M)
  where Z^k = closed k-forms, B^k = exact k-forms

  These are vector spaces (coefficients in R).
  Dimensions: b_k = dim H^k_dR(M) = k-th Betti number

  de Rham's theorem: H^k_dR(M) is isomorphic to singular cohomology H^k(M; R).
  TOPOLOGY ENCODED IN ANALYSIS: The topology of M (holes, handles) is
  detected by whether closed forms are exact.
```

**Examples**:

```
  R^n: H^0 = R, H^k = 0 for k > 0  (contractible, no holes)
  S^n: H^0 = R, H^n = R, H^k = 0 otherwise  (one n-sphere shell)
  T^2: H^0 = R, H^1 = R^2, H^2 = R  (torus has two 1-cycles)
```

---

## Hodge Theory (Riemannian Setting)

On a Riemannian manifold (M, g), the Hodge star operator provides an isomorphism between k-forms and (n-k)-forms:

```
  Hodge star: *: Lambda^k -> Lambda^{n-k}

  Defined by: alpha wedge (*beta) = g(alpha, beta) Vol_M  for alpha, beta in Lambda^k
  where Vol_M = sqrt(det g) dx^1 wedge ... wedge dx^n is the volume form.

  **: Lambda^k -> Lambda^k  with **omega = (-1)^{k(n-k)} omega

  The Hodge Laplacian: Delta = d d* + d* d  where d* = (-1)^{...} * d *
  This is the correct Laplacian on forms.
  On functions: Delta f = -div(grad f) = -(Sum_i partial_i^2 f) in R^n
```

**Hodge decomposition theorem** (compact orientable Riemannian manifold):

```
  Lambda^k(M) = d Lambda^{k-1} + d* Lambda^{k+1} + H^k

  Where H^k = harmonic k-forms (Delta omega = 0).
  Each cohomology class has a unique harmonic representative.
  H^k_dR(M) is isomorphic to H^k (harmonic forms).
```

This connects topology (cohomology) to analysis (harmonic functions). Harmonic forms on compact manifolds are the topologically "essential" directions in the space of forms.

---

## Decision Cheat Sheet

| Object/Operation | What It Is | Use |
|---|---|---|
| k-form omega | Antisymmetric (0,k) tensor field | Integrand on k-dimensional submanifold |
| Wedge product wedge | Antisymmetric tensor product | Build k-forms from 1-forms |
| Exterior derivative d | d: Lambda^k -> Lambda^{k+1} | Unifies grad/curl/div |
| Interior product i_X | Lambda^k -> Lambda^{k-1} | Contract vector into form |
| Lie derivative L_X | Lambda^k -> Lambda^k | Form variation along flow |
| Stokes' theorem | Int d omega = Int_{boundary} omega | Unifies all classical theorems |
| Closed form | d omega = 0 | Locally exact; globally may not be |
| Exact form | omega = d eta | Integrals around closed curves = 0 |
| de Rham cohomology H^k | Closed / Exact forms | Topological invariant |
| Hodge star * | Lambda^k -> Lambda^{n-k} | Inner product on forms, Laplacian |

---

## Common Confusion Points

**"d^2 = 0 is just a computation result."**
It is the algebraic heart of the theory. From it follows: exact forms are closed (without computing anything), curl(grad) = 0, div(curl) = 0, Bianchi identity in GR (d of Riemann tensor = 0 symbolically). In gauge theories, the field strength F = dA is automatically closed: dF = d^2 A = 0.

**"A closed 1-form defines a function up to a constant."**
Only on simply connected spaces. On M with non-trivial first fundamental group, a closed form may have non-zero integrals around non-contractible loops. The obstruction is H^1_dR(M). The example omega = d(theta) on S^1 is closed but not exact (integral around the circle = 2pi).

**"The wedge product is just the tensor product."**
The tensor product alpha tensor beta is a (0,k+l) tensor that is neither symmetric nor antisymmetric. The wedge product is the antisymmetrized tensor product. The difference matters: tensor products don't have the d^2 = 0 property; exterior products do.

**"Integration of k-forms is just multi-dimensional integration."**
The pullback mechanism is more subtle. When you integrate a k-form on a k-dimensional manifold, the change-of-variables formula with the Jacobian determinant is encoded in the antisymmetry of the form. This is why forms are the natural integrands and why there is no "volume form" needed separately — the form IS the integrand, and its behavior under coordinate change is correct by construction.
