# Representation Theory — Complete Reference

## The Big Picture

Representation theory studies how groups act on vector spaces — it is the bridge between abstract algebraic symmetry and concrete linear algebra. It is the mathematical language of particle physics (SU(2), SU(3), the Standard Model), quantum mechanics (angular momentum, spin), and crystallography. More recently it is the theoretical foundation for equivariant neural networks and geometric deep learning. From your MIT background in groups and linear algebra, you have all the prerequisites — this guide builds from finite groups to Lie groups to the physics and ML applications.

```
┌─────────────────────────────────────────────────────────────────────────────┐
│  REPRESENTATION THEORY LANDSCAPE                                             │
│                                                                              │
│  Finite Groups                        Compact Lie Groups                     │
│  ──────────────────────────────        ──────────────────────────────────     │
│  Group algebra ℂ[G]                   Lie algebras (tangent at identity)    │
│  Maschke's theorem (semisimplicity)   Exponential map exp: 𝔤 → G            │
│  Characters χ(g) = tr ρ(g)            Root systems, Dynkin diagrams         │
│  Character table                      Highest weight theorem                 │
│  Regular, induced representations     Weyl character formula                 │
│                                                                              │
│  Key Groups in Physics               ML & Computation                        │
│  ──────────────────────────────        ──────────────────────────────────     │
│  U(1): electromagnetism              G-equivariant networks (G-CNNs)        │
│  SU(2) ≅ Spin(3): fermions           SE(3)-equivariant molecular modeling   │
│  SU(3): strong force                 Permutation-equivariant (set networks) │
│  SU(2)×U(1): electroweak             Spectral graph theory / GNNs           │
│  SU(3)×SU(2)×U(1): Standard Model   Non-abelian Fourier (Peter-Weyl)       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. Representations of Finite Groups

### Definition

A **(linear) representation** of group G on vector space V (over field k) is a group homomorphism:
```
ρ: G → GL(V)

That is: ρ(gh) = ρ(g)ρ(h) and ρ(e) = I for all g,h ∈ G.

Equivalently: a left G-module structure on V.
  G acts on V via: g · v = ρ(g)v.

Degree (dimension) of ρ: dim V.
```

**Examples**:
```
Trivial representation: ρ(g) = 1 (or I) for all g. Degree 1.
Regular representation: V = ℂ[G] (group algebra), ρ(g) acts by left multiplication.
  dim = |G|. Contains every irrep with multiplicity = its degree.

Sign representation of Sₙ: ρ(σ) = sgn(σ) = ±1. Degree 1.
Standard representation of Sₙ: subrepresentation of ℂⁿ (sum-0 hyperplane). Degree n-1.

Permutation representation: G acts on set X, V = ℂ^X, g maps basis eₓ ↦ e_{gx}.
```

### Subrepresentations and Irreducibility

A **subrepresentation** (or G-invariant subspace) W ⊆ V satisfies: ρ(g)W ⊆ W for all g.

A representation is **irreducible** (irrep) if it has no proper nonzero subrepresentations.

**Maschke's Theorem**: For G finite with char(k) ∤ |G| (e.g., k = ℂ always):
```
Every representation V decomposes as a direct sum of irreducible representations.
V = V₁^{m₁} ⊕ V₂^{m₂} ⊕ ... ⊕ Vₛ^{mₛ}

mᵢ = multiplicity of Vᵢ in V.
Vᵢ are irreducible, and decomposition is unique (up to isomorphism).
```

**Proof idea**: For any G-invariant subspace W ⊆ V, construct a G-equivariant projection P: V → W by averaging over G:
```
P = (1/|G|) Σ_{g∈G} ρ(g) ∘ P₀ ∘ ρ(g)⁻¹
```
where P₀ is any projection onto W. Then Im(P) = W and ker(P) is also G-invariant.

**Schur's Lemma**: The fundamental lemma of representation theory.
```
Let ρ: G → GL(V) and σ: G → GL(W) be irreps.
Let φ: V → W be a G-equivariant map (intertwiner): φ∘ρ(g) = σ(g)∘φ.

(1) Either φ = 0 or φ is an isomorphism.
(2) If V = W (same irrep) and k = ℂ: φ = λI for some λ ∈ ℂ.

Proof of (1): ker(φ) and Im(φ) are G-invariant subspaces → by irreducibility, each is 0 or all.
Proof of (2): φ has an eigenvalue λ (over ℂ). ker(φ - λI) is G-invariant → = V.
```

**Consequence**: Irreps are the "atomic" building blocks. Over ℂ, the only intertwiners between distinct irreps are 0; self-intertwiners of an irrep are scalars.

---

## 2. Characters and Character Theory

### Characters

The **character** of representation ρ on V:
```
χ_ρ: G → ℂ
χ_ρ(g) = tr(ρ(g))

Properties:
  χ(e) = dim V
  χ(hgh⁻¹) = χ(g)  [class function: constant on conjugacy classes]
  χ(g⁻¹) = χ(g)̄   [complex conjugate]
  χ_{V⊕W} = χ_V + χ_W
  χ_{V⊗W} = χ_V · χ_W
```

### The Character Inner Product

```
⟨χ₁, χ₂⟩ = (1/|G|) Σ_{g∈G} χ₁(g) χ₂(g)̄

Orthogonality of characters (Schur's orthogonality):
  ⟨χᵢ, χⱼ⟩ = δᵢⱼ  for distinct irreps Vᵢ, Vⱼ.

Multiplicity formula:
  mᵢ = ⟨χ_V, χᵢ⟩ = (1/|G|) Σ_g χ_V(g) χᵢ(g)̄

  V is irreducible iff ⟨χ_V, χ_V⟩ = 1.
```

### The Character Table

```
Rows: one per irreducible representation.
Columns: one per conjugacy class.
Entry: χᵢ(Cⱼ) = value of character of ρᵢ on class Cⱼ.

Key facts:
  Number of irreps = number of conjugacy classes.
  Σᵢ (dim Vᵢ)² = |G|.
  Rows are orthonormal under (1/|G|)Σ_C |C| · (row1)(row2)̄.
  Columns are orthonormal under: (1/dim)Σ_ρ (dim ρ)(row of ρ at C₁)(row of ρ at C₂)̄.
```

**Character table of S₃** (symmetric group on 3 elements):
```
S₃ has 3 conjugacy classes: {e}, {(12),(13),(23)}, {(123),(132)}
  Sizes: 1, 3, 2

          e     (ij)    (ijk)
trivial:  1      1       1
sign:     1     -1       1
standard: 2      0      -1

Check: 1² + 1² + 2² = 6 = |S₃|. ✓
```

### Regular Representation

The regular representation ρ_reg has χ_reg(g) = |G|·δ_{g,e}.

Decomposition: ρ_reg = ⊕ᵢ (dim Vᵢ) · ρᵢ (each irrep Vᵢ appears with multiplicity dim Vᵢ).

Proof: ⟨χ_reg, χᵢ⟩ = (1/|G|)|G|·χᵢ(e) = dim Vᵢ. ✓

---

## 3. Induced Representations

### Construction

For H ≤ G (subgroup) and representation σ of H, the **induced representation** Ind_H^G(σ):
```
V = Ind_H^G(σ) = ℂ[G] ⊗_{ℂ[H]} W    (W = space of σ)
  = {functions f: G → W : f(hg) = σ(h)f(g) for all h ∈ H}

dim = [G:H] · dim σ

G acts by right translation: (g·f)(x) = f(xg).
```

**Frobenius reciprocity**:
```
Hom_G(Ind_H^G(σ), ρ) ≅ Hom_H(σ, Res_H^G(ρ))

In terms of characters:
  ⟨Ind_H^G(χ_σ), χ_ρ⟩_G = ⟨χ_σ, Res_H^G(χ_ρ)⟩_H

The number of times σ appears in ρ|_H = number of times Ind_H^G(σ) contains ρ.
```

Frobenius reciprocity is an adjunction: Ind ⊣ Res (induction is left adjoint to restriction).

---

## 4. Lie Groups and Lie Algebras

### Lie Groups

A **Lie group** G is both a group and a smooth manifold, with group operations smooth.

```
Key examples:
  GL(n,ℝ): invertible n×n real matrices. Open subset of ℝ^{n²}.
  GL(n,ℂ): invertible n×n complex matrices.
  SL(n): det=1 matrices. Codimension 1.
  O(n): orthogonal matrices (A'A=I). Compact.
  SO(n): special orthogonal (det=+1). Compact, connected.
  U(n): unitary matrices (A†A=I). Compact.
  SU(n): special unitary (det=1). Compact, simply connected for n≥2.
  Sp(2n): symplectic matrices.
  ℝ, ℝ*, S¹=U(1), torus T^n = (S¹)^n.
```

### Lie Algebras

The **Lie algebra** 𝔤 = Lie(G) of G is the tangent space at the identity:
```
𝔤 = T_e G

Structure: 𝔤 is a vector space with Lie bracket [·,·]: 𝔤×𝔤 → 𝔤.
  [X,Y] = -[Y,X]               [anti-symmetry]
  [X,[Y,Z]] + [Y,[Z,X]] + [Z,[X,Y]] = 0  [Jacobi identity]

For matrix Lie groups: 𝔤 = {X : e^{tX} ∈ G ∀t}
  [X,Y] = XY - YX  (matrix commutator)
```

**Correspondence table**:

| Lie group | Lie algebra | Bracket |
|-----------|------------|---------|
| GL(n,ℝ) | 𝔤𝔩(n,ℝ) = M(n,ℝ) | [X,Y]=XY-YX |
| SL(n) | 𝔰𝔩(n): tr=0 matrices | [X,Y]=XY-YX |
| SO(n) | 𝔰𝔬(n): skew-symmetric | [X,Y]=XY-YX |
| U(n) | 𝔲(n): skew-Hermitian | [X,Y]=XY-YX |
| SU(n) | 𝔰𝔲(n): skew-Hermitian, tr=0 | [X,Y]=XY-YX |
| SU(2) | 𝔰𝔲(2) ≅ ℝ³ | Lie bracket ↔ cross product |

### Exponential Map

```
exp: 𝔤 → G

exp(X) = e^X = Σ_{n=0}^∞ Xⁿ/n!   (matrix exponential for matrix groups)

Properties:
  exp(0) = e
  exp((s+t)X) = exp(sX)exp(tX)   [one-parameter subgroup]
  d/dt exp(tX)|_{t=0} = X
  If [X,Y]=0: exp(X+Y) = exp(X)exp(Y)

BCH formula: exp(X)exp(Y) = exp(X + Y + ½[X,Y] + 1/12[X,[X,Y]] - 1/12[Y,[X,Y]] + ...)
  (Baker-Campbell-Hausdorff — encodes non-commutativity of G)
```

For compact connected Lie groups, exp is surjective (every group element is a matrix exponential).

### SU(2) — The Rotation Group Double Cover

```
SU(2) = {A ∈ M(2,ℂ) : A†A=I, det A=1}
      = { (α  -β̄) : |α|²+|β|²=1 } ≅ S³ (3-sphere)
        (-β   ᾱ)

𝔰𝔲(2): spanned by iσ₁, iσ₂, iσ₃ (Pauli matrices times i)
  σ₁ = (0 1), σ₂ = (0 -i), σ₃ = (1  0)
       (1 0)       (i  0)       (0 -1)

  [iσⱼ/2, iσₖ/2] = -εⱼₖₗ (iσₗ/2)  [structure constants = Levi-Civita]

SU(2) ↠ SO(3): 2-to-1 homomorphism (both ±I ↦ identity rotation).
SU(2) is the double cover of SO(3), called Spin(3).
This is why spin-1/2 particles transform under SU(2) representations, not SO(3).
A rotation by 2π returns a vector to itself but rotates a spinor by -1.
```

---

## 5. Representations of Lie Groups

### Representation of a Lie Group

A smooth group homomorphism ρ: G → GL(V) for finite-dimensional V.

**Induced Lie algebra representation** dρ: 𝔤 → 𝔤𝔩(V):
```
dρ(X) = d/dt|_{t=0} ρ(exp(tX))

This is a Lie algebra homomorphism: dρ[X,Y] = [dρ(X), dρ(Y)].
For simply connected G: representations of G ↔ representations of 𝔤 (Lie's theorem).
```

### Representations of SU(2)

The irreps of SU(2) are indexed by non-negative half-integers j ∈ {0, 1/2, 1, 3/2, 2, ...}:
```
V_j: dimension 2j+1.

Angular momentum operators (from Lie algebra action):
  J_z eigenvalues: -j, -j+1, ..., j-1, j  (magnetic quantum numbers m)
  J² = J₁²+J₂²+J₃² = j(j+1)I on V_j

Physics identification:
  j=0:   spin-0 (scalar, meson π⁰)
  j=1/2: spin-1/2 (electron, quark, proton) — V_{1/2} = ℂ² (spinor)
  j=1:   spin-1 (photon, W/Z boson, vector particle)
  j=3/2: spin-3/2 (Δ baryon)
  j=2:   spin-2 (graviton, predicted)

Tensor product (Clebsch-Gordan):
  V_j ⊗ V_k = V_{|j-k|} ⊕ V_{|j-k|+1} ⊕ ... ⊕ V_{j+k}

  Example: j=1/2 ⊗ j=1/2 = j=0 ⊕ j=1
           Two spin-1/2 particles → singlet (j=0) + triplet (j=1).
           This is how hydrogen spin states decompose.
```

### Highest Weight Theory

For semisimple Lie algebras (SU(n), SO(n), Sp(2n) and their Lie algebras):

```
Cartan decomposition: 𝔤 = 𝔥 ⊕ (⊕_α 𝔤_α)
  𝔥 = Cartan subalgebra (maximal abelian semisimple)
  𝔤_α = root spaces, α ∈ Φ = root system

For 𝔰𝔩(2,ℂ):
  𝔥 = span{H = (1 0; 0 -1)}
  𝔤_+ = span{E = (0 1; 0 0)}   [raising operator]
  𝔤_- = span{F = (0 0; 1 0)}   [lowering operator]
  [H,E] = 2E,  [H,F] = -2F,  [E,F] = H

In any representation V:
  H acts diagonally (V = ⊕_m V_m where V_m = {v: Hv=mv})
  E raises: E: V_m → V_{m+2}
  F lowers: F: V_m → V_{m-2}

Highest weight vector v_max: E·v_max = 0.
  Starting from v_max, apply F repeatedly to get basis.
  Irrep of 𝔰𝔩(2) classified by highest weight λ = max eigenvalue of H.
  dim V = λ+1. For integer λ: actual SL(2) representation. Half-integer: spin rep.
```

**General semisimple Lie algebras**:
```
Root system Φ in 𝔥* (dual of Cartan subalgebra).
Positive roots Φ⁺, simple roots Δ = {α₁,...,αₗ} (l = rank of 𝔤).
Dynkin diagram encodes inner products between simple roots.

Highest weight theorem: Irreps of 𝔤 (compact semisimple) ↔ dominant integral weights
  λ ∈ 𝔥* with ⟨λ, αᵢ∨⟩ ∈ ℤ≥0 for all simple coroots αᵢ∨.

For SU(n): highest weight = (a₁,...,aₙ₋₁) ∈ ℤ≥0^{n-1}.
For SU(3): highest weight = (p,q), dim V = (p+1)(q+1)(p+q+2)/2.
```

---

## 6. SU(3) and the Quark Model

### The Lie Algebra 𝔰𝔲(3)

```
𝔰𝔲(3) has rank 2 (2-dimensional Cartan subalgebra).
8 generators: Gell-Mann matrices λ₁,...,λ₈.
  λ₃ and λ₈ diagonal (Cartan basis).
  [λᵢ,λⱼ] = 2i fᵢⱼₖ λₖ  (structure constants fᵢⱼₖ totally antisymmetric)

Root system: A₂ (hexagonal). 6 roots: ±α₁, ±α₂, ±(α₁+α₂).
Dynkin diagram: • — • (two nodes, simple edge).
```

### Fundamental Representations

```
3-representation (fundamental): 3-dimensional.
  Quarks: up (u), down (d), strange (s) — three "colors" = three states.
  Weight diagram: equilateral triangle in 2D weight space.

3̄-representation (anti-fundamental): complex conjugate of 3.
  Anti-quarks.

8-representation (adjoint): 8-dimensional.
  Gluons: 8 force carriers of strong interaction.
  Weight diagram: hexagon + origin (doubly degenerate).
```

**Tensor product decompositions**:
```
3 ⊗ 3̄ = 1 ⊕ 8        [singlet + octet; mesons = quark-antiquark]
3 ⊗ 3 = 3̄ ⊕ 6        [triplet + sextet]
3 ⊗ 3 ⊗ 3 = 1 ⊕ 8 ⊕ 8 ⊕ 10   [singlet + two octets + decuplet; baryons = 3 quarks]

The 10 in the last decomposition: baryon decuplet (Δ⁻⁻, Δ⁻, Δ⁰, Δ⁺, ..., Ω⁻).
Gell-Mann predicted the Ω⁻ (Omega minus) in 1962; discovered 1964. Nobel 1969.
```

---

## 7. Character Theory for Compact Groups

### Peter-Weyl Theorem

For compact Lie group G (with Haar measure):
```
L²(G) ≅ ⊕_ρ (V_ρ ⊗ V_ρ*)    [algebraic direct sum, Hilbert space completion]

where ρ ranges over irreducible representations.

The matrix coefficient functions ρ_{ij}: g ↦ ρ(g)_{ij} form an orthogonal basis of L²(G).
Characters χ_ρ = tr∘ρ are in L²(G) and encode representation theory.
```

**Plancherel formula** (non-abelian Fourier analysis):
```
For G compact: f ∈ L²(G) decomposes as:
  f(g) = Σ_ρ (dim ρ) tr(f̂(ρ) ρ(g)*)
  f̂(ρ) = ∫_G f(g) ρ(g) dg ∈ End(V_ρ)

Parseval: ∫_G |f(g)|² dg = Σ_ρ (dim ρ) ||f̂(ρ)||²_HS
  (||·||_HS = Hilbert-Schmidt norm = √tr(A†A))
```

This is exactly the non-abelian Fourier transform. For G = S¹ (circle), reduces to classical Fourier series. For G = ℝ (non-compact), reduces to Fourier transform.

### Weyl Character Formula

For compact semisimple G with highest weight λ:
```
χ_λ(exp H) = Σ_{w ∈ W} ε(w) e^{⟨w(λ+ρ), H⟩}
              ────────────────────────────────────
              Σ_{w ∈ W} ε(w) e^{⟨wρ, H⟩}

W = Weyl group, ε(w) = sign of w, ρ = half-sum of positive roots.

For SU(2): χ_j(θ) = sin((2j+1)θ)/sin(θ)  [the "Chebyshev" formula for characters]
  This is why characters of SU(2) are the Chebyshev polynomials.

Weyl dimension formula:
  dim V_λ = ∏_{α∈Φ⁺} ⟨λ+ρ, α⟩/⟨ρ, α⟩
```

---

## 8. Permutation Groups and Young Tableaux

### Irreps of Sₙ

Irreducible representations of Sₙ are indexed by **partitions** of n (Young diagrams):
```
Partition λ = (λ₁ ≥ λ₂ ≥ ... ≥ λₖ) with λ₁+...+λₖ = n.

Young diagram: rows of boxes with λᵢ boxes in row i.

For S₃ (n=3):
  (3): ☐☐☐          trivial representation (dim 1)
  (2,1): ☐☐          standard representation (dim 2)
         ☐
  (1,1,1): ☐         sign representation (dim 1)
            ☐
            ☐
```

**Hook length formula**: dim V_λ = n! / ∏ (hook lengths)

**RSK correspondence** (Robinson-Schensted-Knuth): Bijection between permutations σ ∈ Sₙ and pairs (P,Q) of standard Young tableaux of the same shape λ. Key connection between representation theory, combinatorics, and symmetric functions.

**Schur polynomials and symmetric functions**: The character of the GL(n)-representation with highest weight λ = (λ₁,...,λₙ) (a partition) evaluated on a diagonal matrix diag(x₁,...,xₙ) is the **Schur polynomial** s_λ(x₁,...,xₙ):

```
s_λ(x₁,...,xₙ) = χ_λ(diag(x₁,...,xₙ))
               = Σ_{T standard Young tableau of shape λ} x^{content(T)}

These form a basis for the ring of symmetric polynomials Λ.

Hall inner product: ⟨s_λ, s_μ⟩ = δ_{λμ}  (Schur polynomials are orthonormal)

Littlewood-Richardson rule: s_λ · s_μ = Σ_ν c^ν_{λμ} s_ν
  c^ν_{λμ} = Littlewood-Richardson coefficient
            = number of LR tableaux of shape ν/λ with content μ.

This is exactly the decomposition rule for tensor products of GL(n) representations:
  V_λ ⊗ V_μ = ⊕_ν (c^ν_{λμ}) V_ν

The RSK correspondence establishes the bridge: permutation → Young tableau pair →
Schur polynomial expansion. This connects Sₙ-representation theory (Young diagrams),
GL(n)-representation theory (highest weights = partitions), and combinatorics (symmetric
functions), all in one framework.
```

### Schur-Weyl Duality

```
Consider V = ℂⁿ (fundamental SL(n)-module).
On V^⊗k, two groups act: GL(n,ℂ) acts diagonally, Sₖ permutes tensor factors.
These actions are centralizers of each other (Schur-Weyl duality):

V^⊗k = ⊕_λ V_λ^{GL(n)} ⊗ V_λ^{S_k}

The sum is over partitions λ of k with at most n rows.
This connects GL(n) representation theory (Schur functors) with Sₙ theory (Young tableaux).
```

---

## 9. Representations in Physics

### Noether's Theorem (Group Theory Version)

```
For every continuous symmetry (Lie group action) of a physical system,
there is a conserved quantity.

U(1) symmetry (phase rotation ψ → e^{iα}ψ):  → conservation of electric charge
SO(3) rotational symmetry:                    → conservation of angular momentum
Translation symmetry (ℝ³):                    → conservation of momentum
Time translation symmetry:                    → conservation of energy
Lorentz symmetry:                            → Lorentz invariance of relativistic energy-momentum

The conserved quantity is the Noether charge associated to the Lie algebra generator.
```

### The Standard Model Gauge Group

```
G_SM = SU(3)_C × SU(2)_L × U(1)_Y

SU(3)_C: color charge of QCD (gluons in 8-rep, quarks in 3-rep)
SU(2)_L: weak isospin (W±, Z bosons; left-handed fermions in doublets)
U(1)_Y:  hypercharge (B boson)

After electroweak symmetry breaking (Higgs mechanism):
  SU(2)_L × U(1)_Y → U(1)_EM  (photon = linear combo of W³ and B)

Fermion multiplets transform under specific representations:
  Left-handed quarks: (3, 2, 1/6) [triplet under SU(3), doublet under SU(2)]
  Right-handed up quark: (3, 1, 2/3)
  Leptons (e,ν): (1, 2, -1/2) left-handed doublet, (1,1,-1) right-handed singlet

All particle content and interactions are encoded in representation theory of G_SM.
```

### Lorentz Group and Spinors

```
Lorentz group: SO(3,1) = {Λ ∈ M(4,ℝ) : Λ'gΛ=g} where g=diag(1,-1,-1,-1).
  Not compact. Irreps labeled by (j₁,j₂) with j₁,j₂ ∈ {0,1/2,1,...}.

Complexified Lorentz: SO(3,1,ℂ) ≅ SL(2,ℂ)×SL(2,ℂ)/ℤ₂.

Key representations:
  (0,0): scalar field
  (1/2,0): left-handed Weyl spinor (2-component) — quarks, neutrinos
  (0,1/2): right-handed Weyl spinor (2-component)
  (1/2,0)⊕(0,1/2): Dirac spinor (4-component) — electrons
  (1/2,1/2): 4-vector Aμ (photon)
  (1,0)⊕(0,1): antisymmetric 2-tensor Fμν (field strength)

Dirac equation: (iγμ∂μ - m)ψ = 0
  γμ are 4×4 matrices satisfying {γμ,γν} = 2gμν (Clifford algebra).
  ψ is a Dirac spinor transforming in the (1/2,0)⊕(0,1/2) representation.
```

---

## 10. Equivariant Neural Networks and Geometric Deep Learning

### Equivariance: The Core Idea

A function f: X → Y between spaces with G-actions is **G-equivariant** if:
```
f(g · x) = g · f(x)  for all g ∈ G, x ∈ X.

G-invariant: f(g · x) = f(x)  [special case where G acts trivially on Y].

Examples:
  Translation equivariant: f(x + t) = f(x) + t  [CNNs are translation equivariant]
  Rotation equivariant: f(Rx) = R f(x)  [SE(3)-equivariant networks]
  Permutation equivariant: f(σ·x) = σ·f(x)  [set networks, graph networks]
```

**Why equivariance matters**: If the task has a symmetry group G (e.g., rotating a molecule doesn't change its energy), then the network should be G-equivariant. A non-equivariant network must learn the same function for all G-transforms of the input from data — requiring exponentially more samples. An equivariant architecture bakes in the symmetry for free.

### Schur's Lemma Constrains the Architecture

This is the key connection between representation theory and network architecture. Let V and W be G-representations (spaces on which G acts via irreps). The equivariant linear maps V → W are exactly the intertwiners:

```
Linear maps T: V → W satisfying T ∘ ρ_V(g) = ρ_W(g) ∘ T  for all g ∈ G.

By Schur's lemma:
  If V = ⊕_i m_i V_i and W = ⊕_j n_j V_j  (isotypic decompositions):

  The space of equivariant maps is isomorphic to:
    ⊕_i Hom(ℂ^{m_i}, ℂ^{n_i}) ⊗ I_{dim V_i}

  i.e., one matrix per irrep type, multiplied by the identity on the irrep space.
  Weight sharing across the irrep dimensions is enforced by Schur's lemma.
```

**Practical consequence for network design**: An equivariant linear layer between feature spaces V and W is parameterized by a block-diagonal matrix — one block per irrep type that appears in both V and W. The architecture is not arbitrary; Schur's lemma dictates the allowed weight structure. This reduces parameter count and guarantees exact equivariance.

### G-CNNs (Group Convolutional Networks)

Cohen & Welling (2016) generalized CNNs to arbitrary compact groups. The construction uses the Peter-Weyl theorem:

```
Standard CNN: features are functions on ℝ² (or ℤ²).
  Convolution: (f * k)(x) = ∫ f(y) k(x-y) dy
  Translation equivariant by construction.

G-CNN: features are functions on a group G (or homogeneous space G/H).
  Group convolution: (f * k)(g) = ∫_G f(h) k(g⁻¹h) dh
  G-equivariant by construction.

Steerable CNNs: features are sections of G-equivariant vector bundles.
  Feature at each location x carries a representation of the stabilizer subgroup H_x.
  Convolutional kernel k: ℝ² → Hom(V_in, V_out) is constrained to be H-equivariant.

Irrep decomposition of feature spaces:
  Features are expanded in irreps of G.
  For G = SO(2) on ℝ²: irreps are e^{inθ} (angular frequency n = 0, ±1, ±2, ...).
  For G = SO(3): irreps are spherical harmonics Y_l^m.
  Equivariant convolution in frequency domain = multiplication by learnable coefficients
  per irrep type (exactly the Schur's lemma block-diagonal structure).
```

### SE(3)-Equivariant Networks for 3D Molecular Modeling

The group SE(3) = ℝ³ ⋊ SO(3) (rigid body motions: translations + rotations) is the symmetry group of 3D molecular geometry. A molecule's energy, forces, and properties must be rotation-invariant (scalar) or rotation-equivariant (vector/tensor).

```
SO(3) irreps: spherical harmonics Y_l^m, indexed by l = 0, 1, 2, ...
  l=0: scalars (invariant)
  l=1: vectors (equivariant under rotations as 3-vectors)
  l=2: rank-2 tensors (quadrupole moments)
  general l: rank-l tensors / "type-l features"

Clebsch-Gordan product (tensor product decomposition):
  V_l₁ ⊗ V_l₂ = ⊕_{l=|l₁-l₂|}^{l₁+l₂} V_l
  This is the same Clebsch-Gordan formula as for SU(2) angular momentum addition.
  Product of two SO(3) features combines irreps by angular momentum addition rules.

Architecture (Tensor Field Networks, SE(3)-Transformers, NequIP, MACE):
  1. Embed atoms as type-0 features (scalars: element, charge, ...).
  2. For each edge (atom pair): compute spherical harmonics Y_l(r_ij/|r_ij|) of direction.
  3. Equivariant message passing:
       h_i^{l} ← Σ_j  (learnable radial filter)(|r_ij|)  ⊗_{CG}  Y_l(r̂_ij) ⊗  h_j^{l'}
     where ⊗_{CG} means tensor product with Clebsch-Gordan decomposition.
  4. Output: type-0 features (energy = scalar), type-1 features (forces = vectors).

Key property: exact SE(3)-equivariance by construction → no data augmentation needed.
  A rotated molecule gives exactly the rotated output. This is not an approximation.
```

### Permutation-Equivariant Networks (Sets and Graphs)

For inputs that are sets {x₁,...,xₙ} (no canonical ordering), the relevant group is Sₙ:

```
Permutation equivariant: f({x_σ(1),...,x_σ(n)}) = {f_σ(1),...,f_σ(n)}
Permutation invariant:   f({x_σ(1),...,x_σ(n)}) = f({x₁,...,xₙ})  [scalar output]

Deep Sets (Zaheer et al.): The most general permutation-invariant function is:
  f({x₁,...,xₙ}) = ρ(Σ_i φ(xᵢ))  [encode each element, sum, decode]

Graph Neural Networks: graphs have node permutation symmetry (Sₙ) and edge permutation.
  Message passing: h_i^{(k+1)} = UPDATE(h_i^{(k)}, AGGREGATE({h_j^{(k)} : j~i}))
  AGGREGATE must be permutation-invariant over neighbors.

Sₙ-equivariant layers (higher-order): The space of Sₙ-equivariant linear maps
  (ℝⁿ)^⊗k → (ℝⁿ)^⊗k is spanned by permutation matrices → "tensor networks" for sets.
  Maron et al. (2019): characterized all invariant and equivariant layers for sets.
```

### Signal Processing on Non-Euclidean Domains

The Peter-Weyl theorem generalizes Fourier analysis to any compact group, and spectral graph theory does the same for graphs:

```
Classical Fourier (G = ℝ): irreps are e^{ikx}, Fourier modes indexed by frequency k.
  f(x) = ∫ f̂(k) e^{ikx} dk     [Fourier inversion]
  Convolution theorem: f * g → f̂ · ĝ  [pointwise in frequency domain]

Peter-Weyl (G compact): irreps ρ play the role of Fourier modes.
  f ∈ L²(G): f(g) = Σ_ρ (dim ρ) tr(f̂(ρ) ρ(g)*)
  Convolution on G: (f * h)(g) = ∫_G f(gh⁻¹) h(g) dg
  Fourier domain: (f * h)^(ρ) = f̂(ρ) ĥ(ρ)  [matrix product in each irrep block]

Spectral graph theory (discrete setting):
  Graph G = (V, E), Laplacian L = D - A  (degree matrix minus adjacency).
  L is symmetric positive semidefinite: L = UΛUᵀ  (eigendecomposition).
  Eigenvectors of L: graph Fourier modes  (analogous to e^{ikx} on ℝ).
  Graph Fourier transform: f̂ = Uᵀ f  (project onto eigenvector basis).
  Graph convolution: f * k → U (Uᵀf ⊙ Uᵀk)  [pointwise in spectral domain].

ChebNet / spectral GNNs: parameterize filter as polynomial in L:
  k_θ(L) = Σ_j θ_j T_j(L)  [Chebyshev polynomial of Laplacian]
  Efficient: O(|E|) computation per layer without full eigendecomposition.
  Connection: Chebyshev polynomials are the characters of SU(2) (Weyl formula above).
```

---

## 11. Harmonic Analysis on Groups

### Spherical Harmonics from SO(3) Reps

```
SO(3) acts on S² (unit sphere). L²(S²) decomposes under SO(3) action:
  L²(S²) = ⊕_{l=0}^∞ V_l
  V_l: irrep of SO(3) of dimension 2l+1.

Basis functions for V_l: spherical harmonics Y_l^m(θ,φ) for m = -l,...,l.
  Y_0^0 = 1/√(4π)  [constant function — trivial rep]
  Y_1^m: linear functions on S² [l=1 triplet]
  Y_2^m: quadratic [l=2 quintet]
  ...

Orthogonality: ∫_{S²} Y_l^m (Y_{l'}^{m'})* dΩ = δ_{ll'} δ_{mm'}
Completeness: f ∈ L²(S²) → f = Σ_{l,m} a_l^m Y_l^m

This is exactly the Peter-Weyl theorem for G = SO(3).
Hydrogen atom: eigenstates labeled (n,l,m) where l and m are SO(3) rep labels.
```

### Fourier Transform as Representation Theory

**Abelian groups**: The irreps of ℝⁿ are one-dimensional: ρ_k(x) = e^{ik·x} for k ∈ ℝⁿ.

```
Peter-Weyl for ℝ:
  f(x) = (1/2π) ∫ f̂(k) e^{ikx} dk

This IS the Fourier transform — Plancherel formula for the non-compact group ℝ.

Pontryagin duality: For locally compact abelian G:
  Ĝ = group of characters (irreps) of G.
  ℝ̂ ≅ ℝ  (Fourier self-dual)
  ẑⁿ ≅ (ℤ/nℤ) ↔ DFT
  T̂ = S¹ hat = ℤ ↔ Fourier series
```

---

## Decision Cheat Sheet

```
Question:                                    Tool:
────────────────────────────────────────     ──────────────────────────────────────────
Decompose V into irreps                      Character inner product: mᵢ = ⟨χ_V, χᵢ⟩
Check if representation is irreducible       ⟨χ,χ⟩ = 1 iff irreducible
Find all irreps of finite group G            Build character table (rows=irreps, cols=classes)
Representations of SU(2)                     Half-integer j ∈ {0,½,1,...}, dim=2j+1
Angular momentum addition (QM)              Clebsch-Gordan decomposition: V_j ⊗ V_k
Particle content from gauge group           Find irreps of G_SM containing those quantum numbers
Symmetry → conservation law                 Noether's theorem + Lie algebra generator
Spherical harmonics                         L²(S²) = ⊕_l V_l (SO(3) representation)
Fourier transform                           Irreps of ℝ (Pontryagin duality)
Non-abelian Fourier analysis on G           Peter-Weyl theorem
Classify irreps of semisimple Lie group     Highest weight classification
Dimension of irrep                          Weyl dimension formula
Spinors vs tensors                          (½,0)⊕(0,½) vs (½,½) Lorentz reps
Build a G-equivariant network layer        Parameterize weights as intertwiners (Schur's lemma)
G-equivariant filter bank                   Decompose L²(G) into irreps (Peter-Weyl)
SE(3)-equivariant 3D network               SO(3) irreps (spherical harmonics) + CG products
Permutation-invariant network (sets)        Deep Sets: ρ∘Σ∘φ architecture
Spectral convolution on graph              Graph Laplacian eigenvectors as Fourier modes
Equivariant map between irrep spaces        Schur's lemma: must be 0 or scalar × identity
GL(n) rep tensor product coefficients       Littlewood-Richardson rule (Schur polynomials)
```

---

## Common Confusion Points

**SO(3) vs SU(2)**: SU(2) is the double cover of SO(3). They have the same Lie algebra. Integer-spin representations of SU(2) descend to SO(3); half-integer-spin (spinors) representations do NOT — they pick up a sign under 2π rotation. Electrons transform under SU(2), not SO(3).

**Lie group vs Lie algebra representations**: For simply connected G (e.g., SU(2), SU(n), Sp(2n)), there is a bijection between reps of G and reps of 𝔤. For non-simply connected G (e.g., SO(3)), some Lie algebra reps don't integrate to group reps (spinors).

**Character table uniquely determines group... sometimes**: Groups with the same character table are called "Galoisian conjugate" groups but may be non-isomorphic (e.g., D₄ and Q₈ have the same character table). Characters don't distinguish extensions.

**Representation ≠ just matrices**: A representation is an action — it can be on an infinite-dimensional space (e.g., L²(G)) or on abstract objects. The matrix representation comes only after choosing a basis for V.

**Compact vs non-compact Lie groups**: Compact groups (U(n), SU(n), SO(n)) have unitary finite-dimensional irreps. Non-compact groups (SL(2,ℝ), Lorentz group) have no faithful unitary finite-dimensional reps — their unitary reps are infinite-dimensional (principal series, complementary series). This is why Lorentz reps are tricky.

**Root systems classify semisimple Lie algebras**: The ADE classification connects Lie algebras, surface singularities (Du Val singularities), and the McKay correspondence. Finite subgroups Γ ≤ SL(2,ℂ) correspond bijectively to ADE Dynkin diagrams — the McKay graph of Γ (nodes = irreps of Γ, edges from the natural 2D representation ρ₂: connect V_i to V_j iff V_j ⊆ V_i ⊗ ρ₂) is the extended Dynkin diagram of the corresponding ADE Lie algebra. The McKay correspondence unifies: (1) finite group representation theory (irreps of Γ), (2) algebraic geometry (resolution of the quotient singularity ℂ²/Γ — the exceptional divisors correspond to nodes of the Dynkin diagram), and (3) Lie algebra classification. This unexpected unity is one of the deepest results connecting algebra, geometry, and combinatorics.

**Quark color vs quark flavor**: SU(3)_color (gauge symmetry of QCD) vs SU(3)_flavor (approximate global symmetry of up/down/strange quarks — broken by mass differences). Both are SU(3) but very different physics. Gell-Mann's eightfold way used flavor SU(3); the actual forces are color SU(3).

**Equivariance vs invariance in ML**: An equivariant function transforms its output coherently with the input transformation (forces = vectors, equivariant). An invariant function ignores the transformation (energy = scalar, invariant). Invariant = equivariant to the trivial representation. Most geometric deep learning papers want equivariant intermediate features and invariant final output (energy prediction).

**Schur polynomials are characters, not just symmetric functions**: s_λ(x₁,...,xₙ) is the character of the GL(n) irrep with highest weight λ evaluated at the diagonal matrix. The Littlewood-Richardson coefficients c^ν_{λμ} are both tensor product multiplicities (rep theory) and structure constants of the symmetric function ring (combinatorics) — this double interpretation is the content of Schur-Weyl duality.
