# chemistry/ — Status

**12 files | Complete ✅**

## Files

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | Discipline map (ABIOP minus B), module boundaries, ownership table, reading order | ✅ |
| `01-INORGANIC-CHEMISTRY.md` | CFT/LFT, CFSE, Jahn-Teller, isomerism, kinetics, 18e rule, organometallics, Pd catalysis, bioinorganic | ✅ |
| `02-ACID-BASE-SOLUTION.md` | Brønsted/Lewis/HSAB, polyprotic, buffers + capacity, Ksp, EDTA conditional constants, superacids | ✅ |
| `03-ORGANIC-SYNTHESIS.md` | Retrosynthesis, named reactions, pericyclic/FMO/Woodward-Hoffmann, protecting groups, asymmetric, green metrics | ✅ |
| `04-ANALYTICAL-QUANTITATIVE.md` | Gravimetry, four titration families, potentiometry/voltammetry, calibration, standard addition, ICH validation | ✅ |
| `05-SEPARATION-SCIENCE.md` | van Deemter/plate theory, GC, HPLC, TLC, CE, LLE/SPE, hyphenated MS | ✅ |
| `06-NMR-SPECTROSCOPY.md` | ¹H/¹³C, DEPT, 2D COSY/HSQC/HMBC/NOESY, small-molecule elucidation, dynamic/solid-state | ✅ |
| `07-OPTICAL-SPECTROSCOPY-AND-MS.md` | IR/UV-Vis interpretation, photochemistry, MS fragmentation (α-cleavage, McLafferty), combined elucidation | ✅ |
| `08-CRYSTALLOGRAPHY.md` | Bragg, space groups/absences, SHELX, refinement metrics, Flack, CSD, powder XRD/Rietveld/Scherrer | ✅ |
| `09-PHYSICAL-CHEMISTRY-DEPTH.md` | Partition functions → thermochem, activity/Debye-Hückel, adsorption isotherms, surface kinetics | ✅ |
| `10-COMPUTATIONAL-CHEMISTRY.md` | QM ladder (HF→CCSD(T)), DFT functionals, basis sets, MD, free energy, QM/MM, reaction paths, cheminformatics | ✅ |
| `11-MEASUREMENT-AND-SAFETY.md` | SI/uncertainty (GUM), GLP/ALCOA+, GHS/SDS/NFPA, reactive-class recognition, PPE/controls, waste segregation | ✅ |

## Coverage Notes

`chemistry/` is chemistry **as a first-class discipline** — the upper-undergraduate-
to-graduate layer that sits above general chemistry (`natural-sciences/01-05, 17`)
and below the applied domains that consume it. It maps to the ACS certified-degree
core (**A**nalytical, **B**iochemistry, **I**norganic, **O**rganic, **P**hysical =
ABIOP) *minus* biochemistry (owned by `biochemistry/`), plus the two tracks modern
curricula require: **computational chemistry** and **laboratory measurement/safety**.

This directory deliberately does **not** re-derive general-chemistry foundations.
Atomic/quantum structure, basic bonding/VSEPR, the thermodynamic laws, intro
kinetics, electrochemical cells, and first-semester organic (functional groups,
stereochemistry, SN1/SN2/E1/E2) live in `natural-sciences/` and are treated as an
assumed floor, cross-referenced but not repeated.

Boundary contracts to avoid duplication: element-by-element properties →
`periodic-table/`; band theory and periodic/solid-state DFT → `materials/`; process-
scale reactors and distillation → `chemical-eng/`; drug PK/PD and receptor theory →
`pharmacology/`; metabolism and enzymes → `biochemistry/` (bridged only via
bioinorganic active sites in `01`); Beer-Lambert physics and IR/Raman selection rules
→ `optics/07` (this module owns spectral *interpretation* and MS fragmentation);
protein crystallography/NMR → `biophysics/03` (this module owns small-molecule XRD
and structure elucidation); condensed-matter statistical mechanics →
`statistical-mechanics/` (this module owns molecular partition functions →
thermochemistry). The focus here is **discipline-level chemistry**: coordination and
organometallic reactivity, synthesis design, instrumental analysis and structure
determination, physical-chemistry depth, molecular computation, and the measurement/
safety frameworks that make chemical work rigorous and defensible.
