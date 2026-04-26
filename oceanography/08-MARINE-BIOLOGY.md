# Marine Biology — Planktonic Food Web, Marine Trophic Levels, Coral Reef Ecology, Deep Scattering Layers

## The Big Picture

```
+===========================================================================+
|                   MARINE ECOSYSTEM STRUCTURE                              |
|              From photons to whales — energy flow in the ocean            |
+===========================================================================+
|                                                                           |
|  AUTOTROPHS (PRIMARY PRODUCERS)                                           |
|  Phytoplankton (50 Gt C/yr NPP)  Seagrasses  Kelp  Salt marsh grasses    |
|          │                                                                |
|          ▼ ~10% efficiency at each trophic level                          |
|  HERBIVORES (Trophic Level 2)                                             |
|  Zooplankton (copepods, krill, salps)  Sea urchins  Small fish            |
|          │                                                                |
|          ▼                                                                |
|  PLANKTIVORES (TL 3)                                                      |
|  Small fish: herring, sardine, anchovy, menhaden                          |
|          │                                                                |
|          ▼                                                                |
|  PISCIVORES (TL 4)                                                        |
|  Tuna, cod, large squid, marine mammals                                   |
|          │                                                                |
|          ▼                                                                |
|  APEX PREDATORS (TL 4.5–5)                                                |
|  Sharks, orcas, sperm whales, large tuna                                  |
|                                                                           |
+===========================================================================+
|  PARALLEL LOOP — MICROBIAL LOOP                                           |
|  DOC ← exudation ← phytoplankton                                          |
|  Bacteria → flagellates → ciliates → back to metazoa                      |
|  ~50% of primary production passes through microbial loop                 |
+===========================================================================+
```

---

Marine trophic dynamics map cleanly to information/energy cascades you already know. The 10% trophic efficiency is a multi-stage efficiency loss: each trophic level passes roughly 10% of energy input to the next, exactly as a cascade of lossy amplifiers each with 10 dB loss — the product of n stages is 10⁻ⁿ. The microbial loop is a feedback path that recycles DOC back into the food web, analogous to regenerative feedback in circuits: it increases system efficiency in the sense of recovering energy that would otherwise be lost, but at the cost of retaining carbon in the surface rather than exporting it. Maximum Sustainable Yield (MSY) from logistic population growth (MSY = rK/4 at N = K/2) is the same peak-power-transfer problem: maximum power is extracted from a source when the load matches the source impedance — in ecological terms, when the harvest rate equals half the maximum intrinsic growth rate.

## Primary Producers

### Phytoplankton — Classification and Function

```
MAJOR PHYTOPLANKTON GROUPS:

  DIATOMS (Bacillariophyta):
    Siliceous frustules (SiO₂ outer shell) — intricate geometry
    Size: 5 μm to 2 mm
    Dominant in nutrient-rich, upwelling zones, spring blooms
    ~25% of global primary production
    Sink fast (heavy) → important for biological pump

  COCCOLITHOPHORES (Haptophyta):
    Calcium carbonate plates (coccoliths)
    Size: 5–25 μm
    Dominant in subtropical oligotrophic waters
    Emiliania huxleyi: most abundant calcifier in ocean (forms huge blooms visible from space)
    Important for carbonate pump

  CYANOBACTERIA (Prokaryotes):
    Prochlorococcus: smallest oxygenic photosynthesizer (~0.6 μm)
    Most abundant organism on Earth: ~3×10²⁷ cells, ~100 Gt C biomass globally
    Dominant in ultra-oligotrophic subtropical gyres
    Synechococcus: slightly larger, slightly more nutrient-tolerant
    Trichodesmium: N₂-fixing cyanobacterium → supplies fixed N to tropical ocean

  DINOFLAGELLATES (Dinoflagellata):
    Armored (theca) or naked
    Size: 20–2000 μm
    Some mixotrophic (both photosynthesis and predation)
    HABs (Harmful Algal Blooms): red tides, neurotoxins (saxitoxin, brevetoxin)

  FLAGELLATES (various):
    Nanoflagellates (2–20 μm): often dominant in oligotrophic systems
    Chrysophytes, Prasinophytes: diverse, understudied

PHYTOPLANKTON BLOOM CYCLE:
  Spring: stratification begins, nutrients still available from winter mixing
    → rapid growth (doubling time ~1 day) → bloom
  Summer: nutrients depleted → bloom collapses → oligotrophic summer state
  Fall: wind mixing re-entrains nutrients → secondary bloom possible
  Winter: deep mixing, low light → low growth
```

---

## Zooplankton

```
COPEPODS (Crustacea: Copepoda):
  Most numerically abundant metazoa on Earth
  Size: 0.1–10 mm
  Herbivores (grazing phytoplankton) and carnivores
  Diapause: high-latitude copepods (Calanus spp.) store lipids,
    overwinter at 500–2000 m depth (metabolically dormant)
  Carbon flux: copepod fecal pellets sink rapidly → efficient export pathway

KRILL (Euphausia superba):
  Antarctic krill: 0.5 g each, ~500 million tonnes biomass (~6×10¹⁴ individuals)
  Largest animal biomass on Earth (possibly)
  Filter feeders on phytoplankton/ice algae
  80% of energy supply for penguins, seals, whales, seabirds of Southern Ocean
  DVM (diel vertical migration): ascend to feed at night, descend during day

SALPS AND GELATINOUS ZOOPLANKTON:
  Salps: transparent barrel-shaped filter feeders
  Population explosions in high-bloom conditions (faster population growth than copepods)
  Produce large fecal pellets → efficient carbon export (>5000 m/day sinking rate)
  "Jelly falls" (salp blooms collapsing) → pulse of organic matter to seafloor

JELLYFISHES:
  Scyphozoa (true jellyfish), Ctenophora (comb jellies), Siphonophora (colonial)
  Physalia (Portuguese man-o-war): colony, not individual
  Bloom events increasing (jellyfish blooms correlated with eutrophication, warming)

DIEL VERTICAL MIGRATION (DVM):
  Many zooplankton migrate 100–600 m daily:
    Dawn: descend below thermocline (avoid visual predators in daylight)
    Dusk: ascend to surface epipelagic (feed on phytoplankton)
  Active biological pump: migrants feed at surface → respire CO₂ at depth
  ~15–40% additional carbon export compared to passive sinking
```

---

## Microbial Loop

```
DISCOVERY: Azam et al. (1983) — "The Ecological Role of Water-Column Microbes in the Sea"
  Paradigm shift: previously thought DOC was "lost" to heterotrophy
  Actually: DOC → bacteria → flagellates → ciliates → zooplankton → back to food web

MICROBIAL LOOP STRUCTURE:

  Phytoplankton leak DOC: exudation, sloppy feeding, viral lysis, cell death
    (up to 50% of gross primary production as DOC)
  Heterotrophic bacteria: consume DOC, grow rapidly (0.1–2 day doubling time)
  Bacterivorous nanoflagellates: consume bacteria
  Ciliates: consume nanoflagellates
  Mesozooplankton: consume ciliates

  → Energy repackaged from unedible DOC into particulate form
  → But each trophic transfer loses ~90% (10% efficiency)
  → Net effect: microbial loop RETAINS carbon in surface water
    (vs. large cells/fecal pellets that export it)

VIRAL SHUNT:
  Viruses lyse ~10–50% of bacterial production per day
  Also lyse phytoplankton (cyanophage infecting Prochlorococcus)
  Viral lysis → DOC + small particles (cell fragments)
  → Shortcircuits grazing food chain
  → Diverts more carbon to dissolved/colloid pool → microbial loop
  → Reduces export production (keeps carbon in surface)

BIOGEOCHEMICAL SIGNIFICANCE:
  In oligotrophic gyres: microbial loop dominates (no blooms, no export)
  In eutrophic/upwelling systems: large phytoplankton → short food chains → export
  Polar oceans: hybrid — large diatoms + active microbial loop
```

---

## Coral Reef Ecology

```
CORAL REEF PHYSICS AND CHEMISTRY:

  REEF-BUILDING CORALS:
    Scleractinian corals: aragonite CaCO₃ exoskeleton
    Zooxanthellae (Symbiodinium spp.): dinoflagellate endosymbionts in coral tissue
      Supply 90%+ of coral energy via photosynthesis (coral = obligate photoautotrophy)
      Also: confer color (brown-golden hue)

  CORAL BLEACHING:
    Stress (temperature, light, chemicals) → zooxanthellae expelled
    → white skeleton visible through transparent tissue ("bleached")
    Bleached coral: not dead yet, but dying if stress continues >2–4 weeks
    Recovery: possible if thermal anomaly brief
    Mass bleaching threshold: ~1°C above mean summer maximum for 4+ weeks
    Degree Heating Weeks (DHW) metric: >8 DHW → severe bleaching

  REEF CALCIFICATION:
    Ca²⁺ + 2HCO₃⁻ → CaCO₃ + CO₂ + H₂O
    Calcification rate depends on:
      Temperature (optimal ~26–28°C), aragonite saturation (Ω), light, nutrients

REEF ARCHITECTURE AND ZONES:
  ┌──────────────────────────────────────────────────────────┐
  │ FORE REEF (windward)  REEF CREST    BACK REEF  LAGOON    │
  │ High wave energy       Algal ridge  Patch reefs Seagrass │
  │ Coral buttresses       (coralline   Coral heads Sandy    │
  │ Spur-and-groove        algae)                  bottom    │
  └──────────────────────────────────────────────────────────┘

  Great Barrier Reef: 2,300 km, >2,900 individual reefs, largest biogenic structure
  Coral Triangle (SE Asia): maximum coral biodiversity, 600+ species
  Caribbean reefs: ~70 coral species, heavily stressed by bleaching + crown-of-thorns
```

---

## Fisheries and Trophic Dynamics

### Trophic Level and Energetics

```
10% EFFICIENCY RULE (Lindeman's trophic efficiency):
  ~10% of energy at one trophic level passed to next
  (90% lost to respiration, excretion, uneaten material)

  100 tonnes phytoplankton
    → 10 tonnes zooplankton (TL2)
      → 1 tonne small fish (TL3)
        → 100 kg medium fish (TL4)
          → 10 kg large predator (TL5)

  FISHING IMPLICATIONS:
    1 tonne tuna = consuming 1000 tonnes phytoplankton-equivalent
    Short food chains (phytoplankton → krill → whale) far more efficient
    Fishmeal-fed aquaculture: 4–10 kg feed per kg fish produced

MEAN TROPHIC LEVEL OF FISHERIES CATCH:
  Global catch TL has DECLINED from ~3.3 to ~3.1 since 1950
  "Fishing down the food web" (Pauly et al. 1998): apex predators depleted first,
  then prey species, then planktivores, then invertebrates
  → Sequential depletion of each trophic level

MAXIMUM SUSTAINABLE YIELD (MSY):
  MSY = 0.5 × K × r/4   (simplified logistic model)
  where K = carrying capacity, r = intrinsic growth rate
  At 50% K: population growth maximized → highest sustainable harvest
  Reality: multispecies, variable environment, poorly known K and r
  Most major fisheries are at or beyond MSY (FAO: 35% overfished, 57% maximally fished)
```

---

## Marine Mammals

```
CETACEA — evolutionary return to sea:
  Artiodactyla ancestors → pakicetids → ambulocetids → fully aquatic → modern
  Odontoceti (toothed): echolocation, hunt fish/squid individually
  Mysticeti (baleen): filter feeders on krill/copepods/small fish

SPERM WHALE DIVE:
  Maximum recorded: 2,992 m depth, 138 min
  Echolocation clicks: loudest biological sound (~230 dB re 1 μPa)
  Spermaceti organ: lens that focuses sound beam; may regulate buoyancy via
    temperature-controlled wax (solid vs. liquid = denser vs. less dense)
  Prey: Architeuthis (giant squid) at depth — evidence from stomach contents

CETACEAN ACOUSTIC COMMUNICATION:
  Humpback whale songs: 15–30 min structured compositions, evolving annually
    All males in a population sing the same song (cultural transmission)
    Songs detected via SOFAR channel thousands of km away
  Sperm whale codas: structured click sequences, culturally transmitted
    Different "clan dialects" in Pacific sperm whales (similar to human language dialects)
  Blue whale 52-Hz call: previously thought from unidentified species
    ("52-Hz whale" — single individual with anomalous frequency; identified as hybrid)

MARINE MAMMAL THERMOREGULATION:
  Blubber: thermal insulation (~20 cm thick in bowhead whale)
  Countercurrent heat exchange: arteries surrounded by veins in flippers
    → heat transferred from outgoing warm blood to incoming cold blood
    → flippers near ambient temperature while core stays warm

POPULATION RECOVERY POST-WHALING:
  North Atlantic right whale: ~500 remaining (critically endangered)
  Bowhead: recovered to ~10,000+ from near-extinction
  Humpback: recovered from ~10,000 to ~80,000+ globally
  Blue whale: ~10,000–25,000 (pre-whaling: 300,000+)
```

---

## Deep Scattering Layer (DSL)

```
DISCOVERY:
  WWII sonar operators detected "false bottom" at 200–800 m depth
  Moved UP at night, DOWN during day
  Initially feared to be submarines → hence wartime interest
  Identified: dense layer of mesopelagic organisms performing DVM

DSL COMPOSITION:
  Myctophids (lanternfish): ~90% of total mesopelagic fish biomass
    Swim bladders → strong acoustic backscatter at 12–120 kHz
    ~1 billion tonnes biomass (10× estimated before recent surveys)
  Euphausiids (krill): strong scatterers
  Siphonophores: large gas-filled floats → very strong scatter (38 kHz)
  Mesopelagic squid: abundant, poorly studied

GLOBAL SIGNIFICANCE:
  Myctophids alone: ~1–10 billion tonnes wet weight biomass (contested, large uncertainty)
  They consume ~10% of surface primary production
  Active biological pump: DVM + respiration at depth = ~15–40% of passive flux
  Carbon export: 0.08–1 GtC/yr via active transport (vs. ~10 GtC/yr passive sink)

ACOUSTIC OBSERVATION:
  Echosounders (38 kHz, 120 kHz, 200 kHz) on research vessels
  Multifrequency analysis → distinguish species by acoustic resonance
  120 kHz most commonly used for fisheries/ecology surveys
  Acoustic Doppler Current Profiler (ADCP): uses DSL as a passive current meter
    (Track Doppler shift of scatterer motion → infer water velocity)
```

---

## Polar Marine Ecosystems

```
ARCTIC:
  Sea ice ecosystem: ice algae (Melosira, Fragilariopsis) grow under sea ice in spring
  Primary productivity concentrated in brief summer (24-hr light)
  Arctic cod (Boreogadus saida): central link between copepods/krill and seals/narwhals
  Rapid change: Arctic sea ice loss → profound ecosystem reorganization

ANTARCTIC:
  Sea ice ecosystem + open ocean phytoplankton bloom
  Euphausia superba (Antarctic krill): keystone species
  Iron-limited Southern Ocean: large nutrients, low productivity
  except near islands, polynyas, ice edges (natural Fe fertilization)
  Toothfish (Dissostichus eleginoides, "Chilean sea bass"): slow-growing, heavily fished

ICE EDGE PRODUCTIVITY:
  Spring ice melt → stratification → ideal bloom conditions
  "Green belt" around retreating sea ice edge
  Both Arctic and Antarctic — highly productive transition zones
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What limits phytoplankton? | Nutrients (N, P, Fe), light, grazing; varies by region and season |
| What is the microbial loop? | DOC → heterotrophic bacteria → flagellates → ciliates → zooplankton; retains C in surface |
| What are HNLC regions? | High Nutrient, Low Chlorophyll — Fe-limited (Southern Ocean, equatorial Pacific) |
| What causes coral bleaching? | Thermal stress expels zooxanthellae symbionts; threshold ~1°C above summer max for >4 wk |
| What is "fishing down the food web"? | Sequential depletion of higher TL species forces fisheries to target lower trophic levels |
| What is the DSL? | Deep Scattering Layer — dense mesopelagic organisms (mainly myctophids) performing DVM |
| Why are krill so important? | Bottom of Southern Ocean food web — supports almost all large fauna there |
| What is the active biological pump? | DVM carries organic carbon to depth via respiration (vs. passive particle sinking) |

---

## Common Confusion Points

**Net vs. gross primary production**: Gross primary production (GPP) = total photosynthesis. Net primary production (NPP) = GPP − autotrophic respiration. In marine ecosystems, GPP ≈ 100 GtC/yr, NPP ≈ 50 GtC/yr (half lost to phytoplankton respiration). Export production (below 100 m) ≈ 10 GtC/yr.

**Zooplankton vs. phytoplankton**: Both are plankton (passively drifting). Phytoplankton = photosynthetic (plant-like). Zooplankton = heterotrophic (animal-like). Some dinoflagellates do both (mixotrophic). The distinction is metabolic, not taxonomic.

**Coral bleaching ≠ coral death (immediately)**: Bleached corals are stressed, not dead. They lose energy income (zooxanthellae-derived) and begin consuming lipid reserves. Recovery occurs if thermal anomaly subsides quickly. Prolonged bleaching (>4–6 weeks) → death. Mass bleaching events are occurring more frequently and with insufficient recovery time between events.

**Trophic efficiency is not fixed at 10%**: The 10% rule is an average. Actual transfer efficiencies range from 2% to 20% depending on organism type, temperature, food quality. Gelatinous organisms (salps) can have higher transfer efficiencies. Deep-sea food webs may operate at lower efficiency due to cold temperatures.

**Baleen whale feeding isn't filtering seawater randomly**: Baleen whales don't swim with mouths open filtering all water. They target dense krill aggregations — lunge-feeding (rorquals like blue and fin whales), skim-feeding (right whales), benthic-feeding (gray whales). Krill aggregate in patches of 10,000+ individuals/m³, and whales target these patches efficiently. Blue whales consume ~3.6 tonnes of krill per day during summer feeding season.

## Marine Invasive Species

Invasive species are among the most significant human-caused perturbations to marine ecosystems, primarily vectored by ballast water discharge from global shipping.

```
BALLAST WATER PROBLEM:
  Ships take on ballast water at port of origin, discharge at destination
  ~10 billion tonnes of ballast water transferred globally per year
  Contains: ~7,000 species of microorganisms, larvae, plankton per voyage
  IMO BWM Convention (2004, in force 2017): requires ballast water treatment
  (filtration + UV or chemical disinfection) — implementation still patchy

MAJOR INVASIONS:

  LIONFISH (Pterois volitans/miles) in W. Atlantic / Caribbean:
    Native: Indo-Pacific (Red Sea to Pacific)
    Vector: aquarium trade releases, Florida 1985–1992
    Spread: entire US East Coast, Bermuda, Gulf of Mexico, Caribbean by 2009
    Impact: ~65% prey fish decline on invaded reefs within 5 weeks of arrival
      (lionfish have no learned predator avoidance in Atlantic fish)
    No natural predators in Atlantic; some groupers may learn to eat them
    Control: commercial harvest, SCUBA culling — neither ecologically sufficient

  CAULERPA TAXIFOLIA in Mediterranean (1984 Monaco):
    Toxic alga escaped from Monaco Oceanographic Museum aquarium
    Covered ~30,000 ha of Mediterranean seafloor by 1997
    Outcompetes native seagrass (Posidonia), mussels, other benthic fauna
    Eradicated from California (found 2000, response within weeks, chlorine)
    Still established in Mediterranean after failed eradication attempts

  COMB JELLY (Mnemiopsis leidyi) in Black Sea:
    Native: US East Coast estuaries
    Introduced 1982 via ballast water
    By 1989: 500 million tonnes biomass in Black Sea (~10× all fish biomass)
    Consumed anchovy eggs and larvae → anchovy fishery collapsed
    Partially controlled by accidental introduction of Beroe (its predator)

  ZEBRA / QUAGGA MUSSELS (Dreissena) in North American freshwater:
    Ballast water from Ponto-Caspian region; Great Lakes since 1988
    Filter phytoplankton → reduced zooplankton → food web collapse
    Clog water intake pipes → billions in infrastructure damage
    Now in most major river systems east of Rockies; westward spread ongoing

MANAGEMENT:
  Prevention >> control: ballast water treatment mandated but compliance mixed
  Early detection networks: eDNA monitoring at ports
  Physical removal: effective only at very early stage (Caulerpa CA success)
  Biological control: rarely viable in marine systems (can't contain the predator)
```
