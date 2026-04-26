# Rope Properties: Strength, Elongation, Abrasion, UV, Creep

## The Performance Framework

Rope performance is multidimensional. A rope optimized for strength may fail on UV exposure; a rope optimized for shock absorption may creep unacceptably under sustained load. The correct specification requires knowing which properties govern the application.

```
ROPE PERFORMANCE DIMENSIONS
============================

  ┌──────────────────────────────────────────────────────────────────┐
  │  STATIC PROPERTIES              DYNAMIC PROPERTIES               │
  │  ┌──────────────────┐           ┌──────────────────┐             │
  │  │ Breaking strength│           │ Elongation/energy│            │
  │  │ (MBS, ASTM F1623)│           │ absorption (fall │            │
  │  │                  │           │ arrest, mooring) │            │
  │  └──────────────────┘           └──────────────────┘            │
  │                                                                   │
  │  DURABILITY PROPERTIES          HANDLING PROPERTIES             │
  │  ┌──────────────────┐           ┌──────────────────┐            │
  │  │ UV degradation   │           │ Flexibility      │            │
  │  │ Abrasion resistance│         │ Knotability      │            │
  │  │ Chemical resistance│         │ Coilability      │            │
  │  │ Creep (sustained)│           │ Hand (softness)  │            │
  │  └──────────────────┘           └──────────────────┘            │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Breaking Strength and Working Load

```
STRENGTH TERMINOLOGY
====================

  MBS (Minimum Breaking Strength):
  ┌──────────────────────────────────────────────────────────────────┐
  │  The MINIMUM result from a test series — not the average.        │
  │  ASTM F1623 / EN 919 testing: choked eyes or machine grips       │
  │  Test to failure: force at which rope breaks completely          │
  │  MBS is the 5th percentile (or minimum observed) of test results │
  │  Published in catalogs, must be met by every coil                │
  └──────────────────────────────────────────────────────────────────┘

  ABS (Average Breaking Strength): average of test series
  Some standards specify ABS; verify which is being referenced.
  ABS > MBS — using ABS when MBS is required is unconservative.

  WLL (Working Load Limit) = MBS / Safety Factor:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Application              SF         WLL = MBS/SF                │
  │  ─────────────────────────────────────────────────────────────── │
  │  Life safety (NFPA 1983) 10:1        WLL = MBS/10                │
  │  Lifting (ASME B30.9)     5:1–8:1    WLL = MBS/5 to MBS/8        │
  │  Marine (ISO 4565)        5:1–6:1    WLL = MBS/5 or MBS/6        │
  │  Arborist (ANSI Z133)     10:1       WLL = MBS/10                │
  │  Rigging (general)        5:1        WLL = MBS/5                 │
  └──────────────────────────────────────────────────────────────────┘

  SHOCK LOAD:
  ┌──────────────────────────────────────────────────────────────────┐
  │  A sudden jerked load can temporarily exceed WLL by 2–4×.        │
  │  Dynamic application (crane lifts, mooring, vehicle towing):     │
  │  Effective safety factor must account for dynamic factor.        │
  │  Rule of thumb: dynamic loads → apply 2× additional factor.      │
  │                 10:1 SF for life safety covers this.             │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Strength by Material and Construction

```
BREAKING STRENGTH BENCHMARKS (3/8" / 10mm rope, approximately)
=================================================================

  MATERIAL          CONSTRUCTION        MBS (approx)
  ─────────────────────────────────────────────────────────────────
  Manila natural    3-strand             1,350 lb   (6 kN)
  Hemp (tarred)     3-strand             1,200 lb   (5.3 kN)
  Nylon             3-strand             4,500 lb   (20 kN)
  Nylon             double braid         5,000 lb   (22 kN)
  Polyester         double braid         5,600 lb   (25 kN)
  Polypropylene     3-strand             1,900 lb   (8.5 kN)
  UHMWPE (Dyneema)  single braid         14,000 lb  (62 kN)
  Aramid (Kevlar)   braid/core          14,000 lb   (62 kN)
  Vectran           braid                12,000 lb  (53 kN)

  WET STRENGTH FACTOR:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Manila:    80–90% of dry strength                               │
  │  Nylon:     85% of dry strength (moisture plasticization)        │
  │  Polyester: 100% (no water absorption)                           │
  │  UHMWPE:    100% (no water absorption)                           │
  │  Cotton:    100–110% (gains slightly when wet — unusual)         │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Elongation and Energy Absorption

Elongation is the extension at a given load as a percentage of rope length. It is NOT simply the fiber elongation — rope construction geometry and braid/lay angle contribute significantly.

```
ELONGATION CATEGORIES
=====================

  HIGH ELONGATION ROPES (energy-absorbing applications):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Nylon 3-strand/braid: 20–30% at break; 8–12% at 10% MBS         │
  │  Uses: Anchor rodes, mooring lines, climbing rope                │
  │  Physics: Energy = ∫F·dx = area under F-elongation curve         │
  │           Higher elongation → larger area → more energy stored   │
  │  Benefit: Absorbs surge, dock impact, fall energy                │
  └──────────────────────────────────────────────────────────────────┘

  MEDIUM ELONGATION ROPES (balance of use):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Polyester double braid: 10–15% at break; 3–6% at 10% MBS        │
  │  Uses: General marine, sheets, halyards, static rigging          │
  │  Balance: Enough stretch to absorb normal loads; not so much     │
  │           that positioning control is lost                       │
  └──────────────────────────────────────────────────────────────────┘

  LOW ELONGATION ROPES (position-critical applications):
  ┌──────────────────────────────────────────────────────────────────┐
  │  UHMWPE:    3–4% at break; <1% at 10% MBS                        │
  │  Vectran:   3.3% at break; <1% at 10% MBS                        │
  │  Aramid:    3.6% at break; ~1% at 10% MBS                        │
  │  Uses: Racing sails, offshore mooring, precise positioning,      │
  │         structural stays where length control critical           │
  │  Note: Low elongation = poor energy absorption = cannot arrest   │
  │         dynamic falls (Dyneema is NOT suitable for dynamic       │
  │         climbing rope — no energy absorption, breaks anchor)     │
  └──────────────────────────────────────────────────────────────────┘

  ELONGATION TEST (ASTM D4268):
  Measure rope length at minimum tension (0.5–2% MBS as datum)
  Load to 30% MBS, measure elongation
  Report as % change from datum
```

---

## Abrasion Resistance

Abrasion occurs when rope runs over a rough surface under load. It degrades the outer fibers of the sheath, eventually reaching load-bearing core.

```
ABRASION RESISTANCE RANKING (rope-level, approximate)
======================================================

  BEST ABRASION RESISTANCE:
  ┌──────────────────────────────────────────────────────────────────┐
  │  1. Nylon              (excellent — fiber toughness)             │
  │  2. Polyester          (very good — hard fiber, stable)          │
  │  3. UHMWPE             (excellent for dry; reduced in gritty     │
  │                         abrasion — softness cuts on sharp grit)  │
  │  4. Aramid             (moderate — cuts along fiber axis)        │
  │  5. Polypropylene      (moderate)                                │
  │  6. Hemp/Manila        (poor — surface fibers sacrifice readily) │
  └──────────────────────────────────────────────────────────────────┘

  ABRASION TEST (ASTM D3108 or proprietary):
  Rope specimen repeatedly pulled over test bar under tension
  Cycles to failure (or % strength retained after N cycles)

  PRACTICAL ABRASION MANAGEMENT:
  ┌──────────────────────────────────────────────────────────────────┐
  │  • Chafe gear: rubber, leather, or plastic sleeve at chafe point│
  │  • Chafe guard hose: split garden hose over running line         │
  │  • Fairleads: smooth-surfaced rollers or blocks to guide line    │
  │  • Inspection: check sheath regularly; replace when core shows   │
  │  • Running rope is better than static (distributes wear)         │
  └──────────────────────────────────────────────────────────────────┘
```

---

## UV Degradation

```
UV DEGRADATION RATES
====================

  MECHANISM:
  Ultraviolet photons (290–400 nm wavelength) break polymer chains.
  Result: embrittlement, strength loss, color change, surface cracking.

  DEGRADATION RANKING (outdoor UV exposure, uncoated):
  ┌──────────────────────────────────────────────────────────────────┐
  │  MOST RESISTANT:                                                 │
  │  Polyester:    Excellent UV resistance — recommended for         │
  │                permanent outdoor installations                   │
  │                Color fading before strength loss                 │
  │                                                                  │
  │  Nylon:        Good; better than PP; some UV stabilizer helps    │
  │                                                                  │
  │  Manila/Hemp:  Moderate; surface degrades but core protected     │
  │                by compacted construction                         │
  │                                                                  │
  │  UHMWPE:       Moderate; absorbs UV at surface; sheath           │
  │                protection recommended for long-term use          │
  │                                                                  │
  │  Polypropylene:POOR — brittle and weak in 1–2 seasons            │
  │                without UV stabilizer (carbon black additive      │
  │                extends life significantly — black PP is better)  │
  │                                                                  │
  │  Aramid (Kevlar): VERY POOR — must be sheathed for outdoor use   │
  │                   UV destroys fiber within months of exposure    │
  │                                                                  │
  │  PBO (Zylon):  EXTREMELY POOR — must be sheathed at all times    │
  │                6 months of UV exposure causes 40%+ loss          │
  └──────────────────────────────────────────────────────────────────┘

  INSPECTION INDICATORS:
  PP: stiffness, surface cracking, color fading to chalky white
  UHMWPE: color change yellow/brown, reduced elongation before break
  Aramid: surface fiber fuzz, color change, strength testing required
  General: sheath damage, core exposure, glazing over chafe points
```

---

## Creep Under Sustained Load

Creep = gradual extension of rope under constant load over time. Different from elastic elongation (which is recoverable). Creep is non-recoverable — the rope gets longer.

```
CREEP BEHAVIOR BY MATERIAL
===========================

  HIGH CREEP (problematic under sustained load):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Nylon:    Significant creep at loads >10% MBS                   │
  │  UHMWPE:   Creep at room temperature is low; but at >70°C        │
  │            and loads >20% MBS, creep becomes significant         │
  │  Polyester: Moderate creep; less than nylon                      │
  └──────────────────────────────────────────────────────────────────┘

  LOW CREEP (preferred for long-term tensioned applications):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Vectran LCP: Very low creep — designed for sustained tension    │
  │    → preferred for: boat shrouds, seismic moorings, suspensions│
  │  Aramid:     Low creep at ambient (bending fatigue is the issue)│
  │  Polyester:  Moderate (better than nylon, worse than Vectran)    │
  └──────────────────────────────────────────────────────────────────┘

  CREEP TEST: ASTM D6988
  Load rope to fixed % of MBS for fixed time period
  Measure extension at intervals
  Report as % extension per decade of log time

  PRACTICAL CONSEQUENCE:
  Sailing rig: creep in synthetic stays means the rig goes slack
  over days/weeks under sail loads → Vectran shrouds need less
  tensioning adjustment than polyester shrouds.
  Suspension bridges: creep in cables would cause sag — why bridges
  use steel wire rope, not synthetic.
```

---

## Inspection Criteria and Retirement

```
ROPE RETIREMENT CRITERIA
=========================

  GENERAL INSPECTION (before each use):
  ┌──────────────────────────────────────────────────────────────────┐
  │  VISIBLE DAMAGE:                                                 │
  │  • Core visible through sheath (discard immediately)             │
  │  • Cuts, glazing, severe abrasion on sheath (evaluate)           │
  │  • Hard spots or soft spots (internal damage — discard)          │
  │  • Diameter reduction (tension damage, core failure)             │
  │  • Discoloration from chemical exposure (test or discard)        │
  │                                                                  │
  │  LIFE SAFETY ROPE (NFPA 1983 compliant):                         │
  │  Discard after:                                                  │
  │  • Any life-safety load event                                    │
  │  • Visible damage of any type                                    │
  │  • Contamination (chemicals, sharp particles)                    │
  │  • 10 years from manufacture date (NFPA recommendation)          │
  │  • When inspection reveals any doubt                             │
  └──────────────────────────────────────────────────────────────────┘

  WIRE ROPE DISCARD CRITERIA (ASME B30.9):
  ┌──────────────────────────────────────────────────────────────────┐
  │  • 6 randomly distributed broken wires in one rope lay           │
  │  • 3 broken wires in one strand per lay                          │
  │  • 10% diameter reduction from original                          │
  │  • Evidence of kinking, bird-caging, crushing                    │
  │  • Corrosion inside or on exterior                               │
  │  • Evidence of heat damage                                       │
  └──────────────────────────────────────────────────────────────────┘
```

---

## Decision Cheat Sheet

| Required Property | Best Fiber/Construction |
|-------------------|------------------------|
| Maximum breaking strength (weight-limited) | UHMWPE (Dyneema) single braid |
| Maximum elongation (energy absorption) | Nylon 3-strand or double braid |
| Minimum elongation (position control) | UHMWPE, Vectran, or Aramid braid |
| Best UV resistance | Polyester (UV stable, no performance degradation) |
| Best abrasion resistance | Nylon (soft fiber, high toughness) |
| Minimum creep under sustained load | Vectran LCP |
| Best heat resistance | Aramid (Kevlar/Technora) |
| Maximum strength in marine environment | UHMWPE — floats + high strength |
| Life safety compliance (NFPA 1983) | Polyester kernmantle, test-certified |

---

## Common Confusion Points

**MBS is not average breaking strength.** Manufacturers sometimes publish ABS in catalog listings without clearly labeling it. ABS > MBS. Always verify which value is being used before calculating WLL. For life safety, use MBS with 10:1 SF.

**Elongation is not the same as compliance.** A rope can be flexible and compliant in bending without having high elongation under axial load. Hollow braid polyester is flexible in bending (low bending stiffness) but has moderate elongation under tension. Kernmantle UHMWPE is stiff in bending but has low axial elongation.

**UV damage is invisible until testing.** Polypropylene and aramid can lose 50% of their breaking strength with no visible indication on the exterior surface. The only reliable detection is bend testing (if stiff/crackles) or tensile testing. Never trust UV-exposed rope of these materials in life-safety applications beyond their inspection/replacement schedule.

**Creep ≠ stretch under load.** Elastic stretch (instantaneous, recoverable) occurs immediately when load is applied and reverses when load is removed. Creep is permanent, time-dependent elongation under sustained load. A rope that has crept is longer than when new, even with no load applied.
