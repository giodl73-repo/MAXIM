# Digital Workflow

## The Big Picture

The digital photography workflow is a signal chain from captured photons to final output. Every step is a transformation of image data, and understanding what information exists at each stage — and what irreversibly destroys it — determines the quality ceiling of the final image. The critical insight is that RAW preserves all captured information; everything downstream narrows the information available to you.

```
DIGITAL WORKFLOW PIPELINE:

  CAPTURE
  ┌──────────────────────────────────────────────────────────────┐
  │ Sensor → Bayer CFA → ADC → Linear RAW data (12/14 bit)      │
  │ White balance tag, exposure metadata written (not applied)   │
  └────────────────────────────────┬─────────────────────────────┘
                                   │ RAW file (.CR3, .NEF, .ARW, .DNG)
  ┌──────────────────────────────────────────────────────────────┐
  │ RAW PROCESSING (Lightroom, Capture One, darktable, RawTherapee)│
  │  1. White balance → chromatic adaptation → neutral grays      │
  │  2. Demosaicing → full RGB at every pixel                     │
  │  3. Tone curve → map linear scene values to perceptual space  │
  │  4. Color space conversion → sRGB / AdobeRGB / ProPhoto       │
  │  5. Noise reduction → luminance NR + color NR                │
  │  6. Output sharpening → USM or deconvolution                 │
  └────────────────────────────────┬─────────────────────────────┘
                                   │ Processed image (16-bit TIFF)
  ┌──────────────────────────────────────────────────────────────┐
  │ EDITING (Photoshop, Affinity Photo, Pixelmator)               │
  │  Local adjustments, compositing, retouching                   │
  └────────────────────────────────┬─────────────────────────────┘
                                   │
  ┌──────────────────────────────────────────────────────────────┐
  │ OUTPUT                                                        │
  │  Screen: sRGB JPEG/HEIC (8-bit; ICC embed)                   │
  │  Print: CMYK conversion; soft proof → printer profile TIFF    │
  │  Archive: original RAW + sidecar (.xmp) or catalog backup     │
  └──────────────────────────────────────────────────────────────┘

KEY PRINCIPLE:
  Linear RAW → non-linear output
  All RAW processors do the same fundamental operations
  Differences: algorithms, color science, default rendering, workflow philosophy
```

---

## RAW Format

### What RAW Actually Contains

```
RAW FILE CONTENTS:
  Unprocessed (or minimally processed) sensor data:
  → Bayer CFA values: one color channel per pixel, linear luminance
  → Typically 12 or 14-bit integer values (4096 or 16384 levels)
  → Metadata: camera model, lens, shutter speed, aperture, ISO, GPS
  → White balance setting (recorded but NOT baked in — can be changed)
  → JPEG preview (embedded; used by card readers/OS, not actual image data)
  → Color matrix: transforms sensor's native primaries to camera color space
  → Tone curve: recorded (if applied to JPEG preview) but raw data is always linear

  WHAT IT IS NOT:
  Not "unprocessed" — it IS processed:
    Demosaicing not yet done
    But: dark current subtraction, defective pixel correction, sometimes lens correction
    "Raw" = sensor CFA values with minimal processing, not zero processing

PROPRIETARY vs DNG:
  Proprietary formats: .CR3 (Canon), .NEF (Nikon), .ARW (Sony), .RAF (Fuji), .ORF (Olympus)
  → Manufacturers can change format; old software may break
  → Undocumented internal structures in some

  DNG (Digital Negative — Adobe, 2004):
  → Open, documented specification
  → Embeds proprietary RAW data inside DNG container, or converts to DNG data
  → Lightroom: can convert to DNG at import (lossless; adds validation checksum)
  → Pros: future-proof; no sidecar; verified integrity
  → Cons: lossy conversion possible; Adobe controls spec; camera maker RAW may have private data

BIT DEPTH AND DYNAMIC RANGE:
  12-bit: 4,096 levels; ~12 stops possible; compressed RAW (cRAW) often 12-bit
  14-bit: 16,384 levels; ~14 stops; standard lossless RAW for most modern cameras
  16-bit: 65,536 levels; possible in some medium format + Phase One → extra shadow detail
  → 14-bit vs 12-bit: ~2 stops more shadow recovery; visible in extreme edits
  → Bit depth is the ceiling — actual DR still limited by sensor's shot noise floor

LINEAR DATA:
  Sensor response is approximately linear: 2× photons = 2× signal
  Human perception is not linear (logarithmic — Weber-Fechner)
  → Linear data: half the tonal levels are in the top stop of exposure
  → Histogram in linear space looks very dark image even if well-exposed
  → RAW processors apply a tone curve to map linear → perceptual (gamma encoding)
  → This is why "RAW files look flat" until the tone curve is applied
```

---

## White Balance

```
WHAT WHITE BALANCE IS:
  Adjustment of R, G, B channel multipliers to make a neutral scene neutral
  A light source with color temperature 5500K contains more blue than red photons
  → Daylight-balanced sensor captures: blue slightly elevated, red slightly lower
  → White balance: multiply R × 1.8; G × 1.0; B × 0.8 (example) → white looks white

CHROMATIC ADAPTATION:
  HVS (human visual system) automatically adapts to illuminant color
  → Tungsten light (2700K): we still see white paper as white
  → Camera records absolute spectral distribution → needs correction
  Bradford transform: used in ICC profiles to model chromatic adaptation
  Von Kries transform: simpler diagonal channel scaling (what in-camera WB does)

COLOR TEMPERATURE (Kelvin):
  Theoretical "black body radiator" temperature that produces a given light color
  Lower K → warmer (orange/red): candle 1800K; tungsten 2700K; studio tungsten 3200K
  Higher K → cooler (blue): overcast sky 6500K; blue sky shade 7000–12000K
  Daylight: ~5500–6500K
  Flash: 5500K (designed to match daylight)

  TINT (green-magenta axis):
    Perpendicular to the Kelvin axis
    Fluorescent: green spike → tint correction needed
    LED: variable; often requires both K + tint correction

DAYLIGHT (D50 vs D65):
  D50 (5000K): print industry reference illuminant (matches tungsten viewing booth)
  D65 (6500K): digital display, sRGB, broadcast reference
  → Why images look different on screen vs print: different reference illuminant
  → Soft proofing simulates paper+ink under D50 on your D65 screen

WHITE BALANCE IN RAW PROCESSING:
  Changing WB in RAW: zero quality cost (just changes multipliers on linear data)
  Changing WB in JPEG: quality cost (gamut clipping possible; 8-bit already)
  → This is one of the primary reasons to shoot RAW: WB is fully revisable

AUTO WHITE BALANCE (AWB):
  Camera analyzes scene → estimates illuminant → applies correction
  Modern AWB (AI-based): 90%+ reliable under mixed lighting
  Failure modes: extreme color casts; unusual illuminants; intentional color lighting
```

---

## Tone Curves

```
LINEAR vs PERCEPTUAL:
  Sensor output: linear (photon count)
  Display and print: require gamma-encoded data
  Human perception: approximately logarithmic (1 stop = 2× light → equal perceptual step)

GAMMA ENCODING:
  sRGB transfer function (IEC 61966-2-1):
    For V ≤ 0.0031308: L = 12.92 × V  (linear segment near black)
    For V > 0.0031308: L = 1.055 × V^(1/2.4) − 0.055  (power curve)
    Approximately γ = 2.2

  Purpose: allocate 8-bit encoding efficiently for perceptual uniformity
    → Linear: half of 256 values in top stop (overkill in highlights; banding in shadows)
    → Gamma-encoded: values spread more uniformly across perceived tonal range

S-CURVE (creative tone curve):
  Standard camera rendering: slight S-curve applied to linear data
  → Shadows: lifted slightly (raised contrast)
  → Midtones: steeper (increased local contrast → snappy)
  → Highlights: rolled off (shoulder → preserves highlight texture)

  LOG GAMMA (video):
    Flattened S-curve; preserves maximum dynamic range for grading
    → S-Log3 (Sony), Log-C (Arri), Canon Log 3
    → "Flat" looking until LUT applied in grading
    → More stops in highlights + shadows at cost of appearance

LIGHTROOM TONE CONTROLS:
  Exposure: shifts entire curve up/down (multiply all values by a constant)
  Highlights: affects upper portion of curve (compress/expand top 2 stops)
  Shadows: lifts or drops lower portion
  Whites: clips point (sets white clipping)
  Blacks: sets black clipping point
  → All: adjustments to the shape of the tone curve applied to linear data
  → Parametric curve vs point curve: same result; different UI metaphor

CLIPPING:
  Highlight clipping: value exceeds maximum → 255 (white) → detail gone
  Shadow clipping: value below minimum → 0 (black) → detail gone
  RAW: can recover ~1–2 stops of clipped highlights (data still in other channels)
  JPEG: no recovery — data discarded at in-camera processing
```

---

## Noise Reduction

```
NOISE TYPES IN DIGITAL IMAGES:
  Luminance noise: random variation in pixel brightness → film grain analog
                   Looks like: gray speckle; still gives texture impression
  Color (chroma) noise: random variation in color at each pixel
                   Looks like: colored blotches (red, green, teal spots)
                   More objectionable than luminance noise; eliminated first

NOISE REDUCTION ALGORITHMS:

  SPATIAL NR (traditional):
    Gaussian blur: weighted average of neighboring pixels → reduces noise but blurs
    Median filter: replaces each pixel with median of neighborhood → preserves edges better
    Bilateral filter: weight by spatial distance AND intensity distance
      → Blurs noise but preserves sharp edges (used in Lightroom's older NR)
    Luminance NR in Lightroom: bilateral + edge-aware filtering

  NLM — Non-Local Means:
    For each pixel: search entire image for similar patches → average them
    → Far better than local filters for texture preservation
    Computationally expensive; widely used in RAW software

  FREQUENCY DOMAIN NR:
    Wavelet decomposition: separate image into frequency bands
    → Apply thresholding in frequency domain (noise has different spectral signature)
    → Used in: ACR/Lightroom Enhance NR, RawTherapee wavelet NR

  AI / CNN NOISE REDUCTION:
    Deep learning trained on noisy/clean image pairs
    → Learns to remove noise while preserving texture
    Lightroom AI Denoise (2023): uses ML model → dramatically better than traditional
    Topaz DeNoise AI, DxO DeepPRIME: standalone products
    → Can recover 2–3 stops of effective ISO: ISO 25600 → looks like ISO 3200

COLOR NR:
  Much simpler: chroma noise is at high spatial frequencies
  → Low-pass filter (blur) the ab channels in Lab color space
  → Doesn't reduce perceived sharpness (luminance = sharpness; chrominance = color)
  → Even aggressive chroma NR: minimal quality cost

NR WORKFLOW:
  Color NR first: remove blotches → doesn't affect edge detection
  Luminance NR second: tune to preserve texture vs. remove grain
  Sharpening: always after NR (NR degrades sharpness → restore with USM)
```

---

## Output Sharpening

```
WHY IMAGES NEED SHARPENING:
  Multiple softening sources in the capture chain:
    Anti-aliasing filter: optical blur (intentional)
    Lens diffraction: unavoidable at small apertures
    Camera motion / subject motion (even slight)
    Bayer demosaicing: introduces slight softness
    Focus imprecision: even slightly off-plane blur
  → Capture sharpening: compensate for these
  → Output sharpening: compensate for print/display resizing

USM — UNSHARP MASK:
  Name from darkroom technique: subtract blurred (unsharp) copy from original
  → Residual = edges (high-frequency content)
  → Add residual back (scaled) → edge enhancement

  Three parameters:
    Amount: how much to boost edges (0–500%)
    Radius: size of detail being sharpened (pixels) — match to subject texture scale
    Threshold: minimum contrast for sharpening (avoid sharpening noise)

  Typical capture sharpening (in RAW developer):
    Amount: 50–100; Radius: 0.6–1.0; Threshold: 5–10

DECONVOLUTION SHARPENING:
  Instead of boosting edges: reverse the blur mathematically
  Requires estimating the PSF (point spread function) of the blur source
  More sophisticated than USM; restores information rather than just boosting contrast
  Lightroom AI Masking + Sharpening: uses lens profile → deconvolution-based
  Better than USM for: diffraction blur, lens optical aberrations

HIGH-PASS SHARPENING:
  Photoshop: duplicate layer → High Pass filter (extracts edges) → overlay blend
  Gives more control over which edges; non-destructive when done on separate layer

OUTPUT SHARPENING:
  Screen: sharpen for 72–96ppi; typically lighter sharpening
  Print: sharpen more aggressively (print dots are smaller than screen pixels)
  Resize before final sharpen: scale to output size first, then apply USM
  → Sharpening at print size vs. at capture size: very different amounts needed

SHARPENING ARTIFACTS:
  Halos: white/dark rings at edges (too high amount/radius)
  Noise amplification: sharpening amplifies noise (NR before sharpen)
  Texture damage: over-sharpening smooth gradients → posterization artifacts
```

---

## Color Spaces in Digital Workflow

```
COLOR SPACE COMPARISON:

  Space       Gamut           Bit depth    Use
  ──────────────────────────────────────────────────────────────
  sRGB        Small (~35% vis) 8-bit OK    Web, social, consumer display
  AdobeRGB    Medium (~50%)    16-bit req  Pro print; saturated colors
  ProPhoto    Very large (~90%) 16-bit req  Editing space; never for output
  Display P3  Medium-large     10-bit      iPhone, Apple displays, newer HDR
  Rec.2020    Huge (~76%)      10/12-bit   HDR broadcast; future displays

  Visible gamut: ~100% (cannot be fully represented in any digital space)
  Most printers: exceed sRGB in yellow/green; fall short in blue/violet

WORKING SPACE SELECTION:
  Edit in: ProPhoto (Lightroom default) or AdobeRGB — preserve maximum data
  Output for web: convert to sRGB — clip or compress out-of-gamut colors
  Output for print: convert to printer profile — either AdobeRGB → CMYK or direct

GAMUT CLIPPING vs GAMUT MAPPING:
  Clipping: colors outside destination gamut → snapped to boundary
    → Saturated reds on screen → red blob on paper
    → Perceptual intent: tries to compress all colors proportionally
  Perceptual rendering intent: squeezes entire gamut into smaller space
    → Relative relationships preserved; absolute values shift
  Relative colorimetric: clips out-of-gamut; maps in-gamut colors exactly
    → Best for images mostly within gamut; accurate for most colors

JPEG ENCODING:
  sRGB JPEG is the standard: 8-bit per channel; ~16.7M colors
  YCbCr color model: Y (luminance), Cb/Cr (chrominance)
  Chroma subsampling: 4:2:0 (JPEG default) → Cb/Cr sampled at half resolution
    → Loses color resolution at fine detail → color fringing at sharp edges
    → 4:4:4: no subsampling; used in high-quality JPEG settings
  DCT compression artifacts: 8×8 pixel blocks → "blockiness" at high compression
    → Ringing: artifact around sharp edges (Gibbs phenomenon)
    → Quality 90+: usually imperceptible; quality <60: significant artifacts
```

---

## Decision Cheat Sheet

| Goal | Recommendation |
|------|----------------|
| Maximum editing latitude | Shoot RAW 14-bit; edit in ProPhoto; output sRGB |
| Fix white balance perfectly | Change in RAW; no quality penalty |
| Reduce high-ISO noise | AI denoise (Lightroom/Topaz) → 2–3 stop equivalent gain |
| Sharpen for web output | USM after resize: Amount 80, Radius 0.5, Threshold 3 |
| Sharpen for print | More aggressive; deconvolution preferred; after resize to print size |
| Web output | Convert to sRGB; 8-bit JPEG quality 90; embed color profile |
| Professional print | Export 16-bit TIFF AdobeRGB; convert to printer profile in RIP |
| Archive images | Keep original RAW + .xmp sidecar; or embed adjustments in DNG |
| Recover blown highlights | Only works in RAW; 1–2 stops possible if not all channels clipped |

---

## Common Confusion Points

**White balance on RAW has zero cost; on JPEG it's destructive**
A RAW file stores WB as metadata: a tag saying "multiply R by X, B by Y." Changing this in a RAW processor costs nothing — the original linear data is untouched. Once baked into JPEG (or HEIC/TIFF), white balance is applied via channel multiplication and the result is quantized to 8 bits. Correcting WB after JPEG conversion clips data and introduces quantization error.

**RAW files are not unprocessed — they're minimally processed**
Every RAW file has undergone: hot pixel correction, dark frame subtraction (or similar), possibly lens correction data embedding, and metadata application. "RAW" means the Bayer CFA data is preserved and demosaicing/tone curve application happens in software — not that zero processing has occurred in-camera.

**ProPhoto RGB is for editing, not delivery**
ProPhoto's gamut is larger than most monitors and all printers can display/reproduce. Working in ProPhoto preserves color information that exists in the sensor's capture but would be clipped in sRGB. However, ProPhoto 8-bit has obvious banding — you must use 16-bit with ProPhoto. Never save a JPEG in ProPhoto for web use: a viewer without an embedded profile will interpret the values as sRGB, causing washed-out desaturated colors.

**Output sharpening is different from capture sharpening**
Capture sharpening compensates for sensor/lens-introduced softness — should be subtle, targeted at fine texture. Output sharpening is applied at final delivery size for the output medium (screen/print). Sharpening for an 8×10 print is very different from sharpening for a web-sized image — the print has much higher PPI and needs stronger sharpening.

**JPEG "quality 100" is not lossless**
JPEG is intrinsically lossy due to DCT block compression and chroma subsampling. Quality 100 in Photoshop means "maximum quality JPEG" but still applies the DCT transform, which introduces quantization error (very small at Q100, but present). Lossless formats: TIFF (LZW), PNG (8-bit), DNG (lossless) — use these for archival editing masters.
