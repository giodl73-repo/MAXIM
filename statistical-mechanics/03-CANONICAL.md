# Canonical Ensemble

## The Big Picture

The canonical ensemble describes a system at fixed temperature T — in thermal contact with
a large heat reservoir. Unlike the microcanonical ensemble (fixed E), energy fluctuates and
the system samples all energy levels with probability e^{-βE}/Z. The partition function Z
encodes all thermodynamic information: take a log, differentiate, and any quantity you want
falls out. The Helmholtz free energy F = -kT ln Z is the master potential for systems at
fixed T and V.

```
CANONICAL ENSEMBLE — MASTER STRUCTURE
═══════════════════════════════════════════════════════════════════════════════

  SYSTEM at fixed (N, V, T):
  Energy can fluctuate; T fixed by heat reservoir

  ┌──────────────────────────────────┐     ┌──────────────────────────────┐
  │         SYSTEM                   │◄────►│     HEAT RESERVOIR at T     │
  │    (small; we care about this)   │     │  (huge; β = 1/kT is fixed)   │
  └──────────────────────────────────┘     └──────────────────────────────┘

  PARTITION FUNCTION:   Z(β, N, V) = Σ_n e^{-β E_n}
                                    (sum over all quantum states)

  PROBABILITY of microstate n:   P_n = e^{-βE_n} / Z

  ┌──────────────────────────────────────────────────────────────────────┐
  │  ALL THERMODYNAMICS FROM Z:                                          │
  │                                                                      │
  │  F = −k_BT ln Z              (Helmholtz free energy)                 │
  │  U = −∂(ln Z)/∂β = ⟨E⟩      (internal energy = ⟨H⟩)                  │
  │  S = −∂F/∂T = k_B(ln Z + βU) (entropy)                               │
  │  P = −∂F/∂V = k_BT ∂(ln Z)/∂V (pressure)                             │
  │  C_V = ∂U/∂T = k_Bβ² ∂²(ln Z)/∂β² (heat capacity)                  │
  │  μ = ∂F/∂N                   (chemical potential)                    │
  │                                                                      │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Deriving the Canonical Distribution

**Setup**: Total system = (small system S) + (reservoir R). Total energy E_total is fixed; energy of S can fluctuate.

When system S is in microstate n with energy E_n, the reservoir has energy E_R = E_total − E_n. The number of reservoir microstates:

    Ω_R(E_total − E_n) = exp[S_R(E_total − E_n) / k_B]

Taylor expand S_R around E_total (since E_n << E_total for a large reservoir):

    S_R(E_total − E_n) = S_R(E_total) − (∂S_R/∂E_R) E_n + O(E_n²)
                       = S_R(E_total) − E_n/T + O(E_n²)

So:

    Ω_R(E_total − E_n) ∝ exp(−E_n / k_BT) = exp(−β E_n)

Since P_n ∝ Ω_R(E_total − E_n):

    P_n = e^{-β E_n} / Z     where Z = Σ_n e^{-β E_n}    **CANONICAL DISTRIBUTION**

**Key insight**: The Boltzmann factor e^{-βE_n} is a property of the RESERVOIR (through β = 1/kT). The system's details only enter through its energy levels E_n. The derivation requires only that E_n << E_total — the system can be anything.

---

## The Partition Function — Structure and Factorization

### General Form

    Z(β, N, V) = Σ_n e^{-β E_n}    (quantum: sum over energy eigenstates)
    Z = (1/h^{3N} N!) ∫ d³ᴺq d³ᴺp e^{-β H(q,p)}    (classical limit)

The classical formula has:
- 1/h^{3N}: converts phase space volume to a dimensionless count (Heisenberg cells)
- N!: indistinguishability of identical particles

### Factorization for Independent Subsystems

If the Hamiltonian separates: H = H_A + H_B (e.g., non-interacting particles), then:

    Z_total = Z_A × Z_B    (partition function multiplies)
    F_total = F_A + F_B    (free energy adds)

For N identical indistinguishable particles (classical):

    Z = z^N / N!    where z = single-particle partition function

```
FACTORIZATION EXAMPLE — IDEAL GAS:

  Single-particle z:
  z = (1/h³) ∫ d³r d³p e^{-β p²/2m}
    = (V/h³) × (2πmk_BT)^{3/2} = V / λ³

  where λ = h/√(2πmk_BT) is the THERMAL DE BROGLIE WAVELENGTH.

  N-particle Z:
  Z = z^N / N! = (V/λ³)^N / N!

  ln Z = N [ln(V/Nλ³) + 1]    (using Stirling)

  F = −k_BT ln Z = −Nk_BT [ln(V/Nλ³) + 1]

  P = −∂F/∂V = Nk_BT/V    ✓  (ideal gas law PV = NkT)
  U = −∂(ln Z)/∂β = (3/2)Nk_BT    ✓  (equipartition)
```

---

## Thermodynamics from Z — The Systematic Procedure

The free energy F = −k_BT ln Z is the master potential for fixed (N, V, T). All thermodynamic quantities are partial derivatives of F:

```
F(T, V, N) = −k_BT ln Z

dF = −S dT − P dV + μ dN    ← fundamental relation

  S = −(∂F/∂T)_{V,N}
  P = −(∂F/∂V)_{T,N}
  μ = +(∂F/∂N)_{T,V}

  Internal energy: U = F + TS = −∂(βF)/∂β = −∂(ln Z)/∂β = ⟨E⟩

  Heat capacity:   C_V = (∂U/∂T)_{V,N} = k_B β² (∂²ln Z/∂β²)
                       = k_B β² (⟨E²⟩ − ⟨E⟩²)
                       = ⟨(ΔE)²⟩ / k_BT²

  ENERGY FLUCTUATIONS = HEAT CAPACITY:
  ┌──────────────────────────────────────────────────────────┐
  │  Var(E) = k_BT² C_V                                      │
  │                                                          │
  │  Relative fluctuation: √Var(E)/⟨E⟩ ~ 1/√N → 0 for N→∞  │
  │  For large N, canonical ≡ microcanonical (sharp peak)    │
  └──────────────────────────────────────────────────────────┘
```

---

## Worked Example — Quantum Harmonic Oscillator

One quantum harmonic oscillator at temperature T. Energy levels: E_n = ℏω(n + 1/2), n = 0, 1, 2, ...

**Partition function**:

    z = Σ_{n=0}^∞ e^{-β ℏω(n+1/2)}
      = e^{-βℏω/2} / (1 − e^{-βℏω})
      = 1 / (2 sinh(βℏω/2))

**Average energy**:

    U = −∂(ln z)/∂β = (ℏω/2) + ℏω / (e^{βℏω} − 1) = ℏω(⟨n⟩ + 1/2)

where ⟨n⟩ = 1/(e^{βℏω}−1) is the Bose-Einstein mean occupation of the oscillator mode.

```
LIMITS:
  High T (k_BT >> ℏω):
  ⟨n⟩ ≈ k_BT/ℏω  ⟹  U ≈ k_BT  (equipartition)
  C_V → k_B

  Low T (k_BT << ℏω):
  U ≈ ℏω/2 + ℏω e^{-βℏω}   (zero-point energy + exponentially frozen)
  C_V ≈ k_B (βℏω)² e^{-βℏω} → 0 (quantum freeze-out)

  Crossover at T* = ℏω/k_B (characteristic temperature of oscillator)
```

**Einstein model of a solid**: 3N oscillators all at frequency ω_E.

    C_V = 3Nk_B (ℏω_E/k_BT)² e^{ℏω_E/k_BT} / (e^{ℏω_E/k_BT} − 1)²

Matches Dulong-Petit (3Nk_B) at high T; goes exponentially to zero at low T.

---

## Two-State System — Schottky Anomaly

System with two states: energy 0 and ε. Simplest non-trivial canonical calculation.

    Z = 1 + e^{-βε}
    U = ε / (1 + e^{βε})
    C_V = k_B (βε)² e^{βε} / (1 + e^{βε})²

```
SCHOTTKY PEAK:
  C_V peaks at T* ≈ 0.42 ε/k_B.

  High T: both states equally likely → C_V → 0 (no energy gradient)
  Low T: only ground state → C_V → 0 (no thermal excitation)
  At T*: maximum contrast between populations → maximum heat capacity

  Appears in: magnetic impurities, tunneling systems in glasses,
  nuclear spins, any two-level system.
  Fingerprint: C_V ~ T^{-2} e^{-ε/kT} at low T.
```

---

## Grand Canonical Ensemble

When the system exchanges both energy and particles with a reservoir, use the grand canonical ensemble. Fix chemical potential μ and temperature T; particle number N fluctuates.

**Grand partition function**:

    Z_G(β, μ, V) = Σ_{N=0}^∞ e^{βμN} Z_N(β, V)
                 = Σ_{N,n} e^{-β(E_n(N) − μN)}

**Grand potential** Ω_G (Landau potential):

    Ω_G = −k_BT ln Z_G

    dΩ_G = −S dT − P dV − ⟨N⟩ dμ

    S = −∂Ω_G/∂T,    P = −∂Ω_G/∂V,    ⟨N⟩ = −∂Ω_G/∂μ

```
GRAND CANONICAL — WHEN TO USE:
  - Quantum gases (fermions/bosons): each mode has variable occupation
  - Open systems exchanging particles with environment
  - Chemical reactions: μ controls species concentrations
  - Adsorption: μ of gas controls surface occupancy
  - Semiconductors: Fermi level μ controls carrier density

  KEY: For ideal quantum gases, each momentum mode is independent,
  and Z_G factorizes over modes:
  Z_G = Π_k z_k^{grand}
  where z_k depends on whether mode k holds 0, 1, 2, ... particles.
  → Fermi-Dirac (at most 1) or Bose-Einstein (any N) distributions.
  (Details in 04-QUANTUM-STATS.md)
```

---

## The Legendre Transform Connection

The canonical ensemble arises from the microcanonical by a Legendre transform — the same mathematical structure that maps Lagrangian to Hamiltonian (see variational-calculus/05-HAMILTONIAN-MECHANICS.md).

```
ENSEMBLE ↔ LEGENDRE TRANSFORM:

  MICROCANONICAL: S(E, V, N) — entropy as function of energy
  ┌──────────────────────────────────────────────────────┐
  │  Legendre transform S → T:  F = E − TS               │
  │  (or equivalently: β = 1/kT = ∂S/∂E, F = −kT ln Z)   │
  └──────────────────────────────────────────────────────┘

  CANONICAL → GRAND CANONICAL:
  ┌──────────────────────────────────────────────────────┐
  │  Legendre transform N → μ:  Ω = F − μN = −kT ln Z_G  │
  └──────────────────────────────────────────────────────┘

  THERMODYNAMIC POTENTIALS — full structure:

  U(S,V,N)               fundamental relation
  F(T,V,N) = U − TS      Helmholtz (canonical ensemble)
  H(S,P,N) = U + PV      Enthalpy (fixed pressure processes)
  G(T,P,N) = U−TS+PV     Gibbs (chemistry at fixed T, P)
  Ω(T,V,μ) = F − μN      Grand potential (open systems)
```

---

## Decision Cheat Sheet

| Need to... | Formula |
|-----------|--------|
| Partition function (quantum) | Z = Σ_n e^{-βE_n} |
| Partition function (classical, N particles) | Z = (h^{3N} N!)^{-1} ∫d³ᴺqd³ᴺp e^{-βH} |
| Helmholtz free energy | F = −k_BT ln Z |
| Internal energy | U = −∂(ln Z)/∂β |
| Entropy | S = −∂F/∂T = k_B(ln Z + βU) |
| Pressure | P = −∂F/∂V |
| Heat capacity | C_V = k_Bβ²(⟨E²⟩ − ⟨E⟩²) |
| Chemical potential | μ = ∂F/∂N |
| Grand partition function | Z_G = Σ_{N,n} e^{-β(E_n − μN)} |
| Grand potential | Ω_G = −k_BT ln Z_G |
| Single-particle ideal gas | z = V/λ³, λ = h/√(2πmkT) |
| N indistinguishable (classical) | Z = z^N/N! |
| Quantum harmonic oscillator | z = 1/(2 sinh(βℏω/2)) |

---

## Common Confusion Points

**F = −kT ln Z is Helmholtz, not Gibbs**: Helmholtz F(T,V,N) is minimized at fixed T, V. Gibbs G(T,P,N) = F + PV is minimized at fixed T, P — more natural for chemistry (constant pressure reactions). Z at fixed (N,V,T) gives F. The Gibbs partition function sums over volumes.

**The canonical ensemble sums over ALL energy levels**: Every microstate contributes to Z, even those far from equilibrium. The Boltzmann factor e^{-βE} suppresses high-energy states, but they're in the sum. The energy distribution P(E) = g(E)e^{-βE}/Z peaks sharply at ⟨E⟩ for large N — but this sharpness is a result, not an input.

**Factorization Z = z^N/N! fails for interacting systems**: Once particles interact (Σᵢⱼ V(rᵢ−rⱼ)), Z does not factorize. Computing Z for interacting systems requires virial expansions, cluster expansions, mean-field theory, or numerical methods. Most of statistical mechanics is the study of this difficulty.

**μ = 0 for photons and phonons**: When particle number is not conserved (photons can be emitted/absorbed freely, phonons created/destroyed), the free energy minimization ∂F/∂N = μ = 0 has no constraint on ⟨N⟩. There is no Lagrange multiplier for particle number, so the Bose-Einstein distribution becomes n(ε) = 1/(e^{βε}−1) with μ = 0. This is why the Planck blackbody distribution has no chemical potential. For conserved bosons (⁴He, cold atoms), μ is real and negative, approaching zero at the BEC critical temperature. Details in 04-QUANTUM-STATS.md.

**The Legendre transform as Fenchel conjugate**: The transform S(E) → F(T) via F = E − TS is exactly the convex conjugate (Fenchel-Legendre dual): F(β)/k_B = sup_E[βE − S(E)/k_B]. The dual variable β = ∂S/∂E is the gradient at the supremum. This is the same duality that appears in convex optimization (e.g., the dual of a linear program, or the conjugate function in Fenchel duality), which is why the canonical and microcanonical descriptions carry equivalent information — they are Legendre duals.

**"Fixed T" requires the system to be small compared to the reservoir**: The derivation of the canonical distribution relies on E_n << E_reservoir. If system and reservoir are comparable in size, neither is canonical. For macroscopic systems, the canonical and microcanonical ensembles give identical macroscopic predictions anyway.
