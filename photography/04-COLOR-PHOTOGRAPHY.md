# Color Photography

## The Big Picture

Color photography requires capturing and reproducing the three-dimensional nature of color (hue, saturation, lightness) from a two-dimensional image. The path from scene light to faithful color reproduction involves physics (light and optics), chemistry (dyes and films), and digital signal processing (color spaces and profiles).

```
HUMAN COLOR VISION:
  3 cone types: L (peak ~565nm), M (~535nm), S (~420nm)
  → Color = 3-number response → 3D perceptual space
  → Any color can be matched by adjusting 3 primaries

REPRODUCING COLOR (two fundamental approaches):
  ADDITIVE synthesis: combine colored lights
    Red + Green + Blue light = White
    Used: displays (monitor, TV, projector), digital capture
    Primary triplet: R, G, B

  SUBTRACTIVE synthesis: absorb portions of white light
    Cyan ink absorbs Red; Magenta absorbs Green; Yellow absorbs Blue
    All three: absorb everything → Black
    Used: printing, photographic dyes, color negative film
    Primary triplet: C, M, Y (+ K for practical printing)
```

---

## Additive Color Systems

### Early Additive Photography

```
AUTOCHROME (Lumière Brothers, 1907):
  First commercially successful color process
  Mechanism: random mosaic of dyed potato starch grains on plate
    Red, green, blue dyed particles mixed and distributed randomly
    Each particle acts as a tiny RGB filter
    Panchromatic silver halide emulsion coated over particles
  Viewing: transmitted light through positive transparency
           each grain passes only its own color → color image by additive mosaic

  Problem: 1/4 of light gets through mosaic → low sensitivity
  Result: beautiful, painterly color; ~4-stop exposure penalty
  Historical significance: first widely used color process; Prokudin-Gorsky used it

LIPPMANN PHOTOGRAPHY (Gabriel Lippmann, 1891, Nobel Prize 1908):
  No filters at all — uses light interference
  Mercury mirror behind emulsion → standing wave nodes form in emulsion
  Silver precipitates at nodes → wavelength-specific grating
  Result: interference colors perfectly matching original wavelengths
  Problem: narrow viewing angle; mercury + collodion → extreme care required
  Practical significance: nearly zero, but beautiful physics
```

### Digital Capture (Additive)

```
DIGITAL SENSOR AS ADDITIVE SYSTEM:
  Bayer pattern: RGB mosaic over silicon photodiodes
  Each pixel measures ONE color channel (red, green, or blue)
  50% green, 25% red, 25% blue pixels (reflects human eye's green sensitivity)
  → Demosaicing reconstructs 3-channel RGB image from single-channel mosaic
  (see 06-DIGITAL-SENSORS.md for full treatment)
```

---

## Subtractive Color: How Color Film Works

### Subtractive Primary Geometry

```
SUBTRACTIVE MIXING:

  White light (all wavelengths)

  CYAN ink/dye: absorbs RED → reflects blue + green = cyan
  MAGENTA ink/dye: absorbs GREEN → reflects red + blue = magenta
  YELLOW ink/dye: absorbs BLUE → reflects red + green = yellow

  Combinations:
    Cyan + Magenta: absorbs red + green → only blue reflected
    Magenta + Yellow: absorbs green + blue → only red reflected
    Cyan + Yellow: absorbs red + blue → only green reflected
    All three: absorbs red + green + blue = black (imperfect in practice)

DYES vs INKS:
  Transparent dyes in a gelatin layer filter transmitted light
  → Viewing by transmission (slides, film) or by reflection off white paper
  Inks: printed dots; subtractive mixing approximately; also halftone dot gain
```

### Color Negative Film Architecture

```
COLOR NEGATIVE FILM LAYERS:

Top of emulsion stack → viewed first by incoming light:

  UV filter layer (prevents UV from exposing lower layers)
  ───────────────────────────────────────────────────────
  Blue-sensitive layer + YELLOW coupler
  (Blue light → yellow dye; yellow dye subtracts blue from white = cyan + red = scene color)
  ───────────────────────────────────────────────────────
  Yellow filter layer (absorbs residual blue — AgBr intrinsically blue-sensitive)
  ───────────────────────────────────────────────────────
  Green-sensitive layer + MAGENTA coupler
  (green spectral sensitization; green light → magenta dye)
  ───────────────────────────────────────────────────────
  Red-sensitive layer + CYAN coupler
  (red spectral sensitization; red light → cyan dye)
  ───────────────────────────────────────────────────────
  Antihalation layer (prevents light scatter back)
  Polyester or cellulose triacetate base

KEY RELATIONSHIPS:
  Blue in scene → yellow dye in negative (complementary)
  Green in scene → magenta dye
  Red in scene → cyan dye
  → Negative has complementary colors of scene

ORANGE MASK:
  Color negative film has overall orange cast
  Cause: magenta and cyan dyes have inherent unwanted blue/green absorption
         that introduces error in color balance
  Correction: colored couplers (orange, colored residue after development)
              compensate for dye impurities
  Effect in printing: must subtract the orange mask's effect
                      → color printing filters compensate automatically
  → Orange mask improves color accuracy of printed output
```

---

## Color Reversal Film (E-6)

Slide film produces a direct positive transparency — you see the scene colors directly on the film.

```
E-6 PROCESSING SEQUENCE:

1. First developer (black and white, conventional):
   Exposed silver halide → metallic silver in all three layers
   Only exposed areas (high scene density) develop

2. Reversal step:
   Remaining unexposed silver halide fogged chemically
   (historically: re-exposure to white light; now chemical fogging agent)

3. Color developer (CD-4):
   Fogged (originally unexposed) halide developed
   Oxidized CD-4 + dye coupler → colored dye forms
   Yellow dye in blue layer (where blue was NOT)
   Magenta dye in green layer (where green was NOT)
   Cyan dye in red layer (where red was NOT)

4. Conditioner → bleach → fix → wash

5. Result: where scene was BRIGHT (much exposure) →
           silver developed in step 1 → removed by bleach →
           no remaining dye → the slide is light (correct)
   where scene was DARK (little exposure) →
           fogged and developed in step 3 → dye forms → slide is dark

CRITICAL DIFFERENCE FROM NEGATIVE:
  Reversal film latitude: ~5–7 stops total; 1–2 stops from ideal = visible shift
  Negative film latitude: 12–16 stops; 3+ stops from ideal still printable

Slide film metering rule: "expose for the highlights"
  → Overexposed highlights wash out completely; no recovery possible
  → Underexposed shadows gain density in printing; highlights irreplaceable
```

---

## Color Management: The ICC Profile System

**Linear algebra of color**: CIE XYZ coordinates are linear combinations of cone responses (from the 1931 color matching experiments), designed so Y = luminance and all coordinates are non-negative. Every color space conversion (camera RGB -> XYZ -> sRGB -> Adobe RGB) is a **3x3 matrix multiplication** on the RGB triplet — color spaces are coordinate systems in a 3D linear vector space, related by invertible linear transforms. CIELAB adds a perceptual nonlinearity (cube-root compression, modeling Weber-Fechner) on top of XYZ. The structure is: linear sensor space -> linear reference space (XYZ) -> perceptual space (Lab). See `colors/03-COLOR-SYSTEMS.md` for the full treatment.

### The Problem: Device-Dependence

```
WHY COLOR MANAGEMENT EXISTS:

  Same RGB values (255, 0, 0) displayed on:
    Monitor A: orange-red, D65 white point
    Monitor B: bluer red, cooler white
    Printer: physical red ink, different gamut
    Camera: red interpretation before white balance

  → Without calibration, same numbers = different colors on each device

  The device color problem:
    Every device has its own color response:
    Camera sensors: have spectral sensitivities, white balance applied
    Monitors: phosphors or OLEDs with specific R/G/B primaries
    Printers: CMYK inks, halftone dots, paper absorption
    Projectors: lamp spectrum, optics, screen gain

  To communicate color accurately across devices:
    Need a device-independent reference space → map every device into it
    → CIE XYZ or CIE Lab as reference; ICC profiles as device-to-device map
```

### ICC Profiles

```
ICC PROFILE:
  File containing the color transform between a device color space and
  the Profile Connection Space (PCS — usually CIE D50 Lab)

PROFILE TYPES:
  Input profiles (cameras, scanners): device → PCS
  Display profiles (monitors): device ↔ PCS (bidirectional)
  Output profiles (printers, presses): device → PCS (simulate output)

HOW COLOR MANAGEMENT PIPELINE WORKS:

  Camera RAW data
       │ apply camera profile (input profile)
       ▼
  Device-independent Lab/XYZ
       │ apply display profile (monitor calibration)
       ▼
  Monitor-specific RGB → screen display

  For printing:
  Lab/XYZ
       │ apply printer profile + paper profile
       ▼
  CMYK or RGB printer values → printed dot

RENDERING INTENTS:
  Four options for handling out-of-gamut colors:
  1. Perceptual: compress entire gamut proportionally to fit destination gamut
     → Maintains relationships; colors shift but look natural
     → Best for photographs with wide tonal range
  2. Relative colorimetric: shift only out-of-gamut colors to nearest in-gamut
     → Preserves in-gamut colors exactly
     → Best for accurate reproduction of specific colors (logos, proofing)
  3. Absolute colorimetric: like relative, but preserves absolute white point
     → Shows paper white as actual paper color (useful for proofing simulation)
  4. Saturation: maximize saturation → best for graphics, charts, logos
```

### Standard Color Spaces

```
COMMON RGB WORKING SPACES:

sRGB:
  Primaries: same as HDTV/Rec.709; white point D65
  Gamma: 2.2 approximately (actually piecewise linear + power)
  Gamut: medium; covers ~35% of visible colors
  Use: internet, consumer devices, JPEGs for web
  Problem: cannot represent highly saturated colors (Fuji Velvia film palette)

Adobe RGB (1998):
  Wider gamut than sRGB (covers ~50% of visible colors)
  Larger green triangle; extends into colors sRGB cannot encode
  White point D65, gamma 2.2
  Use: professional photography, pre-press, printing workflows
  Problem: opens extra bit depth vs sRGB for same visual quality

ProPhoto RGB:
  Very wide gamut (covers ~90% of visible colors, including non-physical)
  White point D50 (print-oriented)
  Gamma 1.8
  Use: archival RAW workflows; must use 16-bit — 8-bit = posterization artifacts
  Problem: contains non-realizable colors outside human vision → can't display all of it

DCI-P3:
  Digital Cinema Initiatives wide gamut
  Primaries designed for digital cinema projectors
  25% larger gamut than sRGB; fully contained within ProPhoto
  Use: iPhone displays, newer monitors, HDR content
  Trend: becoming new consumer display standard

Rec. 2020 (BT.2020):
  Ultra HD / HDR standard
  Extremely wide gamut (covers ~75% of visible colors)
  Few consumer displays can show its full gamut yet (2025)
  Future standard for 4K HDR content
```

---

## Soft Proofing

```
SOFT PROOF: simulate on-screen how an image will look when printed
            on a specific printer/paper combination

SOFT PROOFING WORKFLOW:

1. Calibrate monitor (hardware calibration preferred)
   → ICC display profile created by colorimeter + software

2. Open image in editing application (Lightroom, Photoshop, Capture One)

3. Enable soft proof → select printer + paper ICC profile
   → Application simulates: color gamut compression + paper white
   → Colors that fall outside printer gamut shown as "gamut warning" (gray overlay)

4. Make adjustments to optimize for that specific print output
   → May need to reduce saturation, open shadows to preserve in output gamut

5. Print → result should closely match soft proof on calibrated monitor

PREREQUISITES FOR ACCURATE SOFT PROOF:
  Calibrated display (ΔE < 2 ideally)
  Profile for your specific printer + paper combination
  Controlled viewing light (D50 5000K lamp, no glare)
  Room not too dim (ambient can affect perception)

WHY IT OFTEN DOESN'T PERFECTLY MATCH:
  Metamerism: print and display use different physics; match under one illuminant,
    differ under another (monitor emits light; print reflects)
  Paper white: hard to simulate on luminous display
  Display gamut may not cover all print colors (some matte papers have
    different saturation characteristics)
  Human perceptual adaptation changes over viewing time
```

---

## Color Perception: Why Reproduction Is Hard

```
METAMERISM:
  Two colors match under one illuminant but not another
  → Different spectral power distributions, same tristimulus values under one light
  → Illuminant change → different tristimulus values → different appearance
  Problem for:
    Photographing objects that will be viewed under different lights
    Printing that looks like the display under D65 but not under incandescent light

SIMULTANEOUS CONTRAST:
  A neutral gray looks different surrounded by different colors
  → Human visual system adapts to surround
  → Viewing prints in a colored environment shifts perceived colors
  → Printing industry standard: D50 booth with neutral gray surround

CHROMATIC ADAPTATION:
  Eyes adapt to ambient illuminant → "white" appearance varies by illuminant
  → Camera doesn't adapt (no chromatic adaptation without white balance)
  → White balance corrects for illuminant; "auto white balance" attempts to
    mimic human chromatic adaptation

SIMULTANEOUS CONTRAST IN DIGITAL DARKROOM:
  Working on screen in dark room vs bright room → different saturation judgments
  Industry standard: editing environment with D50 ambient, 64–160 cd/m² luminance
```

---

## Decision Cheat Sheet

| Goal | Choice |
|------|--------|
| Widest print color gamut | Adobe RGB or ProPhoto RGB in 16-bit workflow |
| Web delivery | Convert to sRGB at export |
| Proofing print output on screen | Soft proof with printer ICC profile |
| Most latitude for exposure errors | Color negative film (12+ stops) |
| Richest color slide presentation | Color reversal E-6 (Fuji Velvia 50 for max saturation) |
| Calibrated monitor color | Hardware calibration + ICC display profile |
| Cross-device consistent color | ICC workflow: embed profiles, convert at output |
| Printing from RAW | Export ProPhoto RGB 16-bit to printer RIP |

---

## Common Confusion Points

**sRGB is not a universal standard that guarantees correct color**
sRGB defines the primaries and gamma of a specific color space. A file tagged sRGB will display correctly only if the display is calibrated to sRGB. An uncalibrated monitor may display sRGB files with incorrect colors. The ICC system addresses this; simply tagging files as sRGB doesn't fix poorly calibrated displays.

**Color negative orange mask is not a problem — it's a solution**
The orange mask in color negatives compensates for impure dye spectral absorption. Without it, the printed color would be less accurate. Scanning color negatives: scanners understand the orange mask; RAW scanners allow you to correct for it manually; "inversion" of a negative without understanding the mask creates poor results.

**Perceptual rendering intent moves all colors, not just out-of-gamut ones**
Perceptual intent compresses the entire gamut proportionally, which changes even in-gamut colors slightly to preserve relationships. Relative colorimetric preserves in-gamut colors exactly but clips out-of-gamut. Which is better depends on the image content and how much of it is out-of-gamut.

**Rec.709 and sRGB have the same primaries and differ only in transfer function**
sRGB uses an approximate gamma 2.2 curve; Rec.709 (HDTV) uses a different gamma 2.4 effective curve with a linear region at the bottom. The primaries (red, green, blue, white point) are identical. Most consumer content mixing these up causes subtle display differences.

**Slide scanning requires a very different workflow than negative scanning**
Slides are positives with very limited latitude — what you see in the scan is roughly what you have; there is very little shadow recovery possible. Negatives have enormous latitude encoded in a compressed positive-Orange format — and the scanner (or software like Lightroom's "Dehaze" profile models for negative film) must decompress this into a viewable image. Profiling scanners correctly matters enormously for negatives.
