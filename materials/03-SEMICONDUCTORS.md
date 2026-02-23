# Semiconductors — From Carrier Statistics to Devices

## The Big Picture

```
    SEMICONDUCTOR LANDSCAPE
    ══════════════════════════════════════════════════════════

    PHYSICS                          DEVICES
    ┌──────────────────────┐        ┌────────────────────────┐
    │ Band structure E_g   │        │ p-n junction diode     │
    │ Carrier statistics   │───────▶│ Bipolar transistor     │
    │ Drift + diffusion    │        │ MOSFET (CMOS)          │
    │ Recombination        │        │ Solar cell (PV)        │
    │ Generation           │        │ LED / laser diode      │
    │ Doping (n/p type)    │        │ Photodetector          │
    └──────────────────────┘        └────────────────────────┘

    Connects:  band theory (02-BONDING-BANDS) → device operation
               materials choice (E_g, μ, n_i) → circuit performance
```

---

## Intrinsic Semiconductors

At T=0, valence band (VB) fully filled, conduction band (CB) empty.
At T>0, thermal excitation across the band gap creates electron-hole pairs.

### Effective Density of States

Near the CB minimum (parabolic approximation, effective mass m_e*):

$$N_c = 2\left(\frac{2\pi m_e^* kT}{h^2}\right)^{3/2}$$

Near the VB maximum (effective mass m_h*):

$$N_v = 2\left(\frac{2\pi m_h^* kT}{h^2}\right)^{3/2}$$

For Si at 300K: N_c = 2.8×10¹⁹ cm⁻³, N_v = 1.04×10¹⁹ cm⁻³

### Intrinsic Carrier Concentration

Equilibrium condition: n = p = n_i. Set Fermi level, apply Fermi-Dirac:

$$\boxed{n_i = \sqrt{N_c N_v} \cdot \exp\left(-\frac{E_g}{2kT}\right)}$$

```
    n_i values at 300K:
    Si   (E_g=1.12 eV): n_i = 1.5×10¹⁰ cm⁻³  ← crucial reference
    Ge   (E_g=0.67 eV): n_i = 2.4×10¹³ cm⁻³
    GaAs (E_g=1.43 eV): n_i = 2.0×10⁶  cm⁻³
    GaN  (E_g=3.4 eV):  n_i ≈ 10⁻¹⁰   cm⁻³  (negligible)
    4H-SiC (E_g=3.3 eV):n_i ≈ 10⁻⁸   cm⁻³

    Temperature dependence (from activation):
    d(ln n_i)/dT ≈ E_g/(2kT²)
    For Si: n_i doubles for every ~8°C near 300K
    → Devices designed for T < 150°C (Si), < 400°C (SiC)

    Mass action law (fundamental, holds even under bias):
    np = n_i²   (equilibrium)
```

Intrinsic Fermi level E_i (where n = p):

$$E_i = \frac{E_c + E_v}{2} + \frac{3kT}{4}\ln\frac{m_h^*}{m_e^*} \approx \text{midgap}$$

---

## Extrinsic Doping

### n-type: Donors

Group V atoms (P, As, Sb in Si) contribute one extra electron.
Donor level E_D lies slightly below E_c (shallow donor).

**Binding energy** (hydrogen atom analogy with screening and effective mass):

$$E_b = \frac{m_e^*}{m_0 \kappa^2} \times 13.6 \text{ eV}$$

For Si (m_e* = 0.26m₀, κ = 11.7): E_b = 0.026 eV ≈ kT at 300K → fully ionized.

With donor concentration N_D (assuming full ionization, N_D >> n_i):
- Majority carriers: n ≈ N_D
- Minority carriers: p = n_i²/N_D
- Fermi level: $E_F = E_i + kT \ln(N_D / n_i)$

```
    Example: N_D = 10¹⁶ cm⁻³ phosphorus in Si:
    n = 10¹⁶ cm⁻³
    p = (1.5×10¹⁰)²/10¹⁶ = 2.25×10⁴ cm⁻³ (12 orders below n!)
    E_F - E_i = 0.026 × ln(10¹⁶/1.5×10¹⁰) = 0.026 × 13.0 = 0.34 eV above midgap
```

### p-type: Acceptors

Group III atoms (B, Al, Ga in Si) accept one electron, leaving hole.
Acceptor level E_A lies slightly above E_v.

With acceptor N_A:
- Majority: p ≈ N_A
- Minority: n = n_i²/N_A
- Fermi level: $E_F = E_i - kT \ln(N_A / n_i)$

### Charge Neutrality and General Solution

Always: n + N_A⁻ = p + N_D⁺ (charge balance)

Complete ionization: $n + N_A = p + N_D$, combined with $np = n_i^2$:

$$n = \frac{N_D - N_A}{2} + \sqrt{\left(\frac{N_D - N_A}{2}\right)^2 + n_i^2}$$

```
    Four regimes:
    N_D >> N_A, N_D >> n_i: n ≈ N_D          (strong n-type)
    N_A >> N_D, N_A >> n_i: p ≈ N_A          (strong p-type)
    N_D ≈ N_A:              n ≈ n_i           (compensated)
    T high: n_i >> N_D, N_A: n ≈ n_i          (intrinsic regime)

    Conductivity:
    σ = e(nμ_e + pμ_h)
    n-type: σ ≈ eN_Dμ_e
    Si, N_D=10¹⁶: σ ≈ 1.6×10⁻¹⁹ × 10²² × 0.145 = 0.23 S/cm
    Resistivity ρ = 4.3 Ω·cm (typical n-Si)
```

---

## Carrier Transport

### Drift

Under electric field E: carrier drift velocity v_d = μE (for low fields).
Drift current density: J_drift = e(nμ_e + pμ_h)E = σE (Ohm's law).

At high fields, velocity saturates (optical phonon scattering):
$$v_{sat}(Si) \approx 10^7 \text{ cm/s}$$

Saturation velocity limits transistor speed: f_T ≈ v_sat/(2πL)

### Diffusion

Carrier gradient → diffusion current:
$$J_{diff,n} = eD_n \frac{dn}{dx}, \quad J_{diff,p} = -eD_p \frac{dp}{dx}$$

Einstein relation: $D = \mu kT/e$ (connects diffusion coefficient to mobility).

```
    For Si at 300K:
    D_n = μ_n × kT/e = 1450 × 0.026 = 37.7 cm²/s
    D_p = μ_p × kT/e = 450 × 0.026  = 11.7 cm²/s
```

Minority carrier diffusion length:
$$L = \sqrt{D\tau}$$
τ = minority carrier lifetime (recombination).
L_n in p-Si: if D_n = 25 cm²/s, τ = 1 μs → L_n = 50 μm.

---

## p-n Junction Physics

### Depletion Region

Electrons from n-side + holes from p-side recombine near junction → ionized dopants remain → space charge → electric field.

**Built-in potential** (from Fermi level alignment):
$$V_{bi} = \frac{kT}{e}\ln\frac{N_A N_D}{n_i^2}$$

For Si, N_A = N_D = 10¹⁶ cm⁻³:
V_bi = 0.026 × ln[(10¹⁶)²/(1.5×10¹⁰)²] = 0.026 × 26.0 = 0.72 V

**Depletion width** (abrupt junction, applied bias V):

$$\boxed{W = \sqrt{\frac{2\varepsilon_s(V_{bi} - V)}{e} \cdot \frac{N_A + N_D}{N_A N_D}}}$$

```
    Component widths:
    x_n = W · N_A/(N_A + N_D)  (into n-side)
    x_p = W · N_D/(N_A + N_D)  (into p-side)
    Electric field max at junction: E_max = 2(V_bi-V)/W = eN_D x_n/ε_s
    Charge: Q_dep = e N_D x_n A = e N_A x_p A (symmetric doping: equal)

    At V = 0 (Si, N_A = N_D = 10¹⁶):
    W = √(2 × 11.7 × 8.85×10⁻¹² × 0.72 / (1.6×10⁻¹⁹ × 10²²/2)) = 0.43 μm

    Forward bias V > 0: W shrinks, barrier lowers → exponential current
    Reverse bias V < 0: W grows, barrier higher → small reverse current
    Capacitance: C_j = ε_s A / W ∝ (V_bi - V)^(-1/2)
    → Varactor diode: voltage-tunable capacitor
```

### Shockley Ideal Diode Equation

$$\boxed{I = I_0\left(e^{qV/kT} - 1\right)}$$

Saturation current from minority carrier injection:
$$I_0 = Ae^2 n_i^2 \left(\frac{D_p}{L_p N_D} + \frac{D_n}{L_n N_A}\right)$$

Note: I_0 ∝ n_i² ∝ exp(-E_g/kT) — strongly temperature dependent.

```
    In practice: I = I_0(e^{qV/nkT} - 1), n = ideality factor
    n = 1: ideal diffusion current
    n = 2: generation-recombination in depletion region (low V)
    n = 1 to 2 depending on bias level

    Si diode at room temperature: I_0 ~ 10⁻¹² A (1 pA for 1 cm² area)
    At V = 0.6 V: I/I_0 = e^{0.6/0.026} ≈ 10^{10} → large current
    Forward voltage at given I decreases ~2 mV/°C (due to I_0 increase with T)

    Breakdown mechanisms:
    Zener: V_BR < 5V, tunneling across narrow depletion (heavily doped)
    Avalanche: V_BR > 7V, impact ionization cascade
    Breakdown voltage: V_BR ≈ ε_s E_crit²/(2eN) (lower N → higher V_BR)
    SiC: E_crit = 2.5 MV/cm vs Si: 0.3 MV/cm → SiC V_BR >> Si at same thickness
```

---

## Bipolar Junction Transistor (BJT)

NPN structure: n⁺-emitter / thin p-base / n-collector

**Active region** (V_BE > 0, V_BC < 0):

```
    Emitter injects electrons over forward-biased EB junction barrier
    Electrons diffuse across base (width W_B << L_n)
    Fraction α = e^(-W_B/L_n) reaches collector depletion region
    Rest recombine → base current I_B = recombination current

    I_C = α_T · I_E ≈ I_E (if W_B << L_n)
    I_B = (1-α_T)·I_E ≈ I_E·W_B/L_n  (if W_B << L_n)
    β = I_C/I_B = α_T/(1-α_T) ≈ L_n/W_B - 1

    Example: W_B = 0.1 μm, L_n = 10 μm → β ≈ 99 ≈ 100
    Practical β: 50-300 (depends on processing quality)

    Ebers-Moll model:
    I_C = I_S(e^{qV_BE/kT} - 1) - I_S/β_R·(e^{qV_BC/kT} - 1)
    I_S = saturation current (same physics as diode I_0)
    β_R = reverse β (much smaller, emitter not optimized for injection from base)

    Speed: f_T = g_m/(2πC_total), g_m = I_C/(kT/q)
    High f_T requires thin base W_B, low parasitics
    SiGe HBT: graded Ge in base → quasi-field accelerates electrons → f_T > 500 GHz
```

---

## MOSFET: The Foundation of Digital Electronics

### Structure

```
    Gate (metal or poly-Si)
         ↓
    ─────────────────────── ← gate oxide (SiO₂, t_ox ~ 1-5 nm)
    ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ← inversion layer (channel, ~1 nm thick)
    ● ● ● ● ● ● ● ● ● ● ← p-type body (N_A)
    ┌──┐              ┌──┐
    │n⁺│  source  drain │n⁺│
    └──┘              └──┘
    Isolation   ←L→   Isolation
     (STI)           (STI)

    Key dimensions (Intel Meteor Lake 2023):
    Gate length L ≈ 6-18 nm (depending on cell type)
    Gate oxide EOT ≈ 0.7 nm (equivalent SiO₂ thickness)
    Actual: HfO₂ (high-κ) with SiO₂ interfacial layer
```

### Threshold Voltage

$$V_T = V_{FB} + 2\phi_F + \frac{Q_{dep,max}}{C_{ox}}$$

$$\phi_F = \frac{kT}{q}\ln\frac{N_A}{n_i}, \quad C_{ox} = \frac{\varepsilon_{ox}}{t_{ox}}, \quad |Q_{dep,max}| = \sqrt{2\varepsilon_s q N_A \cdot 2\phi_F}$$

```
    V_FB = flat-band voltage: work function difference (φ_M - φ_Si) + oxide charge

    For p-Si, N_A = 10¹⁷ cm⁻³, t_ox = 3 nm (SiO₂, ε_ox = 3.9ε₀):
    φ_F = 0.026 ln(10¹⁷/1.5×10¹⁰) = 0.42 V
    C_ox = 3.9×8.85×10⁻¹²/(3×10⁻⁹) = 11.5 mF/m² = 11.5 fF/μm²
    Q_dep,max = √(2×11.7×8.85e-12×1.6e-19×10²³×0.84) = 1.65×10⁻² C/m²
    V_T = V_FB + 0.84 + 1.65e-2/11.5e-3 = V_FB + 0.84 + 1.43 V

    Body effect: increasing V_SB (reverse body-source bias) increases V_T
    ΔV_T = -(γ/2φ_F)(√(2φ_F + V_SB) - √(2φ_F))
    γ = √(2ε_s q N_A)/C_ox  (body-effect coefficient)
```

### I-V Characteristics

**Linear region** (V_DS < V_GS - V_T):
$$I_D = \mu_n C_{ox}\frac{W}{L}\left[(V_{GS}-V_T)V_{DS} - \frac{V_{DS}^2}{2}\right]$$

**Saturation** (V_DS ≥ V_GS - V_T, channel pinched off at drain):
$$\boxed{I_D = \frac{\mu_n C_{ox}}{2}\frac{W}{L}(V_{GS}-V_T)^2}$$

```
    Transconductance: g_m = ∂I_D/∂V_GS|_{V_DS sat} = μ_n C_ox (W/L)(V_GS-V_T)
    Output conductance (channel length modulation):
    I_D = I_D,sat(1 + λV_DS), λ = 1/V_A (Early voltage for MOSFET)

    Transit frequency: f_T = g_m/(2π(C_GS + C_GD))
    For minimum L MOSFET: f_T ≈ μ_n(V_GS-V_T)/(2πL²)
    Si NMOS: f_T ~ 100-500 GHz for L ~ 10 nm

    Sub-threshold current (V_GS < V_T, needed for leakage analysis):
    I_D = I_0 exp(q(V_GS-V_T)/nkT)(1 - e^{-qV_DS/kT})
    Subthreshold slope S = ln(10)·nkT/q = 60 mV/decade (n=1, 300K)
    Can't go below 60 mV/dec in conventional MOSFET (thermal limit)
    → Tunnel FETs, negative-C FETs proposed for steeper subthreshold

    Power: P_dynamic = α C V²_DD f  (switching power)
           P_static  = I_off V_DD   (leakage power)
    At 3nm node: P_static comparable to P_dynamic → major design challenge
```

---

## Solar Cells

### Photovoltaic Mechanism

Absorbed photon creates electron-hole pair. Built-in junction field separates them.

**Illuminated I-V equation**:
$$I = I_{SC} - I_0(e^{qV/kT} - 1)$$

I_SC = short-circuit photocurrent (proportional to incident photon flux × quantum efficiency).

**Open-circuit voltage**:
$$V_{OC} = \frac{kT}{q}\ln\left(\frac{I_{SC}}{I_0} + 1\right) \approx \frac{kT}{q}\ln\frac{I_{SC}}{I_0}$$

**Fill factor**:
$$FF = \frac{P_{max}}{V_{OC} \cdot I_{SC}} = \frac{V_{mp} \cdot I_{mp}}{V_{OC} \cdot I_{SC}}$$

**Efficiency**: η = FF × V_OC × I_SC / P_in

```
    Shockley-Queisser (SQ) limit for single-junction (1961):
    Fundamental losses:
    1. Sub-bandgap photons: ℏω < E_g → transmitted (not absorbed)
    2. Thermalization: ℏω > E_g → excess becomes heat
    3. Radiative recombination: mandatory (detailed balance)
    4. Voltage factor: qV_OC < E_g always

    SQ maximum efficiency:
    Si (1.12 eV):  33.7%
    GaAs (1.43 eV): 33.8% (near optimum for AM1.5G)
    InP (1.35 eV): 33.8%
    Optimal E_g for AM1.5G: ~1.1-1.4 eV

    Record cells (2024):
    Si single junction:  29.4% (kaneka, HIT cell)
    GaAs single junction: 29.6% (Alta Devices)
    3-junction concentrator: 47.6% (Fraunhofer ISE)
    Si commercial module:  24% (SunPower M-series)
    Perovskite/Si tandem:  33.9% (Helmholtz Berlin)

    Two-junction requirement for each bandgap:
    Top cell: large E_g, absorbs high-energy photons
    Bottom cell: small E_g, absorbs transmitted photons
    Current matching required (series connection)
```

---

## LEDs and Laser Diodes

### LED Physics

Forward-biased p-n junction in direct-gap semiconductor.
Injected minority carriers recombine → photon.

```
    Requirements for efficient LED:
    1. Direct bandgap: no phonon needed for momentum conservation
    2. High radiative recombination rate B_r >> non-radiative rate
    3. Carrier confinement (quantum well structures preferred)

    Emission wavelength: λ = hc/E_g = 1240 nm / E_g(eV)

    Material choices:
    Red  (625-760nm): AlGaInP, GaAsP, AlGaAs (E_g = 1.6-2.0 eV)
    Green (520-565nm): InGaN with high In content, GaP:N
    Blue (450-490nm): InGaN/GaN (E_g ~ 2.7 eV with In₀.₁₅Ga₀.₈₅N)
    UV   (<380nm):   AlGaN/GaN, AlN (deep UV)
    White: Blue chip (InGaN) + YAG:Ce phosphor (converts to yellow)
           Combined spectrum appears white to human eye

    Nobel 2014: Akasaki, Amano, Nakamura for blue LED (GaN)
    Key challenge: p-type doping of GaN
    Mg acceptors passivated by hydrogen during MOCVD → need thermal activation at 700°C

    EQE (external quantum efficiency) = photons_out / electrons_in
    Modern LEDs: 50-80% EQE
    Droop: EQE falls at high current density (Auger recombination)
```

### Laser Diode (LD)

Stimulated emission + feedback (Fabry-Perot cavity or DFB grating).

```
    Threshold condition: gain G = loss (cavity + mirror losses)
    Below threshold: LED-like spontaneous emission
    Above threshold: lasing (coherent, narrow linewidth)

    Rate equations:
    dN/dt = J/(qd) - N/τ_sp - v_g G(N-N_0)S
    dS/dt = Γ v_g G(N-N_0)S - S/τ_ph + β_sp N/τ_sp
    N = carrier density, S = photon density, G = material gain
    Γ = confinement factor, τ_ph = photon lifetime

    Applications by wavelength:
    780 nm:  GaAs/AlGaAs → CD players, laser printers
    850 nm:  VCSEL → short-reach fiber, 3D sensing (Face ID)
    1310 nm: InGaAsP/InP → zero-dispersion fiber wavelength
    1550 nm: InGaAsP/InP, EML → telecom C-band, DWDM
    405 nm:  GaN → Blu-ray
    DFB at 1550nm: linewidth < 1 MHz, tunable 50GHz channel spacing
```

---

## Photodetectors

```
    Reverse-biased p-n junction or PIN structure.
    Photon absorbed → electron-hole pair → swept by field → photocurrent.

    Responsivity: R = I_photo/P_opt = ηq/(hf) A/W
    η = quantum efficiency (fraction of photons that create carriers)
    For Si at 850 nm: η ≈ 0.9, R ≈ 0.62 A/W

    Bandwidth limited by:
    1. Transit time: t_transit = W_dep/v_sat → f_-3dB ≈ 0.44/t_transit
    2. RC time constant: R_load × C_j

    Tradeoff: wider depletion → more absorption (η↑) → more transit time (f_-3dB↓)
    APD (avalanche photodiode): internal gain M = 5-100 through impact ionization
    Excess noise F = M^x (x = 0.5 for Si, 0.7 for InGaAs/InP)

    Detector materials:
    Si:      400-1100 nm, mature, cheap, CMOS compatible
    InGaAs:  900-1700 nm, telecom (1310/1550 nm)
    Ge-on-Si: 800-1600 nm, CMOS compatible Ge photodetector
    HgCdTe:  1-10 μm (tunable via composition), night vision, FLIR
    InSb:    3-5 μm, cooled, thermal IR
```

---

## Materials Comparison Table

| Property           | Si      | Ge      | GaAs    | InP     | GaN     | 4H-SiC  | Diamond |
|-------------------|--------|--------|--------|--------|--------|--------|--------|
| E_g (eV)           | 1.12    | 0.67    | 1.43    | 1.35    | 3.4     | 3.26    | 5.5     |
| Gap type           | Indirect| Indirect| Direct | Direct | Direct | Indirect| Indirect|
| ε_r                | 11.7    | 16.0    | 12.9    | 12.5    | 9.0     | 10.0    | 5.7     |
| μ_e (cm²/V·s)     | 1450    | 3900    | 8500    | 5400    | 1250    | 1000    | 4500    |
| μ_h (cm²/V·s)     | 450     | 1900    | 400     | 200     | 200     | 115     | 3800    |
| n_i(cm⁻³, 300K)   | 1.5×10¹⁰| 2.4×10¹³| 2×10⁶ | 10⁷    | ~10⁻¹⁰ | ~10⁻⁸  | <10⁻²⁰ |
| E_crit (MV/cm)     | 0.3     | 0.1     | 0.4     | 0.5     | 3.3     | 2.5     | 10      |
| k (W/m·K)          | 150     | 60      | 46      | 68      | 130     | 490     | 2200    |
| v_sat (10⁷ cm/s)   | 1.0     | 0.6     | 2.0     | 2.0     | 2.5     | 2.0     | 2.7     |
| Lattice a (Å)      | 5.43    | 5.66    | 5.65    | 5.87    | 3.19    | 3.08    | 3.57    |

Figures of merit for power devices:
- Baliga's FOM: ε μ E_crit³ (minimizes on-resistance per breakdown voltage)
  Si=1, GaN≈1000, SiC≈500, Diamond≈50000
- Johnson's FOM: (E_crit v_sat)²/(4π²) (high-frequency power)
  GaN wins for RF power amplifiers → GaN PA in 5G base stations

---

## Decision Cheat Sheet

| Application                    | Best Material       | Why                                     |
|-------------------------------|--------------------|-----------------------------------------|
| CMOS logic (high volume)       | Si                  | Mature, cheap, excellent native SiO₂    |
| RF/microwave LNA, PA           | GaAs PHEMT, GaN HEMT| High μ_e, GaN also high power           |
| EV power electronics           | SiC MOSFET          | High E_crit, high k, high T operation   |
| 5G base station PA             | GaN-on-SiC          | High power density, efficiency, f_T     |
| Blue/white LED                 | InGaN/GaN           | Direct gap, stable, high EQE            |
| Telecom laser (1550nm)         | InGaAsP/InP DFB     | Direct gap, lattice matched, low loss   |
| Silicon photonics             | Si + Ge-on-Si        | CMOS integration, modulator+detector    |
| High-T electronics (>300°C)   | SiC, GaN            | Large E_g → tiny n_i                    |
| Quantum computing qubit        | Si/SiGe, GaAs, NV-diamond | Coherence time, scalability       |
| Solar cell (commercial)        | Si                  | Cheap, abundant, mature, 22-25%         |
| Concentrator multi-junction PV | GaAs/InGaP/Ge       | Highest efficiency, aerospace           |

---

## Common Confusion Points

**Depletion width is not where current flows**: Most current in a forward-biased diode flows
as minority carrier diffusion in the quasi-neutral regions adjacent to the depletion zone.
The depletion region is where the space charge and field live; the current-generating physics
is the minority carrier injection and recombination.

**V_T is not V_bi**: Threshold voltage V_T (0.3-0.8 V) is the gate voltage needed to invert
the channel. Built-in voltage V_bi (0.6-0.8 V for Si) is the equilibrium contact potential.
They're numerically similar for Si but arise from completely different physics.

**Si is indirect-gap but still makes decent solar cells**: Optical absorption is slower
(~300 μm needed vs ~1 μm for GaAs), but Si uses light-trapping (texturing + reflectors)
to make optical path much longer than physical thickness. Cost advantage overwhelms the
efficiency penalty for terrestrial applications.

**MOSFET saturation ≠ BJT saturation**: In a BJT, "saturation" means both junctions forward
biased and the transistor acts like a closed switch with small V_CE. In a MOSFET, "saturation"
means the channel is pinched off at the drain and I_D is controlled by V_GS alone. Completely
different physics, unfortunately sharing the same word.

**High-κ dielectric for modern gate oxide**: Below ~2 nm SiO₂, direct tunneling gate leakage
becomes unacceptably high. Solution (Intel 45nm, 2007): replace SiO₂ with HfO₂ (κ=20-25,
vs 3.9 for SiO₂). A 4 nm HfO₂ film has same capacitance as 0.78 nm SiO₂ (EOT=0.78nm) but
far lower tunneling current. Trade-off: HfO₂ reduces channel mobility (remote phonon scattering).
