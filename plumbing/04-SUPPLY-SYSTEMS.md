# Supply Systems

## Pressure, Water Heaters, Hammer, Recirculation, Anti-Scald

## The Big Picture

```
RESIDENTIAL SUPPLY SYSTEM OVERVIEW

  Municipal main
  (service pressure: 40–150 PSI)
         ↓
  Curb stop (utility shutoff)
         ↓
  Water meter
         ↓
  Main shutoff (house side of meter)
         ↓
  [Backflow preventer — if required by code]
         ↓
  PRV (pressure reducing valve — if service > 80 PSI)
         ↓
  [Expansion tank — required with backflow preventer]
         ↓
  Main cold supply (3/4" typical residential)
         ↓
    ├──→ Cold to fixtures
    │
    └──→ Water heater inlet (cold)
              ↓
         Water heater
         (120-140°F, storage or tankless)
              ↓
         Hot main
              ↓
         Hot to fixtures

  [Optional: Recirculation pump/loop at end of hot main → back to heater]
```

---

## Pressure

### Municipal Service Pressure

```
  TYPICAL STREET PRESSURE: 60–80 PSI (common residential)
  RANGE: 40–150 PSI (varies by municipality and elevation)

  RESIDENTIAL TARGETS:
    Minimum: 40 PSI at fixtures (adequate shower flow)
    Optimum: 55–70 PSI at point of use
    Maximum: 80 PSI at any fixture — above this:
      → Fixture seals, supply hoses, and washing machine valves
        degrade faster
      → Increased water hammer risk
      → Risk of supply line failure (burst flex hose = major flood)
      → Code requires PRV above 80 PSI in most jurisdictions

  PIPE FRICTION LOSS:
    Pressure drops with distance and flow rate
    Rule of thumb: expect ~5-10 PSI drop from meter to shower
    Undersized supply pipe + long run + high flow = low pressure
    Sizing charts in IRC/IPC tables based on:
      Total developed length (pipe run)
      Total fixture units demanding simultaneously
      Available pressure at source
<!-- @editor[bridge/P1]: The underlying physics is Darcy-Weisbach: ΔP = f × (L/D) × (ρv²/2), where f is the Moody friction factor (function of Reynolds number and relative roughness). For fully turbulent flow in rough pipes, f is approximately constant (Moody chart flat region). This means ΔP ∝ v² ∝ Q² — doubling flow rate quadruples pressure drop. This is the same relationship as congestion in network links: doubling traffic → quadrupling latency increase in many queueing models. The IRC sizing tables are just precomputed Darcy-Weisbach solutions. For this learner, naming the governing equation makes the "rule of thumb" interpretable as physics, not plumber lore. The pump curve interaction (system curve = ΔP vs Q parabola, pump curve = head vs Q, operating point = intersection) is also absent and specifically called for in the calibration. -->
```

### Pressure Reducing Valve (PRV)

```
  FUNCTION: Globe valve with spring-loaded diaphragm
            Inlet pressure: any (typically 80–200 PSI)
            Outlet pressure: adjustable (typically set 55–70 PSI)

  ANATOMY:
  ┌──────────────────────────────────────────────────────────┐
  │  High pressure             Low pressure (set point)       │
  │  inlet ──→                      ──→ outlet               │
  │                                                          │
  │    ┌────────────────────────────────────┐                │
  │    │  Adjusting screw (spring tension)  │                │
  │    │           ↓                        │                │
  │    │     Spring (preset)                │                │
  │    │           ↓                        │                │
  │    │     Diaphragm (flexible)           │                │
  │    │           │                        │                │
  │    │     Valve seat + disc              │                │
  │    └────────────────────────────────────┘                │
  │                                                          │
  │  How it works: outlet pressure pushes on diaphragm       │
  │  → diaphragm compresses spring → closes valve disc       │
  │  Self-regulating: outlet pressure = spring force/area    │
  └──────────────────────────────────────────────────────────┘

  STRAINER: most PRVs have a small screen strainer at inlet
    Clean periodically (unscrew, pull screen, flush, reinstall)
    Clogged strainer = low pressure downstream

  FAILURE MODES:
    Fails open: downstream pressure rises to street pressure
    → fixtures, hoses, supply lines exposed to high pressure
    Fails shut: no water (or very restricted flow)

  DIAGNOSIS:
    Gauge at hose bib: test actual downstream pressure
    If pressure > set point: PRV failed open
    If pressure varies widely with flow: PRV seat worn

  ADJUSTMENT:
    Loosen locknut; turn adjustment screw
    Clockwise = increase pressure
    Counter-clockwise = decrease pressure
    Test at nearby hose bib with gauge; retighten locknut
```

---

## Thermal Expansion and Expansion Tanks

```
  THE CLOSED SYSTEM PROBLEM:

  Open system: water heater heats water → volume expands → excess
               pushes back toward street main → no pressure buildup

  Closed system (with backflow preventer or check valve):
               water heater heats water → volume expands → nowhere to go
               → pressure spike in domestic supply

  WATER EXPANSION:
    Cold water at 50°F → 140°F tank temperature
    Volume expansion: ~3.7% (about 1.5 gallons in a 40-gallon tank)
    If nowhere to go: pressure spike to 150+ PSI
    → PRV relief valve opens (dripping PRV = symptom)
    → Supply lines stressed
    → Tank and heater fittings stressed

  EXPANSION TANK:
  ┌──────────────────────────────────────────────────┐
  │  Bladder/diaphragm tank                          │
  │                                                  │
  │  Air side │ Diaphragm │ Water side               │
  │  (pre-charged to         (connected to supply)   │
  │   supply pressure)                               │
  │                                                  │
  │  As water expands: pushes diaphragm → compresses │
  │  air → absorbs volume increase without pressure  │
  │  spike                                           │
  └──────────────────────────────────────────────────┘

  SIZING:
    IRC Table P2903.4: sized based on supply pressure + tank size
    Typical residential: 2-gallon expansion tank for 40-50 gal heater

  PRE-CHARGE PRESSURE:
    Must match supply pressure (measured at cold supply)
    If under-charged: tank fills with water, loses effectiveness
    Check with tire pressure gauge at Schrader valve
    Re-charge with bicycle pump or air compressor if low
```

---

## Water Hammer

```
  PHYSICS:
    Moving column of water has momentum (mass × velocity)
    Fast-closing valve stops flow suddenly
    → Kinetic energy converts to pressure wave
    → Wave travels back through pipe at ~4,000 ft/sec (speed of sound in water)
    → Banging sound (pipes impact hangers, fittings)
    → Pressure spike: can be 10× operating pressure momentarily

  COMMON SOURCES:
    Solenoid valves (dishwasher fill, washing machine)
    Fast-closing cartridge faucets (1/4-turn ceramic disc)
    Ballcock float valves (old toilet tank filler)
    Irrigation zone valves

  DIAGNOSIS:
    Hammer right at appliance: valve closing too fast
    Hammer at distant location: pipe not supported; wave travels to
                                loose section and bangs against structure

  SOLUTIONS:
    Water hammer arrestors (ASSE 1010 listed):
      Mechanical device: piston + gas chamber absorbs pressure wave
      Install at offending valve (within 6 pipe diameters)
      Rated by fixture type (W = washing machine, D = dishwasher, etc.)
      Unlike air chambers: won't waterlog over time

    Air chambers (traditional):
      Vertical capped pipe above branch — trapped air cushion
      Problem: air gradually dissolves into water → chamber fills
      → Must be re-charged periodically by shutting off water
         and opening fixtures (drains air cushion)

    Slower-closing valves:
      Two-handle faucets vs single-lever (slower close)
      Hammer-preventing washing machine valves (slow-close)

    Pipe strapping:
      Secure loose pipes to structure every 6-8 ft horizontal,
      every 4-6 ft vertical
      Copper: plastic isolating clips (prevent galvanic contact with hangers)
```

---

## Water Heaters

### Storage Tank

```
  ANATOMY:
    Glass-lined steel tank (borosilicate glass fused to steel)
    Anode rod (magnesium or aluminum) — sacrificial corrosion protection
    Temperature-pressure relief valve (T&P) — safety device
    Dip tube (cold in from top, delivers to bottom)
    Hot outlet (from top — hottest water)
    Drain valve (bottom)

  SELECTION METRICS:
    First-hour rating (FHR): gallons delivered in first hour, starting full
      Morning peak demand: two showers back-to-back = ~40-60 gallons
      This is the primary sizing criterion (not tank size)
    Recovery rate: gallons reheated per hour after depletion
      Gas heater 40-gal: ~40 GPH recovery
      Electric 40-gal: ~20 GPH recovery

  GAS WATER HEATERS:
    Atmospheric draft: natural draft through B-vent; simplest; no electricity
    Power vent: fan pushes exhaust horizontally; uses PVC/CPVC flue
                to exterior; requires electricity; flexible installation
    Direct vent: sealed combustion; two coaxial pipes (air in/exhaust out)
                 No combustion air from indoor space; good for tight houses
    Condensing: 90-95% efficiency; PVC flue; expensive; small market share

  ELECTRIC:
    Dual element (upper + lower): upper element handles recovery
                                   lower element handles maintenance heating
    Relay prevents simultaneous operation (single circuit)
    Heat pump water heater (HPWH): strips heat from surrounding air
      COP: ~3.5 (1 kWh electric → 3.5 kWh heat)
      vs resistance heater: COP = 1.0
      HPWH saves ~70% vs resistance electric
      Requirement: ~700 ft³ surrounding air space; works best above 50°F
      ambient; cools and dehumidifies surrounding space (useful in warm climates)
      IRA (Inflation Reduction Act 2022): $300 federal tax credit for HPWH
```

### Temperature Settings: The Legionella Dilemma

```
  THE CONFLICT:
    Scald prevention → 120°F maximum
    Legionella prevention → 140°F minimum

  LEGIONELLA PNEUMOPHILA:
    Bacterium causing Legionnaires' disease (severe pneumonia)
    Survives and multiplies: 77–108°F (25–42°C)
    Killed rapidly: at 131°F (55°C); near instantly at 140°F
    High-risk populations: elderly, immunocompromised, smokers

  STRATEGIES:
    EPA recommendation: 120°F (compromise; lowest scald risk)
    OSHA guideline: 140°F at heater with ASSE 1017 mixing valve
    ASSE 1017 thermostatic mixing valve:
      Installed at water heater outlet
      Mixes cold to deliver 120°F to system
      Heater runs at 140°F (kills Legionella)
      Delivery is 120°F (scald-safe)
      Required for: healthcare, senior living; recommended for homes
                    with young children or elderly

  RISK COMPARISON:
    Residential water heater: low Legionella risk (daily draw keeps water fresh)
    Cooling towers: high risk (slow turnover, spray)
    Large building plumbing: risk if dead legs or underused branches
```

### Tankless Water Heaters

```
  OPERATION:
    Flow switch activates burner/element when flow detected
    Modulating burner (gas) or element (electric) adjusts output
    No storage tank; no standby heat loss

  KEY SPEC: GPM at temperature rise
    Example: 5 GPM at 70°F rise (60°F incoming → 130°F delivery)
    Two simultaneous showers: ~4-6 GPM demand

  GAS TANKLESS (whole-house):
    BTU requirement: 180,000-199,000 BTU/h (vs 40,000 for storage)
    Gas line: 3/4" or 1" required (storage heater: 1/2" typically)
    MUST upsize gas line in most retrofit scenarios
    Flue: direct vent (PVC) or power vent

  ELECTRIC TANKLESS:
    24-36 kW for whole-house in cold climate
    At 240V: 100-150 amps dedicated circuit
    Most residential panels: not enough capacity for whole-house electric tankless
    Only practical for point-of-use (under-sink single fixture)
    or warm climates with small temperature rise

  "COLD WATER SANDWICH" ISSUE:
    After a shower ends briefly, hot water in pipes → resident draws again
    Initial draw: hot (water in pipe) → then cold (heater activating) →
    then hot (heater up to temp)
    Brief cold burst in middle = "cold water sandwich"
    Solution: recirculation system; or accept as limitation of technology
```

---

## Recirculation Systems

```
  PROBLEM: 15-30 seconds waiting for hot water = water wasted
  SOLUTION: keep hot water moving continuously (or on demand)

  DEDICATED RETURN LOOP:
    Hot supply: heater → fixtures → return loop back to heater inlet
    Small pump (Grundfos, Taco) circulates continuously
    Hot water always near fixtures
    DISADVANTAGE: heat loss from return pipe = significant energy penalty
                  (insulate the entire hot + return run)

  MODIFIED RETURN (COMFORT SYSTEM):
    No dedicated return pipe
    Pump + sensor installed at farthest fixture
    Cold supply pipe used as return path
    Thermistor: when hot supply temp drops below threshold → pump runs
    Slightly warms cold water at fixtures (may be noticeable)

  DEMAND-ACTIVATED:
    Button at fixture (or motion sensor, app trigger)
    User presses button; pump runs until hot water detected at fixture
    Pump stops; hot water arrives in 15-30 seconds (vs 30-60+ seconds)
    Lowest energy use; slight wait still
    Best energy-efficiency profile
```

---

## Decision Cheat Sheet

| Situation | Action |
|---|---|
| Street pressure > 80 PSI | Install/adjust PRV |
| PRV installed but T&P valve drips | Install expansion tank |
| Washing machine makes banging sound | Water hammer arrestor at valves |
| Want endless hot water | Tankless gas (properly sized gas line) |
| Minimize energy use | Heat pump water heater (HPWH) |
| Want hottest first shower in house | Large storage tank (80 gal) |
| Legionella concern + scald safety | 140°F heater + ASSE 1017 mixing valve |
| Tired of waiting for hot water | Recirculation (demand-type for efficiency) |

---

## Common Confusion Points

**Dripping T&P relief valve usually means expansion, not excess pressure**: The T&P valve is also designed to relieve thermal expansion when there's no expansion tank and the system is closed. A dripping T&P usually means you need an expansion tank, not that your PRV failed.

**Tankless doesn't mean unlimited hot water at any flow**: Tankless heaters are flow-rate limited. A 5 GPM unit running two showers + a dishwasher may fall short. Calculate actual peak demand before specifying.

**"First-hour rating" matters more than tank size**: Two 50-gallon tanks with different FHR provide different amounts of hot water. FHR depends on recovery rate AND starting capacity. Look at FHR on the yellow EnergyGuide label.

**Water hammer arrestors are not the same as air chambers**: Air chambers (capped pipes) waterlog over time. ASSE 1010-listed mechanical arrestors don't. If the old "air chamber" no longer works, replace with a real arrestor.
