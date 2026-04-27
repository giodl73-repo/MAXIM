# Masonry — Landscape Overview

## The Big Picture

Masonry is the art and engineering of building with discrete units bonded by mortar (or dry-stacked). The defining structural constraint — units strong in compression, negligible in tension — drives every design decision from arch geometry to buttress placement to reinforcement strategy.

```
MASONRY MATERIAL HIERARCHY
===========================

  UNITS (the solid pieces)
  ┌─────────────────────────────────────────────────────────────────┐
  │  Brick        CMU            Natural Stone      Adobe/Rammed    │
  │  (fired clay) (concrete)     (igneous/sed/meta) (earth)         │
  └─────────────────────────────────────────────────────────────────┘
                    ↓ bonded by ↓
  MORTAR (the connective tissue)
  ┌─────────────────────────────────────────────────────────────────┐
  │  Type M   Type S   Type N   Type O   Historic Lime Putty        │
  │  (strong) (flex)  (general) (soft)   (hydraulic / non-hyd)      │
  └─────────────────────────────────────────────────────────────────┘
                    ↓ arranged in ↓
  BOND PATTERNS (structural + visual organization)
  ┌─────────────────────────────────────────────────────────────────┐
  │  Running   Flemish   English   Stack   Ashlar   Rubble          │
  └─────────────────────────────────────────────────────────────────┘
                    ↓ forming ↓
  ASSEMBLIES (walls, arches, vaults, domes)
  ┌─────────────────────────────────────────────────────────────────┐
  │  Unreinforced    Reinforced (rebar+grout)   Post-tensioned      │
  │  Cavity wall     Veneer     Composite       Single-wythe        │
  └─────────────────────────────────────────────────────────────────┘
                    ↓ governed by ↓
  STRUCTURAL BEHAVIOR
  ┌─────────────────────────────────────────────────────────────────┐
  │  Compressive strength  f'm    (ASTM C1314 prism test)           │
  │  Slenderness ratio     h/t    (empirical limits TMS 402)        │
  │  Thrust lines                 (funicular geometry)              │
  │  Seismic response             (reinforced masonry, SDC D/E/F)   │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Masonry's Central Constraint: Compressive-Only Material

Masonry units are strong in compression (brick: 3,000–20,000 psi), negligible in tension (<100 psi). Mortar joints are the weakest link in tension. This single fact drives the entire history of the discipline.

```
STRESS DIAGRAM: UNREINFORCED MASONRY WALL
==========================================

  AXIAL LOAD (gravity):
    Force P points DOWN at the top of the wall.
    The wall body is in pure compression — masonry handles
    this fine.

  LATERAL LOAD (wind/seismic):
    Force H points HORIZONTAL at the top of the wall.
    The wall bends; the LEEWARD face sees tension.
    TENSION = CRACKING RISK in unreinforced masonry.

  Solution set:
  ① Geometry  — arch/vault redirects tension into compression
  ② Mass      — thick walls keep resultant within middle third (kern)
  ③ Buttress  — redirects thrust to ground at angle
  ④ Rebar     — reinforced masonry: steel takes tension in grouted cores
  ⑤ PT        — post-tensioning pre-compresses, suppresses tension

  KERN CONCEPT (middle-third rule):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Wall section thickness = t                                     │
  │  +---- t/3 ----+---- t/3 ----+---- t/3 ----+                    │
  │                [   KERN   ]                                     │
  │                                                                 │
  │  Resultant force within kern → no tension anywhere in section   │
  │  Resultant force outside kern → tension at one face → cracking  │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Historical Arc

### Phase 1: Mud Brick and Dressed Stone (5000 BCE – 700 BCE)
- Mesopotamian sun-dried adobe: unbaked earth + organic binder
- Egyptian limestone and granite: quarried, dressed, dry-stacked with metal cramps
- Greek isodomic ashlar: equal-height courses, near-zero tolerances, no mortar

### Phase 2: Roman Masonry and Concrete (700 BCE – 400 CE)
- Opus incertum / reticulatum / testaceum: irregular / diamond / brick-faced concrete cores
- Pozzolanic concrete: volcanic ash (pozzolana) + lime + aggregate → hydraulic set (hardens underwater)
- The Pantheon (125 CE): 142-ft unreinforced concrete dome — still standing
- Roman concrete formulations largely lost after empire collapse; not fully reproduced until modern era

### Phase 3: Medieval Masonry and the Gothic Experiment (500–1500 CE)
- Lime mortar: slow carbonation cure — explains multi-decade cathedral construction schedules
- Romanesque: thick walls, small windows, barrel vaults (thrust dispersed over long base)
- Gothic invention: pointed arch (reduces horizontal thrust component) + rib vault (concentrates loads to piers) + flying buttress (carries thrust outside wall plane)
- Gothic is the engineering answer to: "How tall can unreinforced masonry go?"

### Phase 4: Industrial Brick and Portland Cement (1800–1950)
- William Aspdin patents Portland cement (1824): reliable, high-strength, hydraulic
- Machine-made brick replaces hand-molded: uniform size, repeatable quality
- Structural clay tile, hollow CMU: reduce dead load, create air spaces
- Chicago frame (1880s): steel skeleton takes gravity loads, masonry becomes enclosure only

### Phase 5: Reinforced and Post-Tensioned Masonry (1950–present)
- Rebar in CMU grout cores: masonry wall behaves analogously to reinforced concrete
- Empirical design gives way to engineered design (IBC / ASCE 7 / TMS 402)
- Cavity wall construction: drainage plane, air barrier, continuous insulation
- High-seismic SDC D/E/F: special reinforced masonry provisions mandatory

---

## The Masonry Taxonomy

```
MASONRY TYPE MAP
================

  BY UNIT:
    CLAY:     Brick, Structural tile, Terra cotta
    CONCRETE: CMU (block), Precast panel
    STONE:    Ashlar (dressed), Rubble, Dry-stone
    EARTH:    Adobe, Rammed earth

  BY STRUCTURAL SYSTEM:
    UNREINFORCED MASONRY (URM):
      Pre-code buildings; low-seismic zones only;
      empirical h/t limits.
    REINFORCED MASONRY (RM):
      Rebar in grouted cores; steel takes tension;
      all seismic zones permitted.
    POST-TENSIONED (PTM):
      PT tendons in grout cores; high slenderness possible.
    CAVITY WALL:
      Outer wythe + air gap + insulation + inner wythe.

  BY MORTAR JOINT:
    MORTARED:    Standard joints; repointing.
    DRY-STACKED: No mortar; gravity + fit.

  BY HISTORICAL PERIOD:
    Pre-Portland (classical):
      Lime putty mortars; natural hydraulic lime (NHL);
      pozzolanic concrete.
    Portland era (modern):
      Cement mortars Types M/S/N/O;
      reinforced/grouted systems.
```

---

## Material Properties at a Glance

| Material | Compressive Strength | Tensile Strength | Weight (pcf) | Notes |
|----------|---------------------|-----------------|--------------|-------|
| Fired brick, SW grade | 3,000–20,000 psi | <100 psi | 120–130 | Severe weather |
| CMU, normal weight | 1,900–3,000 psi | ~100 psi | 130–145 | Before grouting |
| CMU, lightweight | 1,500–2,500 psi | ~80 psi | 85–105 | Pumice/expanded shale |
| Limestone | 5,000–20,000 psi | 700–2,000 psi | 140–160 | Sedimentary, porous |
| Granite | 15,000–35,000 psi | 2,000–4,000 psi | 160–175 | Igneous, very hard |
| Sandstone | 4,000–15,000 psi | 400–1,000 psi | 130–160 | Varies by silica content |
| Adobe (stabilized) | 300–600 psi | <50 psi | 90–120 | Low strength, earth only |
| Type S mortar | 1,800 psi min | — | — | ASTM C270 |

Key rule: **mortar must be softer than the unit**. Portland-rich mortar on soft historic brick destroys the brick face during thermal cycling — the joint must fail first, not the face. This is the cardinal compatibility rule of masonry.

---

## Structural Logic: The Funicular Polygon

The thrust line (line of pressure) inside a masonry arch must stay within the arch thickness. If it exits the arch boundary, a hinge forms; three hinges = mechanism = collapse. Robert Hooke stated the principle (1675): "as hangs the flexible line, so but inverted stands the rigid arch."

```
ARCH THRUST LINE
================

  FLEXIBLE CHAIN (hanging under gravity)     INVERTED = IDEAL ARCH SHAPE
  ┌──────────────────────────────────┐       ┌──────────────────────────────────┐
  │                                  │       │   ╭─────────────────────────╮    │
  │  A ──────────────────────── B    │  →   │  A                           B  │
  │       ╰──────────────────╯       │       │       ╭──────────────────╯       │
  │   (catenary under uniform load)  │       │   (inverted catenary = arch)     │
  └──────────────────────────────────┘       └──────────────────────────────────┘

  Chain: PURE TENSION throughout              Arch: PURE COMPRESSION throughout
  (unique shape where no bending occurs)      (thrust line = chain shape inverted)

  Real-world complication: loads non-uniform → thrust line migrates
  Design rule: keep thrust line within MIDDLE THIRD of arch thickness at all sections
  Three hinges = collapse mechanism (statically determinate critical state)
```

---

## Guide Map

| File | Topic |
|------|-------|
| 01-MASONRY-UNITS.md | Brick sizes/grades, CMU, stone, adobe, tile |
| 02-MORTAR-GROUT.md | ASTM types, mix design, compatibility |
| 03-BRICKLAYING.md | Bond patterns, leads, corners, methodology |
| 04-STONEWORK.md | Ashlar, rubble, dry-stone, quarrying |
| 05-STRUCTURAL-MASONRY.md | Load paths, slenderness, reinforced masonry, codes |
| 06-ARCHES-VAULTS.md | Thrust line, voussoirs, vault types, Gothic structure |
| 07-HISTORIC-MASONRY.md | Roman concrete, medieval lime, Islamic geometry |
| 08-REPAIR-RESTORATION.md | Repointing, crack diagnosis, compatibility, cleaning |
| 09-MODERN-APPLICATIONS.md | Cavity wall, thin brick, insulated CMU, seismic |

---

## Decision Cheat Sheet

| Situation | Masonry Solution |
|-----------|-----------------|
| High compressive load, simple geometry | Standard brick or CMU, running bond |
| Seismic zone SDC D or higher | Special reinforced CMU with grouted rebar cores |
| Historic building repair mortar | Lime-based mortar matching original; never Portland-only |
| Spanning opening without steel lintel | Arch — soldier course or full voussoir construction |
| Insulated wall, single wythe | Insulated CMU or cavity wall with batt + air gap |
| Below-grade or severe wet exposure | Type S or M mortar, SW-grade brick |
| Aesthetic stone facade, non-structural | Adhered thin-stone or thin-brick veneer system |
| Large span roof over masonry walls | Barrel vault or groin vault — geometry eliminates tension |

---

## Common Confusion Points

**"All mortar is mortar" — False.** Type M (high Portland) used on soft historic brick will cause spalling within one freeze-thaw cycle. Mortar hardness must match unit hardness. The joint is the sacrificial element, not the unit face.

**"Brick is structural everywhere" — Not since ~1890.** Modern brick is almost always a 4-inch veneer on a steel or concrete frame. The frame takes gravity loads; the brick is enclosure. True load-bearing brick is rare in post-1920 construction.

**"Dry-stone is primitive masonry" — Not structurally.** A well-built dry-stone wall with proper batter, through-stones, and coping can outlast a poorly mortared modern wall. Traditional Scottish drystane dykes from the 1700s still stand.

**"Portland cement is always better" — False for historic work.** Portland-based mortars are far stronger and less flexible than lime mortars. On old buildings with natural settlement movement, a stiff Portland mortar cracks the units rather than the joint. The joint must give first.

**"Gothic cathedrals were slow because of lime curing" — Partly true.** Lime mortar carbonation (CO2 absorption from air) takes years for full strength gain. But multi-decade cathedral timelines also reflect medieval finance, labor availability, and political disruptions, not mortar chemistry alone.
