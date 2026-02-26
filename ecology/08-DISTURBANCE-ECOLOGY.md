# Disturbance Ecology — IDH, Fire Ecology, Invasive Species

## The Big Picture

Disturbance — any event that disrupts ecosystem structure and releases resources — was once viewed as purely destructive. The modern view: disturbance is a fundamental driver of biodiversity and community composition. Many ecosystems are maintained *by* disturbance (fire-adapted grasslands, flood-maintained riparian forests). The key variables are disturbance frequency, intensity, extent, and predictability.

```
+---------------------------------------------------------------+
|              DISTURBANCE ECOLOGY FRAMEWORK                     |
|                                                                |
|  DISTURBANCE TYPES:                                            |
|  Physical: fire, wind, flood, drought, ice storm, volcano    |
|  Biotic: herbivory, disease outbreak, invasive species       |
|  Anthropogenic: clear-cutting, tillage, pollution, hunting   |
|                                                                |
|  KEY VARIABLES:                                                |
|  Frequency: how often      Intensity: how severe              |
|  Extent: spatial scale     Duration: how long                 |
|  Return interval: T between events                            |
|                                                                |
|  RESPONSES:                                                    |
|  Resistance: avoid disturbance (thick bark, deep roots)      |
|  Resilience: recover after disturbance                        |
|  Avoidance: dormancy (seeds, bulbs, spores)                  |
+---------------------------------------------------------------+
```

---

## Intermediate Disturbance Hypothesis (IDH)

Connell (1978): Maximum species diversity occurs at intermediate levels of disturbance frequency/intensity:

```
DIVERSITY
    ^
    |                 *
    |               *   *
    |             *       *
    |           *           *
    |         *               *
    |   *   *                   *   *
    +---+---+---+---+---+---+---+---+-> DISTURBANCE
       Low               High

LOW DISTURBANCE:
  Competitive exclusion takes over
  Dominant species displace others
  Low diversity (one or few species win)

INTERMEDIATE DISTURBANCE:
  Dominant competitors set back periodically
  Opportunities for inferior competitors + early colonizers
  Coexistence maintained
  → MAXIMUM DIVERSITY

HIGH DISTURBANCE:
  Only disturbance-tolerant species survive
  Few species can persist under continuous stress
  Low diversity again
```

**Evidence for IDH:** Tropical forests (tree-fall gaps increase diversity). Intertidal zones (moderate wave action). Grasslands (intermediate grazing). Prairie dogs (burrow disturbance increases small mammal diversity).

**Critique of IDH:** Meta-analyses show the unimodal pattern is not universal. Diversity may peak at low disturbance in some systems. Taxonomic group, spatial scale, and disturbance type all matter. But IDH is still useful as a conceptual framework.

**Exploration-exploitation connection:** The IDH is structurally identical to the exploration/exploitation tradeoff in reinforcement learning and optimization. Low disturbance = pure exploitation: dominant competitor wins, all "resource" allocated to best-known option, diversity collapses. High disturbance = pure exploration: too much randomness, only disturbance specialists survive, diversity collapses. Intermediate disturbance = epsilon-greedy or Thompson sampling: competitive dominants occasionally reset, inferior competitors get opportunities, diversity maintained. The ε-greedy RL agent and the intermediate-disturbance forest are maximizing different objectives but experiencing the same tradeoff dynamics.

---

## Fire Ecology — Fire as Ecosystem Process

Fire is one of the oldest and most pervasive disturbances. Many biomes co-evolved with fire:

```
FIRE TYPES:
  Surface fire: Burns ground vegetation + litter; low/moderate intensity
                Spares most trees (thick bark)
                Historically dominant in ponderosa pine forests
                (return interval 1–15 years; "maintenance fire")

  Crown fire:   Climbs into canopy; kills most trees
                Occurs when surface fuels accumulated (fire exclusion)
                Or in normally crown-fire adapted systems
                High intensity; creates large opening

  Ground fire:  Burns below surface through organic soil/peat
                (boreal peatlands; smolders for weeks)

FIRE BEHAVIOR DETERMINANTS:
  Fuel (amount, type, moisture)   +   Wind   +   Topography
  (slope increases uphill fire spread rate dramatically)
```

**Fire-adapted traits (plants):**

| Trait | Mechanism | Example |
|-------|-----------|---------|
| Thick bark | Insulates cambium | Ponderosa pine, cork oak |
| Serotinous cones | Cones sealed by resin; open only after fire heat | Lodgepole pine, Banksia |
| Lignotuber / burl | Underground storage organ; resprouts | Eucalyptus, chaparral shrubs |
| Deep roots | Survive surface heat | Grasses (most of biomass below ground) |
| Fire-stimulated germination | Seeds germinate only after smoke/heat | Many South African fynbos |
| Self-pruning | Lower branches die; raise crown → reduces fire ladder | Longleaf pine |

### Fire Regimes — Three Archetypes

```
HIGH FREQUENCY / LOW INTENSITY:  "Creeping fire"
  (Savannas, grasslands, open pine forests)
  Return interval: 1–10 years
  Kills small woody plants; favors grasses
  Maintains open structure; prevents tree encroachment
  Fire exclusion → woody encroachment → savanna → scrub/forest

LOW FREQUENCY / HIGH INTENSITY:  "Stand-replacing fire"
  (Boreal forest, lodgepole pine forest)
  Return interval: 100–300 years
  Kills almost everything; large patch dynamics
  Serotinous cones + massive seed release post-fire
  Creates age-class mosaic across landscape

MIXED SEVERITY: Intermediate (most western North American forests)
  Return interval: variable; stand-replacing patches in high-severity areas,
  surface fires in moderate areas, fuel-limited areas unburned
```

**Fire exclusion consequences** — 20th century fire suppression in western US (Smokey Bear era) accumulated fuel loads far above historical levels. Result: larger, more intense fires when they occur; loss of fire-adapted species; altered forest structure. Prescribed fire programs attempt to restore fire to these systems.

**Boreal forest and fire:** Fire is the dominant disturbance in boreal forest (taiga). Large fires (millions of hectares in Siberia, Canada) are normal ecosystem dynamics, not disasters. Climate change is increasing fire activity globally — higher temperature + drought + lightning ignition.

---

## Wind and Ice Disturbances

**Windthrow (treethrow, blowdown):**
```
MECHANISM:
  High winds exceed drag resistance of individual trees or stands
  → Uprooting (root anchorage failure) or stem breakage

SCALES:
  Single treefall: creates canopy gap (~0.01–0.1 ha); most common
  Blowdown patch: storm event; 0.1–10 ha; complex post-disturbance mosaic
  Catastrophic blowdown: tornado path, orographic wind (foehn/chinook events)
    → 1000s of hectares; e.g., 1999 Boundary Waters blowdown, Minnesota (~160,000 ha)

ECOLOGICAL SIGNIFICANCE:
  Single treefalls: primary mechanism of gap-phase dynamics in tropical and
    temperate forests; drives ~40% of tree regeneration in some systems
  Creates structural diversity: root throw mounds, tip-up pits, coarse woody debris
  → Habitat for specialized invertebrates, fungi, cavity nesters
  Blowdown patches: initiates secondary succession within a matrix of intact forest
```

**Ice storms:**
```
MECHANISM:
  Freezing rain (supercooled water droplets) → ice accumulation on branches
  Ice loading: even 1 cm radial ice = 10× branch weight
  → Branch breakage, stem bending, whole-tree uprooting

ECOLOGICAL PATTERNS:
  Selective: species with dense crowns, brittle wood, high crown mass most vulnerable
    (sugar maple, beech > white pine, red oak)
  Epiphytes and canopy lichens: ice loading → brittle lichen mat loss
  Recovery: rapid sprouting from epicormic buds; regeneration from seed bank

HISTORICAL EXAMPLE: January 1998 North American Ice Storm
  Affected Quebec, Ontario, New York, Maine
  Destroyed 100+ million trees in southern Quebec maple-beech forests
  Pulp/paper industry losses ~$1.5B; power outages for 28 days in some areas
  Ecological: maple stands severely damaged; compositional shift in some areas
```

**Hurricane/Cyclone disturbance:**
```
ECOLOGICAL IMPACTS:
  Defoliation: wind removes leaves → light pulse to forest floor → understory flush
  Branch + stem damage: opens canopy; increases coarse woody debris
  Uprooting: same gap dynamics as windthrow but spatially extensive
  Rainfall: massive hydrological pulse → nutrient flushing, stream scour

CHARACTERISTIC PATTERNS:
  Damage heterogeneous: topographic position matters (ridges more exposed)
  Species-selective: shallow-rooted species (Cecropia) vs deep-rooted (mahogany)
  Intensity gradient: outer bands low-damage; eyewall catastrophic
  Recovery: typically fast in the wet tropics (high NPP, resilient root systems)
    → 1989 Hurricane Hugo (Caribbean): 80% canopy loss → substantial recovery in 10 years

HURRICANE DISTURBANCE REGIME (Caribbean/SE US):
  Return interval: ~25–100 years at a given point in hurricane-prone regions
  → Shapes successional trajectories across the entire region
  → Wind-adapted traits selected for: higher wood density in Atlantic vs Pacific forests
    of same species (Atlantic exposed to more frequent hurricanes)

CLIMATE CHANGE AND HURRICANE INTENSITY:
  Warming SST → more intense (Category 4–5) hurricanes
  Rapid intensification events more common
  Ecological implication: fewer but more severe disturbance events
    → Less frequent but larger-magnitude regime disruption
```

---

## Invasive Species — Biological Invasion

An invasive species is a non-native species whose introduction causes ecological or economic harm. Not all introduced species are invasive (most die out or persist without major impacts):

```
INVASION PROCESS:

INTRODUCTION → ESTABLISHMENT → SPREAD → IMPACT
(intentional   (survives +    (expands  (ecological/
 or accidental) reproduces)    range)   economic harm)

 10%            10%           10%
(of introduced (of established (of spread   → some have
 species        species        species       major impacts)
 establish)     spread)
"The Tens Rule" (Williamson, 1996) — very rough estimate
```

### Why Do Some Species Become Invasive?

**Enemy Release Hypothesis:** In native range, species kept in check by predators, parasites, diseases. In new range, these natural enemies absent → population erupts. Supporting evidence: invasive plants often have fewer pathogens in new range.

**Novel weapons:** Some invaders have compounds toxic to native species in new range (garlic mustard inhibits mycorrhizal fungi that native trees depend on).

**Propagule pressure:** More individuals introduced + more introduction events → higher invasion probability (statistical argument; bypasses ecological filtering).

**Biotic homogenization:** Invasions are replacing unique regional biotas with a subset of globally widespread species → world becoming more ecologically homogeneous.

### Major Invasive Species — Case Studies

```
CASE 1: Brown tree snake (Boiga irregularis) — Guam
  Accidentally introduced ~1950 (WWII cargo from Admiralty Islands)
  Guam had no native snakes → birds evolutionarily naive
  Result: 9 of 12 native forest birds EXTINCT; 6 of 12 native lizards gone
  Also causes massive power outages (climbs electrical infrastructure)
  Cost: $4-5 million/year in control + outage repair

CASE 2: Cane toad (Rhinella marina) — Australia
  Intentionally introduced 1935 to control cane beetle pest
  Result: Failed to control beetles; toad itself became invasive
  Poisonous parotoid glands → kills native predators (quolls, goannas, snakes)
  Now >200 million individuals in NE Australia; still spreading

CASE 3: Zebra/Quagga mussels — North American Great Lakes
  Arrived ~1988 in ballast water from Black/Caspian Sea
  Filter feeding → dramatically increased water clarity
  → Shifted energy from plankton to benthic system
  → Native mussels eliminated from most of Great Lakes
  → $500 million+/year in biofouling costs (pipes, boats)

CASE 4: Kudzu (Pueraria montana) — SE United States
  Introduced from Japan in 1876 for erosion control; promoted as cattle feed
  Growth rate: up to 30 cm/day in summer
  Smothers trees, power lines, buildings
  "The vine that ate the South"
  Now ~3 million acres in SE US; expanding northward with warming

CASE 5: Chestnut blight fungus (Cryphonectria parasitica) — Eastern US
  Introduced ~1900 on nursery stock
  Nearly eliminated American chestnut (Castanea dentata)
  in 30 years — a dominant canopy species from Maine to Georgia
  >3 billion trees functionally extinct (stumps still sprout but die)
```

**Control methods:**

| Method | Approach | Best for |
|--------|---------|---------|
| Physical removal | Trapping, shooting, hand removal | Small populations; vertebrates |
| Chemical | Targeted herbicide, pesticide | Plants, insects |
| Biological control | Native natural enemies | Best long-term if available; risks of own biocontrol |
| Sterile male release | Overwhelm wild population with sterile males | Insects (screwworm success) |
| Early detection/rapid response | Eliminate before established | Prevention is key |

---

## Decision Cheat Sheet

| Disturbance ecology situation | Interpretation |
|-------------------------------|---------------|
| Old-growth fire suppressed forest with dense understory | High crown fire risk; fuel accumulation from exclusion |
| Species diversity highest in meadow patchwork | IDH: gap-phase dynamics or intermediate grazing maintaining openness |
| Native predator absent; prey species erupting | Trophic cascade; consider predator reintroduction |
| Invasive plant outcompeting natives | Enemy release likely; biological control if available |
| Fire-adapted ecosystem with declining fire frequency | Woody encroachment risk; prescribed fire needed |
| New pathogen wiping out dominant plant species | Analogous to chestnut blight; consider resistance breeding |

---

## Common Confusion Points

**"Disturbance" ≠ unusual event** — In fire-adapted grasslands, fire every 1–5 years is normal. In lodgepole pine forests, stand-replacing fire every 100–300 years is normal. The disturbance regime defines the ecosystem. Human fire exclusion is an *unusual* event from an ecological perspective.

**Not all non-native species are invasive** — ~90% of introduced species establish but don't become invasive. The European honeybee is non-native in the Americas but is not ecologically invasive in most contexts. "Exotic" ≠ "invasive." Only species causing significant harm to native ecosystems qualify as invasive.

**Invasive eradication gets harder with time** — There's a short window after introduction to eradicate before populations become established and widespread. Once an invasive is well-established across a landscape, eradication is essentially impossible with current tools. Early detection systems (eDNA, citizen science) are critical.

**Fire as both ecosystem process and hazard** — Fire is ecologically necessary in many systems AND an extreme hazard to humans. The solution is not simply "let fire burn" everywhere — it requires sophisticated landscape management: prescribed fire in appropriate areas, fire exclusion around human communities, and restoration of fire-adapted species compositions.