# Lie Groups and Lie Algebras

## The Big Picture

A Lie group is simultaneously a smooth manifold and a group, with the two structures compatible. Lie algebras are their linearizations at the identity. Lie groups are the mathematical home of continuous symmetry.

```
+------------------------------------------------------------------+
|                    LIE GROUPS OVERVIEW                           |
+------------------------------------------------------------------+
|                                                                  |
|  LIE GROUP G                                                     |
|  = Smooth manifold M                                             |
|  + Group structure (G, *, e)                                    |
|  + Compatibility: multiplication and inversion are smooth       |
|                                                                  |
|  LINEARIZATION: Lie algebra g = T_e G                          |
|                                                                  |
|  EXPONENTIAL MAP: exp: g -> G                                   |
|  Connects Lie algebra (linear) to Lie group (nonlinear)        |
|                                                                  |
|  KEY EXAMPLES:                                                   |
|  +-----------+--------+--------+---------------------------+    |
|  | Group     | dim    | Field  | Geometry/Physics          |    |
|  +-----------+--------+--------+---------------------------+    |
|  | GL(n,R)   | n^2    | R      | Invertible linear maps    |    |
|  | SL(n,R)   | n^2-1  | R      | Volume-preserving         |    |
|  | O(n)      | n(n-1)/2| R     | Orthogonal transformations|    |
|  | SO(n)     | n(n-1)/2| R     | Rotations in R^n          |    |
|  | U(n)      | n^2    | C      | Unitary transformations   |    |
|  | SU(n)     | n^2-1  | C      | Special unitary           |    |
|  | SE(3)     | 6      | R      | Rigid body motions in R^3 |    |
|  | SO(3,1)   | 6      | R      | Lorentz group (spacetime) |    |
|  +-----------+--------+--------+---------------------------+    |
+------------------------------------------------------------------+
```

---

## Definition and Basic Structure

A **Lie group** G is a smooth manifold with:
- Group structure: binary operation * and identity e
- Smooth operations: multiplication (g,h) |-> g*h and inversion g |-> g^{-1} are smooth maps

```
  IMMEDIATE CONSEQUENCES:
  Left translation L_g: G -> G, L_g(h) = g*h  (smooth diffeomorphism)
  Right translation R_g: G -> G, R_g(h) = h*g  (smooth diffeomorphism)
  Conjugation C_g: G -> G, C_g(h) = g h g^{-1}  (smooth diffeomorphism)

  Left-invariant vector fields:
  A vector field X on G is left-invariant if (L_g)_* X = X for all g.
  i.e., d(L_g)_e X_e = X_g  for all g.

  Key: A left-invariant vector field is determined by its value at e.
  So: {left-invariant vector fields} is isomorphic to T_e G as vector spaces.
```

---

## The Lie Algebra

The **Lie algebra** g = T_e G is the tangent space at the identity, equipped with the Lie bracket:

```
  For X, Y in T_e G: extend to left-invariant vector fields X_bar, Y_bar.
  Define: [X, Y] = [X_bar, Y_bar]_e  (Lie bracket of vector fields, evaluated at e)

  Properties of the Lie bracket:
  [X, Y] = -[Y, X]               (antisymmetry)
  [[X,Y],Z] + [[Y,Z],X] + [[Z,X],Y] = 0   (Jacobi identity)
  [aX + bY, Z] = a[X,Z] + b[Y,Z]            (bilinearity)

  The Lie algebra is a "first-order approximation" to the group structure.
  The Baker-Campbell-Hausdorff formula recovers the group from the algebra:
  exp(X) exp(Y) = exp(X + Y + (1/2)[X,Y] + (1/12)[[X,Y],Y] - ... )
```

**Concrete Lie algebras**:

```
  GL(n,R): gl(n,R) = Mn(R)  (all n x n matrices, bracket = commutator [A,B] = AB - BA)
  SL(n,R): sl(n,R) = {A: tr A = 0}  (traceless matrices)
  O(n):    o(n)    = {A: A + A^T = 0}  (antisymmetric matrices)
  SO(n):   so(n)   = o(n)  (same; SO(n) and O(n) have the same Lie algebra)
  U(n):    u(n)    = {A: A + A^* = 0}  (skew-Hermitian matrices)
  SU(n):   su(n)   = {A: A + A^* = 0, tr A = 0}  (traceless skew-Hermitian)
```

---

## The Exponential Map

The exponential map exp: g -> G sends tangent vectors at e to group elements:

```
  exp(X) = gamma_X(1)

  where gamma_X: R -> G is the unique one-parameter subgroup with gamma'_X(0) = X.
  (A one-parameter subgroup satisfies gamma(s+t) = gamma(s) gamma(t).)

  KEY PROPERTIES:
  gamma_X(t) = exp(tX)               (one-parameter subgroup)
  exp(0) = e                         (identity)
  exp(-X) = exp(X)^{-1}              (inverse)
  exp((s+t)X) = exp(sX) exp(tX)      (group homomorphism along X)
  d/dt exp(tX)|_{t=0} = X            (derivative at identity = X)

  For matrix groups: exp(A) = Sum_{k=0}^inf A^k / k!   (matrix exponential)
  This is NOT a coincidence: one-parameter subgroups of GL(n,R) are exactly
  curves t |-> exp(tA) for matrix A.
```

**Surjectivity**: exp is a local diffeomorphism near 0 in g. For compact, connected G, exp is surjective. For non-compact G, exp need not be surjective (e.g., SL(2,R)).

---

## SO(3): The Rotation Group

The most important Lie group for mechanics and robotics:

```
  SO(3) = {A in M_3(R): A^T A = I, det A = +1}
  dim = 3,  Lie algebra so(3) = {antisymmetric 3x3 matrices}

  PARAMETERIZATIONS:
  1. Rotation matrices (3x3): good for composition, bad for interpolation
  2. Euler angles (phi, theta, psi): intuitive, but GIMBAL LOCK at singularities
  3. Axis-angle: R = exp(theta * k_hat) where k_hat = unit axis, theta = angle
  4. Quaternions: unit quaternions in R^4 = SU(2) -- double cover of SO(3)

  LIE ALGEBRA so(3):
  Basis: e_1 = [0 0 0; 0 0 -1; 0 1 0], e_2 = [0 0 1; 0 0 0; -1 0 0], e_3 = [0 -1 0; 1 0 0; 0 0 0]

  [e_1, e_2] = e_3,  [e_2, e_3] = e_1,  [e_3, e_1] = e_2
  Isomorphic to (R^3, x) where x = cross product! (so(3) iso (R^3, x))

  EXPONENTIAL MAP for SO(3) (Rodrigues' formula):
  exp(theta * k_hat_x) = I + sin(theta) k_hat_x + (1-cos theta) k_hat_x^2
  where k_hat_x = antisymmetric matrix of k_hat (the "hat map")
```

**SU(2) is the universal cover of SO(3)**:

```
  SU(2) = {[a, -b_bar; b, a_bar]: |a|^2 + |b|^2 = 1} (unit quaternions as 2x2 matrices)
  dim = 3, simply connected.

  Covering map: SU(2) -> SO(3) with kernel {+I, -I} (Z_2)
  So SO(3) = SU(2) / Z_2.
  This is the spinor phenomenon: a 2pi rotation = -I in SU(2) (not the identity!).
  A 4pi rotation returns to identity. Electrons (spin-1/2) "see" this.
```

---

## SE(3): The Special Euclidean Group

Rigid body motions (rotations + translations) in 3D:

```
  SE(3) = SO(3) semi-direct product R^3

  Elements: (R, t) where R in SO(3), t in R^3
  Action: (R, t) * x = Rx + t   (rotate then translate)
  Composition: (R1, t1) * (R2, t2) = (R1 R2, R1 t2 + t1)
  Identity: (I, 0)
  Inverse: (R, t)^{-1} = (R^T, -R^T t)

  4x4 HOMOGENEOUS MATRIX REPRESENTATION:
  g = [R  t; 0  1]  in GL(4,R)
  Points: [x; 1] in R^4  (homogeneous coordinates)
  g [x; 1] = [Rx + t; 1]

  LIE ALGEBRA se(3):
  Xi = [omega_x  v; 0  0]   where omega in R^3 (angular velocity), v in R^3 (linear velocity)
  dim se(3) = 6 (3 rotational + 3 translational DOF)
```

**Application to robotics**: Robot joint configurations live in SE(3). A rigid body has 6 DOF. The exponential map gives the group element (pose) from the Lie algebra element (twist velocity).

---

## Adjoint Representation and Killing Form

**Adjoint representation**: The group acts on its Lie algebra by conjugation:

```
  Ad: G -> GL(g)   (a representation of G on g)
  Ad_g(X) = d/dt C_g(exp(tX))|_{t=0}
           = d(C_g)_e X        (pushforward of conjugation map)

  For matrix groups: Ad_g(X) = g X g^{-1}

  The adjoint action is the "infinitesimal" version:
  ad: g -> End(g)
  ad_X(Y) = [X, Y]   (the Lie bracket IS the adjoint of the Lie algebra)
```

**Killing form**: A symmetric bilinear form on g:

```
  B(X,Y) = tr(ad_X o ad_Y)

  For semi-simple Lie algebras (like su(n), so(n)):
  B is non-degenerate.
  Cartan's criterion: g is semi-simple iff B is non-degenerate.

  The Killing form is Ad-invariant: B(Ad_g X, Ad_g Y) = B(X,Y).
  For compact simple groups, -B is a Riemannian metric on G (bi-invariant metric).
```

---

## Symmetric Spaces

A **symmetric space** is a Riemannian manifold M where every point p has a geodesic-reversing isometry sigma_p (sigma_p(gamma(t)) = gamma(-t) for geodesics through p):

```
  EXAMPLES:
  Euclidean space R^n: sigma_p(x) = 2p - x  (reflection through p)
  Sphere S^n: sigma_p(x) = -x (antipodal for p=N)  -- actually geodesic symmetry
  Hyperbolic space H^n: sigma_p = reflection in p
  Grassmannians Gr(k,n): space of k-planes in R^n
  Positive definite matrices Sym+(n): sigma_A(B) = A B^{-1} A

  CLASSIFICATION: Cartan's symmetric spaces M = G/K
  G = isometry group, K = isotropy group at a point.
  All have a description as coset spaces of Lie groups.
```

**Positive definite matrices Sym+(n)**: This symmetric space appears in ML (covariance matrices), statistics (Wishart distributions), and diffusion tensor imaging. Geodesics are:

```
  Gamma(t) = A^{1/2} exp(t A^{-1/2} log(A^{-1/2} B A^{-1/2}) A^{1/2})
  Distance: d(A,B)^2 = ||log(A^{-1/2} B A^{-1/2})||_F^2
```
<!-- @editor[content/P2]: Sym+(n) section is correct but missing the connection to natural gradient and information geometry: the Fisher information matrix F(theta) of a parametric model is an element of Sym+(n), making the parameter space itself a Riemannian manifold with metric F. Natural gradient descent replaces the identity preconditioner with F^{-1}, i.e., it uses the Riemannian gradient (sharp of df with the Fisher metric) instead of the Euclidean gradient. This is exactly Riemannian gradient descent on the statistical manifold — the most direct application of Sym+(n) geometry to ML. Also missing: the log-Euclidean metric (approximation to affine-invariant metric, computationally cheaper) and its use in practical Riemannian ML frameworks (Geomstats, pyRiemann). -->

---

## Decision Cheat Sheet

| Group | Dim | Structure | Applications |
|---|---|---|---|
| SO(2) = S^1 | 1 | Rotations in plane | 2D rotations, phase |
| SO(3) | 3 | 3D rotations | Robotics, mechanics, graphics |
| SU(2) | 3 | Double cover SO(3) | Quantum mechanics, spin |
| SE(2) | 3 | 2D rigid motions | 2D robot kinematics |
| SE(3) | 6 | 3D rigid motions | 3D robot kinematics, pose |
| SL(2,R) | 3 | Area-preserving | Hyperbolic geometry |
| SU(3) | 8 | Unitary, det=1 | Strong force (QCD) |
| O(n), SO(n) | n(n-1)/2 | n-D rotations | Grassmannians, fiber bundles |
| U(n), SU(n) | n^2 | Unitary | Gauge theories |
| Sym+(n) | n(n+1)/2 | Positive definite matrices | Covariance geometry |

---

## Common Confusion Points

**"The Lie algebra determines the Lie group."**
The Lie algebra determines the simply-connected cover of the group (by Lie's third theorem). Different groups can have the same Lie algebra: SO(3) and SU(2) both have Lie algebra so(3) ≅ su(2), but SU(2) is simply connected while SO(3) = SU(2)/Z_2.

**"exp: g -> G is always surjective."**
Only for compact connected G. For SL(2,R) (non-compact), some elements cannot be expressed as exp(X) for any X in sl(2,R). In robotics: SE(3)'s exponential map is surjective (every rigid motion is a screw motion — the Chasles-Mozzi theorem).

**"The abstract algebra background is separate from the geometry."**
The whole point of Lie groups is that they are both. The abstract group structure tells you about symmetries. The manifold structure tells you about smooth deformations of those symmetries. The Lie bracket in the algebra encodes the curvature of the group manifold. Abstract algebra (groups) + differential geometry (manifolds) = Lie group theory.

<!-- @editor[bridge/P2]: Missing the equivariant networks → representation theory bridge. The Peter-Weyl theorem (compact Lie group G has irreducible representations that decompose L^2(G)) is the foundation for spherical harmonics (irreps of SO(3)) and the Clebsch-Gordan coefficients used in equivariant networks. This is mentioned in 09-APPLICATIONS but should be anchored here where the representation theory machinery lives. The key bridge: NequIP, SEGNN, and similar architectures use SO(3)/SE(3) irreducible representations as feature types; equivariance is enforced by requiring network layers to be linear maps between representation spaces (intertwiners). The abstract framework is the representation theory of Lie groups — it belongs in this file. -->

**"SO(3) and SU(2) are different objects."**
They are different groups (different as abstract groups, since SU(2) is simply connected and SO(3) is not). But they have the same Lie algebra. The covering map SU(2) -> SO(3) is a smooth group homomorphism with kernel Z_2. Physically: classical mechanics lives in SO(3), quantum mechanics of spin-1/2 particles requires SU(2).
