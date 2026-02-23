# Optical Fiber — Total Internal Reflection, Drawing, Attenuation, Modes

## The Big Picture

Optical fiber is the physical infrastructure of the modern internet. Every transatlantic cable, every long-haul network link, every data center interconnect runs on glass fibers thinner than a human hair. The physics is elegant: light guided by total internal reflection through ultra-pure glass with losses so low that a signal can travel 80km before needing amplification.

```
OPTICAL FIBER SYSTEM ARCHITECTURE
====================================

TRANSMITTER → FIBER → AMPLIFIER → FIBER → RECEIVER
  (laser)      (SMF)    (EDFA)     (SMF)    (photodetector)

SINGLE FIBER SPAN:
 Core (8-10μm, SMF): light travels here
 Cladding (125μm OD): lower RI → TIR keeps light in core
 Primary coating (250μm OD): soft acrylate; bend protection
 Secondary coating/buffer: mechanical protection

MODERN SYSTEM BANDWIDTH:
 One fiber pair (Tx + Rx): 100+ Tb/s (DWDM, C-band)
 96+ wavelength channels at 100-400 Gb/s each
 One transoceanic cable: 8-16 fiber pairs
 Total cable capacity: 1+ Pb/s (petabits/second)

NETWORK CONTEXT:
 Long-haul: SMF; 1,550nm; EDFA amplifiers every 80-100km
 Metro/access: SMF or MMF; shorter spans
 Data center: MMF for 100m-300m; SMF for longer DCI
 Premises/FTTH: SMF to the home (G.657 bend-insensitive fiber)
```

---

## Total Internal Reflection (TIR) — The Physics

```
TIR FUNDAMENTALS
=================

SNELL'S LAW: n₁ sin(θ₁) = n₂ sin(θ₂)
 n₁, n₂: refractive indices of medium 1 and 2
 θ₁, θ₂: angles from normal (perpendicular to interface)

CRITICAL ANGLE (θ_c):
 When light travels from denser → less dense medium
 At θ_c: refracted ray travels along the interface (θ₂ = 90°)
 n₁ sin(θ_c) = n₂ sin(90°) = n₂
 θ_c = arcsin(n₂/n₁)

 For silica glass (n≈1.444) to air (n=1.0):
  θ_c = arcsin(1.0/1.444) = arcsin(0.693) ≈ 43.7°
  Above 43.7° angle of incidence: total reflection; no refraction

FIBER GEOMETRY:
 Core (n₁ = higher): guides light
 Cladding (n₂ = lower): surrounds core; TIR at core-cladding interface
 Core-cladding RI difference: small (~0.3-1%)
  achieved by DOPING:
   Core: add GeO₂ (germanium dioxide) → increases RI
   Cladding: add fluorine → decreases RI
   Or: pure silica cladding + Ge-doped core (most common SMF)

NUMERICAL APERTURE (NA):
 NA = sin(half-angle of acceptance cone) = √(n₁² - n₂²)
 SMF typical NA: 0.12-0.14
 MMF typical NA: 0.20-0.30
 Higher NA → accepts light from wider angle → easier coupling to LED
  but: higher NA = more modes → more modal dispersion
```

---

## Single-Mode vs Multimode Fiber

```
FIBER TYPE COMPARISON
======================

SINGLE-MODE (SMF):
 Core diameter: 8-10μm (standard SMF G.652)
 Cladding: 125μm
 Color jacket: yellow (OS1, OS2)
 Operation: only the fundamental mode propagates
  → no modal dispersion
  → can carry very high bandwidth over very long distances
 Light source: laser (DFB laser, external-cavity laser) — must be narrow linewidth
  to avoid chromatic dispersion issues; expensive
 Wavelength windows:
  O-band: 1,260-1,360nm (~0.35 dB/km)
  E-band: 1,360-1,460nm (water peak band; reduced in low-water-peak fiber)
  S-band: 1,460-1,530nm
  C-band: 1,530-1,565nm (minimum loss ~0.18 dB/km; primary DWDM window)
  L-band: 1,565-1,625nm (extended DWDM)
 Applications: all long-haul telecom, submarine cables, metro rings,
               data center long-haul interconnect

MULTIMODE (MMF):
 Core diameter: 50μm (OM3, OM4, OM5) or 62.5μm (OM1, OM2 — legacy)
 Cladding: 125μm
 Color jacket: aqua (OM3/OM4) or lime green (OM5)
 Operation: multiple modes travel simultaneously
  → modal dispersion: modes travel at slightly different velocities
  → pulse spreading over distance → bandwidth-distance product limited
 OM3: 2,000 MHz·km bandwidth (50μm core)
 OM4: 4,700 MHz·km
 OM5: 28,000 MHz·km (at 953nm for short-wavelength SWDM)
 Light source: LED or VCSEL (vertical-cavity surface-emitting laser)
  VCSEL: 850nm; inexpensive; powers modern MMF data center links
 Applications: data center (top-of-rack to end-of-row, typically <100m)
               SAN (storage area networks); campus backbone

KEY DISTINCTION:
 SMF: one mode → no modal dispersion → long distance + high bandwidth
 MMF: many modes → modal dispersion → limited distance; lower cost
 In data centers: MMF at 100m-300m with short-wavelength VCSELs is
  economically optimal; SMF for longer connections (>300m or inter-building)

GRADED-INDEX vs STEP-INDEX:
 Step-index MMF: sharp RI boundary between core and cladding
  → severe modal dispersion (outer modes slower than center modes)
 Graded-index MMF: RI varies continuously (parabolic profile) through core
  → higher modes travel faster (lower RI path) → modes arrive simultaneously
  → dramatically reduces modal dispersion (enabled MMF for 1 Gb/s+)
 All modern OM3/OM4/OM5 are graded-index (α-profile core)
```

---

## Attenuation — Loss Mechanisms

```
FIBER ATTENUATION
==================

UNIT: dB/km  (decibels per kilometer)
 Each 10 dB = power reduced by 10×
 System budget: total power budget ÷ loss per km = max span length

LOSS MECHANISMS:

RAYLEIGH SCATTERING (dominant at short wavelengths):
 Light scattered by refractive index fluctuations at molecular scale
 (composition fluctuations "frozen in" during fiber drawing)
 Scales as λ⁻⁴ (shorter wavelength = much more scattering)
 Irreducible in silica at any practical temperature
 At 1,550nm: ~0.12 dB/km Rayleigh contribution
 At 850nm: ~1.2 dB/km Rayleigh contribution (10× worse)
 This is why long-haul uses 1,550nm not 850nm

IR ABSORPTION (dominant at long wavelengths):
 Si-O bond vibrations (molecular phonons) absorb IR
 Fundamental absorption: ~9μm (mid-IR)
 Overtones and combination bands extend into telecom window
 At 1,550nm: ~0.06 dB/km IR absorption contribution

WATER PEAK (OH⁻ ions):
 OH⁻ ions dissolved in glass during manufacturing (from moisture)
 Absorb strongly at 2.73μm; overtone at 1.38μm ("water peak")
 The 1,383nm water peak limits the E-band window
 Standard SMF (G.652D): very low OH⁻ → E-band usable ("low-water-peak")
 Old fiber (pre-1990): significant water peak → only O and C/L bands usable

MINIMUM LOSS:
 Rayleigh + IR absorption cross at ~1,550nm
 Standard SMF at 1,550nm: ~0.18-0.20 dB/km (world record: 0.142 dB/km)
 The 1,550nm minimum defines the C-band DWDM window
 80km unrepeatered span → ~14-16 dB total loss → within EDFA launch budget

BENDING LOSSES:
 Macro-bend: radius below critical bend radius → light escapes
  Standard SMF: R > 30mm (typical installation) → negligible loss
  G.657.A1/B1 bend-insensitive SMF: R down to 10mm/5mm → FTTH use
  (installation in conduits, tight corners requires bend tolerance)
 Micro-bend: micron-scale surface perturbations (from coating pressure,
  installation friction) → scattering losses; cumulative over km
  Modern fiber coating designed to minimize micro-bend contribution
```

---

## Fiber Fabrication — Preform and Draw

```
MANUFACTURING PROCESS
======================

STEP 1: PREFORM MANUFACTURE
 Cylindrical glass rod with designed core/cladding RI profile
 Typical dimensions: 10-15 cm diameter; 1 meter long
 Mass: 5-15 kg
 One preform → 1,000-5,000 km of fiber (draw ratio: 1/10,000+ in length)

MCVD (Modified Chemical Vapor Deposition):
 Silica tube (starting substrate) rotated and traversed by oxy-hydrogen torch
 Gas phase: SiCl₄ + GeCl₄ + O₂ (or fluorine-containing gas for cladding)
 Oxidation reaction: SiCl₄ + O₂ → SiO₂ + 2Cl₂
  Occurs INSIDE the tube → oxide soot deposits on inner wall
 Layer by layer deposition → multiple passes with varying compositions
 Core: GeO₂-doped SiO₂ layers; cladding: pure or F-doped SiO₂
 Collapse: final heating → tube collapses to solid rod (the preform)
 Inside deposition = core at center, cladding as surrounding tube
 Used by: Corning, OFS, many others

OVD (Outside Vapor Deposition) / VAD (Vapor-phase Axial Deposition):
 Flame hydrolysis: SiCl₄ + 2H₂O → SiO₂ + 4HCl
  (in oxyhydrogen flame; soot deposited onto target)
 OVD: deposits layers on outside of rotating mandrel (seed rod)
 VAD: deposits on end of rotating rod (axially); no mandrel to remove
 Both: glass soot deposited → sintered at high temperature → dense glass preform
 Used by: Fujikura, Sumitomo (VAD) ; Corning (OVD) as primary large-scale method

STEP 2: DRAW TOWER
 Tower: 20-30m tall; preform feeds down from top
 Preform neck-down zone: ~2,000-2,100°C; zirconia furnace or CO₂ laser
 Glass neck down → fiber forms at bottom
 Drawing speed: 10-30 m/s
 Diameter control: laser micrometer measures fiber OD continuously
  → feedback to drawing speed: faster pull = thinner fiber
  Target: 125.0 ± 0.1μm (tight tolerance)
 Coating application: UV-cured acrylate applied immediately after drawing
  Two layers: soft inner primary (protects glass); hard outer secondary
 UV cure: mercury lamp banks; cure in <0.1 second
 Take-up spools: fiber wound at drawing speed
 Typical spool: 25km of fiber
```

---

## DWDM and Amplification

```
DENSE WAVELENGTH DIVISION MULTIPLEXING
=========================================

PRINCIPLE:
 Different wavelengths of light travel independently in the same fiber
 Combine (multiplex) multiple channels → transmit → separate (demultiplex)
 Each channel: independent data stream at different λ
 Capacity multiplication: 96 channels × 400 Gb/s = 38.4 Tb/s per fiber pair

ITU GRID:
 C-band: 1,530-1,565nm; divided into channels
 100 GHz grid: 40 channels (~0.8nm spacing)
 50 GHz grid: 80 channels (~0.4nm spacing)
 25 GHz grid: 160 channels (~0.2nm spacing)
 Flex grid (G.694.1): variable width channels for optical superchannels

EDFA (ERBIUM-DOPED FIBER AMPLIFIER):
 Revolutionized long-haul transmission (introduced ~1987; deployed early 1990s)
 Previously: optical → electrical → optical regeneration required every 20-30km
 EDFA: purely optical amplification; no OEO conversion
 Physics: Er³⁺ ions in glass fiber; pump laser (980nm or 1,480nm) excites Er³⁺
  → population inversion → stimulated emission at ~1,550nm
  Signal photons → stimulated emission → amplified
 Bandwidth: amplifies entire C-band simultaneously
  → all DWDM channels amplified in single amplifier
 Span: 80-100km between EDFAs; multiple EDFAs per submarine cable
 Noise: EDFA adds ASE (amplified spontaneous emission) noise; accumulated

COHERENT MODULATION:
 Modern long-haul: coherent detection with DP-QPSK, DP-16QAM
 Modulates phase and amplitude; digital signal processing recovers signal
 DSP compensates: chromatic dispersion, PMD, nonlinearities
 This enabled 100G → 400G → 800G and beyond per channel
 The fiber itself hasn't fundamentally changed; the signaling has
 (Same physics of fiber; different modulation formats and DSP chips)

SUBMARINE CABLES:
 Longest: FLAG cable (Asia-Europe-US, ~28,000km); 2Africa (~45,000km)
 Fiber: multiple pairs (8-24 pairs in modern cables)
 Repeaters (EDFAs): every 50-80km; powered from shore via DC on armor wire
 Capacity: 2Africa = 180+ Tb/s design capacity
 Reliability: designed for 25-year life; landing station locations = geopolitical
 The internet's physical foundation: ~400 submarine cables carry ~99% of
 international internet traffic (not satellite — not even close by capacity)
```

---

## Common Confusion Points

**TIR requires light to travel from denser to less dense medium**:
Light in fiber travels from higher-RI core to lower-RI cladding → TIR possible. If you reversed core and cladding RI, TIR would not trap light in the core. This is why cladding must have lower RI than core.

**Single-mode vs multimode is not about signal quality in a simple sense**:
SMF is better for long distance (no modal dispersion) but requires expensive lasers. MMF is sufficient for short-distance, high-bandwidth applications (data centers) with cheap VCSELs. Neither is universally "better" — it's application-dependent.

**EDFA amplifies light, not electrical signal**:
EDFA is a purely optical device. The signal never becomes electrical during EDFA amplification. This is why EDFA was so revolutionary — prior regeneration required three conversions (O→E→O at each repeater). EDFA also amplifies multiple DWDM channels simultaneously.

**Fiber attenuation at 1,550nm is fundamental, not a material defect**:
The 0.18 dB/km minimum loss of silica SMF at 1,550nm is set by fundamental physics (Rayleigh scattering + IR absorption cross). It cannot be improved by making the glass "purer." New fiber materials (hollow-core photonic bandgap fiber) aim to beat this limit by propagating light in air, not glass.

---

## Decision Cheat Sheet

| Fiber Question | Answer |
|----------------|--------|
| Why long-haul uses 1,550nm | Minimum attenuation in silica (~0.18 dB/km) |
| Why data centers use 850nm with MMF | VCSEL cost + MMF cheaper for short (<300m) links |
| Core diameter: SMF vs MMF | SMF ~9μm; MMF 50μm or 62.5μm |
| RI difference source in silica fiber | Core: Ge-doped (higher RI); cladding: pure or F-doped |
| How preform is made | MCVD (inside deposition) or OVD/VAD (outside deposition) |
| Draw tower height | 20-30m; drawing at 10-30 m/s |
| How EDFA amplifies | Er³⁺ ions pumped by 980nm laser → stimulated emission at 1,550nm |
| DWDM channel count (C-band, 50 GHz) | 80 channels |
| Critical angle in silica→air | ~43.7° |
| What limits fiber span before amplification | Rayleigh scattering + IR absorption (~0.18 dB/km × 80km = 14 dB) |
