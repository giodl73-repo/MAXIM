# Life Sciences

10 directories · molecular chemistry through clinical medicine, with full coverage of the biological stack

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
