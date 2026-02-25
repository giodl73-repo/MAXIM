# The AlphaFold Era — Architecture, Database, and What Remains Unsolved

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   THE ALPHAFOLD ERA LANDSCAPE                             │
│                                                                            │
│  TIMELINE:                                                                 │
│  1951: Pauling: α-helix and β-sheet from H-bond geometry                 │
│  1957: First protein structure (myoglobin, Kendrew) by X-ray             │
│  1969: Levinthal's paradox — folding cannot be exhaustive search         │
│  1994: CASP competition begins (biennial structure prediction contest)    │
│  2018: AlphaFold1 (CASP13): first major improvement in 20 years          │
│  2020: AlphaFold2 (CASP14): near-experimental accuracy; solved CASP      │
│  2021: AlphaFold2 paper + code released; 200M+ structure database        │
│  2022: ESMFold (Meta), RoseTTAFold; RFdiffusion (de novo design)         │
│  2023-24: AlphaFold3 (DNA/RNA/small molecules); RF2/Boltz-1              │
│                                                                            │
│  WHAT ALPHAFOLD2 SOLVED:                                                  │
│  Static 3D structure of most single-chain soluble proteins                │
│  → Near-experimental quality (TM-score ≈ 0.9 on CASP14)                 │
│                                                                            │
│  WHAT REMAINS UNSOLVED:                                                    │
│  Protein dynamics / conformational ensembles                              │
│  Intrinsically disordered proteins (IDPs)                                 │
│  Protein-protein interaction prediction at atomic resolution              │
│  Drug design (structure → binding → efficacy is long chain)              │
│  Function prediction from structure                                       │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — What AlphaFold2 Actually Does

### Input Representation

AlphaFold2 takes a single-chain amino acid sequence and produces a 3D structure.
The critical feature is that it builds a Multiple Sequence Alignment (MSA)
from the input sequence:

```
  INPUT: Amino acid sequence (single chain)
    ↓
  MSA SEARCH:
    Search UniRef90, BFD (Big Fantastic Database), MGnify
    Find evolutionarily related sequences (homologs)
    Align: each row = one homolog; each column = one position
    Typical MSA: 100-10,000 sequences × L residues (L = length)
    ↓
  TEMPLATE SEARCH:
    Find known structures with sequence similarity to input
    Used as structural priors in structure module
```

Why the MSA matters: covariation. If positions i and j are in contact in the
3D structure, mutations that disrupt one are often compensated by mutations at
the other over evolutionary time. This covariation signal in the MSA encodes
distance information.

### Architecture Overview

```
┌──────────────────────────────────────────────────────────────────────────┐
│  ALPHAFOLD2 ARCHITECTURE                                                  │
│                                                                            │
│  ┌────────────────────────────────────────────────────────┐              │
│  │  MSA representation: [N_seq × L × c_m]                │              │
│  │  Pair representation: [L × L × c_z]                    │              │
│  └────────────────┬───────────────────┘                   │              │
│                   │                                        │              │
│  ┌────────────────▼────────────────────────────────────┐  │              │
│  │  EVOFORMER STACK (48 blocks)                        │  │              │
│  │                                                      │  │              │
│  │  MSA row attention: attention across MSA rows       │  │              │
│  │  (shared queries per column — efficient)            │  │              │
│  │  MSA column attention: attention within each col.  │  │              │
│  │  MSA transition: feed-forward                       │  │              │
│  │                                                      │  │              │
│  │  Pair triangular multiplicative update:             │  │              │
│  │    z[i,j] updated from z[i,k] and z[k,j]           │  │              │
│  │    (triangle inequality: ij < ik + kj)              │  │              │
│  │  Pair triangular attention (outgoing/incoming)      │  │              │
│  │  Pair transition: feed-forward                      │  │              │
│  │                                                      │  │              │
│  │  MSA ↔ Pair communication via "outer product mean"  │  │              │
│  └────────────────┬────────────────────────────────────┘  │              │
│                   │                                        │              │
│  ┌────────────────▼────────────────────────────────────┐  │              │
│  │  STRUCTURE MODULE (8 blocks)                        │  │              │
│  │                                                      │  │              │
│  │  Invariant Point Attention (IPA):                   │  │              │
│  │    Residues represented as rigid frames             │  │              │
│  │    (R_i ∈ SO(3), t_i ∈ R³)                          │  │              │
│  │    Attention is SE(3)-invariant                     │  │              │
│  │    Updates frames based on pair representation      │  │              │
│  │                                                      │  │              │
│  │  Backbone update: update R_i, t_i per residue       │  │              │
│  │  Sidechain prediction: 8-layer MLP for chi angles   │  │              │
│  │  FAPE loss: frame-aligned point error               │  │              │
│  └────────────────┬────────────────────────────────────┘  │              │
│                   ↓                                        │              │
│  3D STRUCTURE + pLDDT + PAE (predicted aligned error)      │              │
└──────────────────────────────────────────────────────────────────────────┘
```

### The Evoformer: Attending Over Evolutionary Covariation

The Evoformer is the core innovation. It jointly updates the MSA and pair
representations using attention mechanisms:

```
  MSA REPRESENTATION:
    m[s,i] = embedding for residue i in sequence s
    Row attention: for each residue position i,
      attention over sequences: which sequences are informative?
    Column attention: for each sequence s,
      attention over residue positions: sequential context

  PAIR REPRESENTATION:
    z[i,j] = embedding for pair (residue i, residue j)
    Encodes: distance likelihood, contact probability, relative orientation
    Updated by triangular operations (geometric consistency):

    Triangular multiplicative update ("outgoing"):
      z[i,j] ← f(z[i,k], z[k,j]) for all k
    Intuition: if I know the geometry of (i,k) and (k,j),
      update my belief about (i,j)
    This is a geometric consistency constraint — triangle inequality in 3D space
    is encoded softly through the pair representation.
```

### Invariant Point Attention (IPA)

The structure module represents each residue as a rigid body frame
(rotation matrix + translation vector). IPA is SE(3)-invariant:

```
  RESIDUE FRAME REPRESENTATION:
    Each residue i: frame T_i = (R_i, t_i)
    R_i ∈ SO(3): orientation (3x3 rotation matrix)
    t_i ∈ R³: position (Cα coordinates)

  IPA ATTENTION:
    Query/key/value: functions of single-residue features s_i
    Geometric bias: weighted by |R_i q_iᵖ + t_i - (R_j q_jᵖ + t_j)|²
    (distances between points in each residue's local frame)
    SE(3)-invariant: attention is unchanged by global rotation/translation

  Why invariant?:
    Physics is SE(3)-invariant (same protein in different orientations = same protein)
    IPA bakes this in, avoiding the need to learn this symmetry from data

  FAPE LOSS (Frame Aligned Point Error):
    L_FAPE = (1/N_frames)(1/N_atoms) Σᵢⱼ |Rᵢᵀ(xⱼ - tᵢ) - Rᵢᵀ(x̂ⱼ - tᵢ)|
    Computes atom position errors in every residue's local reference frame
    SE(3)-invariant loss function for backbone training
```

### Confidence Metrics: pLDDT and PAE

AlphaFold2 outputs are not just atomic coordinates but confidence estimates:

```
  pLDDT (predicted Local Distance Difference Test):
    Range: 0-100 (higher = more confident)
    pLDDT > 90: high confidence (expect < 1 Å RMSD from true structure)
    pLDDT 70-90: good confidence (most protein domains)
    pLDDT 50-70: low confidence (likely flexible region)
    pLDDT < 50: very low — predicted to be disordered (do not model as structure)

  These thresholds are guidelines; calibration varies by protein class.

  PAE (Predicted Aligned Error):
    [L × L] matrix: PAE[i,j] = expected position error of residue j
                                when residue i frame is aligned to truth
    Low PAE(i,j): confident about relative arrangement of i and j
    High PAE for distant domains: uncertain interdomain arrangement
    Used for: detecting domain boundaries, assessing multimer quality
```

---

## Section 2 — The AlphaFold Database

### Scale and Coverage

Released 2021 (v1), expanded 2022 (v4):

```
  ~200 million protein structures
  Covers:
    - Human proteome: ~20,000 proteins
    - UniProt: ~47 million proteins
    - Major model organisms
    - Predicted structures for proteins with no known homologs

  Average pLDDT across all structures:
    ~35% of residues: pLDDT < 50 (disordered)
    ~35% of residues: pLDDT 50-70 (low confidence)
    ~30% of residues: pLDDT > 70 (confident)

  Before AF2: ~180,000 structures in PDB (50 years of experimental work)
  After AF2: ~200,000,000 computed structures (released in 2 years)
  → 1000× more structures, but experimental validation still required
```

### What the Database Enables

```
  ┌────────────────────────────────────────────────────────────────────┐
  │  APPLICATION                  │  HOW DATABASE HELPS                │
  │  ───────────────────────────  │  ──────────────────────────────── │
  │  Structure-based drug design  │  Virtual screening against targets │
  │                               │  previously without structures     │
  │  Evolutionary analysis        │  Compare structures across kingdoms│
  │                               │  (functional divergence)           │
  │  Structural genomics          │  Find uncharacterized protein folds│
  │  Protein-protein docking      │  Starting structures for docking   │
  │  Molecular replacement in X-ray│ Use AF2 models as MR search models│
  │  Machine learning             │  Training data for downstream tasks│
  │  Function annotation          │  Map sequence → structure → function│
  │  Orphan drug targets          │  Get structure for "undruggable" targets│
  └────────────────────────────────────────────────────────────────────┘
```

---

## Section 3 — What AlphaFold2 Does NOT Solve

### Dynamics and Conformational Ensembles

AlphaFold2 predicts a single structure — the lowest-energy (most likely) conformation.
Many proteins function through multiple conformations:

```
  PROTEINS THAT AF2 HANDLES POORLY:

  1. Intrinsically disordered proteins (IDPs):
     ~30% of human proteome is predicted disordered (low pLDDT)
     IDPs don't have a fixed structure — they exist as dynamic ensembles
     p53 transcription factor: ~40% IDP
     c-Myc oncogene: ~90% IDP
     Many cancer-relevant targets are IDPs

  2. Conformational switchers:
     Kinases: active ↔ inactive conformation (DFG-in vs. DFG-out)
     GPCRs: multiple functional states (inactive/active/intermediate)
     AF2 gives one state; which state depends on evolutionary pressure in MSA

  3. Allosteric proteins:
     Structure changes upon binding of effector molecule
     AF2 gives apo structure only (unless ligand is in training set)
     Allosteric mechanisms are functionally critical but invisible

  4. Large flexible assemblies:
     Ribosomes: highly accurate for individual subunits
     Histone complexes: nucleosome wrapping geometry is dynamic
     IDP-containing complexes: FRET shows large-scale dynamics invisible to AF2
```

### Why Structure ≠ Function

```
  STRUCTURE → FUNCTION GAP:

  Knowing the structure does not tell you:
  ┌──────────────────────────────────────────────────────────────────┐
  │  What you need to know        │  Why structure doesn't tell you  │
  │  ───────────────────────────  │  ──────────────────────────────  │
  │  What ligands bind            │  Pocket shape is necessary but   │
  │                               │  not sufficient; also: charge,   │
  │                               │  desolvation, induced fit        │
  │  Enzymatic mechanism          │  Need: substrate, protonation    │
  │                               │  states, electrostatics, dynamics│
  │  Regulatory logic             │  PTMs, conformational switch,    │
  │                               │  interaction partners            │
  │  Cellular localization        │  Sequence signals not in struct  │
  │  Pathogenicity of mutations   │  Need: thermodynamics, kinetics  │
  │                               │  of folding change + function    │
  │  Drug efficacy                │  ΔG_binding → ΔΔG_binding (FEP) │
  │                               │  → in vitro potency → ADMET      │
  │                               │  → clinical efficacy: very long chain│
  └──────────────────────────────────────────────────────────────────┘
```

### Protein-Protein Interaction Prediction

AlphaFold-Multimer (Evans et al. 2022) extended AF2 to heterodimers and homooligomers:

```
  ALPHAFOLD-MULTIMER PERFORMANCE:
    Good: stable hetero-complexes with many evolutionary coevolving contacts
    Mediocre: transient interactions (insufficient MSA covariation signal)
    Poor: hub proteins with many different binding partners
    Poor: IDPs in complexes (no fixed interface geometry)

  Interface prediction accuracy (CASP15 protein-protein):
    ~40-50% of interfaces predicted correctly at < 5 Å RMSD
    (still a hard problem; much better than before AF2 but far from solved)

  RFAA (RoseTTAFold All-Atom, 2023):
    Extended to protein + small molecule + DNA/RNA
    Handles covalent modifications, cofactors
    Still limited for highly dynamic assemblies
```

---

## Section 4 — RoseTTAFold and ESMFold

### RoseTTAFold (Baker group, 2021)

A parallel development to AlphaFold2, with different architectural choices:

```
  THREE-TRACK ARCHITECTURE:

  1D track: residue-level features (sequence, MSA)
  2D track: pair-level features (distances, contacts)
  3D track: atomic coordinates (3D point cloud)

  Information flows in all directions:
    1D ↔ 2D ↔ 3D (bidirectional between tracks)

  Lower accuracy than AF2 on CASP14 benchmark
  BUT:
    Open-source earlier (full code immediately)
    Extended to RFdiffusion (protein design)
    Extended to RFdiffusion for protein-protein interactions
    Faster inference per model
```

### ESMFold (Meta, 2022)

A large language model approach — no MSA required:

```
  ARCHITECTURE:
    Large language model (ESM-2, 650M or 3B parameters) pre-trained
    on protein sequence database (language modeling on sequences)
    → sequence embeddings capture co-evolutionary information implicitly
    Structure prediction head: folding trunk (smaller than Evoformer)
    using ESM-2 embeddings as input

  KEY DIFFERENCE FROM AF2:
    No explicit MSA: embeddings derived from model parameters, not alignment
    → 60× faster inference (no MSA search bottleneck)
    → Works even for de novo sequences (no homologs needed)
    → Lower accuracy than AF2 for proteins with informative MSAs
    → Comparable accuracy for proteins without homologs (orphans)

  Published 690 million structures (more than AF2 for metagenomic proteins)
```

---

## Section 5 — What Comes Next: The Remaining Hard Problems

### De Novo Protein Design

AlphaFold enabled inverse folding at scale: design new sequences to fold into
desired structures. The key tools:

```
  RFdiffusion (2023):
    Diffusion model on protein backbone coordinates
    Generate novel backbone folds (not found in PDB) given design constraints
    Then: ProteinMPNN (sequence design conditioned on backbone)
    Then: AF2 for in silico verification
    Applications: binders to targets, enzymes, new topologies

  ProteinMPNN:
    Message-passing neural network for inverse folding
    Given backbone structure → predict sequences likely to fold to it
    Outperforms Rosetta-based methods in computational metrics
    Experimental validation rate: ~50-80% (fraction that fold as designed)

  This closes the design loop:
    Target function → Structure (RFdiffusion)
    → Sequences (ProteinMPNN) → Verify (AF2) → Synthesize → Test
```

### Drug Design: Why AF2 Is Not a Drug Discovery Machine

```
  STRUCTURE-BASED DRUG DESIGN PIPELINE:

  1. Protein structure                ← AF2 solves this (mostly)
         ↓
  2. Binding pocket identification     ← FPocket, SiteMap, computational
         ↓
  3. Virtual screening / docking       ← Glide, AutoDock, Vina
         ↓
  4. Predict binding affinity (ΔG)    ← FEP+, alchemical free energy
         ↓
  5. Synthesize & test in vitro        ← chemistry, assay development
         ↓
  6. Optimize potency/selectivity      ← SAR, medicinal chemistry
         ↓
  7. ADMET (absorption/distribution/   ← entirely separate models
     metabolism/excretion/toxicity)    ← usually kills candidates
         ↓
  8. In vivo efficacy                  ← animal models
         ↓
  9. Clinical trials

  AF2 is enormously useful at step 1.
  Steps 2-9 require different tools, different data, different biology.
  Success rate clinical → approval: ~10% even with good structure.
  AF2 alone does not change clinical success rates directly.
```

### AlphaFold3 (2024)

DeepMind released AlphaFold3 for joint prediction of protein, nucleic acid,
small molecule, and ion structures:

```
  ARCHITECTURE CHANGE:
    Replaced structure module (IPA) with diffusion model
    Input: any combination of protein / DNA / RNA / small molecule / ions
    Joint coordinate prediction → handles covalent ligands, crosslinks

  WHAT IMPROVED:
    Protein-protein interface accuracy (CASP15 PPI track)
    Protein-ligand docking (better than AutoDock Vina on many targets)
    Protein-nucleic acid complex structures
    Post-translational modifications (phospho, glycosyl, etc.)

  WHAT REMAINED HARD:
    Dynamics still absent
    IDPs still not handled (low pLDDT ≠ meaningful ensemble)
    Allosteric transitions: AF3 gives one state
    Large flexible assemblies still limited
```

---

## Section 6 — Connecting to the MIT TCS Background

### What AlphaFold2 Is (and Isn't) Computationally

From a theoretical CS perspective, AlphaFold2 made the following trade:

```
  BEFORE AF2:
    Structure prediction = NP-hard in the worst case (lattice HP model)
    Real proteins: no polynomial-time exact algorithm known
    Heuristic methods (Rosetta): fragment assembly + energy minimization
    Accuracy limited by energy function imprecision

  AF2'S INSIGHT:
    Does NOT solve the physics; instead, learns the mapping sequence → structure
    from the ~180,000 known structures in PDB
    The training data is a proxy for the physics
    MSA + attention encodes evolutionary constraints ≈ physical constraints
    Generalization beyond training: worked because the physics is universal

  THEORETICAL LIMIT:
    AF2 is an approximation learned from data.
    For proteins with no evolutionary relatives (de novo sequences, novel folds):
    AF2 performance degrades. ESMFold and RFdiffusion handle this regime better.
    The underlying optimization landscape (energy landscape) is not explicitly used.
```

### Attention Mechanism Over Sequences = Statistical Coevolution

The MSA attention in Evoformer is computing, at a high level:

```
  Mutual information between positions:
    I(i,j) = H(i) + H(j) - H(i,j)
    where H = Shannon entropy of residue distribution in the MSA

  Direct coupling analysis (DCA, pre-AF2):
    Explicitly extracted contacts from MI after removing transitive correlations
    Gaussian model: use inverse covariance matrix (Potts model)
    Predicted ~60% of contacts above random at L/5 precision

  AF2 Evoformer does this implicitly but better:
    Learned to extract direct couplings through attention weights
    Including structural context, template information, geometric constraints
    All jointly — not a pipeline but end-to-end learning
```

---

## Decision Cheat Sheet

| Question | Answer | Source |
|----------|--------|--------|
| What does AlphaFold2 take as input? | Amino acid sequence (builds MSA internally) | Section 1 |
| What key architectural innovation handles long-range contacts? | Triangular multiplicative updates in pair representation | Section 1 |
| What does pLDDT < 50 mean? | Predicted disordered; do not model as fixed structure | Section 1 |
| How many structures in the AF database? | ~200 million (v4, 2022) | Section 2 |
| Why can't AF2 predict drug binding? | No dynamics; no ligand-induced conformational change | Section 3 |
| What does ESMFold do differently from AF2? | No explicit MSA; uses LLM sequence embeddings | Section 4 |
| What does RFdiffusion do? | Generate novel backbone folds for protein design | Section 5 |
| What did AlphaFold3 add? | Protein + nucleic acid + small molecule joint prediction | Section 5 |

---

## Common Confusion Points

**AlphaFold2 is not MD simulation.** Molecular dynamics explicitly integrates
Newton's equations of motion and explores conformational space over time. AF2
predicts a single static structure. AF2 gives you the native fold; MD tells you
what happens when the protein jiggles, unfolds, or interacts with other molecules.

**High pLDDT does not mean high accuracy.** pLDDT is a predicted confidence score.
It correlates with accuracy on average but can be miscalibrated for novel folds,
proteins outside the training distribution, or very small proteins. Always validate
against experimental data (X-ray, cryo-EM, NMR, biochemistry) when possible.

**The 200M structure database is not a validated proteome.** AF2 structures have
not been experimentally determined. For most of these proteins, there is no
functional annotation, no experimental validation, and no knowledge of cellular
context. The database is a hypothesis repository — useful for hypothesis generation
but not a replacement for experiment.

**AlphaFold3 is not fully open.** Unlike AF2 (published with full code and weights),
AF3 was initially released as a server with restricted access and without full
model weights. This limits community use and validation. The open-source community
responded with Boltz-1 and Chai-1 as open alternatives.

**Structure prediction did not solve protein design.** Knowing the native fold
does not tell you the inverse: what sequence will fold to a desired structure.
That is the protein design problem, which requires RFdiffusion, ProteinMPNN, and
similar tools. AlphaFold2 is used as a final verification step in design pipelines,
not as the design engine itself.
