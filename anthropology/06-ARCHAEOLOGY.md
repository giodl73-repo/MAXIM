# Archaeology

## The Big Picture

```
+------------------------------------------------------------------+
|                        ARCHAEOLOGY                                |
|                                                                   |
|  "The study of human past through material remains — artifacts,  |
|   structures, features, and environmental data"                  |
+------------------------------------------------------------------+
         |              |              |              |
         v              v              v              v
  +-----------+ +-----------+ +-----------+ +-----------+
  | FIELDWORK | |  DATING   | |  THEORY   | | APPLIED   |
  | METHODS   | |  METHODS  | |           | | ARCHAE.   |
  +-----------+ +-----------+ +-----------+ +-----------+
  | Survey    | | Relative  | | Processual| | CRM       |
  | Excavation| | Absolute  | | Post-proc.| | NAGPRA    |
  | Recording | | Radiocarb | | Agency    | | Heritage  |
  | Remote    | | K-Ar/OSL  | | Landscape | | Human     |
  | sensing   | | Dendro    | |           | | rights    |
  +-----------+ +-----------+ +-----------+ +-----------+
```

Archaeology is the only discipline with direct empirical access to the
99%+ of human history that predates writing. Every artifact is a data point
in an argument about behavior, cognition, society, and change over time.

---

## Section 1: Fieldwork Methods

### Survey — Finding Sites Before You Dig

```
  PEDESTRIAN SURVEY:
  Systematic coverage of a study area on foot, at regular
  intervals. Crew members walk parallel transects, record
  surface artifacts, features, and site boundaries.

  Sampling strategies:
  ┌────────────────────────────────────────────────────────┐
  │ FULL COVERAGE: survey entire study area. Most complete.│
  │ Impractical for large areas.                           │
  │                                                        │
  │ RANDOM SAMPLING: randomly select transects/units.     │
  │ Statistically defensible; misses spatially clustered  │
  │ sites.                                                 │
  │                                                        │
  │ STRATIFIED SAMPLING: divide area into environmental   │
  │ zones; sample each proportionally. Better for         │
  │ heterogeneous landscapes.                             │
  │                                                        │
  │ JUDGMENTAL SAMPLING: survey where you think sites     │
  │ are (near water, on ridges). Efficient but biased.   │
  └────────────────────────────────────────────────────────┘

  SITE DEFINITION: a spatial concentration of artifacts
  and/or features above background noise. "Background noise"
  is determined from offsite sampling.
```

### Excavation — The Irreversible Act

```
  KEY INSIGHT: excavation destroys the context it recovers.
  You cannot re-excavate. Meticulous documentation is
  not bureaucracy — it is the only way the data persists.

  STRATIGRAPHIC METHOD:
  Remove deposits layer by layer, following natural
  stratigraphy (the actual depositional layers), not
  arbitrary depth levels (which cut across strata and
  mix contexts).

  WHEELER BOX-GRID (Mortimer Wheeler, 1930s):
  Grid of 10x10m (or similar) squares with baulks (unexcavated
  walls) between them, preserving stratigraphy for reading.
  The baulk lets you see the full stratigraphic sequence as
  a visible cross-section. Dominant method through mid-20th c.

  OPEN AREA EXCAVATION (single context recording):
  Remove baulks; expose the full horizontal extent of each
  depositional unit (context) before moving to the next.
  Better for understanding spatial organization of features.
  Now dominant in European urban/settlement archaeology.

  RECORDING:
  Each "context" (discrete deposit, layer, feature, cut)
  gets its own context sheet: stratigraphic relationships,
  soil description, finds, samples, spatial data.
  Total station survey: sub-centimeter 3D coordinates on
  artifacts in situ. Site drawings + photography + digital.
```

### Remote Sensing — Finding What You Cannot See

```
  LIDAR (Light Detection and Ranging):
  Airborne or terrestrial laser scanning generates point cloud
  of ground surface at cm resolution.

  KEY CAPABILITY: "bare earth" models strip vegetation.
  Under dense tropical jungle: invisible to satellite/air photo.
  LiDAR reveals topography below the canopy.

  ┌────────────────────────────────────────────────────────┐
  │ CARACOL, Belize (Chase et al. 2010):                  │
  │ Classic Maya city. Airborne LiDAR over 200 km².       │
  │ Revealed: causeways, agricultural terracing, plazas,  │
  │ and a continuous urban complex MUCH larger than       │
  │ ground survey suggested (>100,000 population).        │
  │ Transformed understanding of Maya urbanism.           │
  │                                                        │
  │ ANGKOR, Cambodia (Evans et al. 2013):                 │
  │ LiDAR revealed hydraulic infrastructure (reservoir    │
  │ systems, canal networks) and suburban extent of       │
  │ Angkor complex. Largest pre-industrial urban spread.  │
  │                                                        │
  │ AMAZON BASIN (various 2010s-present):                 │
  │ Earthworks, ditched enclosures, raised fields under   │
  │ dense forest — evidence of large pre-Columbian        │
  │ populations that transformed the landscape.           │
  └────────────────────────────────────────────────────────┘

  GROUND-PENETRATING RADAR (GPR):
  Emits radar pulses into the ground; measures reflections
  from density contrasts. Produces 3D subsurface image
  without excavation.

  Uses: mapping buried structures, walls, ditches, graves.
  Resolution: decimeter-scale at shallow depth.
  Limitation: cannot identify material type; only density
  contrast. Clay-rich soils reduce penetration.

  MAGNETOMETRY:
  Measures variations in soil magnetic properties.
  Burned features (hearths, kilns, fired structures):
  high magnetism. Ditches (infilled): low magnetism.
  Can survey large areas quickly (hundreds of m² per day).
  Cannot see through standing vegetation as well as GPR.

  SATELLITE REMOTE SENSING:
  Multispectral imagery reveals crop marks: buried features
  affect soil moisture and chemistry, which affects
  vegetation growth above them — visible in infrared.
  Used for: detecting looted sites, mapping agricultural
  systems, identifying site networks across landscapes.
```

---

## Section 2: Stratigraphy and Dating Framework

### Stratigraphic Principles

```
  LAW OF SUPERPOSITION (Steno 1669, extended to archaeology):
  In undisturbed deposits, older material is below younger.

  EXCEPTIONS (critical):
  - Bioturbation: burrowing animals, tree roots, earthworms
    move material vertically
  - Intrusions: pits, wells, graves cut down through older
    layers (they are younger than everything they cut through)
  - Reverse stratigraphy: erosion and redeposition can invert
    sequences

  TERMINUS POST QUEM (TPQ):
  "Limit after which" — the deposit cannot be OLDER than
  its latest datable item. A coin dated 50 CE in a layer
  means the layer cannot predate 50 CE.

  TERMINUS ANTE QUEM (TAQ):
  "Limit before which" — the deposit cannot be YOUNGER than
  the earliest date of what seals it. Sealed by a floor
  dated to 100 CE means the layer was deposited before 100 CE.

  HARRIS MATRIX:
  A directed graph representation of stratigraphic relationships.
  Each context is a node. Edges represent:
  - A is above B (A later than B)
  - A is the same as B (same event)
  - A cuts B (A intrudes into B, therefore younger)

  The Harris Matrix formalizes the stratigraphic record as
  a dependency graph — exactly the conceptual structure of
  a DAG. If you understand dependency resolution in build
  systems, you understand Harris Matrix logic.
```

---

## Section 3: Dating Methods

### Radiocarbon (14C) Dating

```
  PRINCIPLE:
  Cosmic rays -> nitrogen in atmosphere -> 14C
  Plants fix 14C during photosynthesis; animals eat plants.
  While alive: organism maintains atmospheric 14C ratio.
  At death: 14C decays, 12C stays.

  14C half-life: 5,730 years (±40 yr)

  Measure: ratio of 14C to 12C/13C in sample.
  Convert to age via decay equation.

  AMS (Accelerator Mass Spectrometry): counts atoms directly.
  Needs only milligrams of carbon. Older, more precise than
  conventional radiometric counting.

  CALIBRATION:
  Atmospheric 14C:12C ratio is NOT constant — solar activity
  and ocean circulation vary. Raw radiocarbon dates are "14C
  years BP" (Before Present = before 1950).

  Must calibrate against the INTCAL20 curve (2020 update):
  dendrochronology + coral + speleothems + varves provide
  absolute dates tied to actual calendar years.

  OxCal / CALIB: standard software for calibration.
  Result: a probability distribution over calendar years, not
  a single date. Wiggles in the calibration curve can cause
  flat regions where precision is low (e.g., calibration
  plateau ~400-900 CE — notorious for poor precision).

  ┌────────────────────────────────────────────────────────┐
  │ Effective range: ~50-50,000 calendar years BP          │
  │ (beyond 50,000 yr: too little 14C left to measure)     │
  │                                                        │
  │ Precision: typically ±30-200 cal yr depending on       │
  │ sample quality and position on calibration curve       │
  │                                                        │
  │ RESERVOIR EFFECT: marine organisms take up 14C from   │
  │ ocean water (which exchanges with atmosphere slowly).  │
  │ Apparent age ~400 years older — must apply marine      │
  │ reservoir correction. Freshwater reservoirs vary.     │
  └────────────────────────────────────────────────────────┘

  BAYESIAN MODELING (Bronk Ramsey):
  Use stratigraphic order as prior constraints on a series
  of radiocarbon dates. Dramatically improves precision.
  If you know A is below B is below C, and you have
  radiocarbon dates on all three, you can reject calibrated
  ranges that violate the stratigraphic prior.
```

### Other Absolute Dating Methods

```
  POTASSIUM-ARGON (K-Ar) AND ARGON-ARGON (40Ar/39Ar):
  ┌────────────────────────────────────────────────────────┐
  │ 40K decays to 40Ar with half-life of 1.25 billion yr  │
  │ Measures: ratio of 40Ar to 40K in volcanic rocks       │
  │ Zero-point: volcanic eruption releases all argon;      │
  │             clock resets                               │
  │ Ar-Ar: more precise, same principle, samples multiple  │
  │         isotopes simultaneously                        │
  │                                                        │
  │ Use: dating volcanic ash layers at hominin fossil      │
  │ sites (Omo Kibish, Laetoli, Olduvai). Effective from   │
  │ ~100,000 yr to billions of years. Cannot date below    │
  │ ~100 ka reliably.                                      │
  └────────────────────────────────────────────────────────┘

  THERMOLUMINESCENCE (TL) AND OSL (Optically Stimulated
  Luminescence):
  ┌────────────────────────────────────────────────────────┐
  │ Crystal lattice (quartz, feldspar) accumulates trapped │
  │ electrons from ambient radioactivity over time.        │
  │ Heating (TL) or light exposure (OSL) releases          │
  │ electrons as luminescence.                             │
  │                                                        │
  │ Zero-point event:                                      │
  │ TL: firing of ceramics, burning of sediment           │
  │ OSL: sunlight exposure during sediment transport       │
  │                                                        │
  │ Effective range: TL 1,000-500,000 yr                  │
  │                  OSL 100-500,000 yr                    │
  │                                                        │
  │ USE: dating:                                           │
  │ - Ceramics without organic content                    │
  │ - Burned lithics                                       │
  │ - Loess, aeolian, alluvial sediments                  │
  │   (for when sediment was last exposed to light)        │
  └────────────────────────────────────────────────────────┘

  DENDROCHRONOLOGY:
  ┌────────────────────────────────────────────────────────┐
  │ Tree rings: one per year; width varies with climate   │
  │ Pattern of wide/narrow rings is distinctive for       │
  │ regional climate sequence — can be cross-dated         │
  │                                                        │
  │ MASTER CHRONOLOGIES: built by overlapping living +    │
  │ dead + fossil trees:                                   │
  │ - US Southwest: ~8,000 years                          │
  │ - German oak: ~12,500 years                           │
  │ - Anatolian oak: used for IntCal calibration           │
  │                                                        │
  │ Precision: exact calendar year.                        │
  │                                                        │
  │ Limitation: requires wood that survived in context;   │
  │ not universal. And the wood may be reused (old-growth  │
  │ timber in a new building doesn't date the building).  │
  └────────────────────────────────────────────────────────┘
```

### Relative Dating — Typology and Seriation

```
  TYPOLOGY: artifact classification system where type = a cluster
  of attributes that co-occur with more-than-chance frequency.

  Key insight: artifact styles change through time.
  Like version numbers — 3.0 shares more features with 2.5
  than with 1.0. The sequence can be worked out without
  knowing the absolute dates.

  SERIATION (Petrie 1899, Ford 1952):
  Arrange assemblages so that each type shows gradual
  appearance, peak frequency, and gradual disappearance.
  A "battleship curve" when graphed.

  ┌────────────────────────────────────────────────────────┐
  │          TIME                                          │
  │  Early ┌───────────────────────────────────┐ Late    │
  │        │ Type A: ░░░████████████░░░         │         │
  │        │ Type B: ░░░░░████████████████░░░░  │         │
  │        │ Type C:     ░░░░░░████████████████ │         │
  └────────┴───────────────────────────────────┴─────────┘
  Each type rises, peaks, and falls. Works for ceramics,
  projectile points, glass types, coins.
  Does NOT work for items that never go out of style, or
  for items that revive (retro trends).
```

---

## Section 4: Key Transitions and Sites

### The Neolithic Revolution — Agriculture Origins

```
  NOT a single revolution — multiple independent origins:
  ┌─────────────────────────┬───────────────────────────────┐
  │ Region                  │ Domesticated plants/animals   │
  ├─────────────────────────┼───────────────────────────────┤
  │ Fertile Crescent        │ Wheat, barley, lentils, sheep,│
  │ (SW Asia, ~10,500 BCE)  │ goat, cattle, pig             │
  ├─────────────────────────┼───────────────────────────────┤
  │ China (~7,000 BCE)      │ Rice, millet, pig, chicken    │
  ├─────────────────────────┼───────────────────────────────┤
  │ Mesoamerica (~5,000 BCE)│ Maize, beans, squash, turkey  │
  ├─────────────────────────┼───────────────────────────────┤
  │ Andes (~5,000 BCE)      │ Potato, quinoa, llama, alpaca │
  ├─────────────────────────┼───────────────────────────────┤
  │ New Guinea (~7,000 BCE) │ Taro, bananas, sugarcane      │
  └─────────────────────────┴───────────────────────────────┘

  GOBEKLITEPE — THE MODEL-BREAKER (2008, Klaus Schmidt):
  Southeast Turkey. Monumental stone pillars (T-shaped, up to
  5m tall, ~50 tons) with carved animal reliefs. Dates: 9500-
  8000 BCE — before agriculture in the region.

  THE STANDARD MODEL was shattered:
  Old model: agriculture -> surplus -> sedentism -> ritual centers
  Gobeklitepe model: ritual/monument construction -> aggregation
  of mobile populations -> sedentism -> agriculture (reverse)

  The temple preceded the settlement. Ritual capacity may have
  been the driver of sedentism, not the product of it.

  CATALHOYUK (Anatolia, ~7500-5700 BCE):
  Proto-urban settlement. Up to ~8,000 people.
  No streets — entered buildings through rooftop openings.
  Burials under house floors (skulls sometimes removed, circulated).
  Relatively egalitarian burial goods.
  Extensive symbolic life (bulls' horns, female figurines, wall art).
  Ian Hodder's long-term excavation; post-processual interpretation.
```

### The Bronze Age Collapse (~1200 BCE)

```
  THE EVENT:
  Within a ~50-year window (~1200-1150 BCE), the Eastern
  Mediterranean palace system collapsed:
  - Mycenaean Greece: palaces destroyed, Linear B writing ceases
  - Hittite Empire: capital Hattusa destroyed, empire ends
  - Ugarit (Syria): destroyed, never reoccupied
  - Egypt: severely weakened, loses empire
  - Cyprus: many cities destroyed

  THE SUSPECTS (Cline, "1177 BC"):
  ┌────────────────────────────────────────────────────────┐
  │ Sea Peoples: Egyptian records describe migrations and  │
  │ raids by confederacy of peoples from "the islands."   │
  │ DNA evidence: some were from Aegean/Mycenaean region. │
  │ Were they cause or symptom? Probably both — displaced │
  │ by other disruptions.                                  │
  │                                                        │
  │ Climate/drought: pollen records, sediment cores show  │
  │ ~300-year aridification across Eastern Mediterranean  │
  │ ~1200-900 BCE. Megadrought in 1200s BCE documented.  │
  │                                                        │
  │ Earthquakes: several Mycenaean sites show earthquake   │
  │ damage (~1200 BCE).                                    │
  │                                                        │
  │ Internal rebellion: palace texts show social strain;  │
  │ economic inequality; possible slave/peasant revolts.  │
  │                                                        │
  │ Trade network disruption: palace economies depended   │
  │ on long-distance trade (tin from Afghanistan, copper  │
  │ from Cyprus). Disruption cascaded.                     │
  └────────────────────────────────────────────────────────┘

  LESSON: Complex civilizations have multiple failure modes
  operating simultaneously. "Systems collapse" (Tainter) is
  not monocausal. The interconnectedness that enabled
  prosperity also transmitted shocks across the system.

  This is a direct analogy to: cloud service dependency chains,
  supply chain fragility, and "too big to fail" institutional
  dynamics in any complex technological ecosystem.
```

---

## Section 5: Processual vs. Post-Processual Theory

```
  PROCESSUAL ARCHAEOLOGY (New Archaeology, Binford 1962):
  ┌────────────────────────────────────────────────────────┐
  │ - Archaeology is a science; must use hypothesis testing│
  │ - Culture = adaptive system; behavior = adaptation to  │
  │   environment                                          │
  │ - Goals: find covering laws (general regularities) of  │
  │   cultural process                                     │
  │ - Reject: culture history (just describing sequences); │
  │   normative anthropology                               │
  │ - Methods: quantification, spatial analysis, explicit  │
  │   sampling design, ecological data                    │
  │ - Lewis Binford, David Clarke, Colin Renfrew           │
  └────────────────────────────────────────────────────────┘

  POST-PROCESSUAL ARCHAEOLOGY (Hodder, Shanks, Tilley, 1980s):
  ┌────────────────────────────────────────────────────────┐
  │ - "There are no facts without interpretation"          │
  │ - Artifacts have meaning that cannot be read from      │
  │   form alone (a knife is a knife AND a ritual object)  │
  │ - Agency: individuals make choices; not just adapting  │
  │ - Context: same artifact means different things in    │
  │   different contexts                                   │
  │ - Reflexivity: archaeologist's position shapes        │
  │   interpretation                                       │
  │ - Ian Hodder's Catalhoyuk approach: multivocality      │
  │   (local communities involved in interpretation)       │
  └────────────────────────────────────────────────────────┘

  CURRENT POSITION:
  Most archaeologists use elements of both. Science + meaning.
  Hypothesis testing + interpretive context.
  The dichotomy was productive for the discipline but is
  increasingly seen as a false opposition.
```

---

## Section 6: Applied Archaeology — CRM and NAGPRA

### Cultural Resource Management (CRM)

```
  CRM IS THE LARGEST EMPLOYER OF ARCHAEOLOGISTS in the US.
  Not academics — compliance archaeologists in private firms.

  LEGAL FRAMEWORK:
  ┌────────────────────────────────────────────────────────┐
  │ National Historic Preservation Act (NHPA, 1966):       │
  │ - Section 106: federal undertakings that may affect   │
  │   historic properties require review                  │
  │ - "Adverse effect" triggers mitigation (data recovery  │
  │   = excavation + analysis)                            │
  │                                                        │
  │ Archaeological Resources Protection Act (ARPA, 1979):  │
  │ Illegal to excavate archaeological sites on federal   │
  │ land without a permit.                                 │
  │                                                        │
  │ Section 106 PROCESS:                                   │
  │ Initiate -> Identify historic properties -> Assess     │
  │ effects -> Resolve adverse effects (MOA) -> Carry out  │
  └────────────────────────────────────────────────────────┘

  TIMELINE:
  Before any federal construction, pipeline, highway, cell
  tower, etc.: Phase I survey (identify sites) -> Phase II
  evaluation (are they eligible for National Register?) ->
  Phase III data recovery (if eligible and must be destroyed).
```

### NAGPRA — Repatriation Law

```
  NATIVE AMERICAN GRAVES PROTECTION AND REPATRIATION ACT (1990):

  BACKGROUND: Museums and universities held Native American
  human remains and sacred objects collected during the
  19th-20th centuries — often under coercive or unethical
  circumstances. NAGPRA mandated return of:
  - Human remains
  - Funerary objects
  - Sacred objects
  - Objects of cultural patrimony

  TO: lineal descendants and culturally affiliated tribes.

  PROCESS:
  1. Institutions inventory their collections
  2. Consult with tribes to determine affiliation
  3. Respond to repatriation requests within 90 days
  4. Transfer items to requesting tribe

  KENNEWICK MAN CONTROVERSY:
  9,000-year-old skeleton found in Washington state (1996).
  Scientists wanted to study it (claimed no known tribal
  affiliation at that time scale).
  Tribes (Umatilla, et al.) claimed cultural continuity
  and right to rebury.
  9-year legal battle. Supreme Court ruled for tribes
  on repatriation. Scientists published studies
  beforehand; DNA ultimately confirmed Native American
  ancestry (Ancient One is now reburied, 2017).

  CARE PRINCIPLES for indigenous data:
  Collective Benefit / Authority to Control /
  Responsibility / Ethics — indigenous communities have
  the right to govern how their heritage data is collected,
  used, and shared. Directly relevant to museum databases,
  genomic research databases, and digital repatriation of
  archival collections.
```

---

## Decision Cheat Sheet

| I need to... | Method |
|-------------|--------|
| Find sites without digging | Pedestrian survey + LiDAR + magnetometry + GPR |
| Date organic material < 50,000 yr | Radiocarbon AMS + OxCal calibration |
| Date burned sediment or ceramics | TL or OSL |
| Date volcanic contexts at hominin sites | K-Ar or Ar-Ar |
| Get precise calendar year from wood | Dendrochronology |
| Improve precision of multiple 14C dates | Bayesian modeling with stratigraphic priors |
| Record stratigraphic relationships | Harris Matrix (directed graph) |
| Date artifacts relatively without chemistry | Seriation (battleship curve) |
| Comply with federal construction law | CRM: Section 106 + NHPA process |
| Return tribal human remains | NAGPRA process + tribal consultation |

---

## Common Confusion Points

**"Older = deeper" always holds.**
Not when there is an intrusion. A Roman pit dug into a Bronze Age layer
contains Roman material BELOW the Bronze Age surface. The TPQ/TAQ distinction
and the Harris Matrix exist precisely because simple "older = deeper" fails
at intrusions, bioturbation, and redeposition events.

**"Radiocarbon gives you a single date."**
No — it gives a probability distribution over calibrated calendar years.
The reported "2-sigma range" is a 95% probability window that can be hundreds
of years wide. And calibration wiggles mean some periods (like the notorious
plateau around 400-900 CE) are especially imprecise. Anyone reporting a single
"exact" radiocarbon date is misrepresenting the data.

**"LiDAR finds buried sites."**
LiDAR finds surface topography at high resolution. It reveals micro-topography
that indicates buried features (low mounds, slight depressions, linear features
in fields) — but the features themselves are at or just below the surface.
It doesn't penetrate the ground like GPR.

**"Post-processual archaeology is just political."**
Post-processualism made real theoretical contributions: agency, context-
dependence of meaning, the role of the interpreter. The "it's all politics"
dismissal is itself a political move by processualists. The debate produced a
more sophisticated practice that takes both scientific rigor and interpretive
context seriously.

**"NAGPRA means scientists can't study ancient DNA from Native Americans."**
NAGPRA governs federal institutions and federally funded research. It requires
tribal consultation and can require repatriation — but it does not prohibit
research per se. Many tribes have collaborated on ancient DNA research with
protocols they designed. The issue is consent and control, not absolute
prohibition. Some tribes opt in; some opt out. Researcher must consult.
