# Fiber Bundles

## The Big Picture

A fiber bundle is a space that locally looks like a product (base x fiber) but may be globally twisted. This is the mathematical language of gauge theories in physics and twisted vector spaces in geometry.

```
+------------------------------------------------------------------+
|                    FIBER BUNDLE  E -> M                          |
+------------------------------------------------------------------+
|                                                                  |
|    E (total space)                                              |
|    |                                                             |
|    pi (projection)                                              |
|    |                                                             |
|    M (base space)        F (fiber: pi^{-1}(p) ≅ F for each p)  |
|                                                                  |
|  LOCAL TRIVIALITY: for each p in M, there is an open U with    |
|  pi^{-1}(U) ≅ U x F  (homeomorphism commuting with pi)        |
|                                                                  |
|  TRANSITION FUNCTIONS: on overlaps U_alpha cap U_beta           |
|  phi_{beta alpha}: U_alpha cap U_beta -> Aut(F)                |
|  (tell you how to glue the fibers together)                    |
|                                                                  |
|  TYPES BY FIBER:                                                |
|  F = R^k: vector bundle (TM, T*M are examples)                 |
|  F = G (group): principal bundle                               |
|  F = any: general fiber bundle                                  |
+------------------------------------------------------------------+
```

---

## Formal Definition

A **fiber bundle** (E, pi, M, F) consists of:
- E: total space (smooth manifold)
- M: base space (smooth manifold)
- F: typical fiber (smooth manifold)
- pi: E -> M: projection map (smooth, surjective)
- Local trivializations: for each p in M, there is U_alpha containing p and a diffeomorphism:

```
  Phi_alpha: pi^{-1}(U_alpha) -> U_alpha x F

  such that Phi_alpha commutes with pi:
  pr_1 o Phi_alpha = pi  (first component of Phi_alpha = pi)
```

**Transition functions**: On overlaps U_alpha cap U_beta:

```
  phi_{beta alpha}(p): F -> F  for each p in U_alpha cap U_beta
  defined by: Phi_beta o Phi_alpha^{-1}(p, f) = (p, phi_{beta alpha}(p)(f))

  COCYCLE CONDITION:
  phi_{gamma beta}(p) o phi_{beta alpha}(p) = phi_{gamma alpha}(p)  on triple overlaps

  The transition functions ENCODE the bundle (determine it up to isomorphism).
  A bundle is trivial iff ALL transition functions can be taken to be the identity.
```

**Structure group**: If the transition functions phi_{beta alpha} take values in a subgroup G subset Diff(F), the bundle has **structure group G**. This is the relevant data for gauge theories.

---

## Vector Bundles

A **vector bundle** is a fiber bundle where F = R^k and transition functions are in GL(k,R):

```
  pi^{-1}(p) = E_p is a k-dimensional vector space for each p.

  EXAMPLES:
  Tangent bundle TM:     fiber = T_p M = R^n, structure group GL(n,R)
  Cotangent bundle T*M:  fiber = T*_p M, structure group GL(n,R)
  Normal bundle N(S,M):  fiber = (T_p M / T_p S) for S subset M
  Canonical line bundle:  over RP^n, fiber = each line through origin in R^{n+1}
  Tautological bundle:   over Gr(k,n), fiber = each k-plane in R^n

  TRIVIAL BUNDLE: E = M x R^k.
  Non-trivial: Mobius band = line bundle over S^1 with non-trivial transition function.
               Tangent bundle TS^2 (hairy ball theorem: no global section).
```

**Sections**: A section of E is a smooth map s: M -> E with pi o s = id_M. In other words, a smooth choice of element s(p) in the fiber over each p.

```
  Section of TM = vector field
  Section of T*M = differential 1-form
  Section of Lambda^k T*M = k-form
  Section of a trivial bundle = smooth function to R^k
```

**Characteristic classes**: Topological invariants of vector bundles:

```
  STIEFEL-WHITNEY CLASSES w_k(E) in H^k(M; Z_2)
  Obstruction to real orientability, spin structure.
  w_1 = 0 iff E is orientable; w_1 = w_2 = 0 iff E has spin structure.

  CHERN CLASSES c_k(E) in H^{2k}(M; Z)   for complex vector bundles E
  c_1 = first Chern class: obstructs triviality of complex line bundles.
  For Hermitian bundles: c_k represented by curvature form (Chern-Weil theory).

  PONTRYAGIN CLASSES p_k(E) in H^{4k}(M; Z)   for real bundles
  Appear in: signature theorem, Hirzebruch-Riemann-Roch theorem.
```

---

## Principal Bundles

A **principal G-bundle** is a fiber bundle P -> M with fiber G (the structure group) acting freely and transitively on each fiber:

```
  P has a smooth right G-action: P x G -> P,  (p, g) |-> p * g
  - Free: p * g = p implies g = e
  - Transitive on fibers: given p, q in pi^{-1}(x), there exists unique g with p * g = q
  - pi(p * g) = pi(p)  (G acts within fibers)

  EXAMPLES:
  Frame bundle FM: P = set of frames (bases) of T_p M, G = GL(n,R)
  Orthonormal frame bundle: G = O(n) (for Riemannian manifold)
  Hopf fibration: S^3 -> S^2 with fiber S^1 = U(1)  (principal U(1)-bundle)
  Principal SU(2)-bundle over S^4: important in gauge theory

  ASSOCIATED VECTOR BUNDLE:
  Given principal G-bundle P and representation rho: G -> GL(V):
  E = P x_G V = (P x V) / ((p,v) ~ (pg, rho(g^{-1})v))
  is a vector bundle with fiber V.

  TM comes from the frame bundle with the standard representation of GL(n,R).
```

---

## Connections on Principal Bundles

A **connection** on a principal G-bundle P -> M is a G-equivariant splitting of the tangent bundle TP into horizontal (H) and vertical (V) parts:

```
  TP = V TP + H TP    (vertical = along fibers, horizontal = complement)

  The vertical subspace V_e P = ker(d pi)_e (tangent to the fiber).
  The horizontal subspace H_e P is a complement specified by the connection.

  G-equivariance: d(R_g) maps H to H.

  CONNECTION FORM A: a Lie-algebra-valued 1-form A in Omega^1(P, g)
  A takes vertical vectors to their "generator" in g and
  vanishes on horizontal vectors.
  A(zeta_X) = X for all X in g  (zeta_X = fundamental vector field of X)
```

**Local connection form (gauge potential)**:

```
  Over a local trivialization U x G, the connection A restricts to:
  A|_U = A_mu dx^mu  (a g-valued 1-form on U)

  Under gauge transformation g: U -> G (change of trivialization):
  A -> g A g^{-1} + g^{-1} dg   (gauge transformation of the potential)

  This is EXACTLY the transformation law of gauge potentials in physics:
  For U(1): A_mu -> A_mu + partial_mu lambda  (electromagnetic gauge transform)
  For SU(n): A_mu -> U A_mu U^{-1} + U partial_mu U^{-1}  (non-abelian gauge transform)
```

**Curvature (field strength)**:

```
  F = dA + A wedge A   (curvature 2-form, g-valued)

  In physics notation: F_{mu nu} = partial_mu A_nu - partial_nu A_mu + [A_mu, A_nu]

  Bianchi identity: dF + A wedge F - F wedge A = 0   (DF = 0)
  In physics: D_mu F_{nu rho} + D_nu F_{rho mu} + D_rho F_{mu nu} = 0

  For U(1) (electromagnetism): [A_mu, A_nu] = 0 (abelian group)
  F_{mu nu} = partial_mu A_nu - partial_nu A_mu  (the electromagnetic tensor)
  Bianchi: partial_{[mu} F_{nu rho]} = 0  (Maxwell homogeneous equations)
```

---

## Gauge Theories and Physics

The Standard Model of particle physics is entirely about connections on principal bundles:

```
  ELECTROMAGNETISM (U(1) gauge theory):
  Principal bundle: P = principal U(1)-bundle over spacetime M^4
  Connection: A = electromagnetic vector potential A_mu dx^mu
  Curvature: F = dA  (electromagnetic field tensor F_{mu nu})
  Matter: sections of associated line bundle (charged fields)
  Action: S = Integral (-1/4) F_{mu nu} F^{mu nu} + J^mu A_mu  sqrt(-g) d^4x
  Maxwell equations: d*F = *J  (Hodge dual)

  YANG-MILLS THEORY (SU(n) gauge theory):
  Same structure with G = SU(2) [weak force] or SU(3) [strong force]
  Non-abelian: F = dA + A wedge A  (curvature includes A wedge A term)
  This term = self-interaction of gauge bosons (W/Z/gluons interact with themselves)

  Standard Model gauge group: U(1) x SU(2) x SU(3)
  Bundles: one for each factor, combined on spacetime.
```

**Yang-Mills equations**:

```
  D * F = * J   (Bianchi DF = 0 + Yang-Mills DF = 0 for vacuum)

  These are the Euler-Lagrange equations for the Yang-Mills action.
  For pure gauge theory (no matter): D * F = 0.
  Self-dual solutions: F = *F (instantons) -- topological solitons.

  Donaldson theory (1983): Geometry of self-dual Yang-Mills instantons on
  4-manifolds provides information about the topology of 4-manifolds.
  Led to exotic 4-manifolds and proved R^4 has exotic smooth structures.
```
**Donaldson theory — closing the loop to 01-MANIFOLDS**: The full chain connecting gauge theory to exotic smooth structures: (1) Start with an SU(2) principal bundle P over a smooth 4-manifold M. (2) Self-dual Yang-Mills connections (instantons) on P: F_A = *F_A (curvature equals its Hodge dual). (3) The moduli space M of instantons is a smooth manifold whose topology depends on the smooth structure of M. (4) Donaldson's polynomial invariants, defined by integrating cohomology classes over M, distinguish smooth structures. (5) Result: exotic R^4 (uncountably many smooth structures on a single topological R^4), and the smooth Poincare conjecture in dimension 4 remains open. This is the payoff: gauge physics (connections on principal bundles) provides the only known tool for probing smooth 4-manifold topology.

---

## Holonomy and Gauge Fields

The holonomy of a connection measures the failure of parallel transport around loops:

```
  For a loop gamma based at p in M:
  Hol_gamma: P_p -> P_p (parallel transport in the total space P)
  Since P_p ≅ G: Hol_gamma is an element of G.

  WILSON LINE / WILSON LOOP:
  W(gamma) = P exp(Integral_gamma A) in G   (path-ordered exponential)
  = holonomy of the gauge connection along gamma.

  AHARONOV-BOHM EFFECT: charged particle in magnetic field with
  non-simply-connected region. No local field, but non-trivial holonomy.
  Holonomy observable; force is not. This is the physical manifestation
  of the non-trivial topology of the bundle.
```

---

## Classification of Fiber Bundles

**Clutching construction**: Principal G-bundles over S^n are classified by:

```
  pi_{n-1}(G)  (homotopy classes of maps S^{n-1} -> G)

  This is the clutching construction: two trivial bundles on hemispheres,
  glued along the equator S^{n-1} by a transition function.

  Examples:
  U(1)-bundles over S^2: classified by Z = pi_1(U(1))
  = first Chern class = quantized magnetic charge (Dirac monopole)
  SU(2)-bundles over S^4: classified by Z = pi_3(SU(2))
  = instanton number = winding number

  CHERN-WEIL THEORY: Characteristic classes (Chern, Pontryagin) can be
  computed as integrals of curvature forms.
  For a principal U(1)-bundle: c_1 = (1/2pi) Integral_M F  (quantized!)
```

---

## Decision Cheat Sheet

| Bundle Type | Fiber | Structure Group | Key Application |
|---|---|---|---|
| Tangent bundle TM | R^n | GL(n,R) | Vector fields, geometry |
| Riemannian frame bundle | O(n) | O(n) | Orthonormal frames |
| Complex line bundle | C | U(1) | Electromagnetism |
| Principal SU(2)-bundle | SU(2) | SU(2) | Weak force, instantons |
| Principal SU(3)-bundle | SU(3) | SU(3) | Strong force (QCD) |
| Hopf fibration S^3 -> S^2 | S^1 | U(1) | Non-trivial topology |
| Tautological bundle over Gr(k,n) | R^k | GL(k,R) | K-theory, ML features |
| Spinor bundle | C^{2^{n/2}} | Spin(n) | Dirac equation, fermions |

---

## Common Confusion Points

**"A fiber bundle is the same as a product M x F."**
Only when the bundle is trivial. The Mobius band (non-trivial line bundle over S^1) is a fiber bundle E -> S^1 with fiber R, but E ≠ S^1 x R (the Mobius band is non-orientable; S^1 x R is orientable). The global twist is encoded in the transition functions.

**"A gauge transformation changes the physics."**
No — gauge transformations are changes of local trivializations (coordinate changes in the fiber direction). Physical observables (Wilson loops, field strengths) are gauge-invariant. Different gauge potentials A and A' = A + d_lambda give the same physical field F = dA = dA'.

**"Connections on principal bundles vs. connections on vector bundles."**
They are equivalent: a connection on a principal G-bundle P induces a connection (covariant derivative) on every associated vector bundle E = P x_G V. The Levi-Civita connection comes from a connection on the orthonormal frame bundle (principal O(n)-bundle). Gauge connections are connections on principal SU(n)-bundles.

**"The Chern class is a differential geometry invariant."**
Chern classes are topological invariants — they don't change when you smoothly deform the bundle. The Chern-Weil theorem says you can COMPUTE them using curvature (differential geometry), but the result is a topological invariant independent of the connection or metric used to compute it.

## Fiber Bundles and Equivariant Networks

A gauge-equivariant CNN is a neural network whose mathematical content is fiber bundle theory:

```
FIBER BUNDLE CONCEPT            EQUIVARIANT NETWORK EQUIVALENT
──────────────────────────────────────────────────────────────────────
Principal G-bundle P → M        Symmetry group G acting on the domain
Associated vector bundle E      Feature bundle (feature space at each point)
Section of E (s: M → E)         Feature map (assigns features to each point)
Connection on P                 Convolutional kernel (parallel transporter)
Parallel transport along γ      Message passing / feature aggregation
Gauge transformation            Change of local coordinate frame
Gauge equivariance              Network output independent of frame choice
Curvature of connection         Non-commutativity of feature transport

CONCRETE EXAMPLE (Cohen & Welling 2016, Weiler et al. 2018):
  M = pixel grid or point cloud.
  G = SO(2) for planar rotations, SE(3) for 3D rigid motions.
  Feature map = section of the associated bundle E = P ×_G V.
  Convolution kernel = G-equivariant map between fibers.
  The kernel must be an intertwiner: k(g·x) = ρ_out(g) k(x) ρ_in(g)^{-1}.
  This constraint (from representation theory) is what makes the
  network equivariant — it is the fiber bundle condition in disguise.
```

This is not an analogy. The gauge freedom in choosing local frames on M is exactly the coordinate freedom that equivariant networks are designed to be invariant under.
