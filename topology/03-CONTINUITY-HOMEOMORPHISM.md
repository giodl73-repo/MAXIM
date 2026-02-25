# Continuity and Homeomorphisms

## The Big Picture

```
+====================================================================+
|         TOPOLOGICAL MAPS — A HIERARCHY                            |
+====================================================================+
|                                                                    |
|  ALL MAPS                                                         |
|      ↓ preimage of open = open                                    |
|  CONTINUOUS MAPS   (preserve topology)                            |
|      ↓ also injective, preimage of open = open                    |
|  TOPOLOGICAL EMBEDDINGS                                           |
|      ↓ also surjective                                            |
|  QUOTIENT MAPS  (sometimes called "identification maps")          |
|      ↓ bijective + continuous + open  (or: bijective + cts + closed)|
|  HOMEOMORPHISMS  (topological isomorphisms)                       |
|                                                                    |
|  TOPOLOGICAL INVARIANTS: properties preserved by homeomorphisms.  |
|  If X ≇ Y: at least one invariant differs.                        |
|  If X ≅ Y: all invariants agree (but equal invariants ≠ homeo.)   |
+====================================================================+
```

---

## Continuous Maps

```
DEFINITION: f: X → Y is continuous if f^{-1}(U) is open in X for every open U in Y.

EQUIVALENT FORMULATIONS:
  1. f^{-1}(V) is closed in X for every closed V in Y.
  2. f(cl(A)) ⊆ cl(f(A)) for every A ⊆ X.
  3. For every x and neighborhood N of f(x), f^{-1}(N) is a neighborhood of x.
  4. In metric spaces: ε-δ definition.
  5. In sequential spaces: xₙ → x implies f(xₙ) → f(x).

COMPOSITION: f: X→Y, g: Y→Z continuous → g∘f: X→Z continuous.
  (This is why continuous maps form the morphisms of the category Top.)

RESTRICTION: If f: X→Y is continuous and A ⊆ X, then f|_A: A→Y is continuous.

PASTING LEMMA: If X = A∪B with A,B closed, and f: A→Y, g: B→Y continuous with
  f|_{A∩B} = g|_{A∩B}, then h: X→Y defined by h|_A = f, h|_B = g is continuous.
  (Not true for open sets without the gluing condition.)
  Version for open sets: if A,B open and f,g agree on A∩B, then h continuous.
```

---

## Homeomorphisms

```
DEFINITION: f: X → Y is a homeomorphism if:
  1. f is bijective.
  2. f is continuous.
  3. f^{-1} is continuous.

X ≅ Y (homeomorphic): there exists a homeomorphism between them.
Homeomorphism = isomorphism in the category Top.

NOTE: Bijective + continuous ≠ homeomorphism!
  Counterexample: f: [0,1) → S¹ by f(t) = e^{2πit}.
  Bijective, continuous, but f^{-1} is not continuous (S¹ is compact, [0,1) is not).
  [S¹ is the circle; if [0,1) were homeomorphic to S¹, removing one point would
   give two connected components in [0,1) — impossible, only one.]

COMPACT + HAUSDORFF THEOREM: If X is compact, Y is Hausdorff, and f: X→Y is
  a continuous bijection, then f IS a homeomorphism.
  (Because f maps closed sets to closed sets — compact subsets of Hausdorff are closed.)
```

### Famous Homeomorphisms

```
R ≅ (0,1) ≅ (-∞,∞): via f(x) = x/(1+|x|) or f(x) = arctan(x).
Rⁿ ≅ open ball: via x ↦ x/√(1+‖x‖²).
Disk minus boundary ≅ Rⁿ: stereographic projection.
[0,1]² ≅ [0,1] (space-filling curve gives surjection, not homeomorphism).

NOT homeomorphic:
  R ≇ R² (removing one point from R disconnects; removing one point from R² does not).
  S¹ ≇ S² (S¹ is not simply connected... wait, S¹ has fundamental group Z; S² has trivial π₁).
  T² ≇ S²: different fundamental groups (Z² vs trivial), different homology.
  Closed disk D² ≇ S¹: D² is contractible; S¹ has nonzero π₁.
```

---

## Topological Invariants

```
INVARIANT: A property P such that X ≅ Y → (P(X) ↔ P(Y)).
Two spaces with different invariants are NOT homeomorphic.
Two spaces with the same invariants MIGHT be homeomorphic (depends on the invariant).

BASIC INVARIANTS:
  Cardinality |X| — preserved (obvious since homeomorphism is a bijection).
  Connectedness — f^{-1} of disconnected open cover would disconnect X.
  Path-connectedness — f∘(path in X) is a path in Y.
  Compactness — f^{-1} of open cover in Y gives open cover in X; finite subcover exists.
  Hausdorff property — f^{-1} gives disjoint neighborhoods.
  Dimension — dimₜ(X) (topological dimension, defined via coverings).

ALGEBRAIC INVARIANTS (stronger, harder to compute):
  π₁(X) — fundamental group.
  πₙ(X) — higher homotopy groups.
  H_n(X; Z) — singular homology groups.
  H^n(X; Z) — singular cohomology groups (ring structure via cup product).
  Euler characteristic χ(X) = Σ(-1)ⁿ rank(Hₙ(X)).

EXAMPLES:
  S¹: π₁ = Z. S² has π₁ = 0 → S¹ ≇ S².
  Torus T²: π₁ = Z×Z. Sphere S²: π₁ = 0 → T² ≇ S².
  Klein bottle K: H₁(K;Z) = Z ⊕ Z/2. T²: H₁ = Z² → K ≇ T².
  RP²: H₁ = Z/2 → RP² ≇ S², T², Klein bottle.
```

---

## Invariants From Removing a Point

```
A CLASSICAL TECHNIQUE: X ≅ Y implies X\{p} ≅ Y\{q} for corresponding points.
  If X\{p} and Y\{q} are not homeomorphic: X ≇ Y.

R vs R²:
  R\{0} has 2 connected components.
  R²\{0} has 1 connected component.
  → R ≇ R².

R vs Rⁿ (n ≥ 2):
  R\{0} = 2 components.
  Rⁿ\{0} = 1 component (for n≥2).
  → R ≇ Rⁿ for n≥2.

Rⁿ vs Rᵐ (n ≠ m):
  Rⁿ\{0} ≅ Sⁿ⁻¹ × R (homotopy equivalent to Sⁿ⁻¹).
  Hₙ₋₁(Rⁿ\{0}) = Hₙ₋₁(Sⁿ⁻¹) = Z if n-1 ≥ 1.
  For n≠m: Sⁿ⁻¹ ≇ Sᵐ⁻¹ (different homology) → Rⁿ ≇ Rᵐ.
  This is the INVARIANCE OF DOMAIN theorem (Brouwer, 1912).

Invariance of domain: if f: U ⊆ Rⁿ → Rⁿ is continuous and injective, f is open.
  Corollary: Rⁿ ≇ Rᵐ for n≠m.
```

---

## Homotopy

```
HOMOTOPY between maps f, g: X → Y:
  A continuous map H: X × [0,1] → Y with H(x,0) = f(x), H(x,1) = g(x).
  "f can be continuously deformed into g."

HOMOTOPY EQUIVALENCE: X and Y are homotopy equivalent (X ≃ Y) if
  ∃f: X→Y, g: Y→X with g∘f ≃ id_X and f∘g ≃ id_Y.

CONTRAST:
  Homeomorphism: bijective, inverse is continuous. (X ≅ Y)
  Homotopy equivalence: not necessarily bijective.  (X ≃ Y)
  Homeomorphism → homotopy equivalence, but not conversely.

EXAMPLES:
  R ≃ {pt} (R is contractible).
  Rⁿ ≃ {pt}.
  S¹ ≁ {pt} (not contractible; π₁(S¹)=Z ≠ 0).
  Möbius band ≃ S¹ (deformation retract to core circle).
  Solid torus D²×S¹ ≃ S¹.
  Annulus = S¹×(0,1) ≃ S¹.

CONTRACTIBLE: X ≃ {pt}. Every loop is contractible to a point.
  Rⁿ, disks, trees — all contractible.
  Spheres, tori — not contractible.

DEFORMATION RETRACT: r: X → A ⊆ X with r|_A = id_A and r ≃ id_X.
  r is a continuous "collapse" of X onto A within X.
  A is a deformation retract of X → X ≃ A.
```

---

## The Invariants Table

```
+--------------------------------------------------------------------+
| SPACE        | π₁      | H₀ | H₁      | H₂  | χ  | Compact? Ori? |
+--------------------------------------------------------------------+
| Point {pt}   | 0       | Z  | 0       | 0   | 1  | Yes       Yes  |
| Interval I   | 0       | Z  | 0       | 0   | 1  | Yes       Yes  |
| Circle S¹    | Z       | Z  | Z       | 0   | 0  | Yes       Yes  |
| Sphere S²    | 0       | Z  | 0       | Z   | 2  | Yes       Yes  |
| Sphere S³    | 0       | Z  | 0       | 0   | 2  | Yes       Yes  |
| Disk D²      | 0       | Z  | 0       | 0   | 1  | Yes       Yes  |
| Torus T²     | Z×Z     | Z  | Z²      | Z   | 0  | Yes       Yes  |
| Klein Bottle | <...>   | Z  | Z⊕Z/2   | 0   | 0  | Yes       No   |
| RP²          | Z/2     | Z  | Z/2     | 0   | 1  | Yes       No   |
| Rⁿ           | 0       | Z  | 0       | 0   | 1  | No        Yes  |
| R\{0}        | Z       | Z  | Z       | 0   | 0  | No        Yes  |
| R²\{0}       | Z       | Z  | Z       | 0   | 0  | No        Yes  |
| Figure 8     | F₂(free)| Z  | Z²      | 0   |−1  | No        N/A  |
+--------------------------------------------------------------------+
```

---

## Decision Cheat Sheet

| Task | Approach |
|------|---------|
| Prove f continuous | Show f^{-1}(U) open for every open U |
| Prove f is a homeomorphism | Show bijective + continuous + f^{-1} continuous |
| Shortcut: f homeomorphism | Compact domain + Hausdorff codomain + bijective + continuous |
| Prove X ≇ Y | Find invariant that differs (π₁, homology, compactness, etc.) |
| Show X ≃ Y (homotopy equiv.) | Construct f: X→Y, g: Y→X, homotopies g∘f≃id, f∘g≃id |
| Prove spaces have same dim | Invariance of domain |
| Distinguish Rⁿ and Rᵐ | Homology of sphere Sⁿ⁻¹ vs Sᵐ⁻¹ |

---

## Common Confusion Points

**"Bijective + continuous = homeomorphism."**
False. f: [0,1) → S¹ is a bijection and continuous. But f^{-1} is not continuous
(S¹ is compact, [0,1) is not, and removing one endpoint disconnects one but not the other).
You need BOTH continuous + continuous inverse.

**"Homotopy equivalent = homeomorphic."**
Not at all. A disk D² is homotopy equivalent to a point but not homeomorphic to a point
(different cardinality, different topology). Homotopy equivalence is much weaker than
homeomorphism. Any contractible space is homotopy equivalent to a point.

**"Two spaces with the same fundamental group are homeomorphic."**
Only if all higher invariants also agree. Lens spaces L(7,1) and L(7,2) have the same
π₁ = Z/7 but are not homeomorphic (different Reidemeister torsion). Computing enough
invariants to definitively classify spaces is one of the central problems of topology.

**"Invariance of domain is obvious."**
It's not. Invariance of domain says: if f: U ⊆ Rⁿ → Rⁿ is continuous and injective,
it's open (and in particular, f(U) is homeomorphic to U). This requires Brouwer's fixed
point theorem or homology for its proof. The analogous statement for f: Rⁿ → Rᵐ with
m < n fails (space-filling curves show n → m is possible for m < n).
