# Geotechnical Engineering — Landscape

## The Big Picture

Geotechnical engineering is the discipline concerned with the engineering behavior of earth materials. Every structure sits on or in the ground. Before you can design a foundation, a slope, a retaining wall, or an underground excavation, you need to understand what the ground is made of, how it behaves under load, and how it changes over time.

```
+------------------------------------------------------------------+
|               GEOTECHNICAL ENGINEERING — SYSTEM MAP             |
+------------------------------------------------------------------+
|                                                                  |
|  THE LOAD PATH: Structure → Foundation → Soil/Rock              |
|                                                                  |
|  +------------+     +-------------------+     +---------------+ |
|  |  STRUCTURE |     |    FOUNDATION     |     |  GROUND       | |
|  |  (gravity, |     |  (transfers load  |     |  (resists     | |
|  |  wind, EQ  |---->|  to ground via    |---->|  load through | |
|  |  loads)    |     |  shallow or deep  |     |  bearing,     | |
|  +------------+     |  elements)        |     |  friction,    | |
|                      +-------------------+     |  compression) | |
|                                                +---------------+ |
|                                                                  |
|  WHAT GEOTECHNICAL ENGINEERS MUST KNOW:                         |
|  +-----------------------+  +---------------------------------+ |
|  |  SOIL/ROCK            |  |  ANALYSIS                      | |
|  |  CHARACTERIZATION     |  |  Effective stress, seepage,    | |
|  |  Field investigation  |  |  consolidation, shear strength,| |
|  |  Lab testing          |  |  bearing capacity, stability   | |
|  |  Classification       |  |                                 | |
|  +-----------------------+  +---------------------------------+ |
|                                        |                         |
|              +-------------------------+                         |
|              v                                                   |
|  +--------------------------------------------------+           |
|  |  ENGINEERING JUDGMENT                            |           |
|  |  Terzaghi: "soil is nature's most erratic        |           |
|  |  material." Testing gives samples; judgment      |           |
|  |  fills the gaps.                                 |           |
|  +--------------------------------------------------+           |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Terzaghi and the Birth of the Discipline

Karl von Terzaghi (1883–1963) is universally recognized as the founder of soil mechanics. Before Terzaghi, foundations were designed by rule-of-thumb; the theoretical framework that explains why soils behave as they do did not exist.

**Key contributions**:
- **Effective stress principle** (1925): σ' = σ - u. The single most important insight in geotechnical engineering — it is the effective stress, not total stress, that governs soil strength and compressibility.
- **Consolidation theory** (1925): mathematical model of time-dependent settlement of saturated clay under load
- **Bearing capacity theory** (1943): rational formula for the capacity of shallow foundations
- *Erdbaumechanik* (1925): the founding treatise of soil mechanics

Terzaghi also coined the famous warning: "We must not forget that it is nature who has the last word."

---

## The Geotechnical Triangle

The discipline rests on three equally important pillars. Weakness in any one causes failure — literally:

```
+------------------------------------------------------------------+
|               THE GEOTECHNICAL TRIANGLE                          |
|                                                                  |
|                    SOIL CHARACTERIZATION                         |
|                    /\                                            |
|                   /  \                                           |
|                  /    \                                          |
|                 /      \                                         |
|                /        \                                        |
|               /          \                                       |
|              /    Good    \                                       |
|             /  geotechnical\                                      |
|            /   engineering  \                                     |
|           /    requires all  \                                    |
|          /       three        \                                   |
|         /____________________\                                   |
|        ANALYSIS               JUDGMENT                           |
|        (theory &              (experience,                       |
|         computation)          precedent,                         |
|                               uncertainty mgmt)                  |
|                                                                  |
|  Characterization without analysis = empiricism without theory   |
|  Analysis without characterization = precision without accuracy  |
|  Both without judgment = false certainty                         |
|                                                                  |
+------------------------------------------------------------------+
```

---

## The Three-Phase System

Soil is a three-phase material: **solid** (mineral grains), **liquid** (water), and **gas** (air). Understanding how these phases interact is central to all soil mechanics.

```
SOIL ELEMENT — THREE PHASES:

  +----------------+     Volume and Mass relationships:
  |   Air (Va)     |
  |  (gas phase)   |     Void ratio:  e = Vv/Vs   (0.3–3.0 typical)
  +----------------+     Porosity:    n = Vv/V    (0.25–0.75 typical)
  |   Water (Vw)   |     Degree of   S = Vw/Vv   (0 = dry, 1 = saturated)
  |  (liquid phase)|     saturation:
  +----------------+     Unit weight: γ = W/V
  |   Solid (Vs)   |
  | (mineral grains)|    For saturated soil (S=1): γsat = γw(Gs + e)/(1+e)
  +----------------+     where Gs = specific gravity of solids (~2.65-2.72)

  KEY INSIGHT: The void ratio e controls everything —
  compressibility, permeability, shear strength.
  Dense (low e) = stronger, stiffer, less compressible.
  Loose (high e) = weaker, softer, more compressible.
```

---

## Site Investigation — Foundation of Everything

No amount of sophisticated analysis compensates for inadequate site characterization. The ground is non-uniform, anisotropic, and variable in ways that cannot be captured by limited borings.

```
SITE INVESTIGATION SEQUENCE:

  PHASE 1: DESK STUDY
  Existing maps, aerial photos, prior reports, geology maps,
  groundwater records, construction history, LIDAR
      |
      v
  PHASE 2: FIELD INVESTIGATION
  +-------------------+  +------------------+  +----------------+
  |  BORINGS          |  |  IN-SITU TESTS   |  |  GEOPHYSICS    |
  |  Split-spoon      |  |  SPT (N-value)   |  |  Seismic       |
  |  sampling (SPT)   |  |  CPT (cone tip   |  |  refraction    |
  |  Thin-wall        |  |  resistance,     |  |  MASW (shear   |
  |  Shelby tubes     |  |  sleeve friction)|  |  wave velocity)|
  |  (undisturbed     |  |  Vane shear      |  |  ERT (ground-  |
  |  clay)            |  |  (undrained Su)  |  |  water table)  |
  |  Rock cores (NX,  |  |  Pressuremeter   |  |  GPR           |
  |  HX, BX)          |  |  Dilatometer     |  |                |
  +-------------------+  +------------------+  +----------------+
      |
      v
  PHASE 3: LAB TESTING
  Classification tests (Atterberg limits, gradation)
  Consolidation tests (oedometer)
  Shear strength tests (direct shear, triaxial UU/CU/CD)
  Permeability (constant head, falling head)
      |
      v
  PHASE 4: ANALYSIS AND REPORT
```

### Standard Penetration Test (SPT)

The most widely used in-situ test in the world:
- Drop 140-lb hammer 30 inches onto split-spoon sampler
- Count blows for last 12 inches of 18-inch drive = N-value
- N-value correlates with density (sands), consistency (clays), bearing capacity, liquefaction potential
- Energy correction: N60 (corrected to 60% efficiency); overburden correction: (N1)60

### Cone Penetration Test (CPT)

Increasingly preferred for soft soils:
- Continuous electronic log of tip resistance qc and sleeve friction fs
- No sample but continuous stratigraphic profile
- Corrections: qt (pore pressure correction for thin tip); Rf = fs/qc (friction ratio)
- Rf ~ 0.5-1% = clean sand; Rf ~ 4-7% = clay
- CPTu adds pore pressure measurement u2 — resolves fine-grained vs. coarse

---

## Discipline Connections

```
+------------------------------------------------------------------+
|         GEOTECHNICAL ENGINEERING — CONNECTIONS                   |
+------------------------------------------------------------------+
|                                                                  |
|  STRUCTURAL ENGINEERING (structural/)                           |
|  Column loads, wall moments → foundation design loads           |
|  Foundation stiffness → structural frame analysis               |
|  Differential settlement → structural damage assessment         |
|                                                                  |
|  GEOLOGY (geology/)                                              |
|  Rock classification, fault zones, geologic history            |
|  Parent material → soil type and behavior                       |
|  Subsurface mapping: stratigraphy, groundwater                  |
|                                                                  |
|  CONSTRUCTION MATERIALS (construction-materials/)               |
|  Concrete foundations, steel piles, grout materials            |
|  MSE wall geosynthetics                                         |
|                                                                  |
|  HYDRAULICS AND HYDROLOGY (hydrology/)                          |
|  Groundwater table → pore pressures → effective stress          |
|  Seepage → piping → dam and levee safety                        |
|  Drainage design → settlement control                           |
|                                                                  |
|  EARTHQUAKE ENGINEERING                                          |
|  Liquefaction of saturated sands                                |
|  Site amplification (NEHRP site classes)                        |
|  Seismic slope stability (Newmark sliding block)                |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Module Map

```
00-OVERVIEW (this file)
     |
     +-- 01-SOIL-CLASSIFICATION: USCS, Atterberg limits, sieve analysis
     |
     +-- 02-EFFECTIVE-STRESS: Terzaghi principle, pore pressure, seepage, flow nets
     |
     +-- 03-CONSOLIDATION: Primary settlement, Terzaghi 1D theory, time rates, PVDs
     |
     +-- 04-SHEAR-STRENGTH: Mohr-Coulomb, triaxial tests, critical state, residual strength
     |
     +-- 05-SLOPE-STABILITY: Limit equilibrium methods, Bishop, Spencer, seismic stability
     |
     +-- 06-SHALLOW-FOUNDATIONS: Bearing capacity (Terzaghi/Meyerhof), settlement, mats
     |
     +-- 07-DEEP-FOUNDATIONS: Driven piles, drilled shafts, capacity, lateral loads
     |
     +-- 08-RETAINING: Earth pressure theories, wall types, MSE, seismic increment
     |
     +-- 09-GROUND-IMPROVEMENT: Preloading, stone columns, grouting, DSM, liquefaction
```

---

## Decision Cheat Sheet

| You want to understand... | Go to... |
|--------------------------|---------|
| What kind of soil is this? | 01-SOIL-CLASSIFICATION (USCS, Atterberg limits) |
| Why does groundwater matter so much? | 02-EFFECTIVE-STRESS (Terzaghi principle) |
| How long will settlement take? | 03-CONSOLIDATION (Terzaghi 1D, PVDs) |
| Will this slope fail? | 05-SLOPE-STABILITY (Bishop, Spencer) |
| Can this footing support the load? | 06-SHALLOW-FOUNDATIONS (bearing capacity) |
| Why piles instead of footings? | 07-DEEP-FOUNDATIONS (when soils are weak near surface) |
| What holds back a retaining wall? | 08-RETAINING (Rankine/Coulomb active/passive) |
| The site is too soft — now what? | 09-GROUND-IMPROVEMENT (preloading, stone columns) |

---

## Common Confusion Points

**Total stress vs. effective stress**: Total stress (σ) is what you calculate from overburden weight. Pore pressure (u) is the water pressure in the voids. Effective stress (σ' = σ - u) is what actually squeezes the grains together and governs strength. Increasing pore pressure reduces strength — this is how liquefaction occurs.

**Drained vs. undrained**: When load is applied quickly to low-permeability clay, pore water cannot escape. The test must be done undrained (UU or CU triaxial). Over time, pore pressure dissipates and drained strength applies. Choosing wrong: overstimates strength of clay under rapid loading.

**Bearing capacity failure vs. excessive settlement**: A footing fails if it either (a) shears through the soil (bearing capacity failure, F < 1) or (b) settles more than the structure can tolerate (serviceability failure). Settlement usually governs in soft clay; bearing capacity governs in weak fills or very soft clays.

**SPT N-value is not a material property**: N depends on equipment energy, borehole diameter, rod length, and sampler liner. Always use corrected N60 or (N1)60. Raw N values from different contractors cannot be directly compared.
