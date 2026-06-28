---
maxim_schema: maxim.frontmatter.v1
id: maxim:naval-architecture:hydrostatics-and-stability
kind: guide
module: naval-architecture
section: naval-architecture
title: Hydrostatics and Stability
status: source-custody
source_custody: partial
current_path: naval-architecture/01-HYDROSTATICS-AND-STABILITY.md
canonical_path: naval-architecture/01-HYDROSTATICS-AND-STABILITY.md
backsource_ids: [proof-backfill:naval-architecture:01-hydrostatics-and-stability, git-history:naval-architecture:01-hydrostatics-and-stability]
concepts: [buoyancy, metacentric height, righting arm, stability curve, hydrostatics]
root_concepts: [hydrostatics, stability]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Hydrostatics and Stability

## The Big Picture

A ship floats because the water pushes up exactly as hard as gravity pulls down.
It stays *upright* for a different and subtler reason: when it tilts, the shape of
the underwater volume changes, the upward push shifts sideways, and that shift creates
a torque that rights the ship. Hydrostatics is the study of the floating ship at rest;
stability is the study of whether it returns to upright after a disturbance. Both are
exact geometry — the most rigorous, most settled part of the whole field.

```
THE TWO QUESTIONS OF HYDROSTATICS
===============================================================================

+---------------------------------------+---------------------------------------+
|  Q1: DOES IT FLOAT?                   |  Q2: DOES IT STAY UPRIGHT?            |
|  (vertical equilibrium)               |  (rotational equilibrium)             |
|                                       |                                       |
|        weight W (down)                |   tilt by theta, then ask:            |
|            |                          |   does a RIGHTING torque appear?      |
|            v                          |                                       |
|    ~~~~~~~~~~~~~~~~~ waterline        |   ~~~~~~~~/~~~~~~~ heeled waterline   |
|    '.              .'                 |     '.   M . pivot                    |
|      '.   hull   .'                   |       '.  /|\                         |
|        '.      .'                     |        'G | '.  <- G fixed in ship    |
|          '.__.'                       |          '. |B' '.  <- B to low side  |
|            ^                          |            '|    '.                   |
|            |                          |             '.___ '.                  |
|     buoyancy Fb (up)                  |      W down vs Fb up = a couple       |
|                                       |                                       |
|   FLOATS when  Fb = W                 |   RIGHTS when  M is ABOVE G           |
+---------------------------------------+---------------------------------------+
```

Q1 is Archimedes. Q2 is the metacenter. Get these two right and you have understood
80% of why ships are shaped the way they are.

---

## Layer 1: Archimedes and Vertical Equilibrium

Archimedes' principle, stated as the engineering identity that begins every design:

```
   Buoyant force  =  weight of displaced fluid
        Fb        =  rho_water  x  g  x  V_submerged

   At rest, vertical equilibrium demands  Fb = W (the ship's weight), so:

        W  =  rho  x  g  x  V_submerged
```

The buoyant force is not magic — it is the resultant of hydrostatic pressure acting
over the wetted hull. Pressure grows with depth (p = ρgh), so the bottom of the hull
is pushed up harder than the top is pushed down. Integrating that pressure over the
closed wetted surface yields a net upward force equal to ρg times the enclosed volume,
acting through the centroid of that volume. That centroid is the **centre of buoyancy, B**.

```
PRESSURE INTEGRAL -> BUOYANT FORCE (why Archimedes is exact, not a rule of thumb)
===============================================================================

   sea surface  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                 small p here     |     |     small p
                       \          v     v          /
                        .-------------------------.
   deep -> big p ->  => |        HULL VOLUME      | <= => big p
                        |     (displaces water)   |
                        '-------------------------'
                       /          ^     ^          \
                 big p here       |     |       big p here
                 (net UP because bottom pressure > top pressure)

   Resultant = rho g V, acting up through B (centroid of submerged volume).
```

### Reading the hydrostatic curves

Naval architects pre-compute how all of this varies with draft and store it as the
**hydrostatic curves** (also "hydrostatic particulars"). Push the ship deeper and
every quantity changes; the curves tabulate them so you never re-integrate.

| Curve | Symbol | What it tells you |
|-------|--------|-------------------|
| Displacement vs draft | Δ(T) | How heavy the ship is at each waterline |
| Centre of buoyancy (vertical) | KB | Height of B above keel |
| Centre of buoyancy (long.) | LCB | Fore-aft position of B (sets trim) |
| Waterplane area | Aw | Area of the slice at the waterline |
| Tonnes per cm immersion | TPC | Weight to push the ship 1 cm deeper |
| Metacentric radius | BM | How high M sits above B (see Layer 2) |
| Moment to change trim 1 cm | MCT1cm | Trimming stiffness |

```
   TPC (tonnes per centimetre) — the most-used hydrostatic number:

        TPC = rho x Aw / 100        (Aw = waterplane area in m^2, rho in t/m^3)

   Add 500 t of cargo, divide by TPC -> sinkage in cm. That simple.
```

---

## Layer 2: The Metacenter — Why a Ship Rights Itself

This is the crown jewel. When a ship heels by a small angle θ, the underwater shape
becomes asymmetric: a wedge of buoyancy emerges on the high side and an equal wedge
immerges on the low side. The centre of buoyancy B migrates toward the low (immersed)
side, to a new point B'. The line of action of the buoyant force, drawn vertically up
through B', intersects the ship's centerline at a point called the **metacenter, M**.

```
THE METACENTER GEOMETRY (small-angle heel)
===============================================================================

                         . M   <- metacenter: where the new buoyancy
                        /|\        line crosses the centerline
                       / | \
                      /  |  \
                upright  |   \
              buoyancy   |    \
                line     G  <- centre of gravity (fixed in the ship)
                      |  |\    \
                      |  | \    \
                  ~~~~|~~|~~\~~~~|~~~~ heeled waterline
                    \ |  |   \   |  /
                     \|  B    \ B' <- buoyancy shifts to low side
                      \  |     \| /
                       \ +------+ /     KB = height of B above keel K
                        \|      |/      BM = height of M above B
                         +------+       KM = KB + BM
                            K  <- keel (reference datum)
```

The key vertical distances, all measured from the keel K:

```
   KB  = height of centre of buoyancy above keel   (from hydrostatics)
   BM  = metacentric radius = I_T / V              (the magic term, below)
   KM  = KB + BM = height of metacenter above keel
   KG  = height of centre of gravity above keel    (from the weight estimate)

   GM  = KM - KG  = metacentric height  <-- THE stability number
```

### The metacentric radius BM = I_T / V

The single most elegant formula in ship stability. The height of the metacenter
above the centre of buoyancy is the **transverse second moment of area of the
waterplane** divided by the **displaced volume**:

```
        BM  =  I_T / V

   I_T = transverse moment of inertia of the waterplane about the
         centerline = integral of x^2 dA over the waterplane area
   V   = submerged volume (displacement / rho)
```

Why this matters intuitively: I_T grows with the **cube of beam** (a wide waterplane
has a huge second moment), so widening a ship dramatically raises M and stiffens
stability. This is the mathematical reason barges and catamarans are extremely stable
and why narrow racing hulls are tender. For a reader from the math side: I_T is the
same areal second moment that appears in beam bending (`structural/`); here it is taken
about the centerline of the *waterplane slice*, and BM is its first appearance of the
"wide is stable" principle.

> Old world -> new world bridge. BM = I_T/V is a sensitivity: it is the derivative of
> the buoyancy-line position with respect to heel, exactly as a Jacobian term tells you
> how an output shifts per unit input. M is the linearization point — valid for small
> θ, breaks down at large angles, which is why we need the full GZ curve (Layer 3).

### GM — the stability stiffness

**Metacentric height GM = KM − KG** is the distance from the centre of gravity to the
metacenter. It is the *stiffness* of the ship in roll.

```
   GM > 0   M above G   -> STABLE. Disturbance creates a righting torque.
   GM = 0   M at G       -> NEUTRAL. Ship sits at any small angle (dangerous).
   GM < 0   M below G    -> UNSTABLE. Disturbance creates a CAPSIZING torque;
                            ship "lolls" to a heeled angle of equilibrium.
```

```
+-------------------+-------------------+-------------------+
|   STABLE (GM>0)   |  NEUTRAL (GM=0)   |  UNSTABLE (GM<0)  |
|-------------------|-------------------|-------------------|
|        M          |                   |        G          |
|        |          |       M = G       |        |          |
|        G          |        .          |        M          |
|     righting      |     no torque     |    overturning    |
|     returns it    |   stays heeled    |   loll / capsize  |
+-------------------+-------------------+-------------------+
```

Typical GM values: a cargo ship runs GM ≈ 0.5–2 m. Too small (< 0.15 m) and it is
unsafe; too large and it is *stiff* — it snaps back so violently that the roll is
short-period and brutal, wrecking cargo and crew comfort. Stability is a Goldilocks
problem, not a maximization (see Common Confusion Points).

---

## Layer 3: The Righting Arm GZ and the Stability Curve

GM only describes *small* angles. At a real heel of 20°, 40°, 60°, the metacenter
moves and the linear picture fails. The exact quantity is the **righting arm GZ**:
the horizontal distance between the line of gravity (down through G) and the line of
buoyancy (up through B'). The product of GZ and the displacement is the righting moment.

```
THE RIGHTING ARM GZ (the exact, large-angle quantity)
===============================================================================

                    G------>Z          GZ = horizontal lever between the
                    |       |                weight line and buoyancy line
              W down|       |Fb up
                    v       ^           Righting moment = W x GZ = Delta x GZ
              ~~~~~~|~~~~~~~|~~~~~~ heeled waterline
                    |       |
                    G'      B'
                  (gravity)(buoyancy)

   Small-angle approximation:   GZ  ~=  GM x sin(theta)
   (valid only while M is effectively fixed, roughly theta < 7-10 deg)
```

The headline formula, exactly as a naval architect writes it for small angles:

```
        GZ  =  GM x sin(theta)            (small-angle righting arm)
        Righting moment  =  Delta x GZ  =  Delta x GM x sin(theta)
```

At large angles GZ must be computed directly from the cross-sectional geometry at each
heel — it is no longer GM·sinθ. Plotting GZ against heel angle gives the **GZ curve**
(the "curve of statical stability"), the single most important diagram in stability.

```
THE GZ CURVE (curve of statical stability)
===============================================================================

  GZ
  (m) |
 0.8 -|                 ___ GZ_max (peak righting arm)
      |              .-'   '-.
 0.6 -|            .'         '.
      |          .'             '.
 0.4 -|        .'                 '.
      |      .'  <- slope here =     '.
 0.2 -|    .'      GM (deg->rad)       '.
      |  .'                              '.
 0.0 -+-'----------------------------------'------> heel angle theta
      0    10    20    30    40    50    60   70 (deg)
      |<-- area = dynamic stability (energy) -->|  ^
                                                   |
                                  angle of vanishing stability (AVS):
                                  GZ returns to zero -> ship capsizes beyond this
```

What the GZ curve tells you, all at once:

| Feature of the curve | Physical meaning |
|----------------------|------------------|
| Initial slope at θ=0 | Equals GM (in radians) — the small-angle stiffness |
| Peak value GZ_max | Largest steady heeling moment the ship can resist |
| Angle of GZ_max | Heel at which righting ability is greatest |
| Angle of vanishing stability (AVS) | Beyond this, GZ < 0 — capsize |
| Area under the curve | **Dynamic stability** — energy to capsize the ship |

The area under the curve is critical: a sudden gust or a breaking wave delivers
*energy*, not a static moment. The ship survives if the area (work the righting moment
can do) exceeds the energy the disturbance injects. This is why regulators (IMO) specify
minimum *areas* under the GZ curve, not just a minimum GM.

> Old world -> new world bridge. The GZ curve is a one-dimensional potential-energy
> well in disguise. Righting moment = −dE/dθ, so the area under GZ is the depth of the
> energy well, and AVS is the saddle point where the well opens and the ship rolls over
> the barrier. Anyone who has reasoned about basins of attraction in a dynamical system
> (see `dynamical-systems/`) already understands capsize: it is escape from a potential
> well. Calm-water stability is the static well; `seakeeping/` [05] adds the dynamics.

---

## Layer 4: Free Surface Effect — The Hidden Stability Killer

A tank that is *partly* full of liquid is far more dangerous than a full or empty one.
As the ship heels, the liquid in a slack tank flows to the low side, shifting weight in
the wrong direction and *reducing effective GM*. This is the **free surface effect**,
and it has sunk ships that were nominally stable.

```
FREE SURFACE EFFECT
===============================================================================

   FULL or EMPTY tank:               SLACK (partly full) tank:
   liquid cannot shift               liquid sloshes to low side on heel

   .-----------.                     .-----------.
   |###########|  <- solid           |        ###|  <- liquid runs
   |###########|     no shift         |     ######|     downhill,
   |###########|                     |  #########|     moving G the
   '-----------'                     '-----------'     WRONG way

   Virtual rise of G:   GG' = i / V     (i = moment of inertia of the
                                          free liquid surface, per tank)

   Effective metacentric height:  GM_fluid = GM_solid - sum(i/V)
```

The correction is a *virtual* rise of G by i/V per tank, where i is the second moment
of the free liquid surface — note the same I/V form as BM, now working *against* you.
Because i scales with the cube of the tank's breadth, one wide slack tank is far worse
than two narrow ones of the same volume. This is the entire reason large tanks are
subdivided by longitudinal bulkheads. It is also why you never leave many tanks slack:
each one steals from GM, and the losses add.

---

## Layer 5: Damage Stability — Floating After Flooding

Intact stability assumes a watertight hull. **Damage stability** asks: if a compartment
floods, does the ship survive? Modern ships are designed to a damage standard — they
must remain afloat and stably upright with one or more compartments open to the sea.

```
SUBDIVISION & DAMAGE STABILITY
===============================================================================

   A long open hold = one breach floods everything = sink.
   Watertight bulkheads divide the hull into compartments:

   .----+----+----+----+----+----+----+----.
   | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |   <- transverse bulkheads
   '----+----+----+----+----+----+----+----'
              XXXX  <- C3 holed and flooded
   The ship sinks deeper and trims, but C2 and C4 bulkheads
   contain the water. Reserve buoyancy (freeboard) keeps it afloat.

   "One-compartment ship": survives ANY single compartment flooded.
   "Two-compartment ship": survives any two adjacent flooded (e.g. passenger).
```

Two methods describe a flooded compartment: **lost buoyancy** (the flooded volume no
longer provides buoyancy, so the ship sinks to find more) and **added weight** (treat
the floodwater as cargo). They give the same final waterline by different bookkeeping.
The Titanic is the canonical lesson: its bulkheads did not extend high enough, so as
the bow sank, water spilled over the tops from one compartment to the next — a
progressive flooding cascade the subdivision could not contain.

The modern standard is **probabilistic damage stability** (SOLAS): rather than a fixed
"survive N compartments," it computes an *attained subdivision index A* (probability of
surviving a random breach, integrated over breach location and extent) that must exceed
a *required index R*. This is a risk-based reframing of a deterministic rule — the same
move insurance and reliability engineering made.

---

## Worked Example: Full Stability Check

A small cargo ship. Verify it is stable and find its righting moment at 10° heel.

```
   GIVEN:
     Displacement   Delta = 8,000 t   (so V = 8000/1.025 = 7,805 m^3)
     Beam           B = 18 m
     Waterplane I_T = 95,000 m^4  (transverse moment of inertia)
     KB = 3.2 m  (centre of buoyancy above keel)
     KG = 7.0 m  (centre of gravity above keel, from weight estimate)
     Free surface loss: sum(i/V) = 0.15 m

   STEP 1 — metacentric radius:
     BM = I_T / V = 95,000 / 7,805 = 12.17 m

   STEP 2 — metacenter height above keel:
     KM = KB + BM = 3.2 + 12.17 = 15.37 m

   STEP 3 — solid metacentric height:
     GM_solid = KM - KG = 15.37 - 7.0 = 8.37 m

   STEP 4 — correct for free surface:
     GM_fluid = 8.37 - 0.15 = 8.22 m    -> POSITIVE, ship is stable. OK.
     (8.2 m is in fact very stiff; comfort would suffer — see confusion points.)

   STEP 5 — righting arm at 10 deg (small-angle approx):
     GZ = GM x sin(10 deg) = 8.22 x 0.1736 = 1.427 m

   STEP 6 — righting moment:
     M_right = Delta x GZ = 8,000 t x 1.427 m = 11,420 tonne-metres
     (x g = 1.120 x 10^8 N.m if you want SI force units)
```

The ship is stable (GM > 0) and develops an 11,400 t·m righting moment at 10° — a
strong restoring torque. Every loading condition gets this check.

---

## Common Confusion Points

### "More GM is always safer" — NO

```
   LOW GM (tender)            HIGH GM (stiff)
   ----------------           ----------------
   small righting moment      large righting moment
   slow, gentle roll          fast, violent, short-period roll
   long roll period           short roll period (T_roll ~ 1/sqrt(GM))
   risk: too little to        risk: snaps upright so hard it throws
         resist heeling             cargo, injures crew, fatigues hull
```

Stability is a *band*, not a maximum. Roll period scales roughly as 1/√GM, so a very
stiff ship has a short, jerky roll that is uncomfortable and can damage cargo and
structure. The art is enough GM for safety, not so much that the ship is brutal.

### B (beam) vs B (centre of buoyancy)

The letter **B** means both the **beam** (a width) and the **centre of buoyancy**
(a point). They are unrelated quantities that happen to share a symbol. Read by context:
"the beam is 18 m" (a length) vs. "B rises and shifts as the ship heels" (a point).

### Metacenter is not a fixed point in the ship

M is only the pivot of the buoyant force for *small* heel. It moves as the angle grows
(that is exactly why the GZ curve bends away from the straight GM·sinθ line). Treating
M as a permanent landmark is the most common beginner error; M lives where the *current*
buoyancy line crosses the centerline, and that crossing migrates with heel.

### GM, GZ, and the righting moment are three different things

```
   GM  = metacentric height   [length]   -> the SLOPE of stability at zero heel
   GZ  = righting arm         [length]   -> the LEVER at a given heel
   M_r = righting moment      [force.length] = Delta x GZ -> the TORQUE
```

GM is the special case GZ → GM·sinθ near θ=0. The righting moment is what actually
turns the ship back upright, and only it has units of torque.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Check if the ship floats at all | Δ = ρgV (Archimedes) |
| Find how much it sinks per tonne added | TPC = ρ·Aw/100 |
| Check small-angle stability | GM = KM − KG > 0 |
| Get the height of the metacenter | KM = KB + BM, with BM = I_T/V |
| Find the righting arm at small heel | GZ = GM·sinθ |
| Find the actual righting torque | M = Δ·GZ |
| Assess large-angle / capsize safety | The full GZ curve, AVS, area under it |
| Account for partly-full tanks | Subtract Σ(i/V) from GM (free surface) |
| Survive a hull breach | Damage stability / subdivision (SOLAS index A ≥ R) |
| Understand the dynamic (in-waves) response | See `seakeeping/` [05] |
| Review the general second-moment-of-area math | See `structural/` |
