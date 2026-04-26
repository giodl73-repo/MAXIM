# Distillation — Physics, Equipment, and Cuts

## The Big Picture

```
+------------------------------------------------------------------+
|                  DISTILLATION OVERVIEW                           |
|                                                                  |
|  INPUT: Fermented liquid (~5-15% ABV)                            |
|  OUTPUT: Concentrated spirit (15-95% ABV)                        |
|  MECHANISM: Exploit different boiling points of mixture          |
|                                                                  |
|  POT STILL                        COLUMN STILL                   |
|  (batch distillation)             (continuous distillation)      |
|  ----------------                 --------------------------     |
|  One charge at a time             Continuous input/output        |
|  Simple or compound               Theoretical plates             |
|  Retains congeners                Strips congeners               |
|  Lower ABV (<70%)                 Higher ABV (up to 96%)         |
|  More flavor                      More neutral                   |
|  Scotch, Cognac, Irish pot        Vodka, grain neutral, column   |
|                                   Scotch grain, rum              |
+------------------------------------------------------------------+
```

---

## Vapor-Liquid Equilibrium (VLE)

The physics that makes distillation work.

### Raoult's Law

For an ideal mixture of two components A and B:

```
P_total = x_A * P_A^sat + x_B * P_B^sat

Where:
  x_A, x_B = mole fractions in liquid phase
  P_A^sat, P_B^sat = vapor pressures of pure components at that temp
```

For ethanol-water:
- Ethanol BP = 78.37 degrees C (760 mmHg)
- Water BP = 100 degrees C (760 mmHg)
- Ethanol vapor pressure >> water at any given temperature
- -> Vapor enriched in ethanol relative to liquid

**Relative volatility (alpha):**
```
alpha = (y_A / x_A) / (y_B / x_B)

alpha >> 1: A much more volatile than B -> easy separation
alpha = 1: inseparable (azeotrope or same volatility)
```

For ethanol-water: alpha ~2-3 at most concentrations, but drops toward 1 near 95.6% ABV.

---

## The Ethanol-Water Azeotrope

The fundamental physical limit of simple distillation.

```
ETHANOL-WATER PHASE DIAGRAM

100 |             .-'''''-.
    |           .'         '.
    |          /     VAPOR   '.
    |    BP   /               '.
    | 78.37 degC               '.
    |    /   /                  '.  *AZEOTROPE*
    |   /   /                    '* 95.6% ABV, 78.15 degC
    |  /   /  LIQUID + VAPOR      |
    | /                           |
  78|_____________________________|
    0%   20%   40%   60%   80% 95.6%  100%
                    Ethanol ABV

The liquid and vapor curves meet at 95.6% ABV (78.15 degrees C)
-> At this point, vapor composition = liquid composition
-> Boiling the mixture does not change composition
-> Cannot exceed 95.6% ABV (189.1 proof) by simple distillation
```

**How to get above 95.6% ABV:**
- Molecular sieves (zeolite absorbents selectively remove water)
- Azeotropic distillation (add benzene or cyclohexane -- toxic entrainers)
- Pressure-swing distillation (change pressure, shifts azeotrope)

Pharmaceutical-grade and fuel-grade absolute ethanol (>99.9%) uses molecular sieves.
No spirits producer needs to exceed the azeotrope -- the goal is flavor, not purity.

---

## Pot Still: Batch Distillation

```
POT STILL ANATOMY

     CONDENSER
     (coil in cold water)
          ^
          |
     LYNE ARM
     (pipe carrying vapor)
          ^
          |
     SWAN NECK
     (curved pipe; angle determines reflux)
          ^
          |
     STILL HEAD / HELMET
     (collects vapors above liquid)
          ^
          |
     POT (kettle)
     (charge of low-wine or wash)
          |
     HEAT SOURCE
     (fire, steam coil, electric)
```

**Reflux: the key concept.**
As vapor rises up the neck and lyne arm, heavier components condense and fall back.
This condensate refluxes back into the pot, effectively providing additional
separation stages. More reflux = more separation = lighter, cleaner spirit.

```
STILL SHAPE -> REFLUX -> CHARACTER

Tall, narrow neck:  Much reflux (vapor must travel far, heavier fractions fall back)
                    -> Lighter, more delicate spirit

Short, fat neck:    Little reflux
                    -> Heavier, more robust spirit (more congeners)

Upward lyne arm:    Forces vapor to rise -> more reflux
Downward lyne arm:  Easy vapor path -> less reflux, heavier spirit
Boil ball/lantern:  Extra reflux zone in neck

EXAMPLE:
  Glenmorangie: tallest stills in Scotland (~5.14m)
  -> Very light, delicate spirit
  Balvenie, Glenfarclas: shorter, pot-bellied stills
  -> More robust, oily spirit
```

### Pot Still Run: Heads, Hearts, Tails

```
DISTILLATION CUT PROFILE (time/temperature vs composition)

              HEADS        HEARTS        TAILS
              -----        ------        -----
Time:         First 5-15%  Middle 60-70% Last 20-30% of run
Temp at       <78 degrees  78-82 degrees >82 degrees
lyne arm:
ABV:          High (~80%+) Medium        Falling
Compounds:    Acetaldehyde Ethanol +     Fusel oils
              Ethyl acetate desirable    (propanol,
              Methanol     congeners     isoamyl alcohol)
              (low levels)               Fatty acids
Aroma:        Solvent,     Target spirit  Oily, meaty,
              harsh, sharp  character     rancid, heavy
              green

Decision:     Discard      KEEP          Discard
              (or add to
               next run)
```

**How distillers make cuts:**
1. Temperature: thermometer at lyne arm -- watch transition points
2. ABV: hydrometer reading at spirit safe
3. Smell: direct sensory at spirit safe; experience-based
4. Time/volume: established protocols per still

"Feints" = combined heads + tails = added back to next charge for redistillation.

---

## Column Still: Continuous Distillation

```
COLUMN STILL (Patent Still / Coffey Still / Continuous Still)

              VAPOR OUT (to condenser)
                   ^
                   |
         +----+---------+----+
         |    |         |    |
         | RECTIFIER  COLUMN  | <- continuous rectification
         |    |         |    |
         | PLATES (bubblecap, sieve, valve)
         |    |         |    |    Each plate = theoretical stage of separation
         |    |         |    |    Vapor rises, liquid falls
         |    |         |    |    Vapor enriches as it rises
         +----+---------+----+
                   |
              BEER/WINE FEED (pre-heated, enters partway up)
                   |
         +----+---------+----+
         |    |         |    |
         |      STRIPPER      | <- strips ethanol from liquid
         |    |         |    |
         +----+---------+----+
                   |
              STILLAGE OUT (spent liquid, mostly water + dissolved solids)
                   |
              HEAT INPUT (steam)
```

**Theoretical plates:**
Each plate achieves one equilibrium stage of vapor-liquid separation.
More plates = more stages = higher separation = higher purity at top.
- Simple pot still: ~1-2 theoretical stages
- Coffey still: 20-30+ stages
- Industrial vodka column: 50-100+ stages

**HETP (Height Equivalent to a Theoretical Plate):**
For packed columns (random packing vs plates), HETP describes the bed height
required to achieve one equilibrium stage. Lower HETP = more efficient packing.

**McCabe-Thiele diagram:**
Graphical method for binary distillation design:
- Y-axis: vapor composition (y)
- X-axis: liquid composition (x)
- Equilibrium curve: VLE relationship
- Operating line: material balance (slope = L/V, liquid/vapor ratio)
- Staircase: each step = one theoretical plate
- Count steps between feed and top = plates required for desired separation

---

## Proof and ABV Measurement

```
ABV vs PROOF (historical and modern):

  US PROOF = 2 x ABV %
  100 proof = 50% ABV
  80 proof = 40% ABV (minimum for most labeled spirits in US)
  151 proof = 75.5% ABV

  Historical origin:
  British "gunpowder test": mix spirit with black powder, ignite.
  If powder ignites: spirit is "proven" = ~57.15% ABV
  -> 100 British proof = 57.15% ABV (Sikes hydrometer system)
  Modern British/EU: switched to ABV, abandoned proof

  US system (Sykes/Treasury standard):
  100 proof defined as 50% ABV by volume at 60 degrees F
  Used commercially until today on US labels
```

**ABV measurement methods:**

| Method | Principle | Precision | Use |
|--------|-----------|-----------|-----|
| Hydrometer + temperature | Density of water-ethanol mixture | +/- 0.1-0.5% | On-site, distillery |
| Pycnometer | Precise density measurement | +/- 0.01% | Laboratory |
| Digital density meter (Anton Paar) | Oscillating U-tube density | +/- 0.01% | Modern lab/distillery |
| Ebulliometer | Boiling point depression | +/- 0.1% | Field use |
| Gas chromatography | Direct ethanol quantification | +/- 0.01% | Regulatory/TTB |

---

## Congener Management in Distillation

```
CONGENER BEHAVIOR BY STILL TYPE

            POT STILL              COLUMN STILL
            (pot still whisky)     (grain neutral spirit)
            ----------             -------------------
Method      Batch                  Continuous
Plates      1-2 theoretical        30-100+ theoretical
ABV out     60-72% typical         92-96% typical
Esters      Retained               Stripped
Fusel oils  Partially retained     Mostly stripped
Aldehydes   Heads fraction cut     Mostly stripped
Fatty acids Tails fraction cut     Stripped
Character   Rich, complex          Clean, neutral
Examples    Malt Scotch, Cognac    Vodka, grain whisky

COLUMN CUTS: Even in column distillation, fusel oils concentrate
  at a specific point in the column (a side-stream).
  Industrial fuel ethanol sometimes draws off the "fusel oil fraction"
  as a byproduct (used in solvents/flavors).
```

---

## Copper and Spirit Quality

```
WHY COPPER STILLS MATTER

Fermentation produces sulfur compounds (H2S, DMS, thiols):
  - Yeast stress -> H2S production
  - Amino acid degradation -> various thiols

COPPER + H2S -> Copper sulfide (CuS, solid)
                Deposits on still surface
                -> Removes sulfur from spirit vapor

RESULT: Copper contact time -> sulfur reduction -> cleaner spirit

This is why:
  - Pot stills are copper (not stainless)
  - Copper packing/mesh used in column stills
  - Lyne arm and condenser are copper
  - Used copper stills must be regularly "polished" (reactivated)
  - Stainless stills require added copper contact elsewhere

Worm tubs (coil condenser in cold water tank):
  Traditional condensers; slower cooling -> more copper contact -> cleaner spirit
  Replaced by shell-and-tube heat exchangers -> faster, less copper contact -> heavier spirit
  Some distilleries (Craigellachie, Dalwhinnie) intentionally use worm tubs for character.
```

---

## Distillery Economics and Maturation

```
ANGEL'S SHARE:
  Ethanol evaporates from barrel during aging
  Rate: ~2% per year in Scotland/Ireland (cold, humid)
          ~4% per year in Kentucky (hot, humid summers)
          ~8-10% per year in tropical climates (Caribbean rum)
  -> 10-year Scotch: ~18% of original spirit is gone
  -> 30-year Scotch: ~46% of original spirit is gone
  -> Price premium for aged spirits partly reflects angel's share loss

YIELD CALCULATIONS:
  Brewing/fermentation efficiency:
    Grain in (kg) x extract (kg sugar/kg grain) -> fermentable extract
    Fermentable extract x yeast attenuation -> ethanol produced
  Distillation yield:
    Low wines ABV x volume -> LPA (liters of pure alcohol)
    Spirit ABV x volume -> LPA collected
    Yield = spirit LPA / potential LPA from grain

WATER ACTIVITY:
  Spirits diluted to barrel entry strength: bourbon max 62.5% ABV, Scotch varies
  Dilution water quality matters: mineral content affects flavor integration
  Chill filtration: cooling + filter to remove fatty acid esters that cloud when cold
  -> Removes some flavor compounds; controversial
  -> Non-chill filtered: increasingly common for premium products
```

---

## Legal Definitions by Category

| Spirit | Legal ABV | Distillation Limit | Other Requirements |
|--------|-----------|-------------------|-------------------|
| Scotch single malt | Min 40% bottled | Max 94.8% distillation | Pot still; malted barley; oak; Scotland; 3yr min |
| Bourbon | Min 40% (80 proof) | Max 80% (160 proof) | 51%+ corn; new charred oak; USA |
| Cognac | Min 40% | Charentais pot still | Charente/Charente-Maritime; Ugni Blanc; Limousin/Tronc oak |
| Vodka | EU: Min 37.5%; US: Min 40% (80 proof) | No limit | Neutral grain/potato spirit; no distinctive character |
| Gin | EU: Min 37.5%; US: Min 40% | No limit | Juniper must dominate botanical flavor |
| Rum | US: No legal definition beyond "sugar cane" | No limit | Varies wildly by country |
| Armagnac | Min 40% | Continuous column (alembic armagnacais) | Gascony; Ugni Blanc/Baco/Folle Blanche/Colombard |

---

## Common Confusion Points

**"You can make vodka at home by distilling cheap wine."**
In most countries, home distillation is illegal regardless of the input.
In the US, it's a federal felony without a DSP (Distilled Spirits Plant) license.
This is a regulatory issue, not a physics issue.

**"The azeotrope is why spirits have a maximum ABV."**
Partially true but misdirected. The azeotrope is a physical limit at 95.6% ABV.
Legal spirits cap out well below this (bourbon max 80%, Scotch max 94.8%).
These legal limits are flavor decisions, not physical limits.

**"Pot stills are primitive; column stills are better."**
False. They produce different products for different purposes. Column stills
produce neutral spirit efficiently. Pot stills retain congeners intentionally.
Blended Scotch uses both: malt from pot stills + grain from column stills.

**"Heads contain dangerous methanol."**
Small amounts of methanol are present but not hazardous in commercial volumes.
The danger from bootleg spirits is deliberate methanol adulteration, not the
small amount from fermentation. A professional distiller's heads cut removes
other off-flavor compounds (acetaldehyde, ethyl acetate) primarily -- not
methanol specifically.

**"Higher proof = stronger flavor."**
Inversely related for spirits: higher ABV extraction during distillation =
more neutral. Lower ABV distillation (pot still, lower proof) = more congeners =
more flavor. Premium aged spirits are typically bottled at 43-46% ABV, not higher,
for optimal flavor expression with water dilution.

---

## Decision Cheat Sheet

| I want... | Still type | ABV target | Character |
|---|---|---|---|
| Maximum neutral spirit | Multi-column | 94-96% | Vodka base; no character |
| Whisky/brandy character | Pot still | 60-72% | Rich, congener-forward |
| Blended whisky efficiency | Coffey still (column) | 85-94% | Lighter grain whisky |
| Irish pot still character | Large copper pot | 65-72% | Triple distillation; clean, light |
| Maximum Jamaican ester | Pot + dunder + muck | 65-70% | Heavy ester rum |
| Understand the cuts | Pot still run | N/A | Temperature monitoring + sensory |
