# Metals and Alloys — Phase Diagrams, Microstructure, Strengthening

---

## Big Picture

```
PHASE DIAGRAMS
(thermodynamic equilibrium map)
        │
        ▼
SOLIDIFICATION / HEAT TREATMENT
(traverse the phase diagram with time)
        │
        ▼
MICROSTRUCTURE
(grains, phases, precipitates, defects)
        │
        ▼
MECHANICAL PROPERTIES
(strength, toughness, ductility, fatigue life)

KEY: structure ↔ properties link runs through microstructure.
Same alloy composition, different heat treatment → 3× strength difference.
```

---

## Thermodynamics Primer

**Gibbs free energy:**
```
G = H - TS   (at constant T, P)

Equilibrium: minimize G
Phase stable if G lower than alternatives
```

**Mixing:** for A-B solid solution:
```
ΔG_mix = ΔH_mix - TΔS_mix

ΔS_mix = -Nk_B[x_A ln x_A + x_B ln x_B]   (always positive → entropy favors mixing)
ΔH_mix = Ω x_A x_B   (Ω = interaction parameter)

Ω > 0: like atoms prefer neighbors → phase separation tendency
Ω < 0: unlike atoms prefer neighbors → ordered compound tendency
Ω = 0: ideal solution (Raoult's law)
```

**Phase equilibrium:** two phases α and β coexist when:
```
μ_A^α = μ_A^β   AND   μ_B^α = μ_B^β   (chemical potentials equal)
```

**Gibbs phase rule:**
```
F = C - P + 2   (general, including P and T)
F = C - P + 1   (at fixed pressure, common in materials)

F = degrees of freedom (T, P, composition)
C = number of components
P = number of phases present

Example: pure metal (C=1), solid+liquid (P=2): F = 1-2+1 = 0 (invariant — melting point fixed)
Binary (C=2), two phases (P=2): F = 2-2+1 = 1 (fix T → compositions fixed)
```

---

## Binary Phase Diagrams

### Isomorphous System (complete solid solubility): Cu-Ni

```
T (°C)
1455 ├── Liquid only (L region)
     │
 ───  ├── LIQUIDUS LINE
     │   Two-phase: L + S
 ───  ├── SOLIDUS LINE
     │
1085 ├── Solid only (α region)
     └────────────────────────
     Cu                   Ni
      0%                 100%
```

**Lever rule** (find phase compositions and fractions at a given T, x_0):
```
At temperature T, alloy x_0 = 40% B:
Liquidus: x_L (less B), Solidus: x_S (more B)

f_L = (x_S - x_0)/(x_S - x_L)   (fraction liquid = right arm / total lever)
f_S = (x_0 - x_L)/(x_S - x_L)   (fraction solid = left arm / total lever)
```

### Eutectic System: Pb-Sn (solder)

```
T
327 ├─────    α + L         L         β + L    ──────
    │
183 ├─────────────── EUTECTIC POINT ─────────────── ←  eutectic: L → α + β simultaneously
    │
    │         α          α + β         β
    └───────────────────────────────────────────
    Pb                 61.9% Sn                Sn
```

**Eutectic reaction:** upon cooling at eutectic composition:
```
L → α + β  (simultaneous solidification of two solid phases)
```
Eutectic microstructure: alternating lamellae of α and β (Pb-rich + Sn-rich).

**Near-eutectic alloy:** primary α forms first, then eutectic matrix surrounds it.

---

## Iron-Carbon Phase Diagram

The most industrially important phase diagram. Carbon content (wt%) determines steel type.

```
T (°C)
1538 ├── δ-Fe (BCC)
     │
1495 ├── Peritectic point (0.17% C)
     │
1394 ├── γ (FCC austenite) field
     │
912  ├── α (BCC ferrite) field
     │
     │   Eutectoid point (0.76% C, 727°C)
727  ├── A₁ line: γ → α + Fe₃C
     │
     │   α + Fe₃C (pearlite region for steels)
  RT └────────────────────────────────────
     0  0.022  0.76  2.14      4.3   6.67%C
     ↑         ↑      ↑         ↑      ↑
  pure Fe  eutectoid  γ limit  eutectic  Fe₃C (cementite)
           (steel boundary)   (cast iron boundary)
```

**Key phases:**
| Phase | Crystal | C solubility | Notes |
|-------|---------|-------------|-------|
| α-ferrite | BCC | 0.022 wt% max | Soft, ductile, magnetic |
| γ-austenite | FCC | 2.14 wt% max | Non-magnetic, formable hot |
| δ-ferrite | BCC | 0.09 wt% max | High temperature only |
| Fe₃C cementite | Orthorhombic | 6.67 wt% C | Hard, brittle |
| Pearlite | α + Fe₃C lamellar | 0.76 wt% | Strong, moderate ductility |

**Why FCC austenite dissolves more C than BCC ferrite?**
FCC has larger octahedral interstices: r_oct(FCC) = 0.052a vs r_oct(BCC) = 0.036a.
Carbon atomic radius = 0.071 nm → fits better in FCC. Explains why steels must be
quenched from austenite to trap C → form martensite.

---

## Steel Heat Treatment

### Eutectoid transformation: γ → α + Fe₃C (pearlite)
At 727°C (A₁ temperature), 0.76% C steel:
- Fast cool: fine pearlite (thin lamellae → stronger)
- Slow cool: coarse pearlite (thick lamellae → softer)
- Very fast cool to room temperature: martensite (see below)

### TTT Diagram (Time-Temperature-Transformation)

```
T
     │
A₁ = 727°C ├───────────────────────────── (stable austenite above)
            │            "C-curve" nose
550°C ─     │        ╔═══════════╗
            │        ║  Pearlite ║
350°C ─     │       ╔══════════════╗
            │       ║   Bainite    ║
  M_s ─    │  ╔════════════════════╗
            │  ║    Martensite     ║
  M_f ─    │  ╚════════════════════╝
            └──────────────────────────────
            0.1 s      1 s   10 s   1 h
                         time →
```

**Martensite:** formed by quenching austenite faster than the "C-curve nose":
- Diffusionless transformation: FCC → BCT (body-centered tetragonal)
- Carbon trapped in octahedral sites → massive lattice distortion → very hard
- Hardness increases with %C: ~20 HRC at 0.2%C to ~65 HRC at 0.8%C
- Also very brittle — must be tempered

**Bainite:** intermediate transformation (upper bainite: laths; lower bainite: plates with ε-carbides)
- Tougher than martensite at same strength; austempered spring steels

**Tempering martensite:** heat 150–700°C after quench:
- C atoms diffuse out of BCT lattice → carbide precipitation
- Hardness decreases, toughness increases
- "Tempered martensite" is what most structural steels use

**Annealing:** slow cool from austenite → coarse pearlite, softens for machining

---

## Strengthening Mechanisms

Four independent additive mechanisms. Total strength ≈ Σ contributions.

### 1. Solid Solution Strengthening
Misfit strain from solute atom → local stress field → impedes dislocation motion.
```
Δσ_ss = C · G · c^(1/2) · ε_misfit

c = solute concentration (mole fraction)
ε_misfit = (r_solute - r_host)/r_host  (size misfit parameter)
G = shear modulus
```

Example: C in Fe (+~200 MPa at 0.002 wt% interstitial C, due to large misfit strain).
Cu-Ni alloys: max strengthening at ~50/50 composition.

### 2. Work Hardening (Strain Hardening)
Dislocation multiplication → dislocation-dislocation interactions → immobile tangles.
```
σ = σ_0 + K ε^n   (power law)

n = strain hardening exponent (0.1–0.5)
K = strength coefficient

Taylor: σ = σ_0 + αGb√ρ   (ρ = dislocation density)
```

Reversible by annealing (recovery + recrystallization → ρ decreases).

### 3. Precipitation Hardening (Age Hardening)
Fine coherent precipitates block dislocations. Used in aerospace Al alloys, Ni superalloys.

```
PROCESS: Solution anneal → quench → age (controlled T, time)

PEAK AGING:
1. Undersized: coherent GP zones (small precipitates) → sheared by dislocations
2. Peak: semi-coherent precipitates (θ' in Al-Cu, γ' in Ni) → maximum strength
3. Overaged: incoherent particles → dislocations bow around (Orowan looping)

Orowan bypass stress:
τ = Gb / L   (L = interparticle spacing)
```

Al-Cu alloy (Duralumin/2024-T3): solution anneal at 500°C, quench, age at 120°C 24h.
Strength: 70 MPa (annealed) → 450 MPa (peak aged) — 6× increase.

GP zones: Guinier-Preston zones (thin single-atom-layer disks of Cu in Al matrix).
Observed by X-ray diffuse scattering; precede precipitation.

### 4. Grain Boundary Strengthening (Hall-Petch)
Already covered in 01-CRYSTAL-STRUCTURE.md:
```
σ_y = σ_0 + k_y/√d
```
Grain refinement: thermomechanical processing (TMCP in steel), severe plastic deformation.
HSLA steels: grain refinement (Nb, Ti microalloying) + solid solution → 500+ MPa at low carbon.

---

## Fracture

**Griffith criterion** (thermodynamic): crack propagates when energy released > energy to create new surfaces:
```
σ_f = √(2Eγ_s / πa)

E = Young's modulus
γ_s = surface energy (J/m²)
a = half crack length

For metals: γ_s replaced by G_c (critical strain energy release rate, includes plastic zone):
σ_f = √(EG_c / πa)
```

**Stress intensity factor:**
```
K_I = Y σ √(πa)

Y = geometry factor (~1 for central crack in infinite plate)
K_IC = fracture toughness (material property, MPa·m^(1/2))

Failure criterion: K_I = K_IC
```

K_IC values:
| Material | K_IC (MPa·m^½) |
|----------|----------------|
| Glass | 0.7 |
| Alumina ceramic | 3–5 |
| Cast iron | 15–20 |
| High-strength Al alloy | 20–30 |
| Structural steel | 50–150 |
| Tough steel (4340) | ~60 |
| Carbon fiber composite | 30–50 |

**Ductile vs brittle fracture:**
- Brittle: rapid, no plastic deformation, flat fracture surface, cleavage planes (BCC metals at low T)
- Ductile: slow, extensive necking, cup-and-cone fracture, dimples under SEM
- DBTT (ductile-brittle transition temperature): BCC steels have DBTT; FCC do not (Charpy impact test)
  - Why Titanic sank: hull steel had DBTT above -2°C seawater temperature → brittle fracture at collision

**Fatigue:** crack initiation + propagation under cyclic loading.
```
da/dN = C(ΔK)^m   (Paris law)

ΔK = Y Δσ √(πa)   (stress intensity range)
Typical: C ~ 10⁻¹¹, m ~ 3–4 for steel

S-N curve (Wöhler): endurance limit at 10⁶ cycles (~0.5 UTS for steels, no limit for Al)
```

Fatigue life dominated by: surface quality (finish, notches), residual stress (shot peening beneficial), environment (corrosion fatigue).

---

## Aluminum Alloys

```
SERIES  MAIN ALLOY  TREATMENT       USE               TYPICAL UTS
1xxx    (pure Al)   none            electrical wire   90 MPa
2xxx    Cu          age hardened    aerospace         440 MPa (2024-T3)
3xxx    Mn          H hardening     beverage cans     150 MPa
5xxx    Mg          strain hardened marine, auto      230 MPa
6xxx    Mg+Si       age hardened    extrusions, auto  290 MPa (6061-T6)
7xxx    Zn          age hardened    aerospace         570 MPa (7075-T6)
```

**7075-T6:** 570 MPa UTS, 503 MPa yield, density 2.81 g/cc → specific strength rivals Ti-6Al-4V.
Used in: aircraft structures, bicycle frames, climbing gear.

---

## Nickel Superalloys

Used in gas turbine hot section (T_service up to 1050°C = 0.8 T_melt). Strength at temperature.

**γ' precipitate (Ni₃Al, Ni₃Ti):** L1₂ ordered FCC structure coherent with FCC γ matrix.
Remarkable: strength INCREASES with temperature up to ~800°C ("yield stress anomaly").
Reason: dislocations in γ' cross-slip from {111} to {001} at high T → locked → stronger.

Modern single-crystal superalloys (CMSX-4, René N5): eliminate grain boundaries → no creep along GBs.
Composition: ~70% Ni, Re (~3%), Mo, W, Ta, Al, Ti, Cr, Co (>10 elements!).
Thermal barrier coatings (YSZ, 100–300 μm) add another 100–150°C capability.

---

## Decision Cheat Sheet

| Application | Material | Why |
|-------------|---------|-----|
| Car body (formable) | IF steel (interstitial-free) + coating | High ductility, paint-bake hardening |
| Car bumper (crash-safe) | AHSS (DP, TRIP) | Energy absorption via TRIP effect |
| Bridge | A572 Grade 50 | Yield 345 MPa, weldable, cheap |
| Aerospace skin | 7075-T6 or 2024-T3 | High specific strength |
| Aerospace spar | 7050-T7451 | Better toughness than 7075 |
| Turbine blade | CM247LC SC | High-T creep resistance |
| Offshore platform | HSLA (S420) | Notch toughness at -40°C |

---

## Common Confusion Points

**1. Phase diagram = equilibrium. Real heat treatment involves kinetics (TTT/CCT).**
Phase diagram tells you what SHOULD exist; actual microstructure depends on cooling rate.
Quench fast enough → skip equilibrium phases entirely → martensite.

**2. Steel "strength" often means yield strength, not UTS.**
Yield: onset of permanent deformation (important for structural design, σ < σ_y for elastic design).
UTS: maximum load-bearing capacity (important for safety factor calculation).
Ductility (elongation %) also critical — a high-strength, zero-ductility material is useless.

**3. Pearlite is not a phase — it's a microstructure (mixture of two phases).**
Pearlite = alternating lamellae of α-ferrite + Fe₃C cementite. Both phases are present.
The eutectoid reaction γ → α + Fe₃C produces this lamellar arrangement.

**4. Overaging weakens despite more precipitate.**
Too long/high aging → precipitates coarsen (Ostwald ripening, driven by surface energy reduction).
Fewer, larger particles → larger interparticle spacing L → lower Orowan stress τ = Gb/L.

**5. Tempered martensite embrittlement (TME) occurs at 250–400°C tempering.**
"Tempered martensite embrittlement" (TME, ~300°C): avoid. Use 400–700°C.
"Temper embrittlement" (TE, slow cool through 350–550°C): impurity (P, Sb, Sn) segregation to prior austenite GBs → intergranular fracture. Molybdenum addition suppresses TE.
