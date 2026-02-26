# Industrial Mycology

## The Big Picture

```
+------------------------------------------------------------------+
|              FUNGI AS INDUSTRIAL WORKHORSES                      |
|                                                                  |
|  ANTIBIOTICS        ORGANIC ACIDS      ENZYMES                  |
|  Penicillin (1928)  Citric acid        Amylases (starch→sugar)  |
|  → WWII scale-up   (Aspergillus niger) Lipases (biodiesel)      |
|  → β-lactam era    → 2M tonnes/year    Cellulases (biofuel)     |
|                    Gluconic acid       Proteases (detergent)    |
|                    Itaconic acid       Pectinases (juice)       |
|                                                                  |
|  FOOD & FERMENTATION  MYCOPROTEIN      MATERIALS                 |
|  Bread (S. cerevisiae) Quorn           Mycelium composites       |
|  Beer / wine          (Fusarium venena-  (Ecovative, IKEA)      |
|  Soy sauce (Asperg.)  tum venenatum)   Fungal leather (Bolt     |
|  Miso, tempeh         22,000 t/year      Threads, Ganni)        |
|  Cheese ripening                                                 |
|                                                                  |
|  PHARMACEUTICALS      BIOREMEDIATION   BIOPESTICIDES            |
|  Statins (lovastatin)  Petroleum        Trichoderma (biocontrol) |
|  Cyclosporine         PAHs, dioxins    Beauveria bassiana        |
|  Ergot alkaloids      Heavy metals     (insect pathogen)        |
|  Taxol (endophyte)    (mycoextraction) Metarhizium (locusts)    |
+------------------------------------------------------------------+
```

Fungi are the most economically exploited microorganisms after bacteria. The key insight: their osmotrophic nutrition (secreting enzymes externally, absorbing products) makes them natural bioreactors for secreting industrially useful molecules in enormous quantity.

---

## Penicillin: The Discovery and Industrial Scale-Up

### Fleming, 1928 — The Original Observation

```
THE ACCIDENT:
  Alexander Fleming, St. Mary's Hospital, London, September 1928
  Staphylococcus culture plate contaminated by mold
  Observation: clear zone of inhibition around mold colony
  Fleming's insight: mold produces diffusible bactericidal substance
  Named it "penicillin" (from Penicillium notatum, the contaminant)

WHAT FLEMING DID AND DID NOT DO:
  Did: Identify the phenomenon; characterize antibacterial spectrum;
       note it was non-toxic to animals; published 1929 (British Journal
       of Experimental Pathology)
  Did not: Purify or concentrate it; trial in patients; develop for
           clinical use
  → Fleming's strain produced tiny amounts; unstable; nobody could
    work with it therapeutically for 10 years

THE CHAIN/FLOREY TEAM (Oxford, 1938–1941):
  Howard Florey (Australian pathologist) + Ernst Chain (German Jewish
  biochemist refugee) + Norman Heatley (biochemist)
  → Concentrated and purified penicillin (ammonium salt extraction)
  → Animal trials 1940: mice challenged with streptococcal lethal dose;
    treated animals survived; untreated died
  → First human trial: Albert Alexander, police officer, February 1941
    Severe septicemia from rose thorn scratch (face/scalp)
    Penicillin: dramatic recovery → supply ran out → he died
  → Demonstrated clinical efficacy; demonstrated the supply problem

1941 Nobel: Fleming + Florey + Chain shared it (1945)
```

### The Cantaloupe Strain — Industrial Scale-Up

```
THE SUPPLY PROBLEM (1941):
  Fleming's P. notatum: produced ~2 units/mL in culture
  Growing Penicillium in flasks: labor-intensive; tiny yield
  WWII demand: Allied forces needed penicillin at industrial scale
  US Army + pharmaceutical companies + USDA: crash program 1941–1945

THE PEORIA CANTALOUPE:
  USDA Northern Regional Research Laboratory, Peoria, Illinois
  Mary Hunt ("Mouldy Mary"): tasked with finding better Penicillium strains
    from any local source of moldy material
  1943: A moldy cantaloupe from a Peoria market
  Strain: Penicillium chrysogenum (now reclassified P. rubens)
  Yield: ~100 units/mL (vs. 2 units/mL from Fleming's strain)
    → 50× improvement from a piece of rotten fruit

FURTHER STRAIN IMPROVEMENT:
  Cantaloupe strain → X-ray and UV mutagenesis → mutant screening
  → Selected for maximum penicillin overproducers
  → Ultimately: 50,000+ units/mL in industrial fermentation
    (>25,000× the yield of Fleming's original strain)
  All industrial penicillin worldwide traces to that cantaloupe.

FERMENTATION ENGINEERING ADVANCES:
  Deep-tank submerged fermentation (vs. surface culture in flasks)
    → Pfizer, 1943: first deep-tank production
  Corn steep liquor (waste from corn milling): found to be ideal
    medium component → massive yield boost
  pH control, aeration, temperature optimization
  Penicillin is a SECONDARY METABOLITE: produced when growth slows
    → Fed-batch culture: maintain suboptimal growth rate →
       secondary metabolism phase → high penicillin titer
  This is early industrial biotechnology — optimization of a living
  system for maximum product output under constrained conditions

WWII PRODUCTION RAMP:
  1942: ~400 million units produced (for all Allied forces)
  1945: ~6.8 trillion units produced
  Price drop: $20/dose (1943) → pennies (1946)
  → Enabled D-Day: casualties treated rather than dying of wound infection

THE β-LACTAM PLATFORM:
  Penicillin G (the original): acid-labile; oral not effective; narrow spectrum
  6-APA (6-aminopenicillanic acid): core scaffold
  Semisynthetic penicillins: attach different side chains to 6-APA
    → Ampicillin: oral; broader spectrum
    → Methicillin: resistant to penicillinase (but MRSA emerged)
    → Amoxicillin: most prescribed antibiotic globally
  Cephalosporins: related β-lactam; Cephalosporium acremonium (1948)
  Carbapenems: synthetic β-lactam; last resort
  All of modern antibiotic medicine builds on the Peoria cantaloupe.
```

### Why Fungi Make Antibiotics

```
EVOLUTIONARY LOGIC:
  β-Lactam antibiotics: why does Penicillium make them?
  Hypothesis: competitive weapon in soil/substrate against bacteria
    that compete for the same decomposing organic matter
  Secondary metabolites ≠ primary metabolism (not required for growth)
  → Produced under nutrient stress; when competition is high
  → Regulation: nitrogen depletion triggers β-lactam biosynthesis genes

BIOSYNTHESIS PATHWAY:
  L-α-aminoadipic acid + L-cysteine + L-valine
  → δ-(L-α-aminoadipyl)-L-cysteinyl-D-valine (ACV tripeptide)
     by ACV synthetase (ACVS, 11,000 aa megaenzyme — NRPS)
  → Isopenicillin N (cyclized) → Penicillin G (side chain exchange)
  NRPS = Non-Ribosomal Peptide Synthetase: modular enzyme assembly line
    → Similar to polyketide synthases (PKS) for other natural products
    → Analogous to: pipeline/assembly line programming — modular, composable

PHARMACEUTICAL RELEVANCE:
  Identifying and engineering NRPS/PKS modules → designed natural products
  Combinatorial biosynthesis: swap modules → new compound libraries
  This is the logic of synthetic biology applied to secondary metabolism
```

---

## Citric Acid Production — Aspergillus as Acid Factory

```
CITRIC ACID:
  E330; used as acidulant, preservative, flavoring in:
  → Food and beverages (~75% of production)
  → Pharmaceuticals (~10%): effervescent tablets, chelation
  → Cleaning/descaling (~10%): chelates calcium, iron
  → Industrial/cosmetics (~5%)
  Global production: ~2 million tonnes/year
  Almost entirely by fermentation of Aspergillus niger

HISTORICAL CONTEXT:
  Pre-1900: citric acid from Italian lemon juice (Sicily)
  1917: James Currie (USDA) discovered Aspergillus niger produces
        massive citric acid under specific conditions
  1919: Pfizer began first industrial fermentation production
  1920s: fermentation displaced lemon juice entirely
  → Classic early example of fermentation replacing chemical synthesis
    or agricultural extraction

THE BIOCHEMISTRY:
  TRICARBOXYLIC ACID (TCA) CYCLE OVERFLOW:
  Normal TCA: citrate → isocitrate → α-ketoglutarate → ...
  Aspergillus overproduction trick:
    High glucose + MANGANESE DEFICIENCY → aconitase inhibited
    → Citrate cannot convert to isocitrate
    → Citrate accumulates → excreted into medium
  Also: Low pH (2–3) → suppresses unwanted competing acids
        High dissolved O₂ → aerobic overflow metabolism
        Specific strains selected for maximum excretion

PRODUCTION CONDITIONS:
  Submerged fermentation (stirred tank) or surface fermentation
  Molasses (cheap sucrose source) or glucose
  Manganese limitation (Mn²⁺ < 0.5 µg/L): critical
  pH 2–3; 28–33°C; 5–7 days fermentation
  Yield: 70–90% of theoretical (carbon → citric acid efficiency)
  Recovery: precipitation as calcium citrate → acidify → citric acid

OTHER ASPERGILLUS ORGANIC ACIDS:
  Gluconic acid: A. niger; glucose oxidase pathway; food acidulant
  Itaconic acid: A. terreus; building block for biopolymers
  Malic acid: fungal fermentation interest for bioplastics
```

---

## Enzyme Production

### The Industrial Enzyme Landscape

```
+------------------------------------------------------------------+
|            INDUSTRIAL ENZYMES: APPLICATIONS                      |
|                                                                  |
|  FOOD PROCESSING:                                                |
|  Amylases (A. oryzae, A. niger)                                 |
|    α-amylase: starch → dextrins (liquefaction)                  |
|    glucoamylase: dextrins → glucose (saccharification)          |
|    → Corn syrup production; bread softening; brewing            |
|  Proteases: bread dough conditioning; cheese making             |
|  Pectinases: fruit juice clarification (apple, grape)           |
|  Lipases: cheese ripening flavor; interesterification           |
|  Xylanases: wheat bread volume improvement                      |
|                                                                  |
|  DETERGENTS (~30% of industrial enzyme market):                 |
|  Proteases (Savinase, Subtilisin E): protein stain removal      |
|  Lipases: fat stains                                            |
|  Amylases: starch stains                                        |
|  Cellulases: cotton fabric finishing (softening, anti-pilling)  |
|                                                                  |
|  BIOFUELS:                                                       |
|  Cellulases + xylanases: cellulose → fermentable sugars         |
|  (lignocellulosic ethanol; the 2nd-generation biofuel problem)  |
|  Trichoderma reesei: prolific cellulase producer                |
|                                                                  |
|  TEXTILES:                                                       |
|  Cellulases: stone-washing denim (replaced pumice stones)       |
|  Proteases: wool shrink-proofing; silk degumming                |
|  Laccases: denim bleaching (replaced chlorine)                  |
|                                                                  |
|  PAPER:                                                          |
|  Cellulases, xylanases: pulp biobleaching                       |
|  Lipases: pitch control                                         |
+------------------------------------------------------------------+
```

### Key Fungal Enzyme Producers

```
Aspergillus niger: amylases, glucoamylases, pectinases, lipases, citric acid
Aspergillus oryzae: amylases, proteases → koji for soy sauce/miso/sake
Aspergillus awamori: glucoamylases
Trichoderma reesei: cellulases, xylanases (primary lignocellulose degrader)
  → Named after Everett Reese (US Army, WWII: investigated why
    army canvas equipment was rotting in South Pacific jungles;
    found T. reesei (then Trichoderma viride) as the cause;
    became most studied cellulase producer)
Penicillium spp.: lipases, xylanases
Rhizopus spp.: lipases (for biodiesel, food processing)
  → Rhizopus microsporus: tempeh starter

PRODUCTION SYSTEM:
  Fungi used either submerged fermentation (SmF) or
  solid-state fermentation (SSF):
  → SSF (growing on moist solid substrate, like grain or bran):
    some enzymes (pectinases, glucoamylases) produced at 10–100×
    higher specific activity under SSF vs. SmF
    → Traditional koji process IS solid-state fermentation
  Downstream: filtration → ultrafiltration → spray drying
  → Enzymes sold as industrial powders or liquid concentrates

PROTEIN SECRETION PATHWAY:
  Why fungi are good at secreting enzymes:
  → Aspergillus niger can secrete 20+ g/L of glucoamylase into culture medium
  → Hypersecreting strains selected: mutations in secretion pathway,
    protease knockouts (prevent degradation of product)
  → Filamentous growth creates high surface area → efficient contact
    with substrate → efficient enzyme secretion
  Engineering: insert heterologous enzyme genes behind strong fungal
    promoters + secretion signal → heterologous protein secreted
  → Fungi as production hosts for non-fungal enzymes
```

---

## Pharmaceuticals Beyond Penicillin

```
STATINS (cholesterol-lowering drugs):
  Lovastatin: Aspergillus terreus (also Monascus purpureus, red yeast rice)
  Compactin (mevastatin): Penicillium citrinum (Akira Endo, 1973, Sankyo)
    → First statin discovered; Endo's story parallels Fleming's
    → Cholesterol-lowering effect in animals and humans
  Simvastatin (Zocor), Atorvastatin (Lipitor): semisynthetic from lovastatin
  Mechanism: HMG-CoA reductase inhibition → blocks cholesterol synthesis
  Why do fungi make lovastatin?
    → Possibly competitive weapon (bacteria use mevalonate pathway too)
    → Exactly analogous to why Penicillium makes penicillin
  Market: statins are among the top-selling drug classes in history
    Lipitor: ~$125B lifetime revenue (best-selling drug ever)

CYCLOSPORINE:
  Tolypocladium inflatum (a fungus, formerly classified as Trichoderma)
  Discovered 1970 (Sandoz, Basel) from Norwegian soil sample
  Mechanism: inhibits calcineurin → blocks T-cell IL-2 production
    → Immunosuppression without myelosuppression
  Enabled modern organ transplantation (kidney, heart, liver)
  Non-ribosomal peptide: 11-amino acid cyclic peptide (NRPS product)
  → Immunosuppressant category essentially did not exist before this

ERGOT ALKALOIDS (Claviceps purpurea):
  Claviceps: parasitic fungus of grain crops (wheat, rye, barley)
  Ergotism: mass poisoning events from contaminated rye bread
    → St. Anthony's Fire: vasoconstrictive ergotism → gangrene
    → Convulsive ergotism: seizures (possibly Salem witch trials)
    → Mediéval mass poisoning events across Europe
  PHARMACEUTICAL RELEVANCE:
  Ergotamine: migraine treatment; α-adrenergic effects
  Ergometrine: uterine contraction after childbirth (prevents hemorrhage)
  Lysergic acid: scaffold for LSD (Albert Hofmann, Sandoz, 1938/1943)
    → LSD was an attempt to make a circulatory stimulant; the
       psychedelic effects were accidental (Hofmann's bike ride, 1943)
  Bromocriptine: dopamine agonist; Parkinson's, prolactinoma, acromegaly
  All are derivatives of lysergic acid; all from Claviceps alkaloid chemistry

TAXOL (paclitaxel) — THE ENDOPHYTE CONNECTION:
  Taxol: widely used anticancer drug (ovarian, breast, lung)
  Originally isolated from bark of Taxus brevifolia (Pacific yew, 1971)
  Supply problem: 1 large yew tree = 2 doses; tree must be killed
  1993: Gary Strobel (Montana State) + Andrea Stierle:
    Taxomyces andreanae (endophytic fungus from Taxus brevifolia)
    → This fungus INSIDE the tree produces paclitaxel independently
  Many other endophytes in Taxus spp. also produce taxol
  Current supply: total synthesis + semi-synthesis from Taxus baccata
    (needles, renewable) + endophyte fermentation research
  → Endophytes as reservoir of bioactive compounds that mirror
    or inspired the host plant chemistry
```

---

## Food Fermentation — Fungal Products at Scale

```
KOJI (Aspergillus oryzae / A. sojae):
  Koji = grain (rice, wheat, barley) colonized by Aspergillus
  Function: mold secretes amylases and proteases into grain
    → Amylases: starch → fermentable sugars (for subsequent
       yeast/bacterial fermentation)
    → Proteases: protein → amino acids including glutamate (umami)
  Applications:
    Sake: rice → koji → saccharification → yeast fermentation
      Parallel fermentation: koji still working when yeast adds →
        highest natural alcohol content of any beverage (~20%)
    Soy sauce (shoyu): soy + wheat + koji → 6–12 month fermentation
    Miso: soy or grain + koji → months to years maturation
    Amazake, rice vinegar, mirin: koji derivatives
  A. oryzae is GRAS (Generally Recognized As Safe, FDA)
  Domesticated version of A. flavus (aflatoxin producer) —
    A. oryzae has lost the aflatoxin biosynthesis genes in domestication

CHEESE RIPENING FUNGI:
  Penicillium roqueforti: blue cheese (Roquefort, Gorgonzola, Stilton)
    → Grows in channels in the cheese curd
    → Secretes lipases (lipolysis) → free fatty acids →
       β-ketones and methyl ketones: the blue cheese flavor
  Penicillium camemberti: Camembert, Brie
    → White surface rind; creamy texture from proteolysis
    → Alkalizes the outer layer → typical "mushroomy" aroma
  Both: carefully selected strains; controlled temperature/humidity

TEMPEH: Rhizopus oligosporus/microsporus
  Soaked, dehulled soybeans + Rhizopus spores → 24–48 hr fermentation
  Mycelium binds soybeans into firm cake → tempeh
  Proteases break down antinutritional factors (phytic acid, trypsin inhibitors)
  Vitamin B12 precursors (some evidence in traditional tempeh)
  → One of the most complete plant protein foods after fermentation

QUORN (Mycoprotein):
  Organism: Fusarium venenatum (previously misidentified as Fusarium graminearum)
    → Isolated from soil in Marlow, UK (Rank Hovis McDougall, 1960s–1980s)
    → Screening program for protein sources; 3,000+ samples tested
  Fermentation: continuous-flow fermenter; glucose + minerals
    → High-protein (45% protein DW), high-fiber (β-glucan + chitin)
    → Produced as continuous filamentous mycelium
    → Processed: heat-treated (kills mold); spun into fibrous texture
    → Mimics muscle fiber texture; takes flavoring well
  Scale: ~22,000 tonnes/year; sold in 17 countries
  Protein content: comparable to chicken per gram (~11g/100g cooked)
  Nutritional profile: all essential amino acids; low saturated fat;
    mycoprotein fiber slows glucose absorption
  Regulatory path: UK: approved 1985 (Quorn brand launched)
                  US: approved 2002 (GRAS petition after prolonged FDA review)
                  Controversy: a very small subset of consumers (0.001%)
                    reported allergic reactions; company required to add
                    label warning (vomiting, allergic reactions in some)
  → Most commercially successful mycoprotein product by far
```

---

## Mycelium Composites and Biomaterials

```
THE CONCEPT:
  Fungal mycelium → "nature's glue"
  Hyphae infiltrate and bind agricultural waste (hemp hurds, corn stalks,
    straw, wood chips) → mycelium binds particles into rigid composite
  → Grown into molds → heat-killed → dried → fire retardant material

ECOVATIVE DESIGN (founded 2007, Green Island, NY):
  Founders: Eben Bayer + Gavin McIntyre (Rensselaer Polytechnic)
  Process:
    1. Mix agricultural waste + Ganoderma resinaceum (or similar) spawn
    2. Pack into molds
    3. Dark incubation: mycelium grows through waste, binds it
    4. 5–7 days: full colonization
    5. Heat-kill at 60°C to stop growth
    6. Dried product: rigid, lightweight composite
  Properties:
    Compressive strength: comparable to polystyrene foam (EPS)
    Fire retardant (no added chemicals): chitin + protein naturally flame-resistant
    Hydrophobic after treatment
    Fully compostable: home compost in 45 days
  Applications:
    Packaging: Dell (server packaging); IKEA (furniture packaging, 2019 pilot)
    Insulation panels: mycelium boards vs. mineral wool
    Building materials: acoustic panels
    Design objects: Ecovative licensed technology + direct product sales
  Scale: Ecovative now makes both mycelium packaging and foam-alternative

MYCELIUM LEATHER AND TEXTILES:
  Bolt Threads (San Francisco): Mylo™ material
    → Ganoderma species mycelium grown on hemp/corn agricultural waste
    → Harvested, processed like leather (tanning analogues)
    → Properties: flexible, suede-like, durable
    → Partners: Stella McCartney, Lululemon, Hermès (pilot), Ganni
  MycoWorks (San Francisco): Reishi™ (Fine Mycelium)
    → Proprietary 3D growth platform → controlling mycelium density
    → Hermès: shelf bag in Reishi mycelium leather (2021, "Sylvania")
    → Extremely tight fine mycelium → mechanical properties closer to
       traditional leather than earlier composites
<!-- @editor[content/P2]: Mycelium materials market status dated 2024 — check whether Bolt Threads (Mylo) and MycoWorks (Reishi) have scaled, pivoted, or folded since then; this is a fast-moving space -->
  Limitations (2024): price still premium vs. synthetic alternatives;
    scaling production challenging; durability data still being gathered

FUNGAL-BASED CONSTRUCTION (research/emerging):
  Mycelium bricks: Ecovative + academic research
    → Load-bearing capacity: research building blocks
  Self-healing mycelium concrete (research): incorporating fungi that can
    precipitate calcite (carbonate) to fill cracks
  Living mycelium structures: "Hy-Fi" pavilion (MoMA PS1, 2014):
    first large architectural structure from mycelium + corn stover
    → Completely composted after installation
```

---

## Bioremediation and Biocontrol

```
MYCOREMEDIATION:
  Term popularized by Paul Stamets (Fungi Perfecti, 1999 book "Mycelium Running")
  Ligninase systems of white rot fungi degrade:
    Polycyclic aromatic hydrocarbons (PAHs): petroleum contaminants
    → Laccase + Mn-peroxidase + lignin peroxidase have broad substrate specificity
    → Same enzymes that depolymerize lignin can oxidize PAHs
    TNT and related nitroaromatics (military site contamination)
    Dioxins (chlorinated aromatics): demonstrated in lab; field scale limited
    Some pharmaceuticals and endocrine disruptors in wastewater

  FIELD REALITY vs. HYPE:
    Lab demonstrations: impressive; many compounds degraded
    Field applications: fewer success stories
    Challenges:
      → Fungi compete poorly with indigenous soil microbiome
      → Water activity, O₂, pH must be correct
      → Inoculated fungus often out-competed within weeks
      → Best results in controlled conditions (biopiles, bioreactors)
    Honest assessment: mycoremediation is a useful tool in the toolkit,
      not the universal solution sometimes portrayed in popular science

FUNGAL BIOPESTICIDES:
  Beauveria bassiana: Hyphomycete; infects wide range of insects
    → Cuticle penetration → systemic infection → insect death
    → Commercial products: BotaniGard (thrips, whiteflies, aphids)
    → Advantage: narrow host range vs. broad-spectrum chemical insecticides
    → Spore formulation; apply like a pesticide spray

  Metarhizium anisopliae: locusts (primary biocontrol use in Africa)
    → Green Muscle biopesticide for African migratory locust
    → Phase II/III: slower than chemical but no environmental toxicity
    → Mycotoxin beauvericin produced → contributes to insect kill

  Trichoderma spp.: biocontrol OF fungi (hyperparasite)
    → Applied to soil/roots → antagonist of plant pathogens
    → Mechanisms: mycoparasitism + competition + antibiosis
    → Also: plant growth promotion via IAA and cytokinin release
    → Commercial: RootShield, Trianum, Plantsman — >$200M market

  Lecanicillium (Verticillium) lecanii: aphids, whitefly, scale insects
    → Greenhouse applications

BIOCONTROL MECHANISM TABLE:
  Mechanism        | Example               | Target
  -----------------|-----------------------|---------------------------
  Mycoparasitism   | Trichoderma spp.      | Fusarium, Botrytis in soil
  Cuticle invasion | Beauveria bassiana    | Thrips, whiteflies, beetles
  Competition      | Trichoderma spp.      | Root pathogens
  Antibiosis       | Trichoderma harzianum | Soil-borne pathogens
  Systemic killing | Metarhizium           | Locusts, termites
```

---

## Fungal Biofuels

```
THE LIGNOCELLULOSIC CHALLENGE:
  Second-generation biofuel: ethanol from agricultural waste
    (corn stover, wheat straw, sugarcane bagasse, wood chips)
  Problem: cellulose/hemicellulose locked in recalcitrant lignin matrix
  Solution: PRETREAT → SACCHARIFY (enzymes) → FERMENT (yeast)

  SACCHARIFICATION: the fungal role
  Trichoderma reesei cellulase cocktail:
    Cellobiohydrolase I (Cel7A): 60% of secretome; attacks crystalline cellulose
    Cellobiohydrolase II (Cel6A): complementary attack
    Endoglucanases (multiple): internal cleavage
    β-glucosidase: cellobiose → glucose (prevents product inhibition)
  T. reesei secretes up to 100 g/L protein, mostly cellulases
  → Novozymes, DSM Biosite: commercial cellulase products
  → Cellic CTec series: optimized for lignocellulosic conversion

  FERMENTATION:
  Conventional: saccharification then fermentation (SHF) or simultaneous
    saccharification and fermentation (SSF) with S. cerevisiae
  Next generation: consolidated bioprocessing (CBP) —
    single organism does all steps
    → Clostridium thermocellum (bacterial) — leading CBP candidate
    → Neurospora crassa: natural cellulolytic Ascomycete;
       genetics well understood; used as model for CAZyme (carbohydrate-
       active enzyme) discovery
    → S. cerevisiae engineered with cellulase genes: research ongoing

  LIPID-BASED BIOFUELS:
  Oleaginous yeasts/fungi: accumulate triacylglycerol >20% dry weight
    Mortierella alpina: ~50% fat; docosahexaenoic acid (DHA) producer
      → Commercial DHA for infant formula (Martek/DSM process)
      → Also used in omega-3 supplements (vegan DHA = this fungus)
    Yarrowia lipolytica: oleaginous yeast; model for lipid engineering
    Cunninghamella echinulata: high PUFA content
  Algae-to-fungus comparison: fungi easier to ferment; no light requirement

MYCO-BASED PLASTICS:
  Itaconic acid from A. terreus → building block for biopolymers
    (methacrylic acid substitute; can make acrylics bio-derived)
  Polyhydroxyalkanoates (PHAs): some fungal production (research)
  Lactic acid: Rhizopus oryzae produces L-lactic acid (PLA precursor)
    → Polylactic acid (PLA): compostable bioplastic
    → Rhizopus fermentation vs. bacterial Lactobacillus both in use
```

---

## Fungal Genomics and Engineering

```
GENOME RESOURCES:
  S. cerevisiae (1996): first eukaryotic genome sequenced
    → ~6,000 genes; 12 Mb; benchmark for all eukaryote genomics
    → Gene deletion library: every gene deleted; phenotype database
    → Global protein interaction (yeast 2-hybrid) maps
  Neurospora crassa: classical genetics model; genome 2003
  Aspergillus nidulans: genetics model; secondary metabolite gene clusters
  Aspergillus niger: genome enables metabolic engineering for organic acids
  JGI MycoCosm: >2,000 fungal genomes; public database

SECONDARY METABOLITE GENE CLUSTERS:
  Fungal secondary metabolites (antibiotics, statins, mycotoxins):
    encoded in genomic clusters (co-regulated genes adjacent)
  NRPS clusters: penicillin, cephalosporin, cyclosporine
  PKS clusters: lovastatin, aflatoxin, citrinin
  Terpene clusters: gibberellins (plant hormones), paclitaxel pathway
  Discovery approach: bioinformatics → find cluster → heterologous expression
  → Hundreds of uncharacterized clusters in sequenced genomes
  → "Genome mining": major source of new natural product leads

METABOLIC ENGINEERING:
  Aspergillus niger for citric acid: strain engineering via:
    → Overexpressing citrate synthase
    → Deleting competing pathways (isocitrate dehydrogenase knockouts)
    → Promoter replacement for constitutive expression
  Yeast metabolic engineering:
    → Artemisinin semi-synthesis: Amyris engineered S. cerevisiae to
       produce artemisinic acid (precursor to malaria drug artemisinin)
       → 2013 industrial fermentation: billions of doses
    → Opioid precursors: Berkeley group (2015) engineered yeast with
       25-step pathway to produce thebaine/hydrocodone from glucose
    → This is the same logic as software refactoring: extract a pathway,
       optimize it, plug in new modules
```

---

## Decision Cheat Sheet

| Application | Organism | Product/Function | Scale |
|-------------|----------|-----------------|-------|
| Antibiotics | Penicillium rubens | Penicillin G (β-lactam) | Megatonne APIs |
| Citric acid | Aspergillus niger | E330 acidulant | ~2M t/year |
| Starch processing | A. oryzae / A. niger | α-Amylase, glucoamylase | Largest enzyme market |
| Cellulosic biofuel | Trichoderma reesei | Cellulase cocktail | Commercial enzyme products |
| Immunosuppressant | Tolypocladium inflatum | Cyclosporine | Organ transplant medicine |
| Statins | A. terreus / P. citrinum | Lovastatin → semisynthetics | Best-selling drug class |
| Koji/fermented foods | A. oryzae | Amylases, proteases | Soy sauce, sake, miso |
| Mycoprotein | Fusarium venenatum | Quorn (~22,000 t/year) | 17-country market |
| Packaging | Ganoderma sp. | Mycelium composite | Growing; IKEA, Dell |
| Mycoleather | Bolt Threads; MycoWorks | Mylo / Reishi | Premium fashion |
| Biocontrol | Trichoderma spp. | Hyperparasite of pathogens | >$200M market |
| Insect biocontrol | Beauveria bassiana | Entomopathogen | Greenhouse crops |
| DHA omega-3 | Mortierella alpina | Docosahexaenoic acid | Infant formula |

---

## Common Confusion Points

**The Peoria strain is the mother of all industrial penicillin**: Every kilogram of penicillin (and amoxicillin, ampicillin, and derived cephalosporins) produced since WWII traces to a moldy cantaloupe found in an Illinois market. Fleming discovered the phenomenon; the Peoria strain made it industrial. This distinction matters: scientific discovery and industrial development are different problems requiring different skills.

**Citric acid does not come from citrus**: Since the 1920s, essentially all industrial citric acid is fermented by Aspergillus niger, not extracted from lemons or oranges. The Italian lemon industry was economically destroyed by this transition. Fermentation economics overwhelm agricultural extraction.

**Quorn is not soy**: Quorn is made from Fusarium venenatum (a filamentous fungus), not a plant. It is a distinct product from tofu (soy protein) or tempeh (whole soy + Rhizopus). The fibrous mycelium texture is intrinsic, not processed.

**Koji is a mold, not a bacterium**: The umami character of Japanese and East Asian fermented foods (soy sauce, miso, sake) comes largely from Aspergillus protease and amylase activity — a mold doing enzymatic work before bacteria or yeast take over. The mold is step one; yeast and bacteria are later. Traditional "beneficial bacteria" narratives often skip the fungal step entirely.

**Mycoremediation works in the lab but is harder in the field**: The enzymatic chemistry is real — laccases and peroxidases do degrade PAHs, TNT, dioxins. The ecological challenge is that introduced fungi are outcompeted in complex soil microbiomes. Biopiles (mixed substrate in controlled piles) work better than in situ inoculation. Do not over-generalize from laboratory demonstrations.

**Statins came from fungi before chemists redesigned them**: Lovastatin is a fungal secondary metabolite (A. terreus). Simvastatin and atorvastatin are semisynthetic or synthetic analogs of lovastatin. The entire $30B+/year statin market traces to Akira Endo's discovery of compactin from Penicillium in 1973 — a direct parallel to Fleming's β-lactam discovery, right down to the fungal origin and decades of optimization before mass production.
