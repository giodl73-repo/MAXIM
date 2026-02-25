# MAXIM — The Physical Encyclopedia

*A personal reference library in 52 bound volumes.*
*Named for Maximus, the boxer who chose his owner.*
*A maxim: a short statement expressing a general truth.*

---

## The Mark

Twelve rays at 30° intervals. Center point. 12 + 1 = 13 sections.
Single-color, works in gold foil relief on fabric cover stock.

```
            ·   ·
          ·   |   ·
        ·     |     ·
       ·      |      ·
      ·───────●───────·
       ·      |      ·
        ·     |     ·
          ·   |   ·
            ·   ·
```

**The count:** 12 rays + 1 center point = 13 sections = 52 volumes.
Thirteen sections times four volumes each. A deck of cards.

**The center point = People.**
Every other section is a domain of knowledge. People is who made it.
The human is at the center of the mark. Maximus. You. The reader.

**Formal description for binder:**
12-ray radial mark. Equal 30° spacing. Rays terminate at equal radius.
Filled center point (●), visually distinct from ray endpoints (·).
No text. No border. Suitable for foil die — provide as SVG or EPS.
Print size on front cover: 2.5" diameter, centered upper third.
Print size on spine: 0.6" diameter, top of spine.

**12 rays — Origins Arc order (clockwise from 12 o'clock):**

| Ray | Section | Era |
|-----|---------|-----|
| 1 | Natural World | Paleolithic — the immediate world |
| 2 | Earth & Space | Neolithic — stars, seasons, ground underfoot |
| 3 | Material Culture | Bronze/Iron Age — fire, clay, metal |
| 4 | Life Sciences | Understanding the body and living systems |
| 5 | History & Ideas | The written record and its interpretation |
| 6 | Mechanics | Classical engineering — lever through locomotive |
| 7 | Technology | Modern engineering — circuit through satellite |
| 8 | Social Sciences | How groups organize, govern, trade |
| 9 | Language & Communication | Encoding and transmitting knowledge |
| 10 | Mathematics & Physics | The formal language of pattern and law |
| 11 | Arts & Culture | Expression beyond the utilitarian |
| 12 | Computing & Software | Formalizing thought itself |
| ● | **People** | **The center — who made all of the above** |

*The survivor at center reads outward: ray 1 first (what can I eat?), ray 12 last (how do I think about this precisely?). People is not a destination in the arc — it is the origin.*

---

## Binding Specification

| Parameter | Specification |
|-----------|---------------|
| **Binder** | PHD Book Binding — phdbookbinding.com |
| **Style** | Fabric Hard Cover |
| **Material** | Buckram |
| **Color** | Dark Navy (or Dark Green — decide per order) |
| **Foil** | Gold, front cover + spine |
| **Headbands** | Top and bottom, gold/navy |
| **Endsheets** | Archival quality (acid-free) |
| **Page size** | 8.5 × 11 in |
| **Paper** | 24 lb acid-free bond (archival, ~90 gsm) |
| **Pages per volume** | 300–420 (target ~350) |
| **Spine width** | ~20 mm at 350 pages on 24 lb |
| **Copies** | Minimum 10 required; order 1 set (34 vols) |

---

## Cover Layout

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│                                                                     │
│                                                                     │
│                           · · · · ·                                │
│                        ·     ·|·     ·                             │
│                       ·      ·|·      ·                            │
│                      ·───────·+·───────·                           │
│                       ·      ·|·      ·                            │
│                        ·     ·|·     ·                             │
│                           · · · · ·                                │
│                                                                     │
│                            M A X I M                               │
│                                                                     │
│                        ─────────────────                           │
│                                                                     │
│                        MECHANICS · II                              │
│                                                                     │
│                                                                     │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

**Front cover text (foil stamped):**
- Line 1: MAXIM (large, centered, ~36pt equivalent, spaced caps)
- Line 2: em-rule divider
- Line 3: SECTION NAME · VOLUME NUMBER (smaller, ~18pt)

**Back cover:** plain buckram, no text.

**Inside front endsheet (printed, not foil):**
```
MAXIM
A Personal Reference Encyclopedia
180 Domains · 13 Sections · 52 Volumes

This volume: MECHANICS · II
  chemical-eng/ · nuclear/ · energy-systems/
```

---

## Spine Layout

Spine text runs bottom-to-top (standard — readable when shelved spine-up).

```
         ┌──────┐
         │  ↑↑  │  ← gold radial mark, 0.6" diam
         │      │
         │  M   │
         │  A   │
         │  X   │
         │  I   │
         │  M   │
         │      │
         │  ──  │  ← gold rule
         │      │
         │  M   │
         │  E   │
         │  C   │
         │  H   │
         │  A   │
         │  N   │
         │  I   │
         │  C   │
         │  S   │
         │      │
         │  ──  │  ← gold rule
         │      │
         │  II  │  ← Roman numeral volume
         └──────┘
```

Spine text order (top to bottom): MARK · MAXIM · rule · SECTION · rule · VOL

---

## Print Specification

| Parameter | Value |
|-----------|-------|
| **Font — body** | Palatino or EB Garamond, 11pt |
| **Font — code** | JetBrains Mono, 10pt |
| **Line height** | 14pt (1.27× body) |
| **Margins** | 0.75" all sides |
| **Lines per page** | ~52 |
| **Header** | Section · Directory · Filename (small caps, 8pt) |
| **Footer** | Page number centered, volume-relative (e.g. 1–420) |
| **Print method** | PDF upload to PHD; send as single merged PDF per volume |
| **Generate PDF** | `mkdocs2book` (ebadi/mkdocs2book) or pandoc + LaTeX |

---

## Volume Plan — All 52 Volumes

*13 sections × 4 volumes each = 52. A deck of cards.*
*Origins Arc order: rays 1–12 clockwise, People (●) at center.*
*Three thin sections (Natural World, Material Culture, Language & Comm, Mechanics) will reach full*
*4 × 250 pp depth via Batch 12 content additions. Current stubs noted.*

### Ray 1 — Natural World  (4 volumes · ~870 pp current + Batch 12)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| NW·I | periodic-table/ · animal-phylogeny/ · spices/ · food-plants/ | ~250 |
| NW·II | culinary-history/ · fermentation-spirits/ · mycology/ · marine-biology/ | ~220 |
| NW·III | entomology/ · ornithology/ · zoology/ · horticulture/ | ~200 |
| NW·IV | *Batch 12: dendrology/ · freshwater-biology/ · soil-science/ · coral-reefs/* | ~200 |

### Ray 2 — Earth & Space  (4 volumes · ~1,050 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| ES·I | astronomy/ · geology/ · paleontology/ | ~350 |
| ES·II | meteorology/ · climate-science/ · oceanography/ · hydrology/ | ~280 |
| ES·III | geography/ · agriculture/ · mineralogy/ · planetary-science/ | ~280 |
| ES·IV | geochemistry/ · space-exploration/ · astrobiology/ | ~220 |

### Ray 3 — Material Culture  (4 volumes · ~850 pp current + Batch 12)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| MC·I | pigments/ · coatings/ · textiles/ | ~200 |
| MC·II | ceramics/ · glassmaking/ · jewelry/ · metalworking/ | ~240 |
| MC·III | plastics-polymers/ · papermaking/ · composite-materials/ · furniture/ | ~210 |
| MC·IV | *Batch 12: woodworking/ · leatherworking/ · masonry/ · rope-cordage/* | ~200 |

### Ray 4 — Life Sciences  (4 volumes · ~1,050 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| LS·I | natural-sciences/ · biology/ · botany/ · ecology/ | ~360 |
| LS·II | human-biology/ · neuroscience/ · cognitive-science/ · disease/ | ~280 |
| LS·III | medicine/ · nutrition/ · genomics/ · immunology/ · microbiology/ | ~300 |
| LS·IV | evolutionary-biology/ · virology/ · biophysics/ · pharmacology/ · developmental-biology/ | ~270 |

### Ray 5 — History & Ideas  (4 volumes · ~1,010 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| HI·I | historical-geography/ · history-of-science/ · economic-history/ · military-history/ | ~360 |
| HI·II | anthropology/ · philosophy/ · mythology/ · religious-studies/ · archaeology/ | ~310 |
| HI·III | logic/ · intellectual-history/ · social-history/ | ~220 |
| HI·IV | political-history/ · philosophy-of-mind/ · ethics/ | ~230 |

### Ray 6 — Mechanics  (4 volumes · ~1,000 pp)
*Classical engineering: Archimedes through the Industrial Revolution.*

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| M·I | mechanical/ · structural/ · aeronautics/ | ~260 |
| M·II | chemical-eng/ · nuclear/ · energy-systems/ | ~260 |
| M·III | electrical-grid/ · hvac/ · plumbing/ · construction-materials/ | ~260 |
| M·IV | acoustics/ · optics/ · transportation/ · manufacturing/ | ~260 |

### Ray 7 — Technology  (4 volumes · ~870 pp current + Batch 12)
*Modern engineering: electronic age through systems age.*

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| T·I | semiconductor-manufacturing/ · telecommunications/ · robotics/ | ~240 |
| T·II | biomedical-engineering/ · formal-methods/ · systems-engineering/ | ~220 |
| T·III | urban-planning/ · environmental-engineering/ · materials-processing/ | ~210 |
| T·IV | *Batch 12: nanotechnology/ · energy-storage/ · infrastructure-systems/* | ~200 |

### Ray 8 — Social Sciences  (4 volumes · ~1,100 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| SS·I | economics/ · finance/ · behavioral-economics/ · game-theory/ · statistics-applied/ | ~380 |
| SS·II | political-science/ · law/ · sociology/ · demography/ | ~280 |
| SS·III | criminology/ · psychology/ · organizational-behavior/ · public-health/ | ~280 |
| SS·IV | media-studies/ · education/ · international-relations/ | ~220 |

### Ray 9 — Language & Communication  (4 volumes · ~900 pp current + Batch 12)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| LC·I | linguistics/ · world-languages/ · codes/ · typography/ | ~260 |
| LC·II | printing-publishing/ · cinema-film/ · radio-television/ · literature/ | ~240 |
| LC·III | rhetoric/ · philosophy-of-language/ · semiotics/ · translation/ | ~200 |
| LC·IV | *Batch 12: journalism/ · oral-tradition/ · epigraphy/ · digital-media/* | ~200 |

### Ray 10 — Mathematics & Physics  (4 volumes · ~1,050 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| MP·I | mathematics/ · physics/ · electronics/ | ~370 |
| MP·II | materials/ · quantum-computing/ · control-theory/ · signal-processing/ · information-theory/ | ~280 |
| MP·III | number-theory/ · abstract-algebra/ · topology/ · probability-statistics/ · differential-geometry/ · numerical-methods/ | ~300 |
| MP·IV | complex-analysis/ · fluid-dynamics/ · statistical-mechanics/ · partial-differential-equations/ · variational-calculus/ · lie-groups/ | ~290 |

### Ray 11 — Arts & Culture  (4 volumes · ~940 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| AC·I | art-history/ · architecture-history/ · architecture/ · music-theory/ | ~300 |
| AC·II | photography/ · colors/ · cartography/ · games-history/ · sports-history/ | ~260 |
| AC·III | watchmaking/ · theater-performance/ · dance/ · industrial-design/ | ~250 |
| AC·IV | graphic-design/ · fashion/ · comics-sequential-art/ · sports-science/ | ~230 |

### Ray 12 — Computing & Software  (4 volumes · ~920 pp)

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| C·I | computing/ · ai-engineering/ · data-science/ | ~340 |
| C·II | languages/ · query-languages/ · scripting/ · os/ | ~350 |
| C·III | cryptography/ · computer-architecture/ · machine-learning-theory/ | ~230 |
| C·IV | *Batch 12: distributed-systems/ · security-engineering/ · cloud-architecture/* | ~200 |

### ● Center — People  (4 volumes · ~1,180 pp)
*The humans who made everything on rays 1–12.*

| Vol | Directories | Target pp |
|-----|-------------|-----------|
| P·I | mathematicians-logicians/ · physicists-astronomers/ · chemists-naturalists/ | ~300 |
| P·II | engineers-inventors/ · computing-pioneers/ · explorers/ | ~300 |
| P·III | philosophers-thinkers/ · artists-architects/ · writers-poets/ | ~300 |
| P·IV | political-reformers/ · social-reformers/ · visionaries/ | ~300 |

---

## Summary

*In Origins Arc order (rays 1–12, People at center ●). Each section 4 volumes. 13 × 4 = 52.*

| Ray | Section | Volumes | Approx. Pages |
|-----|---------|---------|---------------|
| 1 | Natural World | 4 | ~870 |
| 2 | Earth & Space | 4 | ~1,050 |
| 3 | Material Culture | 4 | ~850 |
| 4 | Life Sciences | 4 | ~1,050 |
| 5 | History & Ideas | 4 | ~1,010 |
| 6 | Mechanics | 4 | ~1,000 |
| 7 | Technology | 4 | ~870 |
| 8 | Social Sciences | 4 | ~1,100 |
| 9 | Language & Communication | 4 | ~900 |
| 10 | Mathematics & Physics | 4 | ~1,050 |
| 11 | Arts & Culture | 4 | ~940 |
| 12 | Computing & Software | 4 | ~920 |
| ● | **People** | **4** | **~1,180** |
| — | **Total** | **52** | **~13,790** |

---

## Shelf Layout

52 volumes, each ~20 mm wide = ~1,040 mm total ≈ 41 inches of shelf.
Two standard 24" shelves (or one 48" shelf) holds the complete set.

```
── Shelf 1 ──────────────────────────────────────────────────────────────────
NW  NW  NW  NW   ES  ES  ES  ES   MC  MC  MC  MC   LS  LS  LS  LS
I   II  III IV    I   II  III IV    I   II  III IV    I   II  III IV

HI  HI  HI  HI   M   M   M   M    T   T   T   T    SS  SS  SS  SS
I   II  III IV    I   II  III IV    I   II  III IV    I   II  III IV

── Shelf 2 ──────────────────────────────────────────────────────────────────
LC  LC  LC  LC   MP  MP  MP  MP   AC  AC  AC  AC   C   C   C   C
I   II  III IV    I   II  III IV    I   II  III IV    I   II  III IV

P   P   P   P
I   II  III IV
```

*Abbreviations: NW Natural World · ES Earth & Space · MC Material Culture · LS Life Sciences*
*HI History & Ideas · M Mechanics · T Technology · SS Social Sciences*
*LC Language & Comm · MP Mathematics & Physics · AC Arts & Culture · C Computing*
*P People (center section)*

---

## Index Volume (optional Vol. 53)

A comprehensive cross-reference index across all 52 volumes:
- Person → sections where they appear
- Concept → all relevant directory entries
- Cross-section bridges (e.g. "Fourier transform → signal-processing/, complex-analysis/, physics/")

Binding: same spec, spine: `MAXIM · INDEX`

Vol. 53 if printed. Shelf slot reserved at right end of Shelf 2.

---

## Order Checklist

- [ ] Convert MkDocs to print PDF (one PDF per volume per volume plan above)
- [ ] Design the 12-ray radial mark as SVG/EPS (send to binder)
- [ ] Choose buckram color (dark navy or dark green — decide before first order)
- [ ] Choose foil color (gold recommended; silver is alternative)
- [ ] Contact PHD Bookbinding — info@PHDBookbinding.com — for fabric hard cover quote on 52 volumes
- [ ] Confirm page count per volume before ordering (measure actual output PDF)
- [ ] Print on acid-free 24 lb bond before binding
- [ ] Order 1 complete set; reorder individual volumes as content updates

---

*This document is the binding specification for the MAXIM Encyclopedia.*
*Named for Maximus. Built for permanence.*
