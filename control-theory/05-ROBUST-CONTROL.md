# Robust Control

## Big Picture: Nominal Model vs Reality

```
┌─────────────────────────────────────────────────────────────────────┐
│                    ROBUST CONTROL FRAMEWORK                         │
│                                                                     │
│  REALITY:                                                           │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │  True plant: G_real(s) = G(s)(1 + Δ(s))                    │   │
│  │                                        ↑                    │   │
│  │  Nominal model: G(s)  (what you designed for)               │   │
│  │  Uncertainty: Δ(s)    (unknown, but ‖Δ‖∞ ≤ 1 assumed)      │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                     │
│  FUNDAMENTAL QUESTION:                                              │
│  Design C(s) that stabilizes G(s)(1+Δ(s)) for ALL admissible Δ    │
│                                                                     │
│  TOOLS:                                                             │
│  Small Gain Theorem ──► H∞ control ──► μ-synthesis               │
│  (stability condition)  (min worst-case gain)  (structured Δ)      │
│                                                                     │
│  CLASSICAL METRICS vs ROBUST METRICS:                              │
│  Classical: gain margin, phase margin (single SISO loop)            │
│  Robust:    H∞ norm of closed-loop map (MIMO, structured uncertainty│
└─────────────────────────────────────────────────────────────────────┘
```

---

## Uncertainty Representations

### Uncertainty Models

```
ADDITIVE UNCERTAINTY:
  G_real(s) = G(s) + Δ_A(s)
  ‖Δ_A(jω)‖ ≤ l_A(ω)  (frequency-dependent bound)
  Captures: additive noise, model error in absolute terms
  Feedback: Δ_A enters as input disturbance in standard form

MULTIPLICATIVE OUTPUT UNCERTAINTY:
  G_real(s) = (I + Δ_O(s)) G(s)
  ‖Δ_O(jω)‖ ≤ l_O(ω)
  Captures: relative model error — more natural for systems where
  error scales with gain (sensor calibration, gain uncertainty)
  Feedback: Δ_O is "wrapped around" plant output

MULTIPLICATIVE INPUT UNCERTAINTY:
  G_real(s) = G(s)(I + Δ_I(s))
  ‖Δ_I(jω)‖ ≤ l_I(ω)
  Captures: actuator uncertainty (servo amplifier gain variation)

COPRIME FACTOR UNCERTAINTY:
  G_real(s) = (M̃(s) + ΔM)⁻¹(Ñ(s) + ΔN)
  where G = M⁻¹N is a coprime factorization
  ‖[ΔN, ΔM]‖∞ ≤ ε
  Captures: right/left half-plane pole/zero uncertainty
  Basis for McFarlane-Glover loop shaping
```

### Structured vs Unstructured

```
UNSTRUCTURED UNCERTAINTY:
  Δ(s) is arbitrary matrix bounded in H∞ norm
  ‖Δ‖∞ ≤ 1  (normalized)
  Conservative: assumes worst possible perturbation structure
  Used in H∞ design

STRUCTURED UNCERTAINTY:
  Δ = diag(δ₁I_{k₁}, ..., δₛI_{kₛ}, Δ₁, ..., Δ_f)
  Known structure: δᵢ are scalar uncertainties (parameter variations)
                   Δⱼ are full complex matrix uncertainties (dynamic)
  Less conservative: exploits that perturbations act independently
  Requires μ-synthesis (structured singular value)

EXAMPLE — Aircraft pitch axis:
  q_eff/q_cmd ≈ G_nominal(s) with:
  δ₁ = ±20% CG uncertainty (scalar, real)
  δ₂ = ±15% aerodynamic gain (scalar, real)
  Δ₁ = unmodeled flex dynamics (complex, 2×2)
```

---

## Small Gain Theorem

### Statement and Derivation

```
STANDARD INTERCONNECTION:

  w ─────►┌───────┐──── z
          │  M(s) │
  ┌───────└───────┘◄───┐
  │                    │
  │       ┌───────┐    │
  └──────►│  Δ(s) │────┘
          └───────┘

where M is the closed-loop transfer function from (w, output of Δ)
to (z, input to Δ), and Δ is the uncertainty.

SMALL GAIN THEOREM:
  If ‖M‖∞ < 1/‖Δ‖∞  for all ω,
  then the interconnection is stable for all stable Δ.

EQUIVALENTLY: If ‖M(jω)‖ · ‖Δ(jω)‖ < 1 for all ω ∈ ℝ

PROOF SKETCH (L2 gain argument):
  Let ‖M‖∞ = γ_M, ‖Δ‖∞ = γ_Δ, γ_M · γ_Δ < 1
  Signals e = w + Δy, y = Me
  ‖y‖₂ ≤ γ_M ‖e‖₂ = γ_M ‖w + Δy‖₂ ≤ γ_M(‖w‖₂ + γ_Δ‖y‖₂)
  ‖y‖₂ (1 - γ_M γ_Δ) ≤ γ_M ‖w‖₂  →  ‖y‖₂ ≤ γ_M/(1 - γ_M γ_Δ) ‖w‖₂
  Bounded input → bounded output: L2 stable. □

DESIGN IMPLICATION:
  Design M = T_zw(C, G) so that ‖M‖∞ < 1/l(ω) at all frequencies
  where l(ω) is the uncertainty weight ‖Δ(jω)‖ ≤ l(ω)
```

---

## H∞ Control

### Problem Formulation

```
GENERALIZED PLANT P(s):
  ┌─────────────────┐
  │                 │
w ─►               ├──► z    (exogenous input w → performance output z)
  │     P(s)        │
u ─►               ├──► y    (control input u → measured output y)
  └─────────────────┘

Partition P: [z]   [P₁₁  P₁₂] [w]
             [y] = [P₂₁  P₂₂] [u]

Controller u = C(s)y → closed-loop z = T_zw(P, C) w

H∞ PROBLEM: find C(s) stabilizing P such that
  ‖T_zw(P, C)‖∞ < γ  (minimize γ)

‖T_zw‖∞ = sup_ω σ_max(T_zw(jω)) = worst-case RMS gain from w to z
```

### Mixed Sensitivity Formulation (SISO)

```
TYPICAL WEIGHTING STRUCTURE:
  ┌───┐           ┌────┐
r ─►│ W₁│──► e ──►│ C  │──► u ──►┌───┐──► y
  └───┘     ↑    └────┘         │ G │
            │─────────────────────└───┘

  Minimize: ‖[W₁S]‖   where S = (1 + GC)⁻¹  (sensitivity)
            ‖[W₂T]‖∞       T = GC(1 + GC)⁻¹ (complementary sensitivity)
            ‖[W₃CS]‖       CS = C(1 + GC)⁻¹ (control sensitivity)

WEIGHT DESIGN RULES:
  W₁(s): performance weight on S — high at low ω (good disturbance rejection)
    Typical: W₁(s) = (s/M + ω_B) / (s + ω_B A)
    Parameters: ω_B = desired bandwidth, M = peak sensitivity bound, A = steady-state error

  W₂(s): weight on T — roll off at high ω (robustness to sensor noise, unmodeled dynamics)
    Typical: W₂(s) = (s + ω_B/M_T) / (ε·s + ω_B)  (high-pass)

  W₃(s): limit control effort at high frequencies (actuator limits)

WATERBED EFFECT:
  S(jω) + T(jω) = 1  →  pushing down S somewhere pushes up T elsewhere
  Bode's integral: ∫₀^∞ log|S(jω)|dω = π Σ Re(pᵢ) (RHP poles)
  Can't make S small everywhere — must budget sensitivity
```

### Riccati Equation Solution

```
H∞ SUBOPTIMAL CONTROL (Doyle-Glover-Khargonekar-Francis, 1989):
  Existence of C achieving ‖T_zw‖∞ < γ is equivalent to:
  1. X∞ ≥ 0 solves: A^T X∞ + X∞A + C₁^TC₁ + X∞(B₁B₁^T/γ² - B₂B₂^T^{-1}...
     [standard form Riccati with γ-dependent term]
  2. Y∞ ≥ 0 solves: AY∞ + Y∞A^T + B₁B₁^T + Y∞(C₁^TC₁/γ² - C₂^TR₂^{-1}C₂)Y∞ = 0
  3. ρ(X∞Y∞) < γ²  (spectral radius condition)

OPTIMAL γ SEARCH: Binary search on γ until conditions marginally met
  γ → ∞: Riccati solutions exist (LQG limit)
  γ → γ_opt: Riccati solutions approach each other (optimal γ)

CONTROLLER STRUCTURE:
  H∞ controller has same order as plant (state dimension = n)
  Generalizes LQG: H∞ = LQG when γ → ∞
  State estimate from H∞ filter (minimax estimation)
```

---

## Loop Shaping — McFarlane-Glover

```
PROCEDURE:
  1. Design desired open-loop shape L₀(s) by classical frequency-domain methods
     (bandwidth, roll-off rate, integral action — exactly like classical design)

  2. Form shaped plant: G_s(s) = W₂(s) G(s) W₁(s)
     where W₁, W₂ are pre/post compensators shaping L₀

  3. Find robustly stabilizing controller for G_s using normalized
     coprime factor uncertainty:
     G_s = M_s⁻¹ N_s  →  maximize ε: Gᵣₑₐₗ = (M_s + ΔM)⁻¹(N_s + ΔN)

  4. The robust stability margin ε_max = (1 - σ_min(∞)²)^{1/2}
     where ∞ = [Y  X; -Ñ  M̃] (controllability/observability Gramians)

  5. Recommended: ε_max ≥ 0.25-0.3 for good robustness

ADVANTAGE: Intuitive design (engineer shapes L₀) + automatic robustification
LIMITATION: Only for coprime factor uncertainty — not directly for parametric uncertainty
```

---

## μ-Synthesis (Structured Singular Value)

### Structured Singular Value μ

```
DEFINITION: For M ∈ ℂⁿˣⁿ and structure set Δ = {diag(δ₁I,..., Δ_f,...)}:

  μ_Δ(M) = 1 / min{σ_min(Δ) : Δ ∈ Δ, det(I - MΔ) = 0}

  If no Δ ∈ Δ destabilizes: μ = 0

INTERPRETATION: μ is the smallest structured perturbation that causes instability
  μ < 1: robust stability for all ‖Δ‖∞ ≤ 1 (normalized)
  1/μ: gain margin for structured perturbations

ROBUST STABILITY TEST: max_ω μ_Δ(M(jω)) < 1

BOUNDS:
  ρ(M) ≤ μ_Δ(M) ≤ σ̄(M)   (spectral radius ≤ μ ≤ max singular value)
  Exact μ: NP-hard in general
  Upper bound: σ̄(D·M·D⁻¹) for diagonal scaling D — tight for ≤3 full blocks
```

### D-K Iteration

```
D-K ITERATION:
  1. Fix D = I, solve H∞ problem: min_C ‖D·T_zw(P,C)·D⁻¹‖∞
     → get controller C_k
  2. Fix C = C_k, find D(jω) minimizing σ̄(D(jω)·M(jω)·D⁻¹(jω)) at each ω
     → fit rational stable D(s) to frequency response
  3. Repeat from Step 1 with new D(s)
  Until: max_ω μ estimate converges

CONVERGENCE: Not guaranteed globally, but works in practice
RESULT: C that achieves small μ — robustly stable for structured uncertainty

MATLAB: dksyn(P, nmeas, ncont, opt_struct)  (Robust Control Toolbox)
  Requires: specifying uncertainty structure (ucomplex, ureal, ultidyn)
```

---

## Comparison: PID vs LQR vs H∞ vs μ-synthesis

```
┌──────────────────────────────────────────────────────────────────────┐
│ METHOD       │ PLANT   │ UNCERTAINTY    │ CONSTRAINTS  │ COMPLEXITY  │
├──────────────┼─────────┼────────────────┼──────────────┼─────────────┤
│ PID          │ SISO,   │ Gain/phase     │ None         │ 3 params    │
│              │ simple  │ margins only   │              │ trivial     │
├──────────────┼─────────┼────────────────┼──────────────┼─────────────┤
│ LQR/LQG      │ MIMO,   │ None (nominal) │ None         │ Riccati eq  │
│              │ linear  │                │              │ moderate    │
├──────────────┼─────────┼────────────────┼──────────────┼─────────────┤
│ H∞           │ MIMO,   │ Unstructured,  │ H∞ norm      │ Riccati/LMI │
│              │ linear  │ norm-bounded   │ bound        │ moderate    │
├──────────────┼─────────┼────────────────┼──────────────┼─────────────┤
│ μ-synthesis  │ MIMO,   │ Structured,    │ Structured   │ D-K iter    │
│              │ linear  │ complex/real   │ gain margin  │ high        │
├──────────────┼─────────┼────────────────┼──────────────┼─────────────┤
│ Loop shaping │ MIMO,   │ Coprime factor │ Bandwidth,   │ Moderate    │
│ (McFarlane)  │ linear  │ (unstructured) │ roll-off     │             │
└──────────────┴─────────┴────────────────┴──────────────┴─────────────┘

WHEN TO USE EACH:
  PID:        Simple SISO plants, operator tuning required, embedded control
  LQR/LQG:   MIMO systems, known model, no uncertainty model required
  H∞:        MIMO systems with unstructured uncertainty, mixed sensitivity
  μ:          Multiple independent parameter uncertainties, MIMO aerospace/vehicles
  McFarlane:  Want intuitive loop shape + automatic robustification
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────┐
│ SCENARIO                     │ RECOMMENDATION                       │
├──────────────────────────────┼───────────────────────────────────────┤
│ Single uncertain gain        │ Gain/phase margins (classical), or   │
│ in SISO plant                │ H∞ sensitivity minimization          │
├──────────────────────────────┼───────────────────────────────────────┤
│ Multiple independent         │ μ-synthesis (D-K iteration)          │
│ parametric uncertainties     │ Model as structured Δ                │
├──────────────────────────────┼───────────────────────────────────────┤
│ High-frequency dynamics      │ H∞ with output multiplicative        │
│ unmodeled (rolloff needed)   │ uncertainty weight; W₂T bound        │
├──────────────────────────────┼───────────────────────────────────────┤
│ Want intuitive design        │ Loop shaping (McFarlane-Glover):     │
│ + automatic robustification  │ shape L₀, then run coprime synthesis │
├──────────────────────────────┼───────────────────────────────────────┤
│ Robust stability only        │ Small gain theorem:                  │
│ (no performance spec)        │ ‖T_zw‖∞ · l(ω) < 1 sufficient      │
├──────────────────────────────┼───────────────────────────────────────┤
│ Real parametric uncertainty  │ μ with real scalings (harder, non-   │
│ (physical parameter ranges)  │ convex); robust LMI methods          │
└──────────────────────────────┴───────────────────────────────────────┘
```

---

## Common Confusion Points

**H∞ norm is not the same as H₂ norm (LQG).** H₂ norm minimizes RMS output for white noise input (average case). H∞ norm minimizes worst-case gain (maximum over all inputs). H∞ is conservative relative to LQG for typical inputs but guaranteed for worst-case disturbances.

**μ < 1 guarantees robust stability, not robust performance.** Robust stability means the closed loop is stable for all Δ in the set. Robust performance requires the performance objective (H∞ bound on T_zw) is met for all Δ. Robust performance is equivalent to a μ condition on an augmented M with the performance channel included as a fictitious full complex block.

**Small gain theorem is sufficient but not necessary for stability.** There exist cases where ‖M‖∞ · ‖Δ‖∞ > 1 but the interconnection is still stable — the theorem is conservative. For structured Δ, μ gives a tighter (less conservative) condition. For unstructured Δ with arbitrary phase, small gain is both necessary and sufficient.

**Loop shaping is different from Bode plot loop design.** Classical Bode plot design shapes the open loop for a specific nominal plant. McFarlane-Glover loop shaping uses the coprime factor framework to guarantee a robust stability margin ε after you've specified the desired loop shape. The robustness guarantee is for coprime factor uncertainty, not for arbitrary unstructured perturbations.

**D-K iteration does not converge to the global minimum of max μ.** It's an alternating optimization (fix C, optimize D; fix D, optimize C) that may converge to a local minimum. Multiple starting points are recommended for critical applications.
