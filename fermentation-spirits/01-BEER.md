# Beer — From Grain to Glass

## The Big Picture

```
+------------------------------------------------------------------+
|                    BEER PRODUCTION FLOW                          |
|                                                                  |
|  MALTHOUSE              BREWHOUSE              FERMENTATION      |
|  ---------              ---------              -----------       |
|  Barley                 Mash Tun               Fermentation Vessel |
|  -> Steep               (mashing)              (7-14 days)       |
|  -> Germinate           -> Lauter Tun           -> Conditioning  |
|  -> Kiln                (lautering)             -> Packaging     |
|  MALT                   -> Kettle               -> BEER          |
|                         (boiling + hops)                         |
+------------------------------------------------------------------+

KEY INPUTS AT EACH STAGE:
  Malthouse: Water, temperature, time
  Mash Tun: Hot water (strike water), enzyme activity, temperature rests
  Kettle: Hops (bittering + aroma), heat (Maillard, DMS volatilization)
  Fermenter: Yeast strain, temperature, oxygen (initially)
```

---

## Stage 1: Malting

Malting converts raw barley into a stable enzyme-rich substrate for mashing.

```
RAW BARLEY
     |
     | STEEP (48-72 hrs, 12-18 degrees C)
     | Water absorption to ~42-45% moisture
     | Activates gibberellin -> aleurone layer activation
     v
GERMINATING BARLEY (3-6 days at 15-20 degrees C)
     |
     | ACROSPIRE grows to 3/4 grain length
     | Enzymes synthesized:
     |   alpha-amylase    -> cleaves starch internally (dextrins)
     |   beta-amylase     -> cleaves from starch ends (maltose)
     |   proteases        -> modify proteins (head retention, clarity)
     |   beta-glucanase   -> breaks gummy beta-glucans
     |   limit dextrinase -> debranches starch
     v
KILNING (50-105+ degrees C, 24-48 hrs)
     |
     | Dries grain to <5% moisture (stable for storage)
     | Temperature determines malt character
     v
MALT (enzymes preserved or destroyed depending on kiln temp)
```

**Kiln temperature determines malt type:**

| Malt Type | Kiln Temp | Color (SRM) | Enzymes | Flavor | Use |
|-----------|-----------|-------------|---------|--------|-----|
| Pale malt | 65-85 degrees C | 1.5-3 | Full enzymatic power | Biscuit, grain | Base malt; provides enzymes |
| Vienna | 90 degrees C | 3-4 | Substantial | Light toast | Lager character |
| Munich | 100-105 degrees C | 6-9 | Some | Malty, bread | Dark lager, Märzen |
| Crystal/Caramel | Wet-kilned 65 degrees C + 150 degrees C | 10-120 | None | Sweet, caramel, toffee | Body, color, sweetness |
| Chocolate | 200 degrees C | 350-450 | None | Coffee, chocolate | Stout, porter |
| Black/Roasted | 220-230 degrees C | 500-600 | None | Roast, ash | Dry stout (Guinness character) |

**Crystal malt mechanism (different from regular kilning):**
Wet germinated grain is put directly into a hot kiln (stewing). Internal enzymes
convert starch to sugar while grain is still moist, then high heat caramelizes those
sugars in situ. Result: glassy, crystallized sugar interior. Not enzymatically active
but adds fermentable + unfermentable sugars and sweetness.

---

## Stage 2: Mashing

Mashing extracts fermentable sugars by activating enzymes in hot water.

```
MASH TUN (infusion or decoction)

Strike water at target temperature -> add crushed malt -> stabilizes at mash temp
                                                          (grist ratio ~3-4 L/kg)

TEMPERATURE RESTS (enzyme activity windows):

  40-45 degrees C    beta-glucanase rest
  |                  Breaks beta-glucans -> reduces viscosity
  |                  5-20 min (skip in most modern malts)
  |
  50-55 degrees C    Protein rest
  |                  Proteases digest proteins
  |                  -> foam-positive fraction (FAN for yeast nutrition)
  |                  -> skip in modern well-modified malts
  |
  62-65 degrees C    beta-amylase optimum
  |                  Cleaves maltose from starch chain ends
  |                  -> highly fermentable wort (dry beer)
  |                  Denatures ~75 degrees C
  |
  68-72 degrees C    alpha-amylase optimum
  |                  Random internal cleavage -> dextrins + shorter chains
  |                  -> fuller body, less fermentable (sweet beer)
  |                  Stable to ~80 degrees C
  |
  77 degrees C       Mash out
                     Denatures all enzymes, locks in fermentability profile
                     Reduces viscosity for lautering
```

**Single infusion vs step mashing:**
- Single infusion at 65-68 degrees C: most modern well-modified malts only need this
- Step mashing: for undermodified malts, adjuncts requiring gelatinization, or specific profiles
- Decoction: German/Bohemian traditional -- pull portion of mash, boil it, return
  -> Maillard reactions in mash itself -> melanoidins -> flavor complexity

**Starch gelatinization:**
Starch must gelatinize (swell and dissolve in hot water) before amylases can act.
Barley starch: 61-65 degrees C. Corn: 65-75 degrees C. Rice: 68-78 degrees C.
Unmalted adjuncts (corn grits, rice) require separate cereal cooker to gelatinize
before adding to mash -- otherwise just float through.

---

## Stage 3: Lautering

Separating sweet wort from spent grain.

```
LAUTER TUN (false bottom or manifold)

  Mash -> Vorlauf (recirculate until wort runs clear)
       -> First runnings (concentrated wort)
       -> Sparge (hot water rinse, 75-78 degrees C)
          rinse sugars from grain bed
       -> Collect to pre-boil volume

STUCK SPARGE: grain bed compacts -> flow stops
  Causes: too-fine crush, too much protein, high adjunct content
  Fix: stir, raise bed, reduce sparge rate

Pre-boil specific gravity measured here (hydrometer or refractometer)
Brewers calculate extract efficiency (typically 70-80% homebrew, 85-95% commercial)
```

---

## Stage 4: Boiling

The boil achieves multiple objectives simultaneously.

```
KETTLE BOIL (60-90 min, rolling boil)

1. STERILIZATION
   Kills bacteria from mashing process
   -> Wort is not sterile until post-boil

2. DMS VOLATILIZATION
   DMS = Dimethyl sulfide (cooked corn/vegetables)
   SMM (S-methylmethionine) in malt -> DMS when heated
   Vigorous boil with open kettle vents DMS
   -> NEVER cover kettle during boil (DMS redissolves)

3. MAILLARD REACTION
   Reducing sugars + amino acids + heat
   -> Melanoidins -> color, flavor complexity
   -> Not caramelization (sugars alone) -- it's Maillard
   -> Darker wort, slight toast notes

4. PROTEIN COAGULATION (Hot break)
   Proteins + polyphenols aggregate -> cold/hot trub
   -> Clearer wort, longer shelf life

5. HOP ISOMERIZATION (see Hop Chemistry section)
```

---

## Hop Chemistry

```
HOP (Humulus lupulus) CHEMISTRY OVERVIEW

+------------------+------------------+------------------+
|   ALPHA-ACIDS    |   BETA-ACIDS     |  ESSENTIAL OILS  |
|   (bittering)    |   (antimicrobial)|  (aroma)         |
|                  |                  |                  |
| Humulone         | Lupulone         | Myrcene          |
| Cohumulone       | (not isomerized, | (pungent, earthy)|
| Adhumulone       |  contributes     | Linalool         |
|                  |  to foam and     | (floral)         |
| ISOMERIZED by    |  antimicrobial   | Geraniol         |
| boiling:         |  properties)     | (rose, floral)   |
| -> iso-alpha-    |                  | Beta-caryophyllene|
|    acids         |                  | (spicy, woody)   |
| -> BITTERNESS    |                  |                  |
+------------------+------------------+------------------+

IBU FORMULA (simplified):
  IBUs = (oz_hops x %AAU x utilization%) / gallons_wort x 74.89

Utilization depends on:
  - Boil time: 60 min = ~30%; 15 min = ~15%; 5 min = ~5%
  - Wort gravity: higher gravity = lower utilization
  - Form: pellets vs whole hops
```

**Dry hopping:**
Adding hops post-boil (during/after fermentation) adds aroma without bitterness.
Hop oils do not isomerize at room temperature -- you get aroma compounds, not IBUs.
Temperature affects which compounds extract: biotransformation by yeast can convert
hop glycosides -> aromatic alcohols (e.g., geraniol -> citranellol).

**SRM Color Scale:**

| SRM | Color | Style Examples |
|-----|-------|----------------|
| 1-3 | Pale straw | Light lager, American adjunct |
| 3-6 | Gold | Pilsner, American Pale Ale |
| 6-9 | Amber | Vienna lager, Kolsch |
| 9-14 | Copper | Amber ale, ESB |
| 14-18 | Brown | Brown ale, Märzen |
| 18-25 | Dark brown | Dunkel, porter |
| 25-35 | Very dark | Stout, black IPA |
| 35+ | Black opaque | Imperial stout, schwarzbier |

---

## Stage 5: Fermentation

```
YEAST LIFECYCLE IN FERMENTATION

Pitch yeast (active, healthy)
     |
     | LAG PHASE (1-12 hrs)
     | Yeast adapts, takes up oxygen, synthesizes sterols
     | -> AERATE wort before pitching (or oxygenate with O2)
     | -> Sterols required for healthy cell membrane at fermentation temps
     v
EXPONENTIAL GROWTH (12-36 hrs)
     |
     | Rapid cell division
     | Glycolysis active
     | High ester production (ester synthase + ethanol + organic acids)
     | -> Temperature control critical here for flavor development
     v
STATIONARY/ATTENUATION PHASE (3-10 days)
     |
     | Sugars depleted in order: glucose -> fructose -> maltose -> maltotriose
     | Alcohol accumulates
     | Diacetyl produced (acetolactate -> diacetyl via oxidation)
     | -> Yeast reabsorbs diacetyl (reduce by VDK rest at end)
     v
FLOCCULATION (yeast drops out or rises)
     |
     | S. cerevisiae (ale): top-flocculant, 15-24 degrees C
     | S. pastorianus (lager): bottom-flocculant, 4-12 degrees C
     v
CONDITIONING (lagering/dry conditioning)
     |
     | Cold conditioning (lagering): 0-4 degrees C, 3-6+ weeks
     | -> Flavor smooths, CO2 absorbs, haze proteins precipitate
     v
BEER (packaged: kegged, bottled, canned)
```

---

## Ale vs Lager: The Definitive Comparison

```
                    ALE                         LAGER
                    ---                         -----
Yeast           S. cerevisiae               S. pastorianus
                (top-fermenting)            (bottom-fermenting)
                                            Hybrid: S. cerevisiae x
                                            S. eubayanus
Temp            15-24 degrees C             4-12 degrees C
Ferment time    3-7 days primary            7-14 days primary
                3-7 days conditioning       3-6 weeks lagering
Character       Fruity (esters from         Clean (fewer esters)
                higher temps)               Crisp, malt-forward
                Complex, varied             Consistent, round
History         Older global tradition      Invented Bavaria ~1400s
                (all pre-lager beer)        Mass production 1800s+
Volume          ~30% of world beer          ~70% of world beer
                (but massive variety)       (industrial lagers dominate)
Examples        IPA, stout, porter,         Pilsner, Helles, Märzen,
                Belgian ales, wheat         Bock, Dunkel, Schwarzbier
```

---

## Beer Style Taxonomy

```
+------------------------------------------------------------------+
|                    BEER STYLE TREE                               |
|                                                                  |
|  LAGER                          ALE                              |
|  -----                          ---                              |
|  Pale                           British                          |
|  +-Pilsner (Czech/German)       +-Pale Ale / Bitter              |
|  +-Helles (Munich)              +-IPA (English)                  |
|  +-Kolsch (top-fermented lager) +-Porter / Stout                 |
|  +-American Light               +-Barleywine                     |
|                                                                  |
|  Amber/Dark                     American                         |
|  +-Vienna                       +-American Pale Ale              |
|  +-Märzen/Oktoberfest            +-American IPA (West Coast)     |
|  +-Dunkel                       +-Double/Imperial IPA            |
|  +-Schwarzbier                  +-New England/Hazy IPA           |
|                                 +-American Stout                 |
|  Strong                                                          |
|  +-Bock                         Belgian                          |
|  +-Doppelbock                   +-Witbier (wheat, coriander)     |
|  +-Eisbock                      +-Saison (rustic, farmhouse)     |
|                                 +-Tripel / Dubbel / Quad         |
|  German Wheat                   +-Lambic / Gueuze (spontaneous)  |
|  +-Hefeweizen (S. cerevisiae    +-Krieken (cherry lambic)        |
|    with Weizen character)                                        |
|  +-Dunkelweizen                 Sour/Wild                        |
|  +-Weizenbock                   +-Berliner Weisse (Lactobacillus) |
|                                 +-Gose (salt + coriander)        |
|                                 +-Flanders Red (Roeselare blend) |
+------------------------------------------------------------------+
```

---

## The Reinheitsgebot and Its Legacy

**German Purity Law of 1516:**
Duke Wilhelm IV of Bavaria: only water, barley malt, and hops permitted in beer.
(Yeast not yet known -- it was assumed to appear naturally.)

```
ORIGINAL (1516)          MODERN INTERPRETATION     EFFECT
--------------------     --------------------     ------
Water                    Water                    Innovation
Barley malt              Any malt (wheat          suppressed:
Hops                     permitted for            - No fruit
(implicit yeast)         weizenbier)              - No spices
                         Yeast                    - No adjuncts
                                                  - No sugar
                         Germany: still largely
                         followed by tradition
                         EU: no legal force
                         outside Germany
```

The Reinheitsgebot blocked Belgian-style ales, spiced beers, and creative adjuncts
within German brewing tradition for centuries. Paradoxically, it also prevented
low-quality adulteration (toxic bittering agents were common elsewhere).

---

## Craft Beer Renaissance

```
TIMELINE

1959  Anchor Brewing near-closes (San Francisco)
1965  Fritz Maytag buys Anchor, saves it, begins quality focus
1971  CAMRA founded (UK, Campaign for Real Ale) -- reaction to big brewery
1977  New Albion Brewing -- first modern US microbrewery
1978  US homebrewing legalized (Carter signs HR 1337)
      -> Amateur experimentation explodes
1980s Sierra Nevada Pale Ale (1980) -- defines American Pale Ale style
      Boston Beer Company / Samuel Adams (1984)
      Cascade hop becomes signature of American craft
1990s Belgian styles rediscovered; extreme beer begins
      (Dogfish Head, Rogue, Stone Brewing)
2000s Craft brewery count: 1,000 -> 3,000+ in USA
2010s Hazy/New England IPA dominates (Heady Topper 2011 as inflection)
      Craft sour/wild ales (Cantillon influence)
2020s Hard seltzer, non-alcoholic beer (Athletic Brewing)
      10,000+ US craft breweries
      Major acquisitions: ABInBev buys Goose Island, Wicked Weed, etc.
```

---

## Fermentation Defects and Off-Flavors

| Off-Flavor | Cause | Sensory | Remedy |
|-----------|-------|---------|--------|
| Diacetyl | Acetolactate not reabsorbed | Butter, butterscotch | Diacetyl rest (raise temp 3 days end of ferment) |
| Acetaldehyde | Insufficient fermentation | Green apple, solvent | Allow fermentation to complete |
| DMS | SMM not volatilized; covered kettle | Cooked corn, vegetables | Vigorous open boil; rapid chilling |
| Sour/acetic | Acetobacter contamination (O2 + bacteria) | Vinegar | Sanitation; minimize O2 exposure |
| Phenolic | Wild yeast (Brettanomyces), chlorophenols | Band-aid, medicinal, barnyard | Sanitation; use unchlorinated water |
| Lightstruck | UV + iso-alpha-acids -> 3-MBT | Skunk | Brown/green glass, cans, avoid light |
| Oxidized | O2 exposure post-fermentation | Cardboard, sherry, flat | Minimize O2 pickup; proper purging |
| Astringent | Over-sparging, tannin extraction | Dry, puckering | Sparge temp <77 degrees C; pH control |
| Fusel hot | High-temp fermentation, underpitching | Rubbing alcohol, hot | Temperature control; proper pitch rate |

---

## Numbers Reference

| Parameter | Measurement | Typical Range |
|-----------|-------------|---------------|
| Original Gravity (OG) | Specific gravity | 1.030-1.120 (normal to imperial) |
| Final Gravity (FG) | After fermentation | 1.006-1.020 |
| Attenuation | (OG-FG)/(OG-1) x 100% | 70-85% apparent |
| ABV | (OG-FG) x 131.25 | 3-14% typical |
| IBUs | Isomerized alpha acids | 5-120+ (typical 15-80) |
| SRM | Color (spectrophotometric) | 1-50+ |
| pH (mash) | Hydrogen ion concentration | 5.2-5.4 optimal |
| pH (wort/beer) | | 4.0-4.5 finished |

---

## Common Confusion Points

**"Ales are warm-fermented and dark; lagers are cold-fermented and light."**
Temperature distinction is correct. Color is not. Many ales are pale (Kolsch,
Hefeweizen, Belgian Witbier). Many lagers are dark (Dunkel, Schwarzbier, Bock).
Style and yeast type are orthogonal to color.

**"Craft beer = IPAs."**
IPA dominates US craft sales (~25-30%) but craft encompasses hundreds of styles.
The BJCP Style Guide has 100+ categories. IPA's dominance is commercial, not
a categorical definition.

**"More hops = better beer."**
IBUs above ~70-80 are mostly imperceptible beyond a certain bitterness plateau.
Balance matters. A 120 IBU beer tastes similar to an 80 IBU beer to most palates.
The hop aroma revolution (NEIPA, dry-hopping) is about flavor, not bitterness.

**"Reinheitsgebot = high quality."**
It prevented adulteration but also prevented innovation. Belgian ales -- widely
considered among the world's finest -- would be illegal under strict Reinheitsgebot
interpretation (sugar additions, spices, various yeasts).

---

## Decision Cheat Sheet

| I want to... | Key parameter |
|---|---|
| Make beer drier/more fermentable | Mash at 62-65 degrees C (beta-amylase favored) |
| Make beer fuller/sweeter | Mash at 68-72 degrees C (alpha-amylase favored) |
| Add color without bitterness | Crystal/caramel malts (no enzymatic activity needed) |
| Add bitterness | Early hop additions (60 min boil = max isomerization) |
| Add hop aroma without bitterness | Late additions (flameout, whirlpool, dry-hop) |
| Brew a lager | S. pastorianus, 4-12 degrees C, 3-6 week cold condition |
| Brew a clean ale | S. cerevisiae, 16-18 degrees C (low end), temp control |
| Brew a fruity/Belgian ale | Higher temp, specific Belgian yeast strains (15-25 degrees C) |
| Understand a style | BJCP Style Guide -- the definitive reference |
