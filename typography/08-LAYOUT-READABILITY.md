# 08 — Layout and Readability

## The Big Picture

Typography at the character level (which typeface, which weight) is only half the problem. Typography at the layout level — how text is arranged in space — determines whether that beautiful typeface is actually readable. Most readability failures in software interfaces are layout failures, not typeface failures.

```
READABILITY PARAMETERS — INTERACTION MAP
────────────────────────────────────────────────────────────────────────────────

  TYPE SIZE ──→ determines ──→ LINE HEIGHT (leading)
      │                              │
      │                              ▼
      │                    affects: MEASURE (line length)
      │                              │
      ▼                              ▼
  X-HEIGHT ──→ determines ──→ APPARENT SIZE
      │
      ▼
  TRACKING ──→ global letter-spacing
      │
      ▼
  KERNING ──→ pair-specific letter-spacing
      │
      ▼
  WORD SPACING ──→ interacts with JUSTIFICATION
                    │
                    ▼
               RIVERS (justified text pathology)

  All of these interact. You cannot optimize one in isolation.

────────────────────────────────────────────────────────────────────────────────
```

---

## Legibility vs Readability: The Distinction

```
LEGIBILITY vs READABILITY
──────────────────────────────────────────────────────────────────────

LEGIBILITY:
  Can you distinguish one letterform from another?
  "Is this an 'l' or an 'I' or a '1'?"
  "Is this a 'rn' or an 'm'?"

  Legibility is letter-level and type-size-level.
  Primarily a function of: x-height, counter size, letter spacing,
  aperture (open vs closed letters), font quality.

READABILITY:
  Can you read continuous text comfortably at length?
  Does the text fatigue you? Do your eyes lose their place?

  Readability is paragraph-level and page-level.
  Primarily a function of: measure, leading, typeface weight,
  word spacing, text size.

THEY ARE DIFFERENT:
  A typeface can be highly legible but poorly readable:
    Impact (the font): very legible individual letters; terrible for body text
    (too condensed, too heavy for extended reading)

  A typeface can be readable but have legibility problems:
    Some calligraphic scripts: beautiful in paragraphs; specific letter
    pairs confusable (e, o; l, i; m, rn)

PASSWORD FIELD EXAMPLE:
  A font that confuses 'l', '1', 'I', 'O', '0' is a security problem.
  Use: input[type="password"] { font-family: 'monospace'; }
  Or specify a font with clear disambiguation: JetBrains Mono, Cascadia Code
  This is a legibility problem causing a functional problem.

──────────────────────────────────────────────────────────────────────
```

---

## Measure: The Most Important Layout Parameter

The **measure** is the line length — the horizontal width of a column of text. It is the single most consequential typographic layout decision.

```
OPTIMAL MEASURE
──────────────────────────────────────────────────────────────────────────────

BRINGHURST'S RULE (Robert Bringhurst, "The Elements of Typographic Style"):
  Optimal measure: 45–75 characters per line (including spaces)
  For single-column text: 66 characters is widely cited as ideal
  For multi-column layouts: 40–50 characters per column
  For footnotes/marginal text: 35–40 characters

WHY THERE'S AN OPTIMAL:
  Too short:
  - Each line requires frequent direction changes (eye tracks right → left)
  - Justification becomes impossible without bad spacing or bad hyphenation
  - Rhythm is choppy; reading feels mechanical
  - Under ~30 chars: reading becomes significantly slower

  Too long:
  - Eye must travel far to reach the next line start
  - Risk of "losing the line": returning to wrong line
  - Must use generous leading (more space between lines) to compensate
  - Over ~90 chars: reading significantly slows; error increases

PRACTICAL CSS:
  The `ch` unit in CSS = width of the '0' character (approx. average width)
  Good approximation for measure:

  p {
    max-width: 65ch;   /* ~65 character measure; Bringhurst */
    /* or */
    max-width: 38em;   /* em-based; depends on typeface */
  }

  65ch is more semantically correct (character-based measure)
  38em is more traditional but typeface-dependent

MEASURE AND LEADING INTERACTION:
  Wider measure requires more leading (line spacing):
    45 chars + 1.3× leading = appropriate
    75 chars + 1.5× leading = appropriate
    75 chars + 1.3× leading = too tight; hard to find next line

  Narrower measure can use tighter leading:
    40 chars + 1.25× leading = fine
    Multi-column layouts are narrower → denser leading acceptable

──────────────────────────────────────────────────────────────────────────────
```

---

## Leading: Line Spacing

```
LEADING — LINE HEIGHT
──────────────────────────────────────────────────────────────────────────────

NAME ORIGIN:
  Strips of lead inserted between lines of hand-set metal type
  Thicker lead = more space between lines
  Modern metric: the distance from one baseline to the next

MEASUREMENT:
  Traditional: expressed in points ("9/11" = 9pt type on 11pt leading)
  CSS: line-height property (unitless ratio OR absolute value OR percentage)
  Relationship: if type is 16px and line-height is 1.5, spacing = 24px
                half the extra 8px appears above, half below each line

OPTIMAL RANGE:
  Body text: 120%–145% of type size (1.2–1.45 relative)
  Typical defaults: 1.2 (browsers), 1.4–1.5 (good practice)

  Factors that increase needed leading:
  - Wider measure (needs more leading for eye to track lines)
  - High x-height (letters feel crowded with standard leading)
  - Light weight on colored background (needs more air)
  - Sans-serif (slightly more leading helps differentiation)

  Factors that allow tighter leading:
  - Narrow measure (lines short; easy to find next)
  - Display size (large type; visual separation clear)
  - Low x-height (Old Style; more natural white space)
  - All caps (no descenders conflict; can go tight)

CSS BEST PRACTICE:
  /* Body text */
  body {
    font-size: 16px;
    line-height: 1.5;        /* 24px absolute; accessible default */
  }

  /* Display/heading */
  h1 {
    font-size: 48px;
    line-height: 1.1;        /* tighter; display type */
    letter-spacing: -0.02em; /* slight tightening for large display */
  }

  /* Caption/small text */
  .caption {
    font-size: 12px;
    line-height: 1.6;        /* more generous at small size */
  }

LEADING AND VERTICAL RHYTHM:
  Vertical rhythm: align text baselines to a common grid
  If base leading = 24px, headings should be multiples: 24, 48, 72px
  CSS rarely enforces this strictly; it is a design aspiration
  Useful: baseline-grid overlays in design tools (Figma, Sketch)

──────────────────────────────────────────────────────────────────────────────
```

---

## Tracking and Kerning

```
TRACKING vs KERNING
──────────────────────────────────────────────────────────────────────────────

TRACKING (letter-spacing):
  Global adjustment to space between ALL letters
  Applied uniformly across a range of text
  CSS: letter-spacing property

  When to OPEN tracking (add space):
  - ALL CAPS text: visually crowded without additional tracking
    (capital letters have no ascenders/descenders to create rhythm)
    recommendation: +0.05em to +0.1em for all-caps
  - Small text in body (8pt and below): letters too close at small size
  - Highly condensed typefaces
  - Uppercase headlines in some editorial styles

  When to TIGHTEN tracking (remove space):
  - Large display type (> 40pt/px): default metrics feel too loose
  - Condensed display text
  - Strong brands often tighten tracking for distinctive feel
    recommendation: -0.02em to -0.05em for large display

  NEVER: tight tracking on body text (deliberate torture)
  NEVER: positive tracking on italic or script (breaks design intention)

  CSS example:
    .all-caps-label {
      text-transform: uppercase;
      letter-spacing: 0.08em;  /* compensate for uppercase visual crowding */
    }

    .hero-headline {
      font-size: 72px;
      letter-spacing: -0.03em;  /* tighten large display text */
    }

KERNING:
  Pair-specific adjustment to space between SPECIFIC letter pairs
  Applied to specific combinations: AV, VA, WA, To, Te, Ly, P., etc.

  Why kerning is needed:
  ┌──────────────────────────────────────────────────────────────────┐
  │  AVOCADO with no kerning:                                        │
  │  A V O C A D O                                                   │
  │  [uniform advance widths; A and V have too much space between]   │
  │                                                                  │
  │  AVOCADO with kerning:                                           │
  │  AVOCADO                                                         │
  │  [A and V overlap slightly in advance width; closes the gap]     │
  └──────────────────────────────────────────────────────────────────┘

  The problem: 'A' has a slanted right side; 'V' has a slanted left side
  Together, the diagonal strokes create a large visual gap
  Kerning: move V leftward by X units when preceded by A

  KERNING TYPES:
  Metric kerning: use kern table values from the font
    (OpenType GPOS or kern table pairs)
    Fast; consistent with font designer's intent
    Font may have 10,000+ kern pairs; automated

  Optical kerning: application-computed based on glyph shapes
    Adobe applications: Optical kerning recalculates for text size
    More accurate at display sizes; more CPU intensive
    Default in InDesign for good reason

  CSS: letter-spacing is NOT kerning
    letter-spacing applies global tracking (not pair-specific)
    CSS has no pair-specific kerning control
    OpenType kerning: font-kerning: auto; (enabled by default in browsers)
    font-feature-settings: 'kern' 1;  (explicit; default on)

──────────────────────────────────────────────────────────────────────────────
```

---

## Word Spacing and Justification

```
JUSTIFICATION: THE MINEFIELD
──────────────────────────────────────────────────────────────────────────────

ALIGNMENT OPTIONS:
  Left-aligned (ragged right):   ████████████████████
  (flush left)                   ████████████████
                                 ████████████████████████
                                 ████████████
  Word spacing: consistent; lines vary in length
  Advantage: consistent letter/word spacing; no rivers
  Default for most screen text: use this

  Justified:                     ████████████████████
  (flush left + right)           ████████████████████
                                 ████████████████████
                                 ████████
  Word spacing: VARIES per line (to fill measure)
  Advantage: clean column edges; more formal/book-like
  Disadvantage: variable word spacing; RIVERS

RIVERS:
  In justified text with short measure or bad algorithm:
  Spaces happen to stack vertically through multiple lines
  Creating a vertical white "river" through the text block
  Visually distracting; eye follows the river not the text

  ████ ████ ████████████████████
  ███████████████ ████████████
  ████████████████████ ████████
  █████████████████████████████

  Rivers are more common with:
  - Short measure (narrow column; limited flexibility)
  - Long words (can't split without hyphenation)
  - Coarse justification algorithm (web browsers: simple)
  - No hyphenation

HYPHENATION:
  Reduces rivers dramatically in justified text
  CSS: hyphens: auto;  (requires lang attribute on html)
  Browser hyphenation: uses hyphenation dictionary per language
  html[lang="en"] { hyphens: auto; }

  Recommendation for justified text:
  text-align: justify;
  hyphens: auto;
  -webkit-hyphens: auto;

OPTIMAL LINE-BREAKING ALGORITHMS:
  Greedy (browser default): greedy per line; can create bad paragraphs
  Knuth-Plass (TeX, InDesign): considers entire paragraph at once
    minimizes total "badness" across all lines; eliminates most rivers
  CSS: text-wrap: balance;  (Chrome 114+, limited)
  CSS: text-wrap: pretty;  (Chrome 117+; Knuth-Plass-like for last few lines)

──────────────────────────────────────────────────────────────────────────────
```

---

## Type on Screen: DPI Evolution

```
SCREEN DPI EVOLUTION AND TYPOGRAPHY
──────────────────────────────────────────────────────────────────────────────

HISTORICAL SCREEN DPIS:
  Mac 128K (1984):        72 dpi  (intentionally 72 = 72pt/inch; WYSIWYG)
  Windows (1990s):        96 dpi  (larger pixels → larger UI for readability)
  Common LCD (2000s):     72–96 dpi
  MacBook Pro Retina (2012): 220 ppi (first mainstream HiDPI laptop)
  iPhone 4 "Retina" (2010):  326 ppi
  iPhone 14 Pro:          460 ppi
  Modern 27" 5K iMac:     218 ppi
  Dell UltraSharp 27" 4K: 163 ppi

DPI RATIONALE FOR TYPOGRAPHY:
  At 72–96 dpi: pixel is 0.26–0.35mm; visible to naked eye
  Letterforms at 12px = 12 tiny squares; huge quality problem
  → ClearType, hinting, careful font design to compensate

  At 2× (144+ dpi): pixel is 0.18mm; edge artifacts nearly invisible
  Letterforms at 12px × 2 = 24 actual pixels per letter
  → Anti-aliasing and hinting help less; outline quality dominates

  Practical implication:
  • Low DPI: need well-hinted fonts; ClearType; careful size selection
  • HiDPI: almost any well-designed font renders well; relaxed constraints
  • Mixed DPI: your design must handle both; test on 1× screens

PIXEL DENSITY AND RENDERING:
  CSS px is a reference pixel:
  At 1× (96 dpi): 1 CSS px = 1 physical pixel
  At 2× (192 dpi): 1 CSS px = 2×2 = 4 physical pixels
  window.devicePixelRatio: JavaScript access to DPR

  Font at 16px CSS on 2× screen:
  16px × 2 = 32 physical pixels per em
  Plenty of resolution; renders beautifully with no special engineering

RESPONSIVE TYPOGRAPHY:
  Fluid type: scale font size with viewport width
  CSS clamp():
    font-size: clamp(16px, 1rem + 2vw, 28px);
    /* Minimum 16px, grows with viewport, caps at 28px */

  CSS container queries (modern):
    @container (width > 600px) {
      p { font-size: 18px; }
    }

──────────────────────────────────────────────────────────────────────────────
```

---

## Type Size Guidelines

```
TYPE SIZE REFERENCE
──────────────────────────────────────────────────────────────────────

PRINT SIZE REFERENCE:
  6pt     ← Absolute minimum (legal disclaimers, fine print)
  7–8pt   ← Footnotes, captions (short text, infrequent reading)
  9–10pt  ← Newspaper body text (optimized typefaces + paper)
  10–11pt ← Standard book body text
  12pt    ← Book text in poor lighting; many word processor defaults
  14–18pt ← Large print / accessibility
  18–24pt ← Display / subheadings
  24pt+   ← Display / headlines

  Note: 12pt = default MS Word. This is not a typographic ideal —
  it is the historical default from typewriter conventions.
  Quality books are set 10–11pt.

SCREEN SIZE REFERENCE:
  Body text:  14–18px (16px: browser/WCAG default baseline)
  Small text: 12–14px (avoid below 12px for sustained reading)
  Captions:   11–13px (brief; not sustained reading)
  UI labels:  12–14px
  Headings:   20–48px (depends on hierarchy level)
  Hero text:  48–120px+

WCAG ACCESSIBILITY:
  WCAG 2.1 contrast requirements:
  Normal text (< 18pt/24px): contrast ratio ≥ 4.5:1 (AA), 7:1 (AAA)
  Large text (≥ 18pt/24px or 14pt bold): contrast ratio ≥ 3:1 (AA)
  body contrast: black text (#000) on white (#FFF) = 21:1 (max)
  A common failure: gray text #888 on white = 3.5:1 (fails AA for normal text)

  Body font-size < 16px + pixel zooming not supported = accessibility failure
  CSS: font-size using rem units respects user browser text size preferences

SIZE AND WEIGHT INTERACTION:
  Large size → can use lighter weight (detail visible)
  Small size → need regular or slightly heavier weight (thin strokes disappear)
  Never: thin weight (100–200) at body text sizes
  Exception: some typefaces designed with high-quality thin at small size

──────────────────────────────────────────────────────────────────────
```

---

## Dyslexia-Friendly Typography

```
DYSLEXIA AND TYPOGRAPHY
──────────────────────────────────────────────────────────────────────────────

WHAT DYSLEXIA IS (briefly):
  Neurological processing difference affecting phonological awareness
  and mapping symbols to sounds; not a vision problem
  Estimated: 5–17% of population; significant design consideration

WHAT THE RESEARCH ACTUALLY SHOWS:
  "Dyslexia fonts" (OpenDyslexic, etc.) have weak evidence
  Most studies: no statistically significant readability improvement
  from letterforms specifically designed for dyslexia

  WHAT IS EVIDENCE-BASED:
  1. LARGER SPACING:
     Letter-spacing +0.1em and word-spacing 0.3em show measurable benefit
     Extra leading (line-height 1.6–1.8) reduces confusion
     Wider character spacing alone helps more than font changes

  2. SANS-SERIF AT TEXT SIZES:
     Modest preference for clean sans over serif in many dyslexia studies
     (serifs can visually connect letters that should be distinct)
     Not universal: individual variation is large

  3. SHORT LINES:
     Shorter measure (40–60 chars) reduces tracking difficulty

  4. CLEAR LETTERFORM DISTINCTION:
     Fonts where 'b' and 'd' are clearly distinct (mirroring confusion)
     Fonts where 'p' and 'q' are clearly distinct
     Fonts with clear I/l/1 and O/0 distinction
     Atkinson Hyperlegible (Braille Institute, 2019): designed specifically
     for low vision; clear distinctions; free to use; good research basis

  5. HIGH CONTRAST:
     Not extreme contrast (#000 on #FFF) — some users prefer slight offset
     Off-white (#F8F8F8) + near-black (#1A1A1A) often preferred
     But avoid patterned or textured backgrounds

CSS FOR DYSLEXIA ACCESSIBILITY:
  body {
    font-size: 18px;
    line-height: 1.8;
    letter-spacing: 0.05em;
    word-spacing: 0.2em;
    max-width: 65ch;
    font-family: 'Atkinson Hyperlegible', 'Verdana', sans-serif;
  }

WCAG 1.4.12 (Text Spacing):
  No loss of content when user overrides:
  letter-spacing ≥ 0.12em
  word-spacing ≥ 0.16em
  line-height ≥ 1.5
  paragraph spacing ≥ 2em
  Your CSS should not use hard pixel heights that clip text at these values.

──────────────────────────────────────────────────────────────────────────────
```

---

## Comprehensive Layout Reference

```
LAYOUT DECISION REFERENCE
──────────────────────────────────────────────────────────────────────

BODY TEXT BASELINE (web):
  font-size: 16px;
  line-height: 1.5;
  max-width: 65ch;
  font-family: [system stack or chosen webfont];
  color: #1a1a1a;  /* slightly off-black; less harsh than pure black */

HEADING SCALE (typographic scale, minor third ≈ 1.2×):
  h6: 12px / 0.75rem
  h5: 14px / 0.875rem
  h4: 16px / 1rem
  h3: 20px / 1.25rem
  h2: 24px / 1.5rem
  h1: 30px / 1.875rem
  (or use Major Third 1.25×, Perfect Fourth 1.33×, etc.)

  Recommendation: use CSS custom properties for scale:
  --scale-ratio: 1.25;
  --size-sm: calc(1rem / var(--scale-ratio));
  --size-base: 1rem;
  --size-lg: calc(1rem * var(--scale-ratio));
  etc.

ALL-CAPS TREATMENT:
  text-transform: uppercase;
  letter-spacing: 0.08em;  /* Required; uppercase reads poorly without tracking */
  font-size: 0.85em;       /* Visually balance: caps look larger than mixed case */

NUMERIC TABLES:
  font-variant-numeric: tabular-nums;  /* fixed-width; columns align */
  font-family: [monospace fallback if tabular-nums not available];

CODE WITHIN PROSE:
  font-family: 'JetBrains Mono', 'Fira Code', Consolas, monospace;
  font-size: 0.875em;    /* monospace looks larger at same px; scale down */
  background: #f4f4f4;
  padding: 0.15em 0.3em;
  border-radius: 3px;

──────────────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Parameter | Optimal Range | Notes |
|-----------|---------------|-------|
| Measure | 45–75 characters | 65ch in CSS; narrower for multi-column |
| Leading (body) | 1.4–1.5× type size | More for wide measure; less for narrow |
| Leading (display) | 1.1–1.2× type size | Headlines: tight; display: very tight |
| Tracking (body) | 0 (default) | Do not add/remove from body text |
| Tracking (all-caps) | +0.05em to +0.1em | Required for uppercase legibility |
| Tracking (display) | -0.02em to -0.05em | Tighten large type slightly |
| Type size (body, screen) | 16–18px | WCAG baseline; 16px minimum |
| Type size (body, print) | 10–12pt | 10pt for quality print; 12pt generic |
| Contrast ratio (body) | ≥ 4.5:1 | WCAG AA; check with contrast tool |
| Contrast ratio (large) | ≥ 3:1 | ≥ 18pt or 14pt bold |
| Letter-spacing (dyslexia) | +0.05em | Evidence-based; also helps generally |
| Word-spacing (dyslexia) | +0.15–0.2em | Combined with letter-spacing |

---

## Common Confusion Points

**The browser's default line-height is not good enough**
Browser default: `line-height: normal` which maps to approximately 1.2. For body text, 1.2 is too tight — WCAG recommends 1.5 minimum for body text. Setting `line-height: 1.5` on the body element is the single highest-impact accessibility improvement for text-heavy interfaces.

**CSS letter-spacing is not kerning**
`letter-spacing` in CSS applies a uniform global adjustment to ALL letter pairs. OpenType kerning (font-kerning: auto, which is the default) applies pair-specific adjustments from the font's GPOS/kern tables. These operate independently. You can have both: kerning from the font applied, plus additional global tracking from letter-spacing. They add.

**Justified text is not "more professional"**
Justified alignment can look professional in book design where Knuth-Plass line-breaking + hyphenation is applied carefully. In web browsers, justified text with no hyphenation on a narrow measure creates rivers and inconsistent word spacing. Left-aligned text is almost always the right choice for web body text.

**The ch unit is an approximation**
`1ch = width of the '0' character` in the current font. Average character width is somewhat less. The common formula `65ch ≈ 65 characters per line` is an approximation; actual characters per line depends on the specific typeface. Check your layout visually, not just by the ch value.
