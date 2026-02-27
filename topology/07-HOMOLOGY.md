# Homology

## The Big Picture

```
+====================================================================+
|              HOMOLOGY — COUNTING HOLES ALGEBRAICALLY              |
+====================================================================+
|                                                                    |
|  CORE IDEA: Assign abelian groups Hₙ(X) to a space X.            |
|  These groups count "n-dimensional holes":                        |
|  H₀(X) = free abelian on connected components (count components) |
|  H₁(X) = 1-dimensional loops not bounding a disk                 |
|  H₂(X) = 2-dimensional voids not bounding a solid               |
|  Hₙ(X) = n-dimensional holes not bounding (n+1)-chains           |
|                                                                    |
|  KEY PRINCIPLE: Hₙ = (n-cycles) / (n-boundaries)                 |
|                     = ker(∂ₙ) / im(∂ₙ₊₁)                        |
|  Boundary of boundary = 0: ∂ₙ ∘ ∂ₙ₊₁ = 0  (the central identity)|
|                                                                    |
|  EXAMPLES:                                                         |
|  H₀(S¹) = Z, H₁(S¹) = Z, Hₙ(S¹) = 0 for n ≥ 2.                 |
|  H₀(S²) = Z, H₁(S²) = 0, H₂(S²) = Z, Hₙ = 0 for n ≥ 3.        |
|  H₀(T²) = Z, H₁(T²) = Z², H₂(T²) = Z, Hₙ = 0 for n ≥ 3.       |
|  Hₙ(Sⁿ) = Z, Hₖ(Sⁿ) = 0 for k ≠ 0,n.                           |
+====================================================================+
```

---

## Simplicial Homology

### Simplicial Complexes

BRIDGE TO GRAPH THEORY (the data structures you know):
  A graph G = (V, E) IS a 1-dimensional simplicial complex:
    vertices = 0-simplices, edges = 1-simplices.
  Homology of a graph:
    H₀(G) = Z^(# connected components) — same as BFS/DFS components.
    H₁(G) = Z^(cycle rank) where cycle rank = |E| − |V| + components.
    This is the first Betti number b₁ = dim(cycle space).
  A simplicial complex generalizes: add 2-simplices (filled triangles),
    3-simplices (filled tetrahedra), etc. Each dimension adds new
    "holes" that Hₙ detects.
  The Vietoris-Rips complex (used in TDA, see 10-APPLICATIONS.md) is
    built exactly like a clique complex of a graph: connect vertices
    within distance r, then fill in all cliques as higher simplices.
    Computing persistent H₀ on a Rips filtration = tracking connected
    components as the distance threshold r increases — a graph algorithm.
    H₁ persistence = tracking cycle births/deaths = higher-dimensional
    generalization of cycle rank.
```
SIMPLEX: The n-simplex Δⁿ is the convex hull of (n+1) affinely
  independent points v₀,...,vₙ ∈ Rᴺ.
  Δ⁰ = point (vertex)
  Δ¹ = line segment (edge)
  Δ² = filled triangle (face)
  Δ³ = filled tetrahedron (tet)

FACE: A (k)-face of Δⁿ = convex hull of a (k+1)-element subset of vertices.
  Δ² has 3 vertices (0-faces), 3 edges (1-faces), 1 triangle (2-face).

SIMPLICIAL COMPLEX K:
  A finite collection of simplices such that:
  1. Any face of a simplex in K is in K.
  2. Intersection of two simplices is a face of each (or empty).

  Think: a "combinatorial shape" built by gluing simplices.

EXAMPLES:
  K₁ = {v₀, v₁, [v₀v₁]} = an edge (1-complex = graph edge)
  K₂ = boundary of triangle = {v₀,v₁,v₂, [v₀v₁],[v₁v₂],[v₀v₂]}
       (NOT the filled triangle — just the boundary loop)
  K₃ = boundary of tetrahedron = S² triangulated

TRIANGULATION of a topological space X:
  A homeomorphism from |K| (geometric realization of K) to X.
  S¹ can be triangulated by a triangle boundary.
  T² can be triangulated (needs ≥ 7 vertices — no fewer suffice).
```

### Oriented Simplices and Chain Groups

```
ORIENTED SIMPLEX: Choose an ordering of the vertices.
  [v₀v₁] = edge from v₀ to v₁.
  [v₁v₀] = -[v₀v₁]  (reversal = negation).

  For higher simplices: [v₀v₁v₂] = [v₁v₂v₀] = [v₂v₀v₁]  (even permutation = same)
                         [v₁v₀v₂] = -[v₀v₁v₂]              (odd permutation = negation)

n-CHAIN: A formal integer linear combination of oriented n-simplices.
  Example: 2[v₀v₁] - [v₁v₂] + 3[v₀v₂] is a 1-chain.

CHAIN GROUP Cₙ(K; Z):
  The free abelian group on the set of oriented n-simplices.
  If K has kₙ n-simplices, Cₙ(K;Z) = Zᵏⁿ.

BOUNDARY OPERATOR ∂ₙ: Cₙ(K) → Cₙ₋₁(K):
  ∂ₙ[v₀,...,vₙ] = Σᵢ₌₀ⁿ (-1)ⁱ [v₀,...,v̂ᵢ,...,vₙ]
  where v̂ᵢ means "omit vᵢ".

EXPLICIT EXAMPLES:
  ∂₁[v₀v₁] = [v₁] - [v₀]   (boundary of edge = endpoint - startpoint)

  ∂₂[v₀v₁v₂] = [v₁v₂] - [v₀v₂] + [v₀v₁]
              = [v₁v₂] + [v₂v₀] + [v₀v₁]   (the boundary loop, going around)

  ∂₃[v₀v₁v₂v₃] = [v₁v₂v₃] - [v₀v₂v₃] + [v₀v₁v₃] - [v₀v₁v₂]
                   (boundary of tetrahedron = four oriented faces)
```

### The Chain Complex and ∂∂ = 0

```
CHAIN COMPLEX:
  ... → C₃ --∂₃--> C₂ --∂₂--> C₁ --∂₁--> C₀ → 0

KEY IDENTITY: ∂ₙ ∘ ∂ₙ₊₁ = 0  for all n.

PROOF (for n=2): Compute ∂₁(∂₂[v₀v₁v₂]):
  ∂₂[v₀v₁v₂] = [v₁v₂] - [v₀v₂] + [v₀v₁]
  ∂₁([v₁v₂] - [v₀v₂] + [v₀v₁])
    = ([v₂]-[v₁]) - ([v₂]-[v₀]) + ([v₁]-[v₀])
    = [v₂]-[v₁]-[v₂]+[v₀]+[v₁]-[v₀] = 0 ✓

WHY THIS WORKS: Each (n-2)-face appears with coefficient
  (-1)ⁱ(-1)ʲ + (-1)ʲ⁻¹(-1)ⁱ = 0  (two terms cancel).
  The general proof is the same algebraic cancellation.

INTUITION: The boundary of a boundary is empty.
  The boundary of a filled disk = the circle.
  The boundary of the circle = (nothing) = 0.
  "Chains with no boundary" (cycles) include all boundaries,
  and the homology measures the difference.
```

---

## Homology Groups

### Cycles, Boundaries, Homology

```
n-CYCLES: Zₙ(K) = ker(∂ₙ) = {chains whose boundary is 0}
  A cycle is a chain with no boundary.

n-BOUNDARIES: Bₙ(K) = im(∂ₙ₊₁) = {chains that are boundaries of (n+1)-chains}
  A boundary is a cycle (since ∂∂=0): Bₙ ⊆ Zₙ.

HOMOLOGY GROUP: Hₙ(K) = Zₙ(K) / Bₙ(K)
  Two cycles are HOMOLOGOUS if their difference is a boundary.
  Hₙ measures cycles that are NOT boundaries — "genuine n-holes."

INTUITION:
  H₀: path components. Two 0-cycles (vertices) are homologous iff
    they're connected by an edge-path (a 1-chain whose boundary is their difference).
    So H₀ = Z^(# connected components).

  H₁: 1-dimensional loops. A 1-cycle = closed loop.
    It's a boundary iff it bounds a 2-chain (a surface patch).
    H₁ measures loops that don't bound — "independent handles."

  H₂: 2-dimensional voids. A 2-cycle = closed surface.
    It's a boundary iff it bounds a 3-chain (a solid).
    H₂ measures enclosed voids — "independent cavities."
```

### Worked Examples

```
EXAMPLE 1: S¹ (triangulated as triangle boundary)
  K = {v₀, v₁, v₂, [v₀v₁], [v₁v₂], [v₀v₂]}

  C₀ = Z³ (generated by v₀, v₁, v₂)
  C₁ = Z³ (generated by [v₀v₁], [v₁v₂], [v₀v₂])
  C₂ = 0 (no 2-simplices)

  ∂₁: C₁ → C₀:
    ∂₁[v₀v₁] = v₁ - v₀
    ∂₁[v₁v₂] = v₂ - v₁
    ∂₁[v₀v₂] = v₂ - v₀

  Z₁ = ker(∂₁): solving av₁-av₀ + bv₂-bv₁ + cv₂-cv₀ = 0
    → (-a-c)v₀ + (a-b)v₁ + (b+c)v₂ = 0
    → a = -c, b = a. So cycles are multiples of [v₀v₁]+[v₁v₂]-[v₀v₂].
    Z₁ ≅ Z (generated by the loop "going around" the triangle).

  B₁ = im(∂₂) = 0 (no 2-simplices).

  H₁(S¹) = Z₁/B₁ = Z / 0 = Z ✓

  Z₀ = C₀ = Z³ (all 0-chains are 0-cycles).
  B₀ = im(∂₁) = {av₁-av₀ + bv₂-bv₁ + cv₂-cv₀} = span{v₁-v₀, v₂-v₁}.
  H₀ = Z³ / span{v₁-v₀,v₂-v₁} ≅ Z.
  (All vertices are homologous since the triangle is connected.) ✓

EXAMPLE 2: S² (boundary of tetrahedron)
  K = {v₀,v₁,v₂,v₃ (vertices), 6 edges, 4 triangles: [v₁v₂v₃],[v₀v₂v₃],[v₀v₁v₃],[v₀v₁v₂]}
  C₃ = 0 (no 3-simplex — NOT the filled tetrahedron, just the boundary).
  C₂ = Z⁴, C₁ = Z⁶, C₀ = Z⁴.

  H₀ = Z (connected).
  H₁ = 0 (every loop bounds a triangle — no independent loops).
  H₂ = Z (the entire surface is a 2-cycle; it can't bound a 3-chain since there is none).
  ✓ matches H₀(S²)=Z, H₁(S²)=0, H₂(S²)=Z.

EXAMPLE 3: T² (torus)
  Best computed via the cellular chain complex (see below).
  H₀(T²) = Z, H₁(T²) = Z², H₂(T²) = Z.
  The two Z generators of H₁: the a-loop and b-loop around the two handles.
```

---

## Euler Characteristic

```
EULER CHARACTERISTIC:
  χ(X) = Σₙ (-1)ⁿ rank Hₙ(X)
       = Σₙ (-1)ⁿ bₙ

where bₙ = rank(Hₙ) = n-th BETTI NUMBER.

EQUIVALENT FORMULA (for simplicial complexes):
  χ(K) = Σₙ (-1)ⁿ (number of n-simplices)
        = |vertices| - |edges| + |faces| - |tetrahedra| + ...

EXAMPLES:
  Point: χ = 1.
  S¹:  b₀=1, b₁=1.  χ = 1-1 = 0.
  S²:  b₀=1, b₁=0, b₂=1.  χ = 1-0+1 = 2.
  T²:  b₀=1, b₁=2, b₂=1.  χ = 1-2+1 = 0.
  RP²: b₀=1, b₁=0 (Z/2 is torsion, rank 0), b₂=0.  χ = 1.
  Genus-g surface Σ_g: b₀=1, b₁=2g, b₂=1.  χ = 2-2g.

EULER'S FORMULA (for polyhedra homeomorphic to S²):
  V - E + F = 2.
  (Vertices - Edges + Faces = χ(S²) = 2.)
  Platonic solids all satisfy this: tetrahedron 4-6+4=2, cube 8-12+6=2.

TOPOLOGICAL INVARIANCE:
  χ(X) depends only on the homeomorphism type, not the triangulation.
  Invariance proved by: χ(X) = Σ(-1)ⁿ bₙ, and bₙ are topological invariants.
```

---

## Cellular Homology

```
CW COMPLEX: More flexible than simplicial. Spaces built by attaching cells eⁿ
  (open n-disks) via attaching maps.

EXAMPLE: S¹ as a CW complex with 1 vertex (e⁰) and 1 edge (e¹).
  (Much simpler than the 3-vertex simplicial model.)

  T² = S¹ × S¹ as CW complex:
    One 0-cell (the basepoint)
    Two 1-cells a and b (the two loops)
    One 2-cell D (the square, attached by the word aba⁻¹b⁻¹)

CELLULAR CHAIN COMPLEX:
  Cₙ^{CW}(X) = Z^(number of n-cells).
  Cellular boundary map ∂ₙ: defined by degree of attaching maps.

  T² cellular chain complex:
    C₂ = Z (one 2-cell D)
    C₁ = Z² (two 1-cells a, b)
    C₀ = Z (one 0-cell pt)

  ∂₂(D) = a + b - a - b = 0
  (The attaching map goes a, then b, then a⁻¹, then b⁻¹ — a+b+(-a)+(-b) = 0.)
  ∂₁(a) = pt - pt = 0, ∂₁(b) = pt - pt = 0.

  H₀ = Z/0 = Z ✓
  H₁ = Z²/0 = Z² ✓  (both a and b are cycles, ∂₂(D)=0 means nothing kills them)
  H₂ = Z/0 = Z ✓  (D is a cycle since ∂₂D=0, nothing in C₃ to bound it)

  Klein bottle cellular chain complex:
    C₂ = Z (one 2-cell), C₁ = Z² (a,b), C₀ = Z.
    Attaching word: aba⁻¹b  (unlike torus: aba⁻¹b⁻¹)
    ∂₂(D) = a + b - a + b = 2b.  (the a's cancel, b appears twice)
    H₁ = Z²/⟨2b⟩ = Z ⊕ Z/2.
    H₂ = ker(∂₂) = 0  (∂₂(D)=2b ≠ 0).
    So H₁(Klein bottle) = Z ⊕ Z/2 — torsion indicates non-orientability.
```

---

## Singular Homology

```
SINGULAR SIMPLEX: A continuous map σ: Δⁿ → X (not required to be an embedding).

SINGULAR CHAIN GROUP Cₙ(X):
  Free abelian group on singular n-simplices.
  HUGE group — uncountable generators for most spaces.

SINGULAR BOUNDARY: Same formula as simplicial, using face maps.

SINGULAR HOMOLOGY Hₙ(X) = ker(∂ₙ)/im(∂ₙ₊₁).

WHY SINGULAR?
  1. Defined for ANY topological space (no triangulation required).
  2. Functorial: f: X → Y continuous induces f*: Hₙ(X) → Hₙ(Y).
  3. Agrees with simplicial homology for triangulable spaces.

FUNCTORIALITY:
  f: X → Y continuous → f*: Hₙ(X) → Hₙ(Y) is a group homomorphism.
  If f ≃ g (homotopic) then f* = g*.
  If f: X → Y is a homeomorphism, then f*: Hₙ(X) ≅ Hₙ(Y).

HOMOTOPY INVARIANCE:
  If X ≃ Y (homotopy equivalent), then Hₙ(X) ≅ Hₙ(Y) for all n.
  Implication: Rⁿ is contractible → Hₙ(Rⁿ) = 0 for n ≥ 1, H₀(Rⁿ) = Z.
```

---

## Long Exact Sequences

### The Mayer-Vietoris Sequence

```
MAYER-VIETORIS:
  Let X = A ∪ B (open cover, A∩B nonempty).
  ... → Hₙ(A∩B) --(i*,j*)--> Hₙ(A) ⊕ Hₙ(B) --k*--> Hₙ(X) --∂--> Hₙ₋₁(A∩B) → ...

  where:
    (i*,j*)(x) = (iₐ*(x), -iᵦ*(x))  with iₐ: A∩B → A, iᵦ: A∩B → B.
    k*(a,b) = jₐ*(a) + jᵦ*(b)        with jₐ: A → X, jᵦ: B → X.
    ∂: connecting homomorphism (a "long sequence" zig-zag).

ANALOGY WITH VAN KAMPEN:
  Mayer-Vietoris is the homological analog of van Kampen's theorem.
  van Kampen computes π₁ (pushout of groups).
  Mayer-Vietoris computes homology (long exact sequence for abelian groups).

EXAMPLE: Compute H*(S²) using Mayer-Vietoris.
  A = S² \ {south pole} ≅ R² ≃ pt.  Hₙ(A) = 0 for n > 0, H₀ = Z.
  B = S² \ {north pole} ≅ R² ≃ pt.  Same.
  A ∩ B ≅ S¹ × (−1,1) ≃ S¹.  Hₙ(A∩B): H₀=Z, H₁=Z, rest 0.

  Plug into Mayer-Vietoris:
  n=2: ... → H₂(A)⊕H₂(B) → H₂(S²) → H₁(A∩B) → H₁(A)⊕H₁(B) → ...
              0                            Z                0
  So H₂(S²) → Z is an isomorphism: H₂(S²) = Z ✓.

  n=1: ... → H₁(A∩B) → H₁(A)⊕H₁(B) → H₁(S²) → H₀(A∩B) → H₀(A)⊕H₀(B) → ...
                Z               0                      Z            Z⊕Z
  H₁(A)⊕H₁(B)=0, so H₁(S²) → H₀(A∩B) is injective; connecting map H₀(A∩B)→H₀(A)⊕H₀(B)
  sends 1 ↦ (1,1), which is injective. So H₁(S²) = 0 ✓.
```

### Relative Homology and Long Exact Sequence of a Pair

```
PAIR (X, A): topological space X with subspace A ⊆ X.

RELATIVE CHAIN COMPLEX: Cₙ(X,A) = Cₙ(X) / Cₙ(A).
  Relative homology Hₙ(X,A) = Hₙ of this complex.
  Intuition: "homology of X with A collapsed to a point" ≈ Hₙ(X/A) (often, not always).

LONG EXACT SEQUENCE OF A PAIR:
  ... → Hₙ(A) --i*--> Hₙ(X) --j*--> Hₙ(X,A) --∂--> Hₙ₋₁(A) → ...

  This is EXACT: im(each map) = ker(next map).

KEY EXACT SEQUENCE PATTERN: 0 → A → B → C → 0 (short exact).
  If any two of A,B,C are known, the third is determined.
  For abelian groups: B ≅ A ⊕ C if the sequence splits (not always).

EXCISION THEOREM:
  If Z ⊆ A ⊆ X and cl(Z) ⊆ int(A):
  Hₙ(X,A) ≅ Hₙ(X\Z, A\Z).
  (Can "excise" closed interior pieces from both.)
  Key technical lemma for many homology computations.

REDUCED HOMOLOGY:
  H̃ₙ(X): augment C₀ → Z → 0 (add a map sending every vertex to 1).
  H̃₀(X) = Z^{(components-1)}: measures "excess" components beyond one.
  H̃ₙ(X) = Hₙ(X) for n ≥ 1.
  Cleaner for suspension/wedge computations.

SUSPENSION ISOMORPHISM:
  H̃ₙ(ΣX) ≅ H̃ₙ₋₁(X).
  Repeatedly applying: H̃ₙ(Sⁿ) = Z, H̃ₖ(Sⁿ) = 0 for k ≠ n.
```

---

## Homology with Coefficients

```
Hₙ(X; G) for an abelian group G:
  Replace chain groups with Cₙ(X; G) = Cₙ(X) ⊗ G.

UNIVERSAL COEFFICIENT THEOREM:
  There is a split (non-natural) short exact sequence:
  0 → Hₙ(X;Z) ⊗ G → Hₙ(X;G) → Tor(Hₙ₋₁(X;Z), G) → 0

  Tor(A, G): the "torsion" functor. Key cases:
  Tor(Z, G) = 0, Tor(Z/n, G) = {g ∈ G : ng = 0} = G[n].
  Tor(Z/m, Z/n) = Z/gcd(m,n).

KEY EXAMPLES:
  RP²: H₁(RP²;Z) = Z/2, H₂(RP²;Z) = 0.
  H₁(RP²; Z/2) = Z/2 ⊗ Z/2 = Z/2 (tensor part).
  H₂(RP²; Z/2) = Tor(Z/2, Z/2) = Z/2.
  So RP² "looks" different over Z/2 than over Z.

WHY COEFFICIENTS MATTER:
  Z coefficients: most information (includes torsion).
  Z/2 coefficients: simpler, works for non-orientable spaces.
  Q coefficients: kills torsion, gives Betti numbers.
  R or C coefficients: connects to de Rham theory.
```

---

## Homology of Key Spaces

```
+------------------------------------------------------------------+
| SPACE         | H₀ | H₁    | H₂    | H₃  | H₄  | χ   |
+------------------------------------------------------------------+
| Point         | Z  | 0     | 0     | 0   | 0   |  1  |
| S¹            | Z  | Z     | 0     | 0   | 0   |  0  |
| S²            | Z  | 0     | Z     | 0   | 0   |  2  |
| S³            | Z  | 0     | 0     | Z   | 0   |  2  |
| Sⁿ            | Z  | 0     | ...   | Z   | 0   | 1+(-1)ⁿ|
| T² = S¹×S¹   | Z  | Z²    | Z     | 0   | 0   |  0  |
| T³            | Z  | Z³    | Z³    | Z   | 0   |  0  |
| RP²           | Z  | Z/2   | 0     | 0   | 0   |  1  |
| RP³           | Z  | Z/2   | 0     | Z   | 0   |  2  |
| Klein bottle  | Z  | Z⊕Z/2 | 0     | 0   | 0   |  0  |
| Genus-g Σ_g  | Z  | Z^{2g}| Z     | 0   | 0   | 2-2g|
+------------------------------------------------------------------+

PATTERN: Hₙ(Sᵐ) = Z if n=0 or n=m, else 0.
PATTERN: Torsion in homology signals non-orientability or cyclic structure.
PATTERN: Hₙ(X×Y) ≠ Hₙ(X)⊗Hₙ(Y) in general — use Künneth formula.
```

### Künneth Formula

```
KÜNNETH FORMULA:
  For "nice" spaces X, Y with free homology (no torsion):
  Hₙ(X×Y) = ⊕_{i+j=n} Hᵢ(X) ⊗ Hⱼ(Y).

EXAMPLE: T² = S¹ × S¹.
  H₀(T²) = H₀(S¹)⊗H₀(S¹) = Z⊗Z = Z ✓
  H₁(T²) = H₀(S¹)⊗H₁(S¹) ⊕ H₁(S¹)⊗H₀(S¹) = Z⊗Z ⊕ Z⊗Z = Z² ✓
  H₂(T²) = H₁(S¹)⊗H₁(S¹) = Z⊗Z = Z ✓

EXAMPLE: Hₙ(Sᵐ × Sᵏ):
  = ⊕_{i+j=n} Hᵢ(Sᵐ) ⊗ Hⱼ(Sᵏ).
  Non-zero terms: n=0 (Z), n=m (Z), n=k (Z), n=m+k (Z).
  (Assuming m,k ≥ 1 and m ≠ k.)
```

---

## Morse Theory — Homology from Critical Points

For a smooth function f: M → R on a compact manifold with isolated non-degenerate critical points (a Morse function), the homology H*(M) can be computed entirely from the critical points.

```
MORSE THEORY — THE BRIDGE FROM ANALYSIS TO HOMOLOGY:

  Critical point of f: point p where ∇f(p) = 0.
  Morse index k: number of negative eigenvalues of Hess(f) at p.
    index 0 = local minimum
    index 1 = saddle (one down-direction)
    index k = k independent down-directions

  As c increases past a critical value f(p) with index k:
  The sublevel set M_c = {x : f(x) ≤ c} changes by attaching a k-cell.
    index 0: new connected component born (H₀ generator born)
    index 1: handle attached — either two components merge (H₀ death)
             or a 1-cycle created (H₁ generator born)
    index 2: 2-cell caps off a 1-cycle (H₁ death) or creates a void (H₂ born)

  MORSE INEQUALITIES:
    bₖ ≤ Cₖ   (Betti number bₖ ≤ count of index-k critical points)
    Σ(-1)ᵏ Cₖ = Σ(-1)ᵏ bₖ = χ(M)   (alternating sum = Euler char.)

  MORSE COMPLEX: Chain complex with one generator per critical point,
    boundary maps counting gradient flow lines between critical points.
    H*(Morse complex) ≅ H*(M) — an efficient chain complex.

  BRIDGE TO TDA:
    Sublevel-set persistence of f = tracking births/deaths of Hₖ generators
    as c increases. Each birth/death pair corresponds to a critical point.
    The persistence diagram IS the Morse-theoretic decomposition of f.
```

Morse theory is the bridge from differential topology (09-MANIFOLDS.md) to homology computation and to TDA (10-APPLICATIONS.md). It was the key tool in Smale's proof of the h-cobordism theorem and the precursor to Floer homology (infinite-dimensional Morse theory on loop spaces).

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Compute H₀(X) | Count connected components: H₀ = Z^(# components) |
| Build chain complex | Orient simplices, compute ∂ₙ by the alternating face formula |
| Compute Hₙ from CW complex | Use cellular chain complex (far fewer generators) |
| Compute Hₙ of a union | Mayer-Vietoris long exact sequence |
| Compute Hₙ(X,A) | Long exact sequence of the pair (X,A) |
| Compute Hₙ(X×Y) | Künneth formula ⊕_{i+j=n} Hᵢ(X) ⊗ Hⱼ(Y) |
| Find Euler characteristic | χ = Σ(-1)ⁿ bₙ = Σ(-1)ⁿ(# n-cells) |
| Detect orientability | Hₙ(M;Z) = Z if orientable n-manifold; 0 if not |
| Change coefficients | Universal Coefficient Theorem |
| Relate to topology | Hₙ is homotopy invariant; homeomorphic → isomorphic homology |

---

## Common Confusion Points

**"Homology and homotopy groups are the same thing."**
Homology groups Hₙ are abelian (by construction). Homotopy groups πₙ are abelian only for n ≥ 2.
The Hurewicz theorem gives the connection: if πᵢ(X) = 0 for i < n (space is (n-1)-connected),
then Hₙ(X) ≅ πₙ(X). For simply-connected spaces, H₁ = 0 and H₂ = π₂ (Hurewicz in dimension 2).
But for S¹: π₁(S¹) = Z = H₁(S¹) — the Hurewicz map in degree 1.

**"H₁ = π₁."**
H₁(X) is the abelianization of π₁(X) (Hurewicz theorem for n=1).
For abelian π₁: H₁ = π₁. For non-abelian π₁: H₁ = π₁^{ab} = π₁/[π₁,π₁].
Example: figure-8 has π₁ = F₂ (free group on 2 generators), H₁ = Z² (abelianization of F₂).

**"Hₙ(Sⁿ) = Z is obvious."**
The calculation requires genuine work. The simplicial/cellular calculation
works (once you set up the complex). But the claim that Sⁿ is non-contractible —
i.e., that Hₙ(Sⁿ) ≠ 0 — requires proving that the top cycle cannot be a boundary.
This is what Hₙ ≅ Z rather than 0 encodes.

**"χ is a topological invariant but Euler's V-E+F formula is not."**
Euler's formula applies to CW structures. But χ(X) = Σ(-1)ⁿbₙ is topological
(same for any triangulation). The V-E+F formula gives the same answer for any
triangulation of S² because χ(S²) = 2 regardless of how you triangulate it.

**"Long exact sequences are complicated."**
They encode a simple idea: if 0 → A → B → C → 0 is exact, then B "is" A plus C
(up to extension). The connecting homomorphism ∂: Hₙ(C) → Hₙ₋₁(A) captures the
"interaction" between the pieces. Master the short exact sequence first, then the
long version is just a concatenated chain of them.
