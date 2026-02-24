# Silicon Substrate — A Layered Guide

## The Big Picture

Every chip starts with a single crystal of silicon — the purest solid manufactured
at industrial scale. The Czochralski process converts sand into a boule of
electronic-grade silicon with impurity levels below 1 part per trillion.

```
FROM SAND TO WAFER
════════════════════════════════════════════════════════════════════

Quartz sand (SiO₂)
    │
    ▼ Carbon arc furnace at 1800°C
Metallurgical-grade Si (98% pure, ~10¹⁶ impurities/cm³)
    │
    ▼ Siemens process (trichlorosilane distillation + CVD)
Electronic-grade (EG) Si: 11 nines pure (99.999999999%)
    ≈ 10¹⁰ impurities/cm³ — one alien atom per 100 billion Si
    │
    ▼ Czochralski (CZ) crystal growth
Single-crystal Si ingot (boule)
    300 mm diameter, 2 m long, ~250 kg
    │
    ▼ Diamond wire saw → slicing
Raw wafers (775 µm thick at 300 mm)
    │
    ▼ Lapping → edge grinding → CMP → cleaning
Polished production wafer: surface roughness <0.15 nm RMS
    Ready for lithography
```

---

## Czochralski Process

```
CZOCHRALSKI (CZ) CRYSTAL GROWTH

               ┌─────────────────────────┐
               │     Pulling rod         │
               │          │              │
               │     [Seed crystal]      │
               │          │              │
               │     Crystal boule       │
               │    (growing upward)     │
               │         ╱╲              │
               │   Melt puddle           │
               │ (polycrystalline Si     │
               │  + controlled dopants)  │
               │                         │
               │     Quartz crucible     │
               │     in vacuum/inert     │
               │     atmosphere, RF      │
               │     heated to 1420°C    │
               └─────────────────────────┘

PROCESS:
1. Melt EG polysilicon in quartz crucible (~1420°C)
2. Lower single-crystal seed crystal to melt surface
3. Seed crystal wets melt; atoms align with seed lattice
4. Pull slowly upward (few mm/hr) + rotate:
   → Crystal solidifies epitaxially onto seed
   → Diameter controlled by pull rate + temperature
5. Neck (very thin) grown first → eliminates dislocations from seed
   (Dash necking technique)
6. Shoulder growth → expand to target diameter
7. Body growth → maintain diameter for 1-2 meters
8. Tail taper → prevent dislocation back-propagation
9. Result: dislocation-free single crystal boule

DIAMETER HISTORY:
  25 mm (1960s) → 100 mm → 150 mm → 200 mm (1990s) → 300 mm (2000s)
  450 mm: stalled (industry couldn't justify retooling cost for marginal gain)
  300 mm is current standard for leading-edge logic

PULL RATE vs DIAMETER:
  Pull rate: 1-5 mm/min
  Crystal length: 1,000-2,000 mm
  Total growth time: 24-48 hours per boule
```

---

## Doping: n-Type and p-Type Silicon

```
SILICON DOPING

Intrinsic Si: 4 valence electrons, forms covalent lattice
  ni ≈ 1.5 × 10¹⁰ carriers/cm³ at 300 K (both electrons and holes)

N-TYPE (adding donor atoms):
  Group V elements: phosphorus (P), arsenic (As), antimony (Sb)
  Each donor contributes 1 extra electron (majority carrier)
  n ≈ ND (donor concentration)
  Typical: 10¹⁵ - 10¹⁷ atoms/cm³
  Fermi level shifts toward conduction band

P-TYPE (adding acceptor atoms):
  Group III elements: boron (B)
  Each acceptor contributes 1 hole (majority carrier)
  p ≈ NA (acceptor concentration)
  Typical: 10¹⁵ - 10¹⁷ atoms/cm³
  Fermi level shifts toward valence band

RESISTIVITY vs DOPING CONCENTRATION:
  ρ = 1/(q·n·µn + q·p·µp)   [Ω·cm]
  µn ≈ 1350 cm²/V·s (electron mobility)
  µp ≈ 480 cm²/V·s (hole mobility)

  Doping (cm⁻³)   Resistivity (Ω·cm)   Type
  ────────────────────────────────────────
  10¹³             ~100-500             intrinsic-like
  10¹⁵             ~5                  lightly doped
  10¹⁷             ~0.05               moderately doped
  10¹⁹             ~0.001              heavily doped (ohmic contact)

CZ DOPING:
  Boron (p-type) or phosphorus (n-type) added to melt
  Segregation coefficient k₀ < 1: dopants concentrate in melt as crystal grows
  → Concentration gradient from seed end to tail
  → Target: uniform axial resistivity across usable wafer region
```

---

## Float Zone (FZ) Silicon

```
FLOAT ZONE (FZ) vs CZOCHRALSKI (CZ)

FZ PROCESS:
  No crucible: polysilicon rod held vertically
  RF coil heats small molten zone → moves along rod
  Crystal grows behind melting front
  Impurities segregate into advancing melt zone → driven off end
  Result: highest-purity Si possible

COMPARISON:
                        CZ                      FZ
  ─────────────────────────────────────────────────────────────
  Purity                Very high (10-20 ppb O)  Highest (<0.1 ppb O)
  Oxygen content        High (Oi ~ 10¹⁸ cm⁻³)   Very low
  Carbon                Low                       Very low
  Max diameter          300+ mm                  200 mm (difficult larger)
  Cost                  Lower                    Higher
  Mechanical strength   Higher (O strengthens)   Lower
  Yield in fab          Good                     More fragile

FZ APPLICATIONS:
  Power semiconductors (IGBT, power diodes): need high resistivity (>50 Ω·cm)
  High-voltage: 5-20 kΩ·cm FZ Si
  Radiation detectors, solar cell research
  NOT used for leading-edge logic (CZ standard there)

OXYGEN IN CZ:
  O comes from quartz crucible dissolution at 1420°C
  O at ~10¹⁸ cm⁻³: not intrinsically bad
  Beneficial: oxide precipitates getter metallic impurities during processing
  Harmful: oxygen donors form at 350-500°C anneal → unintended doping
  Intrinsic gettering uses O precipitates in bulk to trap metals away from device region
```

---

## Silicon on Insulator (SOI)

```
SOI WAFER STRUCTURE

Standard (bulk) Si:
  [Device layer Si — 775 µm thick]

SOI structure:
  [Device layer Si — 5-100 nm thin Si film]
  [Buried Oxide (BOX) — 50-150 nm SiO₂]
  [Handle wafer Si — 750 µm thick]

SOI MANUFACTURING:
  SIMOX: implant O⁺ ions at high energy → form buried oxide → anneal
  Smart Cut (Soitec process — dominant):
    1. Oxidize donor Si wafer → grow SiO₂ (future BOX)
    2. Implant H⁺ at controlled depth → hydrogen-rich layer (cleavage plane)
    3. Bond to handle wafer (oxide-oxide bonding)
    4. Anneal: hydrogen layer causes exfoliation → top Si film transfers
    5. CMP: smooth transferred Si surface → production SOI wafer

SOI ADVANTAGES:
  Full isolation: device layer fully surrounded by insulator
    → No latch-up (parasitic thyristor action in bulk CMOS)
    → No soft errors from bulk leakage
  Reduced junction capacitance → faster switching at lower voltage
  Better subthreshold slope → lower Vt at same off-state current

FD-SOI (Fully Depleted SOI):
  Si device layer thin enough (5-10 nm) to be fully depleted → no partial depletion
  Very well controlled Vt; low leakage
  STMicroelectronics/Samsung: 28 nm and 22 nm FD-SOI (FD-SOI-28, FD-SOI-22)
  Competing approach to FinFET for some applications (IoT, automotive, RF)

DISADVANTAGES:
  Wafer cost: 3-5× bulk Si wafer
  Thermal conductivity lower (SiO₂ is thermal insulator) → self-heating
  History: IBM led SOI for Power CPUs; Intel uses SOI only for specialty; TSMC logic is bulk
```

---

## Wafer Specifications

```
WAFER SPECIFICATIONS (300 mm production standard)

PHYSICAL:
  Diameter:       300 mm ± 0.2 mm
  Thickness:      775 µm (300 mm) / 725 µm (200 mm)
  Total Thickness Variation (TTV): <2 µm
  Bow/Warp:       <60 µm (flatness for lithography alignment)
  Surface roughness (polished face): <0.15 nm RMS

CRYSTAL QUALITY:
  Orientation: (100) dominant (cleave easier, better gate oxide quality)
               (111) for bipolar, power devices
  Primary flat / notch: indicates orientation + crystal type
  Dislocation density: zero for prime grade (CZ, Dash necking)
  Point defects: COP (Crystal Originated Pits) <50/wafer prime

ELECTRICAL:
  Resistivity specification tied to doping (see above table)
  For CMOS logic substrate: lightly doped (5-20 Ω·cm) p-type
  Device-layer doping separate (implanted during process)

CLEANLINESS:
  Metals (Fe, Ni, Cu, Na): <10¹⁰ atoms/cm² surface
  Particles (≥0.09 µm): <50/wafer
  Delivered sealed in sealed cassettes (FOUPs) under nitrogen

PRODUCTION FORMAT:
  FOUP (Front Opening Unified Pod): cassette of 25 wafers
  AMHS (Automated Material Handling System): robots move FOUPs
  A 300 mm fab processes ~150,000-200,000 wafers/month at full capacity
```

---

## Decision Cheat Sheet

| Application | Substrate Choice |
|-------------|-----------------|
| Leading-edge logic (CPU/GPU/mobile) | Bulk CZ Si, 300 mm, (100), p-type |
| High-voltage power devices (IGBT) | FZ Si, 150-200 mm, high resistivity |
| Low-power IoT / RF front-end | FD-SOI (22FDX or 28FDSOI) |
| Memory (DRAM/NAND) | Bulk CZ, 300 mm, cell-optimized process |
| Compound semiconductor RF (GaN/GaAs) | SiC substrate (GaN-on-SiC) or semi-insulating GaAs |
| Silicon photonics | SOI (Si waveguide in SiO₂ cladding) |

---

## Common Confusion Points

**"11 nines pure" doesn't mean all atoms are Si**: Electronic-grade Si is 99.999999999% pure
by concentration, but the relevant metric is impurity atoms per cm³. At 11 nines, you have
~10¹⁰ impurity atoms/cm³ in a matrix of ~5×10²² Si atoms/cm³. For reference, a lightly doped
wafer intentionally has 10¹⁵ boron atoms/cm³ — five orders of magnitude more than unintended impurities.

**The wafer isn't the chip's active region**: The 775 µm Si wafer is structural. The actual transistors
exist in the top 50-100 nm of silicon. The rest is just mechanical support.

**CZ vs FZ isn't about purity for logic**: CZ silicon has more oxygen (from crucible), which is
actually beneficial for logic fabs — oxygen precipitates getter metallic contaminants away from
the device region. FZ purity is needed for power devices requiring high resistivity.

**300 mm hasn't given way to 450 mm despite predictions**: The semiconductor equipment industry
couldn't agree on funding the ~$10B joint investment to retool all equipment for 450 mm wafers.
TSMC, Intel, and Samsung tried (EUV 450 program collapsed ~2015). 300 mm remains production standard
indefinitely.
