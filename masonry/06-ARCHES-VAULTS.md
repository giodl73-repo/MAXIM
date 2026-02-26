# Arches and Vaults: Thrust Line Theory, Voussoirs, and Gothic Structure

## The Big Picture

An arch resolves vertical load into inclined thrust, which masonry — strong in compression — can carry perfectly. The elegance of arch engineering is that it converts a tension-prone spanning problem into a purely compressive one. The theory is Hooke's catenary principle (1675), formalized by La Hire, Coulomb, and Heyman.

```
THE ARCH LOGIC
==============

  BEAM (conventional spanning):          ARCH (masonry spanning):
  ┌────────────────────────────┐         ┌────────────────────────────┐
  │  P      P      P          │         │  P      P      P          │
  │  ↓      ↓      ↓          │         │  ↓      ↓      ↓          │
  │  ════════════════════      │         │      ╭─────────╮           │
  │  Tension in bottom fiber   │         │  ╭──╯           ╰──╮      │
  │  → masonry cannot do this  │         │  │   COMPRESSION   │      │
  │                            │         │  ←──────────────────→     │
  │  RESULT: Not possible in   │         │  Horizontal thrust at base │
  │  unreinforced masonry for  │         │  → must be resisted by    │
  │  any significant span      │         │    buttress, wall mass,   │
  └────────────────────────────┘         │    or adjacent arch       │
                                          └────────────────────────────┘

  KEY INSIGHT: The arch converts the bending problem into pure
  compression PLUS horizontal thrust at the supports.
  Managing that horizontal thrust is the central challenge of
  arch-and-vault structural engineering.
```

---

## Thrust Line Theory (Hooke 1675)

Robert Hooke's anagram (1675), revealed posthumously: "Ut pendet continuum flexile, sic stabit contiguum rigidum inversum" — As hangs the flexible line, so but inverted stands the rigid arch.

```
CATENARY AND ARCH RELATIONSHIP
================================

  A flexible chain hanging under its own weight takes a catenary shape:
  y = a × cosh(x/a)    (where a = parameter related to chain length/tension)

  Under uniform load per horizontal unit (e.g., uniform horizontal distributed):
  y = a × x²  (parabola — not catenary)

  CRITICAL RULE: For a masonry arch to stand in pure compression, the
  THRUST LINE (line of pressure) must lie entirely within the arch thickness.

  ┌──────────────────────────────────────────────────────────────────────┐
  │                  ARCH CROSS-SECTION                                  │
  │                                                                        │
  │  ╔════════════════════════════════════════════╗  ← extrados (top)    │
  │  ║                                            ║                        │
  │  ║  ─ ─ ─ ─ ─ THRUST LINE ─ ─ ─ ─ ─ ─ ─ ─  ║  ← stays inside      │
  │  ║                                            ║                        │
  │  ╚════════════════════════════════════════════╝  ← intrados (bottom) │
  │                                                                        │
  │  THREE HINGE MECHANISM (collapse state):                             │
  │  ╔══╗                              ╔══╗                               │
  │  ║  ╚═══╗  hinge              ╔═══╝  ║                               │
  │  ║      ╚═══════[HINGE]═════╝      ║   ← thrust line exits;         │
  │  ╚═════[H]═══════════════════[H]═══╝     arch becomes mechanism     │
  │                                                                        │
  │  3 hinges = statically determinate mechanism = COLLAPSE              │
  └──────────────────────────────────────────────────────────────────────┘
```

**Middle-third rule**: For zero tension anywhere in the arch section, the thrust line must pass through the middle third of the depth at every cross-section. This is the safe working criterion for unreinforced masonry arches.

---

## Voussoir Anatomy

A voussoir arch is built from wedge-shaped stones (voussoirs) that transfer load to neighbors through compression at their contact faces (joints).

```
VOUSSOIR ARCH ANATOMY
======================

  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                    │
  │              KEYSTONE (crown)                                     │
  │               ┌────┐                                              │
  │            ╔══╝    ╚══╗                                          │
  │  HAUNCH  ╔═╝          ╚═╗  HAUNCH                               │
  │         ╔╝   VOUSSOIRS   ╚╗                                      │
  │  SPRING ╝                  ╚ SPRINGER                            │
  │        ╔╝                   ╚╗                                   │
  │  ──────╝  SKEWBACK           ╚──────  SKEWBACK                  │
  │  ABUTMENT ←                → ABUTMENT (must resist horiz. thrust) │
  │                                                                    │
  │  INTRADOS = inner curved face of arch (soffit)                   │
  │  EXTRADOS = outer curved face of arch                            │
  │  RISE = vertical distance from spring line to crown              │
  │  SPAN = horizontal distance between springers                    │
  └──────────────────────────────────────────────────────────────────┘

  JOINT ORIENTATION: voussoir joints are RADIAL (perpendicular to
  the arch curve). This ensures compression acts perpendicular to
  joint face → pure compression transfer, no shear.
```

---

## Arch Geometries

```
SEMICIRCULAR ARCH (Roman)
==========================
  • Rise = span/2
  • Generates high horizontal thrust (H ≈ V × cot(α))
  • Requires massive abutments or buttresses
  • Strong, simple to set out (compass from single center point)
  • Typical in Roman bridges, Romanesque buildings

  Profile:  ╭─────────╮  (full half-circle)

POINTED ARCH (Gothic)
======================
  • Two circular arcs intersecting at crown — angle adjustable
  • Lower rise-to-span ratio reduces horizontal thrust
  • HOW: Increasing the rise with same span steepens the force
    vectors → horizontal component decreases
  • Allows thinner walls, larger windows
  • Key Gothic structural innovation

  Profile:  ╱‾‾‾╲  (two arcs, pointed crown)

COMPARISON: THRUST AT SAME SPAN
================================
  ┌────────────────────────────────────────────────────────────────┐
  │  Semicircular: H = V / 2 (rise/span = 0.5)                   │
  │  Pointed 2-centered: H = V × (depends on rise)               │
  │  Pointed (steep): H significantly < semicircular              │
  │                                                                 │
  │  Higher rise → lower horizontal thrust                         │
  │  This is why Gothic cathedrals could build TALLER with LESS   │
  │  wall material than Romanesque predecessors                    │
  └────────────────────────────────────────────────────────────────┘

SEGMENTAL ARCH
==============
  • Less than semicircle (rise < span/2)
  • Higher horizontal thrust than semicircular
  • Used where headroom clearance limited
  • Requires substantial abutment

  Profile:  ╭───────────╮  (shallow arc)

JACK ARCH (flat arch)
=====================
  • Nearly horizontal — very shallow segmental
  • Very high horizontal thrust
  • Used for shallow floor arch between steel beams (19th century)
  • Requires steel tie rods or heavy abutments

  Profile:  ━━━━━━━━━━━━  (near flat, slight camber)
```

---

## Vault Types

A vault is an arch extended in depth — essentially an arch that covers a space rather than just spanning an opening.

```
VAULT TAXONOMY
==============

  BARREL VAULT (simplest)
  ┌──────────────────────────────────────────────────────────────────┐
  │  A semicircular arch extruded along its length                  │
  │                                                                   │
  │  ╭─────────────────────────────────────────────────╮            │
  │  │  continuous vault surface                        │            │
  │  ╰─────────────────────────────────────────────────╯            │
  │                                                                   │
  │  Problem: generates continuous lateral thrust along full length  │
  │  → requires continuous thick walls or buttresses                │
  │  Use: Roman halls, Romanesque naves, tunnels                    │
  └──────────────────────────────────────────────────────────────────┘

  GROIN VAULT (2 barrel vaults intersecting at right angles)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Two barrel vaults crossing → diagonal groins (lines of         │
  │  intersection) concentrate load at 4 corner piers               │
  │                                                                   │
  │     ╱───────╲                                                   │
  │    ╱  GROIN  ╲   ← diagonal groins (lines of intersection)    │
  │   ╱  vault    ╲                                                  │
  │  ╱─────────────╲                                                │
  │                                                                   │
  │  Advantage: load concentrates at 4 points → walls between      │
  │  piers freed from thrust → can have openings (windows)         │
  │  Use: Roman baths, Romanesque crossing vaults                  │
  └──────────────────────────────────────────────────────────────────┘

  RIB VAULT (Gothic revolution)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Diagonal ribs built first → guide infill panels (webs)         │
  │  Ribs are structural arch ribs in stone                         │
  │  Thin masonry webs (infill) between ribs                        │
  │                                                                   │
  │  Construction advantage:                                         │
  │  • Ribs built on light centering (temporary wooden formwork)   │
  │  • Webs infilled after ribs set                                 │
  │  • Centering removed rib by rib — never entire vault at once   │
  │                                                                   │
  │  Structural advantage:                                           │
  │  • Concentrated point loads at piers (not distributed wall)    │
  │  • Thin webs = lighter vault = less thrust                     │
  └──────────────────────────────────────────────────────────────────┘

  FAN VAULT (Late Gothic / Tudor)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Each support sprouts fan-shaped ribs of equal curvature        │
  │  Highly complex geometry; requires precision stone cutting      │
  │  Use: King's College Chapel (Cambridge), Henry VII Chapel       │
  │  Structure: more of a rigid shell than true rib-and-web system  │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Gothic Structural System: The Complete Picture

```
GOTHIC CATHEDRAL STRUCTURAL SYSTEM
=====================================

  PLAN:
  ┌──────────────────────────────────────────────────────────────────┐
  │  [BUTTRESS] [FLYING BUTTRESS]  [PIER]  [FLYING] [BUTTRESS]     │
  │                                                                   │
  │  OUTER AISLE    │    NAVE    │    OUTER AISLE                    │
  │                 │           │                                     │
  │  SIDE AISLE     │   (HIGH)  │    SIDE AISLE                     │
  │                 │   VAULT   │                                     │
  └──────────────────────────────────────────────────────────────────┘

  SECTION:
  ┌──────────────────────────────────────────────────────────────────┐
  │         RIB VAULT                                                │
  │       ╭───────────╮                                              │
  │      /             \   ← thrust vector at haunch                │
  │     /               \                                            │
  │  ──/──               ──\──  CLERESTORY WALL (large windows)    │
  │  │←FLYING BUTTRESS→     │                                       │
  │  │  (carries thrust     │                                       │
  │  │   over side aisle)   │                                       │
  │  │                      │                                       │
  │  BUTTRESS PIER           BUTTRESS PIER                          │
  │  (anchored by            (heavy masonry, sometimes with         │
  │   pinnacle weight)        decorative pinnacle as extra load     │
  │                           to keep thrust within base)           │
  └──────────────────────────────────────────────────────────────────┘

  HOW IT WORKS:
  1. Rib vault at nave generates outward thrust at haunch
  2. Flying buttress (half-arch) picks up thrust at haunch height
  3. Flying buttress carries thrust over side aisle roof
  4. Main buttress pier absorbs thrust and directs to ground
  5. Pinnacle adds vertical load → steepens resultant vector
     → keeps thrust line within buttress kern → no tension
```

The flying buttress is not ornamental — it is a structural arch in disguise, carrying the vault's horizontal thrust to the ground while leaving the clerestory wall free to be mostly glass.

---

## Domes: The Third Dimension

```
DOME GEOMETRY AND STRUCTURAL BEHAVIOR
======================================

  A dome = arch rotated 360° about vertical axis.
  Meridional stress (longitude lines): COMPRESSION throughout
  Hoop stress (latitude lines):
    Upper portion: COMPRESSION
    Lower portion: TENSION (at latitude > ~52° from crown)

  ┌──────────────────────────────────────────────────────────────────┐
  │     CROWN                                                        │
  │      │                                                            │
  │   ╔══╧══╗   ← meridional compression (arch behavior)           │
  │  ╔╝     ╚╗                                                       │
  │ ╔╝  COMP  ╚╗  hoop compression in upper dome                   │
  │╔╝──────────╚╗  ← transition zone (~52° from crown)             │
  │╚╗  TENSION  ╔╝  hoop tension in lower dome                     │
  │ ╚╗         ╔╝                                                    │
  │  ╚╗       ╔╝                                                     │
  │   ╚═══════╝   ← base: maximum hoop tension (cracks here!)      │
  │  [DRUM/RING BEAM]  ← resists hoop tension                      │
  └──────────────────────────────────────────────────────────────────┘
```

### Three Great Domes Compared

| Dome | Date | Diameter | Construction | Key Innovation |
|------|------|----------|-------------|----------------|
| Pantheon (Rome) | 125 CE | 142 ft | Cast Roman concrete (pozzolanic) | Reduced aggregate density toward crown; stepped buttressing rings |
| Hagia Sophia (Istanbul) | 537 CE | 102 ft | Brick on pendentives | Pendentives transfer circular dome to square plan; semi-domes absorb thrust |
| St. Peter's Basilica | 1590 CE | 136 ft | Brick + iron chains | Double shell; iron chain ring tension reinforcement at base — Michelangelo/Della Porta |

**Hoop tension management**:
- Pantheon: stepped rings around drum externally; aggregate density reduction (pumice near crown)
- Hagia Sophia: surrounding structure; four main piers absorb meridional thrust
- St. Peter's: three iron chains at base of drum added after cracks appeared

---

## Centering and Construction

```
ARCH CENTERING
==============

  Centering = temporary wooden framework supporting masonry
  during construction (before arch is self-supporting)

  PROCEDURE:
  ┌──────────────────────────────────────────────────────────────────┐
  │  1. Erect wooden centering to arch profile                      │
  │  2. Lay voussoirs from both sides toward crown simultaneously  │
  │     (balanced loading — prevents centering from tipping)       │
  │  3. Place keystone last                                         │
  │  4. Allow mortar to cure (or allow dry arch to consolidate)    │
  │  5. STRIKING THE CENTERING: lower gradually on wedges or       │
  │     sand jacks → arch springs into self-supporting action      │
  │  6. Monitor for cracking — small cracks at crown and           │
  │     haunches normal as thrust line readjusts                   │
  └──────────────────────────────────────────────────────────────────┘

  Gothic rib vault centering:
  • Light centering built for each rib individually
  • Web infill done between ribs after ribs set
  • Far less timber required than barrel vault (which needs
    centering for entire vault surface simultaneously)
  • This explains why Gothic building progressed faster —
    less centering timber to move, less scaffolding needed
```

---

## Decision Cheat Sheet

| Situation | Arch/Vault Choice |
|-----------|-----------------|
| Opening in masonry wall ≤ 6 ft | Brick soldier arch or segmental arch |
| Opening 6–16 ft | Semicircular or segmental arch with proper abutment |
| Large span, low thrust required | Pointed arch (Gothic two-centered) |
| Spanning rectangular room in masonry | Groin vault (concentrates loads at 4 corners) |
| Maximum height, slender walls | Gothic rib vault + flying buttresses |
| Complex decorative ceiling, Tudor aesthetic | Fan vault (King's College type) |
| Large open circular plan | Dome on drum (pendentives if square plan base) |
| Small arch, tight budget | Brick soldier course (flat arch, steel angle backup acceptable) |

---

## Common Confusion Points

**Keystone is not special structurally.** The keystone is the last voussoir placed and closes the arch, but all voussoirs carry equal compressive load. The keystone is architecturally prominent but structurally equivalent to its neighbors. Arches don't "need" the keystone — they need all voussoirs bearing against each other.

**Flying buttresses are arches.** They are often perceived as decorative extensions of the wall. They are structural half-arches carrying specific vault thrust vectors from haunch to ground. Remove the flying buttresses from Chartres Cathedral and the nave vault collapses outward within weeks.

**Three hinges = collapse, but a hinge is not a crack.** In masonry arch theory, a "hinge" is a point where the thrust line exits the arch section — the masonry is in contact at one edge with zero compression at the other. Small cracks at crown and haunches in old arches often indicate the arch has settled into a three-hinge configuration that is still stable (statically determinate but right at the limit). This is why old arches can be cracked and still standing.

**Catenary = only for self-weight.** Hooke's catenary is the ideal arch shape only when load is uniform per unit arc length (self-weight of uniform arch). For most real conditions (uniform horizontal load, or concentrated loads), the ideal thrust line is a parabola or more complex polynomial. The catenary is a good approximation for masonry arches of moderate span.
