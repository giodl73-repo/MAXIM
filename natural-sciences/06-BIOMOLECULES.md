# 06-BIOMOLECULES — Biological Molecules

> Amino acids, proteins, nucleic acids, lipids, carbohydrates.
> Structure → function is the central theme: every molecular feature
> exists because it enables a specific biological role.

---

## The Four Classes — Quick Map

```
BIOMOLECULE     MONOMER           POLYMER              PRIMARY FUNCTION
──────────────────────────────────────────────────────────────────────────
Proteins        Amino acids (20)  Polypeptide → fold   Catalysis, structure,
                                                        signaling, transport
Nucleic acids   Nucleotides       DNA / RNA             Information storage,
                                                        transfer, catalysis
Lipids          Fatty acids +     Membrane bilayer,     Barrier, signaling,
                glycerol/sphingo  triglycerides         energy storage
Carbohydrates   Monosaccharides   Polysaccharides       Energy, structural,
                                                        cell recognition
```

---

## Amino Acids

### The 20 Standard Amino Acids

All share the same backbone. R-group determines identity and chemistry.

```
        H
        │
H₂N — C — COOH
        │
        R

At physiological pH (~7.4):
  −NH₂  →  −NH₃⁺  (pKa ~9–10)
  −COOH →  −COO⁻  (pKa ~2)
  Zwitterion: +H₃N−CHR−COO⁻
```

### Side-Chain Classification

```
NONPOLAR / HYDROPHOBIC (buried in protein core)
  Gly (G)  — H       (smallest, no chirality, helix breaker)
  Ala (A)  — CH₃
  Val (V)  — isopropyl     (β-branched — disfavors α-helix)
  Leu (L)  — isobutyl
  Ile (I)  — sec-butyl     (β-branched)
  Pro (P)  — cyclic to N   (rigid, helix breaker, found at turns)
  Phe (F)  — benzyl        (aromatic, π-stacking)
  Trp (W)  — indole        (largest, strong UV absorbance at 280 nm)
  Met (M)  — thioether

POLAR / UNCHARGED (surface or buried H-bonding)
  Ser (S)  — −CH₂OH       (phosphorylation site)
  Thr (T)  — −CH(OH)CH₃   (phosphorylation site, β-branched)
  Cys (C)  — −CH₂SH       (disulfide bonds, metal ligand, pKa 8.3)
  Tyr (Y)  — p-hydroxyphenyl  (phosphorylation site, pKa 10.1)
  Asn (N)  — −CH₂CONH₂   (N-glycosylation site)
  Gln (Q)  — −(CH₂)₂CONH₂

CHARGED (surface, ionic interactions, acid/base catalysis)
  Positive (+) at pH 7:
    Lys (K)  — −(CH₂)₄NH₃⁺   pKa 10.5
    Arg (R)  — guanidinium     pKa 12.5  (almost always +)
    His (H)  — imidazole       pKa 6.0   (near-neutral — key in catalysis)

  Negative (−) at pH 7:
    Asp (D)  — −CH₂COO⁻       pKa 3.7
    Glu (E)  — −(CH₂)₂COO⁻   pKa 4.3
```

### pKa and Ionization

```
Henderson-Hasselbalch:   pH = pKa + log([A⁻]/[HA])

At pH = pKa: 50% ionized
pH < pKa: protonated form dominates (acid form)
pH > pKa: deprotonated form dominates (base form)

Histidine (pKa 6.0) near physiological pH:
  → small pH shifts toggle protonation state
  → why His is the ubiquitous acid/base catalyst in enzyme active sites

Cysteine (pKa 8.3): mostly protonated at pH 7 but easily deprotonated
  → active-site Cys as nucleophile in cysteine proteases (papain, caspases)
```

### Chirality

All 20 standard amino acids are L-configuration (except Gly — no chiral center).
D-amino acids occur in bacterial cell walls (D-Ala in peptidoglycan) and some peptide antibiotics.
L vs D: same as (S) vs (R) for most, but Cys is opposite due to priority rules.

---

## Protein Structure

### Primary Structure

Amino acid sequence. Encoded by DNA. Written N→C terminus.
Peptide bond: −CO−NH− formed by condensation (loss of H₂O). Planar due to partial double-bond character (resonance). ω (omega) dihedral angle ≈ 180° (trans) for almost all residues.

```
       O    R₂    O
       ‖    │     ‖
─N─C─C─N─C─C─N─C─
 │  │  ─H  │     │
 H  R₁     H     R₃

Dihedral angles:
  φ (phi):  N−Cα bond rotation
  ψ (psi):  Cα−C bond rotation
  ω (omega): C−N bond (≈180°, planar)
```

### Ramachandran Plot

Maps allowed (φ, ψ) combinations. Most space is forbidden (steric clash).

```
        ψ
   180° ┤
        │  ██        ██
        │  ██        ██   ← β-sheet region
        │             ██
     0° ┤
        │
        │    ██           ← α-helix region
  −180° ┤
        └──────────────── φ
       −180°    0°    180°

Allowed regions: α-helix (φ≈−57°, ψ≈−47°), β-sheet (φ≈−120°, ψ≈+120°)
Gly: allowed everywhere (no R-group)
Pro: restricted (cyclic side chain limits φ ≈ −60°)
```

### Secondary Structure

Local regular structures stabilized by backbone H-bonds (NH···O=C).

**α-Helix:**
```
  3.6 residues/turn,  rise = 1.5 Å/residue,  pitch = 5.4 Å/turn
  H-bond: residue i to residue i+4
  Side chains point outward
  Dipole moment along helix axis (N-terminus positive end)
  Breakers: Pro (kink), Gly (too flexible), β-branched (Val, Ile, Thr — steric)
```

**β-Sheet:**
```
  Parallel: both chains run N→C same direction
    H-bonds slightly weaker, less stable
  Antiparallel: chains run in opposite directions
    H-bonds more linear, stronger, more stable
  Twisted sheet: right-handed twist (~15°/strand) — thermodynamically preferred
  β-barrel: antiparallel sheet rolled into cylinder (porin channels, TonB)
```

**Turns and Loops:**
- β-turns: reverse direction of chain (i→i+3 H-bond, various types)
- Loops: irregular — often on protein surface, frequently involved in binding

### Tertiary Structure

Complete 3D fold of one polypeptide chain.

```
Driving forces for folding:
  1. Hydrophobic effect (dominant)
     Nonpolar residues avoid water → bury in core → reduces ordered water shell
     ΔG_fold < 0 because ΔS_water > |ΔS_chain|

  2. H-bonds (secondary structure, polar side-chain interactions)
     Contribute enthalpy BUT unfolded chain also H-bonds with water
     Net ΔH_H-bond is small

  3. Disulfide bonds (Cys−S−S−Cys)
     Covalent cross-links, formed in ER (oxidizing environment)
     Stabilize extracellular and secreted proteins

  4. Salt bridges (Lys/Arg···Asp/Glu)
     Electrostatic, ~1–3 kcal/mol each
     Can be destabilized at extreme pH

  5. Van der Waals (packing in hydrophobic core)
     Small individually, large cumulatively (many contacts)
```

**Protein folding problem**: sequence → structure mapping. Levinthal's paradox:
random search of all conformations would take >universe lifetime; real folding ~ms–s.
Solution: folding funnel — energy landscape guides to native state.
AlphaFold2 (2020) achieves near-experimental accuracy for single-chain proteins.

### Quaternary Structure

Multiple polypeptide chains (subunits) assembled into functional complex.

```
Homodimer:    two identical chains (many transcription factors)
Heterodimer:  two different chains (receptor + ligand binding)
Homotetramer: hemoglobin-like (4 subunits)
Hemoglobin:   α₂β₂ heterotetramer — allosteric cooperativity (see 07-ENZYMES.md)

Advantages of quaternary structure:
  → Allosteric regulation across subunit interfaces
  → Economies of genetic encoding (one gene, multiple copies)
  → Structural stability (buried interfaces)
```

---

## Nucleic Acids

### Nucleotide Structure

```
Nucleotide = nitrogenous base + sugar + 1–3 phosphate groups

Bases:
  Purines (two rings):    Adenine (A), Guanine (G)
  Pyrimidines (one ring): Cytosine (C), Thymine (T — DNA only),
                           Uracil (U — RNA only)

Sugar:
  DNA: 2'-deoxyribose (no OH at 2' carbon)
  RNA: ribose (OH at 2' carbon)

Phosphodiester backbone:
  3'-OH of one nucleotide + 5'-phosphate of next → phosphodiester bond
  Chain direction: 5' → 3'
  Charge: −1 per phosphate at pH 7 → DNA/RNA are polyanions
```

### DNA Double Helix (Watson-Crick, B-form)

```
  5'─ phosphate ─ sugar ─ Base ┐
                         Base ─┤── H-bonds
  3'─ phosphate ─ sugar ─ Base ┘

Base pairing (antiparallel strands):
  A = T   (2 H-bonds)
  G ≡ C   (3 H-bonds)   ← GC content ↑ → higher melting temperature Tm

B-DNA geometry:
  Right-handed helix, 10.5 bp/turn, rise = 3.4 Å/bp, diameter = 20 Å
  Major groove: wider, more H-bond donors/acceptors → protein binding site
  Minor groove: narrower, less accessible

A-DNA: right-handed, 11 bp/turn, wider/shorter — RNA:DNA hybrids, dry DNA
Z-DNA: left-handed, 12 bp/turn — GC-rich sequences, potential regulatory role

Melting temperature:
  Tm ≈ 81.5 + 16.6·log[Na⁺] + 0.41·(%GC) − 675/N
  GC-rich DNA melts at higher T (3 H-bonds vs 2 for AT)
```

### RNA Structure and Types

RNA is single-stranded but folds on itself:

```
Type         Function
──────────────────────────────────────────────────────────────
mRNA         messenger — carries coding sequence from DNA to ribosome
tRNA         transfer — adaptor, carries amino acid, reads codon (~76 nt, cloverleaf)
rRNA         ribosomal — structural + catalytic core of ribosome (16S, 23S in bacteria)
snRNA        small nuclear — splicing (U1, U2, U4, U5, U6 in spliceosome)
miRNA        micro RNA — ~22 nt, gene regulation via mRNA degradation/repression
siRNA        small interfering — exogenous (RNAi pathway), gene silencing
lncRNA       long noncoding — chromatin regulation, scaffolding
ribozyme     catalytic RNA — self-splicing introns, peptidyl transferase (rRNA)
```

---

## Lipids

### Fatty Acids

Long hydrocarbon chains with terminal carboxylic acid.

```
Saturated: no double bonds — straight chain, pack tightly, solid at RT
  Palmitic acid: CH₃(CH₂)₁₄COOH   (C16:0)
  Stearic acid:  CH₃(CH₂)₁₆COOH   (C18:0)

Unsaturated: one or more C=C double bonds — kinked, fluid at RT
  Oleic acid:    C18:1 (Δ9, cis)   monounsaturated — olive oil
  Linoleic:      C18:2 (Δ9,12)     polyunsaturated — essential (ω-6)
  α-Linolenic:   C18:3 (Δ9,12,15)  polyunsaturated — essential (ω-3)

Nomenclature:
  C18:2 Δ9,12  = 18 carbons, 2 double bonds at C9 and C12
  ω-6: last double bond 6 carbons from methyl end
  cis double bonds: kinked chain, lower packing → lower melting point
  trans double bonds: straight (like saturated), higher melting point
```

### Membrane Lipids

```
Phosphatidylcholine (PC):
  glycerol backbone
  + 2 fatty acid chains (esterified at sn-1 and sn-2)
  + phosphate + choline (at sn-3)

Amphiphilic structure → self-assembly into bilayer:
  ┌────────────────────────────────┐
  │ ●●●●●●●●●●●●●●●●●●●●●●●●●●●●   │
  │ |||||||||||||||||||||||||||||| │
  │ |||||||||||||||||||||||||||||| │
  │ ●●●●●●●●●●●●●●●●●●●●●●●●●●●●   │
  └────────────────────────────────┘
    Top and bottom rows of "●": polar heads (outward, face water).
    Two middle rows of "|":     nonpolar tails (inward, face each other).

Bilayer thickness: ~4 nm
Lateral diffusion: fast (μm²/s); flip-flop: slow (hours, requires flippase)

Cholesterol:
  Rigid sterol ring intercalates between fatty acid chains
  Moderates fluidity: prevents crystallization at low T, reduces fluidity at high T
  → "fluidity buffer"
  Eukaryotes only. 30–40% of plasma membrane lipids.

Sphingomyelin: sphingosine backbone (not glycerol); in lipid rafts with cholesterol
Cardiolipin: two phosphatidyl groups + glycerol; inner mitochondrial membrane; crucial for ETC
```

---

## Carbohydrates

### Monosaccharides

```
General formula: (CH₂O)n,  most common n = 3–7

Trioses:   glyceraldehyde (C3) — glycolysis intermediate
Pentoses:  ribose/deoxyribose (C5) — nucleic acid backbone
Hexoses:   glucose, fructose, galactose (C6) — primary energy source

Glucose ring (pyranose form):
  Open chain ⇌ ring (hemiacetal between C1 and C5)
  α-D-glucose: −OH at C1 axial (below ring in Haworth)
  β-D-glucose: −OH at C1 equatorial (above ring in Haworth) → more stable

Anomers: α and β differ only at C1 (anomeric carbon)
Mutarotation: α ⇌ β equilibration in solution (α:β ≈ 36:64 at equilibrium)
```

### Glycosidic Bonds and Disaccharides

```
Bond between anomeric C1 of one sugar and OH of another; loss of H₂O.

α(1→4) bond: starch (amylose) — helical, digestible
β(1→4) bond: cellulose — straight, parallel chains, H-bonded, structural (not digestible by most)
α(1→2) bond: sucrose (glucose+fructose) — nonreducing (both anomeric C's locked)
β(1→4) bond: lactose (galactose+glucose) — reducing (free C1 on glucose)
α(1→6) branch: glycogen/amylopectin branching

Reducing sugar: free anomeric OH present — reacts with oxidizing agents (Benedict's test)
Nonreducing: anomeric OH locked in glycosidic bond (sucrose, trehalose)
```

### Polysaccharides

```
Starch (amylose + amylopectin):  energy storage in plants
  Amylose:     α(1→4) linear → helical → binds iodine (blue-black color)
  Amylopectin: α(1→4) with α(1→6) branches every ~25 residues

Glycogen: animal energy storage (liver, muscle)
  Like amylopectin but more branched (every ~10 residues)
  More branch ends → faster mobilization (more phosphorylase access points)

Cellulose: plant structural (most abundant organic polymer on Earth)
  β(1→4) glucose → fully extended chains → H-bond between parallel chains
  → microfibril bundles → high tensile strength

Chitin: β(1→4) N-acetylglucosamine — arthropod exoskeleton, fungal cell wall
Peptidoglycan: bacterial cell wall — β(1→4) linked alternating NAG-NAM, cross-linked by peptides
  → target of lysozyme (cleaves β(1→4) bond), β-lactam antibiotics
```

---

## Decision Cheat Sheet

| Question | Concept | Answer |
|----------|---------|--------|
| Why is His the key catalytic residue? | pKa near pH 7 | Can donate or accept protons at physiological pH |
| Why do proteins fold hydrophobic core inward? | Hydrophobic effect | Burying nonpolar residues releases ordered water → ΔS > 0 |
| Why does more GC content raise DNA melting temp? | H-bond count | G≡C has 3 H-bonds vs A=T with 2 |
| Why is saturated fat solid at room temp? | Fatty acid packing | No kinks → tight van der Waals packing → higher Tm |
| Why can't humans digest cellulose? | Glycosidic bond specificity | β(1→4) linkage requires β-glucosidase; humans lack it |
| Why are disulfide bonds rare in cytoplasm? | Redox environment | Cytoplasm is reducing (GSH); ER is oxidizing |
| What distinguishes DNA from RNA structurally? | 2'-OH and base | DNA: 2'-H, thymine; RNA: 2'-OH, uracil |
| Why is the major groove preferred for protein binding? | Groove geometry | Wider with more H-bond donor/acceptor patterns |
| Why does cholesterol "buffer" membrane fluidity? | Rigid ring intercalation | Prevents both crystallization (low T) and excess fluidity (high T) |
| Why is Gly found at helix-breaking positions? | No R-group → φ,ψ unrestricted | Too flexible to maintain regular helix geometry |

---

## Common Confusion Points

**Primary structure determines 3D structure (Anfinsen's dogma)**
Under the right conditions, a protein will spontaneously fold to its native state
from its amino acid sequence alone. This was proven by denaturation/renaturation
of ribonuclease A. However: prions, amyloids, and chaperone-dependent folding are
exceptions where the folding pathway or environment matters.

**Hydrogen bonds are not unique to proteins and DNA**
Water itself is held together by H-bonds. The H-bond network in liquid water is
why many of water's properties are anomalous (high bp, surface tension, ice density).
Protein/DNA H-bonds are special only in that they're geometrically constrained
and cooperate with other forces to define specific structures.

**α vs β glucose has large biological consequences**
Starch (α-glucose) is digestible; cellulose (β-glucose) is not.
A single configuration difference at C1 changes the bond angle enough that
different enzyme active sites are required. This is a striking example of
how molecular geometry determines macroscopic biological function.

**RNA can be catalytic (ribozymes)**
The "central dogma" implies DNA → RNA → protein, with RNA as passive messenger.
But ribosomal RNA performs peptidyl transfer (it IS the catalyst in the ribosome,
proteins are structural scaffolding). Self-splicing introns, RNase P, and HDV
ribozyme are other examples. The RNA world hypothesis: RNA predated proteins
as both information carrier and catalyst.

**Lipid bilayers are dynamic, not static**
"Fluid mosaic model" (Singer-Nicolson, 1972): proteins float in a 2D lipid fluid.
Individual lipids exchange neighbors ~10⁷/s (lateral diffusion), but flip-flop
(transleaflet) is slow without flippases. Lipid rafts — cholesterol/sphingomyelin
microdomains — are a more recent refinement, controversial in detail.
