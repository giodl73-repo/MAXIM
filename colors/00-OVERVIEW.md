# Color — Overview

## The Layered Problem

```
+------------------------------------------------------------------+
|                    WHAT COLOR ACTUALLY IS                        |
|                                                                  |
|  LAYER 1: PHYSICS                                                |
|  Electromagnetic radiation, 380–700 nm                          |
|  Spectral power distribution (SPD) of light source              |
|  Spectral reflectance of surface                                 |
|  → Objective, measurable, wavelength-specific                    |
|                                                                  |
|  LAYER 2: PHYSIOLOGY                                             |
|  Three cone types (L/M/S) in retina                             |
|  Opponent-channel encoding (red-green, blue-yellow, light-dark)  |
|  → 3D compression of infinite spectral information              |
|                                                                  |
|  LAYER 3: PERCEPTION                                             |
|  Brain constructs color experience                               |
|  Context-dependent (simultaneous contrast, constancy)            |
|  → Subjective, not measurable directly                           |
|                                                                  |
|  LAYER 4: NAMING                                                 |
|  Languages carve color space differently                         |
|  Berlin-Kay universal sequence across languages                  |
|  → Cultural, historically contingent                             |
|                                                                  |
|  LAYER 5: REPRODUCTION                                           |
|  Encoding for transmission (RGB, CMYK, ICC profiles)             |
|  Device-dependent → device-independent → device-dependent again  |
|  → Engineering approximation of perception                       |
|                                                                  |
|  KEY POINT: No layer maps cleanly onto the next.                 |
|  "Same color" means different things at each layer.              |
+------------------------------------------------------------------+
```

---

## Color Is Not a Property of Objects

```
COMMON MISCONCEPTION:
  "A red apple is red."

WHAT'S ACTUALLY HAPPENING:
  1. Illuminant emits spectral power distribution
  2. Apple surface absorbs most wavelengths, reflects 600–700 nm range
  3. Reflected light hits L/M/S cones differently
  4. Visual system processes LMS signals via opponent channels
  5. Brain constructs the experience "red"

  Change any of these and "red" changes:
  • Different illuminant (sodium street lamp → apple looks orange-brown)
  • Different observer (red-green color blindness → color different)
  • Different context (red next to yellow looks different from red next to green)

METAMERISM:
  Two surfaces with different spectral reflectance curves
  that appear IDENTICAL under one light source
  but DIFFERENT under another.
  → Color is always a three-way interaction: source × surface × observer
```

---

## Why Some Colors Have No Wavelength

```
SPECTRAL COLORS (exist as single wavelengths):
  Red    ~700 nm
  Orange ~620 nm
  Yellow ~580 nm
  Green  ~530 nm
  Cyan   ~490 nm
  Blue   ~470 nm
  Violet ~420 nm

NON-SPECTRAL COLORS (require mixing, exist only in perception):
  Magenta/pink: stimulate L and S cones but NOT M
    → No single wavelength does this
    → No "magenta" in a rainbow
    → Brain creates it as complement of green

  Purple: blue-violet end of spectrum + red end
    → Short and long wavelength together
    → The "line of purples" on CIE diagram — never in spectrum

  White: all wavelengths together
  Black: absence of light (or very low relative luminance)
  Brown: low-luminance orange (no "brown" photons exist)
    → Brown only exists in context of surrounding brighter colors
    → A brown object in total darkness would appear orange

IMPLICATION:
  The color wheel (rainbow → bent into circle + magenta filling the gap)
  is a human perceptual construct, not physics.
```

---

## The Visible Spectrum in Context

```
ELECTROMAGNETIC SPECTRUM:
  Radio → Microwave → IR → [VISIBLE] → UV → X-ray → Gamma

  Visible: ~380 nm (violet) to ~700 nm (red)
  ONE OCTAVE: 700/380 ≈ 1.84 (less than an octave of EM frequency)
  Humans are sensitive to ~0.00000035% of the EM spectrum

OTHER SPECIES:
  +-------------------+-----------------------------+
  | Species           | Sensitivity                 |
  +-------------------+-----------------------------+
  | Honeybee          | UV to red (no far red)      |
  | Pit viper         | Near-infrared (heat pits)   |
  | Mantis shrimp     | 16 photoreceptor types      |
  | Pigeon            | Tetrachromat + UV           |
  | Dog               | Dichromat (blue-yellow)     |
  | Deep-sea fish     | Shifted toward blue         |
  +-------------------+-----------------------------+

  "Visible" = visible to humans; the universe doesn't know about it.
```

---

## Color Science Architecture

```
COLORIMETRY (measurement and specification):
  Spectrophotometry → SPD → tristimulus XYZ
  CIE 1931 Standard Observer model
  → The physics-to-numbers step

COLOR SPACES (organizing the numbers):
  CIE XYZ → CIE xy chromaticity → CIELAB → sRGB
  Each transformation: different purpose
  → The numbers-to-geometry step

COLOR APPEARANCE MODELS:
  CIECAM02 and successors
  Account for: adaptation, surround, luminance level
  → The geometry-to-perception step

IMAGE COLOR MANAGEMENT:
  ICC profiles: describe what "red" means for THIS device
  Color management system (CMS): converts between profiles
  Rendering intents: how to handle out-of-gamut colors
  → The cross-device consistency step

WHAT THIS MEANS IN PRACTICE:
  "Blue" on your monitor ≠ "blue" on a different monitor
  unless both are calibrated to a shared standard (e.g., sRGB, D65 white)
  ICC color management is the solution
```

---

## Color Systems — Which to Use When

```
+------------------------+------------------------------------------+
| SYSTEM                 | USE FOR                                  |
+------------------------+------------------------------------------+
| Munsell (1905)         | Paint mixing, soil science, color        |
|                        | research; perceptually uniform spacing;  |
|                        | 3D: Hue / Value / Chroma                 |
+------------------------+------------------------------------------+
| CIE XYZ / xyY (1931)  | Measurement, device characterization;   |
|                        | foundation for everything else;          |
|                        | NOT perceptually uniform                 |
+------------------------+------------------------------------------+
| CIELAB / L*a*b* (1976)| Color difference measurement (ΔE);      |
|                        | industrial tolerancing; perceptually     |
|                        | (approximately) uniform                  |
+------------------------+------------------------------------------+
| sRGB                   | Screens, web, consumer images;          |
|                        | default assumption for most digital      |
|                        | content; ~35% of CIE gamut               |
+------------------------+------------------------------------------+
| Display P3             | Modern Apple devices, HDR content;       |
|                        | ~26% wider gamut than sRGB               |
+------------------------+------------------------------------------+
| Pantone PMS            | Cross-company color communication;       |
|                        | brand colors; spot ink specification;    |
|                        | proprietary (licensing required)         |
+------------------------+------------------------------------------+
| RAL                    | Industrial/construction in Europe;       |
|                        | metal, powder coating, facades           |
+------------------------+------------------------------------------+
| NCS                    | Scandinavian architecture/design;        |
|                        | based on opponent-color perception model |
+------------------------+------------------------------------------+
| CMYK                   | Commercial print (offset, digital);      |
|                        | device-dependent (varies by substrate)   |
+------------------------+------------------------------------------+
```

---

## Module Map

```
colors/
├── 00-OVERVIEW.md        ← you are here
├── 01-COLOR-PHYSICS.md   EM radiation, absorption, structural color,
│                         blackbody radiation, Rayleigh scattering
├── 02-VISION-PERCEPTION.md  Cone types, opponent channels, metamerism,
│                            simultaneous contrast, color constancy, blindness
├── 03-COLOR-SYSTEMS.md   Munsell, CIE 1931, CIELAB (ΔE), sRGB,
│                         Display P3, Pantone, RAL, NCS
├── 04-COLOR-NAMING.md    Berlin-Kay universal sequence, wine-dark sea,
│                         Sapir-Whorf, focal colors, Himba case
├── 05-HISTORICAL-SHADES.md  Mauve (Perkin 1856), magenta, gamboge,
│                            chartreuse, puce, vermilion, indigo
├── 06-MIXING-THEORY.md   Additive vs subtractive, CMYK halftone,
│                         RYB artist model, optical mixing, gamut
├── 07-PSYCHOLOGY-CULTURE.md  Cross-cultural symbolism, marketing,
│                             synesthesia, Luscher, ecological valence
├── 08-COLOR-IN-NATURE.md Structural color (morpho/opal), melanin/
│                         carotenoids, bioluminescence (GFP), camouflage
└── 09-DIGITAL-COLOR.md   Bit depth, gamma, ICC profiles, HDR (PQ/HLG),
                          CSS color spaces, PBR rendering
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Is color a property of objects? | No — it's a three-way interaction: light source × surface reflectance × observer visual system |
| Why does magenta not appear in a rainbow? | No single wavelength stimulates L+S cones without M — magenta is a non-spectral color, existing only in perception |
| Why are there color standards at all? | Metamerism: colors match under one light source but not another — without standards, "matching" is device/illuminant-dependent |
| What's the difference between hue and chroma? | Hue = which color family (red/blue/green). Chroma = saturation/purity (gray=0, vivid=high). Munsell separates these from Value (lightness). |
| CIE 1931 vs CIELAB — what's the difference? | CIE 1931 maps device primaries; not perceptually uniform. CIELAB derived from XYZ specifically to make equal distances = equal perceived differences. Use Lab for ΔE color difference. |
| sRGB vs Display P3 — when does it matter? | P3 has more saturated greens/reds. Matters for UI on Apple devices, video, photography. For web serving general audiences: sRGB is safe default. |
| What is ΔE? | CIE color difference formula. ΔE < 1: barely perceptible. ΔE 1-2: acceptable. ΔE > 5: obvious. CIEDE2000 is current best version. |

---

## Common Confusion Points

**The rainbow doesn't contain all colors:** The rainbow (spectral colors) is missing magenta, pink, brown, and white. These require mixing wavelengths — they're "extra-spectral." Newton added indigo to get seven colors (matching musical notes) — most modern color scientists consider indigo a naming artifact.

**Subtractive doesn't mean "worse":** Subtractive mixing (paint) isn't an inferior version of additive (light). They're different physical systems. Paint pigments absorb light; screens emit it. Starting conditions differ (white paper vs black screen).

**sRGB isn't the only "correct" color space:** sRGB is a standard, not the color space. It covers only ~35% of what human vision can see. ProPhoto RGB covers ~91%. The right choice depends on the workflow and output target.

**Color blindness isn't seeing in black and white:** Red-green color blindness (most common) means reduced discrimination, not absence. Protan/deuteran dichromats see a reduced gamut, not grayscale. Complete achromatopsia (grayscale) is extremely rare.
