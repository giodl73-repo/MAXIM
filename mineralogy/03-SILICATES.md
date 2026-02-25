# Silicate Minerals

## The Big Picture

```
+------------------------------------------------------------------+
|              SILICATE CLASSIFICATION BY CONNECTIVITY             |
|                                                                  |
|  Building block: SiO₄ tetrahedron                               |
|  Si at center, 4 oxygens at corners                             |
|  When tetrahedra share oxygens, they polymerize                 |
|                                                                  |
|  ISOLATED          No sharing    Nesosilicates    Olivine       |
|  PAIRS             1 shared O    Sorosilicates    Epidote       |
|  RINGS             2 shared O    Cyclosilicates   Tourmaline    |
|  SINGLE CHAIN      2 shared O    Inosilicates     Pyroxene      |
|  DOUBLE CHAIN      2½ shared O   Inosilicates     Amphibole     |
|  SHEETS            3 shared O    Phyllosilicates  Mica, clay    |
|  3D FRAMEWORK      4 shared O    Tectosilicates   Quartz, feld. |
+------------------------------------------------------------------+

This is literally a graph connectivity problem:
  0 shared corners per tetrahedron → isolated (degree 0)
  1 shared corner → pair (degree 1 at the bridge)
  2 shared corners → chain (degree 2)
  3 shared corners → sheet (degree 3)
  4 shared corners → framework (degree 4)
```

The Si:O ratio drops systematically as connectivity increases: isolated (1:4) → framework (1:2). The more shared oxygens, the higher the Si/O ratio, the more polymerized, the more resistant to chemical weathering.

---

## The SiO₄ Tetrahedron

```
      O
      |
  O — Si — O        Bond angle O-Si-O ≈ 109.5°
      |               Si-O bond: strong covalent character
      O               Bond length: ~1.62 Å

Si⁴⁺ charge = +4
4 × O²⁻ charge = -8
Net: SiO₄⁴⁻ (tetrahedron is a polyanion)

When two tetrahedra share an oxygen:
O₃Si-O-SiO₃ → the bridging O is shared, not counted twice
→ Si₂O₇⁶⁻ for a pair (sorosilicate)
```

---

## Class 1: Nesosilicates (Island Silicates)

**Isolated SiO₄⁴⁻ tetrahedra** — no polymerization. Held together by cations between tetrahedra. High degree of ionic character.

```
Si:O = 1:4    General formula: (cations)(SiO₄)

OLIVINE GROUP: (Mg,Fe)₂SiO₄
Forsterite (Mg₂SiO₄) — fayalite (Fe₂SiO₄): complete solid solution
Most abundant mineral in Earth's upper mantle
Dense, refracts readily (mg-rich olivine = Mg-dominated), high melting point
→ Dunite rock = >90% olivine; peridotite = olivine + pyroxene
Critical: subducting oceanic crust carries olivine → phase transitions
  at depth drive deep focus earthquakes

GARNET GROUP: X₃Y₂(SiO₄)₃
X = Ca, Mg, Fe, Mn; Y = Al, Fe, Cr
No cleavage (all covalent linkage in 3D around tetrahedra)
Indicator minerals: pyrope (Mg-garnet) = high-P mantle source
almandine (Fe-garnet) = common in schist and gneiss
grossular (Ca-Al garnet) = calc-silicate rocks
uvarovite (Ca-Cr garnet) = bright green, in chromite deposits

ZIRCON: ZrSiO₄
Extremely resistant to weathering and chemical alteration
Incorporates U and Th into structure → geochronology by U-Pb decay
Oldest material on Earth: detrital zircon grains from Jack Hills, Australia
  age 4.404 billion years (Earth formed ~4.54 Ga)
Hafnium isotopes in zircon → crustal growth history

TOPAZ: Al₂SiO₄(F,OH)₂
Hardness 8 on Mohs scale
Gemstone; also used as pressure calibrant in experimental petrology
```

---

## Class 2: Sorosilicates (Pair Silicates)

**Two tetrahedra sharing one oxygen** → Si₂O₇⁶⁻ double tetrahedral unit.

```
Si:O = 2:7    Less common than other classes

EPIDOTE GROUP: Ca₂(Al,Fe)₃(Si₂O₇)(SiO₄)(OH)
Common in low-grade metamorphic rocks
Mixed sorosilicate + nesosilicate in same structure
Pistachio green, used as metamorphic indicator

HEMIMORPHITE: Zn₄(Si₂O₇)(OH)₂·H₂O
Zinc ore mineral in oxidized zones
```

---

## Class 3: Cyclosilicates (Ring Silicates)

**Tetrahedra in closed rings** — 3-member, 4-member, or 6-member rings.

```
Si:O = 1:3    Ring formula: (SiO₃)ₙⁿ⁻

6-MEMBERED RING: Si₆O₁₈¹²⁻
BERYL: Be₃Al₂(Si₆O₁₈)
  Emerald = Cr-bearing beryl (chromium gives intense green)
  Aquamarine = Fe-bearing beryl (blue-green)
  Morganite = Mn-bearing beryl (pink)
  Very low chemical reactivity, hard (7.5–8 Mohs)
  Large channels in structure → beryllium ore source

TOURMALINE: complex Na,Ca / Mg,Fe,Al / B / Si₆O₁₈ ring
  Most compositionally complex common mineral
  Pyroelectric and piezoelectric (electric polarization under stress/temp)
  → Pressure sensor in early instruments; now synthesized for electronics
  Tourmaline = type mineral for piezoelectricity

3-MEMBERED RING: Si₃O₉⁶⁻
BENITOITE: BaTiSi₃O₉ — rare; California state gem
```

---

## Class 4: Inosilicates (Chain Silicates)

### Single Chains — Pyroxene Group

```
SINGLE CHAIN: each tetrahedron shares 2 oxygens → (SiO₃)ₙ²ⁿ⁻

Si:O = 1:3

     O   O   O   O
     |   |   |   |
 ——Si——Si——Si——Si——   infinite chain
     |   |   |   |
     O   O   O   O

PYROXENE GROUP: General formula (Ca,Mg,Fe,Na)(Mg,Fe,Al)(Si,Al)₂O₆

Important members:
  Enstatite (MgSiO₃) — mantle pyroxene
  Diopside (CaMgSi₂O₆) — calc-silicate, decorative stone
  Augite (Ca,Na)(Mg,Fe,Al)(Si,Al)₂O₆ — dominant in basalt
  Jadeite (NaAlSi₂O₆) — one jade mineral (true jade)
  Hedenbergite (CaFeSi₂O₆) — iron-rich pyroxene

Crystal form: 2 cleavage planes at ~90° to each other
→ Square cross-section in thin section (diagnostic)
Dominant mafic mineral in basalt and gabbro
```

### Double Chains — Amphibole Group

```
DOUBLE CHAIN: two chains linked → Si₄O₁₁⁶⁻ unit

Si:O = 4:11

     Two single chains zipped together laterally
     Every other tetrahedron links the two chains

AMPHIBOLE GROUP: General formula
A₀₋₁B₂C₅T₈O₂₂(OH,F,Cl)₂
  A = Na, K; B = Ca, Na, Mg, Fe, Mn; C = Mg, Fe, Al, Ti; T = Si, Al

Important members:
  Hornblende — dominant amphibole in igneous/metamorphic rocks
  Actinolite — green, in greenschist facies metamorphic rocks
  Tremolite — asbestiform variety = tremolite asbestos
  Glaucophane — Na-rich; marker of high-P/low-T (blueschist facies)
  Riebeckite — fibrous form = crocidolite (blue asbestos)

Crystal form: 2 cleavage planes at ~60°/120° to each other
→ Hexagonal cross-section in thin section (diagnostic)
→ Pyroxene vs. amphibole ID: cleavage angle (90° vs. 60°)

ASBESTOS NOTE:
Six silicate minerals form asbestiform (fibrous) habits:
chrysotile (serpentine), amosite (cummingtonite), crocidolite (riebeckite),
tremolite, actinolite, anthophyllite
The fibrous habit → aerosol → mesothelioma risk
Chemical composition is secondary to fiber geometry in toxicity
```

---

## Class 5: Phyllosilicates (Sheet Silicates)

**Tetrahedra share 3 oxygens** → infinite 2D sheets. Produces flat, plate-like crystals with perfect basal cleavage.

```
Si:O = 2:5    Sheet unit: Si₄O₁₀⁴⁻ (4-ring repeating unit in sheet)

SHEET STRUCTURE:
     _____   _____   _____
    /     \ /     \ /     \   ← Tetrahedral sheet
    \_____/ \_____/ \_____/
         |||||||||||||        ← Interlayer cations/water
    _____   _____   _____
    /     \ /     \ /     \   ← Octahedral sheet (Al/Mg)
    \_____/ \_____/ \_____/

T-O structure: 1 tet + 1 oct layer (kaolinite, serpentine)
T-O-T structure: 1 oct sandwiched between 2 tet (mica, chlorite, smectite)
```

**Mica Group** — T-O-T + interlayer cation (K⁺, Na⁺):

```
MUSCOVITE: KAl₂(AlSi₃)O₁₀(OH)₂
  White/silver mica; common in granites, schists, quartzite
  Perfect basal cleavage → thin transparent sheets
  Used historically as window glass, furnace windows

BIOTITE: K(Mg,Fe)₃(AlSi₃)O₁₀(OH)₂
  Black mica; iron-magnesium analog of muscovite
  K-Ar and ⁴⁰Ar/³⁹Ar geochronometer

PHLOGOPITE: KMg₃(AlSi₃)O₁₀(OH)₂
  Magnesium mica; in kimberlites and ultramafic rocks

LEPIDOLITE: K(Li,Al)₃(AlSi₃)O₁₀(OH,F)₂
  Lithium mica — indicator for lithium-bearing pegmatites
  Ore mineral for Li in some deposits
```

**Clay Minerals** — T-O or T-O-T with variable interlayer:

| Mineral | Structure | Swelling | Occurrence |
|---------|-----------|---------|------------|
| Kaolinite | T-O (1:1) | None | Tropical weathering of feldspar |
| Illite | T-O-T (2:1), K⁺ | None | Diagenesis of smectite |
| Smectite (montmorillonite) | T-O-T (2:1), H₂O | High | Bentonite, drilling muds |
| Chlorite | T-O-T-O (2:1:1) | None | Metamorphic, low-T alteration |

**Serpentine Group**:

```
CHRYSOTILE: Mg₃Si₂O₅(OH)₄ — fibrous (rolled sheets)
LIZARDITE: Mg₃Si₂O₅(OH)₄ — platy
ANTIGORITE: Mg₃Si₂O₅(OH)₄ — corrugated sheets
Serpentinization: olivine + water → serpentine + magnetite + heat
Reaction is exothermic; major heat source in slow-spreading ocean ridges
Chrysotile = "white asbestos" (most commercially used; fibrous habit)
```

---

## Class 6: Tectosilicates (Framework Silicates)

**All 4 oxygens shared** → 3D framework. Highest Si/O ratio, highest polymerization, lowest density, most resistant to weathering.

```
Si:O = 1:2    All oxygens bridging (no "free" oxygens)

QUARTZ: SiO₂ — pure silica framework
  Hexagonal (low-quartz, α-quartz): stable <573°C
  Pure covalent network — very hard (7 Mohs), no cleavage
  Piezoelectric: quartz oscillators → frequency standards (MHz)
  Crystal oscillators in watches, electronics
  Extremely resistant to weathering → beach sand is largely quartz

FELDSPAR GROUP — most abundant mineral group (60% of Earth's crust)
  AlSi₃O₈ framework with cation in cavities
  Al³⁺ replaces Si⁴⁺ in some tetrahedra → charge deficit → cation needed

  K-FELDSPAR: KAlSi₃O₈
    Orthoclase (monoclinic), sanidine (high-T), microcline (triclinic)
    Pink color in granites; potassium ore source
    K-Ar and Ar-Ar geochronometer

  PLAGIOCLASE: NaAlSi₃O₈ (albite) ↔ CaAl₂Si₂O₈ (anorthite)
    Complete solid solution series
    Charge-coupled: Na + Si ↔ Ca + Al
    Polysynthetic twinning (definitive microscopic ID)
    ANORTHITE CONTENT controls: density, melting point, weathering rate

ZEOLITES — aluminosilicate frameworks with large open channels
  Channel size: 3–13 Å → molecular sieves
  Na, K, Ca in channels — exchangeable → water softeners
  Clinoptilolite, mordenite, natrolite, analcime (natural)
  ZSM-5, zeolite-A, zeolite-Y (synthetic — billions of tons for catalysis)
  → Zeolites = mineral inspiration for industrial molecular sieves

FELDSPATHOIDS — Si-poor relatives of feldspar
  Nepheline (NaAlSiO₄), leucite (KAlSi₂O₆), sodalite
  Occur only in Si-undersaturated rocks; incompatible with quartz
```

---

## Rock-Forming Mineral Summary

```
BOWEN'S REACTION SERIES — crystallization from mafic melt

HIGH TEMPERATURE (first to crystallize from basaltic melt)
  Olivine (Mg-rich)  ←— Discontinuous branch: each mineral
  Pyroxene               is a different structure
  Amphibole
  Biotite
LOW TEMPERATURE

  Anorthite (Ca-plagioclase)  ←— Continuous branch: same structure,
  Labradorite                      compositional shift toward Na
  Andesine
  Oligoclase
  Albite (Na-plagioclase)

LATE CRYSTALLIZATION (both branches converge)
  K-feldspar
  Muscovite
  Quartz                ←— Last to crystallize from felsic melt

This series explains why mafic rocks (basalt) are olivine+pyroxene
and felsic rocks (granite) are quartz+feldspar+mica
```

---

## Si:O Ratio and Weathering Resistance

| Class | Si:O | Example | Weathering resistance |
|-------|------|---------|----------------------|
| Nesosilicates | 1:4 | Olivine | Low — olivines weather rapidly |
| Sorosilicates | 2:7 | Epidote | Low-moderate |
| Cyclosilicates | 1:3 | Tourmaline | High |
| Inosilicates (single chain) | 1:3 | Pyroxene | Moderate |
| Inosilicates (double chain) | 4:11 | Amphibole | Moderate-high |
| Phyllosilicates | 2:5 | Mica | Variable (cleavage exposes surface) |
| Tectosilicates | 1:2 | Quartz | Very high |

Goldich's dissolution series (1938) matches Bowen's reaction series in reverse — the minerals that crystallize first at high temperature are the least stable at Earth's surface conditions.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why are silicates dominant? | Si + O = 74% of crust; SiO₄ tetrahedra polymerize into all structure types |
| How to ID pyroxene vs. amphibole? | Cleavage angles: pyroxene ~90°, amphibole ~60°/120° |
| What is jade? | Jadeite (pyroxene) or nephrite (tremolite/actinolite amphibole) — different minerals, same name |
| Why is quartz resistant to weathering? | 3D covalent framework, no cleavage, chemically inert at surface T |
| What are clay minerals? | Phyllosilicates formed by weathering of feldspar; kaolinite, smectite, illite |
| Why does mica split into thin sheets? | Perfect basal cleavage along weak interlayer bonds (K⁺ bridges between T-O-T units) |
| Why is olivine in the mantle? | High density, high Mg content, crystallizes at highest T from mafic melt |

---

## Common Confusion Points

**Amphibole vs. pyroxene under the microscope**: Both form dark elongate crystals in thin section. The diagnostic test is cleavage angle. Pyroxene shows near-right-angle cleavage in cross-section; amphibole shows oblique 60°/120° cleavage. Also, amphiboles have OH in structure; pyroxenes do not — amphiboles dehydrate at higher T than their stability field.

**Feldspar abundance**: Feldspars are the most abundant mineral group in Earth's crust (~60%). Quartz gets the attention (in "quartz sandstone"), but feldspar is the dominant mineral in most igneous and metamorphic rocks.

**Zeolites as minerals**: Natural zeolites (clinoptilolite, natrolite) are minerals. Synthetic zeolites (ZSM-5, zeolite-A) are technically not minerals (not "naturally occurring"), but share the same structural principles. The synthetic versions are enormously important industrially.

**Serpentine asbestos vs. amphibole asbestos**: Chrysotile (serpentine) fibers are curly; amphibole asbestos (crocidolite, amosite) fibers are straight and needle-like. Straight fibers are more biopersistent (harder for lungs to clear) → amphibole asbestos is more dangerous, but all forms are regulated.

**T-O vs. T-O-T clay layers**: Kaolinite has a 1:1 (T-O) layer — no swelling. Smectite has a 2:1 (T-O-T) layer with water in the interlayer → swells dramatically when wet. This is why bentonite (smectite-rich clay) is used as a sealant and why montmorillonite soil shrinks/cracks when dry.
