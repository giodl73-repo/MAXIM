# Applications: Relativity, Gauge Theory, Robotics, ML

## The Big Picture

Differential geometry is the language of fundamental physics, modern robotics, and increasingly, machine learning. The concepts from 01-08 connect directly to real systems.

```
+------------------------------------------------------------------+
|              APPLICATIONS OF DIFFERENTIAL GEOMETRY               |
+------------------------------------------------------------------+
|                                                                  |
|  GENERAL RELATIVITY           GAUGE THEORIES                    |
|  +--------------------+       +--------------------+            |
|  | Spacetime = 4D     |       | Standard Model =   |            |
|  | Lorentzian manifold|       | connections on     |            |
|  | Einstein equations |       | principal bundles  |            |
|  | Geodesics = free   |       | U(1) x SU(2) x SU(3)|          |
|  | fall trajectories  |       +--------------------+            |
|  +--------------------+                                          |
|                                                                  |
|  ROBOT KINEMATICS             ML ON MANIFOLDS                   |
|  +--------------------+       +--------------------+            |
|  | SE(3) = rigid body |       | Riemannian SGD     |            |
|  | motions            |       | Natural gradient   |            |
|  | Screw motions      |       | Manifold-valued    |            |
|  | Configuration space|       | data (SPD matrices)|            |
|  +--------------------+       +--------------------+            |
|                                                                  |
+------------------------------------------------------------------+
```

---

## General Relativity

**The manifold setup**: Spacetime is a 4-dimensional smooth manifold M with a **Lorentzian metric** g of signature (-,+,+,+):

```
  ds^2 = g_{mu nu} dx^mu dx^nu
       = -c^2 dt^2 + dx^2 + dy^2 + dz^2   (flat Minkowski, locally)

  The metric has one negative eigenvalue (time direction).
  Geodesics: timelike (ds^2 < 0), null (ds^2 = 0), spacelike (ds^2 > 0).

  Physical objects travel on timelike geodesics.
  Light travels on null geodesics.
```

**Einstein field equations**:

```
  G_{mu nu} + Lambda g_{mu nu} = (8 pi G / c^4) T_{mu nu}

  G_{mu nu} = Ric_{mu nu} - (1/2) g_{mu nu} R   (Einstein tensor, from 06-CURVATURE)
  Lambda g_{mu nu} = cosmological constant term   (dark energy)
  T_{mu nu} = stress-energy tensor               (matter/energy distribution)

  This is a system of 10 coupled nonlinear PDEs for g_{mu nu} (symmetric 4x4 tensor).
  Solutions: Schwarzschild (static black hole), Kerr (rotating black hole),
             FLRW (expanding universe), gravitational waves.

  Geodesic equation = equations of motion:
  d^2 x^mu/d tau^2 + Gamma^mu_{nu rho} (dx^nu/d tau)(dx^rho/d tau) = 0
  (tau = proper time along worldline)
  In weak field: recovers Newtonian gravity as leading correction.
```

**Key solutions and phenomena**:

```
  SCHWARZSCHILD METRIC (vacuum, spherically symmetric):
  ds^2 = -(1 - r_s/r) dt^2 + (1 - r_s/r)^{-1} dr^2 + r^2 dOmega^2
  r_s = 2GM/c^2  (Schwarzschild radius)

  Singularity at r=0 (physical) and r=r_s (coordinate singularity -- horizon).
  r = r_s defines the event horizon: null geodesics can escape from r>r_s but not r<r_s.

  GRAVITATIONAL WAVES:
  Linearized GR: perturb Minkowski metric g_{mu nu} = eta_{mu nu} + h_{mu nu}.
  h_{mu nu} satisfies wave equation: Box h_{mu nu} = -16 pi G T_{mu nu}.
  Transverse-traceless waves propagate at speed c.
  LIGO detects: strain h ~ 10^{-21} (10^{-21} relative length change).
```

**GPS needs GR**: Satellite clocks run faster (less gravity, special relativistic time dilation combined). Without correction (~38 microseconds/day), GPS accumulates 11 km/day of error. GR in software.

---

## Gauge Theories in Physics

The fundamental forces are all fiber bundle connections. This section connects 07-LIE-GROUPS and 08-FIBER-BUNDLES to physics.

```
  FORCE             GAUGE GROUP        BOSON          BUNDLE
  Electromagnetism  U(1)               Photon         Complex line bundle over spacetime
  Weak force        SU(2)              W+, W-, Z      Principal SU(2)-bundle
  Strong force      SU(3)              8 Gluons       Principal SU(3)-bundle
  Gravity           Diff(M) / SO(3,1)  Graviton       Frame bundle (Lorentz bundle)
```

**Electromagnetism as U(1) gauge theory**:

```
  Connection: A_mu (electromagnetic 4-potential)
  Curvature: F_{mu nu} = partial_mu A_nu - partial_nu A_mu  (EM field tensor)
  Contains: E_i = F_{0i} (electric field), B_i = epsilon_{ijk} F_{jk}/2 (magnetic field)

  Maxwell equations in differential form language:
  dF = 0               (Bianchi identity, automatic since F = dA)
                       = magnetic Gauss law + Faraday's law
  d * F = * J          (Yang-Mills equation)
                       = electric Gauss law + Ampere's law

  Gauge transformation: A -> A + d lambda  (lambda: M -> R)
  F -> F + d(d lambda) = F + 0 = F   (invariant)

  Minimal coupling to matter: replace partial_mu with D_mu = partial_mu - ieA_mu
  This is covariant derivative on the associated line bundle.
  Dirac equation with EM: (i D_mu gamma^mu - m) psi = 0
```

**Non-Abelian gauge theories (Yang-Mills)**:

```
  For G = SU(2): W boson fields
  Connection A = A_mu^a T^a dx^mu where T^a are SU(2) generators
  Curvature F_{mu nu} = partial_mu A_nu - partial_nu A_mu + [A_mu, A_nu]
                      = partial_mu A_nu - partial_nu A_mu + A_mu A_nu - A_nu A_mu
  The commutator [A_mu, A_nu] is the non-Abelian contribution.
  Physical consequence: self-interaction of W bosons (detected at LEP, LHC).

  INSTANTON (self-dual solution):
  F = *F  (self-dual field strength)
  Solutions on S^4 or R^4.
  Topological charge: k = (1/8pi^2) Integral tr(F wedge F) in Z
  (integer by Chern-Weil theory)
  Instantons are the dominant non-perturbative effects in QCD.
```

---

## Robot Kinematics via SE(3)

Rigid body motion in 3D lives in SE(3). Lie group machinery makes kinematic computations systematic.

**Forward kinematics**:

```
  A robot arm with n joints:
  Configuration: (theta_1, ..., theta_n) in T^n = S^1 x ... x S^1 or R^n
  End-effector pose: g in SE(3)

  Each joint contributes a transformation in SE(3):
  g(theta) = g_1(theta_1) * g_2(theta_2) * ... * g_n(theta_n)

  For revolute joint i (rotation around axis k_i through point q_i):
  g_i(theta_i) = exp(theta_i * xi_i)   where xi_i in se(3) is the twist of joint i

  The exponential map exp: se(3) -> SE(3) gives:
  exp(theta * [omega_x; v; 0; 0]) = [exp(omega_x theta), (I - exp(omega_x theta)) omega x v + omega omega^T v theta; 0, 1]
  (Rodrigues formula extended to SE(3))

  PRODUCT OF EXPONENTIALS (POE) formula:
  g_st(theta) = exp(xi_1 theta_1) ... exp(xi_n theta_n) g_st(0)
  Clean, singularity-free formulation of forward kinematics.
```

**Velocity kinematics (Jacobian)**:

```
  Body twist (velocity expressed in end-effector frame):
  V_b = g^{-1} g_dot in se(3)

  Spatial twist (velocity in world frame):
  V_s = g_dot g^{-1} in se(3)

  Body Jacobian J_b: V_b = J_b(theta) theta_dot
  Columns: J_b^i = Ad_{g_{i+1}...g_n}^{-1} xi_i

  Singularity: det(J_b) = 0 => loss of one DOF. Avoid in workspace planning.

  Inverse kinematics: given desired g in SE(3), find theta.
  Generally overdetermined/underdetermined for non-6-DOF robots.
  For 6-DOF: local solution by Newton-Raphson on the Lie algebra.
```

**Interpolation on SE(3)**:

```
  Need to move from pose A to pose B smoothly.

  Naive (bad): interpolate 4x4 matrices linearly => not SE(3).
  Correct: geodesic interpolation in SE(3) with bi-invariant metric.

  g(t) = A * exp(t * log(A^{-1} B))   t in [0,1]
  = follows the geodesic from A to B in SE(3).

  This is "screw interpolation" (Chasles: every rigid motion is a screw motion).
```

---

## Machine Learning on Manifolds

As ML models work with data having inherent geometric structure, Riemannian geometry provides the right framework.

**Why manifold-valued ML**:

```
  Data with geometric constraints:
  - Rotation matrices: SO(n) -- aerial robotics, computer vision
  - Covariance matrices: Sym+(n) -- brain imaging, financial returns
  - Unit spheres: S^n -- normalized word embeddings, Fisher's discriminant
  - Stiefel manifolds St(k,n): -- orthogonal networks, PCA
  - Grassmannians Gr(k,n): -- subspace-valued data
  - Hyperbolic space H^n: -- hierarchical data, knowledge graphs

  Naive ML (treating manifold as Euclidean):
  Averaging rotation matrices by averaging entries -> invalid rotation (det ≠ 1).
  Correct: Fréchet mean on the manifold.
```

**Fréchet mean on a manifold**:

```
  Given points p_1, ..., p_n in M:
  Fréchet mean = argmin_{p in M} Sum_i d(p, p_i)^2

  Computed by iterative gradient descent on the manifold:
  p <- exp_p(-alpha Sum_i log_p(p_i))

  For Sym+(n): the Fréchet mean is the matrix geometric mean.
  For SO(n): solved via polar decomposition / SVD.
```

**Riemannian Gradient Descent**:

```
  Standard gradient descent in R^n:
  x_{t+1} = x_t - alpha * grad f(x_t)

  Riemannian gradient descent on (M, g):
  x_{t+1} = exp_{x_t}(-alpha * grad_M f(x_t))

  Where grad_M f = (grad f)^sharp  (raise index with the metric)
  (Riemannian gradient: projection of Euclidean gradient onto tangent plane,
  then raise with metric)

  CONVERGENCE: For geodesically convex functions on manifolds with
  non-negative curvature, Riemannian GD converges at the same rate as
  Euclidean GD for convex functions.
```

**Geodesic Convexity**:

```
  f: M -> R is geodesically convex if for any geodesic gamma:
  f(gamma(t)) <= (1-t) f(gamma(0)) + t f(gamma(1))

  Examples:
  Log-det(A) is geodesically convex on Sym+(n) with the natural metric.
  d(., p)^2 is geodesically convex on manifolds with K <= 0.
  Energy functions in graph Laplacian problems.

  Geodesic convexity unlocks global convergence guarantees for Riemannian GD.
```

**Geometric Deep Learning**:

```
  Principle: Build neural networks that respect the symmetries of the data.

  G-EQUIVARIANT NETWORKS:
  If data x transforms as x -> rho(g) x (representation rho of group G),
  the network should satisfy: f(rho(g)x) = rho'(g) f(x)

  Applications:
  SO(3)-equivariant networks: for 3D molecular data (SchNet, DimeNet, NequIP)
  SE(3)-equivariant: protein structure prediction (AlphaFold uses IPA attention)
  Grid data on S^2: SE(2)-equivariant CNNs for satellite imagery
  Graphs: permutation-equivariant (GNNs are implicitly equivariant to graph automorphisms)

  Key mathematical tool: Peter-Weyl theorem -- decompose representations of
  compact Lie groups into irreducibles. For SO(3): spherical harmonics basis.
  Clebsch-Gordan coefficients: how tensor products of irreps decompose.
```

**Hyperbolic Neural Networks**:

```
  Hierarchical data (trees, taxonomies) embed better in hyperbolic space H^n
  than in Euclidean space:
  - In H^n: exponential growth of "volume" matches tree branching.
  - Embedding a binary tree in R^2 requires distortion; H^2 = perfect.

  Hyperbolic networks:
  Operations in H^n using Poincaré disk model or hyperboloid model.
  Poincaré embeddings for knowledge graphs (Nickel & Kiela 2017).
  Fully hyperbolic neural networks: matrix multiplication and softmax in H^n.

  Poincaré disk model: {z in C: |z| < 1}
  Metric: ds^2 = 4 dz dz_bar / (1 - |z|^2)^2
  Geodesics: circles orthogonal to the unit circle.
  Sectional curvature: K = -1 (constant negative curvature).
```

---

## Symplectic Geometry and Hamiltonian Mechanics

The phase space of classical mechanics is a symplectic manifold:

```
  SYMPLECTIC MANIFOLD (M, omega):
  omega = closed, non-degenerate 2-form (omega^n != 0, d omega = 0)

  Phase space: M = T*Q (cotangent bundle of configuration space Q)
  Natural symplectic form: omega = dq^i wedge dp_i  (in coordinates)

  Hamiltonian H: M -> R (total energy)
  Hamilton's equations from omega:
  dH = omega(X_H, -)  defines the Hamiltonian vector field X_H
  q_dot^i = partial H / partial p_i,    p_dot_i = -partial H / partial q_i

  Symplectic connection: Liouville's theorem (symplectomorphisms preserve volume)
  = conservation of phase space volume under Hamiltonian flow.

  MOMENT MAP mu: M -> g*  (Lie algebra dual)
  Encodes conserved quantities for G-symmetric Hamiltonians.
  Angular momentum = moment map for SO(3) action on T*R^3.
```

---

## Decision Cheat Sheet

| Application | Geometric Object | Key Operation |
|---|---|---|
| Free fall / planetary orbit | Geodesic on Lorentzian manifold | Solve geodesic equation |
| Light bending near mass | Null geodesic near curved region | Schwarzschild geodesics |
| Robot forward kinematics | SE(3) via exp map | Product of exponentials formula |
| Robot velocity | Jacobian in se(3) | Body/spatial twist |
| Pose interpolation | Geodesic in SE(3) | exp(t * log(A^{-1} B)) |
| Average covariance matrices | Fréchet mean in Sym+(n) | Riemannian gradient descent |
| Rotation-equivariant network | SO(3) group representations | Spherical harmonics, CG coefficients |
| Hierarchical embedding | Hyperbolic space H^n | Poincaré disk model, geodesics |
| Hamiltonian simulation | Symplectic integrator on T*Q | Preserve symplectic structure |
| EM field equations | U(1) connection on line bundle | F = dA, d*F = *J |

---

## Common Confusion Points

**"GR replaces Newtonian gravity with geometry — is it just a change of coordinates?"**
No. The curvature of spacetime is a genuine physical effect, not a coordinate artifact. Geodesic deviation (tidal forces) is measured by the Riemann tensor, which is a coordinate-free quantity. You cannot globally "undo" curvature with a coordinate change.

**"Gauge symmetry is a physical symmetry."**
Gauge symmetry is a redundancy in the description, not a physical symmetry. Gauge-equivalent field configurations are physically identical. True physical symmetries (like Lorentz invariance) relate physically distinct configurations.

**"Riemannian manifold operations on SO(3) are expensive."**
The exp and log maps for SO(3) have closed forms (Rodrigues' formula, ~O(1) computation). For SE(3), also closed form. For Sym+(n): O(n^3) eigendecomposition. The computational cost is comparable to a matrix multiplication for the important special cases.

**"Equivariance is the same as invariance."**
Equivariance: f(gx) = g f(x) (output transforms). Invariance: f(gx) = f(x) (output unchanged). Equivariant networks can output transformed versions (useful for predicting 3D structure); invariant outputs a scalar (useful for energy prediction). SE(3)-equivariant networks predict forces that correctly transform as vectors; energy (scalar) is SE(3)-invariant.
