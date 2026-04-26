# 03 — Filters

```
FILTER LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  Frequency selective networks — pass some frequencies, attenuate others.

  IDEAL                      REALIZABLE
  ────────────────           ─────────────────────────────────────────
  |H(jω)|                    |H(jω)|
    ___                         /‾‾‾\___
   |   |                       /      ‾‾‾───
  ─┘   └──  →ω              ──        →ω
                             ↑           ↑
                           Passband    Stopband (rolloff, not brick wall)
                         (ripple ok)   (attenuation in dB)

  Filter types:      LPF  HPF  BPF  BSF (band-stop/notch)
  Classic designs:   Butterworth, Chebyshev I/II, Elliptic, Bessel
  Realizations:      Passive RLC, Active RC (op-amp), Switched capacitor, Digital

  6.002 bridge: passive LC filters. 6.003 bridge: H(jω) concept, Bode plots.
```

---

## 1. Filter Specifications

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │          |H(jω)| (dB)                                               │
  │   0 ──────────────────                                              │
  │                          ╲                                          │
  │  -Rp (ripple) ─ ─ ─ ─ ─  ╲ ─ ─ ─ ─ ─                             │
  │                              ╲ transition                           │
  │  -As (stopband) ─ ─ ─ ─ ─ ─  ╲─────────── ─ ─ ─                   │
  │                   ωp     ωs        ω                                │
  │            passband  stopband edge                                  │
  └─────────────────────────────────────────────────────────────────────┘

  Key specs:
    ωp = passband edge frequency (where attenuation = Rp dB)
    ωs = stopband edge frequency (where attenuation ≥ As dB)
    Rp = passband ripple (typically 0.1–3 dB)
    As = stopband attenuation (typically 20–80 dB)
    Selectivity: ωs/ωp (closer to 1 = harder)

  Order n: higher order → sharper rolloff, more components, more phase shift.
```

---

## 2. Filter Design Approximations

### Butterworth — Maximally Flat Passband

```
  |H(jω)|² = 1 / (1 + (ω/ω_c)^(2n))

  Monotonically decreasing (no ripple anywhere).
  At ω_c: |H| = 1/√2 = -3 dB always.
  Rolloff: -20n dB/decade beyond ω_c.

  Poles: equally spaced on a circle of radius ω_c in LHP.
  s_k = ω_c · e^(jπ(2k+n-1)/(2n)),  k=1,...,n

  Phase response: smooth but significant phase distortion.
  Typical use: general-purpose, when flatness matters more than rolloff.

  Order formula:
    n ≥ log[(10^(As/10)-1)/(10^(Rp/10)-1)] / [2·log(ωs/ωp)]
```

### Chebyshev Type I — Equiripple in Passband

```
  |H(jω)|² = 1 / (1 + ε²·Tₙ²(ω/ω_c))

  Tₙ = Chebyshev polynomial of order n.
  Equiripple (constant ripple amplitude) in passband [0, ω_c].
  Monotonically decreasing in stopband.
  Sharper rolloff than Butterworth for same n and Rp.

  ε² = 10^(Rp/10) - 1   (controls ripple level)

  Order formula (sharper than Butterworth):
    n ≥ cosh⁻¹(√[(10^(As/10)-1)/ε²]) / cosh⁻¹(ωs/ωp)
```

### Chebyshev Type II — Equiripple in Stopband

```
  Flat passband (like Butterworth), equiripple stopband.
  Finite stopband zeros (notches at specific frequencies).
  Less common in practice but better for some applications.
```

### Elliptic (Cauer) — Equiripple Both Bands

```
  Equiripple in passband AND stopband.
  Minimum order for given (Rp, As, ωs/ωp) specifications.
  Finite transmission zeros in stopband.

  Tradeoff: steepest rolloff for given n, but worst group delay variation.
  Use when: need minimum order, don't care about phase/group delay.
```

### Bessel (Thomson) — Maximally Flat Group Delay

```
  Group delay: τ(ω) = -d∠H/dω
  Flat group delay = constant time delay for all frequencies = linear phase.
  Linear phase → no phase distortion → pulse shape preserved.

  Worst magnitude response (slowest rolloff), but best transient behavior.
  Use when: pulse fidelity, time-domain waveform shape matters.
  Audio DACs, oscilloscopes, digital communications.
```

### Comparison Table

| Approximation | Passband | Stopband | Group delay | Rolloff | Order needed |
|---|---|---|---|---|---|
| Butterworth | Flat | Monotone | Moderate | Moderate | Medium |
| Chebyshev I | Equiripple | Monotone | Worse | Better | Less |
| Chebyshev II | Flat | Equiripple | Better | Better | Less |
| Elliptic | Equiripple | Equiripple | Worst | Best | Minimum |
| Bessel | Slight roll | Monotone | Flat | Worst | Most |

```
  Selectivity ranking (same order n, same Rp):
    Elliptic > Chebyshev > Butterworth > Bessel
  Phase response ranking (best first):
    Bessel > Butterworth > Chebyshev > Elliptic
```

---

## 3. First and Second Order Sections

### First Order (n=1)

```
  Low-pass:   H(s) = ω_c/(s + ω_c)        = 1/(1 + s/ω_c)
  High-pass:  H(s) = s/(s + ω_c)           = (s/ω_c)/(1 + s/ω_c)
  |rolloff| = 20 dB/decade

  RC circuit: ω_c = 1/(RC)
  RL circuit: ω_c = R/L
```

### Second Order (n=2)

```
  General 2nd order LP:
    H(s) = ω₀²/(s² + (ω₀/Q)s + ω₀²)
         = ω₀²/(s² + 2ζω₀s + ω₀²)

  Q = 1/(2ζ): quality factor of the poles
  For Butterworth 2nd order: Q = 1/√2 ≈ 0.707
  For Chebyshev: Q > 1/√2
  For Bessel: Q < 1/√2

  HP version: multiply LP by s²/ω₀²  (replace s/ω₀ → ω₀/s)
    H_HP(s) = s²/(s² + (ω₀/Q)s + ω₀²)

  Bandpass (LP to BP transform: s → (s² + ω₀²)/(BW·s)):
    H_BP(s) = (BW·s)/(s² + BW·s + ω₀²)
    Peak at ω₀, 3dB bandwidth = BW, Q = ω₀/BW

  Notch (band-stop):
    H_BS(s) = (s² + ω₀²)/(s² + (ω₀/Q)s + ω₀²)
    Zeros on jω axis at ±jω₀ → null at ω₀
```

### Cascading Sections

```
  High-order filters = cascade of 1st and 2nd order sections.
  n even: n/2 second-order sections.
  n odd: one 1st-order section + (n-1)/2 second-order sections.

  H(s) = H₁(s) · H₂(s) · ... · H_k(s)

  Butterworth n=4 poles: two 2nd order sections with
    Q₁ = 1/(2cos(67.5°)) ≈ 1.307
    Q₂ = 1/(2cos(22.5°)) ≈ 0.541

  Section ordering: put lowest-Q section first to minimize internal clipping.
```

---

## 4. Active RC Filter Realizations

### Why Active Filters?

```
  Passive LC filters:
    + No power required
    + Low noise
    − Inductors: large, heavy, lossy, component tolerances poor at audio freq
    − No gain possible
    − Load-dependent (component values shift with load)

  Active RC filters (op-amp + R + C):
    + No inductors
    + Can provide gain
    + Low output impedance (load-independent)
    − Need power supply
    − Op-amp bandwidth limits high-frequency operation (GBW product)
    − Power supply noise enters signal path
    Use for: audio, instrumentation, data acquisition
```

### Sallen-Key Topology (2nd order LP)

```
         R₁    R₂
  Vin ───┤├────┤├────┬────── Vout
                     │         │
                    C₂         C₁
                     │         │
                    (−)        │
                    (+)────────┘
                    (op-amp as voltage follower)

  Unity gain Sallen-Key LP:
    H(s) = 1/[R₁R₂C₁C₂s² + (R₁C₁ + R₂C₁)s + 1]

    ω₀ = 1/√(R₁R₂C₁C₂)
    Q = √(R₁R₂C₁C₂) / (R₁C₁ + R₂C₁)

  Butterworth: choose R₁=R₂=R, C₁=C, C₂=C/2 → Q=1/√2

  Advantages: low component count, good sensitivity for moderate Q.
  Limitation: Q limited to ~10 (high Q requires tight component matching).
```

### Multiple Feedback (MFB) Topology (2nd order LP)

```
      Z₁     Z₂
  Vin─┤├────┤├────┬────── Vout
                  │         │
                 (−)       Z₃ (feedback to summing node)
                 (+)──GND  │
                            (input side, + side = GND)

  More complex but: inverting, arbitrary gain, better high-Q performance.
  Standard form for Chebyshev sections.
```

### State Variable / KHN (Kerwin-Huelsman-Newcomb)

```
  Three op-amps. Simultaneously provides LP, HP, and BP outputs.
  Best for high-Q sections (Q > 10).
  Excellent component sensitivity.

  ARCHITECTURE
  ┌─────────────┐    ┌──────────────┐    ┌──────────────┐
  │  Summing amp │───▶│ Integrator 1 │───▶│ Integrator 2│
  │  (op-amp 1) │    │  (op-amp 2)  │    │  (op-amp 3)  │
  │  HP output  │    │  BP output   │    │  LP output   │
  └──────┬───────┘    └──────────────┘    └──────┬───────┘
         ↑                                        │
         └────── R_Q feedback ────────────────────┘
         └────── R_f feedback (from BP) ──────────┘

  Transfer functions (equal-value design: R₁=R₂=R, C₁=C₂=C):
    ω₀ = 1/RC                        (set by integrator R and C)
    Q  = (1 + R_f/R_Q) / 3           (set by feedback resistor ratio)
    → ω₀ depends only on RC; Q depends only on R_f/R_Q
    → tuning Q does not shift ω₀, and vice versa

  Design example — 1 kHz bandpass, Q = 20:
    Choose C = 10 nF → R = 1/(2π×1000×10⁻⁸) ≈ 15.9 kΩ  (use 16 kΩ)
    Q = 20 → R_f/R_Q = 3Q - 1 = 59 → R_Q = 1 kΩ, R_f = 59 kΩ

  Why independent tuning matters for production:
    In Sallen-Key at Q > 10, ω₀ and Q both depend on the same component
    ratios — a 1% resistor tolerance can shift both simultaneously.
    In the KHN topology, component drift in the integrator chain shifts ω₀
    without affecting Q, and vice versa. This makes KHN practical for
    high-Q sections where Sallen-Key would need 0.1% components.
```

---

## 5. Switched-Capacitor Filters

```
  Key idea:  A capacitor C switched at frequency f_clk simulates a resistor:
    R_eq = 1/(C·f_clk)

  Operation:
    φ₁: charge C to V_in    → q = C·V_in
    φ₂: discharge C to V_out → ΔV = V_in - V_out, ΔQ = C·ΔV

  Average current: I_avg = ΔQ/T_clk = C·f_clk·(V_in - V_out) = (V_in-V_out)/R_eq

  Advantage:
    Filter cutoff tracks f_clk exactly.
    No absolute R and C tolerance issues — only ratio C₁/C₂ matters.
    Accurate ratios achievable in CMOS (0.1% easily).
    Tunable by changing clock frequency.

  Used in: audio codecs, ADC anti-aliasing, CMOS IC filters.
  Limitation: sampled-data system (aliasing, clock feedthrough noise).
```

---

## 6. Filter Frequency Transformations

**Analog → digital bridge:** Every analog filter prototype H(s) in this guide can be converted to a digital IIR filter via the bilinear transform: s = (2/T)(z-1)/(z+1). This maps the entire s-plane left half-plane to the interior of the unit circle, preserving stability. The analog pole locations designed here become digital pole locations in module 06-DSP. Pre-warp the critical frequency to compensate for the nonlinear frequency mapping.

```
  Start with prototype LP with ω_c = 1 rad/s.
  Transform to get other types:

  LP → HP:   s → ω₀²/s     (invert frequency axis)
  LP → BP:   s → Q(s/ω₀ + ω₀/s) = (s² + ω₀²)/(ω₀ BW · s)
  LP → BS:   s → ω₀ BW·s/(s² + ω₀²)    (inverse of LP→BP)

  LP → LP (frequency scale):  s → s·ω_old/ω_new  (shift cutoff)

  Then denormalize: scale R and C values to practical ranges.
  Impedance scaling: R → kR, C → C/k (doesn't change H(s))
```

---

## 7. Practical Filter Design Flow

```
  1. Specify: LPF/HPF/BPF/BSF, f_passband, f_stopband, Rp, As
  2. Choose approximation: Butterworth/Chebyshev/Elliptic/Bessel
  3. Compute order n from specs
  4. Look up normalized prototype H(s) (polynomial tables or software)
  5. Apply frequency transformation to shift cutoff to desired frequency
  6. Choose topology: Sallen-Key (Q<10), MFB (medium Q), State variable (Q>10)
  7. Scale impedance to practical R/C values
  8. Simulate in SPICE, then breadboard
  9. Check: component tolerances, op-amp GBW vs cutoff (need GBW >> Q·f_c)
```

---

## 8. Decision Cheat Sheet

| Need... | Use |
|---|---|
| Flat passband, no ripple | Butterworth |
| Sharpest rolloff, don't care about ripple | Elliptic |
| Preserve pulse shape / group delay | Bessel |
| Compromise rolloff + group delay | Butterworth or Chebyshev II |
| Audio / voice filter (op-amp) | Sallen-Key (simple) or MFB |
| High Q (>10) active filter | State variable (KHN) |
| High accuracy without trimming | Switched-capacitor |
| High frequency (RF) | Passive LC (no op-amp GBW limit) |
| Simple 20 dB/dec rolloff | Single-pole RC, ω_c = 1/RC |
| 40 dB/dec, max flat | 2nd order Butterworth Sallen-Key, Q=1/√2 |
| Quick 3dB corner calc | f_c = 1/(2πRC) |

---

## 9. Common Confusion Points

**1. Filter order = number of poles ≠ number of components**
A 4th order filter has 4 poles. Active RC: each 2nd-order section has 2 poles and uses 2 capacitors + 2 resistors + 1 op-amp. Two sections → 4 poles, 4 caps, 4 resistors, 2 op-amps. Not 4 of everything.

**2. Chebyshev ripple is in the passband, not the stopband**
Chebyshev Type I has equiripple passband and monotone stopband. Chebyshev Type II (inverse Chebyshev) has flat passband and equiripple stopband. The type matters significantly for practical specs.

**3. -3 dB frequency isn't always the cutoff specification frequency**
For Butterworth: passband edge = -3 dB point always. For Chebyshev: passband edge = end of ripple band (can be -0.5 dB or -3 dB depending on spec). Know what your spec defines as "cutoff."

**4. Op-amp GBW limits active filter frequency**
If op-amp GBW = 1 MHz and you need Q=10 filter at f₀ = 100 kHz, the required gain-bandwidth = Q × f₀ = 1 MHz — exactly the op-amp limit, so performance degrades severely. Rule of thumb: GBW > 100 × Q × f₀ for Sallen-Key.

**5. Switched-capacitor filters alias**
SC filters are sampled-data systems. Anti-aliasing before the SC filter is required if signals near f_clk/2 are present. The continuous-time input must be bandlimited before the SC filter samples it.

**6. Cascading filter sections changes the overall response**
H_total = H₁·H₂ doesn't mean -3 dB is at same frequency. Two identical first-order sections: |H|² = [1/(1+(ω/ωc)²)]², so -3 dB of cascade is at ω where this = 1/2 → ω = ωc√(√2-1) ≈ 0.644ωc. To get -3 dB at specified frequency, you must denormalize accounting for cascade.
