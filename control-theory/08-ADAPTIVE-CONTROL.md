# Adaptive Control

## Big Picture: Unknown or Time-Varying Plants

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ADAPTIVE CONTROL ARCHITECTURE                    │
│                                                                     │
│  PROBLEM: θ* = true plant parameters — UNKNOWN                     │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  DIRECT ADAPTIVE CONTROL:                                    │  │
│  │  Controller parameters θ updated directly from error         │  │
│  │  (no explicit plant estimation)                              │  │
│  │                                                              │  │
│  │     r ─► [C(θ(t))] ─► u ─►[Plant G(θ*)] ─► y              │  │
│  │                              error ↑                        │  │
│  │              θ̇ = -γ·e·(regression vector)                  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │  INDIRECT ADAPTIVE CONTROL (Self-Tuning Regulator):          │  │
│  │  1. Estimate θ̂(t) from I/O data                             │  │
│  │  2. Design controller for estimated plant (certainty equiv.)  │  │
│  │                                                              │  │
│  │     r ─► [C(θ̂(t))] ─► u ─► [Plant G(θ*)] ─► y             │  │
│  │                              ↓ estimation                   │  │
│  │              θ̂̇ = RLS update                                │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                     │
│  GAIN SCHEDULING: No adaptation — scheduled from operating point   │
│  L1 ADAPTIVE:     Fast adaptation + low-pass filter (Hovakimyan)  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Model Reference Adaptive Control (MRAC)

### Setup

```
REFERENCE MODEL Wm(s): defines desired closed-loop behavior
  Input: r(t) → Output: ym(t) = Wm(s)r(t)
  Chosen by designer: Wm(s) typically SPR (strictly positive real) or
  chosen as ideal closed-loop you wish to match

ERROR: e(t) = y(t) - ym(t)  (output tracking error)

GOAL: adapt controller parameters θ(t) so that e(t) → 0 as t → ∞

FIRST-ORDER EXAMPLE:
  Plant:     ẏ = -a_p y + b_p u    (a_p, b_p unknown)
  Ref model: ẏm = -am ym + bm r    (am > 0, bm known — desired response)
  Control:   u = θ₁(t)r + θ₂(t)y  (parameterized)

  Matching: θ₁* = bm/b_p, θ₂* = (a_p - am)/b_p → perfect model matching
```

### MIT Rule and Lyapunov-Based Derivation

```
MIT RULE (heuristic, 1966):
  Gradient descent on J = e²/2:
  θ̇ᵢ = -γ · ∂e/∂θᵢ · e    (γ > 0 adaptation gain)

  Not guaranteed stable in general — works for slow adaptation,
  can go unstable for large γ or poor excitation

LYAPUNOV-BASED MRAC (provably stable):
  For the first-order example:
  Define parameter errors: φ₁ = θ₁ - θ₁*, φ₂ = θ₂ - θ₂*
  Error dynamics:  ė = -am·e + b_p(φ₁r + φ₂y)

  Lyapunov function: V = e²/2 + b_p/(2γ)(φ₁² + φ₂²)

  V̇ = e·ė + b_p/γ(φ₁φ̇₁ + φ₂φ̇₂)
     = e[-am·e + b_p(φ₁r + φ₂y)] + b_p/γ(φ₁φ̇₁ + φ₂φ̇₂)
     = -am·e² + b_p[φ₁(er + φ̇₁/γ) + φ₂(ey + φ̇₂/γ)]

  CHOOSE: φ̇₁ = θ̇₁ = -γer,  φ̇₂ = θ̇₂ = -γey
  → V̇ = -am·e² ≤ 0  ✓

  By LaSalle: e → 0 (but NOT necessarily θ → θ* — parameter convergence
  requires persistent excitation)
```

### Persistent Excitation (PE)

```
PARAMETER CONVERGENCE: θ̂ → θ* requires PE condition on regression vector φ(t):

  ∃T > 0, α > 0 such that:
  ∫_{t}^{t+T} φ(τ)φᵀ(τ) dτ ≥ αI  for all t

  INTERPRETATION: Signal φ must be "rich" enough in all directions
  For n-parameter system: reference r must contain at least n distinct frequencies
  Sinusoid at single frequency → only 1D excitation → only 1 parameter identifiable

PRACTICAL IMPLICATION:
  With only set-point tracking (r = constant): φ is low-rank → poor identification
  Add small sinusoidal dither to r → improves parameter convergence
  Trade-off: dither improves adaptation but slightly degrades nominal tracking
```

---

## Self-Tuning Regulators (STR)

### Certainty Equivalence Principle

```
INDIRECT ADAPTIVE CONTROL:
  1. Run online parameter estimator: θ̂(t) = RLS(past inputs and outputs)
  2. At each t: design controller C(θ̂(t)) assuming θ̂(t) = θ* (certainty equiv.)
  3. Apply C(θ̂(t)) to plant

STRUCTURE:
  ┌──────────────┐    θ̂    ┌───────────────────┐
  │  Estimator   │ ──────► │  Controller Design │
  │  (RLS)       │         │  C(θ̂) = ?         │
  └──────┬───────┘         └────────┬───────────┘
         │ y, u                     │ u
         └──────────────────────────┘
                    Plant G(θ*)

IMPLICIT STR: Directly update controller parameters from I/O
  (skip explicit plant parameter estimates)
EXPLICIT STR: Estimate plant θ̂, then redesign C(θ̂) each step
  (PID auto-tuning, self-tuning LQG)
```

---

## Recursive Least Squares (RLS)

### Algorithm

```
LINEAR REGRESSION MODEL:
  y(t) = φᵀ(t)θ + noise(t)
  φ(t) = [y(t-1), ..., y(t-na), u(t-1), ..., u(t-nb)]  (regression vector)
  θ = [a₁,...,ana, b₁,...,bnb]ᵀ  (plant parameters to identify)

RLS UPDATE (recursive form, avoids matrix inversion):
  ê(t) = y(t) - φᵀ(t)θ̂(t-1)            (prediction error)
  L(t) = P(t-1)φ(t) / [λ + φᵀ(t)P(t-1)φ(t)]   (gain vector)
  θ̂(t) = θ̂(t-1) + L(t)ê(t)             (parameter update)
  P(t) = [I - L(t)φᵀ(t)]P(t-1)/λ        (covariance update)

  λ ∈ (0, 1]: forgetting factor
  λ = 1:   infinite memory (batch least squares in recursive form)
  λ < 1:   exponential forgetting, weight recent data more
           effective memory ~ 1/(1-λ) samples
  Typical: λ = 0.95-0.99 for time-varying systems

P(t) INTERPRETATION: Proportional to parameter estimation covariance
  Large P → high uncertainty → fast adaptation (large L)
  Small P → low uncertainty → slow adaptation (trusts current estimate)
```

### Covariance Windup

<!-- @editor[bridge/P2]: RLS forgetting factor λ is the control-theory formalization of exponential moving averages and sliding window metrics in monitoring systems. λ = 0.95 means 95% weight on the recent window — the effective memory is 1/(1-0.95) = 20 samples, exactly like a 20-point moving average. The covariance windup problem maps to a well-known monitoring failure mode: when a metric goes constant (no new signal), the monitoring system's "confidence" in its model grows artificially, causing it to overreact when the signal resumes. The directional forgetting fix maps to dead-band detection in anomaly systems. This bridge is immediately useful for someone who has designed or reviewed monitoring infrastructure. -->

```
COVARIANCE WINDUP (directional forgetting problem):
  If φ(t) is persistently in one direction (e.g., only one input active):
  P(t) grows unboundedly in directions orthogonal to φ
  → L(t) becomes large → parameter estimates jump when new direction excited

FIXES:
  1. Variable forgetting: λ(t) = 1 - (1-λ_min)·ê(t)²/‖φ(t)‖²
     (only forget when prediction error is large)

  2. Regularized RLS: P(t) → min(P(t), P_max·I)  (covariance bounding)

  3. Projection: bound θ̂ to known feasible set θ ∈ Θ
     θ̂(t) = Proj_Θ[θ̂(t-1) + L(t)ê(t)]
     → Prevents parameter drift even with poor excitation
```

---

<!-- @editor[bridge/P2]: Gain scheduling — a family of linear controllers indexed by operating point, no true adaptation — is the exact mental model behind canary deployments and A/B testing in infrastructure. You design a "controller" (traffic routing policy, autoscaler config) for each operating region (traffic pattern, region, tier), then interpolate. The scheduling variable ρ(t) maps to a feature flag value or a traffic segment tag. The stability caveat (fast scheduling can destabilize) maps directly to the danger of rapid feature flag toggling — each individual configuration is safe, but rapid switching can create transient instability. This bridge is unusually concrete and worth making explicit. -->

## Gain Scheduling

```
CONCEPT: Not truly adaptive — a family of linear controllers, one per operating point

  ┌─────────────────────────────────────────────────────────────┐
  │  GAIN SCHEDULE:                                             │
  │                                                             │
  │  Schedule variable ρ(t)  (e.g., airspeed, temperature, SOC)│
  │         ↓                                                   │
  │  Lookup table: C(ρ) = {K(ρ), gain, reference}              │
  │         ↓                                                   │
  │  Linear controller interpolated from design grid            │
  └─────────────────────────────────────────────────────────────┘

DESIGN PROCESS:
  1. Identify set of operating points {ρ₁, ρ₂,..., ρₙ}
  2. Linearize plant at each: G_i(s) = G(s)|_{ρ=ρᵢ}
  3. Design linear controller Cᵢ(s) for each G_i
  4. Interpolate: C(ρ) = Σᵢ wᵢ(ρ) Cᵢ  (weight by proximity)

STABILITY:
  NOT guaranteed: each Cᵢ stabilizes G_i, but fast scheduling can destabilize
  Safe if: scheduling variable varies slowly compared to closed-loop dynamics
  Formal analysis: Linear Parameter-Varying (LPV) theory provides stability
  guarantees using parameter-dependent Lyapunov functions

AEROSPACE EXAMPLE:
  F-16 flight control: gain scheduled on Mach, altitude, angle of attack
  Different aerodynamics at subsonic/transonic/supersonic → 3D gain table
  Same approach: automotive engine control (RPM + load = schedule variables)
```

---

## L1 Adaptive Control

```
PROBLEM WITH STANDARD MRAC:
  Fast adaptation (large γ) → better tracking but potential instability/oscillation
  Slow adaptation (small γ) → stable but poor disturbance rejection
  Fundamental bandwidth/robustness tradeoff

L1 ADAPTIVE CONTROL (Hovakimyan & Cao, 2010):
  Separates adaptation bandwidth from control bandwidth via low-pass filter

ARCHITECTURE:
  ┌────────────────────────────────────────────────────────────────┐
  │  State predictor:  x̂̇ = A_m x̂ + B(u + σ̂(t))               │
  │                   (fast, uses current θ̂)                      │
  │  Adaptation law:  σ̂̇ = ΓProj(σ̂, -Bᵀ P ẽ)  (fast, Γ → ∞)   │
  │                   ẽ = x̂ - x  (prediction error)              │
  │  Control signal:  u(s) = -C(s)σ̂(s)  (LPF of adaptive signal) │
  │                   C(s) = ω/(s + ω)  (low-pass filter)         │
  └────────────────────────────────────────────────────────────────┘

KEY PROPERTY:
  Γ → ∞ (arbitrarily fast adaptation) → σ̂ → σ (exact disturbance estimation)
  Low-pass C(s) cuts adaptation signal above ω_c → control bandwidth = ω_c
  Stability margin determined by C(s), NOT by Γ
  → Can have Γ → ∞ (perfect adaptation) while maintaining guaranteed stability margins

GUARANTEED BOUNDS (uniform in Γ):
  ‖x - x_{ref}‖_{L∞} ≤ O(1/ω_c)  (tracking error bounded regardless of Γ)
  → Transient performance guarantees (MRAC has no transient bounds)

USE CASE: Aircraft, quadrotors — applications where transient behavior during
  adaptation must be bounded and safe
```

---

## Neural Network Adaptive Control

```
MOTIVATION: Unknown nonlinearities f(x) — no parametric structure available

UNIVERSAL APPROXIMATION:
  Single-hidden-layer NN: f(x) ≈ Wᵀσ(Vx + b) for appropriate W, V, b
  Over any compact set Ω: ‖f(x) - Wᵀσ(Vx)‖ < ε  (approximation error)

INDIRECT NN ADAPTIVE (identification-based):
  1. Train NN online to approximate plant dynamics
  2. Use NN model in feedback linearization or MPC
  3. NN weights W updated by gradient of prediction error

LYAPUNOV STABILITY WITH NN:
  V = ½eᵀPe + ½tr(W̃ᵀΓ⁻¹W̃)    (e = tracking error, W̃ = W - W* estimation error)

  V̇ = -½eᵀQe + eᵀPB[W̃ᵀσ + ε(x)]    (ε = approximation error, bounded ≤ ε_max)
     ≤ -½λ_min(Q)‖e‖² + ‖PB‖‖e‖ε_max + cross-terms

  Choose adaptation law to cancel cross terms:
  Ẇ = -Γσeᵀ PB  → V̇ ≤ -c‖e‖² + c'ε_max²

  ULTIMATE BOUNDEDNESS: ‖e‖ ≤ f(ε_max) — bounded tracking error
  Perfect convergence: only if ε_max = 0 (NN approximates exactly)
  In practice: ε_max > 0 → error proportional to NN approximation quality

ISSUES:
  Weight initialization matters (bad init → slow convergence, instability)
  Projection needed to prevent weight drift (same as parameter drift in RLS)
  Overparameterization: too many NN weights → slow convergence, poor generalization
```

---

## Practical Issues in Adaptive Control

```
PARAMETER DRIFT (integral windup analog):
  If plant output near setpoint and noise present:
  θ̂ slowly drifts without bound (even though signals are bounded)
  FIX: Projection operator — constrain θ̂ ∈ Θ (known bounded set)
    θ̂(t) = Proj_Θ[θ̂(t) - γe·φ(t)]
    If θ̂ on boundary of Θ and update would leave Θ: project to boundary

BURSTING PHENOMENON:
  Parameters appear converged → reference changes → error spikes → rapid adaptation
  → Potential instability during burst
  FIX: e-modification or σ-modification — add stabilizing term to adaptation:
    θ̇ = -γe·φ - σθ̂  (σ > 0 dampens parameters toward zero)
    Trade-off: prevents drift but introduces steady-state bias in θ̂

FAST ADAPTATION → INSTABILITY:
  Large γ → fast tracking of θ* → but also amplifies noise
  Theoretical bound: γ < some function of minimum singular value of PE condition
  Practical: tune γ conservatively, verify with simulation over full disturbance envelope

CONTROL EFFORT DURING ADAPTATION:
  Large parameter errors at startup → large initial control effort
  Anti-saturation: constrain u within limits; update adaptation only when not saturated
  (modified adaptation law with dead zone near saturation)
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                     │ RECOMMENDATION                       │
├──────────────────────────────┼───────────────────────────────────────┤
│ Linear plant, parametric     │ MRAC (direct, Lyapunov-based);       │
│ uncertainty, tracking        │ add projection to prevent drift       │
├──────────────────────────────┼───────────────────────────────────────┤
│ SISO plant identification    │ RLS with forgetting factor;           │
│ + controller redesign        │ STR (indirect) with certainty equiv.  │
├──────────────────────────────┼───────────────────────────────────────┤
│ Known operating points,      │ Gain scheduling — simpler, safer,    │
│ slow scheduling variable     │ industry standard; use LPV for       │
│                              │ formal stability analysis            │
├──────────────────────────────┼───────────────────────────────────────┤
│ Safety-critical + adaptation │ L1 adaptive control — guaranteed     │
│ needed (aerospace)           │ transient bounds; tune via C(s) ω_c  │
├──────────────────────────────┼───────────────────────────────────────┤
│ Unknown nonlinear dynamics   │ NN adaptive control + Lyapunov       │
│                              │ stability analysis + projection       │
├──────────────────────────────┼───────────────────────────────────────┤
│ Time-varying plant, need     │ RLS with λ < 1; set λ based on       │
│ tracking of parameter change │ time constant of variation           │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## Common Confusion Points

**MRAC stability does not imply parameter convergence.** Lyapunov-based MRAC proves e(t) → 0 (tracking error). Parameter estimates θ̂(t) converge to true values θ* ONLY if the reference signal satisfies the PE condition. Without PE: perfect tracking is possible with wrong parameters (multiple parameter combinations may achieve the same zero error).

**Certainty equivalence is an assumption, not a theorem.** The STR design assumes θ̂ = θ*. There is no general stability theorem for certainty equivalence adaptive systems — stability is proven only for specific cases (slow adaptation, specific plant/controller structures). Bursting can occur precisely when the certainty equivalence assumption is most violated.

**RLS forgetting factor does not make RLS robust to all time variations.** Exponential forgetting forgets old data uniformly. For a plant where one parameter changes abruptly (step change), RLS with λ = 0.95 needs ~1/(1-λ) = 20 samples to forget the old value. For a sinusoidal parameter variation, the effective tracking bandwidth is related to (1-λ)/sampling_rate.

**L1 adaptive control's Γ → ∞ is theoretical.** In implementation, very large Γ (fast adaptation) amplifies numerical errors and measurement noise. The theoretical result says stability margin doesn't depend on Γ, but in practice there is an effective upper bound on Γ set by noise and sampling rate.

**Gain scheduling with interpolation is not guaranteed stable.** Linear interpolation between stabilizing controllers does not guarantee a stabilizing controller at intermediate points, especially for rapid parameter variations. The correct theoretical framework is LPV control with parameter-dependent Lyapunov functions, which provides explicit stability conditions on the rate of parameter variation.

**Adaptive control and robust control have complementary limitations.** Robust control handles fixed uncertainty sets — works for slow/fixed parameter variations but is conservative. Adaptive control handles time-varying parameters — can track changes but may be unstable during rapid changes or with poor excitation. Combining both (robust adaptive control) is an active area: project parameters onto Lyapunov-stable set using robust stability margins.
