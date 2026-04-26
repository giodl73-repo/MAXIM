# Typography in Graphic Design

## The Big Picture

```
+------------------------------------------------------------------+
|                  TYPOGRAPHY IN GRAPHIC DESIGN                    |
|                                                                  |
|  TYPE DESIGN        TYPOGRAPHY           TYPESETTING             |
|  (making fonts)     (using type)         (production)            |
|  Glyphs, FontLab    Hierarchy, spacing   Kerning, tracking       |
|  Bezier curves      Layout decisions     InDesign, CSS           |
|                                                                  |
|  TYPEFACE CATEGORIES                                             |
|  Serif    Sans-serif   Monospace   Display   Script              |
|                                                                  |
|  KEY SYSTEMS                                                     |
|  Type scale | Leading | Kerning/Tracking | Measure | Weight      |
|                                                                  |
|  HISTORICAL ARC                                                  |
|  Metal type -> Phototype -> Digital (PostScript) -> Variable     |
+------------------------------------------------------------------+
```

---

## Typeface Taxonomy

```
+---------------------------+-----------------------------------+
| CATEGORY                  | CHARACTERISTICS / USE             |
+---------------------------+-----------------------------------+
| Old Style Serif           | Low contrast, angled stress,      |
| (Garamond, Caslon,        | bracketed serifs. Long text,      |
|  Palatino)                | traditional feel.                 |
+---------------------------+-----------------------------------+
| Transitional Serif        | Higher contrast, more vertical    |
| (Times New Roman,         | stress. Newspapers, books.        |
|  Baskerville, Century)    |                                   |
+---------------------------+-----------------------------------+
| Modern / Didone Serif     | High contrast, hairline serifs,   |
| (Bodoni, Didot)           | vertical stress. Fashion, luxury, |
|                           | display. Difficult at small sizes.|
+---------------------------+-----------------------------------+
| Slab Serif                | Low contrast, thick square serifs.|
| (Rockwell, Clarendon,     | Headlines, posters, Victorian     |
|  Courier)                 | revival, westerns.                |
+---------------------------+-----------------------------------+
| Grotesque Sans            | Early geometric reduction,        |
| (Akzidenz-Grotesk,        | irregular in detail. Workhorse.  |
|  Franklin Gothic)         |                                   |
+---------------------------+-----------------------------------+
| Neo-Grotesque / Humanist  | Optically refined, larger x-height|
| Sans                      | Helvetica, Arial (neutral corp.)  |
| (Helvetica, Univers,      | Gill Sans, Frutiger (human feel)  |
|  Frutiger, Gill Sans)     |                                   |
+---------------------------+-----------------------------------+
| Geometric Sans            | Circle/square construction basis. |
| (Futura, Avenir,          | Clean, modern, cold when overused.|
|  Bauhaus-influenced)      |                                   |
+---------------------------+-----------------------------------+
| Script / Calligraphic     | Simulate handwriting. Low legibility
| (various)                 | at small sizes. Invitation, luxury.|
+---------------------------+-----------------------------------+
| Display / Decorative      | One job: headlines at large size. |
| (hundreds of variants)    | Never use for body text.          |
+---------------------------+-----------------------------------+
| Variable Fonts            | Single file, multiple axes        |
| (modern)                  | (weight, width, slant). CSS font- |
|                           | variation-settings.               |
+---------------------------+-----------------------------------+
```

---

## Type Anatomy

```
    Cap Height                        ASCENDER
    |                                 |
    |  B  A  S  E  L  I  N  E         | d  f  h  k  l  t
    |                                    |
    +-- x-height (lowercase body) -------+
                                         |
                                         | DESCENDER
                                         | g  j  p  q  y

PARTS OF A LETTERFORM
  Ascender   Stroke above x-height (h, d, b)
  Descender  Stroke below baseline (g, p, y)
  x-height   Height of lowercase 'x'; readability lever
  Cap height Height of capital letters
  Serif      Terminal stroke (or its absence)
  Stem       Main vertical stroke
  Bowl       Curved enclosure (d, b, p, o)
  Counter    Interior space of a letter (inside 'o', 'p')
  Aperture   Opening in a letter (c, e, S)
  Stress     Angle of thick/thin stroke variation
  Ear        Small stroke on 'g', 'r'
  Spur       Small projection (on G, sometimes)
```

---

## Type Measurement System

```
POINT SYSTEM (print)
  1 point = 1/72 inch
  12 points = 1 pica
  6 picas = 1 inch

  Type is specified: size/leading
  9/11 = 9pt type, 11pt leading
  12/15 = 12pt type, 15pt leading (common)
  "Solid" = 12/12 (no extra space)

WEB / SCREEN
  px = physical pixels (but logical on high-DPI)
  em = relative to current element font-size
  rem = relative to root font-size (preferred for predictability)
  % = percentage of parent

  Relationship to print: 1pt ~ 1.333px at 96dpi

RULE OF THUMB FOR LEADING
  Body text: leading = type size x 1.2 to 1.5
  9pt body: 11-13.5pt leading
  At wider measures: increase leading
  At narrower measures: tighter leading acceptable
```

---

## Type Hierarchy

A type hierarchy communicates document structure visually before content is read.

```
HIERARCHY LEVELS (typical document)
-------------------------------------
H1 - Title / Display
     36-72pt, Bold or Heavy, little/no leading
     Sets tone; most distinctive type choice

H2 - Section Head
     18-24pt, Bold
     Clear step down from H1

H3 - Sub-section
     14-16pt, Bold or Medium
     Another step down; may match body in face

Body Text
     9-12pt, Regular, 11-16pt leading
     Maximum readability; optically neutral
     65-75 characters per line (optimal measure)

Caption / Label
     7-9pt, same face or contrasting face
     Often different weight (lighter) or style (italic)

Page Number / Running Header
     7-9pt, light, subdued
     Navigation, not content

CONTRAST WITHIN HIERARCHY:
  Size contrast: each level distinctly different
  Weight contrast: Regular -> Bold -> ExtraBold
  Color contrast: dark -> lighter
  Type style: Roman vs. Italic
  Face change: serif body + sans-serif head (classic contrast)
```

---

## Typographic Spacing

### Tracking and Kerning

```
TRACKING (letter-spacing in CSS)
  Uniform adjustment of space between ALL characters in a range.

  NEVER track body text tighter (loss of readability)
  Tracking body text looser (slightly) can help at small sizes

  DISPLAY TYPE:
  Large headlines often need NEGATIVE tracking (tighter)
  because optical spacing at large size looks too wide

  ALL CAPS: always add tracking (+50 to +100 in many tools)
  Uppercase letters have no ascenders/descenders = naturally
  tight; they need extra tracking to read comfortably.

KERNING
  Adjustment of space between SPECIFIC character PAIRS.

  Problem pairs: AV, WA, To, Te, FA, LT, PA, VA, Yo

  +--+--+--+
  |A |V |  |  Without kerning: gap looks large between A-V
  +--+--+--+

  |AV|   Optically kerned: visual center of mass balanced

  Fonts include kerning tables; professional fonts have
  thousands of kern pairs. Bad fonts have few.

  AUTO vs MANUAL kerning:
  For body text: use auto/optical kerning
  For display type at large sizes: manually check A-V, T-o, etc.
```

### Measure (Line Length)

```
OPTIMAL READING MEASURE
  65-75 characters per line for single column
  45-65 for multi-column (narrower columns)

  Too short: eye jumps back too often; choppy rhythm
  Too long: eye loses track of next line start (losing your place)

  Test: select a line of body text; count characters.
  If > 80 or < 45, reconsider column width or type size.

IN WEB CSS:
  max-width: 65ch;   (ch unit = width of '0' in current font)
```

---

## Type and Color

```
CONTRAST REQUIREMENTS
  WCAG AA:  4.5:1 contrast ratio (text vs background)
  WCAG AAA: 7:1 for body text
  Large text (18pt+): 3:1 minimum

  CHECK WITH: WebAIM Contrast Checker, Figma accessibility plugins

  Black text on white: 21:1 (maximum)
  #333333 on white:    12.6:1 (slightly softer, still accessible)
  Medium gray on white: often fails -- check before using

TYPE ON IMAGERY
  Problem: legibility varies with image
  Solutions:
  1. Text box with background (opacity or solid)
  2. Image darkening overlay
  3. Drop shadow (use sparingly; looks cheap)
  4. Ensure type always lands on consistent tone area of image

REVERSED TYPE (light on dark)
  Works well for display sizes
  For body text: increase tracking slightly
  Avoid thin serifs reversed -- hairlines disappear
```

---

## Typographic Systems: Picking a Type Pair

The most common design decision: which typeface(s) to use together.

```
STRATEGIES FOR PAIRING

SAME FAMILY (safest)
  Use one superfamily with multiple weights/widths
  IBM Plex (serif + sans + mono): designed to work together
  Freight (display + text + micro sizes): same DNA

SERIF + SANS CONTRAST
  Classic combination: contrasting but harmonious
  Method:
    1. Match x-heights approximately
    2. Match overall "color" (weight / texture on page)
    3. Contrast in form (geometric sans + humanist serif)

  Examples that work:
    Minion (serif) + Myriad (sans) -- Adobe's internal pair
    Garamond + Helvetica -- classic editorial
    Freight Text + Freight Sans -- same designer

HISTORICAL PERIOD MATCH
  Both faces from same era share proportional DNA
  Baskerville (1750s) + a geometric sans (1920s) = clash
  Baskerville + a transitional sans = better

ONE FACE ONLY (advanced minimalism)
  Swiss style often: one typeface, multiple weights
  Helvetica Regular + Helvetica Bold + Helvetica Light
  Works when: face is a superfamily with many weights
  Fails when: face has only 2-3 weights (no range)

DISPLAY FACE + WORKHORSE BODY
  Distinctive display for headlines (brand expression)
  Legible, neutral body (GT America, Source Serif, etc.)
  This is the majority of brand typography today
```

---

## Typography in the Design System Context

Design systems (what large digital products use) formalize typography:

```
DESIGN TOKEN APPROACH
  --font-size-base: 16px
  --font-size-sm: 14px
  --font-size-lg: 20px
  --font-size-xl: 24px
  --font-size-2xl: 32px
  --font-size-3xl: 48px

  --line-height-body: 1.5
  --line-height-heading: 1.1
  --font-weight-regular: 400
  --font-weight-medium: 500
  --font-weight-bold: 700

  These tokens bridge design (Figma styles) to code (CSS variables).
  Same mental model as configuration over hardcoding.

TYPOGRAPHIC SCALE SYSTEMS
  Modular scale: each step = previous x ratio
  Ratio 1.25 (Major Third): 12, 15, 19, 24, 30, 37px
  Ratio 1.414 (augmented 4th): 12, 17, 24, 34, 48px

  Tools: typescale.com, type-scale.com
  This is the same logic as musical intervals --
  an MIT TCS background means you'll recognize the
  mathematical elegance immediately.
```

---

## Common Confusion Points

**"Serif is for print, sans-serif is for screen"** -- This was true on low-
resolution screens (pre-2010 roughly). On Retina/HiDPI screens, serifs render
cleanly. The distinction is now about aesthetics and brand, not readability.

**"More typefaces = richer design"** -- No. Two typefaces well-chosen and
consistently applied > five typefaces randomly mixed. Restraint in type selection
is a mark of typographic maturity.

**"Bold means emphasis"** -- Bold is ONE emphasis tool. Italics, size increase,
color, and letter-spacing all work. Using all simultaneously destroys hierarchy.

**"Leading just means line spacing"** -- Leading (from the metal type era -- strips
of lead inserted between lines) is specified from baseline to baseline, not as
whitespace between lines. 12/15 means 3pt of actual space between the bottom of
descenders and the top of ascenders on the next line.

**"Variable fonts are just one font"** -- Variable fonts contain a design space with
axes (weight, width, optical size, slant). A font file can interpolate to any point
in that space. This is a meaningful technical difference with performance implications
(one HTTP request vs. many).

---

## Decision Cheat Sheet

| Problem                              | Solution                                   |
|--------------------------------------|--------------------------------------------|
| Text is hard to read at small size   | Increase x-height; increase leading        |
| Headline looks too loose at 60px     | Add negative tracking (-20 to -40)         |
| Two typefaces look wrong together    | Check: similar x-height? Similar color?    |
| Serif vs sans-serif choice           | Brand tone: traditional/authoritative (serif) |
|                                      | Modern/neutral/technical (sans)            |
| Body text measure feels wrong        | Count characters per line; target 65-75    |
| Type on image is unreadable          | Add scrim overlay; don't use drop shadow   |
| Choosing a type scale for web        | Use modular scale 1.25 or 1.333            |
| Corporate design, "safe" choice      | Inter, Helvetica Neue, GT America, IBM Plex|
| Premium editorial feel               | Freight Text, Tiempos Text, Mercury        |
