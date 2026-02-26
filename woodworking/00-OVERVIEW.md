# Woodworking: Wood, Tools, Joinery, and Finishing — Landscape

## The Big Picture

Woodworking is the craft of shaping wood into objects through a combination of stock preparation, joinery, and surface treatment. The fundamental constraint that distinguishes it from metalworking: wood is anisotropic and hygroscopic — it moves with changes in humidity, and it moves differently along its three axes. Every design decision, every joint, every finishing choice must account for this movement.

```
WOODWORKING KNOWLEDGE MAP
===========================

              MATERIAL KNOWLEDGE
              (the irreducible foundation)
              +---------------------------+
              | Wood species selection    |
              | Grain direction           |
              | Moisture content / EMC    |
              | Movement and seasonal     |
              | dimensional change        |
              +---------------------------+
                      |
          +-----------+------------+
          |                        |
    STOCK PREPARATION         JOINERY
    +-----------------+    +-------------------+
    | Flattening /    |    | Mortise & tenon   |
    | milling rough   |    | Dovetail          |
    | lumber          |    | Box joint         |
    | Hand planing    |    | Floating tenon    |
    | Scrapers        |    | Frame and panel   |
    | Sanding         |    | (movement-accom.) |
    +-----------------+    +-------------------+
          |                        |
          +------+        +--------+
                 |        |
            CONSTRUCTION
            +-----------+
            | Casework  |
            | Chairs    |
            | Tables    |
            | Cabinets  |
            | Turning   |
            | Carving   |
            +-----------+
                 |
            FINISHING
            +------------------+
            | Film finishes    |
            | Penetrating oils |
            | Shellac          |
            | Lacquer          |
            | Water-based      |
            +------------------+
```

---

## Wood Movement: The Fundamental Constraint

Before tools or joinery: if you don't understand wood movement, every piece you build eventually fails.

```
WOOD MOVEMENT AXES
===================

           LONGITUDINAL (along grain)
           Changes: ~0.1%  (negligible)

     CROSS-SECTION:
     +------------------+
     |                  |
     |   RADIAL         |  Changes: 2–5% per 4% MC change
     |  (center to bark)|  (quarter-sawn boards move this way)
     |                  |
     +------------------+
     TANGENTIAL          Changes: 4–12% per 4% MC change
     (rings / bark dir.) (flat-sawn boards move this way)

EXAMPLE (4% MC change; going from 12% to 8% MC — typical seasonal):
  10" wide flatsawn oak:
    Tangential shrinkage: ~7% per 4% MC × 10" = ~0.7" of movement
  10" wide quartersawn oak:
    Radial shrinkage: ~3.5% per 4% MC × 10" = ~0.35" of movement

  This is why quartersawn is preferred for tabletops:
  HALF the movement of flatsawn from the same species

MOISTURE CONTENT (MC):
  Fiber Saturation Point (FSP): ~28–30% MC
  Below FSP: wood shrinks as it dries
  Above FSP: only free water changes (no dimensional change)
  EMC (Equilibrium MC): MC wood reaches in given humidity
    65% RH indoor → ~12% MC
    30% RH (dry winter interior) → ~7% MC
```

---

## The Two Tool Traditions

```
HAND TOOLS vs. POWER TOOLS TRADITIONS
========================================

HAND TOOL TRADITION                 POWER TOOL TRADITION
--------------------                --------------------
Timing: Antiquity → present         Timing: Late 19th c. → present
Center: England/Japan/Germany        Center: American industrial shops
Goal: Surface quality direct         Goal: Production speed and quantity
      from tool (no sanding)

Key tools:                          Key tools:
  Bench planes (No.4, No.5, No.7)     Table saw (primary breakdown)
  Chisels (bench, mortise, paring)    Band saw (curves + resawing)
  Western / Japanese saws             Jointer (face flattening)
  Marking and layout tools            Thickness planer
  Mallets                             Router / Router table
  Hand router planes                  Drill press

Philosophy:                         Philosophy:
  Quiet; fine-tunable;               Loud; faster; consistent;
  learned feel for wood              precision via jigs + fences
  No electricity needed              Dust collection required
  Better surface quality possible    Power can't replace technique

Trend:
  Hybrid shops: power tools for stock preparation (breaking down rough
  lumber, thicknessing, jointing) + hand tools for joinery and finishing
  surfaces. This is the dominant modern approach among quality craftspeople.
```

---

## Species Spectrum

```
HARDWOOD vs. SOFTWOOD (NOT about actual hardness)
===================================================

HARDWOOD                            SOFTWOOD
(flowering trees — angiosperms)     (conifers — gymnosperms)
--------------------------------    -------------------------
Vessels visible in cross-section    Tracheids only (no vessels)
More complex anatomy                Simpler anatomy
Examples:                           Examples:
  Oak, maple, walnut, cherry          Pine, cedar, fir, spruce
  mahogany, teak, ash                 hemlock, redwood, Douglas fir
Generally harder (but balsa is a    Generally softer (but yew and
hardwood; pine is harder than balsa) some pines are quite hard)

WHEN TO USE HARDWOOD:
  - Furniture exposed to wear (tabletops, chair parts, drawers)
  - Visible joinery (dovetails that show)
  - Any application requiring sharpening tools (hardwood takes
    crisp edges better)

WHEN TO USE SOFTWOOD:
  - Construction lumber (studs, joists, sheeting)
  - Shop jigs and fixtures (cost)
  - Rustic furniture where texture acceptable
  - Some finish carpentry (pine, cedar trim)
  - Certain traditional applications (Shaker pieces in pine)
```

---

## Module Map

```
woodworking/
├── 00-OVERVIEW.md             ← you are here
├── 01-WOOD-SELECTION.md       Species, grain, figure, defects, moisture
├── 02-HAND-TOOLS.md           Planes, chisels, saws, marking — setup and use
├── 03-POWER-TOOLS.md          Table saw, band saw, router, lathe — safety and use
├── 04-JOINERY.md              Mortise-tenon, dovetail, box joint, biscuit, dowel
├── 05-SURFACE-PREPARATION.md  Flattening, planing, scraping, sanding
├── 06-FINISHING.md            Oils, shellac, lacquer, varnish, water-based
├── 07-FURNITURE-CONSTRUCTION.md Casework, frame-and-panel, chairs, tables
├── 08-TURNING-CARVING.md      Lathe basics, bowl turning, relief carving
└── 09-SHOP-SETUP.md           Workbench, tool storage, dust collection, electrical
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is the primary constraint in woodworking design? | Wood movement (dimensional change with humidity) |
| Which sawn orientation moves least? | Quartersawn (~half the movement of flatsawn in the same species) |
| What is EMC? | Equilibrium moisture content — what wood stabilizes to at a given humidity |
| Hardwood vs. softwood — what's the actual distinction? | Botanical (flowering tree vs. conifer), not actual hardness |
| What is the hybrid shop approach? | Power tools for stock prep; hand tools for joinery and final surfaces |
| What causes most woodworking project failures? | Wood movement not accommodated (splits, warps, broken joints) |
| What is fiber saturation point? | ~28–30% MC; below this wood shrinks/swells; above this only free water changes |
| What indoor RH gives ~12% MC? | ~65% relative humidity |
| What is tangential vs. radial movement? | Tangential = along annual rings (flatsawn); radial = center to bark (quartersawn) |
| Why is quarter-sawn preferred for tabletops? | Half the seasonal movement; more stable; also shows ray figure in oak |

---

## Common Confusion Points

**Hardwood/softwood is botanical, not physical hardness.** Balsa is a hardwood. Some species of pine (like longleaf) are harder by Janka scale than many "hardwoods." The distinction is angiosperms (hardwood) vs. gymnosperms (softwood) — cellular anatomy is what differs, with hardwoods having vessel cells (pores) and softwoods having only tracheids.

**Wood is not dimensionally stable.** This is the most important fact in the craft. Furniture fails because makers either don't know about wood movement or don't accommodate it. A 12" wide solid wood panel glued into a rigid frame will crack the frame or the panel within a couple of seasonal cycles.

**"Grain" means at least three different things**: (1) the direction of wood fibers (with grain, across grain), (2) the visual pattern of growth rings on a surface (straight grain, cathedral grain), (3) the specific texture of a wood species (open-grained oak, closed-grained maple). Context usually makes clear which is meant.

**Shop tools require sequential use in a specific order.** The sequence for milling rough lumber: face flattening (jointer or hand plane) → edge jointing → thickness planing → ripping to width → crosscutting to length. Skipping steps or reversing order produces twisted, non-square stock that causes problems downstream.

**Hand tool work is not inherently slower than power tools for small batches.** Setup time for power tools (fence adjustment, blade changes, test cuts, jig construction) means that for a single piece or a few pieces, hand tools are often faster. Power tools win on batch production of identical parts.
