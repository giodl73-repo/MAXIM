# 18-ECOLOGY — Ecology

## Ecosystems, Population Dynamics, Food Webs, Biogeochemical Cycles, Conservation

---

## Big Picture: Ecology's Scale Hierarchy

```
LEVELS OF ECOLOGICAL ORGANIZATION
───────────────────────────────────────────────────────────────────
  Individual  →  Population  →  Community  →  Ecosystem  →  Biosphere
     │               │               │              │             │
  physiology     demographics    interactions    energy flow   global cycles
  behavior       growth models   food webs       nutrients     climate
  adaptation     dispersal       succession      trophic       planetary
                                                 structure     boundaries

CORE QUESTIONS AT EACH LEVEL:
  Individual:   How does organism survive/reproduce in its environment?
  Population:   Why do numbers go up and down? What regulates them?
  Community:    Who eats whom? What determines which species coexist?
  Ecosystem:    How does energy flow? How do nutrients cycle?
  Biosphere:    What are the global consequences of biology?

ECOLOGICAL TIMESCALES:
  Individual:    seconds → years (behavioral responses, lifespan)
  Population:    years → centuries (demographic dynamics)
  Community:     decades → millennia (succession, evolution)
  Ecosystem:     centuries → Myr (soil formation, biogeochemical change)
  Biosphere:     Myr → Gyr (atmospheric composition, mass extinctions)
───────────────────────────────────────────────────────────────────
```

---

## Niche Theory

```
HUTCHINSON'S NICHE HYPERVOLUME (1957)
  Niche = n-dimensional hypervolume where a species can survive & reproduce
  Each dimension = an environmental variable (temperature, food size, salinity, etc.)

  Fundamental niche: where organism can physically survive (no competition)
  Realized niche:    where organism actually lives (competitive exclusion reduces it)

  Niche overlap → competition (if resources limited)
  Character displacement: evolution reduces niche overlap between competitors
    Classic example: Darwin's finches beak sizes diverge where species coexist

COMPETITIVE EXCLUSION PRINCIPLE (Gause, 1934):
  Two species with identical niches cannot coexist indefinitely
  Empirical test: Paramecium aurelia vs P. caudatum in the same tube → one wins
  Coexistence requires niche differentiation (partitioning of resources)

NICHE CONSTRUCTION:
  Organisms modify environment → alter selective pressures on themselves and others
  Examples: beaver dams, earthworm bioturbation, plant litter, coral reefs
  Creates evolutionary feedback between organism and environment
```

---

<!-- @editor[bridge/P3]: Natural bridge to CS/math — Lotka-Volterra equations are coupled nonlinear ODEs; Leslie matrix is a linear recurrence (eigenvalue problem). The learner's MIT math background maps directly: population dynamics = dynamical systems theory, metapopulations = graph connectivity. -->
## Population Ecology

```
BASIC DEMOGRAPHIC EQUATION:
  ΔN = Births + Immigration − Deaths − Emigration
  dN/dt = B − D = rN  (simplest continuous form)

EXPONENTIAL GROWTH:
  dN/dt = rN   where r = intrinsic rate of natural increase = b − d
  Solution: N(t) = N₀ · eʳᵗ
  Doubling time: t_double = ln(2)/r ≈ 0.693/r
  J-shaped curve — describes early growth with unlimited resources
  r selection (fast-growing species): high r, small body size, short lifespan

LOGISTIC GROWTH (Verhulst, 1838):
  dN/dt = rN · (K − N)/K
  K = carrying capacity (resources set upper limit)
  S-shaped curve (sigmoidal)
  As N → K: growth rate → 0

  Inflection point at N = K/2 → maximum rate of increase
  Maximum sustainable yield (fisheries): harvest at K/2 (theory)

  K selection: competitive strategy, slow growth, large K
  r-K continuum is useful heuristic (replaced by life history theory in modern ecology)

AGE-STRUCTURED MODELS — LESLIE MATRIX:
  Population vector: n(t) = [n₁, n₂, ..., nₖ] (individuals in each age class)
  Leslie matrix L: contains age-specific fecundities (F) and survival probabilities (P)
  n(t+1) = L · n(t)
  Dominant eigenvalue λ₁ of L = finite rate of increase (λ>1 growing, λ<1 declining)

SURVIVORSHIP CURVES:
  Type I:   most mortality late (humans, large mammals) — high parental investment
  Type II:  constant mortality rate (birds, small mammals)
  Type III: most mortality early (fish, trees, invertebrates) — many offspring, low survival

METAPOPULATION DYNAMICS (Levins, 1969):
  A set of local populations connected by dispersal
  Patch occupancy p: dp/dt = cp(1−p) − ep
  c = colonization rate, e = local extinction rate
  Equilibrium: p̂ = 1 − e/c  (patches go extinct but are recolonized)
  Threshold: if c < e, entire metapopulation goes extinct
  Important for conservation: habitat fragmentation creates metapopulations
```

---

## Species Interactions

```
INTERACTION TYPES (population effects on each species):
  Competition    (−/−)  both harmed
  Predation      (+/−)  predator gains, prey loses
  Herbivory      (+/−)  same structure as predation
  Mutualism      (+/+)  both benefit
  Commensalism   (+/0)  one benefits, other unaffected
  Parasitism     (+/−)  parasite benefits, host harmed
  Amensalism     (0/−)  one harmed, other unaffected

LOTKA-VOLTERRA PREDATOR-PREY EQUATIONS:
  dV/dt = rV − aVP          prey: grow exponentially, eaten by predators
  dP/dt = bVP − mP          predator: grow by eating prey, die at rate m

  Parameters:
    V = prey density, P = predator density
    r = prey intrinsic growth, a = predation rate
    b = conversion efficiency (prey → predator offspring), m = predator mortality

  Zero isoclines:
    Prey: P = r/a   (prey stable when predators at this level)
    Predator: V = m/b (predators stable when prey at this level)

  Oscillating cycles: predator-prey cycle with ¼ period lag (prey peaks before predator)
  Classic example: Canadian lynx–snowshoe hare data (Hudson's Bay Company, 1845-1935)
  Real complexity: hare cycle driven by plant quality + predators (not purely Lotka-Volterra)

  Paradox of enrichment (Rosenzweig, 1971):
    Adding nutrients to prey → destabilizes system → predator-prey oscillations increase
    Counter-intuitive: enriching ecosystem can cause collapse of food web

COMPETITION — LOTKA-VOLTERRA:
  dN₁/dt = r₁N₁(K₁ − N₁ − α₁₂N₂)/K₁
  dN₂/dt = r₂N₂(K₂ − N₂ − α₂₁N₁)/K₂
  α₁₂ = effect of species 2 on species 1 (competition coefficient)
  Coexistence requires: intraspecific > interspecific competition (α₁₂ · α₂₁ < 1)
  Otherwise one excludes the other (outcome depends on initial conditions if priority effects)

MUTUALISM:
  Obligate: neither can survive without partner (fig-fig wasp, yucca-yucca moth)
  Facultative: beneficial but not required (most pollination)
  Mycorrhizal networks: fungal hyphae ↔ plant root: fungus gets carbohydrates,
    plant gets water + nutrients. Present in ~90% of plant species.

TROPHIC CASCADE:
  Predator suppresses prey → releases prey's prey from competition/predation
  Wolves → elk → willows → riparian vegetation → stream structure (Yellowstone)
  Sea otters → sea urchins → kelp forests (Pacific coast)
  Loss of apex predator unravels ecosystem structure (trophic downgrading)
```

---

## Community Ecology

```
COMMUNITY STRUCTURE:
  Food chain: linear sequence of who eats whom (rare in nature)
  Food web: complex network of feeding relationships

  Trophic levels:
    1st: primary producers (plants, algae, chemolithotrophs)
    2nd: primary consumers (herbivores)
    3rd: secondary consumers (carnivores)
    4th: tertiary consumers (top predators)
    Detritivores/decomposers: break down dead organic matter (cross-level)

ENERGY FLOW — 10% RULE (Lindeman, 1942):
  Only ~10% of energy transfers from one trophic level to the next
  (range: 5-20%; ~10% is rough average)
  Losses: respiration, heat, unassimilated food, excretion

  Consequence: food chains limited to ~4-5 trophic levels
  Why vegetarian diets are more efficient (more direct solar energy)

  Primary Productivity:
    GPP (Gross Primary Productivity): total photosynthesis
    NPP (Net Primary Productivity) = GPP − plant respiration
    Secondary productivity: animal biomass production from NPP

    Terrestrial NPP by biome (gC/m²/yr):
      Tropical rainforest:  ~2200 (highest)
      Temperate forest:     ~1200
      Grassland:            ~700
      Desert:               ~100
      Tundra:               ~140
      Open ocean:           ~140 (but huge area)

KEYSTONE SPECIES (Paine, 1966):
  Disproportionately large effect on ecosystem relative to abundance
  Remove keystone → dramatic community reorganization
  Sea star Pisaster ochraceus: removed from intertidal → mussels (prey) dominate
    eliminated 15 species → monoculture of mussels
  NOT all top predators are keystone species (need disproportionate effect)

ECOLOGICAL SUCCESSION:
  Primary succession: bare substrate (lava flow, glacier retreat) → climax community
    Pioneer → intermediate → climax stages over decades-centuries
    Soil development (pedogenesis) is the key process
    Example: Glacier Bay, Alaska: ~250 years from bare rock to spruce forest

  Secondary succession: existing soil, prior species removed (fire, farming)
    Faster (decades) because soil intact
    Old-field succession (eastern US): annual weeds → perennial herbs → shrubs → forest

  Facilitation: pioneer species modify environment, enable later species
  Tolerance: later species tolerate pioneer conditions (not facilitated)
  Inhibition: pioneer species inhibit later ones until pioneer dies

  Intermediate disturbance hypothesis: maximum diversity at intermediate disturbance
    Frequent disturbance → only disturbance-adapted species
    No disturbance → competitive exclusion → low diversity
    Intermediate → many species at different successional stages

BIODIVERSITY METRICS:
  α (alpha) diversity: species richness within a site
  β (beta) diversity: turnover of species between sites
  γ (gamma) diversity: total diversity across regional landscape

  Shannon index H' = −Σ pᵢ ln(pᵢ)   (accounts for evenness)
  Simpson's D = 1 − Σ pᵢ²           (probability two random are different species)
  Species-area relationship: S = cA^z  (z ≈ 0.25-0.30 for island biogeography)
```

---

## Island Biogeography

```
MacARTHUR-WILSON THEORY (1963, 1967):
  Species richness on islands = equilibrium between immigration and extinction
  Turnover: species composition changes even as number stays constant

                    Immigration rate (I)
                    from mainland
         │\
         │  \   ← large island (lower extinction)
         │    \
  Rate   │      \___
         │    I    X  ← equilibrium S* = immigration = extinction
         │  Extinction
         │  rate (E) ↗
         │_____________
              Species richness S
         0         S*         S_mainland

  Larger island: lower extinction rate → higher S*
  Nearer island: higher immigration rate → higher S*

  Predictions confirmed: oceanic islands, mountaintops, forest fragments, habitat patches

SPECIES-AREA RELATIONSHIP:
  S = cA^z      (power law, linearizes in log-log)
  z ≈ 0.20-0.35 for oceanic islands
  z ≈ 0.12-0.17 for continental samples (less isolated)
  c: depends on taxon and region

MINIMUM VIABLE POPULATION (MVP):
  Smallest population with >95% probability of persisting 100 years
  Accounts for: demographic stochasticity, environmental stochasticity, genetic drift
  Rule of thumb: ~1000 individuals (varies greatly by species)

SLOSS DEBATE (Single Large Or Several Small):
  Single large reserve vs many small with same total area?
  Current consensus: depends on species — edge effects, connectivity important
  Corridors can link fragmented habitats (meta-population connection)
```

---

## Biogeochemical Cycles

```
CARBON CYCLE
  Atmospheric reservoir: ~870 GtC (as CO₂ ~420 ppm in 2024)
  Terrestrial vegetation: ~560 GtC
  Soil organic matter: ~1500 GtC  (largest terrestrial reservoir)
  Ocean: ~38,000 GtC  (dissolved, organic, carbonate)
  Sedimentary rock: ~60,000,000 GtC  (geological timescale)

  Fluxes:
    Photosynthesis: CO₂ → organic carbon (−119 GtC/yr gross)
    Respiration:    organic C → CO₂ (+119 GtC/yr)
    Net primary prod: ~60 GtC/yr to organic matter
    Ocean uptake:   ~2.5 GtC/yr anthropogenic CO₂
    Land uptake:    ~3 GtC/yr
    Fossil fuel + deforestation: +11.5 GtC/yr (2020s)
    → Net atmospheric increase: ~5 GtC/yr (+2.5 ppm CO₂/yr)

NITROGEN CYCLE
  Atmosphere: 78% N₂ (not bioavailable — triple bond requires breaking)

  Fixation pathways:
    Biological: Rhizobium (legume root nodules), free-living Azotobacter, cyanobacteria
    Industrial: Haber-Bosch process (N₂ + H₂ → NH₃, 150 atm, 450°C, Fe catalyst)
    Lightning: small amount (<2% of total)

  Key steps:
    N₂ →(fixation)→ NH₄⁺ →(nitrification)→ NO₂⁻ →(nitrification)→ NO₃⁻
    NO₃⁻ →(denitrification, anoxic)→ N₂O → N₂   (back to atmosphere)
    NO₃⁻ →(plant/microbial assimilation)→ organic N →(mineralization)→ NH₄⁺

  Problem: Haber-Bosch doubled N inputs to terrestrial ecosystems
    → eutrophication, dead zones, N₂O (310× GWP of CO₂)

PHOSPHORUS CYCLE
  No gaseous phase (unlike C and N)
  Weathering-limited: P enters from rock weathering (geological timescale)
  Limiting nutrient in freshwater systems (vs N limiting in marine)
  Mycorrhizae key in P uptake for plants
  Agriculture: P mining from rock phosphate (non-renewable on human timescales)
    → eutrophication from runoff

WATER CYCLE
  Evapotranspiration: plants return ~50% of terrestrial precipitation to atmosphere
  Transpiration cooling: forests lower local temperatures by 2-8°C
  Deforestation → reduced transpiration → altered rainfall patterns
  Example: Amazon dieback could shift rainfall to SE Brazil (La Plata watershed)
```

---

## Biomes

```
TERRESTRIAL BIOMES — Temperature and Precipitation Determine Biome Type

       Tropical      Temperate     Boreal      Tundra      Desert
       Rainforest    Deciduous     (Taiga)
       ─────────────────────────────────────────────────────────────
Temp   25-30°C       5-20°C       −10 to 5°C  −20 to 5°C  >30 to −20°C
Precip 200-400 cm    75-150 cm    30-85 cm    <25 cm      <25 cm
NPP    Highest       Moderate     Low         Very low    Very low
Area   ~12%          ~10%         ~17%        ~8%         ~26%
       land          land         land        land        land

Tropical Rainforest:
  ~50% of all species (vast biodiversity)
  Closed nutrient cycle: nutrients in living biomass, not soil
  Deforestation → nutrient flush then barren soil

Boreal (Taiga):
  Largest biome by area
  Dominated by conifers (Picea, Abies, Pinus) — needles resist freezing/desiccation
  Permafrost: stores ~1500 GtC of frozen organic matter
    Thawing → CH₄ and CO₂ release (positive feedback to climate change)

AQUATIC BIOMES:
  Marine (71% of Earth surface):
    Photic zone: 0-200 m (light penetrates, photosynthesis)
    Aphotic zone: >200 m (darkness, ~95% of ocean volume)
    Mesopelagic (200-1000 m): biological pump — sinking particles
    Hadal zone: trenches >6000 m

  Upwelling zones: deep cold nutrient-rich water rises → high productivity
    Eastern boundary currents (California, Peru/Humboldt, Benguela, Canary)
    El Niño suppresses upwelling → collapse of anchovy fisheries (Peru)

  Coral reefs:
    "Rainforests of the sea" — <0.1% of ocean but ~25% of marine species
    Depend on zooxanthellae (symbiotic algae in coral polyps)
    Bleaching: thermal stress → zooxanthellae expelled → coral dies
    1°C above normal for 8+ weeks → mass bleaching events
    2016: ~50% of Great Barrier Reef bleached (worst on record)
    Ocean acidification: CO₂ + H₂O → carbonic acid → [CO₃²⁻] drops → aragonite saturation
      pH from 8.2 to 8.1 since industrial revolution = 26% increase in [H⁺]

  Freshwater:
    Lakes: thermocline separates warm epilimnion from cold hypolimnion
    Eutrophication: nutrient loading (N + P) → algal blooms → O₂ depletion → hypoxia → dead zones
    Lake Erie: restored from eutrophication 1970s-1980s (Clean Water Act) → re-eutrophication 2010s
```

---

## Conservation Biology

```
BIODIVERSITY LOSS — THE SIXTH MASS EXTINCTION
  Background extinction rate: ~1 species per million species-years
  Current rate: 100-1000× background (estimates based on habitat loss + direct obs)
  Leading causes: Habitat destruction (by far #1), overexploitation, invasive species,
                  pollution, climate change (increasing importance)
  Amphibians most threatened (~40% species threatened)

HABITAT FRAGMENTATION:
  Creates edge effects: different microclimate, predation pressure, invasive species
  Reduces patch size → smaller populations → extinction debt (future extinctions guaranteed)
  Corridors can mitigate: wildlife crossings, riparian buffers, forest strips

INVASIVE SPECIES:
  Characteristics of successful invaders: fast growth, high reproductive rate,
    broad niche, phenotypic plasticity, human-commensal
  Island ecosystems most vulnerable (evolved in absence of mainland predators)
  Classic disasters: rats → seabird extinctions globally; Nile perch → 200+ cichlid
    extinctions in Lake Victoria; chestnut blight → elimination of American chestnut

PLANETARY BOUNDARIES (Rockström et al. 2009, updated 2023):
  9 Earth system boundaries; crossing → risk of crossing into new planetary state

  Boundary                    Pre-industrial  2023 Status
  ───────────────────────────────────────────────────────
  Climate change (CO₂ ppm)    280            421 ⚠️ BREACHED
  Biosphere integrity (BII%)  >90%           ~80% 🔴 BREACHED
  Biogeochemical flows (P)    ~1 TgP/yr      22 TgP/yr 🔴 BREACHED
  Biogeochemical flows (N)    ~62 TgN/yr     ~190 TgN/yr 🔴 BREACHED
  Land-system change (forest) >75% remaining 60% remaining ⚠️ BREACHED
  Freshwater use (km³/yr)     ~415           ~2600 🔴 BREACHED (blue water)
  Ocean acidification (Ω_a)   2.7-3.3        2.8 (marginal zone)
  Stratospheric ozone         277-280 DU      293 DU (recovering)
  Novel entities (plastic,    0               exceeded definition 🔴
    synthetic chemicals)
  Aerosol loading             regional        regionally breached

  "Safe operating space for humanity": all 9 in green zone
  Current reality: 6 of 9 breached as of 2023 paper (Richardson et al.)

ECOSYSTEM SERVICES:
  Provisioning: food, water, fiber, fuel, medicines, genetic resources
  Regulating: climate regulation, flood control, water purification, disease control
  Cultural: recreation, spiritual, aesthetic, educational
  Supporting: nutrient cycling, soil formation, primary production (underpins others)

  Natural capital accounting: including ecosystem services in GDP calculations
  TEEB (The Economics of Ecosystems and Biodiversity): global initiative
  Global ecosystem services estimated at $125-145 trillion/yr (vs global GDP ~$100T)
```

---

## Ecological Applications and Climate Change

```
CLIMATE CHANGE ECOLOGY:
  Range shifts: species tracking their climatic niche poleward + upslope
    Average shift: +16.9 km/decade poleward, +11.0 m/decade upslope (Parmesan & Yohe 2003)
    Mismatch problem: different species shift at different rates → phenological mismatch

  Phenological mismatch:
    Spring ephemerals blooming before pollinators arrive (or vice versa)
    Great tit chick timing vs peak caterpillar timing (Visser et al., Netherlands)
    → reproductive fitness declines when phenology decouples

  Trophic mismatch (Match-Mismatch Hypothesis, Cushing 1990):
    Larval fish abundance must match zooplankton peak → recruitment success
    Climate shifts plankton timing → fishery collapse

  Coral bleaching projection:
    2°C warming → annual bleaching events for most coral reefs by 2050s
    Functional extinction of coral reefs at >2°C above pre-industrial

FISHERIES ECOLOGY:
  Maximum sustainable yield (MSY): harvest at K/2 theoretically
  B_MSY = K/2, F_MSY = r/2 (fishing mortality at MSY)
  Reality: single-species MSY ignores ecosystem interactions
  Ecosystem-Based Fishery Management (EBFM): accounts for food web

  Stock collapse:
    Classic: North Atlantic cod collapse 1992 (from ~2Mt to <100kt)
    Caused by overfishing below B_MSY for years → depensation (Allee effect at low density)
    Still not recovered 30+ years later

RESTORATION ECOLOGY:
  Active: reintroduce species, replant vegetation, alter hydrology
  Passive (natural regeneration): remove stressor, let ecosystem recover
  Reference ecosystem: target state for restoration
  Novel ecosystems: ecosystems with no historical analog (climate change creating new combos)

  Rewilding: large-scale restoration with minimal management
    Reintroduce apex predators → trophic cascade → ecosystem reorganization
    Yellowstone wolves (1995): willows, beavers, streamflow patterns changed in 10 years
    (Some evidence contested — complexity of real ecosystems vs idealized cascade)
```

---

## Decision Cheat Sheet

| Question | Concept | Key Equation/Rule |
|----------|---------|-------------------|
| Why is population growing exponentially? | Unlimited resources, dN/dt = rN | J-curve |
| Why does growth plateau? | Carrying capacity K | Logistic: dN/dt = rN(K-N)/K |
| Why do predator-prey populations cycle? | Lotka-Volterra oscillations | ¼-period lag |
| Can two identical species coexist? | Competitive exclusion | No — one excludes other |
| How many species on island? | Island biogeography equilibrium | Larger+closer → more species |
| What limits primary productivity? | Nutrient or light colimitation | N in ocean, P in freshwater |
| What trophic level should I eat? | 10% energy transfer rule | Each level = 10x more land |
| What drives succession? | Facilitation, tolerance, inhibition | Primary (bare rock) vs secondary (soil intact) |
| Why are coral reefs bleaching? | Thermal stress → lose zooxanthellae | >1°C above normal |
| How to measure biodiversity? | Shannon H', species-area S=cA^z | α/β/γ diversity levels |
| Is this ecosystem at planetary boundary? | Rockström framework | 6 of 9 boundaries currently breached |

---

## Common Confusion Points

**r vs K selection is a simplification**: The original Pianka (1970) r-K spectrum is useful intuition but modern life history theory replaces it with multiple axes (pace of life, reproductive investment, adult vs juvenile survival). Don't use r-K as a rigid theory.

**Competitive exclusion vs coexistence**: In nature, many similar species coexist. This is because real niches have more dimensions than simple models. Niche differentiation, spatial/temporal heterogeneity, and non-equilibrium dynamics all permit coexistence.

**10% rule is an average**: Efficiency varies from 5-30%. Ectotherms transfer more efficiently than endotherms (less energy to heat). Aquatic systems often more efficient than terrestrial.

**Keystone species ≠ dominant species**: Keystone species have disproportionate impact relative to their biomass. Dominant species are simply abundant. Not all top predators are keystone species.

**Eutrophication vs productivity**: High nutrient inputs → algal blooms → O₂ consumption by decomposers → hypoxia → "dead zone." System is highly productive but ecologically degraded.

**Island biogeography applies to habitat patches**: Forest fragments, mountain tops, and lake systems follow the same species-area relationship as ocean islands. Conservation implication: large reserves + corridors.

**Lotka-Volterra predicts neutral cycles**: Real predator-prey systems are damped (not neutral) due to prey behavior, environmental heterogeneity, and multiple prey species. L-V is a starting model, not a complete description.
