---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "04-SHIP-STRUCTURES.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:ship-structures
kind: guide
module: naval-architecture
section: naval-architecture
title: Ship Structures
status: source-custody
source_custody: partial
current_path: naval-architecture/04-SHIP-STRUCTURES.md
canonical_path: naval-architecture/04-SHIP-STRUCTURES.md
backsource_ids: [proof-backfill:naval-architecture:04-ship-structures, git-history:naval-architecture:04-ship-structures]
concepts: [hull girder, longitudinal strength, hogging, sagging, scantlings, marine materials]
root_concepts: [ship structures]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Ship Structures

## The Big Picture

A ship hull is, structurally, a giant hollow box-section beam — a **box girder** —
floating on a support (buoyancy) that is distributed unevenly along its length and that
changes second by second as waves pass. The structural problem is to make this beam strong
enough to resist bending, shear, and local pressure for 25 years of corrosion and millions
of wave-induced load cycles, while being as light as possible (every tonne of steel is a
tonne of lost cargo). This guide applies the beam mechanics of `structural/` to the
specific, hardest case: a beam that is also the buoyant body it must support.

```
THE SHIP AS A HULL GIRDER
===============================================================================

   Forget the details: the whole ship is ONE big beam in bending.

        WEIGHT acts DOWN, unevenly (cargo here, engine there, empty there)
         |    |       | | |          |      |
         v    v       v v v          v      v
   .=======================================================.   <- the hull
   |                THE HULL = A BOX GIRDER                 |      (a beam)
   '======================================================='
         ^    ^   ^      ^      ^   ^     ^      ^    ^
         |    |   |      |      |   |     |      |    |
        BUOYANCY acts UP, also unevenly (depends on hull shape + waves)

   Where weight > buoyancy locally -> the beam wants to sag there.
   Where buoyancy > weight locally -> the beam wants to hog there.
   The MISMATCH between the weight curve and buoyancy curve = the load
   that bends the entire ship. Integrate it twice -> bending moment.
```

The entire longitudinal-strength problem is this: weight and buoyancy are both
distributed along the length but *not in the same way*, and their difference bends the
ship. Everything else is bookkeeping on that idea.

---

## Layer 1: Longitudinal Strength — Hogging and Sagging

Sum weight and buoyancy at each station along the length. Their difference is the **load
curve** q(x). Integrate q(x) once to get the **shear force** Q(x); integrate again to get
the **bending moment** M(x). This is ordinary Euler-Bernoulli beam theory (`structural/`),
applied to a floating beam. The two extreme load cases have names.

```
HOGGING vs SAGGING (the two governing wave conditions)
===============================================================================

   HOGGING: wave CREST amidships          SAGGING: wave TROUGH amidships
   (extra buoyancy in the middle)         (extra buoyancy at the ends)

        ___---^^^---___  wave crest             wave              wave
       /               \                       crest             crest
   ~~~/~~~~~~~~~~~~~~~~~~\~~~ surface       ~~~\~~~~~~~~~~~~~~~~~~/~~~ surface
   +===================+         +===================+
   |  hull bends DOWN  |         |  \  trough   /    |
   |  at the ends      |         |   \________/      |
   +===================+         +===================+
    ends droop, middle up                  ends up, middle droops
    DECK in TENSION                         DECK in COMPRESSION
    BOTTOM in COMPRESSION                   BOTTOM in TENSION
```

```
   The beam relations (exactly as in structural/, applied to the hull):

        load:     q(x) = buoyancy(x) - weight(x)        [force / length]
        shear:    Q(x) = integral of q(x) dx
        moment:   M(x) = integral of Q(x) dx            (max amidships, usually)

        bending stress:   sigma = M / Z
        where Z = SECTION MODULUS = I / y
          I = second moment of area of the hull cross-section
          y = distance from neutral axis to the deck (or keel)
```

The headline design equation is **σ = M / Z**: the bending stress in the deck or bottom
equals the bending moment divided by the section modulus. Design controls two things: keep
M down (it is largely fixed by ship size and the sea, though loading discipline matters) and
make Z big (concentrate steel far from the neutral axis — the deck and bottom — exactly
where a wide-flange I-beam puts its material).

```
WHY THE STEEL GOES TOP AND BOTTOM (section modulus, applied)
===============================================================================

   The hull cross-section is a hollow box. Bending stress is
   PROPORTIONAL TO DISTANCE from the neutral axis. So:

        +=================+  <- STRENGTH DECK: thick plate, far from N.A.
        |                 |     -> carries the most stress, gets the most steel
        |                 |
        | - - - - - - - - |  <- NEUTRAL AXIS (zero bending stress)
        |                 |
        |                 |
        +=================+  <- BOTTOM/KEEL: thick plate, far from N.A.
                                -> double bottom here (also damage protection)

   Material near the neutral axis does almost nothing for bending strength.
   So the sides are thinner; the deck and bottom are thick. The whole hull
   is an I-beam wrapped into a closed box.
```

---

## Layer 2: The Structural Hierarchy — Three Scales of Strength

Ship structure is checked at three nested scales. A design can pass the global check and
still fail locally, so all three matter.

```
THE THREE LEVELS OF STRUCTURAL RESPONSE
===============================================================================

  +-----------------------------------------------------------------------+
  | PRIMARY (the whole hull girder)                                       |
  |   the entire ship as one beam in hogging/sagging.                     |
  |   Failure mode: the ship breaks in half. Governed by sigma = M/Z.     |
  +-----------------------------------------------------------------------+
              | zoom in
              v
  +-----------------------------------------------------------------------+
  | SECONDARY (a panel between bulkheads / decks)                         |
  |   a stiffened plate panel (e.g. a section of deck or side) bending    |
  |   under local pressure between its supports.                          |
  |   Failure mode: panel yields or buckles.                              |
  +-----------------------------------------------------------------------+
              | zoom in
              v
  +-----------------------------------------------------------------------+
  | TERTIARY (one plate between stiffeners)                               |
  |   a single plate "field" bending under local water/cargo pressure.    |
  |   Failure mode: local yield, dishing, or fatigue cracking at welds.   |
  +-----------------------------------------------------------------------+

   The three stresses SUPERPOSE. A spot on the deck carries primary
   (hull bending) + secondary (panel bending) + tertiary (plate bending)
   stress at once. The sum must stay below yield with a margin.
```

This superposition is why a ship can be globally fine yet crack locally: the tertiary
stress at a weld toe, riding on top of the primary deck stress, is where fatigue cracks
nucleate. The neutral-axis material that does nothing for primary strength may still be
working hard at the secondary or tertiary scale.

> Old world -> new world bridge. The three scales are a structural analog of separation of
> concerns: a global invariant (the hull girder must not break) plus local invariants
> (each panel, each plate) that must each hold, with their stresses *composing* rather than
> being independent. Verifying the system means checking every level and their sum — you
> cannot prove the whole safe by proving only the global property, the same way passing an
> integration test does not discharge the unit-level obligations.

---

## Layer 3: Buckling — The Compression Failure That Matters Most

Steel is roughly as strong in tension as compression at the *material* level, but a thin
plate or panel in compression fails by **buckling** — sideways collapse — long before it
reaches yield stress. Because the deck is in compression during sagging and the bottom
during hogging, buckling, not yield, is frequently the governing failure mode for the hull
girder.

```
BUCKLING — WHY THIN PLATES IN COMPRESSION ARE THE WEAK LINK
===============================================================================

   push a thin plate edge-on:           critical (Euler-type) stress:

   ====>  | flat |  <====               sigma_cr ~ k x E x (t/b)^2
          |      |                       t = plate thickness
          | bows |   ->  buckles         b = unsupported width
          | out  |       sideways at     E = Young's modulus
   ====>  |______|  <==== a stress       k = edge-condition factor
                         BELOW yield

   Defense = STIFFENERS: weld T-bars/angles to break a big panel into
   many narrow ones. Halving b QUADRUPLES sigma_cr (the (t/b)^2 term).

   +---+---+---+---+---+   each bay is narrow -> high buckling stress
   |   |   |   |   |   |   the stiffeners carry compression as columns
   +---+---+---+---+---+   (themselves checked for column buckling)
   stiffened panel (the universal ship structural element)
```

This is why ship structure is *stiffened plate* everywhere — the entire hull is plates
broken into small bays by a grid of stiffeners, frames, and girders. Buckling resistance
goes as (t/b)², so subdividing a panel (shrinking b) is a far cheaper way to gain strength
than thickening the plate (raising t). The same Euler buckling physics from `structural/`
governs, here in two dimensions for plates.

---

## Layer 4: Framing Systems — How the Grid Is Arranged

The stiffeners can run mostly *along* the ship or mostly *across* it. The choice is one of
the oldest design decisions and it follows from Layer 1: longitudinal stress dominates, so
stiffen longitudinally where you can.

```
+--------------------------+--------------------------+
| TRANSVERSE FRAMING       | LONGITUDINAL FRAMING     |
|--------------------------|--------------------------|
| ribs run ACROSS the ship | stiffeners run ALONG it  |
|   | | | | | | | | |      |   ===============        |
|   ribs like a rib cage   |   long stringers + few   |
|   closely spaced frames  |   heavy transverse webs  |
|--------------------------|--------------------------|
| simple, good for SHORT   | resists HULL-GIRDER      |
| ships and local loads    | bending efficiently      |
| weaker against global    | (steel aligned with the  |
| bending; more steel for  | primary stress) -> less  |
| same longitudinal Z      | steel for the same Z     |
|--------------------------|--------------------------|
| barges, small craft,     | long ships: tankers,     |
| ice belts                | bulkers, container ships |
+--------------------------+--------------------------+
       |                              |
       '----------> COMBINED / "framing system" <------'
        Most large ships: longitudinal in deck & bottom (where
        primary stress lives) + transverse webs + transverse
        framing in the side shell. Best of both.
```

The dominant modern choice for large ships is **longitudinal framing** in the deck and
bottom (aligning the steel with the primary bending stress) tied together by widely-spaced
heavy transverse web frames. The double bottom and (in tankers) double sides are deep
girder structures that both carry load and provide a second skin against grounding and
collision.

---

## Layer 5: Fatigue and the 25-Year Sea

A ship does not see one load; it sees ~10⁸ wave cycles over its life. Even stresses well
below yield will, repeated enough, grow a crack from a weld defect to failure. **Fatigue**
is therefore a primary design check, especially at structural details — hatch corners,
weld toes, bracket terminations — where stress concentrates.

```
FATIGUE — DEATH BY A HUNDRED MILLION WAVES
===============================================================================

   S-N curve (stress range vs cycles to failure), log-log:

   stress |
   range  |\
   (S)    | \                       fatigue is governed by stress RANGE,
          |  \                      not peak stress. Each wave = one cycle.
          |   \____                 Welds have notches -> stress concentration
          |        \____            -> cracks start there.
          |             \_______
          |                     \________  endurance limit (steel, in air)
          +------------------------------------> cycles N (log scale)
          10^4    10^6    10^8

   But SEAWATER removes the endurance limit (corrosion fatigue):
   cracks keep growing no matter how low S is. Hence: good weld details,
   grinding weld toes smooth, generous radii at hatch corners, and
   CORROSION PROTECTION are structural requirements, not finishing.
```

The brittle-fracture lesson is historical and concrete: the WWII **Liberty ships** cracked
in half, sometimes in harbor, because their continuous-welded hulls let a crack run
unimpeded through steel that turned brittle in cold water (the steel's ductile-to-brittle
transition temperature was too high). The fixes — tougher notch-tested steel, crack-arrest
strakes, riveted seams as crack stoppers — are why modern hull steel is specified by
**Charpy impact toughness** at service temperature, not strength alone. (Fracture
mechanics and the ductile-brittle transition belong to `materials/`; here they are a
hard design constraint.)

---

## Layer 6: Marine Materials

What the hull is made of. The choice trades strength, weight, cost, corrosion, and
fabrication. (Metallurgy lives in `materials/`; this is the marine selection lens.)

| Material | Strength/weight | Corrosion | Where used | Key issue |
|----------|-----------------|-----------|------------|-----------|
| Mild / HT steel | Moderate (heavy) | Poor — must coat & protect | 99% of large ships | Cheap, weldable, fatigue/corrosion |
| High-tensile steel | Better | Poor | Decks, highly-stressed zones | Lets plates be thinner — but thinner buckles more easily |
| Aluminium alloy | High (light) | Good (oxide layer) | Superstructures, fast ferries, navy | Soft at fire temps; galvanic w/ steel |
| GRP / composite | High (light) | Excellent | Minehunters, yachts, small craft | Cost, no magnetic signature (a feature for navy) |
| Stainless / duplex | Moderate | Excellent | Chemical tanks, piping | Expensive |
| Concrete | Low | Excellent | Some barges, offshore gravity bases | Very heavy, niche |

Two recurring marine-specific problems:

```
   CORROSION: steel + seawater + oxygen = rust. Defenses, layered:
     - coatings (paint systems) -- the first line
     - sacrificial anodes (zinc/aluminium) -- galvanic protection:
       a less-noble metal corrodes INSTEAD of the hull (see galvanic series)
     - impressed current cathodic protection (ICCP) -- drive the hull
       cathodic with an applied current
     - corrosion allowance: extra mm of steel the rules add, sacrificed
       to a known wastage rate over the ship's life

   GALVANIC TRAP: bolt aluminium to steel in seawater and the aluminium
   (less noble) corrodes fast. Mixed-metal joints must be electrically
   isolated. The galvanic series (materials/) is law at sea.
```

Cathodic protection is straight electrochemistry: make the hull the cathode of a cell so a
sacrificial anode (or impressed current) corrodes in its place. The galvanic series from
`materials/` is not academic here — it dictates which metals may touch.

---

## Worked Example: Longitudinal Strength Check

A bulk carrier amidships. Verify the deck stress in hogging is safe.

```
   GIVEN (amidships section, hogging condition):
     Still-water bending moment  M_sw = 1.20 x 10^9 N.m  (loading-dependent)
     Wave bending moment         M_w  = 2.40 x 10^9 N.m  (rule wave, hogging)
     Section modulus to deck     Z    = 18.0 m^3
     Steel yield strength        sigma_y = 315 MPa (HT steel)

   STEP 1 -- total design bending moment (still water + wave, same sign):
     M = M_sw + M_w = 1.20e9 + 2.40e9 = 3.60 x 10^9 N.m

   STEP 2 -- bending stress at the deck:
     sigma = M / Z = 3.60e9 / 18.0 = 2.00 x 10^8 Pa = 200 MPa

   STEP 3 -- compare to allowable (rule allowable ~ 0.75 sigma_y typical):
     sigma_allow = 0.75 x 315 = 236 MPa
     200 MPa < 236 MPa  -> PASS, with ~18% margin.

   STEP 4 -- but the DECK is in TENSION in hogging, so yield governs there;
     the BOTTOM is in COMPRESSION -> must ALSO check buckling:
     compare 200 MPa (bottom compressive) against sigma_cr of the bottom
     stiffened panels. If sigma_cr < 200 MPa, the bottom buckles first ->
     add stiffeners or thicken plate even though yield was satisfied.

   STEP 5 -- fatigue: take the stress RANGE between hogging and sagging at a
     hatch corner (a stress-concentration detail) and check against the S-N
     curve for ~10^8 cycles in seawater. This often governs the DETAIL design
     even when the primary stress passes comfortably.
```

The structural lesson in one line: passing the yield check (Step 3) does *not* finish the
job — buckling (Step 4) and fatigue (Step 5) are separate gates, and on real ships they
frequently govern.

---

## Common Confusion Points

### Hogging and sagging — which way does the deck go?

```
   HOGGING (crest amidships): ship arches UP in the middle
            -> DECK stretched -> TENSION;  bottom squeezed -> COMPRESSION
   SAGGING (trough amidships): ship droops in the middle
            -> DECK squeezed  -> COMPRESSION; bottom stretched -> TENSION
```

The mnemonic: a "hog's back" arches up. Hogging puts the deck in tension. Get this backward
and you check the wrong failure mode (yield vs. buckling) in the wrong place.

### Section modulus Z is not the same as moment of inertia I

```
   I = second moment of area (m^4) -- governs DEFLECTION (stiffness)
   Z = I / y = section modulus (m^3) -- governs STRESS (strength)
```

Strength checks use Z; stiffness/deflection checks use I. Concentrating steel far from the
neutral axis raises both, but Z is the one in σ = M/Z.

### Higher-strength steel does not automatically mean a stronger ship

High-tensile steel lets you use *thinner* plate for the same yield stress — but thinner
plate buckles more easily and is more fatigue- and corrosion-sensitive (less metal to
sacrifice). Substituting HT steel can shift the governing failure mode from yield to
buckling or fatigue. Strength is not a scalar you simply turn up.

### Still-water bending moment is not zero

Even in a flat calm, uneven loading (heavy cargo in some holds, fuel in others) bends the
hull. The total design moment is still-water + wave. Bad cargo distribution can overstress a
hull in port — which is why loading computers enforce a bending-moment limit during cargo
operations.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Model the whole ship's bending | Hull girder: σ = M/Z |
| Get the bending load | q = buoyancy − weight; integrate twice |
| Identify the worst wave condition | Hogging (crest) and sagging (trough) |
| Increase hull-girder strength | Raise section modulus Z (steel in deck/bottom) |
| Resist compression failure | Buckling check; add stiffeners (b↓ → σ_cr↑) |
| Choose how to arrange stiffeners | Longitudinal framing for long ships |
| Ensure 25-year life | Fatigue (S-N) at weld/detail stress ranges |
| Pick hull material | Steel default; Al/composite for light/special |
| Stop the hull from rusting | Coatings + sacrificial anodes / ICCP |
| Avoid mixed-metal corrosion | Galvanic series; isolate dissimilar metals |
| Review general beam/buckling theory | `structural/` |
| Review metallurgy & fracture mechanics | `materials/` |
