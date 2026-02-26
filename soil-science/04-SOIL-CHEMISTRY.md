# Soil Chemistry: CEC, pH, Redox, Mineral Nutrients, Buffering

## The Big Picture

Soil chemistry determines which nutrients are available to plants and microorganisms. Four interacting chemical systems govern this: cation exchange capacity (CEC, the nutrient holding capacity), soil pH (the master chemical variable controlling almost everything else), redox chemistry (controlling nutrient forms in wet soils), and specific nutrient chemistry (P sorption, Al toxicity, liming).

```
SOIL CHEMISTRY — FOUR INTERACTING SYSTEMS

  CEC                         pH
  +------------------+        +------------------+
  | Holding capacity |        | Controls nutrient|
  | for cation       | <----> | availability,    |
  | nutrients        |        | Al/Fe solubility,|
  | (Ca,Mg,K,NH4+)   |        | microbial activity|
  +------------------+        +------------------+
          |                           |
          +---------------------------+
          |
  REDOX (Eh)                  NUTRIENT CHEMISTRY
  +------------------+        +------------------+
  | Saturated soils  |        | P sorption to Fe/Al|
  | Fe/Mn reduction  | <----> | N mineralization  |
  | N2O/N2 formation |        | Micronutrient     |
  | Anaerobic zone   |        | availability      |
  +------------------+        +------------------+
```

---

## Section 1 — Cation Exchange Capacity (CEC)

CEC is the total capacity of a soil to hold exchangeable cations. It is the most important single chemical property for predicting nutrient-holding ability.

### Definition and Units

```
  CEC = total amount of exchangeable positive ions a soil can hold
  Units: cmolc/kg = centimoles of charge per kg = meq/100g (identical values)
  (milliequivalents per 100 grams = the traditional unit, still widely used)

  EXCHANGE SITES are negative charges on:
  +-- Clay mineral surfaces (permanent negative charge from isomorphous substitution)
  +-- Humus/organic matter surfaces (variable charge; pH-dependent)
  +-- Fe/Al oxide surfaces (variable charge; can be positive at low pH)

  EXCHANGEABLE CATIONS (held at negative sites):
  Ca²⁺, Mg²⁺, K⁺, Na⁺, Al³⁺, H⁺, NH₄⁺, Fe²⁺/³⁺, Mn²⁺
  These are plant-available when soil solution concentrations drop
  (plant uptake creates concentration gradient --> desorption from exchange sites)
```

### CEC by Component

```
  CEC CONTRIBUTION BY MATERIAL:

  SMECTITE (montmorillonite):   80–150 cmolc/kg  [high; 2:1 clay]
  Vermiculite:                 100–150 cmolc/kg  [very high; 2:1]
  Illite:                        10–40 cmolc/kg  [moderate]
  Kaolinite:                      1–15 cmolc/kg  [low; 1:1 clay]
  Fe/Al oxides:                   0–5 cmolc/kg   [very low]
  Humus/organic matter:         150–300 cmolc/kg  [very high]

  TYPICAL SOIL CEC VALUES:
  Sandy soil:        2–5 cmolc/kg   (minimal clay; minimal OM)
  Sandy loam:        5–12           (low-moderate clay)
  Loam:             10–20           (moderate clay + OM)
  Silt loam:        15–25
  Clay loam:        20–35
  Clay (smectitic):  30–60
  Organic soil (peat): > 50–100     (dominated by OM contribution)

  IMPLICATION: Tropical Oxisols have CEC of 1–5 cmolc/kg despite 60–80% clay
               (kaolinite + Fe/Al oxides = low CEC per clay unit)
               --> Cannot hold cation nutrients; nutrients leached rapidly
               Temperate Mollisols: CEC 25–40 (smectite + high SOM)
               --> Nutrient bank; fertilizer retained; minimal leaching
```

### Base Saturation

```
  BASE SATURATION (BS%) = proportion of CEC occupied by "base" cations
  Base cations: Ca²⁺, Mg²⁺, K⁺, Na⁺ (plant-beneficial)
  Acid cations: Al³⁺, H⁺ (occupy sites; at high % = Al toxicity risk)

  BS% = (Ca + Mg + K + Na exchangeable) / CEC × 100

  INTERPRETATION:
  > 80%: base-rich; neutral-alkaline pH; fertile; minimal Al toxicity
  50–80%: moderate; neutral-slightly acid; Alfisols
  < 35%: acid, low pH; Ultisols; significant Al toxicity risk
  < 20%: highly leached; acidic; Spodosols, Oxisols; Al dominates

  CATION SATURATION RATIOS (Albrecht concept):
  Ideal saturation: Ca 70–80%, Mg 10–15%, K 2–5%, Na < 3%
  Ca:Mg ratio: 4:1 to 8:1 optimal (imbalances affect grass quality, soil structure)
  Ca:K ratio: 20:1 to 100:1 (K excess reduces Ca uptake; luxury consumption)
```

---

## Section 2 — Soil pH

pH is the master variable of soil chemistry. Almost every soil chemical process — nutrient solubility, microbial activity, mineral weathering, Al toxicity — is pH-dependent.

### pH and Nutrient Availability

```
  NUTRIENT AVAILABILITY vs. SOIL pH (classic Truog diagram, 1947):

  pH:        4.0   5.0   6.0   7.0   8.0   9.0
             |     |     |     |     |     |
  NITROGEN   ████░░████████████████░░░░░░
  PHOSPHORUS ███░░░████████████████░░░░░
  POTASSIUM  ████████████████████████░░
  SULFUR     ████████████████████░░░░░░
  CALCIUM    ████░████████████████████
  MAGNESIUM  ████░████████████████████
  IRON       █████████░░░░░░░░░░░░░░░░
  MANGANESE  ████████░░░░░░░░░░░░░░░░░
  BORON      ████░░████████████░░░░░░░
  COPPER     ████████████████░░░░░░░░░
  ZINC       ████████████████░░░░░░░░░
  MOLYBDENUM ░░░░░░░████████████████

  ████ = high availability   ░░░░ = low availability

  KEY PATTERN:
  Most nutrients: optimal availability at pH 6.0–7.0
  Micronutrients (Fe, Mn, Zn, Cu): MORE available at low pH (acid soils)
  Molybdenum: MORE available at high pH
  Phosphorus: maximum at pH 6.0–6.5 (forms insoluble precipitates at both extremes)
  At pH < 5.5: Al³⁺ and Mn²⁺ become toxic (solubility increases dramatically)
```

### Aluminum Toxicity

```
  AL TOXICITY MECHANISM:
  At pH < 5.5: Al(OH)3 dissolves --> Al³⁺ soluble in soil solution
  Al³⁺ + root tips --> inhibits cell division in root apex
  --> Root tips brown, stubby, proliferating near surface
  --> Unable to absorb water or nutrients from depth
  --> Crop yield collapses even if P/K/N are adequate

  Al TOXICITY THRESHOLD:
  Sensitive crops (wheat, soybean): > 0.5 mg Al/L = toxicity
  Tolerant crops (maize, sorghum): tolerate up to 2–5 mg Al/L
  Al-accumulating plants (tea, Camellia): thrive at pH 4.5–5.5;
  require Al for flavonoid production

  MANGANESE TOXICITY:
  At pH < 5.5: Mn²⁺ also increases sharply
  Mn toxicity: leaf necrosis, "manganese spot"
  Threshold: > 50 ppm Mn in plant tissue
```

### Soil pH Buffering

```
  BUFFERING CAPACITY:
  Soils resist pH change due to:
  1. Carbonates: CaCO3 neutralizes acid (high buffering at pH > 7)
     CaCO3 + H2SO4 --> CaSO4 + H2O + CO2
  2. Clay CEC: releases base cations from exchange sites when H+ added
  3. Organic matter: carboxyl groups act as weak acid buffer
  4. Al hydroxides: dissolve and consume H+ at pH < 5.5

  BUFFERING POWER BY SOIL TYPE:
  Sandy low-OM soil:    very low buffering (1 kg lime raises pH sharply)
  Loam with 3% OM:      moderate buffering
  Clay with smectite:   high buffering
  Organic soil (peat):  very high buffering (enormous acid input required)
```

---

## Section 3 — Liming

Liming raises soil pH by adding calcium or magnesium carbonates or oxides.

```
  COMMON LIMING MATERIALS:
  +--------------------+----------+----------+----------------------------+
  | Material           | CCE%     | Speed    | Notes                      |
  +--------------------+----------+----------+----------------------------+
  | Calcitic lime      | 85–100%  | Moderate | Ca only; finely ground     |
  | (ground limestone, |          |          | works faster; coarse slow  |
  |  CaCO3)            |          |          |                            |
  +--------------------+----------+----------+----------------------------+
  | Dolomitic lime     | 95–109%  | Moderate | Ca + Mg; if Mg deficient,  |
  | (CaMg(CO3)2)       |          |          | preferred choice           |
  +--------------------+----------+----------+----------------------------+
  | Hydrated lime      | 120–135% | Fast     | Caustic; can over-apply;   |
  | (Ca(OH)2)          |          |          | industrial use             |
  +--------------------+----------+----------+----------------------------+
  | Burnt lime         | 150–175% | Very fast| Very reactive; caustic;    |
  | (CaO)              |          |          | specialist use only        |
  +--------------------+----------+----------+----------------------------+

  CCE = Calcium Carbonate Equivalent (neutralizing power vs. pure CaCO3)

  LIMING RATE CALCULATION:
  Rate (t/ha) = ΔpH_target × Buffer_pH_factor / CCE

  BUFFER pH: measurement of soil's buffering capacity (SMP buffer test)
  Compares field pH vs. buffer solution to estimate lime requirement
  Typical Midwest corn belt loam at pH 5.5, target 6.5:
  ~2–4 t/ha of 85% CCE calcitic lime (specific to soil type and buffering capacity)

  LIMING REACTIONS:
  CaCO3 + H2O + CO2 --> Ca²⁺ + 2HCO3⁻  (dissolution; HCO3- is buffering agent)
  2HCO3⁻ + 2H⁺ --> 2H2O + 2CO2         (neutralizes soil acidity)
  Net: CaCO3 + 2H+ (acid soil) --> Ca²⁺ + H2O + CO2
```

---

## Section 4 — Phosphorus Chemistry

P chemistry in soil is more complex than N — P forms highly insoluble compounds with Fe, Al, and Ca, severely limiting availability.

```
  P FORMS IN SOIL:

  SOLUTION P (bioavailable): PO4³-, H2PO4-, HPO4²-
  pH controls speciation:
  pH < 7: H2PO4- (monovalent) dominates
  pH > 7: HPO4²- (divalent) dominates
  pH > 9: PO4³- (trivalent) -- most strongly sorbed; very low bioavailability

  P SORPTION TO IRON AND ALUMINUM OXIDES (acid soils):
  At low pH: abundant Fe³⁺ and Al³⁺ oxides
  PO4³- adsorbs to oxide surfaces: Fe-OH + H2PO4- --> Fe-OPO3H2 + OH-
  At high sorption: P "fixed" in unavailable form
  Oxisols: up to 90% of added fertilizer P sorbed within days!

  P FIXATION AT HIGH pH:
  At pH > 7: Ca²⁺ abundant
  Ca²⁺ + HPO4²- --> CaHPO4 (dicalcium phosphate; slightly soluble)
  Further: 3Ca²⁺ + 2PO4³- --> Ca3(PO4)2 (insoluble)
  Eventually: Ca5(PO4)3OH (hydroxyapatite; very insoluble)

  MAXIMUM P AVAILABILITY: pH 6.0–6.5
  (minimum Fe/Al oxide sorption + maximum Ca-P solubility)

  P SATURATION DEGREE (DPS):
  DPS = P_soil_Oxalate / (Fe_oxalate + Al_oxalate) × 100
  DPS > 25% = elevated P loss risk to water
  DPS > 40% = high P loss risk; soil no longer able to retain P
```

---

## Section 5 — Redox Chemistry in Waterlogged Soils

When soils are flooded, O2 depletes and microbial respiration shifts to alternative electron acceptors. This creates reducing conditions (low Eh, low redox potential) that transform soil chemistry fundamentally.

```
  REDOX SEQUENCE (as soils become wetter and O2 depletes):

  Eh (mV)    Reaction                            Effect
  +800       Aerobic respiration (O2 reduced)    Normal aerobic soil
  +300       NO3- reduced to N2 (denitrification) N loss as gas; N2O produced
  +200       Mn4+ reduced to Mn2+               Mn becomes soluble (gray/brown)
  +100       Fe3+ reduced to Fe2+               Iron released; gray color
   -100      SO4²- reduced to S2- (H2S)         Rotten egg smell; H2S toxic to roots
   -200      CO2 reduced to CH4                 Methanogenesis; bubbles

  INDICATOR in soil:
  Gray/green/blue-gray matrix = reduced Fe (Fe2+) under saturation
  Orange-red mottles (redox concentrations) = oxidized Fe (Fe3+) where O2 enters
      near root channels or drying cracks

  WETLAND SOIL CHEMISTRY:
  Fe reduction --> Fe2+ increases --> P released (Fe-P bond breaks)
  NH4+ increases (denitrification depletes NO3-, mineralization produces NH4+)
  Mn2+ increases (can be toxic)
  pH shifts: acid soils rise toward neutral (H+ consumed)
             alkaline soils fall toward neutral (OH- consumed by reduction)
  --> Waterlogged soils often converge to pH 6–7 regardless of initial pH
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is CEC and what determines it? | Total cation-holding capacity; determined by clay type (smectite > kaolinite) and organic matter content |
| At what pH is phosphorus most available? | pH 6.0–6.5 (minimum Fe/Al oxide sorption and maximum Ca-P solubility) |
| Why is Al³⁺ toxic to most crops? | Inhibits root tip cell division at pH < 5.5; roots become stubby, can't absorb water or nutrients from depth |
| Why do tropical Oxisols have low CEC despite high clay? | Kaolinite (1:1 clay) has CEC of 1–15 cmolc/kg; Fe/Al oxides essentially 0; smectite gone after deep weathering |
| What is base saturation? | Fraction of CEC occupied by base cations (Ca, Mg, K, Na); < 35% defines Ultisols |
| Why does liming work? | CaCO3 + 2H⁺ → Ca²⁺ + H₂O + CO₂; carbonate neutralizes soil acidity; raises pH; displaces Al from exchange sites |
| What happens to P when soil floods? | Fe³⁺ reduced to Fe²⁺; Fe-P bond breaks; P released to soil solution (internal loading mechanism) |

---

## Common Confusion Points

**CEC and nutrient content are different measurements.**
A high CEC soil (e.g., smectite-rich Vertisol) can hold large quantities of nutrient cations, but if those sites are occupied by Al³⁺ and H⁺ (low pH), there are no plant-available nutrients. Always measure both CEC and base saturation (or individual extractable cation levels) to assess fertility.

**pH affects micronutrients opposite to macronutrients.**
Fe, Mn, Zn, Cu availability increases at lower pH — they are more soluble under acid conditions. Liming to optimal pH (6.5) reduces their availability. On high-pH calcareous soils, Fe chlorosis (yellowing from Fe deficiency) is common in sensitive crops, not because Fe is absent but because it's insoluble.

**Phosphorus sorption in tropical soils means fertilizer efficiency is very low.**
In Oxisols, phosphorus fertilizer applied at conventional rates can be 80–90% "fixed" within days. Farmers may need to apply 5–10× more P than in temperate soils to achieve the same plant response. Mycorrhizal associations are particularly critical in these P-fixing environments.

**Waterlogged soil pH convergence to neutral seems paradoxical.**
Acid soils rise in pH when flooded because H⁺ is consumed by Fe³⁺ and Mn⁴⁺ reduction (consuming H⁺). Alkaline soils fall because CO₂ from anaerobic respiration forms carbonic acid. Both systems move toward pH 6–7 under prolonged flooding — a useful guide for interpreting paddy soil chemistry.
