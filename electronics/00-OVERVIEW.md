# Electronics — Field Overview

Electronics is applied electromagnetism, reduced through successive approximations to tractable models — the same abstraction-layer strategy used in compiler theory (source → IR → machine code) or numerical analysis (exact PDE → finite element → algebraic system). The approximation hierarchy here is Maxwell's equations → quasi-static fields → lumped circuit elements (R, L, C), and the art of electronics is knowing when each layer breaks.

## The Big Picture

```
ELECTRONICS FIELD MAP
═══════════════════════════════════════════════════════════════════════════════

  SIGNAL DOMAIN ──────────────────────────────────────────────────────────────
                    ANALOG                          DIGITAL
                 (continuous)                    (discrete levels)
  ┌─────────────────────────────┐    ┌──────────────────────────────────────┐
  │  Circuits (01)              │    │  Digital Logic (08)                  │
  │  Reactive components (02)   │    │  Embedded / VLSI (09)               │
  │  Filters (03)               │    │                                      │
  │  Amplifiers (04)            │    │  Bridge: ADC/DAC converts between    │
  └─────────────────────────────┘    └──────────────────────────────────────┘
                    ↑                                  ↑
             signal conditioning             computation / control
                    │                                  │
                    └──────────── ADC / DAC ───────────┘

  FREQUENCY DOMAIN ────────────────────────────────────────────────────────────
  DC    |    Audio    |   RF            |   Microwave     |   Optical
  0 Hz  | 20Hz-20kHz  | 3kHz-300MHz     | 300MHz-300GHz   | ~200THz
        │             │                 │                  │
        │  Signals &  │  Filters (03)   │  Lumped model    │  Photonics
        │  Systems (05)│  Amplifiers(04)│  breaks down     │  (not here)
        │  DSP (06)   │                 │  use distributed │
        │  2D-DSP (07)│                 │  element models  │

  SCALE ───────────────────────────────────────────────────────────────────────
  Discrete                  Integrated Circuit         System-on-Chip / FPGA
  components                ┌─────────────┐            ┌──────────────────────┐
  R, L, C, BJT, MOSFET  →  │ op-amp, ADC │  →         │ CPU, GPU, FPGA, ASIC │
  individual packages       │ DRAM cell   │            │ billions of Tx       │
  µW – W range              └─────────────┘            └──────────────────────┘
                                                              VLSI (09)

  POWER RANGE ─────────────────────────────────────────────────────────────────
  µW          mW          W           kW           MW
  MEMS        MCU (sleep) MCU (active) Motor drive  Grid inverter
  sensor      Smartphone  CPU/GPU      EV traction  (power electronics)
  nodes       SoC                                   [NOT in this directory]
```

---

## Signal Chain: The Unifying Architecture

Almost every electronics system is a signal chain — data flows left to right
through conditioning, conversion, and processing stages.

```
  GENERIC SIGNAL CHAIN
  ┌──────────┐   ┌───────────────┐   ┌──────────┐   ┌────────────────┐   ┌────────┐
  │  SOURCE  │──▶│  CONDITIONING │──▶│  ADC/DAC │──▶│  PROCESSING    │──▶│ OUTPUT │
  │          │   │               │   │          │   │                │   │        │
  │ sensor   │   │ amplification │   │ analog→  │   │ CPU / DSP /    │   │ display│
  │ antenna  │   │ filtering      │   │ digital  │   │ FPGA / MCU     │   │ speaker│
  │ mic      │   │ impedance match│   │ (or D→A) │   │ (modules 05-09)│   │ motor  │
  │ photo-   │   │ anti-aliasing  │   │          │   │                │   │ RF Tx  │
  │ detector │   │ (modules 01-04)│   │          │   │                │   │        │
  └──────────┘   └───────────────┘   └──────────┘   └────────────────┘   └────────┘

  Key metrics at each stage:
  Conditioning:  gain (dB), noise figure (NF, dB), bandwidth (Hz)
  Conversion:    resolution (bits), SNR (dB), SFDR (dBc), sample rate (S/s)
  Processing:    throughput (MOPS/GOPS), latency (µs), power (mW)
```

---

## Component Taxonomy

### Passive vs Active

```
  PASSIVE                           ACTIVE
  ────────────────────────────────  ────────────────────────────────────────
  Cannot amplify signal             Can amplify (requires external power)
  Power: consume or store only      Power: can deliver more than input

  Resistor R: V = IR               BJT: I_C = β·I_B  (current controlled)
  Capacitor C: I = C·dV/dt         MOSFET: I_D = f(V_GS, V_DS)
  Inductor L: V = L·dI/dt          Op-amp: V_out = A_OL·(V+ - V-)
  Transformer: V₂/V₁ = N₂/N₁      Diode: I = I_S·(e^(V/nV_T) - 1)

  Passive filters: RC, LC, RLC     Active filters: op-amp + RC (module 03)
  Passive networks: dividers,       Active circuits: amplifiers (module 04)
  matching networks, attenuators    oscillators, mixers
```

### Linear vs Nonlinear

```
  LINEAR (superposition holds)      NONLINEAR (superposition breaks)
  ────────────────────────────────  ────────────────────────────────────
  R, L, C (ideal)                  Diodes, transistors (large-signal)
  Linear op-amp in feedback         Saturated/clipped amplifier
  → analysis: Laplace, phasors,     → analysis: Volterra series,
    Bode plots, convolution           load-line graphical, SPICE
  Modules 01-06 mostly here         Modules 04 (nonlinear region),
                                    08-09 (logic switching)
```

### Time-Invariant vs Time-Varying

```
  LTI (Linear Time-Invariant)       Time-varying
  ────────────────────────────────  ────────────────────────────────
  Parameters don't change with t    Parameters change (switched-cap
  RC filter: same response at t=0   filters, mixers, switched-mode PS)
  and t=1000s
  → Full frequency-domain analysis  → Cannot use standard Fourier; use
    valid: H(jω) fully characterizes  modulation theory, Z-domain for
    the system                        discrete-time switching
  Core assumption in modules 05-07
```

---

## Frequency Regions in Detail

```
  FREQUENCY MAP
  ─────────────────────────────────────────────────────────────────────────────
  Frequency    Region          Key Phenomena           Engineering Domain
  ─────────────────────────────────────────────────────────────────────────────
  DC – 1 Hz    Quasi-static    Drift, leakage          Power supply, sensors
  1 Hz – 20 kHz  Audio         Human hearing range     Audio, seismic, EEG
  20 kHz – 1 MHz  Sub-RF       PWM switching, ultrasound  Motor control, SMPS
  1 MHz – 30 MHz  HF/shortwave Ionospheric propagation  Amateur radio, SW Tx
  30 MHz – 1 GHz  VHF/UHF      Line-of-sight prop      TV, FM, 4G, WiFi 2.4G
  1 GHz – 30 GHz  Microwave    Free-space, waveguide   WiFi 5/6, 5G mmWave, RADAR
  30 GHz – 300 GHz  mm-wave   Atmospheric absorption  5G FR2, imaging
  > 300 GHz    THz/optical     Quantum transitions     Spectroscopy, LiDAR
  ─────────────────────────────────────────────────────────────────────────────

  LUMPED ELEMENT MODEL VALIDITY
  Valid when: λ >> L_physical  (wavelength much larger than circuit dimensions)

  At 1 MHz:    λ = 300 m   → 1-cm PCB trace is fine, λ/L = 30,000×
  At 1 GHz:    λ = 30 cm   → 1-cm trace is λ/30 — microstrip effects matter
  At 10 GHz:   λ = 3 cm    → trace IS a transmission line; must use S-params
  At 100 GHz:  λ = 3 mm    → waveguide and distributed structures only

  Breakdown symptoms: unexpected resonances, signal reflections (S11),
  impedance mismatch insertion loss, radiation (PCB becomes antenna)
```

---

## Physics Foundation: Maxwell to Circuit Theory

```
  MAXWELL EQUATIONS (full)
  ∇·E = ρ/ε₀          (Gauss's Law: charge sources E field)
  ∇·B = 0              (no magnetic monopoles)
  ∇×E = -∂B/∂t         (Faraday: changing B induces E)
  ∇×B = µ₀J + µ₀ε₀∂E/∂t  (Ampere-Maxwell: current + changing E sources B)
         │
         │ Approximations for circuit theory:
         │ 1. Low frequency → ∂E/∂t negligible in Ampere → quasi-static
         │ 2. λ >> L_physical → fields uniform across lumped elements
         │ 3. Ohm's Law: J = σE inside conductors
         ▼
  CIRCUIT THEORY (lumped element)
  KVL: ΣV_loop = 0     (Faraday's Law integrated around a loop)
  KCL: ΣI_node = 0     (continuity equation at a node)
  V = IR, I = C·dV/dt, V = L·dI/dt

  Both KVL and KCL break at high frequency when:
  • Wire has significant inductance (di/dt effects, L = µ₀l/2π·ln(d/r))
  • Capacitance between traces causes crosstalk (C_parasitic = ε·A/d)
  • PCB trace delay becomes comparable to signal edge rate
    (rule of thumb: 5× rise time < trace propagation time → ringing)
```

---

## How the 8 Modules Connect

```
  MODULE DEPENDENCY MAP
  ─────────────────────────────────────────────────────────────────────────────

  ANALOG SIGNAL CHAIN (left-to-right signal flow)
  ┌──────────────┐  ┌──────────────┐  ┌───────────────┐  ┌──────────────────┐
  │ 01-CIRCUITS  │─▶│ 02-REACTIVE  │─▶│  03-FILTERS   │─▶│  04-AMPLIFIERS   │
  │ KVL/KCL      │  │ C, L, RLC    │  │ Bode, poles/  │  │ small-signal, FB │
  │ Thevenin     │  │ transients   │  │ zeros, design │  │ stability, noise │
  │ op-amp basic │  │ phasors      │  │               │  │                  │
  └──────────────┘  └──────────────┘  └───────────────┘  └──────────────────┘
         │                 │                  │                    │
         └─────────────────┴──────────────────┴────────────────────┘
                                      │
                              (prerequisites for)
                                      │
  SIGNAL PROCESSING THEORY            ▼
  ┌──────────────────┐  ┌─────────────────┐  ┌─────────────────────────────┐
  │ 05-SIGNALS-SYS   │─▶│   06-DSP        │─▶│      07-2D-DSP              │
  │ LTI, convolution │  │ sampling, DFT/  │  │ image processing, 2D-FFT    │
  │ Laplace, z-domain│  │ FFT, FIR/IIR   │  │ wavelets, compression       │
  └──────────────────┘  └─────────────────┘  └─────────────────────────────┘

  DIGITAL DOMAIN
  ┌────────────────────────────┐  ┌──────────────────────────────────────────┐
  │    08-DIGITAL-LOGIC        │─▶│           09-EMBEDDED-VLSI               │
  │ Boolean, gates, FSMs, FPGA │  │ MCU/RTOS/peripherals + RTL→tapeout flow  │
  └────────────────────────────┘  └──────────────────────────────────────────┘

  Bridge points:
  • 04→06: Analog anti-aliasing filter must be designed before ADC sampling rate set
  • 05↔06: Laplace (s-domain) ↔ z-domain: H(z) from H(s) via bilinear transform
  • 08→09: Digital logic IS the hardware substrate that VLSI implements
```

---

## Key Metrics Reference

| Metric | Symbol | Unit | What It Measures | Typical Range |
|--------|--------|------|------------------|---------------|
| Voltage gain | A_v | V/V or dB | Signal amplification | 1–120 dB |
| Current gain | A_i | A/A or dB | Current amplification | β = 50–500 (BJT) |
| Bandwidth | BW | Hz | Frequency range of flat response | kHz – GHz |
| Gain-bandwidth product | GBW | Hz | Op-amp figure of merit | 1 MHz – 10 GHz |
| Noise figure | NF | dB | SNR degradation by component | 0.5 – 20 dB |
| Signal-to-noise ratio | SNR | dB | Signal power / noise power | 20 – 120 dB |
| Spurious-free dynamic range | SFDR | dBc | Strongest spurious relative to carrier | 50 – 100 dBc |
| Total harmonic distortion | THD | % or dB | Nonlinearity measure | 0.001% – 10% |
| Input impedance | Z_in | Ω | Load presented to source | 50Ω – 1MΩ |
| Output impedance | Z_out | Ω | Source impedance presented to load | 0.1Ω – 10kΩ |
| Power supply rejection | PSRR | dB | Immunity to supply noise | 60 – 100 dB |
| Phase margin | PM | degrees | Stability margin in feedback | >45° desired |
| Sample rate | f_s | S/s | ADC/DAC conversion rate | kS/s – GS/s |
| ENOB | bits | bits | Effective number of bits (actual ADC quality) | 6 – 18 bits |

### dB Conversion Quick Reference

```
  Power ratio:  dB = 10·log₁₀(P₂/P₁)
  Voltage ratio: dB = 20·log₁₀(V₂/V₁)   [assuming equal impedances]

  Common values:
  +3 dB  = 2× power = 1.41× voltage
  +6 dB  = 4× power = 2× voltage
  +10 dB = 10× power = 3.16× voltage
  +20 dB = 100× power = 10× voltage
  -3 dB  = half power = 0.707× voltage  (the "-3 dB bandwidth" definition)
  -20 dB = 1/100 power = 1/10 voltage
  -40 dB = 1/10,000 power = 1/100 voltage
  0 dBm  = 1 mW into 50Ω → 0.224 V_rms
```

---

## Electronics in Computing Context

This is the domain where electronics and software engineering overlap most
directly. The abstractions that software engineers build on have physical
electrical substrates.

```
  COMPUTING ELECTRICAL CONCERNS
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  CPU / SoC Power Delivery                                               │
  │  ─────────────────────────────────────────────────────────────────────  │
  │  Voltage regulator module (VRM): buck converter, multi-phase           │
  │  Dynamic voltage/freq scaling (DVFS): V scales as √P → f              │
  │  Capacitor decoupling: handles transient current spikes (dI/dt)        │
  │  IR drop: ΔV = I·R_trace on power plane → core gets less than nominal │
  │  AMD Zen4 @ 1.1V, 95W TDP: ~86A peak current, needs µF capacitors     │
  │  within mm of die for <1ns transient response                          │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  PCB Signal Integrity (SI)                                              │
  │  ─────────────────────────────────────────────────────────────────────  │
  │  PCIe 5.0 (32 GT/s): signal edges at ~20ps → 10 GHz content           │
  │  Trace impedance control: Z₀ = √(L/C), target 50Ω or 100Ω diff        │
  │  Skin effect: current crowds to surface at high f; R ∝ √f             │
  │  Via stubs: reflected energy at stub resonant frequency                │
  │  Crosstalk: NEXT (near-end) vs FEXT (far-end); tight diff pairs avoid │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  DDR Memory Electrical                                                  │
  │  ─────────────────────────────────────────────────────────────────────  │
  │  DDR5: 4800–6400 MT/s; 1.1V; differential clocking (CK/CK#)           │
  │  On-die termination (ODT): absorbs reflections, controlled in software │
  │  Write leveling, read/write training: MCU adjusts timing per-DIMM      │
  │  Eye diagram: intersection of all bit transitions — must clear mask    │
  └─────────────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Thermal Management                                                     │
  │  ─────────────────────────────────────────────────────────────────────  │
  │  Thermal resistance θ_JA: °C/W from junction to ambient                │
  │  T_junction = T_ambient + P_dissipated × θ_JA                         │
  │  Modern CPUs: max T_j = 100°C; throttle before damage                  │
  │  Capacitor reliability: every 10°C above rated → 2× failure rate       │
  └─────────────────────────────────────────────────────────────────────────┘
```

---

## RF/Microwave Bridge — When Lumped Models Break

Above ~300 MHz, circuit dimensions approach the signal wavelength and the lumped-element model fails. The replacement framework is **scattering parameters (S-parameters)** — the RF equivalent of Thévenin/Norton, but describing incident and reflected power waves at each port rather than voltage and current.

```
  S-PARAMETER FRAMEWORK (2-port example)
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Incident power a₁ → [DUT] → Transmitted power b₂                      │
  │  Reflected power b₁ ←        ← Incident power a₂                      │
  │                                                                         │
  │  S₁₁ = b₁/a₁  (reflection at port 1 = "return loss")                  │
  │  S₂₁ = b₂/a₁  (forward transmission = "gain" or "insertion loss")     │
  │  S₁₂ = b₁/a₂  (reverse isolation)                                     │
  │  S₂₂ = b₂/a₂  (reflection at port 2)                                  │
  │                                                                         │
  │  Measured with a vector network analyzer (VNA) at 50Ω reference.       │
  │  Smith chart: graphical tool mapping complex S₁₁ to impedance plane.   │
  │                                                                         │
  │  Modern wireless relevance:                                             │
  │  WiFi 6E (6 GHz):   antenna S₁₁ < -10 dB over 5.925–7.125 GHz band   │
  │  5G FR2 (mmWave):   phased array with per-element S-param calibration  │
  │  Bluetooth (2.4 GHz): matching network designed via Smith chart         │
  │  PCIe 5.0 (32 GT/s): S₂₁ insertion loss budget < 30 dB at 16 GHz     │
  └─────────────────────────────────────────────────────────────────────────┘
```

Impedance matching in RF replaces the Thévenin max-power-transfer condition: conjugate match Z_L = Z_S* maximizes power delivered to load, and the matching network (LC, stub, or microstrip) serves the same role as a Thévenin equivalent — transforming an arbitrary impedance to the 50Ω system impedance.

---

## What Is NOT in This Directory

| Domain | Why excluded | Where to look |
|--------|-------------|----------------|
| Power electronics | Inverters, SMPS, motor drives — specialized discipline | separate power-electronics directory |
| RF/microwave design | S-parameters, Smith chart, transmission line theory | telecom / RF modules |
| Full VLSI design flow | Partially in 09; deep dive in semiconductor-manufacturing/ | semiconductor-manufacturing/ |
| Analog IC design | Full custom (not covered): bandgap references, PLLs, ADC architectures | EE textbooks (Razavi) |
| Electromagnetic compatibility (EMC) | FCC/CE compliance, shielding, ferrite beads | EMC standards references |
| Power distribution networks | Grid-scale power systems | electrical-grid/ |

---

## Decision Cheat Sheet

| You want to understand... | Go to module |
|--------------------------|-------------|
| Kirchhoff's laws, op-amp fundamentals, transistor operation | 01-CIRCUITS |
| Capacitor/inductor behavior, RC/LC transients, phasors | 02-REACTIVE |
| Filter design, Bode plots, pole-zero analysis | 03-FILTERS |
| Amplifier gain, bandwidth, noise, stability in feedback | 04-AMPLIFIERS |
| LTI systems, convolution, Laplace/z-domain theory | 05-SIGNALS-SYSTEMS |
| Sampling theorem, FFT, FIR/IIR filter design, quantization | 06-DSP |
| Image processing, 2D convolution, wavelets, compression | 07-2D-DSP |
| Boolean logic, flip-flops, FSMs, FPGA architecture, HDL | 08-DIGITAL-LOGIC |
| MCU programming, RTOS, peripheral interfaces, VLSI flow | 09-EMBEDDED-VLSI |
| PCIe/DDR electrical specs, power delivery, signal integrity | This overview |

---

## Common Confusion Points

**Bandwidth means different things in different contexts.**
Filter bandwidth: frequency range passing through. Amplifier bandwidth: -3 dB
frequency. Channel bandwidth: data rate capacity (Shannon). ADC bandwidth:
highest input frequency the ADC can accurately digitize (Nyquist = f_s/2).

**dB is always a ratio, not an absolute.**
"The gain is 20 dB" means the output is 10× the input voltage. "The signal
is at -80 dBm" uses dBm which IS absolute (referenced to 1 mW). Always check
what the reference is: dBm (1 mW), dBV (1 V), dBu (0.775 V), dBFS (full-scale).

**Lumped element model silently fails at high frequency.**
A 100 nH inductor at 100 MHz has impedance jω·L ≈ 63 Ω — significant. At 1 GHz,
it may self-resonate (parasitic C) and act like a capacitor. A 10 cm trace on
a 2-layer PCB has ~8 nH/cm inductance; at 500 MHz, 80 nH × 3.14 GHz = 251 Ω.
If your signal integrity simulation gives non-physical results, check parasitic
models of passives.

**SNR vs SFDR vs ENOB — three different quality metrics for ADCs.**
SNR includes thermal noise. SFDR is the worst spurious tone, usually from
nonlinearity causing harmonics. ENOB = (SINAD - 1.76) / 6.02 is the overall
quality metric. A "16-bit ADC" may have only 14 ENOB at high frequency because
aperture jitter and nonlinearity degrade SNR as f_in increases.

**Ground is not "zero volts" on a PCB.**
Ground is a node, and every real trace has inductance (≈1 nH/mm). A ground
plane with high-frequency return currents has local voltage variations. This
is why analog and digital grounds are often split and joined at a single point,
and why bypass capacitors must be placed close to the IC, not the "nearest
available pad."
