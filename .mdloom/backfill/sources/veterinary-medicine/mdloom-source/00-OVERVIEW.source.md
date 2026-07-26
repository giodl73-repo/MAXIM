---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "00-OVERVIEW.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:veterinary-medicine:overview
kind: guide
module: veterinary-medicine
section: veterinary-medicine
title: Veterinary Medicine - Landscape, Scope, and One Health
status: source-custody
source_custody: partial
current_path: veterinary-medicine/00-OVERVIEW.md
canonical_path: veterinary-medicine/00-OVERVIEW.md
backsource_ids: [mdloom-backfill:veterinary-medicine:00-overview, git-history:veterinary-medicine:00-overview]
concepts: [overview]
root_concepts: [overview]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Veterinary Medicine — Landscape, Scope, and One Health

```
+-----------------------------------------------------------------------------+
|                        THE VETERINARY PROBLEM SPACE                         |
|                                                                             |
|   ONE PHYSICIAN, ONE SPECIES         ONE VETERINARIAN, MANY SPECIES         |
|   --------------------------         ---------------------------------      |
|   Homo sapiens only.                 Dog, cat, horse, cow, pig, chicken,    |
|   ~70 kg adult baseline.             parrot, snake, koi, honeybee, tiger.   |
|   Dose in mg/kg, one curve.          Body mass spans 5 orders of magnitude  |
|                                      (20 g mouse -> 5000 kg elephant).      |
|                                                                             |
+--------------------------------------+--------------------------------------+
                                       |
                                       v
+-----------------------------------------------------------------------------+
|                       FOUR AXES OF VARIATION                                |
|                                                                             |
|   SPECIES        PURPOSE          ENVIRONMENT        ECONOMICS              |
|   -------        -------          -----------        ---------              |
|   anatomy        companion        clinic / cage      owner pays per animal  |
|   physiology     food / fiber     pasture / herd     vs. herd cost per head |
|   metabolism     work / sport     wild / range       vs. public good (free) |
|   behavior       research         zoo / aquarium     vs. conservation value |
|                  conservation                                               |
+-----------------------------------------------------------------------------+
                                       |
                                       v
+------------------------------------------------------------------------------+
|                          ONE HEALTH (the coupled system)                     |
|                                                                              |
|        HUMAN HEALTH  <---->  ANIMAL HEALTH  <---->  ENVIRONMENT              |
|        zoonoses, food, antimicrobial resistance, climate, spillover          |
+------------------------------------------------------------------------------+
```

**Read top-down.** Human medicine optimizes one species. Veterinary medicine is the same
biology under four simultaneous axes of variation — species, purpose, environment, and
economics — and the whole field sits inside a feedback loop where animal, human, and
environmental health are not separable subsystems. That coupling (One Health) is the thesis
of the directory.

**Systems Bridge:** If human medicine is a single-tenant service tuned for one workload,
veterinary medicine is a multi-tenant platform. The "API" (give a drug, expect an effect) is
the same, but every tenant has different resource limits (a cat's liver lacks an enzyme a
dog has), different SLAs (a pet owner will fund an MRI; a feedlot will not fund it per head),
and different blast radius (one sick chicken is a flock-level and possibly a pandemic-level
event). The discipline is less "treat the patient" and more "operate a fleet of biologically
heterogeneous nodes under economic and public-health constraints."

---

## What Veterinary Medicine Is — and Is Not

This directory is **comparative animal health**. It deliberately does not re-teach material
that already has a home in the library.

| If you want...                          | Go to...                          |
|-----------------------------------------|-----------------------------------|
| Human clinical practice and drug classes | `medicine/`                       |
| The catalog of human diseases            | `disease/`                        |
| Drug receptor / PK-PD mechanism theory   | `pharmacology/`                   |
| Animal taxonomy and body plans           | `zoology/`, `animal-phylogeny/`   |
| Human anatomy and physiology baseline    | `human-biology/`                  |
| Epidemiology, surveillance, food safety  | `public-health/`                  |
| **What changes when the patient is a cow, parrot, snake, or cat** | **here** |

The recurring move in every file below is *comparative*: take a mechanism you already know
from human biology and ask how it differs across the animal kingdom, and why that difference
is clinically load-bearing.

**Old world -> new world bridge:** A human physician learns one normal. A veterinarian learns
a *family* of normals and the transformation rules between them. A canine heart rate of 120
bpm is normal; the same rate in a horse is a tachycardic emergency; in a hummingbird it would
be bradycardia near death. "Normal" is a function of the species, not a constant.

---

## The Species Span

The patients are not a list — they are a tree (see `animal-phylogeny/`). Clinical groupings
cut across that tree by management and economics, not strictly by phylogeny.

```
+------------------------------------------------------------------------------+
|                       CLINICAL SPECIES GROUPINGS                             |
|                                                                              |
|  COMPANION          PRODUCTION         EQUINE          EXOTIC / WILDLIFE     |
|  ---------          ----------         ------          -----------------     |
|  dog (canine)       cattle (bovine)    horse           rabbits, rodents      |
|  cat (feline)       swine (porcine)    donkey, mule    ferrets               |
|  small mammals      sheep (ovine)      (own specialty  reptiles, amphibians  |
|                     goat (caprine)      because of      birds (avian)        |
|                     poultry (avian)     economics +     fish (aquaculture +  |
|                                         athletics)      ornamental)          |
|                                                         zoo megafauna        |
|                                                         free-ranging wild    |
+------------------------------------------------------------------------------+
```

Note that "avian" appears in two columns: a backyard chicken is production medicine; a pet
parrot is exotic medicine. Same biology, different economic and emotional contract. The horse
gets its own column because it is simultaneously a companion animal (high owner spend), an
athlete (sports medicine), and historically a working animal — a unique blend.

---

## Scope of Practice — What a Veterinarian Actually Does

The job is much wider than the human-medicine analogy suggests. A single license covers
roles that in human health are split across physician, surgeon, pharmacist, public-health
officer, food-safety inspector, and pathologist.

```
                        +---------------------------+
                        |   VETERINARY PRACTICE     |
                        +---------------------------+
                          |      |      |      |
         .----------------'      |      |      '----------------.
         v                       v      v                       v
+----------------+   +----------------+   +----------------+   +----------------+
| CLINICAL       |   | POPULATION /   |   | PUBLIC HEALTH  |   | LABORATORY /   |
| (individual)   |   | HERD           |   | & REGULATORY   |   | RESEARCH       |
+----------------+   +----------------+   +----------------+   +----------------+
| diagnose       |   | herd health    |   | meat / milk    |   | pathology      |
| medicate       |   | production     |   |   inspection   |   | toxicology     |
| operate        |   |   metrics      |   | disease        |   | drug / vaccine |
| dentistry      |   | vaccination    |   |   surveillance |   |   development  |
| imaging        |   |   programs     |   | zoonosis       |   | lab animal     |
| euthanasia     |   | biosecurity    |   |   control      |   |   welfare      |
+----------------+   +----------------+   +----------------+   +----------------+
```

The euthanasia line has no clean human-medicine analog. The authority and obligation to
end suffering humanely — and to do so for economic, welfare, or disease-control reasons,
not only terminal-illness reasons — is structurally central to the profession and shapes
many decisions a human physician never faces.

---

## One Health — The Coupled System

This is the organizing idea of the whole directory, so it gets its own diagram. The claim is
not a slogan; it is that human, animal, and environmental health share state and feed back on
each other, so optimizing any one in isolation is a local optimum that can blow up the others.

```
+------------------------------------------------------------------------------+
|                            ONE HEALTH TRIAD                                  |
|                                                                              |
|                          .-----------------.                                 |
|                          |   ENVIRONMENT   |                                 |
|                          | climate, water, |                                 |
|                          | vectors, land   |                                 |
|                          '-----------------'                                 |
|                            ^             ^                                   |
|         habitat loss ->    |             |    <- vector range shift          |
|         spillover          |             |       (warming -> ticks/mosq.)    |
|                            v             v                                   |
|             .-----------------.     .-----------------.                      |
|             |  ANIMAL HEALTH  |<--->|  HUMAN HEALTH   |                      |
|             | wildlife,       |     | clinical,       |                      |
|             | livestock, pets |     | public health   |                      |
|             '-----------------'     '-----------------'                      |
|                   zoonotic spillover (~60% of human                          |
|                   infectious diseases are zoonotic;                          |
|                   ~75% of EMERGING ones)                                     |
+------------------------------------------------------------------------------+
```

Concrete couplings (each developed later in the directory):

| Edge of the triad         | Worked example                                          |
|---------------------------|---------------------------------------------------------|
| Animal -> Human           | H5N1 avian influenza spilling from poultry/wild birds   |
| Human -> Animal            | "Reverse zoonosis": humans transmitting SARS-CoV-2 to mink, deer, cats |
| Environment -> Animal -> Human | Warming expands tick range -> Lyme, anaplasmosis spread |
| Animal use -> Human (slow) | Antimicrobial use in livestock selecting resistant bacteria that reach people |
| Animal -> Human (catastrophic) | BSE prions in beef -> variant CJD in humans         |

The estimate that roughly 60% of known human infectious diseases and about three quarters of
emerging ones are zoonotic is the quantitative backbone of why veterinary surveillance is a
front line of human pandemic defense (`04-ZOONOSES-AND-ONE-HEALTH.md`,
`09-PUBLIC-HEALTH-ROLE.md`).

---

## The Comparative Method — How to Read Every File Here

Each downstream guide uses the same intellectual engine. Internalize it once:

```
   KNOWN BASELINE              ASK THE DELTA              CLINICAL CONSEQUENCE
   (human or one species)      (what changed, why)        (why it matters)
   ------------------          --------------------       --------------------
   Humans glucuronidate        Cats lack adequate         Acetaminophen / many
   many drugs in the liver     UGT1A6 glucuronidation     drugs are far more toxic
                               (evolutionary loss in       to cats; dosing rules
                               an obligate carnivore)      differ from dogs/humans

   Humans have one             Ruminants ferment in a     Drug absorption, bloat,
   acid stomach                4-chambered foregut         and feed toxicology are
                               (rumen) before the          completely different
                               true acid stomach           from monogastrics
```

Whenever you meet a new species fact, run it through this template: *baseline -> delta ->
consequence*. That is the entire discipline in three boxes.

---

## Map of This Directory

```
00-OVERVIEW ............... you are here (landscape, scope, One Health)
   |
   +-- 01-COMPARATIVE-ANATOMY .. body plans across mammals/birds/reptiles
   +-- 02-ANIMAL-PHYSIOLOGY .... digestion, thermoregulation, reproduction
   |
   +-- 03-INFECTIOUS-DISEASE ... agents and the major animal diseases
   +-- 04-ZOONOSES-ONE-HEALTH .. the human-animal-environment interface
   |
   +-- 05-COMPANION-ANIMALS .... dog / cat / small-mammal clinical medicine
   +-- 06-LIVESTOCK-HEALTH ..... herd / flock production medicine
   +-- 07-WILDLIFE-AND-EXOTICS . conservation, zoo, exotic species
   |
   +-- 08-VET-PHARM-AND-SURGERY  drug differences, anesthesia, surgery
   +-- 09-PUBLIC-HEALTH-ROLE ... food safety, surveillance, AMR
```

Read 01-02 for the biological substrate, 03-04 for disease and its cross-species jump,
05-07 for the clinical worlds grouped by economics, and 08-09 for the toolkit and the public
mandate.

---

## Decision Cheat Sheet

| I want to understand...                          | Read |
|--------------------------------------------------|------|
| Why a cow's stomach is unlike mine               | `01-COMPARATIVE-ANATOMY.md` |
| Why birds need air sacs and one-way lungs        | `01-COMPARATIVE-ANATOMY.md` |
| Why cats and dogs metabolize drugs differently   | `08-VETERINARY-PHARM-AND-SURGERY.md` |
| The major animal pathogens (FMD, parvo, FeLV)    | `03-INFECTIOUS-DISEASE.md` |
| How animal disease becomes a human pandemic      | `04-ZOONOSES-AND-ONE-HEALTH.md` |
| Common dog/cat conditions and what to suspect    | `05-COMPANION-ANIMALS.md` |
| How a feedlot or dairy is kept healthy at scale  | `06-LIVESTOCK-HEALTH.md` |
| Treating a snake, parrot, or wild tiger          | `07-WILDLIFE-AND-EXOTICS.md` |
| Why vets are central to food safety and AMR      | `09-PUBLIC-HEALTH-ROLE.md` |
| The taxonomy / body-plan substrate               | `zoology/`, `animal-phylogeny/` |

---

## Common Confusion Points

### "Veterinary medicine is just human medicine on animals"

It overlaps in mechanism but diverges in everything operational. The patient cannot report
symptoms, spans five orders of magnitude in body mass, may be one of a thousand identical
herd-mates whose individual value is a fraction of the diagnostic cost, and may legally be
food. The mechanisms in `pharmacology/` and `human-biology/` are the shared substrate; the
clinical decisions are a different field.

### "One Health is a marketing buzzword"

It is a falsifiable systems claim with a track record. SARS, MERS, HIV, Ebola, COVID-19,
and most influenza pandemics originated in animals. Surveillance that watches only humans
sees the spillover after it has already happened. One Health says: instrument the animal and
environmental subsystems too, because that is where the signal appears first.

### "A vet treats pets"

Companion-animal practice is the most visible slice, but the same license covers feedlot
herd health, meat inspection, vaccine development, wildlife conservation, and pandemic
surveillance. The profession's largest public impact is arguably in the parts the public
never sees — food safety and zoonosis control (`09-PUBLIC-HEALTH-ROLE.md`).

### "Animals are basically small/large humans for dosing"

No. Allometric scaling (metabolic rate scales roughly with body mass to the 3/4 power, not
linearly) means you cannot dose a cat as a small dog or an elephant as a large horse by
simple mg/kg, and species-specific metabolic gaps (the feline glucuronidation deficit, the
greyhound's altered anesthetic clearance) break linear extrapolation entirely. This is the
subject of `08-VETERINARY-PHARM-AND-SURGERY.md`.
