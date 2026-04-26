# Wood and Joinery: Applied Geometry

## The Big Picture

Wood joinery is an engineering problem disguised as craft. The core challenge: wood is a biological anisotropic composite that moves with moisture changes, and joints must accommodate that movement while maintaining structural integrity across decades or centuries.

```
THE JOINERY PROBLEM HIERARCHY

+---------------------------------------------------------------+
|  CONSTRAINT 1: Wood moves (moisture-driven dimensional change) |
|  Wood moves across grain; negligible along grain              |
|  A 300mm-wide board can move 6–9mm seasonally                 |
+---------------------------------------------------------------+
                    |
                    v
+---------------------------------------------------------------+
|  CONSTRAINT 2: Joint must resist mechanical loads             |
|  Tension (pulling apart), compression, shear, racking         |
|  Different joints excel at different load types               |
+---------------------------------------------------------------+
                    |
                    v
+---------------------------------------------------------------+
|  CONSTRAINT 3: Joint must be manufacturable                   |
|  Hand tools → machine tools → CNC → flat-pack hardware        |
|  Cost of the joint scales with precision required             |
+---------------------------------------------------------------+
                    |
                    v
+---------------------------------------------------------------+
|  SOLUTION SPACE: Joinery taxonomy                             |
|  Butt < Mortise-tenon < Dovetail < Japanese interlocking      |
|  (increasing mechanical sophistication and material cost)     |
+---------------------------------------------------------------+
```

---

## Wood Anatomy

Understanding joinery requires understanding what wood actually is.

### Cell Structure

```
TRUNK CROSS-SECTION (schematic):

    Bark (outer protection)
    |
    Cambium (growth layer — 1 cell thick)
    |
    Sapwood (outer rings — active water transport, lighter colored)
    |
    Heartwood (inner rings — dead, denser, more durable, darker)
    |
    Pith (center — weakest, avoid in furniture)

CELLULAR STRUCTURE:
  Wood = bundles of hollow cellulose tubes (tracheids/vessels)
  bonded with lignin matrix. Like carbon fiber:
  - fibers (cellulose) provide tensile strength
  - matrix (lignin) provides compressive resistance
  - anisotropic: very different properties along vs. across grain
```

### Grain Directions

```
       LONGITUDINAL (along grain)
            |
            |  <-- Strong in tension and compression
            |  <-- Movement: negligible (<0.1% seasonal)
            |
   RADIAL ---+--- TANGENTIAL
   (radius    |   (circumference
   of log)    |    of log)
              |
         RADIAL:    ~3–5% total shrinkage (green to oven-dry)
         TANGENTIAL: ~6–10% total shrinkage (green to oven-dry)
         (tangential moves about 2x more than radial — consistent across species)
```

These are **total shrinkage coefficients** from green (fully saturated) to oven-dry — a worst-case bound, not seasonal movement in a conditioned interior. In practice, kiln-dried lumber at 8% MC in a climate-controlled space sees far smaller swings.

**The practical rule for seasonal indoor movement**: a 300mm board in a temperate interior (30–50% RH swing, summer vs. winter) moves approximately:
- Quartersawn (radial face showing): ~3–6mm
- Flatsawn (tangential face showing): ~6–12mm

The EMC calculation in the section below (5.4mm for 300mm quartersawn oak) is correct for these real-world conditions. This is not a small effect — Victorian drawers that stick in summer are telling you about moisture and grain direction, and 6mm of panel movement is the difference between a frame-and-panel door working and a solid-panel door splitting.

### Flatsawn vs. Quartersawn

```
FLATSAWN (plain-sawn):
  Log sliced through in parallel cuts
  Tangential face shows on surface
  Wider planks, less waste, cheaper
  More movement, more distortion (cupping)
  Figure: cathedrals and ovals

QUARTERSAWN:
  Log cut into quarters, then each quarter
  sawn through at ~90 degrees to growth rings
  Radial face shows on surface
  Less movement, more stable, straighter grain
  More waste, more expensive
  Figure: ray fleck (oak, sycamore) — the silver streaks
  Best for: wide panels, table tops, instrument soundboards
```

### Figure

"Figure" = visual pattern from grain irregularities. These are valuable and require specific sawing orientation to reveal:

| Figure | Cause | Value |
|--------|-------|-------|
| Ray fleck / silver grain | Medullary rays exposed by quartersawing | High (oak, sycamore) |
| Burl / burr | Abnormal growth from stress or injury | Very high |
| Bird's-eye | Genetic defect in maple — small circular dimples | High |
| Curly / fiddleback | Undulating grain — wavy reflective figure | High |
| Quilted | Compression figure in face grain | High (maple, mahogany) |
| Straight grain | Normal growth, no irregularities | Standard |

---

## The Wood Movement Problem

Wood is hygroscopic: it gains and loses moisture with relative humidity changes, and this causes dimensional changes. A panel glued rigidly will crack or the joint will fail.

```
EQUILIBRIUM MOISTURE CONTENT (EMC):
  RH 40% = EMC ~8%  (typical heated interior, winter)
  RH 60% = EMC ~11% (typical spring/fall)
  RH 75% = EMC ~14% (humid summer or tropical)

  Swings of RH 40% → 75% = ~6% EMC change
  For tangential grain in 300mm oak board:
  6% MC × (tangential shrinkage coefficient ~0.003/%) × 300mm
  ≈ 5.4mm of movement across 300mm

This is why:
  - Table tops must be attached with figure-8 buttons or clips (not screws)
  - Wide panels must float in frames, not be glued
  - Drawers stick in summer, rattle in winter
  - Antique boards crack when brought from English dampness to American central heating
```

**The engineering solutions**:

1. **Avoid wide solid panels**: break them up or use plywood
2. **Frame-and-panel construction**: panel floats free in a grooved frame — the panel can move without distortion
3. **Quarter-saw where stability matters**: halves the movement
4. **Engineered wood (plywood, MDF)**: cross-grain lamination eliminates most movement entirely
5. **Design joints to allow movement**: elongated screw holes, floating tenons

---

## Joinery Taxonomy

### Hierarchy by Mechanical Sophistication

```
BUTT JOINTS (weakest — require fasteners or adhesive)
    |
    +-- Flat butt (just two faces meeting)
    +-- Dowel butt (cylindrical alignment pegs add shear resistance)
    +-- Biscuit butt (flat oval biscuit in slot — alignment + glue area)
    +-- Pocket screw (angled screw from inside — fast, hidden, modern)
    +-- Domino (proprietary Festool system — loose tenon in routed slots)
    +-- Cam lock + confirmat (IKEA hardware — see 07-IKEA-MODEL.md)

DADO / HOUSING (groove receives shelf/panel — resists shear)
    |
    +-- Through dado (groove crosses full width)
    +-- Stopped dado (groove stops before edge, hides joint)

RABBET / REBATE (L-shaped notch at edge — used at cabinet backs, drawer bottoms)

LAP JOINTS (one piece crosses or laps another)
    |
    +-- Half-lap (both pieces halved — flush on both faces)
    +-- Cross-lap (middle of both pieces — used in grids)
    +-- End-lap (at ends — frame corners)

MORTISE AND TENON (fundamental structural joint)
    |   [see full section below]

DOVETAIL (mechanical interlock — resists tension in one direction)
    |   [see full section below]

BOX JOINT / FINGER JOINT (interlocking square fingers — drawer construction)

BRIDLE JOINT (open mortise at end — used in chair legs, light frames)

JAPANESE INTERLOCKING JOINERY (extreme elaboration — no glue or fasteners)
    +-- Chigai kama (interlocking wedge-key)
    +-- Shachisen (pins and wedges in complex 3D geometry)
    +-- Sanmaisen-kama, kanawa-tsugi, etc.
```

---

## Mortise and Tenon — The Fundamental Joint

The mortise-and-tenon joint has been used for at least 5,000 years (found in Egyptian furniture). Every other joint is a variation or elaboration.

```
BASIC ANATOMY:

  MORTISE (hole)          TENON (tongue)
  +----------+            +----------+
  |          |            |    +-+   |
  |  [HOLE]  |  <------   |    |T|   |
  |          |            |    +-+   |
  +----------+            +----------+
  (in the stile,          (on the rail,
   vertical member)        horizontal member)

PROPORTIONS (rule of thumb):
  Tenon thickness = 1/3 mortise member thickness
  Tenon length = at least 3× tenon thickness
  Tenon width = max 5× tenon thickness (beyond this, movement splits it)
```

### Mortise-and-Tenon Variants

| Variant | What It Adds | When Used |
|---------|-------------|-----------|
| Blind (stopped) tenon | Tenon doesn't show on far side | Most furniture — clean appearance |
| Through tenon | Tenon exits far face | Visible joinery (Arts & Crafts aesthetic) |
| Haunched tenon | L-shaped shoulder fills groove at panel edge | Where panel groove runs through |
| Drawbored tenon | Offset hole drilled through joint — peg pulls shoulders tight | No clamps needed; very strong |
| Tusked tenon | Through tenon with wedged keys — can be disassembled | Trestle tables, knockdown |
| Twin / double tenon | Two tenons side by side | Wide rails where single would be too wide |
| Loose/floating tenon | Separate tenon fits into mortises in both pieces — Festool Domino | Modern fast production |

### Why the Joint Works

The mortise-and-tenon resists:
- **Compression**: shoulders bear load
- **Racking (shear)**: tenon fits tightly, resists side forces
- **Tension**: glued cheeks resist pullout; drawbore pin locks mechanically

It does NOT work well as-cut for tension in the grain direction — that's why pegs, glue, or wedges are added.

---

## Dovetail — Mechanical Interlock

The dovetail's geometry creates a mechanical interlock that resists tension even without adhesive. The name comes from the trapezoidal shape — wider at the base than the tip, like a dove's tail.

```
DOVETAIL GEOMETRY:

  PINS (narrow, vertical)    TAILS (wide, angled)
       |     |                /   \   /   \
       |     |               /     \ /     \
      /|     |\             /       X       \
     / |     | \           /    (tails interlock)\
    /  |     |  \          \   with pins          /
   +---+     +---+          +---+---+---+---+---+
```

### Dovetail Variants

| Variant | Where Used | How to Identify |
|---------|-----------|----------------|
| Through dovetail | Box corners, drawer sides | Joint visible on both faces |
| Half-blind (lapped) | Drawer fronts | Joint hidden on one face — very common in antiques |
| Full-blind (secret mitered) | High-end casework | Joint hidden on both faces — rare, expensive |
| Sliding dovetail | Shelves in carcase, table legs to aprons | Dovetail shaped sliding into mating slot |

**Hand-cut vs. machine-cut tells**:
- Hand-cut: slight variation in pin spacing, slightly angled baselines, saw marks visible on pins
- Router-cut (dovetail jig): perfectly uniform pin spacing, exact 90° baselines, usually half-blind pattern
- CNC: uniform plus potentially variable spacing (mimicking hand-cut appearance)

The half-blind dovetail is the standard for drawer fronts because it's the strongest joint that hides its own construction from the front. When you pull open a drawer in quality furniture, you're pulling against the mechanical interlock of the tails against the pins — not just glue.

---

## Frame-and-Panel Construction

The engineering solution to the wood movement problem for large surfaces:

```
+----------------------------------+
|  STILE    |    PANEL    |  STILE |
| (vertical)|  (floats in |( vert.)|
|           |   groove -- |        |
+--+        |  NOT glued) |       ++
|  |        |             |        |
|  | RAIL   |    wood can |  RAIL  |
|  |(horiz.)|    expand / |        |
+--+        |    contract |       ++
|           |    without  |        |
|  STILE    |    stress   |  STILE |
+----------------------------------+

  Frame (stiles + rails): structural, stable
  Panel: floats free -- can move seasonally
  Groove: ~3mm wider than panel for movement allowance
```

Applications: Cabinet doors, church paneling, Wainscoting, raised panel doors.

Without the floating panel, a wide solid wood panel would crack or blow the frame apart. This is not a hypothesis — you can see cracked solid-panel Victorian doors in any old building.

---

## Glue Types

| Glue | Open Time | Reversible | Best For | Notes |
|------|-----------|-----------|---------|-------|
| Hide glue (protein) | 5–10 min hot | Yes (heat + moisture) | Antique restoration, fine furniture, musical instruments | Classic; reversibility is essential for repair |
| PVA (yellow/white) | 5–20 min | No (water softens) | General woodworking | Most common; damp conditions weaken it |
| Aliphatic (Titebond II/III) | 5–10 min | No | Outdoor furniture | Water-resistant; III is waterproof |
| Epoxy | 5–90 min (type) | No | Gap-filling, voids, composites | Can fill large gaps; expensive |
| Polyurethane (Gorilla) | 20–30 min | No | Difficult materials, some plastics | Foams to fill gaps; messy |
| Cyanoacrylate (CA/super) | Seconds | Partial (acetone) | Small repairs, tool handles | Not for structural joints |

**Hide glue is the correct choice for antique restoration**: reversible with heat and moisture means future restorers can disassemble without damage. PVA joints must be broken, which often damages the wood.

---

## Modern KD (Knock-Down) Joinery

Flat-pack and RTA (Ready-To-Assemble) furniture use hardware joints instead of traditional woodworking:

```
CAM LOCK (IKEA standard):
  +---------+      +-------+
  | CAM     |      | DOWEL |
  | (spins  |      | (pegs |
  |  in     |      |  for  |
  |  hole)  |      | align)|
  +---------+      +-------+
  Bolt from one piece enters cam in other piece;
  turning cam with screwdriver draws pieces tight.
  Fast, no skill, ~$0.10 per unit — genius at scale.

CONFIRMAT SCREW:
  Specialized screw with coarse thread and
  cylindrical shank — designed for particleboard.
  Drive in, it bites — remove and re-drive,
  it still holds (within limits).

EURO SCREW + BARREL NUT:
  Machine screw through one piece into barrel nut
  in other piece. Requires exact alignment.
  Fully disassemble-and-reassemble without
  material degradation (unlike cam, which wears).
```

---

## Japanese Joinery — Extreme Elaboration

Japanese temple carpentry developed joinery of extraordinary geometric complexity — joints that interlock in three dimensions, can be assembled and disassembled, and need neither glue nor fasteners:

```
CHIGAI KAMA (interlocking wedge splice):
  Two beams meet end-to-end; their ends are
  shaped so they can only be assembled by
  sliding together at a specific angle.
  Assembled: can't pull apart, can't pry apart.
  Disassemble: only by reversing the assembly motion.

KANAWA-TSUGI (bolt splice):
  Six interlocking fingers in 3D geometry;
  a hidden wooden pin locks the assembly.
  Used for extending a single timber over long spans.

SHIGUCHI (corner joint for post-and-beam):
  Multiple interlocking elements; assembled
  by a precise sequence of movements.
```

Why no glue? Traditional Japanese buildings are designed to flex in earthquakes. Rigid glued joints in a seismic zone fail catastrophically; interlocked joints flex and recover. This is a structural engineering choice, not mere artistry — the joinery is the earthquake resistance.

---

## Decision Cheat Sheet

| Situation | Joint to Use | Reason |
|-----------|-------------|--------|
| Chair leg to seat rail | Mortise and tenon, drawbored | High stress, must be disassemble-resistant |
| Drawer sides to drawer back | Through dovetail | Resists pulling action of drawer |
| Drawer front to drawer sides | Half-blind dovetail | Strong + hides joint from front view |
| Wide table top attachment | Figure-8 clips in elongated holes | Allows seasonal wood movement |
| Cabinet back panel | Floating in groove OR thin ply glued in rabbet | Panel stability vs. structural backing need |
| Shelf in carcase (bookcase) | Sliding dovetail OR shelf pins | Dovetail stronger; pins allow repositioning |
| Fast RTA assembly (commercial) | Cam lock + confirmat + dowels | Speed, no skill required, flat-pack compatible |
| Fine reproduction furniture | Hide glue, traditional joinery | Reversibility for future restoration |
| Outdoor furniture | Waterproof PVA or Titebond III, through wedged tenons | Moisture resistance, no hardware to rust |

---

## Common Confusion Points

**"The grain" is ambiguous**: it can mean the direction of wood cells (longitudinal grain, end grain), the visual pattern on the surface (straight grain, figured grain), or whether you're seeing the flat-cut or edge-cut face. Specify which you mean.

**End grain joints are weak**: butt joints where end grain meets long grain are essentially gluing tubes to a wall — very little bonding surface. This is why you always need mechanical reinforcement (dowels, biscuits, pocket screws) for end-grain-to-long-grain joints.

**Dovetails resist tension in one direction only**: the joint locks against pulling the drawer front off the side. It does not resist compression (pushing) in the same direction, nor does it resist lateral racking — that's handled by the drawer bottom.

**Plywood does not need frame-and-panel**: the cross-grain lamination eliminates most movement, so plywood cabinet sides can be glued solidly at corners. This is why modern casework uses plywood construction — a flat-pack particleboard cabinet exploits the same stability principle.

**Mortise-and-tenon is not just for wood**: the principle — a tongue fitting into a hole — appears in IKEA's wooden dowel alignment pegs, in precast concrete connections, in injection molds, and in printed circuit board edge connectors. It's a universal fastening geometry.
