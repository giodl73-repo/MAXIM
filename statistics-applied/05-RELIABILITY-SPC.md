# Reliability & Statistical Process Control

## The Big Picture

```
+------------------------------------------------------------------+
|     RELIABILITY ENGINEERING + SPC: PRODUCT & PROCESS QUALITY     |
|                                                                  |
|  RELIABILITY (time-to-failure perspective):                      |
|  Product: does it fail? when? → Weibull, bathtub curve           |
|  System: redundancy architecture → series/parallel models        |
|  Field: repair cycle → MTBF, MTTR, availability                  |
|  Software: MTTF, chaos engineering, reliability growth           |
|                                                                  |
|  SPC (Statistical Process Control):                              |
|  Process: in control? improving? → control charts                |
|  Product: meets spec? → process capability (Cp, Cpk)             |
|  Incoming: accept or reject lots? → acceptance sampling          |
|                                                                  |
|  ORIGINS:                                                        |
|  Reliability: WWII military requirements → reliability engineering|
|  SPC: Walter Shewhart (1924, Bell Labs) → Deming in Japan 1950   |
|  Six Sigma: Motorola 1986; GE 1990s adoption                     |
+------------------------------------------------------------------+
```

---

## Reliability Fundamentals

```
FUNDAMENTAL FUNCTIONS:

Probability density function (failure time distribution): f(t)
Cumulative Distribution Function: F(t) = P(T ≤ t) = ∫₀ᵗ f(u)du
  → Probability of failure by time t

Reliability function: R(t) = P(T > t) = 1 − F(t)
  → Probability of surviving past time t
  → R(0) = 1; R(∞) = 0

Failure rate / Hazard function: h(t) = f(t) / R(t)
  → Instantaneous rate of failure given survival to t
  → NOT a probability: can be > 1; has units of 1/time

Cumulative hazard function: H(t) = ∫₀ᵗ h(u)du = −ln R(t)
  → R(t) = exp(−H(t))

RELATIONSHIP:
  Know any one of {f(t), F(t), R(t), h(t), H(t)} → derive all others
  f(t) = h(t) × R(t) = h(t) × exp(−H(t))
```

---

## The Bathtub Curve

```
BATHTUB CURVE: h(t) over product lifetime

         High failure rate
         |
h(t)     |  Early              Constant           Wear-out
         |  failures  _______  failures  ________  failures
         | /         |                            |       \
         |/          |                            |        \
         +--phase-1--|--------phase-2-------------|--phase-3-→ t
         0          t₁                           t₂

PHASE 1 — INFANT MORTALITY (β < 1 in Weibull):
  Decreasing failure rate
  Cause: manufacturing defects, weak components, poor assembly
  Strategy: burn-in testing (operate under stress before shipping)
  → Fails out the weak units; remaining units are more reliable

PHASE 2 — USEFUL LIFE (β ≈ 1, exponential):
  Approximately constant failure rate
  Cause: random events — accidents, use variability, random component failure
  MEMORYLESS: past use history is irrelevant to future failure
  MTTF = 1/λ (characteristic of exponential distribution)
  → The assumption behind most simple reliability calculations

PHASE 3 — WEAR-OUT (β > 1 in Weibull):
  Increasing failure rate
  Cause: physical degradation — fatigue, corrosion, wear, aging
  Strategy: preventive maintenance before reaching this region
  → Scheduled replacement before typical wear-out time

SOFTWARE NOTE:
  Software doesn't "wear out" (no physical degradation)
  Software reliability: infant mortality phase (bugs found and fixed early)
  → After debugging, approximately constant failure rate
  → Major releases reset to infant mortality phase
```

---

## Weibull Distribution

```
WEIBULL PDF:
  f(t) = (β/η) × (t/η)^(β−1) × exp(−(t/η)^β)
  β = shape parameter (determines phase: <1, =1, >1)
  η = scale parameter (characteristic life = time at which 63.2% have failed)

  Verification: F(η) = 1 − exp(−(η/η)^β) = 1 − exp(−1) ≈ 0.632 ✓

SHAPE PARAMETER β (the key):
+----------+---------------------------+------------------------+
| β < 1    | Decreasing failure rate   | Infant mortality       |
| β = 1    | Constant failure rate     | Exponential (random)   |
| β ≈ 3.5  | ≈ Normal distribution     | Symmetric wear-out     |
| β > 1    | Increasing failure rate   | Wear-out / fatigue     |
+----------+---------------------------+------------------------+

HAZARD FUNCTION:
  h(t) = (β/η) × (t/η)^(β−1)
  β<1: h(t) decreasing; β=1: h(t) = 1/η (constant); β>1: h(t) increasing

WEIBULL PLOT (linearization):
  Take log twice:
  ln(−ln(1−F(t))) = β × ln(t) − β × ln(η)
  → Plot ln(−ln(1−F̂(t))) vs ln(t) → straight line if Weibull
  Slope = β; intercept at ln(t) = 0 gives −β × ln(η)
  → Graphical estimation of parameters; check of fit

MLE ESTIMATION:
  β̂ and η̂ via maximum likelihood (numerical optimization; no closed form for β̂)
  R: fitdistrplus::fitdist('weibull'); Python: scipy.stats.weibull_min.fit()
  Standard errors from Fisher information matrix
  Confidence bounds on reliability function: Greenwood-type formula or bootstrap

APPLICATIONS:
  Ball bearing fatigue life: β ≈ 1.5
  Capacitor dielectric breakdown: β ≈ 2-4
  Human mortality (in adults): β ≈ 5-6 (Gompertz-Weibull)
  Software time-to-failure: often exponential (β=1 phase) after debugging
```

---

## System Reliability

```
SERIES SYSTEM (all components must function):
  R_sys(t) = R₁(t) × R₂(t) × ... × Rₙ(t)
  → Weakest link: one failure = system failure
  → System reliability ≤ any component's reliability

  n identical components: R_sys = Rⁿ
  n=10, R=0.99: R_sys = 0.99¹⁰ ≈ 0.90
  n=100, R=0.99: R_sys = 0.99¹⁰⁰ ≈ 0.366
  → System reliability degrades exponentially with number of series components

PARALLEL SYSTEM (at least one must function):
  R_sys(t) = 1 − ∏(1 − Rᵢ(t))
  → Redundancy: system fails only if ALL fail
  → System reliability ≥ any component's reliability

  n=2, R=0.90: R_sys = 1 − (0.10)² = 0.99
  n=3, R=0.90: R_sys = 1 − (0.10)³ = 0.999

K-OF-N SYSTEM:
  System functions if at least k of n components function
  Used in: RAID arrays (RAID-5: any 1 of n can fail; RAID-6: any 2)
  R_sys = Σ_{i=k}^{n} C(n,i) × R^i × (1−R)^(n−i)

AVAILABILITY:
  For repairable systems: A = MTBF / (MTBF + MTTR)
  MTBF: mean time between failures (exponential: MTBF = 1/λ)
  MTTR: mean time to repair

  THE NINES:
  +----------+-------------+-------------------------+
  | 99%      | 2 nines     | 87.6 hr/yr downtime     |
  | 99.9%    | 3 nines     | 8.76 hr/yr              |
  | 99.99%   | 4 nines     | 52.6 min/yr             |
  | 99.999%  | 5 nines     | 5.26 min/yr             |
  | 99.9999% | 6 nines     | 31.5 sec/yr             |
  +----------+-------------+-------------------------+
  Azure/AWS SLA: typically 99.9% per service (multi-region: higher)
  Financial systems: 99.99%+ target

FAULT TREE ANALYSIS (FTA):
  Top-down: system failure → combinations of component failures
  AND gates: all inputs must fail (parallel)
  OR gates: any input fails (series)
  Quantify: assign failure rates to basic events → compute P(top event)
  FMEA (Failure Mode and Effects Analysis):
  Bottom-up: for each component, enumerate failure modes → effects → risk
  RPN = Severity × Occurrence × Detection (1-10 each) → prioritize mitigations
```

---

## Statistical Process Control

```
WALTER SHEWHART (1924): Bell Labs, book "Economic Control of Quality of Manufactured Product" (1931)
  INSIGHT: variation in processes is always present; not all variation is the same

  Common cause (chance) variation: inherent randomness in the process
    → Cannot be eliminated; is the "natural" background noise
    → Stable, predictable → process is "in control"

  Special cause (assignable) variation: signal of an unusual event
    → Identifiable source: tool wear, operator error, bad material lot, machine jam
    → Process is "out of control"
    → Should be investigated and eliminated

CONTROL CHART PURPOSE:
  Distinguish: is this variation common cause OR special cause?
  → Common cause: leave process alone (adjusting makes things WORSE)
  → Special cause: find root cause, eliminate

  "Tampering": adjusting a process in response to common cause variation
  → Increases total variation (Walker, 1947; Deming's funnel experiment)
  → One of the most common quality mistakes in manufacturing
```

### X-bar and R Charts

```
SETUP:
  Take subgroups of size n (typically n=4 or 5) at regular intervals
  Compute: X̄ (subgroup mean) and R (subgroup range = max − min)

X-BAR CHART (monitors process mean):
  Center line: X̄̄ = grand mean = Σ X̄ᵢ / m  (m = number of subgroups)
  Upper/Lower Control Limits:
  UCL = X̄̄ + A₂ × R̄      LCL = X̄̄ − A₂ × R̄
  R̄ = average range
  A₂ is a constant depending on subgroup size n:
  n=2: A₂=1.880; n=4: A₂=0.729; n=5: A₂=0.577; n=10: A₂=0.308

R CHART (monitors process variability):
  Center line: R̄
  UCL = D₄ × R̄      LCL = D₃ × R̄
  n=2: D₄=3.267, D₃=0; n=4: D₄=2.282, D₃=0; n=5: D₄=2.115, D₃=0
  (D₃=0 for n<7; range cannot be negative)

  WHY 3-SIGMA LIMITS?
  If process is normal and in control:
  P(point outside 3σ limits) = 0.0027 (false alarm rate = 0.27%)
  Shewhart's economic choice: balance false alarm cost vs detection speed
  (Tighter limits: more false alarms; wider: slower detection)

INDIVIDUALS AND MOVING RANGE (I-MR):
  For single observations (n=1); cannot compute within-subgroup range
  Moving range: MR_i = |X_i − X_{i-1}|
  X chart: UCL/LCL = X̄ ± 3σ̂, where σ̂ = MR̄/d₂ (d₂ = 1.128 for n=2)
  → Common in: continuous processes, slow-rate sampling, chemical processes
```

### Out-of-Control Rules

```
WESTERN ELECTRIC (WECO) RULES:
  Out of control if any of:
  1. One point beyond ±3σ (basic Shewhart rule)
  2. Two of three consecutive points beyond ±2σ (on same side)
  3. Four of five consecutive points beyond ±1σ (on same side)
  4. Eight consecutive points on same side of centerline (run rule)
  5. Six consecutive points trending in same direction
  6. Fifteen consecutive points in Zone C (within ±1σ, stratification — too stable)
  7. Fourteen consecutive points alternating up/down (zigzag)
  8. Eight consecutive outside Zone C (avoiding center)

Rules 1-4 are most commonly used (Nelson rules include variants)

ACTION PROTOCOL:
  Point out of control → do NOT immediately adjust process
  Step 1: Is there an obvious assignable cause? (operator change, material lot, machine jam)
  Step 2: Investigate cause; mark on chart with notation
  Step 3: If cause found and removed → process returns to control
  Step 4: If no cause found → adjust control limits? Or investigate more?

PHASE I vs PHASE II:
  Phase I: establish control limits from historical data
    → Remove out-of-control points with assignable causes
    → Recalculate limits on remaining points
    → Iterate until all remaining points in control
  Phase II: monitor ongoing process with established limits
    → Points triggering rules → investigate immediately
```

---

## Process Capability

```
CAPABILITY vs PERFORMANCE:
  Capability: potential of a process WHEN IN CONTROL
  Performance: actual output including out-of-control periods

PROCESS CAPABILITY INDICES:
  Specification limits: USL (upper) and LSL (lower) set by engineering/customer
  Process spread: 6σ (contains ≈ 99.73% of output under normality)

  Cp = (USL − LSL) / 6σ
  "Width ratio": spec width / process spread
  → Cp = 1: process spread exactly fills spec (barely acceptable)
  → Cp = 1.33: 4σ margin on each side (minimum for most manufacturing)
  → Cp = 2: Six Sigma potential
  LIMITATION: Cp ignores process centering (only looks at spread)

  Cpk = min((USL − μ) / 3σ, (μ − LSL) / 3σ)
  "Centering-adjusted capability"
  → Takes the minimum of upper and lower potential
  → Cpk = Cp when process is perfectly centered on spec midpoint
  → Cpk < Cp when process is off-center
  → Cpk < 0: mean is outside a spec limit

  Minimum Cpk guidelines:
  ≥ 1.00: barely capable (6.68% defective if centered)
  ≥ 1.33: standard requirement (0.007% defective if centered)
  ≥ 1.67: advanced quality (0.0001% defective if centered)
  ≥ 2.00: Six Sigma level (3.4 DPMO with 1.5σ shift; see below)

SIX SIGMA:
  Motorola 1986, GE 1990s mainstream adoption
  Goal: process with Cp = Cpk = 2.0 (theoretically)

  3.4 DPMO ← THIS IS THE NUMBER PEOPLE QUOTE
  IMPORTANT: Motorola assumed a 1.5σ long-term process drift/shift
  Short-term: Cp=2 → ±6σ → 0.002 DPMO (pure theory)
  Long-term: with 1.5σ shift → 3.4 DPMO (the quoted number)
  → "Six Sigma" means different things to different people

  DPMO = Defects Per Million Opportunities
  +-----+------+----------+
  |Sigma|Cpk   |DPMO(1.5σ)|
  +-----+------+----------+
  | 1σ  | 0.33 |  697,672 |
  | 2σ  | 0.67 |  308,537 |
  | 3σ  | 1.00 |   66,807 |
  | 4σ  | 1.33 |    6,210 |
  | 5σ  | 1.67 |      233 |
  | 6σ  | 2.00 |      3.4 |
  +-----+------+----------+
```

---

## Software Reliability and Chaos Engineering

```
SOFTWARE RELIABILITY MODELS:

JELINSKI-MORANDA (1972):
  Assume N₀ initial faults; each fix removes one fault
  Failure rate: λ_i = φ(N₀ − (i−1))  after (i−1) fixes
  → Decreasing failure rate as faults removed
  Simplest reliability growth model; unrealistic assumptions but pedagogically useful

NHPP MODELS (Non-Homogeneous Poisson Process):
  General framework: expected cumulative failures Λ(t) = ∫₀ᵗ λ(u)du
  Goel-Okumoto (1979): Λ(t) = a(1 − exp(−bt))  (S-curve shape)
  Musa-Okumoto (1984): log-Poisson; better for some software empirically

RELIABILITY GROWTH:
  During testing: faults found and fixed → failure rate decreases
  This is the infant mortality phase for software
  After release: approximately constant failure rate (exponential)
  Major version release: resets to growth phase (new code → new faults)

CHAOS ENGINEERING (Netflix, 2010):
  Proactively introduce failures to find weaknesses before they cause incidents
  "Chaos Monkey": randomly terminates production instances
  Chaos experiments:
  1. Hypothesize: "system tolerates X losing 1 availability zone"
  2. Define steady state: measure normal system behavior
  3. Inject failure: shut down AZ, add latency, corrupt packets
  4. Measure: does steady state hold? Where does it fail?
  5. Fix and iterate

  Reliability implications:
  • Forces actual distributed system resilience (not just documented resilience)
  • Finds SINGLE POINTS OF FAILURE that architecture review missed
  • Netflix "Chaos Gorilla": terminates an entire AZ
  • "Chaos Kong": terminates an entire region
  Analogy: controlled burns in forestry to prevent uncontrolled fires
```

---

## Acceptance Sampling

```
SETUP:
  Receive lot of N items; don't want 100% inspection (expensive/destructive)
  Sample n items → observe d defectives → accept if d ≤ c (acceptance number)
  AQL (Acceptable Quality Level): maximum acceptable fraction defective

OPERATING CHARACTERISTIC (OC) CURVE:
  P(accept lot | true defective fraction p) vs p
  Ideal: accept all lots with p < AQL; reject all with p > AQL
  Reality: statistical curve → errors in both directions
  Producer's risk (α): P(reject | lot is actually good, p = AQL)
  Consumer's risk (β): P(accept | lot is actually bad, p = LTPD)

MIL-STD-105 / ANSI/ASQ Z1.4:
  Standard tables for sampling plans by lot size + AQL
  Normal, tightened, reduced inspection levels
  Switching rules: tighten if quality deteriorates; reduce if consistently good
  Single, double, multiple sampling plans

WHEN 100% INSPECTION:
  Very small lots; catastrophic consequences of defect
  Destructive testing: never 100% (test destroys item)
  High reliability requirements: cannot rely on sampling alone

LIMITATIONS:
  Acceptance sampling screens LOTS; does not improve PROCESS
  If process produces 10% defective: sampling plan rejects most lots
  → Root cause fix (SPC, process improvement) is more valuable than sampling
  Deming: "Cease dependence on inspection to achieve quality"
  → Quality comes from process improvement, not inspection at end
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What does Weibull β < 1 indicate? | Infant mortality — decreasing failure rate. Fix: burn-in testing before shipping. β=1: exponential (random failures). β>1: wear-out (increasing failure rate). |
| What is η in Weibull? | Scale parameter (characteristic life) = time at which 63.2% of units have failed (since F(η) = 1 − e⁻¹ ≈ 0.632 regardless of β). |
| What is Cpk = 1.33 in practical terms? | 4σ between mean and each spec limit. Defect rate ≈ 64 PPM (if centered). Minimum acceptable for most industrial manufacturing. Below 1.0: process is barely fitting spec. |
| What does SPC distinguish? | Common cause variation (inherent, stable, do not tamper) vs special cause variation (assignable event → investigate and eliminate). |
| What is tampering? | Adjusting a process in response to common cause variation — increases total variation rather than reducing it. Deming's funnel experiment demonstrates this. |
| What is MTTF vs MTBF? | MTTF: mean time to failure for non-repairable units. MTBF: mean time between failures for repairable systems. Availability = MTBF/(MTBF+MTTR). |
| Five nines availability = how much downtime per year? | 99.999% = 5.26 minutes per year downtime. |

---

## CS and Systems Bridges

| Reliability / SPC concept | CS / systems analogue |
|---|---|
| Control chart (Shewhart X̄/R chart) | Statistical process monitoring: control limits (±3σ from process mean) are the principled foundation for alert thresholds in application monitoring — the rules for detecting special causes (8 consecutive points above mean, 2 of 3 beyond 2σ) are exactly the alert sensitivity/specificity tradeoffs in SLO monitoring |
| Common cause vs special cause variation | Noise vs signal in telemetry: common cause = intrinsic system variability (do not alert, do not adjust); special cause = assignable event (alert, investigate, eliminate) — tampering on common cause variation increases total variance, the same as over-eager autoscaling on random load spikes |
| CUSUM / EWMA charts | Sequential change-point detection: CUSUM accumulates signed deviations to detect sustained shifts; EWMA exponentially weights recent observations — both are streaming anomaly detectors equivalent to those in time-series monitoring frameworks |
| Weibull β < 1 (infant mortality) | Burn-in period / early-life failure: high initial failure rate that decreases over time — the statistical basis for burn-in testing hardware before deployment; in software, analogous to canary deployment catching integration failures that only manifest early in a component's operating life |
| Weibull β = 1 (random failures, constant hazard) | Memoryless Poisson process: failures arrive at constant rate regardless of age; service request arrivals and hardware random failures both follow this; exponential inter-arrival times, constant MTBF |
| Weibull β > 1 (wear-out) | Aging degradation: failure rate increases with age — storage device write endurance, battery cycle life, mechanical wear; reliability-centered maintenance (replace before wear-out inflection) mirrors proactive infrastructure replacement before MTTF distribution tail |
| Six Sigma (3.4 DPMO, Cpk = 1.5) | Quality SLO: the "five nines" (99.999%) of manufacturing; 3.4 DPMO ≈ 0.00034% defect rate; Cpk = 1.5 is the process capability target — directly analogous to software availability SLAs and error budgets, where the allowed failure rate is the spec limit |
| FMEA (Failure Mode and Effects Analysis) | Fault tree / threat model: systematic enumeration of failure modes, each with severity × probability → RPN (Risk Priority Number); prioritizes reliability investment — identical structure to security threat modeling (threat × impact × likelihood) |
| Availability = MTBF/(MTBF+MTTR) | SLO availability budget: MTBF is the average up-time interval; MTTR is the average repair time; higher MTTR shrinks availability even with identical MTBF — the operational implication is that fast recovery (deployment speed, automated rollback) contributes as much to availability as failure prevention |

## Common Confusion Points

**Cpk doesn't measure short-term vs long-term:** Cp and Cpk are instantaneous capability estimates from process data. The "1.5σ shift" in Six Sigma is an empirical adjustment Motorola made for long-term process drift — it's an assumption, not derived from the Cpk formula. Don't confuse Cp/Cpk with the 3.4 DPMO number.

**Control charts vs spec limits are conceptually different:** Control limits (based on process variation: ±3σ from centerline) indicate statistical control. Spec limits (from engineering/customer) define acceptance. A process can be in statistical control but produce 50% out-of-spec product (capable of control but not capable of meeting spec). These are independent assessments.

**MTBF doesn't mean "half fail by MTBF":** For exponential distribution (constant failure rate), F(MTBF) = 1 − e⁻¹ ≈ 63.2% fail by MTBF, not 50%. Median life (50% fail point) = MTBF × ln(2) ≈ 0.693 × MTBF. The "mean" of an exponential is not the 50th percentile.

**Chaos engineering is not the same as load testing:** Load testing: push system to capacity, measure when it fails. Chaos engineering: inject specific failure modes (network partition, instance termination, latency injection) to test resilience to real failure scenarios, not just scale. The goal is discovering hidden dependencies, not finding the throughput limit.
