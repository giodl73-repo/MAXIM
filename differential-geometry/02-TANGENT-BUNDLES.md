# Tangent and Cotangent Bundles

## The Big Picture

The tangent bundle TM packages all tangent spaces into one smooth manifold. Sections of TM are vector fields; sections of T*M are differential forms. Tensor fields are sections of higher tensor products.

```
+------------------------------------------------------------------+
|                    BUNDLE HIERARCHY                              |
+------------------------------------------------------------------+
|                                                                  |
|  M (base manifold, dim n)                                       |
|  |                                                               |
|  +--> TM  (tangent bundle)         sections = vector fields     |
|  |    Each fiber T_p M = R^n                                    |
|  |                                                               |
|  +--> T*M (cotangent bundle)       sections = 1-forms           |
|  |    Each fiber T*_p M = (T_p M)* = dual space                 |
|  |                                                               |
|  +--> T^r_s M (tensor bundle)      sections = (r,s) tensor fields|
|  |    r contravariant, s covariant indices                      |
|  |                                                               |
|  +--> Sym^2 T*M                    sections = Riemannian metrics |
|  |                                                               |
|  +--> Lambda^k T*M                 sections = k-forms           |
|       (totally antisymmetric)                                   |
+------------------------------------------------------------------+
```

---

## Tangent Bundle TM

**Definition**: TM = Union_{p in M} T_p M (disjoint union of all tangent spaces).

```
  TM has a natural smooth manifold structure of dimension 2n:
  - If (U, phi = (x^1, ..., x^n)) is a chart on M
  - The induced chart on TM is:
    (U x R^n, (x^1,...,x^n, v^1,...,v^n))
    where v^i = components of tangent vector in the x^i basis

  Projection: pi: TM -> M,  pi(p, v) = p

  A smooth map F: M -> N induces a pushforward:
  dF (or F_*): TM -> TN
  At p: dF_p: T_p M -> T_{F(p)} N
  In coordinates: (dF_p)^i_j = partial F^i / partial x^j
```

**Vector bundle structure**: TM is a vector bundle — each fiber T_p M is a vector space, and the bundle structure is locally trivial:

```
  Local trivialization: TM|_U ≅ U x R^n   (over each chart domain U)

  These trivializations glue together with transition functions:
  If (U, phi) and (V, psi) are charts on M with U cap V != emptyset:
  Transition function g_{UV}: U cap V -> GL(n,R)
  g_{UV}(p) = d(psi o phi^{-1})_{phi(p)}  (Jacobian of transition map)
```

---

## Vector Fields

A **vector field** X on M is a smooth section of TM:

```
  X: M -> TM  with pi o X = id_M
  (assigns to each point a tangent vector at that point)

  In local coordinates: X = Sum_i X^i(x) partial/partial x^i
  where X^i: U -> R are smooth functions.

  OPERATIONS:

  Pointwise: (X + Y)_p = X_p + Y_p, (fX)_p = f(p) X_p

  Lie bracket (commutator):
  [X, Y] = X o Y - Y o X    (as derivations on C^inf(M))
  In coordinates: [X,Y]^i = Sum_j (X^j partial_j Y^i - Y^j partial_j X^i)

  The Lie bracket measures failure of X and Y to commute.
  Key identity: [X,Y] is again a vector field. (Lie algebra structure!)
```

**Integral curves and flows**:

```
  An integral curve of X through p: smooth gamma: (-eps,eps) -> M with
  gamma(0) = p, gamma'(t) = X_{gamma(t)}  for all t.
  This is an ODE: existence and uniqueness by Picard-Lindelof.

  Flow of X: phi_t: M -> M defined by phi_t(p) = gamma_p(t)
  phi_0 = id, phi_{s+t} = phi_s o phi_t  (group property)

  If X is complete (integral curves exist for all t in R):
  {phi_t} is a one-parameter group of diffeomorphisms.
```

---

## Cotangent Bundle T*M and 1-Forms

**Cotangent space** T*_p M = (T_p M)* = space of linear functionals on T_p M.

**Dual basis**: If {partial/partial x^i} is a basis of T_p M, the dual basis {dx^i} of T*_p M satisfies:

```
  dx^i (partial/partial x^j) = delta^i_j  (Kronecker delta)

  A general 1-form (covector) at p: omega_p = Sum_i a_i(p) dx^i
  Evaluation: omega_p(v) = Sum_i a_i(p) v^i   (a number)
```

**T*M**: the cotangent bundle — the disjoint union of all cotangent spaces, a smooth 2n-dimensional manifold.

**Differential of a function**: For smooth f: M -> R:

```
  df: M -> T*M
  df_p: T_p M -> R  defined by  df_p(v) = v(f)  (directional derivative)

  In coordinates: df = Sum_i (partial f / partial x^i) dx^i

  This is the EXACT 1-form associated to f.
  Key: df is coordinate-independent; the partial derivatives alone are not.

  Pullback: for F: M -> N smooth and omega in Omega^1(N):
  F* omega in Omega^1(M) defined by (F*omega)_p(v) = omega_{F(p)}(dF_p(v))
```

---

## Tensor Fields

A **(r, s) tensor field** is a smooth section of T^r_s M = TM^{tensor r} tensor T*M^{tensor s}:

```
  (r,s) tensor T at p: multilinear map
  T_p: T*_p M x ... x T*_p M x T_p M x ... x T_p M -> R
              r times                   s times

  Alternatively: a (0,0) tensor = function; (1,0) = vector field; (0,1) = 1-form.

  Transformation law in coordinates:
  T^{i_1...i_r}_{j_1...j_s}(new) = T^{k_1...k_r}_{l_1...l_s}(old)
    * (partial x^{i_1}_new / partial x^{k_1}_old) ...
    * (partial x^{l_1}_old / partial x^{j_1}_new) ...

  r upstairs (contravariant) indices transform with the Jacobian.
  s downstairs (covariant) indices transform with the inverse Jacobian.
```

**Important (0,2) tensor fields**:

```
  Metric tensor g:   g(X,Y) = inner product of X and Y    (symmetric, positive-definite)
  Symplectic form omega: omega(X,Y) = signed area          (antisymmetric, non-degenerate)

  g and omega are the geometric structures added to a smooth manifold.
  Riemannian: + g.  Symplectic (Hamiltonian mechanics): + omega.
```
**Symplectic structure on T*Q — phase space**: The cotangent bundle T*Q of any manifold Q carries a canonical symplectic form. The tautological 1-form is λ = p_i dq^i (in local coordinates (q^i, p_i) on T*Q), and the symplectic form is ω = dλ = dp_i ∧ dq^i. This ω is closed (dω = 0) and non-degenerate (ω^n ≠ 0), making T*Q a symplectic manifold. The non-degeneracy defines a musical isomorphism ω♭: TM → T*M (different from the Riemannian g♭) that converts the gradient of the Hamiltonian H into the Hamiltonian vector field X_H: ω(X_H, ·) = dH. Hamilton's equations q̇ = ∂H/∂p, ṗ = −∂H/∂q are exactly the flow of X_H. This is the geometric formulation of classical mechanics; symplectic integrators in 09-APPLICATIONS preserve ω numerically.

---

## Pullback and Pushforward

The fundamental operations on tangent/cotangent objects:

```
  For F: M -> N:

  PUSHFORWARD (F_* or dF): TM -> TN
  Moves tangent vectors FORWARD along F.
  (F_* X)_{F(p)} = dF_p(X_p)

  PULLBACK (F*): T*N -> T*M  (and more generally: differential forms)
  Moves covectors and forms BACKWARD along F.
  (F* omega)_p(v) = omega_{F(p)}(dF_p(v))

  KEY ASYMMETRY:
  - Pushforward works for vectors (needs F to be smooth, no injectivity needed)
  - Pullback always works for forms (no restrictions on F)
  - Pushforward of vector FIELDS requires F to be a diffeomorphism
    (to push the FIELD: need unique preimage for each point)

  The exterior derivative d COMMUTES with pullback:
  d(F* omega) = F*(d omega)
  This is the naturality of d.
```

---

## Lie Derivative

The Lie derivative measures how a tensor field changes along the flow of a vector field:

```
  L_X T = lim_{t->0} (phi_t* T - T) / t

  where phi_t is the flow of X.

  For functions: L_X f = X(f) = df(X)  (directional derivative)

  For vector fields: L_X Y = [X, Y]  (Lie bracket!)

  For 1-forms (Cartan's magic formula):
  L_X omega = d(i_X omega) + i_X (d omega)

  where i_X omega = interior product = omega(X, -)  (contraction with X)

  The Lie derivative encodes the "active" perspective: how the tensor
  changes as you drag it along the flow of X.
  The covariant derivative (05) encodes the "passive" perspective:
  how the tensor changes direction in a fixed space.
```

---

## The Musical Isomorphisms

A Riemannian metric g provides a canonical isomorphism between TM and T*M:

```
  FLAT  (index lowering, "b"):  TM -> T*M
  X^b(Y) = g(X, Y)   for all Y
  In coordinates: X_i = Sum_j g_{ij} X^j   (lower index with g)

  SHARP (index raising, "sharp"):  T*M -> TM
  (omega^sharp) = g^{-1} omega
  In coordinates: omega^i = Sum_j g^{ij} omega_j  (raise index with g^{ij})

  Without a metric, TM and T*M are NOT naturally isomorphic!
  In classical mechanics: position q in T*Q (cotangent bundle = phase space),
  momentum p is a covector. The metric (kinetic energy tensor) is needed
  to identify momentum with velocity.
```

---

## Frame Bundle and G-Structures

A global concept unifying the bundle perspective:

```
  FRAME BUNDLE FM:
  At each p in M, the fiber is the set of all ordered bases of T_p M.
  GL(n,R) acts freely and transitively on each fiber (changing basis).
  FM is a principal GL(n,R)-bundle over M.

  G-STRUCTURES: A G-structure is a reduction of the frame bundle to
  a principal G-bundle (G subset GL(n,R)).

  Examples:
  O(n)-structure:    Riemannian metric (orthonormal frames)
  SO(n)-structure:   Riemannian metric + orientation
  Sp(2n,R)-structure: Symplectic structure
  U(n)-structure:    Almost complex structure (+ compatibility)
  {e}-structure:     Parallelization (global frame field)
```

This connects to fiber bundles (08) — a Riemannian metric is exactly an O(n)-reduction of the frame bundle.

**Frame bundle → equivariant neural networks**: A G-equivariant neural network on a manifold is precisely a network that respects a G-structure on the feature bundle. In gauge-equivariant CNNs (Cohen et al. 2019), feature maps are sections of an associated vector bundle E = F(M) ×_G V, where F(M) is the frame bundle and V is a representation of G. The convolutional kernel is a parallel transport operator (connection on E), and gauge equivariance means the output is independent of the local frame choice (local trivialization). The Stiefel manifold St(k,n) of orthonormal k-frames in R^n appears directly as the parameter space for orthogonal weight matrices in these architectures. This is not an analogy — it is the literal mathematical content of geometric deep learning. Full treatment in 09-APPLICATIONS.

---

## Decision Cheat Sheet

| Object | Definition | Acts On | Section Is |
|---|---|---|---|
| TM (tangent bundle) | Union of T_p M | — | Vector field |
| T*M (cotangent bundle) | Union of T*_p M | — | 1-form |
| T^{1,0}M | = TM | — | Vector field |
| T^{0,1}M | = T*M | — | 1-form |
| T^{r,s}M | r up, s down | Vectors and covectors | (r,s)-tensor field |
| Lambda^k T*M | Antisym (0,k) | k tangent vectors | k-form |
| Sym^2 T*M | Symm (0,2) | Pairs of vectors | Symmetric bilinear form |
| Pushforward dF | TM -> TN | Vectors forward | — |
| Pullback F* | Omega^k(N) -> Omega^k(M) | Forms backward | — |
| Lie derivative L_X | Tensors -> Tensors | Along flow of X | — |

---

## Common Confusion Points

**"The tangent bundle TM = M x R^n."**
Only locally (over each chart). Globally, TM may be non-trivial — the fibers are twisted together. Example: TS^2 (tangent bundle of the 2-sphere) is non-trivial — you cannot find a nowhere-vanishing vector field on S^2 (hairy ball theorem). TS^1 and TS^3 are trivial (you can parallelize S^1 and S^3).

**"The differential df and the gradient of f are the same thing."**
df is a 1-form (a cotangent vector field) — it is coordinate-free. The gradient grad f is a tangent vector field, obtained by applying the musical isomorphism (raising df with the metric): grad f = (df)^sharp. Without a metric, there is no gradient, only a differential.

**"Pushforward and pullback are just transpose of each other."**
Not quite. Pullback F*: T*N -> T*M goes backwards; pushforward dF: TM -> TN goes forwards. They are "dual" in the sense that F*(omega)(v) = omega(dF(v)), but they map between different spaces. The asymmetry — that pullback always works for forms but pushforward requires a diffeomorphism for vector fields — is geometrically meaningful.

**"Contravariant and covariant are just old terminology."**
They encode transformation behavior under coordinate changes, which is fundamental. Objects with upstairs indices (contravariant, vectors) transform with the Jacobian; objects with downstairs indices (covariant, forms) transform with the inverse Jacobian. This distinction is not terminological — it tells you whether the object "goes with" or "goes against" the coordinate change.
