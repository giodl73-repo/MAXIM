# Applications of Topology

## The Big Picture

```
+====================================================================+
|      TOPOLOGY IN THE WILD — THREE MAJOR APPLICATION DOMAINS        |
+====================================================================+
|                                                                    |
|  1. TOPOLOGICAL DATA ANALYSIS (TDA)                               |
|     Persistent homology: the shape of data.                       |
|     H₀ tracks connected components; H₁ tracks loops.             |
|     Birth-death pairs give "persistence diagrams" — multi-scale   |
|     topological summaries robust to noise.                        |
|                                                                    |
|  2. TOPOLOGICAL PHASES OF MATTER (Condensed Matter Physics)       |
|     TKNN invariant, Chern numbers, Berry phase.                   |
|     Quantum Hall effect: Hall conductance = Chern number = integer.|
|     Topological insulators: bulk-boundary correspondence.         |
|     K-theory classifies topological phases.                       |
|                                                                    |
|  3. CONFIGURATION SPACES IN ROBOTICS                              |
|     Configuration space C = all robot configurations.             |
|     Obstacle avoidance = topology of C \ obstacles.               |
|     Motion planning = path-finding in C.                          |
|     Topological complexity measures motion planning difficulty.   |
+====================================================================+
```

---

## Part 1: Topological Data Analysis (TDA)

### The Core Problem

```
GIVEN: A finite point cloud X = {x₁,...,xₙ} ⊆ Rᵈ.
GOAL: Understand the "shape" of X despite:
  - Finite sampling (not a continuous manifold)
  - Noise (points shifted from "true" positions)
  - High dimensionality (d large, visualization impossible)

TRADITIONAL APPROACH: PCA, clustering (k-means), dimension reduction.
  These capture "linear structure" or "local density" — not topology.

TDA APPROACH: Compute topological invariants of X.
  H₀: How many connected components? (= number of clusters, at each scale)
  H₁: How many independent loops? (= circular or ring-shaped data structures)
  H₂: How many voids? (= hollow structures)
  These are robust to perturbations and noise.
```

### Simplicial Complexes from Data

```
VIETORIS-RIPS COMPLEX Rips(X, ε):
  Vertices: points in X.
  Add a k-simplex {x_{i₀},...,x_{iₖ}} iff all pairwise distances d(xᵢ,xⱼ) ≤ ε.

  At small ε: each point isolated (trivial homology, just n points).
  At large ε: everything connected (one component, possibly complex topology).

ČECH COMPLEX Čech(X, ε):
  Vertices: points in X.
  Add a k-simplex {x_{i₀},...,x_{iₖ}} iff the balls B(xᵢ, ε) have a common intersection.
  Nerve theorem: Čech(X,ε) has the same homotopy type as ∪B(xᵢ,ε).
  More expensive to compute than Rips; more theoretically clean.

ALPHA COMPLEX:
  Subcomplex of Rips, using Voronoi cells to restrict which simplices to include.
  More efficient in low dimensions; same homotopy type as ∪B(xᵢ,ε) (from Nerve theorem).
```

### Persistent Homology

```
KEY IDEA: Vary ε from 0 to ∞ and track how homology changes.

FILTRATION: A nested sequence of complexes:
  ∅ = K₀ ⊆ K₁ ⊆ K₂ ⊆ ... ⊆ Kₙ = K
  obtained by increasing ε through thresholds ε₁ < ε₂ < ... < εₙ.

BIRTH AND DEATH:
  A homology class α ∈ Hₖ(Kᵢ) is "born" at Kᵢ if α ∉ im(Hₖ(Kᵢ₋₁) → Hₖ(Kᵢ)).
  It "dies" at Kⱼ if it maps to 0 in Hₖ(Kⱼ) but not in Hₖ(Kⱼ₋₁).

  Persistence = death_time - birth_time.
  LONG-lived features: likely true topological features of the underlying space.
  SHORT-lived features: likely noise.

PERSISTENCE DIAGRAM:
  A multiset of points {(birth, death)} in R².
  Each point = a homological feature with its lifespan.
  Points far from the diagonal (birth ≠ death) = significant features.
  Points near diagonal = noise.

EXAMPLE:
  Data sampled from a circle S¹ with noise:
  H₀ persistence: many points born early, all die quickly as ε grows (clusters merge).
    One H₀ class survives to death=∞ (the single connected component).
  H₁ persistence: one point (b,d) with large persistence (the loop of S¹).
    Many short-lived H₁ features (noise artifacts).
  The long-lived H₁ class tells you: the data has circular structure.

STABILITY THEOREM (fundamental result of TDA):
  The bottleneck distance between persistence diagrams satisfies:
  d_B(Dgm(f), Dgm(g)) ≤ ‖f - g‖_∞.
  Persistence diagrams are Lipschitz-stable: small perturbation of data →
  small change in persistence diagram. This makes TDA robust to noise.
```

### Persistent Homology Algorithms

```
MATRIX REDUCTION:
  The filtration gives a boundary matrix D (columns = simplices, rows = simplices).
  Reduce D using left-to-right column operations (over Z/2 for simplicity).
  Reduced matrix R = D ∘ V (V = change of basis).
  Birth-death pairs read off from pivot positions.

  Complexity: O(n³) for n simplices (naively); practical algorithms much faster.
  Standard: Ripser (C++ implementation), Gudhi (Python).

PERSISTENT HOMOLOGY OVER DIFFERENT FIELDS:
  Over Z/2: simplest, handles non-orientable spaces.
  Over Z: more information but harder (persistence theory still works via Smith normal form).
  Over Q: intermediate.
  Most practical TDA uses Z/2 or Z/p for small primes.

PERSISTENT COHOMOLOGY:
  Dual theory; sometimes more efficient to compute.
  Persistent cup products can detect "higher-order" topological features.
```

### Applications of TDA

```
COMPUTATIONAL BIOLOGY:
  - Point clouds from cryo-EM data: shape of protein structures.
  - Topology of gene expression data: loops in cell differentiation cycles.
  - Neuroscience: topology of neural firing patterns (Curto-Itskov).
    Hippocampal place cells form simplicial complexes encoding spatial topology.

MATERIAL SCIENCE:
  - Topology of amorphous materials (glasses, foams): persistent H₁ counts loops.
  - Phase transitions detectable as topology changes in atomic configurations.

MACHINE LEARNING:
  - Topology of loss landscape: saddle points, local minima counted by H₀/H₁.
  - Topological regularization: penalize topological complexity of learned representations.
  - Mapper algorithm (Carlsson): compressed representation of high-dimensional data.

SIGNAL PROCESSING:
  - Natural images lie near low-dimensional manifolds;
    topology of image patches (3×3 pixel patches) ≈ S¹ (Klein bottle for a subset).
  - Time series analysis: sublevel set persistence of a signal f: R → R.
    H₀ persistence = merge tree of level sets (related to Morse theory).

MAPPER ALGORITHM:
  1. Choose filter function f: X → R (e.g., first PCA component, density).
  2. Cover f(X) with overlapping intervals.
  3. Cluster each preimage f⁻¹(interval).
  4. Connect clusters with shared points.
  Result: a graph (or simplicial complex) summarizing the shape of data.
  Used in breast cancer survival analysis (Carlsson group) — identified a subtype.

WHY MAPPER WORKS — THE THEORETICAL BASIS:
  Mapper is a discrete approximation to the REEB GRAPH of f.
  Reeb graph: quotient space X/~ where x ~ y iff x,y are in the same
    connected component of f⁻¹(f(x)). Continuous version of Mapper.

  NERVE THEOREM (justification):
    If U = {U₁,...,Uₖ} is a "good cover" of X (all intersections contractible),
    then the nerve N(U) has the same homotopy type as X.
    Mapper builds a nerve of the pullback cover — under good-cover conditions,
    it captures the topology of X faithfully.

  FILTER FUNCTION CHOICE matters:
    f = first PCA component → captures dominant linear variation.
    f = eccentricity (max distance to other points) → reveals outliers.
    f = density → captures cluster structure.
    Different filters give complementary topological summaries.

  MULTISCALE MAPPER: vary the cover resolution (interval width, overlap).
    Coarse cover → global structure. Fine cover → local structure.
    The persistence of features across resolutions is the signal.
```

---

## Part 2: Topological Phases of Matter

### Berry Phase

```
QUANTUM ADIABATIC EVOLUTION:
  System with Hamiltonian H(λ), λ = parameter (e.g., magnetic field direction).
  State evolves slowly (adiabatically) along a path γ: [0,1] → parameter space Λ.
  If λ returns to start (γ is a loop), the state picks up a phase:
  |ψ(T)⟩ = e^{iγ_Berry} · e^{iγ_dynamic} |ψ(0)⟩.

BERRY PHASE (geometric phase):
  γ_Berry = i ∮_γ ⟨n(λ)| ∇_λ |n(λ)⟩ · dλ
  where |n(λ)⟩ is the instantaneous eigenstate.

BERRY CONNECTION (gauge field):
  𝒜_μ(λ) = i ⟨n|∂/∂λ_μ|n⟩  (a 1-form on parameter space).

BERRY CURVATURE (field strength):
  𝛀_μν = ∂_μ 𝒜_ν - ∂_ν 𝒜_μ  (a 2-form on parameter space).
  γ_Berry = ∮_γ 𝒜 · dλ = ∬_Σ 𝛀  (Stokes' theorem — Berry phase = flux).

TOPOLOGICAL NATURE:
  For a closed loop γ bounding a 2D surface Σ in parameter space:
  γ_Berry = ∬_Σ 𝛀 dλ.
  If Σ is a sphere S² (e.g., spin-1/2 in all directions of magnetic field):
  γ_Berry = Ω/2 = (solid angle subtended by γ)/2.
  This is a topological invariant of the loop.

CONNECTION TO CHERN NUMBERS:
  The Berry curvature 𝛀 is a 2-form on parameter space.
  If parameter space is a 2-torus T² (Brillouin zone in k-space):
  Chern number C = (1/2π) ∬_{T²} 𝛀 dk ∈ Z.
  This is an integer by topology (Chern class of the U(1) bundle over T²).
```

### Quantum Hall Effect (TKNN Invariant)

```
SETTING: 2D electron gas in a strong magnetic field at low temperature.
  Landau levels: energy quantized into flat bands.
  Filling factor ν = n/n_Φ (electrons per magnetic flux quantum).

HALL CONDUCTANCE:
  σ_xy = ν · e²/h (measured in units of e²/h ≈ 3.874 × 10⁻⁵ Ω⁻¹).
  ν must be an INTEGER (quantum Hall effect, 1980, von Klitzing — Nobel 1985).
  Remarkably precise: σ_xy = ν e²/h to 1 part in 10⁹.

THOULESS-KOHMOTO-NIGHTINGALE-DEN NIJS (TKNN) THEORY (1982):
  For a Bloch Hamiltonian H(k) in 2D (k = crystal momentum ∈ T²):
  The occupied bands form a vector bundle over T² (the Brillouin zone torus).

  Hall conductance = e²/h × C₁,  where C₁ is the FIRST CHERN NUMBER:
  C₁ = (1/2π) Σ_{occupied bands n} ∬_{T²} 𝛀ₙ(k) d²k.

  𝛀ₙ(k) = Im⟨∂k_x uₙ | ∂k_y uₙ⟩ - Im⟨∂k_y uₙ | ∂k_x uₙ⟩  (Berry curvature).

  The Hall conductance is quantized because C₁ ∈ Z (Chern numbers are integers).
  The integer is a topological invariant — robust to perturbations.

WHY TOPOLOGY?
  The occupied-bands bundle over T² is a topological object.
  Smooth deformations of H(k) that don't close the gap don't change C₁.
  The integer can only change at a quantum phase transition (gap closing).
  → Plateau structure of Hall conductance is topologically protected.
```

### Topological Insulators

```
TOPOLOGICAL INSULATOR: A material that is:
  - Insulating in the bulk (gap at Fermi energy).
  - Conducting on the surface/edge (gapless surface states).
  - Topologically non-trivial (surface states protected by topology).

BULK-BOUNDARY CORRESPONDENCE:
  Topological invariant of the bulk ↔ number of protected boundary modes.
  If bulk has Chern number C: C chiral edge modes on the boundary.
  Edge modes are "topologically protected" — cannot be removed by
  non-magnetic disorder (as long as symmetries are preserved).

QUANTUM SPIN HALL INSULATOR (2D TI, Z/2 classification):
  Protected by time-reversal symmetry T (T² = -1 for electrons = spin-1/2).
  Z/2 topological invariant ν: 0 (trivial) or 1 (topological).
  ν = 1: one pair of helical edge states (spin-up going right, spin-down going left).
  Kane-Mele (2005): predicted in graphene; Bernevig-Hughes-Zhang (2006): HgTe — confirmed.

3D TOPOLOGICAL INSULATOR:
  Surface states: a single Dirac cone (linear crossing at time-reversal invariant k).
  Realized in Bi₂Se₃, Bi₂Te₃. The surface is a "topological metal" protected by T.
  The Z/2 invariant (in 3D): four indices (ν₀; ν₁ν₂ν₃).
  Strong TI: ν₀ = 1.

CLASSIFICATION OF TOPOLOGICAL PHASES (periodic table):
  Kitaev (2009): classification by symmetry class (10 Altland-Zirnbauer classes)
  and dimension gives the "periodic table of topological insulators":

  Symmetry \  Dim   1     2     3
  Class A:         0     Z     0
  Class AIII:      Z     0     Z
  Class AI:        0     0     0
  Class AII:       0    Z/2   Z/2  ← quantum spin Hall, 3D TI

  (Entries: 0=trivial, Z=integer invariant, Z/2=binary invariant)

K-THEORY:
  The full classification uses K-theory of the Brillouin zone with symmetry:
  KR-theory (real K-theory) for time-reversal invariant systems.
  K-groups K^n(X) = appropriate homotopy classes of maps from BZ to classifying spaces.
```

### Other Topological Phenomena

```
WEYL SEMIMETALS:
  Bulk has Weyl points (band-crossing points) with topological charge (chirality ±1).
  Total chirality = 0 (Nielsen-Ninomiya theorem).
  Surface states: Fermi arc (an open curve connecting two Weyl points on surface BZ).
  Classified by Chern number of a sphere surrounding each Weyl point.

TOPOLOGICAL SUPERCONDUCTORS:
  Analogous to topological insulators; pairing gap replaces band gap.
  Edge modes: Majorana fermions (their own antiparticle).
  Kitaev chain (1D): Z/2 invariant; zero modes = Majorana bound states at ends.
  Non-Abelian braiding statistics → potential fault-tolerant quantum computing.

ANYONS AND TOPOLOGICAL QUANTUM COMPUTING:
  2D topological phases support anyons (particles with fractional statistics).
  Braiding anyons = performing quantum gates.
  Topologically protected: result of braiding depends only on topology of worldlines.
  Fibonacci anyons: universal quantum computing by braiding alone.
  Physical realization: fractional quantum Hall effect, topological superconductors.

MONOPOLES AND FIELD THEORY:
  Dirac monopole: magnetic field of a monopole = curvature of a U(1) bundle over S².
  Chern number = monopole charge. Dirac quantization: charge quantized (integer).
  't Hooft-Polyakov monopole: non-abelian gauge theory with topological soliton.
  Instanton: topology in 4D Euclidean gauge theory (π₃(SU(2)) = Z).
```

---

## Part 3: Configuration Spaces in Robotics

### Configuration Spaces

```
CONFIGURATION of a robot: The minimal set of parameters that uniquely
  specify the position of every part of the robot.

CONFIGURATION SPACE (C-space): The set of all possible configurations.
  For n-joint robotic arm: C = T^n = (S¹)^n (n-torus, one angle per joint).
  For a rigid body in R²: C = R² × S¹ (position + orientation).
  For a rigid body in R³: C = R³ × SO(3) (position + rotation group).
  For two rigid bodies: C₁ × C₂.

OBSTACLES in C-space:
  Physical obstacles in workspace → forbidden regions in C-space.
  C_free = C \ C_obstacles (the "free" configuration space).
  MOTION PLANNING = find a path in C_free from start to goal.

TOPOLOGY OF C_free DETERMINES FEASIBILITY:
  π₀(C_free): are start and goal in same connected component? (Reachability.)
  π₁(C_free): are there independent "ways around"? (Path planning complexity.)
  Contractible C_free: planning reduces to simple homotopy.
  Highly connected C_free: many independent paths exist.

EXAMPLES:
  Two-joint arm on a table with an obstacle:
  C = T² (2-torus), C_obstacle = some region in T².
  C_free = T² minus a region — typically has nontrivial π₁.
  Planning = finding a path in this punctured torus.

  Parallel manipulator (multiple arms sharing an end effector):
  C-space can be an algebraic variety — more complex topology.
```

### Topological Complexity

```
TOPOLOGICAL COMPLEXITY TC(X) (Farber, 2003):
  The minimum number of "continuous motion rules" needed to plan
  motion between any pair of configurations.

FORMAL DEFINITION:
  TC(X) = secat(π₁₂: PX → X×X) - 1
  where PX = space of all paths in X, and π₁₂(γ) = (γ(0), γ(1)).
  TC(X) = minimum k such that X×X can be covered by k open sets,
    each admitting a continuous section s: U → PX.

EXAMPLES:
  TC(Rⁿ) = 0: one motion rule suffices (straight-line motion).
  TC(S¹) = 1: two rules (one can't plan without a decision point).
  TC(T²) = 2: three rules.
  TC(Sⁿ) = 1 for n odd; TC(Sⁿ) ≤ 2 for n even; TC(S²) = 2.
  TC(RP^n) = n (proven using cohomology of RP^n).

BOUNDS ON TC:
  cat(X) - 1 ≤ TC(X) ≤ 2 cat(X) - 1
  where cat(X) = Lusternik-Schnirelmann category = minimum cover by contractible sets.

  Cohomological lower bound:
  TC(X) ≥ max{k : ∃ u₁,...,uₖ ∈ H*(X;F) with zero-divisors: ∏(1⊗uᵢ - uᵢ⊗1) ≠ 0 in H*(X×X)}.

HIGHER TC:
  TCₙ(X): complexity for simultaneous planning of n robots.
  TC₂ = TC. TCₙ(X) related to Hⁿ*(Xⁿ).
  Practical significance: multi-robot path planning.
```

### Motion Planning Algorithms (Topological Perspective)

```
ROADMAP METHODS:
  Build a graph Γ ⊆ C_free.
  Γ captures the homotopy type of C_free.
  Plan = find path in Γ.
  Visibility graph: vertices at obstacle corners, edges with line-of-sight.

PROBABILISTIC ROADMAP (PRM):
  Sample C_free randomly, connect nearby samples.
  Converges to capturing the topology of C_free as samples → ∞.
  Practically: captures connected components quickly.
  Limitation: thin passages (narrow corridors in C_free) require many samples.

RRT (RAPIDLY-EXPLORING RANDOM TREES):
  Build a tree rooted at start, expand toward random samples.
  Complete: finds path if one exists (asymptotically).
  Topology oblivious: just looks for any path, doesn't map C_free.

CELL DECOMPOSITION:
  Decompose C_free into simple cells (contractible pieces).
  Cell decomposition induces a graph (adjacency of cells).
  Planning reduces to graph search.

TOPOLOGICAL OBSTRUCTION TO PLANNING:
  If C_free is not simply connected: no planner can give a continuous
  motion rule (single algorithm covering all pairs).
  TC(C_free) > 0 iff C_free is not contractible.
  This gives a lower bound on the number of "rule switches" any planner needs.
```

### Further Examples: Topology in Robotics

```
SNAKE ROBOT:
  n links, each with angle in S¹ → C = Tⁿ.
  Self-intersection constraints: some regions of Tⁿ forbidden.
  C_free = Tⁿ minus self-intersection set (complex topology for large n).

MULTI-ROBOT PLANNING (n robots in workspace W):
  C = Wⁿ = W × ... × W.
  Collision-free = C_free = {(q₁,...,qₙ) ∈ Wⁿ : qᵢ ≠ qⱼ for i≠j}.
  For point robots in R²: C_free = (R²)^n \ {qᵢ=qⱼ}.
  π₁(C_free for n robots in R²) = pure braid group PBₙ (subgroup of braid group Bₙ).
  Braid groups capture the topology of multi-robot path planning.

BRAID GROUP Bₙ:
  Group of homotopy classes of paths in (R²)^n \ {collision set}.
  Generators σᵢ = "strand i crosses over strand i+1."
  Relations: σᵢσᵢ₊₁σᵢ = σᵢ₊₁σᵢσᵢ₊₁ (braid relation), σᵢσⱼ = σⱼσᵢ for |i-j|≥2.
  B₂ = Z (one generator, one "crossing" = winding number).
  Bₙ for n ≥ 3: non-abelian, infinite group.
  Connection: closure of braids → knots/links (Alexander's theorem).

GRASP PLANNING:
  Finger positions on an object → grasp space.
  Topology of grasp space: determines stability, grasp diversity.
  Contact configuration spaces have non-trivial topology (fingers constrained to object surface).
```

---

## Topological Methods in Other Fields

```
KNOT THEORY — BIOLOGY, PHYSICS, AND COMPUTATION:

  A knot K = embedding of S¹ in S³ (up to ambient isotopy).
  Knot group: π₁(S³ \ K) — see 06-FUNDAMENTAL-GROUP.md for Wirtinger presentation.

  INVARIANTS (hierarchy of power):
    Knot group π₁(S³\K)         strongest algebraic invariant (hard to compare)
    Alexander polynomial Δ_K(t)  computable: det(tV − Vᵀ), V = Seifert matrix
    Jones polynomial V_K(t)      discovered 1984, quantum groups connection
    HOMFLY-PT P_K(a,z)           generalizes both Alexander and Jones
    Knot Floer homology HFK      categorified invariant (Ozsváth-Szabó)
                                 detects genus, fiberedness

  DNA TOPOLOGY:
    Double-stranded DNA is a ribbon (two curves with linking).
    LINKING NUMBER Lk = algebraic crossing count of two DNA strands.
    Călugăreanu-White-Fuller theorem: Lk = Tw + Wr
      Tw = twist (local helical winding of strands around each other)
      Wr = writhe (global coiling of the DNA axis in 3D)
    Lk is a topological invariant (unchanged by deformation).
    Tw and Wr are geometric — they trade off while Lk stays fixed.

    TOPOISOMERASES: enzymes that change DNA topology.
      Type I: cuts one strand → changes Lk by ±1 → relaxes supercoiling.
      Type II: passes one strand through another → changes Lk by ±2
               → decatenates linked DNA circles, unknots knotted DNA.
    DNA replication creates catenanes (linked rings);
      Type II topoisomerase is essential to separate them.

    Gel electrophoresis separates knotted DNA by crossing number —
      literally a physical knot invariant measurement.

  PROTEIN KNOTTING:
    ~1% of protein structures contain topological knots (trefoil, figure-8).
    Classified by the same knot invariants used in mathematics.
    Knotted proteins: slower folding, increased stability.
    How they fold into knots is an open question (threading vs. slipknot).

  KNOTS AND QUANTUM COMPUTING (Jones → Chern-Simons → anyons):
    Witten (1989): the Jones polynomial V_K(t) is the expectation value
      of a Wilson loop observable in Chern-Simons gauge theory at level k:
      V_K(e^{2πi/(k+2)}) = ⟨W_K⟩_{CS}
    The path integral of Chern-Simons theory on S³ computes V_K(t).
    This connects: knot invariants ↔ 3D TQFT ↔ quantum computation.
    ANYONIC BRAIDING: in 2+1D topological phases, particle worldlines
      form braids; the resulting amplitudes are knot/link invariants.
      Fibonacci anyons: braiding alone gives universal quantum computation.
      Evaluating the Jones polynomial is #P-hard in general — but
      quantum computers can approximate it efficiently (BQP-complete).
    The Freedman-Kitaev-Wang theorem: topological quantum computation
      is equivalent to standard quantum computation.

NETWORK TOPOLOGY:
  Social networks, internet topology, protein interaction networks.
  Persistent homology of networks: H₀ = components, H₁ = cycles/redundant paths.
  Degree distribution vs topological holes: complementary information.

TOPOLOGICAL FLUID DYNAMICS:
  Helicity H = ∫ v · (∇×v) dV: a topological invariant of the vorticity field.
  H = 0 for unlinked vortex lines; H ≠ 0 measures linking number of vortex tubes.
  Conserved under ideal (Euler) flow → topological constraint on turbulence.
  Related to Hopf invariant of maps S³ → S².

TOPOLOGICAL QUANTUM FIELD THEORY (TQFT):
  Assigns vector spaces to manifolds, linear maps to cobordisms.
  Atiyah's axioms for TQFT.
  Chern-Simons theory: 3D TQFT with Jones polynomial as partition function.
  BF theory: topological field theory in any dimension.
  Witten-Donaldson: 4D TQFT counting instantons = Donaldson invariants.

```

---

## Part 4: Modern Foundations — HoTT and ∞-Categories

### Homotopy Type Theory (HoTT)

```
HOMOTOPY TYPE THEORY — TOPOLOGY AS A FOUNDATION FOR MATHEMATICS:

  Core idea: reinterpret Martin-Löf type theory so that types ARE spaces.

  TYPE ↔ SPACE DICTIONARY:
    Type A              ↔  Space A
    Term a : A          ↔  Point a ∈ A
    Id_A(a,b)           ↔  Path space (paths from a to b)
    Proof of a = b      ↔  A path from a to b
    Id_{Id_A}(p,q)      ↔  Homotopy between paths p and q
    Function A → B      ↔  Continuous map A → B
    Π(x:A).B(x)         ↔  Section of fibration B → A
    Σ(x:A).B(x)         ↔  Total space of fibration B → A

  UNIVALENCE AXIOM (Voevodsky):
    (A ≃ B) ≃ Id_U(A,B)
    "Equivalent types are equal in the universe U."
    This means: any property that respects equivalence (= homotopy
    equivalence) can be transported along an equivalence.
    This is EXACTLY what mathematicians do informally ("Q and R are
    isomorphic, so anything true of Q is true of R").

  WHY IT MATTERS FOR TCS:
    1. Proof assistants (Coq, Agda, Lean) can formalize homotopy theory.
       The HoTT library formalizes: π₁(S¹) = Z, Freudenthal suspension,
       Blakers-Massey, Seifert-van Kampen — all constructively.
    2. Higher inductive types: define S¹ as a type with one point and one
       loop (no embedding in R² needed). Fully synthetic homotopy theory.
    3. Cubical type theory (Cohen-Coquand-Huber-Mörtberg): computational
       interpretation of univalence — the axiom is no longer an axiom but
       a theorem of the type theory.
```

### ∞-Categories

```
(∞,1)-CATEGORIES — THE MODERN FRAMEWORK FOR HOMOTOPY THEORY:

  An (∞,1)-category has:
    Objects, morphisms, 2-morphisms (homotopies), 3-morphisms, ...
    All k-morphisms for k ≥ 2 are invertible (up to higher morphisms).

  THE (∞,1)-CATEGORY OF SPACES:
    Objects = topological spaces (or ∞-groupoids).
    Morphisms = continuous maps.
    2-morphisms = homotopies.
    3-morphisms = homotopies of homotopies.
    This is the fundamental object of homotopy theory.

  ∞-TOPOI (Lurie, "Higher Topos Theory" 2009):
    An ∞-topos is an (∞,1)-category satisfying the ∞-categorical
    version of Giraud's axioms (descent, colimits, generators).
    Classical sheaf theory ⊂ ∞-topos theory:
      Sheaves of sets → sheaves of spaces (∞-groupoids).
      Cohomology = mapping spaces in the ∞-topos of sheaves.

  COBORDISM HYPOTHESIS (Lurie 2009):
    Fully extended n-dimensional TQFTs (functors from Cob(n) to a
    symmetric monoidal (∞,n)-category C) are classified by
    fully dualizable objects of C.
    This is the most powerful classification result in modern TQFT,
    and its statement and proof require the full ∞-categorical framework.

  DERIVED ALGEBRAIC GEOMETRY:
    Replace commutative rings with E∞-ring spectra.
    "Spaces" are derived stacks — functors from E∞-rings to ∞-groupoids.
    Classical algebraic geometry ⊂ derived algebraic geometry.
    Moduli problems that are "wrong" classically (non-smooth, obstructed)
    become well-behaved in the derived setting.

  WHY ∞-CATEGORIES FOR THIS GUIDE:
    The classical tools (π₁, homology, cohomology) are shadows of
    ∞-categorical data. The fundamental groupoid Π_∞(X) carries strictly
    more information than all πₙ(X) combined (they lose the interaction
    between different levels). Modern topology works in ∞-categories
    because that is where the full structure lives.
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Analyze "shape" of data cloud | Persistent homology (Vietoris-Rips filtration, Ripser) |
| Find clusters in data | H₀ persistence = connected components at each scale |
| Find loops in data | H₁ persistence = long-lived 1-cycles |
| Summarize multi-scale topology | Persistence diagram or barcode (birth-death pairs) |
| Compute Hall conductance | Chern number = (1/2π)∬ Berry curvature over Brillouin zone |
| Check if topological insulator | Z/2 invariant via parity of occupied states at TRIM points |
| Count edge modes | Bulk-boundary correspondence: Chern number = # edge modes |
| Plan robot motion | Build roadmap in C_free; complexity bounded by TC(C_free) |
| Count independent paths | π₁(C_free) = fundamental group of free configuration space |
| Analyze multi-robot planning | Braid groups Bₙ (n robots in plane) |
| Lower bound on motion planners | Topological complexity TC(C_free) |

---

## Common Confusion Points

**"TDA is just clustering."**
TDA computes multi-scale topological features — not just connected components (which
is what clustering does). H₁ persistent homology captures circular structure that
no clustering algorithm detects. The persistence diagram gives a coordinate-free,
multi-scale summary. Clustering can be seen as H₀ persistence, but TDA is richer.

**"Topological invariants are fragile — topology changes under perturbation."**
The stability theorem for persistence diagrams says the opposite: small perturbations
of data (bounded by ε in Hausdorff distance) change the persistence diagram by at most ε
in bottleneck distance. This is the key robustness result that makes TDA practical.
Similarly, topological phases are robust: the Chern number can only change at a phase
transition (gap closing), so small perturbations don't change it.

**"Berry phase is just a dynamical phase."**
The Berry phase is a geometric phase that depends on the path in parameter space,
not on the rate of traversal. It's path-dependent but not rate-dependent (unlike
the dynamical phase ∫E dt). The Berry phase is the holonomy of the Berry connection
on the eigenstate bundle — a genuinely geometric/topological quantity.

**"Configuration space is just the workspace."**
The workspace is physical space (where the robot moves). The configuration space is
the space of all robot configurations — potentially much higher dimensional. A 6-DOF
robot arm has C = T⁶ (6-torus), even though the workspace is R³. The topology of
C-space determines feasibility and complexity of motion planning — it's the right
space for planning, not the workspace.

**"Topological quantum computing is just quantum computing."**
Standard quantum computing uses local operations on qubits — errors (local
perturbations) destroy the state. Topological QC uses anyonic braiding: the
computation is encoded in the topology of worldlines, which is immune to
local perturbations (you'd have to reroute the entire worldline to make an error).
The Hilbert space is not a product of local factors — it's a global topological space.
