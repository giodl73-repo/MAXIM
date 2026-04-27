# Structural Masonry: Load Paths, Slenderness, Reinforcement, and Codes

## The Big Picture

Structural masonry design has two modes: empirical (rule-of-thumb h/t limits, no calculation) and engineered (stress analysis per TMS 402/ACI 530). The governing standard in the US is **TMS 402** (Masonry Society / American Concrete Institute / ASCE). Modern reinforced masonry works similarly to reinforced concrete — steel takes tension, masonry takes compression.

```
STRUCTURAL MASONRY DESIGN DECISION TREE
========================================

  Is this a load-bearing masonry wall?
  ├── NO → Veneer or partition rules (see 09-MODERN-APPLICATIONS.md)
  └── YES
      ├── Is it in seismic design category (SDC) D, E, or F?
      │   ├── YES → SPECIAL REINFORCED MASONRY required (TMS 402 §7.4.6)
      │   │         Cannot use URM; must have rebar + grouted cores
      │   └── NO → Continue
      │
      ├── Is the slenderness ratio h/t within empirical limits?
      │   h = effective height, t = wall thickness
      │   ├── h/t ≤ 18 for URM → Empirical design possible
      │   └── h/t > 18       → Engineered design required
      │
      ├── Does the wall have eccentric loads or significant lateral loads?
      │   ├── YES → Engineered design (moment + axial)
      │   └── NO → Empirical may suffice (low-rise, simple geometry)
      │
      └── Select design method:
          ├── Allowable Stress Design (ASD) — TMS 402 Chapter 8
          └── Strength Design (SD)         — TMS 402 Chapter 9
```

---

## Load Paths in Masonry

```
VERTICAL LOAD PATH
==================

  ROOF LOAD
  ↓
  ROOF BEAM / JOIST → transfers to bearing wall
  ↓
  TOP BOND BEAM (reinforced CMU) — distributes concentrated loads
  ↓
  MASONRY WALL (compression in face shells and mortar joints)
  ↓
  FOOTING / FOUNDATION WALL
  ↓
  SOIL

  LATERAL LOAD PATH (wind / seismic)
  ===================================

  WIND PRESSURE on wall face
  ↓
  WALL (flexes out-of-plane like a vertical beam)
  ↓
  FLOOR/ROOF DIAPHRAGM (horizontal plate — distributes lateral load)
  ↓
  SHEAR WALLS (masonry walls parallel to load direction)
  ↓
  FOUNDATION

  KEY POINT: Masonry walls act as BOTH vertical load carriers AND
  shear walls (in-plane lateral resistance). Out-of-plane resistance
  requires either: (a) very thick wall, (b) reinforcement, or (c)
  limiting slenderness ratio (h/t).
```

---

## Compressive Strength: f'm

The design compressive strength of masonry (f'm) is determined by either:
1. **Unit strength method** (ASTM C270 Table 2): f'm from unit and mortar type
2. **Prism test method** (ASTM C1314): test prisms of actual construction

```
UNIT STRENGTH METHOD (simplified table)
=========================================

  Clay Masonry f'm (psi) by mortar type:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Unit Strength (psi)  │  Type M or S  │  Type N                  │
  │  ─────────────────────┼───────────────┼──────────────────────    │
  │  ≥14,000              │  5,300        │  4,400                 │
  │  ≥12,000              │  4,700        │  3,900                 │
  │  ≥10,000              │  4,000        │  3,300                 │
  │  ≥ 8,000              │  3,350        │  2,700                 │
  │  ≥ 6,000              │  2,700        │  2,200                 │
  │  ≥ 4,000              │  2,000        │  1,600                 │
  └──────────────────────────────────────────────────────────────────┘

  Concrete Masonry f'm (psi) by mortar type:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Unit Net Strength (psi)  │  Type M or S  │  Type N              │
  │  ─────────────────────────┼───────────────┼────────────────────  │
  │  ≥4,800                   │  3,000        │  2,500              │
  │  ≥3,750                   │  2,500        │  2,000              │
  │  ≥2,800                   │  2,000        │  1,500              │
  │  ≥1,900                   │  1,500        │  1,200              │
  └──────────────────────────────────────────────────────────────────┘

  Note: f'm for masonry is MUCH LOWER than unit alone — the assembly
  (including mortar joints and testing configuration) reduces strength
  by 40–70% compared to the individual unit.
```

---

## Slenderness Ratio (h/t)

The h/t ratio (effective height to wall thickness) is the primary slenderness check for unreinforced masonry.

```
SLENDERNESS LIMITS (TMS 402 Empirical Design)
===============================================

  UNREINFORCED MASONRY BEARING WALLS:
  ┌──────────────────────────────────────────────────────────────────┐
  │  h/t ≤ 18  for solid masonry                                     │
  │  h/t ≤ 18  for hollow masonry                                    │
  │  h/t ≤ 12  for walls with d/t > 25 (cavity/composite walls)      │
  └──────────────────────────────────────────────────────────────────┘

  h = effective height
  ┌──────────────────────────────────────────────────────────────────┐
  │  Both ends fixed   → h_eff = 0.5 × clear height                  │
  │  One end pinned    → h_eff = 0.7 × clear height                  │
  │  Both ends pinned  → h_eff = 1.0 × clear height                  │
  │  One end free      → h_eff = 2.0 × clear height (cantilever)     │
  └──────────────────────────────────────────────────────────────────┘

  EXAMPLE:
  8" CMU wall, floor-to-floor height 12 ft, top pinned to diaphragm:
  h_eff = 0.7 × 144" = 101"
  t = 7.625" actual
  h/t = 101 / 7.625 = 13.2 ≤ 18 → OK for empirical URM
```

---

## Unreinforced vs. Reinforced Masonry

```
URM vs. RM COMPARISON
======================

  UNREINFORCED MASONRY (URM)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Cross-section: solid or hollow (ungrouted)                      │
  │  Tension: masonry mortar only (very low)                         │
  │  Seismic: permitted SDC A, B, C only                             │
  │  Failure mode: brittle cracking at mortar joints                 │
  │  h/t limit: ≤ 18 for bearing walls                               │
  │  Advantage: simple, low cost                                     │
  └──────────────────────────────────────────────────────────────────┘

  REINFORCED MASONRY (RM)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Cross-section: CMU with grout in reinforced cells               │
  │                                                                  │
  │  ┌────────────────────────────────────────────────────┐          │
  │  │  [FACE][CORE w/rebar+grout][WEB][CORE ungrouted]   │         │
  │  └────────────────────────────────────────────────────┘         │
  │                                                                   │
  │  Tension: Steel rebar in grout core takes all tensile stress   │
  │  Seismic: All SDC permitted with proper detailing               │
  │  h/t limit: higher — up to 24–30 with special RM               │
  │  Ductility: Rebar develops flexural ductility (SDC D/E/F)      │
  └──────────────────────────────────────────────────────────────────┘

  HORIZONTAL REINFORCEMENT:
  Bond beams (reinforced CMU with horizontal rebar in grout) at:
  • 48" O.C. (or closer) — TMS 402 minimum for ordinary RM
  • Top of wall, over openings, at floor/roof connections
  • Ladder or truss-type joint wire reinforcement also used
```

---

## Reinforced Masonry Design Concepts

```
REINFORCED CMU WALL SECTION (ASD approach)
===========================================

  CROSS-SECTION AT REINFORCED CORE:
  ┌──────────────────────────────────────────────────────────────────┐
  │                  ← t = 7.625" →                                  │
  │  ┌──────┬────────────────────────┬──────┐                        │
  │  │FACE  │ GROUT                  │FACE  │ ← full grouted core   │
  │  │SHELL │   ─────  ← rebar (A_s)│SHELL │                       │
  │  │ 1.25"│         CENTERED       │ 1.25"│                       │
  │  └──────┴────────────────────────┴──────┘                       │
  └──────────────────────────────────────────────────────────────────┘

  STRESS DISTRIBUTION (ASD under combined axial + bending):
  ┌──────────────────────────────────────────────────────────────────┐
  │  fa = P / An  (axial compressive stress)                         │
  │  fb = M / Sn  (flexural stress)                                  │
  │                                                                  │
  │  Combined: fa/Fa + fb/Fb ≤ 1.0 (ASD interaction equation)        │
  │  where: Fa = 0.25 f'm × [1 - (h/140r)²]  for h/r ≤ 99            │
  │         Fb = 0.33 f'm  (flexural compression allowable)          │
  │         r  = radius of gyration of net section                   │
  └──────────────────────────────────────────────────────────────────┘
```

### Rebar Spacing in CMU

Standard 8×8×16 CMU has cores on 8" centers. Rebar can be placed:
- Every core: @ 8" O.C. (maximum reinforcement)
- Every other core: @ 16" O.C. (common)
- Every fourth core: @ 32" O.C. (minimum for some conditions)

Minimum grout consolidation: vibrate or rod in 16" lifts maximum. ASTM C476 fine or coarse grout per core clear dimension.

---

## Post-Tensioned Masonry (PTM)

Post-tensioned masonry uses high-strength steel rods or cables tensioned after masonry construction to pre-compress the wall. This suppresses net tension under lateral loads, allowing:
- Slender walls (h/t up to 50+ for low seismic)
- Single-wythe walls replacing cavity wall systems
- Repair of damaged URM buildings

```
POST-TENSIONED MASONRY CONCEPT
================================

  BEFORE PT:           UNDER LATERAL LOAD:    AFTER PT APPLIED:
  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
  │  Wall weight P  │  │  P + Moment M   │  │  P + PT + M     │
  │  (compression)  │  │  Tension on     │  │  PT force adds  │
  │                 │  │  windward face  │  │  compression;   │
  │                 │  │  CRACKING RISK  │  │  net = compress.│
  └─────────────────┘  └─────────────────┘  └─────────────────┘
                                              No net tension!

  PT HARDWARE:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Anchor plate at top of wall                                     │
  │  ↑                                                               │
  │  High-strength threaded rod or cable in CMU core (ungrouted      │
  │    or debonded sleeve)                                           │
  │  ↓                                                               │
  │  Anchor plate at foundation                                      │
  │                                                                  │
  │  Tensioning: hollow ram jack stretches rod against top plate     │
  │  Locking: nut or wedge anchor locks rod at target force          │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Out-of-Plane Bending

Masonry walls subjected to lateral loads (wind, seismic) bend out-of-plane. This is the critical design case for URM in wind and seismic applications.

```
OUT-OF-PLANE BENDING MODEL
===========================

  Wall supported top and bottom (pin-pin):
  ┌───────────────────────────────────────────────────────────────────┐
  │  FLOOR/ROOF DIAPHRAGM  ← lateral support (pin)                    │
  │         │                                                         │
  │         │   ← wind pressure w (uniform)                           │
  │         │   →→→→→→→→→→→→→→→                                       │
  │    WALL │                                                         │
  │         │   →→→→→→→→→→→→→→→                                       │
  │         │                                                         │
  │  FLOOR/FOUNDATION  ← lateral support (pin)                        │
  └───────────────────────────────────────────────────────────────────┘

  Maximum moment: M_max = w × h² / 8  (pin-pin, uniform load)

  For URM (no rebar):
    Tensile stress at max moment < f_r (modulus of rupture of masonry)
    TMS 402 f_r = 50–100 psi (varies by direction and mortar type)

  For RM (rebar in grouted core):
    Section behaves like singly-reinforced concrete flexural element
    Tension taken entirely by rebar
```

---

## Seismic Provisions (ASCE 7 / TMS 402)

```
SEISMIC DESIGN CATEGORY vs. MASONRY REQUIREMENTS
==================================================

  SDC   Seismic Risk    Masonry Requirement
  ────────────────────────────────────────────────────────────────
  A     Very low        Empirical design permitted; URM OK
  B     Low             Ordinary plain (URM) permitted
  C     Moderate        Detailed plain (limited URM) or
                        Ordinary RM required
  D     High            Intermediate RM or Special RM required
  E/F   Very high       SPECIAL REINFORCED MASONRY only (TMS 402 §7.4.6)

  SPECIAL REINFORCED MASONRY REQUIREMENTS (SDC D/E/F):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Vertical rebar: max spacing 48" in shear walls                  │
  │  Horizontal rebar: max spacing 48" in shear walls                │
  │  Minimum reinforcement: 0.0007 in each direction                 │
  │  Maximum reinforcement: complex formula (ductility limit)        │
  │  Full grouting: all cores in shear wall zones                    │
  │  Lap splice length: governed by development length in grout      │
  │  Inspection: Level C (continuous special inspection) required    │
  └──────────────────────────────────────────────────────────────────┘

  WHY MASONRY FAILS IN EARTHQUAKES:
  ┌──────────────────────────────────────────────────────────────────┐
  │  URM fails in shear → diagonal X-cracking in wall panels         │
  │  URM fails in flexure → bed joint sliding at base                │
  │  URM fails out-of-plane → wall overturns from its own inertia    │
  │                                                                  │
  │  RM resists all three IF: rebar properly placed + fully grouted  │
  │    + walls properly connected to diaphragm                       │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Engineered vs. Empirical Design

```
DESIGN METHOD COMPARISON
=========================

  EMPIRICAL DESIGN (TMS 402 Chapter 5):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Rules of thumb based on historical practice                     │
  │  No stress calculations required                                 │
  │  Limits: ≤3 stories OR ≤35 ft height, low seismic only           │
  │  Wall thickness minimums, h/t limits, bearing width requirements │
  │  Adequate for small, simple, low-seismic buildings               │
  └──────────────────────────────────────────────────────────────────┘

  ENGINEERED DESIGN — ASD (TMS 402 Chapter 8):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Working stress design                                           │
  │  Allowable stresses = fraction of f'm (safety factor embedded)   │
  │  Interaction equation: fa/Fa + fb/Fb ≤ 1.0                       │
  │  Simple to apply; conservative                                   │
  │  Industry standard for mid-20th century through today            │
  └──────────────────────────────────────────────────────────────────┘

  ENGINEERED DESIGN — Strength (TMS 402 Chapter 9):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Factored loads × load factors (matches LRFD philosophy)         │
  │  φ factors on nominal strength                                   │
  │  More complex; allows more economical designs                    │
  │  Required for some high-seismic applications                     │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Situation | Design Approach |
|-----------|----------------|
| 1-2 story residential, SDC A/B | Empirical design — h/t ≤ 18, standard proportions |
| 3+ story, any seismic zone | Engineered design required (TMS 402 ASD or SD) |
| SDC D/E/F (California, Pacific NW, New Madrid) | Special reinforced masonry — no exceptions |
| High slenderness wall (large window openings) | PT masonry or reinforced masonry required |
| Shear wall in lateral-force-resisting system | Reinforced; design in-plane shear and flexure |
| Upgrade existing URM building | Add bond beams, anchor to diaphragm, possibly PT |
| CMU retaining wall | Treat as cantilever — reinforced, ASD or SD |

---

## Common Confusion Points

**f'm is not the unit strength.** The assembly f'm is always lower than brick/CMU individual unit strength because it includes mortar joints, grout, and testing geometry effects. A 3,000 psi CMU with Type S mortar gives f'm ≈ 1,500–2,000 psi.

**h/t is effective height, not clear height.** End conditions matter. A wall with floor diaphragm connections top and bottom has fixed-fixed boundary conditions: h_eff = 0.5 × clear height. Using clear height is doubly conservative but overly penalizes well-connected construction.

**URM is not permitted in SDC D without major qualification.** Existing URM buildings in California and Pacific Northwest are a known seismic hazard. Mandatory retrofit programs (ASCE 41) address them. Do not design new URM in high seismic zones.

**Grouting CMU doubles structural calculations.** Grouted CMU uses gross area; ungrouted uses net area. Getting this backward (using gross area for ungrouted wall) can be a factor-of-two unconservative error. Check grouting intent before structural calcs.
