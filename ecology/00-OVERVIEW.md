# Ecology — Overview

## The Big Picture

Ecology is the study of interactions between organisms and their environment. It operates at nested levels of organization and intersects every other biological and earth science. The fundamental insight: species don't exist in isolation — they exist in webs of relationships, constrained by physical environment and shaped by evolution.

```
+------------------------------------------------------------------+
|                    ECOLOGY LEVELS OF ORGANIZATION                 |
|                                                                   |
|  ORGANISM     Individual physiology, behavior, life history      |
|      |                                                            |
|      v                                                            |
|  POPULATION   Single species in a place; dynamics over time     |
|               (birth, death, immigration, emigration)            |
|      |                                                            |
|      v                                                            |
|  COMMUNITY    Multiple species interacting                       |
|               (predation, competition, mutualism)                |
|      |                                                            |
|      v                                                            |
|  ECOSYSTEM    Community + abiotic environment                    |
|               (energy flow + nutrient cycling)                   |
|      |                                                            |
|      v                                                            |
|  LANDSCAPE    Mosaic of ecosystems                               |
|      |                                                            |
|      v                                                            |
|  BIOME        Major vegetation/climate zone (global scale)       |
|      |                                                            |
|      v                                                            |
|  BIOSPHERE    All life on Earth + Earth systems                  |
+------------------------------------------------------------------+
```

---

## Abiotic vs Biotic Factors

**Abiotic** = non-living physical and chemical factors:

| Category | Examples | Key Variables |
|----------|---------|---------------|
| Climate | Temperature, precipitation, radiation, wind | Mean + variance + seasonality |
| Soils | Texture, nutrients (NPK), pH, organic matter | Availability, not just amount |
| Water | Salinity, pH, dissolved O₂, depth, flow | Aquatic systems primarily |
| Disturbance | Fire, flood, drought, wind | Frequency, intensity, extent |

**Biotic** = living components:
- Producers (autotrophs): fix energy from sunlight or chemosynthesis
- Consumers (heterotrophs): herbivores, carnivores, omnivores, detritivores
- Decomposers: bacteria, fungi — recycle nutrients from dead organic matter
- Parasites, pathogens, mutualists

<!-- @editor[bridge/P2]: Liebig's Law maps to bottleneck analysis in systems engineering and critical-path scheduling; any engineer from capacity planning needs this connection -->
**Liebig's Law of the Minimum** — growth rate of an organism is limited by the resource most scarce relative to requirement. Even if all others are abundant. Originally for crop nutrients (nitrogen, phosphorus, potassium) but applies broadly.

---

## Founding Figures and Historical Context

| Figure | Contribution | Year |
|--------|-------------|------|
| Ernst Haeckel | Coined "Oekologie" (ecology) | 1866 |
| Alfred Russel Wallace | Biogeography, species distributions | 1870s |
| Charles Elton | Food chains, ecological niche, population dynamics | 1920s–1940s |
| G. Evelyn Hutchinson | Multidimensional niche concept, limnology | 1940s–1970s |
| Robert MacArthur | Island biogeography, competition theory, optimization | 1960s |
| E.O. Wilson | Sociobiology, biodiversity, island biogeography | 1960s–2000s |
| Eugene Odum | Ecosystem ecology, energy flow, ecosystem services | 1950s–1970s |
| C.S. Holling | Resilience, panarchy, adaptive cycles | 1970s–2000s |
| Paul Ehrlich | Population ecology, extinction crisis | 1960s–present |

---

## The Niche Concept

<!-- @editor[bridge/P2]: n-dimensional hypervolume = convex feasibility region in R^n; connect to constraint satisfaction or feasible solution spaces for MIT math background -->
G. E. Hutchinson's (1957) fundamental niche: n-dimensional hypervolume in environmental space within which a species can persist. Realized niche = subset occupied given competition, predation.

```
FUNDAMENTAL NICHE:
  Full range where species can physiologically survive

REALIZED NICHE:
  Actual range after biotic interactions (usually smaller)

NICHE DIMENSIONS MIGHT INCLUDE:
  Temperature range, humidity, food particle size,
  time of activity, substrate type, depth...

NICHE OVERLAP → COMPETITION
  Two species with identical niches cannot coexist (competitive exclusion)
  Coexistence requires niche differentiation (resource partitioning)
```

---

## Directory Map

| File | Core Concept |
|------|-------------|
| `01-POPULATION-DYNAMICS.md` | Growth models, Lotka-Volterra, r/K selection, metapopulation |
| `02-COMMUNITY-ECOLOGY.md` | Species interactions, keystone species, trophic cascades |
| `03-ECOSYSTEM-ENERGETICS.md` | Energy flow, trophic efficiency, GPP/NPP |
| `04-BIOGEOCHEMICAL-CYCLES.md` | Carbon, nitrogen, phosphorus cycles; human perturbation |
| `05-SUCCESSION-STABILITY.md` | Succession models, resilience, regime shifts |
| `06-BIOGEOGRAPHY.md` | Island biogeography, dispersal/vicariance, diversity gradients |
| `07-AQUATIC-ECOSYSTEMS.md` | Lakes, streams, estuaries, coral reefs |
| `08-DISTURBANCE-ECOLOGY.md` | IDH, fire ecology, invasive species |
| `09-CONSERVATION-BIOLOGY.md` | Biodiversity metrics, fragmentation, rewilding |

---

<!-- @editor[structure/P1]: Missing Decision Cheat Sheet -- overview should have "which guide to read when" decision table mapping ecological questions to the right file -->
## Common Confusion Points

**Ecology ≠ environmentalism** — Ecology is the science of interactions between organisms and environments. Environmentalism is a value system/movement. Ecologists can study invasive species, pest control, agricultural systems — not just "natural" systems.

**Population vs community** — A population is one species in one place. A community is multiple species. Population ecology: How does wolf population size change over time? Community ecology: How do wolves, elk, and vegetation interact?

**Ecosystem services** — the benefits humans obtain from ecosystems: provisioning (food, water), regulating (climate, flood control, water purification), cultural (recreation, spiritual), supporting (nutrient cycling, soil formation). A framework for valuing ecological processes in economic terms.