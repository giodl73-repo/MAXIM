# Ultrasound — A Layered Guide

## The Big Picture

Ultrasound (> 20 kHz) uses acoustic waves for imaging, therapy, cleaning, and sensing.
The fundamental advantage: short wavelengths (< 1 mm) enable millimeter-scale resolution.

```
ULTRASOUND FREQUENCY AND APPLICATION MAP
════════════════════════════════════════════════════════════════════

Frequency:  20 kHz    200 kHz    2 MHz     20 MHz     200 MHz
            │         │          │         │          │
            ▼         ▼          ▼         ▼          ▼
         ┌──────────┬──────────┬──────────┬──────────┬──────────┐
         │Ultrasonic│  Power   │ Medical  │High-freq │ Acoustic │
         │cleaning, │ultrasound│ imaging  │imaging   │microscopy│
         │welding,  │(HIFU,    │(cardiac/ │(vascular/│(SAM)     │
         │sonication│lithotrip)│obstetric)│skin)     │          │
         │          │          │          │          │          │
         │Industrial│Therapy   │Diagnosis │Superficial│Research │
         │NDT       │          │          │ tissue   │          │
         └──────────┴──────────┴──────────┴──────────┴──────────┘

KEY TRADE-OFF: Higher frequency → better resolution (λ = c/f → smaller) BUT
               shorter range (attenuation ∝ f in tissue)

λ in tissue at 5 MHz: λ = 1540 m/s / 5 MHz = 0.31 mm (axial resolution ≈ λ/2)
λ in tissue at 15 MHz: λ = 0.10 mm → superficial imaging (skin, eyes)
```

---

## Piezoelectric Effect

The physical basis of most ultrasound transducers.

```
PIEZOELECTRIC EFFECT

DIRECT: Apply force/stress to crystal → electric charge generated
         (mechanical → electrical: sensor/microphone)

INVERSE: Apply electric field to crystal → mechanical strain
          (electrical → mechanical: actuator/transmitter)

MATERIALS:
Quartz: natural, low coupling, very stable → frequency references
PZT (lead zirconate titanate): strong coupling, ceramic, dominant for medical imaging
PVDF (polyvinylidene fluoride): polymer, flexible, lower coupling, wide bandwidth
LiNbO₃, LiTaO₃: for high-frequency and wide-bandwidth applications

COUPLING COEFFICIENT k:
k² = electrical energy converted / total mechanical energy stored
PZT: k ≈ 0.5–0.7 (efficient)
PVDF: k ≈ 0.1–0.2 (less efficient but wide bandwidth)

RESONANT FREQUENCY:
For thickness-mode vibration (most common):
f₀ = c_piezo / (2·t)   where t = thickness
At 5 MHz: t = c_PZT / (2·f) = 4000 m/s / 10⁷ = 0.4 mm

Backing material: damping layer behind transducer to reduce ringdown
(improves bandwidth at cost of sensitivity)
Matching layers: λ/4 matching layers between piezo and tissue (impedance matching)
```

---

## Medical Ultrasound Imaging

### A-Mode (Amplitude Mode)

```
A-MODE (1D):

Transmit short pulse → receive echoes → plot amplitude vs time (= depth)

Pulse echo:
  ─────────────────────────────────────────────────────────
  Transmit: ∥∥∥
  Echo from surface 1:           ┌┐
  Echo from surface 2:                  ┌┐
  Echo from surface 3:                           ┌┐
  ─────────────────────────────────────────────────────────
  Time:     0               10µs             20µs
  Depth:    0               7.7mm            15.4mm   (at c=1540m/s, depth=c·t/2)

A-mode: plot echo amplitude vs depth (one scan line)
Used for: ophthalmology (eye measurements), cardiac measurements
```

### B-Mode (Brightness Mode) — Standard Imaging

```
B-MODE (2D cross-sectional image):

Steer or move beam through many angles/positions:
  Scan line 1: ──────── echoes → column 1 of image
  Scan line 2: ──────── echoes → column 2
  Scan line N: ──────── echoes → column N

Assemble 2D image: brightness ∝ echo amplitude

MODERN TRANSDUCER ARRAY:
Linear array: 128–256 elements, electronic steering
  → Real-time frame rate 30–60 Hz
  → No mechanical scanning

RESOLUTION:
Axial (along beam): ≈ c·τ/2  where τ = pulse duration
  = c/(2·BW)  for bandwidth BW
  At 5 MHz, 50% bandwidth: axial resolution ≈ 0.15 mm

Lateral (across beam): ≈ λ·F/D   (diffraction limit)
  = λ·F/D  where F = focal distance, D = aperture
  At 5 MHz, 40mm focus, 20mm aperture: lateral ≈ 0.75 mm

Dynamic focusing: synthesize focus at every depth during receive (no moving parts)
```

### M-Mode (Motion Mode)

```
M-MODE:
Single scan line, continuous sampling → tracks motion vs time
Classical use: Cardiac wall motion (mitral valve, wall thickness changes)

PLOT: Depth (y-axis) vs Time (x-axis) → shows moving boundaries
```

### Doppler Ultrasound

```
DOPPLER FREQUENCY SHIFT:

Moving target (blood flow velocity v, angle θ to beam):
f_Doppler = 2·f₀·v·cos(θ) / c

At 3.5 MHz, blood flow v = 0.5 m/s, θ = 60°:
f_D = 2 × 3.5×10⁶ × 0.5 × cos(60°) / 1540 = 1136 Hz
                                               (audible range!)

CONTINUOUS WAVE DOPPLER:
One crystal transmits, another receives simultaneously
Cannot measure depth (range-ambiguous)
Used for high-velocity flow (valves, fetal heart)

PULSED WAVE DOPPLER:
Same transducer, pulse echo with range gate
Measures velocity at specific depth
Maximum velocity limited by PRF (pulsed repetition frequency):
  v_max = c · PRF / (8 · f₀ · cos θ)   (Nyquist for Doppler)

COLOR FLOW DOPPLER:
Estimate Doppler shift at each pixel → color overlay on B-mode image
Red: toward probe; Blue: away from probe
Typical flow displayed: 5 cm/s to 1 m/s

DUPLEX IMAGING: B-mode + spectral Doppler simultaneously
```

---

## Industrial Nondestructive Testing (NDT)

Ultrasonic NDT detects flaws (cracks, voids, inclusions) in metals, composites, and welds.

```
NDT IMAGING METHODS

PULSE-ECHO (UT):
  Transmit → travel through material → echo from defect or back wall

  Probe ──────────────────────── Back wall
  ||||  →  →  →  →  →  →  →  →  echo
            ↓ defect → early echo!

  Defect location = echo time × c / 2

PHASED ARRAY UT (PAUT):
  Array of 16–256 elements
  Electronic steering and focusing (like medical imaging)
  → Full cross-sectional imaging
  → TOFD (Time of Flight Diffraction): two probes, measures diffracted tips of cracks
    → More accurate sizing than amplitude-based methods

COMMON INSPECTIONS:
  Weld inspection: pipeline welds, pressure vessels (ASME code)
  Aerospace: composites for delamination (A320, 787 fuselage)
  Railroad: wheel and rail flaw inspection (automated at speed)
  Nuclear: reactor pressure vessel welds (mandatory, strict codes)
```

---

## Therapeutic Ultrasound

```
HIFU (High-Intensity Focused Ultrasound):

Focus high-intensity ultrasound beam deep in tissue → thermal ablation at focal point
Surrounding tissue: < 10°C temperature rise (transparent to beam)
Focal point: 55–80°C → protein denaturation → coagulative necrosis

APPLICATIONS:
• Uterine fibroids (FDA approved, non-invasive)
• Prostate cancer ablation
• Essential tremor (focused through skull via MRI guidance)
• Breast tumors (under investigation)
• Blood-brain barrier opening (low intensity, bubbles)

LITHOTRIPSY (SWL - Shock Wave Lithotripsy):
Not strictly ultrasound but acoustic: shock waves at 20–100 kPa pulses, 1000–3000 pulses
Focus on kidney stone → mechanical fragmentation → stone passes naturally
Non-invasive first-line treatment for kidney stones ≤ 2 cm

PHYSIOTHERAPY (diagnostic frequencies):
1–3 MHz, 0.5–3 W/cm² → thermal effects in soft tissue (tendon, ligament)
→ Increased blood flow, reduced muscle spasm
Evidence base is controversial compared to HIFU.
```

---

## Ultrasonic Cleaning and Sonochemistry

```
CAVITATION MECHANISM:

Ultrasound in liquid (usually 20–80 kHz) creates:
1. Rarefaction half-cycle: liquid tension → nucleation of microbubbles
2. Compression half-cycle: bubbles collapse violently

CAVITATION COLLAPSE:
• Bubble collapses in ~1 µs
• Localized temperature: ~5000 K (hot spot)
• Localized pressure: ~1000 atm
• Microjet: liquid jet at ~100 m/s toward surface

APPLICATIONS:
Ultrasonic cleaning:
  Cavitation knocks contaminants off surfaces
  Penetrates geometry that physical brushing can't reach
  Used for: semiconductor wafer cleaning, jewelry, surgical instruments

Sonochemistry:
  Cavitation drives unusual chemical reactions
  Synthesis of metal nanoparticles, emulsification
  Sono-Fenton reactions for water treatment
```

---

## Decision Cheat Sheet

| Application | Frequency | Reason |
|-------------|-----------|--------|
| Cardiac imaging | 2–5 MHz | Penetrate chest wall (5–20 cm depth) |
| Obstetric imaging | 3–7 MHz | Adequate penetration, good fetal resolution |
| Vascular superficial | 10–15 MHz | Fine resolution for superficial vessels |
| Skin imaging | 20–100 MHz | Sub-millimeter resolution, 1–5 mm depth |
| Industrial weld inspection | 2–10 MHz | Penetrate 20–100 mm steel |
| NDT thin composites | 5–15 MHz | Resolution for thin layers |
| Ultrasonic cleaning | 20–80 kHz | Optimal cavitation threshold |
| HIFU therapy | 0.5–5 MHz | Penetrate tissue, create focal heating |

---

## Common Confusion Points

**Ultrasound resolution is not fixed**: Axial resolution = c/(2·BW) depends on pulse bandwidth.
Higher center frequency → finer resolution, BUT higher frequency → higher attenuation → less depth.
Clinical systems trade off resolution for penetration by selecting transducer frequency.

**Impedance matching layers are critical**: PZT impedance ≈ 30 MRayl; tissue ≈ 1.5 MRayl.
Direct contact: Rₚ = ((30-1.5)/(30+1.5))² ≈ 0.82 → 82% reflected back!
One λ/4 matching layer with Z_match = √(Z_piezo · Z_tissue) ≈ 6.7 MRayl reduces this drastically.
Multiple quarter-wave layers → broad bandwidth transducers.

**Cavitation is the mechanism for many ultrasound effects**: Cleaning, sonochemistry, lithotripsy,
cell membrane permeabilization for drug delivery — all rely on cavitation, not just acoustic pressure.
Above cavitation threshold, all effects change dramatically. Below threshold, mainly thermal.

**Doppler angle matters enormously**: f_D ∝ cos(θ). At θ = 90° (beam perpendicular to flow):
cos(90°) = 0 → no Doppler signal. Must angle probe at 30–60° to flow for best measurement.
Automatic angle correction in clinical scanners assumes straight vessel over measured segment.
