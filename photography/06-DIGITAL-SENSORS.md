# Digital Sensors

## The Big Picture

A digital sensor converts photons into electrons, then into numbers. The fundamental limit is shot noise — photon statistics — not the technology. Everything else (read noise, quantization, demosaicing) is engineering around that limit. Understanding sensors means understanding why the photon count at each pixel is the fundamental quantity of interest.

```
SENSOR SIGNAL CHAIN:

  Photons arriving at sensor
         │
  Color filter array (Bayer mosaic) — absorbs 2/3 of photons!
         │
  Microlenses — concentrate light onto photodiode
         │
  Photodiode — electron-hole pair per photon absorbed
         │
  Full-well capacity — electron accumulator (10k–100k e⁻ before saturation)
         │
  Readout — CCD: charge transfer to edge; CMOS: per-pixel amplifier
         │
  Analog signal → ADC → digital value per pixel (12/14/16 bit)
         │
  Demosaicing — reconstruct full RGB from Bayer mosaic
         │
  Output: raw file (CFA data) or processed JPEG/HEIC

FUNDAMENTAL PERFORMANCE LIMITS:

  Shot noise:    σ_shot = √N  (where N = number of photons)
                → 10,000 photons → SNR = 100:1 → 40 dB
                → 100 photons → SNR = 10:1 → 20 dB
                UNAVOIDABLE — physics, not engineering

  Read noise:    Amplifier thermal/electronic noise at readout
                Modern CMOS: 1–3 electrons RMS
                → Only dominates when N << read_noise²
                → At base ISO with good exposure: shot noise dominates

  Dynamic range: log₂(full_well / read_noise) in stops
                Typical: 4,000 e⁻ well / 4 e⁻ read = 1,000:1 → ~10 stops
                Modern BSI CMOS: 14–15 stops at base ISO
```

---

## CCD vs CMOS Architecture

### CCD — Charge-Coupled Device

```
CCD OPERATION:

  Each pixel: photodiode accumulates charge during exposure
  Readout: charge clocked ("coupled") across chip row-by-row to output register
  Single output amplifier → low noise, uniform → historically superior quality

  ┌──────────────────────────────────┐
  │  Row 1: ●●●●●●●●●●●●●●●●●●●●●●  │
  │  Row 2: ●●●●●●●●●●●●●●●●●●●●●●  │  → clock ↓
  │  ...                             │
  │  Output register ← ← ← ← ← ← ←│  → single ADC
  └──────────────────────────────────┘

ADVANTAGES:
  Low noise (single, optimized output amplifier)
  Uniform response (same amplifier for all pixels)
  High fill factor (no in-pixel circuitry)

DISADVANTAGES:
  Slow readout (serial clocking — one row at a time)
  High power consumption (clocking all charge across chip)
  Smearing: if shutter fails or in video mode, charge from bright objects
    blooms vertically during readout
  Must complete full readout before starting next exposure
  Expensive to manufacture

HISTORICAL ROLE:
  Dominated serious digital photography 1991–2008 (Kodak DCS, Canon 1Ds era)
  Astronomical CCD still used (extreme low noise, deep cooling)
  Largely replaced by CMOS in consumer/pro cameras after 2008
```

### CMOS — Complementary Metal-Oxide-Semiconductor

```
CMOS ACTIVE PIXEL SENSOR:

  Each pixel contains: photodiode + amplifier + select transistor (3T or 4T design)

  PIXEL CIRCUIT (4T):
    ┌────────────────────────────┐
    │  PD → Transfer gate → FD  │  FD = floating diffusion (charge → voltage)
    │        (TX)          │    │
    │                      ▼    │
    │               Source follower amplifier
    │               → Row select → Column bus → Column ADC
    └────────────────────────────┘

  Each row can be read independently → parallel readout
  Each pixel has its own amplifier → potentially noisier (fixed-pattern noise)
  Modern: column-parallel ADCs → fast readout; on-chip processing

ROLLING vs GLOBAL SHUTTER:

  ROLLING SHUTTER (default CMOS):
    Rows exposed and read sequentially (top-to-bottom)
    Different rows captured at slightly different times
    Exposure time: each row starts ~5–10ms after previous
    → PROBLEM: fast-moving subjects distort ("jello effect" in video)
    → Sports: moving vertical bars skew diagonally
    → Benefits: simple; most pixels; silent (electronic only)

  GLOBAL SHUTTER:
    All pixels exposed simultaneously → captured at exactly same instant
    Requires: storage node per pixel (holds charge while others read)
    → More transistors → lower fill factor → smaller effective area → more noise
    → Or stacked BSI design to regain fill factor
    Nikon Z9, Sony A9 III (2024): full global shutter from stacked sensors
    → No mechanical shutter needed; 120fps; 1/16000s max; flash sync at any speed
```

### BSI — Backside Illumination

```
BSI vs FSI SENSOR STRUCTURE:

  FSI (Front Side Illuminated) — traditional:
    Wiring and transistors on same side as light path
    Metal interconnects partially block photons
    Fill factor ~50–65% at small pixel pitch

  BSI (Back Side Illuminated):
    Wafer flipped after fabrication — light enters from backside
    Wiring is behind photosensitive layer → doesn't block light
    Fill factor ~90%+
    → Better low-light performance for same pixel size
    Now standard for all modern smartphones and most cameras ≥ 2015

  STACKED BSI:
    BSI sensor wafer bonded to separate logic/DRAM wafer
    → In-sensor DRAM for ultra-fast readout buffer
    → Enables: 4K/120fps, real-time subject detection on chip,
               global shutter capability (A9 III, Z9)
    → Much faster readout → reduces rolling shutter artifacts
```

---

## Bayer Color Filter Array

<!-- @editor[bridge/P2]: The Bayer CFA is a spatial sampling problem — the sensor samples the color field at different spectral channels on a regular 2D grid, and demosaicing is signal reconstruction. The Nyquist connection is direct: the CFA pattern introduces a sampling frequency of N/2 for each color channel (where N = pixel pitch), so color information above that frequency aliases. Anti-aliasing filters exist to prevent moiré precisely because of this — they are optical low-pass filters. This bridge to sampling theory and signal reconstruction is not made, and a learner with signals background will immediately want it. -->
```
BAYER CFA PATTERN (Bryce Bayer, Kodak, 1976):

  R G R G R G
  G B G B G B
  R G R G R G
  G B G B G B
  R G R G R G

  Pattern: 2×2 quad: R G
                     G B

  Why 2 greens (RGGB, not RRGB or RGBRGB)?

  HUMAN VISUAL SYSTEM:
    Luminance sensitivity peaks at ~555nm (green)
    ~ 64% of luminous efficiency function is in green region
    Eye has far more M-cones (green) than L-cones (red) + S-cones (blue)
    Green pixels carry most of the luminance (perceived brightness) information

  RESOLUTION CONSEQUENCES:
    Full-color resolution is ~1/4 of total pixel count (without demosaicing)
    Luminance resolution ~1/2 of total (2 green channels)
    → Green channel provides edge/detail information; RGB provides color
    → This is why sharpness is driven by green channel

  ALTERNATIVES:
    X-Trans (Fujifilm): 6×6 pattern with more varied distribution → less moiré
    Quad Bayer (Sony, Samsung): 2×2 pixel-binning for ISO; full res for still
    Foveon (Sigma): three stacked photodiodes per pixel → no CFA, no demosaicing
      → True full-color at each pixel; but color separation issues + lower sensitivity

  QUANTUM EFFICIENCY:
    Blue filter: transmits 380–480nm → ~8–15% QE of unfiltered
    Green filter: transmits 490–580nm → ~20–30% QE
    Red filter: transmits 580–700nm → ~15–25% QE
    → Most photons are blocked by filters → efficiency loss is intrinsic to Bayer
```

---

## Demosaicing

```
DEMOSAICING PROBLEM:
  Each pixel has only one color value (R, G, or B)
  Must reconstruct full RGB for every pixel by interpolation
  → An inverse problem: underdetermined; many solutions; artifacts possible

BILINEAR INTERPOLATION (simplest):
  Each missing channel: average of nearest neighbors of that channel
  G at R pixel: average of 4 adjacent G pixels
  R at G pixel: average of 2 adjacent R pixels (horizontal or vertical)

  Simple; fast; but produces color fringing at sharp edges
  ("zipper artifacts" — false color at diagonal edges)

AHD — ADAPTIVE HOMOGENEITY-DIRECTED DEMOSAICING:
  Compute candidate interpolations in horizontal and vertical directions
  Compare "homogeneity" (color uniformity) of each direction
  At each pixel: use direction with higher homogeneity (more uniform color)
  → Adapts to local image structure; suppresses zipper artifacts
  Standard in many raw processors (dcraw, darktable)

AMaZE — ALIASING MINIMIZATION AND ZIPPER ELIMINATION:
  More sophisticated: uses frequency analysis + directional interpolation
  Multiple passes; iterative refinement
  Handles: diagonal edges, fine diagonal patterns, very fine detail
  Default in darktable, RawTherapee for high-quality output
  Slower but fewer artifacts; preserves fine detail better

DRIZZLE / PIXEL-SHIFT DEMOSAICING:
  Sensor shift: camera moves sensor by 1 pixel in 4 positions (or 16)
  → Each pixel captures all 4 Bayer samples → true full-resolution RGB
  → No demosaicing interpolation needed
  Olympus/OM System, Pentax, Sony: "pixel shift" mode
  Limitation: subject must be stationary (otherwise ghosting)

ARTIFACTS:
  False color (chroma noise, zipper): at high-frequency edges
  Moiré: periodic patterns + CFA pattern → interference → color moiré
    → Anti-aliasing (low-pass) filter: optical blur before sensor
    → Removes moiré but reduces resolution
    → Many modern cameras: no AA filter (rely on demosaicing algorithms)
```

---

## ISO, Noise, and Dynamic Range

### ISO as Analog Gain

```
ISO IN DIGITAL CAMERAS:

  ISO = analog amplification of the sensor's output signal

  Sensor → charge → ADC → value
  ISO 100: amplify × 1 → full well = 14 EV range
  ISO 800: amplify × 8 → signal boosted × 8 → BUT noise × 8 also
         → 3 stops less dynamic range
  ISO 6400: amplify × 64 → 6 stops less dynamic range than ISO 100

  NATIVE ISO:
    ISO where sensor operates at natural gain (no amplification)
    → Lowest read noise; full dynamic range
    Most cameras: native ISO 100 or 200

  DUAL NATIVE ISO:
    Some sensors: two native ISO values (e.g., 100 and 800)
    Switch between gain paths → preserves low read noise at both
    → Sony A7S III: native ISO 100 + 1280 → low noise at 1280

  INVARIANCE:
    ISO-invariant sensor: read noise so low that pushing in post = same as raising ISO
    → Advantage: shoot at ISO 100; recover shadows in post = same SNR as ISO 6400
    → Sony BSI sensors: highly invariant
    → Canon DSLR era sensors: less invariant (benefit to in-camera ISO raise)

NOISE TYPES:
  Shot noise: σ = √N — unavoidable; proportional to signal
  Read noise: amplifier electronics; measured in electrons; irreducible for given hardware
  Fixed pattern noise (DSNU): per-pixel offset variation; corrected by dark frame subtraction
  PRNU (Photo Response Non-Uniformity): per-pixel sensitivity variation; flat field correction
  Thermal noise (dark current): electrons generated by heat; reduced by cooling
```

### Dynamic Range

```
DYNAMIC RANGE DEFINITION:

  DR = ratio of maximum signal to minimum detectable signal
  In stops (EV): DR_stops = log₂(DR_ratio)

  Maximum signal: full-well capacity (saturation)
  Minimum signal: noise floor (typically read_noise × 1 or 3)

  EXAMPLE:
    Full well: 50,000 e⁻
    Read noise: 3 e⁻
    DR = 50,000 / 3 = 16,667 → log₂(16,667) = 14.0 stops

  MODERN SENSORS (2020+):
    Sony A7R V, Nikon Z8 at base ISO: ~15 stops (DxO measure)
    iPhone 14 Pro: ~13 stops (with multi-frame HDR)
    Film (RAW negative): ~13–14 stops

  DR vs ISO:
    Each stop of ISO gain: lose 1 stop of DR (from top — highlights clip)
    ISO 100 → 15 stops; ISO 1600 → 11 stops

  EXPOSURE TO THE RIGHT (ETTR):
    Maximize electrons in shadow areas → improve SNR in shadows
    Expose as bright as possible without clipping highlights
    → Pull down in post → better noise performance than underexposure + boost
    Physics: sensor SNR improves linearly with photons (√N), not with ISO

HIGH DYNAMIC RANGE (HDR) CAPTURE:
  Multi-exposure HDR: bracket 3–5 exposures; merge in software
  Dual-gain readout: each pixel read at two amplification levels simultaneously
    → Sony "SBI" (Simultaneous Bi-directional) — single exposure HDR
    → Apple ProRes LOG: similar approach in iPhone capture pipeline
  Pixel-binning + unbinning: combines near and far pixel states
```

---

## Sensor Size and Equivalence

```
SENSOR SIZE COMPARISON:

  Format              Size (mm)    Crop factor    Diagonal
  ─────────────────────────────────────────────────────────
  Medium format dig.  53 × 40      0.79×          66mm
  Full frame (FF)     36 × 24      1.0×           43mm (reference)
  APS-H               28 × 19      1.3×           34mm
  APS-C (Nikon/Sony)  23.5 × 15.6  1.5×           28mm
  APS-C (Canon)       22.2 × 14.8  1.6×           27mm
  Micro Four Thirds   17.3 × 13    2.0×           21.6mm
  1-inch              13.2 × 8.8   2.7×           15.9mm
  1/1.3" (pixel phone) 9.6 × 7.2  ~4.5×          12mm

EQUIVALENCE PRINCIPLE:
  To get same angle of view + same depth of field:
  Crop factor applies to both focal length AND aperture

  FF 50mm f/2 ↔ APS-C 33mm f/1.3 ↔ m4/3 25mm f/1 (same framing + DoF)
  FF 200mm f/2.8 ↔ APS-C 133mm f/1.8 (equivalent reach + isolation)

  WHY SMALLER SENSOR IS NOT "BETTER REACH":
  APS-C 300mm f/5.6 has same angle of view as FF 450mm
  But APS-C total aperture diameter = 300/5.6 = 53mm
  vs FF 450mm f/5.6 → aperture = 450/5.6 = 80mm → more light → better SNR
  The "reach" comes at a noise cost: fewer photons per pixel at equivalent scene

PIXEL PITCH AND DIFFRACTION:
  Smaller pixels: more resolution but reach diffraction limit sooner
  Diffraction limit: Airy disk diameter ≈ 2.44 × λ × f/#
  At f/8, λ = 550nm: Airy disk ≈ 10.7μm
  If pixel pitch = 5μm: diffraction-limited at f/4–f/5.6
  → Stopping down past diffraction limit: resolution DECREASES
  → High-resolution sensors (60MP+) with small pixels: avoid f/11+ for max sharpness

SENSOR SIZE AND LOW LIGHT:
  Same scene brightness → same photons per unit area → same per area
  But larger sensor collects more total photons → lower relative noise
  Full frame at f/1.4, 50mm: much more light than m4/3 at f/1.4, 25mm
  → Physics enforces: larger photosensitive area = better low-light, all else equal
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why does high ISO cause noise? | Amplification magnifies read noise; DR lost from top |
| Why can't you just boost shadows in post? | Shot noise already present; ISO-invariant sensors do allow it |
| Why 2 green pixels in Bayer? | Green carries luminance — resolution sensitive to green channel |
| Which demosaicing for best quality? | AMaZE (darktable) or custom manufacturer (Adobe) |
| Rolling vs global shutter: which is better? | Global for any fast motion; rolling fine for static |
| Why does APS-C have less background blur? | Smaller sensor = smaller aperture for same DoF = fewer photons |
| Diffraction: when does stopping down hurt? | Past f/8 for most modern sensors; f/5.6 for high-MP APS-C |
| Why does BSI improve low light? | Higher fill factor — more photons reach photodiode |
| Can a phone sensor match full frame? | No — photon count is a physics limit; computational can help but not overcome |

---

## Common Confusion Points

**ISO is gain, not sensitivity**
The sensor's physical sensitivity is fixed — it generates a certain number of electrons per photon at its native ISO. Increasing ISO amplifies the output signal, which amplifies noise equally. A sensor doesn't become "more sensitive" at ISO 6400; the signal is just turned up louder, along with the noise floor.

**Megapixels ≠ image quality**
A 60MP APS-C sensor with small pixels may have worse low-light performance than a 24MP full-frame sensor. Pixel count determines maximum print/crop resolution, not dynamic range, noise, or color accuracy. More pixels at the same sensor size means smaller pixels means more noise per pixel at any given aperture.

**Crop factor multiplies focal length for field of view only**
A 50mm lens on APS-C gives the field of view of a 75mm lens on full frame. But the physical focal length is still 50mm — depth of field is determined by physical focal length, aperture, and subject distance. To get equivalent DoF on APS-C, you need the same physical aperture diameter as on FF, which means a wider aperture f-stop.

**Rolling shutter "jello" is not a Bayer artifact**
Rolling shutter occurs because CMOS sensors read rows sequentially rather than all at once. It has nothing to do with the color filter pattern. The same artifact exists with monochrome CMOS sensors. It's an architecture issue, not a color issue.

**BSI sensors didn't eliminate pixel read noise — they reduced it**
BSI eliminated some photon blocking and improved fill factor. But the 3T/4T transistor read noise from the in-pixel amplifier still exists. Stacked BSI with column-parallel ADCs further reduced read noise. Modern 1–3 electron RMS read noise comes from the whole engineering package, not just the back-illumination geometry.
