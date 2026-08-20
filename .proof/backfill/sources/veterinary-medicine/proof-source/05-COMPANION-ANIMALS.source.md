---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "05-COMPANION-ANIMALS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:veterinary-medicine:companion-animals
kind: guide
module: veterinary-medicine
section: veterinary-medicine
title: Companion Animals - Dog, Cat, and Small-Mammal Medicine
status: source-custody
source_custody: partial
current_path: veterinary-medicine/05-COMPANION-ANIMALS.md
canonical_path: veterinary-medicine/05-COMPANION-ANIMALS.md
backsource_ids: [proof-backfill:veterinary-medicine:05-companion-animals, git-history:veterinary-medicine:05-companion-animals]
concepts: [companion animals]
root_concepts: [companion animals]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Companion Animals — Dog, Cat, and Small-Mammal Medicine

```
+------------------------------------------------------------------------------+
|                   THE COMPANION-ANIMAL EXAM ROOM                             |
|                                                                              |
|   DOG (canine)        CAT (feline)        SMALL MAMMALS ("pocket pets")      |
|   ------------        ------------        ----------------------------       |
|   omnivore-ish        obligate            rabbit (hindgut ferment),          |
|   highly variable     carnivore           rodents (guinea pig, hamster,      |
|   by breed (size,     stoic, hides        rat, mouse, gerbil),               |
|   conformation,       illness, narrow     ferret (obligate carnivore,        |
|   genetics)           drug tolerance      short gut)                         |
|        |                   |                       |                         |
|   ECONOMICS: owner pays per individual; high willingness to spend ->         |
|   advanced diagnostics and surgery available (MRI, chemo, joint repair).     |
|   Contrast with the per-head economics of livestock (file 06).               |
+------------------------------------------------------------------------------+
```

**Read across.** Companion-animal practice is individual-patient medicine, closest in spirit to
human clinical medicine, because the economics support per-animal diagnostics and the emotional
contract is high. But the patients still span obligate carnivores (cat, ferret), omnivores
(dog), and hindgut-fermenting herbivores (rabbit) — so the comparative-physiology rules from
files 01-02 are constantly load-bearing.

**Systems Bridge:** This is the "one premium customer, full SLA" tier. Unlike the herd model,
cost-per-incident tolerance is high, so you run the full diagnostic stack on a single node. The
catch is that each species is a different runtime with different safe operating limits — and
the cat in particular is a node that *hides* its telemetry (cats mask illness), so by the time
the alert fires, the failure is often advanced.

For drug-handling differences underlying everything here, see
`08-VETERINARY-PHARM-AND-SURGERY.md`; for the agents behind infectious cases, file 03.

---

## The Dog — Variation Is the Defining Feature

No other domestic species varies as much. A 2 kg Chihuahua and a 90 kg Mastiff are the same
species; this artificial-selection spread drives breed-specific disease.

```
+------------------------------------------------------------------------------+
|              BREED CONFORMATION -> PREDICTABLE DISEASE                       |
|                                                                              |
|   CONFORMATION          BREEDS              PREDISPOSED PROBLEM              |
|   ------------          ------              -------------------              |
|   Brachycephalic        bulldog, pug,       BOAS (brachycephalic obstr.      |
|   (flat face)           boxer, Persian cat   airway syndrome): noisy/hard    |
|                                              breathing, heat intolerance.    |
|   Large / giant breed   Great Dane, Mastiff  GDV (bloat/torsion), hip        |
|                                              dysplasia, faster aging,        |
|                                              cardiomyopathy.                 |
|   Long-backed           Dachshund, Corgi     IVDD (intervertebral disc       |
|                                             disease) -> back pain/paralysis. |
|   Deep-chested          Great Dane, Setter,  GDV risk highest.               |
|                         Weimaraner                                           |
|   Herding (collie-type) Collie, Aussie,      MDR1/ABCB1 mutation -> drug     |
|                         Sheltie              sensitivity (ivermectin etc).   |
+------------------------------------------------------------------------------+
```

### GDV (bloat) — the giant-breed emergency

Gastric dilatation-volvulus: the stomach fills with gas and then twists on its axis, cutting
off blood supply and trapping the gas. It is rapidly fatal without surgery.

```
   Deep-chested large breed, ate a big meal, exercised ->
   stomach distends with gas (dilatation) ->
   stomach ROTATES (volvulus) -> occludes blood vessels + esophagus ->
   shock, necrosis, death within hours.

   This is a TRUE surgical emergency. Prophylactic gastropexy (tacking the
   stomach to the body wall) is done in high-risk breeds to prevent the twist.
```

Contrast with the horse, which also gets fatal GI distension (colic) for analogous
anatomical reasons (file 01) — both are "a big mobile gut organ that can twist."

### Other common canine conditions

| Condition | What it is | Note |
|-----------|------------|------|
| Hip/elbow dysplasia | Malformed joint -> osteoarthritis | Heritable; large breeds; screened in breeding |
| Cruciate (CCL) rupture | Knee ligament tear | The canine analog of the human ACL; very common; surgical |
| Atopic dermatitis / allergies | Itchy skin, ear infections | Among the most common reasons for visits |
| Heart disease | Mitral valve degeneration (small breeds), DCM (large breeds) | Different lesions by breed size |
| Hypothyroidism | Underactive thyroid -> weight gain, coat changes | Common; treatable with levothyroxine |
| Cushing's / Addison's | Adrenal over-/under-function | Hormone disorders, like the human versions |

---

## The Cat — Obligate Carnivore, Stoic Patient

The cat's physiology (file 02) drives its disease profile, and its behavior (hiding illness)
drives its presentation: cats often arrive late and sick.

```
+------------------------------------------------------------------------------+
|                    THE FELINE "BIG FOUR" CHRONIC DISEASES                    |
|                                                                              |
|  CHRONIC KIDNEY DISEASE (CKD)   the #1 chronic illness of older cats.        |
|     kidneys lose concentrating ability -> increased thirst/urination,        |
|     weight loss, eventually uremia. Managed (diet, fluids), not cured.       |
|                                                                              |
|  HYPERTHYROIDISM                older cats; a benign thyroid tumor over-     |
|     produces hormone -> weight loss DESPITE ravenous appetite, hyper-        |
|     activity, fast heart. Treatable (methimazole, radioiodine, surgery).     |
|                                                                              |
|  DIABETES MELLITUS              often type-2-like, obesity-linked. Cats can  |
|     go into remission with early insulin + diet (unlike most dog diabetes,   |
|     which is usually permanent and insulin-dependent).                       |
|                                                                              |
|  FELINE LOWER URINARY TRACT DISEASE (FLUTD) / urethral obstruction           |
|     especially male cats: crystals/plugs block the narrow urethra ->         |
|     CANNOT URINATE -> rapidly fatal (potassium rises, bladder ruptures).     |
|     A "blocked tom" is a same-day emergency.                                 |
+------------------------------------------------------------------------------+
```

### Why cat dosing and toxins are different

Because the cat lacks robust glucuronidation (file 02, detailed in file 08), substances that
are mild in dogs or humans can be lethal in cats:

```
   NEVER give a cat:
     * Acetaminophen (paracetamol/Tylenol) -- causes methemoglobinemia and
       fatal liver injury; cats cannot conjugate it. A single tablet can kill.
     * Aspirin / many NSAIDs -- very narrow margin; toxic at "normal" doses.
     * Permethrin (a common DOG flea product) -- cats are highly sensitive;
       applying dog spot-on to a cat causes tremors/seizures/death.
     * Lilies (the plant) -- even small amounts of true lily cause acute,
       often fatal kidney failure in cats. Pollen, water from the vase count.
```

These are not dose-adjustment problems; they are species-incompatibility problems. The cat's
metabolic gaps make it the most toxicologically fragile common pet.

### Dog-specific toxins (the mirror image)

Dogs, being indiscriminate eaters, dominate poisoning cases:

| Toxin | Mechanism / effect | Note |
|-------|--------------------|----|
| **Chocolate** | Theobromine (a methylxanthine) — dogs metabolize it slowly | Dark/baking chocolate worst; cardiac + neuro |
| **Xylitol** (sugar-free gum/candy) | Triggers massive insulin release -> hypoglycemia; liver failure | Dog-specific; even small amounts dangerous |
| **Grapes / raisins** | Idiosyncratic acute kidney failure | Mechanism still not fully defined; avoid entirely |
| **Onions / garlic** | Oxidative damage to red cells -> Heinz-body anemia | Cats are especially sensitive |
| **Anticoagulant rodenticide** | Blocks vitamin K -> bleeding | Antidote is vitamin K1 |
| **Antifreeze (ethylene glycol)** | Metabolized to oxalate -> kidney failure | Sweet taste; cats and dogs; emergency |

**Old world -> new world bridge:** Think of each species as having a different "allowlist" of
safe inputs. Xylitol is on the human and dog-toxic list but processed differently; chocolate is
fine for humans, toxic for dogs because the clearance pathway is slow. You cannot assume an
input safe on one runtime is safe on another — the toxicology is per-species, not universal.

---

## Small Mammals — Where Husbandry Dominates

"Pocket pets" are not small dogs. Their physiology (often hindgut fermenters or short-gut
carnivores) makes them fragile, and most disease traces to husbandry and diet.

```
+-----------------------------------------------------------------------------+
|                    SMALL-MAMMAL ESSENTIALS                                  |
|                                                                             |
|  RABBIT (hindgut fermenter, prey species)                                   |
|    * GI STASIS: the gut stops moving (stress, pain, low-fiber diet) ->      |
|      a true emergency; rabbits can die from a "silent" gut shutdown.        |
|    * Ever-growing teeth -> malocclusion -> can't eat (file 01).             |
|    * Needs high-fiber (hay) diet; needs to eat its cecotropes (special      |
|      night feces) to recover nutrients.                                     |
|    * Extremely sensitive to many antibiotics (oral penicillins/             |
|      clindamycin wreck the gut flora -> fatal enterotoxemia).               |
|                                                                             |
|  GUINEA PIG                                                                 |
|    * Like primates and humans, CANNOT synthesize vitamin C -> needs         |
|      dietary vitamin C or develops scurvy.                                  |
|    * Also antibiotic-sensitive gut flora.                                   |
|                                                                             |
|  FERRET (obligate carnivore, short gut)                                     |
|    * Insulinoma (pancreatic tumor -> hypoglycemia) and adrenal disease      |
|      are very common in older ferrets.                                      |
|    * Females: induced ovulators -> unspayed jills risk fatal estrogen-      |
|      driven aplastic anemia (file 02).                                      |
|    * Susceptible to HUMAN influenza (and a classic flu research model).     |
|                                                                             |
|  HAMSTER / RAT / MOUSE                                                      |
|    * Short lifespans; tumors common (esp. mammary in rats).                 |
|   * "Wet tail" (proliferative ileitis) in hamsters -> often fatal diarrhea. |
+-----------------------------------------------------------------------------+
```

The unifying theme: in small mammals, the enclosure, diet, and a few species-specific traps
(rabbit antibiotic sensitivity, guinea pig vitamin C, ferret reproductive hormones) explain
most of medicine. "Husbandry is medicine" applies almost as strongly here as for reptiles.

---

## Preventive Care — The Core Schedule

Most companion-animal medicine is preventive. The backbone:

```
   CORE VACCINES
     Dog:  rabies (legally required in most places) + DAP
           (Distemper, Adenovirus/hepatitis, Parvovirus).
     Cat:  rabies + FVRCP (feline viral Rhinotracheitis, Calicivirus,
           Panleukopenia).
   NON-CORE (risk-based)
     Dog:  leptospirosis, Lyme, Bordetella ("kennel cough"), influenza.
     Cat:  FeLV (esp. outdoor cats).
   PARASITE PREVENTION
     Year-round flea/tick + monthly heartworm preventive (file 03).
   SPAY / NEUTER
     Population control + removes pyometra (uterine infection) risk,
     reduces some mammary/testicular cancers, behavioral effects.
   DENTAL + WEIGHT
     Periodontal disease and obesity are the two most under-treated
     chronic problems in pets.
```

Pyometra deserves a flag: an intact (unspayed) older female dog or cat can develop a
life-threatening pus-filled uterine infection. A sick intact female is pyometra until proven
otherwise — it is an emergency spay.

---

## Decision Cheat Sheet

| Presentation | Think first |
|--------------|-------------|
| Male cat straining, not producing urine | Urethral obstruction (blocked tom) — emergency |
| Deep-chested big dog, distended abdomen, retching | GDV/bloat — surgical emergency |
| Older cat: weight loss + huge appetite + hyperactive | Hyperthyroidism |
| Older cat: weight loss + increased thirst/urination | Chronic kidney disease |
| Dog ate sugar-free gum | Xylitol — hypoglycemia + liver failure |
| Dog ate dark chocolate | Theobromine toxicity |
| Cat exposed to lily / acetaminophen / dog flea product | Each is potentially fatal to cats |
| Rabbit stopped eating and passing stool | GI stasis — emergency |
| Intact older female dog, sick + vaginal discharge | Pyometra — emergency spay |
| Dachshund, sudden back pain or hind-limb weakness | IVDD (disc disease) |

---

## Common Confusion Points

### "What's safe for my dog is safe for my cat"

Dangerously false. Acetaminophen, many NSAIDs, permethrin flea products, and lilies are all
far more toxic — often lethal — to cats than to dogs, because of the feline glucuronidation
gap. Never extrapolate dog products or human medicines to cats.

### "Cats are low-maintenance and hide problems well — so no news is good news"

Cats are stoic and mask illness, so silence is not reassurance. The feline "big four" (CKD,
hyperthyroidism, diabetes, urinary obstruction) often present late. Subtle weight loss or
litter-box changes are real signals.

### "A rabbit is basically a small cat or dog to treat"

A rabbit is a hindgut-fermenting prey species with ever-growing teeth and antibiotic-sensitive
gut flora. GI stasis is a genuine emergency, and several common antibiotics are lethal. Small
mammals follow their own rules.

### "Spaying/neutering is just about population control"

It also prevents pyometra (a common, lethal uterine infection in intact females), reduces
mammary and testicular cancers, and removes the ferret/rabbit reproductive-hormone hazards.
The medical case is as strong as the population case. Production-scale medicine, where the
economics invert, is the subject of `06-LIVESTOCK-HEALTH.md`.
