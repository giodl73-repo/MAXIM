---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-VETERINARY-PHARM-AND-SURGERY.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:veterinary-medicine:pharm-and-surgery
kind: guide
module: veterinary-medicine
section: veterinary-medicine
title: Veterinary Pharmacology and Surgery - Drug Differences, Anesthesia, Common Procedures
status: source-custody
source_custody: partial
current_path: veterinary-medicine/08-VETERINARY-PHARM-AND-SURGERY.md
canonical_path: veterinary-medicine/08-VETERINARY-PHARM-AND-SURGERY.md
backsource_ids: [mdloom-backfill:veterinary-medicine:08-pharm-and-surgery, git-history:veterinary-medicine:08-pharm-and-surgery]
concepts: [veterinary pharmacology, veterinary surgery]
root_concepts: [veterinary pharmacology]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Veterinary Pharmacology and Surgery — Drug Differences, Anesthesia, Common Procedures

```
+------------------------------------------------------------------------------+
|              WHY YOU CANNOT JUST SCALE THE HUMAN DOSE                        |
|                                                                              |
|   THREE INDEPENDENT REASONS A DRUG BEHAVES DIFFERENTLY PER SPECIES:          |
|                                                                              |
|   1. METABOLIC GAPS    a species lacks an enzyme (cat: glucuronidation;      |
|      (qualitative)     -> the drug is not cleared -> accumulates -> toxic.   |
|                                                                              |
|   2. ALLOMETRIC SCALE  metabolic rate scales ~ (body mass)^0.75, NOT         |
|      (nonlinear)       linearly. A 20 g mouse clears per-kg far faster       |
|                        than a 5000 kg elephant. mg/kg breaks at extremes.    |
|                                                                              |
|   3. TARGET / SAFETY   a transporter mutation (collie MDR1) lets a drug      |
|      DIFFERENCES       into the brain; a different receptor sensitivity;     |
|                        food-animal RESIDUE rules (can't enter the food       |
|                        chain) constrain what you may even use.               |
+------------------------------------------------------------------------------+
```

**Read top-down.** Three independent failure modes break naive dose extrapolation: a missing
metabolic pathway (qualitative), nonlinear body-size scaling (allometry), and target/safety
differences including the food-residue constraint unique to veterinary practice. The mechanism
theory (receptors, PK/PD, enzyme families) lives in `pharmacology/` and `medicine/`; this file
is the *species-difference* layer on top of it.

**Systems Bridge:** Same API, different runtimes with different capabilities and resource
limits. The cat runtime is missing a library (the UGT glucuronidation module), so a call that
returns cleanly on the human runtime throws a fatal error there. Allometry is a non-linear
scaling curve, not a constant multiplier — you cannot size a cat as a small dog any more than
you can size a fleet by multiplying one node's spec. And food animals add a compliance
constraint (residues must clear before slaughter/milk) absent from any single-tenant system.

---

## The Metabolic Gaps — Species-Specific Drug Traps

```
+------------------------------------------------------------------------------+
|                   KNOWN SPECIES METABOLIC DEFICITS                           |
|                                                                              |
|  SPECIES   DEFICIT                    CONSEQUENCE                            |
|  -------   -------                    -----------                            |
|  CAT       Poor GLUCURONIDATION       Acetaminophen -> fatal (methemo-       |
|            (low UGT enzyme activity)  globinemia + liver). Aspirin/NSAIDs    |
|                                       cleared slowly -> narrow margin.       |
|                                       Many drugs need longer dosing          |
|                                       intervals than in dogs.                |
|  DOG       (broadly capable, but...)  Sighthounds (greyhounds) have low      |
|            certain breeds differ      body fat + altered hepatic clearance   |
|                                       -> prolonged thiopental/propofol       |
|                                       recovery; dose anesthetics carefully.  |
|  COLLIE-   MDR1 / ABCB1 gene mutation P-glycoprotein pump at the blood-      |
|  TYPE      (herding breeds)           brain barrier is defective -> drugs    |
|  BREEDS                               like high-dose ivermectin,             |
|                                       loperamide, some chemo agents cross    |
|                                       into the brain -> neurotoxicity.       |
|                                       ("White feet, don't treat" mnemonic    |
|                                       for ivermectin-class sensitivity.)     |
|  HORSE/    Hindgut microbe dependence Many oral antibiotics destroy gut      |
|  RABBIT/   (file 01-02)               flora -> fatal enterocolitis. Route    |
|  RUMINANT                             and drug choice are constrained.       |
|  BIRDS     Renal portal system +      Drug handling differs; some drugs      |
|            high metabolic rate        dosed far more frequently.             |
+------------------------------------------------------------------------------+
```

These are not dose adjustments — they are *contraindications driven by physiology*. The cat
acetaminophen case and the collie ivermectin case are the two most cited, and both trace to a
single molecular fact (a missing conjugation enzyme; a defective efflux transporter).

### The food-animal residue constraint

A category with no human-medicine analog: any drug given to a food-producing animal must clear
to safe levels before the meat, milk, or eggs enter the food supply.

```
   WITHDRAWAL TIME: the mandated interval between the last drug dose and
   when the animal's products may enter the food chain. Violating it leaves
   illegal drug RESIDUES in food.
     * Some drugs are outright BANNED in food animals (e.g. chloramphenicol,
       certain others) due to human health risk.
     * "Extra-label" use is tightly regulated; the vet is legally
       responsible for residue avoidance.
   => Drug choice for a cow is constrained not just by efficacy and safety
      to the cow, but by what it leaves in YOUR food. (file 09)
```

---

## Allometric Scaling — Why mg/kg Fails at the Extremes

Metabolic rate does not scale linearly with body mass; it scales roughly with mass to the 3/4
power (Kleiber's law). Small animals run "hotter" per gram and clear drugs faster per kg; huge
animals clear slower per kg.

```
   Naive assumption:  dose = constant  x  body mass        (linear, WRONG at extremes)
   Reality (approx):  metabolic rate ~ body_mass^0.75      (sub-linear)

   So PER KILOGRAM, a tiny animal needs MORE drug (and more often), and a
   giant animal needs LESS per kg, than a mid-sized one.

   +---------------------------------------------------------------+
   |  20 g mouse  ->  fast per-kg metabolism, frequent dosing      |
   |  5 kg cat    ->  ...                                          |
   |  500 kg horse ->  ...                                         |
   |  5000 kg elephant -> slow per-kg metabolism                   |
   +---------------------------------------------------------------+

   For exotic/wildlife species with no published dose (file 07), allometric
   scaling from a known related species is often the only starting estimate.
```

This is why dosing references are species- and size-specific, and why "scale the human dose by
weight" produces overdoses in small pets and underdoses in megafauna.

---

## Anesthesia — Multimodal and Species-Tuned

Veterinary anesthesia follows the same physiology as human anesthesia (the shared theory is in
`medicine/09-ANESTHESIA-SURGERY.md`) but must flex across species with very different airways,
metabolism, and restraint needs. The modern approach is **balanced/multimodal**: combine small
doses of several agents acting at different points rather than one big dose.

```
+------------------------------------------------------------------------------+
|                  THE ANESTHESIA WORKFLOW (small animal)                      |
|                                                                              |
|  1. PREMEDICATION   sedative (alpha-2 agonist e.g. dexmedetomidine, or       |
|                     acepromazine) + opioid analgesic. Calms, reduces the     |
|                     dose of everything that follows, pre-empts pain.         |
|        |                                                                     |
|  2. INDUCTION       rapid IV agent (propofol, alfaxalone, or ketamine        |
|        |            combos) to get from awake to unconscious smoothly,       |
|        |            then INTUBATE (secure the airway).                       |
|  3. MAINTENANCE     inhalant anesthetic (isoflurane / sevoflurane) in        |
|        |            oxygen, titrated to depth. Same gases as human use.      |
|  4. MONITORING      depth, HR, BP, SpO2, capnography, temperature            |
|        |            (animals lose heat fast under anesthesia).               |
|  5. RECOVERY +      reversal agents where applicable (atipamezole reverses   |
|     ANALGESIA       alpha-2s; naloxone reverses opioids), ongoing pain       |
|                     control. Smooth recovery matters (esp. horses).          |
+------------------------------------------------------------------------------+
```

Species-specific anesthesia notes worth holding:

| Species | Anesthesia challenge |
|---------|----------------------|
| **Horse** | A large animal that must lie down and then *stand back up* under anesthesia; recovery is dangerous (a panicked, ataxic half-ton animal can fracture itself). Recovery management is a defining equine problem |
| **Cat** | Narrow drug margins; airway is small and laryngospasm-prone; metabolic gaps (above) |
| **Sighthounds** | Prolonged recovery from some IV agents (low fat, altered clearance) |
| **Rabbits / small mammals** | High anesthetic mortality vs cats/dogs; hard to intubate; lose heat fast |
| **Ruminants** | Risk of regurgitation + aspiration (the rumen!) and bloat when recumbent; fast prolonged from feed |
| **Megafauna** | Immobilization with ultra-potent opioids; positional/weight injury; capture myopathy (file 07) |
| **Birds** | Air-sac system means inhalant uptake is very rapid; no diaphragm to assist (file 01) |

The reason small mammals and rabbits have notably higher anesthetic risk than dogs and cats is
a combination of difficult airway access, rapid heat loss from small body mass, and stress
physiology — another reason exotic anesthesia is its own skill.

---

## Common Surgical Procedures

Surgery spans routine high-volume procedures (spay/neuter) to species-specific emergencies.

```
+-----------------------------------------------------------------------------+
|                    THE SURGICAL CASE SPECTRUM                               |
|                                                                             |
|  ROUTINE / ELECTIVE        EMERGENCY (often species-specific)               |
|  ------------------        --------------------------------                 |
|  Spay (ovariohyster-       GDV/bloat correction (dog, file 05)              |
|    ectomy) / Neuter         + prophylactic gastropexy                       |
|  (castration)              Foreign-body removal (dogs eat things)           |
|  Dental procedures         Cesarean section (dystocia)                      |
|  Mass / tumor removal      Cystotomy (bladder stones; blocked-cat relief)   |
|  Wound repair              COLIC surgery (horse, file 01) -- find + fix     |
|                              the displaced/twisted gut                      |
|                            Displaced abomasum correction (dairy cow)        |
|                            Fracture repair (orthopedics; plates, pins)      |
|                            Cruciate (CCL) repair (dog knee, file 05)        |
+-----------------------------------------------------------------------------+
```

### Spay/neuter — the highest-volume surgery in the world

Ovariohysterectomy (spay) and castration (neuter) are the bread-and-butter procedures, done
for population control and the medical benefits noted in file 05 (no pyometra, fewer mammary/
testicular tumors, behavior). High-volume spay/neuter is a public-health and animal-welfare
program as much as individual surgery.

### Field surgery and large-animal reality

Large-animal surgery is often done **standing**, under sedation and local/regional anesthesia
rather than full general anesthesia, precisely because dropping and recovering a half-ton
animal is itself dangerous (the equine recovery problem above). Bovine surgeries like the
displaced-abomasum correction and many equine procedures are commonly performed on the
standing, sedated animal in the field — a striking contrast to small-animal practice.

```
   SMALL ANIMAL                       LARGE ANIMAL (field)
   ------------                       --------------------
   general anesthesia, dorsal         often STANDING, sedated + local/
   recumbency, sterile OR             regional block, on the farm
   patient lifted/positioned freely   gravity + size constrain everything
   recovery in a cage                 recovery = must safely STAND again
```

**Old world -> new world bridge:** Small-animal surgery is a controlled lab environment; large-
animal field surgery is operating on production hardware in the data center while it stays
powered on, because you cannot safely take it fully offline (anesthetize and recover a horse)
without large risk. You work around the constraint (standing, sedated, local block) rather than
fighting it.

---

## Pain Management — and Its Species Traps

Modern veterinary medicine takes analgesia seriously (pain is a welfare and recovery issue),
but the species drug traps recur:

```
   NSAIDs (carprofen, meloxicam, etc.): effective for inflammation/pain in
     DOGS; used cautiously and at much lower frequency in CATS (slow
     clearance). NEVER casually give human NSAIDs (ibuprofen, naproxen) to
     pets -- narrow margins, GI/renal toxicity.
   OPIOIDS: used for moderate/severe pain; species differ in receptor
     response (e.g. some opioids cause excitement in cats/horses at certain
     doses).
   ALPHA-2 AGONISTS: sedation + analgesia, reversible.
   LOCAL/REGIONAL BLOCKS: increasingly central (multimodal), and the basis of
     standing large-animal surgery.
```

The single most important consumer-facing safety rule that falls out of all this: **do not give
human pain medications to pets**. Ibuprofen and naproxen are dangerous to dogs and cats;
acetaminophen is lethal to cats; aspirin has a narrow feline margin. This connects directly to
the household-toxin list in file 05.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| Why is acetaminophen lethal to cats? | Cats lack glucuronidation; can't detoxify it -> methemoglobinemia + liver failure |
| Why are collies/herding breeds drug-sensitive? | MDR1/ABCB1 mutation -> defective blood-brain barrier pump -> ivermectin-class neurotoxicity |
| Why can't you dose a cat as a small dog? | Metabolic gaps + allometric scaling break linear mg/kg |
| Why are some oral antibiotics fatal to rabbits/horses? | They destroy hindgut/rumen flora -> fatal enterocolitis |
| Why is equine anesthesia uniquely risky? | A half-ton animal must lie down and stand back up; recovery is the danger |
| Why is large-animal surgery often done standing? | Dropping/recovering the animal under GA is itself high-risk |
| Why does a cow drug have a "withdrawal time"? | Residues must clear before meat/milk enter the food chain |
| Why are rabbit/small-mammal anesthetics higher-risk? | Difficult airway, rapid heat loss, stress physiology |
| Can I give my dog ibuprofen? | No — human NSAIDs have narrow, toxic margins in pets |

---

## Common Confusion Points

### "Just give the animal a weight-scaled human dose"

Three independent reasons this fails: metabolic gaps (cats can't clear acetaminophen at any
dose), allometric (non-linear) scaling, and breed/target differences (MDR1). Dosing is
species- and often breed-specific, from references, not arithmetic on the human dose.

### "Anesthesia is anesthesia"

The theory is shared, but airway access, heat loss, recovery danger (horses), regurgitation
risk (ruminants), and metabolic clearance vary enormously. Rabbits and small mammals carry
notably higher anesthetic risk than dogs and cats; megafauna need ultra-potent immobilizers
with staged antidotes (file 07).

### "Human painkillers are fine in a pinch"

They are a common cause of pet poisoning. Ibuprofen/naproxen are toxic to dogs and cats;
acetaminophen is lethal to cats. Use veterinary-approved analgesics at veterinary doses only.

### "A withdrawal time is just a formality"

It is a legal and food-safety requirement: drug residues in meat, milk, or eggs are a direct
human-health hazard, and some drugs are banned in food animals entirely. This is the bridge
into the veterinarian's public-health mandate — food safety, surveillance, and antimicrobial
resistance — covered in `09-PUBLIC-HEALTH-ROLE.md`.
