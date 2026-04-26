# Masonry Units: Brick, CMU, Stone, Adobe, Tile

## The Unit Landscape

Every masonry assembly begins with the unit. The unit type determines structural capacity, weathering behavior, thermal mass, and jointing requirements. Units fall into five material families, each with distinct production methods and performance profiles.

```
MASONRY UNIT FAMILIES
=====================

  ┌──────────────────────────────────────────────────────────────────┐
  │                    MASONRY UNITS                                 │
  └──────────────────────────────────────────────────────────────────┘
           │            │            │           │            │
           ▼            ▼            ▼           ▼            ▼
    ┌─────────┐  ┌─────────────┐  ┌────────┐  ┌───────┐  ┌────────┐
    │  BRICK  │  │     CMU     │  │ STONE  │  │ ADOBE │  │  TILE  │
    │(fired   │  │ (concrete   │  │(quarry │  │(earth │  │(terra  │
    │ clay)   │  │  masonry    │  │  or    │  │ +     │  │ cotta/ │
    │         │  │  unit)      │  │ field) │  │ straw)│  │ SCT)   │
    └─────────┘  └─────────────┘  └────────┘  └───────┘  └────────┘
    ASTM C62      ASTM C90        Various      ASTM     ASTM C212
    ASTM C216     ASTM C129       ASTM C568    E2392    ASTM C126
    (building)    (hollow)        (limestone)
    (facing)
```

---

## Brick: Sizes

Brick dimensions are expressed as **actual × nominal**. Nominal = actual + one mortar joint (typically 3/8").

```
STANDARD BRICK SIZES (actual dimensions in inches: W × H × L)
==============================================================

  ┌────────────────────────────────────────────────────────────────┐
  │ Size Name     Actual (W×H×L)      Nominal (W×H×L)  Notes       │
  ├────────────────────────────────────────────────────────────────┤
  │ Modular       3-5/8 × 2-1/4 × 7-5/8   4 × 2-2/3 × 8   Most common US  │
  │ Standard      3-3/4 × 2-1/4 × 8        —            Older buildings    │
  │ Engineer Mod  3-5/8 × 2-13/16 × 7-5/8  4 × 3-1/5 × 8  5 courses = 16" │
  │ Closure Mod   3-5/8 × 3-5/8 × 7-5/8   4 × 4 × 8     Square face       │
  │ Norman        3-5/8 × 2-1/4 × 11-5/8  4 × 2-2/3 × 12  Longer unit     │
  │ Roman         3-5/8 × 1-5/8 × 11-5/8  4 × 2 × 12     Thin, horizontal │
  │ King          2-3/4 × 2-5/8 × 9-5/8   3-1/8 × 3 × 10  Modular courses │
  │ Queen         2-3/4 × 2-3/4 × 7-5/8   3-1/8 × 3-1/8×8  Plinth course  │
  │ Utility       3-5/8 × 3-5/8 × 11-5/8  4 × 4 × 12    CMU-compatible    │
  │ Norwegian     3-5/8 × 2-13/16 × 11-5/8 4 × 3-1/5 × 12  Long engineer  │
  └────────────────────────────────────────────────────────────────┘

  COURSE HEIGHTS (with 3/8" mortar joint):
  ┌──────────────────────────────────────────┐
  │  Modular:   3 courses = 8" (2-2/3" nom)  │
  │  Engineer:  5 courses = 16"              │
  │  Roman:     6 courses = 12"              │
  │  Norman:    3 courses = 8"               │
  └──────────────────────────────────────────┘
```

Why sizes matter: the **modular** system (3 courses = 8") aligns with CMU (8" nominal height), making mixed masonry assemblies dimensionally compatible without cutting.

---

## Brick: ASTM Grades by Weather Exposure

ASTM C216 (facing brick) and C62 (building brick) define three grades based on resistance to freeze-thaw damage:

```
BRICK GRADE SELECTION BY EXPOSURE
==================================

  ┌────────────────────────────────────────────────────────────────────┐
  │ Grade  Full Name           Use                  Saturation Coeff.  │
  ├────────────────────────────────────────────────────────────────────┤
  │  SW    Severe Weathering   Exposed below grade; │  ≤ 0.78          │
  │                            pavement; retaining  │  (low absorption)│
  │                            walls; freezing zones│                   │
  ├────────────────────────────────────────────────────────────────────┤
  │  MW    Moderate Weather-   Vertical above grade │  ≤ 0.88          │
  │        ing                 in most US climates  │                  │
  ├────────────────────────────────────────────────────────────────────┤
  │  NW    Negligible Weather- Interior use only;   │  No limit        │
  │        ing                 very dry climates    │                   │
  └────────────────────────────────────────────────────────────────────┘

  Saturation Coefficient = (24-hr cold water absorption) / (5-hr boil absorption)
  Low coeff → low pore saturation → better freeze-thaw resistance

  ASTM C216 additionally classifies TYPE:
  Type FBS (standard facing) — general use
  Type FBX (select)          — tight tolerances, low variation
  Type FBA (architectural)   — non-uniform, textured for effect
```

| Grade | Min Compressive Strength (avg of 5) | Min Modulus of Rupture |
|-------|-------------------------------------|----------------------|
| SW (C216) | 3,000 psi | 500 psi |
| MW (C216) | 2,500 psi | 350 psi |
| NW (C62)  | 1,500 psi | — |

---

## CMU: Concrete Masonry Units

The standard CMU is **nominally 8" × 8" × 16"** (actual: 7-5/8" × 7-5/8" × 15-5/8"). This aligns with 3-brick modular coursing (8") and standard 16" structural bays.

```
CMU ANATOMY
===========

  PLAN VIEW (top):
  ┌──────────────────────────────────────┐
  │  FACE SHELL     CORE     FACE SHELL  │
  │  ┌────────┐  ┌──────┐  ┌────────┐    │
  │  │        │  │      │  │        │  │
  │  │   1¼"  │  │ open │  │   1¼"  │  │
  │  │        │  │      │  │        │  │
  │  └────────┘  └──────┘  └────────┘  │
  │                                      │
  │  ←────────── 15-5/8" ──────────────→ │
  └──────────────────────────────────────┘

  SECTION VIEW (side):
  ┌──────────────────┐
  │ ┌────────────┐   │  ← face shell 1-1/4" min (hollow units)
  │ │  HOLLOW    │   │  ← webs connect face shells
  │ │  CORE(S)   │   │
  │ └────────────┘   │
  │                  │  7-5/8" actual height
  └──────────────────┘
```

**Hollow percentage**: Standard 2-core CMU is ~46–48% hollow by cross-sectional area. This matters because:
- Net area (after hollow) governs structural calculations
- Grouting fills cores → converts net area to gross area
- Fully grouted CMU approaches solid-unit behavior

### CMU Density Classifications

| Type | Unit Weight | Application |
|------|------------|-------------|
| Normal weight | 125–145 pcf | General structural |
| Medium weight | 105–125 pcf | Reduced dead load |
| Lightweight | 85–105 pcf | Non-structural, insulation value |

Lightweight aggregate: expanded shale, clay, slate (ESLA) or pumice. Lightweight CMU has better thermal resistance but lower compressive strength.

### CMU Types (ASTM C90)

All CMU for structural use is ASTM C90 regardless of weight class:
- **Type I** (moisture-controlled): controlled curing, use where dimensional stability critical
- **Type II** (non-moisture-controlled): standard use (most common in field)

Minimum net area compressive strength: **2,000 psi** (ASTM C90 current edition).

### Grouting CMU

```
GROUT SELECTION (ASTM C476)
============================

  Fine grout:   Cement + sand + water (no coarse aggregate)
                Use when core clear dimension < 2" in one direction
                Slump 8–11" (highly fluid for consolidation)

  Coarse grout: Cement + sand + pea gravel (3/8" max) + water
                Use when core clear dimension ≥ 2" × 3"
                Slump 8–11" required

  GROUTING PATTERN OPTIONS:
  ┌──────────────────────────────────────────────────────────────────┐
  │ Full grouting    → all cores filled (max strength, max weight)   │
  │ Partial grouting → only reinforced cores filled (most common)    │
  │ Solid grouting   → all voids including webs (unusual)            │
  └──────────────────────────────────────────────────────────────────┘

  Low-lift grouting: fill in lifts ≤ 5 ft (consolidate with rod or vibrator)
  High-lift grouting: full wall height pour (cleanouts at base required)
```

---

## Natural Stone: Workability by Rock Type

```
STONE TYPE vs. WORKABILITY
===========================

  IGNEOUS
  ┌────────────────────────────────────────────────────────────────┐
  │ Granite: Silica-rich, crystalline, very hard (Mohs 6–7)        │
  │  Workability: Difficult — requires diamond tooling             │
  │  Use: Dimensional stone, countertops, exterior paving          │
  │  Finish: Polished, honed, flamed (thermal), bush-hammered      │
  │                                                                │
  │ Basalt: Fine-grained, dark, hard; columnar jointing common     │
  │  Use: Paving, aggregate; less common as ashlar                 │
  └────────────────────────────────────────────────────────────────┘

  SEDIMENTARY
  ┌────────────────────────────────────────────────────────────────┐
  │ Limestone: Calcium carbonate, relatively soft (Mohs 3–4)       │
  │  Workability: Good — hand-chisel or saw                        │
  │  Use: Gothic cathedrals, facades, lintels                      │
  │  Caution: Acid-etched by rain, urban pollution                 │
  │                                                                │
  │ Sandstone: Silica grains + cement matrix; hardness varies      │
  │  Workability: Moderate; check bedding orientation              │
  │  Use: Victorian buildings, retaining walls                     │
  │  Caution: Lay on natural bed (not face-bedded) to avoid spall  │
  │                                                                │
  │ Slate: Metamorphosed shale; excellent cleavage plane           │
  │  Use: Roofing, flooring, wall facing                           │
  │  Workability: Splits cleanly along cleavage; drills well       │
  └────────────────────────────────────────────────────────────────┘

  METAMORPHIC
  ┌────────────────────────────────────────────────────────────────┐
  │ Marble: Recrystallized limestone (Mohs 3–4)                    │
  │  Workability: Good — saws easily, accepts high polish          │
  │  Use: Interior cladding, statuary, floors                      │
  │  Caution: Exterior marble hygrothermally warps (thin panels)   │
  │                                                                │
  │ Quartzite: Metamorphosed sandstone; very hard (Mohs 7)         │
  │  Use: Paving, retaining walls; limited dimensional stone use   │
  └────────────────────────────────────────────────────────────────┘
```

**Bedding plane rule**: Sedimentary stone must be laid with its natural bedding plane horizontal ("natural bed"). Face-bedding (bedding plane vertical, running parallel to wall face) exposes lamination to weathering and causes delamination spalling.

---

## Adobe: Soil Mix and Construction

Adobe is sun-dried (not fired) earthen brick. Its structural characteristics depend entirely on soil composition.

```
ADOBE SOIL MIX REQUIREMENTS
=============================

  IDEAL COMPOSITION (by weight):
  ┌──────────────────────────────────────────────────────────────────┐
  │  Clay:    20–30%   (binding agent — holds particles together)    │
  │  Silt:    20–30%   (filler)                                      │
  │  Sand:    40–50%   (aggregate — prevents shrinkage cracking)     │
  │  Organic: 0–5%     (straw, grass — fiber reinforcement)          │
  └──────────────────────────────────────────────────────────────────┘

  ILC RATIO = Inorganic:Lime:Clay (used in stabilized adobe)
  Standard: 75:15:10 by volume when Portland or lime stabilizer added

  ASTM E2392: Standard guide for design and construction of low-rise
  earthen walls (including adobe, rammed earth, compressed earth block)

  TYPICAL ADOBE BLOCK SIZE: 10" × 4" × 14" or 12" × 4" × 18"
  (larger than fired brick — no kiln size constraint)

  STRENGTH:
  Unstabilized: 200–400 psi compressive
  Lime-stabilized: 300–600 psi compressive
  Portland-stabilized: 400–800 psi (ASTM E2392 min: 300 psi)
```

Adobe is load-bearing in low-seismic zones (SDC A/B). Seismic performance is poor unless reinforced with horizontal bond beams and vertical rebar.

---

## Structural Clay Tile

Structural clay tile (ASTM C212) is hollow fired-clay unit used for:
- **Load-bearing tile**: walls, columns (4-8" thick, cells vertical)
- **Partition tile**: non-load-bearing walls (cells horizontal for ease of installation)
- **Fireproofing tile**: encasing steel columns and beams

SCT largely replaced by CMU after 1950, but still specified in historic restoration work.

---

## Absorption and Strength Reference Table

| Unit | Min Compressive Strength | Max Water Absorption | ASTM Standard |
|------|-------------------------|---------------------|---------------|
| Brick, SW grade | 3,000 psi | 17% by weight (5-hr boil) | C216/C62 |
| Brick, MW grade | 2,500 psi | 22% by weight | C216/C62 |
| CMU, normal weight | 2,000 psi (net area) | — | C90 |
| CMU, lightweight | 2,000 psi (net area) | — | C90 |
| Concrete brick | 3,500 psi | — | C55 |
| Limestone (ASTM C568 II) | 4,000 psi | 3% max | C568 |
| Granite (ASTM C615) | 19,000 psi | 0.4% max | C615 |
| Sandstone (ASTM C616 II) | 2,000 psi | 8% max | C616 |
| Marble (ASTM C503) | 7,500 psi | 0.2% max | C503 |

Absorption governs freeze-thaw durability: high-absorption units saturate, water freezes, expansion destroys the face. SW bricks survive because low absorption limits the water available to freeze.

---

## Decision Cheat Sheet

| Situation | Unit Choice |
|-----------|-------------|
| Load-bearing exterior wall, cold climate | SW-grade modular brick or normal-weight CMU |
| Non-structural interior partition | Lightweight CMU (8×8×16) or partition tile |
| Historic restoration — match existing brick | Mock-up test new brick for color, texture, absorption |
| Structural wall, seismic SDC C or higher | CMU, fully grouted reinforced cores |
| Low-cost, vernacular, dry climate | Adobe (ASTM E2392 requirements) |
| Decorative ashlar facade | Limestone or sandstone — check bedding orientation |
| Fire-rated column enclosure | Structural clay tile or CMU fireproofing |
| Pavement, plaza, freeze-thaw exposure | SW brick, laid on bed, not face-bedded |

---

## Common Confusion Points

**Nominal vs. actual size.** A "4-inch" brick is 3-5/8" actual. The 3/8" mortar joint makes up the difference. Always design to nominal; order and detail to actual.

**Hollow percentage and structural calculations.** CMU structural design uses net area (face shell area only) for stress calculations unless fully grouted, in which case gross area applies. A partially grouted wall has intermediate net area — calculate based on grouted cores only.

**Adobe and rammed earth are different.** Adobe = molded and sun-dried blocks, laid in courses. Rammed earth = damp soil compacted in formwork as monolithic construction. Both are earth, but the process and structural behavior differ.

**Stone absorption and durability.** Low absorption in granite does not mean granite needs no maintenance — it means it resists freeze-thaw. Granite spalls in acid rain over centuries. Limestone deteriorates faster in urban pollution but can be cleaned and re-carved. Match stone selection to actual exposure chemistry, not just climate.
