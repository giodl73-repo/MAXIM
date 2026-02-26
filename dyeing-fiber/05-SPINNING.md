# Spinning: Twist, Draft, Drop Spindle, Spinning Wheel, Yarn Structure

## The Big Picture

Spinning converts loose fiber into yarn through two simultaneous actions: **draft** (attenuate the fiber mass to the desired thickness) and **twist** (lock the attenuated fibers together so they can bear load). Without draft, you cannot control thickness. Without twist, fibers slide past each other and the yarn falls apart. Every spinning system is a variation on delivering these two operations in a controlled sequence.

```
THE TWO OPERATIONS

  DRAFT: Thin out the fiber supply
    Fiber bundle <=====> pull apart <===> thinner bundle
    Staple length determines how far you can draft before fibers separate
    (Draft ratio = input length / output length per unit time)

  TWIST: Lock the drafted fibers
    Twisted fibers: friction locks them -> yarn can bear tension
    Twist direction:
      Z-twist: top tilts right  ( /  like center bar of Z)
      S-twist: top tilts left   ( \  like center bar of S)

CRITICAL SEQUENCE:
  Draft BEFORE twist gets to that section.
  If twist enters the fiber supply before you draft, the fibers lock
  and will not draft further -> thick spot -> uneven yarn

  STAPLE THEORY:
    Draft zone must be <= staple length apart
    Short draft (supported): < 2 x staple length
    Long draw: > 2 x staple length (relies on twist controlling thin spots)
```

---

## Twist Physics

Twist mechanics have a direct physical basis:

```
TWIST PER INCH (TPI) AND YARN STRENGTH

  As TPI increases from 0:
    Fiber-to-fiber friction increases
    Yarn strength increases
    Yarn diameter decreases (fibers compact)
    Eventually: too much twist -> yarn biased, kinks, weakens

  OPTIMAL TWIST FACTOR:
    twist_factor = TPI * sqrt(yarn_count)  (empirical constant for fiber type)
    Wool: 3-5 (lace) to 8-12 (sock/worsted)
    Cotton: 3-6 (weaving warp)

  WHY TWIST IN OPPOSITE DIRECTIONS FOR PLYING:
    Singles Z-twist + ply S-twist = balanced yarn
    The ply twist partially untwists the singles, creating stable structure
    Net angle: individual fibers at ~45 degrees to yarn axis (maximum strength)
    Unbalanced yarn (same twist direction): rotates, biases, distorts fabric

YARN GEOMETRY:
  Single (singles): one strand, typically biased (wants to untwist)
  2-ply: two singles twisted together in opposite direction
  3-ply: three singles twisted together
  Cable / chain: plied yarn then plied again with third direction reversal
```

---

## Drop Spindle: Gravity-Driven Spinning

The oldest spinning tool. A shaft with a whorl (flywheel) that stores rotational momentum. Available worldwide from Neolithic period forward:

```
DROP SPINDLE ANATOMY

         SHAFT (wooden, ~30-45cm)
           |
    ----HOOK (at top) -- yarn wrapped here
           |
           |  yarn wrapped up shaft
           |
  [===WHORL===]  (at bottom: high whorl spindle)
                 or at top: low whorl

  WHORL: disc of clay, stone, or wood -- acts as flywheel
  Heavier whorl = more momentum = longer spin = needs thicker, heavier fiber
  Lighter whorl = less momentum = finer yarn possible

SPINNING TECHNIQUE (drop spindle):

  PARK AND DRAFT:
    1. Spin spindle, "park" it (hang or rest in bowl)
    2. Draft fiber while spindle is stationary
    3. Release spindle, let twist run up into drafted fiber
    4. Repeat
    ADVANTAGE: Maximum control. Good for beginners.

  SUPPORTED DROP (in bowl):
    Spindle rests in small bowl at bottom
    Continuous spinning while drafting
    Used for very fine or short fibers (cotton, cashmere)

  LONG DRAW ON DROP SPINDLE:
    Advanced: draft and let twist climb simultaneously
    Fastest technique on drop spindle
    Requires understanding of twist propagation
```

---

## Spinning Wheel: Mechanical Spinning

Two fundamental designs evolved: the great wheel (spindle wheel) and the treadle wheel (flyer-and-bobbin system).

### Great Wheel (Malt Spindle / Walking Wheel)

```
GREAT WHEEL MECHANICS

  Large drive wheel (hand-driven, 1-1.5m diameter)
  Drives small spindle via drive band

  Drive ratio: wheel circumference / whorl circumference
    Example: 1.2m wheel / 0.03m whorl = 40:1
    One turn of wheel = 40 turns of spindle

  SPINNING MOTION: intermittent
    1. Draft fiber outward (away from spindle) while turning wheel forward
    2. Twist travels up drafted fiber
    3. Reverse wheel slightly to release twist
    4. Wind onto spindle by advancing at right angle
    LIMITATION: Cannot draft and wind simultaneously -> slow

  USED FOR: woolen preparation (short-draw), walking away from wheel
  Historical: flax, wool in medieval and early modern Europe
  Revival: teaching tool, production of thick woolen singles
```

### Flyer-and-Bobbin (Treadle Wheel): Continuous Spinning

The pivotal invention (attributed to Jürgen / Johann of Nuremberg, ~1530s): the flyer-and-bobbin mechanism allows simultaneous drafting and winding:

```
FLYER-AND-BOBBIN MECHANISM

  WHEEL -> DRIVE BAND -> WHORL/PULLEY on FLYER/BOBBIN

  FLYER: U-shaped, with hooks. Twists the yarn.
  BOBBIN: sits on flyer shaft, winds the yarn.
  DIFFERENTIAL ROTATION: flyer and bobbin rotate at SLIGHTLY different speeds

  SCOTCH TENSION (bobbin-lead):
    Drive band on bobbin; separate brake band on flyer
    Bobbin turns slightly faster than flyer -> winds yarn
    Adjust brake tension to control wind-on speed

  DOUBLE DRIVE (Irish tension):
    Drive band drives BOTH flyer and bobbin, from same wheel
    via two different whorl sizes
    Speed difference = drive ratio difference
    More responsive; traditional for fine spinning

  NORWEGIAN / SAXONY WHEEL STYLES:
    Saxony: bobbin-flyer at low angle, three legs
    Norwegian: upright, compact
    Castle: upright wheel, bobbin sits above flyer
    Ashford Traveller / Louet S10: modern production wheels

  RATIO / GEARING:
    Ratio = drive wheel circumference / whorl circumference
    Low ratio (4:1 to 8:1): thick yarn, strong twist
    High ratio (15:1 to 30:1): fine yarn, more twist per treadle
    Modern wheels: multi-ratio with swappable whorls
```

---

## Drafting Techniques

### Short Draw (Supported Draw / Inch-Worm)

```
SHORT DRAW

  Both hands hold fiber:
    Back hand: holds fiber supply
    Front hand: pinches just behind twist zone
  Draft by moving front hand forward, back hand follows
  Twist enters drafted zone behind front hand
  Maximum control of fiber density

  WORSTED SHORT DRAW:
    Both hands always maintain contact with fiber
    Fibers drafted parallel to yarn axis
    Result: smooth, dense, strong singles (worsted character)
    Used on combed top (parallel preparation)
```

### Long Draw (Free Hand)

```
LONG DRAW

  Back hand holds fiber supply
  Front hand draws back, away from orifice
  Twist allowed to travel into the drafting zone
  Twist self-regulates: thin spots twist harder (more friction) -> draft easier
                        thick spots twist less -> pulls out next
  Draft ratio: 3x to 10x staple length

  RESULT: Airy, uneven, high-loft yarn (woolen character)
  Fast technique; traditional for handspun woolen yarn
  Requires: well-prepared carded rolags, NOT worsted top
```

---

## Yarn Structure: Singles, Plied, Cable

```
YARN HIERARCHY

  SINGLES (Z-twist standard):
    Single strand from one fiber supply
    Biased: tries to untwist, problematic in fabrics

  2-PLY (S-twist on Z-twist singles):
    Two singles plied together in opposite direction
    Balanced: fibers at optimal angle to axis
    Standard for: knitting yarns, lace, sock yarn

  3-PLY (S-twist on Z-twist singles):
    Three singles: rounder cross-section than 2-ply
    Standard for: traditional Aran, some weaving yarns

  CABLE YARN (Z-twist on S-twist 2-ply):
    Two 2-ply yarns plied AGAIN in Z direction
    Four strands total; very stable, round, bouncy
    Standard for: sturdy knitting yarn

  ANDEAN PLYING (no added twist method):
    Wind singles around hand (Andean bracelet technique)
    Ply two ends from same ball: both ends move at equal rate
    Same as conventional plying without extra skein winding step

Z/S NOTATION:
  Report as: twist direction of singles / ply twist
  "Z/S" = Z-twist singles, S-twist ply (most common)
  "S/Z" = S-twist singles, Z-twist ply (reversed, less common)
  Must alternate each level for balanced construction
```

---

## Grist and Yarn Weight Standards

```
GRIST MEASUREMENT SYSTEMS (historical, mutually incompatible)

  WORSTED COUNT (Nc): yards per pound
    Nc = yarn_length_yards / (weight_pounds * 560)
    Higher number = finer yarn
    "6s worsted" = 6 * 560 = 3360 yards per pound

  WOOLEN COUNT: same as worsted but with different base unit
    Nm = meters per gram * 1000 (metric count)

  WPI (wraps per inch):
    Wind yarn closely around ruler: count wraps per inch
    Simple field measurement; not standardized across fibers

YARN WEIGHT CATEGORIES (CYC / Craft Yarn Council):
  Lace / 0:    WPI 30-40
  Fingering / 1: WPI 14-22
  Sport / 2:   WPI 12-18
  DK / 3:      WPI 11-15
  Worsted / 4: WPI 9-12
  Bulky / 5:   WPI 7-10
  Super Bulky / 6: WPI 5-7

NOTE: CYC categories are for knitting/crochet; weaving uses different systems.
Weaving yarns are specified in: yards per pound, meters per 100g, Nm count.
```

---

## Decision Cheat Sheet

| Goal | Preparation | Draft | Tool | Yarn Type |
|------|-------------|-------|------|-----------|
| Soft warm knitting | Card to rolag | Long draw | Treadle wheel | Woolen, airy |
| Smooth weaving warp | Comb to top | Short draw worsted | Treadle wheel | Worsted, strong |
| Fine lace | Comb to top | Short draw, long attenuation | High-ratio wheel | Fine worsted singles |
| Beginner practice | Card (any) | Park and draft | Drop spindle | Woolen singles |
| Very fine yarn (Merino) | Comb top | Short draw | Fine ratio wheel | Fine worsted |
| Rustic character | Torn locks | Long draw | Walking wheel | Thick-thin woolen |
| Balanced knitting yarn | Any prep | Singles + ply opposite dir | Any wheel | Balanced 2-ply |

---

## Common Confusion Points

**"Worsted" and "worsted weight" are not the same** -- Worsted spinning refers to using combed parallel fiber with a short draw worsted draft technique. "Worsted weight" is a CYC yarn thickness category (about 200-300 yards per 100g). A yarn can be woolen-spun (from carded preparation) yet be sold as "worsted weight" by thickness. Confusingly common in commercial yarn labeling.

**Plied yarn is not necessarily stronger per unit weight** -- Plying adds twist-on-twist overhead. Two 1-ply yarns of the same thickness have more fiber than one 2-ply of similar diameter. Plied yarn is more balanced and abrasion-resistant, but the raw fiber count is lower.

**You cannot long-draw from combed top** -- Long draw requires a woolen preparation where fibers are not parallel. If you try to long draw from combed top, the twist simply can't self-regulate through parallel fibers, and you get irregular thick-thin yarn or breakage. Use top for short draw.

**S-twist and Z-twist matter for weaving** -- Warp threads with too much residual bias can cause fabric to skew off-square. Traditional practice: alternate S and Z twist singles in the warp to cancel the torque. This is why Navajo weavers historically spun some yarns in each direction.
