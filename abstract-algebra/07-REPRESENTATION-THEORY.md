# Representation Theory

## The Big Picture

```
+====================================================================+
|          REPRESENTATION THEORY — GROUPS ACTING ON VECTOR SPACES    |
+====================================================================+
|                                                                    |
|  REPRESENTATION of G over F:                                       |
|  ρ: G → GL(V)  (homomorphism from G to invertible linear maps)    |
|  = "abstract group G" acting concretely on a vector space V        |
|                                                                    |
|  QUESTIONS:                                                        |
|  1. How many non-isomorphic irreducible representations?          |
|     Answer: one per conjugacy class.                               |
|  2. What are their dimensions?                                     |
|     Answer: d₁,d₂,...,dₖ with Σdᵢ² = |G|.                       |
|  3. How do tensor products decompose?                              |
|     Answer: character inner product (Clebsch-Gordan).             |
|                                                                    |
|  APPLICATIONS:                                                     |
|  Quantum mechanics: SU(2) → spin representations                  |
|  Chemistry: molecular orbitals from symmetry groups               |
|  Number theory: Artin L-functions from Galois representations      |
|  CS: Fourier transform on finite groups, graph symmetry            |
+====================================================================+
```

---

## Representations

```
DEFINITION: A representation (ρ, V) of group G over field F:
  V: F-vector space (finite-dimensional).
  ρ: G → GL(V): group homomorphism.

  Each ρ(g) is an invertible linear transformation V → V.
  ρ(e) = Id_V,  ρ(gh) = ρ(g)∘ρ(h).

EQUIVALENTLY: G-module structure on V.
  g · v = ρ(g)(v) satisfies:
  e·v = v, (gh)·v = g·(h·v), linearity in v.

DIMENSION: dim_F(V).

TRIVIAL REPRESENTATION: dim=1, ρ(g) = 1 for all g.
  Every group has this (trivial action).

REGULAR REPRESENTATION: V = F[G] (group algebra), ρ(g)(h) = gh.
  dim = |G|. Contains every irreducible as a subrepresentation.
```

### Subrepresentations and Irreducibility

```
SUBREPRESENTATION: W ≤ V is G-invariant: g·w ∈ W for all g∈G, w∈W.

IRREDUCIBLE REPRESENTATION (irrep): no proper nonzero subrepresentations.
  = "atomic" building blocks.

COMPLETELY REDUCIBLE: V = V₁ ⊕ V₂ ⊕ ... ⊕ Vₖ (direct sum of irreps).

MASCHKE'S THEOREM (over C or when char F ∤ |G|):
  Every finite-dimensional representation of a finite group G
  over F = C (or char 0, or char p ∤ |G|) is completely reducible.

Proof sketch: Given G-invariant W ≤ V, find G-invariant complement.
  Take any complement W', define the "G-averaged" projection:
  π̄ = (1/|G|) Σ_{g∈G} g ∘ π ∘ g^{-1}
  where π: V → W is any projection. Then π̄ is G-equivariant and idempotent.
  Its kernel is a G-invariant complement to W.  □

NOTE: Over fields with char | |G|, this fails.
  Example: F_p[Z/p] — the trivial subrepresentation has no G-invariant complement.
  Modular representation theory (char = p) is much harder.

<!-- @editor[content/P2]: Modular representation theory gets one dismissive sentence — for a graduate-level reader, Brauer characters, decomposition numbers, and the connection to p-local group theory (blocks, defect groups) are a major branch. The remark "much harder, active research area" is true but gives nothing to hold onto. Add: Brauer characters are characters in char 0 (lifted via Teichmüller), decomposition numbers relate ordinary to Brauer characters, Alperin's weight conjecture is the main open problem -->
```

---

## Characters

```
CHARACTER of representation (ρ,V):
  χ_V: G → F by χ_V(g) = Tr(ρ(g)).

PROPERTIES:
  χ(e) = dim(V).
  χ(g) = χ(hgh^{-1}) — character is a class function (constant on conjugacy classes).
  χ(g^{-1}) = χ̄(g) (for unitary representations over C: χ̄ = complex conjugate).
  χ_{V⊕W} = χ_V + χ_W.
  χ_{V⊗W} = χ_V · χ_W  (pointwise product!).

INNER PRODUCT ON CLASS FUNCTIONS:
  ⟨χ, ψ⟩ = (1/|G|) Σ_{g∈G} χ(g) ψ̄(g).

SCHUR'S ORTHOGONALITY RELATIONS:
  ⟨χᵢ, χⱼ⟩ = δᵢⱼ  (irreducible characters are orthonormal).

DECOMPOSITION FORMULA:
  If V = ⊕ nᵢVᵢ (decomposition into irreps):
  nᵢ = ⟨χ_V, χᵢ⟩ = (1/|G|) Σ_g χ_V(g) χ̄ᵢ(g).

KEY THEOREM: Two representations are isomorphic iff they have the same character.
  "Characters determine representations."
```

---

## Schur's Lemma

```
SCHUR'S LEMMA: Let V, W be irreducible representations of G.
  (a) Every G-equivariant map f: V → W is either 0 or an isomorphism.
  (b) Every G-equivariant endomorphism f: V → V is a scalar (f = λ Id_V).

Proof:
  (a): ker(f) is a G-invariant subspace of V (since f is G-equivariant and V irreducible).
       So ker(f) = 0 (hence f injective) or ker(f) = V (f=0).
       If f injective: im(f) is G-invariant in W, nonzero, hence all of W. □

  (b): f has an eigenvalue λ (over C, all operators have eigenvalues).
       f - λId is G-equivariant and not an isomorphism (has non-trivial kernel).
       By (a): f - λId = 0 → f = λId. □

CONSEQUENCE:
  EndG(V) = F for irreducible V over algebraically closed F.
  The G-equivariant endomorphisms form a division algebra.
  Over C: they're just scalars (by Schur's Lemma).

APPLICATION:
  Abelian groups: all irreps over C are 1-dimensional.
  Proof: for abelian G, every ρ(h) is G-equivariant (since G abelian).
  By Schur's Lemma: each ρ(h) = scalar. So every G-invariant subspace is the whole space — dim=1.
```

---

## Character Tables

```
CHARACTER TABLE of G: matrix where rows = irreducible characters, columns = conjugacy classes.
  Entry (i,j) = χᵢ(gⱼ) (value of i-th character on j-th conjugacy class).

NUMBER OF IRREPS = NUMBER OF CONJUGACY CLASSES (over C).
  (One of the key theorems of the subject.)

SIZE CONSTRAINT: Σᵢ (dim Vᵢ)² = |G|.

EXAMPLE: Character table of S_3 (= D_3).
  |S_3| = 6.  3 conjugacy classes: {e}, {(12),(13),(23)}, {(123),(132)}.

  G = S_3:     | {e}  | 3 transp. | 2 3-cycles |
  -------------+-------+-----------+------------+
  χ_trivial    |   1   |     1     |      1     |
  χ_sign       |   1   |    -1     |      1     |
  χ_standard   |   2   |     0     |     -1     |

  Check: 1²+1²+2² = 6 = |S_3|. ✓
  Orthogonality: ⟨χ_triv, χ_sign⟩ = (1·1·1+3·1·(-1)+2·1·1)/6 = (1-3+2)/6 = 0. ✓

EXAMPLE: Character table of Z/4Z = {0,1,2,3}.
  4 conjugacy classes (each element is its own class — abelian).
  4 one-dimensional irreps: χₖ(j) = e^{2πijk/4} = iᵏʲ.

  Z/4Z:        | 0 | 1 | 2 | 3 |
  χ₀           | 1 | 1 | 1 | 1 |
  χ₁           | 1 | i |-1 |-i |
  χ₂           | 1 |-1 | 1 |-1 |
  χ₃           | 1 |-i |-1 | i |

  This is exactly the DFT matrix! (Discrete Fourier Transform)
```

---

## Representation Theory of SU(2) and SO(3)

```
SU(2) = {M ∈ GL(2,C) : M*M=I, det(M)=1}.
  SU(2) ≅ S³ as a topological space.
  As a Lie group, connected and simply connected.

IRREDUCIBLE REPRESENTATIONS OF SU(2):
  One for each dimension n = 1, 2, 3, 4, ...
  V_n = symmetric n-th tensor power of C² = polynomials of degree n-1 in z₁,z₂.
  dim V_n = n.
  Highest weight: n-1 (quantum number = (n-1)/2).

HALF-INTEGER SPIN:
  Spin j = (n-1)/2 for n = 1,2,3,...
  j = 0: trivial (spin-0, scalar).
  j = 1/2: V_2 (2-dimensional — spinor, electron).
  j = 1: V_3 (3-dimensional — vector boson).
  j = 3/2: V_4 (4-dimensional — Δ baryon).

SO(3) REPRESENTATIONS:
  SO(3) = SU(2)/{±I} (quotient by center).
  Representations of SO(3) = representations of SU(2) where -I acts trivially.
  Only ODD-dimensional irreps of SU(2) descend to SO(3): j = 0, 1, 2, ...
  EVEN-dimensional (j = 1/2, 3/2, ...) do NOT descend — these are "spinors."
  This is why spin-1/2 requires a full 720° rotation to return to original state.

CLEBSCH-GORDAN DECOMPOSITION:
  V_m ⊗ V_n ≅ ⊕_{k=|m-n|/2}^{(m+n)/2} V_{2k+1}
  (using half-integer j notation: V^{j₁} ⊗ V^{j₂} ≅ ⊕_{j=|j₁-j₂|}^{j₁+j₂} V^j)

  Example: spin-1/2 ⊗ spin-1/2 = spin-0 ⊕ spin-1 (singlet + triplet).
  The "spin addition" rule in quantum mechanics.
```

---

## Induced Representations

```
If H ≤ G and (σ, W) is a representation of H:
  Induced representation Ind_H^G(σ): a representation of G.
  dim(Ind_H^G(σ)) = [G:H] · dim(σ).

CONSTRUCTION:
  Ind_H^G(W) = F[G] ⊗_{F[H]} W
  As a vector space: {functions f: G → W : f(hg) = σ(h)f(g)}, dim = [G:H]·dim(W).

FROBENIUS RECIPROCITY:
  ⟨Ind_H^G(σ), ρ⟩_G = ⟨σ, Res_H^G(ρ)⟩_H
  (Inner product in G = inner product in H of the restriction.)

APPLICATIONS:
  Character values: χ_{Ind(σ)}(g) = (1/|H|) Σ_{x∈G, x^{-1}gx∈H} χ_σ(x^{-1}gx).
  Artin's theorem: every character of G is a Q-linear combination of characters
    induced from cyclic subgroups.
  This is used to study L-functions (Artin induction in number theory).
```

---

## Fourier Analysis on Finite Groups

```
DISCRETE FOURIER TRANSFORM on Z/nZ:
  f: Z/nZ → C.
  f̂(k) = Σ_{j=0}^{n-1} f(j) e^{-2πijk/n}.
  = ⟨f, χₖ⟩ where χₖ(j) = e^{2πijk/n} are the characters of Z/nZ.

FOURIER INVERSION:
  f(j) = (1/n) Σ_k f̂(k) e^{2πijk/n}.

FAST FOURIER TRANSFORM (FFT):
  O(n log n) algorithm for DFT.
  Exploits the decomposition Z/nZ = Z/2Z × Z/(n/2)Z (for n even).
  Each split halves the problem: T(n) = 2T(n/2) + O(n) → O(n log n).

GENERAL GROUPS:
  For non-abelian group G: irreps ρᵢ of dimension dᵢ.
  f̂(ρᵢ) = Σ_{g∈G} f(g) ρᵢ(g)  [matrix-valued Fourier coefficient]
  Plancherel formula: Σ_{g∈G} |f(g)|² = Σᵢ dᵢ Tr(f̂(ρᵢ)* f̂(ρᵢ)).

NTT (Number Theoretic Transform):
  FFT over Z/pZ instead of C. Used in:
  Polynomial multiplication in polynomial-time algorithms.
  Lattice-based cryptography (Kyber uses NTT in Z_q[x]/(x^n+1)).

<!-- @editor[bridge/P2]: Harmonic analysis on non-abelian groups (the non-abelian Fourier transform) is introduced in one paragraph but the applications are absent — graph neural networks that are equivariant to the symmetric group use exactly this machinery (Zaheer et al., DeepSets; Maron et al., invariant/equivariant networks). The non-abelian FFT on S_n is polynomial time and is used in computational group theory for efficient group product computations. The learner calibration calls out "representation theory → harmonic analysis on groups" as a best bridge; this section has the math but needs the application anchor -->
```

---

## Decision Cheat Sheet

| Task | Tool |
|------|------|
| Decompose representation into irreps | Compute character inner products ⟨χ_V, χᵢ⟩ |
| Check if rep is irreducible | ⟨χ,χ⟩ = 1 iff irreducible |
| Count irreducible representations | = number of conjugacy classes of G |
| Find dimensions of irreps | Σdᵢ² = |G|; each dᵢ | |G| |
| Understand spin-1/2 | SU(2) 2-dim irrep; doesn't factor through SO(3) |
| Tensor product of irreps | Clebsch-Gordan: decompose character product |
| Build character table | Orthogonality relations + size constraints |
| Apply FFT | Characters of Z/nZ = Fourier modes |

---

## Common Confusion Points

**"All representations are direct sums of irreducibles (over any field)."**
Over C, or over fields where char ∤ |G|: yes (Maschke's theorem).
Over F_p when p | |G|: NO. There exist indecomposable but reducible representations.
This is modular representation theory — much harder, active research area.

**"SU(2) and SO(3) have the same representations."**
SU(2) has irreps of all dimensions 1,2,3,... — integer and half-integer spin.
SO(3) only has odd-dimensional irreps (integer spin: 1,3,5,...).
The half-integer spin representations exist for SU(2) but NOT for SO(3).
The covering map SU(2) → SO(3) is 2-to-1 with kernel {±I}.

**"Character determines the representation up to equivalence only over C."**
Over C: yes, characters uniquely determine (algebraically closed characteristic 0).
Over R or finite fields: characters in general may not fully distinguish representations.
Over C (for finite groups), the theorem is exactly: same character = isomorphic.

**"The Fourier transform on Z/nZ is unrelated to representation theory."**
The DFT IS the decomposition of functions on Z/nZ into irreducible representations.
The irreps of Z/nZ are the characters χₖ(j) = e^{2πijk/n}.
The Fourier coefficients are exactly the multiplicities in the decomposition.
FFT = fast algorithm exploiting the cyclic group structure.
