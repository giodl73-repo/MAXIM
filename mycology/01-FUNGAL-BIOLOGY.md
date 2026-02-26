# Fungal Biology

## The Big Picture

```
+------------------------------------------------------------------+
|                    FUNGAL CELL BIOLOGY                           |
|                                                                  |
<!-- @editor[diagram/P2]: Diagram shows cell components in parallel columns but doesn't show the layered architecture (wall → membrane → cytoplasm → nucleus) as a system — rework as concentric-layer or cross-section view -->
|  CELL WALL          MEMBRANE         CYTOPLASM                  |
|  Chitin + glucan    Ergosterol       Organelles (ER, Golgi,     |
|  (NOT cellulose)    (NOT cholesterol) mitochondria, vacuoles)   |
|       |                  |                                       |
|       v                  v                                       |
|  GROWTH AT TIPS     ANTIFUNGAL       NUCLEI (can be multiple    |
|  (apical extension) TARGET           per cell if aseptate)      |
|                                                                  |
|  NUTRITION: osmotrophic                                         |
|  Secrete enzymes externally → absorb small molecules           |
|  No phagocytosis; no photosynthesis                            |
+------------------------------------------------------------------+
```

---

## Cell Wall

The fungal cell wall is the defining structural feature and the primary target of antifungal drugs.

```
FUNGAL CELL WALL LAYERS (inside to outside):
+--------------------------------------------------+
|  Plasma membrane (ergosterol)                   |
|  β-1,3-glucan layer (branched polysaccharide)  |
|  β-1,6-glucan crosslinks                       |
|  Chitin fibres (embedded in glucan)             |
|  α-1,3-glucan + galactomannan (outer layer)    |
|  Mannoproteins (surface glycoproteins)          |
+--------------------------------------------------+

CHITIN: poly-N-acetylglucosamine (β-1,4 linkages)
  Same polymer as insect exoskeleton and crustacean shells
  NOT found in animal cells (fungi-specific)
  → Target for antifungal drugs (but limited clinical agents exploit it)
  Echinocandins (caspofungin, micafungin): inhibit β-1,3-glucan synthase
    → Damages cell wall → cell lysis
    → Very low mammalian toxicity (no mammalian cell wall to damage)

ERGOSTEROL in membrane:
  Analogous to cholesterol in animal membranes (same general function)
  Chemically distinct from cholesterol
  → Target for polyene antifungals: Amphotericin B binds ergosterol →
    membrane pores → ion leakage → cell death
    (high toxicity: binds somewhat to cholesterol too → kidney damage)
  → Target for azole antifungals: fluconazole, itraconazole
    Inhibit ergosterol biosynthesis (CYP51 inhibition)
    → Depletion of ergosterol → fungistatic effect
```

---

## Hyphal Growth

```
APICAL EXTENSION MODEL:
  Hyphae grow ONLY at their tips (apex)
  Not by cell division along the length
  Vesicles (Spitzenkörper: "tip body") at apex deliver:
    → Cell wall precursors
    → Secretory vesicles (enzymes)
    → Membrane components

  SPITZENKÖRPER: fungal-specific structure
    Composed of vesicles aggregated near growing tip
    Acts as distributor for vesicle fusion with plasma membrane
    Controls direction of hyphal growth
    When Spitzenkörper displaced → hyphal branching

  BRANCH FORMATION:
    New Spitzenkörper forms → new branch
    Branching angles, frequencies: species-specific
    → Colony morphology on agar plates reflects branching pattern

  GROWTH RATES:
    Neurospora crassa (bread mold): up to 5 cm/hr
    Arbuscular mycorrhizal fungi: much slower
    Growth rate = measure of metabolic activity and carbon supply
```

---

## Septa and Nuclear Distribution

```
SEPTATE HYPHAE (most Ascomycetes and Basidiomycetes):
  Cross-walls (septa) divide hyphae into compartments
  Septa have CENTRAL PORES (not solid walls)
  → Cytoplasm and organelles can move between compartments
  → Nuclei can migrate through pores

ASCOMYCETE SEPTA:
  Simple septal pore blocked by Woronin bodies under stress
  → Woronin body plugs pore if cell damaged (compartmentalizes damage)
  → Like a circuit breaker

BASIDIOMYCETE SEPTA (dolipore):
  More complex: barrel-shaped parenthesome caps
  → Larger central channel; more regulated nuclear movement
  → Clamp connections: structure that allows nuclear migration during mating

ASEPTATE (COENOCYTIC) HYPHAE (Mucoromycota):
  No septa → one continuous cytoplasm with many nuclei
  → Multinucleate "supercell"
  → Nuclear mitoses not synchronized with cell division
  → Consequence: if damaged, whole mycelium can be affected faster

NUCLEAR STATES:
  Haploid (n): most vegetative growth
  Dikaryotic (n+n): two nuclei per cell from two mating types
    (key stage in Basidiomycetes; can persist for years)
  Diploid (2n): brief; usually only at karyogamy (nuclear fusion) before meiosis
```

---

## Nutrition: Osmotrophy

```
OSMOTROPHIC NUTRITION (feeding by absorption):
  1. SECRETE ENZYMES into environment
     Cellulases: break cellulose → glucose
     Ligninases / peroxidases: break lignin (unique to fungi + bacteria)
     Proteases: break proteins → amino acids
     Amylases: break starch → glucose
     Lipases: break fats → fatty acids

  2. SMALL MOLECULES diffuse back into hyphae
     Glucose, amino acids, short peptides, inorganic ions

  3. TRANSPORT PROTEINS in plasma membrane
     Active uptake against gradient
     Species-specific transporters for sugars, amino acids, vitamins

COMPARISON TO OTHER NUTRITIONAL STRATEGIES:
+--------------------------------------------------+
|  Strategy      | Who         | Mechanism        |
+--------------------------------------------------+
|  Photosynthesis| Plants, algae| Light → carbon  |
|  Ingestion     | Animals     | Eat whole food   |
|  Osmotrophy    | Fungi       | External digestion|
|  Heterotrophy  | Bacteria    | Various          |
+--------------------------------------------------+

NUTRITIONAL CATEGORIES OF FUNGI:
  Saprotrophic: feed on dead organic matter (decomposers)
  Mycorrhizal: mutualistic with plant roots (receive photosynthate)
  Parasitic: derive nutrients from living hosts (harmful to host)
  Endophytic: live in living plant tissue (neutral to beneficial)
```

---

## Spore Types and Dispersal

Spores are the primary means of reproduction and dispersal. Fungi produce an extraordinary diversity of spore types.

```
ASEXUAL SPORES:
  CONIDIA: produced at tips of conidiophores (specialized hyphae)
    → Aspergillus: characteristic radiate heads of conidia
    → Penicillium: brush-like conidiophores ("penicillus" = paintbrush)
    → Produced in enormous numbers: billions/m²
    → Inhaled constantly; usually harmless

  SPORANGIOSPORES: produced in sporangia (Mucoromycota)
    → Bread mold (Rhizopus): black sporangia visible to naked eye

  ARTHROSPORES: hyphae fragment directly into spore-like segments
    → Coccidioides: dangerous; can be inhaled → valley fever

SEXUAL SPORES:
  ASCOSPORES: produced in asci (Ascomycota)
    → 4 or 8 spores per ascus (product of meiosis)
    → Forcibly discharged in many species

  BASIDIOSPORES: produced on basidia (Basidiomycota)
    → Typically 4 spores on sterigmata (short protrusions)
    → Forcibly discharged; land on still air surface first
    → "Gill" surface of mushroom = billions of basidia → millions of spores

  ZYGOSPORES: thick-walled resting spores from sexual fusion (Mucoromycota)

DISPERSAL MECHANISMS:
  Wind: most spores; aerodynamically optimized
  Water splash: rain impact → aerosol
  Animals: sticky spores adhere to insects/animals (myrmecochory)
  Ballistic ejection: Pilobolus shoots sporangia at dung → parasitize grazers
  Self-burial: hygroscopic structures drill into substrate
```

---

## Fungal Life Cycles and Reproduction

```
GENERALIZED FUNGAL LIFE CYCLE:
  Haploid mycelium (n) + Haploid mycelium (n) [compatible mating types]
       ↓
  PLASMOGAMY (cytoplasm fusion; nuclei not yet fused)
       ↓
  DIKARYON STAGE (n + n) — extended in Basidiomycetes
       ↓
  KARYOGAMY (nuclear fusion → 2n)
       ↓
  MEIOSIS → 4 haploid nuclei
       ↓
  SPORE FORMATION → dispersal → germination → new mycelium (n)

MATING TYPES:
  Not "male" and "female" — mating type genes control compatibility
  Two-mating-type system: most Ascomycetes
  Multiple mating types: some Basidiomycetes
    Coprinopsis cinerea (ink cap): 23,000 mating types
    → Any individual can mate with almost any other individual
  Self-fertile (homothallic) vs. obligate outcrossing (heterothallic)

PARASEXUAL CYCLE (Ascomycetes especially):
  Genetic exchange without meiosis
  Hyphal fusion → heterokaryosis (mixed nuclei) → rare diploidization
  → Mitotic recombination → haploidization
  → Generates genetic variation without sexual cycle
  Important for: Aspergillus niger (industrial); non-sexual pathogens
```

---

## Dimorphism
<!-- @editor[bridge/P3]: Natural bridge to state machines / mode switching — dimorphic fungi are biological finite state machines with environmental transition triggers. Worth a one-liner for this learner. -->

Some fungi switch between forms depending on conditions:

```
DIMORPHIC FUNGI:
  Mold form (mycelial, room temperature) ↔ Yeast form (unicellular, body temperature)

  HISTOPLASMA CAPSULATUM:
    Mold in soil (23°C) → infective spores inhaled
    Yeast in lung tissue (37°C) → pathogenic state
    Temperature is the switch signal

  CANDIDA ALBICANS:
    Yeast form: commensal in gut (normal state)
    Hyphal/pseudohyphal form: invasive; tissue penetration
    Switch triggered by: temperature, pH, CO₂, serum, contact surfaces
    → Hyphal switching = virulence switch

  SPOROTHRIX SCHENCKII:
    Mold in environment; yeast in infected tissue
    "Rose thorn disease": inoculation through skin puncture

CLINICAL SIGNIFICANCE:
  Dimorphism = morphological switch = virulence switch in many pathogens
  → Targeting the switch (e.g., Hsp90 chaperone) is a therapeutic strategy
```

---

## Decision Cheat Sheet

| Property | Fungi | Plants | Animals |
|----------|-------|--------|---------|
| Cell wall material | Chitin | Cellulose | None |
| Membrane sterol | Ergosterol | Phytosterols | Cholesterol |
| Nutrition | Osmotrophic | Photosynthetic | Phagotrophic |
| Carbon storage | Glycogen | Starch | Glycogen |
| Growth mode | Apical extension | Meristematic | Interstitial |
| Closely related to | Animals | Plants | (answer depends) |

---

## Common Confusion Points

**Yeast is a fungus, not a separate kingdom**: Yeasts are unicellular fungi — specifically the unicellular growth form of some Ascomycetes and Basidiomycetes. Saccharomyces cerevisiae is an Ascomycete; Cryptococcus is a Basidiomycete. "Yeast" is a growth form, not a phylogenetic category.

**Antifungal resistance is increasing**: Azole (fluconazole) resistance in Candida and Aspergillus is growing — particularly Candida auris which is resistant to multiple drug classes. The mechanism is often upregulation of efflux pumps (Cdr1/2 in Candida) or CYP51 mutations. Parallels to antibiotic resistance in bacteria.

**Ergosterol target vs. cholesterol toxicity**: Amphotericin B binds ergosterol with high affinity but also has some affinity for cholesterol → explains kidney toxicity. Azoles are more selective (inhibit fungal CYP51 preferentially over human CYP51) → lower toxicity but more drug interactions (human CYPs affected).

**Coenocytic vs. septate**: Coenocytic (aseptate) fungi (most Mucoromycota) have continuous cytoplasm with many nuclei. When something damages the hyphae, there's no compartmentalization to limit damage. This is also why certain antifungals can be more destructive to coenocytic fungi (cytoplasm disruption spreads).
