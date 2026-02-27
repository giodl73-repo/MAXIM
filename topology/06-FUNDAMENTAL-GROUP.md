# Fundamental Group

## The Big Picture

```
+====================================================================+
|         THE FUNDAMENTAL GROUP — π₁(X, x₀)                        |
+====================================================================+
|                                                                    |
|  LOOPS at x₀: continuous γ: [0,1] → X with γ(0) = γ(1) = x₀.   |
|  HOMOTOPY: a deformation of one loop to another (fixing endpoints).|
|  π₁(X,x₀) = {homotopy classes of loops based at x₀}.             |
|                                                                    |
|  GROUP OPERATION: [γ][δ] = [γ * δ]  (concatenation of loops).    |
|                                                                    |
|  EXAMPLES:                                                         |
|  π₁(Rⁿ) = 0          (contractible — all loops shrink to point)  |
|  π₁(S¹) = Z          (winding number counts loops around circle)  |
|  π₁(Sⁿ) = 0 (n≥2)    (spheres are simply connected)              |
|  π₁(T²) = Z × Z      (two independent generators on torus)        |
|  π₁(RP²) = Z/2        (double cover = universal cover)            |
|  π₁(Figure 8) = F₂   (free group on 2 generators)                |
|                                                                    |
|  VAN KAMPEN'S THEOREM:                                            |
|  π₁(A∪B) = π₁(A) *_{π₁(A∩B)} π₁(B)   (pushout of groups)        |
+====================================================================+
```

---

## Loops and Homotopy

```
LOOP at x₀ ∈ X:
  γ: [0,1] → X continuous with γ(0) = γ(1) = x₀.

HOMOTOPY (RELATIVE TO ENDPOINTS):
  Two loops γ, δ at x₀ are homotopic (γ ≃ δ rel x₀) if:
  ∃H: [0,1]×[0,1] → X continuous with:
    H(t,0) = γ(t), H(t,1) = δ(t)  (start and end are γ and δ)
    H(0,s) = H(1,s) = x₀  (basepoint fixed throughout)

  Think: H(t,s) is a continuous family of loops, s ∈ [0,1] is the "time" of deformation.

CONCATENATION:
  (γ * δ)(t) = γ(2t) for t ∈ [0,1/2]
               δ(2t-1) for t ∈ [1/2,1]
  First traverse γ at double speed, then δ at double speed.
  Well-defined up to homotopy.

CONSTANT LOOP: cₓ₀(t) = x₀ for all t. The identity element.
REVERSE LOOP: γ̄(t) = γ(1-t). The inverse element.

π₁(X, x₀) = {[γ] : γ loops at x₀} with operation [γ][δ] = [γ * δ].
This is a group (associativity up to homotopy, identity = [cₓ₀], inverse = [γ̄]).
```

---

## Computing Fundamental Groups

### Simply Connected Spaces

```
π₁(Rⁿ) = 0:
  Straight-line homotopy: H(t,s) = (1-s)γ(t) + s·x₀ contracts any loop to x₀.

π₁(Sⁿ) = 0 for n ≥ 2:
  Any loop misses some point of Sⁿ (by smooth approximation and Sard's theorem).
  Sⁿ minus a point is homeomorphic to Rⁿ — contractible.
  So any loop in Sⁿ is contractible. □

π₁(convex set) = 0:
  Straight-line homotopy works for convex subsets of Rⁿ.
```

### The Circle π₁(S¹) = Z

```
WINDING NUMBER: The integer measuring how many times a loop goes around the circle.

PROOF: The universal cover of S¹ is R (unwrap the circle to the real line).
  Covering map: p: R → S¹ by p(t) = e^{2πit}.
  Any loop γ in S¹ based at 1 lifts uniquely to a path γ̃ in R starting at 0.
  γ̃(1) ∈ Z (since γ̃(0) = 0 and p(γ̃(1)) = p(0) = 1, so γ̃(1) ∈ p^{-1}(1) = Z).
  The winding number: [γ] ↦ γ̃(1) ∈ Z.

  This map Z → π₁(S¹) is an isomorphism.
  Generator: [e^{2πit}] ↦ 1 (one counterclockwise loop).

IMPORTANT IMPLICATION:
  No retraction D² → S¹.  (Proof: if r: D² → S¹ were a retraction with r|_{S¹} = id,
  consider r composed with inclusion S¹ → D²: S¹ → D² → S¹.
  This is id on S¹. But π₁(D²) = 0, π₁(S¹) = Z.
  A map 0 → Z cannot be surjective → contradiction.)

BROUWER'S FIXED POINT THEOREM (from this):
  Every continuous f: D² → D² has a fixed point.
  Proof: If f(x) ≠ x for all x, define r(x) = point on ∂D² by extending x to f(x) to
  the boundary. Then r: D² → S¹ is a retraction with r|_{S¹} = id. Contradiction. □
```

### Torus π₁(T²) = Z × Z

```
Torus T² = S¹ × S¹.
π₁(S¹ × S¹) = π₁(S¹) × π₁(S¹) = Z × Z.
(Product formula: π₁(X×Y) = π₁(X) × π₁(Y) for path-connected spaces.)

Generators:
  a = [loop around one S¹ factor]
  b = [loop around other S¹ factor]
  Relation: ab = ba (commute, since torus is abelian).

CONTRAST WITH Klein BOTTLE:
  Klein bottle K: π₁(K) = ⟨a,b : abab^{-1} = 1⟩ ≠ Z×Z.
  Non-abelian (in fact, has a presentation showing it's not abelian).
  K cannot be embedded in R³; it self-intersects.
```

---

## Van Kampen's Theorem

```
SEIFERT-VAN KAMPEN THEOREM:
  Let X = A ∪ B where A, B, A∩B are path-connected open sets.
  All contain the basepoint x₀.
  Then:
  π₁(X, x₀) = π₁(A) *_{π₁(A∩B)} π₁(B)

  where *_{H} denotes the AMALGAMATED FREE PRODUCT (pushout of groups):
  π₁(A) *_{π₁(A∩B)} π₁(B) = ⟨π₁(A), π₁(B) : iₐ(h) = iᵦ(h) ∀h ∈ π₁(A∩B)⟩

  iₐ: π₁(A∩B) → π₁(A), iᵦ: π₁(A∩B) → π₁(B) are the maps induced by inclusions.

APPLICATIONS:

1. Figure 8 = S¹ ∨ S¹ (wedge of two circles):
   A = first circle + small overlap, B = second circle + small overlap.
   A∩B contractible. π₁(A) = Z, π₁(B) = Z, π₁(A∩B) = 0.
   π₁(S¹∨S¹) = Z * Z = F₂  (free group on 2 generators).

2. Torus via van Kampen:
   T² = square with identified edges.
   A = T²\{interior disk}, B = disk, A∩B = annulus ≃ S¹.
   π₁(A) = ⟨a,b : aba^{-1}b^{-1}=1⟩ = Z×Z, π₁(B) = 0.
   Recover: π₁(T²) = Z×Z ✓.

3. Genus-g surface Σ_g:
   π₁(Σ_g) = ⟨a₁,b₁,...,aₘ,bₘ : ∏[aᵢ,bᵢ] = 1⟩
   where [a,b] = aba^{-1}b^{-1} (commutator), g=genus.

4. RP² (projective plane):
   π₁(RP²) = Z/2.  [a : a² = 1]
   (RP² = disk with antipodal boundary identification; boundary loop is non-trivial but its square is trivial.)
```

---

## Covering Spaces

```
COVERING MAP: p: X̃ → X is a covering map if:
  ∀x ∈ X, ∃ open U∋x such that p^{-1}(U) = ∪_{α} Ũα (disjoint union of open sets)
  with p|_{Ũα}: Ũα → U a homeomorphism.
  X̃ is a "covering space" of X; each Ũα is a "sheet."

EXAMPLES:
  p: R → S¹ by t ↦ e^{2πit}.
    Sheets over small arc: infinitely many, one per integer translate of the arc.
    Each local sheet is a small interval mapping homeomorphically to the arc.

  p: Sⁿ → RPⁿ by x ↦ [x] (antipodal quotient).
    Sheets over each neighborhood: exactly 2 (the point and its antipode).
    A 2-sheeted cover. Sⁿ is the "double cover" of RPⁿ.

  p: C → C* by z ↦ e^z.
    Strips {z : nπ < Im(z) < (n+1)π} are sheets.
    This is how branch cuts for log(z) arise: z↦log(z) is multi-valued because
    the covering is infinite-sheeted.

FUNDAMENTAL THEOREM OF COVERING SPACES:
  For "nice" X (path-connected, locally path-connected, semi-locally simply connected):
  There is a bijection:
    {Isomorphism classes of covering spaces of X} ↔ {Subgroups of π₁(X)}

  Number of sheets of p: X̃ → X = [π₁(X) : p*(π₁(X̃))]  (index of subgroup).

  UNIVERSAL COVER X̃ corresponds to H = {e} (trivial subgroup).
  - X̃ is simply connected.
  - Every covering space is a quotient of X̃.
```

### Deck Transformations

```
DECK TRANSFORMATION (= covering transformation):
  Homeomorphism φ: X̃ → X̃ with p ∘ φ = p.
  (Permutes the sheets over each point of X.)

  Deck(X̃/X) = group of all deck transformations.

GALOIS COVERING (= normal covering):
  If H = p*(π₁(X̃)) ◁ π₁(X), the covering is called "regular" or "Galois."
  In this case: Deck(X̃/X) ≅ π₁(X)/H.

UNIVERSAL COVER:
  H = {e} is always normal → universal cover is always Galois.
  Deck(X̃/X) ≅ π₁(X)/\{e} = π₁(X).
  π₁(X) acts freely and properly discontinuously on X̃, and X = X̃/π₁(X).

EXAMPLES:
  R → S¹: deck transformations = t ↦ t+n for n ∈ Z.  Deck ≅ Z = π₁(S¹). ✓
  Sⁿ → RPⁿ: deck transformations = {id, antipodal map}. Deck ≅ Z/2 = π₁(RPⁿ). ✓

ANALOGY TO GALOIS THEORY:
  Covering spaces of X ↔ Subgroups of π₁(X)
  Normal coverings ↔ Normal subgroups
  Deck transformations ↔ Quotient group
  Universal cover ↔ "Splitting field" (simply connected = fully resolved)

  This is the precise topological analog of Galois correspondence:
  Extension fields of K ↔ Subgroups of Gal(K/F).
  The same categorical structure!

<!-- @editor[content/P2]: The Galois correspondence for covers is stated correctly but the deeper categorical statement is missing: π₁ is a functor Top* → Grp, and the full correspondence is an equivalence of categories between covering spaces of X and π₁(X)-sets. This is the version a learner who needs "∞-categories" will want — it generalizes to the ∞-categorical statement that the ∞-groupoid fundamental groupoid Π₁(X) classifies fibrations with discrete fiber. Add a line on the groupoid version (Π₁(X) not just π₁) since the single-basepoint version breaks for non-connected spaces. -->
```

---

## Higher Homotopy Groups

```
πₙ(X, x₀) = {homotopy classes of maps (Sⁿ, *) → (X, x₀)}.
  [Maps from n-sphere to X, preserving basepoints, up to basepoint-preserving homotopy.]

π₁: fundamental group — loops, non-abelian in general.
πₙ (n ≥ 2): abelian groups always.
  (Proof: two spheres Sⁿ can "pass through each other" — Eckmann-Hilton argument.)

EXAMPLES:
  πₙ(Sⁿ) = Z for all n ≥ 1.
  πₙ(Sᵏ) = 0 for n < k.
  π₂(S²) = Z. π₃(S²) = Z (the Hopf fibration!).
  π₃(S³) = Z. πₙ(S³) for n ≥ 4: complicated.

HOPF FIBRATION:
  p: S³ → S² with fiber S¹.
  η: S³ → S²: p(z₁,z₂) = z₁/z₂ ∈ C∪{∞} = S².
  The Hopf fibration generates π₃(S²) = Z.
  It appears in: classical mechanics (fiber bundle structure), quantum mechanics
  (Berry phase), and string theory.

HOMOTOPY GROUPS OF SPHERES πₙ(Sᵏ):
  Completely understood for n≤k (trivial) and n=k (Z).
  Stable range (n > 2k-1): stable homotopy theory.
  General: extremely difficult. πₙ(S²) is known for small n; no complete pattern.
  This is one of the hardest open problems in topology.

<!-- @editor[content/P2]: Missing knot groups — π₁(S³ \ K) for a knot K is the "knot group," the primary algebraic invariant of a knot. This is the direct bridge to knot theory (flagged as "DOES need" in learner calibration). The meridian and longitude of a knot are generators of π₁; Wirtinger presentation gives an explicit group presentation from a knot diagram. The abelianization of the knot group is always Z — which is why H₁(S³ \ K) = Z and why knots are detected by higher invariants. This bridge from π₁ to knot theory belongs in this file. -->

<!-- @editor[content/P2]: Missing ∞-groupoids and the homotopy hypothesis — a key modern development the learner needs. Grothendieck's homotopy hypothesis: ∞-groupoids (up to equivalence) are the same as topological spaces (up to homotopy equivalence). HoTT formalizes this: types are ∞-groupoids, the identity type is the path space. The higher homotopy groups πₙ(X) are the π₀ of iterated loop spaces Ωⁿ(X). A brief bridge here would anchor the ∞-categories / HoTT content the learner needs. -->
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Compute π₁ of simple space | Use homotopy equivalences + known π₁ |
| Compute π₁ of union | Van Kampen's theorem (amalgamated free product) |
| Classify covering spaces | Subgroups of π₁ (Galois correspondence for covers) |
| Find deck transformations | π₁(X)/H for H-covering; π₁(X) for universal |
| Prove fixed point theorem | No retraction D² → S¹ (from π₁(D²)=0, π₁(S¹)=Z) |
| Prove winding number integers | Lift to universal cover R of S¹ |
| Understand branch cuts | Multi-valued function = section of covering p: C → C* |
| Compute π₁ of genus-g surface | ⟨a₁,b₁,...,aₘ,bₘ : ∏[aᵢ,bᵢ]=1⟩ via van Kampen |

---

## Common Confusion Points

**"The fundamental group doesn't depend on basepoint."**
For a path-connected space, changing the basepoint from x₀ to x₁ gives an isomorphic
group (via the isomorphism induced by any path from x₀ to x₁). But the isomorphism
is NOT canonical (depends on choice of path). For non-path-connected spaces, π₁ at
different components can be completely different groups.

**"Covering spaces and quotient spaces are inverses."**
Quotient: X → X/~ (collapse things). Covering: X̃ → X (unfold things).
They're related via Galois theory: quotient of X̃ by deck transformations = X.
But "unfold then refold" ≠ original space unless done carefully.

**"Van Kampen only applies to two pieces."**
Van Kampen applies to any number of pieces, as long as each pairwise intersection
is path-connected. Multiple pieces give the colimit (amalgamated free product over
all intersections) of the fundamental groups.

**"Higher homotopy groups πₙ(Sᵏ) are trivial for n ≠ k."**
FALSE. π₃(S²) = Z (via Hopf fibration). πₙ(S²) are often nontrivial for n > 2.
The homotopy groups of spheres are notoriously complicated and not fully computed.
The "stable" part (stable homotopy groups of spheres) is partially understood but still
an active research area.
