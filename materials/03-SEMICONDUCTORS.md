# Semiconductors — Devices from First Principles

> This fills the MIT 6.012 gap: device physics from band theory, not just circuit symbols.

---

## Big Picture

```
Band theory (02-BONDING-BANDS.md)
        │
        ▼
INTRINSIC SEMICONDUCTOR
(pure Si at room temperature: some e⁻ thermally excited across gap)
        │
        ├──── n-TYPE DOPING (donor atoms → extra electrons)
        └──── p-TYPE DOPING (acceptor atoms → extra holes)
                    │
                    ▼
             p-n JUNCTION
             (the fundamental device)
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
    DIODE       SOLAR CELL    LED/LASER
                    │
                    ▼
              TRANSISTORS
              (BJT, MOSFET)
                    │
                    ▼
              INTEGRATED CIRCUITS
```

---

## Intrinsic Semiconductors

**Carrier concentration at thermal equilibrium:**

Electrons excited from valence band to conduction band leave behind holes.

```
n = ∫_{E_C}^{∞} g_c(E) f(E) dE   (electrons in conduction band)
p = ∫_{-∞}^{E_V} g_v(E) [1-f(E)] dE   (holes in valence band)
```

For non-degenerate semiconductor (E_F far from band edges by > 3k_BT):

```
n = N_C exp[-(E_C - E_F)/k_BT]

p = N_V exp[-(E_F - E_V)/k_BT]

N_C = 2(2πm_n*k_BT/h²)^(3/2)   (effective density of states, conduction band)
N_V = 2(2πm_p*k_BT/h²)^(3/2)   (effective density of states, valence band)

m_n*, m_p* = effective masses (different from free electron mass m_e)
```

**Intrinsic carrier concentration:**
```
np = N_C N_V exp(-E_g/k_BT) = n_i²   (mass action law — holds always)

n_i = √(N_C N_V) exp(-E_g/2k_BT)

n_i for Si at 300K ≈ 1.5 × 10¹⁰ cm⁻³
(compared to Si atom density: 5 × 10²² cm⁻³ → one in 3 trillion atoms is ionized)
```

**Intrinsic Fermi level** (n = p for intrinsic):
```
E_Fi = (E_C + E_V)/2 + (k_BT/2) ln(N_V/N_C)
     ≈ midgap  (if m_n* ≈ m_p*)
```

Temperature dependence:
```
n_i ∝ T^(3/2) exp(-E_g/2k_BT)

At 300K:
Si: n_i = 1.5×10¹⁰ cm⁻³  (E_g = 1.12 eV)
Ge: n_i = 2.4×10¹³ cm⁻³  (E_g = 0.67 eV)  ← why Ge circuits fail above ~70°C
GaAs: n_i = 2×10⁶ cm⁻³  (E_g = 1.42 eV)
```

---

## Extrinsic Semiconductors — Doping

**n-type (donors):** Group V atom (P, As, Sb) in Si lattice. Extra electron weakly bound.

```
Donor ionization energy (hydrogen model):
E_d = m_n* e⁴ / (2(4πε₀ε_r ℏ)²) = (m_n*/m_e)(1/ε_r²) × 13.6 eV

For Si: m_n*/m_e ≈ 0.26, ε_r = 11.7
E_d ≈ 0.026 eV  (25 meV ≈ k_BT at room temperature → fully ionized at 300K!)
```

At room temperature, donors are fully ionized: n ≈ N_D (donor concentration).

```
n ≈ N_D   (if N_D >> n_i)
p = n_i² / N_D   (from mass action law)
E_F = E_C - k_BT ln(N_C/N_D)   (moves toward conduction band)
```

**p-type (acceptors):** Group III atom (B, Al, Ga) in Si. Missing electron = hole.
```
p ≈ N_A   (acceptor concentration)
n = n_i² / N_A
E_F = E_V + k_BT ln(N_V/N_A)   (moves toward valence band)
```

**Compensation:** both donors and acceptors present:
```
If N_D > N_A: n ≈ N_D - N_A, p = n_i²/(N_D - N_A)
If N_A > N_D: p ≈ N_A - N_D, n = n_i²/(N_A - N_D)
```

Typical doping levels: N_D, N_A = 10¹⁵–10²⁰ cm⁻³
(vs intrinsic Si: 1.5×10¹⁰ → doping increases majority carrier by 5–10 orders of magnitude)

---

## Drift and Diffusion

**Drift current** (field-driven):
```
J_n_drift = enμ_n E
J_p_drift = epμ_p E

μ_n = qτ_c/m_n*   (mobility = drift velocity per unit field)
μ_p = qτ_c/m_p*

Si at 300K: μ_n = 1400 cm²/V·s, μ_p = 470 cm²/V·s
```

Mobility limited by: lattice scattering (phonons, ∝ T^(-3/2)) + impurity scattering (∝ N^(-1)T^(3/2))

**Diffusion current** (gradient-driven):
```
J_n_diff = eD_n (dn/dx)   [electrons flow down concentration gradient]
J_p_diff = -eD_p (dp/dx)  [holes flow down concentration gradient]
```

**Einstein relation:**
```
D_n/μ_n = D_p/μ_p = k_BT/e   (thermal voltage V_T = 26 mV at 300K)
```

**Continuity equations:**
```
∂n/∂t = (1/e)∂J_n/∂x + G - R
∂p/∂t = -(1/e)∂J_p/∂x + G - R

G = generation rate, R = recombination rate
Minority carrier lifetime τ: R = Δn/τ for low-level injection
```

---

## p-n Junction

The core device. Connects two differently-doped regions.

**Built-in potential:**
```
V_bi = (k_BT/e) ln(N_A N_D / n_i²)

Typical values: Si with N_A = N_D = 10¹⁶ cm⁻³
V_bi = 0.026 × ln(10¹⁶ × 10¹⁶ / (1.5×10¹⁰)²) = 0.026 × ln(4.4×10¹¹) ≈ 0.69 V
```

**Depletion width** (solved from Poisson equation ∇²φ = -ρ/ε):
```
x_n = √(2ε_s V_bi N_A / (eN_D(N_A+N_D)))   [depletion into n-side]
x_p = √(2ε_s V_bi N_D / (eN_A(N_A+N_D)))   [depletion into p-side]

Total depletion width:
W = x_n + x_p = √(2ε_s V_bi (N_A + N_D)/(e N_A N_D))

Under bias V: replace V_bi → V_bi - V  (V > 0 is forward bias → W decreases)
```

**Capacitance:**
```
C_j = ε_s A / W   (depletion capacitance, like parallel plate with W separation)
C_j ∝ (V_bi - V)^(-1/2)   → 1/C_j² vs V is linear → gives V_bi, N_D from slope
```

**Junction I-V characteristic (Shockley diode equation):**
```
I = I_0 [exp(eV/nk_BT) - 1]

I_0 = eA(D_p p_{n0}/L_p + D_n n_{p0}/L_n)   (reverse saturation current)
n = ideality factor (1 for ideal, 2 for recombination-dominated)
L_p = √(D_p τ_p)   (minority carrier diffusion length)

p_{n0} = n_i²/N_D   (minority hole concentration on n-side at equilibrium)
n_{p0} = n_i²/N_A   (minority electron concentration on p-side at equilibrium)
```

Forward bias: exponential current increase (doubling every 60 mV for n=1).
Reverse bias: current saturates at -I_0 (very small).
Breakdown: Zener (tunneling, E_g < ~5 eV) or avalanche (impact ionization, high field).

---

## MOSFET — The 6.012 Gap

Metal-Oxide-Semiconductor Field-Effect Transistor. Controls current via electric field through oxide.

```
Gate (metal/poly-Si)
     ├────────────────┤
     │    SiO₂ oxide  │  (t_ox ~ 1-3 nm in modern CMOS)
     │                │
p-type body
┌────┬────────────────┬────┐
│ n⁺ │   p-channel    │ n⁺ │
│ S  │   (body)       │ D  │
└────┴────────────────┴────┘
     ↑
  depletion region + inversion layer
```

**Three regimes:**

**1. Accumulation (V_GS < 0 for NMOS):**
Holes attracted to surface. No inversion layer. No significant current.

**2. Depletion (0 < V_GS < V_th):**
Holes repelled, depletion region forms. Still insufficient electrons for conduction.

**3. Inversion (V_GS > V_th — ON state):**
Electron inversion layer forms at Si/SiO₂ interface. Current can flow from source to drain.

**Threshold voltage:**
```
V_th = V_FB + 2φ_F + Q_dep/C_ox

φ_F = (k_BT/e) ln(N_A/n_i)   (Fermi potential, ~0.35 V for N_A = 10¹⁷ cm⁻³)
Q_dep = -eN_A W_dep   (depletion charge)
C_ox = ε_ox/t_ox   (oxide capacitance per area)
V_FB = flat-band voltage (work function difference + oxide charge)
```

**MOSFET I-V characteristics (long-channel model):**
```
Linear region (V_DS < V_GS - V_th):
I_D = μ_n C_ox (W/L) [(V_GS - V_th)V_DS - V_DS²/2]

Saturation region (V_DS ≥ V_GS - V_th):
I_D = (μ_n C_ox W)/(2L) (V_GS - V_th)²

Transconductance: g_m = ∂I_D/∂V_GS = μ_n C_ox (W/L)(V_GS - V_th)  [linear]
                       = √(2μ_n C_ox W I_D / L)  [saturation]
```

**CMOS scaling (Moore's Law physics):**
Reduce L → more transistors/chip, higher switching speed (f_T ∝ 1/L²).
Scaling limits:
- Gate oxide leakage: t_ox < ~2 nm → tunneling → replaced SiO₂ with high-κ (HfO₂)
- Short-channel effects: V_th varies with L, drain-induced barrier lowering (DIBL)
- Power density: dynamic power P_dyn = αC_load V_DD² f → must reduce V_DD
- Subthreshold slope: kT ln(10)/e = 60 mV/decade at 300K → lower limit for V_th/V_DD

**FinFET/GAA:** 3D gate wraps around fin/nanowire → better electrostatic control at sub-10 nm.

---

## Bipolar Junction Transistor (NPN)

Three regions: emitter (n⁺), base (p, thin), collector (n).
Minority carrier injection + diffusion across thin base → current gain.

**Active mode** (forward-biased E-B, reverse-biased B-C):
```
I_C ≈ I_S exp(V_BE/V_T)   (V_T = k_BT/e = 26 mV)
I_B = I_C/β
I_E = I_C + I_B = I_C(1 + 1/β)

β = common-emitter current gain = D_n A_E n_{p0} L_B / (D_p A_B p_{n0} W_B)
  ~ 50–500 for discrete BJTs
```

Gain determined by minority carrier storage in base. Base width modulation (Early effect):
V_CE increases → collector depletion expands into base → W_B decreases → I_C increases slightly.

**BJT vs MOSFET:**
| | BJT | MOSFET |
|---|---|---|
| Control | V_BE (exponential) | V_GS - V_th (quadratic) |
| Input current | Yes (base current I_B) | No (gate is capacitor) |
| Speed | High f_T, but base charge storage | Very high at small L |
| Noise | Lower 1/f noise | Higher 1/f noise |
| Use today | RF/analog (HBT), power | Digital VLSI, most analog |

---

## Photovoltaics (Solar Cell)

p-n junction + light → generates electricity.

**Photogeneration:** photon absorbed (if E_photon > E_g) → creates e-h pair.
Excess minority carriers diffuse to junction → swept by built-in field → external current.

**Solar cell I-V under illumination:**
```
I = I_0[exp(eV/k_BT) - 1] - I_ph

I_ph = eA G (L_n + L_p + W)   (photocurrent, proportional to illumination)
```

**Short-circuit current:** V = 0 → I_sc = I_ph
**Open-circuit voltage:** I = 0:
```
V_oc = (k_BT/e) ln(I_sc/I_0 + 1) ≈ (k_BT/e) ln(I_sc/I_0)
```

**Fill factor and efficiency:**
```
FF = P_max / (I_sc × V_oc)   (FF ~ 0.7–0.85 for good cells)
η = P_max / P_incident = FF × I_sc × V_oc / P_in
```

**Shockley-Queisser limit:** thermodynamic maximum efficiency for single-junction:
~33.7% for band gap 1.1–1.4 eV. Si at 1.12 eV: theoretical ~29%.
Losses: photons with E < E_g not absorbed; excess energy thermalized; recombination.
Multijunction cells (GaInP/GaAs/Ge): capture more spectrum → ~46% under concentration.

---

## LEDs and Laser Diodes

**LED:** forward-biased p-n junction → minority carrier injection → radiative recombination.

Requires **direct bandgap** semiconductor (GaAs, InGaAs, GaN, InGaN):
In direct-gap: conduction band minimum and valence band maximum at same k-point.
Recombination conserves momentum → photon emitted directly.

Si is indirect-gap (minimum at k ≠ 0) → phonon needed → much lower radiative efficiency.

```
Photon energy: E_photon = E_g (+ thermal corrections) → λ = hc/E_g

GaAs: E_g = 1.42 eV → λ = 873 nm (near-IR)
InGaN (blue): E_g ≈ 2.7 eV → λ = 460 nm
AlGaInP (red): λ = 620–640 nm
```

**Laser diode:** adds optical cavity (cleaved facets) → stimulated emission.
Threshold: gain > loss. Lasing threshold current density:
```
J_th ∝ exp(E_g/k_BT)   → requires cooling or pulsed operation for high-power
```

Double heterostructure: sandwich thin active layer (GaAs) between larger-gap layers
(AlGaAs) → carrier and optical confinement simultaneously → efficient lasers.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why does Si dominate digital? | Stable native SiO₂, abundant, mature processing, 1.12 eV gap |
| Why GaN for power electronics? | 3.4 eV gap → high breakdown voltage; high thermal conductivity |
| Why GaAs for RF/analog? | High μ_n (8500 cm²/V·s vs Si's 1400), direct gap for optical |
| Why SiC for EV inverters? | Wide gap (3.2 eV), high thermal conductivity, mature processing |
| Why InGaN for LEDs? | Tunable direct gap, high efficiency in visible range |
| V_th formula components? | Work function difference + depletion charge + oxide charge |
| MOSFET vs BJT for logic? | MOSFET wins: no DC base current → lower power, easier to scale |

---

## Common Confusion Points

**1. The p-n junction built-in potential does NOT do work — it's not free energy.**
V_bi is an equilibrium potential. Connect a voltmeter → reads 0. You must apply external
bias to make current flow. The built-in field just maintains equilibrium by balancing
diffusion current.

**2. MOSFET threshold voltage is not fixed — it depends on V_SB.**
Body effect: if source is not at same potential as body, V_th increases.
In circuits: V_th = V_th0 + γ(√(2φ_F + V_SB) - √(2φ_F)).

**3. Long-channel MOSFET model breaks down below ~0.5 μm.**
Velocity saturation: carriers reach max velocity at high fields → I_D ∝ V_GS - V_th (not squared).
Short-channel effects: V_th roll-off, DIBL, punchthrough.

**4. Solar cell efficiency vs band gap is not monotonic.**
Too small E_g: absorb all photons but low V_oc. Too large E_g: high V_oc but miss most photons.
Sweet spot at ~1.1–1.4 eV (Si: 1.12, GaAs: 1.42) → Shockley-Queisser argument.

**5. Direct vs indirect bandgap is a k-space concept, not a real-space one.**
Si has an indirect gap because conduction band minimum is near X-point in BZ, not at Γ.
This means k(electron) ≠ k(photon) → momentum must come from phonon → lower probability.
