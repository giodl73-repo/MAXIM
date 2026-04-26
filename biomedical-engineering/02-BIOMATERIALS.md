# Biomaterials — Materials for Medical Implants

## The Big Picture

A biomaterial is any material intended to interface with a biological system for a medical
purpose. The central constraint: the material must be biocompatible — it must not harm the
host, and must perform its mechanical function for the device's intended lifetime.

```
+---------------------------------------------------------------------+
|              BIOMATERIALS — LANDSCAPE                               |
+---------------------------------------------------------------------+
|                                                                     |
|  METALS              CERAMICS           POLYMERS        COMPOSITES  |
|  ------              --------           --------        ----------  |
|  316L SS             Hydroxyapatite     UHMWPE          CF/PEEK     |
|  Ti-6Al-4V           Alumina (Al2O3)    PEEK            HA/polymer  |
|  CoCrMo              Zirconia (ZrO2)    PLGA/PLA/PCL                |
|  Nitinol             Bioglass           Silicone                    |
|                      TCP               PMMA                        |
|       |                    |                    |                   |
|       +--------------------+--------------------+                   |
|                            |                                        |
|                     BIOCOMPATIBILITY                                |
|                     ISO 10993 test battery                          |
|                     Host response: protein adsorption ->            |
|                     macrophage -> encapsulation or integration      |
|                                                                     |
|       SURFACE MODIFICATION          DEGRADATION MECHANISMS          |
|       Plasma, anodization,          Corrosion, hydrolysis,          |
|       RGD grafting, HA coating      wear, oxidation                 |
+---------------------------------------------------------------------+
```

---

## Metals

Metals dominate load-bearing implant applications because of their high strength, toughness,
and fatigue resistance. The challenge is corrosion, ion release, and MRI compatibility.

### 316L Stainless Steel

```
  316L STAINLESS STEEL
  ====================
  316L = 18% Cr, 14% Ni, 3% Mo, low carbon ("L")
  The Mo addition resists crevice corrosion vs. standard 316

  +------------------+------------------------------------------+
  | Property         | Value                                    |
  +------------------+------------------------------------------+
  | Young's modulus  | ~200 GPa (10x stiffer than cortical bone)|
  | Yield strength   | 170-690 MPa (cold work dependent)        |
  | UTS              | 480-860 MPa                              |
  | Fatigue (10^7)   | ~300 MPa                                 |
  | Corrosion        | Passive Cr2O3 layer                      |
  | MRI              | Ferromagnetic — NOT MRI compatible!      |
  +------------------+------------------------------------------+

  Applications: Temporary fixation hardware (bone plates, screws,
  intramedullary nails, external fixators). The standard for
  fracture fixation where retrieval is planned.
  NOT used for permanent implants (ion release, MRI incompatibility).
```

### Ti-6Al-4V

The workhorse of permanent implants — excellent biocompatibility, osseointegration, MRI
conditional, and high strength-to-weight ratio.

```
  Ti-6Al-4V (Grade 5 Titanium Alloy)
  ====================================
  Alpha-beta alloy: 6% Al (alpha stabilizer) + 4% V (beta stabilizer)

  +------------------+------------------------------------------+
  | Property         | Value                                    |
  +------------------+------------------------------------------+
  | Young's modulus  | ~114 GPa (vs. 200 GPa for steel)         |
  | Yield strength   | 880-1100 MPa                             |
  | Fatigue (10^7)   | ~500 MPa                                 |
  | Corrosion        | TiO2 passive layer — excellent           |
  | Osseointegration | YES — titanium is one of few materials   |
  |                  | that bone bonds to directly              |
  | MRI              | MRI conditional — weak ferromagnetism    |
  | Density          | 4.43 g/cm3 (vs. 7.9 for steel)          |
  +------------------+------------------------------------------+

  Applications: Cementless hip/knee implants, spinal cages, dental
  implants, bone screws, pacemaker housings.
  Ti-6Al-4V ELI (extra-low interstitials): better fatigue for
  fracture-critical applications (orthopedic stems).

  Osseointegration mechanism: TiO2 surface -> protein adsorption ->
  osteoblast differentiation -> bone grows directly onto implant surface.
  No fibrous capsule — direct bone-implant contact at 6-12 weeks.
```

### CoCrMo

The gold standard for articulating surfaces — best wear resistance of all metallic implant
materials.

```
  CoCrMo (ASTM F75 / F799)
  =========================
  Cast (F75) or wrought/forged (F799)

  +------------------+------------------------------------------+
  | Property         | Value                                    |
  +------------------+------------------------------------------+
  | Young's modulus  | ~230 GPa                                 |
  | Yield strength   | 450-1030 MPa                             |
  | UTS              | 655-1200 MPa                             |
  | Fatigue (10^7)   | ~300-500 MPa                             |
  | Hardness         | High — excellent wear resistance         |
  | Corrosion        | Cr2O3 passive layer                      |
  | Ion release      | Co, Cr, Mo ions at wear surfaces         |
  | MRI              | NOT compatible (ferromagnetic)           |
  +------------------+------------------------------------------+

  Applications: Femoral head of hip implants, tibial knee implants,
  hip resurfacing. Metal-on-metal (MoM) bearings fell out of favor
  due to elevated systemic Co/Cr ion levels and ARMD (adverse
  reaction to metal debris).
  Now primarily: metal-on-polyethylene (UHMWPE)
```

### Nitinol (Nickel-Titanium Shape Memory Alloy)

```
  NITINOL — SUPERELASTIC AND SHAPE MEMORY
  ========================================
  ~55% Ni, ~45% Ti. Transformation temperature tunable by composition.

  Two effects:
  SUPERELASTIC (at body temperature):
    Stress-induced martensite -> strain up to 8% recoverable
    Application: self-expanding stents, endovascular devices
    Stent compressed in catheter -> body temperature opens it

  SHAPE MEMORY:
    Deform in martensite phase -> heat above Af -> returns to shape
    Application: orthodontic archwires (body heat activates)

  Biocompatibility concern: Ni content; TiO2 surface passivation
  limits Ni release significantly.
```

---

## Ceramics

Ceramics are brittle but excel in wear resistance, hardness, and chemical inertness. Used
where these properties outweigh the brittleness risk.

```
  CERAMIC BIOMATERIALS
  ====================

  BIOINERT: no significant chemical interaction with tissue
  +---------+---------+--------------------+------------------+
  | Material| Al2O3   | ZrO2 (zirconia)    | Notes            |
  |         | Alumina | stabilized         |                  |
  +---------+---------+--------------------+------------------+
  | Modulus | 380 GPa | 200 GPa            | Very stiff       |
  | Hardness| 2000 HV | 1200 HV            | Excellent wear   |
  | KIC     | 3-4     | 6-10 MPa√m         | ZrO2 tougher    |
  | Use     | Femoral | Femoral head,      |                  |
  |         | head,   | dental crowns      |                  |
  |         | bearing | (white, esthetic)  |                  |
  +---------+---------+--------------------+------------------+
  Ceramic-on-ceramic bearings: lowest wear of any combination
  Catastrophic failure risk: brittle fracture (rare, ~0.01%)

  BIOACTIVE: bonds chemically to bone
  +--------------------+------------------------------------------+
  | Hydroxyapatite     | Ca10(PO4)6(OH)2                          |
  | (HA)               | Chemical composition of bone mineral     |
  |                    | Directly bonds to bone (osseoconductive) |
  |                    | Used as: coating on Ti implants,         |
  |                    |   porous scaffold material               |
  |                    | Sintered HA: brittle, limited structural  |
  +--------------------+------------------------------------------+
  | Bioglass (45S5)    | SiO2-Na2O-CaO-P2O5                       |
  |                    | Forms HA layer on surface in body fluid  |
  |                    | Bonds to both bone AND soft tissue       |
  |                    | Oseoconductive + osteostimulatory        |
  +--------------------+------------------------------------------+

  BIORESORBABLE CERAMICS:
  Beta-TCP (tricalcium phosphate): resorbs over 6-18 months
  as bone grows in. Used as bone graft substitute.
```

---

## Polymers

Wide range — from inert structural materials (UHMWPE, PEEK) to degradable scaffolds (PLGA).

```
  POLYMER BIOMATERIALS — TAXONOMY
  ================================

  NON-DEGRADABLE               DEGRADABLE
  =============                =========
  UHMWPE   PEEK    Silicone    PLGA    PLA    PCL    PHBV
  (joints) (spine) (soft)     (drug/  (bone  (long   (tissue
                               scaffold)screws) deg)  eng)

  +-----------+--------------------------------------------------+
  | UHMWPE    | Ultra-high molecular weight polyethylene         |
  | (GUR 1020)| Mw > 3.5 million g/mol                           |
  |           | Young's modulus: 0.6-1 GPa (soft, absorbs shock) |
  |           | Excellent wear resistance (acetabular cups,      |
  |           | tibial knee inserts)                             |
  |           | Cross-linked UHMWPE: even better wear (2000s+)   |
  |           | Vitamin E UHMWPE: oxidation-stabilized           |
  +-----------+--------------------------------------------------+
  | PEEK      | Polyetheretherketone                             |
  | (Victrex) | Young's modulus: 3.5-4.5 GPa                    |
  |           | (closer to bone than metal — less stress shield) |
  |           | Radiolucent (can see bone healing on X-ray)      |
  |           | Applications: spinal interbody cages, cranial    |
  |           |   implants, trauma fixation                      |
  |           | Not naturally osseointegrating — needs surface   |
  |           | modification or HA coating                       |
  +-----------+--------------------------------------------------+
  | PMMA      | Polymethylmethacrylate — "bone cement"           |
  |           | Exothermic polymerization in situ                |
  |           | Fills interface gap in cemented arthroplasty     |
  |           | Brittle: KIC ~1-2 MPa√m                          |
  |           | Fatigue failure at cement-implant interface      |
  |           |   over 10-15 years (revision trigger)            |
  +-----------+--------------------------------------------------+
  | Silicone  | Polydimethylsiloxane (PDMS)                      |
  |           | Excellent elasticity, biocompatible soft tissue  |
  |           | Breast implants, finger/toe joint implants       |
  |           | Silicone gel: risk of capsular contracture       |
  +-----------+--------------------------------------------------+

  DEGRADABLE POLYMERS:
  +-----------+--------------------------------------------------+
  | PLGA      | Poly(lactic-co-glycolic acid)                    |
  |           | Degradation: hydrolysis of ester bonds -> LA + GA|
  |           | Tunable degradation: PLGA 50:50 -> ~3 months     |
  |           |                      PLGA 85:15 -> ~12 months    |
  |           | Applications: drug delivery microspheres,        |
  |           |   tissue engineering scaffolds, absorbable sutures|
  +-----------+--------------------------------------------------+
  | PLA       | Poly(lactic acid)                                |
  |           | PLLA (crystalline, stronger) vs. PDLA (amorphous)|
  |           | Absorbable bone screws/pins (3-4 year resorption) |
  +-----------+--------------------------------------------------+
  | PCL       | Poly(caprolactone) — very slow degradation       |
  |           | ~2-4 years. Electrospun scaffolds, long-term     |
  |           | drug delivery                                    |
  +-----------+--------------------------------------------------+
```

---

## Biocompatibility — ISO 10993

ISO 10993-1 risk-based framework: the test battery is selected based on nature and duration
of contact (surface/external communicating/implant) and contact duration.

```
  ISO 10993 TEST SELECTION MATRIX
  ================================

  Contact Type:                  Duration:
  Surface contacting             < 24h (limited)
  External communicating         24h - 30d (prolonged)
  Implant                        > 30d (permanent)

  Tests (selected by risk):
  +---------------------------+------+----------+-----------+
  | Test                      |Surf. |Ext.Comm. |Implant    |
  +---------------------------+------+----------+-----------+
  | Cytotoxicity (10993-5)    |  X   |    X     |    X      |
  | Sensitization (10993-10)  |  X   |    X     |    X      |
  | Irritation (10993-10)     |  X   |    X     |    X      |
  | Systemic toxicity         |      |    X     |    X      |
  | Subchronic toxicity       |      |          |    X      |
  | Genotoxicity (10993-3)    |  X   |    X     |    X      |
  | Implantation (10993-6)    |      |          |    X      |
  | Hemocompatibility         |      |    X     |    X(blood)|
  | Chronic toxicity          |      |          | permanent |
  | Carcinogenicity           |      |          | permanent |
  | Reproductive toxicity     |      |          | if relevant|
  +---------------------------+------+----------+-----------+
```

### Host Response Cascade

```
  HOST RESPONSE TO IMPLANT
  =========================

  SECONDS:
  Protein adsorption to implant surface
  -> Fibronectin, vitronectin, albumin, IgG
  -> Pattern of adsorption shapes all subsequent cellular responses
  -> THIS is why surface chemistry matters enormously

  MINUTES TO HOURS:
  Platelet adhesion and activation (if blood-contacting)
  -> Coagulation cascade
  -> Complement activation (innate immunity)

  HOURS TO DAYS:
  Neutrophil recruitment (acute inflammation)
  Monocyte recruitment -> differentiate to macrophages
  Macrophages attempt to phagocytose the implant
  -> Too large to phagocytose: frustrated phagocytosis
  -> Release reactive oxygen species, degradative enzymes

  WEEKS:
  Macrophage fusion -> Foreign Body Giant Cells (FBGCs)
  Fibroblast recruitment
  Granulation tissue formation
  -> Angiogenesis into granulation tissue

  MONTHS TO YEARS:
  OPTION A — Fibrous encapsulation (most implants)
  Collagen capsule isolates implant from host
  Capsule thickness indicates chronic inflammation severity

  OPTION B — Integration (osseointegration, tissue ingrowth)
  Bone or tissue grows into implant
  Only some materials / surface conditions enable this

  DETERMINANTS of outcome:
  Surface chemistry, topography, charge, hydrophilicity,
  release of degradation products, implant motion
```

---

## Surface Modification

Surface modification changes the implant-tissue interface without changing bulk material
properties. Most critical factor in determining biocompatibility outcome.

```
  SURFACE MODIFICATION APPROACHES
  ================================

  PHYSICOCHEMICAL:
  +-----------------+------------------------------------------------+
  | Plasma treatment| Low-pressure O2/N2/Ar plasma                   |
  |                 | Removes contamination, increases hydrophilicity |
  |                 | Adds functional groups (-OH, -NH2, -COOH)      |
  |                 | for subsequent biofunctionalization            |
  +-----------------+------------------------------------------------+
  | Acid etching    | HCl/H2SO4 creates microroughness              |
  |                 | Increases surface area, improves cell adhesion  |
  +-----------------+------------------------------------------------+
  | Anodization     | Electrochemical TiO2 thickening on titanium    |
  |                 | Controls oxide layer structure (amorphous,     |
  |                 | anatase, rutile — anatase best for osseointegr.)|
  |                 | Nanotube arrays: dramatically improves         |
  |                 | osteoblast differentiation                     |
  +-----------------+------------------------------------------------+
  | Grit blasting   | Al2O3 or TiO2 particles create macro-roughness |
  |                 | Standard for cementless implant surfaces (SLA:  |
  |                 | sand-blasted acid-etched — Straumann standard)  |
  +-----------------+------------------------------------------------+

  COATINGS:
  +-----------------+------------------------------------------------+
  | HA plasma spray | Plasma-sprayed hydroxyapatite coating           |
  |                 | 50-150 μm thick, promotes rapid bone ingrowth   |
  |                 | Risk: coating delamination under shear          |
  +-----------------+------------------------------------------------+
  | Drug eluting    | PLGA or other polymer loaded with drug         |
  |                 | Drug-eluting stents (paclitaxel/sirolimus)     |
  |                 | Antibiotic-eluting bone cement                 |
  +-----------------+------------------------------------------------+
  | Anti-fouling    | PEG (polyethylene glycol) brush coating         |
  | PEG             | Resists protein adsorption (steric hindrance)   |
  |                 | Reduces platelet activation on blood-contacting |
  |                 | devices, catheter surfaces                      |
  +-----------------+------------------------------------------------+

  BIOFUNCTIONALIZATION:
  +-----------------+------------------------------------------------+
  | RGD peptides    | Arg-Gly-Asp integrin-binding sequence from      |
  |                 | fibronectin, vitronectin                        |
  |                 | Covalently grafted to surface                   |
  |                 | Enhances osteoblast/fibroblast adhesion         |
  +-----------------+------------------------------------------------+
  | BMP-2 immobil.  | Bone morphogenetic protein-2 immobilized       |
  |                 | Osteoinductive signal at implant surface       |
  |                 | Experimental — concern about ectopic bone      |
  +-----------------+------------------------------------------------+
```

---

## Degradation Mechanisms

Understanding how implant materials fail over time is as important as their initial properties.

```
  DEGRADATION MECHANISMS
  ======================

  METALS:
  +-----------------+---------------------------------------------+
  | General         | Uniform material loss in electrolyte        |
  | corrosion       | Rare with passive oxide layer               |
  +-----------------+---------------------------------------------+
  | Galvanic        | Two different metals in ionic solution       |
  | corrosion       | Anodic metal (less noble) corrodes          |
  |                 | 316L SS + Ti-6Al-4V: Ti is cathode ->       |
  |                 | SS corrodes. NEVER mix metals in implants.  |
  +-----------------+---------------------------------------------+
  | Crevice         | Depleted O2 in crevice destroys passive     |
  | corrosion       | layer locally. Screw-plate interfaces.      |
  +-----------------+---------------------------------------------+
  | Pitting         | Local passive layer breakdown               |
  +-----------------+---------------------------------------------+
  | Fretting        | Micromotion at modular junctions +          |
  | corrosion       | corrosion = tribocorrosion.                 |
  |                 | Taper junctions in total hip replacements.  |
  |                 | Generates metal debris + ions locally.      |
  +-----------------+---------------------------------------------+

  POLYMERS:
  +-----------------+---------------------------------------------+
  | Hydrolysis      | Water breaks ester/amide bonds              |
  |                 | PLGA, PLA, PCL — designed to degrade        |
  |                 | UHMWPE — does NOT hydrolyze                 |
  +-----------------+---------------------------------------------+
  | Oxidation       | Reactive oxygen species from macrophages    |
  |                 | UHMWPE oxidation -> chain scission ->       |
  |                 | embrittlement (solved by cross-linking +    |
  |                 | Vitamin E stabilization)                    |
  +-----------------+---------------------------------------------+
  | Wear            | UHMWPE in joint articulation                |
  |                 | Adhesive wear (asperity contact)            |
  |                 | Abrasive wear (hard particle plowing)       |
  |                 | Wear debris -> macrophage activation ->     |
  |                 | osteolysis -> aseptic loosening             |
  +-----------------+---------------------------------------------+

  CERAMICS:
  +-----------------+---------------------------------------------+
  | Low-temp        | Hydrothermal degradation of Y-TZP zirconia  |
  | degradation     | (ageing): tetragonal -> monoclinic at       |
  |                 | low temps in water. Surface roughening.     |
  |                 | Addressed by alumina-toughened zirconia.    |
  +-----------------+---------------------------------------------+
```

---

## Common Confusion Points

**Biocompatibility is not a single pass/fail test**: ISO 10993-1 risk-based approach means
the test battery changes with device contact type and duration. A surgical instrument needs
fewer tests than a permanent cardiovascular implant. Companies sometimes over- or under-test
because they don't properly classify their device first.

**Osseointegration vs. fibrous encapsulation**: Most implants get encapsulated (isolated by
collagen scar tissue). Only titanium (and some ceramics/bioactive glasses) achieve true
osseointegration where bone grows directly onto the implant. Osseointegration requires both the
right material surface AND initial mechanical stability — micromotion >150 μm during healing
prevents it.

**Cross-linked UHMWPE tradeoff**: Cross-linking dramatically reduces wear but reduces
toughness and fatigue crack resistance. First-generation highly cross-linked UHMWPE had some
fatigue fractures in thin acetabular liners. Vitamin E stabilization plus moderate cross-linking
is the current compromise.

**MRI compatibility vs. MRI conditional**: MRI safe = no known hazards in any MRI environment.
MRI conditional = safe under specific conditions (field strength, gradient, SAR limits).
MRI unsafe = known hazards. Most metallic implants are "MRI conditional" not "MRI safe."
Stainless steel (316L) — used in surgical instruments and temporary fixation — is NOT MRI
compatible because it is ferromagnetic.

**Degradation timescales**: PLGA 50:50 degrades in ~3 months; PLGA 85:15 ~6-12 months; PLA ~1-2
years; PCL ~2-4 years. Choosing wrong degradation rate relative to tissue healing rate leads to
premature loss of mechanical support (scaffold collapses before tissue forms) or persistent
foreign body response (scaffold outlasts need).

---

## Decision Cheat Sheet — Material Selection

| Application | Primary Choice | Rationale |
|---|---|---|
| Fracture fixation plate (temporary) | 316L SS or Ti-6Al-4V | Stiffness, strength, removal planned |
| Cementless hip stem (permanent) | Ti-6Al-4V (porous-coated) | Osseointegration, MRI conditional |
| Hip femoral head bearing | CoCrMo or alumina (ceramic) | Wear resistance |
| Acetabular cup liner | UHMWPE (cross-linked + Vit. E) | Low wear, toughness |
| Spinal interbody cage | PEEK or Ti-6Al-4V (porous) | Radiolucency, stiffness matching |
| Dental implant | Ti-6Al-4V or Ti Grade 4 | Osseointegration |
| Absorbable bone screw | PLLA or PLGA composite | Degrades as bone heals |
| Drug delivery scaffold | PLGA (tunable degradation) | Releases drug as it degrades |
| Self-expanding stent | Nitinol | Superelastic, MRI conditional |
| Balloon-expanded stent | CoCrMo or 316L SS | High radial strength |
| Soft tissue implant | Silicone | Elasticity, bioinert |
| Bone graft substitute | Beta-TCP or HA | Resorbable, osteoconductive |
