# Plant Nutrition and Irrigation

## The Big Picture

Plant nutrition and irrigation are two aspects of the same system: water moves through the plant, and the nutrients dissolved in that water move with it. Managing one without understanding the other produces poor results.

```
NUTRIENT DELIVERY SYSTEM:

  ATMOSPHERE: CO₂ (carbon source for photosynthesis)
       |
       v
  LEAF (stomata): CO₂ in; H₂O, O₂ out
       |             (transpiration stream drives nutrient delivery)
       |
  XYLEM (transport): water + dissolved ions move up from roots
       |
  ROOT (uptake): active (membrane transport proteins) and passive
       |         (mass flow with water)
       |
  SOIL SOLUTION: nutrients dissolved in soil water
       |
       |    <-- (fertigation adds nutrients directly here)
  SOIL SOLID: nutrients held on CEC surfaces; released by cation exchange

KEY INSIGHT:
  Most nutrient uptake is driven by mass flow (water moving through roots).
  Increase transpiration → increase nutrient delivery.
  Under-irrigation → reduced transpiration → nutrient deficiency possible
  even when nutrients are present in soil.
```

---

## Macronutrients

### Nitrogen (N)

```
FUNCTION: Component of amino acids, proteins, chlorophyll, nucleic acids.
FORMS TAKEN UP: NO₃⁻ (nitrate) and NH₄⁺ (ammonium). Both.
MOBILITY IN PLANT: Very mobile (moves to new growth). Deficiency shows
                   in old leaves first (plant remobilizes N).

DEFICIENCY: Pale yellow-green; starts on oldest leaves.
            Stunted growth; narrow leaves.
            Chlorosis uniform across leaf (vs. iron which is interveinal).

TOXICITY: Lush growth; dark green; delayed maturity; succulence (frost susceptibility).
          Excess NO₃⁻: leaches to groundwater. Excess NH₄⁺: root phytotoxicity.

FERTILIZER FORMS:
  Urea (CO(NH₂)₂ — 46%N): most concentrated N fertilizer.
    Must be hydrolyzed to NH₄⁺ by soil urease, then nitrified to NO₃⁻.
    Applied to soil surface: can volatilize as NH₃ (up to 30% loss if not incorporated).
  Ammonium nitrate (34%N): immediate NH₄⁺ and NO₃⁻ availability.
    Regulated as explosive precursor; restricted in some countries.
  Calcium ammonium nitrate (CAN, 27%N): safe, widely used.
  Ammonium sulfate (21%N): acidifying; useful in high-pH soils.
```

### Phosphorus (P)

```
FUNCTION: ATP (energy currency), nucleic acids (DNA/RNA), membranes.
          Critical for root development, flowering, and fruiting.
FORM TAKEN UP: H₂PO₄⁻ (at low pH) and HPO₄²⁻ (at higher pH).
MOBILITY IN PLANT: Mobile but less so than N. Deficiency in old leaves.
MOBILITY IN SOIL: Essentially immobile. Diffuses only ~0.1mm/day.
                  Roots and mycorrhizae must grow to P, not the reverse.

DEFICIENCY: Purple/reddish color (anthocyanin accumulation in leaves/stems).
            Especially visible on undersides of leaves and stems.
            Delayed maturity; poor root development.

FERTILIZER FORMS:
  Superphosphate (0-20-0): calcium phosphate + calcium sulfate. Cheap.
  Triple superphosphate (0-46-0): concentrated; more expensive.
  Monoammonium phosphate MAP (11-52-0): soluble; excellent for drip/fertigation.
  Diammonium phosphate DAP (18-46-0): soluble; slightly alkaline initially.

LABEL CONVENTION: P₂O₅ (not elemental P).
  To convert: %P₂O₅ × 0.437 = %P elemental.
```

### Potassium (K)

```
FUNCTION: Enzyme activation, stomatal opening/closing, osmoregulation,
          phloem loading of sugars. Not part of organic structures.
FORM TAKEN UP: K⁺.
MOBILITY IN PLANT: Very mobile. Deficiency in old leaves first.

DEFICIENCY: Marginal leaf scorch (brown edges); crinkled leaves.
            In fruit: soft fruit; poor color; reduced shelf life.
            In vegetables: tip burn (lettuce, cabbage).

FERTILIZER FORMS:
  Muriate of potash (KCl, 0-0-60): most common; very cheap.
    Contains Cl⁻ — problem for Cl-sensitive crops (tobacco, berries, potatoes).
  Potassium sulfate (K₂SO₄, 0-0-50): Cl-free; preferred for sensitive crops.
  Potassium nitrate (KNO₃, 13-0-44): provides both K and NO₃⁻; soluble.

LABEL CONVENTION: K₂O (not elemental K).
  To convert: %K₂O × 0.83 = %K elemental.
```

### Secondary Macronutrients

| Nutrient | Primary Function | Deficiency Symptom | Notes |
|----------|-----------------|-------------------|-------|
| Calcium (Ca) | Cell wall structure, membrane integrity | Blossom end rot (tomato), tip burn (lettuce), bitter pit (apple) | Immobile in plant — deficiency appears in youngest tissue; caused by water stress even when Ca present in soil |
| Magnesium (Mg) | Chlorophyll center atom, enzyme activator | Interveinal chlorosis on older leaves (Mg mobile) | Easily leached in sandy soils; corrected with Epsom salt (MgSO₄) |
| Sulfur (S) | Amino acids (methionine, cysteine), glucosinolates | Uniform yellowing of young leaves (S immobile) | Usually adequate from atmospheric deposition + organic matter |

---

## Micronutrients

Required in small quantities but have large consequences when deficient:

```
MICRONUTRIENT  FUNCTION              DEFICIENCY SYMPTOM         NOTES
─────────────────────────────────────────────────────────────────────────────
Fe (iron)      Chlorophyll synthesis  Interveinal chlorosis on  Common in high pH soils;
               (in Mg center too)     young leaves; worst in    chelated forms (EDDHA,
               Electron transport     calcareous soils          DTPA) most effective

Mn (manganese) Photosystem II        Interveinal chlorosis;     pH >7.0: rapid
               Enzyme activation      gray speck in oats        deficiency; pH <5.5:
                                      Poor shoot tips            toxicity

Zn (zinc)      Auxin synthesis,      Little leaf; rosette;      Tight pH range; deficiency
               enzyme activation      shortened internodes       common in corn (pH 6+)

Cu (copper)    Photosystem I,        Wilting; blue-green;       Peat soils low in Cu;
               enzyme activity        die-back                   toxic at low concentrations

B (boron)      Cell wall, pollen,    Hollow stem (broccoli,     Narrow sufficiency range;
               sugar translocation    cauliflower), hollow       deficiency and toxicity
                                      heart (beet), fruit crack  close together

Mo (molybdenum) Nitrate reductase,   Whiptail (cauliflower);    Required in tiny amounts;
                nitrogen fixation     cup-shaped leaves          deficiency at low pH

Cl (chlorine)   Stomatal regulation, Wilting; chlorosis         Usually adequate;
                photosystem II        Bronze leaves              toxicity more common
─────────────────────────────────────────────────────────────────────────────
```

---

## Fertilizer Calculations

### The N-P₂O₅-K₂O Label

```
FERTILIZER LABEL CONVENTION:
  Always listed as: N - P₂O₅ - K₂O
  Example: 10-5-8 means:
    10% N by weight
    5% P₂O₅ by weight → × 0.437 = 2.2% P elemental
    8% K₂O by weight → × 0.83 = 6.6% K elemental

  WHY OXIDES? Historical chemistry convention.
  P₂O₅ is how P was originally analyzed.
  Nobody actually has P₂O₅ — it's a calculated value.
  The convention persists despite being confusing.

CALCULATION EXAMPLE:
  You want to apply 100 lb N/acre.
  You have 46-0-0 urea (46% N).
  Required: 100 lb N ÷ 0.46 = 217 lb urea/acre.

  In SI:
  You want to apply 100 kg N/ha.
  Using 46-0-0 urea:
  Required: 100 ÷ 0.46 = 217 kg urea/ha.

  Application rate per 1,000 sq ft (US home use):
  1 lb N per 1,000 sq ft using 10-10-10:
  Required: 1 ÷ 0.10 = 10 lbs of 10-10-10 per 1,000 sq ft.
```

---

## Fertigation

Fertigation = injection of fertilizer into irrigation water. The delivery method for intensive horticulture:

```
FERTIGATION ADVANTAGES:
  1. Precise placement: nutrients in root zone, not lost on soil surface.
  2. Flexible timing: apply when plants need nutrients, not on calendar.
  3. Small, frequent doses: matches plant uptake rate; reduces leaching.
  4. Labor efficiency: one operation (irrigate + fertilize simultaneously).
  5. Reduced salt damage: dilute application avoids high concentration burn.

INJECTION SYSTEMS:
  Venturi injector (differential pressure):
    Main line flow past narrow section → suction draws from tank.
    Cheap ($50–500), no power, variable injection rate.
    Drawback: flow rate changes with system pressure.

  Positive displacement pump (dosatron type):
    Motorized or water-driven pump delivers fixed ratio.
    More accurate; more expensive ($200–2,000).

  Batch tank + circulation pump:
    Large tank; all water in tank then applied.
    Accurate; suited to greenhouse recirculation.

SOLUBILITY LIMITS (key nutrient sources):
  Nutrient salt           Solubility (g/L at 20°C)
  Potassium nitrate       316
  Calcium nitrate         1,290
  Monopotassium phosphate 226
  Magnesium sulfate       710
  Ammonium nitrate        1,900
  Urea                    1,080

  COMPATIBILITY:
  NEVER mix calcium salts with sulfate or phosphate solutions
  directly (precipitates form: calcium sulfate, calcium phosphate).
  Use two separate tanks (Tank A: calcium; Tank B: phosphate + sulfate).
  Mix only in the irrigation line where both are diluted.
```

---

## Irrigation Methods

### Comparison

```
METHOD           WUE*    Disease Risk   Capital   Labor    Best For
─────────────────────────────────────────────────────────────────────────────
Flood (border)   30–50%  Low (no leaves)  Low      Low    Field crops; flat land
Furrow           50–65%  Low             Low      Medium  Row crops; orchards
Overhead sprinkler 60–75% High (wet foliage) Medium Low  Field veg; germination
Drip             85–95%  Low             High     Low    Vegetables, orchards,
                                                          vine crops
Subsurface drip  90–95%  Very low        Very high Low   High-value crops,
                                                          water-limited areas
Micro-sprinkler  75–85%  Medium          Medium   Low    Orchards; tree fruits
Aeroponics       95%+    Low             Very high High  CEA; research
─────────────────────────────────────────────────────────────────────────────
*WUE = Water Use Efficiency (application vs. plant uptake)
```

### Drip Irrigation Details

```
DRIP EMITTER TYPES:
  Pressure-compensating (PC): maintains constant flow rate over
    pressure range (typically 7–70 psi). More expensive but
    essential on sloped terrain (lower emitters would otherwise flow more).
  Non-pressure-compensating: flow rate varies with pressure.
    Acceptable on flat land with uniform pressure.
  Emitter flow rates: 0.5–4 L/hr typical.

BURIED DRIP TAPE:
  Thin-walled tape (0.1–0.4mm wall) with emitters every 20–30cm.
  Used for: strawberry, lettuce, tomato, melon, cotton.
  Depths: 10–30cm below surface.
  Root intrusion: managed with high pressure flushes + Treflan (herbicide)
  or with Rootguard® emitters (copper impregnated to inhibit roots).
  Lifespan: 1 season (surface) to 15+ years (buried, careful management).
```

---

## ET-Based Irrigation Scheduling

### Penman-Monteith Equation

The gold standard for estimating evapotranspiration from weather data:

```
PENMAN-MONTEITH (FAO-56 version):
  ET₀ = [0.408Δ(Rn - G) + γ(900/(T+273))u₂(es - ea)] / [Δ + γ(1 + 0.34u₂)]

  Where:
  ET₀  = reference evapotranspiration (mm/day) for short clipped grass
  Rn   = net radiation (MJ/m²/day)
  G    = soil heat flux (MJ/m²/day) — small, often ~0 for daily calc
  T    = mean air temperature (°C)
  u₂   = wind speed at 2m height (m/s)
  es   = saturation vapor pressure (kPa) — from T
  ea   = actual vapor pressure (kPa) — from dewpoint or RH
  Δ    = slope of saturation vapor pressure-temperature curve (kPa/°C)
  γ    = psychrometric constant (kPa/°C)

IN PRACTICE:
  Weather stations (CIMIS in California, Mesonet in Oklahoma, etc.)
  calculate ET₀ automatically from measured weather variables.
  Growers subscribe to the data service.
  ET₀ is the reference for a standardized grass surface.
```

### Crop Coefficients (Kc)

```
ACTUAL CROP ET:
  ETc = ET₀ × Kc

  Kc = crop coefficient. Specific to crop + growth stage.

  Example (tomato):
  Stage         Duration   Kc
  Initial       30 days    0.60
  Rapid growth  40 days    (0.60 → 1.15, linear)
  Mid-season    40 days    1.15
  Late season   25 days    (1.15 → 0.70, linear)

  A day with ET₀ = 6mm/day, tomato at mid-season:
  ETc = 6.0 × 1.15 = 6.9 mm/day water required.

  FIELD APPLICATION:
  Drip system efficiency 90% → apply 6.9/0.90 = 7.7mm/day.
  Convert to runtime based on emitter output and spacing.
  This is the rational basis for irrigation scheduling.

DEFICIT IRRIGATION:
  Apply less than full ETc — deliberately stress the crop.
  Regulated deficit irrigation (RDI): stress at specific growth stages
  that improve quality without yield loss.
  Example: tomato at flowering — slight water stress increases lycopene;
           excessive water dilutes sugars and flavor.
  Example: wine grapes — moderate water stress from fruit set to veraison
           improves flavor concentration.
```

---

## Soil Moisture Monitoring

```
TENSIOMETER:
  Porous ceramic cup connected to vacuum gauge/pressure transducer.
  Water leaves/enters cup to equilibrate with soil moisture.
  Gauge reads soil matric potential (tension, kPa).
  Range: 0 (saturated) to ~80 kPa (before air enters ceramic).
  Limitation: range is narrow; misses dry-end measurements.
  Strength: direct measurement of matric potential (what roots feel).

  READING INTERPRETATION:
  0–10 kPa: saturated; waterlogging risk
  10–30 kPa: field capacity; ideal for most crops after rain
  30–50 kPa: slightly dry; begin irrigation for shallow-rooted crops
  50–80 kPa: moderately dry; irrigate
  >80 kPa: tensiometer loses contact; switch to other method

CAPACITANCE PROBE / TDR (Time Domain Reflectometry):
  Electromagnetic probes measure apparent dielectric constant of soil.
  Higher water content → higher dielectric constant.
  Reports: volumetric water content (VWC, % volume).
  TDR: sends EM pulse; measures travel time through probe; very accurate.
  Capacitance: continuous logging; cheaper; slightly less accurate.
  Used for: automated irrigation control, precision scheduling.

CALIBRATION:
  Both require soil-specific calibration for best accuracy.
  Generic calibrations OK for sandy soil; poor for clay and organic media.
```

---

## Decision Cheat Sheet

| Situation | Approach | Key Parameter |
|-----------|---------|--------------|
| Young transplants in field | Overhead sprinkler to establish | Keep soil surface moist for 2–3 weeks |
| Mature vegetable crop | Drip with ET-based scheduling | Kc × ET₀ = daily application |
| Orchard on sloped ground | Pressure-compensating drip | Uniform application despite pressure variation |
| Greenhouse crop (tomatoes/cucumbers) | Fertigation through drip | EC as nutrient concentration proxy; daily reading |
| Sandy soil, humid climate | Split N applications | Avoid high single doses that leach before uptake |
| Calcareous soil, iron chlorosis | Foliar FeEDDHA + soil pH management | EDDHA chelate most stable at high pH |
| Blossom end rot in tomato | Consistent irrigation + Ca in drip | Prevents water stress that blocks Ca delivery |

---

## Common Confusion Points

**P₂O₅ and K₂O are not the forms plants take up**: these are analytical conventions. Plants take up H₂PO₄⁻ (phosphate ion) and K⁺ (potassium ion). The fertilizer label uses oxide notation. Convert for plant physiology discussions; use oxide notation for fertilizer calculations.

**High soil P does not mean plants are absorbing P**: P availability depends on pH, soil moisture, and root/mycorrhiza activity. Very high soil P test values (above sufficiency range) waste money and may cause secondary micronutrient deficiencies by competitive inhibition.

**Irrigation scheduling by calendar is obsolete**: the evapotranspiration approach (ET₀ × Kc) accounts for actual weather variation. A calendar-based schedule applies the same water on a hot windy day as on a cool cloudy day — consistently wrong in opposite directions.

**EC is not the same as pH**: electrical conductivity (EC) measures total dissolved salt concentration in irrigation water or fertigation solution. It is NOT the same as pH (which measures H⁺ concentration). High EC causes osmotic stress (the soil solution is more concentrated than plant cell contents — water moves out). EC is measured in dS/m or mS/cm.

**Tensiometer readings need interpretation by crop and soil**: 40 kPa matric potential is adequate for a deep-rooted tree on clay loam but severe stress for shallow-rooted lettuce on sandy loam. The tensiometer measures soil water status; what matters to the plant depends on rooting depth, root density, and crop sensitivity.
