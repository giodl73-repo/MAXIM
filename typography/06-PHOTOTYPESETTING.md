# 06 — Phototypesetting: The Transitional Era (1950s–1980s)

## The Big Picture

Phototypesetting was the 30-year bridge between hot metal and digital typography. It eliminated the molten lead, moved to film output, enabled offset lithography, and introduced the concept of type as licensed intellectual property separate from physical hardware. The chaos it created — dozens of vendors selling the same typeface under different names — directly motivated the need for font format standardization (PostScript, OpenType).

```
PHOTOTYPESETTING TECHNOLOGY GENERATIONS
────────────────────────────────────────────────────────────────────────────────

GENERATION 1 (1950s): Mechanical/Optical
  Physical film negatives of characters + light flash + photographic paper
  Rotating disk or filmstrip of character images
  Speed: slight improvement over hot metal
  Examples: Photon (USA), Intertype Fotosetter

GENERATION 2 (1960s): Electro-optical
  Electronic control of exposure timing + lens adjustment
  CRT tubes beginning to appear for character generation
  Speed: ~5,000–8,000 chars/hr
  Examples: Linofilm, Photon 713, IBM 2680

GENERATION 3 (1970s–early 1980s): Fully digital rasterization
  Characters defined as digital bitmaps
  CRT or laser beam exposes photographic media
  Speed: 10,000–30,000 chars/hr
  Fully controllable spacing, kerning, tracking
  Examples: Compugraphic EditWriter, Berthold Diatronic, Hell Digiset

DIGITAL FRONT-END (1980s): Transition to PostScript
  Fully digital composition → PostScript interpreter → imagesetter
  Characters as Bézier outlines (resolution-independent)
  Speed: limited by RIP (Raster Image Processor), not mechanics
  → This is the digital typography era (Module 07)

────────────────────────────────────────────────────────────────────────────────
```

---

## Generation 1: Mechanical Phototypesetting (1950s)

### Why Phototypesetting at All?

The driving force was the printing industry's shift to **offset lithography**. Traditional letterpress printing (raised type → ink → paper) required heavy metal formes. Offset lithography (image on flat plate → transfers via rubber blanket → paper) was cheaper, faster, and produced higher quality at scale — but it needed film negatives as the intermediate, not metal type.

```
LETTERPRESS vs OFFSET LITHOGRAPHY
──────────────────────────────────────────────────────────────────────

LETTERPRESS (hot metal era):
  Metal type → inked → paper pressed against it
  Type face makes direct contact with paper
  Requires: physical metal type + forme + heavy press
  Output quality: good for text; limited for halftones

OFFSET LITHOGRAPHY (phototype era):
  Film negative → photosensitive plate (UV exposed)
  Plate → rubber blanket roller → paper
  Type never touches paper (indirect "offset" printing)
  Requires: film negative → NOT metal type
  Output quality: superior halftones; cheaper for long runs
  Speed: much faster for high-volume printing

WHY THIS MATTERS:
  If your output process wants film negatives,
  there is no reason to cast metal type at all.
  Phototypesetting: directly expose characters onto film.
  Bypass metal entirely.
──────────────────────────────────────────────────────────────────────
```

### Photon / Lumitype (1954)

The Photon (USA) and Lumitype (France) were the first commercial phototypesetting machines. The design:

```
PHOTON MACHINE DESIGN (~1954)
──────────────────────────────────────────────────────────────────────

  SPINNING DISK:
  ┌─────────────────────────────────────────────────────────────────┐
  │ Glass disk rotating at high speed                               │
  │ 96 characters arranged in concentric rings on the disk          │
  │ Each character = a film negative image of the letterform        │
  │                                                                 │
  │         ┌────────────────────────────────────────────────┐      │
  │         │  •  A  B  C  D  E  F  G  ...  (outer ring)     │     │
  │         │    • a  b  c  d  e  f  g  ... (inner ring)     │     │
  │         └────────────────────────────────────────────────┘     │
  └─────────────────────────────────────────────────────────────────┘

  When a character is needed:
  1. Disk rotates to position desired character over the light path
  2. Stroboscopic flash fires (microseconds — freezes the disk)
  3. Light passes through character's film negative
  4. Lens focuses and sizes the image
  5. Character exposed onto photosensitive paper/film
  6. Paper/film advances by character width amount

  SIZE CONTROL:
  A lens between disk and paper controls size
  Same disk character can be output at 6pt through 72pt by adjusting lens
  This was a key advantage over hot metal: one matrix → all sizes
  (Hot metal: different physical matrix for each size)
──────────────────────────────────────────────────────────────────────
```

---

## Generation 2: Electronic Control (1960s)

The second generation added electronic control of exposure timing, lens positioning, and line spacing. By 1965, CRT-based systems began appearing — characters drawn on a cathode ray tube and photographed.

Key milestone: **Linofilm** (Linotype Co., 1954 commercial) — Linotype's entry into phototypesetting, protecting its market position while the technology transitioned.

```
INTERTYPE FOTOSETTER — HYBRID DESIGN
──────────────────────────────────────────────────────────────────────

The Intertype Fotosetter (1950) was an interesting transitional machine:
  - Used Linotype-compatible matrices (existing investment)
  - But instead of casting metal, flashed light through the matrix
  - Matrix returned via same distributor mechanism as Linotype

This exemplifies the classic crossing-the-chasm problem:
  Optimize for backward compatibility (reuse existing matrices)
  vs. start clean with optically superior new designs
  Fotosetter chose backward compatibility → limited upside
  Later machines chose new designs → better quality but customer friction

THE TRANSITION PLAYBOOK:
  Linotype → Linofilm: same brand, new technology (protect base)
  ATF → couldn't make the transition (became irrelevant)
  Monotype → Monophoto: survived the transition
  New entrants: Compugraphic, Hell → better technology, no legacy
──────────────────────────────────────────────────────────────────────
```

---

## Generation 3: Digital Rasterization (1970s)

The third generation eliminated physical character images entirely. Characters were stored as digital bitmaps (raster data) and drawn on CRT or laser output devices.

```
HELL DIGISET (1965–1970) — FIRST DIGITAL TYPESETTER
──────────────────────────────────────────────────────────────────────

Developed by Dr. Ing. Rudolf Hell (Germany)
The first typesetter to use digitally stored character bitmaps

Architecture:
  Magnetic disk: stores character bitmaps as digital data
  CRT output: scans electron beam to draw characters
  Photographic paper: exposed by CRT beam

Performance (Digiset 50T):
  Speed: ~10,000 chars/hr
  Resolution: 600–1200 dpi
  Type sizes: 5–72pt from same digital master (via scaling)

THE BITMAP PROBLEM:
  Characters stored as bitmaps at one resolution
  Scaling up = blocky/aliased
  Different size masters needed for quality
  → Motivates outline (vector) representation
  → PostScript (1982) solves this with Bézier curve outlines
──────────────────────────────────────────────────────────────────────
```

### Compugraphic and Market Expansion

Compugraphic Corporation (1960–1988) was the dominant third-generation vendor, specifically targeting the mid-market with affordable systems:

```
COMPUGRAPHIC'S MARKET STRATEGY
──────────────────────────────────────────────────────────────────────

Before Compugraphic:
  Phototypesetting machines cost $100,000–$500,000
  Only major newspapers and large print shops could afford them
  Small print shops still used hand composition

Compugraphic innovation:
  EditWriter series (1972): $25,000 – $50,000
  Affordable for small newspapers, trade publications
  Simplified operation (keyboard + digital storage + output)
  "Democratized" professional typesetting

Result:
  Thousands of small publications switched from hot metal
  New profession: typesetting operator (vs. Linotype operator)
  Desktop typesetting: Compugraphic was the closest thing to DTP
  before the Macintosh (1984)
──────────────────────────────────────────────────────────────────────
```

---

## ITC: Type Licensing as Software Licensing

The International Typeface Corporation (ITC), founded in 1970, was the most structurally significant development in type business since Gutenberg. ITC did not manufacture type or machines — it was a pure intellectual property licensing intermediary.

```
ITC FOUNDING AND STRUCTURE
──────────────────────────────────────────────────────────────────────

FOUNDERS:
  Aaron Burns — graphic designer and typography educator
  Herb Lubalin — celebrated typographic designer
  Ed Rondthaler — veteran of phototypesetting industry (Photo-Lettering Inc.)

CONTEXT:
  By 1970, phototypesetting created a problem:
  Same typeface sold by 20 different vendors under 20 different names
  No licensing infrastructure for type designs
  Designers received no royalties when their work was reproduced
  In the US, letterform designs were NOT (and still are NOT) copyright-protected
    — the utility exception: letterforms are utilitarian
    — but the SOFTWARE encoding a font IS copyrighted
  In Germany, designs ARE protected; in UK, partial protection

ITC BUSINESS MODEL:
  1. License typeface designs from designers (pay royalties)
  2. License those designs to phototypesetting manufacturers
  3. Manufacturers pay ITC per unit manufactured or per license
  4. Designers receive royalties from ITC

  Revenue flow:
    Manufacturer → ITC → Designer
  (ITC takes a cut; designer gets royalty; manufacturer gets licensed design)

WHY THIS WAS REVOLUTIONARY:
  Before ITC: type designers often received one-time payment for designs
  After ITC: designers could receive ongoing royalties from popular typefaces
  This made type design a sustainable intellectual profession
  Parallel to software licensing (vs. work-for-hire)
──────────────────────────────────────────────────────────────────────
```

### ITC's Type Design Legacy

```
KEY ITC TYPEFACE RELEASES (1970–1990)
──────────────────────────────────────────────────────────────────────

1970  ITC Avant Garde Gothic (Herb Lubalin + Tom Carnase)
      Based on Lubalin's logo design for Avant Garde magazine (1968)
      Geometric sans with distinctive round forms and tight spacing
      Associated with the 1970s aesthetic; now nostalgic
      Note: works well as display; less so as body text (too tight default)

1971  ITC Souvenir (Ed Benguiat revival of Souvenir, Morris Benton 1914)
      Soft, rounded; extremely popular 1970s face; now vintage cliché

1974  ITC American Typewriter (Joel Kaden + Tony Stan)
      Slab serif resembling typewriter type; instantly recognizable
      Popular for advertising of the period

1974  ITC Bookman revival
1975  ITC Garamond (Tony Stan) — controversial revival;
      very different proportions from historical Garamond; not recommended

1975  ITC Tiffany (Ed Benguiat) — art nouveau influenced display

1977  ITC Galliard (Matthew Carter) — superb revival of Granjon types

1978  ITC Novarese (Aldo Novarese)

1980  ITC Clearface (Morris Fuller Benton revival)

The ITC era created a distinctive visual culture — warm, rounded, slightly
inflated forms. Look at a 1975 book or magazine and you'll recognize it.
──────────────────────────────────────────────────────────────────────
```

---

## Notable Type Designs of the Phototypesetting Era

### Optima (Hermann Zapf, 1958)

Optima is in a class of its own — the "serifless roman" or "flared sans":

```
OPTIMA — THE HYBRID
──────────────────────────────────────────────────────────────────────

Designed: Hermann Zapf; Stempel, Frankfurt; 1958
Inspired by: Zapf saw inscriptions on 15th-century Florentine gravestones
             with letterforms that were not serif but had slight terminal flares
             (Like the Roman capital letter tradition, but without full serifs)

OPTICAL PROPERTIES:
  Strokes: taper slightly toward terminals, then flare outward slightly
  The flare is NOT a serif — no perpendicular foot — but provides
  the visual anchoring that serifs provide
  Result: legibility of a serif face + cleanliness of a sans

  This makes Optima extremely hard to classify:
  ATypI calls it: "Glyphic" — carved letterforms
  Others: "humanist sans with flares"
  Design truth: it doesn't fit the classification system

USE:
  Long-form text where you want sans-serif cleanliness without coldness
  Premium design contexts: cosmetics branding, medical
  Vietnam Veterans Memorial (Maya Lin, 1982) — inscribed in Optima
  Lufthansa (historical brand identity)

LIMITATION:
  The subtle terminal flare can disappear at small sizes on low-resolution
  output → use at 11pt minimum for text; shines at display sizes
──────────────────────────────────────────────────────────────────────
```

### Frutiger (Adrian Frutiger, 1975)

Designed specifically for wayfinding at Charles de Gaulle Airport, Frutiger became the model for humanist sans typography:

```
FRUTIGER — DESIGNED FOR MOVEMENT
──────────────────────────────────────────────────────────────────────

Commission: Charles de Gaulle Airport (Roissy), opened 1974
            Signage system; type visible from moving vehicle at distance
Designed:   Adrian Frutiger; 1975 (simultaneously adapted for phototypesetting)

DESIGN CONSTRAINTS:
  Must read: from a car moving at 30+ mph (50+ km/h)
  Must read: at oblique angles (not straight-on)
  Must read: at varying distances
  Must distinguish: all letterforms instantly (I/l/1, O/0, etc.)

DESIGN SOLUTIONS:
  Open apertures: 'c', 'e', 'a' letters opened up so they never close
    to looking like 'o' at distance
  Clear letter distinctions: 'i' has distinct top serif-like element;
    '1' has distinct base; 'I' clear cap form
  Humanist proportions: not mechanical uniformity; natural rhythm
  Consistent stroke terminals: clear rhythm; not mechanical
  Wide range of weights: signage needs Light through Black

RESULT:
  Considered by many designers the most legible sans-serif typeface ever made
  Still used at Charles de Gaulle (and many other airports worldwide)
  Influenced subsequent humanist sans: Myriad, Meta, Thesis
  Frutiger Neue (2014): updated version

WHY THIS MATTERS FOR ENGINEERS:
  Frutiger's design process is a case study in type for user needs:
  Not "what looks elegant" but "what works in these conditions"
  The font-as-UX-solution approach
──────────────────────────────────────────────────────────────────────
```

---

## The Font Naming Chaos Problem

The phototypesetting era created a font naming disaster that continues to affect us:

```
THE FONT NAME PROBLEM
──────────────────────────────────────────────────────────────────────

PROBLEM:
  In the hot metal era: Linotype's matrices ≠ Monotype's matrices
  (Different physical equipment; different sizes; proprietary)

  In phototypesetting: same typeface design could be manufactured
  by ANY phototypesetter vendor — but licensing was unclear
  → Each vendor gave the design a different name:

  Helvetica (original):
    Linotype:         "Helvetica"
    Berthold:         "Akzidenz-Grotesk" (different but similar)
    ITC:              Didn't touch Helvetica (too well-known)
    Compugraphic:     "Helios"
    Autologic:        "Triumvirate"
    Alphatype:        "Megaron"
    AM Varityper:     "Geneva" (not the Apple font)

  Garamond:
    Linotype:         "Garamond"
    Berthold:         "Garamond"  ← same name, different design!
    ITC:              "ITC Garamond" ← very different design
    Stempel:          "Stempel Garamond"

  Futura:
    Bauer:            "Futura"
    Compugraphic:     "Spartan"
    Intertype:        "Techno"
    Mergenthaler:     "Twentieth Century"
    Monotype:         "Twentieth Century" (licensed)

This created:
  1. Consumer confusion (which "Garamond" am I getting?)
  2. No legal clarity (designs not protected in US)
  3. No standardization (file formats incompatible between vendors)
  4. Designer frustration (no royalties on copied designs)

RESOLUTION:
  PostScript (1982): standardized outline format
  OpenType (2000): unified format with licensing metadata
  Digital licensing: font files are copyrighted software
  ITC: established royalty model
  → But the naming confusion persists in many font databases today
──────────────────────────────────────────────────────────────────────
```

---

## Desktop Publishing: The Phase Transition (1984–1988)

The true end of phototypesetting was not a slow evolution but a phase transition triggered by a single year:

```
1984–1985: THE DESKTOP PUBLISHING REVOLUTION
──────────────────────────────────────────────────────────────────────

January 1984:  Apple Macintosh launched
               - 9" screen, 72 dpi, WYSIWYG interface
               - Bit-mapped screen fonts (Susan Kare)
               - MacPaint: drawing tools for desktop
               - No PostScript yet

January 1985:  Apple LaserWriter launched
               - First desktop laser printer with PostScript built in
               - 300 dpi output (600 dpi equivalent perception with PostScript)
               - Fonts: included Times, Helvetica, Courier, Symbol
               - Resident fonts = no download time for those faces

July 1985:     Aldus PageMaker 1.0 (for Macintosh)
               - First desktop page layout program
               - Print to LaserWriter = typeset-quality output at your desk
               - Previous cost: $50,000+ professional typesetting system
               - New cost: $3,000 Mac + $7,000 LaserWriter + $500 software

ECONOMIC DISRUPTION:
  Professional typesetters: their trade made obsolete in ~5 years
  Newspapers: composing rooms emptied by 1990
  New profession: "desktop publisher" (derogatory from professionals)
  Knowledge democratization: anyone with a Mac could do what
  required years of training and expensive equipment

THE QUALITY GAP CLOSED FAST:
  1985: LaserWriter at 300 dpi looked "good enough" for most uses
  1987: Linotype L300 PostScript imagesetter at 1270 dpi
  1989: PostScript imagesetters at 2400 dpi = film quality
  By 1990: DTP output indistinguishable from professional phototypesetting
──────────────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Generation | Technology | Speed | Key Products | Key Limitation |
|-----------|------------|-------|--------------|----------------|
| Gen 1 (1950s) | Spinning disk + flash | ~2,000 chars/hr | Photon, Fotosetter | Limited speeds; small character set |
| Gen 2 (1960s) | Electronic + CRT emerging | ~5,000 chars/hr | Linofilm, Photon 713 | Expensive; requires skilled operators |
| Gen 3 (1970s) | Digital bitmaps + CRT/laser | ~15,000 chars/hr | Compugraphic, Hell Digiset | Bitmap scaling; format chaos |
| DTP (1985+) | PostScript + Macintosh | Unlimited | LaserWriter, PageMaker | Initial low resolution (300 dpi) |

---

## Common Confusion Points

**Phototypesetting did not eliminate the type designer**
It changed what designers produced. Instead of cutting steel punches, designers drew letterforms on paper at large scale, which were then photographed and reduced to master film. Optima, Frutiger, Helvetica Neue, and most major typefaces you use were all developed during the phototypesetting era — it was a golden age of type design.

**ITC "Garamond" is not Garamond**
ITC Garamond (Tony Stan, 1975) is a controversial redesign with much wider proportions and a distinctly 1970s feel. If you specify "Garamond" and receive ITC Garamond, it looks quite different from Adobe Garamond Pro or EB Garamond. Always name the specific version when precision matters.

**"WYSIWYG" was a phototypesetting-era concept**
What-You-See-Is-What-You-Get was the promise of early desktop publishing — but with 72 dpi screen fonts and 300 dpi laser output, it was WYSIWYG only approximately. The idea that the screen should preview the printed page was a phototypesetting-era aspiration that DTP partially delivered. Perfect WYSIWYG (screen = print) still doesn't exist due to DPI differences and rendering engine differences.

**Compugraphic and Berthold are not remnants**
Compugraphic (1960–1988) was acquired by Agfa in 1988. Berthold (German foundry) went bankrupt in 1993; the library has been partially sold off. Neither company survived the digital transition — they were specialized for phototypesetting hardware that became worthless with PostScript DTP.
