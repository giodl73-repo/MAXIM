# GD&T and Tolerancing (ASME Y14.5)

## The Big Picture

GD&T (Geometric Dimensioning and Tolerancing) replaces coordinate ± tolerancing with a formal language that specifies what geometric condition a feature must satisfy — not just where its center nominally falls.

```
COORDINATE TOLERANCING          GD&T (ASME Y14.5)
─────────────────────────────   ──────────────────────────────────────
X = 1.000 ± 0.010               ┌──────────────────────────────────┐
Y = 1.000 ± 0.010               │ ⌀0.500 ±0.002 │⌀│0.020│A│B│C│  │
                                 └──────────────────────────────────┘
Creates square tolerance zone    Feature control frame = complete
(0.020 × 0.020 = 0.0004 in²)    geometric specification

Actual circular zone:            Circular tolerance zone (⌀0.020):
⌀0.028 inscribed circle          area = π(0.010)² = 0.000314 in²
area = 0.000314 in²              57% more tolerance than square zone
                                 Same number, more usable geometry
```

**Key insight**: GD&T doesn't tighten tolerances — it accurately describes the geometry that actually matters. A hole position controls fit and function. Whether the center is at (1.009, 1.001) or (1.005, 1.005) is irrelevant to assembly as long as it's within a circle of specified diameter.

---

## The GD&T Symbol Set

### Characteristic Symbols (ASME Y14.5-2018)

```
FORM (no datum required)
  ─────────────────────
  ━━   Straightness          Line or axis must lie within two parallel lines/planes
  □    Flatness              Surface must lie within two parallel planes
  ○    Circularity           Cross-section must lie within two concentric circles
  ⌀    Cylindricity          Full cylinder within two coaxial cylinders

ORIENTATION (datum required)
  ──────────────────────────
  ∠    Angularity            Feature at specified angle to datum
  ⊥    Perpendicularity      Feature at 90° to datum
  ∥    Parallelism           Feature parallel to datum

LOCATION (datum required)
  ────────────────────────
  ⊕    True Position         Center within circular/cylindrical tolerance zone
  ◎    Concentricity         Center points coaxial to datum axis (form-related)
  ═    Symmetry              Feature symmetric about datum plane

RUNOUT (datum required, rotational)
  ──────────────────────────────────
  ↗    Circular Runout       Circular element variation during one revolution
  ↗↗   Total Runout          Full surface variation during all revolutions

PROFILE (may or may not need datum)
  ────────────────────────────────
  ⌒    Profile of a Line     2D cross-section within bilateral zone
  ⌓    Profile of a Surface  3D surface within bilateral zone
```

---

## The Feature Control Frame

Every GD&T callout lives in a feature control frame — read left to right:

```
┌──────┬──────────────┬────────┬────────┬────────┐
│  ⊕   │  ⌀ 0.020 M   │   A    │   B    │   C    │
└──────┴──────────────┴────────┴────────┴────────┘
   │           │           │       │       │
   │           │           └───────┴───────┘
   │           │                   │
Characteristic  Tolerance       Datum references
(True Position) value and zone  (primary, secondary,
                 modifiers       tertiary)
```

### Tolerance Zone Modifiers

| Symbol | Name | Meaning |
|--------|------|---------|
| (none) | RFS — Regardless of Feature Size | Tolerance applies at any size. Default in Y14.5-2018. |
| M | MMC — Maximum Material Condition | Bonus tolerance when feature departs from MMC. Most common for clearance holes. |
| L | LMC — Least Material Condition | Bonus tolerance when feature departs from LMC. Used for wall thickness, structural applications. |
| P | Projected Tolerance Zone | Zone extends into mating part space. Long studs, pins. |
| F | Free State | Applied to non-rigid parts in free state (sheet metal, rubber). |

---

## The Datum Reference Frame

The datum system provides the coordinate frame from which measurements are made.

```
DATUM REFERENCE FRAME (DRF)
─────────────────────────────────────────────────
Datum A (primary)    ── constrains 3 DOF
  Flat surface → removes 3 translational DOF
  (plane contact)    Actually: Z translation + X rot + Y rot

Datum B (secondary)  ── constrains 2 more DOF
  Edge or surface → removes 2 more DOF
  (line contact)

Datum C (tertiary)   ── constrains 1 more DOF
  Point or stop → removes last DOF
  (point contact)

Result: 6 DOF fully constrained.
        Part location completely defined.
        All measurements made from this frame.
```

### Datum Setup Reality

```
Inspection Fixture:
                        ┌─────────────────────────┐
                        │         Part            │
         Datum A ───────┤  (rests flat on plate)  │── 3-2-1 setup
         (bottom face)  │                         │
                        └─────┬─────────┬─────────┘
                              │         │
                        Datum B      Datum C
                       (back edge)  (side stop)
```

The 3-2-1 method: 3 points define primary plane (A), 2 points define secondary line (B), 1 point defines tertiary (C). This eliminates all rigid body degrees of freedom.

---

## Fits and Limits (ISO 286 / ASME B4.1)

### The Fit System

```
HOLE-BASIS SYSTEM (most common in US)
─────────────────────────────────────
Hole is fundamental (H = lower deviation at zero).
Shaft varies to achieve desired fit.

  CLEARANCE FIT          TRANSITION FIT         INTERFERENCE FIT
  ──────────────         ──────────────         ────────────────
  Shaft < Hole           Shaft ≈ Hole           Shaft > Hole
  Always a gap           May be + or –          Always press required

  ┌──────┐               ┌──────┐               ┌──────┐
  │ H7   │               │ H7   │               │ H7   │
  │ hole │               │ hole │               │ hole │
  └──────┘               └──────┘               └──────┘
    │                      │                      │
  g6 shaft              k6 shaft               p6 shaft
  (sliding fit)         (locating fit)         (press fit)
```

### Common Fit Designations

| Fit Code | Type | Application |
|----------|------|-------------|
| H7/g6 | Clearance — sliding | Shafts in bearings, sliding components |
| H7/h6 | Clearance — close running | Accurate location, easy assembly |
| H7/k6 | Transition — locating | Gears, pulleys — light press or clearance |
| H7/n6 | Transition — push | Hubs, close-fit bushings |
| H7/p6 | Interference — press | Standard press fit, removable by tool |
| H7/s6 | Interference — shrink | Permanent assembly, high torque |

### Fit Calculation

```
Example: 25mm H7/g6
─────────────────────────────────────────────────────────────────
H7 hole:  ⌀25.000 +0.021 / 0.000   → 25.000 to 25.021 mm
g6 shaft: ⌀25.000 −0.007 / −0.020  → 24.980 to 24.993 mm

Maximum clearance:  25.021 − 24.980 = 0.041 mm (largest hole, smallest shaft)
Minimum clearance:  25.000 − 24.993 = 0.007 mm (smallest hole, largest shaft)
Always clearance: shaft is always smaller than hole.
```

---

## True Position Calculation

Position tolerance controls where a feature center can be relative to its nominal location.

```
Nominal hole center:  X = 1.000, Y = 1.000
Actual hole center:   X = 1.008, Y = 1.005

Deviation: ΔX = 0.008, ΔY = 0.005

Diametral deviation = 2 × √(ΔX² + ΔY²)
                    = 2 × √(0.064 + 0.025)
                    = 2 × √(0.089)
                    = 2 × 0.0082
                    = 0.0164" (the diametral position error)

If tolerance = ⌀0.020", this hole PASSES (0.0164 < 0.020).
If tolerance were ±0.010" (square zone), it would FAIL
(ΔX = 0.008 < 0.010, ΔY = 0.005 < 0.010 — wait, it passes)
But ΔX = 0.010, ΔY = 0.010 would fail circular, pass square.
The key: square zones accept corners that may fail functional assembly.
```

---

## Bonus Tolerance (MMC)

When a hole is at MMC (smallest allowed diameter), clearance for the mating pin is minimum — so position tolerance must be tightest. As the hole grows, bonus clearance exists — more positional slop is acceptable.

```
Hole: ⌀0.500 +0.010/0.000
Position: ⌀0.020 M (at MMC)

MMC (smallest hole) = ⌀0.500  → position tol = ⌀0.020 (stated)
VC  (virtual cond.) = ⌀0.500 − 0.020/2...

Actually simpler:
MMC of hole = 0.500
Actual size = 0.508  → departed from MMC by 0.008
Bonus tolerance   = 0.008
Total position tol = 0.020 + 0.008 = 0.028 ⌀

Actual size = 0.510 (LMC)
Bonus        = 0.010
Total tol    = 0.030 ⌀
```

**Virtual Condition** = the worst-case mating envelope:
- External feature (shaft) at MMC: VC = MMC + position tolerance
- Internal feature (hole) at MMC: VC = MMC − position tolerance

Gauges (Go/No-Go) check virtual condition.

---

## Profile Tolerances

Profile is the most general GD&T characteristic — it can control size, form, orientation, and location simultaneously.

```
PROFILE OF A SURFACE
─────────────────────
Bilateral profile: tolerance zone extends equally each side of nominal
  ┌──────────────┐
  │  0.030 ⌓ A  │  → surface must lie within 0.015 each side of true
  └──────────────┘    profile relative to datum A

Unilateral profile (Y14.5-2018):
  ┌──────────────────────┐
  │  0.030 ⌓ A  U 0.010 │  → 0.010 outside nominal, 0.020 inside
  └──────────────────────┘
```

Profile replaces separate size + form + location callouts for complex surfaces (airfoils, cam profiles, freeform geometry). It's the right tool when coordinate tolerancing becomes unmanageable.

---

## Inspection Methods

| Feature | Inspection Method |
|---------|------------------|
| Diameter, length | Micrometer, caliper, air gauge |
| Position, concentricity | CMM (coordinate measuring machine) |
| Flatness | Surface plate + dial indicator or CMM |
| Roundness / cylindricity | Roundness tester (Talyrond) or CMM |
| Surface finish | Profilometer (contact or optical) |
| Complex profiles | CMM with surface scanning |
| Runout | V-blocks + dial indicator or CMM |
| Go/No-Go | Functional gauges (check virtual condition) |

### CMM Process

```
Part → CMM bed → Probe touches → Point cloud →
→ Software fits geometric primitives →
→ Compares to nominal (CAD or drawing) →
→ Pass/fail per each GD&T callout
```

Modern CMMs bridge directly to CAD: PMI (Product Manufacturing Information) attached to 3D models drives inspection programs automatically — this is ASME Y14.41 Model-Based Definition.

---

## Common GD&T Application Patterns

### Hole Pattern (bolt circle)

```
Typical callout for a 4-hole bolt circle:
  Each hole: ⌀0.500 +0.010/0.000
  Position:  ⌀0.020 M  A  B  C

Means: each hole's axis must fall within ⌀0.020
(or more with bonus) cylindrical zone relative
to the DRF defined by A, B, C.
All holes checked simultaneously for pattern.
```

### Shaft in Housing

```
Shaft OD:   ⌀25.000 −0.000/−0.013   (h6 tolerance)
Roundness:  0.003 ○                  (circularity)
Runout:     0.010 ↗ A               (total to bearing datum)
Surface:    Ra 0.4                   (profilometry)
```

### Mating Flat Surfaces

```
Primary face:  0.005 □              (flatness — form only, no datum)
Perpendicular: 0.010 ⊥ A           (to datum A face)
Bolt holes:    ⌀0.020 M ⊕ A B C   (position at MMC)
```

---

## Decision Cheat Sheet

| I want to control... | Use |
|----------------------|-----|
| Hole/shaft size only | Plus/minus on diameter |
| Hole center location relative to datums | True Position (⊕) |
| Shaft wobble during rotation | Total Runout (↗↗) |
| Flatness of a surface | Flatness (□) — no datum needed |
| Two surfaces parallel to each other | Parallelism (∥) |
| Two surfaces perpendicular | Perpendicularity (⊥) |
| Freeform or complex surface | Profile of a Surface (⌓) |
| Maximum position error (bonus OK) | Position with MMC (M) modifier |
| Bearing surface — no bonus allowed | Position RFS (no modifier) |
| Concentricity / coaxiality | Position or Concentricity (◎) |

---

## Common Confusion Points

**RFS is the default in Y14.5-2018**: Earlier editions (2009 and prior) required the RFS symbol (S) if you wanted regardless-of-feature-size. The 2018 edition makes RFS the default. Explicitly calling MMC now requires the M circle. Check which edition your drawings reference.

**Circularity vs cylindricity**: Circularity is per cross-section (2D). Cylindricity is the whole surface (3D). Cylindricity is tighter — it includes circularity + straightness + taper.

**Datum vs datum feature**: The datum is the theoretical perfect plane/axis/point used for measurement. The datum feature is the actual imperfect surface on the part that approximates it. CMMs fit an ideal plane to the datum feature surface.

**Profile vs position for holes**: Position controls hole center location. Profile controls the full geometry of the hole including size and form. Use position for fastener holes. Use profile for precision features where all geometric aspects matter simultaneously.

**Virtual condition and gauging**: A fixed-size gauge checks whether the feature at its worst case (MMC + maximum positional error) would still assemble. That worst-case envelope IS the virtual condition. Go gauges = check virtual condition (will the mating part fit?). No-Go gauges = check that the feature hasn't exceeded LMC (wall too thin?).
