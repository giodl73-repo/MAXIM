# Applications Beyond Physics

## The Big Picture

Lie groups appear wherever continuous symmetry matters. Physics is the classical domain
(gauge theory, quantum mechanics), but the same mathematical structures appear in harmonic
analysis, machine learning on geometric data, robotics, and computer vision.

```
+----------------------------------------------------------------------+
|                  LIE GROUPS: APPLICATION MAP                         |
+----------------------------------------------------------------------+
|                                                                      |
|  PHYSICS                          HARMONIC ANALYSIS                  |
|  Gauge theory (07)                Fourier on groups                  |
|  Angular momentum (04)            Peter-Weyl theorem (03)            |
|  Spacetime symmetry               Zonal spherical functions          |
|                                                                      |
|  DIFFERENTIAL GEOMETRY            MACHINE LEARNING                   |
|  Principal bundles (08)           Equivariant neural networks        |
|  Holonomy, curvature              SE(3)-equivariant GNNs             |
|                                   E(3) equivariant networks          |
|                                                                      |
|  ROBOTICS & CONTROL               COMPUTER VISION                    |
|  SE(3) rigid body motion          Camera calibration (SO(3))         |
|  Lie group integrators            Pose estimation                    |
|  Kinematics on Lie groups         Optical flow (SE(2))               |
|                                                                      |
|  MATHEMATICS                      SIGNAL PROCESSING                  |
|  Symmetric spaces                 Wavelets on spheres                |
|  Representation theory            Non-commutative harmonic analysis  |
|                                                                      |
+----------------------------------------------------------------------+
```

---

## Fourier Analysis on Groups (Peter-Weyl as Generalized Fourier)

Classical Fourier analysis on R or S^1 generalizes to any locally compact group via
representation theory. The Peter-Weyl theorem (03-REPRESENTATIONS.md) is the compact group
version.

**Abelian case — standard Fourier series:**
```
G = S^1 = U(1):
  Irreps: rho_n: e^{i theta} |-> e^{i n theta}  for n in Z (1-dim reps)
  Characters: chi_n(g) = rho_n(g) = e^{i n theta}
  Fourier expansion: f(theta) = sum_n f_hat(n) e^{i n theta}
  Parseval: ||f||^2_{L^2} = sum_n |f_hat(n)|^2
```

**Non-abelian case — Peter-Weyl:**
```
G = SU(2) (dim 3, irreps V_j for j = 0, 1/2, 1, ...):
  Fourier transform: f_hat(j) = integral_{SU(2)} f(g) rho_j(g^{-1}) dg   (matrix-valued)
  Fourier expansion: f(g) = sum_j (2j+1) tr(rho_j(g) f_hat(j))
  Parseval: ||f||^2_{L^2} = sum_j (2j+1) ||f_hat(j)||^2_{Hilbert-Schmidt}
```

The factor (2j+1) = dim(V_j) replaces the factor 1 (all irreps are 1-dim) in the abelian case.
The Fourier transform of f is now a sequence of matrices (one per irrep), not scalars.

**Spherical harmonics as group theory:** Functions on the sphere S^2 = SO(3)/SO(2):
```
S^2 functions = functions on SO(3) invariant under right SO(2) action
             = class functions on SO(3) induced from SO(2)
```
The spherical harmonics Y^m_l for fixed l are the basis for the l-th irrep of SO(3) restricted
to functions on S^2. The Laplace-Beltrami operator on S^2 has eigenvalues -l(l+1) on Y^m_l —
this is the Casimir element of so(3) acting in the spin-l representation.

**Practical applications:**
- Solving PDEs on spheres (atmospheric modeling, geophysics): expand in spherical harmonics
- Non-commutative signal processing on groups: replace Fourier transforms with Peter-Weyl
- Quantum chemistry: molecular orbitals classified by SO(3) irreps (s,p,d,f,...)

---

## Equivariant Neural Networks: SE(3)-GNNs

**The problem:** Neural networks processing 3D molecular geometry or point clouds should not
care about the orientation of the input in 3D space. A molecule's energy should not depend on
how we rotate the coordinate system. But standard MLPs are not equivariant — they treat the
coordinates as bare numbers.

**Equivariance definition:** A function f: X -> Y is G-equivariant if:
```
f(rho_X(g) . x) = rho_Y(g) . f(x)  for all g in G, x in X
```
where rho_X and rho_Y are representations of G on X and Y.

For rotation equivariance (G = SO(3)): rotating the input should correspondingly rotate the output.

**E(3) and SE(3) equivariant networks:**
```
G = E(3) = O(3) semi-direct R^3  (Euclidean group, includes reflections)
G = SE(3) = SO(3) semi-direct R^3 (special Euclidean, rotations+translations only)

A SE(3)-equivariant neural network:
  Input: 3D point cloud {x_i in R^3} with features {f_i in V}
  Output: features in V' (or scalars, vectors, tensors)
  Equivariance: if input is rotated/translated, output transforms accordingly
```

**How to build equivariant layers:** Using Peter-Weyl, decompose features into irreps of SO(3):
- Scalars (j=0): rotation-invariant quantities
- Vectors (j=1): rotate as 3-vectors
- Tensors (j=2): rotate as symmetric traceless tensors
- Higher j: spin-j irreps of SO(3)

Features are stored as collections of (2j+1)-dimensional vectors for various j. Network layers
are maps between these that commute with SO(3) action.

**Tensor product decomposition in networks:** To combine two features of types j_1 and j_2,
use the Clebsch-Gordan decomposition:
```
V_{j_1} tensor V_{j_2} = direct_sum_{j=|j_1-j_2|}^{j_1+j_2} V_j
```
with Clebsch-Gordan coefficients. The output features of type j are weighted sums of these
products. This is exactly angular momentum addition from quantum mechanics, repurposed as a
neural network layer.

**Key SE(3)-equivariant architectures:**

| Architecture | Year | Key idea |
|-------------|------|---------|
| Tensor Field Networks (TFN) | 2018 | First SE(3)-equivariant GNN using CG coefficients |
| SE(3)-Transformers | 2020 | Attention + SE(3) equivariance |
| PaiNN | 2021 | Equivariant message passing for molecules |
| NequIP | 2022 | High-accuracy equivariant interatomic potentials |
| MACE | 2022 | Many-body equivariant message passing; SOTA on materials |
| Equiformer | 2022 | Equivariant transformer with DFT-level accuracy |

**AlphaFold2 connection:** While AlphaFold2 itself uses a different approach (invariant point
attention), the successor AlphaFold3 and contemporary work on protein structure prediction
increasingly uses SE(3)-equivariant architectures because they dramatically improve sample
efficiency — you don't need to train on all orientations of the same molecule.

---

## Robotics: SE(3) Rigid Body Motion

**Configuration space:** A rigid body in 3D has configuration in SE(3):
```
SE(3) = SO(3) semi-direct R^3
(R, t) where R = 3x3 rotation matrix, t = 3-vector translation
```

**Lie algebra se(3):** The algebra has basis {omega_1, omega_2, omega_3, v_1, v_2, v_3}:
```
se(3) = so(3) semi-direct R^3
Elements: (omega, v) where omega in so(3) (angular velocity), v in R^3 (linear velocity)

In matrix form (homogeneous coordinates, 4x4 matrices):
  (omega, v) <-->  [[ omega_skew | v ],
                    [    0       | 0 ]]
```
where omega_skew is the 3x3 skew-symmetric matrix of omega.

**Kinematics on SE(3):**
```
Configuration: g(t) = (R(t), x(t)) in SE(3)
Velocity: g_dot = g * xi   (body-frame velocity xi in se(3))
          g_dot = eta * g  (spatial-frame velocity eta in se(3))

Body velocity: xi = (omega_b, v_b) = body angular + linear velocity
               xi = g^{-1} g_dot  (Maurer-Cartan form applied to g_dot)
Spatial velocity: eta = g_dot g^{-1}  (spatial angular + linear velocity)
```

**Exponential map for SE(3):**
```
exp(omega_skew, v) = ?

If omega != 0, let theta = |omega|, u = omega/theta:
  R = I + sin(theta)/theta * omega_skew + (1-cos(theta))/theta^2 * omega_skew^2
  t = (I - R) * (omega x v) / theta^2 + omega * (omega . v) / theta^2

(Closed-form formula for exp in SE(3))
```

**Rodrigues' formula for SO(3):**
```
exp(theta * n_skew) = I + sin(theta) n_skew + (1-cos(theta)) n_skew^2
```
where n is a unit vector (rotation axis) and n_skew is its skew-symmetric matrix.

**Lie group integration for robot trajectory planning:**
```
Naive approach: represent orientation as Euler angles phi,theta,psi
  Problem: gimbal lock (singularity when theta = pm pi/2)

Lie group approach: represent orientation as R in SO(3) or q in SU(2)
  Update: R_new = R_old * exp(delta_omega_skew)
  No singularities, correct handling of large rotations

Forward kinematics in se(3):
  T_total = T_1 * T_2 * ... * T_n  (product of SE(3) elements)
  Each T_i from joint parameters; overall pose = product
```

**Screw theory:** The Lie algebra se(3) has a basis of "screws" — rotations about an axis
combined with translations along it. Every rigid body motion is a screw motion (Chasles' theorem).
This is the Lie-algebraic form of the classical result.

---

## Computer Vision: Pose Estimation and Camera Groups

**Camera rotation estimation:** Given two images of the same scene from different viewpoints,
recover the rotation R in SO(3) and translation t in R^3 relating them.

**Essential matrix:** The fundamental constraint relating corresponding points (x_1, x_2):
```
x_2^T E x_1 = 0   where E = t_skew * R   (the essential matrix)
```
E lives in a 5-parameter space (modulo scale): 3 params for R in SO(3), 2 for direction of t.

**Lie group perspective:** The space of camera motions is SE(3)/scale. Optimizing over camera
poses requires optimization on a Lie group manifold — the gradient descent must use the group
structure to stay on the manifold.

**Rotation averaging:** Given N noisy rotation measurements R_1,...,R_N (e.g., from multiple
camera pairs), compute the "mean rotation":
```
Naive: can't average matrices (R_bar = (1/N) sum R_i is not a rotation matrix in general)

Frechet mean on SO(3): R_mean = argmin_{R in SO(3)} sum_i d(R, R_i)^2
  where d is the geodesic distance on SO(3): d(R_1,R_2) = || log(R_1^T R_2) ||_F / sqrt(2)

Iterative algorithm (Lie group gradient descent):
  R <- R * exp(-(1/N) sum_i log(R^T R_i))
  Repeat until convergence.
```

**Optical flow and SE(2):** In 2D images, the symmetry group relevant to planar rigid motions
is SE(2) = SO(2) semi-direct R^2 (rotation + translation in 2D). Estimating optical flow
in video is estimating the SE(2) motion field.

---

## Harmonic Analysis on Riemannian Symmetric Spaces

**The generalization:** Spherical harmonics generalize from S^n = SO(n+1)/SO(n) to arbitrary
symmetric spaces G/K. The "zonal spherical functions" play the role of Y^0_l (the m=0 case):

```
phi_lambda(g) = integral_K e^{(i lambda + rho)(log(a(kg))) } dk
              = Harish-Chandra's spherical functions
```

**Helgason's theorem:** The Plancherel formula for L^2(G/K) generalizes Peter-Weyl:
```
L^2(G/K) = integral_a_+* V_lambda d mu(lambda)
```
where the integral is over the "dual" of K-spherical spectrum and d mu is the Plancherel measure.

**Applications:**
- Diffusion MRI: model brain white matter as fields on SO(3)/SO(2) (spherical functions)
- Cryo-EM protein structure: average over unknown orientations in SO(3)
- Statistics on Lie groups: sample mean, covariance, hypothesis testing on manifolds

---

## Statistical Shape Analysis and SO(n) in Data Science

**Kendall shape spaces:** The "shape" of a set of k landmark points in R^m (modulo rigid motions)
lives in a quotient manifold:
```
Sigma^m_k = {centered k-point configurations in R^m} / (scale, rotation, translation)
          = S^{mk-m-1} / SO(m)    (for m=2: the complex projective space CP^{k-2})
```

**Procrustes analysis:** Align two shapes by finding the optimal rotation:
```
min_{R in SO(m)} sum_i || R x_i - y_i ||^2
Solution: via SVD of Y^T X = U Sigma V^T: R_opt = U V^T
```
This is optimization on the Lie group SO(m) with an analytic solution.

---

### Geometric Deep Learning: The Unifying Framework

The architectures above (TFN, SE(3)-Transformers, MACE, Equiformer) are all instances of the **Geometric Deep Learning** (GDL) blueprint (Bronstein, Bruna, LeCun, Szlam, Vandergheynst, 2021): pick your symmetry group G, build G-equivariant layers via the representation theory of G, and you get the appropriate inductive bias for your geometric domain.

| Architecture | Symmetry Group G | Equivariance |
|-------------|------------------|-------------|
| CNN | Translation T^n | Shift-equivariant feature maps |
| GNN | Permutation S_n | Node/edge permutation invariant |
| SE(3)-GNN (TFN, MACE) | SE(3) | Rotation + translation equivariant |
| Gauge-equivariant CNN | Gauge group on manifold | Coordinate-free processing on curved surfaces |
| Transformer (with position) | Permutation (+ learned position) | Set function with positional encoding |

The unifying principle: the choice of symmetry group determines the architecture. All of deep learning's major architecture families are instances of this single construction.

---

## Decision Cheat Sheet

| Application | Lie group | Key tool |
|-------------|-----------|---------|
| Fourier on S^1 | U(1) | Characters chi_n(theta) = e^{ino} |
| Spherical harmonics | SO(3) | Peter-Weyl: Y^m_l = irrep V_l restricted to S^2 |
| Equivariant ML (3D) | SE(3) = SO(3) x_s R^3 | Clebsch-Gordan tensor products |
| Rigid body kinematics | SE(3) | Exponential map, adjoint representation |
| Rotation averaging | SO(3) | Frechet mean via log/exp |
| Camera pose | SO(3) or SE(3) | Essential matrix, manifold optimization |
| Quantum chemistry | SO(3) | Atomic orbital = spherical harmonic = SO(3) irrep |
| Cryo-EM reconstruction | SO(3) | Average over unknown orientations |
| Shape statistics | SO(n) | Procrustes analysis, Kendall shape space |

---

## Common Confusion Points

**"Equivariant means invariant":** Equivariant means the output transforms consistently with
the input (f(gx) = g f(x)). Invariant is the special case where the output doesn't change
(f(gx) = f(x)). Invariant networks (like MPNN without directional features) lose directional
information; equivariant networks preserve it. For geometry tasks (forces on atoms, molecular
dipole moment), you need equivariance, not just invariance.

**"SE(3)-equivariant is the same as SO(3)-equivariant":** SE(3) includes translations; SO(3)
only rotations. For a fixed origin, SO(3) suffices. For arbitrary translation of the coordinate
system, you need SE(3) equivariance. Most molecular applications need both.

**"Clebsch-Gordan coefficients are just quantum mechanics notation":** They are the fundamental
tool for combining irreducible representations of any group with tensor product structure. In
equivariant networks, they are used as a learned linear combination weighted by coefficients
that are the CG coefficients. The physics and ML communities independently discovered the same
mathematics.

**"Fourier on non-abelian groups is harder computationally":** Yes. For U(1), Fourier transform
is O(N log N) via FFT. For SO(3), the non-commutative Fourier transform requires computing all
irreps up to some bandwidth L and has cost O(L^3) for naive algorithms. The non-equivariant FFT
on SO(3) (exploiting the group structure) brings this down to O(L^2 log L). For ML applications,
computing CG tensor products is the computational bottleneck in equivariant networks.
