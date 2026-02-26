# Single-Molecule Techniques — Optical Tweezers, AFM, FRET, Magnetic Tweezers

## The Big Picture

```
┌──────────────────────────────────────────────────────────────────────────┐
│              SINGLE-MOLECULE TECHNIQUE LANDSCAPE                          │
│                                                                            │
│  TECHNIQUE         WHAT IT MEASURES        FORCE RANGE   RESOLUTION      │
│  ─────────────     ────────────────────────────────────────────────────  │
│  Optical tweezers  Force, displacement      0.1-100 pN    0.1 nm, 0.1 pN │
│  Magnetic tweezers Force, extension, torque 0.01-100 pN   nm, 0.01 pN    │
│  AFM               Force, topography        10 pN-10 nN   0.1 nm, ~10 pN │
│  smFRET            Distance, dynamics       N/A           1-10 nm dist.  │
│  Patch clamp       Ion current              N/A           0.1 pA, 0.05 ms│
│                                                                            │
│  THE VALUE: ensemble methods give averages;                               │
│  single-molecule methods reveal:                                          │
│    • Distributions (not just means)                                       │
│    • Rare intermediates hidden in ensemble average                        │
│    • Individual conformational states                                     │
│    • Real-time trajectories of individual molecules                       │
│    • Stochastic switching between states                                  │
│    • Heterogeneity that ensemble would average away                       │
└──────────────────────────────────────────────────────────────────────────┘
```

---

## Section 1 — Optical Tweezers

### Physical Basis

A tightly focused laser beam creates a three-dimensional light trap for
micron-scale dielectric objects:

```
  TRAPPING MECHANISM (geometric optics, r >> λ):

  Refraction at bead surface redirects photons → momentum transfer to bead
  For bead displaced from focus:
    Rays refracted unequally → net force toward focus (gradient force)
    Net: restoring force F ∝ -x  (harmonic potential near focus)

  Exact treatment (Mie/Rayleigh theory for r ≈ λ or r << λ):
    Gradient force: F_grad ∝ ∇|E|² → toward intensity maximum
    Scattering force: F_scat ∝ I → along beam axis (must balance)
    Trapping: high-NA objective (NA > 1.2) → axial gradient > scattering

  Typical parameters:
    Laser: 1064 nm Nd:YAG or 800 nm Ti:Sapphire (biologically inert wavelengths)
    Trap stiffness: k = 0.001-1 pN/nm (depends on bead size, laser power)
    Bead diameter: 0.5-5 μm (polystyrene or silica)
```

### Calibration

The trap is a spring (F = -kx) whose stiffness must be calibrated:

```
  METHOD 1: Equipartition theorem
    ½k⟨x²⟩ = ½k_BT   →   k = k_BT / ⟨x²⟩
    Measure variance of Brownian fluctuations → get spring constant
    Advantage: no external calibration needed
    Disadvantage: depends on accurate position measurement bandwidth

  METHOD 2: Power spectrum (Lorentzian fit)
    Trapped bead PSD: S(f) = k_BT/(π²γ) × 1/(f_c² + f²)
    Corner frequency: f_c = k/(2πγ)  where γ = 6πηr (Stokes drag)
    Fit Lorentzian → f_c → k
    Advantage: rigorously correct, frequency-domain, noise-robust
    This is the standard method

  METHOD 3: Stokes drag force
    Move the stage at velocity v → drag force F = γv
    Displacement x = F/k → k from known drag
    Advantage: checks calibration dynamically
```

### Force-Extension Curves: DNA Mechanics

DNA is the classic test system. Stretching a single DNA molecule with optical
tweezers reveals its elastic properties:

```
  FORCE-EXTENSION REGIMES:

  F (pN)
   100 ├────────────────────────────── contour length (inextensible)
       │                              (overstretching > 65 pN)
    10 ├──────────────    WLC regime: F ≈ (k_BT/Lp)×[1/(4(1-x/L)²) - 1/4 + x/L]
       │         ─────                WLC = worm-like chain
     1 ├─────────                     Lp = 50 nm (persistence length)
       │         entropic             L = contour length
   0.1 ├ ─────── (Gaussian)          x = end-to-end distance
       └────────────────── extension (L fraction)
       0                1

  Key parameters:
    Persistence length Lp = 50 nm (DNA)
    Contour length L = 0.34 nm/bp × N (bp)
    Torsional stiffness C ≈ 110 nm (twist persistence length)

  Overstretching at 65 pN: B-DNA → S-DNA transition
  (strand separation or strand switching, still debated)
```

### Single-Molecule Motor Measurements

For kinesin stepping (see also 06-MOLECULAR-MOTORS.md):

```
  Setup: kinesin attached to bead; bead in trap; MT below
         (dumbbell assay: bead-kinesin-MT-kinesin-bead more symmetric)

  Position-clamp (force clamp):
    Feedback: stage moves to keep bead at fixed distance from trap center
    → constant load F applied to motor
    → measure velocity vs. F directly

  Position-detection:
    Back focal plane interferometry: position resolution 0.3 nm at 10 kHz
    Laser back-scattered into quadrant photodiode or CMOS camera
    8-nm steps clearly visible in position trace vs. time

  From stepping data:
    Step size distribution → mechanical coupling
    Dwell time distribution → kinetics (rate constants)
    Randomness r = Var(steps)/Mean(steps) → mechanism (r=1 for single rate-lim.)
```

---

## Section 2 — Atomic Force Microscopy (AFM)

### Physical Basis

A sharp tip mounted on a flexible cantilever scans a surface or is pressed
onto it. Force is detected by cantilever deflection:

```
  CANTILEVER PHYSICS:

  Spring constant k_cantilever:
    k = Et³w / (4L³)   (E = Young's modulus, t=thickness, w=width, L=length)
    Typical: k = 0.01-10 N/m  (tuned to application)

  Deflection detection:
    Laser reflects off back of cantilever → position-sensitive detector
    Sensitivity: sub-Å deflection measurable
    Force resolution: δF = sqrt(4kk_BT Δf) (thermal noise floor)
    At k = 0.01 N/m, Δf = 100 Hz, T = 300 K:
    δF = sqrt(4 × 0.01 × 4.1×10⁻²¹ × 100) ≈ 40 fN rms

  AFM modes:
    Contact mode: tip in contact, measure deflection at constant force
    Tapping mode (intermittent): oscillate cantilever, measure amplitude
    Force spectroscopy: extend/retract, record force vs. distance
```

### AFM Force Spectroscopy: Protein Unfolding

Pulling a protein between tip and surface while retracting:

```
  FORCE EXTENSION CURVE (titin, a muscle protein with tandem Ig domains):

  Force
    │           *               *               *
    │          /|              /|              /|
    │    WLC  / |        WLC  / |        WLC  / |  sawtooth pattern
    │   ─── /  |        ─── /  |        ─── /  |
    │       /   | unfold     /   | unfold     /   | unfold
    │      /    │           /    │           /    │  peak ≈ 100-300 pN per domain
    │─────/     v          /     v          /     v
    └──────────────────────────────────────────── extension
                ↑                ↑                ↑
            domain 1          domain 2          domain 3
            unfolds           unfolds           unfolds

  Each peak: force needed to mechanically unfold one domain
  Contour between peaks: WLC extension of newly unfolded polypeptide
  Information: unfolding force, unfolding pathway, mechanical stability

  Loading rate dependence (Bell model):
    Peak force F* = (k_BT/x_u) × ln(r × x_u / (k_BT × k_off°))
    r = loading rate [pN/s], x_u = transition state distance, k_off° = off rate
    → vary loading rate → extract energy barrier landscape
```

### AFM Imaging

In imaging mode, AFM provides topographic maps of surfaces:

```
  Lateral resolution: ~1-5 nm (limited by tip radius, ~5-20 nm)
  Vertical resolution: <0.1 nm (Å-level)
  Can image: DNA, protein complexes, membranes, virus capsids
  In liquid: proteins remain native and functional

  Advantage over EM: can image in buffer (no staining/vitrification)
  Limitation: slower than EM (minutes per image); tip artifacts;
              limited to surfaces

  High-speed AFM (Ando group): 10-100 ms per frame
  → Watch conformational changes in real time
  → E.g.: myosin V walking on actin, GroEL-GroES cycling
```

---

## Section 3 — FRET: Fluorescence Resonance Energy Transfer

### Physical Basis: Förster Theory

FRET is non-radiative energy transfer from donor fluorophore to acceptor
fluorophore via dipole-dipole coupling:

```
  Transfer rate: k_T = (1/τ_D) × (R₀/r)⁶

  τ_D = donor excited-state lifetime (in absence of acceptor)
  r = donor-acceptor distance
  R₀ = Förster radius (distance at 50% transfer efficiency)

  Efficiency: E = 1 / (1 + (r/R₀)⁶)  ← the working equation

  R₀ = 0.211 × [κ² n⁻⁴ Q_D J(λ)]^(1/6)   (in nm)
    κ² = orientation factor (2/3 for random; 1-4 for fixed)
    n = refractive index of medium (~1.33)
    Q_D = donor quantum yield
    J(λ) = spectral overlap integral

  Typical R₀ values: 2-8 nm for common FRET pairs
  Sensitive range: ~0.5-2 × R₀ = 1-16 nm for most pairs

  FRET pairs (common):
    Cy3/Cy5:  R₀ ≈ 5 nm
    CFP/YFP:  R₀ ≈ 5.5 nm
    Alexa488/Alexa594: R₀ ≈ 6 nm
```

The (r/R₀)⁶ dependence: extremely steep. A 10% change in r gives a ~77% change
in k_T at r = R₀. This makes FRET a very sensitive "molecular ruler" but only
over a narrow range.

### Single-Molecule FRET (smFRET)

Surface-immobilized or diffusing individual molecules observed by:

```
  TIRF (Total Internal Reflection Fluorescence):
    Evanescent field illuminates only ~200 nm above surface
    → selectively excites surface-immobilized molecules
    → rejects background fluorescence from bulk
    → enables single-molecule detection

  smFRET measurement:
    Donor: excited by laser
    Acceptor: excited by FRET when close to donor
    E = I_A / (I_A + I_D)   (intensity ratio)

  Time trace of E reveals:
    → Static FRET: one population → fixed distance
    → Dynamic FRET: switching between E values → conformational dynamics
    → Distribution of E values: multiple conformations
    → Transition rates between states: kinetics
```

### smFRET Applications

```
  ┌────────────────────────────────────────────────────────────────────┐
  │  APPLICATION            │  WHAT FRET REVEALS                       │
  │  ─────────────────────  │  ──────────────────────────────────────  │
  │  Protein folding        │  Compact vs. extended ensemble           │
  │                         │  Folding intermediates                   │
  │  Enzyme conformational  │  Open/closed active site dynamics        │
  │  dynamics               │  Substrate-induced conformational change │
  │  RNA/DNA junction       │  Junction dynamics, strand invasion      │
  │  dynamics               │  Holliday junction switching             │
  │  Ribosome translation   │  tRNA movement, translocation steps      │
  │  DNA repair             │  Sliding, searching along DNA            │
  │  Molecular motors       │  Head coordination in kinesin            │
  └────────────────────────────────────────────────────────────────────┘
```

---

## Section 4 — Magnetic Tweezers

### Physical Basis

Magnetic beads (superparamagnetic) are attracted toward magnetic field maxima:

```
  Force on bead: F = (χ_V × V) × ∇(B²) / (2μ₀)

  χ_V = volume magnetic susceptibility
  V = bead volume
  B = magnetic field magnitude

  Adjusting magnet height → adjust force (0.01-100 pN range)
  Rotating magnets → apply torque to bead → twist DNA/protein

  Advantages vs. optical tweezers:
    → Torque application (twist and stretch)
    → Many molecules in parallel (field-of-view measurement)
    → No photodamage (no laser on sample)
    → Direct force control (no feedback needed for fixed force)
    → Naturally applied to DNA topology studies

  Disadvantages:
    → Force less precisely calibrated than optical tweezers
    → Slower position readout (camera-based, ~60 Hz)
    → Cannot rapidly switch force
```

### DNA Topology Experiments

Magnetic tweezers are uniquely suited to studying DNA supercoiling:

```
  EXPERIMENT:
    One DNA end tethered to surface; other end to magnetic bead
    Rotate magnet → bead rotates → twist DNA
    Measure extension vs. number of turns (linking number change ΔLk)

  RESULTS:
    Positive supercoiling: writhe accumulates → DNA shortens
    Negative supercoiling: same, with denaturation bubbles
    Plectonemes form above critical supercoiling density

  APPLICATIONS:
    Topoisomerase activity: watch relaxation of supercoiling
    Helicase unwinding: watch extension changes
    DNA-binding protein: observe changes in effective twist
    Nucleosome assembly/disassembly: extension changes

  Torque measurement:
    From angular diffusion: τ = k_BT × ∂(ln P)/∂θ
    Or: torque fluctuation analysis
```

---

## Section 5 — Comparing Techniques

### What Each Technique Can and Cannot Do

```
┌──────────────────────────────────────────────────────────────────────────┐
│  TECHNIQUE     │  FORCE    │  DIST.   │  TORQUE │  IMAGING │  THROUGHPUT│
│  ─────────────  │  RANGE    │  RES.    │         │          │            │
│  Optical        │  0.1-100pN│  0.1 nm  │  No*    │  No       │  1 at a    │
│  tweezers       │           │          │         │          │  time      │
│  Magnetic       │  0.01-100 │  nm      │  Yes    │  No       │  Many      │
│  tweezers       │  pN       │          │         │          │  (parallel)│
│  AFM            │  10pN-10  │  0.1 nm  │  No     │  Yes      │  1 at a    │
│                 │  nN       │          │         │          │  time      │
│  smFRET         │  None     │  1-10 nm │  No     │  Yes (2D) │  100s      │
│                 │           │  (coarse)│         │  (position│  (parallel)│
│                 │           │          │         │  only)   │            │
│  Patch clamp    │  None     │  None    │  No     │  No       │  1-10      │
│  (ion channels) │  (current)│  (current│         │          │  cells     │
└──────────────────────────────────────────────────────────────────────────┘
*Dual-beam optical tweezers can apply torque via birefringent particles
```

### When to Use Which Technique

```
  ┌───────────────────────────────────────────────────────────────┐
  │  QUESTION                           │  BEST TECHNIQUE         │
  │  ─────────────────────────────────  │  ─────────────────────  │
  │  Motor step size & stall force      │  Optical tweezers       │
  │  Protein unfolding force/pathway    │  AFM force spectroscopy │
  │  DNA supercoiling, topo enzymes     │  Magnetic tweezers      │
  │  Conformational dynamics (nm scale) │  smFRET                 │
  │  Distance between two labeled sites │  smFRET                 │
  │  Surface topography, membrane struct│  AFM imaging            │
  │  DNA mechanics, WLC parameters      │  Optical tweezers       │
  │  Single ion channel conductance     │  Patch clamp            │
  │  Parallel throughput, many molecules│  smFRET or Mag tweezers │
  │  In-cell dynamics (FCS, SPT)        │  Fluorescence + camera  │
  └───────────────────────────────────────────────────────────────┘
```

---

## Section 6 — Key Technical Challenges

### Drift and Noise

```
  NOISE SOURCES IN OPTICAL TWEEZERS:
    Brownian motion of bead: dominant noise source
    Thermal noise floor: σ_x = sqrt(k_BT/k_trap)
      For k_trap = 0.1 pN/nm: σ = sqrt(4.1 pN·nm / 0.1 pN/nm) = 6.4 nm rms

    Instrument drift: thermal expansion of optics/stage
    → typically 1-10 nm/min → limit long-duration experiments
    → controlled by temperature stabilization, differential measurement

  FRET CHALLENGES:
    Photobleaching: fluorophores bleach after ~10⁶-10⁷ photons
    → limits observation time to ~1-100 s per molecule
    Blinking: fluorophores stochastically dark for ms-s
    → confounds dynamics measurement
    Labeling efficiency: must achieve >90% double-labeling for smFRET
    Immobilization artifacts: surface quenching, restricted diffusion
```

### Surface Chemistry

All surface-based techniques require attaching molecules to surfaces without
perturbing their function:

```
  COMMON STRATEGIES:
    PEG (polyethylene glycol) passivation: prevents non-specific adsorption
    Biotin-streptavidin: strong (Kd ~ 10⁻¹⁵ M) oriented attachment
    His-tag/Ni-NTA: reversible attachment, site-specific
    DNA handles: attach molecular machine to bead via DNA tether
    NHS-ester chemistry: covalent attachment at Lys residues (not site-specific)

  Surface effects to control:
    Non-specific adsorption: protein sticking to surface in wrong orientation
    Restricted diffusion: molecule tethered too tightly cannot function
    Surface-induced conformational changes: hydrophobic surfaces denature proteins
```

---

## Signal Processing, Control, and Metrology Bridges

Single-molecule experiments are precision measurement instruments. Every design decision maps onto classical signal processing and control systems theory.

```
  SINGLE-MOLECULE TECHNIQUE     SIGNAL PROCESSING / CONTROL PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Optical trap SNR and          SNR = signal / noise floor:
  detection limits              thermal noise floor σ_x = sqrt(k_BT/k_trap)
                                (equipartition). At k = 0.1 pN/nm:
                                σ = 6.4 nm rms. To resolve 8 nm kinesin
                                steps, need k_trap >> k_BT/(8 nm)² ≈ 0.06
                                pN/nm. Detection bandwidth (10 kHz for
                                motor experiments) sets Nyquist limit.

  Force clamp (position clamp)  PID feedback control loop:
                                The stage servo moves to hold bead at
                                fixed displacement from trap center →
                                constant applied force. The feedback
                                bandwidth must be > step rate (100 Hz for
                                kinesin) to faithfully follow motor steps.
                                Overshoot → force artifacts; underdamped
                                response → ringing on step detection.

  Trap stiffness calibration    Metrology: two independent methods
  (equipartition + power        (equipartition and Lorentzian fit) must
  spectrum + Stokes drag)       agree within calibration error. The
                                Lorentzian fit is the more robust method
                                because it detects bandwidth artifacts
                                directly from the corner frequency shape.
                                This is exactly calibration traceability
                                in metrology.

  FRET efficiency E = 1/(1+(r/R₀)⁶)  Nonlinear distance sensor with
                                strong sensitivity in the 0.5-2×R₀ range.
                                The 1/r⁶ dependence is a very steep transfer
                                function — useful for detecting small
                                distance changes near R₀ but poor outside
                                this range. Analogous to a log-scale sensor.

  Magnetic tweezers torque      Torsional mechanics: rotating magnets apply
  (DNA supercoiling)            a torque τ = dF/dθ to the bead. Extension
                                vs. turns experiments measure the writhe
                                compliance of DNA — directly analogous to
                                measuring torsional spring constant of a
                                physical shaft.

  Photobleaching as clock       Single-step photobleaching is a stochastic
                                process (exponential lifetime) used to count
                                labeled molecules (1 step = 1 molecule,
                                2 steps = 2, etc.) — discrete counting
                                statistics.
  ──────────────────────────────────────────────────────────────────────
```

**The fundamental challenge**: every single-molecule measurement is dominated by thermal noise at the relevant scale. The experimenter's job is to design feedback systems and calibration protocols that separate signal from noise — the same challenge as any precision measurement system operating near its noise floor.

---

## Decision Cheat Sheet

| Goal | Best technique | Key parameter |
|------|---------------|---------------|
| Measure motor step size | Optical tweezers | 0.3 nm spatial resolution at 10 kHz |
| Protein mechanical unfolding | AFM force spectroscopy | Load spring constant k ~ 10-100 pN/nm |
| DNA topology, supercoiling | Magnetic tweezers | Rotational control |
| Conformational switching (< 10 nm) | smFRET | Förster radius R₀ ~ 5 nm pair |
| Many molecules in parallel | Magnetic tweezers or smFRET | Wide-field camera |
| Real-time protein dynamics on surface | HS-AFM | 10-100 ms/frame |
| Trap calibration (accurate stiffness) | Lorentzian power spectrum | Corner frequency f_c |
| Distance between two labeled sites | smFRET | E = 1/(1+(r/R₀)⁶) |

---

## Common Confusion Points

**FRET distance is not a ruler between atom positions.** FRET gives an apparent
distance between the fluorophore attachment points, averaged over the donor
excited-state lifetime (~ns). The dye linker (~5-15 Å) introduces uncertainty
on top of the distance measurement uncertainty. FRET distances ≠ crystal structure
interatomic distances. They are nevertheless precise reporters of relative changes
in distance (conformational changes) even when absolute calibration is uncertain.

**Equipartition calibration gives k, not absolute position.** The equipartition
theorem method determines the trap spring constant from Brownian fluctuations.
It requires the position detection to faithfully report displacements at all
relevant frequencies (no filtering artifacts). The power spectrum method is more
robust because it detects bandwidth artifacts directly.

**Optical tweezers don't directly measure force.** They measure bead displacement
from trap center, then calculate F = k × x. Force is derived, not directly
measured. Calibration errors in k propagate directly to force errors. This is
why force clamp experiments (constant displacement) are cleaner than calculating
force from position.

**Magnetic tweezers apply tension, not extension.** Magnetic tweezers control
force by adjusting magnet height; extension is the result. Optical tweezers
can control either force or extension (with appropriate feedback). This distinction
matters for interpreting force-extension curves: in magnetic tweezers, you set F
and observe x; in optical tweezers, you can set either.

**smFRET "efficiency" is not a quantum yield.** FRET efficiency E is the fraction
of photons transferred from donor to acceptor, not the quantum yield of emission.
E = 1 means all donor excitation energy transferred to acceptor (maximum FRET,
minimum distance). E = 0 means no transfer (large distance). In practice,
corrections for direct acceptor excitation, gamma factor (detection efficiency
ratio), and crosstalk are needed for quantitative E values.
