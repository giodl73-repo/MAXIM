# Ecology, Niches, and Trophic Roles

## The Big Picture

Ecological niche theory is the framework for understanding how species partition resources and coexist (or fail to). Hutchinson's hypervolume niche formalization, Lotka-Volterra competition models, and food web theory together describe how energy flows through ecosystems and why particular species combinations are stable. Zoology contributes the animal components — primary and secondary consumers, apex predators, scavengers — to these frameworks.

```
ECOLOGICAL HIERARCHY
======================

  INDIVIDUAL:      foraging, behavior, physiological tolerance
       |
  POPULATION:      birth/death rates, density dependence, age structure
       |
  COMMUNITY:       species interactions, competition, predation, mutualism
       |
  ECOSYSTEM:       energy flow, nutrient cycling, trophic structure
       |
  BIOSPHERE:       global patterns; macroecology; biogeography

  Animal ecology spans all levels but particularly focuses on:
    - Species interactions (competition, predation, coevolution)
    - Food web topology (who eats whom)
    - Population regulation (density dependence, predator-prey dynamics)
    - Trophic cascades (indirect effects through food chains)
```

---

## The Niche Concept

### Hutchinson's Hypervolume

```
HUTCHINSON'S NICHE DEFINITION (1957)
=======================================

N-DIMENSIONAL HYPERVOLUME:
  For each environmental variable (temperature, humidity, food size, pH...)
  species has a tolerance range.
  NICHE = n-dimensional hypervolume defined by all tolerance ranges simultaneously

  Example: salt marsh sparrow niche
    Dimension 1: temperature [5-30 C]
    Dimension 2: salinity [0-15 ppt]
    Dimension 3: vegetation height [20-80 cm]
    Dimension 4: invertebrate prey size [3-20mm]
    ...
  N-dimensional volume = fundamental niche

FUNDAMENTAL vs REALIZED NICHE:
  Fundamental: all conditions where species CAN survive/reproduce
  Realized: conditions where it ACTUALLY lives (constrained by competition)
  Realized < Fundamental (competition pushes species out of parts of fundamental niche)
  Remove competitor: realized expands toward fundamental
    (competitive release: species fills more habitat when competitor removed)

COMPETITIVE EXCLUSION PRINCIPLE (Gause 1934):
  Two species with IDENTICAL niches cannot coexist indefinitely
  -> "Complete competitors" cannot coexist
  One must outcompete the other OR niches must differ
  (Mathematical basis: Lotka-Volterra competition model)
```

### Niche Differentiation and Coexistence

```
NICHE DIFFERENTIATION MECHANISMS
====================================

FOR COEXISTENCE (modern coexistence theory, Chesson 2000):
  Equalizing mechanisms: reduce fitness differences between species
  Stabilizing mechanisms: promote return to equilibrium when disturbed
  REQUIRED: intraspecific competition > interspecific competition
    (each species limits itself more than it limits competitors)

RESOURCE PARTITIONING:
  Species use different subsets of available resources
  MacArthur's warblers (1958): vertical foraging zone partitioning
  Character displacement: competing species evolve to minimize overlap
    Galapagos finch beak: size distribution bimodal in sympatry;
    unimodal in allopatry -> competition drives divergence

TEMPORAL PARTITIONING:
  Activity time differences: diurnal vs nocturnal
    Hawk by day; owl by night -> same prey; temporal partition
  Seasonal differences: spring vs summer breeders

CHARACTER DISPLACEMENT:
  Sticklebacks in lakes with both Gasterosteus species:
    Limnetic species: smaller mouth; feeds on plankton
    Benthic species: larger mouth; feeds on benthic invertebrates
    Single-species lakes: intermediate mouth morphology
  -> Competition drives morphological divergence and ecological specialization
```

---

## Food Webs: Structure and Function

```
FOOD WEB CONCEPTS
==================

TROPHIC LEVELS:
  Level 1: Primary producers (plants, algae, cyanobacteria)
  Level 2: Primary consumers (herbivores; eat producers)
  Level 3: Secondary consumers (eat herbivores)
  Level 4: Tertiary consumers (eat secondary consumers)
  Apex predators: top of food chain; no predators

TROPHIC EFFICIENCY:
  ~10% energy transferred per trophic level (range: 5-20%)
  -> 1000 kg plants -> 100 kg herbivores -> 10 kg secondary consumers
  CONSEQUENCE: food chains rarely exceed 4-5 levels (insufficient energy)
  Long food chains: marine (more efficient production + low respiration rate)
  Short food chains: terrestrial (high plant respiration cost)

  WHY 10% EFFICIENCY?
  ~40% of ingested energy: not assimilated (feces)
  ~50% of assimilated: respiration (cellular metabolism)
  ~10%: growth + reproduction (available to next trophic level)

FOOD WEB METRICS:
  Connectance: proportion of possible links realized
    Real food webs: ~5-15% connectance (not all possible predator-prey pairs exist)
  Link density: average links per species
  Trophic level: calculated (not integer; omnivory common)
  Keystone species: disproportionate impact relative to biomass
```

### Food Web Topology

```
FOOD WEB TYPES
================

SIMPLE FOOD CHAIN:
  Grass -> rabbit -> fox -> (nothing eats fox)
  Assumes: one species per trophic level; no omnivory; linear

REAL FOOD WEBS:
  Omnivory: species feed at multiple trophic levels (bears, pigs, humans)
  Trophic loops: A eats B; B eats A (rare but documented in some plankton)
  Ontogenetic diet shifts: juvenile fish = prey; adult fish = predator
    (predator-prey relationship inverts over development)
  Parasites + parasitoids: largely excluded from classic food web models
    (including them roughly doubles apparent web complexity)

CASCADE MODEL (Cohen & Newman 1985):
  Species can eat any species with lower "niche value"
  Generates realistic food web statistics
  Better: allometric constraints (predators eat prey smaller than themselves)

NETWORK ANALYSIS APPLIED TO FOOD WEBS:
  Degree distribution: power law in some webs (scale-free)
  Modularity: groups of strongly interacting species (compartments)
  Keystone: nodes whose removal causes disproportionate restructuring
```

---

## Predator-Prey Dynamics

```
LOTKA-VOLTERRA PREDATOR-PREY MODEL
=====================================

EQUATIONS:
  dH/dt = rH - aHP     [Prey: grow (r) minus predation (a*P)]
  dP/dt = b*aHP - qP   [Predator: grow from prey (b*a*H) minus die (q)]

  H = prey density; P = predator density
  r = prey intrinsic growth rate
  a = predation rate (attack efficiency)
  b = conversion efficiency (prey -> predator)
  q = predator mortality rate

PREDICTION: NEUTRAL CYCLES
  Both populations oscillate indefinitely
  Predator peak follows prey peak by 1/4 cycle
  Neutrally stable (zero eigenvalues) -> marginal stability

REAL EXAMPLE: Hare-Lynx cycle (Hudson's Bay Company fur records)
  10-year cycle; lynx follows hare by ~1-2 years
  NOT pure Lotka-Volterra: food plant also cycles
    -> 3-trophic-level interaction (plant-hare-lynx)
  + Hare shows cycle even on islands without lynx
  -> BOTH predation AND food (bottom-up + top-down) drive cycle

MODIFIED MODELS:
  Prey logistic growth: ceiling on prey (K); damps cycles -> convergence to equilibrium
  Functional response: predation rate saturates at high prey density
    Type II (hyperbolic): c = aH/(1+ahH); saturation by handling time
    Type III (sigmoid): c = aH^2/(1+ahH^2); prey switching; stabilizing
  Refugia: fraction of prey inaccessible -> stabilizes (Nicholson-Bailey)
```

---

## Trophic Cascades

```
TROPHIC CASCADES
=================

DEFINITION: Effect of predator abundance propagates DOWN the food chain
  Top-down effect: predator reduces prey -> prey's prey increases
  (alternating positive/negative effects at successive levels)

THREE-LEVEL CASCADE (Hairston, Smith, Slobodkin 1960 "Green World Hypothesis"):
  WHY IS THE WORLD GREEN?
    Predators keep herbivores in check
    -> Herbivores don't eat all plants
    -> World stays green
  Evidence: remove predators -> herbivore outbreak -> plant overgrazing
  Experimental: Isle Royale wolves + moose + birch (partial evidence)

CLASSIC CASES:

SEA OTTER (Enhydra lutris) -- kelp forest:
  Sea otters eat sea urchins
  Remove sea otters (fur trade + killer whale predation):
    Urchin population explodes
    Urchins overgraze kelp -> "urchin barrens"
    All kelp-dependent species disappear
  Restore sea otters:
    Urchin population suppressed
    Kelp forests recover
    Marine biodiversity recovers
  RESULT: sea otter = keystone predator; cascade extends 3 levels

WOLVES IN YELLOWSTONE:
  Wolf reintroduction (1995): 41 wolves from Canada
  Effects:
    Elk: reduced in density; behavior changed (avoid valleys + streams)
    Willows + aspen: recovery in stream banks (no more elk browsing)
    Beavers: returned to valleys (willow habitat)
    Songbirds: returned (willow nesting habitat)
    Fish: improved (stream bank shade + structure)
    Bears: benefited from wolf kills (carrion + berry access)
  "Trophic cascade" + "landscape of fear" (behaviorally-mediated cascade)
  Debate: cascade magnitude may be exaggerated (Kauffman 2010)
    -> effect real but not as dramatic as initial reports

SHARKS AND MESOPREDATORS:
  Shark decline (~90% in N. Atlantic, overfishing):
    Cownose rays: primary prey of sharks -> population explosion
    Rays eat bay scallops + clams
    Scallop fishery collapse in North Carolina (2004 documented)
  RESULT: removal of apex predator -> mesopredator release -> prey collapse
```

---

## Keystone Species

```
KEYSTONE SPECIES CONCEPT (Paine 1969)
=======================================

DEFINITION: Species with ecological impact disproportionate to biomass
  Remove the keystone: dramatic change in community structure
  (vs "dominant" species: important because of large biomass)

PAINE'S EXPERIMENT:
  Rocky intertidal; ochre sea star (Pisaster ochraceus) removed from plots
  Result: mussels (Mytilus) dominated entire area within 1 year
          15 species -> 8 species; homogeneous community
  Pisaster (small biomass): kept mussels in check
              -> allowed diverse community with algae, barnacles, limpets, whelks

KEYSTONE SPECIES TYPES:
  Predator: Pisaster, sea otter, wolf (above)
  Engineer: elephants (knock down trees -> create habitat); beavers (dam)
  Mutualist: fig trees (figs + fig wasps; if figs gone, ~30% tropical species gone)
  Disperser: large frugivores (hornbills, tapirs, elephants) for large-fruited trees

KEYSTONE CONCEPT PROBLEMS:
  Not every species is a keystone
  Identifying keystones requires removal experiments (often unethical)
  "Keystone" applied loosely in popular conservation discourse
  Better metric: "interaction strength" (net per capita effect on community)
```

---

## Niche Theory and Community Assembly

```
COMMUNITY ASSEMBLY RULES
===========================

ASSEMBLY RULES (Diamond 1975):
  Not all species combinations occur; some are "forbidden"
  Competitive exclusion limits co-occurrence of ecologically similar species
  Evidence from island bird surveys: assembly not random

NEUTRAL THEORY (Hubbell 2001):
  Radical null: species ecologically equivalent
  Community = random walk of birth, death, immigration, speciation
  Explains species-abundance distributions without niche differentiation
  Challenge: real communities show niche differentiation (evidence above)
  Modern view: neutral + niche mechanisms both operate; proportion varies

METACOMMUNITY THEORY:
  Community = local + regional (dispersal among patches)
  Species sorting: local community filtered by environment
  Patch dynamics: disturbance + colonization
  Mass effects: immigration maintains sink populations
  Neutral: dispersal-limited random assembly

SPECIES ABUNDANCE DISTRIBUTIONS:
  Most communities: many rare species + few abundant species
  Preston (1948): log-normal distribution fits well
  Broken stick model (MacArthur 1957): resource partitioning explains
  Neutral theory: reproduces log-normal without niches
  -> Both niche and neutral can produce same pattern; not a discriminating test
```

---

## Zoological Roles in Ecosystems

```
FUNCTIONAL ROLES OF ANIMALS IN ECOSYSTEMS
===========================================

PRIMARY CONSUMERS (herbivores):
  Transfer plant production to higher trophic levels
  ~10% efficiency; most plant production goes to decomposers, not herbivores
  Regulate plant community: grazing prevents competitive dominance
  Examples: ungulates, insects, zooplankton

SECONDARY CONSUMERS (carnivores):
  Population regulation of herbivores
  Energy integration: connect spatially dispersed prey populations
  Examples: insectivores (birds, bats); piscivores; small mammal predators

APEX PREDATORS:
  Trophic cascade effects (above)
  Landscape of fear: behavioral effects on prey (spatial + temporal)
  Prey population regulation: often not via direct killing rate
    -> indirect behavioral suppression is important

DECOMPOSERS:
  Break down organic matter into inorganic nutrients
  Mainly: bacteria + fungi (not animals)
  Animal decomposers (detritivores):
    Earthworms: soil mixing + fragmentation
    Dung beetles: dung processing + nitrogen release
    Vultures: rapid carcass removal (prevent disease spread)
    Blowfly larvae: carcass processing (see forensic entomology)

NUTRIENT CYCLING ROLES:
  Salmon (Pacific): transport marine N + P to freshwater + terrestrial
    Salmon carcasses: 80% of streamside forest N from salmon (Alaska)
    Grizzly bears: distribute salmon into forest (150m from stream)
  Whales: "whale pump" -- deep feeding + surface defecation
    -> bring nutrients from deep to photic zone
  Migratory birds: transport nutrients between ecosystems
```

---

## Decision Cheat Sheet

| Concept | Mathematical core | Classic example |
|---------|------------------|-----------------|
| Niche hypervolume | n-dimensional tolerance space | Hutchinson (1957) |
| Competitive exclusion | Same niche = cannot coexist | Gause's Paramecium |
| Trophic efficiency | ~10% energy transfer per level | 1000kg plant -> 100kg herbivore -> 10kg carnivore |
| Lotka-Volterra predator-prey | dH/dt = rH - aHP; dP/dt = bHP - qP | Hare-lynx cycle |
| Trophic cascade | Apex predator removal -> herbivore explosion -> plant collapse | Sea otter + urchin + kelp |
| Keystone species | Disproportionate impact relative to biomass | Pisaster + mussel + algae diversity |

---

## Common Confusion Points

**"10% efficiency" is an average**: Trophic efficiency varies from ~5% (warm-blooded endotherm predators) to ~20% (ectotherm predators, some marine systems). The 10% rule is a useful heuristic but not a physical constant.

**Food chains vs food webs**: A food chain (grass -> rabbit -> fox) is a linear simplification. Real food webs have many omnivores and cross-connections. Most ecological dynamics require web-level thinking. Food chain length predictions (based on energetic constraints) hold approximately but are complicated by omnivory.

**Competitive exclusion is a mathematical result with empirical support**: Gause's lab result (two Paramecium species couldn't coexist on single resource) is clean. In the field, coexistence of similar species is common. Modern coexistence theory explains: stabilizing mechanisms (density-dependence) allow coexistence even with some niche overlap.

**Trophic cascades are not always dramatic**: The Yellowstone wolf example is real but its magnitude may have been exaggerated in the popular press. Other trophic cascades (sea otter + urchin) are well-documented and strong. Cascade strength varies with: system type (marine > terrestrial), food chain length, prey behavior.

**"Keystone species" is overused in conservation**: Every charismatic species tends to get labeled a keystone. The technical definition requires disproportionate impact relative to biomass, demonstrated by removal or manipulation. Many "keystone" claims lack this experimental support. "Umbrella species" (large range; protects many others if protected) and "keystone species" are different concepts.
