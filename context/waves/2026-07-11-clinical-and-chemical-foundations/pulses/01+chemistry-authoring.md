---
wave: clinical-and-chemical-foundations
pulse: 01
date: 2026-07-11
status: done
depends_on: []
governing_roles: [reference-editor, expert-skeptic, index-weaver, ascii-cartographer]
---

# Pulse 01 - Chemistry Module Architecture and Authoring

## Mission

Stand up `chemistry/` as a first-class, non-duplicating MAXIM discipline module.
Define scope against `natural-sciences/`, `biochemistry/`, `materials/`,
`chemical-eng/`, `optics/`, `biophysics/`, and `statistical-mechanics/`, then
author the full 12-guide module at peer-level depth (not outlines or template
filler), and wire it into section/navigation surfaces and the source-corpus
pipeline.

## Scope Inventory

| Area | Files |
|---|---|
| Module guides | `chemistry/00-OVERVIEW.md` through `chemistry/11-MEASUREMENT-AND-SAFETY.md` (12 guides) |
| Module manifest | `chemistry/STATUS.md` |
| Navigation | `.mkdocs/mkdocs.yml` (Life Sciences nav), `sections/life-sciences.md` (landscape + Directories) |
| Portfolio registry | `TRACKER.md` (Summary Dashboard row + counts) |
| Source corpus | `.mdloom/backfill/sources/chemistry/**`, `.mdloom/backfill/modules/chemistry.json`, `.mdcrop/views/**`, `.mdport/packs/**`, `.fletch/registries/maxim-chemistry-source-corpus.json` |

## Scope Contract (non-duplication)

- Assumes and cross-references `natural-sciences/01-05, 17` as the general-chem
  floor; does not re-derive atomic structure, VSEPR, the four laws, intro
  kinetics, Nernst, or SN1/SN2/E1/E2.
- Defers element trends to `periodic-table/`, band theory / periodic DFT to
  `materials/`, process separations/reactors to `chemical-eng/`, PK/PD to
  `pharmacology/`, metabolism to `biochemistry/` (bridged only via bioinorganic),
  Beer-Lambert / IR-Raman selection rules to `optics/07`, protein XRD/NMR to
  `biophysics/03`, and condensed-matter stat mech to `statistical-mechanics/`.
- Uniquely owns: coordination/organometallic/bioinorganic chemistry, HSAB and
  solution equilibria, synthesis design, instrumental quantitation and
  separations, small-molecule NMR + MS fragmentation + small-molecule XRD,
  statistical thermodynamics/activity/surface catalysis, molecular computation,
  and chemical measurement/safety frameworks.

## Deliverables

- [x] `00-OVERVIEW` - discipline map (ABIOP minus B), ownership table, reading order.
- [x] `01-INORGANIC-CHEMISTRY` - CFT/LFT, Jahn-Teller, 18e rule, Pd catalysis, bioinorganic.
- [x] `02-ACID-BASE-SOLUTION` - Brønsted/Lewis/HSAB, buffers + capacity, Ksp, EDTA K'f.
- [x] `03-ORGANIC-SYNTHESIS` - retrosynthesis, named reactions, pericyclic/W-H, asymmetric, green metrics.
- [x] `04-ANALYTICAL-QUANTITATIVE` - titrimetry, voltammetry, calibration, ICH validation.
- [x] `05-SEPARATION-SCIENCE` - van Deemter, GC/HPLC/TLC/CE, extraction, hyphenated MS.
- [x] `06-NMR-SPECTROSCOPY` - 1H/13C/DEPT, 2D COSY/HSQC/HMBC/NOESY, elucidation workflow.
- [x] `07-OPTICAL-SPECTROSCOPY-AND-MS` - IR/UV-Vis interpretation, photochemistry, MS fragmentation.
- [x] `08-CRYSTALLOGRAPHY` - space groups/absences, SHELX, Flack, CSD, powder XRD.
- [x] `09-PHYSICAL-CHEMISTRY-DEPTH` - partition functions, Debye-Hückel, adsorption, surface kinetics.
- [x] `10-COMPUTATIONAL-CHEMISTRY` - QM ladder, DFT functionals, MD, QM/MM, cheminformatics.
- [x] `11-MEASUREMENT-AND-SAFETY` - GUM uncertainty, GLP, GHS/SDS/NFPA, reactive-class reference.
- [x] `STATUS.md` manifest with coverage/boundary notes.
- [x] Navigation + registry integration (mkdocs, life-sciences section, TRACKER).
- [x] Source-corpus regeneration via `module_source_backfill.py --module-dir chemistry --module-id chemistry --validate`.

## Validation

```powershell
python .claude\skills\maxim-source-backfill\scripts\module_source_backfill.py `
  --module-dir chemistry --module-id chemistry --validate
git --no-pager diff --check
```

Each guide carries a landscape diagram, layered model with equations/mechanisms,
decision-useful tables, explicit ownership/cross-reference boundaries, 3-5 reader
tasks, a Decision Cheat Sheet, and Common Confusion Points. Factual specifics
(equations, constants, named reactions, spectral values) were checked; `11` is
framed as educational hazard-classification reference that defers all actual
handling/first-aid to the SDS and EHS/professionals.

## Status

Authoring and structural integration complete; source-corpus artifacts
regenerated from the canonical guides. Pulse 02 (adversarial expert review and
BLOCK-finding repair) remains open per the wave plan.

## Non-Goals

- Do not modify `README.md`, `FOREWORD.md`, `VOLUMES.md`, `PROJECTS.md`.
- Do not rename or re-scope `medicine/` (deferred to a later wave decision).
- Do not lower the depth bar to introductory-textbook prose or template filling.
- Do not create bulk content-editing scripts over the module.
