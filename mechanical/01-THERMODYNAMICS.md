# 01 — Thermodynamics

## Laws, Cycles, Entropy, Exergy

The central question in engineering thermodynamics is not "what are the laws" but "what is the maximum useful work extractable from a given energy source, and what destroys availability?" The answer is exergy analysis — the Second Law applied quantitatively. The laws below are the foundation; cycles and exergy analysis (later sections) are the engineering payoff.

```
ENERGY IN ──► [THERMODYNAMIC SYSTEM] ──► USEFUL WORK OUT
                      │
                      ▼
               HEAT REJECTED (unavoidable)
               Second law sets the floor.
```

Thermodynamics answers: **how much work can you extract, and at what cost?**
The answer is always: less than you think, because entropy.

---

## Thermodynamic State Properties

```
EXTENSIVE (scale with mass)        INTENSIVE (independent of mass)
────────────────────────────       ────────────────────────────────
U — internal energy [J]            u = U/m  specific internal energy
H = U + pV  enthalpy [J]           h = H/m  specific enthalpy
S — entropy [J/K]                  s = S/m  specific entropy
V — volume [m³]                    v = V/m  specific volume
G = H − TS  Gibbs free energy      T — temperature [K]
A = U − TS  Helmholtz free energy  p — pressure [Pa]
```

**State functions** depend only on state (path-independent): U, H, S, G, A, p, T, v
**Path functions** depend on process: Q (heat), W (work)
Notation: δQ and δW (inexact differentials) vs dU (exact differential)

---

## The Four Laws

### Zeroth Law — Temperature

Transitivity of thermal equilibrium: A~B and B~C implies A~C. This equivalence relation defines temperature as a well-defined intensive state property.

### First Law — Energy Conservation

**Closed system** (fixed mass, piston-cylinder):
```
dU = δQ − δW
where δW = p dV  (boundary work, PdV work)
```

**Open system** (steady-state, control volume — turbine, pump, heat exchanger):
```
Q̇ − Ẇ_s = ṁ[(h₂ − h₁) + ½(v₂² − v₁²) + g(z₂ − z₁)]
```
where Ẇ_s = shaft work (excludes flow work, which is absorbed into enthalpy h = u + pv).

**Key: enthalpy H = U + pV** is the natural variable for flowing systems because
the pV term accounts for work done pushing fluid into/out of the control volume.

### Second Law — Entropy and Irreversibility

**Clausius inequality:**
```
∮ δQ/T ≤ 0  (equality for reversible cycle, < for irreversible)
```

**Entropy generation:**
```
dS_system = δQ/T + δS_gen    where δS_gen ≥ 0  always
```

Irreversibilities (entropy generators):
- Friction (mechanical)
- Heat transfer across finite ΔT
- Mixing of different substances
- Chemical reactions (irreversible)
- Throttling (Joule-Thomson: isenthalpic, not isentropic)

**Carnot efficiency** — maximum possible for any heat engine between Th and Tc:
```
η_Carnot = 1 − Tc/Th  (temperatures in Kelvin!)
```
Example: Steam power plant with Th=600°C (873K), Tc=40°C (313K):
η_Carnot = 1 − 313/873 = 0.641 = 64.1%
Real plants achieve ~35–45% (irreversibilities in heat transfer, turbine, pump).

### Third Law — Absolute Entropy

```
S → 0  as  T → 0 K  for a perfect crystal
```
This sets an **absolute zero** for entropy, enabling absolute entropy calculations.
Consequence: absolute zero (0 K) is unattainable in finite steps.

---

## Ideal Gas & Real Gas

### Ideal Gas
```
pV = nRT  or  pv = RT  (per unit mass, R = R_universal/M)
```

Specific heats (ideal gas):
```
c_v = (∂u/∂T)_v       c_p = (∂h/∂T)_p = c_v + R
γ = c_p/c_v            (γ = 1.4 for diatomic: air, N₂, O₂)
```

**Isentropic relations** (adiabatic, reversible — ideal gas):
```
T₂/T₁ = (p₂/p₁)^((γ-1)/γ) = (v₁/v₂)^(γ-1)
```
Used constantly for compressors, turbines, nozzles.

### Real Gas — van der Waals
```
(p + a/v²)(v − b) = RT
```
- a/v² correction: intermolecular attractions (reduces pressure)
- b correction: finite molecular volume (reduces available volume)
- Reduces to ideal gas at high T, low p

**Compressibility factor:** Z = pv/RT  (Z=1 for ideal, Z≠1 for real)
Pitzer acentric factor ω for polar molecules. Lee-Kesler tables for engineering.

---

## Power Cycles — T-s Diagrams

The T-s (temperature-entropy) diagram is the power tool: area under process curve = heat exchange, enclosed area = net work.

### Carnot Cycle (theoretical maximum)
```
T
│   2───────3
│   │       │  ← Isothermal expansion (heat in at Th)
Th  │       │
│   │       │
Tc  1───────4  ← Isothermal compression (heat out at Tc)
│   │       │
    ────────── s
    Adiabatic processes (vertical lines on T-s)
```
η = 1 − Tc/Th. Impractical (isothermal processes require infinitely slow operation).

### Rankine Cycle (Steam Power Plant)

```
       BOILER (heat in)
     3──────────────4 (superheat)
     │               │
     │               │ ← Steam turbine (work out)
     │               │
     2               5 (wet steam or superheated)
     │               │
     1───────────────  ← Condenser (heat out at low T)
   Pump
   (work in)

Processes:
  1→2: Pump (isentropic compression of liquid)
  2→3: Subcooled liquid heating
  3→4: Vaporization at constant pressure
  4→5: Superheat
  5→1: Turbine expansion (isentropic ideal)
  1→: Condenser (constant pressure heat rejection)
```

**Rankine efficiency:**
```
η = (h₄ − h₅) − (h₂ − h₁)    ← turbine work − pump work
    ─────────────────────────
           h₄ − h₂             ← heat input

Typical: 35–45% for modern supercritical plants (620°C, 25 MPa)
```

**Improvements:** Reheat (re-superheat after partial expansion), Regeneration (feedwater heating by turbine extraction steam → raised average Th).

### Brayton Cycle (Gas Turbine / Jet Engine)

```
Processes (air-standard):
  1→2: Isentropic compression (compressor)
  2→3: Constant-pressure heat addition (combustor)
  3→4: Isentropic expansion (turbine)
  4→1: Constant-pressure heat rejection (exhaust/atmosphere)

Efficiency:
  η_Brayton = 1 − 1/r_p^((γ-1)/γ)
  where r_p = p₂/p₁ = pressure ratio

  At r_p = 20 (typical): η ≈ 0.575 (57.5%) theoretically
  Real gas turbines: 35–45% (compressor/turbine isentropic efficiencies ~85–90%)
```

**Back work ratio** = compressor work / turbine work ≈ 40–80% for gas turbines
(contrast: Rankine pump work = 1–2% of turbine work — liquids are nearly incompressible)

**Combined cycle (CCGT):** Gas turbine → exhaust → HRSG → steam Rankine cycle.
Overall efficiency 55–62% — the best thermal efficiency of any commercial power plant.

### Otto Cycle (Spark Ignition / Gasoline Engine)

```
Processes (air-standard):
  1→2: Isentropic compression (compression stroke)
  2→3: Constant-volume heat addition (ignition)
  3→4: Isentropic expansion (power stroke)
  4→1: Constant-volume heat rejection (exhaust blow-down)

η_Otto = 1 − 1/r_c^(γ-1)   where r_c = compression ratio

At r_c = 9 (typical gasoline): η = 1 − 1/9^0.4 = 58% (ideal)
Real: ~25–35% (friction, incomplete combustion, heat loss)
```

**Knock (detonation):** Autoignition before spark → limits compression ratio.
High-octane fuel resists autoignition → allows higher r_c → higher efficiency.

### Diesel Cycle (Compression Ignition)

```
Processes:
  1→2: Isentropic compression (higher r_c than Otto, ~14–22)
  2→3: Constant-pressure heat addition (fuel injection, slower)
  3→4: Isentropic expansion
  4→1: Constant-volume heat rejection

Cutoff ratio: r_c_cutoff = v₃/v₂  (proportional to fuel mass)

η_Diesel = 1 − [1/r_c^(γ-1)] × [(r_cutoff^γ − 1)/(γ(r_cutoff − 1))]

Higher compression ratio → higher efficiency than Otto at same r_c
No knock (autoignition is desired) → can run at r_c = 14–22
Real diesel: 40–45% efficiency
```

### Stirling Cycle (External Combustion)

```
Processes:
  1→2: Isothermal expansion (heat in at Th)
  2→3: Constant-volume cooling (regenerator)
  3→4: Isothermal compression (heat out at Tc)
  4→1: Constant-volume heating (regenerator)

η_Stirling = η_Carnot = 1 − Tc/Th  (with ideal regenerator!)
```
Practical Stirling engines: 30–40%. Used in spacecraft (RTG), submarines (Sweden/Japan AIP), micro-CHP. Resurgent interest for H₂ combustion.

---

## Refrigeration & Heat Pumps

### Vapor Compression Cycle (Reverse Rankine)

```
     ┌──────CONDENSER──────┐
     │   (high p, heat out) │
     │                     │
  Compressor             Expansion
  (work in)               valve
     │                     │
     │    EVAPORATOR       │
     └──────────────────────┘
        (low p, heat in from space to be cooled)
```

**COP (Coefficient of Performance):**
```
COP_refrigerator = Q_L / W_net = Q_L / (Q_H − Q_L)
COP_heat_pump    = Q_H / W_net = Q_H / (Q_H − Q_L)

Carnot limits:
  COP_R,max = Tc / (Th − Tc)
  COP_HP,max = Th / (Th − Tc)
```

**Common refrigerants:**
| Refrigerant | GWP | Application | Phase-out? |
|-------------|-----|-------------|------------|
| R-134a (HFC) | 1430 | Automotive, refrigeration | Phasing out |
| R-410A (HFC blend) | 2088 | HVAC | Phasing out (EU 2025) |
| R-32 (HFC) | 675 | Room AC | Transition |
| R-290 (propane) | 3 | Small appliances | Growing |
| CO₂ (R-744) | 1 | Supermarkets, heat pumps | Growing |
| NH₃ (R-717) | 0 | Industrial | Standard |
| R-1234yf (HFO) | 4 | Automotive | Replacement for R-134a |

---

## Exergy Analysis

**Exergy** = maximum useful work extractable as system reaches dead state (T₀, p₀):
```
Ex = (U − U₀) + p₀(V − V₀) − T₀(S − S₀)    [closed system]
ex_flow = h − h₀ − T₀(s − s₀)                [flow exergy]
```

**Exergy destruction** = T₀ × S_gen (second-law irreversibility, always ≥ 0)

**Second-law efficiency:**
```
η_II = actual work / maximum possible work = η_actual / η_Carnot
```
Useful for diagnosing where inefficiency lives (unlike first-law efficiency which can be misleadingly high).

**Example:** Electric water heater, η_I = ~99% (nearly all electricity → heat).
But η_II ≈ 5–15%: you're using high-quality work (electricity) to raise water temperature by 40°C — hugely wasteful thermodynamically. A heat pump COP=3 means η_II ≈ 40–50%.

---

## Combustion Thermodynamics

**Stoichiometric air-fuel ratio (AFR) for octane C₈H₁₈:**
```
C₈H₁₈ + 12.5O₂ → 8CO₂ + 9H₂O
AFR_stoich = 15.1 kg_air / kg_fuel
```

**Equivalence ratio:** φ = AFR_stoich / AFR_actual
- φ < 1: lean mixture (excess air) → lower temperatures, lower NOx, higher efficiency
- φ > 1: rich mixture (fuel-rich) → CO production, incomplete combustion, soot

**Adiabatic flame temperature** (T_ad): maximum temperature if no heat loss:
```
H_products(T_ad) = H_reactants(T_initial) + LHV
```
Propane in air: T_ad ≈ 2267 K
Hydrogen in air: T_ad ≈ 2480 K

**Heating values:**
- LHV (Lower Heating Value): water in products as vapor
- HHV (Higher Heating Value): water in products as liquid
- Boiler efficiency often quoted on LHV basis

---

## Phase Equilibria

### Phase Diagrams (pure substance)

```
P (pressure)
│     SOLID    │  LIQUID   │
│              │           │
│              CP (critical)│ ── SUPERCRITICAL FLUID
│    ──────────┤           │
│    │ TRIPLE  │           │
│    │  POINT  └───────────┴──► T
│    │
│    └── VAPOR
│
└──────────────────────────────► T
```

**Key points for water:** Triple point: 0.01°C, 611 Pa | Critical point: 374°C, 22.1 MPa
Above critical point: no phase boundary — fluid can transition between liquid-like and gas-like without crossing a phase boundary.

**Clausius-Clapeyron (saturation curve slope):**
```
dp/dT = h_fg / (T v_fg)   ≈ h_fg p / (RT²)  for ideal vapor

where h_fg = latent heat of vaporization, v_fg = v_g − v_l
```

### Psychrometrics (Humid Air)
```
Humidity ratio: ω = m_water / m_dry_air = 0.622 p_w/(p − p_w)
Relative humidity: φ = p_w / p_sat(T)
Enthalpy: h = h_a + ω h_g ≈ c_pa T + ω(h_fg + c_pv T)
Dew point T_dp: temperature at which φ → 1
Wet bulb temperature T_wb: equilibrium temperature of evaporating water
```
Psychrometric chart: plots all these properties on ω vs T diagram.

---

## Common Confusion Points

**First law signs:** Physics convention: dU = δQ − δW (work done BY system is positive).
Engineering convention: sometimes dU = δQ + δW (work done ON system positive). Check your source.

**Isentropic ≠ adiabatic ≠ reversible:** Isentropic = adiabatic AND reversible (dS=0). Adiabatic alone means no heat transfer but can still be irreversible (entropy generated by friction). A wet sponge compressed adiabatically: not isentropic.

**Enthalpy for open systems:** h = u + pv already includes flow work. Don't double-count pv work in open system energy balance.

**COP > 1 is fine:** Heat pump COP=4 is not violating anything. You're moving heat, not creating it.

**T in Rankine or Kelvin:** η_Carnot = 1 − Tc/Th requires absolute temperature scale. °C will give wrong answers.

**LHV vs HHV:** Most US engineering tables use LHV; European often HHV. Boiler efficiency >100% on LHV basis is physically correct (condensing boiler recovers latent heat).

---

## Decision Cheat Sheet

| Question | Tool | Formula |
|----------|------|---------|
| Maximum efficiency of heat engine | Carnot | η = 1 − Tc/Th |
| Actual cycle efficiency | First law | η = W_net/Q_in |
| Irreversibility in a device | Second law | Ẋ_destroyed = T₀ Ṡ_gen |
| Maximum refrigeration COP | Carnot reversed | COP = Tc/(Th − Tc) |
| Isentropic temperature ratio | Ideal gas + adiabatic | T₂/T₁ = (p₂/p₁)^((γ-1)/γ) |
| Steam turbine exit state | h-s (Mollier) diagram | use steam tables |
| Compressor work | Open system 1st law | Ẇ = ṁ(h₂ − h₁) |
| Flame temperature | Enthalpy balance | H_prod(T_ad) = H_react + LHV |
| Which cycle for my power plant? | Efficiency vs complexity | See cycle comparison above |
