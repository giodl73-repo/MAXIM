---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:disease:overview
kind: guide
module: disease
section: disease
title: Disease - Overview
status: source-custody
source_custody: partial
current_path: disease/00-OVERVIEW.md
canonical_path: disease/00-OVERVIEW.md
backsource_ids: [proof-backfill:disease:00-overview, git-history:disease:00-overview]
concepts: [overview]
root_concepts: [overview]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Disease — Overview

## The Big Picture: Disease Classification

```
DISEASE
┌───────────────────────────────────────────────────────────────────┐
│  INFECTIOUS                  │  NON-INFECTIOUS                    │
│  Exogenous agent required    │  Endogenous or multifactorial      │
│                              │                                    │
│  Bacterial                   │  Neoplastic (cancer)               │
│  Viral                       │  Cardiovascular                    │
│  Fungal                      │  Metabolic / Endocrine             │
│  Parasitic (protozoa +       │  Autoimmune / Inflammatory         │
│    helminths)                │  Genetic / Developmental           │
│  Prion                       │  Neurological / Psychiatric        │
│                              │  Nutritional                       │
│                              │  Iatrogenic (treatment-caused)     │
│                              │  Idiopathic (unknown cause)        │
└───────────────────────────────────────────────────────────────────┘
```

**Systems Bridge:** The infectious/non-infectious split is the same exogenous-versus-endogenous distinction that organizes any fault taxonomy. In software: exogenous faults (bad inputs, network failures, malicious actors) versus endogenous faults (bugs, resource exhaustion, design errors). The same epidemiological triangle (agent + host + environment) describes any system vulnerability: a security exploit requires a vulnerability in the target, an attacker with a capable exploit, and an environment that allows delivery. Germ theory (Koch, 1880s) and cellular pathology (Virchow, 1850s) were competing frameworks: "disease as invader" vs "disease as cellular dysfunction." Both are correct, non-exclusive — exactly as software failures can be both externally triggered and internally amplified.

Most diseases are multifactorial: a genetic predisposition + environmental trigger + host response.
The "infection vs non-infection" binary is also not sharp: H. pylori → peptic ulcer → gastric cancer; HPV → cervical cancer; chronic HBV/HCV → cirrhosis → HCC.

---

## Pathology Fundamentals: Cellular Response to Injury

> **Cross-reference — mechanism depth.** This section is a **compact** summary of the
> cell-injury, inflammation, and hemodynamic fundamentals, sized for the disease catalog. The
> standalone, mechanism-first treatment at peer depth lives in the `pathology/` module:
> [`pathology/01-CELL-INJURY-ADAPTATION-AND-DEATH.md`](../pathology/01-CELL-INJURY-ADAPTATION-AND-DEATH.md),
> [`pathology/02-INFLAMMATION-AND-TISSUE-REPAIR.md`](../pathology/02-INFLAMMATION-AND-TISSUE-REPAIR.md),
> and [`pathology/03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK.md`](../pathology/03-HEMODYNAMIC-DISORDERS-THROMBOSIS-AND-SHOCK.md).
> `disease/` owns the disease **entities**; `pathology/` owns the general **mechanism**.

### Reversible vs Irreversible Injury

```
CELL INJURY STIMULUS (hypoxia, toxin, pathogen, trauma)
         ↓
REVERSIBLE INJURY:
  ↓ ATP → Na/K-ATPase fails → Na⁺ + water enter → cell swelling (hydropic change)
  ER swells → ribosomes detach → ↓ protein synthesis
  Mitochondria swell (reversible)
  Fatty change (lipid accumulation) in hepatocytes
  → Remove stimulus → cell recovers

         ↓ (if stimulus continues or severe)
IRREVERSIBLE INJURY:
  Point of no return markers:
    Massive mitochondrial dysfunction → membrane permeability transition pore (mPTP) opens
    Plasma membrane damage → Ca²⁺ floods in → phospholipases + proteases activated
    Lysosome rupture → hydrolases released → autolysis

IRREVERSIBLE INJURY → CELL DEATH (two modes)
```

### Apoptosis vs Necrosis

```
                    APOPTOSIS                   NECROSIS
Purpose             Programmed, controlled      Accidental, pathological
Trigger             Intrinsic (DNA damage,       Ischemia, toxins, infection,
                    withdrawal signals) or       severe injury
                    Extrinsic (death receptors)
Cell size           Shrinks                      Swells
Membrane            Intact until fragmentation   Ruptures
DNA                 Ladder pattern (~180 bp       Random degradation
                    fragments — endonuclease)
Contents            Packaged in apoptotic bodies  Released → inflammation
                    → phagocytosed cleanly
Inflammation        None (anti-inflammatory)      Yes (DAMP release)
Energy              ATP-dependent                 Passive

NECROSIS TYPES:
  Coagulative: most organs — architecture preserved, cells "ghost-like" (ischemia)
  Liquefactive: brain (lots of hydrolases), abscesses (pus)
  Caseous: TB — "cheesy" center, surrounded by granuloma (macrophages + giant cells)
  Fat necrosis: pancreatic enzymes liquefy mesenteric fat → chalky deposits (saponification)
  Gangrenous: coagulative + secondary bacterial decomposition → wet or dry gangrene
  Fibrinoid: immune-complex deposition in vessel walls (SLE, polyarteritis nodosa)
```

### Intrinsic Apoptosis Pathway

```
DNA damage / oxidative stress / ER stress / growth factor withdrawal
  ↓
↑ Proapoptotic BCL-2 family members (BAX, BAK, BID)
↓ Antiapoptotic (BCL-2, BCL-XL, MCL-1)
  ↓
Mitochondrial outer membrane permeabilization (MOMP)
  ↓
Cytochrome c release → APAF-1 → Apoptosome → Caspase-9 → Caspase-3
  ↓
Execution: DNA fragmentation, cytoskeletal cleavage, PS flip → phagocytosis signal

BCL-2 overexpression (t(14;18) in follicular lymphoma): blocks apoptosis → accumulation
Venetoclax (BCL-2 inhibitor): restores apoptosis in CLL/AML — precision oncology target
```

### Extrinsic Apoptosis

Death receptor pathway (Fas/FasL, TRAIL/DR4-5, TNF/TNFR1):
- Ligand → receptor trimerization → DISC (death-inducing signaling complex) → caspase-8 → caspase-3
- Immune system uses this to kill target cells (CTL Fas-FasL) and to delete activated lymphocytes (AICD)

---

## Cellular Adaptations

The cell between normal and irreversible injury:

```
ATROPHY: ↓ cell size (↓ workload, ↓ blood supply, denervation, aging)
  E.g., muscle atrophy in cast/bedrest; brain atrophy in Alzheimer's

HYPERTROPHY: ↑ cell size, not number (non-dividing cells: cardiac muscle, neurons)
  E.g., LV hypertrophy in hypertension; skeletal muscle in exercise

HYPERPLASIA: ↑ cell number (dividing cells) in response to ↑ demand or hormonal
  E.g., endometrial hyperplasia from excess estrogen; benign prostatic hyperplasia

METAPLASIA: replacement of one adult cell type by another (reversible)
  Usually stress-adaptive, but cancer risk if sustained:
  E.g., Barrett's esophagus (squamous → columnar) — acid reflux → adenocarcinoma risk
  Squamous metaplasia in bronchus (smoking) → squamous cell carcinoma risk

DYSPLASIA: disordered growth — abnormal cells, not yet invasive
  Pre-cancerous: CIN (cervical intraepithelial neoplasia — HPV), Barrett's with dysplasia
  Loss of architecture, nuclear atypia, mitotic figures
  → Carcinoma in situ (CIS) → invasive carcinoma
```

---

## Inflammation: Acute and Chronic

### Acute Inflammation

Neutrophil-dominated response to infection/injury (hours to days):

```
CARDINAL SIGNS: Rubor (redness) + Calor (warmth) + Tumor (swelling) + Dolor (pain) + Functio laesa

MEDIATOR SOURCES:
  Preformed (immediate): histamine (mast cells), serotonin (platelets), lysosomal enzymes
  Synthesized (minutes): prostaglandins (COX-1/2), leukotrienes (5-LOX), PAF, nitric oxide
  Complement/kinin: C3a/C5a (anaphylatoxins), bradykinin (pain, vasodilation)
  Cytokines (later): TNF-α, IL-1β, IL-6 → systemic effects (fever, acute phase response)

OUTCOMES:
  Complete resolution (most bacterial infections with adequate response)
  Abscess formation (contained suppurative collection)
  Chronic inflammation (persistent stimulus)
  Fibrosis/scarring (extensive tissue damage → activated fibroblasts → collagen)
```

### Chronic Inflammation

Mononuclear cell–dominated (macrophages, lymphocytes, plasma cells):
- Simultaneous destruction + repair
- Results from: persistent infection (TB, H. pylori), foreign material (sutures, silica), autoimmune disease

**Granulomatous inflammation**: macrophage aggregates forming nodules:
```
Activated macrophages (epithelioid cells) + multinucleate giant cells
  (formed by macrophage fusion — too large to phagocytose agent)
Center: caseous necrosis (TB) or no necrosis (sarcoid, foreign body)

Causes: TB (Mycobacterium), sarcoidosis (unknown antigen), Crohn's disease,
        berylliosis, histoplasmosis, cat-scratch disease, leprosy
```

---

## Koch's Postulates (Classical and Molecular)

**Koch's classical postulates (1884):**
1. Organism must be present in all cases of disease
2. Must be isolated from diseased host and grown in pure culture
3. Cultured organism must cause disease in healthy host
4. Must be re-isolated from experimentally diseased host and match original

**Limitations/molecular revisions:**
- Many pathogens not culturable (H. pylori was finally cultured 1982 by Marshall and Warren)
- Viruses cannot be grown in "pure culture" by Koch's definition
- Commensal organisms can cause opportunistic disease
- Microbiome — "organism present in all cases" is no longer binary

**Molecular Koch's postulates (Falkow, 1988):**
1. Virulence gene associated with pathogenic strains, absent from non-pathogenic
2. Inactivation of virulence gene reduces pathogenicity
3. Restoration of virulence gene restores pathogenicity

---

## Host-Pathogen-Environment Triad (Epidemiological Triangle)

```
              HOST
           /        \
          /    →      \
    AGENT    ←    ENVIRONMENT
```

Disease occurs when:
- **Agent**: sufficient exposure to pathogen or sufficient pathogen virulence
- **Host**: adequate susceptibility (immune status, genetics, nutritional state)
- **Environment**: conditions that facilitate transmission (crowding, sanitation, climate)

All three must align. Changing any vertex breaks the triangle and reduces disease.

---

## Cellular Pathology Lab Markers

| Analyte | Source | Clinical meaning |
|---------|--------|-----------------|
| Troponin I/T | Cardiomyocyte | Myocardial necrosis (MI) |
| CK-MM | Skeletal muscle | Rhabdomyolysis |
| ALT/AST | Hepatocytes | Hepatocellular injury (ALT more liver-specific) |
| GGT | Bile duct cells | Cholestasis, alcohol |
| LDH | All cells | Non-specific necrosis; also hemolysis |
| Creatinine | Muscle (filtration marker) | Renal function |
| Amylase/lipase | Pancreatic acinar | Pancreatitis |
| CRP | Liver (acute phase) | Inflammation marker |
| Ferritin | All cells (stored Fe) | Acute phase reactant; iron overload |
| β-hCG | Trophoblast | Pregnancy; germ cell tumors |
| PSA | Prostate epithelium | Prostate cancer screening (low specificity) |

---

## Global Burden of Disease

```
LEADING CAUSES OF DEATH GLOBALLY (GBD 2019 data):
  1. Ischemic heart disease (~9M deaths/year)
  2. Stroke (~6M)
  3. Chronic obstructive pulmonary disease (~3M)
  4. Lower respiratory infections (~2.6M)
  5. Neonatal disorders (~2M)
  6. Trachea/bronchus/lung cancer (~1.8M)
  7. Alzheimer's/other dementia (~1.6M)
  8. Diarrhoeal diseases (~1.5M)
  9. Diabetes (~1.4M)
  10. Kidney disease (~1.3M)

HIGH-INCOME vs LOW/MIDDLE-INCOME:
  LMIC: higher burden from communicable disease, neonatal, nutritional
  HIC: overwhelmingly non-communicable (CVD, cancer, dementia)

DALY (Disability-Adjusted Life Year):
  DALY = YLL (years of life lost to premature death) + YLD (years lived with disability)
  1 DALY = 1 year of healthy life lost
  More policy-useful than mortality alone: captures morbidity (depression, low back pain)
```

---

## Decision Cheat Sheet

| If you need to diagnose... | Start With | Key Caveat |
|---|---|---|
| Whether injury is reversible | Look for hydropic change, membrane integrity, mitochondrial recovery, stimulus duration, and return of ATP-dependent transport. | Reversible injury can tip into necrosis or apoptosis if the stress persists. |
| A necrosis pattern | Match morphology to mechanism: coagulative ischemia, liquefactive abscess/CNS, caseous granuloma, fat saponification, or fibrinoid vessel injury. | Morphology narrows the cause; it rarely proves the upstream etiology alone. |
| An inflammatory infiltrate | Separate neutrophil-predominant acute inflammation, mononuclear chronic inflammation, granulomatous response, and immune-complex vasculitis. | Time course, organism, tissue, and host immune state can blur the classic categories. |
| Infectious vs non-infectious disease | Ask whether an organism, toxin, immune reaction, metabolic failure, vascular event, neoplasm, or genetic defect explains the lesion. | Koch-style causal thinking helps, but many diseases are multifactorial or unculturable. |
| A neoplastic process | Check invasion, clonality, proliferation control, differentiation, metastasis, and host/tissue context. | Hyperplasia and dysplasia are not the same as invasive cancer. |
| A population-burden claim | Separate incidence, prevalence, CFR, IFR, age structure, income setting, risk exposure, and surveillance quality. | High-income and low-income burden patterns differ; development shifts dominant categories rather than eliminating disease. |

**Global burden anchor:** From the landscape diagram above, non-infectious disease dominates many high-income mortality profiles, while infectious, maternal/neonatal, and exposure-linked diseases remain heavier in many low- and middle-income settings. Public health, sanitation, vaccination, nutrition, and chronic-disease risk transitions shift the dominant category mix over time.

---

## Module Map

| Module | Category | Key concepts |
|--------|----------|--------------|
| `01-BACTERIAL.md` | Infectious | Gram staining, virulence, ESKAPE, resistance |
| `02-VIRAL.md` | Infectious | Baltimore classification, HIV, influenza, oncogenic viruses |
| `03-FUNGAL-PARASITIC-PRION.md` | Infectious | Opportunistic fungi, malaria, prion mechanism |
| `04-CANCER.md` | Neoplastic | Hallmarks, oncogenes/TSGs, metastasis, staging |
| `05-CARDIOVASCULAR-DISEASE.md` | CV | Atherosclerosis, MI, HF, arrhythmias, stroke |
| `06-METABOLIC-ENDOCRINE.md` | Metabolic | Diabetes, metabolic syndrome, thyroid, adrenal |
| `07-AUTOIMMUNE-INFLAMMATORY.md` | Immune | RA, SLE, MS, IBD, psoriasis |
| `08-NEUROLOGICAL-PSYCHIATRIC.md` | Neuro/Psych | Alzheimer's, Parkinson's, epilepsy, depression, schizophrenia |
| `09-GENETIC-DEVELOPMENTAL.md` | Genetic | Chromosomal, single-gene disorders, teratogens |
| `10-EPIDEMIOLOGY.md` | Public Health | R₀, study designs, outbreak investigation |

---

## Cross-References

- `01-BACTERIAL.md` starts the pathogen-specific disease sequence.
- `04-CANCER.md` shows disease as dysregulated growth and selection.
- `10-EPIDEMIOLOGY.md` connects disease mechanisms to population evidence and causal inference.

## Common Confusion Points

**Neoplasia vs hyperplasia vs hypertrophy**
Hypertrophy/hyperplasia: adaptive, controlled, reversible. Neoplasia: autonomous, heritable growth alteration, irreversible. Hyperplasia can progress to dysplasia to neoplasia — but they are distinct.

**Prognosis vocabulary**
- Morbidity: illness/disability caused by disease
- Mortality: death rate
- Incidence: new cases/time/population
- Prevalence: all existing cases at a time point
- CFR (case fatality rate): deaths/confirmed cases (denominator includes only diagnosed)
- IFR (infection fatality rate): deaths/all infected (denominator includes subclinical — always lower than CFR)

**Malignant vs benign neoplasm**
Not purely about size or speed. Key distinction: **invasion** and **metastasis** capability.
- Benign: locally confined, often encapsulated, cytologically bland
- Malignant: invades basement membrane, can metastasize

**Iatrogenic disease**
Caused by medical treatment itself. 5th most common cause of death in some analyses: drug adverse effects, hospital-acquired infections (HAIs), procedural complications. "First do no harm" has quantitative weight.
