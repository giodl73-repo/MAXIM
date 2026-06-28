# biochemistry/ — Status

**10 files | Complete ✅**

## Files

| File | Topic | Status |
|------|-------|--------|
| `00-OVERVIEW.md` | The biochemistry landscape — chemistry of life, flux networks | ✅ |
| `01-BIOMOLECULES.md` | Water/pH, carbohydrates, lipids, proteins, nucleic acids | ✅ |
| `02-PROTEIN-STRUCTURE.md` | Primary→quaternary, folding, motifs, domains | ✅ |
| `03-ENZYMES-AND-KINETICS.md` | Catalysis, Michaelis-Menten, inhibition, allostery | ✅ |
| `04-METABOLISM-OVERVIEW.md` | Catabolism/anabolism, ATP/NAD(P)H carriers, regulation | ✅ |
| `05-GLYCOLYSIS-AND-GLUCONEOGENESIS.md` | EMP pathway, net yields, reciprocal regulation | ✅ |
| `06-TCA-AND-OXIDATIVE-PHOSPHORYLATION.md` | Citric acid cycle, ETC, chemiosmosis, ATP yield | ✅ |
| `07-LIPID-AND-AMINO-ACID-METABOLISM.md` | β-oxidation, ketones, urea cycle | ✅ |
| `08-PHOTOSYNTHESIS-AND-CARBON.md` | Light reactions, Calvin cycle, C4/CAM | ✅ |
| `09-MOLECULAR-AND-REGULATION.md` | Signaling, hormones, second messengers | ✅ |

## Coverage Notes

`biochemistry/` is the **chemistry of life**: the molecules cells are built
from, the enzymes that catalyze their transformations, and the metabolic
pathways that extract and store energy. It treats metabolism as a flux network
and regulation as feedback control — the natural systems framing for a software
reader.

This directory deliberately does **not** re-derive the central dogma machinery.
DNA structure, replication, transcription, and translation live in `biology/`
(especially `01-MOLECULAR-MACHINERY`); `09-MOLECULAR-AND-REGULATION.md` bridges
to them rather than duplicating. Pure-chemistry foundations (bonding,
thermodynamics, reaction kinetics in the abstract) live in `natural-sciences/`.
Drug-target and inhibitor pharmacodynamics extend into `pharmacology/`;
sequence-level genetics into `genomics/`; dietary macronutrient context into
`nutrition/`. The focus here is **metabolism and molecular function**: stoichiometry,
ΔG, ATP yields, kinetics, and allosteric control.
