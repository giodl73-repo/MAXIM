# Reference Library — Expansion Process

Repeatable process for selecting and executing content expansion batches.
Used every time a new batch of directories is added.

---

## 1. Selection Criteria

New directories are chosen against these filters — all three must be true:

| Filter | Test |
|--------|------|
| **Coverage gap** | Domain not covered (or only a stub) in any existing directory |
| **Thematic coherence** | Fits into an identifiable intellectual cluster (pure math, earth systems, media history, etc.) |
| **Learner relevance** | Useful to a VP-level technical leader or enriches a domain the learner cares about |

**Avoid**:
- Directories that would duplicate 80%+ of an existing module
- Hyper-narrow topics better served as a section inside an existing guide
- Topics where the learner has no adjacent background and no clear entry ramp

---

## 2. Grouping Principles

Each batch is organized into 4 parallel writing groups for agent parallelism:

```
Batch N
├── Group NA  (3 directories, ~10-12 files each, ~30-36 files total)
├── Group NB  (3 directories, ~10-12 files each, ~30-36 files total)
├── Group NC  (3 directories, ~10-12 files each, ~30-36 files total)
└── Group ND  (3 directories, ~10-12 files each, ~30-36 files total)
```

**Grouping rules**:
- Keep thematically related directories together (earth science dirs together, math dirs together, etc.)
- Balance file counts across groups (~30-36 files per group)
- Each group gets exactly one writing agent — avoid cross-group dependencies

**File count per directory**:
- Minimum 8, maximum 14
- `00-OVERVIEW.md` is always file 0 — the landscape / taxonomy guide
- Files numbered `01` through `N` covering distinct subtopics
- `STATUS.md` is the internal manifest (not a content file; doesn't count toward the file total)

---

## 3. Stub Creation Format

Each new directory requires:

### STATUS.md (internal manifest)

```markdown
# {DirectoryName}/ — Status

## Files

| File | Topic | Status |
|------|-------|--------|
| 00-OVERVIEW.md | Landscape, taxonomy, key concepts | 🔜 |
| 01-TOPIC.md    | First subtopic | 🔜 |
| ...            | ... | 🔜 |

## Coverage Notes

One-paragraph summary of what the directory covers and what makes it distinct.
Key connections to other directories in the library.
```

### Content stubs

Each content file gets a minimal 3-line stub:

```markdown
# {Topic Title}

> Stub — to be written.
```

This ensures the file exists in the scaffolded tree and will be found by any tool
scanning the directory, even before content is written.

---

## 4. Agent Prompt Template

Use this template when launching each writing agent. Customize the bracketed fields.

```
You are writing Group {NA} of Batch {N} of the reference library at C:\src\reference.

DIRECTORIES: {dir1}/ ({N1} files), {dir2}/ ({N2} files), {dir3}/ ({N3} files)

LEARNER PROFILE (from C:\src\reference\CLAUDE.md):
- VP of Software Engineering, Microsoft, age 52
- MIT double major: Mathematics + Theoretical Computer Science
- Deep background: .NET, Azure, VSTS, ADO.NET, ADF, Power Query
- ~10-year leadership gap (not hands-on coder)
- Peer-level technical writing — no handholding
- Bridges to Azure/.NET/VSTS where natural

STYLE CONTRACT (follow computing/01-PACKAGE.md format exactly):
1. Big Picture diagram first — full landscape in one ASCII diagram
2. Layer downward — each section drills into one component
3. ASCII boxes for system diagrams, flow charts, decision trees
4. Tables for comparisons and cheat sheets
5. "Old world → new world" bridges where the learner has prior art
6. End each file with Decision Cheat Sheet + Common Confusion Points sections

INSTRUCTIONS:
1. Read C:\src\reference\CLAUDE.md for full learner profile
2. Read each directory's STATUS.md for planned file list and coverage notes
3. Write every file listed in each STATUS.md — full content, not stubs
4. Follow the format of computing/01-PACKAGE.md exactly
5. When you finish all files in a directory, update that directory's STATUS.md
   — change all 🔜 to ✅, add a completion timestamp
6. Token budget: keep each file under ~32,000 tokens; split to Part 1 / Part 2 if needed

DOMAIN-SPECIFIC NOTES:
{Any domain bridges, depth notes, or special instructions for this group}
```

---

## 5. TRACKER.md Update Checklist

Before launching agents:
- [ ] Add rows to Summary Dashboard table (one per new directory, status 🔜)
- [ ] Add new batch section at bottom (list groups, directories, file counts)
- [ ] Commit the scaffolding (TRACKER.md + STATUS.md stubs + content stubs)

After agents complete:
- [ ] Verify each STATUS.md shows all files ✅
- [ ] Update Summary Dashboard: change 🔜 → ✅ for each completed directory
- [ ] Update file counts if any files were added during writing
- [ ] Update the top-level file count summary line

---

## 6. Completion Verification

Run these before the final commit:

```bash
# Count total files
find C:/src/reference -name "*.md" | wc -l

# Check for unfinished stubs
grep -r "^> Stub" C:/src/reference --include="*.md" -l

# Verify STATUS.md completions
grep -r "🔜" C:/src/reference --include="STATUS.md" -l
```

All three should return clean results before declaring a batch done.

**Section landing page update pass** — after completing a batch, scan which `sections/*.md` files need new directory entries. Each new directory gets one row added to its section's Directories table and wired into the mkdocs.yml nav. Sections: `computing-software`, `mathematics-physics`, `engineering`, `life-sciences`, `earth-space`, `history-ideas`, `social-sciences`, `language-communication`, `arts-culture`, `material-culture`, `natural-world`, `people`.

---

## 7. Commit Sequence

```bash
# Stage everything in the new directories
git add C:/src/reference/<dir1>/ C:/src/reference/<dir2>/ ...

# Stage TRACKER.md and EXPANSION.md
git add C:/src/reference/TRACKER.md C:/src/reference/EXPANSION.md

# Commit
git commit -m "Add Batch N: 12 new reference directories, NNN files"
```

Commit message format: `Add Batch {N}: {X} new reference directories, {Y} files`

---

## Batch History

| Batch | Groups | Directories | Files | Date |
|-------|--------|-------------|-------|------|
| 1 | A–E | medicine, law, philosophy, aeronautics, cryptography, spices, pigments, colors, statistics-applied, textiles, plumbing, coatings, climate-science, jewelry, ceramics, glassmaking, organizational-behavior, hvac, political-science, psychology, geography | ~189 | 2026-02 |
| 2 | 2A–2D | construction-materials, architecture-history, electrical-grid, culinary-history, food-plants, botany, fermentation-spirits, games-history, sports-history, cartography, typography, watchmaking | ~131 | 2026-02 |
| 3 | 3A–3D | signal-processing, acoustics, telecommunications, semiconductor-manufacturing, geology, meteorology, ecology, agriculture, art-history, economic-history, military-history, history-of-science, metalworking, photography, nutrition, sociology | ~181 | 2026-02 |
| 4 | 4A–4D | robotics, optics, biomedical-engineering, formal-methods, energy-systems, anthropology, religious-studies, architecture, game-theory, transportation, urban-planning, environmental-engineering | ~96 | 2026-02 |
| 5 | 5A–5D | oceanography, hydrology, paleontology, number-theory, abstract-algebra, topology, printing-publishing, cinema-film, radio-television, public-health, demography, behavioral-economics | ~129 | 2026-02 |
| 6 | 6A–6D | probability-statistics, differential-geometry, numerical-methods, genomics, immunology, microbiology, literature, theater-performance, rhetoric, mineralogy, archaeology, mycology | ~120 | 2026-02 |
| 7 | 7A–7D | complex-analysis, fluid-dynamics, statistical-mechanics, partial-differential-equations, variational-calculus, lie-groups, evolutionary-biology, virology, biophysics, dance, industrial-design, marine-biology | ~120 | — |
| 8 | 8A–8D | logic, intellectual-history, social-history, manufacturing, systems-engineering, materials-processing, criminology, media-studies, education, philosophy-of-language, semiotics, computer-architecture | ~120 | — |
| 9 | 9A–9D | entomology, ornithology, zoology, planetary-science, geochemistry, space-exploration, plastics-polymers, papermaking, composite-materials, graphic-design, fashion, comics-sequential-art | ~120 | — |
| 10 | 10A–10D | machine-learning-theory, pharmacology, developmental-biology, political-history, translation, international-relations, furniture, horticulture, sports-science, astrobiology, philosophy-of-mind, ethics | ~120 | — |
| 11 | 11A–11D | mathematicians-logicians, physicists-astronomers, chemists-naturalists, engineers-inventors, computing-pioneers, explorers, philosophers-thinkers, artists-architects, writers-poets, political-reformers, social-reformers, visionaries | ~132 | — |
| 12 | 12A–12F | dendrology, freshwater-biology, soil-science, coral-reefs, woodworking, leatherworking, masonry, rope-cordage, journalism, oral-tradition, epigraphy, digital-media, distributed-systems, security-engineering, cloud-architecture, nanotechnology, energy-storage, infrastructure-systems | ~198 | — |
| 13 | 13A–13C | remote-sensing, dyeing-fiber, historiography, philosophy-of-science, geotechnical-engineering, development-studies, programming-language-theory | ~77 | — |

---

## Batch 7 — Mathematical Foundations + Science Cores + Arts Gaps

Target sections: Mathematics & Physics (7A–7B), Life Sciences (7C), Arts & Culture / Natural World (7D)

| Group | Directories | Files | Section |
|-------|-------------|-------|---------|
| 7A | `complex-analysis/` · `fluid-dynamics/` · `statistical-mechanics/` | 30 | Mathematics & Physics |
| 7B | `partial-differential-equations/` · `variational-calculus/` · `lie-groups/` | 30 | Mathematics & Physics |
| 7C | `evolutionary-biology/` · `virology/` · `biophysics/` | 30 | Life Sciences |
| 7D | `dance/` · `industrial-design/` · `marine-biology/` | 30 | Arts & Culture / Natural World |

**Domain notes per group:**

7A — Bridge to physics/ (statistical-mechanics ↔ thermodynamics, fluid-dynamics ↔ Navier-Stokes as unsolved problem), mathematics/ (complex-analysis ↔ topology, Riemann surfaces). MIT TCS: complex-analysis underlies spectral theory; fluid-dynamics connects to algorithms via CFD discretization.

7B — PDEs are the language of physics; variational-calculus underlies Lagrangian mechanics AND modern ML (gradient descent as variational problem); Lie groups are the algebraic structure behind gauge theory, the standard model, and representation theory (MIT math background assumed — go deep).

7C — evolutionary-biology/ should treat population genetics mathematically (Hardy-Weinberg, drift, Wright-Fisher model) and connect to genomics/. virology/ distinct from microbiology/: focus on replication cycles, Baltimore classification in full depth, quasispecies theory. biophysics/: cryo-EM revolution, protein folding (AlphaFold context), Hodgkin-Huxley as physical model.

7D — dance/: treat as a formal system (Laban notation, phrase structure) as well as cultural history. industrial-design/: Bauhaus through Braun (Rams) through Ive — design as engineering constraint satisfaction. marine-biology/: 71% of Earth's surface; chemosynthesis, bioluminescence, deep sea as alien biosphere.

---

## Batch 8 — Intellectual History + Engineering Depth + Social Sciences

Target sections: History & Ideas (8A), Engineering (8B), Social Sciences (8C), Language & Communication / Computing (8D)

| Group | Directories | Files | Section |
|-------|-------------|-------|---------|
| 8A | `logic/` · `intellectual-history/` · `social-history/` | 30 | History & Ideas |
| 8B | `manufacturing/` · `systems-engineering/` · `materials-processing/` | 30 | Engineering |
| 8C | `criminology/` · `media-studies/` · `education/` | 30 | Social Sciences |
| 8D | `philosophy-of-language/` · `semiotics/` · `computer-architecture/` | 30 | Language & Comm / Computing |

**Domain notes per group:**

8A — logic/: treat as companion to computing/21-AUTOMATA.md and computing/23-PL-THEORY.md — Gödel incompleteness bridges to Turing undecidability and Rice's theorem (MIT TCS). Modal logic → temporal logic → model checking. intellectual-history/: history of ideas as sociology of knowledge (Kuhn, Mannheim) — how do paradigms shift? social-history/: Annales school methodology, Braudel's longue durée, quantitative history.

8B — manufacturing/: GD&T (ASME Y14.5), tolerancing, CNC, additive manufacturing (FDM/SLA/DMLS), lean/TPS. Bridge to computing: Industry 4.0 as cyber-physical systems. systems-engineering/: V-model, SysML, FMEA — VP-critical; large system design as engineering discipline. materials-processing/: TTT diagrams, heat treatment, fracture mechanics — the bridge between materials/ and manufacturing/.

8C — criminology/: white-collar crime (Sutherland), rational choice, mass incarceration as policy choice. media-studies/: McLuhan's tetrad, Frankfurt School, Baudrillard simulacra, platform capitalism (attention economy). education/: spacing effect, retrieval practice, Piaget/Vygotsky, MOOC completion crisis.

8D — philosophy-of-language/: Frege's sense/reference → Russell's descriptions → Wittgenstein (TLP then PI) → speech acts (Austin/Searle) → possible worlds semantics (Kripke). Bridge to computing: formal semantics ↔ type theory (Curry-Howard correspondence). semiotics/: Saussure vs. Peirce, structuralism, post-structuralism. computer-architecture/: ISA/microarchitecture split (x86/ARM/RISC-V), pipelining, cache coherence, GPU SIMT model.

---

## Batch 9 — Natural World Depth + Material Culture + Arts Completion

Target sections: Natural World (9A), Earth & Space (9B), Material Culture (9C), Arts & Culture (9D)

| Group | Directories | Files | Section |
|-------|-------------|-------|---------|
| 9A | `entomology/` · `ornithology/` · `zoology/` | 30 | Natural World |
| 9B | `planetary-science/` · `geochemistry/` · `space-exploration/` | 30 | Earth & Space |
| 9C | `plastics-polymers/` · `papermaking/` · `composite-materials/` | 30 | Material Culture |
| 9D | `graphic-design/` · `fashion/` · `comics-sequential-art/` | 30 | Arts & Culture |

**Domain notes per group:**

9A — entomology/: insects as 80% of animal species; eusociality as an evolutionary puzzle (Hamilton's rule); pollinator collapse economics. ornithology/: avian evolution from theropod dinosaurs — the K-Pg boundary as context; migration navigation (magnetic compass, stellar). zoology/: comparative physiology framework; ethology (Tinbergen's four questions); Conway Morris vs. Gould on convergence.

9B — planetary-science/: Nice model for solar system formation; comparative planetology (Venus as cautionary tale); exoplanet demographics from Kepler. geochemistry/: U-Pb geochronology, stable isotope paleoproxies (δ¹⁸O for temperature), carbon isotope excursions (Permian extinction). space-exploration/: Tsiolkovsky equation, specific impulse, staging — the physics of getting to orbit; SpaceX reusability revolution.

9C — plastics-polymers/: polymer chemistry (Tg, crystallinity, Mw/Mn), major thermoplastics/thermosets, injection molding, environmental impact (microplastics), bioplastic promises vs. reality. papermaking/: Cai Lun → Fourdrinier (1803) → Kraft process; archival paper (acid-free, cotton rag) for this library's own context. composite-materials/: CLT (classical laminate theory), prepreg/autoclave, Boeing 787 case study, end-of-life problem.

9D — graphic-design/: Bauhaus → Swiss Style (Müller-Brockmann) → American Modernism (Rand, Bass) → digital. fashion/: couture system, fast fashion economics (Zara model), Rana Plaza as inflection point. comics-sequential-art/: McCloud's closure theory, panel transitions, Maus as literary turning point, manga as global phenomenon.

---

## Batch 10 — Deep Specialization + Final Gaps

Target sections: Computing / Life Sciences (10A), History & Ideas / Language (10B), Material / Natural / Arts (10C), Earth & Space / History & Ideas (10D)

| Group | Directories | Files | Section |
|-------|-------------|-------|---------|
| 10A | `machine-learning-theory/` · `pharmacology/` · `developmental-biology/` | 30 | Computing / Life Sciences |
| 10B | `political-history/` · `translation/` · `international-relations/` | 30 | History & Ideas / Language |
| 10C | `furniture/` · `horticulture/` · `sports-science/` | 30 | Material / Natural / Arts |
| 10D | `astrobiology/` · `philosophy-of-mind/` · `ethics/` | 30 | Earth & Space / History & Ideas |

**Domain notes per group:**

10A — machine-learning-theory/: PAC learning (Valiant), VC dimension, Rademacher complexity, neural tangent kernel, double descent — the theoretical foundations below the engineering of ai-engineering/. pharmacology/: PK/PD, ADME, CYP metabolism, receptor theory — deeper than medicine/'s drug-class overview. developmental-biology/: Wnt/Notch/Hedgehog signaling toolkit, HOX genes, iPSCs (Yamanaka 2006), regeneration.

10B — political-history/: revolution (Skocpol's structural theory), imperialism, decolonization (1947/1960s), Cold War historiography, contemporary democratic backsliding. translation/: equivalence problem, Bible translation history (Vulgate/Luther/KJV), Nabokov's literalism, neural MT (BLEU score). international-relations/: Waltz vs. Mearsheimer vs. Wendt, nuclear deterrence (MAD/credibility), power transition theory.

10C — furniture/: joinery as applied geometry, Bauhaus tubular steel (Breuer), Eames as engineering, IKEA KD model. horticulture/: plant propagation (grafting, tissue culture), soil science, IPM, controlled environment agriculture. sports-science/: VO₂max, lactate threshold, periodization, sports psychology (flow state), doping biochemistry.

10D — astrobiology/: origin of life (RNA world, hydrothermal vents), extremophile envelope, Fermi paradox responses, biosignature detection (JWST context). philosophy-of-mind/: Chalmers' hard problem, Chinese Room (Searle), functionalism, free will and determinism, AI consciousness implications. ethics/: consequentialism/deontology/virtue ethics foundations, Rawls, applied AI ethics, research ethics (Nuremberg/Helsinki).

---

## Batch 11 — People

Target section: People (new 12th section, all four groups)

| Group | Directories | Files | Section |
|-------|-------------|-------|---------|
| 11A | `mathematicians-logicians/` · `physicists-astronomers/` · `chemists-naturalists/` | 33 | People |
| 11B | `engineers-inventors/` · `computing-pioneers/` · `explorers/` | 33 | People |
| 11C | `philosophers-thinkers/` · `artists-architects/` · `writers-poets/` | 33 | People |
| 11D | `political-reformers/` · `social-reformers/` · `visionaries/` | 33 | People |

**Domain notes per group:**

11A — mathematicians-logicians/: MIT TCS background means engage with the actual mathematics — Gödel's incompleteness theorems in full, Turing's reduction, Grothendieck's abstract algebra revolution. Biographical narrative does not require avoiding precision. physicists-astronomers/: follow the conceptual breaks — Galilean vs. Newtonian, classical vs. quantum, Einsteinian vs. standard model. chemists-naturalists/: bridge to genomics/ (DNA as culmination of naturalist tradition), and to materials/ (Pauling's valence bond theory).

11B — engineers-inventors/: Engineering history is the history of constraint satisfaction — what was physically possible at each era. Bridge to the Engineering section directories throughout. computing-pioneers/: the personal dimension of computing/ — Turing's biography illuminates why the Church-Turing thesis matters. Bridge to languages/ (language designers), cryptography/ (Turing's Bletchley work), ai-engineering/ (AI founders). explorers/: geographic exploration as knowledge-making — cartography/, historical-geography/, oceanography/ connections.

11C — philosophers-thinkers/: connect to philosophy/ for the ideas, but focus here on the person and context — why did Wittgenstein abandon the Tractatus? What was the Vienna Circle's social context? Bridge to logic/ (formal logic history) and philosophy-of-mind/ (Chalmers, Dennett). artists-architects/: connect to art-history/ and architecture-history/ throughout. Do not just name-drop — explain what each artist's formal innovation was. writers-poets/: connect to literature/ for genre/period analysis. Focus on the writer's relationship to their language and tradition.

11D — political-reformers/: avoid hagiography — assess consequences, not just intentions. Lincoln preserved the Union; Gandhi's methods worked in specific colonial context; assess each. social-reformers/: bridge to public-health/, education/, sociology/. The Nightingale entry should engage with her statistical innovations (she invented the polar area chart). visionaries/: the Vannevar Bush entry ("As We May Think," 1945) is the direct ancestor of hypertext and the web — bridge to computing/ and internet/web. Engelbart's demo (1968) was the first computer mouse, windows, hypertext, video conferencing — frame against computing-pioneers/.

---

## Batch 12 — Completing the Five ♠ (Frontier) Volumes

Target sections: Natural World NW·IV (12A–12B), Material Culture MC·IV (12B–12C), Language & Communication LC·IV (12C–12D), Computing C·IV (12E), Technology T·IV (12F)

| Group | Directories | Files | Section / Card |
|-------|-------------|-------|----------------|
| 12A | `dendrology/` · `freshwater-biology/` · `soil-science/` | 33 | Natural World ♠ (2♠) |
| 12B | `coral-reefs/` · `woodworking/` · `leatherworking/` | 33 | NW·IV + MC·IV (2♠/4♠) |
| 12C | `masonry/` · `rope-cordage/` · `journalism/` | 33 | MC·IV + LC·IV (4♠/10♠) |
| 12D | `oral-tradition/` · `epigraphy/` · `digital-media/` | 33 | Language & Comm ♠ (10♠) |
| 12E | `distributed-systems/` · `security-engineering/` · `cloud-architecture/` | 33 | Computing ♠ (K♠) |
| 12F | `nanotechnology/` · `energy-storage/` · `infrastructure-systems/` | 33 | Technology ♠ (8♠) |

**Domain notes per group:**

12A — dendrology/: tree rings as climate archive — bridge to climate-science/ and geology/; wood anatomy bridges to construction-materials/ and manufacturing/. freshwater-biology/: limnology as the freshwater parallel to oceanography/ — thermoclines, trophic cascades, eutrophication as a policy problem. soil-science/: CLORPT factors and horizon formation; soil microbiology (mycorrhizae, nitrogen fixation) bridges to ecology/ and agriculture/.

12B — coral-reefs/: zooxanthellae symbiosis and bleaching as the climate-change canary; carbonate chemistry bridges to oceanography/ and geochemistry/. woodworking/: grain direction, seasonal movement, and wood species selection — bridges to dendrology/ (wood anatomy) and construction-materials/ (structural timber). leatherworking/: vegetable vs. chrome tanning as industrial chemistry — bridges to textiles/ and dyeing-fiber/.

12C — masonry/: thrust line analysis for arches — bridges to structural/ (load paths) and construction-materials/; historic masonry bridges to archaeology/. rope-cordage/: fiber selection and twist geometry; Inca quipu as information storage (bridge to codes/ and oral-tradition/). journalism/: press freedom as political science topic (bridge to political-science/); data journalism bridges to statistics-applied/ and digital-media/.

12D — oral-tradition/: Parry-Lord oral-formulaic theory — the structural linguistics of pre-literate composition; bridge to linguistics/ and literature/. epigraphy/: decipherment methods (statistical analysis of symbol frequency, bilingual texts) — bridge to codes/ and world-languages/; Maya glyph decipherment as a solved problem. digital-media/: attention economy connects to behavioral-economics/; platform architecture connects to computing/ and distributed-systems/.

12E — distributed-systems/: VP bridge — VSTS was a distributed system; Azure DevOps is a distributed system; the CAP theorem explains every design choice you made. Paxos and Raft are the consensus algorithms behind every distributed database. Bridge to cloud-architecture/ (patterns built on top) and security-engineering/ (distributed threat surface). security-engineering/: SDL at Microsoft as the reference — this is what the learner built. STRIDE threat modeling, secure SDLC, and DevSecOps bridge directly to computing/ and formal-methods/. cloud-architecture/: Azure-first framing; FinOps and cost optimization are VP-relevant; Kubernetes architecture bridges to os/ (scheduling) and distributed-systems/ (consensus).

12F — nanotechnology/: quantum confinement effects — bridge to physics/ (quantum mechanics) and semiconductor-manufacturing/ (nanofab tools overlap). energy-storage/: Li-ion electrochemistry in depth — bridge to natural-sciences/ (electrochemistry) and electrical-grid/ (grid balancing); LCOS learning curves bridge to economics/. infrastructure-systems/: Rinaldi interdependency model — cascading failure as the central concept; bridge to systems-engineering/ (complex systems) and urban-planning/ (critical urban infrastructure).

---

## Batch 13 — Filling Seven Thin Cards

Target sections: Earth & Space (13A), Material Culture (13A), History & Ideas (13A–13B), Technology (13B), Social Sciences (13C), Computing (13C)

| Group | Directories | Files | Card |
|-------|-------------|-------|------|
| 13A | `remote-sensing/` · `dyeing-fiber/` · `historiography/` | 33 | 3♠ · 4♣ · 6♥ |
| 13B | `philosophy-of-science/` · `geotechnical-engineering/` | 22 | 6♠ · 8♥ |
| 13C | `development-studies/` · `programming-language-theory/` | 22 | 9♠ · K♥ |

**Domain notes per group:**

13A — remote-sensing/: InSAR as the bridge between physics (wave interference) and earth science (ground deformation measurement); connects astronomy/ (satellite platforms) and geology/ (deformation). dyeing-fiber/: Perkin's accidental synthesis of mauveine (1856) as the founding moment of industrial organic chemistry — bridge to pigments/ and natural-sciences/ (organic chemistry); spinning connects to textiles/. historiography/: the Annales school and longue durée as the intellectual framework for how to read this entire library; bridge to intellectual-history/ and philosophy-of-science/ (epistemology of historical knowledge).

13B — philosophy-of-science/: Kuhn's paradigm structure is the meta-framework for understanding how every section in this library changed over time — reading this unlocks the intellectual-history/ entries. Lakatos research programs explain why scientific fields don't simply switch on falsification. Bridge to logic/, history-of-science/, and intellectual-history/. geotechnical-engineering/: Terzaghi's effective stress principle is one of the most elegant physical insights in engineering — bridge to structural/ (foundation loads) and soil-science/ (soil mechanics overlap).

13C — development-studies/: the Sen capabilities approach (from economics/ and public-health/) applied to international development; Acemoglu/Robinson institutions framework bridges to political-science/ and international-relations/. programming-language-theory/: the Curry-Howard correspondence (proofs as programs) is the bridge between the MIT TCS background (type theory, logic) and modern programming languages — this should feel like completing a circuit for this learner. Bridge to formal-methods/ (proof assistants), languages/ (applied type systems), and cryptography/ (type-theoretic verification).
