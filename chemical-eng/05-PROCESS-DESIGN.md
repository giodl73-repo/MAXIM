# 05 — Process Design & Safety

## Flowsheets, Heat Integration, Process Control, HAZOP

```
PROCESS DESIGN HIERARCHY (Douglas Doctrine)

Step 1:  Batch vs continuous?      → Continuous for >10,000 tons/yr
Step 2:  Input-output structure    → Select reactions, raw materials, products
Step 3:  Recycle structure         → Where to recover unreacted feed?
Step 4:  Separation system         → Sequence for separating products
Step 5:  Heat integration          → Minimize utilities via heat exchange network
Step 6:  Control system design     → Stabilize inventory, reject disturbances
Step 7:  Safety analysis (HAZOP)   → Identify and mitigate hazards
Step 8:  Economic optimization     → Maximize NPV
```

---

## Process Documentation Hierarchy

### Block Flow Diagram (BFD)

```
[RAW MATERIALS] → [REACTOR] → [SEPARATOR] → [PRODUCT]
                               ↓
                         [RECYCLE STREAM]

Boxes = processes, arrows = streams with molar flow/composition
Purpose: overall material balance, major unit operations
```

### Process Flow Diagram (PFD)

More detailed: major equipment (with designations like E-101, V-201), all process streams with flow rate, T, P, composition, heat duties. Stream table below diagram. Major control loops.

### Piping & Instrumentation Diagram (P&ID)

**Most detailed:** All equipment, instruments, control valves, line sizes, interlocks, safety systems.

**ISA-5.1 instrumentation symbols:**
```
Circle with letters:
  First letter = measured variable:
    T = temperature, P = pressure, F = flow, L = level, A = analyzer
  Second/third letter = function:
    I = indicator, C = controller, T = transmitter, A = alarm, V = valve

Example: FIC-101 = Flow Indicating Controller, loop 101
         PSV-201 = Pressure Safety Valve, loop 201
         TT-301 = Temperature Transmitter, loop 301

Lines:
  Process line (thick solid)
  Instrument signal (dashed)
  Pneumatic signal (dashes with dots)
  Electrical signal (thin solid with //)
```

---

## Material and Energy Balances

### Degree of Freedom Analysis

```
DOF = number of unknowns − number of independent equations
DOF = 0: exactly determined (solve)
DOF > 0: underspecified (need more information)
DOF < 0: overspecified (inconsistent — check equations)
```

**For a steady-state unit with N_s streams, each with C components + T + P:**
```
Unknowns: N_s × (C + 2)  [flows, compositions, T, P for each stream]
Equations: C material balances + 1 energy balance + phase equilibrium + specifications
```

### Recycle Streams — Tearstream Convergence

```
A → B → ... → RECYCLE → A

Iterative convergence (successive substitution):
  1. Guess recycle stream composition/flow
  2. Propagate around loop → get new recycle estimate
  3. Check convergence
  4. Repeat (possibly slow)

Wegstein acceleration or Broyden's method speeds convergence
ASPEN, HYSYS handle automatically — but understand convergence behavior
```

### Energy Balance — Heat Duties

```
For each unit operation:
  Q = ṁ Cp ΔT  (sensible heat)
  Q = ṁ ΔH_rxn  (reaction heat)
  Q = ṁ λ (latent heat for phase change)

Utilities:
  HP steam (200°C+): high-T heating
  LP steam (100–150°C): general heating
  Cooling water (25–40°C): general cooling
  Chilled water (5–15°C): moderate refrigeration
  Refrigerant (−40°C to 0°C): deep refrigeration (expensive)
```

---

## Heat Integration — Pinch Analysis

Pioneered by Linnhoff (1970s). Minimizes energy consumption by matching hot and cold streams internally before using utilities.

### Composite Curves

```
Hot composite: combine all hot streams (need cooling) on T-H diagram
Cold composite: combine all cold streams (need heating) on T-H diagram

Pinch point: minimum temperature approach ΔT_min between curves
  Below pinch: heating utility only
  Above pinch: cooling utility only
  At pinch: both

Q_H,min (minimum hot utility) = right end extension of cold curve
Q_C,min (minimum cold utility) = left end extension of hot curve
```

**Pinch design rules:**
1. Don't transfer heat across the pinch (will increase both hot and cold utility)
2. Above pinch: matches must have CP_hot ≤ CP_cold  (CP = flow × heat capacity)
3. Below pinch: matches must have CP_hot ≥ CP_cold

**Benefits:** Pinch analysis typically reveals 20–40% energy savings opportunity in existing plants.

### Network Design

```
Maximum energy recovery (MER) design:
  1. Start at pinch, work outward
  2. Match streams according to rules
  3. Count exchangers: N_ex = S + L − 1  (S = streams, L = loops in network)
  4. Reduce exchangers by stream splitting or accepting small utility penalty

Software: ASPEN Energy Analyzer, SuperTarget, PinchExpress
```

---

## Process Simulation

**Purpose:** Model full plant steady-state (or dynamic) behavior to design and optimize.

**Steady-state simulators:** Aspen Plus, HYSYS (AspenTech), PRO/II, CHEMCAD.

**Workflow:**
```
1. Select thermodynamic model (critical choice!):
   - Hydrocarbon processing: Peng-Robinson
   - Polar systems: NRTL or UNIQUAC
   - Electrolytes: e-NRTL
   - Polymers: PC-SAFT

2. Define streams: composition, T, P, flow

3. Build flowsheet: connect unit operations

4. Specify: which variables free, which fixed

5. Converge: simulator solves DOF = 0 system
   - Sequential modular: solve each unit in sequence
   - Equation-oriented: solve all equations simultaneously (better for design spec)

6. Sensitivity analysis: vary one parameter → plot output
7. Optimization: maximize NPV or minimize utility cost subject to constraints
```

---

## Process Control

### PID Control Fundamentals

The PID algorithm is identical to software control loops (autoscalers, rate limiters, backpressure controllers). P = scale by current error. I = accumulate past error to eliminate steady-state offset (but risks windup — the same queue accumulation problem under sustained overload that anti-windup resets and backpressure mechanisms solve). D = react to rate of change (predictive damping). See `control-theory/` for the full treatment.

```
PID controller output:
  u(t) = K_c [e(t) + (1/τ_I) ∫e dt + τ_D de/dt]

e(t) = set point − measured value  (error signal)
K_c = controller gain (proportional)
τ_I = integral time constant (eliminates offset)
τ_D = derivative time constant (reduces overshoot)

Transfer function: G_c(s) = K_c(1 + 1/(τ_I s) + τ_D s)

Proportional only: steady-state offset (need I action to eliminate)
PI: no offset, good for most applications (most common)
PID: reduces overshoot for slow processes; risky for noisy processes
```

**Ziegler-Nichols tuning (step test method):**
```
From open-loop step response (FOPDT model: gain K_p, time constant τ_p, dead time θ):
  K_c = 1.2τ_p/(K_p θ)
  τ_I = 2θ
  τ_D = 0.5θ
```

### Control Loop Design

**Typical loops in a plant:**
```
Level control: use proportional-only (avoid reset windup) or P+I
  Fast response unnecessary; smooth flow to downstream more important

Flow control: fast → tight PI control
  Use low gain, fast reset (τ_I ≈ 0.1–1 min)

Temperature control: slower process → may use PID
  Distillation column: tray temperature → reflux ratio or reboiler duty

Pressure control: critical safety parameter
  Relief valve (hard safety); pressure control valve (regulatory)

Composition control: slow (analyzer delay) → cascade control often used
  Inner loop (fast: T or flow) → outer loop (slow: composition)
```

**Cascade control:**
```
Master (primary) controller: composition or temperature (slow)
Slave (secondary) controller: flow or T (fast)
Master setpoint → slave setpoint → slave output → process → master measurement
```

**Plantwide control strategy:**
1. Control all inventories (levels, pressures) — otherwise unstable
2. Product quality specs — primary objective
3. Safety constraints — hard limits always override
4. Economic objectives — optimize within safety/quality bounds

---

## Process Safety

### Inherently Safer Design (Kletz)

Four strategies, in order of preference:
```
1. MINIMIZE: reduce quantities of hazardous material
   (small continuous reactor vs large batch vessel)

2. SUBSTITUTE: replace hazardous with less hazardous
   (use dilute acid instead of concentrated; change solvent)

3. MODERATE: use less hazardous process conditions
   (lower T, lower P, diluted instead of concentrated)

4. SIMPLIFY: eliminate or reduce complexity
   (fewer connections, fewer isolation valves, simpler design)
```

### HAZOP (Hazard and Operability Study)

**Engineering bridge:** HAZOP is systematic fault injection testing — chaos engineering before chaos engineering existed. Each guide word below is a fault category applied to every process node:

```
HAZOP GUIDE WORD     FAULT INJECTION EQUIVALENT
──────────────────────────────────────────────────────────────────────────
NO / NOT             Null input, zero throughput, connection drop
MORE                 Overload, buffer overflow, resource exhaustion
LESS                 Timeout, underflow, degraded throughput
REVERSE              Backpressure, deadlock, inverted dependency
AS WELL AS           Contamination, mixed state, unexpected side-channel
PART OF              Partial failure, incomplete write, split-brain
OTHER THAN           Wrong type, format error, misrouted message
```

The structured per-node walkthrough — asking "what if MORE flow at this point?" for every stream — is the same systematic enumeration that FMEA and chaos experiments use. The difference: HAZOP is done on paper before the plant is built.

Systematic team review of process by applying guide words to each node (stream or equipment):

```
Guide words:
  NO / NOT: complete negation (no flow, no reaction)
  MORE:     quantitative increase (high flow, high T, high P)
  LESS:     quantitative decrease (low flow, low T)
  REVERSE:  opposite (reverse flow, back-pressure)
  AS WELL AS: additional component (contamination, extra phase)
  PART OF:  incomplete (concentration too low, partial failure)
  OTHER THAN: complete substitution (wrong material, different phase)

For each guide word + parameter: identify cause → consequence → safeguards → actions
```

**HAZOP team:** Process engineer, operations, instrumentation engineer, maintenance, HAZOP leader (facilitator), scribe. 1–2 weeks for typical plant design.

### Layers of Protection Analysis (LOPA)

Quantitative risk screening: are existing safeguards sufficient?

```
Scenario: Initiating event (IE) + enabling conditions → hazard

Frequency of unmitigated event = f_IE × P_E1 × P_E2 × ... (enabling conditions)

Independent Protection Layers (IPL): BPCS, alarm + operator, SIS, physical protection (relief valve), containment

Each IPL has probability of failure on demand (PFD):
  BPCS: 0.1 (10% failure)
  Relief valve: 0.01
  SIS (SIL2): 0.01

Mitigated frequency = f_IE × ΠPFDᵢ(IPLs)
Target: mitigated frequency < 10⁻⁴/yr for serious injury
```

### Relief System Design (API 520/521)

```
Relief scenarios (must consider all):
  1. Fire (vessel surrounded by fire → boiling/vapor generation)
  2. Control valve failure (open → overpressure)
  3. Blocked outlet (flow continues, pressure rises)
  4. Heat exchanger tube failure (high-P tube leaks into low-P shell)
  5. Loss of cooling (exothermic reaction runway)
  6. Liquid expansion (thermal expansion of trapped liquid)

Relief valve sizing:
  A = W / (C K_d P₁ √(M/(Z T₁)))   (for vapor, from API 520)
  A = area, W = mass flow, C = gas constant, K_d = discharge coefficient
  P₁ = relieving pressure, M = molecular weight, Z = compressibility, T₁ = temperature
```

---

## Process Economics

### Capital Cost Estimation

```
Lang factor method:
  FCI (Fixed Capital Investment) = Lang factor × Σ(equipment purchase cost)
  Lang factor: 3–4 for fluid processing, 4–5 for mixed fluid/solid, 5–6 for solid

Purchased equipment cost C_p:
  C_p = C_b (S/S_b)^n   (capacity scaling)
  n ≈ 0.6–0.7 ("six-tenths rule")   → scale up 10× capacity: cost only 4–5×

Order of magnitude: ±30–50%
Preliminary estimate: ±15–25%
Definitive estimate: ±5–10% (requires detailed design)
```

### Profitability Analysis

```
NPV = Σ (C_t / (1+i)^t) − C₀

IRR: rate i where NPV = 0
Payback period: years to recover initial investment

Simple profitability:
  Revenue = selling price × production rate
  Operating cost = raw material + utilities + maintenance + labor
  Gross profit = Revenue − Operating cost
  Net profit = Gross profit − Depreciation − Taxes
  ROI = Net profit / FCI × 100%
```

---

## Common Confusion Points

**PFD vs P&ID:** PFD shows process — streams, major equipment, basic control. P&ID shows engineering — all instruments, all control valves, line sizes, safety systems. P&ID is the document used for HAZOP and plant construction.

**HAZOP is not a checklist:** HAZOP systematically applies guide words to every line and vessel. It's a team exercise requiring process knowledge, not a solo desk exercise. It finds hazards that weren't in anyone's mental model.

**Pinch above = need heat, pinch below = need cooling:** A common mistake. Rethink: above the pinch, hot streams need to be cooled (but there's no cold stream below the pinch to take that heat — it came from hot utility). Above pinch requires HOT utility. Below pinch requires COLD utility.

**Relief valve vs control valve:** Control valve (regulating, continuous modulation). Relief valve (safety, opens only on demand, self-closing). Rupture disk (non-reclosing, one-time-use, upstream of relief valve for corrosive service).

**Heat integration constraint:** Don't recover heat across the pinch — this seems to save energy locally but forces more utility use overall. This is the fundamental insight of pinch technology.

---

## Decision Cheat Sheet

| Design task | Tool/Approach | Output |
|-------------|--------------|--------|
| Material balance with recycle | DOF analysis + successive substitution | Converged stream compositions |
| Energy efficiency improvement | Pinch analysis | Q_H,min, Q_C,min, HEN |
| Full plant simulation | ASPEN Plus or HYSYS | Steady-state flowsheet |
| Control loop tuning | Ziegler-Nichols or IMC | K_c, τ_I, τ_D |
| Cascade vs single loop | Identify fast inner variable | T or flow as inner; composition outer |
| Hazard identification | HAZOP with guide words | Action items, safeguards |
| Risk quantification | LOPA | Mitigated event frequency vs target |
| Relief valve size | API 520/521 | Required orifice area |
| Project profitability | NPV/IRR analysis | Accept if NPV > 0, IRR > WACC |
| Capital cost estimate | Lang factor method | ±30% estimate |
