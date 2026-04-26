# Compressible Flow and Shock Waves

## The Big Picture

When flow speeds approach the speed of sound (Mach number M → 1), density changes become significant and new physics emerge: pressure waves propagate at finite speed, information cannot travel upstream in supersonic flow, and discontinuous solutions (shock waves) become thermodynamically required. Shock waves are one of the most dramatic phenomena in fluid dynamics — infinitesimally thin surfaces across which pressure, density, temperature, and velocity change abruptly, with irreversible entropy generation. Compressible flow is the fluid mechanics of high-speed aircraft, rockets, turbine engines, and explosions.

```
COMPRESSIBLE FLOW — REGIMES BY MACH NUMBER
═══════════════════════════════════════════════════════════════════════════════

  M = U/c,  c = √(γRT) = speed of sound

  M < 0.3     INCOMPRESSIBLE (density changes < 5%)
              All previous incompressible theory applies

  0.3 < M < 0.8  SUBSONIC COMPRESSIBLE
              Density corrections needed; no shocks
              Prandtl-Glauert correction: C_L → C_L/√(1-M²)

  0.8 < M < 1.2  TRANSONIC (mixed subsonic + supersonic + shocks)
              Most difficult regime; strong shock-boundary layer interaction

  M > 1.2     SUPERSONIC
              Oblique shocks; expansion fans; supersonic boundary layers
              Zone of silence: no information from sources downstream

  M > 5       HYPERSONIC
              Aerodynamic heating dominates; chemical dissociation,
              ionization; shock layer merges with boundary layer

  ┌────────────────────────────────────────────────────────────────┐
  │  KEY FACT: At M > 1, disturbances cannot propagate upstream    │
  │  (they are swept downstream at U > c).                         │
  │  ⟹  Supersonic flow "doesn't know" what's coming next.         │
  │  ⟹  Shocks form suddenly when flow must adjust to boundaries.  │
  └────────────────────────────────────────────────────────────────┘
```

---

## Governing Equations — Compressible Euler

For inviscid compressible flow (Euler equations):

    ∂ρ/∂t + ∇·(ρ**v**) = 0    (mass)
    ∂(ρ**v**)/∂t + ∇·(ρ**vv** + pI) = 0    (momentum)
    ∂E/∂t + ∇·[(E+p)**v**] = 0    (energy, E = ρ(e + v²/2))

Closed by an equation of state: for ideal gas, p = ρRT = (γ−1)ρe.

**Perfect gas relations**:
- γ = c_p/c_v (ratio of specific heats: 1.4 for air)
- c = √(γRT) = √(γp/ρ) (speed of sound)
- h = e + p/ρ (specific enthalpy: c_pT for perfect gas)

---

## Isentropic Flow Relations

For steady, adiabatic, reversible (isentropic) flow, stagnation quantities are conserved:

**Stagnation (total) conditions**: quantities at M = 0 (if flow were decelerated isentropically)

    T₀/T = 1 + (γ−1)/2 · M²    (total temperature)
    p₀/p = [1 + (γ−1)/2 · M²]^{γ/(γ−1)}    (total pressure)
    ρ₀/ρ = [1 + (γ−1)/2 · M²]^{1/(γ−1)}    (total density)

For air (γ = 1.4):
    T₀/T = 1 + 0.2M²
    p₀/p = (1 + 0.2M²)^{3.5}

**At M = 1** (sonic conditions, denoted *):
    T*/T₀ = 2/(γ+1) = 0.833 (air)
    p*/p₀ = [2/(γ+1)]^{γ/(γ−1)} = 0.528 (air)

---

## De Laval Nozzle and Throat Conditions

The de Laval (convergent-divergent) nozzle is the canonical compressible flow device — it accelerates flow from subsonic to supersonic.

```
DE LAVAL NOZZLE:

  RESERVOIR     CONVERGING  THROAT  DIVERGING   SUPERSONIC
  (p₀, T₀,M=0) ──────────── M=1 ──────────────  JET
    ────────────────────────────────────────────────────────
    high p,T              A*           low p,T
    low v                 (minimum area)  high v, M > 1

  AREA-MACH RELATION (from continuity + isentropic):
  A/A* = (1/M) × [(2/(γ+1))(1 + (γ−1)/2 M²)]^{(γ+1)/(2(γ−1))}
```

For given A/A*, there are TWO solutions: one subsonic (M < 1) and one supersonic (M > 1). Which occurs depends on the back pressure.

**Area-velocity relation**: dA/A = (M² − 1) dv/v
- M < 1 (subsonic): to accelerate (dv > 0), need convergence (dA < 0) — counter-intuitive at first
- M > 1 (supersonic): to accelerate, need divergence (dA > 0) — the "nozzle must expand to accelerate supersonic flow"

This is the fundamental design principle of rocket nozzles and supersonic wind tunnels.

---

## Normal Shock Waves

A **normal shock** is a discontinuity perpendicular to the flow, across which conditions jump.

**Rankine-Hugoniot jump conditions** (derived from conservation laws):

    ρ₁v₁ = ρ₂v₂    (mass)
    ρ₁v₁² + p₁ = ρ₂v₂² + p₂    (momentum)
    h₁ + v₁²/2 = h₂ + v₂²/2    (energy)

Solutions (in terms of M₁ = upstream Mach number):

    M₂² = (M₁² + 2/(γ−1)) / (2γ/(γ−1) M₁² − 1)

    p₂/p₁ = 1 + 2γ/(γ+1) (M₁² − 1)

    ρ₂/ρ₁ = (γ+1)M₁² / ((γ−1)M₁² + 2)

    T₂/T₁ = p₂/p₁ · ρ₁/ρ₂

```
NORMAL SHOCK PROPERTIES:
  Upstream: M₁ > 1 (MUST be supersonic)
  Downstream: M₂ < 1 (ALWAYS subsonic)

  For M₁ = 2.0 (air, γ = 1.4):
    M₂ = 0.577
    p₂/p₁ = 4.50
    ρ₂/ρ₁ = 2.67
    T₂/T₁ = 1.69
    p₀₂/p₀₁ = 0.721  (TOTAL pressure DECREASES — entropy increases)

  For M₁ = 1 (infinitely weak shock): ratios all = 1, entropy change = 0
```

**Second law**: Normal shocks are irreversible. Total pressure always decreases (p₀₂ < p₀₁). The entropy jump is:

    Δs = c_v ln(p₁/p₂ · (ρ₂/ρ₁)^γ) > 0    (2nd law satisfied)

The shock exists because supersonic flow cannot adjust smoothly to a boundary — the compression must occur as a discontinuity.

---

## Oblique Shocks and Expansion Fans

### Oblique Shocks

When supersonic flow turns INTO itself (compressive turn), an oblique shock forms at angle θ to the incoming flow. The shock turns the flow toward the surface.

```
OBLIQUE SHOCK:
  M₁ > 1
  ──────────────────────────────────────────────────────
  →→→→→→→→→→ shock angle β
                   ╲
  →→→→→→→→→→       ╲  deflection angle δ
              M₂<M₁  ╲
               →→→→→→→ ╲
  ──────────────────────────────────────────────────────
                     WALL (turns flow by δ)

  Θ-β-M relation: tan δ = 2 cot β [(M₁² sin²β − 1)/(M₁²(γ + cos 2β) + 2)]
  Two solutions for β given M₁ and δ: weak shock (β small) and strong shock
  In practice: weak shock occurs naturally
```

### Prandtl-Meyer Expansion Fan

When supersonic flow turns AWAY from itself (expansion), flow accelerates smoothly through a fan of Mach waves — no shock, no entropy change.

```
EXPANSION FAN (Prandtl-Meyer):
  M₁ > 1
  ────────────────────────────────
              ╭╭╭╭╭ fan of Mach waves (isentropic)
  →→→→→→ ╭╭╭╭╭╭
         M₁      M₂ > M₁
  ────────────────────────────────
                 CORNER (outward turn)
```

The Prandtl-Meyer function ν(M) gives the angle through which a sonic flow must turn to reach Mach M.

**Shock vs expansion**:
- Inward turn → shock (compression, entropy increase, M decreases)
- Outward turn → expansion fan (isentropic, M increases)

---

## Characteristic Methods

For supersonic flow, information propagates along **Mach lines** — these are the **characteristic curves** of the compressible Euler equations, which form a hyperbolic system. The Mach angle mu = arcsin(1/M) defines the cone of influence (domain of dependence) for each point: only the region inside the upstream Mach cone can affect conditions at a point. This is exactly the characteristic curve theory of first-order hyperbolic PDEs — finite signal speed, domains of dependence, and the consequence that supersonic flow "doesn't know what's ahead" because information cannot propagate upstream faster than the flow carries it downstream.

**Mach angle**: μ = arcsin(1/M) (angle between Mach line and flow direction)

```
MACH LINES:
  M = 1:   μ = 90°  (sound propagates perpendicular to flow)
  M = 2:   μ = 30°
  M = 5:   μ ≈ 12°
  M = ∞:   μ = 0°  (Mach lines align with flow)

  Supersonic zone of influence:
  A disturbance at point P influences only the region downstream of
  the Mach cone (Mach angle μ). Nothing upstream is affected.
```

**Method of Characteristics**: Compute supersonic flow by tracking information along characteristic lines. Used to design nozzle contours, supersonic diffusers.

---

## Shock Tube — The Canonical Experimental Setup

The shock tube is how shock physics is studied in the lab:

```
SHOCK TUBE:
  HIGH PRESSURE  |  LOW PRESSURE
      4           |       1
  ─────────────── DIAPHRAGM ──────────────────
  p₄, ρ₄, T₄    |  p₁, ρ₁, T₁

  DIAPHRAGM BURSTS:
  ←← RAREFACTION         CONTACT SURFACE  →→ SHOCK
      (p decreases)           │            (p jumps)
  ─────────── 4/3 ────────── 3/2 ───────── 2/1 ──

  Region 2: compressed, shocked gas
  Region 3: contact surface (density jump, no pressure jump)
  Rarefaction: isentropic expansion fan
```

The shock tube is used to generate precisely known high-pressure, high-temperature conditions for microseconds — enabling measurement of chemical reaction rates, material properties, and shock physics.

---

## Aerodynamic Heating

At hypersonic speeds, stagnation temperature is enormous:

    T₀ = T(1 + (γ−1)/2 M²) → T₀ ≈ 0.2 TM²  (for large M, γ=1.4)

At M = 8, T = 220 K (stratosphere): T₀ ≈ 3,000 K — above melting point of steel.

This is why reentry vehicles need thermal protection systems (ablative tiles on Space Shuttle, heat shield on Orion) — not just insulation but ablation (sacrificial evaporation of the heat shield material).

---

## Decision Cheat Sheet

| Situation | Tool |
|----------|------|
| Check if compressibility matters | Ma < 0.3 → incompressible; Ma > 0.3 → use compressible formulas |
| Stagnation temperature | T₀ = T(1 + (γ-1)M²/2) |
| Normal shock M₂ from M₁ | Use Rankine-Hugoniot; M₂ < 1 always |
| Supersonic nozzle throat | A* = A at M=1; use A/A* relation for given M |
| Oblique shock deflection | θ-β-M relation; weak shock branch |
| Flow around a corner (turning away) | Prandtl-Meyer expansion fan (isentropic) |
| Shock tube analysis | Rankine-Hugoniot for shock; isentropic for rarefaction |
| Heating at high M | T₀ = T(1 + 0.2M²) for air |

---

## Common Confusion Points

**Supersonic ≠ fast subsonic**: The physics changes qualitatively at M = 1. Supersonic flows cannot be treated as "really fast subsonic flows." Information propagation, wave structure, and governing equations are fundamentally different.

**Total pressure decrease through shocks**: Even though static pressure increases through a shock, total (stagnation) pressure always decreases (second law). This is why shocks are bad for engine inlets — they cause pressure losses that reduce thrust.

**Weak shocks are nearly isentropic**: For M₁ ≈ 1 (Mach waves), shock entropy increase scales as (M₁²-1)³. Oblique shocks with small turning angle are nearly isentropic. This is exploited in transonic airfoil design — many weak shocks are better than one strong one.

**The de Laval nozzle requires specific exit pressure**: For a nozzle to produce supersonic flow, the back pressure must be below the critical value (p*/p₀). If back pressure is too high, a normal shock forms inside the diverging section. Adjusting the back pressure moves the shock to the design point.
