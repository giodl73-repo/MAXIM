# Fertilizers and Pesticides — Haber-Bosch, Synthetic NPK, Pesticide Classes, IPM

## The Big Picture

Synthetic fertilizers and pesticides are the two chemical pillars of industrial agriculture. Together they enabled the Green Revolution's yield increases — but at scale and duration, they impose costs: N pollution cascading through waterways, pesticide resistance, non-target mortality, and soil biology disruption. The discipline of Integrated Pest Management (IPM) and precision nutrient management represent attempts to get the benefits while reducing the costs.

```
+------------------------------------------------------------------+
|              CHEMICAL INPUTS TO AGRICULTURE                       |
|                                                                   |
|  FERTILIZERS                   PESTICIDES                        |
|  ──────────────────────        ─────────────────────────────── |\n|  Provide macronutrients        Kill or repel organisms that   |
|  (N, P, K) + secondaries      compete with or damage crops    |
|                                                                   |
|  SOURCES:                      CLASSES:                          |
|  Synthetic: Haber-Bosch N      Herbicides   (weeds)             |
|  Mined:     P (phosphate rock) Insecticides (insects)           |
|  Mined:     K (potash/sylvite) Fungicides   (fungi)             |
|  Organic:   manure, compost    Nematicides  (nematodes)         |
|                                Rodenticides (rodents)           |
|                                Molluscicides (slugs/snails)     |
|                                                                   |
|  GLOBAL SCALE:                                                   |
|  ~190 million tonnes N applied/yr (synthetic)                   |
|  ~4 million tonnes active ingredient pesticide/yr               |
+------------------------------------------------------------------+
```

---
<!-- @editor[bridge/P2]: No old-world bridge — Haber-Bosch is a classic chemical engineering optimization (Le Chatelier + catalyst kinetics); IPM's economic threshold logic is decision theory under uncertainty; MOA rotation is exactly an adversarial strategy against evolving opponents. The learner's MIT background covers all three frameworks — anchor to them. -->

## Haber-Bosch Process — The Most Consequential Reaction

### Background: The Nitrogen Problem

Plants need N but cannot access atmospheric N₂ (triple bond, ΔG of breaking = 945 kJ/mol):

```
NITROGEN CYCLE BEFORE HABER-BOSCH:
  N₂ (atmosphere, 78%) — almost inert
       ↓ (biological N fixation only)
  NH₄⁺ from:
    - Legume-Rhizobium symbiosis
    - Free-living Azotobacter, cyanobacteria
    - Lightning (small contribution)

  Global natural fixation: ~130 Tg N/yr

  Problem by 1900: Europe's population growth
  outstripping soil N capacity → food security crisis
  Guano (seabird droppings, Peru) and Chilean
  saltpeter (NaNO₃) being mined as N sources → finite
```

### The Synthesis

Fritz Haber (chemistry), Carl Bosch (chemical engineering) — Nobel Prizes 1918 and 1931:

```
THE HABER-BOSCH REACTION:
  N₂ + 3H₂ ⇌ 2NH₃    ΔH = -92 kJ/mol (exothermic)

EQUILIBRIUM PROBLEM:
  Le Chatelier's Principle:
    ↑ Pressure → favors product (4 mol gas → 2 mol gas)
    ↓ Temperature → favors product (exothermic reaction)
    But: low temp → reaction rate too slow

  SOLUTION (Bosch's engineering triumph):
    Pressure:    150–300 atm
    Temperature: 400–500°C (compromise — rate vs equilibrium)
    Catalyst:    Iron (Fe) promoted with K₂O and Al₂O₃
    Single-pass conversion: ~15–25%
    Unreacted gas: recycled continuously
    Yield at equilibrium (industrial): ~10–15% → acceptable
    because gas recycled

  HYDROGEN SOURCE (the hidden cost):
    Originally: water electrolysis
    Modern: steam methane reforming (SMR) of natural gas
    CH₄ + H₂O → CO + 3H₂  (then water-gas shift)
    → Haber-Bosch is tightly coupled to fossil fuel supply
    → ~1-2% of global energy consumption
    → ~1.4% of global CO₂ emissions

SCALE:
  Global production: ~180 million tonnes NH₃/yr (2023)
  ~80% used for agriculture
  Rest: explosives, plastics, industrial chemicals

  "Half of nitrogen atoms in your body passed through
   a Haber-Bosch reactor" (estimated 50% of human
   N now synthetic in origin)
```

**Historical impact:** Enabled feeding ~4 billion people who would not exist without it. Simultaneously enabled 20th-century industrial-scale warfare (nitrates for explosives from same NH₃).

---

## Synthetic N Fertilizers — Forms and Properties

```
FERTILIZER NITROGEN FORMS:

ANHYDROUS AMMONIA (NH₃):
  82% N; injected directly into soil at ~30 cm depth
  Must be sealed → volatile if exposed
  Lowest cost per unit N
  Specialist equipment; risk of escape
  Converts quickly to NH₄⁺ → then NO₃⁻ in soil

UREA (CO(NH₂)₂):
  46% N; most widely used solid fertilizer globally
  Applied: broadcast, incorporated, or UAN solution
  Converts to NH₄⁺ via urease enzyme (hydrolysis)
  PROBLEM: Volatilization as NH₃ if surface-applied
            without incorporation (can lose 20-40%)
  Solution: urease inhibitors (NBPT) slow hydrolysis

AMMONIUM NITRATE (NH₄NO₃):
  34% N; half as NH₄⁺ (slow release), half as NO₃⁻ (fast)
  Widely used in Europe; restricted in US (explosive risk)
  CAN = calcium ammonium nitrate (safer blended form)

UAN SOLUTION (28-32% N):
  Urea + ammonium nitrate in aqueous solution
  Easy to apply with liquid systems; blend with
  herbicides possible

CONTROLLED-RELEASE FERTILIZERS:
  Polymer-coated urea: release over 60-180 days
  Nitrification inhibitors: slow NH₄⁺ → NO₃⁻ conversion
  → Less leaching; higher N use efficiency (NUE)
  → Higher cost; niche use (golf, high-value horticulture)
```

**Nitrogen use efficiency (NUE):** Only ~30–50% of applied N is taken up by the crop. The rest is lost via: leaching (NO₃⁻ to groundwater), denitrification (N₂, N₂O to atmosphere), volatilization (NH₃), or immobilization in soil organic matter.

---

## Phosphorus and Potassium Fertilizers

```
PHOSPHORUS FERTILIZERS:
  Source: Phosphate rock (fluorapatite, Ca₅(PO₄)₃F)
          Mined in Morocco (~70% world reserves),
          China, Russia, USA

  Processing:
    Phosphate rock + H₂SO₄ → superphosphate
    (SSP: 18-20% P₂O₅; TSP: 46% P₂O₅)
    Phosphate rock + phosphoric acid → DAP, MAP
    DAP (18-46-0): diammonium phosphate — most used
    MAP (11-52-0): monoammonium phosphate

  KEY CONCERN: Phosphate rock is non-renewable
    Estimated reserves: 50–300 years at current use
    (highly contested; Morocco holds strategic position)
    Phosphorus cannot be synthesized — only recycled
    → "Peak phosphorus" concern: global food security
       fundamentally tied to phosphate mining access

POTASSIUM FERTILIZERS:
  Source: Potash deposits (ancient evaporite basins)
          Sylvite (KCl): Canada, Russia, Belarus (~75% reserves)
          Langbeinite, kainite (contain K + Mg + S)

  Muriate of potash (MOP): KCl, 60% K₂O (most common)
  Sulfate of potash (SOP): K₂SO₄, 50% K₂O + S
                           (use when Cl⁻ sensitive crops: potato, some fruits)

  Belarus/Russia dominate supply →
  2022 sanctions disrupted global K supply → price spike
```

---

## Pesticide Classes — Mechanisms of Action

### Herbicides

```
HERBICIDE MODE OF ACTION (MOA):

PHOTOSYNTHESIS INHIBITORS (Group C):
  Atrazine (triazine): blocks PSII electron transport
  Linuron (urea): same target
  Use: corn, sorghum; very widely used in US
  Problem: Atrazine groundwater contamination widespread

AMINO ACID SYNTHESIS INHIBITORS:
  ALS inhibitors (Group B):
    Sulfonylureas, imidazolinones
    Block acetohydroxy acid synthase → branched AA synthesis stops
    Very low use rates (grams/ha vs kg/ha)
    High resistance evolution risk

  EPSP inhibitors (Group G):
    Glyphosate (Roundup): blocks EPSPS enzyme in shikimate pathway
    → No shikimate pathway in animals (hence low mammalian toxicity)
    Broad-spectrum; kills almost all vegetation
    Basis of GMO herbicide-tolerant crops (Roundup Ready)
    Half-life in soil: 2–197 days (highly variable, binds to clay)
    Global use: >800 million kg/yr (most used herbicide on Earth)
    Resistance evolution: >250 weed species now resistant

CELL MEMBRANE DISRUPTORS (Group E):
  PPO inhibitors (e.g., lactofen): generate reactive oxygen species
  → Membrane lipid peroxidation → rapid cell death
  Contact herbicide; good resistance management tool

SYNTHETIC AUXINS (Group O):
  2,4-D, dicamba, MCPA
  Mimic auxin (IAA) → disrupt cell elongation in dicots
  Selective: monocots (grass, grain crops) not affected
  Old herbicides (2,4-D since 1944) but still widely used
  Dicamba: volatility → drift to non-target crops problem
```

### Insecticides

```
INSECTICIDE CLASSES AND TARGETS:

ORGANOPHOSPHATES (OPs):
  Mechanism: inhibit acetylcholinesterase (AChE)
             → acetylcholine accumulates → nerve overstimulation
  Examples: chlorpyrifos, malathion, parathion
  Broad-spectrum; high vertebrate toxicity (same AChE)
  Most OPs phased out from food uses in developed world

CARBAMATES:
  Same target (AChE) as OPs; reversible inhibition
  Examples: carbofuran, carbaryl (Sevin)
  Lower persistence; still used but declining

PYRETHROIDS (synthetic pyrethrins):
  Target: Na⁺ voltage-gated channels → stay open → paralysis
  Examples: cypermethrin, permethrin, deltamethrin
  Low mammalian toxicity (temperature-dependent Na channel)
  Very toxic to fish, aquatic invertebrates, bees
  Highly stable; widely used in grain storage, cotton, vegetables

NEONICOTINOIDS:
  Target: nicotinic acetylcholine receptors (nAChR) — systemic
  Examples: imidacloprid, clothianidin, thiamethoxam
  Systemic: taken up by plant, expressed in all tissues including nectar/pollen
  Highly effective on sucking insects (aphids, whiteflies)
  Bee toxicity: linked to colony collapse disorder (contested but restricted in EU)
  Most widely used insecticide class globally (>25% of market)

Bt TOXINS (biological, not synthetic):
  Bacillus thuringiensis proteins disrupt insect gut
  Cry proteins bind to brush border → pore formation → death
  Used as spray; also expressed in Bt-GMO crops
  Highly specific (lepidoptera, coleoptera, diptera strains)
  Safe for vertebrates, beneficial insects (mostly)

DIAMIDES:
  Target: ryanodine receptors (muscle Ca²⁺ release channels)
  Examples: chlorantraniliprole, cyantraniliprole
  Low vertebrate toxicity; high efficacy on caterpillars
  Newer class; resistance emerging
```

### Fungicides

```
FUNGICIDE CLASSES:

DEMETHYLATION INHIBITORS (DMIs, Group 3):
  Triazoles: tebuconazole, propiconazole, prothioconazole
  Imidazoles: prochloraz
  Block ergosterol biosynthesis (fungal membrane lipid)
  → Systemic; preventive and curative
  Most widely used fungicide class (cereals, soybeans, fruits)

QUINONE OUTSIDE INHIBITORS (QoIs/Strobilurins, Group 11):
  Azoxystrobin, trifloxystrobin
  Block Complex III (bc₁) in mitochondrial electron transport
  Very broad spectrum; powerful systemic activity
  RESISTANCE RISK: single point mutation (G143A) confers
  near-complete resistance → must rotate MOA

SDHI (Succinate Dehydrogenase Inhibitors, Group 7):
  Boscalid, fluxapyroxad, benzovindiflupyr
  Block Complex II of mitochondrial ETC
  Newer, effective; resistance developing rapidly in some pathogens

MULTI-SITE INHIBITORS (Group M):
  Mancozeb (dithiocarbamate), chlorothalonil, copper
  Multiple sites → resistance evolution very slow
  Used as tank mix partners to protect at-risk MOA fungicides
  Copper: oldest fungicide (Bordeaux mixture since 1882);
          heavy metal accumulation in organic viticulture
```

---

## Integrated Pest Management (IPM)

IPM is a decision framework that uses multiple control methods, with pesticides as a last resort rather than first response:

```
IPM HIERARCHY (decision ladder):

1. PREVENTION (no inputs required)
   Crop rotation → breaks pest/disease cycles
   Resistant varieties → genetic defense
   Timing (plant/harvest to avoid peak pest)
   Sanitation (remove volunteer plants, infected residue)
   Correct fertility → avoid lush growth that attracts pests

2. MONITORING + ECONOMIC THRESHOLDS
   Scout fields: sample pest populations (counts/trap)
   Economic Injury Level (EIL): crop loss = pesticide cost
   Economic Threshold (ET): pest density requiring action
   → Do NOT spray below ET (economic + resistance logic)

   EXAMPLE: Soybean aphid ET = 250 aphids/plant
   before R1 (flowering), with increasing population
   → Below threshold: no spray, rely on natural enemies
   → Above threshold: treat if population rising

3. BIOLOGICAL CONTROL
   Conservation biocontrol: habitat for natural enemies
     (wildflower strips, hedgerows → parasitoids, predators)
   Augmentative biocontrol: release Trichogramma wasps,
     lacewings, ladybeetles for greenhouse/field
   Classical biocontrol: introduce natural enemy from
     country of origin of invasive pest
     (requires careful host-specificity testing)

   Natural enemies can suppress 50-80% of pest populations
   if not disrupted by pesticide applications

4. CULTURAL AND MECHANICAL CONTROL
   Trap crops: plant preferred host on border → concentrate pests
   Physical barriers: row covers, sticky traps, copper tape
   Precision cultivation: mechanical weed control between rows
   Soil solarization: solar heating kills soilborne pathogens

5. TARGETED CHEMICAL CONTROL (last resort)
   Select: most specific MOA for target pest
   Rotate MOA: never use same group consecutively
   Time: spray at vulnerable life stage, avoid flowering
   Buffer: maintain buffer zones near water, sensitive areas
   Record: track usage for resistance monitoring
```

**Resistance management — the MOA rotation principle:**

```
RESISTANCE EVOLUTION:
  Any pest population contains rare resistant individuals
  Pesticide exposure selects for these → survive, reproduce
  → Resistance can evolve in 2-20 generations depending on
     selection pressure, inheritance, migration

PREVENTION:
  Rotate MOA (mode of action): different biochemical target
    in alternating applications or seasons
  Refuge strategy: leave 20% of field unsprayed → susceptible
    individuals survive, dilute resistance alleles
  Tank mixes: two MOAs simultaneously → double mutation
    required (extremely rare) for resistance
  Biological + chemical rotation: break selection pressure

IRAC/FRAC/HRAC: insecticide/fungicide/herbicide resistance
  action committees maintain MOA numbering system
  Always check Group number (1, 2, 11, 14...) not trade name
```

---

## Environmental Impacts of Agricultural Chemicals

```
NITROGEN POLLUTION CASCADE:

  NH₃ volatilization
    → atmospheric deposition to sensitive ecosystems
    → N eutrophication of lichens, bogs (most sensitive)

  NO₃⁻ leaching to groundwater
    → Drinking water contamination (>10 mg/L = health risk)
    → EU Nitrates Directive, US MCL = 10 mg/L

  NO₃⁻ to surface water
    → Algal blooms → eutrophication → hypoxia
    → Gulf of Mexico Dead Zone: ~22,000 km² hypoxic zone
       fed by Mississippi River agriculture
    → Baltic Sea, Chesapeake Bay, Black Sea similar

  N₂O emissions from soil denitrification
    → GHG with GWP 265× CO₂ (100-yr)
    → Agriculture: ~60% of global anthropogenic N₂O
    → Denitrification increased by excess N application
       and wet conditions

PHOSPHORUS POLLUTION:
  P attached to soil particles → surface runoff → water
  P drives eutrophication in freshwater (N in marine)
  "Legacy P" in soils takes decades to flush through
  No atmospheric sink → accumulates in sediments

PESTICIDE ENVIRONMENTAL FATE:
  Persistence: DT₅₀ (time for 50% degradation)
    Glyphosate: 2-200 days (variable)
    Chlorpyrifos: 30-60 days soil; hours in water
    Imidacloprid: 40-1200 days (soil type dependent)

  Non-target impacts:
    Bees: neonicotinoids, pyrethroids
    Aquatic invertebrates: pyrethroids (ng/L lethal doses)
    Birds: rodenticides (secondary poisoning raptors)
    Natural enemies: broad-spectrum insecticides → pest resurgence
```

---

## Decision Cheat Sheet

| Situation | Action |
|-----------|--------|
| High N demand crop (corn, wheat); precision approach | Split N application (starter + sidedress); presidedress N test (PSNT) to calibrate in-season |
| Surface-applied urea; summer heat/rain | Use urease inhibitor (NBPT) or incorporate within 24 hr to prevent volatilization |
| Weed control; herbicide resistance suspected | Test field populations; rotate to different MOA Group; include multi-site inhibitor in tank mix |
| Pest approaching Economic Threshold | Identify species; select narrow-spectrum insecticide for that pest; protect beneficial insects |
| Fungal disease pressure in cereal | Rotate DMI + SDHI + multi-site; do NOT use same Group 3 two years running |
| Water near field; runoff risk | Setback buffers; banded fertilizer placement; slow-release N; foliar-applied P |
| Phosphate rock supply concern | Prioritize P recycling (manure P accounting); struvite recovery from wastewater; reduce P to legacy-P soils |

---

## Common Confusion Points

**Haber-Bosch "fixed" nitrogen but not the yield problem alone** — The synthesis provides NH₃, but that had to be converted to forms plants could absorb (NO₃⁻ via nitrification), distributed globally, and paired with the right crop genetics. The Green Revolution combined Haber-Bosch N with high-yielding dwarf varieties that could absorb more N without lodging (falling over). N without good varieties = lodged crops, not yield gains.

**"Organic" pesticides aren't automatically safer** — Organic-approved pesticides (rotenone, copper sulfate, pyrethrin, spinosad) can be toxic to non-target organisms. Rotenone is an aquatic toxin; copper accumulates in soil. The certification "organic" refers to source (natural), not to toxicological safety or environmental impact.

**Glyphosate's low mammalian toxicity ≠ environmental safety** — Glyphosate's LD₅₀ is low for mammals (shikimate pathway absent). But it: disrupts soil microbiome (EPSPS present in bacteria), kills non-target plants (weed pressure shifts), and is found ubiquitously in water/food due to scale of use. "Safe" claims and "dangerous" claims are both context-dependent.

**Economic Threshold logic prevents resistance too** — Spraying below ET not only wastes money; it also applies selection pressure without fully controlling the population, accelerating resistance while not achieving economic benefit. IPM's economic discipline and resistance discipline align: less spraying = better outcomes both ways.

**Phosphorus is fundamentally non-renewable at human timescales** — Unlike nitrogen (Haber-Bosch can be powered by renewables), phosphorus must come from phosphate rock. There is no synthetic alternative. This makes P supply — geographically concentrated in Morocco — a genuine long-term food security constraint that doesn't have a technology fix, only recycling and efficiency improvements.
