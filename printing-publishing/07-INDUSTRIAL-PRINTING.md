# Industrial Printing: Steam Press, Rotary Press, Linotype, Offset Lithography, Phototypesetting

## The Big Picture

Industrial printing is a series of automation upgrades to the Gutenberg system. Each step trades capital expenditure for labor reduction at scale. The same pattern as every industrial revolution: manual skilled labor replaced by machines, production volumes increase, unit costs collapse.

```
PRINTING TECHNOLOGY PROGRESSION: OUTPUT CAPACITY

Technology              Year    Sheets/hour   Key Constraint
-----------------------+-------+-------------+---------------------------
Hand press             1455    ~250           Human muscle power
Koenig steam press     1814    ~1,100         Steam cylinder
Applegath 4-cylinder   1828    ~5,000         Multiple cylinder banks
Hoe Type-Revolving     1847    ~20,000        Rotary, type on cylinder
Web rotary (newsprint) 1865    ~18,000*       Continuous paper roll
Linotype + web rotary  1890s   ~40,000*       Mechanical composition
Offset lithography     1900s   ~10,000-50,000 Thin flexible plates
Modern offset (sheetfed) 2020s ~15,000-18,000 Digital prepress
Modern web offset      2020s   ~80,000+       Digital workflow

* sheets/hour equivalent (web rotary runs continuously, counted in copies)

ORDERS OF MAGNITUDE:
  Hand press (1455) to web rotary (1865): ~80x improvement
  Linotype (1884) removed the COMPOSITION bottleneck
  (Fast press was useless if type couldn't be set fast enough)
```

---

## Koenig Steam Press (1814)

The first application of steam power to printing — the enabling technology for the penny press and mass newspapers.

```
KOENIG STEAM PRESS MECHANISM (1814)

Friedrich Koenig (German inventor):
  Developed in London for John Walter II (The Times, London)
  First use: The Times, November 29, 1814

MECHANISM:
  Gutenberg flat press:
    Paper pressed down onto flat type forme
    One press cycle = one sheet side
    Operator turns screw manually

  Koenig's cylinder press:
    +---[STEAM ENGINE]---+
    |                    |
    |  CYLINDER (rotates)|
    |  Paper wraps around|
    |  cylinder          |
    +--------------------+
           |
    +------v------+
    |  TYPE FORME |  <- still flat, moves back/forth
    |  (reciprocating bed)|
    +--------------+

  Type forme moves forward under rotating cylinder
  Cylinder presses paper against type as it rotates
  Forme returns as cylinder lifts slightly
  Inking done by inking rollers on return stroke
  No manual inking required (rollers mechanized)

OUTPUT:
  Hand press: ~250 sheets/hour
  Koenig 1814: ~1,100 sheets/hour
  Koenig 1816 (2-cylinder): ~2,400 sheets/hour
  Improvement: 4-10x immediate, further refinements later

The Times (London): printed its entire run on the new press
  without the compositors knowing until they arrived in morning
  (Walter feared sabotage from workers who would lose jobs)
```

---

## Rotary Press

```
ROTARY PRESS EVOLUTION

CONCEPT: Instead of flat forme + cylinder, make the TYPE itself
          into a cylinder. Both type and impression are round.
          Continuous motion, no reciprocating bed.

PROBLEM: How do you put type on a cylinder?
  Solution 1: stereotype plates
    Make a papier-mâché or plaster impression of flat type
    Cast curved metal plate from that impression
    Wrap plate around cylinder
    Problem: loss of fine detail, additional step

  Solution 2: type secured to cylinder directly
    Richard Hoe's "Type-Revolving Press" (1847)
    Type secured on large central cylinder (~2m diameter)
    Multiple impression cylinders around it (~4-6)
    Paper feeds between type cylinder and each impression cylinder
    Each impression cylinder: one press operator
    6 impression cylinders -> 6 operators -> 6x output

HOE PRESS OUTPUT:
  Hoe Type-Revolving (1847): ~18,000-20,000 impressions/hour
  Philadelphia Public Ledger: first US user (1847)

WEB ROTARY (1865-1870s):
  KEY INNOVATION: Continuous roll of paper ("web") instead of sheets
  Walter Press (1866, The Times, London): first web rotary
  Paper feeds from roll (massive spool, tons of paper)
  Printing continuous: no stop-and-feed per sheet
  Cutting and folding integrated at output end

  WEB PRESS PAPER PATH:
  [Paper Roll] -> unwinding tension control
              -> printing unit (type cylinder + impression cylinder)
              -> second printing unit (back side)
              -> folding cylinder: folds web into pages
              -> cutting: cuts into newspaper sections
              -> stacking/bundling at speed

  Output: New York Tribune's press (1875): ~18,000 complete
          4-page newspapers per hour
```

---

## Linotype Machine (Mergenthaler, 1884)

The bottleneck by the 1870s was not press speed — it was composition. Setting type by hand (individual characters from type case) was the limiting step. The Linotype eliminated it.

```
LINOTYPE: THE COMPOSITION BOTTLENECK SOLUTION

PROBLEM:
  Fast steam presses could print 10,000+ sheets/hour
  Hand compositor: 1,000-1,500 ems/hour
  (An "em" = width of capital M; standard measure of composition speed)
  Newspaper page: ~30,000-60,000 ems
  One compositor: 20-60 hours per page
  Need: dozens of compositors per large newspaper

  Compositors were highly skilled, highly paid:
  Must know location of every character in the type case
  Must space words correctly (justified text)
  Must reverse-read mirror-image type
  Strong union: International Typographical Union

OTTMAR MERGENTHALER'S SOLUTION (1884):
  Keyboard-operated machine that:
  1. Assembles matrices (brass molds) for each character
  2. Casts a complete line of type as a single metal slug
  3. Distributes matrices back for reuse automatically
  4. Returns used slugs to melting pot for recycling

LINOTYPE MECHANISM:

  Operator keyboard: 90 keys
  (Lowercase, uppercase, numbers, punctuation, spaces)

  When key pressed:
    Matrix drops from magazine into assembling elevator
    Matrices line up -> form line

  When line complete:
    Operator presses justify key
    Space bands expand to fill line width (justified text)
    Assembled matrices raised to mold wheel
    Molten lead alloy injected -> LINE CAST
    Slug: one complete line of type in relief
    ~height = type high, exact width of column

  Matrices: returned via overhead distribution system
    Each matrix has notch pattern at top
    Distributor bar: sorts matrices back into correct magazine slots
    One matrix can be reused immediately

  Recycling:
    Printed slugs melted back in pot
    Lead alloy recycled immediately
    No permanent type inventory needed

OUTPUT:
  Hand compositor: 1,000-1,500 ems/hour
  Linotype operator: 5,000-6,000 ems/hour
  Productivity gain: ~4-5x on composition
  Skill level: lower (keyboard, not knowledge of type case positions)

IMPACT ON UNION LABOR:
  ITU (typographers union) fought Linotype vigorously
  Eventually negotiated: Linotype operators must be union members
  Set minimum crew sizes
  Slower adoption in union-strong markets
  Result: Linotype created new union job category instead of eliminating union

NEWSPAPER ECONOMICS BEFORE LINOTYPE:
  Large paper: 100+ compositors per shift
  After Linotype: 20-30 operators per shift
  Enabled: same-day composition of late news
  Previously: deadline meant "type set by 4pm for morning paper"
  With Linotype: "type set by 1am for 2am press run"
```

---

## Monotype System (Lanston, 1887)

Alternative to Linotype: cast individual characters, not lines.

```
MONOTYPE vs LINOTYPE COMPARISON

LINOTYPE (1884, Mergenthaler):
  Casts COMPLETE LINE as one slug
  One machine: keyboard + caster combined
  Error correction: re-keyboard entire line
  Best for: newspaper text (speed priority)
  Type quality: good but not perfect

MONOTYPE (1887, Tolbert Lanston):
  Two machines:
    1. Keyboard: punches holes in paper ribbon (like piano roll)
    2. Caster: reads ribbon, casts INDIVIDUAL CHARACTERS
  Error correction: re-punch single character
  Best for: book and fine printing (quality priority)
  Type quality: excellent (individual characters, precise)

The two systems coexisted and served different markets:
  Newspapers: mostly Linotype (speed)
  Books/quality printing: mostly Monotype
  Both used same lead-antimony-tin alloy as Gutenberg
  Both completely replaced by phototypesetting in 1960s-70s
  Both completely gone from commercial printing by ~1985
```

---

## Offset Lithography

A completely different printing principle — not letterpress (relief). The dominant commercial printing process since the mid-20th century.

```
OFFSET LITHOGRAPHY: PHYSICS AND MECHANISM

FUNDAMENTAL PRINCIPLE: Oil and water do not mix.

  Image areas: accept oil-based ink, repel water
  Non-image areas: accept water, repel oil-based ink
  This is a CHEMICAL difference, not physical relief

LITHOGRAPHY ORIGINS:
  Alois Senefelder (Bavaria, 1796):
  Discovered: grease drawing on flat limestone + acid
  Grease drawing areas: accept ink
  Acid-etched areas: retain water, reject ink
  First flat (planographic) printing

OFFSET PRINCIPLE (~1900-1904):
  Problem with direct lithography: printing directly on rough/textured
  surfaces is difficult; stone/plate wears fast

  Solution: transfer ink to intermediate rubber blanket first

  OFFSET PRESS (3-cylinder):

  PLATE CYLINDER                BLANKET CYLINDER
  (aluminum plate)    prints to  (rubber blanket)
                                    |
                                    | transfers to
                                    v
                               IMPRESSION CYLINDER
                               (paper between blanket
                                and impression)

  WHY "OFFSET": image first goes (is offset) to blanket, THEN to paper

  BLANKET ADVANTAGES:
  - Rubber conforms to paper surface texture
  - Much better quality on rough paper
  - Plate never touches paper: plate lasts longer
  - Can print on almost any surface

OFFSET PLATE:
  Aluminum plate, photosensitized coating
  Light through film negative exposes plate
  Developer washes away unexposed areas
  Fixing: binds image areas to plate
  No raised/recessed surface: completely flat
  Image = chemical property, not physical relief

FOUR-COLOR OFFSET (CMYK):
  Separate plate for each color:
  Cyan + Magenta + Yellow + Black (Key)
  Halftone screening: each color broken into dots
  Dot size varies to simulate continuous tone
  All four dots printing at different angles:
    -> avoids moiré pattern (halftone rosette)
  Print in registration: dots align across colors

  Process colors and their screen angles:
  Cyan: 105 degrees
  Magenta: 75 degrees
  Yellow: 90 degrees
  Black: 45 degrees (most visible, needs most accuracy)
```

---

## Phototypesetting — Eliminating Hot Metal

```
PHOTOTYPESETTING EVOLUTION (1950s-1985)

CONCEPT: Replace metal type with photographic image of characters

PHASE 1 (1950s-1960s): Second-generation systems
  Intertype Fotosetter (1949): modified Linotype
  Uses glass matrix instead of metal matrix
  Character illuminated through glass -> photographic paper
  Still mechanically similar to Linotype
  Output: photographic type on paper
  Advantage: lighter, no hot metal, faster film output

PHASE 2 (1960s-1970s): CRT-based
  Characters as electronic waveforms
  CRT displays characters on screen
  Lens system projects CRT image onto photographic paper
  Speed: 1,000+ characters/second
  Resolution: very high
  Fonts: stored as analog waveform data

PHASE 3 (1970s-1985): Digital raster
  Characters as bitmaps in computer memory
  Raster laser or CRT exposing phototypesetter
  Font: digital bitmap or outline
  Output to: photographic paper or film
  Computer controls: all spacing, hyphenation, pagination
  Examples: Compugraphic, Linotronic, Berthold

IMPACT:
  Hot metal typesetting: eliminated in ~20 years (1960s-1980s)
  Compositors: massive job loss
  ITU union: rapid decline
  Cost: plummeted
  Quality: improved (no physical wear, exact reproduction)
  Lead alloy: no longer needed (environmental benefit)

WORKFLOW (late 1970s):
  Writer -> typewriter/word processor
         -> markup (typographic instructions)
         -> keyboarder inputs to phototypesetter computer
         -> galleys output on photographic paper
         -> paste-up on boards (wax adhesive)
         -> camera: photograph boards -> film
         -> film -> offset plate
         -> press

  This workflow is what PageMaker (1985) eliminated for small publishers
  Large commercial printers retained it until early 1990s
```

---

## Impact on Labor and Society

```
PRINTING LABOR TRANSITIONS

HAND PRESS ERA (1455-1814):
  Masters, journeymen, apprentices
  Small shops: 2-5 workers
  Compositors: skilled, literate, high status
  Franklin's autobiography: printer's trade = path to literacy

STEAM PRESS ERA (1814-1884):
  Separation: composition (skilled) vs presswork (semi-skilled)
  Larger shops: 20-50 workers
  First industrial printing labor organizations (~1850s)

LINOTYPE ERA (1884-1960s):
  ITU (International Typographical Union): 1852
  Strong union: controlled training, apprenticeship, wages
  Linotype operator: reskilled from compositor
  Union fought automation but successfully captured new technology

PHOTOTYPESETTING ERA (1960s-1985):
  Keyboarding: lower skill than composition
  ITU: sharp membership decline
  Publishers moved operations to non-union shops
  Wapping dispute (UK, 1986): Rupert Murdoch moved
    News International to Wapping plant
    Replaced union typesetters with new computerized systems
    Fought 13-month strike
    Won: decisive defeat of UK print unions
    Similar battles in US and Europe throughout 1980s

DESKTOP PUBLISHING ERA (1985+):
  Eliminated almost all dedicated prepress jobs
  Design + layout: now done by one person with Mac + PageMaker
  Printing plant: much smaller staff
  Analogous to: GitHub Copilot replacing junior developers
```

---

## Decision Cheat Sheet

| Technology | Year | Key Innovation | Production Change |
|-----------|------|----------------|------------------|
| Koenig steam press | 1814 | Steam power, cylinder impression | 250 -> 1,100 sheets/hr |
| Hoe type-revolving | 1847 | Type on cylinder, multiple impression units | ~20,000 sheets/hr |
| Web rotary | 1865 | Continuous paper roll, integrated folding | Continuous production |
| Linotype | 1884 | Cast complete type lines from keyboard | 4-5x composition speed |
| Monotype | 1887 | Cast individual chars from paper tape | Better quality, slower |
| Offset lithography | 1900s | Oil/water chemistry, rubber blanket transfer | Any surface, high quality |
| Phototypesetting | 1950s-70s | Photo/digital chars replace metal | Eliminated hot metal |

---

## Common Confusion Points

**"Offset lithography uses raised type like Gutenberg."** Offset is planographic — the printing surface is completely flat. Image and non-image areas are chemically different, not physically raised or recessed. This is a fundamentally different physical principle from relief printing (letterpress, flexography) or intaglio (gravure, etching).

**"The Linotype replaced the hand compositor immediately."** The transition took decades. Unions negotiated work rules, reskilling programs, and minimum staffing. The full replacement of hand composition in the US newspaper industry took ~30-40 years (1884-1920s). In book printing, the Monotype system ran parallel to Linotype well into the 1960s.

**"Phototypesetting is 'digital printing.'"** Phototypesetting is photographic output — light exposing photographic paper or film. "Digital printing" (laser printers, inkjet, digital offset like HP Indigo) is direct marking of the final substrate. The confusion arises because phototypesetting used digital data to drive the exposure, but the output medium was still analog photographic.

**"The Wapping dispute was about printing technology."** It was about union power, not technology. Murdoch's new Wapping plant had been secretly equipped and staffed while negotiations continued. The technology (ATEX computerized composition) was already in use elsewhere. The dispute was about whether the printing unions could maintain exclusive control over the new technology's operation.

**"CMYK mixing produces all colors."** CMYK is a subtractive color model that approximates a large but not complete color gamut. Rich blacks require all four colors. Spot colors (Pantone) are pre-mixed inks for colors outside CMYK gamut. High-end printing adds 5th and 6th color stations. The CMYK approximation is why printed color never exactly matches screen color (which is additive RGB).
