# Polymers — Chain Architecture, Thermal Transitions, Mechanics

---

## Big Picture

```
MONOMER → POLYMER (repeat units linked into long chains)
        │
        ├── CHAIN ARCHITECTURE → crystal structure (or lack of it)
        │
        ├── MOLECULAR WEIGHT DISTRIBUTION → processing behavior, toughness
        │
        ├── T_g (glass transition) and T_m (melting)
        │        → define service temperature window
        │
        └── MECHANICAL RESPONSE = viscoelastic
                → time-dependent: E*(ω) = E'(ω) + iE''(ω)
                → temperature-dependent: WLF equation
```

---

## Chain Architecture

```
LINEAR:     ─●─●─●─●─●─●─●─   (HDPE, nylon, PET)
BRANCHED:   ─●─●─●─●─●─     (LDPE: random branches)
              │   │
              ●   ●─●
CROSSLINKED: ─●─●─X─●─●─     (vulcanized rubber, epoxy thermoset)
                  │
              ─●─●─●─
STAR:            /          (used in block copolymer templates)
         ─●─●─●─●─●─●─
                  \
               ─●─●─
DENDRITIC:  perfect branching → sphere-like, very different properties
```

**Tacticity** (stereoregularity of side groups along backbone):
```
ISOTACTIC:   all R groups on same side → crystallizes easily (iPP)
SYNDIOTACTIC: R groups alternate → crystallizes (sPP, but less common)
ATACTIC:     R groups random → amorphous (aPS: clear, but brittle)
```

**Copolymers:**
```
RANDOM: -AABBABABBA-   (SBR rubber: random styrene-butadiene)
ALTERNATING: -ABABAB-  (specific synthesis required)
BLOCK: -AAAA-BBBB-     (SBS thermoplastic elastomer: PS-PB-PS)
GRAFT: AAAA backbone with BBBB side chains
```

Block copolymers (BCPs) phase-separate at nanoscale (lamellar, cylindrical, spherical, gyroid)
→ self-assembled templates for nanolithography (Intel, IBM). Domain size ~10–100 nm.

---

## Molecular Weight and Distributions

Polymer chains have a distribution of lengths. Two averages matter:

```
NUMBER-AVERAGE molecular weight:
M_n = Σ N_i M_i / Σ N_i   (average molecule count per chain length)

WEIGHT-AVERAGE molecular weight:
M_w = Σ N_i M_i² / Σ N_i M_i   (biased toward longer, heavier chains)

PDI (polydispersity index) = M_w / M_n ≥ 1

Narrow distribution (PDI → 1): living polymerization, anionic
Broad distribution (PDI = 2): free radical polymerization (most industrial)
Very broad (PDI = 5–20): condensation polymerization
```

**Effect on properties:**
- M_n controls: colligative properties (freezing point depression, osmotic pressure)
- M_w controls: melt viscosity (η ∝ M_w^3.4 for M > M_c entanglement), tensile strength
- PDI: broad → wider processing window but lower ultimate properties

**Entanglement molecular weight M_c:**
Above M_c: chains are physically entangled → plateau modulus G_N^0 ~ 10⁵–10⁶ Pa.
Below M_c: low melt viscosity, weak film.

---

## Crystallinity and Morphology

**Semicrystalline polymers:** partially ordered. True 100% crystalline is rare.

**Crystallization:** regular chain segments fold into lamellae (~10–50 nm thick).
Lamellae radiate from nuclei → spherulites (μm scale, visible under polarized light as Maltese cross).

```
Crystal structure examples:
PE (polyethylene):  orthorhombic, chains in all-trans (zig-zag) conformation
PET: triclinic, requires slow cooling or drawing
iPP: α-form monoclinic, β-form hexagonal (tougher, less common)
```

**Degree of crystallinity X_c:**
```
X_c = ΔH_f(sample) / ΔH_f^∞   (measured by DSC, compare to 100% crystal)

or from density: X_c = (ρ_s - ρ_a)/(ρ_c - ρ_a)

ρ_c = density of perfect crystal
ρ_a = density of fully amorphous
```

Crystallinity affects:
| Property | Effect of higher X_c |
|----------|---------------------|
| Stiffness E | ↑ (crystals stiffer than amorphous) |
| Strength | ↑ |
| Transparency | ↓ (crystals scatter light if λ_crystal > λ_visible) |
| Barrier (O₂, H₂O) | ↑ (crystallites are impermeable) |
| Chemical resistance | ↑ (solvent can't penetrate crystal) |
| Elongation to break | ↓ |

**Quench from melt:** suppress crystallization → amorphous. Then anneal below T_m → crystallize.

---

## Thermal Transitions

### Glass Transition Temperature T_g

**Physical meaning:** below T_g, chain segments are frozen (glassy solid). Above T_g, chain segments have enough thermal energy to undergo cooperative rearrangement (rubbery state).

NOT a thermodynamic phase transition (no latent heat) — it's a kinetic phenomenon.
T_g depends on cooling rate (faster cooling → higher apparent T_g).

**Free volume theory:**
```
v_f = v - v_0   (free volume = actual volume - occupied volume)

At T_g: v_f / v ≈ 0.025 (universal ~ 2.5% free volume)

α_liquid > α_glass   (thermal expansion coefficient larger above T_g)
v_f increases linearly with T above T_g
```

**Factors that increase T_g:**
| Factor | Effect | Example |
|--------|--------|---------|
| Stiffer backbone | ↑ T_g | PC > PE (phenylene vs -(CH₂)ₙ-) |
| Bulkier side groups | ↑ T_g | PS (phenyl) >> PE: PS T_g = 100°C, PE T_g = -80°C |
| Polar groups | ↑ T_g | PVC (Cl) T_g = 87°C vs PE T_g = -80°C |
| Crosslinks | ↑ T_g | Increase with crosslink density |
| Plasticizer | ↓ T_g | Add flexible small molecule (DOP) → increases free volume |

Representative T_g values:
| Polymer | T_g (°C) |
|---------|---------|
| PDMS (silicone) | -123 |
| Polybutadiene | -85 |
| PE (HDPE) | -80 |
| PP (atactic) | -20 |
| PET | 69 |
| PVC | 87 |
| PMMA | 105 |
| PS | 100 |
| PC | 145 |
| Epoxy (cured) | 80–200 |
| PEEK | 143 |
| PI (Kapton) | >300 |

### Melting Temperature T_m

Only for crystalline/semicrystalline polymers.

```
T_m = ΔH_f / ΔS_f   (equilibrium for perfect crystal)

Higher T_m: higher ΔH_f (stronger intermolecular forces, e.g., H-bonds) or
            lower ΔS_f (stiffer chain, less entropy gain upon melting)
```

Key relationships:
- T_m > T_g always (for same polymer)
- T_g/T_m ≈ 0.5–0.8 (K/K) — empirical rule, Kauzmann's ratio

**Semicrystalline service window:**
```
Below T_g: rigid, brittle glassy solid
T_g to T_m: rubbery, leathery, tough (best mechanical performance)
Above T_m: flows (melt processing window)
Above T_decomp: pyrolysis
```

---

## Rubber Elasticity (Entropy Spring)

**Physical picture:** crosslinked network. Stretch → reduce conformational entropy of chains.
Restoring force is ENTROPIC (like a stretched ideal gas), not enthalpic.

**Statistical mechanics of a single chain:**
For a freely-jointed chain with N links of length l:
```
End-to-end distance at equilibrium: ⟨r²⟩ = Nl²
Probability: P(r) = (3/2πNl²)^(3/2) exp(-3r²/2Nl²)   (Gaussian for small r/Nl)

Entropy: S(r) = k_B ln P(r) = const - 3k_B r²/(2Nl²)
Force: f = -T ∂S/∂r = 3k_BT r/(Nl²)   ← Hooke's law! Spring constant k = 3k_BT/(Nl²)
```

**Macroscopic neo-Hookean model:**
For an incompressible crosslinked network with n chains per unit volume:
```
σ = nk_BT (λ - 1/λ²)   (for uniaxial extension, λ = stretch ratio)

Small strain: σ ≈ nk_BT · 3ε = Eε   where E ≈ 3nk_BT = 3G

G = nk_BT = (ρ/M_c)RT   (shear modulus from network density)
```

**Key features of rubber elasticity:**
1. Modulus increases with temperature (opposite of metals!) — pure entropy
2. G ~ 0.1–10 MPa (very low compared to metals: ~10–200 GPa)
3. Large deformation (λ up to ~8) before failure
4. Rate-independent for ideal rubber (no viscous dissipation)

Real rubber deviates from neo-Hookean at large stretch (chains approach finite extensibility → Langevin chain model).

---

## Viscoelasticity

Real polymers are neither purely elastic (spring) nor purely viscous (dashpot) — they're both.

### Models

**Maxwell model** (spring + dashpot in series):
```
ε = ε_spring + ε_dashpot
dε/dt = (1/E)(dσ/dt) + σ/η

Creep at const σ: ε(t) = σ(1/E + t/η) — grows without bound
Stress relaxation at const ε: σ(t) = σ_0 exp(-t/τ)  where τ = η/E
```

**Kelvin-Voigt model** (spring + dashpot in parallel):
```
σ = Eε + η(dε/dt)

Creep at const σ: ε(t) = (σ/E)[1 - exp(-t/τ)]  — bounded, reaches equilibrium
Good for creep; poor for stress relaxation (predicts instant recovery)
```

**Standard Linear Solid (SLS):** adds spring in series with Kelvin-Voigt → captures both.

### Dynamic Mechanical Analysis (DMA)

Apply oscillatory strain: ε = ε_0 sin(ωt)
Response: σ = σ_0 sin(ωt + δ)

```
E* = E' + iE''

E' = storage modulus = σ_0/ε_0 cos δ   (elastic, in-phase component)
E'' = loss modulus  = σ_0/ε_0 sin δ    (viscous, out-of-phase)
tan δ = E''/E'   (loss tangent, measure of damping)
```

DMA E' vs T spectrum:
```
E' (Pa)
10⁹ │ ──────────────── Glassy plateau
    │              ↘
10⁷ │               ──── Rubbery plateau (if crosslinked)
    │               T_g → glass transition (tan δ peak)
10⁵ │                    ──── Flow (if uncrosslinked)
    └────────────────────────── T (°C)
                    ↑
               T_g from tan δ peak
               (slightly higher than DSC midpoint T_g)
```

### WLF Equation (Time-Temperature Superposition)

A master curve can be constructed by shifting DMA data:

```
log a_T = -C₁(T - T_ref) / (C₂ + T - T_ref)

Universal constants near T_g: C₁ = 17.44, C₂ = 51.6 K (with T_ref = T_g)
a_T = horizontal shift factor; higher T → shift left (faster dynamics)

Physical basis: free volume theory — α_f = 4.8×10⁻⁴/K is universal
```

**Practical implication:** lower T ↔ faster frequency (same effect on modulus).
Polymer tested at 1 Hz, 150°C: equivalent to 10⁶ Hz, room temperature.
→ Crash testing at slow rate is NOT equivalent to high-rate impact.

---

## Thermoplastics vs Thermosets vs Elastomers

```
                    THERMOPLASTICS
                    ──────────────
                    Melt and reflow above T_m (semi-crystalline) or T_g (amorphous)
                    Recyclable (in principle)
                    Processing: injection molding, extrusion, blow molding
                    Examples: PE, PP, PS, PET, Nylon, PEEK, PC

                    THERMOSETS
                    ──────────
                    Crosslinked during curing (irreversible network)
                    Cannot be remelted
                    Processing: RIM, RTM, pultrusion (composites), casting
                    Examples: epoxy, vinyl ester, phenolic, BMI, DGEBA/amine
                    T_g can be 80°C (epoxy/amine) to 250°C+ (bismaleimide)

                    ELASTOMERS
                    ──────────
                    Lightly crosslinked → rubbery at service T
                    T_g << service temperature (usually room T)
                    High elongation, entropy-spring mechanics
                    Examples: NR (natural), SBR, EPDM, silicone (PDMS), nitrile (NBR)
                    Vulcanization: sulfur crosslinks -S- or -S₂- between chains
```

**Thermoplastic elastomers (TPE):** no chemical crosslinks — physical crosslinks from
hard block domains (PS in SBS triblock): deform elastically due to network; melt above
T_g of hard block (PS, 100°C) → processable like thermoplastic. Used in soles, grips, seals.

---

## Processing Fundamentals

**Melt viscosity:**
```
η_0 ∝ M_w^3.4   (for M_w > M_c)   (entangled regime)
η_0 ∝ M_w^1     (for M_w < M_c)   (Rouse regime)

Shear thinning: η(γ̇) = η_0 (1 + (λγ̇)^(1-n))^((n-1)/1)   (Cross model)
Power law: η = K γ̇^(n-1)   (n < 1 for shear thinning; most polymer melts)
```

Viscosity temperature dependence:
```
η(T) = η_ref exp[-C₁(T - T_ref)/(C₂ + T - T_ref)]   (WLF above T_g)
η(T) = A exp(E_a/RT)   (Arrhenius, for T >> T_g)
```

**Processing windows:**
| Process | Requirement | Typical T | Typical γ̇ (s⁻¹) |
|---------|------------|-----------|-----------------|
| Injection molding | Low η, fast fill | T_m + 20–50°C | 10³–10⁵ |
| Extrusion | Stable flow | T_m + 10–30°C | 10²–10³ |
| Compression molding | Low η, closed mold | T_m or cure T | 0.1–10 |
| Fiber spinning | Draw stability | T_m + 30°C | 10³–10⁵ |
| Film blowing | Melt strength | T_m + 10°C | 10²–10³ |

---

## Common Engineering Polymers — Reference Card

| Polymer | T_g (°C) | T_m (°C) | E (GPa) | σ_UTS (MPa) | Notable for |
|---------|---------|---------|---------|------------|------------|
| HDPE | -80 | 135 | 1.0 | 30 | Chemical resistance, pipes |
| PP | -20 | 160–165 | 1.5 | 35 | Hinge fatigue resistance, living hinges |
| PS | 100 | — | 3.2 | 50 | Brittle, clear, cheap |
| PMMA | 105 | — | 3.3 | 72 | Optically clear, "plexiglass" |
| PVC | 87 | — | 3.0 | 50 | Flame retardant (Cl), pipe, cable |
| PC | 145 | — | 2.4 | 65 | Impact resistant, bulletproof glass |
| PET | 69 | 255 | 3.1 | 55 | Bottles, fiber (polyester), biaxial film |
| Nylon 66 | 50 | 265 | 2.8 | 80 | Gears, bearings (moisture absorbs) |
| PEEK | 143 | 343 | 3.6 | 100 | High T, chemical resistant, implants |
| PTFE | -97 | 327 | 0.5 | 35 | Lowest friction, chemical inert, Teflon |
| Epoxy (cured) | 80–200 | — | 3–4 | 60–90 | Adhesive, composite matrix |
| NR (rubber) | -70 | — | 0.001–0.01 | 20–30 | Natural, high tear strength |

---

## Decision Cheat Sheet

| Need | Choose | Avoid |
|------|--------|-------|
| High T service (> 200°C) | PEEK, PI, PPS, BMI | Most standard thermoplastics |
| Optical clarity | PMMA, PC, PS, PET film | Any semicrystalline at large grain |
| Living hinge (flex millions of cycles) | PP | PC, PMMA (brittle in fatigue) |
| Chemical resistance | PTFE, HDPE, PVDF | Nylon (absorbs water), PC (attacked by ketones) |
| Low friction bearing | PTFE, UHMWPE, Nylon | Rubber, PS |
| Thermoset matrix for CFRP | Epoxy | Thermoplastics (higher T_process) |
| Recyclable flexible packaging | LDPE film, PP, PET | Thermosets |
| Wearable electronics substrate | PI (Kapton) film | Rigid thermosets |

---

## Common Confusion Points

**1. T_g is not the maximum service temperature.**
Above T_g: polymer is rubbery but still solid (if semicrystalline, until T_m).
Maximum service T is application-dependent: medical device needs T_g >> autoclave (134°C).

**2. WLF time-temperature equivalence only works in the 50°C window around T_g.**
Far above T_g (> T_g + 100°C): Arrhenius behavior, not WLF.
Crystallization kinetics do NOT obey WLF.

**3. Modulus of rubber INCREASES with T (opposite of metals).**
Metal: E decreases with T (atoms vibrate more → weaker effective spring constant).
Rubber: G = nk_BT → proportional to T. Cooling rubber stiffens it (eventually vitrifies at T_g).

**4. Crosslinking and crystallinity both increase stiffness but by different mechanisms.**
Crosslinks: restrict chain mobility → network rubber modulus G = nk_BT.
Crystallinity: rigid crystal phase parallel to amorphous → composite model (Takayanagi).
A crosslinked amorphous network (silicone rubber) and a semicrystalline thermoplastic (HDPE)
can have similar stiffness by completely different mechanisms.

**5. Molecular weight PDI = 1 does NOT mean all chains are exactly the same length.**
PDI = 1 means the distribution is monodisperse, but there's still a narrow distribution.
Only living polymerization approaches PDI = 1.01–1.10. Free radical always gives PDI ≈ 2.
