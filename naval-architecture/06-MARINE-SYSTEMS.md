---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:marine-systems
kind: guide
module: naval-architecture
section: naval-architecture
title: Marine Systems
status: source-custody
source_custody: partial
current_path: naval-architecture/06-MARINE-SYSTEMS.md
canonical_path: naval-architecture/06-MARINE-SYSTEMS.md
backsource_ids: [proof-backfill:naval-architecture:06-marine-systems, git-history:naval-architecture:06-marine-systems]
concepts: [marine systems, ship electrical, steering, ballast, HVAC, auxiliaries]
root_concepts: [marine systems]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Marine Systems

## The Big Picture

A ship is a self-contained floating city that must make its own power, water, and air,
move its rudder, trim its tanks, fight its fires, and treat its waste — for weeks, with no
shore connection and no outside help. Marine engineering is the discipline of those
shipboard systems: everything that keeps the ship *running* as opposed to the hull that
keeps it *floating*. The unifying theme is **redundancy under autonomy** — at sea there is
no second power grid to fail over to, so the ship carries its own.

```
THE SHIP AS A SELF-CONTAINED UTILITY (every utility a city has, onboard)
===============================================================================

   +---------------------------------------------------------------------+
   | PRIME POWER: main engine(s) + generators  ->  the source of all     |
   +---------------------------------------------------------------------+
        |            |             |            |            |
        v            v             v            v            v
   .---------. .-----------. .-----------. .---------. .-------------.
   |PROPULS- | |ELECTRICAL | | STEERING  | | FLUID   | | HABITABIL-  |
   |ION TRAIN| |GENERATION | | & MANEUV. | | SYSTEMS | | ITY (HVAC,  |
   |shaft,   | |& DISTRIB. | | rudder,   | |ballast, | | fresh water,|
   |gearbox  | |gensets,   | | thrusters,| |bilge,   | | sewage,     |
   |[guide03]| |switchboard| | steering  | |fuel,    | | refrigera-  |
   |         | |MSB, loads | | gear      | |cooling  | | tion)       |
   '---------' '-----------' '-----------' '---------' '-------------'
        |            |             |            |            |
        +------------+-------------+------------+------------+
                              |
                     SAFETY SYSTEMS overlay everything:
                     fire main, CO2/water mist, lifeboats, bilge alarms,
                     emergency generator + emergency switchboard (own fuel)
```

Read it as: one power source feeds five utility families, with a safety layer cross-cutting
all of them. The naval architect sizes spaces and weights for these; the marine engineer
designs and runs them.

---

## Layer 1: Shipboard Electrical Power

A ship runs an isolated electrical grid — its own generation, distribution, and protection,
with no infinite bus behind it. Power comes from **diesel generators** (gensets), a
**shaft generator** off the main engine, and increasingly batteries; in diesel-electric
ships (guide [03]) the *same* generators feed both propulsion and the ship.

```
SHIPBOARD ELECTRICAL ARCHITECTURE (an islanded microgrid)
===============================================================================

   GEN 1   GEN 2   GEN 3   SHAFT GEN        EMERGENCY GEN (own fuel + start)
     |       |       |        |                       |
     +-------+-------+--------+                        |
                     |                                 |
            .========================.        .================.
            |   MAIN SWITCHBOARD     |        | EMERGENCY      |
            |   (MSB) - the "bus"    |--tie-->| SWITCHBOARD    |
            '========================'        '================'
              |       |       |                   |        |
              v       v       v                   v        v
          propulsion  hotel   deck            steering   nav/comms
          (if D-E)    load    machinery       gear       emergency lighting

   POWER MANAGEMENT SYSTEM (PMS) decides which gensets run, load-shares
   them, sheds non-essential load on a fault, and starts a standby genset
   before the bus collapses. A real-time control problem.
```

Distinctive features of a marine grid:

| Feature | Why |
|---------|-----|
| Islanded (no shore grid) | At sea you ARE the grid; frequency/voltage are yours to hold |
| N+1 generator redundancy | Lose one genset and still meet the load |
| IT earthing (isolated neutral) | First ground fault does not trip the ship dark — a wet, vibrating environment will have ground faults; the ship keeps running and alarms instead |
| Emergency switchboard | Separate board, separate genset, own fuel, autostarts on blackout |
| Power Management System (PMS) | Automated load-sharing, load-shedding, blackout recovery |

> Old world -> new world bridge. A ship's electrical plant is an **islanded microgrid with
> automated failover** — N+1 generation, a power-management controller that does load
> shedding and auto-restart, and a segregated emergency bus. The design goals are exactly a
> data center's: hold the bus through any single failure, shed non-critical load gracefully,
> and recover from a blackout automatically. The marine version simply cannot call the
> utility — there is no utility — so the redundancy is hard requirement, not best practice.

The **isolated (IT) earthing** point is worth dwelling on: unlike a shore building that
trips on first ground fault, a ship is deliberately wired so the first earth fault does *not*
open the breaker. The ship raises an alarm and keeps steaming; you do not want a single damp
cable to black out a vessel in a storm. Two faults are needed to trip — defense in depth for
an environment where one fault is inevitable.

---

## Layer 2: Steering and Maneuvering

The ship must change and hold heading. The **rudder** is a control surface in the propeller
race; turning it generates a side force that yaws the hull. Below a certain speed the rudder
is useless (no flow), so low-speed maneuvering uses **thrusters**.

```
HOW A RUDDER TURNS A SHIP (a wing in the propeller race)
===============================================================================

   propeller wash -->  ====>  ___
                              /   \  rudder angled
                       ====> |     | -> generates SIDE force (lift)
                              \___/      |
                                         v
   side force aft -> yawing moment about the ship's pivot point
   -> bow swings the OTHER way -> ship turns.

   The rudder works on the FAST propeller race, so it bites even at
   modest ship speed -- but at near-zero speed there is no flow over it
   and it stalls. That is why docking uses thrusters, not the rudder.
```

The maneuvering toolkit, from open-sea course-keeping to millimetre docking:

| Device | Speed regime | Role |
|--------|--------------|------|
| Rudder + steering gear | Steerageway and above | Primary heading control |
| Bow / stern thrusters | Low speed / docking | Sideways translation, turning in place |
| Azimuth pods (guide [03]) | All | Vector thrust any direction; no rudder needed |
| Dynamic positioning (DP) | Station-keeping | Computer holds position against wind/current |

**Steering gear** is the hydraulic (or electric) machine that swings the rudder; SOLAS
requires it to be *duplicated* — two independent power units — because loss of steering in a
seaway is loss of the ship. **Dynamic positioning** deserves its own note: a DP vessel holds
a fixed position and heading with no anchor, using a Kalman-filtered position estimate
(GPS + gyro + reference systems) feeding a controller that allocates thrust across multiple
thrusters and pods. It is a multivariable feedback control system — bridge to
`control-theory/` — and it is what lets a drillship sit over a wellhead in 2000 m of water
or a cruise ship hold station off a tender port.

> Old world -> new world bridge. Dynamic positioning is a classic estimator-plus-controller
> stack: sensor fusion (Kalman filter over GPS/gyro/hydroacoustic references) produces a
> state estimate, a controller computes the required net force and moment, and a thrust-
> allocation layer distributes that demand across redundant actuators — with graceful
> degradation when a thruster fails (DP2/DP3 redundancy classes). It is the same
> sense-estimate-actuate loop, with the sea as the disturbance. See `control-theory/`.

---

## Layer 3: Ballast, Bilge, and Tank Systems

The ship constantly manages water and fluids in its tanks: **ballast** to control draft,
trim, heel, and stability; **bilge** to remove water that leaks into spaces; **fuel and
fresh-water** transfer to feed the plant and keep the ship in trim as tanks empty.

```
THE FLUID SYSTEMS (a network of tanks, pumps, and valves)
===============================================================================

   BALLAST: pump seawater IN/OUT of ballast tanks to:
     - adjust draft (empty ship rides high -> add ballast for propeller
       immersion and seakeeping)
     - correct trim and heel (move ballast fore/aft, port/stbd)
     - maintain stability and limit hull-girder bending (link to [01],[04])

        +----+----+----+----+   double-bottom + wing ballast tanks
        | WB | WB | WB | WB |   pumped via a ballast main + valves
        +----+----+----+----+

   BILGE: remove unwanted water (leaks, condensation, washdown) from the
   bottom of machinery and cargo spaces. Bilge wells -> bilge pumps ->
   overboard (through an OILY-WATER SEPARATOR, by law, if any oil present).

   FUEL: settling tank -> purifier (centrifuge) -> service tank -> engine.
   Heavy fuel oil must be HEATED to flow and centrifuged to remove water
   and sludge before it can be burned.
```

Two systems carry heavy regulatory weight:

- **Ballast water treatment.** Ballast taken on in one port and dumped in another moves
  invasive species worldwide (zebra mussels, etc.). The IMO Ballast Water Management
  Convention now requires onboard *treatment* (UV or electro-chlorination) before
  discharge. A pure ecology problem (bridge to `ecology/`) that became a mandatory ship
  system.
- **Oily-water separator + oil record book.** Discharging oily bilge water is illegal
  (MARPOL). Every ship has an oily-water separator and a tamper-logged record book; the
  "magic pipe" (an illegal bypass) is one of the most-prosecuted marine crimes.

The link back to stability is direct: ballast operations change the loading condition, so
they feed straight into the GM and bending-moment checks of [01] and [04]. The loading
computer treats ballast as a control input for trim, heel, and hull stress.

---

## Layer 4: Habitability — Air, Water, Climate

The ship must keep its crew (and on passenger ships, thousands of guests) alive and
comfortable: breathable conditioned air, fresh water, refrigeration, and sewage treatment.

```
THE LIFE-SUPPORT SYSTEMS
===============================================================================

   HVAC: ventilate, heat, cool, dehumidify. Marine twists:
     - SALT AIR is corrosive -> filtration and corrosion-resistant coils
     - machinery spaces need huge ventilation (engine combustion air +
       heat rejection) -> big intake/exhaust trunks
     - fire dampers in every duct (a duct is a fire highway)
     - on cruise ships, HVAC is a major share of the hotel electrical load

   FRESH WATER: a ship MAKES its own water from the sea:
     - evaporators (use waste engine heat to distill) -- classic, cheap heat
     - reverse osmosis (RO) -- membranes, electrically driven, now common
     -> potable water for crew/guests + technical water for the plant

   REFRIGERATION: provisions stores + (on reefer ships) the cargo itself.

   SEWAGE: marine sanitation device (MSD) -- biological/chemical treatment
     before discharge; black water and grey water handled per MARPOL Annex IV.
```

Fresh-water generation is a small triumph of energy integration: the classic **evaporator**
distills seawater using *waste heat* from the engine jacket cooling water — the engine has
to reject that heat anyway, so the fresh water is nearly free. Where waste heat is scarce or
demand is high (cruise ships), **reverse osmosis** dominates, trading electrical energy for
independence from engine load. (The desalination physics — osmotic pressure, membrane flux —
lives in `chemical-eng/`; here it is a sized shipboard plant.)

---

## Layer 5: Safety Systems

Some shipboard systems exist only for the bad day. They are mandated by SOLAS and are
cross-cutting — they overlay propulsion, electrical, and structure.

```
THE SAFETY OVERLAY
===============================================================================

  FIRE:    detection (smoke/heat sensors) + fire main (seawater, always
           pressurized) + fixed systems:
             - CO2 flooding or water-mist for machinery spaces
             - sprinklers for accommodation
             - inert gas (IG) for tanker cargo tanks (no oxygen -> no fire)
           + structural fire protection: A/B/C-class boundaries that hold
             back fire for a rated time (A-60 = 60 min insulation).

  FLOODING: bilge alarms, watertight doors (remote-closable), the damage
            stability of [01] as the last line.

  ABANDON: lifeboats (often free-fall on cargo ships), liferafts, immersion
           suits, EPIRBs, the GMDSS distress radio system.

  POWER:   emergency generator + emergency switchboard (own fuel, autostart)
           keeps steering, navigation lights, comms, and lighting alive
           through a main-plant blackout.
```

The **inert gas system** on tankers is the elegant one: rather than fight fire in a cargo
tank, you ensure it can never start by filling the ullage space (above the oil) with
oxygen-depleted flue gas — below ~8% oxygen, hydrocarbons cannot ignite. It is fire
prevention by removing one leg of the fire triangle, the same principle as a controlled
atmosphere store. **Structural fire protection** (A/B/C-class divisions, "A-60" = a steel
boundary insulated to hold the far side below a limit for 60 minutes) is a structures-meets-
safety topic that sizes insulation and bulkhead arrangement throughout the ship.

---

## Worked Example: Sizing the Electrical Plant and a Blackout Recovery

A mid-size vessel. Size the generators and trace what happens in a blackout.

```
   GIVEN electrical demand (the "electrical load analysis"):
     Hotel/accommodation load        ........  900 kW
     Deck & machinery auxiliaries    ........  700 kW
     HVAC                            ........  600 kW
     Bow thruster (intermittent)     ........ 1200 kW (only at maneuvering)
     Sea-going steady load (no thruster) ~ 2200 kW

   STEP 1 -- pick genset size with N+1 redundancy:
     Use 3 x 1100 kW gensets. At sea, 2 running carry 2200 kW; 1 is standby.
     -> any one genset can fail and the ship still meets sea load. N+1. OK.

   STEP 2 -- maneuvering peak (thruster online):
     2200 + 1200 = 3400 kW. Run all 3 gensets (3300 kW) PLUS shed the bow
     thruster's full draw via soft-start/limit, or run a 4th set in port.
     The PMS auto-starts the standby set before the thruster is engaged.

   STEP 3 -- a generator trips at sea (the bad moment):
     bus frequency starts to droop as the surviving sets overload ->
       a) PMS sheds non-essential load (some HVAC, deck machinery) in ms
       b) PMS signals the standby genset to autostart and synchronize
       c) frequency recovers; shed loads restored. Ship never went dark.

   STEP 4 -- total blackout (all main gensets lost):
     emergency generator autostarts (within ~45 s per SOLAS), emergency
     switchboard energizes: STEERING GEAR, nav lights, GMDSS radio,
     emergency lighting, fire pump. The ship can steer and call for help
     while the engineers restore the main plant (a "dead-ship start"
     using emergency power + air bottles to relight the main engine).
```

The recovery sequence is pure fault-tolerant-systems design: detect the loss, shed
gracefully, fail over to a standby resource automatically, and keep the safety-critical
subset alive on a segregated emergency supply. The marine constraint is that there is no
external grid and no on-call utility crew — the ship must do all of it itself, automatically,
in the worst weather.

---

## Common Confusion Points

### A ground fault does not (immediately) trip a ship

Shore buildings trip on first earth fault; ships use **isolated (IT) earthing** so the first
ground fault only raises an alarm. A ship is wet and vibrating — ground faults are routine —
and blacking out at sea is far more dangerous than running with one fault while engineers
locate it. Two faults are needed to cause a trip.

### Ballast is a control input, not just "dead weight"

Ballast water is actively pumped to set draft, correct trim and heel, immerse the propeller,
and limit hull-girder bending. It links straight to the stability [01] and structure [04]
calculations. An empty ship is *less* safe in some respects — too high out of the water — so
it ballasts down deliberately.

### A ship makes its own fresh water

Ships do not carry weeks of drinking water; they distill it (evaporators, using waste engine
heat) or reverse-osmosis it from the sea. Running out of bunkered water is not normally the
constraint — running out of the *energy* or membranes to make it is.

### Emergency power is a separate, segregated system

The emergency generator, its switchboard, its fuel, and its cabling are deliberately
independent of the main plant and located above the bulkhead deck — so a flood or fire that
kills the main plant cannot kill emergency power too. It is physical, not just logical,
segregation.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Power the ship | Diesel gensets + shaft gen; N+1 redundancy |
| Decide which gensets run | Power Management System (load-share/shed) |
| Avoid blacking out on a ground fault | Isolated (IT) earthing + alarm |
| Keep steering alive in a blackout | Emergency genset + emergency switchboard |
| Turn the ship at speed | Rudder + steering gear (duplicated, SOLAS) |
| Maneuver at low speed / dock | Bow/stern thrusters, azimuth pods |
| Hold position without anchoring | Dynamic positioning (`control-theory/`) |
| Set draft, trim, heel | Ballast system (feeds [01]/[04] checks) |
| Make drinking water | Evaporator (waste heat) or reverse osmosis |
| Prevent a cargo-tank fire | Inert gas system (O₂ below ignition limit) |
| Survive total power loss | Emergency power + dead-ship restart |
| Understand the engine driving the gensets | guide [03] Propulsion / `mechanical/` |
