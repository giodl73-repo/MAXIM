# Ceramics and Composites

## The Big Picture

```
CERAMICS & COMPOSITES LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  CERAMICS                                COMPOSITES
  ─────────────────────────────────────   ─────────────────────────────────────
  Inorganic, non-metallic solids          Two or more distinct phases combined
  Ionic-covalent bonding                  to exploit each component's strengths
  High T_melt, extreme hardness           (neither phase alone achieves the
  Brittle — no dislocation glide          combination of properties)

  Crystal structure drives properties:    Classification by reinforcement:
    rocksalt, fluorite, perovskite,        Particle: particulate reinforced
    corundum — each with distinct          Fiber: unidirectional, woven, braided
    electrical / thermal / optical         Laminate: stacked plies (CFRP)
    characteristics                        Sandwich: face sheets + low-density core

  KEY CERAMICS BY FUNCTION:               KEY COMPOSITES BY MATRIX:
  Al₂O₃  → substrate, wear, insulation   Thermoset + CFRP → aerospace structure
  ZrO₂   → thermal barrier, toughened    Thermoplastic + CFRP → recyclable aero
  SiC    → power electronics, armor      Metal matrix (MMC) → high-T structure
  Si₃N₄  → bearings, turbocharger        Ceramic matrix (CMC) → jet engine hot section
  BaTiO₃ → capacitors, piezo, sensors    Concrete → civil (oldest composite)
  YBCO   → superconductor (77K HTS)

  ASHBY MAP POSITION:
  Ceramics: upper-right (high E, low ρ, high T_melt, HIGH K_Ic-1 = brittle)
  Composites: upper-left (high E, low ρ — the "aerospace sweet spot")
```

---

## Part 1: Ceramics

### Bonding and Why Ceramics Are Brittle

```
  BONDING IN CERAMICS
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Ionic bonding (MgO, NaCl): electrostatic attraction of opposite ions  │
  │    → high melting point, electrically insulating, cleavage along       │
  │    crystallographic planes (charge neutrality must be maintained)       │
  │                                                                          │
  │  Covalent bonding (SiC, Si₃N₄, diamond): shared electron pairs        │
  │    → extremely strong, directional; highest hardness and T_melt         │
  │    → even more brittle than ionic ceramics                              │
  │                                                                          │
  │  Most ceramics: mix of ionic + covalent (Al₂O₃ ~60% ionic/40% covalent)│
  └─────────────────────────────────────────────────────────────────────────┘

  WHY NO PLASTIC DEFORMATION:
  In metals:    dislocations glide on {111}⟨110⟩ slip systems
                → yield before fracture; tough

  In ceramics:  Slip would require moving like-charged ions adjacent to
                each other → electrostatic repulsion is enormous energy barrier
                Result: no dislocation glide at room temperature
                → crack propagates before any plastic zone can form
                → fracture toughness K_Ic = 1–5 MPa√m vs steel ~50 MPa√m
```

### Crystal Structures of Key Ceramics

```
  STRUCTURE         EXAMPLES              APPLICATIONS / DISTINCTIVE PROPERTY
  ─────────────────────────────────────────────────────────────────────────────
  ROCKSALT (NaCl)   MgO, NiO, FeO        Refractory linings; MgO: T_melt=2852°C
  Coordination 6:6  CaO, CoO             Simple cubic cation lattice in FCC anion

  FLUORITE (CaF₂)   ZrO₂, CeO₂, ThO₂   ZrO₂: thermal barrier coatings (TBC)
  Coordination 8:4  UO₂ (nuclear fuel)   CeO₂: solid oxide fuel cell electrolyte
  FCC cation, all                         High O²⁻ ion conductivity (vacancies)
  tetrahedral holes
  filled with anion

  PEROVSKITE (ABO₃) BaTiO₃, SrTiO₃     FERROELECTRIC: spontaneous polarization
  Ferroelectricity arises from a structural phase transition (cubic → tetragonal
  at the Curie temperature T_c) where the B-site cation (Ti⁴⁺ in BaTiO₃) displaces
  off-center, breaking inversion symmetry → permanent electric dipole per unit cell.
  This is a Landau second-order transition: F = a(T-T_c)P² + bP⁴ + ... with order
  parameter P = polarization. Above T_c: paraelectric (cubic, centrosymmetric).
  Below T_c: ferroelectric (tetragonal, polar). Domains form to minimize depolarization energy.
  B-site in center  PbZrO₃, PbTiO₃      BaTiO₃: ~1000 MLCCs in every smartphone
  of BO₆ octahedron PZT (PbZr₁₋ₓTiₓO₃) PZT: piezoelectric actuators/sensors
  A-site at corners LaAlO₃, SrRuO₃      SrTiO₃: high-κ dielectric, substrate
                    YBCO (distorted)      LaAlO₃: gate dielectric, 2DEG at LAO/STO

  CORUNDUM (Al₂O₃)  Al₂O₃ (sapphire)    Substrate for LEDs, SiC wafers
  HCP O²⁻; Al³⁺     α-Fe₂O₃, Cr₂O₃    Watch crystals; scratch-resistant windows
  in 2/3 of         Ti-doped → ruby      Alumina: wear parts, electrical insulators
  octahedral sites   Cr-doped → ruby
                     Fe+Ti → sapphire

  WURTZITE           ZnO, AlN, GaN       GaN: power electronics and LEDs
  Hexagonal, close   SiC (α form)        AlN: high-κ substrate (κ = 320 W/mK!)
  to HCP                                 ZnO: piezoelectric, TCO (transparent)
```

### Key Ceramic Materials

| Material | T_melt (°C) | Hardness (GPa Vickers) | κ (W/mK) | Key use |
|----------|------------|----------------------|---------|---------|
| Diamond (C) | 3550 | ~100 | 2000 | Cutting, heat spreader |
| SiC | 2730 (dec) | 28 | 120–490 | Power electronics, armor, abrasive |
| Si₃N₄ | 1900 (dec) | 15–17 | 20–30 | Bearing balls, turbocharger rotors |
| Al₂O₃ | 2054 | 15–20 | 30 | IC substrates, wear, insulation |
| ZrO₂ (cubic) | 2715 | 12 | 2–3 | TBC (low κ desired for TBC) |
| MgO | 2852 | 7 | 55 | Refractory, nuclear, IR windows |
| BaTiO₃ | 1625 | 6 | 6 | MLCC, piezo, non-linear optics |
| YBCO | ~1000 (decomp) | — | ~4 | High-Tc superconductor |
| AlN | 2200 | 12 | 320 | LED substrate, power module |

### Fracture Mechanics

```
  GRIFFITH CRITERION — crack propagation condition:

  σ_f = √(2Eγ / πa)

  where: σ_f = fracture stress
         E   = Young's modulus
         γ   = surface energy (energy to create two fracture surfaces)
         a   = half-length of largest crack/flaw

  Physical meaning: crack of length 2a acts as a stress concentrator.
  When stress intensity exceeds surface energy cost to extend crack → fracture.

  ┌─────────────────────────────────────────────────────────────────────────┐
  │  STRESS INTENSITY FACTOR:  K_I = σ√(πa) · Y  (Y = geometry factor)    │
  │  Fracture when: K_I ≥ K_Ic  (fracture toughness, material property)   │
  │                                                                          │
  │  Material    K_Ic (MPa√m)   Implication                                │
  │  Glass           0.7        Shatters at any crack                       │
  │  Al₂O₃          3–5        Better but still brittle                    │
  │  Si₃N₄          5–8        Best monolithic ceramic                     │
  │  SiC             3–5        Hard but brittle                            │
  │  t-ZrO₂          7–15       Toughened (transformation mechanism)        │
  │  Steel (4340)   50–100      Ductile — enormous comparison               │
  │  CFRP            25–45      Composite — tough via fiber bridging        │
  └─────────────────────────────────────────────────────────────────────────┘

  WEIBULL STATISTICS — ceramics fail at a distribution of stresses
  (not a single yield point like metals)

  P_f(σ) = 1 - exp[-(σ/σ₀)^m]   (probability of failure at stress σ)

  m = Weibull modulus:
    m = 5–10: typical ceramic (high variability — design at 99.9% survival)
    m = 20:   good engineering ceramic (more uniform flaw distribution)
    m = 100:  structural steel (essentially deterministic)

  Engineering implication: Never use a single "strength" value for ceramic
  design. Use Weibull statistics to set design allowables at target reliability.
```

### Transformation Toughening in ZrO₂

```
  ZIRCONIA POLYMORPHS:
  Temperature:  >2370°C     1170–2370°C    <1170°C (RT)
  Phase:        Cubic  ──→  Tetragonal ──→ Monoclinic
  Volume change on t→m transition: +3–5% expansion

  TOUGHENING MECHANISM:
  Metastable tetragonal particles dispersed in matrix
       │
       │  Crack tip advances → stress field
       │
       ▼
  Stress-induced t→m transformation at crack tip
       │
       ▼
  Volume expansion COMPRESSES crack tip → crack must do extra work to advance
  → K_Ic increases from ~3 MPa√m (pure ZrO₂) to 7–15 MPa√m (t-ZrO₂)

  Stabilizers:  Y₂O₃ (3 mol% → partially stabilized zirconia, PSZ)
                CeO₂  (Ce-TZP: highest toughness, ~20 MPa√m)
                MgO, CaO (fully stabilized cubic → ionic conductor, no toughening)

  8YSZ (8 mol% Y₂O₃, cubic): TBC on turbine blades — LOW κ = 2.3 W/mK (desired)
  3YSZ (TZP): dental crowns, ceramic knives — HIGH toughness (structural)
```

### Processing

```
  PROCESSING ROUTE           CONDITIONS / NOTES
  ──────────────────────────────────────────────────────────────────────────
  Powder synthesis           Sol-gel, co-precipitation, spray drying,
                             Pechini method (solution → calcine → powder)

  Powder compaction          Uniaxial die pressing (simple shapes)
                             Cold isostatic pressing (CIP): uniform density

  Sintering                  Solid-state diffusion; T = 0.5–0.8 × T_melt
  (densification)            Shrinkage ~15–20% linear
                             Atmosphere: air, N₂, H₂ for SiC/Si₃N₄

  Hot pressing (HP)          Uniaxial pressure + heat; near theoretical density
                             More expensive, limited to simple shapes

  Hot isostatic pressing     HIP: pressure from all sides; near-perfect density
  (HIP)                      Used for turbine blades, medical implants

  Chemical vapor dep (CVD)   SiC fiber coating, diamond films, Si₃N₄ coatings
  Reaction bonding           Si + C → SiC in situ; no shrinkage (net-shape)
  Sol-gel                    Metal alkoxide hydrolysis → oxide gel → ceramic
```

---

## Part 2: Composites

### Classification and Architecture

```
  COMPOSITE CLASSIFICATION
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  BY REINFORCEMENT GEOMETRY:                                             │
  │                                                                          │
  │  Particle-reinforced:     WC-Co (cemented carbide); SiC/Al MMC          │
  │  (isotropic, low cost)    Al₂O₃ particles in polymer; concrete          │
  │                                                                          │
  │  Short fiber / whisker:   Chopped CFRP; glass-filled nylon              │
  │  (quasi-isotropic in 2D)  SiC whisker reinforced Al₂O₃; TiB₂/Ti        │
  │                                                                          │
  │  Continuous fiber UD:     CFRP prepreg unidirectional ply               │
  │  (max stiffness along UD) High E and σ in fiber direction, low ⊥        │
  │                                                                          │
  │  Woven fabric:            ±45°, 0/90° weave patterns                    │
  │  (balanced in-plane)      Plain, twill, satin weave architectures        │
  │                                                                          │
  │  Laminate:                Multiple UD plies at different angles stacked  │
  │  (engineered anisotropy)  Quasi-isotropic: [0/±45/90]_s                 │
  │                           Tailored for load path                         │
  │                                                                          │
  │  Sandwich:                CFRP face sheets + Nomex honeycomb core        │
  │  (high flexural rigidity  Flexural stiffness ∝ (thickness)³             │
  │  at low areal density)    Floor panels, racing car tubs                  │
  └─────────────────────────────────────────────────────────────────────────┘
```

### Rule of Mixtures

```
  LONGITUDINAL MODULUS (fiber direction — Voigt model):
  E_c = V_f · E_f + V_m · E_m = V_f · E_f + (1-V_f) · E_m

  Physical picture: fibers and matrix in PARALLEL → share strain equally
  Fiber dominates (E_f >> E_m typically)

  TRANSVERSE MODULUS (perpendicular to fibers — Reuss model):
  1/E_c⊥ = V_f/E_f + V_m/E_m

  Physical picture: fibers and matrix in SERIES → share stress equally
  Matrix dominates → much lower than longitudinal

  Example: CFRP with V_f = 0.6, E_f = 230 GPa (IM carbon), E_m = 3.5 GPa (epoxy)
  E_c∥  = 0.6×230 + 0.4×3.5 = 138 + 1.4 = 139.4 GPa   (compare: steel = 200 GPa)
  E_c⊥  = 1/(0.6/230 + 0.4/3.5) = 1/(0.0026 + 0.114) = 8.5 GPa

  This 16:1 anisotropy ratio (139 vs 8.5 GPa) is why laminates are designed
  with fibers along all significant load paths.

  STRENGTH (longitudinal, fiber-dominated):
  σ_c∥ = V_f · σ_f + V_m · σ_m*
  where σ_m* = matrix stress at fiber failure strain

  DENSITY:
  ρ_c = V_f · ρ_f + V_m · ρ_m   (exact — no approximation needed)
```

### Fiber Types

```
  FIBER         E (GPa)  σ_uts (GPa)  ρ (g/cm³)  Notes
  ─────────────────────────────────────────────────────────────────────────────
  HS Carbon     230      3.5–4.5      1.76        Standard aerospace/sporting
  (IM6, T700)
  HM Carbon     400–600  2.5–3.5      1.8–2.0     High modulus; stiffer but
  (M60J, M55J)                                    lower strength; satellite structure
  UHM Carbon    800+     2.0          2.1         Ultra-high modulus; niche
  E-Glass       72       3.4          2.56        Low cost, isotropic; boat hulls,
                                                   wind turbine blades, insulation
  S-Glass       87       4.6          2.48        Higher performance, more expensive
  Aramid        80–130   3.6          1.45        Kevlar: high toughness, low ρ
  (Kevlar 49)                                     Poor compression strength
  Boron         400      3.6          2.5         Original USAF stealth; expensive
  SiC (fiber)   200–400  3.0          2.5–3.2     CMC fiber; high-T retention
  Basalt        90       4.8          2.7         Low cost, fire resistant
  ─────────────────────────────────────────────────────────────────────────────
  Specific modulus (E/ρ): HS Carbon ≈ 131 GPa·cm³/g vs Steel ≈ 26 GPa·cm³/g
  → Carbon fiber is ~5× stiffer per unit mass than steel
```

### Matrix Systems

```
  THERMOSET MATRICES (cure = irreversible chemical crosslink)
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Epoxy: most common; T_g up to 180°C; excellent adhesion; 120°C cure    │
  │  Phenolic (BMI): fire resistant, low smoke; aircraft interiors          │
  │  Cyanate ester: low dielectric loss; radomes, electronics               │
  │  PEKK/PEEK thermoset: high-T capability (T_g > 200°C)                   │
  │  Disadvantage: cannot remelt/recycle; cure shrinkage; pot life          │
  └──────────────────────────────────────────────────────────────────────────┘

  THERMOPLASTIC MATRICES (no cure — melt and solidify)
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  PEEK: T_g = 143°C, T_melt = 343°C; excellent chemical resistance       │
  │  PEKK: T_g = 160°C; slightly better than PEEK, more processable         │
  │  PPS: lower cost, T_melt = 285°C; automotive, oil & gas                 │
  │  LMPAEK: lower melt temp than PEEK — easier processing                  │
  │  Advantages: recyclable; weldable (resistance/induction/ultrasonic);     │
  │  no cure; no pot life; fast consolidation; impact resistant              │
  │  Disadvantage: higher processing temp/pressure; fiber impregnation hard │
  └──────────────────────────────────────────────────────────────────────────┘

  CERAMIC MATRIX COMPOSITES (CMC)
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  SiC/SiC: SiC fibers in SiC matrix; T_use to 1400°C                    │
  │  C/SiC, C/C: carbon fibers in SiC or carbon matrix; >1600°C (inert atm)│
  │  Application: GE LEAP engine fan blades, turbine stage 1 shrouds        │
  │  Benefit: 25% lower density than Ni-superalloy → higher bypass ratio    │
  │  BN interphase coating: weak fiber-matrix bond → crack deflection,       │
  │  not through-fiber fracture → pseudo-ductility                          │
  └──────────────────────────────────────────────────────────────────────────┘
```

### Interface and Failure Mechanics

```
  FIBER-MATRIX INTERFACE FUNCTIONS:
  1. Stress transfer from matrix to fiber (load-bearing function)
  2. Protect fiber from environment (chemical barrier)
  3. Control crack propagation mode (tough vs. strong interface tradeoff)

  INTERFACE STRENGTH TRADEOFF:
  Strong interface: good stress transfer, high tensile strength
                   BUT crack runs straight through (brittle fracture mode)
  Weak interface:  crack deflects along fiber-matrix interface
                   → fiber bridging, pullout → energy absorption → TOUGHNESS
                   (used in CMCs: BN coating creates weak interface deliberately)

  FAILURE MODES IN LAMINATES:
  ┌─────────────────────────────────────────────────────────────────────────┐
  │  Fiber breakage (UD tension):    catastrophic in fiber direction        │
  │  Matrix cracking (transverse):   damage tolerance; precursor to delam  │
  │  Delamination:                   interlaminar shear failure between plies│
  │    → caused by: out-of-plane loads, impact, free-edge effects           │
  │    → detected by: ultrasonic C-scan, thermography, X-ray CT            │
  │  Fiber microbuckling (compression): kink band formation; limits σ_c     │
  │  Impact damage:                  BVID (barely visible impact damage)    │
  │    invisible on surface, significant internal damage; design-critical    │
  └─────────────────────────────────────────────────────────────────────────┘
```

### Applications and the Ashby Chart Context

```
  ASHBY MAP: E vs ρ  (stiffness vs density)
  ┌─────────────────────────────────────────────────────────────────────────┐
  │                                                                          │
  │  E (GPa)                                                                 │
  │  1000 │  Diamond                                                         │
  │       │    Ceramics (Al₂O₃, SiC, Si₃N₄)                                │
  │   100 │    Steel, Ti alloys     CFRP (0°) ← composites fill here        │
  │       │    Al alloys                                                     │
  │    10 │              GFRP, CFRP (quasi-iso)                             │
  │       │                         Wood (along grain)                      │
  │     1 │                    Rigid polymers                               │
  │       │                         Elastomers                              │
  │  0.01 │                              Foams                              │
  │       └───────────────────────────────────────────── ρ (g/cm³)         │
  │              0.1         1          2        5  10                      │
  │                   ←── low density steels, Ti ──────►                    │
  │                                                                          │
  │  CFRP fills the upper-left corner (high E, low ρ) — no monolithic       │
  │  material achieves this combination. This is why composites dominate     │
  │  aerospace primary structure.                                            │
  └─────────────────────────────────────────────────────────────────────────┘

  APPLICATIONS:
  Boeing 787: 50% CFRP by weight (fuselage barrel, wing box, empennage)
    → 20% fuel savings vs 767 (lower weight + aerodynamics)
    → Lightning strike concern → copper mesh embedded in skin
  Airbus A350: 53% CFRP
  F-35: ~35% CFRP, ~14% other composites
  Wind turbine blade: GFRP + some CFRP spar caps; 80m+ blades
  Sports: CF bicycle frames (6kg → 700g), tennis rackets, ski poles
  Ceramic armor: Al₂O₃ or SiC tile + UHMWPE backing → NIJ Level IV
  Dental: ZrO₂ crowns (aesthetic + tough); glass-ceramic (e.max)
```

---

## Decision Cheat Sheet

| You need... | Use |
|------------|-----|
| Maximum hardness (cutting, wear) | SiC, Al₂O₃, Si₃N₄, WC-Co |
| High temperature structure (>1000°C) | Si₃N₄, SiC, CMC (SiC/SiC) |
| Thermal barrier coating | 8YSZ (low κ, strain tolerant) |
| Ferroelectric capacitor (MLCC) | BaTiO₃ (doped) |
| Piezoelectric sensor/actuator | PZT (PbZr₁₋ₓTiₓO₃) |
| High-κ dielectric, substrate | SrTiO₃, AlN |
| Highest specific stiffness (E/ρ) | Unidirectional CFRP |
| Balanced in-plane properties | Quasi-isotropic CFRP laminate [0/±45/90]_s |
| Recyclable aerospace composite | PEEK or PEKK thermoplastic matrix |
| High toughness ceramic | Transformation-toughened ZrO₂ (Ce-TZP) |
| Low cost structural composite | E-glass / vinyl ester |
| High toughness + light weight | Aramid (Kevlar) hybrid composite |
| Understand composite design | Rule of mixtures → CLT (Classical Laminate Theory) |

---

## Common Confusion Points

**Ceramic "strength" is not a material constant — it's a distribution.**
Unlike metals, where you can look up yield strength and use it, ceramics
require Weibull analysis. A ceramic component "rated" at 300 MPa has a
probability of failure at that stress — typically specified at 99.9%
survival. Design allowables are set by the Weibull parameters (m, σ₀),
test sample size, and target reliability.

**Volume fraction vs weight fraction — composites spec often uses weight.**
Prepreg specs list fiber areal weight (FAW, g/m²) and resin content (%). Rule
of mixtures uses volume fraction V_f. Convert: V_f = (w_f/ρ_f) / (w_f/ρ_f + w_m/ρ_m).
At 60 vol% carbon fiber, the fiber is ~52 wt% (carbon is denser than epoxy).

**Transformational toughening in ZrO₂ only works while the t-phase is present.**
At high temperatures, the tetragonal phase is the stable phase — no transformation
occurs, so the toughening mechanism vanishes above ~400°C. PSZ toughness drops
significantly at elevated temperature. For TBC applications, you WANT the stable
cubic phase (8YSZ) for high-T stability — toughness is not the design goal there.

**CFRP is not uniformly "strong" — strength is direction-specific.**
A unidirectional ply has ~1500 MPa tensile strength at 0° and only ~40 MPa at 90°
(matrix-dominated). A quasi-isotropic laminate [0/±45/90]_s averages to ~500–600 MPa
in any in-plane direction — this is the "knockdown" from 1500 MPa UD to QI. Design
laminates with fibers along primary load paths; don't assume isotropic behavior.
