# Bricklaying: Bond Patterns, Leads, Corners, and Field Methodology

## The Big Picture

Bricklaying is a sequenced process: establish a corner lead, fill between leads course by course, maintain plumb/level/range with a line. Bond pattern determines both structural behavior (overlap distributes load, ties wythes together) and visual character. The lead is the key concept — it sets vertical control for all in-between courses.

```
BRICKLAYING WORKFLOW
====================

  1. ESTABLISH LEADS (corners)          2. FILL BETWEEN LEADS
  ┌─────────────────────────┐           ┌─────────────────────────┐
  │   A         B           │           │   A ─────────────── B   │
  │  ███                    │           │  ███████████████████    │
  │ █████       █████       │     →     │ █████████████████████   │
  │███████     ███████      │           │███████████████████████  │
  │  Lead A    Lead B       │           │  leads set level        │
  │  (5-7      (5-7         │           │  line pulled between    │
  │  courses   courses      │           │  at each course         │
  │  tall)     tall)        │           │                         │
  └─────────────────────────┘           └─────────────────────────┘

  3. QUALITY CHECKS:
  ┌────────────────────────────────────────────────────────────────┐
  │  PLUMB  — each lead face is vertical (level bubble or 4' level)│
  │  LEVEL  — bed joints are horizontal (mason's 4' level)         │
  │  RANGE  — line pulled tight between leads: each course aligns  │
  │  COURSE — story pole confirms cumulative course height         │
  └────────────────────────────────────────────────────────────────┘
```

---

## Bond Patterns

### Running Bond (Stretcher Bond)

The most structurally efficient and most common bond. Each unit overlaps the one below by half its length (1/2 bond) or 1/3 of its length (1/3 bond).

```
RUNNING BOND (1/2 bond offset)
================================

  Course 3: |  3  |  4  |  5  |  6  |
  Course 2:   |  1  |  2  |  3  |  4  |
  Course 1: |  A  |  B  |  C  |  D  |

  ┌────┬────┬────┬────┬────┬────┐
  │    │    │    │    │    │    │  Course 3
  ├──┬─┴─┬──┴─┬──┴─┬──┴─┬──┴──┤
  │  │   │   │   │   │   │   │  Course 2
  ├──┴─┬──┴─┬──┴─┬──┴─┬──┴───┤
  │    │    │    │    │    │     Course 1
  └────┴────┴────┴────┴────┘

  Structural behavior: excellent load distribution
  Visual: uniform horizontal emphasis
  Use: single-wythe walls, veneer, CMU
  Note: in single-wythe, this is the ONLY structural option
```

### Flemish Bond

Alternating stretchers (long face out) and headers (short face out) in every course, with headers centered over stretchers below.

```
FLEMISH BOND
=============

  Course 4:  |S|H|S|H|S|H|S|H|    S = Stretcher (long face)
  Course 3:  |H|S|H|S|H|S|H|S|    H = Header (short face)
  Course 2:  |S|H|S|H|S|H|S|H|
  Course 1:  |H|S|H|S|H|S|H|S|

  ASCII representation:
  ┌────┬──┬────┬──┬────┬──┬────┐
  │    │  │    │  │    │  │    │  Course 4 (S H S H)
  ├──┬─┴──┴─┬──┴──┴─┬──┴──┴──┤
  │  │      │      │       │  │  Course 3 (H S H S)
  ├──┴──┬───┴──┬────┴──┬────┴─┤
  │     │      │       │      │  Course 2 (S H S H)
  └─────┴──────┴───────┴──────┘

  Structural purpose: headers tie front and back wythes together
  Visual: elegant alternating pattern
  Use: traditional 2-wythe solid brick walls
  Closure brick: in closures, a "bat" (half-brick) is placed to
    maintain the bond pattern at openings and corners
```

### English Bond

Alternate courses of all-stretchers and all-headers. Headers tie the two wythes together every other course — stronger wall tie than Flemish.

```
ENGLISH BOND
=============

  Course 4:  |S|S|S|S|S|S|S|  ← all stretchers
  Course 3:  |H|H|H|H|H|H|H|  ← all headers
  Course 2:  |S|S|S|S|S|S|S|  ← all stretchers
  Course 1:  |H|H|H|H|H|H|H|  ← all headers

  ┌──┬──┬──┬──┬──┬──┬──┬──┬──┐
  │  │  │  │  │  │  │  │  │  │  Course 4 (stretchers)
  ├──┴──┴──┴──┴──┴──┴──┴──┴──┤
  │                           │  Course 3 (headers — solid band)
  ├──┬──┬──┬──┬──┬──┬──┬──┬──┤
  │  │  │  │  │  │  │  │  │  │  Course 2 (stretchers)
  ├──┴──┴──┴──┴──┴──┴──┴──┴──┤
  │                           │  Course 1 (headers)
  └───────────────────────────┘

  Structural purpose: maximum wythe integration
  Visual: strong horizontal banding
  Use: heavy structural walls, chimneys, industrial buildings
```

### Stack Bond

No overlapping — all head joints align vertically. Zero lateral load distribution across joints.

```
STACK BOND (STRUCTURAL WARNING)
=================================

  ┌──────┬──────┬──────┬──────┐
  │      │      │      │      │
  ├──────┼──────┼──────┼──────┤  ← continuous vertical joint = weakness
  │      │      │      │      │
  ├──────┼──────┼──────┼──────┤  ← no interlocking across joints
  │      │      │      │      │
  └──────┴──────┴──────┴──────┘

  Structural behavior: POOR — joints form continuous planes of weakness
  Required reinforcement: horizontal joint reinforcement (ladder or truss
    type) every 16" vertically to provide lateral continuity
  Use: purely decorative; contemporary aesthetic; must have joint reinf.
  Never use: unreinforced stack bond in structural applications
```

### Structural vs. Decorative Bonds Summary

| Bond | Wythe Integration | Structural Suitability | Notes |
|------|-----------------|----------------------|-------|
| Running (1/2) | Single wythe | Excellent | Most common |
| Running (1/3) | Single wythe | Very good | Wider units |
| Flemish | Full (headers) | Good | Classic 2-wythe |
| English | Full (headers) | Excellent | Maximum tie |
| Stack | None | Poor | Decorative only; requires joint reinf. |
| Common/American | Headers every 6th course | Good | 19th century standard |

---

## Course Height and Story Pole

```
COURSE HEIGHT CALCULATION
==========================

  For modular brick (2-1/4" actual height + 3/8" mortar joint):
  One course height = 2-1/4" + 3/8" = 2-5/8"
  3 courses         = 3 × 2-5/8" = 7-7/8" ≈ 8" (nominal modular)

  STORY POLE (rod pole):
  ┌──────────────────────────────────────────────────────────────────┐
  │  A story pole is a vertical rod marked at each course height     │
  │  Pre-marked to show: sill heights, lintel heights, floor heights │
  │                                                                  │
  │  Purpose: Maintain uniform joint thickness without measuring     │
  │           every course. Mark once, use throughout project.       │
  │                                                                  │
  │  Mark locations (typical 8' wall, modular brick, 3 courses=8"):  │
  │  8", 16", 24", 32", 40", 48" (sill), 56", 64", 72", 80" (arch) │
  │                                                                  │
  │  RULE: If courses don't hit marks, mortar joint is wrong.        │
  │        Adjust mortar joint thickness — never cut brick.          │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Lead Construction

The lead is a pyramid-shaped section of brick at a corner, typically 5–7 courses tall. It sets both the vertical alignment and the horizontal bond pattern for the entire wall run between two leads.

```
CORNER LEAD CONSTRUCTION (Running Bond, 5-course lead)
=======================================================

  VIEW FROM CORNER (perspective):

  Course 5:  ▓
  Course 4:  ▓▓
  Course 3:  ▓▓▓
  Course 2:  ▓▓▓▓
  Course 1:  ▓▓▓▓▓

  Each course steps back one half-brick → racked-back pyramid shape

  PROCEDURE:
  Step 1: Bed first course on clean, dampened substrate
          Butter face shell ends for head joints
          Check level in both directions, plumb corner brick

  Step 2: Lay second course: offset first brick by 1/2 unit (running bond)
          Maintain 3/8" bed and head joints consistently

  Step 3: Check after every 2 courses:
          • PLUMB: level against face of lead (both faces)
          • LEVEL: level bed joint (both directions at corner)
          • TWIST: diagonal check — no racking out of plane

  Step 4: Repeat to desired lead height (5–7 courses typical)

  Step 5: Set opposite lead to same height; pull line between
```

---

## Corners, Reveals, and Jambs

```
CORNER GEOMETRY: RUNNING BOND
===============================

  PLAN VIEW OF CORNER (alternating courses):

  Course 1:          Course 2:
  ┌────┬────┐         ┌──┬────┬──┐
  │    │    │         │  │    │  │
  │    ├────┤         ├──┤    ├──┤
  │    │    │         │  │    │  │
  └────┴────┘         └──┴────┴──┘

  REVEALS: The set-back of the masonry at a window/door frame
  ┌──────────────────────────────────────────────────────────────────┐
  │  Window frame      │ ← reveal dimension (typically 1/2"–1")      │
  │  ────────────      │                                             │
  │  [   glass   ]     │  Reveal must be consistent course-to-course │
  │  ────────────      │  Marks end of wythe; requires closure brick │
  └──────────────────────────────────────────────────────────────────┘

  JAMB: Vertical edge of opening in masonry wall
  Brick jambs must be carefully planned so that the bond pattern
  works out without awkward cuts at the jamb.
```

---

## Closure Brick (Bat Placement in Flemish Bond)

The closure is the final brick placed in a course to complete a run. Its position is determined by the bond pattern — in Flemish bond, this requires a "bat" (half-brick).

```
CLOSURE IN FLEMISH BOND
========================

  Problem: The last space in a Flemish bond course may be a header position.
  A full header = 3-5/8" wide. If remaining space ≠ 3-5/8", a closure is needed.

  CLOSURE TYPES:
  ┌────────────────────────────────────────────────────────────────┐
  │ QUEEN CLOSER: Brick split along length = half-width unit       │
  │  Use: In Flemish bond to start/end a course at corner          │
  │  Position: Placed next to corner header to "close" the bond    │
  │                                                                │
  │  [H][QC][S][H][S][H][S][CORNER]                                │
  │       ↑                                                        │
  │  Queen closer adjusts spacing to maintain bond pattern         │
  │                                                                │
  │ KING CLOSER: Brick cut diagonally                              │
  │  Use: Turning corners in Flemish bond                          │
  │                                                                │
  │ BAT: Brick cut to 1/2 length                                   │
  │  Use: Filling end position in running bond                     │
  └────────────────────────────────────────────────────────────────┘

  CLOSURE PROCEDURE:
  1. Butter all four sides of closure brick heavily
  2. Slide into position from above (never push from side)
  3. The buttered mortar is compressed on all faces simultaneously
  4. Do not disturb adjacent bricks during placement
```

---

## Plumb, Level, and Range Methodology

```
QUALITY CONTROL SEQUENCE
=========================

  TOOL: Mason's line (string line pulled taut between leads)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Lead A ────────────────────────────────────────── Lead B        │
  │          ← string line at top of course height →                 │
  │          Each brick's top edge aligns with string                │
  │          Leave 1/16" gap between string and brick face           │
  │          (touching string bows it → course bulges out)           │
  └──────────────────────────────────────────────────────────────────┘

  THREE CHECKS:
  ┌────────────────────────────────────────────────────────────────┐
  │  PLUMB: Is the face of the wall vertical?                      │
  │    Tool: 4-foot mason's level held vertically against face     │
  │    Tolerance: 1/4" in 10 feet max (ACI 530.1 / TMS 602)        │
  │                                                                │
  │  LEVEL: Are bed joints horizontal?                             │
  │    Tool: 4-foot mason's level held horizontally on bed joint   │
  │    Tolerance: 1/8" in 10 feet max                              │
  │                                                                │
  │  RANGE: Are bricks in plane along the run?                     │
  │    Tool: String line pulled between leads                      │
  │    Tolerance: 1/16" gap between string and each brick          │
  └────────────────────────────────────────────────────────────────┘

  JOINT THICKNESS TOLERANCE (ASTM C270):
  Bed joint: 3/8" ± 1/8" (1/4" to 1/2" range acceptable)
  Head joint: 3/8" ± 1/8"
  Collar joint (cavity): 3/4" to 1" typical
```

---

## Decision Cheat Sheet

| Situation | Bond and Method Choice |
|-----------|----------------------|
| Single-wythe CMU wall | Running bond — only option without headers |
| Traditional 2-wythe brick, maximum strength | English bond — headers every course |
| Traditional 2-wythe brick, classic appearance | Flemish bond — headers every course alternate |
| Contemporary aesthetic, flat joints | Running bond (1/2 or 1/3 offset) |
| Stack bond (aesthetic requirement) | Horizontal joint reinforcement every 16" — required |
| Repair existing Flemish bond wall | Match existing bond exactly — use queen closures |
| Tall lead required (over 7 courses) | Use corner poles (metal guides) instead of masonry leads |

---

## Common Confusion Points

**Flemish bond requires bats (half-bricks) at corners.** The alternating header/stretcher pattern means that at a right-angle corner, you need a queen closer or bat to maintain the stagger. Missing this produces a "false bond" where head joints run continuously around the corner.

**Stack bond is not a bond.** In structural terms, stack bond has no interlocking — it's a pattern, not a bond. Always requires horizontal reinforcement (ladder wire) embedded in bed joints to distribute lateral forces across the continuous vertical joint planes.

**String line gap is critical.** The string line is set at the top face of each brick, not the mortar line. Touching the string with the brick bows the line outward and produces a course that bellies out over its run. The 1/16" gap is intentional.

**Story pole corrects joint accumulation errors.** Without a story pole, slight variations in joint thickness compound course by course. A 1/16" error per course becomes 3/4" error in 12 courses. The story pole catches this before it becomes irreversible.

**Lead height vs. wall height.** Leads are typically 5–7 courses before the fill-in between leads is laid. If leads get too far ahead of the field, vertical differential settlement can occur before mortar sets. Maximum lead-to-field height difference: about 4 feet in most specifications.
