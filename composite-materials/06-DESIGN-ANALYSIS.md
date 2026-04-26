# Structural Design and Analysis

## The Big Picture

```
+------------------------------------------------------------------+
|              COMPOSITE STRUCTURAL DESIGN FRAMEWORK               |
|                                                                  |
|   DESIGN DRIVERS          ANALYSIS TOOLS        FAILURE MODES    |
|   ─────────────           ──────────────        ────────────     |
|   Stiffness/strength       CLT                  Fiber failure    |
|   Weight                   Tsai-Wu, Max stress  Matrix cracking  |
|   Damage tolerance         FEA (progressive)    Delamination     |
|   Certification            Buckle analysis      Buckling         |
|   Manufacturability        Fatigue (S-N, DFB)   Bearing/pull-out |
|                                                                  |
|   BUILDING BLOCK APPROACH (aerospace):                           |
|   Coupon → Element → Detail → Component → Full-scale test        |
+------------------------------------------------------------------+
```

---

## Failure Modes in Composites

Composites fail differently from metals — multiple interacting mechanisms.

### In-Plane Failure Modes

```
   FIBER TENSION FAILURE:
   ─────────────────────────
   Individual fiber fracture, propagates across bundle
   Failure strain: 1.2–2.0% (CF), 4–5% (GF)
   Net section failure (like metal fracture but brittle)
   Strain concentration: notches, holes → stress concentration factor Kt
   Open hole tension (OHT): σ_net ≈ σ_UTS/Kt_notch
   Typical OHT allowable ≈ 60–70% of unnotched tensile

   FIBER COMPRESSION FAILURE (microbuckling):
   ──────────────────────────────────────────
   Fiber kinking at ~20–25° to fiber direction
   Matrix shear modulus (G12) critical: σ_1C ≈ G12 / (1 + φ0/γ12)
   Most moisture/temperature sensitive mode → drive design allowables
   Open hole compression (OHC): typically lowest strength allowable

   MATRIX CRACKING:
   ─────────────────
   Transverse tension (σ2) or shear (τ12) → matrix micro-cracks
   Onset at ~40–70% of ultimate (first ply failure)
   Crack density increases with load → stiffness degradation, moisture ingress
   Not immediate structural failure but precursor to delamination

   DELAMINATION:
   ──────────────
   Crack growing between plies
   Driven by interlaminar normal stress (σ3) or shear (τ13, τ23)
   Mode I (opening) or Mode II (sliding) — or mixed
   Critical at ply drop-offs, free edges, holes, impact damage
   Arrest by: interlaminar toughening (rubber particles, thermoplastic interleaves)
```

---

## Design Allowables

Composites certification uses a statistical allowable system:

```
   FAA AC 25.613 — MATERIAL STRENGTH PROPERTIES:
   ──────────────────────────────────────────────
   B-basis allowable: 90% probability of exceeding at 95% confidence
   A-basis allowable: 99% probability of exceeding at 95% confidence
   S-basis: specification minimum (no statistical basis)

   TYPICAL DEVELOPMENT:
   ─────────────────────
   Test 30+ specimens per condition per property
   Statistical fit (Weibull or normal distribution)
   Compute B-basis: lower 90% confidence bound on 10th percentile
   Common: CF/epoxy B-basis tension ≈ 85–90% of mean
           CF/epoxy B-basis compression ≈ 80–85% of mean (more scatter)

   ENVIRONMENTAL KNOCKDOWNS:
   ──────────────────────────
   ETW (elevated temperature, wet): lowest allowable
   RTD (room temperature, dry): highest allowable
   Apply most severe environment for each structural location

   EXAMPLE KNOCKDOWN FACTORS FOR CF/EPOXY:
   ──────────────────────────────────────────
   Property          RTD    ETW (180°C wet)
   Fiber tension     1.0    0.90
   Fiber compression 1.0    0.75
   Matrix tension    1.0    0.65
   ILSS              1.0    0.50
```

---

## Stability: Buckling of Thin Composite Plates

Thin composite skins are buckling-critical. Buckling not always failure if
postbuckling reserve exists.

```
   ORTHOTROPIC PLATE BUCKLING (simply supported):
   ──────────────────────────────────────────────────
   Nx_cr = (π²/b²) · [D11·(b/a)²·m⁴ + 2(D12+2D66)·m²·n² + D22·(a/b)²·n⁴] / m²
   m,n = number of half-waves in x, y

   For a square plate (a = b), minimum:
   Nx_cr = (π²/b²) · [4·D11 + 4(D12+2D66) + D22] / 4

   Simplified for quasi-isotropic laminate:
   Nx_cr ≈ 3.6 · D11 / b²    (for a ≈ b, worst case)

   KEY DESIGN IMPLICATION:
   ─────────────────────────
   D11 = (1/3) · Q̄11_outer_ply · (h³ - (h-2t)³) / 4  (outer ply dominates!)
   → Outer 0° plies drive bending stiffness → critical for buckling resistance
   → Wing skin: 0° plies on outside, ±45° in middle
```

### Postbuckling Reserve

For plates under shear or compression, postcritical reserve can be 2–4× critical
load before full structural failure. Use only with rigorous testing and certification.

---

## Joints in Composite Structures

Joints are typically the weakest point — composites are strong at the ply level
but joints introduce stress concentrations.

### Mechanical Fastening

```
   BEARING / PULL-THROUGH FAILURE:
   ─────────────────────────────────
   Bolt bearing stress: σ_b = F / (d · t)
   CF/epoxy allowable bearing stress: ~500–700 MPa (B-basis)
   Vs. aluminum: ~600–900 MPa
   → CFRP comparable to aluminum for bearing

   HOLE DESIGN RULES (empirical):
   ────────────────────────────────
   Edge distance (e): e/d ≥ 3 (to prevent shear-out)
   Pitch: p/d ≥ 4 (row of fasteners)
   Fastener fit: interference fit → improves fatigue (like metal)
   Bolt material: titanium or stainless preferred
     → Galvanic corrosion: Al and CF = galvanic couple → NO Al fasteners in CFRP!

   LAMINATES FOR BEARING (empirical optimum):
   ────────────────────────────────────────────
   0° content: 25–50%
   ±45° content: ≥ 40%
   Avoid 100% 0° or 90° at hole (very low bearing)
   [0/±45/90]s is a good starting point
```

### Adhesive Bonding

```
   JOINT GEOMETRIES:
   ──────────────────
   SINGLE LAP: simple, asymmetric, peel moment → worst for composites
   DOUBLE LAP: symmetric, better, but peel stress at end
   SCARF JOINT: tapered — most efficient (uniform shear), complex to make
   STEPPED SCARF: approximation of scarf, practical for thick section

   STRESS DISTRIBUTION IN SINGLE LAP:
   ─────────────────────────────────────
   Shear stress peak at overlap ends (not uniform!)
   Peak/average = depends on overlap length, adherend stiffness
   → Short overlap: high peak/average → peel → failure
   → Long overlap: peak unchanged but average low → better efficiency

   PEEL STRESS (σ3 at end of bond):
   ──────────────────────────────────
   Composites cannot tolerate through-thickness tension well
   ILSS ~ 80 MPa, GIc ~ 300 J/m²
   Design rule: peel stress < 20 MPa in composite bondline

   DESIGN PRINCIPLE FOR COMPOSITES:
   ──────────────────────────────────
   Preferred: scarf or stepped scarf
   Minimize peel stress (chamfer ends, use rubber toughened adhesive)
   Hybrid: bond + fasteners (belt + suspenders for primary structure)
```

---

## Fatigue of Composites

Composites fail under cyclic loading differently from metals.

```
   METAL FATIGUE:                    COMPOSITE FATIGUE:
   ──────────────                    ──────────────────
   Single crack initiates            Distributed damage
   Crack grows → fracture            Matrix cracking → delamination
   S-N curve: steep slope            S-N curve: shallower slope
   Fatigue limit (some alloys)       No fatigue limit in most composites
   R-ratio critical                  R-ratio critical (compression worse)

   COMPOSITE FATIGUE DAMAGE:
   ──────────────────────────
   Stage 1: Matrix microcracking (onset at ~20–40% UTS)
   Stage 2: Crack coupling, fiber-matrix debonding
   Stage 3: Delamination, fiber fracture → sudden failure

   S-N CURVES FOR CF/EPOXY (typical):
   ────────────────────────────────────
   Tension-tension (R=0.1): σ at 10⁷ cycles ≈ 40–50% static UTS
   Tension-compression (R=-1): ≈ 30–40% static UTS (worst case)
   Compression-compression (R=10): ≈ 25–35% static UTS

   DESIGN APPROACH (FAA):
   ───────────────────────
   Static allowables already conservative (A or B-basis)
   Fatigue testing (typically: DFB = damage-free design, or damage tolerance)
   Spectrum loading (variable amplitude) — rainflow counting
   Primary: no detectable damage should accumulate to failure
```

---

## Impact and Damage Tolerance

The critical weak point of laminated CFRP.

```
   IMPACT DAMAGE MECHANISMS:
   ───────────────────────────
   Low velocity impact (tools, runway debris, hail):
   → Matrix cracking, delamination
   → Barely Visible Impact Damage (BVID): ≤ 0.3 mm dent depth
   → Visible Impact Damage (VID): > 0.3 mm, > 6.35 mm (FAA definition)

   HIGH VELOCITY (bird strike, debris):
   → Fiber fracture + delamination
   → Penetration in severe cases

   COMPRESSION AFTER IMPACT (CAI):
   ──────────────────────────────────
   Key certification test (FAA, EASA)
   Impact panel, then load in compression to failure
   CAI strength ≈ 30–50% of undamaged compression strength
   Driven by: delamination buckling under compression

   WHY CFRP IS BRITTLE TO IMPACT:
   ────────────────────────────────
   Brittle fibers → energy not absorbed by plastic deformation
   Matrix: also brittle → cracks and delaminations absorb energy inefficiently
   GFRP and AFRP: much better impact tolerance (glass/Kevlar more ductile)
   Toughened epoxy (interleaved): improves CAI by 30–50% vs. brittle epoxy
```

---

## Building Block Approach (Aerospace)

FAA/EASA certification requires systematic experimental evidence at multiple scales.

```
   PYRAMID:
   ─────────
              [FULL SCALE]
            [COMPONENTS: wing box, fuselage barrel]
          [DETAILS: joints, cutouts, frames]
        [ELEMENTS: stiffened panels, shear webs]
      [COUPONS: flat plates, OHT, OHC, CAI, fatigue]

   Each level: ~10–100× more specimens than level above
   Coupon: 1,000–10,000 specimens (statistical basis)
   Full scale: 1 (very expensive)

   EACH LEVEL verifies:
   ─────────────────────
   Coupon: material properties, allowables, environmental effects
   Element: stiffened panel buckling, joint efficiency
   Detail: local geometry effects, cutout behavior
   Component: load redistribution, combined loading
   Full scale: structural proof, fail-safe demonstration

   COST DISTRIBUTION:
   ───────────────────
   Coupon testing: ~15% of total certification test cost
   Full-scale: ~50% (one test rig can cost > $100M for aircraft)
```

---

## Decision Cheat Sheet

| Design situation | Approach |
|-----------------|---------|
| Strength-critical UD laminates | Max stress criterion per ply, ROM |
| Off-axis or multi-load | Tsai-Wu failure criterion |
| Thin panel stability | Orthotropic plate buckling formula or FEA |
| Adhesive joint design | Scarf joint preferred; single-lap only with peel mitigation |
| Mechanical fastening | e/d ≥ 3, p/d ≥ 4, no aluminum fasteners in CFRP |
| Impact damage tolerance | CAI test, BVID as design damage state |
| Fatigue design | S-N spectrum at R=-1 is limiting; use damage tolerance approach |
| Design allowable level | B-basis minimum; A-basis for single-load-path critical |

---

## Common Confusion Points

**Composite allowables are not material properties**: A "CF/epoxy allowable"
is a combination of material, environment (ETW or RTD), and layup. A [0/±45/90]s
OHT allowable is different from a UD tensile allowable. The building block approach
generates allowables for each geometry + environment of interest.

**First ply failure ≠ structural failure**: Matrix cracking in off-axis plies
begins at 40–60% of ultimate. Structures are often designed beyond FPF using
a progressive failure model. However, for pressurized fuselage, permeation
starts at matrix cracking → must design below FPF for some applications.

**Composites are NOT always fatigue-superior to aluminum**: Under tension-
dominated loading (R > 0), CFRP outperforms aluminum dramatically. Under
compression or reversed loading, CFRP advantage shrinks. For spectrum loading
with significant compression, the comparison is not always clear — depends
on the specific spectrum, notch effects, and damage tolerance requirements.
