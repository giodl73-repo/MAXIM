# Photography — Overview

## The Big Picture

Photography is **controlled light capture** — physically recording photon interactions with matter, then interpreting that record. The history is a sequence of progressively more sensitive, more stable, and more computationally tractable recording media.

```
ERA         RECORDING MEDIUM            KEY INNOVATION
────────────────────────────────────────────────────────────────────
1021        Pinhole + paper             Camera obscura (Ibn al-Haytham)
1826        Bitumen on pewter           Heliograph: first photograph (Niépce, 8h exposure)
1839        Silver iodide on silver     Daguerreotype: unique positive, no negative
1841        Silver bromide on paper     Calotype: negative → multiple positives (Talbot)
1851        Collodion on glass          Wet plate: sharper, faster — must develop wet
1871        Ag-Br gelatin on glass      Dry plate: store before/after exposure
1888        Ag-Br gelatin on paper roll Kodak roll film: democratization of photography
1925        35mm leica miniature        35mm standard: portability, large print from small neg
1935        3-layer dye-coupled film    Kodachrome: color reversal, archival stability
1970        Silicon photodiodes         CCD invention (Boyle & Smith, Bell Labs)
1975        Digital prototype           Kodak digital camera: 0.01MP, cassette output
1991        Kodak DCS-100               First commercial DSLR: 1.3MP on Nikon F3 body
2007        iPhone + computational      Multi-frame processing, AI pipeline, social share
2016+       Neural rendering, AI        Upscaling, style transfer, generative photography
```

---

## Technical Domains Map

```
┌────────────────────────────────────────────────────────────────────────┐
│                           PHOTOGRAPHY                                   │
├──────────────┬────────────────┬─────────────────┬─────────────────────┤
│   OPTICS     │   RECORDING    │   PROCESSING    │       OUTPUT        │
│              │                │                 │                     │
│ Thin lens    │  Film:         │  Chemical:      │  Print:             │
│ equation     │  Ag-halide     │  developer      │  optical enlarger,  │
│ f-number     │  crystals      │  stop bath      │  inkjet, laser      │
│ Depth of     │  latent image  │  fixer          │                     │
│ field        │  dye coupling  │  bleach (color) │  Display:           │
│ Aberrations  │                │                 │  monitor, projector │
│ MTF curves   │  Digital:      │  Digital RAW:   │                     │
│ AR coatings  │  CCD/CMOS      │  demosaicing    │  Computational:     │
│ Diffraction  │  Bayer CFA     │  white balance  │  AI upscaling       │
│ limit        │  pixel wells   │  tone curve     │  style transfer     │
│              │  ADC + ISO     │  noise redux    │  computational HDR  │
│              │  amplification │  sharpening     │  super-resolution   │
└──────────────┴────────────────┴─────────────────┴─────────────────────┘
```

---

## The Fundamental Exposure Triangle

All photography — film or digital — is governed by three coupled parameters:

```
                        EXPOSURE
                       /    |    \
                      /     |     \
             APERTURE    SHUTTER   ISO / FILM SPEED
             (f-stop)    SPEED     (sensor sensitivity)
                │           │             │
                ▼           ▼             ▼
            Controls     Controls      Controls
            light        motion blur   noise / grain
            volume +     and camera    floor and
            depth of     shake         dynamic range
            field

Stop doubling: each full stop doubles the light reaching the sensor

  f-stops:  f/1.4  f/2  f/2.8  f/4  f/5.6  f/8  f/11  f/16  f/22
  shutter:  1s  1/2  1/4  1/8  1/15  1/30  1/60  1/125  1/250  1/500  1/1000
  ISO:      50  100  200  400  800  1600  3200  6400  12800  25600

EV (Exposure Value) combines all three:
  EV = log₂(N²/t)  where N = f-number, t = exposure time
  ISO 100 is the reference; each ISO doubling = +1 EV of sensitivity
```

---

## The Photographic Chain — Where Quality Degrades

```
SCENE ILLUMINATION
     │
     │  Color temperature affects color balance:
     │  Candle 1800K / Tungsten 3200K / Daylight 5500K / Shade 7000K
     ▼
LENS
     │  Aberrations: chromatic (wavelength-dependent focus) → color fringing
     │               spherical → soft at wide apertures
     │               coma / astigmatism / field curvature → off-axis blur
     │  Diffraction: at small apertures (f/16+) → Airy disk limits resolution
     │  Flare: internal reflections reduce contrast (why multi-coating matters)
     │  MTF curve: how faithfully the lens transfers spatial frequencies
     ▼
RECORDING MEDIUM
     │  Film: grain size vs sensitivity tradeoff (faster = larger grains)
     │        exposure latitude = dynamic range (~11 stops for fine-grain neg)
     │  Digital: photon shot noise (√N — physics limit)
     │           read noise (electronics floor — lower on backside-illuminated CMOS)
     │           fixed pattern noise (pixel-to-pixel variation — calibrated out)
     │           ADC bit depth (12–14 bits typical RAW; 8 bits JPEG)
     ▼
PROCESSING
     │  Film: developer chemistry, agitation, temperature, time control
     │  Digital: demosaicing (reconstruct 3-channel image from Bayer mosaic)
     │           white balance (set color temperature of neutral)
     │           gamma curve / tone curve (log-linear mapping to display)
     │           noise reduction (spatial smoothing vs edge preservation tradeoff)
     ▼
OUTPUT
     Scene gamut >> display gamut >> print gamut
     Tone mapping: compress wide scene dynamic range to display range
     Color profile (ICC): device-independent color specification
```

---

## Sensor Size and Crop Factor

```
FORMAT SIZE COMPARISON (approximate sensor diagonal)
┌────────────────────────────────────────────────────────────────┐
│                                                                │
│  Medium Format  (54×40mm)  ████████████████████████████████  │
│                                                                │
│  Full Frame     (36×24mm)  ████████████████████              │
│                                                                │
│  APS-C          (24×16mm)  ████████████                      │
│                                                                │
│  Micro Four Thirds (17×13mm) ████████                        │
│                                                                │
│  1-inch         (13×9mm)   ██████                            │
│                                                                │
│  Smartphone     (~5×4mm)   ███                               │
│                                                                │
└────────────────────────────────────────────────────────────────┘

Crop factor = full-frame diagonal / sensor diagonal
  APS-C: ~1.5× (Nikon, Sony) or 1.6× (Canon)
  Micro Four Thirds: 2×
  1-inch: 2.7×

Why smaller sensors are noisier (same pixel count):
  Smaller sensor → smaller pixels → less light per pixel → worse SNR
  Shot noise ∝ √(photon count) → fewer photons → higher relative noise
  Why pixel count alone is misleading for low-light comparisons

Why depth of field is deeper on smaller sensors:
  To frame the same subject the same way, you use a shorter focal length
  Shorter lens → more depth of field at same aperture
  "Equivalent aperture" for DoF: f-stop × crop factor
  f/2.8 on Micro 4/3 ≈ f/5.6 on full-frame for depth of field
```

---

## Key Metrics

| Metric | Film equivalent | Digital equivalent | Limiting factor |
|--------|-----------------|--------------------|-----------------|
| **Resolution** | Film grain (lp/mm) | Megapixels | Lens MTF, diffraction, AA filter |
| **Dynamic range** | Exposure latitude (stops) | Stops (12–16 for modern sensors) | Shot noise vs read noise floor |
| **Sensitivity** | ISO/ASA rating | ISO (amplification) | Read noise, shot noise |
| **Color accuracy** | Dye metamerism, film stock | Color filter array + WB algorithm | Bayer interpolation, illuminant |
| **Sharpness** | Acutance (edge contrast) | Sharpening algorithms | MTF, pixel pitch, stabilization |
| **Temporal resolution** | Not applicable | Frame rate, rolling shutter | Data throughput, readout speed |

---

## Module Map

| Module | Topic | Key Concepts |
|--------|-------|-------------|
| `01-OPTICS-LENSES.md` | Lens physics | Thin lens, f-number, DoF, aberrations, coatings |
| `02-FILM-CHEMISTRY.md` | Silver halide | Latent image, Gurney-Mott, developer, Kodachrome |
| `03-DARKROOM.md` | Analog processing | Enlarger, zone system, dodge/burn, archival |
| `04-COLOR-PHOTOGRAPHY.md` | Color | Additive/subtractive, neg/reversal, ICC profiles |
| `05-CAMERA-TECHNOLOGY.md` | Camera mechanics | SLR, rangefinder, mirrorless, medium format |
| `06-DIGITAL-SENSORS.md` | CCD/CMOS | Bayer CFA, demosaicing, noise sources, dynamic range |
| `07-DIGITAL-WORKFLOW.md` | RAW processing | White balance, tone curves, color spaces, export |
| `08-COMPUTATIONAL-PHOTOGRAPHY.md` | Algorithms | HDR, focus stacking, AI pipeline, super-resolution |
| `09-HISTORY-ARC.md` | Timeline | Full arc: Niépce → Kodak → digital → computational |

---

## Bridges to Adjacent Fields

| Field | Connection |
|-------|-----------|
| `physics/` | Geometric optics, wave optics, quantum efficiency of photodetectors |
| `signal-processing/` | Sampling (Nyquist), convolution (PSF), Fourier analysis of MTF |
| `art-history/` | Photography as art movement: Pictorialism, Modernism, documentary |
| `computing/` | Digital imaging pipelines, JPEG/HEIF compression, GPU ISP |
| `natural-sciences/` (chemistry) | Silver halide photochemistry, developer reduction reactions |
| `colors/` (future) | Color spaces, gamut, perceptual color models (CIELAB, OKLCH) |

---

## Decision Cheat Sheet

| You want to understand | Go to |
|------------------------|-------|
| Why lenses are soft at edges or wide open | `01-OPTICS-LENSES.md` — MTF, aberrations |
| How film actually records and stores light | `02-FILM-CHEMISTRY.md` — Gurney-Mott |
| How Ansel Adams zone system worked | `03-DARKROOM.md` — zone system |
| Why color film is more complex than B&W | `04-COLOR-PHOTOGRAPHY.md` — dye coupling |
| Why mirrorless displaced DSLRs | `05-CAMERA-TECHNOLOGY.md` — mirror box problems |
| Why small sensors are noisier | `06-DIGITAL-SENSORS.md` — photon shot noise |
| What RAW vs JPEG actually encodes | `07-DIGITAL-WORKFLOW.md` |
| How iPhone beats physics with computation | `08-COMPUTATIONAL-PHOTOGRAPHY.md` |
| Full photographic history | `09-HISTORY-ARC.md` |

---

## Common Confusion Points

**f-stop is a ratio, not an absolute aperture diameter**
f/2.8 on a 50mm lens = 50/2.8 ≈ 18mm aperture. f/2.8 on a 200mm lens = 200/2.8 ≈ 71mm aperture. Same f-stop gives the same exposure regardless of focal length — that's the point of the ratio definition.

**Megapixels ≠ resolution in practice**
A 50MP smartphone sensor with 0.7µm pixels is diffraction-limited and lens-limited long before those pixels contribute. A 24MP full-frame sensor with 6µm pixels routinely outresolves it with a quality lens. Pixel count is necessary but not sufficient.

**ISO above native amplifies noise, not just signal**
At base ISO (typically 100–200), the sensor reads signal at its lowest noise floor. Every stop of ISO gain amplifies the signal — but the read noise floor is already baked in. "ISO invariance" (many modern sensors) means pushing exposure in post-processing is equivalent to raising ISO in-camera.

**RAW is not "unprocessed"**
RAW files have already been: demosaiced (Bayer interpolation), linearized, and had lens corrections applied (in many systems). They still require white balance, tone mapping, and color matrix decisions. The camera applies those decisions when generating a JPEG; RAW hands you those decisions.

**Depth of field is a perceptual specification, not an optical boundary**
There is no sharp boundary. DoF is defined by the "circle of confusion" — a blur diameter that appears sharp at a specific print size and viewing distance. On a 4" print at arms length, f/8 looks razor sharp throughout. On a 20×30" print, the same shot shows obvious fall-off. "Sharpness" is always relative to output size.
