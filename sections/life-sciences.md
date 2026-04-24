# Life Sciences

18 directories · molecular chemistry through clinical medicine, with full coverage of the biological stack

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
| [`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) | Full chemistry and biochemistry stack — atomic structure through metabolism — plus cell biology, genetics, and plasma science | [`01-ATOMIC-QUANTUM.md`](../natural-sciences/01-ATOMIC-QUANTUM.md) for the physics-chemistry boundary; [`06-BIOMOLECULES.md`](../natural-sciences/06-BIOMOLECULES.md) to enter the biochem block | [`physics/`](../physics/01-ELECTROSTATICS.md) (quantum ↔ atomic), [`medicine/`](../medicine/00-OVERVIEW.md) (biochem mechanisms underlie drug targets), [`ecology/`](../ecology/00-OVERVIEW.md) (thermochem ↔ energy flow) |
| [`biology/`](../biology/00-OVERVIEW.md) | Cell structure and organelles, genetics (Mendelian through molecular), evolution, systems biology, synthetic biology | [`00-OVERVIEW.md`](../biology/00-OVERVIEW.md) — covers central dogma and field taxonomy | [`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) (shares cell-biology territory; read together), [`botany/`](../botany/00-OVERVIEW.md) and [`ecology/`](../ecology/00-OVERVIEW.md) (evolutionary biology framework) |
| [`botany/`](../botany/00-OVERVIEW.md) | Plant anatomy, photosynthesis (light/dark reactions, C3/C4/CAM), sexual and asexual reproduction, taxonomy, ethnobotany | [`01-PLANT-CELL-PHYSIOLOGY.md`](../botany/01-PLANT-CELL-PHYSIOLOGY.md) — structural foundation before biochemistry | [`ecology/`](../ecology/00-OVERVIEW.md) (primary productivity, food webs), [`agriculture/`](../agriculture/00-OVERVIEW.md) (crop science), [`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) (photosynthesis ↔ thermochem) |
| [`ecology/`](../ecology/00-OVERVIEW.md) | Ecosystems and energy flow, food webs and trophic structure, population dynamics (Lotka-Volterra), biome classification, conservation biology | [`01-POPULATION-DYNAMICS.md`](../ecology/01-POPULATION-DYNAMICS.md) — establishes the systems framing | [`geography/`](../geography/00-OVERVIEW.md) (biomes ↔ climate zones), [`climate-science/`](../climate-science/00-OVERVIEW.md) (carbon cycle feedbacks), [`botany/`](../botany/00-OVERVIEW.md) (primary production), [`paleontology/`](../paleontology/00-OVERVIEW.md) (mass extinctions) |
| [`human-biology/`](../human-biology/00-OVERVIEW.md) | All major body systems: musculoskeletal, cardiovascular, nervous, endocrine, immune, renal, reproductive — physiology-first | [`00-OVERVIEW.md`](../human-biology/00-OVERVIEW.md) — systems map before diving per-system | [`disease/`](../disease/00-OVERVIEW.md) (each system has failure modes), [`medicine/`](../medicine/00-OVERVIEW.md) (drug targets map to system physiology), [`neuroscience/`](../neuroscience/00-OVERVIEW.md) (nervous system depth) |
| [`neuroscience/`](../neuroscience/00-OVERVIEW.md) | Neuronal electrophysiology, synaptic transmission, circuit logic, systems-level cognition, neuroimaging methods (fMRI/EEG), synaptic plasticity and learning | [`01-NEURONS-SIGNALS.md`](../neuroscience/01-NEURONS-SIGNALS.md) — start at the cell before circuits | [`human-biology/`](../human-biology/00-OVERVIEW.md) (nervous system context), [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md) (circuits → behavior), [`disease/`](../disease/00-OVERVIEW.md) (neurological disorders), [`medicine/`](../medicine/00-OVERVIEW.md) (CNS drug targets) |
| [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md) | Perception, attention, working and long-term memory, language acquisition and processing, decision-making under uncertainty, consciousness theories, AI alignment connections | [`00-OVERVIEW.md`](../cognitive-science/00-OVERVIEW.md) — interdisciplinary map (neuroscience / psychology / linguistics / AI) | [`neuroscience/`](../neuroscience/00-OVERVIEW.md) (neural substrates of cognition), [`psychology/`](../psychology/00-OVERVIEW.md) (behavioral layer), [`ai-engineering/`](../ai-engineering/00-OVERVIEW.md) (cognitive architectures ↔ LLM design), [`philosophy/`](../philosophy/00-OVERVIEW.md) (mind, consciousness) |
| [`disease/`](../disease/00-OVERVIEW.md) | Infectious disease (bacterial, viral, fungal — mechanisms of pathogenicity), cancer biology (oncogenes, tumor microenvironment, immunoevasion), cardiovascular, metabolic, autoimmune, neurological, and genetic disorders | [`01-BACTERIAL.md`](../disease/01-BACTERIAL.md) — covers the broadest category first | [`medicine/`](../medicine/00-OVERVIEW.md) (disease mechanism → treatment class), [`human-biology/`](../human-biology/00-OVERVIEW.md) (normal physiology ↔ pathophysiology), [`public-health/`](../public-health/00-OVERVIEW.md) (epidemiology of disease burden) |
| [`medicine/`](../medicine/00-OVERVIEW.md) | Drug classes and mechanism of action: antibiotics (beta-lactams through fluoroquinolones), antivirals, cardiovascular agents, CNS drugs, endocrine pharmacology, cancer therapeutics, immunomodulators, diagnostics (imaging, lab, pathology) | [`01-ANTIBIOTICS.md`](../medicine/01-ANTIBIOTICS.md) — most mechanism variety, best entry for pharmacology logic | [`disease/`](../disease/00-OVERVIEW.md) (drug classes map to disease categories), [`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) (molecular targets), [`public-health/`](../public-health/00-OVERVIEW.md) (rational prescribing, AMR) |
| [`nutrition/`](../nutrition/00-OVERVIEW.md) | Macronutrient metabolism (carbs, lipids, protein), micronutrient biochemistry, major dietary patterns (Mediterranean, low-carb, plant-based) with evidence quality, gut microbiome composition and function, nutritional epidemiology and confounding | [`01-CARBOHYDRATES.md`](../nutrition/01-CARBOHYDRATES.md) — metabolic pathways before dietary patterns | [`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) (metabolism block), [`disease/`](../disease/00-OVERVIEW.md) (metabolic disease, cancer, cardiovascular risk), [`public-health/`](../public-health/00-OVERVIEW.md) (dietary policy), [`medicine/`](../medicine/00-OVERVIEW.md) (therapeutic nutrition) |
| [`genomics/`](../genomics/00-OVERVIEW.md) | Sequencing technology (Sanger → Illumina → nanopore → single-cell), genome assembly (de Bruijn graphs, telomere-to-telomere), variant calling (SNPs/indels/SVs, GATK pipeline), RNA-seq and differential expression, epigenomics (methylation/ChIP-seq/ATAC-seq), GWAS and polygenic scores, CRISPR mechanism and applications, bioinformatics pipelines, personalized medicine | [`01-SEQUENCING-TECH.md`](../genomics/01-SEQUENCING-TECH.md) — the technology before the analysis | [`biology/`](../biology/00-OVERVIEW.md) (genetics foundations); Computing [`data-science/`](../data-science/01-NUMPY.md) (bioinformatics pipelines are software engineering); [`medicine/`](../medicine/00-OVERVIEW.md) (pharmacogenomics, cancer genomics); [`immunology/`](../immunology/00-OVERVIEW.md) (immune repertoire sequencing) |
| [`immunology/`](../immunology/00-OVERVIEW.md) | Innate immunity (pattern recognition, complement, innate cell types), adaptive immunity (clonal selection, MHC, antigen presentation), B cells and antibody classes (VDJ recombination, affinity maturation), T cell subsets (CD4/CD8, thymic selection, Tregs), cytokine networks (JAK-STAT/NF-κB), vaccine mechanisms (inactivated/subunit/mRNA/adjuvants), immunotherapy (checkpoint inhibitors/CAR-T), autoimmunity, immunodeficiency | [`01-INNATE-IMMUNITY.md`](../immunology/01-INNATE-IMMUNITY.md) — pattern recognition is the simpler starting point | [`human-biology/`](../human-biology/00-OVERVIEW.md) (immune system chapter); [`disease/`](../disease/00-OVERVIEW.md) (immune mechanisms underlie infectious disease, cancer, and autoimmunity); [`medicine/`](../medicine/00-OVERVIEW.md) (immunotherapy and biologics); [`genomics/`](../genomics/00-OVERVIEW.md) (HLA genetics, immune repertoire) |
| [`microbiology/`](../microbiology/00-OVERVIEW.md) | Bacterial cell biology and metabolism, viral structure and replication cycles (Baltimore classification), archaea and eukaryotic microbes, human microbiome (gut/skin/oral) and dysbiosis, microbial ecology (biofilms, quorum sensing, biogeochemical cycling), pathogen virulence mechanisms, antimicrobial resistance (mechanisms, HGT, One Health), microbial genetics (operons, CRISPR-Cas in bacteria), applied microbiology (industrial fermentation, synthetic biology) | [`01-BACTERIAL-BIOLOGY.md`](../microbiology/01-BACTERIAL-BIOLOGY.md) — bacterial cell structure before comparing domains | [`disease/`](../disease/00-OVERVIEW.md) (pathogen mechanisms); [`ecology/`](../ecology/00-OVERVIEW.md) (microbial ecology and nutrient cycling); [`genomics/`](../genomics/00-OVERVIEW.md) (metagenomics); Natural World [`fermentation-spirits/`](../fermentation-spirits/00-OVERVIEW.md) (yeast and bacterial fermentation) |
| [`evolutionary-biology/`](../evolutionary-biology/00-OVERVIEW.md) | Natural selection from first principles (mechanism and experimental evidence — Lenski's E. coli evolution experiment), population genetics (Hardy-Weinberg equilibrium, genetic drift and the Wright-Fisher model, effective population size), neutral theory and molecular evolution (Kimura's challenge to pan-selectionism), speciation mechanisms (allopatric, sympatric, ring species), phylogenetics and molecular clocks, evolutionary developmental biology (evo-devo: HOX genes, deep homology, constraint), sexual selection and life history theory, coevolution and Red Queen dynamics, macroevolution and the fossil record | [`01-NATURAL-SELECTION.md`](../evolutionary-biology/01-NATURAL-SELECTION.md) — mechanism before population genetics | [`genomics/`](../genomics/00-OVERVIEW.md) (population genomics extends population genetics); [`ecology/`](../ecology/00-OVERVIEW.md) (selection is always ecology-mediated); Earth & Space [`paleontology/`](../paleontology/00-OVERVIEW.md) (macroevolution and the fossil record) |
| [`virology/`](../virology/00-OVERVIEW.md) | Distinct from microbiology — focuses on what makes viruses uniquely virus-like: viral structure (capsid geometry, icosahedral vs. helical, enveloped vs. naked), Baltimore classification in full depth (6 classes, replication strategy for each), replication cycles (attachment through budding — what varies by virus family), virus-host interactions and tissue tropism, immune evasion strategies (antigenic drift/shift, latency, interferon antagonism), quasispecies theory (why RNA viruses evolve so fast — the quasi-species dynamics of high mutation rate), antiviral drug mechanisms and resistance, pandemic biology (spillover, R₀, serial interval, phylodynamics) | [`01-VIRUS-STRUCTURE.md`](../virology/01-VIRUS-STRUCTURE.md) — structure and Baltimore classification, the taxonomy before biology | [`microbiology/`](../microbiology/00-OVERVIEW.md) (viral elements in bacterial biology); [`immunology/`](../immunology/00-OVERVIEW.md) (virus-immune interactions); [`disease/`](../disease/00-OVERVIEW.md) (viral disease mechanisms) |
| [`biophysics/`](../biophysics/00-OVERVIEW.md) | Physics applied to biological systems — the discipline that produced structural biology and electrophysiology: thermodynamics of biological systems (free energy, protein stability, binding affinity from ΔG), protein folding (energy landscape theory, Anfinsen's dogma, folding funnel, chaperones), structural methods (X-ray crystallography, NMR relaxation, cryo-EM revolution — from blurry to near-atomic resolution), membrane biophysics (lipid bilayer as a 2D fluid, membrane potential, Goldman equation), Hodgkin-Huxley model (the ionic basis of the action potential — the greatest model in neuroscience), molecular motors (kinesin, myosin — free energy transduction), single-molecule techniques (optical tweezers, AFM, FRET), AlphaFold and what deep learning revealed about the folding problem | [`01-THERMODYNAMICS-BIO.md`](../biophysics/01-THERMODYNAMICS-BIO.md) — biological thermodynamics before structural methods | [`physics/`](../physics/01-ELECTROSTATICS.md) (Math & Physics) for statistical mechanics; [`neuroscience/`](../neuroscience/00-OVERVIEW.md) (Hodgkin-Huxley is the entry point to neurophysics); [`genomics/`](../genomics/00-OVERVIEW.md) (protein structure prediction connects) |
| [`pharmacology/`](../pharmacology/00-OVERVIEW.md) | The mechanistic science beneath medicine's drug catalog: receptor theory (Langmuir binding isotherm, affinity vs. efficacy, agonist/partial agonist/antagonist/inverse agonist, spare receptors), pharmacokinetics (ADME — absorption/distribution/metabolism/excretion, compartmental models, bioavailability, half-life), pharmacodynamics (dose-response, EC50/IC50, therapeutic index, Hill equation), CYP450 metabolism (which enzymes metabolize what, DDI prediction, phenotype variation), CNS pharmacology (GABA, glutamate, dopamine, serotonin systems), cardiovascular pharmacology, cancer pharmacology (cytotoxic through targeted through immunotherapy), drug development pipeline (IND through NDA, Phase I-III trial design), pharmacogenomics | [`01-RECEPTOR-THEORY.md`](../pharmacology/01-RECEPTOR-THEORY.md) — receptor binding before PK/PD | [`medicine/`](../medicine/00-OVERVIEW.md) (drug classes in clinical context); [`genomics/`](../genomics/00-OVERVIEW.md) (pharmacogenomics); [`disease/`](../disease/00-OVERVIEW.md) (drug targets map to disease mechanisms) |
| [`developmental-biology/`](../developmental-biology/00-OVERVIEW.md) | How a single cell becomes a complex organism — the toolkit of development: fertilization and cleavage (symmetry breaking, totipotency), gastrulation (germ layer formation — the most consequential 24 hours in vertebrate life), the conserved signaling toolkit (Wnt for cell fate and proliferation; Notch for lateral inhibition; Hedgehog for pattern formation — these three pathways underlie cancer too), HOX genes and axial patterning (why a fly mutation gives legs where antennae should be), organogenesis (inductive interactions, morphogenetic fields), neural development (neural tube, regionalization, axon guidance), stem cells (pluripotency factors, ground state vs. primed pluripotency), iPSCs (Yamanaka's 2006 Nobel-worthy discovery — dedifferentiation by four transcription factors), regeneration (planaria through salamander limb — why we can't) | [`01-FERTILIZATION-CLEAVAGE.md`](../developmental-biology/01-FERTILIZATION-CLEAVAGE.md) — fertilization and the earliest events before signaling | [`genomics/`](../genomics/00-OVERVIEW.md) (developmental gene expression programs); [`evolutionary-biology/`](../evolutionary-biology/00-OVERVIEW.md) (evo-devo); [`disease/`](../disease/00-OVERVIEW.md) (developmental pathways are cancer pathways) |

---

## Paths

### The Full Stack — Molecule to Disease
[`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) → [`human-biology/`](../human-biology/00-OVERVIEW.md) → [`disease/`](../disease/00-OVERVIEW.md) → [`medicine/`](../medicine/00-OVERVIEW.md)
*Follow atoms through biochemistry into physiology, see how system failures produce disease, then map each disease to its drug class — the complete vertical from molecular mechanism to clinical intervention.*

### The Neural Path
[`neuroscience/`](../neuroscience/00-OVERVIEW.md) → [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md) → [`psychology/`](../psychology/00-OVERVIEW.md)
*Neurons and circuits explain behavior at the biophysical level; cognitive science formalizes perception/memory/decision models; psychology gives you the behavioral and clinical outputs — the clean three-layer stack.*

### The Ecological Stack
[`natural-sciences/`](../natural-sciences/00-OVERVIEW.md) → [`biology/`](../biology/00-OVERVIEW.md) → [`ecology/`](../ecology/00-OVERVIEW.md)
*Biochemistry and genetics underlie all biological organization; cell and systems biology scales up to whole organisms; ecology places populations and species into energy-flow networks — bottom-up from chemistry to biosphere.*

---

## Adjacent Sections

| Section | The bridge |
|---------|------------|
| Earth & Space | [`ecology/`](../ecology/00-OVERVIEW.md) ↔ [`geography/`](../geography/00-OVERVIEW.md) and [`climate-science/`](../climate-science/00-OVERVIEW.md) — biome distribution is climate-driven; species range shifts, carbon cycling, and biodiversity loss are joint territory |
| Social Sciences | [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md) → [`psychology/`](../psychology/00-OVERVIEW.md) and [`behavioral-economics/`](../behavioral-economics/00-OVERVIEW.md) — decision-making under uncertainty has both neural substrates and behavioral/economic models; [`medicine/`](../medicine/00-OVERVIEW.md) → [`public-health/`](../public-health/00-OVERVIEW.md) — individual pharmacology scales to population health policy |
| Computing & Software | [`cognitive-science/`](../cognitive-science/00-OVERVIEW.md) → [`ai-engineering/`](../ai-engineering/00-OVERVIEW.md) — transformer attention, memory, and reasoning architectures draw explicit inspiration from cognitive models; [`neuroscience/`](../neuroscience/00-OVERVIEW.md) ↔ spiking neural net literature |
| History & Ideas | [`disease/`](../disease/00-OVERVIEW.md) and [`medicine/`](../medicine/00-OVERVIEW.md) ↔ [`history-of-science/`](../history-of-science/00-OVERVIEW.md) — germ theory, antibiotic discovery, and vaccine development are among the most consequential paradigm shifts in intellectual history |
