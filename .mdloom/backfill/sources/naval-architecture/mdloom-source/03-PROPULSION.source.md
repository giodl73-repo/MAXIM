---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-PROPULSION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:propulsion
kind: guide
module: naval-architecture
section: naval-architecture
title: Marine Propulsion
status: source-custody
source_custody: partial
current_path: naval-architecture/03-PROPULSION.md
canonical_path: naval-architecture/03-PROPULSION.md
backsource_ids: [mdloom-backfill:naval-architecture:03-propulsion, git-history:naval-architecture:03-propulsion]
concepts: [propeller, thrust, cavitation, marine engine, propulsive efficiency]
root_concepts: [marine propulsion]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Marine Propulsion

## The Big Picture

Propulsion answers the question guide [02] set up: resistance demands a force to
overcome it — where does that force come from, and how efficiently? The answer is almost
always a screw propeller, driven through a shaft by a prime mover (usually a low-speed
diesel). The chain from fuel to forward motion passes through a series of conversions,
each with losses, and the naval architect's job is to *match* engine, propeller, and hull
so the whole train runs near its best efficiency.

```
THE PROPULSION CHAIN — FUEL TO FORWARD MOTION
===============================================================================

   FUEL  ->  PRIME MOVER  ->  TRANSMISSION  ->  SHAFT  ->  PROPELLER  ->  THRUST
   (HFO/   (diesel/turbine/  (gearbox or     (line   (screw turns   (force that
    LNG/    electric)         direct drive)   shaft)  torque into    overcomes
    diesel) burns fuel,       reduces RPM     spins   axial flow)    R_total)
            makes torque      to prop speed
   |--------|----------------|---------------|--------|--------------|----------|
   chemical  brake power      delivered       shaft    converts to    must equal
   energy    PB               power PD        torque   open-water     ship drag
                                                       thrust T       at speed V

   MATCHING PROBLEM: engine torque-RPM curve must meet propeller
   torque-RPM demand at the design point. Mis-match = lost efficiency,
   over-revving, or engine lugging.
```

The thrust the propeller develops, reduced by hull interaction, must equal the
resistance from guide [02]. That force-balance is the design point the whole chain is
tuned around.

---

## Layer 1: How a Propeller Makes Thrust

A propeller is a set of rotating wings (blades). Each blade section is an airfoil moving
through water; it generates lift, and the axial component of that lift, summed over all
blades, is **thrust**. Equivalently — and this is the cleaner mental model — the propeller
accelerates a column of water aft, and by Newton's third law the reaction pushes the ship
forward. Both pictures are correct; they are the blade-element view and the momentum view.

```
TWO VIEWS OF THE SAME PROPELLER
===============================================================================

   MOMENTUM (actuator disk) view:          BLADE-ELEMENT view:
   accelerate water aft, react forward     each blade = a rotating wing

      inflow V                                       lift L
   ====>  |  ====> V + dV (faster aft)             (perpendicular
          |                                  ___    to inflow)
        [ DISK ]  <- pressure jump          /   \    \
          |                                | sec |----> thrust component
   <==== thrust reaction                    \___/    \
                                          rotation    drag (torque)
   T = m_dot x dV (rate of momentum added) T = sum(L cos - D sin) over blades
```

Two geometry terms dominate propeller design:

```
   PITCH (P): the distance the propeller would advance in one revolution
              IF it were a screw in a solid nut (no slip). Like screw threads.

   ADVANCE (the real distance per rev) is less than pitch, because water
   yields. The shortfall is SLIP:

        Slip = (P x n - V_a) / (P x n)        n = revs/sec, V_a = advance speed

   ADVANCE COEFFICIENT (the propeller's "operating point", dimensionless):
        J = V_a / (n x D)        D = propeller diameter
```

The advance coefficient J is to a propeller what angle of attack is to a wing: it sets the
whole operating state. Slip is not waste — a propeller with zero slip produces zero thrust,
exactly as a wing at zero angle of attack produces (near) zero lift. Some slip is the price
of force.

> Old world -> new world bridge. Thrust = rate of momentum imparted to the water,
> T = ṁ·ΔV. This is the same momentum-flux relation behind a jet engine or a rocket
> (see `mechanical/` and `aeronautics/`): force equals mass flow times velocity change.
> A propeller is a low-disk-loading version — it moves a *lot* of water *slowly*, which is
> why it is efficient at ship speeds where a water-jet (high loading) is not.

---

## Layer 2: Propeller Performance — The Open-Water Curves

A propeller's behavior is captured by three dimensionless coefficients plotted against the
advance coefficient J. These **open-water characteristics** come from tank tests or CFD and
are the propeller's datasheet.

```
   THRUST coefficient:   K_T = T / (rho x n^2 x D^4)
   TORQUE coefficient:   K_Q = Q / (rho x n^2 x D^5)
   OPEN-WATER EFFICIENCY: eta_o = (J / 2pi) x (K_T / K_Q)

   (T = thrust, Q = torque, n = rev/s, D = diameter, rho = water density)
```

```
OPEN-WATER DIAGRAM (the propeller datasheet)
===============================================================================

  value |
  0.8 - |K_Q (x10)
        |---___                              eta_o (efficiency)
  0.6 - |      ---___                    ...........
        |K_T         ---___          .'''           ''. <- peak eta_o
  0.4 - |---___            ---___  .'                   '. (design J here)
        |      ---___            X'                       \
  0.2 - |            ---___    .'  ---___                  \
        |                  --'        K_T -> 0 here         \
  0.0 - +-------------------------------------------'--------\----> J
        0      0.2     0.4     0.6     0.8     1.0    1.2
              low J = heavily loaded     high J = lightly loaded -> windmills

   Read it: pick the J where eta_o peaks, then size D and n to put the
   propeller THERE at the ship's design speed. Thrust falls to zero at the
   J where the blade angle of attack -> zero (the "windmilling" point).
```

The design game: choose diameter D and revs n so the ship's design speed lands the
propeller at the J of peak η₀. Constraints fight you — bigger D is more efficient but is
limited by hull clearance and draft; lower n is more efficient but demands a bigger,
slower engine or a reduction gearbox.

---

## Layer 3: Hull-Propeller Interaction — Where Efficiency Hides

A propeller behind a hull does not see clean water, and it changes the flow around the
hull in return. Three interaction factors connect the open-water propeller to the real
installed performance. They are the reason "propulsive efficiency" is not just the
propeller's own efficiency.

```
THE THREE INTERACTION FACTORS
===============================================================================

  +------------------------------------------------------------------------+
  | WAKE FRACTION  w : the hull drags water along, so the propeller sees   |
  |   a slower inflow than the ship speed.                                 |
  |        V_a = V (1 - w)        (advance speed < ship speed)             |
  |   GOOD: a slow inflow means the prop recovers some hull-wake energy.   |
  +------------------------------------------------------------------------+
  | THRUST DEDUCTION  t : the working propeller lowers pressure at the     |
  |   stern, ADDING to hull resistance. So thrust must exceed resistance:  |
  |        T (1 - t) = R        ->   T = R / (1 - t)                       |
  +------------------------------------------------------------------------+
  | RELATIVE ROTATIVE EFFICIENCY  eta_R : the propeller behaves slightly   |
  |   differently in the non-uniform hull wake than in open water          |
  |   (usually ~0.98-1.05).                                                |
  +------------------------------------------------------------------------+
```

The force balance you must remember: **T(1 − t) = R**. The propeller must produce *more*
thrust than the bare-hull resistance, because its own suction at the stern increases the
drag. These combine into the **quasi-propulsive coefficient**:

```
   eta_D = eta_o x eta_H x eta_R

   where the HULL efficiency  eta_H = (1 - t) / (1 - w)
   (this is the term that can exceed 1.0 -- the propeller recovers
    wake energy the hull would otherwise waste)

   Typical:  eta_D ~ 0.65 - 0.75 for a merchant ship.
   So delivered power PD = PE / eta_D = R x V / eta_D.
```

Hull efficiency η_H exceeding 1.0 is not a perpetual-motion violation: the propeller is
re-using kinetic energy already in the hull's wake, energy that would otherwise be
dissipated downstream. It is energy recovery, not creation.

---

## Layer 4: Cavitation — The Hard Physical Limit

Push a propeller too hard and the pressure on the blade's suction side drops below the
**vapor pressure of water**. The water *boils at ambient temperature* — vapor bubbles form,
are swept to a higher-pressure region, and *collapse* (implode) violently. This is
**cavitation**, and it is the dominant limit on how much thrust a propeller can deliver.

```
CAVITATION — WATER BOILING ON THE BLADE
===============================================================================

   Bernoulli on the blade back: fast flow -> LOW pressure.
   If local pressure  p < p_vapor, water flashes to vapor:

        + low pressure here on suction side
        |        .oOo.   <- vapor bubbles form ("cavities")
        |       (      )
   ===> | BLADE  '.oOo.'      then sweep aft into higher pressure ...
        |        section                  |
        +                                 v
                                      *IMPLODE* -> microjets, shock,
                                      ~1000s of atmospheres locally

   THE CAVITATION NUMBER (does it cavitate?):
        sigma = (p_local - p_vapor) / (0.5 rho V^2)
        low sigma -> cavitation likely.  High V or shallow depth -> low sigma.
```

Why it matters, in order of severity:

| Consequence | Mechanism |
|-------------|-----------|
| Thrust breakdown | Cavity blankets the blade; lift collapses; thrust plateaus |
| Erosion | Implosion microjets pit and eat away the blade metal |
| Noise & vibration | Bubble collapse is broadband acoustic noise (sonar signature!) |
| Efficiency loss | Energy goes into making/collapsing vapor, not thrust |

Defenses: **more blade area** (spread the load — higher disk area ratio, DAR), **lower
RPM with bigger diameter**, **skewed blades** (so a blade enters the high-wake zone
gradually, not all at once), and for warships **supercavitating or subcavitating designs**
tuned to manage rather than avoid the cavity. For a submarine, cavitation avoidance is a
*stealth* requirement — a cavitating propeller is audible for tens of kilometres, so subs
run deep (higher ambient pressure raises σ) and slow to stay below cavitation inception.

> Old world -> new world bridge. Cavitation is a phase transition driven below the vapor
> curve — the same p–T threshold physics as boiling, just reached by dropping pressure at
> constant temperature instead of raising temperature at constant pressure. A reader who
> knows the Clausius–Clapeyron relation already understands cavitation inception; the
> cavitation number σ is just the safety margin to that curve, nondimensionalized.

---

## Layer 5: Prime Movers — What Turns the Shaft

The engine. Marine prime movers are chosen on a fuel-cost vs. power-density vs.
responsiveness trade. Merchant shipping overwhelmingly uses the low-speed two-stroke
diesel because it burns the cheapest fuel at the highest thermal efficiency of any heat
engine in production.

```
+----------------------+------------------+----------------+------------------+
| PRIME MOVER          | Efficiency       | Power density  | Typical use      |
|----------------------|------------------|----------------|------------------|
| Low-speed 2-stroke   | HIGHEST (~50%+   | low (huge,     | merchant ships   |
|   diesel             | thermal)         | heavy, slow)   | (tankers,bulkers,|
|   (~70-250 rpm)      | burns HFO        | direct-drive   | container)       |
|----------------------|------------------|----------------|------------------|
| Medium-speed         | high (~45%)      | medium         | ferries, smaller |
|   4-stroke diesel    | needs gearbox    |                | ships, gensets   |
|----------------------|------------------|----------------|------------------|
| Gas turbine          | lower (~35-40%)  | HIGHEST        | warships, fast   |
|                      | thirsty          | light, compact | ferries          |
|----------------------|------------------|----------------|------------------|
| Diesel-electric /    | flexible         | medium         | cruise ships,    |
|   integrated         | (engines run at  |                | icebreakers,     |
|   electric           | best point)      |                | DP vessels,subs  |
|----------------------|------------------|----------------|------------------|
| LNG / dual-fuel      | high, low-CO2    | medium         | new-build,       |
|                      | low SOx/NOx      |                | emissions-driven |
+----------------------+------------------+----------------+------------------+
```

Two structural points:

- **Why low-speed and direct-drive?** Propeller efficiency wants low RPM (Layer 2). A
  low-speed diesel turns at exactly propeller speed (~80-100 rpm), so it can bolt straight
  to the shaft with no gearbox — eliminating gear losses *and* matching the efficient
  propeller. The engine is the size of a house; that is the price of efficiency.
- **Why diesel-electric for cruise/DP?** Decoupling the engine speed from the propeller
  via an electrical bus lets each generator run at its best load point regardless of ship
  speed, and lets the same power feed propulsion, thrusters, and the hotel load. It trades
  a few percent conversion loss for operational flexibility — the marine version of a
  serverless "run each workload at its efficient point" architecture. (General
  thermodynamic cycles for these engines live in `mechanical/`.)

---

## Layer 6: Propulsor Types Beyond the Fixed Screw

The fixed-pitch propeller is the default, but the design space is wider.

| Propulsor | What it adds | Where used |
|-----------|--------------|------------|
| Fixed-pitch propeller (FPP) | Simple, robust, efficient | Most merchant ships |
| Controllable-pitch (CPP) | Blades rotate; thrust without changing RPM | Ferries, navy, tugs |
| Ducted (Kort nozzle) | Shroud boosts thrust at low speed/high load | Tugs, trawlers |
| Azimuth thruster / pod | Whole unit rotates 360° — propulsion + steering | Cruise, DP, offshore |
| Voith-Schneider (cycloidal) | Vertical blades; instant thrust any direction | Tugs, ferries (precision) |
| Waterjet | Pump ejects a jet; no exposed propeller | Fast craft, shallow draft |
| Contra-rotating / wake-recovery | Recover swirl energy left in the race | Efficiency retrofits |

The **azimuth pod** is the most consequential modern change: it merges propulsion and
steering (no rudder, no long shaft), and the electric pod can be diesel-electric driven,
which is why nearly every large cruise ship now uses pods.

---

## Worked Example: Sizing the Propeller and Engine

Continue the ship from guide [02]: total resistance R = 397 kN at V = 7.5 m/s, PE ≈ 3.0 MW.
Size the propulsion. (Assume w = 0.25, t = 0.18, η₀ = 0.62, η_R = 1.0.)

```
   STEP 1 -- advance speed the propeller sees:
     V_a = V (1 - w) = 7.5 x (1 - 0.25) = 5.63 m/s

   STEP 2 -- thrust required (thrust deduction):
     T = R / (1 - t) = 397,000 / (1 - 0.18) = 484,100 N = ~484 kN
     (the propeller must make 484 kN to overcome 397 kN of hull drag)

   STEP 3 -- hull efficiency and quasi-propulsive coefficient:
     eta_H = (1 - t) / (1 - w) = (1 - 0.18)/(1 - 0.25) = 0.82/0.75 = 1.093
     eta_D = eta_o x eta_H x eta_R = 0.62 x 1.093 x 1.0 = 0.678

   STEP 4 -- delivered power at the propeller:
     PD = PE / eta_D = 3.0e6 / 0.678 = 4.42 x 10^6 W = ~4.42 MW

   STEP 5 -- brake (engine) power, allowing shaft+gear losses ~0.96:
     PB = PD / 0.96 = 4.42 / 0.96 = ~4.6 MW
     -> select an engine rated ~5 MW with margin (sea + fouling allowance).

   STEP 6 -- sanity check cavitation margin (qualitative):
     thrust loading T/A_disk must stay modest; if too high, increase blade
     area ratio (DAR) or diameter to keep sigma above inception. The pod/prop
     is then iterated in the design spiral with hull clearance.
```

Note η_H = 1.093 > 1: the hull efficiency exceeds unity because the propeller recovers
wake energy — that is real, not an arithmetic slip. The bottom line: ~3 MW to tow the bare
hull becomes ~4.6 MW at the engine after all the losses, and that 4.6 MW sets the engine
size, the fuel bill, and a large fraction of the ship's lifetime cost.

---

## Common Confusion Points

### Pitch is not the same as advance, and slip is not "waste"

```
   PITCH    = theoretical advance per rev (geometry of the blade)
   ADVANCE  = actual advance per rev (water yields)
   SLIP     = the difference, as a fraction.
```

A propeller with zero slip makes zero thrust — slip is the cause of thrust, not a loss to
eliminate. You *want* the right amount of slip, exactly as a wing wants the right angle of
attack.

### Thrust does not equal resistance

Because of thrust deduction, **T(1−t) = R**, so the propeller always produces *more* thrust
than the hull's drag. Forgetting the (1−t) factor under-sizes the propeller.

### More RPM is not the path to more efficiency

Propeller efficiency *rises* as RPM falls (bigger, slower-turning disk moves more water
gently). The reason merchant ships use enormous slow-turning engines is to match that
efficient low-speed propeller directly. High RPM is for compactness (warships), not
efficiency.

### Cavitation is a pressure problem, not a speed problem per se

A propeller cavitates when *local pressure drops below vapor pressure*. Deep, slow
operation (high ambient pressure) suppresses it; shallow, fast, heavily-loaded operation
invites it. Submarines exploit this directly — depth buys cavitation margin and therefore
silence.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Get the propeller's operating point | Advance coefficient J = V_a/(nD) |
| Read a propeller's performance | Open-water curves: K_T, K_Q, η₀ vs J |
| Find inflow speed at the propeller | V_a = V(1−w) (wake fraction) |
| Find required thrust | T = R/(1−t) (thrust deduction) |
| Get installed propulsive efficiency | η_D = η₀·η_H·η_R (≈0.65–0.75) |
| Convert resistance to engine power | PB = R·V/(η_D·η_shaft) |
| Check if the propeller will cavitate | Cavitation number σ vs inception |
| Maximize fuel efficiency | Big slow-turning prop + low-speed 2-stroke diesel |
| Combine propulsion + steering | Azimuth pod / thruster |
| Run engines at best load regardless of speed | Diesel-electric |
| Understand the engine's thermodynamic cycle | `mechanical/` |
| Get the resistance the thrust must overcome | guide [02] Hull Form & Resistance |
