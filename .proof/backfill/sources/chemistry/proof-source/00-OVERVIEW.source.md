---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:overview
kind: guide
module: chemistry
section: chemistry
title: Chemistry - Discipline Map and Module Boundaries
status: source-custody
source_custody: partial
current_path: chemistry/00-OVERVIEW.md
canonical_path: chemistry/00-OVERVIEW.md
backsource_ids: [proof-backfill:chemistry:00-overview, git-history:chemistry:00-overview]
concepts: [chemistry, analytical, inorganic, organic, physical, computational]
root_concepts: [chemistry]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Chemistry — Discipline Map and Module Boundaries

Chemistry is the science of matter at the scale where **electrons decide
outcomes**: what bonds form, how fast, in which geometry, and how you prove it
happened. This module is the upper-undergraduate-to-graduate reference for
chemistry *as a discipline* — the part that sits above general chemistry
(`natural-sciences/01-05, 17`) and below the applied domains that consume it
(`materials/`, `chemical-eng/`, `pharmacology/`, `biochemistry/`).

```
CHEMISTRY AS A DISCIPLINE (ACS "ABIOP" core)
==========================================================================
  SUBSTANCE                 TRANSFORMATION            EVIDENCE
  what exists               how it changes            how you know

  [ INORGANIC (01) ]        [ ORGANIC SYNTH (03) ]    [ ANALYTICAL/STRUCTURE ]
   coordination,             retrosynthesis,           quantitation (04)
   organometallic,           named reactions,          separations  (05)
   bioinorganic              pericyclic, green         NMR (06), optical+MS (07)
        |                         |                    crystallography (08)
        v                         v                         |
  [ ACID-BASE + SOLUTION EQUILIBRIA (02) ]                  |
   Bronsted/Lewis, HSAB, buffers, Ksp, EDTA                 |
        |                                                   |
        v                                                   v
  [ PHYSICAL CHEMISTRY DEPTH (09) ]  ->  explains WHY all the above
   stat thermo, activity/non-ideality, surfaces + catalysis
        |
        |----->  [ COMPUTATIONAL (10) ]  QM ladder, DFT, MD, QM/MM, cheminf.
        |----->  [ MEASUREMENT + SAFETY (11) ]  uncertainty, GLP, GHS/SDS, waste
==========================================================================
  Read left-to-right as a lab thinks: make a substance, transform it, then
  prove what you made. Physical chemistry is the theory floor under all of it.
```

The ACS certified-degree core is five areas — **A**nalytical, **B**iochemistry,
**I**norganic, **O**rganic, **P**hysical (ABIOP). MAXIM already owns the **B** in
depth (`biochemistry/`), so this module is *ABIOP minus B*, plus the two tracks
every modern curriculum treats as required: **computational chemistry** and
**laboratory measurement/safety**. That is six intellectual clusters mapped onto
twelve guides.

---

## The Layers Below and Above This Module

A software reader should hold chemistry as a **stack with a strict "owns"
contract**, exactly like a service catalog: each layer exposes an interface and
does not reimplement the layer below it.

```
        APPLICATION DOMAINS (consume chemistry, own their own scale-up)
        materials/  chemical-eng/  pharmacology/  geochemistry/  plastics-polymers/
        biochemistry/ (life's chemistry)   nutrition/   disease/
                        ^
                        |  chemistry/ hands them mechanism + method
        ============================================================
          chemistry/  (THIS MODULE)  discipline-level chemistry
          coordination · synthesis · analysis · structure · pchem depth
        ============================================================
                        ^
                        |  builds on general-chemistry primitives
        GENERAL CHEMISTRY FLOOR  (natural-sciences/)
        01 atomic/quantum  02 bonding  03 thermochem  04 kinetics
        05 electrochem     17 intro organic
                        ^
                        |
        PHYSICS + MATH   physics/ (QM, stat mech)   mathematics/   materials/ (solids)
```

**The rule this module follows everywhere:** if `natural-sciences/` already
derived it (atomic orbitals, VSEPR, the four laws, Arrhenius, Nernst, SN1/SN2),
this module *cross-references and builds up* — it does not re-derive. Treat the
general-chemistry floor as a floor, not a ceiling.

---

## What Each Guide Owns (and Where NOT to Look Here)

| # | Guide | Uniquely owns | Explicitly defers to |
|---|-------|---------------|----------------------|
| 01 | Inorganic | CFT/LFT, CFSE, Jahn-Teller, 18e rule, organometallics, Pd catalysis, bioinorganic | element trends → `periodic-table/`; band theory → `materials/02` |
| 02 | Acid-Base/Solution | HSAB, polyprotic, buffer capacity, Ksp, EDTA conditional constants, superacids | ΔG/K basics → `natural-sciences/03` |
| 03 | Organic Synthesis | retrosynthesis, named reactions, pericyclic/FMO, protecting groups, asymmetric, green metrics | SN1/SN2/E1/E2, stereo basics → `natural-sciences/17` |
| 04 | Analytical/Quantitative | gravimetry, titrimetry, voltammetry, calibration, ICH validation | cell EMF/Nernst → `natural-sciences/05` |
| 05 | Separation Science | van Deemter, GC, HPLC, TLC, CE, SPE, hyphenated MS | distillation/process → `chemical-eng/04` |
| 06 | NMR | ¹H/¹³C, DEPT, COSY/HSQC/HMBC/NOESY, small-molecule elucidation | protein NMR → `biophysics/03` |
| 07 | Optical + MS | IR/UV-Vis interpretation, photochemistry, MS fragmentation, combined elucidation | Beer-Lambert physics, IR/Raman rules → `optics/07` |
| 08 | Crystallography | space groups/absences, SHELX, Flack, CSD, powder XRD/Rietveld | protein XRD/PDB → `biophysics/03`; lattices → `materials/01` |
| 09 | Physical Chemistry Depth | partition functions → thermochem, Debye-Hückel/activity, adsorption, surface kinetics | Ising/phase transitions → `statistical-mechanics/` |
| 10 | Computational | molecular QM ladder, DFT functionals, MD for solutions, QM/MM, cheminformatics | periodic DFT for solids → `materials/09` |
| 11 | Measurement + Safety | GUM uncertainty, GLP, GHS/SDS, reactive handling, waste | — (module-unique) |

Every guide opens with an ownership box so navigation errors are cheap to catch.
When two MAXIM guides touch the same technique, the split is by **problem**, not
by technique: `chemistry/06` does NMR for a 300-Da unknown; `biophysics/03` does
NMR for a 300-residue protein — same physics, different question.

---

## Bridge: Software Mental Models → Chemistry

These are load-bearing analogies for a reader with deep CS but light chemistry.

| Software / systems concept | Chemistry analog |
|---|---|
| Type system / schema | Bonding + valence: what combinations are even legal |
| Compiler optimization passes | Retrosynthetic analysis: rewrite target → simpler precursors |
| Static vs. dynamic dispatch | Thermodynamic control (most stable product) vs. kinetic control (fastest to form) |
| Rate limiter / critical path | Rate-determining step; turnover-limiting step in catalysis |
| Unit/integration test | Titration, NMR, MS, XRD — orthogonal assays that must agree |
| Numerical precision / error bars | Measurement uncertainty (GUM), LOD/LOQ, significant figures |
| Approximation ladder (O(1)→O(n³)) | QM method ladder (MM → DFT → MP2 → CCSD(T)); accuracy costs compute |
| Canonical serialization (JSON) | SMILES / InChI: canonical text encoding of a molecular graph |
| Determinism vs. stochastic sim | Static structure (XRD) vs. ensemble sampling (molecular dynamics) |
| Reference implementation | The Cambridge Structural Database / spectral libraries as ground truth |

The single most useful bridge: **a molecule is a typed graph, and a reaction is a
graph rewrite that must conserve atoms and obey an energy budget (ΔG).** Every
later guide is either about legal rewrites (01-03), reading the graph back out of
a sample (04-08), or predicting the energy budget (09-10).

---

## Reading Order by Background

```
LAB SCIENTIST / EXPERIMENTALIST     THEORY / PHYSICS BACKGROUND
  00 -> 04 -> 05 -> 06/07 -> 08       00 -> 09 -> 10 -> 01 -> 02
  (measure first, theory as needed)   (build the theory floor, then apply)

CS / DATA BACKGROUND                 CANONICAL LINEAR PATH
  00 -> 10 -> 06/07 -> 03             00 -> 01 -> 02 -> 03 -> 04 -> 05
  (cheminformatics + spectra as data)  -> 06 -> 07 -> 08 -> 09 -> 10 -> 11
```

Hard prerequisite edges inside the module: read **02 before 04** (titrimetry is
applied acid-base/complex equilibria); skim **09** before **10** if partition
functions and activity are unfamiliar; **06, 07, 08** are mutually reinforcing —
real structure elucidation fuses NMR + MS + IR + XRD, so 07's combined-elucidation
section assumes 06.

---

## Reader Tasks (answerable from this guide)

1. **"I want to understand how a drug candidate gets designed and made — where do
   I start?"** → `03-ORGANIC-SYNTHESIS` for the retrosynthesis + reaction toolkit;
   `10-COMPUTATIONAL` for QSAR/docking; `pharmacology/` for what happens once it's
   in a body. Chemistry owns the *making*; pharmacology owns the *effect*.
2. **"Where does chemistry end and materials science begin?"** → At the
   molecule/solid boundary. Discrete molecules and coordination complexes: here
   (`01`, `10`). Extended solids, band structure, and periodic DFT: `materials/`.
   Small-molecule crystals: `08`; the same crystal *as an engineering material*:
   `materials/01`.
3. **"Which existing MAXIM module do I read before this one?"** →
   `natural-sciences/01-05` and `17` are the assumed floor. If those are shaky,
   read them first; this module deliberately does not repeat them.
4. **"An unknown organic compound is on my bench — what's the identification
   workflow?"** → `07` (MS for formula + IR for functional groups) fused with
   `06` (NMR for connectivity), confirmed by `08` (XRD) if a crystal grows. Guide
   07's combined-elucidation section is the orchestration layer.
5. **"Is 'chemistry' redundant with `biochemistry/`?"** → No. Biochemistry owns
   metabolism, enzymes, and biomolecules. This module's only bridge back is
   *bioinorganic* chemistry (`01`) — metalloenzyme active sites as coordination
   complexes.

---

## Decision Cheat Sheet

| I need to... | Go to |
|---|---|
| Predict a transition-metal complex's color/magnetism | `01` (CFT: Δ_oct, high/low spin) |
| Choose a buffer and predict its capacity | `02` (Henderson-Hasselbalch, β) |
| Plan a multistep synthesis of a target | `03` (retrosynthesis + named reactions) |
| Quantify an analyte with known uncertainty | `04` (calibration, standard addition) + `11` (GUM) |
| Pick GC vs. HPLC vs. CE for a mixture | `05` (van Deemter + selectivity table) |
| Elucidate an organic structure from spectra | `06` + `07` (NMR + MS + IR fusion) |
| Determine an absolute configuration in the solid | `08` (Flack parameter) |
| Get activity coefficients for an ionic solution | `09` (Debye-Hückel/Davies) |
| Choose a QM method for a target accuracy | `10` (method-vs-cost table) |
| Handle a pyrophoric or peroxide-forming reagent safely | `11` (reactive-class reference) |

---

## Common Confusion Points

**"Isn't this just `natural-sciences/` again?"** No. `natural-sciences/` is the
general-chemistry survey (one year of gen chem + one semester organic). This
module is the *major-level* discipline: it assumes that survey and picks up at
coordination chemistry, synthesis design, instrumental analysis, and statistical
thermodynamics — none of which the survey covers.

**"Physical chemistry appears in three places."** Deliberately.
`natural-sciences/03-04` own intro thermo/kinetics; `statistical-mechanics/`
(Math & Physics) owns condensed-matter stat mech (Ising, RG, phase transitions);
`chemistry/09` owns molecular partition functions → thermochemistry and
solution/surface chemistry. Same formalism, three different problem classes.

**"Analytical chemistry is scattered across 04-08."** It is one subdiscipline
split by *technique family*: quantitation (04), separation (05), and three
structure-determination families (06 NMR, 07 optical/MS, 08 diffraction). A real
analytical problem usually touches several.

**"Where's electrochemistry / thermodynamics / kinetics?"** The foundations live
in `natural-sciences/03-05`. This module adds only the discipline-level
extensions: voltammetry for analysis (04), activity/non-ideality and surface
kinetics (09). It does not restate the Nernst equation or the rate-law taxonomy.

**"Computational chemistry vs. `materials/09` vs. `ai-engineering/`."** Three
different computational cultures. `chemistry/10` = molecular electronic structure
(Gaussian-basis QM, thermochemistry, cheminformatics). `materials/09` = periodic
solids (plane waves, k-points, band structure). ML-for-chemistry (interatomic
potentials, generative models) is referenced in `10` but the ML theory lives in
`machine-learning-theory/`.
