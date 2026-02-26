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

**Liebig's Law of the Minimum** — growth rate of an organism is limited by the resource most scarce relative to requirement. Even if all others are abundant. Originally for crop nutrients (nitrogen, phosphorus, potassium) but applies broadly.

This is bottleneck analysis applied to biology: the system throughput is determined by the single scarcest resource, regardless of excess elsewhere. Equivalent to Amdahl's Law for biological systems — optimizing non-bottleneck resources has zero effect until the true bottleneck is addressed. In practice: adding N fertilizer to a P-limited lake does nothing for algal growth. Adding water to a N-limited desert does nothing for plant growth. Identify the constraint first.

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

G. E. Hutchinson's (1957) fundamental niche: n-dimensional hypervolume in environmental space within which a species can persist. Realized niche = subset occupied given competition, predation.

Formally: the fundamental niche is the feasible region in ℝⁿ defined by n inequality constraints (one per environmental variable). Each constraint is a range: species survives when temperature ∈ [T_min, T_max], humidity ∈ [H_min, H_max], etc. The intersection of all n constraint sets is the niche hypervolume — exactly a convex polytope in the n-dimensional parameter space if constraints are independent. The realized niche is the feasible region further reduced by biotic constraints (competition, predation) — a constraint satisfaction problem where abiotic constraints define the feasible region and biotic interactions carve out additional infeasible subsets.

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

## Decision Cheat Sheet — Which Guide to Read When

| Your question | Guide | Core concept |
|---------------|-------|-------------|
| Why is this population growing / crashing? | 01-POPULATION-DYNAMICS | Exponential / logistic growth, r, K, λ |
| Will predator-prey cycle? Can both species coexist? | 01-POPULATION-DYNAMICS | Lotka-Volterra, equilibrium stability |
| Which age class should conservation target? | 01-POPULATION-DYNAMICS | Leslie matrix, sensitivity/elasticity analysis |
| Why do some species coexist and others exclude each other? | 02-COMMUNITY-ECOLOGY | Competitive exclusion, coexistence theory, niche partitioning |
| What happens when a top predator is removed? | 02-COMMUNITY-ECOLOGY | Trophic cascade, keystone species |
| How much energy is available at trophic level 4? | 03-ECOSYSTEM-ENERGETICS | 10% rule: NPP × 10% × 10% × 10% |
| Why is beef production energetically costly? | 03-ECOSYSTEM-ENERGETICS | Endotherm trophic efficiency (~5–10%); trophic level 2–2.5 |
| Why is this lake turning green? | 04-BIOGEOCHEMICAL-CYCLES | Phosphorus-limited eutrophication |
| What's the carbon balance of this ecosystem? | 04-BIOGEOCHEMICAL-CYCLES | GPP, NPP, NEP, NBP; carbon sink vs source |
| Why is the ecosystem not recovering after disturbance stops? | 05-SUCCESSION-STABILITY | Regime shift, hysteresis, alternative stable states |
| Why are there more species in the tropics? | 06-BIOGEOGRAPHY | Latitudinal diversity gradient; energy + time hypotheses |
| How many species will be lost if I reduce habitat by 50%? | 06-BIOGEOGRAPHY | Species-area relationship: S = cA^z; z ≈ 0.25 |
| Why is lake productivity seasonal? | 07-AQUATIC-ECOSYSTEMS | Thermal stratification, fall/spring overturn |
| When does fire increase vs decrease biodiversity? | 08-DISTURBANCE-ECOLOGY | IDH; fire regime type; frequency × intensity |
| How to prioritize which habitats to protect? | 09-CONSERVATION-BIOLOGY | Hotspots, complementarity, Marxan, gap analysis |

**Use 01 when** the question is about a single species over time. **Use 02 when** the question involves species interactions. **Use 05 when** the question is about recovery after disturbance or why an ecosystem isn't returning to its prior state.

---

## Common Confusion Points

**Ecology ≠ environmentalism** — Ecology is the science of interactions between organisms and environments. Environmentalism is a value system/movement. Ecologists can study invasive species, pest control, agricultural systems — not just "natural" systems.

**Population vs community** — A population is one species in one place. A community is multiple species. Population ecology: How does wolf population size change over time? Community ecology: How do wolves, elk, and vegetation interact?

**Ecosystem services** — the benefits humans obtain from ecosystems: provisioning (food, water), regulating (climate, flood control, water purification), cultural (recreation, spiritual), supporting (nutrient cycling, soil formation). A framework for valuing ecological processes in economic terms.