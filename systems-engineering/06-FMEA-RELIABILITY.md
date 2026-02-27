# FMEA, Fault Trees, and Reliability Engineering

## The Big Picture

Reliability engineering quantifies the probability that a system will perform its required function for a specified time under stated conditions. FMEA and FTA are the two primary analytical tools: FMEA works bottom-up (what happens if this component fails?); FTA works top-down (what combinations of failures cause this bad outcome?).

```
RELIABILITY ANALYSIS METHODS
──────────────────────────────────────────────────────────────────
BOTTOM-UP: What failures can occur and what are their effects?
  FMEA  (Failure Mode and Effects Analysis)
  FMECA (FMEA + Criticality Analysis)

TOP-DOWN: What combinations lead to a specific bad outcome?
  FTA   (Fault Tree Analysis)
  ETA   (Event Tree Analysis) — conditional probability of outcomes

QUANTITATIVE RELIABILITY:
  RBD   (Reliability Block Diagram)
  MTBF, MTTR, Availability, MTTF calculations
  Weibull analysis (failure distribution)
  Markov analysis (complex redundancy)
```

---

FMEA is the physical-systems equivalent of distributed systems failure analysis: for each component (service/node/link), what happens if it fails? How does that cascade? Is there a SPOF? The "local effect -> next-higher effect -> end effect" chain maps to "service failure -> dependency cascade -> user-visible impact." The RPN (Severity x Occurrence x Detection) parallels SLO/error-budget thinking: severity = impact on user; occurrence = failure rate; detection = monitoring coverage. High-RPN items are the reliability equivalent of high-severity, low-detection service risks.

## FMEA (Failure Mode and Effects Analysis)

### FMEA Process

```
FMEA WORKFLOW
──────────────────────────────────────────────────────────────────
1. Define SCOPE and BOUNDARIES
   What level of indenture? (System / Subsystem / Component)
   What is the operational mode? (Normal / Emergency / Startup)

2. IDENTIFY FUNCTIONS of each item
   What does this component/function do?

3. IDENTIFY FAILURE MODES
   How can each function fail?
   Fail to function: open circuit, spring fails to return
   Partial function: wrong value output, low pressure
   Unintended function: valve opens when should be closed

4. IDENTIFY EFFECTS
   Local effect: effect on this component
   Next higher effect: effect on subsystem
   End (system) effect: effect on mission / user / safety

5. ASSESS SEVERITY, OCCURRENCE, DETECTION (for FMEA/FMECA with RPN)
   Severity:   1–10 (impact of effect)
   Occurrence: 1–10 (likelihood of failure mode)
   Detection:  1–10 (ease of detecting before it causes effect)

6. CALCULATE RPN (Risk Priority Number)
   RPN = Severity × Occurrence × Detection
   High RPN → prioritize for mitigation action

7. IDENTIFY MITIGATION ACTIONS
   Design change: eliminate or reduce failure mode
   Redundancy: add backup component
   Fault detection: add monitoring/alerting
   Maintenance: scheduled inspection to catch before failure
```

### FMEA Worksheet

| Item | Function | Failure Mode | Local Effect | End Effect | S | O | D | RPN | Action |
|------|----------|-------------|-------------|------------|---|---|---|-----|--------|
| Fuel pump | Deliver fuel at 50 psi | Pump fails to rotate | No fuel flow | Engine flame-out | 9 | 2 | 3 | 54 | Add redundant pump |
| Fuel pump | Deliver fuel at 50 psi | Pump delivers low flow | Reduced pressure | Engine underpowered | 6 | 3 | 4 | 72 | Low-pressure warning |
| Check valve | Prevent backflow | Fails open | Backflow | Fuel system contamination | 7 | 2 | 5 | 70 | Test at maintenance interval |

**S, O, D scales (SAE J1739 / AIAG standard):**

```
SEVERITY:  1=None, 2=Very minor, 3=Minor, 4=Low, 5=Moderate,
           6=Significant, 7=High, 8=Very high, 9=Hazardous w/warning,
           10=Hazardous w/o warning

OCCURRENCE: 1=Remote (1 in 10^6), ... 5=Occasional (1 in 400),
            ... 10=Almost certain (> 1 in 2)

DETECTION: 1=Almost certain to detect, 5=Moderate chance,
           10=Cannot detect
```

### Design FMEA vs Process FMEA

```
DFMEA (Design FMEA)          PFMEA (Process FMEA)
────────────────────────     ────────────────────────
Analyzes DESIGN decisions    Analyzes MANUFACTURING
  and components               and assembly processes
Done during design phase     Done during process design
Owner: Design engineer       Owner: Manufacturing engineer
Focus: Does the design       Focus: Can we make it right?
  work correctly?              Will the process introduce defects?

DFMEA failure mode:          PFMEA failure mode:
  Component fails to operate   Operator installs part backwards
  Component wears too fast     Fixture holds wrong dimension
  Component fails under load   Heat treatment temp too high
```

### FMECA (FMEA + Criticality Analysis)

```
CRITICALITY ANALYSIS
──────────────────────────────────────────────────────────────────
MIL-STD-1629A method:

Criticality Number = Failure mode ratio × Failure rate × Time

  Cn = αβλt

where:
  α = failure mode ratio (fraction of all failures that are this mode)
  β = conditional probability failure mode causes end effect
  λ = part failure rate (from MIL-HDBK-217 or field data)
  t = mission duration

Criticality Category:
  Category I: Catastrophic (loss of life, vehicle)
  Category II: Critical (mission failure, major damage)
  Category III: Marginal (degraded mission, minor damage)
  Category IV: Negligible (no impact)

Criticality matrix: plots Criticality Number vs Category
  Upper right = highest priority for mitigation
```

---

## Fault Tree Analysis (FTA)

### FTA Methodology

FTA is deductive — starts from an undesired top event and systematically identifies the combinations of events (fault conditions) that cause it.

```
FTA APPROACH
──────────────────────────────────────────────────────────────────
1. Define TOP EVENT (undesired outcome)
   "Aircraft engine flame-out during cruise"
   "Software system unavailable > 1 hour"

2. IDENTIFY IMMEDIATE CAUSES using logic gates
   What combinations of lower-level events cause the top event?

3. DECOMPOSE each cause until:
   Basic events (component failures, human errors) reached
   Cut sets can be identified

4. CALCULATE probability of top event
   Using component failure rates and Boolean algebra
```

### FTA Gates and Symbols

```
FAULT TREE SYMBOLS
──────────────────────────────────────────────────────────────────
TOP EVENT:        ┌─────────┐
                  │ Engine  │
                  │ Flame-out│
                  └────┬────┘
                       │

OR GATE:           ┌───┴───┐         Any ONE input causes output
                   │  OR   │
                   └───────┘
                   Probability = 1 - ∏(1-Pi)  (if independent)

AND GATE:          ┌───┴───┐         ALL inputs required for output
                   │  AND  │
                   └───────┘
                   Probability = ∏Pi  (if independent)

BASIC EVENT:       ◯                 Bottom-level failure event
                                     Has a failure probability/rate

UNDEVELOPED:       ◇                 Not developed further
                                     (outside scope or unknown)

INHIBIT:           INHIBIT           Basic event only causes output
                    gate              if conditioning event also true

TRANSFER:          △  (triangle)     Continuation on another page
```

### Fault Tree Example

```
EXAMPLE: Aircraft Fuel System FTA
──────────────────────────────────────────────────────────────────
          ┌──────────────────────────────────┐
          │ TOP: Engine loses fuel supply    │
          └──────────────┬───────────────────┘
                         │
                    ┌────┴────┐
                    │   OR    │
                    └────┬────┘
          ┌──────────────┼──────────────┐
          │              │              │
    ┌─────▼─────┐  ┌─────▼─────┐ ┌─────▼──────────┐
    │Pump A     │  │Pump A AND │ │Fuel line        │
    │ fails     │  │Pump B fail│ │blockage         │
    └───────────┘  └─────┬─────┘ └────────────────┘
    P(pump_A_fail)       │
         = λt      ┌────┴────┐
                   │   AND   │
                   └────┬────┘
              ┌─────────┴──────────┐
         ┌────▼────┐          ┌────▼────┐
         │Pump A   │          │Pump B   │
         │ fails   │          │ fails   │
         └─────────┘          └─────────┘

With AND gate and independent failures:
  P(both pumps fail) = P(A) × P(B) = λ²t²

Single pump (OR gate at top):
  P(failure) = P(pump fail) = λt
  Example: λ = 10⁻⁵ per hour, t = 1000h → P = 0.01 (1%)

Dual redundant pumps (AND gate):
  P(failure) = (λt)² = (0.01)² = 10⁻⁴ (0.01%)

Redundancy reduces failure probability by orders of magnitude.
```

### Cut Sets and Minimal Cut Sets

```
CUT SETS
──────────────────────────────────────────────────────────────────
Cut set: set of basic events that together cause top event
Minimal cut set (MCS): smallest cut set (no unnecessary events)

Top event fails if ANY minimal cut set fails.

Example:
  MCS1 = {Pump A failure}          (single point of failure)
  MCS2 = {Pump B failure}          (second SPOF)
  MCS3 = {Valve fails closed}      (third SPOF)
  MCS4 = {Pump A AND Pump B AND Crossfeed valve fails open}

Single-element MCS = Single Point of Failure (SPOF)
  → Design must eliminate or add detection/mitigation

Importance analysis:
  Birnbaum importance: which component most affects top-event probability
  Criticality importance: probability component is in a failed MCS
  Used to prioritize reliability improvements
```

---

## Reliability Mathematics

### Failure Rate and MTBF

```
RELIABILITY FUNDAMENTALS
──────────────────────────────────────────────────────────────────
Failure rate λ: probability of failure per unit time (constant in mid-life)
  Units: failures per hour (or per 10⁶ hours = FIT — Failures In Time)

MTBF (Mean Time Between Failures):
  MTBF = 1/λ  [for constant failure rate — exponential distribution]
  If λ = 10⁻⁵ failures/hour → MTBF = 100,000 hours

Reliability R(t): probability of surviving to time t
  R(t) = e^(-λt)  [exponential distribution]

  R(1000h) for λ = 10⁻⁵: R = e^(-0.01) = 0.990 = 99%
  R(10000h): R = e^(-0.1) = 0.905 = 90.5%

Failure probability F(t) = 1 - R(t)
  F(1000h) = 0.01 = 1% probability of failure in 1000 hours
```

### The Bathtub Curve

```
BATHTUB CURVE (failure rate vs time)
──────────────────────────────────────────────────────────────────
Failure
Rate
│
│ ╲                                                  /
│  ╲                              ──────────────   /
│   ╲      Constant failure rate (useful life)   /
│    ╲────────────────────────────────────────  /
│                                              /
│                                            /  Wear-out
└────────────────────────────────────────────────────────► Time
  Infant    │                            │
  mortality  Burn-in complete             Wear-out begins

Infant mortality: manufacturing defects, assembly errors
  → Remove by burn-in (operate to failure in factory)

Useful life: constant failure rate → exponential distribution
  → Most reliability calculations use this regime

Wear-out: aging, fatigue, corrosion
  → Weibull distribution (β > 1) models increasing failure rate
  → Predictive maintenance targets this regime
```

### Availability

```
AVAILABILITY CALCULATIONS
──────────────────────────────────────────────────────────────────
Inherent Availability (Ai):
  Ai = MTBF / (MTBF + MTTR)
  MTBF = Mean Time Between Failures
  MTTR = Mean Time To Repair (active repair only)

  If MTBF = 1000h, MTTR = 2h:
  Ai = 1000 / (1000 + 2) = 0.998 = 99.8%

Operational Availability (Ao):
  Ao = MTBM / (MTBM + MDT)
  MTBM = Mean Time Between Maintenance (includes preventive)
  MDT = Mean Down Time (includes logistics, admin delay)

System availability with k-of-n redundancy:
  2-of-2 series: A = A₁ × A₂
  1-of-2 parallel: A = 1 - (1-A₁)(1-A₂)
  k-of-n: binomial distribution
```

### Reliability Block Diagrams (RBD)

```
RBD STRUCTURES
──────────────────────────────────────────────────────────────────
SERIES: All blocks must work
  ─[A]─[B]─[C]─
  R_system = R_A × R_B × R_C
  Less reliable than weakest component

PARALLEL (all active): any block keeps system alive
  ─┬─[A]─┬─
   ├─[B]─┤
   └─[C]─┘
  R_system = 1 - (1-R_A)(1-R_B)(1-R_C)
  More reliable than best component

k-of-n (M-of-N): k of n blocks must work
  Binomial: R = Σ C(n,i) × R^i × (1-R)^(n-i) for i=k to n

Load sharing: failure of one increases load on remaining
  More complex — failure rate of survivors changes
  Requires Markov analysis or simulation
```

---

## Reliability Prediction Methods

```
RELIABILITY PREDICTION STANDARDS
──────────────────────────────────────────────────────────────────
MIL-HDBK-217F (military):
  Electronic component failure rate models
  λ = λ_base × π_T × π_Q × π_E × ...
  Temperature factor (π_T): Arrhenius equation
  Quality factor (π_Q): MIL-spec vs commercial
  Environment factor (π_E): ground vs airborne vs space
  Status: "frozen" (no updates since 1995), still used in defense

Telcordia (formerly Bellcore) SR-332:
  Commercial electronics, telecommunications
  Better models for modern components than MIL-HDBK-217

IEC 62380 (formerly RDF 2000):
  European standard, mission profile-based
  Better temperature modeling

OREDA (Offshore Reliability Data):
  Field data from offshore oil/gas equipment
  Empirical failure rates from actual operations

Physics of Failure (PoF):
  Model failure mechanisms (fatigue, corrosion, electromigration)
  CALCE (University of Maryland) methodology
  Better accuracy than empirical methods
  More effort — used for critical components
```

---

## Allocation and Design for Reliability

```
RELIABILITY ALLOCATION (MARKOV or APPORTIONMENT)
──────────────────────────────────────────────────────────────────
Given: System reliability requirement R_sys = 0.995 for 1000 hours
Work backward to allocate to subsystems.

Equal allocation:
  n subsystems: R_each = R_sys^(1/n)
  For 5 subsystems: R_each = 0.995^(0.2) = 0.999

Weighted allocation:
  More reliable subsystems get tighter allocation
  Simpler subsystems get less tight requirements
  Uses judgment about relative complexity/reliability

AGREE method:
  Weighted by number of modules and mission time fraction

After allocation:
  Check feasibility (can component reliability be achieved?)
  Verify with BoM failure rate prediction
  Iterate design if prediction shows gap to allocation
```

---

## Decision Cheat Sheet

| Need | Tool |
|------|------|
| Find all ways a system can fail | FMEA (bottom-up) |
| Find what causes a specific failure | FTA (top-down) |
| Quantify probability of bad outcome | FTA with failure rates |
| Prioritize failure modes for mitigation | FMEA RPN or FMECA criticality |
| Find single points of failure | FMEA single-effect items or FTA single-element MCS |
| Calculate system MTBF from components | RBD + failure rate data |
| Predict electronics reliability | MIL-HDBK-217F (defense) or Telcordia SR-332 (commercial) |
| Design to availability requirement | MTBF + MTTR calculation |

---

## Common Confusion Points

**FMEA RPN is misleading**: A severity=10 / occurrence=1 / detection=1 item has RPN = 10, same as severity=3/occurrence=2/detection=2. But the severity=10 item could kill someone. Never sort FMEA solely by RPN — always review high-severity items regardless of RPN. Severity=9 or 10 always requires mitigation.

**MTBF ≠ "expected lifetime"**: MTBF = 100,000 hours does NOT mean the component will last 100,000 hours. Under exponential distribution, a component has ~37% probability of surviving to its MTBF (e^(-1) ≈ 0.368). Half survive to 0.693×MTBF. MTBF is a rate, not a lifetime.

**Redundancy doesn't help with common-cause failures**: Dual redundant pumps have near-zero probability of independent simultaneous failure. But if a manufacturing defect affects both pumps identically, or a single shock event damages both, the redundancy provides zero benefit. Common cause failure analysis is a separate discipline — FMEA often misses it.

**FTA independence assumption**: FTA probability calculation (P_top = P_A × P_B for AND gate) assumes statistical independence. For software faults (two implementations of same algorithm by same team), they may correlate. For environmental failures (power surge, shock), they almost certainly correlate. Document independence assumptions explicitly.

**λ constant = exponential distribution assumption**: Reliability analysis almost always assumes constant failure rate (exponential distribution) for component-level calculations. This is only valid in the useful-life regime (post infant mortality, pre wear-out). Components near end of useful life need Weibull analysis, not exponential.
