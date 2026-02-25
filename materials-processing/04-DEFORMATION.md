# Plastic Deformation and Work Hardening

## The Big Picture

Plastic deformation changes the shape of a metal permanently by moving dislocations through the crystal lattice. The interaction between dislocations — and between dislocations and other microstructural features — determines why metals get harder when deformed (work hardening) and how to undo that hardening (annealing).

```
DEFORMATION MECHANISMS BY TEMPERATURE
──────────────────────────────────────────────────────────────────
Low T / High strain rate          High T / Low strain rate
(Cold work regime)                (Creep regime)
──────────────────────────────    ──────────────────────────────
Dislocation glide                 Dislocation climb + recovery
Twinning (BCC, HCP)               Grain boundary sliding
Work hardening accumulates        No hardening accumulation
→ Increased yield strength        → Strain rate sensitive
→ Decreased ductility             → Time-dependent flow

"Cold work" < 0.3 Tm              "Hot work" > 0.6 Tm
"Warm work" 0.3–0.6 Tm

Tm = melting temperature in Kelvin
At room temperature:
  Al (Tm=933K): T/Tm = 298/933 = 0.32 → warm for Al
  Fe (Tm=1811K): T/Tm = 298/1811 = 0.16 → cold for steel
  Pb (Tm=600K): T/Tm = 298/600 = 0.50 → warm for Pb
    (Pb cannot work harden at room temperature — it self-anneals)
```

---

## Dislocation Theory

### Edge and Screw Dislocations

```
DISLOCATION TYPES
──────────────────────────────────────────────────────────────────
EDGE DISLOCATION:
  Extra half-plane of atoms inserted in crystal
  Burgers vector ⊥ to dislocation line
  Moves by glide (easy) in glide plane containing both
  Moves perpendicular to glide plane by climb (requires diffusion)

  Perfect lattice:      With edge dislocation:
  ○ ○ ○ ○ ○ ○          ○ ○ ○ ○ ○ ○
  ○ ○ ○ ○ ○ ○          ○ ○ ○ ○ ○ ○
  ○ ○ ○ ○ ○ ○          ○ ○ ○ ↓ ○ ○  ← extra half-plane
  ○ ○ ○ ○ ○ ○          ○ ○ ○ ○ ○ ○

SCREW DISLOCATION:
  Spiral stacking: lattice planes form helix around dislocation line
  Burgers vector ∥ to dislocation line
  Can glide on any plane containing the dislocation line
  (More flexibility in cross-slip)

MIXED DISLOCATION:
  Most real dislocations have both edge and screw character
  Burgers vector at angle to dislocation line
```

### Critical Resolved Shear Stress (CRSS)

```
SCHMID'S LAW
──────────────────────────────────────────────────────────────────
Slip occurs when resolved shear stress on slip system exceeds CRSS:
  τ_resolved = σ × cos(φ) × cos(λ)
  φ = angle between load and slip plane normal
  λ = angle between load and slip direction
  M = cos(φ)cos(λ) = Schmid factor

Slip occurs when: τ_resolved ≥ τ_critical (material constant)

Schmid factor range: 0 to 0.5
  M = 0.5: most favorably oriented grain → slips first
  M = 0: hard orientation (load ∥ slip plane or ∥ slip direction)

FCC metals (Cu, Al, Ni, γ-Fe): {111}⟨110⟩ slip systems
  12 independent slip systems → very ductile, low CRSS
BCC metals (α-Fe, W, Mo): {110}⟨111⟩ + other systems
  48 possible slip systems → high CRSS, more sensitive to temperature
HCP metals (Ti-α, Mg, Zn): limited slip systems
  3 basal slip systems → brittle, anisotropic
  Twinning important for deformation of Mg
```

---

## Work Hardening (Strain Hardening)

### The Hardening Mechanism

```
WHY DISLOCATIONS CAUSE WORK HARDENING
──────────────────────────────────────────────────────────────────
Dislocation density ρ increases with deformation:
  Annealed metal: ρ ≈ 10⁶–10⁸ cm⁻²
  Heavily cold-worked: ρ ≈ 10¹¹–10¹² cm⁻²

As dislocations multiply, they interact with each other:
  Intersections: "jogs" created → point defects → immobile segments
  Lomer-Cottrell locks: immobile dislocation formed by reaction
  Pile-ups: dislocations behind barriers (grain boundaries) pile up
  → Stress field of pile-up back-stress stops new dislocations

Result: to continue deformation, higher stress needed
  → Yield strength increases with strain
  → Ductility decreases (dislocations run out of room)

TAYLOR RELATION:
  τ ≈ τ₀ + αGb√ρ
  G = shear modulus, b = Burgers vector magnitude, α ≈ 0.5
  Strength proportional to square root of dislocation density
```

### True Stress-Strain and Work Hardening Rate

```
TRUE STRESS-STRAIN CURVE
──────────────────────────────────────────────────────────────────
True stress:   σ = F/A  (current area A, not original A₀)
True strain:   ε = ln(L/L₀)  (natural log)

vs. Engineering:
  σ_eng = F/A₀,  ε_eng = (L-L₀)/L₀
  At large strains: engineering stress shows "necking" drop
  True stress continues rising until fracture

POWER LAW (Hollomon equation):
  σ = K × εⁿ
  K = strength coefficient (material constant)
  n = strain hardening exponent (0 ≤ n ≤ 1)

  n = 0: perfectly rigid-plastic (no hardening)
  n = 1: linear hardening
  Typical values:
    Copper (annealed):    n ≈ 0.54
    Aluminum 1100:        n ≈ 0.20
    Low carbon steel:     n ≈ 0.22
    Stainless 304:        n ≈ 0.44

High n → deep drawability (uniform deformation without necking)
Low n → quick necking, limited drawability

NECKING CRITERION (Considère):
  Necking begins when dσ/dε = σ  (i.e., when n = ε at necking)
  Therefore: true strain at necking = n
```

---

## Recrystallization and Annealing

### Recovery, Recrystallization, Grain Growth

```
STAGES OF ANNEALING (cold-worked metal heated)
──────────────────────────────────────────────────────────────────
RECOVERY (low temperature, 0.3–0.5 Tm):
  Dislocation rearrangement, annihilation
  Residual stress decreases significantly
  Hardness decreases slightly
  Electrical resistivity decreases (point defects heal)
  Subgrain structure forms (cells with low-angle boundaries)
  No new grain boundaries formed

RECRYSTALLIZATION (medium temperature, 0.4–0.6 Tm):
  New strain-free grains nucleate and grow
  Consumes deformed (high-energy) microstructure
  Rapid decrease in hardness and strength
  Recovery of ductility
  Driving force: stored energy of cold work (dislocation density)

GRAIN GROWTH (high temperature, >0.5–0.6 Tm):
  After recrystallization complete, grains coarsen
  Larger grains consume smaller (capillary driving force)
  Grain boundary energy minimized
  Grain diameter D ∝ t^(1/2) × exp(-Q/RT)
  Reduced strength, increased ductility

        Hardness
           │
           │╲               ← Recrystallization knee
           │ ╲
           │  ╲──────────────────────
           │    Recovery zone
           └─────────────────────────────► Temperature
        Recovery  Recrystallization  Grain growth
```

### Recrystallization Temperature

```
RECRYSTALLIZATION TEMPERATURE
──────────────────────────────────────────────────────────────────
Definition: Temperature at which recrystallization is complete
  in 1 hour for heavily deformed metal.
Typically: 0.4–0.6 × Tm (Kelvin scale)

Material dependence:
  Pure metal:    lower Trex (~0.3 Tm) — no solute drag
  Alloyed:       higher Trex — solute and precipitates pin boundaries

Approximate recrystallization temperatures:
  Aluminum (1xxx): ~150°C
  Aluminum alloys (2xxx, 7xxx): 300–400°C
  Copper:          ~200°C
  Iron (low-C):    ~450°C
  Nickel:          ~600°C
  Tungsten:        ~1200°C

Factors that LOWER Trex:
  Heavier cold work (more stored energy → larger driving force)
  Smaller grain size (more nucleation sites)
  Purer metal (less solute drag)

Factors that RAISE Trex:
  Alloying (solute drag on boundary migration)
  Prior warm work (partial recovery, less driving force)
  Large initial grain size (fewer nucleation sites)
```

### Dynamic Recrystallization (DRX)

```
DYNAMIC RECRYSTALLIZATION (DRX)
──────────────────────────────────────────────────────────────────
Recrystallization DURING deformation (not during subsequent anneal).
Occurs in hot working when:
  Temperature > 0.5–0.6 Tm
  Strain rate low enough for recovery
  Critical strain (usually ~2× strain at peak stress)

Mechanism:
  Strain accumulates → dislocations pile up → nucleate new grains
  New grains grow, then strain accumulates again → oscillating behavior

Consequences in hot rolling/forging:
  Grain is continuously refined during pass
  Final grain size controlled by deformation conditions
  More deformation per pass → finer grains → higher strength

DYNAMIC STRAIN AGING (DSA):
  Solutes diffuse to dislocations DURING straining
  "Locks" dislocations temporarily → Portevin–Le Chatelier effect
  Serrated stress-strain curve (saw-tooth)
  Common in: Al-Mg, mild steel at certain T/strain rate
  Can cause fatigue damage in structures (avoid by design or alloy choice)
```

---

## Deformation Textures

```
CRYSTALLOGRAPHIC TEXTURE
──────────────────────────────────────────────────────────────────
Random polycrystal: all grain orientations equally probable
  Properties: isotropic (same in all directions)

Textured material: grain orientations non-random (preferred orientation)
  Caused by: rolling, drawing, extrusion, solidification

Rolling texture (FCC, Al, Cu):
  {110}⟨112⟩ "brass" and {112}⟨111⟩ "copper" components
  Magnetic soft iron: {110}⟨001⟩ Goss texture → easy magnetization
    (used in transformer laminations)

Consequences of texture:
  Anisotropy:   properties different in rolling vs transverse direction
  Earing:       deep drawn cups have "ears" at 45° or 90° to roll direction
  Springback:   anisotropic springback in sheet metal bending
  R-value (Lankford coefficient):
    R = ε_width / ε_thickness during tensile test
    High R → resistant to thinning → good deep drawability
    R depends on texture; R > 1 preferred for deep drawing
```

---

## Flow Stress and Forming Parameters

```
FLOW STRESS IN HOT WORKING
──────────────────────────────────────────────────────────────────
Flow stress σ_f depends on: temperature, strain, strain rate

Simplified power law:
  σ_f = C × ε̇ᵐ      (at constant T and ε)
  m = strain rate sensitivity exponent

  m ≈ 0.1–0.2: most metals at hot working temperatures
  m ≈ 0.5: superplastic materials (Ti-6Al-4V at 850°C, fine grain)
  m = 1.0: Newtonian viscous flow (glass, hot glass processing)

Superplasticity:
  Fine grain (<10 µm) + high T (>0.5 Tm) + slow strain rate
  → Elongations of 200–1000% without necking
  → Used for aerospace forming (Ti-6Al-4V SPF, blow forming)

Zener-Hollomon parameter (hot working):
  Z = ε̇ × exp(Q/RT)
  Normalizes strain rate by temperature effect
  Lower Z → finer recrystallized grain (hot worked aluminum, steel)
```

---

## Work Hardening Applications

```
ENGINEERING USE OF WORK HARDENING
──────────────────────────────────────────────────────────────────
Shot peening:
  Metal shot impacts surface → localized surface plastic deformation
  → Compressive residual stress in surface layer
  → Improved fatigue life (cracks initiate at tension, not compression)
  Application: turbine blades, springs, gears, aircraft structure

Cold drawing (wire, tube):
  Progressive reduction through dies → significant cold work
  Yield strength increases with each draw pass
  High-strength steel wire (piano wire): 2000+ MPa by cold drawing
  Annealing between passes if too much work hardening

Prestressing:
  Autofrettage: over-pressurize gun barrel or pressure vessel
  → Surface compressive residual stress
  → Increased fatigue life and burst pressure

Skin pass / tension leveling:
  Light cold work (0.5–3%) on steel sheet:
  → Eliminate yield point phenomenon (Lüders bands)
  → Improve flatness
  → Slight strength increase
```

---

## Decision Cheat Sheet

| I want to achieve... | Process |
|---------------------|---------|
| Increase yield strength without heat treatment | Cold work (rolling, drawing, shot peen) |
| Improve fatigue life of critical surface | Shot peen or laser peen (compressive residual stress) |
| Soften work-hardened metal for more forming | Recrystallization anneal |
| Grain refinement via hot working | Hot rolling/forging with DRX (high reduction, controlled T) |
| Remove processing texture | Anneal above recrystallization T with appropriate conditions |
| Maximize deep drawability (Al/steel sheet) | High n, high R-value alloy; texture control |
| Very high strength wire | Heavy cold drawing (no intermediate anneal) |
| Titanium complex formed shape | Superplastic forming (SPF) at 850°C |

---

## Common Confusion Points

**Cold work vs cold rolling**: Cold work is any plastic deformation below 0.3 Tm. Cold rolling is a specific process. Cold work is the general phenomenon that cold rolling causes. You can work harden by drawing, forging, bending, shot peening — all are "cold work" if done below 0.3 Tm.

**Recovery ≠ recrystallization**: Recovery reduces residual stress and slightly reduces hardness — no new grains form. Recrystallization creates new strain-free grains — major hardness and strength reduction. In practice, recovery is often incomplete when recrystallization begins. They overlap.

**Grain size vs grain growth**: Grain refinement (smaller grains) increases yield strength (Hall-Petch: σ = σ₀ + k/√d). Grain growth during prolonged annealing at high temperature reverses this — coarser grains, lower yield strength, higher ductility. The grain size goal depends on the application.

**Dynamic recrystallization in hot working is not recrystallization in annealing**: DRX during hot rolling occurs simultaneously with deformation, controlled by strain rate and temperature. Static recrystallization (SRX) occurs during the inter-pass intervals and in post-deformation annealing. Both contribute to final grain size in hot worked products, but through different mechanisms and timing.

**Texture anisotropy in sheet metal is exploitable**: "Earing" (non-uniform ear formation in deep drawing) is a quality defect. But controlled texture (high R-value) is deliberately developed in deep-drawing-quality (DDQ) steel and aluminum sheet. Texture is not inherently bad — its effect on the target product determines whether it's a problem or a feature.
