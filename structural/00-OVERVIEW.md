# Structural Engineering — Landscape & Field Taxonomy

## The Big Picture

Structural engineering asks one question: **will this hold?** Given applied loads, a structure must
neither collapse nor deform excessively. The discipline spans from fundamental mechanics (force,
stress, strain) to design codes (ACI 318, AISC, Eurocodes) to geotechnical behavior of the ground
a structure sits on.

```
APPLIED LOADS
  Gravity (dead + live)     Wind     Seismic     Thermal     Fatigue
        │                     │          │             │          │
        └─────────────────────┴──────────┴─────────────┴──────────┘
                                      │
                              STRUCTURAL SYSTEM
        ┌─────────────────────────────────────────────────────────────┐
        │  STATICS                                                     │
        │  Equilibrium — reactions, internal forces (V, M, N, T)       │
        ├─────────────────────────────────────────────────────────────┤
        │  MECHANICS OF MATERIALS                                      │
        │  Stress/strain, bending, shear, torsion, deflection         │
        ├─────────────────────────────────────────────────────────────┤
        │  STRUCTURAL ANALYSIS                                         │
        │  Matrix methods, FEM, influence lines, dynamics             │
        ├─────────────────────────────────────────────────────────────┤
        │  STRUCTURAL DESIGN                                           │
        │  RC (ACI 318), Steel (AISC), Timber (NDS), Masonry         │
        ├─────────────────────────────────────────────────────────────┤
        │  GEOTECHNICAL                                                │
        │  Soil mechanics, foundations, earth pressure, slope stability│
        └─────────────────────────────────────────────────────────────┘
                                      │
                              SERVICEABILITY + SAFETY
```

---

## Module Map

| Module | Core Topic | Key Equations | Real Application |
|--------|-----------|---------------|-----------------|
| `01-STATICS` | Equilibrium, trusses, frames | ΣF=0, ΣM=0 | Finding reactions, member forces |
| `02-MECHANICS-OF-MATERIALS` | Stress, bending, torsion | σ=My/I, τ=Tr/J | Sizing beams, shafts |
| `03-STRUCTURAL-ANALYSIS` | Matrix methods, FEM, dynamics | [K]{d}={F} | Computer analysis |
| `04-GEOTECHNICAL` | Soil, foundations, slopes | τ=c+σ'tanφ | Foundation design |

---

## Fundamental Quantities

```
FORCE AND MOMENT EQUILIBRIUM (the foundation of everything)
  ΣFx = 0,  ΣFy = 0,  ΣFz = 0    (force balance)
  ΣMx = 0,  ΣMy = 0,  ΣMz = 0    (moment balance)

2D: 3 equations → can solve 3 unknowns (statically determinate)
    More unknowns → statically indeterminate (need compatibility equations)

INTERNAL FORCES on a cross section:
  N = normal force (axial, along member)
  V = shear force (perpendicular to member axis)
  M = bending moment
  T = torsional moment (torque)

STRESS (force per area):
  σ = N/A (axial)       σ = My/I (bending)
  τ = VQ/(Ib) (shear)   τ = Tr/J (torsion)

STRAIN (deformation per length):
  ε = σ/E (normal)      γ = τ/G (shear)
```

---

## Structural Materials

| Material | E [GPa] | S_y or f'c [MPa] | ρ [kg/m³] | Characteristics |
|----------|---------|-----------------|---------|----------------|
| Structural steel (A992) | 200 | F_y = 345 | 7850 | Ductile, tension + compression, weldable |
| Reinforcing steel (Grade 60) | 200 | F_y = 414 | 7850 | Rebar only (used in tension in RC) |
| Normal weight concrete | 25–35 | f'c = 28 (compression only) | 2400 | Brittle, weak in tension |
| Aluminum 6061-T6 | 69 | S_y = 276 | 2700 | Light, no endurance limit |
| Timber (Douglas fir) | 12 | F_b = 14–20 (bending) | 500 | Orthotropic, moisture-sensitive |
| Glass fiber composite (GFRP) | 20–45 | 300–700 (tension) | 1800 | Light, corrosion-resistant, brittle |

---

## Load Types and Load Combinations

**Dead load (D):** Permanent: structure self-weight, finishes, permanent equipment.
**Live load (L):** Occupancy: people, furniture, movable equipment. Varies by occupancy.
**Wind load (W):** From building code (ASCE 7), depends on exposure category and building height.
**Seismic load (E):** Earthquake, depends on seismic zone and building category.
**Snow load (S):** Depends on geography and roof slope.

**LRFD (Load and Resistance Factor Design) — US codes (ACI, AISC):**
```
Factored load: U = max of:
  1.4D
  1.2D + 1.6L + 0.5(S or R)
  1.2D + 1.6(S or R) + (L or 0.5W)
  1.2D + 1.0W + L + 0.5S
  0.9D + 1.0W
  0.9D + 1.0E  (seismic)

Required: φR_n ≥ U   (resistance factor φ × nominal strength ≥ factored load)
```

**ASD (Allowable Stress Design) — older codes and many geotechnical:**
```
Allowable stress = S_y / Factor of safety (typically n = 1.5–3)
```

---

## Connection to Computing/Software

| Structural Concept | Software Analog |
|-------------------|----------------|
| Direct stiffness method [K]{d}={F} | Sparse linear system solve (same math as FEA in every domain) |
| Influence lines | Sensitivity analysis (∂output/∂input) |
| Modal analysis (natural frequencies) | Eigenvalue decomposition of stiffness matrix |
| Nonlinear geometric analysis | Newton-Raphson iteration (same algorithm) |
| Monte Carlo structural reliability | Probabilistic risk analysis |
| BIM (Building Information Modeling) | Structured data model + 3D geometry (like a CAD version of Azure Digital Twins) |

---

## Decision Guide

```
WHAT STRUCTURAL PROBLEM ARE YOU SOLVING?
        │
        ├─ What are the reactions and internal forces?
        │   └─► 01-STATICS (hand methods) or 03-STRUCTURAL-ANALYSIS (matrix/FEM)
        │
        ├─ Will the cross-section fail or deform too much?
        │   └─► 02-MECHANICS-OF-MATERIALS (σ, τ, deflection)
        │
        ├─ Is this an indeterminate structure or dynamic problem?
        │   └─► 03-STRUCTURAL-ANALYSIS (matrix stiffness, modal analysis)
        │
        └─ Is the ground involved (foundation, retaining wall, slope)?
            └─► 04-GEOTECHNICAL
```
