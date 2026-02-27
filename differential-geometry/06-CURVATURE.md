# Curvature

## The Big Picture

Curvature measures how much a Riemannian manifold deviates from being flat. The Riemann curvature tensor is the fundamental invariant; all other curvature quantities are derived from it.

```
+------------------------------------------------------------------+
|                     CURVATURE HIERARCHY                          |
+------------------------------------------------------------------+
|                                                                  |
|  RIEMANN CURVATURE TENSOR R (most information)                  |
|  R^l_{kij}: antisymmetric in i,j; Bianchi symmetries           |
|  In n dimensions: n^2(n^2-1)/12 independent components         |
|  n=2: 1 component = Gaussian curvature                          |
|  n=4: 20 independent components (spacetime!)                    |
|         |                                                         |
|         v                                                         |
|  RICCI TENSOR Ric                                               |
|  Ric_{ij} = R^k_{ikj} (trace of Riemann over one index pair)   |
|  Symmetric (0,2) tensor; n(n+1)/2 components                   |
|         |                                                         |
|         v                                                         |
|  SCALAR CURVATURE R                                             |
|  R = g^{ij} Ric_{ij} (trace of Ricci)                          |
|  Single function on M                                           |
|         |                                                         |
|  SECTIONAL CURVATURE K(sigma)                                   |
|  One number per 2-plane sigma in T_p M                          |
|  Determines Riemann tensor if all sectional curvatures known    |
+------------------------------------------------------------------+
```

---

## The Riemann Curvature Tensor

**Definition**: The curvature measures the failure of parallel transport around infinitesimal loops:

```
  R(X,Y)Z = nabla_X nabla_Y Z - nabla_Y nabla_X Z - nabla_{[X,Y]} Z

  This is a (1,3) tensor: R: TM x TM x TM -> TM
  Antisymmetric in X,Y.
  R(X,Y)Z = -R(Y,X)Z

  In coordinates (components of (0,4) tensor R_{lijk} = g(R(partial_k, partial_j) partial_l, partial_i)):
  R^l_{kij} = partial_i Gamma^l_{kj} - partial_j Gamma^l_{ki} + Gamma^l_{im} Gamma^m_{kj} - Gamma^l_{jm} Gamma^m_{ki}

  Two partial derivatives of Gamma (second derivatives of g) minus products of Gamma.
```

**Geometric interpretation**: Take a small parallelogram in M with sides along X and Y. Parallel transport a vector Z around this parallelogram. The result is Z + R(X,Y)Z * Area + higher order terms.

```
  Flat: R = 0. Parallel transport is path-independent.
  Curved: R != 0. Parallel transport around a loop rotates the vector.

  Holonomy (05) and curvature (06) are related:
  For small loops: Hol ~ exp(R * Area)  (Lie algebra element)
  For finite loops: Ambrose-Singer theorem.
```

---

## Symmetries of the Riemann Tensor

```
  R_{ijkl} = g(R(partial_k, partial_l) partial_j, partial_i)   (all lower indices)

  ALGEBRAIC SYMMETRIES:
  R_{ijkl} = -R_{ijlk}               (antisymmetric in last two)
  R_{ijkl} = -R_{jikl}               (antisymmetric in first two)
  R_{ijkl} = R_{klij}                (swap pairs)

  These give n^2(n^2-1)/12 independent components.

  FIRST BIANCHI IDENTITY:
  R(X,Y)Z + R(Y,Z)X + R(Z,X)Y = 0
  R_{i[jkl]} = 0   (antisymmetrize over last three = 0)

  SECOND BIANCHI IDENTITY (differential):
  nabla_W R(X,Y)Z + nabla_X R(Y,W)Z + nabla_Y R(W,X)Z = 0
  nabla_{[m} R_{ij]kl} = 0

  The contracted second Bianchi identity:
  nabla^j (Ric_{ij} - (1/2) g_{ij} R) = 0
  nabla^j G_{ij} = 0   (where G_{ij} = Ric_{ij} - (1/2) g_{ij} R is the Einstein tensor)
  This is the mathematical reason the Einstein field equations are consistent.
```

---

## Ricci Tensor and Scalar Curvature

**Ricci tensor**: A single contraction of the Riemann tensor:

```
  Ric_{ij} = R^k_{ikj} = Sum_k R^k_{ikj}   (trace over first and third indices)

  Ric is symmetric: Ric_{ij} = Ric_{ji}
  n(n+1)/2 independent components.

  GEOMETRIC MEANING: Ric_{ij} v^i v^j measures how small balls in direction v
  deviate in volume from flat-space balls:
  Vol(geodesic ball radius eps in direction v)
  = omega_n eps^n [1 - Ric(v,v)/6(n+2) eps^2 + O(eps^4)]

  Negative Ricci curvature: balls LARGER than in flat space
  Positive Ricci curvature: balls SMALLER than in flat space
```

**Scalar curvature**: The full trace:

```
  R = g^{ij} Ric_{ij} = Sum_i kappa_i  (sum of sectional curvatures in all 2-planes)

  Single function R: M -> R.
  R > 0: manifold "curved inward on average"
  R = 0: compatible with flat (not sufficient for flat)
  R < 0: manifold "curved outward on average"
```

---

## Einstein Tensor

The key combination in General Relativity:

```
  G_{ij} = Ric_{ij} - (1/2) g_{ij} R

  Properties:
  G_{ij} = G_{ji}  (symmetric)
  nabla^j G_{ij} = 0  (divergence-free: from contracted Bianchi)

  EINSTEIN FIELD EQUATIONS:
  G_{ij} = 8 pi G / c^4 * T_{ij}

  G_{ij}: geometric (curvature of spacetime)
  T_{ij}: stress-energy tensor (distribution of matter/energy)

  "Matter tells spacetime how to curve;
   curved spacetime tells matter how to move."
   -- Wheeler's paraphrase

  The contracted Bianchi identity nabla^j G_{ij} = 0 forces
  nabla^j T_{ij} = 0: energy-momentum conservation is a CONSEQUENCE
  of the geometric structure.
```

---

## Sectional Curvature

For a 2-dimensional subspace sigma = span{X,Y} in T_p M:

```
  K(sigma) = R(X,Y,X,Y) / (g(X,X)g(Y,Y) - g(X,Y)^2)
           = R_{ijkl} X^i Y^j X^k Y^l / (||X||^2 ||Y||^2 - g(X,Y)^2)

  K(sigma) is independent of the choice of basis for sigma.
  It equals the Gaussian curvature of the surface swept out
  by geodesics in the plane sigma.
```

**Curvature comparison theorems**: The sectional curvature controls geometry:

```
  THEOREM (Bonnet-Myers): If Ric >= (n-1)K > 0 (Ricci bounded below),
  then diam(M) <= pi/sqrt(K) and M is compact with finite fundamental group.

  THEOREM (Cartan-Hadamard): If K <= 0 everywhere and M is complete,
  then exp_p: T_p M -> M is a diffeomorphism (M is diffeomorphic to R^n).
  No conjugate points. Geodesics are globally minimizing.

  THEOREM (Sphere theorem): If K in (1/4, 1] (1/4-pinched),
  then M is homeomorphic to S^n (Berger-Klingenberg).
  Differentiably: if K in (1/4, 1] strictly, M is diffeomorphic to S^n (Brendle-Schoen 2007).
```

---

## Gauss-Bonnet Theorem

Connects curvature (differential geometry) to topology (Euler characteristic):

```
  For a compact, oriented 2-manifold M:
  Integral_M K dA = 2 pi chi(M)

  Where K = Gaussian curvature, dA = area element, chi = Euler characteristic.

  chi(S^2) = 2:    Integral_{S^2} K dA = 4 pi.   For round S^2: K=1, Area=4pi. ✓
  chi(T^2) = 0:    Integral_{T^2} K dA = 0.       Flat torus: K=0. ✓
  chi(genus-g surface) = 2-2g.

  CONSEQUENCE: No matter how you deform a sphere, the total curvature stays 4 pi.
  You can't change the topology by smooth deformation.

  HIGHER DIMENSION (Chern-Gauss-Bonnet, even dim n=2m):
  Integral_M Pf(R) = (2 pi)^m chi(M)
  Where Pf(R) is the Pfaffian of the curvature form.
```

---

## Weyl Tensor and Conformal Curvature

The Riemann tensor decomposes into:

```
  R_{ijkl} = W_{ijkl}
            + (1/(n-2)) (g_{ik} Ric_{jl} - g_{il} Ric_{jk} - g_{jk} Ric_{il} + g_{jl} Ric_{ik})
            - (R/((n-1)(n-2))) (g_{ik} g_{jl} - g_{il} g_{jk})

  W = Weyl tensor (trace-free part of Riemann)
  Ric part: information in Ricci tensor
  R part: scalar curvature

  W_{ijkl} is conformally invariant:
  If g -> e^{2f} g (conformal rescaling), then W -> e^{2f} W.

  In 4D spacetime: W encodes "tidal forces" (gravitational waves, radiation).
  Ric part encodes local matter distribution (Einstein equations constrain Ric, not W).
  The Weyl curvature of the early universe was near zero; today it is large (structure).
```

---

## Spaces of Constant Curvature

The complete classification:

```
  Simply-connected, complete, n-dimensional Riemannian manifold with
  constant sectional curvature K:

  K > 0:  S^n (round sphere)        -- unique up to scaling
  K = 0:  R^n (Euclidean space)     -- unique
  K < 0:  H^n (hyperbolic space)    -- unique up to scaling

  These are the three "model spaces" of constant curvature.
  Any other constant curvature manifold is a quotient: M^n / Gamma
  where Gamma is a discrete group of isometries acting freely and properly.

  Geometric structure of surfaces (2D):
  Sphere S^2, flat torus R^2/Z^2, hyperbolic surfaces H^2/Gamma.
  The Gauss-Bonnet theorem rules: chi > 0 -> K>0; chi=0 -> K=0; chi < 0 -> K<0.

  Thurston's geometrization (3D): Every compact 3-manifold can be cut into
  pieces, each admitting one of 8 model geometries. Proved by Perelman (2003)
  as a consequence of the Poincare conjecture.
```

---

## Ricci Flow

**Ricci flow** (Hamilton 1982, used by Perelman to prove Poincaré conjecture):

```
  Evolve the metric by Ricci curvature:
  d/dt g_{ij} = -2 Ric_{ij}

  INTUITION: "smooth out" the metric. Regions of positive Ricci curvature
  (too much curving) shrink. Regions of negative Ricci curvature grow.

  Fixed points: Ricci-flat metrics (Ric = 0). Examples: T^n, Calabi-Yau manifolds.
  "Ricci solitons": self-similar solutions (solitons moving by diffeomorphism + scaling).

  APPLICATION to machine learning: "neural ODEs" on manifolds, geometric flows
  for shape analysis, Ricci flow for graph neural networks.
```
<!-- @editor[content/P2]: The ML application note for Ricci flow is thin — one line with no detail. Specific gaps: (1) Ollivier-Ricci curvature on graphs (discrete analogue) detects community structure and bottlenecks; Forman-Ricci curvature on edges identifies graph surgery candidates — active research in network analysis. (2) The optimization landscape connection: positive sectional curvature in the loss landscape geometry correlates with saddle-point problems in training; negative curvature is exploited by second-order methods. (3) Normalized Ricci flow on compact surfaces: converges to constant curvature metric, providing the 2D classification (sphere, flat torus, hyperbolic surface) as a flow fixed point. -->

---

## Decision Cheat Sheet

| Curvature Tensor | Dimension | Information | Key Use |
|---|---|---|---|
| Riemann R_{ijkl} | n^2(n^2-1)/12 | Full curvature | Holonomy, sectional curvature |
| Ricci Ric_{ij} | n(n+1)/2 | Average over 2-planes | Einstein equations, comparison thms |
| Scalar R | 1 | Full trace | Gauss-Bonnet, energy conditions |
| Sectional K(sigma) | 1 per 2-plane | Curvature in a direction | Comparison geometry |
| Weyl W_{ijkl} | Conformal | Tidal forces, radiation | Conformal geometry, GR |
| Einstein G_{ij} | n(n+1)/2 | Ric - (1/2)gR | Source term in GR |

---

## Common Confusion Points

**"Curvature is the second derivative of the metric."**
Roughly: the Riemann tensor involves second derivatives of the metric (and products of first derivatives via Christoffel symbols). But in normal coordinates at a point, the first derivatives of g vanish, and R_{ijkl} = second derivatives of g (at that point). The Riemann tensor is the obstruction to locally flattening the metric.

**"Ricci curvature = 0 means flat."**
Ricci-flat (Ric = 0) is much weaker than flat (R = 0). A Ricci-flat manifold can have non-zero Riemann tensor (non-zero Weyl tensor). Calabi-Yau manifolds are Ricci-flat but highly curved. In GR, the vacuum equations are G = 0 (or equivalently Ric = 0 in 4D), yet gravitational waves and black holes are solutions — they are Ricci-flat but not flat.

**"Gauss-Bonnet only works in 2D."**
The classical Gauss-Bonnet is for 2-manifolds. The Chern-Gauss-Bonnet theorem generalizes to all even dimensions, and the Atiyah-Singer index theorem is a further vast generalization connecting differential geometry (curvature) to analysis (elliptic operators) and topology (characteristic classes).

<!-- @editor[content/P2]: Atiyah-Singer index theorem is mentioned here and in the decision table but not developed anywhere in the guide. For this learner (MIT TCS background, interested in gauge theory and ML), this is a priority: the index theorem says analytical index (dim ker D - dim coker D for elliptic operator D) equals topological index (integral of characteristic classes). Specific instance: Dirac operator on a spin manifold — index = A-hat genus; Dolbeault operator on a complex manifold — index = holomorphic Euler characteristic. The theorem also underlies the classification of anomalies in quantum field theory (chiral anomaly = index of Dirac operator). A short section with these examples would complete the curvature → topology → analysis chain. -->

**"The curvature tensor has n^4 components."**
The naive count is n^4, but the symmetries of Riemann reduce this to n^2(n^2-1)/12. For n=2: 1 component (Gaussian curvature). For n=3: 6 components. For n=4: 20 components. For n=10 (string theory): 825 independent components.
