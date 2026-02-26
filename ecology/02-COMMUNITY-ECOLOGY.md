# Community Ecology — Interactions, Keystone Species, Trophic Cascades

## The Big Picture

A community is the set of species coexisting in a place, connected by interactions. The interactions range from predation (one benefits, one harmed) through competition (both harmed) to mutualism (both benefit). Understanding how these interactions shape community structure — who's present, at what abundance — is the core question of community ecology.

```
+---------------------------------------------------------------+
|           SPECIES INTERACTION MATRIX                           |
|                                                                |
|  INTERACTION    EFFECT A  EFFECT B   EXAMPLE                  |
|  ------------   --------  --------   ----------------------   |
|  Predation/     +         -          Wolf-elk, lion-zebra     |
|  Parasitism/                         (consumer-victim)        |
|  Herbivory                                                     |
|                                                                |
|  Competition    -         -          Two species, same niche  |
|  (interspecific)                                               |
|                                                                |
|  Mutualism      +         +          Mycorrhizae-plant,       |
|                                      bee-flower, cleaner fish  |
|                                                                |
|  Commensalism   +         0          Epiphytes on trees,      |
|                                      cattle egrets with cows  |
|                                                                |
|  Amensalism     0         -          Allelopathy (black       |
|                                      walnut chemical)         |
+---------------------------------------------------------------+
```

---

## Competitive Exclusion and Coexistence

**Competitive Exclusion Principle** (Gause, 1934): Two species competing for the same limiting resource cannot coexist at stable equilibrium — one will always exclude the other.

```
LOTKA-VOLTERRA COMPETITION:

dN₁/dt = r₁N₁(K₁ - N₁ - α₁₂N₂)/K₁
dN₂/dt = r₂N₂(K₂ - N₂ - α₂₁N₁)/K₂

α₁₂ = competition coefficient: effect of one individual of species 2
       on growth rate of species 1 (relative to intraspecific competition)

COEXISTENCE CONDITION:
  α₁₂ × α₂₁ < 1

  Each species inhibits itself more than it inhibits the other
  → STABLE COEXISTENCE (both species persist)

  If α₁₂ × α₂₁ > 1:
  → Unstable equilibrium; one species excludes other depending on
    initial conditions
```

**Game theory connection:** The competition coefficients α₁₂ and α₂₁ are exactly payoff matrix entries for a two-player symmetric game. Stable coexistence (α₁₂α₂₁ < 1) corresponds to a Nash equilibrium where both species persist — neither can increase fitness by "defecting" (going to zero). Competitive exclusion (α₁₂α₂₁ > 1) is the prisoner's dilemma outcome: the system converges to a corner (one species wins) with the outcome depending on initial conditions. The unstable equilibrium at the interior point (both present) is the knife-edge — any perturbation sends the system to one corner or the other.

**Resource partitioning** — coexistence mechanism: species use different parts of the resource spectrum. MacArthur's warblers: five species of wood warbler coexist in one spruce tree by foraging in different zones (top, middle, bottom, outside, inside branches).

**Niche differentiation** — Tilman (1982) resource ratio theory: two species can coexist if each is a superior competitor for a different limiting resource, AND if their optimal resource ratios differ. Commonly demonstrated with phytoplankton and nutrients.

---

## Predator-Prey Community Dynamics

Beyond Lotka-Volterra basics:

**Top-down vs bottom-up control:**

```
TOP-DOWN (trophic cascade):
  Predators control herbivore density
  → Low herbivore density → plants abundant

BOTTOM-UP (nutrient/energy limitation):
  Plant productivity limits herbivore density
  → Herbivore density limits predator density

MOST SYSTEMS: Both operate simultaneously
Relative importance varies by ecosystem type:
  Terrestrial: often bottom-up dominant
  Freshwater lakes: often top-down dominant
  Marine: complex, context-dependent
```

---

## Keystone Species

Paine (1969): A keystone species has disproportionately large effects on community structure relative to its biomass. Its removal causes drastic community reorganization.

```
CLASSIC EXAMPLE: Sea star (Pisaster ochraceus) + intertidal community
  Sea star eats mussels (Mytilus) preferentially
  Without sea star: mussels competitively dominate, displace other species
  → Community diversity collapses from 15+ species to near-monoculture

  Paine experimentally REMOVED sea stars → mussel takeover
  → Coined "keystone predator"
  → Keystone: small removal → disproportionate community change
```

**Types of keystone species:**

| Type | Mechanism | Example |
|------|-----------|---------|
| Keystone predator | Suppresses dominant competitor | Sea star, wolf, shark |
| Ecosystem engineer | Physically modifies habitat | Beaver (creates wetlands), elephant (opens forest), prairie dog (burrows) |
| Keystone mutualist | Provides critical service | Fig trees (figs + wasps), pollinators, mycorrhizal fungi |
| Keystone prey | Critical food source for many predators | Salmon, krill, herring |

**Identifying keystones** — not always obvious until removal. Functional redundancy vs fragility: is one species uniquely doing what it does, or can other species substitute? Keystone status depends on context (some predators are keystones in some habitats, not others).

---

## Trophic Cascades

Trophic cascade = predator → prey → plant chain of indirect effects propagating down through food web:

```
WOLF-ELK-ASPEN CASCADE (Yellowstone):

WITHOUT WOLVES (1926-1995):          WITH WOLVES (1995-present):
Elk: abundant, tame                  Elk: fewer + behavioral fear
Willows/Aspens: overbrowsed          Willows/Aspens: recovering
Stream banks: eroded                 Stream banks: stabilizing
Songbirds: few                       Songbirds: increasing
Beaver: rare (no willow)             Beaver: returning

The cascade even changed RIVERS:
  More riparian vegetation → bank stabilization
  → Channel narrowing + meandering
  → "Wolves changed rivers" (Ripple & Beschta)
```

**Behavioral cascade** — indirect effects through fear (landscape of fear), not just direct predation. Elk change where they browse when wolves are present → release of vegetation in risky areas (steep terrain, riparian zones) even without high predation rates.

**Marine trophic cascade — Orcas and kelp forests:**
```
ORCA → SEA OTTER → SEA URCHIN → KELP FOREST

1970s-90s: Orcas shifted to eating sea otters (prey switching when whales depleted)
→ Sea otter decline → sea urchin population explosion
→ Sea urchins overgraze kelp → "urchin barren" (near-desert seafloor)
→ Cascade from apex predator to primary producer
```

---

## Food Webs and Complexity

```
SIMPLE FOOD CHAIN:           REAL FOOD WEB:
                              (simplified)
Plant → Herbivore →          Oak → Caterpillar → Chickadee
Predator → Top predator      Oak → Aphid → Ladybird
                              Oak → Squirrel → Hawk
                              Grasshopper → Frog → Snake → Hawk
                              Caterpillar → Parasitic wasp
                              Bacteria → Earthworm → Robin

FOOD WEB PROPERTIES:
  Connectance C = L / S²  (L = links; S = species richness)
  Linkage density = L/S   (average links per species)
  Omnivory: species feeding at multiple trophic levels
  (complicates clean trophic level assignments)
```

**Graph-theoretic analysis:** A food web is a weighted directed graph: adjacency matrix A where A[i,j] = interaction strength from j to i (nonzero if j eats i or is eaten by i). Standard graph metrics apply directly:
- Connectance C = L/S²: link density normalized by possible links (like graph density)
- Compartmentalization: modularity (Q) of the community structure — highly modular webs have block-diagonal interaction matrices
- Trophic level: fractional trophic level = 1 + mean trophic level of prey (recursive; solved by linear system)
- Spectral analysis: the dominant eigenvalue of the community matrix (Jacobian at equilibrium) determines local stability — if any eigenvalue has positive real part, equilibrium is unstable
- May's result: for random matrices with connectance C and average interaction strength s, stability requires s√(SC) < 1 (the "complexity-stability" bound)

**Complexity and stability debate:**
- May (1973): random food webs — MORE complex (more species, more connections) → LESS stable (mathematics)
- Real food webs: seem to be stable at high complexity — suggests non-random, selected structure
- Keystone structure, compartmentalization, interaction strength distributions matter more than raw connectance

---

## Succession in Community Context

Communities change over time (→ covered in detail in 05-SUCCESSION-STABILITY.md). Clements (1916): deterministic, convergent succession toward a stable "climax." Gleason (1926): individualistic — species respond independently to environment; no deterministic endpoint. Modern view: mostly Gleasonian, with some community-level predictability.

---

## Decision Cheat Sheet

| Community observation | Ecological interpretation |
|-----------------------|--------------------------|
| Single species dominates after removal of one species | Keystone predator or dominant competitor removed |
| Vegetation recovering in areas of predator reintroduction | Trophic cascade (behavioral + consumptive) |
| Two similar species segregate in different microhabitats | Character displacement / niche partitioning (coexistence mechanism) |
| Species diversity highest with intermediate predation | Keystone predator maintains diversity by suppressing dominant |
| Introduced predator collapses native prey community | Naive prey (no evolutionary history with predator) |
| Plant diversity increases after fire removes dominant grass | Intermediate disturbance; competitive dominant suppressed |

---

## Common Confusion Points

**Keystone ≠ most numerous or most biomass** — A keystone species typically has *below-average* biomass but *above-average* impact. Sea stars were <1% of intertidal biomass. The "keystone" metaphor: the small stone at the arch's apex that holds the whole arch together.

**Competitive exclusion vs character displacement** — Competitive exclusion eliminates one species. Character displacement is the evolutionary response to competition: species *diverge* in morphology/behavior to reduce niche overlap → coexistence. Darwin's finches on Galápagos show character displacement in beak morphology.

**Food chain length is limited by energy** — Why aren't there 20-level food chains? Energy loss ~90% per trophic level. At level 10, you'd have 10^-9 of original energy — too little to support a population. Also: longer chains are mathematically less stable (perturbations amplify).

**Trophic levels are not discrete** — Omnivores feed at multiple levels (bear eats salmon, berries, rodents). Trophic level = average position in the food web. Typically expressed as fractionated numbers (e.g., trophic level 2.5 for an omnivore). The clean "1st producer → 2nd herbivore → 3rd predator" is useful but oversimplified.