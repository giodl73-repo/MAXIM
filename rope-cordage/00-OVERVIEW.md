# Rope and Cordage — Landscape Overview

## The Big Picture

Rope is a composite structure: fibers twisted or braided into yarns, yarns into strands, strands into rope. Each level of the hierarchy trades some tensile efficiency for structural stability, handling properties, and resistance to failure by kinking, bending, or untwisting. The central design tension is between strength (maximized by straight parallel fibers) and usefulness (maximized by the helical twist that gives the rope its ability to be coiled, knotted, and handled).

```
ROPE STRUCTURE HIERARCHY
========================

  FIBER           YARN              STRAND          ROPE
  (individual     (parallel or      (multiple        (3-strand or
   filament)       twisted fibers)   yarns twisted     braided
                                     together)         together)

  ┌──────┐       ┌──────────┐      ┌─────────────┐  ┌─────────────┐
  │ ~~   │  →    │ ≋≋≋≋≋≋≋ │  →   │  STRAND 1   │  │  ╭───────╮  │
  │ ~~   │       │ (Z-twist)│      │  (3 yarns)  │  │  │ ╭───╮ │  │
  │fiber │       │          │      │  STRAND 2   │ →│  │ │   │ │  │
  └──────┘       └──────────┘      │  (3 yarns)  │  │  │ ╰───╯ │  │
                                    │  STRAND 3   │  │  ╰───────╯  │
                                    └─────────────┘  └─────────────┘

  EACH LEVEL ADDS:
  • Structural coherence (won't fall apart when cut)
  • Bending compliance (can coil without kinking)
  • Load distribution (no single fiber takes all load)
  • Manufacturing tractability (can be produced continuously)

  EACH LEVEL COSTS:
  • Tensile efficiency (helix angle means fibers not purely axial)
  • Some elongation increase (helix straightens under load)
```

---

## Construction Methods

```
TWISTED (LAID) ROPE
===================

  3-strand hawser laid (classic):
  Z yarn → S ply → Z strand → S rope
  (alternating direction at each level = balanced, won't self-unlay)

  Cross-section view:          Side view:
  ┌─────────────────────┐     ┌────────────────────────────────────┐
  │   STRAND 1  ╮        │     │  /\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\ │
  │  ╱──────────╯        │     │  Left lay: S on the body         │
  │  STRAND 2            │     │  Right lay: Z on the body        │
  │  ╱──────────╮        │     │  (most rope is right-lay = Z)    │
  │  STRAND 3  ╯         │     └────────────────────────────────────┘
  └─────────────────────┘

  BRAIDED ROPE
  ============

  Round braid: carriers interlace diagonally
  ┌──────────────────────────────────────────────────────────────────┐
  │  8-carrier braid:  4 clockwise + 4 counterclockwise            │
  │  16-carrier braid: 8 + 8 (tighter, rounder, smoother)         │
  │  Hollow braid: no core — can accept core for double-braid      │
  │  Solid braid: fully filled cross-section                        │
  └──────────────────────────────────────────────────────────────────┘

  KERNMANTLE (core-and-sheath):
  ┌──────────────────────────────────────────────────────────────────┐
  │  KERN: parallel fiber core (takes 70–80% of load)              │
  │  MANTLE: braided sheath (abrasion protection, handling)        │
  │  Cross-section:  [sheath ═══ CORE ═══ sheath]                  │
  │  Use: climbing rope, technical rescue                           │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Natural vs. Synthetic: The Revolution

```
NATURAL vs. SYNTHETIC FIBER COMPARISON
========================================

  ERA 1 (antiquity – 1930s): NATURAL FIBERS ONLY
  ┌────────────────────────────────────────────────────────────────┐
  │ Hemp: workhorse of sailing rigging (300–900 MPa tensile)      │
  │ Manila (abaca): superior to hemp for marine use               │
  │ Sisal: cheaper, less durable — baling twine                   │
  │ Cotton: soft, low strength — clothing, light use              │
  │ Jute: low strength, high absorption — burlap, packaging       │
  │ Coir (coconut): buoyant, rot-resistant, low strength          │
  └────────────────────────────────────────────────────────────────┘

  ERA 2 (1938–1980s): FIRST-GENERATION SYNTHETICS
  ┌────────────────────────────────────────────────────────────────┐
  │ Nylon (PA 6/6.6, DuPont 1938): 10× manila strength, elastic  │
  │ Polyester (PET, ICI 1941): lower stretch than nylon, marine   │
  │ Polypropylene (PP, 1950s): cheap, floats, weak UV degradation │
  └────────────────────────────────────────────────────────────────┘

  ERA 3 (1980s–present): HIGH-PERFORMANCE SYNTHETICS
  ┌────────────────────────────────────────────────────────────────┐
  │ UHMWPE (Dyneema/Spectra, DSM 1979): 15× steel by weight      │
  │ Aramid (Kevlar/Technora, DuPont 1965): heat-resistant         │
  │ Vectran (liquid crystal polymer, Kuraray): ultra-low creep    │
  │ PBO (Zylon, Toyobo): highest strength, UV degradation warning │
  └────────────────────────────────────────────────────────────────┘

  PERFORMANCE SNAPSHOT:
  ┌───────────────────────────────────────────────────────────────────────┐
  │ Fiber          Tensile (MPa)  Elongation%  Density(g/cc)  UV stable? │
  │ ─────────────────────────────────────────────────────────────────────│
  │ Hemp (natural) 300–900        2–4%          1.4–1.5        Moderate  │
  │ Nylon 6.6      900–1,000      20–30%         1.14          Good      │
  │ Polyester      800–1,100      10–15%         1.38          Good      │
  │ Polypropylene  300–500        15–25%         0.91          Poor      │
  │ UHMWPE (Dyn.)  2,400–3,600   3–4% (rope)    0.97          Moderate  │
  │ Kevlar 29      2,900–3,600   3.6%            1.44          Poor      │
  │ Vectran HS     2,850–3,340   3.3%            1.41          Moderate  │
  │ PBO (Zylon)    5,800         3.5%            1.56          Very poor │
  └───────────────────────────────────────────────────────────────────────┘
```

---

## Applications by Rope Type

```
APPLICATION MAP
===============

  ┌─────────────────────────────────────────────────────────────────┐
  │  MARINE SAILING (see 07-MARINE-APPLICATIONS.md)                │
  │  Standing rigging: stainless wire or Dyneema (low stretch)     │
  │  Running rigging: polyester (sheets, halyards)                 │
  │  Mooring: nylon (stretch absorbs surge)                        │
  └─────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────┐
  │  CLIMBING / RESCUE (see 08-INDUSTRIAL-USE.md)                  │
  │  Dynamic climbing: nylon kernmantle (UIAA/EN 892)              │
  │  Static rescue: low-elongation polyester kernmantle (NFPA 1983)│
  │  Life safety escape: polyester or nylon, 5:1 min safety factor │
  └─────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────┐
  │  LIFTING / RIGGING (see 08-INDUSTRIAL-USE.md)                  │
  │  Wire rope: steel, torque-balanced, safety factor 5:1 to 8:1  │
  │  Synthetic slings: web, round-sling, polyester or nylon        │
  │  Chain: for high-temperature, abrasion-exposed applications    │
  └─────────────────────────────────────────────────────────────────┘
  ┌─────────────────────────────────────────────────────────────────┐
  │  HIGH-PERFORMANCE APPLICATIONS (see 09-MODERN-SYNTHETICS.md)   │
  │  Offshore moorings: UHMWPE (Dyneema) for buoyancy + strength  │
  │  Racing yacht rigging: Vectran (low creep)                     │
  │  Aerospace: Zylon/Kevlar (weight-critical, not UV exposed)     │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Strength Terminology

```
ROPE STRENGTH TERMS
===================

  MBS (Minimum Breaking Strength) = Breaking Strength:
  Lowest breaking load from testing (not average — minimum)
  Also called BL (Breaking Load), ASTM F1623 / BS EN 919

  WLL (Working Load Limit) = SWL (Safe Working Load):
  Maximum load allowed in normal service
  WLL = MBS / Safety Factor (SF)

  SAFETY FACTORS BY APPLICATION:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Application         SF Typical   Comments                      │
  │  ─────────────────────────────────────────────────────────────── │
  │  Crane lifting        5:1 – 8:1   ASME B30; depends on mode    │
  │  Life safety          10:1        NFPA 1983 (rescue ropes)     │
  │  Marine mooring       5:1 – 6:1   Depends on surge/dynamic     │
  │  Arborist (static)    10:1        ANSI Z133                    │
  │  Tow lines            5:1         Dynamic consideration        │
  │  Military (SOP)       10:1        Field/life-critical          │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Guide Map

| File | Topic |
|------|-------|
| 01-FIBER-MATERIALS.md | Natural and synthetic fibers — properties table |
| 02-SPINNING-TWISTING.md | S/Z twist, ply, hawser lay, cable lay |
| 03-BRAIDING-PLAITING.md | 8/16-carrier braid, kernmantle, hollow braid |
| 04-ROPE-PROPERTIES.md | Breaking strength, elongation, abrasion, UV, creep |
| 05-KNOTS-SPLICES.md | Ashley taxonomy, eye splice, back splice, whipping |
| 06-HISTORICAL-CORDAGE.md | Egypt, Inca quipu, Viking rigging, sailmaking |
| 07-MARINE-APPLICATIONS.md | Standing/running rigging, mooring, anchor rodes |
| 08-INDUSTRIAL-USE.md | Crane slings, arborist, rescue, mining hoist |
| 09-MODERN-SYNTHETICS.md | UHMWPE, aramid, Vectran, PBO — selection table |

---

## Decision Cheat Sheet

| Situation | Rope Choice |
|-----------|------------|
| Dynamic climbing (fall arrest) | Nylon kernmantle, UIAA-certified dynamic |
| Static rigging, minimal stretch | Polyester double-braid or Dyneema |
| Mooring lines (absorb surge) | Nylon — high elongation by design |
| Life safety rescue | Low-elongation polyester kernmantle, NFPA 1983 compliant |
| Weight-critical application | UHMWPE (Dyneema/Spectra) — highest strength-to-weight |
| High-temperature environment | Aramid (Kevlar/Technora) — stable to 480°C dry |
| Budget light-duty use | Polypropylene — cheap, floats; accept UV degradation |
| Racing yacht standing rigging | Dyneema or Vectran (low creep, low stretch) |

---

## Common Confusion Points

**Rope is a helical structure — never purely axial.** Fibers in a 3-strand twisted rope are at ~20–25° helix angle relative to rope axis. This means the fiber tensile strength cannot be fully realized — the rope's strength is always less than fiber tensile × total fiber cross-section. The braid angle/twist angle × sin/cos geometry determines this efficiency.

**Breaking strength is not working load.** A rope with 10,000 lb MBS has a WLL of 1,000–2,000 lb (10:1 to 5:1 SF). Loads near MBS cause internal fiber damage without visible indication. Never approach MBS in use.

**Knots dramatically reduce strength.** A bowline in a rope reduces breaking strength to ~70% of the straight rope. An eye splice reduces to only ~5% loss (95% efficiency). Splices are always structurally preferred over knots in load-bearing applications.

**Polypropylene floats — that's its main structural property.** PP ropes are used specifically where buoyancy matters (throw lines, water rescue). They have poor UV resistance (degrade in 1–2 seasons outdoors), poor heat resistance, and low strength. Floating is the feature.
