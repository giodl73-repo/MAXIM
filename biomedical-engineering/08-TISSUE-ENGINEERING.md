# Tissue Engineering and Regenerative Medicine

## The Big Picture

Tissue engineering aims to grow functional tissue in the lab and implant it — or to stimulate
the body to repair itself. The canonical framework is the tissue engineering triad: scaffold
provides architecture, cells provide biology, signals drive differentiation. All three must be
optimized simultaneously.

```
+---------------------------------------------------------------------+
|              TISSUE ENGINEERING — LANDSCAPE                        |
+---------------------------------------------------------------------+
|                                                                     |
|  SCAFFOLD                  CELLS                  SIGNALS           |
|  (architecture)            (biology)              (differentiation) |
|  Electrospun nanofibers    Autologous             Growth factors    |
|  3D bioprinted hydrogel    Allogeneic             Mechanical load   |
|  Decellularized ECM        Xenogeneic             Substrate stiffness|
|  Porous ceramic            ESC                    Oxygen tension    |
|  Biodegradable polymer     MSC / HSC              Electrical stim.  |
|                            iPSC (Yamanaka 2006)                     |
|                                                                     |
|       +-----------------------------+                               |
|       |        BIOREACTOR           |                               |
|       | Spinner flask, rotating wall|                               |
|       | Perfusion, mechanical stimul|                               |
|       +-----------------------------+                               |
|                   |                                                 |
|                   v                                                 |
|            VASCULARIZATION                                          |
|            (the central unsolved problem)                           |
|            O2 diffusion limit ~200 μm                               |
|            Sacrificial template, vasculogenesis, 3D printing        |
|                   |                                                 |
|                   v                                                 |
|         CLINICAL TRANSLATION                                        |
|         Skin (approved), cartilage (trials), organoids (research)   |
+---------------------------------------------------------------------+
```

---

## Scaffolds

### Design Principles

```
  SCAFFOLD DESIGN REQUIREMENTS
  ============================

  POROSITY:
  >90% porosity required for adequate cell seeding and nutrient diffusion
  Pore size must match tissue type:
  Bone ingrowth: 100-500 μm pores
  Vascular tissue: 20-150 μm pores
  Neural scaffolds: 5-100 μm pores (smaller neurons)
  Skin: 20-125 μm (dermal fibroblasts)

  INTERCONNECTED PORES:
  Not just pore size — pores must be interconnected
  Isolated pores cannot be seeded or vascularized
  Often the fabrication challenge: achieving open, interconnected porosity

  MECHANICAL PROPERTIES:
  Match host tissue stiffness (important for mechanotransduction)
  Must survive handling during surgery
  Maintain mechanical integrity until tissue formation
  Ideally: stiffness decreases as tissue forms (isostatic)

  DEGRADATION RATE:
  Synchronized with tissue formation rate
  Too fast: scaffold collapses before tissue can bear load
  Too slow: chronic foreign body response
  Remodeling equation: tissue growth rate ~ scaffold degradation rate

  SURFACE CHEMISTRY:
  Hydrophilic surfaces: better cell adhesion vs. hydrophobic
  Protein adsorption: first event after implant (fibronectin, vitronectin)
  -> mediates integrin binding (RGD sequences)
  Surface functionalization: covalently attach ECM proteins, peptides

  STERILIZABILITY:
  EO gas, gamma irradiation, e-beam — each affects polymer differently
  PLGA: sensitive to gamma (degrades) -> EO preferred
  Titanium: gamma, e-beam, steam — more options
```

### Fabrication Methods

#### Electrospinning

```
  ELECTROSPINNING
  ===============

  PRINCIPLE:
  Polymer solution in syringe -> high voltage (~10-30 kV) applied
  between needle tip and collector plate
  Charge builds on droplet at needle tip -> Taylor cone forms
  -> thin jet ejects, solvent evaporates in flight
  -> solid nanofibers (~100 nm - 10 μm) deposit on collector

  MORPHOLOGY:
  Random fibers: standard flat collector -> isotropic mat
  Aligned fibers: rotating mandrel collector -> directional
    (useful for tendons, ligaments, nerves — aligned ECM)

  ADVANTAGES:
  High surface area (mimics ECM fibrous structure)
  Fiber diameter tunable by polymer concentration, voltage, flow rate
  Can coaxially spin: core-shell fibers (drug in core, polymer shell)
  -> controlled drug release from fiber mat

  MATERIALS: PLGA, PCL, collagen, PLA, PAN, PEO, many others

  LIMITATIONS:
  Poor cell infiltration into fiber mesh (too dense)
  Typically 2D mat or thin tube — limited 3D architecture
  Scaling to large constructs is challenging

  APPLICATIONS:
  Wound dressings, vascular grafts (small diameter), tendon repair,
  nerve conduits, cardiac patches, drug-eluting membranes
```

#### Freeze-Drying (Lyophilization)

```
  FREEZE-DRYING (LYOPHILIZATION) SCAFFOLD FABRICATION
  =====================================================

  Process:
  Polymer solution -> freeze (ice crystal formation as template)
  -> freeze-dry (sublimation of ice under vacuum)
  -> porous sponge remains where ice was

  PORE SIZE CONTROL:
  Fast freeze: small ice crystals -> small pores (~10-50 μm)
  Slow freeze or directional freeze: large ice crystals -> large pores
  Directional freeze: aligned lamellar pores for oriented scaffolds

  MATERIALS: collagen, PLGA, gelatin, chitosan, hyaluronic acid

  ADVANTAGES:
  Simple equipment, scalable
  Excellent for collagen sponges (Integra wound matrix)
  FDA-approved products use this method

  LIMITATIONS:
  Irregular pore geometry (vs. CAD-controlled 3D printing)
  Structural weakness if very high porosity
```

#### 3D Bioprinting

```
  3D BIOPRINTING — METHODS
  =========================

  EXTRUSION BIOPRINTING (most common):
  Bioink in syringe -> pneumatic or mechanical extrusion
  Printed layer-by-layer on build platform
  Bioink: hydrogel containing cells (alginate, GelMA, Pluronic)

  Bioink requirements:
  SHEAR-THINNING: viscosity decreases under shear (print flows)
  YIELD STRESS: gel at rest (printed structure holds shape)
  CROSSLINKABLE: gelates after printing (thermal or UV/ionic)
  CYTOCOMPATIBLE: shear stress during extrusion must not kill cells

  Shear stress on cells during extrusion:
  τ = 4ηQ/(πr³) (Hagen-Poiseuille for Newtonian, approximate)
  Higher flow rate + narrower nozzle + stiffer ink = more stress
  Typical viability post-print: 70-90% (some cell death is accepted)

  INKJET BIOPRINTING:
  Thermal (bubble) or piezoelectric drop-on-demand
  Low-viscosity bioinks (1-10 mPa·s)
  High resolution (~50 μm), high speed
  Lower shear stress than extrusion -> better viability
  Limited scaffold height, nozzle clogging with cells

  STEREOLITHOGRAPHY (SLA) / DLP BIOPRINTING:
  Photocrosslinkable bioink (GelMA + photoinitiator)
  UV or visible light exposure layer-by-layer
  Excellent resolution (<50 μm), complex geometries
  Concern: UV photoinitiator cytotoxicity -> visible light systems preferred

  LASER-ASSISTED BIOPRINTING (LAB):
  Pulsed laser generates vapor bubble -> ejects droplet from ribbon
  No nozzle -> no clogging, high cell density inks possible
  Low throughput, expensive

  BIOINK FORMULATIONS:
  +------------------+----------------------------------------------+
  | GelMA (gelatin   | Gelatin methacrylate — photocrosslinkable    |
  | methacrylate)    | Tunable stiffness (0.5-40 kPa)              |
  |                  | RGD sequences -> cell adhesion               |
  |                  | Most popular research bioink                  |
  +------------------+----------------------------------------------+
  | Alginate         | Ionic crosslink (CaCl2)                      |
  |                  | Biocompatible, easy to work with              |
  |                  | Poor cell adhesion (no RGD) -> blend needed  |
  +------------------+----------------------------------------------+
  | Fibrin           | Thrombin + fibrinogen -> coagulates quickly  |
  |                  | Native ECM material, excellent bioactivity   |
  |                  | Weak mechanical properties                   |
  +------------------+----------------------------------------------+
  | Pluronic F127    | Reverse thermal gelation (gel at 37°C)       |
  |                  | Sacrificial ink: print, then dissolve at 4°C |
  |                  | Creates channels within GelMA structure       |
  +------------------+----------------------------------------------+
```

---

## Cell Sourcing

### Autologous vs. Allogeneic

```
  CELL SOURCING TRADE-OFFS
  =========================

  +------------------+---------------------+------------------------+
  | Source           | Advantage           | Disadvantage           |
  +------------------+---------------------+------------------------+
  | Autologous       | No immune rejection | Donor site morbidity   |
  | (patient's own)  | Patient-specific    | Limited quantity       |
  |                  | Gold standard       | Time: harvest -> culture|
  |                  |                     | -> implant = weeks     |
  +------------------+---------------------+------------------------+
  | Allogeneic       | Off-the-shelf       | Immune rejection risk  |
  | (donor-derived)  | Scalable            | Requires matching or   |
  |                  | Consistent quality  | immunosuppression or   |
  |                  | Ready when needed   | immune evasion strategy|
  +------------------+---------------------+------------------------+
  | Xenogeneic       | Abundant supply     | Strong immune response |
  | (animal-derived) | (porcine valves)    | Hyperacute rejection   |
  |                  |                     | Zoonotic risk          |
  +------------------+---------------------+------------------------+
  | iPSC-derived     | Patient-specific    | Complex differentiation|
  | (patient iPSC)   | No immune rejection | Cost, time, quality    |
  |                  | Unlimited supply    | Genomic stability risk |
  |                  | Disease modeling    | Residual pluripotency  |
  +------------------+---------------------+------------------------+
```

---

## Stem Cells

### The iPSC Revolution

```
  INDUCED PLURIPOTENT STEM CELLS (iPSC)
  ======================================

  YAMANAKA FACTORS (2006, Nobel Prize 2012):
  Takahashi and Yamanaka showed mature differentiated cells
  can be reprogrammed to pluripotency by forced expression of:
  OCT4 (POU5F1)   — pluripotency master regulator
  SOX2            — pluripotency, neural stemness
  KLF4            — pluripotency, epithelial
  c-MYC           — proliferation (optional, but improves efficiency)
  OSKM = Oct4 + Sox2 + Klf4 + cMyc

  REPROGRAMMING METHODS:
  Integrating viral (retrovirus, lentivirus): original method
  -> insertional mutagenesis risk (oncogenesis)
  Non-integrating:
  - Episomal vectors: plasmid, transiently maintained
  - RNA/mRNA delivery (synthetic mRNA method)
  - Sendai virus (non-integrating RNA virus): current standard
    for clinical-grade iPSC generation
  - Small molecules: some chemical combinations (no genetic material)

  CHARACTERIZATION of iPSC:
  Morphology: ESC-like compact colonies with defined borders
  Markers: OCT4, NANOG, SOX2, SSEA-4, TRA-1-60 (pluripotency markers)
  Karyotype: must confirm normal karyotype (reprogramming can introduce errors)
  Teratoma assay: inject iPSC into immunocompromised mouse -> forms
    teratoma with all three germ layers (gold standard for pluripotency)
  In vitro differentiation: confirm ability to form ectoderm, mesoderm, endoderm

  Bridge to software: iPSC reprogramming is factory-resetting a cell.
  The genome is unchanged — epigenetic marks (methylation, histone
  modification) are erased and reset to pluripotent state.
  It is not genetic engineering — the DNA sequence is (mostly) the same.
  It is operating-system-level state reset, not source code modification.
```

### Differentiation Protocols

```
  DIFFERENTIATION — DIRECTING iPSC TO TARGET CELL TYPE
  =======================================================

  iPSC can become (theoretically) any cell type.
  Differentiation requires recapitulating embryonic development
  in accelerated form: 5-30 days vs. months in vivo.

  CARDIOMYOCYTE DIFFERENTIATION:
  Days 0-2: Wnt activation (CHIR99021 = GSK3 inhibitor)
    -> mesoderm induction
  Days 2-4: Wnt inhibition (IWR-1 or IWP-2)
    -> cardiac mesoderm -> cardiac progenitors
  Days 10-15: Beating cardiomyocyte clusters visible
  Days 20+: Metabolic purification (lactate medium)
    -> cardiomyocytes survive (use lactate), pluripotent cells die
  Result: ~80-90% cardiomyocyte purity

  NEURAL DIFFERENTIATION:
  Dual SMAD inhibition (LDN193189 + SB431542):
    -> blocks BMP + TGF-beta -> forces neural fate
  Adds retinoic acid and sonic hedgehog (SHH) for spinal neuron type
  BDNF, GDNF, NT-3 for neuronal maturation
  Days 25-60 for mature neurons

  MECHANOTRANSDUCTION IN DIFFERENTIATION:
  Substrate stiffness (Young's modulus) directs stem cell fate:
  ~0.1-1 kPa (soft as brain)    -> neural lineage
  ~8-17 kPa (muscle stiffness)  -> myogenic lineage
  ~25-40 kPa (bone stiffness)   -> osteogenic lineage
  Seminal work: Engler et al., Cell 2006
  Mechanism: integrin-focal adhesion-cytoskeleton mechanosensing
    -> nuclear YAP/TAZ translocation -> gene expression changes
```

---

## Bioreactors

```
  BIOREACTOR TYPES FOR TISSUE ENGINEERING
  =========================================

  SPINNER FLASK:
  Cells on microcarriers or scaffold suspended in medium
  Magnetic stirrer bar agitates medium
  Convective mass transfer: O2, glucose, waste products
  Problem: turbulent shear at high RPM damages cells
  Use: embryoid body formation, cartilage precultivation
  Volume: 100 mL - 10 L (scalable)

  ROTATING WALL VESSEL (RWV):
  NASA-developed. Two cylinders rotating at same speed
  -> simulated microgravity-like environment
  Cells/constructs in free suspension (minimal fluid shear)
  Low turbulence, good nutrient transport
  Use: cartilage, bone, tumor spheroids, cancer models

  PERFUSION BIOREACTOR:
  Medium pumped through scaffold pores
  -> convective transport to cells in scaffold interior
  Solves nutrient deprivation in thick constructs (>2 mm)
  Flow also provides shear stress -> mechanostimulation
  Important for bone (osteogenic), vascular (endothelial)
  Hollow fiber perfusion: ECM tube with medium flow inside

  MECHANICAL STIMULATION BIOREACTORS:
  CYCLIC STRETCH: for vascular and cardiac tissue
    Pulsatile pressure stretches silicone tube with cells
    -> VSMCs align, collagen production
  COMPRESSIVE LOADING: for cartilage
    Cyclical compression on hydrogel construct
    -> chondrocyte matrix production
  SHEAR FLOW: for endothelium
    Flow chamber applies fluid shear stress
    -> EC alignment, anti-thrombogenic phenotype

  BIOREACTOR GOALS:
  1. Mass transfer (O2 and nutrient delivery deep into construct)
  2. Mechanical stimulation (mimic physiological loading)
  3. Waste removal (CO2, lactate, ammonia)
  4. Scalability for manufacturing
```

---

## Vascularization — The Central Problem

```
  THE VASCULARIZATION PROBLEM
  ============================

  FUNDAMENTAL CONSTRAINT:
  Oxygen diffusion limit in tissue: ~100-200 μm from nearest capillary
  Beyond that: cells become hypoxic -> necrosis at center of thick construct

  Thin constructs (<200 μm): vascularization less critical
  -> avascular cornea, cartilage, skin substitutes — already clinically used

  Thick constructs (bone, heart, liver): REQUIRE vascularization before
  or immediately upon implantation -> clinically difficult

  STRATEGIES:

  1. PRE-VASCULARIZATION:
     Co-culture HUVECs (human umbilical vein endothelial cells) +
     stromal cells (pericytes) in scaffold before implantation
     -> forms rudimentary capillary network in vitro
     Upon implantation: host vessels inosculate with pre-formed network
     Problem: slow in vivo vascular inosculation (days to week)

  2. VASCULOGENESIS via co-culture:
     Seed scaffold with endothelial cells + pericytes + smooth muscle cells
     Allow self-assembly in bioreactor
     Perfusable networks form over 7-14 days

  3. SACRIFICIAL TEMPLATING:
     Print carbohydrate glass (glucose + sucrose lattice) within GelMA
     -> crosslink GelMA around lattice
     -> dissolve carbohydrate (water soluble) leaving channels
     Channels ~150 μm diameter, connected network
     Endothelial cell lining of channels -> functional vessels
     Miller et al., Nature Materials 2012

  4. 3D BIOPRINTED CHANNELS:
     Pluronic F127 ink (fugitive): print channels within cell-laden hydrogel
     -> cool to 4°C to liquefy Pluronic -> aspirate out -> channels remain
     Endothelialization of channels -> perfusable vascular network
     Kolesky et al., Advanced Materials 2014

  5. ANGIOGENESIS via growth factors:
     VEGF (vascular endothelial growth factor): primary pro-angiogenic signal
     Incorporate VEGF in scaffold -> sustained release -> host vessel ingrowth
     bFGF (basic fibroblast growth factor): angiogenesis co-factor
     Controlled release: PLGA microspheres in scaffold, temporal gradients

  6. BIOFABRICATION of anastomosable vessels:
     Engineered small-diameter vascular grafts (TEVG):
     Weinberg-Bell (1986): collagen gel + smooth muscle cells + endothelium
     Niklason (1999): pulsatile bioreactor for collagen remodeling -> strong
     Humacyte: decellularized bioengineered vessel (FDA cleared)
       -> "acellular" vessel, recellularized by host after implant
```

---

## Organoids

```
  ORGANOIDS — SELF-ORGANIZING 3D CULTURES
  =========================================

  DEFINITION:
  Self-organizing 3D structures derived from stem cells (iPSC or adult stem cells)
  that recapitulate key architectural and functional features of an organ.
  Key: self-organization (cells drive the organization, not the researcher)

  FOUNDING ORGANOID PAPERS:
  Intestinal: Sato et al., Nature 2009 (Lgr5+ intestinal stem cells in Matrigel)
  Brain: Lancaster et al., Nature 2013 (cerebral organoids from iPSC)
  Kidney: Takasato et al., Nature 2015
  Liver: Huch et al., Gut 2015

  INTESTINAL ORGANOID:
  Source: Lgr5+ intestinal stem cells from crypts (endoscopic biopsy)
  Self-organize into "mini-gut": crypts + villi architecture
  Contains absorptive enterocytes, goblet cells, Paneth cells
  Applications: cystic fibrosis drug testing (patient-specific),
    inflammatory bowel disease research, host-microbiome interactions

  BRAIN ORGANOID (cerebral organoid):
  Source: iPSC -> neural induction -> free-floating 3D culture
  Forms cortical-like layers, cortical neurons, glial cells
  Recapitulates some developmental neurobiology
  Uses: microcephaly (MCPH1, CDK5RAP2), Zika virus pathology,
    drug screening, Alzheimer's models from patient iPSC
  Limitations: no vasculature -> necrotic core beyond ~1mm
               no sensory input/output -> activity not physiological
               lacks proper connectivity

  PATIENT-DERIVED ORGANOIDS FOR DRUG SCREENING:
  Biopsy from patient tumor -> tumor organoid -> drug panel
  Predict which drugs will work for that patient (precision oncology)
  Clinical correlation studies ongoing (Clevers group, Netherlands)
  Pancreatic cancer: organoid drug response correlated with clinical
  response in Phase II studies

  ORGAN-ON-CHIP:
  Microfluidic device with human cells in physiologically relevant
  architecture. Not self-organizing (unlike organoids), but controlled.
  Lung-on-chip (Wyss): alveolar + endothelial cells, breathing motion
  Gut-on-chip: intestinal cells + peristalsis, microbiome co-culture
  Liver-on-chip: hepatocytes + flow (sinusoid analog)
  Multi-organ: gut -> liver -> kidney chip (microphysiological system)
  FDA: Advancing Alternative Methods Act (2022) — allows alternatives
    to animal testing for drug development
```

---

## 3D Bioprinting — Clinical Progress

```
  CLINICAL TRANSLATION OF 3D BIOPRINTING
  ========================================

  FDA CLEARED:
  +---------------------------+-------------------------------------+
  | Skin                      | RECELL (Avita Medical) — uses       |
  |                           | patient's own cells, spray device   |
  |                           | FDA cleared for burns and wounds    |
  |                           | Not strictly "bioprinting" but      |
  |                           | autologous cell-based              |
  |                           |                                     |
  |                           | 3D-printed acellular skin scaffolds:|
  |                           | Integra (collagen/GAG scaffold) —   |
  |                           | not bioprinted but 3D designed      |
  +---------------------------+-------------------------------------+

  IN CLINICAL TRIALS:
  +---------------------------+-------------------------------------+
  | Cartilage                 | MACI (Vericel) FDA approved —       |
  |                           | autologous chondrocytes on collagen |
  |                           | membrane (not strictly bioprinted)  |
  |                           | 3D bioprinted cartilage: early      |
  |                           | clinical trials for ears (auricle), |
  |                           | tracheal ring repair               |
  +---------------------------+-------------------------------------+
  | Bone                      | Patient-specific 3D printed Ti      |
  |                           | implants (not bioprinted, but       |
  |                           | 3D printed from CT data)            |
  |                           | Bioprinted bone: Phase I trials     |
  +---------------------------+-------------------------------------+

  RESEARCH STAGE:
  +---------------------------+-------------------------------------+
  | Heart                     | Lewis lab: pumping cardiac tissue   |
  |                           | from iPSC-derived cardiomyocytes    |
  |                           | Vascularized heart patch: ongoing   |
  |                           | Full organ: decades away            |
  +---------------------------+-------------------------------------+
  | Kidney                    | Organoid stage; tubular structures  |
  |                           | printed with PTEC cells             |
  +---------------------------+-------------------------------------+
  | Liver                     | Organovo NovoGen: liver tissue for  |
  |                           | drug toxicity testing (commercial)  |
  |                           | Implantable: research stage         |
  +---------------------------+-------------------------------------+

  KEY MANUFACTURING CHALLENGES:
  1. GMP (Good Manufacturing Practice) compliance for cell processing
  2. Scale-up: from lab-scale to clinical quantities
  3. Cold chain: cell viability during storage and transport
  4. Lot-to-lot variability: living cells are inherently variable
  5. Regulatory pathway: combination product (device + cells + scaffold)
  6. Shelf life: autologous requires patient-specific manufacturing
```

---

## Common Confusion Points

**iPSC are not embryonic stem cells**: ESC are derived from inner cell mass of blastocyst
embryos (ethical issues). iPSC are derived by reprogramming mature somatic cells — no embryo
required. Both are pluripotent (can form all cell types). iPSC have potential for patient-
specific therapies and disease modeling. However, iPSC may retain epigenetic memory of origin
tissue and can have genomic instability introduced during reprogramming.

**Scaffold porosity vs. pore size**: You need BOTH high porosity (>90% void space for cell
ingrowth) AND appropriate pore size (100-500 μm for bone) AND interconnected pores.
High porosity with small, isolated pores fails. Many scaffold papers report porosity percentage
without reporting interconnectivity — a critical oversight.

**Organoids are not miniature organs**: Brain organoids lack vasculature, immune cells, and
proper sensory connectivity. They recapitulate aspects of development and disease, but drug
responses in organoids may not predict in vivo responses due to missing stromal components,
immune microenvironment, and systemic factors. They are exceptional models for specific
questions, not replacement for animal studies in all contexts.

**Electrospinning fiber diameter vs. cell size**: Typical electrospun fibers are 100 nm to 10
μm in diameter. A typical cell is 10-50 μm in diameter. Cells cannot easily penetrate into
a tightly packed nanofiber mat — they sit on the surface. For applications requiring cell
infiltration through the thickness, either coarser fibers, sacrificial fibers to create space,
or hybrid approaches are needed.

**GMP scale-up is a separate engineering problem**: Getting a tissue engineering construct to
work in a lab is very different from manufacturing it under GMP conditions with consistent
quality. GMP manufacturing requires environmental controls, SOPs for every process step,
equipment validation (IQ/OQ/PQ), raw material qualification, lot release testing, stability
testing. Many constructs that work beautifully in research labs fail at GMP scale-up.

---

## Decision Cheat Sheet

| Tissue engineering challenge | Approach | Notes |
|---|---|---|
| Scaffold for bone | 3D-printed porous Ti or HA ceramic or PEEK | Proven clinically; bone is stiff, needs stiff scaffold |
| Scaffold for soft tissue | Electrospun PCL/PLGA or decellularized ECM | Compliance matching important |
| Scaffold for skin | Integra (collagen/GAG) or electrospun + cells | Avascular tissue — works clinically |
| Cell source: patient-specific | iPSC (Sendai virus reprogramming) | Weeks to generate, complex differentiation |
| Cell source: off-the-shelf | Allogeneic MSC or iPSC banks | HLA matching or immune evasion strategy needed |
| Disease modeling | Patient iPSC -> target organoid | Cardiac, neural, hepatic, gut all established |
| Drug screening | Organ-on-chip or patient-derived organoid | Replaces some animal testing |
| Vascularized thick construct | Sacrificial Pluronic template or VEGF-releasing scaffold | Still largely research stage |
| Bioreactor for cartilage | Rotating wall vessel or cyclic compression | Proven for chondrocyte matrix production |
| Bioreactor for vascular | Pulsatile flow bioreactor | Shear stress drives endothelial alignment |
| Regulatory strategy | Combination product (CBER or CDRH lead) | Long timelines; iPSC adds complexity |
