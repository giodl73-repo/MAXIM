# Manifolds

## The Big Picture

```
+====================================================================+
|           MANIFOLDS — SPACES THAT LOCALLY LOOK LIKE Rⁿ           |
+====================================================================+
|                                                                    |
|  TOPOLOGICAL MANIFOLD M of dimension n:                           |
|  A Hausdorff, second-countable space that is locally homeomorphic |
|  to Rⁿ. Charts, atlases, no preferred coordinates globally.      |
|                                                                    |
|  SMOOTH MANIFOLD: topological manifold + compatible smooth atlas. |
|  Allows calculus: tangent vectors, derivatives, integrals.        |
|                                                                    |
|  RIEMANNIAN MANIFOLD: smooth manifold + metric tensor g.          |
|  Allows geometry: lengths, angles, curvature, geodesics.         |
|                                                                    |
|  CLASSIFICATION:                                                   |
|  Surfaces (2-manifolds): Σ_g (orientable) + RP²#... (unorient.)  |
|  3-manifolds: Thurston geometrization (8 geometries).             |
|  4-manifolds: still largely open (exotic R⁴, Donaldson theory).  |
|  n ≥ 5: surgery theory (Smale, Browder, Novikov) classifies many. |
+====================================================================+
```

---

## Topological Manifolds

### Definition and First Examples

```
TOPOLOGICAL n-MANIFOLD M:
  1. Hausdorff (distinct points have disjoint neighborhoods).
  2. Second countable (countable basis of open sets).
  3. Locally Euclidean: every point p ∈ M has a neighborhood U
     homeomorphic to Rⁿ (or the half-space Hⁿ = {x : xₙ ≥ 0} if p ∈ ∂M).

  The conditions 1+2 exclude pathological examples (long line, etc.).

MANIFOLDS WITH BOUNDARY:
  Interior points: neighborhood ≅ Rⁿ.
  Boundary points: neighborhood ≅ Hⁿ (half-space), xₙ ≥ 0.
  ∂M = set of boundary points. ∂M is an (n-1)-manifold (without boundary).

EXAMPLES:
  n=0: Finite discrete set (0-manifold without boundary).
  n=1: R, S¹, (0,1) (1-manifolds). With boundary: [0,1].
  n=2: R², S², T², Σ_g, RP², Klein bottle, Möbius band (with boundary).
  n=3: R³, S³, T³, S²×S¹, lens spaces, hyperbolic 3-manifolds.

NON-EXAMPLES:
  Figure 8 (not locally Euclidean at crossing point).
  Cone over S¹ at the cone point (not locally Rⁿ at tip).
  [0,1) × [0,1) at the corner (not locally R² or H² at corner).

ORIENTABILITY:
  An n-manifold M is orientable if it has a consistent "orientation" across all charts.
  Precisely: all transition maps have positive Jacobian determinant.
  Equivalently: the tangent bundle TM is trivial or the top cohomology Hⁿ(M;Z) = Z.

  Orientable surfaces: Σ_g (genus-g closed surfaces), S², T², cylinders.
  Non-orientable surfaces: RP², Klein bottle, Möbius band.
```

---

## Charts, Atlases, and Smooth Structure

### Charts and Coordinate Systems

```
CHART (coordinate system): A pair (U, φ) where:
  U ⊆ M is open.
  φ: U → Rⁿ is a homeomorphism onto an open subset of Rⁿ.
  φ assigns coordinates (x₁,...,xₙ) to each point of U.

TRANSITION MAP: Given two charts (U, φ) and (V, ψ) with U∩V ≠ ∅:
  φ ∘ ψ⁻¹: ψ(U∩V) → φ(U∩V)  is a map from Rⁿ to Rⁿ.

ATLAS: A collection {(Uα, φα)} of charts covering M.

C^∞ SMOOTH ATLAS: All transition maps φα ∘ φβ⁻¹ are C^∞ (infinitely differentiable).

SMOOTH MANIFOLD: A topological manifold with a maximal smooth atlas.
  "Maximal" = you've included every chart compatible with the smooth structure.
  A smooth structure is determined by any smooth atlas (take its maximal extension).

EXAMPLE: S² as smooth manifold.
  Chart 1 (stereographic from north): φ_N: S²\{N} → R²
    φ_N(x,y,z) = (x/(1-z), y/(1-z)).
  Chart 2 (stereographic from south): φ_S: S²\{S} → R²
    φ_S(x,y,z) = (x/(1+z), y/(1+z)).
  Transition: φ_N ∘ φ_S⁻¹ on R²\{0}: (u,v) ↦ (u/(u²+v²), v/(u²+v²)).
  This is C^∞ (even real-analytic). So S² has a smooth structure. ✓

EXOTIC SMOOTH STRUCTURES:
  Topological manifold can have MULTIPLE non-diffeomorphic smooth structures.
  Milnor (1956): S⁷ has 28 exotic smooth structures (exotic 7-spheres).
  R⁴ (exotic R⁴s): R⁴ has uncountably many non-diffeomorphic smooth structures —
    a unique phenomenon. Rⁿ for n≠4 has exactly one smooth structure (up to diffeo).
  Donaldson (1983): first proof via Yang-Mills gauge theory.
```

---

## Tangent Spaces and Tangent Bundle

### Tangent Vectors

```
TANGENT VECTOR at p ∈ M: An equivalence class of smooth curves through p.
  Two curves γ₁, γ₂: (-ε,ε) → M with γᵢ(0) = p are equivalent if
  (φ ∘ γ₁)'(0) = (φ ∘ γ₂)'(0)  in some (hence any) chart φ.

TANGENT SPACE TₚM:
  The set of all tangent vectors at p. This is an n-dimensional real vector space.

IN COORDINATES: If (U, x₁,...,xₙ) is a chart:
  TₚM has basis {∂/∂x₁|ₚ, ..., ∂/∂xₙ|ₚ}.
  A tangent vector v = Σ vⁱ ∂/∂xᵢ.

DERIVATION VIEW: Tangent vectors as derivations on smooth functions.
  v: C^∞(M) → R, linear, satisfies Leibniz: v(fg) = v(f)g(p) + f(p)v(g).
  This algebraic view is coordinate-free and extends to algebraic geometry.

TANGENT BUNDLE:
  TM = ∪_{p∈M} TₚM  (disjoint union of all tangent spaces).
  TM is itself a smooth 2n-manifold with a natural projection π: TM → M.
  (π: TₚM ↦ p.)
  TM → M is a VECTOR BUNDLE of rank n.

SECTIONS OF TM = VECTOR FIELDS:
  X: M → TM with π ∘ X = id_M.  X(p) ∈ TₚM.
  In coordinates: X = Σ Xⁱ(x) ∂/∂xᵢ.
  Lie bracket [X,Y] = X∘Y - Y∘X (another vector field).

COTANGENT BUNDLE T*M:
  T*M = ∪ₚ TₚM*  (dual spaces).
  Sections = 1-forms (differential forms of degree 1).
  In coordinates: ω = Σ ωᵢ(x) dxᵢ.
```

### Maps Between Manifolds

```
SMOOTH MAP: f: M → N smooth if in every pair of charts, the map is C^∞.

DIFFERENTIAL (PUSHFORWARD): df_p: TₚM → T_{f(p)}N.
  The linear map on tangent spaces induced by f.
  In coordinates: (df_p)_j^i = ∂f^i/∂x^j |_p (the Jacobian matrix).

IMMERSION: df_p is injective at every p.
  "M maps into N without self-intersection of tangent directions."
  Example: curve in R³ with nonzero velocity at each point.

EMBEDDING: An injective immersion that is a homeomorphism onto its image.
  Example: S² ↪ R³ (the standard sphere as a subspace of R³).

SUBMERSION: df_p is surjective at every p.
  Example: S³ → S² (Hopf fibration).
  By the Implicit Function Theorem: fibers f⁻¹(y) are submanifolds.

DIFFEOMORPHISM: Smooth bijection with smooth inverse.
  f: M → N diffeomorphism ↔ M and N are "the same" as smooth manifolds.

REGULAR VALUE THEOREM (inverse function theorem + implicit function):
  If f: Mⁿ → Nᵏ smooth and y ∈ N is a regular value (df_p surjective for all p ∈ f⁻¹(y)):
  Then f⁻¹(y) is a smooth (n-k)-dimensional submanifold of M.
  Example: f(x,y,z) = x²+y²+z² on R³, regular value 1 → f⁻¹(1) = S². ✓
```

---

## Riemannian Manifolds

```
RIEMANNIAN METRIC g: A smooth assignment of an inner product to each tangent space.
  g_p: TₚM × TₚM → R, symmetric, bilinear, positive definite.
  In coordinates: ds² = gᵢⱼ dxᵢ ⊗ dxⱼ  (the metric tensor).

EXAMPLES:
  Euclidean Rⁿ: gᵢⱼ = δᵢⱼ (standard inner product).
  S² ⊂ R³: induced metric from R³. In spherical: ds² = dθ² + sin²θ dφ².
  Hyperbolic plane H²: ds² = (dx² + dy²)/y² (upper half-plane).
    Constant curvature -1.

LENGTH AND DISTANCE:
  Length of curve γ: [a,b] → M:  L(γ) = ∫_a^b √{g(γ'(t), γ'(t))} dt.
  d(p,q) = inf{L(γ) : γ connects p to q}.
  A Riemannian manifold is a metric space.

GEODESIC: A curve γ that locally minimizes length.
  Satisfies: ∇_{γ'} γ' = 0  (covariant acceleration = 0).
  In coordinates: γ̈ᵏ + Γᵏᵢⱼ γ̇ⁱ γ̇ʲ = 0  (geodesic equation, Γ = Christoffel symbols).

  Examples:
  R² geodesics: straight lines.
  S² geodesics: great circles.
  H² geodesics: vertical lines and semicircles centered on x-axis.

CURVATURE:
  Riemann curvature tensor R(X,Y)Z = ∇_X∇_Y Z - ∇_Y∇_X Z - ∇_{[X,Y]}Z.
  Measures failure of parallel transport to commute.

  Gaussian curvature K (for surfaces):
    K > 0: sphere (elliptic geometry).
    K = 0: flat plane, cylinder, torus (Euclidean geometry).
    K < 0: hyperbolic plane (hyperbolic geometry).
    K = -1: "saddle surface."

  Gauss-Bonnet theorem:
    ∫_M K dA = 2π χ(M)  (for compact orientable surface without boundary).
    Connects curvature (local/differential) to Euler characteristic (global/topological).
    For S²: ∫_{S²} K dA = 4π = 2π · χ(S²) = 2π · 2. ✓
    For T²: ∫_{T²} K dA = 0 = 2π · 0. ✓

MORSE THEORY — TOPOLOGY FROM CRITICAL POINTS:
  A Morse function f: M → R (smooth, non-degenerate critical points)
  encodes the entire homology H*(M).

  As c sweeps from min(f) to max(f), the sublevel set M_c = {f ≤ c}:
    passes index-0 critical point → attach 0-cell (new component)
    passes index-1 critical point → attach 1-cell (merge or create cycle)
    passes index-k critical point → attach k-cell (k-handle)

  MORSE INEQUALITIES:
    bₖ(M) ≤ Cₖ   (Betti number ≤ count of index-k critical points)
    Σ(-1)ᵏ Cₖ = χ(M)   (strong Morse inequality)

  EXAMPLE — height function on T²:
    1 minimum (index 0), 2 saddles (index 1), 1 maximum (index 2).
    b₀ ≤ 1, b₁ ≤ 2, b₂ ≤ 1. Equality holds: b₀=1, b₁=2, b₂=1. ✓

  KEY APPLICATIONS:
  (1) Smale's h-cobordism theorem: canceling pairs of critical points
      shows W ≅ M×[0,1] in dim ≥ 6 → proves Poincaré conjecture dim ≥ 5.
  (2) TDA sublevel-set persistence = Morse theory on a filter function.
  (3) Floer homology = infinite-dimensional Morse theory on loop spaces.

CHERN-GAUSS-BONNET AND ATIYAH-SINGER:
  Gauss-Bonnet generalizes to arbitrary even-dimensional manifolds:
    ∫_M Pf(Ω/(2π)) = χ(M)   (Pf = Pfaffian of curvature 2-form matrix)

  The ATIYAH-SINGER INDEX THEOREM (1963) subsumes this:
    For an elliptic differential operator D on a compact manifold M:
    index(D) = dim ker(D) − dim coker(D) = ∫_M ch(σ(D)) · Td(TM ⊗ C)

  Special cases:
    D = d + d*  (de Rham)  → index = χ(M)  (Gauss-Bonnet)
    D = ∂̄ + ∂̄* (Dolbeault) → index = χ(O_M) (Hirzebruch-Riemann-Roch)
    D = Dirac operator      → index = Â(M)  (Â-genus)

  The index theorem connects analytical data (solutions of PDEs) to
  topological data (characteristic classes) — the apex of the differential
  topology → differential geometry → analysis bridge.
  Physics: the chiral anomaly in QFT = index of the Dirac operator.
```

---

## Classification of Manifolds

### 1-Manifolds

```
CLASSIFICATION (compact, without boundary):
  S¹ (the only compact connected 1-manifold).

CLASSIFICATION (compact, with boundary):
  [0,1] = I (the only compact connected 1-manifold with boundary).

PROOF SKETCH:
  Any compact 1-manifold is a finite union of arcs and circles.
  The connected cases: [0,1] (boundary = 2 points) or S¹ (no boundary).
```

### 2-Manifolds (Surfaces)

```
CLASSIFICATION OF COMPACT SURFACES (the fundamental theorem of surface theory):

ORIENTABLE SURFACES:
  Every compact connected orientable surface is homeomorphic to exactly one of:
  Σ_g = sphere with g handles (genus-g surface), for g = 0, 1, 2, ...

  Σ₀ = S² (sphere)
  Σ₁ = T² (torus)
  Σ₂ = double torus (two-holed torus)
  Σ_g: g handles attached to S².

  Invariant: genus g = number of handles = (1/2) rank H₁ = (1 - χ/2).
  χ(Σ_g) = 2 - 2g.

NON-ORIENTABLE SURFACES:
  Every compact connected non-orientable surface is homeomorphic to exactly one of:
  N_k = connected sum of k copies of RP², for k = 1, 2, 3, ...

  N₁ = RP² (projective plane)
  N₂ = Klein bottle
  N₃ = "dyck's surface"

  χ(N_k) = 2 - k.
  N₁ has χ=1, N₂ has χ=0, ...

  NOTE: Klein bottle = T² with one orientation-reversing twist (not embeddable in R³).

CONNECTED SUM:
  M#N = remove open disk from each, glue boundary circles.
  Σ_g#Σ_h = Σ_{g+h}.
  Σ_g # RP² = N_{2g+1} (connected sum of orientable + non-orientable = non-orientable).

KEY TOOLS FOR CLASSIFICATION:
  1. Triangulate (possible for any surface — Radó's theorem).
  2. Cut along curves to reduce to a polygon with identifications.
  3. Standard polygon word: Σ_g = a₁b₁a₁⁻¹b₁⁻¹...aₘbₘaₘ⁻¹bₘ⁻¹.
  4. Determine genus from Euler characteristic.

COMPLETE INVARIANTS: genus + orientability ↔ homeomorphism class.
```

### 3-Manifolds

```
THURSTON'S GEOMETRIZATION CONJECTURE (proved by Perelman, 2003):
  Every closed orientable 3-manifold can be cut into "geometric pieces,"
  each admitting one of 8 model geometries:
    S³, R³, H³ (constant curvature ±1, 0)
    S²×R, H²×R (product geometries)
    SL̃₂(R), Nil, Sol  (twisted geometries)

POINCARÉ CONJECTURE (special case of geometrization):
  Every simply connected compact 3-manifold is homeomorphic to S³.
  Open 1904–2003. Proved by Perelman using Ricci flow + surgery.
  First solved millennium problem.

RICCI FLOW:
  ∂gᵢⱼ/∂t = -2Rᵢⱼ  (metric evolves to become "more uniform").
  Hamilton introduced it (1982). Perelman added the "surgery" to handle singularities.
  Analogous to the heat equation for the metric.

CLASSIFICATION IS HARD:
  No complete invariant set known for 3-manifolds in general.
  Homeomorphism problem for 3-manifolds is decidable (Geometrization gives algorithm).
  But finding all invariants is active research.
```

### 4-Manifolds

```
4-MANIFOLDS: The wild west of topology.

INTERSECTION FORM:
  For compact oriented 4-manifold M, the cup product:
  H²(M;Z) × H²(M;Z) → H⁴(M;Z) ≅ Z
  is a symmetric bilinear form (over Z), the "intersection form."

CLASSIFICATION BY INTERSECTION FORM:
  TOPOLOGICAL (Freedman, 1982):
  Every symmetric bilinear form over Z (with some constraints) arises as the
  intersection form of a simply-connected compact topological 4-manifold.
  The manifold is classified up to homeomorphism by its intersection form +
  Kirby-Siebenmann invariant.

  SMOOTH (Donaldson, 1983):
  Constrains which forms can arise smoothly:
  If M is smooth and simply connected, its intersection form is either:
    - Diagonal (±1's on diagonal) — "standard" form.
    - Even type with signature divisible by 8.
  This means MOST topological 4-manifolds admit no smooth structure!

EXOTIC R⁴:
  There exist uncountably many smooth 4-manifolds homeomorphic to R⁴
  but pairwise non-diffeomorphic.
  None exist for Rⁿ with n ≠ 4.
  First found via Donaldson's work + Freedman's theorem.

E₈ MANIFOLD:
  The E₈ form (8×8 even positive definite matrix) gives a topological
  4-manifold (Freedman) that has no smooth structure (Donaldson).
```

### Higher Dimensional Manifolds

```
n ≥ 5: SURGERY THEORY
  Smale (h-cobordism theorem, 1960): If W is an h-cobordism between M and N
  (simply connected, dim ≥ 6), then W ≅ M×[0,1].
  Corollary (Generalized Poincaré conjecture in dim ≥ 5):
  M homotopy equivalent to Sⁿ (n ≥ 5) → M homeomorphic to Sⁿ.

SURGERY: Cut out Sᵏ × Dⁿ⁻ᵏ ⊂ M, replace with Dᵏ⁺¹ × Sⁿ⁻ᵏ⁻¹.
  Systematic way to build manifolds and classify them.

COBORDISM:
  Two n-manifolds M, N are cobordant if ∃ (n+1)-manifold W with ∂W = M ⊔ N.
  Cobordism classes form a ring under disjoint union (addition) and product (multiplication).
  Thom's theorem: oriented cobordism ring ⊗Q = Q[CP², CP⁴, CP⁶, ...] (polynomial on CP^{2k}'s).

COBORDISM → TQFT (the modern development connection):
  A TOPOLOGICAL QUANTUM FIELD THEORY (TQFT) is a symmetric monoidal functor:
    Z: Cob(n) → Vect
  Objects of Cob(n) = closed (n-1)-manifolds (boundaries).
  Morphisms = n-dimensional cobordisms between them.
  Z assigns a vector space to each boundary and a linear map to each cobordism.
  Atiyah's axioms (1988) formalize this.

  COBORDISM HYPOTHESIS (Lurie 2009):
    Fully extended n-dimensional TQFTs (extending down to points) are
    classified by fully dualizable objects in the target ∞-category.
    This is stated and proved in the language of (∞,n)-categories.
    It connects cobordism theory (the algebraic structure of manifold
    surgery) to the modern ∞-categorical framework.

  EXAMPLES:
    2D TQFT ↔ commutative Frobenius algebra (complete classification).
    3D Chern-Simons theory ↔ modular tensor category (Witten, Reshetikhin-Turaev).
    4D Donaldson/Seiberg-Witten theory ↔ smooth 4-manifold invariants.

EXOTICA IN HIGH DIMENSIONS:
  Kervaire-Milnor (1963): exotic n-spheres for n ≥ 7.
  Number of exotic n-spheres:
    n: 1,2,3,4,5,6,7,8,9,10,11,12,...
    #: 1,1,1,?,1,1,28,2,8,6,992,1,...
  (n=4 unknown — smooth 4-dim Poincaré conjecture open.)
```

---

## Fiber Bundles and Vector Bundles

```
FIBER BUNDLE: π: E → B with fiber F.
  Local trivialization: each x ∈ B has U∋x with π⁻¹(U) ≅ U × F (homeomorphism).
  Structure group G (acting on F): transition maps φ_αβ: U_α∩U_β → G.

EXAMPLES:
  Trivial bundle: B × F → B.
  Tangent bundle TM → M (fiber = Rⁿ, structure group GL(n,R)).
  Tautological bundle over RP^n (fiber = line in Rⁿ⁺¹ over the corresponding point).
  Hopf bundle S³ → S² (fiber S¹): η: (z₁,z₂) ↦ z₁/z₂ ∈ C∪{∞} = S².
  Frame bundle F(M) → M (fiber = GL(n,R), structure group GL(n,R)).

VECTOR BUNDLE: Fiber bundle with fiber Rᵏ and structure group GL(k,R).
  Each fiber is a k-dimensional vector space; transitions are linear.

SECTION of π: E → B: s: B → E with π ∘ s = id_B.
  Sections of TM = vector fields.
  Sections of T*M = 1-forms.
  Nowhere-zero sections: need "the bundle is trivial" (roughly).

HAIRY BALL THEOREM:
  Every vector field on S² has at least one zero.
  (You can't comb a hairy ball flat without a cowlick.)
  Proof: χ(S²) = 2 ≠ 0.  Poincaré-Hopf theorem: index sum of zeros = χ(M).
  Contrast: T² has χ=0 → vector fields with no zeros exist.

PRINCIPAL BUNDLE: Fiber bundle P → B with fiber G (a Lie group), G acting freely.
  G-bundle over B. Example: frame bundle (G = GL(n,R)).
  Connection on principal bundle = gauge field in physics.
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Define smooth manifold | Hausdorff + second-countable + smooth atlas (transition maps C^∞) |
| Classify compact surfaces | Genus (orientable) or cross-cap number (non-orientable); χ determines g |
| Distinguish smooth from homeomorphic | Look for exotic smooth structures (especially in dim 4 and 7) |
| Compute tangent bundle | Charts + overlap conditions; bundle over M with fiber TₚM ≅ Rⁿ |
| Build a manifold via surgery | Attach handles (Dᵏ × Dⁿ⁻ᵏ) to a manifold with boundary |
| Apply Gauss-Bonnet | ∫ K dA = 2π χ(M) for compact orientable surface |
| Prove no nowhere-zero vector field | χ(M) ≠ 0 (Poincaré-Hopf) |
| Classify 3-manifolds | Thurston geometrization (8 model geometries + decomposition) |
| Study smooth 4-manifolds | Intersection form + Donaldson theory / Seiberg-Witten invariants |
| Fibration with fiber F | Use Serre spectral sequence to compute cohomology of total space |

---

## Common Confusion Points

**"Smooth manifold = manifold with a smooth boundary."**
"Smooth" refers to the compatibility condition on transition maps (C^∞),
not the shape of any boundary. A manifold with boundary is a separate concept
(boundary points have half-space neighborhoods). A smooth manifold without
boundary has no boundary; a smooth manifold with boundary has a boundary
that is itself a smooth manifold (without boundary).

**"Every topological manifold has a unique smooth structure."**
False, especially in dimension 4 (and 7). Milnor's exotic S⁷ (1956) was the
first counterexample: a topological 7-sphere with a smooth structure not
diffeomorphic to the standard one. R⁴ admits uncountably many exotic smooth
structures. In dimensions 1, 2, 3: every topological manifold has a unique
smooth structure (up to diffeomorphism).

**"Orientability = having a well-defined inside and outside."**
Orientability means you can consistently choose a "handedness" (orientation)
for all tangent spaces. For surfaces in R³, this is roughly equivalent to
having two distinct sides — but in general, orientability is intrinsic to the
manifold itself, not dependent on any embedding. The Klein bottle is
non-orientable intrinsically, regardless of how you embed it.

**"The tangent bundle is always trivial."**
Parallelizable manifolds (TM trivial) include Rⁿ, T^n, S¹, S³, S⁷ (Adams's theorem:
only n=0,1,3,7 have trivial tangent bundle). S² is not parallelizable (hairy ball
theorem). Most manifolds have non-trivial tangent bundles, measured by characteristic
classes (Stiefel-Whitney, Pontryagin, Chern).

**"The Poincaré conjecture is solved in all dimensions."**
In dimensions n ≥ 5: solved by Smale (1961). In dimension 4: open for smooth
Poincaré conjecture (smooth 4-manifold homotopy equivalent to S⁴ → homeomorphic?
Freedman: yes topologically. Smooth: unknown). In dimension 3: Perelman (2003).
The smooth 4-dimensional Poincaré conjecture remains open.
