# Renormalization Group

## The Big Picture

Near a critical point, the correlation length ξ diverges — the system has structure on all
length scales simultaneously. Ordinary perturbation theory in a small parameter breaks down.
The renormalization group (RG), developed by Wilson (1971), handles this by asking: how does
the system look when viewed at progressively longer length scales? The answer is a flow in the
space of coupling constants. Fixed points of this flow correspond to scale-invariant systems
(critical points). The RG explains universality: different microscopic systems flow to the
same fixed point and therefore have the same critical exponents.

```
RENORMALIZATION GROUP — CONCEPTUAL FLOW
═══════════════════════════════════════════════════════════════════════════════

  COUPLING CONSTANT SPACE (J, h, r, u, ...):

  Many different microscopic Hamiltonians H(s; J, h, r, u)
  describing the same physics at different length scales.

  COARSE-GRAINING (block spin):
  Integrate out short-distance degrees of freedom.
  Replace block of spins by single effective spin.
  This maps H → H' (same form, different couplings).

  RG TRANSFORMATION:  (J, h, ...) → (J', h', ...)
                                    ↓
  FIXED POINT:  H* maps to itself.  J*' = J*,  h*' = h*.
  Critical point IS the fixed point.
                                    ↓
  LINEARIZE around fixed point:  eigenvalues → critical exponents.

  UNIVERSALITY:  Many different starting Hamiltonians flow to the SAME
  fixed point H* → same critical exponents.
```

---

## Coarse-Graining and Block Spins

**Kadanoff block spins** (1966): The intuition behind RG.

Partition the lattice into blocks of size b^d (b = 2 in d dimensions). Replace each block by a single effective spin. This is a coarse-graining transformation.

```
1D BLOCK SPIN EXAMPLE (b=2):

  Original lattice:  s₁ s₂ | s₃ s₄ | s₅ s₆ | s₇ s₈

  Majority rule: S_I = sign(s_{2I-1} + s_{2I})

  New lattice:       S₁ | S₂ | S₃ | S₄     (half as many spins)

  New lattice spacing: a' = 2a
  New temperature coupling:  T' = f(T)
  At T_c: T_c' = T_c  (fixed point — critical temperature maps to itself)

  KEY INSIGHT (Kadanoff):
  If ξ >> a (near T_c), the system looks the same after coarse-graining.
  The block spins should behave just like the original spins, but with
  a rescaled lattice spacing.
```

**The formal RG step** in Wilson's formulation:

1. **Integrate** out Fourier modes with k ∈ [Λ/b, Λ] (high-momentum modes, short distances)
2. **Rescale** lengths: r → r/b, so the lattice spacing returns to a
3. **Rescale** fields to maintain the normalization of the kinetic term

After one RG step: the effective action S'[φ] describes physics at scale ab, with renormalized couplings.

---

## RG Flow and Fixed Points

The RG transformation is a map on coupling constant space:

    g_i → R_b(g_i)

where {g_i} are all couplings in the Hamiltonian.

**Fixed point**: g_i* such that R_b(g_i*) = g_i*. At the fixed point, the system is self-similar at all length scales — it IS the critical point.

**Linearization around fixed point**:

    δg_i → Σ_j M_{ij} δg_j    where M_{ij} = ∂R_i/∂g_j|_{g*}

Eigenvalues λ_a of M are related to scaling dimensions y_a:

    λ_a = b^{y_a}

**Classification of operators**:

```
RG EIGENVALUE CLASSIFICATION:

  y_a > 0:  RELEVANT operator.
            Perturbation grows under RG (b > 1 → λ_a > 1).
            Drives system AWAY from critical point.
            Example: temperature deviation t = (T−T_c)/T_c
                     magnetic field h

  y_a < 0:  IRRELEVANT operator.
            Perturbation decays under RG.
            Does NOT affect critical exponents.
            Example: higher-order interactions (u|φ|⁶ in d>3)

  y_a = 0:  MARGINAL operator.
            Requires higher-order analysis (e.g., d=4 is marginal for Ising).
            Leads to logarithmic corrections.
```

---

## From Scaling to Critical Exponents

**Scaling hypothesis**: Near T_c, the free energy density is a homogeneous function.

    f(t, h) = b^{-d} f(b^{y_t} t, b^{y_h} h)

for any rescaling b. Choose b = |t|^{-1/y_t}:

    f(t, h) = |t|^{d/y_t} f(±1, h/|t|^{y_h/y_t})

This gives:
    C_V ~ |t|^{d/y_t − 2}     → α = 2 − d/y_t
    m ~ |t|^{(d − y_h)/y_t}   → β = (d − y_h)/y_t
    χ ~ |t|^{(2y_h − d)/y_t}  → γ = (2y_h − d)/y_t
    ξ ~ |t|^{-1/y_t}          → ν = 1/y_t

**All critical exponents from two RG eigenvalues**: y_t and y_h (the eigenvalues for temperature and field perturbations). This is why there are only two independent critical exponents (all others from scaling relations).

```
CONNECTING EXPONENTS:
  ν = 1/y_t,      η = 2 + d − 2y_h

  From these two: α = 2 − dν,  β = ν(d − 2 + η)/2,  γ = ν(2 − η),
                 δ = (d + 2 − η)/(d − 2 + η)

  THE SCALING RELATIONS ARE NOT EMPIRICAL — they are consequences of
  the RG structure. That a simple 2-dimensional fixed point controls
  the behavior of a 10²³-particle system is the deep result.
```

---

## Wilson's Epsilon Expansion

**Important caveat**: The ε-expansion is an asymptotic series with zero radius of convergence — like most perturbative expansions in QFT. Setting ε = 1 (d = 3) at one-loop gives ~15% accuracy for ν, but higher-order terms diverge factorially. Practical extraction of d = 3 exponents uses Borel resummation of the series to 5–7 loop order, or the conformal bootstrap method (which gives near-exact results without perturbation theory: ν = 0.6300(5) for 3D Ising from bootstrap, vs. 0.625 from one-loop ε-expansion). The conformal bootstrap is now the precision tool; the ε-expansion remains the conceptual framework.

For φ⁴ theory (the field theory of the Ising universality class):

    S[φ] = ∫ d^d r [(1/2)|∇φ|² + (r/2)φ² + (u/4!)φ⁴]

**Upper critical dimension**: d_c = 4 (for n=1 Ising). For d > 4, u is irrelevant and mean-field theory is exact. For d < 4, u is relevant and fluctuations change the exponents.

**Wilson-Fisher fixed point**: Work in d = 4 − ε dimensions and expand in ε.

At one-loop:

    β_u ≡ du/dl = −εu + (3/16π²) u² + O(u³, ε²)

Fixed point: u* = (16π²/3) ε + O(ε²)

Eigenvalues at the Wilson-Fisher fixed point:

    y_t = 2 − ε/3 + O(ε²)
    η = ε²/54 + O(ε³)

**Critical exponents to order ε**:

    ν = 1/2 + ε/12 + O(ε²)     (mean-field: 1/2)
    η = 0 + O(ε²)               (mean-field: 0)
    β = 1/2 − ε/6 + O(ε²)      (mean-field: 1/2)
    γ = 1 + ε/6 + O(ε²)        (mean-field: 1)

Setting ε = 1 (d = 3) gives reasonable approximations, though ε = 1 is not really small. Higher-order calculations and resummation methods improve accuracy.

---

## Universality Explained

```
WHY UNIVERSALITY?

  Consider two different ferromagnets:
  Model A: Ising on cubic lattice, J₁ (nearest-neighbor)
  Model B: Ising on FCC lattice, J₁, J₂ (next-nearest-neighbor)

  DIFFERENT microscopic Hamiltonians.
  SAME critical exponents.

  RG EXPLANATION:
  Both models flow under RG to the SAME fixed point H*.
  The difference (model A vs B) corresponds to different starting
  points in coupling-constant space — but different IRRELEVANT
  perturbations of the fixed point.
  Irrelevant perturbations vanish under RG → both models approach H*.
  Critical behavior = universal properties of H*.

  UNIVERSALITY CLASS = BASIN OF ATTRACTION of the fixed point.

  ┌─────────────────────────────────────────────────────────────────┐
  │  What determines the universality class:                        │
  │  1. Spatial dimension d                                         │
  │  2. Symmetry of the order parameter (Z₂, O(n), etc.)           │
  │  3. Range of interactions (short vs. long-range)                │
  │                                                                 │
  │  What does NOT matter:                                          │
  │  Lattice structure, nearest-neighbor vs. next-nearest,          │
  │  specific values of coupling constants, microscopic details     │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Real-Space RG — 1D Ising Exact

The exact RG for the 1D Ising model with no field illustrates the fixed point structure.

Hamiltonian: H = −K Σᵢ sᵢ sᵢ₊₁ (K = J/k_BT)

**Decimation** (integrate out even sites, keep odd sites):

    Z = Tr_all exp(K Σ sᵢ sᵢ₊₁) = Tr_odd [Π_I R(s_{2I-1}, s_{2I+1})]

where:

    R(s, s') = Σ_{σ=±1} e^{K(sσ + σs')} = 2 cosh(K(s+s'))

Rewrite R(s,s') = e^{K'ss' + const}:

    e^{K'} = cosh(2K)^{1/2}    ⟹    K' = (1/2)ln(cosh(2K))

```
1D ISING RG FLOW:

  K' = (1/2) ln cosh(2K)

  FIXED POINTS:
  K* = 0:     T = ∞ (trivial, disordered)    STABLE (attractive)
  K* = ∞:     T = 0 (ordered)                UNSTABLE (repulsive from both sides)

  For any 0 < K < ∞: K flows toward 0 under RG.
  → NO phase transition at finite T in 1D Ising. ✓

  K* = ∞ is a zero-temperature fixed point, not a physical critical point.
  In 1D, you need T = 0 to order — consistent with Peierls argument.
```

---

## Connection to Quantum Field Theory

The partition function of a d-dimensional classical statistical system at temperature T is formally identical to the path integral of a (d−1)-dimensional quantum field theory in imaginary time β = ℏ/k_BT.

```
STAT MECH ↔ QFT DICTIONARY:

  Classical stat mech (d dims)    Quantum field theory (d-1 dims)
  ─────────────────────────────────────────────────────────────────
  Partition function Z             Path integral Z = ∫Dφ e^{iS/ℏ}
  Temperature β = 1/kT            Imaginary time extent β = ℏ/kT
  Correlation length ξ             Inverse mass m ~ 1/ξ
  Critical point ξ → ∞             Massless field theory
  Universality class               Renormalizable QFT
  RG flow in coupling space        Running of coupling constants
  UV fixed point (high energy)     Same fixed point structure

  Wilson's RG, developed for critical phenomena in the 1970s,
  became the foundational tool for understanding renormalization
  in quantum field theory — regularizing divergences by identifying
  which operators are relevant, irrelevant, or marginal.
```

The Wilsonian view of QFT: the standard model of particle physics is an effective field theory, valid below some UV cutoff Λ. Relevant operators correspond to the finite number of renormalizable interactions (mass, kinetic term, couplings). Irrelevant operators are suppressed by powers of E/Λ — hence the standard model works so well without knowing the UV completion.

## Engineering Bridge: RG as Multiscale Coarse-Graining

```
RG CONCEPT                         CS / ML EQUIVALENT
──────────────────────────────────────────────────────────────────────────────
Block-spin transformation           CNN pooling layer
  integrate out fine-grained        → aggregate local features into
  degrees of freedom within block     coarser representation

Hierarchical coarse-graining        Wavelet transform / hierarchical clustering
  structure at every length scale   → multiresolution analysis of signals

Scale invariance at fixed point     "Edge of chaos" initialization
  correlations at all scales        → gradient signal neither vanishes nor
                                      explodes through depth

Relevant/irrelevant operators       Feature importance in deep networks
  relevant: survives coarsening     → features that persist through pooling
  irrelevant: washed out            → fine-grained noise discarded by layers

RG flow: many UV theories           Transfer learning
  → same IR fixed point             → different pretraining → same fine-tuned
                                      representation (universality)
```

A CNN with pooling layers is literally a block-spin RG: each convolutional layer integrates local features (fine-grained spins), and pooling coarsens the spatial resolution by a factor b. Features surviving to the deepest layers are the "relevant operators" of the network's effective theory. The mean-field theory of deep networks (Poole et al. 2016, Schoenholz et al. 2017) makes this precise: a randomly initialized deep network propagates inputs through a composition of nonlinear maps, and the input-input correlation function flows under an RG-like recursion. At the "critical" initialization (edge of chaos), the network is at a fixed point where correlations propagate without decay — exactly the condition for trainability.

---

## Decision Cheat Sheet

| Need to... | Approach |
|-----------|---------|
| Understand why universality holds | RG flow; different systems → same fixed point |
| Find critical exponents from RG | Linearize RG around fixed point; eigenvalues y_t, y_h → exponents |
| Check if mean-field is valid | Is d > d_c = 4 for Ising (n=1)? Then mean-field exact |
| Determine if perturbation is relevant | y_a > 0 → relevant; grows under coarse-graining |
| Epsilon expansion for Ising | d = 4−ε; Wilson-Fisher fixed point at u* ~ ε |
| 1D Ising: does it order at T > 0? | No — K flows to 0 under decimation RG |
| Relate stat mech to QFT | Z_stat = ∫Dφ e^{-S_E}; imaginary-time path integral |
| Scaling relation from y_t, y_h | ν = 1/y_t, η = 2+d−2y_h; all others follow |

---

## Common Confusion Points

**The RG group is not actually a group**: The RG transformation is a semi-group — it has composition (apply two RG steps = one bigger step) but no inverse (you can't undo coarse-graining). "Group" is a historical misnomer (Stueckelberg and Petermann 1953).

**Renormalization in QFT and stat mech RG are the same thing**: The divergences of Feynman diagrams in QFT arise because you integrate loop momenta up to Λ → ∞. Wilson's real-space RG and the diagrammatic β-function are two faces of the same idea: physics is independent of the arbitrary UV cutoff, so how must the couplings run to compensate?

**The epsilon expansion is asymptotic**: The series in ε is not convergent — it's an asymptotic expansion (like the perturbative expansion in QFT). Setting ε = 1 gives useful estimates, but the series technically diverges. Padé approximants and resummation techniques improve accuracy.

**Fixed point ≠ equilibrium**: In thermodynamics, equilibrium means the system has minimized free energy. A fixed point of the RG is NOT a thermodynamic equilibrium — it's a scale-invariant configuration in the space of Hamiltonians. A critical system at T = T_c is in thermodynamic equilibrium (at its free energy minimum for that T) AND at the RG fixed point.

**Stat mech RG vs. QFT beta function have opposite sign conventions**: In stat mech RG, coarse-graining goes from short to long distances (UV → IR). A "relevant" operator has y > 0 and grows under coarse-graining (coupling increases as you zoom out). In QFT, the beta function β(g) = dg/d ln μ describes how couplings run with energy scale μ (going from IR → UV). A coupling that is "relevant" in stat mech (grows as you zoom out) has a negative QFT beta function (coupling decreases with energy, asymptotic freedom). A coupling that is "irrelevant" in stat mech (shrinks as you zoom out) has a positive QFT beta function. QCD's asymptotic freedom (β < 0 in QFT, coupling weakens at high energy) is an "irrelevant" perturbation in the stat mech RG sense — it decays under coarse-graining toward the IR. This sign confusion is inevitable when reading across literatures; always check which direction the flow is defined.
