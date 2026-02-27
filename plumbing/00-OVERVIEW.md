# Plumbing Systems — Overview

## The Big Picture: Three Separate Trees

Residential plumbing is three independent pipe systems sharing the same walls:

```
+------------------------------------------------------------------+
|                    PLUMBING SYSTEM OVERVIEW                       |
+------------------------------------------------------------------+
|                                                                  |
|  SUPPLY SYSTEM              DWV SYSTEM           GAS SYSTEM      |
|  =============              ==========           ==========      |
|  Pressurized                Gravity-driven       Pressurized     |
|  40–80 PSI                  1/4" per foot slope  0.25–2 PSI      |
|                                                                   |
|  Municipal main             Fixtures drain        Gas meter       |
|      ↓                          ↓                    ↓           |
|  PRV (if needed)            Drain branches       Regulator       |
|      ↓                          ↓                    ↓           |
|  Water meter                P-trap (water seal)  Distribution    |
|      ↓                          ↓                    ↓           |
|  Cold main                  Horizontal drain     Branch lines    |
|      ↓         ↓            (1/4"/ft slope)          ↓           |
|  Cold       Hot water       Vertical stack       Appliances      |
|  fixtures   heater (120°F)      ↓               (furnace/range)  |
|                             Building drain                        |
|                                 ↓                                |
|                             Sewer/septic                         |
|                                                                  |
|  VENT STACK (extends above roof — part of DWV)                   |
|  Maintains atmospheric pressure; prevents trap siphon            |
+------------------------------------------------------------------+
```

**Key principle**: Supply is pressure-driven (municipal pump). DWV is gravity-driven (1/4" per foot minimum slope). They never interconnect — that's a cross-connection, a health code violation, and a public health hazard.
**Hydraulic engineering framing**: Supply is a pressurized pipe network governed by Darcy-Weisbach (ΔP = f(L/D)(ρv²/2) — pressure drop proportional to Q²). PRVs are pressure regulators (voltage regulator analog). Pump curves (head vs. flow) intersect system curves (required head vs. flow) to determine the operating point. DWV is open-channel gravity flow governed by Manning's equation for partially-filled pipes, designed for self-scouring velocity (>2 fps). Code sizing tables are precomputed solutions to these underlying physics equations.


---

## Pressure vs. Gravity: The Fundamental Divide

```
SUPPLY SYSTEM                    DWV SYSTEM
=============                    ==========

Energy source: municipal         Energy source: gravity
pressure (~60 PSI typical)

Pipe direction: any              Pipe direction: must slope downhill
                                 (1/4" per foot horizontal minimum)
                                 or vertical (stacks)

Failure mode: pressurized        Failure mode: backup (blocked by
leak — active, immediate         solids, incorrectly sloped, no vent)

Pipe sizing: velocity and        Pipe sizing: drainage fixture units
pressure drop calculation        (DFU) — flow by volume

Minimum pipe: 1/2" branch,      Minimum: 1-1/4" trap arm, 3" building
3/4" main (residential)         drain (residential typical)

Joints: watertight under         Joints: watertight, correct slope,
pressure (tested at 100 PSI)     correct direction (hub faces upstream)
```

---

## The Vent System: Why Drains Need Air

This is the most counterintuitive piece for people new to plumbing:

```
WHAT HAPPENS WITHOUT VENTING:
  Water rushing down drain creates low pressure behind it
                      ↓
  Low pressure siphons water out of nearby P-traps
                      ↓
  P-trap loses its water seal
                      ↓
  Sewer gas (H₂S, methane, CO₂) enters building
                      ↓
  Smell, health hazard, potential explosion risk

WHAT THE VENT STACK DOES:
  Open pipe from drain system to atmosphere (above roofline)
                      ↓
  Air enters at top, maintains atmospheric pressure in drain pipes
                      ↓
  Drains flow freely without siphoning nearby traps
                      ↓
  Trap seals maintained — sewer gas excluded

  THE VENT IS NOT VISIBLE IN THE FINISHED BUILDING
  but it is just as essential as the drain pipe itself
```

---

## The Code Framework

```
GOVERNING CODES
┌────────────────────────────────────────────────────────────┐
│  IRC — International Residential Code                      │
│  Chapters 25-32: plumbing for 1-2 family dwellings        │
│  Published by ICC (International Code Council)            │
├────────────────────────────────────────────────────────────┤
│  IPC — International Plumbing Code                        │
│  Commercial/multi-family, more comprehensive              │
│  Published by ICC                                         │
├────────────────────────────────────────────────────────────┤
│  UPC — Uniform Plumbing Code                              │
│  Western states: CA, WA, OR, AZ, HI                      │
│  Published by IAPMO                                       │
├────────────────────────────────────────────────────────────┤
│  LOCAL AMENDMENTS — ALWAYS WIN                            │
│  AHJ = Authority Having Jurisdiction = local building dept│
│  Some localities prohibit PEX-b or push-fit fittings     │
│  Always check before buying materials                     │
└────────────────────────────────────────────────────────────┘

INSPECTION SEQUENCE:
  1. Pull permit (required for most work beyond minor repairs)
  2. Rough-in inspection — before walls are closed
     Inspector checks: pipe material, slope, trap, vent connections
  3. Pressure test (supply): pressurize to 100 PSI, hold 15 min
  4. Final inspection — after fixtures installed
     Inspector checks: proper fixture installation, water flow,
     hot/cold orientation, anti-scald valves
```

---

## Pipe Material Quick Reference

```
APPLICATION          MATERIAL            REASON
-----------          --------            ------
Supply — hot/cold    PEX-a               Flexible, freeze-resistant,
(new residential)                        expansion fitting = strongest joint

Supply — hot/cold    Copper (Type L)     Proven 60+ yr lifespan,
(traditional)                            soldered joints, antimicrobial

Supply — cold only   PVC Sch 40          Cheapest — NOT for hot water
                                         (softens at 140°F)

Supply — hot/cold    CPVC               Chlorinated PVC, rated to 200°F
(retrofit)                               solvent-welded

Drain/waste/vent     ABS or PVC          Lightweight, chemical-resistant,
(residential)                            easy solvent weld

Drain — commercial   Cast iron           Sound damping (apartments/hotels)
or sound-critical

Gas lines            Black iron          Traditional, code-accepted
                     or CSST             CSST = faster install, requires bonding

Legacy (remove)      Galvanized steel    Corrodes internally, restricts flow
                                         DO NOT use for new work
```

---

## Module Map

| Module | Topic | Key Concept |
|--------|-------|-------------|
| 01 | History | Roman lead → copper → PEX, 4,000 years |
| 02 | Pipe Materials | K/L/M copper, PEX a/b/c, PVC/CPVC, cast iron |
| 03 | Fittings & Joints | 8 joint types from solder to push-fit |
| 04 | Supply Systems | PRV, water heaters, anti-scald, water hammer |
| 05 | Drain-Waste-Vent | Gravity, traps, venting, cleanouts |
| 06 | Fixtures | Toilets, faucets, shower valves |
| 07 | Water Quality | Hardness, softeners, filtration, RO |
| 08 | Specialty | Gas, hydronic, radiant floor, fire suppression |
| 09 | Codes & Standards | IRC/IPC/UPC, permit process, sizing tables |

---

## Decision Cheat Sheet

| I need to... | See |
|---|---|
| Understand supply vs drain systems | This overview |
| Choose pipe material for new construction | 02 |
| Connect pipes without soldering | 03 (push-fit) |
| Size a water heater | 04 |
| Diagnose sewer smell | 05 (trap siphon/dry trap) |
| Fix a running toilet | 06 |
| Address hard water | 07 |
| Add gas to an appliance | 08 |
| Know what needs a permit | 09 |

---

## Common Confusion Points

**DWV ≠ supply**: Physically separate systems. "Drain" and "vent" are part of the same DWV pipe system — both non-pressurized, both gravity/atmosphere-driven.

**The vent stack carries air, not water**: It doesn't drain anything — it maintains atmospheric pressure so drains flow freely. Blocked vents cause gurgling, slow drainage, and sewer odors.

**P-trap is a gas seal, not a flow restrictor**: The water in the P-trap's curve is a gas barrier. An unused sink with a dried-out trap smells like sewer because the barrier is gone.

**PRV location**: Pressure-reducing valve is on the supply main entering the house, right after the meter. If pipes hammer, showers pulsate, or appliances fail early from overpressure — check PRV first.

**Copper vs PEX**: Both are correct. Copper costs more, lasts longer in aggressive water, and is antimicrobial. PEX installs faster, handles freezing better (expands ~8% vs copper bursting), and is quieter. Most new residential construction uses PEX.
