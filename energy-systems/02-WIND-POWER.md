# Wind Power

## The Big Picture

Wind is now the cheapest source of new electricity in most of the world for onshore,
and offshore wind is the dominant strategy for decarbonizing high-latitude grids
(UK, northern Europe, US Northeast) where solar resources are weak. Understanding
the Betz limit, the capacity factor economics, and the wake/siting problem is the
core. The generator and grid integration layers sit on top.

```
WIND ENERGY STACK

  WIND RESOURCE (Weibull distribution of wind speeds)
        │
        │  Cut-in wind speed (~3-4 m/s): turbine starts generating
        │  Rated wind speed (~11-13 m/s): full rated power
        │  Cut-out wind speed (~25 m/s): turbine shuts down (storm protection)
        v
  +---------------------+
  |  ROTOR SYSTEM        |  Blades capture kinetic energy from wind
  |  Blades (3-blade)    |  Lift-based aerodynamics (not drag)
  |  Hub                 |  Pitch control: adjust blade angle
  +---------------------+
        │  Shaft rotation (low-speed, ~10-20 RPM)
        v
  +---------------------+
  |  DRIVETRAIN          |  Gearbox (steps up to ~1500 RPM)
  |  Gearbox or          |  OR direct-drive (no gearbox, large PMSG)
  |  Direct-drive       |
  +---------------------+
        │  High-speed shaft (gearbox) or direct connection
        v
  +---------------------+
  |  GENERATOR           |  DFIG (doubly-fed induction) or PMSG (permanent magnet)
  |  + Power Electronics |  Full-scale converter (PMSG) or partial-scale (DFIG)
  +---------------------+
        │  Variable-frequency AC → grid-frequency AC
        v
  +---------------------+
  |  TRANSFORMER +       |  Step up to collection voltage (33 kV onshore,
  |  TOWER SWITCHGEAR    |  66 kV offshore increasingly)
  +---------------------+
        │
        v
  GRID (via collection cable or overhead line → substation → transmission)
```

---

## Betz Limit — The Physics Ceiling

This is a fundamental aerodynamic result that no turbine can exceed.
The derivation is actuator disk theory — a classic fluid mechanics result.

```
  ACTUATOR DISK MODEL

  Upstream:              Disk:              Downstream:
  velocity = v₁         velocity = v_d     velocity = v₂
  pressure = p₁         acts on area A     pressure = p₁ (ambient)
                          │
                          │  Force extracted = A × (p+ - p-)
                          │  (pressure drop across disk)

  Key results from momentum theory:

  1. Velocity at disk: v_d = (v₁ + v₂) / 2
     (average of upstream and downstream)

  2. Axial induction factor: a = 1 - v_d/v₁
     Range: a = 0 (no extraction) to a = 0.5 (full extraction)

  3. Power extracted:
     P = ½ ρ A v₁³ × 4a(1-a)²

  4. Power coefficient:
     Cp = P / P_available = 4a(1-a)²

  5. Maximum Cp: dCp/da = 0 → a = 1/3 → v₂ = v₁/3
     Cp_max = 4 × (1/3) × (2/3)² = 16/27 ≈ 0.593

  THE BETZ LIMIT: No turbine rotor can extract more than 59.3%
  of the kinetic energy in the wind passing through it.
  This is not a technology limit — it's fundamental physics.

  Real turbines:
  Modern large turbines: Cp = 0.45-0.50 (at optimal wind speed)
  Cp vs Betz: ~80-85% of theoretical maximum
  (remaining losses: tip vortices, drag, finite blade number)
```

### The Power Equation

```
  P = ½ × ρ × A × v³ × Cp

  where:
    ρ = air density (1.225 kg/m³ at sea level, 15°C)
    A = rotor swept area = π × R² (R = rotor radius in meters)
    v = wind speed (m/s)
    Cp = power coefficient (0.45-0.50 for modern turbines)

  CRITICAL INSIGHT: Power scales with v³ (wind speed cubed)
    Double the wind speed → 8× the power
    10 m/s → 20 m/s means 8× more power potential
    This is why siting matters enormously.
    It's also why hub height matters (wind shear increases speed with altitude).

  EXAMPLE: GE 3-MW turbine, rotor diameter 130 m:
    A = π × (65)² = 13,273 m²
    At v = 12 m/s, Cp = 0.48:
    P = ½ × 1.225 × 13,273 × 12³ × 0.48 = ~3.0 MW ✓ (rated power)
```

---

## Turbine Architecture

### Rotor and Blades

```
  BLADE CROSS-SECTION (airfoil):

                    ┌──────────────────────┐
                   /  LIFT (upward/forward)  \
  Wind →          /____________________________\
                  \                            /  ← Trailing edge
                   \__________________________/
                  Leading edge

  Blades use aerodynamic lift (like aircraft wings) NOT drag.
  Lift-drag ratio ~100:1 for modern blades.

  BLADE PARAMETERS:
  • Chord length: varies from root (wide) to tip (narrow)
  • Twist: blade twisted along span (~15° twist root-to-tip)
    → keeps optimal angle of attack at each section despite
      different circumferential velocity (tip moves faster than root)
  • Material: fiberglass-epoxy (dominant), carbon fiber for large blades
  • Length: 50-80 m onshore, 80-115 m+ offshore
  • Mass: 15-25 tonnes each (for 5-7 MW class)
  • Certification life: 20 years (fatigue is the design driver)

  PITCH CONTROL:
  • Blade angle adjusts continuously with wind speed
  • Below rated speed: maximize Cp (track optimal tip-speed ratio)
  • Above rated speed: pitch to reduce Cp, maintain rated power
  • At cut-out: feather to 90° (blade edge into wind, stops rotation)
```

### Tip Speed Ratio (TSR) and the Cp Curve

```
  TIP SPEED RATIO:  λ = (tip velocity) / (wind speed)
                      = (ω × R) / v

  Cp vs λ curve (characteristic of rotor design):

  Cp
  │        ╭─────╮
  0.50│      ╭╯     ╰╮
  0.45│    ╭╯         ╰╮
  0.40│   ╭╯             ╰╮
  0.35│  ╭╯                ╰╮
  0.30│ ╭╯                   ╰────
  0.25│╭╯
     0│─────────────────────────── λ
       0  2  4  6  8  10  12

  Optimal λ for modern 3-blade turbines: ~7-8
  At optimal λ: Cp = 0.45-0.50

  Turbine control: vary rotor speed (variable-speed via power electronics)
  to maintain λ_opt as wind speed changes → maximize Cp at all wind speeds
  (below rated; pitch limiting above rated)

  Fixed-speed turbines (legacy): only optimal at one wind speed
  Variable-speed (modern standard): optimal across full wind range
```

### Tower and Hub Height

```
  WIND SHEAR — velocity increases with height:
    v(h) = v_ref × (h / h_ref)^α

  Where α = wind shear exponent:
    Open flat terrain (IEC Class II): α ≈ 0.14
    Forested/complex terrain:         α ≈ 0.20-0.30

  EXAMPLE: doubling hub height from 80m to 160m in open terrain:
    v_160 = v_80 × (160/80)^0.14 = v_80 × 2^0.14 = v_80 × 1.104
    Power ∝ v³: 1.104³ = 1.34 → 34% more power from same rotor

  Hub height vs cost:
    Standard onshore: 80-120 m (lattice or tubular steel)
    Tall onshore (Germany, forested): 140-180 m (hybrid concrete/steel)
    Offshore: 80-120 m (shorter, stronger winds near surface)

  Turbine scaling trend (capacity vs rotor diameter):
    2000: 0.75 MW, ~50m rotor
    2010: 2.0 MW, ~90m rotor
    2020: 5-6 MW, ~150-170m rotor
    2024: 14-16 MW offshore, ~220-240m rotor (Vestas V236, SGRE SG 14-236 DD)
    IEC 62600: turbines >15 MW under development (GE Haliade, Siemens Gamesa)
```

---

## Drivetrain — Gearbox vs Direct-Drive

```
  GEARBOX DRIVETRAIN (DFIG — common onshore):
  ┌──────────────────────────────────────────────────────┐
  │  Rotor (10-20 RPM)                                   │
  │      │                                               │
  │      └──► [3-stage gearbox] ──► High-speed shaft     │
  │                                    (~1500 RPM)       │
  │                                      │               │
  │                                      └──► DFIG       │
  │                              (doubly-fed induction)  │
  │                                      │               │
  │                              Partial-scale converter │
  │                              (~30% of rated power)   │
  │                              Variable speed ±30% RPM │
  └──────────────────────────────────────────────────────┘

  GEARBOX PROS:  Smaller, lighter generator; cheaper power electronics
  GEARBOX CONS:  Gearbox failure (~3% annual failure rate) = expensive offshore

  ─────────────────────────────────────────────────────────────────

  DIRECT-DRIVE PMSG (dominant offshore, growing onshore):
  ┌──────────────────────────────────────────────────────┐
  │  Rotor (5-15 RPM)                                    │
  │      │                                               │
  │      └──► PMSG (permanent magnet synchronous)        │
  │           Large diameter ring generator              │
  │           No gearbox (no high-speed shaft)           │
  │                │                                     │
  │           Full-scale converter                       │
  │           (100% of rated power goes through it)      │
  │           Decouples generator from grid frequency    │
  └──────────────────────────────────────────────────────┘

  PMSG PROS:  No gearbox failures; full variable speed; excellent low-wind perf
              Lower O&M cost offshore (no gearbox oil changes at sea)
              Better grid-forming capability (full power electronics control)
  PMSG CONS:  Larger/heavier nacelle; higher upfront cost; rare earth magnets (Nd)
              Full-scale converter = larger power electronics cost
  Users:      Goldwind (dominant China), Siemens Gamesa (SG DD), GE Cypress (semi-DD)
```

---

## Onshore vs Offshore

### Economics Comparison

| Parameter | Onshore | Offshore Fixed | Offshore Floating |
|-----------|---------|----------------|-------------------|
| Capacity factor | 25-40% | 40-55% | 45-60% (projected) |
| Water depth | Land | 0-60 m | 60-1000+ m |
| Foundation | Concrete pad | Monopile/jacket | Semi-sub, TLP, spar |
| Turbine size | 4-7 MW | 10-16 MW | 10-20 MW (planned) |
| LCOE (2024) | $25-50/MWh | $70-120/MWh | $100-180/MWh |
| O&M access | Easy (truck) | Helicopter/vessel | Remote vessel |
| Land use conflict | Setback rules | Visual/fishing conflict | Minimal (far offshore) |
| Grid connection | Overhead line | Submarine HVAC or HVDC | HVDC typically |

### Offshore Foundation Types

```
  WATER DEPTH → FOUNDATION TYPE:

  0-30 m: MONOPILE (dominant, ~80% of installed offshore)
  ┌─────────────────────┐
  │  Turbine on top     │
  │                     │
  │  Transition piece   │
  │  ──────────────────  │  ← waterline
  │                     │
  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │  steel monopile, ~8-12 m diameter
  │  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   │  driven into seabed
  └─────────────────────┘

  20-60 m: JACKET (lattice frame)
  ┌─────────────────────┐
  │  Turbine on top     │
  │  Transition piece   │
  │  ──────────────────  │  ← waterline
  │     /  │  \         │
  │    /   │   \         │  3 or 4-leg jacket
  │   /    │    \        │  heavier, more expensive than monopile
  │  /─────┼─────\       │  used for larger turbines and deeper water
  └─────────────────────┘

  >60 m: FLOATING (emerging, first commercial projects 2024+)
  Three main concepts:
    Semi-submersible:  Multiple pontoons, wide stable base, mooring lines
    TLP (tension leg):  Buoyant platform, taut vertical mooring lines
    Spar-buoy:          Deep cylindrical keel, stable but needs very deep water

  Floating target markets:
    Norwegian/Atlantic coast, US West Coast, Japan, Taiwan deep water
    First commercial: Hywind Tampen (Norway, 88 MW, 2022)
```

---

## Wake Effects and Farm Layout

### The Wake Problem

```
  WIND FARM WITH WAKE EFFECTS:

  Wind direction →
  ┌─────────────────────────────────────────────────────────────┐
  │  T1 ●         T2 ●         T3 ●         T4 ●                │
  │     │            │            │            │                │
  │     └──wake──────►            └──wake──────►                │
  │     (reduced      cumulative  wake deficit                  │
  │     wind speed    loss at T3 = ~25-30% power loss)         │
  │                                                             │
  │  T5 ●         T6 ●         T7 ●         T8 ●               │
  │                                                             │
  │  Cross-row spacing (perpendicular): 3-5D (D = rotor diameter)│
  │  Along-row spacing (parallel to wind): 7-10D               │
  └─────────────────────────────────────────────────────────────┘

  WAKE MODELS:
  Jensen (Top Hat):  Simple, fast, slightly pessimistic
                     Wake deficit decays as 1/distance
  Gaussian model:    Smooth velocity deficit profile, more accurate
  LES (Large-Eddy Simulation): Highest fidelity, expensive, used for research

  Farm-level losses:
    Densely packed (3D spacing): 20-30% wake loss on interior turbines
    Well-spaced (8D): 5-10% wake loss
    Optimal layout: balance land cost vs wake loss (not always max spacing)
```

### Wind Farm Control

Emerging field: deliberately curtail upwind turbines (reduce Cp via wake steering)
to increase total farm output. Upwind turbine redirects wake away from downwind machines.
Field trials show 3-8% farm-level AEP improvement. Being deployed commercially at scale.

---

## Variability and Forecasting

```
  WIND POWER VARIABILITY CHARACTERISTICS:

  Timescale      Cause                  Grid Response
  ─────────────  ─────────────────────  ──────────────────────
  Seconds        Turbulence             Automatic voltage regulation
  Minutes        Gusts, local weather   Primary frequency regulation
  Hours          Frontal systems        Day-ahead unit commitment
  Days           Synoptic patterns      Weekly generation scheduling
  Seasonal       Climatological cycle   Long-term adequacy planning
  Annual         El Niño/La Niña, etc.  Resource uncertainty in LCOE

  Forecast methods:
  NWP (numerical weather prediction):  ECMWF, GFS — basis for 1-10 day ahead
  Statistical/ML:  Correct NWP bias using historical data; LSTM, gradient boosting
  Ensemble:        Multiple model runs to quantify uncertainty
  Short-term (<1hr): nowcasting using radar, LiDAR, current turbine data

  Ramp events:
  Rapid large changes in wind output (e.g., 2 GW/hr in ERCOT)
  Grid operators need to pre-position reserves
  Forecasting large ramps remains difficult; tail events drive reserve requirements
```

---

## Market and Deployment Context

### Global Installed Capacity (End 2023)

| Region | Onshore (GW) | Offshore (GW) | Total |
|--------|-------------|---------------|-------|
| China | ~400 | ~30 | ~430 |
| USA | ~145 | ~0.3 | ~145 |
| Germany | ~61 | ~8.5 | ~70 |
| India | ~44 | ~0 | ~44 |
| UK | ~15 | ~14 | ~29 |
| Spain | ~30 | ~0 | ~30 |
| Rest of EU | ~100 | ~15 | ~115 |
| **Global Total** | **~950** | **~75** | **~1,025** |

IEA NZE 2030 target: ~2,400 GW onshore + offshore additions per year globally.
2023 additions: ~117 GW. Gap = 20× increase required. The bottleneck is permitting,
grid, and supply chain — not cost.

### Supply Chain and Critical Materials

```
  TURBINE SUPPLY CHAIN CONSTRAINTS:

  Rare earth magnets (neodymium/dysprosium):
    • Required for PMSG direct-drive generators
    • ~200-300 kg of rare earth magnets per MW (approx)
    • China controls ~85% of rare earth processing
    • DFIG (gearbox turbines) avoid rare earths but have O&M penalty

  Steel:
    • Towers: ~200-500 tonnes per turbine (structural steel)
    • Cost-sensitive to steel prices

  Blade manufacturing:
    • Fiberglass/epoxy: concentrated in a few global manufacturers
    • Blade transport (80m+) requires specialized logistics
    • End-of-life blade recycling unsolved (cement kiln, pyrolysis pilots)

  Offshore-specific:
    • Specialized installation vessels (jack-up, heavy lift crane)
    • Few in existence globally; lead time 3-5 years to build new
    • WTIV (wind turbine installation vessel) bottleneck for US offshore
```

---

## Repowering

Aging turbines (2000-era, 0.75-2 MW, 20-year lifespan) can be repowered with modern turbines
on existing permitted sites. Economics:
- Existing permits, grid connections, and land leases
- New turbines 3-5× larger than what they replace
- AEP increase of 100-200% on same land area
- Typically requires environmental review but not full new permit
- Germany has ~30 GW eligible for repowering; regulatory bottleneck slowing this

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Maximum theoretical wind energy extraction? | 59.3% (Betz limit) — physics, not engineering |
| Why does power scale with v³? | KE = ½mv²; mass flow = ρAv → P = ½ρAv³Cp |
| Best CF for onshore wind? | 35-40% in good sites (Great Plains, central Europe) |
| Best CF for offshore? | 40-55% fixed; 45-60% floating (projected) |
| Gearbox vs direct-drive for offshore? | Direct-drive wins (no gearbox failures at sea) |
| DFIG vs PMSG? | DFIG: cheaper partial converter; PMSG: better variable speed, no rare earth issue (wound-field variants) |
| Why spacing matters? | Wake losses: 7-10D along-wind spacing; 3-5D cross-wind |
| Largest turbines (2024)? | 14-16 MW offshore (Vestas V236, SGRE SG 14-222 DD) |
| Onshore LCOE? | $25-50/MWh — cheapest new electricity in most markets |
| Offshore fixed LCOE? | $70-120/MWh (falling, target <$60 by 2030 in North Sea) |
| Main bottleneck for US offshore? | Permitting, WTIV vessel shortage, supply chain, cable |

---

## Common Confusion Points

**"Rated power vs actual output"**
A 5 MW turbine only produces 5 MW at its rated wind speed (~12 m/s).
At 8 m/s (more typical average), it produces ~1.4 MW (Cp × ½ρAv³).
CF of 35% means it produces 35% of 5 MW × 8,760 hrs/yr = 15,330 MWh/yr.

**"Offshore is better, so build all offshore"**
Offshore CF is higher, but LCOE is 2-3× onshore. In regions with good onshore wind
(US Great Plains, northern Europe plains), onshore is far cheaper per MWh.
Offshore makes economic sense when: (a) land is unavailable/opposed, (b) onshore
resource is poor (UK, New England), (c) load centers are coastal.

**"Wind doesn't work when it's calm"**
True for a single turbine. False at grid scale. Correlation of wind across distant locations
drops sharply beyond ~500 km. A European interconnected grid with wide geographic spread
has much less total variability than any single site. Averaging across regions is a key
design tool for high-penetration wind grids.

**"Direct-drive is always better"**
Direct-drive PMSG avoids gearbox failures and has better variable-speed control.
But gearbox turbines with DFIG are cheaper and still dominant onshore (easier O&M access).
The rare earth dependency of PMSG is a supply chain risk some developers hedge by
choosing gearbox turbines or wound-field synchronous generators (no permanent magnets).

**"Betz limit means 59.3% is achievable"**
Betz is the actuator disk limit — a 1D flow model. Real rotors have finite blade count,
tip vortices, drag, and rotational KE in the wake. Best commercial turbines achieve
~80-85% of Betz = ~48-50% of wind KE. Not 59%.
