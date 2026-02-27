# Hydrodynamics and Free-Surface Flows

## The Big Picture

Hydrodynamics is fluid dynamics with free surfaces (where water meets air), gravity waves, and flows dominated by gravity rather than pressure gradients. The key new feature: the free surface is a boundary that deforms with the flow. This creates waves, sloshing, hydraulic jumps, tsunamis, and geophysical circulation. The Froude number Fr = U/√(gL) is the governing parameter — it separates subcritical (Fr < 1, wave information propagates upstream) from supercritical (Fr > 1, hydraulic analogue of supersonic flow).

```
FREE-SURFACE FLOWS — LANDSCAPE
═══════════════════════════════════════════════════════════════════════════════

  FROUDE NUMBER: Fr = U/√(gL) = inertia/gravity

  Fr < 1  SUBCRITICAL (tranquil, deep)
  ─────────────────────────────────────────────────────────────────────
  │ Gravity waves propagate upstream and downstream                    │
  │ Information can travel upstream (like subsonic flow)              │
  │ Deep water: wave speed c = √(gλ/2π) for surface gravity waves    │
  └─────────────────────────────────────────────────────────────────────

  Fr = 1  CRITICAL (standing waves, hydraulic jump transition)
  ─────────────────────────────────────────────────────────────────────
  │ Wave speed = flow speed                                           │
  └─────────────────────────────────────────────────────────────────────

  Fr > 1  SUPERCRITICAL (shooting, rapid)
  ─────────────────────────────────────────────────────────────────────
  │ Flow faster than wave speed                                       │
  │ Information cannot propagate upstream (like supersonic flow)      │
  │ Hydraulic jump = analogue of normal shock                        │
  └─────────────────────────────────────────────────────────────────────
```

---

## Surface Gravity Waves

Small-amplitude (linear) water waves on a layer of depth h:

**Dispersion relation**:

    ω² = gk tanh(kh)    where k = 2π/λ (wavenumber), ω = 2π/T (angular frequency)

**Phase speed**: c_p = ω/k = √(g/k tanh(kh))

**Group speed**: c_g = dω/dk = ∂ω/∂k (speed of wave energy transport)

### Deep Water (kh >> 1): tanh(kh) → 1

    ω = √(gk)
    c_p = √(g/k) = √(gλ/2π)  (longer waves go faster)
    c_g = c_p/2  (energy travels at HALF the phase speed)

```
DEEP WATER WAVE PROPERTIES:
  Wavelength  100 m:  c_p = √(9.8 × 100/2π) ≈ 12.5 m/s = 45 km/h
  Wavelength  1 km:   c_p ≈ 40 m/s = 144 km/h
  Wavelength  100 km: c_p ≈ 400 m/s = 1440 km/h  (ocean swell)
  Wavelength  200 km: c_p ≈ 560 m/s (tsunami wavelength → shallow water)
```

**Dispersive**: deep water waves are dispersive — different wavelengths travel at different speeds. A wave packet spreads out over time (like optical dispersion in fiber).

### Shallow Water (kh << 1): tanh(kh) → kh

    ω = k√(gh)
    c_p = c_g = √(gh)  (non-dispersive!)

**Tsunamis**: long-wavelength waves (λ ~ 200 km >> ocean depth h ~ 4 km) → shallow water limit:
    c = √(gh) = √(9.8 × 4000) ≈ 200 m/s = 720 km/h

Tsunamis travel at jetliner speed across the ocean. As they approach the coast (h decreases), c decreases and wave amplitude grows (shoaling).

---

## Hydraulic Jump

The hydraulic analogue of a normal shock wave. Subcritical → supercritical (or vice versa) flow transition.

```
HYDRAULIC JUMP:

  SUPERCRITICAL          JUMP        SUBCRITICAL
  (Fr > 1, shallow, fast)  │  (Fr < 1, deep, slow)
                            │
  ────────────────────── ╔══╝══╗ ──────────────────────
  →→→→→→→→→→→→→→→→→→→→  ║FOAM ║  ──────────────────→→
  (fast, shallow)         ║ZONE ║  (slow, deep)
  ──────────────────────  ╚══╗══╝ ──────────────────────
                            │
                        JUMP OCCURS HERE
```

**Jump relations** (from mass and momentum conservation, analogue of Rankine-Hugoniot):

    h₂/h₁ = (1/2)(√(1 + 8Fr₁²) − 1)    (sequent depth ratio)

    Fr₁ > 1, Fr₂ < 1 (transition from super to subcritical)

**Energy dissipation**: significant energy is lost in a hydraulic jump (turbulent mixing, foam). The flow is irreversible. This is used in spillways and stilling basins to dissipate energy safely.

---

## Open Channel Flow (Manning's Equation)

For gravity-driven flow in open channels (rivers, canals):

**Manning's equation**:

    Q = (1/n) A R_h^{2/3} S₀^{1/2}

where:
- Q = volumetric flow rate
- n = Manning roughness coefficient (0.01 for smooth concrete, 0.04 for natural rivers)
- A = cross-sectional area
- R_h = A/P = hydraulic radius (A = area, P = wetted perimeter)
- S₀ = bed slope (dimensionless)

**Physical meaning**: Flow rate increases with cross-section, with bed slope, and with smoothness (1/n).

---

## Geophysical Flows — Rotation and Stratification

At large scales (oceans, atmosphere), two additional effects dominate:

### Coriolis Effect (Earth's rotation)

For flow in a rotating frame (Earth's rotation Ω = 7.3×10⁻⁵ rad/s):

    Added term in momentum: −2**Ω** × **v** (Coriolis force per unit mass)

**Rossby number**: Ro = U/(fL) where f = 2Ω sin(latitude) = Coriolis parameter

- Ro >> 1: rotation negligible (small scales, fast flows)
- Ro << 1: rotation dominates (large scales, slow flows = geostrophic balance)

**Geostrophic balance** (Ro << 1): pressure gradient balances Coriolis:

    f × **v**_h = −(1/ρ)∇_h p

Flow goes *along* isobars (pressure contours), not toward low pressure. This is why winds rotate around cyclones rather than directly into them.

### Stratification (density variations)

**Brunt-Väisälä frequency**: N = √(−g/ρ · dρ/dz) (stable: dρ/dz < 0)

N characterizes the oscillation frequency of a displaced fluid parcel:
- N² > 0: stable stratification (parcel oscillates back)
- N² < 0: convective instability (parcel accelerates away)

**Internal gravity waves**: In stratified fluid, waves travel on density surfaces (isopycnals) rather than the free surface.

---

## Waves at Interfaces — Kelvin-Helmholtz Instability

At the interface between two fluids moving at different speeds, or two layers of different density:

**Kelvin-Helmholtz instability**: Derived by standard linear stability analysis — assume perturbations of the form e^{sigma*t + ikx} (normal modes), substitute into the linearized equations, and solve the resulting eigenvalue problem for sigma(k). Instability occurs when Re(sigma) > 0. Small perturbations grow when:

    (ρ₁ + ρ₂)(U₁ − U₂)² > 4gk(ρ₁ − ρ₂) × tanh(kh₁) × tanh(kh₂)

For equal-density fluids (ρ₁ = ρ₂): always unstable for any velocity difference.
For stratified: gravity stabilizes short waves; instability at intermediate k.

```
KELVIN-HELMHOLTZ INSTABILITY:

  Stable:    ──────────────────────────────────── ρ₂
             ──────────────────────────────────── ρ₁ > ρ₂

  Perturbed: ───────────────────────────────────
                     ∿∿∿∿∿∿∿∿∿∿∿∿∿∿              → growing waves

  Rolled up: ───────────────────────────────────
                    ○ ○ ○ ○ ○ ○ ○               → vortex rolls

  Seen in: clouds (Kelvin-Helmholtz clouds = billowing undulations),
           ocean thermocline, atmosphere, solar corona, Saturn's bands
```

---

## Sloshing and Wave Resonance

Liquid in a container can resonate when forced at its natural frequencies.

**Natural frequencies of a rectangular tank** (length L, depth h):

    ω_n = √(gk_n tanh(k_n h))    where k_n = nπ/L, n = 1, 2, ...

**Sloshing in engineering**: Important for fuel tanks in spacecraft, LNG tankers, liquid-filled road tankers. Resonance can cause catastrophic structural loads.

**Seiche**: Standing wave in an enclosed or semi-enclosed basin (bay, lake). Period T = 2L/c where c = √(gh). Lake Baikal has seiche periods of hours.

---

## Capillary Waves and Surface Tension

At small scales, surface tension σ competes with gravity. **Weber number**: We = ρU²L/σ.

**Capillary-gravity dispersion relation** (complete form including surface tension):

    ω² = (gk + σk³/ρ) tanh(kh)

**Minimum phase speed** at capillary-gravity crossover:

    k_min = √(ρg/σ)    c_min = (4gσ/ρ)^{1/4} ≈ 0.23 m/s (for water)

Waves with λ > 2π/k_min = 2π√(σ/ρg) ≈ 1.7 cm are gravity-dominated.
Waves with λ < 1.7 cm are capillary-dominated.

A boat moving slower than 0.23 m/s creates no wave — this is the minimum phase speed below which no surface waves can be sustained.

---

## Decision Cheat Sheet

| Situation | Tool |
|----------|-----|
| Classify channel flow | Fr = V/√(gh): <1 subcritical, >1 supercritical |
| Analyze hydraulic jump | Sequent depth ratio from Fr₁ |
| Deep water wave speed | c = √(gλ/2π) |
| Shallow water / tsunami speed | c = √(gh) |
| Open channel flow rate | Manning's equation |
| Geophysical flow (large scale) | Rossby number, geostrophic balance |
| Stratification stability | Brunt-Väisälä frequency N |
| Interface instability | Kelvin-Helmholtz criterion |
| Capillary effects important? | Weber number We = ρU²L/σ |

---

## Common Confusion Points

**Wave speed ≠ water particle speed**: In ocean waves, water particles move in circles (deep water) — they don't travel with the wave. A floating cork bobs up and down but doesn't move forward with the wave pattern. Phase speed c = ω/k is the speed of the wave crest, not water molecules.

**Group velocity ≠ phase velocity**: For dispersive waves (deep water), c_g = c_p/2. Energy travels at the group velocity, not the phase velocity. Wave groups (packets of multiple wavelengths) spread out because each component has a different phase speed.

**Hydraulic jump is analogous to a normal shock, not exactly equivalent**: Both involve a transition from "supercritical" (Fr > 1 or M > 1) to "subcritical" (Fr < 1 or M < 1), with entropy increase and total energy/pressure loss. But the governing equations and media are different (water vs gas; incompressible vs compressible).

**Coriolis does not cause water draining clockwise/counterclockwise in hemispheres**: The Coriolis effect is real and important for hurricanes (100s of km scale). For bathtub drains (cm scale), Ro >> 1, and surface tension, initial conditions, and container shape dominate. Experiments that "demonstrate" Coriolis in drains are controlled illusions.
