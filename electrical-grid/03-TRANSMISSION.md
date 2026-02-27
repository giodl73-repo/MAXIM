# Electrical Grid — Transmission Systems
## Moving Gigawatts Across Hundreds of Miles

---

## The Big Picture: Why Transmission Exists

```
GENERATION SITES                              LOAD CENTERS
(Where power is cheap to make)               (Where power is needed)

  Coal/nuclear: remote riverside locations       Cities: dense, expensive land
  Wind:  Texas Panhandle, Great Plains           Industrial: need reliable supply
  Solar: Arizona/Nevada desert                   New England: imported energy
  Hydro: Columbia River gorge, Hoover Dam        Southeast: need Florida/SE coal

  Distance: 50 to 1,000+ miles between source and sink

WITHOUT HIGH-VOLTAGE TRANSMISSION:
  Transmit at 13.8 kV (generator terminal voltage)
  1,000 MW over 100 miles of copper → I = P/V = 1,000,000,000 / 13,800 ≈ 72,000 A
  Typical ACSR conductor resistance: 0.1 Ω/mile
  Loss per 100 miles = I²R = (72,000)² × 0.1 × 100 = 5.2 × 10¹⁰ watts — impossible

WITH 500 kV TRANSMISSION:
  I = 1,000,000,000 / 500,000 = 2,000 A (36× less current)
  Loss = (2,000)² × 0.1 × 100 = 40,000,000 W = 40 MW = 4% loss
  This is manageable. Step-up to 500 kV is why long-distance transmission works.
```

---

## Why High Voltage: The I²R Mathematics

The governing equation: **P_loss = I² × R**

For a transmission line of resistance R, carrying current I:
- All the power is in P = I × V
- All the heat loss is in P_loss = I² × R
- Doubling voltage → half the current for same power → quarter the losses

```
TRANSMISSION EFFICIENCY vs VOLTAGE (1000 MW, 200 mile line, ACSR 795 MCM):
R per circuit = 200 miles × 0.048 Ω/mile = 9.6 Ω (typical ACSR 795 MCM)

Voltage | Current (A) | I²R Loss (MW) | Loss %
--------|-------------|---------------|--------
 69 kV  |   14,500    |   2,026 MW    |  203%  (impossible — more loss than power)
138 kV  |    7,250    |     506 MW    |   51%  (still unworkable)
230 kV  |    4,350    |     182 MW    |   18%  (marginal)
345 kV  |    2,899    |      81 MW    |    8%  (acceptable for medium distance)
500 kV  |    2,000    |      38 MW    |    4%  (standard long-distance)
765 kV  |    1,307    |      16 MW    |  1.6%  (EHV, used in US for longest lines)

Note: These are single-conductor calculations. Real lines use bundled conductors
and multiple circuits — see below. Numbers illustrate the principle.
```

---

## Transmission Line Conductors

### ACSR: Aluminum Conductor Steel Reinforced

The dominant overhead transmission conductor since the 1950s.

```
ACSR CROSS-SECTION:

        Stranded aluminum wires
        (carry current, ρ = 2.65 μΩ·cm)
     ╱╲
    ╱  ╲    ← Aluminum outer wires (multiple layers)
   │Steel│   ← Steel core wires (structural strength)
    ╲  ╱     ρ_steel = 10.0 μΩ·cm (steel carries little current due to
     ╲╱       higher resistivity — mostly structural)

PROPERTIES:
  Aluminum: ρ = 2.65 μΩ·cm (vs copper 1.72 μΩ·cm — 54% more resistive)
  But aluminum density = 2.70 g/cm³ vs copper 8.96 g/cm³
  → For same conductance: aluminum wire is 54% heavier than copper would be
    in resistance, but aluminum weighs 50% of copper for same resistance
  → Tower loading allows much larger aluminum conductors vs copper
  → Economic winner for overhead at scale

Common ACSR conductors:
  Drake (795 MCM): 0.0523 Ω/km, 1,600 A ampacity (typical 345/500 kV)
  Lapwing (1590 MCM): 0.0283 Ω/km, 2,200 A (large conductors)
  Cardinal (954 MCM): 0.0443 Ω/km, 1,800 A
  MCM = Thousand Circular Mils = cross-sectional area unit
```

### Bundled Conductors

At 230 kV and above, multiple conductors per phase are bundled together:

```
SINGLE CONDUCTOR (230 kV and below):  Phase A: ●

BUNDLED CONDUCTORS (345 kV+):
  2-conductor bundle (345 kV):     Phase A: ● ●  (30-46 cm spacing)
  3-conductor bundle (500 kV):     Phase A: ● ● ●  (triangular arrangement)
  4-conductor bundle (765 kV+):    Phase A: ● ● ● ●  (square arrangement)

WHY BUNDLE?
1. Corona discharge control: Electric field at conductor surface ∝ V/r
   At 500 kV, single conductor surface field exceeds ~30 kV/cm → air ionization → corona
   (audible hum, ozone, radio interference, real power loss)
   Bundled conductors: equivalent larger radius → lower surface field → less corona
2. Lower impedance: Multiple parallel conductors reduce resistance + inductance
3. Higher current capacity: More conductor material
```

---

## Transformers: The Essential Component

Transformers are why AC transmission is economical. They step voltage up (generation → HV) and down (HV → distribution → service).

### Operating Principle

Faraday's law: V = N × dΦ/dt (voltage = turns × rate of flux change)
For sinusoidal AC: V₁/V₂ = N₁/N₂ (turns ratio determines voltage ratio)
Power conservation: V₁I₁ ≈ V₂I₂ (ignoring losses) → current transforms inversely to voltage

```
TRANSFORMER INTERNALS:

           Primary winding               Secondary winding
           (N₁ turns)                   (N₂ turns)
           ┌──────────┐                 ┌──────────┐
V₁ ───────▶│ xxxxxxxx │──── Core ───────│ xxxxxxxx │──────── V₂
           │          │   (silicon      │          │
I₁ ←───────│ xxxxxxxx │    steel        │ xxxxxxxx │──────── I₂
           └──────────┘    laminations) └──────────┘

V₁/V₂ = N₁/N₂
I₂/I₁ = N₁/N₂ (current transforms inversely)
Impedance transforms as (N₁/N₂)²

CORE DESIGN: Silicon steel laminations (0.3–0.5 mm thick, insulated from each other)
  Purpose: laminations break eddy current paths → reduce eddy current losses
  Hysteresis loss: core magnetization/demagnetization each cycle → heat
  Core losses: typically 0.1–0.5% of rated capacity (constant, 24/7)
  Copper losses: I²R in windings (proportional to load²)

INSULATION: Paper impregnated with mineral oil
  Oil serves: insulation + cooling (convection)
  Temperature limits: 105°C top oil, 65°C winding hotspot rise above 40°C ambient
  Transformer life: 40-65 years (if operated within limits)
  Oil-cooled: ONAN (self-cooled), ONAF (forced air), OFAF (forced oil + air)
```

### Transformer Losses and Efficiency

```
TOTAL TRANSFORMER LOSSES = Core losses + Copper losses

Core losses (no-load, constant):
  Hysteresis: ∝ f × B^n × volume (B = flux density, n ≈ 1.6-2.0 for silicon steel)
  Eddy current: ∝ f² × B² × t² (t = lamination thickness)
  Typical: 0.05–0.15% of rated capacity

Copper losses (load-dependent):
  Primary: I₁² × R₁
  Secondary: I₂² × R₂
  Typical full-load: 0.3–0.5% of rated capacity

Combined losses:
  Small distribution transformer: 98.0–98.5% efficiency
  Large power transformer (100+ MVA): 99.3–99.7% efficiency
  Generator step-up (500+ MVA): 99.5–99.8% efficiency

These seem small but matter at scale:
  A 500 MW step-up transformer at 0.3% loss = 1.5 MW continuous heat dissipation
  That's 13.1 GWh/yr — $1M+ in energy cost at wholesale prices
```

### Transformer Types in the Grid

| Type | Location | Example Rating | Notes |
|------|----------|---------------|-------|
| Generator Step-Up (GSU) | Power plant | 500 MVA, 13.8/500 kV | Steps generator voltage to HV |
| Bulk Power Transformer | Transmission substation | 300 MVA, 500/230 kV | Autotransformer or two-winding |
| Transmission Substation | EHV/HV boundary | 500 MVA, 230/69 kV | Often autotransformer |
| Distribution Transformer | Distribution substation | 25–150 MVA, 115/12.47 kV | Steps to primary distribution |
| Pad-Mount | Residential/commercial | 25–500 kVA, 12.47kV/480V | Ground-level, padlocked box |
| Pole-Mount | Rural residential | 5–100 kVA, 7,200V/120-240V | Single-phase, US common |

---

## Reactive Power and Power Factor

This is the concept that most confuses people outside the power industry, but it's fundamental to grid operation.

### Real Power vs Reactive Power vs Apparent Power

```
POWER TRIANGLE:

         ╱| S (Apparent Power, MVA) = V × I
        ╱ |
   Q   ╱  | Q (Reactive Power, MVAR) = V × I × sin(φ)
(MVAR) ╱   |   — stores/releases energy in inductors/capacitors
      ╱ φ  |   — does NO net work
     ╱─────┘
         P (Real Power, MW) = V × I × cos(φ)
           — does actual work (heats homes, runs motors)

Power Factor = P/S = cos(φ) (1.0 is ideal, 0.0 is pure reactive)

PHYSICAL INTERPRETATION:
  An inductive load (motor, transformer, induction generator) draws lagging current
  (current lags voltage by angle φ) → consumes reactive power
  A capacitive load (capacitor bank, overexcited generator, lightly loaded cable)
  supplies reactive power → current leads voltage
  Power lines themselves are both: inductive in series (self-inductance),
  capacitive in shunt (line-to-ground capacitance)
```

### Why Reactive Power Management Is Critical

```
REACTIVE POWER PROBLEM:

  Inductive loads consume Q locally. Q cannot be efficiently transmitted long distances
  because: delivering Q over a line = more current I → more I²R loss → voltage drops
  Q must be generated near where it's consumed.

  Long transmission line characteristic:
  Loaded line (heavy load): line inductance dominates → line CONSUMES reactive power
                            → voltage drops toward load end
  Lightly loaded line: line capacitance dominates → line GENERATES reactive power
                        → voltage RISES toward load end (Ferranti effect)
                        → problem for long lines during low-load periods

SOLUTION TOOLS:
  Shunt capacitor banks:   Generate Q locally at distribution level (+MVARs)
  Shunt reactors:          Absorb excess Q on long lightly-loaded lines (-MVARs)
  Synchronous generators:  Best VAR source — continuously variable, fast control
                           Overexcited = capacitor (supplies Q), underexcited = inductor (absorbs Q)
  STATCOM:                 Fast electronic VAR injection/absorption (see FACTS)
  SVC:                     Thyristor-controlled reactor/capacitor banks
```

### FACTS Devices (Flexible AC Transmission Systems)

Power flow in AC networks follows Kirchhoff's laws — it goes where impedance directs it, not where the operator wants it. FACTS devices modify effective impedance to control power flow:

| Device | Function | Technology |
|--------|---------|-----------|
| **SVC** (Static VAR Compensator) | Fast reactive power injection/absorption | Thyristor-controlled reactor + fixed capacitor banks |
| **STATCOM** (Static Synchronous Compensator) | Faster VAR control, can work at low voltage | IGBT-based voltage source converter |
| **TCSC** (Thyristor-Controlled Series Capacitor) | Series capacitor for line loading control | Series capacitor with bypass thyristors |
| **SSSC** | Series reactive power injection | IGBT voltage source converter |
| **UPFC** (Unified Power Flow Controller) | Full control: P, Q, voltage, angle | Combination series + shunt converters; most capable, most expensive |

---

## HVDC: High Voltage Direct Current

### When AC Loses to DC

```
COMPARISON FOR LONG-DISTANCE/SUBMARINE TRANSMISSION:

AC long line:                           DC long line:
  Phase-to-phase voltage nominal          No reactive power
  Reactive charging current grows         No skin effect (DC distributes evenly)
  with line length (line capacitance)     No ac synchronization requirement
  AC cable: ~50-100 km practical limit    DC cable: thousands of km viable
  Reactive compensation every 100 km     Converter stations at each end
  Synchronization required between ends  Asynchronous interconnection possible

COST CROSSOVER (rule of thumb):
  Overhead: HVDC cheaper than HVAC at distances > ~800 km
  Underground/submarine: HVDC cheaper at essentially all distances > ~50 km

HVDC ECONOMICS:
  Overhead HVDC: ~$1.5-3M per MW (per 1000 km) vs HVAC ~$1M per MW (shorter)
  But: HVDC losses ~0.3-0.7% per 100 km vs HVAC 1-3% (including reactive)
  For 2,000 MW × 3,000 km: HVDC total cost ~$4-6B, HVAC ~$6-10B+
```

### LCC-HVDC vs VSC-HVDC

Two converter technologies with fundamentally different capabilities:

```
LCC-HVDC (Line-Commutated Converter):
  Technology: Thyristors (silicon-controlled rectifiers, SCR)
  Commutation: Uses AC grid voltage at the converter bus to commutate (switch) thyristors
               → REQUIRES existing AC voltage to operate (cannot feed a passive load)
  Reactive power: Consumes 50-60% of active power as reactive power (must compensate)
  Power flow: Bipolar (±500 kV common)
  Four-quadrant: NO — current direction fixed, voltage reversal for power reversal
  Fault ride-through: Poor at AC faults (commutation failure)
  Black start: NO — needs AC voltage to commutate
  Efficiency: ~99.4% per converter station (very low losses)
  Cost: Lower than VSC for very high power
  Projects: Pacific DC Intertie (±500 kV, 3,100 MW), China UHV DC (±1,100 kV, 12,000 MW)

VSC-HVDC (Voltage-Source Converter):
  Technology: IGBTs (Insulated Gate Bipolar Transistors) in MMC configuration
               (Modular Multi-level Converter — many series-connected sub-modules)
  Commutation: Self-commutated — switches at any time, independent of AC grid
               → CAN feed a passive network (black start capability)
  Reactive power: Can generate or absorb Q independently of active power (4-quadrant)
  Power flow: Monopolar, bipolar, or symmetrical monopole
  Four-quadrant: YES — full independent P and Q control
  Fault ride-through: Excellent
  Black start: YES — can re-energize dead AC system
  Efficiency: ~98.5-99.0% per converter station (slightly lower than LCC)
  Cost: Higher capex than LCC, but dropping rapidly
  Projects: BritNed (900 MW), Caithness-Moray (UK offshore wind), NordLink (Germany-Norway)
```

### MMC (Modular Multi-Level Converter) — Modern VSC

```
MMC ARCHITECTURE (one phase, one arm):

  DC Bus +
     │
  ┌──┴──┐  Sub-module 1: half-bridge (IGBT + diode + capacitor)
  │ SM1 │  Each SM: ~1-2 kV DC voltage step
  ├──┴──┤
  │ SM2 │  Hundreds of SMs in series → smooth staircase waveform
  ├──┴──┤  approximating AC sinusoid
  │ SM3 │  → Very low harmonics without heavy filtering
  ├──┴──┤
  │ ... │  (30-400 SMs per arm depending on voltage level)
  └──┬──┘
     │
  AC output (to transformer/grid)
     │
  ┌──┴──┐  Lower arm SMs
  │ SM  │
  ├──┴──┤
  │ SM  │
  └──┬──┘
     │
  DC Bus -

  Key MMC advantage: synthesizes very high quality AC waveform from DC
                     without need for large filters
                     Each SM capacitor also acts as local energy storage
                     (helps with fault current and inertia emulation)
```

**Major HVDC projects worldwide:**
- Pacific DC Intertie: ±500 kV, 3,100 MW, 1,362 km (Oregon → California), operational 1970
- Three Gorges → Shanghai: ±500 kV, 3,000 MW, 1,060 km (China)
- Changji → Guquan: ±1,100 kV, 12,000 MW, 3,293 km (China — world's most powerful)
- NordLink: ±525 kV, 1,400 MW, 623 km (Norway → Germany, VSC, 2021)
- BritNed: ±450 kV, 1,000 MW, 260 km (Netherlands → UK, VSC, 2011)

---

## Corona Discharge and Line Ratings

### Corona Discharge

At high electric field gradients, air molecules ionize, creating a visible glow (corona) and audible buzz. This is the hissing/buzzing you hear near high-voltage lines in humid weather.

```
CORONA THRESHOLD:
  Air breakdown field: ~30 kV/cm (30,000 V per centimeter)
  Electric field at conductor surface: E = V / (r × ln(D/r))
  Where: r = conductor radius, D = distance between conductors

  For 500 kV line, single conductor (r = 1.5 cm):
  E_surface ≈ 20-25 kV/cm → approaching breakdown → corona!

  Solution: bundled conductors
  3-conductor bundle with s = 45 cm spacing:
  Equivalent radius r_eq = r × (s²)^(1/3) ≈ 12 cm (effective)
  E_surface drops to ~8-10 kV/cm → below corona threshold

CORONA EFFECTS:
  Power loss: 0.5-5 kW/km in wet weather, less in dry
  Audible noise: 40-55 dB at 15m (annoying to nearby residents)
  Radio/TV interference: electromagnetic noise
  Ozone production: O₃ — chemical oxidizer, damages materials
  UV light: visible as bluish glow in darkness
```

### Thermal Line Ratings

Transmission lines are rated by their ampacity — maximum current they can carry without exceeding conductor temperature limits.

```
CONDUCTOR TEMPERATURE LIMITS:
  ACSR standard maximum: 75-90°C continuous (older NERC standard)
  HTLS (High-Temperature Low-Sag): 150-250°C (newer conductors)
  Aluminum annealing begins: >90°C (permanent strength loss)
  Clearance concern: conductor sags under heat (thermal expansion)
  Ground clearance requirements (NERC FAC-001): >8m at 115 kV, varies by voltage

STATIC vs DYNAMIC LINE RATINGS (DLR):
  Static: Fixed ampacity based on worst-case summer conditions
          (e.g., 35°C ambient, no wind, full sun)
  Dynamic: Real-time ampacity based on actual conditions
           (cool/windy day: same conductor may carry 40-60% MORE current)
           Technology: sensors on conductors measure actual sag/temperature
           + weather data + thermal models

DLR economic value:
  A 500 MW rated line might carry 700 MW on a cold, windy winter night
  This matters when a wind farm is trying to export maximum power — exactly
  when conditions (cold, windy) allow higher line ratings
  DLR systems cost $200-500k per line section; payback < 3 years in constrained areas
```

### Right-of-Way (ROW)

Transmission lines require permanent easements across property — the right to have towers and wires overhead.

```
ROW WIDTHS (typical):
  115 kV single circuit:     75-100 ft (23-30m)
  230 kV double circuit:    150-200 ft (46-61m)
  345 kV double circuit:    200-250 ft (61-76m)
  500 kV double circuit:    250-350 ft (76-107m)
  765 kV single circuit:    200-300 ft (61-91m)

ROW REQUIREMENTS:
  Vegetation management: mandatory under NERC FAC-003
    (failure → contributing factor in 2003 Northeast Blackout)
  No permanent structures (buildings, but agriculture OK)
  Height restrictions near airports
  Access roads for maintenance

PERMITTING/SITING:
  Federal: FERC (if across state lines), NEPA environmental review
  State: Public Utility Commission approval required
  Local: county/municipal zoning (some veto power)
  Typical timeline: 7-15 years from proposal to energization
  This is why transmission buildout is the bottleneck for renewable integration
```

---

## Substation Architecture

Substations are where transformers, circuit breakers, and protective equipment connect the transmission system.

```
BULK TRANSMISSION SUBSTATION (simplified):

    From 500 kV line ─────────────────────────────────── To 500 kV line
                      │                           │
                    ┌─┴─┐                       ┌─┴─┐
                    │CB │ 500 kV circuit         │CB │  (SF₆ gas insulated)
                    └─┬─┘ breaker               └─┬─┘
                      │                           │
               500 kV Bus ─────────────────────────
                      │
                    ┌─┴──────┐
                    │500/230 │ Autotransformer
                    │  kV    │ (e.g., 500 MVA)
                    │AutoTX  │
                    └─┬──────┘
                      │
               230 kV Bus ─────────────────────────
                      │                           │
                    ┌─┴─┐                       ┌─┴─┐
                    │CB │                       │CB │
                    └─┬─┘                       └─┬─┘
                      │                           │
               To 230 kV line               To distribution substation

KEY EQUIPMENT:
  SF₆ Circuit Breakers: Sulfur hexafluoride gas as arc-quenching medium
    Contact opens during fault → arc forms → SF₆ quenches arc in < 3 cycles (50 ms)
    Also used as insulation (5× better than air) → compact substation
  Disconnect switches: Manually operated, de-energize equipment for maintenance
  Current Transformers (CT): Step down current for metering and protection
    (5,000A line current → 5A for relays)
  Potential Transformers (PT): Step down voltage for metering
    (500 kV → 115V for relays)
  Surge Arresters (MOV): Metal oxide varistor; clamp lightning transients
  Lightning mast: Ground rods and overhead shielding wires
```

---

## Power Flow and Kirchhoff in Meshed Networks

AC Optimal Power Flow (OPF) is the mathematical heart of grid operations — a constrained optimization problem: minimize total generation cost sum(C_i(P_i)) subject to power balance at every bus (equality constraints from KCL/KVL), thermal line limits (inequality constraints), and voltage magnitude bounds. The DC power flow approximation (drop reactive power, linearize around flat voltage) reduces this to a linear program — solvable in seconds for thousands of buses. Full AC OPF is nonlinear and non-convex, but convex relaxations (SDP, SOCP) provide tractable approximations. Every EMS economic dispatch run solves this: "find the cheapest feasible operating point." The dual variables (shadow prices) on the power balance constraints are the locational marginal prices (LMPs) that set wholesale electricity prices in real time.

This is the key concept that makes AC power systems hard to control: power doesn't flow where you want it. It flows where impedance (mostly inductance at transmission frequency) directs it.

```
MESHED NETWORK EXAMPLE:

  Bus A ────── Line 1 (Z=j1Ω) ────── Bus B
    │                                   │
    │ Line 3 (Z=j2Ω)          Line 4 (Z=j1Ω)
    │                                   │
  Bus C ────── Line 2 (Z=j1Ω) ────── Bus D

  Generator at A: inject 300 MW
  Load at D: consume 300 MW

  Power flow distribution (simplified):
  Line 1 (A→B): carries ~150 MW (lower impedance path)
  Line 2 (A→C via Line 3, then to D via Line 4) splits remaining
  NO OPERATOR ACTION controls this — it's Kirchhoff's current law

  Problem: if Line 1 has a thermal limit of 100 MW, operator cannot
  "redirect" power around it (without FACTS or HVDC)
  Must either:
    - Redispatch generation (use different generators)
    - Build transmission
    - Install FACTS device
    - Accept congestion (cost uplift)
```

**Congestion management:** When power flow wants to exceed a line's thermal limit, the ISO/RTO "re-dispatches" — replaces cheap generation on the congested side with more expensive local generation. The price difference between buses reflects congestion cost. This is the congestion component of LMP pricing (see 08-MARKETS.md).

---

## Decision Cheat Sheet

| Question | Short Answer |
|----------|-------------|
| Why use high voltage for transmission? | I²R losses; 500 kV vs 13.8 kV = I is 36× lower → losses 1,296× lower for same power |
| Why ACSR and not copper? | Aluminum weighs ~30% of copper for same conductance; tower loading makes this viable |
| What limits line current? | Thermal rating (conductor temperature) → sag → clearance violation |
| Why bundle conductors? | Reduce surface electric field below corona threshold; also reduces impedance |
| When does HVDC beat HVAC overhead? | Distance > ~800 km (losses), or asynchronous interconnect required |
| When does HVDC beat HVAC for cables? | Essentially always at > ~50 km (capacitive charging current limits AC cable) |
| LCC vs VSC HVDC? | LCC: cheaper, needs AC voltage to operate, can't black start; VSC: full 4-quadrant, can black start, self-commutated |
| What is reactive power? | Q = V×I×sin(φ); stored/released by inductors/capacitors; does no net work but causes real current and voltage drops; must be managed locally |
| What is the Ferranti effect? | Long lightly-loaded line generates capacitive Q → voltage rises toward receiving end → must install shunt reactors |
| Why can't power flow be directed easily in AC networks? | It follows path of least impedance (Kirchhoff) — FACTS or HVDC needed for control |

---

## Common Confusion Points

**"HVDC has no losses":** False. HVDC converter stations have losses (~0.5-1% per station, so ~1-2% round-trip). The advantage is that DC line losses are lower per kilometer than AC, and there's no reactive power issue. For long enough distances, total HVDC losses beat HVAC total losses including reactive compensation.

**Transformer turns ratio and impedance:** The voltage transforms as N₁/N₂. Current transforms inversely as N₂/N₁. Impedance transforms as (N₁/N₂)². This last one is critical for fault current calculations — the impedance of a generator looks very different from the high-voltage side of the transformer than it does from the generator terminal.

**Autotransformer vs two-winding transformer:** An autotransformer has a single winding with a tap — the primary and secondary share part of the winding. More economical for voltage ratios close to 1:1 (like 500/345 kV = 1.45:1). Disadvantage: no electrical isolation between primary and secondary (matters for some protection schemes).

**Reactive power "flows":** Engineers talk about reactive power flowing, but it's a convenient fiction. What actually flows is current. The power factor of that current determines how much real work is done vs how much just sloshes back and forth in the inductors/capacitors. The "flow" of reactive power is a useful circuit analysis tool but isn't a separate physical flow.

**Dynamic line rating vs seasonal ratings:** Many utilities use seasonal ratings (summer, winter, spring/fall). DLR takes this further to real-time conditions. Neither changes the conductor's physical limits — they change the model's estimate of how close the conductor is to those limits given current conditions.

---

*Next: 04-DISTRIBUTION.md — substation topology, feeder design, reliability metrics*
*See also: 05-GRID-STABILITY.md for FACTS devices in stability context*
*See also: 08-MARKETS.md for LMP congestion pricing*
