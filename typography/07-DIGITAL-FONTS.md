# 07 — Digital Fonts: PostScript, TrueType, OpenType

## The Big Picture

Digital fonts are programs. Not metaphorically — PostScript Type 1 fonts contain actual bytecode executed by an interpreter. TrueType fonts contain a bytecode instruction set that executes on the rasterizer. Understanding the technical substrate of digital type gives you the vocabulary to reason about performance, rendering quality, and format choice.

```
DIGITAL FONT FORMAT TIMELINE AND RELATIONSHIPS
────────────────────────────────────────────────────────────────────────────────

1982  PostScript language (Adobe)
      ↓
1984  PostScript Type 1 (Adobe) — cubic Bézier outlines
      Monopoly: encrypted; only Adobe tools could create
      ↓
1988  PostScript Type 3 — unencrypted; user-definable; no hinting
      ↓
1991  TrueType (Apple + Microsoft) — quadratic B-spline outlines
      Challenge to Adobe's Type 1 monopoly
      ↓
1990  Type 1 decrypted (Adobe released specification)
      ↓
1994  Multiple Master (Adobe) — interpolatable Type 1 (precursor to variable)
      ↓
1996  OpenType specification (Adobe + Microsoft) — unified container
      CFF (Type 1/PostScript) OR glyf (TrueType) outlines inside OpenType
      ↓
2000  OpenType publicly released; adoption begins
      ↓
2000  ClearType (Microsoft) — subpixel rendering for LCD screens
      ↓
2010  WOFF (Web Open Font Format) — OpenType with metadata + zlib compression
      ↓
2013  WOFF2 — OpenType with Brotli compression (~30% smaller than WOFF)
      ↓
2016  OpenType Variable Fonts — design spaces, single file for families
      ↓
2020  Variable fonts: universal browser support

────────────────────────────────────────────────────────────────────────────────
```

---

## Mathematical Foundations: Curves in Type

Before getting into format specifics, the math that underlies all digital type:

```
BÉZIER CURVES AND B-SPLINES
──────────────────────────────────────────────────────────────────────────────

PARAMETRIC CURVES:
  A curve expressed as a function of parameter t (0 ≤ t ≤ 1)
  P(t) = position on curve when t=0 is start, t=1 is end
  The curve is smooth, differentiable, computable

CUBIC BÉZIER (PostScript/CFF):
  4 control points: P0, P1, P2, P3
  P0 = on-curve start point
  P1 = off-curve handle (tangent direction from P0)
  P2 = off-curve handle (tangent direction into P3)
  P3 = on-curve end point

  B(t) = (1-t)³P0 + 3(1-t)²tP1 + 3(1-t)t²P2 + t³P3

  Visual:
     P1 ●              ● P2
       \                 /
    P0 ●─────────────────● P3
        (on-curve)          (on-curve)
       (off-curve handles shown as ●)

  Property: the curve passes through P0 and P3
            P1 and P2 are "handles" that pull the curve

QUADRATIC B-SPLINE (TrueType/glyf):
  3 control points per segment: P0, P1, P2
  P0 = on-curve
  P1 = off-curve (single handle)
  P2 = on-curve

  Q(t) = (1-t)²P0 + 2(1-t)tP1 + t²P2

  Visual:
        ● P1 (off-curve)
       / \
  P0 ●   ● P2
  (on)   (on)

  Property: uses fewer control points per segment
  But: cubic has more expressive power; complex curves need more segments

PRACTICAL DIFFERENCES:
  Cubic (PostScript): one segment for complex letter curve
  Quadratic (TrueType): may need 2–3 segments for same curve
  Modern tools: internally use cubic; TrueType converted on export
  Rasterization speed: historically quadratic faster; modern hardware: negligible
  Quality: functionally equivalent at printing resolutions

──────────────────────────────────────────────────────────────────────────────
```

---

## PostScript Type 1 (Adobe, 1984)

PostScript was not designed as a font format — it was designed as a page description language. Adobe's insight: describe the page as a program; the printer (or imagesetter) executes the program at its native resolution.

```
POSTSCRIPT ARCHITECTURE
──────────────────────────────────────────────────────────────────────────────

POSTSCRIPT LANGUAGE (1982):
  Stack-based interpreted language (like Forth)
  Objects: integers, reals, strings, arrays, dictionaries, procedures
  Every page description is a PostScript program
  Printer has a PostScript interpreter built in
  Device-independent: same .ps file → 300dpi laser → 2400dpi imagesetter

  Example PostScript (draw a line):
    72 72 moveto
    200 200 lineto
    stroke

  Type rendered as PostScript procedure (outline as path)
  Any resolution: scale outline → rasterize → perfect edges

TYPE 1 FORMAT (1984–1990, encrypted; 1990, open):
  Two-file structure (in early Mac/PC implementations):
    .PFB (Printer Font Binary) — the outline data + hinting bytecode
    .AFM (Adobe Font Metrics) — metrics file (widths, kerning pairs)
    .PFM (Printer Font Metrics) — Windows metrics
  Inside .PFB:
    CharStrings dictionary: one procedure per glyph
    Private dictionary: hinting data (stem widths, alignment zones)
    Encoding vector: maps character codes to glyph names

  Glyph description (encrypted Charstring):
    Sequence of numbers + operators:
    moveto, lineto, curveto, closepath (simplified)
    hstem, vstem: hint operators (alignment instructions)
    seac: standard encoding accented character composite

  ENCRYPTION:
    CharStrings encrypted with eexec + Charstring encryption
    Adobe claimed this prevented cheap imitation
    Decryption algorithm published in 1990 (Seybold seminar; reverse-engineered)
    Adobe released spec officially after pressure

──────────────────────────────────────────────────────────────────────────────
```

### The Adobe Monopoly and Its End (1984–1991)

```
THE TYPE 1 MONOPOLY PERIOD
──────────────────────────────────────────────────────────────────────

1984–1990: Adobe PostScript = the only professional digital font standard
  Adobe licensed PostScript to printer manufacturers (royalties per unit)
  Adobe Fonts: sold as cartridges or downloaded to printers
  Expensive: $100–$200 per font family
  Professional quality: excellent hinting, cubic curves

PROBLEMS WITH THE MONOPOLY:
  Apple: paying Adobe per LaserWriter unit + per font license
  Third-party font creators: had to license from Adobe or use Type 3
  Type 3: no hinting → poor small-size rendering
  Users: expensive fonts; limited to Adobe's library

1991: BREAKING THE MONOPOLY
  Apple and Microsoft co-develop TrueType
  Apple licenses TrueType to Microsoft (royalty-free)
  Both companies bundle TrueType fonts in their OS
  Mac System 7 + Windows 3.1: built-in TrueType rendering (ATM for Mac)
  Adobe responds: releases Type 1 specification publicly
  Market: two competing formats; consumer confusion; better deals on fonts

INTERMEDIATE: ADOBE ATM (Adobe Type Manager, 1989)
  Before ATM: Type 1 fonts only rendered correctly on PostScript printers
  Screen fonts were separate bitmap fonts (one per size)
  ATM: added runtime Type 1 rendering on screen
  (Installed in Mac/Windows; rendered Type 1 on screen at any size)
  This was the first outline renderer for desktop screens
  Bridge: GDI (Windows) used bitmap fonts; ATM added outline rendering
  Parallel for .NET devs: GDI/GDI+ was the old Windows font stack;
  DirectWrite is the modern equivalent (see below)
──────────────────────────────────────────────────────────────────────
```

---

## TrueType (Apple + Microsoft, 1991)

TrueType was a strategic counter to Adobe's Type 1 monopoly, not a technically superior format. It introduced a different curve type (quadratic B-spline) and a programmable hinting system.

```
TRUETYPE ARCHITECTURE
──────────────────────────────────────────────────────────────────────────────

FILE STRUCTURE:
  Single .ttf file (unlike Type 1's two files)
  Structured as a collection of named tables:

  Required tables:
  ┌─────────┬───────────────────────────────────────────────────────┐
  │ Table   │ Contents                                              │
  ├─────────┼───────────────────────────────────────────────────────┤
  │ cmap    │ Character-to-glyph mapping (Unicode → GlyphID)        │
  │ glyf    │ Glyph outlines (quadratic B-spline paths + hints)     │
  │ head    │ Font header (version, flags, created/modified dates)  │
  │ hhea    │ Horizontal header (ascender, descender, line gap)     │
  │ hmtx    │ Horizontal metrics (advance widths, left sidebearings) │
  │ loca    │ Glyph location index (offset into glyf table)         │
  │ maxp    │ Maximum profile (glyph count, max contours, etc.)     │
  │ name    │ Name strings (font name, copyright, designer, etc.)   │
  │ post    │ PostScript information (glyph name lookup)            │
  │ OS/2    │ OS/2 + Windows metrics (xHeight, CapHeight, etc.)    │
  └─────────┴───────────────────────────────────────────────────────┘

GLYPH DATA (glyf table):
  Each glyph = contour list:
    numberOfContours (int16; negative = composite glyph)
    xMin, yMin, xMax, yMax (bounding box)
    endPtsOfContours[] (last point index of each contour)
    flags[] (on-curve / off-curve / overlap flags per point)
    xCoordinates[], yCoordinates[] (relative delta encoding)

  Composite glyphs: composed of references to other glyphs
  (e.g., 'À' = 'A' + combining grave accent glyph)

TRUETYPE HINTING:
  A complete bytecode instruction set (~200 opcodes)
  Executed by a TrueType interpreter (a virtual machine)
  Instructions embedded in the glyph data

  Key hinting operations:
    SRP0–SRP2: set reference points
    IP: interpolate point positions
    DELTAP: apply delta adjustments at specific ppem (pixels per em) sizes
    DELTAC: delta adjustments for CVT (Control Value Table) entries
    MIAP: move indirect absolute point (align to CVT)
    MD: measure distance between points

  CVT (Control Value Table): shared measurements (stem widths, alignment zones)
  fpgm (font program): function definitions; runs once at load
  prep (pre-program): runs at each size change; sets CVT values

  WINDOWS vs MAC HINTING:
    Windows: executes TrueType hints faithfully (full byte code interpretation)
    Mac (old): used its own rasterizer, partially ignored hints
    This created platform-specific rendering differences that plagued
    type designers for 20 years until HiDPI reduced hinting's importance

──────────────────────────────────────────────────────────────────────────────
```

---

## OpenType (Adobe + Microsoft, 1996/2000)

OpenType is the unification: a single file format that can contain either CFF (PostScript cubic Bézier) or glyf (TrueType quadratic) outlines, plus an extensive table structure for advanced typographic features.

```
OPENTYPE FILE STRUCTURE
──────────────────────────────────────────────────────────────────────────────

.otf extension: typically uses CFF (PostScript) outlines
.ttf extension: typically uses glyf (TrueType) outlines
Both: OpenType format; the extension is convention, not format difference

Additional tables added by OpenType (beyond TrueType's required set):

  Typography tables:
  ┌─────────┬───────────────────────────────────────────────────────┐
  │ GSUB    │ Glyph Substitution — ligatures, alternates, small caps │
  │ GPOS    │ Glyph Positioning — kerning, mark attachment          │
  │ GDEF    │ Glyph Definitions — glyph class assignments           │
  │ JSTF    │ Justification — line breaking + justification rules   │
  │ BASE    │ Baseline offsets for multilingual typesetting         │
  └─────────┴───────────────────────────────────────────────────────┘

  Layout feature examples in GSUB:
  Feature 'liga' (ligatures):
    fi → fi-ligature glyph
    fl → fl-ligature glyph
    ffi, ffl, fj, ffi → ligature glyphs

  Feature 'smcp' (small caps):
    A, B, C, ... → corresponding small cap glyphs

  Feature 'onum' (old-style figures):
    0123456789 → oldstyle numeral glyphs

  Feature 'sups' (superscript):
    0123456789 → superscript numeral glyphs

  Feature 'salt' (stylistic alternates):
    a → alternate 'a' design (e.g., single-storey vs double)

  Feature 'calt' (contextual alternates):
    Context-dependent: ff, fi, ff-, etc. trigger different glyphs

  Kerning in GPOS:
    Pair positioning: AV → move V -80 units from default
    Class-based kerning: all A-class + all V-class = -80 units
    Mark attachment: diacritics positioned relative to base glyphs

GLYPH COUNT:
  TrueType original: 256 glyph limit (8-bit encoding vector)
  OpenType: 65,535 glyph limit (16-bit GlyphID)
  → Enables: multilingual coverage; multiple script support;
    stylistic alternates; ornamental sets; full Unicode range

──────────────────────────────────────────────────────────────────────────────
```

---

## The Rendering Pipeline

Understanding what happens between "font file" and "pixels on screen":

```
FONT RENDERING PIPELINE — FULL DETAIL
──────────────────────────────────────────────────────────────────────────────

STEP 1: SHAPING
  Input: Unicode string + font file
  Engine: HarfBuzz (open source), CoreText (Apple), Uniscribe (Windows)
  Operations:
    - Unicode normalization (NFC, NFD)
    - Script detection (Latin, Arabic, Devanagari, etc.)
    - Apply GSUB rules: substitute glyphs (ligatures, alternates)
    - Apply GPOS rules: compute relative glyph positions (kerning)
    - For complex scripts (Arabic, Devanagari):
        contextual forms, mark attachment, reordering
  Output: sequence of (GlyphID, x-advance, x-offset, y-offset) tuples
  This is the "shaped text" — a sequence of positioned glyphs

STEP 2: LAYOUT
  Input: shaped text + layout constraints (measure, alignment)
  Engine: layout engine (browser, OS text API, PDF engine)
  Operations:
    - Line breaking (Knuth-Plass algorithm or greedy)
    - Hyphenation
    - Justification (expand spaces or adjust tracking)
    - Baseline alignment for mixed scripts/sizes
  Output: positioned glyph stream with line/paragraph structure

STEP 3: RASTERIZATION
  Input: glyph outline (Bézier curves from font file) + size (ppem)
  Engine: FreeType (open source), Windows GDI/DirectWrite, CoreText/CG
  Operations:
    A. HINTING (optional; important at small sizes):
       Execute hinting bytecode (TrueType) or apply autohinter
       Adjust outline control points to align with pixel grid
       Goal: stem widths become integer pixels; consistent across letters
    B. SCAN CONVERSION:
       Convert adjusted outline to coverage mask
       For each pixel: compute fraction of pixel covered by outline
       This fraction = anti-aliasing value (0–255)
  Output: bitmap of coverage values (grayscale or per-channel)

STEP 4: ANTI-ALIASING
  Takes coverage values → applies to pixels
  Types:
    None (1-bit): on or off; jaggy edges
    Grayscale (standard): one gray value per pixel
    Subpixel (ClearType): separate R, G, B values per pixel (see below)
  Output: pixels with appropriate gray/color values

STEP 5: GAMMA CORRECTION
  Display gamma (typically 2.2 for sRGB) must be applied to anti-aliasing values
  If not corrected: text appears too thin or too thick at certain weights
  ClearType does this; many older renderers did not
  This is a major difference between "looks right" and "looks wrong"

STEP 6: COMPOSITING
  Rendered text pixels composited into framebuffer
  If text on colored background: blend modes applied
  If layered UI: sub-pixel rendering must match background color
  (One problem with ClearType: subpixel rendering assumes white background)

──────────────────────────────────────────────────────────────────────────────
```

---

## Hinting: The Pixel-Grid Problem

Hinting is the most complex aspect of digital font rendering — the problem of mapping smooth curves to a discrete pixel grid.

```
THE HINTING PROBLEM
──────────────────────────────────────────────────────────────────────────────

FONTS AT LOW RESOLUTION:
  A lowercase 'n' at 12px:
    em = 12 pixels
    x-height ≈ 6px (50% of em)
    stem width in design ≈ 80 units of 1000 = 0.08 em = ~1 pixel

  PROBLEM: stems at this size are ~1 pixel wide
    If outline isn't aligned to pixel grid:
      Some stems might land on pixel boundary → render at 1.5px = gray
      Others land centered → render at 1px = black
      Result: inconsistent weight within the word — some letters look bolder

  SOLUTION — HINTING:
    Move outline control points so stems align exactly with pixel grid
    Force all vertical stems to be exactly N pixels wide
    Force all horizontal strokes to be exactly M pixels wide
    Align x-height to integer pixel grid
    This is what hinting bytecode does

BEFORE HINTING:               AFTER HINTING:
┌──────────────────────────┐  ┌──────────────────────────┐
│  n   n   n              │  │  n   n   n              │
│  (stems vary in          │  │  (all stems same         │
│   apparent weight)       │  │   apparent weight)       │
│  m and n look slightly   │  │  m and n look consistent │
│  different weights       │  │  in weight               │
└──────────────────────────┘  └──────────────────────────┘

HINTING COST:
  Good TrueType hinting: thousands of hours per typeface family
  The reason major fonts cost money: the hinting work is enormous
  Variable fonts: hinting must work across the design space (harder)
  HiDPI screens: at 2×, each "pixel" = 4 physical pixels → hinting less critical

──────────────────────────────────────────────────────────────────────────────
```

---

## Anti-Aliasing and ClearType

```
ANTI-ALIASING TYPES
──────────────────────────────────────────────────────────────────────────────

NO ANTI-ALIASING (1-bit):
  ████████          ████████
  Each pixel = black or white
  Result: "jaggies" on diagonal and curved strokes
  Used: very early digital type; some special contexts (pixel fonts)

GRAYSCALE ANTI-ALIASING:
  For each pixel, compute coverage (0.0 to 1.0)
  Render pixel as proportional gray value
  ░░████████░░
  Result: smooth edges perceived; resolution effectively doubled
  Problem: requires gamma correction to look right

SUBPIXEL RENDERING (ClearType):
  LCD screen physical structure:
  ┌───┬───┬───┬───┬───┬───┬───┬───┐
  │ R │ G │ B │ R │ G │ B │ R │ G │  (each pixel = 3 subpixels)
  └───┴───┴───┴───┴───┴───┴───┴───┘

  At 96 dpi: pixel pitch = 0.264mm; subpixel pitch = 0.088mm
  Horizontally: 3× resolution available by addressing R, G, B separately

  ClearType method:
  ■ Each subpixel treated as independent sample for horizontal coverage
  ■ Coverage of left edge: control R subpixel intensity
  ■ Coverage of right edge: control B subpixel intensity
  ■ Result: horizontal resolution effectively 3× physical

  VISUAL RESULT:
  Without ClearType (grayscale):  text appears slightly fuzzy
  With ClearType (subpixel):      text appears sharper, more defined

  LIMITATION:
  Subpixel rendering assumes specific pixel geometry (RGB horizontal strip)
  On rotated screens, rotated subpixels, or high-DPI screens: artifacts
  On modern OLED screens with PenTile arrangement: different subpixel layout
  → ClearType assumptions break

  WHY HIDPI CHANGES EVERYTHING:
  At 1× DPI (96 ppi): pixel = 0.264mm; type at 12pt = 16px = clearly pixelated
  At 2× DPI (192 ppi): pixel = 0.132mm; 12pt = 32px; each curve has more samples
  At 2×, the quantization error is so small it's imperceptible
  → Subpixel rendering offers little benefit (may even look odd)
  → Hinting less critical (minor grid misalignment imperceptible)
  → This is why text on Retina Macs / modern iPhones looks simply correct

──────────────────────────────────────────────────────────────────────────────
```

---

## Windows Font Rendering: GDI+ → DirectWrite

Directly relevant if you have .NET/Windows background:

```
WINDOWS FONT RENDERING STACK (OLD WORLD → NEW WORLD)
──────────────────────────────────────────────────────────────────────────────

GDI (Graphics Device Interface — Windows 1.0 → XP):
  Core Windows graphics API
  Font rendering: bitmap-first; outline rendering via device driver
  Limited anti-aliasing
  TrueType via GDI: standard grayscale AA
  Your WinForms apps used this (if you used GDI+)

GDI+ (.NET Framework, Windows XP):
  Wrapper around GDI with more capabilities
  Font rendering: improved but still GDI-based
  In .NET: System.Drawing.Font + Graphics.DrawString()
  ClearType: available but font smoothing settings-dependent
  Problem: GDI+ font rendering is not hardware-accelerated

CLEARTYPE + GDI (Windows XP, 2001):
  Microsoft's ClearType technology (Bill Hill, Greg Hitchcock, 2000)
  Available in GDI from XP; default from Vista
  Problem: only for compatible rendering paths; DirectDraw/Direct3D bypassed it

DIRECTWRITE (Windows 7, 2009):
  New text rendering API using Direct2D
  Key improvements over GDI+:
    - GPU-accelerated rendering
    - Better ClearType (gamma-corrected; per-monitor DPI aware)
    - Improved hinting (new "natural" hinting mode)
    - OpenType layout features (GSUB/GPOS) exposed to applications
    - Font fallback and font collection management improved
    - Subpixel positioning (glyphs can be placed at 1/64-pixel precision)
  WPF, WinUI, UWP: use DirectWrite
  Modern .NET (WPF): System.Windows.Media.FormattedText → DirectWrite

BRIDGE SUMMARY:
  Old code (.NET Framework, WinForms): System.Drawing.Font → GDI+
  New code (WPF, WinUI, .NET 6+):       FontFamily/Typeface → DirectWrite
  CSS/browser rendering: Chromium uses Skia → DirectWrite on Windows

DIRECTWRITE vs MACOS CORETEXT:
  DirectWrite (Microsoft): focused on ClearType LCD rendering; Windows-first
  CoreText (Apple): always emphasized subpixel-less high-quality rendering
  Historical debate: "Microsoft text looks sharper but colored; Apple text
  looks softer but more faithful to typeface design"
  After HiDPI: both look essentially identical at 2×

──────────────────────────────────────────────────────────────────────────────
```

---

## Web Fonts: CSS and Delivery

```
WEB FONTS AND CSS
──────────────────────────────────────────────────────────────────────────────

@font-face (CSS2, 1998; properly implemented ~2008):
  Lets CSS request arbitrary font files from server

  @font-face {
    font-family: 'My Font';
    src: url('/fonts/myfont.woff2') format('woff2'),
         url('/fonts/myfont.woff') format('woff');
    font-weight: 400;
    font-style: normal;
    font-display: swap;           /* loading behavior */
    unicode-range: U+0000-00FF;  /* subsetting hint */
  }

FONT-DISPLAY VALUES:
  auto:     browser default (usually swap)
  block:    invisible until font loads (max 3s), then render; swap never
  swap:     show fallback immediately; swap when font ready
  fallback: block ~100ms; if not loaded: use fallback; no swap after 3s
  optional: block ~100ms; if not fast, abandon (use fallback permanently)

  For body text: font-display: swap (layout stability; not invisible)
  For headers: font-display: block or swap (OK to show blank briefly)
  For performance: font-display: optional (never shifts layout)

WOFF2 FORMAT:
  WOFF  (2010): OpenType/TrueType + metadata + zlib compression
  WOFF2 (2013): OpenType/TrueType + metadata + Brotli compression
  Size comparison for typical font:
    .ttf (uncompressed):  200 KB
    .woff (zlib):         140 KB (~30% smaller)
    .woff2 (Brotli):      100 KB (~50% smaller than TTF)
  Browser support: WOFF2 is universal (Chrome 36+, Firefox 39+, all modern)
  Recommendation: serve WOFF2 as primary; WOFF as fallback for IE11

UNICODE RANGE SUBSETTING:
  unicode-range: U+0000-00FF;  /* Basic Latin + Latin-1 Supplement */
  unicode-range: U+0100-024F;  /* Latin Extended-A + B */

  Purpose: browser only downloads font file when page contains those chars
  Google Fonts uses this to split fonts into per-script chunks
  A page using only Latin chars doesn't download the Greek/Cyrillic subset

LOADING STAGES (font loading API):
  loading → loaded → error (or blocked by font-display)
  document.fonts.ready → Promise resolves when all @font-face loaded
  document.fonts.check('16px MyFont') → true if glyph ready to render

FLASH OF UNSTYLED TEXT (FOUT):
  With font-display: swap: page renders in fallback font first
  When custom font loads: reflow can occur if metrics don't match
  Solution: use font-metric-override to adjust fallback font metrics:

  @font-face {
    font-family: 'Fallback Font';
    src: local('Arial');
    ascent-override: 90%;
    descent-override: 20%;
    line-gap-override: 5%;
    size-adjust: 107%;  /* scale fallback to match custom font metrics */
  }

  This minimizes layout shift when font swaps

──────────────────────────────────────────────────────────────────────────────
```

---

## OpenType Feature Reference

```
COMMON OPENTYPE FEATURES AND CSS ACCESS
──────────────────────────────────────────────────────────────────────

Feature tag  CSS property                    Effect
──────────── ─────────────────────────────── ─────────────────────────────
liga         font-variant-ligatures: common  fi fl ffi ffl ligatures
dlig         font-variant-ligatures:         ct st sp (discretionary)
             discretionary
calt         font-variant-ligatures:         context-dependent substitutions
             contextual
smcp         font-variant-caps: small-caps   lowercase → small caps
c2sc         font-variant-caps: all-small-   uppercase → small caps
             caps
onum         font-variant-numeric:           1234 → oldstyle figures
             oldstyle-nums
tnum         font-variant-numeric: tabular-  fixed-width figures (tables)
             nums
pnum         font-variant-numeric:           proportional figure widths
             proportional-nums
lnum         font-variant-numeric: lining-   lining (default) figures
             nums
frac         font-variant-numeric: diagonal- 1/4 → ¼ glyph
             fractions
ordn         font-variant-numeric: ordinal   1st → 1ˢᵗ
sups         font-feature-settings: 'sups'   superscript numerals
subs         font-feature-settings: 'subs'   subscript numerals
swsh         font-feature-settings: 'swsh'   swash alternates (decorative)
ss01–ss20    font-feature-settings: 'ss01'   stylistic sets

GENERIC ACCESS (low-level):
  font-feature-settings: 'liga' 1, 'dlig' 1, 'smcp' 1;
  Use when high-level CSS property doesn't expose the feature

HIGH-LEVEL CSS (preferred):
  font-variant: small-caps;
  font-variant-numeric: oldstyle-nums tabular-nums;
  font-variant-ligatures: common-ligatures discretionary-ligatures;
──────────────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Format | Curve Type | Max Glyphs | Key Use | Notes |
|--------|------------|------------|---------|-------|
| Type 1 (.pfb+.afm) | Cubic Bézier | 256 | Legacy PostScript | Obsolete; replaced by OpenType CFF |
| TrueType (.ttf) | Quadratic B-spline | 65,535 | Windows system fonts | Strong hinting bytecode; Windows |
| OpenType CFF (.otf) | Cubic Bézier | 65,535 | Professional typography | Smaller file; better for print |
| OpenType TT (.ttf) | Quadratic B-spline | 65,535 | Cross-platform | Same as TrueType but OpenType tables |
| WOFF (.woff) | Either | 65,535 | Web delivery (legacy) | zlib compressed OpenType |
| WOFF2 (.woff2) | Either | 65,535 | Web delivery (current) | Brotli compressed; best choice |
| Variable (.ttf/.otf) | Either | 65,535 | Design spaces | One file, multiple instances |

---

## Common Confusion Points

**Font files are copyrighted software, not design (in the US)**
US copyright does not protect letterform designs (utilitarian). But the font file — the software encoding the design — is protected software. This means you cannot legally extract outlines from a font file and redistribute them, but someone can look at Garamond and draw new letterforms inspired by it.

**OTF vs TTF: the extension doesn't mean what you think**
A .ttf file today is almost certainly an OpenType font using TrueType (quadratic) outlines. A .otf file is an OpenType font using CFF (PostScript cubic) outlines. Both are "OpenType fonts" in terms of the table structure and feature support. The curve type inside affects rendering details but is transparent to most users.

**ClearType does not work correctly on all displays**
ClearType assumes horizontal RGB subpixels. On vertical RGB subpixels, BGR subpixels, PenTile OLED subpixels, or e-ink displays, ClearType subpixel rendering may introduce color fringing. Windows allows per-monitor ClearType tuning (ClearType Tuner) but most users never do this. On HiDPI screens, the subpixel rendering benefit is negligible and ClearType's grayscale fallback is used.

**Hinting is not required — it's a low-DPI optimization**
At 2× DPI (HiDPI), hinting does almost nothing — the pixel grid is fine enough that outline rendering produces good results without adjustment. This is why free/open-source fonts with poor hinting look fine on modern Retina displays. If you only target modern hardware (mobile phones, HiDPI laptops), hinting quality is not a significant selection criterion.
