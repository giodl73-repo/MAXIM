# Economic Geology — Ore Deposits, Petroleum Systems, Critical Minerals

**Bridge — ore concentration factor as signal-to-noise ratio:** Economic geology is fundamentally about enrichment ratios. Gold averages 4 ppb in continental crust; an economic deposit runs 1–10 g/t (ppm), representing 250,000–2,500,000× enrichment above background. This is identical to extracting actionable signal from noisy data — the geological processes that form ore deposits are the physical-chemical filters that amplify signal (target metal) while rejecting noise (gangue). Hydrothermal fluid flow is a natural column chromatograph: different metals precipitate at different temperatures and chemical conditions, separating them from the bulk rock matrix. Placer deposits are gravity-sorted arrays: specific gravity differences act as a filter, concentrating dense metals (Au SG=19.3, Cassiterite SG=7.0) while washing away silicate gangue (SG≈2.6). Cutoff grade is the signal threshold: below it, the cost of extraction exceeds the value of signal recovered. Changing metal price shifts the threshold, reclassifying "noise" as "signal" — exactly like adjusting a classifier's decision boundary.

## The Big Picture

Economic geology connects geologic processes to resource extraction. The core concept: **concentration**. Iron is 5% of the crust; economically minable iron ore requires 50%+ concentration (10× enrichment). Gold is 4 ppb in crust; a mineable deposit might be 1–10 ppm (250–2500× enrichment). Every deposit type reflects specific geologic processes that concentrated material.

```
+---------------------------------------------------------------+
|              ECONOMIC GEOLOGY FRAMEWORK                       |
|                                                               |
|  GEOLOGIC PROCESS → CONCENTRATION MECHANISM → DEPOSIT TYPE    |
|                                                               |
|  Magmatic differentiation   → Magmatic deposits               |
|  Hydrothermal fluid flow    → Hydrothermal veins, porphyry    |
|  Weathering + residual      → Laterite, bauxite, placer       |
|  Sedimentation              → Banded iron, phosphorite, coal  |
|  Diagenesis + burial        → Petroleum, coal                 |
|  Evaporation                → Evaporites (K, NaCl, gypsum)    |
|  Metamorphism               → Some Au, graphite               |
+---------------------------------------------------------------+
```

---

## Ore Deposit Classification

### Magmatic Deposits — Crystallization from Magma

```
DEPOSIT TYPE         METAL/MINERAL     FORMATION              EXAMPLE
-------------------  ----------------  ---------------------  ------------------
Chromite layers      Cr                Crystal settling in    Bushveld Complex,
(stratiform)                           mafic/ultramafic       South Africa
                                        layered intrusion      (world's largest)

PGE reefs            Pt, Pd, Rh, Ru    Crystal settling or   Merensky Reef
(platinum group)                        magma mixing          (80% world PGE)

Ni-Cu-PGE sulfide    Ni, Cu, Co, PGE   Sulfide liquid        Sudbury, Norilsk,
                                        immiscibility +        Kambalda
                                        settling

Kimberlite pipes     Diamonds (C)      Deep mantle xenolith  Kimberley, S. Africa
                                        host (not magmatic    (also indicator:
                                         concentration)        olivine, pyrope
                                                               garnet)

Carbonatite          REE, Nb, P, Ti    Carbonate-rich        Mountain Pass
                                        magma (unusual)        (California REE)
```

### Hydrothermal Deposits — Hot Fluid Circulation

Most of the world's metals come from hydrothermal deposits — hot, saline, metal-bearing fluids depositing minerals as they cool or encounter reactive rocks:

```
FLUID SOURCE:  Magmatic (derived from crystallizing magma)
               Meteoric (rainwater circulated through hot rock)
               Metamorphic (fluids driven off during metamorphism)
               Marine (seawater circulating at mid-ocean ridges)

FLUID PATH:    Faults, fractures, permeable beds, contact zones

PRECIPITATION: Cooling + pressure drop
               pH change (acid fluid enters carbonate = neutralization)
               Chemical reduction (sulfide precipitation)
               Boiling (CO₂ loss → pH rise)
```

| Deposit Type | Metals | Setting | Example |
|-------------|--------|---------|---------|
| **Porphyry Cu-Mo** | Cu, Mo (+Au, Ag) | Arc subduction; large granitic intrusion + surrounding fractured rock | Bingham Canyon (Utah), Escondida (Chile) |
| **Epithermal** | Au, Ag, Cu | Shallow (0–2 km), low T; volcanic systems | Hishikari (Japan), Yanacocha (Peru) |
| **VHMS (Volcanogenic Massive Sulfide)** | Cu, Zn, Pb, Au, Ag | Seafloor hydrothermal; ancient ocean floor | Kidd Creek (Canada), Flin Flon |
| **Skarn** | Fe, Cu, Pb, Zn, W, Mo | Contact zone between intrusion + carbonate | Many in CRD (carbonate-replacement) |
| **Orogenic Au** | Au (+ Sb, W, As) | Metamorphic belts, quartz veins | Kalgoorlie (Australia), Mother Lode (CA) |
| **Mississippi Valley Type (MVT)** | Pb, Zn | Carbonate-hosted; brines in sedimentary basins | Tri-State (OK-KS-MO), Pine Point |

```
HYDROTHERMAL SYSTEM — FLUID FLOW ARCHITECTURE

  HEAT SOURCE          FLUID SOURCE          FLUID PATH
  (magmatic           (magmatic water,      (faults, fractures,
   intrusion, or       meteoric water,       permeable beds,
   radiogenic heat)    seawater, brines)     contact zones)
        |                    |                    |
        v                    v                    v
  +---------------------------------------------+
  |  HOT FLUID (150–500°C)                      |
  |  Metal-bearing, saline, acidic              |
  |  Migrates upward along pressure gradient    |
  +---------------------------------------------+
        |
        v (cooling + chemical change → precipitation)
  +-------------------------------------------------+
  | DEPOSITION ZONE:                                |
  | Temperature drop → sulfide/oxide precipitation  |
  |   (porphyry: stockwork veins in fractured rock) |
  |   (epithermal: boiling zone, 50–300m depth)     |
  |   (VHMS: cold seawater mixing at seafloor vent) |
  |   (MVT: brine mixing in carbonate, low T)       |
  +-------------------------------------------------+
        |
        v
  ALTERATION HALO (diagnostic zonation):
  Potassic (K-feldspar, biotite) → Phyllic (sericite) →
  Argillic (kaolinite, illite) → Propylitic (chlorite, epidote)
  Zoning maps distance from fluid conduit
```

### Sedimentary and Weathering Deposits

```
DEPOSIT TYPE     METAL       PROCESS                   EXAMPLE
---------------  ----------  ------------------------  ------------------
Banded Iron      Fe          Chemical precipitation    Hamersley Basin
Formation (BIF)              in Proterozoic oceans     (Australia), Brazil
                             (before O₂ oxygenated
                              oceans; 2.5–1.8 Ga)

Laterite/Bauxite Al, Ni      Tropical weathering       Guinea, Jamaica (Al)
                             removes Si, Ca, Mg;        New Caledonia (Ni)
                             residual Al/Fe/Ni
                             concentrated

Placer deposits  Au, Sn, Ti, Stream/beach sorting by   Klondike (Au),
                 Zr          specific gravity           Kerala (Ti, Zr)

Red bed Cu       Cu, Ag      Oxidizing fluids in red   Kupferschiefer
                             sandstones precipitate     (European)
                             sulfides at redox
                             boundaries

Phosphorite      P           Marine upwelling zones;   Moroccan deposits
                             biogenic concentration     (world's largest)
```

---

## Petroleum Systems

A petroleum system requires all five elements to exist simultaneously:

```
+----------------------------------------------------------------+
|                    PETROLEUM SYSTEM                             |
|                                                                 |
|  SOURCE ROCK      Organic-rich shale buried to "oil window"    |
|  (kitchen)        Ro 0.6–1.3% = oil; 1.3–3.0% = wet gas;     |
|                   >3% = dry gas (overmature)                   |
|                                                                 |
|  MIGRATION        Primary: micro-scale to carrier bed          |
|                   Secondary: updip through permeable bed       |
|                   Expulsion when pore pressure builds          |
|                                                                 |
|  RESERVOIR        Porous + permeable rock                      |
|                   Sandstone (intergranular porosity)           |
|                   Carbonate (vuggy, fracture, intercrystalline)|
|                   Key metrics: φ (porosity 10–35%)             |
|                                k (permeability 1–1000 mD)      |
|                                                                 |
|  TRAP             Where oil/gas accumulates                    |
|                   Structural: anticline, dome, fault           |
|                   Stratigraphic: pinch-out, unconformity       |
|                   Combination                                   |
|                                                                 |
|  SEAL             Cap rock preventing escape                   |
|                   Shale, evaporite (best: halite is plastic)   |
|                   Must be present before/during charge         |
+----------------------------------------------------------------+
```

**Oil window depths** (~2–5 km depending on geothermal gradient):
- Above 2 km: immature (preserved organic matter, no oil)
- 2–4 km: oil window (~60–120°C)
- 4–5 km: wet gas zone (~120–150°C)
- Below 5 km: dry gas only (methane only, thermally cracked)

**Unconventional hydrocarbons:**
- **Tight oil/gas** — same source/seal but reservoir has very low permeability (shale, tight sand); requires hydraulic fracturing (fracking)
- **Shale gas** — source rock IS the reservoir (gas stays in source)
- **Oil sands (tar sands)** — heavy oil + sand (Alberta); biodegraded conventional oil
- **Gas hydrates** — methane clathrates in sediment; enormous resource, no commercial production yet

---

## Coal Rank and Characteristics

```
COAL RANK    CARBON %   CALORIFIC    VOLATILES   EXAMPLE USE
-----------  ---------  ----------   ----------  -----------------
Peat         <60%       Low          High        Fuel (Ireland,
             (wet)      (~8 MJ/kg)               Scandinavia)
Lignite      ~60–70%    Low          Very high   Power stations
(brown coal) (soft)     (~15 MJ/kg)              (Germany)
Sub-         ~70–77%    Medium       High        Power stations
bituminous
Bituminous   ~77–89%    High         Medium      Power, steel
(soft coal)             (~30 MJ/kg)              (thermal + coking)
Anthracite   89–98%     High         Very low    Heating, some
(hard coal)  (hard,     (~35 MJ/kg)              industrial
             shiny)
```

**Coking coal vs thermal coal** — Coking (metallurgical) coal is bituminous rank coal that softens and fuses when heated, allowing coke production for steel. Thermal coal is used for power generation. Both are bituminous but different sub-ranks.

---

## Critical Minerals — The 21st Century Battlefield

"Critical" = economically important + supply chain risk (few producers, geopolitically concentrated):

```
MINERAL/METAL   KEY USE                  TOP PRODUCERS      CONCENTRATION
--------------  -----------------------  -----------------  ---------------
Lithium (Li)    EV batteries (cathode    Chile, Australia,  ~85% in 3 countries
                + electrolyte)           Argentina
                                         ("Lithium Triangle")

Cobalt (Co)     Li-ion cathodes (NMC)    DRC (~70%)         Supply chain risk
                                                            (artisanal mining)

Nickel (Ni)     NMC batteries,           Indonesia (class   High-grade
                stainless steel          1 nickel), Russia  sulfide depleting;
                                                            laterite growing

Rare Earth      Nd-Fe-B magnets          China (60%+
Elements (REE)  (EV motors, wind         production,        Extreme
                turbines, electronics)   ~80% processing)   concentration

Graphite        Li-ion anodes            China (>80%)       Near-monopoly

Copper (Cu)     Electrification          Chile, Peru,       Well-distributed
                (EVs, renewables,        DRC                but demand rising
                grid)                                       fast

Platinum Group  Catalytic converters     South Africa       Bushveld Complex
(PGE)           (Pt, Pd), H₂ fuel cells  (70%+), Russia     dominates

Gallium,        Semiconductors,          China (90%+        Strategic export
Germanium       solar cells, military    each)              controls (2023)
                electronics
```

---

## Ore Grade and Cutoff Concepts

```
METAL     CRUSTAL AVERAGE   MINEABLE GRADE   ENRICHMENT FACTOR
--------  ----------------  ---------------  -----------------
Iron (Fe) 5.6%              >25–30%          ~5×
Al        8.2%              >25% (bauxite)   ~3×
Cu        55 ppm            0.3–1%           ~50–100×
Ni        80 ppm            0.3–1%           ~30–100×
Pb        13 ppm            1–2%             ~1000×
Zn        70 ppm            2–5%             ~300–700×
Au        4 ppb             1–5 g/t           250,000–1,250,000×
Pt        10 ppb            2–5 g/t           200,000–500,000×
```

**Cutoff grade** — the grade below which ore is uneconomic to process. Changes with metal price, processing cost, and ore geometry. A deposit at one metal price can become sub-economic at another price, instantly reclassifying "reserves" to "resources."

---

## Decision Cheat Sheet

| Deposit type encountered | Look for |
|--------------------------|---------|
| Porphyry Cu | Large intrusive; disseminated sulfides; stockwork veins; argillic alteration halo |
| Epithermal Au | Shallow volcanic setting; silicified veins; adularia; low-sulfidation or high-sulfidation alteration |
| BIF iron ore | Precambrian; alternating chert + magnetite/hematite bands; high-grade if supergene enriched |
| Laterite (bauxite/Ni) | Tropical humid climate; residual concentration; red/yellow clay profile |
| Coal | Sedimentary basin; carbonaceous strata; Carboniferous or Permian age typical |
| Petroleum | Sedimentary basin; identify source + trap + seal + migration path |

---

## Common Confusion Points

**Resources vs reserves** — JORC/NI-43-101 terminology: Mineral "resources" are estimated tonnage/grade; mineral "reserves" are the economically extractable subset (after applying cutoff grades, mining costs, engineering). Reserves ≤ Resources always. This distinction is legally significant and media often conflates them.

**REE ≠ rare** — Rare Earth Elements are not particularly rare in the crust; cerium is more abundant than copper. They are "rare" because economically minable concentrations are uncommon. The real challenge is that REE processing generates radioactive thorium waste (associated in monazite), making new mines politically difficult outside China.

**Porphyry copper ≠ copper-colored porphyry rock** — "Porphyry" here refers to the porphyritic texture of the associated intrusive rocks, not to copper's color. Porphyry Cu deposits are the world's most important copper source (~75% of production).

**Oil trap vs reservoir** — A trap is the geometric structure that holds oil; the reservoir is the porous rock within that trap. Anticlines are traps only if a seal cap rock exists on top. Without the seal, oil migrates through.
