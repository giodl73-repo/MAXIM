# Nutrient Cycling: Nitrogen Fixation, Nitrification, Phosphorus Cycle

## The Big Picture

Soil nutrient cycling is the engine of terrestrial productivity — the biochemical machinery that converts atmospheric gases and mineral elements into plant-available forms and back again. Nitrogen and phosphorus are the most commonly limiting nutrients, but their cycling pathways are fundamentally different: nitrogen cycles through gas phases (atmospheric N₂ pool; N₂O and N₂ losses), while phosphorus is entirely sedimentary (no atmospheric pool; driven by weathering and biological transformation).

```
NUTRIENT CYCLE COMPARISON

  NITROGEN CYCLE              PHOSPHORUS CYCLE
  +------------------+        +------------------+
  | Atmospheric pool |        | No atmospheric   |
  | (78% N2 in air)  |        | pool (closed     |
  | N2 fixation      |        | system; sediment-|
  | Denitrification  |        | ary cycle only)  |
  | N2O (GHG)        |        | Weathering input |
  | Gas exchange     |        | Sorption to Fe/Al|
  | with atmosphere  |        | Microbial P cycl.|
  +------------------+        +------------------+
  OPEN SYSTEM:                CLOSED SYSTEM:
  N can enter (fixation)      P inputs only from
  N can leave (denitrif.)     weathering + deposition;
  N can leave (leaching       losses only to erosion
  as NO3-)                    and water export
```

---

## Section 1 — The Nitrogen Cycle in Soils

### N Fixation

Biological nitrogen fixation (BNF) is the only natural pathway by which atmospheric N₂ (triple-bonded, chemically inert) enters the biological N cycle.

```
  NITROGENASE REACTION:
  N2 + 8H+ + 8e- + 16 ATP --> 2NH3 + H2 + 16 ADP + 16 Pi

  Energy cost: 16 ATP per N2 fixed (enormous; most expensive biological reaction)
  Enzyme: nitrogenase (has Fe-Mo cofactor; sensitive to O2)
  All nitrogen fixers: ANAEROBIC sites (O2 inhibits nitrogenase)
    Aerobic fixers (Azotobacter): protect nitrogenase with respiratory O2 scavenging
    Legume root nodules: leghemoglobin maintains microaerobic conditions in nodule

  RATES OF BIOLOGICAL N FIXATION:
  +--------------------------+----------+-----------------------------------+
  | System                   |Rate      | Conditions for maximum fixation   |
  |                          |(kg N/ha/yr)                                  |
  +--------------------------+----------+-----------------------------------+
  | Rhizobium (soybean)      | 100–300  | Low soil N; acid pH 6.0–7.5;     |
  | Rhizobium (alfalfa)      | 150–250  | adequate P, Mo, Fe; correct       |
  | Rhizobium (clover)       |  50–200  | Rhizobium strain                  |
  | Bradyrhizobium (cowpea)  |  80–150  | Warm temperature                  |
  +--------------------------+----------+-----------------------------------+
  | Frankia (alder, Alnus)   |  50–150  | Riparian; early succession        |
  | Frankia (bayberry, etc.) |  20– 80  | Actinorhizal associations         |
  +--------------------------+----------+-----------------------------------+
  | Azotobacter (free-living)|   0.2–5  | Aerobic; limited by C supply      |
  | Clostridium (free-living)|   0.1–2  | Anaerobic soils; wet              |
  | Cyanobacteria (rice)     |  10– 50  | Flooded paddy; blue-green mats    |
  +--------------------------+----------+-----------------------------------+

  IMPORTANCE:
  Global BNF: ~120–140 Tg N/yr (agriculture-induced ~50 Tg; natural ~60–90 Tg)
  Haber-Bosch (industrial N fixation): ~120–130 Tg N/yr (as fertilizer)
  Haber-Bosch has doubled N availability in terrestrial ecosystems since ~1960
```

### Mineralization (Ammonification)

```
  MINERALIZATION:
  Organic N (proteins, nucleic acids, chitin) --> NH4+ (ammonium)
  Performed by: heterotrophic bacteria and fungi (decomposers)
  Requires: O2 for aerobic organisms; also occurs anaerobically (slower)

  CONTROLS:
  C:N RATIO OF SUBSTRATE:
  C:N < 20: Net mineralization (N released as NH4+)
  C:N > 25: Net immobilization (N taken up by microbes; not available to plants)
  C:N = 20–25: Transition zone; variable

  PRACTICAL EXAMPLES:
  Legume cover crop (C:N 12–20): NET N RELEASE; plant available within 2–4 wk
  Cereal straw (C:N 70–100): NET N IMMOBILIZATION; may cause N deficiency 2–6 wk
  Manure (C:N 10–20 depending on type): NET N RELEASE; variable
  Humus (C:N 10–12): SLOW net release

  TEMPERATURE EFFECT:
  Q10 ~ 2: rate doubles per 10°C increase
  Wet warm soils mineralize N very rapidly
  Cold soils: slow mineralization; N accumulates in SOM over winter
  "Nitrogen flush": rapid mineralization at spring thaw
```

### Nitrification

```
  NITRIFICATION (aerobic; two-step):

  STEP 1: NH4+ + 1.5 O2 --> NO2- + H2O + 2H+   (Nitrosomonas, Nitrospira)
  STEP 2: NO2- + 0.5 O2 --> NO3-                (Nitrobacter, Nitrospira)

  NET: NH4+ + 2O2 --> NO3- + H2O + 2H+

  IMPORTANT: Each nitrification step PRODUCES H+ (acid)
  --> Repeated N fertilizer application as ammonium lowers soil pH
  --> Calcification required in intensive ammonia-based systems

  CONTROLS:
  O2: strict aerobic requirement; stops below ~2% O2
  pH: inhibited below pH 5.5; optimal 6.5–8.0
  Temperature: optimal 25–35°C; slow below 5°C
  NH4+ substrate: rate depends on NH4+ availability

  ENVIRONMENTAL SIGNIFICANCE:
  NO3- is mobile (anion; not sorbed by negative CEC sites)
  --> Leaches to groundwater (nitrate contamination of wells)
  --> Leaches to streams (eutrophication)
  N2O produced as a byproduct during nitrification:
  NH4+ --> N2O (side reaction at low O2; during nitrifier denitrification)
  N2O: GWP = 273 (100-yr); ~7% of global GHG emissions from agricultural soils
```

### Denitrification

```
  DENITRIFICATION (anaerobic):
  NO3- --> NO2- --> NO --> N2O --> N2

  Performed by: facultative anaerobes when O2 depleted
  Key genera: Pseudomonas, Paracoccus, Thiobacillus denitrificans

  REQUIREMENTS:
  1. Anoxic conditions (O2 < 0.2 mg/L in soil water; saturated pores)
  2. NO3- as terminal electron acceptor
  3. Organic C as electron donor (energy source)
  4. Temperature > 5°C (optimal 25–35°C)

  CONTROLS:
  "DNDC" (denitrification-decomposition) model: hot spots + hot moments
  HOT SPOTS: wet, aggregated microsites within otherwise well-drained soil;
             footslope positions; near manure amendments
  HOT MOMENTS: post-rain events; spring thaw; manure application followed by rain

  GLOBAL DENITRIFICATION:
  ~10% of applied N fertilizer lost to denitrification (average; varies 0–50%)
  N2O intermediate: released to atmosphere from partial denitrification
  Complete denitrification (to N2): benign; just removes N
  Incomplete (to N2O): climate problem
```

### The Nitrogen Budget (Arable Field)

```
  TYPICAL CORN FIELD NITROGEN BUDGET:

  INPUTS:
  Fertilizer applied:      200 kg N/ha/yr
  BNF (minimal in corn):     5 kg N/ha/yr
  Atmospheric deposition:  15 kg N/ha/yr
  Soil N mineralization:   50 kg N/ha/yr
  TOTAL INPUT:             ~270 kg N/ha/yr

  OUTPUTS:
  Crop N uptake:           150 kg N/ha/yr  (removed in grain + stover)
  NO3- leaching:            50 kg N/ha/yr  (to groundwater)
  Denitrification (N2):     20 kg N/ha/yr
  N2O emission:              5 kg N/ha/yr  (potent GHG)
  NH3 volatilization:       20 kg N/ha/yr  (from surface-applied urea)
  TOTAL OUTPUT:            ~245 kg N/ha/yr

  SURPLUS: ~25 kg N/ha/yr accumulating in soil organic matter
           or building in soil solution
  N use efficiency of applied fertilizer: ~150/200 = 75% (above average)
  In reality many fields: 50–60% NUE; large environmental losses
```

---

## Section 2 — Phosphorus Cycle

### P Cycle Pathways

```
  PHOSPHORUS CYCLE (soil):

  PRIMARY MINERAL P (apatite, feldspar):
  [Ca5(PO4)3OH = hydroxyapatite; most common P mineral]
          |
          | Chemical weathering (hydrolysis, dissolution)
          | Rate: slow; 0.1–1 kg P/ha/yr from rock weathering
          v
  INORGANIC SOIL P (solution + sorbed forms)
          |                          |
          | Plant/microbial uptake   | P sorption to Fe/Al oxides
          |                          | or Ca precipitation (at high pH)
          v                          v
  ORGANIC P (in plant/microbial biomass)
          |
          | Decomposition (phosphatase enzymes)
          v
  INORGANIC P (back to solution)

  KEY DIFFERENCE FROM N: No gaseous P forms; no atmospheric reservoir
  P lost from ecosystem only by: erosion, streamflow, harvest (crop P removal)
  P gained only by: weathering, atmospheric dust, applied fertilizer/manure
```

### Phosphorus Sorption Isotherms

```
  SORPTION ISOTHERM:
  Relationship between P in solution (Ceq) and P sorbed to soil (q):

  LANGMUIR ISOTHERM:
  q = (qmax × k × Ceq) / (1 + k × Ceq)

  Where:
    q = P sorbed (mg P/kg soil)
    qmax = maximum sorption capacity (mg P/kg soil)
    k = affinity constant (L/mg P)
    Ceq = equilibrium solution P concentration (mg P/L)

  FREUNDLICH ISOTHERM (empirical):
  q = Kf × Ceq^n
  log q = log Kf + n × log Ceq  (linear on log-log plot)

  SORPTION CAPACITY RANGES:
  Sandy soil, low Fe/Al:     qmax = 50–200 mg P/kg
  Loam, moderate Fe/Al:      qmax = 200–500 mg P/kg
  Clay, high Fe/Al:          qmax = 500–2000 mg P/kg
  Oxisol (tropical, Al rich): qmax = 1000–4000+ mg P/kg

  P BUFFER POWER:
  High sorption capacity = "P buffer" -- resists change in solution P
  Good for: prevents P loss; bad for: plants must "pay" more to access P
  Fertilizer P efficiency inversely related to sorption capacity
```

### Mycorrhizal P Acquisition

```
  WHY MYCORRHIZAE ARE ESSENTIAL FOR P IN MOST SOILS:
  1. Root depletion zone: P in soil solution diffuses VERY SLOWLY (Dp ~ 10-13 m²/s)
     Diffusion rate: ~1 mm/day; root depletes P in ~1 mm sphere rapidly
     Roots cannot physically grow fast enough to access fresh P
  2. AM hyphae: 2–5 µm diameter; penetrate pores too small for roots
     Access 100–1000× soil volume compared to root hairs alone
  3. Organic P mineralization: phosphatase enzymes released by hyphae
     Hydrolyze organic P into plant-available orthophosphate

  QUANTITATIVE IMPACT:
  Non-mycorrhizal plant in P-limited soil: 5–30 mg P uptake/plant
  Mycorrhizal plant: 50–300 mg P uptake/plant (10× increase common)
  In some agroecosystems: 40–80% of P in crop comes via AM pathway

  MANAGEMENT IMPLICATION:
  High P fertilization rates suppress AM colonization (plant down-regulates symbiosis)
  --> Creates P dependency (crop requires high P fertilizer input)
  --> Reduced AM colonization in intensively fertilized soils (worldwide problem)
  --> Transition to lower P input requires rebuilding AM inoculum (2–5 yr)
```

---

## Section 3 — Liebig's Law of the Minimum

```
  LIEBIG'S LAW (1840 formulation):
  "Plant growth is limited by the most limiting nutrient, regardless
   of the abundance of all other nutrients"

  MODERN INTERPRETATION:
  Growth proceeds at rate limited by MOST SCARCE nutrient relative to demand
  Adding non-limiting nutrients: zero yield response
  Adding limiting nutrient: yield response proportional to deficiency

  LIEBIG BARREL ANALOGY:
  +-----+-----+-----+-----+-----+-----+
  |  N  |  P  |  K  |  Ca |  Mg | ... |
  +     |     |     |     |     |     |
  |     |     |     +-----+     |     |
  |     |     |           |     |     |
  |     +-----+           |     |     |
  |                       |     |     |
  +-----                  +-----+-----+
  Water level = growth rate; shortest stave = limiting nutrient

  COLIMITATION:
  When two nutrients are NEARLY equally limiting, both limit growth together
  Adding either alone: small response
  Adding both together: large synergistic response
  Common: N+P colimitation in soils where both are near-deficient
  N+S colimitation: high-input agriculture in S-depleted soils

  MODERN EXTENSION — ECOLOGICAL STOICHIOMETRY:
  Organisms have fixed elemental composition (homeostasis)
  Plant tissue C:N:P ratios approximately 500:10:1 (wide variation)
  Microbial biomass: C:N ~6–10:1; C:P ~60–100:1
  If substrate C:N >> microbial C:N: N immobilized (microbial nutrient demand > supply)
  Determines whether added organic matter mineralizes or immobilizes N (see Guide 06)
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| How much N does soybean fix per year (symbiotic)? | 100–300 kg N/ha/yr with functional Rhizobium |
| Why does straw incorporation cause N deficiency? | C:N of straw (70–100:1) >> microbial C:N (6–10:1); microbes immobilize soil mineral N to decompose straw |
| Why is denitrification a "hot moment" process? | Requires simultaneous anoxia + NO3- + C; occurs in short events (rain, thaw) not continuously |
| What is P sorption and why does it matter? | Orthophosphate adsorbs to Fe/Al oxides; reduces plant-available P; Oxisols need 5–10× more fertilizer |
| What is the P diffusion problem for roots? | P diffuses only ~1 mm/day; roots deplete the P sphere; AM hyphae solve this by accessing larger soil volume |
| What happens when N fertilizer (urea) is applied to acidic soil? | Nitrification produces 2H+ per NH4+ oxidized; progressively acidifies; requires liming |
| How much of global N fixation is industrial vs. biological? | Both ~120–140 Tg N/yr; total ~250 Tg N/yr; doubled N availability since pre-industrial |

---

## Common Confusion Points

**N immobilization is not N loss.**
When microbes immobilize N (C:N > 25 substrate), N is taken up into microbial biomass — not lost from the system. It will eventually be re-mineralized when microbes die and their biomass is decomposed. The practical problem is TIMING: immobilization can last 4–8 weeks, creating N deficiency in a fast-growing crop.

**Mycorrhizal P uptake and fertilizer P are not interchangeable.**
AM fungi access P from soil pores and organic fractions that are not accessible to roots. They do not simply increase uptake from fertilizer P added to soil. In fact, excessive fertilizer P suppresses AM colonization, reducing the plant's "P foraging network" for future P acquisition.

**The N₂O problem is from BOTH nitrification and denitrification.**
N₂O is produced during incomplete denitrification (N₂O not fully reduced to N₂) AND during nitrification at low O₂. Many field N₂O emissions come from microsites where nitrification occurs adjacent to denitrification zones — the two processes interfacing at aggregate boundaries.

**Phosphorus "saturation" of a soil does not mean P is no longer retained.**
Even at DPS > 40% (high P saturation), soils continue to sorb additional P, just at lower efficiency. The concern is not that P stops being sorbed but that a larger fraction escapes in drainage water — particularly during storm events that mobilize P-enriched surface soil and runoff.
