# 02 — Chemical Reaction Engineering

## Kinetics, Reactor Design, Selectivity, Catalysis

```
REACTION ENGINEERING WORKFLOW

  KINETICS           REACTOR TYPE         DESIGN EQUATION
  ─────────          ────────────         ───────────────
  -r_A = f(C,T)  →   Batch              → N_A0 dX/dt = -r_A V
                      CSTR (mixed)       → τ = C_A0 X / (-r_A)_exit
                      PFR (plug flow)    → τ = C_A0 ∫dX/(-r_A)
                      Non-ideal          → RTD + model
```

---

## Rate of Reaction

**Definition:** rate of disappearance of A per unit volume [mol/(L·s) or mol/(m³·s)]
```
-r_A = (−1/V)(dN_A/dt)    (batch, intensive, based on volume)
     = −dC_A/dt            (constant-volume batch)
     = k C_A^m C_B^n      (power-law form)

Stoichiometry: aA + bB → cC + dD
  -r_A/a = -r_B/b = r_C/c = r_D/d
```

---

## Reaction Kinetics

### Rate Laws

```
Power-law:    -r_A = k C_A^m C_B^n
  m = order in A, n = order in B, (m+n) = overall order
  k = rate constant [units depend on order]

Determine experimentally:
  Initial rate method: vary C_A (hold C_B const) → ln(-r_A₀) vs ln(C_A₀) → slope = m
  Integral method: assume order → integrate → fit concentration-time data
```

**Arrhenius equation:**
```
k = A exp(−E_a/RT)

A = pre-exponential (frequency) factor [same units as k]
E_a = activation energy [J/mol]
R = 8.314 J/(mol·K)

ln k = ln A − E_a/(RT)   → plot ln k vs 1/T → slope = −E_a/R

Rule of thumb: k doubles every 10°C near room temperature (for E_a ≈ 50 kJ/mol)
E_a values: simple bond rotation ~10 kJ/mol; enzyme catalysis ~50 kJ/mol; combustion ~100–250 kJ/mol
```

### Integrated Rate Laws

| Order | -r_A | Integrated | Half-life t₁/₂ |
|-------|------|-----------|---------------|
| Zero | k | C_A = C_A0 − kt | C_A0/(2k) |
| First | kC_A | C_A = C_A0 e^(-kt), or ln(C_A0/C_A) = kt | ln2/k |
| Second | kC_A² | 1/C_A − 1/C_A0 = kt | 1/(kC_A0) |

---

## Ideal Reactor Types

### Engineering Bridge: Reactor Types as Processing Architectures

```
REACTOR TYPE        PROCESSING ARCHITECTURE EQUIVALENT
──────────────────────────────────────────────────────────────────────────
Batch               Batch/MapReduce processing
  all material in     → all data in, process, all results out
  react, drain out    → no flow during processing; downtime between batches

CSTR                Perfectly mixed message queue
  continuous flow     → continuous ingest, every item sees same conditions
  exit = interior     → exit state = queue state (no ordering preserved)

PFR                 Streaming pipeline / FIFO
  continuous flow     → each item processed in sequence
  no axial mixing     → order preserved; no item "sees" any other
  each element reacts → each message processed independently in transit
  for time τ = V/v₀
```

### Batch Reactor (BR)

No flow in or out. All material reacts together.

```
Mole balance: N_A0 dX/dt = (-r_A) V
For constant volume: dX/dt = (-r_A)/C_A0

Reaction time for conversion X:
  t = C_A0 ∫₀^X dX/(-r_A(X))    ← Levenspiel integral

Advantages: flexible (different products in same vessel), small scale
Disadvantages: batch time + downtime, non-steady product quality
```

### Continuous Stirred Tank Reactor (CSTR)

Perfectly mixed → exit composition = bulk composition = inlet composition.

```
Design equation (steady state):
  V/F_A0 = τ/C_A0 = X/(-r_A)_exit

  F_A0 = inlet molar flow [mol/s]
  τ = V/v₀ = space time [s]
  (-r_A)_exit = rate evaluated at exit composition (lowest rate = worst case)

CSTR performance for first-order: C_A0/C_A = 1 + kτ → X = kτ/(1+kτ)
```

### Plug Flow Reactor (PFR)

No mixing in flow direction; each fluid element reacts identically.

```
Design equation:
  V/F_A0 = ∫₀^X dX/(-r_A(X))    ← Levenspiel integral, same form as batch

PFR performance for first-order: C_A/C_A0 = e^(-kτ) → X = 1 − e^(-kτ)
```

### PFR vs CSTR Comparison

```
For equal V and same X:
  Elementary A → B (first order, positive order kinetics):
    PFR always outperforms CSTR (CSTR operates at lowest rate; PFR at all rates)
    Ratio: V_CSTR/V_PFR → 1 as X→0, grows as X→1

For non-monotonic rates (autocatalytic):
  CSTR can outperform PFR at low conversions
  Optimal: CSTR to optimum X_opt, then PFR to final X

CSTR in series → approaches PFR performance as N → ∞
```

**Levenspiel plot (1/(-r_A) vs X):**
```
PFR volume = area under curve (integral)
CSTR volume = rectangle of width X and height 1/(-r_A)_exit

For positive-order kinetics: curve is monotonically increasing → PFR area < CSTR area
```

---

## Non-Isothermal Reactors

**Energy balance on PFR:**
```
ρ C_p v₀ dT/dz = (-ΔH_rxn)(-r_A) A_cross - Ua(T − T_coolant)

Adiabatic: set Ua = 0:
  T = T₀ + (−ΔH_rxn) C_A0 X / (ρ C_p)
  Adiabatic temperature rise: ΔT_ad = (−ΔH_rxn) C_A0 / (ρ C_p)
```

**CSTR stability — multiple steady states:**
```
Heat generation: Q_gen = (-ΔH_rxn)(-r_A)V  (S-shaped vs X)
Heat removal: Q_rem = F_A0 C_p(T − T₀) + UA(T − T_c)  (straight line)
Intersections = steady states (up to 3)

Lower SS: stable (low T, low X) — ignition point
Middle SS: unstable (saddle point — not observed)
Upper SS: stable (high T, high X) — desired operating point

Bifurcation: as cooling increases, upper SS extinguishes → reactor "quenches"
```
This is the same positive feedback instability that appears in distributed systems: higher temperature → faster reaction → more heat generated → higher temperature. The S-curve/straight-line intersection analysis is structurally identical to a service where load increases latency → triggers retries → increases load. The upper steady state corresponds to "overloaded but stable"; the lower to "healthy"; the middle is unreachable. Bifurcation (losing the upper SS when cooling increases) maps to a cascade failure where the overloaded state quenches and the system drops to the low-throughput regime — the chemical engineering equivalent of a thundering herd recovery.

---

## Multiple Reactions: Selectivity

For reactions generating both desired product D and undesired product U:

```
A → D  (desired),   rate r_D
A → U  (undesired), rate r_U

Instantaneous selectivity: S_D/U = r_D/r_U

Maximize selectivity:
  If order of D > order of U in A: high [A] favors D → PFR or batch (not CSTR)
  If order of D < order of U in A: low [A] favors D → CSTR or differential PFR
  Temperature effects: high T if E_D > E_U (D has higher activation energy)

Overall yield: Y_D = (moles D formed) / (moles A fed initially)
Overall selectivity: S_D = (moles D formed) / (moles A reacted)
```

---

## Catalysis and Heterogeneous Reactors

### Langmuir Adsorption Isotherm

```
θ_A = K_A p_A / (1 + K_A p_A + K_B p_B + ...)

θ_A = fraction of surface sites occupied by A
K_A = adsorption equilibrium constant (dimensionless or 1/pressure)

Langmuir-Hinshelwood mechanism (bimolecular):
  -r_A = k K_A K_B p_A p_B / (1 + K_A p_A + K_B p_B)²
  Common in catalytic reactions (NH₃ synthesis, CO oxidation)

Eley-Rideal mechanism:
  -r_A = k K_A p_A p_B / (1 + K_A p_A)
  One species adsorbed, other from gas phase
```

### Diffusion Limitations (Pore Diffusion)

In porous catalyst pellets, reactant must diffuse into pores before reacting.

```
Thiele modulus:
  φ = R √(k/D_eff)   [R = pellet radius, k = rate const, D_eff = effective diffusivity]
  φ ≪ 1: diffusion fast (kinetic control)
  φ ≫ 1: diffusion slow (diffusion limited, rate ∝ 1/R)

Effectiveness factor η:
  η = actual rate / rate if no diffusion limitation = tanh(φ)/φ   (slab geometry)
  η → 1 as φ → 0 (kinetic control)
  η → 1/φ as φ → ∞ (diffusion limited)

Weisz-Prater criterion (no diffusion limitation if):
  C_WP = (-r_A)_obs ρ_c R² / (D_eff C_As) < 1
```

---

## Residence Time Distribution (RTD) — Non-Ideal Reactors

Real reactors deviate from ideal (CSTR/PFR) due to channeling, dead zones, bypassing.

**RTD measurement:**
```
Pulse experiment: inject tracer at t=0, measure concentration C(t) in exit
  E(t) = C(t) / ∫C(t) dt   (normalized: ∫E(t) dt = 1)
  Mean residence time: t̄ = ∫t E(t) dt

Step experiment: switch to tracer feed, measure F(t) = ∫₀^t E(t) dt
```

**RTD comparison:**
```
Ideal CSTR:   E(t) = (1/τ) exp(−t/τ)   (exponential decay)
Ideal PFR:    E(t) = δ(t − τ)          (Dirac delta at mean residence time)
Real reactor: between these extremes
```

**Tanks-in-series model (N CSTRs):**
```
E(t) = [1/(N−1)!] (N/τ)^N t^(N-1) exp(−Nt/τ)

N → 1: CSTR; N → ∞: PFR
Fit N from variance: σ² = τ²/N → N = τ²/σ²
```

**Dispersion model (plug flow with axial mixing):**
```
∂C/∂t = D_a ∂²C/∂z² − v ∂C/∂z
Peclet number: Pe = vL/D_a
  Pe → ∞: ideal PFR; Pe → 0: ideal CSTR
```

---

## Common Confusion Points

**Space time τ ≠ residence time t̄:** τ = V/v₀ (based on inlet volumetric flow). Actual residence time = V/v (based on reactor volumetric flow at conditions). Equal only if density constant (liquid, or gas at isothermal constant p).

**-r_A in CSTR evaluated at exit:** In a CSTR, the entire vessel is at exit conditions. So (-r_A) is evaluated at C_A_exit (lowest concentration), giving worst-case rate. This is why CSTRs need larger volume than PFRs for the same conversion.

**Conversion X vs yield Y vs selectivity S:** X = fraction of feed converted. Y = fraction forming desired product. S = fraction of converted reactant forming desired product. Y = X × S.

**Equilibrium vs kinetics:** Thermodynamic equilibrium (K_eq) sets the maximum achievable conversion. Kinetics determines how fast you get there. You can't get above equilibrium conversion by adding catalyst — only by changing T or removing products.

**Effectiveness factor and scale-up:** Lab: small particles → η ≈ 1 (kinetic regime). Industrial: larger pellets → η < 1 (diffusion limited). Scale-up with same particle size maintains η. Bigger particles → lower η → lower apparent rate.

---

## Decision Cheat Sheet

| Design question | Tool | Key formula |
|----------------|------|------------|
| Reactor size for conversion X | Levenspiel integral | V = F_A0 ∫dX/(-r_A) |
| CSTR vs PFR? | Compare Levenspiel plots | PFR = area, CSTR = rectangle |
| Temperature effect on rate | Arrhenius | k = A exp(−Ea/RT) |
| Optimal T for exothermic rxn | Balance equilibrium + kinetics | Start high, cool down |
| Maximize selectivity | Compare orders in A, T effects | See selectivity section |
| Check diffusion limitation | Weisz-Prater criterion | C_WP < 1 for no limitation |
| Non-ideal reactor | RTD + model | E(t) from tracer experiment |
| Number of CSTR stages needed | Tanks-in-series | N = τ²/σ² from RTD |
