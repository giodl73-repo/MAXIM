# Color Theory and Brand

## The Big Picture

```
+------------------------------------------------------------------+
|                   COLOR IN DESIGN SYSTEMS                        |
|                                                                  |
|  PHYSICS          PERCEPTION        APPLICATION                  |
|  -------          ----------        -----------                  |
|  Wavelength       Color models      Brand palettes               |
|  Light spectrum   Contrast/harmony  Print production             |
|  Metamerism       Gestalt effects   Digital systems              |
|                                                                  |
|  COLOR MODELS BY CONTEXT                                         |
|  Print:  CMYK, Pantone (PMS), LAB                                |
|  Screen: RGB, HEX, HSL, HSB, Display P3                          |
|  Bridge: LAB / LCH (perceptually uniform)                        |
|                                                                  |
|  THE DESIGN PIPELINE:                                            |
|  Concept color -> Brand color spec -> Print spec + Screen spec   |
+------------------------------------------------------------------+
```

---

## Color Models

### The Physical Basis

```
LIGHT = ADDITIVE                PIGMENT = SUBTRACTIVE

Red + Green = Yellow            Cyan + Magenta = Blue
Red + Blue  = Magenta           Cyan + Yellow  = Green
Green + Blue = Cyan             Magenta + Yellow = Red
R + G + B   = White             C + M + Y = theoretic black
                                (+ K = real black)

DISPLAY (monitors, phones)      PRINT (ink on paper)
uses additive: RGB              uses subtractive: CMYK
start from black                start from white (paper)
add light = brighter            add ink = darker
```

### RGB

```
Red:   0-255
Green: 0-255
Blue:  0-255

rgb(255, 0, 0)   = pure red
rgb(0, 0, 255)   = pure blue
rgb(0, 0, 0)     = black
rgb(255,255,255) = white

HEX is just RGB in base-16:
#FF0000 = R:255 G:0 B:0 (red)
#000000 = black
#FFFFFF = white
#808080 = medium gray (R:128 G:128 B:128)
```

### HSL / HSB (designer-friendly RGB)

```
HSL: Hue, Saturation, Lightness
HSB: Hue, Saturation, Brightness (= Value = HSV)

HUE:        0-360 degrees on the color wheel
SATURATION: 0% (gray) to 100% (pure color)
LIGHTNESS:  0% (black) to 100% (white) -- HSL
BRIGHTNESS: 0% (black) to 100% (full color) -- HSB

WHY DESIGNERS PREFER HSL/HSB:
  Adjusting one dimension adjusts one attribute.
  To darken a color: decrease L (or B)
  To desaturate: decrease S
  To rotate hue: adjust H

  With RGB: changing one value shifts all three perceptual dims

hsl(0, 100%, 50%)    = pure red
hsl(120, 100%, 50%)  = pure green
hsl(240, 100%, 50%)  = pure blue
hsl(0, 0%, 50%)      = medium gray (hue irrelevant; S=0)
```

### CMYK

```
CMYK: Cyan, Magenta, Yellow, Key (Black)

Values: 0-100%

C:100 M:0 Y:0 K:0   = pure cyan
C:0 M:100 Y:0 K:0   = pure magenta
C:0 M:0 Y:100 K:0   = pure yellow
C:0 M:0 Y:0 K:100   = black

WHY K (black) when C+M+Y should make black?
  1. Real inks produce muddy dark brown, not true black
  2. Using 3 inks to print black wastes ink and takes longer to dry
  3. Black ink prints sharp text more cheaply
  4. K = Key (historically: the key printing plate, usually black)

CMYK gamut < RGB gamut
Many RGB colors cannot be reproduced in print.
Neon colors, vivid electric blues: lossy conversion.
```

### LAB and LCH

```
LAB (CIE L*a*b*, 1976)
  L: Lightness (0-100)
  a: green-red axis (-128 to +127)
  b: blue-yellow axis (-128 to +127)

  PERCEPTUALLY UNIFORM: equal numerical differences
  correspond to approximately equal perceived differences.
  RGB is NOT perceptually uniform.

LCH (Lightness, Chroma, Hue)
  Same as LAB but in cylindrical coordinates
  L: Lightness
  C: Chroma (saturation from center)
  H: Hue angle

WHY DESIGNERS CARE:
  CSS now has oklch() -- the designer-friendly version
  oklch(50% 0.2 240) = a blue at 50% lightness
  Manipulating oklch adjusts PERCEIVED color, not math color
  This is the future of CSS color in 2025+
```

### Pantone (PMS)

```
PANTONE MATCHING SYSTEM
  Numbered spot colors; guaranteed physical consistency
  PMS 185 C = a specific red; same everywhere in the world
  Mixed as single pre-formulated ink, not CMYK halftone

  USE WHEN:
  - Brand color must be exactly consistent (logos, packaging)
  - Printing only 1-2 colors (cheaper than 4-color process)
  - Metallic or fluorescent colors (CMYK cannot reproduce)

  COATED (C) vs UNCOATED (U)
  Same Pantone number looks different on:
  - Coated paper (glossy): brighter, more saturated
  - Uncoated paper: more matte, absorbed, duller
  Brand standards must specify C or U -- they are different.

  PMS -> CMYK CONVERSION IS APPROXIMATE
  The Pantone chip and the CMYK print will NOT match exactly.
```

---

## Color Harmony Models

```
COLOR WHEEL RELATIONSHIPS
--------------------------

COMPLEMENTARY
  Hues 180 degrees apart
  H:0 + H:180 (red + cyan)
  Maximum contrast; vibrates when adjacent at similar saturation
  Use: one dominant, one accent

SPLIT-COMPLEMENTARY
  One hue + two adjacent to its complement
  Less tension than complementary; more interest than analogous

ANALOGOUS
  3-5 hues adjacent on wheel (within 30-60 degrees)
  Harmonious, cohesive, calm
  Risk: lacking contrast; add a neutral or one complementary accent

TRIADIC
  Three equally spaced hues (120 degrees apart)
  Vibrant; requires careful dominance (one primary, two accent)

TETRADIC / SQUARE
  Four hues (90 degrees apart)
  Complex; usually dominance of one color + others as accents

MONOCHROMATIC
  Single hue, varying saturation and lightness
  Highly cohesive; sophisticated; limited in expressiveness
```

---

## Color in Brand Identity

### Defining a Brand Color System

```
BRAND COLOR ARCHITECTURE
-------------------------

PRIMARY PALETTE
  1-2 colors that carry the brand
  Must work in every context (print, screen, embroidery, molded plastic)
  Must work in black and white (reversals, embossing)
  Specified: Pantone + CMYK + RGB + HEX + LAB

SECONDARY PALETTE
  3-6 colors supporting the primary
  Used in backgrounds, charts, UI states, illustrations
  Must harmonize with primary; must provide sufficient variety

NEUTRAL PALETTE
  Black, white, 2-4 grays
  Background colors, text colors, UI surfaces
  Often most-used colors despite being "neutral"

FUNCTIONAL COLORS
  (in digital products)
  Success: green spectrum
  Warning: yellow/amber spectrum
  Error: red spectrum
  Info: blue spectrum
  These must meet accessibility contrast ratios

EXAMPLE ARCHITECTURE:
  Primary:    --color-brand: #0057FF (blue)
  Secondary:  --color-sky: #E8F2FF (light blue tint)
              --color-accent: #FF6B00 (orange complement)
  Neutrals:   --color-900: #111111
              --color-700: #444444
              --color-500: #888888
              --color-300: #CCCCCC
              --color-100: #F5F5F5
  Functional: --color-success: #22C55E
              --color-warning: #F59E0B
              --color-error: #EF4444
```

### Famous Brand Color Decisions

```
BRAND         COLOR           RATIONALE
-----         -----           ---------
Coca-Cola     PMS 485         Red = excitement, energy, warmth
              (specific red)  Established 1887; now owns the red in its category

IBM           IBM Blue        Reliability, corporate authority, technology
              PMS 2718C       "Nobody ever got fired for buying IBM"

Tiffany       Tiffany Blue    Exclusivity; unmistakable; trade-dressed
              (custom PMS)    Cannot be reproduced exactly in standard Pantone

UPS           Brown           (Originally to hide dirt on trucks)
              PMS 7518        Became: reliability, hard work, workhorse
              "What can Brown do for you?"

McDonald's    Red + Yellow    Red = appetite stimulation (hunger)
                              Yellow = happiness, children, speed

John Deere    Green + Yellow  Agricultural heritage; differentiation
              (since 1876)

Apple         Depends on era  Original rainbow: inclusivity, creativity
              -> monochrome   Post-Jobs return: minimalism, premiumness
              -> aluminum/    Current: neutrals with product color
                 space gray
```

---

## Color Contrast and Accessibility

```
WCAG 2.1 CONTRAST REQUIREMENTS
--------------------------------

For text on background:
  Level AA (minimum):
    Normal text (< 18pt regular / < 14pt bold): 4.5:1 ratio
    Large text (>= 18pt regular / >= 14pt bold): 3:1 ratio

  Level AAA (enhanced):
    Normal text: 7:1 ratio
    Large text: 4.5:1 ratio

  Non-text UI components (icons, form fields): 3:1 ratio

CONTRAST RATIO CALCULATION:
  Relative luminance of lighter color: L1
  Relative luminance of darker color: L2
  Ratio = (L1 + 0.05) / (L2 + 0.05)

  Black on white: (1.0 + 0.05) / (0.0 + 0.05) = 21:1
  #777777 on white: approximately 4.48:1 (barely passes AA)
  #888888 on white: approximately 3.54:1 (fails AA for normal text)

PRACTICAL IMPLICATION:
  Medium grays fail accessibility on white backgrounds.
  This is why much UI uses #333 or darker for body text.
  Do not use "nice soft gray" for body copy without checking.

TOOLS:
  whocanuse.com   (checks against simulated color blindness types)
  contrast-ratio.com
  Figma: built-in contrast checker in accessibility panel
```

---

## Color and Printing

### The Conversion Problem

```
RGB -> CMYK: GAMUT COMPRESSION
  Some RGB colors are outside the CMYK gamut.
  Electric blues, neon greens, vivid purples lose saturation.

  WORKFLOW:
  1. Design in RGB for screen
  2. Convert to CMYK before sending to print
  3. Check softproof (monitor shows predicted print result)
  4. Adjust colors that converted poorly
  5. Supply CMYK file to printer, not RGB

  OR: Design in CMYK from start (print-only work).

PANTONE BRIDGE
  Some printers offer "Pantone simulation" in CMYK
  (approximation). For brand-critical work: real Pantone.

PAPER MATTERS
  Same CMYK values print differently on:
  - Gloss coated: vibrant, saturated
  - Matte coated: softer, lower contrast
  - Uncoated white: absorbed, duller
  - Newsprint: significant dot gain, loses fine detail
```

---

## Color Psychology: What the Evidence Shows

Treat color psychology claims with skepticism; the actual evidence is thin.
Strong effects are real; specific claims are mostly folklore.

```
WELL-SUPPORTED EFFECTS
  High-contrast colors are more readable (physical, not cultural)
  Red has higher arousal response than blue (physiological, consistent)
  Colors associated with food appetite: red, yellow, orange
  (McDonald's didn't invent this; they found the research)

CULTURALLY VARIABLE (do not over-generalize)
  White = mourning in Japan, purity in West
  Green = nature (universal), Islam (cultural), money (US only)
  Red = danger/stop (traffic convention), luck (Chinese)
  Blue = corporate trust (Western convention)

APPLIED OBSERVATION (consistent across industries)
  Blue: finance, healthcare, tech (trust, calm, professional)
  Green: environment, health, finance (growth, safety)
  Orange: energy, youth, food, conversion (CTAs often orange)
  Black + gold: luxury (contrast + warmth)
  Pastels: healthcare, baby products, cosmetics

HONEST FRAMING:
  Color alone does not make a brand succeed.
  Consistent application makes a color "mean" a brand.
  Coca-Cola's red works because it has been red for 130 years,
  not because red inherently means Coca-Cola.
```

---

## Common Confusion Points

**"Design in RGB, print in CMYK"** -- True for conversion workflow, but the
correct approach for print-first work is to design in CMYK from the start.
Converting after design completion can ruin color relationships.

**"Pantone = CMYK"** -- No. Pantone is a separate color system. A Pantone-to-CMYK
conversion is an approximation. Brands that require exact color (Tiffany, Coca-Cola)
use actual Pantone inks for brand-critical applications.

**"Any two complementary colors harmonize"** -- Complementary colors at equal
saturation and similar lightness create optical vibration (the "buzzing" effect).
To use complements effectively: make one dominant and desaturate or lighten the other.

**"Accessibility means only considering contrast"** -- WCAG contrast is one criterion.
Color should not be the ONLY means of conveying information (color blindness affects
~8% of males). Use pattern, icon, or label alongside color coding.

---

## Decision Cheat Sheet

| I need to...                                    | Approach                           |
|-------------------------------------------------|------------------------------------|
| Define a brand's primary color                  | Specify Pantone, CMYK, RGB, HEX    |
| Check if text is accessible on a background     | Measure contrast ratio; target 4.5:1|
| Choose a secondary palette                      | Analogous for harmony; complementary for punch |
| Work with both print and screen versions        | Specify in both CMYK and RGB/HEX   |
| Understand why my print color looks wrong       | Check CMYK conversion; softproof   |
| Build a digital product color system            | Primary + secondary + neutrals + functional |
| Pick a color model for UI design                | HSL for manipulation; HEX for handoff |
| Understand CSS color future                     | OKLCH: perceptually uniform, wide gamut |
