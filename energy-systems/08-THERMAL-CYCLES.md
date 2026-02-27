# Thermal Power Cycles — Where the Alchemist Pays the Carnot Tax

*Every thermal power plant is a heat engine. Every heat engine is a machine for partially
converting thermal energy into work while surrendering the rest to the environment as waste
heat. The second law sets the ceiling. The engineering sets the floor. The gap between them
is where the Alchemist earns a living.*

---

## The Big Picture — Cycle Landscape

```
THERMAL POWER CYCLE FAMILY TREE
                                                         η_actual
HEAT ENGINE CYCLES                                       (typical)
═══════════════════════════════════════════════════════════════════

  CARNOT CYCLE (theoretical ceiling)                     ← unachievable
  │
  ├── RANKINE FAMILY (external combustion → working fluid phase change)
  │   │
  │   ├── Subcritical Rankine                             33-38%
  │   │   Coal, biomass, nuclear PWR/BWR
  │   │   Steam at 540°C / 165 bar
  │   │
  │   ├── Supercritical Rankine                           40-45%
  │   │   Advanced coal, Gen III+ nuclear
  │   │   Steam at 600°C / 250+ bar (above critical point)
  │   │
  │   ├── Ultra-Supercritical Rankine                     45-47%
  │   │   Cutting-edge coal (700°C+ / 300+ bar)
  │   │   Materials limit: nickel superalloys
  │   │
  │   └── Organic Rankine Cycle (ORC)                     10-20%
  │       Low-grade waste heat, geothermal (80-350°C)
  │       Working fluid: pentane, R245fa, siloxanes
  │
  ├── BRAYTON FAMILY (internal combustion → gas-phase working fluid)
  │   │
  │   ├── Open-Cycle Gas Turbine (OCGT)                   35-42%
  │   │   Peaker plants, aero-derivative turbines
  │   │   Exhaust at ~500-600°C → wasted to atmosphere
  │   │
  │   ├── Closed-Cycle Brayton                            25-40%
  │   │   Helium cycle (nuclear HTGR)
  │   │   External heat source, inert working fluid
  │   │
  │   └── Supercritical CO₂ Brayton (sCO₂)               45-55%
  │       Next-generation: compact, high efficiency
  │       Near-critical-point CO₂ — extreme density
  │       Nuclear Gen IV, CSP, waste heat
  │
  ├── COMBINED CYCLE (Brayton topping + Rankine bottoming)
  │   │
  │   └── CCGT (Combined Cycle Gas Turbine)                58-64%
  │       Gas turbine exhaust → HRSG → steam turbine
  │       Highest thermal efficiency of any deployed cycle
  │
  └── EXOTIC / EMERGING
      ├── Kalina Cycle (ammonia-water binary mixture)       12-18%
      │   Low-grade heat, geothermal
      ├── Stirling Cycle (external combustion, closed)      25-35%
      │   Solar dish, micro-CHP, submarine AIP
      └── Allam-Fetvedt Cycle (sCO₂ oxy-combustion)        51-54%
          Inherent CO₂ capture, near-zero emissions

═══════════════════════════════════════════════════════════════════
```

**The Alchemist's question for every cycle:** Where does the exergy die? In the combustion
irreversibility? In finite-temperature heat transfer? In expansion losses? In the condenser?
Each cycle makes different choices about where to accept irreversibility and where to fight it.

---

## Thermodynamic Foundations — The Four Processes

Every power cycle is built from combinations of four idealized processes. You know these
from thermodynamics coursework at MIT; what matters here is how real cycles deviate from
the idealized versions and why.

```
THE FOUR BUILDING BLOCKS:

  Process           Ideal (reversible)         Real (irreversible)
  ────────────────  ──────────────────────     ──────────────────────────
  Compression       Isentropic (s = const)     Polytropic; friction, heat
                    w_in = h₂s - h₁            leak → η_c = 0.85-0.92
                                                (isentropic efficiency)

  Heat addition     Isobaric (p = const)       Finite ΔT across heat
                    or isothermal               exchanger → entropy
                                                generation → exergy loss

  Expansion         Isentropic (s = const)     Blade friction, tip leakage,
                    w_out = h₃ - h₄s           moisture erosion (LP stages)
                                                η_t = 0.88-0.95

  Heat rejection    Isobaric / isothermal      Condenser approach ΔT
                    (condenser)                 (pinch = 3-10°C above
                                                ambient) → sets actual T_cold

  ───────────────────────────────────────────────────────────────────────
  BRIDGE: Irreversible losses in a power cycle are analogous to overhead
  in a software pipeline. Each stage has parasitic costs (serialization
  overhead, context switches, GC pauses). The "ideal throughput" assumes
  zero overhead; the actual throughput is the ideal minus the sum of all
  stage losses. Optimization targets the biggest loss first.
```

### The Carnot Cycle — The Ceiling Nobody Reaches

```
CARNOT CYCLE ON T-s DIAGRAM:

  T (Temperature)
  │
  │    T_H ─────────── ① ─────────────── ②
  │                    │                  │
  │                    │   Q_in           │
  │                    │   (isothermal    │
  │                    │    heat add)     │
  │                    │                  │
  │    T_C ─────────── ④ ─────────────── ③
  │                    │                  │
  │                    │   Q_out          │
  │                    │   (isothermal    │
  │                    │    heat reject)  │
  │
  └────────────────────────────────────────── s (entropy)

  η_Carnot = 1 - T_C / T_H    (temperatures in Kelvin)

  WHY CARNOT IS UNREACHABLE:
  1. Isothermal heat addition at T_H requires infinite heat exchanger area
     (ΔT → 0 means infinite area per Fourier's law: Q = UAΔTlm)
  2. Isothermal compression of a two-phase fluid is impractical
  3. Reversible processes require infinite time (zero entropy production)
  4. Real working fluids have phase boundaries, critical points, material limits

  WHAT CARNOT TELLS US:
  → The only way to raise efficiency: increase T_H or decrease T_C
  → T_C is bounded by ambient (~288-310 K) — limited room
  → T_H is bounded by materials: 870 K (steam), 1600 K (gas turbine),
    1900 K (theoretical ceramic limit)
  → CCGT achieves 58-64% because it uses gas at 1600 K AND steam at 870 K
```

---

## The Rankine Cycle — Workhorse of Thermal Power

The Rankine cycle is the dominant cycle for coal, nuclear, biomass, geothermal, and
concentrated solar power. It uses water/steam as the working fluid, exploiting the
phase change from liquid to vapor to absorb large amounts of heat at constant temperature.

### Ideal Rankine Cycle

```
IDEAL RANKINE CYCLE — T-s DIAGRAM:

  T (K)
  │
  │         Critical point (647 K, 221 bar for H₂O)
  │              ╱╲
  │            ╱    ╲           Saturation dome
  │          ╱        ╲
  │        ╱     ③──────╲──── ③  Superheated steam (T_max)
  │       ╱     ╱        ╲   │
  │      │     ╱          ╲  │  TURBINE: ③→④
  │      │    ② Boiling    ╲ │  (isentropic expansion)
  │      │   ╱   at const   ╲│
  │      │  ╱     pressure    ④  Wet steam exits turbine
  │      │ ╱                  │
  T_cond ─①──────────────────╱── ④ condenser (isobaric heat rejection)
  │      ↑                     │
  │    PUMP                    │
  │    ①→② (isentropic         │
  │    compression of liquid)  │
  │
  └─────────────────────────────────── s (entropy)

  THE FOUR STEPS:
  ① → ②  PUMP:       Compress liquid water (very little work — liquid is
                      nearly incompressible). w_pump = v(P₂ - P₁)

  ② → ③  BOILER:     Heat water → steam at constant pressure.
                      Preheating + evaporation + superheating.
                      Q_in = h₃ - h₂

  ③ → ④  TURBINE:    Expand steam through turbine → shaft work.
                      w_turbine = h₃ - h₄

  ④ → ①  CONDENSER:  Reject heat at constant pressure.
                      Cool/condense exhaust steam back to liquid.
                      Q_out = h₄ - h₁

  η_Rankine = (w_turbine - w_pump) / Q_in
            = [(h₃ - h₄) - (h₂ - h₁)] / (h₃ - h₂)

  RANKINE ADVANTAGE OVER CARNOT:
  Pump work is tiny (compressing a liquid ≈ 1-3% of turbine work)
  Carnot requires compressing a two-phase mixture — impractical
  Rankine avoids this by condensing fully, then pumping pure liquid
```

### Subcritical vs Supercritical vs Ultra-Supercritical

The three tiers of Rankine cycle represent increasingly aggressive steam parameters,
limited by metallurgy.

```
RANKINE TIERS — STEAM CONDITIONS AND EFFICIENCY:

  Tier              P_boiler    T_main    T_reheat    η_plant    Materials
  ────────────────  ────────    ──────    ────────    ───────    ──────────
  Subcritical       165 bar     540°C     540°C       33-38%     Ferritic steel
  (pre-2000s)                                                     (T22, T91)

  Supercritical     250 bar     600°C     600-610°C   40-43%     Austenitic steel
  (SC, 2000s+)                                                    (TP347HFG, Super304)

  Ultra-SC (USC)    300+ bar    700°C+    720°C+      45-47%     Ni-base superalloy
  (demo/pilot)                                                    (Inconel 740H)

  Advanced USC      350+ bar    760°C+    760°C+      47-50%     Under development
  (A-USC, R&D)                                                    (ceramics, coatings)


  T-s COMPARISON (schematic):

  T (K)
  │
  │  USC ───────────────────── ③''     (highest T_max = 973+ K)
  │                           ╱
  │  SC ────────────────── ③'          (T_max = 873 K)
  │                       ╱
  │  Sub ──────────── ③              (T_max = 813 K)
  │                 ╱
  │               ╱  All share similar T_cold (~310 K condenser)
  │             ╱
  │  ④───④'──④''                       (same condenser conditions)
  │
  └─────────────────────────────── s

  Each tier raises T_H → raises Carnot ceiling → captures more exergy
  Diminishing returns: 540→600°C = +5% points; 600→700°C = +4% points
  Materials cost and risk escalate nonlinearly with temperature
```

### Reheat and Regeneration — Wringing Out More Work

Two modifications that every real Rankine plant uses to improve efficiency beyond the
simple four-step cycle.

```
REHEAT — Expand in two stages, reheat between them:

  T (K)
  │
  │    T_max ──── ③─────────── ③'    (reheat to original T after partial expansion)
  │              ╱               ╲
  │             ╱                 ╲
  │            ╱                   ╲
  │   ② ─────╱                     ╲
  │   │                              ④  (final expansion to condenser)
  │   │                              │
  T_c ①──────────────────────────────╱
  │
  └────────────────────────────────── s

  WHY REHEAT:
  1. Prevents excessive moisture in LP turbine stages
     (moisture > 10-12% causes blade erosion → mechanical failure)
  2. Increases average temperature of heat addition → higher η
  3. Single reheat: +3-4% efficiency gain
  4. Double reheat: additional +1.5-2% (used in largest USC plants)

  DOUBLE REHEAT STATIONS:
  Few examples: Nordjylland 3 (Denmark, 410 MW, 580°C/580°C/580°C, η=47%)
  Complexity and cost favor single reheat for most plants

────────────────────────────────────────────────────────────────────

REGENERATIVE FEEDWATER HEATING — Use bleed steam to preheat feedwater:

  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │  Turbine: HP ──►[bleed]──► IP ──►[bleed]──► LP ──► Cond. │
  │                   │                │                       │
  │                   ▼                ▼                       │
  │              [FWH #1]         [FWH #2]                    │
  │              (closed or       (open /                     │
  │               open)           deaerator)                  │
  │                   │                │                       │
  │                   ▼                ▼                       │
  │              ───── Feedwater heated from ~35°C to ~250°C  │
  │                    before entering the boiler              │
  └────────────────────────────────────────────────────────────┘

  WHY REGENERATION:
  Heating feedwater with bleed steam replaces low-grade heat addition
  in the boiler (where fuel is burned). The extracted steam would have
  produced some work in the remaining turbine stages — but less work
  than the exergy gain from raising feedwater temperature.

  Net effect: raises the average temperature of external heat addition
  → closer to Carnot → typically +4-7% efficiency gain

  Modern coal plant: 6-8 feedwater heaters
  Nuclear plant: 4-6 feedwater heaters (lower pressures)

  DEAERATOR:
  One feedwater heater is "open" (direct contact) — also removes
  dissolved O₂ and CO₂ from feedwater (prevents boiler corrosion).
  Operating at ~1-3 bar, ~120-150°C.
```

### Rankine Cycle Losses — Where the Exergy Dies

```
EXERGY DESTRUCTION BREAKDOWN — Typical 600 MW Supercritical Coal Plant:

  Component           Exergy destroyed    % of fuel exergy    Why
  ──────────────────  ──────────────────  ──────────────────  ──────────────
  Combustion          ~25-30%             Largest single      Flame at ~2000 K
  (boiler furnace)                        loss                transfers to steam
                                                              at 600°C → huge ΔT

  Heat transfer       ~5-8%              Finite ΔT across    Pinch points in
  (boiler tubes)                          tube walls          superheater, reheater

  Turbine             ~4-6%              Blade friction,      LP stages worst
  (expansion)                             tip leakage,        (large volume,
                                          moisture            wet steam)

  Condenser           ~3-5%              Reject heat at       T_cold > T_ambient
  (heat rejection)                        ~35-45°C not 15°C   approach ΔT = 10-15°C

  Auxiliaries         ~3-5%              Fans, pumps, mills,  Feed pump = biggest
  (plant parasitic)                       coal handling        single aux load

  Stack gas           ~3-5%              Flue gas exits at    Acid dew point limits
  (sensible heat)                         120-150°C            how cool you can go

  Generator + elec    ~1-2%              I²R, magnetic,       Minor
                                          transformer

  TOTAL DESTROYED:    ~45-60%
  η_plant (net):      ~40-43% (SC), ~45-47% (USC)

  THE DOMINANT LOSS: Combustion irreversibility (~25-30%)
  Burning fuel at ~2000 K to heat steam to 600 K is a massive voluntary
  exergy destruction. The Alchemist's response: raise T_H (USC, A-USC)
  or skip combustion entirely (fuel cells convert chemical → electrical
  directly, bypassing the Carnot tax on the thermal intermediate).
```

---

## The Brayton Cycle — Gas Turbines

The Brayton cycle is the basis for all gas turbines: aviation jet engines, industrial
power turbines, and the topping cycle in combined-cycle plants. Working fluid stays
gaseous throughout — no phase change.

### Ideal Brayton Cycle

```
IDEAL BRAYTON CYCLE — T-s DIAGRAM:

  T (K)
  │
  │        ③ ──────────────── T_max (~1500-1700 K)
  │       ╱ ╲
  │      ╱   ╲
  │     ╱     ╲   TURBINE: ③→④ (isentropic expansion)
  │    ╱       ╲
  │   ╱         ╲
  │  ②           ④  (~800-900 K exhaust)
  │   ╲         ╱
  │    ╲       ╱
  │     ╲     ╱
  │      ╲   ╱   COMPRESSOR: ①→② (isentropic compression)
  │       ╲ ╱
  │        ① ────────────── T_ambient (~288-310 K)
  │
  └─────────────────────── s (entropy)

  THE FOUR STEPS:
  ① → ②  COMPRESSOR:    Compress ambient air (pressure ratio 15-25:1)
                         w_comp = h₂ - h₁ = cp(T₂ - T₁)
                         THIS IS EXPENSIVE: 50-60% of turbine output

  ② → ③  COMBUSTOR:     Burn fuel (natural gas) with compressed air
                         Q_in = h₃ - h₂ = cp(T₃ - T₂)
                         T₃ = 1500-1700 K (turbine inlet temperature, TIT)

  ③ → ④  TURBINE:       Expand hot gas through turbine
                         w_turb = h₃ - h₄ = cp(T₃ - T₄)
                         Net work = w_turb - w_comp

  ④ → ①  EXHAUST:       Hot gas exhausted to atmosphere
                         (open cycle) or cooled (closed cycle)
                         T₄ ≈ 500-650°C — this is the "leftover" the
                         Rankine bottoming cycle will capture in CCGT

  η_Brayton = 1 - (T₁/T₂) = 1 - 1/r^((γ-1)/γ)

  where r = pressure ratio (P₂/P₁), γ = cp/cv ≈ 1.4 for air

  AT r = 20:  η_ideal = 1 - 1/20^(0.4/1.4) = 1 - 1/2.35 = 57.5%
  AT r = 30:  η_ideal = 1 - 1/30^(0.286) = 1 - 1/2.68 = 62.7%

  Actual η = 35-42% (OCGT) due to compressor/turbine irreversibilities,
  combustion losses, cooling air diversion, and pressure drops.
```

### Why Turbine Inlet Temperature (TIT) Is Everything

```
THE TIT RACE — Efficiency vs Materials:

  Decade     TIT (°C)    TIT (K)    OCGT η    Key technology enabler
  ─────────  ──────────  ─────────  ────────  ─────────────────────────
  1960s       900        1173       25-28%    Forged nickel alloys
  1970s      1050        1323       28-32%    Vacuum-cast blades
  1980s      1200        1473       32-36%    Directional solidification
  1990s      1350        1623       36-39%    Single-crystal blades (CMSX-4)
  2000s      1400        1673       38-40%    Film cooling, TBC coatings
  2010s      1500        1773       40-42%    Advanced TBCs, cooling designs
  2020s      1600+       1873+      42-44%    Ceramic matrix composites (CMC)

  BLADE COOLING:
  HP turbine blades operate in gas hotter than their melting point.
  Internal cooling channels + film cooling + thermal barrier coating (TBC)
  keep metal temperature ~200-300°C below gas temperature.

  ┌────────────────────────────────────────────────────┐
  │  Gas path: 1600°C                                  │
  │  ▓▓▓▓▓▓▓▓▓▓▓ TBC (ceramic, yttria-stabilized ZrO₂)│
  │  ─── Bond coat (MCrAlY)                            │
  │  ████████████ Ni-base superalloy blade (single crystal) │
  │  ○○○○○○○○○○○ Internal cooling passages (compressed air) │
  │  Metal temp: ~1000-1050°C                          │
  │  Blade temp limit: ~1100°C (creep life)            │
  └────────────────────────────────────────────────────┘

  Cooling air = parasitic load: 15-25% of compressor air diverted to cooling
  → reduces net work output
  → there is an optimal TIT beyond which more cooling negates the efficiency gain

  CMC REVOLUTION:
  Ceramic matrix composites (SiC/SiC) can operate at ~1300°C without cooling
  vs Ni superalloy at ~1050°C with cooling
  → Reduces or eliminates cooling air → net efficiency gain
  GE and Safran using CMC in aviation (LEAP engine) and power (HA turbines)
```

### Open-Cycle Gas Turbine (OCGT) — The Peaker

```
OCGT IN POWER GENERATION:

  Natural gas + air → [COMPRESSOR] → [COMBUSTOR] → [TURBINE] → exhaust
                                                       │
                                                    Generator
                                                       │
                                                    → Grid

  ROLE:    Peaker plant. Starts in 5-15 minutes. Runs 500-2000 hours/yr.
  η:       35-42%
  CAPEX:   $400-700/kW (low — simple, fast to build)
  OPEX:    High fuel cost (gas) + moderate maintenance
  CF:      10-30% (runs only during peak demand)
  Ramp:    10-30 MW/min (fast response for grid needs)

  GE LM6000 (aero-derivative):  46 MW, η=42%, 10-min start
  GE 7HA.03 (heavy-duty):       375-430 MW, η=44%, 30-min start
  Siemens SGT-800:              62 MW, η=41%, 15-min start

  WHY STILL BUILT:
  At high VRE penetration, the grid needs fast-start capacity for:
  1. Evening ramp (duck curve neck)
  2. Unexpected wind/solar shortfall
  3. Cold snaps and heat waves (extreme demand events)
  BESS is replacing peakers for <4h duration; gas peakers remain
  for longer events until long-duration storage materializes.

  BRIDGE: OCGT in the grid = on-demand compute instance.
  Low utilization (CF 10-30%), high marginal cost, but critical for peak.
  Cloud spot instances serve a similar function — available on demand,
  higher price per unit, essential for burst capacity.
```

### Brayton with Regeneration (Recuperation)

```
RECUPERATED BRAYTON CYCLE:

  T (K)
  │
  │        ③ ─────────── T_max
  │       ╱ ╲
  │      ╱   ╲
  │     ╱     ╲
  │    ╱       ╲
  │   ②'        ④    exhaust T₄ still hot (~500°C)
  │   ╱ ↑       │ ↓
  │  ②  │regen  ④'   exhaust cooled after recuperator
  │   ╲ │       ╱
  │    ╲│      ╱
  │     ①─────╱
  │
  └──────────────── s

  REGENERATOR (recuperator): heat exchanger between hot exhaust (④)
  and compressed air (②), preheating air before combustor entry.

  ②→②': compressed air heated by exhaust (saves fuel)
  ④→④': exhaust cooled (waste heat recovered)

  η_regen = 1 - (T₁/T₃) × r^((γ-1)/γ)

  When r is LOW and T₃/T₁ is HIGH, regeneration helps most.
  At high pressure ratios, compressor exit T₂ approaches turbine
  exit T₄ → no temperature gradient → regenerator useless.

  APPLICATION: nuclear HTGR (helium Brayton with regenerator)
  Helium at 950°C from reactor → turbine → recuperator → cooler
  η ≈ 45-48% (vs 33% for Rankine at same heat source)
  No steam, no phase change, compact turbomachinery
```

---

## The Combined Cycle — Engineering's Best Answer

The combined-cycle gas turbine (CCGT) is the highest-efficiency thermal power plant
in commercial service. It is the Alchemist's masterpiece of cascade: extract work from
the hottest gas first (Brayton), then extract more work from its still-hot exhaust
(Rankine). Two taxes paid on the same fuel, two revenue streams captured.

### How CCGT Works

```
COMBINED CYCLE GAS TURBINE — SYSTEM DIAGRAM:

  Natural gas + air
        │
        ▼
  ┌─────────────────────────────────────────────────────┐
  │  GAS TURBINE (Brayton topping cycle)                │
  │                                                      │
  │  [Compressor] → [Combustor] → [Turbine] → Generator │
  │                                    │                  │
  │  Exhaust gas: ~550-650°C           │                  │
  └────────────────────────────────────┼──────────────────┘
                                       │
                                       ▼
  ┌─────────────────────────────────────────────────────┐
  │  HRSG (Heat Recovery Steam Generator)                │
  │                                                      │
  │  Exhaust gas passes through:                         │
  │    HP superheater → HP evaporator → HP economizer   │
  │    IP superheater → IP evaporator → IP economizer   │
  │    LP superheater → LP evaporator → LP economizer   │
  │                                                      │
  │  Three pressure levels extract maximum heat          │
  │  HP steam: ~565°C / 170 bar                          │
  │  IP steam: ~565°C / 40 bar                           │
  │  LP steam: ~250°C / 5 bar                            │
  │                                                      │
  │  Stack gas exit: ~80-100°C (nearly all heat captured)│
  └────────────┬─────────────────────────────────────────┘
               │  Steam at three pressures
               ▼
  ┌─────────────────────────────────────────────────────┐
  │  STEAM TURBINE (Rankine bottoming cycle)             │
  │                                                      │
  │  HP turbine → IP turbine → LP turbine → Condenser  │
  │                                              │       │
  │                                           Generator  │
  └──────────────────────────────────────────────────────┘

  EFFICIENCY ARITHMETIC:
  Gas turbine (Brayton): η_GT ≈ 40%
  Of the 60% waste heat, HRSG captures ~90%: available = 54%
  Steam turbine (Rankine): η_ST ≈ 33% of available heat = 18%

  η_combined = η_GT + (1 - η_GT) × η_HRSG × η_ST
             = 0.40 + 0.60 × 0.90 × 0.33
             = 0.40 + 0.18 = 0.58

  Best modern CCGT: 62-64% (GE 9HA.02, Siemens SGT5-9000HL)
  The extra 4-6% comes from higher TIT, better cooling, optimized HRSG
```

### T-s Diagram of Combined Cycle

```
COMBINED CYCLE — COMPOSITE T-s DIAGRAM:

  T (K)
  │
  │ 1700│       ③_gas ────── TIT (gas turbine peak)
  │     │      ╱ ╲
  │ 1400│     ╱   ╲         BRAYTON CYCLE (gas)
  │     │    ╱     ╲
  │ 1100│   ╱       ╲
  │     │  ②         ╲
  │  800│              ④_gas ── exhaust enters HRSG
  │     │              │
  │     │              │  HEAT TRANSFER (gas → steam)
  │     │              │
  │  600│       ③_stm ─── HP steam (superheated)
  │     │      ╱ ╲
  │  450│     ╱   ╲        RANKINE CYCLE (steam)
  │     │    ╱     ╲
  │  310│   ╱       ④_stm ── condenser
  │     │  ①_stm ───╱
  │
  └──────────────────────────────────── s (entropy)

  THE TWO CYCLES SHARE NO WORKING FLUID — only heat.
  Gas cycle working fluid: air/combustion products
  Steam cycle working fluid: H₂O
  HRSG is the thermal bridge between them.

  THE PINCH POINT:
  In the HRSG, the minimum temperature difference between gas and steam
  (the "pinch") must be maintained (typically ΔT_pinch ≥ 8-15°C).
  If pinch is too small: infinite heat exchanger area (cost).
  If pinch is too large: lost efficiency (exergy destruction).
  Optimal pinch ≈ 8-12°C — engineering trade between cost and performance.

  THREE-PRESSURE HRSG:
  Multiple pressure levels allow steam to be generated at different
  temperatures, better matching the gas cooling curve.
  This reduces the average ΔT → less exergy destruction.
  Triple-pressure with reheat is standard for large CCGT (>400 MW).
```

### The CCGT Fleet — Key Machines

```
WORLD'S MOST EFFICIENT CCGT UNITS (2024):

  Model                    GT Output   CC Output   CC η (LHV)   TIT
  ───────────────────────  ─────────   ─────────   ──────────   ─────
  GE 9HA.02 + D650 ST     382 MW GT   >680 MW CC   64.0%       1600°C+
  Siemens SGT5-9000HL     375 MW GT   >650 MW CC   63.5%       1600°C
  MHPS M701JAC            360 MW GT   >630 MW CC   63.0%       1600°C
  GE 7HA.03               375-430 GT  >640 MW CC   64.2%       1600°C+

  OPERATIONAL CHARACTERISTICS:
  Cold start:      2-4 hours (GT ready in 30 min; steam system needs soak)
  Hot start:       <1 hour (if shut down <8 hours ago)
  Ramp rate:       30-50 MW/min (GT section)
  Minimum load:    30-40% (GT can turn down, but efficiency drops sharply)
  Fuel:            Natural gas (primary); fuel oil (backup, rare)
  Lifetime:        25-30 years; major overhaul every 4-6 years
  CAPEX:           $700-1,100/kW (vs $400-700 for OCGT)

  WHY CCGT EFFICIENCY BEATS EVERYTHING ELSE:
  η_Carnot at TIT=1600°C, T_cold=35°C = 1 - 308/1873 = 83.6%
  η_actual = 64% → realizes 76% of Carnot limit
  No other deployed thermal cycle comes close to this ratio.
```

### CCGT Operating Modes

```
CCGT DISPATCH MODES IN HIGH-VRE GRIDS:

  MODE         HOURS/YR    REASON                 η IMPACT
  ───────────  ─────────   ─────────────────────  ─────────────
  Baseload     5000-7000   Cheap gas, high CF     Peak η ~63%
  (traditional)

  Mid-merit    3000-5000   VRE displaces midday   η drops at
  (2020s)                  → CCGT morning/evening  part-load

  Cycling      1000-3000   Frequent start/stop    Thermal stress
  (high VRE)               overnight shutdowns    + lower avg η

  Peaking      500-1500    Only during "dark      OCGT mode (GT
  (future?)                doldrums" or peaks     only) — η ~40%

  THE FLEXIBILITY PROBLEM:
  CCGT was designed for continuous baseload operation.
  High-VRE grids demand frequent cycling → thermal stress on HRSG,
  steam turbine, and GT hot section → higher maintenance costs.
  Modern "flex-CCGT" designs (Siemens Flex-Plant, GE TrueChoice Flex)
  optimize for cycling: faster starts, wider turn-down, better part-load η.

  BRIDGE: CCGT operational transition mirrors the shift from
  dedicated on-prem servers (always-on, high utilization) to
  cloud instances that scale up/down. The infrastructure was designed
  for steady-state; the workload became bursty. Both domains respond
  with architectures optimized for variable load (auto-scaling / flex plants).
```

---

## Supercritical CO₂ (sCO₂) Brayton Cycle — Next Generation

The sCO₂ cycle is the most promising next-generation power cycle. It exploits the
unusual properties of CO₂ near its critical point (31.1°C, 73.8 bar): extremely high
density approaching that of a liquid, but compressibility of a gas.

```
sCO₂ CRITICAL POINT AND PROPERTIES:

  Property              Near critical       Far from critical     Water (steam)
                        (35°C, 80 bar)      (500°C, 200 bar)
  ──────────────────    ────────────────    ──────────────────    ─────────────
  Density (kg/m³)       ~500-700            ~100-150              ~25 (at 250 bar)
  Cp (kJ/kg·K)         ~10-50 (peaks!)     ~1.2                  ~2.5
  Compressibility       Very low (liquid-   Moderate              Moderate
                        like)

  WHY THIS MATTERS FOR TURBOMACHINERY:
  High density near critical point → compression requires very little work
  (compressing a dense fluid is cheap — same reason Rankine pump work is tiny)
  → Net cycle work = turbine - compressor is a larger fraction of turbine work
  → Higher cycle efficiency for the same temperature ratio

  sCO₂ SIMPLE RECUPERATED BRAYTON CYCLE:

  T (K)
  │
  │  T_max ──── ③───────── (700-1000 K, depending on heat source)
  │            ╱   ╲
  │           ╱     ╲     TURBINE: ③→④
  │          ╱       ╲
  │  ②' ───╱    REGEN  ④   exhaust
  │  ↑               │ ↓
  │  ②               ④'   cooled exhaust
  │   ╲             ╱
  │    ╲           ╱
  │     ① ───────╱          near critical point (~35°C, 80 bar)
  │
  └──────────────────── s

  COMPRESSION NEAR CRITICAL POINT:
  ① → ② is near the critical point → density is high → w_comp is small
  Compressor work = ∫v dP ≈ v × ΔP (v is tiny near critical → tiny work)
  Compare to ideal gas Brayton: w_comp can be 50-60% of w_turb
  In sCO₂: w_comp can be only 25-30% of w_turb → more net output

  RECUPERATION IS ESSENTIAL:
  Without recuperation, sCO₂ cycle is mediocre (~25% for low T_max)
  With recuperation (preheating compressed CO₂ from turbine exhaust):
  η can reach 45-55% depending on T_max

  HEAT SOURCE COMPATIBILITY:
  Nuclear (HTGR, MSR):      700-900°C → sCO₂ η ~45-48%
  CSP (solar tower):        600-800°C → sCO₂ η ~42-48%
  Fossil (coal/gas):        700-1000°C → sCO₂ η ~50-55%
  Waste heat recovery:      300-600°C → sCO₂ η ~25-35%
```

### Why sCO₂ Is a Big Deal

```
sCO₂ vs STEAM RANKINE — COMPARISON:

  Property                sCO₂ Brayton          Steam Rankine
  ──────────────────────  ──────────────────    ──────────────────
  Turbine size            10× smaller           Large (multi-stage)
  (for same power)        (high density, compact) (low density steam)

  Compressor work         25-30% of turbine     1-3% (pump, liquid)
  (relative to turbine)

  Working fluid toxicity  Non-toxic, inert      Non-toxic (steam)
  Pressure                80-300 bar            150-300 bar (SC steam)
  Phase change            None (always sCO₂)    Yes (water → steam)
  Heat source temp range  300-1000°C+           200-760°C+
  Cycle η at 700°C        ~47%                  ~42% (SC Rankine)
  Footprint               ~1/10 of steam plant  Large turbine hall

  THE COMPACT TURBINE ADVANTAGE:
  sCO₂ at 200 bar, 700°C has density ~80 kg/m³
  Steam at 250 bar, 600°C has density ~45 kg/m³
  → sCO₂ turbine blades see much denser working fluid
  → Same mass flow rate through smaller annulus
  → Turbine diameter: ~1 m for 10 MW sCO₂ vs ~3 m for 10 MW steam
  → Enormous implications for nuclear (compact, modular) and CSP

  DEVELOPMENT STATUS (2024):
  Sandia National Labs: 1 MW test loop (operational since 2016)
  GE/SwRI/GTI: 10 MW pilot (DOE STEP program, San Antonio TX)
  Echogen: EPS100 (8 MW waste heat recovery, commercial)
  Korean KIER: 250 kW test loop for nuclear application
  Full commercial: 2028-2035 expected for first utility-scale deployment

  BRIDGE: sCO₂ turbomachinery compactness vs steam is analogous to
  the RISC vs CISC revolution in processors. Same function, radically
  smaller/simpler hardware, higher throughput per unit volume. The
  physical footprint shrinks by an order of magnitude while performance
  improves — enabling deployment in previously space-constrained
  environments (submarines, space reactors, modular nuclear).
```

---

## Organic Rankine Cycle (ORC) — Harvesting Low-Grade Heat

The ORC uses organic fluids (hydrocarbons, refrigerants) instead of water. These fluids
have lower boiling points, enabling power generation from heat sources as low as 80°C.

```
ORC PRINCIPLE:

  Standard Rankine (water):  boils at 100°C (1 atm), 311°C (100 bar)
  → Needs heat source > 350°C for reasonable efficiency

  ORC fluids:
  ┌──────────────┬──────────────┬───────────────────────┬────────────┐
  │ Fluid        │ T_boil (1atm)│ Typical heat source   │ η_cycle    │
  ├──────────────┼──────────────┼───────────────────────┼────────────┤
  │ n-Pentane    │  36°C        │ 120-200°C             │ 10-16%     │
  │ R245fa       │  15°C        │ 80-170°C              │  8-14%     │
  │ Toluene      │ 111°C        │ 200-350°C             │ 18-24%     │
  │ Siloxane MDM │ 153°C        │ 250-400°C             │ 20-26%     │
  │ Cyclopentane │  49°C        │ 150-250°C             │ 12-18%     │
  └──────────────┴──────────────┴───────────────────────┴────────────┘

  ORC SYSTEM DIAGRAM:

  LOW-GRADE HEAT SOURCE (80-400°C)
  (geothermal, waste heat, biomass, solar thermal)
        │
        ▼
  ┌──────────────────┐
  │  EVAPORATOR       │  Organic fluid boils at low temperature
  │  (heat exchanger) │
  └────────┬─────────┘
           │ Organic vapor
           ▼
  ┌──────────────────┐
  │  TURBINE / EXPANDER │  Vapor expands → shaft work → generator
  │  (single-stage)     │  (simpler than multi-stage steam turbine)
  └────────┬────────────┘
           │ Low-pressure vapor
           ▼
  ┌──────────────────┐
  │  CONDENSER        │  Vapor condenses at ~25-40°C
  └────────┬─────────┘
           │ Liquid
           ▼
  ┌──────────────────┐
  │  PUMP             │  Pressurize liquid back to evaporator
  └──────────────────┘

  KEY ORC PROPERTY — "DRY EXPANSION":
  Most organic fluids are "dry" — their saturation curve slopes right
  on the T-s diagram. Expansion from saturated vapor ends in the
  superheated region, not in the two-phase region.
  → No moisture in the turbine → no blade erosion → simpler turbine
  → Can use single-stage radial turbines (vs multi-stage axial for steam)
```

### ORC Applications

```
ORC DEPLOYMENT:

  APPLICATION           HEAT SOURCE T    SCALE       INSTALLED (2024)
  ────────────────────  ────────────     ──────      ────────────────
  Geothermal binary     80-180°C         1-50 MW     ~3 GW globally
  (most common ORC)                                  (60%+ of ORC market)

  Industrial waste heat 150-400°C        0.5-10 MW   ~1 GW
  (cement, glass, steel)

  Biomass CHP           250-350°C        0.5-5 MW    ~2 GW
  (wood, biogas)

  Solar thermal (small) 150-300°C        50 kW-5 MW  ~0.3 GW
  (parabolic trough)

  Engine waste heat     350-500°C        10-500 kW    Pilot stage
  (marine diesel, truck) (exhaust gas)                (Cummins, MAN)

  TOTAL ORC INSTALLED: ~6-7 GW globally
  MARKET LEADERS: Turboden (Mitsubishi), ORMAT, Enertime, Atlas Copco

  EFFICIENCY REALITY CHECK:
  ORC η = 10-25%, which sounds terrible. But the alternative is often:
  • Geothermal at 120°C: Rankine impossible (T < boiling point of water
    at economical pressures). ORC at 12% vs nothing = infinite improvement.
  • Industrial waste heat at 200°C: currently dumped to atmosphere.
    ORC at 15% converts free heat → electricity. Payback: 3-5 years.

  The Alchemist's perspective: ORC doesn't violate thermodynamics —
  it obeys it honestly. Low T_H → low Carnot ceiling → low η.
  But any exergy recovered from waste heat is pure profit.
```

---

## The Allam-Fetvedt Cycle — Carbon Capture Built In

This cycle deserves special treatment because it solves a seemingly impossible problem:
burn natural gas at combined-cycle efficiency with near-zero CO₂ emissions, *without*
post-combustion capture.

```
ALLAM-FETVEDT CYCLE SCHEMATIC:

  Natural gas + PURE O₂ (from ASU)
        │
        ▼
  ┌──────────────────────────────────────────────┐
  │  COMBUSTOR                                    │
  │  Oxy-combustion: CH₄ + 2O₂ → CO₂ + 2H₂O    │
  │  Working fluid: supercritical CO₂ at ~300 bar │
  │  T_combustor: ~1150°C                         │
  └────────┬─────────────────────────────────────┘
           │  sCO₂ + H₂O at 1150°C, 300 bar
           ▼
  ┌──────────────────────────────────────────────┐
  │  sCO₂ TURBINE                                 │
  │  Expansion: 300 bar → 30 bar                  │
  │  Power output: generator                      │
  └────────┬─────────────────────────────────────┘
           │  Exhaust: ~700°C, 30 bar
           ▼
  ┌──────────────────────────────────────────────┐
  │  RECUPERATOR (multi-stream heat exchanger)    │
  │  Hot exhaust preheats recycled CO₂            │
  │  Cooled exhaust → water separator             │
  └────────┬─────────────────────────────────────┘
           │
           ├──► H₂O separated (condensed out)
           │
           ├──► CO₂ stream splits:
           │      95% → recompressed → recycled to combustor
           │       5% → pipeline/storage (the NET CO₂ produced)
           │
           └──► Recycled CO₂ → compressor → recuperator → combustor
                (closed loop with 5% bleed-off)

  KEY INNOVATION:
  sCO₂ is both the working fluid AND the combustion product.
  No N₂ in the combustor (pure O₂) → exhaust is CO₂ + H₂O.
  Condense the water → nearly pure CO₂ stream.
  No amine scrubbing, no post-combustion capture equipment.

  EFFICIENCY:   ~51-54% net (after ASU and CO₂ compressor parasitic loads)
                (comparable to CCGT's ~60-64%, but with 97%+ CO₂ capture)

  CO₂ CAPTURE:  Inherent — the CO₂ IS the working fluid.
                Capture rate: 97-99% (the small bleed stream)
                vs amine scrubbing: 85-90% capture with 20%+ energy penalty

  STATUS:
  NET Power 50 MW thermal demo (La Porte, TX): operated 2018-2022
  NET Power commercial plant: 280 MWe proposed, Occidental partnership
  Timeline: first commercial operation ~2026-2028
  Economic target: LCOE competitive with CCGT + CCS

  THE ALCHEMIST'S TAKE:
  The Allam cycle is elegant because it makes the pollution product
  (CO₂) into the working fluid. The thermodynamic penalty of capture
  is absorbed into the cycle design rather than bolted on afterward.
  It is not magic — the air separation unit (ASU) for pure O₂ consumes
  ~10-15% of gross power. But the NET penalty is far lower than
  post-combustion CCS because no amine regeneration heat is needed.
```

---

## Cycle Comparison — The Alchemist's Scoreboard

```
THERMAL CYCLE HEAD-TO-HEAD:

  Cycle             T_H range     η_actual   Fuel/Source        Maturity
  ────────────────  ──────────    ────────   ─────────────      ────────
  Subcrit. Rankine  540°C         33-38%     Coal, nuclear PWR  Mature
  SC Rankine        600°C         40-43%     Coal, nuclear      Mature
  USC Rankine       700°C+        45-47%     Coal (advanced)    Demo
  ORC               80-350°C      10-25%     Waste heat, geo    Mature
  OCGT (Brayton)    1500-1700°C   35-42%     Natural gas        Mature
  CCGT (Combined)   1600°C+GT     58-64%     Natural gas        Mature
  sCO₂ Brayton      700-1000°C    45-55%     Nuclear, CSP, WH   Pilot
  Allam-Fetvedt     1150°C        51-54%     Natural gas+O₂     Demo
  Helium Brayton    950°C         45-48%     Nuclear HTGR       Design
  Stirling          700-1000°C    25-35%     Any external heat  Niche

  EXERGY EFFICIENCY (2nd law — what fraction of available work is captured):

  Cycle                η_exergy (η_actual / η_Carnot)
  ────────────────     ──────────────────────────────
  Subcrit. Rankine      55-62%
  SC Rankine            62-68%
  OCGT                  44-52%
  CCGT                  74-80%   ← best deployed
  sCO₂ (projected)     70-78%
  ORC (at 150°C)        35-45%

  BRIDGE: Exergy efficiency is to thermal cycles what algorithmic efficiency
  is to computation. A sort algorithm's actual time vs the Θ(n log n) lower
  bound gives you "how close to optimal." An η_exergy of 76% means the CCGT
  realizes 76% of the thermodynamically possible work — the remaining 24%
  is the sum of all internal irreversibilities. Optimizing a power cycle is
  literally the same mathematical structure as profiling and optimizing code:
  identify the largest loss terms and attack them in order.
```

---

## Heat Rejection — The Condenser Problem

Every thermal cycle must reject waste heat at T_cold. How you reject it matters for
efficiency, water use, and environmental impact.

```
HEAT REJECTION METHODS:

  METHOD              T_cold ACHIEVED   WATER USE        ENVIRONMENTAL
  ──────────────────  ────────────────  ───────────────  ───────────────
  Once-through        ~20-25°C          HIGH             Thermal discharge
  (river/sea water)   (ambient water T) ~100 L/MWh       to water body
                      Best η (lowest    (USGS: 41% of
                      T_cold)           US freshwater
                                        withdrawal!)

  Wet cooling tower   ~25-35°C          MODERATE         Evaporative plume
  (evaporative)       (approaches       ~2-3 L/MWh       visible in winter
                      wet-bulb T)       consumed (evap)

  Dry cooling         ~35-50°C          ZERO             No water use; large
  (air-cooled)        (approaches       (fans only)      fan arrays, noisy
                      dry-bulb T)                        η penalty: 2-5%

  Hybrid              ~30-40°C          LOW              Best of both;
  (wet + dry)                           ~0.5-1 L/MWh    expensive

  EFFICIENCY IMPACT OF CONDENSER TEMPERATURE:
  For a Rankine cycle with T_H = 600°C (873 K):

  T_cond (°C)   T_cond (K)   η_Carnot    Δη vs 25°C baseline
  ───────────   ──────────   ────────    ────────────────────
  25            298          65.9%        (baseline)
  30            303          65.3%        -0.6%
  35            308          64.7%        -1.2%
  40            313          64.1%        -1.8%
  50            323          63.0%        -2.9%

  Each 10°C increase in condenser temperature costs ~1.2% η_Carnot
  Actual impact is ~0.5-0.8% net plant efficiency per 10°C
  On a 1 GW plant at CF 85%: 0.5% = ~37 GWh/yr lost = ~$1.5M/yr revenue

  WHY DESERT PLANTS USE DRY COOLING:
  Water scarcity (Atacama, Middle East, Australian outback) →
  dry cooling despite 2-5% efficiency penalty.
  Solar PV has zero water footprint → inherent advantage over
  thermal plants in water-scarce regions.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Most efficient deployed thermal cycle? | CCGT at 58-64% (Brayton + Rankine combined) |
| Why CCGT beats everything? | Captures work from gas at 1600 K AND steam at 870 K — two cascaded cycles |
| Rankine subcritical vs supercritical? | SC operates above water's critical point (374°C, 221 bar) → higher T_H → +5-7% |
| What limits Rankine efficiency? | Metallurgy: boiler tube and turbine blade materials set T_max |
| Why nuclear PWR efficiency is only 33%? | T_hot deliberately limited to ~320°C for fuel cladding integrity |
| What is OCGT's grid role? | Peaker: fast start (5-15 min), low CF (10-30%), high marginal cost |
| What is sCO₂ and why does it matter? | CO₂ near critical point is very dense → tiny compressor work → high η in compact package |
| When is sCO₂ better than steam? | T_source 500-800°C; space-constrained (nuclear SMR, offshore, CSP); waste heat |
| What is ORC for? | Low-grade heat (80-350°C) that can't drive a steam cycle: geothermal, waste heat |
| Allam cycle vs CCGT + CCS? | Allam: inherent CO₂ capture (CO₂ is working fluid); CCGT + CCS: bolted-on amine scrubbing |
| Reheat purpose? | Prevent moisture in LP turbine + raise avg T of heat addition → +3-4% η |
| Regenerative feedwater heating? | Bleed steam preheats boiler feedwater → +4-7% η; 6-8 heaters in modern plant |
| Biggest exergy loss in a coal plant? | Combustion irreversibility (~25-30%): flame at 2000 K → steam at 600°C |
| Dry vs wet cooling impact? | Dry cooling raises T_cold by 10-25°C → 1-5% efficiency penalty; saves water |

---

## Common Confusion Points

**"Efficiency is just Carnot minus losses"**
No. The Carnot efficiency sets the ceiling for a cycle operating between T_H and T_C,
but the actual T_H and T_C of a cycle depend on the cycle design. A Rankine cycle at
540°C steam has a different Carnot ceiling than a Brayton at 1600°C gas — even if both
burn the same fuel. The combined cycle captures efficiency by using BOTH temperature
levels. Quoting "Carnot efficiency" without specifying T_H and T_C is meaningless.

**"Higher pressure ratio always means higher Brayton efficiency"**
Only in the ideal case. In practice, higher pressure ratio means higher compressor
exit temperature (T₂), which can approach turbine exit temperature (T₄). When T₂ > T₄,
regeneration becomes impossible and the gain from higher pressure ratio is partly consumed
by larger compressor work. There is an optimal pressure ratio for each TIT that maximizes
net work, and a different optimum that maximizes efficiency. These optima are NOT the same.

**"Combined cycle means combining any two cycles"**
Specifically, it means a Brayton (gas turbine) topping cycle cascading into a Rankine
(steam turbine) bottoming cycle via an HRSG. Other combinations exist (Brayton + sCO₂,
SOFC + gas turbine), but "combined cycle" in industry means CCGT unless stated otherwise.

**"sCO₂ will replace steam everywhere"**
sCO₂ excels at 500-800°C heat sources and compact installations. For very high T_hot
(>1200°C), the Brayton gas turbine is still superior. For very large power output
(>1 GW), multi-stage steam turbines are well-optimized and hard to beat on cost.
sCO₂ will likely dominate the medium-temperature range (nuclear, CSP, waste heat),
not replace all thermal cycles. The installed base of steam infrastructure is enormous
and won't be scrapped for marginal gains.

**"ORC is inefficient, so it's not worth building"**
A 12% efficient ORC recovering 200°C waste heat from a cement kiln produces electricity
from energy that was being discarded. The alternative is 0% efficiency (dumping to atmosphere).
ORC efficiency is low because Carnot is low at those temperatures — the ORC is actually
quite close to Carnot for its temperature range. Efficiency without context is misleading;
what matters is the value of recovered energy vs the cost of the ORC system.

**"The Allam cycle is too good to be true"**
The efficiency claims are real but context matters. The 51-54% net includes the air
separation unit (ASU) that produces pure O₂ — a major parasitic load. Without ASU,
gross efficiency would be higher. The comparison should be: Allam at 52% with 97% CO₂
capture vs CCGT at 62% with 0% capture, or CCGT at 48% with 90% amine CCS. On a
*captured-emission-adjusted* basis, Allam wins. The remaining question is capital cost
and operational reliability at commercial scale — NET Power's first full-scale plant
(~2027) will answer this.

**"Nuclear could be more efficient with higher temperatures"**
Yes, and this is the Gen IV thesis. PWR operates at ~320°C (efficiency ~33%) not because
fission is inefficient but because zirconium fuel cladding degrades above ~350°C and
the pressure vessel must contain 155 bar water. HTGR uses helium coolant at 750-950°C
(no pressure-vessel water) → efficiency 45-48% via Brayton or sCO₂ cycle. Molten salt
reactors can go even higher. The trade is safety case complexity vs efficiency.
