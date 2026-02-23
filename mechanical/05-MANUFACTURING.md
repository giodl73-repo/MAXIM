# 05 — Manufacturing Processes

## Machining, Forming, Casting, Joining, Additive Manufacturing

```
MANUFACTURING PROCESS TAXONOMY

                  MANUFACTURING
                       │
        ┌──────────────┼──────────────┐
        │              │              │
   SUBTRACTIVE    FORMING         ADDITIVE
   (material      (shape by       (build layer
    removed)       deformation)    by layer)
        │              │              │
   Machining     Forging/Rolling  FDM/SLA/SLS
   Grinding       Sheet metal      DMLS/EBM
   EDM/Laser      Extrusion        DED/binder
   Waterjet       Drawing          jet/ink jet
                       │
              NET SHAPE / NEAR-NET-SHAPE
                       │
              Casting (liquid metal → mold)
              Powder metallurgy
              Injection molding (polymers)
```

---

## Machining Fundamentals

### Chip Formation

Three chip types:
- **Continuous:** Ductile materials, sharp tool, moderate speed — good surface finish
- **Built-up edge (BUE):** Work material welds to tool tip at medium speeds — poor finish, tool wear
- **Discontinuous:** Brittle materials or low rake angle — chunks, acceptable for cast iron

**Merchant model (orthogonal cutting):**
```
Shear plane angle φ: tan(φ) = r cos(α) / (1 − r sin(α))
  r = chip thickness ratio, α = rake angle

Cutting force: Fc = τ_s A_chip / (sin(φ) cos(φ+β−α))
  τ_s = shear strength, β = friction angle = arctan(μ)
```

**Taylor's tool life equation:**
```
v T^n = C

v = cutting speed [m/min], T = tool life [min]
n = exponent (0.1–0.5, depends on tool/work material)
C = constant (speed for T=1 min)

→ Double cutting speed → dramatically shorter tool life
n = 0.3 (carbide), C = 200 → halving speed gives 2^(1/0.3) ≈ 10× life
```

### Cutting Tool Materials

| Material | Hardness | Speed range | Notes |
|----------|----------|-------------|-------|
| High-speed steel (HSS) | ~65 HRC | Up to 30 m/min | Flexible, re-grindable, cheap |
| Cemented carbide (WC-Co) | ~90 HRA | 100–500 m/min | Most common insert material |
| Coated carbide (TiN, TiAlN, Al₂O₃) | — | 200–600 m/min | Coatings extend life 3–5× |
| Ceramics (Al₂O₃, Si₃N₄) | ~95 HRA | 500–1000 m/min | No coolant, brittle |
| CBN (cubic boron nitride) | ~4500 HV | 100–300 m/min | Hardened steel, cast iron |
| PCD (polycrystalline diamond) | ~8000 HV | 1000+ m/min | Non-ferrous only (reacts with Fe) |

### Machining Operations

**Turning (lathe):**
```
Cutting speed: v = πdN/1000  [m/min], d = mm, N = rpm
MRR = π d f v / 1000  (material removal rate, cm³/min)
  f = feed rate [mm/rev], d_oc = depth of cut [mm]
Surface roughness: Ra ≈ f²/(8r_ε)   r_ε = nose radius
```

**Milling:**
- Peripheral (slab) milling vs face milling
- Climb (down) milling: chip starts thick → thin (preferred for CNC, better finish)
- Conventional (up) milling: chip starts thin → thick (better for old manual machines with backlash)

**Drilling:**
- Feed rate in mm/rev × 2 (both lips cut)
- Chisel edge doesn't cut — it pushes → requires high thrust force (~60% of total)
- Pilot hole for large drills; reamer for precision bores (h7 class, IT6–7 tolerance)

### Surface Roughness

```
Ra = arithmetic average roughness [μm]
Rz = average peak-to-valley [μm] ≈ 4Ra (rough estimate)

Achievable Ra by process:
  Grinding:     0.1–0.8 μm
  Fine turning: 0.4–1.6 μm
  Rough turning: 1.6–12.5 μm
  Milling:      0.8–3.2 μm
  EDM:          0.4–1.6 μm
  Casting:      3–25 μm
```

---

## Non-Traditional Machining

| Process | Material removal mechanism | Best for |
|---------|--------------------------|---------|
| EDM (Electric Discharge) | Spark erosion in dielectric | Hardened dies, complex cavities |
| Wire EDM | Spark + moving wire electrode | Precise cutout shapes |
| ECM (Electrochemical) | Anodic dissolution in electrolyte | Burr-free turbine blades |
| Laser cutting | Thermal vaporization | Sheet metal, plastics, precision parts |
| Waterjet | Erosion (abrasive particles) | Heat-sensitive, thick composites |
| Ultrasonic | Abrasive slurry + vibration | Brittle materials (glass, ceramics) |

---

## Metal Forming

### Plasticity Basics

```
Flow stress (yield in compression): σ_0 = C ε_true^n
  C = strength coefficient, n = strain hardening exponent

True strain: ε = ln(A₀/Af) = ln(h₀/hf)
Engineering strain: e = (l − l₀)/l₀

For incompressible plastic flow: A₀ l₀ = Af lf → volume constant
```

### Forging

- **Open-die (free) forging:** Between flat dies; billet spread laterally; bulk shapes
- **Closed-die (impression) forging:** Flash formed, trimmed; net-shape capability; dies costly
- **Flashless precision forging:** No flash; near-net-shape; complex dies

```
Forging pressure (average):
  p̄ ≈ σ_f (1 + 2μR/(3h))    (friction factor μ, disk radius R, height h)

Hot forging: T > 0.6 T_melt → lower forces, no strain hardening
Cold forging: T < 0.3 T_melt → work-hardening, good surface finish, close tolerance
```

**Forgability (ease of forging):** Aluminum alloys > Copper alloys > Low-carbon steel > Stainless > Ti alloys > Ni superalloys > Ceramics (can't forge)

### Rolling

```
Draft: d = h₀ − h₁  (reduction in thickness)
Roll force: F = L w σ_avg    L = contact length = √(R × draft)
Forward slip (workpiece exits faster than roll surface speed): important for strip tension

Hot rolling: slabs → plates/strips (rough shape, scale on surface)
Cold rolling: improves surface finish, tighter tolerances, work-hardening
```

### Sheet Metal Operations

**Bending:**
```
Springback angle: Δθ ∝ σ_y/E  (elastic recovery after forming)
K-factor: material neutral axis offset during bending
  Bend allowance L_b = α(r + K × t)  where α = bend angle in radians

Minimum bend radius: r_min/t = function of material elongation capability
```

**Deep drawing (cups, cans):**
```
Limiting Drawing Ratio (LDR): max ratio D₀/D_p achievable
  LDR ≈ 2.0–2.3 for steel, 2.1–2.5 for aluminum (depends on anisotropy)

Drawing force: F = π D_p t σ_UTS (D₀/D_p − 0.7)
Wrinkling: flange buckles when blank too thin vs radial compression
Tearing: cup wall stress too high → reduce friction, add blank holder
```

**Stamping/Punching:**
```
Punch force: F = L t τ_max   L = perimeter, t = thickness, τ_max ≈ 0.7 S_ut
Clearance per side: 5–10% of thickness (for clean shear; too small → fracture, too large → burr)
```

---

## Casting

### Process Overview

```
Sand casting: Expendable sand mold, pattern → cavity → pour → shake out
  Draft angle: 1–3° for easy pattern removal
  Shrinkage allowance: steel ~2%, cast iron ~1%, aluminum ~1.3%
  Riser: reservoir of molten metal to feed shrinkage during solidification

Die casting (pressure): Liquid metal injected under high pressure into metallic die
  High accuracy (±0.1mm), good surface finish, high rate — aluminum, zinc alloys
  Hot chamber (Zn/Mg): plunger in molten metal; fast cycle
  Cold chamber (Al): metal ladled in; slower

Investment (lost-wax): Wax pattern → ceramic shell → melt out wax → pour
  Complex parts, excellent surface, near-net-shape — aircraft blades, jewelry
  Tolerances: ±0.1mm typical

Centrifugal casting: Rotating mold (horizontal/vertical); pipes, bearings
```

### Solidification

```
Nucleation: Requires undercooling ΔT; heterogeneous (on foreign particles) >> homogeneous
  Grain refiners (TiB₂ in Al) add nucleation sites → finer equiaxed grains

Dendrite growth: Tree-like crystals grow toward cold regions
  SDAS (secondary dendrite arm spacing) ∝ (cooling rate)^(-1/3)
  Faster cooling → finer SDAS → better mechanical properties

Shrinkage:
  Liquid shrinkage: ~4% (volume) as T drops before solidification
  Solidification shrinkage: steel ~3%, Al ~7%, grey iron ~0% (graphite expansion)
  Solid shrinkage: linear ~1–2% after solidification

Porosity types:
  Shrinkage: centerline or hot spots → fix with risers/chills
  Gas: dissolved gas evolved on solidification → degas melt (degassing tablets, vacuum)
```

---

## Welding

### Key Processes

| Process | Heat source | Shielding | Applications |
|---------|-------------|-----------|-------------|
| SMAW (stick) | Electric arc | Coated electrode slag | Field welding, maintenance |
| GMAW/MIG | Arc + wire electrode | Gas (Ar, CO₂, mix) | High productivity, robotic |
| GTAW/TIG | Non-consumable W electrode | Gas (Ar, He) | Precision, thin materials, Ti |
| SAW (submerged arc) | Arc under flux | Flux blanket | Thick plates, pressure vessels |
| Electron beam | Focused e-beam | Vacuum | Deep narrow welds, aerospace |
| Laser | Focused laser | Gas | High speed, automation |
| Friction stir (FSW) | Friction + tool | None (solid state) | Aluminum alloys, dissimilar metals |

### Weld Metallurgy

```
Heat affected zone (HAZ):
  Fusion zone → solidification microstructure (dendrites)
  HAZ: heated above A₁ but below T_melt → grain growth, property changes
  Base metal: unaffected

HAZ problems:
  Sensitization (stainless): Cr carbides at grain boundaries → intergranular corrosion
  Hydrogen cracking (high-strength steel): H diffuses to HAZ → cold cracking
  Lamellar tearing: rolling inclusions perpendicular to weld → use through-thickness ductility grades

Residual stresses: weld shrinks as it cools → tension in weld, compression in base metal
  → Stress relief annealing (600–650°C for steel) or shot peening for fatigue
```

---

## Additive Manufacturing

```
Process        Material        Mechanism           Characteristics
──────────────────────────────────────────────────────────────────
FDM/FFF        Thermoplastics  Extruded filament   Cheap, anisotropic, rough
               (PLA, ABS, PEEK)

SLA/DLP        Photopolymer    UV curing           Smooth, brittle, limited materials
               resin

SLS (powder    Nylon, PC,      Laser sintering     No support needed, porous
bed, polymer)  glass-filled    of powder           unless infiltrated

DMLS/SLM       Metal powder    Laser melting       Near-full density, support needed
(powder bed,   (Ti, IN718,     of metal bed        for overhangs, residual stress
metal)         SS, AlSi10Mg)

EBM            Ti, Co-Cr       Electron beam melt  In vacuum, less residual stress
               metal powder    in vacuum           than SLM

DED (directed  Metal powder    Blown powder or     Repair, cladding, large parts
energy dep.)   or wire         wire melted by
                               laser/arc
```

**Design for AM (DfAM):**
- Lattice structures for lightweight stiffness
- Organic topology-optimized shapes impossible by subtractive methods
- Consolidated assemblies (reduce part count)
- Support structure minimization (costly to remove, surface quality issue)
- Layer orientation → mechanical anisotropy (tensile strength across layers ~50–80% of along-layer)

**Cost drivers:** Machine time (expensive), material cost (metal powder ~$50–200/kg), post-processing (HIP, machining, surface finishing often required).

---

## Tolerances and GD&T

### ISO Tolerance System

```
IT grades (International Tolerance):
  IT01–IT2: precision gauges
  IT3–IT7:  precision fits, bearings
  IT7–IT11: general machining
  IT12–IT16: rough machining, casting

Fundamental deviation: position of tolerance zone relative to zero line
  Lowercase letter → shaft: a through z
  Uppercase letter → hole: A through Z

Common fits:
  H7/h6: Clearance fit (running fit, easy assembly)
  H7/k6: Transition fit (could be clearance or interference)
  H7/p6: Press fit (interference, require pressing in)
  H7/s6: Force fit (heavy press, or shrink fit)
```

### GD&T (Geometric Dimensioning and Tolerancing)

```
Feature control frame: ┤ symbol │ tolerance │ datum(s) ├

Key symbols:
  ─┤⊙├─ Circularity (roundness): deviation from perfect circle
  ─┤⌭├─ Cylindricity: combined roundness + straightness
  ─┤//├─ Parallelism: relative to datum
  ─┤⊥├─ Perpendicularity: 90° to datum
  ─┤∠├─ Angularity: at specified angle to datum
  ─┤◎├─ Position: true position (replaces ± for holes)
  ─┤⌖├─ Concentricity / Runout
  ─┤↗├─ Profile of a line/surface

Maximum Material Condition (MMC): feature at largest material (smallest hole, largest shaft)
Least Material Condition (LMC): feature at smallest material
Regardless of Feature Size (RFS): tolerance applies regardless of actual size
```

---

## Common Confusion Points

**Hot working vs cold working:** Hot working = above recrystallization temperature (not melting point). 0.4 T_melt is rule of thumb. Recrystallization restores ductility as you deform → no work hardening. Cold working = below recrystallization → work hardens.

**Shrinkage allowance vs draft angle:** Shrinkage allowance in casting = make pattern/die larger to account for thermal contraction. Draft angle = taper to allow removal from mold (different concept).

**FDM layer orientation matters:** Parts printed with layers horizontal (Z = up) have much lower strength in the Z direction. Design critical features parallel to XY build plane.

**Investment casting vs die casting:** Investment casting: wax → ceramic mold → complex parts, ferrous + non-ferrous, low production rate. Die casting: metal die → high rate, tight tolerance, non-ferrous (Al, Zn, Mg) only (die life issues with steels).

**GD&T ± vs position tolerance:** ±0.5mm on X and Y for a hole center creates a square zone of side 1mm. True position ⊙0.5 creates a circular zone of diameter 0.5mm — more restrictive, or you get a "bonus tolerance" at MMC that allows more tolerance when feature is away from MMC.

---

## Decision Cheat Sheet

| Need | Process | Consider |
|------|---------|---------|
| Complex internal cavity, any material | Investment casting | Cost, surface finish |
| High-volume Al parts, close tolerance | Die casting | Tooling cost amortized |
| Structural steel part, custom shape | Open-die forging | Grain flow = strong |
| Complex steel part, high volume | Closed-die forging | Expensive tooling |
| Flat/prismatic features | Machining | CNC milling, turning |
| Round bores to h6 tolerance | Grinding or reaming | After rough machining |
| Complex metal part, low volume | DMLS/SLM metal AM | Post-machine critical features |
| Prototype, plastic | FDM/SLA | Mechanical anisotropy of FDM |
| Structural weld, outdoor | SMAW (stick) | Portable, weather tolerant |
| Thin wall, precision join | TIG (GTAW) | Skilled operator required |
| Long seam, thick plate | SAW | Automated, very productive |
