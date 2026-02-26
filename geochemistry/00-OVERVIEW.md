# Geochemistry — Landscape and Taxonomy

## The Big Picture

Geochemistry applies chemistry to understand the Earth and solar system: where elements live, how they move, and how isotopes record the timing and conditions of geological processes.

```
GEOCHEMISTRY: THREE PILLARS WITH FEEDBACKS
+------------------------------------------------------------------+
|                                                                  |
|  ELEMENT DISTRIBUTION          feeds into ——→  ISOTOPE SYSTEMS  |
|  (Goldschmidt classification;                  (parent/daughter  |
|   reservoirs; partition coeff.;                ratios encode age  |
|   incompatible element cycling)  ←———————     + source tracing) |
|       |                              |                           |
|       |  (element abundances in     (isotopes record            |
|       |   each reservoir set the     conditions of process)     |
|       v   initial conditions for v)                             |
|  PROCESS GEOCHEMISTRY ←—————————————————————————               |
|  (weathering, hydrothermal, ocean chemistry, diagenesis)        |
|   ↑ processes redistribute elements between reservoirs ↑        |
|   ↑ subduction returns crust to mantle; volcanism returns        |
|     mantle material to surface — system is cyclic, not          |
|     a one-way pipeline                                          |
|                                                                  |
+------------------------------------------------------------------+

SUBDISCIPLINES
  Aqueous geochem:   Solution chemistry; speciation; pH/Eh
  Isotope geochem:   Geochronology + paleoclimate proxies
  Organic geochem:   Carbon compounds in sediments
  Cosmochemistry:    Extraterrestrial matter; solar system origin
  Biogeochemistry:   Life ↔ chemistry coupling
  Marine geochem:    Ocean element cycling
  Low-T geochem:     Weathering, diagenesis, soils
  High-T geochem:    Magmatic, hydrothermal, metamorphic
```

---

## Goldschmidt Classification

Victor Goldschmidt's 1937 classification places elements into four groups based on their affinity for different chemical phases during planetary differentiation:

```
GOLDSCHMIDT CLASSIFICATION
===========================

  SIDEROPHILE ("iron-loving")   → Core
  --------------------------
  Fe, Ni, Co, Mo, W, Re, Os, Ir, Pt, Ru, Rh, Pd, Au, Ge (partly)
  High metal/silicate partition coefficient
  Depleted in silicate Earth relative to chondrites

  LITHOPHILE ("rock-loving")    → Mantle + Crust
  ---------------------------
  Si, O, Al, Ca, Mg, Na, K, Ti, Li, Rb, Cs, Sr, Ba, REE, Th, U
  Prefer oxide/silicate phases
  Form the rock-forming minerals

  CHALCOPHILE ("sulfide-loving")→ Sulfide phases
  ----------------------------
  Cu, Zn, Pb, Ag, Cd, Hg, As, Se, Te, S, Bi
  Prefer sulfide over silicate
  Concentrated in sulfide ore deposits

  ATMOPHILE                      → Atmosphere / volatile
  ----------
  H, C, N, O, noble gases (Ne, Ar, Kr, Xe)
  Partition into gas/fluid phases

  RULE:  electronegativity + ionization potential + ionic radius
         → predicts which phase an element prefers
```

The classification is useful but not absolute: many elements are partly in multiple groups (Ge is partly siderophile + lithophile).

---

## Geochemical Reservoirs

```
EARTH'S MAJOR GEOCHEMICAL RESERVOIRS
======================================

  RESERVOIR            MASS (kg)        KEY ELEMENTS
  ---------            ---------        ------------
  Continental crust    2.3 × 10²²       Si, Al, K, Na, Ca (felsic)
  Oceanic crust        6.0 × 10²¹       Mg, Fe, Si, Ca (mafic/basaltic)
  Depleted mantle      3.5 × 10²⁴       Mg, Si, Fe (ultramafic)
  Primitive mantle     (reference)      Assumed = chondritic starting point
  Liquid outer core    1.8 × 10²⁴       Fe, Ni, S, O, H, Si (light elements)
  Inner core           9.7 × 10²²       Fe, Ni (solid)
  Ocean                1.4 × 10²¹       H₂O; Na, Cl, Mg, SO₄, Ca dominant
  Atmosphere           5.1 × 10¹⁸       N₂, O₂, Ar, CO₂, H₂O

  BSE = Bulk Silicate Earth = mantle + crust (everything except the core)
  BSE composition is a key reference: deviations from it reveal fractionation history

  ENRICHMENT / DEPLETION:
    If a reservoir has MORE of an element than BSE → enriched
    If LESS → depleted
    Continental crust: enriched in K, Rb, U, Th, Ba, La vs mantle
    (LILE: large ion lithophile elements — incompatible, extracted into crust)
    Depleted mantle: residue after partial melting → low LILE
```

---

## Partition Coefficients

The geochemical partition coefficient D is formally identical to the distribution coefficient K_D in liquid-liquid extraction chemistry (separatory funnel, solvent extraction columns): D = C_phase1 / C_phase2 at equilibrium. In solvent extraction you choose the organic phase to have high D for the target element; in petrology the "phases" are mineral and melt, and D is set by the crystal field and ionic radius constraints of the mineral lattice. An incompatible element with D << 1 is the geochemical equivalent of a solute that strongly prefers the aqueous phase over the organic phase — it refuses to enter the solid and concentrates in whatever liquid is present.

```
PARTITION COEFFICIENT (D)
==========================

  D = concentration in mineral / concentration in melt

  COMPATIBLE element:    D > 1   (prefers mineral; stays behind during melting)
  INCOMPATIBLE element:  D < 1   (prefers melt; extracted into the magma)

  EXAMPLE (olivine/basaltic melt):
    Ni:  D ~ 4-10    (compatible → stays in mantle)
    Rb:  D ~ 0.0002  (highly incompatible → extracted into crust)
    U:   D ~ 0.0001  (highly incompatible → crust enriched in U)
    Ba:  D ~ 0.0002  (highly incompatible)

  CONSEQUENCE:
    Repeated partial melting events over 4 Ga:
    → Continental crust enriched in incompatible elements (K, U, Th, REE)
    → Residual (depleted) mantle becomes depleted in these elements
    → Ocean island basalts (OIB): tap less-depleted "primitive mantle" plume
    → Mid-ocean ridge basalts (MORB): tap depleted upper mantle

  TRACE ELEMENT PATTERNS:
    Normalized to CI chondrites (primitive solar composition)
    Spider diagrams: show enrichments/depletions across elements
    Subduction signature: Nb-Ta depletion (key diagnostic of arc magmas)
```

---

## Module Map

```
00-OVERVIEW  (this file)
    |
    +-- 01-ELEMENT-DISTRIBUTION    Goldschmidt classification + reservoirs
    |                              Incompatibility, spider diagrams, REE
    |
    +-- 02-ISOTOPE-SYSTEMS         Radiogenic (Rb-Sr, Sm-Nd) + stable isotopes
    |                              Half-lives, decay systems overview
    |
    +-- 03-GEOCHRONOLOGY           U-Pb, Ar-Ar, Re-Os, Sm-Nd dating
    |                              Concordia diagram, isochrons
    |
    +-- 04-STABLE-ISOTOPE-PALEO    δ¹⁸O, δD, δ¹³C as climate proxies
    |                              Paleothermometry, paleohydrology
    |
    +-- 05-CARBON-CYCLE            Long-term C cycle; carbon isotope excursions
    |                              Kerogen, carbonate, organic C
    |
    +-- 06-HYDROTHERMAL            Hydrothermal systems and ore formation
    |                              Black smokers, epithermal, porphyry deposits
    |
    +-- 07-WEATHERING-SOILS        Chemical weathering reactions
    |                              Soil profiles, regolith chemistry
    |
    +-- 08-OCEAN-GEOCHEMISTRY      Marine element cycling
    |                              Residence times, trace metals, proxies
    |
    +-- 09-PLANETARY-GEOCHEMISTRY  Cosmochemistry + solar system geochemistry
                                   Chondrites, CAIs, planetary differentiation
```

---

## Key Analytical Tools

```
GEOCHEMICAL ANALYTICAL METHODS
================================

  ICP-MS (Inductively Coupled Plasma - Mass Spec)
    Gold standard for trace elements + isotope ratios
    Detection limits: ppt-ppb for most elements
    Multi-element: 50+ elements simultaneously

  TIMS (Thermal Ionization Mass Spec)
    High-precision isotope ratio measurement
    Used for: U-Pb, Rb-Sr, Sm-Nd geochronology
    Precision: 0.001-0.01% (10-100 ppm)

  SIMS (Secondary Ion Mass Spec) / Ion Microprobe
    Spatial resolution: ~10-30 μm
    In situ isotope analysis in minerals (e.g., U-Pb in zircon)
    SHRIMP (Sensitive High-Resolution Ion Microprobe): landmark instrument

  LA-ICP-MS (Laser Ablation ICP-MS)
    Laser ablates material from polished grain
    ~20-50 μm spatial resolution
    In situ trace elements + some isotope ratios

  EPMA (Electron Probe Micro-Analyzer)
    Major element composition of minerals
    ~1-2 μm spatial resolution
    Non-destructive; WDS detectors

  ISOTOPE DILUTION (ID):
    Add known amount of enriched spike isotope
    Measure mixed spike+natural ratio
    Back-calculate concentration with very high precision
    Combined with TIMS (ID-TIMS): gold standard for geochronology
```

---

## The Geochemical Detective Framework

```
PROBLEM → SYSTEM → TOOL SELECTION
===================================

  QUESTION                     APPROACH
  --------                     --------
  How old is this rock?        Geochronology (U-Pb, Ar-Ar, Rb-Sr)

  What was ancient temperature? Stable isotope paleothermometry (δ¹⁸O)

  Where did this magma come from? Sr-Nd-Pb isotopes → mantle source
                                   Trace element patterns (spider diagram)

  How did this ore form?         Fluid inclusion T/P; S isotopes; Pb-Pb

  How much CO₂ was ancient atm?  δ¹³C excursions; boron isotopes (pH proxy)

  What is Earth's core made of?  Siderophile element depletion in BSE

  Is this sample contaminated?   Isotope systematics to check
```

---

## Decision Cheat Sheet

| Question | Answer |
|---|---|
| What controls where an element goes during melting? | Partition coefficient D; D>1 = compatible (stays in residue); D<1 = incompatible (enters melt) |
| What is BSE? | Bulk Silicate Earth — mantle + crust; the non-core portion of Earth; used as a reference composition |
| What is a LILE? | Large Ion Lithophile Element (K, Rb, Cs, Sr, Ba, Pb, U, Th) — high charge, large radius, incompatible in most minerals → concentrated in crust |
| What is a HFSE? | High Field Strength Element (Nb, Ta, Zr, Hf, Ti) — high charge/small radius ratio; immobile in fluids; depleted in subduction-zone magmas |
| What does the Nb-Ta depletion signature mean? | Characteristic of subduction zone (arc) magmas; HFSE retained in subducted slab; diagnostic of tectonic setting |
| What does ICP-MS measure? | Elemental concentrations to ppt level and isotope ratios (less precisely than TIMS); multi-element in one run |
| How does cosmochemistry define "primitive"? | Composition close to CI chondrites (carbonaceous chondrites type CI) — best approximation of bulk solar system composition minus volatiles |

---

## Common Confusion Points

**Goldschmidt classification is behavior, not fixed**: Elements don't always go where the rules say. Depends on oxygen fugacity, pressure, temperature. Under reduced conditions (low O₂), more elements become siderophile. In the early Earth's reducing magma ocean, even Cr and Mn had some siderophile character.

**Depleted vs enriched mantle**: "Depleted" mantle is the mantle residue after partial melts have been extracted to form the crust — it's depleted in incompatible elements. "Enriched" mantle (EMII, EMI) has been contaminated by recycled crustal material via subduction. These are different from each other; both are called "mantle."

**Primitive mantle ≠ original mantle**: "Primitive mantle" is a model composition (CI-chondrite-normalized) representing the bulk silicate Earth before continental crust extraction. No rocks today represent primitive mantle; the concept is a geochemical reference.

**CI chondrites are not the most abundant type**: CI chondrites are the most geochemically primitive (closest to solar photosphere composition) but are extremely rare and friable. Ordinary chondrites (H, L, LL) are the most abundant meteorite type. CI composition is used as the reference because it's most pristine, not because it's most common.
