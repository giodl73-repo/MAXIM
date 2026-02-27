# Classical Control — PID, Root Locus, Bode, Nyquist

## The Big Picture

Classical control theory is frequency-domain analysis of single-input single-output (SISO)
linear time-invariant (LTI) systems. It answers: **for a given plant G(s), what controller
C(s) makes the closed-loop system stable, fast, and accurate?**

```
+------------------------------------------------------------------+
|             CLOSED-LOOP CONTROL SYSTEM                           |
|                                                                   |
|            e(t)          u(t)              y(t)                  |
|  r(t) → Σ ──→ [C(s)] ──→ [G(s)] ──────────→                   |
|          ↑                  PLANT           |                    |
|          │                                  |                    |
|          └──────────────────────────────────┘ feedback           |
|                         (unity feedback shown)                    |
|                                                                   |
|  r(t) = reference (desired output)                               |
|  e(t) = r - y = tracking error                                   |
|  u(t) = controller output (actuator signal)                      |
|  y(t) = plant output (sensor measurement)                        |
|                                                                   |
|  Closed-loop TF: T(s) = C(s)G(s) / (1 + C(s)G(s))             |
|  Error TF:       E(s)/R(s) = 1 / (1 + C(s)G(s))               |
+------------------------------------------------------------------+
```

---

## PID Controller

The **Proportional-Integral-Derivative** controller is the workhorse of industrial control.
~90% of all control loops in process industries run PID.

```
             ┌─────────────────────────────────────────────────┐
             │  u(t) = Kp·e(t) + Ki·∫e(τ)dτ + Kd·(de/dt)    │
             │                                                  │
             │       Kp    = proportional gain                  │
             │       Ki    = integral gain = Kp/Ti              │
             │       Kd    = derivative gain = Kp·Td            │
             └─────────────────────────────────────────────────┘

Transfer function (Laplace domain):
  C(s) = Kp(1 + 1/(Ti·s) + Td·s)
       = Kp + Ki/s + Kd·s

Parallel form:
  C(s) = Kp + Ki/s + Kd·s

Standard form (ISA):
  C(s) = Kp(1 + 1/(Ti·s) + Td·s)   Ti = integral time, Td = derivative time
```

### The Three Terms and Their Effects

```
TERM          EFFECT ON RESPONSE                 EFFECT ON STEADY-STATE ERROR
────────────  ──────────────────────────────────  ──────────────────────────────
P (prop.)     Faster response; more overshoot     Reduces error but can't
              Higher Kp = faster but may          eliminate it for step input
              destabilize                         Steady-state error ∝ 1/(1+Kp·Gdc)

I (integral)  Eliminates steady-state error       Zero steady-state error for
              Slows response, adds phase lag       step inputs (type 1 system)
              Wind-up problem if output saturates  Can cause windup → instability

D (derivative) Damps oscillation; predicts error  No effect on steady-state
              Increases bandwidth; amplifies noise Usually needs low-pass filter:
              Derivative = "braking" action        Kd·s / (1 + s/ωf)
```

### PID Design Intuition

```
ERROR TOO BIG (slow response):    Increase Kp
STEADY-STATE ERROR PERSISTS:      Add/increase Ki
OSCILLATING / OVERSHOOTING:       Decrease Kp, increase Kd
OSCILLATING AFTER ADDING D:       Add low-pass filter on D term (derivative filter)
SYSTEM UNSTABLE:                  Decrease Kp
WINDUP (actuator saturates):      Add anti-windup: clamp integrator when saturated
```

---

## Anti-Windup

<!-- @editor[bridge/P2]: Anti-windup is the exact control-theory analog of backpressure and rate limiting in distributed systems. When an actuator saturates (downstream can't absorb more), clamping the integrator is structurally identical to a token bucket or leaky bucket: stop accumulating "debt" when the downstream queue is full, otherwise you get a burst surge when saturation ends. This bridge is highly concrete for a VP of Eng who has designed rate limiters — make it explicit. -->

When the actuator saturates (e.g., motor hits max voltage), the integrator keeps
accumulating ("winding up"), causing large overshoot when saturation ends:

```
BACK-CALCULATION ANTI-WINDUP:
  u_unsat = Kp·e + Ki·∫e dt + Kd·de/dt   (unsaturated controller output)
  u_sat   = sat(u_unsat)                  (actual actuator input)

  Anti-windup feedback:
  d/dt [integrator] = e + (1/Tt)·(u_sat - u_unsat)

  When saturated: u_sat - u_unsat ≠ 0 → integrator back-calculated
  When not saturated: u_sat = u_unsat → normal operation
  Tt = tracking time constant (typically Ti/Td to Ti)
```

---

## Ziegler-Nichols Tuning

Classic empirical tuning rules when plant model is unknown:

### Method 1: Ultimate Gain (closed-loop step response)

```
1. Set Ki = Kd = 0 (P-only controller)
2. Increase Kp until system oscillates with constant amplitude
   (sustained oscillation — marginally stable)
3. Record: Ku = ultimate gain, Tu = period of oscillation

CONTROLLER  Kp          Ti          Td
──────────  ─────────── ──────────  ──────────
P           0.5·Ku      —           —
PI          0.45·Ku     Tu/1.2      —
PID         0.6·Ku      Tu/2        Tu/8
```

### Method 2: Process Reaction (open-loop step response)

```
Apply step to plant input; record S-shaped response:
  L = delay (inflection point intercept with time axis)
  T = time constant (slope at inflection point)
  K = steady-state gain

CONTROLLER  Kp          Ti          Td
──────────  ─────────── ──────────  ──────────
P           T/(K·L)     —           —
PI          0.9·T/(K·L) L/0.3       —
PID         1.2·T/(K·L) 2L          0.5L
```

Z-N tuning gives ~1/4 damping ratio (25% overshoot). For less overshoot, reduce Kp ~20%.

---

## Laplace Transform and Transfer Functions

```
TIME DOMAIN (ODE)               LAPLACE DOMAIN (algebra)
──────────────────────────────  ──────────────────────────────────────────
ẍ + 2ζωn·ẋ + ωn²·x = ωn²·u   →  (s² + 2ζωn·s + ωn²)·X(s) = ωn²·U(s)

Transfer function: G(s) = X(s)/U(s) = ωn² / (s² + 2ζωn·s + ωn²)

Poles: roots of denominator = s = -ζωn ± jωn√(1-ζ²)
Zeros: roots of numerator (none here)

STANDARD 2ND ORDER SYSTEM:
  G(s) = ωn² / (s² + 2ζωn·s + ωn²)

  ζ < 1: underdamped — poles at s = -ζωn ± jωd  where ωd = ωn√(1-ζ²)
  ζ = 1: critically damped — double pole at s = -ωn
  ζ > 1: overdamped — two real poles
  ζ = 0: undamped — poles at ±jωn

Step response metrics:
  Rise time:       tr ≈ (1.8/ωn) for ζ ≈ 0.6
  Peak time:       tp = π/ωd
  Overshoot:       OS% = 100·e^(-πζ/√(1-ζ²))
  Settling time:   ts ≈ 4/(ζωn)   (2% criterion)
```

---

## Root Locus

Root locus traces closed-loop poles as a gain K varies from 0 to ∞.

```
CLOSED-LOOP: T(s) = KG(s)H(s) / (1 + KG(s)H(s))
Characteristic equation: 1 + KG(s)H(s) = 0
Root locus: {s : KG(s)H(s) = -1}

ANGLE CONDITION:  ∠G(s)H(s) = ±180° (odd multiples)
MAGNITUDE COND:   |KG(s)H(s)| = 1

ROOT LOCUS CONSTRUCTION RULES:
  ─────────────────────────────────────────────────────────────────
  Rule 1: Branches start (K=0) at open-loop poles
  Rule 2: Branches end (K=∞) at open-loop zeros (or infinity)
  Rule 3: Number of branches = max(#poles, #zeros)
  Rule 4: Locus on real axis: to the left of an ODD number of real poles+zeros
  Rule 5: Asymptotes for n-m branches going to ∞:
            angles: (2k+1)·180°/(n-m)  for k=0,1,...,n-m-1
            centroid: σa = (Σpoles - Σzeros)/(n-m)
  Rule 6: Breakaway/break-in: solve dK/ds = 0
  Rule 7: Imaginary axis crossings: Routh-Hurwitz on characteristic equation
  ─────────────────────────────────────────────────────────────────

Example: G(s) = 1/(s(s+2))  (DC motor-like plant)
  Open-loop poles at 0 and -2; no zeros
  Root locus: starts at 0 and -2, asymptotes at ±90°, centroid at -1
  Breakaway point: at s = -1 (between poles)
  As K increases: poles move toward jω axis, cross at s = ±j√2 when K=4
  K > 4: closed-loop goes unstable
```

**Root locus tells you:** how to place closed-loop poles by selecting K. Adding lead/lag
compensators reshapes the locus to achieve desired pole locations.

---

## Frequency Domain: Bode Plots

Bode plots show open-loop frequency response G(jω): magnitude |G(jω)| and phase ∠G(jω)
vs. log frequency.

```
BODE PLOT READING:
                |G(jω)| in dB
               40 │ ╲                         (−20 dB/decade per pole)
               20 │   ╲  ╱──────              (−40 dB/decade for two poles)
               0  │─────╲─────────────────
              -20 │      ╲
              -40 │       ╲
                  └────────────────────→ log ω
                       ωc = crossover

              ∠G(jω) in degrees
               0° │─────────────────
              -90° │         ╲────────  ← each pole contributes -90°
             -180° │               ╲──  ← phase margin measured here
                  └────────────────────→ log ω

ASYMPTOTIC BODE APPROXIMATIONS:
  Pole at s = -a:  magnitude slope breaks by -20 dB/decade at ω=a
                   phase: −45° at ω=a, transitions −5° to −85° over 2 decades
  Zero at s = -a:  magnitude slope breaks by +20 dB/decade at ω=a
                   phase: +45° at ω=a
  Integrator (pole at 0): -20 dB/decade slope, -90° phase throughout
  Underdamped pair: resonance peak, sharp phase drop at ωn
```

---

## Stability Margins

**Gain margin (GM)** and **phase margin (PM)** measure how close to instability:

```
PHASE CROSSOVER FREQUENCY ω_pc: where ∠G(jω) = -180°
GAIN CROSSOVER FREQUENCY  ω_gc: where |G(jω)| = 1 (0 dB)

GAIN MARGIN = 1/|G(jω_pc)|  in dB: GM = -|G(jω_pc)|_dB
  How much gain can be increased before instability
  Rule of thumb: GM > 6 dB (factor 2 in gain)

PHASE MARGIN = 180° + ∠G(jω_gc)
  How much more phase lag before instability
  Rule of thumb: PM > 45° (PM ≈ 60° for good transient response)
  Relation: PM ≈ damping ratio ζ ≈ PM/100  (rough, ζ ≈ PM(deg)/100)

BODE STABILITY CRITERION (minimum phase systems only):
  If |G(jω)| < 1 at ω where ∠G = -180°, system is stable.

EXAMPLE:
  G(s) = 10/(s(s+1)(s+5))
  ω_pc: solve ∠G(jω) = -180° → ω_pc ≈ 2.24 rad/s
  |G(j·2.24)| ≈ 0.5 → GM = 1/0.5 = 2 = 6 dB  ← barely adequate
  ω_gc: |G(jω)| = 1 → ω_gc ≈ 0.74 rad/s
  ∠G(j·0.74) ≈ -132° → PM = 180-132 = 48°  ← acceptable
```

---

## Nyquist Stability Criterion

<!-- @editor[bridge/P2]: Nyquist's encirclement criterion has a striking analog in distributed consensus: a network of agents (or microservices) is stable when the open-loop gain product around any feedback cycle stays below 1. A positive feedback cycle (N encirclements of -1) is exactly what happens in a distributed thundering herd or feedback amplification failure — one node's overload signal causes all other nodes to retry harder, driving the system unstable. This is a high-value bridge for this learner given the CI/CD and Azure DevOps background. -->

More powerful than Bode — handles unstable open-loop plants and non-minimum-phase systems.

```
NYQUIST PLOT: plot of G(jω)H(jω) in complex plane as ω: -∞ → +∞

NYQUIST CRITERION:
  Z = N + P
  Z = number of closed-loop unstable poles (RHP)
  N = number of clockwise encirclements of (-1, 0)
  P = number of open-loop unstable poles (RHP)

For stable closed-loop: Z = 0, so N = -P

Simple case (P=0, stable open-loop plant):
  Closed loop stable ⟺ Nyquist plot does NOT encircle (-1, 0)

GAIN AND PHASE MARGINS ON NYQUIST PLOT:
  Phase margin: distance from (-1,0) along the unit circle arc
  Gain margin: 1/|G(jω_pc)| = inverse of where the plot crosses the negative real axis

ADVANTAGE OVER BODE:
  Works for unstable plants (P≠0)
  Works for non-minimum-phase (RHP zeros)
  Rigorous for MIMO extension (return difference matrix)
```

---

## Lead and Lag Compensators

When simple gain tuning is insufficient, add a dynamic compensator:

```
LEAD COMPENSATOR: C(s) = Kc(s+z)/(s+p), where p > z (zero left of pole)
  ─ Adds positive phase near ωgc → increases phase margin
  ─ Increases bandwidth (faster response)
  ─ Use when: PM too low, response too slow

LEAD DESIGN PROCEDURE:
  1. Find phase deficiency: φ_needed = PM_desired - PM_current + 5°-12° safety
  2. α = (1-sin φ_needed)/(1+sin φ_needed)  (α < 1)
  3. Max phase contribution at ω_max = 1/(τ√α)
  4. Set ω_max = ω_gc_new (desired crossover)
  5. z = ω_max·√α, p = ω_max/√α

LAG COMPENSATOR: C(s) = Kc(s+z)/(s+p), where z > p (zero right of pole)
  ─ Reduces gain at high frequencies → shifts crossover to lower ω
  ─ Increases steady-state accuracy (zero ≈ at origin)
  ─ Use when: steady-state error too large, bandwidth high enough

PD, PI, PID AS COMPENSATORS:
  PD = lead compensator (approximate, pure differentiator is improper)
  PI = lag compensator with zero at origin
  PID = lead-lag combination
```

---

## Steady-State Error and System Type

```
SYSTEM TYPE = number of open-loop integrators (poles at s=0)

For step input R(s) = 1/s:
  ess = lim(s→0) s·E(s) = lim(s→0) s / (1 + G(s)C(s)) · 1/s
      = 1/(1+Kp)  where Kp = lim(s→0) G(s)C(s)  (position constant)

TYPE 0 (no integrators): ess = 1/(1+Kp), finite steady-state error to step
TYPE 1 (one integrator): ess = 0 for step, ess = 1/Kv for ramp (velocity constant)
TYPE 2 (two integrators): ess = 0 for step and ramp, finite for parabola

PI/I controller adds one integrator → increases system type by 1 → eliminates
steady-state error for one lower-order input.
```

---

## Digital (Discrete-Time) PID

In software, the PID is implemented in discrete time. Approximation methods:

```
FORWARD EULER (explicit):    s ≈ (z-1)/T      (unstable for large T)
BACKWARD EULER (implicit):   s ≈ (z-1)/(Tz)   (always stable, overdamping)
BILINEAR (TUSTIN):           s ≈ 2(z-1)/(T(z+1))  (best frequency response)
  Recommended — maps jω axis to unit circle

DISCRETE PID (Tustin):
  u[k] = u[k-1] + Kp(e[k]-e[k-1]) + Ki·T/2·(e[k]+e[k-1])
                + Kd/T·(e[k]-2e[k-1]+e[k-2])

SAMPLING RULE OF THUMB:
  Sample at least 20x the bandwidth: Ts < 0.05/ωgc
  Nyquist: Ts < π/ωgc (absolute minimum — unworkable in practice)
```

---

## Decision Cheat Sheet

| Goal | Method |
|------|--------|
| Quick tuning without model | Ziegler-Nichols (accept 25% overshoot) |
| Eliminate steady-state error | Add integrator (PI or I action) |
| Reduce overshoot / oscillation | Add derivative (PD or D action) |
| Visualize closed-loop pole movement | Root locus |
| Check gain and phase margins | Bode plot |
| Handle unstable open-loop plant | Nyquist criterion |
| Increase bandwidth + phase margin | Lead compensator |
| Improve steady-state accuracy | Lag compensator (or PI) |
| Prevent integrator saturation | Anti-windup back-calculation |
| Implement in software | Discrete PID with Tustin (bilinear) transform |
| Trade-off between PM and bandwidth | Bode: PM ↑ → bandwidth ↓ |

## Common Confusion Points

**Gain margin and phase margin can both be infinite (for a type-0 first-order system).**
A first-order plant G(s) = K/(s+a) has only -90° phase lag maximum — never reaches -180°
— so it is stable for all K>0, gain margin = ∞.

**Bode stability criterion only applies to minimum-phase systems.** A system with RHP
zeros or open-loop unstable poles requires Nyquist. Bode will give wrong stability
conclusions for non-minimum-phase plants.

**Adding a derivative action requires a filter.** Pure derivative C(s) = Kd·s is
improper (degree of numerator > denominator) — not realizable. Practical: Kd·s/(1+s/N)
where N = 5-20 is the derivative filter coefficient.

**Root locus for negative gains is an inverted root locus.** Standard root locus is for
positive K. For K < 0, use angle condition = 0° (even multiples of 180°) — the locus
is different and called "complementary root locus."

**PM ≈ damping ratio ζ is a rough rule only.** ζ ≈ PM(radians)/2 works for second-order
systems; for higher-order systems with significant high-frequency poles, the relationship
degrades.
