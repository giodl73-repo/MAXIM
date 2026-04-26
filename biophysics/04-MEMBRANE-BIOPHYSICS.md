# Membrane Biophysics — Lipid Bilayers, Membrane Potential, and Ion Channels

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│               MEMBRANE BIOPHYSICS LANDSCAPE                              │
│                                                                            │
│  BILAYER STRUCTURE               ELECTRICAL PROPERTIES                   │
│  ────────────────                ────────────────────                    │
│  Singer-Nicolson fluid mosaic    Resting potential: -70 mV (neuron)      │
│  2D fluid: lateral diffusion     Goldman-Hodgkin-Katz equation           │
│  Lipid asymmetry                 Nernst equation per ion                 │
│  Rafts / phase separation        Membrane as RC circuit                  │
│                                                                            │
│  ION CHANNELS                    VESICLE MECHANICS                       │
│  ────────────                    ─────────────────                       │
│  Gating: voltage / ligand / mech Bending rigidity κ ≈ 20 k_BT            │
│  Single channel conductance      Helfrich free energy                    │
│  Selectivity filter              Curvature-inducing proteins             │
│  Patch clamp technique           BAR domains, dynamin                    │
│                                                                            │
│  SCALE:                                                                    │
│  Bilayer thickness: ~4 nm total (hydrophobic core: ~3 nm)                │
│  Single channel current: 1-100 pA (10⁶-10⁷ ions/s)                       │
│  Membrane resistance: ~10⁸ Ω per μm² (neuron at rest)                    │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — Lipid Bilayer Structure: The Fluid Mosaic Model

### Singer-Nicolson Model (1972)

The lipid bilayer is a 2D fluid: lipids and proteins diffuse laterally within
each leaflet. Proteins float in the bilayer like icebergs in a lipid sea.

```
  BILAYER CROSS-SECTION:

  Extracellular                     ~2-3 nm
  ────────────────────────────────────────────────────────── ← headgroups
  ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○
  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ← fatty acid tails
  |||||||||||||||||||||||||||||||||||||||||||||||||||||||||| ~3 nm hydrophobic
  ○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○○
  ────────────────────────────────────────────────────────── ← headgroups
  Cytoplasmic                       ~2-3 nm

  ○ = phospholipid headgroup (charged / polar)
  | = fatty acid chain (hydrophobic)
  Total bilayer: ~4-5 nm

  Integral membrane protein: TM helices span the 3 nm hydrophobic core
  Peripheral membrane protein: binds headgroup surface electrostatically
```

### Lipid Species and Their Biophysical Roles

```
  ┌─────────────────────────────────────────────────────────────────────┐
  │  LIPID CLASS    │  LOCATION        │  BIOPHYSICAL ROLE              │
  │  ─────────────  │  ─────────────── │  ────────────────────────────── │
  │  DPPC (PC)      │  Both leaflets   │  Most abundant, forms bilayer  │
  │  PE             │  Inner leaflet   │  Cone shape → negative curvature│
  │  PS             │  Inner leaflet   │  Negatively charged (apoptosis │
  │                 │                  │  signal when outer leaflet)    │
  │  PI(4,5)P₂      │  Inner leaflet   │  Signaling: PLC substrate,     │
  │                 │                  │  channel gating modulator      │
  │  Cholesterol    │  Both leaflets   │  Modulates fluidity, forms rafts│
  │                 │                  │  40% of mammalian membrane lipid│
  │  Sphingomyelin  │  Outer leaflet   │  High melting temperature,     │
  │                 │                  │  raft component                │
  │  Cardiolipin    │  Inner mitochond.│  Anchors ETC complexes,        │
  │                 │  membrane        │  required for ATP synthase     │
  └─────────────────────────────────────────────────────────────────────┘
```

### Membrane Fluidity and Phase Transitions

Lipids undergo a gel-to-liquid crystalline phase transition at temperature Tm:

```
  T < Tm (gel phase):
    Ordered, all-trans fatty acid chains
    Slow lateral diffusion: D ≈ 10⁻¹⁰ m²/s
    High viscosity

  T > Tm (liquid crystalline):
    Disordered, gauche kinks in chains
    Fast lateral diffusion: D ≈ 10⁻⁸-10⁻⁹ m²/s
    Low viscosity

  Factors affecting Tm:
    Chain length ↑   →  Tm ↑ (more van der Waals contact)
    Unsaturation ↑   →  Tm ↓ (kinks prevent packing)
    Cholesterol: broadens transition, sets intermediate fluidity

  At 37°C, mammalian membranes are in liquid crystalline phase.
  Bacteria adjust chain composition to maintain fluidity at their T
  (homeoviscous adaptation).
```

### Lipid Rafts

Cholesterol + sphingomyelin form liquid-ordered (Lo) phase domains that are
more ordered than the surrounding liquid-disordered (Ld) phase:

```
  Lo (raft) phase:          Ld (bulk) phase:
  Cholesterol-enriched      Unsaturated PE/PC
  Sphingomyelin-rich        Low cholesterol
  More ordered              Disordered
  Slower diffusion          Faster diffusion
  GPI-anchored proteins     Most TM proteins

  Rafts are 10-200 nm in size, transient (ms timescale)
  Hard to isolate: detergent-resistant membranes (DRMs) used as proxy
  but this is artifact-prone (cold detergent extracts artifacts)
```

---

## Section 2 — Membrane Potential

### Equilibrium Potential: The Nernst Equation

For an ion species i crossing a membrane, the equilibrium (Nernst) potential
is where the concentration gradient exactly cancels the electrical gradient:

```
  Eᵢ = (RT / zᵢF) × ln([ion]_out / [ion]_in)
     = (25.7 mV / zᵢ) × ln([ion]_out / [ion]_in)   at 25°C
     = (26.7 mV / zᵢ) × ln([ion]_out / [ion]_in)   at 37°C

  Typical mammalian neuron:

  Ion    [out]    [in]     z    E_Nernst
  ─────  ───────  ───────  ──   ────────
  Na⁺    145 mM   12 mM   +1   +67 mV
  K⁺     4 mM     155 mM  +1   -98 mV
  Cl⁻    110 mM   4 mM    -1   -90 mV
  Ca²⁺   1.5 mM   100 nM  +2   +137 mV

  Resting membrane potential: -70 mV
  (between E_K and E_Na, closer to E_K because
   membrane is ~100× more permeable to K⁺ at rest)
```

### Goldman-Hodgkin-Katz (GHK) Equation

When multiple ions contribute (with different permeabilities), the resting
potential is a permeability-weighted average:

```
  V_m = (RT/F) × ln[(P_K[K⁺]_o + P_Na[Na⁺]_o + P_Cl[Cl⁻]_i) /
                     (P_K[K⁺]_i + P_Na[Na⁺]_i + P_Cl[Cl⁻]_o)]

  At rest (neuron):  P_K : P_Na : P_Cl ≈ 1 : 0.04 : 0.45

  At action potential peak:  P_Na / P_K ≈ 20  (Na channels open)
  → Vm shifts toward E_Na ≈ +67 mV

  This is the GHK voltage equation. For current (flux), the GHK current equation:
  Iᵢ = Pᵢ z²ᵢ F² Vm/RT × ([ion]_i - [ion]_o exp(-zᵢFVm/RT)) /
                            (1 - exp(-zᵢFVm/RT))
```

### Membrane as an Electrical Circuit

```
  Equivalent circuit model:

  Extracellular
      │
  ────┤────────┬──────────────────────────────────────────
      │        │
     C_m      G_K(E_K)   G_Na(E_Na)   G_Cl(E_Cl)
     (capacitor) (conductance and battery for each ion)
      │        │
  ────┤────────┴──────────────────────────────────────────
      │
  Intracellular

  C_m = membrane capacitance ≈ 1 μF/cm²  (for lipid bilayer)
  G_ion = conductance = reciprocal of resistance
  E_ion = Nernst potential (EMF source)

  Kirchhoff's law:  C_m × dV/dt = -Σ G_ion(V-E_ion) + I_ext

  Time constant:  τ = R_m × C_m (sets how fast V changes)
  Space constant: λ = sqrt(R_m / R_axial) (how far signal propagates)
```

---

## Section 3 — Ion Channels

### Channel Basics

Ion channels are membrane proteins that form hydrophilic pores:

```
  ┌───────────────────────────────────────────────────────────────┐
  │  ION CHANNEL PROPERTIES                                       │
  │                                                               │
  │  Single-channel conductance:  1-100 pS (picosiemens)          │
  │  → At -70 mV: current = g × V ≈ 1 pS × 70 mV = 70 fA        │
  │  → Ionic flux: ~10⁶-10⁷ ions/second per channel               │
  │                                                               │
  │  Selectivity filter: sub-Å selectivity between K⁺ and Na⁺     │
  │  (K⁺ r = 1.33 Å; Na⁺ r = 0.95 Å; filter: ~3 Å pore)         │
  │  → Selectivity paradox: K⁺ passes 10⁴× faster than Na⁺        │
  │     despite K⁺ being larger                                   │
  │  → Resolution: K⁺ fits perfectly into 8-oxygen cage; Na⁺      │
  │     retains hydration shell (dehydration cost > electrostatic │
  │     gain inside filter)                                       │
  │                                                               │
  │  Gating mechanisms:                                           │
  │    Voltage-gated: S4 helix (charged) moves in field           │
  │    Ligand-gated: ACh, GABA, glutamate binding opens pore      │
  │    Mechanically-gated: membrane tension, touch                │
  │    Inactivation: N-type (ball-and-chain), C-type (pore        │
  │      collapse during sustained depolarization)                │
  └───────────────────────────────────────────────────────────────┘
```

### Voltage-Gated Channels: Structural Basis of Gating

Voltage-gated K⁺ channel (Kv): four subunits, each with 6 TM helices:

```
  Topology per subunit:
  S1-S4: voltage-sensing domain (VSD)
  S5-S6: pore domain (forms the conduction pathway)

  S4 helix: 4-7 basic residues (Arg/Lys) at every 3rd position
    → gating charges; moves ~10-15 Å through the membrane field
    → moves ~1-4e× per subunit; 4 subunits × 2-3e = 12e total
    → experimentally measured: ~12-14e gating charge per channel

  Selectivity filter: TVGYG motif (highly conserved in K⁺ channels)
    → four K⁺ binding sites (S1-S4) in single-file conduction
    → two K⁺ ions occupy alternating sites (concerted knock-on)
```

### Patch Clamp Technique

Developed by Neher and Sakmann (Nobel 1991), patch clamp records electrical
activity of single ion channels:

```
  Fire-polished pipette (tip ~1 μm) pressed against cell membrane

  ┌─────────────────────────────────────────────────────────────┐
  │  PATCH CLAMP CONFIGURATIONS                                 │
  │                                                             │
  │  Cell-attached: pipette on intact cell                      │
  │    → channels in native membrane environment                │
  │    → cytoplasmic face inaccessible                          │
  │                                                             │
  │  Whole-cell: rupture patch → access to cell interior        │
  │    → measure total membrane current                         │
  │    → cell contents exchange with pipette solution           │
  │                                                             │
  │  Inside-out: pull after cell-attached                       │
  │    → cytoplasmic face exposed to bath solution              │
  │    → apply ligands to cytoplasmic side                      │
  │                                                             │
  │  Outside-out: pull after whole-cell                         │
  │    → extracellular face exposed to bath                     │
  │    → apply agonists to extracellular side                   │
  └─────────────────────────────────────────────────────────────┘

  Seal resistance: >1 GΩ ("gigaseal") required
    → noise floor: ~0.1 pA  (allows 1-pS channels to be detected)

  Voltage clamp: feedback amplifier holds Vm at command potential
    → records current as channels open/close
    → isolates ionic from capacitive current
```

### Channel Kinetics: Markov Models

Channel gating is modeled as a continuous-time Markov chain:

```
  Simple two-state (closed ⇌ open):
    C ⇌ O    with rates α (opening) and β (closing)

  Open probability:  Po = α / (α + β) = α × τ_open

  Mean open time:  τ_open = 1/β
  Mean closed time: τ_closed = 1/α

  For voltage-gated Na⁺ channel (Hodgkin-Huxley notation):
    C3 ⇌ C2 ⇌ C1 ⇌ O ⇌ I  (three closed, one open, one inactivated)

  Full dwell-time histogram analysis reveals number of states and
  their kinetics from single-channel recordings.
```

---

## Section 4 — Membrane Mechanics: Bending, Curvature, and Vesicles

### Helfrich Free Energy

The membrane's mechanical energy as a thin elastic sheet:

```
  F_Helfrich = ∫ [κ/2 × (c₁ + c₂ - c₀)² + κ_G × c₁c₂] dA + σ∫dA

  c₁, c₂ = principal curvatures at each point
  c₀ = spontaneous curvature (asymmetric bilayer)
  κ = bending rigidity ~ 10-25 k_BT for typical bilayer
  κ_G = Gaussian curvature modulus
  σ = membrane tension

  Key values:
    DPPC bilayer:    κ ≈ 25 k_BT
    Erythrocyte:     κ ≈ 18 k_BT
    Asymmetric bilayer: c₀ ≠ 0 (favors spontaneous curvature)
```

### Vesicle Formation and Membrane Curvature

Forming a spherical vesicle from flat membrane costs energy:

```
  Sphere: c₁ = c₂ = 1/R → (c₁+c₂)² = 4/R²

  F_bending = ∫ κ/2 × 4/R² dA = κ/2 × 4/R² × 4πR² = 8πκ

  F_bending is INDEPENDENT of radius!
  → Same energy to form a 20 nm or 200 nm vesicle

  For κ = 20 k_BT:  F_bending = 8π × 20 k_BT ≈ 500 k_BT
  → Thermally impossible; requires active machinery or lipid asymmetry
```

Biological curvature generation:

```
  ┌─────────────────────────────────────────────────────────────────┐
  │  CURVATURE MECHANISM    │  PROTEIN/LIPID     │  PROCESS         │
  │  ─────────────────────  │  ─────────────────  │  ──────────────── │
  │  BAR domain scaffold    │  N-BAR, F-BAR, I-BAR│  Endocytosis,   │
  │                         │  (banana-shaped)    │  tubulation       │
  │  Amphipathic helix ins. │  ENTH, ANTH, ALPS   │  Sensing and      │
  │                         │  N-BAR H0 helix     │  generating curv. │
  │  Lipid asymmetry        │  Flippases (ATP dep.)│  PS inner leaflet │
  │                         │  Scramblases        │  apoptosis signal │
  │  Dynamin GTPase         │  Helical polymer     │  Vesicle scission │
  │                         │  around neck        │  (endocytosis)    │
  │  Clathrin coat          │  Triskelion lattice  │  Clathrin-coated  │
  │                         │  geometry           │  pits             │
  └─────────────────────────────────────────────────────────────────┘
```

---

## Section 5 — Ion Channel Examples in Context

### Voltage-Gated Na⁺ Channel (Nav)

```
  Structure: single polypeptide, 4 homologous domains (I-IV)
  Selectivity: Na⁺ >> K⁺ (selectivity filter: DEKA ring)
  Activation: +30 mV → channels open in 0.1 ms
  Inactivation: fast inactivation within 1-2 ms (IFM motif)
  Recovery: -70 mV, 10-20 ms before next AP possible (refractory period)

  Pharmacology:
    TTX (tetrodotoxin): blocks pore from outside; 1 nM potency
    Local anesthetics: block from inside; state-dependent
    Batrachotoxin: prevents inactivation → sustained activation
```

### Potassium Channels

```
  KcsA (bacterial): first channel crystal structure (MacKinnon, Nobel 2003)
  → 2.0 Å resolution; revealed selectivity filter carbonyl caging of K⁺
  → 4 K⁺ sites; ions in S1-S2-S3-S4 positions
  → Concerted knock-on: ions jump 2 positions simultaneously

  Kir (inward rectifier):
  → Blocked by Mg²⁺ and polyamines from inside at positive potentials
  → Allows K⁺ in but not out at depolarized potentials
  → Sets resting potential in cardiomyocytes

  hERG (KCNH2 / Kv11.1):
  → Drug binding causes long-QT syndrome (arrhythmia)
  → ~200 drugs affect hERG: must screen all new drugs
```

---

## Electrical Engineering Bridges

Membrane biophysics is literally electrical engineering applied to a lipid dielectric. Every major concept maps one-to-one onto circuit theory.

```
  MEMBRANE BIOPHYSICS            ELECTRICAL ENGINEERING PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Lipid bilayer                  Capacitor: C_m ≈ 1 μF/cm² (dielectric =
                                 ~3 nm hydrocarbon core, ε ≈ 2). This is
                                 the correct formula: C = ε₀ε·A/d.
                                 Bilayer is a parallel-plate capacitor.

  Ion channel                    Conductance: g = 1/R (siemens). A single
                                 channel at 1-100 pS is a voltage-controlled
                                 resistor that switches between open (g > 0)
                                 and closed (g = 0) states.

  Nernst potential (E_ion)       Battery EMF: the concentration gradient
                                 across the membrane is a chemical potential
                                 difference — equivalent to an EMF source in
                                 series with the channel conductance.
                                 E_K ≈ -98 mV is the K⁺ battery voltage.

  Kirchhoff's current law        Hodgkin-Huxley master equation:
  at the membrane node           C_m·dV/dt = -Σ gᵢ(V - Eᵢ) + I_ext
                                 Sum of currents at a node = 0 (with the
                                 capacitive current as the displacement term).

  Cable equation (Kelvin, 1855)  Lossy transmission line (R-C ladder network):
  λ²∂²V/∂x² - τ_m ∂V/∂t = V    λ = sqrt(r_m/r_a) is the characteristic
                                 length of the cable; τ = r_m·c_m is the
                                 time constant. Myelination increases r_m
                                 (insulation) and decreases c_m → λ jumps
                                 to >> internode spacing → saltatory prop.

  Space clamp (whole-cell        Operational amplifier feedback control:
  voltage clamp)                 the patch clamp amplifier holds V_m at
                                 the command potential by injecting the
                                 exact compensating current — a virtual
                                 ground configuration.

  Helfrich bending energy        Beam theory (thin plate mechanics):
  F = ∫ κ/2·(c₁+c₂)²dA         κ is the bending stiffness, analogous to
                                 EI in structural mechanics. The 8πκ result
                                 (vesicle energy independent of radius) is
                                 a classic result in thin-shell theory.
  ──────────────────────────────────────────────────────────────────────
```

The Hodgkin-Huxley model (Module 05) is simply this equivalent circuit with nonlinear, voltage-dependent conductances. A neuron IS a nonlinear RC circuit driven by chemical batteries.

---

## Decision Cheat Sheet

| Question | Concept | Key Equation/Value |
|----------|---------|-------------------|
| Why is membrane resting potential ~-70 mV? | GHK equation; K⁺ dominant permeability | P_K >> P_Na at rest |
| What is the Nernst potential for K⁺ in a neuron? | E_K = (RT/F) ln([K]o/[K]i) | ≈ -98 mV |
| How fast do lipids diffuse laterally in a membrane? | 2D fluid diffusion | D ≈ 1-10 μm²/s (liquid crystalline) |
| What determines ion selectivity in K⁺ channels? | Selectivity filter geometry | TVGYG motif, 8-oxygen cage |
| Why can't a Na⁺ ion pass through a K⁺ channel? | Dehydration energy mismatch | Na⁺ can't shed hydration shell profitably |
| What makes patch clamp work at single-channel resolution? | Gigaseal | >1 GΩ seal, 0.1 pA noise floor |
| What energy is required to form a vesicle? | Helfrich elastic energy | 8πκ ≈ 500 k_BT (independent of radius) |
| What drives membrane curvature in endocytosis? | BAR domains, clathrin coat | Scaffold + amphipathic helix insertion |

---

## Common Confusion Points

**Nernst potential vs. resting potential.** The Nernst potential E_K is where the
K⁺ electrochemical gradient is zero — only K⁺ matters. The resting potential V_m
is the actual membrane voltage, set by all permeant ions weighted by their
permeabilities (GHK equation). V_m ≈ -70 mV is close to E_K (≈ -98 mV) because
K⁺ dominates, but offset because small Na⁺ permeability pulls it toward E_Na.

**K⁺ channels let K⁺ out, not in, at rest.** K⁺ is more concentrated inside than
outside, and V_m = -70 mV > E_K = -98 mV. The net driving force (V_m - E_K = +28 mV)
pushes K⁺ out of the cell. K⁺ efflux is what maintains the negative resting potential.
If K⁺ permeability suddenly increases (as in an action potential repolarization), K⁺
rushes out, hyperpolarizing the membrane.

**Selectivity filter selects K⁺ over Na⁺ despite K⁺ being larger.** The key is
dehydration energy. K⁺ (1.33 Å) fits precisely into the 4-carbonyl cage, perfectly
replacing its hydration waters. Na⁺ (0.95 Å) is too small to be properly caged —
it retains a partial hydration shell, costing more energy to enter than it gains
from electrostatic interactions inside. The filter geometry is tuned for K⁺.

**Bending energy is independent of vesicle radius.** This counterintuitive result
(F = 8πκ) means it costs the same energy to form a 20 nm or a 200 nm vesicle.
What differs is the membrane tension contribution (σ × 4πR²), which grows with R.
This is why cells regulate membrane tension independently of curvature machinery.

**"Lipid rafts" are controversial.** The DRM (detergent-resistant membrane) method
for isolating rafts is artifact-prone — cold detergent extraction can create Lo
domains that don't exist in the native warm membrane. Direct evidence for rafts
in living cells requires super-resolution microscopy. The concept is real; the
size, lifetime, and composition remain debated.
