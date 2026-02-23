# Mixing Theory — Additive vs Subtractive, CMYK, Gamut

## The Big Picture

```
+------------------------------------------------------------------+
|              TWO FUNDAMENTALLY DIFFERENT MIXING SYSTEMS          |
|                                                                  |
|  ADDITIVE MIXING (light sources)                                 |
|  Start from: BLACK (no light)                                    |
|  Add: colored lights → increase luminance                        |
|  Primaries: RED + GREEN + BLUE → WHITE                           |
|  Used in: monitors, theater lighting, digital imaging            |
|  Physics: sum the SPDs                                           |
|                                                                  |
|  SUBTRACTIVE MIXING (pigments/inks)                              |
|  Start from: WHITE (paper/canvas reflects all light)             |
|  Add: pigment layers → each subtracts wavelengths                |
|  Primaries: CYAN + MAGENTA + YELLOW → BLACK (ideal)             |
|  Used in: printing, painting, dyes                               |
|  Physics: multiply the reflectance curves                        |
|                                                                  |
|  OPTICAL (PARTITIVE) MIXING                                      |
|  Small patches of different colors → eye mixes them at distance  |
|  Approximates additive, but with reflected not emitted light     |
|  Used in: Pointillism, woven textiles, halftone printing         |
|                                                                  |
|  KEY CONFUSION: "mixing colors" means different things           |
|  in each system; rules don't transfer across systems             |
+------------------------------------------------------------------+
```

---

## Additive Mixing (Light)

```
PHYSICS:
  Multiple light sources illuminate same spot
  Total SPD = sum of individual SPDs
  Cone response = sum of cone responses
  → More light = more stimulation = lighter/brighter

PRIMARY COLORS IN ADDITIVE:
  RED: stimulates primarily L-cone
  GREEN: stimulates primarily M-cone
  BLUE: stimulates primarily S-cone
  → Three primaries = approximate L, M, S cone stimulation independently

  R + G = Yellow (L + M stimulated, S weak)
  G + B = Cyan (M + S stimulated, L weak)
  R + B = Magenta (L + S stimulated, M weak)
  R + G + B = White (all cones stimulated)
  No light = Black

DISPLAY TECHNOLOGY:
  CRT: red/green/blue phosphors excited by electron beam
  LCD: backlight filtered by color filters (R/G/B subpixels) with LC shutter
  OLED: organic emitters per subpixel (R/G/B individually driven)
  → Each pixel: combination of 3 subpixels at different intensities
  → Result: any color in sRGB (or Display P3) gamut

"RGB VALUE" (e.g., rgb(255, 0, 0)):
  255, 0, 0 = max red, no green, no blue = pure red
  128, 128, 128 = equal mid-intensity → medium gray
  255, 255, 0 = red + green → yellow
  → These are ENCODED values (after gamma); linear values are different
  → rgb(128, 128, 128) is NOT 50% luminance! It's ~18% luminance (gamma effect)
  → css color(srgb-linear 0.5 0.5 0.5) would be 50% luminance gray
```

---

## Subtractive Mixing (Pigments and Inks)

```
PHYSICS:
  Light hits pigment layer → some wavelengths absorbed, rest reflected
  Multiple pigment layers → each absorbs its wavelengths
  Total reflectance = product of individual reflectances at each wavelength

  Layer 1: reflects 80% at 500nm, 20% at 600nm
  Layer 2: reflects 90% at 500nm, 90% at 600nm
  Combined: 0.8 × 0.9 = 72% at 500nm, 0.2 × 0.9 = 18% at 600nm
  → Combined: more blue-green, less red → cool result

PRIMARY COLORS IN SUBTRACTIVE:
  CYAN: absorbs RED, reflects blue + green
  MAGENTA: absorbs GREEN, reflects red + blue
  YELLOW: absorbs BLUE, reflects red + green

  C + M = Blue (absorbs red + green, reflects blue)
  C + Y = Green (absorbs red + blue, reflects green)
  M + Y = Red (absorbs green + blue, reflects red)
  C + M + Y = Black (absorbs all visible) — theoretical; in practice: dark muddy brown

WHY CMY ARE THE SUBTRACTIVE PRIMARIES:
  CMY are complements of RGB:
  Cyan = complement of Red (absorbs what red stimulates)
  Magenta = complement of Green (absorbs what green stimulates)
  Yellow = complement of Blue (absorbs what blue stimulates)
  → Mixing any two CMY = produces one RGB primary
  → Mixing all three = absorbs all primaries = black (ideally)

PAINTING REALITY:
  No pigment is perfectly cyan or perfectly yellow
  Real pigments have residual absorption at unintended wavelengths
  → Mixing real yellow + real blue doesn't give clean green
  → "Dead" or "muddy" results from multiple overlapping imperfect absorbers
  → Oil painters learn specific pigment combinations for clean colors
     (e.g., transparent mixing: phthalo blue + hansa yellow → vivid green)
     (e.g., opaque mixing: titanium white + raw umber → not same as pale umber)
```

---

## The RYB Artist Model

```
TRADITIONAL ART SCHOOL SYSTEM:
  Taught in Western art education since ~17th century
  "Primary colors": Red, Yellow, Blue
  "Secondary colors": Orange (R+Y), Green (Y+B), Purple (R+B)
  "Tertiary": red-orange, yellow-orange, etc.

WHY IT'S TECHNICALLY WRONG:
  RYB is not scientifically derived from physics or colorimetry
  "Blue + Yellow = Green" works only approximately with real pigments
  "Red + Blue = Purple" works only approximately
  Neither rule works for light (additive mixing)
  Neither rule holds for process printing inks (CMY, not RYB)

WHY IT PERSISTS:
  Works approximately for opaque oil/acrylic paint
  Real-world pigment mixing: "blue" paint (ultramarine/cobalt) + "yellow" paint
  → does produce green because pigments are broadband absorbers
  → the approximation is good enough for practical painting
  Itten's Bauhaus color wheel (based on RYB): pedagogically influential
  → used in design schools, art curricula worldwide

RYB vs CMY in practice:
  Printing: CMY is correct (ink subtracts from white paper)
  Light: RGB is correct (screen adds to black)
  Painting: CMY is more accurate than RYB, but:
    Artists don't use pure cyan/magenta/yellow
    Pigments named "red" are often close to magenta
    Pigments named "blue" are often close to cyan
    The confusion is partly nomenclature
  → Quinacridone red (≈ magenta) + phthalo blue (≈ cyan) + hansa yellow (≈ yellow)
    IS essentially CMY painting — more color mixing theory-accurate than RYB
```

---

## CMYK Printing

```
FOUR-COLOR PROCESS:
  C: Cyan ink
  M: Magenta ink
  Y: Yellow ink
  K: Key (Black) ink
  Printed as overlapping halftone dots

WHY ADD K (BLACK)?
  CMY inks are NOT perfectly transparent and perfectly complementary
  CMY "black" = muddy brown (residual color + paper show-through)
  True black requires K ink
  Cost savings: black ink cheaper than CMY; using K for text/shadows saves money
  Total ink limit (TIL): putting C+M+Y+K all at 100% would over-saturate paper
  → K replaces some CMY where dark neutrals are needed (GCR: Grey Component Replacement)

HALFTONE DOTS:
  Continuous-tone image → discrete dots at different sizes and angles
  Larger dots (higher % area) → more ink → darker area at that color
  Classic screen angles (prevent moiré):
  • Black (K): 45° (most visible color → least visible angle: diagonal)
  • Magenta (M): 75°
  • Cyan (C): 105° (= 15° from black, other side)
  • Yellow (Y): 90° (least visible color → can use less ideal angle)

MOIRÉ PATTERN:
  When two periodic patterns at similar angles overlap → beat frequency visible
  Careful angle separation prevents moiré in conventional printing
  Digital/FM screening (frequency modulation): random dot placement
  → No regular pattern → no moiré → better for fine detail
  → Used in high-quality inkjet and digital press

CMYK GAMUT vs sRGB:
  CMYK gamut is NOT simply inside sRGB gamut
  • CMYK can reproduce some blues/violets that sRGB cannot
  • sRGB can reproduce some saturated colors that CMYK cannot
  • Overlap is large; exclusions are at extreme saturations
  → "Convert sRGB to CMYK" = gamut mapping required at boundaries
  → Rendering intent determines how out-of-gamut colors are compressed
```

---

## Optical / Partitive Mixing

```
PHENOMENON:
  Small patches of different colors → at a distance, cones integrate
  → Result approximates additive mixing (not subtractive)
  → Colors appear more vivid than physical mixture of same pigments

WHY MORE VIVID:
  Physical mixing (subtractive): reflectance curves multiplied → darker
  Optical mixing (partitive): cones average signals
    → Closer to additive averaging → maintains higher luminance
  Result: juxtaposed red + blue dots → perceive violet that is
    brighter and more vivid than mixing red + blue paint

SEURAT AND SIGNAC — NEO-IMPRESSIONISM / POINTILLISM:
  Georges Seurat applied Chevreul + Maxwell + Ogden Rood ("Modern Chromatics," 1879)
  Method: small dots of pure unmixed pigment
  Theoretical effect: optical mixing at viewing distance
  Practical result: vibrant, luminous surfaces
  → "Sunday Afternoon on La Grande Jatte" (1884-1886): pure dots
  CAVEAT: Modern analysis shows many of Seurat's dots are complementary colors
    placed adjacently — enhancing simultaneous contrast rather than mixing

TEXTILES:
  Woven fabric: colored yarns interlace → at distance, blend
  Harris tweed: two-color woven → appears third color from distance
  → Textile colorists have used optical mixing for centuries
  → "Shot silk" (warp one color, weft another) → iridescent effect

HALFTONE PRINTING:
  CMYK dots at printing resolution → when viewed normally, blend optically
  70-150 lines per inch typical → dots ~0.17-0.36 mm
  → Below resolution of normal viewing distance → optical mix
  → Actually PARTITIVE mixing (reflected, not emitted) but approximates additive
```

---

## Gamut and Color Gamut Mapping

```
GAMUT DEFINITION:
  The set of all colors reproducible by a given system
  Represented as a 3D volume in a color space (e.g., CIELAB)
  or as a 2D triangle on CIE chromaticity diagram (projection)

GAMUT SIZES (approximate % of CIE chromaticity, 2D projection):
+------------------+--------+------------------------------------------+
| SYSTEM           | %      | NOTES                                    |
+------------------+--------+------------------------------------------+
| sRGB             | ~35%   | Default internet/consumer screens        |
| Display P3       | ~45%   | Modern Apple/HDR displays                |
| Adobe RGB        | ~50%   | Wide-gamut print preparation             |
| CMYK (typical)   | ~30%   | Varies by ink/paper; can be non-subset   |
| Rec.2020         | ~76%   | UHD/HDR broadcast standard               |
| ProPhoto RGB     | ~91%   | Archival raw; most content outside display|
| Human vision     | 100%   | Reference (all CIE diagram)              |
+------------------+--------+------------------------------------------+

OUT-OF-GAMUT PROBLEM:
  Real-world camera → ProPhoto RGB (wide) → display (sRGB/P3, narrower)
  Some colors in photo are outside display gamut → must be mapped

RENDERING INTENTS (ICC standard):
  PERCEPTUAL:
    Compress all colors; preserve relationships
    Out-of-gamut colors brought in; in-gamut colors shift to maintain spacing
    Good for: photographs, images with large gamut content
    Risk: all colors shift, even in-gamut ones

  RELATIVE COLORIMETRIC:
    Only out-of-gamut colors clipped/mapped
    In-gamut colors preserved exactly (with white point adjustment)
    Good for: logo colors, specific spot color matching
    Risk: out-of-gamut colors clip to gamut boundary (no grading)

  SATURATION:
    Maximize saturation, ignore colorimetric accuracy
    Good for: business graphics, charts (vivid colors more important than accuracy)

  ABSOLUTE COLORIMETRIC:
    Exact reproduction, no white point compensation
    Good for: proofing (simulating one device on another)

GAMUT WARNING IN PHOTO EDITING:
  Photoshop View > Gamut Warning: highlights out-of-gamut colors
  Soft Proof: preview how colors will appear on target device/profile
  → Editors fix out-of-gamut areas before sending to print
```

---

## The Color of Shadows

```
OBSERVATIONAL PHYSICS:
  In natural light (sunlight + blue sky):
  • Lit areas: warmer light (direct sunlight, ~5500K)
  • Shadowed areas: lit ONLY by sky (diffuse blue/violet, ~10000K)
  → Shadows have a blue-violet color cast

IMPRESSIONIST INSIGHT:
  Pre-Impressionist academic painting: shadows = gray (add black to main color)
  Impressionist observation (plein air): shadows are COLORED, not gray
  → Monet, Renoir: lavender and blue-violet shadows in sunlit paintings
  → Specifically: snow shadows are blue-violet (sky light only)
  → Shadow on skin in sunlight: blue-green (blue sky) or warm (reflected surrounds)

COMPLEMENTARY SHADOW CONVENTION:
  Light source color → shadow contains complement + blue sky component
  Orange firelight → blue-green shadows
  Green-lit stage → red-purple shadows
  This is how theatrical lighting colorists think: warm key → cool fill
  This is how Impressionists painted: light color → complementary in shadow

PHYSICS EXPLANATION:
  Light source → illuminates direct component of reflectance
  Sky/ambient → illuminates shadow component
  Perceived color = sum of reflected components weighted by illuminant
  Shadow area = only sky component → sky's blue tint appears
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Red + Green light = ? | Yellow (additive mixing — L + M cone stimulation) |
| Red + Green paint = ? | Dark brownish-orange (subtractive — each absorbs different wavelengths; combined absorption leaves limited reflection) |
| Why does CMYK use K in addition to CMY? | CMY inks are impure; combined CMY gives muddy brown, not black. Black ink provides true black and saves expensive CMY ink costs. |
| Why are Seurat's colors more vivid than mixed paint? | Optical/partitive mixing: juxtaposed pure pigment dots blend in the eye approximately additively → higher perceived luminance than physical subtractive mixing of same pigments |
| What are the four ICC rendering intents? | Perceptual (compress all, preserve relationships), Relative Colorimetric (clip only out-of-gamut), Saturation (maximize vividness), Absolute Colorimetric (exact, no white point compensation) |
| Why do shadows in sunlight look blue? | Shadowed areas receive only diffuse sky light (~10,000K, blue-violet) rather than direct sunlight. Impressionists were the first Western painters to consistently paint this observation rather than using gray shadows. |
| What is gamut? | The full range of colors reproducible by a given system (display/printer/film). sRGB = ~35% of all visible colors. Out-of-gamut colors must be mapped (clipped or compressed) when converting to a smaller-gamut system. |

---

## Common Confusion Points

**CMY and RYB give different "secondaries":** In CMY: C+M=blue, C+Y=green, M+Y=red. In RYB: R+Y=orange, Y+B=green, R+B=purple. They're different systems. CMY is physics; RYB is a historical approximation for paint. The confusion comes from calling both "the primary color system."

**Additive mixing doesn't apply to pigments:** Computer scientists learn RGB and then try to mix digital colors intuitively, then are confused when paint doesn't work the same way. Mixing rgb(255,0,0) + rgb(0,255,0) gives rgb(255,255,0) (yellow) in screen compositing; mixing red paint + green paint gives dark muddy brown. Different physical systems.

**Partitive (optical) mixing ≠ additive mixing:** Seurat's pointillism produces approximate additive mixing but the mechanism is not emission. Reflected light from dots averages (partitive); this is closer to additive than subtractive but not identical. Pure additive mixing requires emitted light (screens).

**sRGB gamut ≠ "all the colors we can see":** 65% of perceptible colors are outside sRGB. This becomes practically relevant in nature photography (vivid greens, saturated blues), in HDR content, and in wide-gamut print workflows. The statement "sRGB covers all visible colors" is simply false.
