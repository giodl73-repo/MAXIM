# Composite Materials — Landscape and Taxonomy

## The Big Picture

```
+------------------------------------------------------------------+
|                  THE COMPOSITES UNIVERSE                         |
|                                                                  |
|   MATRIX               REINFORCEMENT        COMPOSITE           |
|   ──────               ─────────────        ─────────           |
|   Polymer              Carbon fiber    ──►  CFRP (carbon)       |
|   (thermoset or        Glass fiber     ──►  GRP/GFRP (glass)    |
|    thermoplastic)      Aramid          ──►  Kevlar composite     |
|                        Natural fiber   ──►  Bio-composite        |
|   Metal (Al, Ti, Mg)   Particles/short ──►  Short-fiber         |
|   Ceramic (SiC, Al2O3) Continuous      ──►  Continuous-fiber     |
|                                                                  |
|   HYBRID COMPOSITES: multiple fiber types in one structure      |
|   SANDWICH STRUCTURE: thin face sheets + low-density core       |
+------------------------------------------------------------------+
```

A composite = two or more distinct constituent materials combined to yield
properties neither constituent possesses alone. The constituent materials
remain distinct at the macroscopic scale (distinguishable phases).

Global composites market: ~$120 billion/yr (2023), growing ~6%/yr
CFRP specifically: ~$35 billion, growing faster than glass

---

## The Matrix + Reinforcement Model

```
   WHY COMPOSITES OUTPERFORM EITHER CONSTITUENT:
   ──────────────────────────────────────────────
   CARBON FIBER alone:
   - Very strong in tension (5,000 MPa)
   - Very brittle (strain to failure: ~1.5%)
   - Poor in compression (microbuckling of individual fiber)
   - Poor shear, impact properties
   - Cannot be shaped easily

   EPOXY ALONE:
   - Moderate tensile strength (70–90 MPa)
   - Low modulus (3.5 GPa)
   - Can be shaped/molded

   CFRP (60% fiber volume fraction):
   - Tensile strength: 1,200–1,500 MPa (fiber-dominated)
   - Modulus: 70–100 GPa (fiber-dominated)
   - Compression: 800–1,000 MPa (matrix stabilizes fiber)
   - Weight: 1.55 g/cm³ (lighter than aluminum: 2.7 g/cm³)
   - Specific strength: ~900 MPa·cm³/g (aluminum: ~90)
```

---

## Four Ways to Classify Composites

### 1. By Matrix Type

```
   POLYMER MATRIX COMPOSITES (PMC) — dominant (~90% of market)
   ─────────────────────────────────
   Thermoset: epoxy (aerospace), vinyl ester (marine), phenolic (aircraft)
   Thermoplastic: PEEK (aerospace), PP (automotive), PA (sporting goods)
   Temperature limit: typically 100–250°C

   METAL MATRIX COMPOSITES (MMC) — specialty
   ──────────────────────────────
   Aluminum + SiC particles: light, wear-resistant
   Ti + SiC fibers: aerospace (fan blade at expensive)
   Al + graphite: electronic thermal management

   CERAMIC MATRIX COMPOSITES (CMC) — extreme environment
   ────────────────────────────────
   SiC/SiC, SiC/C, Al2O3/Al2O3
   Use: gas turbine blades (2000°C+), re-entry vehicles
   Challenge: brittle, difficult manufacturing
```

### 2. By Fiber Architecture

```
   CONTINUOUS FIBER (0D to continuous):
   ─────────────────────────────────────
   Unidirectional (UD): all fibers parallel
   Woven fabric: fibers in 0° and 90°
   Multiaxial (NCF): several directions, stitched
   Braided: tubular, complex shapes

   DISCONTINUOUS FIBER:
   ─────────────────────
   Chopped strand mat (CSM): random, 25–50 mm fibers
   Short fiber (injection molded): 0.2–1 mm after processing
   Long fiber (LFT): 5–25 mm in molded part
```

### 3. By Fiber Volume Fraction (Vf)

```
   LOW Vf (25–40%)    MEDIUM Vf (40–55%)    HIGH Vf (55–65%)
   ─────────────────  ─────────────────────  ─────────────────
   RTM, infusion      Prepreg autoclave      High-pressure RTM
   lower stiffness    aviation standard      aerospace, racing
   lower cost         best balance           highest performance
   more matrix        typical aerospace Vf   requires high pressure
```

### 4. By Manufacturing Route

```
   WET LAY-UP → HAND LAY-UP → CURE (low cost, low quality)
   RTM (Resin Transfer Molding) → closed mold, good fiber/resin control
   PREPREG / AUTOCLAVE → aerospace standard, highest quality
   PULTRUSION → continuous profiles, lowest cost/weight for rod, beam
   FILAMENT WINDING → pipes, pressure vessels, golf clubs
   AFP/ATL (automated fiber placement) → modern large structure fabrication
```

---

## Key Performance Metrics

```
SPECIFIC PROPERTIES (normalized by density):
────────────────────────────────────────────

Specific Strength = σ_UTS / ρ   [MPa / (g/cm³)] = [kN·m/kg]
Specific Modulus  = E / ρ       [GPa / (g/cm³)] = [MN·m/kg]

MATERIAL COMPARISON:
──────────────────────────────────────────────────────────
                  ρ      E      σ_UTS   E/ρ    σ/ρ
                g/cm³   GPa    MPa    GPa·g⁻¹  MPa·g⁻¹
                                        cm³      cm³
Mild steel       7.8    210    400     27       51
Aluminum 2024   2.77    73     470     26      170
Ti-6Al-4V       4.43   114     950     26      214
CF/epoxy (UD)   1.55   130   1,500     84      968
GF/epoxy (UD)   2.10    45     750     21      357
Kevlar/epoxy    1.36    80   1,400     59     1029

CFRP dominates specific modulus and specific strength — hence aerospace.
```

---

## The Weight/Cost Tradeoff

```
   COST-PERFORMANCE MAP:

   PERFORMANCE (specific modulus / strength)
   HIGH  │                         [CF/epoxy autoclave]
         │                    [CF/epoxy RTM]
         │               [CFRP short fiber]
         │         [Kevlar/epoxy]
         │    [GF/epoxy]
   LOW   │  [Steel]   [Aluminum]
         └──────────────────────────────────────────────→ COST
           LOW ($1/kg steel)                    HIGH ($300+/kg CF autoclave part)
```

This is why composites adoption follows a predictable diffusion:
1. Space / military (cost blind)
2. Racing / high-end sport (performance premium)
3. Commercial aerospace (fuel savings justify cost)
4. Automotive (learning curve reduces cost → mass market)
5. Wind energy (volume drives cost down → energy economics)

---

## Directory Contents

| File | Topic |
|------|-------|
| 01-FUNDAMENTALS.md | Rule of mixtures, fiber-matrix interaction, interface |
| 02-FIBER-TYPES.md | Carbon, glass, aramid, natural fibers — properties comparison |
| 03-MATRIX-SYSTEMS.md | Epoxy, VE, phenolic, PEEK, PP — matrix selection |
| 04-LAMINATE-THEORY.md | Classical Laminate Theory (CLT): ABBD matrix |
| 05-MANUFACTURING.md | Prepreg, autoclave, infusion, RTM, AFP |
| 06-DESIGN-ANALYSIS.md | Failure criteria, fatigue, joint design, FEA |
| 07-BOEING-787.md | Case study: 787 Dreamliner composites program |
| 08-DAMAGE-INSPECTION.md | Damage types, NDT methods (UT, thermography, shearography) |
| 09-END-OF-LIFE.md | Recycling, pyrolysis, mechanical recycling, reuse |

---

## Decision Cheat Sheet — Which Composite?

| Requirement | Composite type |
|-------------|---------------|
| Lightweight aerospace structure | CF/epoxy prepreg (autoclave or AFP) |
| Marine hull / boat | GF/vinyl ester (hand lay-up or infusion) |
| Automotive CFRP (cost-sensitive) | CF/epoxy RTM or CF-SMC |
| Ballistic protection / soft armor | Aramid (Kevlar) + PE |
| Wind turbine blade | GF/epoxy or GF+CF hybrid, infusion |
| Pressure vessel / pipe | Filament-wound GF or CF/epoxy |
| Automotive underbody structure | Long-fiber thermoplastic (LFT-PP) |
| High-temperature aerospace | CMC (SiC/SiC) or CF/polyimide |
| Large structural infused part | E-glass / vinyl ester / VARTM |

---

## Common Confusion Points

**Composite ≠ just carbon fiber**: The word "composite" encompasses plywood
(wood + resin), concrete (aggregate + cement), carbon-carbon (CF + carbon matrix),
metal matrix, and ceramic matrix systems. In casual engineering usage it usually
means fiber-reinforced polymer (FRP), but the technical term is broader.

**Higher fiber volume fraction is not always better**: At Vf > 65–70%, the matrix
cannot fully wet all fibers — voids form, impairing interlaminar shear strength
and fatigue. Autoclave prepreg achieves 58–62% Vf by design. Going to 65% requires
specialty processes (filament winding with compaction, dry fiber + high-pressure
resin).

**Composites are anisotropic**: A UD ply has E = 130 GPa in fiber direction and
E = 10 GPa transverse. A quasi-isotropic laminate [0/+45/–45/90]s is roughly
isotropic in-plane but still has different through-thickness properties. Treating
CFRP like isotropic aluminum in FEA is a common and costly mistake.
