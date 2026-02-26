# Biogeography — Island Biogeography, Dispersal vs Vicariance, Diversity Gradients

## The Big Picture

Biogeography asks: why are species where they are? The answer involves both ecological processes (current environment, interspecific interactions) and historical processes (continental drift, past climate, colonization history). The island biogeography theory of MacArthur and Wilson elegantly united ecology and evolution and has become the theoretical backbone of modern conservation biology.

```
+---------------------------------------------------------------+
|              BIOGEOGRAPHY FRAMEWORK                            |
|                                                                |
|  HISTORICAL FACTORS          ECOLOGICAL FACTORS               |
|  ----------------------      -------------------------        |
|  Continental drift           Current climate                  |
|  (vicariance)                Current habitat availability     |
|  Past climate (glacials)     Interspecific competition        |
|  Dispersal events            Predation + disturbance          |
|  Mass extinctions            Niche availability               |
|                                                                |
|  PATTERN: Species distributions reflect both                 |
|           historical contingency + current filtering         |
+---------------------------------------------------------------+
```

---

## Island Biogeography Theory — MacArthur and Wilson (1967)

The classic theory explains species richness on islands as an equilibrium between colonization and extinction:

```
SPECIES RICHNESS MODEL:

      Rate of                    Rate of
    Colonization               Extinction
         |                         |
         v                         v
    High |                         | High
         |  \ Colonization rate    |           / Extinction rate
         |   \  (decreases as      |          /  (increases as
    Low  |    \ more species       |  Low    /   more species
         |     \ established)      |        /    compete for
         |      \                  |       /     limited space)
         |       \                 |      /
         +---+----\----------------+-----/-----→ Species richness
                   \ ↗                 ↗
                    × = S* (equilibrium species richness)
                    (immigration = extinction)
```

**Key predictions:**

```
1. AREA EFFECT: Larger islands → more species
   Mechanism: Larger area → larger populations → lower extinction
   S = c × A^z  (species-area relationship)
   z ≈ 0.20–0.35 for oceanic islands
   z ≈ 0.10–0.20 for mainland "habitat islands"

2. DISTANCE EFFECT: More isolated islands → fewer species
   Mechanism: Greater distance → lower colonization rate
   → Fewer species at equilibrium

3. TURNOVER: Species composition changes over time
   even at equilibrium S* (constant rate of extinction +
   recolonization of different species)

4. RESCUE EFFECT: More isolated islands → lower extinction
   (partially counter to distance effect)
   Mechanism: Immigrants boost small populations near extinction
```

**Species-area relationship (SAR):**
```
log(S) = log(c) + z × log(A)

S = species richness
A = area
c = constant (fitted to data)
z ≈ 0.25 for oceanic islands (empirical average)

IMPLICATION:
  10× area → S increases by 10^0.25 = 1.78× (78% more species)
  Reducing habitat to 1/10 → losing ~46% of species
  (converse of SAR: habitat loss reduces species)
```

**Power-law connection:** S = cA^z is a pure power law — the same mathematical form as Zipf's law (word frequency ∝ rank^-1), the Pareto distribution (wealth ∝ rank^-1.16), and the degree distribution of scale-free networks (P(k) ∝ k^-γ). In log-log space, all power laws are straight lines with slope z (or -γ). The species-area exponent z ≈ 0.25 for oceanic islands is empirically consistent across taxa and biogeographic regions — suggesting a universal underlying process rather than a taxon-specific mechanism.

**Fractal dimension connection:** The species-area relationship can be derived from fractal habitat structure. If a habitat has fractal dimension D (between 1 and 2 for a 2D surface), and species territories scale with area, then z = 2/D in the simplest model. Real landscapes have fractal coastlines, fractal elevation contours — the irregular geometry of habitat edges contributes to the SAR exponent. Habitat loss that increases fragmentation (reduces effective D) steepens the effective z, making species loss worse than the simple SAR predicts.

**Simberloff and Wilson (1969)** — experimentally defaunated small mangrove islands in Florida and tracked recolonization. Confirmed equilibrium theory and turnover predictions.

---

## Species-Area Relationship in Conservation

The SAR is the theoretical foundation of habitat fragmentation analysis:

```
HABITAT FRAGMENTATION EFFECTS:

ORIGINAL HABITAT:              FRAGMENTED HABITAT:
+---------------------------+   +-----+ +---+ +-------+
|                           |   |  A  | | B | |   C   |
|    CONTINUOUS FOREST      |   +-----+ +---+ +-------+
|    (high connectivity)    |   (same total area; lower species)
+---------------------------+

WHY FEWER SPECIES IN FRAGMENTS?
1. SAR: smaller area → fewer species (area effect)
2. Edge effects: fragment dominated by edges (different microclimate,
   invasive species, predators)
3. Isolation: immigration reduced → rescue effect lost
4. Demographic: small populations → stochastic extinction
5. Loss of interior habitat: forest interior species sensitive to edges
```

**SLOSS Debate** (Single Large Or Several Small):
- Single large reserve preserves large-area specialists and large mammals
- Several small preserves more total edge habitat, different communities
- Modern consensus: context-dependent; large reserves + corridors are best

---

## Dispersal vs Vicariance — Historical Biogeography

Two mechanisms produce disjunct (geographically separated) populations:

```
VICARIANCE:                        DISPERSAL:
Ancestral range divided by         Ancestor disperses across barrier
geological/climate barrier         → establishes new population
(continental drift, mountain       (rafting, wind, birds)
 formation, sea level change)

A + B (connected)                  A disperses → lands on island B
       ↓                           A                  B
  Barrier forms                  (source)         (colonized)
  /         \
 A           B                  Example: Darwin's finches (from
(isolated   (isolated)          Central America → Galápagos via
 population) population)        chance dispersal ~2-3 Ma)
Example: tapirs in South America + SE Asia (vicariant: Gondwana)
         Marsupials in Australia + Americas (vicariant: Gondwana breakup)
```

**Molecular phylogeography** — using DNA divergence times to test vicariance vs dispersal hypotheses. If divergence time < barrier age → dispersal. If divergence time ≈ barrier age → vicariance.

---

## Biogeographic Regions (Realms)

Alfred Russel Wallace (1876) defined six major biogeographic realms based on vertebrate distributions. These reflect continental isolation history:

```
REALM          AREA                   CHARACTERISTIC GROUPS
-----------    -------------------    ---------------------------
Neotropical    South + Central        Monkeys (New World), tapir,
               America                llama, toucans, hummingbirds

Nearctic       North America          Bison, pronghorn, many
               (+ Greenland)          Holarctic overlap with Palearctic

Palearctic     Europe + Asia          Pandas, tigers, reindeer (Holarctic)
               + N Africa

Ethiopian      Sub-Saharan Africa     Elephants (African), lions, giraffes,
(Afrotropical)                        gorillas, wildebeest

Oriental       S + SE Asia            Elephants (Asian), orangutan,
(Indomalayan)  (India to Indonesia)   tigers, Indian rhino

Australian     Australia + New        Marsupials (dominant), monotremes,
(Australasian) Guinea + NZ            birds of paradise, kiwi

Marine realms: 10+ defined by oceanographic barriers
```

**Wallace Line** — Alfred Russell Wallace identified a profound faunal discontinuity between Bali/Borneo (Oriental fauna) and Lombok/Sulawesi (Australasian fauna). Despite only 35 km separation, the deep Lombok Strait was a barrier even during Pleistocene ice ages (sea level lowering exposed land bridges in the Sunda Shelf but not across the deep Lombok-Makassar straits).

---

## Latitudinal Diversity Gradient

The most striking pattern in biogeography: species richness increases from poles to equator, in almost every taxon:

```
DIVERSITY (species number)
    ^
    |
100 |
    |                         *
 50 |                    *
    |               *
 20 |          *
    |     *
 10 |*
    +----+----+----+----+----> LATITUDE
    90°N 70°  50°  30°  10°

(approximate for trees; pattern similar for birds, mammals, insects)
```

**Explanatory hypotheses (multiple non-exclusive):**

| Hypothesis | Mechanism | Evidence |
|-----------|-----------|---------|
| **Energy** (Temperature/productivity) | More energy → more species can be supported | Correlates: correlation with temperature, NPP |
| **Evolutionary speed** | Higher T → faster mutation, speciation | DNA divergence faster in tropics |
| **Time/stability** | Tropics stable for longer (fewer glacial extinctions) | Tropical lineages older |
| **Rapoport's rule** | Tropical species have narrower ranges; more species can "fit" in same area | Pattern observed in many taxa |
| **Niche conservatism** | Most lineages originated in tropics; don't colonize cold | Phylogenetic data |
| **Diversification rate** | Tropics = higher speciation minus extinction | Some phylogenetic evidence |

**Most likely: combination of energy availability, evolutionary time, and stability.**

---

## Glacial Refugia and Post-Glacial Colonization

Pleistocene glaciations (~20 glacial cycles in last 2 Ma) repeatedly shifted species ranges:

```
GLACIAL MAXIMUM (18-22 ka):
  Ice sheets to 45°N in North America and Europe
  Forests retreated to refugia (unglaciated pockets)
  Species compressed into smaller ranges

DEGLACIATION (post-18 ka):
  Rapid warming → range expansions from refugia
  Gene flow between previously isolated populations
  Colonization of deglaciated terrain
  Sea level rise (120 m) → flooded land bridges

CONSEQUENCES:
  Modern species ranges still reflect post-glacial expansion routes
  (latitudinal gradients in genetic diversity: less at northern edge)
  Rapid evolution in newly expanded ranges (founder effects)
  Hybridization where expanding populations meet
```

---

## Decision Cheat Sheet

| Biogeographic question | Tool/concept |
|----------------------|-------------|
| Why are two similar species on opposite sides of ocean? | Vicariance (continental drift) or dispersal |
| How many species in protected habitat? | Species-area relationship: S = cA^z |
| What fraction of species lost if habitat reduced to 10%? | ~46% (if z=0.25); 10^0.25 ≈ 1.78 |
| Why is tropical diversity higher than temperate? | Energy, evolutionary time, stability (multiple hypotheses) |
| Why do Australian mammals look so different? | Long isolation (vicariance); marsupials filled niches convergently |
| Why does island have fewer species than mainland of same area? | Colonization rate lower; extinction rate higher (MacArthur-Wilson) |

---

## Common Confusion Points

**"Islands" in conservation** — In conservation biology, "islands" include any patch of habitat surrounded by unsuitable matrix: forest patch in agricultural landscape, mountain top, lake, desert oasis. Island biogeography theory applies to all "habitat islands," not just oceanic islands.

**SAR z-values differ for islands vs mainlands** — Oceanic islands (z ≈ 0.25–0.35): higher because they are truly isolated. Habitat islands on mainlands (z ≈ 0.10–0.20): lower because some dispersal crosses the matrix. Using oceanic island z-values for conservation planning overestimates species loss from habitat reduction.

**Equilibrium theory is about richness, not identity** — MacArthur-Wilson predicts species *number* at equilibrium, not *which species* will be there. Turnover is expected even at equilibrium S*. The same number of species persist, but turnover means different species replace each other over time.

**Wallace ≠ Darwin's islands** — Darwin spent most time on the Galápagos (Pacific); Wallace worked primarily in Malay Archipelago (SE Asia/Indonesia). Both developed natural selection essentially simultaneously (1858, joint presentation). Wallace's biogeographic work was independent and complementary to Darwin's evolutionary thinking.