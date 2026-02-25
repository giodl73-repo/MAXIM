# Life Sciences

13 directories · molecular chemistry through clinical medicine, with full coverage of the biological stack

---

## Landscape

```
╔══════════════════════════════════════════════════════════════════════════════════════════╗
║  MOLECULAR FOUNDATION                                                                    ║
║                                                                                          ║
║  ┌─────────────────────────────────────────────────────────────────────────────────┐    ║
║  │  natural-sciences/                                                              │    ║
║  │  Chemistry block: atomic/quantum · bonding · thermochem · kinetics · electrochem│    ║
║  │  Biochem block:   biomolecules · enzymes · metabolism · molecular-bio           │    ║
║  │  Biology block:   cell-biology · evolution/genetics · plasma science            │    ║
║  └──────────────────────────────────┬────────────────────────────────────────────-┘    ║
║                                     │ builds up                                         ║
╠═════════════════════════════════════▼═══════════════════════════════════════════════════╣
║  CELL TO ORGANISM                                                                        ║
║                                                                                          ║
║  ┌───────────────────┐     ┌─────────────────────┐     ┌────────────────────────┐      ║
║  │  biology/         │────▶│  botany/             │     │  ecology/              │      ║
║  │  cell structure   │     │  photosynthesis      │────▶│  ecosystems            │      ║
║  │  genetics         │     │  plant reproduction  │     │  food webs             │      ║
║  │  systems/synth bio│     │  taxonomy            │     │  population dynamics   │      ║
║  └───────────────────┘     └─────────────────────┘     │  biomes · conservation │      ║
║          │                                              └────────────────────────┘      ║
║          │ shared mechanisms                                    │                        ║
╠══════════▼══════════════════════════════════════════════════════╪════════════════════════╣
║  HUMAN SYSTEMS                                              specializes                 ║
║                                                                 ▼                        ║
║  ┌────────────────────────┐  ┌─────────────────┐   ┌──────────────────────────┐        ║
║  │  human-biology/        │  │  neuroscience/  │──▶│  cognitive-science/      │        ║
║  │  musculoskeletal       │  │  neurons/synap. │   │  perception · attention  │        ║
║  │  cardiovascular        │  │  circuits       │   │  memory · language       │        ║
║  │  nervous · endocrine   │  │  cognition      │   │  decision-making         │        ║
║  │  immune · renal · repro│  │  neuroimaging   │   │  consciousness · AI conn.│        ║
║  └────────────────┬───────┘  └─────────────────┘   └──────────────────────────┘        ║
║                   │ when systems fail                                                    ║
╠═══════════════════▼══════════════════════════════════════════════════════════════════════╣
║  HEALTH & DISEASE                                                                        ║
║                                                                                          ║
║  ┌─────────────────────┐   ┌──────────────────────┐   ┌──────────────────────┐         ║
║  │  disease/           │──▶│  medicine/            │   │  nutrition/          │         ║
║  │  infectious · cancer│   │  drug classes        │   │  macros · micros     │         ║
║  │  cardiovascular     │   │  antibiotics/antiviral│   │  dietary patterns    │         ║
║  │  metabolic          │   │  CNS · endocrine      │   │  gut microbiome      │         ║
║  │  autoimmune · neuro │   │  cancer · immuno.     │   │  nutritional epi.    │         ║
║  │  genetic disorders  │   │  diagnostics          │   │                      │         ║
║  └─────────────────────┘   └──────────────────────┘   └──────────────────────┘         ║
╚══════════════════════════════════════════════════════════════════════════════════════════╝

  Vertical axis: scale (molecular → cellular → organismal → population → clinical)
  Horizontal axis: breadth (generalist biology → human specialization → applied health)
```

---

## Directories

| Directory | Focus | Entry Point | Bridges to |
|-----------|-------|-------------|------------|
| `natural-sciences/` | Full chemistry and biochemistry stack — atomic structure through metabolism — plus cell biology, genetics, and plasma science | `01-ATOMIC-QUANTUM.md` for the physics-chemistry boundary; `06-BIOMOLECULES.md` to enter the biochem block | `physics/` (quantum ↔ atomic), `medicine/` (biochem mechanisms underlie drug targets), `ecology/` (thermochem ↔ energy flow) |
| `biology/` | Cell structure and organelles, genetics (Mendelian through molecular), evolution, systems biology, synthetic biology | `00-OVERVIEW.md` — covers central dogma and field taxonomy | `natural-sciences/` (shares cell-biology territory; read together), `botany/` and `ecology/` (evolutionary biology framework) |
| `botany/` | Plant anatomy, photosynthesis (light/dark reactions, C3/C4/CAM), sexual and asexual reproduction, taxonomy, ethnobotany | `01-PLANT-STRUCTURE.md` — structural foundation before biochemistry | `ecology/` (primary productivity, food webs), `agriculture/` (crop science), `natural-sciences/` (photosynthesis ↔ thermochem) |
| `ecology/` | Ecosystems and energy flow, food webs and trophic structure, population dynamics (Lotka-Volterra), biome classification, conservation biology | `01-ECOSYSTEMS.md` — establishes the systems framing | `geography/` (biomes ↔ climate zones), `climate-science/` (carbon cycle feedbacks), `botany/` (primary production), `paleontology/` (mass extinctions) |
| `human-biology/` | All major body systems: musculoskeletal, cardiovascular, nervous, endocrine, immune, renal, reproductive — physiology-first | `00-OVERVIEW.md` — systems map before diving per-system | `disease/` (each system has failure modes), `medicine/` (drug targets map to system physiology), `neuroscience/` (nervous system depth) |
| `neuroscience/` | Neuronal electrophysiology, synaptic transmission, circuit logic, systems-level cognition, neuroimaging methods (fMRI/EEG), synaptic plasticity and learning | `01-NEURONS.md` — start at the cell before circuits | `human-biology/` (nervous system context), `cognitive-science/` (circuits → behavior), `disease/` (neurological disorders), `medicine/` (CNS drug targets) |
| `cognitive-science/` | Perception, attention, working and long-term memory, language acquisition and processing, decision-making under uncertainty, consciousness theories, AI alignment connections | `00-OVERVIEW.md` — interdisciplinary map (neuroscience / psychology / linguistics / AI) | `neuroscience/` (neural substrates of cognition), `psychology/` (behavioral layer), `ai-engineering/` (cognitive architectures ↔ LLM design), `philosophy/` (mind, consciousness) |
| `disease/` | Infectious disease (bacterial, viral, fungal — mechanisms of pathogenicity), cancer biology (oncogenes, tumor microenvironment, immunoevasion), cardiovascular, metabolic, autoimmune, neurological, and genetic disorders | `01-INFECTIOUS.md` — covers the broadest category first | `medicine/` (disease mechanism → treatment class), `human-biology/` (normal physiology ↔ pathophysiology), `public-health/` (epidemiology of disease burden) |
| `medicine/` | Drug classes and mechanism of action: antibiotics (beta-lactams through fluoroquinolones), antivirals, cardiovascular agents, CNS drugs, endocrine pharmacology, cancer therapeutics, immunomodulators, diagnostics (imaging, lab, pathology) | `01-ANTIBIOTICS.md` — most mechanism variety, best entry for pharmacology logic | `disease/` (drug classes map to disease categories), `natural-sciences/` (molecular targets), `public-health/` (rational prescribing, AMR) |
| `nutrition/` | Macronutrient metabolism (carbs, lipids, protein), micronutrient biochemistry, major dietary patterns (Mediterranean, low-carb, plant-based) with evidence quality, gut microbiome composition and function, nutritional epidemiology and confounding | `01-MACRONUTRIENTS.md` — metabolic pathways before dietary patterns | `natural-sciences/` (metabolism block), `disease/` (metabolic disease, cancer, cardiovascular risk), `public-health/` (dietary policy), `medicine/` (therapeutic nutrition) |
| `genomics/` | Sequencing technology (Sanger → Illumina → nanopore → single-cell), genome assembly (de Bruijn graphs, telomere-to-telomere), variant calling (SNPs/indels/SVs, GATK pipeline), RNA-seq and differential expression, epigenomics (methylation/ChIP-seq/ATAC-seq), GWAS and polygenic scores, CRISPR mechanism and applications, bioinformatics pipelines, personalized medicine | `01-SEQUENCING-TECH.md` — the technology before the analysis | `biology/` (genetics foundations); Computing `data-science/` (bioinformatics pipelines are software engineering); `medicine/` (pharmacogenomics, cancer genomics); `immunology/` (immune repertoire sequencing) |
| `immunology/` | Innate immunity (pattern recognition, complement, innate cell types), adaptive immunity (clonal selection, MHC, antigen presentation), B cells and antibody classes (VDJ recombination, affinity maturation), T cell subsets (CD4/CD8, thymic selection, Tregs), cytokine networks (JAK-STAT/NF-κB), vaccine mechanisms (inactivated/subunit/mRNA/adjuvants), immunotherapy (checkpoint inhibitors/CAR-T), autoimmunity, immunodeficiency | `01-INNATE-IMMUNITY.md` — pattern recognition is the simpler starting point | `human-biology/` (immune system chapter); `disease/` (immune mechanisms underlie infectious disease, cancer, and autoimmunity); `medicine/` (immunotherapy and biologics); `genomics/` (HLA genetics, immune repertoire) |
| `microbiology/` | Bacterial cell biology and metabolism, viral structure and replication cycles (Baltimore classification), archaea and eukaryotic microbes, human microbiome (gut/skin/oral) and dysbiosis, microbial ecology (biofilms, quorum sensing, biogeochemical cycling), pathogen virulence mechanisms, antimicrobial resistance (mechanisms, HGT, One Health), microbial genetics (operons, CRISPR-Cas in bacteria), applied microbiology (industrial fermentation, synthetic biology) | `01-BACTERIAL-BIOLOGY.md` — bacterial cell structure before comparing domains | `disease/` (pathogen mechanisms); `ecology/` (microbial ecology and nutrient cycling); `genomics/` (metagenomics); Natural World `fermentation-spirits/` (yeast and bacterial fermentation) |
| `evolutionary-biology/` | Natural selection from first principles (mechanism and experimental evidence — Lenski's E. coli evolution experiment), population genetics (Hardy-Weinberg equilibrium, genetic drift and the Wright-Fisher model, effective population size), neutral theory and molecular evolution (Kimura's challenge to pan-selectionism), speciation mechanisms (allopatric, sympatric, ring species), phylogenetics and molecular clocks, evolutionary developmental biology (evo-devo: HOX genes, deep homology, constraint), sexual selection and life history theory, coevolution and Red Queen dynamics, macroevolution and the fossil record | `01-NATURAL-SELECTION.md` — mechanism before population genetics | `genomics/` (population genomics extends population genetics); `ecology/` (selection is always ecology-mediated); Earth & Space `paleontology/` (macroevolution and the fossil record) |
| `virology/` | Distinct from microbiology — focuses on what makes viruses uniquely virus-like: viral structure (capsid geometry, icosahedral vs. helical, enveloped vs. naked), Baltimore classification in full depth (6 classes, replication strategy for each), replication cycles (attachment through budding — what varies by virus family), virus-host interactions and tissue tropism, immune evasion strategies (antigenic drift/shift, latency, interferon antagonism), quasispecies theory (why RNA viruses evolve so fast — the quasi-species dynamics of high mutation rate), antiviral drug mechanisms and resistance, pandemic biology (spillover, R₀, serial interval, phylodynamics) | `01-VIRUS-STRUCTURE.md` — structure and Baltimore classification, the taxonomy before biology | `microbiology/` (viral elements in bacterial biology); `immunology/` (virus-immune interactions); `disease/` (viral disease mechanisms) |
| `biophysics/` | Physics applied to biological systems — the discipline that produced structural biology and electrophysiology: thermodynamics of biological systems (free energy, protein stability, binding affinity from ΔG), protein folding (energy landscape theory, Anfinsen's dogma, folding funnel, chaperones), structural methods (X-ray crystallography, NMR relaxation, cryo-EM revolution — from blurry to near-atomic resolution), membrane biophysics (lipid bilayer as a 2D fluid, membrane potential, Goldman equation), Hodgkin-Huxley model (the ionic basis of the action potential — the greatest model in neuroscience), molecular motors (kinesin, myosin — free energy transduction), single-molecule techniques (optical tweezers, AFM, FRET), AlphaFold and what deep learning revealed about the folding problem | `01-THERMODYNAMICS-BIO.md` — biological thermodynamics before structural methods | `physics/` (Math & Physics) for statistical mechanics; `neuroscience/` (Hodgkin-Huxley is the entry point to neurophysics); `genomics/` (protein structure prediction connects) |
| `pharmacology/` | The mechanistic science beneath medicine's drug catalog: receptor theory (Langmuir binding isotherm, affinity vs. efficacy, agonist/partial agonist/antagonist/inverse agonist, spare receptors), pharmacokinetics (ADME — absorption/distribution/metabolism/excretion, compartmental models, bioavailability, half-life), pharmacodynamics (dose-response, EC50/IC50, therapeutic index, Hill equation), CYP450 metabolism (which enzymes metabolize what, DDI prediction, phenotype variation), CNS pharmacology (GABA, glutamate, dopamine, serotonin systems), cardiovascular pharmacology, cancer pharmacology (cytotoxic through targeted through immunotherapy), drug development pipeline (IND through NDA, Phase I-III trial design), pharmacogenomics | `01-RECEPTOR-THEORY.md` — receptor binding before PK/PD | `medicine/` (drug classes in clinical context); `genomics/` (pharmacogenomics); `disease/` (drug targets map to disease mechanisms) |
| `developmental-biology/` | How a single cell becomes a complex organism — the toolkit of development: fertilization and cleavage (symmetry breaking, totipotency), gastrulation (germ layer formation — the most consequential 24 hours in vertebrate life), the conserved signaling toolkit (Wnt for cell fate and proliferation; Notch for lateral inhibition; Hedgehog for pattern formation — these three pathways underlie cancer too), HOX genes and axial patterning (why a fly mutation gives legs where antennae should be), organogenesis (inductive interactions, morphogenetic fields), neural development (neural tube, regionalization, axon guidance), stem cells (pluripotency factors, ground state vs. primed pluripotency), iPSCs (Yamanaka's 2006 Nobel-worthy discovery — dedifferentiation by four transcription factors), regeneration (planaria through salamander limb — why we can't) | `01-FERTILIZATION-CLEAVAGE.md` — fertilization and the earliest events before signaling | `genomics/` (developmental gene expression programs); `evolutionary-biology/` (evo-devo); `disease/` (developmental pathways are cancer pathways) |

---

## Paths

### The Full Stack — Molecule to Disease
`natural-sciences/` → `human-biology/` → `disease/` → `medicine/`
*Follow atoms through biochemistry into physiology, see how system failures produce disease, then map each disease to its drug class — the complete vertical from molecular mechanism to clinical intervention.*

### The Neural Path
`neuroscience/` → `cognitive-science/` → `psychology/`
*Neurons and circuits explain behavior at the biophysical level; cognitive science formalizes perception/memory/decision models; psychology gives you the behavioral and clinical outputs — the clean three-layer stack.*

### The Ecological Stack
`natural-sciences/` → `biology/` → `ecology/`
*Biochemistry and genetics underlie all biological organization; cell and systems biology scales up to whole organisms; ecology places populations and species into energy-flow networks — bottom-up from chemistry to biosphere.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Earth & Space | `ecology/` ↔ `geography/` and `climate-science/` — biome distribution is climate-driven; species range shifts, carbon cycling, and biodiversity loss are joint territory |
| Social Sciences | `cognitive-science/` → `psychology/` and `behavioral-economics/` — decision-making under uncertainty has both neural substrates and behavioral/economic models; `medicine/` → `public-health/` — individual pharmacology scales to population health policy |
| Computing & Software | `cognitive-science/` → `ai-engineering/` — transformer attention, memory, and reasoning architectures draw explicit inspiration from cognitive models; `neuroscience/` ↔ spiking neural net literature |
| History & Ideas | `disease/` and `medicine/` ↔ `history-of-science/` — germ theory, antibiotic discovery, and vaccine development are among the most consequential paradigm shifts in intellectual history |
