---
maxim_schema: maxim.frontmatter.v1
id: maxim:veterinary-medicine:zoonoses-and-one-health
kind: guide
module: veterinary-medicine
section: veterinary-medicine
title: Zoonoses and One Health - The Human-Animal-Environment Interface
status: source-custody
source_custody: partial
current_path: veterinary-medicine/04-ZOONOSES-AND-ONE-HEALTH.md
canonical_path: veterinary-medicine/04-ZOONOSES-AND-ONE-HEALTH.md
backsource_ids: [proof-backfill:veterinary-medicine:04-zoonoses-and-one-health, git-history:veterinary-medicine:04-zoonoses-and-one-health]
concepts: [zoonoses, one health]
root_concepts: [zoonoses]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Zoonoses and One Health — The Human-Animal-Environment Interface

```
+------------------------------------------------------------------------------+
|                    THE SPILLOVER PIPELINE                                    |
|                                                                              |
|   RESERVOIR  ->  AMPLIFIER  ->  SPILLOVER  ->  HUMAN  ->  HUMAN-TO-HUMAN     |
|   (wildlife)     (livestock/    (the jump)     (index    (sustained          |
|                   bridge host)                  case)     transmission =     |
|                                                           epidemic/pandemic) |
|                                                                              |
|   bats, birds    pigs, poultry,  bite, aerosol, dead-end   the rare,         |
|   rodents,       camels, civets  contact, food, OR onward  catastrophic      |
|   primates                       vector       human spread step              |
|                                                                              |
|   STOP THE CHAIN EARLY (left) = far cheaper than stopping it late (right).   |
|   Veterinary surveillance watches the LEFT of this pipeline.                 |
+------------------------------------------------------------------------------+
```

**Read left to right.** A zoonosis is a disease that moves from animals to humans. Most do not
spread human-to-human and burn out (a "dead-end" infection like rabies in a person). The
dangerous ones acquire human-to-human transmission and become epidemics. The whole argument
for One Health is that the cheapest place to stop the pipeline is on the left — at the animal
reservoir — which is precisely where veterinary medicine operates.

**Systems Bridge:** Spillover is a cross-tenant escape in a multi-tenant system. A pathogen
"sandboxed" to one host species exploits a vulnerability (a shared receptor, a contact event)
to execute on a new host. Most escapes fail to propagate (dead-end). The catastrophic ones
achieve persistence (human-to-human transmission) and then it is a worm, not a single exploit.
Defense is the same as in security: monitor the boundary (the animal-human interface), reduce
attack surface (limit risky contact, wet markets, deforestation), and patch the reservoir
(vaccinate animals) rather than waiting to treat every infected human.

This file connects `03-INFECTIOUS-DISEASE.md` (the agents), `disease/` and `public-health/`
(human epidemiology), and `09-PUBLIC-HEALTH-ROLE.md` (surveillance and stewardship).

---

## The Quantitative Backbone

Two figures anchor the field:

```
   ~60%  of known human infectious diseases are ZOONOTIC in origin.
   ~75%  of NEW / EMERGING human infectious diseases are zoonotic.

   => Watching only human patients means you see emergence AFTER it
      has already crossed over. The animal reservoir is the leading
      indicator. This is the entire rationale for veterinary
      surveillance as pandemic defense.
```

The list of pandemics and major outbreaks with animal origins is long: HIV (primates),
influenza pandemics (birds/pigs), SARS (bats via civets), MERS (bats via camels), Ebola
(bats/primates), and COVID-19 (coronavirus of probable bat origin). The pattern is the rule,
not the exception.

---

## Directionality — It Is Not One-Way

```
+------------------------------------------------------------------------------+
|                  WHO INFECTS WHOM                                            |
|                                                                              |
|   ZOONOSIS              ANTHROPONOSIS / "REVERSE ZOONOSIS"                   |
|   animal -> human        human -> animal                                     |
|   --------------         ----------------                                    |
|   rabies (dog->human)    SARS-CoV-2 (human -> mink, white-tailed deer,       |
|   H5N1 (bird->human)        domestic cats, big cats in zoos)                 |
|   plague (rodent->human) human TB / influenza into great apes                |
|                                                                              |
|   SAPROZOONOSIS          VECTOR-BORNE                                        |
|   environment reservoir  arthropod intermediary                              |
|   ----------------       --------------------                                |
|   anthrax spores in soil  Lyme (tick), West Nile (mosquito),                 |
|   histoplasmosis (bird    plague (flea), Rift Valley fever                   |
|   droppings + soil)                                                          |
+------------------------------------------------------------------------------+
```

Reverse zoonosis matters more than people expect: when a human pathogen establishes in an
animal population (SARS-CoV-2 in white-tailed deer, in farmed mink), that population becomes a
*new reservoir* that can re-seed humans with mutated variants. The boundary is bidirectional,
which is why One Health insists on watching both directions.

---

## The Headline Zoonoses

### Rabies — the archetype

```
+--------------------------------------------------------------------------+
|                              RABIES                                      |
|                                                                          |
|   AGENT: Lyssavirus (rhabdovirus, bullet-shaped).                        |
|   RESERVOIR: dogs (most human deaths globally), plus bats, raccoons,     |
|              foxes, skunks depending on region.                          |
|   ROUTE: bite -> virus travels up PERIPHERAL NERVES to the brain         |
|          (retrograde axonal transport) -> fatal encephalitis.            |
|   KEY FACTS:                                                             |
|     * Once clinical signs appear, it is ~100% FATAL. Essentially no      |
|       survivors. This makes prevention everything.                       |
|     * Long, variable incubation (weeks to months) because the virus      |
|       must travel the nerves -> there is a window for POST-EXPOSURE      |
|       PROPHYLAXIS (wound care + vaccine + immunoglobulin) that           |
|       prevents disease if given before symptoms.                         |
|     * Vaccinating DOGS breaks the chain to humans. Mass dog              |
|       vaccination has eliminated dog-mediated human rabies in many       |
|       countries -- a textbook One Health win.                            |
+--------------------------------------------------------------------------+
```

Rabies is the canonical case: a ~100% fatal disease where the entire public-health strategy is
to immunize the *animal* reservoir, not to treat the human. Vaccinate ~70% of the dog
population and dog-mediated human rabies collapses. It is the cleanest demonstration that
animal health *is* human health.

### Influenza — the reassortment machine

Influenza A is the pandemic engine because its segmented genome can **reassort** when two
strains co-infect one host, swapping whole gene segments.

```
   WHY THE PIG IS THE "MIXING VESSEL"
   ----------------------------------
   Pig respiratory cells carry receptors for BOTH avian-type and
   human-type influenza. A pig co-infected with a bird flu and a human
   flu can let the two viruses swap genome segments (REASSORTMENT),
   producing a brand-new strain with human transmissibility + novel
   surface proteins humans have no immunity to. That is how some
   pandemic strains arise.

   H5N1 (highly pathogenic avian influenza):
     * Devastates poultry; spreads in wild birds globally.
     * Spills into humans (and recently dairy cattle and other mammals),
       with high case-fatality in the rare human cases.
     * The pandemic fear: a few mutations or a reassortment that grants
       efficient human-to-human spread. Hence intense surveillance of
       birds and pigs. (This is WHY poultry outbreaks trigger culls.)
```

The naming (H5N1, H1N1) refers to the surface proteins hemagglutinin (H) and neuraminidase
(N) — the same proteins drugs and vaccines target (`virology/`,
`medicine/02-ANTIVIRALS-VACCINES.md`). Surveillance of avian and swine influenza is one of the
most important standing One Health activities.

### Brucellosis — the slow occupational zoonosis

```
   AGENT: Brucella (B. abortus cattle, B. melitensis goats/sheep, B. suis pigs).
   ANIMAL DISEASE: late-term ABORTION storms, infertility.
   HUMAN DISEASE: "undulant fever" -- recurring fevers, sweats, joint pain;
                  chronic, debilitating, hard to clear.
   ROUTE TO HUMANS: contact with birthing fluids/aborted tissue (farmers,
                    vets, abattoir workers) and UNPASTEURIZED dairy.
   CONTROL: test-and-slaughter programs + animal vaccination have eradicated
            it from many national herds. A One Health success via the
            ANIMAL side.
```

### Other major zoonoses worth holding

| Disease | Animal source | Human route | Note |
|---------|---------------|-------------|------|
| **Bovine TB** (M. bovis) | Cattle (badgers as wildlife reservoir in UK) | Raw milk, aerosol | Why milk is pasteurized |
| **Leptospirosis** | Rodents, dogs, livestock | Urine-contaminated water | Flooding-associated outbreaks |
| **Plague** (Yersinia pestis) | Rodents | Flea bite | Still endemic in some regions |
| **Toxoplasmosis** | Cats (definitive host) | Oocysts in feces; undercooked meat | Fetal risk in pregnancy |
| **Salmonella / Campylobacter** | Poultry, reptiles, eggs | Food-borne; reptile handling | Leading bacterial food-borne illness |
| **Q fever** (Coxiella) | Sheep, goats, cattle | Aerosolized birthing fluids | Extremely infectious, environmentally tough |
| **Hantavirus** | Rodents (deer mice) | Aerosolized droppings/urine | Severe pulmonary syndrome |
| **Variant CJD** | Cattle (BSE prion) | Contaminated beef | The prion bridge (file 03) |

The toxoplasmosis row deserves precision because it is widely misstated: cats are the
definitive host that sheds oocysts, but most human exposure is also via undercooked meat. The
pregnancy advice (avoid the litter box, cook meat thoroughly) targets fresh oocysts and tissue
cysts — not the existence of a household cat.

---

## The Environmental Edge — Where Climate Enters

One Health is a *triad*, and the environment is the third node. Environmental change moves the
boundaries of the other two.

```
+------------------------------------------------------------------------------+
|              ENVIRONMENT -> ANIMAL -> HUMAN (worked drivers)                 |
|                                                                              |
|   DRIVER                 MECHANISM                  DISEASE EFFECT           |
|   ------                 ---------                  --------------           |
|   Warming                Tick/mosquito range and    Lyme, anaplasmosis,      |
|                          season expand poleward     West Nile, bluetongue    |
|                          and upward                 spread to new regions    |
|   Deforestation /        Wildlife pushed into        Spillover events        |
|   habitat encroachment   human/livestock contact     (Nipah, Ebola, novel    |
|                                                       coronaviruses)         |
|   Intensive livestock    High-density susceptible    Amplification +         |
|   farming                hosts in one place          reassortment (flu,      |
|                                                       AMR selection)         |
|   Wildlife trade /       Mixing of species that       SARS (civets), exotic  |
|   live ("wet") markets   never meet in nature        pet-borne zoonoses      |
|   Water / flooding       Pathogen + vector habitat    Lepto, Rift Valley     |
|                          expansion                    fever, mosquito-borne  |
+------------------------------------------------------------------------------+
```

This is why One Health is genuinely a *coupled* system, not three adjacent fields: you cannot
predict the animal-disease map without the climate and land-use map, and you cannot predict
human spillover without the animal-disease map.

---

## One Health In Practice — Who Does What

```
+------------------------------------------------------------------------------+
|                      THE ONE HEALTH OPERATING MODEL                          |
|                                                                              |
|   VETERINARIANS          PHYSICIANS / PUBLIC      ECOLOGISTS /               |
|                          HEALTH                   ENVIRONMENTAL SCI          |
|   ----------------       ------------------       -----------------          |
|   surveil animal         surveil human cases,     monitor habitat,           |
|   reservoirs, vaccinate  treat, contact-trace     vectors, climate,          |
|   livestock/pets,        humans                   reservoir ecology          |
|   inspect food                                                               |
|        \                       |                       /                     |
|         \                      |                      /                      |
|          +---- SHARED DATA, JOINT RESPONSE, EARLY WARNING ----+              |
|                                                                              |
|   Coordinating bodies (international): WHO (human), WOAH/OIE (animal),       |
|   FAO (food/agriculture), UNEP (environment) -- the "Quadripartite"          |
|   collaboration. National analog: linked human + veterinary + wildlife       |
|   agencies sharing surveillance.                                             |
+------------------------------------------------------------------------------+
```

**Old world -> new world bridge:** One Health is observability across a distributed system
with shared dashboards. Each team instruments its own service (human, animal, environment), but
the value is in the *correlated* telemetry — a spike in dead wild birds is an alert for the
human-flu on-call, not just the wildlife team. Siloed monitoring misses cross-service failures;
exactly the lesson of integrated tracing in microservices.

---

## Decision Cheat Sheet

| Situation | One Health response |
|-----------|---------------------|
| Bite from an unvaccinated/unknown dog | Post-exposure prophylaxis (rabies); the prevention is dog vaccination |
| Poultry mass die-off with neuro signs | Suspect HPAI/Newcastle; report, cull, surveil for human cases |
| Farmworkers with recurring fevers + cattle abortions | Suspect brucellosis; test-and-slaughter + animal vaccination |
| Pregnant household member + cat | Avoid handling fresh litter; cook meat; cat itself is low-risk |
| New tick-borne disease appearing further north | Climate-driven vector range shift; expand surveillance |
| Wildlife pushed into farms by deforestation | Spillover risk; interface management, not just treatment |
| Why pasteurize milk? | Kills M. bovis (TB), Brucella, Coxiella, etc. — animal-to-human dairy route |
| Why does animal vaccination protect people? | It removes the reservoir/amplifier on the LEFT of the spillover pipeline |

---

## Common Confusion Points

### "Zoonoses only go animal-to-human"

Reverse zoonosis (human-to-animal) is real and dangerous: SARS-CoV-2 established in mink and
white-tailed deer, creating new reservoirs that can re-infect humans with new variants. The
interface is bidirectional.

### "Getting a cat causes toxoplasmosis in pregnancy"

The risk is fresh oocysts shed in cat feces (and undercooked meat), not cat ownership.
Indoor cats fed cooked/commercial food rarely shed; the advice is litter-box and food-handling
hygiene, not rehoming the cat.

### "Bird flu is a poultry problem, not a human one"

H5N1 is mostly a poultry and wild-bird disease today, but its pandemic potential — via
mutation or reassortment (especially in pigs, the mixing vessel) toward efficient human spread
— is exactly why it is surveilled so intensely. The poultry cull is human-pandemic defense.

### "One Health is just a slogan for cooperation"

It is a structural claim: ~75% of emerging human diseases are zoonotic, so human-only
surveillance is a lagging indicator. Watching the animal and environmental subsystems is a
*leading* indicator, and several diseases (rabies, brucellosis, bovine TB) have been controlled
specifically by acting on the animal side. The public-mandate side is detailed in
`09-PUBLIC-HEALTH-ROLE.md`.
