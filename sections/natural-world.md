# Natural World

6 directories · The living world and its intersection with human use — from element properties to food traditions

---

## Landscape

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                              NATURAL WORLD                                          │
└─────────────────────────────────────────────────────────────────────────────────────┘

 FOUNDATION SCIENCE
 ┌──────────────────────────────────────────────────────────────────────────────────┐
 │                                                                                  │
 │  ┌────────────────────────────┐          ┌────────────────────────────────────┐  │
 │  │       periodic-table/      │          │         animal-phylogeny/          │  │
 │  │  element properties        │          │  tree of life · major phyla        │  │
 │  │  electron configuration    │          │  evolutionary relationships        │  │
 │  │  periodic trends           │          │  key adaptations                   │  │
 │  │  isotopes                  │          │  vertebrate/invertebrate survey    │  │
 │  │  practical element ref.    │          └────────────────────────────────────┘  │
 │  └────────────────────────────┘                                                  │
 │  (the what of matter)                    (the what of life)                      │
 └──────────────────────────────────────────────────────────────────────────────────┘
              │                                          │
              │ chemistry of flavor                      │ organisms as food
              ▼                                          ▼
 PLANTS AS HUMAN RESOURCES
 ┌──────────────────────────────────────────────────────────────────────────────────┐
 │                                                                                  │
 │  ┌────────────────────────────┐          ┌────────────────────────────────────┐  │
 │  │           spices/          │          │           food-plants/             │  │
 │  │  trade history (VOC)       │          │  staple crops · domestication      │  │
 │  │  Columbian Exchange        │          │  botany of edible plants           │  │
 │  │  botanical sources         │          │  genetic improvement               │  │
 │  │  flavor chemistry          │          │  global distribution               │  │
 │  │  alkaloids/terpenes/       │          └────────────────────────────────────┘  │
 │  │  phenylpropanoids          │                                                  │
 │  └────────────────────────────┘                                                  │
 └──────────────────────────────────────────────────────────────────────────────────┘
              │                                          │
              │ ingredients → cooking                    │ raw plants → processed food
              ▼                                          ▼
 FOOD SYSTEMS
 ┌──────────────────────────────────────────────────────────────────────────────────┐
 │                                                                                  │
 │  ┌────────────────────────────┐          ┌────────────────────────────────────┐  │
 │  │       culinary-history/    │          │       fermentation-spirits/        │  │
 │  │  cooking techniques + chem │          │  microbiology of fermentation      │  │
 │  │  cuisine traditions        │          │  beer · wine · distillation        │  │
 │  │  ingredient adoption       │          │  regional traditions               │  │
 │  │  restaurant history        │          │  flavor chemistry                  │  │
 │  │  food technology           │          │  spirits taxonomy                  │  │
 │  └────────────────────────────┘          └────────────────────────────────────┘  │
 └──────────────────────────────────────────────────────────────────────────────────┘

 SCOPE NOTE: This section covers the natural/cultural interface.
 ┌───────────────────────────────────────────────────────────────────────────────────┐
 │  Life Sciences covers deep biology (cell biology, genetics, evolution).           │
 │  Natural World covers organisms and elements as they enter human culture —        │
 │  what we eat, grow, trade, and transform.                                         │
 └───────────────────────────────────────────────────────────────────────────────────┘
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `periodic-table/` | Element-by-element reference organized around chemical behavior: electron configuration and its consequences (shielding, effective nuclear charge, why the periodic trends exist rather than just what they are), periodic trends in depth (atomic radius, ionization energy, electronegativity, electron affinity — the four that explain reactivity), block organization (s/p/d/f and what it means for chemistry), isotope stability and the band of stability, practical element surveys (alkali metals, halogens, noble gases, transition metals, lanthanides and actinides — each group with actual physical properties and industrial uses), the superheavy elements and synthesis | `01-STRUCTURE.md` — electron configuration and why the table has its shape | Mathematics & Physics `natural-sciences/01-ATOMIC-QUANTUM.md` for the quantum mechanics underneath; Material Culture `metalworking/` and `jewelry/` for industrial and precious metal properties in use |
| `animal-phylogeny/` | Tree of life from LUCA to mammals: the three-domain system (Bacteria/Archaea/Eukarya — why Archaea rewrote the tree), eukaryote origins (endosymbiotic theory with actual evidence), major animal phyla with body plan logic (Porifera, Cnidaria, Platyhelminthes, Annelida, Mollusca, Arthropoda, Echinodermata, Chordata — body cavity, symmetry, and segmentation as organizing axes), deuterostome/protostome split and why it matters, vertebrate radiation (fish → amphibian → reptile → bird/mammal — each transition's key innovation), primate phylogeny and human evolution, key adaptations as engineering solutions (flight, echolocation, endothermy, venom systems) | `01-DOMAINS-PHYLA.md` — the deep tree before the animal-specific survey | Life Sciences `biology/` for cellular and molecular biology; `food-plants/` for the parallel plant-side survey; History & Ideas for human evolution context |
| `spices/` | Spice trade as world history and flavor as chemistry: the spice trade economies (Arab intermediaries, Portuguese rounding of Africa, Dutch VOC monopoly on nutmeg and clove — these are genuine drivers of colonialism), the Columbian Exchange (what moved between hemispheres and why that reorganized global cuisine), botanical sources organized by plant part (seeds: pepper/mustard/cumin; bark: cinnamon/cassia; flower buds: cloves; rhizomes: ginger/turmeric/galangal; fruits: vanilla/cardamom/chili), flavor chemistry by molecular class (alkaloids: capsaicin/piperine — VR1 receptor and why they burn; terpenes: limonene/linalool — volatile aromatics; phenylpropanoids: eugenol/anethole/cinnamaldehyde; sulfur compounds: allicin in garlic), per-spice deep dives with cultivation geography, historical use, and culinary applications | `01-TRADE-HISTORY.md` — spice trade economics, situates every individual spice in historical context | History & Ideas `economic-history/` for VOC and colonial economics; `culinary-history/` for how these ingredients entered cooking traditions; `periodic-table/` for the underlying organic chemistry of flavor molecules |
| `food-plants/` | Domestication, botany, and global distribution of plants humans eat: the origins of agriculture (Fertile Crescent, Yangtze valley, Mesoamerica — polycentric domestication), domestication syndrome (reduced seed dispersal, larger seeds, loss of dormancy — convergent evolution under human selection), staple grain botany (wheat/rice/maize — C3 vs. C4 photosynthesis and why it matters for yield potential), legume nitrogen fixation (why beans and grains together are nutritionally complete), tuber crops (potato/cassava/sweet potato — different starch storage systems), vegetable and fruit taxonomy (why tomato is botanically a fruit, why strawberry is botanically not), genetic improvement history (Green Revolution wheat and rice — Borlaug's semi-dwarfing genes), GMO biology and regulatory landscape | `01-DOMESTICATION.md` — origins of agriculture, the historical and evolutionary foundation | Life Sciences `botany/` for plant biology depth; History & Ideas for the Green Revolution's geopolitical consequences; `culinary-history/` for how these plants entered cuisine |
| `culinary-history/` | Cooking as technology and tradition: the chemistry of heat (Maillard reaction — carbonyl/amine condensation, not caramelization; why browning matters; why high heat is required), cooking method taxonomy (dry heat: roasting/frying/grilling; moist heat: boiling/steaming/braising; combination: stew/braise; no-heat: curing/fermentation), the five major cuisine traditions (Chinese, French, Japanese, Indian, Mediterranean — each with its own flavor principle and structural logic), major ingredient adoption events (tomato/potato/chili entering Old World cuisine post-1492), professional kitchen organization (brigade system, Escoffier's rationalization of French cuisine), food technology (pasteurization, canning, refrigeration, freeze-drying — each a shelf-life engineering problem), the food science movement (Myhrvold's modernist cuisine as engineering applied to cooking) | `01-HEAT-CHEMISTRY.md` — Maillard and caramelization chemistry, the science of cooking | `spices/` and `food-plants/` for the ingredient side; `fermentation-spirits/` for the preservation and flavor-development techniques that parallel cooking; History & Ideas for cuisine as cultural identity |
| `fermentation-spirits/` | Microbiology and craft of fermentation: fermentation biochemistry (yeast glycolysis → ethanol + CO2, bacterial fermentation pathways — lactic/acetic/propionic, why different microbes produce different flavors), beer production (malting: enzyme activation in barley; mashing: starch → fermentable sugars; lautering; fermentation; conditioning — each step a biochemical transformation), wine production (grape chemistry, must composition, yeast selection, malolactic fermentation, oak aging), distillation physics (fractional distillation, pot still vs. column still, congener distribution and flavor development), regional traditions by spirit type (Scotch whisky: peat smoke and copper pot stills; Bourbon: new charred oak and corn; Cognac: double distillation and oxidative aging; mezcal: agave roasting as flavor source), flavor chemistry of aged spirits (ester formation, oxidation products, wood-extracted compounds — lactones, vanillin, tannins) | `01-FERMENTATION-BIOCHEM.md` — yeast metabolism and fermentation chemistry, the microbiological foundation | `culinary-history/` for fermentation as a food preservation and flavor technique; Material Culture `coatings/` for the organic chemistry overlap (esters, oxidation); Life Sciences `biology/` for microbial ecology |

---

## Paths

### Chemistry of flavor
`periodic-table/` → `spices/` → `culinary-history/`
*Start with molecular structure (organic chemistry is periodic table chemistry applied), then trace how specific molecular classes (capsaicinoids, terpenes, phenylpropanoids) produce specific flavor experiences, then see how culinary traditions are built on those flavor chemistries — this is the reductionist path from atom to cuisine.*

### Agriculture to plate
`food-plants/` → `culinary-history/` → `fermentation-spirits/`
*Domestication explains what plants are available; culinary history explains what humans did with them; fermentation shows how preservation techniques became flavor traditions — the full arc from field to finished product.*

### Evolutionary context for food
`animal-phylogeny/` → `food-plants/` → `spices/`
*The tree of life establishes what organisms are and their evolutionary relationships; food plants shows plants as a human-selected subset of that tree; spices shows the most extreme case of human valuation reshaping the distribution of specific plant species across the globe.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Life Sciences | `animal-phylogeny/` is the entry point to Life Sciences `biology/` — the phylogeny gives the who, cell biology gives the how. `food-plants/` connects to `botany/` for plant physiology and `nutrition/` for biochemical processing of food by human bodies. `fermentation-spirits/` connects to microbiology and `ecology/` for microbial community dynamics. |
| Earth & Space | `food-plants/` and agriculture connect to `geology/` (soil science, soil parent material, nutrient cycling) and `climate-science/` (agricultural zones, crop range shifts under warming). `spices/` geographic distribution is partly explained by tropical geology and climate. |
| History & Ideas | `spices/` — the nutmeg and clove monopoly drove Dutch colonial expansion; pepper financed the Portuguese empire. `culinary-history/` — the Columbian Exchange is one of the largest single disruptions to human diet in history. `fermentation-spirits/` — the economics of alcohol (temperance movements, Prohibition, excise taxation) are recurring themes in political and economic history. |
| Material Culture | Fermentation chemistry shares organic chemistry foundations with `coatings/` (ester chemistry, oxidative reactions). Plant-derived dyes and mordants in `textiles/` connect back to the same botanical sources as `food-plants/` and `spices/`. The vessels of food culture — ceramics, glass, metalwork — are all covered in Material Culture. |
