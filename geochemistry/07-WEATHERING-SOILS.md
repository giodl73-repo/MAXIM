# Weathering, Soils, and Regolith

## The Big Picture

Weathering is the chemical and physical breakdown of rocks at or near the Earth's surface. It is the first step in the geochemical cycle — releasing elements from minerals into solution, creating soil, and driving the long-term carbon cycle (silicate weathering = planetary thermostat).

```
+------------------------------------------------------------------+
|                    WEATHERING SYSTEM                              |
+------------------------------------------------------------------+
|                                                                  |
|  PHYSICAL WEATHERING          CHEMICAL WEATHERING                |
|  -----------------            -------------------                |
|  Frost cracking               Dissolution                        |
|  Salt crystal growth          Hydrolysis                         |
|  Thermal expansion            Oxidation                          |
|  Root wedging                 Hydration                          |
|  Abrasion/comminution         Carbonation                        |
|                                                                  |
|  Effect: surface area ↑       Effect: mineral composition →      |
|  (enhances chemical           secondary minerals + dissolved     |
|  weathering)                  ions (solutes)                     |
|                                                                  |
|  WEATHERING → REGOLITH → SOIL (with biology) → SEDIMENT          |
|                                                                  |
|  KEY OUTPUT: Clay minerals + solutes (cations, silica, CO₂ draw) |
+------------------------------------------------------------------+
```

---

## Chemical Weathering Reactions

### Primary Mineral Weathering

```
KEY WEATHERING REACTIONS
=========================

  CARBONATION OF SILICATES (CO₂ drawdown):
    Feldspar hydrolysis:
    2KAlSi₃O₈ + 2H₂CO₃ + 9H₂O →
    Al₂Si₂O₅(OH)₄ + 4H₄SiO₄ + 2K⁺ + 2HCO₃⁻
    K-feldspar → kaolinite + silica (aq) + K⁺ + bicarbonate

    → CO₂ consumed; K⁺ enters rivers; kaolinite accumulates in soil

  OLIVINE WEATHERING:
    Mg₂SiO₄ + 4H₂CO₃ → 2Mg²⁺ + H₄SiO₄ + 4HCO₃⁻
    (Forsterite + carbonic acid → Mg²⁺ + silica + bicarbonate)
    Fast weathering rate: ~10× faster than feldspar
    → Target for CDR (carbon dioxide removal) proposals (rock powdering)

  PYRITE OXIDATION (ACID PRODUCTION):
    2FeS₂ + 7O₂ + 2H₂O → 2Fe²⁺ + 4SO₄²⁻ + 4H⁺
    FeS₂ (pyrite) + O₂ + H₂O → sulfuric acid + iron oxides
    → Acid mine drainage (AMD); dissolves carbonate rocks
    → Net: atmospheric O₂ consumed; acid produced

  CARBONATE DISSOLUTION (fast, reversible):
    CaCO₃ + CO₂ + H₂O → Ca²⁺ + 2HCO₃⁻
    Karst formation: dissolution of limestone
    Fast (days-years); no net CO₂ drawdown (CO₂ released when calcite recrystallizes)
    THIS IS NOT THE SAME AS SILICATE WEATHERING

  SERPENTINIZATION:
    Mg₂SiO₄ (olivine) + H₂O → Mg₃Si₂O₅(OH)₄ (serpentine) + Fe₃O₄ + H₂
    Produces H₂ (potential energy source for chemolithotrophs)
    Ultramafic rocks (peridotite) + water → serpentine + magnetite + H₂
    Warm springs above serpentinite: high pH (9-11), H₂-rich
    Relevant: Mars (geothermal + olivine-rich crust)
              Europa, Enceladus (seafloor water-rock interaction)
```

---

<!-- @editor[bridge/P2]: The Bowen reaction series (high-T minerals weather fastest) is the inverse of the crystallization sequence — framing this explicitly as a thermodynamic stability argument (minerals far from their equilibrium conditions decompose fastest) would connect to the learner's physics intuition -->
## Weathering Rates and Controls

```
CONTROLS ON WEATHERING RATE
=============================

  MINERAL REACTIVITY (intrinsic):
  Fast to slow weathering:
    Olivine >> Pyroxene >> Ca-plagioclase >> Amphibole >>
    Na-plagioclase >> K-feldspar >> Muscovite >> Quartz

    Rule of thumb: Mineral formed at highest T/P weathers fastest
    (crystallization stability order reverses weathering order)

  EXTERNAL CONTROLS:
    TEMPERATURE: Arrhenius equation; rate ∝ e^(-Ea/RT)
      ~2-3× rate increase per 10°C increase
    RAINFALL/RUNOFF: carries products away; prevents saturation
    SURFACE AREA: physical comminution increases surface → faster
    pH: acidic pH increases dissolution rate for silicates
        (H⁺ attacks Si-O-Al bonds)
    BIOLOGICAL ACTIVITY: mycorrhizal fungi accelerate feldspar
                          weathering by organic acid production
                          (~3-10× acceleration)

  KINETIC vs THERMODYNAMIC CONTROL:
    Transport-limited: weathering outpaces removal (warm, humid, flat)
      → thick chemically mature soil; depleted in mobile elements
      → end product: kaolinite, gibbsite, iron oxides
    Reaction-limited: removal outpaces weathering (cold, steep, arid)
      → thin, chemically immature soil; primary minerals present
      → mixed minerals; Ca, Na, K, Mg retained

  WEATHERING PROXY (CIA: Chemical Index of Alteration):
    CIA = Al₂O₃/(Al₂O₃ + CaO* + Na₂O + K₂O) × 100
    (CaO* = silicate-bound CaO, excluding carbonate)
    Fresh granite: CIA ≈ 50
    Kaolinite:     CIA ≈ 100
    Bauxite:       CIA ≈ 100+
    High CIA = intense weathering (tropical); Low CIA = cold/arid
```

---

## Clay Minerals: Products of Weathering

```
CLAY MINERAL SYSTEMATICS
==========================

  Clay minerals: phyllosilicates (<2 μm); formed from weathering of primary silicates

  STRUCTURE:
    T = tetrahedral sheet: Si-O₄ tetrahedra linked in sheet
    O = octahedral sheet: Al/Mg/Fe in octahedral coordination
    Layer types: 1:1 (T:O) or 2:1 (T:O:T)

  MAJOR CLAY GROUPS:
    KAOLINITE (1:1):
      Al₂Si₂O₅(OH)₄
      Forms in strongly acidic, highly leached soils (tropical)
      Low CEC (cation exchange capacity): ~3-15 meq/100g
      No swelling; stable; "end product" of intense weathering
      Economic: ceramics, paper coating, pharmaceuticals

    ILLITE (2:1, non-swelling):
      K(Al,Fe,Mg)₂(Al,Si)₄O₁₀(OH)₂
      Common in temperate soils; altered from K-feldspar
      Intermediate CEC: 10-40 meq/100g
      "Diagenetic" illitization: smectite → illite during burial

    SMECTITE/MONTMORILLONITE (2:1, swelling):
      Variable Mg, Al, Fe in octahedral sites
      Highly swelling: absorbs water; 2× volume change
      High CEC: 80-150 meq/100g (important for soil fertility)
      Forms in alkaline, poorly-drained, temperate to subtropical soils
      Problem: expansive soils → building foundation damage

    CHLORITE (2:1:1):
      Brucite layer interlayer
      Forms in low-T metamorphism and hydrothermal alteration
      Non-swelling; low CEC

    VERMICULITE (2:1 with expanded interlayer):
      High CEC: 100-150 meq/100g
      Forms from biotite weathering
      Expanded by heating: horticultural uses

  KAOLIN → GIBBSITE → BOEHMITE (aluminum hydroxides):
    End products of extreme weathering in tropical laterites
    Al(OH)₃ (gibbsite): all Si leached out; only Al remains
    Bauxite = gibbsite + boehmite + diaspore — aluminum ore
```

---

## Soil Profiles (Pedology)

```
SOIL HORIZON SEQUENCE
======================

  SURFACE
  |  O HORIZON: Organic material; litter, humus
  |             pH often acidic (organic acids); high microbial activity
  |
  |  A HORIZON: Topsoil; mixed mineral + organic
  |             Leaching: water moves downward, carrying solutes
  |             Color: dark (organic matter + humus)
  |             Root zone; high biological activity
  |
  |  E HORIZON: Eluviation (leaching) zone
  |             Light color; pale gray/white (depleted in Fe, Al, clay)
  |             Podzolization: Fe, Al complexed by organic acids and leached down
  |
  |  B HORIZON: Illuviation (accumulation) zone
  |             Fe, Al oxides accumulate (Bs = spodic horizon)
  |             Clay accumulates (Bt = argillic horizon)
  |             CaCO₃ accumulates in arid soils (Bk = calcic horizon)
  |             Color: red/brown (Fe oxides)
  |
  |  C HORIZON: Weathered parent material; saprolite
  |             Partially weathered rock; structure of original rock visible
  |
  BEDROCK (R)

  DEPTH: Varies from cm (polar) to >30 m (tropical laterites)
  TIME: Full soil profile: 10⁴ to 10⁶ yr depending on climate/parent material
```

### Soil Orders (USDA)

```
USDA SOIL TAXONOMY (12 ORDERS)
================================

  ORDER         KEY CHARACTERISTIC          CLIMATE/LOCATION
  -----         -----------------           ----------------
  Entisol       No development (fresh)      Beaches, flood plains, slopes
  Inceptisol    Minimal development         Young soils; cool/glaciated
  Aridisol      Dry; salt/carbonate accum.  Deserts; B horizon accumulation
  Vertisol      Shrink-swell clays          Semiarid; high smectite
  Mollisol      Thick dark A; base-rich     Grasslands (Great Plains, Ukraine)
                "chernozem" = rich ag soil
  Alfisol       Argillic B; mod. leached    Temperate deciduous forest
  Ultisol       Strongly leached; kaolinite Subtropical humid forest
  Oxisol        Extreme weathering; Fe/Al   Tropical; laterite; low fertility
                oxides; bauxite
  Spodosol      Podzol; E + Bs horizon      Boreal forest; coarse parent material
  Histosol      Organic (peat, bog)         Wetlands; permafrost
  Gelisol       Permafrost within 2 m       Arctic/subarctic
  Andisol       Volcanic ash parent         Volcanically active regions

  GEOCHEMICAL SIGNIFICANCE:
  Oxisols (laterites): Al₂O₃ + Fe₂O₃ left behind; bauxite ore formed
  Aridisols: CaCO₃ accumulates in Bk → caliche
  Spodosols: podzolization → Bs horizon (Fe-Al-organic complex accumulation)
```

---

## Regolith: The Full Weathering Profile

```
REGOLITH DEFINITION AND STRUCTURE
====================================

  REGOLITH = all unconsolidated material above fresh bedrock
  (includes soil, saprolite, colluvium, alluvium, loess)

  REGOLITH PROFILE:
    Soil (pedosphere): biological + chemical processing
    Saprolite: weathered bedrock; structure preserved but minerals changed
    Transition zone: saprolite → fresh bedrock
    Fresh bedrock (R)

  SAPROLITE:
    Rock structure visible: original textures, veins, inclusions preserved
    Minerals replaced by clays, oxides
    High porosity (ghost structure); very weak mechanically
    Can be 10-100 m thick in tropical settings (ancient weathering profiles)

  DURICRUSTS:
    Hardened surface layers from concentration of specific minerals:
    Laterite (ferricrete): Fe₂O₃ concentration; tropical; industrial bauxite
    Calcrete: CaCO₃ accumulation; arid climates; "caliche"
    Silcrete: SiO₂ cementation; various climates
    Gypcrete: CaSO₄·2H₂O; hyperarid (coastal fog zone)

  PLANETARY REGOLITH:
    Moon: impact gardening; 2-8 m thick; gardened to 1-2 cm/Myr
    Mars: oxidized regolith; perchlorate-rich; ferric oxides → red color
    All rocky planets have some form of regolith; thickness scales with impact history
    Absence of biological weathering → less clay, less Fe³⁺ reduction on Mars
```

---

## Weathering and the Rock Record

```
PALEOCLIMATIC INDICATORS IN SEDIMENTARY RECORD
================================================

  PALEOSOLS:
    Ancient soil horizons preserved in rock record
    Clay mineral assemblage → ancient climate (kaolinite = tropical wet)
    CIA → weathering intensity → temperature + rainfall
    δ¹³C_organic + δ¹³C_carbonate → pCO₂ reconstruction
    δ¹⁸O_carbonate → paleotemperature + paleohydrology

  CHEMICAL SEDIMENTARY PROXIES:
    Fe-speciation: ratio of reactive Fe to total Fe
      Euxinic (H₂S-rich): high pyrite Fe
      Anoxic ferruginous: high carbonate/oxide Fe
      Oxic: low reactive Fe fraction
    Ce anomaly: Ce³⁺ → Ce⁴⁺ under oxidizing conditions → depleted in seawater
      Negative Ce anomaly = oxic seawater; absent Ce anomaly = anoxic

  GREAT OXIDATION EVENT (2.4-2.0 Ga):
    Transition from anoxic to oxic atmosphere
    EVIDENCE:
    - MIF-S disappears at 2.45 Ga (see 02-ISOTOPE-SYSTEMS.md)
    - Paleosols: pre-GOE lack Fe oxidation; post-GOE iron-rich
    - Banded Iron Formations (BIFs): dominant before 1.8 Ga; record Fe²⁺ → Fe³⁺
    - Red beds appear: Fe³⁺ oxides require O₂
    CAUSE: Cyanobacterial oxygenic photosynthesis; "Great Oxygenation"
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What is the primary chemical weathering mechanism for silicates? | Hydrolysis: H⁺ (from carbonic acid or organic acids) attacks Si-O bonds, releasing cations (Ca²⁺, Mg²⁺, K⁺, Na²⁺) and producing clay minerals |
| What is CIA? | Chemical Index of Alteration = Al₂O₃/(Al₂O₃ + CaO* + Na₂O + K₂O) × 100; fresh granite ~50; kaolinite ~100; measures weathering intensity |
| Why does olivine weather faster than quartz? | Olivine formed at high T/P (thermodynamically far from surface conditions); quartz is stable near surface; minerals furthest from their formation conditions weather fastest |
| What is saprolite? | Deeply weathered bedrock with original rock structure preserved but minerals replaced by clays and oxides; can be 10-100 m thick in tropical settings |
| What is podzolization? | Soil-forming process in boreal forest: organic acids chelate Fe and Al from E horizon, move them to B horizon (Bs) where they precipitate as oxides |
| Why does silicate (not carbonate) weathering draw down CO₂ long-term? | Carbonate dissolution releases CO₂ when carbonates recrystallize in the ocean; silicate weathering produces bicarbonate from CO₂ that gets buried permanently as carbonate in the ocean → net drawdown |
| What is laterite? | Tropical weathering residue rich in Fe and Al oxides (kaolinite + gibbsite + goethite); formed by extreme leaching; low fertility; bauxite (Al ore) is a mature laterite |
| What drives the positive feedback between weathering and temperature? | Higher T → more rainfall → more weathering → more CO₂ drawdown → cooler; negative feedback that stabilizes climate on 100 kyr timescales |

---

## Common Confusion Points

**Carbonate weathering does not permanently draw down CO₂**: When CaCO₃ dissolves (CO₂ + H₂O + CaCO₃ → Ca²⁺ + 2HCO₃⁻), the carbon ends up as bicarbonate. When that bicarbonate reaches the ocean and carbonate precipitates again, CO₂ is returned. Net result: zero CO₂ removed on geological timescale. Only silicate weathering (consuming CO₂ to produce clay + bicarbonate that gets buried as carbonate) sequesters CO₂ permanently.

**Soil fertility is not the same as weathering maturity**: Oxisols (laterites) in tropical rainforests are intensely weathered and geochemically "mature" (CIA near 100) but have very low agricultural fertility — the nutrients have been leached away. The fertile soils for agriculture are Mollisols (grassland soils) with high base saturation, organic matter, and relatively unweathered minerals.

**Regolith and soil are not synonymous**: Regolith includes everything unconsolidated above bedrock — soil, saprolite, alluvial deposits, glacial till. Soil is just the biologically-active upper part with horizon development. All soils are part of the regolith, but not all regolith is soil.

**Clay minerals form, don't persist everywhere**: In very strongly acidic conditions (tropical podzolization), even kaolinite dissolves and you're left with aluminum hydroxides (gibbsite) and iron oxides only. Clay minerals are intermediate weathering products, not always the final stage.
