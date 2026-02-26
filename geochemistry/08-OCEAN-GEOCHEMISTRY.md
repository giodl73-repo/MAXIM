# Ocean Geochemistry and the Marine Record

## The Big Picture

The ocean is the primary integrator of the Earth's geochemical cycles. It receives elements from rivers and hydrothermal vents, cycles them biologically and chemically, and buries a record of Earth's past chemistry in deep-sea sediments.

```
+------------------------------------------------------------------+
|                    OCEAN GEOCHEMICAL SYSTEM                       |
+------------------------------------------------------------------+
|                                                                  |
|  INPUTS                  CYCLING                OUTPUTS          |
|  ------                  -------                -------          |
|  Rivers (weathering)     Biological pump        Carbonate burial  |
|  Hydrothermal vents      Thermohaline circ.     Organic C burial  |
|  Atmospheric deposition  Scavenging             Evaporite burial  |
|  Submarine volcanism     Adsorption onto        Clay mineral sed. |
|  Benthic fluxes          particles              Hydrothermal exch.|
|                          Remineralization                         |
|                          Dissolution                              |
+------------------------------------------------------------------+
```

---

## Seawater Composition

```
MAJOR ION COMPOSITION OF SEAWATER (S = 35‰)
=============================================

  ION         CONC (mmol/kg)    FRACTION OF TOTAL SALT
  ---         ---------------   ----------------------
  Cl⁻         546               55.1%
  Na⁺         469               30.6%
  SO₄²⁻       28.2              7.7%
  Mg²⁺        53.1              3.7%
  Ca²⁺        10.3              1.2%
  K⁺          10.2              1.1%
  HCO₃⁻       2.1               0.4%
  Br⁻         0.84              0.19%
  Total DIC:  2.1-2.3 mM

  CONSTANCY OF RELATIVE PROPORTIONS:
    Seawater composition is nearly identical everywhere
    (Dittmar's Principle, 1884)
    Despite inputs from rivers, hydrothermal vents, evaporation/precip.
    Reason: residence times >> mixing timescale of ocean (~1000 yr)

  pH:  7.9-8.3 (surface); 7.4-8.0 (deep); decreasing ~0.002/yr now
  Alkalinity: ~2350 μmol/kg
  T_mix: ~100-1000 yr (average ocean mixing)
```

---

## Residence Times

Ocean residence time τ = stock / flux is the mean lifetime of an atom in the ocean reservoir — formally identical to the time constant of a first-order linear system. If you add an impulse of element X to the ocean, it decays exponentially with time constant τ: [X](t) = [X]₀ e^(-t/τ). This is the same math as RC circuit discharge, radioactive decay, or any linear removal process. Elements with τ >> ocean mixing time (~1000 yr) become uniformly distributed (conservative elements: Na, Cl, Mg). Elements with τ << mixing time are heterogeneous in concentration across ocean basins (scavenged elements: Al, Fe, Co, Pb, Th). The residence time concept directly determines which elements can be used as tracers of ocean circulation (short τ → records recent changes) versus which are robust records of total input (long τ → integrated signal).

```
ELEMENT RESIDENCE TIMES IN SEAWATER
=====================================

  DEFINITION: τ = (amount in ocean) / (input flux)
              = (amount in ocean) / (removal flux)

  LONG τ (millions of years → well-mixed, conservative):
    Na⁺      68 Myr
    Mg²⁺     13 Myr
    Cl⁻      87 Myr
    SO₄²⁻    11 Myr
    K⁺       7 Myr
    → These are "conservative" — constant concentration at given S

  INTERMEDIATE τ (kyr-Myr):
    Ca²⁺     1 Myr
    Sr²⁺     4 Myr (→ seawater ⁸⁷Sr/⁸⁶Sr curve = mixing of inputs)
    Li⁺      1 Myr

  SHORT τ (yr-kyr → highly variable, biological control):
    Ba        10,000 yr
    Al³⁺      200 yr    (rapid scavenging onto particles)
    Fe²⁺/³⁺   200 yr   (extremely low; biologically limiting)
    Mn        40-100 yr
    PO₄³⁻    150,000 yr
    NO₃⁻     ~10,000 yr
    Si        20,000 yr  (removal by diatoms/radiolarians)
    Rare Earth: <500 yr (scavenging-dominated)

  KEY INSIGHT:
    τ >> ocean mixing time (~1000 yr) → element is well-mixed (uniform [])
    τ < ocean mixing time → element varies with location (non-conservative)
```

---

## The Biological Pump

```
BIOLOGICAL PUMP ARCHITECTURE
=============================

  SURFACE OCEAN (photic zone, 0-200 m)
    CO₂ + H₂O --photosynthesis--> organic matter + O₂
    Nutrient uptake: N, P, Si, Fe, Zn, Co
    CaCO₃ production by forams, coccolithophores
    BSi (biogenic silica) production by diatoms, radiolarians

    ↓  sinking particles (faecal pellets, aggregates, "marine snow")

  EXPORT PRODUCTION:
    ~10% of primary production sinks below 100 m (export efficiency)
    ~1-2% reaches 1000 m depth
    ~0.1-0.3% reaches seafloor
    90% of organic matter remineralized in upper 200 m

  DEEP OCEAN (mesopelagic + bathypelagic)
    Remineralization by bacteria: organic matter oxidized by O₂
    → O₂ depletion; CO₂ production; nutrient regeneration
    → Oxygen Minimum Zone (OMZ): ~200-1000 m; O₂ near zero

  SEAFLOOR
    Burial: ~0.1% of surface production permanently buried
    Remineralization: ~99.9% oxidized at seafloor or in water column

  REDFIELD RATIO (Redfield, 1934):
    C:N:P = 106:16:1 in marine organic matter
    This ratio governs nutrient cycling
    When organic matter remineralizes, it releases:
    106 CO₂ : 16 NH₄⁺ : 1 HPO₄²⁻ (+ H₂O, H⁺)
    Seawater N:P ≈ 16:1 (reflects Redfield)
    Deviations → N-limitation (tropical) or P-limitation (depends on timescale)
```

---

## Ocean Circulation and Chemical Transport

```
THERMOHALINE CIRCULATION AND WATER MASSES
==========================================

  SURFACE WATER:
    Warm, low density; in contact with atmosphere
    ~200 m deep; temperature gradient in thermocline
    δ¹³C DIC: relatively high (+2.5‰) — biological pump enriches ¹³C
    δ¹⁸O seawater: ~0‰ SMOW (slightly positive in tropics due to evap)

  NORTH ATLANTIC DEEP WATER (NADW):
    Formation: surface water cools at high latitude; becomes dense; sinks
    T: 2-4°C; S: 34.9-35.0‰; ρ: ~1027.8 kg/m³
    High O₂ (recently at surface); low nutrients; high δ¹³C DIC
    Flows south through the Atlantic and into Indian/Pacific Oceans

  ANTARCTIC BOTTOM WATER (AABW):
    Densest water; forms near Antarctica (sea ice formation + cooling)
    T: -0.5 to -1.5°C; S: ~34.65‰; ρ: ~1028 kg/m³
    Flows along seafloor globally (oldest water in deep sea)

  PACIFIC DEEP WATER (PDW):
    Old (upwelling Atlantic deep water aged by ~1000 yr in Pacific)
    Low O₂; high nutrients; low δ¹³C DIC
    → "Nutrient trap" of Pacific

  δ¹³C DIC GRADIENT:
    Atlantic deep: +0.5 to +1.0‰ (young water; high O₂; low nutrients)
    Pacific deep: -0.2 to +0.2‰ (old water; organic C remineralized → ¹²C added)
    → Used to reconstruct past ocean circulation
    → Cd/Ca in benthic forams: proxy for nutrient (PO₄) gradient
```

---

## Trace Metal Biogeochemistry

```
TRACE METAL BEHAVIOR CLASSIFICATION
=====================================

  NUTRIENT-TYPE:       depleted in surface by biology; enriched in deep
    Zn:   2-9 nmol/kg surface; >6 nmol/kg deep
    Cd:   <0.2 nmol/kg surface; ~1 nmol/kg deep
    Si:   <1-2 μmol/kg surface; >100 μmol/kg deep
    Fe:   <0.1 nmol/kg surface; ~0.5-1 nmol/kg deep
    Ba:   surface low; deep enriched (BaSO₄ dissolution)

  SCAVENGED-TYPE:      removed rapidly by particle adsorption
    Al:   ~30 nmol/kg; highest near dust inputs; low everywhere
    Pb:   highly variable; anthropogenic signal clear
    REE:  removed by adsorption; fractionation by scavenging
    Th:   strong scavenging; ²³⁰Th/²³¹Pa ratio: ocean circulation proxy

  CONSERVATIVE-TYPE:   constant at given salinity
    Na, Cl, Mg, SO₄:  major ions; conservative
    Mo:   ~107 nmol/kg; well-mixed; long τ (~800 kyr)
    U:    ~13 nmol/kg; conservative at modern redox; removed under anoxia

  REDOX-SENSITIVE:     behavior switches between oxic and anoxic
    Fe, Mn, V, Cr, U, Mo, Re:
      In oxic water: sorbed, insoluble, or oxidized
      In anoxic water: reduced, soluble, mobile
    → Enrichment in black shales = paleo-anoxia indicator
    → U enrichment: redox-controlled burial
```

---

## Paleoceanographic Proxies

```
SEDIMENT PROXY TOOLKIT FOR PALEOCEANOGRAPHY
============================================

  PROXY          MATERIAL          WHAT IT RECORDS
  -----          --------          ---------------
  δ¹⁸O           Forams            T + ice volume (see 04-STABLE-ISOTOPE)
  Mg/Ca           Forams            Temperature (partition coeff T-dependent)
  B/Ca            Forams            Carbonate saturation state (Ω)
  δ¹¹B            Forams            Ocean pH
  Ba/Ca           Forams            Productivity proxy (nutrient flux)
  Zn/Ca           Forams            Zn in deep water (nutrient circulation)
  δ¹³C DIC        Forams            Ocean circulation + productivity
  Cd/Ca           Benthic forams    Deep water PO₄ (nutrient distribution)
  δ¹³C_org        Bulk sediment     Organic matter source; carbon cycle
  ³H excess       -                 U-series dating of sediment
  ²³⁰Th           Sediment          Particle flux normalization (²³⁰Th constant)
  ⁸⁷Sr/⁸⁶Sr      Carbonates        Global weathering rate (continental vs oceanic)
  Mo/U ratio      Black shale       Redox proxy; euxinic vs ferruginous anoxia
  ε_Nd (εNd)      Fish teeth, FeMn  Deep water circulation (Nd source tracing)

  FORAMINIFERAL Mg/Ca THERMOMETRY:
    Mg/Ca_foram = A × e^(B × T)  (species-specific calibration)
    B ≈ 0.09-0.1 per °C for most planktonic species
    Typically: Mg/Ca (mmol/mol) increases ~9-10% per °C
    Combined with δ¹⁸O → separate T from ice volume (powerful technique)

  ²³⁰Th NORMALIZATION:
    ²³⁰Th produced at constant rate in water column (U in seawater)
    Scavenged quickly onto sinking particles → proportional to their flux
    Measure ²³⁰Th in sediment → normalize other proxies to constant production
    → Account for varying accumulation rates (dissolution, dilution, winnowing)
```

---

## Seawater ⁸⁷Sr/⁸⁶Sr Curve

```
STRONTIUM ISOTOPE STRATIGRAPHY
================================

  PRINCIPLE:
    Seawater ⁸⁷Sr/⁸⁶Sr is a global signal:
    INPUT 1: Rivers (weathering of old continental crust): HIGH ⁸⁷Sr/⁸⁶Sr (~0.712)
    INPUT 2: Hydrothermal vents (mantle Sr): LOW ⁸⁷Sr/⁸⁶Sr (~0.703)
    MEAN residence time of Sr: ~4 Myr → ocean is well-mixed → uniform globally

    Sr is conservative → recorded in marine carbonates and phosphates at time of precipitation

  THE SEAWATER ⁸⁷Sr/⁸⁶Sr CURVE:
    0 Ma:    0.70917 (modern; rising rapidly)
    5 Ma:    0.70900
    23 Ma:   0.70875 (Oligocene-Miocene minimum)
    34 Ma:   0.70780 (Eocene-Oligocene boundary; more hydrothermal input?)
    65 Ma:   0.70780
    140 Ma:  0.70700 (Mesozoic minimum; high volcanism / hydrothermal)
    500 Ma:  0.70790 (Cambrian)

  USES:
    Chemostratigraphy: age of a marine carbonate by reading the Sr curve
    (requires knowing the curve well and that the sample is unaltered)
    Resolution: works best where curve changes rapidly (e.g., rapid rise since 23 Ma)
    LIMITATION: Where curve is flat → poor time resolution

  HIMALAYAN UPLIFT SIGNAL:
    Sr curve rises steeply from 20 Ma to present
    Himalayan uplift → exposure of radiogenic basement → high ⁸⁷Sr riverine input
    → Monsoon intensification → more continental weathering
    → Well-constrained record of Cenozoic climate-tectonic coupling
```

---

## Nutrient Cycling and Limitation

```
MARINE NUTRIENT DYNAMICS
==========================

  MACRO-NUTRIENTS (mol scale):
    Nitrogen (N): Nitrate (NO₃⁻) dominant in deep; assimilated as NO₃⁻ or NH₄⁺
    Phosphorus (P): Phosphate (PO₄³⁻); recycled from sediment
    Silicon (Si): Silicic acid (H₄SiO₄); used by diatoms, radiolarians

  REDFIELD RATIO IN NUTRIENT CYCLING:
    DIN:DIP = 16:1 (dissolved inorganic N:P) in deep water ≈ Redfield
    Deviation → nutrient limitation:
    High N:P (N excess): P-limiting
    Low N:P (P excess): N-limiting
    Most open ocean: N-limiting (N is depleted by denitrification + N₂ fixation)

  IRON (Fe) LIMITATION:
    HNLC regions (High Nutrient, Low Chlorophyll):
      Southern Ocean, equatorial Pacific, subarctic Pacific
    Nutrients present but no phytoplankton bloom → Fe is limiting
    Evidence: iron fertilization experiments (ADD Fe → BLOOM)
    Fe sources: aeolian dust (Saharan dust → Atlantic)
                upwelling from sediments
                hydrothermal plumes (significant Fe source)

  TRACE METAL CO-LIMITATION:
    Zn: part of carbonic anhydrase; limits coccolithophores at low pH?
    Co: vitamin B12 cofactor; low in open ocean
    Mn: photosystem II; may co-limit in some regions
    → Multiple trace metal limitation; complex interactions
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What does residence time tell you? | How long an element stays in the ocean; long τ → well-mixed → conservative; short τ → variable → biological or scavenging-controlled |
| What is the Redfield ratio? | C:N:P = 106:16:1 in marine organic matter; governs nutrient cycling; seawater N:P ≈ 16:1 reflects biological control |
| What drives the biological pump? | Photosynthesis in surface waters fixes CO₂ into organic matter; sinking of particles exports C to the deep; organic C burial is the long-term CO₂ sink |
| Why is deep Pacific depleted in O₂ and enriched in nutrients vs. Atlantic? | Pacific deep water is older (longer transit time from formation); more remineralization of organic C has occurred → more O₂ consumed, more nutrients released |
| What is the ²³⁰Th normalization method? | ²³⁰Th is produced at constant rate from U in seawater and scavenged onto sinking particles; sediment ²³⁰Th content normalizes other flux estimates for varying accumulation rate |
| What controls seawater ⁸⁷Sr/⁸⁶Sr? | Balance between river input (continental weathering; high ⁸⁷Sr/⁸⁶Sr ~0.712) and hydrothermal input (mantle Sr; ~0.703); Himalayan uplift drives the Cenozoic rise |
| What makes the HNLC regions paradoxical? | High nitrate + phosphate, but low productivity → iron is the limiting nutrient; adding Fe causes blooms (verified by experiments) |
| How does Cd/Ca record ocean circulation? | Cd in seawater co-varies with PO₄; benthic foram Cd/Ca records bottom water Cd (∝ PO₄) → reconstructs past nutrient distributions = past circulation patterns |

---

## Common Confusion Points

**"Well-mixed" ocean has a ~1000-yr timescale**: The ocean is not mixed on human timescales. Deep water formed in the North Atlantic takes ~500-1000 years to circulate through the deep Pacific. This is why deep ocean CO₂ uptake is slow — the mixing timescale limits exchange between surface and deep.

**The biological pump is not a simple conveyor belt**: Only ~0.1-0.3% of surface production is buried permanently. The vast majority is remineralized by bacteria in the water column or at the seafloor. The "efficiency" of the pump varies by ecosystem type, particle aggregation, and seafloor depth.

**Mn nodules are not being formed everywhere on the seafloor**: Mn-Fe nodule fields occur on slow-accumulating pelagic sediments where the sediment accumulation rate is slower than Mn oxide precipitation rate (~1 mm/Myr for sediment). Fast-accumulating sediments bury nodules before they form. The "strategic minerals" in nodules are economically significant but extraction is technically and environmentally complex.

**The Dittmar principle holds for major ions, not trace metals**: Major ions (Na, Cl, Mg, SO₄) maintain constant relative proportions because their residence times far exceed ocean mixing. Trace metals with short residence times (Fe, Al, Mn) vary widely across ocean basins. The "constant proportions" rule does not apply to trace elements.
