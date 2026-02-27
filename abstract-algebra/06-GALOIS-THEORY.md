# Galois Theory

## The Big Picture

```
+====================================================================+
|           GALOIS THEORY — THE CORRESPONDENCE                       |
+====================================================================+
|                                                                    |
|  QUESTION: Can f(x) ∈ Q[x] be solved by radicals?                |
|  ANSWER: f is solvable by radicals ⟺ Gal(f) is a solvable group. |
|                                                                    |
|  THE GALOIS CORRESPONDENCE (for Galois extension K/F):            |
|                                                                    |
|  Subfields of K        ←→        Subgroups of Gal(K/F)           |
|  containing F                                                     |
|                                                                    |
|  F = K^G (fixed field) ←→       G = Gal(K/F) (full group)        |
|  K                    ←→        {e} (trivial group)              |
|                                                                    |
|  E₁ ⊆ E₂             ←→        H₂ ⊆ H₁  (REVERSAL of order)    |
|  [E₂:E₁]             =         [H₁:H₂]  (index)                 |
|  E/F Galois           ←→        H ◁ G  (H normal subgroup)       |
|  Gal(E/F)             ≅         G/H    (quotient)                |
+====================================================================+
```

Galois theory is the deepest tool connecting field theory to group theory.
The key insight: automorphisms of K that fix F form a group, and the
lattice of intermediate fields is exactly (in reverse) the lattice of subgroups.

---

## Galois Groups

```
DEFINITION: Let K/F be a field extension.
  Aut(K/F) = {σ: K → K : σ is a field automorphism and σ(a) = a for all a ∈ F}.
  = field automorphisms of K fixing F pointwise.

  This is a group under composition.

GALOIS EXTENSION: K/F is Galois if:
  |Aut(K/F)| = [K:F].
  Equivalently: K is the splitting field of a separable polynomial f ∈ F[x].
  (Separable: no repeated roots — always true in char 0 or for irreducible poly in char p.)

GALOIS GROUP: Gal(K/F) = Aut(K/F) when K/F is Galois.

EXAMPLES:
  Q(√2)/Q: Gal = {id, σ} where σ(√2) = -√2. ≅ Z/2Z.
  Q(i)/Q: Gal = {id, σ} where σ(i) = -i (complex conjugation restricted). ≅ Z/2Z.
  Q(ζₙ)/Q (cyclotomic): Gal ≅ (Z/nZ)*, order φ(n).
    σₐ(ζₙ) = ζₙᵃ for each a ∈ (Z/nZ)*.
  F_{p^n}/F_p: Gal = ⟨Frobenius⟩ ≅ Z/nZ.
  Q(∛2, ω)/Q (ω = e^{2πi/3}): Gal = S_3. (Degree 6, symmetric group on roots.)
```

---

## Fixed Fields and the Galois Correspondence

### Fixed Field

```
For H ≤ Gal(K/F):
  K^H = {α ∈ K : σ(α) = α for all σ ∈ H} = "fixed field of H."

  K^H is a subfield of K containing F.
  [K : K^H] = |H|.  (Artin's theorem — key fact)
  K/K^H is a Galois extension with Gal(K/K^H) = H.
```

### The Fundamental Theorem

```
FUNDAMENTAL THEOREM OF GALOIS THEORY:
  Let K/F be a finite Galois extension with G = Gal(K/F).

  There is a bijection:
  {intermediate fields F ⊆ E ⊆ K}  ←→  {subgroups H ≤ G}
  given by:
    E ↦ Gal(K/E)
    H ↦ K^H

  Under this correspondence:
  1. [E:F] = [G:H] = |G|/|H|  (index = degree)
  2. [K:E] = |H|
  3. E₁ ⊆ E₂  ⟺  Gal(K/E₂) ⊆ Gal(K/E₁)  [REVERSED]
  4. E/F is Galois  ⟺  Gal(K/E) ◁ G  [E normal ↔ subgroup normal]
  5. When E/F is Galois: Gal(E/F) ≅ G/Gal(K/E).
```

### Example: Q(√2, √3) / Q

```
G = Gal(Q(√2,√3)/Q) ≅ Z/2 × Z/2.
  Four automorphisms:
  e:   √2↦√2, √3↦√3
  σ:   √2↦-√2, √3↦√3
  τ:   √2↦√2, √3↦-√3
  στ:  √2↦-√2, √3↦-√3

Subgroups of Z/2×Z/2:
  {e}: whole field K = Q(√2,√3)
  ⟨σ⟩: fixed field = Q(√3)  (σ fixes √3)
  ⟨τ⟩: fixed field = Q(√2)
  ⟨στ⟩: fixed field = Q(√6)  (στ fixes √2·√3 = √6? check: (στ)(√6) = (-√2)(-√3) = √6 ✓)
  G = Z/2×Z/2: fixed field = Q

Lattice (REVERSED):
  Subgroups:  {e} ← ⟨σ⟩,⟨τ⟩,⟨στ⟩ ← G
  Fields:     K   →  Q(√3),Q(√2),Q(√6) → Q
```

---

## Cyclotomic Extensions

```
K = Q(ζₙ) where ζₙ = e^{2πi/n}, a primitive n-th root of unity.

GALOIS GROUP:
  Gal(Q(ζₙ)/Q) ≅ (Z/nZ)* via σₐ(ζₙ) = ζₙᵃ, gcd(a,n)=1.
  [Q(ζₙ):Q] = φ(n).

KRONECKER-WEBER THEOREM:
  Every abelian extension of Q (Galois with abelian group) is
  contained in some Q(ζₙ).
  Equivalently: Q^{ab} = Q(all roots of unity).

CYCLOTOMIC POLYNOMIAL:
  Φₙ(x) = ∏_{gcd(k,n)=1, 1≤k≤n} (x - ζₙᵏ) = minimal polynomial of ζₙ over Q.
  deg(Φₙ) = φ(n).
  xⁿ-1 = ∏_{d|n} Φd(x).

RAMIFICATION:
  p ramifies in Q(ζₙ) iff p | n.
  If p ∤ n: p is unramified; the Frobenius at p is σ_p ∈ Gal.
    The order of Frobenius = order of p in (Z/nZ)* = ord(p mod n).
    p is split completely iff Frobenius = e iff p ≡ 1 (mod n).

PRIMES THAT SPLIT COMPLETELY IN Q(ζₙ):
  p splits completely in Q(ζₙ) iff p ≡ 1 (mod n).
  Example: p splits in Q(ζ_5) = Q(e^{2πi/5}) iff p ≡ 1 (mod 5): {11, 31, 41, 61,...}.
```

---

## Solvability by Radicals

### Radical Extensions

```
A RADICAL EXTENSION of F is obtained by successively adjoining n-th roots:
  F = F₀ ⊆ F₁ ⊆ ... ⊆ Fₘ = K
  where Fᵢ = Fᵢ₋₁(αᵢ) and αᵢⁿⁱ ∈ Fᵢ₋₁ for some nᵢ ≥ 1.

SOLVABLE BY RADICALS: f(x) ∈ F[x] is solvable by radicals if its roots
  lie in some radical extension of F.

GALOIS CRITERION:
  f is solvable by radicals ⟺ Gal(splitting field of f / F) is a solvable group.

RECALL: Solvable group = derived series reaches {e}.
  Abelian → solvable (trivially).
  S₃, S₄ → solvable.
  S₅ → NOT solvable (S₅' = A₅, A₅' = A₅, never reaches {e}).
```

### Degrees 2–4: Solvable

```
DEGREE 2: x² + bx + c = 0.
  Galois group ⊆ S₂ ≅ Z/2 (solvable).
  Formula: x = (-b ± √(b²-4c)) / 2.  ← adjoining one square root.

DEGREE 3: x³ + px + q = 0 (depressed cubic via substitution x = t - b/3).
  Galois group ⊆ S₃ (order 6, solvable — derived series: S₃' = A₃ ≅ Z/3, then {e}).
  Cardano's formula (1545):
    Let D = -(4p³+27q²) (discriminant).
    u = ∛(-q/2 + √(D/108)), v = ∛(-q/2 - √(D/108)) with uv = -p/3.
    Three roots: u+v, ωu+ω²v, ω²u+ωv  where ω = e^{2πi/3}.
  Requires: square root + two cube roots.

DEGREE 4: Ferrari's method (1545).
  Reduce to a cubic resolvent (which is solvable by degree 3).
  Galois group ⊆ S₄ (order 24, solvable — S₄' = A₄, A₄' = V₄, V₄' = {e}).

Historical note: Quadratic known ancient times; cubic/quartic discovered 16th century.
  The race to find the cubic formula: Tartaglia→Cardano dispute (1545).
  Ferrari (student of Cardano) solved the quartic.
  Abel (1824) and Galois (1832) then showed degree ≥ 5 is generally impossible.
```

### Degree 5 and Beyond: Unsolvable

```
ABEL-RUFFINI THEOREM (Abel 1824, Galois 1832 — full proof):
  The general degree-5 polynomial is NOT solvable by radicals.
  "General" = with coefficients as independent variables.

WHY:
  The general degree-n polynomial has Galois group = Sₙ (as a permutation group
  on the n roots over the field F(s₁,...,sₙ) of symmetric functions in the roots).
  For n=5: Gal = S₅.
  S₅ is NOT solvable: S₅' = A₅, and A₅ is simple (non-abelian), so A₅' = A₅.
  Derived series: S₅ ▷ A₅ ▷ A₅ ▷ A₅ ▷ ... (never reaches {e}).

SPECIFIC vs GENERAL:
  The GENERAL quintic is not solvable.
  Some SPECIFIC quintics ARE solvable.
  Example: x⁵-5x+12 over Q — check if Gal(f) is solvable.
  x⁵-1 (cyclotomic) — always solvable (Gal ⊆ (Z/5Z)* ≅ Z/4, abelian).
  x⁵-2 — Gal = F₂₀ (Frobenius group of order 20, solvable).

NUMERICAL METHODS:
  Since there's no radical formula, numerical root-finding uses:
  Newton's method (quadratic convergence), Jenkins-Traub (for polynomials).
  Graeffe's method, Weierstrass-Durand-Kerner (finds all roots simultaneously).
  None give exact algebraic expressions — they give approximate values.
```

---

## Insolvability of the Quintic — Proof Sketch

```
THEOREM: There is no formula analogous to the quadratic formula for degree ≥ 5.

Proof sketch:
1. The splitting field K of the general quintic f over F = Q(s₁,...,s₅)
   (sᵢ = i-th elementary symmetric polynomial in roots x₁,...,x₅)
   has Gal(K/F) = S₅.

2. Any radical extension tower F = F₀ ⊂ F₁ ⊂ ... ⊂ Fₘ = K corresponds
   to a tower of groups G = G₀ ▷ G₁ ▷ ... ▷ Gₘ = {e} with Gᵢ/Gᵢ₊₁ cyclic.
   (Adding n-th root → cyclic extension → cyclic quotient group.)

3. This means G = S₅ is solvable — but S₅ is NOT solvable.

4. Contradiction — no radical tower can yield the splitting field of the general quintic.

(The full proof requires also handling the case where F doesn't contain enough
roots of unity, using "Galois closure" techniques.)
```

---

## Inverse Galois Problem

```
QUESTION: For each finite group G, does ∃ Galois extension K/Q with Gal(K/Q) ≅ G?

KNOWN:
  Every abelian group: YES (Kronecker-Weber).
  Every solvable group: YES (Šafarevič, 1954).
  A_n for all n: YES.
  S_n for all n: YES.
  All groups of order ≤ 1000: YES (computed).
  Most sporadic simple groups: YES (various authors).
  The Monster: YES (J. Thompson et al.).

OPEN: The general inverse Galois problem.
  No known group G for which the answer is definitively NO.
  But also no proof that the answer is always YES.

<!-- @editor[content/P2]: Missing absolute Galois group and Langlands program — the absolute Galois group Gal(Q̄/Q) is one of the central objects of modern mathematics, and its representations are the subject of the Langlands program. For a TCS/Math reader at this level, the statement "Gal(Q̄/Q) acts on ℓ-adic cohomology of varieties → Weil conjectures → Deligne's proof" is the natural next step after the inverse Galois problem. At minimum a forward pointer and a 3-line orientation to why Gal(Q̄/Q) is hard and important -->

<!-- @editor[bridge/P2]: No connection between Galois theory and pairing-based cryptography — the learner calibration explicitly flags "Galois theory → algebraic cryptography" as a best bridge. Weil pairings on elliptic curves, the Tate pairing, and bilinear pairing groups (used in BLS signatures, SNARKs, identity-based encryption) all rely on Galois-theoretic structure of the field extensions. The file handles solvability/radicals well but doesn't connect Galois theory to the pairing-based crypto that defines modern post-SNARKs cryptography -->
```

---

## Applications to Ruler-and-Compass Constructions

```
A real number α is CONSTRUCTIBLE iff [Q(α):Q] is a power of 2.
  (Each compass/straightedge step can at most double the degree of the extension.)

CLASSICAL IMPOSSIBILITIES (proved using Galois theory):
  Squaring the circle: π is transcendental (Lindemann 1882) → not constructible.
  Duplicating the cube: need ∛2, [Q(∛2):Q]=3, not a power of 2 → not constructible.
  Trisecting arbitrary angle: 60° angle requires constructing cos(20°).
    Minimal poly of 2cos(20°) = 8x³-6x-1, irreducible of degree 3 over Q. → impossible.

CONSTRUCTIBLE REGULAR POLYGONS (Gauss-Wantzel):
  n-gon is constructible iff φ(n) is a power of 2.
  Equivalently: n = 2^k · p₁ · p₂ · ... · pₘ where pᵢ are distinct Fermat primes.
  Fermat primes: 3, 5, 17, 257, 65537 (only known ones).
  Examples: 3, 4, 5, 6, 8, 10, 12, 15, 17, 20, 24, 30, 51, ...
  Not constructible: 7-gon (φ(7)=6=2·3, not power of 2).
```

---

## Decision Cheat Sheet

| Task | Method |
|------|--------|
| Find Gal(K/F) | Find all F-automorphisms of K |
| Determine if extension is Galois | Check: splitting field of separable polynomial |
| Find fixed field of H | α ∈ K with σ(α)=α for all σ ∈ H |
| Apply Galois correspondence | H ↔ K^H, index ↔ degree |
| Test if f solvable by radicals | Compute Gal(f); check if solvable group |
| Prove quintic not solvable | Gal(general quintic) = S₅; S₅ not solvable |
| Find constructible numbers | [Q(α):Q] must be power of 2 |
| Find cyclotomic Galois group | Gal(Q(ζₙ)/Q) ≅ (Z/nZ)* |

---

## Common Confusion Points

**"Galois group is just the automorphism group of the splitting field."**
Precisely: Gal(K/F) = automorphisms of K that FIX F. The full automorphism
group Aut(K) might be much larger. The "fixing F" condition is crucial.

**"Solvable group means the group can be factored."**
Solvable means the derived series eventually reaches {e}. This is weaker than
abelian but stronger than simple. It says the group can be "unraveled" step by
step through abelian layers. The word "solvable" comes from "solvable by radicals."

**"The quintic has no roots."**
It has 5 roots (in C, by the Fundamental Theorem of Algebra). The issue is
expressing them using the four arithmetic operations and nth roots, starting from
the coefficients — no such general formula exists.

**"Non-solvable means every quintic is hard."**
Most quintics with integer coefficients ARE solvable (their Galois group over Q
might not be all of S₅). The theorem says: the GENERAL quintic (with abstract
coefficient variables) has Gal = S₅. For specific polynomials, compute the Galois
group case by case.
