# Galactic Structure and Dynamics
## Milky Way Anatomy, Spiral Arms, Dark Matter, Stellar Dynamics, Galaxy Formation

---

## 1. The Full Picture — Milky Way Architecture

```
  MILKY WAY CROSS-SECTION (edge-on, not to scale)

                      ┌─────────────────────────────────────┐
                      │         DARK MATTER HALO             │
                      │    (~200 kpc virial radius)          │
    ╔══════════════════╪══════════════════════════════════════╪═════════╗
    ║  Stellar Halo    │                                      │         ║
    ║  (old, metal-   │         ╔══════════════╗             │         ║
    ║   poor, streams) │  ·  ·  ║    THICK     ║  ·  ·  ·   │         ║
    ║  [Fe/H] < −1    │   ·    ║  DISK         ║     ·      │         ║
    ║  h_z ~ 3 kpc    │        ║  h_z ~ 900pc  ║            │         ║
    ╠══════════════════╪════════╬══════════════╬════════════╪══════════╣
    ║  GAS + DUST     ▓▓▓▓▓▓▓▓▓║   THIN DISK  ║▓▓▓▓▓▓▓▓▓▓▓▓▓  WARP  ║
    ║  young stars    ▓▓▓▓▓▓▓▓▓║  h_z ~300 pc  ║▓▓▓▓▓▓▓▓▓▓▓▓▓         ║
    ╠══════════════════╪════════╬══════════════╬════════════╪══════════╣
    ║  [disk midplane: z=0]     ║              ║                       ║
    ║                  │    ╔══╩══════════════╩══╗          │         ║
    ║                  │    ║   BULGE / BAR       ║          │         ║
    ║                  │    ║  triaxial, ~3.5 kpc ║          │         ║
    ║                  │    ║  bar angle ~27°      ║          │         ║
    ║                  │    ║  [CMZ: inner ~200pc] ║          │         ║
    ║                  │    ║  [Sgr A* at center]  ║          │         ║
    ║                  │    ╚════════════════════╝          │         ║
    ╚══════════════════╧═══════════════════════════════════════════════╝

  KEY SCALES:
    R_d (thin disk scale length) ~ 3.5 kpc
    h_z (thin disk scale height) ~ 300 pc
    h_z (thick disk)             ~ 900 pc
    Bulge/bar half-length        ~ 3.5 kpc
    Dark matter halo r_vir       ~ 200 kpc
    R☉ (Sun–GC distance)        ~ 8.178 kpc  [GRAVITY 2019]
    z☉ (Sun above midplane)     ~ 17 pc
```

```
  MILKY WAY FACE-ON (schematic, looking down from north Galactic pole)

                                N
                                |
                          ╭─────┴──────╮
                   ╭─────╮│  Perseus   │╭─────╮
                ╭──╯  ╭──╯│   Arm      │╰──╮  ╰──╮
              ╭─╯   ╭─╯   ╰────────────╯   ╰─╮   ╰─╮
            ─────────────────────────────────────────────── Cygnus
           |  Norma  |    ╔══════════════╗   |  Outer |   ←  GC dir
           |  Arm    |    ║     BAR      ║   |  Arm   |
           |         |    ║   ~3.5 kpc   ║   |        |
           |         |    ║   ↗ 27° from ║   |        |
            ─────────────╫──Sun-GC line──╫───────────────
                          ║     Sgr A*   ║
                          ╚══════════════╝
              ╰─╮   ╰─╮   ╭────────────╮   ╭─╯   ╭─╯
                ╰──╮  ╰──╮│Carina-Sag  │╭──╯  ╭──╯
                   ╰─────╯│   Arm      │╰─────╯
                          ╰─────┬──────╯
                                S

  ★ = Sun (R☉ ~ 8.178 kpc)   We are in the LOCAL (Orion) SPUR
  Orion Spur is an inter-arm bridge between Perseus and Carina-Sag arms
  NOT a major spiral arm

  4 MAJOR ARMS: Norma, Crux-Centaurus, Carina-Sagittarius, Perseus
  Pitch angle i ~ 12–13° (logarithmic spiral)
  Arm equation: ln(R/R₀) = −(θ − θ₀) tan(i)
```

---

## 2. Milky Way Components — Numerical Reference

```
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ COMPONENT         │ MASS          │ SCALE HEIGHT │ [Fe/H]   │ AGE       │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ Thin disk         │ ~5×10¹⁰ M☉   │ ~300 pc      │ > −1     │ 0–10 Gyr │
  │ Thick disk        │ ~1×10¹⁰ M☉   │ ~900 pc      │ −0.5 to−1│ 8–12 Gyr │
  │ Bulge/Bar         │ ~1×10¹⁰ M☉   │ ~700 pc      │ bimodal  │ 8–12 Gyr │
  │ Stellar halo      │ ~3×10⁸ M☉    │ R^−3.5 (NFW) │ < −1     │ 10–13 Gyr│
  │ Dark matter halo  │ ~10¹² M☉     │ NFW: r_s~20kpc│ N/A     │ —        │
  │ Total MW (virial) │ ~1.3×10¹² M☉ │               │          │          │
  └─────────────────────────────────────────────────────────────────────────┘
  [Watkins et al. 2019, ApJ 873, 118 — Gaia + HST proper motions of GCs]

  CIRCULAR VELOCITY (local):   v_c(R☉) ~ 220–240 km/s
  ESCAPE VELOCITY:             v_esc(R☉) ~ 550 km/s  [Piffl 2014]
  ORBITAL PERIOD (Sun):        T☉ = 2πR☉/v_c ~ 225 Myr  ("Galactic year")
```

### 2.1 Thin Disk — Active Star-Forming Layer

The thin disk is the site of current star formation. Its vertical density profile is approximately:

```
  Vertical (z) profile — sech² law:

  ρ(R, z) = ρ₀(R) × sech²(z / 2h_z)

  For large |z|, sech² → 2 exp(−|z|/h_z):  exponential falloff

  Radial profile — exponential:
  Σ(R) = Σ₀ exp(−R/R_d)     [surface mass density]

  Combined:
  ρ(R, z) = (Σ₀/2h_z) exp(−R/R_d) × sech²(z/2h_z)

  h_z ~ 300 pc (young stars/gas even thinner: ~100 pc for HI)
  R_d ~ 3.5 kpc
  Σ₀(R☉) ~ 50–60 M☉/pc²  (stars + gas; gas ~ 10 M☉/pc²)
```

The thin disk scale height is supported against gravity by a combination of thermal pressure (gas), turbulence, and the velocity dispersion of stellar populations. The disk **flares** outward (h_z increases with R) because the gravitational restoring force weakens at large R. The outer disk (~R > 14 kpc) also shows a coherent warp — the disk midplane deviates from z=0, induced primarily by LMC infall torque.

### 2.2 Thick Disk — Ancient Relic

The thick disk is structurally and chemically distinct: older, hotter (velocity dispersion σ_z ~ 40 km/s vs ~25 km/s for thin disk), and [α/Fe]-enhanced at fixed [Fe/H], indicating rapid enrichment before Type Ia SN iron contribution. Origin debate: (1) early gas-rich mergers that dynamically heated a proto-disk; (2) in-situ formation at high redshift in a turbulent, thick gas layer; (3) radial migration via churning (Sellwood & Binney) — stars migrate outward from inner disk. APOGEE survey data support scenario (1)+(2) hybrid: the "high-α" sequence is old and kinematically hot from its formation epoch.

### 2.3 Bulge and Bar

```
  BAR MORPHOLOGY:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Triaxial bar: axis ratios roughly 1 : 0.4 : 0.3                │
  │  Half-length: ~3.5 kpc (to "bar ends")                          │
  │  Bar angle: ~27° between bar major axis and Sun–GC line         │
  │  Pattern speed Ω_bar ~ 40–45 km/s/kpc (controversial)         │
  │                                                                 │
  │  "Boxy/Peanut" (B/P) morphology in central ~2.5 kpc:          │
  │  Viewed edge-on, the bulge has an X-shape                       │
  │  Origin: vertical resonance — bar undergoes BUCKLING instability│
  │  When bar amplitude exceeds threshold, vertical resonance       │
  │  (2:1 vertical frequency to bar tumbling) heats stars into      │
  │  off-plane banana-shaped orbits → peanut morphology             │
  └─────────────────────────────────────────────────────────────────┘
  This is NOT a classical bulge (slowly built by mergers).
  It's a PSEUDO-BULGE — the buckled inner bar.
  Distinguisher: pseudo-bulge has Sérsic index n < 2, disk-like
  kinematics, ongoing SF; classical bulge has n ~ 4, hot kinematics.
```

The bar is the dominant structure inside corotation. Stars near corotation tend to get trapped into orbital families that reinforce the bar (x1 orbits — elongated orbits aligned with the bar). The bar connects to the spiral arms at its ends, feeding gas inward along it.

---

## 3. Spiral Structure — Density Waves vs Material Arms

### 3.1 The Winding Problem

Differential rotation is the key constraint. The angular velocity of circular orbits:

```
  Ω(R) = v_c(R) / R

  For flat rotation curve (v_c = const):
    Ω(R) ∝ 1/R  — angular velocity decreases with R

  A material arm (stars physically moving together) wound up
  after t years:
    Number of wraps ~ Δθ/(2π) = [Ω(R_inner) − Ω(R_outer)] t / 2π

  With v_c ~ 220 km/s, between R=4 and R=8 kpc:
    Δθ ~ (220/4 − 220/8) km/s/kpc × 2×10¹⁰ yr
    ~ 27.5 km/s/kpc × 2×10¹⁰ yr × (1 kpc / 3.09×10¹⁶ km)
    ~ 27.5 × 2×10¹⁰ × 3.24×10⁻¹⁴  rad
    ~ ~18 radians ~ 3 full wraps in 2 Gyr

  Result: material arms would wind into a featureless disk in ~2 Gyr.
  Observed pitch angles (12–13°) persist for ~10 Gyr. CONTRADICTION.
```

### 3.2 Lin-Shu Density Wave Theory

Proposed by C.C. Lin and Frank Shu (1964): spiral arms are **density waves** — quasi-stationary patterns that rotate rigidly at angular velocity Ω_p (pattern speed), independent of the stars and gas:

```
  DENSITY WAVE PICTURE:
  ┌──────────────────────────────────────────────────────────────────┐
  │                                                                  │
  │   Stars/gas orbit at local Ω(R).                                 │
  │   The density wave pattern rotates at Ω_p ~ 25–30 km/s/kpc.   │
  │                                                                  │
  │   Stars inside corotation (R < R_CR):                            │
  │     Ω(R) > Ω_p → stars overtake the pattern                   │
  │     Stars slow down, pile up, then pass through                  │
  │     Net effect: enhanced density in the arm → SF triggered       │
  │                                                                  │
  │   Stars outside corotation (R > R_CR):                           │
  │     Ω(R) < Ω_p → pattern overtakes stars                      │
  │                                                                  │
  │   COROTATION RADIUS: Ω(R_CR) = Ω_p                            │
  │   For Ω_p ~ 28 km/s/kpc, v_c ~ 220 km/s:                      │
  │   R_CR = v_c/Ω_p ~ 220/28 ~ 7.9 kpc  ≈ R☉                    │
  └──────────────────────────────────────────────────────────────────┘

  Analogy: traffic jam on a highway. Individual cars move through
  the jam (the jam is the wave). Cars ≡ stars; jam ≡ density arm.
```

The density wave compresses gas as it passes through, triggering the Jeans collapse that produces the OB associations and HII regions we observe as spiral tracers. Dust lanes appear on the leading edge of the arm (upstream of the compression for R < R_CR).

### 3.3 Lindblad Resonances

The wave-orbit interaction has resonances when the orbital response frequency matches the forcing frequency:

```
  EPICYCLIC FREQUENCY κ(R) [see Section 5.3]:
    κ² = R dΩ²/dR + 4Ω²   [general]
    κ = √2 Ω               [flat rotation curve: v_c = const]

  RESONANCE CONDITIONS for m-armed spiral:
  ┌──────────────────────────────────────────────────────────┐
  │  Inner Lindblad Resonance (ILR): Ω − κ/m = Ω_p        │
  │  Outer Lindblad Resonance (OLR): Ω + κ/m = Ω_p        │
  │  Corotation (CR):                Ω       = Ω_p        │
  └──────────────────────────────────────────────────────────┘

  For m=2 (two-armed spiral), MW parameters:
    ILR at R ~ 3–4 kpc
    CR  at R ~ 7.9 kpc
    OLR at R ~ 11–12 kpc

  Waves are TRAPPED between ILR and OLR.
  Wave action is absorbed at Lindblad resonances → damping → wave
  must be continuously regenerated or... the steady-state is wrong.

  DIFFICULTY: True steady-state density waves require maintenance
  mechanism (swing amplification + feedback loop, or mode excitation
  by bar). MW is better described as intermediate between grand-design
  and flocculent — quasi-stationary, not perfectly periodic.
```

### 3.4 Galaxy Morphological Types

```
  SPIRAL MORPHOLOGY CLASSIFICATION:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Grand Design (M51, M81)                                         │
  │   Two dominant, well-defined, symmetric arms                    │
  │   Often driven by companion interaction or strong density wave  │
  │   Strong coherent CO and HI arm structures                      │
  ├─────────────────────────────────────────────────────────────────┤
  │ Flocculent (NGC 2841)                                           │
  │   Multiple short, patchy arm segments                           │
  │   No coherent global density wave pattern                       │
  │   Stochastic self-propagating SF (SSPSF) model:                │
  │     OB stars → SNe → expand HII region → compress surrounding  │
  │     GMC → trigger next generation → propagating SF             │
  ├─────────────────────────────────────────────────────────────────┤
  │ Multi-armed / Intermediate (Milky Way)                          │
  │   4 major arms + local spur + flocculent structure              │
  │   Mix of density wave (global 4-arm pattern) + SSPSF            │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 4. Galactic Rotation Curve and the Dark Matter Halo

### 4.1 Force Balance and the Rotation Curve

For a test mass in circular orbit in an axisymmetric potential Φ(R, z):

```
  CIRCULAR VELOCITY from radial force balance:

  v_c²/R = |∂Φ/∂R|_{z=0} = F_R(R)

  For spherical mass distribution:
    v_c²(R) = G M(<R) / R

  Contributions add in quadrature [roughly; actual potential decomposition
  is more subtle — you add forces, not velocities]:
    F_R,total = F_R,disk + F_R,bulge + F_R,halo + F_R,gas

  Observed: v_c(R) ≈ 220–240 km/s, FLAT from ~3 kpc to ~25 kpc
            (Sofue 2012, Reid et al. 2014)

  Expected from luminous matter alone:
    Beyond bulge, disk surface density Σ ∝ exp(−R/R_d)
    Disk contribution: v_disk(R) peaks at R ~ 2.2 R_d ~ 7.7 kpc
    then FALLS as exp(−R/2R_d) × Bessel functions → v_disk → 0
    Bulge: v_bulge ~ √(GM_bulge/R) → 0 rapidly beyond ~3 kpc

  MASS DEFICIT at large R: ~70% of gravitational force at R=15 kpc
  must come from non-luminous matter — DARK MATTER HALO.
```

### 4.2 NFW Profile — The CDM Halo

Navarro, Frenk & White (1996, 1997) showed N-body CDM halos converge to a universal profile:

```
  NFW DENSITY PROFILE:
  ┌─────────────────────────────────────────────────────────────────┐
  │  ρ_NFW(r) = ρ_s / [(r/r_s)(1 + r/r_s)²]                      │
  │                                                                 │
  │  r_s   = scale radius (~20 kpc for MW)                          │
  │  ρ_s   = characteristic density (set by halo concentration c)   │
  │                                                                 │
  │  Asymptotic behavior:                                           │
  │    r << r_s:  ρ ∝ r⁻¹   (cuspy inner profile)                 │
  │    r >> r_s:  ρ ∝ r⁻³   (rapid outer fall-off)                │
  └─────────────────────────────────────────────────────────────────┘

  HALO CONCENTRATION:  c = r_vir / r_s
  For MW: r_vir ~ 200 kpc, r_s ~ 20 kpc → c ~ 10 (typical for MW mass)

  ENCLOSED MASS:
  M_NFW(<r) = 4π ρ_s r_s³ [ln(1 + r/r_s) − (r/r_s)/(1 + r/r_s)]

  NFW CIRCULAR VELOCITY PROFILE:
  v_c²(r) = G M_NFW(<r) / r
           = 4πG ρ_s r_s³/r × [ln(1 + r/r_s) − (r/r_s)/(1+r/r_s)]

  v_c peaks at r_max ~ 2.16 r_s, then slowly declines.
  For MW r_s~20 kpc: peak at ~43 kpc, then v_c ∝ r^{-1/2} at large r.
  At R☉=8.178 kpc << r_s: NFW curve is still rising — roughly flat.
  This correctly reproduces the observed flat rotation curve in the
  observed range.

  EINASTO PROFILE (alternative, softer cusp):
  ρ_E(r) = ρ_s exp{−(2/α)[(r/r_s)^α − 1]}
  α ~ 0.16 for MW-mass halos; inner slope softer → better for
  γ-ray DM signals (less cusp divergence).

  CUSP-CORE PROBLEM:
  NFW predicts ρ ∝ r⁻¹ (cusp); dwarf galaxy observations prefer
  ρ = const (core). Resolution: baryonic feedback (SN-driven gas
  outflows) repeatedly kicks dark matter, heating the inner cusp
  into a core — plausible for low-mass dwarfs, not massive galaxies.
```

### 4.3 Oort Constants and Local Kinematics

The local rotation curve is characterized by two constants from Oort (1927):

```
  OORT CONSTANTS (defined at R = R☉):

  A ≡ −½ R dΩ/dR |_☉ = ½(v_c/R − dv_c/dR)|_☉    [shear rate]
  B ≡   ½ R dΩ/dR |_☉ + Ω = −½(v_c/R + dv_c/dR)|_☉ − Ω/2...

  Precise definitions:
  ┌──────────────────────────────────────────────────────────────┐
  │  A = ½ [v_c/R − dv_c/dR]_{R☉}   ~ +15.3 km/s/kpc          │
  │  B = −½ [v_c/R + dv_c/dR]_{R☉}  ~ −11.9 km/s/kpc          │
  └──────────────────────────────────────────────────────────────┘
  [Bovy 2017, from APOGEE+Gaia]

  PHYSICAL MEANINGS:
    A: measures shear. Rate at which nearby stars pull apart
       along the Galactic plane. A > 0 means stars inside R☉
       orbit faster (recede in the direction of Galactic rotation).
    B: measures vorticity. B < 0 because disk rotation is
       retrograde (clockwise viewed from north) relative to usual
       coordinate sense.

  DERIVED QUANTITIES:
    Angular velocity at Sun:  Ω☉ = A − B ~ 27.2 km/s/kpc
    Circular speed at Sun:    v_c(R☉) = Ω☉ × R☉ = 27.2 × 8.178 ~ 222 km/s
    Oort's A − B = Ω☉ (total angular speed)
    A + B = −dv_c/dR |_☉  (negative for rising curve → A+B < 0 outside peak)

  EPICYCLIC FREQUENCY:
    κ² = −4B(A − B) = 4Ω☉(A − B) + 4B²...

    More carefully: κ² = R dΩ²/dR + 4Ω²
    At R☉: κ² = −4B(A − B)
    κ = √[−4B(A−B)] = √[−4(−11.9)(27.2)] = √1295 ~ 36 km/s/kpc

    For flat rotation curve: κ = √2 Ω☉ ~ √2 × 27.2 ~ 38.5 km/s/kpc
    Ratio κ/Ω ~ 1.36 (close to √2 ~ 1.41 → nearly flat at R☉)

  VERTICAL FREQUENCY ν:
    ν² = 4πGρ_midplane + 2(A²−B²) [dominates at z~0]
    ν ~ 70–90 km/s/kpc  (ν > κ > Ω hierarchy)
    → Stars oscillate vertically faster than radially, faster than azimuthally

  OBSERVATIONAL ACCESS (Oort 1927 method):
    Radial velocity of nearby star at angle l from GC:
    v_r = A d sin(2l)   [radial component]
    Proper motion:  μ = A cos(2l) + B   [both A and B visible from μ]
    Works for stars within ~1 kpc (linear approximation valid).
```

---

## 5. Stellar Populations and Chemical Evolution

### 5.1 Population Classification

```
  STELLAR POPULATION TAXONOMY:
  ┌───────────────────────────────────────────────────────────────────────┐
  │ Population  │ Age        │ [Fe/H]       │ Location        │ [α/Fe]    │
  ├───────────────────────────────────────────────────────────────────────┤
  │ Pop I       │ 0–8 Gyr   │ −1 to +0.5   │ thin disk, arms │ low      │
  │ Pop II      │ 8–13 Gyr  │ −1 to −5     │ thick disk, halo│ high     │
  │ Pop III     │ ~200 Myr  │ 0 (primordial)│ early universe  │ unknown  │
  │             │ after BB   │              │ (none observed) │          │
  └───────────────────────────────────────────────────────────────────────┘
  [α-elements: O, Mg, Si, Ca, Ti — produced in core-collapse SNe (Type II)]

  KEY ABUNDANCE DIAGNOSTIC:
    [Fe/H] = log₁₀(N_Fe/N_H)_star − log₁₀(N_Fe/N_H)_Sun
    [α/Fe] = log₁₀(N_α/N_Fe)_star − log₁₀(N_α/N_Fe)_Sun
```

### 5.2 The [α/Fe] vs [Fe/H] Diagram — Reading Star Formation History

```
  [α/Fe]
    |
  +0.4 ─┬──────────────────────
        │  ╲  HIGH-α SEQUENCE
  +0.3  │   ╲  (thick disk +
        │    ╲   inner halo)        ← rapid SF, α enhanced:
  +0.2  │     ╲                      CCSN enrich before
        │      ╲_______________       SNe Ia contribute
  +0.1  │              ╲
        │          LOW-α ╲
  0.0 ──│          SEQUENCE╲___     ← slower SF, Ia catch up
        │          (thin disk) ─────
 -0.1  ─┴──────────────────────────────
       -2.5  -2.0  -1.5  -1.0  -0.5   0.0  +0.3
                                             [Fe/H]

  THE "ALPHA KNEE" at [Fe/H] ~ −1:
  ┌───────────────────────────────────────────────────────────────────┐
  │  CCSN (core-collapse SNe, M > 8 M☉):                            │
  │    Timescale: ~10 Myr after SF episode begins                    │
  │    Products: α-elements (O, Mg, Si, Ca, Ti) + some Fe           │
  │    Effect: drives [α/Fe] HIGH, [Fe/H] rising                    │
  │                                                                   │
  │  SNe Ia (thermonuclear, WD+companion):                           │
  │    Timescale: ~1 Gyr delay (DTD peaks at ~1 Gyr, tail to ~10 Gyr)│
  │    Products: Fe-peak elements (Fe, Ni, Co)                       │
  │    Effect: when they "turn on," [Fe/H] rises faster than [α/Fe] │
  │            → [α/Fe] drops → the knee                            │
  │                                                                   │
  │  READING HISTORY:                                                 │
  │  High [α/Fe] at given [Fe/H] → fast SF (no time for Ia delay)   │
  │  Low [α/Fe] at given [Fe/H] → slow SF or quenching+resumption   │
  │  Two distinct sequences in MW → thick+thin disk had DISTINCT SF  │
  └───────────────────────────────────────────────────────────────────┘
```

### 5.3 Closed-Box Chemical Evolution Model

The simplest model: isolated system with gas, stars, no inflow/outflow.

```
  VARIABLES:
    M_g(t) = gas mass at time t
    M_s(t) = stellar mass at time t
    Z(t) = metallicity (mass fraction of metals in gas)
    p = yield (fraction of stellar mass returned as metals per unit
        mass locked into long-lived stars — typically p ~ 0.02)

  MASS CONSERVATION:
    M_g + M_s = M_total = const
    d M_g / dt = −(1−R) ψ   [R = returned fraction, ψ = SFR]
    where (1−R)ψ is net mass locked up (surviving stars)

  METAL EVOLUTION:
    d(Z M_g)/dt = −Z(1−R)ψ + p ψ   [metals lost to SF + metals produced]

    Simplify: Z dM_g + M_g dZ = −Z(1−R)ψ dt + p ψ dt
    Using d M_g = −(1−R)ψ dt:
    M_g dZ = −Z d M_g − Z d M_g + p × (−d M_g/(1−R)) × (1−R) + ...

    CLEAN FORM (Pagel 1997):
    ┌────────────────────────────────────────────────────────┐
    │  dZ/d(−M_g) = [p − Z(1−R)] / (1−R) M_g × M_g        │
    │                                                        │
    │  Simple case: dZ / d ln(M_g) = −p  (no recycling)    │
    │  → Z(M_g) = p × ln(M_total / M_g)                    │
    │  → Z(μ) = p × ln(1/μ)   where μ = M_g/M_total = gas │
    │                          fraction                      │
    └────────────────────────────────────────────────────────┘

  PREDICTION:
    Stars forming when gas fraction = μ have metallicity Z = p ln(1/μ)
    Low-Z (metal-poor) stars should be abundant (formed early, μ ~ 1)
    → Distribution of stellar metallicities:
      dN/dZ = M_total/p × exp(−Z/p)   [exponential, many metal-poor stars]
```

### 5.4 The G-Dwarf Problem

The closed-box model predicts too many metal-poor ([Fe/H] < −1) G dwarfs in the solar neighborhood. Observed: sharply fewer metal-poor disk dwarfs than predicted.

```
  RESOLUTION: Infall (Lynden-Bell 1975, Pagel 1989):
  ┌──────────────────────────────────────────────────────────────────┐
  │  The disk was NOT pre-enriched. It formed by INFALL of           │
  │  metal-poor (primordial) gas over time.                          │
  │                                                                  │
  │  When pristine gas falls in, it DILUTES the metallicity.         │
  │  Early on, infalling gas keeps Z low → few stars form at         │
  │  low Z because the infalling gas increases the denominator       │
  │  (gas mass) faster than SF can reduce it.                        │
  │                                                                  │
  │  Infall model metallicity distribution: suppresses the           │
  │  low-[Fe/H] tail → matches observations.                         │
  │                                                                  │
  │  Physical: MW disk built up by cosmological accretion,           │
  │  preferentially from metal-poor CGM/satellites.                  │
  └──────────────────────────────────────────────────────────────────┘
```

### 5.5 Metallicity Gradients

```
  RADIAL GRADIENT (thin disk Cepheids, HII regions, open clusters):
    dZ/dR ~ −0.06 dex/kpc (consistent across tracers)
    [Fe/H] drops from ~+0.3 at R~4 kpc to ~−0.3 at R~14 kpc

  ORIGIN: inside-out disk formation. Inner disk formed earlier, had
  more SF cycles, more enrichment. Outer disk still accreting.
  Gas infall rate and SF efficiency both decrease outward.

  VERTICAL GRADIENT (thin disk):
    dZ/dz ~ −0.1 to −0.2 dex/kpc (smaller, less certain)
    Metal-rich stars concentrated near midplane.

  AGE-METALLICITY RELATION (AMR):
    Weak correlation in the field (large scatter at any age).
    Tight in OPEN CLUSTERS (mono-age, mono-metallicity populations).
    Field scatter: radial migration churns stars from different R
    (and hence different initial Z) to solar neighborhood.
```

---

## 6. The Galactic Center

### 6.1 Sgr A* — The Supermassive Black Hole

```
  SGR A* FUNDAMENTAL PARAMETERS:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Mass: M_• = 4.154 ± 0.014 × 10⁶ M☉                          │
  │  [GRAVITY Collaboration, Abuter et al. 2019, A&A 625, L10]    │
  │                                                                 │
  │  Schwarzschild radius:                                          │
  │  r_S = 2GM/c² = 2 × 6.67×10⁻⁸ × 4.15×10⁶ × 2×10³³           │
  │           / (3×10¹⁰)²                                           │
  │       ~ 1.24×10¹² cm ~ 0.083 AU                               │
  │                                                                 │
  │  Angular size: θ = r_S / D = 0.083 AU / 8.178 kpc ~ 10 μas    │
  │  EHT resolution: ~20 μas at 230 GHz → Sgr A* marginally         │
  │  resolvable (EHT 2022 image published)                          │
  │                                                                 │
  │  Luminosity: L_Sgr A* ~ 10³⁶ erg/s ~ 300 L☉                  │
  │  Eddington limit: L_Edd = 4πGMc/κ ~ 5×10⁴⁴ erg/s             │
  │  → Sgr A* radiates at ~10⁻⁸ of Eddington (DORMANT GALACTIC CENTER) │
  └─────────────────────────────────────────────────────────────────┘
```

### 6.2 S-Star Cluster and GR Tests

The most direct BH mass determination comes from stellar orbits in the S-star cluster:

```
  S2/S0-2 ORBIT:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Period:       P = 16.0 yr                                      │
  │  Semi-major axis: a = 1025 AU = 0.005 pc                        │
  │  Eccentricity: e = 0.884 (highly elliptical)                    │
  │  Pericenter:   r_p = a(1−e) = 119 AU = 1430 r_S               │
  │                                                                 │
  │  KEPLER → BH MASS:                                              │
  │  M = 4π²a³/(GP²) = 4π²(1025×1.496×10¹³)³/(6.67×10⁻⁸×(16×3.15×10⁷)²) │
  │  ~ 4.15×10⁶ M☉                                                │
  │                                                                 │
  │  GR EFFECTS DETECTED (GRAVITY Collaboration 2020):              │
  │  1. Gravitational redshift at pericenter:                       │
  │     Δz = Δv_grav/c = GM/(r_p c²) − v_p²/2c²                   │
  │     First confirmed in S2 pericenter passage 2018               │
  │  2. Schwarzschild precession of orbital periapsis:              │
  │     Δφ = 6πGM/(ac²(1−e²)) per orbit                           │
  │         ~ 12' per orbit for S2 → detected 2020                │
  │  No evidence of extended mass (confirms BH, not compact cluster)│
  └─────────────────────────────────────────────────────────────────┘
```

### 6.3 Fermi Bubbles

```
  FERMI BUBBLE MORPHOLOGY:
  ┌─────────────────────────────────────────────────────────────────────┐
  │                                                                     │
  │        ╭───────────────╮   north bubble                             │
  │       ╭╯               ╰╮  ~10 kpc tall                           │
  │       │  uniform hard   │  (= 10 kpc above GC plane)              │
  │       │  γ-ray spectrum │  γ-ray: E > 1 GeV                       │
  │       │  E^−2 power law │  microwave excess (WMAP "haze"):        │
  │       │                 │  ~ 1–3 GHz synchrotron from             │
  │       ╰╮               ╭╯  high-energy electrons                  │
  │    ────╰───────────────╯──────────── Galactic plane ──────        │
  │        ╭───────────────╮   south bubble                           │
  │       ╭╯               ╰╮  symmetric counterpart                  │
  │       │  ~10 kpc tall   │                                         │
  │       ╰╮               ╭╯  Total energy ~ 10⁵⁵ J                  │
  │        ╰───────────────╯                                          │
  └─────────────────────────────────────────────────────────────────────┘

  ORIGIN DEBATE:
  Hypothesis 1: Past AGN outburst from Sgr A*
    Timescale ~ 1–15 Myr ago (bubble edges sharp → recent)
    Required Eddington accretion for ~10⁵ yr, or sub-Eddington longer
    Support: X-ray edges suggest forward shock at bubble boundary

  Hypothesis 2: Nuclear starburst
    Intense SF in CMZ ~ few Myr ago
    SN-driven superwind inflates bubbles
    Support: molecular outflow from GC at ~100–200 km/s observed

  Both may contribute. Not yet settled.
```

### 6.4 Central Molecular Zone

```
  CMZ STRUCTURE (inner ~200 pc):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Total gas mass: ~ 5×10⁷ M☉ (mostly molecular H₂)             │
  │  Gas density: n > 10⁴ cm⁻³ (100× higher than spiral arm GMCs) │
  │  Temperature: T_gas ~ 60–200 K (warm due to cosmic rays, shocks)│
  │  Turbulent velocity: σ ~ 10–30 km/s (hugely supersonic)         │
  │                                                                 │
  │  LANDMARKS (in order of position, roughly):                     │
  │  Sgr C (l ~ −0.5°): dense cloud + HII region                    │
  │  Sgr B2 (l ~ +0.7°): most massive GMC in MW (~10⁷ M☉),        │
  │                        site of complex organic chemistry        │
  │  Sgr A West (l ~ 0°): minispiral of ionized gas                 │
  │                        orbiting within 1 pc of Sgr A*           │
  │  Sgr A East (l ~ 0°): expanding shell of non-thermal emission   │
  │                        ~ supernova remnant                      │
  │                                                                 │
  │  SFR in CMZ: ~0.05–0.1 M☉/yr — surprisingly LOW given         │
  │  high gas density (expected: ~1 M☉/yr from Kennicutt-Schmidt)   │
  │  Open problem: strong turbulence + magnetic pressure suppress SF│
  └─────────────────────────────────────────────────────────────────┘
```

### 6.5 Hypervelocity Stars

```
  HILLS MECHANISM (Hills 1988):
  ┌─────────────────────────────────────────────────────────────────┐
  │  A stellar binary approaches Sgr A* on a near-radial orbit.     │
  │  Tidal disruption of the binary:                                │
  │    r_t = a_binary (M_BH / m_binary)^{1/3}                     │
  │  One star is CAPTURED (extreme hardening of orbit around BH)    │
  │  Other star is EJECTED with velocity:                           │
  │    v_HVS ~ √(2GM_BH/r_t) × (m_binary/M_BH)^{1/6}             │
  │          ~ few × 10³ km/s at ejection                           │
  │                                                                 │
  │  Observed HVS (Brown et al. 2005 first discovery):              │
  │    ~30 HVS candidates with v > 400 km/s (> v_esc at R☉)       │
  │    Mostly B-type stars (short-lived → constrain ejection time)  │
  │    Anisotropic on sky → trace back to GC (not disk sources)     │
  │    Current record holder: ~700 km/s                             │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 7. Stellar Dynamics — Collisionless Systems

### 7.1 Two-Body Relaxation and the Collisionless Limit

The key question: do gravitational encounters between individual stars matter?

```
  TWO-BODY RELAXATION TIME:

  Consider a star moving through N identical stars in a sphere of radius R.
  Cumulative effect of many weak deflections (Chandrasekhar):

  SINGLE ENCOUNTER: star at impact parameter b deflects by angle:
    δv_⊥ / v ~ 2Gm / (bv²)    [first-order, b >> Gm/v²]

  SUM OVER ALL ENCOUNTERS (b from b_min to b_max):
    (Δv_⊥)² / v² ~ 8πG²m²n ln(b_max/b_min) / v⁴ × t
    = 8πG²ρ m ln(Λ) t / v³

  where Λ = b_max/b_min = N/1 → ln(Λ) = ln(N) (Coulomb logarithm)

  RELAXATION TIME (randomize v):
  ┌──────────────────────────────────────────────────────────────────┐
  │  t_relax ~ N / (8 ln N) × t_cross                              │
  │                                                                  │
  │  t_cross = R/σ = crossing time (~ orbit period)                │
  │  N = number of "field stars"                                     │
  └──────────────────────────────────────────────────────────────────┘

  FOR MILKY WAY DISK:
    N ~ 10¹¹ stars, t_cross ~ 200 Myr (orbital period)
    t_relax ~ 10¹¹ / (8 × 25) × 2×10⁸ yr
            ~ 10¹¹ / 200 × 2×10⁸ yr
            ~ 10¹⁷ yr   >> Hubble time (1.4×10¹⁰ yr)

  FOR GLOBULAR CLUSTER:
    N ~ 10⁵, t_cross ~ 1 Myr
    t_relax ~ 10⁵ / (8 × 12) × 10⁶ yr ~ 10⁹ yr ~ Hubble time
    → GCs DO experience two-body relaxation → core collapse possible

  CONCLUSION: The MW disk is effectively COLLISIONLESS on Hubble time.
  Individual star-star encounters are irrelevant for disk dynamics.
  The only exception: the dense GC environment within ~0.1 pc of Sgr A*.
```

### 7.2 The Collisionless Boltzmann Equation

For a collisionless system, the distribution function f(x, v, t) evolves via:

```
  COLLISIONLESS BOLTZMANN EQUATION (CBE):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ∂f/∂t + v · ∇_x f − ∇Φ · ∇_v f = 0                         │
  │                                                                 │
  │  (also written: df/dt = 0  along phase-space trajectories)      │
  └─────────────────────────────────────────────────────────────────┘

  f(x, v, t): number of stars per unit volume per unit velocity volume
              = phase-space distribution function
  Φ(x, t): gravitational potential (sourced by f via Poisson equation)

  ∇²Φ = 4πG ∫ f d³v = 4πG ρ    [Poisson equation; self-consistent]

  The CBE says: phase-space density is conserved along orbits
  (Liouville's theorem for Hamiltonian flow).

  PHYSICAL INTUITION:
  Phase-space "fluid" is incompressible. You can't create or destroy
  phase-space density — you can only stir and rearrange it.
  This has a key implication: violent relaxation (rapid potential changes
  during mergers) can mix phase space but not increase f at a given energy.
```

### 7.3 Jeans Theorem

```
  JEANS THEOREM:
  ┌─────────────────────────────────────────────────────────────────┐
  │  In steady state (∂f/∂t = 0), f depends on phase-space        │
  │  coordinates ONLY through integrals of motion (constants of     │
  │  motion along orbits).                                          │
  │                                                                 │
  │  Strong form: For an integrable potential with isolating        │
  │  integrals I₁, I₂, I₃:    f = f(I₁, I₂, I₃)                  │
  └─────────────────────────────────────────────────────────────────┘

  EXAMPLES:
  Spherical potential: integrals = E (energy), L (total angular momentum)
    → f = f(E, L)   [Eddington's formula: given ρ(r), invert for f(E)]

  Axisymmetric potential (MW disk): integrals approximately
    E (energy), L_z (angular momentum about z-axis), and the "third
    integral" I₃ (no closed form, but exists numerically)
    → f = f(E, L_z, I₃)

  WHY THIS MATTERS:
  Jeans theorem tells you that equilibrium stellar systems are
  "memory-erased" — they retain only the gross conserved quantities.
  The details of how the system formed are lost. This is why you can
  model a galaxy without knowing its exact formation history,
  just its current f(E, L_z, I₃).

  EXCEPTION: Substructure (stellar streams, shells) = departures from
  steady state. Gaia has revealed hundreds of stellar streams in the
  halo — each a fossil of a past accretion event.
```

### 7.4 Jeans Equations — Moments of the CBE

Take velocity moments of the CBE to get equations for observable quantities:

```
  ZEROTH MOMENT: ∂ρ/∂t + ∇·(ρ v̄) = 0    [continuity equation]

  FIRST MOMENT (radial, cylindrical coords, steady state ∂/∂t=0):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ρ ∂Φ/∂R = ρ(v̄_φ²/R − v̄_R²/R) − ∂(ρ σ_RR²)/∂R             │
  │           − (σ_RR² − σ_φφ²) ρ/R − ∂(ρ σ_Rz²)/∂z             │
  └─────────────────────────────────────────────────────────────────┘
  where σ_ij² = velocity dispersion tensor components.

  VERTICAL JEANS EQUATION (more commonly used):
  ┌─────────────────────────────────────────────────────────────────┐
  │  ∂(ρ σ_zz²)/∂z = −ρ ∂Φ/∂z = −ρ K_z                         │
  └─────────────────────────────────────────────────────────────────┘
  K_z = vertical restoring force

  PRACTICAL APPLICATION (Oort 1932 / Kuijken & Gilmore 1989):
    Measure σ_zz(z) and ρ_star(z) from stellar surveys.
    Integrate to get K_z(z).
    K_z = −∂Φ/∂z → Poisson → total midplane density ρ_total(R☉, 0)
    Compare ρ_total to visible matter → local dark matter density.

    Result: ρ_DM(R☉, 0) ~ 0.009–0.013 M☉/pc³ ~ 0.3–0.4 GeV/cm³
    [Used in direct dark matter detection experiments — the "local DM density"]
```

### 7.5 Epicyclic Orbits

Stars on nearly circular orbits undergo small oscillations — this is the epicyclic approximation:

```
  EPICYCLIC ORBIT GEOMETRY:
  ┌────────────────────────────────────────────────────────────────────┐
  │  Guiding center radius: R_g (set by L_z = R_g v_c(R_g))         │
  │  Radial displacement: x = R − R_g                                  │
  │  Radial oscillation: ẍ = −κ² x                                   │
  │  (κ = epicyclic frequency, defined in Section 4.3)               │
  │                                                                    │
  │  SOLUTION:                                                         │
  │    R(t) = R_g + A cos(κt + φ₀)                                   │
  │    φ(t) = Ω_g t − (2A Ω_g)/(κ R_g) sin(κt + φ₀)               │
  │                                                                    │
  │  The orbit traces an ELLIPSE (epicycle) about the guiding center.  │
  │  In the guiding center frame: the star moves on an ellipse with    │
  │  axis ratio (radial:azimuthal) = κ : 2Ω                         │
  │  For flat curve: κ = √2 Ω → axis ratio 1/√2 ~ 0.71              │
  │                                                                    │
  │  WHY ORBITS DON'T CLOSE in general:                                │
  │  Orbital period = 2π/Ω_g (azimuthal return time)                 │
  │  Epicyclic period = 2π/κ                                           │
  │  For orbit to close: κ/Ω = rational number                       │
  │  For flat curve: κ/Ω = √2 = irrational → orbits DON'T close     │
  │  → rosette patterns (they precess)                                 │
  └────────────────────────────────────────────────────────────────────┘

  VELOCITY DISPERSION vs DISK HEATING:
    Stars form cold (σ_R ~ 5 km/s from the GMC parent cloud).
    Over time, interactions with spiral arms, GMCs, the bar heat them:
    σ_R²(t) ∝ t^0.5  (empirical; theory still debated)

    Age-velocity dispersion relation (AVR):
    σ_R(young thin disk) ~ 15–20 km/s
    σ_R(thick disk/old stars) ~ 40–50 km/s
    → Dynamically hotter = older (modulo migration effects)
```

### 7.6 Vertical Dynamics and the Disk Scale Height

```
  VERTICAL OSCILLATIONS:

  Vertical equation of motion for a star in the disk:
    z̈ = −∂Φ/∂z ≈ −ν² z    [for small |z|; harmonic approximation]
    ν² ≈ 4πG ρ_midplane     [for thin disk, Poisson gives this]

  This gives ν ~ 70–90 km/s/kpc at R☉ (from ρ_mid ~ 0.1 M☉/pc³)

  ISOTHERMAL SHEET (self-gravitating disk):
    Assume disk is isothermal (σ_z = const) and self-gravitating.
    Poisson + Jeans vertical → sech² profile:

    ρ(z) = ρ_0 sech²(z/z_0)    z_0 = σ_z / √(2πGρ_0)

    For σ_z = 25 km/s (thin disk), ρ_0 = 0.1 M☉/pc³:
    z_0 = 25 km/s / √(2π × 6.67×10⁻⁸ × 0.1 × 2×10³³/3.09×10³⁸ cm³)
    Let's just note: z_0 ~ 100–150 pc for thin disk gas, confirming
    scale height ~ 300 pc (sech² width = 2z_0).

  DISK STABILITY (Toomre criterion):
    Disk is locally unstable to gravitational fragmentation if:
    Q = κ σ_R / (π G Σ) < 1   (gas)
        κ σ_R / (3.36 G Σ) < 1  (stars)

    Q ~ 1 in star-forming disk regions → marginal stability
    Q < 1 → spiral arm formation, GMC fragmentation, SF triggered
    Q > 1 → stable, no SF, no spirals
```

### 7.7 Tidal Stripping and the Tidal Radius

```
  TIDAL RADIUS OF SATELLITE:
  A satellite galaxy of mass m orbiting at distance R from MW (mass M(R)):

  ┌──────────────────────────────────────────────────────────────────┐
  │  r_t = R × (m / 3M(R))^{1/3}                                   │
  │                                                                  │
  │  DERIVATION: At the satellite's edge, the tidal force from MW    │
  │  equals the satellite's self-gravity:                            │
  │  2GM(R) r_t / R³  = G m / r_t²                                 │
  │  → r_t³ = m R³ / (2M(R))                                       │
  │  [factor of 2 → 3 from including centrifugal term in rotating    │
  │  frame, Roche criterion]                                         │
  │                                                                  │
  │  EXAMPLE: Sagittarius dwarf (M_Sgr ~ 10⁸ M☉) at R = 20 kpc:  │
  │  M_MW(20 kpc) ~ 10¹¹ M☉                                        │
  │  r_t = 20 × (10⁸/3×10¹¹)^{1/3} = 20 × (3.3×10⁻⁴)^{1/3}      │
  │      = 20 × 0.069 ~ 1.4 kpc                                    │
  │  → Stars beyond ~1.4 kpc from Sgr center get tidally stripped    │
  └──────────────────────────────────────────────────────────────────┘

  TIDAL STREAMS:
  Stripped stars form two tidal tails:
    - Leading tail: slightly smaller orbit, runs ahead of satellite
    - Trailing tail: slightly larger orbit, runs behind satellite
  Together these wrap around the sky as the satellite orbits.

  Sagittarius stream: wraps ~360° around the sky, found in
  multi-wrap detections (Majewski 2003, Law & Majewski 2010).
  Constrains MW halo shape: spherical/oblate/prolate/triaxial?
  Current data prefer slightly oblate-to-spherical halo.
```

---

## 8. Satellite Galaxies and the Local Group

### 8.1 Local Group Census

```
  LOCAL GROUP MEMBERSHIP (key objects):
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ Object          │ Type    │ Distance  │ M_* (M☉)    │ Notes             │
  ├─────────────────────────────────────────────────────────────────────────┤
  │ Milky Way       │ SBbc    │ —         │ ~5×10¹⁰    │ Our galaxy       │
  │ M31 (Andromeda) │ SAb     │ 770 kpc   │ ~10¹¹      │ Approaching MW   │
  │ M33 (Triangulum)│ Sc      │ 860 kpc   │ ~3×10⁹     │ M31 satellite?   │
  │ LMC             │ Irr/SBm │ 50 kpc    │ ~1.5×10¹⁰  │ First pericenter │
  │ SMC             │ Irr     │ 62 kpc    │ ~3×10⁸     │ LMC companion    │
  │ Sagittarius dSph│ dSph    │ 26 kpc    │ ~10⁸       │ Disrupting now   │
  │ Fornax dSph     │ dSph    │ 147 kpc   │ ~2×10⁷     │ Classical dSph   │
  │ Sculptor dSph   │ dSph    │ 86 kpc    │ ~2×10⁶     │ Classical dSph   │
  │ Leo I, II       │ dSph    │ 250, 205  │ ~5×10⁶     │ Distant classics │
  │ Draco, UMi      │ dSph    │ 76, 66    │ ~2×10⁵     │ Low M/L giants   │
  │ Segue 1, 2...   │ UFD     │ 23–50 kpc │ ~10³–10⁵   │ Ultra-faint dSphs│
  │ ~80 total known │         │           │             │                  │
  └─────────────────────────────────────────────────────────────────────────┘
  UFD = Ultra-Faint Dwarf; most DM-dominated objects known (M/L ~ 1000–10000)

  LOCAL GROUP EXTENT: ~1.5 Mpc radius, total mass ~ 3×10¹² M☉
  ZERO-VELOCITY SURFACE: ~1.2 Mpc (turnaround radius; beyond = Hubble flow)
```

### 8.2 LMC Infall and the Dark Matter Wake

The LMC is not a typical small satellite. Its mass (~10% of the MW disk mass) makes it dynamically significant:

```
  LMC INFALL DYNAMICS:
  ┌─────────────────────────────────────────────────────────────────────┐
  │  LMC mass: M_LMC ~ 1.5×10¹⁰ M☉ (from stellar mass + subhalos)  │
  │  Pericenter: ~50 kpc, 50 Myr ago (FIRST pericenter — not on a    │
  │  long-bound orbit, just arrived on cosmological infall trajectory)│
  │                                                                     │
  │  EFFECTS ON MW:                                                   │
  │  1. DARK MATTER WAKE: LMC gravitationally drags DM halo behind   │
  │     it as it orbits → overdense trailing wake detected in         │
  │     RR Lyrae star counts (Conker et al. 2021)                    │
  │                                                                     │
  │  2. REFLEX MOTION OF MW: LMC's gravity pulls MW inner halo       │
  │     toward LMC → MW disk is offset from MW halo center by ~30 kpc│
  │     This induces apparent proper motion of SGR A* (spurious!)     │
  │     and must be corrected for in MW mass measurements             │
  │                                                                     │
  │  3. DISK PERTURBATION: LMC induces a warp + corrugations in      │
  │     the outer MW disk (confirmed in Gaia red giant branch stars)  │
  │                                                                     │
  │  4. MW-ANDROMEDA MERGER TIMING: LMC infall adds uncertainty       │
  │     to MW total mass → collision timing uncertain by ~1 Gyr       │
  └─────────────────────────────────────────────────────────────────────┘
```

### 8.3 MW-Andromeda Merger

```
  FUTURE MERGER: MW + M31
  ┌─────────────────────────────────────────────────────────────────┐
  │  Current separation: ~770 kpc                                   │
  │  Radial velocity: −110 km/s (approaching)                       │
  │  Transverse velocity: ~17 km/s (from HST + Gaia proper motions) │
  │  → Nearly head-on collision, low angular momentum               │
  │                                                                 │
  │  First pericenter: ~4.5 Gyr from now                            │
  │  Full merger ("Milkomeda"): ~6–7 Gyr from now                   │
  │                                                                 │
  │  EXPECTED OUTCOME:                                              │
  │  Major merger → bursty SF → AGN activity → gas funneled to      │
  │  merged nucleus → likely quenching → giant elliptical galaxy    │
  │  Solar System is almost certainly ejected to large radius       │
  │  (~100 kpc orbits in the merger remnant)                        │
  │  Probability of direct stellar collision: effectively zero      │
  │  (stars are too small relative to inter-stellar spacing)        │
  └─────────────────────────────────────────────────────────────────┘
```

### 8.4 The Small-Scale Structure Problems

```
  ΛCDM PREDICTIONS vs OBSERVATIONS at small scales:

  ┌──────────────────────────────────────────────────────────────────────┐
  │ Problem              │ CDM Prediction    │ Observation      │ Status │
  ├──────────────────────────────────────────────────────────────────────┤
  │ Missing Satellites   │ ~10³ subhalos     │ ~60 MW sats      │ Tension │
  │                      │ M > 10⁸ M☉       │ known+projected  │         │
  │ Resolution: reionization photo-evaporates gas from small halos;     │
  │ SDSS/LSST finding more UFDs; observational incompleteness.          │
  ├──────────────────────────────────────────────────────────────────────┤
  │ Too Big to Fail      │ Most massive subs │ Not hosting      │ Tension│
  │                      │ (10^9-10 M☉ halos)│ bright galaxies  │        │
  │ Resolution: SN feedback lowers central density; baryon effects       │
  │ reduce rotation curves of massive subs below observed dSphs.         │
  ├──────────────────────────────────────────────────────────────────────┤
  │ Core-Cusp           │ NFW: ρ ∝ r⁻¹     │ dwarf sph: cores │ Tension │
  │                      │ (cuspy core)      │ (flat center)    │         │
  │ Resolution: baryonic feedback (repeated SN outbursts) heats DM     │
  │ cusp → core. Works for dwarfs with SFH; fails for halos with no SF. │
  ├──────────────────────────────────────────────────────────────────────┤
  │ Planes of Satellites │ Isotropic         │ MW + M31 sats    │ Active │
  │ (great plane problem)│ accretion → no    │ in co-planar     │ debate │
  │                      │ preferred plane   │ co-rotating plane│        │
  │ Resolution: filamentary accretion along cosmic web; but            │
  │ co-rotation is hard to explain. Some say statistical fluke.        │
  └──────────────────────────────────────────────────────────────────────┘

  ALTERNATIVES TO CDM:
  WDM (warm dark matter): free-streaming suppresses small halos
    → lighter DM particle (keV mass, e.g., sterile neutrino)
    → power spectrum cutoff at ~10⁸ M☉ scale
    Constraint: Lyman-α forest limits m_WDM > 3–5 keV

  SIDM (self-interacting dark matter): DM cross section σ/m ~ 1 cm²/g
    → DM halos thermalize → isothermal cores (solves cusp-core)
    → galaxy clusters: core structures in mergers (Bullet Cluster OK)

  Fuzzy/ultra-light DM (FDM): m_a ~ 10⁻²² eV
    → de Broglie wavelength ~ kpc scale → quantum pressure supports cores
    → Schrödinger-Poisson equation for DM waves
    → Interesting for UFDs; tension with Lyman-α at small scales
```

---

## 9. Galaxy Morphology and Classification

### 9.1 Hubble Sequence — The Tuning Fork

```
  HUBBLE TUNING FORK:

                              Sa   Sb   Sc   Sd
                         ╭───┬────┬────┬────┬────╮ Spirals (S)
     Ellipticals         │   │    │    │    │    │
     E0 E1 E2 ... E7 ───S0──╪────╪────╪────╪────╪ (S0 = lenticular)
                         │   │    │    │    │    │
                         ╰───┴────┴────┴────┴────╯ Barred Spirals (SB)
                              SBa  SBb  SBc  SBd
                                        \
                                         └── Irr (irregular)
                                              (Magellanic, HII-dominated)

  CLASSIFICATION AXES (along Hubble sequence S→Sd):
  ┌──────────────────────────────────────────────────────────────────┐
  │ Property         │  Early-type (E/S0/Sa) │  Late-type (Sd/Irr)   │
  ├──────────────────────────────────────────────────────────────────┤
  │ Bulge fraction   │  Large (50–100%)       │  Small (<5%)         │
  │ Arm definition   │  Tightly wound (>25°)  │  Open, ragged        │
  │ Gas fraction     │  Low (<5%)             │  High (>50%)         │
  │ Color            │  Red                   │  Blue                │
  │ SFR              │  Quiescent             │  Active              │
  │ Dominant pop     │  Pop II                │  Pop I               │
  │ Typical mass     │  10¹⁰–10¹² M☉         │  10⁷–10¹⁰ M☉       │
  └──────────────────────────────────────────────────────────────────┘

  TERMINOLOGY NOTE: "Early" and "late" are historical — Hubble
  thought the sequence was evolutionary (it is NOT). Early-type
  ≠ older formation. The terms just persist by convention.
```

### 9.2 Surface Brightness Profiles

```
  EXPONENTIAL DISK (Freeman 1970):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Σ(R) = Σ₀ exp(−R/R_d)                                        │
  │                                                                 │
  │  Σ₀ = central surface density [M☉/pc²]                          │
  │  R_d = scale length [kpc]                                       │
  │  μ(R) = μ₀ + 1.086 R/R_d   [magnitude/arcsec²; 1.086 = 2.5/ln10]│
  │                                                                 │
  │  MW: R_d ~ 3.5 kpc, Σ₀(R☉) derived from deprojection          │
  └─────────────────────────────────────────────────────────────────┘

  SÉRSIC PROFILE (de Vaucouleurs 1948 generalized by Sérsic 1963):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Σ(R) = Σ_e exp{−b_n [(R/R_e)^{1/n} − 1]}                    │
  │                                                                 │
  │  R_e = effective radius (half-light radius)                     │
  │  Σ_e = surface density at R_e                                   │
  │  n   = Sérsic index                                             │
  │  b_n ≈ 2n − 1/3 + 4/(405n) + ...  (from Γ(2n) = 2γ(2n, b_n)) │
  │                                                                 │
  │  n=1: exponential disk (b_1 ≈ 1.678)                            │
  │  n=4: de Vaucouleurs profile (classical ellipticals) (b_4 ≈ 7.67)│
  │  n<2: pseudo-bulge (disk-like)                                  │
  │  n>2: classical bulge / elliptical                              │
  └─────────────────────────────────────────────────────────────────┘

  SCHECHTER LUMINOSITY FUNCTION:
  ┌─────────────────────────────────────────────────────────────────┐
  │  φ(L) dL = φ* (L/L*)^α exp(−L/L*) d(L/L*)                    │
  │                                                                 │
  │  L* ~ 2×10¹⁰ L☉ (characteristic "knee" luminosity)            │
  │  α ~ −1.05 (faint-end slope; −1 → equal mass per decade in L) │
  │  φ* ~ 1.4×10⁻² h³ Mpc⁻³ (normalization)                      │
  │                                                                 │
  │  L >> L*: exponential cutoff → rare very luminous galaxies      │
  │  L << L*: power-law rise → many faint galaxies                  │
  │  L* corresponds to MW ~ M31 luminosity range                    │
  └─────────────────────────────────────────────────────────────────┘
```

### 9.3 Scaling Relations

```
  TULLY-FISHER RELATION (1977):
  ┌─────────────────────────────────────────────────────────────────┐
  │  L ∝ v_c^4    (spiral galaxies; v_c from 21-cm HI linewidth)  │
  │  or: M_* ∝ v_c^4 (more fundamental; stellar mass TF relation) │
  │                                                                 │
  │  DERIVATION SKETCH:                                             │
  │  Assume: M ∝ v_c² R (virial), Σ ~ const (Freeman), L ∝ M_*:  │
  │  M ~ v_c² R, R ∝ M^{1/2}/Σ^{1/2} → M ∝ v_c^4/Σ             │
  │  For constant Σ: M ∝ v_c^4                                      │
  │                                                                 │
  │  USE: Standard ruler/candle for distances to spiral galaxies    │
  │  (measure v_c from emission lines; get intrinsic L; compare to  │
  │  apparent magnitude → distance)                                 │
  └─────────────────────────────────────────────────────────────────┘

  FABER-JACKSON RELATION (1976):
    L ∝ σ^4    (ellipticals; σ = central velocity dispersion)
    Scatter: ~0.5 mag; superseded by Fundamental Plane

  FUNDAMENTAL PLANE (Dressler 1987, Djorgovski & Davis 1987):
  ┌─────────────────────────────────────────────────────────────────┐
  │  log R_e = α log σ₀ + β log <I_e> + γ                         │
  │                                                                 │
  │  Standard values: α ~ 1.24, β ~ −0.82                           │
  │  Scatter: ~0.07 dex in log R_e (< 20% in R_e)                 │
  │                                                                 │
  │  VIRIAL EXPECTATION:                                            │
  │  Virial theorem: M ∝ σ² R_e                                     │
  │  M/L = const → L ∝ M → L ∝ Σ R_e² → Σ_e ∝ M/R_e²            │
  │  Combining: R_e ∝ σ^2 / Σ_e   [virial FP]                     │
  │  α=2, β=−1 expected; observed α=1.24 → "tilt" of FP          │
  │  Tilt due to: M/L increasing with mass (massive ellipticals     │
  │  have older stellar populations + more DM contribution)         │
  └─────────────────────────────────────────────────────────────────┘

  GALAXY BIMODALITY:
  ┌─────────────────────────────────────────────────────────────────┐
  │              M_* ~ 3×10¹⁰ M☉                                  │
  │              (green valley transition)                          │
  │   LOW MASS:                          HIGH MASS:                 │
  │   Blue Cloud                         Red Sequence               │
  │   Star-forming                       Quiescent                  │
  │   Exponential disks                  de Vaucouleurs / Sérsic n>2 │
  │   Low [Fe/H] (ongoing infall)        High [Fe/H], old           │
  │   Isolated or low-density envs       Cluster centers            │
  │                                                                 │
  │   QUENCHING MECHANISMS:                                         │
  │   1. AGN feedback: energy/momentum from SMBH → ejects/heats gas │
  │   2. Virial heating: in M > 10¹² M☉ halos, infalling gas shocks│
  │      to T_vir and can't cool fast → no cold gas → no SF         │
  │   3. Ram-pressure stripping: ICM strips ISM from satellite      │
  │      galaxies in clusters → "jellyfish galaxies"                │
  │   4. Strangulation: halo stripped → no further gas accretion    │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 10. Galaxy Formation and Evolution

### 10.1 Bottom-Up Structure Formation

```
  CDM STRUCTURE FORMATION HIERARCHY:
  ┌──────────────────────────────────────────────────────────────────┐
  │  POWER SPECTRUM: P(k) ∝ k^n_s T²(k)                           │
  │  n_s ~ 0.965 (primordial tilt from inflation)                    │
  │  T(k) = transfer function (suppresses small scales below         │
  │          matter-radiation equality horizon ~ 100 Mpc comoving)   │
  │                                                                  │
  │  BOTTOM-UP (hierarchical) for CDM:                               │
  │  Small halos (10⁶ M☉) collapse first at z ~ 20–30              │
  │  Merge progressively → larger halos                              │
  │  Galaxy clusters (10¹⁴ M☉) only assemble recently (z < 1)     │
  │                                                                  │
  │  CONTRAST with WDM / HDM:                                        │
  │  HDM (neutrinos): free-stream far, small scales erased           │
  │  → top-down structure: large pancakes fragment into galaxies     │
  │  Observed large-scale structure (voids, filaments, walls)        │
  │  + galaxy formation times → rules out HDM (neutrino masses       │
  │  too large ruled out by Lyman-α forest + CMB).                   │
  └──────────────────────────────────────────────────────────────────┘
```

### 10.2 Cooling and the Galaxy Formation Condition

White & Rees (1978) formulated the key physics: gas falls into DM potential wells, but only collapses into galaxies if it can cool:

```
  WHITE-REES CONDITION:
  ┌──────────────────────────────────────────────────────────────────┐
  │  Gas in halo virial shock heated to:                             │
  │  T_vir = μ m_H v_c² / (2 k_B)                                  │
  │        ~ 5×10⁵ K (v_c/100 km/s)²     [for μ = 0.59]           │
  │                                                                  │
  │  Cooling function Λ(T) [erg cm³ s⁻¹]:                          │
  │    T < 10⁴ K: negligible (neutral gas)                         │
  │    T ~ 10⁴–10⁵ K: atomic H + He cooling (collisional excitation)│
  │    T ~ 10⁵–10⁷ K: metal-line cooling dominates               │
  │    T > 10⁷ K: Bremsstrahlung (free-free), Λ ∝ T^{1/2}         │
  │                                                                  │
  │  COOLING TIME: t_cool = (3/2) n k_B T / (n² Λ) ∝ T/(nΛ)      │
  │  DYNAMICAL TIME: t_dyn = 1/√(Gρ)                               │
  │                                                                  │
  │  GALAXY FORMATION CONDITION: t_cool < t_dyn                    │
  │  → Gas can radiate away its thermal energy faster than it        │
  │    would gravitationally disperse → collapse → star formation    │
  │                                                                  │
  │  THIS IS MET FOR:                                                │
  │    Halos with M ~ 10¹⁰–10¹² M☉ (T_vir in cooling peak)       │
  │    → galaxy mass scale! Explains why galaxies have masses in     │
  │      this range (White-Rees 1978 — fundamental result).          │
  │                                                                  │
  │  NOT MET FOR:                                                    │
  │    M < 10¹⁰ M☉: gas heated by UV background after reionization │
  │                   → gas photo-evaporated, no SF                  │
  │    M > 10¹² M☉: cooling time >> dynamical time even with metals  │
  │                   → VIRIAL SHOCK; hot diffuse halo; no cold      │
  │                     inflow → no star formation → red, dead       │
  └──────────────────────────────────────────────────────────────────┘
```

### 10.3 Hot vs Cold Accretion — Dekel-Birnboim

```
  TWO ACCRETION MODES (Dekel & Birnboim 2006):
  ┌──────────────────────────────────────────────────────────────────┐
  │  M_halo < ~10¹² M☉  (T_vir < ~2×10⁶ K):                      │
  │    COLD ACCRETION: infalling gas streams along dark matter       │
  │    filaments, never shocks, reaches disk as cold (T ~ 10⁴ K)   │
  │    dense streams → efficient SF                                  │
  │    → Blue, star-forming, gas-rich galaxies                       │
  │                                                                  │
  │  M_halo > ~10¹² M☉  (T_vir > ~2×10⁶ K):                      │
  │    VIRIAL SHOCK: infalling gas cannot penetrate hot halo         │
  │    (shock heating + AGN feedback prevents cooling)               │
  │    → No cold supply → quenching → red sequence                 │
  │                                                                  │
  │  The ~10¹² M☉ threshold is the "bimodality mass" → it          │
  │  corresponds to the L* transition in the galaxy luminosity       │
  │  function and the star-forming/quiescent bimodality.             │
  │                                                                  │
  │  At HIGH REDSHIFT (z > 2):                                       │
  │    Even massive halos can have cold streams penetrate through    │
  │    the hot halo along cosmic web filaments → explains why        │
  │    z~2 SMGs (massive, dusty SF galaxies) exist and form stars    │
  │    rapidly despite being in massive halos.                       │
  └──────────────────────────────────────────────────────────────────┘
```

### 10.4 Feedback Mechanisms

```
  SUPERNOVA FEEDBACK (low-mass galaxies):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Each SN releases ~10⁵¹ erg. With SFR ~ 1 M☉/yr:              │
  │  SN rate ~ 1/100 yr → power ~ 10⁵¹ erg / 10⁷ yr ~ 3×10³⁶ W  │
  │                                                                 │
  │  In low-mass halos: v_esc small → SN energy can drive winds     │
  │  that eject gas, enrich CGM, suppress SF                        │
  │  Mass loading: η = Ṁ_wind / SFR ~ 1–10 for dwarf galaxies     │
  │  Coupling efficiency: ~30% of SN energy goes to wind kinetics   │
  │  (rest radiated away during Sedov phase before hot gas merges)  │
  └─────────────────────────────────────────────────────────────────┘

  AGN FEEDBACK (high-mass galaxies — the "maintenance mode"):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Two modes:                                                     │
  │                                                                 │
  │  QUASAR MODE (high accretion, z ~ 2–3 peak):                    │
  │    Ṁ_BH ~ 0.1–1 Ṁ_Edd → luminous; radiative driving           │
  │    → blast wave quenching of host galaxy ("blowout")            │
  │    → rapid BH mass growth (BH–bulge mass correlation set here)  │
  │                                                                 │
  │  RADIO/KINETIC MODE (low accretion, present-day clusters):      │
  │    RIAF (radiatively inefficient accretion flow)                │
  │    Jets inflate bubbles in cluster ICM (seen in X-ray cavities) │
  │    Bubble enthalpy ~ P V = 4 × 10⁶⁰ erg                       │
  │    Heating balances cooling in cluster cores → no catastrophic  │
  │    cooling flow → no starburst in central galaxy ("maintenance")│
  │                                                                 │
  │  M_BH − σ RELATION:                                             │
  │  M_BH ~ 10⁸ M☉ (σ/200 km/s)^5   [Gebhardt 2000, Ferrarese 2000]│
  │  Scatter: ~0.3 dex; implies co-evolution of BH + bulge          │
  │  Physical: energy coupling via quasar wind; BH mass when wind   │
  │  can unbind the bulge's gas: E_wind = f ε Ṁ c² = f_gas M_bulge  │
  │  σ² → M_BH ∝ σ^5 (King 2003 momentum-driven)                  │
  └─────────────────────────────────────────────────────────────────┘
```

### 10.5 Downsizing and Anti-Hierarchical Star Formation

```
  DOWNSIZING PARADOX:
  ┌─────────────────────────────────────────────────────────────────┐
  │  CDM predicts: massive galaxies assembled LATER (more mergers   │
  │  required; halos virialize later for larger mass scales).       │
  │                                                                 │
  │  Observed: the most MASSIVE galaxies:                           │
  │  1. Have the OLDEST stellar populations ([α/Fe] enhancement     │
  │     → rapid SF → old)                                           │
  │  2. Were quenched earliest (passive evolution since z ~ 2)      │
  │  3. Their stars formed in the highest-SFR events at z ~ 2–4     │
  │                                                                 │
  │  RESOLUTION: "Downsizing in STARS, not in halos"                │
  │  Massive halos DO assemble hierarchically (CDM is right about   │
  │  halos). But their star formation is ANTI-HIERARCHICAL because: │
  │                                                                 │
  │  At z ~ 2–3: massive halos host quasar activity → AGN quenches  │
  │  → stars formed in burst at high z, then galaxy goes red.       │
  │  Subsequent mergers add stellar mass but are gas-poor "dry"     │
  │  mergers → no new SF, just stellar growth.                      │
  │                                                                 │
  │  Low-mass galaxies: shallow potential → SN feedback regulates   │
  │  SF to be slow and steady → stars still forming today           │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 11. The Interstellar Medium — Phases and Physics

### 11.1 ISM Phase Diagram

```
  ISM THERMAL PHASES (pressure equilibrium):

  Temperature (K)
  10⁶ ─────┬─────────────────────────────────────────────
           │  ╔═══════════════╗
           │  ║ HOT IONIZED   ║  (HIM)
           │  ║ MEDIUM (HIM)  ║  T ~ 10⁶ K
           │  ║ n ~ 10⁻³ cm⁻³║  SN remnants, OB winds
           │  ║ filling: ~50% ║  soft X-ray background
           │  ╚═══════════════╝
  10⁴ ─────┼──────────────────────────────────────────────
           │  ╔══════════╗  ╔══════════╗
           │  ║   WARM   ║  ║   WARM   ║
           │  ║ NEUTRAL  ║  ║ IONIZED  ║  (WNM / WIM)
           │  ║  MEDIUM  ║  ║  MEDIUM  ║  T ~ 8000 K
           │  ║T~8000 K  ║  ║ n_e~.03  ║  Hα, DM of pulsars
           │  ║n~0.4cm⁻³ ║  ║  cm⁻³   ║  WNM: 21-cm emission
           │  ╚══════════╝  ╚══════════╝
  10² ─────┼──────────────────────────────────────────────
           │  ╔══════════╗  ╔══════════╗
           │  ║   COLD   ║  ║ MOLECULAR║
           │  ║ NEUTRAL  ║  ║   GAS    ║  T ~ 10–80 K
           │  ║  MEDIUM  ║  ║  n>10²  ║  CO tracer
           │  ║  (CNM)   ║  ║ cm⁻³   ║  GMCs, SF sites
           │  ║T~80 K    ║  ║         ║
           │  ║n~40 cm⁻³ ║  ╚══════════╝
           │  ╚══════════╝
  ─────────┴──────────────────────────────────────────────
           n:  10⁻³   10⁻²   10⁻¹   10⁰   10¹   10²  cm⁻³

  KEY: CNM and WNM coexist at the SAME THERMAL PRESSURE
       P/k_B ~ n T ~ 3000 K cm⁻³
       This is the two-phase equilibrium (Field+Goldsmith+Habing 1969)
```

### 11.2 Thermal Instability — Field (1965)

The classic result: a thermally stratified gas in pressure equilibrium can be unstable, producing phase separation:

```
  FIELD INSTABILITY CRITERION:

  Consider gas in thermal equilibrium with P = const.
  Net cooling function: L(ρ, T) = n² Λ(T) − n Γ  [erg/cm³/s]
    Λ(T) = cooling function, Γ = heating rate per atom

  At equilibrium: L = 0  → defines equilibrium curve in n-T plane.

  For an isobaric perturbation (P = const = n k_B T → δn/n = −δT/T):

  INSTABILITY if:    ∂L/∂T |_{P=const} < 0

  Equivalently (Field 1965):
  ┌──────────────────────────────────────────────────────────────────┐
  │  d ln Λ/d ln T < 1   (at constant pressure)                    │
  │  → THERMALLY UNSTABLE: perturbations grow → phase separation   │
  │                                                                  │
  │  STABLE PHASES:                                                  │
  │  T < 300 K or T > 6000 K: d ln Λ/d ln T > 1 → stable          │
  │  → CNM (T ~ 80 K) and WNM (T ~ 8000 K) are the stable phases   │
  │                                                                  │
  │  UNSTABLE REGIME:                                                │
  │  300 < T < 6000 K: d ln Λ/d ln T < 1                           │
  │  → Any gas forced into this range phase-separates into CNM+WNM │
  └──────────────────────────────────────────────────────────────────┘

  PHYSICAL INTERPRETATION:
  In the unstable range: if gas is compressed (δT < 0 at const P),
  cooling increases faster than heating → gas cools further → runaway
  to CNM. Expanded gas → runs away to WNM.
  Result: gas naturally segregates into the two stable phases,
  explaining the observed bimodal temperature distribution in HI.
```

### 11.3 ISM Energy Balance — Approximate Equipartition

```
  ENERGY DENSITIES AT R ~ R☉:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Thermal (T ~ 8000 K WNM):  P_th = n k_B T                    │
  │    ~ 0.4 × 1.38×10⁻¹⁶ × 8000 ~ 4.4×10⁻¹³ erg/cm³            │
  │                                                                 │
  │  Turbulent:  P_turb = ½ ρ σ²_turb                               │
  │    σ_turb ~ 10 km/s, n_WNM ~ 0.4 cm⁻³                        │
  │    ~ ½ × 0.4 × 1.67×10⁻²⁴ × (10⁶)² ~ 3×10⁻¹³ erg/cm³       │
  │                                                                 │
  │  Magnetic:  P_B = B²/8π                                         │
  │    B ~ 4 μG = 4×10⁻⁶ G                                        │
  │    ~ (4×10⁻⁶)²/(8π) ~ 6×10⁻¹³ erg/cm³                       │
  │                                                                 │
  │  Cosmic ray:  P_CR ~ 10⁻¹² erg/cm³  (GeV protons)             │
  │                                                                 │
  │  ALL FOUR ARE COMPARABLE — ~10⁻¹² erg/cm³ = 1 eV/cm³          │
  │  This is NOT a coincidence: the ISM self-regulates to near-     │
  │  equipartition. SN feedback drives turbulence; turbulence       │
  │  amplifies B via dynamo; CRs stream along B and provide         │
  │  additional pressure support. Each component contributes ~      │
  │  equally to disk pressure balance and vertical hydrostatic equil.│
  └─────────────────────────────────────────────────────────────────┘

  MAGNETIC FIELD STRUCTURE:
  ┌─────────────────────────────────────────────────────────────────┐
  │  Regular field: B ~ 2 μG, following spiral arm pattern          │
  │  Field reversal at ~3–4 kpc inside R☉ (sign flip in RM)       │
  │  Random/turbulent component: δB ~ B_reg                         │
  │  Vertical: B_z very small (B mostly in plane)                   │
  │                                                                 │
  │  Scale height of B: ~ 1–2 kpc (thin disk)                       │
  │  Parker instability: magnetic buoyancy lifts field out of plane │
  │    → loops emerge → CRs escape along loops → pressure relief    │
  │    → Vertical convective transport of magnetic flux             │
  └─────────────────────────────────────────────────────────────────┘
```

### 11.4 21-cm Line and ISM Diagnostics

```
  THE 21-cm LINE (HI λ = 21.106 cm, ν = 1420.4 MHz):
  ┌─────────────────────────────────────────────────────────────────┐
  │  Hyperfine structure of ground-state HI:                        │
  │  F=1 (parallel spins) → F=0 (antiparallel) + photon           │
  │  A_10 = 2.87×10⁻¹⁵ s⁻¹  (half-life ~ 11 Myr for single atom) │
  │  BUT: n_H ~ 10²⁰–10²² cm⁻² in galaxy → emission detectable    │
  │                                                                 │
  │  Column density from optically thin emission:                   │
  │  N_HI [cm⁻²] = 1.82×10¹⁸ ∫ T_B(v) dv   [K km/s]             │
  │                                                                 │
  │  Velocity field → Galactic rotation via 21-cm line:             │
  │  v_obs = v_LSR = v_c(R) sin(l) cos(b) − v_c(R☉) sin(l)       │
  │  [for b=0 (midplane), l = Galactic longitude]                   │
  │                                                                 │
  │  TANGENT POINT METHOD (l < 90°):                                │
  │  Maximum velocity at given l is from tangent point at R=R☉ sin(l)│
  │  → v_max(l) = v_c(R_tan) − v_c(R☉) sin(l)                    │
  │  → Trace v_c(R) from 21-cm observations alone                   │
  └─────────────────────────────────────────────────────────────────┘

  PULSAR DISPERSION MEASURE (DM probe of WIM):
  ┌─────────────────────────────────────────────────────────────────┐
  │  DM = ∫₀^d n_e dl  [pc cm⁻³]                                  │
  │  Pulsar dispersion: Δt ∝ DM/ν² (pulse arrives later at lower ν)│
  │  With pulsar distance known → n_e(l, b) model of WIM          │
  │  YMW16 model: n_e(R, z) at ~ 0.05 cm⁻³ (local WIM)           │
  └─────────────────────────────────────────────────────────────────┘
```

---

## 12. Reference Cheat Sheet

```
  ╔══════════════════════════════════════════════════════════════════════════╗
  ║              GALACTIC STRUCTURE — KEY NUMBERS                          ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  R☉ = 8.178 ± 0.013 kpc   (GRAVITY 2019)                            ║
  ║  v_c(R☉) ~ 220–240 km/s    (flat rotation curve)                     ║
  ║  v_esc(R☉) ~ 550 km/s      (Piffl 2014)                              ║
  ║  Ω☉ = v_c/R☉ ~ 27.2 km/s/kpc                                        ║
  ║  T_orbit ≡ 2πR☉/v_c ~ 225 Myr  (Galactic year)                      ║
  ║  Oort A ~ 15.3, B ~ −11.9 km/s/kpc                                  ║
  ║  κ(R☉) ~ 36–38 km/s/kpc   (√2 Ω for flat curve)                    ║
  ║  ρ_DM(R☉, 0) ~ 0.3–0.4 GeV/cm³ = 0.009–0.013 M☉/pc³              ║
  ║  B_ISM ~ 3–6 μG (disk);  turbulent δB ~ B_reg                       ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║              MILKY WAY MASSES                                          ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  M_disk (thin+thick) ~ 5×10¹⁰ M☉                                   ║
  ║  M_bulge ~ 1×10¹⁰ M☉                                               ║
  ║  M_DM halo (virial) ~ 10¹² M☉                                      ║
  ║  M_MW (total virial) ~ 1.3×10¹² M☉  (Watkins 2019)                 ║
  ║  M_Sgr A* = 4.154×10⁶ M☉            (GRAVITY 2019)                 ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║              PROFILES                                                   ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  Thin disk: Σ(R) = Σ₀ exp(−R/R_d),  R_d~3.5 kpc, h_z~300 pc        ║
  ║  Thick disk: h_z ~ 900 pc                                             ║
  ║  Sérsic: Σ(R) = Σ_e exp{−b_n[(R/R_e)^{1/n}−1]}                     ║
  ║    n=1 (disk), n=4 (de Vaucouleurs elliptical), n<2 (pseudo-bulge)   ║
  ║  NFW halo: ρ = ρ_s/[(r/r_s)(1+r/r_s)²],  r_s~20 kpc for MW         ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║              DYNAMICS                                                   ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  Relaxation time: t_relax ~ (N/8 ln N) × t_cross                     ║
  ║  CBE: ∂f/∂t + v·∇f − ∇Φ·∂f/∂v = 0                                  ║
  ║  Jeans theorem: f = f(integrals of motion) in steady state            ║
  ║  Epicyclic freq: κ² = R dΩ²/dR + 4Ω²  → κ = √2 Ω (flat curve)     ║
  ║  Tidal radius: r_t = R(m/3M)^{1/3}                                  ║
  ║  Toomre Q = κ σ_R/(π G Σ);  Q<1 → unstable → SF/spirals             ║
  ║  Resonances: Ω ± κ/m = Ω_p  (ILR, OLR)                             ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║              SCALING RELATIONS                                          ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  Tully-Fisher:   L ∝ v_c^4   (spirals; also M_* TF relation)        ║
  ║  Faber-Jackson:  L ∝ σ^4     (ellipticals; superseded by FP)         ║
  ║  Fund. Plane:    log R_e = α log σ₀ + β log <I_e> + γ               ║
  ║  M_BH−σ:         M_BH ∝ σ^5  (M_BH ~ 10⁸ M☉ at σ=200 km/s)       ║
  ║  Schechter:      φ(L) ∝ (L/L*)^α exp(−L/L*);  L*~2×10¹⁰ L☉        ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║              ISM PHASES                                                 ║
  ╠══════════════════════════════════════════════════════════════════════════╣
  ║  CNM: T~80 K, n~40 cm⁻³;  WNM: T~8000 K, n~0.4 cm⁻³               ║
  ║  WIM: T~8000 K, n_e~0.03 cm⁻³;  HIM: T~10⁶ K, n~10⁻³ cm⁻³        ║
  ║  Molecular: T~10–30 K, n>100 cm⁻³                                   ║
  ║  Equipartition: P_th ~ P_turb ~ P_B ~ P_CR ~ 10⁻¹² erg/cm³         ║
  ║  Metalicity gradient: dZ/dR ~ −0.06 dex/kpc (thin disk)             ║
  ╚══════════════════════════════════════════════════════════════════════════╝
```

---

## 13. Common Confusion Points

**Spiral arms are not material structures.**
Stars and gas pass through spiral arms. The arm is a density enhancement (either a quasi-stationary density wave or a transient self-gravitating structure) through which material flows. The observed OB associations in arms are the youngest populations, born when gas was compressed passing through — they've barely moved since formation. This is why arm-tracing with HII regions works: these are "just born" markers.

**Corotation does not mean the Sun rides a spiral arm.**
Corotation radius R_CR ~ 8 kpc is close to R☉ ~ 8.178 kpc. The Sun doesn't orbit *with* a spiral arm. It means the Sun and the spiral pattern happen to have similar angular velocities at this radius — stars inside corotation lap the pattern, outside they fall behind it. The Sun's proximity to corotation means it crosses arms infrequently, which has been invoked (controversially) as a selection effect favoring complex life.

**The bulge is not a classical merger-built bulge.**
The MW "bulge" is primarily a buckled bar — a pseudo-bulge. The evidence: boxy/X-shaped morphology in BRAVA survey kinematics, cylindrical rotation, Sérsic n ~ 1–2. The bar buckled vertically due to a resonance (vertical frequency commensurable with bar tumbling frequency), creating banana-shaped orbits (x4 orbital family). Classical merger-built bulges are kinematically hot, spheroidal, Sérsic n ~ 4.

**NFW concentration and scale radius are not independent parameters.**
Given halo mass M_vir, concentration c = r_vir/r_s is set (approximately) by the halo's formation redshift via c-M relation from N-body simulations: halos that collapsed earlier are denser (higher concentration). MW's c ~ 10 is typical for a ~10¹² M☉ halo collapsing at z ~ 2–3.

**[α/Fe] measures SF timescale, not absolute age.**
High [α/Fe] at a given [Fe/H] means fast SF (CCSN enriched the ISM before SNe Ia could contribute Fe). It is not a direct age indicator — a galaxy could have short, intense SF very recently and still have high [α/Fe]. But for the MW specifically, the high-α sequence being old is supported by spectroscopic ages (isochrone fitting) and Gaia asteroseismology. The two diagnostics together pin down both when and how fast stars formed.

**The missing satellites and too-big-to-fail problems are not fatal to ΛCDM.**
Baryonic physics (reionization quenching, SN feedback, observational incompleteness) substantially resolves the missing satellites problem. TBTF is resolved in hydrodynamic simulations where SN feedback reduces the inner DM density of massive subhalos, lowering their rotation curves to match observed dSphs. The Planes of Satellites problem remains more challenging theoretically, though some argue for statistical fluke or filamentary accretion. ΛCDM at large scales (BAO, CMB, cluster abundance) remains a success.

**The Jeans theorem is not the same as the Jeans instability.**
Two completely different things. Jeans theorem: in steady-state collisionless dynamics, f depends only on integrals of motion (Section 7.3). Jeans instability: gas is unstable to gravitational collapse when M > Jeans mass M_J = (π/6) ρ (π c_s²/Gρ)^{3/2} — a fluid/gas stability criterion. The name coincidence is historical (James Jeans worked on both).

**Toomre Q = 1 in disk is not a coincidence — it is self-regulation.**
When Q < 1, the disk fragments: GMCs form, stars form, SNe heat the gas → increase σ → Q rises back to ~1. When Q >> 1, no fragmentation, no SF, ISM cools → σ decreases → Q falls back to ~1. The disk self-regulates around Q ~ 1. Observations of external galaxies confirm this: SF occurs preferentially where Q < 1.

**"Downsizing" is about stars, not halos.**
CDM halos DO assemble hierarchically (small first, large later). "Downsizing" refers specifically to stellar populations: stars in today's massive galaxies are *older* and were formed *faster* than stars in today's low-mass galaxies. These two facts are consistent once you account for AGN quenching (massive halos quench early) vs SN-regulated slow SF (low-mass halos form stars slowly over a Hubble time).

**The Fermi bubbles are not fully explained.**
Both the past AGN activity hypothesis and the nuclear starburst hypothesis for the Fermi bubbles remain viable. The sharp edge of the bubbles (detected in X-ray by eROSITA as the "eROSITA bubbles" at even larger ~14 kpc scale) suggests a single recent energetic event rather than sustained emission, favoring a brief AGN episode. But molecular outflows at ~100–200 km/s from the CMZ support starburst contributions as well. Both may have played a role.
```
