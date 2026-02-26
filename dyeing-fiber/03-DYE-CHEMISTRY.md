# Dye Chemistry: Chromophores, Auxochromes, Fiber-Dye Bonding, Fastness

## The Big Picture

Color in dyes is quantum mechanical: the molecule absorbs photons at specific wavelengths because the energy gap between molecular orbital levels matches the photon energy. The part of the molecule doing this is the chromophore (the pi-conjugated system). Auxochromic groups modify the absorption wavelength and provide bonding sites. The bond between dye and fiber determines fastness.

```
DYE MOLECULE ANATOMY

   AUXOCHROME         CHROMOPHORE              AUXOCHROME
   (bonding site +    (pi system that          (bonding + color
    color modifier)    absorbs visible light)   modifier)
        |              |              |              |
        v              v              v              v
    -OH group    ====C=C-C=C-C=C===  chromophore    -NH2 group
    (hydroxyl)   conjugated pi bonds                (amine)

  COLOR RULE: Longer conjugated pi system -> longer wavelength absorbed
    -> complementary color shifts toward red (bathochromic shift)

  COMPLEMENTARY COLORS:
    Absorbs: blue (420-490nm)  -> Appears: orange/red
    Absorbs: green (490-560nm) -> Appears: purple/red
    Absorbs: red (620-700nm)   -> Appears: green
    Absorbs: orange (590-620nm) -> Appears: blue
```

---

## Chromophore Theory: The Witt Model (1876, updated)

Otto Witt first proposed that color in organic compounds requires two structural features: a chromophore (color-bearing group) and an auxochrome (color-intensifying group). This has been substantially refined by quantum mechanics but the categories remain useful:

### Primary Chromophore Groups

```
CHROMOPHORE   STRUCTURE            EXAMPLE DYES
-----------   ---------            -------------
Azo           -N=N-                Azobenzene dyes (largest synthetic class)
                                   Congo Red, Direct Red 80, Disperse Orange 3

Carbonyl      >C=O                 Anthraquinone dyes (alizarin, disperse blue)
  (conjugated)                     Quinone-based natural dyes

Ethylene      >C=C<                Polyene dyes, some natural pigments
  (polyene)   multiple conjugated  Carotenoids (yellow-orange)

Acridan       N-containing ring    Acridine dyes (fluorescent)
Nitro group   -NO2                 Picric acid derivatives (historic)
Thiocarbonyl  >C=S                 Some sulfur dyes

INDIGO:
  bis-oxindole  O=C-C=C-C=O with NH bridges
                Unique: two carbonyl groups connected through conjugated bridge
                Deep blue: absorption peak 620nm (red absorbed -> blue seen)
                Relatively insensitive to substituents (halogenation increases lambda)
```

### Auxochrome Groups

```
AUXOCHROME   EFFECT                        ROLE IN BONDING
----------   ------                        ---------------
-OH          Bathochromic (red shift)      H-bond, metal chelation (mordant)
-NH2         Strong bathochromic           H-bond, salt formation (acid dyes)
-NHR         Bathochromic, less than NH2   As above
-NR2         Bathochromic                  As above (quaternary: cationic dyes)
-COOH        Weak bathochromic             Salt formation, reactive linking
-SO3H        Hypsochromic (blue shift)     Salt formation, water solubility
-SH          Bathochromic                  Metal bonding (sulfur dyes)
-Cl, -Br     Variable                      Leaving group (reactive dyes)

IMPACT ON MORDANT CHEMISTRY:
  Multiple -OH groups (alizarin, luteolin) -> strong polydentate chelation
  More chelation sites -> more stable dye-metal complex -> better fastness
  Catechol (-OH adjacent pair) especially effective for Fe3+, Al3+, Cu2+
```

---

## HOMO-LUMO Gap and Color

The quantum mechanical explanation: color arises when the energy gap between the highest occupied molecular orbital (HOMO) and the lowest unoccupied molecular orbital (LUMO) matches visible light photon energies:

```
ENERGY LEVEL DIAGRAM

  LUMO  ----     <- photon absorbed, electron promoted to LUMO
         ^
         | h*nu (photon energy = visible light)
         | E = hc/lambda

  HOMO  ----     <- ground state: electrons fill to here

  SHORT CONJUGATION (few double bonds):
    Large HOMO-LUMO gap -> UV absorption -> no visible color (colorless)
    Example: benzene absorbs ~250nm (UV); colorless

  LONG CONJUGATION (many alternating double bonds):
    Small HOMO-LUMO gap -> visible absorption -> colored
    Example: beta-carotene (11 conjugated double bonds) absorbs ~450nm (blue) -> orange
    Indigo (complex conjugated system) absorbs ~620nm (red) -> blue

  EFFECT OF AUXOCHROMES:
    Electron-donating groups (-OH, -NH2) raise HOMO -> smaller gap -> red shift
    Electron-withdrawing groups (-NO2, -SO3H) lower LUMO -> smaller gap -> red shift
    Metal coordination (mordant): distorts electron distribution -> shifts gap
```

---

## Dye Classification by Application Method

The most useful classification for dyers: how does the dye bond to the fiber?

```
DYE CLASS         BOND TO FIBER         FIBER AFFINITY    EXAMPLES
-------------------------------------------------------------------------
ACID DYES         Ionic: -SO3- dye      Wool, silk,       Most synthetic dyes for
                  + -NH3+ fiber         nylon             wool: brilliant, fugitive
                  (protonated amine)                       without mordant

BASIC DYES        Ionic: quaternary     Acrylic, some     Aniline-based, brilliant
(cationic)        -N+(dye) + fiber-COO- wool (modified)   colors; fade in light

DIRECT DYES       H-bonds and           Cotton, linen     Congo Red, Direct Blues
                  van der Waals to      (cellulose)       Poor washfastness without
                  cellulose                               aftertreatment

MORDANT DYES      Coordinate bond       Wool, cotton      All classical natural dyes
                  through metal ion     (with tannin)     + synthetic mordant class
                  bridge                                   (e.g., chrome dyes)

REACTIVE DYES     Covalent bond to      Cotton, linen     ICI Procion dyes (1956)
                  fiber (C-O or C-N)    (cellulose)       Best washfastness on cotton
                                        + silk, wool

VAT DYES          Physical entrapment:  Cotton, linen     Indigo, synthetic vat dyes
                  reduced (leuco) ->    (cellulose)       (Vat Blue 1, Indanthren)
                  absorbed -> oxidized
                  -> insoluble in fiber

DISPERSE DYES     Solid solution in     Polyester,        Low-water solubility;
                  hydrophobic polymer   acetate, nylon    diffuse into fiber at high T
                  fiber matrix
```

---

## Vat Dye Chemistry: Indigo in Detail

Indigo is insoluble in water. It must be chemically reduced to a soluble "leuco" (yellow-green) form, absorbed by fiber, then re-oxidized back to the insoluble blue form -- trapped inside the fiber.

```
INDIGO REDOX CYCLE

  INDIGO (blue, insoluble, C16H10N2O2)
     |
     |  + 2H (reducing agent: Na2S2O4, fructose, or bacteria)
     |  + alkali (NaOH, Ca(OH)2 -- to provide OH- ions)
     v
  LEUCO-INDIGO (yellow-green, soluble as disodium salt, C16H12N2O2^2-)
  "indigo white" = sodium salt of dihydroindigo
     |
     |  Fiber immersed in vat; leuco-indigo diffuses into fiber
     |
     |  Remove fiber from vat; expose to air (O2)
     v
  OXIDATION: leuco-indigo -> indigo (blue)
  Indigo is regenerated INSIDE fiber -- now physically trapped
     |
     |  Repeat: re-dip -> oxidize -> deeper blue
     v
  FINAL COLOR: depth proportional to number of dips
  Traditional Japanese aizome: 20-60+ dips for deep navy
  "Japan Blue" / denim weft: typically 5-8 dips

  VAT CONDITIONS (fermentation vat):
    Traditional: stale urine (urea + bacteria), indigo, wood ash
    Modern natural: fructose (reducing) + lime + heat (pH 10-12)
    Modern chemical: sodium hydrosulfite (Na2S2O4) + NaOH
    Temperature: 40-50°C (warm; not boiling -- destroys leuco-indigo)
    pH: 10-12 required for efficient reduction
```

---

## Reactive Dye Chemistry: Cold Water Dyeing (Procion)

Reactive dyes (invented 1956 by Rattee and Stephens at ICI) form a covalent bond with the fiber hydroxyl groups:

```
REACTIVE DYE - CELLULOSE BOND

  PROCION MX (cold-water reactive, triazine-based):

  Dye-Cl  +  Cellulose-OH  + NaOH  ->  Dye-O-Cellulose  +  HCl + NaOH

  Mechanism:
    1. NaOH deprotonates cellulose -OH -> nucleophilic -O-
    2. Nucleophilic aromatic substitution (SNAr): -O- attacks triazine ring
    3. Chloride displaced -> covalent ether bond (C-O)

  REACTION pH: requires pH 10-12 (soda ash: Na2CO3)
  TEMPERATURE: cold water (Procion MX) or hot (Procion H)
  EXHAUSTION: ~70-80% of dye bonds; ~20-30% hydrolyzes with water -> must be washed out
  WASHFASTNESS: ISO 5/5 -- excellent; covalent bond is permanent

  FIBER AFFINITY:
    Cellulose (cotton, linen, hemp): excellent
    Silk: good (NH2 + OH groups)
    Wool: possible (NH2 groups) but requires lower pH and temp
    Polyester: no --reactive sites not compatible
```

---

## Lightfastness: Photodegradation Mechanisms

The Blue Wool Scale (ISO 105-B02) measures lightfastness by comparing fading of dyed samples to 8 reference blue wool standards under a standardized xenon arc light source:

```
BLUE WOOL SCALE

  BW 1: extremely poor -- visible fade in hours
  BW 2: very poor -- fades in days
  BW 3: poor -- fades in weeks (most flowers, turmeric)
  BW 4: moderate -- months (cochineal on alum, most natural dyes)
  BW 5: fairly good -- years (weld, madder on good mordant)
  BW 6: good -- many years (indigo, some reactive dyes)
  BW 7: very good -- decades (vat dyes, chrome-mordanted dyes)
  BW 8: excellent -- exceptional durability (best synthetic vat dyes)

PHOTODEGRADATION MECHANISM:

  1. UV photon absorbed by chromophore (or by ground-state O2 -> singlet O2)
  2. Excited chromophore + O2 -> reactive oxygen species (ROS)
  3. ROS oxidize the pi system -> break conjugation
  4. Broken conjugation = larger HOMO-LUMO gap -> absorption shifts UV
  5. Color visibly fades or changes hue

  PROTECTIVE FACTORS:
    Mordant stability: metal chelation protects dye from O2 oxidation
    Fiber matrix: wool (natural UV absorbers) slows degradation vs. cotton
    Storage: dark storage slows fading
    UV absorbers: some mordants (Cr3+) absorb UV protecting chromophore
```

---

## Fiber-Dye Affinity Table

```
              ACID   BASIC  DIRECT MORDANT REACTIVE  VAT  DISPERSE
              -------------------------------------------------------
WOOL           XXX    X      X      XXX     X          X     --
SILK           XXX    X      X      XXX     X          X     --
COTTON          X     --     XX     XXX*    XXX       XXX    --
LINEN           X     --     XX     XXX*    XXX       XXX    --
NYLON          XX     X      X       X      X          X    X
POLYESTER       --    X      --      --      --         --  XXX
ACRYLIC         --   XXX     --      --      --         --   X

XXX = primary recommended class
XX  = good affinity
X   = possible but not optimal
--  = not suitable

* Cellulose mordant dyes require tannin pre-treatment
```

---

## Decision Cheat Sheet

| Fiber | Want | Dye Class | Key Chemistry |
|-------|------|-----------|---------------|
| Wool | Natural color, any | Mordant dyes (natural) | Metal coordination |
| Wool | Brilliant modern color | Acid dyes | Ionic bond to protonated -NH2 |
| Cotton | Best washfastness | Reactive dyes (Procion MX) | Covalent C-O bond |
| Cotton | Historical/natural | Mordant dyes via tannin | Tannin bridge + metal chelation |
| Cotton | Blue | Indigo vat dye | Leuco-reduced vat, physical entrapment |
| Silk | Natural tradition | Mordant dyes | As wool, lower temp |
| Polyester | Any | Disperse dyes | Sublimation dyeing, high temp |
| Anything | Deep blue permanent | Indigo (vat process) | No mordant; reduction chemistry |

---

## Common Confusion Points

**"Color is in the conjugated system" not in the ring count** -- Benzene has no color (absorbs UV). Anthracene (3 fused rings) is pale yellow. Tetracene (4 fused rings) is orange. It is the length and topology of conjugation, not simply the ring count. Substitution by electron-donating groups (auxochromes) at specific positions can shift a colorless molecule into the visible range without changing the ring system.

**Acid dyes vs. acidic dyeing conditions**: These are different things. Acid dyes work at low pH (acid bath) but this is to protonate the fiber amine groups, not because the dye itself is acidic. The pH makes the fiber receptive. The dye class "acid dye" refers to the ionic bond mechanism, not the pH.

**Indigo has no mordant but has excellent lightfastness** -- Indigo is physically trapped inside the fiber (not chemically bonded), yet it has Blue Wool Scale 6-7. The fastness comes from the molecule's intrinsic photostability (the unique bis-oxindole resonance structure dissipates absorbed energy without photochemical decomposition -- known as "excited-state proton transfer").

**ISO washfastness and lightfastness are independent tests** -- A dye can have excellent washfastness but poor lightfastness (many direct dyes), or excellent lightfastness but moderate washfastness (some mordant dyes). Always evaluate both for end-use suitability.
