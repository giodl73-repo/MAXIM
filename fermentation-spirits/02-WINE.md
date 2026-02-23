# Wine — Viticulture, Vinification, and Classification

## The Big Picture

```
+------------------------------------------------------------------+
|                    WINE PRODUCTION FLOW                           |
|                                                                    |
|  VINEYARD            HARVEST            WINERY                    |
|  --------            -------            ------                    |
|  Vitis vinifera      Brix/pH/TA         Crush/Destem              |
|  Terroir             decision           -> Press (white)          |
|  Annual cycle        Hand vs            -> Macerate (red)         |
|  Pruning/training    mechanical         -> Ferment                 |
|                      pick               -> MLF (optional)         |
|                                         -> Aging                  |
|                                         -> Bottle                 |
+------------------------------------------------------------------+

CRITICAL BRANCH POINT: White vs Red vs Rosé

  WHITE: Grapes -> Press -> Juice -> Ferment (no skin contact)
  RED:   Grapes -> Crush -> Ferment ON SKINS -> Press -> Age
  ROSE:  Grapes -> Short skin contact (hours) -> Press -> Ferment
  ORANGE: White grapes fermented on skins like red wine
```

---

## Viticulture

### Vitis vinifera: The Wine Grape Species

```
VITIS VINIFERA (European wine grape)
  |
  +-- Origin: Caucasus/Near East (genetic bottleneck with domestication ~6000 BCE)
  |
  +-- ~10,000 named cultivars, ~1,000-1,300 commercially significant
  |
  +-- Notable varieties:
  |     Red: Cabernet Sauvignon, Merlot, Pinot Noir, Syrah/Shiraz,
  |          Grenache, Sangiovese, Nebbiolo, Tempranillo, Zinfandel
  |     White: Chardonnay, Sauvignon Blanc, Riesling, Pinot Gris,
  |            Gewurztraminer, Chenin Blanc, Viognier, Albarino
  |
  +-- Not V. labrusca (American fox grape -- Concord; different flavor compounds)
  |    Not V. rotundifolia (Muscadine -- Southern US)
  |
  +-- Phylloxera crisis 1870s: root louse nearly destroyed all European viticulture
       Solution: graft V. vinifera scion onto American Vitis species rootstock
       (American species are phylloxera-resistant)
       Still done universally today -- virtually all wine grapes grow on grafted stock
```

### Terroir

The French concept capturing everything about where and how grapes grow:

```
TERROIR COMPONENTS

  SOIL          CLIMATE         TOPOGRAPHY      HUMAN
  -----         -------         ----------      -----
  Drainage      Temperature     Aspect (slope   Winemaker
  Mineral       Rainfall        direction)      decisions
  composition   Frost risk      Altitude        Viticulture
  pH            Sunshine hrs    Proximity to    practices
  Depth         Diurnal range   water bodies    Tradition
  Structure     Maritime/       Meso-climate    Legal AOC
                continental                     constraints
```

**Why terroir matters for flavor:**
- Calcareous (limestone) soils: poor drainage retention forces roots deep ->
  mineral character, lower yields (Champagne, Burgundy, Chablis)
- Volcanic: high mineral content, saline notes (Santorini, Sicily)
- Slate: heat retention, mineral finesse (Mosel Riesling)
- Clay: water retention, full-bodied wines (Pomerol - Petrus)
- Gravel/sand: drainage, warm roots, tannic structure (Medoc)

**Diurnal temperature range:**
Large day/night temperature swings preserve acidity while achieving ripeness.
California Central Coast, Mendoza, Mosel: hot days, cold nights.
Key for balance: ripeness (sugar) + freshness (acid).

---

## Harvest Timing

The most consequential decision in wine production.

```
HARVEST TIMING TRADE-OFFS

    BRIX (sugar)  ACIDITY (TA)  PHENOLIC RIPENESS  FLAVOR

Early harvest:    Low Brix      High acid          Underripe phenolics   Green, tart
                  (~20-22)      (tartaric/malic)   (green tannins)       Herbal, lean

Optimal window:   22-26 Brix    Moderate TA        Ripe tannins          Fruit-forward
                               (balanced)          (anthocyanins)        Balanced

Late harvest:     27+ Brix      Low acid           Over-ripe             Jammy, alcoholic
                               (flabby)            Raisinated            Pruny, hot

LATE LATE harvest: 35+ Brix    Low (may add acid)  Concentrated          Sweet, rich
(Sauternes,       (Botrytis or  tartaric            Dessert wine
ice wine)          freeze conc.)
```

**Measurement tools:**

| Measurement | What It Measures | Units | Why It Matters |
|-------------|-----------------|-------|----------------|
| Brix | Dissolved solids (mostly sugar) | Degrees Brix | Predicts final ABV: Brix / 56 x 100 = approx % ABV |
| pH | Hydrogen ion activity | pH 3.0-3.8 | Microbial stability, color, tartness perception |
| TA (titratable acidity) | Total acid concentration | g/L as tartaric | Balance, freshness, aging potential |
| Malic acid | Pre-MLF malic acid level | g/L | Determines whether MLF is needed/desired |

---

## White Wine Production

```
GRAPES -> CRUSH/DESTEM (optional; some whole-cluster pressed)
            |
            v
         PRESS
         (pneumatic bladder press or basket press)
            |
            v
         FREE-RUN JUICE (highest quality, ~70% yield)
         PRESS FRACTIONS (second, third press -- increasingly tannic/oxidized)
            |
            v
         COLD SETTLING / DEBOURBAGE (12-24 hrs at 10-15 degrees C)
         Solids drop out; turbid juice causes off-flavors in fermentation
            |
            v
         FERMENTATION (temperature-controlled, often 10-16 degrees C)
         Slow, cool = more aromatic, more ester formation
         Stainless steel: fresh, fruity, no oak character
         French oak barrel: adds vanilla/spice/tannin + micro-oxidation
            |
            v
         MLF (optional -- see below)
            |
            v
         AGING / ELEVAGE (months to years)
            |
            v
         FINING (bentonite, egg white, isinglass) -- removes particles/proteins
         FILTRATION (optional -- controversial with natural wine movement)
            |
            v
         BOTTLING
```

---

## Red Wine Production

```
GRAPES -> CRUSH/DESTEM
          (whole berry: more CO2 maceration; destemmed: cleaner tannin)
            |
            v
         COLD SOAK (optional, 24-72 hrs at 10-15 degrees C)
         Extracts color/flavor without alcohol (pre-fermentation)
            |
            v
         ALCOHOLIC FERMENTATION ON SKINS (7-21+ days, 18-32 degrees C)
            |
         CAP MANAGEMENT (CO2 lifts skins to surface -- must break cap)
         |                    |
         PUNCH-DOWN          PUMP-OVER
         (plunger through     (pump from bottom,
          cap manually)        spray over cap)
         Gentler extraction   More efficient extraction
            |
         EXTENDED MACERATION (post-ferment skin contact)
         -> More tannin extraction -> more aging potential
         -> Risk of harsh tannins if overdone
            |
            v
         PRESS (free-run + press wine; often blended later)
            |
            v
         MLF (almost universal in red wine)
            |
            v
         BARREL AGING / VAT AGING
            |
            v
         BLENDING (barrel selection, variety blending)
            |
            v
         FINING + FILTRATION
            |
            v
         BOTTLING
```

---

## Tannin and Anthocyanin Chemistry

```
PHENOLIC COMPOUNDS IN RED WINE

ANTHOCYANINS (color)               TANNINS (structure/astringency)
------------                       -------
Grape skin pigments                Proanthocyanidins (condensed tannins)
Malvidin dominant in V. vinifera   From skins, seeds, stems, oak
pH-dependent color:                Precipitate proteins in mouth
  pH 3.0 = red                     -> Astringency sensation
  pH 4.0 = violet                  Polymerize with aging ->
  pH >5.0 = blue                   softer, more complex

Young red: red/purple              Age = brown/garnet (anthocyanin
Aged red: garnet/brick/brown       oxidation + tannin polymerization)

EXTRACTION FACTORS:
  Temperature: higher = more extraction
  Alcohol: higher = more tannin extraction
  Skin contact time: longer = more everything
  Pump-over vs punch-down: different extraction profiles
```

---

## Malolactic Fermentation (MLF)

```
MALOLACTIC FERMENTATION

Bacterium: Oenococcus oeni (lactic acid bacterium)
Reaction:  Malic acid (2 carbons, 2 COOH) -> Lactic acid (1 COOH) + CO2

+-----------------------------------------------------------+
|           BEFORE MLF              AFTER MLF               |
|  Sharp, tart acidity              Softer, rounder         |
|  Higher TA                        Lower TA                |
|  High malic acid (apple-tasting)  Low malic acid          |
|  Green apple notes                Creamy, dairy notes     |
|                                   Diacetyl possible       |
|                                   (buttery if excessive)  |
+-----------------------------------------------------------+

WHEN TO USE:
  Always: Most red wines (tannin structure benefits from MLF softening)
  Often:  Chardonnay (especially barrel-fermented, richer styles)
  Rarely: Crisp whites (Sauvignon Blanc, Riesling, Pinot Grigio)
          Aromatic whites, high-acid styles where freshness is the goal

CONTROL:
  Promote: Add ML bacteria inoculum, warm cellar (20 degrees C), remove SO2
  Block: Keep cellar cold, add SO2 (bisulfite), remove bacteria by filtration
         Lysozyme enzyme addition destroys bacteria
```

---

## Oak Aging Chemistry

```
OAK BARREL CHEMISTRY

NEW OAK BARREL
     |
     +-> LACTONES (oak lactones / whisky lactones)
     |   Coconut, vanilla, sweet wood character
     |   Higher in American oak than French oak
     |
     +-> ELLAGITANNINS (hydrolyzable tannins)
     |   From oak wood; different from grape tannins
     |   Antioxidant protection; soften grape tannins
     |
     +-> VANILLIN
     |   From lignin degradation during toasting
     |   Vanilla, sweet character
     |
     +-> GUAIACOL / EUGENOL
     |   From lignin; toasty, smoky, spicy notes
     |   More pronounced with heavy toast
     |
     +-> MICRO-OXYGENATION
         Small amount of O2 diffuses through staves
         Softens tannins (polymerization)
         Stabilizes color (anthocyanin-tannin bonding)

TOASTING LEVELS (stave inside is charred):
  Light toast:  More lactones, more vanilla, subtle spice
  Medium toast: Balanced flavor integration
  Heavy toast:  More smoke, toast, coffee, less primary fruit
```

**Oak source comparison:**

| Oak Type | Grain | Lactone Content | Character | Used In |
|----------|-------|-----------------|-----------|---------|
| American (Quercus alba) | Wide | High | Coconut, vanilla, sweet | Bourbon, Rioja, some Chardonnay |
| French Limousin | Wider | Medium | Earthy, tannic | Cognac |
| French Troncais | Tight | Low | Elegant, subtle | Burgundy, Bordeaux |
| Hungarian | Medium | Medium | Spicy, floral | European wines |
| New vs neutral | N/A | New barrel = more extraction | Neutral = no new oak character | 1st use = new; 2nd-3rd = neutral |

---

## Classification Systems

### Bordeaux 1855 Classification

```
BORDEAUX CLASSIFICATION (1855, left bank)

Commissioned by Napoleon III for the Paris Exposition
Based on price/reputation at the time -- essentially unchanged since

1er Grand Cru Classe (First Growth):
  Chateau Lafite Rothschild (Pauillac)
  Chateau Margaux (Margaux)
  Chateau Latour (Pauillac)
  Chateau Haut-Brion (Graves -- only non-Medoc)
  Chateau Mouton Rothschild (added 1973 -- only change in 168 years)

2eme through 5eme Cru Classe: 57 chateaux total

LEFT BANK (Medoc, Graves):            RIGHT BANK (Pomerol, St-Emilion):
  Cabernet Sauvignon dominant           Merlot dominant
  Gravel/sand soils                     Clay soils
  Age well, tannic when young           Earlier drinking, plush
  Strict classification system          Pomerol: NO classification
                                        St-Emilion: separate classification
                                        Petrus (most expensive Bordeaux) =
                                        NOT in 1855 classification at all
```

### Burgundy Hierarchy

```
BURGUNDY GRAND CRU HIERARCHY

Most wines from most areas (village level)
     |
     | VILLAGE (commune) APPELLATION
     | e.g., "Gevrey-Chambertin" -- entire village wine
     |
     v
     | PREMIER CRU
     | Named vineyard on label: "Gevrey-Chambertin 1er Cru"
     | ~1/3 of Cote d'Or production
     |
     v
     | GRAND CRU
     | Top 33 vineyards -- the vineyard NAME is the appellation
     | "Chambertin" "Montrachet" "Corton" -- no village needed
     | ~2% of Burgundy production
```

**Burgundy vs Bordeaux philosophically:**
Burgundy: one variety (Pinot Noir for red, Chardonnay for white), tiny plots,
terroir expression is everything, producer name matters less than vineyard name.
Bordeaux: multi-variety blends, chateau system, producer brand dominates.

### Champagne: Methode Champenoise

```
CHAMPAGNE PRODUCTION

BASE WINE (still, low alcohol ~10-11% ABV, high acid, blended)
     |
     | ASSEMBLAGE (blending across villages, varieties, years for NV)
     v
TIRAGE (bottling with added sugar + yeast: "liqueur de tirage")
     |
     | SECONDARY FERMENTATION IN BOTTLE
     | Yeast + 24g/L sugar -> CO2 (dissolves under pressure: 6 atm)
     | + 1.2-1.5% additional ABV
     v
LEES AGING (dead yeast cells in bottle)
     | NV minimum 15 months; Vintage minimum 36 months
     | Autolysis: yeast cells break down -> brioche, toast, biscuit notes
     v
RIDDLING (remuage)
     | Bottles gradually tilted from horizontal to vertical, neck down
     | Sediment collects in neck
     | Mechanical gyropalette (6 hrs) replaces 6-8 weeks hand riddling
     v
DISGORGEMENT (degorgement)
     | Neck frozen in brine bath
     | Crown cap removed -> pressure ejects plug of frozen sediment
     v
DOSAGE (liqueur d'expedition: sugar + wine added)
     | Brut Nature: 0-3 g/L residual sugar
     | Extra Brut: 0-6 g/L
     | Brut: 0-12 g/L (most common)
     | Extra Dry: 12-17 g/L (paradoxically sweeter than "Brut")
     | Demi-Sec: 32-50 g/L
     v
BOTTLED (cork + wire cage)
```

---

## Special Wine Styles

### Fortified Wines

```
FORTIFICATION: adding distilled grape spirit to arrest fermentation

PORT (Douro Valley, Portugal):
  Fermentation starts -> when 1/3 sugar remains, add aguardente (~77% ABV)
  -> Yeast killed by alcohol -> residual sweetness
  -> 20% ABV
  LBV (Late Bottled Vintage), Tawny (oxidative aging), Ruby (reductive aging)
  Vintage Port: single year, 20+ year aging potential

SHERRY (Jerez, Andalucia, Spain):
  DRY fermentation first (all sugar consumed)
  Then fortified to 15-17% for Fino/Manzanilla (flor yeast protection)
  Or 17-18% for Oloroso (no flor -- oxidative)
  Solera system: fractional blending across vintages
  Fino: under flor, pale, dry, saline
  Oloroso: oxidized, dark, raisinated, nutty
  PX (Pedro Ximenez): sun-dried grapes -> very sweet dessert sherry
```

### Botrytis and Ice Wine

```
BOTRYTIS CINEREA (noble rot):
  Fungus that dehydrates grapes -> concentrates sugar, acid, glycerol
  Requires: misty mornings (humidity for spore germination)
           dry afternoons (prevents bunch rot destroying concentration)
  Result: Sauternes (Bordeaux), Tokaji (Hungary), Beerenauslese/TBA (Germany)
  Flavor: honeyed, apricot, marmalade, ginger -- distinctive "botrytis character"

ICE WINE:
  Grapes freeze ON THE VINE (Canada, Germany -- Eiswein)
  Ice crystals = water; pressed while frozen -> concentrated juice flows
  German minimum: -8 degrees C; Canadian: -8 degrees C
  Very expensive: small yield, risky, labor-intensive
```

---

## Wine Faults

| Fault | Cause | Sensory | Detection |
|-------|-------|---------|-----------|
| TCA (cork taint) | 2,4,6-trichloroanisole -- from chlorine + mold in cork | Musty, wet cardboard, suppresses fruit | Smell of cork itself and wine |
| VA (volatile acidity) | Acetobacter oxidation; excess acetic acid | Vinegar, nail polish | Strong solvent smell |
| Reduction/Sulfur | Insufficient O2; yeast stress -> H2S, mercaptans | Rotten eggs, rubber, struck match | Unpleasant sulfur |
| Oxidation | O2 exposure -> ethanol -> acetaldehyde -> acidity | Sherry-like, flat, brown | Color browning; flat aroma |
| Brettanomyces | Wild yeast contamination | Barnyard, horse, Band-Aid, leather | Distinctive once known |
| Refermentation | Residual yeast + sugar at bottling | Spritz in still wine, yeast deposits | Unexpected effervescence |
| Crystals | Tartrate precipitation (cold stabilization skip) | Harmless glass shards appearance | Visible, no taste impact |

---

## Common Confusion Points

**"Old World vs New World wine."**
Old World = Europe (France, Italy, Spain, Germany, etc.) -- emphasis on terroir and
appellation; wines labeled by place, not grape variety.
New World = Americas, Australia, South Africa, NZ -- emphasis on variety and winemaker;
usually labeled by grape variety. But these are tendencies, not rules.
Italian Barolo: labeled by place (Barolo = Nebbiolo from that region). California:
usually labeled "Cabernet Sauvignon." This reflects philosophy more than quality.

**"Tannins and sulfites cause headaches."**
Red wine headaches: most evidence points to histamines, biogenic amines, and
individual alcohol metabolism rather than tannins or sulfites.
Sulfites are higher in white wine and dried fruit than most red wine -- yet white wine
drinkers rarely complain. The "sulfite headache" claim is largely debunked.

**"Expensive wine = better wine."**
Price correlates with scarcity and brand, not reliably with sensory quality.
Professional blind tastings repeatedly show trained palates cannot consistently
distinguish $20 from $200 bottles. Parker effect: 100-point scale created enormous
price distortions in Bordeaux and California.

**"Wine improves with age."**
Only specific wines age well: high tannin reds (Barolo, Bordeaux, Burgundy Grand Cru),
high acid whites (German Riesling, white Burgundy), sweet wines.
~95% of wine produced is best consumed within 1-3 years. "Hold it" advice applies
to a tiny fraction of production.

---

## Decision Cheat Sheet

| I want to... | Wine style | Key region |
|---|---|---|
| Red with maximum aging potential | Tannic, high acid | Barolo (Nebbiolo), Bordeaux, Burgundy Grand Cru |
| Red, early drinking, plush | Low tannin, ripe | Beaujolais Nouveau, Pinot Noir (Oregon), Merlot |
| White, crisp/mineral/aromatic | High acid, no oak | Chablis, Mosel Riesling, Muscadet, Sancerre |
| White, rich/oaky/buttery | MLF + oak | White Burgundy, California Chardonnay |
| Sparkling, traditional method | Champagne-style | Champagne, Cava, Cremant, TasmanianSparkling |
| Sweet/dessert | Botrytis or freeze | Sauternes, Eiswein, Tokaji Aszu |
| Fortified, dry | Sherry | Fino Manzanilla (Sanlucar), Amontillado |
| Fortified, sweet | Port | LBV Port, Vintage Port, Tawny 10/20yr |
| Understand classification | Bordeaux | 1855 Classification + St-Emilion + Pomerol |
| Understand terroir theory | Burgundy | Cote d'Or commune/premier cru/grand cru hierarchy |
