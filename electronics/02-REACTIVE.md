# 02 — Reactive Components: Capacitors, Inductors, RLC

```
REACTIVE LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Energy storage elements — they remember. Resistors dissipate; these store.

  INDIVIDUAL ELEMENTS
  ┌──────────────────────────────┐    ┌──────────────────────────────┐
  │  Capacitor C                 │    │  Inductor L                  │
  │  Stores E-field: W = ½CV²   │    │  Stores B-field: W = ½LI²   │
  │  I = C dV/dt                 │    │  V = L dI/dt                 │
  │  Z_C = 1/(sC)  — falls w/ ω │    │  Z_L = sL   — rises w/ ω   │
  └──────────────┬───────────────┘    └──────────────┬───────────────┘
                 │                                    │
                 ▼                                    ▼
  COMBINATIONS: Series/parallel rules (§1-2), mutual inductance (§2)
                 │
                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  RLC CIRCUITS — energy exchanges between C and L                 │
  │  Natural frequency ω₀ = 1/√(LC)    Q = ω₀L/R = 1/(2ζ)         │
  │  Damping ζ controls: oscillation (ζ<1) vs exponential decay (ζ>1)│
  │  Characteristic equation roots = s-domain poles (§3-4)          │
  └──────────────────────────────┬───────────────────────────────────┘
                                 │
                                 ▼
  ┌──────────────────────────────────────────────────────────────────┐
  │  RESONANCE & FILTERING — frequency selectivity (§5-6)           │
  │  High Q → narrow bandpass, voltage magnification                │
  │  → Foundation for filter design (03-FILTERS)                    │
  └──────────────────────────────────────────────────────────────────┘

  6.002/6.003 bridge: RLC is where circuit analysis meets differential equations
  and s-domain analysis becomes essential.
```

---

## 1. Capacitors

### Basic Relations

```
  Charge:    Q = CV
  Current:   I = C dV/dt    (current proportional to rate of voltage change)
  Voltage:   V(t) = (1/C)∫₀ᵗ I(τ)dτ + V(0)

  Energy stored:  W = ½CV²
  Power:          P = VI = CV·(dV/dt)

  Key behavior:
    DC steady state: I = 0  (capacitor is open circuit at DC)
    Instantaneous voltage change requires infinite current
    Acts as short circuit at high frequency (Z → 0 as ω → ∞)
```

### Impedance in s-Domain

```
  Z_C(s) = 1/(sC)
  Z_C(jω) = 1/(jωC) = -j/(ωC)
  |Z_C| = 1/(ωC)      decreases with frequency
  ∠Z_C = -90°         current leads voltage by 90°
```

### Capacitor Combinations

```
  Series:    1/C_eq = 1/C₁ + 1/C₂ + ...    (opposite of resistors)
  Parallel:  C_eq = C₁ + C₂ + ...           (same direction as resistors)

  Mnemonic: capacitors in parallel add (like resistors in series — both add V to same node)
```

### Physical Types

| Type | Capacitance | Polarized? | Frequency | Use |
|---|---|---|---|---|
| Ceramic (MLCC) | pF–μF | No | High | Decoupling, RF |
| Electrolytic | μF–mF | Yes | Low | Bulk bypass, filtering |
| Tantalum | μF | Yes | Medium | Compact bulk bypass |
| Film (polyester/polypropylene) | nF–μF | No | Medium-High | Audio, precision |
| Mica | pF–nF | No | Very High | RF precision |

**Decoupling/bypass**: Place ceramic caps (100nF) close to IC power pins. Suppresses high-frequency supply noise. Electrolytic caps handle low-frequency bulk energy.

---

## 2. Inductors

### Basic Relations

```
  Magnetic flux: Φ = LI
  Voltage:       V = L dI/dt    (voltage proportional to rate of current change)
  Current:       I(t) = (1/L)∫₀ᵗ V(τ)dτ + I(0)

  Energy stored: W = ½LI²
  Power:         P = VI = LI·(dI/dt)

  Key behavior:
    DC steady state: V = 0  (inductor is short circuit at DC)
    Instantaneous current change requires infinite voltage
    Acts as open circuit at high frequency (Z → ∞ as ω → ∞)
    Real inductors: resistance R_L (wire resistance) + parasitic capacitance
```

### Impedance in s-Domain

```
  Z_L(s) = sL
  Z_L(jω) = jωL
  |Z_L| = ωL      increases with frequency
  ∠Z_L = +90°    voltage leads current by 90°
```

### Mutual Inductance (Transformers)

```
  Two coils with mutual inductance M:
    V₁ = L₁ dI₁/dt + M dI₂/dt
    V₂ = M dI₁/dt + L₂ dI₂/dt

  Coupling coefficient: k = M/√(L₁L₂),  0 ≤ k ≤ 1
  k=1: perfect coupling (ideal transformer)

  Ideal transformer: turns ratio n = N₂/N₁
    V₂/V₁ = n
    I₂/I₁ = 1/n     (power conserved)
    Z₁ = Z₂/n²      (impedance transformation)
```

### Real Inductor Effects

```
  Self-resonant frequency (SRF):
    Parasitic capacitance C_p in parallel with L.
    Acts like inductor only for ω << ω_SRF = 1/√(LC_p)
    Above SRF: capacitive! Inductor becomes useless as intended component.

  Core saturation:
    Ferrite/iron core inductors: L decreases when I exceeds rating.
    Air-core inductors: L stable regardless of I but lower inductance.

  Q factor of inductor: Q = ωL/R_series
    Higher Q = lower loss. Matters in resonant circuits.
```

---

## 3. Series RLC Circuit

**Pole-zero connection:** The characteristic equation roots s₁,₂ = -ζω₀ ± ω₀√(ζ²-1) are exactly the s-domain poles of the circuit's transfer function H(s). Overdamped (ζ > 1) = two real poles on the negative real axis. Critically damped (ζ = 1) = repeated real pole. Underdamped (ζ < 1) = complex conjugate pole pair. This is the same pole-zero framework developed fully in 05-SIGNALS-SYSTEMS — the RLC circuit is the physical system that makes poles tangible.

```
    Vs ──R──L──C──┐
                   │
                  GND

  Differential equation:
    L·d²i/dt² + R·di/dt + (1/C)i = dVs/dt

  Characteristic equation (set Vs=0, i = e^(st)):
    Ls² + Rs + 1/C = 0
    s² + (R/L)s + 1/LC = 0
    s² + 2ζω₀s + ω₀² = 0

  where:
    ω₀ = 1/√(LC)        natural frequency (rad/s)
    ζ = R/(2√(L/C)) = R/(2L·ω₀)  damping ratio
    Q = ω₀L/R = 1/(2ζ) = (1/R)√(L/C)    quality factor
```

### Three Cases

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  ζ > 1  (Q < 0.5)  OVERDAMPED                                       │
  │    s₁,₂ = -ζω₀ ± ω₀√(ζ²-1)   (two real negative poles)           │
  │    i(t) = A₁e^(s₁t) + A₂e^(s₂t)                                   │
  │    No oscillation. Exponential decay. Slow response.               │
  │                                                                     │
  │  ζ = 1  (Q = 0.5)  CRITICALLY DAMPED                               │
  │    s₁,₂ = -ω₀   (repeated pole)                                    │
  │    i(t) = (A₁ + A₂t)e^(-ω₀t)                                      │
  │    Fastest decay without oscillation. Optimal for step response.   │
  │                                                                     │
  │  ζ < 1  (Q > 0.5)  UNDERDAMPED                                     │
  │    s₁,₂ = -ζω₀ ± jω_d   where ω_d = ω₀√(1-ζ²)  (damped freq)    │
  │    i(t) = e^(-ζω₀t)[A·cos(ω_d t) + B·sin(ω_d t)]                 │
  │    Oscillates at ω_d with decaying envelope.                       │
  │    Overshoot in step response.                                     │
  └─────────────────────────────────────────────────────────────────────┘

  Physical intuition:
    L↑ or C↑ → ω₀ down (slower oscillation, more inertia)
    R↑ → ζ up (more damping, dissipates energy faster)
    High Q ↔ low damping ↔ rings for a long time
```

---

## 4. Parallel RLC Circuit

```
       Is ──┬──R──┬──L──┬──C──┐
            │     │     │     │
           GND   GND   GND   GND

  Same natural frequency ω₀ = 1/√(LC)
  Different Q:  Q = R/√(L/C) = Rω₀C = R/(ω₀L)   (note: R in parallel → higher R = higher Q)
  ζ = 1/(2Q) = √(L/C)/(2R) = 1/(2Rω₀C)

  Series vs parallel:
    Series RLC: higher R → more damping (lower Q)
    Parallel RLC: higher R → less damping (higher Q)
    Physical: in parallel, R shunts current from LC tank; large R = less current shunted = less loss
```

---

## 5. Q Factor — Quality Factor

```
  Q = 2π · (energy stored) / (energy lost per cycle) = ω₀ · W_stored / P_dissipated

  For resonant circuits:
    Q = ω₀ / Δω   where Δω = 3dB bandwidth of resonance peak

  High Q → narrow resonance peak → selective filter
  Low Q  → wide resonance peak → broadband

  ┌────────────────────────────────────────────────────────────────────┐
  │           |H(jω)|                                                  │
  │              │ ← Q=10 (tall, narrow)                              │
  │              │                                                     │
  │         ─── │ ──── Q=1 (shorter, wider)                           │
  │    ─────────┼─────────── Q=0.5 (no peak)                         │
  │             ω₀    ω→                                              │
  └────────────────────────────────────────────────────────────────────┘

  Typical Q values:
    Power inductor: Q ~ 20–100
    Crystal oscillator: Q ~ 10⁴–10⁶
    Atomic clock resonator: Q ~ 10¹⁰
    LC filter for RF: Q ~ 100–500
    Active RC filter: Q as designed (no real energy storage)
```

---

## 6. Frequency Response of RLC Filters

### Series RLC Voltage Output

```
  H(s) = V_out/V_in depends on which element you take V_out across:

  Across R:  H_R(s) = sRC/(s²LC + sRC + 1)   → Bandpass  (peak at ω₀)
  Across C:  H_C(s) = 1/(s²LC + sRC + 1)      → Low-pass  (−40dB/dec above ω₀)
  Across L:  H_L(s) = s²LC/(s²LC + sRC + 1)   → High-pass (−40dB/dec below ω₀)

  Standard 2nd-order LP form:
    H(s) = ω₀²/(s² + 2ζω₀s + ω₀²)
    = ω₀²/(s² + (ω₀/Q)s + ω₀²)

  Frequency response at resonance ω = ω₀:
    H_R(jω₀) = 1                   (R gets all the voltage — max for bandpass)
    H_C(jω₀) = jQ                  (capacitor voltage = Q × source voltage!)
    H_L(jω₀) = -jQ                 (inductor voltage = Q × source voltage!)
    → In high-Q circuit, inductor and capacitor have large voltages that cancel.
```

### Resonance and Impedance

```
  Series RLC total impedance: Z(jω) = R + jωL + 1/(jωC) = R + j(ωL - 1/(ωC))

  At resonance: ωL = 1/(ωC)  →  Z = R  (purely resistive)
  Below ω₀: capacitive  (imaginary part < 0)
  Above ω₀: inductive   (imaginary part > 0)

  Parallel RLC admittance: Y(jω) = 1/R + jωC + 1/(jωL) = 1/R + j(ωC - 1/(ωL))
  At resonance: Y = 1/R  →  Z = R  (impedance maximum for parallel)
```

---

## 7. Step Response and Transients

```
  Series RLC step response (switch closes at t=0, drives step Vs):

  Energy stored initially?  → ICs determine A₁, A₂ in solution.
  Common case: i(0) = 0, V_C(0) = 0 (uncharged capacitor, no initial current).

  Underdamped step (ζ < 1):
    V_C(t) = Vs[1 - e^(-ζω₀t)(cos(ω_d t) + (ζ/√(1-ζ²))sin(ω_d t))]
    Overshoot: M_p = e^(-πζ/√(1-ζ²))
      ζ=0.5:   M_p ≈ 16%
      ζ=0.707: M_p ≈ 4.3%  (Butterworth — common design target)

  Settling time (to within 2%): t_s ≈ 4/(ζω₀)
  Rise time (10% to 90%): t_r ≈ 1.8/ω_d   (approx for underdamped)

  Energy analysis during step:
    Source provides ½CV_s² to capacitor + ½CV_s² dissipated in R.
    Only half the energy reaches the capacitor, regardless of R!
    (This is why CMOS logic power P = ½CV²f — charging/discharging caps)
```

---

## 8. Practical LC Design

```
  Choose ω₀ and Q:
    ω₀ = 1/√(LC)   →  once ω₀ fixed, LC product determined
    Q = ω₀L/R       →  pick L and C to give desired LC product and Q

  Example: 10 MHz bandpass filter, Q=50, R=50Ω
    ω₀ = 2π × 10⁷ rad/s
    L = QR/ω₀ = 50 × 50 / (2π × 10⁷) ≈ 40 μH
    C = 1/(ω₀²L) ≈ 6.3 pF

  Bandwidth: Δf = f₀/Q = 10 MHz / 50 = 200 kHz

  Parasitic effects:
    Inductor wire resistance R_L adds series loss → degrades Q
    Capacitor ESR (equivalent series resistance) → degrades Q
    Actual Q ≈ Q_design only if R_L, ESR << R

  Above SRF of inductor → element no longer inductive → design breaks.
  Keep operating frequency well below SRF of all components.
```

---

## 9. Decision Cheat Sheet

| Situation | What you need |
|---|---|
| AC circuit, find voltages/currents at one frequency | Z_R=R, Z_L=jωL, Z_C=1/(jωC), then KVL/KCL |
| Full frequency response, find H(jω) | Build H(s) via impedances, evaluate on jω axis |
| Time domain transient, ICs given | Laplace transform with ICs, partial fractions, inverse |
| Characterize resonance | Find ω₀, Q, ζ. Determine over/under/critically damped |
| Fast step response, no overshoot | Critically damped (ζ = 1) |
| Narrow frequency selection (filter) | High Q resonance, ζ << 1 |
| Energy storage per unit voltage | Capacitor (W = ½CV²) |
| Energy storage per unit current | Inductor (W = ½LI²) |
| Block DC, pass AC | Series capacitor |
| Block high-frequency noise on supply | Shunt capacitor to ground (bypass) |
| Inductors in series | Add L values (like resistors) |
| Capacitors in parallel | Add C values (opposite of resistors) |

---

## 10. Common Confusion Points

**1. Capacitor current and voltage: which leads?**
V_C cannot change instantaneously (needs time to charge). I_C = C dV_C/dt. In AC: current *leads* voltage by 90°. Remember: "ELI the ICE man" — in an inductor (L), E (voltage) leads I (current); in a capacitor (C), I leads E (voltage).

**2. Series vs parallel Q are different formulas**
Series RLC: Q = ω₀L/R = 1/(ω₀RC). Parallel RLC: Q = Rω₀C = R/(ω₀L). Higher resistance increases Q in parallel (less energy stolen by R), but decreases Q in series. Don't mix them up.

**3. Resonance is NOT necessarily the peak of |H(jω)|**
For a 2nd-order bandpass, the peak does occur at ω₀. But for 2nd-order LP, the peak frequency is ω_peak = ω₀√(1-2ζ²) < ω₀ for ζ < 1/√2. Only for high Q is ω_peak ≈ ω₀. At ζ ≥ 1/√2 (Q ≤ 1/√2), the LP has no peak — monotonically decreasing.

**4. At resonance, capacitor voltage can exceed source voltage**
V_C = Q × V_source in a series RLC at resonance. High-Q circuits have enormous voltages across L and C internally, even while input appears resistive. This matters for component voltage ratings and for LC filter design in RF.

**5. The CMOS power equation**
P = αCV²f (activity factor α, capacitance C, supply voltage V, frequency f) derives from the RLC step analysis: each clock cycle charges then discharges C, dissipating CV²/2 on charge and CV²/2 on discharge. It's not an RLC oscillation phenomenon — it's fundamental charge/discharge energy loss.

**6. Inductor current can't change instantly — but voltage can be huge**
When you open a switch in series with an inductor carrying current I, the inductor tries to maintain I by generating whatever voltage is needed: V = L dI/dt. With a fast switch, dI/dt is huge → spark or arc. This is why relay coil snubbers and flyback diodes are required in circuits with inductive loads.
