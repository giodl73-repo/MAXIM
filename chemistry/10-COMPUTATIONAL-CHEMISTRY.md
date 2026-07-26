---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:computational-chemistry
kind: guide
module: chemistry
section: chemistry
title: Computational Chemistry - Quantum Chemistry, MD, Cheminformatics
status: source-custody
source_custody: partial
current_path: chemistry/10-COMPUTATIONAL-CHEMISTRY.md
canonical_path: chemistry/10-COMPUTATIONAL-CHEMISTRY.md
backsource_ids: [proof-backfill:chemistry:10-computational-chemistry, git-history:chemistry:10-computational-chemistry]
concepts: [quantum-chemistry, density-functional-theory, molecular-dynamics, qm-mm, cheminformatics]
root_concepts: [computational-chemistry]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Computational Chemistry — Quantum Chemistry, MD, Cheminformatics

**This guide owns** molecular computation: the ab-initio/DFT method ladder for
*discrete molecules*, basis sets, molecular dynamics for solution/biomolecular
systems, free-energy and QM/MM methods, reaction-path finding, and cheminformatics
(SMILES/InChI, databases, RDKit, QSAR). **It defers** periodic DFT for solids
(plane waves, k-points, band structure) to `materials/09`, and machine-learning
theory to `machine-learning-theory/`. For a CS reader this is the most familiar
guide in the module: it is an **accuracy-vs-compute tradeoff ladder** with an
approximation hierarchy exactly like numerical methods.

```
THE ACCURACY / COST LADDER (pick your rung per problem)
==========================================================================
  cost   method                electron correlation     scaling
  ----   ------                --------------------     -------
  low    Molecular Mechanics   none (empirical FF)      O(N) - O(N log N)
   |     Semiempirical (PM6)   parameterized            O(N^3)
   |     DFT (GGA/hybrid)      approximate (functional) O(N^3) - O(N^4)
   |     HF (Hartree-Fock)     NONE (mean field)        O(N^4)
   |     MP2                   2nd-order perturbation    O(N^5)
   |     CCSD                  coupled cluster           O(N^6)
  high   CCSD(T) "gold std"    ~exact (single-ref)       O(N^7)
         CASSCF/CASPT2         multireference (biradicals, excited)

  RULE: match the rung to the question. Geometry: cheap DFT. Barrier
  height / thermochem to 1 kcal/mol: CCSD(T)/CBS. Big system: MM/MD.
==========================================================================
```

---

## Ab Initio Quantum Chemistry

**Hartree-Fock (HF)** is the reference: each electron moves in the *mean field* of
the others, giving the **Roothaan equations** (LCAO → a matrix eigenvalue problem
solved self-consistently, the SCF cycle). Its defining flaw is **no electron
correlation** — it misses the instantaneous electron-electron avoidance, so it gets
bond energies and barriers wrong and cannot describe dispersion at all. Correlated
("post-HF") methods add it back at rising cost:

| Method | Adds | Scaling | Notes |
|---|---|---|---|
| HF | mean field | O(N⁴) | no correlation; wrong energetics |
| MP2 | 2nd-order perturbation | O(N⁵) | cheap correlation; good for closed shells; fails near-degeneracy |
| CCSD | coupled-cluster singles+doubles | O(N⁶) | size-consistent |
| **CCSD(T)** | + perturbative triples | O(N⁷) | **"gold standard"**; ~1 kcal/mol with CBS |
| CASSCF/CASPT2 | multireference | steep | biradicals, bond breaking, excited states |

**CCSD(T)/CBS** reaches **chemical accuracy** (~1 kcal/mol) for thermochemistry of
single-reference molecules and is the benchmark everything else is measured against.
When a system has near-degenerate configurations (transition states with partial
bonds, biradicals, many transition-metal excited states), single-reference methods
break and you need **multireference** CASSCF/CASPT2.

---

## Density Functional Theory (for molecules)

DFT replaces the many-electron wavefunction with the electron density; the
approximation lives entirely in the **exchange-correlation functional**, organized
as Perdew's **"Jacob's ladder"** of rising sophistication:

```
   Jacob's ladder (accuracy climbs, so does cost/empiricism)
   rung 5  double-hybrid  B2PLYP     (adds MP2-like correlation)
   rung 4  hybrid         B3LYP (20% exact exch.), PBE0 (25%),
                          range-separated wB97X-D, CAM-B3LYP (charge transfer)
   rung 3  meta-GGA       TPSS, SCAN, M06-L (uses kinetic-energy density)
   rung 2  GGA            PBE, BLYP  (uses density gradient)
   rung 1  LDA            SVWN       (uniform electron gas; overbinds)
```

B3LYP is the long-time default workhorse; range-separated hybrids (ωB97X-D,
CAM-B3LYP) fix charge-transfer and Rydberg states that plain hybrids get badly wrong.

**The dispersion problem (why B3LYP fails on van der Waals):** standard
(semi)local functionals have no long-range correlation, so they miss London
dispersion — π-stacking energies, host-guest binding, and conformer preferences come
out qualitatively wrong. **The fix is an add-on empirical correction, Grimme's
DFT-D3 with Becke-Johnson damping (D3-BJ)**, or a dispersion-inclusive functional
(the ωB97X-D "-D" is exactly this). Never run conformational or non-covalent work
with an uncorrected functional. **TDDFT** extends DFT to excited states / UV-Vis
(good for valence π→π*, n→π* within ~0.3 eV; needs range-separation for
charge-transfer).

### Basis sets

The LCAO expansion uses Gaussian-type orbitals (GTOs — analytic integrals) rather
than the physically correct but expensive Slater-type:

| Family | Examples | Use |
|---|---|---|
| Minimal / split-valence (Pople) | STO-3G, 6-31G*, 6-311G** | * = polarization (d on heavy); ** adds p on H |
| Diffuse-augmented | 6-31+G, aug-cc-pVXZ | anions, excited states, weak interactions |
| Dunning correlation-consistent | cc-pVDZ → cc-pVTZ → cc-pVQZ | systematic **CBS extrapolation** |

Two traps: **basis-set superposition error (BSSE)** inflates binding energies (fix
with counterpoise correction), and small bases give artificially good numbers by
error cancellation. Converge the basis (or extrapolate to CBS) before trusting an
energy.

---

## Molecular Mechanics and Dynamics

For thousands–millions of atoms (proteins, membranes, solvated drugs), quantum
methods are hopeless; **molecular mechanics** models atoms as balls-and-springs with
a classical **force field**:

```
   E_total = E_bond + E_angle + E_dihedral + E_improper + E_vdW(LJ) + E_elec(Coulomb)
   FIELDS: AMBER, CHARMM (biomolecules) ; OPLS-AA (liquids) ; GAFF/CGenFF (small mol)
   PARAMS: geometry+Hessian from QM ; partial charges from RESP/CM5
   LIMITS: no bond breaking ; fixed charges (no polarization) unless AMOEBA-type FF
```

**Molecular dynamics (MD)** integrates Newton's equations with **velocity Verlet**,
timestep **1–2 fs** (2 fs with H-bond constraints, SHAKE/LINCS). Control ensembles
with thermostats and barostats — and know which are rigorous:

| Component | Rigorous choice | Equilibration-only |
|---|---|---|
| Thermostat (NVT) | Nosé-Hoover chains, V-rescale | Berendsen (wrong fluctuations) |
| Barostat (NPT) | Parrinello-Rahman | Berendsen |
| Long-range electrostatics | PME (Ewald), O(N log N) | plain cutoff (artifacts) |

Standard protocol: **minimize → heat → NPT equilibrate → NVT/NPT production**.
**Free-energy methods** extract the quantities experiments measure:

```
   FEP  : Delta A = -kT ln <exp(-Delta U / kT)>_0   (alchemical mutation A->B)
   TI   : Delta A = INT_0^1 <dU/d.lambda>_lambda d.lambda
   Umbrella sampling + WHAM : PMF along a reaction coordinate
   Metadynamics : history-dependent bias fills wells to escape them
```

Relative binding free energy (RBFE/FEP+) is now a production tool in drug discovery
for ranking congeneric analogs.

**QM/MM** treats a reactive core with QM and its environment with MM (link atoms at
the boundary, electrostatic embedding so MM charges polarize the QM density; **ONIOM**
is the layered form). It is the standard for enzyme mechanisms and reactions in a
protein pocket.

**Reaction paths:** optimize minima (BFGS/L-BFGS), find transition states
(quasi-Newton/Berny, QST2/QST3), then run an **intrinsic reaction coordinate (IRC)**
— steepest descent in mass-weighted coordinates from the TS — to *prove* the TS
connects the intended reactants and products; **NEB** finds the minimum-energy path
between two known endpoints. A TS is validated by exactly one imaginary vibrational
frequency plus the IRC check.

---

## Cheminformatics and QSAR

The data layer: molecules as canonical text and searchable databases.

```
   SMILES : linear string for a molecular graph. aspirin = CC(=O)Oc1ccccc1C(=O)O
            (c = aromatic; ring-closure digits; @/@@ = stereo; / \ = E/Z)
   InChI / InChIKey : IUPAC canonical identifier + hashed key for exact lookup
   DATABASES: PubChem/ChEMBL (open) ; CAS SciFinder, Reaxys (reactions, subscription)
   TOOLKITS : RDKit (Python: parsing, fingerprints, descriptors, substructure) ;
              Open Babel (format conversion) ; PyMOL/VMD (visualization)
```

**QSAR/QSPR** regresses activity/property against molecular descriptors (topological,
electronic, 3D pharmacophoric) with MLR/PLS or ML models — validated by
cross-validation, an external test set, Y-scrambling, and an applicability-domain
check. The famous heuristic is **Lipinski's Rule of Five** for oral bioavailability:
MW ≤ 500, logP ≤ 5, H-bond donors ≤ 5, acceptors ≤ 10. To get aspirin's logP with
RDKit: parse the SMILES to a molecule, then call the Crippen logP descriptor
(`Descriptors.MolLogP`) — a one-line computed estimate (**≈1.31** from RDKit's
Crippen implementation) used to flag druglikeness at scale.

---

## End-to-End Workflow: From Molecule to a Validated Number

A method menu is not a calculation. A *defensible* result comes from a fixed
pipeline that pins down the molecular state, the model, the environment, and the
checks — then validates against something independent and archives enough to
reproduce. Worked on a case where shortcuts famously give the **wrong sign**: the
tautomer equilibrium **2-hydroxypyridine ⇌ 2-pyridone**, whose preferred form
*reverses* between gas phase and water.

```
END-TO-END: A DEFENSIBLE RELATIVE-ENERGY CALCULATION
  case: 2-hydroxypyridine  <=>  2-pyridone   (a tautomer equilibrium)

  0. STATE the species  : charge 0, singlet (mult 1); neutral microspecies
                          at ~pH 7 ; enumerate BOTH tautomers (that IS the Q)
  1. CONFORMERS         : generate + prune rotamers (here O-H syn/anti; ring
                          is rigid) -> keep low-E set (RDKit ETKDG / CREST)
  2. METHOD + BASIS     : dispersion-corrected DFT (wB97X-D or M06-2X) /
                          def2-TZVP ; plan a CCSD(T)/CBS or expt check
  3. SOLVENT            : implicit continuum (SMD or CPCM) -- REQUIRED here;
                          gas and water give DIFFERENT answers
  4. OPT + FREQ         : optimize each; freq check = 0 imaginary (a minimum);
                          freq -> ZPE + thermal -> compare GIBBS energies
  5. DIAGNOSTICS        : SCF + tight geometry convergence; fine grid;
                          single-reference OK (small T1); <S^2>~0 (closed shell)
  6. VALIDATE           : reproduce experiment / a higher level (table below)
  7. ARCHIVE            : functional+dispersion, basis, solvation model+radii,
                          grid, T, software+version, xyz, energies (FAIR record)
```

**State, conformers, method.** Both tautomers are neutral closed-shell singlets, so
charge/spin is settled; the *point* of the problem is to enumerate the two tautomers
(and, for 2-hydroxypyridine, its syn/anti O–H rotamers) rather than assume one.
Geometry is cheap on dispersion-corrected DFT; benchmark energetics want CCSD(T)/CBS
or experiment.

**Solvent is the crux.** Optimize each species and run frequencies (0 imaginary
frequencies confirms a true minimum; the frequencies give ZPE + thermal corrections
so you compare **Gibbs** energies, not bare electronic energies). Do it **twice** —
gas phase and with an implicit solvent (SMD/CPCM) — because that is exactly where the
answer moves.

| Phase | Computed ΔG (pyridone − hydroxy) | Experiment | Verdict |
|---|---|---|---|
| Gas | expected small **positive** ΔG: 2-hydroxypyridine slightly favored | 2-hydroxy slightly favored | target sign for a pinned run |
| Water (SMD) | expected **negative** ΔG: 2-pyridone strongly favored | 2-pyridone strongly favored | target solvent reversal |

These are **benchmark expectations**, not results generated by this repository.
A reproducible calculation must pin input geometries, software/version, functional,
basis, dispersion, solvent model, grid, convergence thresholds, temperature, and
the resulting electronic/ZPE/thermal energies before reporting a numerical ΔG or K.

The physics is transparent: 2-pyridone has the much larger dipole (~4 D vs ~1.5 D),
so a polar continuum stabilizes it far more, flipping a ~few-kJ/mol gas-phase
preference into a ~15-kJ/mol aqueous preference. **Validation** here means the
calculation *reproduces the experimentally known reversal* (and, ideally, the gas-
phase ΔG within a high-level CCSD(T) reference) — not merely that it converged.

**Diagnostics and reproducibility.** Confirm SCF and tight geometry convergence, a
fine integration grid, that the wavefunction is single-reference (small T1/D1 — safe
for these closed-shell aromatics), and no spin contamination. Then **archive the full
spec**: functional + dispersion correction, basis set, solvation model and cavity
radii, integration grid, temperature, software **version**, and the optimized
coordinates and energies — so the number is reproducible, not a screenshot.

**Rejected alternatives (each gets the case wrong).**

- **Gas-phase-only** — reports 2-hydroxypyridine, the wrong species in water.
- **An uncorrected functional (LDA / plain B3LYP)** — no London dispersion; a poor
  choice for conformer/relative energies (use D3(BJ) or ωB97X-D/M06-2X).
- **One tautomer / one conformer** — you cannot answer a tautomer question by
  assuming the answer, or by scoring a single high-energy rotamer.
- **Comparing electronic energies, skipping ZPE/thermal** — you need Gibbs energies;
  omitting the frequency step can flip small differences.
- **A minimal basis** — error cancellation flatters it; converge the basis (or note
  BSSE for any *intermolecular* energy — minor for this unimolecular comparison).

---

## Reader Tasks

1. **Why does B3LYP fail for van der Waals dispersion, and what do you add?** Local/
   hybrid functionals lack long-range correlation → no London dispersion; add
   **Grimme D3(BJ)** (or use a dispersion-corrected functional like ωB97X-D) before
   any stacking/conformer/binding study.
2. **From a transition state to a validated mechanism?** Optimize the TS (one imaginary
   frequency), then run the **IRC** downhill both ways; if it lands on the intended
   reactants and products, the TS is confirmed to connect them.
3. **SMILES for aspirin and its logP?** `CC(=O)Oc1ccccc1C(=O)O`; parse in RDKit and
   compute `Descriptors.MolLogP` (**≈1.31**, RDKit's Crippen value), then check it
   against Lipinski's Rule of Five.
4. **What method for 1 kcal/mol thermochemistry?** **CCSD(T)** extrapolated to the
   complete basis set (CCSD(T)/CBS); DFT is too functional-dependent for benchmark
   energetics.
5. **Which thermostat for a production NVT run?** Nosé-Hoover chains or V-rescale
   (correct canonical fluctuations); Berendsen is fine for equilibration only.
6. **Which tautomer dominates in water — 2-hydroxypyridine or 2-pyridone?** Don't
   answer from a gas-phase electronic energy: enumerate both tautomers, optimize with
   dispersion-corrected DFT + frequencies (compare **Gibbs**, not electronic,
   energies), and add an implicit solvent (SMD). **2-pyridone** wins in water though
   2-hydroxypyridine edges it in vacuum — then validate against the known experimental
   reversal and archive the full spec.

## Decision Cheat Sheet

| Task | Method | Why |
|---|---|---|
| Geometry / vibrational frequencies | DFT (B3LYP-D3 / ωB97X-D, 6-31+G*) | cheap, reliable structures |
| Benchmark thermochemistry / barriers | CCSD(T)/CBS | chemical accuracy |
| Biradical / bond-breaking / many excited states | CASSCF/CASPT2 | multireference needed |
| Non-covalent / conformers | dispersion-corrected DFT | uncorrected functionals fail |
| Excited states / UV-Vis | TDDFT (range-separated for CT) | affordable spectra |
| 10³–10⁶ atoms, dynamics | MM/MD (AMBER/CHARMM/OPLS) | QM infeasible |
| Enzyme mechanism | QM/MM (ONIOM) | reactive core + environment |
| Confirm a transition state | IRC (+ 1 imaginary freq) | proves connectivity |
| Rank analog binding | FEP/TI (RBFE) | rigorous ΔΔG |
| Screen druglikeness at scale | QSAR + Rule of Five | descriptor models |
| Store/search molecules | SMILES/InChI + RDKit | canonical, searchable |
| Run a defensible calculation | the 8-step workflow | state→conformers→method/basis→solvent→opt+freq→diagnostics→validate→archive |

## Common Confusion Points

- **DFT is not one method.** Results depend on the functional; "we did DFT" is
  meaningless without naming it and its dispersion correction. B3LYP-D3 ≠ LDA ≠ ωB97X-D.
- **This is molecular QM, not solid-state.** Gaussian bases, molecular thermochemistry,
  and solution MD live here; plane-wave periodic DFT, k-points, and band structure are
  `materials/09`.
- **A low energy from a small basis can be luck.** Error cancellation flatters minimal
  bases; converge the basis or extrapolate, and correct BSSE for interaction energies.
- **A stationary point is not automatically a transition state.** A real TS has exactly
  one imaginary frequency *and* an IRC that connects the right endpoints.
- **Compare Gibbs energies in the right phase and state — not electronic energies in
  vacuum.** A relative energy without ZPE/thermal corrections, solvation, a conformer
  search, and the correct protonation/tautomer state can get even the *sign* wrong
  (2-hydroxypyridine vs 2-pyridone is the textbook example).
- **MD force fields cannot break bonds.** Classical FFs have fixed connectivity and
  (usually) fixed charges; reactions need QM/MM or reactive force fields (ReaxFF).
- **Berendsen thermostat/barostat give wrong fluctuations.** Great for gentle
  equilibration, invalid for sampling a true ensemble — switch to Nosé-Hoover /
  Parrinello-Rahman for production.
