# Color Systems — Munsell, CIE, CIELAB, sRGB, Pantone

## The Big Picture

```
+------------------------------------------------------------------+
|           COLOR SYSTEMS: PURPOSE AND GENEALOGY                   |
|                                                                  |
|  PERCEPTUAL SYSTEMS (organized by how humans see)                |
|  Munsell (1905): 3D Hue/Value/Chroma — art/soil/design          |
|  NCS (1979): opponent-color model — Scandinavian architecture    |
|                                                                  |
|  MEASUREMENT SYSTEMS (physics → numbers)                         |
|  CIE XYZ (1931): tristimulus values from color-matching funcs    |
|  CIE xyY (1931): chromaticity + luminance (2D horseshoe diagram) |
|                                                                  |
|  UNIFORM PERCEPTUAL SPACES (physics → equal-step perception)     |
|  CIELAB (1976): L*a*b*, ΔE color difference standard            |
|  CIELUV (1976): alternative, better for self-luminous displays  |
|  OKLab (2020): improved uniform space (modern CSS default)       |
|                                                                  |
|  DEVICE SPACES (encode for specific output hardware)             |
|  sRGB (1996): screens, internet — D65 white, γ=2.2              |
|  Adobe RGB (1998): print preparation — wider gamut               |
|  Display P3 (2015): modern displays — ~26% wider than sRGB       |
|  Rec.2020 (2012): UHD/HDR standard — 76% of CIE gamut           |
|                                                                  |
|  INDUSTRY COMMUNICATION SYSTEMS (physical sample catalogs)       |
|  Pantone PMS: spot inks, proprietary                             |
|  RAL: European industrial/construction                           |
|  NCS: Scandinavian design                                        |
+------------------------------------------------------------------+
```

---

## Munsell Color System (1905)

### Structure

```
ALBERT H. MUNSELL (1858–1918): American artist and art teacher
Published "A Color Notation" (1905) — the first systematic perceptual color system

THREE AXES:

HUE (H): which color family
  5 principal: R, Y, G, B, P
  5 intermediate: YR, GY, BG, PB, RP
  → 10 major hues, each subdivided 1-10 (so 5R, 10R, etc.)
  → 100 hue steps total (40 are commonly used)
  Arranged in a circle; opposite hues are complementary

VALUE (V): lightness
  0 = ideal black (no light)
  10 = ideal white (all light)
  Scale is visually equal-interval
  Grays: N 0/ through N 10/

CHROMA (C): saturation/purity (distance from neutral gray)
  0 = neutral gray (no saturation)
  Maximum varies by hue and value (not uniform)
  → Yellows: chroma can reach ~16
  → Blues: chroma stops at ~10 for mid-value
  → Shape of Munsell solid is IRREGULAR (not sphere or cylinder)
     because achievable chroma is hue- and value-dependent

NOTATION: H V/C
  Example: 5R 4/14 = hue 5R (pure red), value 4, chroma 14 (vivid red)
           10GY 7/4 = yellow-green, light, moderate saturation
           N 5/ = neutral gray, mid-lightness
```

### Why Munsell Matters

```
PERCEPTUAL SPACING:
  Munsell was the first to achieve equal perceived color steps
  (empirically derived from observer experiments, not calculation)
  → Moving one unit in any direction = equal perceived change
  This is the original data set that CIE later tried to formalize

APPLICATIONS:
  Soil science: Munsell Soil Color Charts (still standard in pedology)
  Paint industry: historical paint matching system
  Color research: defining "color categories" experimentally
  Forensics: tooth/skin color matching
  Archaeology: ceramic color description

MUNSELL vs OTHER SYSTEMS:
  Munsell value 0-10 ≠ CIE L* 0-100 (but related: L* ≈ 10×V roughly)
  Munsell chroma ≠ CIELAB chroma C*ab (different scale)
  Munsell hue circle ≠ CIELAB hue angle (different distortions)
  → Convert between via lookup tables (CIE H 18-1983 provides mappings)
```

---

## CIE 1931 Standard Observer

### The Color Matching Experiment

```
EXPERIMENT (Guild, Wright, 1920s):
  Human observers adjusted 3 primaries (R, G, B at fixed wavelengths)
  to match monochromatic test light at each wavelength
  → Records: how much R, G, B needed to match 1 watt of each wavelength

  PROBLEM: Some wavelengths require "negative" amounts of R primary
  (so vivid cyan can't be matched without "subtracting" red)
  → No physical meaning; mathematical artifact

CIE 1931 FIX:
  Transform to fictional XYZ primaries (outside physical spectrum)
  → All real colors have X, Y, Z ≥ 0
  → Y is defined to equal luminance (useful secondary property)

  Color matching functions:
  x̄(λ): X-primary response curve
  ȳ(λ): Y-primary response curve (= luminous efficiency function V(λ))
  z̄(λ): Z-primary response curve

  TRISTIMULUS VALUES:
  X = ∫ S(λ) × x̄(λ) dλ
  Y = ∫ S(λ) × ȳ(λ) dλ  (= luminance)
  Z = ∫ S(λ) × z̄(λ) dλ
  Where S(λ) = SPD × reflectance
```

### CIE Chromaticity Diagram (xy)

```
CHROMATICITY: separate color from luminance
  x = X / (X+Y+Z)
  y = Y / (X+Y+Z)
  z = Z / (X+Y+Z) = 1 − x − y

  (x, y) = chromaticity (2D, normalized, luminance-independent)
  Y = luminance (add back when needed → xyY space)

THE HORSESHOE DIAGRAM:
  Plot (x, y) for all monochromatic wavelengths
  → Curved boundary from ~380 to 700 nm (spectral locus)
  Connect endpoints with straight line (the "line of purples")
  → All real colors are inside this boundary

  WHITE POINT D65:
  x = 0.3127, y = 0.3290 (defined standard daylight illuminant)
  → Reference white for sRGB, Display P3, Rec.2020

  GAMUT TRIANGLES:
  RGB display primaries = triangle on the diagram
  Colors inside triangle = reproducible
  Colors outside = out-of-gamut

CRITICAL LIMITATION OF CIE XY:
  Not perceptually uniform
  Equal distances in xy ≠ equal perceived color differences
  Green region: huge area for small perceptual difference
  Blue-violet region: small area for large perceptual difference
  → Cannot use xy for ΔE color difference calculation (use CIELAB)
```

---

## CIELAB (CIE L*a*b*, 1976)

```
PROBLEM CIELAB SOLVES:
  CIE XYZ is not perceptually uniform
  Need a space where ΔE (color difference) = 1 → 1 JND everywhere

TRANSFORMATION (nonlinear from XYZ):
  X₀, Y₀, Z₀ = XYZ of reference white (D65 for sRGB: X₀=95.047, Y₀=100, Z₀=108.883)

  f(t) = t^(1/3)           if t > (6/29)³ ≈ 0.00886
         (29/6)² × t/3 + 4/29  otherwise (linear near black)

  L* = 116 × f(Y/Y₀) − 16   (lightness, 0=black, 100=white)
  a* = 500 × [f(X/X₀) − f(Y/Y₀)]  (green- to red+)
  b* = 200 × [f(Y/Y₀) − f(Z/Z₀)]  (blue- to yellow+)

INTERPRETATION:
  +a* = red, −a* = green
  +b* = yellow, −b* = blue
  L* = 0 (black) to L* = 100 (white)
  Neutral grays: a* = 0, b* = 0

  Cylindrical form (LCh):
  C*ab = √(a*² + b*²)  (chroma)
  h_ab = atan2(b*, a*)  (hue angle, 0-360°)
  → More intuitive: L* / C*ab / h_ab

COLOR DIFFERENCE (ΔE):
  ΔE*ab = √(ΔL*² + Δa*² + Δb*²)  (original 1976 formula)

  INTERPRETATIONS:
  ΔE < 1.0:  Barely perceptible even to trained observer
  1.0-2.0:   Acceptable for most applications (printing, textiles)
  2.0-3.5:   Perceptible to trained observer
  3.5-5.0:   Obviously different on direct comparison
  > 5.0:     Obvious even to casual observer; different colors

CIEDE2000:
  Improved formula accounting for known non-uniformities in CIELAB:
  • Hue dependency (blue region still non-uniform in L*a*b*)
  • Chroma dependency
  • Lightness dependency
  Much more complex formula; 6 correction terms
  Standard for textile, paint, plastic color tolerancing

CIELAB LIMITATIONS:
  Still not perfect (CIEDE2000 needed for improvement)
  Better than XYZ but not ideal near blue-violet
  OKLab (Björn Ottosson, 2020) is more uniform but not ISO standard yet
```

---

## sRGB (1996)

```
ORIGIN: Joint Microsoft/HP specification, 1996
  Designed for: consumer monitors, internet, consistent display
  White point: D65 (x=0.3127, y=0.3290) — standard daylight
  Gamma: γ = 2.2 (with linear segment near black: sRGB transfer function)

PRIMARIES (CIE xy chromaticities):
  R: x=0.64, y=0.33
  G: x=0.30, y=0.60
  B: x=0.15, y=0.06
  → Gamut covers ~35% of CIE xy chromaticity diagram

ENCODING:
  Linear: 0.0 to 1.0 physical light intensity
  Encoded: 0 to 255 (8-bit) with sRGB transfer function applied
  Transfer function: approximately x^(1/2.2) for x > 0.0031308
  → Most images stored as encoded sRGB

UBIQUITY:
  Default for JPEG, PNG (without profile), most web content
  When no color profile embedded → assume sRGB
  Monitor default without calibration ≈ sRGB (approximately)

LIMITATIONS:
  No saturated cyans, magentas, or wide-gamut greens
  ~65% of CIE gamut is outside sRGB
  Inadequate for HDR (luminance limited)
  Professional photography/video outgrew sRGB by early 2000s
```

---

## Display P3 and Rec.2020

```
DISPLAY P3:
  Origin: DCI-P3 (digital cinema), adapted by Apple for displays
  White point: D65 (same as sRGB)
  Different R, G primaries → green shifted toward cyan
  Gamut: ~25-26% larger than sRGB
  Dominant on all modern Apple devices (iPhone 7+, MacBook 2016+, iPad Pro)
  → CSS color(display-p3 r g b) syntax

  Practical gap:
  sRGB red: R(0.64, 0.33) P3 red: R(0.68, 0.32) — slightly more saturated
  sRGB green: G(0.30, 0.60) P3 green: G(0.265, 0.690) — significantly more saturated
  → The extra gamut is mostly in greens (nature photography, sRGB undersaturates)

REC.2020 (BT.2020):
  ITU-R standard for UHD and HDR broadcast
  Primaries chosen to be spectrally narrow (near monochromatic) → very wide gamut
  Gamut: ~76% of CIE chromaticity diagram
  R: x=0.708, y=0.292  G: x=0.170, y=0.797  B: x=0.131, y=0.046

  PROBLEM: No display currently achieves 100% Rec.2020
  Best quantum dot displays: ~90%
  Standard LCD: ~65%
  → Rec.2020 is a container/future-proofing standard, not current display spec

  Paired with HDR transfer functions:
  PQ (Perceptual Quantizer, ST 2084): up to 10,000 nits absolute luminance
  HLG (Hybrid Log-Gamma): backward-compatible with SDR, up to ~1000 nits

PROPHOTO RGB:
  Even wider than Rec.2020 (~91% of CIE gamut)
  Used for archival RAW photo storage
  Most pixels in ProPhoto are outside display gamut → editing-space only
  Never used for delivery (most content would be outside any display's gamut)
```

---

## Pantone Matching System (PMS)

```
HISTORY:
  Lawrence Herbert acquired Pantone Inc. (1962)
  Created standardized spot-ink system for printing industry
  Problem it solved: "match my logo red" across different printers

STRUCTURE:
  ~2,100 PMS colors (Pantone 2023 guide)
  Each has: unique number, substrate designation (C/U/M), ink formulas
  • C = coated paper (bright, saturated)
  • U = uncoated paper (softer appearance, same formula)
  • M = matte paper

PANTONE NUMBER SYSTEM:
  100-200: yellows and yellow-reds
  300-400: reds and pinks
  500-600: magentas and purples
  700-800: blues and purples
  900s: mixed/neutral
  1000s: greens (process-based)
  Metallic: 8000 series
  Pastels: 9000 series

PANTONE vs CMYK:
  Many Pantone colors are OUT of CMYK gamut
  CMYK is 4-color process (halftone dots of C, M, Y, K)
  Pantone is SPOT color (premixed ink applied solid)
  → Vivid orange, vivid green, metallics: only reproducible as Pantone spot
  → "Convert to CMYK" = gamut compression = color shift

PANTONE COLOR OF THE YEAR:
  Annual declaration since 2000 (Leatrice Eiseman / Pantone Color Institute)
  2020: Classic Blue (19-4052)
  2021: Illuminating (yellow) + Ultimate Gray
  2022: Very Peri (17-3938) — periwinkle blue-violet
  2023: Viva Magenta (18-1750)
  2024: Peach Fuzz (13-1023)
  Cultural signaling → influence on fashion, interior design, packaging

PANTONE vs COMPETITORS:
  RAL: German standard, more common in industrial/construction Europe
  Federal Standard 595: US government/military
  NCS: Natural Color System (Scandinavian)
  Toyo: Japanese printing system
  DIC: Japanese design system
```

---

## RAL and NCS

```
RAL (Deutsches Institut für Gütesicherung und Kennzeichnung):
  HISTORY: Founded 1927, "Reichs-Ausschuß für Lieferbedingungen" (Imperial Committee)
  → Standardizing industrial product specifications

  RAL CLASSIC: 213 colors; 4-digit codes
    1000-1099: Yellows (1001 Beige, 1018 Zinc Yellow)
    2000-2099: Oranges (2004 Pure Orange)
    3000-3099: Reds (3020 Traffic Red)
    4000-4099: Violets (4007 Purple Violet)
    5000-5099: Blues (5015 Sky Blue)
    6000-6099: Greens (6002 Leaf Green, 6005 Moss Green)
    7000-7099: Greys (7016 Anthracite Grey — ubiquitous in European design)
    8000-8099: Browns
    9000-9099: Whites and blacks

  RAL DESIGN SYSTEM+: 1825 colors in CIELAB-based systematic arrangement
  → Professional design/architecture use

  RAL 7016 (Anthracite Grey): the dominant window frame color in Europe
  RAL 9005 (Jet Black), RAL 9010 (Pure White): architectural standards

NCS (Natural Color System):
  DEVELOPED: Scandinavian Colour Institute, Sweden, 1979
  THEORY: Based on Hering's opponent-color perception model (not tristimulus)
  NOTATION: S YYCC-C₁hue₂ → e.g., S 2050-B40G

  NCS describes: how much of each "elementary" color a color contains
  6 elementary colors: white (W), black (S), yellow (Y), red (R), blue (B), green (G)
  Nuance: percentage of blackness + chromaticness
  Hue: described by percentage between two adjacent elementaries

  APPLICATIONS:
  • Scandinavian building codes
  • Furniture (IKEA uses NCS)
  • Nordic paint manufacturers (Jotun, Nordsjö)
  Advantage over Pantone: physically based in perception, not proprietary
```

---

## Color Appearance Models: CIECAM02 and Successors

CIELAB assumes fixed viewing conditions. Real cross-media matching (print at 2000 lux vs. screen at 200 lux) requires modeling how the visual system adapts:

```
CIECAM02 (CIE Color Appearance Model, 2002):
  Inputs: XYZ of stimulus, XYZ of white point (Xw,Yw,Zw),
          adapting luminance (LA), background relative luminance (Yb),
          surround condition (average/dim/dark)

  Outputs: J (lightness), C (chroma), h (hue angle), Q (brightness),
           M (colorfulness), s (saturation)

  Key effects modeled:
  • Hunt effect: colorfulness increases with luminance
  • Stevens effect: contrast increases with luminance
  • Chromatic adaptation: von Kries-style, CAT02 transform

CIECAM16: 2016 revision fixing known issues with CAT02 matrix.
ZCAM (2021): Further refinements, used in some HDR workflows.

OKLab (Ottosson 2020): A practical approximation of CIECAM16/ZCAM JMh space
  designed for computational efficiency. Perceptually uniform, good hue linearity.
  Used in CSS Color Level 4 (oklch), Figma, modern design tools.
```

### Color Space Conversion as Linear Algebra

All XYZ-to-RGB and RGB-to-XYZ transformations are 3x3 matrix multiplications — the color matching functions define the transform for a given set of primaries. For sRGB, the matrix is defined in IEC 61966-2-1. The CIELAB cube-root nonlinearity is the only non-matrix step in the XYZ-to-Lab path; everything else in the color pipeline is linear algebra.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What's the difference between CIE XY and CIELAB? | CIE xy: device-independent measurement; not perceptually uniform. CIELAB: derived from XYZ but cube-root transformed for perceptual uniformity; use for ΔE color difference |
| What ΔE value indicates "acceptable" color match? | ΔE < 2.0 is acceptable for most commercial applications. ΔE < 1.0 is barely perceptible even to experts. CIEDE2000 formula is more accurate than ΔE*ab |
| Why does sRGB cover only 35% of visible colors? | sRGB primaries form a triangle in CIE chromaticity space; the most saturated visible colors (spectral locus) are outside that triangle. It's a gamut limitation of the chosen primaries. |
| When to use Pantone vs CMYK? | Pantone: logo/brand color needing exact reproduction; vivid out-of-gamut colors; metallic. CMYK: full-color print where Pantone budget isn't justified; photos always CMYK. |
| What is RAL 7016? | Anthracite Grey — the dominant European window frame, door, and architectural metal color. If you've been in a modern European building, you've seen RAL 7016. |
| What's the key innovation of Munsell? | Equal perceptual spacing (empirically calibrated from observer experiments) in all three dimensions (Hue/Value/Chroma), before colorimetry existed. Still used in soil science. |
| What's the relationship between L* and brightness? | L* = 116 × (Y/Yn)^(1/3) − 16. The cube root makes it perceptually uniform. L*=50 is not 50% luminance — it's the luminance value that appears half-bright. |

---

## Common Confusion Points

**Pantone numbers don't have universal meaning outside print:** Pantone 485 C in screen context means nothing without conversion. When designers specify "Pantone 485" for a website, they mean "match this red," not "encode as Pantone." The actual screen value is specified separately.

**sRGB gamma ≠ exactly 2.2:** The sRGB transfer function has a linear segment near black (below 0.0031308) and a power segment with exponent 1/2.4 (≈ gamma 2.4, not 2.2). The effective gamma is ~2.2 across the full range. "sRGB gamma is 2.2" is a common simplification.

**L*a*b* is still not perfectly uniform:** CIEDE2000 exists because L*a*b* has known residual non-uniformities (especially in the blue region). L*a*b* is much better than XYZ but not perfect. For the most accurate color difference calculation, always use CIEDE2000, not the simple Euclidean ΔE*ab formula.

**Display P3 ≠ DCI-P3:** DCI-P3 (digital cinema) uses a white point of ~6300K (different from D65). Display P3 (Apple) uses D65 white point. Same primaries, different white. Confusingly similar names for subtly different specifications.
