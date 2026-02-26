# Effective Stress: Terzaghi Principle, Pore Pressure, Stress Paths, Seepage

## The Big Picture

Effective stress is the single most important concept in soil mechanics. Everything that matters about a soil — its strength, its compressibility, its tendency to consolidate — is governed by the effective stress acting between soil particles, not by the total stress applied from above. Understanding pore water pressure and its relationship to effective stress is the key to understanding why soils behave as they do.

```
+------------------------------------------------------------------+
|               EFFECTIVE STRESS — MASTER CONCEPT                 |
+------------------------------------------------------------------+
|                                                                  |
|  TOTAL STRESS  σ = weight of everything above (soil + water)    |
|                                                                  |
|  PORE WATER PRESSURE  u = pressure of water in the voids        |
|  (hydrostatic: u = γw × hw   where hw = depth below water table)|
|                                                                  |
|  EFFECTIVE STRESS  σ' = σ - u                                   |
|  = the intergranular contact stress between soil particles       |
|  = what actually squeezes grains together                        |
|  = what governs strength, compressibility, volume change        |
|                                                                  |
|  KEY INSIGHT:                                                    |
|  Pumping water out (lowering water table) → u decreases         |
|  → σ' increases → soil compresses (surface settles!)           |
|                                                                  |
|  Mexico City built on ancient lake bed:                         |
|  Pumping groundwater for city supply →                          |
|  Water table drops 30+ meters →                                 |
|  Effective stress increases dramatically →                      |
|  City sinks 8–10 meters over 20th century.                      |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Terzaghi's Effective Stress Principle (1925)

**σ' = σ - u**

This equation is deceptively simple. Its derivation requires careful assumptions:
- Soil particles are incompressible (compared to the soil skeleton)
- Fluid is incompressible (water)
- Contact areas between grains are a negligible fraction of total area

Under these assumptions, the total applied stress σ is shared between:
1. The pore fluid (hydrostatic pressure u)
2. The soil skeleton through interparticle contacts (effective stress σ')

**The proof of concept**: Take a saturated clay sample under total stress σ. Increase u (by back-pressuring the sample) without changing σ. The sample does NOT consolidate. Only when σ' = σ - u increases does consolidation (volume change) occur.

---

## Computing Stress Profiles

### Total Vertical Stress

Integrate unit weight from surface to depth z:

```
STRESS PROFILE CALCULATION:

  Surface

  ─────────────────────────────  z = 0, σv = 0

  LAYER 1: γ₁ = 18 kN/m³ (unsaturated sand), thickness h₁ = 3m
           σv increases at 18 kN/m³ per meter

  ─────────────────────────────  z = 3m, σv = 54 kPa

  WATER TABLE

  ─────────────────────────────  z = 3m, u = 0

  LAYER 2: γsat = 20 kN/m³ (saturated clay), thickness h₂ = 5m
           σv increases at 20 kN/m³ per meter

  ─────────────────────────────  z = 8m, σv = 54 + 5×20 = 154 kPa
                                          u = 5 × 9.81 = 49 kPa
                                          σ' = 154 - 49 = 105 kPa

  Note: γw = 9.81 kN/m³ ≈ 10 kN/m³ (often used for simplicity)
        γ' = γsat - γw = 20 - 10 = 10 kN/m³ (buoyant unit weight)
        So below water table: σ' increases at γ' = γsat - γw per meter
```

---

## Ko — At-Rest Lateral Earth Pressure Coefficient

Soil at rest (no lateral strain) has a lateral effective stress related to vertical by:

**Ko = σ'h / σ'v**

**Jaky's formula** (for normally consolidated soils):
Ko = 1 - sin φ'

where φ' is the effective friction angle.

Typical values:
- Dense sand (φ' = 40°): Ko = 1 - sin 40° = 0.36
- Loose sand (φ' = 30°): Ko = 1 - sin 30° = 0.50
- NC clay (φ' = 25°): Ko = 1 - sin 25° = 0.58

**OCR effect on Ko** (overconsolidated soils):
Ko(OC) = Ko(NC) × OCR^(sin φ')

Heavily OC soils can have Ko > 1 (horizontal stress > vertical stress). London Clay: Ko ≈ 2–3 in some areas.

---

## Stress Paths

The stress path is a trace on a stress diagram of the successive stress states experienced by a soil element. The most useful plots:

**p-q plot** (total stress):
- p = (σ1 + σ3)/2 (mean stress)
- q = (σ1 - σ3)/2 (deviatoric stress / shear stress)

**p'-q' plot** (effective stress):
- p' = p - u = (σ'1 + σ'3)/2
- q' = q = (σ1 - σ3)/2 (shear stress doesn't change with pore pressure)

```
p'-q' STRESS PATH EXAMPLE — UNDRAINED TRIAXIAL:

  q'
  |          Failure envelope (Kf line: slope = sinφ', intercept = c'cosφ')
  |         /
  |       /         Path B: NC clay (undrained, excess u generated)
  |     /          /  ← moves LEFT because u increases
  |   /           /    (p' decreases as u builds up)
  | /            /
  +──────────────────── p'
       Path A: Dense sand (undrained)
               moves RIGHT initially (dilates, negative u)
               then turns back at failure
```

Stress paths are essential for:
- Predicting whether soil will fail in drained or undrained conditions
- Understanding how construction loading changes pore pressures
- Designing back-pressure consolidated triaxial tests

---

## Pore Pressure Coefficients (Skempton)

When total stresses change rapidly (undrained), pore pressures change predictably:

**Skempton's B coefficient**:
Δu = B × Δσ3

- B ≈ 1.0 for saturated soil
- B → 0 as degree of saturation decreases

**Skempton's A coefficient**:
Δu = B[Δσ3 + A(Δσ1 - Δσ3)]

A varies during shearing:
- Normally consolidated (NC) clay: A ≈ 0.5–1.0 (positive → pore pressure increases in shear)
- Overconsolidated (OC) clay: A can be negative (dilative → pore pressure decreases in shear)
- Loose sand: A > 0 (contractive)
- Dense sand: A < 0 (dilative)

**Practical use**: If you know A and B from lab tests, you can estimate pore pressure changes in the field during construction.

---

## Capillary Rise and Negative Pore Pressure

Above the water table, water fills fine pores due to surface tension (capillary suction). Pore pressure is **negative** (suction). Negative pore pressure increases effective stress → soil stronger than the water table location would suggest.

**Capillary height**: hc ≈ C / (e × D10)
where C ≈ 0.1–0.5 cm² depending on mineralogy, e = void ratio, D10 = particle size (cm).

Typical capillary heights:
- Coarse sand: < 0.1 m
- Fine sand: 0.1–1 m
- Silt: 1–10 m
- Clay: > 10 m (but slow to develop)

**Engineering implication**: Excavations that lower the water table can initially use capillary suction strength — but if rain saturates the exposed face, strength is lost rapidly. Cut slopes in silty soils are susceptible to "cave-ins" during rainstorms precisely because capillary suction is lost.

---

## Seepage and Flow Nets

When water table is higher on one side of a structure (dam, retaining wall, levee), seepage occurs. Seepage generates **seepage forces** that reduce effective stress and can cause failure.

### Darcy's Law

v = k × i

where:
- v = seepage velocity (m/s)
- k = hydraulic conductivity (coefficient of permeability, m/s)
- i = hydraulic gradient = Δh/L (head loss per unit length)

Typical k values:
| Soil Type | k (cm/s) |
|-----------|---------|
| Clean gravel | 1–10 |
| Clean sand | 10⁻² – 10⁻¹ |
| Silty sand | 10⁻³ – 10⁻⁴ |
| Silt | 10⁻⁴ – 10⁻⁵ |
| Clay | < 10⁻⁷ |

### Flow Nets

A flow net is the graphical solution to Laplace's equation (∂²h/∂x² + ∂²h/∂z² = 0) for steady seepage:

```
FLOW NET COMPONENTS:

  Flow lines: paths water takes (tangent to velocity vector)
  Equipotential lines: lines of equal total head
  Flow tubes: channels between adjacent flow lines
  Potential drops: intervals between adjacent equipotentials

  Properties:
  - Flow lines ⊥ equipotential lines (for isotropic soil)
  - Flow elements form approximate squares
  - Seepage quantity: q = k × Nf/Nd × Δh
    where Nf = number of flow tubes
          Nd = number of potential drops
          Δh = total head difference

BENEATH A SHEET PILE (schematic):

  HIGH HEAD                    LOW HEAD
  ──────────────     ┃     ──────────────
                     ┃
  ↘  ↘  ↘  ↘       ┃       ↙  ↙  ↙
    ↘  ↘  ↘         ┃         ↙  ↙
      ↓  ↓  ↓       ┃       ↑  ↑  ↑
        ↓  ↓  ↓  ↙  ┃  ↘  ↑  ↑  ↑
             ↓ ↙    ┃    ↖ ↑  ↑
               ──────────────
               (flow curves under pile)
```

### Critical Hydraulic Gradient and Piping

At the downstream exit of a seepage path, water flows upward. When the upward seepage force equals the submerged weight of the soil:

**Critical gradient**: ic = (Gs - 1) / (1 + e) = γ'/γw ≈ 1.0

When i ≥ ic, effective stress → 0, soil "boils" (quicksand). This is **piping failure**. Dams and levees can fail this way.

**Factor of safety against piping**: F = ic / iexit

Require F ≥ 3–5 for important structures.

**Control of piping**: downstream drainage blanket (gravel toe drain), filter criterion (Terzaghi filter rules: D15filter < 4–5 × D85base; D15filter > 4–5 × D15base).

---

## Uplift Pressure

Water pressure acts upward on buried structures (basement slabs, dam foundations, culverts):

**Net uplift** = (pore pressure at base) − (weight of overlying soil/structure)

Design requirement: weight of structure > uplift force
Or provide drainage to reduce pore pressure

---

## Decision Cheat Sheet

| Problem | Principle | Key Calculation |
|---------|-----------|----------------|
| Vertical effective stress at depth z below water table | σ' = σ - u | σ' = γ' × z (using buoyant unit weight γ' = γsat - γw) |
| Lateral stress at rest | Ko × σ'v | Ko = 1 - sinφ' (NC), apply OCR factor for OC |
| Pore pressure during undrained loading | Skempton B and A | Δu = B[Δσ3 + A(Δσ1 - Δσ3)] |
| Seepage flow quantity | Darcy + flow net | q = k × (Nf/Nd) × Δh |
| Is piping occurring? | Critical gradient | ic = (Gs-1)/(1+e) ≈ 1.0; if iexit > ic: failure |
| Will lowering water table cause settlement? | σ' increases → consolidation | Use consolidation theory (03-CONSOLIDATION) |

---

## Common Confusion Points

**Total stress is not what controls soil behavior**: Total stress (weight of everything above) is easy to calculate. But increasing total stress while simultaneously raising the water table can produce zero net increase in effective stress. The ground stays unchanged. Effective stress is what matters.

**Negative pore pressure is suction, not vacuum**: Below the water table, u > 0. Above the water table in fine soils, u can be negative (capillary suction). This negative pore pressure adds to effective stress. When suction is lost (soil saturates), strength can be dramatically reduced.

**Ko applies only at rest**: The at-rest coefficient Ko applies when there is no lateral strain. If a retaining wall moves (even slightly), active (Ka) or passive (Kp) conditions develop. Ko is a useful starting condition for stress initialization, not a design earth pressure.

**Permeability varies by orders of magnitude**: Hydraulic conductivity spans 10 orders of magnitude across soil types. A factor of 2 error in k from lab to field is common (remolding, macro-structure, fabric). Always use field permeability tests for important seepage calculations.
