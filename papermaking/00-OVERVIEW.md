# Papermaking — Landscape and Taxonomy

<!-- @editor[diagram/P2]: Landscape diagram lists categories in flat boxes but doesn't show the process flow — raw material → pulping → forming → finishing should be connected with arrows to show the manufacturing pipeline. Rework as a layered system view with directional flow -->

## The Big Picture

```
+------------------------------------------------------------------+
|                 THE PAPER UNIVERSE                               |
|                                                                  |
|   RAW MATERIAL   PULPING         FORMING      FINISHING          |
|   ───────────    ───────         ───────      ─────────         |
|   Wood chips     Chemical        Paper        Sizing             |
|   Cotton rags    (Kraft, sulfite) machine      Coating            |
|   Agricultural   Mechanical      (Fourdrinier, Calendering       |
|   residue        (TMP, CTMP)     twin-wire)   Supercalendering   |
|   Recycled fiber Semi-chemical   Press + dry  Cutting / reeling  |
|                                                                  |
|   CHEMISTRY           PRODUCT FAMILIES                          |
|   ────────            ────────────────                          |
|   Sizing agents       Printing/writing paper                    |
|   Coatings            Packaging board                           |
|   Brighteners         Tissue / hygiene                          |
|   Retention aids      Specialty / technical                     |
|   Drainage aids       Security paper                            |
+------------------------------------------------------------------+
```

Paper = a web of cellulose fibers, hydrogen-bonded together, formed from a
dilute aqueous suspension and dried. ~400 million metric tons/year produced
globally. One of the oldest industrial processes (105 CE, Cai Lun) now
operating at machine speeds of 2,000 m/min and widths of 11 m.

---

## The Fiber: Cellulose

Paper is cellulose in fiber form. Understanding the fiber is everything.

```
   CELLULOSE STRUCTURE:
   ──────────────────────────────────────────────────────────
   [C6H10O5]n    β-1,4-glycosidic bonds linking glucose
   Degree of polymerization (DP): native wood ~10,000
                                   kraft pulp ~1,000–1,500
                                   cotton linters ~7,000

   Hydrogen bonding within and between chains → crystalline microfibrils

   Cell wall layers:
   S1 (outer) — 15–35% of wall thickness
   S2 (middle, dominant) — 65–85%    ← controls fiber flexibility
   S3 (inner) — thin

   Microfibril angle (MFA) in S2:
   Low MFA (5–10°): stiff, high tensile, low elongation (latewood)
   High MFA (20–45°): flexible, high elongation (juvenile wood)
```

### Wood Fibers — Softwood vs. Hardwood

```
   SOFTWOOD (conifers: pine, spruce, fir, eucalyptus in some contexts)
   ─────────────────────────────────────────────────────────────────────
   Fiber length: 2–4 mm (tracheid cells)
   High bonding strength, high tear resistance
   Kraft SW pulp: strength papers, grocery bags, corrugated

   HARDWOOD (deciduous: birch, eucalyptus, aspen, maple)
   ──────────────────────────────────────────────────────
   Fiber length: 0.5–1.5 mm (shorter)
   Finer sheet structure → smoother surface, better printing
   Kraft HW pulp: printing/writing paper, tissue, copy paper
```

### Non-Wood Fibers

```
   COTTON LINTERS   — seed fiber, very long (5–40mm), high purity cellulose
                      Banknotes, security paper, high-quality writing paper
   FLAX / HEMP      — bast fiber, long (~10–50mm), high strength
                      Historical European rag paper, specialty
   SUGARCANE BAGASSE— agricultural residue, South America, Asia
   BAMBOO           — fast-growing, significant in Asia
   STRAW (wheat, rice)— low-quality, old masonry papers, emerging
```

---

## The Three Pulping Routes

```
                        WOOD CHIPS
                            |
           +----------------+----------------+
           |                |                |
    CHEMICAL PULPING  MECHANICAL PULPING  SEMI-CHEMICAL
    ──────────────   ──────────────────  ─────────────
    Dissolve lignin  Mechanical           Chemical pre-
    with chemicals   separation of        treatment then
                     fibers               mechanical
    Kraft (kraft)    TMP                  NSSC
    Sulfite          CTMP                 (corrugating medium)
           |
    60–65% yield     90–95% yield         80–85% yield
    Strong fibers    Weaker fibers        Stiff (lignin retained)
    Bleachable       Yellows (newsprint)  Medium-strength
```

---

## Paper Grades: The Market Map

```
PRINTING & WRITING PAPER
  Office paper (copy, laser)  — free sheet, 75–90 gsm
  Coated printing             — LWC, MWC, WFC (magazines, brochures)
  Uncoated groundwood         — newsprint, telephone directories

PACKAGING
  Kraftliner / testliner      — corrugated box faces
  Corrugating medium (fluting)— corrugated box inner
  Cartonboard (SBS, GC1)      — folding cartons (food, pharma)
  Liquid packaging board (LPB)— Tetra Pak-style

TISSUE & HYGIENE
  Facial tissue, toilet tissue, hand towels, diapers
  Creping essential — wet-laid process different from flat paper

SPECIALTY
  Security paper              — banknotes, passports
  Thermal paper               — receipts, tickets
  Release paper               — silicone coating for labels
  Cigarette paper             — precise porosity
  Tea bags                    — wet strength, sealing ability
  Filter paper                — defined pore size distribution
  Wallcovering                — dimensional stability, cleanability
```

---

## Key Paper Properties and Units

```
+----------------------------------------------------------+
|  GRAMMAGE (basis weight):  g/m²  (gsm)                  |
|    Tissue: 14–20 gsm    Copy: 75–90    Kraft: 70–150    |
|    Board: 170–350+      Corrugated medium: 80–190       |
|                                                          |
|  THICKNESS:  µm (microns)                               |
|    Tissue: 50–100 µm   Copy: 100 µm   Board: 350–700   |
|                                                          |
|  DENSITY = grammage / thickness (g/cm³)                 |
|    Soft tissue: 0.20 g/cm³   Supercalendered: 1.3       |
|                                                          |
|  TENSILE:  kN/m (tensile index: Nm/g)                   |
|    Machine direction (MD) stronger than CD              |
|    MD/CD ratio: 2:1 to 3:1 (machine anisotropy)        |
|                                                          |
|  TEAR:  mN (Elmendorf tear)                              |
|    Inversely related to tensile: high-yield = better tear|
|                                                          |
|  BRIGHTNESS:  % ISO (457 nm reflectance)                |
|    Newsprint: 55–60   Office: 85–92   Optical brightened: 96+ |
|                                                          |
|  SMOOTHNESS:  Sheffield units or Bekk seconds           |
|                                                          |
|  AIR PERMEABILITY:  ml/min (Gurley)                     |
|    Critical for filter paper, cigarette paper           |
+----------------------------------------------------------+
```

---

## Directory Contents

| File | Topic |
|------|-------|
| 01-HISTORY.md | Cai Lun to Fourdrinier — 1900 years of papermaking |
| 02-RAW-MATERIALS.md | Wood pulp anatomy, cotton, non-woods, recycled fiber |
| 03-KRAFT-PROCESS.md | Chemical pulping: cooking, washing, bleaching, recovery |
| 04-PAPER-MACHINE.md | Forming, pressing, drying — the Fourdrinier to today |
| 05-PAPER-CHEMISTRY.md | Sizing, coating, retention, wet strength, calendering |
| 06-ARCHIVAL-PAPER.md | Acid degradation, alkaline paper, conservation |
| 07-SPECIALTY-PAPERS.md | Security, thermal, filter, cigarette, technical papers |
| 08-DIGITAL-DISRUPTION.md | Office paper decline, packaging growth, future |
| 09-SUSTAINABILITY.md | Recycling, FSC/PEFC, carbon footprint, alternatives |

---

<!-- @editor[bridge/P2]: No old-world bridge in the overview — natural parallels: continuous manufacturing pipeline (any process engineering), polymer chemistry (cellulose as a natural polymer), or feedback control systems (paper machine CD/MD profiling). A senior engineer from any stack would benefit from "paper mill as a chemical reactor + continuous process line" framing -->

## Decision Cheat Sheet

| Need | Paper type |
|------|------------|
| High-speed laser printing | Free sheet (acid-free, sized, 75–90 gsm) |
| Glossy magazine | LWC or MWC coated |
| Strong packaging | Unbleached softwood kraft |
| Banknote / security document | Cotton-based security paper |
| Long archival life | Alkaline, acid-free, buffered, no lignin |
| Tissue / hygiene | Through-air dried (TAD) or crêped wet-press |
| Corrugated box face | Kraftliner (SW or recycled) |
| Thermal receipt | Thermal paper (BPA-free increasingly) |
| Filter (laboratory) | Defined pore-size hardened cotton filter paper |

---

## Common Confusion Points

**"Bond paper" is not a separate process**: "Bond" refers to the finish/use
(originally for bonds/certificates — sturdy, crisp). Today it just means good
quality uncoated paper.

**Paperboard is not plastic-lined cardboard**: Liquid packaging board (Tetra Pak,
milk carton) is paperboard + polyethylene + aluminum foil laminate. Plain
folding carton board (SBS) has no plastic layer. Different end-of-life paths.

**Recycled paper is not as strong as virgin**: Fibers are shorter, hornified
(less swellable = fewer hydrogen bonds), and contaminated. OCC (old corrugated
container) recycling produces testliner — adequate for boxes but not kraft sacks.

**pH matters enormously for paper longevity**: Documents on wood-pulp acidic paper
from 1900–1980 are crumbling in library archives now. Alkaline (pH 7.5–8.5)
and buffered (calcium carbonate) paper lasts centuries. Switch to alkaline
papermaking happened in 1980s–90s for fine paper grades.
