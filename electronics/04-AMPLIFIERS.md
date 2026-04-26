# 04 — Amplifiers: BJT, MOSFET, Differential Pair, Feedback

```
AMPLIFIER LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  DEVICE MODELS               CONFIGURATIONS             FEEDBACK
  ─────────────────────────   ─────────────────────────  ─────────────────────
  BJT: NPN/PNP                Common emitter (CE)        Negative: stabilizes
    I_C = β·I_B                 High gain                  Reduces Rin, Rout
    I_C = I_S e^(V_BE/V_T)     High R_in (hfe topology)   Increases BW
                              Common base (CB)           Positive: oscillates
  MOSFET: NMOS/PMOS             Low R_in, high freq         or clips
    I_D = ½μnCox(W/L)(Vgs-Vth)² Common collector (CC)   Miller effect
    Vgs controls I_D             Follower, gain<1, low Rout  frequency limitation

  Small-signal model:          Differential pair          Op-amp = macromodel
    BJT: g_m, r_π, r_o          Tail current source           of amplifier
    MOSFET: g_m, r_o            CMRR, high gain               principles

  6.012 bridge: Device physics behind BJT/MOSFET. This module uses
  behavioral models — physics is the course you haven't taken.
```

---

## 1. BJT — Bipolar Junction Transistor

### Physical Operation (Behavioral Model)

```
  NPN BJT:
    Base-Emitter junction forward biased (like diode, ~0.7V)
    Collector-Base junction reverse biased
    Small I_B controls large I_C

  Active region (linear amplifier):
    I_C = β·I_B        (β = hFE = current gain, typically 50–300)
    I_E = I_C + I_B = (β+1)·I_B
    V_BE ≈ 0.6–0.7 V  (forward biased junction)
    V_CE > V_CE_sat   (keep out of saturation for linear operation)

  Exact (Ebers-Moll, active region):
    I_C = I_S · e^(V_BE/V_T)
    V_T = kT/q ≈ 26 mV at room temperature  (thermal voltage)
    → Exponential relationship!

  Transconductance:
    g_m = dI_C/dV_BE = I_C/V_T    (at operating point I_C)
    At I_C = 1 mA: g_m = 1/(26 mV) ≈ 38.5 mA/V
    g_m proportional to bias current — key design parameter.
```

### Small-Signal Model (π-model)

```
  For AC analysis: replace BJT with linear equivalent at operating point.

           B        C
           │        │
           ├──r_π───┤
           │        ├── g_m·v_π (current source)
           │        │
           └────────┴── r_o
                    │
                    E

  r_π = β/g_m = V_T·β/I_C   (input resistance)
  g_m = I_C/V_T              (transconductance)
  r_o = V_A/I_C              (output resistance, V_A = Early voltage ~50–100V)

  Finding the operating point:
    1. Ignore AC sources, set to DC values
    2. Assume V_BE = 0.7V for NPN
    3. Find I_C from DC circuit (KVL with V_BE = 0.7V)
    4. Compute g_m, r_π, r_o at that I_C
```

---

## 2. MOSFET — Field Effect Transistor

### Physical Operation (Behavioral Model)

```
  NMOS (n-channel):
    Gate-Source voltage V_GS creates channel under gate oxide.
    Drain current I_D flows when V_GS > V_th (threshold voltage).

  Operating regions:
    Cutoff (V_GS < V_th):      I_D = 0
    Linear/Triode (V_GS-V_th > V_DS > 0):
      I_D = μnCox(W/L)[(V_GS-V_th)V_DS - V_DS²/2]
      Acts like voltage-controlled resistor.
    Saturation (V_DS ≥ V_GS-V_th):
      I_D = ½μnCox(W/L)(V_GS-V_th)²    ← quadratic, not exponential!
      Current independent of V_DS (approximately).

  Key difference from BJT:
    BJT: exponential V_BE → I_C, base current required
    MOSFET: quadratic V_GS → I_D, gate current ≈ 0 (capacitive input)
    MOSFET advantage: zero DC gate current, easier biasing
```

### MOSFET Small-Signal Model

```
         G          D
         │          │
         ├──────────┤
         │     g_m·v_gs (current source)
         │          │
         │          r_o
         │          │
         └──────────┴
                    S

  g_m = dI_D/dV_GS = μnCox(W/L)(V_GS-V_th) = √(2μnCox(W/L)I_D)
  r_o = 1/(λI_D)   where λ = channel-length modulation parameter

  Note: MOSFET g_m is typically lower than BJT g_m at same current.
  MOSFET threshold V_th: 0.3–1V (depends on process, adjustable by bias)
```

### BJT vs MOSFET Comparison

| Property | BJT | MOSFET |
|---|---|---|
| Control | Base current I_B | Gate voltage V_GS |
| Input | Low-Z (r_π) | Very high-Z (capacitive) |
| Current eq | Exponential I_C = I_S e^(V_BE/V_T) | Quadratic I_D ∝ (V_GS-V_th)² |
| g_m at same I | Higher (g_m = I_C/V_T) | Lower (g_m ∝ √I_D) |
| V_BE/V_GS-V_th | ~0.7V (fixed) | 0.3–1V (adjustable) |
| DC bias power | V_BE × I_B wasted | No gate current |
| Matching | Good | Excellent (digital VLSI) |
| Speed | High (bipolar process) | High (submicron CMOS) |
| Use case | RF, precision analog | Digital VLSI, power, CMOS analog |

---

## 3. Single-Transistor Amplifier Configurations

### Common Emitter (CE) — BJT Voltage Amplifier

```
  VCC
   │
   R_C ──── V_out
   │
  (C)──── V_out
  (B)──── V_in (via coupling cap)
  (E)────[R_E]── GND (bypass C_E to GND for AC)

  Small-signal (with emitter bypass cap, so r_e = 0):
    A_v = V_out/V_in = -g_m · (r_o || R_C) ≈ -g_m · R_C
    R_in = R_B1 || R_B2 || r_π                (bias resistors in parallel)
    R_out = r_o || R_C ≈ R_C

  Without emitter bypass (R_E in small-signal path):
    A_v = -g_m R_C / (1 + g_m R_E) ≈ -R_C/R_E
    R_in = R_B || (r_π + (β+1)R_E)            (much higher input resistance)
    Gain stabilized (less sensitive to β variation) ← this is local feedback
```

### Common Base (CB)

```
  Low input impedance (~1/g_m), high output impedance, non-inverting.
  Voltage gain ≈ g_m·R_C.
  No Miller effect (base is AC ground between input and output).
  Use for: high-frequency, RF (no input-output capacitance coupling).
```

### Common Collector (CC) — Emitter Follower

```
  R_out = r_π/β + R_source/β ≈ 1/g_m   (low)
  R_in = r_π + (β+1)R_E                 (very high)
  A_v ≈ 1 (slightly less)

  Use for: impedance buffer (matches high-Z source to low-Z load)
  Emitter follower = BJT version of op-amp voltage follower
```

### MOSFET Equivalent Configurations

| BJT | MOSFET | Properties |
|---|---|---|
| Common emitter | Common source | Inverting voltage gain, medium Rin |
| Common base | Common gate | Low Rin, high-freq, non-inverting |
| Common collector | Common drain (source follower) | Buffer, gain≈1, low Rout |

---

## 4. Differential Pair

```
  The building block of all op-amps and precision analog circuits.

        VCC
         │
      ┌──┴──┐
     R_C   R_C
      │     │
  V_out2   V_out1
      │     │
     (C₁)  (C₂)    Q1, Q2: matched transistors
     (B₁)  (B₂)
     V_in1  V_in2
     (E₁)  (E₂)
       └──┬──┘
          │
         I_EE (tail current source)
          │
         GND

  Differential input: V_id = V_in1 - V_in2
  Common-mode input:  V_ic = (V_in1 + V_in2)/2

  Operation:
    Tail current I_EE is fixed (from current source).
    V_id → 0: I_EE splits equally, V_out1 = V_out2
    V_id → positive: Q1 steals current from Q2
    V_id large positive: Q1 takes all I_EE, Q2 cuts off (saturated diff amp)
    Transfer characteristic: I_C1-I_C2 = I_EE·tanh(V_id/(2V_T))  [for BJT]
```

### Small-Signal Analysis

```
  Half-circuit concept: split into two independent circuits.
    Differential mode: tail current source → open circuit for differential
    Common mode: tail current source → 2·r_ee (resistance to GND)

  Differential gain:
    A_d = -g_m · R_C         (same as single CE with R_C as load)

  Common-mode gain:
    A_c = -R_C / (2·r_ee + 1/g_m)  ← small when r_ee large
    With ideal current source r_ee → ∞: A_c → 0

  CMRR = |A_d/A_c| = g_m · 2·r_ee = 2·g_m·r_ee  ← want large
    High CMRR → rejects noise common to both inputs.
    Op-amp spec: CMRR typically 80–120 dB.
```

---

## 5. Feedback

### The Four Feedback Topologies

```
  Negative feedback in amplifiers: sense output, subtract from input.

  What you sense (at output):  V or I
  How you feed back (at input): V (series) or I (shunt)

  ┌──────────────────────────────────────────────────────────────────────┐
  │  Topology         Sense    Feed    Effect on              Gain       │
  │                   output   back    Rin    Rout            stability  │
  ├──────────────────────────────────────────────────────────────────────┤
  │  Series-Shunt     V        V       Up     Down     A_v (V→V)  stable │
  │  (non-inverting)                                                     │
  │  Series-Series    I        V       Up     Up       A_i (V→I) stable  │
  │  Shunt-Shunt      V        I       Down   Down     Z (I→V)   stable  │
  │  (transresistance)                                                   │
  │  Shunt-Series     I        I       Down   Up       A_i (I→I) stable  │
  └──────────────────────────────────────────────────────────────────────┘

  Summary:
    Sense voltage → Rout decreases (good voltage source)
    Series subtraction → Rin increases (good voltage input)
    Feed back current → Rin decreases (good current input)
    Series injection → Rout increases (good current source)
```

### Feedback Equations

```
  Open-loop gain: A   (can be very large and variable)
  Feedback factor: β   (stable, set by resistors)
  Loop gain: T = Aβ

  Closed-loop gain:  A_f = A/(1 + Aβ) ≈ 1/β   (for T >> 1)

  Gain sensitivity:  dA_f/A_f = (1/(1+Aβ)) · dA/A
    Error in A reduced by factor (1+Aβ).
    Feedback trades gain for gain stability.

  Bandwidth:   BW_f = BW_open · (1+Aβ)
    Gain-bandwidth product preserved.
    Op-amp: A × BW = GBW product (constant), so reducing gain increases BW.

  Non-linearity: reduced by (1+T) — feedback linearizes.
  Noise: input-referred noise unchanged; output noise reduced.
```

### Stability and the Miller Effect

```
  BODE PLOT EXAMPLE: TWO-POLE SYSTEM — LOOP GAIN Aβ(jω)

  |Aβ| (dB)     Phase of Aβ
  60│──.                           0°│──────────────.
    │   ╲  -20 dB/dec                │                ╲
  40│    ╲                        -45°│                 ╲
    │     ╲                          │                   ╲
  20│      ╲  p₁                 -90°│        ╲           ╲
    │       ·─── -40 dB/dec          │         ╲           ╲
   0│─ ─ ─ ─╲─ gain crossover  -135°│          ╲  p₂       ╲
    │    ωgc  ╲  (|Aβ|=1)           │           ·────────────╲
 -20│          ╲            PM -180°│─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ ─ (oscillation)
    └───────────────→ ω              └───────────────────────→ ω
              p₂                            ωgc
                                       PM = 180° + phase(Aβ) at ωgc

  Phase margin vs step response:
    PM ≈ 75°:  no overshoot, slow response
    PM ≈ 60°:  ~5% overshoot, well-damped
    PM ≈ 45°:  ~23% overshoot, slight ringing — minimum acceptable
    PM ≈ 20°:  severe ringing, near-oscillation
    PM ≤ 0°:   unstable — sustained oscillation

  Mapping to pole locations (closed-loop):
    PM ≈ 60° → ζ ≈ 0.6 → complex poles well into LHP
    PM ≈ 45° → ζ ≈ 0.45 → poles closer to jω axis, more ringing
    PM < 0°  → poles cross into RHP → unstable
```

```
  Stability:
    Negative feedback → phase shift at high frequency → becomes positive feedback.
    If loop gain > 1 at the frequency where phase = 180°: oscillation.

    Phase margin PM = 180° + ∠(A(jω)β) at gain crossover (|Aβ|=1)
    PM > 0°: stable. PM > 45°: well-damped.

  Miller Effect:
    Capacitor C across inverting amplifier with gain -A:
    Input capacitance = C(1+A)  ← appears much larger!

    Why: if input voltage changes by 1V, output changes by -A volts.
    Capacitor sees A+1 volts change → draws A+1 times as much current.
    Effective C_in = C_f(1+A).

    Problem: limits bandwidth of common-emitter and common-source amps.
    Fix: cascode topology puts common-base/gate stage between C and E/S.
      Common-base has low impedance input → Miller multiplier ≈ 1.
```

---

## 6. Amplifier Noise — The Information-Theoretic Floor

Every amplifier adds noise to the signal, setting a fundamental limit on recoverable information. Noise analysis completes the gain–bandwidth–stability triad.

```
  NOISE SOURCES IN AMPLIFIERS
  ┌────────────────────────────────────────────────────────────────────────────┐
  │  Johnson-Nyquist (thermal):  v_n² = 4kTRΔf                              │
  │    k = 1.38×10⁻²³ J/K, T = temperature (K), R = resistance, Δf = BW    │
  │    At 300K, 1 kΩ, 1 Hz BW: v_n = 4.07 nV/√Hz                           │
  │    → Every resistor is a noise source. R_source noise → amplifier input. │
  │                                                                            │
  │  Shot noise:  i_n² = 2qI_DC Δf                                           │
  │    q = 1.6×10⁻¹⁹ C, I_DC = DC bias current                              │
  │    Dominant in BJT base current and photodiode dark current.               │
  │                                                                            │
  │  Flicker (1/f):  S(f) ∝ 1/f                                              │
  │    Dominant below corner frequency f_c (1 Hz – 10 kHz depending on tech).  │
  │    CMOS has higher 1/f noise than BJT — matters for DC precision amps.     │
  └────────────────────────────────────────────────────────────────────────────┘

  NOISE FIGURE AND SIGNAL CHAIN
  ┌────────────────────────────────────────────────────────────────────────────┐
  │  Noise figure NF = 10 log₁₀(SNR_in / SNR_out) [dB]                      │
  │  NF = 0 dB → noiseless amplifier (impossible; ≥ 0.5 dB for best LNAs)   │
  │                                                                            │
  │  Friis cascade formula (N stages):                                         │
  │    NF_total = NF₁ + (NF₂-1)/G₁ + (NF₃-1)/(G₁G₂) + ...                 │
  │    → First stage dominates! Low-noise amplifier (LNA) must be first.     │
  │                                                                            │
  │  Information-theoretic connection:                                         │
  │    Shannon capacity: C = B log₂(1 + SNR)  [bits/s]                       │
  │    Amplifier NF degrades SNR → directly reduces channel capacity.          │
  │    For an ADC front end: input-referred noise + quantization noise         │
  │    together set ENOB = (SINAD - 1.76) / 6.02.                            │
  │    A 16-bit ADC with NF = 10 dB front-end amp may achieve only 14 ENOB.  │
  └────────────────────────────────────────────────────────────────────────────┘

  DESIGN RULES
  Input-referred noise:  v_ni = √(v_n_amp² + (i_n_amp × R_source)²)
  SNR at ADC input:      SNR = V_signal_rms / v_ni
  Budget allocation:     amplifier noise ≤ quantization noise → ENOB preserved
    For N-bit ADC, full-scale V_FS:  v_q = V_FS / (√12 × 2^N)
    Require v_ni < v_q for noise not to degrade resolution.
```

---

## 7. Multi-Stage and Operational Amplifiers

### Op-Amp Internal Architecture

```
  Typical two-stage CMOS op-amp:

  V_in+ ──┐
           ├── Diff pair ──── Gain stage ──── Output buffer ──── V_out
  V_in- ──┘        │                │
                 Tail              Compensation
                 current           capacitor Cc
                 source            (Miller compensation)

  Stage 1: Differential pair → high CMRR, sets input characteristics
  Stage 2: Common source → high voltage gain (typically 1000–10000)
  Stage 3: Output buffer (source follower) → low Rout

  Compensation capacitor Cc:
    Creates dominant pole at low frequency (Miller effect).
    Ensures other poles are beyond gain crossover → PM > 45°.
    "Pole splitting" — moves one pole lower, one higher.

  Gain: A_v = g_m1 · r_o1 · g_m2 · r_o2   (product of stage gains)
  GBW = g_m1 / Cc
```

### Op-Amp Non-Idealities

**Practical impact of non-idealities on system design:**

```
  12-bit ADC with 3.3V full-scale → LSB = 3.3V / 4096 ≈ 0.8 mV
  → V_os of 5 mV = 6 LSB error at DC (unacceptable without calibration)
  → I_B of 1 µA through R_source = 10 kΩ → V_error = 10 mV = 12 LSB
  → CMRR of 80 dB with 1V common-mode → CM error = 100 µV ≈ 0.1 LSB (OK)

  Design rules:
  • V_os budget: select op-amp with V_os < 1 LSB of your ADC
  • Source impedance limit: R_source < V_os_budget / I_B
  • For precision (>14 bits): use chopper-stabilized op-amp (V_os < 10 µV)
  • Slew rate check: SR > 2π × f_signal × V_peak for full-power bandwidth
```

| Parameter | Effect | Typical Value |
|---|---|---|
| Input offset voltage V_os | Output error even with 0 input | 1–10 mV (BJT), 1–25 mV (CMOS) |
| Input bias current I_B | Error from source resistance | pA (CMOS), nA–μA (BJT) |
| Input offset current I_os | Differential of I_B | I_B/10 |
| Common-mode rejection (CMRR) | Rejects V_ic | 80–120 dB |
| Power supply rejection (PSRR) | Rejects supply noise | 60–120 dB |
| Slew rate (SR) | Max dV/dt at output | 0.5–1000 V/μs |
| GBW product | Gain × bandwidth | 1 MHz–1 GHz |
| Output swing | Maximum output voltage range | V_ss+0.1 to V_dd-0.1 (rail-to-rail) |

```
  Slew rate limiting:
    Large step input → diff pair driven out of linear range → output slews at SR.
    SR = 2I_EE/Cc (limited by tail current charging Cc).
    Full-power bandwidth: f_FP = SR / (2π·V_peak)
    Above f_FP: large signals are slew-rate limited (distorted sine becomes triangle).
```

---

## 7. Decision Cheat Sheet

| Need... | Use |
|---|---|
| Moderate voltage gain, common | Common emitter (BJT) or common source (MOSFET) |
| Current-to-voltage conversion | Shunt-shunt feedback transresistance amp |
| Impedance buffer (Z transform) | Emitter/source follower or op-amp buffer |
| High-frequency amplifier (avoid Miller) | Common base/gate (cascode) |
| Reject common-mode noise | Differential pair + high tail current source |
| Stable precise gain | Negative feedback, A_f ≈ 1/β |
| Amplify + filter in one stage | Transimpedance amp (photodiode) |
| High input impedance (sensor) | MOSFET input (FET op-amp) |
| High precision offset/low noise | BJT diff pair (lower V_os than CMOS) |
| Low power, VLSI | CMOS differential pair |
| Understand op-amp frequency rolloff | GBW = g_m1/Cc, check SR for large signals |

---

## 8. Common Confusion Points

**1. β (current gain) is not the feedback factor β**
Two completely different β. BJT: I_C = β·I_B (current gain, also called h_FE, typically 50–300). Feedback: A_f = A/(1+Aβ) where β is the feedback fraction (0 < β ≤ 1). Context determines which is meant. In this module β_feedback is often written f or B to avoid confusion.

**2. Small-signal model is only valid near operating point**
The small-signal equivalent circuit (g_m, r_π, r_o) is a linearization valid only for small signal swings around the DC bias point. Large signals: use the full nonlinear model (Ebers-Moll for BJT, I_D equation for MOSFET). For distortion analysis, you need higher-order terms.

**3. The diff pair doesn't eliminate CM signal — it rejects it**
CMRR is finite (80–120 dB, not infinite). A signal at the same voltage at both inputs is not completely rejected — it appears at output divided by CMRR. Important when common-mode range exceeds the supply or when CMRR degrades at high frequency (CMRR falls with frequency).

**4. Feedback stability requires checking the loop, not just the sign**
Negative feedback at DC can become positive feedback at high frequency due to additional phase shift through poles. Even an amplifier with "negative feedback" can oscillate. Must check phase margin at the frequency where loop gain = 1.

**5. Slew rate is not bandwidth**
Bandwidth (small-signal): frequency where |H(jω)| = 1/√2. Slew rate: max dV/dt for large signals. An op-amp with 10 MHz bandwidth and 1 V/μs slew rate will distort a 1 MHz, 1 V_peak sine (requires dV/dt_max = 2π × 1 MHz × 1V ≈ 6.3 V/μs > 1 V/μs SR).

**6. MOSFET threshold voltage varies with process, temperature, bias**
V_th isn't fixed. It shifts with temperature (roughly -2 mV/°C for NMOS), with substrate bias (body effect), and varies ±20% or more across process corners. Analog design must accommodate this variation. Digital design relies on the process being controlled within spec.
