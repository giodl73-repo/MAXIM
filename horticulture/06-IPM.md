# Integrated Pest Management (IPM)

## The Big Picture

IPM is a decision-making framework for pest control that uses ecological principles to minimize economic damage while reducing reliance on chemical controls. The underlying logic is systems thinking: pests exist in ecosystems, and managing those ecosystems is more durable than individual interventions.

```
THE IPM PYRAMID (hierarchy of interventions):

  +--------------------------+
  |   CHEMICAL (last resort) |   Pesticides; only when all else fails
  +--------------------------+
  +------------------------------+
  | MECHANICAL / PHYSICAL        |   Exclusion, traps, steam sterilization
  +------------------------------+
  +------------------------------------+
  | BIOLOGICAL CONTROL                 |   Predators, parasitoids, pathogens
  +------------------------------------+
  +------------------------------------------+
  | CULTURAL / PREVENTIVE                     |   Resistant varieties, sanitation,
  | (foundation; always operating)            |   crop rotation, timing, habitat
  +------------------------------------------+

PHILOSOPHY:
  Not "zero pest" (impossible at practical cost).
  Goal: keep pest population below the economic threshold.
  Pests are managed, not eradicated.
  Chemical controls are tools of last resort, not first response.
```

---

## Economic Threshold Concept

The quantitative core of IPM is the economic threshold — the pest density at which control is economically justified:

```
KEY LEVELS:
  Economic Injury Level (EIL):
    The pest density at which crop damage cost = control cost.
    Above EIL: damage exceeds cost to control → control justified.
    Below EIL: control cost exceeds damage avoided → don't spray.

  Economic Threshold (ET) / Action Threshold:
    Pest density at which you must act to prevent reaching EIL.
    ET < EIL (you act before you reach the injury level).
    The gap is the "safety margin" — accounts for time between
    decision and treatment effectiveness.

  General Equilibrium Position (GEP):
    The average pest density in the absence of control.
    Below ET: no action needed (natural regulation sufficient).
    Above ET: endemic problem requiring management.

DIAGRAM:
  Population
  density
       |              EIL ---------------------
       |              ET - - - - - - - - - - --  <- Act here
       |         /\
       |        /  \      /\
       |       /    \    /  \
  GEP |______/______\__/____\_________
       |
       +--------------------------------> Time

  ACTION: When population trajectory will exceed ET → apply control.
  GOAL: Keep population below EIL, using ET as early warning.
```

### Economic Thresholds in Practice

```
EXAMPLE THRESHOLDS (illustrative, vary by region and crop):
  Western corn rootworm on corn: 1 beetle per plant OR 0.5 rootworms/plant on previous year's corn
  Aphids on lettuce: 100 aphids per 100 plant inspection (at harvest approach)
  Two-spotted spider mite on strawberry: 5–10 mites per leaflet (mid-summer)
  Colorado potato beetle: 0.5 small larvae per plant (at egg hatch)
  Tomato fruitworm (Heliothis): 1 egg or small larva per 10 plants

THRESHOLD REFINEMENT:
  Temperature-based models: pest development is temperature-dependent.
  Degree-day accumulation predicts when eggs hatch, larvae emerge, adults fly.
  More accurate than calendar timing.
  EXAMPLE: Codling moth in apples.
    Biofix = first adult trap catch.
    From biofix, accumulate degree-days (base 10°C).
    250 DD: first egg hatch → apply larvicide.
    500 DD: peak egg hatch → second application if needed.
  Trap catch data + degree-day model → precision timing.
```

---

## Scouting Protocols

IPM requires data, and data comes from scouting:

```
SCOUTING OBJECTIVES:
  1. Determine if pest is present.
  2. Estimate pest population density.
  3. Identify life stage (eggs, larvae, adults have different thresholds).
  4. Assess natural enemy activity (are beneficials already controlling?).
  5. Record for trend analysis (are populations increasing or decreasing?).

SAMPLING METHODS:
  Sequential sampling: sample until you can make a decision.
    Stop if pest count is clearly above or below ET.
    More efficient than fixed-size sample when pest density is extreme.

  D-Vac (vacuum sampler): physical vacuum collection of insects from plants.
    Most accurate for small, mobile insects on foliage.

  Sticky traps: yellow/blue/white catches flying insects.
    Yellow: aphids, whiteflies, fungus gnats.
    Blue: thrips (preferentially attracted).
    Pheromone: species-specific lure for moth/beetle monitoring.
    Traps for monitoring, not control.

  Leaf inspection: count mites, aphids, eggs per leaf.
    Sample pattern: systematic (every Nth plant, Nth row).
    Sample size: typically 10–50 plants per field.

RECORD KEEPING:
  Date, location, crop stage, pest species, life stage, density.
  Compare to same time previous years.
  Plot counts over time to see trajectory (accelerating or declining?).
  IPM decision is about trajectory, not just current density.
```

---

## Cultural Controls

Cultural controls operate at the ecosystem level — they alter the environment to make it less suitable for pests:

```
RESISTANT VARIETIES:
  The most cost-effective pest management tool.
  Mechanism: physical barriers (thick cuticle, trichomes, waxy coating),
             chemical deterrents (secondary metabolites), tolerance.
  Examples:
    Aphid-resistant lettuce (most commercial varieties have resistances)
    Nematode-resistant tomato rootstocks (Mi gene for root-knot nematode)
    Scab-resistant apple cultivars (Vf gene — reduces fungicide requirement 70%)
    Disease-resistant: almost all modern vegetable cultivars carry
    multiple disease resistances (look for letters after variety name:
    V=Verticillium, F=Fusarium, N=nematodes, A=Alternaria, T=TMV).

CROP ROTATION:
  Moving crops to different fields breaks pest/host continuity.
  Most effective for: soilborne pathogens, nematodes, soil insects.
  Rule: minimum 2-year break between same crop family.
  Exception: highly mobile pests (aphids, whiteflies) are NOT managed by rotation
  (they fly in from neighboring fields).
  Corn rootworm: corn rotation resistance biotype has evolved —
  rootworm now lays eggs in soybean fields as an adaptation.

SANITATION:
  Remove crop debris immediately after harvest (destroys overwintering sites).
  Bury or compost; do not leave in-field.
  Remove volunteer plants (often alternate hosts for viruses).
  Roguing: remove individual infected plants before they spread disease.
  Effective for: powdery mildew, botrytis, many bacterial diseases.

PLANTING DATE MANIPULATION:
  Plant outside the pest's most damaging window.
  Cabbage maggot: plant early (cold) or after peak fly emergence.
  Wheat Hessian fly: "fly-free date" — plant after fly has laid eggs
  (eggs die without a host; late-planted wheat avoids damage).
  Aphid-vectored viruses: plant early in season before aphid populations build.

TRAP CROPS:
  Plant a small area of highly attractive crop to concentrate pests.
  Then treat (or destroy) the trap crop before pests move to main crop.
  Example: Blue Hubbard squash as trap for cucumber beetles near melon fields.
  Example: Mustard border rows for Lygus bugs in strawberry fields.
```

---

## Biological Control

### Classical Biological Control

```
CLASSICAL (IMPORTATION) BIOCONTROL:
  Target: exotic (introduced) pests that have arrived without
          their natural enemies from their home range.
  Method: find the pest's natural enemies in its native range;
          import them; establish them in the new environment.

FAMOUS EXAMPLES:
  Cottony cushion scale (Icerya purchasi) introduced from Australia
  to California citrus (1868). Devastated industry.
  Solution (1888): ladybeetle Rodolia cardinalis imported from Australia.
  Control: complete, spectacular, within 2 years. Still operating.
  First and most celebrated biocontrol success.

  Alligator weed (Alternanthera philoxeroides): flea beetle from Argentina
  (Agasicles hygrophila) released in SE US; major control achieved.

REQUIREMENTS FOR SUCCESS:
  Agent must be highly specific to target pest.
  Agent must be able to establish and survive.
  Agent must reduce pest below ET.
  Risk assessment: no effect on non-target species.
  Regulation: extensive host-specificity testing before release.
```

### Augmentative Biological Control

```
AUGMENTATIVE BIOCONTROL:
  Mass-rear beneficial organisms; release to augment natural populations.
  Does not depend on establishment — released organisms do the job
  and need not survive permanently.

INUNDATIVE RELEASE: Large numbers; rapid control; like a biopesticide.
INOCULATIVE RELEASE: Smaller numbers; establish and multiply; slower.

KEY AGENTS:
  Trichogramma spp. (parasitoid wasps, ~0.5mm):
    Parasitize lepidopteran (moth/butterfly) eggs.
    50+ species; host range varies.
    Applied by helicopter over corn fields (inundative).
    ~30% of biological insecticide market in some regions.

  Phytoseiulus persimilis (predatory mite):
    Predator of two-spotted spider mite (Tetranychus urticae).
    Applied as sachets hung in greenhouse; disperses and feeds.
    Standard practice in European greenhouse tomato/cucumber production.
    Key limitation: does not work below ~18°C or at low humidity.
    Amblyseius californicus: alternative species; works at lower temperatures.

  Bacillus thuringiensis (Bt):
    Soil bacterium producing crystal proteins (Cry proteins).
    Cry proteins toxic to specific insect orders; essentially non-toxic to others.
    Bt var. kurstaki (Btk): caterpillars (Lepidoptera).
    Bt var. israelensis (Bti): mosquito and fungus gnat larvae (Diptera).
    Bt var. tenebrionis (Btt): Colorado potato beetle larvae (Coleoptera).
    Applied as spray; must be ingested; UV-degraded (reapply after rain/sunlight).

  Steinernema and Heterorhabditis (entomopathogenic nematodes, EPNs):
    Soil-dwelling nematodes that host-seek insects.
    Carry symbiotic bacteria (Xenorhabdus, Photorhabdus) that kill the host.
    Applied as drench to moist soil.
    Soil pests: fungus gnat larvae, vine weevil, black vine weevil, cutworms.
    Temperature window: 12–30°C; moist soil essential.
```

### Conservation Biological Control

```
CONSERVATION BIOCONTROL:
  Create and maintain habitat for natural enemies already present.
  Don't disrupt them with pesticides; give them what they need.

STRATEGIES:
  Insectary strips: strips of flowering plants in fields.
    Provide: pollen and nectar (food for adult parasitoids and predators).
    Species: phacelia, buckwheat, sweet alyssum, dill, cilantro.
    Effect: increases parasitism rates of nearby pests.

  Beetle banks: raised, unplowed strips with dense grass.
    Overwintering habitat for ground beetles and spiders.
    Ground beetles emerge in spring, feed on weed seeds and pest eggs.

  Reduce pesticide disruption:
    Broad-spectrum insecticides kill natural enemies as effectively as pests.
    After disruption: pest populations rebound fast (no natural enemies);
    natural enemy populations recover slowly.
    The "pesticide treadmill": use pesticide → kill natural enemies → pest resurgence → need more pesticide.
```

---

## Mechanical and Physical Controls

```
ROW COVERS (floating row covers, agri-fabric):
  Spunbonded polypropylene placed directly over crops.
  Excludes: flying insects, aphids, whiteflies, cucumber beetles, carrot fly.
  Transmits: light, water, air.
  Limitation: must be removed for pollination of fruiting crops.
  Used for: carrots, brassicas (cabbage maggot), early strawberries.

STICKY TRAPS:
  Yellow sticky cards: aphids, whiteflies, leafminers, fungus gnats.
  Used for: monitoring (count insects/card/week) AND low-level control.
  Limitations: catch beneficial insects indiscriminately; high pest pressure
    requires many cards; impractical for field scale.

EXCLUSION NETTING:
  Insect-proof mesh (0.9mm or finer) over structures.
  Used for: caterpillar-free Brassica production, fruit fly exclusion.
  High cost; high effectiveness.

STEAM STERILIZATION:
  Apply steam (100°C) to soil before planting.
  Kills: soilborne pathogens, weed seeds, nematodes, soil insects.
  Depth: 30cm or more with proper injection.
  Used in: greenhouse soils, nursery beds.
  Not in-field (too expensive; impractical at scale).
  Replaced methyl bromide for many greenhouse applications.

COPPER TAPE / BARRIERS:
  Copper releases Cu²⁺ ions that deter slugs and snails.
  Used: around raised beds, pots.
  Effective for low-level slug management; not for high infestations.
```

---

## Chemical Controls

### When and How

```
IPM CHEMICAL CONTROL PRINCIPLES:
  1. Only when pest density is at or above ET (not preemptive).
  2. Use the most selective pesticide available.
  3. Rotate modes of action (IRAC/FRAC numbers) to prevent resistance.
  4. Apply at the most susceptible life stage.
  5. Protect beneficials: spray at low-bee-activity times; use spot treatments.
  6. Record applications for resistance tracking.
```

### Pesticide Mode of Action (MOA)

The Insecticide Resistance Action Committee (IRAC) assigns group numbers to MOAs:

```
IRAC MOA GROUPS (key ones):
  Group 1A: Organophosphates — acetylcholinesterase inhibition
  Group 1B: Carbamates — acetylcholinesterase inhibition
  Group 2A: Organochlorines — GABA-gated Cl- channel blockers
  Group 3A: Pyrethroids — voltage-gated sodium channels
  Group 4A: Neonicotinoids — nicotinic acetylcholine receptors
    (imidacloprid, clothianidin, thiamethoxam)
    CONTROVERSY: systemic; expressed in pollen/nectar; bee toxicity concerns.
  Group 5: Spinosyns (spinosad, spinetoram) — nicotinic receptor + GABA
    Relatively selective; low mammalian toxicity; OMRI-listed (organic).
  Group 6: Avermectins (abamectin, emamectin) — glutamate-gated Cl- channels
  Group 7: Juvenile hormone analogues
  Group 11: Bacillus thuringiensis proteins (Cry toxins)
  Group 22: Indoxacarb — voltage-gated sodium channels (different site)
  Group 28: Diamides (chlorantraniliprole) — ryanodine receptors
    Very selective; low toxicity to beneficials; no resistance yet widespread.
    Premium price but excellent fit in biocontrol programs.

FUNGICIDE MOA (FRAC):
  Group 1: MBC fungicides (benzimidazoles) — tubulin
  Group 3: DMI/SBI fungicides (triazoles, imidazoles) — ergosterol
  Group 7: SDHI fungicides — succinate dehydrogenase (relatively new)
  Group 11: Qo inhibitors (strobilurins) — cytochrome bc1 complex
  Group M: Multi-site (copper, sulfur, captan) — no specific resistance
```

### Resistance Management

```
RESISTANCE MANAGEMENT PRINCIPLE:
  Each exposure to a pesticide selects for survivors with resistance.
  Rotating MOA prevents resistance from building in any one pathway.

  WRONG: Apply pyrethroids all season.
         Year 1: 90% kill. Year 3: 40% kill. Year 5: 5% kill.
         Pyrethroid-resistant population has been selected.

  RIGHT: Rotate:
         Application 1: Pyrethroid (Group 3A)
         Application 2: Organophosphate (Group 1A)
         Application 3: Spinosad (Group 5)
         Application 4: Diamide (Group 28)
         Each selection event is for resistance to a different mechanism.
         No single resistance trait provides advantage for long.

  THREE-YEAR RULE: In practice, many extension recommendations:
  Use no more than one MOA twice per crop cycle.
  Different MOA in each application window.
```

---

## Organic Options

```
ORGANIC IPM TOOLS (OMRI-listed or approved):
  Insecticides:
    Neem (azadirachtin): disrupts molting hormones; IGR effect; repellent.
      Effective for aphids, whiteflies, mites, thrips at early stages.
    Pyrethrin (from Chrysanthemum): fast knockdown; rapid degradation.
      Toxic to beneficials if misapplied; short residual.
    Spinosad: Group 5; fermentation product; selective; highly effective.
      Use sparingly — resistance developing in thrips (western flower thrips).
    Kaolin clay (Surround): physical barrier; applied to fruit surfaces.
      Deters egg-laying; reduces sunburn. Not a pesticide per se.
    Diatomaceous earth: physical abrasion to insect cuticle; slow.

  Fungicides:
    Sulfur: multi-site; very effective for powdery mildew, some rust.
      Cannot apply within 2 weeks of oil spray (phytotoxicity).
    Copper (copper hydroxide, Bordeaux mixture): bactericide + fungicide.
      Used for blight (potato, tomato), bacterial canker, downy mildew.
      Accumulates in soil with long-term use (Cu toxicity to earthworms).
    Bicarbonate (potassium bicarbonate): powdery mildew; alkaline surface.
    Biological fungicides: Trichoderma, Bacillus subtilis (Serenade®).
      Effective preventatively; minimal efficacy once disease established.
```

---

## Decision Cheat Sheet

| Situation | Primary Approach | Decision Trigger |
|-----------|-----------------|-----------------|
| New pest outbreak | Scout first; identify life stage | Reach ET before any action |
| Soilborne disease history | Cultural (rotation, resistant variety) | Site selection + variety choice at planting |
| Greenhouse spider mites | Release Phytoseiulus persimilis early | Presence of spider mites (before threshold — preventive release) |
| Caterpillar pests | Btk + Trichogramma release | At egg hatch window (degree-day model) |
| Aphid-vectored virus pressure | Reflective mulch, mineral oil, early planting | Before virus season (preventive) |
| High-value crop at ET | Selective pesticide (IRAC Group 28 or 5) | At ET; rotate MOA each application |
| Organic certification | OMRI-listed inputs only | Same ET framework applies |

---

### Control Systems and Operations Framing

IPM's Economic Injury Level (EIL) / Economic Threshold (ET) framework is a pre-emptive alerting system identical in logic to SLA-based capacity alerting. The EIL is the damage point — pest density at which economic damage equals the cost of control. Intervening at the EIL is already too late (you've taken the hit). The ET (typically 75–80% of EIL) is the intervention trigger: you act at the threshold that prevents reaching the damage level. This is exactly the capacity planning model: don't alert when you're at 100% CPU utilization (EIL — already degraded), alert at 80% (ET — enough headroom to intervene before the service degrades).

Degree-day (DD) accumulation models are univariate time-series forecasting for biological systems. The model accumulates heat above a base temperature (T_base) over time: DD = sum(T_mean - T_base) for each day where T_mean > T_base. Each pest species has calibrated DD thresholds for life stage transitions (egg hatch, larval peak, adult flight peak). When accumulated DD crosses the threshold, the forecast triggers a scouting recommendation or treatment window. This is threshold-crossing event detection on a time-integrated signal — identical to the statistical process control methods used to detect drift in manufacturing or service metrics.

The combination of ET + DD models provides the full alerting architecture: the DD model predicts *when* pests will be at a vulnerable stage (timing the intervention window), and the ET model determines *whether* density is high enough to justify intervention (avoiding unnecessary treatments). The intersection — "pest is at vulnerable stage AND density exceeds ET" — is the trigger. This is AND-gate logic on two independent signals, which is standard practice in alert engineering to reduce false positives.

## Common Confusion Points

**Biological control agents are not zero-cost**: purchasing Phytoseiulus sachets, Trichogramma cards, or entomopathogenic nematodes has a direct cost that must be compared to pesticide costs. The comparison must include: pesticide cost + application labor + resistance risk + benefit impact + regulatory risk. Biologicals often win this comparison but are not free.

**"Natural" pesticides are not non-toxic**: pyrethrin (from chrysanthemum) is highly toxic to aquatic invertebrates and bees. Copper (organic-approved) accumulates in soil and is toxic to earthworms at high levels. Organic status does not equal environmental harmlessness.

**Economic thresholds require calibration**: EIL published in extension guides assumes average commodity prices and average control costs. If your crop is a premium specialty item at 3× standard price, your EIL is lower (smaller damage is now economically significant). Recalculate for your actual costs and prices.

**Resistance is irreversible once established**: once a resistant allele reaches high frequency in a pest population, removing pesticide selection pressure does not restore sensitivity (the allele has no fitness cost in most cases). Rotating MOA PREVENTS resistance; it does not reverse existing resistance.

**Scouting IS the intervention, not just a prelude to it**: the act of going into the field, observing, and recording data is itself valuable independent of any pesticide decision. Scouts identify problems early, identify natural enemy activity, and provide the data trail that proves IPM is working.
