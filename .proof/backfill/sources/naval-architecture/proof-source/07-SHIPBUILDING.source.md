---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "07-SHIPBUILDING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:shipbuilding
kind: guide
module: naval-architecture
section: naval-architecture
title: Shipbuilding
status: source-custody
source_custody: partial
current_path: naval-architecture/07-SHIPBUILDING.md
canonical_path: naval-architecture/07-SHIPBUILDING.md
backsource_ids: [proof-backfill:naval-architecture:07-shipbuilding, git-history:naval-architecture:07-shipbuilding]
concepts: [shipbuilding, block construction, welding, classification societies, ship production]
root_concepts: [shipbuilding]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Shipbuilding

## The Big Picture

Designing a ship and *building* one are different engineering problems. A modern large ship
is not assembled plank by plank on a slipway; it is built as dozens of pre-outfitted
**blocks** — three-dimensional hull sections complete with piping, ladders, and paint —
that are welded together in a dry dock in a matter of weeks. The dominant constraint is no
longer "will it float" (the design office settled that) but **production efficiency**:
minimize the most expensive operation (welding and work performed in awkward positions high
up in a dock) by doing as much as possible early, on the ground, in a workshop.

```
THE SHIPBUILDING PIPELINE — FROM STEEL PLATE TO LAUNCHED SHIP
===============================================================================

   STEEL          PART            SUB-          BLOCK          ERECTION
   STOCKYARD  ->  FABRICATION ->  ASSEMBLY  ->  ASSEMBLY  ->   (join blocks
   plates,        cut, bend,      weld parts    pre-outfit:    in dry dock)
   profiles       blast, prime    into panels   pipe, cable,        |
   |              |               + stiffeners  paint, fit out      v
   |              v               |             |               LAUNCH /
   |          NC cutting          v             v               FLOAT-OUT
   |          (plasma/laser)   stiffened      a 3-D hull            |
   |          robotic welding  panels         section,             v
   |                                          ~hundreds of    SEA TRIALS
   |                                          tonnes,         (commissioning,
   v                                          erected by      speed/turning/
   the further LEFT you do work, the          giant cranes    endurance) ->
   CHEAPER it is (flat, low, in a shop).      onto the keel   DELIVERY
```

The governing production principle: **move work left and down** — do it earlier in the
sequence, lower to the ground, flatter, and in a controlled shop rather than overhead in a
dock. Every metre of weld done on a flat panel in a workshop is far cheaper than the same
weld done overhead, 30 m up, joining two blocks.

---

## Layer 1: Why Block Construction Won

Before ~1940, ships were built keel-up on a slipway: lay the keel, erect frames, hang plates,
launch the bare hull, then spend a year outfitting the floating shell with engines and
piping in cramped, dark, vertical spaces. Block (or "modular") construction inverts this.

```
OLD WAY (slipway, sequential) vs MODERN (block, parallel)
===============================================================================

  SLIPWAY (serial):                    BLOCK (parallel + pre-outfit):
  keel -> frames -> plating ->         build ~50 blocks SIMULTANEOUSLY in
  launch -> outfit afloat              workshops, each fully outfitted, then
  (one long critical path)             weld blocks together in the dock

  time --->                            time --->
  [====lay hull====][===outfit===]     [blocks built in parallel][erect][outfit
                                        \________ overlap ________/  gaps only]

  WHY BLOCKS WIN:
   - parallelism: 50 blocks built at once -> short dock occupancy
   - pre-outfitting: install engines/pipe/paint in an open block on the
     ground (good access, downhand welding) BEFORE it is closed up
   - downhand welding: weld flat/down, not overhead -> faster, better quality
   - the expensive dry dock is occupied only for erection, not the whole build
```

The dry dock is the bottleneck resource (there are only so many, and they are enormous
capital), so the entire method is organized to *minimize dock occupancy*. Liberty-ship mass
production in WWII proved the principle (a ship in days by welding pre-made sections); the
Japanese and Korean yards industrialized it into today's method.

> Old world -> new world bridge. Block construction is parallelized assembly with
> pre-integration — build independent modules concurrently with their interfaces fully
> defined, integrate each in isolation, then do a fast final assembly with only the seams
> left. The dry dock is the scarce shared resource you protect by doing everything possible
> off it first. It is the same logic as componentized builds: maximize the work that happens
> in parallel and in isolation, minimize the serial integration window on the shared
> critical path.

---

## Layer 2: Welding — The Joining Technology

A steel ship is held together by welds — kilometres of them. Welding fuses the plates into
the continuous box girder that [04] assumes. The choice of process trades speed, position,
quality, and automation.

```
THE MAIN MARINE WELDING PROCESSES
===============================================================================

  +-----------------+--------------------------+----------------------------+
  | Process         | How                      | Where used                 |
  |-----------------|--------------------------|----------------------------|
  | SMAW (stick)    | consumable coated        | repairs, awkward positions,|
  |                 | electrode, manual        | erection joints in the dock|
  |-----------------|--------------------------|----------------------------|
  | GMAW / FCAW     | continuous wire feed,    | workhorse: panels, blocks; |
  | (MIG / flux-    | semi-auto, high deposit  | robot-friendly             |
  |  cored)         |                          |                            |
  |-----------------|--------------------------|----------------------------|
  | SAW (submerged  | arc under a flux blanket,| LONG straight seams on flat|
  |  arc)           | very high deposit, auto  | panels -> hugely productive|
  |-----------------|--------------------------|----------------------------|
  | Robotic / one-  | automated GMAW/SAW; weld | high-volume panel lines    |
  |  side welding   | a panel from one side    | (Korean/Japanese megayards)|
  +-----------------+--------------------------+----------------------------+
```

The two structural concerns the welder fights, both from `materials/`:

- **Distortion.** Welding pours heat into one line; the metal expands, then shrinks on
  cooling, warping the panel. Yards control it with welding *sequence* (balanced, symmetric),
  jigs, pre-setting, and line heating to straighten afterward. A warped block will not mate
  with its neighbor.
- **Residual stress and defects.** Cooling welds lock in tensile residual stress; defects
  (porosity, lack of fusion, cracks) become fatigue-crack starters ([04]). Hence
  **nondestructive testing (NDT)** — radiography, ultrasonics, dye penetrant, magnetic
  particle — to a sampling plan the classification society sets. Critical joints get 100%
  inspection.

The **erection joints** (where blocks meet in the dock) are the worst case: often overhead
or vertical, hard to access, and welded with manual SMAW. Block design deliberately places
the block boundaries where the structure is simplest and most accessible, precisely to make
these unavoidable hard welds as easy as possible.

---

## Layer 3: Hull Form to Steel — Lofting and Lines

The design office defines the hull as a smooth surface (the **lines plan**); the yard must
turn that surface into thousands of individually-cut, individually-bent steel plates that
fair together. This translation is **lofting**, and it has been revolutionized by CAD/CAM.

```
FROM A SMOOTH SURFACE TO CUT PLATES
===============================================================================

   LINES PLAN (the design surface, a set of level curves):
     waterlines (horizontal slices) + buttocks (vertical fore-aft slices)
     + sections (transverse slices). Three orthogonal families of curves
     that together define one smooth hull surface.

        sections           waterlines          buttocks
        )  )  )  )         ___________         | | | |
       (  (  (  (         /___________\        | | | |
        )  )  )  )       /_____________\       | | | |
       (transverse)     (horizontal)          (fore-aft vertical)

   FAIRING: make all three families mutually consistent and SMOOTH (no
   bumps). Once done on a computer (was once done full-size on a
   "mould loft" floor), the surface is exact.

   NESTING: unfold the curved hull into flat plate developments, then
   NEST the parts onto stock plates to minimize scrap, and post NC
   cutting paths (plasma/laser) + bending data (rolls, line heating).
```

Old shipyards had a **mould loft** — a vast floor where the lines were drawn full-size and
wooden templates made. Today the loft is a CAD model, and the same data drives NC cutting
machines and robotic welders directly — a continuous digital thread from the fairing surface
to the cutting torch. **Plate bending** to compound (double) curvature at the bow and stern
is still part craft: rolls do single curvature, but compound shapes are formed by **line
heating** (running a torch in patterns so differential shrinkage curls the plate) — a
technique that resists full automation.

> Old world -> new world bridge. Lofting/fairing is constructing a smooth interpolating
> surface from constraint curves and verifying continuity — the marine ancestor of spline
> surface modeling. Indeed the **ship spline** (a flexible batten bent through control points
> by "ducks") is literally where the mathematical spline comes from: B-splines and NURBS in
> CAD are a formalization of the draftsman's wooden batten. The numerical-methods reader will
> recognize fairing as enforcing C² continuity across patches.

---

## Layer 4: Launching and Float-Out

Once the hull is structurally complete, it must enter the water. The method depends on how
the ship was built.

```
GETTING THE HULL WET
===============================================================================

  DRY DOCK FLOAT-OUT (modern norm):      END / SIDE LAUNCH (older slipways):
  ship built in a graving dock; flood    ship slides down a greased ramp into
  the dock, ship floats up, tow out.     the water, stern-first (or sideways
  Gentle, controlled, no dynamics.       in a narrow river). A dramatic but
                                         DYNAMICALLY tricky event.

   |~~~~~~~~~~~~~~~~|                     ship -->\
   |   ___________  |  flood              ========= \  greased
   |  /   SHIP    \ | -> floats          ==========  \ ways
   |  \___________/ |    up               ----------- \____ SPLASH
   |________________|                            ~~~~~~~~~~~~~~~~

   Launch mechanics (for ramp launches): as the stern enters and gains
   buoyancy, the ship pivots about the fore poppet; the naval architect
   computes the launching curves to ensure it does NOT (a) tip over the
   end, (b) drop the bow too hard, or (c) overstress the hull as support
   shifts from the ways to buoyancy. A genuine transient stability problem.
```

Most large ships today are built in **graving (dry) docks** and simply *floated out* — flood
the dock, the ship lifts on its own buoyancy, tow it to the fitting-out quay. It is calm and
controllable. The traditional **end launch** down greased ways is a real dynamics problem
(the launching calculation ensures the ship neither tips over the end of the ways nor drops
its bow nor overstresses as buoyancy takes over from the ground ways) and survives mostly at
smaller or older yards.

---

## Layer 5: Classification Societies and Regulation

A ship is not certified by its builder. **Classification societies** — independent technical
bodies — set the structural and systems rules, approve the design, survey construction, and
issue the "class" certificate that insurers and flag states require. This is the marine
analog of an external standards-and-certification authority, and it is central to the whole
industry.

```
WHO SAYS THE SHIP IS SAFE? (the certification stack)
===============================================================================

  +----------------------------------------------------------------------+
  | IMO (International Maritime Organization, UN body)                   |
  |   makes the CONVENTIONS: SOLAS (safety), MARPOL (pollution),         |
  |   Load Line, STCW (crew training), Ballast Water. Treaty law.        |
  +----------------------------------------------------------------------+
                       | adopted into national law by ...
                       v
  +----------------------------------------------------------------------+
  | FLAG STATE (the country the ship is registered in)                   |
  |   legally responsible; often DELEGATES survey/certification to ...   |
  +----------------------------------------------------------------------+
                       | delegates technical work to ...
                       v
  +-----------------------------------------------------------------------+
  | CLASSIFICATION SOCIETY (DNV, Lloyd's Register, ABS, BV, ClassNK...)   |
  |   - publishes the STRUCTURAL RULES (scantlings, [04])                 |
  |   - approves the design drawings                                      |
  |   - SURVEYS construction (welds, NDT, tests) and issues CLASS         |
  |   - re-surveys periodically for the ship's LIFE (annual/5-yr docking) |
  +-----------------------------------------------------------------------+
                       | PORT STATE CONTROL inspects in port (a check on all)
```

The major societies (DNV, Lloyd's Register, ABS, Bureau Veritas, ClassNK, and others
coordinated through IACS) write the **class rules** — the empirical-and-analytical
scantling formulas the structural designer of [04] actually uses. "Building to class" means
the ship is designed to those rules and surveyed against them; **maintaining class** means
periodic surveys (annual, intermediate, and the major 5-year special survey in dry dock) for
the ship's entire life. Lose class and the ship is uninsurable and effectively cannot trade.
**Port State Control** (e.g. the Paris and Tokyo MoUs) is the enforcement backstop — any
port may inspect any visiting ship and detain it if substandard.

> Old world -> new world bridge. The class-society regime is a third-party conformance and
> continuous-audit system: an independent authority publishes the standard, certifies the
> design against it, witnesses the build, and re-audits on a fixed cadence for the asset's
> whole life — with a separate enforcement body (Port State Control) spot-checking in the
> field. It is the safety-critical-industry pattern of "the builder cannot self-certify;"
> the same structure as independent certification in aviation or in regulated software.

---

## Worked Example: Planning a Block Build

A 250 m container ship, ~22,000 tonnes of hull steel. Plan the block strategy at a high
level.

```
   STEP 1 -- divide the hull into blocks:
     Target block size ~ 300-600 t (limited by the dock crane capacity, say
     900 t cranes in tandem). 22,000 t / ~450 t avg -> ~50 blocks.
     Place block boundaries at SIMPLE, ACCESSIBLE structure (avoid splitting
     a complex bracket) so the erection welds are as easy as possible.

   STEP 2 -- maximize PRE-OUTFITTING (move work left/down):
     In each open block on the ground, install: piping spools, cable trays,
     ventilation ducts, ladders, foundations, and PAINT -- all with good
     access and downhand welding, BEFORE the block is closed and erected.
     Rule of thumb: every hour of outfitting done in the block is worth
     several hours done later in the closed, erected ship.

   STEP 3 -- build blocks in PARALLEL in workshops:
     ~50 blocks fabricated concurrently on panel lines and assembly bays.
     The dry dock sits empty of THIS ship until erection begins -> dock
     occupancy minimized (the scarce resource is protected).

   STEP 4 -- erect in the dry dock:
     Lay the keel blocks, then crane successive blocks into place and weld
     the erection joints (the hard, often-overhead welds). NDT the critical
     joints to the class society's sampling plan. Fair and align as you go.

   STEP 5 -- float out and finish:
     Flood the dock, float the ship to the fitting-out quay, complete the
     systems that cross block boundaries, then SEA TRIALS: measure speed vs
     power (validating guide [02]/[03]!), turning circle, crash-stop,
     endurance, and noise -- the design's predictions meet reality here.

   STEP 6 -- deliver under class:
     Class surveyor signs off the build; flag state issues statutory
     certificates (SOLAS, Load Line, MARPOL). The ship can now trade.
```

Sea trials are the moment the whole module closes the loop: the speed-power curve predicted
in [02] and the propulsion design of [03] are measured against the real ship, and the
stability booklet from [01] is verified by an **inclining experiment** (deliberately shift a
known weight, measure the heel, back out the real GM/KG). Theory meets the sea, and the
design is confirmed or corrected.

---

## Common Confusion Points

### Ships are not built keel-up plank-by-plank anymore

The mental image of laying a keel and building up frame by frame is a century out of date
for large vessels. Modern ships are built as ~50 pre-outfitted blocks welded together — the
"keel laying" is now a ceremonial placement of the first block, not the start of a serial
build.

### Pre-outfitting is the whole point

The reason block construction is cheap is not just parallelism — it is that pipe, cable,
paint, and machinery go *into an open block on the ground* with excellent access, instead of
into a finished hull's cramped vertical spaces. Closing a block too early (before outfitting)
throws away the main advantage.

### "Classification" is not a quality rating

A classification society is not ranking ships like a hotel. "In class" is a binary technical
certification that the ship meets the society's structural and systems rules and has passed
its surveys. A ship is either in class or not; losing class makes it uninsurable.

### The flag state and the class society are different things

The **flag state** is the country of registration (legally responsible, sets statutory
requirements); the **class society** is the independent technical body that writes the
construction rules and does the surveys (often delegated the statutory work by the flag).
"Flags of convenience" (Panama, Liberia, Marshall Islands) are about jurisdiction and cost,
not about who inspects the welds.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Build a large ship efficiently | Block (modular) construction |
| Make construction cheap | Pre-outfit blocks; move work left and down |
| Protect the dry-dock bottleneck | Build blocks in parallel; erect fast |
| Join the steel | Welding: SAW (long seams), GMAW/FCAW (blocks), SMAW (erection) |
| Avoid weld warping | Welding sequence, jigs, line-heating correction |
| Verify weld integrity | NDT (radiography/ultrasonics) to class sampling |
| Turn a hull surface into cut plates | Lofting/fairing → nesting → NC cutting |
| Form compound-curved plates | Rolls + line heating |
| Get the hull into the water | Dry-dock float-out (modern) or ramp launch |
| Certify the design and build | Classification society rules + survey |
| Know the international safety law | IMO conventions (SOLAS, MARPOL, Load Line) |
| Verify the design predictions | Sea trials + inclining experiment ([01]/[02]/[03]) |
| Review the welds' structural role | guide [04] Ship Structures |
| Review weld metallurgy & defects | `materials/`, `manufacturing/` |
