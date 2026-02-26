# Composite Fundamentals: Matrix, Fiber, Interface

## The Big Picture

```
+------------------------------------------------------------------+
|              COMPOSITE STRUCTURE — THREE LEVELS                  |
|                                                                  |
|   CONSTITUENT LEVEL         PLY LEVEL           LAMINATE LEVEL  |
|   ──────────────────        ─────────           ──────────────  |
|   Fiber properties          Fiber orientation   Stacking sequence|
|   Matrix properties         Vf (vol fraction)   Thickness        |
|   Interface/interphase      UD or woven         Symmetry         |
|                             thickness           Balance           |
|                                                                  |
|   ↓ Rule of Mixtures        ↓ Classical Laminate Theory (CLT)   |
|   Ply properties            Laminate properties                  |
|   E1, E2, G12, ν12         [A][B][D] matrices                   |
+------------------------------------------------------------------+
```

Composite mechanics is a multi-scale problem. Properties at each scale derive
from the scale below via micromechanical and structural mechanics models.

---

## Rule of Mixtures (ROM) — Micromechanics Foundation

The most important micromechanical model. Predicts ply properties from fiber
and matrix properties + volume fraction.

### Longitudinal Modulus (Voigt Bound — exact in tension)

```
   E1 = Ef · Vf + Em · (1 - Vf)

   Physical interpretation:
   Fibers and matrix share strain in parallel (isostrain condition)
   ε_fiber = ε_matrix = ε_composite
   Each phase carries load proportional to E × Vf
```

For CF/epoxy: E1 = 230 × 0.60 + 3.5 × 0.40 = 138 + 1.4 = 139.4 GPa
Fiber dominates completely.

### Transverse Modulus (Reuss Bound — lower bound approximation)

```
   1/E2 = Vf/Ef + (1-Vf)/Em   (Reuss, isostress — exact lower bound)

   More accurate Halpin-Tsai (empirical correction):
   E2 = Em · (1 + ξ·η·Vf) / (1 - η·Vf)
   η = (Ef/Em - 1) / (Ef/Em + ξ)
   ξ = 2 for circular fibers in transverse direction

   For CF/epoxy: E2 ≈ 9–11 GPa (vs. Em = 3.5 GPa)
   → 3× matrix modulus, but not fiber-dominated
```

### Shear Modulus

```
   G12 ≈ Gm / (1 - √Vf·(1 - Gm/Gf))   (approximation)

   Typical CF/epoxy: G12 ≈ 5–7 GPa
   Note: Gf_carbon ≈ 70 GPa (carbon fiber), Gm ≈ 1.3 GPa (epoxy)
```

### Strength: Simpler Models Only

For strength, simple ROM is less reliable (local stress concentrations matter):

```
   Longitudinal tensile strength (simple ROM):
   σ1_ult ≈ Vf · σf_ult + (1-Vf) · σm*
   σm* = matrix stress at fiber failure strain

   For CF/epoxy: εf_ult ≈ 1.5%, σm* = Em × εf_ult = 3.5 × 0.015 = 52 MPa
   σ1_ult ≈ 0.60 × 5,000 + 0.40 × 52 = 3,000 + 21 = 3,021 MPa (upper est.)

   Actual: ~1,500–2,000 MPa — fiber bundle effects, stress concentrations
```

---

## Fiber, Matrix, and Interface — Three-Phase Model

### The Interface: Often the Limiting Factor

```
   FIBER            INTERPHASE           MATRIX
   ─────            ──────────           ──────
   Carbon fiber     Sizing layer on      Epoxy (or other)
   surface          fiber surface        bulk polymer
   typically
   chemically       Chemical/physical
   treated          bonding
   (oxidized,       Sizing: 0.2–0.5 µm
    anodized,       polymeric film
    sized)          Graded properties
                    fiber→matrix
```

**The interphase** is not simply the geometric surface. It's a zone of modified
matrix chemistry near the fiber, typically 0.1–1 µm thick, with properties
intermediate between fiber and bulk matrix.

### Fiber Surface Treatment for Adhesion

Carbon fiber is chemically inert as produced. Surface treatment dramatically
changes ILSS (interlaminar shear strength):

```
   UNTREATED CF:     ILSS ~ 20–40 MPa (matrix cracks easily at interface)
   OXIDIZED CF:      ILSS ~ 60–80 MPa (oxygen groups → H-bond sites)
   EPOXY-SIZED CF:   ILSS ~ 80–100 MPa (chemical compatibility)

   SURFACE TREATMENT METHODS:
   ────────────────────────────
   Electrochemical oxidation (anodization): most common for carbon
      HNO3, H2SO4, or ammonium bicarbonate electrolyte
      Creates –COOH, –OH, –C=O groups on surface
      Increases surface energy from ~45 to ~70 mJ/m²

   Sizing (sizing agent):
      Thin polymer film applied over oxidized fiber
      Epoxy-compatible size for epoxy matrix
      PEEK-compatible size for thermoplastic matrix
      Functions: fiber handling protection + matrix compatibility
```

### Fiber Volume Fraction and Its Measurement

```
   Vf = volume of fiber / total volume of composite

   MEASUREMENT METHODS:
   ─────────────────────
   Acid digestion (ASTM D3171 Method A):
   Dissolve matrix in acid (H2SO4, HNO3)
   Weigh remaining fiber
   Calculate from density measurements
   Accurate for carbon/epoxy, not for reactive fibers

   Burnout (ASTM D3171 Method B):
   Burn off polymer matrix in furnace
   Weigh remaining fiber (works for GF — CF may oxidize slightly)

   Optical microscopy:
   Polish cross section → point count or image analysis
   Most accurate for Vf and void content simultaneously

   TYPICAL Vf BY PROCESS:
   ────────────────────────
   Hand lay-up: 25–45%
   Resin infusion: 45–55%
   RTM: 50–60%
   Prepreg autoclave: 55–65%
   Filament winding: 55–70%
```

---

## Void Content and Its Effects

Voids = pockets of entrapped air or volatiles. Critical quality metric.

```
   HOW VOIDS FORM:
   ────────────────
   Insufficient vacuum in bag molding → dissolved gas not removed
   Trapped air at ply overlaps or changes in geometry
   Volatiles from resin cure (solvent, water from moisture)
   Incomplete resin flow at high Vf during infusion

   EFFECTS ON PROPERTIES:
   ──────────────────────
   Each 1% void content:
   → ILSS (interlaminar shear strength): -3 to -5%
   → Tensile strength: -0.5 to -1%
   → Compressive strength: -1 to -3%
   → Fatigue life: can be catastrophic (void = crack initiation site)

   VOID CONTENT LIMITS:
   ────────────────────
   Aerospace primary structure: < 0.5%
   Aerospace secondary: < 1%
   Automotive: < 2–3%
   Marine/civil: < 5% (typical hand lay-up)

   MEASUREMENT:
   ─────────────
   Optical microscopy (direct)
   Ultrasonic C-scan (signal attenuation — indirect, non-destructive)
   X-ray microtomography (3D, expensive)
   Density comparison: actual vs. theoretical
```

---

## Key Ply Properties for Carbon/Epoxy

### Engineering Constants of a UD Ply

```
   TYPICAL IM7/977-3 CF/EPOXY UD PLY PROPERTIES:
   ──────────────────────────────────────────────
   Vf ~ 60%

   E1   = 165 GPa    (fiber direction tensile modulus)
   E2   = 9.5 GPa    (transverse modulus)
   G12  = 5.7 GPa    (in-plane shear modulus)
   ν12  = 0.34       (major Poisson's ratio)

   X1T  = 2,500 MPa  (fiber direction tensile strength)
   X1C  = 1,200 MPa  (fiber direction compressive strength)
   X2T  = 65 MPa     (transverse tensile strength — matrix-dominated)
   X2C  = 200 MPa    (transverse compressive strength)
   S12  = 80 MPa     (in-plane shear strength)

   ρ    = 1.55 g/cm³
   α1   = 0.1 × 10⁻⁶/°C    (CTE — near zero!)
   α2   = 28 × 10⁻⁶/°C     (CTE transverse — large)
```

Note the extreme anisotropy:
- E1/E2 = 165/9.5 = 17.4 (modulus ratio)
- X1T/X2T = 2500/65 = 38 (strength ratio)
- Tensile/compressive: 2500/1200 = 2.1 (asymmetric)

### The Compression Problem

CFRP compressive strength (~1,200 MPa) is only ~48% of tensile. Why?

```
   FIBER MICROBUCKLING (kinking):
   ────────────────────────────────
   Individual fibers, if slightly misaligned, buckle under compression
   Matrix must resist lateral buckling: G12 of matrix critical
   Failure mode: "kink band" at ~20–25° to fiber direction

   Kink band initiation: local fiber misalignment (±0.5–2° typical)
   Critical:  σ1C_kink ≈ G12 / (1 + φ0/γ12)
   φ0 = initial fiber misalignment angle

   CONSEQUENCE: moisture absorption reduces Em and G12
   → Compressive strength is moisture/temperature sensitive
   Design: use lower design allowables at elevated temperature/wet (ETW)
```

---

## Interlaminar Properties

The critical weakness of laminated composites:

```
   INTERLAMINAR SHEAR STRENGTH (ILSS / ISS):
   ────────────────────────────────────────────
   Three-point short beam shear test (ASTM D2344)
   Typical CF/epoxy: 80–100 MPa
   Controlled by matrix and fiber-matrix interface

   MODE I FRACTURE TOUGHNESS (GIc — opening mode):
   ────────────────────────────────────────────────────
   Double cantilever beam (DCB) test (ASTM D5528)
   Typical CF/epoxy: 200–600 J/m²
   Toughened epoxy: 400–1,000 J/m² (rubber particles, thermoplastic interleaves)

   MODE II FRACTURE TOUGHNESS (GIIc — shear mode):
   ─────────────────────────────────────────────────
   End-Notched Flexure (ENF) or 4ENF test
   Typical CF/epoxy: 600–2,000 J/m²

   MODE MIXITY in real structures: delaminations involve both Mode I and II
   Mixed mode failure criterion: (GI/GIc)^m + (GII/GIIc)^n = 1
```

---

## Decision Cheat Sheet

| Design question | Key parameter | How to get it |
|-----------------|--------------|---------------|
| Stiffness in fiber direction | E1 (Rule of Mixtures accurate) | Test / datasheet |
| Stiffness off-axis | CLT with E1, E2, G12, ν12 | CLT calculation |
| Failure prediction (fiber) | X1T, X1C | Tension/compression test |
| Failure prediction (matrix/off-axis) | X2T, X2C, S12 + criterion | Test + Tsai-Wu, etc. |
| Delamination resistance | GIc, GIIc | DCB, ENF tests |
| Effect of moisture | ETW knockdown | Conditioning + test |
| Fiber volume fraction (quality) | Vf | Acid digest or burnout |
| Process quality (void content) | Vv | Optical microscopy or UT |

---

## Common Confusion Points

**ROM underestimates transverse stiffness, Halpin-Tsai is better**: The simple
Reuss bound for E2 gives a lower bound, typically 20–30% below the actual.
Halpin-Tsai equations with ξ = 2 (transverse) and ξ = 1 (shear) are practical
engineering approximations. For high accuracy: FEA of representative volume
element (RVE) with hexagonal fiber packing.

**Compressive failure ≠ tensile failure reversed**: The mechanisms are entirely
different. Tensile failure = fiber fracture. Compression failure = fiber
microbuckling / kinking — governed by fiber misalignment, matrix shear modulus,
and void content. This is why neat resin G12 is the most important matrix
property for compressive CFRP design.

**Interface ≠ interphase**: The interface is the geometric surface between fiber
and matrix. The interphase is the 3D zone of modified chemistry/properties
surrounding the fiber. Surface treatments and sizing create and modify the
interphase — which is why the same fiber with different sizings in the same
matrix can show very different ILSS.
