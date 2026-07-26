---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:biochemistry:overview
kind: guide
module: biochemistry
section: biochemistry
title: Biochemistry - Overview
status: source-custody
source_custody: partial
current_path: biochemistry/00-OVERVIEW.md
canonical_path: biochemistry/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:biochemistry:00-overview, git-history:biochemistry:00-overview]
concepts: [biochemistry, metabolism, bioenergetics, biomolecules, enzymes]
root_concepts: [biochemistry]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Biochemistry — Overview

```
+------------------------------------------------------------------------+
|                  BIOCHEMISTRY: THE CHEMISTRY OF LIFE                   |
|                                                                        |
|   INPUTS                  TRANSFORMS                  OUTPUTS          |
|   (fuel + matter)         (enzyme network)            (work + waste)   |
|                                                                        |
|   glucose      ---.                              .--> ATP (energy)     |
|   fatty acids  ---+--> [ CATABOLISM ]  --------->+--> NADH / FADH2     |
|   amino acids  ---'      breaks down             '--> CO2 + H2O        |
|                              |                                         |
|                              v                                         |
|                      .---------------.                                 |
|                      |  ATP / NADPH  |  shared energy + reducing       |
|                      |  CARRIER POOL | currency couples the two halves |
|                      '---------------'                                 |
|                              |                                         |
|                              v                                         |
|   CO2          <--.      [ ANABOLISM ]  <--------.                     |
|   small         --+--<   builds up               +--< ATP / NADPH      |
|   precursors    --'                              '--< drawn from pool  |
|                  '--> proteins, membranes, nucleic acids, glycogen     |
|                                                                        |
|   REGULATION: allosteric feedback + covalent modification + hormones   |
|   keep flux through this network matched to demand (control theory).   |
+------------------------------------------------------------------------+
```

Biochemistry is the **operating system of the cell**: a few thousand small
molecules and a few thousand protein machines, wired into a directed graph of
chemical reactions. Read the diagram as a pipeline — fuel flows in, gets broken
down to harvest energy into a shared carrier pool (ATP, NADH), and that pool
powers the construction of everything the cell needs.

A software reader can hold the whole field with one analogy: **metabolism is a
dataflow graph with a global resource budget**. Nodes are metabolites, edges are
enzyme-catalyzed reactions, and ATP/NADPH are the shared currency that makes some
edges run "downhill" (spontaneous) and forces others to be paid for. Regulation
is the scheduler.

---

## The Four Questions Biochemistry Answers

```
+------------------------------------------------------------------------+
|  1. WHAT are cells made of?      -> Biomolecules (01)                  |
|     carbohydrates, lipids, proteins, nucleic acids + water/pH          |
|                                                                        |
|  2. HOW do molecules get their shape and function?                     |
|     -> Protein structure + folding (02)                                |
|                                                                        |
|  3. HOW are reactions made fast and selective enough for life?         |
|     -> Enzymes + kinetics (03)                                         |
|                                                                        |
|  4. HOW do cells extract, store, and spend energy?                     |
|     -> Metabolism + bioenergetics (04-08)                              |
|                                                                        |
|  + GLUE: How is all of this coordinated? -> Signaling/regulation (09)  |
+------------------------------------------------------------------------+
```

---

## Bridge: Old World → New World

The learner already has a complete model of computation. These mappings are
load-bearing — use them throughout the directory.

| Software / systems concept | Biochemical analog |
|---|---|
| Energy budget / resource quota | ATP pool; cells run at ~tens of mM ATP, turned over fast |
| Shared bus / message currency | ATP carries phosphoryl-transfer energy between reactions |
| Reducing/oxidizing as a "credit" | NADH/NADPH carry electrons (reducing power) |
| Dataflow graph | Metabolic pathway map (nodes = metabolites, edges = enzymes) |
| Function call with a catalyst | Enzyme: lowers activation energy, unchanged by reaction |
| Rate limiter / bottleneck | Committed/regulated step (e.g., PFK-1 in glycolysis) |
| Feedback control loop | Allosteric inhibition by end product |
| Config flag / runtime patch | Covalent modification (phosphorylation toggles activity) |
| Hardware vs. software | Enzyme = hardware accelerator; substrate = data |
| Free energy ΔG | "Will this run on its own?" ΔG<0 spontaneous; ΔG>0 needs power |

The single most important bridge: **ΔG is the "is this edge enabled?" predicate.**
A reaction with ΔG < 0 is favorable and proceeds; one with ΔG > 0 must be
**coupled** to ATP hydrolysis (a strongly negative-ΔG reaction) to run. This is
exactly how a scheduler borrows from a resource budget to run an otherwise
impossible task.

---

## The Energy Currency Layer

Everything in metabolism routes through three reusable carriers. Memorize these;
they recur in every later file.

```
+------------------------------------------------------------------------+
|  CARRIER       CARRIES          CHARGED FORM    SPENT FORM             |
|  -------       -------          ------------    ----------             |
|  ATP           phosphoryl /     ATP             ADP + Pi               |
|                free energy      (3 phosphates)  (2 phosphates)         |
|                                                                        |
|  NAD+ / NADH   2 electrons +    NADH            NAD+                   |
|                1 H+ (catabolic) (reduced)       (oxidized)             |
|                                                                        |
|  NADP+/NADPH   2 electrons +    NADPH           NADP+                  |
|                1 H+ (anabolic)  (reduced)       (oxidized)             |
|                                                                        |
|  FAD / FADH2   2 electrons +    FADH2           FAD                    |
|                2 H+            (reduced)       (oxidized)              |
+------------------------------------------------------------------------+
```

**ATP hydrolysis** (ATP + H2O -> ADP + Pi) releases about -30.5 kJ/mol under
standard conditions and closer to -50 to -60 kJ/mol inside a real cell (because
the actual ATP:ADP ratio is far from equilibrium). Cells keep ATP held high so
the "discharge" reaction stays strongly favorable — like keeping a capacitor
charged so it can always deliver a pulse.

**NADH vs NADPH** is a deliberate accounting split, not chemistry: the two
molecules differ by one phosphate group that does nothing energetically but lets
enzymes tell them apart. NADH feeds **catabolism toward ATP production**; NADPH
feeds **anabolism (biosynthesis)**. Same electrons, separate ledgers — like
having a "revenue" account and a "capital" account that hold identical dollars
but are never commingled.

---

## The Metabolic Map (Where Each File Lives)

```
+------------------------------------------------------------------------+
|                         FUEL MOLECULES                                 |
|     carbohydrates        fats              proteins                    |
|         |                 |                   |                        |
|         v                 v                   v                        |
|     GLYCOLYSIS        BETA-OXIDATION      transamination               |
|       (05)               (07)               (07)                       |
|         |                 |                   |                        |
|         v                 |                   v                        |
|     pyruvate              |              carbon skeletons              |
|         |                 |                   |                        |
|         v                 v                   v                        |
|     +------------------ acetyl-CoA -------------------+                |
|                            |                                           |
|                            v                                           |
|                     TCA / CITRIC ACID CYCLE  (06)                      |
|                            |                                           |
|                   produces NADH, FADH2, GTP, CO2                       |
|                            |                                           |
|                            v                                           |
|              ELECTRON TRANSPORT CHAIN + ATP SYNTHASE  (06)             |
|                  NADH/FADH2 -> proton gradient -> ATP                  |
|                                                                        |
|   PHOTOSYNTHESIS (08): the reverse logic — light -> ATP/NADPH ->       |
|   fix CO2 into sugar. Plants run the whole map backward in daylight.   |
+------------------------------------------------------------------------+
```

Acetyl-CoA is the **central hub** — the metabolite where carbohydrate, fat, and
protein catabolism converge. If you remember one node, remember this one.

---

## A Note on Stoichiometry (Why the Numbers Matter)

Biochemistry is quantitative. The headline numbers are worth committing because
they are easy to get wrong (older textbooks did):

| Quantity | Correct value | Common error |
|---|---|---|
| Glycolysis net ATP (per glucose) | **2 ATP** | confusing gross (4) with net |
| Glycolysis NADH (per glucose) | **2 NADH** | — |
| Glycolysis pyruvate (per glucose) | **2 pyruvate** | — |
| Complete oxidation of glucose | **~30–32 ATP** | the old **36–38** figure |
| ATP per NADH (oxidative phos.) | **~2.5** | the old whole-number **3** |
| ATP per FADH2 | **~1.5** | the old whole-number **2** |

The modern ~30–32 ATP figure replaced the textbook 36–38 once the **proton
stoichiometry** of ATP synthase was actually measured: ATP synthase needs about
**4 protons per ATP** (3 to spin the rotor + 1 for transport), and the shuttle
that moves cytosolic NADH into mitochondria costs energy. The old numbers assumed
clean integer ratios that the machinery does not honor. File `06` derives this in
full.

---

## Decision Cheat Sheet

| I want to understand... | Read |
|---|---|
| What molecules life is built from | `01-BIOMOLECULES.md` |
| Why water/pH matter so much | `01-BIOMOLECULES.md` (water section) |
| How a protein gets its 3D shape | `02-PROTEIN-STRUCTURE.md` |
| How enzymes speed reactions; Km/Vmax | `03-ENZYMES-AND-KINETICS.md` |
| The shared ATP/NADH currency model | `04-METABOLISM-OVERVIEW.md` |
| How glucose becomes pyruvate (+ ATP) | `05-GLYCOLYSIS-AND-GLUCONEOGENESIS.md` |
| Where most ATP actually comes from | `06-TCA-AND-OXIDATIVE-PHOSPHORYLATION.md` |
| How fats and amino acids are burned | `07-LIPID-AND-AMINO-ACID-METABOLISM.md` |
| How plants make sugar from CO2 + light | `08-PHOTOSYNTHESIS-AND-CARBON.md` |
| Hormones, signaling, second messengers | `09-MOLECULAR-AND-REGULATION.md` |
| DNA replication / transcription / translation | `biology/` (central dogma machinery) |
| Pure chemistry foundations | `natural-sciences/` |

---

## Common Confusion Points

### "Biochemistry vs. molecular biology — what's the line?"

```
  BIOCHEMISTRY            MOLECULAR BIOLOGY
  ------------            -----------------
  metabolism, energy      DNA -> RNA -> protein
  enzymes + kinetics      gene expression
  small-molecule flux     information flow
  "the chemistry"         "the central dogma"
```

They overlap heavily and the boundary is cultural, not real. This directory takes
the **chemistry/energy** half; the **information** half (replication,
transcription, translation) lives in `biology/`. File `09` bridges them.

### "Is metabolism really one giant graph, or separate pathways?"

It is one connected graph; "pathways" are just human-named subgraphs (high-traffic
routes) drawn on it. Acetyl-CoA, pyruvate, and the TCA intermediates are shared
junctions used by many pathways at once. Treat pathway names as labels on a single
network, not as isolated modules.

### "Why two reducing-power carriers (NADH and NADPH)?"

Pure bookkeeping. The extra phosphate on NADPH is an enzyme-readable tag that
keeps the "burn fuel for ATP" pool (NADH) separate from the "build molecules"
pool (NADPH), so the cell can run catabolism and anabolism in opposite directions
simultaneously without the two short-circuiting each other.

### "Does the cell ever store ATP?"

No — ATP is working capital, turned over in seconds (a human turns over roughly
their own body weight in ATP per day). Energy is *stored* as glycogen and fat;
ATP is just the spend-on-demand currency the stores get converted into.
