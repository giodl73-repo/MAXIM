# 04 — Machine Design

Machine elements are **design contracts** — each has a defined input, output, and failure envelope:

- **Gears**: speed/torque transformers. Gear ratio i = omega_1/omega_2 = T_2/T_1 — a typed API contract where power in = power out (minus friction losses), and the ratio is the interface specification.
- **Bearings**: friction-reduction interfaces. Replace sliding friction (mu~0.3) with rolling contact (mu~0.001) — a 300:1 improvement in the friction coefficient contract.
- **Springs**: energy storage contracts. F = kx with defined stiffness, fatigue life, and natural frequency.
- **Shafts**: torque transmission channels. Sized for combined bending + torsion fatigue.

Three major topics not yet covered in this guide: **tribology** (Stribeck curve mapping boundary → mixed → hydrodynamic lubrication regimes), **vibration/resonance** (SDOF eigenvalue omega_n = sqrt(k/m), Campbell diagram for rotating machinery), and **mechanism synthesis** (Grashof condition for linkage design). These connect directly to eigenvalue decomposition, transfer functions, and state machine design.

## Stress, Failure Theories, Fatigue, Machine Elements

```
DESIGN PROCESS
        │
        ▼
┌───────────────────────────────────────────────────┐
│  Define loads + environment                        │
│  (forces, torques, temperatures, corrosion, ...)  │
├───────────────────────────────────────────────────┤
│  Compute stresses (σ, τ) and strains              │
│  Mohr's circle, principal stresses                │
├───────────────────────────────────────────────────┤
│  Select failure criterion (ductile vs brittle)    │
│  von Mises, Tresca, max normal stress             │
├───────────────────────────────────────────────────┤
│  Check fatigue life (if cyclic)                   │
│  Goodman diagram, S-N curve, Miner's rule         │
├───────────────────────────────────────────────────┤
│  Size the element with factor of safety n         │
│  Select materials, tolerances, surface finish     │
└───────────────────────────────────────────────────┘
```

---

## Stress and Strain Fundamentals

### Stress State

```
3D stress tensor (symmetric, 6 independent components):
     ┌ σx  τxy τxz ┐
σ =  │ τxy σy  τyz │
     └ τxz τyz σz  ┘

Principal stresses σ₁ ≥ σ₂ ≥ σ₃: eigenvalues (zero shear on principal planes)

2D plane stress (thin plates, surfaces): σz = τxz = τyz = 0

Principal stresses (2D):
  σ₁,₂ = (σx+σy)/2 ± √[((σx−σy)/2)² + τxy²]

Max shear stress (2D):
  τ_max = √[((σx−σy)/2)² + τxy²]  (in-plane)
  τ_abs_max = max of {τ₁₂, τ₂₃, τ₁₃}/2 where τᵢⱼ = (σᵢ−σⱼ)/2  (must check out-of-plane)
```

### Mohr's Circle

Graphical representation of stress state: circle with center at (σx+σy)/2 and radius = τ_max.

```
τ
│     ╭───────╮
│    ╱         ╲
│   │     C     │──── σ (horizontal axis)
│    ╲         ╱
│     ╰───────╯
│
└──────────────────► σ
     σ₂    C    σ₁
     (min) (avg) (max)
```

Rotate physical element by θ → rotate Mohr's circle by 2θ.

---

## Failure Theories

### Ductile Materials (most metals)

**Distortion Energy Theory (von Mises) — most accurate:**
```
σ_von Mises = σ_vm = √(σ₁² + σ₂² − σ₁σ₂)  (plane stress, σ₃=0)

3D: σ_vm = √(½[(σ₁−σ₂)² + (σ₂−σ₃)² + (σ₁−σ₃)²])

Failure when: σ_vm ≥ S_y  (yield strength)
Factor of safety: n = S_y / σ_vm
```

**Maximum Shear Stress Theory (Tresca) — more conservative:**
```
τ_max ≥ S_y/2   → failure
σ₁ − σ₃ ≥ S_y  → failure (in terms of principal stresses)

Tresca inscribed inside von Mises: predicts failure first (conservative by up to 15%)
```

**Which to use:** von Mises for design (less conservative, more accurate). Tresca for pressure vessels and code compliance (conservatism is specified).

### Brittle Materials (cast iron, glass, ceramics)

**Maximum Normal Stress Theory (Rankine):**
```
Failure when: σ₁ ≥ S_ut  or  |σ₃| ≥ S_uc
```

**Mohr's Theory (brittle):** Uses two circles: one at S_ut, one at −S_uc.
Better than max normal stress when S_uc ≠ S_ut (common for brittle materials).

---

## Stress Concentration

Real parts have notches, holes, fillets — stress concentrates there:
```
σ_max = Kt × σ_nom

where:
  σ_nom = nominal stress (based on net cross-section)
  Kt = stress concentration factor (geometric, from charts/FEA)

Example values of Kt:
  Round hole in infinite plate, tension: Kt = 3.0
  Deep U-notch: Kt = 4–6
  Sharp V-notch: Kt → ∞ (fracture mechanics regime)
  Fillet radius r/d = 0.1: Kt ≈ 1.6–2.5 (depends on geometry)
```

**Fatigue stress concentration Kf ≤ Kt:** Neuber's rule adjusts for notch sensitivity:
```
Kf = 1 + q(Kt − 1)   where q = notch sensitivity (0–1, from material/radius charts)
```
Ductile materials redistribute stress at notch (q < 1). Brittle materials: q ≈ 1.

---

## Fatigue

### S-N (Wöhler) Curve

```
S (stress amplitude)
│  ╲
│   ╲
│    ╲  High cycle fatigue
│     ╲
│      ──────────────────  Se (endurance limit, steels only)
│                          (No endurance limit for Al, Ti, polymers)
└──────────────────────────────► N (cycles to failure, log scale)
   10³  10⁴  10⁵  10⁶  10⁷  10⁸
```

**Endurance limit for steels (Marin equation):**
```
S_e = S_e' × k_a × k_b × k_c × k_d × k_e × k_f

S_e' = 0.5 S_ut  for S_ut ≤ 1400 MPa
     = 700 MPa   for S_ut > 1400 MPa

k_a = surface factor (machined vs ground vs hot-rolled)
k_b = size factor (d < 8mm: k_b=1; larger → k_b < 1)
k_c = loading factor (bending=1, axial=0.85, torsion=0.59)
k_d = temperature factor
k_e = reliability factor
k_f = miscellaneous (residual stress, corrosion, ...)
```

**Note:** No endurance limit for aluminum → use S_f at 10⁸ cycles (finite life design).

### Goodman Diagram (Most-Used Fatigue Design Tool)

Combines mean stress σ_m and alternating stress σ_a:

```
σ_a
│  S_e ─ ─ ─ ╲
│              ╲  (Goodman line, conservative)
│               ╲
│                ╲
│             ────╲──── (Gerber parabola, less conservative)
│                  ╲
└─────────────────────► σ_m
                  S_ut
```

**Goodman criterion (most common):**
```
σ_a/S_e + σ_m/S_ut = 1    → failure boundary

Factor of safety:
  1/n = σ_a/S_e + σ_m/S_ut

For fluctuating stress: σ_m = (σ_max + σ_min)/2, σ_a = (σ_max − σ_min)/2
```

**Miner's Rule** (cumulative damage):
```
D = Σ(n_i/N_i)   → failure when D = 1

n_i = cycles at stress level i
N_i = cycles to failure at stress level i (from S-N curve)
```

### Fracture Mechanics (LEFM)

**Engineering punchline:** Given an initial crack (detected by NDE or assumed at detection threshold), integrate da/dN = C(delta_K)^m to find the number of cycles until the crack reaches critical size. This integration is a first-order IVP where crack size a(N) evolves as a discrete dynamical system. The result sets the inspection interval — typically half the predicted life, so you catch the crack before it becomes critical. See materials-processing/05-FRACTURE-MECHANICS.md for the full treatment.

For high-cycle fatigue or brittle materials with cracks:
```
Stress intensity factor:
  K = σ√(πa) F    (F = geometry correction factor, tabulated)

Fracture when K ≥ K_IC  (critical stress intensity, material property)
→ critical crack size: a_c = (K_IC/(σF))²/π

Fatigue crack growth (Paris Law):
  da/dN = C(ΔK)^m   where ΔK = ΔσF√(πa)
  Integrate from a_initial to a_critical → total life

Inspection interval = life / safety factor
```

---

## Shaft Design

Combined bending (M) + torsion (T) is the standard case:
```
Bending stress (fully reversed): σ_a = 32M/(πd³)
Torsional stress (steady): τ_m = 16T/(πd³)

Distortion energy + Goodman (DE-Goodman criterion):
  16/(πd³) × √[(8M K_f/S_e)² + (K_fs T_m/S_ut)²] = 1/n

Solve for diameter d:
  d = {16n/π × [4(K_f M_a/S_e)² + 3(K_fs T_m/S_e)² + 4(K_f M_m/S_ut)² + 3(K_fs T_a/S_ut)²]^(1/2)}^(1/3)
```

---

## Rolling Element Bearings

A bearing is a friction-reduction contract: rolling contact (mu~0.001) replaces sliding contact (mu~0.3). The L10 life equation embeds a probabilistic contract — the C/P ratio determines the statistical reliability at a given operating life. **Hydrodynamic plain bearings** (crankshafts, large turbines) operate on a different contract: they require minimum speed to maintain a full oil film (the Stribeck curve maps friction vs. speed through boundary → mixed → hydrodynamic regimes). Below the minimum speed, the film breaks down and friction spikes.

**Load-life relationship (L10 = 90% reliability):**
```
L10 = (C/P)^p × 10⁶ rev

C = dynamic load rating [N] (from bearing catalog)
P = equivalent dynamic load [N]
p = 3 for ball bearings, 10/3 for roller bearings

P = X Fr + Y Fa    (radial Fr, axial Fa, factors X, Y from catalog)

For reliability R ≠ 90%:
  L_n = a₁ L10   where a₁ = reliability factor
```

**Bearing selection process:**
1. Compute required life (hours × rpm = revolutions)
2. Determine equivalent load P
3. Select C from catalog: C = P × (L_required/10⁶)^(1/p)
4. Check bore size, radial/axial load capacity, speed limit

---

## Gears

### Geometry

```
Module m = d/N = 1/P_d
  d = pitch circle diameter [mm]
  N = number of teeth
  P_d = diametral pitch (US units: teeth/inch)

Standard pressure angle: 20° (was 14.5°, still found on old equipment)
Addendum: a = m     (tooth extends above pitch circle by one module)
Dedendum: b = 1.25m  (tooth extends below pitch circle)
```

**Gear ratio:** i = N₂/N₁ = d₂/d₁ = ω₁/ω₂ = T₂/T₁ (torque ratio is inverse of speed ratio)
**Contact ratio:** typically 1.5–2.0 (>1 means multiple teeth in contact simultaneously)

### Gear Forces (Spur Gear)

```
Tangential force: Ft = 2T/d = P/v    (transmits torque)
Radial force:     Fr = Ft tan(φ)     (separates gears, loads bearings)
                  φ = pressure angle
```

**AGMA gear stress equations:**
```
Bending stress: σ_b = Ft/(b m) × Ko Ka Km Ks / (Kv J)
Contact stress: σ_c = Cp √(Ft Ko Ka Km Ks / (d b Kv I))

Ko = overload factor, Ka = application factor, Km = load distribution
Kv = dynamic factor, Ks = size factor, J = geometry factor
Cp = elastic coefficient, I = pitting resistance geometry factor
```

### Worm Gears

High reduction in single stage (10:1 to 100:1). But high sliding → low efficiency.
```
Self-locking: if lead angle λ < arctan(μ)   (can't back-drive)
Efficiency: η = tan(λ)/tan(λ + φ')   where φ' = friction angle
λ small → self-locking, but also low efficiency (~30–50%)
λ large → non-locking, higher efficiency (~80–95%)
```

---

## Fasteners and Bolted Joints

### Bolt Preload

```
Preload F_i = target: ~75% of proof strength load

Proof load F_p = A_t × S_p
  A_t = tensile stress area (threaded section)
  S_p = proof strength ≈ 0.85 S_y

Torque to achieve preload:
  T = K F_i d   where K ≈ 0.2 for lubricated, 0.3 for dry
```

### Joint Analysis Under External Load

```
Member stiffness km vs bolt stiffness kb:
  Bolt stiffness: kb = A_b E / l_b
  Member stiffness: km >> kb  (typically km/kb ~ 3–10)

Load sharing:
  Bolt load = F_i + Pb       Pb = P × kb/(kb+km)
  Joint load = F_i − Pm      Pm = P × km/(kb+km)

Joint separation (opening) when compression in member → 0:
  F_separation = F_i × km/(kb+km) / P_crit

Factor of safety against separation: n_sep = F_i / P(km/(kb+km))
Factor of safety against bolt yielding: n_yield = (S_p A_t − F_i) / Pb
```

---

## Springs

**Helical compression spring:**
```
Spring rate: k = G d⁴ / (8 D³ Na)
  G = shear modulus (79 GPa for steel)
  d = wire diameter, D = mean coil diameter, Na = active coils

Shear stress (Wahl factor):
  τ = 8FD/(πd³) × K_W
  K_W = (4C-1)/(4C-4) + 0.615/C   where C = D/d = spring index

Solid length: L_s = d(Nt)   (natural stop against overcompression)
Natural frequency: fn = (d/πNa D²)√(G/8ρ)  (avoid resonance)
```

**Vibration note:** The SDOF equation m*x'' + c*x' + kx = F(t) has natural frequency omega_n = sqrt(k/m) — the eigenvalue of the mass-stiffness system. The frequency response function H(omega) = 1/(k - m*omega^2 + j*c*omega) is the mechanical transfer function (same Laplace/Fourier-domain analysis from signals & systems). For rotating machinery, the Campbell diagram plots natural frequencies vs rotational speed — critical speeds occur where excitation harmonics cross natural frequency lines, causing resonance. This is the most important practical application of vibration analysis in machine design. Full treatment would merit its own section.

---

## Common Confusion Points

**von Mises vs principal stress:** von Mises predicts yielding based on distortion energy, not maximum stress. A state of equal triaxial tension (σ₁=σ₂=σ₃=S_y) never yields by von Mises (no distortion), even though each principal stress equals S_y. This is correct — hydrostatic stress doesn't cause yielding.

**Endurance limit vs fatigue strength:** Only steels have a true endurance limit (horizontal S-N asymptote). Aluminum, titanium, and polymers have no true endurance limit — specify life in cycles.

**Goodman vs Gerber:** Goodman is linear and conservative. Gerber parabola is more accurate but harder to use and not conservative. Soderberg (using S_y instead of S_ut) is most conservative. Use Goodman for design, compare to test data.

**Rolling vs plain bearings:** Ball/roller bearings dominate for intermittent operation, moderate speed, easy replacement. Plain (journal) bearings dominate for high speed, high load, continuous operation (crankshaft, large turbines) — only work with hydrodynamic film established.

**Stress concentration for static vs fatigue:** Under static ductile loading, Kt doesn't reduce ultimate strength much (yielding redistributes stress). Under fatigue, Kf reduces endurance limit significantly. Never ignore Kf in fatigue calculations.

---

## Decision Cheat Sheet

| Question | Tool | Notes |
|----------|------|-------|
| Will this ductile part yield? | von Mises criterion | σ_vm = S_y/n |
| Will this brittle part fracture? | Max normal stress / Mohr | σ₁ = S_ut/n |
| How long will this part last? (cyclic) | Goodman diagram + S-N | Account for Kf, surface finish |
| What bearing size? | L10 life equation | C/P ratio → catalog |
| How big should the shaft be? | DE-Goodman | Check combined M+T |
| Are these bolts tight enough? | Joint separation analysis | n_sep > 1 required |
| What gear ratio? | N₂/N₁ = i | Torque scales inversely |
| Can I back-drive this worm? | Lead angle vs friction angle | λ < arctan(μ): self-locking |
