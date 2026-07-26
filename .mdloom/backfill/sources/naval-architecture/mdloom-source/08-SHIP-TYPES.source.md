---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-SHIP-TYPES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:ship-types
kind: guide
module: naval-architecture
section: naval-architecture
title: Ship Types
status: source-custody
source_custody: partial
current_path: naval-architecture/08-SHIP-TYPES.md
canonical_path: naval-architecture/08-SHIP-TYPES.md
backsource_ids: [mdloom-backfill:naval-architecture:08-ship-types, git-history:naval-architecture:08-ship-types]
concepts: [ship types, cargo ships, tankers, container ships, passenger ships, naval vessels]
root_concepts: [ship types]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Ship Types

## The Big Picture

There is no such thing as a generic ship. Every vessel is the answer to a specific mission,
and the mission dictates the hull form, the speed, the structure, and the systems. A
supertanker and a frigate share the same physics — the same Archimedes, the same Froude, the
same hull girder — yet they look nothing alike, because they optimize for opposite things:
one maximizes cargo per dollar at low speed, the other maximizes speed and survivability at
any cost. This guide is the taxonomy: **form follows cargo (or mission)**, and reading the
shape tells you the job.

```
THE SHIP-TYPE LANDSCAPE — MISSION DICTATES FORM
===============================================================================

                         WHAT IS BEING MOVED / DONE?
                                    |
   +----------------+---------------+----------------+-----------------+
   |                |               |                |                 |
   v                v               v                v                 v
  DRY CARGO       LIQUID CARGO    PEOPLE           MILITARY        SPECIAL /
  (solids)        (bulk liquids)  (passengers)     (warfare)       WORKING
   |                |               |                |                 |
   +-bulk carrier   +-crude tanker  +-cruise ship    +-aircraft       +-tug
   +-container ship +-product tnkr  +-ferry (ro-pax) | carrier        +-dredger
   +-general cargo  +-chemical tnkr +-yacht          +-destroyer/     +-research
   +-reefer        +-LNG/LPG carrier|                | frigate        +-icebreaker
   +-ro-ro (cars)   +-              |                +-submarine       +-fishing
   +-heavy-lift     |               |                +-amphibious      +-offshore
   |                |               |                |                 | (guide 09)
   slow, full,     slow, full,     moderate,        fast, fine,      varied,
   Cb~0.8          segregated      comfort+stability survivable,      task-built
                   tanks           driven            redundant
```

Read it top-down: the cargo (or mission) at the top forces every design choice below it.
The block coefficient, the speed, the structural arrangement, the systems — all fall out of
what the ship must carry and how fast. The physics of every box here is the same; only the
optimization target differs.

---

## Layer 1: Dry Bulk and General Cargo

The oldest and simplest mission: move solid cargo. The split is **bulk** (loose,
poured — grain, coal, ore) versus **unitized** (in containers or on pallets).

```
+----------------------+---------------------------------------------------+
| Type                 | What and how                                      |
|----------------------|-------------------------------------------------- |
| BULK CARRIER         | Loose dry cargo (iron ore, coal, grain) in large  |
|   (bulker)           | open holds, loaded by chute/grab. Cb~0.80, slow   |
|                      | (~14 kn), single-deck. Sizes: Handysize ->        |
|                      | Panamax -> Capesize (too big for any canal).      |
|                      | RISK: heavy dense ore in one hold -> high hull    |
|                      | bending [04]; cargo liquefaction -> stability.    |
|----------------------|-------------------------------------------------- |
| GENERAL CARGO        | Mixed break-bulk on multiple 'tween decks, own    |
|                      | cargo cranes. The pre-container workhorse, now    |
|                      | niche (project cargo, ports without container     |
|                      | handling).                                        |
|----------------------|-------------------------------------------------- |
| REEFER (refrigerated)| Perishables in refrigerated holds. Largely        |
|                      | displaced by refrigerated CONTAINERS.             |
|----------------------|-------------------------------------------------- |
| RO-RO / car carrier  | Wheeled cargo driven on/off via ramps. Car        |
|   (PCTC)             | carriers are tall slab-sided boxes (huge windage, |
|                      | many car decks). RISK: open vehicle decks -> free |
|                      | surface + low subdivision -> stability sensitive. |
+----------------------+---------------------------------------------------+
```

Two type-specific dangers worth knowing because they are pure applications of earlier guides:

- **Bulk-carrier hull bending.** Dense ore fills only part of the hold's volume, so it can be
  concentrated in alternate holds — producing severe still-water bending moments ([04]). Bad
  loading has broken bulkers in half. Loading is computer-controlled to a bending-moment
  limit.
- **Cargo liquefaction.** Fine wet ore concentrates can behave like a liquid under vibration
  — the cargo *liquefies*, its free surface destroys stability ([01]), and the ship rolls
  over. This has sunk multiple bulkers; it is a moisture-content cargo-safety rule.

---

## Layer 2: Container Ships — The Engine of Globalization

The container ship deserves its own layer: standardizing cargo into the **intermodal
container** (the ISO TEU — twenty-foot equivalent unit) collapsed the cost of moving goods
and reshaped the world economy. The ship is essentially a cellular rack for steel boxes.

```
THE CONTAINER SHIP (a cellular rack at sea)
===============================================================================

   cross-section: containers stacked in CELL GUIDES, below AND above deck

        +--+--+--+--+--+--+--+--+   <- lashed on-deck stacks (high, exposed)
        |[]|[]|[]|[]|[]|[]|[]|[]|
   deck ============================
        |[]|[]|[]|[]|[]|[]|[]|[]|   <- in-hold cells (vertical cell guides
        |[]|[]|[]|[]|[]|[]|[]|[]|      hold the boxes in stacks)
        |[]|[]|[]|[]|[]|[]|[]|[]|
        +--------------------------+ double bottom (ballast/fuel)

   STRUCTURAL CHALLENGE: huge deck OPENINGS (the hatches) for cell access
   remove most of the strength deck -> the hull loses TORSIONAL stiffness.
   An open-top box is weak in TWIST. So container ships have very strong,
   deep TORSION BOXES along the deck edges and at hatch corners (fatigue
   hot-spots, [04]). The MOL Comfort (2013) broke in half -- a hull-girder
   failure that reshaped container-ship strength rules.
```

The container ship is a beautiful illustration of structure following cargo. To stack and
access boxes you need huge hatch openings, but a box with the top cut out is torsionally weak
(twist it and it racks open). The whole structural design — heavy continuous **torsion
boxes** down the deck edges, reinforced hatch corners — exists to restore the twist stiffness
the openings removed. Sizes have exploded from a few hundred TEU (1960s) to >24,000 TEU
(ULCV, Ultra-Large Container Vessels) — limited now by port draft and crane reach, not naval
architecture.

> Old world -> new world bridge. The shipping container is the original interface standard:
> a fixed-dimension, opaque, self-describing payload that any ship, crane, truck, or train
> can handle without knowing its contents. Malcolm McLean's 1956 standardization did for
> freight exactly what a stable ABI or a containerized deployment artifact did for software —
> decouple the payload from the transport so each can evolve independently. "Containerization"
> is the same word and the same idea; the software usage borrowed the metaphor deliberately.
> (See `transportation/` for the intermodal logistics network this ship serves.)

---

## Layer 3: Tankers and Gas Carriers — Liquid Cargo

Liquid cargo is carried in integral tanks built into the hull. The defining concerns are
**segregation** (don't mix or contaminate cargoes), **fire/explosion** (volatile cargo +
oxygen), and for cold gases, **containment of cryogenic liquid**.

```
+----------------------+---------------------------------------------------+
| Type                 | Cargo and key feature                             |
|----------------------|-------------------------------------------------- |
| CRUDE OIL TANKER     | Crude oil in large tanks. DOUBLE HULL mandatory   |
|   (VLCC/ULCC)        | (MARPOL, post-Exxon Valdez) -- a void/ballast     |
|                      | space between cargo and the sea to survive a      |
|                      | grounding without spilling. Inert gas system [06] |
|                      | keeps tanks below the explosive O2 limit.         |
|----------------------|-------------------------------------------------- |
| PRODUCT TANKER       | Refined products (gasoline, diesel, jet). Many    |
|                      | smaller COATED tanks for segregation + cleaning.  |
|----------------------|-------------------------------------------------- |
| CHEMICAL TANKER      | Many independent tanks, exotic coatings/stainless,|
|                      | each cargo isolated (own pump/line) -- a floating |
|                      | array of separate chemical reactors-in-transit.   |
|----------------------|-------------------------------------------------- |
| LNG CARRIER          | Methane at -162 C, near atmospheric pressure.     |
|                      | Cryogenic CONTAINMENT (membrane tanks or Moss     |
|                      | spheres). BOIL-OFF gas is burned as fuel.         |
|----------------------|-------------------------------------------------- |
| LPG CARRIER          | Propane/butane, either PRESSURIZED, or REFRIG.    |
|                      | (-48 C), or semi-pressurized. Simpler than LNG.   |
+----------------------+---------------------------------------------------+
```

Two type-defining engineering points:

- **The double hull.** After the Exxon Valdez (1989), MARPOL mandated **double-hull** crude
  tankers: a second inner skin separated from the outer by ~2 m of ballast/void space, so a
  grounding that breaches the outer hull does not reach the cargo. It is damage tolerance
  bought with structure — and a direct application of the subdivision logic in [01].
- **LNG containment and boil-off.** LNG is methane chilled to −162 °C, where it shrinks ~600×
  to a liquid. The tanks (Moss spherical, or **membrane** systems lining the hold) must
  contain a cryogenic liquid that constantly **boils off** as heat leaks in; the boil-off gas
  is routed to the engines as clean fuel — turning an unavoidable loss into propulsion. The
  sloshing of partially-full membrane tanks is itself a structural load case (a free-surface
  problem, cousin to [01] and [05]).

---

## Layer 4: Passenger Ships — Carrying People

When the cargo is human beings, the optimization shifts to **comfort, stability margin, and
survivability**. Passengers cannot be ballast — they move, they get seasick, and they must
all be evacuated.

```
+----------------------+--------------------------------------------------+
| Type                 | Defining concerns                                |
|----------------------|--------------------------------------------------|
| CRUISE SHIP          | A floating resort. Huge superstructure (high VCG |
|                      | -> stability challenge, [01]). Diesel-electric + |
|                      | pods [03][06]. Roll stabilizers for comfort [05].|
|                      | SAFE RETURN TO PORT rules: redundant, segregated |
|                      | so one casualty can't disable the ship.          |
|----------------------|--------------------------------------------------|
| FERRY / RO-PAX       | Cars + passengers, short routes, fast turnaround.|
|                      | The RO-RO vehicle deck is the danger: one long   |
|                      | open deck -> if flooded, catastrophic free       |
|                      | surface -> rapid capsize. (Herald of Free        |
|                      | Enterprise 1987, Estonia 1994.) -> tighter       |
|                      | damage-stability rules for ro-pax.               |
|----------------------|--------------------------------------------------|
| HIGH-SPEED CRAFT     | Catamarans, hydrofoils, SES -- trade displacement|
|                      | for speed (planing/foiling past hull speed [02]).|
+----------------------+--------------------------------------------------+
```

The passenger-ship lessons are written in disasters. The **ro-ro vehicle deck** is a single
vast open space with no subdivision; if the bow door fails or water enters, the free surface
([01]) is enormous and the ship can capsize in minutes — the Herald of Free Enterprise
(1987) and Estonia (1994) are the grim case studies that drove tighter ro-pax damage-
stability rules. Modern cruise ships are governed by **Safe Return to Port** philosophy: the
ship is so redundant and segregated that after a fire or flood casualty it can still make
port under its own power with essential systems running — the "ship is its own lifeboat"
principle. The tall superstructure raises the centre of gravity, making cruise-ship stability
([01]) a genuine design tension against the desire for more decks and balconies.

---

## Layer 5: Naval Vessels — Mission Is Warfare

Warships abandon cost-per-tonne efficiency entirely. They optimize **speed, survivability,
and the ability to carry and fight a weapons system**. The hull is fine and fast (low Cb,
[02]); the design is dominated by redundancy, signature reduction, and shock resistance.

```
+----------------------+---------------------------------------------------+
| Type                 | Defining concerns                                 |
|----------------------|-------------------------------------------------- |
| AIRCRAFT CARRIER     | A mobile airbase. Vast flight deck; nuclear or    |
|                      | gas-turbine; enormous power for catapults (EMALS).|
|                      | Survivability through size + compartmentation.    |
|----------------------|-------------------------------------------------- |
| DESTROYER / FRIGATE  | Fast (~30 kn), fine hull, gas-turbine or CODAG/   |
|                      | CODLAG. Packed with sensors, missiles, guns.      |
|                      | Damage control + redundancy are paramount.        |
|----------------------|-------------------------------------------------- |
| SUBMARINE            | Operates SUBMERGED -> pressure hull (a cylinder   |
|                      | in EXTERNAL pressure -> buckling-critical, [04]). |
|                      | Ballast/trim for DEPTH control. Nuclear or AIP.   |
|                      | Stealth: cavitation avoidance [03], quieting.     |
|----------------------|-------------------------------------------------- |
| AMPHIBIOUS / LANDING | Move and land troops/vehicles. Well decks, ramps. |
+----------------------+---------------------------------------------------+
```

Two naval-specific physics points that flip earlier guides on their head:

- **The submarine pressure hull is loaded the opposite way.** A surface ship resists internal
  loads and external waves; a submerged submarine's hull is a cylinder in *external*
  pressure, so its enemy is **collapse buckling** ([04]) — the deeper it goes, the closer to
  implosion. Its "collapse depth" is a buckling limit, and ring-stiffened cylinders are the
  classic solution. Submarines also control depth by **vertical** equilibrium of buoyancy and
  weight (blow/flood ballast), making them the one vessel where stability is genuinely
  three-dimensional.
- **Survivability through redundancy and signature.** Warship design is dominated by *damage
  control* (zoned firefighting, redundant power and propulsion, shock-hardened mounts) and
  *signature reduction* (radar, acoustic, magnetic, infrared, and — crucially — the
  cavitation noise of [03], which is why submarines run deep and slow to stay silent). A
  frigate's stealth is a multi-spectrum optimization problem layered on top of a fast hull.

---

## Layer 6: Special-Purpose and Working Vessels

Ships built around a *task* rather than a cargo. The hull and systems serve the job.

| Type | Task / defining feature |
|------|-------------------------|
| Tug | Massive thrust at near-zero speed; bollard pull, not transit speed, is the spec. Often Voith-Schneider or azimuth ([03]) for instant omnidirectional thrust |
| Dredger | Excavate and move seabed material; trailing-suction or cutter-suction; cargo is mud |
| Icebreaker | Ride up onto and crush ice with hull weight; reinforced bow, huge power, special hull form; pod propulsion for maneuvering in ice |
| Research vessel | Quiet (acoustic survey), DP for station-keeping, lab and crane fit-out |
| Fishing vessel | Catch handling and processing; stability sensitive (catch on deck = high free-surface/VCG) |
| Cable layer / offshore | Highly task-specialized; many overlap with offshore engineering (guide [09]) |
| Heavy-lift / semi-submersible | Submerge the deck to float a cargo (a platform, another ship) over it, then deballast to lift |

The **icebreaker** is the nicest illustration of mission-driven form: it does not cut ice
edge-on; it rides its reinforced, raked bow *up onto* the ice and breaks it with the ship's
weight, then pushes the broken floes aside with a rounded hull. Its hull form, structure
([04]), and enormous installed power all follow from that single mechanical idea — exactly
the "form follows mission" thesis of this whole guide.

---

## Comparison: The Full Type Spectrum at a Glance

| Type | Cb (fullness) | Speed | What drives the design |
|------|---------------|-------|------------------------|
| VLCC tanker | ~0.83 | ~15 kn | Cargo volume per dollar; segregation; double hull |
| Bulk carrier | ~0.80 | ~14 kn | Dense cargo; hull bending; cheap structure |
| Container ship | ~0.65 | ~22 kn | TEU capacity; torsion box; schedule speed |
| Cruise ship | ~0.65 | ~22 kn | Comfort; stability vs. tall superstructure; SRtP |
| Ro-pax ferry | ~0.55 | ~25 kn | Turnaround; vehicle-deck damage stability |
| Frigate | ~0.45 | ~30 kn | Speed, survivability, weapons fit |
| Submarine | n/a (cylinder) | varies | Collapse depth (buckling); stealth; depth control |
| Tug | ~0.55 | low | Bollard pull, not speed; omnidirectional thrust |

The single most revealing column is Cb: it sorts the entire merchant-to-naval spectrum from
the "brick" (maximize volume, minimize cost) to the "knife" (minimize wave drag, maximize
speed), exactly as guide [02] predicts.

---

## Common Confusion Points

### A "container ship" and a "bulk carrier" are not interchangeable

They carry fundamentally different cargo with opposite structural problems. A bulker has huge
open holds and fights *hull bending* from dense concentrated cargo; a container ship has huge
deck openings and fights *torsion* from the missing strength deck. You cannot pour ore into a
container ship or stack boxes efficiently in a bulker.

### Tonnage means different things for different types

A "300,000 DWT tanker" (deadweight — cargo-carrying weight) and a "200,000 GT cruise ship"
(gross tonnage — internal volume) are measured by *different quantities* (see [00]). Tankers
and bulkers are sold on deadweight (how much they carry); cruise ships on gross tonnage and
berths (how much enclosed space). Comparing the numbers directly is meaningless.

### A submarine's stability problem is upside-down from a surface ship's

A surface ship relies on the *waterplane* (the metacenter, [01]) for stability — which a
fully submerged submarine does not have. Submerged, a sub is stable only if G is *below* B
(pendulum stability), and its hull's enemy is external-pressure *buckling*, not wave bending.
Almost every stability intuition from [01] inverts for the submerged case.

### Bigger is limited by ports, not by naval architecture

Ultra-large container ships and VLCCs have stopped growing not because the physics fails but
because **draft, beam, canal locks, and crane reach** cap them. The "Panamax/Suezmax/
Capesize" size classes are named after the *infrastructure* constraint, not a hydrodynamic
one — the chokepoint is the port and the canal.

---

## Decision Cheat Sheet

| The mission is... | The ship is... |
|---|---|
| Move loose dry cargo cheaply | Bulk carrier (watch hull bending, liquefaction) |
| Move standardized boxes on schedule | Container ship (watch torsion, hatch corners) |
| Move crude/refined oil | Double-hull tanker + inert gas |
| Move chilled methane | LNG carrier (cryogenic containment, boil-off fuel) |
| Move cars and passengers, short route | Ro-pax ferry (vehicle-deck damage stability) |
| Move thousands of guests in comfort | Cruise ship (Safe Return to Port, stabilizers) |
| Project air power | Aircraft carrier |
| Fight fast on the surface | Destroyer/frigate (speed + survivability) |
| Operate hidden, submerged | Submarine (collapse-depth buckling, stealth) |
| Apply huge thrust at zero speed | Tug (bollard pull, omnidirectional thrust) |
| Break ice | Icebreaker (ride-up bow, huge power) |
| Why each hull is shaped as it is | guide [02] Hull Form & Resistance |
| The logistics network these serve | `transportation/` |
