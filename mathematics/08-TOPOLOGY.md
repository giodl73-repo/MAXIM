# 08 — Topology: Continuity, Shape, and Invariants

```
THE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  POINT-SET TOPOLOGY          ALGEBRAIC TOPOLOGY         PHYSICS APPLICATIONS
  ┌────────────────────┐      ┌──────────────────────┐   ┌──────────────────┐
  │ Metric spaces      │      │ Homotopy             │   │ Topological ins. │
  │ Topological spaces │  →   │ Fundamental group π₁ │ → │ Quantum Hall eff.│
  │ Continuity         │      │ Homology groups      │   │ Fiber bundles    │
  │ Compactness        │      │ Euler characteristic │   │ Gauge fields     │
  │ Connectedness      │      │ Covering spaces      │   │ Monopoles, knots │
  └────────────────────┘      └──────────────────────┘   └──────────────────┘

  THE CENTRAL IDEA:
  Topology studies properties preserved under continuous deformation.
  Not distance, not angle, not area — just "can you get from here to there
  without cutting or gluing?"

  A coffee cup and a donut are topologically identical (both have one hole).
  A sphere and a torus are topologically distinct.
  The number of holes is a topological invariant — it doesn't change under
  continuous deformation.
═══════════════════════════════════════════════════════════════════════════════
```

---

## 1. Metric Spaces — Where Topology Starts

### 1.1 The Definition

A **metric space** (X, d) has a distance function d: X × X → ℝ satisfying:

```
  1. Non-negative:      d(x,y) ≥ 0, and d(x,y) = 0 ↔ x = y
  2. Symmetric:         d(x,y) = d(y,x)
  3. Triangle ineq:     d(x,z) ≤ d(x,y) + d(y,z)

  EXAMPLES:
  ℝⁿ with Euclidean:    d(x,y) = √(Σ(xᵢ-yᵢ)²)
  ℝⁿ with taxicab:      d(x,y) = Σ|xᵢ-yᵢ|         (L¹ norm)
  ℝⁿ with max:          d(x,y) = max|xᵢ-yᵢ|        (L∞ norm)
  C([a,b]) with sup:    d(f,g) = sup|f(x)-g(x)|    (function space)
  Discrete metric:      d(x,y) = 0 if x=y, 1 if x≠y
  Graph distance:       d(u,v) = length of shortest path
```

### 1.2 Open and Closed Sets in a Metric Space

```
  Open ball: B(x, r) = {y ∈ X | d(x,y) < r}   (strict inequality)

  OPEN SET U: for every x ∈ U, ∃r > 0 with B(x,r) ⊆ U
  (every point is an interior point — there's wiggle room)

  CLOSED SET: complement is open
  Equivalently: contains all its limit points
  (a sequence in the set converging to a limit → limit is in the set)

  EXAMPLES:
  ℝ: (a,b) open,  [a,b] closed,  [a,b) neither,  ℝ itself is both
  ℝ²: open disk {(x,y) | x²+y² < 1} is open
      closed disk {(x,y) | x²+y² ≤ 1} is closed

  WARNING: "Open" and "closed" are NOT opposites.
  A set can be: open, closed, both (clopen), or neither.
  ∅ and X are always both open AND closed.
```

### 1.3 Continuity — The Topological Definition

```
  EPSILON-DELTA (metric version):
  f: X → Y is continuous at x₀ if:
  ∀ε > 0, ∃δ > 0: d(x,x₀) < δ ⟹ d(f(x),f(x₀)) < ε

  TOPOLOGICAL VERSION (the "right" definition):
  f: X → Y is continuous if:
  for every open set V ⊆ Y, the preimage f⁻¹(V) is open in X

  Why is this better?
  ├── Works without a metric (pure topology)
  ├── Generalizes to any topological space
  └── Composition of continuous maps is continuous: trivially f⁻¹(g⁻¹(V)) = (g∘f)⁻¹(V)

  EQUIVALENT CHARACTERIZATIONS:
  f continuous ↔ preimage of every open set is open
                ↔ preimage of every closed set is closed
                ↔ f(x_n → x) = f(x_n) → f(x)  [in metric spaces]
```

---

## 2. Topological Spaces

### 2.1 The Abstract Definition

A **topology** on X is a collection τ of subsets of X (the "open sets") satisfying:

```
  1. ∅ ∈ τ and X ∈ τ
  2. Arbitrary unions of open sets are open:  ∪ᵢ Uᵢ ∈ τ
  3. Finite intersections of open sets are open: U₁ ∩ U₂ ∈ τ

  The pair (X, τ) is a TOPOLOGICAL SPACE.

  Note: infinite intersections need not be open.
  ∩ₙ₌₁^∞ (-1/n, 1/n) = {0}  ← not open in ℝ

  EXAMPLES OF TOPOLOGIES ON X:
  Discrete topology:  τ = 𝒫(X) (every subset is open)
  Indiscrete topology: τ = {∅, X} (coarsest possible)
  Metric topology:    τ = all sets that are open in the metric sense
  Subspace topology:  if A ⊆ X, τ_A = {U ∩ A | U ∈ τ}
  Product topology:   X × Y, open sets = unions of U × V (U open in X, V in Y)
```

### 2.2 Key Topological Properties

```
  HAUSDORFF (T₂): distinct points have disjoint neighborhoods
  ∀x ≠ y, ∃ open U∋x, V∋y with U ∩ V = ∅
  All metric spaces are Hausdorff. Hausdorff = points can be "separated."
  Non-Hausdorff: Zariski topology in algebraic geometry.

  COMPACTNESS: every open cover has a finite subcover
  Intuition: "finite in spirit" — can't escape to infinity

  Heine-Borel theorem (ℝⁿ): compact ↔ closed and bounded
  Unit interval [0,1] is compact. ℝ is not. Open interval (0,1) is not.

  KEY THEOREMS FOR COMPACT SPACES:
  ├── Continuous image of compact = compact  (f(K) compact if K compact)
  ├── Continuous f: K → ℝ attains max and min  (extreme value theorem)
  └── Compact + Hausdorff → normal (points and closed sets separable)

  CONNECTEDNESS: X cannot be written as union of two disjoint open sets
  Path-connectedness: ∀x,y ∈ X, ∃ continuous γ: [0,1] → X with γ(0)=x, γ(1)=y
  Path-connected ⟹ connected (converse fails: topologist's sine curve)
```

---

## 3. Homeomorphisms — Topological Equivalence

### 3.1 Definition

```
  A HOMEOMORPHISM is a bijection f: X → Y such that both f and f⁻¹ are continuous.
  X ≅ Y (homeomorphic) means they have the same topological structure.

  "Same shape" in topology = homeomorphic.

  FAMOUS HOMEOMORPHISMS:
  ├── Open interval (-1,1) ≅ ℝ       [via f(x) = tan(πx/2)]
  ├── Any open interval ≅ ℝ
  ├── Open disc ≅ ℝ²
  ├── Circle S¹ ≅ square boundary
  ├── Sphere S² ≅ surface of cube
  └── Coffee cup ≅ torus (donut)     [the famous one]

  NOT HOMEOMORPHIC:
  ├── Circle ≇ line ℝ  (remove one point: circle stays connected, line splits)
  ├── Sphere S² ≇ torus T²  (different number of holes)
  └── ℝ ≇ ℝ²  (remove one point: ℝ splits, ℝ² stays connected)
```

### 3.2 Topological Invariants

A **topological invariant** is a property preserved by homeomorphisms:

```
  INVARIANT                  SPHERE S²    TORUS T²    Figure-8
  ──────────────────────────────────────────────────────────────
  Compactness                Yes          Yes         Yes
  Connectedness              Yes          Yes         Yes
  Simply connected?          Yes          No          No
  Euler characteristic χ     2            0           -1 (debatable)
  Fundamental group π₁       trivial {0}  ℤ×ℤ         free group F₂
  ──────────────────────────────────────────────────────────────
  If any invariant differs → spaces are NOT homeomorphic.
  Invariants can prove non-homeomorphism; equal invariants don't prove homeomorphic.
```

---

## 4. Homotopy and the Fundamental Group

### 4.1 Homotopy

```
  Two continuous maps f, g: X → Y are HOMOTOPIC (f ≃ g) if there exists
  a continuous deformation H: X × [0,1] → Y with H(x,0) = f(x), H(x,1) = g(x)

  H is the HOMOTOPY — a continuous family of maps interpolating f to g.

  Intuition: f and g can be continuously deformed into each other.

  A space X is CONTRACTIBLE if the identity map id: X → X is homotopic to
  a constant map (map everything to one point).
  ℝⁿ is contractible. S¹ (circle) is not.
```

### 4.2 Loops and the Fundamental Group

```
  A LOOP at basepoint x₀ ∈ X is: γ: [0,1] → X with γ(0) = γ(1) = x₀

  Two loops are HOMOTOPIC if one can be continuously deformed into the other
  while keeping the basepoint fixed.

  FUNDAMENTAL GROUP π₁(X, x₀):
  Elements = homotopy classes of loops at x₀
  Group operation = concatenation of loops: [γ₁]·[γ₂] = [γ₁ then γ₂]
  Identity = constant loop at x₀
  Inverse of [γ] = [γ traversed backwards]

  ┌──────────────────────────────────────────────────────────────────┐
  │  SPACE X          │  π₁(X)          │  MEANING                   │
  ├──────────────────────────────────────────────────────────────────┤
  │  ℝⁿ               │  {e} (trivial)  │  all loops contractible   │
  │  S¹ (circle)      │  ℤ              │  loop winds n times       │
  │  S² (sphere)      │  {e} (trivial)  │  all loops shrinkable     │
  │  Torus T²         │  ℤ × ℤ          │  wind m times in each dir │
  │  Figure-8         │  F₂ (free group)│  non-abelian!             │
  │  ℝ³\{0}           │  {e}            │  go around origin in 3D   │
  │  ℝ³\{line}        │  ℤ              │  wind around the line     │
  │  RP²              │  ℤ/2ℤ           │  spin-½ connection!       │
  └──────────────────────────────────────────────────────────────────┘

  SIMPLY CONNECTED: π₁ = {e} (trivial) — every loop can be shrunk to a point.
  ℝⁿ, S² are simply connected.
  Circle S¹, torus T² are NOT simply connected.
```

### 4.3 Van Kampen's Theorem

```
  If X = U ∪ V with U, V open, path-connected, and U ∩ V path-connected:

  π₁(X) = π₁(U) *_{π₁(U∩V)} π₁(V)    (amalgamated free product)

  Simple case: if U ∩ V is simply connected:
  π₁(X) = π₁(U) * π₁(V)    (free product)

  EXAMPLE: Figure-8 = circle ∪ circle glued at one point
  π₁(circle) = ℤ, intersection = {point} → π₁ = ℤ * ℤ = F₂ (free group on 2 generators)
```

---

## 5. Covering Spaces

```
  A COVERING SPACE of X is a space X̃ with a map p: X̃ → X such that
  every point of X has a neighborhood U with p⁻¹(U) = disjoint union of
  open sets in X̃, each mapping homeomorphically to U.

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────┐
  │  p: ℝ → S¹,  p(t) = e^(2πit)                                    │
  │  The real line "wraps around" the circle.                       │
  │  Fiber p⁻¹(x₀) = ℤ (all integers, equally spaced)               │
  │                                                                 │
  │  p: S² → RP²  (antipodal map)                                   │
  │  Sphere double-covers real projective plane.                    │
  │  Fiber = 2 points.                                              │
  │                                                                 │
  │  p: SU(2) → SO(3)  (the spin covering!)                         │
  │  SU(2) ≅ S³ double-covers SO(3) ≅ RP³                           │
  │  This is why spin-½ exists — SU(2) is the universal cover       │
  └─────────────────────────────────────────────────────────────────┘

  MONODROMY: as you go around a loop in X, the fiber points permute.
  Going around the circle once in S¹ lifts to going from n to n+1 in ℝ.
  Going around a loop in SO(3) once lifts to either a loop or a path
  (depending on whether the loop is trivial in π₁(SO(3)) = ℤ/2ℤ).
```

---

## 6. Euler Characteristic and Surfaces

### 6.1 Euler Characteristic

```
  For a polyhedron (V vertices, E edges, F faces):
  χ = V - E + F

  EXAMPLES:
  Tetrahedron: 4 - 6 + 4 = 2
  Cube:        8 - 12 + 6 = 2
  Octahedron:  6 - 12 + 8 = 2
  All convex polyhedra: χ = 2  (homeomorphic to sphere S²)

  Torus (triangulated): χ = 0
  Double torus (genus 2): χ = -2
  Sphere S²: χ = 2

  GENERAL FORMULA for orientable surface of genus g (g holes):
  χ = 2 - 2g

  g=0 (sphere):    χ = 2
  g=1 (torus):     χ = 0
  g=2 (pretzel):   χ = -2
```

### 6.2 Classification of Compact Surfaces

```
  Every compact connected surface is homeomorphic to exactly one of:
  ├── Orientable: sphere, torus, double torus, ... (genus g = 0, 1, 2, ...)
  └── Non-orientable: RP², Klein bottle, ... (crosscap number k = 1, 2, ...)

  ORIENTABLE SURFACES:
  ┌─────────────────────────────────────────────────────────────────┐
  │                 ○    ○──○    ○──○──○                            │
  │  Sphere  Torus     Genus 2    Genus 3 ...                       │
  │  χ=2     χ=0       χ=-2       χ=-4                              │
  └─────────────────────────────────────────────────────────────────┘

  MÖBIUS BAND: non-orientable surface with boundary
  (one-sided: an ant walking on it visits both "sides")
  REAL PROJECTIVE PLANE RP²: compact, non-orientable, no boundary
  KLEIN BOTTLE: like two Möbius bands glued — can't exist in ℝ³ without self-intersection
```

### 6.3 Gauss-Bonnet Theorem (Preview of Differential Geometry)

```
  For a compact surface M:
  ∫∫_M K dA = 2π χ(M)

  K = Gaussian curvature (intrinsic — measured without embedding)
  χ = Euler characteristic (topological invariant)

  STUNNING CONSEQUENCE:
  Total curvature of a surface depends only on its topology, not its geometry!
  Deform a sphere however you like: the total curvature always equals 4π.
  Poke it, squish it, stretch it: ∫K dA = 4π always.

  For Einstein's GR: the analog is ∫R dV (total scalar curvature),
  and the Gauss-Bonnet-Chern theorem generalizes this to 4D.
```

---

## 7. Topology in Physics

### 7.1 Topological Insulators

```
  Ordinary insulator: band gap everywhere in Brillouin zone
  Topological insulator: band gap in bulk, BUT conducting surface states
                         that cannot be removed without closing the gap

  WHY TOPOLOGY: the band structure defines a map from the Brillouin zone
  (a torus T²) to the space of Hamiltonians. The topological invariant
  of this map (the Chern number Z) classifies the insulator.

  Chern number = (1/2π) ∫∫_BZ Berry curvature dkx dky
  (Berry curvature = curvature of the "Berry connection" = U(1) gauge field!)

  INTEGER quantum Hall effect: Hall conductance σ_xy = n e²/h  (n = Chern number)
  Fractional QHE: even richer — topological order, anyons.

  This is not abstract: it's a TQFT (topological quantum field theory) application
  driving the search for topological quantum computers.
```

### 7.2 Fiber Bundles — The Right Language for Gauge Theory

```
  A FIBER BUNDLE consists of:
  ├── Base space B    (spacetime, Brillouin zone, ...)
  ├── Fiber F         (internal space at each point)
  ├── Total space E   (all fibers together)
  └── Projection π: E → B  (each point in E projects to base)

  Locally: E looks like B × F  (product)
  Globally: E may be "twisted"

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Möbius band:  base = S¹, fiber = interval [-1,1], twisted           │
  │  Cylinder:     base = S¹, fiber = interval [-1,1], untwisted         │
  │  Tangent bundle TM: base = M, fiber = tangent space Tₓ M at each x   │
  │  EM gauge theory:  base = spacetime, fiber = U(1), connection = Aμ   │
  │  Yang-Mills (weak): base = spacetime, fiber = SU(2)                  │
  └──────────────────────────────────────────────────────────────────────┘

  GAUGE FIELD = CONNECTION on a principal fiber bundle.
  The EM 4-potential Aμ is not "the field" — it's the connection on a U(1) bundle.
  The field strength Fμν = ∂μAν - ∂νAμ is the CURVATURE of that connection.
  This is why gauge invariance isn't mysterious: it's the freedom to choose
  local sections of the bundle (change of gauge = change of local trivialization).
```

### 7.3 Magnetic Monopoles and Topology

```
  WHY MONOPOLES ARE TOPOLOGICAL:
  If a magnetic monopole existed at the origin, the B field would be:
  B = g r̂/r²   (like a "magnetic Coulomb" field)

  The vector potential A cannot be defined everywhere on S² surrounding the monopole.
  (If A existed everywhere: B = ∇×A → ∇·B = 0, but ∇·B = 4πg δ³(r) ≠ 0)

  Resolution (Dirac 1931): define A in two patches (N and S hemispheres).
  On the overlap (equator), they differ by a gauge transformation.
  For this to be single-valued: the gauge transformation must be a loop in U(1).
  Loop in U(1): characterized by an integer n ∈ π₁(U(1)) = π₁(S¹) = ℤ.

  DIRAC QUANTIZATION CONDITION:
  eg/ℏc = n/2   (n integer)
  If monopoles exist, all electric charges must be integer multiples of e.
  This would explain why charge is quantized!
  The argument is purely topological.
```

### 7.4 Topological Defects

```
  Phase transitions can create topological defects when topology prevents
  a field from being uniform everywhere.

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Vortices (2D superfluid): π₁(U(1)) = ℤ → quantized vortex lines     │
  │  Strings (3D, symmetry breaking): π₁(vacuum manifold) ≠ 0            │
  │  Monopoles (3D): π₂(vacuum manifold) ≠ 0                             │
  │  Textures: π₃(vacuum manifold) ≠ 0                                   │
  │  Domain walls: π₀(vacuum manifold) ≠ 0  (discrete symmetry broken)   │
  └──────────────────────────────────────────────────────────────────────┘

  The homotopy groups πₙ classify which topological defects are stable:
  π₀: point-like (domain walls, kinks)
  π₁: line-like (vortices, cosmic strings)
  π₂: surface-like (monopoles)
  π₃: textures (Skyrmions in nuclear physics)
```

---

## 8. Higher Homotopy Groups (Brief)

```
  πₙ(X, x₀) = homotopy classes of maps Sⁿ → X (fixing basepoint)

  π₁: maps from circle S¹ → X  (loops — the fundamental group)
  π₂: maps from sphere S² → X  (2-spheres in X)
  π₃: maps from S³ → X

  π₁(S¹) = ℤ        (winding number)
  π₂(S²) = ℤ        (degree of a map)
  π₃(S²) = ℤ        (Hopf fibration — S³ → S² with fiber S¹, non-trivial!)
  πₙ(Sⁿ) = ℤ for all n ≥ 1

  The HOPF FIBRATION π: S³ → S²:
  S³ = unit sphere in ℂ² (4D real space)
  Each fiber = S¹ (a circle)
  Linked fibers → non-trivial bundle
  Appears in: QM state space (Bloch sphere), liquid crystal defects
```

## 9. Homology Groups

Before TDA, the algebraic machinery needs to be in place.

```
  SIMPLICIAL COMPLEX: a combinatorial model for a topological space.
  Built from simplices glued along faces.
  0-simplex: point (vertex)
  1-simplex: edge (between two vertices)
  2-simplex: filled triangle (three vertices + three edges + interior)
  k-simplex: convex hull of k+1 affinely independent points

  CHAIN COMPLEX:
  Cₙ = free abelian group on n-simplices  (formal ℤ-linear combinations)
  Boundary operator ∂ₙ: Cₙ → Cₙ₋₁:
  ∂[v₀,...,vₙ] = Σᵢ (-1)ⁱ [v₀,...,v̂ᵢ,...,vₙ]  (omit the i-th vertex)

  ┌─────────────────────────────────────────────────────────────────────┐
  │  ... → C₂ →^∂₂ C₁ →^∂₁ C₀ → 0                                       │
  │                                                                     │
  │  KEY IDENTITY: ∂²= 0  (boundary of a boundary is empty)             │
  │  Algebraic proof: the (-1)ⁱ signs cause exact cancellation.         │
  │  This mirrors d²=0 from differential forms — same structure.        │
  └─────────────────────────────────────────────────────────────────────┘

  SINGULAR HOMOLOGY Hₙ(X; ℤ):
  Hₙ = ker(∂ₙ) / im(∂ₙ₊₁)  =  (n-cycles) / (n-boundaries)
  ├── n-cycle: chain with zero boundary (∂z = 0) — a "closed" loop or surface
  ├── n-boundary: chain that is ∂ of something — "fills in"
  └── Hₙ measures cycles that are NOT boundaries = "genuine holes"

  EXAMPLES:
  ┌──────────────────────────────────────────────────────────────────────┐
  │  Space X     │  H₀      │  H₁      │  H₂      │  Interpretation      │
  ├──────────────────────────────────────────────────────────────────────┤
  │  Point       │  ℤ       │  0       │  0       │  1 component       │
  │  S¹ (circle) │  ℤ       │  ℤ       │  0       │  1 loop            │
  │  S²          │  ℤ       │  0       │  ℤ       │  1 enclosed void   │
  │  Torus T²    │  ℤ       │  ℤ²      │  ℤ       │  2 independent loops│
  │  RP²         │  ℤ       │  ℤ/2ℤ   │  0       │  torsion!          │
  │  Klein bottle│  ℤ       │  ℤ⊕ℤ/2  │  0       │  non-orientable    │
  └──────────────────────────────────────────────────────────────────────┘

  BETTI NUMBERS bₙ = rank(Hₙ) over ℤ (free part):
  b₀ = number of connected components
  b₁ = number of independent loops
  b₂ = number of enclosed voids
  EULER CHARACTERISTIC: χ = Σₙ (-1)ⁿ bₙ  (Betti numbers → χ)
  For the torus: χ = b₀ - b₁ + b₂ = 1 - 2 + 1 = 0 ✓

  MAYER-VIETORIS SEQUENCE (computing homology of glued spaces):
  If X = U ∪ V:
  ... → Hₙ(U∩V) → Hₙ(U) ⊕ Hₙ(V) → Hₙ(X) → Hₙ₋₁(U∩V) → ...
  Long exact sequence. Works like Van Kampen for π₁ but for all Hₙ.

  EXAMPLE (Torus T² = S¹ × S¹):
  Use Künneth formula: Hₙ(X×Y) = ⊕_{i+j=n} Hᵢ(X) ⊗ Hⱼ(Y)
  H₀(T²) = ℤ, H₁(T²) = ℤ², H₂(T²) = ℤ ✓

  COMPARISON WITH π₁:
  Hₙ is ABELIAN (always); π₁ can be non-abelian.
  In fact: H₁(X) = π₁(X)^{ab} (abelianization of fundamental group).
  Homology is computable; homotopy groups are generally undecidable (πₙ(Sⁿ) hard).
  This is why TDA uses homology, not homotopy.
```

## 10. Topological Data Analysis

```
  TDA CONNECTS: algebraic topology → point cloud data → computable invariants.

  THE FILTRATION IDEA:
  Given a point cloud X ⊂ ℝᵈ, build a family of simplicial complexes:
  for each scale r: Xᵣ = (complex built from X at scale r)

  As r increases, more simplices are added → topological features appear/disappear.

  VIETORIS-RIPS COMPLEX at scale r:
  Include the k-simplex [v₀,...,vₖ] if d(vᵢ,vⱼ) ≤ r for all pairs i,j.
  (Complete graph on all points within distance r, then fill cliques.)

  ČECH COMPLEX at scale r:
  Include [v₀,...,vₖ] if the balls B(vᵢ, r/2) have a common intersection.
  (More geometrically natural; Nerve Lemma: Čech ≃ ∪ₓ B(x,r) homotopically.)
  Vietoris-Rips ⊆ Čech ⊆ Vietoris-Rips(2r): they're interleaved.

  PERSISTENT HOMOLOGY:
  Track how homology classes appear and disappear as r increases.

  BIRTH-DEATH PAIRING:
  Each connected component, loop, void is "born" at some scale r_birth
  and "dies" (merges/fills) at some scale r_death.

  ┌────────────────────────────────────────────────────────────────────┐
  │  PERSISTENCE BARCODE: one horizontal bar per feature               │
  │  r:   0  ──────────────────────────────────────────────► ∞         │
  │  H₀:  ───── ──── ──── ──  ─    (components merging)                │
  │  H₁:                ────────  ──── ─  (loops appearing/dying)      │
  │  Long bars = topologically significant features                    │
  │  Short bars = noise                                                │
  │                                                                    │
  │  PERSISTENCE DIAGRAM: scatter plot of (birth, death) pairs.        │
  │  Points near the diagonal = noise; points far from diagonal =      │
  │  genuine topological signal.                                       │
  └────────────────────────────────────────────────────────────────────┘

  STABILITY THEOREM (Cohen-Steiner-Edelsbrunner-Harer):
  If point clouds X and Y have Hausdorff distance δ:
  Wasserstein distance between their persistence diagrams ≤ δ.
  TDA features are stable under small perturbations — they're not noise artifacts.

  MAPPER ALGORITHM (Singh-Mémoli-Carlsson 2007):
  Graph-based summary of high-dimensional data shape.

  1. Choose filter function f: X → ℝ (e.g., density, first PCA component)
  2. Cover range of f with overlapping intervals U₁,...,Uₖ
  3. For each Uᵢ: cluster f⁻¹(Uᵢ) → each cluster = a node
  4. Connect nodes whose clusters share data points (overlapping intervals)
  5. Result: a graph that captures topological shape

  Mapper discovers "flares," "loops," "branches" in data — structure
  invisible to PCA (which only captures linear subspaces).
  Used to discover cancer subtypes, athlete motion patterns.

  COMPUTATIONAL ENTRY POINTS:
  Ripser (C++/Python) — fastest persistent homology for Vietoris-Rips
  Gudhi (Python/C++) — full TDA library: Rips, Čech, alpha, Mapper
  scikit-tda — sklearn-compatible TDA tools
  giotto-tda — end-to-end TDA pipeline for ML

  # Compute H₁ of a point cloud
  import ripser
  dgms = ripser.ripser(X)['dgms']  # dgms[k] = persistence diagram for Hₖ
  # Each row: [birth, death] pair

  APPLICATIONS IN ML:
  ├── Shape of loss landscapes: H₁ of sublevel sets counts "basins"
  ├── Topological regularization: add persistence-based penalties to loss
  ├── Cycle detection in data: H₁ detects loops (e.g., in time series)
  └── Network architecture analysis: topology of activation spaces
```

### 10.1 Topological Complexity and TCS Connections

```
  TOPOLOGICAL COMPLEXITY (Farber 2003):
  TC(X) = the motion planning complexity of a space.

  PROBLEM: Given a configuration space X, plan a path from any start to any goal.
  A motion planner is a continuous map s: X×X → PX (path space), s(x,y) = a path from x to y.
  TC(X) = minimum number of open sets U covering X×X, each admitting a continuous local planner.

  TC(ℝⁿ) = 1  (trivial: go in a straight line — one global planner)
  TC(S¹) = 2   (circle: need two planners — the "antipodal" case requires separate handling)
  TC(Sⁿ) = 2 for n odd, 1 for n even (connected to vector field problems)
  TC(T²) = 3  (torus — reflects non-commutativity of path composition)

  Related to Schwarz genus (sectional category) of the fibration:
  PX → X×X.  TC(X) is a homotopy invariant — homeomorphic spaces have the same TC.

  APPLICATIONS: robot motion planning, automated surgery (minimizing
  the number of "control regimes" needed to cover all configurations).

  ────────────────────────────────────────────────────────────────────
  π₁ AND THE WORD PROBLEM:

  The fundamental group π₁(X) of a CW-complex X is presented by:
  Generators: one per 1-cell
  Relations: one per 2-cell (boundary word = identity)

  Example: torus T² = one 0-cell, two 1-cells (a,b), one 2-cell (boundary = aba⁻¹b⁻¹)
  π₁(T²) = ⟨a, b | aba⁻¹b⁻¹⟩ = ℤ × ℤ  (the relation makes a,b commute)

  THE WORD PROBLEM for a group G = ⟨generators | relations⟩:
  Given a word w in generators: is w = identity in G?

  For π₁: deciding if a loop is contractible = solving the word problem for π₁.
  For general finitely presented groups: UNDECIDABLE (Novikov 1955, Adian 1957).
  For specific groups: decidable (hyperbolic groups via automatic group theory).

  This connects topology directly to computability theory:
  The topology of a space can encode undecidable decision problems.

  ────────────────────────────────────────────────────────────────────
  HOMOTOPY TYPE THEORY (HoTT):

  HoTT (Voevodsky et al.) identifies:
  Types (in type theory)    ↔  Spaces (in homotopy theory)
  Terms of type A           ↔  Points in space A
  Propositions              ↔  Spaces with at most one point (contractible or empty)
  Equality proofs p: a=b    ↔  Paths from a to b
  Proofs of proofs          ↔  Homotopies between paths
  Higher identity types     ↔  Higher homotopy groups πₙ

  UNIVALENCE AXIOM (Voevodsky): equivalent types are equal.
  This makes isomorphisms "computationally real" — transport along proofs
  of equivalence is function application.

  Implemented in: Agda, Coq (with HoTT library), Lean 4 (Mathlib).
  HoTT provides a foundation for mathematics where proof = computation,
  directly in the spirit of the Curry-Howard correspondence.
```

### 5.1 The Galois Correspondence for Covering Spaces

```
  UNIVERSAL COVER X̃:
  The unique simply-connected covering space of X (when it exists).
  Every other covering space is a quotient of X̃ by a subgroup of π₁(X).

  THE GALOIS CORRESPONDENCE:
  (Covers of X up to isomorphism) ↔ (Subgroups of π₁(X, x₀))

  ┌─────────────────────────────────────────────────────────────────────┐
  │  Cover p: X̃ → X        │  Subgroup H ≤ π₁(X, x₀)                    │
  │  Universal cover        │  H = {e} (trivial subgroup)               │
  │  X itself (trivial)     │  H = π₁(X) (whole group)                  │
  │  n-sheeted cover        │  [π₁:H] = n (index n subgroup)            │
  │  Normal cover           │  H ◁ π₁ (normal subgroup)                 │
  │  Deck transformations   │  π₁/H (quotient when H normal)            │
  └─────────────────────────────────────────────────────────────────────┘

  This is exactly analogous to Galois theory:
  (Field extensions of F) ↔ (Subgroups of Gal(L/F))
  Covering space theory IS Galois theory, with π₁ playing the role of the
  Galois group. Both are instances of the same categorical structure.

  DECK TRANSFORMATIONS (covering automorphisms):
  A deck transformation is a homeomorphism φ: X̃ → X̃ with p∘φ = p.
  For the universal cover X̃: Deck(X̃/X) ≅ π₁(X).
  The group acts freely and properly discontinuously on X̃.
  X ≅ X̃ / π₁(X)  (original space = universal cover mod the group action).

  EXAMPLES:
  ┌─────────────────────────────────────────────────────────────────────┐
  │  X = S¹:  X̃ = ℝ,  π₁(S¹) = ℤ                                        │
  │  Deck transformations: t ↦ t + n (integer translations)             │
  │  S¹ = ℝ/ℤ ✓                                                         │
  │                                                                     │
  │  X = SO(3):  X̃ = SU(2) ≅ S³,  π₁(SO(3)) = ℤ/2ℤ                      │
  │  Deck transformations: {id, antipodal map on S³}                    │
  │  SO(3) = S³/(ℤ/2ℤ) = RP³ ✓                                          │
  │                                                                     │
  │  X = torus T²:  X̃ = ℝ²,  π₁(T²) = ℤ²                                │
  │  Deck transformations: (m,n) integer lattice translations           │
  │  T² = ℝ²/ℤ² ✓                                                       │
  └─────────────────────────────────────────────────────────────────────┘

  MONODROMY REPRESENTATION:
  Given a cover p: X̃ → X and basepoint x₀ ∈ X, choose fiber F = p⁻¹(x₀).
  A loop γ ∈ π₁(X, x₀) permutes the fiber F (lift γ, see where each fiber
  point ends up). This gives a group homomorphism:
  ρ: π₁(X, x₀) → Sym(F)   (the monodromy representation)

  For an n-sheeted cover: ρ: π₁(X) → Sₙ.
  Normal cover ↔ image of ρ acts transitively AND ρ factors through a
  normal subgroup → regular representation.

  IN PHYSICS: monodromy of the Schrödinger equation around a singularity
  in parameter space gives the monodromy matrix — the quantum analog of
  deck transformations for energy level crossings (conical intersections).
```

---

## Decision Cheat Sheet

| Question | Answer |
|---------|--------|
| Are (a,b) and [a,b] homeomorphic? | No — [a,b] compact, (a,b) not |
| Is ℝ homeomorphic to ℝ²? | No — remove a point: ℝ disconnects, ℝ² doesn't |
| What's the fundamental group of a circle? | ℤ (winding number) |
| What's the fundamental group of a torus? | ℤ × ℤ |
| Is the sphere S² simply connected? | Yes — π₁(S²) = {e} |
| Why does spin-½ exist? | SU(2) double-covers SO(3): π₁(SO(3)) = ℤ/2ℤ |
| What is a gauge field mathematically? | Connection on a principal fiber bundle |
| What is the field strength Fμν? | Curvature of the connection |
| What classifies topological insulators? | Chern number (∈ ℤ), a topological invariant |
| What is the Dirac quantization condition? | eg/ℏc = n/2, from π₁(U(1)) = ℤ |
| Euler characteristic of a genus-g surface? | χ = 2 - 2g |

---

## Common Confusion Points

**"Open and closed sound like opposites. Why can a set be both?"**
"Open" and "closed" are defined by two separate conditions, not as complements of each other. The conditions happen to be complementary for the *whole* collection of open sets — the complement of any open set is closed. But for a *specific* set, being open says nothing about whether its complement is open. The real line ℝ itself is both open (trivially — all of X is always declared open) and closed (complement is ∅, which is also always open).

**"What's the difference between homotopy equivalence and homeomorphism?"**
Homeomorphism: bijective continuous map with continuous inverse — the spaces are literally "the same shape." Homotopy equivalence: there exist maps f: X → Y and g: Y → X such that g∘f ≃ id_X and f∘g ≃ id_Y (composites are homotopic to identity). Homotopy equivalence allows collapsing: a disc D² is homotopy equivalent to a point (contractible), but not homeomorphic to a point. Homotopy is coarser — same "holes" but not necessarily same "size."

**"The Euler characteristic seems too simple to be deep."**
It seems like just counting. But χ is a topological invariant — deform the surface however you like, triangulate it however you like, χ doesn't change. And Gauss-Bonnet equates it to the integral of curvature — something analytic. This bridges topology (discrete counting) and differential geometry (integration). The generalization (Atiyah-Singer index theorem) is one of the most profound results in 20th-century mathematics, connecting topology, analysis, and geometry.

**"How is Aμ a connection on a bundle if it's just a 4-vector?"**
At each spacetime point x, the internal space is U(1) = S¹. A "connection" tells you how to parallel-transport vectors in the fiber as you move through the base. For U(1), this is specified by a 1-form on spacetime (the connection 1-form) — which is exactly Aμ dx^μ. Gauge invariance A → A + dα is exactly the freedom to change the local trivialization of the bundle (choosing a different section). The "gauge potential" is not a physical object — only the curvature Fμν is.

---

*Next: `mathematics/09-MANIFOLDS.md` — smooth manifolds, differential forms, and Stokes' theorem that unifies all the integral theorems.*
