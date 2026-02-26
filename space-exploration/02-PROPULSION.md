# Propulsion Systems: Chemical to Electric

## The Big Picture

All rocket propulsion works by the same principle: expelling mass backward to create thrust (Newton's third law). The systems differ in how energetically they can expel that mass, and this determines Isp (efficiency) and thrust (force). There is always a fundamental tradeoff: high Isp (efficiency) comes with low thrust, and vice versa.

<!-- @editor[diagram/P2]: Diagram is a comparison table, not a landscape diagram showing how propulsion types relate to mission phases and spacecraft subsystems — rework as a spectrum or decision tree showing the Isp-vs-thrust tradeoff space with mission regimes overlaid -->
```
+------------------------------------------------------------------+
|                    PROPULSION SPECTRUM                            |
+------------------------------------------------------------------+
|                                                                  |
|  TYPE              Isp (s)   THRUST       APPLICATION            |
|  ----              -------   ------       -----------            |
|  Solid chemical    230-300   High         Strap-ons, SRBs        |
|  Liquid bipropell. 300-460   High         Main engines, upper st.|
|  Liquid monoprop.  150-230   Medium       Attitude control       |
|  Hybrid            280-350   Medium       Suborbital (SpaceShip)|
|  Cold gas          50-70     Very low     Cubesat attitude ctrl  |
|  ---------------------------------------------------             |
|  Electric (ion)    1500-3000 Very low     Deep space science     |
|  Electric (Hall)   1000-3000 Very low     GEO station-keeping    |
|  Electric (gridded) 3000-10000 Ultra-low  Deep space/large sat  |
|  ---------------------------------------------------             |
|  Nuclear thermal   800-1000  Medium       Future deep space      |
|  Nuclear electric  3000-10000 Low         Future outer planets   |
|  Solar sail        ∞         Ultra-low    Photon pressure        |
+------------------------------------------------------------------+
```

---

## Fundamentals: Thrust and Isp

```
ROCKET PROPULSION FUNDAMENTALS
================================

  THRUST (F):
    F = ṁ × v_e + (P_e - P_amb) × A_e
    where:
    ṁ   = mass flow rate (kg/s)
    v_e  = exhaust velocity (m/s)
    P_e  = exit pressure (Pa)
    P_amb = ambient pressure (Pa)
    A_e  = nozzle exit area (m²)
    Second term = pressure thrust (usually smaller)

  SPECIFIC IMPULSE (Isp):
    Isp = F / (ṁ × g₀)  [in seconds]
       = v_e / g₀
    The units "seconds" are a historical artifact — it was thrust per weight flow
    Physical meaning: engine efficiency (how much thrust per unit propellant weight)
    Higher Isp → less propellant for same Δv (Tsiolkovsky equation)

  THRUST-TO-WEIGHT RATIO (TWR):
    TWR = F / (m × g)
    TWR > 1 needed for liftoff from a planetary surface
    SpaceX Merlin (sea level): TWR ≈ 180 (per engine)
    Saturn V F-1: TWR ≈ 83
    Ion engine: TWR ≈ 0.0001 (cannot lift itself!)

  THE FUNDAMENTAL TRADEOFF:
    Chemical: high energy density → high thrust → low Isp
    Ion: low energy density (just electrical) → low thrust → high Isp
    Nuclear thermal: reactor heat → higher Isp than chemical + useful thrust
```

---

## Chemical Propulsion: Liquid

```
LIQUID PROPELLANT ENGINES
==========================

  TYPES OF LIQUID PROPELLANT COMBINATIONS:
  LOX/RP-1 (kerosene): Isp ~ 311-360 s
    Earth-storable; high density (good for first stages)
    SpaceX Merlin: 311 s vac; Falcon 9 first stage
    Turbopump-fed; high chamber pressure possible
    Combustion: 2C₁₂H₂₃ + 37O₂ → 24CO₂ + 23H₂O
    (simplified; kerosene is a complex mixture)

  LOX/LH₂ (liquid hydrogen): Isp ~ 420-460 s
    Highest Isp of chemical; very low density (large tanks)
    RL-10 (Centaur): 444-465 s; most efficient US engine
    RS-25 (Space Shuttle Main Engine): 452 s (vac)
    Cryogenic: LOX = -183°C; LH₂ = -253°C
    Storage challenge: boil-off; cryogenic insulation

  LOX/CH₄ (methane): Isp ~ 355-382 s
    Intermediate: between RP-1 and LH₂ efficiency
    Denser than LH₂; cleaner than RP-1 (no coking)
    SpaceX Raptor: ~380 s vac; 3300 psi chamber pressure (record 2022)
    Advantage: producible on Mars from CO₂ + H₂O → ISRU
    Future standard for Mars-capable engines

  NTO/UDMH (storable hypergolic): Isp ~ 310-315 s
    Self-igniting (hypergolic); storable at room temperature
    Shuttle OMS, Soyuz second stage, most spacecraft thrusters
    Toxic; corrosive; careful handling required
    Used for spacecraft where reliability > performance

  MONOPROPELLANT (hydrazine): Isp ~ 220-230 s
    Single propellant; catalytic decomposition (no oxidizer)
    Simple, reliable; standard for attitude control thrusters
    Electrolytic hydrazine: MR-103, MONARC
    "Green" alternatives: AF-M315E, LMP-103S (higher Isp ~250 s)
```

### Engine Cycle Architecture

```
ENGINE CYCLES
=============

  GAS GENERATOR (GG) CYCLE:
    Small amount of propellant burned in gas generator
    Hot gas drives turbopump → powers main propellant pumps
    Turbine exhaust: dumped overboard (wasted!)
    Isp penalty: ~1-3% loss; simple; reliable
    Used: SpaceX Merlin (Falcon 9), F-1 (Saturn V), RL-10A

  STAGED COMBUSTION (SC) CYCLE:
    ALL propellant passes through turbopump
    Oxidizer-rich (ORSC) or fuel-rich (FRSC) preburner
    Full combustion in main chamber = no exhaust dump
    Higher chamber pressure → higher Isp; more complex
    ORSC: RD-170/180/191 (Russian); extremely high performance
    FRSC: RS-25 (SSME); SpaceX Raptor
    Raptor: full-flow SC (both propellants fully preburned)

  EXPANDER CYCLE:
    Propellant heated by chamber/nozzle cooling channels
    → Vapor drives turbopump → no separate combustion
    Clean; no gas generator; limited power → small engines
    Used: RL-10 (Centaur upper stage); LE-5 (Japan H-II)

  PRESSURE-FED:
    Tank pressure pushes propellant directly to injector
    No turbopump; simple; low chamber pressure; lower Isp
    Used: small spacecraft engines, most attitude control
```

---

## Chemical Propulsion: Solid

```
SOLID ROCKET MOTORS (SRMs)
============================

  OPERATION:
    Propellant premixed in solid form; ignited; burns until exhausted
    No turbopumps; no propellant valves; very simple
    Cannot be throttled or shut down (usually)

  PROPELLANT COMPOSITION:
    Ammonium perchlorate composite propellant (APCP): most common
    NH₄ClO₄ (oxidizer, ~70%) + Al powder (fuel, ~15%) + HTPB binder
    Isp: ~250-270 s (lower than liquid)
    Very high thrust: SRBs for Shuttle = 14.7 MN each!

  STRUCTURE:
    "Grain": cast propellant cylinder with internal void (core)
    Core shape determines burn rate and thrust profile
    Star, wagon wheel, etc. = tailored thrust vs time

  APPLICATIONS:
    First stage strap-ons: Shuttle SRBs, Delta IV, Atlas V
    Upper stages: Castor 30, STAR series (Star 48 for planetary)
    ICBM warheads: Minuteman; Trident D5
    Solid kick stages: moving from transfer orbit to final orbit

  ADVANTAGES/DISADVANTAGES:
    + Simple; reliable; storable; no cryogenics; very high thrust
    - Cannot throttle; lower Isp; cannot restart
    - Toxic exhaust (HCl from ammonium perchlorate)
    - Once ignited, cannot stop (safety concern for crewed vehicles)
```

---

## Electric Propulsion

```
ELECTRIC PROPULSION SYSTEMS
=============================

  COMMON PRINCIPLE: Electrically accelerate ions or ionized gas
  Power source: Solar panels (near Sun) or RTG/nuclear (deep space)

  ION THRUSTER (gridded ion engine):
    Ionize propellant (Xenon, Krypton) with electron bombardment
    Accelerate ions through electric field between grids
    Isp: 3000-12,000 s
    Thrust: 0.05-0.3 N per thruster (millinewtons to a fraction of a Newton)
    Examples: Dawn spacecraft (3 ion engines), Deep Space 1, Hayabusa
    Used for: science missions with large Δv; no time pressure

  HALL EFFECT THRUSTER:
    Magnetic field traps electrons → ionize propellant
    Electric field accelerates ions; electrons provide neutralization
    Isp: 1000-3000 s; Thrust: 0.05-0.5 N
    Examples: Starlink satellites (krypton Hall), GEO station-keeping
    Most commercially widespread electric propulsion type
    Higher thrust than gridded ion; simpler; slightly lower Isp

  RESISTOJET/ARCJET:
    Heat propellant electrically (resistojet: element; arcjet: arc discharge)
    Isp: 150-600 s; low power; low thrust
    Used: attitude control, small maneuvers

  ELECTROSPRAY / FEEP:
    Field Emission Electric Propulsion: liquid metal/ionic liquid emitter
    Isp: 2000-8000 s; thrust: micronewtons
    Used: drag-free CubeSats, LISA Pathfinder, precision pointing

  POWER vs THRUST:
    Electric propulsion requires power: P = F × v_e / (2η)
    Isp = 3000 s, η = 65%, F = 0.1 N → P = 1.4 kW
    At 1 AU: solar panel = ~1 kW/m² (before losses)
    Deep space: solar panels impractical → nuclear needed
```

---

## Nuclear Propulsion

```
NUCLEAR THERMAL PROPULSION (NTP)
==================================

  PRINCIPLE:
    Nuclear fission heats propellant (hydrogen) in reactor
    Hydrogen expelled through nozzle
    Isp: ~800-1000 s (2-3× chemical for same thrust)
    Thrust: 25-100+ kN (useful for Mars missions)

  WHY HYDROGEN:
    Lowest molecular weight → highest exhaust velocity
    v_e ∝ √(T/M) → minimize M → maximize v_e
    Hydrogen: M = 2 → Isp ≈ 2× with same T as kerosene

  NERVA PROGRAM (1955-1972):
    US nuclear rocket program; 20 test firings
    Phoebus 2A (1968): 1.1 GW, 867 kN thrust, Isp = 825 s
    Cancelled 1972 when Mars mission cancelled
    Required safety certification before flight (never achieved)

  MODERN NTP:
    Ultra Safe Nuclear Corporation (USNC); BWX Technologies
    NASA Demonstration Rocket for Agile Cislunar Operations (DRACO): 2027?
    Bimodal NTP: reactor provides both thrust AND electrical power

  NUCLEAR ELECTRIC PROPULSION (NEP):
    Reactor provides power for electric thrusters (ion/Hall)
    Isp: 5000-10,000 s; thrust: low; power: high (100 kW+)
    Mars manned mission concept: VASIMR (Variable Specific Impulse Magneto-plasma Rocket)
    VASIMR: Isp 3000-30,000 s (variable); 200 kW power
    Claims 39-day Mars trip (vs 7-9 months chemical) with 200 MW reactor
    No flight hardware yet; significant engineering challenges

  SAFETY CONSTRAINTS:
    Cannot test fire in atmosphere (radiation + debris)
    Must not accidentally reach criticality during launch
    Requires shielding (adds mass)
    Political/public acceptance challenge
```

---

## Solar Sails and Photonic Propulsion

```
SOLAR SAIL
===========

  PRINCIPLE:
    Solar photons carry momentum: p = E/c = hν/c
    Reflecting photons → 2× momentum transfer
    Pressure at 1 AU: ~9 μN/m²

  ACCELERATION:
    a = 2 × P_solar × A × (1 + reflectivity) / m
    For 1 kg sail, 10 m × 10 m, reflectivity 0.9:
    a ≈ 2 × 9μN/m² × 100 m² × 1.9 / 1 kg ≈ 3.4 mm/s²
    → Tiny but continuous → can build up significant Δv over months/years

  IKAROS (JAXA, 2010): first demonstrated solar sail in deep space
  LightSail 2 (Planetary Society, 2019): raised orbit using photons
  NEA Scout (NASA, 2022): CubeSat solar sail to near-Earth asteroid (lost contact)

  BEAM PROPULSION:
    Laser from Earth pushes a reflective sail
    Starshot concept: 100 GW laser array → 0.2c velocity → Alpha Centauri in 20 yr
    Engineering: mirror must be ~1 g; laser coherence over 10,000 km aperture
    Power requirement enormous; still theoretical

  MAGNETOSAIL / M2P2:
    Magnetic field inflated by plasma → sweeps solar wind
    Larger effective area than physical sail
    Theoretical; no flight demonstration
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is Isp? | Specific impulse; thrust per unit propellant weight flow rate; in seconds; proportional to exhaust velocity; the efficiency metric for rockets |
| Why does hydrogen give the best chemical Isp? | Lowest molecular weight → highest exhaust velocity per unit thermal energy (v_e ∝ √(T/M)); Isp ≈ 450 s vs ~310 s for kerosene-LOX |
| Why doesn't everyone use electric propulsion? | Ultra-low thrust: an ion engine that could go to Mars in months would need megawatts of power; solar panels near Earth can supply only ~kW. Electric propulsion is great for slow orbit-raising and station-keeping; not useful for rapid orbit insertion. |
| What is the Raptor's key achievement? | Full-flow staged combustion (both fuel and oxidizer fully preburned before main chamber); very high chamber pressure (~3300 psi); high Isp; methane = ISRU-compatible with Mars |
| What are storable propellants and why use them? | Propellants that are liquid at room temperature (NTO/UDMH, hydrazine); can be stored in tanks indefinitely; critical for spacecraft thrusters that need to fire months/years after launch; lower Isp than cryogenics but much simpler |
| Why was NERVA cancelled? | Nixon cancelled the post-Apollo Mars mission program in 1972; no mission → no need for nuclear rocket; safety certification and public concerns also factors |

---

<!-- @editor[bridge/P2]: No old-world bridge — natural parallel: the Isp-vs-thrust tradeoff is the same pattern as latency-vs-throughput in systems design (the learner built Azure pipelines); high-Isp/low-thrust is like batch processing (high throughput, high latency), chemical is like low-latency real-time -->
## Common Confusion Points

**Isp in seconds is not "how long the engine runs"**: Isp = thrust / (mass flow rate × g₀) = specific impulse. It was originally defined as thrust per unit weight of propellant per second. "450 seconds" doesn't mean 450 seconds of burn time; it means the engine produces 1 lb of thrust per lb/s of propellant consumed (old units). In modern understanding: higher Isp = exhaust moving faster = more momentum per kg of propellant.

**Electric propulsion is not faster**: Ion drives have Isp 10× higher than chemical — but thrust is 1/10,000th. Getting to Mars with an ion drive takes longer (years) but uses far less propellant. The trip is slower, not faster. The tradeoff is time vs propellant mass.

**Vacuum Isp vs sea-level Isp**: Isp is higher in vacuum because there's no ambient pressure pushing against the nozzle exit (the pressure thrust term (P_e - P_amb) × A_e is positive in vacuum, zero at vacuum design pressure, negative at sea level). RS-25 sea level: 366 s; vacuum: 452 s. Always check which condition when comparing engines.

**Hybrid rockets are not "the best of both worlds"**: They have advantages (throttleable, safer than solid, storable) but practical Isp is usually lower than bipropellant liquid, and regression rate control is difficult. SpaceShipOne/Two used nitrous oxide + rubber. They're commercially viable for suborbital but haven't reached orbital.
