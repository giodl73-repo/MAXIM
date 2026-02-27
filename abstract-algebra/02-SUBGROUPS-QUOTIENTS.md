# Subgroups, Quotient Groups, and the Isomorphism Theorems

## The Big Picture

```
+====================================================================+
|     THE ARCHITECTURE OF QUOTIENTS AND HOMOMORPHISMS               |
+====================================================================+
|                                                                    |
|       G  ──φ──→  H                                               |
|       |                                                           |
|  G/ker(φ) ──≅──→ im(φ)    [First Isomorphism Theorem]            |
|                                                                    |
|  Normal subgroup N ◁ G  ←→  Kernel of some homomorphism G → ?    |
|  (Normal = invariant under conjugation)                           |
|                                                                    |
|  QUOTIENT CONSTRUCTION:                                           |
|  G/N = {cosets gN : g ∈ G}                                       |
|  Multiplication: (gN)(hN) = (gh)N  ← well-defined iff N ◁ G    |
|                                                                    |
|  THE THREE ISOMORPHISM THEOREMS control all quotient structure:   |
|  1st: G/ker ≅ im     (homomorphism theorem)                       |
|  2nd: H/(H∩N) ≅ HN/N  (diamond theorem)                         |
|  3rd: (G/N)/(K/N) ≅ G/K  (tower theorem)                        |
+====================================================================+
```

---

## Normal Subgroups

```
DEFINITION: N ◁ G (N is normal in G) iff:
  gNg^{-1} = N  for all g ∈ G.
  Equivalently: gN = Ng for all g  (left cosets = right cosets).
  Equivalently: gng^{-1} ∈ N for all g ∈ G, n ∈ N.

EXAMPLES OF NORMAL SUBGROUPS:
  - {e} and G itself (always normal — trivial cases).
  - Any subgroup of an abelian group (since gHg^{-1} = H always).
  - Kernel of any homomorphism φ: G → H.
    Proof: if φ(n) = e, then φ(gng^{-1}) = φ(g)φ(n)φ(g)^{-1} = φ(g)·e·φ(g)^{-1} = e.
  - Index-2 subgroups (only two cosets, each must be both left and right coset).
  - A_n in S_n (index 2).
  - SL(n,F) in GL(n,F) (kernel of det: GL → F*).
  - Center Z(G) = {g : gx=xg for all x} (always normal; may be trivial).

EXAMPLES OF NON-NORMAL SUBGROUPS:
  In S_3: H = {e, (12)} has index 3.
    (123)·H = {(123),(13)}, but H·(123) = {(123),(23)}. Not equal.

CONJUGATE SUBGROUPS: gHg^{-1} and H are isomorphic (conjugate = "same up to relabeling").
  Normal means: H equals all its conjugates.
```

---

## Quotient Groups

```
CONSTRUCTION: Given N ◁ G, define:
  G/N = {gN : g ∈ G}  (the set of left cosets)
  Multiplication: (gN)(hN) := (gh)N
  Identity: eN = N
  Inverse: (gN)^{-1} = g^{-1}N

WHY NORMALITY IS NECESSARY:
  Well-definedness of (gN)(hN) = (gh)N requires:
  If g₁N = g₂N (i.e., g₁^{-1}g₂ ∈ N) and h₁N = h₂N (i.e., h₁^{-1}h₂ ∈ N),
  then (g₁h₁)N = (g₂h₂)N, i.e., (g₁h₁)^{-1}(g₂h₂) ∈ N.
  (g₁h₁)^{-1}(g₂h₂) = h₁^{-1}g₁^{-1}g₂h₂.
  Let a = g₁^{-1}g₂ ∈ N, b = h₁^{-1}h₂ ∈ N.
  Need: h₁^{-1}·a·h₁·b ∈ N  ⟺  h₁^{-1}ah₁ ∈ N.
  This holds iff N is normal (h₁^{-1}Nh₁ = N).

NATURAL HOMOMORPHISM: π: G → G/N by g ↦ gN.
  This is a surjective homomorphism with kernel = N.
  Confirms: kernels are exactly normal subgroups.

EXAMPLES:
  G = Z, N = nZ: Z/nZ (integers mod n). The "clock" arithmetic.
  G = GL(n,F), N = SL(n,F): GL/SL ≅ F* (via det).
  G = S_n, N = A_n: S_n/A_n ≅ Z/2 (sign homomorphism).
  G = R, N = Z: R/Z ≅ S¹ (circle group; continuous).
  G = D_n, N = {rotations}: D_n/N ≅ Z/2 (flip = non-trivial coset).
```

---

## The Three Isomorphism Theorems

### First Isomorphism Theorem

```
THEOREM: If φ: G → H is a group homomorphism, then:
  G / ker(φ)  ≅  im(φ)

Proof:
  Define ψ: G/ker(φ) → im(φ) by ψ(gK) = φ(g)  where K = ker(φ).
  Well-defined: if g₁K = g₂K then g₁^{-1}g₂ ∈ K, so φ(g₁^{-1}g₂) = e,
    so φ(g₁) = φ(g₂).
  Homomorphism: ψ(g₁K · g₂K) = ψ(g₁g₂K) = φ(g₁g₂) = φ(g₁)φ(g₂) = ψ(g₁K)ψ(g₂K).
  Injective: ψ(gK) = e iff φ(g) = e iff g ∈ K iff gK = K = identity coset.
  Surjective: every φ(g) = ψ(gK).  □

APPLICATIONS:
  Z → Z/nZ (reduction mod n): Z/nZ ≅ Z/nZ. Trivially confirms the construction.
  det: GL(n,F) → F*: GL/SL ≅ F*. |GL(n,F_p)| = (p^n-1)·|SL(n,F_p)|.
  exp: (R,+) → (R_{>0},×): R/Z ≅ ... wait: (R,+)→(R_{>0},×) by e^x.
    ker = {x: e^x=1} = {0}. im = R_{>0}. R/{0} ≅ R ≅ R_{>0}.  ✓
  sign: S_n → {±1}: S_n/A_n ≅ Z/2Z.

This theorem says: the image of φ is (up to isomorphism) determined by G and ker(φ).
```

### Second Isomorphism Theorem

```
THEOREM: Let H ≤ G and N ◁ G. Then:
  HN = {hn : h ∈ H, n ∈ N} is a subgroup of G.
  H ∩ N ◁ H.
  H/(H∩N) ≅ HN/N.

Proof sketch:
  The map H → HN/N by h ↦ hN is a surjective homomorphism with kernel H∩N.
  Apply First Isomorphism Theorem.  □

GEOMETRIC PICTURE (the "diamond"):
         G
        / \
       HN  ?
      / \ /
     H   N
      \ /
      H∩N

The second isomorphism theorem says the two "sides" of the diamond are isomorphic:
  H/(H∩N) ≅ HN/N.

EXAMPLE:
  G = Z, N = 12Z, H = 8Z.
  HN = 8Z + 12Z = gcd(8,12)Z = 4Z.   [smallest group containing both]
  H ∩ N = lcm(8,12)Z = 24Z.
  H/(H∩N) = 8Z/24Z ≅ Z/3.
  HN/N = 4Z/12Z ≅ Z/3.  ✓
```

### Third Isomorphism Theorem

```
THEOREM: If N ◁ K ◁ G and N ◁ G, then:
  K/N ◁ G/N  and  (G/N)/(K/N) ≅ G/K.

Proof: The map G/N → G/K by gN ↦ gK is a well-defined surjective homomorphism
  with kernel K/N. Apply First Isomorphism Theorem.  □

INTUITION: "Quotient of quotients is a quotient."
  If you mod out by N first, then by K/N, you get the same as modding by K.
  Like: (Z/6Z)/(2Z/6Z) ≅ Z/2Z.  [mod 6, then mod 3 classes ≅ mod 2]

CORRESPONDENCE THEOREM (lattice isomorphism):
  If N ◁ G, the subgroups of G/N are in bijection with subgroups of G containing N.
  H/N ↔ H,  for N ≤ H ≤ G.
  Normality, index, and containment are preserved.
```

---

## Direct and Semidirect Products

### Direct Product

```
G × H: Cartesian product with componentwise operation.
  (g₁,h₁)(g₂,h₂) = (g₁g₂, h₁h₂).
  |G × H| = |G| · |H|.
  G × H is abelian iff both G and H are abelian.

INTERNAL DIRECT PRODUCT:
  G = N × K (internally) iff:
    N ◁ G, K ◁ G,  NK = G,  N ∩ K = {e}.

EXAMPLE:
  Z/6Z ≅ Z/2Z × Z/3Z (by CRT, since gcd(2,3)=1).
  Z/4Z ≇ Z/2Z × Z/2Z (Z/4 has element of order 4; Z/2×Z/2 does not).
```

### Semidirect Product

```
N ⋊_φ H: "N twisted by H using action φ."

Data:
  N ◁ G (normal factor),
  H ≤ G (complement),
  φ: H → Aut(N) (action by conjugation: h acts on N by n ↦ hnh^{-1}).

Operation: (n₁,h₁)(n₂,h₂) = (n₁·φ(h₁)(n₂), h₁h₂).
  Identity: (e_N, e_H).
  Inverse: (n,h)^{-1} = (φ(h^{-1})(n^{-1}), h^{-1}).

KEY: G = N ⋊ H iff N ◁ G, H ≤ G, NH = G, N ∩ H = {e}.
  (Differs from direct product only if φ is non-trivial.)

EXAMPLES:
  D_n = Z/nZ ⋊ Z/2Z.  (Rotations ⋊ Reflections)
    Action: reflection sends rotation r to r^{-1}.
    φ: Z/2Z → Aut(Z/nZ), φ(s)(r^k) = r^{-k}.

  S_3 ≅ Z/3Z ⋊ Z/2Z.  (A_3 = Z/3 ⋊ Z/2)
    The non-trivial action: Z/2 acts on Z/3 by inversion.

  GA(1,F_p) = F_p ⋊ F_p*  (affine transformations x ↦ ax+b).
    Normal subgroup: translations (a=1).
    Complement: scalings (b=0).
```

---

## Derived Subgroup and Solvability

```
COMMUTATOR: [a,b] = aba^{-1}b^{-1}.
  [a,b] = e iff ab = ba.
  Measure of non-commutativity.

DERIVED SUBGROUP (COMMUTATOR SUBGROUP):
  [G,G] = G' = ⟨[a,b] : a,b ∈ G⟩.
  G' ◁ G (always normal).
  G/G' is abelian (and is the LARGEST abelian quotient of G).
  G is abelian iff G' = {e}.

DERIVED SERIES:
  G = G⁽⁰⁾ ≥ G⁽¹⁾ = [G,G] ≥ G⁽²⁾ = [G',G'] ≥ ...

SOLVABLE GROUP: The derived series reaches {e} in finitely many steps.
  Abelian groups: solvable (G'={e} at step 1).
  S₃: S₃' = A₃ ≅ Z/3, [A₃,A₃] = {e}. Solvable.
  S₄: solvable (S₄' = A₄, A₄' = V₄ = Z/2×Z/2, V₄' = {e}).
  S₅: NOT solvable. S₅' = A₅, and A₅ is SIMPLE (A₅' = A₅).
  → This is why there's no quintic formula.

LOWER CENTRAL SERIES (for nilpotency):
  G = G₁ ≥ G₂ = [G,G₁] ≥ G₃ = [G,G₂] ≥ ...
  Nilpotent: G_k = {e} for some k. Stronger than solvable.
  p-groups are nilpotent. S₃ is solvable but not nilpotent.
```

---

## Simple Groups

```
SIMPLE GROUP: No normal subgroups except {e} and G.
  (Indecomposable in the sense of normal subgroups.)

ABELIAN SIMPLE GROUPS: Only Z/pZ for prime p.

NON-ABELIAN SIMPLE GROUPS: Start with A_5 (smallest, order 60).
  A_5 ≅ PSL(2,5) ≅ PSL(2,4) — the icosahedral symmetry group.
  Proof A_5 is simple: Sylow analysis shows any normal subgroup must have
  order 1, 4, or 60, but can't have order 4 (detailed check).

JORDAN-HÖLDER THEOREM:
  Every finite group has a COMPOSITION SERIES:
  G = G₀ ▷ G₁ ▷ G₂ ▷ ... ▷ G_k = {e}
  Each G_i/G_{i+1} is simple.
  This series is unique up to reordering of composition factors.
  (Analogous to prime factorization for groups.)

CLASSIFICATION OF FINITE SIMPLE GROUPS (CFSG):
  Completed 2004, 10,000+ pages.
  Categories: cyclic Z/p, alternating A_n (n≥5), groups of Lie type, 26 sporadic.

<!-- @editor[content/P2]: CFSG entry is a 2-line stub for a result requiring 10,000+ pages — at minimum add: the count and names of the 26 sporadic groups, the Monster's order (~8×10^53), why Lie-type groups are the bulk of the classification, and what "completed 2004" means (the second-generation proof project). The learner can handle the full structure of the classification -->

<!-- @editor[bridge/P2]: No category-theoretic lens on quotients — in Grp (groups), normal subgroups are exactly what's needed for quotients to work because Grp is not an abelian category; in Ab (abelian groups), every subgroup is normal and every subgroup gives a quotient. The contrast Grp vs. Ab is the exact reason abelian categories were invented (Buchsbaum, Grothendieck). A TCS/category-theory reader needs this connection spelled out -->
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Check N ◁ G | gNg^{-1}=N, or N=ker(φ), or index 2 |
| Build G/N | N must be normal; cosets under multiplication |
| Use First Isom. Theorem | Find homomorphism, identify kernel and image |
| Decompose G as product | Find two normal subgroups with G=N₁N₂, N₁∩N₂={e} |
| Decompose G as semidirect | N ◁ G, H complement, find conjugation action φ |
| Show G solvable | Derived series reaches {e} |
| Show G NOT solvable | Derived series stabilizes at non-trivial simple group |
| Find composition factors | Jordan-Hölder: compute composition series |

---

## Common Confusion Points

**"Normal means the subgroup commutes with everything."**
Normal means gNg^{-1} = N for all g (the subgroup is invariant under conjugation),
NOT gn = ng for all g,n. An element n ∈ N may not commute with g, but its conjugate
gng^{-1} must be back in N.

**"G/N is always smaller than G."**
|G/N| = |G|/|N|, so G/N is "smaller." But the isomorphism classes can be anything:
G = Z, N = nZ: G/N = Z/nZ (finite quotient of an infinite group).

**"The isomorphism theorems are just bookkeeping."**
They encode deep structural information. The first IT is exactly why orbit-stabilizer
works (|G| = |orbit| · |stabilizer| = [G:Stab] · |Stab| from φ: G → G·x by g↦gx).
The third IT is why the Galois correspondence for tower extensions works.

**"Semidirect product is the same as direct product."**
If the action φ is trivial (h acts as identity), semidirect = direct. Otherwise,
they differ. D_n = Z/nZ ⋊ Z/2 with non-trivial action; this gives a non-abelian group.
Z/n × Z/2 would be abelian. The choice of action is what distinguishes them.
