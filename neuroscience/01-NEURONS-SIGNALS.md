# Neurons and Signals — Biophysics of Neural Signaling

## The Big Picture

<!-- @editor[diagram/P2]: Diagram is a linear pipeline -- effective for signaling cascade but doesn't show lateral relationships (how cable theory and synaptic transmission interact at dendrite, how AP energy cost constrains firing rate) -->
```
    NEURAL SIGNALING HIERARCHY
    ══════════════════════════════════════════════════════════

    ION GRADIENTS (Nernst equilibrium)
         │
         ▼
    RESTING POTENTIAL (-70 mV) [Goldman-Hodgkin-Katz]
         │
         ▼
    SYNAPTIC INPUTS (EPSPs, IPSPs) + intrinsic conductances
         │
         ▼
    THRESHOLD CROSSING (-55 mV)
         │
         ▼
    ACTION POTENTIAL (Hodgkin-Huxley model)
         │
         ▼
    AXONAL PROPAGATION (cable equation, saltatory conduction)
         │
         ▼
    SYNAPTIC TRANSMISSION (Ca²⁺, vesicle, SNARE, quantal release)
         │
         ▼
    POSTSYNAPTIC INTEGRATION (temporal + spatial summation)
         │
         ▼
    DENDRITIC COMPUTATION (passive + active, NMDA AND-gate)
```

---

## Ion Gradients and Electrochemical Equilibrium

### Ion Concentration Gradients

```
    ┌──────────────────────────────────────────────────────────────┐
    │  ION CONCENTRATIONS (approximate, mammalian neuron)          │
    │                                                              │
    │  Ion      │ Intracellular │ Extracellular │ Nernst Eq.      │
    │  ─────────┼───────────────┼───────────────┼────────────────  │
    │  K⁺       │ 140 mM        │ 5 mM          │ E_K = -90 mV    │
    │  Na⁺      │ 10 mM         │ 140 mM        │ E_Na = +65 mV   │
    │  Cl⁻      │ 10 mM         │ 110 mM        │ E_Cl = -65 mV   │
    │  Ca²⁺     │ 0.0001 mM     │ 2 mM          │ E_Ca = +125 mV  │
    │  A⁻(organ)│ 350 mM        │ 0 mM          │ —               │
    └──────────────────────────────────────────────────────────────┘

    Gradients maintained by Na⁺/K⁺ ATPase pump:
    3 Na⁺ out, 2 K⁺ in per ATP molecule (electrogenic: net +1 charge out)
    ~70% of neuron's metabolic energy goes to this pump!
    Brain energy consumption: 20W × 0.70 = 14W just for ion pumping
```

### Nernst Equation

For a single ion species with valence z, equilibrium potential:

$$E_{ion} = \frac{RT}{zF}\ln\frac{[ion]_{out}}{[ion]_{in}} = \frac{25.7 \text{ mV}}{z}\ln\frac{[ion]_{out}}{[ion]_{in}}$$

```
    At 37°C: RT/F = 26.7 mV (often approximated as 25 mV)

    K⁺ (z=+1): E_K = 25.7 × ln(5/140) = 25.7 × (-3.33) = -85.6 mV ≈ -90 mV
    Na⁺ (z=+1): E_Na = 25.7 × ln(140/10) = 25.7 × 2.64 = 67.9 mV ≈ +65 mV
    Cl⁻ (z=-1): E_Cl = 25.7/(-1) × ln(110/10) = -25.7 × 2.4 = -61.7 mV ≈ -65 mV
    Ca²⁺(z=+2): E_Ca = 25.7/2 × ln(2/0.0001) = 12.85 × 9.9 = 127 mV ≈ +125 mV
```

### Goldman-Hodgkin-Katz (GHK) Equation

Resting potential is not Nernst for any single ion — it's a weighted sum based on
the relative permeabilities of the membrane to each ion:

$$V_m = \frac{RT}{F}\ln\frac{P_K[K^+]_o + P_{Na}[Na^+]_o + P_{Cl}[Cl^-]_i}{P_K[K^+]_i + P_{Na}[Na^+]_i + P_{Cl}[Cl^-]_o}$$

```
    At rest: P_K : P_Na : P_Cl ≈ 1 : 0.04 : 0.45
    (K⁺ dominates because K⁺ leak channels are open at rest)

    Substituting typical values:
    V_m = 25.7 × ln[(1×5 + 0.04×140 + 0.45×10) / (1×140 + 0.04×10 + 0.45×110)]
         = 25.7 × ln[(5 + 5.6 + 4.5) / (140 + 0.4 + 49.5)]
         = 25.7 × ln[15.1 / 189.9]
         = 25.7 × (-2.53) = -65 mV ≈ -70 mV typical ✓

    During action potential: P_Na spikes >> P_K → V_m → E_Na ≈ +65 mV
    Repolarization: K⁺ channels open → P_K increases → V_m → E_K ≈ -90 mV
```

---

<!-- @editor[bridge/P2]: No dynamical-systems bridge for H-H model -- MIT math maps directly: H-H is 4D ODE with Hopf bifurcation at threshold, limit cycle = AP, saddle-node on invariant circle for Type I neurons -->
## Action Potential: Hodgkin-Huxley Model

The foundational model of neural computation. Nobel Prize 1963: Hodgkin and Huxley.

### Hodgkin-Huxley Equations

```
    C_m dV/dt = -g_Na m³h(V - E_Na) - g_K n⁴(V - E_K) - g_L(V - E_L) + I_ext

    where:
    C_m = membrane capacitance per unit area ≈ 1 μF/cm²
    g_Na = maximum Na⁺ conductance ≈ 120 mS/cm²
    g_K  = maximum K⁺ conductance  ≈ 36 mS/cm²
    g_L  = leak conductance         ≈ 0.3 mS/cm²
    E_Na = +55 mV, E_K = -77 mV, E_L = -65 mV

    m, h, n = gating variables (dimensionless, 0 to 1):
    m = Na⁺ activation gate      (m³: three independent gates)
    h = Na⁺ inactivation gate    (one gate, normally open at rest)
    n = K⁺ activation gate       (n⁴: four independent gates)

    Gating variable ODEs (voltage-dependent rate constants):
    dm/dt = α_m(V)(1-m) - β_m(V)m   [similarly for h and n]

    Steady state: m_∞(V) = α_m/(α_m + β_m)
    Time constant: τ_m(V) = 1/(α_m + β_m)

    Rate constants (Hodgkin-Huxley squid axon, 6.3°C):
    α_m = 0.1(V+40)/(1-exp(-(V+40)/10))
    β_m = 4 exp(-(V+65)/18)
    α_h = 0.07 exp(-(V+65)/20)
    β_h = 1/(1+exp(-(V+35)/10))
    α_n = 0.01(V+55)/(1-exp(-(V+55)/10))
    β_n = 0.125 exp(-(V+65)/80)
    (V in mV; temperatures scale α,β by Q₁₀)
```

### Action Potential Anatomy

```
    Vm (mV)
    +50 ┤          ╭──╮   ← Peak: Na⁺ influx, V → E_Na
        │         /    \
      0 ┤        /      \
        │       /        \
    -55 ┤──────●  Threshold │  ← Voltage-clamp reveals gating
    -70 ┤ Rest    \       /
    -80 ┤          \   /  ← Undershoot: K⁺ still flowing out, E_K
    -90 ┤           ───   ← Absolute refractory: Na⁺ inactivated (h gate shut)
        │
        └──────────────────── time (ms)
        0    0.5   1    1.5  2

    PHASES:
    1. Depolarization (0-0.5ms): V exceeds threshold → m opens rapidly
       Na⁺ floods in (g_Na × m³h × (V - E_Na) >> 0)
       Regenerative: more depolarization → more m opening → more Na⁺ in

    2. Repolarization (0.5-1ms): h closes (inactivation, slower than m)
       n opens (K⁺ channels, slower than Na⁺)
       K⁺ flows out → repolarize

    3. Undershoot/AHP (1-2ms): n still open, K⁺ still out → below rest
       E_K = -90 mV pulls V below V_rest = -70 mV

    4. Absolute refractory (0-1ms): h = 0 (Na⁺ inactivated)
       No AP possible regardless of stimulus

    5. Relative refractory (1-3ms): h partially recovered, elevated threshold
       Stronger stimulus can fire AP (but frequency-coded information reduced)
```

### Energy Cost of Action Potentials

```
    One AP on squid axon: ~5 × 10¹² Na⁺ ions enter (per cm²)
    Na⁺/K⁺ pump must restore: 3 Na⁺ out per ATP → 1.67 × 10¹² ATP/cm²
    For myelinated cortical neuron firing at 50 Hz:
    ATP consumption ≈ 1.6 × 10⁸ ATP per second per cm of axon

    Brain total: 86 × 10⁹ neurons × ~10 Hz average × ATP cost
    → ~10²⁰ ATP per second ≈ 20W ✓ (matches measured brain metabolic rate)

    Efficiency: brain is extremely efficient relative to silicon:
    Energy per "operation" (AP): ~10 pJ
    Energy per FLOP (A100 GPU): ~0.3 pJ at 700W, 2000 TFLOP/s
    But "operations" are not equivalent (AP is more than 1 FLOP)
```

---

## Cable Theory

Neurons have spatially extended dendrites — signals decay as they travel.

**Cable equation** (passive, no active currents):

$$\lambda^2 \frac{\partial^2 V}{\partial x^2} = \tau_m \frac{\partial V}{\partial t} + V$$

where:
- $\lambda = \sqrt{r_m/r_i}$ = electrotonic length constant [cm]
- $\tau_m = r_m c_m$ = membrane time constant [ms]
- r_m = membrane resistance (Ω·cm), r_i = axial resistance (Ω/cm), c_m = capacitance (F/cm²)

```
    Steady-state spatial decay: V(x) = V₀ exp(-x/λ)
    Signal decays to 1/e at distance λ from input site

    Typical values (cortical pyramidal dendrite):
    λ ≈ 0.1-1 mm (depends on dendrite diameter, membrane properties)
    τ_m ≈ 10-30 ms

    For a thin distal dendrite (d = 0.2 μm, r_m = 10,000 Ω·cm²):
    r_i = 4ρ_axoplasm/(πd²) = 4×150/(π×(0.2×10⁻⁴)²) ≈ 1.9×10¹⁰ Ω/cm
    r_m = R_m/πd = 10,000/(π×0.2×10⁻⁴) ≈ 1.6×10⁸ Ω·cm
    λ = √(r_m/r_i) = √(1.6×10⁸/1.9×10¹⁰) = 0.092 mm

    → Synaptic inputs at distal dendrites are severely attenuated at soma!
    This is why active conductances in dendrites matter (amplification).

    Input impedance (at terminal of semi-infinite cable):
    Z_in = √(r_m r_i) = r_i × λ  (dimensional analysis: Ω·cm × cm/cm = Ω×... use correctly)
    Actual: Z_in at terminal = √(R_m ρ_i) / (πd^(3/2)) ∝ d^(-3/2)
    → Thin dendrites: high impedance → large EPSP per injected charge ✓
```

### Neuron as Leaky Integrator

From the learner's electronics background:

```
    Equivalent circuit of neuron:
                    I_ext
                      │
         ┌──────────────────────────────┐
         │  Membrane of neuron          │
    ─────┤                              ├─────
    Vm   │   ┌──R_m──┐   ┌──C_m──┐   │
         │   │       │   │       │   │
    ─────┴───┴───────┴───┴───────┴───┴─────
    GND

    Single-compartment passive neuron:
    τ_m dV/dt = -(V - E_L) + R_m I_ext
    τ_m = R_m C_m ≈ 10-30 ms

    Leaky integrate-and-fire (LIF) model:
    τ_m dV/dt = -(V - E_L) + R_m I_ext
    IF V(t) ≥ V_threshold: emit spike, reset V → V_reset, t → t + t_ref

    This is an RC circuit with a threshold comparator + reset:
    V(t) = E_L + R_m I_ext(1 - e^{-t/τ_m}) (constant I, starting from E_L)
    Time to threshold: t_spike = -τ_m ln(1 - (V_th-E_L)/(R_m I_ext))
    Firing rate: f = 1/t_spike (for constant I > I_threshold)
    f(I) = 1/(τ_m ln((I-I_min)/(I-I_min-ΔI_max)))  ← inverse log of the curve

    Gain function (f-I curve): roughly linear for I >> threshold
    Real neurons: often power-law f ∝ (I - I_th)^δ, δ ≈ 0.5-3

    Note: LIF fires repetitively; real neurons adapt (spike-frequency adaptation)
    via slow K⁺ channels that turn on with each spike → reduces excitability
```

---

## Synaptic Transmission

### Anatomy of a Chemical Synapse

```
    ┌─────────────────────────────────────────────────────────────┐
    │  PRESYNAPTIC TERMINAL        │  POSTSYNAPTIC DENSITY (PSD)  │
    │                              │                              │
    │  Synaptic vesicles (SV)      │  Receptors (AMPA, NMDA)     │
    │  ~40 nm diameter             │  PSD-95 scaffolding          │
    │  ~5000 glutamate molecules   │  CaMKII, SHANK, Homer        │
    │  per vesicle                 │                              │
    │  Active zone proteins:       │  Spine head: ~0.1-0.5 μm    │
    │  RIM, Munc13, RIM-BP         │  Spine neck: thin, ~0.1 μm  │
    │                              │                              │
    │  SYNAPTIC CLEFT (~20-30 nm) │                              │
    └─────────────────────────────────────────────────────────────┘
```

### Calcium-Triggered Vesicle Fusion

```
    AP arrives at terminal → depolarization → Ca²⁺ channel opening
    (P/Q-type Cav2.1 at most CNS synapses, N-type Cav2.2 also)

    Ca²⁺ influx → SNARE complex formation:
    VAMP/synaptobrevin (v-SNARE on vesicle) + SNAP-25 + syntaxin (t-SNARE on membrane)
    → 4-helix bundle zippers → pulls membranes together → fusion

    Synaptotagmin I: Ca²⁺ sensor on vesicle (binds 5 Ca²⁺)
    → Inserts into membrane → triggers final fusion step
    KD for Ca²⁺: 10-200 μM, [Ca²⁺] at active zone: 100-300 μM during AP

    Timing: Ca²⁺ enters → vesicle fuses in 0.3-0.5 ms (extremely fast)
    Enabled by: vesicles pre-docked at active zones (ready-releasable pool ~20-30 vesicles)
    NSF + αSNAP: disassemble SNARE complex after fusion → recycle

    Quantal release:
    Each vesicle = one quantum (Katz 1954)
    n = number of release sites, p = release probability per site, q = quantal size
    Mean EPSP amplitude: μ = npq
    Variance: σ² = npq(1-p)q = μq(1-p)  (for binomial)
    Coefficient of variation: CV² = (1-p)/np + CV²_q
    → Can estimate n, p, q from amplitude fluctuations (quantal analysis)

    Typical values (excitatory hippocampal synapse):
    n ≈ 1-5 release sites
    p ≈ 0.1-0.5 (stochastic!)
    q ≈ 0.5-2 mV EPSP amplitude per vesicle
    → Synaptic transmission is probabilistic, not deterministic
```

---

## Synaptic Potentials and Reversal Potential

Ionotropic receptors are ligand-gated ion channels. Opening changes conductance.

**EPSP (Excitatory Post-Synaptic Potential)**:
```
    I_syn = g_syn(V - E_syn)   where E_syn = reversal potential
    For glutamate (AMPA): E_rev ≈ 0 mV (Na⁺ in + K⁺ out roughly equal)
    EPSP depolarizes: V goes from -70 mV toward 0 mV

    Current convention: inward current (into cell) = depolarizing
    AMPA channel: Na⁺ influx + K⁺ efflux → net inward current at V=-70 mV
    g_AMPA × (-70 - 0) = g_AMPA × (-70) → current inward ✓
```

**IPSP (Inhibitory Post-Synaptic Potential)**:
```
    For GABA_A: E_rev ≈ -65 to -75 mV (Cl⁻ channel)
    In adult neurons: E_Cl ≈ -65 mV < V_rest = -70 mV
    → Small outward Cl⁻ current → slight depolarization but shunting inhibition
    OR: in some interneurons E_Cl more negative → actual hyperpolarization

    In young neurons: E_Cl ≈ -40 mV (NKCC1 active) → GABA is EXCITATORY
    Developmental switch: NKCC1 → KCC2 at ~P7 in rats → GABA becomes inhibitory
    Important for: neonatal seizure treatment (NKCC1 inhibitor bumetanide)

    Shunting inhibition: even if IPSP doesn't hyperpolarize, it increases g_total
    → EPSPs smaller amplitude (more current needed to achieve same ΔV)
    → "Vetoing" excitatory inputs without hyperpolarization
```

---

## Temporal and Spatial Summation

```
    TEMPORAL SUMMATION:
    Two EPSPs arrive at same synapse within τ_m (~10-30ms):
    Second EPSP rides on tail of first → larger combined depolarization

    Time window: limited by τ_m (membrane time constant)
    → Inputs arriving within τ_m can summate

    SPATIAL SUMMATION:
    EPSPs from different synapses on same neuron summate at soma
    Attenuation by cable properties: distal inputs smaller than proximal
    Soma integrates all inputs (with distance-dependent weighting)

    COINCIDENCE DETECTION (NMDA receptor):
    NMDA channel has Mg²⁺ block at rest:
    At V = -70 mV: Mg²⁺ occupies pore → no current even with glutamate bound
    For current to flow: need BOTH glutamate (ligand) AND depolarization (removes Mg²⁺)
    → NMDA is a molecular AND gate
    → Fires only when pre AND post active within ~100ms window
    → This is Hebb's rule implemented in hardware: "neurons that fire together wire together"
    → Ca²⁺ through NMDA channel → CaMKII activation → AMPA receptor insertion = LTP
```

---

## Dendritic Computation

Classical view: dendrites are passive cables that sum inputs.
Modern view: dendrites perform complex computations.

```
    Active dendritic mechanisms:
    1. Backpropagating APs (bAPs): APs propagate back into dendrites
       → Depolarize dendrites → helps NMDA activation for LTP induction
       → Requires Na⁺ channels in dendrites (attenuated in thick L5 apical dendrites)

    2. Dendritic spikes:
       Na⁺ spikes: fast, propagate well, threshold ~-50 mV
       Ca²⁺ spikes: slower, local amplification, in distal dendrites
       NMDA spikes: sustained (~50 ms), require NMDA channel activation
       → NMDA spike = nonlinear gain: if ≥ 5-10 synchronous inputs on one branch,
         Ca²⁺ + Na⁺ spike amplifies input enormously

    3. Compartmentalization:
       Thin necks of dendritic spines: high impedance → electrical isolation
       Each branch can act as an independent integration unit
       Poirazi et al. (2003): single pyramidal neuron ≈ 2-layer neural network
       (dendrite = inner layer, soma = output layer)

    4. Direction selectivity in retina:
       Asymmetric inhibitory input onto dendrites → responds to one motion direction
       Starburst amacrine cell dendrites compute local motion direction
```

---

<!-- @editor[structure/P2]: No dedicated old-world bridge section -- leaky-integrator electronics bridge is excellent but buried. Add standalone bridges: dynamical systems (bifurcations for HH), thermodynamics (Nernst = Gibbs free energy), information theory (channel capacity of spike train) -->
## Decision Cheat Sheet

| Biophysical feature             | Functional role                          | Modeling equivalent        |
|---------------------------------|------------------------------------------|---------------------------|
| K⁺ leak channel (at rest)       | Sets V_rest near E_K                     | Bias/resting state         |
| Na⁺ voltage-gated (fast)        | AP upstroke (all-or-nothing)             | Threshold nonlinearity     |
| K⁺ voltage-gated (delayed)      | AP repolarization + undershoot           | Output normalization       |
| K⁺ A-current (I_A)              | Delays first spike → adaptation          | Slow state variable        |
| K⁺ Ca²⁺-dependent (SK, BK)     | AHP → spike-frequency adaptation         | Negative feedback          |
| H-current (I_h, HCN channel)    | Depolarizing sag, resonance               | High-pass filter in dendrite|
| Ca²⁺ persistent (I_CaL)         | Plateau potentials, burst firing          | Bistability                |
| AMPA receptor                   | Fast EPSP, rate-coded excitation          | Weighted sum (linear)      |
| NMDA receptor                   | Coincidence detection, LTP trigger        | AND gate, Hebbian plasticity|
| GABA_A receptor                 | Fast shunting/hyperpolarizing inhibition  | Divisive normalization      |
| GABA_B receptor                 | Slow K⁺ IPSP                            | Long-time-constant feedback |

---

## Common Confusion Points

**Threshold is not a fixed voltage**: The -55 mV "threshold" is an approximation.
The actual threshold depends on how fast the membrane depolarizes (rate of rise affects
Na⁺ channel activation vs inactivation), recent history (Na⁺ inactivation recovers
slowly), and which conductances are active. Dynamic threshold = important for understanding
precision timing of spikes.

**Excitatory inputs can be inhibitory if reversal potential is positive relative to spike threshold**:
An ion channel with E_rev = 0 mV is "depolarizing" from -70 mV rest, but if it's shunting
a dendritic compartment that was going to receive a large excitatory drive, it can prevent
that compartment from summing enough to fire. Context matters.

**Ca²⁺ influx through NMDA is what matters for LTP, not the voltage change**: The
coincidence detection function of NMDA leads to Ca²⁺ entry, which activates CaMKII,
which phosphorylates existing AMPA receptors and triggers AMPA receptor insertion.
The voltage depolarization from NMDA opening is secondary. This is why the Mg²⁺ block
is so important: it gates Ca²⁺ entry, which is the synaptic plasticity signal.

**Synaptic delay ≠ refractory period**: Synaptic delay (0.5-2 ms from AP to EPSP)
is due to Ca²⁺ diffusion, SNARE complex kinetics, and vesicle fusion. Refractory period
(1-3 ms) is the Na⁺ channel inactivation recovery time in the axon/soma. They're separate.
