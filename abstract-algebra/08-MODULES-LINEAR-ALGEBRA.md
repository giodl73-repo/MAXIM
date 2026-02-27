# Modules and Linear Algebra

## The Big Picture

```
+====================================================================+
|              MODULES — VECTOR SPACES OVER RINGS                    |
+====================================================================+
|                                                                    |
|  F-VECTOR SPACE: V with scalar multiplication F × V → V, F FIELD  |
|       |                                                            |
|       | generalize: replace F by any ring R                        |
|       v                                                            |
|  R-MODULE: M with R × M → M, R RING                               |
|                                                                    |
|  LOSS vs GAIN:                                                     |
|  - Lose: basis always exists, all bases same size, free ↔ projective|
|  + Gain: captures abelian groups (Z-modules), ideals (R-modules),  |
|          representations (k[G]-modules), chain complexes          |
|                                                                    |
|  FREE MODULE: M ≅ R^n (has a basis)                               |
|  PROJECTIVE: direct summand of a free module                      |
|  FLAT: M ⊗_R - is exact                                          |
|  INJECTIVE: Hom(-, M) is exact                                    |
|                                                                    |
|  STRUCTURE THEOREM FOR FINITELY GENERATED MODULES OVER PID:        |
|  M ≅ R^r ⊕ R/(d₁) ⊕ R/(d₂) ⊕ ... ⊕ R/(dₖ)                     |
|  where d₁ | d₂ | ... | dₖ  (invariant factor form)               |
+====================================================================+
```

---

## Module Definitions

```
LEFT R-MODULE M:
  (M, +): abelian group.
  Scalar multiplication: R × M → M by (r,m) ↦ r·m.
  Axioms:
    r(m+n) = rm + rn         (distributive over M)
    (r+s)m = rm + sm         (distributive over R)
    (rs)m = r(sm)            (associativity)
    1_R · m = m              (unit acts as identity)

RIGHT MODULE: multiplication M × R → M. For commutative R: left = right.

EXAMPLES:
  R-module R: R acts on itself by multiplication. (Free module of rank 1.)
  Abelian group A: A is a Z-module. (Every abelian group is a Z-module.)
  Vector space V over F: V is an F-module.
  Ideal I ⊆ R: I is a submodule of R (as R acts on I).
  Quotient R/I: R-module.
  k[G]-module: same as a representation of G over k (group algebra module).
    r = Σ rₐa (formal sum), (Σrₐa)·v = Σrₐ(a·v).
  R[x]-module M with an endomorphism T: M → M acting as "multiplication by x."
    This packages linear operator theory into module language.
```

---

## Submodules and Quotient Modules

```
SUBMODULE: N ≤ M means N is a subgroup closed under R-action: rn ∈ N ∀r∈R, n∈N.

QUOTIENT MODULE: M/N = cosets {m+N}, R-action r(m+N) = (rm)+N.

MODULE HOMOMORPHISM: f: M → N with f(m+m') = f(m)+f(m') and f(rm) = rf(m).
  Kernel: ker(f) is a submodule of M.
  Image: im(f) is a submodule of N.

ISOMORPHISM THEOREMS hold exactly as for rings and groups:
  M/ker(f) ≅ im(f).

DIRECT SUM: M ⊕ N (the product module with componentwise operations).

EXAMPLES:
  Submodule of Z (as Z-module): subgroup nZ.
  Submodule of Z²: {(a,b) : a≡0 mod 2} or any subgroup closed under Z-action.
  In k[x]-module on V with T: submodule = T-invariant subspace.
```

---

## Free Modules

```
FREE MODULE: M is free of rank n if M ≅ R^n = R ⊕ R ⊕ ... ⊕ R (n times).
  Equivalently: M has a basis {e₁,...,eₙ} with every m ∈ M uniquely:
  m = r₁e₁ + ... + rₙeₙ, rᵢ ∈ R.

OVER A FIELD: every module (= vector space) is free. Rank = dimension.

OVER Z: free Z-modules = free abelian groups Z^n. Every subgroup of Z^n is free
  (of rank ≤ n). Not every Z-module is free (Z/2Z is not free).

OVER A RING: free modules exist. Not all modules are free.
  Example: Z/2Z as Z-module: if it were free of rank n, it would be isomorphic to Z^n,
  which is infinite. So Z/2Z is not free.

FREE MODULE UNIVERSAL PROPERTY:
  Given basis B = {eᵢ}, any function f: B → N (any module N) extends uniquely
  to a module homomorphism f̄: R^{|B|} → N.
  ("Free" = no relations between basis elements; fully flexible.)
```

---

## Projective, Injective, and Flat Modules

```
PROJECTIVE MODULE P:
  Definition: Hom(P, -) is exact  (projective modules see every surjection as surjective).
  Equivalently: P is a direct summand of a free module.
  Equivalently: Every surjection M → P splits (a section s: P → M exists).

  Over a field: all modules projective.
  Over Z: projective = free (since Z is a PID).
  Over a general ring: projective ≠ free.
    Stably free but not free: Serre's conjecture (proved by Quillen-Suslin 1976):
    over k[x₁,...,xₙ] (polynomial ring), projective modules ARE free.
  Over Dedekind domains: projective = rank-1 ideal module. Directly relates to class group.
    Ideal class group = group of rank-1 projective modules modulo free ones.

INJECTIVE MODULE I:
  Definition: Hom(-, I) is exact.
  Equivalently: Every injection I → M splits (a retraction r: M → I exists).

  Baer's criterion: I is injective iff every homomorphism from an ideal to I
  extends to all of R.
  Over Z: injective Z-modules = divisible abelian groups (Q, Q/Z, Z/p^∞).

FLAT MODULE M:
  M ⊗_R - is exact (i.e., tensoring with M preserves short exact sequences).
  Free → Projective → Flat (implications, not equivalences in general).
  Over a PID: flat = torsion-free.
  Over a Noetherian ring: finitely generated flat = projective.

WHY THIS MATTERS (derived categories, homological algebra):
  Short exact sequence 0 → A → B → C → 0:
  Applying exact functor: sequence stays exact.
  Applying non-exact functor: get derived functors Ext^n, Tor_n measuring deviation.
  Ext^1(C,A) classifies extensions 0 → A → B → C → 0.
  Tor_1(C,A) = "torsion interference" when tensoring.
```

---

## Structure Theorem for Finitely Generated Modules over PIDs

```
THEOREM: Let R be a PID, M a finitely generated R-module.
  M ≅ R^r ⊕ R/(d₁) ⊕ R/(d₂) ⊕ ... ⊕ R/(dₖ)
  where d₁ | d₂ | ... | dₖ (each dᵢ is nonzero, not a unit).

  r = rank (the "free part")
  d₁,...,dₖ = invariant factors (uniquely determined).

EQUIVALENTLY (primary decomposition):
  M ≅ R^r ⊕ ⊕_{p prime, i ≥ 1} R/(pⁱ)^{n(p,i)}

THE CASES:
  R = Z: gives the Classification of Finitely Generated Abelian Groups.
  R = k[x]: gives the Rational Canonical Form / Jordan Normal Form for linear operators.
```

### Application: Finitely Generated Abelian Groups

```
CLASSIFICATION OF FINITELY GENERATED ABELIAN GROUPS:
  A ≅ Z^r ⊕ Z/d₁ ⊕ Z/d₂ ⊕ ... ⊕ Z/dₖ
  where r ≥ 0, d₁ | d₂ | ... | dₖ, dᵢ ≥ 2.

  The dᵢ are the INVARIANT FACTORS; r is the RANK.

  ALTERNATIVELY (primary decomposition):
  A ≅ Z^r ⊕ Z/p₁^{a₁} ⊕ Z/p₂^{a₂} ⊕ ... (one factor per prime power).

EXAMPLES of abelian groups of order 12 = 4·3:
  Invariant factor form: Z/12, Z/2⊕Z/6.
  Primary form: Z/4⊕Z/3, Z/2⊕Z/2⊕Z/3.
  (Z/12 ≅ Z/4⊕Z/3 by CRT; Z/6 ≅ Z/2⊕Z/3.)
  So: two non-isomorphic abelian groups of order 12.
  [Three non-isomorphic groups of order 8 = 2³: Z/8, Z/4⊕Z/2, Z/2⊕Z/2⊕Z/2.]
```

### Application: Jordan Normal Form

```
A vector space V with linear operator T: V → V.
Becomes a k[x]-module via x·v = T(v).

The structure theorem gives:
  V ≅ k[x]/(p₁^{a₁}) ⊕ ... ⊕ k[x]/(pₘ^{aₘ})

Each factor k[x]/(pᵢ^{aᵢ}) for irreducible pᵢ corresponds to a JORDAN BLOCK:
  If pᵢ = x-λᵢ (linear, char = 0 or algebraically closed):
  k[x]/((x-λ)^a) has basis {1, x-λ, ..., (x-λ)^{a-1}}.
  T acts as: (x-λ)^j ↦ (x-λ)^{j+1} (or 0 at top).
  This is exactly the Jordan block with eigenvalue λ and size a.

RATIONAL CANONICAL FORM (over any field, not just algebraically closed):
  Use invariant factors instead of primary decomposition.
  Each invariant factor d(x) ∈ k[x] gives companion matrix:
  k[x]/(d(x)) has companion matrix with characteristic polynomial d(x).
  Valid over any field; works even when eigenvalues not in k.

This shows: matrix theory over a field k = module theory over k[x].
The entire theory of eigenvalues, Jordan form, rational canonical form
is ONE theorem (structure theorem for f.g. modules over PIDs).
```

---

## Tensor Products of Modules

```
M ⊗_R N: universal bilinear map M × N → M ⊗_R N.

CONSTRUCTION: Free module on M × N, quotient by bilinearity relations:
  (m₁+m₂) ⊗ n = m₁⊗n + m₂⊗n
  m ⊗ (n₁+n₂) = m⊗n₁ + m⊗n₂
  (rm)⊗n = m⊗(rn)  [the R-bilinearity condition]

UNIVERSAL PROPERTY: For any R-bilinear f: M×N → P, ∃! linear f̄: M⊗N → P.

EXAMPLES:
  Z/m ⊗_Z Z/n ≅ Z/gcd(m,n).
    Proof: 1⊗1 generates. n(1⊗1) = 1⊗n = 1⊗0 = 0; m(1⊗1) = m⊗1 = 0⊗1 = 0.
    So order of 1⊗1 divides gcd(m,n). And gcd(m,n)·(1⊗1) = 0 can be shown.
  M ⊗_R R ≅ M.
  R/I ⊗_R M ≅ M/IM.  [very useful for reducing computations]
  k[x]/(f) ⊗_{k[x]} k[x]/(g) ≅ k[x]/(gcd(f,g)) over PID k[x].

TENSOR-HOM ADJUNCTION:
  Hom_R(M ⊗_R N, P) ≅ Hom_R(M, Hom_R(N, P))  (natural isomorphism).

IN PHYSICS: tensor products combine state spaces.
  Spin-1/2 ⊗ Spin-1/2 = Hilbert space for two-particle system.
  V^{j₁} ⊗ V^{j₂}: Clebsch-Gordan decomposition.
```

---

## Chain Complexes and Exact Sequences

```
CHAIN COMPLEX:
  ... → M_{n+1} →^{d_{n+1}} M_n →^{d_n} M_{n-1} → ...
  Requirement: d_n ∘ d_{n+1} = 0 (image ⊆ kernel at each step).

HOMOLOGY: H_n = ker(d_n) / im(d_{n+1}).
  Measures "how far the sequence is from exact."

EXACT SEQUENCE:
  0 → A →^f B →^g C → 0  is exact iff:
  f is injective, g is surjective, im(f) = ker(g).
  Called a SHORT EXACT SEQUENCE.

THE SNAKE LEMMA: If you have a commutative diagram of two SES rows
  and vertical maps, you get a connecting homomorphism.
  Foundation of homological algebra.

LONG EXACT SEQUENCE IN Ext:
  0 → Hom(C,A) → Hom(B,A) → Hom(A,A) → Ext¹(C,A) → Ext¹(B,A) → ...
  The Ext groups measure obstructions to extending homomorphisms.

<!-- @editor[content/P2]: Chain complexes and Ext/Tor section is thin — introduces the concepts but stops short of the derived category, which is where this machinery lives. The derived category D(A) of an abelian category A is the natural setting for Ext^n (as Hom in D(A) shifted by n). For a TCS/Math reader: derived categories appear in mirror symmetry, algebraic K-theory, and persistent homology. The "so what" is completely missing from this section -->

<!-- @editor[bridge/P2]: No connection between module theory and persistent homology / topological data analysis — persistent homology is module theory over the polynomial ring k[t] (persistence modules), and the structure theorem for finitely generated modules over k[t] (a PID) gives the barcode decomposition. This is one of the most compelling modern applications of the structure theorem and directly relevant to ML/data science work -->
```

---

## Decision Cheat Sheet

| Task | Structure |
|------|-----------|
| Generalize vector spaces to ring scalars | R-module |
| Classify abelian groups | Structure theorem over Z (PID) |
| Understand Jordan form | k[x]-module structure theorem |
| Decompose a finitely generated module | Invariant factor form |
| Detect projective module | Direct summand of free |
| Detect injective (Z-module) | Divisible abelian group |
| Compute M⊗N for Z-modules | Use Z/m⊗Z/n ≅ Z/gcd(m,n) |
| Understand representations as modules | k[G]-modules where G is the group |

---

## Common Confusion Points

**"Free module = vector space."**
Over a field: yes. Over a general ring: no. Z² is free; Z/2Z is not.
A free module over Z is just a free abelian group (no torsion, rank = number of Z's).

**"Projective = free."**
Over Z or more generally any PID: projective implies free (Steinitz theorem over PIDs).
Over other rings: not true. Over a Dedekind domain O_K: a projective module of rank 1
is an invertible ideal — which is free iff the ideal is principal iff the class group
element is trivial. Non-trivial ideal classes give non-free projective modules.

**"Tensor product M⊗N has dimension dim(M)·dim(N)."**
Over a field: yes (dim V⊗W = dimV · dimW). Over Z: Z/m ⊗ Z/n ≅ Z/gcd(m,n),
which can be much smaller than expected. The tensor product "annihilates" torsion
that's incompatible between the two modules.

**"The structure theorem gives a canonical decomposition."**
The INVARIANT FACTOR form gives a unique decomposition (with invariant factors
uniquely determined). The PRIMARY DECOMPOSITION into prime power pieces is also
unique, but the isomorphism between the two descriptions requires CRT. Neither
decomposition is "natural" (independent of choices) — they're unique up to
isomorphism but not canonically embedded.
