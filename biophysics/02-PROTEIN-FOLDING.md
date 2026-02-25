# Protein Folding — Energy Landscapes, Chaperones, and the AlphaFold Boundary

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│                   PROTEIN FOLDING LANDSCAPE                               │
│                                                                            │
│  SEQUENCE → STRUCTURE → FUNCTION                                          │
│  (1D)        (3D)         (activity)                                      │
│                                                                            │
│  THE FOLDING PROBLEM (three distinct questions):                           │
│  ─────────────────────────────────────────────                            │
│  1. Prediction: Given sequence, what is the 3D structure?  ← AlphaFold2  │
│  2. Mechanism: How does folding happen in time?             ← energy funnels│
│  3. Design: Given desired function, what sequence folds to it? ← RFdiffusion│
│                                                                            │
│  LEVINTHAL'S PARADOX                                                       │
│  ──────────────────                                                        │
│  100-residue protein: 3¹⁰⁰ ≈ 10⁴⁸ conformations                          │
│  At 1 ns/conformation: 10³⁹ years to search exhaustively                  │
│  Actual folding time: microseconds to seconds                              │
│  Resolution: proteins do NOT do exhaustive search — they fold via          │
│  energy funnels, biasing toward lower-energy conformations                 │
│                                                                            │
│  MISFOLDING DISEASES                                                       │
│  ──────────────────                                                        │
│  Alzheimer's:  Aβ, tau fibrillization                                     │
│  Parkinson's:  α-synuclein aggregation                                    │
│  Prion:        PrPᶜ → PrPˢᶜ conversion                                   │
│  Type II DM:   IAPP (islet amyloid polypeptide)                           │
│  Huntington's: polyglutamine expansion → aggregation                      │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — Levinthal's Paradox and Its Resolution

### The Paradox

Cyrus Levinthal (1969) pointed out that exhaustive conformational search is impossible:

```
  100-residue protein:
    Each residue: ~3 backbone states (φ,ψ rotamers)
    Total conformations: 3¹⁰⁰ ≈ 5 × 10⁴⁷

  If each conformation sampled in 10⁻⁹ s (nanosecond timescale):
    Time required: 5 × 10⁴⁷ × 10⁻⁹ s = 5 × 10³⁸ s ≈ 10³¹ years

  Age of universe: ~4 × 10¹⁷ s

  → Exhaustive random search is physically impossible
  → Proteins must be guided to the native state by the energy landscape
```

### The Resolution: Energy Funnels

The landscape is not flat. The native state sits at an energy minimum, and the
landscape is funnel-shaped, systematically biasing the chain toward lower energy
as it forms correct contacts:

```
  ROUGH LANDSCAPE (old view):        FUNNEL LANDSCAPE (correct):

  E   ___   ___   ___              E  |||||||||||||||||||  ← unfolded ensemble
      | | | | | | | |               |  \|||||||||||||||/
      ___| |___| |___               |   \|||||||||||||/
                                    |    \|||||||||||/
  Random walk with many traps       |     \|||||||||/
  → exponentially slow              |      \|||||||/
                                    |       \|||||/
                                    |        \|||/
                                    |         \|/
                                    |          ●   ← native state (global minimum)
```

**Key insight**: the funnel has a global minimum (native state) but a rough
landscape with local minima (kinetic traps). The folding trajectory is not random —
each productive contact lowers the free energy, pruning the conformational space.

---

## Section 2 — Energy Landscape Theory

### The Free Energy Landscape

The conformational free energy G(q) is a function of collective coordinates q
(e.g., fraction of native contacts Q, radius of gyration Rg):

```
  G(Q) landscape for a two-state folder:

      G
      │
      │  ┌─────┐
      │  │     │         ← unfolded basin: high entropy, high energy
      │  │     │   ┌──┐
      │  │     └───┘  │  ← transition state: narrow bottleneck
      │  │             │
      │  │             └────  ← folded basin: low entropy, low energy
      │
      └────────────────── Q (native contacts, 0 to 1)

  ΔG‡ = activation free energy (determines folding rate)
  ΔG_fold = stability (determines folded fraction at equilibrium)
```

These are independently tunable. A protein can be:
- Thermodynamically stable (ΔG_fold large) but kinetically slow (ΔG‡ large)
- Kinetically fast (ΔG‡ small) but marginally stable (ΔG_fold small)
- Both fast and stable (evolved proteins optimize this)

### Two-State vs. Multi-State Folding

**Two-state folders**: small proteins (< ~100 residues), single domain, fold without
populated intermediates. Rate depends only on ΔG‡.

**Multi-state folders**: larger proteins, populated intermediates. Rate depends on
the landscape topology between states.

```
  Diagnostics:
  - Two-state: van't Hoff ΔH = calorimetric ΔH  (DSC test)
  - Two-state: m-value proportional to expected buried surface area
  - Multi-state: urea/GDnHCl denaturation curves are not single sigmoidal
  - Multi-state: transient intermediates visible in stopped-flow kinetics
```

### Folding Rates: Kramers Theory and Phi-Values

Rate of crossing a free energy barrier (Kramers theory, overdamped limit):

```
  k_fold = A × exp(-ΔG‡ / k_BT)

  where A = attempt frequency ≈ 10⁶-10⁸ s⁻¹ (relates to reconfiguration time)

  ΔG‡ depends on topology (contact order):
  - High contact order (long-range contacts) → slow folding
  - Low contact order (local contacts, α-helices) → fast folding

  Contact order CO = (1/NL) Σᵢⱼ |i-j|  (N = residues, L = contacts)
  Correlation: log(k_fold) anti-correlates with CO across many proteins
```

**Phi-values** (Alan Fersht): mutation at residue i changes ΔG_fold and ΔG‡.
Φᵢ = ΔΔΔG‡ / ΔΔG_fold measures whether residue i's contacts are formed in the
transition state (Φ ≈ 1) or not yet (Φ ≈ 0). Maps the folding transition state
without needing an actual structure of the TS.

---

## Section 3 — Chaperones

### Why Chaperones?

The cell is crowded: ~300 g/L protein. Unfolded and partially folded chains expose
hydrophobic surfaces that tend to aggregate with other chains. Chaperones suppress
off-pathway aggregation and enable productive folding:

```
  WITHOUT CHAPERONES:                 WITH CHAPERONES:

  Newly synthesized chain             Chain binds chaperone
       ↓                                   ↓
  Exposes hydrophobic patches         Hydrophobic patches shielded
       ↓                                   ↓
  Aggregates with other chains        Released sequentially
       ↓                                   ↓
  Insoluble aggregate                 Productive folding
```

### Major Chaperone Classes

```
┌──────────────────────────────────────────────────────────────────────────┐
│  CHAPERONE     │  SUBSTRATE           │  MECHANISM                        │
│  ──────────────│──────────────────────│─────────────────────────────────  │
│  Hsp70 (DnaK)  │  Unfolded/extended   │  Binds exposed hydrophobic       │
│  + Hsp40 (DnaJ)│  peptides, ~7 aa     │  stretches. ATP-driven release.  │
│                │                      │  Co-chaperone DnaJ loads clients. │
│  ──────────────│──────────────────────│─────────────────────────────────  │
│  GroEL/GroES   │  Misfolded, sticky,  │  Barrel chamber: encapsulates     │
│  (Hsp60/Hsp10) │  ~20-60 kDa          │  single protein. ATP-driven lid   │
│                │                      │  (GroES) closes → forced unfolding│
│                │                      │  and refolding in isolation.       │
│  ──────────────│──────────────────────│─────────────────────────────────  │
│  Hsp90         │  Signaling proteins, │  Stabilizes near-native states.   │
│                │  kinases, nuclear    │  Regulatory: many co-chaperones.  │
│                │  receptors           │  ATP-dependent conformational      │
│                │                      │  clamp mechanism.                  │
│  ──────────────│──────────────────────│─────────────────────────────────  │
│  TRiC/CCT      │  Actin, tubulin,     │  Eukaryotic GroEL analog.         │
│                │  WD40 domains        │  8 subunits, different pockets    │
└──────────────────────────────────────────────────────────────────────────┘
```

**GroEL/GroES mechanism** (the "Anfinsen cage"):

```
  Step 1: Misfolded/aggregation-prone protein binds GroEL ring
  Step 2: ATP + GroES bind → lid closes → protein encapsulated
  Step 3: Inside cavity: hydrophilic walls, protein diluted to 1 molecule
  Step 4: Protein refolds in isolation (~10 s)
  Step 5: ATP hydrolysis → GroES dissociates → protein released
  Step 6: If still misfolded → rebind and retry (multiple cycles possible)

  Key insight: GroEL doesn't fold the protein — it prevents aggregation
  and provides an isolated environment where the protein can fold on its own.
```

---

## Section 4 — Misfolding Diseases

### Amyloid: The Misfolded Alternative

Many proteins can misfold into amyloid fibrils: cross-β-sheet structures where
β-strands run perpendicular to the fibril axis:

```
  NATIVE FOLD:              AMYLOID FIBRIL:

  Globular, soluble          Long, insoluble fiber
  Unique 3D structure        Universal cross-β architecture
  Functional                 Toxic (especially oligomers)
  Specific sequence          Any sequence can in principle form amyloid
  ~1-100 nm                  μm-mm length

  Cross-β structure:
  ─── β-strand ───          Strands perpendicular to fiber axis
  ─── β-strand ───          H-bonds parallel to fiber axis
  ─── β-strand ───          Spacing: 4.7 Å along fiber (H-bond spacing)
                             Spacing: 10-11 Å across fiber (side chains)
```

The amyloid state is often thermodynamically more stable than the native fold.
The native state is kinetically trapped by the energy barrier of nucleation.

### Disease Mechanisms

**Alzheimer's disease:**
- Amyloid β (Aβ40/Aβ42): cleavage product of APP
- Aβ42 aggregates faster, forms plaques
- Tau: microtubule-associated protein, hyperphosphorylation → NFT
- Current hypothesis: soluble oligomers are the toxic species, not mature plaques

**Parkinson's disease:**
- α-synuclein: small presynaptic protein, function uncertain
- SNCA mutations accelerate aggregation
- Lewy bodies: inclusions of α-synuclein fibrils in dopaminergic neurons
- Spreads cell-to-cell in "prion-like" fashion

**Prion diseases (CJD, BSE, scrapie):**
- Uniquely: the amyloid form (PrPˢᶜ) catalyzes conversion of native form (PrPᶜ)
- Templated misfolding: PrPˢᶜ + PrPᶜ → 2 PrPˢᶜ
- Exponential amplification → fatal neurodegeneration
- Transmissible: the misfolded protein IS the infectious agent (Prusiner, Nobel 1997)

```
  Prion conversion mechanism:

  PrPᶜ (cellular, normal)      PrPˢᶜ (scrapie, pathogenic)
  α-helix rich                  β-sheet rich
  Soluble                       Insoluble aggregate
  Degradable by proteases       Protease-resistant

  PrPˢᶜ + PrPᶜ  →  PrPˢᶜ + PrPˢᶜ  (templated conversion)

  This is the ONLY known case of protein-based inheritance
  (information transfer without nucleic acid)
```

---

## Section 5 — AlphaFold: What It Solved and What It Didn't

### What AlphaFold2 Actually Solved

Structure prediction: given amino acid sequence, predict 3D coordinates of all
atoms with ~Å accuracy for most structured proteins.

**Before AlphaFold2 (CASP13, 2018):** median TM-score ≈ 0.5 (rough fold guess)
**After AlphaFold2 (CASP14, 2020):** median TM-score ≈ 0.9 (near-experimental quality)

This ended the "protein structure prediction problem" as stated for 50+ years.

### What AlphaFold2 Does NOT Solve

```
┌──────────────────────────────────────────────────────────────────────────┐
│  SOLVED BY ALPHAFOLD2           │  NOT SOLVED                            │
│  ──────────────────────────────│────────────────────────────────────── │
│  Single-chain structure         │  Protein dynamics / conformational     │
│  Accurate backbone + sidechain  │    ensemble (only one state predicted) │
│  Most structured proteins       │  Intrinsically disordered proteins     │
│  Homology-template-free         │  Large protein complexes (progress     │
│  ~200M structures in database   │    with AlphaFold-Multimer, partial)  │
│                                 │  Protein-small molecule interactions   │
│                                 │  Protein-nucleic acid interactions     │
│                                 │  Effect of mutations on stability      │
│                                 │  Structure in membrane environment     │
│                                 │  Function prediction                   │
│                                 │  Drug design (indirect only)           │
└──────────────────────────────────────────────────────────────────────────┘
```

**Structure ≠ Function.** Knowing the fold does not tell you:
- What ligands bind (requires binding site identification, docking, experimental validation)
- How the protein is regulated (conformational changes, PTMs)
- What the protein does in the cell (requires genetics, cell biology)
- Whether a mutation is pathogenic (requires functional assays)

AlphaFold2 gives the static, ground-state structure of the dominant conformation.
Many proteins function through their dynamics, alternative conformations, or
intrinsically disordered regions — all invisible to AlphaFold2.

More detail on the AlphaFold architecture and what followed → see 09-ALPHAFOLD-ERA.md.

---

## Section 6 — Protein Folding In Vivo vs. In Vitro

### Cotranslational Folding

In the cell, proteins fold while being synthesized — the N-terminal domain is
released from the ribosome before the C-terminal domain is even synthesized:

```
  IN VITRO (test tube):              IN VIVO (cell):

  Full sequence available             N-terminus exits ribosome first
  Concentration effects               Surrounded by chaperones
  No vectorial synthesis              Cotranslational folding
  Pure protein                        Crowded environment (300 g/L)
  Folding from fully denatured        Folding from extended, never denatured
  Can study equilibrium               Always non-equilibrium

  Consequence: kinetic intermediates are different in vivo vs. in vitro.
  Some proteins that aggregate in vitro fold perfectly in vivo.
```

Ribosome-associated chaperones (RAC, NAC, Trigger Factor) interact with the
emerging chain and begin folding before synthesis completes.

### Protein Quality Control

```
  Folding quality control cascade:

  Newly synthesized protein
       │
       ↓
  Ribosome-associated chaperones (Trigger Factor / RAC)
       │
       ↓ if misfolded
  Hsp70/Hsp40 cycle (multiple rounds)
       │
       ↓ if still misfolded
  GroEL/GroES (bacteria) or TRiC/CCT (eukaryotes)
       │
       ↓ if still misfolded
  Hsp90 (for specific client proteins)
       │
       ↓ if irreversibly misfolded
  Ubiquitin-proteasome system (UPS) → degradation
  OR
  Aggresomes → autophagy → lysosomes
```

---

## Decision Cheat Sheet

| Question | Answer | Module |
|----------|--------|--------|
| Why does protein folding not take astronomical time? | Energy funnel, not random search | Section 2 |
| What determines folding rate (kinetics)? | ΔG‡, contact order | Section 2 |
| What determines folded fraction (equilibrium)? | ΔG_fold | Section 2 |
| What chaperone encapsulates individual proteins? | GroEL/GroES | Section 3 |
| What is the unique feature of prion disease? | PrPˢᶜ catalyzes conversion of PrPᶜ | Section 4 |
| Is amyloid thermodynamically stable? | Yes — kinetically trapped native state | Section 4 |
| What did AlphaFold2 definitively solve? | Static structure of single-chain proteins | Section 5 |
| What can't AlphaFold2 predict? | Dynamics, disorder, function, drug binding | Section 5 |

---

## Common Confusion Points

**Chaperones do not provide information.** Chaperones prevent aggregation and
provide opportunities for folding. They do not "teach" the protein how to fold or
add energy to direct the folding pathway. The structural information is in the
sequence — Anfinsen's thermodynamic hypothesis is still correct.

**ΔG‡ and ΔG_fold are independent.** A protein can be thermodynamically stable
(large ΔG_fold) but fold slowly (large ΔG‡). Kinetics and thermodynamics are
decoupled in protein folding. Many in vitro refolding experiments are limited by
kinetics, not equilibrium stability.

**Amyloid oligomers, not fibrils, are the toxic species.** In Alzheimer's and
Parkinson's, the mature fibrils visible as plaques/Lewy bodies may actually be
protective (sequestration of toxic species). The soluble oligomers — formed
transiently during nucleation — are the likely toxic agents. This distinction
completely changes the therapeutic target.

**AlphaFold2 did not "solve protein folding."** It solved structure prediction —
one of three protein folding problems. The mechanism problem (how folding happens
kinetically) and the design problem (what sequence gives desired function) remain
active research areas. The structure database explosion will feed advances in
both, but they require fundamentally different approaches.

**IDPs (intrinsically disordered proteins) are not misfolded.** IDPs lack a stable
tertiary structure by design. They carry out functions requiring flexibility: linkers,
signaling hubs, transcription factors. They are not "failed folders." AlphaFold2's
low pLDDT score in predicted IDP regions correctly indicates genuine disorder —
this is diagnostic information, not failure.
