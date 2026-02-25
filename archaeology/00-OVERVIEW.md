# Archaeology — Landscape Overview

## The Big Picture

```
+------------------------------------------------------------------+
|                  ARCHAEOLOGY: THE DISCIPLINE MAP                 |
|                                                                  |
|  WHAT IS IT?                                                     |
|  The systematic study of human history and prehistory through   |
|  the recovery and analysis of material culture                  |
|                                                                  |
|  COVERS: from the first stone tools (~3.3 Ma) to yesterday's   |
|  industrial ruins — archaeology has no firm end date           |
|                                                                  |
|  ADJACENT DISCIPLINES                                           |
|  History (written records) ←→ ARCHAEOLOGY ←→ Anthropology      |
|  (cultural behavior)                                            |
|          ↕                            ↕                        |
|  Geology (stratigraphy)       Genomics (ancient DNA)           |
|  Physics (radiocarbon)        Chemistry (isotopes, residues)    |
|  Biology (zooarchaeology)     Linguistics (language spread)     |
+------------------------------------------------------------------+
```

---

## The Scope of Archaeology

```
TIME SPAN
+------------------------------------------------------------------+
|  Prehistoric: before written records (varies by region)         |
|  3.3 Ma    → First stone tools (Lomekwi, Kenya)                |
|  2.6 Ma    → Oldowan industry (Mode 1)                         |
|  1.7 Ma    → Acheulean (Mode 2); Homo erectus                  |
|  300 Ka    → Middle Stone Age / Middle Paleolithic             |
|  45 Ka     → Upper Paleolithic in Europe; behavioral modernity  |
|  12 Ka     → End of Pleistocene; start of Holocene            |
|  10 Ka     → Neolithic Revolution (farming); multiple regions  |
|  5 Ka      → Writing; Bronze Age; state societies             |
|  HISTORIC: parallel written record (varies by region)          |
|  Present   → Industrial archaeology; contemporary archaeology  |
+------------------------------------------------------------------+

GEOGRAPHIC SCOPE: every inhabited continent and ocean
  Terrestrial: excavation, survey, remote sensing
  Underwater: shipwrecks, submerged landscapes, ports
  Cave: Paleolithic art, refuges, burial caves
  Urban: salvage archaeology under modern cities
```

---

## Archaeology vs. History vs. Anthropology

```
DISCIPLINARY BOUNDARIES AND OVERLAPS
+------------------------------------------------------------------+
|                                                                  |
|  HISTORY: primary sources = written documents                   |
|  Coverage: literate societies, from their perspective           |
|  Limits: written record biased toward elites, victors, literate|
|                                                                  |
|  ANTHROPOLOGY: cross-cultural study of human behavior          |
|  4 subfields (US model): cultural, biological, linguistic,     |
|    archaeological anthropology                                  |
|  (In UK/Australia: archaeology is a separate discipline)        |
|                                                                  |
|  ARCHAEOLOGY: material culture, regardless of literacy         |
|  Fills where history is silent:                                |
|    → Prehistory (90%+ of human existence)                     |
|    → Non-literate or marginally-documented societies           |
|    → "History from below" — the enslaved, the peasant,        |
|       the colonized, those who left no written voice           |
|    → Diet, health, demography (bioarchaeology)                 |
|    → Trade networks, resource use, technology change           |
+------------------------------------------------------------------+
```

**Why archaeology matters when history exists**: Written records tell you what powerful people wrote down, in the language they chose, for their purposes. Archaeology tells you what people actually ate, wore, built, and discarded. The divergence between material record and written record is often the most interesting finding.

---

## Core Methodological Principles

```
THE ARCHAEOLOGICAL RECORD: formation processes

DEPOSITION EVENTS:
  Primary context: object deposited where it was used/discarded
  → Ash layer from volcano covers a site immediately
  → Sealed context: floor with objects in place

SECONDARY CONTEXT: object moved from original location
  → Redeposited fill, later disturbance, robbing out
  → Valuable for dating the fill, not the object itself

MATRIX: the material surrounding artifacts (soil, rubble, ash)
  → Context = the stratigraphic unit where something is found
  → Context number is the identity of that matrix unit
  → Single context recording: each layer gets a number

TAPHONOMY: how organic materials survive or decay
  → Bone: survives well in alkaline soil; dissolves in acid
  → Wood: survives waterlogged (anaerobic) or charred only
  → Metal: corrodes in salt/acid; gold inert; iron rusts
  → The absence of evidence ≠ evidence of absence
```

---

## The Stratigraphic Principle

**Steno's law (1669) → applied to archaeology by Pitt Rivers and Wheeler**:

In undisturbed deposits, lower layers are older than upper layers. Archaeological stratigraphy reads earth layers like version control — each layer is a "commit" with a time stamp, and the Harris Matrix is the dependency graph.

```
STRATIGRAPHIC SEQUENCE EXAMPLE
+------------------------------------------------------------------+
|  SURFACE                                                         |
|  [F.100] Modern concrete floor (20th c.)                        |
|  [F.099] Rubble fill layer                                      |
|  [F.098] Plaster floor surface (medieval)                       |
|  [F.097] Occupation deposit (ash, bone, pottery sherds)         |
|  [F.096] Construction trench for wall [W.045]                   |
|  [F.095] Pre-construction surface (earliest occupation)         |
|  [F.094] Natural subsoil (sterile)                              |
|  BEDROCK                                                         |
|                                                                  |
|  Each context (F.xxx) is an entity with:                        |
|  - Unique number (= "commit hash")                              |
|  - Matrix/fill description                                       |
|  - Stratigraphic relationships (above/below/cuts/is-cut-by)    |
|  - Associated finds (pottery, coins, etc.)                      |
|  - Physical samples (for dating, environmental analysis)        |
+------------------------------------------------------------------+
```

---

## The Harris Matrix

Invented by Edward C. Harris (1979). A directed acyclic graph (DAG) of stratigraphic relationships.

```
HARRIS MATRIX NOTATION
  [100] above [099] → 099 is older
  [097] cuts [095] → 095 was present when 097 was deposited

MATRIX RELATIONSHIPS:
  Superposition: A above B (A is younger)
  Correlation: A = B (same deposit, different trench)
  Cutting: A cuts B (A removed part of B; A is younger)

This is exactly a directed acyclic graph:
  Nodes = contexts (stratigraphic units)
  Edges = stratigraphic relationships (above/cuts)
  Topological sort = relative chronological sequence

  [100]
    |
  [099]
    |
  [098]     [097]
    \         /
      [096]
        |
      [095]
        |
      [094] (natural)
```

---

## Branches of Archaeology

| Branch | Focus | Key Methods |
|--------|-------|-------------|
| Prehistoric archaeology | Pre-writing human societies | Typology, radiocarbon, aDNA |
| Classical archaeology | Greece, Rome, Near East | Stratigraphy + texts + epigraphy |
| Medieval archaeology | Post-Roman Europe, Islamic world | Dendrochronology, ceramic sequence |
| Historical archaeology | Post-contact Americas, Colonial world | Material culture + documents |
| Underwater archaeology | Ships, ports, submerged coasts | In-situ recording, photogrammetry |
| Bioarchaeology | Human skeletal remains | Stable isotopes, aDNA, pathology |
| Geoarchaeology | Geological context of sites | Sediment analysis, micromorphology |
| Environmental archaeology | Past environments and human adaptation | Pollen, phytoliths, zooarchaeology |
| Digital archaeology | Remote sensing, GIS, 3D recording | LiDAR, photogrammetry, GIS |
| Experimental archaeology | How past techniques worked | Flint knapping, firing ceramics |

---

## The Theoretical Schools — Major Paradigm Shifts

```
CULTURE HISTORY (1880s–1960s):
  Goal: classify artifacts into types; map cultural groups
  Method: typology (artifact form → culture → period)
  Framework: cultures defined by characteristic assemblage types
  Limitation: assumed cultural change = migration or diffusion;
    little interest in WHY change happened
  Key figures: V. Gordon Childe, Mortimer Wheeler, O. G. S. Crawford

PROCESSUAL / NEW ARCHAEOLOGY (1960s–1980s):
  Goal: explain cultural change by systematic processes
  Inspired by: scientific method, systems theory, ecology
  Method: hypothesis testing; quantitative analysis
  Claims: archaeology can be a science with general laws
  Key figures: Lewis Binford, David Clarke, Kent Flannery
  Contributions: ecological adaptation, demographic models, settlement systems

POST-PROCESSUAL (1980s–present):
  Goal: understand meaning, symbolism, agency, identity
  Inspired by: poststructuralism, feminism, Indigenous perspectives
  Critique of processualism: "objectivity" is ideological; top-down
  Focus: individual agency, gender, ritual, ethnicity, power
  Key figures: Ian Hodder, Michael Shanks, Christopher Tilley
  Contributions: attention to context-specificity; political reflexivity

CURRENT PRACTICE:
  Pluralistic — borrows from all three
  Digital/computational archaeology growing
  Indigenous archaeology and descendant community engagement now central
```

---

## File Guide

| File | Topic | Core Concept |
|------|-------|--------------|
| 01-FIELD-METHODS | Survey, excavation, recording | Stratigraphy as version control |
| 02-DATING-METHODS | Radiocarbon, dendro, OSL, K-Ar | Physics of time measurement |
| 03-MATERIAL-ANALYSIS | Isotopes, aDNA, residues, XRF | Science behind artifacts |
| 04-PREHISTORY | Paleolithic to Bronze Age | Human evolution in material culture |
| 05-ANCIENT-CIVILIZATIONS | First cities and states | Comparative urbanism |
| 06-CLASSICAL-ARCHAEOLOGY | Greece, Rome, underwater | City form and material culture |
| 07-MEDIEVAL-ARCHAEOLOGY | Post-Roman Europe | Settlement patterns, economy |
| 08-HISTORICAL-ARCHAEOLOGY | Colonialism, slavery, industry | Material record vs. written record |
| 09-ARCHAEOLOGICAL-THEORY | Paradigm history | Culture history → processualism → post-processualism |

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What makes archaeology distinct from history? | Studies material culture regardless of literacy; includes 99%+ of human existence before writing |
| Why does context matter? | Decontextualized artifact = lost information; provenance is irreplaceable |
| What is primary vs. secondary context? | Primary = in situ, not moved; secondary = redeposited, disturbed |
| What is the Harris Matrix? | DAG of stratigraphic relationships — the relative chronology graph |
| How long has archaeology been a science? | Systematic stratigraphy: Pitt Rivers, Wheeler (late 19th–early 20th c.); scientific rigor: 1960s processualism |
| What replaced culture history? | Processualism (New Archaeology) — hypothesis testing, systems theory |

---

## Common Confusion Points

**Archaeology is not treasure hunting**: Scientific archaeology is about contextual data recovery. Once context is destroyed (by illicit digging), the information is gone permanently. A decontextualized Roman coin tells you coins existed; an in-situ coin tells you when the floor it lay on was in use.

**Artifact vs. feature vs. ecofact**: Artifact = human-made portable object (pot, tool). Feature = non-portable human-made or modified structure (wall, hearth, pit). Ecofact = natural material associated with human activity (bone, seed, charcoal) — not made by humans but informative about behavior.

**Prehistoric vs. historic**: The boundary varies enormously by region. Egypt has writing at ~3100 BC. Britain's Iron Age is prehistoric until the Roman conquest (43 AD). The American Southwest has written records only after Spanish contact (~1540 AD). Pre-literate ≠ primitive — Göbekli Tepe (10,000 BC) is architecturally complex.

**Antiquarianism vs. archaeology**: Before ~1850, objects were collected without stratigraphic context. Antiquarians (like John Aubrey at Stonehenge) documented but didn't excavate scientifically. General Pitt Rivers' Cranborne Chase excavations (1880s) are often cited as the start of systematic archaeological recording.
