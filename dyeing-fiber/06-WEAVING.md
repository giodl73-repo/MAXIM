# Weaving: Loom Taxonomy, Weave Structures, Sett, Tapestry

## The Big Picture

Weaving interlaces two sets of threads at right angles: the **warp** (longitudinal threads, held under tension) and the **weft** (transverse threads, passed through the warp). Every weave structure is defined by the pattern of over-under crossings between warp and weft. The mathematics of this pattern — the threading, tieup, and treadling — can be encoded as a binary matrix.

```
WEAVING FUNDAMENTALS

  WARP: threads running lengthwise (vertical on loom), held under tension
    Wound onto back beam, pass through heddles, drawn over breast beam
    Warp threads: typically stronger, smoother than weft
    Named: end (singular), ends per inch (EPI)

  WEFT: threads running crosswise, inserted as "shots"
    Carried by shuttle through the shed
    Named: pick (singular), picks per inch (PPI)
    Often softer, more decorative than warp

  SHED: opening between raised and lowered warp threads
    Shuttle passes through shed to insert weft pick
    Shed formed by lifting heddle(s) via shaft(s) + treadle

  SELVEDGE: self-finished edge at each side of woven cloth
    Weft loops back at each edge (not cut)
    Critical for fabric integrity; requires consistent tension
```

---

## Loom Taxonomy

```
LOOM TYPES (by complexity and capability)

BACKSTRAP LOOM:
  Warp tension: body lean (back strap around weaver's waist)
  No rigid frame: portable, used standing or sitting
  Sheds: one rigid heddle, one shed stick
  Traditions: Andean (Peru, Bolivia), Mexican, Guatemalan, Javanese
  Produces: narrow cloth (limited by arm reach), often warp-faced

RIGID HEDDLE LOOM:
  Simple frame, single heddle rod with slots and holes
  Slot warp threads: rise and fall freely
  Hole warp threads: controlled by heddle movement
  Two sheds: heddle up (hole threads rise) and heddle down
  Good for: plain weave, simple patterns, beginners
  Width: 10-45 cm typically

4-SHAFT TABLE LOOM:
  4 independent shafts (harnesses), each holding heddles
  Levers (no treadles) lifted by hand for each shed
  Enables: twill, huck lace, simple pattern weaves
  Width: 40-75 cm typical
  Portable; good for sampling and learning

4-SHAFT FLOOR LOOM:
  4 shafts operated by foot treadles (hands free for shuttle)
  Treadles: 4, 6, or more, tied to shafts via tie-up
  Enables: all patterns possible on 4 shafts
  Width: 60-120 cm typical
  Standard equipment for production weaving

8-SHAFT FLOOR LOOM:
  8 independent shafts: expanded pattern vocabulary
  Summer-and-winter, overshot, complex twills, M's and O's
  Width: 60-120 cm

COUNTERBALANCE vs. JACK vs. COUNTERMARCH:
  Jack: each shaft rises independently; versatile, common in North America
  Counterbalance: shafts connected in pairs; rise/fall together; warp-balanced
  Countermarch: each shaft has independent direct and indirect tie-up; best shed
```

---

## Sett: Ends Per Inch and Cover Factor

Sett determines the structural character of the cloth. Too open: unstable; too dense: weft cannot pack in.

```
SETT CALCULATION

  Sett = ends per inch (EPI) in warp
  Starting point: wrap yarn around ruler, count WPI (wraps per inch)
    Plain weave: EPI = WPI / 2 (50% openness required for weft)
    Twill (2/2): EPI = WPI / 1.5 (more compact)
    Warp-faced: EPI = WPI * 1.0 (no weft visible)
    Weft-faced (tapestry): EPI = WPI * 0.33 (sparse warp, weft covers all)

COVER FACTOR:
  Fraction of cloth surface covered by yarn
  Plain weave balance: 50% warp + 50% weft coverage (if weft = warp diameter)
  Warp-faced: warp covers 100%, weft buried
  Weft-faced (tapestry): weft covers 100%, warp buried

EXAMPLE SETTS by yarn weight:
  Lace weight (40+ WPI): 20 EPI plain weave, 26 EPI twill
  Fingering (20 WPI): 10 EPI plain weave, 14 EPI twill
  DK/worsted (12 WPI): 6 EPI plain weave, 8 EPI twill
  Bulky (7 WPI): 3-4 EPI plain weave, 5 EPI twill
```

---

## The Three Primary Weave Structures

All weave structures are variations on three parent structures:

### Plain Weave (Tabby)

```
PLAIN WEAVE DRAWDOWN

  Warp: 1 2 3 4 (threads numbered left to right)
  Shaft threading: 1-2-1-2-1-2...

  DRAWDOWN (X = warp over weft, . = weft over warp):
  Pick 1 (shaft 1 up): X . X . X . X .
  Pick 2 (shaft 2 up): . X . X . X . X

  PROPERTIES:
    Maximum interlacement: every thread crosses at every opportunity
    Strongest structure per unit weight
    Maximum wear resistance (no exposed floats to snag)
    Minimum fabric flexibility (all threads lock each other)
    Appearance: balanced grid pattern ("square" cloth)
    Examples: taffeta (silk), calico (cotton), muslin, canvas
```

### Twill

```
TWILL DRAWDOWN (2/2 twill, 4 shafts)

  Threading: 1-2-3-4-1-2-3-4...
  Treadling: 1-2 / 2-3 / 3-4 / 4-1 (each treadle lifts pair)

  DRAWDOWN (2/2 balanced twill):
  Pick 1 (1+2 up): X X . . X X . . X X . .
  Pick 2 (2+3 up): . X X . . X X . . X X .
  Pick 3 (3+4 up): . . X X . . X X . . X X
  Pick 4 (4+1 up): X . . X X . . X X . . X

  Diagonal line visible: warp floats on one face, weft floats on other

  PROPERTIES:
    2/2 twill: each thread over 2, under 2
    Diagonal line angle: depends on EPI/PPI ratio
    More drapeable than plain weave (fewer interlacement points)
    Stronger warp alignment: better for diagonal stress
    Examples: denim (3/1 twill, warp-faced), herringbone, houndstooth

TWILL VARIATIONS:
  3/1 twill: warp over 3, under 1 -> warp-faced, very drapeable (denim)
  1/3 twill: warp under 3, over 1 -> weft-faced
  Herringbone: reversal of twill direction creates zigzag
  Houndstooth: two-color herringbone with specific threading
  Diaper twill: diamond pattern from combining Z and S twill direction
```

### Satin and Sateen

```
SATIN (warp-faced): warp floats over many weft picks
SATEEN (weft-faced): weft floats over many warp ends

  5-SHAFT SATIN:
  Threading: 1-2-4-1-3-2-4-3-1...
  (non-consecutive floats: move 2 shafts per pick, not 1)

  PROPERTIES:
    Very long floats: 4 or 7 or more
    Surface: smooth, lustrous (floats reflect light uniformly)
    Structure: very few interlacement points -> weak, snag-prone
    Examples: charmeuse (silk), sateen (cotton), satin ribbons

  WHY NON-CONSECUTIVE THREADING:
    If consecutive (like twill), floats would align -> twill diagonal
    Satin requires floats distributed as evenly as possible -> uniform sheen
    Mathematical: use a "move number" (2, 3, or coprime to shaft count)
```

---

## Tapestry

Tapestry is weft-faced: the warp is entirely covered by weft, and different colored weft yarns are used for pictorial images. The weft does not extend from selvedge to selvedge -- it turns back at color boundaries (discontinuous weft).

```
TAPESTRY STRUCTURE

  Warp: structural foundation, completely hidden by dense weft packing
  Weft: colored picture threads, packed tightly, warp invisible
  Cover: 100% weft coverage
  Structure: plain weave (every warp up alternates) but weft very dense (PPI >> EPI)
  Typical: 8-12 EPI, 30-60 PPI

  SLIT TAPESTRY vs. INTERLOCKED WEFT:
    SLIT: two adjacent colors leave a gap (slit) where they turn back
      Structural weakness along color boundaries; sewn closed or left for effect
      Traditional: Coptic, Peruvian

    INTERLOCKED: weft yarns from adjacent colors link before turning back
      More labor-intensive; no slit
      Traditional: French Gobelin

  TRADITIONS:
    European Gobelin: high-warp or low-warp loom, cartoon below or behind
    Navajo rug: warp-faced but related technique, strong weft packing
    Kilim (flat-woven rug): same structure, used for functional floor coverings
    Pre-Columbian: Paracas and Nazca culture, complex interlocked tapestry
```

---

## Draft Notation

Weave structure is encoded in a standardized grid notation:

```
DRAFT NOTATION SYSTEM

  THREADING DRAFT (top of drawdown):
    Which warp threads go through which shaft
    Column = warp thread (left to right)
    Row = shaft (bottom to top usually)
    Mark = this thread on this shaft

  TREADLING (right side of drawdown):
    Which treadles pressed for each weft pick
    Row = weft pick (top to bottom)
    Column = treadle
    Mark = treadle pressed for this pick

  TIE-UP (top right corner):
    Which shafts each treadle lifts
    Row = shaft
    Column = treadle
    Mark = this treadle lifts this shaft

  DRAWDOWN (main body):
    Result: which warp ends are raised for each pick
    X or black square = warp on top (warp covers weft at this intersection)
    White = weft on top

EXAMPLE: 2/2 twill on 4 shafts, 4 treadles
  Threading: 1-2-3-4-1-2-3-4
  Tieup:     T1=S1+S2, T2=S2+S3, T3=S3+S4, T4=S4+S1
  Treadling: T1-T2-T3-T4-T1-T2-T3-T4

  This notation fully specifies the cloth; published in Strickler's "A Weaver's Book of 8-Shaft Patterns"
```

---

## Decision Cheat Sheet

| Goal | Weave Structure | Sett | Loom |
|------|-----------------|------|------|
| Sturdy dish towels | Plain weave | WPI/2 (balanced) | Rigid heddle or 4-shaft |
| Denim-style fabric | 3/1 twill warp-faced | WPI * 0.8 | 4-shaft floor loom |
| Drapey garment fabric | 2/2 twill | WPI/1.5 | 4-shaft floor loom |
| Smooth silk scarves | Satin (8-shaft) | WPI/1.2 | 8-shaft loom |
| Pictorial wall hanging | Tapestry (plain weave weft-faced) | 8-12 EPI, pack weft | Any warp-controlling loom |
| Andean bands | Backstrap warp-faced | WPI | Backstrap loom |
| Beginners / sampling | Plain weave | WPI/2 | Rigid heddle |
| Complex pattern weaves | Overshot, huck, M's and O's | WPI/1.5 | 4+ shaft floor loom |

---

## Common Confusion Points

**Warp vs. weft confusion in finished cloth** -- Warp runs the length of the fabric (selvedge to selvedge direction is the warp); weft runs the width. In a skirt or curtain: warp is typically vertical (lengthwise grain has less stretch, more strength). Cutting "on the bias" (45 degrees to both) maximizes stretch in any direction.

**"Float" is not a defect, it is a structural element** -- A float is a yarn crossing over multiple perpendicular threads before going under. Long floats create sateen sheen or the body of overshot pattern cloth. Short floats create the interlacement points that give cloth its strength. The design balance between floats and interlacement defines cloth character.

**"4-shaft" does not mean "4 treadle"** -- Shafts and treadles are independent. A 4-shaft loom can have 4, 6, or 8 treadles. Each treadle activates a combination of shafts (per the tie-up). More treadles = more combinations available without re-tying.

**Sett is not constant across structures** -- A thread used at 10 EPI for plain weave should be used at 14 EPI for 2/2 twill (same thread, different interlacement frequency). The formula changes because denser interlacement requires tighter sett to beat evenly. Weaving the wrong sett for the structure produces either a brick-like cloth (too tight) or an unstable loose cloth (too open).
