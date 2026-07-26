---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-CRYSTALLOGRAPHY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:chemistry:crystallography
kind: guide
module: chemistry
section: chemistry
title: Crystallography - Small-Molecule and Powder X-ray Structure
status: source-custody
source_custody: partial
current_path: chemistry/08-CRYSTALLOGRAPHY.md
canonical_path: chemistry/08-CRYSTALLOGRAPHY.md
backsource_ids: [mdloom-backfill:chemistry:08-crystallography, git-history:chemistry:08-crystallography]
concepts: [x-ray-diffraction, space-groups, structure-refinement, powder-xrd, absolute-configuration]
root_concepts: [crystallography]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Crystallography — Small-Molecule and Powder X-ray Structure

**This guide owns** small-molecule X-ray structure determination: Bragg diffraction,
space groups and systematic absences, the phase problem and its small-molecule
solutions (direct methods/Patterson, SHELX), refinement metrics, absolute
configuration by the Flack parameter, the Cambridge Structural Database, and powder
XRD/Rietveld. **It defers** protein crystallography (MR/SAD phasing, PDB, PHENIX/
REFMAC) to `biophysics/03`, and Bravais lattices / Miller indices / crystal defects
to `materials/01`. Under favorable conditions — a good single crystal, near-atomic
resolution, and (for chirality) anomalous scattering — diffraction is the most
direct route to a full 3D atomic model and absolute configuration, and the usual
court of last appeal for a structure that `06`/`07` argued. Its reach is real but
**bounded**: X-rays scatter off electrons, so hydrogen positions, disorder, and
light-atom-only data each limit what can honestly be claimed (detailed below).

```
X-RAY STRUCTURE = INVERSE FOURIER OF A DIFFRACTION PATTERN
==========================================================================
  crystal (3D periodic)  --X-ray-->  diffraction spots (reciprocal)
                                            |
  each spot hkl has:  INTENSITY (measured, |F|^2)  +  PHASE (LOST)
                                            |
                          THE PHASE PROBLEM |
                                            v
  solve phases (direct methods / Patterson) -> electron density map
                                            |
                                 refine (SHELXL, least squares on F^2)
                                            v
  ATOMIC MODEL: xyz + thermal params -> bond lengths, angles, ABS CONFIG

  QUALITY: R1, wR2, GOF, Rint, completeness, redundancy
==========================================================================
```

---

## Bragg's Law and the Structure Factor

A crystal is a 3D grating; constructive interference occurs when path differences are
integer wavelengths — **Bragg's law**:

```
   n*lambda = 2 d sin(theta)          d = interplanar spacing; theta = half the 2theta angle
   Cu K-alpha lambda = 1.5406 A (1.54178 A weighted) | Mo K-alpha = 0.71073 A
```

Cu radiation (longer λ) spreads the pattern to higher angle — good for organics and
powder; Mo (shorter λ) gives more reflections and less absorption — the single-
crystal default. Each reflection hkl carries an amplitude from the **structure
factor**, the Fourier transform of the electron density:

```
   F(hkl) = SUM_j  f_j * exp[ 2*pi*i*(h*x_j + k*y_j + l*z_j) ]
        f_j = atomic scattering factor (heavier atom -> scatters more)
   MEASURED: intensity  I(hkl)  proportional to |F(hkl)|^2   (amplitude only)
   LOST:     the PHASE of F(hkl)   <-- the entire difficulty of crystallography
```

You measure |F| but need both |F| and phase to invert the transform back to electron
density ρ(xyz). Recovering the missing phases is *the phase problem*.

---

## Space Groups and Systematic Absences

The 3D symmetry of a crystal is one of the **230 space groups** (combinations of the
32 point groups with the 14 Bravais lattices and translational elements: screw axes,
glide planes, centering). Translational symmetry causes **systematic absences** —
whole classes of reflections that are extinguished — and reading them backwards
identifies the symmetry:

| Absence condition | Symmetry element | Meaning |
|---|---|---|
| hkl present only if h+k+l = even | body-centering (I) | |
| hkl present only if h+k, k+l, h+l even | face-centering (F) | |
| **h00 absent for h odd** | 2₁ screw along a | translation of a/2 |
| 0k0 absent for k odd | 2₁ screw along b | |
| 00l absent for l odd | 2₁ screw along c | |
| 0kl absent for k odd | b-glide ⊥ a | glide plane |

**Worked space-group ID:** absences of **h00 (h odd), 0k0 (k odd), 00l (l odd)**
indicate three mutually perpendicular **2₁ screw axes** with a primitive lattice →
space group **P2₁2₁2₁** (No. 19) — the most common space group for enantiopure
(chiral) small molecules, which is exactly why it matters for absolute-configuration
work below.

---

## Solving and Refining the Structure

**Phasing (small molecule):**

- **Direct methods** (SHELXT, SHELXD): exploit statistical phase relationships among
  strong reflections (Sayre's equation; positivity and atomicity of ρ). They work
  because small structures have few atoms and near-atomic-resolution data.
- **Patterson methods**: a Fourier of |F|² (no phases needed) gives interatomic
  vectors; a heavy atom stands out, seeding the phases — the fallback when direct
  methods stall.

**Refinement (SHELXL):** least-squares fit of the atomic model (positions + isotropic
then anisotropic displacement parameters) to the data, minimizing on **F²**. Quality
is reported as a small set of numbers you must be able to read — as *diagnostics*,
not universal pass/fail constants:

| Metric | What it is | Indicative value — context-dependent |
|---|---|---|
| **R₁** | Σ‖F_o\|−\|F_c‖ / Σ\|F_o\| (on F) | often a few % for good data; not a hard cutoff |
| **wR₂** | weighted, on F² | ~0.10–0.15 (larger by definition) |
| **GOF (S)** | goodness of fit | ~1.0 (weighting-scheme dependent) |
| **R_int** | merging R of equivalent reflections | small; grows with absorption/decay |
| completeness | fraction of unique reflections measured | high; high-angle shells matter |
| redundancy | average measurements per reflection | more is better; extra for Flack |

**These are diagnostics, not pass/fail constants.** What counts as a "good" R₁
depends on resolution, the crystal's scattering power, collection temperature,
disorder, and how much of the density is heavy atoms — a well-behaved light-atom
structure at room temperature can honestly refine higher than a heavy-atom one at
100 K. Completeness and redundancy targets likewise depend on the question:
absolute-configuration work wants high redundancy of Friedel pairs and strong
high-angle completeness, while a connectivity check tolerates less. Read these
numbers together with the difference map, the displacement parameters, and the IUCr
**checkCIF** alerts — which are prompts to *explain*, not automatic failures.

**What the model does and does not pin down.** X-rays scatter off *electrons*, so
**hydrogen atoms are located poorly** — X–H vectors come out systematically short
(density is drawn into the bond) and H is usually placed by a *riding model* rather
than freely refined; accurate H positions need **neutron diffraction**. **Disordered**
groups (solvent, flexible chains, fractional occupancies) may have no single
position and are modelled as split sites or absorbed by SQUEEZE. And
**light-atom-only** structures carry little anomalous signal, capping absolute-
configuration certainty (next section). A refined structure is a best fit to the data
under these limits, not a photograph of every nucleus.

**SQUEEZE** (PLATON) models diffuse, disordered solvent as a bulk contribution when
it cannot be modeled atom-by-atom. The deposited result is a **CIF** (Crystallographic
Information File), the machine-checkable standard that carries the coordinates,
metrics, and instrument metadata.

---

## Absolute Configuration: the Flack Parameter

Ordinary diffraction cannot tell a molecule from its mirror image (Friedel's law:
I(hkl) = I(−h−k−l)) — *unless* there is **anomalous dispersion**, a resonant
scattering term that breaks the symmetry near an absorption edge. The **Flack
parameter x** quantifies the fraction of the inverted structure:

```
   x = 0  ->  the model has the CORRECT absolute configuration
   x = 1  ->  the model is INVERTED (invert all coordinates and re-refine)
   x = 0.5 ->  approximately equal inversion (racemic) twin fractions
   reliable only with a good standard uncertainty and anomalous scatterers present
```

So a refined **x = 0.02(3)** means the absolute configuration as modeled is correct
(x is zero within three standard deviations). Light-atom (C,H,N,O-only) structures
have weak anomalous signal at Mo Kα; switching to **Cu Kα** boosts the anomalous
dispersion of O/N and makes light-atom absolute configuration determinable — the
practical reason natural-product chemists run Cu data.

---

## The Cambridge Structural Database

The **CSD** is the curated repository of >1.3 million experimentally determined
organic and metal-organic crystal structures. It is the *reference implementation* of
molecular geometry: search a substructure in **ConQuest**, retrieve real bond
lengths/angles/conformations, validate a new structure's geometry against the
population, and visualize/pack in **Mercury**. Uses range from checking that a refined
bond length is normal, to conformational and hydrogen-bond statistics, to seeding
crystal-structure prediction. (The protein analog is the PDB, `biophysics/03`.)

---

## Powder X-ray Diffraction (PXRD)

When you have a microcrystalline powder rather than a single crystal, the reflections
collapse onto **Debye-Scherrer cones**, recorded as a 1D intensity-vs-2θ pattern —
a fingerprint of the phase.

```
   single crystal: 3D array of spots   ->   full structure
   powder:         1D pattern of peaks  ->   phase ID, cell, size, quantification
```

- **Phase identification:** match peak positions/intensities against the **ICDD PDF**
  database — the standard way to say "this is anatase, not rutile."
- **Rietveld refinement:** fit the *entire* calculated profile (peak shapes,
  background, cell, atomic model) to the pattern, extracting accurate lattice
  parameters and **quantitative phase fractions** from a mixture.
- **Crystallite size** from peak broadening via the **Scherrer equation**:

```
   tau = K * lambda / (beta * cos(theta))
        tau = mean crystallite size ; K ~ 0.9 (shape factor) ;
        beta = FWHM in RADIANS (instrument-corrected) ; theta in radians
   -> broader peaks => smaller crystallites (or microstrain; separate via
      Williamson-Hall if both contribute).
```

PXRD is also the tool for **polymorph screening** (critical in pharma: different
crystal forms of the same drug have different solubility, stability, and
bioavailability), co-crystal identification, and in-situ studies of phase transitions.

---

## Reader Tasks

1. **Assign the space group from absences h00 (h odd), 0k0 (k odd), 00l (l odd).**
   Three orthogonal 2₁ screw axes, primitive lattice → **P2₁2₁2₁** (No. 19), the
   canonical chiral small-molecule space group.
2. **Interpret Flack x = 0.02(3).** The modeled **absolute configuration is correct**
   (x indistinguishable from 0 within 3σ); no inversion needed — valid *because* the
   small standard uncertainty implies adequate anomalous signal and redundancy.
   Without those (e.g., light atoms at Mo Kα), a near-zero x is not decisive.
3. **d-spacing for a peak at 2θ = 26.5° with Cu Kα?** Bragg: d = λ/(2 sinθ) =
   1.5406/(2 sin 13.25°) = 1.5406/0.4584 ≈ **3.36 Å**.
4. **Light-atom absolute configuration is ambiguous at Mo Kα — what do you do?** Switch
   to **Cu Kα** to amplify anomalous dispersion of O/N (or introduce a heavier atom),
   and collect high-redundancy Friedel pairs.
5. **You have a powder mixture and need phase fractions.** Run PXRD, identify phases
   against the ICDD PDF, then **Rietveld-refine** the full profile to quantify each
   phase; use Scherrer on the widths for crystallite size.

## Decision Cheat Sheet

| Goal | Method | Key relation / tool |
|---|---|---|
| Full 3D structure + config | single-crystal XRD | Bragg + phasing + SHELXL |
| Identify the space group | systematic absences | screw/glide/centering rules |
| Phase a small structure | direct methods (SHELXT) | statistical phase relations |
| Phase with a heavy atom | Patterson | interatomic-vector map |
| Judge a refinement | R₁, wR₂, GOF, R_int + maps | context-dependent; GOF ≈ 1, low R₁ *for the data*, clean difference map, checkCIF |
| Absolute configuration | Flack parameter | x ≈ 0 correct; Cu Kα for light atoms |
| Check geometry is normal | CSD / Mercury | substructure search |
| Identify a crystalline phase | PXRD + ICDD PDF | peak-position fingerprint |
| Quantify phases in a mixture | Rietveld | full-profile fit |
| Crystallite size | Scherrer | τ = Kλ/(β cosθ), β in radians |

## Common Confusion Points

- **You measure intensities, not phases.** |F|² comes straight from the data; the
  phases must be reconstructed. Everything hard about crystallography is the phase
  problem.
- **R-factor is a fit statistic, not proof of correctness.** A low R₁ on a wrong or
  disordered model is possible; always validate geometry (CSD, PLATON checks) and the
  difference map.
- **Refinement metrics are context-dependent, not universal thresholds.** "Good"
  R₁/R_int/completeness/redundancy scale with resolution, scattering power,
  temperature, and the question (absolute config demands more redundancy). Read them
  with the maps and checkCIF alerts, not as fixed pass/fail lines.
- **X-ray barely sees hydrogens and can't place disordered atoms uniquely.** H
  positions are approximate (riding model; use neutron diffraction for real X–H
  geometry), and disordered/solvent regions may have no single position — don't
  over-read X–H distances or a partially modelled solvent pocket.
- **Flack needs anomalous scatterers.** For C/H/N/O-only structures at Mo Kα the Flack
  uncertainty can be too large to decide configuration — the value alone is
  meaningless without its standard uncertainty and adequate redundancy.
- **Powder ≠ single crystal.** PXRD identifies and quantifies phases and refines cells;
  it rarely yields a full novel structure (structure solution from powder is possible
  but hard). For atomic positions of a new molecule, grow a single crystal.
- **Scherrer β is in radians and instrument-corrected.** Plugging FWHM in degrees, or
  ignoring instrumental broadening, gives nonsense sizes; large crystallites also
  saturate the method (>~100–200 nm).
- **This is not protein crystallography.** Small molecules diffract to atomic
  resolution and phase by direct methods; macromolecules phase by MR/SAD and deposit
  in the PDB — that workflow is `biophysics/03`.
