# Cell Biology — Membranes, Organelles, Signaling, Cell Cycle

---

## Big Picture

```
THE CELL AS A SYSTEM:

 PLASMA MEMBRANE (boundary + communication)
        │
        ├─ Lipid bilayer: selective permeability
        ├─ Receptors: detect extracellular signals
        └─ Transporters: ion channels, pumps, carriers

 INSIDE THE CELL:
        │
        ├─ NUCLEUS: genome storage, transcription
        ├─ ER (endoplasmic reticulum): protein/lipid synthesis
        ├─ GOLGI: protein processing/sorting
        ├─ MITOCHONDRIA: ATP production
        ├─ LYSOSOMES: degradation
        ├─ CYTOSKELETON: structure, transport, movement
        └─ RIBOSOMES: translation (free + ER-bound)

 CELL CYCLE: replicate DNA → segregate chromosomes → divide
```

---

<!-- @editor[bridge/P2]: No old-world bridge — natural parallel: cell membrane = firewall + API gateway, vesicle trafficking = message routing, cell cycle checkpoints = CI/CD quality gates -->

## Cell Membrane

### Lipid Bilayer

```
PHOSPHOLIPID STRUCTURE:
  Hydrophilic head (phosphate + glycerol + choline/serine/etc.)
  Two hydrophobic fatty acid tails (14-24 carbons)
  Amphipathic: spontaneously forms bilayer in aqueous environment

BILAYER PROPERTIES:
  Thickness: ~5-8 nm
  Fluid mosaic model (Singer-Nicolson 1972): lipids + proteins in fluid 2D
  Lateral diffusion: ~2 μm²/s → lipid crosses cell in ~30 s
  Flip-flop: extremely rare (1/month); flippases actively flip for asymmetry

MEMBRANE COMPOSITION:
  OUTER LEAFLET: PC (phosphatidylcholine), SM (sphingomyelin)
                 Glycolipids, cholesterol (asymmetric)
  INNER LEAFLET: PE (phosphatidylethanolamine), PS (phosphatidylserine, negative charge)
                 PI (phosphatidylinositol): signaling reservoir (PIP₂ → DAG + IP₃)

CHOLESTEROL (~30% of mammalian membrane lipids):
  Intercalates between lipids → reduces fluidity → reduces permeability
  Increases membrane order
  Concentrated in lipid rafts (DRM: detergent-resistant membranes)

LIPID RAFTS (controversial):
  Proposed: ordered microdomains enriched in cholesterol + sphingomyelin + GPI-anchored proteins
  May concentrate signaling molecules (Src kinases, GPI proteins)
  Size: ~10-200 nm (below optical resolution — hence controversy)
```

### Membrane Transport

```
PASSIVE TRANSPORT (down concentration gradient, no energy):
  Simple diffusion: O₂, CO₂, small hydrophobic molecules
  Channel-mediated: ion channels (aquaporins for water, Na⁺/K⁺/Cl⁻/Ca²⁺ channels)
    Selectivity filter: molecular sieving
    Gating: voltage-gated, ligand-gated, mechanically gated
  Facilitated diffusion: glucose transporters (GLUTs), Na⁺-dependent amino acid transporters

ACTIVE TRANSPORT (against gradient, requires energy):
  Primary: uses ATP directly
    Na⁺/K⁺-ATPase: 3 Na⁺ out, 2 K⁺ in, per ATP → maintains electrochemical gradients
    Ca²⁺-ATPase (SERCA): pumps Ca²⁺ into SR/ER
    ABC transporters: P-glycoprotein (MDR1) exports drugs out → multidrug resistance!

  Secondary: uses electrochemical gradient (built by primary)
    Na⁺-glucose cotransporter (SGLT): Na⁺ flows in, glucose piggybacked
    Na⁺/H⁺ exchanger: maintains intracellular pH
    Ca²⁺/Na⁺ exchanger: 3 Na⁺ in → 1 Ca²⁺ out (uses Na⁺ gradient from Na⁺/K⁺ ATPase)
```

---

## Organelles

### Endomembrane System

```
ENDOPLASMIC RETICULUM (ER):
  ROUGH ER: ribosome-studded → synthesizes secretory/membrane proteins
    Signal peptide (N-terminal hydrophobic): directs ribosome to ER membrane
    Co-translational translocation: signal recognition particle (SRP) → translocon
    N-linked glycosylation in ER lumen: GlcNAc₂Man₉Glc₃ added to Asn-X-Ser/Thr
    Protein quality control: calnexin/calreticulin (lectins) → retain unfolded
    ER-associated degradation (ERAD): send misfolded → retrotranslocate → proteasome
    UPR (unfolded protein response): activated by ER stress → PERK, ATF6, IRE1

  SMOOTH ER: lipid synthesis, steroid metabolism, Ca²⁺ storage (SR in muscle)
    Liver: drug/toxin metabolism via CYP450 (cytochrome P450) — oxidative modification
    Testosterone → estrogen (aromatase in SER): steroid biosynthesis

GOLGI APPARATUS:
  Cis face: receives vesicles from ER (COPII coated)
  Medial: further processing
  Trans face: sorts proteins to plasma membrane, lysosomes, secretion
  Trans-Golgi Network (TGN): major sorting station

  GLYCAN MODIFICATIONS (Golgi):
    Remove mannose residues → add GlcNAc, Gal, Sialic acid
    O-linked glycosylation: Ser/Thr residues
    Complex vs high-mannose glycans → determine receptor binding, half-life

VESICLE TRAFFICKING:
  COPII: ER → Golgi (anterograde)
  COPI: Golgi → ER (retrograde); within Golgi
  Clathrin: plasma membrane → endosome (receptor-mediated endocytosis); TGN → lysosome

LYSOSOMES:
  pH 4.5-5: maintained by V-ATPase (proton pump)
  Hydrolases: proteases (cathepsins), lipases, nucleases, glucosidases, sulfatases
  Digest: endocytosed material, autophagosomes (autophagy)
  Lysosomal storage diseases: enzyme deficiency → substrate accumulation
    Gaucher: β-glucocerebrosidase deficiency (treatable with enzyme replacement)
    Niemann-Pick: sphingomyelinase deficiency
```

### Mitochondria

The powerhouse. Endosymbiotic origin (α-proteobacterium, ~1.5 billion years ago).

```
STRUCTURE:
  Outer membrane: permeable (VDAC channels, porin-like)
  Intermembrane space: high [H⁺] (proton reservoir)
  Inner membrane: impermeable → proton gradient maintained
    Cristae: folded inner membrane → increased surface area
  Matrix: Krebs cycle enzymes, mtDNA, ribosomes

ELECTRON TRANSPORT CHAIN (ETC):
  Complex I (NADH dehydrogenase): NADH → NAD⁺, pumps 4H⁺
  Complex II (succinate dehydrogenase): FADH₂ → FAD⁺ (no pumping)
  Ubiquinone (CoQ): mobile electron carrier between I/II and III
  Complex III (cytochrome bc1): pumps 4H⁺ per 2 electrons
  Cytochrome c: mobile electron carrier between III and IV
  Complex IV (cytochrome c oxidase): O₂ + 4H⁺ → 2H₂O, pumps 4H⁺

ATP SYNTHASE (Complex V):
  F₀ subunit (membrane): proton channel, rotor (c subunit ring)
  F₁ subunit (matrix): catalytic (α₃β₃γ): binding change mechanism
  Proton motive force = Δψ + ΔpH (~200 mV + 1 pH unit)
  ~2.7 H⁺ per ATP (rotary mechanism)
  Complete oxidation of glucose: ~30-32 ATP per glucose

  GLUCOSE: 2 pyruvate → acetyl-CoA → Krebs cycle:
  2 NADH (glycolysis) + 2 NADH (PDH) + 6 NADH + 2 FADH₂ (Krebs) + 2 GTP → ~30-32 ATP

REACTIVE OXYGEN SPECIES (ROS):
  1-3% of electrons "leak" → O₂•⁻ (superoxide)
  → H₂O₂ (hydrogen peroxide) → •OH (hydroxyl radical, most reactive)
  Antioxidants: SOD (superoxide dismutase), catalase, glutathione peroxidase
  Excess ROS → oxidative stress → DNA damage, lipid peroxidation, protein oxidation
  Role in aging: free radical theory of aging (Harman 1956)
  Role in signaling: H₂O₂ as signal at low concentrations (thiol oxidation)
```

### Cytoskeleton

```
THREE MAIN POLYMERS:

ACTIN MICROFILAMENTS (7 nm):
  G-actin monomers → F-actin polymer (helical filament)
  Treadmilling: ATP-actin adds at barbed (+) end; ADP-actin falls off pointed (-) end
  Profilin: promotes polymerization; cofilin: severs filaments
  Myosin II: motor protein → binds actin → slides filaments (muscle contraction, cytokinesis)
  Arp2/3 complex: nucleates branched actin networks (lamellipodia in cell migration)
  Functions: cell shape, motility, endocytosis, cytokinesis

INTERMEDIATE FILAMENTS (10 nm):
  Cell-specific: keratin (epithelial), vimentin (mesenchymal), neurofilament, lamins (nuclear)
  More stable than actin/microtubules; provide mechanical strength
  Lamins A/B: nuclear lamina → mutated in Hutchinson-Gilford progeria (premature aging)

MICROTUBULES (25 nm):
  α/β tubulin heterodimers → 13 protofilaments → hollow tube
  Dynamic instability: GTP-tubulin adds at plus end; hydrolysis to GDP → catastrophe
  Organizing center: MTOC (centrosome in animal cells, SPB in yeast)
  Kinesin: walks toward plus end (away from centrosome) — cargo transport to periphery
  Dynein: walks toward minus end (toward centrosome) — cargo transport inward; cilia/flagella
  Functions: cell division (mitotic spindle), organelle transport, cilia/flagella
  Drugs: taxol (stabilizes → arrests mitosis → cancer therapy); vincristine (destabilizes)
```

---

## Cell Signaling

### Signal Transduction Cascades

```
GENERAL PRINCIPLE:
  Extracellular signal (hormone, cytokine, growth factor)
    → Receptor activation → cascade → transcription factor modification → gene expression

RECEPTOR TYROSINE KINASES (RTKs):
  EGF-R, insulin receptor, VEGFR, FGFR...
  Ligand binding → receptor dimerization → trans-autophosphorylation (Tyr)
  Phospho-Tyr → docking sites for SH2-domain proteins
    → Grb2/Sos → Ras activation (GDP → GTP)
    → Ras-GTP → Raf → MEK → ERK (MAPK cascade)
    → ERK → nucleus → phosphorylates Elk1 → immediate early genes (c-Fos, c-Myc)
    → PI3K → PIP₃ → Akt → mTOR → protein synthesis, survival
  Ras mutations in ~30% of human cancers (constitutively active)

G PROTEIN-COUPLED RECEPTORS (GPCRs):
  7-TM helix receptors; ~800 in human genome (largest gene family)
  Ligand → conformational change → G protein (Gα-GDP, Gβγ) activation
  Gα-GDP → Gα-GTP (exchange) → Gβγ dissociates → both signal

  Gαs: stimulates adenylyl cyclase → cAMP → PKA
    → PKA phosphorylates CREB → CREB target genes (CRE-containing promoters)
    → Adrenaline/glucagon: Gs → glycogen breakdown

  Gαi: inhibits adenylyl cyclase → cAMP↓
    → Opioids, adenosine → inhibit cAMP signaling

  Gαq: activates PLC-β → PIP₂ → IP₃ + DAG
    → IP₃: opens ER Ca²⁺ channels → [Ca²⁺]cyt↑ → calmodulin → CaM kinases
    → DAG: activates PKC → diverse effects
    → Muscarinic ACh receptor (Gq), angiotensin II receptor

  Gβγ: can directly activate Kir3 K⁺ channels (cardiac slowing by ACh)

GTPase TIMER:
  Intrinsic GTPase activity: Gα hydrolyzes GTP → GDP → turns off
  RGS proteins: GTPase-accelerating proteins → speed termination
  Ras: GTPase activity, accelerated by GAPs (GTPase activating proteins)
  Oncogenic Ras mutations (G12V): impair GTPase → constitutively active
```

### Second Messengers

```
cAMP (cyclic AMP):
  Generated by adenylyl cyclase from ATP → activated by Gs GPCRs
  Degraded by phosphodiesterases (PDEs) — targets of sildenafil, caffeine
  Activates: PKA (protein kinase A) → diverse phosphorylation events

Ca²⁺:
  [Ca²⁺]_cytoplasm at rest: ~100 nM (10,000× lower than extracellular ~2 mM)
  Sources: ER release (IP₃R, RyR) and plasma membrane channels (VGCC, CRAC)
  Cleared by: SERCA (back to ER), plasma membrane Ca²⁺-ATPase, Na⁺/Ca²⁺ exchanger
  Calmodulin (CaM): Ca²⁺ sensor → activates CaMKII, eNOS, phosphodiesterases
  Ca²⁺ signals: global (fertilization) vs local sparks (local ER) vs oscillations (pancreatic β cells)

PIP₂ and its products:
  PIP₂ (PI 4,5-bisphosphate): in inner leaflet → substrate for PLC and PI3K
  PLC: PIP₂ → IP₃ + DAG (as above)
  PI3K: PIP₂ → PIP₃ → recruits Akt, PDK1 → survival, growth

Nitric oxide (NO):
  Gas, freely diffusible; produced by NOS (endothelial, neuronal, inducible)
  eNOS: activated by Ca²⁺/CaM (endothelium) → NO → smooth muscle → guanylyl cyclase → cGMP → PKG → vasodilation
  Sildenafil (Viagra): PDE5 inhibitor → cGMP↑ → vasodilation (penile erection; also pulmonary hypertension)
```

---

## Cell Cycle

```
PHASES:
  G1: growth, preparation for DNA synthesis
  S: DNA synthesis (replication, ~8h)
  G2: preparation for mitosis; check DNA integrity
  M (mitosis): chromosome segregation, cell division (~1h)
  G0: quiescence (exit cell cycle; most adult neurons, muscle cells)

CYCLIN-CDK COMPLEXES:
  CDKs (cyclin-dependent kinases): catalytic subunit (needs cyclin for activity)
  Cyclins: regulatory subunit (rise and fall during cell cycle → pulsed CDK activity)

  Cyclin D-CDK4/6: G1 progression (mitogen-activated)
  Cyclin E-CDK2: G1/S transition, DNA replication initiation
  Cyclin A-CDK2: S phase, DNA synthesis
  Cyclin A-CDK1: G2/M transition
  Cyclin B-CDK1 (MPF): M phase entry, drives mitosis (targets: lamins, condensins)

CHECKPOINTS:
  G1/S: DNA integrity check; growth factor presence (Rb/E2F pathway)
  Intra-S: replication fork stalling → ATR activation
  G2/M: DNA repair completion; Chk1/Chk2 → Cdc25 → CDK1 activity
  Spindle assembly checkpoint (SAC): all kinetochores attached before anaphase
    → MCC (mitotic checkpoint complex): Mad1, Mad2, BubR1, Bub3 → inhibit APC/C
    → APC/C activated only when all chromosomes attached → securin/cyclin B degradation → anaphase
    → Failure of SAC: chromosomal instability → cancer!

RB/E2F:
  Rb (retinoblastoma): sequester E2F transcription factors in G0/G1
  Cyclin D-CDK4/6: phosphorylates Rb → releases E2F → S phase genes (replication machinery)
  Rb mutations: ~30% of human cancers (colorectal, lung, bladder)

p53 PATHWAY:
  p53: "guardian of the genome" — activated by DNA damage, oncogene stress
  ATM/ATR → Chk1/Chk2 → p53 stabilization (MDM2 prevented from targeting p53 for degradation)
  p53 → transcription of: p21 (CDK inhibitor → arrest), PUMA/NOXA (apoptosis), GADD45 (repair)
  p53 mutations: >50% of all human cancers (most common cancer mutation)
```

---

## Apoptosis (Programmed Cell Death)

```
TWO PATHWAYS:
  INTRINSIC: internal stress (DNA damage, hypoxia, oncogene activation)
    → Mitochondria: Bax/Bak (pro-apoptotic) overcome Bcl-2/Bcl-xL (anti-apoptotic)
    → Cytochrome c release from intermembrane space
    → Cytochrome c + Apaf-1 + procaspase-9 → APOPTOSOME
    → Caspase-9 → caspase-3,7 → cell death

  EXTRINSIC: death receptor (FasL, TNF, TRAIL)
    → Fas → FADD → procaspase-8 → caspase-8 → caspase-3,7

CASPASES: cysteine proteases; cleave after Asp
  Initiator: caspase-8, 9, 10 (upstream)
  Executioner: caspase-3, 6, 7 (downstream — commit cell to death)
  Substrates: lamins (nuclear envelope collapse), PARP, DNA-PK, cytoskeletal proteins

HALLMARKS OF APOPTOSIS:
  Cell shrinkage, chromatin condensation, DNA fragmentation (nucleosome ladder on gel)
  Membrane blebbing, apoptotic body formation
  PS externalization (phosphatidylserine → outer leaflet → "eat me" signal for macrophages)
  NO inflammation (unlike necrosis — contents released → inflammatory)

BCL-2 FAMILY:
  Pro-survival: Bcl-2, Bcl-xL, Bcl-w, Mcl-1 (block Bax/Bak)
  Pro-apoptotic (effectors): Bax, Bak (pore-forming)
  Pro-apoptotic (BH3-only): Bid, Bad, Bim, PUMA, NOXA (antagonize Bcl-2, activate Bax/Bak)
  BH3 mimetics (navitoclax, venetoclax): inhibit Bcl-2/Bcl-xL → apoptosis → cancer therapy
```

---

## Decision Cheat Sheet

| Function | Organelle / structure | Key molecule |
|----------|----------------------|-------------|
| Protein synthesis (secretory) | Rough ER → Golgi → vesicles | SRP, translocon, COPII |
| ATP production | Mitochondria (inner membrane) | ATP synthase, cytochromes |
| Lysosomal degradation | Lysosome (pH 4.5) | Cathepsins, V-ATPase |
| Cell movement | Actin + myosin | Arp2/3, profilin, cofilin |
| Chromosome segregation | Microtubules (spindle) | Kinesin, dynein, Eg5 |
| Extracellular signal → gene expression | GPCR/RTK cascade | Ras-ERK, PKA-CREB, PI3K-Akt |
| DNA damage response | Checkpoint kinases | ATM/ATR → Chk1/2 → p53 |
| Cell cycle progression | Cyclin-CDK complexes | Rb/E2F, securin, APC/C |
| Apoptosis commitment | Mitochondria (MOMP) | Bcl-2 family, caspase cascade |

<!-- @editor[structure/P2]: Missing Common Confusion Points section (e.g., apoptosis vs necrosis, 30-32 ATP is modern corrected number) -->
