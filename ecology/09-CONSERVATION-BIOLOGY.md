# Conservation Biology — Biodiversity Metrics, Fragmentation, Rewilding

## The Big Picture

Conservation biology is a crisis discipline — it applies ecological science to prevent species extinction and maintain functional ecosystems. It combines population ecology, biogeography, evolutionary biology, and social science. The scale of the crisis is unprecedented: background extinction rate ~1 species/million species/year; current rate ~100–1000× background.

```
+---------------------------------------------------------------+
|              CONSERVATION BIOLOGY FRAMEWORK                    |
|                                                                |
|  PROBLEM:  Accelerating biodiversity loss                     |
|            Habitat loss / fragmentation / degradation         |
|            Overexploitation                                    |
|            Invasive species                                    |
|            Pollution                                          |
|            Climate change                                     |
|            (HIPPO acronym: H,I,P,P,O)                        |
|                                                                |
|  TOOLS:                                                        |
|  Protected areas   Species recovery plans                     |
|  Connectivity      Ex situ conservation (zoos, seed banks)   |
|  Rewilding         Environmental law / CITES                  |
|  Restoration       Payment for ecosystem services             |
+---------------------------------------------------------------+
```

---

## Biodiversity Metrics — Measuring What We're Losing

**Alpha, Beta, Gamma diversity** (Whittaker, 1960):

```
ALPHA DIVERSITY (α): Species richness within a local site
  Measured as: species count, Shannon index, Simpson index

BETA DIVERSITY (β): Difference in species composition between sites
  High β: sites differ greatly in species composition
  β = γ / α (approximately)
  Measured as: Jaccard similarity (1 - shared/total), Sørensen, Bray-Curtis

GAMMA DIVERSITY (γ): Total regional species richness
  γ = α × β (conceptually)

FOR CONSERVATION:
  Protecting many small diverse sites (high β diversity) vs
  a few large sites (high α diversity) — the SLOSS debate applied
```

**Species richness vs other metrics:**

| Metric | Formula | What it captures |
|--------|---------|-----------------|
| Species richness (S) | Count of species | Simple, widely used; ignores abundance |
| Shannon diversity (H') | -Σ(pᵢ ln pᵢ) | Richness + evenness; sensitive to rare spp |
| Simpson's diversity (D) | 1 - Σpᵢ² | Probability two individuals are different species; robust |
| Chao1 (richness estimator) | S_obs + (F₁²/2F₂) | Estimates true richness from singletons |
| Functional diversity | Range/dispersion of traits | Ecological function, not just identity |
| Phylogenetic diversity | Total branch length | Evolutionary history; deep diversity |

**Functional diversity** is arguably more important than species richness for ecosystem function. A community of 10 functionally distinct species may provide more ecosystem services than 30 species doing similar things.

**Information theory connection:** Shannon diversity H' = -Σ pᵢ ln(pᵢ) is literally Shannon entropy H from information theory (Claude Shannon, 1948). In information theory, H measures the expected information content of a symbol drawn from a distribution — or equivalently, the uncertainty in predicting the next symbol. In ecology, pᵢ is the proportional abundance of species i. A community where all species are equally abundant maximizes H' (maximum entropy = maximum diversity = maximum uncertainty about which species you'd pick at random). A monoculture has H' = 0 (zero entropy = zero uncertainty = minimum diversity). The maximum possible H' for S species = ln(S) (achieved when all pᵢ = 1/S). Evenness J = H'/ln(S) normalizes to [0,1]. This is exactly the same formalism used in physics (Boltzmann entropy), ML (cross-entropy loss), and compression theory (Huffman coding) — the ecology is just a different application of the same mathematical object.

---

## IUCN Red List — Extinction Risk Categories

```
IUCN CATEGORIES (for species assessment):

EX  EXTINCT: No reasonable doubt last individual is dead
EW  EXTINCT IN THE WILD: Only in captivity/cultivation
CR  CRITICALLY ENDANGERED: Extremely high extinction risk
    (>50% in 10 years/3 generations)
EN  ENDANGERED: Very high risk (>20% in 20 years/5 generations)
VU  VULNERABLE: High risk (>10% in 100 years)
NT  NEAR THREATENED: Close to or likely to qualify for VU
LC  LEAST CONCERN: Not threatened

STATUS BY NUMBERS:
  ~8,400 species CR
  ~16,000 EN
  ~17,000 VU
  Total "threatened" (CR+EN+VU): ~41,000+ of 150,000 assessed
  (only ~10% of described species have been assessed)
```

**Criteria for listing** — based on quantitative thresholds:
- A: Population size reduction (>80% over 10 years = CR)
- B: Geographic range restriction (< 100 km² = CR)
- C: Small population + decline (< 250 mature individuals = CR)
- D: Very small or restricted population
- E: Quantitative extinction probability analysis

---

## Habitat Fragmentation — The Primary Threat

Habitat loss + fragmentation is the leading driver of terrestrial biodiversity decline:

```
FRAGMENTATION EFFECTS:

ORIGINAL LANDSCAPE           FRAGMENTED LANDSCAPE

+------------------+         +----+ +--+  +------+
|                  |         | A  | |B |  |  C   |
|  CONTINUOUS      |    →    +----+ +--+  +------+
|  HABITAT         |         (same total area; very different ecology)
|                  |
+------------------+

CONSEQUENCES:
1. Reduced area (SAR) → fewer species
2. Edge effects:
   - Different microclimate: warmer, drier, windier at edges
   - Edge predators penetrate interior (crows, raccoons, cats)
   - Invasive species penetrate along edges
   - "Edge-sensitive" species lose interior habitat

3. Isolation:
   - Reduced gene flow → inbreeding
   - Lost metapopulation dynamics (no rescue effect)
   - Local extinction not replaced by recolonization

4. Increased vulnerability to stochastic events
   (small, isolated populations)
```

**Edge effects penetration distance:**
- Brown-headed cowbird parasitism: up to 3 km into forest (parasitizes nests)
- Predation pressure: up to 1–2 km
- Microclimate effects: up to 100–300 m
- A 1 km² forest patch → nearly all edge habitat

**Effective area concept** — only interior area (beyond edge effect penetration distance) is true habitat for interior-sensitive species. A 5-hectare forest patch may have zero effective interior area.

---

## Minimum Viable Population and Population Viability Analysis

**Minimum Viable Population (MVP)** — smallest population with >99% probability of persistence for 1000 years (original definition). Rule of thumb: ~1000–5000 individuals for most vertebrates (Shaffer, 1981; Franklin 1980).

**Population Viability Analysis (PVA)** — computer simulation models that calculate extinction probability over time, accounting for:
- Demographic stochasticity (random birth/death)
- Environmental stochasticity (year-to-year variation)
- Catastrophes (periodic low-probability high-impact events)
- Genetic deterioration (inbreeding depression)

**50/500 rule (Franklin 1980):**
- 50 breeding individuals: minimum to avoid inbreeding depression short-term
- 500 breeding individuals: minimum for long-term evolutionary potential
- Now considered conservative; many argue 1000+ needed for viability

---

## Reserve Design — From Theory to Practice

Key principles (informed by island biogeography + metapopulation theory):

```
GENERAL PRINCIPLES:
  Larger reserves are better than smaller (area effect + interior habitat)
  Connected reserves better than isolated (dispersal + metapopulation)
  Single large reserve better than several small (for most taxa)
  Circular reserves better than elongate (less edge/area ratio)
  Reserves close together better than far apart
  Corridors improve connectivity between reserves

GAPS IN PRACTICE:
  Reserves often placed on "leftover" land (economically marginal)
  Not necessarily where biodiversity is highest
  "Biodiversity hotspots" receive priority but overlap poorly with
   current protected areas

PROTECTED AREA COVERAGE (2024):
  Land: ~17% (CBD Aichi targets met; Kunming-Montreal target: 30% by 2030)
  Ocean: ~8% (less than land; critical gaps in high seas)
  Effective protection: only ~2–5% fully protected (no extractive use)
```

**Key biogeographic reserve strategies:**
- **Hotspots** (Myers 1988): ~36 regions with exceptional endemism + threat → concentrate resources
- **Wilderness areas**: Large intact areas with low human impact (boreal, Amazon, Congo)
- **Important Bird Areas (IBAs)**: BirdLife criteria → pragmatic global network
- **Indigenous protected areas**: Recognition that indigenous lands have better biodiversity outcomes in many regions

## Systematic Conservation Planning — Algorithms and Tools

Protect-what's-left (hotspot intuition) is insufficient when conservation resources are limited and targets are specific. Systematic conservation planning (SCP) frames reserve selection as a combinatorial optimization problem:

```
PROBLEM FORMULATION:
  Input: n candidate sites × m biodiversity features (species, habitats)
         c[i] = cost of protecting site i (acquisition + management)
         a[i][j] = representation of feature j in site i (presence/abundance)
         T[j] = target for feature j (e.g., 10% of range protected)

  Objective: minimize Σ c[i] × x[i]   (total cost)
  Subject to: Σ a[i][j] × x[i] ≥ T[j] for all j   (representation targets)
              x[i] ∈ {0, 1}   (binary: protect or not)

  → Integer linear program; NP-hard in general
  → Practical solutions via simulated annealing (Marxan) or ILP solvers
```

**Key tools:**

**Marxan** (Ball & Possingham, 2000) — the dominant SCP tool globally:
- Simulated annealing on the reserve selection objective
- Used to design marine protected area networks, terrestrial reserve systems
- Key feature: spatial clustering penalty (avoid fragmented reserve networks)
- Stochastic → run 100× → summarize selection frequency per site (irreplaceability)

**Complementarity** — the core principle of SCP:
- A site's value depends on what's already protected, not just what it contains
- Site with species already well-represented adds less marginal value
- → Builds in functional redundancy across the reserve network
- Contrast with vulnerability-based scoring (adds high-threat sites regardless of complementarity)

**Gap analysis:**
```
PROCEDURE:
  1. Map distribution of all species/habitats of concern
  2. Map current protected area network
  3. Identify "gaps" — species/habitats with inadequate protected area coverage
  4. Prioritize gap species/habitats for new reserve acquisition

OUTPUTS:
  Proportion of each species range currently protected
  Spatial location of gaps (where to add protection)
  Cumulative protection curves: % target achieved vs % area protected
```

**Irreplaceability and vulnerability** — two axes for prioritization:
- High irreplaceability + high vulnerability = immediate priority (few alternatives + high threat)
- High irreplaceability + low vulnerability = monitor (essential but not yet threatened)
- Low irreplaceability + high vulnerability = lower priority (threatened but alternatives exist)

---

## Rewilding — Restoring Ecological Processes

Rewilding goes beyond protecting what's left — it aims to restore ecological processes and self-regulating ecosystems:

```
CORE REWILDING CONCEPTS:

REWILDING 3Cs (Soulé & Noss, Terborgh):
  1. Cores: Large core protected areas
  2. Corridors: Connectivity between cores
  3. Carnivores: Reintroduce apex predators
  (trophic cascades restore ecosystem function)

PASSIVE REWILDING:
  Remove agricultural pressure; let nature recover
  (European rewilding: abandoned farmland → forest)

TRANSLOCATION / REINTRODUCTION:
  Return locally extinct native species
  Gray wolves to Yellowstone (1995) — transformative trophic cascade
  Beavers to Scotland/England — ecosystem engineers
  European bison to Poland — from 12 animals in 1952

PLEISTOCENE REWILDING (Donlan et al. 2005):
  Controversial proposal: reintroduce proxies for
  Pleistocene megafauna to Americas (horses, camels,
  cheetah analogs, Asian elephants as mammoth proxies)
  Argument: fill functional roles lost ~13,000 years ago
  Controversy: ecosystems have reorganized since then
```

**Rewilding outcomes — Yellowstone (1995 wolf reintroduction):**
- Wolf population: 14 wolves (1995) → ~500 (2020)
- Elk: reduced + behaviorally modified (avoid riparian zones)
- Willows/aspens: recovering in riparian zones
- Beaver: returned (willows = beaver food)
- Songbirds: more diverse in recovered riparian
- But: human conflict, livestock predation, ongoing controversy

---

## CITES and International Conservation Framework

```
CITES (Convention on International Trade in Endangered Species):
  Regulates international wildlife trade
  Appendix I: Banned from commercial trade (most endangered)
  Appendix II: Trade permitted with permits (monitoring)
  Appendix III: Protected in at least one country

  ~40,000 species covered
  Example: Ivory trade ban (Appendix I, African elephant) since 1989

CBD (Convention on Biological Diversity):
  1992 Rio Earth Summit
  Kunming-Montreal Framework (2022): 30×30 target
  (protect 30% of land and ocean by 2030)
  Nagoya Protocol: benefit-sharing from genetic resources

ESA (Endangered Species Act, US 1973):
  "Critical habitat" designation
  Species recovery plans
  Prohibits "take" (harm, harassment) of listed species
  Success stories: bald eagle, gray wolf, peregrine falcon, whooping crane
```

## Climate Change Adaptation in Conservation

Climate change has elevated conservation from static habitat protection toward dynamic, forward-looking management:

```
CORE PROBLEM:
  Species' climate envelopes are shifting poleward and upslope
  Current protected areas were sited for current climate, not future climate
  → Many reserves may become climatically unsuitable for their target species
  → Species need to track shifting climate: poleward ~50 km/decade, upslope ~10 m/decade
  → But landscape fragmentation blocks dispersal

ADAPTATION STRATEGIES:
  ┌─────────────────────────────────────────────────────────────────┐
  │ PASSIVE: reduce other stressors, let species self-adjust        │
  │   Reduce fragmentation (improve matrix permeability)           │
  │   Reduce overexploitation, pollution                           │
  │   → Creates "headroom" for adaptation                         │
  │                                                               │
  │ CONNECTIVITY: facilitate natural dispersal                     │
  │   Climate corridors: route from current → future habitat       │
  │   Stepping stones: intermediate patches for long-distance moves│
  │   → Design for future climate, not current conditions         │
  │                                                               │
  │ MANAGED RELOCATION (assisted migration):                       │
  │   Deliberately move individuals/populations to future habitat  │
  │   High controversy: could introduce new invasive dynamics      │
  │   Best cases: species with very limited dispersal ability      │
  │   (plants, tortoises, freshwater fish above dispersal barriers)│
  │   Examples: Torreya taxifolia (Florida) moved to NC mountains  │
  └─────────────────────────────────────────────────────────────────┘
```

**Climate corridors — design principles:**
```
IDENTIFY:
  Current population locations
  Predicted future suitable habitat (species distribution model under RCP4.5/8.5)
  Least-cost path connecting current → future (graph shortest-path on resistance surface)

RESISTANCE SURFACE:
  Each landscape cell assigned resistance to movement
  (land cover, slope, human infrastructure)
  Least-cost corridor = minimum cumulative resistance path
  Tools: Circuitscape (circuit theory model), Linkage Mapper

TRADEOFFS:
  Short/direct corridors: less land required; more exposed to predation in matrix
  Long/wide corridors: more resilient; more land cost; risk of connecting isolated disease patches
```

**Refugia and microclimate heterogeneity:**
- Cool microrefugia (north-facing slopes, riparian valleys, fog zones) allow persistence during warming
- Identifying and protecting microclimate refugia buys decades of time for slow-dispersing species
- Fine-resolution topographic models now allow refugia mapping at relevant scales

**Triage decision framework:**
```
SPECIES × CLIMATE THREAT MATRIX:
  High climate sensitivity + poor dispersal + no alternative habitat: managed relocation
  High climate sensitivity + good dispersal + connected landscape: corridor priority
  Low climate sensitivity: maintain current reserves; address non-climate threats
  Already past threshold: evaluate ex situ as bridge to future restoration
```

---

## Decision Cheat Sheet

| Conservation question | Tool/concept |
|----------------------|-------------|
| How fragmented is a landscape? | Patch size distribution, connectivity metrics, fragmentation indices |
| What size reserve is needed? | PVA + minimum area requirements + target species needs |
| Which species most at risk? | IUCN criteria (A-E); PVA; EDGE (Evolutionarily Distinct/Globally Endangered) |
| How to restore connectivity | Wildlife corridors, stepping stones; landscape permeability models |
| Prioritize conservation investments | Hotspot mapping; irreplaceability analysis; cost-effectiveness |
| Rewild an area | Core-corridor-carnivore framework; identify missing ecological processes |

---

## Common Confusion Points

**"Protected area" ≠ "effectively protected"** — Many protected areas are "paper parks" — designated but not enforced, with continued hunting, logging, or encroachment. Effective protection requires enforcement capacity, community support, and adequate management resources. ~5% of global protected areas have sufficient management.

**Alpha diversity ≠ conservation value** — A disturbed, exotic-dominated grassland may have higher species richness (alpha diversity) than an intact native prairie — but the latter has higher conservation value (native species, functional diversity, evolutionary history). Raw species counts mislead if native/exotic species aren't distinguished.

**Extinction debt** — After habitat fragmentation, current species richness may *appear* adequate, but species are on a trajectory to extinction — they just haven't died out yet. The delay between habitat loss and species extinction can be decades to centuries. We are already committed to future extinctions from past habitat loss.

**Edge effects make small reserves much worse than they appear** — A 100-hectare reserve sounds substantial. But if the entire area is within 300 m of the edge (which it is for most shapes), there's zero effective interior habitat for edge-sensitive species. Large contiguous reserves are exponentially more effective per unit area.