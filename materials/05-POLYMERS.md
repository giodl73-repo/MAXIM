# Polymers — Chain Architecture, Thermal Transitions, Viscoelasticity

## The Big Picture

```
    POLYMER SCIENCE LANDSCAPE
    ══════════════════════════════════════════════════════════

    MOLECULAR ARCHITECTURE              BULK PROPERTIES
    ┌──────────────────────┐           ┌─────────────────────┐
    │ Chain connectivity   │           │ E, σ_y, ε_f         │
    │ Degree of polymer.   │──────────▶│ T_g, T_m            │
    │ MW distribution      │           │ Viscoelasticity      │
    │ Tacticity            │           │ Creep, fatigue       │
    └──────────────────────┘           └─────────────────────┘
              │
              ▼
    MICROSTRUCTURE (crystallinity, spherulites, lamellar thickness)
              │
              ▼
    PROCESSING (flow, crystallization, orientation, crosslinking)
```

---

## Chain Architecture

### Repeat Units and Molecular Weight

A polymer is built from repeating monomer units:
- Polyethylene (PE): [-CH₂-CH₂-]_n
- Polypropylene (PP): [-CH₂-CH(CH₃)-]_n
- Polystyrene (PS): [-CH₂-CH(C₆H₅)-]_n

**Degree of polymerization** (DP): n = number of repeat units per chain.
M_0 = molecular weight of one repeat unit (g/mol).

**Molecular weight distributions**: Real polymers have chains of different lengths.

```
    Number-average molecular weight: M_n = Σ N_i M_i / Σ N_i
    Weight-average molecular weight: M_w = Σ N_i M_i² / Σ N_i M_i
    Z-average:                        M_z = Σ N_i M_i³ / Σ N_i M_i²

    Polydispersity index: PDI = M_w / M_n ≥ 1 always
    PDI = 1: monodisperse (ideal, achieved by anionic polymerization)
    PDI = 2: ideal step-growth polymerization (Flory distribution)
    PDI > 2: broad distribution (free-radical, Ziegler-Natta catalysis)
    PDI > 5: very broad (blends, multi-stage processes)

    Example: HDPE for pipe applications
    M_n ≈ 100,000 g/mol, M_w ≈ 300,000 g/mol, PDI = 3.0
    DP ≈ M_n/M_0 = 100,000/28 = 3571 repeat units per chain (average)

    Entanglement molecular weight M_e:
    When chains are long enough to entangle → network-like behavior
    M_e(PE) ≈ 1,800 g/mol
    M_e(PS) ≈ 17,000 g/mol
    Rheology changes dramatically above M_e: η ∝ M^3.4 (vs M^1 below M_e)
```

### Chain Statistics: The Freely Rotating Chain

<!-- @editor[bridge/P3]: No explicit connection to random walk / statistical mechanics — a physicist immediately recognizes ⟨r²⟩ = nl² as the random walk result (mean-square displacement of N steps of length l). The freely rotating chain and characteristic ratio C_∞ are corrections to the ideal random walk for correlated steps. Worth one line: "This is a biased random walk with bond-angle correlations — C_∞ > 1 encodes the correlation length of the walk" -->

Real polymer chain: backbone bonds have fixed angle θ (C-C = 109.5°) and can rotate.

**Freely rotating chain model** (no correlation beyond bond angle):

$$\langle r^2 \rangle = n l^2 \frac{1 + \cos\theta}{1 - \cos\theta}$$

where n = number of bonds, l = bond length, θ = supplement of bond angle (70.5° for C-C).

For C-C backbone: (1+cos 70.5°)/(1-cos 70.5°) = (1+0.333)/(1-0.333) = 2.0

**RMS end-to-end distance**: $r_{rms} = \sqrt{\langle r^2\rangle} = l\sqrt{2n}$

More general characteristic ratio C_∞ (accounting for hindered rotation):

$$\langle r^2\rangle = C_\infty n l^2$$

```
    C_∞ values:
    PE (polyethylene):    C_∞ ≈ 6.7
    PS (polystyrene):     C_∞ ≈ 9.5
    PDMS (silicone):      C_∞ ≈ 6.2

    For PE with n=3571 bonds, l=1.54 Å:
    r_rms = 1.54√(6.7×3571) = 1.54×154.5 = 238 Å = 23.8 nm

    Contour length (fully extended): L = n·l = 3571×1.54 = 5500 Å = 550 nm
    Extension ratio max: L/r_rms = 550/23.8 = 23× — enormous extensibility!
    → Rubber elasticity derives from this chain statistical mechanics
```

### Molecular Architecture Types

```
    LINEAR:         ─────────────────── (PE, PVC, Nylon)

    BRANCHED:        ─────────│──────── (LDPE: long chain branches)
                              │
                          ────┴────
    (short chain branches: LLDPE, co-monomer incorporation)

    CROSSLINKED:     ─────────│──────── (rubber: S-S crosslinks from vulcanization)
                              │         (thermosets: covalent network from cure)
                    ─────────┘

    BLOCK:          A-A-A-A-B-B-B-B-A-A-A-A (SBS block copolymer, thermoplastic elastomer)

    GRAFT:           A-A-A-A-A-A-A-A   (backbone A, grafted B)
                         │   │
                         B   B

    STAR / DENDRIMER: branched from central point
```

### Tacticity

```
    Polypropylene: [-CH₂-CH(CH₃)-]_n
    Isotactic:     all CH₃ on same side of backbone → crystallizable → high T_m
    Syndiotactic:  alternating CH₃ sides → can crystallize → moderate T_m
    Atactic:       random → cannot crystallize → amorphous, lower T_g only

    Commercial significance:
    Isotactic PP (i-PP): T_m = 165°C, σ_y = 35 MPa — plastic containers, fibers
    Atactic PP (a-PP): amorphous, used as adhesive, soft modifier
    Ziegler-Natta catalysts → isotactic; metallocene → can control tacticity
```

---

## Crystallinity and Morphology

Polymers are NEVER 100% crystalline — chains are too long and entangled.
Semicrystalline polymers have crystalline regions (lamellae) + amorphous matrix.

### Lamellar Crystals

```
    Folded-chain lamellar crystal:
    ─────────────────── crystal surface (fold plane)
    │  │  │  │  │  │   folded chain segments
    │  │  │  │  │  │   c-axis = all-trans chains
    │  │  │  │  │  │   l = lamellar thickness (10-50 nm)
    ─────────────────── crystal surface

    Lamellar thickness l ∝ 1/ΔT (crystallization undercooling)
    Thermodynamic: l_min* = 2σ_e T_m⁰/(ΔH_f ΔT)
    σ_e = fold surface energy, T_m⁰ = equilibrium melting point
    → Deeper quench → thinner lamellae → lower T_m observed
    → Annealing increases l → raises T_m

    Degree of crystallinity χ (by DSC):
    χ = ΔH_m,sample / ΔH_m,100%  (compare to perfectly crystalline standard)
    PE: ΔH_m,100% = 293 J/g; χ = 50-80% typical
    PET: χ = 20-50% depending on processing
    PEEK: χ = 30-35% typical
```

### Spherulite Structure

```
    Spherulite: birefringent spherical entity visible under polarized light (Maltese cross)
    Structure: lamellae radiating outward from central nucleus
    Interlamellar amorphous regions (tie molecules connecting lamellae)
    Size: 1 μm to 1 mm depending on nucleation density

    ○ ○ ○
    ─────────────────────
        spherulites        ← crystalline domains radiating outward
    ─────────────────────
    ○ ○ ○

    Faster cooling → smaller spherulites (more nuclei, less growth time)
    Adding nucleating agents (e.g., talc in PP): very fine spherulites → improved clarity + stiffness
```

---

## Thermal Transitions

### Glass Transition Temperature T_g

**T_g** = temperature where polymer goes from glassy (rigid, brittle) to rubbery (soft, flexible).
Not a first-order phase transition — kinetic phenomenon, depends on cooling rate.

**Free volume theory**:
- Free volume v_f = total volume V - occupied volume V_0
- Below T_g: chains are frozen, v_f barely changes with T (glassy thermal expansion α_g ≈ 3×10⁻⁴ K⁻¹)
- Above T_g: chains gain mobility, v_f increases rapidly (α_r ≈ 6×10⁻⁴ K⁻¹)
- T_g defined where v_f reaches critical value for cooperative segmental motion (~2.5% of V)

**WLF Equation** (Williams-Landel-Ferry, empirical but fundamental):

$$\log a_T = \frac{-C_1(T - T_r)}{C_2 + (T - T_r)}$$

where a_T = shift factor for superposition, T_r = reference temperature (often T_g),
C_1 ≈ 17.4, C_2 ≈ 51.6 K (universal constants close to T_g for many polymers).

```
    Physical interpretation:
    a_T = τ(T)/τ(T_r) = shift factor in time-temperature superposition
    → Mechanical behavior at T' and fast rate ≡ behavior at T and slow rate
    → Allows prediction of creep/relaxation from short-term tests

    Example: PS at T_g = 100°C
    At T = 60°C (below T_g by 40°C):
    log a_T = -17.4×(-40)/(51.6+(-40)) = 696/11.6 = 60
    a_T = 10^60 → essentially infinite relaxation time → glassy
    At T = 140°C:
    log a_T = -17.4×40/(51.6+40) = -696/91.6 = -7.6
    a_T = 10^{-7.6} → 40 million times faster → rubbery flow

    Factors affecting T_g:
    Chain stiffness (aromatic backbone → higher T_g):
    PE: T_g ≈ -125°C, PS: T_g = 100°C, PC: T_g = 147°C
    PEEK: T_g = 143°C, Polyimide: T_g > 300°C

    Plasticizers (e.g., DOP in PVC): fill free volume, lower T_g
    Copolymerization: weighted average by Fox equation
    1/T_g,copolymer = w_A/T_g,A + w_B/T_g,B
    Crosslinking: increases T_g (reduces chain mobility)
    Molecular weight: T_g increases with M_n, saturates above M ≈ 50 M_e
    T_g = T_g,∞ - K/M_n  (Fox-Flory equation)
```

### Melting Temperature T_m

First-order phase transition in semicrystalline polymers.
Equilibrium T_m⁰ is approached from below in practice (finite crystal size, defects).

$$T_m = T_m^0\left(1 - \frac{2\sigma_e}{\Delta H_f \cdot l}\right)$$

```
    Gibbs-Thomson equation above: thinner lamellae → lower T_m
    T_m⁰ (infinite crystal): PE ≈ 145°C, PET ≈ 280°C, PTFE ≈ 327°C
    Observed T_m typically 5-30°C below T_m⁰

    T_g vs T_m:
    Empirical: T_g/T_m ≈ 2/3 (in Kelvin) for symmetric polymers
    T_g/T_m ≈ 1/2 for asymmetric chains (with bulky pendant groups)
    → Useful rough estimate

    Common T_g and T_m values (°C):
    PE: T_g = -125, T_m = 125-137 (depends on density/branching)
    PP: T_g = -20, T_m = 165
    Nylon 66: T_g = 47, T_m = 265
    PET: T_g = 79, T_m = 265
    PTFE: T_g = -97, T_m = 327
    PEEK: T_g = 143, T_m = 343
    HDPE: T_g = -110, T_m = 132
    PC: T_g = 147, T_m = ~250 (rarely fully crystallized)
```

---

## Rubber Elasticity

Elastomers are crosslinked amorphous polymer networks above T_g.
Elasticity is entropic, not energetic.

### Statistical Thermodynamics of a Network Strand

A single polymer strand with n freely jointed links of length l:

End-to-end vector r. Partition function Z(r) from Boltzmann:

$$Z(r) \propto \exp\left(-\frac{3r^2}{2nl^2}\right) \quad \text{(Gaussian chain)}$$

Entropy per chain: $S = k_B \ln Z = -\frac{k_B}{2}\cdot\frac{3r^2}{nl^2} + \text{const}$

Spring constant: $k_{spring} = \frac{3k_B T}{nl^2} = \frac{3k_B T}{\langle r^2\rangle_0}$

### Neo-Hookean Constitutive Law

For a crosslinked network with chain density N (chains per unit volume),
each chain with n segments, under uniaxial stretch λ = L/L₀:

$$\sigma_{true} = NkT\left(\lambda - \frac{1}{\lambda^2}\right)$$

Small strain (λ → 1, ε = λ-1 small):
$$\sigma \approx NkT \cdot 3\varepsilon = E \cdot \varepsilon \quad \Rightarrow \quad E = 3NkT$$

Shear modulus: G = NkT (also G = ρRT/M_c where M_c = molecular weight between crosslinks)

```
    Physical insight:
    → E increases with temperature (opposite of metals!)
    → This is entropic: stretching reduces entropy → restoring force ∝ T
    → Compare to metal spring: E_metal decreases slightly with T (bond softening)
    → E_rubber ∝ T (stronger restoring force at higher T)
    → If T fixed: E ∝ crosslink density N

    Practical:
    Natural rubber (lightly vulcanized with S): M_c ≈ 10,000 g/mol
    G = ρRT/M_c = (0.93×10³)(8.314)(300)/10,000 = 0.23 MPa
    E ≈ 3G = 0.70 MPa ✓ (measured ~ 0.3-1 MPa for rubber)

    Limits: Gaussian chain breaks down at large λ (chain reaches finite extensibility)
    Non-Gaussian corrections: Langevin statistics, Arruda-Boyce 8-chain model
    λ_max ≈ √n (finite extensibility ratio)
    → Strain hardening occurs near λ_max → prevents tearing of rubber seals
```

---

## Viscoelasticity

Polymers are viscoelastic: time-dependent mechanical response.
Simultaneously elastic (store energy, spring-like) and viscous (dissipate energy, dashpot-like).

### Maxwell Model (series spring + dashpot)

```
    ┌────────────────────────────┐
    │    [spring k]─[dashpot η] │
    └────────────────────────────┘

    Same stress in both: σ = k·ε_elastic = η·(dε_viscous/dt)
    Total strain: ε = ε_elastic + ε_viscous
    Constitutive equation: dε/dt = σ/E + σ/η (differentiate)
    → ε̇ = σ̇/E + σ/η   (Maxwell model)

    STRESS RELAXATION TEST (fixed strain ε₀, measure σ(t)):
    dσ/dt + σ/τ = 0   where τ = η/E = relaxation time
    Solution: σ(t) = σ₀ e^{-t/τ}   where σ₀ = Eε₀
    Relaxation modulus: E_r(t) = E·e^{-t/τ}
    → Good for stress relaxation, poor for creep (predicts infinite creep)
```

### Kelvin-Voigt Model (parallel spring + dashpot)

```
    ┌─────────────────┐
    │  [spring k] ∥   │
    │  [dashpot η]    │
    └─────────────────┘

    Same strain in both: σ = k·ε + η·(dε/dt)
    σ = Eε + η(dε/dt)

    CREEP TEST (fixed stress σ₀, measure ε(t)):
    ε(t) = (σ₀/E)(1 - e^{-t/τ})   where τ = η/E
    → Good for creep, poor for stress relaxation (predicts instant relaxation)
    Compliance: J(t) = ε(t)/σ₀ = J₀(1 - e^{-t/τ})
```

### General Linear Viscoelasticity

Real polymers: spectrum of relaxation times. Use generalized Maxwell (Prony series):
$$E_r(t) = E_\infty + \sum_{i=1}^N E_i e^{-t/\tau_i}$$

**Dynamic Mechanical Analysis (DMA)**:

Oscillatory strain ε(t) = ε₀ e^{iωt}:
Response: σ(t) = σ₀ e^{i(ωt+δ)} = ε₀(E' + iE'')e^{iωt}

- Storage modulus E' = σ₀cos(δ)/ε₀ (elastic component, energy stored)
- Loss modulus E'' = σ₀sin(δ)/ε₀ (viscous component, energy dissipated)
- Loss tangent: tan δ = E''/E' (ratio of energy dissipated to stored per cycle)

```
    DMA scan through T (at fixed frequency 1 Hz):

    E'(Pa)
    10¹⁰  ┤───────────────────────────
          │  Glassy region             \
    10⁹   ┤                            \
          │                          transition
    10⁸   ┤                              \
          │  tan δ peak at T_g            \
    10⁷   ┤                        Rubbery plateau
          │                               ─────────
    10⁶   ┤
          └──────────────────────────── T
          T << T_g                T_g             T > T_g

    tan δ peak = T_g from DMA (typically 5-10°C above DSC T_g at 1 Hz)
    Area under tan δ peak ~ energy dissipated per cycle → damping
    Wide tan δ peak → good vibration damper (SBR rubber, PVC blends)
    Frequency shift of T_g: per decade frequency, T_g shifts ~7°C
    (Consistent with WLF equation)
```

---

## Common Polymers Reference Table

| Polymer      | T_g (°C) | T_m (°C) | E (GPa) | σ_y (MPa) | Applications                     |
|-------------|---------|---------|--------|---------|----------------------------------|
| LDPE         | -110    | 108-115 | 0.1-0.3| 8-20    | Bags, film, coating              |
| HDPE         | -110    | 126-135 | 0.8-1.5| 20-37   | Bottles, pipe, geomembranes      |
| PP           | -20     | 160-168 | 1.5-2.0| 30-40   | Containers, fiber, auto parts    |
| PS           | 97-105  | —       | 3.0-3.5| 30-60   | Foam, packaging, CD cases        |
| PVC          | 75-85   | —       | 2.5-4.2| 40-55   | Pipe, wire insulation, flooring  |
| PMMA (acrylic)| 100-108| —       | 2.7-3.2| 60-75   | Windows, optical, signs          |
| Nylon 6      | 47      | 220     | 2.5-3.5| 70-85   | Gears, bearings, textiles        |
| Nylon 66     | 60      | 265     | 2.8-4.0| 80-95   | Engineering parts, carpet        |
| PET          | 70-80   | 250-265 | 2.5-4.5| 55-75   | Bottles, film, fiber (polyester) |
| PC           | 145-150 | ~260    | 2.3-2.4| 55-65   | Safety glass, electronics, CD   |
| PEEK         | 143     | 335-345 | 3.6    | 91      | Aerospace, medical, high-T parts |
| PTFE         | -97     | 320-327 | 0.4-0.7| 20-25   | Non-stick, seals, biomedical     |
| PDMS         | -127    | -40     | 0.001-0.002 | 0.1-0.5| Silicone, microfluidics, sealants |
| Epoxy (cured)| 100-200 | —       | 2.5-4.5| 60-80   | Adhesives, CFRP matrix, PCB      |
| Carbon fiber  | —      | >3000°C | 230-600| —       | Reinforcement fiber              |

---

## Thermosets vs Thermoplastics vs Elastomers

```
    ┌──────────────────────────────────────────────────────────┐
    │  THERMOPLASTICS                                          │
    │  Linear or branched chains → melt and flow above T_g/T_m│
    │  Recyclable, re-processable                              │
    │  Examples: PE, PP, PS, Nylon, PET, PC                   │
    │  Bond type holding together: van der Waals (physical)   │
    ├──────────────────────────────────────────────────────────┤
    │  THERMOSETS                                              │
    │  Covalently crosslinked network → cannot melt or flow   │
    │  Cannot be recycled by melting                           │
    │  Examples: epoxy, polyurethane, phenolic, silicone resin │
    │  Cure: exothermic chemical reaction (mixing A+B, or heat)│
    │  Properties: higher T service, stiffer, more brittle     │
    ├──────────────────────────────────────────────────────────┤
    │  ELASTOMERS (RUBBERS)                                    │
    │  Lightly crosslinked amorphous polymer above T_g         │
    │  Large reversible deformation (100-1000% elongation)     │
    │  E = 0.001-10 MPa (orders below metals/plastics)         │
    │  Examples: NR (vulcanized), SBR, EPDM, silicone          │
    │  Crosslinks: S-S bonds (vulcanization), peroxide, γ-rad  │
    └──────────────────────────────────────────────────────────┘
```

---

## Processing Overview

```
    Processing method   │ Material type  │ Products
    ───────────────────────────────────────────────────────────
    Injection molding   │ Thermoplastics │ Complex 3D parts
                        │                │ (gears, housings, caps)
    Extrusion           │ Thermoplastics │ Pipe, sheet, film,
                        │                │ pellets (compounding)
    Blow molding        │ Thermoplastics │ Bottles, tanks
                        │ (stretch blow) │ (PET water bottles)
    Compression molding │ Thermosets     │ SMC, BMC auto panels
    RTM/VARTM          │ Thermoset + fiber│ CFRP structural parts
    Thermoforming       │ Thermoplastics │ Trays, packaging
    Fiber spinning      │ Thermoplastics │ Fiber, yarn (Nylon, PET)
    FUSED DEPOSITION   │ Thermoplastics │ 3D printing (FDM/FFF)
    SLA/DLP/SLS        │ Thermosets/thermo│ Photopolymer 3D printing
```

### Injection Molding Fundamentals

```
    Melt flow index (MFI): g/10 min pushed through orifice at 190°C, 2.16 kg load
    Low MFI: high MW, viscous → structural parts (not thin-walled)
    High MFI: low MW, flows easily → packaging, thin walls

    Shear thinning: η = η₀/(1+(λγ̇)^a)^n (power law)
    Polymer melts are pseudoplastic (shear-thinning) → power law index n < 1
    → Easier to fill mold at high injection speed (high γ̇ → lower η)

    Frozen skin / crystallization kinetics:
    Fast injection → fill before solidification
    Slow → short shots, warpage
    Crystallizable polymers: slow cool → high crystallinity → higher T_m, stiffer
    Fast cool (thin walls, cold mold) → less crystallinity → tougher but softer
```

---

## Decision Cheat Sheet

| Need                            | Polymer Choice       | Why                                  |
|---------------------------------|---------------------|--------------------------------------|
| High service T (>200°C)        | PEEK, PTFE, PI       | High T_g or T_m + thermal stability  |
| Chemical resistance (everything)| PTFE                 | C-F bonds, inert                     |
| Optical clarity + tough        | PC                   | Amorphous + high K_IC vs glass        |
| Structural load-bearing        | PEEK, Nylon, POM     | Stiff + creep resistant              |
| Flexible seal/gasket           | EPDM, FKM, PDMS     | Elastomer + chemical resistance      |
| Food/medical contact           | PE, PP, PTFE, PEEK  | FDA approved, low leaching           |
| High-performance composite matrix | Epoxy + CF       | CFRP: best E/ρ and σ/ρ              |
| Low friction bearing           | PTFE, UHMWPE, POM   | Low μ_kinetic, good wear             |
| Electronics encapsulant        | Epoxy, silicone      | Low CTE, stable, moldable            |
| Elastomeric damper             | SBR, EPDM            | High tan δ, broad T_g range          |

---

## Common Confusion Points

**T_g is NOT the only relevant transition**: Crystallizable polymers have both T_g (chain
mobility onset) and T_m (crystallite melting). Below T_g: both crystalline and amorphous regions
are frozen, polymer is rigid. Between T_g and T_m: amorphous regions are rubbery but crystallites
constrain. Above T_m: fully molten. The ratio T_g/T_m determines the processing window.

**Entropy-elastic spring means higher T = stiffer**: Rubber stiffness E = 3NkT.
Heat a rubber band → it contracts (entropy drives it to coiled state). This is the opposite
of metals (which soften at higher T). A taut rubber band releases and contracts when heated.
Classic demonstration: hold a stretched rubber band to your lips, then relax and re-stretch —
you feel it cool when relaxed (expanding gas analogy works qualitatively but mechanism differs).

**Degree of crystallinity is not binary**: Semicrystalline polymers are never fully
crystalline. Even highly crystalline PTFE has 50-75% crystallinity. The "crystallinity"
measured by DSC (ΔH_m ratio) or WAXS is a volume-fraction average. Properties interpolate
between amorphous and crystalline extremes. Chain entanglements in the amorphous phase
are kinetically trapped during crystallization.

**PDI > 2 doesn't mean poor polymer**: PDI = 2 for ideal step-growth (Flory-Schulz
distribution). PDI = 1.1-1.5 from controlled/living polymerization (anionic, ATRP, RAFT).
But PDI 5-20 is common and acceptable for many commodity applications — the broad distribution
can actually improve processability (low-MW tail lubricates flow; high-MW tail adds strength).
