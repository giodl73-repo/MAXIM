# Metals and Alloys — Phase Diagrams, Heat Treatment, Strengthening

## The Big Picture

```
    METALS & ALLOYS LANDSCAPE
    ══════════════════════════════════════════════════════════

    THERMODYNAMICS                   KINETICS
    ┌──────────────────────┐        ┌────────────────────────┐
    │ Gibbs phase rule     │        │ Nucleation rate J(T)   │
    │ Phase diagrams       │───────▶│ Growth rate G(T)       │
    │ (what CAN form)      │        │ TTT / CCT diagrams     │
    │ Lever rule           │        │ (what DOES form)       │
    └──────────────────────┘        └────────────────────────┘
               │                               │
               └──────────────┬────────────────┘
                              ▼
              MICROSTRUCTURE (grain size, phases, precipitates)
                              │
                              ▼
              MECHANICAL PROPERTIES (σ_y, UTS, K_IC, fatigue)
```

---

## Gibbs Phase Rule

$$\boxed{F = C - P + 2}$$

F = degrees of freedom (independently variable: T, P, compositions)
C = number of components
P = number of phases present

```
    At constant pressure (materials processing): F = C - P + 1

    Binary alloy (C=2):
    One phase:   F = 2-1+1 = 2 → can vary T and composition independently
    Two phases:  F = 2-2+1 = 1 → fixing T fixes compositions of both phases
    Three phases: F = 2-3+1 = 0 → invariant point (eutectic, eutectoid)

    Pure substance (C=1):
    One phase: F = 1 → varies with T
    Two phases: F = 0 → invariant (melting point)
    Triple point: three phases → F = -1 + 2 = 1 → invariant in (T,P) space
```

---

## Binary Phase Diagrams

### Isomorphous System: Cu-Ni (Complete Solid Solubility)

Cu (T_m = 1085°C) and Ni (T_m = 1453°C): same FCC structure, similar radius and electronegativity → Hume-Rothery rules satisfied → complete mutual solubility.

```
    T(°C)
    1500 │         ●────────────────────────● Ni
         │        / LIQUID                  /
    1300 │       /────────────────────────/
         │      /  LIQUIDUS               /
    1200 │     / ────────────────────────/
         │    │   TWO PHASE REGION       │
    1100 │     \  SOLIDUS               /
         │      \────────────────────────\
    1085 │       ● Cu──────────────────  \
         │
         0%Ni   25   50    75   100%Ni
                     composition

    KEY: Two-phase region between liquidus and solidus curves.
    At temperature T in two-phase region:
    Liquid composition = intersection with liquidus
    Solid composition  = intersection with solidus
    (these are different compositions!)

    Lever Rule (mass fraction of each phase):
    If alloy overall composition C₀, temperature in two-phase L+S region:
    C_L = liquid composition (from liquidus)
    C_S = solid composition  (from solidus)

    f_L = (C₀ - C_S)/(C_L - C_S)  (fraction liquid)
    f_S = (C_L - C₀)/(C_L - C_S)  (fraction solid)
    f_L + f_S = 1

    Example: 50% Ni alloy at 1300°C
    C_L = 45% Ni (read from liquidus at 1300°C)
    C_S = 58% Ni (read from solidus at 1300°C)
    f_S = (45-50)/(45-58) = 5/13 = 0.38 (38% solid)
    f_L = (58-50)/(58-45) = 8/13 = 0.62 (62% liquid)
```

### Eutectic System: Pb-Sn (Soldering Alloy)

```
    T(°C)
    350 │  ●Pb                          ●Sn
        │   \                          /
    300 │    \  LIQUID               /
        │     \                    /
    250 │      \    LIQUIDUS      /
        │  (Pb) \ ──────────── / (Sn)
    200 │  α     \────────────/   β
        │         \          /
    183 │──────────●────────●──────── EUTECTIC (183°C, 61.9% Sn)
        │  α+β (two-phase solid region)
        └────────────────────────────── %Sn
        0%Sn   20    40    62    80    100%Sn

    Eutectic composition (61.9% Sn): melts/solidifies at single temperature 183°C
    On cooling through eutectic: simultaneous formation of α (rich Pb) + β (rich Sn)
    Eutectic microstructure: fine alternating lamellae of α and β
    → Lamellar spacing λ ∝ 1/ΔT_undercooling

    α (Pb-rich): up to 18.3% Sn max solubility at eutectic T
    β (Sn-rich): up to 2.2% Pb max solubility at eutectic T

    Applications:
    Eutectic: Pb-Sn 63/37 = classic electronics solder (melts 183°C)
    Hypoeutectic (< 61.9% Sn): plumber's solder (range of melt temperatures)
    Hypereutectic (> 61.9% Sn): bearing alloys

    Lead-free solders: Sn-Ag-Cu (SAC 305: 3% Ag, 0.5% Cu) — melts ~217°C
    Higher reflow T required → more stress on PCB components
```

---

## The Iron-Carbon Phase Diagram

The most important binary phase diagram in engineering.

```
    T(°C)
    1600 │●───────────────────────────────
         │  LIQUID (L)
    1500 │          ●───L+γ───●
         │         (0.09%)   (0.51%)
         │   L+δ          (4.3%)
    1400 │     ●──L+γ──────────────────●  EUTECTIC: 1147°C, 4.3%C
         │  (2.01%)   LIQUID           │  Liquid → γ-austenite + Fe₃C
    1300 │             +γ              │
         │                             │
    1200 │  γ (austenite, FCC)         │
         │                             │
    1100 │                          Fe₃C + L
    1000 │                             │
         │        γ + Fe₃C           ─┤─────── 1147°C eutectic line
         │                            │
     900 │                            │
         │ γ        EUTECTOID: 727°C, 0.76%C
     800 │    ─────●─────────●────── γ+Fe₃C
         │   /     (0.022%C) (0.76%C) \
     727 │──●──────────────────────────●── EUTECTOID LINE
         │  │                          │
     600 │  α+Fe₃C (PEARLITE)         Fe₃C
         │
     400 │  α-ferrite (BCC)
         │
         └────────────────────────────── %C
         0%   0.5  1.0  1.5  2.0  4.3  6.67%
         ←── STEEL ───────→← CAST IRON →│Fe₃C

    Phase boundaries:
    A₁ = eutectoid temperature 727°C
    A₃ = γ → α+γ boundary (for hypoeutectoid)
    A_cm = γ → γ+Fe₃C boundary (for hypereutectoid)
```

### Phase Descriptions

| Phase | Crystal | Max %C | Description |
|-------|---------|--------|-------------|
| α-ferrite | BCC | 0.022% | Soft, ductile, magnetic below 770°C (Curie T) |
| γ-austenite | FCC | 2.14% | Non-magnetic, stable 727-1394°C in pure Fe |
| δ-ferrite | BCC | 0.09% | High-T, only above 1394°C |
| Fe₃C (cementite) | Orthorhombic | 6.67% | Hard, brittle intermetallic |
| Martensite | BCT (body-centered tetragonal) | 0.1-0.8% | Non-equilibrium, supersaturated C |

### Microstructures in Fe-C System

```
    EUTECTOID STEEL (0.76% C), cooling through 727°C:
    γ (0.76%C) → α(0.022%C) + Fe₃C(6.67%C) simultaneously
    = PEARLITE: fine alternating lamellae of α and Fe₃C
    Lamellar spacing: 0.1-0.5 μm (depends on undercooling)
    Properties: σ_UTS ≈ 720 MPa, ductile, machinable

    HYPOEUTECTOID STEEL (< 0.76% C), e.g., 0.4%C:
    γ → pro-eutectoid α at grain boundaries (white areas) + pearlite
    More %C → more pearlite fraction:
    f_pearlite = (C₀ - 0.022)/(0.76 - 0.022)

    HYPEREUTECTOID STEEL (0.76-2.14% C), e.g., 1.0%C:
    γ → pro-eutectoid Fe₃C at grain boundaries (network) + pearlite
    Embrittlement from Fe₃C network → spheroidize annealing needed

    LEDEBURITE (4.3% C eutectic):
    Liquid → γ + Fe₃C (at 1147°C)
    On further cooling, γ transforms too → complex microstructure
    Cast irons: white (hard, brittle) vs gray (graphite flakes, better machining)
```

---

## Martensite Transformation

Diffusionless (displacive) transformation when austenite is quenched too fast for
diffusion of carbon → carbon trapped in BCT structure.

```
    FCC austenite (γ, carbon in octahedral sites)
              ↓ rapid quench (no C diffusion time)
    BCT martensite (α', carbon trapped in interstitial sites)

    Tetragonality: c/a - 1 ≈ 0.046 × (%C)
    At 0.6%C: c/a = 1 + 0.046×0.6 = 1.028

    Martensite start temperature: M_s = 539 - 423(%C) - 30.4(%Mn)
                                         - 17.7(%Ni) - 12.1(%Cr) - 7.5(%Mo) (°C)
    For 0.4%C steel: M_s ≈ 539 - 423×0.4 = 370°C
    Complete martensite when T reaches M_f (often -50 to -150°C)

    Why is martensite hard?
    1. Carbon in interstitial sites causes tetragonal distortion → lattice strain
    2. High dislocation density from the transformation shear strain
    3. Fine martensite plates/laths → effective small "grain size"
    Hardness: HRC ≈ 30 + 50×(%C) for %C < 0.6 (then saturates ~HRC 65)

    Problems with martensite:
    → Very hard but brittle (no mechanism for plastic relaxation)
    → High residual stress → quench cracking risk
    → Must temper to recover toughness
```

---

## TTT and CCT Diagrams

**TTT = Time-Temperature-Transformation** (isothermal): austenitize then hold at fixed T.
**CCT = Continuous-Cooling-Transformation**: austenitize then cool at constant rate.

```
    TTT diagram for eutectoid steel (0.76%C):

    T(°C)
     800 │
         │        ──────────────────────── A₁
     700 │    Pearlite nose   ────────────────────────
         │        ─────────────────────────────────
     600 │    Bainite upper  ──────────────────
         │                 ──────────────────
     500 │    Bainite lower ────────────────
         │                   ────────────
     400 │
         │             M_s = 220°C──────────────────
     300 │                         Martensite
         │             M_90 = 50°C
     200 │             (Ms, 50%, 90% lines)
         │
         └─────────────────────────────── log time (s)
         0.1   1    10   100  1000  10000

    Pearlite nose: ~550°C, ~1 second (fastest transformation)
    To avoid pearlite: must cool faster than CCR (critical cooling rate)
    CCR for 0.76%C steel: ~140°C/s at pearlite nose

    BAINITE: intermediate transformation product (250-550°C)
    Upper bainite (400-550°C): feathery arrangement of α + elongated Fe₃C
    Lower bainite (250-400°C): similar to tempered martensite, better toughness
    Bainite has better toughness-strength combination than pearlite or martensite

    Adding alloying elements shifts TTT curves RIGHT (more time):
    Mn, Cr, Mo, Ni → increase hardenability (can quench thicker sections)
    → Used in Jominy end-quench test to measure hardenability
```

---

## Steel Heat Treatment

```
    ANNEALING:
    Heat to above A₃ (full anneal) or A₁ (process anneal)
    Slow cool (furnace cool)
    → Equilibrium microstructure: coarse pearlite
    → Purpose: soften for machining, relieve residual stress

    NORMALIZING:
    Heat above A₃, air cool
    → Fine pearlite (faster than furnace cool)
    → Purpose: refine grain size, improve toughness vs annealing

    QUENCHING:
    Heat above A₃ → austenitize → rapid quench (water, oil, air)
    → Martensite (if above CCR)
    → Hard but brittle, high residual stress

    TEMPERING (after quenching):
    Heat to 150-700°C, hold, then air cool
    → Martensite → tempered martensite → transition carbides → cementite
    Sequence: ε-carbide (Fe₂.₄C) at 100-200°C → θ-cementite (Fe₃C) at 250-450°C
    → coarsen carbides + recovery of dislocation structure at 450-700°C
    σ_y and hardness decrease, K_IC and ductility increase with T_temper

    QUENCH AND TEMPER schedule for 4340 steel (Ni-Cr-Mo alloy steel):
    Austenitize: 820°C, 1h → Oil quench → Temper 200°C, 2h
    Result: σ_y ≈ 1600 MPa, UTS ≈ 1800 MPa, K_IC ≈ 50 MPa√m

    AUSTEMPERING (bainite formation):
    Austenitize → quench to bainite nose temperature (say 300°C) → hold → air cool
    → Lower bainite: better toughness-strength than tempered martensite at same hardness
    Used for: springs, high-strength fasteners, ADI (austempered ductile iron)
```

---

## Strengthening Mechanisms

### 1. Solid Solution Strengthening (Vegard's Law)

Substitutional or interstitial solutes distort lattice → impede dislocation motion.

$$\Delta\sigma_{ss} = A c^n \quad (n = 1/2 \text{ for random, } 1/3 \text{ for some systems})$$

Vegard's law (lattice parameter variation): $a_{alloy} = a_A + (a_B - a_A)x_B$ (linear approximation)

```
    Misfit parameter δ = (1/a)(da/dc) = relative size difference
    Strengthening scales with δ and shear modulus G:
    Δτ = Aδ^{4/3}Gc^{2/3}  (Labusch model for random obstacles)

    Interstitial (C, N in Fe): very effective
    C in α-Fe: Δσ ≈ 5600 MPa per wt% C → but solubility limited to 0.022%C
    N in austenitic stainless: Δσ ≈ 600 MPa per wt%

    Substitutional (Cu in Al):
    Δσ ≈ 13 MPa per wt% Cu (significant for aerospace alloys)
```

### 2. Work Hardening (Strain Hardening)

Deformation increases dislocation density ρ → dislocations interact → harder to move.

**Taylor hardening**:
$$\tau = \tau_0 + \alpha G b \sqrt{\rho}$$

```
    τ₀ = friction stress (Peierls-Nabarro), α ≈ 0.3–0.5
    G = shear modulus, b = Burgers vector magnitude

    At large strains (Voce equation):
    σ = σ_∞ - (σ_∞ - σ_0)exp(-ε/ε_0)
    → Stress saturates at σ_∞ (dynamic recovery / dynamic recrystallization)

    Bauschinger effect: if you work harden in tension, easier to deform in compression
    → Cause: pile-up stress at obstacles reversed when loading reversed
    → Important for springback prediction in sheet forming

    Annealing to restore ductility:
    Recovery (T < 0.5T_m): rearrangement of dislocations into lower-energy configurations
    Recrystallization (T > 0.3-0.5T_m): nucleation and growth of new strain-free grains
    Grain growth (T > T_recryst): grain coarsening driven by boundary energy reduction
```

### 3. Precipitation Hardening (Age Hardening)

Most potent strengthening for non-ferrous alloys (Al-Cu, Ni superalloys).

```
    Mechanism: fine coherent precipitates block dislocation glide
    Three stages:
    1. Solution treatment: dissolve all solute in single phase (T > solvus)
    2. Quench: trap solute in supersaturated solid solution (SSSS)
    3. Aging: heat to intermediate T → controlled precipitation

    Al-4%Cu (2024 alloy) precipitation sequence:
    SSSS → GP zones (Cu monolayers on {100}, coherent) → θ'' (coherent disc)
         → θ' (semi-coherent) → θ (Al₂Cu, incoherent) → OVERAGING

    Peak hardness at θ'' (semi-coherent, maximum coherency strain + Orowan spacing)
    Overaging: θ becomes coarse incoherent → easy Orowan bypass → softer

    Coherency strengthening (small, coherent precipitate):
    Δτ = εGb(√(rN))^(1/2)  (cutting mechanism: dislocations cut through particle)

    Orowan bypassing (large, incoherent precipitate):
    Δτ_Orowan = Gb/L  where L = inter-precipitate spacing
    → Dislocations leave loops around particles

    Peak aging condition: where Δτ(cutting) = Δτ(Orowan)
    → Optimize: precipitate size r* and number density N

    Commercial example: 7075-T6 aluminum:
    Age at 120°C for 24h → σ_y = 503 MPa, σ_UTS = 572 MPa
    (compare annealed 7075: σ_y = 103 MPa)
```

### 4. Grain Refinement: Hall-Petch

$$\sigma_y = \sigma_0 + k_y / \sqrt{d}$$

Most universal, also improves toughness simultaneously (unlike other mechanisms).
See 01-CRYSTAL-STRUCTURE for derivation.

### Comparison of Strengthening Mechanisms

| Mechanism          | Δσ_y potential | Ductility effect | Example              |
|-------------------|---------------|------------------|----------------------|
| Solid solution     | 10-100 MPa    | Slight decrease  | Cu-Ni, Fe-Mn         |
| Work hardening     | 100-1000 MPa  | Decreases        | Cold-drawn wire       |
| Precipitation      | 100-500 MPa   | Slight decrease  | Al 7075-T6, IN718    |
| Grain refinement   | 50-300 MPa    | Increases!       | HSLA steels, ECAP    |
| Martensite (quench)| 500-2000 MPa  | Large decrease   | Tool steels          |
| Combine all        | Up to 3000 MPa| Design balance   | Maraging steels      |

---

## Fracture Mechanics: Griffith Criterion

Brittle fracture: crack propagates spontaneously when energy release rate G > surface energy.

**Griffith criterion** (crack of half-length a in infinite plate, tensile stress σ):
$$\sigma_f = \sqrt{\frac{2E\gamma_s}{\pi a}}$$

**Stress intensity factor** (linear elastic fracture mechanics, LEFM):
$$K_I = \sigma\sqrt{\pi a} \cdot F\left(\frac{a}{W}\right)$$

where F = geometry factor ≈ 1 for large plate.

**Critical condition**: K_I = K_IC (fracture toughness — material property, units MPa√m).

```
    For a center crack of length 2a in infinite plate:
    K_I = σ√(πa)    (mode I, opening)
    K_II = τ√(πa)   (mode II, sliding)
    K_III = τ√(πa)  (mode III, tearing)

    Failure when: σ = K_IC/√(πa)
    → Critical flaw size: a_c = (K_IC/σ_y)²/π  (at yield stress level)

    Example: 4340 steel σ_y = 1600 MPa, K_IC = 50 MPa√m
    a_c = (50/1600)²/π = (0.03125)²/π = 0.00098/3.14 = 0.31 mm
    → Any flaw > 0.3 mm can cause brittle fracture at yield stress
    → Inspect by NDT (ultrasonic, eddy current, magnetic particle)

    High-strength Al (7075-T6): σ_y = 500 MPa, K_IC = 24 MPa√m
    a_c = (24/500)²/π = (0.048)²/π = 0.00230/π = 0.73 mm
    → Less sensitive to flaws than steel (larger a_c despite lower K_IC)

    J-integral (elastic-plastic): J = G = K_IC²/E' (plane stress or strain)
    For ductile fracture: use J_IC, CTOD (crack tip opening displacement)
```

---

## Aluminum Alloys

```
    Designation system:
    1xxx: pure Al (≥99%) — electrical conductors, packaging
    2xxx: Al-Cu (+ Mg): age-hardenable → high strength, poor corrosion
          2024-T3: σ_y=345 MPa, K_IC=26 MPa√m — fuselage skins
    3xxx: Al-Mn: moderate strength, good corrosion — beverage cans
    4xxx: Al-Si: low melting point → welding wire, casting alloys
    5xxx: Al-Mg: work-hardenable, excellent corrosion — marine, hulls
          5083-H116: σ_y=228 MPa — boats, cryogenic tanks (-196°C OK)
    6xxx: Al-Mg-Si: age-hardenable → medium strength, extrudable, weldable
          6061-T6: σ_y=276 MPa — structural, bicycle frames
    7xxx: Al-Zn-Mg-Cu: highest strength, poor corrosion, weldability issues
          7075-T6: σ_y=503 MPa — aircraft structure (wings, spars)
          7068-T6511: σ_y=634 MPa — record Al alloy

    Temper designations:
    -O  = annealed (soft, maximum ductility)
    -H  = strain-hardened (1xxx, 3xxx, 5xxx)
    -T3 = solution treated + cold worked + naturally aged
    -T6 = solution treated + artificially aged (peak hardness)
    -T73 = overaged (reduced strength but improved stress corrosion)
    -T7351 = overaged, stress-relieved, straightened

    New developments:
    Al-Li alloys (2195, 2099): E + 10%, ρ - 8% vs 2024 → fuselage
    ALCLAD: pure Al clad over high-strength alloy → galvanic protection
    Scandium additions (0.2-0.3% Sc): pin grain boundaries at high T
    Additive manufacturing: AlSi10Mg for complex aerospace brackets
```

---

## Decision Cheat Sheet

| Need                                  | Steel Choice              | Why                              |
|---------------------------------------|--------------------------|----------------------------------|
| General purpose structural            | A36 / ASTM A572 Gr50     | Cheap, weldable, adequate σ_y    |
| High-strength structural              | HSLA (A514, HY-100)      | σ_y = 690 MPa, good toughness    |
| High-hardness, wear-resistant         | 4340 Q&T, H13 tool steel | Martensite + carbides            |
| Stainless (corrosion)                 | 304, 316 (austenitic)    | Cr₂O₃ passive film               |
| High-T service (600°C+)              | Cr-Mo alloy (P91, P92)   | Tempered martensite, creep res.  |
| Spring                                | 9260 (Si-Mn)             | Elastic energy density σ_y²/E   |
| Bearing race, gear                    | 52100 (Cr-C)             | Contact fatigue resistance       |
| Ultra-high strength                   | 300M, M200, maraging     | σ_y = 2000 MPa, aerospace        |
| Best toughness-strength combination   | 4340 Q&T at 300°C temper | K_IC = 60-80 MPa√m               |

---

## Common Confusion Points

**Phase diagram shows equilibrium, not what you'll get**: If you see a two-phase region
on the Fe-C diagram at room temperature, that doesn't mean you have pearlite in practice.
If you quenched from austenite, you have martensite. The diagram says what's thermodynamically
stable; the microstructure is controlled by kinetics and thermal history.

**Martensite hardness is from carbon, not from BCT structure per se**: Iron alone can form
martensite (α' BCC = no tetragonality because no carbon). Pure iron martensite is only
slightly harder than normal ferrite. It's the supersaturated carbon in BCT structure that
causes enormous hardness. Without carbon, martensite is not a useful strengthening mechanism.

**Hardenability ≠ maximum hardness**: Hardenability is the depth to which martensite forms
under a given quench condition. Maximum hardness is determined solely by carbon content.
High-carbon steel: high maximum hardness, can have low hardenability (martensite only at
surface unless aggressively quenched). Alloy steel: same maximum hardness as plain carbon
steel at same %C, but much better hardenability (martensite forms through thick section).

**Grain refinement uniquely improves both strength and toughness**: All other strengthening
mechanisms (work hardening, solid solution, precipitation) trade strength for toughness.
Grain refinement (Hall-Petch) increases σ_y AND improves K_IC. This is why HSLA steels
use controlled rolling with microalloying to refine grains rather than just adding more
carbon or quenching.
