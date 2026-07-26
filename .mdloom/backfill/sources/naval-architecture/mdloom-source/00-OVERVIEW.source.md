---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:overview
kind: guide
module: naval-architecture
section: naval-architecture
title: Naval Architecture - Landscape and the Design Spiral
status: source-custody
source_custody: partial
current_path: naval-architecture/00-OVERVIEW.md
canonical_path: naval-architecture/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:naval-architecture:00-overview, git-history:naval-architecture:00-overview]
concepts: [naval architecture, design spiral, ship design, marine engineering]
root_concepts: [naval architecture]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Naval Architecture — Landscape and the Design Spiral

## The Big Picture

Naval architecture is the engineering of things that float and move through water.
It sits at the intersection of fluid dynamics (water is the medium), structural
mechanics (the hull is a giant beam), and systems engineering (a ship is a small
self-contained city). The field is unusually constrained: a ship must simultaneously
float upright, resist the sea's loads, move efficiently, and carry cargo — and these
goals fight each other. The discipline is the management of that fight.

```
NAVAL ARCHITECTURE — FULL LANDSCAPE
===============================================================================

  GOVERNING TENSION: Float upright + Resist loads + Move cheaply + Carry payload
  (each pulls the design in a different direction; the naval architect arbitrates)

+-------------------------------------------------------------------------------+
|  WILL IT FLOAT AND STAY UPRIGHT?            ........ HYDROSTATICS / STABILITY |
|    Archimedes, displacement, GM, GZ curve   ........ [01]                     |
+-------------------------------------------------------------------------------+
|  WHAT SHAPE, AND HOW MUCH DOES IT DRAG?     ........ HULL FORM / RESISTANCE   |
|    coefficients, Froude scaling, R = Rf+Rw  ........ [02]                     |
+-------------------------------------------------------------------------------+
|  HOW IS IT PUSHED THROUGH THE WATER?        ........ PROPULSION               |
|    propeller thrust, cavitation, engines    ........ [03]                     |
+-------------------------------------------------------------------------------+
|  WILL THE HULL HOLD TOGETHER?               ........ SHIP STRUCTURES          |
|    hull girder, hogging/sagging, scantlings ........ [04]                     |
+-------------------------------------------------------------------------------+
|  HOW DOES IT BEHAVE IN A SEAWAY?            ........ SEAKEEPING               |
|    6-DOF motions, RAOs, slamming, stabilizers ...... [05]                     |
+-------------------------------------------------------------------------------+
|  WHAT MAKES IT RUN AS A MACHINE?            ........ MARINE SYSTEMS           |
|    power, steering, ballast, HVAC, electrical ...... [06]                     |
+-------------------------------------------------------------------------------+
|  HOW IS IT ACTUALLY BUILT AND CERTIFIED?    ........ SHIPBUILDING             |
|    blocks, welding, classification societies ....... [07]                     |
+-------------------------------------------------------------------------------+
|  WHAT KINDS OF SHIPS EXIST?                 ........ SHIP TYPES               |
|    cargo, tanker, container, passenger, naval ...... [08]                     |
+-------------------------------------------------------------------------------+
|  WHAT ABOUT STRUCTURES THAT DO NOT SAIL?    ........ OFFSHORE ENGINEERING     |
|    platforms, station-keeping, subsea, wind ........ [09]                     |
+-------------------------------------------------------------------------------+
```

Read this top-down as a question cascade: each layer is a question the design must
survive, and each maps to one guide in this module.

---

## Where This Module Sits Relative to Its Neighbors

Naval architecture is an *applied* discipline. It does not re-derive the physics; it
imports results from neighboring fields and specializes them to floating bodies.

```
  fluid-dynamics/  ---->  WATER as a medium
    Navier-Stokes, boundary layers, free-surface waves
    THIS MODULE borrows: drag laws, wave theory, the Froude/Reynolds split
    THIS MODULE adds:    resistance decomposition for hulls, propeller flow

  structural/      ---->  the HULL as a beam
    beam bending, stress, buckling, material mechanics
    THIS MODULE borrows: M = stress x section modulus, Euler buckling
    THIS MODULE adds:    the ship as a box girder, hogging/sagging from waves

  mechanical/      ---->  the SHIP as a machine
    thermodynamic cycles, gears, shafts, bearings
    THIS MODULE borrows: diesel/turbine cycles, shaft design
    THIS MODULE adds:    matching engine to propeller to hull (the power train)

  materials/       ---->  what the hull is MADE of
    steel metallurgy, aluminium alloys, composites, corrosion
    THIS MODULE borrows: yield strength, fatigue, galvanic series
    THIS MODULE adds:    marine-grade selection, cathodic protection of hulls

  transportation/  ---->  the SHIP in a SYSTEM
    logistics, intermodal containers, ports, supply chains
    THIS MODULE borrows: the demand that sizes a ship
    THIS MODULE adds:    the vessel that the logistics network assumes exists
```

The rule of thumb: if a fact is true for any beam, any fluid, or any engine, it
lives in the neighbor module. If it is true specifically for *a hull in water*, it
lives here.

---

## The Three Founding Ideas

Almost everything in this module reduces to three physical insights, each centuries
old, each still exact.

```
+---------------------------------------------------------------------------+
|  1. ARCHIMEDES (c. 250 BC) — buoyancy                                     |
|     A floating body displaces its own weight in water.                    |
|     Weight = Displacement.  This sizes every ship ever built.             |
|     -> guide [01]                                                         |
+---------------------------------------------------------------------------+
|  2. THE METACENTER (Bouguer / Euler, 1740s) — stability                   |
|     A floating body rights itself if the metacenter M is above the        |
|     centre of gravity G. Stability is geometry, not luck.                 |
|     -> guide [01]                                                         |
+---------------------------------------------------------------------------+
|  3. FROUDE'S LAW (William Froude, 1860s-70s) — scaling                    |
|     Wave-making resistance scales by Froude number, not Reynolds.         |
|     This is why you can test a model and predict the full ship.           |
|     -> guide [02]                                                         |
+---------------------------------------------------------------------------+
```

For a reader from the math/physics world: these are not heuristics. Archimedes is a
statement of hydrostatic equilibrium (the integral of pressure over the wetted hull
equals the weight). The metacenter is the instantaneous centre of rotation of the
buoyant force under small heel — a second-order geometric property of the waterplane.
Froude's law is dimensional analysis applied to the free-surface boundary condition.
The discipline is old, but it is exact applied mathematics, not folklore.

---

## The Vocabulary You Must Internalize First

Naval architecture has a dense private vocabulary. Here is the irreducible core; the
rest of the module assumes these.

| Term | Symbol | Meaning |
|------|--------|---------|
| Displacement | Δ (or W) | Weight of water displaced = weight of ship (tonnes) |
| Draft (draught) | T | Depth of hull below the waterline |
| Beam | B | Maximum width of the hull |
| Length between perpendiculars | LBP / LPP | Working length for calculations |
| Freeboard | — | Height of deck above waterline (reserve buoyancy) |
| Trim | — | Difference between forward and aft draft |
| List / Heel | θ | Transverse angle of tilt (list = permanent, heel = momentary) |
| Centre of buoyancy | B | Centroid of the *underwater* volume |
| Centre of gravity | G | Centroid of the ship's *mass* |
| Metacentre | M | Effective pivot of buoyant force under small heel |
| Metacentric height | GM | Distance G to M — the stability stiffness |
| Block coefficient | Cb | Fullness: hull volume ÷ enclosing box |

A note on a confusing collision of letters: **B** is overloaded. It means **beam**
(a length) *and* the **centre of buoyancy** (a point). Context disambiguates: "the
beam is 32 m" vs. "B rises as the ship heels." This module flags it where ambiguous.

---

## The Design Spiral — How a Ship Actually Gets Designed

The single most important process concept in the field. A ship cannot be designed
in one pass because every decision feeds back on every other. You guess, evaluate,
and converge — iterating around a spiral that tightens toward a feasible design.

```
THE DESIGN SPIRAL (read inward; each loop refines the same variables)
===============================================================================

         MISSION / REQUIREMENTS  (carry X tonnes at Y knots over Z range)
                       |
                       v
   .------------------ ESTIMATE displacement & main dimensions (L,B,T,Cb)
   |                            |
   |                            v
   |   .--------------- HYDROSTATICS & STABILITY  (does GM check out?) [01]
   |   |                        |
   |   |                        v
   |   |   .----------- RESISTANCE & POWER  (how much thrust needed?) [02]
   |   |   |                    |
   |   |   |                    v
   |   |   |   .------- PROPULSION  (pick engine + propeller) [03]
   |   |   |   |                |
   |   |   |   |                v
   |   |   |   |   .--- STRUCTURE  (scantlings, weight estimate) [04]
   |   |   |   |   |            |
   |   |   |   |   |            v
   |   |   |   |   |    WEIGHT & COST estimate
   |   |   |   |   |            |
   |   |   |   |   |   does weight = displacement? does cost close?
   |   |   |   |   |            |
   |   |   |   |   |        NO -> loop again (tighter) ------.
   |   |   |   |   |            |                            |
   |   |   |   |   '----<-------+----------------------------'
   |   |   |   '--------<-------'
   |   |   '------------<-------'
   |   '----------------<-------'
   '--------------------<-------'
                       |
                  YES -> CONVERGED feasible design -> detailed engineering
```

Why a spiral and not a checklist? Because the variables are coupled. Adding steel for
strength raises weight, which raises displacement, which raises draft and resistance,
which demands more power, which adds engine weight, which raises displacement again.
The spiral is the field's name for fixed-point iteration on a coupled nonlinear system.

> Old world -> new world bridge. To a software architect this spiral is simply an
> **iterative convergence loop on a system with circular dependencies** — the same
> shape as resolving a coupled build graph or a constraint solver that must reach a
> stable assignment. There is no topological sort because the dependency graph has
> cycles; you relax toward a fixed point instead. The naval architects formalized
> this loop in the 1950s (Evans, 1959), well before software borrowed the idea.

---

## The Two Dimensionless Numbers That Run Everything

Two ratios decide which physics dominates. Internalize the split: they govern
different resistances and *scale differently*, which is the whole basis of model
testing.

```
+----------------------------------+-----------------------------------+
|  REYNOLDS NUMBER  Re = VL/nu     |  FROUDE NUMBER  Fn = V/sqrt(gL)   |
|  ratio: inertia / viscosity      |  ratio: inertia / gravity         |
|----------------------------------|---------------------------------- |
|  governs: FRICTIONAL resistance  |  governs: WAVE-MAKING resistance  |
|  (skin friction on wetted hull)  |  (energy lost making waves)       |
|----------------------------------|---------------------------------- |
|  a full ship has Re ~ 10^9       |  a ship cruises near Fn ~ 0.2-0.3 |
|  (deeply turbulent boundary lyr) |  (the "hull speed" regime)        |
|----------------------------------|---------------------------------- |
|  CANNOT match Re in a small      |  CAN match Fn in a small model:   |
|  model AND the real ship at once |  scale speed by sqrt(scale).      |
+----------------------------------+-----------------------------------+
        |                                          |
        '------------------+-----------------------'
                           v
        FROUDE'S INSIGHT: you cannot match both at model scale,
        so SPLIT the resistance. Scale wave-making by Froude (the
        model gives it directly); compute friction separately from
        a flat-plate formula at each scale. Detail in guide [02].
```

This Reynolds/Froude split (see `fluid-dynamics/00-OVERVIEW.md` for the general
dimensionless-number framework) is the founding methodological trick of the field
and the reason towing tanks work.

---

## A Worked Anchor: Sizing a Ship in One Line

To make the abstractions concrete, here is the equation that begins every design.
Archimedes, written as an engineering identity:

```
   Displacement  =  rho  x  g  x  (underwater volume)
        Delta    =  rho  x  g  x  V_displaced

   For seawater, rho ~ 1025 kg/m^3.

   A box-like hull:   V_displaced  =  Cb x L x B x T
   so                 Delta        =  rho x g x Cb x L x B x T
```

Numbers: a container ship with L = 300 m, B = 40 m, T = 14 m, Cb = 0.65.

```
   V = 0.65 x 300 x 40 x 14            = 109,200 m^3
   mass displaced = 1025 x 109,200     = 111.9 x 10^6 kg = ~111,900 tonnes
```

That ~112,000 tonnes is *everything*: steel hull + machinery + fuel + cargo +
crew. Every other design choice spends against this budget. (We used mass-tonnes
here; multiplying by g gives the buoyant force in newtons. Naval architects usually
speak in tonnes of displacement and let g cancel.)

---

## The Whole Module on One Page

| Guide | Core question | The one equation / idea to remember |
|-------|---------------|-------------------------------------|
| [01] Hydrostatics & Stability | Will it float upright? | GZ = GM·sinθ; right if M above G |
| [02] Hull Form & Resistance | What shape, how much drag? | R = Rf + Rw + Rform; Froude scaling |
| [03] Propulsion | How is it pushed? | T(1−t) = R; avoid cavitation |
| [04] Ship Structures | Will it hold together? | Hull = box girder; hogging/sagging |
| [05] Seakeeping | How does it behave in waves? | 6-DOF motions; RAO = response/wave |
| [06] Marine Systems | What makes it run? | Generation + distribution onboard |
| [07] Shipbuilding | How is it built & certified? | Block assembly; class society rules |
| [08] Ship Types | What kinds exist? | Form follows cargo |
| [09] Offshore Engineering | What doesn't sail? | Station-keeping replaces propulsion |

---

## Common Confusion Points

### "Tonnage" does not mean weight

This trips up everyone. The word "tonnage" usually means **volume**, not weight.

```
  DISPLACEMENT tonnage  = actual WEIGHT of the ship (Archimedes). A force.
  GROSS tonnage (GT)    = a measure of internal VOLUME (dimensionless number).
  NET tonnage (NT)      = volume of revenue-earning (cargo) spaces.
  DEADWEIGHT (DWT)      = WEIGHT the ship can carry (cargo+fuel+stores+crew).
```

GT and NT are unitless capacity measures used for dues and regulation. Deadweight
and displacement are weights. A "100,000 GT cruise ship" and a "100,000 DWT tanker"
are described by completely different quantities. Detail in guides [01] and [08].

### "Naval architecture" vs. "marine engineering"

```
  NAVAL ARCHITECTURE  = the SHIP itself: hull form, stability, structure,
                        resistance, seakeeping. "Will it float, move, survive?"

  MARINE ENGINEERING  = the SYSTEMS inside: propulsion plant, power, piping,
                        auxiliaries. "What makes it go and keeps it running?"
```

They are two halves of one design office and overlap heavily. This module covers
both; guides [01]-[05], [08] lean naval-architecture, [03], [06], [09] lean
marine-engineering.

### Why not just import everything from fluid-dynamics and structural?

Because the *combination* creates problems neither parent owns. A wave both pushes the
hull (a fluid load) and bends it as a beam (a structural response) and rocks it
(a rigid-body motion) — simultaneously, coupled. The coupling is the discipline.
Resistance is not "drag from `fluid-dynamics/`"; it is a specific three-way split
under a scaling law that only matters for free-surface bodies.

---

## Decision Cheat Sheet

| I want to know... | Go to guide |
|---|---|
| Whether a loaded ship will capsize | [01] Hydrostatics & Stability |
| Why a fuller hull costs more power | [02] Hull Form & Resistance |
| How to pick a propeller and avoid cavitation | [03] Propulsion |
| Why ships break in half in storms | [04] Ship Structures |
| How to keep passengers from being seasick | [05] Seakeeping |
| What generates the electricity onboard | [06] Marine Systems |
| How a 300 m hull is welded together | [07] Shipbuilding |
| The difference between a tanker and a bulker | [08] Ship Types |
| How an oil platform stays in one spot | [09] Offshore Engineering |
| The general physics of water as a fluid | `fluid-dynamics/` |
| Beam bending and material stress in general | `structural/` |
| Diesel and turbine cycles in general | `mechanical/` |
