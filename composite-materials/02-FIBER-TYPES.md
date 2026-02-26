# Fiber Types: Carbon, Glass, Aramid, Natural

## The Big Picture

```
+------------------------------------------------------------------+
|              REINFORCEMENT FIBER LANDSCAPE                       |
|                                                                  |
|   CARBON FIBER   GLASS FIBER    ARAMID       NATURAL            |
|   ───────────    ───────────    ──────       ───────            |
|   CFRP / GFRP split of market: 30% CF / 65% GF / 5% other     |
|                                                                  |
|   Carbon:        Glass:         Aramid:      Flax, hemp,        |
|   High E, high σ Low cost       Ballistic     jute, basalt       |
|   Low density    Good E/ρ       Tensile str   Bio-sourced       |
|   Brittle in     Isotropic fib  Weak in       Lower property     |
|   compression    Toughened sys  compression   but sustainable   |
|                                                                  |
|   $25–200/kg     $1.5–8/kg      $20–60/kg    $2–15/kg          |
+------------------------------------------------------------------+
```

---

## Carbon Fiber

### Production: PAN-Based (Dominant)

~96% of commercial carbon fiber is PAN (polyacrylonitrile) based.

```
   PAN PRECURSOR FIBER → CF CONVERSION:
   ──────────────────────────────────────
   1. OXIDATIVE STABILIZATION: 200–300°C in air, several hours
      PAN → stabilized ladder polymer (ring cyclization)
      Removes hydrogen, adds oxygen linkages
      Purpose: prevent melting during high-T carbonization

   2. CARBONIZATION: 1,000–1,600°C in inert atmosphere (N2)
      Removes N, H, O → turbostratic graphite structure
      Density: ~1.75 g/cm³ → increasing toward graphite (2.26 g/cm³)
      Fiber diameter: 5–8 µm

   3. GRAPHITIZATION (optional, for HM grades): 2,000–3,000°C
      Aligns graphene planes parallel to fiber axis
      → Higher modulus (ultrahigh modulus grades: >400 GPa)
      → Lower tensile strength (more brittle)

   4. SURFACE TREATMENT + SIZING: electrolytic oxidation, size applied
```

### Carbon Fiber Grade System

```
   STANDARD MODULUS (SM): E ~ 220–240 GPa   (Torayca T300, Hexcel AS4)
   INTERMEDIATE MODULUS (IM): E ~ 275–295 GPa  (Torayca T800, IM7)
   HIGH MODULUS (HM): E ~ 350–500 GPa   (Torayca M40, M55)
   ULTRAHIGH MODULUS (UHM): E > 500 GPa  (Torayca M60, M70)

   PROPERTY TRADE-OFF:
   ─────────────────────
   As modulus increases (more graphitization):
   ↑ Tensile modulus  ↑ Electrical conductivity  ↓ Density
   ↓ Tensile strength ↓ Strain to failure        ↑ Cost

   Most aerospace uses IM (IM7, T800H):
   best combination of modulus, strength, and failure strain
```

### Standard Carbon Fiber Tow Sizes

```
   TOWS (bundle of continuous filaments):
   ──────────────────────────────────────
   1K, 3K, 6K, 12K, 24K, 48K, 50K, 300K

   K = 1,000 filaments
   3K (3,000 filaments/tow): aerospace standard (best quality control, expensive)
   12K: aerospace secondary, structural infusion
   24K–48K: wind blade, automotive, industrial
   50K (large tow): lowest cost/kg, some property penalty from spreading issues

   Aerospace prepreg: predominantly 6K/12K
   Wind blade infusion: 24K–48K
   Chopped fiber SMC: 24K–50K
```

### Carbon Fiber Manufacturers

```
   JAPANESE (dominant, ~50% global):
   ─────────────────────────────────
   Toray: T300, T700, T800, T1000 (PAN), M series (HM/UHM)
   Teijin (Toho Tenax): STS, IMS, HTS, UTS
   Mitsubishi Chemical: Pyrofil

   US:
   ────
   Hexcel: AS4, IM7 (aerospace standard for Boeing/Airbus), HM63
   Cytec/Solvay: (formerly)

   GERMAN:
   ───────
   SGL Carbon: SIGRAFIL

   Global CF capacity ~2023: ~150,000 t/yr, growing rapidly
   Demand growing: wind (largest), aerospace, automotive
```

---

## Glass Fiber

### Types of Glass Fiber

```
   E-GLASS (electrical grade) — >90% of all glass fiber produced:
   ──────────────────────────────────────────────────────────────
   Composition: SiO2 + Al2O3 + CaO + MgO + B2O3
   E (modulus): ~72 GPa
   σ_UTS: ~2,400–3,500 MPa (depending on diameter + surface treatment)
   ρ: 2.57–2.60 g/cm³
   Cost: ~$1.5–4/kg
   Applications: 90% of all FRP marine, construction, consumer

   S-GLASS (structural):
   ──────────────────────
   Higher SiO2 (65%) + MgO: stronger but no B2O3
   E: ~85–87 GPa (+20% vs. E-glass)
   σ_UTS: ~4,600 MPa (+35–40% vs. E-glass)
   ρ: 2.48 g/cm³
   Cost: ~$15–25/kg (3–10× E-glass)
   Applications: aerospace secondary, ballistic, pressure vessel
   S2-glass: same composition, lower cost via different filament drawing

   R-GLASS (European equivalent to S-glass):
   ECR GLASS (corrosion resistant):
   AR-GLASS (alkali resistant — for cement):
```

### Glass Fiber Manufacturing

```
   GLASS BATCH MELT → BUSHING → DRAWING → COATING → CHOPPING/WINDING
   ─────────────────────────────────────────────────────────────────
   Bushing: platinum-rhodium alloy plate with 400–8,000 holes (tips)
   Fibers pulled at 60 m/s from molten glass
   Diameter set by: glass viscosity + draw speed
   Standard: E = 6–25 µm, S = 8–13 µm

   SIZING:
   ───────
   Applied immediately after forming (before fiber-fiber contact)
   Lubricant: prevents abrasion between filaments
   Film former: holds bundle integrity
   Coupling agent (silane): chemical bond to matrix
   Compatibility: epoxy-compatible vs. polyester-compatible sizings
```

### Glass Fiber Coupling Agents

```
   SILANE COUPLING AGENTS (most important):
   ──────────────────────────────────────────
   Structure: (RO)3Si–CH2CH2CH2–X
   R = methyl or ethyl (hydrolyzes to Si-OH)
   X = functional group matched to matrix chemistry

   Matrix        Silane type                   X group
   Epoxy:        Gamma-glycidoxypropyltrimethoxysilane  epoxide
   Polyester:    Gamma-methacryloxypropyltrimethoxysilane  methacrylate
   PP (nylon):   Aminopropyltriethoxysilane    amine

   Mechanism:
   Si-OH + HO-glass surface → Si-O-glass (chemical bond)
   X group reacts with matrix → X-matrix bond
   Net: glass ──silane── matrix (two chemical bonds)
   Without silane: E-glass + water → rapid strength loss (hydrolysis attacks
   glass-matrix interface → delamination in wet environments)
```

---

## Aramid Fibers

Aromatic polyamide fibers. Trademark: Kevlar (DuPont), Twaron (Teijin).

### Chemistry and Structure

```
   PPTA (poly-p-phenylene terephthalamide) — KEVLAR:
   ──────────────────────────────────────────────────
   [–NH–C6H4–NH–CO–C6H4–CO–]n

   RIGID ROD polymer:
   Phenyl rings + amide bonds (planar, rigid)
   Para-linked → fully extended conformation in solution
   Lyotropic liquid crystal above critical concentration in H2SO4

   SPINNING: liquid crystal solution (~ anisotropic nematic phase)
   Dry-jet wet spinning into water bath
   Chains highly aligned along fiber axis → exceptional fiber properties

   INTERMOLECULAR HYDROGEN BONDING:
   ──────────────────────────────────
   N–H ··· O=C (amide H-bond)
   Forms hydrogen bonded sheets perpendicular to fiber axis
   → Transverse bonding, not covalent → explains poor compression
```

### Aramid Properties

```
   TENSILE:     σ_UTS = 2,800–3,600 MPa
   MODULUS:     E = 70–125 GPa (Kevlar 49: 125 GPa)
   DENSITY:     ρ = 1.44–1.45 g/cm³
   εf (failure strain): 2.4–3.6%
   COMPRESSIVE STRENGTH: ~250–300 MPa (very low — H-bond planes buckle)
```

The compression failure mechanism:
```
   Under compression: kink bands form along H-bonded planes
   H-bonds are strong in-plane but the planes can slide
   → Fibrous/delaminated failure in compression
   → NEVER use aramid in primary compression applications
   → Use in: tension-loaded structures, ballistic, hybrid with CF
```

### Kevlar Grades

| Grade | E (GPa) | σ_UTS (MPa) | ε (%) | Application |
|-------|---------|-------------|-------|-------------|
| Kevlar 29 | 70 | 2,800 | 3.6 | Soft armor, rope, cut resistance |
| Kevlar 49 | 125 | 2,800 | 2.4 | Hard armor, composite, cable |
| Kevlar 129 | 99 | 3,400 | 3.3 | Enhanced ballistic, armor |
| Kevlar XP | — | 3,600 | — | Ballistic premium |
| Twaron CT713 | 80 | 2,800 | 3.5 | Tire reinforcement |

### Aramid Challenges

```
   MOISTURE ABSORPTION: 3.5–7% (vs. CF: 0.2%)
   Effect: 20–30% reduction in tensile strength at saturation
   Compressive strength: further reduced by moisture

   UV SENSITIVITY: photodegrades at UV exposure
   → Must protect from UV in outdoor applications
   → HDPE jacket for ropes, UV-opaque matrix for composites

   DIFFICULT TO CUT/DRILL: fibers "whisker" rather than cut cleanly
   → Use ceramic blades, laser cutting, or diamond wire
   → Delamination during drilling if incorrect tooling

   POOR ADHESION TO MATRICES:
   Smooth surface, chemically inert → poor chemical bonding
   Solutions: plasma treatment, acid etching, silane coupling
   ILSS achievable: 30–45 MPa (vs. 80+ for CF with sizing)
```

---

## Natural Fibers

### Major Natural Fiber Reinforcements

```
   FLAX (Linum usitatissimum):
   ────────────────────────────
   E: 50–70 GPa   σ_UTS: 500–1,500 MPa   ρ: 1.40–1.50 g/cm³
   Specific modulus: 35–47 GPa·cm³/g  (vs. E-glass: 28)
   High cellulose content (~71%), low microfibrillar angle (5–10°)

   HEMP (Cannabis sativa):
   ────────────────────────
   E: 35–70 GPa   σ_UTS: 350–900 MPa   ρ: 1.48 g/cm³
   Similar to flax, slightly lower properties

   JUTE (Corchorus sp.):
   ──────────────────────
   E: 25–55 GPa   σ_UTS: 200–500 MPa   ρ: 1.30–1.45 g/cm³
   Lower properties, very low cost
   Used: backing for carpets, civil reinforcement

   SISAL (Agave sisalana):
   ────────────────────────
   E: 9–22 GPa   σ_UTS: 200–600 MPa   ρ: 1.33–1.50 g/cm³
   Lower stiffness — more ductile

   KENAF (Hibiscus cannabinus):
   ─────────────────────────────
   E: 14–53 GPa   σ_UTS: 300–900 MPa   ρ: 1.19–1.25 g/cm³
   Very fast growing, emerging automotive use
```

### Natural Fiber Challenges

```
   HYDROPHILICITY:
   ───────────────
   Cellulose: –OH groups absorb moisture
   Moisture: swells fiber → poor fiber-matrix adhesion
   Solutions: chemical modification (acetylation, silane treatment, maleic
              anhydride graft for PP)

   THERMAL STABILITY:
   ───────────────────
   Cellulose degrades ~200°C
   → Cannot use with high-temperature processing matrices
   → Limited to epoxy (cure < 120°C), unsaturated PE, PP

   VARIABILITY:
   ─────────────
   Agricultural product: year-to-year, field-to-field variation
   Diameter variation within same fiber: 50–100% range
   → Difficult to predict properties precisely
   → Less suitable for critical structural applications

   APPLICATIONS WHERE NATURAL FIBER WINS:
   ─────────────────────────────────────────
   Automotive interior (door panels, headliners, trunk liners)
   Agricultural equipment
   Noise/vibration damping (better than GF composites)
   Sustainability claim (bio-sourced, compostable end-of-life)
   Cost advantage in high-volume, low-load applications
```

---

## Fiber Property Comparison

| Property | CF (IM) | E-glass | S-glass | Kevlar 49 | Flax |
|----------|---------|---------|---------|-----------|------|
| Density (g/cm³) | 1.78 | 2.57 | 2.49 | 1.44 | 1.45 |
| Tensile E (GPa) | 290 | 72 | 87 | 125 | 60 |
| Tensile σ (MPa) | 5,500 | 3,400 | 4,600 | 2,800 | 900 |
| Strain to failure (%) | 1.9 | 4.8 | 5.4 | 2.4 | 2.3 |
| Specific E (GPa·cm³/g) | 163 | 28 | 35 | 87 | 41 |
| Specific σ (MPa·cm³/g) | 3,090 | 1,323 | 1,847 | 1,944 | 621 |
| Cost ($/kg approx) | 25–200 | 1.5–4 | 15–25 | 20–60 | 2–8 |
| Moisture absorption | <0.2% | ~0.1% | ~0.1% | 3–7% | 10–15% |

---

## Decision Cheat Sheet

| Need | Fiber |
|------|-------|
| Maximum stiffness + weight saving | Carbon (HM or IM grades) |
| Maximum strength/weight | Carbon (IM7, T800) |
| Lowest cost fiberglass structure | E-glass |
| Higher performance glass | S-glass or S2-glass |
| Ballistic protection / soft armor | Kevlar 29/129 |
| Tension cable / high strength rope | Kevlar 49 |
| Sustainable bio-composite | Flax or hemp (with PP or epoxy) |
| Hybrid ballistic + structural | CF + Kevlar hybrid laminate |
| Wind turbine blade (cost sensitive) | E-glass, possibly CF spar cap |

---

## Common Confusion Points

**Carbon fiber grades (T vs. M series)**: Toray T-series = high tensile strength
optimized; M-series = high modulus optimized. T800 has higher strength but lower
modulus than M35. For most structural applications, strength (T800, IM7) is
more critical than ultra-high modulus. Satellite and precision optical structures
use UHM for near-zero CTE, not maximum strength.

**Kevlar cannot carry compression loads**: A Kevlar/epoxy strut in pure tension
is excellent. Load it in compression and it buckles catastrophically at ~250 MPa
(vs. ~1,200 MPa for CFRP). In hybrid laminates, CF carries compression and
Kevlar adds impact resistance. Never spec Kevlar as the primary compression
element.

**E-glass and moisture**: Untreated E-glass loses 30–50% of GFRP strength after
prolonged water immersion. The silane coupling agent is the critical defense.
Using the wrong silane (polyester-compatible sizing in an epoxy matrix) yields
essentially unbonded glass and very poor wet properties.
