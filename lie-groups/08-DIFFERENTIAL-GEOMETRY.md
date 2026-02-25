# Lie Groups in Differential Geometry

## The Big Picture

Lie groups unify differential geometry and group theory. The key structures: principal bundles
(the geometric home of gauge fields), connections (the geometric home of gauge potentials),
curvature (the field strength tensor), and holonomy (the geometric source of Berry phase and
anholonomy in physics).

```
+----------------------------------------------------------------------+
|          LIE GROUPS IN DIFFERENTIAL GEOMETRY                         |
+----------------------------------------------------------------------+
|                                                                      |
|  BASE:          Spacetime M (smooth manifold, dim n)                 |
|                                                                      |
|  STRUCTURE:     Principal G-bundle  pi: P -> M                      |
|                 Fiber pi^{-1}(x) iso G  at each point x             |
|                                                                      |
|  CONNECTION:    Lie-algebra-valued 1-form  A in Omega^1(P, g)       |
|                 Splits tangent bundle TP = Horizontal + Vertical     |
|                 Horizontal lift: parallel transport along curves     |
|                                                                      |
|  CURVATURE:     F = dA + (1/2)[A,A] in Omega^2(P, g)               |
|                 Measures failure of horizontal lifts to commute      |
|                 = electromagnetic field strength F_{mu nu}           |
|                                                                      |
|  HOLONOMY:      For closed loop gamma in M:                          |
|                 Hol(A, gamma) in G                                   |
|                 = path-ordered exponential P exp(- integral A)       |
|                                                                      |
|  GAUGE TRANSFORM: Change of local trivialization of P               |
|                   A -> U A U^{-1} + U dU^{-1}                       |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## Lie Groups as Manifolds: Left-Invariant Structures

Every Lie group G is a smooth manifold. The group structure gives canonical geometric objects.

**Left translation:** L_g: G -> G, L_g(h) = gh. This is a diffeomorphism (smooth with smooth
inverse). Similarly right translation R_g: h |-> hg.

**Left-invariant vector fields:** A vector field X on G is left-invariant if:
```
(dL_g)_h X_h = X_{gh}  for all g, h in G
```
The space of left-invariant vector fields is isomorphic to T_e G = g (the Lie algebra).
Every left-invariant vector field is determined by its value at the identity.

**The Lie bracket of vector fields restricts to the Lie algebra bracket:**
[X,Y] (as vector fields) = [X_e, Y_e] (as algebra elements)

This is one route to defining the Lie algebra: as the algebra of left-invariant vector fields.

**Left-invariant metric:** A Riemannian metric on G is left-invariant if L_g^* <.,.>  = <.,.>.
Any inner product on g extends uniquely to a left-invariant metric on G. If also right-invariant
(bi-invariant), then G is a "compact" geometry.

**Bi-invariant metrics on compact groups:** Every compact Lie group admits a bi-invariant
Riemannian metric. Under this metric, geodesics through the identity are exactly the one-parameter
subgroups t |-> exp(tX). The Riemannian exponential map coincides with the Lie-theoretic
exponential map exp: g -> G.

---

## Principal G-Bundles

A **principal G-bundle** is a fiber bundle pi: P -> M where:
- The structure group is G (a Lie group)
- G acts on P freely and properly on the right: P x G -> P, (p,g) |-> p.g
- The quotient P/G = M (orbit space = base)
- Local trivialization: pi^{-1}(U) iso U x G for small open U subset M

```
PICTURE:

  P  (total space, dim = dim M + dim G)
  |
  pi  (projection, each fiber iso G)
  |
  M  (base space, dim n)

Locally: P|_U iso U x G
         (p, g) |-> (pi(p), g)   (local frame)
```

**Transition functions:** If {U_alpha} covers M and P|_{U_alpha} iso U_alpha x G, then on
overlaps U_alpha cap U_beta there are transition functions:
```
g_{alpha beta}: U_alpha cap U_beta -> G
```
satisfying the cocycle condition: g_{alpha beta} g_{beta gamma} = g_{alpha gamma}.

The principal bundle is classified (up to isomorphism) by the equivalence class of these
transition functions in H^1(M, G) (first Cech cohomology with G-coefficients).

**Associated vector bundles:** Given a representation rho: G -> GL(V), form the associated bundle:
```
E = P x_G V = (P x V) / {(p,v) ~ (pg, rho(g^{-1})v)}
```
Sections of E are fields in the representation rho. Quarks (in the 3-dim rep of SU(3)) are
sections of an associated bundle to the SU(3) principal bundle over spacetime.

---

## Connections on Principal Bundles

A **connection** on pi: P -> M is a G-equivariant splitting of the short exact sequence:
```
0 -> V(P) -> T(P) -> pi*T(M) -> 0
```
where V(P) = ker(dpi) is the vertical subbundle (tangent to fibers).

Equivalently, a connection is a Lie-algebra-valued 1-form:
```
A in Omega^1(P, g)
```
satisfying:
1. A(X_v) = X for all fundamental (vertical) vector fields X_v generated by X in g
2. R_g^* A = Ad_{g^{-1}} A (equivariance)

**Horizontal subspace:** At each p in P, the horizontal subspace is ker(A_p) subset T_p P.
The connection splits TP = H(P) + V(P).

**Parallel transport:** Given a curve gamma: [0,1] -> M, the horizontal lift is the unique
curve gamma_tilde: [0,1] -> P with pi(gamma_tilde) = gamma and gamma_tilde'(t) in H_{gamma_tilde(t)}.
Starting at p_0 in pi^{-1}(gamma(0)), the lift ends at a point p_1 in pi^{-1}(gamma(1)).
This defines the parallel transport map: tau_gamma: pi^{-1}(gamma(0)) -> pi^{-1}(gamma(1)).

**Local form (gauge field):** Choose a local section s: U -> P (a "gauge choice"). Then:
```
A_local = s^* A in Omega^1(U, g)
```
This is the Yang-Mills gauge field A_mu. Different gauge choices give different A_local related
by gauge transformations.

---

## Curvature

The **curvature** of a connection A is the Lie-algebra-valued 2-form:
```
F = dA + (1/2)[A, A] in Omega^2(P, g)
```
where [A,A] means: for vector fields X,Y, [A,A](X,Y) = [A(X), A(Y)] (Lie bracket in g).

**Local expression:** In a local gauge (choice of section), with A_mu = A_local:
```
F_{mu nu} = d_mu A_nu - d_nu A_mu + [A_mu, A_nu]
```
This is exactly the Yang-Mills field strength.

**Geometric meaning:** F measures the failure of horizontal distribution to be integrable
(Frobenius' theorem: a distribution is integrable iff its sections close under Lie bracket).
F = 0 everywhere iff the connection is flat (horizontal distribution is integrable).

**Bianchi identity:** Since F is the curvature of a connection:
```
DF = dF + [A, F] = 0   (Bianchi identity)
```
In components: D_[mu F_{nu rho]] = 0. This is the Jacobi identity for the covariant
derivative and is automatic — no extra equation.

**Chern-Weil theory:** The curvature form F can be used to construct characteristic classes —
closed differential forms on M whose de Rham cohomology classes are topological invariants of P.

Examples:
- First Chern class: c_1 = [tr(F/2pi)] in H^2(M, Z) (for U(1) bundle)
- Second Chern class: c_2 = [(1/8pi^2)(tr(F^2) - tr(F)^2)] in H^4(M, Z)
- Pontryagin class: p_1 = [-(1/8pi^2) tr(F^2)] in H^4(M, Z) (for real bundles)

These are cobordism invariants — they don't change under smooth deformation of the bundle.
The Chern-Simons form (the secondary characteristic class whose derivative gives c_2) appears
in Chern-Simons gauge theory (quantum Hall effect, topological field theories).

---

## Holonomy

**Definition:** For a closed loop gamma based at x in M, the parallel transport around gamma is
an element Hol(A, gamma) in G (in the fiber over x, which is a copy of G). This is the holonomy.

**Path-ordered exponential:** Concretely, for a curve gamma parameterized by t in [0,1]:
```
Hol(A, gamma) = P exp(-integral_0^1 A_mu gamma'(t) dt)
              = T exp(-integral_gamma A)
```
where T (or P) denotes time/path-ordering (because A_mu takes values in non-abelian g).

**Holonomy group:** The set of all holonomies at a point x forms a Lie subgroup of G called
the holonomy group Hol_x(A) subset G. By the Ambrose-Singer theorem:
```
Lie algebra of Hol_x(A) = span{ F(X,Y)_p : p accessible from x by horizontal path, X,Y in H_p P }
```
So F = 0 implies trivial holonomy (flat connection), as expected.

**Berger's classification (1955):** For an irreducible Riemannian manifold M, the holonomy
group Hol(M) of the Levi-Civita connection is one of:
```
SO(n)    : generic Riemannian manifold
U(n/2)   : Kahler manifold (complex structure)
SU(n/2)  : Calabi-Yau manifold (complex + parallel volume form)
Sp(n/4)  : Hyperkahler manifold (three Kahler structures)
Sp(n/4)*Sp(1): Quaternionic Kahler
G_2      : 7-manifold with G_2 holonomy (special Riemannian)
Spin(7)  : 8-manifold with Spin(7) holonomy
```
G_2 and Spin(7) holonomy manifolds appear in string theory compactifications. The compact G_2
manifolds (Joyce manifolds) give 4-dimensional N=1 supersymmetric compactifications of M-theory.

---

## The Maurer-Cartan Form

The **Maurer-Cartan form** is a canonical Lie-algebra-valued 1-form on G itself:
```
theta_MC = g^{-1} dg in Omega^1(G, g)
```
(For matrix groups, this is literally the matrix of 1-forms g^{-1} dg.)

**Properties:**
- Left-invariant: L_g^* theta_MC = theta_MC
- At the identity: theta_MC|_e = identity map T_e G = g -> g
- Satisfies the Maurer-Cartan equation: dtheta_MC + (1/2)[theta_MC, theta_MC] = 0

**Relation to connections:** The Maurer-Cartan form is the tautological connection on the
principal G-bundle G -> {pt} (the bundle over a point). More generally, a flat connection
on P is locally isomorphic to the Maurer-Cartan form.

**Wess-Zumino-Witten term:** In 2D conformal field theory, the WZW action includes a term:
```
(k/24pi^2) integral_{B} tr(g^{-1}dg wedge g^{-1}dg wedge g^{-1}dg)
```
where B is a 3-manifold with boundary Sigma_2, and this integral is the integral of the
Cartan 3-form (a bi-invariant 3-form on G defined by B(X,[Y,Z])). This term is topological and
quantized (the WZW level k must be an integer). The resulting 2D CFT has a current algebra
that is the loop algebra (affine Lie algebra) of g.

---

## Symmetric Spaces as G/K

A **Riemannian symmetric space** is a Riemannian manifold M such that at every point x, there
exists an isometry sigma_x with sigma_x(x) = x and d(sigma_x)_x = -I (geodesic reflection).

**Lie group realization:** Every symmetric space is a quotient M = G/K where:
- G is the isometry group (a Lie group)
- K = Stab(x_0) is the isotropy subgroup at a base point x_0 (compact)
- The pair (G,K) satisfies the symmetric pair conditions

```
Examples:
  Sphere S^n     = SO(n+1) / SO(n)
  Hyperbolic Hn  = SO(n,1) / SO(n)
  Complex proj Pn = SU(n+1) / U(n)
  Grassmannian   = U(n+k) / (U(n) x U(k))
  Siegel domain  = Sp(2n,R) / U(n)
```

**Cartan decomposition:** At the Lie algebra level, g = k + p where k = Lie(K) and p is the
orthogonal complement. The symmetric space condition says [k,p] subset p and [p,p] subset k.
The tangent space T_{x_0}M iso p.

---

## Decision Cheat Sheet

| Concept | Mathematical object | Physics name |
|---------|-------------------|--------------|
| Lie group G | Structure group | Gauge group |
| Principal G-bundle P -> M | Bundle over spacetime | Gauge bundle |
| Connection A on P | g-valued 1-form | Gauge potential A_mu |
| Curvature F of A | g-valued 2-form | Field strength F_{mu nu} |
| Local section s: U -> P | Gauge choice | Choice of gauge |
| Gauge transformation | Section change | Gauge transformation |
| Parallel transport | Horizontal lift | Parallel transport of matter field |
| Holonomy | Path-ordered exp | Wilson loop operator |
| Flat connection F=0 | Integrable distribution | Pure gauge: A = g dg^{-1} |
| Chern class | c_2 integral = instanton # | Topological charge |

---

## Common Confusion Points

**"A gauge transformation changes the physics":** No. A gauge transformation is a change of
description (choice of local trivialization). The physical observables are gauge-invariant
quantities: tr(F^{mu nu} F_{mu nu}), tr(Hol(A, gamma)) (Wilson loop), etc.

**"Parallel transport gives a path-ordered exponential because G is non-abelian":** Exactly.
For U(1) (electromagnetism), the gauge group is abelian, so parallel transport is exp(-i integral A_mu dx^mu).
For SU(3) (QCD), the gauge field takes values in su(3) and you need the path-ordered exponential
because [A_mu, A_nu] != 0.

**"The curvature formula has (1/2)[A,A] but Yang-Mills has [A_mu, A_nu]":** Both correct — different
notation. In the form notation: F = dA + (1/2)[A,A]. In components: F_{mu nu} = d_mu A_nu - d_nu A_mu + [A_mu, A_nu].
The factor of 1/2 absorbs into the antisymmetry of the 2-form.

**"Holonomy and curvature are related but different":** Yes. Curvature F is the infinitesimal version
(measures non-commutativity of infinitesimal parallel transport). Holonomy is the finite version
(actual group element from parallel transport around a loop). For small loops, Hol iso 1 + area * F.
The Ambrose-Singer theorem makes this precise globally.
