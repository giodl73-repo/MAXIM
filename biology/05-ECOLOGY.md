# 05 — Ecology

## Population Dynamics, Species Interactions, Community Ecology, Biogeochemical Cycles

---

## Big Picture

```
ECOLOGY: How organisms interact with each other and their environment

SCALE HIERARCHY:
  Individual → Population → Community → Ecosystem → Biosphere

CORE PROBLEMS:
  Population:   Why do numbers change? What limits growth?
  Community:    Which species coexist? What determines biodiversity?
  Ecosystem:    How does energy flow? How do nutrients cycle?
  Biosphere:    What are the planetary consequences of living systems?

TWO CURRENCIES OF ECOLOGY:
  Energy: flows through ecosystems (enters via photosynthesis, lost as heat)
  Nutrients: cycle within ecosystems (recycled by decomposers)
  → Energy is a one-way flow; matter cycles

ECOLOGY ↔ EVOLUTION FEEDBACK:
  Ecology sets selection pressures (who survives, who reproduces)
  Evolution changes organisms (traits, life histories)
  Eco-evolutionary dynamics: evolution can happen fast enough to affect ecology
  Example: rapid evolution of prey defense when predator introduced
```

---

## Engineering Bridges

```
ECOLOGY ←→ SYSTEMS ARCHITECTURE

Carrying capacity K = autoscaling ceiling enforced by resource constraints
  dN/dt = rN(K-N)/K: growth decelerates as utilization approaches capacity
  Unlike autoscaling, K is not configurable — it's set by food, space, predators
  Allee effects: positive feedback at low density — below threshold, population collapses
  → Analogous to minimum viable traffic for a service to stay warm/healthy

Predator-prey (Lotka-Volterra) = load balancer oscillation
  Prey = requests; predator = processing capacity
  More prey → predator grows → prey suppressed → predator starves → prey recovers
  Neutrally stable cycles in the basic model (like undamped LC circuit oscillation)
  Real systems: damped or limit cycles — additional feedback terms (prey refuge,
    prey switching) add damping
  → Same math as SIR epidemiological model: dS/dt, dI/dt, dR/dt

Food web = directed dependency graph with energy as the flow metric
  Nodes: species; edges: trophic interactions (who eats whom)
  Connectance C = L/S² (link density); empirical food webs: C ≈ 0.05-0.15
  Stability: May (1972) showed random networks destabilize with more connections
  Real food webs stable via: compartmentalization (modules), weak links (damping),
    asymmetric interaction strengths
  → Parallels: microservice dependency graph; weak coupling = stable architecture

Keystone species = single point of failure (SPOF) in ecosystem architecture
  Pisaster sea star (<1% of intertidal biomass) → remove → 15 species lost → mussel monoculture
  Keystone identifies fragility in the dependency graph that biomass alone doesn't reveal
  → Like identifying critical path nodes in a distributed system

Trophic cascade = indirect effects propagating through the dependency graph
  Wolves (added) → elk (suppressed) → willows (recovered) → beavers (returned) → hydrology (changed)
  n-hop indirect effects dominate; direct effects are the minority of ecological impact
  → Like a service outage propagating through a dependency chain
```

## Population Ecology

```
DEMOGRAPHIC EQUATION:
  ΔN = B − D + I − E   (Births − Deaths + Immigration − Emigration)
  In closed population: dN/dt = (b − d)N = rN

EXPONENTIAL GROWTH:
  dN/dt = rN,   N(t) = N₀eʳᵗ
  r = intrinsic rate of increase (b − d)
  J-shaped curve; requires unlimited resources
  Human population: ~1% per year currently; was ~2% peak 1960s

LOGISTIC GROWTH:
  dN/dt = rN · (K − N)/K
  K = carrying capacity (resources set ceiling)
  Inflection at N = K/2 (maximum growth rate)
  S-shaped curve: fast growth → decelerate → plateau at K

  Deviations from logistic:
    Allee effects: positive density-dependence at low N (need mates, group defense)
      → population decline below critical density → extinction vortex
    Depensation: low population → reduced survival (inverse of logistic at low N)
    Key for conservation: small populations may not recover even after threats removed

AGE STRUCTURE (Leslie Matrix):
  n(t+1) = L · n(t)
  L contains age-specific survival and fecundity
  Dominant eigenvalue λ₁: finite rate of population change
    λ > 1: growing; λ < 1: declining; λ = 1: stable
  Stable age distribution: reached regardless of initial age distribution

LIFE HISTORY THEORY:
  Trade-offs: resources are finite → investment in reproduction vs survival vs growth
  Pace of life:
    Fast: small body, high fecundity, short lifespan, high juvenile mortality (mice, weeds)
    Slow: large body, low fecundity, long lifespan, high adult survival (elephants, trees)
  Bet-hedging: variable environments → spread reproductive investment across time
  Semelparity (one reproductive episode): Pacific salmon, bamboo, century plant
  Iteroparity (repeated reproduction): most vertebrates, perennial plants
```

---

## Species Interactions

```
COMPETITION (−/−):
  Interspecific: between species for shared limiting resource
  Intraspecific: within species (often stronger driver of population regulation)
  Competitive exclusion (Gause): identical niches → one species wins
  Niche partitioning: coexistence via resource/habitat differentiation

PREDATION AND HERBIVORY (+/−):
  Lotka-Volterra predator-prey cycles:
    dV/dt = rV − aVP     (prey: grow minus eaten)
    dP/dt = bVP − mP     (predator: grow from prey minus die)
  Neutrally stable oscillations; prey peaks before predator by ~¼ cycle
  Real systems: more complex (prey refuges, prey switching, plant quality feedback)

MUTUALISM (+/+):
  Obligate: neither survives alone (yucca moth, fig wasp, mycorrhizae)
  Facultative: beneficial but not required (most pollination)
  Mycorrhizal networks: fungal hyphae ↔ plant roots
    AMF (arbuscular): in ~80% of plant species
    ECM (ectomycorrhizal): trees (oaks, pines, birches)

PARASITISM (+/−):
  Macroparasites (helminths): aggregate distribution (negative binomial)
    20% of hosts carry 80% of parasites (heterogeneous exposure + immune response)
  Microparasites (pathogens): SIR model (Susceptible-Infected-Recovered)
    R₀ = βN/γ (basic reproduction number)
    Epidemic threshold: R₀ > 1 for spread; herd immunity at 1 − 1/R₀ vaccinated

TROPHIC CASCADES:
  Top-down regulation: predator → prey → plants (indirect positive effect on plants)
  Classic: sea otters → sea urchins → kelp forests
  Wolves in Yellowstone → elk behavior changes → willows/beavers → stream hydrology
  Loss of apex predators → trophic downgrading (Terborgh & Estes)

KEYSTONE SPECIES (Paine, 1966):
  Disproportionately large effect relative to biomass
  Remove → community restructures drastically
  Pisaster sea star: removed → mussels dominate → 15 fewer species
```

---

## Community Structure and Diversity

```
TROPHIC LEVELS AND ENERGY FLOW:
  Primary producers (1°): autotrophs (photosynthesis, chemosynthesis)
  Primary consumers (2°): herbivores
  Secondary consumers (3°): carnivores
  Decomposers: cross-cutting; break down dead organic matter → nutrient release

  10% rule: ~10% energy transferred between trophic levels (range 5-20%)
  → food chains usually < 5 levels long
  Primary productivity:
    GPP: total photosynthesis
    NPP = GPP − plant respiration (what's available to herbivores)
    Highest NPP: tropical rainforest (~2200 gC/m²/yr), estuaries, coral reefs

DIVERSITY METRICS:
  Species richness (S): count of species
  Shannon diversity: H' = −Σ pᵢ ln(pᵢ)  (accounts for evenness)
  Simpson: D = 1 − Σ pᵢ²               (probability two random individuals differ)
  α diversity: within-site diversity
  β diversity: turnover between sites (Whittaker: γ = α × β)
  γ diversity: total regional diversity

  Species-area relationship: S = cA^z  (z ≈ 0.25 continental; 0.30 islands)

INTERMEDIATE DISTURBANCE HYPOTHESIS:
  Maximum diversity at intermediate disturbance frequency
  Low disturbance → competitive exclusion; high disturbance → only disturbance specialists
  Empirical support: variable; modern view more nuanced (depends on productivity)

ECOLOGICAL SUCCESSION:
  Primary: bare substrate → community
    Glacier Bay: 250 years from bare rock → spruce-hemlock forest
    Pioneer species (moss, lichen) → shrubs → trees
  Secondary: after disturbance with soil intact; faster (decades)
  Facilitation: early species improve conditions for later ones
  Inhibition: early species suppress late successional species until die off
  Tolerance: later species tolerant of pioneer conditions

FOOD WEB STRUCTURE:
  Connectance C = L/S²  (L = links, S = species)
  Most empirical webs: C ≈ 0.05-0.15
  Complexity-stability paradox (May, 1972): random networks → instability with increasing S
  Real food webs stable due to: compartmentalization, weak links dampen oscillations,
    asymmetric interactions, adaptive foraging
```

---

## Biogeochemical Cycles

```
CARBON CYCLE:
  Input: photosynthesis (CO₂ → organic C)
  Output: respiration, decomposition (organic C → CO₂)
  Terrestrial net ecosystem production (NEP) = NPP − heterotrophic respiration
  Ocean carbon pump: biological (sinking organic matter) + solubility pump
  Anthropogenic: +11.5 GtC/yr (fossil fuels + deforestation)
    → CO₂ rising ~2.5 ppm/yr; 280 ppm (pre-industrial) → 421 ppm (2024)

NITROGEN CYCLE:
  Atmosphere: 78% N₂ (inert — strong triple bond)
  Biological N fixation: Rhizobium (legumes), free-living diazotrophs, cyanobacteria
  Haber-Bosch: industrial fixation (N₂ + 3H₂ → 2NH₃); doubled terrestrial N inputs
  Nitrification: NH₄⁺ → NO₃⁻  (Nitrosomonas, Nitrobacter; aerobic)
  Denitrification: NO₃⁻ → N₂O → N₂  (anaerobic sediments/soils)
  N₂O: potent greenhouse gas (298× CO₂ GWP over 100 yr); ozone-depleting

PHOSPHORUS CYCLE:
  No gaseous phase → cycling slower, less global
  Source: rock weathering (geological timescale input)
  Limiting nutrient: freshwater lakes (vs N in most marine systems)
  Agriculture: P mining from rock phosphate (non-renewable on human timescale)
  Eutrophication: P + N runoff → algal blooms → hypoxia → dead zones

BIOGEOCHEMICAL FEEDBACKS WITH CLIMATE:
  Permafrost thaw: ~1500 GtC frozen → release as CO₂ and CH₄ (positive feedback)
  Ocean acidification: CO₂ + H₂O → H₂CO₃ → HCO₃⁻ + H⁺
    Ocean pH fell 8.2 → 8.1 (0.1 units = 26% [H⁺] increase since ~1850)
    Affects calcification: coral, mollusks, pteropods (aragonite saturation)
  Boreal/tropical carbon:
    Amazon: on edge of tipping point (deforestation + drought → savannification)
    Boreal fires: increasing → CO₂ + black carbon on snow → albedo + forcing
```

---

## Conservation Ecology

```
BIODIVERSITY CRISIS:
  Current extinction rate: 100-1000× background rate
  Leading causes:
    1. Habitat destruction (most important by far — agricultural expansion)
    2. Overexploitation (hunting, fishing)
    3. Invasive species
    4. Pollution
    5. Climate change (rising rapidly in importance)

  Amphibians: ~40% threatened (chytrid fungus Batrachochytrium dendrobatidis)
  Mammals: ~25% threatened
  Insects: estimated 2.5-7% per decade decline (German windshield study)

EXTINCTION DEBT:
  Habitat loss guarantees future extinctions (time lag)
  Reason: species-area relationship (reduce area → reduce S)
  Habitat must reach new equilibrium — some species persist temporarily on "borrowed time"
  Estimate: already committed to 20-50% of species loss from current habitat loss

MINIMUM VIABLE POPULATION (MVP):
  Smallest population with >95% persistence for 100 years
  Rough guideline: 50 individuals (avoid inbreeding depression) / 500 (avoid drift)
    "50/500 rule" — often inadequate; many recommend 1000+
  Factors: demographic stochasticity, environmental stochasticity, genetic erosion

CONSERVATION GENETICS:
  Inbreeding depression: reduced fitness from mating with relatives
    Isle Royale wolves: moose predation collapse → inbred island population
    Florida panther: FIV, cardiac defects from <30 individuals → Texas cougar introduced
  Genetic rescue: introduce individuals from other populations → increased fitness
  Genetic diversity = evolutionary potential for future adaptation

ECOSYSTEM-BASED CONSERVATION:
  Protect keystone species → maintain ecosystem function
  Corridor design: connect habitat patches → maintain metapopulation dynamics
  Area-design: SLOSS debate (Single Large Or Several Small)
  Rewilding: reintroduce lost species (wolves to Yellowstone, aurochs proxies to Europe)
```

---

## Decision Cheat Sheet

| Question | Concept | Key Tool |
|----------|---------|----------|
| Why is population declining? | Limiting factors, vital rates | Life table, λ from Leslie matrix |
| Can two species coexist? | Lotka-Volterra, niche theory | Coexistence: intraspecific > interspecific competition |
| What's limiting primary production? | Nutrient colimitation | N in oceans; P in freshwater |
| Why is biodiversity high here? | Intermediate disturbance, species-area | S = cA^z; IDH |
| How much energy reaches top predator? | 10% rule | 10^(trophic levels) less than primary production |
| Is this community food web stable? | Connectance, interaction strength | Weak links stabilize; compartmentalization |
| What drives nutrient limitation? | Biogeochemical cycling | N: fixation/denitrification; P: weathering only |
| How to size a nature reserve? | SLOSS + MVP + island biogeography | Large preferred; corridor connectivity crucial |
| What happens when predator removed? | Trophic cascade | Bottom-up release of prey → potential overgrazing |
| Is this habitat patch enough? | Metapopulation viability | Patch occupancy model; extinction-recolonization balance |

---

## Common Confusion Points

**K (carrying capacity) is not fixed**: K varies with resource availability, climate, and other species in the community. It's a model parameter useful for intuition, not a constant of nature.

**Competitive exclusion in theory vs reality**: The principle applies to species with truly identical niches — which rarely exist. Species coexist through niche differentiation, spatial/temporal variation, non-equilibrium dynamics, and predation preventing dominance.

**Trophic cascades are real but complex**: Wolves to willows is a real cascade but simpler than often portrayed. Multiple factors simultaneously affect vegetation. Don't oversimplify trophic cascades to linear chains.

**10% rule is a rough average**: Trophic transfer efficiency ranges from 5% to ~30%. Ectotherms (fish) can be 20%. Endotherms (birds, mammals) are much less efficient (most energy goes to thermoregulation). Deep sea can be lower.

**Biodiversity ≠ biomass**: Tropical rainforests have highest species diversity but are NOT the most productive per area for all groups. Estuaries and coral reefs are highly productive but have less total diversity than tropical forests.

**Eutrophication is not just "too many nutrients"**: N + P → algal bloom → algal death → bacterial decomposition → O₂ consumption → hypoxia → dead zone. The damage is anoxia, not nutrients per se. P is often the limiting nutrient in freshwater; removing P reverses eutrophication.
