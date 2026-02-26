# Insect Ecology and Population Dynamics

## The Big Picture

Insect population ecology bridges individual-level physiology and community-level processes. Insects are both the drivers and the dominated objects in most terrestrial food webs. Their population dynamics — cycles, outbreaks, collapses — are among the most studied in ecology, and the mathematical frameworks developed for insects (Nicholson-Bailey model, density-dependence theory) have become ecological theory foundations.

```
ECOLOGICAL LEVELS IN INSECT ECOLOGY
======================================

INDIVIDUAL:
  Foraging theory (optimal foraging)
  Thermoregulation
  Predator avoidance
         |
         v
POPULATION:
  Birth/death rates; density dependence
  Life tables; cohort analysis
  r vs K strategies
  Population cycles; outbreaks
         |
         v
COMMUNITY:
  Competition; predation; mutualism
  Food web position; trophic cascades
  Diversity indices; assembly rules
         |
         v
ECOSYSTEM:
  Nutrient cycling; decomposition
  Energy flow; primary productivity
  Insect as keystone functional group
```

---

## Life History Strategies

```
r vs K SELECTION IN INSECTS
==============================

r-SELECTED (opportunistic):
  High reproductive rate, short generation time
  Small body size, no parental care
  Population tracks resource availability closely
  Examples:
    Aphids: parthenogenetic; 10-20 days/generation; 50-100 nymphs/female
    Fruit flies: 14-day generation; 400 eggs/female
    Mosquitoes: opportunistic larval habitat
  Characteristic: boom-bust population dynamics
                  colonize disturbed habitats rapidly

K-SELECTED (equilibrium):
  Low reproductive rate, long generation time
  Large body size, possible parental care
  Population near carrying capacity (K)
  Examples:
    Periodical cicadas: 17-year cycle; emerge in synchrony
    Large beetles (Dynastes): 2-5 year development
    Social Hymenoptera: colony-level demography
  Characteristic: stable populations; slow recovery from perturbation

+----------------------------------------------+
| LIFE HISTORY TRADE-OFFS                      |
| Current reproduction vs future survival      |
| Number vs size of offspring                  |
| Development speed vs adult size              |
| Body size vs metabolic rate                  |
+----------------------------------------------+
```

---

## Population Growth Models

```
BASIC INSECT POPULATION MODELS
=================================

EXPONENTIAL GROWTH (density-independent):
  dN/dt = rN
  N(t) = N0 * e^(rt)
  r = intrinsic rate of natural increase
      (birth rate - death rate)
  Aphids: r ~ 0.3/day -> population doubles in 2.3 days
  Appropriate for: invading populations, early colonization

LOGISTIC GROWTH (density-dependent):
  dN/dt = rN(1 - N/K)
  K = carrying capacity
  Population slows as N -> K
  Density dependence: competition, disease, predation increase
  with N -> stabilizes population

LIFE TABLE ANALYSIS:
  x    lx       mx       lx*mx
  0    1.00    0.0       0.0
  1    0.70    2.0       1.4     (lx = survivorship from birth)
  2    0.40    5.0       2.0     (mx = fecundity at age x)
  3    0.10    3.0       0.3
  Net Reproductive Rate R0 = sum(lx*mx) = 3.7
  If R0 > 1: population growing
  If R0 = 1: stable
  If R0 < 1: declining

GENERATION TIME:
  T = sum(x * lx * mx) / R0
  Links life table to intrinsic growth rate r ~ ln(R0)/T
```

---

## Population Regulation: Density Dependence

```
DENSITY DEPENDENCE MECHANISMS
================================

NEGATIVE DENSITY DEPENDENCE (regulatory):
  As N increases -> per capita birth rate decreases OR
  As N increases -> per capita death rate increases
  -> negative feedback -> stabilizes population

  DIRECT DENSITY DEPENDENCE (same generation):
    Intraspecific competition for food -> starvation
    Disease transmission -> mortality increases with density
    Predator aggregation -> predation increases with density

  DELAYED DENSITY DEPENDENCE (different generation):
    Parasitoid-host cycles (Nicholson-Bailey)
    Plant quality decline after outbreak -> next generation suffers
    Leads to: population CYCLES

NICHOLSON-BAILEY PARASITOID-HOST MODEL:
  Host:      Ht+1 = Ht * R * exp(-a * Pt)
  Parasitoid: Pt+1 = Ht * (1 - exp(-a * Pt))
  Where R = host finite rate of increase
        a = searching efficiency of parasitoid
  Predicts: inherently unstable oscillations
  Reality: refugia + functional responses stabilize
```

---

## Insect Outbreaks

Outbreaks are population explosions beyond normal density bounds, typically with large ecological and economic consequences. Understanding their mechanics is essential for pest management.

```
OUTBREAK TYPES AND MECHANISMS
================================

ERUPTIVE SPECIES (endemic low, periodic outbreak):
  Forest defoliators: spruce budworm, gypsy moth, pine processionary
  Mechanism: multiple competing hypotheses
    1. Bottom-up (food quality): post-stress trees = higher N, lower tannin
    2. Top-down (predator release): generalist predators can't track
       rapid host population growth -> prey escape regulation
    3. Lateral (weather): synchronizing outbreaks across landscape
    4. Budworm + delayed density dependence:
       Young trees -> poor habitat -> low outbreak
       Mature trees -> good habitat -> outbreak
       Outbreak kills trees -> forest rejuvenates -> cycle

IRRUPTIVE SPECIES (locust phase polyphenism):
  Schistocerca gregaria:
    Solitary -> gregarious switch: serotonin in CNS
    Trigger: hind leg mechanoreceptors stimulated >2x/min
    Gregarious: darker, larger, aggregative, migratory
    Swarms: 40M-80M insects/km^2; 130km/day; eat entire crop
    Forecast model: satellite remote sensing of vegetation greenness
                    + rainfall -> locust habitat mapping

INVASIVE SPECIES OUTBREAKS:
  Enemy release hypothesis: no natural enemies in new range
  -> rapid population growth to levels never seen in native range
  Examples:
    Emerald ash borer (Agrilus planipennis): ~10B trees killed in N.America
    Brown marmorated stink bug (Halyomorpha halys): US agriculture
    Spotted lanternfly (Lycorma delicatula): grape + tree damage, E. USA
```

---

## Thermal Ecology and Climate

```
INSECT THERMAL BIOLOGY
========================

ECTOTHERMY:
  Body temperature ~ ambient temperature (mostly)
  Exception: flight muscle endothermy (bees, moths pre-flight shivering)
             basking thermoregulation (butterflies)

THERMAL PERFORMANCE CURVES:
  Performance (development rate, reproduction, flight)
         /\
        /  \
       /    \  <- optimal temperature range
      /      \
  ___/        \___ -> mortality
      CTmin   CTmax
  T_opt typically 70-90% of CTmax

DEVELOPMENT AND TEMPERATURE:
  Degree-day accumulation:
    DD = (T_mean - T_base) * days
    T_base = lower development threshold (0-10C typically)
    Sum of degree-days to complete development = constant (species-specific)
    Example: European corn borer: 900 DD base 10C to adult emergence

CLIMATE CHANGE EFFECTS:
  Range shifts poleward/upward: ~6km N/yr or 6m elevation/yr
  Phenological shifts: earlier emergence (5-10 days/decade)
  Mismatch with host plants and natural enemies
  Winter mortality reduction -> population increase in some pests
  Tropical insects: narrower thermal range -> vulnerable to warming

DIAPAUSE AND PHOTOPERIOD:
  Critical photoperiod triggers dormancy before winter
  Climate-adapted genotypes vary in critical photoperiod
  Rapid evolution possible: D. melanogaster CLP evolved in <50 yrs
```

---

## Aquatic Insects and Water Quality

```
AQUATIC INSECT ECOLOGY
========================

MAJOR AQUATIC ORDERS:
  Ephemeroptera (mayflies)    EPT INDEX <- most sensitive
  Plecoptera (stoneflies)           <- water quality indicators
  Trichoptera (caddisflies)   EPA standard biomonitoring
  Odonata (dragonflies)       moderate sensitivity
  Diptera (many midges)       pollution tolerant (Chironomidae)
  Coleoptera (diving beetles) moderate sensitivity

EPT INDEX (Ephemeroptera + Plecoptera + Trichoptera):
  High EPT diversity -> clean water
  Low EPT, high Chironomidae/Tubifex -> organic pollution
  Standard biomonitoring metric globally

FUNCTIONAL FEEDING GROUPS:
  Shredders: tear coarse particulate organic matter (leaves)
             -> fine particulate; Plecoptera, Trichoptera
  Collectors: gather fine particulate organic matter
             -> meiofauna biomass; Chironomidae, Baetidae
  Scrapers:  eat periphyton (algal film on rocks)
             -> Ecdyonurus, Heptageniidae
  Predators: aquatic invertebrate predation; Odonata, Perlidae
  Filterers: filter-feed on suspended FPOM; Simuliidae

LONGITUDINAL RIVER CONTINUUM (Vannote 1980):
  Headwaters: shredders dominant (allochthonous input)
  Mid-reaches: collectors dominant (FPOM from upstream shredding)
  Lower reaches: collectors + filterers (fine suspended matter)
```

---

## Community Ecology: Insects in Food Webs

```
INSECT TROPHIC ROLES
======================

PRIMARY CONSUMERS (herbivores):
  ~40% of insect species
  Transfer plant primary production to higher trophic levels
  Critical link: if removed, vertebrate predators collapse

SECONDARY CONSUMERS (predators + parasitoids):
  Predatory beetles (Carabidae, Coccinellidae)
  Predatory flies (Asilidae)
  Predatory wasps (Vespidae, Pompilidae)
  Odonata (both larval and adult)

PARASITOIDS (trophic level 2.5):
  Larval development consumes host; host dies
  ~150,000 described parasitoid species (mostly Hymenoptera + Diptera)
  May constitute ~20% of insect species
  Critical regulation of herbivore populations

DECOMPOSERS:
  Coleoptera larvae (Dermestidae, Ptinidae): keratin, bone
  Diptera larvae (Calliphoridae, Sarcophagidae): carrion
  Scarabaeidae: dung processing
  Isoptera (termites): lignocellulose

TROPHIC CASCADES:
  Removal of top insect predators (Odonata, Carabidae)
  -> herbivore release -> plant damage increase
  Documented in agricultural systems repeatedly
  "Biological control" = managed trophic cascade
```

---

## Migration and Long-Distance Movement

```
INSECT MIGRATION
=================

CATEGORIES:
  TRUE MIGRATION: directed, long-distance, facultative or obligate
    Monarch (Danaus plexippus): 4,500km N America -> Mexico
    Painted lady (Vanessa cardui): 12,000km W Africa -> Arctic Circle
    Desert locust: follows Inter-Tropical Convergence Zone
    Dragonflies (Libellula, Pantala): transoceanic (Pantala: 14,500km)

  DISPERSAL: undirected movement; colonization of new habitat

NAVIGATION MECHANISMS (Monarch):
  Time-compensated sun compass: sun position + circadian clock
  Magnetic field detection: proposed but evidence equivocal
  Olfactory/visual landmarks: route reinforcement
  Inherited direction: naive monarchs can navigate without learning

WIND ASSISTANCE:
  Most "migrants" are wind-assisted opportunists
  Travel in boundary layer above ground in favorable winds
  Aphid migration: essentially wind-dispersed
  Spruce budworm moths: weather-synchronized mass dispersal

POPULATION CONSEQUENCES:
  Mixing prevents local adaptation in migrants
  Source-sink dynamics: northern breeding season (high r)
                        southern overwintering (survival only)
  Conservation: must protect both ends of migration + stopover habitats
```

---

### Engineering Bridges

Insect population dynamics uses the same differential equation toolkit as queueing theory and capacity planning. The exponential growth model dN/dt = rN is the unbounded queue with constant arrival rate and no service limit — same equation, same instability. The logistic model dN/dt = rN(1 - N/K) is the bounded queue: K is the service capacity (carrying capacity), and the term (1 - N/K) is the utilization factor that slows growth as the system approaches saturation. At N = K/2, growth rate is maximized — this is the inflection point in an S-curve, the same point where a logistic growth process adds the most consumers per unit time.

The Nicholson-Bailey host-parasitoid model is a discrete-time two-species system that produces oscillations and instability — the biological equivalent of an underdamped control loop. The model is:

```
  H(t+1) = λ H(t) exp(-a P(t))         // host next generation
  P(t+1) = c H(t) [1 - exp(-a P(t))]   // parasitoid next generation
```

Where H = host density, P = parasitoid density, λ = host growth rate, a = area of discovery, c = parasitoid yield per host. This system has a single equilibrium that is inherently unstable — small perturbations lead to diverging oscillations (both populations crash to extinction). Real host-parasitoid systems persist because of spatial structure (refugia), heterogeneous attack rates, and density-dependent factors that add stabilizing feedback. This is the control systems insight: an open-loop unstable system requires feedback with sufficient gain and appropriate phase margin to stabilize. IPM biological control adds that stabilizing feedback by managing spatial structure and ensuring parasitoid persistence.

Degree-day accumulation is thermal integration — the biological equivalent of a hardware thermal envelope monitor. A CPU accumulates thermal energy; if sustained above T_junction, the chip fails. An insect pest accumulates thermal energy above its developmental threshold (T_base); when accumulated DD reaches a calibrated threshold, a life-stage transition occurs. The integral ∫(T - T_base)dt over time is the governing quantity in both cases; the threshold at which a state change occurs is the key parameter. Climate-based forecasting of pest emergence is thus analogous to predicting when a CPU will throttle based on thermal history — same math, different physical domain.

## Decision Cheat Sheet

| Concept | Key equation/model | Application |
|---------|-------------------|-------------|
| Exponential growth | dN/dt = rN | Early-stage outbreak prediction |
| Logistic growth | dN/dt = rN(1-N/K) | Carrying capacity; K estimation |
| Degree-days | DD = sum(T_mean - T_base) | Pest emergence forecasting |
| Net reproductive rate | R0 = sum(lx*mx) | Population trajectory direction |
| EPT index | High EPT = clean water | Stream biomonitoring |
| Nicholson-Bailey | Oscillatory parasitoid-host | Biological control design |
| Thermal performance curve | Bell-shaped T vs rate | Climate vulnerability |

---

## Common Confusion Points

**Density dependence vs density independence**: Density-dependent factors (competition, disease) regulate populations; their per capita effect increases with N. Density-independent factors (frost, drought) affect all individuals regardless of N. Most real populations experience both; density dependence provides the regulatory feedback.

**r vs K is a continuum, not a binary**: r/K selection is a heuristic framework. Real insects exist along a continuum. Periodical cicadas (K-ish: long generation, synchronized emergence) also have huge reproductive events. Honey bees (large colony size, K-ish) have very high reproductive rate per worker.

**Outbreaks are not failures of regulation**: Outbreaks can be the normal dynamic of a well-functioning ecosystem. Spruce budworm outbreaks occur every 40-80 years in boreal forests and are part of the forest succession cycle. Suppressing all outbreaks with insecticide creates older, more vulnerable forests.

**Aquatic insect "pollution tolerance" is about oxygen and organic load**: EPT taxa require high dissolved oxygen and are sensitive to BOD (biological oxygen demand). "Clean water" means unpolluted by organic enrichment + pesticides, not necessarily no nutrients. Eutrophication initially increases some insect groups (chironomids) before crashing diversity.

**Migration vs dispersal**: True migration is directed and relatively predictable. Dispersal is undirected. Many insects described as "migratory" are actually dispersers aided by prevailing winds. The distinction matters for conservation: migratory corridors need protection; dispersal networks are harder to identify.
