# Acoustic Wave Physics — A Layered Guide

## The Big Picture

All acoustic phenomena derive from the wave equation. The solutions predict how sound propagates,
reflects, diffracts, and forms standing wave patterns.

```
ACOUSTIC WAVE PHYSICS MAP
════════════════════════════════════════════════════════════════════

Wave equation ──► Plane waves, speed of sound, wavelength
      │
      ├──► Impedance mismatch ──► Reflection / Transmission
      │
      ├──► Huygens principle ──► Diffraction (bending around obstacles)
      │
      ├──► Multiple reflections ──► Standing waves, resonance modes
      │
      └──► Superposition ──► Interference (constructive / destructive)
```

---

## The Wave Equation

The derivation path (Newton's second law + mass conservation for a fluid element → linearize → wave equation) is standard. The acoustic-specific value lies in what follows: impedance mismatch at material interfaces, reflection/transmission coefficients, and standing wave boundary conditions.

```
ACOUSTIC WAVE EQUATION (linear, lossless):

∂²p/∂t² = c² · ∇²p

where p(x,t) = acoustic pressure (Pa)
      c = √(γP₀/ρ₀) = speed of sound in the medium

In 1D (plane wave):  ∂²p/∂x² = (1/c²)·∂²p/∂t²

GENERAL SOLUTION (d'Alembert):
p(x,t) = f₊(t - x/c) + f₋(t + x/c)

f₊ = wave traveling in +x direction at speed c
f₋ = wave traveling in -x direction at speed c
```

**For a harmonic (single-frequency) plane wave**:
```
p(x,t) = P₀ · cos(ωt - kx + φ)

ω = 2πf    (angular frequency, rad/s)
k = ω/c = 2π/λ   (wavenumber, rad/m)
λ = c/f    (wavelength)
```

---

## Speed of Sound in Various Media

```
SPEED OF SOUND c

Medium           c (m/s)       ρ (kg/m³)    Z = ρc (MRayl)
────────────────────────────────────────────────────────────
Air (0°C)        331           1.29         0.000428
Air (20°C)       343           1.21         0.000415
Air (100°C)      387           0.95         0.000368
CO₂ (0°C)        259           1.98         0.000513
Fresh water      1480          998          1.48
Sea water        ~1520         1025         ~1.56
Steel            5100          7800         39.8
Glass            5200          2500         13.0
Concrete         3400          2300         7.8
Wood (pine)      3300          600          1.98
Human tissue     ~1540         ~1060        ~1.63
Rubber           ~1500         ~1100        ~1.65
────────────────────────────────────────────────────────────

TEMPERATURE DEPENDENCE IN AIR:
c(T) ≈ 331 + 0.6·T °C   (linear approximation)
c = 331·√(T/273)  (exact, T in Kelvin)

WHY VARIES BY MEDIUM:
c = √(B/ρ)  where B = bulk modulus (stiffness), ρ = density
Stiff, light materials → fast (steel, aluminum)
Dense, soft materials → slow (rubber, foam)
```

---

## Acoustic Impedance and Wave Behavior at Boundaries

Specific acoustic impedance Z = ρ·c. When a wave hits an interface between two media:

```
NORMAL INCIDENCE AT INTERFACE

Medium 1 (Z₁)              Medium 2 (Z₂)
─────────────────────────│──────────────────────
                         │
   Incident ──────────►  │  ──────────► Transmitted
                         │
   Reflected ◄────────   │

REFLECTION COEFFICIENT (pressure):
R = (Z₂ - Z₁) / (Z₂ + Z₁)   [-1, +1]

TRANSMISSION COEFFICIENT (pressure):
T = 2Z₂ / (Z₂ + Z₁)          [0, 2]

POWER REFLECTION:
Rₚ = ((Z₂-Z₁)/(Z₂+Z₁))²

POWER TRANSMISSION:
Tₚ = 4Z₁Z₂/(Z₁+Z₂)²   = 1 - Rₚ   ✓

EXAMPLES:
Air (0.000415) → Water (1.48 MRayl):
Rₚ = ((1.48-0.000415)/(1.48+0.000415))² ≈ 0.999   (99.9% reflected!)

Air (0.000415) → Glass (13 MRayl):
Rₚ ≈ 0.9997   (99.97% reflected)
→ Double-pane glass achieves isolation by air gap, not glass mass at these levels

Air → Air (no interface): R = 0, T = 1 (no reflection, perfect transmission)
```

**Oblique incidence**: Snell's law applies — sin(θ₂)/c₂ = sin(θ₁)/c₁.
Beyond the critical angle (when c₂ > c₁), total internal reflection occurs.

---

## Diffraction

Sound bends around obstacles when wavelength λ is comparable to or larger than obstacle size.

```
DIFFRACTION PARAMETER: ka = 2πa/λ = (circumference)/(wavelength)

ka << 1  → obstacle much smaller than wavelength → sound goes around freely
ka >> 1  → obstacle much larger than wavelength → geometric shadow (like light)
ka ≈ 1   → transition region, complex pattern

EXAMPLES AT 1 kHz IN AIR (λ = 0.34 m):
Person (shoulder width ~0.5 m): ka ≈ 9 → noticeable shadow
Doorway (0.9 m wide): ka ≈ 17 → directional, but some diffraction
Pencil (1 cm diameter): ka ≈ 0.2 → almost no shadow

WHY BASS "GOES THROUGH WALLS":
100 Hz: λ = 3.4 m — longer than most building features
Geometric acoustics fails → energy diffracts around/through
Also: walls absorb less at low frequencies (mass law)
```

**Huygens principle**: Every point on a wavefront acts as a point source of secondary waves.
The diffracted wave field is the superposition of all secondary waves.
This explains sound wrapping around corners and through gaps.

---

## Standing Waves and Resonance

When waves reflect and interfere with themselves, standing waves form.

```
1D STANDING WAVE (tube/room dimension L):

Forward:  p₊ = P₀·cos(ωt - kx)
Backward: p₋ = P₀·cos(ωt + kx)   (from rigid wall reflection, R=1)
Sum:      p  = 2P₀·cos(kx)·cos(ωt)

NODES: zeros of cos(kx) → no pressure oscillation
ANTINODES: maxima of cos(kx) → maximum pressure oscillation

RESONANT FREQUENCIES for room dimension L:
• Both ends rigid (pressure antinodes):
  f_n = n·c/(2L)    n = 1, 2, 3, ...

• One end rigid, one end open (one node, one antinode):
  f_n = (2n-1)·c/(4L)    n = 1, 2, 3, ...

ROOM MODES (3D box, dimensions L_x, L_y, L_z):
f_{nx,ny,nz} = (c/2)·√((nx/Lx)² + (ny/Ly)² + (nz/Lz)²)

Axial modes: one dimension (nx, 0, 0) — strongest
Tangential modes: two dimensions (nx, ny, 0) — moderate
Oblique modes: all three (nx, ny, nz) — weaker
```

**Modal density and Schroeder frequency** (preview of room acoustics):
Below the Schroeder frequency, modes are discrete and audible as coloration.
Above it, modes overlap and behavior becomes diffuse (statistical).

---

## Spherical Wave Divergence

A point source radiates spherically in free field:

```
SPHERICAL WAVE:
p(r,t) = (A/r) · cos(ωt - kr)

Amplitude falls as 1/r → intensity falls as 1/r² (inverse square law)
SPL decreases 6 dB per doubling of distance

DIRECTIVITY:
Real sources are not omnidirectional.
Directivity index (DI) = 10·log₁₀(Q)
where Q = directivity factor (Q=1 omnidirectional, Q=2 halfspace/flush mount)

NEAR FIELD vs FAR FIELD:
Near field (r < λ/2π): reactive field, pressure and velocity out of phase
Far field (r > λ/2π): propagating wave, well-behaved 1/r decay
```

---

## Decision Cheat Sheet

| Question | Key Physics |
|----------|-------------|
| Why can I hear around a corner? | Diffraction (ka < 1 at low frequencies) |
| Why does sound reflect off walls? | Impedance mismatch (ρ_wall·c_wall >> ρ_air·c_air) |
| Why do rooms have low-frequency peaks? | Standing wave resonances (modes) |
| Speed of sound at 35°C? | c ≈ 331 + 0.6×35 = 352 m/s |
| How deep can bass penetrate a wall? | Mass law and diffraction (long wavelength) |
| Why does water/glass block ultrasound poorly? | Impedance mismatch between transducer and water is low |
| Why does sound focus in SOFAR channel? | Vertical sound speed minimum creates waveguide |

---

## Common Confusion Points

**Particle velocity vs wave velocity**: Particles in a sound wave oscillate back and forth
with velocity u (small, ≤ mm/s for normal sound). The wave pattern propagates at c (~343 m/s).
These are completely different velocities.

**Sound is not transverse**: Unlike EM waves or string waves, sound is longitudinal —
particle displacement is parallel to propagation direction. There are no "acoustic polarizations."

**Impedance mismatch works both ways**: Sound hitting air from glass is also 99.97% reflected.
This is why underwater noise barely escapes into air — it reflects back into the water.

**Standing waves ≠ resonance in the damped sense**: Standing waves exist even without losses.
In a real room, they're damped (finite RT60). The "resonance" is more like poles in a filter —
excited strongly at modal frequencies, decay with room absorption.
