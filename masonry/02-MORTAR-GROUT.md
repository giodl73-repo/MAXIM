# Mortar and Grout: ASTM Types, Mix Design, Compatibility

## The Big Picture

Mortar is the connective matrix between masonry units. It transfers load, accommodates dimensional tolerance, seals against weather, and — critically — must be **softer and weaker than the unit it bonds**. When mortar is too hard, differential thermal movement cracks units instead of joints. The joint is the sacrificial element by design.

```
MORTAR FUNCTION DIAGRAM
=======================

  ┌──────────────────────────────────────────────────────────────────┐
  │                        MASONRY WALL SECTION                      │
  │                                                                  │
  │  [UNIT]  [BED JOINT — horizontal mortar]  [UNIT]               │
  │  [UNIT]  [HEAD JOINT — vertical mortar]   [UNIT]               │
  │                                                                  │
  │  MORTAR FUNCTIONS:                                               │
  │  ① Bond units together (tensile/shear bond strength)             │
  │  ② Transfer compressive loads (gravity path)                     │
  │  ③ Accommodate dimensional variation (3/8" joint tolerance)      │
  │  ④ Seal joints against moisture infiltration                     │
  │  ⑤ SACRIFICIAL ELEMENT — fails before unit face spalls         │
  └──────────────────────────────────────────────────────────────────┘

  MORTAR INGREDIENT TRIANGLE:
             PORTLAND CEMENT
                  △
                 /│\
         Strength/ │ \Durability
               /   │   \
              /    │    \
  LIME ──────┼─────┼─────┼─── SAND
  (plasticity)    (filler +
  (workability)    aggregate)

  Increase Portland → higher strength, lower flexibility
  Increase Lime     → higher flexibility, workability, slower set
  Increase Sand     → lower strength, lower cost, less shrinkage
```

---

## ASTM C270: The Five Mortar Types

ASTM C270 defines mortar by two methods:
- **Proportion specification**: fixed volume ratios of ingredients
- **Property specification**: minimum compressive strength and bond requirements (tested per ASTM C780 field, C109 lab)

```
MORTAR TYPE COMPARISON (ASTM C270)
====================================

  TYPE  STRENGTH  FLEXIBILITY  DURABILITY   PRIMARY USE
  ──────────────────────────────────────────────────────
  M     Highest   Lowest       Highest      Below-grade, retaining walls,
        2,500 psi              (weathering)  pavement, extreme exposure;
                                            use where high compressive
                                            strength required

  S     High      Moderate     High         At/below grade, exterior at
        1,800 psi              (flex bond)   grade, structural (most
                                            reinforced masonry); best
                                            all-around structural mortar

  N     Moderate  High         Moderate     Above-grade exterior, interior
        750 psi               (most         load-bearing, general-purpose
                               workable)     facing brick; most common

  O     Low       Highest      Low          Interior non-load-bearing,
        350 psi               (soft units)  historic restoration matching
                                            old lime-based work; soft brick

  K     Very low  Very high    Very low     Rarely used; historic
        75 psi                              preservation — extremely
                                            soft, friable historic units

  ──────────────────────────────────────────────────────
  Strength: 28-day compressive strength (ASTM C270 property method)
```

**Mnemonic: My Sister Nancy Often Kills** (M, S, N, O, K — decreasing strength order)

---

## Proportion Specifications (ASTM C270 Table)

Mix proportions are by volume (parts). Measured as loose, damp sand.

```
MORTAR PROPORTION TABLE (ASTM C270 Table 1)
============================================

  Type  Portland  Masonry  Hydrated  Sand
        Cement    Cement   Lime      (damp,
                           (Type S)  loose)
  ────────────────────────────────────────────
  M     1         —        ¼         2¾–3¾
  M     ½         1 (Type M)  —      2¾–3¾
  S     1         —        ½–<1¼    2¾–4½
  S     ½         1 (Type S)  —      2¾–4½
  N     1         —        1¼–2½    2¾–9
  N     —         1 (Type N)  —      2¾–3¾
  O     1         —        2½–3½    9+
  O     —         1 (Type O)  —      3–4½
  K     1         —        3½–4½    Not specified

  Notes:
  • Masonry cement = proprietary Portland + plasticizer + air-entrainer blend
  • Portland + lime = traditional "scratch and brown" formula — field adjustable
  • Sand: volume measured by standard loose measurement, not dry weight
  • Air entrainment improves freeze-thaw; masonry cement has ~10–20% air
```

---

## Portland Cement vs. Masonry Cement vs. Lime Putty

```
BINDER COMPARISON
=================

  PORTLAND CEMENT (ASTM C150)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Type I/II: General purpose                                      │
  │  Type III:  High early strength                                  │
  │  Mechanism: Calcium silicate hydration (CSH) — rapid set         │
  │  Set time:  Initial 2–4 hrs, final 6–8 hrs                       │
  │  Strength:  4,000+ psi alone; 2,500 psi in mortar                │
  │  Character: Hard, rigid, low flexibility, good adhesion          │
  └──────────────────────────────────────────────────────────────────┘

  MASONRY CEMENT (ASTM C91)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Pre-blended: Portland + lime (or limestone filler) + plasticizer│
  │              + air-entrainer                                     │
  │  Types: M, S, N (correspond to mortar type when mixed with sand) │
  │  Convenience: One-bag solution — add sand and water only         │
  │  Tradeoff: Lower bond strength than Portland+lime (proprietary   │
  │            plasticizer reduces bond compared to lime putty)      │
  │  Air content: 12–22% by volume (improves workability + FT)       │
  └──────────────────────────────────────────────────────────────────┘

  HYDRATED LIME (ASTM C207)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Type S: Special hydrated lime — fine, high plasticity           │
  │  Type N: Normal hydrated lime — less plastic, drier              │
  │  Chemistry: Ca(OH)₂ (calcium hydroxide)                          │
  │  Set mechanism: Slow carbonation → Ca(OH)₂ + CO₂ → CaCO₃       │
  │  Role in mortar: Workability, plasticity, water retention        │
  │  Sets by: Drying + CO₂ absorption from air (weeks to months)     │
  └──────────────────────────────────────────────────────────────────┘

  LIME PUTTY (non-ASTM, traditional)
  ┌──────────────────────────────────────────────────────────────────┐
  │  Quicklime (CaO) + water → slaked lime putty Ca(OH)₂ paste       │
  │  Aged putty (months to years) develops superior plasticity       │
  │  Historic mortar standard before Portland cement                 │
  │  Natural Hydraulic Lime (NHL): contains silicates → sets         │
  │    partially by hydraulic reaction + carbonation                 │
  │  NHL 2, NHL 3.5, NHL 5 = compressive strength class (MPa)        │
  └──────────────────────────────────────────────────────────────────┘
```

### Type S Lime Chemistry

Quicklime (CaO) from calcining limestone:
```
  CaCO₃ + heat (1650°F) → CaO + CO₂  (calcination)
  CaO + H₂O             → Ca(OH)₂    (slaking — exothermic, violent)
  Ca(OH)₂ + CO₂ (air)  → CaCO₃      (carbonation = hardening in mortar)
```

The carbonation step explains slow mortar gain: CO2 penetrates from the exposed face inward, millimeters per month. Deep joints in thick walls may not fully carbonate for years. Gothic cathedral walls still have incompletely carbonated lime cores in their rubble fill cores.

---

## The Compatibility Rule

The single most important rule in masonry work — especially restoration:

```
COMPATIBILITY HIERARCHY
=======================

  RULE: Each component must be softer than (or equal to) the component it bonds

  Hard             ←──────────────────────────────→  Soft
  ┌────────────┐   ┌────────────┐   ┌────────────┐   ┌────────────┐
  │ GRANITE    │   │ FIRED BRICK│   │ SOFT BRICK │   │  ADOBE     │
  │ 15–35 ksi  │   │ 3–20 ksi   │   │ 1.5–3 ksi  │   │ 0.3–0.6 ksi│
  └────────────┘   └────────────┘   └────────────┘   └────────────┘
        ↓                ↓                ↓                ↓
  Type S or M     Type S or N       Type N or O      Type O or K
  Portland-rich   Portland+lime     High lime         Pure lime
  mortar          mortar            mortar            putty

  IF MORTAR IS TOO HARD:
  • Thermal movement accommodated in UNIT (not joint) → spalling
  • Settlement cracks UNIT not joint → irreversible damage
  • Moisture movement cracks UNIT → masonry deterioration

  IF MORTAR IS TOO SOFT:
  • Mortar weathers rapidly → repointing needed
  • Water infiltration → efflorescence, freeze damage
  • Structural bond inadequate for load

  SWEET SPOT: mortar fails before unit, but not before 30–50 years
```

---

## Repointing: Matching Original Mortar Formulation

When repointing historic masonry, the replacement mortar must match or be softer than the original. Never use Portland-only mortar on pre-1900 brick.

```
REPOINTING MATCHING PROTOCOL
==============================

  Step 1: Sample collection
   ├── Extract hardened mortar sample from inconspicuous joint
   └── Minimum 1/2 oz for petrographic analysis

  Step 2: Petrographic analysis (ASTM C856)
   ├── Identify aggregate type and gradation
   ├── Identify binder type (Portland / lime / natural cement)
   └── Estimate original proportions

  Step 3: Test formulation
   ├── Mix trial batches matching analysis
   ├── Test for compressive strength (not to exceed original unit's)
   └── Test for color and texture match (mock-up panel)

  Step 4: Rake joints (mechanical / hand tools)
   ├── Minimum depth: 3/4" (see 08-REPAIR-RESTORATION.md)
   └── Never use angle grinder on brick — destroys face

  Step 5: Apply in lifts
   ├── Dampen joints before application
   ├── Apply in two passes if joint > 1/2" deep
   └── Strike to match original joint profile
```

---

## Grout: Fine vs. Coarse (ASTM C476)

Grout is a high-slump mixture poured into CMU cores or rubble cavity. Not mortar — different mix design optimized for flowability into small spaces.

```
GROUT SPECIFICATIONS (ASTM C476)
==================================

  PROPERTY        FINE GROUT       COARSE GROUT
  ──────────────────────────────────────────────
  Aggregate max   1/4" (fine sand)  3/8" pea gravel
  Slump required  8–11"             8–11"
  Water/cement    High (by design)  High (by design)
  Use when        Core clear <2"    Core clear ≥2"×3"
                  in any dimension
  Strength min    2,000 psi @28d    2,000 psi @28d

  MIX BY VOLUME (parts):
  Fine:   1 Portland : 2¼–3 fine sand : 0 coarse aggregate
  Coarse: 1 Portland : 2¼–3 fine sand : 1–2 coarse aggregate

  SLUMP EXPLANATION:
  Normal concrete: 3–5" slump (stiff mix)
  Grout: 8–11" slump (liquid-like)
  → Must flow around rebar, consolidate in narrow CMU cores
  → High water/cement ratio → lower strength by w/c law
  → BUT strength is typically adequate (2,000 psi min) because
     grout is confined and not subject to freeze-thaw
```

---

## Mortar Joint Profiles

The shape of the struck joint affects water-shedding and aesthetics:

```
JOINT PROFILE CROSS-SECTIONS
==============================

  TOOLED (weathered) — BEST moisture resistance:
  ┌────────────────────────────────┐
  │  UNIT                          │
  │         \_____/               │ ← concave, water sheds outward
  │  UNIT                          │
  └────────────────────────────────┘

  FLUSH — good resistance:
  ┌────────────────────────────────┐
  │  UNIT                          │
  │  ─────────────────────────    │ ← flat, sealed face
  │  UNIT                          │
  └────────────────────────────────┘

  RAKED — poor moisture resistance (spec for interior only):
  ┌────────────────────────────────┐
  │  UNIT                          │
  │    ┌─────────────────────┐    │ ← shadow line, water pockets
  │  UNIT                          │
  └────────────────────────────────┘

  RODDED (rounded) — good:
  ┌────────────────────────────────┐
  │  UNIT                          │
  │         ╰─────╯               │ ← rounded bead, sheds water
  │  UNIT                          │
  └────────────────────────────────┘

  STRUCK — moderate (overhanging unit edge pockets water on lower face):
  ┌────────────────────────────────┐
  │  UNIT          ←──────────     │
  │   /                            │ ← angled inward at bottom
  │  UNIT                          │
  └────────────────────────────────┘
```

Tooled (concave) joints compress mortar, improving density and bond. Raked joints are purely decorative and should never be used on exterior masonry in wet climates.

---

## Decision Cheat Sheet

| Situation | Mortar Specification |
|-----------|---------------------|
| Below-grade foundation wall, masonry | Type M (highest strength, best water resistance) |
| Exterior above-grade, general facing brick | Type N (best workability + adequate strength) |
| Exterior at grade, reinforced structural | Type S (structural bond + flexibility balance) |
| Interior non-load-bearing partition | Type N or O |
| Pre-1900 historic brick (soft, high absorption) | Type O or lime putty / NHL mortar |
| Repointing historic masonry | Match original — petrographic analysis required |
| Below-grade in freezing climate | Type S or M with air-entrained masonry cement |
| CMU core filling | ASTM C476 fine or coarse grout (not mortar) |
| Pointing thin joints <3/8" | Type N or S with smaller aggregate (pass through joint) |

---

## Common Confusion Points

**Mortar type does not equal Portland content alone.** Type M has the most Portland but that's because lime is low. Type N has more lime and less Portland but is appropriate for most exterior brick applications. Higher Portland ≠ always better.

**Grout ≠ mortar.** Grout goes in cores, not joints. Grout is a high-slump, high-water-content, poured material. Mortar is stiff, workable, troweled. Never substitute one for the other.

**Masonry cement is convenient but trades bond strength.** The plasticizers in masonry cement reduce the bond between mortar and unit compared to Portland+lime formulations. For structural masonry where bond strength is critical, Portland+lime (Type S) outperforms masonry cement Type S.

**Setting vs. curing.** Portland mortars set by hydration — initial set in hours, full cure at 28 days. Lime mortars set by drying then cure by carbonation — months to years for full strength. If you pour Portland grout over lime mortar joints, the Portland's fast alkali can re-activate unreacted lime and cause expansion. This is one reason historic masonry repair sequences matter.

**Water retention is important.** Mortar must retain enough water to allow bond to the porous unit. High-absorption brick draws water out of mortar before it can bond — requires pre-wetting brick or using mortar with added water retention (ASTM C270 water retention requirement: ≥75%).
