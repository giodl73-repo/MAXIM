# Joinery: Mortise-Tenon, Dovetail, Box Joint, Floating Tenon

## The Big Picture

Joinery is the engineering core of woodworking. Each joint type solves a specific mechanical problem with a specific combination of strength axes, glue surface area, and wood movement accommodation. Choosing the wrong joint is a structural engineering mistake, not just an aesthetic one.

```
JOINT SELECTION BY FUNCTION
=============================

JOINT NEEDED FOR:                    USE THIS:
-----------------------------        ----------------------
Frame corner (right angle; tables,   Mortise and tenon
door frames, chair aprons)           Bridle joint
                                     Loose tenon (Domino)

Carcass corner (box construction)    Dovetail (show quality)
                                     Box joint (machine efficient)
                                     Rabbet (simple; less strong)

Edge-to-edge (panels)                Glue only (if flat and flat)
                                     Biscuit/dowel (alignment only)
                                     Tongue and groove

Shelf in carcass (dado)              Dado (housing joint)

Drawer face to sides                 Half-blind dovetail (traditional)
                                     Lock miter (machine)
                                     Rabbet + fasteners (utility)

Two boards crossing / halving        Half-lap / cross-lap

Leg-to-rail at angle                 Mortise-tenon + compound angle
                                     Bridle joint

Long grain to long grain             Glue only (strongest possible)
```

---

## Mortise and Tenon

The most important joint in furniture making. Used wherever a rail meets a leg, a stretcher meets a post, a door rail meets a stile.

```
MORTISE AND TENON GEOMETRY
============================

  STILE / LEG (outer); MORTISE (inner) — cut into the stile.
  TENON projects from the rail and slots into MORT.

     STILE / LEG:
     +--------------+
     |              |
     |              |
     |    [mortise  |
     |     cut into |
     |     stile]   |
     |              |
     +--------------+

     MORTISE detail (cut into the stile):
     +------+
     | MORT.|
     |      |
     +------+

PROPORTIONS (rules of thumb):
  Tenon thickness: 1/3 of rail thickness
    (1" rail → 3/8" tenon; 1.5" rail → 1/2" tenon)
  Tenon length: 2/3 to 3/4 of receiving member thickness
    (don't go all the way through unless through-tenon is intended)
  Tenon width: rail width minus 1/4" to 1/2" per side (shoulder at each edge)

MORTISE PROPORTIONS:
  Width = tenon thickness
  Length = tenon width
  Depth = tenon length + 1/16" (clearance for glue)

HAUNCHED TENON:
  Tenon with a step ("haunch") to fill groove in stile
  Used in frame-and-panel: panel groove continues through mortise area;
  haunch fills that portion of groove
  HAUNCH (fills groove):
  +---+
  |   |
  +---+

  TENON proper (extends below haunch):
  +----------+
  |          |
  +----------+

DRAW-BORING:
  Hole drilled through mortise and tenon; slightly offset
  Hardwood peg driven through: draws joint tight mechanically
  Historically used instead of clamps; allows assembly without clamps
  Works dry (peg swells when glue applied) or with glue
```

---

## Dovetail

The premier corner joint for boxes, drawers, and case sides. Visual proof of craftsmanship; also mechanically superior in tension (tails interlock; can't be pulled apart along the pin board axis).

```
DOVETAIL GEOMETRY
==================

  TAIL BOARD                PIN BOARD
  +--------+                +--------+
  |  \  /  |                | | || | |
  |   \/   |    fit         |  \  /  |
  |   /\   |   together →   |   \/   |
  |  /  \  |                +--------+
  +--------+

RATIO (slope of the tails):
  Hardwood: 1:8 (1 unit horizontal : 8 units longitudinal)
            Angle = arctan(1/8) ≈ 7.1°
  Softwood: 1:6 (softer wood; slightly steeper for holding power)
            Angle = arctan(1/6) ≈ 9.5°
  Note: wider (shallower) is more elegant; narrower (steeper) is stronger
        Traditional furniture varies; 1:8 is a safe, attractive choice

TYPES:
  Through dovetail:      Visible on both faces; show quality joint
  Half-blind dovetail:   Pins concealed from one face (drawer fronts)
  Full-blind/mitered:    Both faces concealed (formal case corners)
  Sliding dovetail:      Single tapered key; drawer assembly; shelf joints

HALF-BLIND DOVETAIL (drawer front):

  Tail board (drawer side):
    Tails project from the end (visible on side, not on front).

  Pin board (drawer front):
    Pins are blind — they don't go all the way through, so the
    drawer front face shows no end-grain.

  Pin-board face is hidden from outside.

HAND-CUTTING SEQUENCE:
  1. Mark baselines (knife line): equal to thickness of mating board
  2. Layout tails with bevel gauge set to ratio (1:8 hardwood)
  3. Saw tails (leave knife line)
  4. Chop out waste between tails (back to baseline)
  5. Transfer tails directly to pin board (mark with knife around tails)
  6. Saw pins
  7. Chop waste between pins
  8. Test fit; adjust with paring chisel

COMMON ERROR: Sawing on the wrong side of the line.
  Rule: The line is the joint surface; saw on the waste side.
  "Leave the line" = saw just outside the knife mark; pare to fit.
```

---

## Box Joint (Finger Joint)

Regular interlocking fingers — equal-width projections and notches. Visually similar to dovetail but no mechanical interlock (no angled surfaces); relies entirely on glue surface area.

```
BOX JOINT GEOMETRY
===================

   +--+  +--+  +--+
   |  |  |  |  |  |  ← fingers (both boards)
   |  |  |  |  |  |
---+  +--+  +--+  +---
              ↑
            all 90° (no angle; unlike dovetail)

GEOMETRY:
  Finger width = pin width = board thickness ÷ any integer
  Common: 1/4" fingers on 3/4" board (3 pins, 2 sockets per corner)
  Larger fingers = faster to cut; less glue area
  Smaller fingers = more glue area; more visual interest

CUTTING METHOD:
  Dado stack on table saw + jig
  Jig: wooden fence with precisely spaced key
  Key is one finger-width from blade center
  Each successive notch: register previous notch on key; cut new notch
  Works like a LFSR — self-indexing

STRENGTH: High glue surface area; strong in all planes except pull-apart along
          finger axis (which is just shear on the glue surface). For boxes,
          this is not the primary load direction.
```

---

## Floating Tenon (Domino / Loose Tenon)

Modern alternative to the hand-cut mortise and tenon: both members get a mortise (slot), and a separate pre-made tenon (the "domino") bridges them.

```
FLOATING TENON SYSTEM
======================

TRADITIONAL M&T:
  Member A (with integral tenon):
  +------+
  |      |
  | TENON|
  |      |
  +------+
       ↕
  Member B (with mortise):
  +------+
  | MORT |
  +------+

FLOATING TENON:
  Member A (slot only):
  +------+
  |      |
  | SLOT |
  |      |
  +------+
       ↕ ↕ ↕
  Separate tenon piece goes into both slots.
  Member B (slot only):
  +------+
  |      |
  | SLOT |
  |      |
  +------+

Festool Domino machine:
  Combination drill + oscillating router
  Cuts precise slot in one plunge
  Tenon pieces: beech, pre-sized
  Sizes: 4mm to 14mm wide tenons

Advantages:
  Much faster than hand-cutting
  Works on complex assemblies
  Adjustable registration (align) vs. fixed (strong)

Disadvantages:
  Festool Domino: $700–$1,500 (tools cost)
  Less visual appeal (entirely hidden joint)
  Fundamentally relies on alignment precision

Biscuits vs. Domino:
  Biscuit: oval pressed wood chip; for alignment + glue surface
           Swells with moisture to lock; but not much structural strength
           Best for: alignment during glue-up; adding glue surface to edge joints
  Domino:  Actual structural tenon; much more strength than biscuit
           Comparable strength to hand-cut mortise and tenon
  Dowels:  Cylindrical rods; traditional; alignment + some shear resistance
           Requires precise drilling; dowel jig helps
```

---

## Bridle Joint and Half-Lap

```
BRIDLE JOINT (OPEN MORTISE AND TENON):
========================================

  Fork piece (like open mortise):
  +--------+
  |        |
  +--------+

  Tenon slides into the fork:
  +------+
  | TENON|
  +------+

  Proportions: same as M&T (1/3 stock thickness)
  Used for: trestle joints; frame corners where face is visible
  Advantages: fast to cut (no internal mortise)
  Disadvantages: open — less strong in one axis; open grain visible

HALF-LAP (cross-lap / corner-lap):
========================================

  CORNER LAP:
    Each piece cut to halfway through; they overlap flat
    at the corner (L-shape). Two pieces, each removing
    half their thickness, meet flush.

  CROSS LAP:
    Each piece cut halfway through; they nest flat where
    they cross. Two pieces, each removing half their
    thickness in the overlap zone, end up coplanar.

  Both pieces maintain full face width at overlap:
  lap thickness = 1/2 board thickness on each piece

  Used for: X-joints (frames); furniture stretchers; cabinet dividers
  Strength: Good in shear perpendicular to laps; not for pull-apart
```

---

## Joinery Strength Comparison

```
JOINT STRENGTH TABLE
=====================

JOINT                  GLUE SURFACE   MECHANICAL    BEST USE
                       AREA           INTERLOCK
-------------------    -----------    -----------   -------
Mortise and tenon      High           High (long    Frame construction;
                       (4 long grain  grain contact)chairs; doors
                       surfaces)      shear + tension

Dovetail               Moderate-High  HIGH (angled  Box/drawer corners;
                       (angled surfs) surfaces;     case sides
                       cannot pull
                       apart in key
                       direction)

Box/finger joint       VERY HIGH      Low (only     Decorative boxes;
                       (many finger   shear; no     drawers (utility)
                       surfaces)      mechanical
                       interlock)

Dowel                  Low-moderate   Low (only     Alignment; face
                       (end grain)    shear in       frame to carcass;
                                      hole direction) knockdown furniture

Biscuit                Low            Very low      Alignment only;
                                      (alignment    edge joints
                                      only)

Floating tenon         High           High          General frame;
(Domino)               (long grain)   (comparable   comparable to M&T
                                      to M&T)

Glue only              Maximum        None          Long grain to long
(no joint)             (pure long     (requires     grain only
                       grain mating)  perfectly     (strongest joint
                                      flat surfaces)if executed well)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is the tenon thickness rule? | 1/3 of the rail thickness |
| What is the tenon length rule? | 2/3 to 3/4 of the mortise-member thickness |
| What angle for dovetails in hardwood? | 1:8 ratio (~7.1°); 1:6 for softwood |
| What is a half-blind dovetail? | Tails visible from inside, pins concealed from outside (drawer front) |
| What is a haunched tenon? | Tenon with a stepped shoulder to fill groove in frame-and-panel stile |
| What is draw-boring? | Offset hole through M&T; peg draws joint tight mechanically |
| Biscuit vs. Domino — what's the difference? | Biscuit = alignment only; Domino = structural floating tenon |
| What is the box joint's strength mode? | Glue surface area (shear); no mechanical interlock |
| When is glue-only the strongest joint? | Long-grain to long-grain with flat, mating surfaces |
| What is a bridle joint? | Open mortise: fork-shaped slot receives a tenon; fast to cut |

---

## Common Confusion Points

**Dovetails are for tension resistance, not compression.** A dovetail resists pulling apart along the axis of the pin board but provides no mechanical advantage against racking. This is why drawers use dovetails (the drawer side is pulled; the joint resists this direction) while chair seats use mortise and tenon (which resists racking from sitting).

**Box joints and dovetails look similar but are mechanically different.** The dovetail's angled surfaces create a mechanical interlock — even with no glue, the joint can't be pulled apart. The box joint has only right-angle surfaces; its strength is entirely dependent on glue area. Both are valid; the choice is aesthetic + manufacturing method.

**"Leave the line" is the most important marking principle.** In joinery, the knife line represents exactly where two surfaces will meet. When sawing, you want the kerf to be entirely in the waste, with the knife line intact. That surface is then pared to the knife line with a chisel. Sawing through the line leaves a gap; sawing too far in the waste requires more fitting work.

**Glue is strongest in long-grain-to-long-grain joints.** This surprises many beginners. A properly made edge glue joint (two pieces glued along their long grain faces) is often stronger than the wood itself — the wood will fail in the wood, not at the glue line. End grain absorbs glue like a sponge and creates a weak joint because the glue penetrates rather than bridging the surfaces. Use joints (mortise and tenon, dovetails) to provide long-grain glue surfaces for end-grain connections.

**Mortise and tenon proportions are not arbitrary.** The 1/3-thickness rule for tenon thickness is the result of empirical testing: thinner tenons break under load; thicker tenons weaken the mortised piece by removing too much material. The 2/3 length rule ensures adequate glue surface without the tenon bottoming out (which would prevent the shoulders from seating).
