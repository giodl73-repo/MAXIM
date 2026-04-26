# 09 — Variable Fonts: Fonts as Design Spaces

## The Big Picture

Variable fonts, introduced in the OpenType specification in September 2016, change the fundamental model of what a font file is. A static font encodes a single typeface instance. A variable font encodes a **multi-dimensional design space** — a mathematical structure from which any point can be instantiated on demand.

From a software engineering perspective, this is a parameterized function: `font(weight, width, slant, opticalSize, ...) → typeface_instance`. The parameters are continuous (not discrete), and the mapping is linear interpolation over glyph coordinates.

```
STATIC FONTS vs VARIABLE FONTS
────────────────────────────────────────────────────────────────────────────────

STATIC FONT MODEL:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Roboto-Thin.ttf         (weight: 100)   68 KB                           │
  │  Roboto-Light.ttf        (weight: 300)   68 KB                           │
  │  Roboto-Regular.ttf      (weight: 400)   68 KB                           │
  │  Roboto-Medium.ttf       (weight: 500)   68 KB                           │
  │  Roboto-Bold.ttf         (weight: 700)   68 KB                           │
  │  Roboto-Black.ttf        (weight: 900)   68 KB                           │
  │  Roboto-ThinItalic.ttf                   65 KB                           │
  │  Roboto-LightItalic.ttf                  65 KB                           │
  │  Roboto-Italic.ttf                       65 KB                           │
  │  Roboto-BoldItalic.ttf                   65 KB                           │
  │  ...                                                                     │
  │  Total: 12 files × ~66 KB = ~790 KB                                      │
  │  Instances available: discrete (100, 300, 400, 500, 700, 900)          │
  └──────────────────────────────────────────────────────────────────────────┘

VARIABLE FONT MODEL:
  ┌──────────────────────────────────────────────────────────────────────────┐
  │  Roboto[wght].woff2      (weight axis: 100–900)  ~180 KB                 │
  │  Total: 1 file × 180 KB = ~180 KB                                        │
  │  Instances available: ANY value from 100.0 to 900.0 (continuous)       │
  │  font-weight: 437;  → valid; precisely between Regular and Medium        │
  └──────────────────────────────────────────────────────────────────────────┘

SIZE COMPARISON:
  Static 12 files: ~790 KB
  Variable 1 file: ~180 KB
  Ratio: ~4.4× smaller; also only 1 HTTP request vs 12

  Note: variable font may be somewhat larger than single static font
  but dramatically smaller than the whole family

────────────────────────────────────────────────────────────────────────────────
```

---

## How Variable Fonts Work: The Math

```
VARIABLE FONT INTERPOLATION — THE MECHANISM
──────────────────────────────────────────────────────────────────────────────

MASTERS (design extremes):
  A variable font contains 2+ complete glyph designs (masters)
  Each master is a full set of glyph outlines
  For a single axis (weight):
    Master 1: Light (weight=100) — all glyph outlines at thin form
    Master 2: Bold (weight=700) — all glyph outlines at heavy form

DELTA ARRAYS:
  For each glyph point, for each axis direction:
    Delta = Master_extreme - Default_position
  Stored as compact delta arrays in the gvar table (TrueType)
  or CFF2 variation data (PostScript/CFF)

INTERPOLATION:
  At any requested weight value:
    normalized_weight = (requested - min) / (max - min)  // 0.0 to 1.0
    For each glyph point (x, y):
      point.x = default.x + normalized_weight × delta.x
      point.y = default.y + normalized_weight × delta.y

  This is linear interpolation over glyph coordinate space.
  Every control point in every glyph moves proportionally.

VISUAL RESULT:
  Weight = 100: point positions at Light master
  Weight = 400: point positions at default (Regular)
  Weight = 700: point positions at Bold master
  Weight = 550: halfway between Regular and Bold
  Weight = 437: precisely 37/300 = 12.3% from Regular toward Bold

TWO-AXIS INTERPOLATION (weight × width):
  glyph_point = default + w_norm × w_delta + wd_norm × wd_delta
                + w_norm × wd_norm × wwd_delta  ← bilinear correction term
  (if designers supplied a 4-master setup: Light-Normal, Bold-Normal,
   Light-Condensed, Bold-Condensed)
  The bilinear term corrects for non-linear interaction between axes

CONSTRAINT: POINT COMPATIBILITY
  ALL masters must have IDENTICAL contour structure:
  Same number of contours, same number of points, same winding direction
  Same composite structure (if composite glyph)
  INCOMPATIBLE glyphs cannot interpolate → font design constraint
  This is why designing variable fonts is harder than static:
  Every change in one master requires matching changes in all masters

──────────────────────────────────────────────────────────────────────────────
```

---

## OpenType Variable Font Tables

```
VARIABLE FONT SPECIFIC TABLES
──────────────────────────────────────────────────────────────────────────────

fvar (Font Variations Table):
  Defines the axes and their parameters:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Axis record:                                                    │
  │   axisTag:    4-byte identifier (e.g., 'wght')                  │
  │   minValue:   minimum allowed value (e.g., 100)                 │
  │   defaultValue: default (e.g., 400)                             │
  │   maxValue:   maximum (e.g., 900)                               │
  │   axisNameID: index into name table for human-readable name     │
  │                                                                 │
  │ Named instances (optional):                                     │
  │   "Light"   → wght=300                                          │
  │   "Regular" → wght=400                                          │
  │   "Bold"    → wght=700                                          │
  │   (These map to CSS font-weight named values)                   │
  └─────────────────────────────────────────────────────────────────┘

gvar (TrueType variation data):
  Glyph variation deltas for TrueType outlines
  Contains delta arrays per glyph per axis
  Compact delta encoding (many points have zero delta)

CFF2 (PostScript variation data):
  CFF2 table: PostScript outlines with embedded variation data
  Used when the font has CFF (cubic Bézier) outlines

HVAR/VVAR (Horizontal/Vertical Metrics Variations):
  Advance widths and sidebearings can vary with axes
  A condensed instance has smaller advance widths than extended

MVAR (Metrics Variations):
  Font-wide metric variations: cap height, x-height, line gap, etc.
  These vary as axes change (a condensed Bold might have different
  line gap than Regular Extended)

STAT (Style Attributes Table):
  Maps named instances to visual style names
  Enables CSS to find "Bold" instance from a font with no bold static file
  Critical for variable fonts used as system fonts

──────────────────────────────────────────────────────────────────────────────
```

---

## Standard Axes

The OpenType specification defines registered axes with 4-character lowercase tags. Registered axes have normalized CSS mappings:

```
REGISTERED AXES
──────────────────────────────────────────────────────────────────────────────

wght — Weight
  Range: 1–1000 (in practice: 100–900)
  CSS mapping: font-weight maps to wght
  font-weight: 450; → wght=450 (CSS accepts arbitrary values since CSS Fonts L4)
  Examples: 100=Thin, 300=Light, 400=Regular, 700=Bold, 900=Black

wdth — Width
  Range: 0–∞ (typically 50–200; 100=normal)
  CSS mapping: font-stretch maps to wdth
  font-stretch: 75%; → wdth=75 (condensed)
  font-stretch: 125%; → wdth=125 (expanded)
  Examples: 50=Ultra Condensed, 75=Condensed, 100=Normal, 125=Expanded

ital — Italic
  Range: 0 to 1 (binary — not continuous for most designs)
  CSS mapping: font-style: italic; → ital=1
  Note: TRUE italic = separate glyph design (not slant)
  Some fonts have intermediate ital values with design variations
  Differs from slnt (which is mechanical slant of existing forms)

slnt — Slant
  Range: -90 to 90 degrees
  CSS mapping: font-style: oblique Ndeg; → slnt=-N (note sign convention)
  Negative slnt = forward-leaning (italic direction)
  0 = upright; used for oblique sans-serif variants
  Example: font-style: oblique -10deg; → slnt=-10

opsz — Optical Size
  Range: type size in points (typically 8–144)
  CSS mapping: font-optical-sizing: auto; (browser uses current font-size)
  The font adjusts design details based on intended rendering size:
    Small opsz (8): thicker strokes, larger counters, more robust serifs
    Large opsz (72): more delicate, high contrast, fine detail
  Most important axis that is often forgotten
  Example: font-optical-sizing: none; (override; use single design)

──────────────────────────────────────────────────────────────────────────────

CUSTOM AXES (not registered; lowercase 4-letter tags convention):
  Registered axes: lowercase 4 letters (wght, wdth, ital, slnt, opsz)
  Custom axes: UPPERCASE 4 letters by convention (GRAD, CASL, MONO, etc.)

  GRAD — Grade
    Adjust visual weight WITHOUT changing advance widths
    Useful for: dark/light mode switch (text reflows if weight changes;
    grade changes visual weight but not layout)

  CASL — Casual (Recursive font)
    0 = linear/geometric; 1 = casual/script-influenced
    Unique to the Recursive typeface

  MONO — Monospace
    0 = proportional; 1 = monospace
    Recursive can switch between proportional and monospace!

  CRSV — Cursive
    Activate cursive letter forms (Recursive)

──────────────────────────────────────────────────────────────────────────────
```

---

## CSS Variable Font API

```
CSS VARIABLE FONT API
──────────────────────────────────────────────────────────────────────────────

HIGH-LEVEL PROPERTIES (preferred):
  font-weight: 450;             /* maps to wght axis */
  font-stretch: 80%;            /* maps to wdth axis */
  font-style: italic;           /* maps to ital=1 */
  font-style: oblique -8deg;   /* maps to slnt=-8 */
  font-optical-sizing: auto;    /* maps opsz to computed font-size */
  font-optical-sizing: none;    /* disable; use default opsz */

LOW-LEVEL (for custom axes or fine control):
  font-variation-settings: 'wght' 650, 'wdth' 80;
  font-variation-settings: 'wght' 400, 'GRAD' -25;
  font-variation-settings: 'wght' 350, 'wdth' 90, 'opsz' 24;

IMPORTANT: font-variation-settings overrides high-level properties
for the same axis. Use one or the other per axis:
  /* WRONG: conflicting */
  font-weight: 700;                          /* → wght=700 */
  font-variation-settings: 'wght' 500;       /* → wght=500; overrides! */

  /* RIGHT: use low-level only when needed for non-standard axes */
  font-weight: 700;                          /* standard weight control */
  font-variation-settings: 'GRAD' -25;       /* non-standard axis only */

ANIMATION (a killer feature):
  Variable font axes are animatable in CSS:

  @keyframes weight-pulse {
    0%   { font-weight: 100; }
    50%  { font-weight: 900; }
    100% { font-weight: 100; }
  }

  .animated-text {
    animation: weight-pulse 2s ease-in-out infinite;
  }

  This creates smooth weight animation — impossible with static fonts.
  Performance: browser can interpolate in GPU; no font file re-download.
  Use case: loading indicators; decorative headings; emphasis effects.
  Note: avoid animating text users are trying to read.

RESPONSIVE WEIGHT:
  Adjust weight based on screen size (thin strokes disappear small):
  h1 { font-weight: 700; }
  @media (max-width: 480px) {
    h1 { font-weight: 800; }  /* heavier on mobile; small screen */
  }

  With variable font this is continuous, not a step change.

──────────────────────────────────────────────────────────────────────────────
```

---

## @font-face Declaration for Variable Fonts

```
LOADING A VARIABLE FONT WITH @font-face
──────────────────────────────────────────────────────────────────────────────

/* Basic variable font loading */
@font-face {
  font-family: 'Inter';
  src: url('/fonts/Inter.var.woff2') format('woff2 supports variations'),
       url('/fonts/Inter.var.woff2') format('woff2');
  font-weight: 100 900;      /* Declare range (not single value) */
  font-style: normal;
  font-display: swap;
}

/* For a font with both roman and italic in one file */
@font-face {
  font-family: 'Source Sans 3';
  src: url('/fonts/SourceSans3VF.woff2') format('woff2 supports variations'),
       url('/fonts/SourceSans3VF.woff2') format('woff2');
  font-weight: 200 900;
  font-style: normal;
}

@font-face {
  font-family: 'Source Sans 3';
  src: url('/fonts/SourceSans3VF-Italic.woff2') format('woff2 supports variations'),
       url('/fonts/SourceSans3VF-Italic.woff2') format('woff2');
  font-weight: 200 900;
  font-style: italic;
}

/* Usage: */
body {
  font-family: 'Inter', system-ui, sans-serif;
  font-optical-sizing: auto;  /* enable opsz if the font supports it */
}

h1 { font-weight: 800; }
h2 { font-weight: 700; }
p  { font-weight: 400; }
strong { font-weight: 600; }

/* All from a single file download */

FORMAT HINT: 'woff2 supports variations':
  Browser feature detection: load this only if browser supports variable fonts
  Fallback (old browsers): load static .woff file instead
  Current state: all major browsers support variable fonts; fallback rarely needed
──────────────────────────────────────────────────────────────────────────────
```

---

## Notable Variable Fonts

```
RECOMMENDED VARIABLE FONTS
──────────────────────────────────────────────────────────────────────────────

Inter (Rasmus Andersson, 2017; variable 2019)
  Axes: wght (100–900)
  Open source (SIL OFL); free via Google Fonts
  Designed specifically for screen UI
  Excellent legibility; well-hinted; widely used in software interfaces
  Used by: GitHub, Mozilla, many apps
  Download: fonts.google.com/specimen/Inter
  File size: ~270KB for variable; replaces 9+ static fonts

Recursive (Arrow Type / Stephen Nixon, 2020)
  Axes: wght (300–1000), CASL (0=linear, 1=casual), MONO (0=proportional, 1=mono)
         CRSV (0–1 cursive), slnt (-15 to 0)
  Unique: can be both proportional AND monospace in one file
  Open source (SIL OFL); free via Google Fonts
  Excellent for developer contexts (can use for both UI and code)

Source Sans 3 (Paul Hunt, Adobe; variable 2021)
  Axes: wght (200–900)
  Open source; free via Google Fonts
  Adobe's principal open-source typeface family
  Companion: Source Serif 4, Source Code Pro

Roboto Flex (Google, 2021)
  Axes: wght, wdth, slnt, opsz, GRAD, plus several custom axes
  Complete redesign of Roboto for variable; very comprehensive axis system
  Free; Google Fonts

Literata (TypeTogether, Google, 2019)
  Axes: wght (300–900), opsz (6–72), ital (0–1)
  Optimized for e-reading; excellent opsz implementation
  Used by Google Play Books

Fraunces (Undercase Type, 2020)
  Axes: wght (100–900), SOFT (0–100), WONK (0–1), opsz (9–144)
  Display serif with unusual axes for personality adjustment
  Free via Google Fonts; excellent for headlines

JetBrains Mono (JetBrains, 2020)
  Axes: wght (100–800), ital (0–1)
  Programming monospace; variable weight
  Free; designed to reduce eye strain in code editors
  Excellent I/l/1 and O/0 distinction

GitHub Monaspace (GitHub, 2023)
  Five variable monospace typefaces (Neon, Argon, Xenon, Radon, Krypton)
  Support "texture healing" (proportional spacing within monospace grid)
  Free (open source)

──────────────────────────────────────────────────────────────────────────────
```

---

## Performance Analysis

```
PERFORMANCE IMPLICATIONS
──────────────────────────────────────────────────────────────────────────────

HTTP REQUEST SAVINGS:
  Static fonts (full family): 4–12 HTTP requests
  Variable font: 1–2 HTTP requests (roman + italic)
  Impact: significant at initial load (HTTP/1.1); moderate on HTTP/2
  (HTTP/2 multiplexing reduces per-request overhead)

FILE SIZE MATH (realistic example):
  Roboto static family (5 weights + italic):
    Roboto-Thin.woff2:         45 KB
    Roboto-Light.woff2:        46 KB
    Roboto-Regular.woff2:      46 KB
    Roboto-Bold.woff2:         46 KB
    Roboto-Black.woff2:        46 KB
    Roboto-Italic.woff2:       44 KB
    Roboto-BoldItalic.woff2:   44 KB
    Total:                    317 KB (7 files)

  Roboto Flex (variable, full):
    RobotoFlex.woff2:         127 KB (1 file, all axes)

  Savings: 190 KB (~60% reduction); 6 fewer HTTP requests

RENDERING PERFORMANCE:
  Variable font rendering: browser computes interpolated outlines at render time
  Historically: slight CPU overhead vs pre-computed static outlines
  Modern hardware (2020+): interpolation happens in GPU; imperceptible
  Animation: frame-by-frame interpolation; GPU-accelerated; smooth

CACHING:
  One variable font file = one cache entry
  Static fonts: each weight/style is a separate cache entry
  If user visits multiple pages using different weights:
    Static: each new weight = potentially new request
    Variable: already cached; any weight available from cached file

FONT-DISPLAY INTERACTION:
  Variable fonts work with all font-display strategies
  swap is most common
  Block period: only when font is "invisible" (font-display: block)
  With Inter Variable + font-display: swap: usually loads before first paint

SUBSETTING VARIABLE FONTS:
  Unicode-range subsetting: works same as static
  Weight subsetting: can subset to specific weight range
  Tool: pyftsubset (fonttools) — works with variable fonts
  Google Fonts: automatically subsets variable fonts by unicode-range
  Warning: don't over-subset; may defeat the flexibility benefit

──────────────────────────────────────────────────────────────────────────────
```

---

## Optical Size Axis in Practice

The `opsz` axis deserves extra attention — it is the axis most type designers care about and most software implementations under-use:

```
OPTICAL SIZE — THE FORGOTTEN AXIS
──────────────────────────────────────────────────────────────────────

WHAT IT SOLVES:
  A font designed for body text (10pt) looks different at display size (48pt)
  Historical solution: separate masters for each optical size
  Garamond had: Text, Subhead, Display, Caption versions
  Different x-heights, stroke widths, spacing, proportions per size

  With opsz axis: these variations are interpolated from a continuous scale

DESIGN DIFFERENCES AT DIFFERENT opsz VALUES:

  opsz = 8 (caption size):
    Larger x-height (for legibility at small size)
    Thicker strokes (thin strokes disappear small)
    More open counters (same reason)
    More generous letter-spacing (easier to distinguish)
    Shorter ascenders/descenders (fit in limited space)

  opsz = 24 (body text):
    Standard design; balanced proportions

  opsz = 72 (display heading):
    Lower x-height (more classical proportions at large size)
    Higher stroke contrast (thin strokes visible; dramatic effect)
    Tighter letter-spacing (characters too far apart at large size)
    More delicate serifs/terminals

CSS USAGE:
  font-optical-sizing: auto;
  /* Browser automatically passes current font-size as opsz value */
  /* If body is 16px, opsz=16 is used */
  /* If heading is 48px, opsz=48 is used */
  /* REQUIRES font to have opsz axis */

  font-optical-sizing: none;
  /* Use the default opsz value regardless of rendering size */
  /* Use when you want consistent design across sizes (unusual) */

WHICH FONTS HAVE opsz:
  Literata: opsz 6–72
  Roboto Flex: opsz 8–144
  Source Serif 4: opsz 8–60
  Fraunces: opsz 9–144
  Most fonts: NO opsz axis (still single design for all sizes)
  Note: the absence is a quality gap; opsz requires significant design work

──────────────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Scenario | Recommendation | Notes |
|----------|----------------|-------|
| Replace 4+ static weights | Variable font | Major performance win |
| Only need one weight | Static font | Simpler; may be smaller |
| Animated weight/width | Variable font | Only option |
| Responsive weight adjustment | Variable font | Use font-weight CSS |
| Need specific opsz at display | Variable font (with opsz) | Few fonts support this |
| Need Inter at 5 weights | Inter Variable | 1 file; open source |
| Need code + UI same font | Recursive | Mono + proportional in one |
| Maximum browser compat | Static with variable fallback | Rarely needed today |
| Custom axis (GRAD, CASL) | font-variation-settings | Low-level API |
| System font; no web font | System font stack | No download; always best perf |

---

## Common Confusion Points

**font-weight: 450 is not interpolated between two static font files**
For font-weight to produce a weight of 450, the font must either (a) be a variable font with a wght axis that includes 450, or (b) have a named static instance at 450. If you specify `font-weight: 450` and load a static Regular (400) + Bold (700), the browser will pick the closer match (400), not interpolate. Variable fonts are required for continuous weight values.

**font-variation-settings doesn't inherit properly**
Unlike `font-weight`, `font-variation-settings` does NOT inherit by default in the way you might expect. If a parent sets `font-variation-settings: 'wght' 700` and a child resets with `font-variation-settings: 'GRAD' 50`, the wght setting is LOST — not merged. The solution: use CSS custom properties as a layer:
```css
:root { --font-wght: 400; }
.heavy { --font-wght: 700; }
* { font-variation-settings: 'wght' var(--font-wght); }
```

**Variable fonts cost more to design**
From the type designer's perspective, a variable font requires designing multiple masters (typically 2–4 per axis) AND ensuring all masters have compatible point structures. This can 2–5× the design work compared to a single static weight. This is why high-quality variable fonts are not free, and why the axis choices matter to designers.

**Not all axes are continuous**
The `ital` axis is typically binary (0 or 1) because italic is usually a separate glyph design, not a slant interpolation. You interpolate between roman and italic glyphs only if the designer explicitly designed intermediate states — most don't. The `slnt` axis IS continuous because it is a mechanical transformation of the existing outlines. These are both rotation/slant-related but completely different in design philosophy.
