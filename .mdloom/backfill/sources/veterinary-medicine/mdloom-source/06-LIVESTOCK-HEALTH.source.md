---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "06-LIVESTOCK-HEALTH.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:veterinary-medicine:livestock-health
kind: guide
module: veterinary-medicine
section: veterinary-medicine
title: Livestock Health - Production Medicine and Herd Health
status: source-custody
source_custody: partial
current_path: veterinary-medicine/06-LIVESTOCK-HEALTH.md
canonical_path: veterinary-medicine/06-LIVESTOCK-HEALTH.md
backsource_ids: [mdloom-backfill:veterinary-medicine:06-livestock-health, git-history:veterinary-medicine:06-livestock-health]
concepts: [livestock health]
root_concepts: [livestock health]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Livestock Health — Production Medicine and Herd Health

```
+------------------------------------------------------------------------------+
|              THE ECONOMIC INVERSION: PATIENT = POPULATION                    |
|                                                                              |
|   COMPANION MODEL (file 05)          PRODUCTION MODEL (this file)            |
|   -------------------------          ------------------------------          |
|   patient = the individual           patient = the HERD / FLOCK              |
|   owner spends $$$ per animal        cost per head must be < value/head      |
|   goal = longevity, quality of life  goal = healthy, efficient OUTPUT        |
|                                       (milk, meat, eggs, offspring)          |
|   metric: is this animal well?       metric: production rate, mortality %,   |
|                                       feed conversion, fertility %           |
|                                                                              |
|   => Treat the SYSTEM. Prevention, not heroic individual rescue, dominates.  |
|      One sick animal is a sentinel for a herd-level problem.                 |
+------------------------------------------------------------------------------+
```

**Read across.** Production medicine inverts the companion-animal economics: the unit of care
is the population, individual diagnostics are constrained by per-head value, and the objective
is an efficient, healthy *output stream*. The veterinarian becomes part epidemiologist, part
production engineer. A sick individual matters mainly as a signal about the herd.

**Systems Bridge:** This is fleet/SRE thinking, not single-server debugging. You do not SSH
into one box and trace a bug; you watch fleet-level SLIs (mortality rate, milk yield, feed
conversion, conception rate), set error budgets, and invest in prevention (vaccination,
biosecurity, nutrition) because incident-by-incident response does not scale to a thousand
identical nodes. One sick animal is a failing health-check that may indicate a systemic issue
(bad feed lot, ventilation failure, a pathogen breaching biosecurity).

Cross-references: `agriculture/` for the production context, `public-health/` and
`09-PUBLIC-HEALTH-ROLE.md` for food safety and AMR, file 03 for the reportable diseases.

---

## The Production Species and Their Output

```
+------------------------------------------------------------------------------+
|                    PRODUCTION SPECIES MATRIX                                 |
|                                                                              |
|  SPECIES        OUTPUT             SYSTEM            KEY HEALTH FOCUS        |
|  -------        ------             ------            ----------------        |
|  Dairy cattle   milk               high-output cow   metabolic (transition   |
|                                    near metabolic     period), mastitis,     |
|                                    limit              lameness, fertility    |
|  Beef cattle    meat               cow-calf +         BRD (respiratory),     |
|                                    feedlot            parasites, nutrition   |
|  Swine          meat               intensive indoor   respiratory, enteric,  |
|                                    all-in/all-out     reproductive, ASF/PRRS |
|  Poultry        eggs + meat        very intensive,    avian influenza,       |
|  (broilers /                       huge flocks        Newcastle, coccidia,   |
|   layers)                                             biosecurity is king    |
| Sheep / goat   meat, wool, milk   range / pasture    parasites (Haemonchus), |
|                                                       footrot, lambing       |
|  Aquaculture    fish (food)         water systems      water quality,        |
|  (salmon, etc)                                         sea lice, viral/      |
|                                                        bacterial outbreaks   |
+------------------------------------------------------------------------------+
```

The intensity gradient (range sheep -> indoor swine -> caged poultry) tracks how dominant
*biosecurity and ventilation* become: the denser the housing, the faster a pathogen amplifies,
and the more the whole operation depends on keeping it out in the first place.

---

## Dairy Cattle — Medicine at the Metabolic Edge

A modern high-yield dairy cow produces enormous quantities of milk, pushing her metabolism to
its limit, especially around calving. Most dairy disease clusters in the **transition period**
(the weeks around calving) when demand spikes.

```
+-------------------------------------------------------------------------------+
|         THE TRANSITION PERIOD CASCADE (around calving)                        |
|                                                                               |
|   Calving + sudden lactation = huge calcium + energy demand                   |
|        |                                                                      |
|        +-> MILK FEVER (hypocalcemia): blood calcium crashes as it pours       |
|        |     into milk -> the cow goes down, can't rise. Treated with IV      |
|        |     calcium. A metabolic, not infectious, "fever."                   |
|        |                                                                      |
|        +-> KETOSIS / negative energy balance: can't eat enough to match       |
|        |     milk output -> mobilizes fat -> ketones. Parallels the cat's     |
|        |     hepatic lipidosis logic (file 02): fat mobilized faster than     |
|        |     the liver handles it -> fatty liver.                             |
|        |                                                                      |
|        +-> DISPLACED ABOMASUM: the true stomach shifts (often left) when      |
|        |     rumen fill drops post-calving -> needs surgical correction       |
|        |     (file 01).                                                       |
|        |                                                                      |
|        +-> RETAINED PLACENTA / METRITIS: uterine infection after calving.     |
+-------------------------------------------------------------------------------+
```

Three other dairy mainstays:

| Problem | What it is | Why it dominates |
|---------|------------|------------------|
| **Mastitis** | Udder infection (Strep, Staph, coliforms) | The #1 production-loss disease in dairy: lowers yield, spoils milk, costs treatment + discarded milk |
| **Lameness** | Hoof/leg disorders (digital dermatitis, sole ulcers) | A leading welfare and culling cause; a lame cow eats and milks less |
| **Subfertility** | Failure to re-breed on schedule | A dairy cow must calve regularly to keep lactating; reproductive efficiency is a core KPI |

Note "milk fever" is a *misnomer* — it is hypocalcemia, not infection. The naming is historical;
the treatment is intravenous calcium, not antibiotics.

---

## Beef Cattle and the Feedlot — Respiratory Disease Rules

Beef production moves animals from dispersed cow-calf operations into dense feedlots, mixing
animals from many sources. That mixing, plus transport stress, makes **Bovine Respiratory
Disease (BRD)** the dominant feedlot problem.

```
   BRD ("shipping fever") -- a MULTIFACTORIAL disease:
     STRESS (transport, weaning, commingling, weather)
        +  VIRAL primers (IBR, BVDV, BRSV, PI3)
        +  BACTERIAL opportunists (Mannheimia haemolytica, Pasteurella,
           Histophilus, Mycoplasma) that invade the stressed lung
        =  pneumonia -> the #1 cause of feedlot illness/death + economic loss.

   Control is SYSTEMS-level:
     * low-stress handling + acclimation
     * vaccination on arrival ("processing")
     * metaphylaxis (treating the whole at-risk group on arrival -- a
       stewardship tension, see file 09)
     * BVDV is special: persistently infected (PI) calves are immunotolerant
       lifelong shedders -- find and remove them or they seed the herd.
```

BRD is the textbook example of *multifactorial* production disease: no single agent, but a
predictable stack of stressor + virus + bacterium. You manage the stack, not just the bug.

---

## Swine — Intensive, Reproductive, and Respiratory

Modern swine production is highly intensive and runs on **all-in/all-out** flow (fill a barn
with one cohort, empty and disinfect it completely before the next) to break disease cycles.

```
+------------------------------------------------------------------------------+
|                    MAJOR SWINE HEALTH AXES                                   |
|                                                                              |
|  RESPIRATORY        PRRS ("blue-ear", a major economic virus),               |
|                     swine influenza (+ pandemic mixing-vessel role,          |
|                     file 04), enzootic pneumonia (Mycoplasma).               |
|  ENTERIC            E. coli + rotavirus scours in piglets; PED               |
|                     (porcine epidemic diarrhea) devastates neonates.         |
|  REPRODUCTIVE       sows are managed for litters/year; reproductive          |
|                     efficiency (pigs weaned per sow per year) is THE KPI.    |
|  CATASTROPHIC       AFRICAN SWINE FEVER (~100% fatal, no good vaccine,       |
|  (reportable)       not zoonotic) -- has wiped out herds across continents.  |
|                     Classical swine fever (hog cholera) also reportable.     |
+------------------------------------------------------------------------------+
```

Pigs sit at a special junction: economically vital, physiologically close to humans (a model
and xenotransplant donor, file 01), and the influenza "mixing vessel" (file 04). A swine barn
is simultaneously a production system and a pandemic-surveillance site.

---

## Poultry — Where Biosecurity Is the Whole Game

Poultry operations are the most intensive of all, with flocks of tens of thousands. At that
density, an introduced pathogen amplifies explosively, so **biosecurity is the dominant
discipline** — keeping disease *out*, because once in, it is uncontrollable.

```
+------------------------------------------------------------------------------+
|                    POULTRY DISEASE + DEFENSE                                 |
|                                                                              |
|  THREAT                          DEFENSE                                     |
|  ------                          -------                                     |
|  Avian influenza (HPAI, H5N1)    perimeter biosecurity, wild-bird            |
|    -- reportable, zoonotic         exclusion, rapid detection + STAMPING     |
|    (file 04)                       OUT (cull the flock) on confirmation.     |
|  Newcastle disease (reportable)  vaccination + biosecurity.                  |
|  Coccidiosis (Eimeria protozoa)  coccidiostats in feed + vaccination;        |
|                                    the major enteric parasite of poultry.    |
|  Marek's disease (herpesvirus    vaccinate day-old chicks (an early,         |
|    tumors/paralysis)               historically important cancer vaccine).   |
|  Salmonella (food-safety + bird) flock testing, vaccination, hygiene         |
|                                    (egg safety; file 09).                    |
|                                                                              |
|  BIOSECURITY MEASURES: all-in/all-out, controlled access, shower-in/         |
|  shower-out, dedicated clothing/boots, rodent + wild-bird control,           |
|  downtime + disinfection between flocks.                                     |
+------------------------------------------------------------------------------+
```

Marek's disease is historically notable: vaccinating day-old chicks against this herpesvirus
that causes tumors and paralysis was one of the first widely successful *cancer* vaccines in
any species — a landmark that predates much of human cancer-vaccine work.

---

## Herd Health as a Discipline

The veterinarian's deliverable in production medicine is not "this cow is cured" but a
*program* that keeps the population productive. The recurring framework:

```
+------------------------------------------------------------------------------+
|                   THE HERD-HEALTH LOOP                                       |
|                                                                              |
|   1. MEASURE      production + health KPIs (mortality %, growth rate,        |
|                   milk yield, somatic cell count for mastitis, conception    |
|                   rate, feed conversion ratio).                              |
|        |                                                                     |
|   2. BENCHMARK    compare to targets / industry norms -> find the            |
|        |          limiting problem (the bottleneck).                         |
|   3. INTERVENE    vaccination program, nutrition change, biosecurity         |
|        |          upgrade, ventilation fix, breeding management.             |
|   4. RE-MEASURE   did the KPI move? Iterate.                                 |
|        |                                                                     |
|        +------------------ continuous improvement loop --------------------+ |
+------------------------------------------------------------------------------+
```

**Old world -> new world bridge:** This is observability + SLOs + continuous improvement
applied to biology. The somatic cell count is a health metric the way error rate is; feed
conversion ratio is efficiency the way cost-per-request is; the transition-period disease
cluster is a known failure mode you instrument and pre-empt. The vet runs the herd like an SRE
runs a service: dashboards, error budgets, and prevention over heroics.

Nutrition is central and easy to underrate: many "diseases" here are really nutritional
mismatches (rumen acidosis from grain overload, hypocalcemia at calving, trace-mineral
deficiencies, parasitism sapping growth). Getting the ration right prevents more disease than
any drug.

---

## Decision Cheat Sheet

| Herd signal | Investigate |
|-------------|-------------|
| Down cow, can't rise, just calved | Milk fever (hypocalcemia) — IV calcium |
| Drop in milk yield + abnormal milk + swollen quarter | Mastitis |
| Group of recently shipped/mixed cattle coughing, febrile | BRD (shipping fever) |
| Repeated abomasal surgeries in fresh cows | Transition-period management problem |
| Piglet barn with explosive neonatal diarrhea | PED / E. coli scours |
| Sudden high mortality in a poultry flock | HPAI / Newcastle — report immediately |
| Poor reproductive numbers herd-wide | Nutrition, BVDV/PI animals, or breeding management |
| Lambs failing to thrive on pasture | Parasitism (Haemonchus) / trace-mineral deficiency |
| ~100% mortality sweeping a pig herd | African swine fever — report (not zoonotic) |

---

## Common Confusion Points

### "Milk fever is an infection"

It is hypocalcemia — a metabolic crash of blood calcium as it floods into milk at calving.
The name is historical. Treatment is intravenous calcium, not antibiotics.

### "You treat livestock like pets, just more of them"

The economics invert the entire approach. The patient is the herd; per-head diagnostic spend
is bounded by per-head value; prevention and population metrics dominate over heroic individual
rescue. A sick individual is mainly a sentinel.

### "More antibiotics = healthier herd"

Metaphylaxis (group treatment) controls outbreaks like BRD but selects for resistance and is
under tightening stewardship rules. Modern production medicine pushes prevention (vaccination,
biosecurity, low-stress handling, nutrition) precisely to reduce antibiotic reliance — the AMR
theme of `09-PUBLIC-HEALTH-ROLE.md`.

### "African swine fever could cause a human pandemic"

ASF is catastrophic to pigs but does not infect humans. The pandemic risk from swine is
*influenza* (the mixing-vessel role), not ASF. Conflating the two misreads the threat. The
non-domestic end of the species spectrum — wildlife and exotics — is the subject of
`07-WILDLIFE-AND-EXOTICS.md`.
