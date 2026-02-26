# Bionanotechnology: Drug Delivery, Biosensors, and Theranostics

## The Big Picture

Bionanotechnology applies nanoscale structures to biological and medical problems.
The field's central insight: nanoscale particles (10-200 nm) interact with biology at
the length scale of proteins, viruses, and cell organelles -- enabling unprecedented
access to biological processes.

```
BIONANOTECHNOLOGY LANDSCAPE
=============================

                NANOPARTICLE INTERACTIONS WITH BIOLOGY
                ========================================

Scale:          1 nm        10 nm       100 nm      1 um
                Proteins    QDs, AuNP   LNP,        Cells
                Antibodies  Iron oxide  Liposomes   Bacteria
                                        Viruses

Interaction level:
  Molecular:    Bind specific receptors, enzymes, DNA (targeting)
  Cellular:     Endocytosis, membrane fusion, organelle targeting
  Tissue:       EPR effect (tumor accumulation), lymphatic drainage
  Organ:        Biodistribution (liver, spleen clearance)
  Whole body:   Pharmacokinetics, immunogenicity

FIELD SEGMENTS:
  Nanomedicine:       Drug delivery, diagnostics, imaging
  Biosensors:         Detection of molecules, pathogens, biomarkers
  Theranostics:       Therapy + diagnostics in one particle
  Nanobiotechnology:  Tools for biology (single-molecule imaging, sequencing)
```

---

## Nanoparticle Pharmacokinetics: The EPR Effect

### Enhanced Permeability and Retention

```
EPR EFFECT: WHY NANOPARTICLES ACCUMULATE IN TUMORS
====================================================

Normal vasculature:
  Tight junctions: pore size ~6-12 nm (excludes most NP)
  Lymphatic drainage: removes excess fluid efficiently
  Result: large molecules/NP do not accumulate in normal tissue

Tumor vasculature (abnormal):
  Angiogenesis creates leaky, disorganized blood vessels
  Pore size: 100-800 nm (allows NP to extravasate into tumor)
  Defective lymphatic drainage: cleared material accumulates

The EPR effect (Matsumura and Maeda, 1986):
  Nanoparticles 10-200 nm in diameter:
    Pass through leaky tumor vessels
    Accumulate in tumor interstitium
    Cannot be cleared by defective lymphatics
    -> Passive tumor targeting

  Comparison:
    Free drug: accumulates in tumor AND normal tissue (systemic toxicity)
    NP-drug: preferentially accumulates in tumor (2-10x enrichment)

EPR LIMITATIONS (important):
  Variability: EPR effect varies enormously between tumor types and patients
  Human tumors: EPR less pronounced than mouse xenograft models
    (most pre-clinical EPR data from mice; human translation is challenging)
  Pressure gradient: elevated interstitial fluid pressure in tumors
    can impede NP extravasation (inward convection fights diffusion)
  EPR is sufficient for: macromolecular drugs, liposomes, albumin-NP
  EPR is not sufficient for: expecting uniform high-concentration tumor coverage

Active targeting:
  Attach ligand to NP surface (antibody, peptide, aptamer)
  Binds overexpressed receptor on tumor cells (EGFR, HER2, folate receptor)
  Improves cellular uptake, not necessarily biodistribution
  Challenge: antibody adds cost, immune recognition, stability issues
```

---

## Liposomal Drug Delivery

```
LIPOSOME STRUCTURE
==================

Lipid bilayer vesicle:
  Hydrophilic head groups face aqueous core and outer medium
  Hydrophobic tails form bilayer interior
  Size: 50-500 nm (unilamellar large: LUV 100-500 nm, SUV 20-100 nm)

  Water core: aqueous drugs (doxorubicin, cisplatin)
  Bilayer: hydrophobic drugs (amphotericin B, paclitaxel)
  Surface: targeting ligands, PEG (stealth coating)

DOXIL (first approved nanomedicine, 1995):
  Doxorubicin encapsulated in PEGylated liposome
  Composition:
    HSPC (hydrogenated soy phosphatidylcholine): structural lipid
    Cholesterol: membrane fluidity/rigidity modulator
    DSPE-PEG2000: PEGylated lipid (stealth coating)
    Doxorubicin HCl: encapsulated in aqueous core (pH gradient loading)

  PEGylation = "stealth" effect:
    PEG chains on surface: hydrophilic brush, steric repulsion
    Prevents opsonization (protein adsorption -> immune recognition)
    Increases circulation half-life: from 2 hours (free dox) to 20+ hours (Doxil)
    Allows EPR accumulation

  Outcome vs. free doxorubicin:
    Reduced cardiotoxicity (heart doesn't see as much drug)
    Increased tumor exposure (EPR effect)
    Palmar-plantar erythrodysesthesia (hand-foot syndrome): new side effect
    Approved for: Kaposi sarcoma, ovarian cancer, multiple myeloma

LIPOSOME TYPES:
  Conventional: DPPC/cholesterol, taken up by liver/spleen rapidly
  PEGylated (Stealth): long circulation, EPR targeting
  Thermosensitive: release cargo above 42 C (tumor hyperthermia triggered)
  pH-sensitive: release in acidic tumor/endosome environment
  Immunoliposome: antibody attached for active targeting
```

---

## Lipid Nanoparticles (LNP): mRNA Vaccines

The COVID-19 mRNA vaccines (BNT162b2, mRNA-1273) brought LNPs to global scale.
Their formulation is the result of decades of nucleic acid delivery research.

```
LNP COMPOSITION (COVID-19 VACCINE)
=====================================

COMPONENT          EXAMPLE (BNT162b2)      FUNCTION
-----------------  ----------------------  --------------------------------
Ionizable lipid    ALC-0315                Key component: protonatable
                   (Acuitas/BioNTech)      at low pH (endosome) -> positive
                                           charge -> membrane disruption
                                           -> mRNA escape to cytoplasm
                                           Neutral at pH 7.4 in blood
                                           (reduces toxicity)

Helper lipid       DSPC                    Structural: forms bilayer
(phospholipid)     (distearoylphosphati-   Affects particle stability,
                   dylcholine)             cellular uptake

Cholesterol        Cholesterol             Membrane fluidity, stability
                                           Facilitates endosomal escape

PEG-lipid          ALC-0159               Stealth coating: prevents
                   (PEGylated DMG)         aggregation, reduces immune
                                           recognition, controls size
                                           ~1.5-2.5 mol% (trace amount)

mRNA payload:      BNT162b2: modRNA        Encapsulated in LNP core
  SARS-CoV-2       (1-methylpseudouridine  N1-methyl-pseudouridine
  spike protein    modified)               modification: evades innate
  encoding                                 immune sensors (Toll-like
                                           receptors), reduces inflammation,
                                           increases translation efficiency

MOLAR RATIO: ALC-0315 : DSPC : cholesterol : ALC-0159 = 46.3 : 9.4 : 42.7 : 1.6

LNP SIZE: ~80-100 nm (dynamic light scattering)
ENCAPSULATION EFFICIENCY: >90% of mRNA inside LNP (Ribogreen assay)

MECHANISM:
1. IV or IM injection: LNP distributed in bloodstream/tissue
2. Cellular uptake: endocytosis (LNP 80-100 nm -> endosomal pathway)
3. Endosomal acidification (pH 5-6): ionizable lipid becomes positive
4. Ionizable lipid disrupts endosomal membrane (fusogenic state)
5. mRNA escapes to cytoplasm
6. Ribosome translates mRNA -> spike protein
7. Immune response to spike protein -> protective immunity

Pfizer/BioNTech + Moderna mRNA LNP IP: extensive patent landscape from:
  Pieter Cullis (UBC) -- ionizable lipid design
  Ian MacLachlan (Acuitas) -- LNP formulation
  Drew Weissman + Katalin Kariko (Penn) -- mRNA modification
```

---

## Biosensors

### Surface Plasmon Resonance (SPR)

```
SURFACE PLASMON RESONANCE (SPR) BIOSENSOR
===========================================

PRINCIPLE:
  Evanescent wave at thin gold film/aqueous interface
  Resonance condition: specific angle theta_SPR

  Gold film (50 nm) on glass prism
  Polarized light hits gold from glass side at angle theta
  At theta_SPR: photons couple to surface plasmon waves on gold
    -> reflected light intensity drops to near zero

  When molecules bind to gold surface:
    Refractive index at surface changes
    theta_SPR shifts proportionally to bound mass
    delta_theta_SPR ~ delta_m / Area (ng/cm^2)

BIACORE (GE Healthcare, now Cytiva):
  Standard instrument; SPR + microfluidics
  Flow cell: protein/antibody immobilized on sensor chip
  Analyte flows over surface; binding increases response units (RU)
  1 RU ~ 10^-9 g/cm^2 bound mass

  Sensorgram:
    Association phase: analyte flows, signal rises as it binds
    Dissociation phase: buffer flows, signal falls as it unbinds
    Regeneration: strip bound analyte, reuse surface

  Kinetic parameters extracted:
    k_on = association rate constant (M^-1 s^-1)
    k_off = dissociation rate constant (s^-1)
    K_D = k_off / k_on = equilibrium dissociation constant
    K_D typical for antibody-antigen: 10^-7 to 10^-12 M

  Advantage: label-free (no fluorophore needed)
  Detection limit: ~0.1 ng/cm^2 (pg/mL for typical proteins)
  Used in: drug discovery (binding affinity measurement), antibody characterization
```

### Nanopore Sequencing (Oxford Nanopore)

```
NANOPORE DNA SEQUENCING
========================

CONCEPT (Deamer/Branton, 1990s):
  Thread single-stranded DNA through 2 nm pore
  Ionic current flows through pore (KCl solution, voltage applied)
  Each nucleotide (A,T,G,C) partially blocks pore differently
  Read sequence from current blockade pattern

OXFORD NANOPORE TECHNOLOGY:
  Biological protein nanopore: CsgG or MspA (engineered variants)
    Pore diameter: ~1.4-2 nm
    Pore embedded in synthetic lipid bilayer
  Ratchet enzyme (motor protein): controls DNA translocation speed
    ~450 bases per second standard; ~1000 bases/s fast mode

  Ionic current signal:
    Unblocked pore: ~100-200 pA
    DNA in pore: ~20-100 pA (depends on kmer in pore)
    ~5 bases in pore simultaneously read as combined signal

  BASECALLING:
    Current trace -> neural network (recurrent/transformer models) -> base sequence
    Error rate: ~1-5% raw reads (higher than Illumina ~0.1%)
    Can be reduced with consensus calling (multiple reads same region)

  ADVANTAGE: ULTRA-LONG READS
    Illumina: 150-300 bp reads (require assembly)
    PacBio HiFi: ~15 kb reads (highly accurate)
    Oxford Nanopore: 10 kb - 4 Mb reads demonstrated
    Long reads: can span repetitive regions, structural variants, chromosome assembly

  APPLICATIONS:
    Real-time: sequence reads as they come off device (no batch)
    MinION: pocket-sized, USB, $1000 device, 50 Gb/run
    PromethION: high-throughput, 12 Tb/run
    Clinical virology: pathogen ID in remote settings (Congo, ISS)
    Nanopore direct RNA: read RNA without cDNA conversion
    Epigenetics: detect 5mC methylation directly (no bisulfite conversion)
```

---

## Theranostics: Therapy + Diagnostics in One Particle

```
THERANOSTIC NANOPARTICLE
=========================

Combines:
  DIAGNOSTIC: imaging agent (MRI contrast, PET tracer, fluorescent, photoacoustic)
  THERAPEUTIC: drug payload, photothermal, photodynamic, radioactivity

EXAMPLES:

1. SPION-Drug conjugate:
   Fe3O4 core (MRI dark contrast T2)
   Doxorubicin attached via pH-sensitive linker (releases in acidic endosome/tumor)
   PEG + targeting antibody (anti-HER2)
   -> MRI can show where NP went; drug released at tumor site
   Status: multiple phase I/II trials; not yet FDA-approved combination theranostic

2. Gold nanorod + dye:
   AuNR: NIR absorption (650-900 nm) for photothermal therapy
   Dye: fluorescence imaging (Cy5 or NIR dye)
   -> Image tumor location, then irradiate with NIR laser to heat and kill
   Status: phase I trials (Nanospectra AuroLase 15 nm gold nanoshell)

3. Radiolabeled PSMA-targeted NP:
   PSMA (prostate-specific membrane antigen) targeting ligand
   ^177Lu radioactive label (beta decay, therapeutic dose)
   PSMA-617: small molecule theranostic (not nanoparticle, but principle same)
   -> FDA approved 2022 (Pluvicto) for mCRPC

4. Photodynamic therapy (PDT) NP:
   Photosensitizer (chlorin e6, porphyrin) loaded in NP
   Light activation -> singlet oxygen (^1O2) generation -> oxidative cell damage
   NP targets tumor (EPR + active), then light treatment applied
   Advantage: localized; no systemic toxicity if light focused to tumor

PROTEIN CORONA PROBLEM:
  When NP enter blood, plasma proteins adsorb rapidly (within seconds)
  Forming "protein corona": albumin, fibrinogen, apolipoproteins
  This corona, not the designed surface, is what cells actually see
  Can redirect biodistribution, reduce targeting efficiency
  Active area of research: design surfaces that resist or control corona
```

---

## Decision Cheat Sheet

| Clinical Goal | Best Current Nanoformulation |
|---------------|------------------------------|
| Reduce doxorubicin cardiac toxicity | Doxil (PEGylated liposome) |
| mRNA vaccine delivery | Lipid nanoparticle (LNP) |
| MRI tumor imaging | SPION (T2 contrast) or Gd-chelate (T1) |
| Tumor hyperthermia | Fe3O4 NP + AC magnetic field |
| Label-free binding kinetics | SPR (Biacore) |
| Long-read DNA sequencing | Oxford Nanopore MinION |
| Real-time pathogen ID (field) | Oxford Nanopore rapid PCR + nanopore |
| Photothermal tumor therapy | AuNR or gold nanoshell + NIR laser |
| Photodynamic therapy | Photosensitizer-loaded NP + light |
| Drug delivery to brain (BBB) | Exosomes, LNP with brain-targeting peptides |

---

## Common Confusion Points

**"EPR targeting makes nanoparticle cancer drugs highly specific."** EPR is passive and
inconsistent. Meta-analyses show only ~0.7% of injected NP dose reaches tumor in humans
on average (Wilhelm 2016 Science survey). Active targeting improves uptake into cells
but does not dramatically improve tumor accumulation. This has led to re-evaluation of
the EPR paradigm.

**"PEGylation makes nanoparticles invisible to the immune system."** PEGylation extends
circulation time significantly but not indefinitely. Anti-PEG antibodies can form (ABC
phenomenon -- accelerated blood clearance on repeat dosing). Some patients have pre-existing
anti-PEG antibodies from PEG-containing consumer products.

**"Nanopore sequencing replaces Illumina."** They are complementary. Illumina: short reads,
high accuracy, high throughput, low cost per base. Nanopore: long reads, lower accuracy,
real-time, portable. Long reads solve problems short reads cannot (structural variants,
repeat regions, haplotype phasing).

**"Theranostics are clinically approved."** Combined therapy+imaging in single particle:
mostly still in trials. However, PSMA-617 (Pluvicto) is the first radioligand theranostic
FDA-approved (2022) -- a small molecule, not a nanoparticle, but the theranostic principle.
Nanoscale theranostics: clinical trials ongoing, few approvals.
